---
name: rad-device-mng
description: Manage the rad-mcp device inventory — list, add, update, and remove RAD/ETX/SecFlow devices. Load whenever the user wants to point this toolkit at their OWN equipment ("add my device", "register a new unit", "I want to manage my own devices", "remove that device from the list", "update the host/group for X"), not just the pre-configured lab units. ALSO load whenever the user addresses "abayev" / "Abayev", "noam" / "Noam", or "rad agent" / "RAD agent" with an inventory operation — e.g. "noam, show the list of devices", "rad agent, add my device", "abayev, remove Device3 from the list".
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

**Fresh install — no inventory file yet (expected, not a fault):**
`inventory.yaml` is gitignored, so a fresh clone has none, and `list_devices`
fails with *"Inventory file not found"* until a first device exists. Treat
that error as "empty inventory": tell the user no devices are registered yet
and offer to add the first one. **The file is created automatically by the
first successful `add_device`** — no manual copy needed (copying
`inventory.example.yaml` is the optional hand-edit path). A file that exists
but has an empty `devices:` lists normally as `[]`. (Verified live on a
fresh Linux clone via Copilot CLI, 2026-07-11.)

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

**No restart for NEW keys** (since 2026-07-10): the server re-reads `.env`
at every credential lookup (`_refresh_env()` in `inventory.py`), so a
just-added device's fresh `RAD_MCP_<NAME>_*` keys work on the very next
`test_connectivity` — the add-device flow is restart-free end to end.
The one case that still needs a server restart: **changing the value of a
key that was already loaded** (e.g. rotating a password) — already-loaded
env vars are not overridden by the re-read.

## `family` must already exist as a driver

`add_device`/`update_device` validate `family` against the drivers rad-mcp
ships (`secflow`, `etx1p`, `etx2` — check `server/rad_mcp/drivers/__init__.py`
for the current list, or just call `list_devices()` and look at what
families are already in use). Registering a device with an unsupported
family is refused with the valid list in the error — this tool adds a new
**unit** of an existing CLI dialect, not support for a new dialect. A
genuinely new dialect (legacy ETX-1, MP-4100, ...) needs its own driver —
a code change, not an inventory change.

## Adding a device — required intake (HARD GATE)

Do NOT call `add_device` until ALL SIX fields below have been explicitly
provided by the user in this conversation. If any are missing, ask for all
the missing ones in ONE consolidated question — not a drip of follow-ups —
and stop until answered.

| Field | Constraint |
|---|---|
| **name** | letters/digits/hyphens/underscores only, starts with letter/digit (becomes `RAD_MCP_<NAME>_*` env-var names). If the user's choice is invalid, propose the closest legal form and get their OK — don't silently rename. |
| **host** | IP address or resolvable hostname |
| **family** | one of the shipped drivers — `secflow`, `etx1p`, `etx2` (see driver section below). Don't guess it from the name or from past sessions; confirm with the user. |
| **group(s)** | at least one group tag, e.g. `lab` |
| **username** | for `server/.env` ONLY — never an MCP tool argument |
| **password** | same — `.env` only, and quote the value in `.env` if it contains `#` (dotenv comment char) |

Rules:
- Missing fields come from the USER — never scavenged from backups, old
  configs, or prior sessions without the user explicitly confirming the value.
- No partial adds: with any field missing, nothing is written anywhere —
  not the inventory, not `.env`.
- Optional extras (ask only if relevant, defaults otherwise): `port` (22),
  `description` ("").

## Workflow

1. **List first** — `list_devices()` to see what's already there and avoid
   name collisions.
2. **Intake gate** — collect all six required fields (section above).
3. **Add** — `add_device(name, host, family, groups=[...], description="...")`
   — facts only; the credentials NEVER appear in the tool call. Its
   response's `next_steps` spells out the `.env` keys and the restart —
   read that back to the user, don't just say "done."
4. **Write the two `.env` lines** — `RAD_MCP_<NAME>_USERNAME` /
   `RAD_MCP_<NAME>_PASSWORD` in `server/.env`. Credentials must never flow
   through an MCP tool argument or response. A local agent (Claude Code) may
   APPEND the two lines itself — append-only, without reading, printing, or
   echoing the file's existing contents; single-quote a password containing
   `#`. Otherwise, tell the user the exact two line names to add manually.
5. **Verify immediately** — new `.env` keys are picked up automatically on
   the next connection (no restart): `test_connectivity(name)`, then
   `health_check(name)`. Only a CHANGED value for an already-loaded key
   (password rotation) still needs a server restart first.
6. **If this is a new unit whose exact firmware/context tree hasn't been
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
