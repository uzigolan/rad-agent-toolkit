# Plan 01 — Capability grouping (transitional)

**Branch:** `main`, behind a flag · **Risk:** low · **Requires:** plan 00
**Leads to:** [plan 09](09-server-extraction.md) — the actual split

---

## Read this framing first

Earlier drafts of this plan treated env-flag profiles as the destination. They
are not. Per [DECOMPOSITION.md](DECOMPOSITION.md), the destination is separate
servers per blast radius. **This plan's only job is to prove the groupings are
correct before you pay the cost of process separation.**

That is worth doing anyway: the groups below are exactly the future server
boundaries, so if a tool turns out to sit wrong, you find out for the price of
an env var rather than a package extraction.

---

## Why grouping is needed at all

The server exposes **43 tools [VERIFIED — enumerated below from a live
session]**; `docs/architecture.md` shows 18 in its stack diagram and is out of
date.

Guidance puts the working ceiling near 20 tools, degrading past about 10. One
server carrying 43 is most of a NOC engineer's whole context budget before
their other servers load.

The shape matters more than the count: **8 of the 43 are the debug tree** —
described in your own docs as unrestricted root access — advertised in every
ordinary session on a server whose safety story is defense in depth.

---

## The current 43 [VERIFIED]

```
add_device                 altera_search              backup_config
check_skill_version        cli_help                   cli_search
commit_config              datasheet_search           debug_access_preflight
debug_logon_request        debug_logon_submit         debug_menu
debug_shell_command        debug_tree_history         enter_debug_shell
exit_debug_shell           get_config                 health_check
knowledge_status           list_devices               list_versions
manual_search              mea_commands_search        mea_search
mib_describe               mib_notifications          mib_search
mib_table                  remove_device              run_demo_device
run_show                   run_show_in_context        save_startup
set_device_credentials     snmp_build_poll_plan       snmp_get
snmp_probe                 snmp_walk                  stage_config
stop_demo_device           test_connectivity          tool_versions
update_device
```

Re-enumerate against the real registration code before starting.

---

## Groups — these become servers in plan 09

Introduce `RAD_MCP_TOOL_PROFILE`, values `legacy` (default) and `lean`.
`legacy` registers a byte-identical surface to today, which is what makes this
safe to merge immediately.

> **[CORRECTED during implementation]** “byte-identical” conflicted with the
> `set_device_credentials` removal below (mandated in **both** profiles — the
> security requirement wins). Actual `legacy` = **42** tools: the pre-grouping
> 43 minus `set_device_credentials`, verified by diffing `tools/list` — that
> one name is the only difference.

| Group | Flag | Default in `lean` | Future home |
|---|---|---|---|
| **knowledge** | — | on | `rad-knowledge` |
| **device** | — | on | `rad-device` |
| **snmp** | `RAD_MCP_SNMP` | on | `rad-device` |
| **debug** | `RAD_MCP_DEBUG_TOOLS` | **off** | `rad-debug` |
| **inventory** | `RAD_MCP_INVENTORY_WRITE` | **off** | `rad-inventory` |
| **dev** | `RAD_MCP_DEV_TOOLS` | off | dropped |

**knowledge** — the 10 search tools. Untouched here; collapsed to 2 in
[plan 03](03-knowledge-search-facade.md).

**device (11)** — `list_devices` `test_connectivity` `run_show`
`run_show_in_context` `cli_help` `get_config` `health_check` `backup_config`
`stage_config` `commit_config` `save_startup`.
`RAD_MCP_READONLY=true` still removes the write tools **[VERIFIED — existing
behaviour, preserve exactly]**. Flags compose; readonly always wins.

**snmp (4)** — read-only by construction, central to the product story, so on
by default.

**debug (8) [CORRECTED — the earlier “9” double-counted]** —
`debug_access_preflight` `debug_logon_request` `debug_logon_submit`
`debug_menu` `debug_shell_command` `debug_tree_history` `enter_debug_shell`
`exit_debug_shell` (`debug_access_preflight` is one OF the 8, not an extra).
Off by default. This flag is the single highest-value line in the plan.

**inventory (3)** — `add_device` `update_device` `remove_device`. Off by
default: a shared HTTP deployment must not let any connected client rewrite
the fleet.

