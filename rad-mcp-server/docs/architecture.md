# rad-mcp architecture

**What this is:** the official-vendor MCP server + Claude Code plugin for
operating RAD Data Communications devices in natural language — health checks,
config backup, syntax discovery, and guarded provisioning. Modeled on the
precedent set by `Juniper/junos-mcp-server` and Cisco's RADkit MCP server;
as of July 2026 no RAD MCP server exists anywhere, so this is RAD's entry
into the MCP ecosystem.

## The stack

```
 Claude surfaces          Claude Code (VS Code / CLI)  ·  Claude Desktop chat  ·  Cowork
        │
 knowledge layer          skills (rad-core, rad-cli-operations)
        │                 + references/ (harvested command trees)
        │                 + slash commands (/rad-health, /rad-backup — Code only)
        │
 MCP server               rad_mcp.server  (Python, FastMCP, stdio)
        │                 tools: list_devices · test_connectivity · run_show ·
        │                 run_show_in_context · cli_help · get_config ·
        │                 health_check · backup_config · stage_config ·
        │                 commit_config · save_startup
        │                 resources: rad://inventory · rad://backups[/name] ·
        │                 rad://command-tree/{family}
        │
 backends (transport)     ssh (Netmiko, device_type rad_etx)   [now]
        │                 radview northbound API                [planned]
        │
 drivers (CLI dialect)    radcli.py — shared context-CLI dialect
        │                   ├── secflow  (SF-1p — verified live)
        │                   └── etx2     (ETX-203AX/205A/220A — pending live check)
        │                 etx1, mp4100/Megaplex — different CLIs, own drivers [planned]
        │
 devices                  inventory.yaml (name/host/family/groups; creds in server/.env)
```

**Why backend × driver?** Transport and dialect vary independently across the
RAD portfolio. SSH now and RADview later must both drive a SecFlow; one SSH
session must be able to drive both a SecFlow and (different dialect) a
Megaplex. Tools stay product-agnostic verbs; the device's `family` field
picks the driver, config picks the backend.

## Safety model (the core design constraint)

Network gear is production infrastructure; every write is treated as
dangerous until a human approves it.

1. **Read whitelist** — `run_show`/`run_show_in_context` accept only
   driver-whitelisted read prefixes; context navigation is validated against
   known contexts and a strict token charset.
2. **Staged commits** — writes go `stage_config` (returns preview, touches
   nothing) → human reviews the diff → `commit_config(stage_id, confirm=true)`.
   The confirm flag is required and the skill forbids setting it without
   explicit user approval in-conversation.
3. **Automatic pre-commit backup** — every commit first snapshots the running
   config to `server/backups/`; the commit output includes the restore path.
4. **`cli_help` never executes** — it relays the CLI's interactive `?` help by
   typing `<prefix>?` and then clearing the pending line (Ctrl-U); newlines
   and control characters in the prefix are refused.
5. **Read-only mode** — `RAD_MCP_READONLY=true` removes every write tool at
   registration time (they don't exist in the session at all).
6. **Append-only audit** — every tool call lands in `server/logs/audit.jsonl`
   with secrets redacted.
7. **Defense in depth** — the same rules live in the skills (Claude refuses
   before trying) and in the server (the tool refuses if asked anyway).
   Dangerous CLI areas (`admin` reboot/factory-default, `file` delete) are
   documented as no-go zones and are not whitelisted.

## Knowledge layers (how Claude "knows" the CLI)

The RAD CLI is huge (2,000+ nodes on SF-1p alone) and context-based — `show`
commands only exist inside contexts. No static prompt could hold it, so
knowledge is layered from cheap/static to live/exact:

| Layer | What | When Claude uses it |
|---|---|---|
| 1. Skill | `rad-cli-operations/SKILL.md`: CLI model, verified command map, safety rules | always loaded for RAD work |
| 2. References | `references/command-tree-<family>.md`: full harvested `tree` captures | to locate which context holds a feature |
| 3. Live `?` help | `cli_help` tool: firmware-exact commands, argument types, constraints (`[2..2 chars]`), `[no]` removability | before staging any config; whenever syntax is uncertain |
| 4. MCP resources | `rad://inventory`, `rad://backups`, `rad://command-tree/{family}` | surfaces without filesystem access (Desktop) |
| 5. Manuals RAG | `search_docs` over official RAD manuals | planned — conceptual questions the CLI can't answer |

The layers reinforce each other: skills teach the *method* (find context →
`cli_help` level → `cli_help` leaf → stage), references give the *map*, and
`cli_help` gives ground truth that can never drift from the firmware. New
verified findings are folded back into layers 1–2 after each session.

## The maintenance loop

```
operate live → verify a new command/behavior → update SKILL.md + references
      ↑                                                        │
      └── next session (any user, any surface) inherits it ←──┘
```

Skill copies: `skills/` in this repo is the **source of truth**; copies go to
workspace `.claude/skills/` (Claude Code), `~/.claude/skills/` (user-level),
and `dist/desktop-skills/*.zip` (Desktop uploads, built by
`scripts/build_desktop_skills.py`). Sync all four when the source changes.

## Distribution path

- **Now (internal pilot):** absolute venv paths in `.mcp.json` / Desktop
  config on the pilot machine.
- **Next:** publish the `rad-mcp` Python package internally → configs become
  `uvx rad-mcp` (self-contained installs); package an `.mcpb` Desktop
  Extension for one-click NOC installs; plugin marketplace moves from local
  directory to a git URL.
- **Later:** RADview backend for fleet-scale operations; remote MCP endpoint
  for Cowork/claude.ai; manuals-RAG (`search_docs`) as the vendor-exclusive
  differentiator.

## Roadmap snapshot (July 2026)

- [x] SecFlow driver verified live (SF-1p, Sw 6.5.0.35) — reads, staged
      writes, backups, health, `cli_help`
- [x] Claude Code plugin (skills + commands) and Desktop deployment
- [ ] Git version control + internal repo
- [ ] ETX-2 live verification (driver written, needs lab time)
- [ ] Packaging: `uvx rad-mcp`, `.mcpb`, marketplace via git
- [ ] ETX-1 and MP-4100/Megaplex dialect drivers
- [ ] RADview northbound backend
- [ ] Manuals RAG
