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

> **[CORRECTED — implementation, 2026-08-08]** The single-definition goal is
> met in the **opposite direction**: a Claude Code slash command is plain
> markdown and has no mechanism to invoke an MCP prompt, so the wrapper
> direction the plan describes is not implementable. Instead the MCP prompts
> (`server/rad_mcp/prompts.py`) load their bodies from the canonical
> `commands/<name>.md` files at invocation time (frontmatter stripped,
> `$ARGUMENTS` filled) — one definition, zero drift, and the slash commands
> keep working untouched. Also: the decomposition into rad-knowledge /
> rad-device / rad-inventory / rad-forge servers (plans 04/08/09) has not
> happened yet, so all six prompts register on today's single server, tagged
> with their future home (`tags={"rad-device"}` etc.) so plan 09 moves them
> mechanically. Landed on `chore/baseline-and-evals` (not `main`) per the
> stream's working branch, server 0.11.0.

---

## Acceptance criteria

- [x] `prompts/list` returns all six with argument schemas — verified
      in-process via `fastmcp.Client`: 6 prompts, required args enforced
      (`rad_harvest.device`, `rad_snmp_survey.device`,
      `rad_family_compare.family_a/b/topic`, `rad_onboard_device.host/family`)
- [x] Each returns a usable message set from `prompts/get` — all six render
      one non-empty user message with sample args; `$ARGUMENTS` substitution
      and frontmatter stripping verified
- [ ] Verified working on at least one non-Claude-Code client — **pending
      user check**: reload the rad-mcp server in VS Code Copilot and invoke
      `/mcp.rad-mcp.rad_health` (in-process MCP client verification done;
      a user surface has not confirmed yet)
- [x] `/rad-health`, `/rad-backup`, `/rad-harvest` behave as before and share
      the prompt definitions — commands/*.md untouched and remain canonical;
      prompts read them at invocation time (direction corrected, see above)
- [x] No prompt body exceeds ~1,500 tokens — largest is `rad_harvest`
      (~1,145 tokens incl. the inherited safety notes); others 56–268
- [x] `rad_harvest` requires an explicit device and restates cleanup checks —
      schema marks `device` required, a blank value raises before rendering,
      and the body (from `commands/rad-harvest.md`) carries the temp-object
      rollback review + `zzz-hrvst` device-cleanliness check verbatim
- [x] `docs/architecture.md` stack diagram no longer marks workflows "Code
      only" — slash commands now noted as thin Claude Code entry points and a
      `prompts:` line lists all six

## Rollback

Additive. Remove the prompt registrations.
