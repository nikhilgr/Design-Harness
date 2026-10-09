# Evaluation plan

This evaluation measures whether the skill changes design decisions, not whether an answer repeats grid vocabulary.

## Run protocol

1. Run every case in `cases.jsonl` once without the skill and once with `$muller-brockmann-grid-design` available.
2. Keep the model, tools, user prompt, source content, and output format constant.
3. Randomize the A/B presentation order for graders.
4. Grade the rendered artifact when one is produced. Use the written rationale only to interpret decisions that cannot be seen directly.
5. Record dimension or implementation checks separately from aesthetic judgment.

Use at least two graders for visual cases. One should be able to inspect layout and typography; the other should focus on task compliance and usability. Resolve score differences greater than 15 points with a short adjudication note.

## Rubric (100 points)

### 1. Problem framing — 10

- Identifies medium, format, content types, priorities, recurring elements, and production or interaction constraints.
- Uses actual content or representative stress cases instead of designing only with empty boxes.

### 2. Typography and readability — 15

- Chooses body size, measure, leading, and hierarchy as a related system.
- Demonstrates comfortable reading rhythm at the intended distance or viewport.

### 3. Grid derivation — 20

- Derives columns, gutters, margins, baseline, and horizontal fields from content and typography.
- Uses the fewest useful divisions and gives implementable measurements or relationships.

### 4. Alignment and rhythm — 15

- Text, images, captions, navigation, and repeated components share deliberate anchors.
- Vertical spacing and field heights resolve to a coherent interval without accidental drift.

### 5. Hierarchy and navigation — 15

- Priority and reading order are clear without showing grid lines.
- Variation supports sequence and emphasis while recurring elements remain predictable.

### 6. Images, data, and white space — 10

- Uses a limited, meaningful family of spans and sizes.
- Preserves useful content, caption attachment, and deliberate unoccupied space.

### 7. Adaptation and constraints — 10

- Handles format changes, breakpoints, binding, safe areas, accessibility, production, or viewing distance when relevant.
- Re-derives the system instead of blindly scaling it.

### 8. Verification and explanation — 5

- Tests edge cases and, for visual outputs, inspects both an overlay and a clean view.
- Explains exceptions and distinguishes structural rules from stylistic choices.

## Critical failures

Any critical failure prevents a passing result regardless of score:

- illegible, clipped, overlapping, inaccessible, or impossible-to-produce output;
- a fixed preset imposed without reference to content or medium;
- no measurable grid or relationship between type and spatial system;
- hierarchy dependent on visible construction lines;
- responsive behavior defined only as proportional shrinking;
- ignored user constraints or altered content meaning.

## Passing and comparison

- **Pass:** 80 or above and no critical failure.
- **Strong pass:** 90 or above.
- **Skill lift:** the skill-enabled result should improve the mean total by at least 10 points and should not regress task compliance.
- Report category-level deltas as well as the total; a higher total that hides a typography or accessibility regression is not acceptable.

## Case-specific grading

Each JSONL case lists `must_observe` and `must_avoid`. These are evidence requirements, not exact solutions. Do not reward a particular column count unless the prompt makes it necessary.
