# Feature Reference – 8 Monitoring and Diagnostics – 8.12 Alarms and Events

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1558–1565.*


## Applicability and Scaling  *(p.1558)*


## List of Alarms and Events  *(p.1558)*

ETX-2i Devices 
8. Monitoring and Diagnostics

To clear the statistics:
•
At the device prompt, enter:
clear-statistics
The statistics for Ethernet ports, flows, and OAM services (running counters only; not current
counters) are cleared. The OAM interval statistics are not cleared.
Note 
PW and E1 do not support running-statistics; therefore, clear-statistics clears 
only the current statistics. 
8.12 Alarms and Events 
An alarm is an indication of a fault in the device. An event is an occurrence in the device that may be a 
fault or may be a user login, change in port status, etc.  
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. 
List of Alarms and Events 
You can view the full lists of alarms and events supported by ETX‑2i. 
Note 
When viewing this user manual online, embedded attachments may not open 
due to your browser settings. Downloading this user manual from 
www.rad.com and viewing it offline guarantees that embedded files always 
open. 

To view the alarms table:
•
Double-click the paper clip image
 on the following line. 

To view the events table:
•
Double-click the paper clip image
 on the following line. 

## Functional Description  *(p.1559)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Note 
• 
Entries with source type card, pcs, or shdsl are relevant for ETX-2i modular 
option with an SHDSL or VDSL2 module. 
• 
Entries with source type e1t1 are relevant for ETX-2i modular option with 
E1/T1 module. 
• 
Entries with source type ptp-recovered or ptp-recovered-master are 
relevant only for PTP ordering options. 
• 
Entries with source type clock-domain, clock-domain-source, or station-
clock are relevant only for timing ordering options. 
• 
Dying Gasp alarms are not immediately issued after the event occurs. The 
relevant ETX-2i device needs 5 - 10 minutes to build the database and be 
ready to issue these alarms. 
Functional Description 
Alarms and events can be written to the alarm and event history log. In addition to the history log 
containing alarms and events, the device maintains statistics for alarms and events in a brief log. Alarms 
can also be written to the active alarm table. An SNMP trap can be sent to management systems as the 
result of an alarm/event. Additionally, you can configure alarms and events to pop up on the serial CLI 
terminal. 
Alarm and Event Properties 
Alarms and events have the following properties: 
Source 
An entity for which alarms and events can be generated. The source consists of a source ID, 
source type, and source name.  
Alarms and events can be generated for any of the following source types: system, fan, power-
supply, station-clock, recovered-clock, g82751-recovered*, g82751-master-cl*,  gnss, card, 
ethernet, vdsl, shdsl, pcs, sdh-sonet, e1, t1, e3, t3, vcg, bridge, logical-mac, etp, gfp, lag, oam-
efm, oam-cfm-mep, oam-cfm-destne, eps, erp, eth-protection, router-interface, pw, bgp, 
domain-clock recovered-clock-*, domain-clock-sou*,  master-clock, smart-sfp, oam-cfm-r-mep, 
erp-port, ospf, ospf-neighbor, ospf-interface, twamp-session, twamp-peer, all 
ID 
Unique numeric identification of the alarm/event 
Name 
Unique alphanumeric identification of the alarm/event, up to 32 characters 
Description 
Alphanumeric description that provides details on the alarm/event 
Severity 
Alarms only; Critical, Major, or Minor 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Alarm and Event Masking 
Alarms and events can be masked per source type, source ID, or minimum severity. When an 
alarm/event is masked, it is not written to the history log, and any corresponding traps are not sent to 
management systems, regardless of masking in the SNMP manager configuration. When an alarm/event 
is not masked, any corresponding traps are sent only to management systems for which the traps are 
not masked in the SNMP manager configuration. 
Alarm Soaking 
ETX‑2i supports alarm soaking. This means that the device does not raise an alarm immediately upon 
detecting an abnormal condition (i.e., defect); only after the abnormal condition has occurred 
uninterrupted for a certain amount of time (called the rising soaking time). Similarly, the alarm is cleared 
only after the abnormal condition is resolved and remains resolved for a certain amount of time (called 
the falling soaking time or clear time). In this way, alarm soaking prevents fleeting alarms, i.e., alarms 
that rise and fall multiple times in a short period. Instead of sending a flood of alarms to RADview, only 
one initial alarm is sent, and the final clear alarm is sent only upon stabilization of the link.  
The device supports alarm soaking, provided the following requirements are met: 
• 
The device supports configurable alarm rising and falling soaking times, as follows: 
 
