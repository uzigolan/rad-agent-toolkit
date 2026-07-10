---
description: Ingest a RAD device user-manual PDF into the skill's manual layer (per-chapter markdown + CLI-topic cross-links). Also use when addressed via "abayev" / "noam" / "rad agent" — e.g. "noam, load the ETX-1p manual", "rad agent, ingest this PDF for secflow"
argument-hint: <pdf-path> <family>   e.g. manuals/ETX-1p_6.4_Mn_05-26_GA.pdf etx1p
---

Ingest a device user manual into the skill knowledge for: $ARGUMENTS

Parse the arguments: first token is the PDF path, second is the family
(`secflow` | `etx1p` | `etx2`). The manual is a COMPANION to the harvested CLI
reference — it answers concepts / procedures / limits / alarm meanings the `?`
help can't, and NEVER overwrites the CLI reference. Unlike `/rad-harvest`, this
touches NO device — it is pure local PDF → markdown extraction.

1. **Resolve the inputs.**
   - If the PDF path is missing, list `rad-mcp-server/manuals/*.pdf` and ask
     which one; the manual PDFs live in `rad-mcp-server/manuals/` (gitignored).
   - If the family is missing, infer from the PDF name if obvious (e.g.
     "ETX-1p" → `etx1p`) and confirm, else ask. The family MUST match an
     inventory device family so the reference lands beside its CLI reference.
   - **Check whether that family was harvested** — does
     `references/cli-help-<family>.jsonl` exist? If NOT, do not block (manual
     ingest is independent and read-only), but WARN: the manual is designed as
     a companion to the CLI reference, its cross-link table points at CLI
     contexts that won't resolve yet, and the skill's "syntax from the
     reference, meaning from the manual" model is only half-built for this
     family. Recommend `/rad-harvest <device-of-this-family>` first (or right
     after), and proceed only on the user's OK.
   - Ensure the tooling dep is present (first run only): if the script fails
     with `ModuleNotFoundError: fitz`, run
     `rad-mcp-server\server\.venv\Scripts\python.exe -m pip install pymupdf`
     (or `pip install -e "rad-mcp-server/server[tooling]"`) and retry.

2. **Run the ingest** (fast — seconds, local; no background needed):

   ```
   rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\ingest_manual.py <pdf-path> <family>
   ```

   It rewrites `references/manual-<family>/` = one markdown file per manual
   chapter + `manual-index.md` (chapter list + CLI-topic → chapter cross-link
   table). Re-running replaces that directory only.

3. **Sanity-check the output** (extraction quality varies by PDF):
   - Read `manual-index.md`: chapter list looks complete (no whole chapters
     missing), and the CLI-topic cross-link table mapped the key areas (mqtt,
     crypto/pki, router/bgp, ports) to real sections.
   - Grep one high-value chapter (e.g. the security/MQTT chapter) for a known
     term and confirm the text is clean prose, not garbled. RAD PDFs can
     mis-extract tables/screenshots — if a chapter is mostly noise, say so;
     the fix is usually a TOC-boundary tweak in `scripts/ingest_manual.py`.
   - Confirm there is NO mojibake written to the files: grep the dir for the
     byte-garble markers and expect zero hits (PowerShell display through a
     non-UTF-8 codepage can look garbled even when the file is clean — trust
     the Grep tool / a UTF-8 read, not the raw console echo).

4. **Sync the skill copies**: copy
   `rad-mcp-server/skills/rad-cli-operations/references/manual-<family>/` to
   `~/.claude/skills/rad-cli-operations/references/manual-<family>/` (and the
   workspace `.claude/skills/...` copy). Remind the user that Claude Desktop
   needs the skill zip rebuilt (`scripts/build_desktop_skills.py`) and
   re-uploaded, and that the new `rad://manual/<family>` MCP resources go live
   only after a window reload.

5. **Offer to commit** the extracted markdown (the PDF stays gitignored under
   `manuals/`; only `references/manual-<family>/*.md` is committed).

Notes: read-only w.r.t. devices — safe any time, no staged-commit flow needed.
If a newer manual revision arrives, drop it in `manuals/` and re-run; the
chapter dir is rewritten in place and git history tracks the manual's evolution.
