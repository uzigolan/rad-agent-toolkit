---
name: rad-core
description: Core workflow for operating RAD devices through the rad-mcp tools — safety rules, staged-commit flow, and inventory conventions. Load whenever working with RAD/ETX devices.
---

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
lab units), load the **`rad-device-management`** skill — it covers the
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
- Planned: `etx1` (legacy ETX-1), `mp4100` (Megaplex-4100) — different CLI
  dialects, own drivers and skills to come.
