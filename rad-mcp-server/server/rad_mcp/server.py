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
from .drivers import get_driver
from .inventory import add_device_entry, get_device, load_inventory, remove_device_entry, update_device_entry

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
    instructions=(
        "Operate RAD Data Communications devices (ETX-2 family and beyond). "
        "New device not in list_devices yet? Use add_device to register it "
        "(facts only — credentials still go in server/.env, never the tool call). "
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


# -------------------------------------------------------------------- write

if WRITE_TOOLS_ENABLED:

    @mcp.tool()
    def add_device(
        name: str,
        host: str,
        family: str,
        port: int = 22,
        groups: list[str] | None = None,
        description: str = "",
        overwrite: bool = False,
    ) -> dict:
        """Register a new device in the local inventory (facts only — never
        credentials, never registered over shared/remote transport since this
        is a write tool). `family` must be a driver rad-mcp already ships
        (see list_devices/drivers — e.g. 'secflow', 'etx1p', 'etx2'); this
        does not add support for a new CLI dialect, only a new unit of an
        existing one.

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
            name, host, family, port=port, groups=groups or [],
            description=description, overwrite=overwrite,
        )
        audit("add_device", name, detail=f"host={host} family={family} overwrite={overwrite}")
        env_prefix = "RAD_MCP_" + name.upper().replace("-", "_")
        return {
            "status": f"Added '{name}' to {inv_path.name}.",
            "device": {
                "name": name, "host": host, "family": family, "port": port,
                "groups": groups or [], "description": description,
            },
            "next_steps": [
                f"Set credentials in server/.env: {env_prefix}_USERNAME=... and "
                f"{env_prefix}_PASSWORD=... (or rely on the global "
                "RAD_MCP_USERNAME/RAD_MCP_PASSWORD if this device shares them).",
                "New .env keys are picked up automatically on the next "
                "connection — no restart needed. (Only changing an "
                "already-loaded key requires a server restart.)",
                f"Run test_connectivity('{name}') then health_check('{name}').",
                f"If '{family}'s CLI reference is missing this unit's context "
                f"or firmware differs from what was harvested, run "
                f"/rad-harvest {name} to build/refresh it.",
            ],
        }

    @mcp.tool()
    def update_device(
        name: str,
        host: str | None = None,
        family: str | None = None,
        port: int | None = None,
        groups: list[str] | None = None,
        description: str | None = None,
    ) -> dict:
        """Update a subset of an existing inventory device's fields (host,
        family, port, groups, description). Omitted parameters keep their
        current value. Does not touch credentials — those still live only in
        server/.env, update them there directly if they changed. Changing
        `family` mid-life is unusual (normally means the entry was
        misconfigured, not that the hardware changed) — confirm with the user
        before doing that specifically.
        """
        _require_write_scope()
        if family is not None:
            get_driver(family)  # raises with the valid-family list if unknown
        updated = update_device_entry(
            name, host=host, family=family, port=port, groups=groups,
            description=description,
        )
        audit("update_device", name, detail=f"host={host} family={family} groups={groups}")
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
