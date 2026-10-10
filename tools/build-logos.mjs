// Generates the Thinking Raven logo concepts as SVG files plus a review board.
// Usage: node tools/build-logos.mjs [board-output.html]
import { writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const OUT = join(ROOT, 'archive', 'round-1-concepts');
const BOARD = process.argv[2] || join(ROOT, 'archive', 'round-1-board.html');

const INK = '#0F0F14';
const BONE = '#F3EFE6';
const AMBER = '#F2A93B';
const SANS = "'Space Grotesk', 'Helvetica Neue', Arial, sans-serif";
const SERIF = "'Instrument Serif', Georgia, serif";
const HEAVY = "'Archivo Black', 'Arial Black', sans-serif";
const FONT_CSS = 'https://fonts.googleapis.com/css2?family=Archivo+Black&family=Instrument+Serif:ital@0;1&family=Space+Grotesk:wght@400;500;600;700&display=swap';

let uid = 0;

// Raven head that doubles as a speech bubble: a circle with a beak-shaped tail.
const headPath = 'M62.4 32 L95 49 Q93.5 53.2 88.5 54 L70.9 62 A30 30 0 1 1 62.4 32 Z';
const head = (fg) => `<path d="${headPath}" fill="${fg}"/><circle cx="54" cy="46" r="5.5" fill="${AMBER}"/>`;

const concepts = [
  {
    id: '01', slug: 'wordmark-sans', name: 'Modern wordmark', type: 'Text',
    story: 'Lowercase geometric sans. "thinking" is light and "raven" is bold, and the amber full stop is the raven\'s eye, the thought landing. Quiet, confident, very usable.',
    vb: '0 0 100 100',
    icon: (fg) => `<text x="50" y="68" text-anchor="middle" font-family="${SANS}" font-size="58" letter-spacing="-2" fill="${fg}"><tspan font-weight="400">t</tspan><tspan font-weight="700">r</tspan><tspan font-weight="700" fill="${AMBER}">.</tspan></text>`,
    wordmark: { vb: '0 0 560 100', draw: (fg) => `<text x="6" y="68" font-family="${SANS}" font-size="66" letter-spacing="-2" fill="${fg}"><tspan font-weight="400">thinking</tspan><tspan font-weight="700">raven</tspan><tspan font-weight="700" fill="${AMBER}">.</tspan></text>` },
  },
  {
    id: '02', slug: 'wordmark-serif', name: 'Editorial wordmark', type: 'Text',
    story: 'A high-contrast serif with an italic "Raven". Feels like a literary imprint or a research institute: timeless, calm and expensive.',
    vb: '0 0 100 100',
    icon: (fg) => `<text x="50" y="69" text-anchor="middle" font-family="${SERIF}" font-size="60" fill="${fg}">T<tspan font-style="italic">r</tspan><tspan fill="${AMBER}">.</tspan></text>`,
    wordmark: { vb: '0 0 560 100', draw: (fg) => `<text x="4" y="72" font-family="${SERIF}" font-size="80" fill="${fg}">Thinking <tspan font-style="italic">Raven</tspan><tspan fill="${AMBER}">.</tspan></text>` },
  },
  {
    id: '03', slug: 'speaking-raven', name: 'Speaking raven', type: 'Minimalist',
    story: 'One shape with two readings: a raven\'s head, and a speech bubble whose tail is the beak. That\'s "thinks before it speaks" in a single mark. Still legible at 16 px.',
    vb: '0 0 100 100',
    icon: (fg) => `<g transform="translate(-3.5 -4)">${head(fg)}</g>`,
  },
  {
    id: '04', slug: 'r-lettermark', name: 'R lettermark', type: 'Lettermark',
    story: 'A bold "R" whose bowl is the raven\'s head: the counter becomes the amber eye, and a beak breaks out of the curve. Reads as a letter first and a bird second.',
    vb: '0 0 100 100',
    icon: (fg) => `<g transform="translate(-6 0)" fill="${fg}"><rect x="18" y="16" width="15" height="68"/><path d="M33 16 H52 A21 21 0 0 1 52 58 H33 Z"/><path d="M70 28 L94 37 L70 46 Z"/><path d="M40 58 L57 58 L78 84 L61 84 Z"/><circle cx="51" cy="37" r="6" fill="${AMBER}"/></g>`,
  },
  {
    id: '05', slug: 'thinking-dots', name: 'Thinking dots', type: 'AI-native',
    story: 'Every AI chat shows "• • •" while it thinks. Here the third dot hatches into the raven. Instantly readable as AI, and it animates naturally in a loading state.',
    vb: '0 0 100 100',
    icon: (fg) => `<g transform="translate(-2 -8)"><circle cx="13" cy="62" r="6" fill="${fg}" opacity=".35"/><circle cx="30" cy="62" r="6" fill="${fg}" opacity=".65"/><path d="M76 46 L97 55 Q95.5 58.2 92 58.6 L78.3 66 A20 20 0 1 1 76 46 Z" fill="${fg}"/><circle cx="67" cy="52" r="4" fill="${AMBER}"/></g>`,
  },
  {
    id: '06', slug: 'in-your-face', name: 'Amber block', type: 'In your face',
    story: 'A full-bleed amber square with a giant cropped raven staring out of it, plus a heavy stacked wordmark. Built to stop the thumb in an X or LinkedIn feed.',
    vb: '0 0 100 100', fixedBg: true,
    icon: () => `<rect width="100" height="100" fill="${AMBER}"/><path d="M68.2 34 L99 53 L81.3 74 A44 44 0 1 1 68.2 34 Z" fill="${INK}"/><circle cx="57" cy="49" r="7" fill="${BONE}"/>`,
    wordmark: { vb: '0 0 420 150', draw: (fg) => `<text x="2" y="30" font-family="${HEAVY}" font-size="30" letter-spacing="10" textLength="408" lengthAdjust="spacing" fill="${fg}">THINKING</text><rect x="0" y="44" width="420" height="104" fill="${AMBER}"/><text x="10" y="134" font-family="${HEAVY}" font-size="100" textLength="400" lengthAdjust="spacingAndGlyphs" fill="${INK}">RAVEN</text>` },
  },
  {
    id: '07', slug: 'seal', name: 'Huginn seal', type: 'Emblem',
    story: 'A circular seal with the raven inside and "THOUGHT & MEMORY" around it, after Odin\'s ravens Huginn and Muninn. Heritage feel; great for stickers, merch and the "about" page.',
    vb: '0 0 200 200',
    icon: (fg) => {
      const id = `ring${++uid}`;
      return `<defs><path id="${id}" d="M100 100 m-77 0 a77 77 0 1 1 154 0 a77 77 0 1 1 -154 0"/></defs><circle cx="100" cy="100" r="95" fill="none" stroke="${fg}" stroke-width="5"/><circle cx="100" cy="100" r="66" fill="none" stroke="${fg}" stroke-width="1.5"/><text font-family="${SANS}" font-weight="700" font-size="14" fill="${fg}"><textPath href="#${id}" textLength="480" lengthAdjust="spacing">THINKING RAVEN • THOUGHT &amp; MEMORY •</textPath></text><g transform="translate(100 102) scale(1.02) translate(-53.5 -54)">${head(fg)}</g>`;
    },
  },
  {
    id: '08', slug: 'thought-memory', name: 'Thought & Memory', type: 'Abstract',
    story: 'Huginn ("thought") and Muninn ("memory") as two interlocking raven heads, turned 180° like a yin-yang. One eye glows amber, the other is negative space.',
    vb: '0 0 100 100',
    icon: (fg, bg) => {
      const h = 'M52.3 24 L76 35 L56.3 46 A20 20 0 1 1 52.3 24 Z';
      return `<path d="${h}" fill="${fg}"/><circle cx="45" cy="33" r="3.6" fill="${AMBER}"/><g transform="rotate(180 50 50)"><path d="${h}" fill="${fg}" stroke="${bg}" stroke-width="3.5" paint-order="stroke"/><circle cx="45" cy="33" r="3.6" fill="${bg}"/></g>`;
    },
  },
  {
    id: '09', slug: 'mascot', name: '"Thinky" mascot', type: 'Mascot',
    story: 'A friendly raven with a big curious eye and three thought bubbles rising. It gives the brand a face for the app icon, onboarding and stickers, while the serious marks carry the name.',
    vb: '0 0 100 100', fixedBg: true,
    icon: () => `<rect width="100" height="100" rx="22" fill="${BONE}"/><ellipse cx="50" cy="68" rx="25" ry="22" fill="${INK}"/><circle cx="50" cy="42" r="21" fill="${INK}"/><path d="M33 63 Q28 78 42 86 Q38 74 33 63 Z" fill="#2B2B36"/><path d="M44 89 v5 M56 89 v5" stroke="${AMBER}" stroke-width="3" stroke-linecap="round"/><path d="M68.5 40 L83 44.5 L68.5 49 Z" fill="${AMBER}"/><circle cx="57" cy="39" r="7.5" fill="#FFFFFF"/><circle cx="59" cy="39.5" r="3.8" fill="${INK}"/><circle cx="60.5" cy="37.8" r="1.2" fill="#FFFFFF"/><circle cx="75" cy="21" r="2.2" fill="${AMBER}"/><circle cx="81.5" cy="14" r="3" fill="${AMBER}"/><circle cx="89.5" cy="7.5" r="3.8" fill="${AMBER}"/>`,
  },
];

// ---------- SVG helpers ----------
const svg = (vb, inner, { title = 'Thinking Raven logo', withFonts = false, width, height } = {}) =>
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}"${width ? ` width="${width}"` : ''}${height ? ` height="${height}"` : ''} role="img" aria-label="${title}">` +
  (withFonts ? `<style>@import url('${FONT_CSS.replace(/&/g, '&amp;')}');</style>` : '') + inner + `</svg>`;

