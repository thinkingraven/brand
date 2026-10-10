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


def run(segments, size, tracking_px):
    """segments: [(text, wght, colour_key)]. Returns (paths, bounds) laid out from x=0 on baseline y=0."""
    x = 0.0
    paths, bounds = [], [float("inf"), float("inf"), float("-inf"), float("-inf")]
    for text, wght, colour in segments:
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
        d_parts = []
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            name = glyph_order[info.codepoint]
            ox, oy = x + pos.x_offset * s, -pos.y_offset * s
            t = (s, 0, 0, -s, ox, oy)
            pen = SVGPathPen(glyphset, lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
            glyphset[name].draw(TransformPen(pen, t))
            d_parts.append(pen.getCommands())
            bp = BoundsPen(glyphset)
            glyphset[name].draw(TransformPen(bp, t))
            if bp.bounds:
                bx0, by0, bx1, by1 = bp.bounds
                bounds = [min(bounds[0], bx0), min(bounds[1], by0), max(bounds[2], bx1), max(bounds[3], by1)]
            x += pos.x_advance * s + tracking_px
        paths.append((colour, " ".join(p for p in d_parts if p)))
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


# Wordmark: "thinking" regular, word space, "raven" bold, amber full stop (66 px master, -2 px tracking).
# The 0.30 em word space keeps the two words from reading as "thinkin graven" (round-2 decision, option A).
WORD_SPACE = 66 * 0.30
wm, wmb = run([("thinking", 400, "fg"), ("", WORD_SPACE, "gap"), ("raven", 700, "fg"), (".", 700, "amber")], 66, -2)
write("thinkingraven-wordmark-ink.svg", wm, wmb, INK, pad=6)
write("thinkingraven-wordmark-bone.svg", wm, wmb, BONE, pad=6)

# Monogram "tr." for icons and avatars.
mono, monob = run([("t", 400, "fg"), ("r", 700, "fg"), (".", 700, "amber")], 58, -2)
write("thinkingraven-monogram-ink.svg", mono, monob, INK, pad=4, title="Thinking Raven monogram")
write("thinkingraven-monogram-bone.svg", mono, monob, BONE, pad=4, title="Thinking Raven monogram")
# Square avatar/app tiles: artwork fills ~56% of the width so circular crops stay safe.
write("thinkingraven-avatar-dark.svg", mono, monob, BONE, pad=0, bg=INK, square=0.56, title="Thinking Raven")
write("thinkingraven-avatar-light.svg", mono, monob, INK, pad=0, bg=BONE, square=0.56, title="Thinking Raven")
