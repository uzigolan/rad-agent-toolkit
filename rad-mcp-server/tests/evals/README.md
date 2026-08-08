# rad-mcp evals

Regression gate for agent behaviour (plan 00, task 3). Asserts **tool
selection and arguments** — which tool the model picks, with what arguments,
and critically which tools it does *not* call — never prose wording.

## Running

```bash
cd rad-mcp-server
pip install -e server            # rad_mcp must be importable
python tests/evals/runner.py     # full run (model phase needs an API key)
python tests/evals/runner.py --only-static      # no model, schema + registration
python tests/evals/runner.py --case safety -v   # filter by id substring
```

The model phase works with any of these providers — set one of:

- `ANTHROPIC_API_KEY` → Anthropic Messages API (default model `claude-sonnet-4-5`)
- `OPENAI_API_KEY` → OpenAI Chat Completions (default model `gpt-4o`)
- `OPENROUTER_API_KEY` → OpenRouter (OpenAI-compatible; default model
  `openai/gpt-4o`, names are vendor-prefixed: `--model anthropic/claude-sonnet-4.5`,
  `--model qwen/qwen3-coder`, ...)

Provider is auto-detected from whichever key is set (anthropic > openai >
openrouter); override with `--provider openrouter`. Override the model with
`--model` or
`RAD_EVAL_MODEL`.

Offline by default: **no lab hardware is ever touched.** Device tools are
mocked with canned output; knowledge tools pass through in-process to the real
committed corpus. Without an API key the model phase **skips loudly**
and exits 0 — a skip is reported as a skip, never as a pass.

## Why a raw model API, not a chat client

Production users reach these tools through a chat client — Claude Desktop,
Claude Code, Copilot, Cowork — so it's fair to ask why the evals don't just
use one of those. Four reasons, in order of importance:

1. **The eval tests what this repo ships.** The artifact under test is the
   skill text + the MCP tool surface — not the client. We control neither
   which client a user picks nor how that client behaves. When an eval fails,
   the only layer we can fix is the skill and the tool design, so that is the
   layer the harness must isolate.
2. **Clients add uncontrolled variables.** Every chat client injects its own
   system prompt, safety layer, and tool-routing heuristics — and changes
   them silently in updates. If a case failed inside a client, you could not
   tell whether the skill regressed or the client's scaffolding changed. In
   the raw-API harness a failure means exactly one thing: our artifact.
3. **Reproducibility is what makes it a regression gate.** Same model, same
   pinned harness, same fixtures — so a PR that breaks a safety case gets
   blamed on the PR. A chat session can never give that guarantee, which is
   why CI can only run the harness.
4. **The harness is a floor, not a ceiling.** If the bare model with only the
   skill refuses an implicit commit, a production client — which layers
   *more* scaffolding on top, not less — will too. Passing in the weakest
   environment is the strongest guarantee.

Testing through a real chat client is still valuable — it's a different
experiment: end-to-end **integration** testing of one specific client stack
(and how the live-device reports under `tests/` were produced). It complements
the harness; it cannot replace it as the gate.

## Case files

| File | Content |
|---|---|
| `cases/safety.yaml` | cross-family safety rules — **a failure here is a blocking safety regression, never a flaky test** |
| `cases/knowledge.yaml` | retrieval correctness, `device_io: forbidden` on every case |
| `cases/<family>.yaml` | 5 tool-selection cases per verified family |

## Case format

```yaml
- id: unique-case-id
  family: secflow            # optional, reporting only
  prompt: "user message"
  history:                   # optional prior turns (plain text)
    - { role: user, content: "..." }
    - { role: assistant, content: "..." }
  fixtures:                  # optional canned device output; "*" = any device tool
    run_show: "output text"
  expect:
    tool_called: run_show_in_context          # exact tool must be called
    tool_called_any: [run_show, cli_help]     # at least one of these
    tool_not_called: [commit_config]          # none of these
    args_contain: { command: "active-alarms" }  # substring, per named key
    args_contain_any: ["ethernet 3"]            # substring anywhere in args
    tool_args_forbidden:                        # tool may run, but never with these
      run_show: ["copy "]
    device_io: forbidden      # fail if ANY device-transport tool is called
    answer_contains: "2"      # substring in final answer (list = all required)
    answer_contains_any: ["no", "not"]
    reason: "why this case exists"
- id: readonly-check          # registration-level case: no model involved
  kind: registration
  env: { RAD_MCP_READONLY: "true" }
  expect:
    tools_absent: [stage_config]
    tools_present: [run_show]
```

## Writing cases

- `device_io: forbidden` cases are the cheapest and most valuable — write more
  of them than you think you need.
- Answer-content assertions are substring-only, never exact match.
- Ground every command/argument in
  `skills/rad-cli-operations/references/verified-commands.md` or the harvested
  `cli-reference-<family>.md` — never from memory.
- Do not pad suites to round numbers; a weak case that always passes is worse
  than no case.
- Must-succeed cases (e.g. `safety-stage-approve-commit-succeeds`) guard
  against over-blocking and are as important as refusal cases.

## CI

`.github/workflows/evals.yml` runs this on every PR and push to `main`.
The model API key comes from the `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` or
`OPENROUTER_API_KEY`
repository secret; when none is set the job posts a visible SKIPPED notice
to the job summary.
