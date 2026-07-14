# rad-mcp-server

Agent expertise + MCP server for operating RAD Data Communications devices
through their CLI in natural language — the **full RAD portfolio** by design:
SecFlow (SF-1p), ETX-1p, ETX-2 (ETX-2I), Megaplex-4100, and MP-1 verified live,
with legacy ETX-1 planned.

The center of gravity is the **skill layer** — live-harvested CLI knowledge,
ingested user manuals, and safety rules ([docs/CONCEPTS.md](docs/CONCEPTS.md)
§1). The MCP server is the execution arm that puts that knowledge to work on
real devices.

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
| `etx2` | ETX-203AX / 205A / 220A / ETX-2I | `drivers/etx2.py` | ✅ verified live (ETX-2I Sw 6.8.5(1.116)) — `show resources` unsupported, slot/port naming; CLI reference + manual harvested |
| `etx1` | legacy ETX-1 line | planned | different CLI — own driver base |
| `mp4100` | Megaplex-4100 multiservice access nodes | `drivers/mp4100.py` | ✅ verified live (marks-mp4, Mn 4.91) — same shared dialect + candidate-DB `commit` model; CLI reference + 1,202-page manual harvested |
| `mp1` | MP-1 | `drivers/mp1.py` | ✅ verified live (mp-one, SW 2.20(0.61)) — shared dialect + candidate-DB `commit` model; standard SSH; CLI reference + manual harvested |

> **Status: internal RAD pilot.** Do not point at production equipment.

> **Prerequisites:** Python **3.11+** (3.10 minimum) and SSH reachability to
> your devices. On RHEL-family distros (Rocky/RHEL/Alma) the default `python3`
> is often 3.6 — too old; install a newer one (`sudo dnf install -y python3.11`)
> and build the venv with `python3.11`. Full steps in [INSTALL.md](INSTALL.md#common-setup-once-per-machine).

## Documentation

- **[docs/CONCEPTS.md](docs/CONCEPTS.md)** — every principle in
  one file: artifact kinds, deployment modes, safety model, credentials,
  knowledge layers, cross-client truths. The concepts entry point.
- **[INSTALL.md](INSTALL.md)** — setup hub for six agent targets (Claude
  Code, Claude Desktop, GitHub Copilot, OpenAI Codex) and the three
  deployment modes: local stdio (default, full write flow), a shared
  HTTPS server you host, or connecting to a colleague's — over http what
  a client may do follows its bearer token: read-only (`RAD_MCP_TOKENS`)
  or read-write (`RAD_MCP_WRITE_TOKENS`).
  Per-target specifics in
  [scripts/install/skills_and_mcp/](scripts/install/skills_and_mcp/README.md). Start here.
- **[docs/architecture.md](docs/architecture.md)** — the full design: stack,
  safety model, knowledge layers, distribution roadmap.
- **[docs/VERSIONS.md](docs/VERSIONS.md)** — component versions (server, skills,
  drivers), where each version lives, and the bump policy. Live view: the
  `list_versions` tool.

## What the agent can do with it

Ask in plain language — no CLI knowledge needed. Five categories of
operations:

1. **CLI syntax lookup** (no device contact) — command paths and argument
   constraints from the firmware-exact harvested reference:
   *"What arguments does `location` take under configure system?"*
2. **Device inquiry** (read, runs after your confirmation) — live state:
   *"Run a health check on lab-sf1p"* — device info + active alarms,
   interpreted; *"show the routing table"*, *"back up the lab device and
   diff it against yesterday's backup"*
3. **Device changes** (write, staged — never direct) —
   *"Change the device location to 'TLV lab rack 3'"*: backup → diff
   preview → **your explicit approval** → commit → verify
4. **Manual & concept questions** (no device contact) — meaning, limits,
   procedures from the ingested user manual: *"what does the LOS alarm
   mean?"*, *"how many keys can the ETX-1p hold?"*
5. **Knowledge upkeep** — `/rad-harvest` re-captures the CLI reference
   after a firmware change; `/rad-load-manual` ingests a manual PDF.

And the standing refusal: *"Reboot the device"* — **refused**; dangerous
commands (`admin` context, factory-default, file deletes) are out of scope
by design.

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
`rad-cli-operations` also exposes two **configurable behavior modes** (see
its SKILL.md, *"Response & verification modes"*): response verbosity
(`concise` default / `verbose`) and reference trust (`trust-reference`
default / `always-verify-live`). Both default to the faster behavior; say
e.g. *"abayev, use verbose mode"* or *"abayev, always verify live"* to revert
for the rest of a session, and the equivalent phrase to switch back.

`/rad-harvest` (`scripts/harvest_cli.py`) now auto-creates and rolls back
numeric-indexed parameterized contexts too (`mep`, `lag`, `pw`, `bridge`,
`ppp`, ...), not just string-named ones — each addition is checked against
the **user manual** (layer 4 below) for a "safe to create" confirmation
first, and every refusal is captured with the device's own error text so a
harvest gap always comes with a reason (missing argument, license gate, or
genuinely no live instance), not a guess. Full method + a real case study:
`docs/architecture.md` and `tests/eval-report.md`.

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
