# Changelog

All notable changes to rad-agent-toolkit are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `CHANGELOG.md` (this file) and the `1.0.0` baseline tag (plan 00).
- Offline eval harness at `rad-mcp-server/tests/evals/` — safety, knowledge,
  and per-family tool-selection cases with an offline-first runner (plan 00).
- CI workflow `.github/workflows/evals.yml` running the eval suite on PR and
  push to `main` (plan 00).
- Harvested/ingested reference artifacts marked `linguist-generated` in
  `.gitattributes` so reviews collapse them and rebases don't fight
  regeneration (plan 00).
- Implementation plan set at `rad-mcp-server/docs/plan/` (plans 00–12,
  DECOMPOSITION, GLOSSARY).

### Considered and deferred
- `merge=ours` for harvested reference files — rejected for now: it silently
  discards incoming changes. Revisit only with a documented decision
  (plan 00, task 2).

## [1.0.0] - 2026-08-07

Baseline release. Tag `1.0.0` marks the state against which all plan-driven
structural changes are measured.

### Features at baseline
- **MCP server** (`rad-mcp` 0.8.0, FastMCP) exposing 43 tools: device CLI
  operations, staged config writes, SNMP, MIB lookup, knowledge search,
  inventory management, debug tree access, and demo-device fixtures.
- **Seven device families verified live**: `secflow`, `etx1p`, `etx2`,
  `mp4100`, `mp1`, `minid`, `etx2v` — each with a harvested `?`-help CLI
  reference, command tree, and family driver (CLI dialect).
- **Safety model**: staged commits (`stage_config` → human review →
  `commit_config` with `confirm=true`), read whitelist, pre-commit backup,
  append-only `audit.jsonl`, `RAD_MCP_READONLY` mode, debug tree only on
  explicit request.
- **Transports**: stdio (local) and HTTP (internal network) with bearer-token
  auth; write tools registered over HTTP only when write-scoped tokens exist,
  optional native TLS.
- **Knowledge corpus**: harvested CLI help (JSONL + rendered markdown),
  ingested manuals and datasheets per family, MIB/OID catalog, MEA/FPGA
  reference, Altera docs, SQLite FTS5 search.
- **Skills**: `rad-core`, `rad-cli-operations` (router), `rad-cli-reference`,
  `rad-snmp-operations`, `rad-mea-debug`, `rad-reference-knowledge`,
  `rad-device-mng`, distributed via local install, desktop zips, and portable
  bundle.
- **Slash commands**: `/rad-health`, `/rad-backup`, `/rad-harvest`,
  `/rad-onboard-family`, `/rad-load-manual`, `/rad-load-datasheet`,
  `/rad-load-mea`, `/rad-load-altera`.
- **Installers** for Claude Code, Claude Desktop, GitHub Copilot, and OpenAI
  Codex.

[Unreleased]: https://github.com/uzigolan/rad-agent-toolkit/compare/1.0.0...HEAD
[1.0.0]: https://github.com/uzigolan/rad-agent-toolkit/releases/tag/1.0.0
