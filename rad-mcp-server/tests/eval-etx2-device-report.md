# ETX-2 Device Test Results  —  RavivETX2-SSH

**Date:** 2026-07-21 16:13  
**Total:** 185

| Status | Count | % |
|--------|-------|---|
| PASS   | 105 | 56% |
| FAIL   | 73 | 39% |
| SKIP   | 7 | 3% |

## By category

| Category | Pass | Fail | Skip |
|----------|------|------|------|
| Admin | 3 | 0 | 0 |
| Bridge | 2 | 1 | 0 |
| File | 8 | 5 | 0 |
| Management | 7 | 0 | 0 |
| OAM | 4 | 18 | 0 |
| PWE | 1 | 7 | 0 |
| Port | 19 | 13 | 0 |
| QoS | 3 | 0 | 0 |
| Reporting | 10 | 2 | 0 |
| Root | 19 | 0 | 0 |
| Router | 15 | 13 | 0 |
| System | 7 | 7 | 0 |
| Test | 7 | 7 | 0 |
| Unknown | 0 | 0 | 7 |

## Failures

- **str-21-classic-1** `ETX-2i>file# show banner-text` — _cli error_
- **str-27-classic-1** `ETX-2i>file# show rollback-config` — _cli error_
- **str-30-classic-1** `ETX-2i>file# show usb-status` — _cli error_
- **str-31-classic-1** `ETX-2i>file# show user-default-config` — _cli error_
- **str-32-classic-1** `ETX-2i>file# show user-dir` — _cli error_
- **str-55-classic-1** `ETX-2i>config>port>eth(port)# show status refresh <sec>` — _cli error_
- **str-60-classic-1** `ETX-2i>config>port>eth(port)# show oam-efm` — _cli error_
- **str-61-classic-1** `ETX-2i>config>port>eth(port)# show oam-efm-statistics` — _cli error_
- **str-62-classic-1** `ETX-2i>config>port>eth(port)# show fat-pipe-list { active | history | all }` — _cli error_
- **str-70-classic-1** `ETX-2i>config>port>lag(n)# show lacp-status ethernet <port>` — _cli error_
- **str-71-classic-1** `ETX-2i>config>port>lag(n)# show lacp-statistics ethernet <port>` — _cli error_
- **str-72-classic-1** `ETX-2i>config>port>e1(slot/port)# show status` — _NAV_ERROR:#                              ^
# cli error: Entry instance doesn't exist_
- **str-73-classic-1** `ETX-2i>config>port>e1(slot/port)# show statistics interval <n>` — _NAV_ERROR:#                              ^
# cli error: Entry instance doesn't exist_
- **str-74-classic-1** `ETX-2i>config>port>shdsl(slot/port)# show status` — _NAV_ERROR:#                           ^
# cli error: command not recognized_
- **str-75-classic-1** `ETX-2i>config>port>shdsl(slot/port)# show statistics current` — _NAV_ERROR:#                           ^
# cli error: command not recognized_
- **str-76-classic-1** `ETX-2i>config>port>vdsl2(slot/port)# show status` — _NAV_ERROR:#                                ^
# cli error: Entry instance doesn't exist_
- **str-77-classic-1** `ETX-2i>config>port>vdsl2(slot/port)# show statistics current` — _NAV_ERROR:#                                ^
# cli error: Entry instance doesn't exist_
- **str-82-classic-1** `ETX-2i>config>port>pcs(n)# show statistics running` — _NAV_ERROR:#                           ^
# cli error: command not recognized_
- **str-84-classic-1** `ETX-2i>config>bridge(n)# show mac-address-table { static | dynamic | all }` — _cli error_
- **str-88-classic-1** `ETX-2i>config>pwe>pw(n)# show status` — _NAV_ERROR:# cli error: PW creation failed: PW type must be configured.
#                         ^
# cli error: Incorrect paramete_
- **str-89-classic-1** `ETX-2i>config>pwe>pw(n)# show statistics current` — _NAV_ERROR:# cli error: PW creation failed: PW type must be configured.
#                         ^
# cli error: Incorrect paramete_
- **str-90-classic-1** `ETX-2i>config>pwe>pw(n)# show statistics interval <n>` — _NAV_ERROR:# cli error: PW creation failed: PW type must be configured.
#                         ^
# cli error: Incorrect paramete_
- **str-91-classic-1** `ETX-2i>config>pwe>pw(n)# show statistics total` — _NAV_ERROR:# cli error: PW creation failed: PW type must be configured.
#                         ^
# cli error: Incorrect paramete_
- **str-92-classic-1** `ETX-2i>config>pwe>pw(n)# show statistics all-intervals` — _NAV_ERROR:# cli error: PW creation failed: PW type must be configured.
#                         ^
# cli error: Incorrect paramete_
- **str-93-classic-1** `ETX-2i>config>pwe>pw(n)# show statistics all` — _NAV_ERROR:# cli error: PW creation failed: PW type must be configured.
#                         ^
# cli error: Incorrect paramete_
- **str-95-classic-1** `ETX-2i>config>pwe>pw(n)# show connectivity-statistics interval <n>` — _NAV_ERROR:# cli error: PW creation failed: PW type must be configured.
#                         ^
# cli error: Incorrect paramete_
- **str-112-classic-1** `ETX-2i>config>router(n)# show nat-translations` — _cli error_
- **str-113-classic-1** `ETX-2i>config>router(n)# show nat-statistics` — _cli error_
- **str-115-classic-1** `ETX-2i>config>router(n)>bgp(n)# show rib { ipv4 | ipv6 }` — _cli error_
- **str-116-classic-1** `ETX-2i>config>router(n)>bgp(n)# show community { ipv4 | ipv6 }` — _cli error_
- **str-117-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv4-unicast-af>neighbor(ip)# show advertised-route` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist_
- **str-118-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv4-unicast-af>neighbor(ip)# show received-route` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist_
- **str-119-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv4-unicast-af>neighbor(ip)# show prefix-list` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist_
- **str-120-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv4-unicast-af>neighbor(ip)# show route-map` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist_
- **str-122-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv6-unicast-af>neighbor(ip)# show advertised-route` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist_
- **str-123-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv6-unicast-af>neighbor(ip)# show received-route` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist_
- **str-124-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv6-unicast-af>neighbor(ip)# show prefix-list` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist_
- **str-125-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv6-unicast-af>neighbor(ip)# show route-map` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist_
- **str-128-classic-1** `ETX-2i>config>router(n)# show summary-interface` — _cli error_
- **str-132-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)# show mef46-ll-status` — _cli error_
- **str-133-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)# show remote-mep-status { remote-mep-id <id> | all }` — _cli error_
- **str-136-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)# show statistics current` — _cli error_
- **str-138-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)# show statistics interval <n>` — _cli error_
- **str-139-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)# show statistics total-intervals` — _cli error_
- **str-141-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)# show statistics running` — _cli error_
- **str-142-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)>dest-ne(n)# show statistics current` — _cli error_
- **str-143-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)>dest-ne(n)# show statistics interval <n>` — _cli error_
- **str-144-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)>dest-ne(n)# show statistics total` — _cli error_
- **str-145-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)>dest-ne(n)# show statistics running` — _cli error_
- **str-146-classic-1** `ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)>dest-ne(n)# show delay-measurement-bins` — _cli error_
- **str-147-classic-1** `ETX-2i>config>oam>twamp>controller(n)# show status` — _NAV_ERROR:#                                          ^
# cli error: License required_
- **str-148-classic-1** `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show status` — _NAV_ERROR:#                                                 ^
# cli error: License required_
- **str-149-classic-1** `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show report <n> all` — _NAV_ERROR:#                                                 ^
# cli error: License required_
- **str-150-classic-1** `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show report <n> current` — _NAV_ERROR:#                                                 ^
# cli error: License required_
- **str-151-classic-1** `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show report <n> interval` — _NAV_ERROR:#                                                 ^
# cli error: License required_
- **str-152-classic-1** `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show summary-report` — _NAV_ERROR:#                                                 ^
# cli error: License required_
- **str-153-classic-1** `ETX-2i>config>oam>twamp>responder(n)# show status` — _NAV_ERROR:#                                           ^
# cli error: parameter or keyword missing or wrong
 - responder <name> [<n_
- **str-155-classic-1** `ETX-2i>config>test>y1564>generator(n)# show mef46-ll-status` — _cli error_
- **str-156-classic-1** `ETX-2i>config>test>y1564>generator(n)# show report summary` — _cli error_
- **str-157-classic-1** `ETX-2i>config>test>y1564>generator(n)# show report detailed` — _cli error_
- **str-160-classic-1** `ETX-2i>config>test>rfc2544>test(n)# show report all` — _cli error_
- **str-161-classic-1** `ETX-2i>config>test>rfc2544>test(n)# show report iteration <n>` — _cli error_
- **str-165-classic-1** `ETX-2i>config>test>l3sat>generator(name)>peer(ip)# show report <name>` — _cli error_
- **str-166-classic-1** `ETX-2i>config>test>l3sat>generator(name)>peer(ip)# show summary-report` — _cli error_
- **str-178-classic-1** `ETX-2i>config>reporting# show alarm-inputs [all]` — _cli error_
- **str-179-classic-1** `ETX-2i>config>reporting# show alarm-information <source-type> <alarm-list>` — _cli error_
- **str-180-classic-1** `ETX-2i>config>system>clock>domain(n)>source(n)# show status` — _NAV_ERROR:#                              ^
# cli error: command not recognized_
- **str-181-classic-1** `ETX-2i>config>system>clock>domain(n)>source(n)# show statistics` — _NAV_ERROR:#                              ^
# cli error: command not recognized_
- **str-182-classic-1** `ETX-2i>config>system>clock>recovered(port/ptp)# show status` — _NAV_ERROR:#                              ^
# cli error: command not recognized_
- **str-183-classic-1** `ETX-2i>config>system>clock>recovered(port/ptp)# show network-metrics current` — _NAV_ERROR:#                              ^
# cli error: command not recognized_
- **str-184-classic-1** `ETX-2i>config>system>clock>recovered(port/ptp)# show network-metrics interval <n>` — _NAV_ERROR:#                              ^
# cli error: command not recognized_
- **str-185-classic-1** `ETX-2i>config>system>clock>recovered(port/ptp)# show network-metrics all` — _NAV_ERROR:#                              ^
# cli error: command not recognized_
- **str-186-classic-1** `ETX-2i>config>system>clock>recovered(port/ptp)# show network-metrics allintervals` — _NAV_ERROR:#                              ^
# cli error: command not recognized_