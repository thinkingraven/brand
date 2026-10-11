"""Convert the Thinking Raven wordmark and monogram to outlined SVG paths.

Usage: python -I outline.py <SpaceGrotesk-VF.ttf> <out_dir>
"""
import io
import sys
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

INK, BONE, AMBER = "#0F0F14", "#F3EFE6", "#F2A93B"
VF_PATH, OUT = Path(sys.argv[1]), Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)

_instances = {}


def instance(wght):
    if wght not in _instances:
        font = instancer.instantiateVariableFont(TTFont(VF_PATH), {"wght": wght})
        buf = io.BytesIO()
        font.save(buf)
        data = buf.getvalue()
        font = TTFont(io.BytesIO(data))
        _instances[wght] = (font, hb.Font(hb.Face(data)))
    return _instances[wght]


def shape(segments, size, tracking_px):
    """segments: [(text, wght, colour_key)]. Returns (glyphs, bounds) laid out from x=0 on baseline y=0.
    Each glyph is a dict: seg (index into segments), char, colour, d (outline path data) and x (its origin)."""
    x = 0.0
    glyphs, bounds = [], [float("inf"), float("inf"), float("-inf"), float("-inf")]
    for seg, (text, wght, colour) in enumerate(segments):
        if colour == "gap":  # explicit word space, in px (wght holds the width)
            x += wght
            continue
        font, hbfont = instance(wght)
        upem = font["head"].unitsPerEm
        s = size / upem
        glyph_order, glyphset = font.getGlyphOrder(), font.getGlyphSet()
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(hbfont, buf, {"kern": True, "liga": True})
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            name = glyph_order[info.codepoint]
            ox, oy = x + pos.x_offset * s, -pos.y_offset * s
            t = (s, 0, 0, -s, ox, oy)
            pen = SVGPathPen(glyphset, lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
            glyphset[name].draw(TransformPen(pen, t))
            bp = BoundsPen(glyphset)
            glyphset[name].draw(TransformPen(bp, t))
            if bp.bounds:
                bx0, by0, bx1, by1 = bp.bounds
                bounds = [min(bounds[0], bx0), min(bounds[1], by0), max(bounds[2], bx1), max(bounds[3], by1)]
            glyphs.append({"seg": seg, "char": text[info.cluster], "colour": colour, "d": pen.getCommands(), "x": ox})
            x += pos.x_advance * s + tracking_px
    return glyphs, bounds


def run(segments, size, tracking_px):
    """Like shape(), but returns (paths, bounds) with one path per segment."""
    glyphs, bounds = shape(segments, size, tracking_px)
    paths = []
    for seg, (_, _, colour) in enumerate(segments):
        if colour != "gap":
            paths.append((colour, " ".join(g["d"] for g in glyphs if g["seg"] == seg and g["d"])))
    return paths, bounds


def fill(colour_key, fg):
    return AMBER if colour_key == "amber" else fg


def write(name, paths, bounds, fg, pad, bg=None, square=None, title="Thinking Raven"):
    x0, y0, x1, y1 = bounds
    w, h = x1 - x0, y1 - y0
    if square:  # centre the artwork in a square canvas, artwork width = square fraction
        side = max(w, h) / square
        vx, vy, vw, vh = x0 - (side - w) / 2, y0 - (side - h) / 2, side, side
    else:
        vx, vy, vw, vh = x0 - pad, y0 - pad, w + 2 * pad, h + 2 * pad
    body = "".join(f'<path fill="{fill(c, fg)}" d="{d}"/>' for c, d in paths)
    bgrect = f'<rect x="{vx:.2f}" y="{vy:.2f}" width="{vw:.2f}" height="{vh:.2f}" fill="{bg}"/>' if bg else ""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx:.2f} {vy:.2f} {vw:.2f} {vh:.2f}" '
           f'role="img" aria-label="{title}"><title>{title}</title>{bgrect}{body}</svg>\n')
    (OUT / name).write_text(svg)
    print(f"{name}: {vw:.0f}x{vh:.0f}")