const iconInner = (c, mode) => {
  const fg = mode === 'dark' ? BONE : INK;
  const bg = mode === 'dark' ? INK : BONE;
  return c.icon(fg, bg);
};
const nested = (c, mode, size = 100) => `<svg x="0" y="0" width="${size}" height="${size}" viewBox="${c.vb}">${iconInner(c, mode)}</svg>`;
const lockup = (c, mode) => {
  const fg = mode === 'dark' ? BONE : INK;
  return `${nested(c, mode)}<text x="118" y="63" font-family="${SANS}" font-weight="600" font-size="38" letter-spacing="-0.5" fill="${fg}">Thinking Raven</text>`;
};

// ---------- write SVG files ----------
mkdirSync(OUT, { recursive: true });
for (const c of concepts) {
  for (const mode of ['light', 'dark']) {
    const bgRect = c.fixedBg ? '' : `<rect width="100%" height="100%" fill="${mode === 'dark' ? INK : 'none'}"/>`;
    writeFileSync(join(OUT, `${c.id}-${c.slug}-icon-${mode}.svg`), svg(c.vb, bgRect + iconInner(c, mode), { withFonts: true }));
    writeFileSync(join(OUT, `${c.id}-${c.slug}-lockup-${mode}.svg`), svg('0 0 440 100', lockup(c, mode), { withFonts: true }));
    if (c.wordmark) writeFileSync(join(OUT, `${c.id}-${c.slug}-wordmark-${mode}.svg`), svg(c.wordmark.vb, c.wordmark.draw(mode === 'dark' ? BONE : INK), { withFonts: true }));
  }
}

