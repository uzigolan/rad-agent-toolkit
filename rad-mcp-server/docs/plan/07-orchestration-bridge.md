# Plan 07 — Orchestration bridge

**Branch:** `feat/langgraph-bridge` · **Risk:** low · **Requires:** plan 00

This plan is as much organisational as technical. Read the "Why" fully before
writing code.

---

## Why

The roadmap includes a RADview northbound backend for fleet-scale operations.
At fleet scale the toolkit hits a class of problem MCP deliberately does not
solve:

- **Durability.** "Check firmware compliance across 40 units and stage
  upgrades" fails at device 27. Today you restart from zero.
- **Checkpointed state.** Partial results across a long run need to survive a
  process restart.
- **Human-in-the-loop as a first-class interrupt.** The stage → approve →
  commit gate currently lives in a conversation. For unattended batch work it
  needs to be a durable pause that a human resolves hours later.
- **Traceable branching** for compliance work where every conditional path must
  be auditable.

That is orchestration-framework territory — LangGraph models workflows as
directed graphs with persistent state and checkpointing to resume after
interruption, and is positioned for exactly the enterprise-automation case
where every branch must be traceable.

**The organisational half.** Colleagues building app-only with LangChain are
not on an older pattern; they are solving a different layer. Separation of
concerns — agent logic in the framework, tooling logic in MCP servers, with
tools versioned and audited independently — is the standard argument for the
split, and it is the argument that makes rad-mcp *their* infrastructure rather
than a competing project. A working adapter in the repo converts an
architectural debate into an integration.

---

## Design

### What this plan is NOT

Not a rewrite. Not a dependency. LangChain must never appear in the server's
runtime requirements. The MCP server stays framework-agnostic — that is its
value.

### Deliverable: `examples/orchestration/`

A standalone, separately-installed example directory with its own
`requirements.txt`.

**1. `fleet_compliance.py`** — a LangGraph graph that:

- reads inventory via the MCP connection
- fans out a read-only compliance check per device
- checkpoints after each device (SQLite checkpointer is fine)
- collects drift into a report
- **interrupts** before any staged change, surfacing the preview for human
  approval
- resumes from checkpoint after a kill -9 mid-run

That last point is the whole demonstration. Make the README show it: run,
kill, resume, correct result.

**2. `README.md`** stating the layer split plainly:

```
capability layer   rad-knowledge   corpus retrieval, no hardware
                   rad-device      live ops, staged writes, audit
                   rad-debug       root access, opt-in
                   rad-inventory   registry
                             shared, versioned, framework-agnostic
orchestration      LangGraph / your framework of choice
                             state, retries, checkpoints, approval gates
application        your app / Claude Code / Desktop / Copilot
```

And the reciprocal point: interactive single-device work does not need a graph
— a client speaking MCP directly is simpler and faster. Say so. The document is
more persuasive if it declines to oversell.

**3. `docs/integration-guide.md`** — connecting any MCP-capable framework to
rad-mcp over both stdio and the authenticated HTTP endpoint, including token
scope selection (`RAD_MCP_TOKENS` read-only vs `RAD_MCP_WRITE_TOKENS`).

### Safety in orchestrated mode

Batch and unattended operation is where the safety model is most likely to be
quietly eroded. State explicitly in the example README:

- Automated approval of staged commits is **out of scope and unsupported**.
  The interrupt exists to reach a human, not to be auto-resolved.
- Fleet runs should use a read-only token by default.
- The example ships read-only; the staging path is demonstrated but the commit
  step is left as an explicit human action.
- Every device call still lands in `audit.jsonl` — orchestration does not
  bypass the server, it drives it.

---

## Acceptance criteria

- [ ] `examples/orchestration/` runs against demo devices with no lab hardware
- [ ] Kill mid-run, resume from checkpoint, correct final result — documented
      with commands in the README
- [ ] Interrupt surfaces a human-readable staged preview
- [ ] Zero new dependencies in any server package (`pip install rad-device`
      must not pull LangChain — verify it)
- [ ] Example connects to `rad-knowledge` and `rad-device` as separate servers,
      demonstrating that decomposition costs the orchestrator nothing
- [ ] Integration guide covers stdio and HTTP with token scopes
- [ ] Safety-in-batch section present and explicit
- [ ] Linked from the root `README.md` so colleagues actually find it

## Rollback

Delete the directory. Nothing in the server depends on it.
