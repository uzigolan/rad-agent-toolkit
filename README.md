# rad-agent-toolkit

Toolkit for AI agents operating **RAD Data Communications** devices.

**The heart of it is the knowledge — the skill.** Firmware-exact CLI
expertise **live-harvested from real units** (every context's `?` help,
captured and verified), device **user manuals ingested** into greppable
per-chapter knowledge with CLI cross-links, a growing verified command
map, expert personas, and hard safety rules — packaged in the cross-vendor
Agent Skills standard, so the same expertise loads in Claude, Copilot, and
Codex unmodified. The **MCP server is the execution arm** — essential, but
second fiddle: it gives the knowledge hands (staged-commit writes,
whitelisted reads, live `?`-help relay). SecFlow, ETX-1p, ETX-2,
Megaplex-4100, and MP-1 verified live; the full RAD portfolio by design.

> **Status: internal RAD pilot.** Private repository. Do not point at
> production equipment.

**Works in** — all six verified live (install:
[INSTALL.md](rad-mcp-server/INSTALL.md) · versions/models tested:
[CONCEPTS.md §8](rad-mcp-server/docs/CONCEPTS.md)):

- Claude Code — VS Code extension
- Claude Code — CLI
- Claude Desktop — chat + Cowork
- GitHub Copilot — VS Code (agent mode)
- GitHub Copilot — CLI (Windows / Linux)
- OpenAI Codex — Codex IDE extension (VS Code / JetBrains)
- OpenAI Codex — Codex in the ChatGPT desktop app

## Device support

| Family | Products | Version | Driver | Status |
|---|---|---|---|---|
| `secflow` | SF-1p and SecFlow gateways | 6.5.0 | `drivers/secflow.py` | ✅ verified live (SF-1p) |
| `etx1p` | ETX-1p demarcation units | 6.5.0 | `drivers/etx1p.py` | ✅ verified live (Device3 + a 6.4 unit) — modern context CLI, harvested references + manual; NOT legacy `etx1` |
| `etx2` | ETX-203AX / 205A / 220A / ETX-2I | 6.8.5 | `drivers/etx2.py` | ✅ verified live (ETX-2I) — `show resources` unsupported, slot/port naming; CLI reference + manual harvested |
| `mp4100` | Megaplex-4100 multiservice access nodes | 4.91 | `drivers/mp4100.py` | ✅ verified live (marks-mp4) — same shared dialect + candidate-DB `commit` model; CLI reference + 1,202-page manual harvested |
| `mp1` | MP-1 | 2.20 | `drivers/mp1.py` | ✅ verified live (mp-one) — shared dialect + candidate-DB `commit` model; standard SSH; CLI reference + manual harvested |
| `minid` | MiNID miniature NID (sleeve device) | 2.6 | `drivers/minid.py` | ✅ verified live (minid-1, prompt `MiNID#`) — shared context CLI, direct-write save; fragile/unique SSH profile; CLI reference + manual harvested |
| `etx2v` | ETX-2V (uCPE-OS chassis platform) | 5.0.0 | `drivers/etx2v.py` | ✅ verified live (etx2v-1, prompt `uCPE-OS#`) — shared context CLI, standard SSH; top-level `virtualization` (VNF) context; 719-node tree / 527 captures harvested + hardware/BIOS manual |
| `etx1` | legacy ETX-1 | - | - | planned — separate (menu) CLI dialect, own driver |

## What this repo demonstrates

Less theory, more concrete examples. One prompt from each section in
[examples.md](rad-mcp-server/docs/examples.md), and what this app does with it:

1. Device management
- Prompt:
  "rad agent, add my device: name lab-etx2, host 172.17.163.205, family etx2, group lab, user su, password 1234"
- What this app does:
  validates required fields, writes inventory facts, keeps credentials in env,
  then lets the same device be used by all supported clients.

2. Device operations
- Prompt:
  "abayev, show the active alarms on sf-163-187"
- What this app does:
  runs a guarded read workflow (confirmation + read-only tool call), collects
  live alarm output, and returns an operator-ready summary.

3. Network engineering
- Prompt:
  "abayev, I have three ETX-2 units in a ring running ERP — give me the configuration for all three"
- What this app does:
  uses harvested CLI references + manuals to produce per-device config blocks
  and verification steps, with staged commit flow when execution is requested.

