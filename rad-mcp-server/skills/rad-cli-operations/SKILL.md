---
name: rad-cli-operations
description: RAD context-based CLI operations (ETX-2, SecFlow families — device families "etx2" and "secflow") — CLI model, verified command paths, health interpretation. Load when running commands on RAD devices.
---

# RAD CLI operations (ETX-2 / SecFlow dialect)

Verified live against a SecFlow-1p (SF-1p, Sw 6.5.0.35) lab unit — full command
tree captured in `server/logs/smoke-lab-sf1p.txt`. The ETX-2 family shares this
dialect (per-family differences: ETX-2 adds flows/EVC contexts). Legacy ETX-1
and MP-4100/Megaplex use different CLIs and will get their own skills.
SecFlow-1p manual: https://www.rad.com/docs/965

## CLI model (critical to understand)

- The CLI is **context-based**: `show` commands do NOT exist at the root
  prompt. You must navigate into a context first — use the
  `run_show_in_context(device, context, command)` tool for this.
- Global commands work in every context: `info`, `level-info`, `help`, `tree`,
  `ping`, `trace-route`, `history`, `save`, `exit`.
- Root `info` dumps the **full running configuration** in replayable CLI form —
  this is what `get_config` uses.
- `exit all` returns to the root context from anywhere.
- Output modifiers: `command | include <regex>`, `| exclude`, `| begin`.

## Verified command map

| Purpose | Context | Command |
|---|---|---|
| Device identity (model, SW, MAC, uptime) | `configure system` | `show device-information` |
| CPU / RAM / disk metrics | `configure system` | `show resources` |
| System info / date | `configure system` | `show system`, `show system-date` |
| Hardware+software inventory | `configure system` | `show summary-inventory` |
| Full diagnostic dump (slow) | `configure system` | `show tech-support` |
| Active alarms | `configure reporting` | `show active-alarms` |
| Active alarms with timestamps + descriptions | `configure reporting` | `show active-alarms-details` |
| Alarm / event log | `configure reporting` | `show alarm-log`, `show log`, `show log-summary` |
| Port config (admin state, VLANs) | `configure port ethernet <n>` | `info` |
| Router interfaces (admin/oper state, IPs, bindings) | `configure router <n>` | `show summary-interface` |
| Routing/neighbor tables | `configure router <n>` | `show routing-table`†, `show arp-table`, `show rib` |
| Startup config | `file` | `show startup-config` |
| Rollback config | `file` | `show rollback-config` |
| Software status | `admin software` | `show status` |
| Full running config | root | `info` |
| Command discovery | any context | `tree` (levels below here), `help` |
| Persist config | any context | `save` |

† syntax accepted; returned empty on the lab unit (no dynamic routes) — output
format unverified.

Top-level `configure` contexts (SF-1p): access-control, bridge, crypto, fault,
management, monitor, oam, port, protection, qos, reporting, router, sd-iot,
system, terminal.

Some contexts are **indexed** and refuse navigation without an index — e.g.
`configure router` errors; it must be `configure router <1..10>`. The error is
self-describing: a failed navigation returns the expected parameters
(`- router <number> ... [1..10]`), so a NAVIGATION ERROR from
`run_show_in_context` usually tells you the missing piece. `tree` on a parent
context is the reliable way to discover what an unfamiliar subtree contains.

## Interactive help: the `cli_help` tool (the CLI is self-documenting)

The CLI answers `?` at any point, and the **`cli_help(device, context,
prefix)`** MCP tool relays it. This is the authoritative way to learn command
syntax for the exact firmware on the device (richer than `tree`, which shows
structure but not arguments). Nothing is executed — the tool clears the
pending input after capturing the help.

- `cli_help(dev, context, "")` — lists every command/leaf at that level with
  one-line descriptions (context `""` = root).
- `cli_help(dev, context, "<command> ")` — **trailing space matters** — lists
  the command's arguments with types and constraints, e.g. prefix
  `"location "` → `<location-of-device> : Device location [0..255 chars]`.
- For multi-argument commands the listing shows accepted keyword/positional
  arguments; `<CR>` in the list means the command is also valid as-is.

Semantics of the listings (verified):

- `+` marks a sub-context you can navigate into; `-` marks a command/leaf.
- A `[no]` prefix on a leaf (e.g. `[no] location`) means the attribute is
  **removable**: `no <leaf>` deletes/unsets it. When reverting config, prefer
  `no <leaf>` over setting an empty value.
- Constraint brackets give validation ranges: `[2..2 chars]`,
  `[0..255 chars, default ...]` — validate values with `cli_help` BEFORE
  staging config, not after a commit fails.
- Level `?` listings also enumerate the context's `show` commands — use this
  to discover reads not yet in the verified map above.

**Workflow for any unfamiliar config task:** find the right context in
`references/command-tree-secflow.md` (also exposed as MCP resource
`rad://command-tree/secflow`) → `cli_help` at that level to see the leaves →
`cli_help` with `"<leaf> "` to get exact argument constraints → stage config.

Useful writable leaves under `configure system`: `name "..."`, `location "..."`,
`contact "..."` (safe, non-service-affecting — good for write-path testing).

## ⚠ Dangerous areas — never navigate here for reads

The `admin` context contains `reboot`, `force-reboot`, `factory-default`,
`factory-default-all`, `user-default`. Never send these; a factory-default or
reboot is service-affecting. The `file` context contains `delete*` commands —
only use its `show ...` commands.

Contexts are not purely navigational — some hold **action commands** alongside
config leaves. `configure router <n>` has `clear-arp-table`,
`clear-neighbor-table`, `clear-bfd-statistics`, `nat clear-nat-translations`,
and `delete` under `prefix-list`/`route-map`. Treat any `clear-*`/`delete`
token as a write: never send one via a read tool or without the staged flow.

## Health interpretation

1. `show device-information` — confirm expected SW version and sane uptime.
2. `show active-alarms` — any major/critical alarm → investigate before changes.
3. For service issues: physical port status → bridge/router state → OAM state.

## Config changes

Config lines for `stage_config` must be a complete, self-contained sequence
starting and ending at root, mirroring the `info` export format, e.g.:

```
exit all
configure system
location "site-A rack 3"
exit all
```

Always end with `exit all`. Changes affect the **running** config only until
`save_startup` is called — a revert is just staging the previous value back.
Verify after commit by re-running the relevant context `info` or `show`.
Rollback: stage the inverse commands or restore from the pre-commit backup
(path is in the commit_config output).
