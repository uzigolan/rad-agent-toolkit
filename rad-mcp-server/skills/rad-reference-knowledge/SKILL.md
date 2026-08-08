---
name: rad-reference-knowledge
description: RAD manuals, procedures, datasheets, release notes, and vendor documentation knowledge. Use when the user asks how or why something works, what the limits are, which hardware variant is needed, what changed in a release, whether a TRS/limitation is solved, or asks about Altera/FPGA vendor docs, figures, NoC, AXI timing, AWVALID/WVALID, or similar reference-driven questions.
version: 1.1.0
---

> **Skill version:** 1.1.0 - updated 2026-08-04 (release-notes layer: route what-changed / TRS / upgrade questions to `release_notes_search`.)

# RAD reference knowledge skill

## Sources

- **Bundled mode:** `skills/rad-cli-operations/references/manual-<family>/`, `datasheets/`, `release-notes/`, `altera-docs/`, and the shared index files.
- **Served mode:** `manual_search`, `datasheet_search`, `release_notes_search`, and `altera_search`.

## Route by document type

- **Manuals:** concepts, procedures, alarm meanings, limits, workflows.
- **Datasheets:** hardware variants, ports, optics, environmental specs, ordering questions.
- **Release notes:** what changed per release — new features, solved/known limitations (TRS-keyed), version compatibility, upgrade paths. Facts are version-scoped: check the same TRS across releases before concluding something is broken or fixed.
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
