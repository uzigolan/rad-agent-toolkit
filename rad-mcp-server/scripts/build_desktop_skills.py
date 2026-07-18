"""Package the skills as Claude Desktop upload zips (dist/claude-desktop-skills/).

For non-Claude clients (ChatGPT/OpenAI, Cursor, ...) see build_portable_bundle.py.

Desktop's skill upload rejects zip entries with backslash paths, which is what
PowerShell Compress-Archive produces on Windows — hence this script.
Run from anywhere: python scripts/build_desktop_skills.py [--knowledge bundled|served]

  bundled (default) — zips carry the skills' references/ (~14 MB); knowledge
                      answers work with no MCP connection.
  served            — thin zips (SKILL.md only); rad-cli-operations/references/
                      is omitted and served by the MCP catalog tools.
"""
import argparse
import os
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "dist" / "claude-desktop-skills"


def _stamp_served(text: str) -> str:
    if "<!--rad-mode:" in text:
        return text
    import re
    return re.sub(r"(?m)^(> \*\*Skill version:\*\*.*)$",
                  r"\1\n<!--rad-mode:served-->", text, count=1)


def _write_zip(out: Path, skill_dir: Path, served: bool) -> None:
    skip = (skill_dir / "references") if served else None
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(skill_dir):
            if skip and (Path(root) == skip or skip in Path(root).parents):
                continue
            for f in files:
                full = Path(root) / f
                arc = full.relative_to(REPO / "skills").as_posix()
                # served: stamp the mode into rad-cli-operations/SKILL.md so the
                # loaded skill's self-check knows it (missing stamp = bundled).
                if served and full.name == "SKILL.md" and full.parent.name == "rad-cli-operations":
                    z.writestr(arc, _stamp_served(full.read_text(encoding="utf-8")))
                else:
                    z.write(full, arc)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--knowledge", choices=("bundled", "served"), default="bundled")
    args = ap.parse_args()
    served = args.knowledge == "served"
    if served:
        print("served mode: thin zips (rad-cli-operations/references omitted — served by the MCP catalog)")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for skill_dir in sorted((REPO / "skills").iterdir()):
        if not (skill_dir / "SKILL.md").exists():
            continue
        out = OUT_DIR / f"{skill_dir.name}.zip"
        try:
            _write_zip(out, skill_dir, served)
        except PermissionError:
            # Claude Desktop holds the loaded skill's zip open — write a
            # side file so the build still produces a fresh artifact.
            out = OUT_DIR / f"{skill_dir.name}-new.zip"
            _write_zip(out, skill_dir, served)
            print(f"  (primary zip locked — wrote {out.name}; "
                  f"close Desktop or replace the loaded skill to refresh the main name)")
        with zipfile.ZipFile(out) as z:
            print(f"{out.relative_to(REPO)} -> {len(z.namelist())} entries")


if __name__ == "__main__":
    main()
