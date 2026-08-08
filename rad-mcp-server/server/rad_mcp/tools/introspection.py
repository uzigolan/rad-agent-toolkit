"""introspection group — version/status reporting tools.

Registered as MCP tools only under the legacy profile; the lean profile
folds this information into the rad://status resource instead (plan 01 —
introspection is data, not action).
"""
from __future__ import annotations

from .. import __version__
from ..audit import audit
from ..drivers import _DRIVERS
from ..runtime import REPO_ROOT, _catalog_present, _kcall, _knowledge, _read_skill_version

# Tool version registry — bumped when tool behavior/signature changes.
# Tools inherit the server version unless introduced in an earlier release.
TOOL_VERSIONS = {
    # Inventory tools (v0.1.0)
    "list_devices": "0.1.0",
    "add_device": "0.1.0",
    "remove_device": "0.1.1",
    "update_device": "0.1.0",
    "run_demo_device": "0.1.0",
    "stop_demo_device": "0.1.1",

    # Metadata tools
    "check_skill_version": "0.6.0",
    "list_versions": "0.5.1",

    # Read tools (v0.1.0)
    "test_connectivity": "0.1.0",
    "run_show": "0.1.0",
    "get_config": "0.1.0",
    "health_check": "0.1.0",
    "run_show_in_context": "0.1.0",
    "cli_help": "0.1.0",
    "debug_tree_history": "0.1.0",
    "backup_config": "0.1.0",

    # SNMP tools
    "snmp_probe": "0.2.0",
    "snmp_get": "0.2.0",
    "snmp_walk": "0.2.0",
    "snmp_build_poll_plan": "0.4.1",

    # Knowledge/Reference tools
    "knowledge_status": "0.3.0",
    "mib_search": "0.3.0",
    "mib_describe": "0.3.0",
    "mib_table": "0.3.0",
    "mib_notifications": "0.3.0",
    "cli_search": "0.5.0",
    "manual_search": "0.5.0",
    "datasheet_search": "0.7.0",
    "mea_search": "0.8.0",
    "mea_commands_search": "1.0.0",
    "altera_search": "0.9.0",

    # set_device_credentials was an MCP tool in 0.8.0 -> 1.0.0; removed from
    # the tool surface in plan 01 (credential provisioning is now the
    # rad-mcp-set-credentials CLI, run by a human on the server host).

    # Write/Config tools (v0.1.0)
    "stage_config": "0.1.0",
    "commit_config": "0.1.1",
    "save_startup": "0.1.1",

    # Debug tools (v0.1.0)
    "debug_logon_request": "0.1.1",
    "debug_logon_submit": "0.1.1",
    "debug_access_preflight": "0.1.0",
    "debug_menu": "0.1.1",
    "enter_debug_shell": "0.1.1",
    "debug_shell_command": "0.1.1",
    "exit_debug_shell": "0.1.0",
}


