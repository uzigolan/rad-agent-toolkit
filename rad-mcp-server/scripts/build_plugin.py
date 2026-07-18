"""Assemble the rad-agent-toolkit Claude plugin (dist/plugin/) + upload zip.

One plugin bundles everything a user needs in a single upload/install:
  - both skills (rad-cli-operations, rad-core)
  - all commands (rad-harvest, rad-load-manual, rad-backup, rad-health)
  - the rad-mcp MCP server (.mcp.json)

Assembled from the canonical sources so there is no extra hand-maintained copy
(re-run after changing skills/commands). Follows the documented plugin layout:
`.claude-plugin/plugin.json` is the ONLY thing under .claude-plugin/; skills/,
commands/, .mcp.json sit at the plugin root.

LOCAL build: the .mcp.json uses this machine's absolute venv + inventory paths
(rad_mcp isn't globally installed). Portable distribution would instead ship
`uvx rad-mcp` or a pip entry point — future work; noted in the plugin README.

Run: python scripts/build_plugin.py
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent          # rad-mcp-server/
SKILLS_SRC = REPO / "skills"
COMMANDS_SRC = REPO / "commands"
OUT_ROOT = REPO / "dist" / "plugin"
PLUGIN = OUT_ROOT / "rad-agent-toolkit"

VENV_PY = REPO / "server" / ".venv" / "Scripts" / "python.exe"
INVENTORY = REPO / "inventory.yaml"

MANIFEST = {
    "name": "rad-agent-toolkit",
    "displayName": "RAD Agent Toolkit",
    "version": "1.0.0",
    "description": "Operate RAD Data Communications devices (SecFlow, ETX-1p, "
                   "ETX-2) from Claude: staged-commit config safety, harvested "
                   "CLI reference + device manuals, and the Abayev/Noam CLI "
                   "expert personas. Bundles the rad-mcp server, skills, and "
                   "maintenance commands.",
    "author": {"name": "Uzi Golan", "email": "UZI_G@rad.com"},
    "keywords": ["rad", "secflow", "etx", "network", "mcp", "cli"],
}

# rad_mcp runs from the server venv (it's `pip install -e`'d there); mirror the
# Desktop config exactly. Absolute paths => works on THIS machine.
MCP = {
    "mcpServers": {
        "rad-mcp": {
            "command": str(VENV_PY),
            "args": ["-m", "rad_mcp.server"],
            "env": {"RAD_MCP_INVENTORY": str(INVENTORY)},
        }
    }
}

README = """# RAD Agent Toolkit (Claude plugin)

One-upload bundle: the **rad-mcp** MCP server + both skills
(`rad-cli-operations`, `rad-core`) + maintenance commands
(`rad-harvest`, `rad-load-manual`, `rad-backup`, `rad-health`).

## Install
- **Claude Desktop:** Customize -> Plugins -> Upload local plugin -> this zip.
- **Claude Code:** `claude --plugin-dir <path-to-unzipped-folder>` to test, or
  install via a marketplace.

## What works where
- **Skills + MCP tools** (reads, staged config, backups, health): Claude Code
  AND Desktop.
- **`/rad-backup`, `/rad-health`:** MCP-based -> work anywhere.
- **`/rad-harvest`, `/rad-load-manual`:** run local Python scripts in this repo
  -> Claude Code only (Desktop can't execute them). Harmless if present.

## LOCAL build caveat
`.mcp.json` points at this machine's venv + inventory (absolute paths), because
`rad_mcp` is installed in `server/.venv`, not globally. It will NOT work on a
different machine as-is. For a portable/shareable plugin, publish `rad-mcp` as
a package and switch the command to `uvx rad-mcp` (or a pip entry point).

If you already configured `rad-mcp` manually in `claude_desktop_config.json`,
remove that entry after installing this plugin to avoid a duplicate server.
"""


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the rad-agent-toolkit plugin bundle.")
    ap.add_argument("--knowledge", choices=("bundled", "served"), default="bundled",
                    help="bundled (default): plugin carries the skills' references (~14 MB). "
                         "served: thin plugin — rad-cli-operations/references omitted, served "
                         "by the MCP catalog tools.")
    args = ap.parse_args()
    served = args.knowledge == "served"

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    (PLUGIN / ".claude-plugin").mkdir(parents=True)

    (PLUGIN / ".claude-plugin" / "plugin.json").write_text(
        json.dumps(MANIFEST, indent=2), encoding="utf-8")
    (PLUGIN / ".mcp.json").write_text(json.dumps(MCP, indent=2), encoding="utf-8")
    (PLUGIN / "README.md").write_text(README, encoding="utf-8")

    # skills/ and commands/ copied verbatim from canonical sources
    ignore = shutil.ignore_patterns("references") if served else None
    shutil.copytree(SKILLS_SRC, PLUGIN / "skills", ignore=ignore)
    if served:
        print("served mode: thin plugin (rad-cli-operations/references omitted — served by the MCP catalog)")
    (PLUGIN / "commands").mkdir()
    for md in sorted(COMMANDS_SRC.glob("*.md")):
        shutil.copy2(md, PLUGIN / "commands" / md.name)

    # zip for Desktop upload (forward-slash arc paths, plugin dir as top level)
    zip_path = OUT_ROOT / "rad-agent-toolkit.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(PLUGIN):
            for f in files:
                full = Path(root) / f
                arc = full.relative_to(OUT_ROOT).as_posix()
                z.write(full, arc)

    n_files = sum(1 for _ in PLUGIN.rglob("*") if _.is_file())
    n_skills = sum(1 for _ in (PLUGIN / "skills").glob("*/SKILL.md"))
    n_cmds = sum(1 for _ in (PLUGIN / "commands").glob("*.md"))
    print(f"plugin -> {PLUGIN.relative_to(REPO)}  "
          f"({n_skills} skills, {n_cmds} commands, {n_files} files)")
    print(f"zip    -> {zip_path.relative_to(REPO)}")
    if not VENV_PY.exists():
        print(f"WARNING: venv python not found at {VENV_PY} — fix the path before use.")


if __name__ == "__main__":
    main()
