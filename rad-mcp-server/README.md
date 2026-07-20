# rad-mcp-server

Agent expertise + MCP server for operating RAD Data Communications devices
through their CLI in natural language — the **full RAD portfolio** by design:
SecFlow (SF-1p), ETX-1p, ETX-2 (ETX-2I), Megaplex-4100, MP-1, MiNID and ETX-2V
(uCPE-OS) verified live.

The center of gravity is the **skill layer** — live-harvested CLI knowledge,
ingested user manuals and product datasheets, and safety rules ([docs/CONCEPTS.md](docs/CONCEPTS.md)
§1). The MCP server is the execution arm that puts that knowledge to work on
real devices.

> **How it reaches devices — two independent paths:**
> - **CLI** (reads, staged config, backups, health) runs over **SSH _or_
>   telnet**, chosen per device by the inventory `transport` field — SSH by
>   default; telnet for units where SSH isn't available (it's cleartext, so
>   prefer SSH when both work). Same CLI, same safety rules over either.
> - **SNMP** (`snmp_probe`/`snmp_get`/`snmp_walk` + the offline MIB catalog) is
>   a **separate, read-only** path over UDP (GET/GETNEXT only, never SET) —
>   independent of the CLI transport.

The first RAD entry in the MCP ecosystem — naming follows the vendor convention
set by `Juniper/junos-mcp-server` and `CiscoDevNet/radkit-mcp-server-community`.

> **Note on the name:** `rad-mcp-server/` is the **full RAD agent toolkit** —
> the MCP server (`server/`) *plus* the skills, commands, and the uploadable
> plugin — not only the MCP server. (The GitHub repo is `rad-agent-toolkit`.)
> The directory name is kept for path stability across configs and the venv.

