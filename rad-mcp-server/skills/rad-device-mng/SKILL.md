---
name: rad-device-mng
description: Manage the rad-mcp device inventory — list, add, update, and remove RAD/ETX/SecFlow devices. Load whenever the user wants to point this toolkit at their OWN equipment ("add my device", "register a new unit", "I want to manage my own devices", "remove that device from the list", "update the host/group for X"), not just the pre-configured lab units.
---

# Managing the device inventory

This is what lets someone who receives this plugin (skills + MCP server) self
onboard their own RAD equipment, instead of being limited to whatever devices
shipped in `inventory.yaml`. Four tools, full CRUD:

| Operation | Tool | Notes |
|---|---|---|
| **List** | `list_devices(group?, family?)` | Read-only, always available (even over shared/remote transport). Credential-free summaries only. |
| **Create** | `add_device(name, host, family, port?, groups?, description?, overwrite?)` | Write tool — local/stdio only, never over shared HTTP. |
| **Update** | `update_device(name, host?, family?, port?, groups?, description?)` | Partial update — omitted fields keep their current value. |
| **Delete** | `remove_device(name, confirm=true)` | Requires explicit user approval first, same as `commit_config`/`save_startup`. |

## The one thing that trips people up: credentials

**Inventory facts and credentials live in two different places, and the
tools only ever touch one of them.** `inventory.yaml` holds name/host/
family/port/groups/description — facts, nothing secret. Credentials live
**only** in `server/.env`, and none of these four tools read, write, or even
see them. After `add_device`, the device exists but has no way to log in
until you also set, in `server/.env`:

```
RAD_MCP_<NAME>_USERNAME=...
RAD_MCP_<NAME>_PASSWORD=...
```

(`<NAME>` = the device name, upper-cased, dashes → underscores — e.g. `my-etx2`
→ `RAD_MCP_MY_ETX2_USERNAME`.) Or skip the per-device pair entirely and rely
on the global `RAD_MCP_USERNAME`/`RAD_MCP_PASSWORD` if this device shares
credentials with others already in `.env`.

**Then restart the MCP server.** `.env` is loaded once at process start
(`load_dotenv()` in `inventory.py`) — a running server process will not see
new `.env` values until it's relaunched. This has bitten this exact
workflow before: adding a device and immediately calling `test_connectivity`
against the *same running process* fails with a credentials error that has
nothing to do with the device itself.

## `family` must already exist as a driver

`add_device`/`update_device` validate `family` against the drivers rad-mcp
ships (`secflow`, `etx1p`, `etx2` — check `server/rad_mcp/drivers/__init__.py`
for the current list, or just call `list_devices()` and look at what
families are already in use). Registering a device with an unsupported
family is refused with the valid list in the error — this tool adds a new
**unit** of an existing CLI dialect, not support for a new dialect. A
genuinely new dialect (legacy ETX-1, MP-4100, ...) needs its own driver —
a code change, not an inventory change.

## Workflow

1. **List first** — `list_devices()` to see what's already there and avoid
   name collisions.
2. **Add** — `add_device(name, host, family, groups=[...], description="...")`.
   Its response's `next_steps` spells out exactly what `.env` keys to set
   and to restart the server — read that back to the user, don't just say
   "done."
3. **Guide the user to edit `server/.env`** — this step cannot be automated
   from inside the tool call (credentials must never flow through an MCP
   tool argument or response). Tell them the exact two line names to add.
4. **After they confirm `.env` is set and the server's been restarted** —
   `test_connectivity(name)`, then `health_check(name)`.
5. **If this is a new unit whose exact firmware/context tree hasn't been
   harvested yet** (new to this family, or firmware differs from what's in
   `cli-reference-<family>.md`), suggest `/rad-harvest <name>` next — see
   the `rad-cli-operations` skill for what that produces and why.

## Update and remove

- `update_device` is a partial patch — pass only the fields that changed.
  Changing `host`/`port`/`groups`/`description` is routine (a unit moved,
  got re-IP'd, changed team ownership). Changing `family` is not — that
  normally means the entry was created wrong, not that the hardware itself
  changed CLI dialect. Confirm with the user before changing `family`
  specifically.
- `remove_device` only forgets the device — it never touches the device
  itself, and never deletes its backup archive or audit-log history. Ask
  for explicit confirmation before calling it with `confirm=true`, same
  gate as any other destructive-sounding write tool in this toolkit.

## Why these are write tools, not always-on

`add_device`/`update_device`/`remove_device` are registered only when the
server isn't running read-only (`RAD_MCP_READONLY`, and always implied by
the shared/remote HTTP transport). A remote client silently registering or
deleting inventory entries on a shared server is exactly the class of
surprise the read-only interlock exists to prevent — see
`docs/architecture.md`'s safety model. `list_devices` stays available
everywhere since it's pure read.
