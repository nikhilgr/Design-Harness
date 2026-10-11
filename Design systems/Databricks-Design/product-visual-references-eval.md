# Databricks product visual references review

**Provisional v0.2, October 10, 2026.** Use with the selected [presentation profile](product-visual-references.md) to improve a specific asset through small A/B comparisons. This is a manual visual review, not a calibrated benchmark or an automatic similarity score. No real Databricks candidate has yet been assessed; the cases below are hypothetical.

## Run one comparison

1. **Fix the brief.** Write the message, audience, source representation, target representation, fidelity boundaries, output dimensions, intended display dimensions, and the details that must remain readable. Judge fidelity against the agreed target, not an assumption that screenshot input requires literal output. Choose 1–3 relevant [reference originals](<../../examples/Product Visual References/README.md>) and identify what each contributes. Keep this set fixed for the round.
2. **Preserve A.** Save the baseline export and editable source/version. Create B by changing one major variable, such as crop, foreground scale, or depth. Keep content, claims, output size, and other treatments consistent. Record unavoidable differences.
3. **View fairly.** Open A, B, and references in the actual review medium at matched intended display dimensions and the same zoom/background. Fit without stretching or silent cropping; record any aspect-ratio mismatch. For example, a 1920 × 1080 export intended for 960 × 540 display is first judged at 960 × 540, not only enlarged. For a narrow destination, select or explicitly define a relevant reference crop and retain its original link. Also inspect candidate exports at native resolution for defects. A contact sheet alone is insufficient for text checks.
4. **Check gates, then compare.** Record gate status for each candidate before considering aesthetic closeness. For eligible pairs, choose A, B, tie, or uncertain using the dimensions below. Cite visible regions and their effect on the message; do not infer quality from filenames or source code.
5. **Keep a result and a next move.** Preserve both versions, the assessment, user preference if supplied, and one prioritized next change. A reviewer recommendation remains provisional until the user chooses. On a tie keep the baseline; on uncertainty identify the missing evidence rather than force a winner. After roughly three wins, or before reusing a treatment across a series, test it on another brief or composition held out from tuning. Record whether the preference transfers; do not generalize one win into a universal rule.

## Hard gates

Use **pass**, **fail**, or **unknown** for each candidate, with evidence. A failed or unknown gate makes a candidate ineligible for an aesthetic win. Fix a failure or obtain the missing evidence first. A passing candidate can be retained over an ineligible one, but that is a validity decision, not a similarity win. If both are ineligible, there is no winner.

| Gate | Pass requires |
| --- | --- |
| Truthful UI and claims | Literal screens match their supplied authentic sources. Composites visibly disclose editorial assembly and distinguish separate states. Concepts visibly disclose speculative behavior and sample data. Crops preserve material qualifiers; values, permissions, charts, and result claims are supported for the chosen representation. |
| Databricks identity | Native UI retains its own styling; editorial additions follow the applicable approved Databricks assets/template and design.md. No imported Claude identity, fake Databricks mark, or foreign controls presented as Databricks. Unknown official details remain identified as proposals, not certified tokens. |
| Readable output | Every detail needed for the message, units, qualifiers, and representation label is readable at the intended display size. No clipping or distortion changes meaning. Small incidental context can remain subordinate if it is not needed to substantiate the claim. |
| Traceable references | Candidate export and editable source/version are recorded, with UI source/crop mapping, reference filenames/IDs, and disclosed provenance limits. The source index's unverified attribution is acceptable for aesthetic reference; it is not authentic Databricks product evidence. |

## Aesthetic comparison

For each relevant dimension, write **A**, **B**, **tie**, or **uncertain**, then one visible observation. These anchors guide subjective judgment; they have not been calibrated. Do not add them into a numerical total. Reward transferable relationships, not pixel resemblance to another brand.

| Dimension | Weaker fit | Stronger fit |
| --- | --- | --- |
| Composition and focus | Several elements compete; the viewer cannot locate the intended feature. | The chosen focal detail is immediate and reading order supports the message and selected reference qualities. |
| Context and density | Irrelevant chrome overwhelms the feature, or the crop removes its location or meaning. | Context answers where/why while the feature has enough room; breadth is used only when the brief calls for it. |
| Typography hierarchy and readability | Added copy competes with UI or hierarchy requires effort, even though minimum readable details pass. | Added headline, UI detail, and caption have clear roles; native typography is preserved and reading is comfortable. |
| Spacing and relative scale | Arbitrary gaps, awkward tangencies, or mismatched scales weaken the relationship between panels. | Shared anchors and deliberate separation connect related pieces; important detail earns the largest useful scale. |
| Depth and background | Shadows, patterns, or contrast compete with evidence or make context look misleadingly disabled. | The outer field and restrained layer separation support focus, using Databricks-appropriate framing. |
| Overall craft | Rough masks, uneven edges, inconsistent treatment, or soft exports distract. | Crops, alignment, image sharpness, and repeated treatments are deliberate at both display and native size. |

