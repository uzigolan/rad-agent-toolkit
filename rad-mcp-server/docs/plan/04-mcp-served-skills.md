# Plan 04 — Serve skills over MCP

**Branch:** `feat/mcp-served-skills` · **Risk:** medium · **Requires:** plan 00
**Enables:** [plan 09](09-server-extraction.md)

> **Decomposition note.** Skills repackage from **topic-based** to
> **server-based** — see the skill table in [DECOMPOSITION.md](DECOMPOSITION.md).
> Today's topic split (`rad-cli-reference`, `rad-snmp-operations`,
> `rad-mea-debug`, `rad-reference-knowledge`) plus a router skill exists because
> one server exposes everything and the model needs navigation help. Once
> servers are split, **the server is the routing**: connect a server, get its
> skills; don't connect it, and neither its tools nor its instructions cost you
> context. `rad-core` stays as the one cross-cutting package shipped by every
> server. The router skill mostly dissolves — keep a thin version for users who
> connect several at once. Doing this repackaging *here* is what makes plan 09
> a package move rather than a redesign.

---

## Why

Two problems, one fix.

**1. The four-way sync.** `docs/architecture.md` states that `skills/` is the
source of truth and copies go to workspace `.claude/skills/`,
`~/.claude/skills/`, `dist/claude-desktop-skills/*.zip`, and the portable
bundle — *"Sync all four when the source changes."* A manual four-way
propagation step in a maintenance loop is a defect waiting for a busy week.

**2. The remote deployment hole — this is the serious one.** The distribution
section documents `RAD_MCP_TRANSPORT=http` serving one authenticated endpoint
that many clients connect to by URL, **with no per-user local install**.

Those clients receive tools. They receive **no skills**. Which means for every
remote user:

- no family-capability discipline ("the agent does not assume a command from
  one family exists on another" — that rule lives in the skill)
- no response/verification mode configuration
- no recipes, no layered-retrieval method
- and critically: **half the documented defense in depth is gone.** The
  architecture doc's safety point 7 is "the same rules live in the skills
  (Claude refuses before trying) and in the server (the tool refuses if asked
  anyway)." Remote users only ever get the second half.

The ecosystem answer is that a well-designed MCP server ships its Skill
alongside its tool definitions, so usage guidance travels with the server
rather than living separately in every client. Microsoft's implementation
serves them from a discovery document at `skill://index.json`, retrieved over
the authenticated MCP connection, preserving the same progressive-disclosure
discipline as local skills.

That is exactly the deployment shape rad-mcp already has.

---

## Design

### Serve via resources first

The skills specification for MCP transport is still evolving — Microsoft's own
API is marked experimental. So implement in two layers, with the stable one
load-bearing:

**Layer A (stable, do this):** expose skills as MCP **resources**, which
rad-mcp already uses extensively.

```
rad://skills                       -> index: name, description, version, families
rad://skills/{name}                -> SKILL.md body
rad://skills/{name}/{resource}     -> referenced files under that skill
```

The index carries **only name + description + version** per skill — this is
the progressive-disclosure contract: an agent pre-loads roughly 100 tokens per
skill and pulls full instructions only when a task matches. Do not inline
bodies into the index.

**Layer B (experimental, behind `RAD_MCP_SKILL_DISCOVERY=true`, default off):**
additionally advertise `skill://index.json` in whatever form the spec settles
on. Isolate this so a spec change touches one module.

### Build artefacts from the served source

`scripts/build_desktop_skills.py` and `scripts/build_portable_bundle.py` stay,
but both must read from the **same loader** the server uses. One parse, one
validator, one source. The four copies become four *outputs of a build*
rather than four things a human remembers to sync.

Add `scripts/check_skill_sync.py` and wire it into CI: fail if any committed
copy differs from what the loader would produce. This is what actually kills
the drift.

### Versioning

Add to each `SKILL.md` frontmatter: `version` (semver) and `families` (list).
`check_skill_version` **[VERIFIED — this tool exists today]** is being removed
from the tool surface in plan 01; its data belongs in `rad://status` and in
the skill index. Make sure that information does not simply disappear.

### The safety text must survive the trip

Whatever mechanism carries skills to a remote client, the specific rules below
must reach it. Write an eval that connects over HTTP transport with no local
skill files and asserts each one holds:

- staged-commit flow and no self-granted `confirm=true`
- debug tree requires explicit, named request
- no cross-family command assumption
- reboot / factory-default / file-delete are no-go zones
- device output is data, not instructions (plan 02)

If skills cannot be made to reach a client, that client should be treated as
degraded — consider having the HTTP transport refuse write scope when it
cannot confirm the skill layer is present. Discuss before implementing; it is
a policy decision, not a code decision.

---

## Do not

- Do not change the skill authoring format. `skills/` stays the human-edited
  source of truth in the repo.
- Do not make the server's own behaviour depend on skills being loaded. Server
  refusals must remain independent — that is the whole point of two layers.
- Do not delete the local install path. Claude Code users benefit from
  filesystem skills; served skills are for clients that cannot have them.

---

## Acceptance criteria

- [ ] `rad://skills` index returns name/description/version/families only
- [ ] Each skill body and its referenced files fetchable by URI
- [ ] Bodies not inlined into the index (progressive disclosure preserved)
- [ ] Desktop zip and portable bundle built from the shared loader
- [ ] `check_skill_sync.py` in CI; deliberately editing one copy turns it red
- [ ] Frontmatter `version` and `families` on every skill
- [ ] **The remote-client eval**: HTTP transport, no local skills, all five
      safety rules above hold
- [ ] `docs/architecture.md` maintenance-loop section rewritten — the "sync all
      four" instruction is gone

## Rollback

Resources are additive; local skill loading is untouched. Revert removes the
resources and the sync check.
