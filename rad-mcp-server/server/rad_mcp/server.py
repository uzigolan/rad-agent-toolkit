"""rad-mcp MCP server.

Tools are product-agnostic verbs; the device's `family` field selects a
driver (CLI dialect), and the backend handles transport. Write tools follow
the staged-commit flow: stage_config -> (human reviews diff) -> commit_config.

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
  RAD_MCP_READONLY=true   disable write tools at registration (all transports)
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
import os
import secrets
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from fastmcp.server.dependencies import get_access_token

from . import __version__
from .audit import audit, redact
from .backends import get_backend
from .drivers import _DRIVERS, get_driver
from .inventory import (add_device_entry, get_device, load_inventory,
                        remove_device_entry, set_device_credentials as _set_device_credentials,
                        update_device_entry)

_TRANSPORT = os.environ.get("RAD_MCP_TRANSPORT", "stdio").lower()
_HTTP = _TRANSPORT in ("http", "streamable-http")


def _parse_tokens(var: str) -> list[str]:
    return [t.strip() for t in os.environ.get(var, "").split(",") if t.strip()]


# Per-token roles: RAD_MCP_TOKENS are read-only, RAD_MCP_WRITE_TOKENS are
# read-write. A value present in both lists is treated as read-write.
_READ_TOKENS = _parse_tokens("RAD_MCP_TOKENS")
_WRITE_TOKENS = _parse_tokens("RAD_MCP_WRITE_TOKENS")
_READONLY_ENV = os.environ.get("RAD_MCP_READONLY", "").lower() in ("1", "true", "yes")

# Interlock 1 (scoped): over HTTP the write tools are REGISTERED only when at
# least one write-scoped token exists, and every write call is re-checked at
# call time (see _require_write_scope) so only write-token holders can invoke
# them. Over stdio (local, trusted) writes are on unless RAD_MCP_READONLY.
if _HTTP:
    WRITE_TOOLS_ENABLED = bool(_WRITE_TOKENS) and not _READONLY_ENV
else:
    WRITE_TOOLS_ENABLED = not _READONLY_ENV

BACKUP_DIR = Path(__file__).resolve().parent.parent / "backups"


def _build_auth():
    """Interlock 2: HTTP requires bearer tokens — refuse to serve unauthenticated.
    Read-only tokens come from RAD_MCP_TOKENS, read-write tokens from
    RAD_MCP_WRITE_TOKENS; each token carries its scope so write tools can
    re-check the caller at call time. stdio needs no auth."""
    if not _HTTP:
        return None
    if not _READ_TOKENS and not _WRITE_TOKENS:
        raise SystemExit(
            "RAD_MCP_TRANSPORT=http requires RAD_MCP_TOKENS (read-only) and/or "
            "RAD_MCP_WRITE_TOKENS (read-write). Refusing to start an "
            "unauthenticated network server."
        )
    tokens: dict[str, dict] = {}
    for i, tok in enumerate(_READ_TOKENS):
        tokens[tok] = {"client_id": f"rad-ro-{i+1}", "scopes": ["read"]}
    # Write tokens win if a value appears in both lists.
    for i, tok in enumerate(_WRITE_TOKENS):
        tokens[tok] = {"client_id": f"rad-rw-{i+1}", "scopes": ["read", "write"]}
    from fastmcp.server.auth.providers.jwt import StaticTokenVerifier
    return StaticTokenVerifier(tokens)


def _require_write_scope() -> None:
    """Interlock 1 (per-call): over HTTP, only tokens carrying the 'write'
    scope (RAD_MCP_WRITE_TOKENS) may invoke a write tool. stdio is local and
    trusted, so it is exempt."""
    if not _HTTP:
        return
    token = get_access_token()
    scopes = list(getattr(token, "scopes", None) or [])
    if "write" not in scopes:
        raise ToolError(
            "This token is read-only. A write-scoped token "
            "(RAD_MCP_WRITE_TOKENS on the server) is required for "
            "configuration and inventory changes."
        )


mcp = FastMCP(
    os.environ.get("RAD_MCP_SERVER_NAME", "rad-mcp"),
    version=__version__,   # reported via MCP serverInfo at the initialize handshake
    instructions=(
        "Operate RAD Data Communications devices (ETX-2 family and beyond). "
        "New device not in list_devices yet? Use add_device to register the facts, "
        "then set_device_credentials for its login — the server stores credentials "
        "in its own .env; never edit inventory.yaml or server/.env yourself. "
        "Always run health_check or test_connectivity before configuration work. "
        "Writes are staged: stage_config returns a stage_id and preview; nothing "
        "touches the device until commit_config is called with confirm=true. "
        "A running-config backup is taken automatically before every commit."
    ),
    auth=_build_auth(),
)

# In-memory staging area: stage_id -> {device, lines, created}
_STAGES: dict[str, dict] = {}


# ---------------------------------------------------------------- inventory

@mcp.tool()
def list_devices(group: str = "", family: str = "") -> list[dict]:
    """List devices from the inventory, optionally filtered by group or product family."""
    devices = load_inventory().values()
    out = []
    for d in devices:
        if group and group not in d.groups:
            continue
        if family and d.family != family:
            continue
        out.append(d.summary())
    return out


def _read_skill_version(name: str) -> str | None:
    """The version the SERVER's own skills/ copy of <name> declares, or None
    if the server ships no such skill."""
    md = (REPO_ROOT / "skills" / name / "SKILL.md")
    if not md.exists():
        return None
    seen = 0
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.strip() == "---":
            seen += 1
            if seen == 2:
                break
            continue
        if seen == 1 and line.lower().startswith("version:"):
            return line.split(":", 1)[1].strip()
    return "(unset)"


def _catalog_present() -> bool:
    try:
        from . import knowledge as _k
        _k._db_path()
        return True
    except Exception:
        return False


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
        mode_note = ("skill is bundled (self-sufficient) while the server is served-capable — "
                     "harmless; you may reinstall thin (--knowledge served) to save space.")
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
        from . import knowledge as _k
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
def test_connectivity(device: str) -> str:
    """Verify SSH reachability and authentication against a device (runs no user commands)."""
    dev = get_device(device)
    try:
        get_backend().execute(dev, "", timeout=20)
        audit("test_connectivity", device, ok=True)
        return f"OK: SSH session to {dev.name} ({dev.host}) established and closed."
    except Exception as e:  # noqa: BLE001 — report, don't crash the server
        audit("test_connectivity", device, detail=str(e), ok=False)
        return f"FAILED: {redact(str(e))}"


# --------------------------------------------------------------------- read

@mcp.tool()
def run_show(device: str, command: str) -> str:
    """Run a whitelisted read-only command (show/info/help/ping...) on a device."""
    dev = get_device(device)
    driver = get_driver(dev.family)
    if not driver.is_show_allowed(command):
        allowed = ", ".join(driver.show_whitelist)
        return f"REFUSED: '{command}' is not whitelisted for {dev.family}. Allowed prefixes: {allowed}"
    out = get_backend().execute(dev, command)
    audit("run_show", device, detail=command)
    return out


@mcp.tool()
def get_config(device: str) -> str:
    """Export the device's current configuration."""
    dev = get_device(device)
    driver = get_driver(dev.family)
    out = get_backend().execute(dev, driver.config_export_command, timeout=60)
    audit("get_config", device)
    return out


