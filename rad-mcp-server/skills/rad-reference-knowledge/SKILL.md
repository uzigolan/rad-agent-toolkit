---
name: rad-reference-knowledge
description: RAD manuals, procedures, datasheets, and vendor documentation knowledge. Use when the user asks how or why something works, what the limits are, which hardware variant is needed, or asks about Altera/FPGA vendor docs, figures, NoC, AXI timing, AWVALID/WVALID, or similar reference-driven questions.
version: 1.0.0
---

> **Skill version:** 1.0.0 - updated 2026-08-04 (split out of `rad-cli-operations` to own manuals, datasheets, and Altera/vendor-document retrieval.)

# RAD reference knowledge skill

## Sources

- **Bundled mode:** `skills/rad-cli-operations/references/manual-<family>/`, `datasheets/`, `altera-docs/`, and the shared index files.
- **Served mode:** `manual_search`, `datasheet_search`, and `altera_search`.

## Route by document type

- **Manuals:** concepts, procedures, alarm meanings, limits, workflows.
- **Datasheets:** hardware variants, ports, optics, environmental specs, ordering questions.
- **Altera/vendor docs:** FPGA behavior, NoC/AXI timing, vendor figures, reset and initialization sequences.

## Altera query budget

- Maximum `altera_search` calls per question: **3**.
- Call 1: one focused normalized query from the user's wording.
- Call 2: doc-filtered follow-up using the top document from call 1 when docs are mixed.
- Call 3: figure-focused follow-up only if figure refs are still missing.
- Do not spray broad one-word probes as independent calls.
- If a high- or medium-confidence hit already includes `figure_refs`, stop searching and answer.

## Hard rules

- Use manuals for `how/why/what does this mean`, not for exact CLI syntax.
- Use datasheets for hardware/product questions, not CLI procedures.
- In bundled mode, do not replace the local reference layer with repository or GitHub search.
- If the user says `stored data only`, stay within these references and do not suggest live checks.
