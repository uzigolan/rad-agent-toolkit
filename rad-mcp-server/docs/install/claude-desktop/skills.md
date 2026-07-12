# Skills install — Claude Desktop

Desktop loads skills from **uploaded zips**, not folders — the one target
with a manual refresh step. No slash commands here — plain language only.
The MCP server is the separate [mcp.md](mcp.md).

## Upload

Sidebar **Customize → Skills → upload** the three zips from
[`dist/claude-desktop-skills/`](../../../dist/claude-desktop-skills/):
`rad-core.zip`, `rad-cli-operations.zip`, `rad-device-mng.zip`.

> Building the zips yourself? `python scripts/build_desktop_skills.py` —
> **not** PowerShell `Compress-Archive`, which writes backslash entry paths
> the upload rejects ("invalid character").

## Keeping them current

Uploaded zips are a **snapshot**: after any skill/reference update in the
repo (including a `/rad-harvest`), rebuild the zips and re-upload —
Desktop never sees repo changes on its own.

## Cowork sessions

The same uploads apply in Cowork automatically — nothing extra to do.

## Verify

Ask *"what's the command for active alarms on the secflow?"* — answered
from the skill's reference with no device contact.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Zip upload: "invalid character" | Zip built with `Compress-Archive` — rebuild with `scripts/build_desktop_skills.py` (forward-slash paths) |
| Skill answers feel stale | The uploads predate a repo update — rebuild + re-upload |