**`set_device_credentials` is removed from the tool surface entirely.**
Credential provisioning becomes a CLI command run by a human. Leaving it
callable means an injection path can end at "rotate the credentials on this
device," which is the worst outcome available and serves no agent workflow.

**dev (2)** — `run_demo_device` `stop_demo_device`. Off by default; kept
because plan 00's eval harness uses them as fixtures.

### Dropped from tools, moved to resources (4)

`list_versions` `tool_versions` `check_skill_version` `knowledge_status`.

Introspection, not action. Fold into `rad://status`: server version, loaded
skill versions, active profile, enabled flags, and corpus build identity
(which comes from [plan 08](08-ingestion-and-corpus-contract.md)). Keep the
functions; drop the `@tool` registration.

### Counts

[CORRECTED — verified against the live surface at implementation time]

| Profile | Tools |
|---|---|
| `legacy` | **42** (43 minus `set_device_credentials`) |
| `lean`, defaults | **25** |
| `lean` + plan 03 merged | **17** |
| `lean` + readonly + plan 03 | 13 |
| `lean` + debug | **33** (25 + 8; the earlier “26” was an arithmetic error) |

After plan 09 the number that matters is per-server: ~2 knowledge, ~15 device,
~9 debug, ~3 inventory.

---

## Implementation

Registration lives in the FastMCP server module — `rad_mcp/server.py`
**[VERIFIED — path was correct]**. Find how
`RAD_MCP_READONLY` currently skips write tools and extend that mechanism
rather than building a parallel one.

> **[DONE — resulting structure]** shared state/helpers extracted to
> `rad_mcp/runtime.py`, profile resolution in `rad_mcp/profile.py`, one module
> per group under `rad_mcp/tools/` (knowledge, device, snmp, debug, inventory,
> dev, introspection), CLI replacement `rad_mcp/credentials_cli.py` installed
> as **`rad-mcp-set-credentials`**. Server version bumped to 0.9.0. One CLI
> behaviour delta vs the old tool: rotating a key the running server already
> loaded needs a server restart (the CLI is a separate process).

- Gate at **registration time**, not inside tool bodies. An unavailable tool
  must not exist in the session — the guarantee readonly already gives.
- Resolve the profile once at startup into an explicit enabled-name set. Log
  it at INFO and write a session-start record to the audit log.
- **Structure the module so each group is a separate registration function**
  (`register_knowledge_tools(mcp)`, `register_device_tools(mcp)`, …). Plan 09
  then becomes moving functions between packages rather than untangling one
  file. This is the part that makes the next plan cheap — do not skip it.
- Unknown profile value → fail fast, no silent fallback.
- `rad://status` reports profile and flags so a user can see why a tool is
  missing.

## Documentation

- `docs/architecture.md`: replace the stale 18-tool diagram with the group
  table; add a "Context economics" note and link DECOMPOSITION.md.
- `INSTALL.md`: `lean` for new installs, `legacy` for existing; document flags
  and the `set_device_credentials` CLI replacement.

---

## Acceptance criteria

- [x] `legacy` tool list identical to `v0.1.0` — diff two `tools/list`
      responses and prove it *(done — diff is exactly
      `['set_device_credentials']`, the mandated removal; see the corrected
      note above)*
- [x] `lean` registers exactly 25 by default *(verified live)*
- [x] Debug tools absent unless `RAD_MCP_DEBUG_TOOLS=true` *(lean+debug = 33)*
- [x] Inventory writes absent unless explicitly enabled *(lean+inventory = 28)*
- [x] `set_device_credentials` unreachable over MCP in **both** profiles; CLI
      replacement documented and working *(`rad-mcp-set-credentials`)*
- [x] Each group has its own registration function in its own module
      *(`rad_mcp/tools/{knowledge,device,snmp,debug,inventory,dev,introspection}.py`)*
- [x] `rad://status` returns version, profile, flags, corpus build id
- [x] Eval suite green under both profiles *(registration cases in
      `tests/evals/cases/profiles.yaml`; runner grew `--profile` and a
      per-case `profiles:` filter — the one debug-positive safety case is
      tagged `profiles: [legacy]`)*
- [x] No test asserts a hardcoded count of 43 *(grep-verified)*

## Rollback

Unset the env var; default is `legacy`. The credential removal is the one
non-revertible piece — ship the CLI replacement in the same PR.
