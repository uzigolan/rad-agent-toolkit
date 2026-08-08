"""rad-mcp MCP server.

Tools are product-agnostic verbs; the device's `family` field selects a
driver (CLI dialect), and the backend handles transport. Write tools follow
the staged-commit flow: stage_config -> (human reviews diff) -> commit_config.

Tools are registered in capability GROUPS (see rad_mcp/tools/ and
rad_mcp/profile.py); RAD_MCP_TOOL_PROFILE selects the surface. Credential
provisioning is NOT an MCP tool — use the rad-mcp-set-credentials CLI on the
server host.

Transports (RAD_MCP_TRANSPORT):
  stdio (default)  local — each client launches its own server process.
  http             remote — one server, many clients connect by URL. For
                   sharing on an INTERNAL network only. Two hard interlocks in
                   code (not just config): http REQUIRES bearer tokens or it
                   refuses to start, and write tools are SCOPED — registered
                   over http only when write-scoped tokens exist, and every
                   write call is re-checked so only write-token holders can
                   invoke it (read-only tokens get reads regardless).

Env:
  RAD_MCP_TOOL_PROFILE    legacy (default) | lean — see rad_mcp/profile.py.
                          legacy = full pre-grouping surface; lean = knowledge
                          + device + snmp (25 tools), optional groups per flag
  RAD_MCP_SNMP            lean only: false drops the 4 SNMP tools (default on)
  RAD_MCP_DEBUG_TOOLS     lean only: true adds the 8 debug-tree tools
  RAD_MCP_INVENTORY_WRITE lean only: true adds add/update/remove_device
  RAD_MCP_DEV_TOOLS       lean only: true adds run/stop_demo_device
  RAD_MCP_READONLY=true   disable write tools at registration (all transports,
                          both profiles — always wins over profile flags)
  RAD_MCP_TRANSPORT       stdio | http
  RAD_MCP_HOST            http bind address (default 127.0.0.1 — set to the
                          internal-network interface to share; never a public one)
  RAD_MCP_PORT            http port (default 8080)
  RAD_MCP_TOKENS          http READ-ONLY bearer tokens, comma-separated
  RAD_MCP_WRITE_TOKENS    http READ-WRITE bearer tokens, comma-separated —
                          holders may also run the staged-write/inventory tools
                          (at least one of TOKENS/WRITE_TOKENS is required for http)
  RAD_MCP_TLS_CERT        path to TLS certificate (PEM) — with RAD_MCP_TLS_KEY,
                          serves https:// natively (both must be set together)
  RAD_MCP_TLS_KEY         path to the certificate's private key (PEM)
"""
from __future__ import annotations

import json
import logging
import os
from pathlib import Path

from fastmcp import FastMCP

from . import __version__
from .audit import audit
from .drivers import _DRIVERS
from .profile import resolve_profile
from .prompts import register_prompts
from .runtime import (_HTTP, BACKUP_DIR, REPO_ROOT, WRITE_TOOLS_ENABLED,
                      _build_auth, _read_skill_version)
from .tools import (register_debug_tools, register_dev_tools,
                    register_device_tools, register_introspection_tools,
                    register_inventory_tools, register_knowledge_tools,
                    register_snmp_tools)

logger = logging.getLogger("rad_mcp")

TOOL_PROFILE = resolve_profile()

mcp = FastMCP(
    os.environ.get("RAD_MCP_SERVER_NAME", "rad-mcp"),
    version=__version__,   # reported via MCP serverInfo at the initialize handshake
    instructions=(
        "Operate RAD Data Communications devices (ETX-2 family and beyond). "
        "New device not in list_devices yet? Use add_device to register the "
        "facts; its credentials are then set by a human on the server host "
        "with the rad-mcp-set-credentials CLI — never edit inventory.yaml or "
        "server/.env yourself. "
        "Always run health_check or test_connectivity before configuration work. "
        "Writes are staged: stage_config returns a stage_id and preview; nothing "
        "touches the device until commit_config is called with confirm=true. "
        "A running-config backup is taken automatically before every commit. "
        "If a tool you expect is missing, read rad://status — it reports the "
        "active tool profile and which capability groups are enabled."
    ),
    auth=_build_auth(),
)

