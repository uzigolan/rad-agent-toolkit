---
description: Ingest Altera PDF docs into repeatable knowledge artifacts (markdown per document + figure assets + index) for FPGA/bitstream/register reference lookups.
argument-hint: [--input-dir <path>] [--pattern <glob>] [--no-figures]   e.g. --input-dir Altera
---

Ingest Altera documentation for: $ARGUMENTS

This is a local-only, repeatable pipeline similar to manual/datasheet ingest.
It rewrites a normalized Altera reference layer consumed by skill/file lookups
(and served-mode tool lookups once `altera_search` is available).
By default it also extracts embedded PDF figures and links them from markdown.

1. Resolve source input.
   - Default: `Altera/` at workspace root.
   - Accept override via `--input-dir` and optional `--pattern`.

2. Run the ingest script.

   ```
   rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\ingest_altera.py $ARGUMENTS
   ```

3. Validate generated outputs under:
   - `skills/rad-cli-operations/references/altera-docs/*.md`
   - `skills/rad-cli-operations/references/altera-docs/figures/<doc-slug>/*`
   - `skills/rad-cli-operations/references/altera-docs/altera-index.md`

4. Report counts and output path.

5. Offer next step:
   - run an `altera_search` query in served mode, or
   - commit generated artifacts for team reuse.
