---
version: 1.0.0
name: Thinking-Raven-design-system
description: A calm, editorial-tech interface for Thinking Raven, an AI product. The system sits on a warm bone canvas with near-black raven-ink text and dark ink "product" surfaces. A single thought-amber accent is reserved for the one primary action and the wordmark's full stop. Type is Space Grotesk throughout, with tight bold display headlines and a signature split-weight headline (light + bold words, like the wordmark "thinking" + "raven"). Its sister face, Space Mono, handles code and uppercase kickers. Where most AI brands go cool blue/purple with glows, Thinking Raven stays warm, flat and quiet: it thinks before it speaks.

colors:
  primary: "#F2A93B"
  primary-active: "#D98F22"
  primary-disabled: "#E9E3D6"
  on-primary: "#0F0F14"
  ink: "#0F0F14"
  body-strong: "#1A1A21"
  body: "#2B2B33"
  muted: "#5C5C68"
  muted-soft: "#6A6A75"
  hairline: "#E3DDD0"
  hairline-soft: "#EEE8DC"
  canvas: "#F3EFE6"
  surface-soft: "#FAF8F3"
  surface-card: "#FFFFFF"
  surface-strong: "#E9E3D6"
  surface-dark: "#0F0F14"
  surface-dark-elevated: "#15151B"
  surface-dark-soft: "#1B1B22"
  hairline-dark: "#2A2A33"
  on-dark: "#F3EFE6"
  on-dark-soft: "#9A9AA8"
  on-dark-muted: "#8A8A98"
  success: "#256B43"
  success-on-dark: "#7BD88F"
  success-soft: "#E3EFE6"
  warning: "#8A5A00"
  warning-on-dark: "#F2A93B"
  warning-soft: "#F8EBD3"
  error: "#B42318"
  error-on-dark: "#FF7B72"
  error-soft: "#F7E1DE"
  info: "#2F5FA8"
  info-on-dark: "#8AB4F8"
  info-soft: "#E1E9F5"
  focus-ring-light: "#0F0F14"
  focus-ring-dark: "#F2A93B"

typography:
  display-xl:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: -2px
  display-lg:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-md:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.6px
  title-lg:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: -0.1px
  title-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  kicker:
    fontFamily: "Space Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 1.8px
    textTransform: uppercase
  code:
    fontFamily: "Space Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  button:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  nav-link:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 18px
  xl: 24px
  pill: 9999px
  full: 50%

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  xxxl: 64px
  section: 72px
  section-lg: 96px
  container: 1120px
  gutter: 16px
  gutter-lg: 28px

elevation:
  none: "none"
  sm: "0 1px 2px rgba(15,15,20,0.06)"
  md: "0 8px 24px rgba(15,15,20,0.10)"
  lg: "0 24px 64px rgba(15,15,20,0.18)"
  focus-light: "0 0 0 2px #F3EFE6, 0 0 0 4px #0F0F14"
  focus-dark: "0 0 0 2px #0F0F14, 0 0 0 4px #F2A93B"

motion:
  duration-fast: 120ms
  duration-base: 200ms
  duration-slow: 320ms
  duration-thinking: 1200ms
  easing-standard: "cubic-bezier(0.2, 0, 0, 1)"
  easing-enter: "cubic-bezier(0, 0, 0, 1)"
  easing-exit: "cubic-bezier(0.3, 0, 1, 1)"

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.pill}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
    height: 44px
  button-secondary-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    borderColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 16px
  button-icon-circular:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    size: 40px
  text-link:
    textColor: "{colors.ink}"
    underlineColor: "{colors.primary}"
    underlineThickness: 2px
    typography: "{typography.body-md}"
  text-link-on-dark:
    textColor: "{colors.on-dark}"
    underlineColor: "{colors.primary}"
    underlineThickness: 2px
  top-nav:
    backgroundColor: "rgba(243,239,230,0.92)"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.nav-link}"
    height: 60px
  hero-band:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  product-card-dark:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    borderColor: "{colors.hairline-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  code-window:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.on-dark}"
    borderColor: "{colors.hairline-dark}"
    typography: "{typography.code}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  chat-bubble-assistant:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 14px 18px
  chat-bubble-user:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 14px 18px
  thinking-indicator:
    dotColor: "{colors.primary}"
    dotSize: 8px
    gap: 6px
    duration: "{motion.duration-thinking}"
  prompt-composer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 14px
    height: 44px
  text-input-focused:
    borderColor: "{colors.ink}"
    shadow: "{elevation.focus-light}"
  text-input-error:
    borderColor: "{colors.error}"
    helperTextColor: "{colors.error}"
  badge-pill:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-amber:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.kicker}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
  status-dot:
    size: 8px
    rounded: "{rounded.full}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.pill}"
    padding: 8px 14px
  category-tab-active:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.pill}"
  alert:
    backgroundColor: "{colors.info-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.info}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 14px 16px
  toast:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.pill}"
    padding: 10px 16px
    shadow: "{elevation.md}"
  avatar:
    rounded: "{rounded.full}"
    size: 32px
  callout-card-amber:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  cta-band-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxxl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl}"
