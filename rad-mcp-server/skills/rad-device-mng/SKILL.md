---
name: rad-device-mng
description: Manage the rad-mcp device inventory — list, add, update, and remove RAD/ETX/SecFlow devices. Load whenever the user wants to point this toolkit at their OWN equipment ("add my device", "register a new unit", "I want to manage my own devices", "remove that device from the list", "update the host/group for X"), not just the pre-configured lab units. ALSO load whenever the user addresses "abayev" / "Abayev", "noam" / "Noam", or "rad agent" / "RAD agent" with an inventory operation — e.g. "noam, show the list of devices", "rad agent, add my device", "abayev, remove Device3 from the list".
version: 1.6.0
---

> **Skill version:** 1.6.0 · updated 2026-07-21 (write-tool gating list now names the 6 debug-tree tools — debug_logon_request/debug_logon_submit/debug_menu/enter_debug_shell/debug_shell_command/exit_debug_shell — alongside the config-write tools, same stdio/HTTP-write-token gating; 1.5.0: stored SNMP credentials now override the family's verified-versions gate — a per-device v3 user (or v2c community) is used even when the family profile only has another version live-verified, instead of failing with "No SNMP credentials"; 1.4.0: set_device_credentials now supports full SNMPv3 — auth_key/priv_key/auth_protocol/priv_protocol for authNoPriv/authPriv, not just the no-auth user; 1.3.0: SNMP secrets — v2c/v1 communities, v1 CSV fallback list, v3 user; 1.2.0: server-managed credentials, remote clients never touch server/.env; 1.1.0: writes DO work over HTTP with a write-scoped token, never hand-edit inventory.yaml, all 7 driver families) (bump this line and the `version:` field on every change; it's how we tell which copy is loaded)

# Managing the device inventory

This is what lets someone who receives this plugin (skills + MCP server) self
onboard their own RAD equipment, instead of being limited to whatever devices
shipped in `inventory.yaml`. Four tools, full CRUD:

| Operation | Tool | Notes |
|---|---|---|
| **List** | `list_devices(group?, family?)` | Read-only, always available (even over shared/remote transport). Credential-free summaries only. |
| **Create** | `add_device(name, host, family, transport?, port?, groups?, description?, overwrite?)` | Write tool — on by default over stdio; over shared HTTP it IS available when the client's token is write-scoped (`RAD_MCP_WRITE_TOKENS` — see the token-roles section below). |
| **Update** | `update_device(name, host?, family?, transport?, port?, groups?, description?)` | Partial update — omitted fields keep their current value. Same write gating as `add_device`. |
| **Delete** | `remove_device(name, confirm=true)` | Requires explicit user approval first, same as `commit_config`/`save_startup`. Same write gating. |
| **Secrets** | `set_device_credentials(name, username?, password?, snmp_community?, snmp_v1_community?, snmp_v1_communities?, snmp_v3_user?, snmp_v3_auth_key?, snmp_v3_priv_key?, snmp_v3_auth_protocol?, snmp_v3_priv_protocol?)` | Write tool, same gating. One tool for ALL device secrets — CLI login (username+password always as a pair) and SNMP (v2c community, v1 community, v1 CSV fallback list, v3 USM at any security level — see below). The SERVER writes them to its own `server/.env` — works identically local and remote. Effective immediately, including rotation. |

**NEVER edit `inventory.yaml` or `server/.env` by hand (or with scripts) —
the whole add-device flow, credentials included, goes through these tools.**
Both files live beside the MCP server (possibly on another machine a client
cannot reach), and the tools are what keep them consistent for every
connected client. If `add_device`/`set_device_credentials` are absent from
your tool list, that is not a cue to edit files — it means this connection is
read-only (read-only token, or `RAD_MCP_READONLY`); say so and point the user
at the token-roles section below. (Hand-editing `server/.env` on the server
host remains a valid ADMIN path — it's just never the agent's job.)

**Fresh install — no inventory file yet (expected, not a fault):**
`inventory.yaml` is gitignored, so a fresh clone has none. On first read,
the server now auto-creates `inventory.yaml` as `devices:` (empty list), and
`list_devices` returns an empty list. No manual copy is required (copying
`inventory.example.yaml` is still the optional hand-edit path).

## The one thing that trips people up: credentials

