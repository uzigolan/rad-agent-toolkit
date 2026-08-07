# DECOMPOSITION — target topology

Companion to `README.md`. This document defines the **target shape**; the
numbered plans are the steps that get there. Read this before any plan.

---

## Principle

One server per **blast radius**, not per feature area.

A feature-area split (`rad-cli`, `rad-snmp`, `rad-mib`) produces servers that
must all be connected together to be useful — decomposition with none of the
benefit. A blast-radius split produces servers a deployment can *decline to
connect*, which is the only decomposition that actually reduces risk and
context cost.

The four questions that place a capability:

1. Does it touch live hardware?
2. Can it change device state?
3. Can it change the knowledge corpus that governs all future sessions?
4. Who is the intended operator?

Capabilities with the same four answers belong in the same server. Different
answers, different server.

---

## Target: four runtime servers + one build-time

| Server | Hardware | Device writes | Corpus writes | Operator | Default |
|---|---|---|---|---|---|
| **rad-knowledge** | no | no | no | anyone | always on |
| **rad-device** | yes | staged only | no | NOC engineer | on |
| **rad-debug** | yes | root shell | no | RAD specialist | **off** |
| **rad-inventory** | probe only | no | no | admin | **off** |
| **rad-forge** | yes (harvest) | temp objects | **yes** | knowledge maintainer | never in a client |

### rad-knowledge

Retrieval over the corpus. **Zero device I/O — not gated, structurally
absent.** No transport, no drivers, no credentials in the process.

Tools: `knowledge_search`, `mib_lookup` (plan 03).
Resources: `rad://manual/*`, `rad://mib/*`, `rad://release-notes/*`,
`rad://corpus/status`.

This is the server that can be shared widely, run on a shared endpoint,
handed to field engineers, or pointed at by a customer-facing app without a
security conversation. Separating it is what makes that possible — today the
same process that answers "how many MQTT servers can an ETX-1p have" also
holds SSH credentials for the fleet.

**~2 tools.** Grows with corpora only by adding `corpus` enum values, never by
adding tools. Release notes, YANG, and whatever comes after cost zero tools.

### rad-device

Live operations on known devices.

Tools: `list_devices` (read), `test_connectivity`, `run_show`,
`run_show_in_context`, `cli_help`, `get_config`, `health_check`,
`backup_config`, `stage_config`, `commit_config`, `save_startup`, and the four
SNMP tools. Plus `run_rad_script` (plan 05) when enabled.

`RAD_MCP_READONLY` keeps working here exactly as today.

**~15 tools.** This is the one that stays roughly constant in size.

### rad-debug

MEA, FPGA, hidden debug tree, root shell. The 8 debug tools.

Separate server, separate install, separate auth token, off by default. Not
merely a flag on rad-device — a thing you must deliberately connect.

It also owns the **MEA corpus gate**: the MEA knowledge lives in rad-knowledge
but is only searchable when a caller presents debug scope. Knowledge access
and tool access stay consistent (plan 08).

**~9 tools**, present in almost no sessions.

### rad-inventory

`add_device`, `update_device`, `remove_device`. Registry mutation.

`set_device_credentials` is **removed from MCP entirely** and becomes a CLI
command run by a human. Credential provisioning at the end of an injection
path is the worst available outcome, and no agent workflow needs it.

**~3 tools**, off by default.

### rad-forge

Build-time only. Never connected to an interactive client. See
[plan 08](08-ingestion-and-corpus-contract.md).

---

## Why this holds as sources multiply

Release notes are the test case. Adding them today, fused, means: an ingest
path, a search tool, a resource family, and a skill section — spread across
one server that already has 43 tools.

Decomposed, adding release notes means:

- **rad-forge**: one new ingest module and one new corpus contract entry
- **rad-knowledge**: one new value in the `corpus` enum, one new resource
  prefix. **No new tool.**
- **rad-device**: nothing
- **rad-debug**: nothing

That's the whole point. YANG, MEA revisions, RADview data, and the next three
sources all land the same way.

---

## Skills mirror servers 1:1

Today's skills are organised by **topic** (`rad-cli-reference`,
`rad-snmp-operations`, `rad-mea-debug`, `rad-reference-knowledge`,
`rad-device-mng`) with a router (`rad-cli-operations`) and a core
(`rad-core`). That routing exists because one server exposes everything and
the model needs help navigating it.

Once servers are split, the server *is* the routing. Repackage:

| Skill package | Ships with | Contains |
|---|---|---|
| `rad-knowledge-skills` | rad-knowledge | retrieval method, corpus precedence, citing provenance, version-awareness |
| `rad-device-skills` | rad-device | safety model, staged-commit discipline, family capability rules, per-family dialect skills, response modes |
| `rad-debug-skills` | rad-debug | MEA tree, FPGA maps, access preflight, the "never without explicit request" rule |
| `rad-inventory-skills` | rad-inventory | onboarding a host, family corroboration |
| `rad-forge-skills` | rad-forge | harvest procedure, ingest review, corpus contract |

Each package is served by its own server (plan 04). Connect a server, get its
skills. Don't connect it, and neither its tools nor its instructions consume
context.

**`rad-core` survives** as the one cross-cutting package: safety posture,
device-output-is-data (plan 02), no cross-family assumption. It ships with
every server; identical content, deduplicated by the client.

**`rad-cli-operations` (the router) mostly dissolves.** Keep a thin version for
users who connect several servers at once.

---

## Shared core library

All five servers import one package — `rad_core` — holding drivers, session
pool, family detection, read whitelist, audit log, and corpus read access.

**Rule: capability lives in the server, mechanism lives in the core.** The
core knows *how* to open a session; it never decides *whether* a caller may.
That decision is which server you connected to.

Package the servers from one repo with shared versioning, so `rad-device
2.1.0` and `rad-knowledge 2.1.0` are known-compatible.

---

## Migration reality

Do **not** attempt the split as one change. Plan 01 uses env-flag profiles
inside the single server as a transitional step — it lets you prove the tool
groupings are right before you pay for process separation. The groups in plan
01 are deliberately identical to the servers here.

Order: flag-based grouping (plan 01) → verify with evals → extract
rad-knowledge first (easiest, no hardware) → rad-debug → rad-inventory →
rad-forge. rad-device is whatever remains.
