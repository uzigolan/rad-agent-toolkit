---
description: Ingest a RAD release-note PDF into the skill's release-notes layer (version-scoped, one record per item, TRS-keyed solved/known limitations). Also use when addressed via "abayev" / "noam" / "rad agent" — e.g. "noam, load the RADview 7.2.3 release notes", "rad agent, ingest this RN"
argument-hint: <pdf> --product <slug> --product-kind <nms|device> [--family <fam>] --version <ver> [--doc-rev <rev>]
---

Ingest a release-note document into the skill knowledge for: $ARGUMENTS

Release notes are the FOURTH knowledge domain (CLI reference = syntax,
manuals = concepts/procedures, datasheets = hardware specs). Their facts are
VERSION-SCOPED: features, solved limitations, new/known limitations,
compatibility matrices and upgrade paths — all pinned to one release, with
solved/known items keyed by TRS tracking numbers (the cross-release join
key that answers "was this fixed, and in which version?"). Like the other
load commands this touches NO device — pure local PDF -> jsonl.

1. **Resolve the inputs.**
   - Release-note PDFs live in `rad-mcp-server/release-notes/` (directory and
     content gitignored; only the extracted jsonl is committed).
   - Two product axes share the schema — pass the right one:
     - NMS release notes (RADview service packs): `--product radview
       --product-kind nms` (no family).
     - Device firmware release notes: `--product-kind device --family <fam>`
       (e.g. `--product etx2 --family etx2`).
   - `--version` is the release the document describes (e.g. `7.2.3`);
     `--doc-rev` is the document revision from the title page (e.g. `v6e`).
     Product/kind/version are auto-guessed from page 1 when possible, but
     pass them explicitly — the guess is best-effort.
   - Tooling dep: pymupdf in the server venv. On `ModuleNotFoundError` run
     `rad-mcp-server\server\.venv\Scripts\python.exe -m pip install pymupdf`.

2. **Run the ingest** (fast — seconds, local):

   ```
   rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\ingest_release_notes.py "RADview_SP_7.2.3.pdf" --product radview --product-kind nms --version 7.2.3 --doc-rev v6e
   ```

   It writes `references/release-notes/rn-<product>-<version>.jsonl` (first
   record = doc meta, then one record per item) and rebuilds
   `release-notes-index.md`.

3. **REVIEW the jsonl — mandatory, the parser is document-vintage sensitive.**
   - The ingest prints per-section counts (`solved=N, known=N, feature=N...`)
     and the TRS-keyed total. Compare against the PDF's own tables: the
     solved-limitations table row count should roughly match `solved=N`.
   - Spot-check a few records: solved/known items should each carry a
     `"trs": "TRS-NNNNN"` and a body that reads like one table row, not a
     page dump. Section-level fallback records titled `"<section> notes"`
     are the degraded path — a few are fine, but if EVERYTHING fell back,
     table detection missed and the parser needs a look before committing.
   - Wrong section labels (e.g. new-known rows classified `solved`) mean a
     heading regex in `HEADING_MAP` needs this vintage's wording added.

4. **Rebuild the knowledge catalog** so release_notes_search answers from sqlite:

   ```
   rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\build_knowledge_catalog.py --mib-root "MIBs2:priority=200" --mib-root "MIBS:priority=100"
   ```

   Then verify: `knowledge_status` shows a non-zero `release_notes` count,
   `release_notes_search` with a TRS number from the doc returns that row,
   and a topic query (e.g. "upgrade") filtered to the product/version hits.
