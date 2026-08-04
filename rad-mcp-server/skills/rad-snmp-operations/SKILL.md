---
name: rad-snmp-operations
description: RAD SNMP and MIB reasoning for ETX/SecFlow/Megaplex/MiNID/ETX-2V families. Use when the user asks about OIDs, MIB objects, traps, `sysDescr`, walks, poll plans, SNMP capability, or family-specific SNMP support.
version: 1.0.0
---

> **Skill version:** 1.0.0 - updated 2026-08-04 (split out of `rad-cli-operations` to own SNMP and MIB routing.)

# RAD SNMP operations skill

## Sources

- **Bundled mode:** `skills/rad-cli-operations/references/snmp-support.md`, `snmp-map-<family>.md`, and `snmp-oid-map.json`.
- **Served mode:** `mib_search`, `mib_describe`, `mib_table`, `mib_notifications`, `snmp_build_poll_plan`, plus live `snmp_probe` / `snmp_get` / `snmp_walk` when the user wants device data.

## Lookup order

1. Ground family support first. SNMP support is family-specific.
2. Resolve the object or table from the SNMP reference layer or `mib_*` tools.
3. If the user wants an execution plan, build the plan before polling.
4. Use live SNMP tools only when the user wants live data and offline evidence is not enough.

## Hard rules

- A MIB definition is not proof that a family implements it.
- Prefer the verified family SNMP map over generic MIB text whenever both exist.
- Choose `snmp_get` for explicit scalar or sparse instance reads; choose `snmp_walk` for bounded subtree discovery.
- If the user says `stored data only`, stop before `snmp_probe`, `snmp_get`, and `snmp_walk`.
- When implementation evidence is missing, say so plainly instead of implying support.

## Common question mapping

- `What OID is this?` -> OID map / `mib_search`.
- `Does etx2 support this table?` -> family SNMP support + capability evidence.
- `How should I poll this?` -> `snmp_build_poll_plan` or the bundled SNMP design references.
- `What traps exist?` -> `mib_notifications` plus any family-specific alarm/trap notes.
