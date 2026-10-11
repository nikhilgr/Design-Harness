#!/usr/bin/env python3

import re
import sys
import argparse
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "AGENTS.md",
    "DESIGN_RULES.md",
    "examples/README.md",
    "OUTPUT_GUIDANCE.md",
]

parser = argparse.ArgumentParser(description="Check harness structure and local documentation links.")
parser.add_argument("--tracked", action="store_true", help="Check only Git-indexed files; untracked local files cannot satisfy links.")
args = parser.parse_args()
tracked = None
if args.tracked:
    try:
        tracked = set(subprocess.check_output(
            ["git", "ls-files", "-z"], cwd=ROOT, stderr=subprocess.PIPE
        ).decode().split("\0")) - {""}
    except subprocess.CalledProcessError:
        parser.error("--tracked requires a Git checkout. Run it in the publishing checkout after staging changes.")


def available(path):
    if not path.exists():
        return False
    if tracked is None:
        return True
    try:
        relative = path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return False
    return relative in tracked or (path.is_dir() and any(
        item.startswith(relative.rstrip("/") + "/") for item in tracked
    ))


def prose(content, strip_inline=True):
    """Ignore fenced examples and inline code when looking for real links."""
    lines = []
    fence = None
    for line in content.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    text = "\n".join(lines)
    return re.sub(r"(`+).*?\1", "", text) if strip_inline else text


def anchors(content):
    result = set()
    counts = {}
    for title in re.findall(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", prose(content, strip_inline=False), re.MULTILINE):
        title = re.sub(r"<[^>]+>", "", title).lower()
        slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        n = counts.get(slug, 0)
        result.add(slug + (f"-{n}" if n else ""))
        counts[slug] = n + 1
    result.update(re.findall(r'''\b(?:id|name)=["']([^"']+)["']''', content))
    return result

# Skills are optional methods, not mandatory prerequisites for every medium.
SKILLS = [str(path.relative_to(ROOT)) for path in (ROOT / "skills").glob("*/SKILL.md") if available(path)]

errors = []
warnings = []

for relative in REQUIRED:
    if not (ROOT / relative).is_file() or not available(ROOT / relative):
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

excluded_parts = {".git", "node_modules", "__pycache__", ".archive", ".pnpm-store"}
if tracked is not None:
    documents = sorted(p for p in tracked if p.endswith(".md"))
else:
    paths = list(ROOT.glob("*.md"))
    for folder in ("skills", "examples", "Design systems"):
        paths.extend((ROOT / folder).rglob("*.md"))
    documents = sorted(str(p.relative_to(ROOT)) for p in paths
                       if not excluded_parts.intersection(p.relative_to(ROOT).parts))

link_pattern = re.compile(r'\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\s*\)')
for relative in documents:
    markdown_path = ROOT / relative
    if not markdown_path.is_file():
        errors.append(f"{relative}: missing documentation file")
        continue
    content = prose(markdown_path.read_text(encoding="utf-8"))
    targets = link_pattern.findall(content)
    targets += re.findall(r'^ {0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)', content, re.MULTILINE)
    for raw_target in targets:
        target = raw_target.strip().removeprefix("<").removesuffix(">")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        resolved = (markdown_path.parent / unquote(parsed.path)).resolve() if parsed.path else markdown_path
        if not available(resolved):
            errors.append(f"{relative}: broken local link to {target}")
        elif parsed.fragment and resolved.suffix.lower() == ".md" and resolved.is_file():
            if unquote(parsed.fragment) not in anchors(resolved.read_text(encoding="utf-8")):
                errors.append(f"{relative}: missing heading anchor in {target}")

# Profiles intentionally have no global section schema or mandatory filename.

print(f"Design harness audit: {len(errors)} error(s), {len(warnings)} warning(s)")
for warning in warnings:
    print(f"WARN  {warning}")
for error in errors:
    print(f"ERROR {error}", file=sys.stderr)

if errors:
    raise SystemExit(1)

print(f"PASS  Required files, skill frontmatter, and local links/Markdown anchors in {len(documents)} documents are valid.")
print("NOTE  Checks cover inline links and reference definitions; external URLs are not fetched.")
print("NOTE  Structural validation does not establish artistic or functional quality.")
