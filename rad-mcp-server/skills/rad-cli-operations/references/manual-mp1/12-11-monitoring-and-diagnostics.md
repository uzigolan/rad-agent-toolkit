# 11 Monitoring and Diagnostics

*Manual `MP-1-mn_ver 2.2.pdf`, pages 405–426.*


## 11.1 Performance Management  *(p.405)*

The following topics are described in this chapter: 
• 
Performance Management 
• 
Detecting Problems 
• 
Handling Alarms and Events 
• 
Syslog  
11.1 Performance Management 
Megaplex-1 maintains performance management (PM) statistics for selected entities in the device. The 
PM statistics are collected into a file periodically, for display in the RADview PM portal (refer to the 
RADview System User’s Manual for further details on the PM portal). The PM collection process can be 
globally enabled or disabled for the entire device. In addition, the statistics collection can be enabled for 
all entities of a specific type, or for specific entities. 
Benefits 
The PM data is useful for analyzing Megaplex-1 service quality. The flexible statistics collection allows 
only the necessary data to be collected. 
Functional Description 
PM statistics collection is configured for the device, entity type, and specific entities. PM statistics are 
collected for the Ethernet ports (NNI and UNI). 
Megaplex-1 
11. Monitoring and Diagnostics 
Note 
• 
PM statistics collection is performed only if it is enabled for the entire 
device, regardless of whether it is enabled for any entity 
• 
PM statistics are not collected for entities that are administratively 
disabled.  
If PM statistics collection is disabled for a particular entity type, then no PM statistics collection is done 
for any entity of that type, except those for which PM statistics collection is enabled.  
Note 
If you are using the RADview PM Portal, it is recommended to enable PM 
statistics collection for all relevant entities.  
PM statistics collection is performed at user-configurable intervals of one second to 15 minutes. A 
different interval can be configured for each entity type, and for specific entities. 
If different intervals are scheduled for collection at the same time, Megaplex-1 collects the PM statistics 
starting with the interval that has the highest frequency, and ending with the interval that has the 
lowest frequency. If Megaplex-1 has not finished collecting the statistics for an interval when the 
scheduled time for another interval arrives, the following action is taken according to whether the new 
interval is the next interval, or an interval with higher frequency: 
• 
If it is the next interval, then the next interval is canceled, and a PM record indicating the 
cancellation is inserted in the PM data 
• 
If it is an interval with higher frequency, then Megaplex-1 collects the higher frequency interval 
statistics and then resumes collecting the lower frequency interval statistics. The PM data is 
retrieved from Megaplex-1 by RADview via TFTP or SFTP. After PM data is retrieved, Megaplex-1 
deletes the file and opens a new one for further data. 
Factory Defaults 
Command 
Level under config 
Default  
Remarks 
pm 
reporting 
pm 
PM statistics 
collection in device is 
globally enabled by 
default. 
pm-collection  
Specific entity level 
Disabled 
- 
pm-collection eth 
reporting 
Disabled 
- 
 
 
 
 
Megaplex-1 
11. Monitoring and Diagnostics 
Configuring Performance Management 
You can configure PM statistics collection for the entire device via the pm command, and for entity 
types via the pm-collection command, in the reporting level. For specific entities, you can configure PM 
statistics collection via pm-collection, in the specific entity level.  
You can configure the device to record statistics at fixed intervals using the pm-collection interval 
<seconds> command or at the close of an interval using the pm-collection on-interval-close command. 
For parameters that are not zeroed regularly, it is recommended to record statistics at fixed intervals. 
For parameters zeroed at fixed intervals (interval statistics), it is recommended to record statistics 
whenever an interval is about to expire, i.e. right before the parameters are zeroed, in order to avoid 
losing data. This option is available for interval statistics only.The interval parameter for the 
pm-collection command can range from 1 to 900 seconds (15 minutes); however, the value must divide 
evenly into 3600. Different intervals can be specified for an entity type and for specific entities of that 
type, up to a supported maximum number of intervals. For example, if the PM statistics collection 
interval for all Ethernet ports is configured to 15 minutes, and the PM statistics collection interval for 
Ethernet 1/1 is configured to 1 minute, the data displayed in the RADview PM portal shows ethernet 
data for every 15 minutes, and Ethernet 1/1 data for every minute. You can also collect PM statistics on 
interval close.  
Note 
PM statistics is collected to a file. If the JOB application in RV is not running 
then the file might reach its maximum size. When the file reaches 90% from its 
maximum size, an alarm is displayed on the CLI terminal. Open Radview and 
JOB application to keep the file.  
The following table shows the PM statistics collection configuration tasks, and their corresponding 
commands, as well as the level of each command. 
Task 
Level 
Command 
Comments 
Globally enabling PM 
statistics collection for 
device 
reporting 
pm 
Type no pm to disable all PM statistics 
collection in Megaplex-1. 
Note: no pm stops all PM collection 
regardless of other PM configuration; 
however, it does not change other 
configurations.  
It deletes any collected PM data and 
PM files, as well. 
Megaplex-1 
11. Monitoring and Diagnostics 
Task 
Level 
Command 
Comments 
Enabling PM statistics 
collection for Ethernet 
ports  
reporting 
pm-collection eth  
{interval <seconds> | 
on-interval-close } 
PM collection can be enabled at a 
defined interval or before an interval 
expires.  
Type no pm-collection eth to disable 
PM statistics collection for Ethernet 
ports. 
Enabling PM statistics 
collection for a specific 
Ethernet port  
port > 
ethernet(<slot>/
<port-num>) 
pm-collection  
{interval <seconds> | 
on-interval-close } 
PM collection can be enabled at a 
defined interval or before an interval 
expires.  
Type no pm-collection to disable PM 
statistics collection for the Ethernet 
port. 
Viewing Performance Management Configuration 
You can use the info detail command to view the performance management configuration. 
 To view the performance management configuration for the device and for entity types: 
