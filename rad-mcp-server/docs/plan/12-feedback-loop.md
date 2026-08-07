# Plan 12 — Feedback & improvement loop

**Branch:** `feat/feedback-loop` · **Risk:** medium (privacy)
**Requires:** plans 00, 08 · **Replaces:** manual dump-and-email

---

## The rule that makes this worth building

**A feedback report is not done when it reaches the maintainer. It is done
when it becomes an eval case.**

```
user dissatisfied → trace captured → triaged → eval case added → fix → case guards it forever
```

Terminate the pipeline in `tests/evals/cases/`. If it terminates in a
dashboard or an inbox, this is a support tool, not an improvement loop — and
the eval suite from plan 00 keeps being built from imagined failures instead
of real ones.

Every merged fix arising from feedback must reference the eval case it added.
Enforce in the PR template.

---

## Part A — Split the payload. This decides whether the feature ships.

A full trace from a customer device carries hostnames, IP addresses, complete
configurations, SNMP community strings, network topology, and customer names
in interface descriptions. Shipping that to a remote server is an exfiltration
path. Your own security review will block it, and telco and utility customers
will refuse categorically.

The insight that resolves it: **the decision path is what improves the system;
the device data usually is not.**

### Tier 1 — decision trace (default, low sensitivity)

```
timestamp, trace_id
model + version
servers connected, tool profile, enabled flags
skills loaded + versions
corpus_build_id, corpus version coverage for the family in play
user prompt
per tool call: name, arguments, latency,
               result SHAPE ONLY (row count, hit count, empty/non-empty,
               error class)
final assistant response
failure category (Part C) + free-text user comment
```

`corpus_build_id` is the sleeper field. "Was this answered from a corpus that
predates this device's firmware" explains a large share of failures and is
only answerable because plan 08 keys on `(family, firmware_version)`. Without
it, most traces are undiagnosable.

Tier 1 alone is roughly 80% of diagnostic value.

### Tier 2 — device payload (opt-in per submission)

Actual command output, configuration text, retrieved corpus passages.
**Elided by default.** The user attaches it deliberately, having seen it.

### Scrubbing, applied client-side before anything leaves the machine

- Credentials and SNMP community strings: **removed**, never hashed — a hash
  of a short community string is not protection.
- IPs and hostnames: **consistently pseudonymised**, not stripped. Topology
  reasoning must survive, so `10.1.1.5` maps to a stable placeholder within a
  trace. Stripping them makes the trace useless; leaking them makes it
  unshippable.
- Interface descriptions and `sysLocation`: often carry customer names — treat
  as Tier 2.

## Part B — Consent and deployment

Non-negotiable:

- **Explicit opt-in per submission.** No background telemetry, ever. This is a
  vendor tool running inside customer networks; silent collection would be a
  breach of trust that no amount of value justifies.
- **Show exactly what will be sent, with a redact step.** The user sees the
  payload, can remove lines, then confirms.
- **Self-hosted collector option.** Many customers will never send anything
  outside their network. An on-prem collector they can point at internally is
  what makes the feature adoptable at all — without it, the customers whose
  feedback you most want are precisely the ones who cannot give it.
- Export-to-file fallback so the current manual path still works for
  fully air-gapped sites.

## Part C — Structure the dissatisfaction

"Not satisfied" is too coarse to route. Categories map to owners and fixes:

| Category | Likely cause | Lands in |
|---|---|---|
| Command doesn't exist on this family | corpus or dialect gap | `rad-forge` / driver |
| Right command, wrong context path | driver dialect | driver |
| Didn't find info that is in the manual | retrieval | `rad-knowledge` |
| Wrong or outdated answer | stale corpus for this version | `rad-forge` |
| **Refused a legitimate request** | over-blocking | safety review |
| **Unexpected device behaviour** | **safety incident** | **urgent, separate** |
| Too slow | performance | `rad-device` |

Two of these need special handling:

**Unexpected device behaviour is a safety incident and must not enter the
general queue.** Route it to a separate channel with its own alerting. It also
triggers an audit-log pull, since `audit.jsonl` holds what actually reached
the device.

**Over-blocking reports are as important as failures.** A system that refuses
legitimate work quietly loses users without generating complaints. Give the
category a visible place in triage — it is the failure mode least likely to be
reported spontaneously and the one that most damages adoption.

## Part D — On "training"

**Do not fine-tune.** The improvement surface for this architecture is
**corpus + skills + tools**: auditable, instantly deployable, reversible, and
attributable to a specific change. Weight updates are a far larger investment
with slower iteration, no provenance, and no way to explain why an answer
changed — which forfeits the property this whole project is built on.

If model adaptation is ever wanted, this trace corpus is exactly the dataset
it would require. So collecting traces is the correct first step under either
future. Just do not make it the goal now.

The realistic improvement loop, in order of value:

1. Corpus fixes — most failures are missing or stale knowledge
2. Skill refinements — method and caveats
3. Tool and retrieval changes — least frequent, most expensive

## Part E — Architecture

- **Client library in `rad_core`** — mechanism, so every server inherits it and
  none can forget it. Consistent with the core/server rule in
  [DECOMPOSITION.md](DECOMPOSITION.md).
- **Collector is a service, not an MCP server.** It is not an agent capability
  and must not appear in any client tool list.
- Reuses `audit.jsonl` for the device-side record rather than duplicating it.
- Good contribution surface for new developers: self-contained, no device
  access, no hardware required. Route volunteers here — see
  [plan 10](10-contribution-model.md).

## Part F — Triage, so it does not rot

A queue nobody works is worse than no queue — it converts user goodwill into
silence.

- Weekly triage; every trace gets a category and either an eval case or an
  explicit "working as intended" with a reason.
- Duplicate detection by failure signature: same tool sequence, same corpus
  build, same family. Ten reports of one bug should appear as one item.
- Close the loop with the reporter. "Fixed in corpus build X" is what makes
  people report a second time.

---

## Acceptance criteria

- [ ] Tier 1 / Tier 2 split implemented; Tier 2 elided by default
- [ ] Credentials and community strings removed client-side; a seeded
      credential in a test trace never appears in collector output
- [ ] IPs and hostnames pseudonymised consistently within a trace
- [ ] Opt-in per submission; preview-and-redact before send; no background path
      exists (verify by inspection, not by configuration)
- [ ] Self-hosted collector deployable; documented
- [ ] File-export fallback works air-gapped
- [ ] `corpus_build_id` and loaded skill versions present in every trace
- [ ] Failure categories implemented; safety-incident route separate and alerting
- [ ] Triage produces an eval case or a documented "working as intended"
- [ ] PR template requires the eval case reference for feedback-driven fixes
- [ ] Collector is not registered as an MCP server anywhere

## Rollback

The client library is opt-in and off unless configured. Disable the config;
users fall back to the existing manual export.
