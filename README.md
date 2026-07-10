# rad-agent-toolkit

Toolkit for AI agents operating **RAD Data Communications** devices: MCP
servers per product line, Claude skills, a staged-commit safety model, and
live-harvested CLI knowledge — SecFlow, ETX-1p, and ETX-2 verified live,
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
| **MCP server** (tools + `rad://` resources) | The open Model Context Protocol as the portable core — device verbs + knowledge exposed to any MCP client | Claude Desktop, Claude Code, GitHub Copilot (VS Code + CLI), OpenAI Codex (CLI/IDE), Cursor, Zed, Gemini CLI, … |
| **Skills** (`SKILL.md` + personas) | Packaging domain expertise, safety rules, and expert personas (Abayev/Noam) as loadable context — now the cross-vendor **Agent Skills** open standard | Claude Code / Desktop, GitHub Copilot (VS Code + CLI), OpenAI Codex |
| **Plugin bundle** | One uploadable unit combining MCP + skills + commands | Claude Desktop "Upload local plugin" |
| **Remote MCP** (HTTPS + bearer auth, read-only) | One shared server many clients reach by URL — auth, read-only, and native TLS enforced in code; one of [three deployment modes](rad-mcp-server/INSTALL.md) | any MCP client on the network |
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
| **Skills** (`rad-mcp-server/skills/`) | Agent Skills teaching the RAD context-based CLI: `rad-core` (safety rules, staged-commit workflow), `rad-cli-operations` (CLI model + `references/` knowledge harvested from live devices), `rad-device-mng` (self-onboard your own equipment). Details in [Skills, options, and an example](#skills-options-and-an-example). |
| **CLI knowledge layer** | Firmware-exact command knowledge captured from real devices: full command trees (`tree`) and complete interactive `?` help harvested per context by [`scripts/harvest_cli.py`](rad-mcp-server/scripts/harvest_cli.py) — stored as grep-friendly references for skills and served to Desktop via MCP resources. |
| **Docs** | [`rad-mcp-server/docs/architecture.md`](rad-mcp-server/docs/architecture.md) — the canonical design: stack, 7-point safety model, 5-layer knowledge strategy, distribution roadmap. [`vendor-mcp-baseline.md`](vendor-mcp-baseline.md) — survey of vendor MCP servers this project is modeled on. |
| **Workspace wiring** (`.claude/`, `.mcp.json`) | Ready-to-use Claude Code configuration for this repo: launches the server, loads the skills and `/rad-health`, `/rad-backup` commands. |

## Skills, options, and an example

The toolkit ships three artifact kinds — **tools** do, **skills** know,
**commands** orchestrate ([definitions](rad-mcp-server/INSTALL.md#the-three-artifact-kinds-used-throughout-these-docs)).
The three skills in [`rad-mcp-server/skills/`](rad-mcp-server/skills/) load
automatically when the conversation matches their trigger:

| Skill | What it does | Loads when you say things like |
|---|---|---|
| [`rad-core`](rad-mcp-server/skills/rad-core/SKILL.md) | The safety contract: look-before-touch, the staged-commit flow (backup → stage → preview → explicit approval → commit → verify), inventory conventions | any RAD/ETX device work |
| [`rad-cli-operations`](rad-mcp-server/skills/rad-cli-operations/SKILL.md) | The CLI expert: context-based CLI model + firmware-exact command knowledge for `etx2`, `etx1p`, `secflow`; expert personas; response/verification modes | *"how do I configure X on the ETX"*, *"what's the command for…"*, *"abayev, …"* / *"noam, …"* / *"rad agent, …"* — any CLI/syntax question |
| [`rad-device-mng`](rad-mcp-server/skills/rad-device-mng/SKILL.md) | Inventory CRUD so you can point the toolkit at your own equipment (`list/add/update/remove_device`), including the credentials-go-in-`.env`-then-restart workflow | *"add my device"*, *"register a new unit"*, *"remove that device"* |

### What you can ask `rad-cli-operations` — five categories of operations

| Category | What it covers | Example | Touches the device? |
|---|---|---|---|
| **CLI syntax lookup** | "What's the command / what arguments does it take" — answered from the firmware-exact harvested reference | *"what's the command for a static route on the SecFlow?"* | No — reference lookup |
| **Device inquiry** | Live state: alarms, health, config, ports, routing tables, identity | *"show the active alarms on sf-163-187"* | Read — after your confirmation |
| **Device changes** | Config edits through the staged flow: backup → diff preview → **your explicit approval** → commit → verify | *"change router interface 1 to 10.0.100.5/24"* | Write — staged, never direct |
| **Manual & concepts** | The *why / how many / what does it mean* layer, answered from the ingested user manual | *"what does the LOS alarm mean?"*, *"how many MQTT servers can it hold?"* | No — manual lookup |
| **Knowledge upkeep** | Refreshing the skill's own knowledge from the device or a manual PDF | `/rad-harvest` after a firmware upgrade, `/rad-load-manual` | Read-only harvest |

All five are available through plain language or by addressing the personas
(*"abayev, …"*, *"noam, …"*, *"rad agent, …"*).

### Slash commands (packaged recipes)

Four explicit commands ([`rad-mcp-server/commands/`](rad-mcp-server/commands/)),
invoked by name — Claude Code only; elsewhere ask in plain language.

| Command | What it does |
|---|---|
| `/rad-health <device \| group>` | Health sweep on one device or a whole group; summarized findings |
| `/rad-backup <device \| group>` | Back up running configs to the local archive |
| `/rad-harvest <device> [subtree]` | Re-harvest the device's CLI `?`-help into the skill reference — after a firmware upgrade, or when the reference is missing a context (optionally one subtree, e.g. `configure crypto`) |
| `/rad-load-manual <pdf> <family>` | Ingest a user-manual PDF into the skill's manual layer (per-chapter markdown + CLI-topic cross-links) |

### Options (spoken toggles — no config files)

`rad-cli-operations` has three session-scoped options, all switched by just
saying so mid-conversation:

| Option | Default | Alternative | Switch by saying |
|---|---|---|---|
| Expert persona | off — plain Claude | answer *as* Abayev or Noam, veteran RAD CLI experts, signed replies | address them: *"abayev, …"* / *"noam, …"* |
| Response verbosity | `concise` — paste-ready command block first, only safety-critical notes around it | `verbose` — full walkthrough with explanation, tables, verify section | *"use verbose mode"* / *"back to concise"* |
| Reference trust | `trust-reference` — answer syntax from the harvested reference, no device round-trip | `always-verify-live` — re-confirm every answer with a live `cli_help` call | *"always verify live"* / *"back to trusting the reference"* |

A switched mode holds until you switch back or the session ends.

### Example

```text
you:    abayev, change router interface 1 on Device3 to 10.0.100.5/24

claude: [loads rad-cli-operations, greps the secflow reference, stages the
        change — nothing touches the device yet]
        Stage rs-4f21 ready. Preview:
          configure router 1 interface 1
          address 10.0.100.5/24
        Pre-commit backup will be taken automatically. Commit?   — Abayev

you:    yes, commit

claude: Committed rs-4f21. Verified: interface 1 `show status` now reports
        10.0.100.5/24. Backup at backups/Device3/…   — Abayev
```

The same conversation works on every surface in the
[install matrix](rad-mcp-server/INSTALL.md) — only the skill install differs
per client.

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
| `etx2` | ETX-203AX / 205A / 220A / ETX-2I | ✅ verified live (ETX-2I, Sw 6.8.5(1.116)) — no `show resources`; slot/port naming (`Ethernet 0/2`); CLI reference + manual harvested |
| `etx1`, `mp4100` | legacy ETX-1, Megaplex-4100 | planned — separate CLI dialects, own drivers |

## Roadmap

- ~~ETX-2 live verification; harvest its CLI reference.~~ ✅ done (ETX-2I).
- ~~Phase-2 harvest: enter parameterized contexts using existing entity
  indexes from the running config.~~ ✅ done, and extended further: numeric
  contexts with no existing instance now get a manual-vetted temp-object
  create/rollback too (`scripts/harvest_cli.py`).
- `rad://cli-reference/{family}/{context}` keyed-lookup resource for Desktop.
- RADview northbound API backend alongside SSH.
- Manuals knowledge layer: lexical retrieval ✅ done (all 3 families);
  semantic RAG over the corpus — not started.
- Distribution: `.mcpb` Desktop Extension + Claude Code plugin marketplace.
- ~~New integration targets: GitHub Copilot (VS Code + CLI) and OpenAI
  Codex (CLI/IDE/desktop).~~ ✅ [guides](rad-mcp-server/docs/install/)
  written; both vendors adopted Agent Skills, so the skills load unmodified.
  Copilot VS Code verified live 2026-07-10.

Full task list: [TODO.md](TODO.md).

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
