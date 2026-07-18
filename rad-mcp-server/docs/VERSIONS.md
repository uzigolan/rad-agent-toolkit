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
`0.6.0` check_skill_version — session drift alert for skill/server version + bundled/served mode · `0.5.1` list_versions reports the knowledge-catalog build · `0.5.0` Phase 5 — CLI refs + manuals + reference docs in the catalog, cli_search/manual_search · `0.4.0` snmp_build_poll_plan + catalog-decoded live values + capability-observation log · `0.3.0` offline knowledge-catalog tools (knowledge_status/mib_search/mib_describe/mib_table/mib_notifications) over rad-knowledge.sqlite · `0.2.0` read-only SNMP tools + pysnmp

**Knowledge catalog:** `rad-knowledge.sqlite` carries `catalog_meta.schema_version` (currently `1`) + a build timestamp + corpus hash; the live view is the `knowledge_catalog` block of `list_versions`. It is a build artifact (gitignored); the build report is committed.

| Driver (family) | Version | Product |
|---|---|---|
| `secflow` | 1.0 | SecFlow / SF-1p |
| `etx1p` | 1.0 | ETX-1p |
| `etx2` | 1.0 | ETX-2 (203AX / 205A / 220A / 2I) |
| `mp4100` | 1.0 | Megaplex-4100 |
| `mp1` | 1.0 | MP-1 |
| `minid` | 1.0 | MiNID (miniature NID / SFP sleeve) |
| `etx2v` | 1.0 | ETX-2V (uCPE-OS chassis platform) |

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
