#!/usr/bin/env python3
"""
Test all extracted prompts against the Raviv-Etx2-Telnet device.

This script:
1. Loads test cases from eval-etx2-full-dataset.json
2. Connects to Raviv-Etx2-Telnet device via telnet (port 2001)
3. For each test case, attempts to execute the expected command
4. Records pass/fail results
5. Generates comprehensive report

Usage:
  python scripts/test_device_commands.py

Output:
  tests/eval-etx2-device-results.json
  tests/eval-etx2-device-results.csv
  tests/eval-etx2-device-report.md
"""
from __future__ import annotations

import csv
import json
import re
import sys
import time
import socket
from datetime import datetime
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]          # rad-mcp-server/
OUT_DIR = REPO / "tests"
DATASET_JSON = OUT_DIR / "eval-etx2-full-dataset.json"

# Device config (from inventory.yaml: Raviv-Etx2-Telnet)
DEVICE_HOST = "172.17.163.252"
DEVICE_PORT = 2001
DEVICE_TIMEOUT = 5
COMMAND_TIMEOUT = 2


def load_test_cases() -> list[dict]:
    """Load test cases from JSON."""
    if not DATASET_JSON.exists():
        print(f"ERROR: {DATASET_JSON} not found")
        print(f"Run: python scripts/test_all_commands_on_device.py")
        sys.exit(1)
    
    with open(DATASET_JSON, 'r', encoding='utf-8') as f:
        cases = json.load(f)
    
    print(f"Loaded {len(cases)} test cases")
    return cases


class SimpleClient:
    """Simple telnet-like client for socket-based connection."""
    
    def __init__(self, host: str, port: int, timeout: float = 5):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(timeout)
        self.sock.connect((host, port))
    
    def read_very_eager(self) -> bytes:
        """Read available data without blocking."""
        try:
            return self.sock.recv(4096)
        except socket.timeout:
            return b''
    
    def write(self, data: bytes):
        """Send data."""
        self.sock.sendall(data)
    
    def close(self):
        """Close connection."""
        try:
            self.sock.close()
        except:
            pass


def connect_device() -> SimpleClient | None:
    """Connect to device via telnet."""
    try:
        print(f"\nConnecting to {DEVICE_HOST}:{DEVICE_PORT}...")
        tn = SimpleClient(DEVICE_HOST, DEVICE_PORT, timeout=DEVICE_TIMEOUT)
        
        # Read initial prompt
        time.sleep(0.5)
        output = tn.read_very_eager().decode('utf-8', errors='ignore')
        print(f"Device prompt: {output.strip()[-50:] if output else '(no output)'}")
        
        return tn
    except Exception as e:
        print(f"ERROR: Could not connect to device: {e}")
        return None


def send_command(tn: SimpleClient, cmd: str) -> str:
    """Send a command and return output."""
    try:
        # Send command
        tn.write(f"{cmd}\n".encode('utf-8'))
        
        # Wait for response
        time.sleep(COMMAND_TIMEOUT)
        output = tn.read_very_eager().decode('utf-8', errors='ignore')
        
        return output
    except Exception as e:
        return f"ERROR: {e}"


