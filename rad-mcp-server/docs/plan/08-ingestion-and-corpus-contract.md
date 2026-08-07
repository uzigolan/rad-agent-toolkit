# Plan 08 — Ingestion split & corpus contract

**Branch:** `feat/rad-forge` · **Risk:** medium · **Requires:** plan 00
**Do before:** adding release notes or YANG as sources

The highest-leverage plan in the set. Cheapest now, most expensive after two
more corpora land.

---

## Why

Knowledge onboarding — harvesting a CLI tree, digesting manuals and
datasheets, ingesting MIBs and MEA data, and re-onboarding an existing device
on a new firmware version — is a **build system**, not a runtime capability.
It shares drivers with the runtime and nothing else.

**Blast radius is the argument.** A runtime tool call affects one session. An
ingestion run rewrites the corpus that governs *every future session for every
user*. A truncated harvest or a mis-OCR'd manual becomes ground truth that
agents then cite with provenance and confidence. That is a supply-chain
surface, and supply chains are not protected by confirm flags.

Two supporting reasons:

- **Harvest performs writes dressed as reads.** Enumerating the tree creates
  and rolls back temp objects on live hardware. That operation has no business
  in a NOC engineer's tool list.
- **The source list is growing.** CLI, manuals, datasheets, MIBs, MEA — plus
  release notes and NETCONF/YANG incoming, plus whatever follows. Fused, every
  new source grows the runtime surface. Split, the runtime surface never grows
  again.

---

## Part A — Extract `rad-forge`

New server package, same repo, importing `rad_core`. **Never listed in any
client install config.** Run from CLI or CI by a knowledge maintainer.

Owns: `scripts/harvest_cli.py`, the manual/datasheet ingest scripts, MIB
ingest, MEA ingest, and every future source module.

Tools (agent-assisted maintenance, not unattended):

```
forge_harvest(device, family, version, subtree=None)
forge_ingest(source_type, path, family, version)
forge_diff(family, from_version, to_version)
forge_validate()          # contract conformance over the whole corpus
forge_build()             # emit corpus artefacts + build id
```

**Hard rule: `rad-forge` is the only code path that may write the corpus.**
The runtime servers open it read-only — enforce at the connection level, not
by convention.

**Output is a pull request, never an in-place write.** The corpus is already
committed to git, so code review is already the gate; this plan just declares
it. `forge_build` writes to a working tree; a human reviews the diff and
merges. Do not add an auto-commit path.

---

## Part B — The corpus contract

This is the substantive half. Write it as
`docs/corpus-contract.md` and make `forge_validate` enforce it.

### B1. Version is a first-class key

Today the corpus appears family-keyed (`cli-help-secflow.jsonl`). Firmware
drift is the entire reason live `cli_help` verification exists in the method —
so make the key `(family, firmware_version)`.

Consequences, all good:

- Re-onboarding an existing device on a new version is an **additive** ingest,
  not a corpus overwrite. Old versions stay queryable.
- `forge_diff(family, from, to)` becomes a first-class query. The harvest diff
  stops being a git diff someone reads and becomes structured firmware history
  — which is a feature you already half-invented; this makes it queryable.
- Retrieval can answer "on the version this device is actually running"
  rather than "on this family, probably."

`knowledge_search` (plan 03) gains an optional `version` filter, and results
state which version the hit came from and whether it was an exact or nearest
match. **Never silently answer from an adjacent version** — say which one.

### B2. Provenance on every row

Minimum columns:

```
source_type      cli_harvest | manual | datasheet | mib | mea | release_notes | yang
family
firmware_version
device_host      (harvest only)
harvested_at     (harvest only)
document_id      (doc sources: title, revision, page/section)
ingest_version   (which ingest script version produced this)
corpus_build_id
confidence       exact | derived | inferred
```

Justification: when an agent produces a wrong command, the first question is
always *where did that come from* — a 2019 PDF or a live 5.2.1 harvest.
Without per-row provenance you can neither answer it nor selectively
invalidate. It also lets `knowledge_search` cite properly, which is the
auditability advantage lexical retrieval was chosen for in the first place.