@mcp.tool()
def health_check(device: str) -> dict[str, str]:
    """Run the driver-defined health sweep (device info, active alarms, ...) over one session."""
    dev = get_device(device)
    driver = get_driver(dev.family)
    results = get_backend().execute_many(dev, list(driver.health_sequence))
    audit("health_check", device)
    # Drop the navigation lines (empty output) from the result for readability
    return {cmd: out for cmd, out in results if out.strip()}


@mcp.tool()
def run_show_in_context(device: str, context: str, command: str) -> str:
    """Run a whitelisted read command inside a CLI context (RAD CLIs scope `show` to contexts).

    context: space-separated navigation path, e.g. "configure reporting" or
    "configure port ethernet 1". Only level names/indexes — never commands
    that set values. command: a whitelisted read command, e.g. "show active-alarms".
    """
    dev = get_device(device)
    driver = get_driver(dev.family)
    if not driver.is_show_allowed(command):
        allowed = ", ".join(driver.show_whitelist)
        return f"REFUSED: '{command}' is not whitelisted for {dev.family}. Allowed prefixes: {allowed}"

    tokens = context.strip().lower().split()
    if not tokens or tokens[0] not in ("configure", "admin", "file"):
        return "REFUSED: context must start with 'configure', 'admin' or 'file'."
    if tokens[0] == "configure" and len(tokens) > 1 and driver.configure_contexts \
            and tokens[1] not in driver.configure_contexts:
        known = ", ".join(driver.configure_contexts)
        return f"REFUSED: unknown configure context '{tokens[1]}'. Known: {known}"
    if any(not t.replace("-", "").replace("/", "").replace(".", "").isalnum() for t in tokens):
        return "REFUSED: context tokens may only contain letters, digits, '-', '/', '.'"

    sequence = ["exit all", context.strip(), command.strip(), "exit all"]
    results = get_backend().execute_many(dev, sequence)
    audit("run_show_in_context", device, detail=f"{context} :: {command}")
    nav_errors = [out for cmd, out in results if cmd != command.strip() and "cli error" in out.lower()]
    if nav_errors:
        return "NAVIGATION ERROR:\n" + "\n".join(nav_errors)
    return next((out for cmd, out in results if cmd == command.strip()), "")