# ------------------------------------------------- capability-group registration
# One registration function per group (rad_mcp/tools/*) — the groups mirror
# the future server boundaries in docs/plan/DECOMPOSITION.md. Which groups
# load is resolved ONCE at startup (rad_mcp/profile.py); an unavailable tool
# does not exist in the session at all. RAD_MCP_READONLY always wins for
# write tools, in both profiles (runtime.WRITE_TOOLS_ENABLED).

if TOOL_PROFILE.knowledge:
    register_knowledge_tools(mcp)
if TOOL_PROFILE.device:
    register_device_tools(mcp, write_enabled=WRITE_TOOLS_ENABLED)
if TOOL_PROFILE.snmp:
    register_snmp_tools(mcp)
if TOOL_PROFILE.debug:
    register_debug_tools(mcp, write_enabled=WRITE_TOOLS_ENABLED)
if TOOL_PROFILE.inventory and WRITE_TOOLS_ENABLED:
    register_inventory_tools(mcp)
if TOOL_PROFILE.dev and WRITE_TOOLS_ENABLED:
    register_dev_tools(mcp)
if TOOL_PROFILE.introspection:
    register_introspection_tools(mcp)

# MCP prompts (plan 06) — curated workflows as the portable primitive; the
# Claude Code slash commands in commands/*.md share the same definitions
# (rad_mcp/prompts.py loads the command bodies). Registered on every profile:
# a prompt is instructions, not capability — if it names a tool the profile
# lacks, the body itself directs the model to rad://status.
register_prompts(mcp)

logger.info("tool profile '%s': groups %s (writes %s)",
            TOOL_PROFILE.name,
            ", ".join(g for g, on in TOOL_PROFILE.groups().items() if on),
            "enabled" if WRITE_TOOLS_ENABLED else "disabled")


# ---------------------------------------------------------------- resources

REFERENCE_DIR = REPO_ROOT / "skills" / "rad-cli-operations" / "references"


@mcp.resource("rad://status")
def status_resource() -> str:
    """Server status: version, active tool profile, capability groups and
    flags, write mode, loaded skill/driver versions, and knowledge-corpus
    build identity. If a tool seems missing, this explains why."""
    skills = []
    for skill_md in sorted((REPO_ROOT / "skills").glob("*/SKILL.md")):
        ver = _read_skill_version(skill_md.parent.name)
        skills.append({"name": skill_md.parent.name, "version": ver or "(unset)"})
    corpus: dict = {"status": "not built (bundled-mode installs answer from skill references)"}
    try:
        from . import knowledge as _k
        s = _k.status()
        m = s.get("meta", {})
        corpus = {
            "schema_version": m.get("schema_version"),
            "built_at": m.get("built_at"),
            "corpus_sha256": (m.get("corpus_sha256") or "")[:16],
        }
    except Exception:
        pass
    return json.dumps({
        "server_version": __version__,
        "tool_profile": TOOL_PROFILE.name,
        "groups_enabled": TOOL_PROFILE.groups(),
        "flags": TOOL_PROFILE.flags,
        "writes_enabled": WRITE_TOOLS_ENABLED,
        "transport": "http" if _HTTP else "stdio",
        "skills": skills,
        "drivers": [{"family": f, "version": getattr(d, "version", "?")}
                    for f, d in sorted(_DRIVERS.items())],
        "knowledge_corpus": corpus,
        "note": ("Tool groups OFF here are not registered in this session. "
                 "Profiles/flags: RAD_MCP_TOOL_PROFILE, RAD_MCP_SNMP, "
                 "RAD_MCP_DEBUG_TOOLS, RAD_MCP_INVENTORY_WRITE, "
                 "RAD_MCP_DEV_TOOLS, RAD_MCP_READONLY."),
    }, indent=1)


@mcp.resource("rad://inventory")
def inventory_resource() -> str:
    """The device inventory (names, hosts, families, groups — no credentials)."""
    path = Path(os.environ.get("RAD_MCP_INVENTORY") or REPO_ROOT / "inventory.yaml")
    return path.read_text(encoding="utf-8")


@mcp.resource("rad://backups")
def backups_resource() -> str:
    """List of configuration backups in the local archive, newest first."""
    if not BACKUP_DIR.exists():
        return "(no backups yet)"
    entries = sorted(BACKUP_DIR.glob("*.cfg"), key=lambda p: p.name, reverse=True)
    return "\n".join(f"{p.name}\t{p.stat().st_size} bytes" for p in entries) or "(no backups yet)"


