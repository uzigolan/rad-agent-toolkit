---
description: Ingest FPGA MEA HTML memory-map files into a reusable knowledge artifact set (per-file JSON + merged index). Use when debug MEA discovery is too manual and you want repeatable stashed knowledge by device/version.
argument-hint: [--input-dir <path>] [--pattern <glob>]   e.g. --input-dir MEA/html_from_zips
---

Ingest FPGA MEA HTML files for: $ARGUMENTS

This is the FPGA-memory-map equivalent of manual/datasheet ingest: local-only,
repeatable, and safe (no device I/O). It normalizes prefixed MEA HTML files
(`...-mem-map__entu_registers.html`, `...-mem-map__entu_tables.html`) into
structured JSON artifacts keyed by device/version/type.

1. Resolve the input source directory.
   - Default: `MEA/html_from_zips` at workspace root.
   - If the user passed `--input-dir`, use that.
   - Validate that the directory exists and contains HTML files.

2. Run the ingest script:

   ```
   rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\ingest_mea.py $ARGUMENTS
   ```

3. Confirm outputs were rewritten under:
   - `skills/rad-cli-operations/references/fpga-mea/raw/*.json`
   - `skills/rad-cli-operations/references/fpga-mea/fpga-mea-index.json`
   - `skills/rad-cli-operations/references/fpga-mea/fpga-mea-index.md`

4. Report counts from script output (files parsed, TOC register entries,
   table rows) and show where the generated artifacts live.

5. Offer next step:
   - wire these artifacts into MCP lookup tools / catalog build, or
   - commit the generated artifacts for team reuse.
