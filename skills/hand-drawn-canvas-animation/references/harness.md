# Design harness integration

This is a local snapshot of the installed alesha-pro skill. Original files are tracked by hash in `../source-manifest.json`; the local entrypoint additionally links this guide. Review upstream changes before replacing this snapshot. The global installation is unchanged.

For still illustrations, use the sibling `hand-drawn-illustration` skill. Do not turn a still request into a film. For animation, retain the upstream production workflow and use the project packaging in the workspace `outputs/README.md`.

Place named projects in `outputs/animations/<ProjectName>/`. Keep film source and runtime modules in `source/`, imported media and fonts in `assets/`, final MP4 and contact sheet in `exports/`, review material in `review/`, and evidence in `QA.md`. Adjust relative imports when copying modules; keep package metadata and lockfile with source. Keep dependency caches and temporary frame staging outside deliverables.

Human Review can annotate an HTML storyboard with stable shot labels and time ranges. Comments on a canvas cannot select individual drawn strokes; carry revisions into the authored drawing data. Normal-speed playback and consecutive-frame inspection remain necessary to assess motion. Requesting a film does not automatically request an interactive review session.

Confirm available Node, Chrome, and ffmpeg paths before rendering. Use the project's package manager and retain its lockfile. Prefer bundled runtimes when system commands are unavailable. Do not assume an old browser path still exists.

Record actual checks separately: still appearance, consecutive-frame continuity, normal-speed playback, encoded decode, duration, dimensions, frame count, and archive integrity if packaged. Report unavailable checks without calling them passed.
