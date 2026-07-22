#!/usr/bin/env python3
"""Validate every standalone skill in this repository."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_PATTERN = re.compile(r"\A---\s*\n(.*?)\n---(?:\n|\Z)", re.DOTALL)
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def metadata_value(frontmatter: str, key: str) -> str | None:
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        match = re.match(rf"^{re.escape(key)}:\s*(.*)$", line)
        if not match:
            continue
        value = match.group(1).strip().strip("\"'")
        if value not in {"", ">", ">-", "|", "|-"}:
            return value
        continuation: list[str] = []
        for following in lines[index + 1 :]:
            if following and not following[0].isspace():
                break
            if following.strip():
                continuation.append(following.strip())
        return " ".join(continuation) or None
    return None


def validate_skill(skill_root: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_root / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_root.name}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return [f"{skill_root.name}: invalid or missing YAML frontmatter"]

    frontmatter = match.group(1)
    name = metadata_value(frontmatter, "name")
    description = metadata_value(frontmatter, "description")
    if name != skill_root.name:
        errors.append(f"{skill_root.name}: frontmatter name must match directory name")
    if not name or not NAME_PATTERN.fullmatch(name) or len(name) > 64:
        errors.append(f"{skill_root.name}: invalid skill name")
    if not description:
        errors.append(f"{skill_root.name}: missing description")

    agent_metadata = skill_root / "agents/openai.yaml"
    if agent_metadata.is_file():
        agent_text = agent_metadata.read_text(encoding="utf-8")
        for field in ("display_name", "short_description", "default_prompt"):
            if not re.search(rf"(?m)^\s*{field}:\s*\S", agent_text):
                errors.append(f"{skill_root.name}: agents/openai.yaml missing {field}")

    for markdown in skill_root.rglob("*.md"):
        markdown_text = markdown.read_text(encoding="utf-8")
        for raw_link in LINK_PATTERN.findall(markdown_text):
            link = raw_link.strip("<>").split("#", 1)[0]
            if not link or re.match(r"^(?:https?://|mailto:)", link):
                continue
            if not (markdown.parent / link).resolve().exists():
                relative = markdown.relative_to(ROOT)
                errors.append(f"{relative}: broken local link {raw_link}")

    for script in skill_root.rglob("*.py"):
        try:
            ast.parse(
                script.read_text(encoding="utf-8"),
                filename=str(script),
                feature_version=(3, 10),
            )
        except (SyntaxError, UnicodeDecodeError) as error:
            errors.append(f"{script.relative_to(ROOT)}: {error}")
    return errors


def main() -> int:
    if not SKILLS_ROOT.is_dir():
        print("error: missing skills directory", file=sys.stderr)
        return 1
    skill_roots = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    if not skill_roots:
        print("error: no skills found", file=sys.stderr)
        return 1

    errors = [error for root in skill_roots for error in validate_skill(root)]
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"validated {len(skill_roots)} skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