2. Navigate to configure reporting. 
3. Enter info detail | include pm to view PM-related commands in the configuration. 
 To view the performance management configuration for specific entities: 
4. Navigate to the specific entity level. 
5. Enter info detail | include pm to view PM-related commands in the configuration. 
Examples 
 To enable PM for all relevant entities in Megaplex-1: 
• 
PM statistics collection enabled for device 
• 
PM statistics collection enabled for all relevant entities, every five minutes. 
exit all 
configure reporting 
#**** Enable PM in device 
Megaplex-1 
11. Monitoring and Diagnostics 
pm 
#**** Enable PM for Eth ports, collection interval=5 min 
  pm-collection eth interval 300 
exit all 
save 
 To configure the following PM:  
• 
PM statistics collection enabled for device 
• 
PM statistics collection enabled for Ethernet ports, every two minutes 
• 
PM statistics collection for Ethernet port 0/2 configured to every minute  
exit all 
configure reporting 
#**** Enable PM in device 
pm 
#**** Enable PM for Eth ports, collection interval=2 min 
  pm-collection eth interval 120 
 
#**** Configure PM statistics collection interval for GbE Eth port 0/2, to 1 min 
configure port ethernet 0/2  
  pm-collection interval 60 
exit all 
save 
 To display PM configuration from above example: 
# configure reporting 
config>reporting# info detail | include pm 
    pm 
    pm-collection eth interval 120 
config>reporting# exit all 
 
# configure port ethernet 0/2 
config>port>eth(0/2)# info detail | include pm 
    pm-collection interval 60 
 
Configuration Errors  
The following table lists the messages displayed by Megaplex-1 when a configuration error is detected.  
Message 
Description 
Invalid interval; must divide evenly 
into 3600 
The pm-collection command was entered with an interval 
value that does not divide evenly into 3600.  

## 11.2 Detecting Problems  *(p.410)*

Megaplex-1 
11. Monitoring and Diagnostics 
Message 
Description 
Interval must be between 1 to 900 
seconds 
The interval configured for PM collection must be between 1 
to 900 seconds 
PM Collection is not supported for this 
entity type 
Megaplex-1 supports PM collection for Ethernet ports only. 
Cannot execute; too many different 
intervals 
Up to 4 different intervals are supported. 
11.2 Detecting Problems 
The LED indicators indicate errors on the hardware level. 
LEDs 
A red LED is usually an indication of a problem. Refer to the Operation chapter for a description of the 
Megaplex-1 LEDs. 
Alarms and Traps  
Alarms serve as notification of a fault in the device, and are indicated by an entry in the alarm and event 
history log, and/or an SNMP trap to a management station. Megaplex-1 supports up to 5000 history 
logs. See Handling Alarms and Events for further details on alarms, events, and traps. 
Statistic Counters 
Statistic counters provide information on possible abnormal behavior and failures. You can collect 
statistics on the following: 
• 
Ethernet ports 
• 
RADIUS server 
• 
PW 
• 
Serial ports working in 3bit-transitional encapsulation mode. 

