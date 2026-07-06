"""Package the skills as Claude Desktop upload zips (dist/desktop-skills/).

Desktop's skill upload rejects zip entries with backslash paths, which is what
PowerShell Compress-Archive produces on Windows — hence this script.
Run from anywhere: python scripts/build_desktop_skills.py
"""
import os
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "dist" / "desktop-skills"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for skill_dir in sorted((REPO / "skills").iterdir()):
        if not (skill_dir / "SKILL.md").exists():
            continue
        out = OUT_DIR / f"{skill_dir.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for root, _, files in os.walk(skill_dir):
                for f in files:
                    full = Path(root) / f
                    arc = full.relative_to(REPO / "skills").as_posix()
                    z.write(full, arc)
        with zipfile.ZipFile(out) as z:
            print(f"{out.relative_to(REPO)} -> {z.namelist()}")


if __name__ == "__main__":
    main()
