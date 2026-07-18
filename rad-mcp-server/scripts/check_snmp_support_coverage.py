"""Validate SNMP support coverage across all registered families.

Checks that every family registered in server/rad_mcp/drivers/__init__.py has:
1) A block in references/family-profiles.yaml
2) A row in references/snmp-support.md top family table
3) A non-empty versions_verified value in family-profiles.yaml
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

import yaml


REPO = Path(__file__).resolve().parents[1]
DRIVERS_INIT = REPO / "server" / "rad_mcp" / "drivers" / "__init__.py"
FAMILY_PROFILES = REPO / "skills" / "rad-cli-operations" / "references" / "family-profiles.yaml"
SNMP_SUPPORT = REPO / "skills" / "rad-cli-operations" / "references" / "snmp-support.md"


def _driver_families() -> set[str]:
    src = DRIVERS_INIT.read_text(encoding="utf-8")
    mod = ast.parse(src)
    for node in mod.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
            value = node.value
        else:
            continue

        for target in targets:
            if isinstance(target, ast.Name) and target.id == "_DRIVERS":
                if not isinstance(value, ast.Dict):
                    raise RuntimeError("_DRIVERS is not a dict literal")
                families: set[str] = set()
                for key in value.keys:
                    if isinstance(key, ast.Constant) and isinstance(key.value, str):
                        families.add(key.value)
                return families
    raise RuntimeError("Could not find _DRIVERS in drivers/__init__.py")


def _profile_families() -> dict[str, dict]:
    raw = yaml.safe_load(FAMILY_PROFILES.read_text(encoding="utf-8")) or {}
    fams = raw.get("families", {}) or {}
    if not isinstance(fams, dict):
        raise RuntimeError("family-profiles.yaml has invalid 'families' shape")
    return fams


def _snmp_support_families() -> set[str]:
    text = SNMP_SUPPORT.read_text(encoding="utf-8")
    # Top support table rows use: | `family` | ...
    return set(re.findall(r"^\|\s*`([a-z0-9_\-]+)`\s*\|", text, flags=re.MULTILINE))


def main() -> int:
    drivers = _driver_families()
    profiles = _profile_families()
    support_rows = _snmp_support_families()

    errors: list[str] = []

    missing_profiles = sorted(drivers - set(profiles.keys()))
    if missing_profiles:
        errors.append("Missing family-profiles.yaml blocks: " + ", ".join(missing_profiles))

    missing_support = sorted(drivers - support_rows)
    if missing_support:
        errors.append("Missing snmp-support.md family rows: " + ", ".join(missing_support))

    missing_verified: list[str] = []
    for fam in sorted(drivers & set(profiles.keys())):
        val = str((profiles.get(fam) or {}).get("versions_verified", "")).strip()
        if not val:
            missing_verified.append(fam)
    if missing_verified:
        errors.append("Missing versions_verified in family-profiles.yaml: " + ", ".join(missing_verified))

    if errors:
        print("SNMP support coverage check: FAILED")
        for err in errors:
            print("- " + err)
        return 1

    print("SNMP support coverage check: OK")
    print("Families covered:", ", ".join(sorted(drivers)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