def parse_cli_command(cmd_str: str) -> str | None:
    """Extract just the command part from 'ETX-2i> show ...' format."""
    if not cmd_str:
        return None
    
    # Remove device prompt prefix
    # e.g. "ETX-2i> show configure service" -> "show configure service"
    match = re.search(r'>(.*?)$', cmd_str, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    return cmd_str.strip()


def test_case(tn: SimpleClient, case: dict) -> dict:
    """Test a single case on the device."""
    expected_cmd = case.get('expected_cli_command', '')
    
    if not expected_cmd:
        return {
            **case,
            'device_test_result': 'SKIP',
            'device_test_reason': 'No expected command',
            'device_output': '',
            'tested_at': datetime.now().isoformat(),
        }
    
    # Parse command
    cmd = parse_cli_command(expected_cmd)
    
    if not cmd:
        return {
            **case,
            'device_test_result': 'SKIP',
            'device_test_reason': 'Could not parse command',
            'device_output': '',
            'tested_at': datetime.now().isoformat(),
        }
    
    try:
        # Send command and get output
        output = send_command(tn, cmd)
        
        # Check for error patterns
        errors = [
            'Invalid command',
            'syntax error',
            '# cli error',
            'Unknown command',
        ]
        
        result = 'PASS'
        reason = 'Command executed'
        
        for err in errors:
            if err.lower() in output.lower():
                result = 'FAIL'
                reason = f'Error: {err}'
                break
        
        return {
            **case,
            'device_test_result': result,
            'device_test_reason': reason,
            'device_output': output[:500],  # First 500 chars
            'tested_at': datetime.now().isoformat(),
        }
    
    except Exception as e:
        return {
            **case,
            'device_test_result': 'FAIL',
            'device_test_reason': f'Exception: {str(e)}',
            'device_output': '',
            'tested_at': datetime.now().isoformat(),
        }


def run_tests():
    """Run all tests against the device."""
    print("=== TEST ALL COMMANDS ON RAVIV-ETX2-TELNET DEVICE ===\n")
    
    # Load test cases
    cases = load_test_cases()
    
    # Connect to device
    tn = connect_device()
    if not tn:
        print("\nERROR: Could not connect to device. Aborting tests.")
        sys.exit(1)
    
    # Run tests
    print(f"\nTesting {len(cases)} cases...")
    results = []
    
    for idx, case in enumerate(cases, 1):
        if idx % 50 == 0:
            print(f"  [{idx}/{len(cases)}] {case['id']}")
        
        result = test_case(tn, case)
        results.append(result)
        
        # Pause between commands
        time.sleep(0.1)
    
    # Disconnect
    try:
        tn.close()
    except:
        pass
    
    # Save results
    save_results(results)
    
    return results


def save_results(results: list[dict]) -> None:
    """Save results to JSON and CSV."""
    
    # Save JSON
    json_path = OUT_DIR / "eval-etx2-device-results.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved results to {json_path}")
    
    # Save CSV
    csv_path = OUT_DIR / "eval-etx2-device-results.csv"
    if results:
        # Include only key fields for CSV
        csv_fields = [
            'id', 'source_row', 'category', 'prompt_type', 'prompt',
            'expected_cli_command', 'device_test_result', 'device_test_reason'
        ]
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=csv_fields)
            writer.writeheader()
            for result in results:
                row = {k: result.get(k, '') for k in csv_fields}
                writer.writerow(row)
        print(f"Saved to {csv_path}")
    
    # Generate summary report
    generate_report(results)


def generate_report(results: list[dict]) -> None:
    """Generate markdown report with statistics."""
    
    # Calculate stats
    total = len(results)
    passed = sum(1 for r in results if r.get('device_test_result') == 'PASS')
    failed = sum(1 for r in results if r.get('device_test_result') == 'FAIL')
    skipped = sum(1 for r in results if r.get('device_test_result') == 'SKIP')
    
    # Group by category and result
    by_category = {}
    for result in results:
        cat = result.get('category', 'Unknown')
        test_result = result.get('device_test_result', 'UNKNOWN')
        
        if cat not in by_category:
            by_category[cat] = {'PASS': 0, 'FAIL': 0, 'SKIP': 0, 'total': 0}
        
        by_category[cat][test_result] += 1
        by_category[cat]['total'] += 1
    
    # Generate report
    report = f"""# ETX-2 Device Test Results — All 499 Commands

**Device:** Raviv-Etx2-Telnet (172.17.163.252:2001)  
**Test Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Total Cases:** {total}

## Summary

| Status | Count | % |
|--------|-------|---|
| **PASS** | {passed} | {100*passed//total if total else 0}% |
| **FAIL** | {failed} | {100*failed//total if total else 0}% |
| **SKIP** | {skipped} | {100*skipped//total if total else 0}% |

## Results by Category

| Category | Total | Pass | Fail | Skip | Pass % |
|----------|-------|------|------|------|--------|
"""
    
    for cat in sorted(by_category.keys()):
        stats = by_category[cat]
        pass_pct = 100 * stats['PASS'] // stats['total'] if stats['total'] else 0
        report += f"| {cat} | {stats['total']} | {stats['PASS']} | {stats['FAIL']} | {stats['SKIP']} | {pass_pct}% |\n"
    
    report += f"""
## Failed Commands

Top 10 failures:
"""
    
    failures = [r for r in results if r.get('device_test_result') == 'FAIL']
    for idx, fail in enumerate(failures[:10], 1):
        report += f"{idx}. **{fail['id']}** - {fail.get('device_test_reason', 'Unknown error')}\n"
        report += f"   - Command: `{fail.get('expected_cli_command', 'N/A')}`\n"
    
    if len(failures) > 10:
        report += f"\n... and {len(failures) - 10} more failures\n"
    
    # Save report
    report_path = OUT_DIR / "eval-etx2-device-report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Saved report to {report_path}")
    
    # Print summary
    print(f"\n=== RESULTS ===")
    print(f"PASS:  {passed}/{total} ({100*passed//total if total else 0}%)")
    print(f"FAIL:  {failed}/{total} ({100*failed//total if total else 0}%)")
    print(f"SKIP:  {skipped}/{total} ({100*skipped//total if total else 0}%)")


def main():
    try:
        results = run_tests()
        print("\n✓ Tests completed successfully!")
    except KeyboardInterrupt:
        print("\n⚠ Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Tests failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
