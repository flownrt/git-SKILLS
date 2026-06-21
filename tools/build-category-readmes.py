#!/usr/bin/env python3
"""Regenerate the skill index inside each category README.

For every top-level category folder (a directory whose README.md contains the
marker block below), this rewrites the lines between

    <!-- skills:start -->
    <!-- skills:end -->

with a table of the skills in that folder: each skill's name and a short
description, read from its SKILL.md YAML frontmatter. Anything outside the
markers (title, blurb, ...) is left untouched, so edit those by hand. Run this
after adding, removing, or renaming a skill:

    python tools/build-category-readmes.py

No third-party dependencies: the frontmatter is read with a small tolerant
parser, so it copes with descriptions that contain colons, quotes, or dashes.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- skills:start -->", "<!-- skills:end -->"
SKIP = {"tools"}  # top-level folders that are not skill categories
KEY = re.compile(r"^([A-Za-z0-9_-]+):(.*)$")
BLOCK_SCALAR = {">", ">-", ">+", "|", "|-", "|+"}


def parse_frontmatter(skill_md: Path) -> dict:
    """Read the YAML-ish frontmatter into a flat {key: value} dict, tolerantly.

    Handles plain values, quoted values, and folded/literal block scalars; values
    spread over several indented lines are joined into one. Avoids a real YAML
    parser so a stray colon inside a description can't blow it up.
    """
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    fields: dict[str, str] = {}
    key, buf = None, []

    def flush() -> None:
        if key is None:
            return
        value = " ".join(s.strip() for s in buf if s.strip())
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        fields[key] = value.strip()

    for line in m.group(1).splitlines():
        head = KEY.match(line)
        if head and not line[:1].isspace():
            flush()
            key, rest = head.group(1), head.group(2).strip()
            buf = [] if rest in BLOCK_SCALAR else [rest]
        else:
            buf.append(line.strip())
    flush()
    return fields


def short_desc(desc: str) -> str:
    """First clause of a description: cut at the first sentence end or dash."""
    desc = " ".join(str(desc).split())
    cut = len(desc)
    for i, ch in enumerate(desc):
        if ch in ".?!–—":  # sentence end, en dash, or em dash
            cut = i
            break
    return desc[:cut].strip(" .,;:!?–—")


def skills_in(category: Path) -> list[tuple[str, str, str]]:
    rows = []
    for d in sorted(p for p in category.iterdir() if p.is_dir()):
        skill_md = d / "SKILL.md"
        if skill_md.exists():
            fm = parse_frontmatter(skill_md)
            rows.append((fm.get("name", d.name), d.name, short_desc(fm.get("description", ""))))
    return rows


def render_table(rows: list[tuple[str, str, str]]) -> str:
    if not rows:
        return ""
    lines = ["| Skill | What it does |", "| --- | --- |"]
    lines += [f"| [`{name}`](./{folder}) | {desc} |" for name, folder, desc in rows]
    return "\n".join(lines)


def update_category(category: Path) -> bool:
    readme = category / "README.md"
    if not readme.exists():
        return False
    text = readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        return False
    table = render_table(skills_in(category))
    block = f"{START}\n{table}\n{END}" if table else f"{START}\n{END}"
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
    if new != text:
        readme.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = [
        cat.name
        for cat in sorted(ROOT.iterdir())
        if cat.is_dir() and not cat.name.startswith(".") and cat.name not in SKIP
        if update_category(cat)
    ]
    print("Updated:", ", ".join(changed) if changed else "nothing (already up to date)")


if __name__ == "__main__":
    main()
