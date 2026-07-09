# TODO

Living task list. See [README.md](README.md) for the project overview and
[rad-mcp-server/docs/architecture.md](rad-mcp-server/docs/architecture.md)
for the full design.

## Done (2026-07-09 session)

- **Device inventory CRUD + `rad-device-mng` skill.** ⚠️ **Built, not
  yet tested end-to-end via real conversation or a live device — only
  verified at the code level (direct `mcp.call_tool()` calls in isolation:
  add → update → list → remove round-trip on a scratch inventory file).
  Still needs a real session testing the skill actually loading on the
  right trigger phrases, and a real `add_device` → `.env` → restart →
  `test_connectivity` pass against a real device.** New MCP tools
  `add_device`/`update_device`/`remove_device` (write tools — local/stdio
  only, never over shared HTTP, same interlock as `stage_config`) alongside
  the existing read-only `list_devices`, so a user who receives this
  plugin/skill set can self-onboard their own equipment instead of being
  limited to the pre-shipped lab units. `inventory.py` gained
  `add_device_entry`/`update_device_entry`/`remove_device_entry` — text-based
  append/edit (not a YAML round-trip) so the file's own safety header
  comment and formatting survive untouched. New skill
  `skills/rad-device-mng/SKILL.md` documents the full workflow,
  especially the credentials split (inventory.yaml = facts only; `.env` =
  credentials, and the running server must be **restarted** to pick up new
  `.env` values — it loads once at process start). `rad-core/SKILL.md`
  updated to cross-reference it and fix stale family-status text (`etx1p`
  was missing from the list entirely; `etx2` still said "pending live
  verification").
- **ETX-2 live verification.** First live etx2 driver verification (ETX-2I,
  Hw 0.2/D, Sw 6.8.5(1.116)). Added to `inventory.yaml`. Found and fixed a
  real driver gap: `configure_contexts` was missing `"test"`, so
  `cli_help`/`run_show_in_context` refused the entire Y.1564/RFC2544/L3SAT
  subtree even though the harvester had already proven it real.
- **Harvester: numeric-indexed parameterized-context auto-create.**
  `scripts/harvest_cli.py`'s create-then-roll-back mechanism (previously
  string-named temp objects only, e.g. `zzz-hrvst`) now also covers
  numeric-indexed contexts: `mep`, `lag`, `pw`, `test`, `bridge`,
  `isakmp-policy`, `mirroring-session`, `ppp`, `tunnel-interface`
  (`NUMERIC_CREATE_ALLOW`). Two safeguards specific to numeric contexts:
  - Each addition is checked against the family's **user manual** for a
    stated "Factory Defaults" / default-configuration confirmation that the
    object is genuinely inert on creation, before it's added to the
    allow-list.
  - The CLI's own declared range is **not trusted as an upper bound** — on
    etx2i, `lag` advertised `[1..4]` but rejected 4 ("Invalid LAG ID"), and
    `test` (rfc2544) declared no range at all but only accepted 1-8. The
    harvester now tries up to 6 free indices ascending from the bottom of
    the declared range, and on every refusal captures the device's own
    error text (plus, for numeric attempts, one read-only `<name> <idx> ?`
    follow-up probe) — so a "not entered" gap always carries a
    device-confirmed reason (missing argument / license gate / no live
    instance), not a guess.
  - Full case study: `rad-mcp-server/tests/eval-report.md`.
- **Re-harvested** `etx2i`, `etx1p`, and `lab-sf1p` with the new logic.
  Device verified clean after every run (fresh-connection `get_config`
  grep for `zzz-hrvst` and every numeric index tried).
