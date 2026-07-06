# rad-mcp-server — MCP Server + Claude Code Plugin for RAD Devices

> **Superseded:** the canonical, maintained architecture doc now lives inside the
> repo at [rad-mcp-server/docs/architecture.md](rad-mcp-server/docs/architecture.md)
> (kept there so it ships with the code). This file is the original design note.

> Architecture v0.2 — July 2026. Internal RAD pilot. Implemented in [rad-mcp-server/](rad-mcp-server/).
> Goal: let AI agents (Claude Code, Claude Desktop, claude.ai connectors) operate the
> **full RAD portfolio** via CLI — SecFlow (SF-1p verified live), ETX-2, and planned
> ETX-1 / MP-4100 — as an official RAD-branded plugin, the first of its kind per the
> [vendor baseline survey](vendor-mcp-baseline.md).
>
> v0.2 update from live lab work (SF-1p-187 @ 172.17.163.187): the RAD CLI is
> **context-based** — `show` commands only exist inside contexts (`configure system`,
> `configure reporting`, …), root `info` exports the full replayable running config,
> `save` is global, and the dangerous `admin` context (reboot/factory-default) is
> excluded from the read whitelist. Drivers now inherit from a shared `RadCliDriver`
> dialect base; families with different CLIs (ETX-1, MP-4100) get their own base.

---

## 1. Design decisions (locked)

| Decision | Choice | Consequence |
|---|---|---|
| Device access | **Pluggable backend — SSH first, RADview later** | Tool layer never touches Netmiko directly; it calls a `DeviceSession` facade |
| Write scope | **Full config management in v1** | Mandatory safety rails: auto-backup before write, diff preview, explicit commit, rollback, audit log |
| Product scope | **Broader RAD portfolio** | Driver registry keyed by platform; ETX-2 is the reference driver, others plug in |
| Distribution | **Internal pilot first** | Private repo, lab devices; public/marketplace release is Phase 3 |

## 2. Component overview

```
┌─────────────────────────────────────────────────────────────┐
│  Claude Code plugin  (rad-fusion)                           │
│  ├── skills/        product knowledge (per family + shared) │
│  ├── commands/      /rad-health, /rad-backup, /rad-provision│
│  └── .mcp.json      auto-registers the MCP server           │
├─────────────────────────────────────────────────────────────┤
│  MCP server  (Python, FastMCP)                              │
│  ├── tools/         typed tools (read / write / inventory)  │
│  ├── safety/        readonly toggle, whitelist, audit log,  │
│  │                  staged-commit engine                    │
│  └── inventory/     YAML device inventory + groups          │
├─────────────────────────────────────────────────────────────┤
│  Driver registry    (CLI dialect per product family)        │
│  ├── etx2/          ETX-203/205/220 — reference driver      │
│  ├── etx2i/         (Phase 2)                               │
│  └── <family>/      MiNID, ETX-5, … (as needed)             │
├─────────────────────────────────────────────────────────────┤
│  Backend layer      (transport)                             │
│  ├── ssh/           Netmiko `rad_etx` (+ custom classes)    │
│  └── radview/       RADview NB API (Phase 2)                │
└─────────────────────────────────────────────────────────────┘
```

**Separation of concerns:**
- **Backend** knows *how to reach* a device (SSH session vs RADview API call).
- **Driver** knows *how to speak* to a product family (prompt patterns, command
  syntax, config-mode entry/exit, save command, health-check command set).
- **Tools** are product-agnostic verbs; they resolve device → driver → backend.
- **Skills** hold the operational knowledge (what to check, in what order, what
  "good" looks like) — the layer generic Netmiko wrappers can't replicate.

## 3. MCP tool surface (v1)

### Inventory & session
| Tool | Notes |
|---|---|
| `list_devices` | From inventory YAML; filterable by group/family/site |
| `get_device_info` | Model, SW version, serial, uptime — auto-detects family |
| `test_connectivity` | Reachability + auth check without running commands |

### Read (safe)
| Tool | Notes |
|---|---|
| `run_show` | Whitelist-validated show/display commands only |
| `get_config` | Running config (full or section) |
| `get_alarms` | Active alarms + recent log |
| `health_check` | Driver-defined command set: interfaces, SFP/DDM, CPU, services, OAM |

### Write (guarded — every call passes the staged-commit engine)
| Tool | Notes |
|---|---|
| `stage_config` | Takes config lines → returns a **diff preview** + stage-ID. Nothing touches the device config yet beyond a candidate check where the platform supports it |
| `commit_config` | Requires stage-ID + explicit `confirm=true`. Auto-backs-up running config first. Optional `revert_timer` (commit-confirm pattern) |
| `rollback_config` | Restore the pre-commit backup |
| `save_startup` | Persist running → startup |
| `backup_config` / `restore_config` | File-level backup to a local archive dir |

