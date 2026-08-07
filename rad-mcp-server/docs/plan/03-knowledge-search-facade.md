# Plan 03 — Knowledge search facade

**Branch:** `feat/knowledge-search-facade` · **Risk:** medium
**Requires:** plans 00, 01 · **Enables:** [plan 09](09-server-extraction.md)

> **Decomposition note.** This facade becomes the entire tool surface of
> `rad-knowledge` (see [DECOMPOSITION.md](DECOMPOSITION.md)). That is the real
> prize: a server whose tool count stays at ~2 **no matter how many corpora you
> add**. Release notes, YANG, MEA revisions, and everything after cost one enum
> value each and zero new tools. Do this before extracting the server.

---

## Why

Ten of the 43 tools are retrieval over **one SQLite FTS5 database**
(`rad-knowledge.sqlite`, architecture doc layer 6):

```
cli_search  manual_search  datasheet_search  mea_search  mea_commands_search
altera_search  mib_search  mib_describe  mib_table  mib_notifications
```

The ten-way split is an implementation detail — which corpus a document came
from — leaking into the model's context as ten schemas the model must choose
between. That choice is also a failure mode: "what does the `los` alarm mean"
could plausibly route to `cli_search`, `manual_search`, or `mib_search`, and
picking wrong yields an empty result the model then has to recover from.

One tool over one database is both fewer schemas and **better recall**,
because the facade can search across corpora and rank.

Note that gateway implementations converging on this pattern do the same thing
at a larger scale — exposing 100+ tools behind a `search_tools` /
`execute_tool` pair so agents load only what they need.

---

## Design

### The new tool

```python
knowledge_search(
    query: str,
    corpus: Literal["auto","cli","manual","datasheet","mib","mea",
                    "vendor","release_notes","yang"] = "auto",
    family: str | None = None,
    version: str | None = None,      # see plan 08 — corpus is version-keyed
    limit: int = 8,
) -> KnowledgeResult
```

`corpus="auto"` searches all corpora and interleaves by relevance. This is the
default and should be right most of the time. Explicit values exist so the
model can narrow when it already knows the answer shape ("exact command
syntax" → `cli`).

`family` filters — critical, since the whole product philosophy is that a
command on one family may not exist on another. `version` filters likewise
once [plan 08](08-ingestion-and-corpus-contract.md) lands; results must state
which version answered and whether it was an exact or nearest match.

**Include `release_notes` and `yang` in the enum from day one**, even before
those corpora exist — returning empty for an unpopulated corpus is free, while
changing a shipped tool schema later is not. This is the design property that
makes the facade worth building: new knowledge sources never again touch the
tool surface.

### Results carry provenance

Every hit returns: `corpus`, `family`, `source` (file/chapter/section/OID),
`snippet`, and a `resource_uri` pointing at the existing `rad://` resource so
the full document is one fetch away. This preserves the auditability the
architecture doc correctly prizes about lexical retrieval — you can still see
exactly which lines were pulled and cite the chapter.

### MIB tools need care — they are not all "search"

`mib_search` is retrieval and folds in cleanly. `mib_describe`, `mib_table`,
and `mib_notifications` are **structured lookups** with typed output — a full
object definition, a complete table model, a notification list. Flattening
those into snippets loses the structure that makes them useful.

Two acceptable resolutions; pick one and document it:

- **(A, preferred)** Fold `mib_search` into the facade. Keep one
  `mib_lookup(ref, kind="object"|"table"|"notification")` merging the other
  three. Net 10 → 2.
- **(B)** Fold all four; the facade returns structured payloads when the hit
  is a MIB object. Net 10 → 1, but the return type becomes a union and the
  schema gets muddier.

**Do not** flatten MIB structure into prose to force option B. The typed
output is a feature.

Same judgement applies to `snmp_build_poll_plan` — it *generates* a plan, it
does not retrieve. It stays out of the facade entirely.

### Migration — additive, then deprecate

1. Ship `knowledge_search` alongside all ten existing tools.
2. Rewrite each old tool's **description** to begin: `DEPRECATED — use
   knowledge_search(corpus="cli"). Retained for compatibility.` Behaviour
   unchanged.
3. Under `RAD_MCP_TOOL_PROFILE=lean` (plan 01), the deprecated ten are **not
   registered**. Under `legacy` they are.
4. Removal is a **separate PR, one release later**. Not in this branch.

---

## Skill changes

`rad-cli-operations/SKILL.md` and `rad-reference-knowledge/SKILL.md` currently
teach a routing method — which search tool for which question shape. That
routing largely moves into the tool. Rewrite those sections to teach:

- when to search at all vs. when to use live `cli_help` (unchanged: firmware
  drift, pre-write verification, contexts the harvest can't enter)
- how to narrow with `corpus` and `family`
- how to follow `resource_uri` for the full chapter

Keep the layered method intact — recipe → reference → manual for meaning →
live verify → stage. Only the tool names change, not the discipline.

---

## Acceptance criteria

- [ ] `knowledge_search` returns results at least as good as the specific tool
      for **every** knowledge eval case from plan 00 — run both, compare
- [ ] `corpus="auto"` finds the manual answer for "how many MQTT servers"
      without the model specifying a corpus
- [ ] `family` filtering proven: a secflow-only command does not surface for
      `family="etx2"`
- [ ] Provenance present on every hit; `resource_uri` resolves
- [ ] MIB structured lookups still return structured output
- [ ] `legacy` profile still exposes all ten with deprecation notices
- [ ] `lean` profile tool count drops by 8 (option A) from plan 01's 15 → 9,
      counting the facade and `mib_lookup`
- [ ] No change to `rad-knowledge.sqlite` schema or the ingest scripts

## Rollback

`lean` profile registers the old ten again; the facade is additive. Revert is
a one-line profile change plus removing the new tool.
