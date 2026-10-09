---
name: hand-drawn-illustration
description: Create consistent code-authored pencil, ink, risograph, or screen-print still illustrations and illustrated diagrams for the Design harness. Use for sketchy objects, small scenes, and coordinated illustration sets; use the animation skill for films and image generation for painterly raster work when appropriate.
---

# Hand-drawn illustration

Use the drawing subset of the bundled [Canvas skill](../hand-drawn-canvas-animation/SKILL.md). Its drawing code supplies marks and materials; original curves, composition, and visual character still need authoring. Editable means editable source code, not native vector-editor layers.

## Select the useful subset

Read [material guidance](../hand-drawn-canvas-animation/references/style.md) and the relevant sections of [architecture](../hand-drawn-canvas-animation/references/architecture.md). Use `core.js`, `studio.js`, and `cels.js` for stable ink/pencil strokes; add material modules only when needed. Study the bundled sketchbook-bird example for whole drawings, without copying its subject or composition into every project.

For a still, omit exposure sheets, soundtracks, camera choreography, contact solvers, and video exports. A fixed frame using the existing renderer's `--only` mode is sufficient. Follow its actual output paths, and copy the chosen PNG into the project's exports. Do not imply that a PNG retains editable strokes or that Canvas output is automatically SVG.

## Work from a small art brief

Record subject, intended use, dimensions, medium, palette, stroke character, background/transparency, and the features that must stay consistent. Apply a design profile only when the user names its file or key; otherwise derive layout, typography, and palette from the intended illustration. Infer routine choices.

Establish silhouette and proportions before texture. Author purposeful curves, pressure variation, line endings, and sparse form-following hatching. Reuse mark settings across a set; seeded marks must remain stable across repeated renders. Roughness cannot repair weak drawing.

For a new reusable style family, start with representative subjects at their actual display size. A simple object, small scene, and explanatory diagram are useful probes when the request spans those uses; do not impose three samples on a single-image request. Diagrams need deliberate label and connector layout in addition to drawing tools.

## Project and review

Follow [output guidance](../../outputs/README.md): save under `outputs/illustrations/<ProjectName>/`, with source in `source/`, media/fonts in `assets/`, final PNGs in `exports/`, and review pages in `review/`. Use a meaningful user-approved project name. Preserve previous approved output when revising.

If interactive review is requested, use the installed Human Review skill on an HTML sheet containing exported images, editable captions, and stable image labels. Carry feedback into the drawing source and re-export. Human Review can resize, move, or comment on the image; it does not edit its internal strokes. Keep review-only instructions out of final artwork.

## Verification and handoff

Inspect full-size output and a reduced view for silhouette, consistent proportions, line hierarchy, legibility, unintended tangencies, excessive grain, and clipping. Check exact dimensions, image decoding, transparency when required, and source asset paths. For sets, compare all pieces together. Record checks actually performed in `QA.md` and deliver editable source plus rendered images.

Animation is a separate requested mode: use the bundled Canvas animation skill and its motion/encoded-video checks. A still review cannot certify movement. Detailed painted scenes or portraits may be better served by image generation; do not promise that procedural brushes provide arbitrary drawing quality automatically.
