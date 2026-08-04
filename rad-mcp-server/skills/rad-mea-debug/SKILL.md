---
name: rad-mea-debug
description: RAD hidden debug tree and FPGA/MEA knowledge. Use when the user asks about `debug mea`, `FPGA>MEA`, stored MEA commands, OAM/PM/HW MEA paths, FPGA register maps, memory-map symbols, or what the device auto-programmed in MEA.
version: 1.0.0
---

> **Skill version:** 1.0.0 - updated 2026-08-04 (split out of `rad-cli-operations` to own MEA/debug-tree and FPGA register-map routing.)

# RAD MEA and debug skill

## The two stores are different

- `debug_tree_history` is the stored MEA command/menu history.
- `mea_search` is the FPGA register/memory-map store.

Do not mix them.

## Routing split

- **Stored MEA command/menu questions:** `which MEA commands`, `under debug mea`, submenu names, OAM/PM/HW paths, exact MEA syntax -> use `debug_tree_history` first.
- **Register/map questions:** addresses, register names, block dumps, FPGA table rows, mem-map symbols -> use `mea_search` first.
- **Cross-check only when needed:** for example, `debug_tree_history` points to `registers`, then `mea_search` supplies the mapped block details.

## Stored-data-only rule

Once the user says `stored data only`, `not on live device`, or equivalent:

- do not propose `debug logon`
- do not propose `debug_menu`
- do not suggest probing hidden menus live

Answer from stored sources only and label any missing submenu details as `not captured in stored data`.

## Query budget

- Maximum MEA evidence calls per question: **3**.
- Call 1: choose the correct primary store.
- Call 2: one narrowing follow-up in the same store if needed.
- Call 3: one companion-store cross-check if needed.
- After that, answer and stop. Do not fan out across broad synonym searches like `fan`, `duty`, `pwm`, `cooling`, `temperature` unless the primary store actually supports that evidence type.

## Live-debug boundary

If the user explicitly wants live debug work on a real device, `rad-core` owns the safety policy for `debug_logon_request`, `debug_logon_submit`, `debug_menu`, `enter_debug_shell`, and `debug_shell_command`.