Rising and falling soaking times may be configured to different values. 
 
The configurable soaking time range is 0 (i.e., no soaking time) to 10,000 milliseconds. 
 
The default rising soaking time is 2,500 milliseconds (2½ seconds); default falling soaking 
time is 10,000 milliseconds (10 seconds). 
 
The actual soaking time may deviate by up to ½ second from the configured value. 
 
The configured soaking times apply only for those entities that do have a standard dictating 
a different behavior. If there is such a standard, such as SDH/SONET and DS1, the standard is 
followed.  
• 
When a defect occurs, the device must wait the rising soaking time (either configured or 
dictated by a standard) before raising the alarm. An alarm is raised only if the defect exists for 
the entire soaking time. If the defect is cleared and reoccurs, the rising soaking timer must be 
rearmed. 
• 
When a condition that caused an alarm is resolved, the device must wait the falling soaking time 
(either configured or dictated by a standard) before clearing the alarm. Only if the condition 
stays resolved for the entire soaking time, the alarm is cleared. If the defect reoccurs, the 
soaking timer must be rearmed.  

## Configuring Alarm and Events  *(p.1561)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuring Alarm and Events 
Configuring Alarm and Event Properties 
This section explains how to configure alarm/event properties. 
Note 
In the commands alarm-source-attribute, alarm-source-type-attribute, and 
mask-minimum-severity, the popup parameter controls popup behavior in 
serial management sessions, and the vty­popup parameter controls popup 
behavior in Telnet/SSH management sessions. 
 
Note 
All traps are maskable, by masking the corresponding alarm/event via the 
alarm-source-attribute/alarm-source-type-attribute commands, or by 
masking the corresponding alarm per severity via the 
mask-minimum-severity command. 
 To configure alarm/event properties: 
1. Navigate to configure reporting. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Configuring alarm input 
alarm-input <port-number> [active {high | low | 
off}] [description  <description>] 
Three input alarms are 
supported over the Alarm 
connector (9-pin Terminal 
Block). 
If you set alarm-input to active 
state, configure alarm input’s 
activation mode to one of the 
following: 
• high – active alarm input 
indicated by high voltage 
• low – active alarm input 
indicated by low voltage 
• off – active alarm input 
disabled 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
In description, enter a 
description of the alarm 
generated by the alarm-input. 
This description is saved in the 
log and sent with snmp traps 
when the alarm occurs. 
Configuring alarm severity 
and alarm/event masking 
per source 
alarm-source-attribute <source-name> [<source-id>] 
alarm { <alarm-list> | all} [severity {critical | major | 
minor }] [log] [snmp-trap] [led] [popup] [vty­popup] 
alarm-source-attribute <source-name> [<source-id>] 
event {<event-list> | all} [log] [snmp-trap] [popup] 
[vty­popup]  
Note: Severity applies only to 
alarms. 
Use the no form to unmask 
alarms/events.  
If a trap is masked according to 
alarm/event attribute, it is not 
sent to any management 
system, regardless of whether it 
is masked in the SNMP manager 
configuration. 
If a trap is unmasked according 
to alarm/event attribute, it is 
sent only to management 
system for which it is not 
masked in the SNMP manager 
configuration. 
Configuring alarm severity 
and alarm/event masking 
per source type 
alarm-source-type-attribute <source-type> 
[<source-id>] alarm {<alarm-list> | all} [severity 
{critical | major | minor}] [log] [snmp-trap] [led] 
[popup] [vty­popup] 
alarm-source-type-attribute <source-type> 
[<source-id>] event {<event-list> | all} [log] 
[snmp-trap] [popup] [vty­popup]  
Note: Severity applies only to 
alarms. 
Use the no form to unmask 
alarms/events.  
If a trap is masked according to 
alarm/event attribute, it is not 
sent to any management 
system, regardless of whether it 
is masked in the SNMP manager 
configuration. 
If a trap is unmasked according 
to alarm/event attribute, it is 
sent only to management 
system for which it is not 
masked in the SNMP manager 
configuration. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Configuring alarm masking 
and popup behavior per 
severity 
mask-minimum-severity [log {critical | major | 
minor}] [snmp-trap {critical | major | minor}] [led 
{critical | major | minor}] [popup {critical | major | 
minor}] [vty­popup {critical | major | minor}] 
Configuring alarm rising 
and falling soaking times 
soaking-time interval [rising rising-msec] clear 
[falling falling-msec] 
rising, falling: 0–10,000 ms  
Default: 
rising – 2500 ms 
falling – 10000 ms  
Note: The configured soaking 
times apply only for entities for 
which there is no standard 
dictating a different behavior. If 
there is such a standard (e.g., for 
SDH/SONET and DS1), the 
standard must be followed. 
Displaying information on 
specified alarms and 
source type 
show alarm-information <source-type> {<alarm-list> 
| all} 
show alarm-information 
<source-type> all indicates to 
display information on all alarms 
of the specified source type.  
Displaying information on 
alarm inputs 
show alarm-inputs [all] 
show alarm-input all indicates 
to display information on all 
alarm inputs of the device (up to 
three). 
The following is displayed for 
each alarm-input: 
• Port – port number 
• Status – active or inactive 
• Voltage – high, low, or off 
• Description  
Displaying list of 
supported alarms, 
optionally for specified 
source/severity 
show alarm-list 
show alarm-list [<source-type> [<source-id>] 
[severity {critical | major | minor}]] 
Displaying information on 
specified event and source 
type 
show event-information <source-type> [<event-list>] 

