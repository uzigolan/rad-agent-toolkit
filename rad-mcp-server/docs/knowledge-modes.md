# Bundled vs Served — the two knowledge modes (plain-English)

When you install the RAD skills you pick one of two modes. Here's the whole
thing on one page.

## The one idea to remember

The **MCP server always holds ALL the deep knowledge** — the full MIB catalog,
the CLI reference, and the device manuals (`rad-knowledge.sqlite`). The mode
only decides whether the **skill files on your client *also* carry a copy** of
the CLI reference + manuals, or leave that to the server.

## The two modes

**Bundled** (a.k.a. "embeded") — the **default**
- The skill carries its `references/` folder (~14 MB): CLI reference + manuals.
- Works **offline** for CLI/manual questions (no server needed for those).
- Every client keeps its own copy → you must reinstall each client to refresh.

**Served** — thin
- The skill is tiny (~56 KB): just `SKILL.md`, `references/` removed.
- CLI reference + manuals come **live from the MCP server's catalog**.
- Needs the MCP server connected for any knowledge; nothing local to go stale.

## What is the SAME in both modes

- **SNMP** (`snmp_probe`/`get`/`walk`) — always via the MCP server, read-only.
- **The full MIB catalog** (rich object definitions, enums, tables, traps) —
  always served by the MCP server. **Bundled does NOT carry the MIB
  definitions**; it only ships a tiny flat OID↔name map as an offline fallback.
- **`SKILL.md` behavior** (safety gates, personas, recipes) — always present.

So the mode changes **only how the CLI reference + manuals reach you.**
Everything SNMP/MIB is a *server* capability — identical either way.

| | Bundled (embeded) | Served |
|---|---|---|
| Skill size | ~14 MB | ~56 KB |
| CLI ref + manuals | in the skill | from the server catalog |
| Full MIB catalog | server only | server only |
| SNMP live tools | server only | server only |
| Works with no server | CLI/manuals yes | no |
| Refresh many clients | reinstall each | rebuild server once |

## Which to pick

- **Bundled** — you need CLI/manual answers **offline**, or a single client.
- **Served** — you **run the MCP server anyway** and have several clients you
  want always-current with zero drift (one server rebuild updates them all).

## Two gotchas from real testing

1. **Installer updates files; reload loads them.** After (re)installing, reload
   the window / start a new chat — otherwise the client keeps using the old
   skill it loaded at startup.
2. **Version numbers don't show mode, and `list_versions` shows the *server's*
   copy — not your local skill.** To see your **local** version + mode, run the
   skill self-check (`check_skill_version`); that's the merged report.