def register_introspection_tools(mcp) -> None:
    """Register the 4 introspection tools (legacy profile only)."""

    @mcp.tool()
    def check_skill_version(skill: str, version: str, mode: str = "") -> dict:
        """Session self-check: a LOADED skill reports its own name, version, and
        installed knowledge mode (bundled|served, from its header's "Installed
        knowledge mode" line — omit if absent). The server replies with the
        version IT ships for that skill and its own effective mode, and flags any
        drift. Call once, before the first rad-mcp action of a session. Any
        returned `alerts` should be surfaced to the user in one line each, then
        continue — these are warnings, not blockers.

        Two checks:
          • VERSION — loaded skill version vs the server's skills/ copy (they drift
            when one is re-synced and the other isn't).
          • MODE — a `served` skill is thin (no references) and depends on the
            server's knowledge catalog; if the server has no catalog, its
            knowledge tools cannot answer and the pairing is broken. A `bundled`
            skill is self-sufficient, so a bundled/served-server pairing is
            harmless (reported as a note, not an alert)."""
        alerts: list[str] = []
        server_ver = _read_skill_version(skill)
        if server_ver is None:
            alerts.append(f"the rad-mcp server ships no skill named '{skill}' — a "
                          "renamed/typo'd skill, or a server that predates it")
            version_match = False
        else:
            version_match = (version.strip() == server_ver.strip())
            if not version_match:
                alerts.append(
                    f"VERSION MISMATCH — the '{skill}' skill loaded here is v{version.strip()}, "
                    f"but the connected rad-mcp server ships v{server_ver}. They may disagree on "
                    "tools/behavior; re-sync the skill copies (re-run the installer) or update the server.")
        loaded_mode = (mode or "").strip().lower() or "unknown"
        server_mode = "served" if _catalog_present() else "bundled-only"
        mode_note = None
        if loaded_mode == "served" and server_mode == "bundled-only":
            alerts.append(
                "MODE MISMATCH — this skill is installed 'served' (thin, no references) but the "
                "server has no knowledge catalog, so cli_search/manual_search/mib_* cannot answer. "
                "Build the catalog (scripts/build_knowledge_catalog.py) or reinstall the skill bundled.")
        elif loaded_mode == "bundled" and server_mode == "served":
            mode_note = ("skill is bundled (self-sufficient) — use local references/ files for all "
                         "knowledge lookups (cli-reference, manual, datasheets, altera-docs, snmp-map); "
                         "do NOT call cli_search/manual_search/datasheet_search/altera_search even though the "
                         "server has a catalog. Reinstall thin (--knowledge served) to save space.")
        return {
            "skill": skill,
            "loaded_version": version.strip(),
            "server_version": server_ver,
            "version_match": version_match,
            "loaded_mode": loaded_mode,
            "server_effective_mode": server_mode,
            "mode_note": mode_note,
            "alerts": alerts,
            "ok": not alerts,
        }

    @mcp.tool()
    def list_versions() -> dict:
        """Report the loaded rad-mcp component versions — the server, each skill, and
        each family driver — so you can tell which revision is running. Read-only,
        available on every transport. Skill versions are read from the server
        install's skills/ dir; driver versions from the live driver registry."""
        skills = []
        for skill_md in sorted((REPO_ROOT / "skills").glob("*/SKILL.md")):
            ver = _read_skill_version(skill_md.parent.name)
            skills.append({"name": skill_md.parent.name, "version": ver or "(unset)"})
        drivers = [{"family": f, "version": getattr(d, "version", "?")}
                   for f, d in sorted(_DRIVERS.items())]
        # Knowledge catalog is a distributable, versioned artifact too (schema +
        # content build). Report it so served-mode installs can spot a stale DB.
        catalog: dict = {"status": "not built (bundled-mode installs answer from skill references)"}
        try:
            from .. import knowledge as _k
            s = _k.status()
            m = s.get("meta", {})
            catalog = {
                "schema_version": m.get("schema_version"),
                "built_at": m.get("built_at"),
                "corpus_sha256": (m.get("corpus_sha256") or "")[:16],
                "objects": s.get("counts", {}).get("mib_objects"),
                "cli_help": s.get("counts", {}).get("cli_help"),
                "manual_sections": s.get("counts", {}).get("manual_sections"),
            }
        except Exception:
            pass
        return {"server": __version__, "skills": skills, "drivers": drivers,
                "knowledge_catalog": catalog}

    @mcp.tool()
    def tool_versions() -> dict:
        """Report all available MCP tools with their version history.
        Lists each tool's introduction version and current status. Bumped when
        tool behavior or signature changes; tools introduced in earlier server
        versions report that version (e.g. mib_search @ 0.3.0 even in 0.8.0)."""
        tools = [
            {"name": name, "version": version}
            for name, version in sorted(TOOL_VERSIONS.items())
        ]
        return {
            "server": __version__,
            "total_tools": len(tools),
            "tools": tools,
        }

    @mcp.tool()
    def knowledge_status() -> dict:
        """Knowledge-catalog status (offline): build identity, corpus hash, object
        counts, source roots, last build's validation summary."""
        k = _knowledge()
        out = _kcall(k.status)
        audit("knowledge_status", "-")
        return out
