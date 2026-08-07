# Plan 09 — Server extraction

**Branch:** one per server, sequentially · **Risk:** medium
**Requires:** plans 00, 01, 03, 04 · **Target:** [DECOMPOSITION.md](DECOMPOSITION.md)

The destination plan 01 was transitional toward. Do not start until plan 01's
groups have run under `lean` with green evals for at least a release cycle.

---

## Why now rather than earlier

Env-flag grouping already removes the context cost. Process separation buys
three things flags cannot:

1. **Structural absence, not configured absence.** `rad-knowledge` with no
   transport layer, no drivers, and no credentials in the process cannot leak
   them regardless of bugs or misconfiguration. A flag is a promise; a missing
   dependency is a guarantee.
2. **Independent deployment and trust.** `rad-knowledge` can sit on a shared
   endpoint for field engineers, or behind a customer-facing app, without a
   security review of device write paths — because they aren't there.
3. **Independent growth.** Adding release notes or YANG touches
   `rad-knowledge` and `rad-forge` only. `rad-device` never rebuilds.

---

## Extraction order

Easiest and highest value first. Each is its own branch and PR.

### 1. `rad-knowledge`

No hardware, no credentials, no session pool — the clean cut. After plan 03 it
is ~2 tools plus resources.

Verify by inspection that the package imports nothing from the transport or
credential modules. Add a CI check asserting it: an import of `paramiko` (or
whatever the SSH layer is) inside `rad-knowledge` should fail the build.

### 2. `rad-debug`

Highest security value. Separate package, separate auth token, separate
install step. A deployment that never installs it cannot be talked into
enabling it.

Carries the debug scope that gates the MEA corpus in `rad-knowledge`
(plan 08). Define that scope handoff explicitly — it is the one cross-server
coupling in the design, so it deserves a written contract rather than an
implicit convention.

### 3. `rad-inventory`

Small. Mostly a move.

### 4. `rad-forge`

Already specified in [plan 08](08-ingestion-and-corpus-contract.md). If plan
08 shipped first, this step is already done.

### 5. `rad-device`

Whatever remains. Do it last so it is a rename rather than a redesign.

---

## `rad_core` — the shared library

Everything the servers share: drivers, session pool, family detection, read
whitelist, audit logging, corpus read access, device-output wrapping
(plan 02).

**Rule: mechanism in the core, capability in the server.** `rad_core` knows
*how* to open a session; it never decides *whether* a caller may. That
decision is which server the client connected to. If you find yourself adding
a permission check inside `rad_core`, the capability is in the wrong package.

Version all packages together from one repo. `rad-device 2.1.0` and
`rad-knowledge 2.1.0` are known-compatible; document that they must match.

---

## Install and distribution

The installers currently produce one config entry. They now produce a menu:

```
[x] rad-knowledge     always
[x] rad-device        NOC / engineering
[ ] rad-debug         RAD specialists only
[ ] rad-inventory     administrators
```

Ship three named presets so nobody assembles this by hand:

- **field** — knowledge only
- **noc** — knowledge + device (device in readonly unless a write token is set)
- **engineering** — knowledge + device + inventory
- *(debug is never in a preset; always a deliberate addition)*

Update all four installers (Code, Desktop, Copilot, Codex) and the portable
bundle.

---

## The thing most likely to go wrong

**Cross-server workflows.** "Check the manual, then verify live, then stage"
now spans `rad-knowledge` and `rad-device`. The model handles this fine — it's
just two servers' tools in one context — but your **skills and prompts must
stop assuming a single server**.

- Skills (plan 04) ship per server; each must be useful alone and compose when
  several are connected.
- Prompts (plan 06) that span servers need a home. Put cross-server workflows
  in `rad-device` (it is the one that implies the others) and have them degrade
  gracefully with a clear message when a needed server is absent.
- Write evals for the **partial-connection** cases: knowledge-only, and
  device-without-knowledge. Both are real deployments and both must behave
  sensibly rather than erroring obscurely.

---

## Acceptance criteria

- [ ] Five packages build and publish from one repo with matched versions
- [ ] `rad-knowledge` has no transport/credential imports; CI enforces it
- [ ] `rad-debug` requires separate install and its own token
- [ ] Debug→MEA scope handoff documented as an explicit contract
- [ ] Installers offer the presets; all four clients verified
- [ ] Full eval suite green in each preset configuration
- [ ] Partial-connection evals pass: knowledge-only, device-only
- [ ] `legacy` single-server mode still available for one release as a
      migration path, then removed in a separate PR

## Rollback

Keep the combined `legacy` server publishable for one full release after the
split. That is the rollback — not a code revert.
