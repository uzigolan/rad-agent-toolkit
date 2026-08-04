"""Build a client-neutral bundle for NON-Claude targets (dist/portable-agent/).

The rad-mcp *server* is already portable — MCP is an open protocol, so any
MCP-capable client (OpenAI Agents / ChatGPT, Cursor, Windsurf, Zed, Gemini CLI,
VS Code agent mode, ...) can use its tools and rad:// resources unchanged. What
is NOT portable is the Claude-specific packaging (SKILL.md loader, /commands,
plugin manifest). This bundle carries the reusable pieces:

  portable-agent/
    knowledge/        <- combined RAD skill brief + references/ + per-skill
                         SKILL.md files, usable as a Custom-GPT knowledge upload,
                         Cursor rules, a system prompt, or any RAG corpus
    README.md         <- how to wire the MCP server into a non-Claude client,
                         and how to adapt SKILL.md into agent instructions

Run: python scripts/build_portable_bundle.py
"""
from __future__ import annotations

import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"
ROUTER_SKILL = SKILLS / "rad-cli-operations"
OUT = REPO / "dist" / "portable-agent"

README = """# RAD skills — portable bundle (non-Claude clients)

The value splits into two layers with very different portability:

| Layer | Portable? | How to use elsewhere |
|---|---|---|
| **rad-mcp server** (tools + `rad://` resources) | **Yes — open MCP protocol** | Point any MCP-capable client at the same launch command (below). No code changes. |
| **Skills** (`skills/*/SKILL.md`, plugin) | Claude-format only | Adapt `knowledge/SKILL.md` into the client's instruction/system-prompt slot, or use the per-skill files under `knowledge/skills/`. |
| **Knowledge** (`references/`, manuals) | Yes — plain markdown/jsonl | Upload as Custom-GPT knowledge, Cursor rules, or a RAG corpus. |

## 1. Wire the MCP server into a non-Claude client (stdio)

The server speaks stdio MCP. The launch command is identical everywhere:

```json
{
  "mcpServers": {
    "rad-mcp": {
      "command": "<repo>/rad-mcp-server/server/.venv/Scripts/python.exe",
      "args": ["-m", "rad_mcp.server"],
      "env": { "RAD_MCP_INVENTORY": "<repo>/rad-mcp-server/inventory.yaml" }
    }
  }
}
```

- **OpenAI Agents SDK / ChatGPT desktop**, **Cursor**, **Windsurf**, **Zed**,
  **Gemini CLI**, **VS Code agent mode**: each has an MCP-servers config that
  takes this same shape (key names vary slightly — check the client's docs).
- **Remote clients** (cloud ChatGPT, hosted agents) can't spawn a local
  process — run the server over HTTP/SSE instead of stdio (FastMCP supports a
  streamable-http transport) and give the client the URL + auth. NOTE: exposing
  device-config *write* tools to a cloud client raises the auth/security bar —
  gate it.

> Verify per client: MCP feature coverage (write-tool support, resource
> support, remote auth) differs and changes fast. Reads (`cli_help`,
> `run_show`, `get_config`) are universally safe; the staged-write flow
> (`stage_config`/`commit_config`) needs a client that surfaces tool output.

## 2. Adapt the skill into agent instructions

`knowledge/SKILL.md` is a combined RAD skill brief assembled from the router
and domain skills. To reuse it as a Custom GPT instruction / OpenAI agent
system prompt / Cursor rule, keep the routing, retrieval, safety, and device
behavior rules; drop Claude-specific mechanics and map local-reference steps to
either attached knowledge or MCP resource/tool calls. If you prefer finer
control, each original skill file is also copied under `knowledge/skills/`.

## 3. Knowledge files

`knowledge/references/` holds, per family: the full CLI `?`-help
(`cli-reference-<family>.md` + `cli-help-<family>.jsonl`), the command tree,
and — where ingested — the user manual (`manual-<family>/`). These are the
same files the rad:// resources serve; ship them directly to clients without
resource support.
"""


def _combined_skill_text() -> str:
  parts = []
  for skill_dir in sorted(SKILLS.iterdir()):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
      continue
    parts.append(f"<!-- {skill_dir.name} -->\n")
    parts.append(skill_md.read_text(encoding="utf-8").strip())
    parts.append("\n")
  return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "knowledge" / "skills").mkdir(parents=True)
    # combined instruction brief + the original per-skill SKILL.md files
    (OUT / "knowledge" / "SKILL.md").write_text(_combined_skill_text(), encoding="utf-8")
    for skill_dir in sorted(SKILLS.iterdir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        target = OUT / "knowledge" / "skills" / skill_dir.name
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(skill_md, target / "SKILL.md")
    shutil.copytree(ROUTER_SKILL / "references", OUT / "knowledge" / "references")
    (OUT / "README.md").write_text(README, encoding="utf-8")
    files = sum(1 for _ in OUT.rglob("*") if _.is_file())
    kb = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file()) / 1024
    print(f"portable-agent bundle -> {OUT.relative_to(REPO)}  ({files} files, {kb:.0f} KB)")


if __name__ == "__main__":
    main()
