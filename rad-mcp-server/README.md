# rad-mcp-server

MCP server + Claude Code plugin for operating RAD Data Communications devices
through their CLI in natural language — the **full RAD portfolio** by design:
SecFlow (SF-1p) and ETX-1p verified live, ETX-2 next (shared dialect), and
planned legacy ETX-1 and MP-4100/Megaplex.

The first RAD entry in the MCP ecosystem — naming follows the vendor convention
set by `Juniper/junos-mcp-server` and `CiscoDevNet/radkit-mcp-server-community`.

> **Note on the name:** `rad-mcp-server/` is the **full RAD agent toolkit** —
> the MCP server (`server/`) *plus* the skills, commands, and the uploadable
> plugin — not only the MCP server. (The GitHub repo is `rad-agent-toolkit`.)
> The directory name is kept for path stability across configs and the venv.

| Family | Products | Driver | Status |
|---|---|---|---|
| `secflow` | SF-1p and SecFlow gateways | `drivers/secflow.py` | ✅ verified live (SF-1p Sw 6.5.0.35) |
| `etx1p` | ETX-1p demarcation units | `drivers/etx1p.py` | ✅ verified live (Device3 Sw 6.5.0.43 + a 6.4.0.165 unit) — modern context CLI, harvested references + manual; NOT legacy `etx1` |
| `etx2` | ETX-203AX / 205A / 220A | `drivers/etx2.py` | shared dialect, pending live ETX-2 verification |
| `etx1` | legacy ETX-1 line | planned | different CLI — own driver base |
| `mp4100` | Megaplex-4100 | planned | different CLI — own driver base |

> **Status: internal RAD pilot.** Do not point at production equipment.

## Documentation

- **[INSTALL.md](INSTALL.md)** — setup for every Claude surface: Claude Code
  (VS Code extension + CLI), Claude Desktop chat, Cowork. Start here.
- **[docs/architecture.md](docs/architecture.md)** — the full design: stack,
  safety model, knowledge layers, distribution roadmap.

## What Claude can do with it

Ask in plain language — no CLI knowledge needed:

- *"Run a health check on lab-sf1p"* — device info + active alarms, interpreted
- *"Back up the lab device and diff it against yesterday's backup"*
- *"What arguments does `location` take under configure system?"* — live
  firmware-exact syntax via the device's own `?` help
- *"Change the device location to 'TLV lab rack 3'"* — staged: backup → diff
  preview → **your explicit approval** → commit → verify
- *"Reboot the device"* — **refused**: dangerous commands are out of scope by
  design

## MCP surface

**Tools** — product-agnostic verbs; the device's `family` picks the CLI dialect:

| Tool | Purpose |
|---|---|
| `list_devices` | Inventory, filterable by group/family |
| `test_connectivity` | SSH reachability + auth check |
| `health_check` | Driver-defined health sweep (identity, alarms) |
| `run_show` / `run_show_in_context` | Whitelisted reads (RAD CLIs scope `show` to contexts) |
| `cli_help` | Relay the CLI's interactive `?` help — commands, argument types, constraints. Never executes |
| `get_config` / `backup_config` | Full config export / snapshot to local archive |
| `stage_config` → `commit_config` | Staged writes: preview, explicit confirm, auto pre-commit backup |
| `save_startup` | Persist running config (confirm required) |

**Resources:** `rad://inventory`, `rad://backups`, `rad://backups/{file}`,
`rad://command-tree/{family}`.

**Skills** (loaded by Claude on demand): `rad-core` — safety rules and the
staged-commit workflow; `rad-cli-operations` — the context-CLI model, verified
command map, and `references/` command trees harvested from live devices.

**Slash commands** (Claude Code only): `/rad-health`, `/rad-backup`.

## Safety model

- Writes follow **backup → diff preview → explicit confirm → commit → verify**; no shortcuts.
- `run_show*` accept only whitelisted read prefixes; contexts are validated.
- `cli_help` types `?` and clears the line — nothing is ever executed.
- `RAD_MCP_READONLY=true` removes every write tool at registration time.
- Append-only audit log at `server/logs/audit.jsonl`, secrets redacted.
- Credentials live only in gitignored `server/.env` — never in inventory or code.

## Layout

```
rad-mcp-server/
├── INSTALL.md                 # per-surface setup (start here)
├── docs/architecture.md       # design: stack, safety, knowledge layers
├── .claude-plugin/plugin.json # Claude Code plugin manifest (rad-mcp)
├── .mcp.json                  # MCP launch config (Claude Code)
├── inventory.yaml             # devices by name/family/group — no credentials
├── server/
│   ├── pyproject.toml
│   └── rad_mcp/
│       ├── server.py          # FastMCP entrypoint: tools + resources (stdio)
│       ├── smoke.py           # CLI smoke test against one device
│       ├── inventory.py / audit.py
│       ├── backends/          # transport: ssh (Netmiko) now, radview later
│       └── drivers/           # radcli.py shared dialect; secflow/etx2 on top
├── skills/
│   ├── rad-core/SKILL.md
│   └── rad-cli-operations/
│       ├── SKILL.md
│       └── references/command-tree-secflow.md   # harvested live tree
├── commands/                  # /rad-health, /rad-backup
├── scripts/build_desktop_skills.py              # Claude Desktop skill zips
├── scripts/build_portable_bundle.py             # bundle for non-Claude MCP clients
└── dist/
    ├── claude-desktop-skills/  # built zips (upload via Desktop → Customize)
    └── portable-agent/         # knowledge + MCP-wiring guide for other clients
```
