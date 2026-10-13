# AGENTS.md: Thinking Raven brand

Instructions for AI agents (Claude, Codex, Cursor, Copilot, etc.) that build anything carrying the Thinking Raven brand: websites, apps, emails, decks, social posts, docs. **Read this before producing any branded output.** For any UI (screens, components, layouts), also follow **`DESIGN.md`**, the full design system: colour roles, type scale, spacing, components and motion. Human-facing guidelines are published at **https://thinkingraven.github.io/brand/** (source: `index.html`).

## 1. Brand facts

| Fact | Value |
|---|---|
| Name in prose | **Thinking Raven** (two words, title case). Never "ThinkingRaven", "Thinking raven" or "TR" in running text. |
| Logo text | `thinking raven.`: all lowercase, two words with a clear space ("thinking" regular, "raven" bold), then the amber full stop. **Logo only**: never type it in sentences, and never close the space (it would read "thinkin graven"). |
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
| A product's README or site (rookery, roost) | `logos/final/<product>-wordmark-ink.svg` (light) · `-bone.svg` (dark) | Product name in visuals is lowercase with the amber full stop (`roost.`); in prose it's lowercase without it (roost). Never the company logo. |
| Website header that collapses to `tr.` on scroll | `logos/final/thinkingraven-logo-morph-ink.svg` (`-bone` on dark) | Inline the SVG markup; add `.tr-logo--mono` to collapse it. Reference CSS: `.tr-logo-morph` in `css/components.css`. Behaviour: DESIGN.md → Top navigation. As an `<img>` it's just the wordmark. |
| Favicon | `exports/favicon/favicon.ico` + `favicon.svg` + `apple-touch-icon.png` | See the snippet in §6. The tab icon is the Thinky mark: `favicon.svg` is white on dark tab bars and ink on light ones; `.ico` is ink. The apple-touch and PWA icons stay the `tr.` tile |
| Thinky mark on its own (white or ink, amber eye) | `logos/final/thinky-mark-white.svg` / `thinky-mark-ink.svg` | Small square spots where the mascot stands in for the site, like a tab icon |
| PWA / Android icons | `exports/favicon/icon-192.png`, `icon-512.png` | |
| Link preview (Open Graph / Twitter card) | `exports/social/og-image-1200x630.png` | |
| Square avatar / app tile (dark) | `logos/final/thinkingraven-avatar-dark.svg` or `exports/social/x-avatar-400.png` | Default avatar everywhere |
| Square avatar (light) | `logos/final/thinkingraven-avatar-light.svg` or `exports/social/avatar-light-1000.png` | Only where dark won't work |
| Small mark, no background | `logos/final/thinkingraven-monogram-ink.svg` / `-bone.svg` | `tr.` |
| Banner / cover images | `exports/social/x-header-1500x500.png`, `linkedin-cover-1128x191.png`, `youtube-banner-2560x1440.png` | |
| Email signature | `exports/wordmark/email-signature-600.png` | Display at 300 px wide |
| Transparent wordmark PNG (slides, docs) | `exports/wordmark/wordmark-ink-2000.png` / `wordmark-bone-2000.png` | |
| iOS app icon | `exports/app/thinky-app-icon-1024.png` | Square and opaque; iOS rounds the corners |
| Mascot in UI (onboarding, empty states) | `logos/final/thinky-mascot-transparent.svg` | On dark surfaces, place it on a bone disc |
| Mascot on an amber band (closing call to action) | `logos/final/thinky-mascot-amber.svg` | Bone beak and feet; the standard amber ones disappear into amber |
| **Building any UI** | `DESIGN.md` + `tokens/tokens.css` + `css/components.css` | Tokens and reference components; never invent new colours |

### Hosted URLs
This repo is public and published with GitHub Pages:
- Site: `https://thinkingraven.github.io/brand/<path>`, e.g. `https://thinkingraven.github.io/brand/logos/final/thinkingraven-wordmark-ink.svg`
- Raw: `https://raw.githubusercontent.com/thinkingraven/brand/main/<path>`

**When to hot-link vs copy:** hot-linking the Pages URLs is fine for docs, READMEs, emails, slide decks and prototypes. For production websites and apps, **copy** the files into the project (for example a `public/` folder) so they're versioned with the product and don't depend on this repo. Keep the original file names.

## 3. Colour and type

Use the tokens. Don't hard-code new colours. Sources: `DESIGN.md` (YAML front matter, the source of truth), `tokens/tokens.json` and `tokens/tokens.css`.

| Token | Hex | Use |
|---|---|---|
| `--tr-canvas` (alias `--tr-bone`) | `#F3EFE6` | Page background in the light theme; text on dark. Marketing pages default to the dark theme, where the canvas is ink |
| `--tr-surface-card` | `#FFFFFF` | Cards, inputs, assistant chat replies |
| `--tr-ink` | `#0F0F14` | Headlines and primary text on light; dark surfaces |
| `--tr-body` / `--tr-muted` | `#2B2B33` / `#5C5C68` | Running text / secondary text |
| `--tr-primary` (alias `--tr-amber`) | `#F2A93B` | Accent only: the full stop, the thinking indicator, **one** primary button per view, and on marketing pages one signal band and one closing band (`.tr-amber`) |
| `--tr-on-dark-soft` (alias `--tr-mute`) | `#9A9AA8` | Secondary text on dark backgrounds |
| `--tr-success` / `--tr-warning` / `--tr-error` / `--tr-info` | see DESIGN.md | Status only, always with an icon or word |

