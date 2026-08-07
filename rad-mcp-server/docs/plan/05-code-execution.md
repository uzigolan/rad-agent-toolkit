# Plan 05 — Code execution mode

**Branch:** `feat/code-execution` · **Risk:** HIGH
**Requires:** plans 00, 01, 02, 03, 04

Highest-value and highest-risk plan in the set. Do it last. If the security
section below cannot be satisfied, **do not ship it** — the toolkit is better
off slow than exploitable.

---

## Why

`docs/architecture.md` optimises the transport floor rigorously: persistent
sessions, prompt-anchored reads, 0.14 s warm health ping, measured numbers per
operation. What it does not address is **round-trip count**.

"Walk IF-MIB on etx2v-1 and summarize interface errors" is an SNMP walk plus N
object lookups plus reasoning — each a full model turn, with the entire
harvested payload passing through context. A fleet health sweep across 40
units is 40+ turns. The device-side cost is already at the floor; the model
side is not.

The pattern: rather than loading every tool definition upfront and
round-tripping per call, the agent explores available capabilities and **writes
code that calls only what it needs**, executing locally and returning a small
result.

There is direct evidence this fits rad-mcp: `health_check` already accepts
"one or more devices" **[VERIFIED from its description]**. That batching exists
because the pain was felt. This plan generalises it instead of adding a
bespoke batch tool per workflow.

---

## Design

### The tool

```python
run_rad_script(code: str, timeout_s: int = 60) -> ScriptResult
```

Executes Python in a sandbox with a curated `rad` API bound.

### The exposed API is read-only in v1

```python
rad.devices()                      # inventory
rad.show(device, command)          # whitelisted reads only
rad.show_in_context(device, ctx, command)
rad.cli_help(device, prefix)
rad.get_config(device)
rad.snmp.get(device, oids)
rad.snmp.walk(device, subtree)
rad.knowledge_search(query, corpus="auto", family=None)   # read-only proxy
```

**Not exposed in v1, and this is non-negotiable:**

`stage_config` · `commit_config` · `save_startup` · `backup_config` ·
inventory writes · credential access · **every debug-tree and shell tool**

Rationale: the entire safety model rests on a human reading a preview between
stage and commit. Code that can stage and commit in one execution deletes that
boundary. A script that can call `debug_shell_command` is remote code
execution with extra steps.

Writes may be considered for v2 **only** as: script returns a *proposed* set of
staged changes → normal `stage_config` → normal human review → normal
`commit_config`. Never inside the sandbox.

### Sandbox requirements

Treat generated code as hostile. Minimum bar:

- Separate process, not a thread. Hard kill on timeout.
- No filesystem access beyond a scratch dir. No network except through the
  `rad` API — no `socket`, no `requests`, no `urllib`.
- No `subprocess`, no `os.system`, no `ctypes`, no `importlib` of arbitrary
  modules.
- Memory and CPU caps. Output size cap — a script that returns 10 MB is as bad
  as one that hangs.
- Credentials never reachable from sandbox scope. The `rad` API holds device
  handles; the script never sees `.env` values, and `set_device_credentials`
  does not exist inside.
- Every `rad.*` call inside a script writes to `audit.jsonl` individually,
  plus one record for the script itself including its **full source**. The
  audit log must let a reviewer reconstruct exactly what touched which device.
- The read whitelist is enforced **inside** `rad.show`, reusing the existing
  driver validation. Do not reimplement it.

If a mature sandbox library covers this, prefer it over hand-rolling.

### Gating

`RAD_MCP_CODE_EXECUTION=true`, **default off**. Not enabled by `lean`. Never
available on the shared HTTP endpoint in v1 — local stdio only. Revisit only
after a security review with a human, documented in the PR.

---

## Prove the value before shipping

Benchmark these three against the current tool-per-call path. Record model
turns, total tokens, and wall clock in `docs/performance.md`:

1. IF-MIB walk on one device → summary of interfaces with errors
2. Health sweep across all inventory devices → table of alarms
3. Config-drift check: same context on three devices → diff

If the win is under roughly 3× on turns, **stop and report**. The security
surface is not worth a marginal gain, and that is a legitimate outcome for this
plan.

---

## Acceptance criteria

- [ ] Sandbox escape attempts fail: filesystem read, socket open, subprocess
      spawn, `os.environ` credential read, import of a blocked module —
      **write these as tests**
- [ ] No write, debug, or credential tool reachable from inside a script
- [ ] Read whitelist enforced inside `rad.show`; a non-whitelisted command is
      refused identically to the direct tool path
- [ ] Timeout kills a `while True` cleanly; session pool survives
- [ ] Audit log contains script source plus each individual device call
- [ ] Default off; absent from `lean`; refused on HTTP transport
- [ ] Benchmarks recorded, ≥3× turn reduction on all three scenarios
- [ ] Full eval suite green with the flag both on and off

## Rollback

Unset the flag. Nothing else depends on it.