@mcp.tool()
def cli_help(device: str, context: str = "", prefix: str = "") -> str:
    """Query the device's interactive `?` help — the authoritative, firmware-exact
    syntax reference. Use it to discover commands and validate arguments BEFORE
    staging config.

    context: navigation path ("configure system") or "" for root-level help.
    prefix: "" lists every command at that level with descriptions; a command
    name ending with a space ("location ") lists that command's arguments,
    types and constraints (e.g. [2..2 chars]). Nothing is executed on the
    device — the pending input is cleared after the help is captured.
    """
    dev = get_device(device)
    driver = get_driver(dev.family)

    if any(ord(c) < 32 for c in prefix) or any(ch in prefix for ch in ("|", ";")):
        return "REFUSED: prefix must be plain text (no control characters, '|' or ';')."
    navigation = ["exit all"]
    ctx = context.strip()
    if ctx:
        tokens = ctx.lower().split()
        if tokens[0] not in ("configure", "admin", "file"):
            return "REFUSED: context must start with 'configure', 'admin' or 'file' (or be empty for root)."
        if tokens[0] == "configure" and len(tokens) > 1 and driver.configure_contexts \
                and tokens[1] not in driver.configure_contexts:
            known = ", ".join(driver.configure_contexts)
            return f"REFUSED: unknown configure context '{tokens[1]}'. Known: {known}"
        if any(not t.replace("-", "").replace("/", "").replace(".", "").isalnum() for t in tokens):
            return "REFUSED: context tokens may only contain letters, digits, '-', '/', '.'"
        navigation.append(ctx)

    out = get_backend().interactive_help(dev, navigation, prefix)
    audit("cli_help", device, detail=f"{ctx or '<root>'} :: {prefix or '<level>'}?")
    # Trim the echoed keystrokes and the re-displayed trailing prompt line.
    lines = out.splitlines()
    if lines and lines[0].strip().endswith("?"):
        lines = lines[1:]
    while lines and (not lines[-1].strip() or lines[-1].rstrip().endswith(("#", "# " + prefix.strip(), prefix))):
        lines = lines[:-1]
    return "\n".join(lines).strip() or out.strip()


@mcp.tool()
def backup_config(device: str) -> str:
    """Export the device configuration and save it to the local backup archive."""
    dev = get_device(device)
    path = _take_backup(dev)
    return f"Backup saved: {path}"


def _take_backup(dev) -> Path:
    driver = get_driver(dev.family)
    config = get_backend().execute(dev, driver.config_export_command, timeout=60)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = BACKUP_DIR / f"{dev.name}-{stamp}.cfg"
    path.write_text(config, encoding="utf-8")
    audit("backup_config", dev.name, detail=str(path))
    return path


# ------------------------------------------------------------- SNMP (reads)
# Read-only by construction (GET / GETNEXT only — this toolkit never sends
# SET; config writes stay on the CLI's staged-commit flow). Registered
# unconditionally, like the other read tools. Credentials come from
# server/.env (RAD_MCP_<NAME>_SNMP_COMMUNITY / _SNMP_V3_USER); see
# backends/snmp.py for the RAD-agent quirks these tools encode.

def _snmp():
    try:
        from .backends import snmp as _mod
        import pysnmp  # noqa: F401 — surface a clean error if absent
        return _mod
    except ImportError as exc:
        raise ToolError(
            "SNMP support needs the 'pysnmp' package in the server venv: "
            "pip install pysnmp  (then retry)"
        ) from exc


@mcp.tool()
def snmp_probe(device: str) -> dict[str, str]:
    """SNMP identity probe (read-only): MIB-II system group — exact firmware
    via sysDescr, plus a sysObjectID -> family hint. Works without any CLI/SSH
    session, so it is the safe first contact for fragile-SSH units."""
    s = _snmp()
    dev = get_device(device)
    out = s.snmp_probe(dev)
    audit("snmp_probe", device)
    return out


def _decorate(oid: str, val: str) -> str:
    """Append catalog semantics (enum meaning, units) to a live value.
    Graceful no-op when the knowledge catalog is absent."""
    try:
        from . import knowledge as k
        d = k.decode_value(oid, val)
    except Exception:
        d = None
    if not d:
        return val
    out = val
    if d.get("meaning"):
        out += f"  = {d['meaning']}"
    if d.get("units"):
        out += f" [{d['units']}]"
    return out


def _log_observation(dev, tool: str, subject: str, observed: str) -> None:
    """Append-only live capability evidence (design Phase 4: stored separately
    from MIB definitions; the next catalog build can import this file)."""
    try:
        import json as _json
        path = REPO_ROOT / "server" / "logs" / "capability-observations.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(_json.dumps({
                "ts": datetime.now(timezone.utc).isoformat(),
                "family": dev.family, "device": dev.name, "tool": tool,
                "subject": subject, "observed": observed,
                "evidence_type": "live-snmp",
            }) + "\n")
    except Exception:
        pass  # evidence logging must never break a live read