@mcp.resource("rad://backups/{name}")
def backup_resource(name: str) -> str:
    """Contents of one backup file from the archive (by file name)."""
    path = (BACKUP_DIR / name).resolve()
    if path.parent != BACKUP_DIR.resolve() or path.suffix != ".cfg":
        return "REFUSED: name must be a .cfg file from the backup archive."
    if not path.exists():
        return f"Unknown backup '{name}'. See rad://backups for the list."
    return path.read_text(encoding="utf-8")


@mcp.resource("rad://command-tree/{family}")
def command_tree_resource(family: str) -> str:
    """Captured CLI command tree for a product family (from live `tree`/`?` sweeps)."""
    path = (REFERENCE_DIR / f"command-tree-{family}.md").resolve()
    if path.parent != REFERENCE_DIR.resolve():
        return "REFUSED: invalid family name."
    if not path.exists():
        known = ", ".join(p.stem.removeprefix("command-tree-") for p in REFERENCE_DIR.glob("command-tree-*.md"))
        return f"No captured tree for '{family}'. Available: {known or '(none yet)'}"
    return path.read_text(encoding="utf-8")


def _load_cli_help(family: str) -> list[dict] | None:
    """Load harvested `?`-help captures for a family (None if not harvested)."""
    path = (REFERENCE_DIR / f"cli-help-{family}.jsonl").resolve()
    if path.parent != REFERENCE_DIR.resolve() or not path.exists():
        return None
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


@mcp.resource("rad://cli-reference/{family}")
def cli_reference_index(family: str) -> str:
    """Index of harvested CLI `?` help: every known context for the family.

    Fetch one context via rad://cli-reference/{family}/{context} — spaces in
    the context path become '+', root level is 'root'
    (e.g. rad://cli-reference/secflow/configure+system).
    """
    entries = _load_cli_help(family)
    if entries is None:
        known = ", ".join(p.stem.removeprefix("cli-help-") for p in REFERENCE_DIR.glob("cli-help-*.jsonl"))
        return f"No harvested CLI help for '{family}'. Available: {known or '(none yet)'}"
    contexts: dict[str, int] = {}
    for e in entries:
        contexts[e["context"]] = contexts.get(e["context"], 0) + 1
    lines = [f"Harvested `?` help for family '{family}' — {len(contexts)} contexts.",
             "Fetch one: rad://cli-reference/" + family + "/<context with '+' for spaces>", ""]
    for ctx, n in contexts.items():
        key = "root" if ctx == "<root>" else ctx.replace(" ", "+")
        lines.append(f"{key}\t({n} captures)")
    return "\n".join(lines)


@mcp.resource("rad://cli-reference/{family}/{context}")
def cli_reference_context(family: str, context: str) -> str:
    """Harvested `?` help for ONE CLI context: the level listing plus each
    command's argument help. context uses '+' for spaces ('root' = root level).
    """
    entries = _load_cli_help(family)
    if entries is None:
        return f"No harvested CLI help for '{family}'. See rad://cli-reference/{family}."
    ctx = context.replace("+", " ").strip()
    if ctx in ("root", ""):
        ctx = "<root>"
    hits = [e for e in entries if e["context"] == ctx]
    if not hits:
        return (f"Unknown context '{ctx}' for '{family}'. "
                f"See rad://cli-reference/{family} for the index.")
    out = [f"# {family} :: {ctx}", ""]
    for e in hits:
        if e["kind"] == "level":
            out.append("Level help (`?`):")
        elif e["kind"] == "args-noenter":
            out.append(f"## {e['prefix']} (not entered — parameterized context; "
                       f"use cli_help with a real index for inner syntax)")
        elif e["kind"] == "args-param":
            key = f"{ctx} {e['prefix']} NAME".replace(" ", "+")
            out.append(f"## {e['prefix']} (parameterized — inner help at "
                       f"rad://cli-reference/{family}/{key})")
        else:
            out.append(f"## {e['prefix']}")
        out.append(e["text"] or "(no help output captured)")
        out.append("")
    return "\n".join(out)