| Family | Products | Version | Driver | Status |
|---|---|---|---|---|
| `secflow` | SF-1p and SecFlow gateways | 6.5.0 | `drivers/secflow.py` | ✅ verified live (SF-1p) |
| `etx1p` | ETX-1p demarcation units | 6.5.0 | `drivers/etx1p.py` | ✅ verified live (Device3 + a 6.4 unit) — modern context CLI, harvested references + manual; NOT legacy `etx1` |
| `etx2` | ETX-203AX / 205A / 220A / ETX-2I | 6.8.5 | `drivers/etx2.py` | ✅ verified live (ETX-2I) — `show resources` unsupported, slot/port naming; CLI reference + manual harvested |
| `mp4100` | Megaplex-4100 multiservice access nodes | 4.91 | `drivers/mp4100.py` | ✅ verified live (marks-mp4) — same shared dialect + candidate-DB `commit` model; CLI reference + 1,202-page manual harvested |
| `mp1` | MP-1 | 2.20 | `drivers/mp1.py` | ✅ verified live (mp-one) — shared dialect + candidate-DB `commit` model; standard SSH; CLI reference + manual harvested |
| `minid` | MiNID miniature NID (sleeve device) | 2.6 | `drivers/minid.py` | ✅ verified live (minid-1, prompt `MiNID#`) — shared context CLI, direct-write save; **fragile/unique SSH** → patient per-family connect profile; `tree` paginates with a bare `more...` pager; harvested branch-by-branch (fragile link can't sustain a full-tree session) + manual |
| `etx2v` | ETX-2V (uCPE-OS chassis platform) | 5.0.0 | `drivers/etx2v.py` | ✅ verified live (etx2v-1, prompt `uCPE-OS#`) — shared context CLI, standard SSH; distinctive top-level `virtualization` (VNF) context; 719-node tree / 527 captures harvested + hardware/BIOS manual |

> **Lab use only.** Do not point at production equipment.

> **Prerequisites:** Python **3.11+** (3.10 minimum) and SSH (or telnet)
> reachability to your devices. On RHEL-family distros (Rocky/RHEL/Alma) the default `python3`
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
- **[docs/examples.md](docs/examples.md)** ([HTML](docs/examples.html)) — 30 ready-to-paste prompts across
  nine usage categories, knowledge-first: user manual, datasheets, device
  management, CLI, SNMP, network engineering, advanced, onboarding, and a
  closing fusion set that spans every layer in one prompt — each addressed
  to "rad agent" / "abayev" / "noam".
- **[docs/knowledge-modes.md](docs/knowledge-modes.md)** — bundled ("embeded")
  vs served skills explained in plain English on one page: what differs, what's
  identical (all SNMP/MIB is server-side), and which to pick.
- **[docs/architecture.md](docs/architecture.md)** — the full design: stack,
  safety model, knowledge layers, distribution roadmap.
- **[docs/workflows.md](docs/workflows.md)** — end-to-end execution flows,
   tooling building blocks, onboarding and lookup pipelines.
- **[docs/future_concept.md](docs/future_concept.md)** — proposed dual-plane
   MCP split (Device Access MCP + Knowledge MCP) and migration phases.
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
5. **Hardware & product questions** (no device contact) — specs, interfaces,
   variants and ordering from the ingested datasheets: *"which Megaplex-4
   card gives me 16 E1 ports?"*, *"how do the ETX-2i 10G and 100G variants
   differ?"* — a `card` answer names the chassis family it plugs into
6. **Knowledge upkeep** — `/rad-harvest` re-captures the CLI reference
   after a firmware change; `/rad-load-manual` ingests a manual PDF;
   `/rad-load-datasheet` ingests the product-datasheet PDFs;
   `/rad-onboard-family` conducts a brand-new family end-to-end (calling
   the pipeline skills — never replacing them).

And the standing refusal: *"Reboot the device"* — **refused**; dangerous
commands (`admin` context, factory-default, file deletes) are out of scope
by design.

## MCP surface

**Tools** — product-agnostic verbs; the device's `family` picks the CLI dialect:

| Tool | Purpose |
|---|---|
| `list_versions` / `check_skill_version` | Report component versions; session self-check that alerts on skill↔server version or bundled/served mode drift |
| `list_devices` | Inventory, filterable by group/family |
| `test_connectivity` | SSH/telnet reachability + auth check (per the device's inventory `transport`) |
| `health_check` | Driver-defined health sweep (identity, alarms) |
| `run_show` / `run_show_in_context` | Whitelisted reads (RAD CLIs scope `show` to contexts) |
| `cli_help` | Relay the CLI's interactive `?` help — commands, argument types, constraints. Never executes |
| `snmp_probe` / `snmp_get` / `snmp_walk` | Read-only SNMP window (GET/GETNEXT only, never SET): identity + exact firmware without an SSH session, explicit-OID polls, capped walks — values decoded with catalog semantics. See `references/snmp-support.md` |
| `knowledge_status` / `mib_search` / `mib_describe` / `mib_table` / `mib_notifications` / `snmp_build_poll_plan` / `cli_search` / `manual_search` / `datasheet_search` | **Offline** semantic MIB catalog (rad-knowledge.sqlite, FTS5): concept search, full object semantics (enums/units/indexes/provenance), table models, trap payloads, CLI/manual/datasheet full-text. Never contacts a device; MIB-defined ≠ implemented (capability evidence carried separately) |
| `get_config` / `backup_config` | Full config export / snapshot to local archive |
| `stage_config` → `commit_config` | Staged writes: preview, explicit confirm, auto pre-commit backup |
| `save_startup` | Persist running config (confirm required) |

**Try it (gold-standard MIB prompt):**
> rad agent, describe RAD-EthIf-MIB::erpNodeState — exact OID, enum values, and description

A correct answer (enterprise OID `1.3.6.1.4.1.164.*`, enum values, a source
`sha256`) proves the semantic catalog is live: that RAD-proprietary detail can
only come from `rad-knowledge.sqlite`, never from model memory. More SNMP/MIB
prompts in [docs/examples.md](docs/examples.md).

**Resources:** `rad://inventory`, `rad://backups`, `rad://backups/{file}`,
`rad://command-tree/{family}`.

**Skills** (loaded by Claude on demand): `rad-core` — safety rules and the
staged-commit workflow; `rad-cli-operations` — the main RAD operations skill:
context-CLI model, verified command map, SNMP read path, and the
`references/` trees/maps harvested from live devices and vendor sources.
It covers both CLI questions and SNMP requests such as checking `sysDescr`,
polling exact OIDs, walking IF-MIB-style tables, or checking trap/alarm
coverage on a device. `rad-cli-operations` also exposes two **configurable
behavior modes** (see its SKILL.md, *"Response & verification modes"*):
response verbosity (`concise` default / `verbose`) and reference trust
(`trust-reference` default / `always-verify-live`). Both default to the
faster behavior; say e.g. *"abayev, use verbose mode"* or *"abayev, always
verify live"* to revert for the rest of a session, and the equivalent phrase
to switch back.

`/rad-harvest` (`scripts/harvest_cli.py`) now auto-creates and rolls back
numeric-indexed parameterized contexts too (`mep`, `lag`, `pw`, `bridge`,
`ppp`, ...), not just string-named ones — each addition is checked against
the **user manual** (layer 4 below) for a "safe to create" confirmation
first, and every refusal is captured with the device's own error text so a
harvest gap always comes with a reason (missing argument, license gate, or
genuinely no live instance), not a guess. Full method + a real case study:
`docs/architecture.md` and `tests/eval-report.md`.

**Slash commands** (Claude Code only): `/rad-health`, `/rad-backup`, and the
knowledge pipelines `/rad-harvest`, `/rad-load-manual`, `/rad-load-datasheet`
— composed one-time by `/rad-onboard-family` (new family end-to-end: driver →
probe → harvest → manual → MIBs/catalog → registration; the pipelines stay
independently runnable for their lifetime triggers).

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
│       ├── backends/          # transport: ssh/telnet (Netmiko) now, radview later
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
