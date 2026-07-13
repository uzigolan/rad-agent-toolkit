# Fallback: skills on older VS Code (no Agent Skills support)

Native Agent Skills needs a Dec-2025+ Copilot Chat (VS Code ~1.10x). On
older builds (field-tested on VS Code 1.100, 2026-07-12) the skills can be
emulated with the **instructions-files** mechanism instead. The MCP part of
the [main guide](README.md) is unchanged — only the skills mechanism
differs.

## 1. Put the skill folders in the workspace

Copy `rad-mcp-server/skills/` (the three folders, `references/` included)
into the workspace, e.g. under `skills/`.

## 2. Make each SKILL.md discoverable as an instructions file

```powershell
copy skills\rad-core\SKILL.md skills\rad-core\rad-core.instructions.md
copy skills\rad-cli-operations\SKILL.md skills\rad-cli-operations\rad-cli-operations.instructions.md
copy skills\rad-device-mng\SKILL.md skills\rad-device-mng\rad-device-mng.instructions.md
```

And point VS Code at them — `.vscode/settings.json` (note the setting is
`chat.instructionsFilesLocations` in current builds; older builds may spell
it without the first `s` — check your version's settings UI):

```json
{
  "chat.instructionsFilesLocations": [".github", "skills/**"]
}
```

Without `applyTo` frontmatter these copies are NOT auto-applied — they're
manually attachable via `#` in chat, and step 3 is what makes them load.

## 3. Always-on loader: `.github/copilot-instructions.md`

```markdown
# Copilot Custom Instructions

## Installed Skills

- [rad-core](../skills/rad-core/SKILL.md) — safety rules, staged-commit flow
- [rad-cli-operations](../skills/rad-cli-operations/SKILL.md) — RAD CLI expertise (ETX-2, ETX-1p, SecFlow)
- [rad-device-mng](../skills/rad-device-mng/SKILL.md) — device inventory management

## General

When the user addresses "Abayev", "Noam", or "rad agent", read and follow
the rad-cli-operations and rad-core skill files. For inventory operations,
also read rad-device-mng. Before executing ANY device command — reads
included — show the command and ask for explicit confirmation.
```

This file is included in every request; the model reads the linked SKILL.md
files on trigger. That's a **behavioral** mechanism (like the Codex
`AGENTS.md` backstop) — hence the confirmation rule repeated in it.

## 4. Verify

Reload the window, switch Copilot Chat to **agent mode** (MCP tools and
workspace file reads need it), accept the MCP trust dialog, then:
`#` should list the three `.instructions.md` files, and
*"rad agent, list managed devices"* should trigger the tool call. The http
connection is read-only by the server's interlock.

## Known limits vs native Agent Skills

- No `/skill-name` invocation, no `/skills` management, no auto-trigger by
  description — the loader paragraph substitutes for all three.
- The `.instructions.md` copies drift from `SKILL.md` on updates — re-copy
  after every skill change.
- Prefer upgrading VS Code; this file exists for machines where you can't.
