# Design Harness

A reusable creative workspace for exploring, comparing, building, and inspecting design across media. It has no default aesthetic, medium, or design profile.

## Start here

- [AGENTS.md](AGENTS.md) is the short entry point for agents working in the workspace.
- [DESIGN_RULES.md](DESIGN_RULES.md) defines the creative workflow, tool responsibilities, source ownership, review, and contextual skill selection.
- [Examples](examples/README.md) describes how to keep useful design evidence.
- [Outputs](OUTPUT_GUIDANCE.md) describes how to organize deliverables and review evidence.

Use this repository as a workspace or copy its harness files into a project. Read the agent instructions first, then load only the methods needed for the current task. Storyboarding requires Paper; production tools depend on the chosen medium.

## Included methods

- [Design interview](skills/design-interview/SKILL.md)

- [Frontend design vocabulary](skills/frontend-design-vocabulary/SKILL.md)
- [Muller-Brockmann grid design](skills/muller-brockmann-grid-design/SKILL.md), with references and behavioral evaluation cases
- [Hand-drawn illustration](skills/hand-drawn-illustration/SKILL.md)
- [Hand-drawn Canvas animation](skills/hand-drawn-canvas-animation/SKILL.md), with reusable assets, examples, and rendering helpers

Skills are optional methods. Their own examples and assets are included because they support reuse. The 22 supplied [product reference images](<examples/Product Visual References/README.md>) and optional [Databricks design profile](<Design systems/Databricks-Design/README.md>) are included. Product video references, the entire outputs folder, generated project artwork, benchmarks, and archives are excluded. Reference-image provenance and interpretation limits are documented in the image index; the repository license does not establish rights to third-party reference images.

The Canvas animation snapshot records its upstream source and file hashes in [source-manifest.json](skills/hand-drawn-canvas-animation/source-manifest.json). Individual method files retain their source references.

## Validate the harness

Run with Python 3:

```sh
python3 scripts/verify_design_harness.py
```

The check validates required files, skill metadata, and framework links. Artistic quality and functional behavior require inspection in the appropriate medium.
