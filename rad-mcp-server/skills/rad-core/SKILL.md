---
name: rad-core
description: Core workflow for operating RAD devices through the rad-mcp tools — safety rules, staged-commit flow, and inventory conventions. Load whenever working with RAD/ETX devices, including whenever the user addresses "abayev" / "Abayev", "noam" / "Noam", or "rad agent" / "RAD agent".
version: 1.0.0
---

> **Skill version:** 1.0.0 · updated 2026-07-14 (bump this line and the `version:` field on every change; it's how we tell which copy is loaded)

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
- Planned: `etx1` (legacy ETX-1) — different (menu) CLI dialect, own driver
  and skill to come.

## Versions

Every skill and family driver carries a version so you can tell which revision
is loaded (and spot a stale deployed copy vs the source). When the user asks to
**show the skills and driver versions** — e.g. *"rad agent, show skills and
drivers versions"*, *"abayev, what versions are loaded"* — produce a table:

1. **Prefer the `list_versions` MCP tool** (read-only, works on every transport
   incl. Desktop). It returns `{server, skills:[{name,version}],
   drivers:[{family,version}]}`.
2. **No tool available?** Read the versions from files: each skill's `version:`
   frontmatter line in `skills/<name>/SKILL.md`, and each driver's `version`
   attribute in `server/rad_mcp/drivers/<family>.py`.

Render **two markdown tables** — *Skills* (name · version) and *Drivers*
(family · version) — and state the server version above them. Bump a skill's
`version:` (and its top-of-body line) on any skill edit, and a driver's
`version` on any change to that family's behavior; mismatched versions across
copies flag drift.
