---
name: muller-brockmann-grid-design
description: Design or audit content-led typographic and modular grid systems inspired by Josef Muller-Brockmann. Use for editorial pages, reports, posters, interfaces, dashboards, slide systems, identity systems, and exhibition graphics where typography, alignment, hierarchy, repeatable spatial rules, or responsive adaptation matter. Do not invoke for isolated artwork or requests concerned only with surface decoration.
---

# Muller-Brockmann Grid Design

Treat the grid as a measurable ordering system derived from the communication problem. It is not a preset column count, a visible motif, or a substitute for composition.

## Choose the mode

- **Construct:** Define a new grid and apply it to a layout or design system.
- **Audit:** Diagnose an existing layout, identify structural causes, and propose precise repairs.
- **Adapt:** Carry an established system across formats or breakpoints without merely scaling it.

Read [references/principles.md](references/principles.md) when constructing or adapting a grid. Read [references/audit.md](references/audit.md) when reviewing an existing design. Read [references/source-map.md](references/source-map.md) only when source attribution or the book's print-era reasoning is useful.

## Construct or adapt

1. **Inventory the problem before drawing lines.** Establish medium, format or viewport, content types, reading distance, sequence, production constraints, recurring elements, and accessibility needs. Mark content priority and likely image or data aspect ratios.
2. **Establish typography first.** Choose body size, leading, measure, paragraph treatment, and display relationships with actual representative content. For sustained reading, use the book's roughly seven-to-ten-words-per-line guidance as a starting hypothesis, then test it in the chosen typeface and medium.
3. **Define the live area.** Set margins or safe areas as purposeful proportions, accounting for binding, trim, controls, device insets, or viewing distance. Do not default to equal margins when asymmetry improves balance, handling, or navigation.
4. **Derive the grid.** Select the fewest columns and vertical fields that accommodate the real content. Set gutters from typography and caption needs. Make horizontal modules compatible with the baseline rhythm. Allow whole fields to combine into larger areas.
5. **Map content to the system.** Align text, titles, images, captions, rules, controls, and folios to shared edges and repeated intervals. Use a limited family of image and component sizes so importance is visible without arbitrary variation.
6. **Compose variations.** Produce at least two materially different arrangements from the same system when the task benefits from exploration. Preserve shared anchors while varying span, position, white space, and sequence. A grid should make variation coherent, not make every page identical.
7. **Verify both structure and experience.** Inspect the layout with a grid or baseline overlay, then hide it and judge hierarchy, reading order, rhythm, density, and tension. Test edge cases: longest text, smallest viewport, missing image, dense data, and repeated pages or states.

For responsive work, re-derive the grid at meaningful breakpoints. Preserve hierarchy, interval logic, and component relationships; do not proportionally shrink a desktop grid onto a small screen.

## Audit

Find the smallest set of structural causes that explains the visible defects. Distinguish grid failures from typography, content, or production failures. Report issues in priority order and pair every criticism with a measurable repair. Use the checklist and severity definitions in [references/audit.md](references/audit.md).

## Non-negotiable decisions

- Derive the grid from content and constraints; never force a familiar 12-column or fixed-field preset without evidence.
- Keep body typography, column width, leading, baseline rhythm, field height, and vertical gaps mathematically compatible.
- Reserve gutters and inter-field gaps for separation and captions; adjacent images or blocks must not collide accidentally.
- Align important edges deliberately. If an element breaks the grid, maintain at least one intelligible anchor and explain the communication benefit.
- Use white space as an active interval, not leftover area.
- Keep hierarchy understandable without showing grid lines.
- Prefer a small system that yields many useful combinations over a fine mesh that adds options without improving the content.
- Do not imitate the book's mid-century surface style unless the user asks for it. Apply its logic with appropriate contemporary type, color, interaction, and accessibility standards.

## Output contract

When designing, provide:

- the content and constraint assumptions;
- a grid specification with format, margins or safe areas, columns, gutters, baseline, horizontal modules, and allowed spans;
- a content-to-grid map for key elements;
- responsive or cross-format behavior when relevant;
- verification evidence or a clear inspection checklist.

When auditing, provide:

- the observed symptom;
- the underlying rule or relationship that failed;
- severity and user impact;
- a measurable correction;
- what should remain unchanged.

If the deliverable is visual, show a normal view and, when practical, a separate diagnostic overlay. Do not leave construction lines visible in the final design unless requested.