// ---------- review board ----------
const card = (c) => {
  const big = (mode) => `<div class="tile ${mode}">${svg(c.vb, iconInner(c, mode))}</div>`;
  const wm = c.wordmark ? `<div class="wm-row"><div class="wm light">${svg(c.wordmark.vb, c.wordmark.draw(INK))}</div><div class="wm dark">${svg(c.wordmark.vb, c.wordmark.draw(BONE))}</div></div>` : '';
  return `
  <article class="card" id="c${c.id}">
    <header>
      <div><span class="num">${c.id}</span><h2>${c.name}</h2><span class="chip">${c.type}</span></div>
      <label class="pick"><input type="checkbox" name="pick" value="${c.id} ${c.name}" form="picks"> Shortlist</label>
    </header>
    <p class="story">${c.story}</p>
    <div class="tiles">${big('light')}${big('dark')}</div>
    ${wm}
    <div class="uses">
      <figure><div class="avatar">${svg(c.vb, iconInner(c, c.fixedBg ? 'light' : 'dark'))}</div><figcaption>X / LinkedIn avatar</figcaption></figure>
      <figure><div class="avatar light-av">${svg(c.vb, iconInner(c, 'light'))}</div><figcaption>Light avatar</figcaption></figure>
      <figure><div class="tab"><span class="fav32">${svg(c.vb, iconInner(c, c.fixedBg ? 'light' : 'dark'))}</span><span class="fav16">${svg(c.vb, iconInner(c, 'light'))}</span><span class="tabtxt">thinkingraven.com</span></div><figcaption>Favicon at 32 px and 16 px</figcaption></figure>
      <figure class="sig"><div class="email">${svg('0 0 440 100', lockup(c, 'light'))}<div class="sigtxt">Vishal · Founder<br><span>hello@thinkingraven.com</span></div></div><figcaption>Email signature</figcaption></figure>
    </div>
  </article>`;
};

