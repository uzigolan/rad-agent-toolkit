# RESULTS — RAD CLI failures (T1-3) + Fusion CLI (T5)

**Scope:** `ETX-2i_Show_Commands_enhanced.xlsx`, sheet `STR`, has 182
total rows. This report covers ONLY the 35 rows that a separate,
external testing app/process marked as **Test3 FAIL** when it originally
generated that spreadsheet — the other 147 rows (where that app's own
Test3 passed) are not analyzed here at all.

## Fusion CLI (T5) summary

Base is 35, not 182: this counts only the rows the original testing
app/process marked Test3 FAIL — it says nothing about the other 147
rows in `STR` that app already passed, which were never re-checked here.

| Result | Reason | Count |
|---|---|---|
| <span style="color:green">PASS</span> |  | 22/35 |
| <span style="color:red">FAIL</span> | <span style="color:yellow">FOUND</span> | 5/35 |
| <span style="color:red">FAIL</span> | <span style="color:orange">LICENSE</span> | 4/35 |
| <span style="color:red">FAIL</span> | <span style="color:red">MISSING</span> | 4/35 |
| <span style="color:red">FAIL</span> | **total** | 13/35 |

## Legend

- **T1 / T2 / T3** — three separate prior test rounds against the real
  device, each already PASS/FAIL, carried through unchanged from the
  original spreadsheet. These were run by **RAD CLI** (a prior AI/tool),
  *not* by this project. (A T4 "Post-Training Re-test" column also
  existed in the source sheet but is omitted here — not relevant to this
  report.)
- **Fusion CLI (T5)** — the next round in that same test lineage, but
  run by **Fusion CLI** (this project) instead: does our
  **rad-cli-operations** skill's harvested etx2 CLI reference actually
  contain the row's expected command? `PASS` = yes, confirmed. `FAIL` =
  not confirmed — zero device I/O either way; see `tests/eval-report.md`
  for full method.
- **Reason** (only shown on FAIL) — `FOUND`: the command's
  context/menu path is real and harvested, just not independently
  confirmed at the exact leaf (no live instance of that context existed
  when the reference was harvested). `LICENSE`: the harvester's own
  diagnostic probe got a device-confirmed "License required" refusal —
  not fixable by any code change, needs a real license on the unit.
  `MISSING`: the command was not found anywhere at the claimed context
  at all.