def write_morph(name, fg, pad=6):
    """The wordmark with one path per letter, carrying what a page needs to collapse it into the monogram.

    Every letter gets --tr-logo-dx, its move in wordmark units. Kept letters (t, r, full stop) move to where
    the monogram has them once it's scaled to the wordmark's letter size. The letters between two kept
    letters move in proportion to where they sit, so the gap closes like an accordion and nothing passes over
    anything; they also get --tr-logo-in and --tr-logo-out, their order when fading in and out (counted from
    the kept letter before them, and from the one after). The root gets --tr-logo-ratio (full width / height)
    and --tr-logo-mono (collapsed width as a fraction of the full width). Width changes crop from the right
    (preserveAspectRatio slice), so the letters never rescale. On its own, or as an <img>, it renders exactly
    like the wordmark. Reference CSS: .tr-logo-morph in css/components.css."""
    wm_glyphs, (x0, y0, x1, y1) = shape(WORDMARK, WORDMARK_SIZE, TRACKING)
    mono_glyphs, mono_bounds = shape(MONOGRAM, MONOGRAM_SIZE, TRACKING)
    k = WORDMARK_SIZE / MONOGRAM_SIZE
    vx, vy, vw, vh = x0 - pad, y0 - pad, x1 - x0 + 2 * pad, y1 - y0 + 2 * pad
    collapsed = (mono_bounds[2] * k + pad - vx) / vw

    # The monogram's letters are the first letter of each wordmark segment: t, r and the full stop.
    firsts = [next(g for g in wm_glyphs if g["seg"] == seg) for seg in sorted({g["seg"] for g in wm_glyphs})]
    assert [g["char"] for g in firsts] == [g["char"] for g in mono_glyphs] == ["t", "r", "."]
    dx = {id(w): k * m["x"] - w["x"] for w, m in zip(firsts, mono_glyphs)}
    kept = sorted(firsts, key=lambda g: g["x"])

    body = []
    for g in wm_glyphs:
        if not g["d"]:
            continue
        if id(g) in dx:
            move = dx[id(g)]
            order = ""
            cls = "tr-logo-morph__keep"
        else:
            a = max((w for w in kept if w["x"] < g["x"]), key=lambda w: w["x"])
            b = min((w for w in kept if w["x"] > g["x"]), key=lambda w: w["x"])
            move = dx[id(a)] + (dx[id(b)] - dx[id(a)]) * (g["x"] - a["x"]) / (b["x"] - a["x"])
            between = [w for w in wm_glyphs if a["x"] < w["x"] < b["x"] and w["d"]]
            i = between.index(g)
            order = f";--tr-logo-in:{i};--tr-logo-out:{len(between) - 1 - i}"
            cls = "tr-logo-morph__fade"
        style = f"--tr-logo-dx:{move:.2f}px{order}" if abs(move) >= 0.005 else order.lstrip(";")
        style = f' style="{style}"' if style else ""
        body.append(f'<path class="{cls}" data-glyph="{g["char"]}"{style} fill="{fill(g["colour"], fg)}" d="{g["d"]}"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx:.2f} {vy:.2f} {vw:.2f} {vh:.2f}" '
           f'preserveAspectRatio="xMinYMid slice" role="img" aria-label="Thinking Raven" class="tr-logo-morph" '
           f'style="--tr-logo-ratio:{vw / vh:.4f};--tr-logo-mono:{collapsed:.4f}">'
           f'<title>Thinking Raven</title>{"".join(body)}</svg>\n')
    (OUT / name).write_text(svg)
    print(f"{name}: {vw:.0f}x{vh:.0f}, collapses to {collapsed:.1%} of its width")


WORDMARK_SIZE, MONOGRAM_SIZE, TRACKING = 66, 58, -2

# Wordmark: "thinking" regular, word space, "raven" bold, amber full stop (66 px master, -2 px tracking).
# The 0.30 em word space keeps the two words from reading as "thinkin graven" (round-2 decision, option A).
WORD_SPACE = WORDMARK_SIZE * 0.30
WORDMARK = [("thinking", 400, "fg"), ("", WORD_SPACE, "gap"), ("raven", 700, "fg"), (".", 700, "amber")]
wm, wmb = run(WORDMARK, WORDMARK_SIZE, TRACKING)
write("thinkingraven-wordmark-ink.svg", wm, wmb, INK, pad=6)
write("thinkingraven-wordmark-bone.svg", wm, wmb, BONE, pad=6)

# Monogram "tr." for icons and avatars.
MONOGRAM = [("t", 400, "fg"), ("r", 700, "fg"), (".", 700, "amber")]
mono, monob = run(MONOGRAM, MONOGRAM_SIZE, TRACKING)
write("thinkingraven-monogram-ink.svg", mono, monob, INK, pad=4, title="Thinking Raven monogram")
write("thinkingraven-monogram-bone.svg", mono, monob, BONE, pad=4, title="Thinking Raven monogram")
# Square avatar/app tiles: artwork fills ~56% of the width so circular crops stay safe.
write("thinkingraven-avatar-dark.svg", mono, monob, BONE, pad=0, bg=INK, square=0.56, title="Thinking Raven")
write("thinkingraven-avatar-light.svg", mono, monob, INK, pad=0, bg=BONE, square=0.56, title="Thinking Raven")

# Logo morph: the wordmark that collapses to the monogram, for website navigation (see write_morph).
write_morph("thinkingraven-logo-morph-ink.svg", INK)
write_morph("thinkingraven-logo-morph-bone.svg", BONE)

# Product wordmarks: the product's name in lowercase Space Grotesk Bold with the amber full stop, set like the
# wordmark (66 px master, -2 px tracking). For product READMEs and sites; never the company logo.
PRODUCTS = ["rookery", "roost"]
for product in PRODUCTS:
    paths, bounds = run([(product, 700, "fg"), (".", 700, "amber")], WORDMARK_SIZE, TRACKING)
    write(f"{product}-wordmark-ink.svg", paths, bounds, INK, pad=4, title=product)
    write(f"{product}-wordmark-bone.svg", paths, bounds, BONE, pad=4, title=product)