const board = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Thinking Raven Logos</title>
<link rel="stylesheet" href="${FONT_CSS}">
<style>
  :root { --ink:${INK}; --bone:${BONE}; --amber:${AMBER}; --page:#09090C; --card:#14141A; --line:#25252E; --mute:#9A9AA8; }
  *,*::before,*::after { box-sizing:border-box; }
  body { margin:0; background:var(--page); color:var(--bone); font-family:${SANS}; }
  main { max-width:1180px; margin:0 auto; padding:40px 16px 80px; }
  .kicker { color:var(--amber); letter-spacing:.18em; text-transform:uppercase; font-size:12px; }
  h1 { font-size:clamp(30px,5vw,52px); margin:.2em 0 .3em; letter-spacing:-.02em; }
  .lead { color:var(--mute); max-width:760px; line-height:1.55; }
  .palette { display:flex; gap:10px; flex-wrap:wrap; margin:18px 0 34px; }
  .sw { display:flex; align-items:center; gap:8px; background:var(--card); border:1px solid var(--line); border-radius:999px; padding:6px 12px 6px 6px; font-size:13px; }
  .sw i { width:22px; height:22px; border-radius:50%; display:inline-block; border:1px solid #333; }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(min(100%,540px),1fr)); gap:20px; }
  .card { background:var(--card); border:1px solid var(--line); border-radius:18px; padding:20px; min-width:0; }
  .card header { display:flex; justify-content:space-between; align-items:flex-start; gap:12px; }
  .card header > div { display:flex; align-items:center; gap:10px; flex-wrap:wrap; }
  .num { color:var(--mute); font-size:13px; }
  h2 { font-size:22px; margin:0; letter-spacing:-.01em; }
  .chip { font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--amber); border:1px solid #4a3a1c; background:#211a0c; padding:3px 8px; border-radius:999px; }
  .pick { font-size:13px; color:var(--mute); white-space:nowrap; cursor:pointer; }
  .pick input { accent-color:var(--amber); width:16px; height:16px; vertical-align:-3px; }
  .story { color:#C9C7C0; font-size:14px; line-height:1.55; margin:10px 0 16px; }
  .tiles { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
  .tile { aspect-ratio:1; border-radius:14px; display:grid; place-items:center; padding:14%; }
  .tile.light { background:var(--bone); } .tile.dark { background:var(--ink); border:1px solid var(--line); }
  .tile svg { width:100%; height:100%; }
  .wm-row { display:grid; grid-template-columns:1fr; gap:10px; margin-top:12px; }
  .wm { border-radius:12px; padding:18px 22px; } .wm.light { background:var(--bone); } .wm.dark { background:var(--ink); border:1px solid var(--line); }
  .wm svg { width:100%; height:auto; max-height:90px; display:block; }
  .uses { display:grid; grid-template-columns:auto auto 1fr; gap:14px 16px; margin-top:16px; align-items:end; }
  figure { margin:0; } figcaption { font-size:11px; color:var(--mute); margin-top:6px; }
  .avatar { width:72px; height:72px; border-radius:50%; overflow:hidden; background:var(--ink); display:grid; place-items:center; border:1px solid var(--line); }
  .avatar.light-av { background:var(--bone); }
  .avatar svg { width:78%; height:78%; }
  .tab { display:flex; align-items:center; gap:8px; background:#202028; border:1px solid var(--line); border-radius:10px 10px 0 0; padding:8px 12px; width:max-content; max-width:100%; }
  .fav32 svg { width:32px; height:32px; display:block; border-radius:6px; background:var(--ink); }
  .fav16 svg { width:16px; height:16px; display:block; background:var(--bone); border-radius:3px; padding:1px; }
  .tabtxt { font-size:12px; color:#ddd; }
  .sig { grid-column:1 / -1; }
  .email { background:#fff; border-radius:10px; padding:12px 14px; display:flex; align-items:center; gap:14px; flex-wrap:wrap; }
  .email svg { width:170px; height:auto; }
  .sigtxt { color:#333; font-size:12px; line-height:1.4; border-left:1px solid #ddd; padding-left:14px; } .sigtxt span { color:#777; }
  form.send { margin-top:34px; background:var(--card); border:1px solid var(--line); border-radius:18px; padding:20px; display:grid; gap:12px; }
  textarea { width:100%; background:#0d0d11; color:var(--bone); border:1px solid var(--line); border-radius:10px; padding:10px; font:inherit; }
  button { justify-self:start; background:var(--amber); color:#111; border:0; border-radius:999px; padding:10px 18px; font:600 14px ${SANS}; cursor:pointer; }
  #status { color:var(--mute); font-size:13px; }
</style></head>
<body><main>
  <p class="kicker">Thinking Raven · Logo exploration · round 1</p>
  <h1>Nine directions, one raven</h1>
  <p class="lead">Every concept uses the same disciplined palette, so whichever you pick works with the rest of the system. Each card shows the mark on light and dark, as an X/LinkedIn avatar, as a browser favicon at real size, and in an email signature. Tick the ones you like and send them back. The next round refines your favourites into the final logo package (ICO, PNG sizes, social kit).</p>
  <div class="palette"><span class="sw"><i style="background:${INK}"></i>Raven ink ${INK}</span><span class="sw"><i style="background:${BONE}"></i>Bone ${BONE}</span><span class="sw"><i style="background:${AMBER}"></i>Thought amber ${AMBER}</span></div>
  <section class="grid">${concepts.map(card).join('')}</section>
  <form id="picks" class="send" data-lavish-question="logo-shortlist" onsubmit="event.preventDefault();
    const picks=[...document.querySelectorAll('input[name=pick]:checked')].map(i=>i.value);
    const notes=(this.notes.value||'').trim();
    if(!picks.length&&!notes){document.getElementById('status').textContent='Tick at least one concept or add a note.';return;}
    const msg='Logo shortlist: '+(picks.join(', ')||'none')+(notes?'. Notes: '+notes:'');
    document.getElementById('status').textContent='Queued: '+msg;
    if(window.lavish) window.lavish.queuePrompt(msg,{tag:'choice',text:msg,element:this,queueKey:'logo-shortlist',data:{picks,notes}});">
    <h2>Send your shortlist</h2>
    <textarea name="notes" rows="2" placeholder="Optional: what you like or dislike, e.g. 'mix #03's shape with #06's colours'"></textarea>
    <button type="submit">Queue my shortlist</button><span id="status" role="status" aria-live="polite"></span>
  </form>
</main></body></html>`;
writeFileSync(BOARD, board);
console.log(`Wrote ${concepts.length} concepts to ${OUT}\nBoard: ${BOARD}`);
