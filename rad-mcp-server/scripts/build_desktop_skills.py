"""Package the skills as Claude Desktop upload zips (dist/claude-desktop-skills/).

For non-Claude clients (ChatGPT/OpenAI, Cursor, ...) see build_portable_bundle.py.

Desktop's skill upload rejects zip entries with backslash paths, which is what
PowerShell Compress-Archive produces on Windows — hence this script.
Run from anywhere: python scripts/build_desktop_skills.py
"""
import os
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "dist" / "claude-desktop-skills"


def _write_zip(out: Path, skill_dir: Path) -> None:
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(skill_dir):
            for f in files:
                full = Path(root) / f
                arc = full.relative_to(REPO / "skills").as_posix()
                z.write(full, arc)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for skill_dir in sorted((REPO / "skills").iterdir()):
        if not (skill_dir / "SKILL.md").exists():
            continue
        out = OUT_DIR / f"{skill_dir.name}.zip"
        try:
            _write_zip(out, skill_dir)
        except PermissionError:
            # Claude Desktop holds the loaded skill's zip open — write a
            # side file so the build still produces a fresh artifact.
            out = OUT_DIR / f"{skill_dir.name}-new.zip"
            _write_zip(out, skill_dir)
            print(f"  (primary zip locked — wrote {out.name}; "
                  f"close Desktop or replace the loaded skill to refresh the main name)")
        with zipfile.ZipFile(out) as z:
            print(f"{out.relative_to(REPO)} -> {len(z.namelist())} entries")


if __name__ == "__main__":
    main()