---

## Overview

Thinking Raven looks like a **quiet, well-edited notebook that happens to be very smart**. The base is a warm **bone canvas** (`{colors.canvas}` #F3EFE6): paper-like, deliberately not the cool white or blue-grey of most AI products. Text is **raven ink** (`{colors.ink}` #0F0F14), an almost-black with a hint of blue, like a raven's feather.

Brand energy comes from **one drop of thought amber** (`{colors.primary}` #F2A93B). In the logo it's the raven's eye, the full stop after `thinking raven`. In the interface it marks **the one thing to do next**: the primary button, the active thinking indicator, a highlight. Amber is never decoration and never text on light surfaces.

The system alternates three surface modes:
1. **Bone canvas** (`{colors.canvas}`): the default floor for reading and marketing pages.
2. **White cards** (`{colors.surface-card}`): content, features, chat replies, inputs. One step *up* from the canvas.
3. **Raven-ink surfaces** (`{colors.surface-dark}`): hero bands, product chrome, code, the user's own chat messages. This is where the product shows itself.

**Key characteristics**
- Warm bone canvas plus near-black ink text. The pairing *is* the brand; pure white pages read as "any other AI tool".
- A single amber accent, scarce on purpose. One amber call to action per view.
- **Space Grotesk** everywhere: bold, tight-tracked display headlines and regular body text. **Space Mono** for code and uppercase kickers.
- The signature **split-weight headline**: light and bold words in one line ("thinks **first**"), echoing the wordmark's "thinking" (400) and "raven" (700).
- Flat by default: depth comes from surface colour (bone → white → ink), not shadows or glows.
- Rounded but not bubbly: pill buttons, 12 px inputs, 18 px cards.
- AI-native components are first-class: chat bubbles, the three-dot **thinking indicator**, and the prompt composer.

## Logo

| Asset | Spec | Files |
|---|---|---|
| **Wordmark** | `thinking raven.`: lowercase Space Grotesk; "thinking" at 400, a **0.30 em word space**, "raven" at 700, tracking −0.03 em, then an amber full stop | `logos/final/thinkingraven-wordmark-ink.svg` (on light) · `-bone.svg` (on dark) |
| **Monogram** | `tr.`: "t" at 400, "r" at 700, amber full stop | `logos/final/thinkingraven-monogram-*.svg` · square tiles `thinkingraven-avatar-dark.svg` / `-light.svg` |
| **Mascot** | Thinky, flat ink/bone/amber raven. Product and app only, never the company logo. | `logos/final/thinky-mascot-*.svg` |

- **The word space is part of the logo.** Without it, the bold "r" joins the "g" and the mark reads "thinkin graven" (rejected in round 2). Never tighten or remove it.
- **Clear space:** at least the height of the "t" on all sides. **Minimum size:** wordmark 100px wide (25 mm in print); monogram 16px.
- Ink wordmark on light surfaces, bone wordmark on dark. The full stop is always amber. No other colour versions, effects or retyping.

## Colors

### Brand & accent
- **Thought amber / primary** (`{colors.primary}` #F2A93B): the wordmark's full stop, the primary button, the thinking indicator, the active state in dark UIs. Ink text on amber is 9.6:1.
- **Amber active** (`{colors.primary-active}` #D98F22): the pressed state of amber buttons. Ink on it is 7.2:1.
- **Amber disabled** (`{colors.primary-disabled}` #E9E3D6): a desaturated bone for disabled primary buttons, with `{colors.muted}` text.
- There is **no second accent colour**. If something needs emphasis, use weight, size or an ink surface, not a new hue.

### Surface
- **Canvas** (`{colors.canvas}` #F3EFE6): the default page floor. Warm bone.
- **Surface soft** (`{colors.surface-soft}` #FAF8F3): table headers and very soft bands.
- **Surface card** (`{colors.surface-card}` #FFFFFF): cards, inputs, assistant chat replies. Sits *above* the canvas.
- **Surface strong** (`{colors.surface-strong}` #E9E3D6): badges, selected rows and pressed ghost buttons.
- **Surface dark** (`{colors.surface-dark}` #0F0F14): the hero band, product showcases, user chat bubbles, toasts and the active tab.
- **Surface dark elevated** (`{colors.surface-dark-elevated}` #15151B): cards inside dark bands.
- **Surface dark soft** (`{colors.surface-dark-soft}` #1B1B22): code blocks and terminal panels.
- **Hairline** (`{colors.hairline}` #E3DDD0) and **hairline soft** (`{colors.hairline-soft}` #EEE8DC): 1 px borders and dividers on light surfaces.
- **Hairline dark** (`{colors.hairline-dark}` #2A2A33): 1 px borders on dark surfaces.

### Text
| Token | Hex | On bone | Use |
|---|---|---|---|
| `{colors.ink}` | #0F0F14 | 16.7:1 | Headlines, primary text, icons |
| `{colors.body-strong}` | #1A1A21 | 15.1:1 | Lead paragraphs |
| `{colors.body}` | #2B2B33 | 12.2:1 | Running text |
| `{colors.muted}` | #5C5C68 | 5.7:1 | Secondary text, descriptions |
| `{colors.muted-soft}` | #6A6A75 | 4.7:1 | Captions, fine print (the lowest allowed for text) |
| `{colors.on-dark}` | #F3EFE6 | 16.7:1 on ink | Text on dark surfaces |
| `{colors.on-dark-soft}` | #9A9AA8 | 6.9:1 on ink | Secondary text on dark |
| `{colors.on-dark-muted}` | #8A8A98 | 5.6:1 on ink | Captions on dark |
| `{colors.on-primary}` | #0F0F14 | 9.6:1 on amber | Text on amber (never white) |

### Semantic
Each status colour has three forms: a **text/border** colour for light surfaces, an **on-dark** colour, and a **soft** tint for alert backgrounds. Text on soft tints is always `{colors.ink}`.

| Status | Light (text, border) | On dark | Soft background |
|---|---|---|---|
| Success | `{colors.success}` #256B43 (5.6:1) | `{colors.success-on-dark}` #7BD88F | `{colors.success-soft}` #E3EFE6 |
| Warning | `{colors.warning}` #8A5A00 (5.2:1) | `{colors.warning-on-dark}` #F2A93B | `{colors.warning-soft}` #F8EBD3 |
| Error | `{colors.error}` #B42318 (5.7:1) | `{colors.error-on-dark}` #FF7B72 | `{colors.error-soft}` #F7E1DE |
| Info | `{colors.info}` #2F5FA8 (5.5:1) | `{colors.info-on-dark}` #8AB4F8 | `{colors.info-soft}` #E1E9F5 |

Never communicate status with colour alone: pair it with an icon or a word ("Error:", ✓, ✗).

### Dark mode
The product supports a dark theme by remapping roles (implemented in `tokens/tokens.css` under `[data-theme="dark"]` and `prefers-color-scheme: dark`):

| Role | Light | Dark |
|---|---|---|
| canvas | #F3EFE6 | #0F0F14 |
| surface-card | #FFFFFF | #15151B |
| surface-soft | #FAF8F3 | #121217 |
| surface-strong | #E9E3D6 | #1B1B22 |
| hairline | #E3DDD0 | #2A2A33 |
| ink / text | #0F0F14 | #F3EFE6 |
| body | #2B2B33 | #D9D5CC |
| muted | #5C5C68 | #9A9AA8 |
| primary | #F2A93B | #F2A93B (unchanged) |
| focus ring | ink | amber |
| semantic text | light variants | `-on-dark` variants |

## Typography

### Font family
- **Space Grotesk** (variable, 300–700; SIL OFL; `fonts/SpaceGrotesk-VF.ttf`) is used for everything a person reads: display, titles, body, buttons and navigation.
- **Space Mono** (400 and 700; SIL OFL; `fonts/SpaceMono-*.ttf`) is the sister face. It's used for code, terminal output, tokens and the uppercase **kicker** labels above headings.
- **Fallback stacks:** `"Space Grotesk", "Helvetica Neue", Arial, sans-serif` and `"Space Mono", ui-monospace, SFMono-Regular, Menlo, monospace`.

### Hierarchy

| Token | Size | Weight | Line height | Tracking | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 72px | 700 | 1.02 | -2px | Hero headline (one per page) |
| `{typography.display-lg}` | 56px | 700 | 1.05 | -1.5px | Landing section openers |
| `{typography.display-md}` | 40px | 700 | 1.1 | -1px | Section heads |
| `{typography.display-sm}` | 30px | 700 | 1.15 | -0.6px | Callouts, CTA bands, pricing |
| `{typography.title-lg}` | 22px | 600 | 1.3 | -0.2px | Card group titles, dialog titles |
| `{typography.title-md}` | 18px | 600 | 1.4 | -0.1px | Card titles, list headers |
| `{typography.title-sm}` | 16px | 600 | 1.4 | 0 | Small card titles, labels |
| `{typography.body-lg}` | 18px | 400 | 1.6 | 0 | Lead paragraphs, hero subtitles |
| `{typography.body-md}` | 16px | 400 | 1.6 | 0 | Default running text, chat messages |
| `{typography.body-sm}` | 14px | 400 | 1.55 | 0 | Secondary text, tables, footer |
| `{typography.caption}` | 13px | 500 | 1.4 | 0 | Captions, badge labels, helper text |
| `{typography.kicker}` | 12px | 700 (Mono) | 1.4 | 1.8px, uppercase | Eyebrow labels above headings: `{colors.muted}` on light, amber on dark |
| `{typography.code}` | 14px | 400 (Mono) | 1.6 | 0 | Code blocks, inline code, tokens |
| `{typography.button}` | 14px | 600 | 1.0 | 0 | Button labels |
| `{typography.nav-link}` | 14px | 500 | 1.4 | 0 | Navigation and tabs |

### Signature: the split-weight headline
The wordmark sets "thinking" in Regular and "raven" in Bold. Headlines can borrow that move: **set the setup words in 400 and the payoff word or words in 700, in the same line.** For example: "AI that thinks **first**." or "Ask **better**."
- Use it only on hero and section-opener headlines, at most once per screen.
- The bold part always comes last, and the line ends with a full stop. An amber full stop is allowed on the hero only.
- Never make the light part lighter than 400, and never use it in body text.

### Principles
- **Display is bold and tight.** Weight 700 with negative tracking (-0.6 to -2px). Space Grotesk's quirky letterforms carry the personality, so don't add effects.
- **Body is regular and open.** Weight 400 with 1.55–1.6 line height for easy reading of long AI answers. Use 500–600 for labels and emphasis, not italics.
- **Sentence case everywhere**: headings, buttons, tabs and menus. The only lowercase-only text is the wordmark.
- **Never retype the wordmark.** Use the SVG. Headlines that mention the brand write "Thinking Raven".
- **Measure:** keep running text at 60–75 characters per line (max-width ≈ 680px).
- **Numbers in tables and prices:** use `font-variant-numeric: tabular-nums`.

### Fallbacks and licensing
Both families are free under the SIL Open Font Licence and are self-hosted from `fonts/` (also available on Google Fonts). If they fail to load, fall back to Helvetica Neue/Arial and the system monospace. **Don't substitute Inter or Roboto** for display: they flatten the brand.

## Layout

### Spacing system
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4 · `{spacing.xs}` 8 · `{spacing.sm}` 12 · `{spacing.md}` 16 · `{spacing.lg}` 24 · `{spacing.xl}` 32 · `{spacing.xxl}` 48 · `{spacing.xxxl}` 64 · `{spacing.section}` 72 · `{spacing.section-lg}` 96.
- **Section padding:** `{spacing.section}` (72px) by default; `{spacing.section-lg}` (96px) for landing-page hero and closing bands.
- **Card padding:** `{spacing.xl}` (32px) for feature/product cards, `{spacing.lg}` (24px) for code windows and compact cards, `{spacing.md}` (16px) for chat bubbles and inputs.
- **Stack rhythm:** heading → paragraph `{spacing.xs}`–`{spacing.sm}`; paragraph → content `{spacing.xl}`; between cards `{spacing.md}`–`{spacing.lg}`.

### Grid & container
- **Max content width:** `{spacing.container}` 1120px, centred, with `{spacing.gutter}` 16px side padding on mobile and `{spacing.gutter-lg}` 28px from 720px up.
- **Reading column:** about 680px max for long text and chat transcripts.
- **Grids:** 12-column logic, implemented with `repeat(auto-fit, minmax(…, 1fr))`. Feature cards are 3-up on desktop, 2-up on tablet and 1-up on mobile. Asset or tile grids are 4–6 up on desktop.
- **Chat layout:** a single centred column (max 760px) with the composer pinned to the bottom. Assistant replies are left-aligned at full column width; user messages are right-aligned at max 80%.

### Whitespace philosophy
Calm comes from space. Generous section padding (72–96px), roomy cards (32px) and short line lengths make dense AI output feel considered rather than overwhelming. When a screen feels busy, remove elements before shrinking type.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No border, no shadow | Page sections, hero, nav |
| Hairline | 1px `{colors.hairline}` (or `{colors.hairline-dark}`) | Cards, inputs, tables, chat replies |
| Surface step | Canvas → `{colors.surface-card}` → `{colors.surface-dark}` | The main way to show depth |
| `{elevation.sm}` | 0 1px 2px rgba(15,15,20,.06) | Hovered cards (optional) |
| `{elevation.md}` | 0 8px 24px rgba(15,15,20,.10) | Menus, popovers, toasts |
| `{elevation.lg}` | 0 24px 64px rgba(15,15,20,.18) | Modals and dialogs only |

**Colour first, shadow rarely.** No glows, no coloured shadows, no gradients on surfaces.

### Focus
Every interactive element has a visible focus ring:
- **On light surfaces:** `{elevation.focus-light}`, a 2px bone gap and then a 2px ink ring. An amber ring on bone is only 1.7:1, so it's not allowed.
- **On dark surfaces:** `{elevation.focus-dark}`, a 2px ink gap and then a 2px amber ring (9.6:1).

### Decorative depth
- Product chrome (code windows, terminals, chat transcripts) on ink surfaces is the main "illustration".
- The amber dot can appear as a small punctuation motif: after hero headlines, as a status dot, or in the thinking indicator. Never as a large decorative blob.

## Shapes

### Border radius scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Inline code, tiny chips, checkboxes |
| `{rounded.sm}` | 8px | Small images, menu items, tooltips |
| `{rounded.md}` | 12px | Inputs, code windows, alerts |
| `{rounded.lg}` | 18px | Cards, chat bubbles, the prompt composer, image tiles |
| `{rounded.xl}` | 24px | CTA bands, large media containers, modals |
| `{rounded.pill}` | 9999px | Buttons, badges, tabs, toasts |
| `{rounded.full}` | 50% | Avatars, icon buttons, status dots |

### Imagery & illustration
- **Product chrome first:** show real chat transcripts, code and answers on ink surfaces rather than abstract "AI" art.
- **The mascot, Thinky:** flat shapes in ink, bone and amber only, used for the app icon, onboarding, empty states and stickers (see `logos/final/thinky-*`). There's one approved pose; new poses need design review.
- **No stock photos** of people at laptops, robots, glowing brains or circuit boards.
- If photography is ever needed, use real people or real work, in **monochrome or ink/amber duotone**, cropped tight. Avatars crop to circles.

## Iconography
- **Style:** outline icons on a 24px grid, 1.75px stroke, round caps and joins. Use [Lucide](https://lucide.dev) (ISC licence) as the default set, since its geometry matches Space Grotesk.
- **Sizes:** 16px (inline with 14px text), 20px (buttons, inputs), 24px (navigation, empty states).
- **Colour:** `currentColor`, so ink on light and bone on dark. Amber only for the active or selected state.
- Icons sit to the **left** of labels in buttons, with an 8px gap. Icon-only buttons need an `aria-label`.
- Don't use filled or multicolour icon packs, emoji as interface icons, or the logo as an icon.

## Motion
**Calm, quick, purposeful.** Motion shows that the system is thinking or that something changed, never spectacle.

| Token | Value | Use |
|---|---|---|
| `{motion.duration-fast}` | 120ms | Hover/press colour changes, toggles |
| `{motion.duration-base}` | 200ms | Menus, tabs, toasts in and out |
| `{motion.duration-slow}` | 320ms | Modals, page-level transitions |
| `{motion.duration-thinking}` | 1200ms | One cycle of the thinking indicator |
| `{motion.easing-standard}` | cubic-bezier(0.2, 0, 0, 1) | Most transitions |
| `{motion.easing-enter}` | cubic-bezier(0, 0, 0, 1) | Elements entering |
| `{motion.easing-exit}` | cubic-bezier(0.3, 0, 1, 1) | Elements leaving |

- **Thinking indicator (signature):** three 8px amber dots that fade between 30% and 100% opacity in sequence (0, 160, 320 ms delays) over `{motion.duration-thinking}`. It shows while the model is working, before text streams in.
- **Streaming text** appears as it arrives. Don't fake typewriter effects for content that's already complete.
- **Fades and small moves only** (≤ 8px). No bounces, springs, parallax or spinning logos.
- **Respect `prefers-reduced-motion`:** disable transitions and show the thinking dots static at full opacity, with "Thinking…" text for screen readers.

## Components

Reference CSS for everything below lives in `css/components.css` (classes prefixed `tr-`), and it's demonstrated live in `index.html`.

### Top navigation
**`top-nav`**: sticky, 60px tall, bone at 92% opacity with a background blur and a hairline bottom border. The ink wordmark sits at the left (`logos/final/thinkingraven-wordmark-ink.svg`, 22px tall). Links in `{typography.nav-link}` sit centre-right, and one `button-primary` sits at the far right. Below 900px the links collapse into a menu button.

### Buttons
- **`button-primary`**: amber pill with ink label, 44px tall, 12×20px padding, `{typography.button}`. **One per view.** Press → `button-primary-active` (#D98F22); disabled → `button-primary-disabled`.
- **`button-secondary`**: transparent pill with a 1px ink border and ink label. The default for every other action.
- **`button-secondary-on-dark`**: the same on dark surfaces, with a 1px bone border and bone label. Never put an amber *and* a white button side by side on dark.
- **`button-ghost`**: text-only pill for tertiary actions ("Cancel", "Skip"); press fills `{colors.surface-strong}`.
- **`button-icon-circular`**: a 40px white circle with a hairline border and an ink 20px icon, for copy, regenerate, share and send.
- **`text-link`**: ink text with a 2px amber underline (offset 3px). On dark surfaces it's bone text with the amber underline. The amber underline is the link signal; the text itself stays readable ink.

### Cards & containers
- **`feature-card`**: white, hairline border, `{rounded.lg}`, 32px padding. A 24px icon, then a `{typography.title-md}` title, then `{typography.body-md}` in `{colors.muted}`.
- **`product-card-dark`**: `{colors.surface-dark-elevated}` with a hairline-dark border, for showing product UI inside dark bands.
- **`code-window`**: `{colors.surface-dark-soft}`, `{rounded.md}`, with a 36px header bar holding three 8px dots in `{colors.hairline-dark}` (no traffic-light colours) and a mono filename in `{colors.on-dark-soft}`. The body is `{typography.code}` and scrolls horizontally rather than wrapping. Syntax colours: keywords amber #F2A93B, strings #7BD88F, comments #8A8A98, everything else bone.
- **`callout-card-amber`**: a full amber card with ink text and a `button-secondary` (ink outline). Use at most once per page.
- **`cta-band-dark`**: an ink band with `{rounded.xl}` and 64px padding, a `{typography.display-sm}` headline (the split-weight style is allowed), and a `button-primary`.

### Chat (AI-native)
- **`chat-bubble-assistant`**: white card with a hairline border, `{rounded.lg}`, 14×18px padding, `{typography.body-md}`, left-aligned at full column width. A 28px avatar tile (`logos/final/thinkingraven-avatar-dark.svg`) sits to its left. Code inside uses `code-window`. Copy and regenerate actions use `button-icon-circular` (32px) and appear under the message.
- **`chat-bubble-user`**: ink surface, bone text, `{rounded.lg}`, right-aligned, max 80% width. There's no avatar; the alignment says who's talking.
- **`thinking-indicator`**: three amber dots (8px, 6px gap) in a small white bubble, animated per the Motion section. Pair it with visually hidden "Thinking…" text (`aria-live="polite"`).
- **`prompt-composer`**: a white box with `{rounded.lg}`, hairline border and 16px padding. It holds an auto-growing textarea (`{typography.body-md}`, placeholder in `{colors.muted-soft}`), with a bottom row for attach and tool buttons (`button-ghost`, icon only) and a **send** button (40px amber circle with an ink arrow) on the right. On focus, the border turns ink and the focus ring shows.

### Inputs & forms
- **`text-input`**: white, 1px hairline border, `{rounded.md}`, 44px tall, 10×14px padding, `{typography.body-md}`. The label sits above in `{typography.title-sm}` (14px, 600); helper text sits below in `{typography.caption}` `{colors.muted}`.
- **`text-input-focused`**: ink border plus `{elevation.focus-light}`.
- **`text-input-error`**: `{colors.error}` border, with helper text in `{colors.error}` prefixed by "Error:" or an icon.
- **Checkbox / radio:** 18px, `{rounded.xs}` (checkbox) or full (radio), hairline border. When checked, the fill is **ink** with a bone check, not amber, to keep amber scarce.
- **Switch:** 36×20px pill, `{colors.surface-strong}` off and ink on, with a white knob.

### Tags / badges
- **`badge-pill`**: `{colors.surface-strong}` background, ink `{typography.caption}`, pill, 4×12px padding. For categories and counts.
- **`badge-amber`**: amber with ink `{typography.kicker}` (Mono, uppercase), for "NEW" and "BETA" only.
- **`status-dot`**: an 8px circle in a semantic colour, always next to a text label.

### Tabs / filters
**`category-tab`** and **`category-tab-active`**: pills in `{typography.nav-link}`. Inactive tabs are transparent with `{colors.muted}` text; the active tab is an ink pill with bone text. Tabs scroll horizontally on mobile rather than wrapping.

### Feedback
- **`alert`**: soft semantic background with a 1px semantic border, `{rounded.md}`, and an icon plus ink text. Variants: info, success, warning, error.
- **`toast`**: ink pill with bone `{typography.body-sm}` and `{elevation.md}`, bottom-centre, auto-dismissed after 4s, entering with `{motion.duration-base}`. Action links inside use `text-link-on-dark`. In dark mode it inverts to a bone pill with ink text, so it stays visible against the dark canvas.
- **Empty states:** the Thinky mascot at 96–120px, one `{typography.title-md}` line, one `{typography.body-sm}` line, and one `button-secondary`. On dark surfaces, Thinky sits on a bone disc (it's a black raven and would disappear otherwise).

### Avatars
**`avatar`**: circles at 24, 32 or 40px. The assistant avatar is the `tr.` tile; user avatars are photos or initials (ink on `{colors.surface-strong}`, 600 weight).

### CTA / footer
**`footer`**: canvas background with a hairline top border and `{typography.body-sm}` in `{colors.muted}`. It holds contact details (hello@thinkingraven.com), social links (X/Instagram @thinkingravenai, GitHub, LinkedIn, Patreon) and legal links. The wordmark appears at the top-left at 22px.

## Accessibility
- **Contrast:** all text tokens meet WCAG AA (4.5:1) on their intended surfaces; see the tables above. Amber is never text on light surfaces (1.7:1).
- **Focus:** always visible, using the ink ring on light and the amber ring on dark. Never `outline: none` without a replacement.
- **Targets:** at least 44×44px for touch (buttons are 44px tall; icon buttons are 40px, with a 44px hit area).
- **Motion:** honour `prefers-reduced-motion` (see Motion).
- **Not colour alone:** status, links and errors also carry an icon, an underline or a word.
- **Images:** the logo's alt text is "Thinking Raven". Decorative mascot art uses `alt=""`. Every icon-only button needs an `aria-label`.
- **Live AI output:** stream into a region with `aria-live="polite"`; announce "Thinking…" while waiting.

## Do's and don'ts

### Do
- Anchor pages on the bone canvas. Use white for cards, and ink for hero and product bands.
- Keep amber for **one** primary action per view, the wordmark dot and the thinking indicator.
- Use bold, tight Space Grotesk for display text, regular for body, and Space Mono for code and kickers.
- Use the split-weight headline for hero and section openers, at most once per screen.
- Show real product chrome (chat, code, answers) instead of abstract AI imagery.
- Use the ink focus ring on light surfaces and the amber ring on dark ones.
- Pace pages: bone → white cards → ink band → bone → amber callout (optional) → footer.

### Don't
- Don't use pure white or cool grey as the page background.
- Don't introduce new accent colours (no blue, purple or teal brand moments, no gradients, no glows).
- Don't set text in amber on light surfaces, or put white text on amber.
- Don't use more than one amber button in a view.
- Don't use light weights (300) for display, or bold for body paragraphs.
- Don't use title case or ALL CAPS headlines (kickers are the only uppercase).
- Don't retype, recolour or distort the wordmark.
- Don't animate with bounces or springs, and don't fake typewriter text.

## Responsive behavior

### Breakpoints

| Name | Width | Key changes |
|---|---|---|
| Mobile | < 640px | Nav links collapse to a menu; display-xl 72 → 40px (clamp); grids 1-up; chat full-width with the composer pinned; buttons can be full-width |
| Tablet | 640–1023px | Grids 2-up; display-xl about 56px; nav links appear from 900px |
| Desktop | 1024–1439px | Full nav; 3-up feature grids; container 1120px |
| Wide | ≥ 1440px | Same as desktop with more outer space; the container stays at 1120px |

Use fluid type for display sizes, e.g. `font-size: clamp(40px, 6vw, 72px)`.

### Touch targets
Buttons are 44px tall, icon buttons 40px with a 44px hit area, inputs 44px, and tabs at least 36px tall with padding that expands the hit area to 44px.

### Collapsing strategy
- The nav collapses to a menu button below 900px; the primary button stays visible.
- Split heroes stack: text first, then media.
- Grids reduce columns; they never shrink cards below 260px.
- Tables and code windows scroll horizontally inside their containers; the page itself never scrolls sideways.
- In chat, the composer stays pinned to the bottom, and user bubbles go up to 88% width on mobile.

### Image behavior
Images scale to their container (`max-width: 100%`) with explicit width and height to prevent layout shift. The mascot keeps its aspect ratio. Social banners are pre-cut for each platform (see `exports/`).

## Iteration guide
1. Work on **one component at a time**, referencing its key (e.g. `{component.prompt-composer}`).
2. Variants (`-active`, `-disabled`, `-focused`, `-error`) are separate entries under `components:`.
3. Always use token references (`{colors.*}`, `{spacing.*}`) or CSS variables (`--tr-*`). Never inline new hex values.
4. Document the default, active/pressed, disabled, focused and error states. Hover is optional: a subtle change only (darker press colour or `{elevation.sm}`).
5. Bone, ink and amber are the whole palette. Semantic colours are for status only.
6. When in doubt about emphasis, use **size or weight before colour**, and never more amber.
7. Keep `DESIGN.md`, `tokens/`, `css/components.css`, `index.html` and `AGENTS.md` in sync.

## Known gaps
- **The product UI isn't designed yet.** The chat, composer and dark-mode specs are system-level starting points and haven't been validated in a real app.
- **The semantic colours are provisional:** they're tested for contrast but not yet used in real flows.
- **Icons use Lucide**, a third-party set. A custom raven glyph or icon set hasn't been made.
- **The mascot has one pose.** Expressions (thinking, success, error) and motion for Thinky aren't designed yet.
- **There's no photography direction** beyond the rules in Imagery.
- **Data-visualisation colours** aren't defined. Until they are, use ink and muted tones with amber for the single highlighted series.
- **The tagline** "AI that thinks before it speaks" is a placeholder.