### B3. Source precedence, and conflicts recorded not resolved

Sources will disagree. Declare the order:

```
1. cli_harvest, exact version          (observed on the actual firmware)
2. release_notes, exact version        (authoritative on what changed)
3. manual, exact version
4. yang, exact version                 (schema — authoritative on structure)
5. manual, nearest version
6. datasheet
7. cli_harvest, adjacent version
```

When sources conflict on the same fact, **store both and emit a conflict
record**. Do not silently pick a winner. A surfaced conflict is useful
information for an engineer; a silent one is a landmine. `forge_validate`
reports conflict counts; `knowledge_search` surfaces them on affected hits.

### B4. Corpus identity is observable at runtime

`rad://corpus/status` returns build id, per-family version coverage, per-source
row counts, ingest script versions, and open conflict count. This is the one
thing runtime needs to know about ingestion.

---

## Part C — Source-specific rules

### Release notes — treat as a first-class delta source

Release notes are **version-delta documents**, which makes them uniquely
valuable against a version-keyed corpus: they are the human-authored
counterpart to the machine-derived harvest diff.

- Ingest keyed to `(family, from_version → to_version)`, not a single version.
- **Cross-validate against `forge_diff`.** If the notes claim a command was
  added in 5.2 and the harvest diff doesn't show it, that's a conflict record —
  and one an engineer genuinely wants to see. This is a capability no other
  source combination gives you; build it deliberately.
- Extract **known issues and caveats** as their own retrievable class. In
  practice "why is this behaving oddly on this version" is answered by a known
  issue more often than by a manual. Tag them so they can be surfaced
  proactively when a device's running version matches.
- Release notes are product-heavy and will be the largest prose corpus. Test
  that they do not swamp `corpus="auto"` ranking — this is the concrete risk
  they introduce.

### YANG — keep it structured, do not flatten to text

Manuals and CLI help are prose you search. YANG is a machine-readable schema
you can **validate against**. Storing it as FTS5 text throws that away.

Keep a structured representation, and the payoff is real: **validate a staged
config before `commit_config`**. That is a genuine addition to the safety
model, not just another corpus. Design for it now — retrofitting structure
after it has been flattened is the expensive path.

### MEA — separately gated corpus

MEA is FPGA registers and the hidden debug tree: the most dangerous knowledge
held. Blended into general search, a routine question can surface root-level
debug material.

Gate it the same way `rad-debug` gates the debug *tools* — MEA rows are only
searchable when the caller presents debug scope. Knowledge access and tool
access must stay consistent, or the gate on the tools is decorative.

### Harvest — device cleanliness is contract, not etiquette

`forge_harvest` must verify temp-object rollback before it reports success,
and refuse to emit corpus rows if cleanup verification fails. A corpus row is
not worth a stray object on a live device.

---

## Acceptance criteria

- [ ] `rad-forge` is a separate package; runtime servers open the corpus
      read-only and cannot write it
- [ ] `rad-forge` appears in no client install config
- [ ] `docs/corpus-contract.md` exists; `forge_validate` enforces it and fails
      on a deliberately malformed row
- [ ] Corpus keyed on `(family, firmware_version)`; two versions of one family
      coexist and are independently queryable
- [ ] `forge_diff` returns a structured CLI delta between two versions
- [ ] Every row carries the full provenance column set
- [ ] Precedence table implemented; a seeded conflict produces a conflict
      record rather than a silent pick
- [ ] `knowledge_search` states version and exact-vs-nearest on every hit, and
      never answers from an adjacent version without saying so
- [ ] MEA rows unsearchable without debug scope
- [ ] `rad://corpus/status` returns build id, coverage, conflict count
- [ ] Harvest refuses to emit rows when cleanup verification fails
- [ ] `forge_build` produces a working-tree diff, never a commit
- [ ] Full eval suite green; knowledge evals additionally assert cited version

## Rollback

Corpus format changes are the hard part. Ship the contract behind a corpus
schema version and keep the v1 reader until v2 has run in production for a
release. `rad-forge` extraction itself is a package move and reverts cleanly.
