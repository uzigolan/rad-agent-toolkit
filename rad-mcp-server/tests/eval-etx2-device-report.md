# ETX-2 Device Test Results  —  Raviv-Etx2-Telnet

**Date:** 2026-07-21 15:57  
**Total:** 185

| Status | Count | % |
|--------|-------|---|
| PASS   | 68 | 36% |
| FAIL   | 110 | 59% |
| SKIP   | 7 | 3% |

## By category

| Category | Pass | Fail | Skip |
|----------|------|------|------|
| Admin | 0 | 3 | 0 |
| Bridge | 0 | 3 | 0 |
| File | 8 | 5 | 0 |
| Management | 0 | 7 | 0 |
| OAM | 4 | 18 | 0 |
| PWE | 0 | 8 | 0 |
| Port | 0 | 32 | 0 |
| QoS | 3 | 0 | 0 |
| Reporting | 12 | 0 | 0 |
| Root | 19 | 0 | 0 |
| Router | 15 | 13 | 0 |
| System | 0 | 14 | 0 |
| Test | 7 | 7 | 0 |
| Unknown | 0 | 0 | 7 |

## Failures

- **str-21-classic-1** `ETX-2i>file# show banner-text` — _cli error_
- **str-27-classic-1** `ETX-2i>file# show rollback-config` — _cli error_
- **str-30-classic-1** `ETX-2i>file# show usb-status` — _cli error_
- **str-31-classic-1** `ETX-2i>file# show user-default-config` — _cli error_
- **str-32-classic-1** `ETX-2i>file# show user-dir` — _cli error_
- **str-34-classic-1** `ETX-2i>admin>scheduler# show scheduler` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-35-classic-1** `ETX-2i>admin>scheduler# show scheduler-details` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-36-classic-1** `ETX-2i>admin>license# show summary` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-37-classic-1** `ETX-2i>config>system# show system-date` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-38-classic-1** `ETX-2i>config>system# show cpu-utilization` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-39-classic-1** `ETX-2i>config>system# show memory` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-40-classic-1** `ETX-2i>config>system# show memory-details` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-41-classic-1** `ETX-2i>config>system# show summary-inventory` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-42-classic-1** `ETX-2i>config>system# show device-information` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-43-classic-1** `ETX-2i>config>chassis# show environment` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-44-classic-1** `ETX-2i>config>mngmnt# show users` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-45-classic-1** `ETX-2i>config>mngmnt# show users-details` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-46-classic-1** `ETX-2i>config>mngmnt# show failed-login-attempts` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-47-classic-1** `ETX-2i>config>mngmnt# show ssh-server fingerprint` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-48-classic-1** `ETX-2i>config>mngmnt>radius# show statistics` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-49-classic-1** `ETX-2i>config>mngmnt>snmp# show snmpv3 information` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-50-classic-1** `ETX-2i>config>mngmnt>snmp# show trap-sync` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-51-classic-1** `ETX-2i>config>port# show statistics` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-52-classic-1** `ETX-2i>config>port# show summary` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-53-classic-1** `ETX-2i>config>port# show summary-full-name` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-54-classic-1** `ETX-2i>config>port>eth(port)# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-55-classic-1** `ETX-2i>config>port>eth(port)# show status refresh <sec>` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-56-classic-1** `ETX-2i>config>port>eth(port)# show statistics` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-57-classic-1** `ETX-2i>config>port>eth(port)# show loopback` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-58-classic-1** `ETX-2i>config>port>eth(port)# show rate` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-59-classic-1** `ETX-2i>config>port>eth(port)# show l2cp-statistics` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-60-classic-1** `ETX-2i>config>port>eth(port)# show oam-efm` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-61-classic-1** `ETX-2i>config>port>eth(port)# show oam-efm-statistics` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-62-classic-1** `ETX-2i>config>port>eth(port)# show fat-pipe-list { active | history | all }` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-63-classic-1** `ETX-2i>config>port>eth(port)# show sfp-extended-information` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-64-classic-1** `ETX-2i>config>port>eth(port)>lldp# show neighbors-details` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-66-classic-1** `ETX-2i>config>port>eth(port)>lldp# show neighbors-summary` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-67-classic-1** `ETX-2i>config>port>eth(port)>lldp# show statistics` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-68-classic-1** `ETX-2i>config>port>lag(n)# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-69-classic-1** `ETX-2i>config>port>lag(n)# show statistics running` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-70-classic-1** `ETX-2i>config>port>lag(n)# show lacp-status ethernet <port>` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-71-classic-1** `ETX-2i>config>port>lag(n)# show lacp-statistics ethernet <port>` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-72-classic-1** `ETX-2i>config>port>e1(slot/port)# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-73-classic-1** `ETX-2i>config>port>e1(slot/port)# show statistics interval <n>` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-74-classic-1** `ETX-2i>config>port>shdsl(slot/port)# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-75-classic-1** `ETX-2i>config>port>shdsl(slot/port)# show statistics current` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-76-classic-1** `ETX-2i>config>port>vdsl2(slot/port)# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-77-classic-1** `ETX-2i>config>port>vdsl2(slot/port)# show statistics current` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-78-classic-1** `ETX-2i>config>port>gfp(n)# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-79-classic-1** `ETX-2i>config>port>gfp(n)# show bind` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-80-classic-1** `ETX-2i>config>port>ppp(n)# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-81-classic-1** `ETX-2i>config>port>ppp(n)>pppoe# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-82-classic-1** `ETX-2i>config>port>pcs(n)# show statistics running` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-83-classic-1** `ETX-2i>config>port>log-mac(n)# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-84-classic-1** `ETX-2i>config>bridge(n)# show mac-address-table { static | dynamic | all }` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-85-classic-1** `ETX-2i>config>bridge(n)# show mac-table [vlan <vlan>] [mac-address <mac>]` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-86-classic-1** `ETX-2i>config>bridge(n)# show vlans` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-87-classic-1** `ETX-2i>config>pwe# show summary` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
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
# cli error: Entry instance doesn't exist
ETX-2I-x86#_
- **str-118-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv4-unicast-af>neighbor(ip)# show received-route` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist
ETX-2I-x86#_
- **str-119-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv4-unicast-af>neighbor(ip)# show prefix-list` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist
ETX-2I-x86#_
- **str-120-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv4-unicast-af>neighbor(ip)# show route-map` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist
ETX-2I-x86#_
- **str-122-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv6-unicast-af>neighbor(ip)# show advertised-route` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist
ETX-2I-x86#_
- **str-123-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv6-unicast-af>neighbor(ip)# show received-route` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist
ETX-2I-x86#_
- **str-124-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv6-unicast-af>neighbor(ip)# show prefix-list` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist
ETX-2I-x86#_
- **str-125-classic-1** `ETX-2i>config>router(n)>bgp(n)>ipv6-unicast-af>neighbor(ip)# show route-map` — _NAV_ERROR:#                                                             ^
# cli error: Entry instance doesn't exist
ETX-2I-x86#_
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
# cli error: License required
ETX-2I-x86#_
- **str-148-classic-1** `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show status` — _NAV_ERROR:#                                                 ^
# cli error: License required
ETX-2I-x86#_
- **str-149-classic-1** `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show report <n> all` — _NAV_ERROR:#                                                 ^
# cli error: License required
ETX-2I-x86#_
- **str-150-classic-1** `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show report <n> current` — _NAV_ERROR:#                                                 ^
# cli error: License required
ETX-2I-x86#_
- **str-151-classic-1** `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show report <n> interval` — _NAV_ERROR:#                                                 ^
# cli error: License required
ETX-2I-x86#_
- **str-152-classic-1** `ETX-2i>config>oam>twamp>controller(n)>peer(ip)# show summary-report` — _NAV_ERROR:#                                                 ^
# cli error: License required
ETX-2I-x86#_
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
- **str-180-classic-1** `ETX-2i>config>system>clock>domain(n)>source(n)# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-181-classic-1** `ETX-2i>config>system>clock>domain(n)>source(n)# show statistics` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-182-classic-1** `ETX-2i>config>system>clock>recovered(port/ptp)# show status` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-183-classic-1** `ETX-2i>config>system>clock>recovered(port/ptp)# show network-metrics current` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-184-classic-1** `ETX-2i>config>system>clock>recovered(port/ptp)# show network-metrics interval <n>` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-185-classic-1** `ETX-2i>config>system>clock>recovered(port/ptp)# show network-metrics all` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_
- **str-186-classic-1** `ETX-2i>config>system>clock>recovered(port/ptp)# show network-metrics allintervals` — _NAV_ERROR:

read_channel_timing's absolute timer expired.

The network device was continually outputting data for longer than 10
seconds.

If this is expected i.e. the command you are executing is continually emitting
data for a long period of time, then you can set 'read_timeout=x' seconds. If
you want Netmiko to keep reading indefinitely (i.e. to only stop when there is
no new data), then you can set 'read_timeout=0'.

You can look at the Netmiko session_log or debug log for more information.

_