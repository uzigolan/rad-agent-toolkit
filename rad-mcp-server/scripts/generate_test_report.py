#!/usr/bin/env python3
"""
Generate comprehensive test report from the extracted dataset.

This analyzes all 499 test cases without requiring device connectivity:
- Groups by category
- Counts by prompt type
- Compares with Excel test results
- Generates summary report

Usage:
  python scripts/generate_test_report.py

Output:
  tests/eval-etx2-comprehensive-report.md
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parents[1]
OUT_DIR = REPO / "tests"
DATASET_JSON = OUT_DIR / "eval-etx2-full-dataset.json"


def load_dataset() -> list[dict]:
    """Load test cases."""
    if not DATASET_JSON.exists():
        print(f"ERROR: {DATASET_JSON} not found")
        sys.exit(1)
    
    with open(DATASET_JSON, 'r') as f:
        return json.load(f)


def generate_report():
    """Generate comprehensive report."""
    
    print("Loading dataset...")
    cases = load_dataset()
    
    # Statistics
    total = len(cases)
    classic = sum(1 for c in cases if c.get('prompt_type') == 'classic')
    implicit = sum(1 for c in cases if c.get('prompt_type') == 'implicit')
    
    # Group by category
    by_category = defaultdict(lambda: {'total': 0, 'classic': 0, 'implicit': 0})
    for case in cases:
        cat = case.get('category', 'Unknown')
        by_category[cat]['total'] += 1
        if case.get('prompt_type') == 'classic':
            by_category[cat]['classic'] += 1
        else:
            by_category[cat]['implicit'] += 1
    
    # Excel test results
    excel_pass = sum(1 for c in cases if c.get('test3_optimized') == 'PASS')
    excel_fail = sum(1 for c in cases if c.get('test3_optimized') == 'FAIL')
    
    # Build report
    report = f"""# Comprehensive ETX-2 Command Test Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Source:** ETX-2i_Show_Commands_enhanced.xlsx, sheet STR  
**Device:** Raviv-Etx2-Telnet (172.17.163.252:2001)

---

## Executive Summary

This report covers **{total} comprehensive test cases** extracted from {len(set(c['source_row'] for c in cases))} rows in the original Excel spreadsheet.

| Metric | Count |
|--------|-------|
| **Total Test Cases** | {total} |
| **Source Rows** | {len(set(c['source_row'] for c in cases))} |
| **Classic Prompts** | {classic} |
| **Implicit Prompts** | {implicit} |

---

## Prior Test Results (From Excel)

These are the original test results from the spreadsheet, before re-testing:

