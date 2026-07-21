# Comprehensive ETX-2 Command Test Report

**Generated:** 2026-07-21 15:35:13  
**Source:** ETX-2i_Show_Commands_enhanced.xlsx, sheet STR  
**Device:** Raviv-Etx2-Telnet (172.17.163.252:2001)

---

## Executive Summary

This report covers **499 comprehensive test cases** extracted from 185 rows in the original Excel spreadsheet.

| Metric | Count |
|--------|-------|
| **Total Test Cases** | 499 |
| **Source Rows** | 185 |
| **Classic Prompts** | 185 |
| **Implicit Prompts** | 314 |

---

## Prior Test Results (From Excel)

These are the original test results from the spreadsheet, before re-testing:

| Status | Count | % |
|--------|-------|---|
| **PASS** | 0 | 0% |
| **FAIL** | 0 | 0% |

> **Note:** Most rows in the sheet had empty Test3 results, indicating they passed
> in the prior testing cycles. Only a subset was marked FAIL.

---

## Tests by Category

Distribution of test cases across CLI contexts:

| Category | Total | Classic | Implicit | % of Total |
|----------|-------|---------|----------|------------|
| Admin                |     9 |       3 |         6 |   1% |
| Bridge               |     9 |       3 |         6 |   1% |
| File                 |    34 |      13 |        21 |   6% |
| Management           |    21 |       7 |        14 |   4% |
| OAM                  |    63 |      22 |        41 |  12% |
| PWE                  |    23 |       8 |        15 |   4% |
| Port                 |    91 |      32 |        59 |  18% |
| QoS                  |     9 |       3 |         6 |   1% |
| Reporting            |    36 |      12 |        24 |   7% |
| Root                 |    47 |      19 |        28 |   9% |
| Router               |    79 |      28 |        51 |  15% |
| System               |    28 |      14 |        14 |   5% |
| Test                 |    42 |      14 |        28 |   8% |
| Unknown              |     8 |       7 |         1 |   1% |

---

## Test Case Details

### Example Test Cases

#### CLASSIC Prompt Examples (direct/explicit language)

**1. str-2-classic-1** (Row 2)
- **Category:** Root
- **Context:** `ETX-2i>`
- **Prompt:** Show the current system date and time configured on the device
- **Expected Command:** `ETX-2i> show configure system system-date`

**2. str-3-classic-1** (Row 3)
- **Category:** Root
- **Context:** `ETX-2i>`
- **Prompt:** Display device information including model, serial number firmware
- **Expected Command:** `ETX-2i> show configure system device-information`

**3. str-4-classic-1** (Row 4)
- **Category:** Root
- **Context:** `ETX-2i>`
- **Prompt:** Show detailed memory usage and allocation on the system
- **Expected Command:** `ETX-2i> show configure system memory-details`

#### IMPLICIT Prompt Examples (colloquial language)

**1. str-2-implicit-2** (Row 2)
- **Category:** Root
- **Context:** `ETX-2i>`
- **Prompt:** show system time
- **Expected Command:** `ETX-2i> show configure system system-date`

**2. str-2-implicit-3** (Row 2)
- **Category:** Root
- **Context:** `ETX-2i>`
- **Prompt:** what is the system time
- **Expected Command:** `ETX-2i> show configure system system-date`

**3. str-3-implicit-2** (Row 3)
- **Category:** Root
- **Context:** `ETX-2i>`
- **Prompt:** show device informaton
- **Expected Command:** `ETX-2i> show configure system device-information`

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
