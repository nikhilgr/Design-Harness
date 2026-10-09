# Design rules

Our goal is richness through coherent depth: details, behavior, and discoveries that reinforce a specific idea and reward attention. Richness may emerge in any medium. Complexity, effects, agent count, and iteration count are not measures of success.

## Explore → compare → deepen → build → inspect → learn

1. **Explore.** Establish the intended experience and the interesting uncertainty. Gather varied references and identify the qualities worth learning from. Explore suitable forms and tools; do not assume a medium, aesthetic, or existing skill is the answer.
2. **Compare.** Make meaningfully different alternatives visible in a form the user can judge. Vary the underlying idea, not just surface styling. Recommend a direction with reasons; let the user's response reveal what matters. Scale breadth and effort to the task rather than prescribing a fixed number of options.
3. **Deepen.** Develop what feels compelling. Translate feedback into concrete experiments and record what must survive. Prove one rich moment—a small, sufficiently complete piece of the experience—before expanding when that reduces uncertainty. Revisit the premise if polishing does not make it more compelling.
4. **Build.** Extend the successful relationships into a coherent whole. Choose techniques by their contribution to the experience. Keep parts independently revisable when useful, preserve accepted versions, and make meaningful iterations easy to inspect. Use parallel agents only when authorized and when responsibilities are separable.
5. **Inspect.** Review the intended effect and functional behavior separately. Use the actual medium: playback for timing, interaction for behavior, close inspection for detail. Compare versions under consistent conditions. Exercise relevant accessibility, performance, and failure states. Report limits honestly; automated checks and model praise cannot establish artistic success.
6. **Learn.** Save the artifact, source, meaningful decisions, provenance, and review evidence together. Capture why a direction won and what failed. Add a reusable rule or method only when evidence warrants it; keep project-specific taste local. Do not update personal memory unless requested.

This is an adaptable working rhythm, not a mandatory stage ceremony. Agree on an appropriate effort budget and review checkpoint for substantial exploration. Stop when the intended outcome is achieved, or surface the unresolved uncertainty when the budget is reached.

## Tool selection and source ownership

Choose tools by the decision being made and the fastest useful feedback. Begin with the intended experience and its largest uncertainty; prove a representative moment before expanding. Add a tool when it unlocks a needed capability or improves iteration. A project need not use every tool.

| Tool | Responsibility |
| --- | --- |
| **Paper** | All storyboarding; composition, typography, and layout exploration where useful. |
| **Diffusion Studio** | Film sequencing and finishing: shot timing, titles, transitions, and audio, combining footage, rendered assets, and procedural scenes. |
| **Blender** | Geometry, materials, lighting, cameras, and animation when dedicated 3D tooling serves the intended result. |
| **Working browser prototype** | Interactive behavior, responsive layouts, and real-time graphics; judge behavior in the running implementation. |
| **Codex workspace** | Connect the brief, references, source, scripts, decisions, versions, and review evidence across tools. |

Keep one authoritative editable source per component. Preserve source scenes behind rendered assets and record their relationship in project notes so revisions can be regenerated. Expose meaningful controls for repeated adjustments. Preserve selected versions and compare experiments under consistent conditions.

## Storyboarding and production handoffs

Create and revise storyboards exclusively in **Paper**. For substantial sequences of shots, scenes, or interaction states, storyboard key compositions and progression before full production. Add concise notes on action, approximate timing, transitions, sound, or interaction as needed. Scale detail and alternatives to the brief and uncertainty.

Keep the Paper board link and useful review exports with project notes; exports and shot lists do not replace the editable board. If Paper is unavailable, report the dependency and continue independent research or feasibility tests without creating a substitute storyboard elsewhere.

Carry the selected direction into production and reflect meaningful sequence changes back into Paper. Paper owns the planned sequence; the production timeline owns exact film timing, and the running prototype owns actual behavior. Verify those in their final medium. Feasibility experiments may precede storyboarding, and small revisions need not restart the process.

## Coaching and critique

The user directs intent, feeling, and selection. The model proposes ambitious possibilities, translates reactions into experiments, recommends a direction, and verifies its work. Feedback need not use technical vocabulary. Useful review questions are: what feels alive, what feels generic or wrong, what should stay, and what uncertainty should we test next?

Use these lenses when helpful, without scoring every artifact or requiring every lens:

- **Coherence:** do the parts reinforce the central idea?
- **Specificity:** what makes this unmistakably itself?
- **Causality:** do related elements respond meaningfully?
- **Time:** how does the experience unfold or invite reading?
- **Discovery:** what rewards closer attention without obscuring essential use?
- **Craft:** does the work hold up under scrutiny and actual use?

When expressive range is part of the intent, consider what the subject could become, where it belongs, and how someone encounters it. Differences in purpose, composition, form, and material can reveal possibilities that changes in palette or ornament do not. A specific invented premise can guide this exploration without an external reference; shared forms remain useful when consistency is the intended experience.

For an addition, consider its contribution, connection to the whole, and cost in attention or performance. More detail earns its place through meaning. Keep the user's decision focused on the experience; discuss implementation when it affects feasibility, cost, or quality.

## Context on demand

There is no default design profile and no prescribed set of media. Apply a design file only when the user names its file or key. Use relevant skills as methods, examples as evidence, and scripts as checks. Project notes can hold a brief, decisions, and QA without separate template documents. Load only what the current task needs.

Choose methods from the intended experience or observed problem, not keywords, availability, or a fixed sequence. Ordinary judgment is enough when a skill adds no useful guidance. The user need not name a skill.

- [Frontend vocabulary](skills/frontend-design-vocabulary/SKILL.md): when qualitative interface feedback needs translation into concrete experiments.
- [Grid design](skills/muller-brockmann-grid-design/SKILL.md): when content hierarchy, typographic rhythm, or cross-format structure needs a deliberate ordering system.
- [Illustration](skills/hand-drawn-illustration/SKILL.md): when the chosen direction benefits from code-authored hand-drawn stills.
- [Animation](skills/hand-drawn-canvas-animation/SKILL.md): when the chosen direction benefits from a hand-drawn film, not ordinary UI motion.

For these methods, use the linked workspace copy rather than loading a duplicate global copy. Read only the selected entry point and the references needed now. These are available methods, not a menu of permitted outcomes; explore other tools and media when they better serve the idea.

When comparing models or harness changes, hold the brief, inputs, tools, and effort reasonably consistent; disclose differences. Judge actual artifacts and repeat promising cases before generalizing. Change one major factor at a time to understand what helped.

## Foundations

The [companion article referenced in the Will Newton harness discussion](https://www.agenticdesign.school/articles/build-a-design-harness-before-you-prompt) contributes lean instructions, distinct responsibilities, evidence, and detail loaded on demand. Its fixed design-system layer serves product consistency; we leave that layer inactive until the user selects one.

[Felix Rieseberg's Made by mechanical means](https://felixrieseberg.com/made-by-mechanical-means/) contributes the practical pattern of visible alternatives, selective deepening, modular production, and repeated review. The richness lenses and this workflow are our adaptation, not a framework attributed to either author.
