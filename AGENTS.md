# AGENTS.md: Thinking Raven brand

Instructions for AI agents (Claude, Codex, Cursor, Copilot, etc.) that build anything carrying the Thinking Raven brand: websites, apps, emails, decks, social posts, docs. **Read this before producing any branded output.** Human-facing guidelines live in `index.html` (published at https://thinkingraven.github.io/brand/).

## 1. Brand facts

| Fact | Value |
|---|---|
| Name in prose | **Thinking Raven** (two words, title case). Never "ThinkingRaven", "Thinking raven" or "TR" in running text. |
| Logo text | `thinkingraven.` all lowercase, with the amber full stop. **Logo only**: never type it as a word in sentences. |
| Domain | thinkingraven.com |
| Contact email | hello@thinkingraven.com |
| GitHub | github.com/thinkingraven |
| X | @thinkingravenai (x.com/thinkingravenai) |
| Instagram | @thinkingravenai |
| LinkedIn | Thinking Raven (company page) |
| Patreon | patreon.com/c/thinkingraven |
| Mascot | **Thinky**, a friendly raven used in the app and on onboarding screens. Not the company logo. |
| Story | Odin's raven Huginn, whose name means "thought", flies out each day and returns with what it learned. The amber full stop is the raven's eye: the moment a thought lands. |
| Placeholder tagline | "AI that thinks before it speaks." (Not final. Don't invent other taglines unless asked.) |

## 2. Which file to use

Always use files from this repo. **Never redraw, retype or approximate the logo**: no CSS text logos and no AI-generated look-alikes.

| Context | File | Notes |
|---|---|---|
| Website header (light background) | `logos/final/thinkingraven-wordmark-ink.svg` | Inline or `<img>`, min 100 px wide |
| Website header (dark background) | `logos/final/thinkingraven-wordmark-bone.svg` | |
| Favicon | `exports/favicon/favicon.ico` + `favicon.svg` + `apple-touch-icon.png` | See the snippet in §6 |
| PWA / Android icons | `exports/favicon/icon-192.png`, `icon-512.png` | |
| Link preview (Open Graph / Twitter card) | `exports/social/og-image-1200x630.png` | |
| Square avatar / app tile (dark) | `logos/final/thinkingraven-avatar-dark.svg` or `exports/social/x-avatar-400.png` | Default avatar everywhere |
| Square avatar (light) | `logos/final/thinkingraven-avatar-light.svg` or `exports/social/avatar-light-1000.png` | Only where dark won't work |
| Small mark, no background | `logos/final/thinkingraven-monogram-ink.svg` / `-bone.svg` | `tr.` |
| Banner / cover images | `exports/social/x-header-1500x500.png`, `linkedin-cover-1128x191.png`, `youtube-banner-2560x1440.png` | |
| Email signature | `exports/wordmark/email-signature-600.png` | Display at 300 px wide |
| Transparent wordmark PNG (slides, docs) | `exports/wordmark/wordmark-ink-2000.png` / `wordmark-bone-2000.png` | |
| iOS app icon | `exports/app/thinky-app-icon-1024.png` | Square and opaque; iOS rounds the corners |
| Mascot in UI (onboarding, empty states) | `logos/final/thinky-mascot-transparent.svg` | |

### Hosted URLs (to hot-link from outside the repo)
- Site: `https://thinkingraven.github.io/brand/<path>`, e.g. `https://thinkingraven.github.io/brand/logos/final/thinkingraven-wordmark-ink.svg`
- Raw: `https://raw.githubusercontent.com/thinkingraven/brand/main/<path>`

## 3. Colour and type

Use the tokens. Don't hard-code new colours. Source: `tokens/tokens.json` and `tokens/tokens.css`.

| Token | Hex | Use |
|---|---|---|
| `--tr-ink` | `#0F0F14` | Text on light, dark backgrounds |
| `--tr-bone` | `#F3EFE6` | Text on dark, light backgrounds |
| `--tr-amber` | `#F2A93B` | Accent only: the full stop, highlights, **one** primary call to action per screen |
| `--tr-mute` | `#9A9AA8` | Secondary text on dark backgrounds |

- **Hard rule:** amber text on bone or white is forbidden (contrast 1.7:1). Amber is fine on ink (9.6:1), and ink text on amber is fine (9.6:1).
- No gradients, glows, drop shadows or "AI purple" on brand marks.
- Font: **Space Grotesk** (`fonts/SpaceGrotesk-VF.ttf`, SIL Open Font Licence; also on Google Fonts). Headings 700, body 400/500.

## 4. Logo rules

- Clear space around the wordmark: at least the height of its "t".
- Minimum size: wordmark 100 px wide; monogram 16 px.
- Ink logo on light backgrounds, bone logo on dark. No other colour versions.
- **Don't:** stretch, skew, rotate, outline, recolour or move the amber dot, add effects, place it on busy photos, or set the wordmark in any other font.

## 5. Voice and tone

Calm, curious, precise. Thinks first, speaks second.
- Short sentences. Plain words. Specific over grand.
- Confident but never hype. Avoid "revolutionary", "game-changing", "unleash", "supercharge", "cutting-edge".
- Light raven/thought imagery is welcome in moderation (e.g. "Something is hatching").
- Use sentence case for headings and buttons.

## 6. Snippets

```html
<!-- Favicons and link preview -->
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:image" content="https://thinkingraven.com/og-image-1200x630.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0F0F14">

<!-- Header logo -->
<a href="/" aria-label="Thinking Raven home">
  <img src="/thinkingraven-wordmark-ink.svg" alt="Thinking Raven" width="180" height="29">
</a>
```

```css
@import url("https://thinkingraven.github.io/brand/tokens/tokens.css");
body { font-family: var(--tr-font); color: var(--tr-ink); background: var(--tr-bone); }
.cta { background: var(--tr-amber); color: var(--tr-ink); border-radius: var(--tr-radius-button); }
```

## 7. Repo map

```
index.html             Human brand guidelines site (GitHub Pages)
AGENTS.md              This file
llms.txt               Machine-readable index of this repo
tokens/                tokens.json, tokens.css
logos/final/           Master SVGs (outlined). Source of truth.
exports/               Generated PNG/ICO files. Don't edit by hand.
fonts/                 Space Grotesk + OFL licence
tools/                 Scripts that regenerate logos/exports
archive/               Round-1 logo exploration (not for use)
thinkingraven-brand-kit.zip   Everything in exports/ + logos/final/ as one download
```

## 8. Changing the brand files

1. Edit the source (`tools/outline.py` for the wordmark and monogram, `tools/export.py` for the mascot and exports).
2. Regenerate the files:
   - Wordmark and monogram: `python tools/outline.py fonts/SpaceGrotesk-VF.ttf logos/final` (needs `fonttools` and `uharfbuzz`)
   - Exports: `python3 tools/export.py . /tmp/tr-export` (needs Google Chrome and macOS `sips`)
   - Rebuild the zip: `zip -r thinkingraven-brand-kit.zip exports logos/final -x '*.DS_Store'`
3. Never hand-edit `exports/`. Never commit an approximated logo.
4. Keep `AGENTS.md`, `llms.txt`, `index.html` and `README.md` consistent when anything changes.

## 9. Before you ship anything branded, check

- [ ] Logo comes from `logos/final/` or `exports/`, not retyped or redrawn
- [ ] Correct version for the background (ink on light, bone on dark)
- [ ] No amber text on light backgrounds
- [ ] Brand name written as "Thinking Raven" in prose
- [ ] Clear space and minimum size respected
- [ ] Favicon and OG image wired up (for websites)
