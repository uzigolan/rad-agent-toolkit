# Plan 11 — Figures & images

**Branch:** `feat/corpus-figures` · **Risk:** low–medium
**Requires:** plans 00, 08 · **Owner surface:** `rad-forge` + `rad-knowledge`

---

## Design decision, stated up front

**Figures are stored as artifacts and additionally described in text. They are
never regenerated from their descriptions.**

This was considered and rejected. Record the reasoning here so it is not
relitigated by a future contributor:

1. **These are factual artifacts, not illustrations.** Rear-panel layouts with
   port numbering, connector pinouts, LED state diagrams, rack mounting,
   block diagrams, AXI/FPGA timing diagrams. A generated rear panel is a
   plausible-looking fabrication. An engineer wiring a device from a
   hallucinated pinout is real damage — and worse than a wrong CLI command,
   because a diagram looks authoritative and nobody re-verifies it.
2. **It contradicts the corpus contract.** Lexical retrieval was chosen over
   vector RAG for auditability — every answer cites a chapter. A generated
   figure has no provenance and cannot satisfy plan 08's provenance columns.
3. **Liability runs the other way from intuition.** These are RAD's own
   product documents ingested inside RAD — the easy case. Emitting a
   *fabricated* diagram presented as depicting a RAD product is the hard one.
4. **Precise semantics do not survive a round trip.** Pinouts and timing
   diagrams carry exact relationships that no prose description reconstructs.

The legitimate use of generation is covered in Part D — it is a different
thing and must stay visibly separate.

---

## Part A — Storage

Figures are binary artifacts. They do not go in the FTS5 database and do not
go into git as raw blobs alongside the text corpus.

- **Content-addressed store.** Filename is the SHA-256 of the bytes.
  Deduplicates across documents and revisions for free — the same panel
  diagram appears in many manuals.
- Backing store: git-lfs or an artifact store. Decide once, record it in the
  corpus contract, and make it configurable — customers running `rad-forge`
  on-prem may need a local path.
- **Never mutate.** Re-ingesting a revised manual adds new hashes; it does not
  overwrite. Same additive discipline as `(family, firmware_version)` keying.

## Part B — Corpus rows

Each figure produces one row conforming to plan 08's contract, plus figure
fields:

```
figure_hash          sha256 of the artifact
mime_type
document_id          source doc + revision
page / section
figure_label         "Figure 3-2" as printed
caption              verbatim from the document
description          generated at ingest, human-reviewed  (see Part C)
figure_type          panel | pinout | led | topology | block | timing | screenshot | other
referenced_from      [] text locations citing this figure
```

Plus the full standard provenance set: `source_type`, `family`,
`firmware_version`, `document_id`, `ingest_version`, `corpus_build_id`,
`confidence`.

**Captions and cross-references are high value — extract both.** Manual text
says "see Figure 3-2"; that link is what lets retrieval return the figure
alongside the paragraph that needs it. A figure ingested without its
`referenced_from` links is an orphan and will rarely surface at the right
moment.

`figure_type` matters because retrieval and safety differ by type: a pinout
answers a wiring question, a timing diagram answers an FPGA question, and a
screenshot of a web UI may be stale in a way a panel diagram is not.

## Part C — Descriptions are an index, not a replacement

A vision-model pass at ingest time in `rad-forge`. Once, offline, never at
query time.

The description exists so the figure is **findable in lexical search** and so
an agent without vision can reason about what the figure contains. It is not a
substitute for showing the figure.

Requirements:

- **Human-reviewed before merge**, like every other corpus row. A description
  becomes ground truth; an unreviewed one is exactly the "confident wrong
  answer" failure the corpus contract exists to prevent.
- Descriptions must be **descriptive, not interpretive**. Record what is
  depicted and what is labelled — port numbers, LED names, pin numbers, signal
  names. Do not record conclusions about what the reader should do.
- Set `confidence: derived` on the description field. It is machine-produced;
  the caption is `exact`.
- For pinouts and timing diagrams, additionally extract a **structured**
  representation (pin table, signal list) where feasible. That is far more
  useful than prose and is checkable against the figure by a reviewer.
- If the vision pass fails or produces something a reviewer rejects, the
  figure still ingests with caption and label only. **A figure with no
  description is fine; a figure with a wrong description is not.**

## Part D — Serving figures back to users

MCP resources on `rad-knowledge`:

```
rad://manual/{document_id}/figure/{figure_label}
rad://figure/{figure_hash}
```

`knowledge_search` hits gain an optional `figures` field listing related
figure URIs — from `referenced_from` links and from figure-row matches
directly. The agent cites the figure; the client renders it. No generation
anywhere in the path.

Search integration: figure rows are searchable through the normal
`knowledge_search` facade, with `corpus="manual"` or an added
`corpus="figure"` value if ranking requires it. **No new tool** — this is the
facade design from plan 03 doing its job.

## Part E — The one legitimate generation path, kept separate

Rendering diagrams **from data the system actually holds** is valuable and is
not what Part A rejects:

- a topology diagram rendered from live device and inventory state
- a structure diagram rendered from YANG
- a chart from SNMP counters

This is synthesis from ground truth, not fabrication of a source artifact.

**Keep it visibly separate.** Rendered output must be labelled as generated
from live data with a timestamp, must never be stored in the figure corpus,
and must never be returned from a `rad://manual/...` URI. A user must never
have to wonder whether a diagram came from the manual or from a renderer. If
this is built, it belongs to `rad-device`, not `rad-knowledge`.

Out of scope for this plan; noted so the boundary is explicit.

---

## Acceptance criteria

- [ ] Figures stored content-addressed; identical figures across two manuals
      deduplicate to one artifact
- [ ] Figure rows carry the full plan 08 provenance set plus figure fields
- [ ] Captions extracted verbatim; `referenced_from` links populated
- [ ] Vision descriptions generated in `rad-forge`, offline, marked
      `confidence: derived`, and gated behind human review
- [ ] A rejected description ingests the figure with caption only, not with a
      guess
- [ ] Pinout figures additionally yield a structured pin table where feasible
- [ ] `rad://manual/{doc}/figure/{label}` resolves and renders in at least two
      clients
- [ ] `knowledge_search` returns figure URIs alongside text hits for a query
      whose answer is a diagram (test: a rear-panel port question)
- [ ] **No new tool added to any server**
- [ ] No code path anywhere generates an image from a stored description —
      grep for it in review

## Rollback

Figure rows are a distinct source type. Drop them from the corpus and remove
the resource routes; text retrieval is unaffected.
