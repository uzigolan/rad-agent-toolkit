# Contributing to rad-agent-toolkit

Welcome. This project controls real network equipment and maintains a
knowledge corpus that shapes how AI agents answer questions about RAD devices.
Both facts shape how we work — please read the section that matches what you
want to do, and only that section.

---

## Start here: what are you contributing?

| I want to… | Go to | Do I need to read server code? |
|---|---|---|
| Add or fix a **device family / dialect** | [§1](#1-device-families) | No |
| Add **manuals, datasheets, release notes** | [§2](#2-knowledge-corpus) | No |
| Harvest a **new firmware version** | [§2](#2-knowledge-corpus) | No |
| Improve a **skill** (recipes, caveats, method) | [§3](#3-skills) | No |
| Add **eval cases** | [§4](#4-evals) | No |
| Change **server tools or core code** | [§5](#5-server-code) | Yes |
| Change anything under `rad_core/safety/` | [§6](#6-safety-critical) | **Talk to us first** |

If your change spans two sections, it is probably two pull requests.

---

## Ground rules (all contributions)

1. **One concern per PR.** Easier to review, easier to revert.
2. **Never widen a whitelist or weaken a safety check as a side effect** of
   fixing something else. If your fix seems to require it, stop and open an
   issue instead — see §6.
3. **Add eval cases for what you add.** A new family, a new corpus source, or
   a new tool without eval cases will not be merged.
4. **Assume no lab hardware.** CI runs offline against recorded fixtures.
   Everything you contribute must be testable that way.
5. **Provenance over guesswork.** If you are not certain a command exists on a
   family, do not add it. An empty corpus is recoverable; a wrong one is worse
   than nothing, because agents cite it confidently.

---

## 1. Device families

Adding a family or fixing a dialect means **adding one file**. You do not edit
any registry, dispatch table, or existing driver.

```
rad_core/drivers/<family>.py
```

Declare the family name, prompt patterns, context navigation, dialect quirks,
and any read-whitelist additions. The driver contract is documented in
`docs/driver-contract.md`, and `tests/contracts/test_driver.py` will tell you
precisely what you got wrong.

**Read-whitelist additions are reviewed carefully.** Adding a read command is
normal and welcome; adding anything that changes device state is not a driver
change — see §6.

Required with your PR:

- 5 eval cases in `tests/evals/cases/<family>.yaml`
- recorded fixtures so CI can run without hardware
- a note in the PR describing which device and firmware version you verified
  against, if any

**Do not assume commands port across families.** That assumption is the single
most common source of bad output in this project.

---

## 2. Knowledge corpus

Manuals, datasheets, MIBs, release notes, harvested CLI trees, MEA data.

All corpus contributions go through `rad-forge` and are validated against
`docs/corpus-contract.md`. You submit rows; `forge_validate` judges them; a
maintainer merges. You never write the corpus directly and never edit server
code.

Non-negotiables from the contract:

- Every row carries full **provenance**: source type, family, firmware
  version, document identity, ingest version.
- The corpus is keyed on **(family, firmware_version)**. A new firmware
  version is an *addition*, never an overwrite of an existing one.
- When sources disagree, **record the conflict**. Do not pick a winner and do
  not delete the losing row. Conflicts are useful; silent resolution is not.
- **MEA content is gated.** It carries root-level debug material and is only
  searchable with debug scope. Do not add MEA rows to a general corpus.

Release notes have their own handling: they are keyed as a delta
(`from_version → to_version`), their known-issues sections are extracted as a
separate retrievable class, and they are cross-validated against the harvest
diff. Read the release-notes section of the corpus contract before starting.

**Harvesting** creates and rolls back temporary objects on live hardware.
Never harvest against a production device you do not own. Cleanup verification
must pass or the run produces no rows.

---

## 3. Skills

Skills are markdown. No Python required.

Skills teach *method* — when to search versus verify live, how to sequence a
safe change, what a family's caveats are. They are not a place to duplicate
server enforcement.

- Family recipes and caveats: very welcome, this is where volume helps most.
- Frontmatter must include `version` and `families`; CI validates the schema.
- Keep bodies tight. Skill content loads into a live context window; a
  3,000-token addition has a real cost on every session that uses it.
- **Never write a skill instruction that relaxes a server-enforced rule.** The
  two layers must agree. If you think a rule is wrong, open an issue.

---

## 4. Evals

The easiest high-value contribution, and always welcome as a standalone PR.

`tests/evals/cases/` — YAML cases asserting which tool the agent picks, with
which arguments, and which tools it must *not* call. Format and examples are
in `tests/evals/README.md`.

Especially wanted:

- cases with `device_io: forbidden` — questions the corpus should answer with
  no device round-trip at all
- family-specific cases for families you know well
- cases that assert correct behaviour *succeeds*, not only that bad behaviour
  is blocked. Over-blocking is a real failure mode and under-tested.

Safety cases in `safety.yaml` are treated as a protected suite. Adding cases
there is welcome; changing or removing existing ones needs maintainer review.

---

## 5. Server code

Tools, transport, session handling, retrieval, ingestion.

Read `docs/architecture.md` and `docs/plan/DECOMPOSITION.md` first — the
latter describes the target topology the project is moving toward, so new work
can be placed correctly even before the packages are split.

- Capability groups live in separate registration modules. Add tools to the
  right group; if it is not obvious which, ask before writing code.
- **Mechanism belongs in `rad_core`; capability belongs in the server.** If you
  are adding a permission check to `rad_core`, it is in the wrong place.
- Device-returned text is untrusted input and is wrapped at the `rad_core`
  boundary. Do not unwrap it, do not sanitise it, and never treat its content
  as instructions.
- New tools need a strong justification. Tool count is a shared, finite budget
  — every tool costs context in every session for every user. Prefer extending
  an existing tool's parameters over adding a new one.

---

## 6. Safety-critical

`rad_core/safety/`, the read whitelist, the audit log, the staged-commit flow,
and `docs/corpus-contract.md`.

**Open an issue before writing code.** These are locked in `CODEOWNERS` and
require maintainer approval.

The invariants, stated plainly so there is no ambiguity about what is being
protected:

- Writes are **staged**, reviewed by a human, then committed. An agent never
  self-approves.
- `confirm=true` is supplied by a person, never inferred, never defaulted.
- The read whitelist is an allowlist. It is never bypassed "just for this
  case."
- Every device interaction is audited, append-only.
- Reboot, factory default, and file deletion are out of scope for agents.
- Skill-side and server-side rules are **both** enforced. Neither is a
  fallback for the other.

If a legitimate use case appears to require breaking one of these, that is a
design conversation, not a pull request. Bring it — those conversations are
how the model improves — but bring it as an issue.