@mcp.tool()
def snmp_get(device: str, oids: list[str]) -> dict[str, str]:
    """SNMP GET of explicit OIDs (read-only), values keyed by OID with the
    symbolic name appended and decoded with catalog semantics (enum meaning,
    units) when the knowledge catalog is present. This — not snmp_walk — is
    the reliable way to poll families whose agent has a sparse GETNEXT chain
    (minid)."""
    s = _snmp()
    dev = get_device(device)
    if not oids:
        raise ToolError("pass at least one OID, e.g. ['1.3.6.1.2.1.1.1.0']")
    if len(oids) > 64:
        raise ToolError("max 64 OIDs per call — split larger polls")
    raw = s.snmp_get(dev, oids)
    audit("snmp_get", device, detail=f"{len(oids)} oids")
    answered = sum(1 for v in raw.values() if not v.startswith(("ERROR", "PDU-ERROR")))
    _log_observation(dev, "snmp_get", f"{len(oids)} explicit OIDs", f"{answered} answered")
    return {f"{oid}  ({s.resolve_name(oid)})": _decorate(oid, val) for oid, val in raw.items()}


@mcp.tool()
def snmp_walk(device: str, oid: str, max_rows: int = 200) -> dict:
    """SNMP GETNEXT walk within a subtree (read-only), row-capped. Returns
    symbolic rows plus explicit completeness flags — `capped` means MORE data
    exists beyond max_rows, and RAD agents signal end-of-view by silence
    (reported in `note`, not an error). On minid prefer snmp_get: its agent's
    NEXT chain is sparse and walks under-report."""
    s = _snmp()
    dev = get_device(device)
    max_rows = max(1, min(int(max_rows), 2000))
    rows, capped, note = s.snmp_walk(dev, oid, max_rows)
    audit("snmp_walk", device, detail=f"{oid} ({len(rows)} rows)")
    _log_observation(dev, "snmp_walk", f"walk {oid}",
                     f"{len(rows)} rows{' (capped)' if capped else ''}{'; ' + note if note else ''}")
    return {
        "root": f"{oid}  ({s.resolve_name(oid)})",
        "rows": {f"{o}  ({s.resolve_name(o)})": _decorate(o, v) for o, v in rows},
        "row_count": len(rows),
        "capped": capped,
        "note": note or ("complete" if not capped else ""),
    }


@mcp.tool()
def snmp_build_poll_plan(refs: list[str], family: str, max_rows_per_walk: int = 200) -> dict:
    """Build an OFFLINE SNMP poll plan from concepts/symbols/OIDs for a target
    family (Phase 4). Resolves refs against the knowledge catalog, expands
    tables, excludes non-readable and notification-only objects, and honors
    the family's live-verified transport profile (version, GET-vs-walk
    strategy, end-of-view behavior). NEVER contacts a device — show the
    returned operations to the user and ask the confirmation question before
    executing them via snmp_get/snmp_walk."""
    k = _knowledge()
    if not refs:
        raise ToolError("pass at least one concept/symbol/OID, e.g. ['erpTable', 'ERP R-APS counters']")
    out = _kcall(k.build_poll_plan, refs, family, max_rows_per_walk=max_rows_per_walk)
    audit("snmp_build_poll_plan", "-", detail=f"{family}: {len(refs)} refs")
    return out


# --------------------------------------------------- knowledge catalog (offline)
# Phase 3 of references/snmp-mib-catalog-design.md: OFFLINE tools over the
# read-only rad-knowledge.sqlite semantic MIB catalog. They never contact a
# device (no confirmation gate needed) and are available to RO and RW tokens
# alike. MIB-DEFINED != device-implemented — answers carry capability
# evidence separately.

def _knowledge():
    from . import knowledge as k
    return k


def _kcall(fn, *args, **kw):
    k = _knowledge()
    try:
        return fn(*args, **kw)
    except k.KnowledgeUnavailable as exc:
        raise ToolError(str(exc)) from exc


@mcp.tool()
def knowledge_status() -> dict:
    """Knowledge-catalog status (offline): build identity, corpus hash, object
    counts, source roots, last build's validation summary."""
    k = _knowledge()
    out = _kcall(k.status)
    audit("knowledge_status", "-")
    return out


@mcp.tool()
def mib_search(query: str, module: str = "", kind: str = "", oid_prefix: str = "",
               family: str = "", limit: int = 25) -> dict:
    """Search the semantic MIB catalog (offline) by concept, symbol, or OID.
    Deterministic ranking: exact > prefix/OID-subtree > full-text (descriptions
    + enum labels). Optional filters: module, kind (scalar/table/row/column/
    notification), oid_prefix; family adds that family's verified transport
    profile to the answer. Results are MIB-defined objects — NOT proof a
    family implements them."""
    k = _knowledge()
    out = _kcall(k.search, query, module=module, kind=kind,
                 oid_prefix=oid_prefix, family=family, limit=limit)
    audit("mib_search", "-", detail=query[:80])
    return out


@mcp.tool()
def mib_describe(ref: str) -> dict:
    """Full semantic definition of one MIB object (offline) by symbol,
    MODULE::symbol, or numeric OID: syntax + textual convention + display
    hint, access, description, enums, ranges, units, default, table/index
    context, augments, notification payload, module revision, source
    provenance (file + sha256), and live capability evidence when any exists."""
    k = _knowledge()
    out = _kcall(k.describe, ref)
    audit("mib_describe", "-", detail=ref[:80])
    return out


