"""Write mascot SVGs, then export every PNG/ICO size for the Thinking Raven brand kit.

Usage: python3 export.py <brand_dir> <work_dir>
"""
import shutil
import struct
import subprocess
import sys
import time
from pathlib import Path

BRAND, WORK = Path(sys.argv[1]), Path(sys.argv[2])
FINAL, EXP = BRAND / "logos" / "final", BRAND / "exports"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
INK, BONE, AMBER, MUTE = "#0F0F14", "#F3EFE6", "#F2A93B", "#9A9AA8"
for d in (EXP / "favicon", EXP / "social", EXP / "app", EXP / "wordmark", WORK):
    d.mkdir(parents=True, exist_ok=True)

# ---------- mascot SVGs (same drawing as concept 09) ----------
RAVEN = (f'<ellipse cx="50" cy="68" rx="25" ry="22" fill="{INK}"/><circle cx="50" cy="42" r="21" fill="{INK}"/>'
         f'<path d="M33 63 Q28 78 42 86 Q38 74 33 63 Z" fill="#2B2B36"/>'
         f'<path d="M44 89 v5 M56 89 v5" stroke="{AMBER}" stroke-width="3" stroke-linecap="round"/>'
         f'<path d="M68.5 40 L83 44.5 L68.5 49 Z" fill="{AMBER}"/><circle cx="57" cy="39" r="7.5" fill="#FFFFFF"/>'
         f'<circle cx="59" cy="39.5" r="3.8" fill="{INK}"/><circle cx="60.5" cy="37.8" r="1.2" fill="#FFFFFF"/>'
         f'<circle cx="75" cy="21" r="2.2" fill="{AMBER}"/><circle cx="81.5" cy="14" r="3" fill="{AMBER}"/>'
         f'<circle cx="89.5" cy="7.5" r="3.8" fill="{AMBER}"/>')
mascots = {
    "thinky-mascot-app.svg": f'<rect width="100" height="100" fill="{BONE}"/>{RAVEN}',            # App Store: square, opaque
    "thinky-mascot-rounded.svg": f'<rect width="100" height="100" rx="22" fill="{BONE}"/>{RAVEN}',
    "thinky-mascot-amber.svg": f'<rect width="100" height="100" fill="{AMBER}"/>{RAVEN.replace(AMBER, BONE)}',
    "thinky-mascot-transparent.svg": RAVEN,
}
for name, body in mascots.items():
    (FINAL / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" '
                              f'aria-label="Thinky, the Thinking Raven mascot"><title>Thinky</title>{body}</svg>\n')
shutil.copy(FINAL / "thinkingraven-avatar-dark.svg", EXP / "favicon" / "favicon.svg")


# ---------- rendering ----------
def shot(out, w, h, html_body, bg="transparent"):
    page = WORK / f"{out.stem}.html"
    page.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;width:{w}px;height:{h}px;'
                    f'background:{bg};overflow:hidden}}body{{display:grid;place-items:center}}img{{display:block}}</style>'
                    f'</head><body>{html_body}</body></html>')
    if out.exists():
        out.unlink()
    # Headless Chrome writes the screenshot but sometimes never exits, so wait for the file and stop it ourselves.
    proc = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--no-first-run", "--hide-scrollbars",
                             f"--user-data-dir={WORK / 'chrome'}", "--default-background-color=00000000",
                             "--virtual-time-budget=3000", f"--window-size={w},{h}", f"--screenshot={out}", page.as_uri()],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    last = -1
    for _ in range(120):
        time.sleep(0.5)
        size = out.stat().st_size if out.exists() else 0
        if size and size == last:
            break
        last = size
    proc.terminate()
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
    if not out.exists():
        raise SystemExit(f"screenshot failed: {out}")
    print(f"{out.relative_to(BRAND) if BRAND in out.parents else out.name}  {w}x{h}")


def img(svg, style="width:100%;height:100%"):
    return f'<img src="{(FINAL / svg).as_uri()}" style="{style}">'