## 11.3 Handling Alarms and Events  *(p.411)*

Megaplex-1 
11. Monitoring and Diagnostics 
For further information, refer to the relevant sections in Chapters 5–10. 
You can clear the statistics for Ethernet ports and PWs. Statistics clearing is globally enabled by default. 
Once statistics are cleared from a PW, the interval becomes “not valid”. 
11.3 Handling Alarms and Events 
An alarm is an indication of a fault in the device. An event is an occurrence in the device that may be a 
fault or may be a user login, change in port status, etc. Alarms and events can be written to the alarm 
and event history log. In addition to the history log containing alarms and events, the device maintains 
statistics for alarms and events in a brief log. Alarms can also be written to the active alarm table. An 
SNMP trap can be sent to management stations as the result of an alarm/event. Additionally, you can 
configure alarms and events to pop up on the serial CLI terminal. 
Alarms and events have the following properties: 
Source 
An entity for which alarms and events can be generated. The source 
consists of a source ID, source type, and source name.  
Alarms and events can be generated for any of the following source 
types:  
• system   
• powerSupply 
• alarmInput    
• stationClock  
• clockDomain 
• clockDomainSource 
• eth  
• mngEth   
• voice   
• ds1   
• ds1Opt    
• serial    
• routerInterface    
• pw 
• Note: Other options appearing in some CLI commands are iirelevant 
to Megaplex-1.   
ID 
Unique numeric identification of the alarm/event 
Megaplex-1 
11. Monitoring and Diagnostics 
Name 
Unique alphanumeric identification of the alarm/event, up to 
32 characters 
Description 
Alphanumeric description that provides details on the alarm/event 
Severity 
Alarms only; Critical, Major, or Minor 
Alarms and events can be masked per source type, source ID, or minimum severity. When an 
alarm/event is masked, it is not written to the history log, and any corresponding traps are not sent to 
management stations, regardless of masking in the SNMP manager configuration. When an alarm/event 
is not masked, any corresponding traps are sent only to management stations for which the traps are 
not masked in the SNMP manager configuration. 
Configuring Alarm and Event Properties 
This section explains how to configure alarm/event properties. 
Note 
In the commands alarm-source-attribute, alarm-source-type-attribute, and 
mask-minimum-severity, the popup parameter controls popup behavior in 
serial management sessions, and the vty­popup parameter controls popup 
behavior in Telnet/SSH management sessions 
 
Note 
All traps are maskable, by masking the corresponding alarm/event 
via the alarm-source-attribute / alarm-source-type—attribute 
commands, or by masking the corresponding alarm per severity via 
the mask-minimum-severity command.  
 To configure alarm/event properties: 