@mcp.resource("rad://manual/{family}")
def manual_index_resource(family: str) -> str:
    """Index of the device user manual for a family: chapter list plus a
    CLI-topic -> manual-chapter cross-link table. The manual is the COMPANION
    to the harvested CLI reference — syntax lives in rad://cli-reference, while
    concepts, procedures, limits and alarm meanings live in the manual.
    Fetch one chapter via rad://manual/{family}/{chapter}.
    """
    path = (REFERENCE_DIR / f"manual-{family}" / "manual-index.md").resolve()
    manual_root = (REFERENCE_DIR / f"manual-{family}").resolve()
    if path.parent != manual_root or manual_root.parent != REFERENCE_DIR.resolve():
        return "REFUSED: invalid family name."
    if not path.exists():
        known = ", ".join(p.name.removeprefix("manual-") for p in REFERENCE_DIR.glob("manual-*") if p.is_dir())
        return f"No ingested manual for '{family}'. Available: {known or '(none yet)'}"
    return path.read_text(encoding="utf-8")


@mcp.resource("rad://manual/{family}/{chapter}")
def manual_chapter_resource(family: str, chapter: str) -> str:
    """One chapter of the device user manual as markdown. `chapter` is a file
    stem from the index (e.g. '06-6-management-and-security'); the '.md'
    suffix is optional.
    """
    stem = chapter[:-3] if chapter.endswith(".md") else chapter
    manual_root = (REFERENCE_DIR / f"manual-{family}").resolve()
    path = (manual_root / f"{stem}.md").resolve()
    if path.parent != manual_root or manual_root.parent != REFERENCE_DIR.resolve():
        return "REFUSED: invalid family or chapter name."
    if not path.exists():
        return f"Unknown chapter '{chapter}' for '{family}'. See rad://manual/{family} for the index."
    return path.read_text(encoding="utf-8")


@mcp.resource("rad://datasheet")
def datasheet_index_resource() -> str:
    """Index of all ingested product datasheets, grouped by family: system
    datasheets, chassis cards and accessories per family, plus standalone
    products with no inventory family. Fetch one datasheet via
    rad://datasheet/{product} (the product slug from this index).
    """
    path = REFERENCE_DIR / "datasheets" / "datasheet-index.md"
    if not path.exists():
        return ("No datasheets ingested yet. Run scripts/ingest_datasheet.py --all "
                "(driven by references/datasheet-map.yaml).")
    return path.read_text(encoding="utf-8")


@mcp.resource("rad://datasheet/{product}")
def datasheet_resource(product: str) -> str:
    """One product datasheet as markdown, split into '##' subject sections
    (features, interfaces, specifications, ordering). `product` is the slug
    from rad://datasheet (e.g. 'etx-2i-10g', 'asmi-54c'); '.md' optional.
    """
    stem = product[:-3] if product.endswith(".md") else product
    ds_root = (REFERENCE_DIR / "datasheets").resolve()
    path = (ds_root / f"{stem}.md").resolve()
    if path.parent != ds_root or path.name == "datasheet-index.md":
        return "REFUSED: invalid product name."
    if not path.exists():
        return f"Unknown product '{product}'. See rad://datasheet for the index."
    return path.read_text(encoding="utf-8")


def main() -> None:
    mode = "read-write (staged commits)" if WRITE_TOOLS_ENABLED else "READ-ONLY"
    groups = ",".join(g for g, on in TOOL_PROFILE.groups().items() if on)
    profile_note = f"profile={TOOL_PROFILE.name} groups={groups}"
    if _HTTP:
        host = os.environ.get("RAD_MCP_HOST", "127.0.0.1")
        port = int(os.environ.get("RAD_MCP_PORT", "8080"))
        cert = os.environ.get("RAD_MCP_TLS_CERT", "").strip()
        key = os.environ.get("RAD_MCP_TLS_KEY", "").strip()
        if bool(cert) != bool(key):
            raise SystemExit(
                "RAD_MCP_TLS_CERT and RAD_MCP_TLS_KEY must be set together "
                "(both for https, neither for plain http)."
            )
        uvicorn_config = None
        scheme = "http"
        if cert:
            for label, p in (("RAD_MCP_TLS_CERT", cert), ("RAD_MCP_TLS_KEY", key)):
                if not Path(p).is_file():
                    raise SystemExit(f"{label} file not found: {p}")
            uvicorn_config = {"ssl_certfile": cert, "ssl_keyfile": key}
            scheme = "https"
        audit("server_start", "-",
              detail=f"v{__version__} {mode} {profile_note} transport={scheme} "
                     f"{host}:{port} (auth required)")
        mcp.run(transport="http", host=host, port=port, uvicorn_config=uvicorn_config)
    else:
        audit("server_start", "-",
              detail=f"v{__version__} {mode} {profile_note} transport=stdio")
        mcp.run()  # stdio


if __name__ == "__main__":
    main()
