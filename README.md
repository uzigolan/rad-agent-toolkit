# rad-agent-toolkit

Toolkit for AI agents operating **RAD Data Communications** devices: MCP
servers per product line, Claude skills, a staged-commit safety model, and
live-harvested CLI knowledge — SecFlow and ETX-2 first, the full RAD
portfolio by design.

> **Status: internal RAD pilot.** Private repository. Do not point at
> production equipment.

## What's in the box

| Component | What it is |
|---|---|
| **[`rad-mcp-server/`](rad-mcp-server/)** | The first RAD MCP server + Claude Code plugin: SSH/Netmiko transport, per-family CLI drivers, read tools, interactive `?`-help relay (`cli_help`), staged-commit config writes with automatic backups, MCP resources. **Start at its [README](rad-mcp-server/README.md) and [INSTALL](rad-mcp-server/INSTALL.md).** |
| **Skills** (`rad-mcp-server/skills/`) | Claude skills teaching the RAD context-based CLI: `rad-core` (safety rules, staged-commit workflow) and `rad-cli-operations` (CLI model + `references/` knowledge harvested from live devices). Work in Claude Code, Desktop, and Cowork. |
| **CLI knowledge layer** | Firmware-exact command knowledge captured from real devices: full command trees (`tree`) and complete interactive `?` help harvested per context by [`scripts/harvest_cli.py`](rad-mcp-server/scripts/harvest_cli.py) — stored as grep-friendly references for skills and served to Desktop via MCP resources. |
| **Docs** | [`rad-mcp-server/docs/architecture.md`](rad-mcp-server/docs/architecture.md) — the canonical design: stack, 7-point safety model, 5-layer knowledge strategy, distribution roadmap. [`vendor-mcp-baseline.md`](vendor-mcp-baseline.md) — survey of vendor MCP servers this project is modeled on. |
| **Workspace wiring** (`.claude/`, `.mcp.json`) | Ready-to-use Claude Code configuration for this repo: launches the server, loads the skills and `/rad-health`, `/rad-backup` commands. |

## Quick start

1. Clone, then create `rad-mcp-server/server/.env` with device credentials
   (never committed — see [INSTALL.md](rad-mcp-server/INSTALL.md)).
2. `cd rad-mcp-server/server && python -m venv .venv && .venv/Scripts/pip install -e .`
3. Open the repo in VS Code with the Claude extension (or `claude` CLI) —
   `.mcp.json` starts the server automatically. Desktop and Cowork setup:
   [INSTALL.md](rad-mcp-server/INSTALL.md).
4. Ask Claude: *"Run a health check on lab-sf1p"*.

## Safety model (short version)

- Writes are **staged**: backup → diff preview → explicit human approval →
  commit → verify. No exceptions.
- Reads are whitelisted; `cli_help` types `?` and clears the line — it can
  never execute anything.
- Dangerous commands (`reboot`, `factory-default`, …) are out of scope by
  design. `RAD_MCP_READONLY=true` removes all write tools.
- Credentials live only in gitignored `server/.env`; audit log is append-only
  with secrets redacted.

Full model: [architecture.md](rad-mcp-server/docs/architecture.md).

## Product coverage

| Family | Products | Status |
|---|---|---|
| `secflow` | SF-1p / SecFlow gateways | ✅ verified live (SF-1p, Sw 6.5.0.35) |
| `etx2` | ETX-203AX / 205A / 220A | shared CLI dialect, pending live verification |
| `etx1`, `mp4100` | legacy ETX-1, Megaplex-4100 | planned — separate CLI dialects, own drivers |

## Roadmap

- ETX-2 live verification; harvest its CLI reference.
- Phase-2 harvest: enter parameterized contexts using existing entity indexes
  from the running config.
- `rad://cli-reference/{family}/{context}` keyed-lookup resource for Desktop.
- RADview northbound API backend alongside SSH.
- Manuals knowledge layer (RAG over official RAD documentation).
- Distribution: `.mcpb` Desktop Extension + Claude Code plugin marketplace.

## Repository layout

```
rad-agent-toolkit/
├── README.md                    # you are here
├── .claude/ / .mcp.json         # Claude Code workspace wiring (skills, commands, server launch)
├── rad-mcp-server/              # the MCP server, skills, docs, scripts (see its README)
├── vendor-mcp-baseline.md       # vendor MCP ecosystem survey
├── rad-fusion-architecture.md   # superseded — points to rad-mcp-server/docs/architecture.md
└── fusion-cli.code-workspace    # VS Code workspace file
```
