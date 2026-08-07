# Plan 06 — MCP prompts

**Branch:** `main` · **Risk:** none · **Requires:** plan 00

Smallest plan here. Good first task for an agent new to the repo.

> **Decomposition note.** Prompts ship with the server that owns the work:
> `rad_family_compare` with `rad-knowledge`; `rad_health`, `rad_backup`,
> `rad_snmp_survey` with `rad-device`; `rad_onboard_device` with
> `rad-inventory`; `rad_harvest` with **`rad-forge`** — it is an ingestion
> operation and does not belong on a runtime server at all (see
> [plan 08](08-ingestion-and-corpus-contract.md)). Cross-server workflows live
> on `rad-device` and must degrade with a clear message when a needed server
> is absent.

---

## Why

`docs/architecture.md` lists slash commands `/rad-health`, `/rad-backup`,
`/rad-harvest` in the knowledge layer, annotated **"Code only"**. The
distribution section confirms it: the Claude skill and plugin format is not
portable; the server and the knowledge are.

Meanwhile `README.md` says installers exist for Claude Code, Claude Desktop,
GitHub Copilot, and OpenAI Codex. Three of those four surfaces get the tools
and the knowledge but none of the curated workflows.

MCP's `prompts` primitive is the portable equivalent — server-defined,
parameterised, discoverable by any compliant client. Same workflows, every
surface, no per-client code.

---

## Design

Expose as MCP prompts:

| Prompt | Arguments | Mirrors |
|---|---|---|
| `rad_health` | `device` or `group` | `/rad-health` |
| `rad_backup` | `device` or `group` | `/rad-backup` |
| `rad_harvest` | `device`, `family`, `version` | `/rad-harvest` — **rad-forge only** |
| `rad_snmp_survey` | `device` | ad-hoc today |
| `rad_family_compare` | `family_a`, `family_b`, `topic` | ad-hoc today |
| `rad_onboard_device` | `host`, `family` | ad-hoc today |

The last three are new: they are common asks in `README.md`'s "What can I
ask?" section that currently rely entirely on the model composing the right
sequence.

### Content rules

A prompt body is **instructions to the model**, not a script. It should state
the method — which layer to consult in what order, when to verify live, when
to stage — and let the model adapt.

Keep bodies short. They land in context in full when invoked; a 3,000-token
prompt template defeats the purpose. Reference `rad://` resources instead of
inlining knowledge.

`rad_harvest` needs particular care: harvesting creates and rolls back temp
objects on live hardware. Its prompt must restate the temp-object cleanup
verification and the device-cleanliness check, and must not be invocable
without an explicit device argument.

### Keep the slash commands

Claude Code users keep `/rad-*`. Reimplement those commands as thin wrappers
that invoke the corresponding MCP prompt, so there is one definition rather
than two that drift.

---

## Acceptance criteria

- [ ] `prompts/list` returns all six with argument schemas
- [ ] Each returns a usable message set from `prompts/get`
- [ ] Verified working on at least one non-Claude-Code client
- [ ] `/rad-health`, `/rad-backup`, `/rad-harvest` behave as before and share
      the prompt definitions
- [ ] No prompt body exceeds ~1,500 tokens
- [ ] `rad_harvest` requires an explicit device and restates cleanup checks
- [ ] `docs/architecture.md` stack diagram no longer marks workflows "Code only"

## Rollback

Additive. Remove the prompt registrations.
