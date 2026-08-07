# rad-agent-toolkit — implementation plans

Target location in repo: `rad-mcp-server/docs/plan/`

Written **for an AI coding agent** (Claude Code, Copilot, Codex) implementing
changes to `uzigolan/rad-agent-toolkit`. Each plan is self-contained: read one
plan, do that work, stop.

**New to the vocabulary?** [GLOSSARY.md](GLOSSARY.md) defines every term of
art used across these plans, with a note on what each means specifically here.

**Read [DECOMPOSITION.md](DECOMPOSITION.md) first.** It defines the target
topology every plan moves toward. A plan read without it will look like a
collection of local optimisations; it isn't.

---

## READ THIS FIRST — rules that apply to every plan

### 1. These plans were written without repository access

Authored from `README.md`, `docs/architecture.md`, and the live tool surface
of a running `rad-mcp` server. Paths and names are marked:

- **[VERIFIED]** — observed directly. Treat as fact.
- **[ASSUMED]** — inferred. **Locate the real thing before editing.** If it
  doesn't exist, find the real equivalent and correct the plan file in the
  same commit.

Never create a file at an [ASSUMED] path because the plan names it.

### 2. One plan, one branch, one PR

Never combine plans. Never open two structural branches at once. If a plan
requires a change belonging to another plan, **stop and report** — do not
scope-creep across the boundary.

### 3. Never break a verified device family

Seven verified live: `secflow`, `etx1p`, `etx2`, `mp4100`, `mp1`, `minid`,
`etx2v`. You have no lab hardware. Therefore:

- Never change driver dialect logic, prompt handling, or read termination as a
  side effect. If a plan seems to require it, stop and report.
- Anything that could alter device I/O ships behind a flag defaulting to
  current behaviour.

### 4. The safety model is not refactorable

Staged commits (`stage_config` → human review → `commit_config` with
`confirm=true`), read whitelist, pre-commit backup, append-only audit. You may
add. You may not simplify, bypass, or "clean up." A change that makes a write
easier to perform needs a human decision, not an agent's.

### 5. Additive first, destructive later

New thing alongside old → old marked deprecated in its description → old
removed in a **separate, later** PR. Never in one step.

### 6. Capability in the server, mechanism in the core

Once packages split, `rad_core` knows *how*; the server decides *whether*. If
you are adding a permission check to `rad_core`, the capability is in the
wrong package.

### 7. Definition of done

The plan's own **Acceptance criteria** pass **and** `tests/evals/` is green.
If plan 00 hasn't merged, do plan 00 first.

---

## Execution order

| # | Plan | Branch | Risk |
|---|------|--------|------|
| 00 | [Baseline & guardrails](00-baseline-and-guardrails.md) | `main` | none |
| 01 | [Capability grouping](01-capability-grouping.md) | `main` (flagged) | low |
| 02 | [Untrusted device output](02-untrusted-output.md) | `main` | low |
| 06 | [MCP prompts](06-mcp-prompts.md) | `main` | none |
| — | **tag `v0.2.0`** | | |
| 08 | [Ingestion split & corpus contract](08-ingestion-and-corpus-contract.md) | `feat/rad-forge` | medium |
| 03 | [Knowledge search facade](03-knowledge-search-facade.md) | `feat/knowledge-search-facade` | medium |
| 04 | [MCP-served skills](04-mcp-served-skills.md) | `feat/mcp-served-skills` | medium |
| — | **tag `v0.3.0`** | | |
| 09 | [Server extraction](09-server-extraction.md) | one per server | medium |
| 11 | [Figures & images](11-figures-and-images.md) | `feat/corpus-figures` | low–med |
| 12 | [Feedback & improvement loop](12-feedback-loop.md) | `feat/feedback-loop` | medium |
| 05 | [Code execution mode](05-code-execution.md) | `feat/code-execution` | **high** |
| 07 | [Orchestration bridge](07-orchestration-bridge.md) | `feat/langgraph-bridge` | low |

**Out of band:** [plan 10 — Contribution model](10-contribution-model.md) and
[CONTRIBUTING-draft.md](CONTRIBUTING-draft.md). Do these *before* external
contributors arrive, regardless of where the sequence above has reached.

**Plan 08 moved ahead of 03 and 04.** The corpus contract is cheapest before
release notes and YANG land, and both 03 and 04 are easier once the corpus is
version-keyed with provenance. Every month it waits, it costs more.

Plan 05 moved after 09 — code execution should be built against the final
`rad-device` boundary, not the combined server.

---

## Why these changes

The knowledge architecture is strong: layered cheap-to-exact retrieval,
harvest diffs as firmware history, deliberate deferral of vector RAG. The gaps
are in **context economics**, **trust boundaries**, and **growth shape**.

1. **43 tools** on one server. Guidance puts the working ceiling near 20,
   degrading past 10. Eight of the 43 are root-access debug tools present in
   every ordinary session.
2. **Skills distributed by copying files to four locations.** HTTP transport
   now exists, so remote clients get tools with **no skill-side safety layer** —
   half the documented defense in depth is absent for those users.
3. **Device-returned text enters context as trusted input.** The safety model
   governs what is *sent*, not what is *believed*.
4. **Multi-step work costs one model turn per round-trip.**
5. **Ingestion and runtime are fused.** A build system living inside a runtime,
   where every new knowledge source grows the runtime tool surface.

Point 5 is the one that compounds. Release notes and NETCONF/YANG are already
queued; the decomposition is what makes them cost one enum value each instead
of a new tool, a new skill section, and a larger context bill for every user.
