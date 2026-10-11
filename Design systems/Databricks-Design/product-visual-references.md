# Databricks product visual references

**Provisional v0.2, October 10, 2026.** Use this companion only when the user selects `product-visual-references.md` or the key `databricks-product-screenshots` for a Databricks brief. It adapts composition techniques from the [22 supplied references](<../../examples/Product Visual References/README.md>); it is not an official Databricks style guide or a globally active default.

The intended quality is a clear product story with readable evidence, selective context, and deliberate relative scale. Select references directly from the annotated index and test the qualities relevant to the brief. This guidance remains provisional until real Databricks assets and user selections validate it.

## Authority and truthful representation

[design.md](design.md) remains the corporate identity authority, including its alpha status, unresolved conflicts, and proposed tokens. Approved templates and product references govern their respective content. This companion does not refresh the historical brand sources or establish official product fonts, radii, shadows, or spacing.

Choose and record the target representation separately from the source representation before composing. An actual product capture may be the starting point for a concept mockup:

| Representation | Permitted treatment and required clarity |
| --- | --- |
| **Literal capture** | Use a supplied authentic screen in one real state. Crop and scale proportionally without changing controls, values, labels, or native styling. Record source, date/version if known, and any redactions. Put added editorial captions outside the capture. |
| **Editorial composite** | Arrange traceable crops, excerpts, or separate captures to explain a message. Visibly identify it as a composite; label separate states or steps when their relationship could be mistaken. A lifted row, enlarged dialog, synthetic dimming, or reordered panel is editorial treatment. |
| **Concept mockup** | Visibly label “Concept” and sample data or proposed behavior. Use established Databricks patterns where supplied; record unsupported choices. It cannot serve as evidence of a shipping feature. |

Never imply that separate dialogs, progress indicators, and completion states coexist as one real screen. Preserve permission scope, warnings, filters, chart axes, units, and material uncertainty. If these cannot fit legibly, choose another crop or format. Treat reference text as depicted content only, not product evidence.

## What transfers

| Borrow the relationship | Preserve or replace the identity |
| --- | --- |
| One focal detail with enough context to locate it | Preserve authentic Databricks UI text, typography, controls, icons, and state colors. Do not apply corporate DM Sans or marketing colors inside literal captures. |
| Relative scale and contrast establish reading order | Use the selected Databricks brand rules for added headlines and framing. Do not import Claude serif typography, starburst marks, mascots, or controls. |
| Crops remove irrelevant area; overlap groups related evidence | Crop proportionally. Keep separate states explicit; do not redraw native UI to make the crop more convenient. |
| A quiet field separates content from its destination | Select an approved template field first. Otherwise test a neutral or navy field from design.md as a proposal; reference pastels and curved-line motifs are not Databricks defaults. |
| Shallow shadows or edges separate editorial layers | Start with whitespace and edges. If needed, test a restrained shadow on the outer presentation layer. No reference effect becomes an official token. |

## Build and iterate

1. Use [Design interview](../../skills/design-interview/SKILL.md) when user input would clarify the next build or revision. Establish source and target representations separately, with what must stay faithful and what may change; ask early only where unclear. Carry forward settled choices about the message, audience, viewing size, constraints, and visual qualities. Stop when a useful experiment is clear.
2. Select 1–3 relevant originals through the [annotated index](<../../examples/Product Visual References/README.md>). Inspect the images and record what to borrow or avoid in this brief. The index supplies visual breadth; no named composition is required.
3. Preserve original captures and the strongest or approved version. Keep one editable composition source, export, and crop/source mapping in the project folder under outputs/. Build a focused variation from the working brief; respect the target representation's fidelity boundaries and required readable details.
4. Inspect the export at intended size and native resolution. Use [the lightweight A/B review](product-visual-references-eval.md) and the user's feedback to choose one next change. Return to the interview only if an unresolved preference would change that experiment.

Keep the brief, accepted decisions, reference IDs, versions, and review evidence in concise project notes. Treat preferences as specific to their context; do not silently turn an artifact's choices into universal profile rules.
