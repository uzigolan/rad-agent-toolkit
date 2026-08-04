# Altera reference knowledge guide

This document defines how Altera documentation is used in the toolkit,
which prompts work best, and how it differs from CLI/manual/device flows.

## Scope

Altera knowledge in this toolkit is document-grounded reference retrieval for:

1. FPGA architecture concepts.
2. bus/interface behavior (for example AWVALID or WVALID timing context).
3. figure-oriented explanations where the answer should cite a specific
   figure or section.

It is not a live device command surface by itself.

## Data sources

1. Ingested Altera markdown artifacts under:
   `skills/rad-cli-operations/references/altera-docs/`.
2. Figure assets extracted during ingest under:
   `skills/rad-cli-operations/references/altera-docs/figures/`.
3. Served-mode access through MCP tool calls instead of skill-side reference
   folders.

## Primary tool

Use `altera_search` for Altera questions.

Typical fit:

1. "explain AWVALID and WVALID timing expectations".
2. "show the relevant figure for NoC write-path behavior".
3. "compare two Altera concepts and cite where each appears".

## Prompt patterns

Use prompts that request both concept and evidence:

1. "In Altera docs explain AWVALID/WVALID timing and cite the relevant figure."
2. "Find the section and figure that explains NoC write acceptance behavior."
3. "Summarize the Altera flow for this topic and include source references."

## Mode behavior

1. Bundled or embedded mode:
- local references are available from installed skill assets.

2. Served mode:
- skills are thin (SKILL.md only).
- references directories are stripped during install/package.
- Altera knowledge must come from MCP-side `altera_search` responses.

## Boundaries

1. Do not use Altera docs as a substitute for exact RAD CLI syntax.
2. Use `rad-cli-reference` plus CLI sources for command syntax questions.
3. Use Altera docs for architecture and vendor-reference reasoning.
