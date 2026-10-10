"""Round-2 wordmark exploration: variants that keep "thinking" and "raven" visually separate.

Usage: python -I wordmark_v2.py <brand_dir> <board_html>
Needs fonttools + uharfbuzz. Writes SVGs to archive/round-2-wordmark/ and a review board.
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

BRAND, BOARD = Path(sys.argv[1]), Path(sys.argv[2])
OUT = BRAND / "archive" / "round-2-wordmark"
OUT.mkdir(parents=True, exist_ok=True)
FONTS = BRAND / "fonts"
INK, BONE, AMBER = "#0F0F14", "#F3EFE6", "#F2A93B"
MUTE_LIGHT, MUTE_DARK = "#6A6A75", "#8A8A98"

_cache = {}


def font(key):
    """key: ('sg', wght) for Space Grotesk instances, ('sm', 400|700) for Space Mono."""
    if key not in _cache:
        if key[0] == "sg":
            f = instancer.instantiateVariableFont(TTFont(FONTS / "SpaceGrotesk-VF.ttf"), {"wght": key[1]})
            buf = io.BytesIO()
            f.save(buf)
            data = buf.getvalue()
        else:
            data = (FONTS / ("SpaceMono-Bold.ttf" if key[1] == 700 else "SpaceMono-Regular.ttf")).read_bytes()
        tt = TTFont(io.BytesIO(data))
        _cache[key] = (tt, hb.Font(hb.Face(data)))
    return _cache[key]


def xheight(key):
    tt, _ = font(key)
    return tt["OS/2"].sxHeight / tt["head"].unitsPerEm


def shape(text, key, size, x, y, tracking=0.0):
    tt, hbf = font(key)
    s = size / tt["head"].unitsPerEm
    order, gs = tt.getGlyphOrder(), tt.getGlyphSet()
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(hbf, buf, {"kern": True, "liga": True})
    parts, bounds = [], None
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        t = (s, 0, 0, -s, x + pos.x_offset * s, y - pos.y_offset * s)
        pen = SVGPathPen(gs, lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
        gs[order[info.codepoint]].draw(TransformPen(pen, t))
        parts.append(pen.getCommands())
        bp = BoundsPen(gs)
        gs[order[info.codepoint]].draw(TransformPen(bp, t))
        if bp.bounds:
            bounds = bp.bounds if bounds is None else (min(bounds[0], bp.bounds[0]), min(bounds[1], bp.bounds[1]),
                                                      max(bounds[2], bp.bounds[2]), max(bounds[3], bp.bounds[3]))
        x += pos.x_advance * s + tracking
    return " ".join(p for p in parts if p), bounds, x


class Mark:
    def __init__(self):
        self.items, self.bounds = [], None

    def add(self, kind, data, colour, bounds):
        self.items.append((kind, data, colour))
        b = bounds
        self.bounds = b if self.bounds is None else (min(self.bounds[0], b[0]), min(self.bounds[1], b[1]),
                                                     max(self.bounds[2], b[2]), max(self.bounds[3], b[3]))

    def text(self, text, key, size, x, y, colour, tracking=0.0):
        d, b, nx = shape(text, key, size, x, y, tracking)
        self.add("path", d, colour, b)
        return nx

    def dot(self, cx, cy, r, colour):
        self.add("circle", (cx, cy, r), colour, (cx - r, cy - r, cx + r, cy + r))

    def svg(self, fg, muted, pad=6, title="Thinking Raven"):
        x0, y0, x1, y1 = self.bounds
        vx, vy, vw, vh = x0 - pad, y0 - pad, x1 - x0 + 2 * pad, y1 - y0 + 2 * pad
        col = {"fg": fg, "muted": muted, "amber": AMBER}
        body = ""
        for kind, data, c in self.items:
            if kind == "path":
                body += f'<path fill="{col[c]}" d="{data}"/>'
            else:
                body += f'<circle fill="{col[c]}" cx="{data[0]:.2f}" cy="{data[1]:.2f}" r="{data[2]:.2f}"/>'
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx:.2f} {vy:.2f} {vw:.2f} {vh:.2f}" role="img" '
                f'aria-label="{title}"><title>{title}</title>{body}</svg>')


SIZE, TRACK = 66, -2
SG4, SG7, SM4 = ("sg", 400), ("sg", 700), ("sm", 400)
SPACE = SIZE * 0.30  # a clear word space

variants = []

m = Mark()
x = m.text("thinking", SG4, SIZE, 0, 0, "fg", TRACK)
x = m.text("raven.", SG7, SIZE, x + SPACE, 0, "fg", TRACK)
# recolour the final full stop amber by re-drawing it on top
m2 = Mark(); x2 = m2.text("thinking", SG4, SIZE, 0, 0, "fg", TRACK); x2 = m2.text("raven", SG7, SIZE, x2 + SPACE, 0, "fg", TRACK); m2.text(".", SG7, SIZE, x2 + TRACK, 0, "amber")
variants.append(("A", "Word space", "The current wordmark with a real space. The smallest possible change: still minimal, and \"graven\" is gone.", m2))

m = Mark(); x = m.text("thinking", SG4, SIZE, 0, 0, "muted", TRACK); x = m.text("raven", SG7, SIZE, x + SPACE, 0, "fg", TRACK); m.text(".", SG7, SIZE, x + TRACK, 0, "amber")
variants.append(("B", "Space + tone", "\"thinking\" steps back in a softer tone and \"raven.\" leads, so the words separate by space, weight and tone. The eye lands on \"raven\" first.", m))

m = Mark(); x = m.text("thinking", SG4, SIZE, 0, 0, "fg", TRACK)
r = SIZE * 0.085; gap = SIZE * 0.36
m.dot(x + gap / 2 - TRACK / 2, -xheight(SG4) * SIZE / 2, r, "amber")
m.text("raven", SG7, SIZE, x + gap, 0, "fg", TRACK)
variants.append(("C", "Amber dot separator", "The raven's eye moves between the words: thinking·raven. One dot, one meaning: the thought lands, then the raven speaks. No full stop.", m))

m = Mark(); m.text("thinking", SG4, SIZE, 0, 0, "fg", TRACK); x = m.text("raven", SG7, SIZE, 0, SIZE * 0.92, "fg", TRACK); m.text(".", SG7, SIZE, x + TRACK, SIZE * 0.92, "amber")
variants.append(("D", "Stacked", "Two lines that can never merge. Compact and square-friendly: ideal for avatars, app splash screens, stickers and social headers.", m))

scale = xheight(SG4) / xheight(SM4)
m = Mark(); x = m.text("thinking", SM4, SIZE * scale, 0, 0, "fg", -1); x = m.text("raven", SG7, SIZE, x + SIZE * 0.26, 0, "fg", TRACK); m.text(".", SG7, SIZE, x + TRACK, 0, "amber")
variants.append(("E", "Mono + bold", "\"thinking\" in Space Mono (machine-like: the process) and \"raven.\" in Grotesk Bold (the answer). Two faces tell the story and the words can't blend.", m))

m = Mark(); x = m.text("Thinking", SG4, SIZE, 0, 0, "fg", TRACK); x = m.text("Raven", SG7, SIZE, x + SPACE, 0, "fg", TRACK); m.text(".", SG7, SIZE, x + TRACK, 0, "amber")
variants.append(("F", "Title case", "Capitals mark each word boundary: Thinking Raven. The most literal and most readable option, and a little more formal.", m))

for vid, name, _, mk in variants:
    slug = name.lower().replace(" + ", "-").replace(" ", "-")
    (OUT / f"{vid}-{slug}-ink.svg").write_text(mk.svg(INK, MUTE_LIGHT) + "\n")
    (OUT / f"{vid}-{slug}-bone.svg").write_text(mk.svg(BONE, MUTE_DARK) + "\n")

current = Mark(); x = current.text("thinking", SG4, SIZE, 0, 0, "fg", TRACK); x = current.text("raven", SG7, SIZE, x, 0, "fg", TRACK); current.text(".", SG7, SIZE, x + TRACK, 0, "amber")


def card(vid, name, why, mk, is_current=False):
    ink, bone = mk.svg(INK, MUTE_LIGHT), mk.svg(BONE, MUTE_DARK)
    pick = "" if is_current else f'<label class="pick"><input type="radio" name="pick" value="{vid} {name}" form="picks"> Choose</label>'
    return f'''
  <article class="card{' current' if is_current else ''}">
    <header><div><span class="vid">{vid}</span><h2>{name}</h2></div>{pick}</header>
    <p class="why">{why}</p>
    <div class="hero dark">{bone}</div>
    <div class="row">
      <div class="tile light">{ink}</div>
      <div class="tile glance light" title="Glance test: blurred, as seen in a quick scroll">{ink}<span>glance test</span></div>
    </div>
    <div class="row small">
      <div class="nav light"><span class="navlogo">{ink}</span><span class="links">Product · Pricing · Docs</span></div>
      <div class="nav dark"><span class="navlogo">{bone}</span><span class="links">Product · Pricing · Docs</span></div>
    </div>
  </article>'''


cards = card("Now", "Current: no space", "For comparison. At a glance the bold \"r\" joins the \"g\" and it reads \"thinkin graven\".", current, True)
cards += "".join(card(*v) for v in variants)
BOARD.write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wordmark Round 2</title>
<style>
  @font-face {{ font-family: "Space Grotesk"; src: url("SpaceGrotesk-VF.ttf"); font-weight: 300 700; }}
  :root {{ --ink:{INK}; --bone:{BONE}; --amber:{AMBER}; }}
  *,*::before,*::after {{ box-sizing:border-box; }}
  body {{ margin:0; background:#09090C; color:var(--bone); font-family:"Space Grotesk", Helvetica, Arial, sans-serif; }}
  main {{ max-width:1180px; margin:0 auto; padding:40px 16px 80px; }}
  .kicker {{ color:var(--amber); letter-spacing:.16em; text-transform:uppercase; font-size:12px; font-weight:600; }}
  h1 {{ font-size:clamp(28px,4.5vw,46px); letter-spacing:-.02em; margin:.2em 0 .3em; }}
  .lead {{ color:#9A9AA8; max-width:780px; line-height:1.55; }}
  .grid {{ display:grid; gap:20px; grid-template-columns:repeat(auto-fill,minmax(min(100%,520px),1fr)); margin-top:28px; }}
  .card {{ background:#14141A; border:1px solid #25252E; border-radius:18px; padding:20px; min-width:0; }}
  .card.current {{ border-color:#5a2a2a; }}
  .card header {{ display:flex; justify-content:space-between; align-items:center; gap:12px; }}
  .card header div {{ display:flex; align-items:center; gap:10px; }}
  .vid {{ font-size:12px; color:#111; background:var(--amber); border-radius:999px; padding:2px 9px; font-weight:700; }}
  .current .vid {{ background:#ff7b72; }}
  h2 {{ margin:0; font-size:20px; }}
  .pick {{ font-size:13px; color:#9A9AA8; cursor:pointer; }} .pick input {{ accent-color:var(--amber); }}
  .why {{ color:#C9C7C0; font-size:14px; line-height:1.55; margin:10px 0 14px; }}
  .hero {{ border-radius:14px; padding:34px 28px; display:grid; place-items:center; }}
  .hero svg {{ width:100%; max-width:420px; height:auto; max-height:130px; }}
  .dark {{ background:var(--ink); border:1px solid #25252E; }} .light {{ background:var(--bone); }}
  .row {{ display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:12px; }}
  .tile {{ border-radius:12px; padding:18px; display:grid; place-items:center; position:relative; min-height:96px; }}
  .tile svg {{ width:100%; max-width:220px; height:auto; max-height:70px; }}
  .glance svg {{ filter:blur(1.6px); max-width:130px; }}
  .glance span {{ position:absolute; bottom:6px; right:10px; font-size:10px; color:#6A6A75; letter-spacing:.08em; text-transform:uppercase; }}
  .nav {{ border-radius:10px; padding:10px 14px; display:flex; align-items:center; justify-content:space-between; gap:10px; min-width:0; }}
  .navlogo svg {{ height:18px; width:auto; display:block; }}
  .nav .links {{ font-size:11px; color:#6A6A75; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
  .nav.dark .links {{ color:#8A8A98; }}
  form {{ margin-top:30px; background:#14141A; border:1px solid #25252E; border-radius:18px; padding:20px; display:grid; gap:12px; }}
  textarea {{ width:100%; background:#0d0d11; color:var(--bone); border:1px solid #25252E; border-radius:10px; padding:10px; font:inherit; }}
  button {{ justify-self:start; background:var(--amber); color:#111; border:0; border-radius:999px; padding:10px 18px; font:600 14px inherit; cursor:pointer; }}
  #status {{ color:#9A9AA8; font-size:13px; }}
</style></head><body><main>
  <p class="kicker">Thinking Raven · wordmark · round 2</p>
  <h1>Keep it minimal, make it unmistakable</h1>
  <p class="lead">The current wordmark can read as "thinkin graven" at a glance. Each option below keeps the same font, palette and quiet feel, but separates the two words. Every card shows the logo on dark and light, a <b>glance test</b> (blurred and small, like a quick scroll), and the logo in a nav bar at 18 px.</p>
  <section class="grid">{cards}</section>
  <form id="picks" data-lavish-question="wordmark-v2" onsubmit="event.preventDefault();
    const pick=(document.querySelector('input[name=pick]:checked')||{{}}).value||'';
    const notes=(this.notes.value||'').trim();
    if(!pick&&!notes){{document.getElementById('status').textContent='Choose a variant or add a note.';return;}}
    const msg='Wordmark round 2 pick: '+(pick||'none')+(notes?'. Notes: '+notes:'');
    document.getElementById('status').textContent='Queued: '+msg;
    if(window.lavish) window.lavish.queuePrompt(msg,{{tag:'choice',text:msg,element:this,queueKey:'wordmark-v2',data:{{pick,notes}}}});">
    <h2>Your pick</h2>
    <textarea name="notes" rows="2" placeholder="Optional: e.g. 'A but with B's softer thinking', or 'C as primary, D for avatars'"></textarea>
    <button type="submit">Queue my pick</button><span id="status" role="status" aria-live="polite"></span>
  </form>
</main></body></html>''')
import shutil
shutil.copy(FONTS / "SpaceGrotesk-VF.ttf", BOARD.parent / "SpaceGrotesk-VF.ttf")
print(f"Wrote {len(variants)} variants to {OUT}\nBoard: {BOARD}")