1. Navigate to configure reporting. 
The config>reporting# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Megaplex-1 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Configuring alarm input 
alarm-input <port-number> [active 
{high | low | off}] [description  
<description>] 
Three input alarms are supported 
over the Alarm connector.  
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
In description, enter a description 
of the alarm generated by the 
alarm-input. This description is 
saved in the log and sent with 
snmp traps when the alarm 
occurs. 
Configuring 
alarm/event severity 
and masking per source 
Note: Severity applies 
only to alarms. 
alarm-source-attribute 
<source-name> [<source-id>] alarm 
{<alarm-list> | all} [severity {critical | 
major | minor}] [log] [snmp-trap] 
[led] [popup] [vty­popup] 
alarm-source-attribute 
<source-name> [<source-id>] event 
{<alarm-list> | all} [log] [snmp-trap] 
[popup] [vty­popup]  
Use the no form to mask 
alarms/events. The following 
apply: 
• If a trap is masked according to 
alarm/event attribute, it is not 
sent to any management 
station, regardless of whether 
it is masked in the SNMP 
manager configuration. 
• If a trap is unmasked according 
to alarm/event attribute, it is 
sent only to management 
station for which it is not 
masked in the SNMP manager 
configuration. 
Megaplex-1 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Configuring 
alarm/event severity 
and masking per source 
type 
Note: Severity applies 
only to alarms. 
alarm-source-type-attribute 
<source-type> [<source-id>] alarm 
{<alarm-list> | all} [severity {critical | 
major | minor}] [log] [snmp-trap] 
[led] [popup] [vty­popup] 
alarm-source-type-attribute 
<source-type> [<source-id>] event 
{<alarm-list> | all} [log] [snmp-trap] 
[popup] [vty­popup]  
Use the no form to mask 
alarms/events. The following 
apply: 
• If a trap is masked according to 
alarm/event attribute, it is not 
sent to any management 
station, regardless of whether 
it is masked in the SNMP 
manager configuration. 
• If a trap is unmasked according 
to alarm/event attribute, it is 
sent only to management 
station for which it is not 
masked in the SNMP manager 
configuration. 
Configuring alarm 
masking and popup 
behavior per severity 
mask-minimum-severity [log {critical 
| major | minor}] [snmp-trap {critical 
| major | minor}] [led {critical | 
major | minor}] [popup {critical | 
major | minor}] [vty­popup {critical | 
major | minor}] 
 
Displaying information 
on specified alarms and 
source type 
show alarm-information 
<source-type> {<alarm-list> | all} 
show alarm-information 
<source-type> all indicates to 
display information on all alarms 
of the specified source type.  
Displaying information 
on alarm inputs 
show alarm-inputs [all] 
show alarm-input all indicates to 
display information on all alarm 
inputs of the device (up to three). 
The following is displayed for each 
alarm-input: 
• Port – port number 
• Status – active or inactive 
• Voltage – high, low, or off 
• Description  
Displaying list of 
supported alarms, 
optionally for specified 
source/severity 
show alarm-list 
show alarm-list [<source-type> 
[<source-id>] [severity {critical | 
major | minor}]] 
 
Megaplex-1 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Displaying information 
on specified event and 
source type 
show event-information 
<source-type> [<event-list>] 
 
Displaying list of 
supported events 
show event-list 
show event-list <source-type> 
[<event-list>] 
 
 
Controlling Popup Behavior  
Alarms and events are displayed (pop up) on active CLI terminals as soon as they occur. You can disable 
the popups per management session, without saving this setting in the configuration. It is relevant only 
for a management session (serial or Telnet/SSH) for which it is configured, and does not affect any other 
active session. 
If the popups are disabled for the current management session, they are not displayed, no matter how 
they are configured for a specific alarm or event (see Configuring Alarm and Event Properties).  
The current alarm/event popup status is available in the show users-details screen (see below). 
 To disable or enable alarm/event popups: 
• 
At any level, enter popup-suspend to disable alarm/event popups. 
• 
Enter no popup-suspend to enable alarm/event popups. 
 To display the user information: 
• 
In the configure>management# prompt, enter show users-details. 
configure management show users-details 
User:1234  Level:su  Popup:Disabled 
    From:Serial  For(sec):281744  
User:123456  Level:su  Popup: Enabled 
    From:100.100.100.100/SSH  For(sec):4510 
Working with Alarm and Event Logs 
This section explains how to work with the log files to display or acknowledge alarm/events. 
Megaplex-1 
11. Monitoring and Diagnostics 
 To work with alarm/event log files: 
