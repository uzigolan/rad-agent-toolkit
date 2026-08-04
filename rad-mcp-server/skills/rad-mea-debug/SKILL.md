---
name: rad-mea-debug
description: RAD hidden debug tree and FPGA/MEA knowledge. Use when the user asks about `debug mea`, `FPGA>MEA`, stored MEA commands, OAM/PM/HW MEA paths, FPGA register maps, memory-map symbols, or what the device auto-programmed in MEA.
version: 1.2.0
---

> **Skill version:** 1.2.0 - updated 2026-08-04 (1.2.0: strict missing-data policy - do not scan arbitrary workspace/repo disk paths for MEA evidence; bundled mode may use only skill reference artifacts, served mode must use MCP MEA tools only. 1.1.0: added explicit MEA command-catalog routing via `mea_commands_search` for "all commands" and command-family lookups; kept `debug_tree_history` for captured sessions and `mea_search` for register maps. 1.0.0: split out of `rad-cli-operations` to own MEA/debug-tree and FPGA register-map routing.)

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

## Query budget

- Maximum MEA evidence calls per question: **3**.
- Call 1: choose the correct primary store (`mea_commands_search`,
  `debug_tree_history`, or `mea_search`).
- Call 2: one narrowing follow-up in the same store if needed.
- Call 3: one companion-store cross-check if needed.
- After that, answer and stop. Do not fan out across broad synonym searches like `fan`, `duty`, `pwm`, `cooling`, `temperature` unless the primary store actually supports that evidence type.

## Live-debug boundary

If the user explicitly wants live debug work on a real device, `rad-core` owns the safety policy for `debug_logon_request`, `debug_logon_submit`, `debug_menu`, `enter_debug_shell`, and `debug_shell_command`.
