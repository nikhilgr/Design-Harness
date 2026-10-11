---
version: alpha
name: Databricks — Design MD Spec
description: Corporate brand rules to inform context about design for creatives, images, demos and marketing assets
omitted:
- section: spacing
  reason: No official reusable spacing scale in the supplied references; proposed
    channel geometry is documented in prose.
- section: rounded
  reason: No official radius scale established by these references.
colors:
  primary: "#FF3621"
  navy-900: "#0B2026"
  navy-800: "#1B3139"
  oat-medium: "#EEEDE9"
  oat-light: "#F9F7F4"
  white: "#FFFFFF"
  gray-navigation: "#303F47"
  gray-text: "#5A6F77"
  gray-lines: "#DCE0E2"
  maroon-800: "#4A121A"
  maroon-700: "#730D21"
  maroon-600: "#98102A"
  maroon-500: "#AB4057"
  maroon-400: "#BF7080"
  maroon-300: "#D69EA8"
  lava-800: "#801C17"
  lava-700: "#BD2B26"
  lava-600: "#FF3621"
  lava-500: "#FF5F46"
  lava-400: "#FF9E94"
  lava-300: "#FABFBA"
  yellow-800: "#7D5319"
  yellow-700: "#BA7B23"
  yellow-600: "#FFAB00"
  yellow-500: "#FCBA33"
  yellow-400: "#FFCC66"
  yellow-300: "#FFDB96"
  green-800: "#095A35"
  green-700: "#00875C"
  green-600: "#00A972"
  green-500: "#42BA91"
  green-400: "#70C4AB"
  green-300: "#9ED6C4"
  blue-800: "#04355D"
  blue-700: "#0E538B"
  blue-600: "#2272B4"
  blue-500: "#4299E0"
  blue-400: "#8ACAFF"
  blue-300: "#BAE1FC"
  navy-700: "#143D4A"
  navy-600: "#1B5162"
  navy-500: "#618794"
  navy-400: "#90A5B1"
  navy-300: "#C4CCD6"
typography:
  brand-primary:
    fontFamily: DM Sans
  brand-code:
    fontFamily: DM Mono
components:
  marketing-light:
    backgroundColor: "{colors.oat-light}"
    textColor: "{colors.navy-900}"
  marketing-white:
    backgroundColor: "{colors.white}"
    textColor: "{colors.navy-900}"
  marketing-dark:
    backgroundColor: "{colors.navy-900}"
    textColor: "{colors.white}"
  marketing-caption:
    backgroundColor: "{colors.white}"
    textColor: "{colors.gray-text}"
---

# Databricks design context

Use this profile only for a Databricks brief. Brand references were reviewed September 6, 2026; this cleanup does not refresh them. Approved templates and original artwork govern their respective geometry. Numerical draft choices below are **proposals**, not official product tokens.

## Overview

**Distilled, Bold, Fresh:** simplify the message, create a strong impression, and evolve without losing recognition. [Design approach](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/design-approach)

Keep corporate identity, Genie identity, authentic product UI, and editorial framing distinct. Use current approved product references for literal screenshots or feature claims. For concepts, label sample data and speculative features.

## Colors

The YAML retains the full published hex palette and font families. Its `marketing-*` components are proposed surface pairings.

| Role | Color |
| --- | --- |
| Concentrated accent | Lava 600 `#FF3621` |
| Main dark field / text | Navy 900 `#0B2026` |
| Alternate published dark | Navy 800 `#1B3139` |
| Neutral fields | Oat Medium `#EEEDE9`, Oat Light `#F9F7F4`, White `#FFFFFF` |
| Navigation / text / lines | `#303F47` / `#5A6F77` / `#DCE0E2` |