1. Navigate to configure reporting. 
The config>reporting# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Acknowledging alarms 
acknowledge {log | brief-log | all-logs} 
The last acknowledgement time is recorded 
by the device and when displaying the log, 
only entries entered after the last 
acknowledgment time are displayed (or 
calculated, in case of the brief log).  
Log – the device acknowledges ony the 
history log. 
Brief-log – the device  acknowledges only 
the brief log (explained below). 
All-logs – the device acknowledges both the 
history and the brief logs. 
Rebuilding active alarm 
database 
active-alarm-rebuild [send-traps] 
Sometimes users suspect there are active 
alarms that were not cleared due to a bug or 
lost notification. This command rebuilds the 
active alarm table from scratch. If send-
traps is specified the device sends artificial 
raising traps for all active alarms. 
Clearing alarms from 
log file(s) 
clear-alarm-log {log | brief-log | all-
logs} 
Note: Activating clear-alarm-log all-logs 
command will erase all history logs. Do not 
use this command if you want to keep the 
history. 
Sselecting whether UTC 
or local timestamps are 
used when saving the 
alarm and event log 
into a file (that can be 
uploaded later) 
log-file-timestamp-type  {utc | local} 
 
   
Displaying active 
alarms, optionally 
according to specified 
criteria 
show active-alarms 
show active-alarms {<source-type> 
[<source-id>] | all} [minimum-severity 
{critical | major | minor}] 
[masked-included] [instance 
<instance-number>]] 
 
Megaplex-1 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Displaying active alarms 
with details, optionally 
according to specified 
criteria 
show active-alarms-details 
show active-alarms-details 
{<source-type> [<source-id>] | all} 
[minimum-severity {critical | major | 
minor}] [time-zone-utc] 
[masked-included] [instance 
<instance-number>]] 
 
