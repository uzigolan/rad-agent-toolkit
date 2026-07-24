# Versions

How rad-mcp components are versioned, and what's current. The **live source of
truth** is the `list_versions` MCP tool (returns the server + every skill +
every driver in one call); the server version is additionally reported via MCP
`serverInfo` at the `initialize` handshake (e.g. Claude Code `/mcp`).

**Skill** versions are intentionally NOT copied into this doc — they change
often and would drift; run `list_versions` for the current numbers. What's
below is the server changelog, the driver→product map, and the where-to-bump
rules — the parts that rarely move.

## Current

**Skills** — run `list_versions` (the server's copies) and `check_skill_version`
(your loaded copy) for current values; not hand-listed here, so they can't go
stale. Where they live + the bump policy are below.

**MCP server changelog** (current version is authoritative via `list_versions`):
`0.8.0` server-managed secrets — set_device_credentials write tool for CLI login AND SNMP communities (v2c/v1/v1-CSV/v3 user; server writes its own .env; effective immediately incl. rotation; remote clients never touch server files) · `0.7.0` datasheet layer — 39 product datasheets in the catalog (datasheet_sections + FTS5, family/product/kind classification via datasheet-map.yaml), datasheet_search tool, rad://datasheet resources, /rad-load-datasheet command · `0.6.0` check_skill_version — session drift alert for skill/server version + bundled/served mode · `0.5.1` list_versions reports the knowledge-catalog build · `0.5.0` Phase 5 — CLI refs + manuals + reference docs in the catalog, cli_search/manual_search · `0.4.0` snmp_build_poll_plan + catalog-decoded live values + capability-observation log · `0.3.0` offline knowledge-catalog tools (knowledge_status/mib_search/mib_describe/mib_table/mib_notifications) over rad-knowledge.sqlite · `0.2.0` read-only SNMP tools + pysnmp

**Knowledge catalog:** `rad-knowledge.sqlite` carries `catalog_meta.schema_version` (currently `1`) + a build timestamp + corpus hash; the live view is the `knowledge_catalog` block of `list_versions`. It is a build artifact (gitignored); the build report is committed. Last known build (2026-07-23): cli_help=4367, manual_sections=1546, datasheet_sections=522, mib_objects=0 (pysmi not-run — no MIB roots selected).

| Driver (family) | Version | Product | Live-Verified SW |
|---|---|---|---|
| `secflow` | 1.0 | SecFlow / SF-1p | 6.x.x |
| `etx1p` | 1.0 | ETX-1p | 6.x.x |
| `etx2` | 1.0 | ETX-2 (203AX / 205A / 220A / 2I) | 6.8.5 (1.150) |
| `mp4100` | 1.0 | Megaplex-4100 | Mn 4.91 |
| `mp1` | 1.0 | MP-1 | SW 2.20(0.61) |
| `minid` | 1.0 | MiNID (miniature NID / SFP sleeve) | SW 2.6 |
| `etx2v` | 1.0 | ETX-2V (uCPE-OS chassis platform) | uCPE-OS (719-node CLI tree) |

## MCP tools

All 38 tools shipped with server 0.8.0. The `tool_versions` MCP tool returns
this table live. Version = the server release that introduced or last changed
the tool's behaviour/signature.

| Tool | Version | Notes |
|---|---|---|
| `add_device` | 0.1.0 | |
| `backup_config` | 0.1.0 | |
| `check_skill_version` | 0.6.0 | |
| `cli_help` | 0.1.0 | Live SSH session required |
| `cli_search` | 0.5.0 | Knowledge catalog — CLI layer |
| `commit_config` | 0.1.1 | `confirm=true` mandatory |
| `datasheet_search` | 0.7.0 | Knowledge catalog — datasheet layer |
| `debug_logon_request` | 0.1.1 | ⚠ Explicit user request required |
| `debug_logon_submit` | 0.1.1 | ⚠ Explicit user request required |
| `debug_menu` | 0.1.1 | ⚠ Explicit user request required |
| `debug_shell_command` | 0.1.1 | ⚠ Explicit user request required |
| `debug_tree_history` | 0.1.0 | |
| `enter_debug_shell` | 0.1.1 | ⚠ Explicit user request required |
| `exit_debug_shell` | 0.1.0 | |
| `get_config` | 0.1.0 | |
| `health_check` | 0.1.0 | |
| `knowledge_status` | 0.3.0 | |
| `list_devices` | 0.1.0 | |
| `list_versions` | 0.5.1 | |
| `manual_search` | 0.5.0 | Knowledge catalog — manual layer |
| `mib_describe` | 0.3.0 | Knowledge catalog — MIB layer |
| `mib_notifications` | 0.3.0 | Knowledge catalog — MIB layer |
| `mib_search` | 0.3.0 | Knowledge catalog — MIB layer |
| `mib_table` | 0.3.0 | Knowledge catalog — MIB layer |
| `remove_device` | 0.1.1 | `confirm=true` mandatory |
| `run_demo_device` | 0.1.0 | In-process demo for MCP tool validation |
| `run_show` | 0.1.0 | Whitelisted read-only commands only |
| `run_show_in_context` | 0.1.0 | |
| `save_startup` | 0.1.1 | `confirm=true` mandatory |
| `set_device_credentials` | 0.8.0 | Writes server/.env; CLI + SNMP |
| `snmp_build_poll_plan` | 0.4.1 | |
| `snmp_get` | 0.2.0 | |
| `snmp_probe` | 0.2.0 | |
| `snmp_walk` | 0.2.0 | |
| `stage_config` | 0.1.0 | |
| `stop_demo_device` | 0.1.1 | `remove_from_inventory=true` + `confirm=true` to clean up |
| `test_connectivity` | 0.1.0 | |
| `update_device` | 0.1.0 | |

## Where each version lives (what to bump)

- **Server** — `server/rad_mcp/__init__.py` `__version__`, kept in sync with
  `server/pyproject.toml` and `.claude-plugin/plugin.json` (all three must
  match). Surfaced through `FastMCP(version=...)` → MCP `serverInfo`.
- **Skill** — `skills/<name>/SKILL.md`: the `version:` frontmatter field **and**
  the `> **Skill version:**` line at the top of the body — keep the two equal.
- **Driver** — `server/rad_mcp/drivers/<family>.py`: the `version` class
  attribute **and** the `Driver version:` line in the module docstring.

## Bump policy

- Bump a **skill** on any content change to its `SKILL.md`.
- Bump a **driver** when that family's behavior changes — contexts, health
  sweep, SSH connection profile, dialect quirks — not for doc-only tweaks.
- Bump the **server** on a release (all three server-version locations together).
- Semver-ish: patch = fixes, minor = additive, major = breaking.

## Checking what's actually loaded

- **`list_versions` tool** → server + all skills + all drivers, one call
  (works on every transport, including Claude Desktop).
- **`/mcp`** (or the client's server-info panel) → the server version from the
  handshake.
- **Files** → grep `version:` in `skills/*/SKILL.md`, `version =` in
  `server/rad_mcp/drivers/*.py`.

### Drift check

The versions a running client reports come from its **deployed skill copies**
(`~/.copilot/skills`, `~/.claude/skills`, `~/.agents/skills`, and the Claude
Desktop zip), not from this repo. If those don't match the table above, the
client is on a stale copy — re-run its installer (and rebuild/re-upload the
Desktop zip) to resync.