The overall choice follows the brief's most important dimension and the cited tradeoffs; it need not match a majority vote. State “uncertain” when the difference is too small to judge reliably or the viewing conditions do not support a decision. User preference and reviewer assessment are separate records; preference does not erase a failed gate.

## Copyable review template

Paste into the asset's project notes. Blank fields are prompts, not completed results.

```markdown
### Screenshot comparison
Date / reviewer / profile version:
Brief: audience; one message; required readable details:
Source representation and role of each input:
Target representation:
Fidelity boundaries: must remain faithful / may change:
Export dimensions / intended display dimensions / actual review medium and zoom:
Reference IDs + file links / relevant quality of each / any reference crop:
UI source links + date/version if known / crop-to-source mapping / provenance limits:
A baseline: export link + editable source/version:
B candidate: export link + editable source/version:
One major change / other differences:
Inspection performed: intended size; native resolution; limitations:

Gates (A and B separately; pass/fail/unknown + evidence):
- Truthful UI and claims:
- Databricks identity:
- Readable output:
- Traceable references:

Eligible pair? If no, repair or missing input:
Dimensions (A/B/tie/uncertain + visible location and reason):
- Composition and focus:
- Context and density:
- Typography hierarchy and readability:
- Spacing and relative scale:
- Depth and background:
- Overall craft:

Recommendation: A/B/tie/uncertain/no eligible pair + decisive evidence and tradeoff:
User preference: pending, or exact choice and reason:
Retained version / approval status:
One prioritized next change and expected visible effect:
Holdout brief/reference and result when due, otherwise not run:
```

## Hypothetical behavior checks

These cases test how to apply the review. They describe imagined inputs and expected decisions, not measured results or supplied Databricks assets.

| Hypothetical case | Expected assessment and next action |
| --- | --- |
| **Similar framing, wrong identity:** A uses an authentic Databricks screen. B resembles S15 closely but substitutes Claude's mark, serif greeting, and controls under a Databricks heading. | B fails identity, and fails truthfulness if presented as literal Databricks UI. It cannot win on similarity. Keep A if its gates pass; rebuild B from the authentic source before comparing framing. |
| **Faithful and readable, framing can improve:** A has a verified Databricks configuration capture, approved identity, traceable sources, and readable required text, but unrelated navigation takes most of the canvas. B proportionally crops the same state to enlarge the relevant panel while retaining its section title. Brief and viewing size are fixed; S22 is the reference. | If both pass gates, recommend B when the larger panel visibly establishes focus without losing meaning. Cite that panel and retained locator. The next isolated experiment could reduce the outer margin; do not rewrite native UI. User preference is still pending. |
| **Polished but false sequence:** A shows configuration and success as labeled steps. B removes the labels and overlays success on an open configuration dialog as though captured together. | B fails truthfulness even if its layering resembles S07. Restore explicit step labels or use a real single state before aesthetic comparison. |
| **Full-size readable, destination unreadable:** B looks sharp at 1920 × 1080 but the required chart units disappear at the intended 480 × 270 display. | B fails readability. Enlarge the relevant chart crop or change the destination; do not grant a pass from native-resolution inspection alone. |
| **Unknown provenance:** B is convincing Databricks-like UI with no original capture and is labeled a literal screen. | Truthfulness and traceability are unknown, not pass. Obtain the source or explicitly rebrief it as a concept; visual plausibility proves no authenticity. |
| **Tiny or conflicting improvement:** A and B pass gates; B has a marginally softer shadow, with no reliable focus improvement. The user likes A. | Record tie or uncertain for depth, preserve the user's A preference, and retain A. Next test a more consequential variable. Before generalizing a spotlight treatment, check a held-out full-workspace brief so useful context is not lost. |

## First real evaluation

Minimum starting input: one authentic Databricks capture, one sentence stating the message, and its intended display size or destination. Establish source and target representations separately and select relevant images and observations from the index. Create a preserved baseline and one controlled variation before running the review. If only a concept is available, identify it explicitly and evaluate only that concept's stated claims. There are no completed candidate reviews, user winners, or calibrated thresholds in this framework yet.
