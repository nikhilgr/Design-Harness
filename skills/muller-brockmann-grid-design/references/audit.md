# Grid audit guide

Use this guide to critique an existing layout or to verify a newly created one. Inspect the rendered artifact, not only its specification.

## Severity

- **Critical:** Prevents reading, interaction, navigation, or production; creates inaccessible or impossible output.
- **Major:** Breaks hierarchy, repeated alignment, responsive behavior, or a core content relationship across multiple elements.
- **Moderate:** Weakens rhythm, legibility, or consistency but remains usable.
- **Minor:** Local refinement with little effect on understanding.

## Diagnostic sequence

### Content and medium

- Is the intended reading order obvious?
- Are the format, viewport, reading distance, trim, binding, safe areas, and interaction constraints accounted for?
- Does the system accommodate the longest title, densest data, smallest screen, and common missing-content states?

### Typography

- Is the body measure comfortable with the chosen type size and leading?
- Do headings, captions, labels, and body text form a clear hierarchy?
- Do different type sizes resolve to compatible line-box multiples where alignment depends on them?
- Are rag, word spacing, and paragraph intervals controlled?

### Structure

- Can you infer repeated columns, gutters, baselines, and horizontal anchors from the layout?
- Are margins and safe areas purposeful rather than accidental or mechanically equal?
- Are vertical fields based on whole text lines or another coherent interval?
- Are nested grids tied back to parent anchors?
- Is the grid finer than the content requires?

### Composition

- Do related items share an edge, baseline, or interval?
- Are image, chart, card, and color-field sizes drawn from a limited family?
- Are captions attached to their objects without crowding?
- Does white space separate levels and create direction?
- Do exceptions preserve an anchor and deliver a clear benefit?

### System behavior

- Across pages or states, are recurring elements placed predictably?
- Across breakpoints, is the grid re-derived rather than compressed?
- Are tokens or measurements implementable without fractional drift or contradictory rules?
- Does the final view work without visible grid lines?

## Report format

For each issue, state:

1. **Symptom:** What is visible and where.
2. **Cause:** The failed relationship, not merely a taste judgment.
3. **Impact:** Reading, navigation, hierarchy, accessibility, or production consequence.
4. **Repair:** Exact alignment, interval, span, type, or responsive change.
5. **Preserve:** What already works and should remain.

End with the smallest coherent rule set that would prevent the issues from recurring. Avoid solving a systemic problem with many one-off offsets.
