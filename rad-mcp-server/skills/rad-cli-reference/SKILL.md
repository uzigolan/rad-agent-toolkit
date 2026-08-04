---
name: rad-cli-reference
description: Exact RAD CLI syntax and context lookup for ETX/SecFlow/Megaplex/MiNID/ETX-2V families. Use when the user asks for a command, context path, `show` syntax, argument form, capability on a specific family, or a paste-ready CLI sequence.
version: 1.0.0
---

> **Skill version:** 1.0.0 - updated 2026-08-04 (split out of `rad-cli-operations` to own exact CLI syntax and capability grounding.)

# RAD CLI reference skill

Use this skill for exact command answers. It is not the safety layer; `rad-core` still governs whether shown commands may be executed.

## Sources

- **Bundled mode:** `skills/rad-cli-operations/references/cli-reference-<family>.md`, `command-tree-<family>.md`, and `manual-<family>/`.
- **Served mode:** `cli_search` for syntax, `manual_search` for concepts/procedures, `cli_help` only when the references are inconclusive or firmware drift must be checked live.

## Lookup order

1. Determine the family first. CLI syntax is family-specific.
2. For an exact command or context question, use the CLI reference first.
3. For `does family X support Y`, ground it in that family's own CLI reference and manual. Do not generalize from another family.
4. Use the manual for `what does this mean`, `how do I`, `what are the limits`, or multi-step workflows.
5. Use live `cli_help` only when the stored references are genuinely inconclusive and the user is not in offline-only mode.

## Hard rules

- The CLI is context-based. A command often exists only under its context header such as `## configure system`.
- Root `show` assumptions are often wrong. If the reference shows the command under a context, answer with that context.
- Parameterized contexts are harvested under a `NAME` placeholder. Keep that placeholder unless the user provided a real instance.
- A manual keyword hit is not proof of support. Read it in context and confirm the family's CLI reference also supports the feature.
- When showing a sequence, return a paste-ready block and mention the starting context.

## Escalation boundary

- If the question shifts to MEA/debug menus, hand off to `rad-mea-debug`.
- If it shifts to OIDs/MIBs/traps, hand off to `rad-snmp-operations`.
- If it shifts to datasheets or Altera/vendor manuals, hand off to `rad-reference-knowledge`.
