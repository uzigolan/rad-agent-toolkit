# MEA knowledge and debug guide

This document defines where MEA data lives, which tool to use for each MEA
question type, and how bundled versus served mode changes data access.

## MEA has three distinct stores

1. Command catalog store (static list)
- Purpose: "list all commands", "MEA util fctl", command-family lookup.
- Tool: `mea_commands_search`.
- Typical source file: `MEA/mea_commands_only_with_relation 1.txt`.
- Code entry point: `server/rad_mcp/knowledge.py` (`mea_commands_search`).

2. Captured debug-tree history store (session evidence)
- Purpose: "what was captured under debug mea", menu path history,
  session-derived hidden command trails.
- Tool: `debug_tree_history`.
- Source files: `skills/rad-cli-operations/references/debug-tree-<family>.jsonl`.
- Code entry point: `server/rad_mcp/debug_tree_log.py`.

3. FPGA register and memory-map store (ingested artifacts)
- Purpose: register names, addresses, blocks, memory-map symbols,
  FPGA table rows.
- Tool: `mea_search`.
- Source files: `skills/rad-cli-operations/references/fpga-mea/raw/*.json`.
- Code entry point: `server/rad_mcp/knowledge.py` (`mea_search`).

## Routing rules

Use one primary MEA store first:

1. "all MEA commands" or command-family ask -> `mea_commands_search`.
2. "captured debug path/menu" ask -> `debug_tree_history`.
3. register/address/memory-map ask -> `mea_search`.

Then cross-check only when needed:

1. command from catalog -> confirm captured path via `debug_tree_history`.
2. captured menu reference to register area -> enrich with `mea_search`.

## Combined questions

For combined prompts (commands plus registers plus live debug intent), answer
in this order:

1. command inventory from `mea_commands_search`.
2. register evidence from `mea_search`.
3. optional live debug actions only if user explicitly asks to run on device,
   using the debug tools under `server/rad_mcp/server.py`.

## Knowledge modes and install behavior

1. Bundled or embedded mode:
- skill reference directories are shipped.
- MEA references are available locally from skill assets.

2. Served mode:
- skills are thin (SKILL.md only).
- references directories are stripped during install/package.
- MEA answers must come from MCP-side knowledge tools and MCP-accessible
  sources, not from client-side skill reference folders.

## Refreshing MEA data

1. Register/map artifacts:
- Run `python scripts/ingest_mea.py`.

2. Command catalog file:
- Update the MEA command-catalog text file in expected locations.
- Validate by running a small `mea_commands_search` query.

3. Captured debug history:
- Produced automatically by debug menu operations and written per family.