@mcp.tool()
def mib_table(ref: str) -> dict:
    """Complete table model (offline) for a table/row/column reference:
    table+entry OIDs, ordered indexes (with types and IMPLIED flags),
    instance-encoding rule, every column with access/type/units/enums, and
    suggested identifying columns — everything needed to plan a poll."""
    k = _knowledge()
    out = _kcall(k.table_model, ref)
    audit("mib_table", "-", detail=ref[:80])
    return out


@mcp.tool()
def mib_notifications(query: str, module: str = "", limit: int = 20) -> dict:
    """Find notifications/traps in the catalog (offline) by concept, with each
    notification's ordered payload objects."""
    k = _knowledge()
    out = _kcall(k.notifications, query, module=module, limit=limit)
    audit("mib_notifications", "-", detail=query[:80])
    return out


@mcp.tool()
def cli_search(query: str, family: str = "", context: str = "", limit: int = 15) -> dict:
    """Search the harvested CLI `?`-help knowledge (offline, Phase 5 — the
    served-mode equivalent of grepping cli-reference-<family>.md). Ranking:
    exact context/prefix > context prefix > full-text over help bodies.
    ALWAYS pass `family` when known — commands are family-specific."""
    k = _knowledge()
    out = _kcall(k.cli_search, query, family=family, context=context, limit=limit)
    audit("cli_search", "-", detail=f"{family}:{query[:60]}")
    return out


@mcp.tool()
def manual_search(query: str, family: str = "", limit: int = 10,
                  include_refdocs: bool = True) -> dict:
    """Search the ingested user manuals per-section (offline, Phase 5 — the
    served-mode equivalent of grepping manual-<family>/). Returns bounded
    excerpts with chapter/section/page provenance; optionally also searches
    the curated reference docs (verified-commands, snmp-support,
    known-limitations, snmp capability maps). Concepts/limits live here —
    exact syntax comes from cli_search."""
    k = _knowledge()
    out = _kcall(k.manual_search, query, family=family, limit=limit,
                 include_refdocs=include_refdocs)
    audit("manual_search", "-", detail=f"{family}:{query[:60]}")
    return out


@mcp.tool()
def datasheet_search(query: str, family: str = "", product: str = "",
                     kind: str = "", limit: int = 10) -> dict:
    """Search the ingested product datasheets per subject section (offline —
    the served-mode equivalent of grepping references/datasheets/). Third
    knowledge domain: hardware specs, interfaces, timing options, ordering and
    product variants live HERE; concepts/procedures in manual_search; exact
    command syntax in cli_search. Results carry `kind`: 'system' is a
    standalone device, 'card' a plug-in module for its family's chassis (e.g.
    every mp4100 card), 'accessory' non-traffic hardware. Filter by `family`
    (inventory family), `product` (datasheet slug, see rad://datasheet), or
    `kind`."""
    k = _knowledge()
    out = _kcall(k.datasheet_search, query, family=family, product=product,
                 kind=kind, limit=limit)
    audit("datasheet_search", "-", detail=f"{family or product or '*'}:{query[:60]}")
    return out


# ---------------------------------------------------------------- resources

REPO_ROOT = Path(__file__).resolve().parents[2]
REFERENCE_DIR = REPO_ROOT / "skills" / "rad-cli-operations" / "references"


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


# -------------------------------------------------------------------- write

