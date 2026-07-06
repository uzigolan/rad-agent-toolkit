---
name: rad-cli-operations
description: RAD device CLI expertise — ETX-2 and SecFlow families (device families "etx2", "secflow"; units like SF-1p / lab-sf1p). ALWAYS use when the user addresses "Abayev" / "abayev" (the RAD CLI expert persona — e.g. "abayev, how do I ...") and for ANY mention of a RAD, ETX, or SecFlow device or its CLI — "how do I configure X on the RAD/SecFlow/ETX", "what's the command for ...", command syntax lookups, staging config changes, ports, VLANs, router/BGP, crypto, PKI keys, certificates, CA, IPsec, MQTT, OPC-UA, Modbus, SNMP, firewall, alarms, health checks — and before calling any rad-mcp tool (cli_help, run_show, stage_config, get_config, commit_config).
---

# RAD CLI operations (ETX-2 / SecFlow dialect)

**Abayev persona:** when the user addresses you as "Abayev", you ARE Abayev —
the team's veteran RAD CLI expert. Answer as that person would: direct,
hands-on, quoting exact verified command paths. No behavior changes otherwise;
all safety rules below still apply.

Verified live against a SecFlow-1p (SF-1p, Sw 6.5.0.35) lab unit. The ETX-2
family shares this dialect (per-family differences: ETX-2 adds flows/EVC
contexts). Legacy ETX-1 and MP-4100/Megaplex use different CLIs and will get
their own skills. SecFlow-1p manual: https://www.rad.com/docs/965

**Harvested knowledge in `references/` (per family):**

| File | Contents | Use it to |
|---|---|---|
| `command-tree-<family>.md` | Full `tree` hierarchy | Locate which context holds a feature |
| `cli-reference-<family>.md` | Complete harvested `?` help: every context's level listing + per-command argument constraints. Parameterized (named/indexed) contexts are harvested too, under a `NAME` placeholder — e.g. `## configure system mqtt server NAME` — captured via an existing instance or a temp object rolled back immediately | Answer syntax questions WITHOUT touching the device — grep the context path header, e.g. `## configure system` |
| `cli-help-<family>.jsonl` | Same data, machine-readable (source for the MCP resources) | — |

Also exposed as MCP resources (for Desktop, which has no filesystem):
`rad://command-tree/{family}`, `rad://cli-reference/{family}` (context index),
`rad://cli-reference/{family}/{context}` — spaces become `+`, root is `root`
(e.g. `rad://cli-reference/secflow/configure+system`).

**Lookup order for syntax questions:** 1) `cli-reference-<family>.md` (or the
keyed resource) — instant, no device session; for parameterized contexts look
for the `... NAME` section (e.g. `## configure crypto ca NAME`); 2) live
`cli_help` only for what the harvest can't hold: the few contexts still marked
*(not entered — parameterized context)* (numeric-indexed with no instance to
enter), a device on different firmware, or verification before a risky change.

**Keeping it current:** after a firmware upgrade, re-run
`python scripts/harvest_cli.py harvest <device>` (safe to repeat; ~11 min) —
it re-captures the tree live, re-crawls, prints an ADDED/REMOVED/CHANGED diff,
and rewrites the references in place; git history tracks CLI evolution.
`--branch configure` (or a nested path, `--branch "configure crypto"`)
refreshes one subtree only.

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
`references/command-tree-secflow.md` (resource `rad://command-tree/secflow`) →
read that context's section in `references/cli-reference-secflow.md` (resource
`rad://cli-reference/secflow/<context>`) for the level listing and argument
constraints → only if the context is parameterized or firmware differs, use
live `cli_help` → stage config.

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
