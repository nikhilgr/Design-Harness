#!/usr/bin/env python3

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "AGENTS.md",
    "DESIGN_RULES.md",
    "examples/README.md",
    "outputs/README.md",
]

# Skills are optional methods, not mandatory prerequisites for every medium.
SKILLS = [str(path.relative_to(ROOT)) for path in (ROOT / "skills").glob("*/SKILL.md")]

errors = []
warnings = []

for relative in REQUIRED:
    if not (ROOT / relative).exists():
        errors.append(f"Missing required file: {relative}")

for relative in SKILLS:
    skill_path = ROOT / relative
    if not skill_path.exists():
        continue
    content = skill_path.read_text(encoding="utf-8")
    folder_name = skill_path.parent.name
    frontmatter = re.match(r"^---\n([\s\S]*?)\n---\n", content)
    if not frontmatter:
        errors.append(f"{relative}: missing YAML frontmatter")
        continue
    name_match = re.search(r"^name:\s*(.+)$", frontmatter.group(1), re.MULTILINE)
    description_match = re.search(
        r"^description:\s*(.+)$", frontmatter.group(1), re.MULTILINE
    )
    name = name_match.group(1).strip().strip('\"\'') if name_match else ""
    description = description_match.group(1).strip() if description_match else ""
    if description in {">", ">-", ">+", "|", "|-", "|+"}:
        block = frontmatter.group(1)[description_match.end():]
        description = " ".join(
            match.group(1).strip()
            for match in re.finditer(r"^([ \t]+\S.*)$", block.split("\n\n", 1)[0], re.MULTILINE)
        )
    if name != folder_name:
        errors.append(f"{relative}: name must match folder ({folder_name})")
    if len(description) < 40:
        errors.append(
            f"{relative}: description must explain capability and activation context"
        )
    if not re.fullmatch(r"[a-z0-9-]{1,64}", folder_name):
        errors.append(
            f"{relative}: folder must be lowercase, hyphenated, and at most 64 characters"
        )

link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for relative in [item for item in REQUIRED if item.endswith(".md")]:
    markdown_path = ROOT / relative
    if not markdown_path.exists():
        continue
    content = markdown_path.read_text(encoding="utf-8")
    for raw_target in link_pattern.findall(content):
        target = raw_target.strip().removeprefix("<").removesuffix(">").split("#", 1)[0]
        if not target or target.startswith(("http:", "https:", "mailto:")):
            continue
        resolved = (markdown_path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{relative}: broken local link to {target}")

# Profiles intentionally have no global section schema or mandatory filename.

print(f"Design harness audit: {len(errors)} error(s), {len(warnings)} warning(s)")
for warning in warnings:
    print(f"WARN  {warning}")
for error in errors:
    print(f"ERROR {error}", file=sys.stderr)

if errors:
    raise SystemExit(1)

print("PASS  Process files, installed skill frontmatter, and framework links are valid.")
print("NOTE  Structural validation does not establish artistic or functional quality.")