## Alarm and Event Logs  *(p.1564)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Displaying list of 
supported events 
show event-list 
show event-list <source-type> [<event-list>] 
  
Controlling Popup Behavior 
Alarms and events are displayed (pop up) on active CLI terminals as soon as they occur. You can disable 
the popups per management session, without saving this setting in the configuration. It is relevant only 
for a management session (serial or Telnet/SSH) for which it is configured and does not affect any other 
active session. 
If the popups are disabled for the current management session, they are not displayed, no matter how 
they are configured for a specific alarm or event (see Configuring Alarm and Event Properties).  
The current alarm/event popup status is available in the show users-details screen (see below). 
 To disable or enable alarm/event popups: 
• 
At any level, enter popup-suspend to disable alarm/event popups. 
• 
Enter no popup-suspend to enable alarm/event popups. 
 To display user information: 
• 
In the config>management# prompt, enter show users-details. 
ETX‑2i# configure management show users-details 
User:1234  Level:su  Popup:Disabled 
    From:Serial  For(sec):281744  
User:123456  Level:su  Popup: Enabled 
    From:100.100.100.100/SSH  For(sec):4510 
Alarm and Event Logs 
This section explains how to work with the log files to display or acknowledge alarm/events, 
 To work with alarm/event log files: 
1. Navigate to configure reporting. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Acknowledging alarms 
acknowledge { log | brief-log | activity-log | all-logs } 
Rebuilding active alarm 
database 
active-alarm-rebuild [send-traps] 
Clearing alarms from log 
file(s) 
clear-alarm-log { log | brief-log | activity-log | all-logs } 
Displaying active alarms, 
optionally according to 
specified criteria 
show active-alarms 
show active-alarms { <source-type> [<source-id>] | all } 
[minimum-severity {critical | major | minor}] 
[masked-included] [instance <instance-number>]] 
Displaying active alarms 
with details, optionally 
according to specified 
criteria 
show active-alarms-details 
show active-alarms-details { <source-type> [<source-id>] 
| all } [minimum-severity { critical | major | minor }] 
[time-zone-utc] [masked-included] [instance 
<instance-number>]] 
Displaying alarms in alarm 
and event history log, 
optionally according to 
specified criteria 
show alarm-log 
show alarm-log {<source-type> [<source-id>] | all} 
[minimum-severity {critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] [start <yyyy-mm-dd> 
[<hh:mm[:ss]>] [end <yyyy-mm-dd> [<hh:mm[:ss]>]] 
show alarm-log {<source-type> [<source-id>] | all} 
[minimum-severity {critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] {[last-seconds <seconds>] | 
[last-entries <entries>]} 
Displaying alarms in brief 
alarm and event history 
log, optionally according 
to specified criteria 
show brief-alarm-log 
show brief-alarm-log {<source-type> [<source-id>] | all} 
[minimum-severity {critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] [start <yyyy-mm-dd> 
[<hh:mm[:ss]>]] [end <yyyy-mm-dd> [<hh:mm[:ss]>]] 
show brief-alarm-log {<source-type> [<source-id>] | all} 
[minimum-severity {critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] {[last-seconds <seconds>] | 
[last-entries <entries>]} 