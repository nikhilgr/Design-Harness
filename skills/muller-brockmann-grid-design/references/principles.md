# Grid-system principles

Use this reference to construct or adapt a grid. The principles are paraphrased from Josef Muller-Brockmann's *Grid Systems in Graphic Design* and translated for contemporary print and screen work.

## 1. Order serves communication

A grid should clarify priorities, make complex material easier to navigate, and create continuity across many pages, states, or formats. Judge it by whether it improves understanding, not by whether the underlying geometry is obvious.

The system should be reproducible and economical, but efficiency is not its only aim. It must also create a coherent rhythm and enough contrast to sustain attention.

## 2. Typography supplies the base unit

Start with representative text, not empty boxes.

- Choose the body type and reading size for the actual medium and distance.
- Set column width together with size and leading. Excessively long lines tire the eye; very short lines interrupt reading rhythm.
- The book proposes about seven words per line for sustained text and demonstrates useful ranges around seven to ten. Treat that as a testable starting point, not a universal quota.
- Use leading to create a stable baseline rhythm. Tight leading can cause adjacent lines to be taken in together; excessive leading fragments paragraphs.
- Keep letter spacing and word spacing even enough that line endings, not gaps inside the line, carry the rhythm.
- Derive display sizes from the same interval system when possible. Different type sizes can share a module when their line boxes resolve to a common multiple.

## 3. The live area and margins are part of the composition

The type or content area must sit convincingly inside the page, screen, or physical surface. Margins control handling, emphasis, and tension.

- Consider binding, trim, touch targets, browser chrome, device insets, and viewing distance.
- Equal margins often produce a static or indecisive page. Deliberate asymmetry can create direction and leave functional room for folios, controls, notes, or handling.
- On facing pages, treat the spread and the binding relationship as a system rather than designing two isolated rectangles.

## 4. Construct the grid from compatible measures

Let:

- `W` be the live width;
- `n` be the number of columns;
- `G` be the gutter;
- `C` be a column width.

Then `C = (W - (n - 1)G) / n`.

Choose `n` only after testing the narrowest text measure, common image ratios, and recurring components. More columns create more combinations but also more opportunities for arbitrary placement.

For the vertical structure:

- select a baseline interval `B` from the body line height;
- define each horizontal field as a whole number of text lines;
- separate fields by one or more whole baseline intervals when practical;
- make the top and bottom of images, rules, and color areas meet shared horizontal anchors;
- reserve enough inter-field space for captions without breaking the baseline rhythm.

An element may span several fields. Its outer edges should still resolve to the grid, and adjacent captions or text should share a visible alignment.

## 5. Use a restrained family of sizes

Pictures, charts, cards, and color areas should normally occupy one or more whole grid fields. A limited set of spans makes importance legible and creates unity across diverse material.

Fewer size changes create a quieter result. More contrast can create energy, but each new size should serve priority, sequence, or content rather than novelty.

Avoid cropping every image to one arbitrary shape. Preserve meaningful content and choose among the system's allowed spans or nested fields.

## 6. White space is an interval with a job

Unprinted or unoccupied space can separate levels, create rest, direct the eye, and increase the apparent importance of nearby content. Specify important spaces as deliberate multiples of the baseline or module instead of treating them as residue.

Do not fill every field. The grid organizes available positions; it does not require all positions to be occupied.

## 7. Hierarchy and navigation must remain visible

Titles, subtitles, body text, captions, folios, controls, and legends should have stable relationships. Use position, span, weight, size, color, and white space in a controlled combination.

Page numbers and recurring navigation belong to the grid. Their placement should extend or reinforce an existing alignment rather than float near an edge.

The reader should be able to identify the first, next, and supporting elements at a glance. A mathematically regular page that obscures priority has failed.

## 8. The grid permits disciplined variation

A strong grid can support quiet, dense, asymmetrical, and image-led compositions. Explore variations by combining fields, leaving fields empty, changing spans, or shifting emphasis while retaining common anchors.

Breaking the grid can be effective when it creates a clear benefit such as emphasis, scale, or a transition. Preserve at least one intelligible relationship and ensure the exception remains exceptional.

## 9. Adapt the logic to contemporary media

- **Responsive interfaces:** Use separate column counts, margins, and module choices at meaningful breakpoints. Preserve hierarchy and spacing logic rather than scaling every measurement.
- **Data-heavy layouts:** Align plots, labels, legends, and tables to shared columns; let data-label fit and comparison tasks influence the grid.
- **Slides:** Use fewer, larger fields; account for distance and presentation-safe areas.
- **Design systems:** Encode spacing, columns, and spans as tokens, but keep component content and accessibility as higher-order constraints.
- **Exhibitions and environmental graphics:** Extend the system across walls, floor, ceiling, products, and wayfinding. Viewing height, circulation, material, and lighting affect the module.

## 10. Verification questions

- Does the grid emerge from actual content and medium constraints?
- Can the body text be read comfortably at the intended distance?
- Are column widths, leading, and vertical fields compatible?
- Do important edges and baselines repeat consistently?
- Are gutters and caption spaces sufficient?
- Are image and component sizes limited but expressive?
- Does white space create hierarchy and rhythm?
- Can the same system produce several coherent layouts?
- Do exceptions communicate more clearly than a conforming alternative?
- Does the design still work when the grid overlay is hidden?