Displaying alarms in 
alarm and event history 
log, optionally 
according to specified 
criteria 
show alarm-log 
show alarm-log {<source-type> 
[<source-id>] | all} [minimum-severity 
{critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] [start 
<yyyy-mm-dd> [<hh:mm[:ss]>] [end 
<yyyy-mm-dd> [<hh:mm[:ss]>]] 
show alarm-log {<source-type> 
[<source-id>] | all} [minimum-severity 
{critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] 
{[last-seconds <seconds>] | 
[last-entries <entries>]} 
 
Displaying alarms in 
brief alarm and event 
history log, optionally 
according to specified 
criteria 
show brief-alarm-log 
show brief-alarm-log {<source-type> 
[<source-id>] | all} [minimum-severity 
{critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] [start 
<yyyy-mm-dd> [<hh:mm[:ss]>]] [end 
<yyyy-mm-dd> [<hh:mm[:ss]>]] 
show brief-alarm-log {<source-type> 
[<source-id>] | all} [minimum-severity 
{critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] 
{[last-seconds <seconds>] | 
[last-entries <entries>]} 
 
Megaplex-1 
11. Monitoring and Diagnostics
Task 
Command 
Comments 
Displaying brief alarm 
and event history log, 
optionally according to 
specified criteria 
show brief-log 
show brief-log {<source-type> 
[<source-id>] | all} [minimum-severity 
{critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] [start 
<yyyy-mm-dd> [<hh:mm[:ss]>]] [end 
<yyyy-mm-dd> [<hh:mm[:ss]>]] 
show brief-log {<source-type> 
[<source-id>] | all} [minimum-severity 
{critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] 
{[last-seconds <seconds>] | 
[last-entries <entries>]} 
Displaying alarm and 
event history log, 
optionally according to 
specified criteria 
show log 
show log {<source-type> [<source-id>] 
| all} [minimum-severity {critical | 
major | minor | cleared}] [order-
ascending] [time-zone-utc] 
[acknowledged-included] [start 
<yyyy-mm-dd> [<hh:mm[:ss]>]] [end 
<yyyy-mm-dd> [<hh:mm[:ss]>]] 
show log {<source-type> [<source-id>] 
| all} [minimum-severity {critical | 
major | minor | cleared}] [order-
ascending] [time-zone-utc] 
[acknowledged-included] 
{[last-seconds <seconds>] | 
[last-entries <entries>]} 
Alarms and Events  
You can view the full lists of alarms and events supported by Megaplex-1. 
 To view the alarms table: 
•
Double-click the paper clip image
 on the following line. 

## 11.4 Syslog  *(p.419)*

Megaplex-1 
11. Monitoring and Diagnostics 
 
 To view the events table: 
• 
Double-click the paper clip image 
 on the following line. 
11.4 Syslog 
Megaplex-1 uses the Syslog protocol to generate and transport event notification messages over IP 
networks to Syslog servers.  
Standards 
RFC 3164, RFC 5674 
Benefits 
Syslog protocol collects heterogeneous data into a single data repository. It provides system 
administrators with a single point of management for collecting, distributing and processing audit data. 
Syslog standardizes log file formats, making it easier to examine log data with various standard tools. 
Data logging can be used for: 
• 
Long-term auditing 
• 
Intrusion detection 
• 
Tracking user and administrator activity 
• 
Product operation management 
Functional Description 
The Syslog protocol provides an instrument for generating and transporting event notification messages 
from Megaplex-1 to servers across IP networks. 
Megaplex-1 
11. Monitoring and Diagnostics 
Elements 
Typical Syslog topology includes message senders (devices) and message receivers (servers). Megaplex-1 
supports up to five Syslog servers. The receiver displays, stores, or forwards logged information. The 
standard designates two types of receivers: 
Relay 
Forwards messages 
Collector 
Displays and stores messages 
Transport Protocol 
Syslog uses User Datagram Protocol (UDP) for its transport. The UDP port assigned to Syslog is 514, but 
devices and servers can be defined to use any port for communication. 
Message Format 
The length of a Syslog message is 1024 bytes or less. It contains the following information: 
• 
Facility and severity (see below) 
• 
Host name or IP address of the device 
• 
Timestamp 
• 
Message content 
A typical Syslog message looks like this: 
<145>Jan 15 13:24:07 172.17.160.69 Eth 1: Loss of signal (LOS) 
Facilities and Severities 
Facility designates a device or application that sends a message. The standard includes some predefined 
facilities in the 0–15 range. For originator identification, Megaplex-1 uses facilities local1– local7. 
Severity is assigned to a message to specify its importance. Megaplex- 1uses the following severity 
designations: 
Code 
Syslog Type 
Description 
0 
Emergency 
Emergency message 
1 
Alert 
Critical alarm 
2 
Critical 
Major alarm 
Megaplex-1 
11. Monitoring and Diagnostics 
Code 
Syslog Type 
Description 
3 
Error 
Minor alarm 
4 
Warning 
Event 
5 
Notice 
Cleared alarm 
6 
Informational 
Informational message, not in use 
7 
Debug 
Debug-level messages, not in use 
Factory Defaults 
By default, Syslog operation is disabled. When enabled, the default parameters are as follows: 
Parameter 
Default Value 
facility 
local1 
port 
514 
severity-level 
informational 
Configuring Syslog Parameters 
When configuring Syslog parameters, it is necessary to define Syslog device and servers. 
 To configure Syslog device: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining a facility from which Syslog 
messages are sent 
facility {local1 | local2 | local3 
| local4 | local5 | local6 | 
local7} 
 
Megaplex-1 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining Syslog device UDP port for 
communication 
port <udp-port-number> 
Possible values: 1–65535 
Port configuration is 
allowed only if a Syslog 
device is administratively 
disabled. 
Defining severity level 
severity-level { emergency | 
alert | critical | error | 
warning | notice | 
informational | debug} 
The log messages that 
contain severity level 
above or equal to the 
specified level are 
transmitted. 
Administratively enabling Syslog 
device 
no shutdown 
shutdown administratively 
disables the Syslog device. 
Displaying statistics 
show statistics 
 
Clearing statistics 
clear-statistics 
 
 To configure a Syslog server: 
1. Navigate to configure system). 
The config>system# prompt is displayed. 
2. At the config>system# prompt, enter syslog server <server-ID> to specify the server to receive 
Syslog messages, where <server-ID> is 1 to 5. 
The config>system>syslog(<server-ID>)# prompt is displayed. 
3. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Enabling logging of command entries  
accounting commands 
To disable command 
logging, enter no 
accounting commands 
Defining Syslog server IP address 
address <ip-address> 
Possible values: 
0.0.0.0–255.255.255.255 
Defining Syslog server UDP port for 
communication 
port <udp-port-number> 
Possible values: 1–65535 
Administratively enabling Syslog 
server 
no shutdown 
shutdown administratively 
disables Syslog server. 
Megaplex-1 
11. Monitoring and Diagnostics 
Viewing Syslog Statistics 
 To display Syslog statistics: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. At the config>system>syslog(device)#, enter show statistics. 
Syslog statistics appear as shown below. The counters are described in the table below. 
config>system>syslog(device)# show statistics 
Total Tx Messages 
 
 
: 356 
Non-queued Dropped Messages 
 
 
: 265 
Parameter 
Description 
Total Tx Messages 
The total number of Syslog messages transmitted 
Non-queued Dropped Messages 
The total number of Syslog messages that were dropped before 
being queued 
 To clear Syslog statistics: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. At the config>system>syslog(device)# prompt, enter clear-statistics. 
The Syslog statistic counters are set to 0. 
Configuration Errors 
The following table lists messages generated by Megaplex-1 when a configuration error is detected. 
Message 
Description 
Syslog Port is out of range 
Selected UDP port value is out of allowed range (1–65535). 
Port is illegal or Device Port is already 
in use 
Selected UDP port is already in use. 
Parameter cannot be changed if 
Logging Status/Server Access is 
enabled 
Device/server UDP port or server IP address cannot be 
changed while Syslog server is enabled. 

## 11.5 Troubleshooting  *(p.424)*

Megaplex-1 
11. Monitoring and Diagnostics 
Message 
Description 
Illegal Severity 
Invalid severity value 
Illegal Facility 
Invalid facility value 
Illegal Server IP Address 
Invalid server IP address 
Example 
• 
Server IP address: 178.16.173.152 
• 
UDP port: 155 
exit all 
configure system  
  syslog device 
    no shutdown 
    exit 
  syslog server 1 
    address 178.16.173.152 
    port 155 
    no shutdown 
    save 
    exit all 
11.5 Troubleshooting 
This section contains a general troubleshooting chart that lists possible failures and provides 
workarounds. 
• 
Use this chart to identify the cause of a problem that may arise during operation. For detailed 
description of the LED indicators functions, refer to the Operation chapter. 
To correct the reported problem, perform the suggested corrective actions. If a problem cannot be 
resolved by performing the suggested action, please contact your RAD distributor. 
Fault/Problem 
Probable Cause 
Corrective Action 
The unit is “dead”  
(POWER LED is off) 
No power 
• Verify that both ends of the power cable are properly 
connected. 
 
Blown fuse 
• Disconnect the power cable from both ends and replace the 
fuse with another fuse of proper rating. 
Megaplex-1 
11. Monitoring and Diagnostics 
Fault/Problem 
Probable Cause 
Corrective Action 
The event log reports 
a power supply error. 
 
• View the inventory file by entering show inventory at the 
config>system prompt. 
• Restart the unit. 
• In case of failure, replace the entire unit. 
The unit is 
unreachable 
Incorrect 
management 
settings 
• Using a local serial connection, enable the relevant 
management access type by entering telnet, snmp, and/or 
ssh at the config>mngmnt>access prompt.  
• View the list of enabled management access types and 
settings by entering info detail at the config>mngmnt 
prompt 
• Verify that a router interface has been configured with 
management access set to allow all, assigned an IP address, 
and bound to an administratively enabled SVI. 
• Verify that management flows have been set up to/from 
the SVI, and that the flows are enabled. 
 
 
Management path 
disconnected 
• In case of remote management, analyze this issue using a 
local serial connection. 
• At the current prompt, check whether the desired unit 
responds by entering ping <IP address>. 
• Check network connectivity issues and firewall settings. 
• Verify that the management flows have been configured 
correctly. 
Physical link fails to 
respond 
Link may be 
administratively 
disabled. 
• Administratively enable the link. 
• In case of Ethernet links, make sure that the 
autonegotiation, speed, and duplex modes match the 
configured values on the access switch/router. 
Ethernet LINK LED 
is off 
Ethernet cable 
problem 
• Check the Ethernet cable to see whether a cross or straight 
cable is needed. 
• Check/replace Ethernet cable. 
• Verify that the range is within the limits. 
• Check the port by connecting the remote end of the cable 
to a different switch. 
• Send the unit for repair. 

## 11.6 Technical Support  *(p.426)*

Megaplex-1 
11. Monitoring and Diagnostics 
11.6 Technical Support 
For technical support of registered products, contact your local authorized RAD partner or go to 
RADcare Online (if you have a valid RADcare service package).  
RAD Data Communications would like your help in improving its product documentation. Please send us 
an e-mail with your comments. 
Thank you for your assistance! 
                       
 
 
 