**Inventory facts and credentials live in two different places, and both are
server-managed.** `inventory.yaml` holds name/host/family/transport/port/
groups/description — facts, nothing secret. Credentials live **only** in
`server/.env` on the server host, and since 2026-07-20 the server manages
them itself via **`set_device_credentials(name, username, password)`** — the
server writes `RAD_MCP_<NAME>_USERNAME`/`_PASSWORD` into its own `.env`
(`<NAME>` = device name upper-cased, dashes → underscores — e.g. `my-etx2` →
`RAD_MCP_MY_ETX2_USERNAME`). This is THE way to set credentials when the
server runs on another machine, where no client can reach that file. The
values are never echoed back and the audit log records only that they
changed; on shared networks call it over TLS (or localhost).

**SNMP secrets go through the same tool** — pass whichever applies:
`snmp_community` (v2c), `snmp_v1_community` (v1), `snmp_v1_communities`
(v1 CSV fallback list, tried left→right), or the `snmp_v3_*` group for
SNMPv3. They map to `RAD_MCP_<NAME>_SNMP_*` keys, which is what
`snmp_probe`/`snmp_get`/`snmp_walk` resolve. After setting them, verify with
`snmp_probe(name)`.

**Stored credentials beat the family version gate.** The SNMP tools prefer
the family profile's live-verified versions (`family-profiles.yaml`,
`versions_verified`), but when the only credentials stored for a device are
for a version outside that list (e.g. a v3 USM user on a family verified
v1-only), the tools fall back to using them rather than refusing — a unit's
actual config (say, v3-only with no communities) wins over the family-level
default.

**SNMPv3 security level is determined by which fields you pass** — set only
what the device's USM user actually needs:
- **noAuthNoPriv**: `snmp_v3_user` alone.
- **authNoPriv**: + `snmp_v3_auth_key` (>=8 chars, RFC 3414 minimum);
  `snmp_v3_auth_protocol` picks `md5`/`sha`/`sha224`/`sha256`/`sha384`/`sha512`
  (default `sha` if omitted).
- **authPriv**: + `snmp_v3_priv_key` (>=8 chars) on top of the auth key;
  `snmp_v3_priv_protocol` picks `des`/`3des`/`aes`/`aes192`/`aes256` (default
  `aes` if omitted).

A priv key without an auth key is rejected — SNMPv3 has no
privacy-without-authentication mode. Ask the user for their USM user's actual
security level rather than guessing; most production units (org policy favors
v3 where available) run authPriv, not the bare no-auth user.

Alternatives that remain valid: rely on the global `RAD_MCP_USERNAME`/
`RAD_MCP_PASSWORD` (and `RAD_MCP_SNMP_*` globals) if the device shares
secrets already in `.env`, or an admin on the server host hand-editing
`server/.env`.

**Effective immediately, restarts never needed via the tool**: new keys have
always been picked up on the next connection (`_refresh_env()`), and
`set_device_credentials` also updates the running process's environment, so
even **rotating an existing password** takes effect at once. (The only
restart case left: an admin hand-edits an already-loaded key in `.env`.)

## `family` must already exist as a driver

`add_device`/`update_device` validate `family` against the drivers rad-mcp
ships (`secflow`, `etx1p`, `etx2`, `etx2v`, `mp4100`, `mp1`, `minid` — check
`server/rad_mcp/drivers/__init__.py`
for the current list, or just call `list_devices()` and look at what
families are already in use). Registering a device with an unsupported
family is refused with the valid list in the error — this tool adds a new
**unit** of an existing CLI dialect, not support for a new dialect. A
genuinely new dialect (e.g. the legacy ETX-1 menu CLI) needs its own driver —
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
| **family** | one of the shipped drivers — `secflow`, `etx1p`, `etx2`, `etx2v`, `mp4100`, `mp1`, `minid` (see driver section below). Don't guess it from the name or from past sessions; confirm with the user. |
| **group(s)** | at least one group tag, e.g. `lab` |
| **username** | passed to `set_device_credentials` after the add — never stored in the inventory |
| **password** | same — the tool quotes it safely in the server's `.env`; never echo it back into the conversation after use |

Rules:
- Missing fields come from the USER — never scavenged from backups, old
  configs, or prior sessions without the user explicitly confirming the value.
- No partial adds: with any field missing, nothing is written anywhere —
  not the inventory, not `.env`.