4. Advanced
- Prompt:
  "rad agent, compare the ETX-2 and the ETX-2V on QoS capabilities"
- What this app does:
  builds a family-by-family comparison grounded in each family's own harvested
  references/manuals, avoiding unsupported cross-family assumptions.

5. Onboarding a new device type
- Prompt:
  "rad agent, harvest the CLI of the new device I just added"
- What this app does:
  runs CLI harvesting into reusable references (command tree + syntax corpus),
  so future answers become firmware-exact instead of generic.

In short: this repo turns those prompts into repeatable workflows by combining
skills (knowledge), MCP tools (execution), and harvested/manual evidence
that can be reused across clients.

## What's in the box

| Component | What it is |
|---|---|
| **[`rad-mcp-server/`](rad-mcp-server/)** | The first RAD MCP server + Claude Code plugin: SSH/Netmiko transport, per-family CLI drivers, read tools, interactive `?`-help relay (`cli_help`), staged-commit config writes with automatic backups, MCP resources. **Start at its [README](rad-mcp-server/README.md) and [INSTALL](rad-mcp-server/INSTALL.md).** |
| **Skills** (`rad-mcp-server/skills/`) | Agent Skills teaching the RAD context-based CLI: `rad-core` (safety rules, staged-commit workflow), `rad-cli-operations` (CLI model + `references/` knowledge harvested from live devices), `rad-device-mng` (self-onboard your own equipment). Details in [Skills, options, and an example](#skills-options-and-an-example). |
| **CLI knowledge layer** | Firmware-exact command knowledge captured from real devices: full command trees (`tree`) and complete interactive `?` help harvested per context by [`scripts/harvest_cli.py`](rad-mcp-server/scripts/harvest_cli.py) — stored as grep-friendly references for skills and served to Desktop via MCP resources. |
| **Docs** | [`CONCEPTS.md`](rad-mcp-server/docs/CONCEPTS.md) — **every principle in one file** (start here for concepts). [`architecture.md`](rad-mcp-server/docs/architecture.md) — the canonical design: stack, 7-point safety model, 5-layer knowledge strategy, distribution roadmap. [`vendor-mcp-baseline.md`](vendor-mcp-baseline.md) — survey of vendor MCP servers this project is modeled on. |
| **Workspace wiring** (`.claude/`, `.mcp.json`) | Ready-to-use Claude Code configuration for this repo: launches the server, loads the skills and `/rad-health`, `/rad-backup` commands. |

## Skills, options, and an example

The toolkit ships three artifact kinds — **tools** do, **skills** know,
**commands** orchestrate ([definitions](rad-mcp-server/INSTALL.md#the-three-artifact-kinds-used-throughout-these-docs)).
The three skills in [`rad-mcp-server/skills/`](rad-mcp-server/skills/) load
automatically when the conversation matches their trigger:

| Skill | What it does | Loads when you say things like |
|---|---|---|
| [`rad-core`](rad-mcp-server/skills/rad-core/SKILL.md) | The safety contract: look-before-touch, the staged-commit flow (backup → stage → preview → explicit approval → commit → verify), inventory conventions | any RAD/ETX device work |
| [`rad-cli-operations`](rad-mcp-server/skills/rad-cli-operations/SKILL.md) | The CLI expert: context-based CLI model + firmware-exact command knowledge for `etx2`, `etx1p`, `secflow`, `mp4100`, `mp1`; expert personas; response/verification modes | *"how do I configure X on the ETX"*, *"what's the command for…"*, *"abayev, …"* / *"noam, …"* / *"rad agent, …"* — any CLI/syntax question |
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
| [`/rad-health`](rad-mcp-server/commands/rad-health.md) `<device \| group>` | Health sweep on one device or a whole group; summarized findings |
| [`/rad-backup`](rad-mcp-server/commands/rad-backup.md) `<device \| group>` | Back up running configs to the local archive |
| [`/rad-harvest`](rad-mcp-server/commands/rad-harvest.md) `<device> [subtree]` | Re-harvest the device's CLI `?`-help into the skill reference — after a firmware upgrade, or when the reference is missing a context (optionally one subtree, e.g. `configure crypto`) |
| [`/rad-load-manual`](rad-mcp-server/commands/rad-load-manual.md) `<pdf> <family>` | Ingest a user-manual PDF into the skill's manual layer (per-chapter markdown + CLI-topic cross-links) |

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

## Documentation map

How the docs link together (each node is reachable from its parent):

```
README.md (this file)
├── rad-mcp-server/README.md ........... server overview + five operation categories
│   ├── docs/CONCEPTS.md .......... ALL principles in one file — concepts entry point
│   ├── INSTALL.md ..................... Part 1 principles · Part 2 targets + verified matrix
│   │   ├── scripts/install/mcp_server/ ─── run a shared http server (start/restart scripts)
│   │   ├── scripts/install/skills_and_mcp/ ─── per-client install scripts + consolidated guide
│   │   └── docs/connecting-remote-mcp.md . host / join a shared server (http)
│   │   ├── docs/connecting-local-mcp.md .. same-machine wiring (stdio + http)
│   ├── docs/architecture.md ........... canonical design (safety, knowledge layers, roadmap)
│   │   ├── docs/performance.md ........ ingestion timing
│   │   └── docs/manual-quality.md ..... per-family manual-ingestion quality
│   ├── skills/*/SKILL.md .............. the three agent skills
│   ├── commands/*.md .................. the four slash commands
│   └── tests/README.md ................ eval harness → RESULTS.md · eval-report.md
├── TODO.md ............................ living task list
├── vendor-mcp-baseline.md ............. vendor MCP survey this project is modeled on
└── rad-fusion-architecture.md ......... original design note (superseded, points inward)
```

## Quick start

1. Clone, then create `rad-mcp-server/server/.env` with device credentials
   (never committed — see [INSTALL.md](rad-mcp-server/INSTALL.md)).
2. Run the installer for your client from
   [rad-mcp-server/scripts/install/skills_and_mcp/](rad-mcp-server/scripts/install/skills_and_mcp/README.md)
   — it auto-creates `server/.venv` and wires **both** the MCP server entry
   (stdio — the client starts the server itself) and the skills:
   - VS Code + Copilot extension: `.\install-copilot-vscode.ps1`
   - Claude Desktop: `.\install-claude-desktop.ps1`
   - other clients (Claude Code, Copilot CLI, Codex): see the
     [folder README](rad-mcp-server/scripts/install/skills_and_mcp/README.md)
3. Restart the client as the script instructs (reload the VS Code window /
   tray-quit and relaunch Desktop) — the stdio entry launches the server
   automatically.
4. Ask: *"rad agent, run a health check on <device-name>"*.

## Safety model (short version)

- Writes are **staged**: backup → diff preview → explicit human approval →
  commit → verify. No exceptions.
- Reads are whitelisted; `cli_help` types `?` and clears the line — it can
  never execute anything.
- Dangerous commands (`reboot`, `factory-default`, …) are out of scope by
  design. `RAD_MCP_READONLY=true` removes all write tools.
- Over http/https, capability follows the bearer token: read-only
  (`RAD_MCP_TOKENS`) or read-write (`RAD_MCP_WRITE_TOKENS`) — a read-only
  token is refused on any write attempt.
- Credentials live only in gitignored `server/.env`; audit log is append-only
  with secrets redacted.

Full model: [architecture.md](rad-mcp-server/docs/architecture.md).

## Roadmap

- ~~ETX-2 live verification; harvest its CLI reference.~~ ✅ done (ETX-2I).
- ~~Phase-2 harvest: enter parameterized contexts using existing entity
  indexes from the running config.~~ ✅ done, and extended further: numeric
  contexts with no existing instance now get a manual-vetted temp-object
  create/rollback too (`scripts/harvest_cli.py`).
- `rad://cli-reference/{family}/{context}` keyed-lookup resource for Desktop.
- RADview northbound API backend alongside SSH.
- Manuals knowledge layer: lexical retrieval ✅ done (all verified families —
  secflow, etx1p, etx2, mp4100, mp1); semantic RAG over the corpus — not started.
- Distribution: `.mcpb` Desktop Extension + Claude Code plugin marketplace.
- ~~New integration targets: GitHub Copilot (VS Code + CLI) and OpenAI
  Codex (CLI/IDE/desktop).~~ ✅ [install scripts + guide](rad-mcp-server/scripts/install/skills_and_mcp/README.md)
  written; both vendors adopted Agent Skills, so the skills load unmodified.
  **All six targets verified live** (2026-07-10/11, four model families) —
  record in [CONCEPTS.md §8](rad-mcp-server/docs/CONCEPTS.md).

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