if WRITE_TOOLS_ENABLED:

    @mcp.tool()
    def add_device(
        name: str,
        host: str,
        family: str,
        transport: str = "ssh",
        port: int | None = None,
        groups: list[str] | None = None,
        description: str = "",
        overwrite: bool = False,
    ) -> dict:
        """Register a new device in the inventory (facts only — credentials
        are set separately via set_device_credentials). Write-gated: stdio by
        default, or HTTP with a write-scoped token. `family` must be a driver
        rad-mcp already ships
        (see list_devices/drivers — e.g. 'secflow', 'etx1p', 'etx2'); this
        does not add support for a new CLI dialect, only a new unit of an
        existing one.

        `transport` is 'ssh' (default) or 'telnet' — same CLI over either.
        `port` defaults to the transport's standard port (22 for ssh, 23 for
        telnet) when omitted. Prefer ssh when the unit offers both; telnet
        sends credentials and config in cleartext, so reserve it for units
        (or lab setups) where SSH is unavailable.

        After this call: set credentials in server/.env as
        RAD_MCP_<NAME>_USERNAME / RAD_MCP_<NAME>_PASSWORD (name upper-cased,
        dashes -> underscores) — or rely on the global RAD_MCP_USERNAME /
        RAD_MCP_PASSWORD if this device shares them. NEW .env keys are picked
        up automatically on the next connection (no restart); only CHANGING
        an already-loaded key still needs a server restart. Then run
        test_connectivity, then health_check.
        """
        _require_write_scope()
        get_driver(family)  # raises with the valid-family list if unknown
        inv_path = add_device_entry(
            name, host, family, transport=transport, port=port,
            groups=groups or [], description=description, overwrite=overwrite,
        )
        audit("add_device", name,
              detail=f"host={host} family={family} transport={transport} overwrite={overwrite}")
        env_prefix = "RAD_MCP_" + name.upper().replace("-", "_")
        return {
            "status": f"Added '{name}' to {inv_path.name}.",
            "device": get_device(name).summary(),
            "next_steps": [
                f"Set its credentials with set_device_credentials('{name}', "
                "<username>, <password>) — the server writes them to its own "
                "server/.env; they are effective immediately. (Alternative for "
                f"someone on the server host: put {env_prefix}_USERNAME / "
                f"{env_prefix}_PASSWORD in server/.env by hand, or rely on the "
                "global RAD_MCP_USERNAME/RAD_MCP_PASSWORD if shared.)",
                f"Run test_connectivity('{name}') then health_check('{name}').",
                f"If '{family}'s CLI reference is missing this unit's context "
                f"or firmware differs from what was harvested, run "
                f"/rad-harvest {name} to build/refresh it.",
            ],
        }

    @mcp.tool()
    def set_device_credentials(name: str, username: str = "", password: str = "",
                               snmp_community: str = "", snmp_v1_community: str = "",
                               snmp_v1_communities: str = "", snmp_v3_user: str = "",
                               snmp_v3_auth_key: str = "", snmp_v3_priv_key: str = "",
                               snmp_v3_auth_protocol: str = "", snmp_v3_priv_protocol: str = "") -> dict:
        """Set (or rotate) an inventory device's secrets — CLI login and/or
        SNMP communities/USM keys. The server writes the RAD_MCP_<NAME>_* keys
        into its OWN server/.env — this is how secrets are managed when the
        server runs on another host, where clients cannot reach that file.
        Effective immediately on the next connection, including rotation (no
        restart needed via this path). The device must already exist
        (add_device first).

        Provide only what you're setting: `username`+`password` (always as a
        pair) for the CLI; `snmp_community` (v2c), `snmp_v1_community` (v1),
        `snmp_v1_communities` (v1 CSV fallback list, tried left->right), or
        the `snmp_v3_*` group for SNMPv3.

        SNMPv3 security levels — set only what the level needs:
          noAuthNoPriv: `snmp_v3_user` alone.
          authNoPriv:   + `snmp_v3_auth_key` (>=8 chars); `snmp_v3_auth_protocol`
                        picks md5/sha/sha224/sha256/sha384/sha512 (default sha).
          authPriv:     + `snmp_v3_priv_key` (>=8 chars) on top of auth;
                        `snmp_v3_priv_protocol` picks des/3des/aes/aes192/aes256
                        (default aes). A priv key without an auth key is
                        rejected — SNMPv3 has no privacy-without-auth mode.

        Write-gated like add_device (stdio, or HTTP with a write-scoped
        token). Secrets transit this tool call, so on shared networks use it
        only over TLS (RAD_MCP_TLS_CERT/KEY) or localhost. Values are never
        echoed back, and the audit log records only which keys changed.
        """
        _require_write_scope()
        res = _set_device_credentials(
            name, username, password, snmp_community=snmp_community,
            snmp_v1_community=snmp_v1_community,
            snmp_v1_communities=snmp_v1_communities, snmp_v3_user=snmp_v3_user,
            snmp_v3_auth_key=snmp_v3_auth_key, snmp_v3_priv_key=snmp_v3_priv_key,
            snmp_v3_auth_protocol=snmp_v3_auth_protocol, snmp_v3_priv_protocol=snmp_v3_priv_protocol)
        audit("set_device_credentials", name,
              detail=f"keys {'+'.join(res['created'] + res['replaced'])} (values redacted)")
        action = "rotated" if res["replaced"] else "created"
        changed = ", ".join(k.removeprefix(res["prefix"] + "_")
                            for k in res["created"] + res["replaced"])
        steps = [f"Run test_connectivity('{name}') then health_check('{name}')."]
        if any("SNMP" in k for k in res["created"] + res["replaced"]):
            steps.append(f"Verify SNMP with snmp_probe('{name}').")
        return {
            "status": f"Secrets for '{name}' {action} in the server's .env "
                      f"({changed}). Effective immediately.",
            "next_steps": steps,
        }

    @mcp.tool()
    def update_device(
        name: str,
        host: str | None = None,
        family: str | None = None,
        transport: str | None = None,
        port: int | None = None,
        groups: list[str] | None = None,
        description: str | None = None,
    ) -> dict:
        """Update a subset of an existing inventory device's fields (host,
        family, transport, port, groups, description). Omitted parameters
        keep their current value. `transport` is 'ssh' or 'telnet'; when the
        transport changes and the port was the old transport's default, the
        port re-resolves to the new default (22 for ssh, 23 for telnet) —
        pass `port` explicitly to override. Does not touch credentials —
        use set_device_credentials for those. Changing `family` mid-life is
        unusual (normally means
        the entry was misconfigured, not that the hardware changed) — confirm
        with the user before doing that specifically.
        """
        _require_write_scope()
        if family is not None:
            get_driver(family)  # raises with the valid-family list if unknown
        updated = update_device_entry(
            name, host=host, family=family, transport=transport, port=port,
            groups=groups, description=description,
        )
        audit("update_device", name,
              detail=f"host={host} family={family} transport={transport} groups={groups}")
        return {"status": f"Updated '{name}'.", "device": updated.summary()}

    @mcp.tool()
    def remove_device(name: str, confirm: bool = False) -> str:
        """Remove a device from the local inventory. Does not touch the
        device itself or delete any backups/audit history — this only stops
        rad-mcp from knowing about it. Requires confirm=true after the user
        has approved removing this specific device."""
        _require_write_scope()
        if not confirm:
            return "REFUSED: remove_device requires confirm=true after the user has approved removing this device."
        get_device(name)  # raises with the known-devices list if unknown
        remove_device_entry(name)
        audit("remove_device", name)
        return f"Removed '{name}' from the inventory. (Credentials in server/.env, if any, were left in place — remove those manually if no longer needed.)"

    @mcp.tool()
    def stage_config(device: str, lines: list[str], purpose: str) -> dict:
        """Stage configuration lines for review. Nothing is sent to the device.

        Returns a stage_id and a preview. Present the preview to the user and
        only call commit_config after they explicitly approve.
        """
        _require_write_scope()
        dev = get_device(device)  # validates the device exists
        # MP candidate-DB families (mp1/mp4100): enforce the verified write
        # recipe — discard-changes FIRST (clears stale candidate edits from
        # earlier sessions, which otherwise fail sanity/commit on config that
        # isn't yours), then sanity-check before commit, commit from root.
        # Verified live on mp-one 2026-07-16; requested as a hard rule.
        if dev.family in ("mp1", "mp4100"):
            toks = [l.strip().lower() for l in lines if l.strip()]
            first_real = next((t for t in toks if t != "exit all"), "")
            problems = []
            if first_real != "discard-changes":
                problems.append("BEGIN with 'discard-changes' (after an optional leading 'exit all')")
            if "sanity-check" not in toks:
                problems.append("include 'sanity-check' after the config lines (must report OK)")
            if "commit" not in toks:
                problems.append("include 'commit' (run from root — after an 'exit all', never inside a new object's $ context)")
            elif "sanity-check" in toks and toks.index("sanity-check") > toks.index("commit"):
                problems.append("put 'sanity-check' BEFORE 'commit'")
            if problems:
                raise ToolError(
                    f"REFUSED: {dev.family} uses the candidate-DB model; every staged "
                    "sequence must follow the verified MP write recipe — "
                    "discard-changes -> <config lines> -> exit all -> sanity-check -> "
                    "commit -> save. This sequence must: " + "; ".join(problems)
                )
        stage_id = secrets.token_hex(4)
        _STAGES[stage_id] = {
            "device": dev.name,
            "lines": lines,
            "purpose": purpose,
            "created": datetime.now(timezone.utc).isoformat(),
        }
        audit("stage_config", device, detail=f"{stage_id}: {purpose}")
        return {
            "stage_id": stage_id,
            "device": dev.name,
            "purpose": purpose,
            "preview": lines,
            "next_step": "Show this preview to the user; commit_config(stage_id, confirm=true) only after explicit approval.",
        }

    @mcp.tool()
    def commit_config(stage_id: str, confirm: bool = False) -> str:
        """Apply a staged config after user approval. Auto-backs-up the running config first."""
        _require_write_scope()
        if stage_id not in _STAGES:
            return f"Unknown stage_id '{stage_id}'. Stage the change first with stage_config."
        if not confirm:
            return "REFUSED: commit_config requires confirm=true after the user has approved the staged preview."
        stage = _STAGES[stage_id]
        dev = get_device(stage["device"])
        backup_path = _take_backup(dev)
        transcript = get_backend().push_config(dev, stage["lines"])
        # Only consume the stage once the push has succeeded, so a connection
        # failure can be retried with the same stage_id.
        _STAGES.pop(stage_id, None)
        audit("commit_config", dev.name, detail=f"{stage_id}: {stage['purpose']}\n{transcript}")
        return (
            f"Committed stage {stage_id} to {dev.name}. Pre-commit backup: {backup_path}\n"
            f"--- session transcript ---\n{redact(transcript)}"
        )

    @mcp.tool()
    def save_startup(device: str, confirm: bool = False) -> str:
        """Persist the running configuration to startup (survives reboot)."""
        _require_write_scope()
        if not confirm:
            return "REFUSED: save_startup requires confirm=true after user approval."
        dev = get_device(device)
        driver = get_driver(dev.family)
        out = get_backend().execute(dev, driver.save_command)
        audit("save_startup", device)
        return out or "Saved."

    @mcp.tool()
    def debug_logon_request(device: str, confirm: bool = False) -> dict:
        """Start unlocking a device's hidden `debug` command tree: sends
        `logon debug` and returns the device's numeric key-code challenge.
        This tool does NOT decrypt it — compute the password for the
        returned key_code (however that's done — the algorithm is
        confidential and lives outside this server) and pass it to
        debug_logon_submit to finish.

        The device is left waiting at its `password>` prompt; don't run
        other tools against it until debug_logon_submit (or a failure)
        clears that. The debug tree includes dangerous commands (reboot,
        factory reset, the raw OS shell) — write-gated + confirm=true like
        commit_config.
        """
        _require_write_scope()
        if not confirm:
            return {"status": "REFUSED: debug_logon_request requires confirm=true — this begins unlocking reboot/shell/factory-reset access."}
        dev = get_device(device)
        key_code = get_backend().debug_logon_request(dev)
        audit("debug_logon_request", device, detail="key code issued", ok=True)
        return {
            "key_code": key_code,
            "next_step": f"Compute the password for this key_code, then call "
                         f"debug_logon_submit('{device}', password=<value>, confirm=true).",
        }

    @mcp.tool()
    def debug_logon_submit(device: str, password: str, confirm: bool = False) -> str:
        """Finish a debug_logon_request challenge: submits `password` (the
        value computed for the key_code that call returned) and confirms
        the device is back at its normal CLI prompt, debug mode unlocked.
        The password is never logged."""
        _require_write_scope()
        if not confirm:
            return "REFUSED: debug_logon_submit requires confirm=true."
        dev = get_device(device)
        get_backend().debug_logon_submit(dev, password)
        audit("debug_logon_submit", device, detail="debug mode unlocked", ok=True)
        return f"Debug mode unlocked on {device}."

    @mcp.tool()
    def debug_menu(device: str, commands: list[str], confirm: bool = False,
                   reset: bool = False) -> str:
        """Run commands inside the already-unlocked `debug` tree (call
        debug_logon_request/submit first).

        By default (reset=False) this CONTINUES from wherever the previous
        debug_menu call on this device left off — no re-grounding. Submenu
        trees (mea/alarms/db/...) are family- and FPGA-specific, undocumented,
        and not whitelisted like run_show, so expect to explore them with
        `?` one command at a time (e.g. call 1: ["debug mea"], call 2:
        ["?"], call 3: ["version"] once you see the right subcommand) —
        each call picks up right where the last one left off, so probing
        step by step does NOT cost you your place in the menu. Pass
        reset=True only when you want to abandon the current navigation and
        force `exit all` back to the top RAD CLI first.
        """
        _require_write_scope()
        if not confirm:
            return "REFUSED: debug_menu requires confirm=true."
        dev = get_device(device)
        out = get_backend().debug_menu(dev, commands, reset=reset)
        audit("debug_menu", device, detail=f"reset={reset} " + "\n".join(commands))
        return redact(out)

    @mcp.tool()
    def enter_debug_shell(device: str, confirm: bool = False) -> str:
        """Drop an already-debug_logon'd session into the device's real OS
        shell (VxWorks or Linux, depending on family). Only works for
        families whose driver has debug_shell_enter_cmd/prompt_re populated
        (confirmed on real hardware) — refuses cleanly otherwise. Once
        inside, use debug_shell_command to run raw commands and
        exit_debug_shell to return to the normal CLI.
        """
        _require_write_scope()
        if not confirm:
            return "REFUSED: enter_debug_shell requires confirm=true — this is unrestricted OS-level access."
        dev = get_device(device)
        out = get_backend().enter_debug_shell(dev)
        audit("enter_debug_shell", device)
        return redact(out) or f"Entered debug shell on {device}."

    @mcp.tool()
    def debug_shell_command(device: str, command: str, confirm: bool = False) -> str:
        """Run one raw command inside an already-entered debug OS shell
        (call enter_debug_shell first). No whitelist — this is the device's
        real VxWorks/Linux shell, use with care."""
        _require_write_scope()
        if not confirm:
            return "REFUSED: debug_shell_command requires confirm=true."
        dev = get_device(device)
        out = get_backend().raw_shell_command(dev, command)
        audit("debug_shell_command", device, detail=command)
        return redact(out)

    @mcp.tool()
    def exit_debug_shell(device: str) -> str:
        """Leave the debug OS shell, returning the session to the normal
        RAD CLI. Always safe to call."""
        _require_write_scope()
        dev = get_device(device)
        out = get_backend().exit_debug_shell(dev)
        audit("exit_debug_shell", device)
        return redact(out) or f"Exited debug shell on {device}."


def main() -> None:
    mode = "read-write (staged commits)" if WRITE_TOOLS_ENABLED else "READ-ONLY"
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
              detail=f"v{__version__} {mode} transport={scheme} {host}:{port} (auth required)")
        mcp.run(transport="http", host=host, port=port, uvicorn_config=uvicorn_config)
    else:
        audit("server_start", "-", detail=f"v{__version__} {mode} transport=stdio")
        mcp.run()  # stdio


if __name__ == "__main__":
    main()
