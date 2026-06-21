#!/usr/bin/env python3
"""Rebuild the distributable .skill bundles in dist/ from the skill sources.

Every skill lives in a category folder as <category>-SKILLS/<skill>/ with a
SKILL.md at its root. This zips each such folder into dist/<skill>.skill, with
the skill folder as the archive's top-level directory (study/SKILL.md,
study/references/..., ...), so the bundle installs cleanly. .DS_Store and
dotfiles are skipped, so the archive stays clean.

Run with no arguments to rebuild every skill, or pass names to rebuild a subset:

    python tools/build-dist.py            # all skills
    python tools/build-dist.py study      # just one

dist/*.skill is gitignored: these are build artifacts, not tracked source. This
script has no third-party dependencies.
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"


def skill_dirs():
    """Yield every <category>-SKILLS/<skill>/ folder that has a SKILL.md."""
    for category in sorted(ROOT.glob("*-SKILLS")):
        if not category.is_dir():
            continue
        for skill in sorted(category.iterdir()):
            if skill.is_dir() and (skill / "SKILL.md").is_file():
                yield skill


def included_files(skill_dir: Path):
    """Files to bundle: everything under the skill folder except dot-entries."""
    for path in sorted(skill_dir.rglob("*")):
        if path.is_dir():
            continue
        rel = path.relative_to(skill_dir)
        if any(part.startswith(".") for part in rel.parts):
            continue  # skips .DS_Store, ._* AppleDouble files, any dotfile/dotdir
        yield path


def build(skill_dir: Path) -> tuple[str, int]:
    name = skill_dir.name
    DIST.mkdir(exist_ok=True)
    dest = DIST / f"{name}.skill"
    tmp = DIST / f".{name}.skill.tmp"
    count = 0
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in included_files(skill_dir):
            arcname = (Path(name) / f.relative_to(skill_dir)).as_posix()
            z.write(f, arcname)
            count += 1
    try:
        tmp.replace(dest)                    # atomic rename on a normal filesystem
    except OSError:
        dest.write_bytes(tmp.read_bytes())   # fallback: overwrite in place (read-only/hard-linked target)
        try:
            tmp.unlink()
        except OSError:
            pass
    return name, count


def main(argv: list[str]) -> int:
    wanted = set(argv)
    built = [build(d) for d in skill_dirs() if not wanted or d.name in wanted]
    if not built:
        target = f" matching {sorted(wanted)}" if wanted else ""
        print(f"build-dist: no skills found{target}", file=sys.stderr)
        return 1
    for name, count in built:
        print(f"dist/{name}.skill  ({count} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
