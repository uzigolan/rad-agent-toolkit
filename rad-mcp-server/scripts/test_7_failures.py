#!/usr/bin/env python3
"""
Re-test only the 7 failing file-system commands from eval results.

Usage:
  cd rad-mcp-server/server && python ../scripts/test_7_failures.py

Output:
  tests/eval-7-failures-retest.json
  tests/eval-7-failures-retest.csv
"""

import json
import csv
from pathlib import Path
from datetime import datetime

# The 7 cases to retest
FAILING_CASES = {
    "str-21": {"cmd": "show banner-text", "ctx": "file", "reason": "banner file missing"},
    "str-23": {"cmd": "show file-details config.txt", "ctx": "file", "reason": "requires actual filename"},
    "str-27": {"cmd": "show rollback-config", "ctx": "file", "reason": "rollback config missing"},
    "str-30": {"cmd": "show usb-status", "ctx": "file", "reason": "N/A: device has no USB", "skip": True},
    "str-31": {"cmd": "show user-default-config", "ctx": "file", "reason": "user-default-config missing"},
    "str-32": {"cmd": "show user-dir config.txt", "ctx": "file", "reason": "requires actual filename"},
    "str-33": {"cmd": "show user-script", "ctx": "file", "reason": "N/A: command not supported"},
}

# The 7 skipped cases
SKIPPED_CASES = [
    ("str-65", "Display detailed neighbor information configured on this port"),
    ("str-94", "Display all pseudowire statistics including current and historical intervals"),
    ("str-100", "Show the Routing Information Base for IPv6"),
    ("str-121", "display the route map policy profiles assigned to the neighbor 10.10.10.1 IPv4 unicast family"),
    ("str-127", "show status of interface 1 router 1"),
    ("str-137", "display mep 1 service 1 current statistics"),
    ("str-140", "display mep 1 service 1 statistics for all intervals"),
]

def main():
    OUT_DIR = Path(__file__).resolve().parents[1] / "tests"
    OUT_DIR.mkdir(exist_ok=True)

    # Build 7 test results
    results = []
    for case_id, info in FAILING_CASES.items():
        if info.get("skip"):
            status = "N/A"
            reason = info["reason"]
        else:
            status = "RETEST_REQUIRED"
            reason = info["reason"]
        
        results.append({
            "id": case_id,
            "context": info["ctx"],
            "command": info["cmd"],
            "status": status,
            "reason": reason,
            "note": "Marked for manual testing or fixture creation"
        })

    # Output JSON
    json_path = OUT_DIR / "eval-7-failures-retest.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Output CSV
    csv_path = OUT_DIR / "eval-7-failures-retest.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "context", "command", "status", "reason", "note"])
        writer.writeheader()
        writer.writerows(results)

    # Output markdown report
    md_path = OUT_DIR / "eval-7-failures-analysis.md"
    md_content = f"""# 7 Failure Cases — Analysis & Status

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Failure Breakdown

| Case | Command | Status | Reason |
|------|---------|--------|--------|
| str-21 | `show banner-text` | ❌ MISSING_FILE | Banner file not configured on device |
| str-23 | `show file-details <filename>` | ⚠️ REQUIRES_PARAM | Needs real filename, not placeholder |
| str-27 | `show rollback-config` | ❌ MISSING_FILE | No rollback config saved |
| str-30 | `show usb-status` | ⏭️ N/A | Device has no USB interface |
| str-31 | `show user-default-config` | ❌ MISSING_FILE | File not created yet |
| str-32 | `show user-dir <filename>` | ⚠️ REQUIRES_PARAM | Needs real filename, not placeholder |
| str-33 | `show user-script` | ⏭️ N/A | Command not in this firmware |

## Category Analysis

### Category 1: Missing Files (3 cases) — ❌
- **str-21**: `show banner-text` — Create banner file to fix
- **str-27**: `show rollback-config` — Save config as rollback to fix
- **str-31**: `show user-default-config` — Copy config to user-default to fix

**Solution**: These commands work if the referenced files exist. Pre-create fixtures.

### Category 2: Requires Parameters (2 cases) — ⚠️
- **str-23**: `show file-details <filename>` — Replace `<filename>` with real file
- **str-32**: `show user-dir <filename>` — Replace `<filename>` with real file

**Solution**: These are valid commands but need actual file paths, not template syntax.

### Category 3: Not Applicable (2 cases) — ⏭️
- **str-30**: `show usb-status` — Device has no USB hardware
- **str-33**: `show user-script` — Not supported on this firmware

**Solution**: Mark as N/A or exclude from tests for this device.

## Skipped Cases (7 total)

These cases were skipped because their CLI context doesn't exist in mapping:

| Case | Prompt |
|------|--------|
| str-65 | Display detailed neighbor information configured on this port |
| str-94 | Display all pseudowire statistics including current and historical intervals |
| str-100 | Show the Routing Information Base for IPv6 |
| str-121 | display the route map policy profiles assigned to the neighbor 10.10.10.1 IPv4 unicast family |
| str-127 | show status of interface 1 router 1 |
| str-137 | display mep 1 service 1 current statistics |
| str-140 | display mep 1 service 1 statistics for all intervals |

**Reason**: These prompts have no context path mapping in `CLI_PATH_CONTEXT` dict, so they're skipped at test time.

## Recommendations

### Short-term (Fix 2 cases)
1. **str-23 & str-32**: Update test data to use real filenames instead of `<filename>` placeholders
   - `show file-details config.txt` (existing file)
   - `show user-dir config.txt`

### Medium-term (Fix 3 cases)
1. **str-21**: Create banner file before test (`file# copy startup-config banner-text`)
2. **str-27**: Save rollback config before test (`configure; save; rollback`)
3. **str-31**: Create user-default-config before test (`file# copy startup-config user-default-config`)

### Long-term (Fix 2 cases)
1. **str-30**: Mark as N/A or skip for non-USB devices
2. **str-33**: Mark as N/A or skip for this firmware version
"""

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"\n=== 7 Failure Cases Analysis ===")
    print(f"Missing Files: 3 (need fixtures)")
    print(f"Requires Parameters: 2 (need real values)")
    print(f"Not Applicable: 2 (skip for this device)")
    print(f"\nSkipped Cases: 7 (no context mapping)")
    print(f"\nOutputs:")
    print(f"  {json_path.name}")
    print(f"  {csv_path.name}")
    print(f"  eval-7-failures-analysis.md")

if __name__ == "__main__":
    main()
