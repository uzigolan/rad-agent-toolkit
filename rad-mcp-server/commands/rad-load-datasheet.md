---
description: Ingest RAD product-datasheet PDFs into the skill's datasheet layer (per-subject markdown + family/product/kind classification). Also use when addressed via "abayev" / "noam" / "rad agent" — e.g. "noam, load the datasheets", "rad agent, ingest the ETX-2i-10G datasheet"
argument-hint: [--all | <product-or-pdf>]   e.g. --all, or asmi-54c
---

Ingest product datasheet(s) into the skill knowledge for: $ARGUMENTS

Datasheets are the THIRD knowledge domain beside the CLI reference and the
user manuals: hardware specs, interfaces, timing options, ordering and product
variants live here. Syntax -> cli_search; concepts/procedures ->
manual_search; specs/variants/ordering -> datasheet_search. Like
`/rad-load-manual` this touches NO device — pure local PDF -> markdown.

1. **Resolve the inputs.**
   - Datasheet PDFs live in `rad-mcp-server/datasheets/` (the directory and
     its whole content are gitignored; only extracted markdown is committed).
   - Classification is driven by
     `references/datasheet-map.yaml` — one entry per PDF with `product`
     (slug), `family` (inventory family, or `null` for standalone products),
     and `kind` (`system` = standalone device, `card` = plug-in chassis
     module — e.g. every Megaplex-4 card, `accessory`). The classification
     comes from each PDF's own first-page banner, NOT the filename.
   - **New PDF not in the map yet?** Open its first page, read the banner
     ("Data Sheet | <family> | <product> | ..."), add a map entry, then run.
     Set `skip: true` to exclude an entry.
   - If the argument is missing, default to `--all` (the map is the roster).
   - Tooling deps live in the server venv: pymupdf + pyyaml. On
     `ModuleNotFoundError` run
     `rad-mcp-server\server\.venv\Scripts\python.exe -m pip install pymupdf pyyaml`.

2. **Run the ingest** (fast — seconds, local; no background needed):

   ```
   rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\ingest_datasheet.py --all
   ```

   (or pass one product slug / pdf name instead of `--all`.) It rewrites
   `references/datasheets/` = one markdown file per datasheet, split into
   `##` subject sections (features, interfaces, specifications, ordering) by
   font-span heading detection, plus `datasheet-index.md` grouped
   family -> system -> cards.

3. **Sanity-check the output** (extraction quality varies by PDF vintage):
   - Read `datasheet-index.md`: every non-skipped map entry appears; card
     counts look right (mp4100 should list ~19 cards + 1 accessory).
   - Grep one sheet's `^## ` headings: subject names (TIMING, MANAGEMENT,
     ORDERING...), not page-banner noise. Older Word-exported sheets fall
     back to per-page sections — that's expected, not a failure.
   - Confirm NO mojibake: grep the dir for byte-garble markers and expect
     zero hits (trust the Grep tool / a UTF-8 read, not raw console echo).

4. **Rebuild the knowledge catalog** so datasheet_search answers from sqlite:

   ```
   rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\build_knowledge_catalog.py --mib-root "MIBs2:priority=200" --mib-root "MIBS:priority=100"
   ```

   Then verify: `knowledge_status` shows a non-zero `datasheet_sections`
   count, and a `datasheet_search` for e.g. "teleprotection" hits the TP card.

5. **Sync the skill copies**: copy
   `rad-mcp-server/skills/rad-cli-operations/references/datasheets/` (and the
   updated `datasheet-map.yaml`) to `~/.claude/skills/rad-cli-operations/...`
   and the workspace `.claude/skills/...` copy, if those copies exist. Remind
   the user that Claude Desktop needs the skill zip rebuilt
   (`scripts/build_desktop_skills.py`) and re-uploaded, and that the
   `rad://datasheet` MCP resources go live only after a window reload.

6. **Offer to commit** the extracted markdown + map (PDFs stay gitignored
   under `datasheets/`; only `references/datasheets/*.md` and
   `datasheet-map.yaml` are committed).

Notes: read-only w.r.t. devices — safe any time, no staged-commit flow needed.
A newer datasheet revision: drop the PDF in `datasheets/`, update its map
entry's `pdf:` filename, re-run; the markdown is rewritten in place.