| Status | Count | % |
|--------|-------|---|
| **PASS** | {excel_pass} | {100*excel_pass//total if total else 0}% |
| **FAIL** | {excel_fail} | {100*excel_fail//total if total else 0}% |

> **Note:** Most rows in the sheet had empty Test3 results, indicating they passed
> in the prior testing cycles. Only a subset was marked FAIL.

---

## Tests by Category

Distribution of test cases across CLI contexts:

| Category | Total | Classic | Implicit | % of Total |
|----------|-------|---------|----------|------------|
"""
    
    for cat in sorted(by_category.keys()):
        stats = by_category[cat]
        pct = 100 * stats['total'] // total if total else 0
        report += f"| {cat:20} | {stats['total']:5} | {stats['classic']:7} | {stats['implicit']:9} | {pct:3}% |\n"
    
    report += f"""
---

## Test Case Details

### Example Test Cases

#### CLASSIC Prompt Examples (direct/explicit language)
"""
    
    # Show some classic examples
    classic_examples = [c for c in cases if c.get('prompt_type') == 'classic'][:3]
    for idx, case in enumerate(classic_examples, 1):
        report += f"""
**{idx}. {case['id']}** (Row {case['source_row']})
- **Category:** {case.get('category', 'N/A')}
- **Context:** `{case.get('cli_path', 'N/A')}`
- **Prompt:** {case.get('prompt', 'N/A')}
- **Expected Command:** `{case.get('expected_cli_command', 'N/A')}`
"""
    
    report += f"""
#### IMPLICIT Prompt Examples (colloquial language)
"""
    
    # Show some implicit examples
    implicit_examples = [c for c in cases if c.get('prompt_type') == 'implicit'][:3]
    for idx, case in enumerate(implicit_examples, 1):
        report += f"""
**{idx}. {case['id']}** (Row {case['source_row']})
- **Category:** {case.get('category', 'N/A')}
- **Context:** `{case.get('cli_path', 'N/A')}`
- **Prompt:** {case.get('prompt', 'N/A')}
- **Expected Command:** `{case.get('expected_cli_command', 'N/A')}`
"""
    
    report += f"""
---

## Testing Strategy

The extracted test cases can be used to:

1. **Skill Evaluation**: Send each prompt to the `rad-cli-operations` skill
   - Verify the skill generates the expected CLI command
   - Test phrasing robustness (classic vs implicit variants)
   - Identify missing or poorly-recognized command contexts

2. **Device Validation**: Execute commands on the live Raviv-Etx2-Telnet device
   - Confirm expected commands work on the actual device
   - Identify firmware version differences
   - Verify CLI reference accuracy vs. running system

3. **Coverage Analysis**: Check against harvested CLI reference
   - Map commands to their context paths
   - Identify missing commands in the reference
   - Verify command syntax accuracy

---

## Implementation Notes

### Prompt Types

- **Classic:** Direct, explicit phrasing of the request
  - Example: "Show all configured services and their current status"
  - Expected to match the original command syntax precisely
  
- **Implicit:** Colloquial, conversational phrasing of the same request
  - Example: "What services are currently running or stopped?"
  - Tests the skill's ability to infer intent from natural language
  - More challenging for AI/ML-based CLI inference

### Command Contexts

Commands are organized by CLI contexts (how the user navigates the menu):
- **Root**: Top-level `ETX-2i>` prompt
- **File**: File management context `ETX-2i>file#`
- **Admin**: Administration context `ETX-2i>admin#`
- **System**: System config context `ETX-2i>config>chassis#`
- **Management**: Management/SNMP context `ETX-2i>config>mngmnt#`
- **Port**: Port configuration context `ETX-2i>config>port#`
- **QoS**: Quality of Service context `ETX-2i>config>qos#`
- **Protection**: Protection/redundancy context `ETX-2i>config>protection#`
- **PWE**: Pseudo-Wire Emulation context `ETX-2i>config>pwe#`
- **OAM**: Operations & Maintenance context `ETX-2i>config>oam#`

---

## Next Steps

1. **Run Skill Tests:**
   ```bash
   python scripts/test_against_skill.py eval-etx2-full-dataset.json
   ```

2. **Run Device Tests (if connectivity available):**
   ```bash
   python scripts/test_device_commands.py
   ```

3. **Generate Coverage Report:**
   ```bash
   python scripts/check_eval_coverage.py
   ```

---

## File Locations

- **Dataset (JSON):** `tests/eval-etx2-full-dataset.json`
- **Dataset (CSV):** `tests/eval-etx2-full-dataset.csv`
- **This Report:** `tests/eval-etx2-comprehensive-report.md`

---

*Report generated by: test framework v1.0*
"""
    
    # Save report
    report_path = OUT_DIR / "eval-etx2-comprehensive-report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✓ Report saved to: {report_path}")
    print(f"\n=== SUMMARY ===")
    print(f"Total test cases: {total}")
    print(f"  - Classic: {classic}")
    print(f"  - Implicit: {implicit}")
    print(f"Categories: {len(by_category)}")
    print(f"\nPrior Excel test results:")
    print(f"  - PASS: {excel_pass}")
    print(f"  - FAIL: {excel_fail}")


if __name__ == '__main__':
    generate_report()
