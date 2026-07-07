# rad-agent-toolkit

Toolkit for AI agents operating **RAD Data Communications** devices: MCP
servers per product line, Claude skills, a staged-commit safety model, and
live-harvested CLI knowledge — SecFlow and ETX-1p verified live, ETX-2 next,
the full RAD portfolio by design.

> **Status: internal RAD pilot.** Private repository. Do not point at
> production equipment.

## What this repo demonstrates

Beyond operating RAD gear, this repo is a **working showcase of the ways AI
capability can be "plugged into" AI applications** — the same device-operations
use case implemented across every integration surface, so each technology can
be evaluated in a real context rather than a toy demo. It is built to plug into
**any AI application, not just one**:

| AI integration technology | What it demonstrates | Plugs into |
|---|---|---|
| **MCP server** (tools + `rad://` resources) | The open Model Context Protocol as the portable core — device verbs + knowledge exposed to any MCP client | Claude Desktop, Claude Code, ChatGPT, Cursor, Zed, Gemini CLI, … |
| **Skills** (`SKILL.md` + personas) | Packaging domain expertise, safety rules, and expert personas (Abayev/Noam) as loadable context | Claude Code / Desktop |
| **Plugin bundle** | One uploadable unit combining MCP + skills + commands | Claude Desktop "Upload local plugin" |
| **Remote MCP** (HTTP + bearer auth, read-only) | One shared server many clients reach by URL — no per-user install; auth + read-only enforced in code | any MCP client on the network |
| **Portable bundle** | The knowledge + wiring guide re-packaged for non-Claude clients (Custom GPT, Cursor rules, RAG corpus) | ChatGPT/OpenAI, others |
| **Knowledge layers** | Live-harvested CLI reference + ingested device manuals as lexical retrieval (RAG-adjacent), served as files and resources | client-agnostic |
| **Automation hooks** | Duration/token metrics per skill run via lifecycle hooks + statusline | Claude Code |

The through-line: **write the capability once (the MCP server + knowledge),
then surface it through whichever integration a given AI app supports.** The
server and knowledge are portable; only the thin wrappers (skill, plugin,
connector config) differ per app.

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
| `etx1p` | ETX-1p demarcation units | ✅ verified live (Sw 6.5.0.43 and 6.4.0.165) — modern context-based CLI + manual layer; **not** the legacy `etx1` |
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