- **Knowledge-coverage eval harness** — checks the `rad-cli-operations`
  skill's harvested reference against 35 prompts a prior AI/tool ("RAD
  CLI") failed on, from a real spreadsheet test log
  (`ETX-2i_Show_Commands_enhanced.xlsx`). Zero device execution, pure
  reference lookup. New scripts: `build_eval_dataset.py`,
  `check_eval_coverage.py`, `build_results_md.py`, `build_results_html.py`.
  Results: `rad-mcp-server/tests/RESULTS.{md,html}`,
  `rad-mcp-server/tests/eval-report.md`.
- Docs updated: root `README.md`, `rad-mcp-server/README.md`,
  `rad-mcp-server/docs/architecture.md`, `rad-mcp-server/tests/README.md`.
- `.gitignore`: root-level `*.xlsx` (source test spreadsheets) and their
  Excel lock files.

## Open

### Device management (untested)
- [ ] Test `rad-device-mng` for real: does the skill actually load on
  its trigger phrases in a fresh conversation? Full `add_device` → edit
  `server/.env` → restart server → `test_connectivity` → `health_check`
  pass against a real device. `update_device`/`remove_device` similarly
  untested outside isolated code-level calls.
- [ ] Decide whether a slash command (e.g. `/rad-device`) is also wanted
  alongside the skill — currently skill-only (conversational trigger, no
  explicit command).

### Harvester / eval gaps (from the etx2i case study)
- [ ] Teach the harvester to supply a second argument for `pw` (`type
  <psn>`) and `twamp responder` (`[<number>] light [l2-probe]`) — currently
  refused at every index because only the first argument is supplied.
- [ ] `twamp controller`/`profile` are genuinely license-gated
  (device-confirmed `License required`) — not a code fix; needs an actual
  TWAMP license on the lab unit, or accept as permanently out of reach on
  this hardware.
- [ ] RFC2544's `test` has no dedicated manual chapter to directly confirm
  create-safety (unlike its y1564/L3SAT siblings) — currently allow-listed
  on architectural-similarity reasoning only.
- [ ] `NUMERIC_CREATE_ALLOW` is a flat, family-agnostic name set. Currently
  safe only because `crawl()` already gates all auto-create to paths
  starting with `"configure"` (confirmed via the `isakmp-policy` /
  `quick-setup vpn` collision this session) — but a future name collision
  might not be as lucky. Consider scoping by `(family, parent_context,
  name)` instead of bare name.
- [ ] Same manual-vetted numeric auto-create pass for `secflow`/`etx1p`'s
  own remaining gaps beyond what's already closed (`bridge`,
  `isakmp-policy`, `mirroring-session`, `ppp`, `tunnel-interface` are done —
  check for others via each family's `args-noenter` entries).

### New integration targets
- [ ] **GitHub Copilot CLI** — package the MCP server + knowledge as a
  Copilot CLI extension/config. Copilot CLI speaks MCP directly; the open
  question is packaging (its own extension manifest format) and whether
  `SKILL.md` content needs translating into Copilot's prompt/instruction
  conventions or can be referenced as-is.
- [ ] **VS Code Copilot extension** — adapt `scripts/build_portable_bundle.py`'s
  output for Copilot Chat's MCP config (`.vscode/mcp.json` /
  workspace settings) and instruction file convention
  (`.github/copilot-instructions.md`). Decide whether personas
  (Abayev/Noam) and the response/verification modes translate directly or
  need Copilot-specific phrasing.
- [ ] Update the root README's "AI integration technology" table with a row
  once either lands, matching the existing MCP/Skills/Plugin rows' format.

### Pre-existing roadmap (carried over, not from this session)
- [ ] `rad://cli-reference/{family}/{context}` keyed-lookup resource for
  Desktop.
- [ ] RADview northbound API backend alongside SSH (currently SSH/Netmiko
  only).
- [ ] Manuals RAG — semantic search/embeddings over the manual corpus.
  Lexical retrieval (layer 4) is done for all 3 families; this is the
  planned layer 6 in `docs/architecture.md`.
- [ ] `.mcpb` Desktop Extension format + Claude Code plugin marketplace
  listing.
