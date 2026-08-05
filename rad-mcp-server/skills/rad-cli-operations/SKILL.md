---
name: rad-cli-operations
description: RAD skill router for ETX/SecFlow/Megaplex/MiNID/ETX-2V requests. Load whenever the user addresses "rad agent", "abayev", or "noam", or asks a broad RAD question that first needs routing across CLI syntax, manuals, SNMP, MEA/debug, vendor documentation, inventory, or live device actions.
version: 2.2.0
---

> **Skill version:** 2.2.0 - updated 2026-08-05 (2.2.0: fixed MEA prompt-category routing - "all stored MEA commands" now routes to `mea_commands_search` as primary source; `debug_tree_history` is supplemental captured-session evidence only. Added stored-first + targeted-live rule for MEA diagnostics to prevent exploratory `?` loops. 2.1.0: strict evidence-source boundary - when data is missing, never browse arbitrary workspace/repo disk paths; bundled mode may read only `skills/.../references/`; served mode must use MCP knowledge tools only. 2.0.0: split the former monolithic skill into a thin router plus domain skills: `rad-cli-reference`, `rad-reference-knowledge`, `rad-snmp-operations`, and `rad-mea-debug`; this file now owns only top-level routing and shared mode boundaries. 1.17.0: fixed MEA routing regression - stored MEA CLI/menu questions must use `debug_tree_history` first; `mea_search` is register/map-only and must not be treated as a command store; added stored-data-only stop rule and MEA anti-loop budget.)

## Session self-check (once, before your first rad-mcp tool call)

Call `check_skill_version(skill="rad-cli-operations", version="2.2.0", mode="<served if an HTML comment near the top marks this file served, otherwise bundled>")`. Surface every returned alert to the user. Alerts are warnings, not blockers.

## Role of this skill

This is the thin RAD router. It should load with `rad-core`, then hand off the deep behavior to one domain skill:

- `rad-cli-reference` - exact CLI syntax, context paths, capability grounding.
- `rad-reference-knowledge` - manuals, procedures, datasheets, Altera/vendor docs.
- `rad-snmp-operations` - OIDs, MIBs, traps, SNMP capability and poll planning.
- `rad-mea-debug` - hidden `debug mea` tree, stored MEA commands, FPGA register maps.
- `rad-device-mng` - inventory CRUD and device onboarding.

`rad-core` remains the shared safety and staged-commit policy layer.

## Domain routing matrix

Choose the domain skill by the user's actual evidence need, not by a single keyword:

| User intent | Primary domain skill | First evidence source |
|---|---|---|
| Exact CLI command, context path, `show` syntax, argument form, capability on a family | `rad-cli-reference` | CLI reference / `cli_search` |
| Procedure, explanation, limits, alarm meaning, hardware spec, datasheet, Altera doc, timing figure | `rad-reference-knowledge` | Manual/datasheet/Altera refs or served knowledge tools |
| SNMP, OID, MIB, trap, walk, poll plan, `sysDescr`, supportability | `rad-snmp-operations` | SNMP refs or `mib_*` / `snmp_*` tools |
| `debug mea`, FPGA/MEA, hidden menu paths, stored MEA commands, register block dumps | `rad-mea-debug` | `mea_commands_search` for command catalogs, `debug_tree_history` for captured menus, `mea_search` for register maps |
| Inventory list/add/remove/update, credentials placement | `rad-device-mng` | Device inventory tools |
| Live config execution, backups, commits, debug-shell safety | `rad-core` | Health check + staged flow |

## Bundled vs served boundary

- **Bundled:** read local knowledge from `skills/rad-cli-operations/references/`.
- **Served:** use MCP knowledge tools instead of repository search.
- **Never** recover missing data by scanning arbitrary workspace/repo folders.
- In bundled mode, local disk evidence is limited to `skills/.../references/` only.
- In served mode, local disk fallback is forbidden; use MCP tools or report missing data.
- Never substitute GitHub/repository search for bundled local references when the local references are the authoritative source.
- If bundled references are missing locally, treat that as a local environment problem first; rebuild/reinstall before claiming the data does not exist.

## Shared cross-domain rules

- Once the user says `stored data only`, `offline only`, or `not on live device`, stop proposing live probing in that thread.
- For MEA diagnostic prompts that combine stored + live intent, do stored preflight first (catalog/history), then run one targeted live command bundle. Do not start with exploratory `?` traversal unless the user explicitly asks to explore menus.
- If the family or target device is ambiguous, resolve it before giving family-specific commands.
- If the evidence is incomplete, say `not captured in stored data` instead of guessing.
- When you show runnable device commands, `rad-core` owns the confirmation and execution gate.

## Notes for the split

- `rad-cli-operations` stays broad so `/rad` and persona prompts still discover the RAD stack.
- The shared harvested references continue to live under `skills/rad-cli-operations/references/`; the specialized skills point to that shared tree rather than duplicating assets.
