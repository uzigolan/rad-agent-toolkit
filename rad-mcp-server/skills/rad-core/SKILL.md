---
name: rad-core
description: Core workflow for operating RAD devices through the rad-mcp tools — safety rules, staged-commit flow, and inventory conventions. Load whenever working with RAD/ETX devices, including whenever the user addresses "abayev" / "Abayev", "noam" / "Noam", or "rad agent" / "RAD agent".
version: 1.3.0
---

> **Skill version:** 1.3.0 · updated 2026-07-21 (golden rule 7: debug_logon_request/submit/debug_menu/enter_debug_shell/debug_shell_command require an explicit user request, never inferred) (bump this line and the `version:` field on every change; it's how we tell which copy is loaded)

## Session self-check (once, at session start)

Call `check_skill_version(skill="rad-core", version="<the X.Y.Z from the Skill
version line above>")` once and surface any returned `alerts` to the user —
version drift between this loaded skill and the connected server's copy. A
mismatch is a warning, not a blocker; if the tool is unavailable, skip
silently.

# Operating RAD devices with rad-mcp

## Golden rules

1. **Look before you touch.** Before any configuration work, run `health_check`
   (or at minimum `test_connectivity`) and review active alarms.
2. **Never bypass the staged flow.** All config changes go:
   `backup_config` → `stage_config` → show the preview to the user →
   `commit_config(stage_id, confirm=true)` only after the user explicitly approves.
3. **Never call `commit_config` or `save_startup` with `confirm=true` unless the
   user approved that exact change in this conversation.**
4. `run_show` accepts only whitelisted read commands. If a command is refused,
   do not look for a way around the whitelist — tell the user.
5. After a commit, verify: re-run the relevant `show`/`info` command and compare
   against the intent before declaring success.
6. If anything looks wrong after a commit, the pre-commit backup path is in the
   commit output — offer to restore rather than iterating blind fixes on a
   possibly-degraded device.
7. **Never call `debug_logon_request`, `debug_logon_submit`, `debug_menu`,
   `enter_debug_shell`, or `debug_shell_command` unless the user has
   explicitly asked to enter debug/shell mode on a specific device in this
   conversation.** These unlock a RAD unit's hidden `debug` tree and, beyond
   it, its real OS shell — completely outside the read whitelist and the
   staged-commit flow, with no safety net but the audit log.
   `debug_logon_request` returns a key code you cannot decrypt yourself —
   ask the user for the resulting password (computed by their own
   confidential tool) rather than guessing or inventing one, then pass it to
   `debug_logon_submit`. See `rad-cli-operations`'s dangerous-areas section
   for the full rationale.

## Inventory

Devices live in `inventory.yaml` (name, host, family, groups). Credentials are
NEVER in the inventory — they come from `server/.env`. Do not read, print, or
log credential values. To list, add, update, or remove a device (e.g. the
user wants to point this at their own equipment, not just the pre-configured
lab units), load the **`rad-device-mng`** skill — it covers the
`list_devices`/`add_device`/`update_device`/`remove_device` tools and the
credentials-live-in-`.env`-not-inventory workflow in full.

## Product families

The plugin targets the full RAD portfolio; each family maps to a driver under
`server/rad_mcp/drivers/`:

- `secflow` — SecFlow secure industrial gateways (SF-1p verified live). Shared
  RAD CLI dialect — see the `rad-cli-operations` skill.
- `etx1p` — ETX-1p demarcation units, verified live. Same shared dialect,
  its own driver (`drivers/etx1p.py`); NOT the legacy `etx1`.
- `etx2` — ETX-2 carrier-Ethernet demarcation family (ETX-203AX/205A/220A/
  ETX-2I), verified live on an ETX-2I unit. Same dialect, with family-specific
  quirks (no `show resources`, slot/port naming) — see `drivers/etx2.py`.
- `mp4100` — Megaplex-4100 multiservice access nodes, verified live
  (marks-mp4, Mn 4.91). Same shared dialect with a **candidate-DB config
  model**: staged sequences must end with the device's `commit` global or
  nothing applies — see `rad-cli-operations` and `drivers/mp4100.py`.
- `mp1` — MP-1, verified live (mp-one, SW 2.20(0.61)). Shared context-CLI
  dialect over standard SSH, with a **candidate-DB config model** like mp4100:
  staged sequences must end with the device's `commit` global or nothing
  applies (never send `discard-changes` casually). CLI reference + manual
  harvested; `configure_contexts` grounded from the live tree (`drivers/mp1.py`).
- `minid` — MiNID miniature NID / SFP sleeve device, verified live (minid-1,
  172.17.166.55, prompt `MiNID#`, SW 2.6). Shared context-CLI dialect — probe
  confirmed `MiNID#` → `MiNID>config>system#` navigation and `info`/`save`
  globals (**direct-write save**, NOT candidate-DB like mp4100/mp1). Its SSH is
  **fragile/unique**, so `drivers/minid.py` ships a patient per-family connect
  profile (long timeouts, keepalive, slow pacing, extra retries). Manual
  ingested; CLI reference harvested from the live tree (`drivers/minid.py`).
- `etx2v` — ETX-2V, verified live (etx2v-1, 172.17.240.100, prompt `uCPE-OS#`).
  RAD's uCPE-OS platform on ETX-2V chassis hardware; shared context-CLI dialect
  over **standard SSH** (not fragile), direct-write save. Distinctive top-level
  `virtualization` context (VNF hosting) plus crypto/ipsec, oam twamp, ldap.
  719-node tree / 527 captures harvested; hardware+BIOS manual ingested
  (`drivers/etx2v.py`).

## Versions

Every skill and family driver carries a version so you can tell which revision
is loaded (and spot a stale deployed copy vs the source). When the user asks to
**show the skills and driver versions** — e.g. *"rad agent, show skills and
drivers versions"*, *"abayev, what versions are loaded"* — produce a table:

1. **Prefer the `list_versions` MCP tool** (read-only, works on every transport
   incl. Desktop). It returns `{server, skills:[...], drivers:[...], knowledge_catalog:{...}}`
   (the catalog block reports the served-mode DB build, or "not built" in bundled mode).
2. **No tool available?** Read the versions from files: each skill's `version:`
   frontmatter line in `skills/<name>/SKILL.md`, and each driver's `version`
   attribute in `server/rad_mcp/drivers/<family>.py`.

Render **two markdown tables** — *Skills* (name · version) and *Drivers*
(family · version) — and state the server version above them. Bump a skill's
`version:` (and its top-of-body line) on any skill edit, and a driver's
`version` on any change to that family's behavior; mismatched versions across
copies flag drift.

## MCP tools status checker

When the user asks for MCP status (examples: "rad agent, what is MCP tools
status", "show MCP status", "is MCP working"), return a compact status table
with explicit terms:

- `OK` — check succeeded.
- `DEGRADED` — MCP is reachable but a capability is limited (for example,
   served mode without an available knowledge catalog).
- `MISSING` — expected capability/tool data is unavailable.

Run these checks in order and include them in one markdown table:

1. `list_versions` — proves MCP server reachability and reports server/skills/drivers.
2. `knowledge_status` — reports knowledge-catalog availability.
3. `list_devices` — verifies inventory read path.
4. Then report **every RAD MCP tool (no exceptions)** with its own row.

If `list_devices` returns empty during this test flow, run a temporary device
cycle so device-bound tools can be probed:

1. `add_device` a demo entry (for example `rad-toolcheck-demo`, family `etx2`,
   host `192.0.2.10`, group `toolcheck`, description `temporary status check`).
2. Run the device-bound tool probes against that demo device.
3. Always clean up at the end with `remove_device(name, confirm=true)`.

Treat connectivity/auth failures on the demo unit as `DEGRADED` evidence,
not as missing tools.

Expected tool inventory for the table (include all rows even when unavailable):

- `check_skill_version`
- `list_versions`
- `knowledge_status`
- `manual_search`
- `cli_search`
- `mib_search`
- `mib_notifications`
- `list_devices`
- `run_show`
- `run_show_in_context`
- `cli_help`
- `health_check`
- `snmp_walk`
- `remove_device`

Table columns (always):

- `Tool`
- `Status`
- `Evidence`
- `Dependencies / Prerequisites`

Status mapping:

- If `list_versions` fails: mark all tools `MISSING` with reason "MCP not reachable".
- If a tool is not available in this runtime/transport: mark it `MISSING` and state
  the missing capability under `Dependencies / Prerequisites`.
- If a tool is available but blocked by setup state (for example empty inventory,
  missing catalog data, missing confirm flag): mark it `DEGRADED` and list the
  exact prerequisite(s) under `Dependencies / Prerequisites`.
- If a tool call succeeds as expected: mark it `OK`.

Prerequisites text should be explicit and actionable, for example:

- "requires at least one registered device"
- "requires knowledge catalog with MIB objects"
- "requires user-approved confirm=true"
- "depends on MCP server reachability"

Always finish with a one-line overall state:

- `Overall: OK`
- `Overall: DEGRADED`
- `Overall: MISSING`