- **Hard rule:** amber text on bone or white is forbidden (contrast 1.7:1). Amber is fine on ink (9.6:1), and ink text on amber is fine (9.6:1). Never white text on amber.
- **Focus rings:** ink on light surfaces, amber on dark (`--tr-focus`).
- No gradients, glows, coloured shadows or "AI purple".
- Fonts: **Space Grotesk** for everything people read (display 500 tight, one weight per headline; body 400) and **Space Mono** for code and uppercase kickers. Both are in `fonts/` (SIL Open Font Licence).
- Dark mode: set `data-theme="dark"` on `<html>`, or add `class="tr-theme-dark"` to any container. **Marketing pages are dark first** (v2, "Night Watch"): dark by default, with a toggle to light.
- Marketing pages use the **framed grid** (`.tr-frame`, `.tr-cells`): rails down both sides and cells that share hairlines. See DESIGN.md → Layout.

## 4. Logo rules

- The wordmark is two words, `thinking raven.`, with a fixed 0.30 em space. **Never tighten or remove the space.**
- Clear space around the wordmark: at least the height of its "t".
- Minimum size: wordmark 100 px wide; monogram 16 px.
- Ink logo on light backgrounds, bone logo on dark. No other colour versions.
- Product wordmarks follow the same rules. A new product gets one by adding its name to `PRODUCTS` in `tools/outline.py`; never set a product name in a font yourself.
- The only logo animation is the nav morph between the wordmark and the monogram. Use `logos/final/thinkingraven-logo-morph-*.svg` with its reference CSS; never animate, split or rebuild the logo yourself.
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
  <img src="/thinkingraven-wordmark-ink.svg" alt="Thinking Raven" width="180" height="28">
</a>
```

```css
/* Prototypes: hot-link. Production: copy tokens.css, components.css and fonts/ into your project. */
@import url("https://thinkingraven.github.io/brand/tokens/tokens.css");
@import url("https://thinkingraven.github.io/brand/css/components.css");
body { font: var(--tr-body-md); color: var(--tr-body); background: var(--tr-canvas); }
/* Then use the reference classes, e.g. <button class="tr-btn tr-btn--primary">Start thinking</button> */
```

## 7. Repo map

```
index.html             Brand guidelines site (https://thinkingraven.github.io/brand/)
DESIGN.md              The design system: tokens + guide (source of truth for UI)
AGENTS.md              This file  ·  CLAUDE.md points here
llms.txt               Machine-readable index of this repo
tokens/                tokens.json (W3C format), tokens.css (CSS variables, dark mode)
css/components.css     Reference CSS for every component (tr- classes)
logos/final/           Master SVGs (outlined). Source of truth for the logo.
exports/               Generated PNG/ICO files. Don't edit by hand.
fonts/                 Space Grotesk, Space Mono + OFL licences
tools/                 Scripts that regenerate logos, exports and explorations
archive/               Logo explorations (round 1 concepts, round 2 wordmark): not for use
thinkingraven-brand-kit.zip   Logos, exports, fonts, tokens, CSS and DESIGN.md in one download
```

## 8. Changing the brand files

1. Edit the source (`tools/outline.py` for the wordmark, monogram, logo morph and product wordmarks, `tools/export.py` for the mascot and exports).
2. Regenerate the files:
   - Wordmark, monogram, logo morph and product wordmarks: `python tools/outline.py fonts/SpaceGrotesk-VF.ttf logos/final` (needs `fonttools` and `uharfbuzz`)
   - Exports: `python3 tools/export.py . /tmp/tr-export` (needs Google Chrome and macOS `sips`)
   - Rebuild the zip: `zip -r thinkingraven-brand-kit.zip exports logos/final fonts tokens css DESIGN.md -x '*.DS_Store'`
3. Never hand-edit `exports/`. Never commit an approximated logo.
4. Keep `DESIGN.md`, `tokens/`, `css/components.css`, `AGENTS.md`, `llms.txt`, `index.html` and `README.md` consistent when anything changes.

## 9. Before you ship anything branded, check

- [ ] Logo comes from `logos/final/` or `exports/`, not retyped or redrawn
- [ ] Correct version for the background (ink on light, bone on dark)
- [ ] No amber text on light backgrounds
- [ ] Brand name written as "Thinking Raven" in prose
- [ ] Clear space and minimum size respected
- [ ] Favicon and OG image wired up (for websites)
- [ ] UI uses DESIGN.md tokens and components: one amber action per view (plus at most one signal band and one closing band per page), visible focus rings, AA contrast

## Public repository rules

This repository is public. Follow the organisation rules in https://github.com/thinkingraven/.github/blob/main/PUBLIC-REPOS.md: no secrets, no employer or client material, no personal data, demo data only in screenshots and examples.
