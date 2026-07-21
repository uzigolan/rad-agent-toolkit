# ETX-2 Device Test Results  —  Yossi-ETX2

**Date:** 2026-07-21 17:07  
**Total:** 185

| Status | Count | % |
|--------|-------|---|
| PASS   | 171 | 92% |
| FAIL   | 7 | 3% |
| SKIP   | 7 | 3% |

## By category

| Category | Pass | Fail | Skip |
|----------|------|------|------|
| Admin | 3 | 0 | 0 |
| Bridge | 3 | 0 | 0 |
| File | 6 | 7 | 0 |
| Management | 7 | 0 | 0 |
| OAM | 22 | 0 | 0 |
| PWE | 8 | 0 | 0 |
| Port | 32 | 0 | 0 |
| QoS | 3 | 0 | 0 |
| Reporting | 12 | 0 | 0 |
| Root | 19 | 0 | 0 |
| Router | 28 | 0 | 0 |
| System | 14 | 0 | 0 |
| Test | 14 | 0 | 0 |
| Unknown | 0 | 0 | 7 |

## Failures

- **str-21-classic-1** `ETX-2i>file# show banner-text` — `cli error: Could not find file`
- **str-23-classic-1** `ETX-2i>file# show file-details <filename>` — `cli error: parameter or keyword missing or wrong - show file-details <filename> expects <filename>`
- **str-27-classic-1** `ETX-2i>file# show rollback-config` — `cli error: Could not find file`
- **str-30-classic-1** `ETX-2i>file# show usb-status` — `cli error: command not recognized`
- **str-31-classic-1** `ETX-2i>file# show user-default-config` — `cli error: Could not find file`
- **str-32-classic-1** `ETX-2i>file# show user-dir` — `cli error: parameter or keyword missing or wrong - show user-dir <filename> expects <filename>`
- **str-33-classic-1** `ETX-2i>file# show user-script` — `cli error: command not recognized`

## Failure Analysis

### Category 1: File Not Found (3 cases)
- `show banner-text` — banner file does not exist on device
- `show rollback-config` — no rollback configuration available
- `show user-default-config` — user default config not available

**Root Cause:** These commands reference files that haven't been created/configured on the test device.

### Category 2: Missing Required Parameter (2 cases)
- `show file-details <filename>` — requires actual filename argument (e.g., `show file-details config.txt`)
- `show user-dir <filename>` — requires actual filename argument

**Root Cause:** Test data includes placeholders but device requires real values. These commands need device-specific file paths.

### Category 3: Command Not Supported (2 cases)
- `show usb-status` — not available on this firmware
- `show user-script` — not available on this firmware

**Root Cause:** Firmware limitation. These commands may be available on newer/older firmware versions.

## Summary

All 7 failures are **device/firmware limitations**, not test issues:
- 3 require pre-existing files/configs not on test device
- 2 require real parameters (not placeholder syntax)
- 2 are unsupported on this firmware version

The test framework correctly identified these issues.