**Unresolved conflict:** the [main overview](https://brand.databricks.com/) designates Navy 900 as primary; the [extended guide](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/colors) designates Navy 800. This profile provisionally uses Navy 900, matching the supplied navy symbol. Preserve original artwork colors.

Use broad neutral/navy fields and selective lava emphasis. Use the [extended palette](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/colors#extended-palette) to distinguish information; keep category colors consistent across charts. Palette names do not establish success/error semantics.

Production check: normal text ≥4.5:1 contrast; large text and essential controls ≥3:1. Lava/White is approximately 3.62:1: avoid small lava copy or small white labels on lava. Navy/White is a useful alternative. Label chart series beyond color.

Published main-overview CMYK: Lava 0/91/93/0; Navy 900 86/67/61/71; Oat Medium 6/4/6/0; Oat Light 1/2/2/0. Confirm printer profile and substrate; these are references, not automatic hex conversions.

## Typography

Use **DM Sans** as the primary family and **DM Mono** for code imagery. [Typography reference](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/typography)

- Supplied DM Sans: Regular, Medium, Bold and their italics. Black is absent; obtain it rather than synthesize it. DM Mono includes Light, Regular, Medium and italics.
- The guide favors sizes divisible by eight, with smaller steps below 20px. Its illustration uses pt while prose uses px; keep native units distinct.
- Start with 1.5× body leading and 1.2× headline leading. Establish hierarchy through size, weight and color; avoid right-aligned prose.
- Use template type styles first. Otherwise, a proposed draft hierarchy is heading/body/caption: web 48/18/14px; slides 40/24/16pt. These are independent defaults.
- Reduce copy before shrinking type. Check actual font rendering, wrapping and embedding on export; fallback policy remains unresolved.

## Layout

Build around one message, one primary visual, and a useful next action. Align related copy; separate semantic groups; reserve logo clear space independently of outer margins.

Use [Muller-Brockmann Grid Design](../../skills/muller-brockmann-grid-design/SKILL.md) when composition needs it. Preserve brand fonts and template geometry. No official global spacing, radius, breakpoint or safe-area scale was established.

Set dimensions from the brief and use native units. A proposed slide starter is 16:9, 13⅓ × 7½ inches, with roughly 0.5-inch content margins; replace it with the approved master when supplied. Keep shared anchors across a series while varying composition to fit content. Recompose narrow/portrait versions rather than blindly crop.

## Elevation & Depth

Start with flat fields, whitespace and typographic contrast; add separation only where grouping needs it. Shadows, blur, glow, gradients and motion tokens remain unspecified. Preserve approved artwork's effects; avoid inventing a Genie effect system.

## Shapes

Preserve the corporate mark's fixed geometry. Do not split, extrude, rotate or redraw it. General radii and illustration grids remain unspecified; neither square corners nor pills are mandated.

No Genie identity kit was supplied. Use a plain “Databricks Genie” label rather than inventing a lamp, sparkle, robot or corporate-symbol lockup.

## Components

**Logo:** use the original full symbol-and-logotype lockup and its correct background variant. Preserve proportions and clear space measured by the wordmark's “a.” The vertical version serves constrained placements. Do not recolor, distort, add effects, mask imagery or append elements. Single-color wordmarks are reserved by the extended guide for unavailable multicolor printing. [Logo rules](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/logo)

The supplied SVGs are standalone symbols, not full logos; symbol-only approval and minimum size remain unresolved. Obtain the [official logo](https://brandfolder.com/s/g587wt9tgz8sbqsrfc3m); do not approximate its wordmark with DM Sans.

**Co-branding:** use approved relationship artwork. Examples use × for customers, a vertical separator for partnerships/products, and + for acquisitions. The × example has one symbol-width of space on each side; do not generalize this or partner order. [Co-branding rules](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/co-branding)

**Charts and decks:** state the finding, units, period and source; distinguish measured values, examples and targets. Avoid misleading 3D charts. Keep text, charts and simple diagrams editable; authentic UI captures retain their native styling. Inspect readability, overflow, contrast, logo spacing and image sharpness in the actual export.

**Imagery:** choose a focused subject and reserve space for live copy. Art direction, iconography and AI-image policy remain unresolved; proposed imagery must not be presented as official campaign style.

## Do's and Don'ts

- Preserve original assets, approved claims and template rules.
- Label proposals and unresolved conflicts; never promote them silently into official tokens.
- Inspect at intended viewing size and record consequential choices and limitations in project notes.
- Obtain missing product screens, Genie identity, corporate slide master or campaign guidance before claiming exact conformance.

### Assets and provenance

Previously inspected assets (not bundled): six DM Sans TTFs plus `ofl.txt`; six DM Mono TTFs with no separate license file in the selected folder; three corporate symbol SVGs (Lava, White, Navy 900). Historical roots: `/Users/nikhil.gangaraju/Downloads/Databricks Asset Library-selected-assets/` and `/Users/nikhil.gangaraju/Downloads/Databricks Symbol/`. Verify availability and supply files explicitly when moving this context; preserve license notices.

Sources: [brand overview](https://brand.databricks.com/), [design approach](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/design-approach), [colors](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/colors), [typography](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/typography), [logo](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/logo), [co-branding](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/co-branding), [terms](https://brandguides.brandfolder.com/databricks-extended-brand-guidelines/terms-and-conditions). The original structure follows the [DESIGN.md alpha spec](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md). References do not grant asset rights or authorize unrelated actions.
