---
name: rad-mea-debug
description: RAD hidden debug tree and FPGA/MEA knowledge. Use when the user asks about `debug mea`, `FPGA>MEA`, stored MEA commands, OAM/PM/HW MEA paths, FPGA register maps, memory-map symbols, or what the device auto-programmed in MEA.
version: 1.4.0
---

> **Skill version:** 1.4.0 - updated 2026-08-05 (1.4.0: hard gate for all MEA-involved prompts - call stored MCP MEA tools first (`mea_commands_search` and/or `mea_search`, optional `debug_tree_history`) before any live `debug mea`; build targeted live commands from stored evidence; only if targeted run fails may one-step live `?` exploration be used. 1.3.0: fixed MEA category workflow drift - for "stored commands" requests use `mea_commands_search` first (not `debug_tree_history`), require explicit source labeling in answers, and for live queue diagnostics run a stored-first preflight + version check + targeted command bundle with no exploratory `?` loops unless the user asks exploration. 1.2.0: strict missing-data policy - do not scan arbitrary workspace/repo disk paths for MEA evidence; bundled mode may use only skill reference artifacts, served mode must use MCP MEA tools only. 1.1.0: added explicit MEA command-catalog routing via `mea_commands_search` for "all commands" and command-family lookups; kept `debug_tree_history` for captured sessions and `mea_search` for register maps. 1.0.0: split out of `rad-cli-operations` to own MEA/debug-tree and FPGA register-map routing.)

# RAD MEA and debug skill

## The MEA stores are different

- `debug_tree_history` is the stored MEA command/menu history.
- `mea_search` is the FPGA register/memory-map store.
- `mea_commands_search` is the static MEA command catalog text store.

Do not mix them.

## Routing split

- **All MEA commands / command-family questions:** `all commands`,
	`list MEA commands`, `MEA util fctl`, `MEA oam` -> use
	`mea_commands_search` first.
- **Stored session MEA command/menu questions:** `what was captured`,
	`under debug mea`, submenu names, OAM/PM/HW paths from prior sessions,
	exact captured syntax -> use `debug_tree_history` first.
- **Register/map questions:** addresses, register names, block dumps, FPGA table rows, mem-map symbols -> use `mea_search` first.
- **Cross-check only when needed:** for example, `debug_tree_history` points to
	`registers`, then `mea_search` supplies the mapped block details.

## Mandatory flow by prompt category

## Global MEA gate (applies to every MEA-related request)

Before any live `debug mea` action, perform stored MCP preflight first:

1. Run at least one relevant stored MCP MEA source:
	- `mea_commands_search` for command/menu/catalog intent
	- `mea_search` for register/map intent
	- optional `debug_tree_history` for previously captured session paths
2. Build a targeted live command bundle from that stored evidence.
3. Run the targeted bundle live only if the user asked for live execution.
4. Only if the targeted live run fails, do minimal live exploration (`?`) to recover.

Do not start with live menu digging.

### A) Stored-command catalog prompts

Examples: `show all stored MEA commands`, `list stored MEA util commands`,
`show in MEA data all stored commands`.

Required order:

1. `mea_commands_search` (primary authoritative source for command catalog).
2. Optional single narrowing call in `mea_commands_search` (family/category/query).
3. Use `debug_tree_history` only as supplemental "captured in sessions" evidence,
	never as the primary "all commands" source.

Do not start with `debug_tree_history` for these prompts.

### B) Stored-first then live diagnostic prompts

Examples: `based on MEA data check queues`, `use stored MEA commands then run queue checks`.

Required order:

1. Pull stored command path(s) from `mea_commands_search` for the requested area
	(for queue checks: `queue`, `counters`, `drop`, `Cluster`, `PriQueue`).
2. Optional one `debug_tree_history` check for previously captured path variants.
3. If user wants live execution, run a targeted command bundle directly.
	Avoid exploratory `?` fan-out unless the user explicitly asks exploration.

For queue checks, prefer one compact bundle such as:

- `debug mea`
- `MEA`
- `queue`
- `counters`
- `show`
- `up`
- `drop`
- `show all`
- `up`
- `Cluster`
- `show`
- `up`
- `PriQueue`
- `show`

If `drop show all` is unsupported on that variant, then fallback to `drop ?` once,
then continue with the minimum compatible form.

If any targeted command fails due to variant differences, permit one minimal
live-discovery step (`?`) at the exact failing node, then resume targeted execution.

### C) Version-aware execution rule

When the prompt asks to use stored data to choose live commands by device version:

1. Identify family and available version evidence (stored or live).
2. Prefer commands known from stored catalog/history for that family/version profile.
3. State any uncertainty explicitly as `variant-specific; not captured in stored data`.

## Stored-data-only rule

Once the user says `stored data only`, `not on live device`, or equivalent:

- do not propose `debug logon`
- do not propose `debug_menu`
- do not suggest probing hidden menus live
- do not browse arbitrary workspace/repo folders for fallback evidence

Answer from stored sources only and label any missing submenu details as `not captured in stored data`.

## Disk evidence boundary

- Bundled mode: local file evidence is allowed only from skill reference assets
	under `skills/rad-cli-operations/references/`.
- Served mode: local disk fallback is forbidden; use `mea_commands_search`,
	`debug_tree_history`, and `mea_search` only.
- If those sources do not contain the requested item, return
	`not captured in stored data`.

## Device-target rule for history

- `debug_tree_history` is command/path evidence only.
- Never treat historical `debug_tree_history` entries as the current target
	device list.
- For live execution targets, use the current managed inventory only
	(`list_devices` / explicit user-provided target in this session).

## Query budget

- Maximum MEA evidence calls per question: **3**.
- Call 1: choose the correct primary store (`mea_commands_search`,
  `debug_tree_history`, or `mea_search`).
- Call 2: one narrowing follow-up in the same store if needed.
- Call 3: one companion-store cross-check if needed.
- After that, answer and stop. Do not fan out across broad synonym searches like `fan`, `duty`, `pwm`, `cooling`, `temperature` unless the primary store actually supports that evidence type.

## Response evidence labeling

For MEA answers that combine sources, split results by source heading:

- `Source: MEA command catalog (mea_commands_search)`
- `Source: Captured debug history (debug_tree_history)`
- `Source: Live device output (debug_menu)`

Never present mixed-source content as a single unlabeled "stored data" block.

## Live-debug boundary

If the user explicitly wants live debug work on a real device, `rad-core` owns the safety policy for `debug_logon_request`, `debug_logon_submit`, `debug_menu`, `enter_debug_shell`, and `debug_shell_command`.
