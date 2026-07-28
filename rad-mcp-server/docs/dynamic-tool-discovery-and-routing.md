# Dynamic Tool Discovery and Routing for Terminal-Centric AI Assistants

## Goal

Enable the AI assistant to work safely even when the loaded tools are unknown in advance.
The assistant should discover available tools at runtime, build a temporary capability map, then route user intents to the best available tool chain.

## Core Principles

- Do not hardcode tool names in routing logic.
- Resolve terminal context first, device operations second.
- Treat secrets as references, not chat-visible values.
- Keep write operations behind explicit approval.
- Return matrix-style results for multi-device clarity.

## Two Tool Families

| Family | Owner | Typical Scope | Direct Device Access |
|---|---|---|---|
| App tools | Your application | terminal binding, context, orchestration, compare | Usually no |
| RAD MCP tools | rad-mcp-server | inventory, connectivity, CLI, SNMP, config, debug | Yes |

## Runtime Capability Discovery

### 1) Discover

At chat/session start, fetch all currently loaded tools and metadata.

Preferred pattern:

- If platform supports native tool listing, use that.
- Otherwise provide one app tool, for example `app_list_capabilities`, that returns all tools the chat can invoke.

### 2) Normalize

Convert discovered tools into a common registry schema.

Suggested schema fields:

- `name`
- `provider` (APP or RAD_MCP)
- `intents` (for example: `device_lookup`, `show_config`, `compare`, `snmp_read`, `write_config`)
- `target_type` (`terminal`, `device`, `global`)
- `required_inputs`
- `optional_inputs`
- `sensitivity` (`read`, `write`, `secret`)
- `confidence_rank` (optional numeric preference)

### 3) Plan

For each user request:

- Parse intent and target entities (`terminal A`, `device X`, `A vs B`).
- Select candidate tools by matching `intents`.
- Rank candidates using policy:
  - exact target compatibility first
  - lower sensitivity first
  - APP tools first for context, RAD MCP tools for device execution

### 4) Execute

Execute selected tools in sequence with validation between steps.

Example chain for: "show configuration on terminal A"

1. `app_get_terminal_binding(terminal=A)`
2. `get_config(device=<resolved device>)`
3. response renderer (matrix row)

### 5) Fallback

If a tool is missing or fails:

- try next ranked candidate
- degrade gracefully (partial results)
- explain what was unavailable and what alternative was used

## Intent-to-Tool Mapping (Dynamic)

| User Intent | Preferred Chain | Fallback |
|---|---|---|
| device info for terminal A | `app_get_terminal_device_info` | `app_get_terminal_binding` + `app_get_device_profile` |
| show config on terminal A | `app_get_terminal_binding` + `get_config` | terminal command executor with read-only guard |
| compare A vs B | `app_compare_terminals` | collect snapshots from both + local diff |
| health check | `health_check` | `test_connectivity` + targeted `run_show` |

## Security Policy

- Never expose plaintext passwords, tokens, communities, or SNMPv3 keys in chat.
- Return masked values and `secret_ref` handles instead.
- Require explicit confirmation for write actions.
- Log tool selection and execution (with secret redaction).

## Guest Device Pattern (Session-Only)

For devices not in managed inventory:

- Register as in-memory guest context (TTL-based).
- Mark rows as `guest=true` in output.
- Auto-expire on TTL/session end.
- Do not persist to inventory unless user explicitly requests onboarding.

## Recommended Response Matrix

| Request | Selected Tools | Status | Evidence | Fallback Used |
|---|---|---|---|---|
| show config on terminal A | `app_get_terminal_binding` -> `get_config` | OK | config export succeeded | no |
| compare A vs B | `app_compare_terminals` | DEGRADED | B missing SNMP fields | yes |

## Minimal Implementation Checklist

1. Add capability discovery endpoint (`app_list_capabilities`) if platform does not expose loaded tools directly.
2. Build per-session capability registry with short TTL cache.
3. Implement intent parser + ranking policy.
4. Implement fallback chain execution.
5. Add matrix renderer with status, evidence, and degradation notes.
6. Enforce secret redaction and write approvals.

## Notes for RAD Skills

- Keep RAD domain logic in skills (health-first, staged writes, safe read defaults).
- Do not hardwire exact tool names where possible; rely on intent tags from capability registry.
- Use APP tools first for terminal resolution; use RAD MCP tools for actual network operations.
- If discovery is unavailable, run in conservative mode:
  - ask for explicit target and operation scope
  - execute only validated read paths
  - require extra confirmation before any write path