def resize(src, dst, size):
    subprocess.run(["sips", "-z", str(size), str(size), str(src), "--out", str(dst)], check=True, stdout=subprocess.DEVNULL)
    print(f"{dst.relative_to(BRAND)}  {size}x{size}")


# Square icons: render once large, then downscale.
master = WORK / "avatar-1024.png"
shot(master, 1024, 1024, img("thinkingraven-avatar-dark.svg"))
for size, name in [(16, "favicon/favicon-16.png"), (32, "favicon/favicon-32.png"), (48, "favicon/favicon-48.png"),
                   (180, "favicon/apple-touch-icon.png"), (192, "favicon/icon-192.png"), (512, "favicon/icon-512.png"),
                   (400, "social/x-avatar-400.png"), (400, "social/linkedin-logo-400.png"),
                   (500, "social/github-avatar-500.png"), (800, "social/youtube-avatar-800.png")]:
    resize(master, EXP / name, size)
shutil.copy(master, EXP / "social" / "instagram-avatar-1080.png")
resize(master, EXP / "social" / "instagram-avatar-1080.png", 1080)
light = WORK / "avatar-light-1024.png"
shot(light, 1024, 1024, img("thinkingraven-avatar-light.svg"))
resize(light, EXP / "social" / "avatar-light-1000.png", 1000)

# favicon.ico with embedded PNGs (16, 32, 48).
pngs = [(s, (EXP / f"favicon/favicon-{s}.png").read_bytes()) for s in (16, 32, 48)]
header = struct.pack("<HHH", 0, 1, len(pngs))
offset, entries, blobs = 6 + 16 * len(pngs), b"", b""
for s, data in pngs:
    entries += struct.pack("<BBBBHHII", s, s, 0, 0, 1, 32, len(data), offset)
    offset += len(data)
    blobs += data
(EXP / "favicon" / "favicon.ico").write_bytes(header + entries + blobs)
print("exports/favicon/favicon.ico  16+32+48")

# Banners and covers: dark background, centred bone wordmark.
wm = lambda pct: img("thinkingraven-wordmark-bone.svg", f"width:{pct}%;height:auto")
shot(EXP / "social" / "x-header-1500x500.png", 1500, 500, wm(42), INK)
shot(EXP / "social" / "linkedin-cover-1128x191.png", 1128, 191, wm(38), INK)
shot(EXP / "social" / "youtube-banner-2560x1440.png", 2560, 1440, wm(34), INK)
shot(EXP / "social" / "og-image-1200x630.png", 1200, 630,
     f'<div style="display:grid;justify-items:center;gap:30px;font-family:-apple-system,Helvetica,Arial,sans-serif">'
     f'{wm(100).replace("width:100%", "width:640px")}'
     f'<div style="color:{MUTE};font-size:30px;letter-spacing:.01em">AI that thinks before it speaks.</div>'
     f'<div style="color:{AMBER};font-size:22px;letter-spacing:.12em">THINKINGRAVEN.COM</div></div>', INK)

# Wordmarks (transparent) and email signature logo.
shot(EXP / "wordmark" / "wordmark-ink-2000.png", 2000, 330, img("thinkingraven-wordmark-ink.svg", "width:100%;height:auto"))
shot(EXP / "wordmark" / "wordmark-bone-2000.png", 2000, 330, img("thinkingraven-wordmark-bone.svg", "width:100%;height:auto"))
shot(EXP / "wordmark" / "email-signature-600.png", 600, 100, img("thinkingraven-wordmark-ink.svg", "width:100%;height:auto"))

# Mascot / app icon.
shot(EXP / "app" / "thinky-app-icon-1024.png", 1024, 1024, img("thinky-mascot-app.svg"), BONE)
shot(EXP / "app" / "thinky-rounded-1024.png", 1024, 1024, img("thinky-mascot-rounded.svg"))
shot(EXP / "app" / "thinky-transparent-1024.png", 1024, 1024, img("thinky-mascot-transparent.svg"))
shot(EXP / "app" / "thinky-amber-1024.png", 1024, 1024, img("thinky-mascot-amber.svg"))