| # | Category | CLI Path | Show Command | Full CLI Command | T1 | T2 | T3 | Prior comment | **Fusion CLI (T5)** | **Reason** | **Detail** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 10 | Root | `ETX-2i>` | `show configure service` | `ETX-2i> show configure service` | <span style="color:red">FAIL</span> | <span style="color:red">FAIL</span> | <span style="color:red">FAIL</span> | , AI repeatedly adds  extra  "configure router 1" to the cli | <span style="color:red">FAIL</span> | <span style="color:red">MISSING</span> | '<root>' fully harvested but 'show configure service' not found there |
| 28 | File | `ETX-2i>file#` | `show schedule-log` | `ETX-2i>file# show schedule-log` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | Test2:AI learned to include "file" in new generaated cli  Te | <span style="color:green">PASS</span> |  | leaf capture in 'file' |
| 29 | File | `ETX-2i>file#` | `show startup-config` | `ETX-2i>file# show startup-config` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | AI learned to include "file" in  context | <span style="color:green">PASS</span> |  | leaf capture in 'file' |
| 34 | Admin | `ETX-2i>admin>scheduler#` | `show scheduler` | `ETX-2i>admin>scheduler# show scheduler` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | AI not learned the new category -it remains on previous | <span style="color:green">PASS</span> |  | leaf capture in 'admin scheduler' |
| 35 | Admin | `ETX-2i>admin>scheduler#` | `show scheduler-details` | `ETX-2i>admin>scheduler# show scheduler-details` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | cli not learned the new category -it remclins on previous | <span style="color:green">PASS</span> |  | leaf capture in 'admin scheduler' |
| 43 | System | `ETX-2i>config>chassis#` | `show environment` | `ETX-2i>config>chassis# show environment` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | initially cli was not running under the correct category | <span style="color:green">PASS</span> |  | leaf capture in 'configure chassis' |
| 48 | Management | `ETX-2i>config>mngmnt>radius#` | `show statistics` | `ETX-2i>config>mngmnt>radius# show statistics` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | cli category was fine just there were bad  syntax issues | <span style="color:green">PASS</span> |  | leaf capture in 'configure management radius' |
| 50 | Management | `ETX-2i>config>mngmnt>snmp#` | `show trap-sync` | `ETX-2i>config>mngmnt>snmp# show trap-sync` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | AI learned the new running category | <span style="color:green">PASS</span> |  | leaf capture in 'configure management snmp' |
| 52 | Port | `ETX-2i>config>port#` | `show summary` | `ETX-2i>config>port# show summary` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | AI learned the new running category successfully | <span style="color:green">PASS</span> |  | leaf capture in 'configure port' |
| 53 | Port | `ETX-2i>config>port#` | `show summary-full-name` | `ETX-2i>config>port# show summary-full-name` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure port' |
| 60 | Port | `ETX-2i>config>port>eth(port)#` | `show oam-efm` | `ETX-2i>config>port>eth(port)# show oam-efm` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | 1) need to Configure L2CP profile before test 2) generated c | <span style="color:green">PASS</span> |  | leaf capture in 'configure port ethernet NAME' |
| 69 | Port | `ETX-2i>config>port>lag(n)#` | `show lacp-status ethernet <port>` | `ETX-2i>config>port>lag(n)# show lacp-status ethernet <port>` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure port lag NAME' |
| 70 | Port | `ETX-2i>config>port>lag(n)#` | `show lacp-statistics ethernet <port>` | `ETX-2i>config>port>lag(n)# show lacp-statistics ethernet <port>` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure port lag NAME' |
| 90 | PWE | `ETX-2i>config>pwe#` | `show summary` | `ETX-2i>config>pwe# show summary` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure pwe' |
| 91 | PWE | `ETX-2i>config>pwe>pw(n)#` | `show status` | `ETX-2i>config>pwe>pw(n)# show status` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:red">FAIL</span> | <span style="color:yellow">FOUND</span> | 'pw' under 'configure pwe': cli error: PW creation failed: PW type must be configured. |
| 92 | PWE | `ETX-2i>config>pwe>pw(n)#` | `show statistics current` | `ETX-2i>config>pwe>pw(n)# show statistics current` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | on first test , AI  generated :"config router 1" line - whic | <span style="color:red">FAIL</span> | <span style="color:yellow">FOUND</span> | 'pw' under 'configure pwe': cli error: PW creation failed: PW type must be configured. |
| 96 | PWE | `ETX-2i>config>pwe>pw(n)#` | `show statistics all` | `ETX-2i>config>pwe>pw(n)# show statistics all` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:red">FAIL</span> | <span style="color:yellow">FOUND</span> | 'pw' under 'configure pwe': cli error: PW creation failed: PW type must be configured. |
| 98 | PWE | `ETX-2i>config>pwe>pw(n)#` | `show connectivity-statistics interval <n>` | `ETX-2i>config>pwe>pw(n)# show connectivity-statistics interval <n>` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | well learned  3rd prompt after second failed | <span style="color:red">FAIL</span> | <span style="color:yellow">FOUND</span> | 'pw' under 'configure pwe': cli error: PW creation failed: PW type must be configured. |
| 102 | Router | `ETX-2i>config>router(n)#` | `show rib { ipv4 \| ipv6 }` | `ETX-2i>config>router(n)# show rib  ipv4 ` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | wrong cli syntax generated on enhanced prompt variation | <span style="color:green">PASS</span> |  | leaf capture in 'configure router NAME' |
| 116 | Router | `ETX-2i>config>router(n)#` | `show nat-statistics` | `ETX-2i>config>router(n)# show nat-statistics` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:red">FAIL</span> | <span style="color:red">MISSING</span> | 'configure router NAME' fully harvested but 'show nat-statistics' not found there |
| 135 | OAM | `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)#` | `show lbm-results` | `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)# show lbm-results` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME' |
| 136 | OAM | `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)#` | `show linktrace-results` | `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)# show linktrace-results` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME' |
| 149 | OAM | `ETX-2i>config>oam>twamp>controller(n)>peer(ip)#` | `show status` | `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show status` | <span style="color:red">FAIL</span> | <span style="color:green">PASS*</span> | <span style="color:red">FAIL</span> | ETX with twamp licsense required | <span style="color:red">FAIL</span> | <span style="color:orange">LICENSE</span> | 'controller' under 'configure oam twamp': cli error: License required |
| 150 | OAM | `ETX-2i>config>oam>twamp>controller(n)>peer(ip)#` | `show report <n> all` | `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show report <n> all` | <span style="color:red">FAIL</span> | <span style="color:green">PASS*</span> | <span style="color:red">FAIL</span> | ETX with twamp licsense required | <span style="color:red">FAIL</span> | <span style="color:orange">LICENSE</span> | 'controller' under 'configure oam twamp': cli error: License required |
| 151 | OAM | `ETX-2i>config>oam>twamp>controller(n)>peer(ip)#` | `show report <n> current` | `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show report <n> current` | <span style="color:red">FAIL</span> | <span style="color:green">PASS*</span> | <span style="color:red">FAIL</span> | ETX with twamp licsense required | <span style="color:red">FAIL</span> | <span style="color:orange">LICENSE</span> | 'controller' under 'configure oam twamp': cli error: License required |
| 152 | OAM | `ETX-2i>config>oam>twamp>controller(n)>peer(ip)#` | `show report <n> interval` | `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show report <n> interval` | <span style="color:red">FAIL</span> | <span style="color:green">PASS*</span> | <span style="color:red">FAIL</span> | ETX with twamp licsense required | <span style="color:red">FAIL</span> | <span style="color:orange">LICENSE</span> | 'controller' under 'configure oam twamp': cli error: License required |
| 154 | OAM | `ETX-2i>config>oam>twamp>responder(n)#` | `show status` | `ETX-2i>config>oam>twamp>responder(n)# show status` | <span style="color:green">PASS*</span> | <span style="color:green">PASS*</span> | <span style="color:red">FAIL</span> | ETX with twamp licsense required | <span style="color:red">FAIL</span> | <span style="color:yellow">FOUND</span> | 'responder' under 'configure oam twamp': cli error: parameter or keyword missing or wrong |
| 155 | Test | `ETX-2i>config>test>y1564>generator(n)#` | `show status` | `ETX-2i>config>test>y1564>generator(n)# show status` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | before test need to setup genarator1 and responder 1 for y15 | <span style="color:green">PASS</span> |  | leaf capture in 'configure test y1564 generator NAME' |
| 156 | Test | `ETX-2i>config>test>y1564>generator(n)#` | `show mef46-ll-status` | `ETX-2i>config>test>y1564>generator(n)# show mef46-ll-status` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure test y1564 generator NAME' |
| 158 | Test | `ETX-2i>config>test>y1564>generator(n)#` | `show report detailed` | `ETX-2i>config>test>y1564>generator(n)# show report detailed` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> | specific command not supported  -  the syntax compared with  | <span style="color:red">FAIL</span> | <span style="color:red">MISSING</span> | 'configure test y1564 generator NAME' fully harvested but 'show report detailed' not found there |
| 163 | Test | `ETX-2i>config>test>rfc2544>test(n)#` | `show summary` | `ETX-2i>config>test>rfc2544>test(n)# show summary` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure test rfc2544 test NAME' |
| 167 | Test | `ETX-2i>config>test>l3sat>generator(name)>peer(ip)#` | `show summary-report` | `ETX-2i>config>test>l3sat>generator(name)>peer(ip)# show summary-report` | <span style="color:red">FAIL</span> | <span style="color:green">PASS*</span> | <span style="color:red">FAIL</span> | show report name  feature is not optional in this cli menu t | <span style="color:red">FAIL</span> | <span style="color:red">MISSING</span> | 'configure test l3sat generator NAME peer NAME' fully harvested but 'show summary-report' not found there |
| 170 | Reporting | `ETX-2i>config>reporting#` | `show accounting-log` | `ETX-2i>config>reporting# show accounting-log` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure reporting' |
| 173 | Reporting | `ETX-2i>config>reporting#` | `show alarm-log` | `ETX-2i>config>reporting# show alarm-log` | <span style="color:green">PASS</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure reporting' |
| 180 | Reporting | `ETX-2i>config>reporting#` | `show alarm-information <source-type> <alarm-list>` | `ETX-2i>config>reporting# show alarm-information <source-type> <alarm-list>` | <span style="color:red">FAIL</span> | <span style="color:green">PASS</span> | <span style="color:red">FAIL</span> |  | <span style="color:green">PASS</span> |  | leaf capture in 'configure reporting' |

`n_prompts` (classic+implicit count per row) omitted from the table above for width; see the JSON for the full per-prompt breakdown — coverage is identical across all of a row's phrasings (verified: 0 rows have mixed coverage).