- Optional extras (ask only if relevant, defaults otherwise): `transport`
  (`ssh`, or `telnet` for units without SSH — telnet is cleartext, prefer
  ssh when both work), `port` (22 for ssh / 23 for telnet), `description` ("").

## Workflow

1. **List first** — `list_devices()` to see what's already there and avoid
   name collisions.
2. **Intake gate** — collect all six required fields (section above).
3. **Add** — `add_device(name, host, family, groups=[...], description="...")`
   — facts only; credentials are the next step's separate call. Read its
   response's `next_steps` back to the user, don't just say "done."
4. **Set credentials** — `set_device_credentials(name, username, password)`.
   The server writes its own `server/.env`; never edit that file yourself
   and never repeat the password back in the conversation afterwards.
5. **Verify immediately** — credentials are effective at once (no restart,
   rotation included): `test_connectivity(name)`, then `health_check(name)`.
6. **If this is a new unit whose exact firmware/context tree hasn't been
   harvested yet** (new to this family, or firmware differs from what's in
   `cli-reference-<family>.md`), suggest `/rad-harvest <name>` next — see
   the `rad-cli-operations` skill for what that produces and why.

## Update and remove

- `update_device` is a partial patch — pass only the fields that changed.
  Changing `host`/`transport`/`port`/`groups`/`description` is routine (a unit moved,
  got re-IP'd, changed team ownership). Changing `family` is not — that
  normally means the entry was created wrong, not that the hardware itself
  changed CLI dialect. Confirm with the user before changing `family`
  specifically.
- `remove_device` only forgets the device — it never touches the device
  itself, and never deletes its backup archive or audit-log history. Ask
  for explicit confirmation before calling it with `confirm=true`, same
  gate as any other destructive-sounding write tool in this toolkit.

## Why these are write tools, not always-on

`add_device`/`update_device`/`remove_device`/`set_device_credentials` (and
the config-write tools `stage_config`/`commit_config`/`save_startup`, plus
the debug-tree tools `debug_logon_request`/`debug_logon_submit`/
`debug_menu`/`enter_debug_shell`/`debug_shell_command`/`exit_debug_shell`)
are gated by transport:

- **stdio (local):** on by default — full toolset. `RAD_MCP_READONLY=true`
  turns them off.
- **http (shared/remote):** off unless the server is started with at least one
  **write-scoped** token (`RAD_MCP_WRITE_TOKENS`). Even then, every write call
  re-checks the caller's token at call time — a read-only token
  (`RAD_MCP_TOKENS`) gets reads only and is refused any write with
  *"This token is read-only…"*. `list_devices` and the other reads stay
  available to every token.

This is the per-token role model (server interlock 1): you decide, per bearer
token, who may only look and who may also change inventory/config on a shared
server. See `docs/connecting-remote-mcp.md`.

## Generating a token WITH permissions (http / shared server)

When someone wants to MANAGE devices against a server that isn't on their own
machine, they need a **write-scoped** token, and the server must be started
with that token in `RAD_MCP_WRITE_TOKENS`. Two roles, two env vars:

| Role | Env var on the server | What the holder can do |
|---|---|---|
| read-only | `RAD_MCP_TOKENS` | reads only: `list_devices`, `run_show`, `health_check`, `get_config`, `backup_config`, … |
| read-write | `RAD_MCP_WRITE_TOKENS` | all reads **plus** `add_device`/`update_device`/`remove_device`/`set_device_credentials` and staged `stage_config`/`commit_config`/`save_startup` |

Both are comma-separated; http refuses to start with neither set.

Generate a token — the value is a **secret**: it goes in the server's
environment, NEVER in an MCP tool call or the inventory:

```
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Then, on the SERVER host, put it under the variable for the role you're
granting and (re)start the server:

```
# read-write operator (can manage devices + config):
RAD_MCP_WRITE_TOKENS=<generated-token>[,<another-rw-token>]
# read-only viewer:
RAD_MCP_TOKENS=<generated-token>[,<another-ro-token>]
```

The client sends the same token as `Authorization: Bearer <token>` (the http
install-script prompt collects or auto-generates it). A token grants only the
role it was listed under on the server — a client can't self-escalate. Rotate
by editing the env var + restarting; a token appearing in BOTH lists is
treated as read-write. Use TLS once tokens cross the LAN
(`RAD_MCP_TLS_CERT`/`RAD_MCP_TLS_KEY`).