### Safety rails (non-negotiable, from the baseline doc's best-practice list)
1. `RAD_MCP_READONLY=true` env toggle disables all write tools at registration time.
2. `run_show` accepts only whitelisted command prefixes per driver — no raw shell strings.
3. Every write: **backup → diff → confirm → commit → verify**, no shortcuts.
4. Append-only audit log (JSONL): who/when/device/command/result, credentials redacted.
5. Credentials **never** in inventory files — env vars or OS keychain only.
6. Per-device concurrency lock — one write session per device at a time.

## 4. Repo layout

```
rad-fusion/
├── .claude-plugin/
│   ├── plugin.json               # name: rad-fusion, version, description
│   └── marketplace.json          # for internal marketplace → later public
├── .mcp.json                     # stdio launch of the server
├── server/
│   ├── pyproject.toml            # fastmcp, netmiko, pydantic
│   ├── rad_fusion/
│   │   ├── server.py             # entrypoint: stdio now, streamable-http flag later
│   │   ├── tools/                # one module per tool group
│   │   ├── safety/               # staging engine, whitelist, audit, redaction
│   │   ├── drivers/
│   │   │   ├── base.py           # RadDriver ABC
│   │   │   └── etx2.py           # reference implementation
│   │   ├── backends/
│   │   │   ├── base.py           # Backend ABC (execute, get_config, push_config)
│   │   │   └── ssh.py            # Netmiko rad_etx
│   │   └── inventory.py
│   └── tests/                    # driver unit tests against recorded CLI transcripts
├── skills/
│   ├── rad-core/                 # shared: inventory conventions, safety workflow
│   ├── etx2-operations/          # ETX-2 CLI reference, config hierarchy, flows/EVCs
│   ├── etx2-troubleshooting/     # CFM/Y.1731, loopbacks, symptom→command playbooks
│   └── etx2-provisioning/        # guided service-activation sequences
├── commands/
│   ├── rad-health.md             # /rad-health [device|group]
│   ├── rad-backup.md             # /rad-backup [device|group]
│   └── rad-provision.md          # /rad-provision — walks the staged-commit flow
└── inventory.yaml.example
```

## 5. Key abstractions

```python
class Backend(ABC):
    """Transport: how bytes reach the device."""
    def execute(self, device: Device, command: str) -> str: ...
    def get_config(self, device: Device, section: str | None) -> str: ...
    def push_config(self, device: Device, lines: list[str]) -> PushResult: ...

class RadDriver(ABC):
    """CLI dialect: how a product family is spoken to."""
    family: str                       # "etx2", "etx2i", "minid", ...
    netmiko_device_type: str          # "rad_etx" for ETX-2
    show_whitelist: list[str]         # allowed read-command prefixes
    health_commands: list[str]        # what health_check runs
    def enter_config(self) -> list[str]: ...
    def save_command(self) -> str: ...
    def diff(self, running: str, candidate: list[str]) -> str: ...
    def detect(self, banner_or_version_output: str) -> bool:  # auto-detection
```

New product family = one driver module + one skill folder. No tool changes.

## 6. Phases

| Phase | Deliverable | Exit criteria |
|---|---|---|
| **1 — Pilot core** | SSH backend + ETX-2 driver + read tools + health-check skill; stdio plugin installed by pilot team | Health check + config backup working against lab ETX units |
| **1.5 — Writes** | Staged-commit engine, provision/rollback tools, provisioning skill | A full EVC/flow provision executed end-to-end via Claude with diff+confirm |
| **2 — Breadth** | RADview backend, second product-family driver, streamable-http transport (token auth) → usable as claude.ai/Desktop connector | Second family passes the same test suite; remote deployment on a bastion |
| **3 — Release** | Security review, docs, public RAD GitHub org repo, MCP Registry + plugin marketplace listing | First **[OFFICIAL]** RAD entry in the ecosystem |

## 7. Open questions

- [ ] Which product family is #2 after ETX-2 (drives the abstraction test)?
- [ ] Does the lab have ETX units reachable via SSH from the dev machine, or do we need a jump host? (affects backend: Netmiko supports SSH proxy)
- [ ] RADview NB API: REST availability/version in your deployment — determines Phase 2 backend design.
- [ ] Naming: `rad-fusion` (working title, matches this workspace) — confirm or rename before repo creation.
- [ ] Firmware upgrade tooling — in scope for v1 or explicitly out?
