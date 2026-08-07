# Plan 10 — Contribution model

**Branch:** `main` · **Risk:** low · **Requires:** plan 00
**Do before:** external contributors land

---

## Read this first: two different kinds of isolation

The rest of this plan set optimises for **runtime isolation** — blast radius,
what a capability can destroy at execution time. That is why servers split the
way [DECOMPOSITION.md](DECOMPOSITION.md) describes.

**Contribution isolation is a different property**: can a developer change X
without reading, understanding, or fearing Y?

They correlate but are not the same. `rad-debug` and `rad-device` are hard
runtime boundaries yet share drivers, so a driver change still touches both.
Conversely, two family dialects inside one server never interact at all and
are perfectly isolated for contribution purposes despite living together.

Decomposition helps contribution isolation. It does not deliver it. Three more
things do:

1. **Seams with written contracts** — so a contributor knows exactly what they
   may rely on and what they must not change.
2. **CI that tells a stranger they broke something** — because a new
   contributor cannot be expected to know what they broke.
3. **Making the highest-volume contributions data, not code.**

Point 3 matters most and is the least obvious.

---

## Part A — Make the common contribution a data contribution

Project the next hundred contributions. Most will be:

- a new device family or a dialect correction
- a new manual, datasheet, or release-notes set
- a new firmware version harvested for an existing family
- a family skill improvement — a recipe, a caveat, a known issue
- new eval cases

**None of those should require editing shared Python.** Each should be adding
a file that conforms to a contract. When that holds, a contributor needs to
understand one contract and zero relationships, and dozens of people can work
in parallel with no merge contention.

Where the repo does not yet allow this, fix it:

### A1. Driver registry instead of a dispatch table

If adding a family means editing a central `if family == ...` map or a
registry list, that file becomes a merge-conflict choke point and a
read-the-whole-system requirement.

Replace with discovery: `rad_core/drivers/<family>.py` declaring its own
`FAMILY`, prompt patterns, dialect quirks, and read whitelist additions,
auto-discovered at import. Adding a family = adding one file. **Nothing
existing is edited.**

Same pattern for ingest modules in `rad-forge`: `sources/<source_type>.py`
conforming to the corpus contract, discovered rather than registered.

### A2. Corpus contributions are files plus a validator

[Plan 08](08-ingestion-and-corpus-contract.md) already makes corpus writes
PR-based and contract-checked. That is the contribution model for all
knowledge work: submit rows, `forge_validate` judges them, a human merges.
A contributor adding release notes for one family never reads a line of
server code.

### A3. Skills are markdown

Already true, and worth protecting. A family skill contribution should require
no Python knowledge. Per [plan 04](04-mcp-served-skills.md) skills are
packaged per server; make sure a contributor can add a family skill without
touching the loader.

---

## Part B — Ownership and locks

### B1. `CODEOWNERS`

Not bureaucracy — it is how a contributor discovers, without asking, which
parts are open and which need a conversation.

```
# Open — normal review
/rad-mcp-server/rad_core/drivers/      @family-maintainers
/rad-mcp-server/skills/                @knowledge-maintainers
/rad-mcp-server/references/            @knowledge-maintainers
/rad-mcp-server/tests/evals/cases/     @everyone

# Locked — requires maintainer approval, no exceptions
/rad-mcp-server/rad_core/safety/       @uzigolan
/rad-mcp-server/rad_core/whitelist*    @uzigolan
/rad-mcp-server/rad_core/audit*        @uzigolan
/rad-mcp-server/docs/corpus-contract.md  @uzigolan
/rad-mcp-server/docs/plan/               @uzigolan
```

### B2. The safety model needs a hard lock, and this is now urgent

With one maintainer, the staged-commit flow and the read whitelist were
protected by the fact that one person wrote everything. With many contributors
they become an **accident surface** — nobody has to be malicious for a
whitelist entry to get widened by someone fixing a legitimate bug.

Consolidate every safety-critical decision into a small, clearly-named module
(`rad_core/safety/`), lock it in CODEOWNERS, and add a CI check that flags any
PR touching it with a required-review label. Small and obvious beats scattered
and implicit.

Same reasoning applies to the corpus: [plan 08](08-ingestion-and-corpus-contract.md)'s
PR-only rule was written against an attacker. With many contributors the more
likely event is an honest bad harvest. The mechanism is the same; the
probability just went up a lot.

---

## Part C — CI that speaks to strangers

A new contributor cannot know what they broke. CI must tell them.

- **Contract tests at every seam.** Driver interface, ingest-source interface,
  skill frontmatter schema, corpus contract. A contributor who violates a seam
  gets a specific failure naming the contract, not a mysterious downstream
  error.
- **Eval cases are part of the definition of done.** A PR adding a family adds
  family eval cases; a PR adding a corpus source adds retrieval cases. Enforce
  in the PR template.
- **Safety evals are non-negotiable and named as such.** When
  `tests/evals/cases/safety.yaml` fails, the CI output must say plainly that
  this is a blocking safety regression, not a flaky test to retry.
- **Per-area test selection.** A driver-only PR should not require the full
  suite to pass locally. Make it obvious which subset applies.

---

## Part D — What to actually have ready before contributors arrive

Realistically, plan 09 will not be done. That is fine — do not rush it, and do
not let contributors land in the middle of a package extraction. What is
needed first:

**Must have:**

1. Plan 00 in full. **The eval harness is the single highest-value item here** —
   it is what lets an unfamiliar contributor's PR be judged without the
   maintainer reading every line.
2. `CONTRIBUTING.md` (see companion file) with a contribution-type router.
3. `CODEOWNERS` with the safety lock.
4. Plan 01's **registration-function refactor** — one module per capability
   group. Even before servers split, this is what lets people work in separate
   files without conflicts.

**Strongly wanted:**

5. Driver registry (A1). Without it, every family contribution collides in one
   file.
6. `docs/corpus-contract.md` from plan 08, even if `rad-forge` extraction
   lags. The contract is what contributors need; the package move can wait.

**Explicitly defer:**

- Plans 05 and 09. Do not run a package extraction while onboarding people —
  every open PR would need rebasing across a moved tree.

---

## Part E — Sequence contributor-facing work to avoid collisions

Order matters when many people arrive at once:

- Announce plan 09 as **planned but not started**, with the target topology
  visible in `DECOMPOSITION.md`. Contributors can then place their work
  correctly even though the packages haven't moved.
- Freeze `rad_core` interfaces before contributors arrive. Interface churn
  under many open PRs is the most expensive failure mode available.
- Land plans 01–04 yourself, not via contributors. They are structural and
  cross-cutting — exactly the work that does not parallelise.
- Route contributors to families, corpora, skills, and evals. That is where
  parallelism is real and where the project genuinely needs volume.

---

## Acceptance criteria

- [ ] Adding a device family requires adding one file and editing none
- [ ] Adding an ingest source requires adding one file and editing none
- [ ] Adding a family skill requires no Python
- [ ] `CODEOWNERS` in place; safety paths locked
- [ ] Safety-critical logic consolidated in one clearly-named module
- [ ] Contract tests exist for driver, ingest-source, skill, and corpus seams
- [ ] `CONTRIBUTING.md` routes by contribution type
- [ ] PR template requires eval cases for new families and sources
- [ ] A contributor can add a family, run the relevant evals, and open a PR
      **without reading any server code** — walk it through with one person
      before the others arrive
