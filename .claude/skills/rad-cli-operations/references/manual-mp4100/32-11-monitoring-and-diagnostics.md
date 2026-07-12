# 11 Monitoring and Diagnostics

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 823–907.*


## (chapter introduction)  *(p.823)*

The Megaplex-4 monitoring and diagnostic functions can be used to identify problems in the network 
incorporating Megaplex-4 units, test the proper operation of each Megaplex-4 unit, and rapidly locate 
the cause of the fault –within the Megaplex-4 itself, in its connections to the network or to user 
equipment, or in another network component.  
Problems can be detected on the hardware level, for example by running the self-test and monitoring 
the LED behavior.  
On the software level, you can follow statistical counters and events and errors returned by the system. 
When a problem occurs, Megaplex-4 offers a set of diagnostic functions that efficiently locate the 
problem (in the Megaplex-4 chassis, in one of Megaplex-4 modules, in a connecting cable, or in external 
equipment) and rapidly restore full service. 
The diagnostic functions include a ping utility on the system level and loopbacks at the various ports, 
which identify whether a malfunction is caused by the Megaplex-4 or by an external system component 
(for example, an equipment unit, cable, or transmission path connected to the Megaplex-4).  
In addition to the general Megaplex-4 functions described in this chapter, you can find information on 
the module-specific diagnostic functions in the Megaplex-4 I/O Modules Installation and Operation 
Manual.  
The following table briefly summarizes Megaplex-4 monitoring and diagnostic functions. 
Megaplex-4 Monitoring and Diagnostics 
Function 
Short Description 
Alarms, events and traps 
Generates various alarms and events that can be displayed at a 
supervision terminal, and sending alarm traps to management 
stations so that operators can identify problems. 
Configuration error messages 
Checking the validity of the user’s configuration activities and 
reporting any conflicts and errors 
Diagnostic loopbacks 
Diagnostic tests for checking transmission paths 
Ethernet OAM (CFM) 
Ethernet Connectivity Fault Management  

## 11.1 Alarms, Events and Traps  *(p.824)*

11. Monitoring and Diagnostics 
Function 
Short Description 
Ethernet OAM (EFM) 
OAM Ethernet at the First Mile 
In-service ping 
Checking connectivity across L2 service paths 
LEDs 
LED indicators 
Performance management  
Performance management (PM) statistics for selected entities 
Ping test 
Checking Megaplex-4IP connectivity  
Statistic counters 
Displaying statistics of the Ethernet, SDH/SONET, E1/T1, VCG,, GFP, 
HDLC and PW ports, RADIUS server and flows  
Syslog 
Generating and transporting event notification messages over IP 
networks to Syslog servers 
11.1 Alarms, Events and Traps 
Megaplex-4 generates various alarms that can be displayed at a supervision terminal, and sends alarm 
traps to management stations so that operators can identify problems. 
Megaplex-4 maintains a cyclic event log file that stores up to 5000 time-stamped events. This list can be 
sent to an external file and seen by means of any text editor. For this procedure, see Copying Files 
within Megaplex-4 in Chapter 10. 
In addition, up to 200 latest alarms/events are displayed on the Megaplex-4 screen in the form of a 
monitor log. This log is user-manageable: it can be renewed, cleared or sorted, as described in Error! 
Reference source not found. below.  
The difference between events, traps and alarms is as follows: 
• 
Alarm. A message that reports a failure. An alarm is a persistent indication of a fault of an entity, 
which may be the device itself or any of its components. 
• 
Event. Any change of status in a managed object in the network. SNMP equipment can generate 
traps for many different kinds of events, not all of which are important for telemetry. The ability 
to filter unimportant events is essential for high-quality SNMP alarm management. An event is 
something that may be of interest, such as a fault, a change in status, crossing a threshold, or an 
external input to the system. 
• 
Trap. An SNMP message issued by an agent that reports an event. The term trap is used as 
abbreviation to SNMPv1 or SNMPv3 notification. The SNMP version is usually omitted, unless it 
is important to specify it. Traps may be generated and sent as a result of event or alarm. 
11. Monitoring and Diagnostics 
Megaplex-4 includes a configurable mechanism of detecting and reporting alarms. Once an alarm is 
triggered, Megaplex-4 sends an alarm trap to the relevant network manager, depending on whether the 
relevant trap has been masked or activated. In the current Megaplex-4 version, all traps are activated.  
Alarms and events have the following properties: 
• 
Source –An entity for which alarms and events can be generated. The source consists of a source 
ID, source type (e.g., system, fan, Ethernet), and source name.  
• 
ID – Unique numeric identification of the alarm/event 
• 
Name – Unique alphanumeric identification of the alarm/event, of up to 32 characters 
• 
Description –Alphanumeric description that provides details about the alarm/event 
• 
Severity (alarms only) – Critical, Major, or Minor.  
Masking 
Alarms and events can be masked per source type, source ID, or minimum severity. When masking by 
source type (such as Ethernet) or source ID (such as Ethernet port 1 on card in slot 1), choose a specific 
alarm or event, or apply the change to all the alarms and events of the selected source type or ID. 
When masking an alarm/event, you can: 
• 
Prevent the alarm/event from being written to the history log, sent to Syslog servers, and 
displayed in the default view of the active alarms table 
• 
Prevent any corresponding traps from being sent to management stations, regardless of 
masking in the SNMP manager configuration 
• 
Deactivate alarm reporting via LED and alarm relay. 
When an alarm/event is not masked, any corresponding traps are sent only to management station for 
which the traps are not masked in the SNMP manager configuration. In addition, you can: 
• 
Change alarm severity  
• 
Mask a specific reporting method 
• 
Mask alarms per their severity. 
You can also acknowledge alarm logs. The last acknowledgement time is recorded by Megaplex-4. When 
displaying the log, only entries entered after the last acknowledgment time are displayed. This action 
does not delete any data from the log, and you can also display acknowledged data by using a 
designated keyword. 
11. Monitoring and Diagnostics 
Alarm Buffer 
Megaplex-4 continuously monitors critical signals and signal processing functions. In addition, it can also 
monitor an external alarm line, connected to the ALARM connector. 
If a problem is detected, Megaplex-4 generates time-stamped alarm messages. The time stamp is 
provided by an internal real-time clock.  
The alarm messages generated by the Megaplex-4 are explained below. 
Internally, the Megaplex-4 stores alarms in an alarm buffer. This alarm buffer can store up to 200 alarm 
messages, together with their time stamps. The alarm history buffer is organized as a FIFO queue; after 
200 alarms are written into the buffer, new alarms overwrite the oldest alarms. 
Alarm messages can also be sent automatically as traps to the user-specified network management 
stations. 
The alarms can be read on-line by the network administrator using the network management station, a 
Telnet host or a supervision terminal. The network administrator can then use the various diagnostic tests to 
determine the causes of the alarm messages and to return the system to normal operation. 
When Megaplex-4 is powered down, the alarm messages are erased; old alarms will not reappear after 
the Megaplex-4 is powered up again. When using the terminal or a Telnet host, the user also can clear 
(delete) the alarms stored in this buffer, after reading them. 
Alarm Relays 
In addition to the alarm reporting facility, Megaplex-4 has two alarm relays with floating change-over 
contacts: one relay for indicating the presence of major alarms and the other for minor alarms. Each 
relay changes state whenever the first alarm is detected, and returns to its normal state when all the 
alarms of the corresponding severity disappear.  
The relay contacts can be used to report internal system alarms to outside indicators (e.g., lights, 
buzzers, bells), located on a bay alarm or remote monitoring panel. 
See also ACM Module, TP Module and VS Modules sections in the Megaplex-4 I/O Modules Installation 
and Operation Manual for description of alarm relays available on these modules. 
11. Monitoring and Diagnostics 
Configuring Alarm Reporting  
This section describes how to configure alarm/event properties, how to mask them and rebuild active 
alarms. Some of the commands are available only with ACM, TP or VS-6/BIN modules installed in the 
system. 
Factory Defaults  
Configuration defaults are listed in the table below. This table is relevant only when the ACM module is 
installed in the chassis. 
Parameter  
Description 
Default Value 
active  
Alarm-input: active state of the port input line 
high 
energized 
Alarm-output: state of port relay when alarm is 
present  
yes  
 To configure alarm/event properties: 
4. Navigate to configure reporting. 
The config>reporting# prompt is displayed. 
5. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Setting the active state of 
the port input line and 
alarm description (ACM 
module only) 
 
alarm-input <slot>/<port> [active 
{high | low | off}] [description  < 
alarm-input-description-string>] 
high – Active alarm input is 
indicated by high voltage 
low – Active alarm input is indicated 
by low voltage 
off – Alarm input is disabled 
Description-string – a free-text 
alarm name 
Setting the alarm 
description (VS-6/BIN 
module only)  
 
alarm-input 
<slot>/<port>/<tributary> 
[description <alarm-input-
description-string>] 
 
Description-string – a free-text 
alarm name  
Active state selection although 
present in CLI is not relevant for this 
module. 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining the state of the 
output relay when an 
alarm is present (ACM 
module only) 
alarm-output <slot>/<port>  
energized {yes | no} 
Energizing:  
• energized yes – The 
corresponding relay is normally 
unenergized and switches to the 
energized state when the alarm 
is active. 
• energized no – The 
corresponding relay is normally 
energized  and switches to the 
unenergized state when the 
alarm is active. 
The relay contacts are normally 
open. 
Binding an alarm of 
specific source type to an 
alarm output port 
bind-alarm-to-relay <source-
type> <alarm-name> alarm-
output  <slot/port/tributary>  
For the list of source types and 
corresponding alarm names, refer to 
Alarm list in this chapter. 
Using no before the command 
cancels the alarm binding 
Applicable for ACM, VS-6/BIN and 
TP modules installed in the system. 
In the TP module, relevant for ports 
5..8 only. 
<tributary> relates only to VS-6/BIN 
modules. 
A cmd-out port cannot be 
simultaneously bound as Alarm 
Relay (the current command) and 
bound as secondary cmd-out port to 
a primary cmd-out port (see Chapter 
6).  
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Binding an alarm of 
specific source type on a 
specific user port to an 
alarm output port 
bind-alarm-source-to-relay 
<source-type> <alarm-name> 
<slot/port> alarm-output 
<slot/port/tributary> 
 
For the list of source types and 
corresponding alarm names, refer to 
Alarm list in this chapter. 
Using no before the command 
cancels the alarm binding. 
Applicable for ACM, VS-6/BIN and 
TP modules installed in the system. 
In the TP module, relevant for ports 
5..8 only. 
<tributary> relates only to VS-6/BIN 
modules. 
Masking alarm/event from 
a specific source, defining 
alarm severity and 
masking reporting 
methods 
Note: Severity and LED-
Relay apply only to 
alarms. 
alarm-source-attribute 
<source-type> [<source-id>] 
alarm <alarm-name> [severity 
{critical | major | minor}] [log] 
[snmp-trap] [led-relay] 
alarm-source-attribute<source-ty
pe> [<source-id>] event 
<event-name> [log] [snmp-trap] 
Use the no form to unmask 
alarms/events.  
When you apply masking command, 
the alarm severity changes. If later 
you apply the unmasking command  
(no alarm-source-attribute…) the 
severity remains at its changed 
value. If you want the initial severity 
back, repeat the command with the 
desired severity.  
The following apply: 
• If a trap is masked according to 
alarm/event attribute, it is not 
sent to any management station, 
regardless of whether it is 
masked in the SNMP manager 
configuration 
• If a trap is unmasked according 
to alarm/event attribute, it is 
sent only to management station 
for which it is not masked in the 
SNMP manager configuration. 
• LED-Relay mask is not activated 
on ALM LED until clear-log 
command is performed for 
active alarm history log. 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Masking alarm per 
severity 
mask-minimum-severity [log 
{critical | major | minor}] 
[snmp-trap {critical | major | 
minor}] [led-relay {critical | 
major | minor}] 
no mask-minimum-severity [log] 
[snmp-trap  [led-relay] 
Masking a minimum severity means 
that lower severities are also 
masked 
Acknowledging the logs 
acknowledge {log | all-logs} 
 
Displaying alarm logs 
show {active-alarms | active-
alarms-details | alarm-
information | alarm-log | alarm-
list | event-information | 
event-list | log ] 
See Error! Reference source not 
found. 
Displaying the state of 
input alarms and 
configured voltage for 
each port of the 
slot/chassis 
 
show alarm-input {slot <slot>| 
all}  
Current status: 
• Active – an active external alarm 
is present on the port    
• Inactive – external alarm is not 
active or port in shutdown state 
Voltage: as defined by alarm-input 
<slot>/<port> [active {high | low | 
off}] command 
Description:  port name 
Displaying the state of 
output alarms for each 
port of the slot/chassis 
 
show alarm-outputs {slot <slot>| 
all}  
• Active – active alarms from the 
list configured by the user are 
present on the port    
• Inactive –no active alarms from 
the list configured by the user 
are present on the port   
 
Note 
If alarm/event is masked using one of the masking commands 
(alarm-source-attribute, alarm-source-type-attribute, 
mask-minimum-severity), there is no need to repeat the procedure using the 
other commands.  
11. Monitoring and Diagnostics 
Examples 
 To mask alarm for a specific source type: 
• 
Source type – All E1s 
• 
Alarm – excessive-bpv 
• 
Reporting methods – log 
mp4100>config# reporting 
mp4100>config>reporting# alarm-source-type-attribute e1 excessive-bpv log 
 To mask event for a specific source: 
• 
Source type –E1 1 in port 1 on card in slot 1 
• 
Event – css-path-tca 
• 
Reporting methods – SNMP trap 
mp4100>config# reporting 
mp4100>config>reporting# alarm-source-attribute e1 1/1 event css-path-tca 
snmp-trap 
 To mask alarms per severity: 
• 
Severity –major and lower 
• 
Reporting method – LED and alarm relay 
mp4100>config# reporting 
mp4100>config>reporting# mask-minimum-severity led-relay major 
Working with the Alarm and Event Logs 
This section explains how to display and clear different type of alarm and event logs. The maximum 
number of items in manageable logs is 200. To export up to 5000 alarms/events to a text log file, see 
Chapter 10. 
Instructions on viewing alarms and events can be found below. Lists of possible alarms and events can 
be found under Alarm List and Event List sections, respectively.  
 To display the alarm/event log: 
1. Navigate to configure>reporting# context. 
11. Monitoring and Diagnostics 
2. Type show followed by the display option parameter listed in the following table. 
Display Option 
Meaning 
Example no 
active-alarms  
Shows the active alarms table. Counters of active 
alarms in the output, in order of severity, appear 
at top of the screen  
1 
active-alarms-details  
Same as above but with time stamp added to 
active alarms 
2 
alarm-information 
Detailed information about alarm type. For 
example, if you need to know what is LOF alarm 
on SDH/SONET in Examples 1 or 2, see Example 3.  
3 
alarm-log  
Log of active and cleared alarms (without events). 
The default view of the alarm log (i.e., history of 
alarms) shows one line per raised alarm and one 
for cleared alarm 
4 
alarm-list   
[<source ID> 
[severity 
{critical|major|minor
}]] 
List of all Megaplex-4 alarms for a specific source 
IDs and severity value or of all the alarms available 
in the system 
5 
event-information 
Detailed information about event type (similar to 
alarm-information) 
 
event-list  
List of all Megaplex-4 events for a specific source 
IDs or of all the events available in the system 
 
log  
Log of active alarms, cleared alarms and events 
 
To scroll up and down in the list, use the arrow keys.  
 To clear a  log: 
• 
At the config>reporting# context, enter clear-alarm-log  {log | activity-log | all-logs}.  
The corresponding log is cleared. 
Example 1: Displaying Active Alarms 
This command shows the table of active alarms. On top of the screen appear counters of active alarms in the 
output, by severity: critical, major and minor. 
 
mp4100>config>reporting# show active-alarms 
Total :      Critical  : 0         Major  : 3         Minor  : 0 
11. Monitoring and Diagnostics 
 
1     SDH-SONET     cl-a/2         LOF             Maj   unmasked 
2     Ethernet      MNG cl-b/1     LOS             Maj   unmasked 
3     SDH-SONET     cl-b/2         LOS             Maj   unmasked 
Example 2. Displaying Active Alarms Details 
This command shows the table of active alarms with their time stamp. On top of the screen appear counters of 
active alarms in the output, by severity: critical, major and minor. 
 
mp4100>config>reporting# show active-alarms-details 
Total :      Critical  : 0         Major  : 3         Minor  : 0 
 
1     Loss of frame (LOF) 
 
15-05-2015   SDH-SONET     LOF   Major     Unmasked 
02:10:52     cl-a/2 
 
 
2     Loss of signal (LOS) 
 
15-05-2015   Ethernet      LOS  Major     Unmasked 
03:38:53     MNG cl-b/1 
 
 
3     Loss of signal (LOS) 
 
15-05-2015   SDH-SONET    LOS  Major     Unmasked 
03:38:48     cl-b/2 
Example 3. Displaying Information of LOF alarm on SDH/SONET port 
This command displays detailed information about a specific alarm. The output shows configuration of 
the source type, followed by a table of sources whose configuration divert from the source type’s 
configuration. 
For example, use this command if you need to know what is LOF alarm on SDH/SONET in Examples 1 or 
2. In this example the table of sources is empty since all the sources are configured the same as their 
type. 
 
mp4100>config>reporting# show alarm-information sdh-sonet lof 
Source        : SDH-SONET 
Name          : LOF 
Description   : Loss of frame (LOF) 
11. Monitoring and Diagnostics 
Alarm ID      : 100003 
Severity      : Major 
LED           : Yes 
LED Relay     : Yes 
Logged        : Yes 
SNMP Trap     : Yes 
SNMP trap OID : 1.3.6.1.4.1.164.3.1.6.2.0.22 
 
Source                Source ID           Severity LED    Logged SNMP Trap 
---------------------------------------------------------------------- 
Example 4. Alarm Log  
This command displays the log of active and cleared alarms (without events). The default view of the 
alarm log (i.e. history alarms) shows one line per raised alarm and one for cleared alarm. The alarm 
severity is shown on the left. Its possible values are critical, major, minor, or cleared. The field on the 
left shows the reason of alarm removal: resolved, user-initiated, alarm suppression, not applicable. 
mp4100>config>reporting# show alarm-log 
Last Acknowledge On : 2026-01-05   18:29:04.0 
 
 
2     Loss of frame (lof)                      
 
2026-01-06   T1          1/1                    lof                 Cleared 
11:12:10.00                                                         Resolved 
 
 
3     Loss of frame (lof)  
 
2026-01-06   T1          1/1                    lof                  Major 
11:12:08.00 
 
 
4     Ethernet frames not received by pw  
 
2026-01-06   Pw          2           rx_failure                      Major 
11:12:06.00 
 
 
5     Ethernet frames not received by pw   
 
2026-01-06   Pw          3     rx_failure                            Major 
11:12:05.00 
 
 
11. Monitoring and Diagnostics 
7     Remote defect indication (rdi) at far-end device                   
 
2026-01-06   Pw          2            fe_rdi                         Cleared 
11:11:51.00                                                          Resolved 
 
 
8     Remote defect indication (rdi) at far-end device  
 
2026-01-06   Pw          2           fe_rdi                           Major 
11:11:50.00 
Example 5. Alarm List  
This command displays the list of all Megaplex-4100 alarms for a specific source IDs and severity value. 
The table also shows whether the alarm appears in the log and whether these parameters are set to 
default or modified by the user. This specific example displays the beginning of the list of all the alarms 
available in the system. 
 
mp4100>config>reporting# show alarm-list  
 
Source 
Name                             ID      Severity  Logged 
 
System 
hardware_failure_fe              20012             Yes     (Default) 
----------------------------------------------------------------------------- 
System 
configuration_mismatch_fe        20013             Yes     (Default) 
----------------------------------------------------------------------------- 
System 
INTERFACE_MISMATCH_FE            20014   Major     Yes     (Default) 
----------------------------------------------------------------------------- 
System 
NO_INTERFACE_FE                  20015             Yes     (Default) 
----------------------------------------------------------------------------- 
Power Supply 
POWER_DELIVERY_FAILURE           20201   Major     Yes     (Default) 
----------------------------------------------------------------------------- 
Alarm Input 
Alarm_Relay_Input                20401   Major     Yes     (Default) 
----------------------------------------------------------------------------- 
Card 
HARDWARE_FAILURE                 40001   Major     Yes     (Default) 
----------------------------------------------------------------------------- 
11. Monitoring and Diagnostics
Card 
CARD_MISMATCH                    40002   Major     Yes     (Default) 
---------------------------------------------------------------------- 
To scroll up and down in the list, use the arrow keys. 
Alarm and Event Lists 
You can view the full lists of alarms and events supported by Megaplex-4, along with the traps 
corresponding to each alarm or event.  
Note 
When viewing this file online, embedded attachments may not open due to 
your browser settings. Downloading this file from www.rad.com and viewing 
it offline guarantees that embedded files always open. 
 To view the alarms table: 
•
Double-click the paperclip image on the following line.
 To view the events table: 
•
Double-click the paperclip image on the following line.
Configuration Error Messages 
The following table lists the messages displayed by Megaplex-4 when a configuration error is detected. 
Code 
Type 
Syntax 
Meaning 
730 
Error 
LOG MUST BE MASKED 
TOGETHER WITH SNMP-TRAP 
If an alarm is masked for log reporting 
(alarm-source-attribute command), it must be masked for 
trap reporting as well. 

## 11.2 Configuration Error Messages  *(p.837)*


## 11.3 Diagnostic Loopbacks  *(p.837)*

11. Monitoring and Diagnostics 
11.2 Configuration Error Messages  
Megaplex-4 includes an extensive subsystem that checks the validity of the user’s configuration 
activities and reports any conflicts and errors. These error messages are referred to as “sanity errors”, 
because they are detected by the so-called sanity check automatically performed to confirm correct 
configuration of the equipment. Two types of messages are generated: 
Warning  
Minor errors that do not prevent using the  
Megaplex-4; for example, an installed module is not programmed in 
the chassis.  
Error  
Errors that prevent proper operation of the  
Megaplex-4 in its intended application; for example, an invalid 
timeslot assignment).  
For further information, refer to the relevant sections in the configuration chapters. 
11.3 Diagnostic Loopbacks  
There are two subsystems/engines in Megaplex-4 – TDM and Ethernet, each featuring its own tests and 
loopbacks. These tests are shown in the diagrams below. 
The following table identifies the general types of test and loopback functions supported by Megaplex-4 
TDM engine, and the paths of the signals when each test or loopback is activated. The available 
diagnostic loopbacks depend on the installed modules, and some of them support additional types of 
loopbacks. For specific instructions, refer to the corresponding section in Chapter 6: for example, 
Testing E1 Ports under E1 Ports, etc. 
The following table schematically shows the tests available in the Megaplex TDM engine.  
11. Monitoring and Diagnostics 
Megaplex-4 Test and Loopback Functions - TDM Engine 
Diagnostic Function 
Megaplex-4100
DS1
Cross-Connect
Matrix
CL
E1/T1
Mapper
SDH/
SONET
Framer
1
........
E1-i/T1-i 
Framers
2
SDH/SONET Interface 
VC/VT
Matrix
I/O Port
Local loopback on I/O 
voice, serial ports  
 
    I/O Port 
    Interface
DS1
Cross-Connect
Matrix
 
 
 
 
 
Remote loopback on 
I/O voice, serial ports 
 
Port 
Interface
DS1
Cross-Connect
Matrix
 
 
 
 
 
Local loopback on  
T1 port (T3 modules) 
Port 
Interface
 1 
"   "
DS1
Cross-Connect
Matrix
 
 
 
 
 
11. Monitoring and Diagnostics 
Diagnostic Function 
Megaplex-4100
DS1
Cross-Connect
Matrix
CL
E1/T1
Mapper
SDH/
SONET
Framer
1
........
E1-i/T1-i 
Framers
2
SDH/SONET Interface 
VC/VT
Matrix
I/O Port
Remote loopback on  
T1 port (T3 modules) 
    Port 
    Interface
DS1
Cross-Connect
Matrix
 
 
 
 
 
 
 
Local loopback on 
T1/T1-i timeslots (T3 
modules)  
DS1
Cross-Connect
Matrix
1
.....
2
I/O Interface
 
 
 
 
 
 
 
Remote loopback on 
T1/T1-i timeslots (T3 
modules) 
1
.....
2
DS1
Cross-Connect
Matrix
I/O Interface
 
 
 
 
 
 
 
Remote loopback on 
SDH/SONET link  
 
 
 
 
 
SDH/SONET
Framer
 
11. Monitoring and Diagnostics 
Diagnostic Function 
Megaplex-4100
DS1
Cross-Connect
Matrix
CL
E1/T1
Mapper
SDH/
SONET
Framer
1
........
E1-i/T1-i 
Framers
2
SDH/SONET Interface 
VC/VT
Matrix
I/O Port
Local loopbacks on 
AUG/OC-3, 
TUG-3/STS-1, 
VC-12/VT-1.5 ports  
 
 
 
 
VC/VT 
Matrix
 
 
Remote loopbacks on 
AUG/OC-3, 
TUG-3/STS-1,  
VC-12/VT-1.5 ports 
 
 
 
 
VC/VT 
Matrix
 
 
Local loopback on E1-
i/T1-i port  
 
 
1
......
E1-i/T1-i Framers
2
  
 
Remote loopback on 
E1-i/T1-i  port  
 
 
1
......
E1-i/T1-i Framers
2
  
 
Local loopback on 
timeslots of  
E1-i/T1-i port  
 
 
E1-I/T1-I 
Framers
 
  
 
11. Monitoring and Diagnostics 
Diagnostic Function 
Megaplex-4100
DS1
Cross-Connect
Matrix
CL
E1/T1
Mapper
SDH/
SONET
Framer
1
........
E1-i/T1-i 
Framers
2
SDH/SONET Interface 
VC/VT
Matrix
I/O Port
Remote loopback on 
timeslots of  
E1-i/T1-i  port  
 
 
E1-I/T1-I 
Framers
 
  
 
Megaplex-4 Test and Loopback Functions - Ethernet Engine  
Diagnostic Function 
 
Megaplex-4100
CL
ETH Engine
L2 
Switch
CPU
I/O Port
CPE
Traffic 
Generator
Traffic 
Counter
 
 
 
 
 
 
 
Ethernet BERT 
       
PCS 
I/O Port
CPE
Traffic 
Generator
Traffic 
Counter
 
Loop per flow 
See Testing the Flows in Chapter 8 
 
  
 
11. Monitoring and Diagnostics 
The Megaplex loopbacks are activated from the following context and are described in the 
corresponding sections in Chapters 6, 8 and 11. 
11. Monitoring and Diagnostics 
Loopbacks 
Activated from 
Local and remote loopbacks on I/O voice, serial 
ports 
configure>port>voice 
configure>port>serial  
Local and remote loopbacks on  
E1 or T1 port  
configure>port>e1 
configure>port>t1 
Local and remote loopbacks on  
T3 ports 
configure>port>t3 
Local and remote loopbacks on E1/E1-i/T1/T1-i 
timeslots 
configure>port>e1 
configure>port>t1  
configure>port>e1-i 
configure>port>t1-i 
Remote loopback on SDH/SONET link  
configure>port>sdh-sonet 
Local and remote loopbacks on AUG ports 
configure>port>sdh-sonet>aug 
 
Local and remote loopbacks on OC-3 ports 
configure>port>sdh-sonet>oc3 
 
Local and remote loopbacks on TUG-3 ports 
configure>port>sdh-sonet>aug>tug3 
 
Local and remote loopbacks on STS-1 ports 
configure>port>sdh-sonet>oc3>sts1 
 
Local and remote loopbacks on VC-12 ports 
configure>port>sdh-sonet>aug>tug3>vc12 
 
Local and remote loopbacks on VT-1.5 ports 
configure>port>sdh-sonet>oc3>sts1>vt1-5 
 
Local and remote loopbacks on E1-i/T1-i port  
configure>port>e1-i 
configure>port>t1-i 
Local and remote loopbacks on timeslots of  
E1-i/T1-i port  
configure>port>e1-i 
configure>port>t1-i 
Ethernet BERT 
configure>test>rfc2544  

## 11.4 Ethernet OAM (CFM)  *(p.844)*

11. Monitoring and Diagnostics 
Loopbacks 
Activated from 
Loop per flow 
configure>flows>flow  
11.4 Ethernet OAM (CFM) 
Ethernet Connectivity Fault Management (CFM) is a service-level OAM protocol that provides tools for 
monitoring and troubleshooting end-to-end Ethernet services. This includes proactive connectivity 
monitoring, fault verification, and fault isolation. CFM uses standard Ethernet frames and can be run on 
any physical media that is capable of transporting Ethernet service frames. Megaplex-4 also supports 
performance monitoring per Y.1731. 
Megaplex-4 can act as a Maintenance Entity Group Intermediate Point (MIP) or Maintenance Entity 
Group End Point (MEP). If Megaplex-4 is acting as a MIP, it forwards OAM CFM messages transparently, 
responding only to OAM link trace (LTM).  
Standards 
IEEE 802.1ag-D8, ITU-T Y.1731 
Benefits 
Ethernet service providers can monitor their services proactively and guarantee that customers receive 
the contracted SLA. Fault monitoring and end-to-end performance measurement provide tools for 
monitoring frame delay, frame delay variation, and frame loss and availability. 
Factory Defaults 
By default, there are no MDs, MAs, or MEPs. 
The default OAM CFM multicast address is 01-80-C2-00-00-30. 
When a maintenance domain is created, it has the following default configuration. 
11. Monitoring and Diagnostics 
Parameter 
Default  
Remarks 
proprietary-cc 
no proprietary-cc 
Standard OAM protocol 
md-level 
3 
 
name   
string  "MD<mdid>" 
For example the default name 
for maintenance domain 1 is 
“MD1”. 
When a maintenance association is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
ccm-interval 
1s 
Continuity check interval is 1 
second 
classification  
vlan 0 
 
name   
string  "MA<maid>" 
For example the default name for 
maintenance association 1 is 
“MA1”. 
When a maintenance endpoint is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
ais 
no ais 
 
bind 
no bind 
 
classification  
vlan  0 
 
client-md-level  
4 
 
dest-addr-type 
ccm  multicast pm  unicast 
• Destination address type for 
CCM messages – multicast 
• Destination address type for 
performance measurement 
messages – unicast 
direction 
down 
 
ccm-initiate 
ccm-initiate 
Initiate continuity check 
messages 
ccm-priority 
0 
 
queue   
fixed  0 block  0/0 
 
shutdown 
shutdown 
Administratively disabled 
11. Monitoring and Diagnostics 
When a service is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
delay-threshold  
10 
 
delay-var-threshold 
10 
 
classification 
priority-bit  0 
 
dmm-interval 
1s 
 
lmm-interval 
1s 
 
shutdown 
shutdown 
Administratively disabled 
When a destination NE is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
delay  
two-way data-tlv-length 0 
 
delay-measurement-bin 
no delay-measurement-bin 
 
delay-var-measurement-bin 
no delay-var-measurement-bin 
 
loss  
single-ended user-data 
 
remote    
mac-address 00-00-00-00-00-00 
 
Functional Description 
OAM (Operation, Administration, and Maintenance) describes the monitoring of network operation by 
network operators. OAM is a set of functions used by the user that enables detection of network faults 
and measurement of network performance, as well as distribution of fault-related information. OAM 
may trigger control plane or management plane mechanisms, by activating rerouting or by raising 
alarms, for example, but such functions are not part of the OAM itself. OAM functionality ensures that 
network operators comply with QoS guarantees, detect anomalies before they escalate, and isolate and 
bypass network defects. As a result, the operators can offer binding service-level agreements. 
Megaplex-4 provides the OAM (CFM) functions listed below in packet-switched networks:  
• 
End-to-end Connectivity Fault Management (CFM) per IEEE 802.1ag: 
 
Continuity check (CC) 
 
Non-intrusive loopback, used to detect loss of bidirectional continuity  
 
Link Trace for fault localization  
11. Monitoring and Diagnostics 
• 
End-to-end service and performance monitoring per ITU-T Y.1731: 
 
Loss measurement 
 
Delay measurement. 
OAM Elements 
The Ethernet OAM mechanism monitors connectivity in Maintenance Association (MA) groups, 
identified by a Maintenance Association Identifier (MAID). Each maintenance association consists of two 
or more maintenance end points (MEP). Every MA belongs to a maintenance domain (MD), and inherits 
its level from the MD to which it belongs. The MD levels are used to specify the scope of the MA 
(provider, operator, customer, etc). 
• 
Maintenance Domain (MD) – The network or the part of the network for which faults in 
connectivity can be managed. Each maintenance domain has an MD level attribute which 
designates the scope of its monitoring. 
• 
Maintenance Association (MA) – A set of MEPs, each configured with the same MAID and MD 
level, established to verify the integrity of a single service instance. 
• 
Maintenance End Point (MEP) – An actively managed CFM entity. A MEP is both an endpoint of 
a single MA, and an endpoint of a separate Maintenance Entity for each of the other MEPs in 
the same MA. A MEP generates and receives CFM PDUs and tracks responses. 
• 
Maintenance Intermediate Point (MIP) – MIPs are defined under the MD level and are 
transparent to connectivity messages.  
OAM Functions 
RAD’s carrier Ethernet aggregation and demarcation devices feature a comprehensive hardware-based 
Ethernet OAM and performance monitoring for SLA assurance: 
• 
End-to-end Connectivity Fault Management (CFM) per IEEE 802.1ag: 
 
Continuity check (CC) 
 
Non-intrusive loopback  
 
Link trace for fault localization  
• 
End-to-end service and performance monitoring per ITU-T Y.1731 
 
Loss measurement (single-ended) 
 
Delay measurement (two-way). 
The device supports: 
• 
Up to 128 maintenance domains (MDs) 
11. Monitoring and Diagnostics 
• 
Up to 128 maintenance associations (MAs) 
• 
Up to 128 maintenance endpoints (MEPs). Up to eight MEPs can be configured for an MA (on 
EVC.cos configuration). 
• 
Up to 512 remote MEPs. Up to 80 remote MEPs can be configured for a MEP.  
• 
Up to 256 services. Up to eight services can be configured for a MEP. 
• 
Up to 256 destination NEs. 
Note 
The above limits are subject to the limit of 300 received PPS (packets per 
second). This includes AIS, Linktrace, and other management packets. It does 
not include continuity check (CC), loopback (LB), delay measurement 
messages (DMM), or loss measurement messages (LMM). The LB rate is 
200 PPS.   
MEPs and Services  
Megaplex-4 Ethernet main cards support Ethernet OAM functionality and host MEPs. A MEP can be 
either Down or Up, depending on its position and port association, as explained below. 
A MEP is transparent to OAM frames whose MD level is higher than the MEP level, and drops OAM 
packets whose MD level lower than the MEP level. It fully supports connectivity check (CC), loopback, 
link trace and PM counters. 
Down MEP 
Down MEPs reside at egress ports and are bound to physical ports. These MEPs receive and send CFM 
PDU from and to the network. Down MEPs are supported for either point-to-point or multipoint 
services. Different MEP locations are illustrated below. 
The following figure illustrates a point-to-point service between the CL and I/O GbE ports with the MEP 
bound to M-ETH port 4. Tx flow in the service points to a queue block. 
 
DOWN
MEP
Rx Flow
Tx Flow
M-ETH
Port 4
CL.2
Port 1
 
Point-to-Point Service with Down MEP Bound to M-ETH Port 4  
11. Monitoring and Diagnostics 
The following figure illustrates a point-to-point service between the CL and I/O GbE ports with the MEP 
bound to CL.2 port 1. Tx flow in the service points to a queue block. 
 
DOWN
MEP
Rx Flow
Tx Flow
M-ETH
Port 4
CL.2
Port 1
 
Point-to-Point Service with Down MEP Bound to CL.2 Port 1 
The Down MEP is defined over the physical port, inheriting its MAC address. The Down MEP location is 
characterized by: 
• 
Rx flow, whose classification profile can be one of the following: 
 
Untagged  
 
Single VLAN  
 
Single VLAN+P-bit 
 
Single outer + single inner VLAN 
 
Single outer VLAN + P-bit + single inner VLAN  
 
Match all. If configured over an IO port, the flow from the corresponding SAP must be used. 
It also needs a classification profile to specify the packet tag structure (as it cannot be taken 
from the flow classification profile). 
• 
Tx flow to a destination queue to forward OAM frames. 
Up MEP  
Up MEPs are bound to physical ports or bridge ports. These MEPs receive and send CFM PDU from and 
to the forwarding block. The Up MEPs inherit their MAC addresses from the corresponding 
physical/bridge ports (egress ports of Tx flows). Different MEP locations are illustrated below.  
The following figure illustrates a point-to-point service between I/O card and CL ports with the Up MEP 
bound to the I/O port. The Tx flow in this service points to the CL port. 
UP
MEP
Rx Flow
Tx Flow
M-ETH
Port 4
CL.2
Port 1
 
11. Monitoring and Diagnostics 
Point-to-Point Service with Up MEP Bound to M-ETH Port 4 
The following figure illustrates a point-to-point service between the CL.2 card and I/O ports with the Up 
MEP bound to the CL port. Tx flow in this service points to the I/O port. 
UP
MEP
Rx Flow
Tx Flow
M-ETH
Port 4
CL.2
Port 1
 
Multipoint Service with Up MEP Bound to CL.2 Port 1 
The following figure illustrates a multipoint service between any Megaplex-4 I/O module and bridge 
ports on the cL module with the Up MEP bound to the bridge port. Tx flow in this service is directed to 
the bridge port. 
Bridge
BP
BP
MEP
Rx Flow
Tx Flow
I/O Module 
Port 2
 
Multipoint Service with Up MEP Bound to Bridge Port 
Messaging System 
The Ethernet service OAM mechanism uses cyclic messages for availability verification, fault detection 
and performance data collection. The main message types are detailed below. 
Note 
OAM cyclic messages (CCMs, LBMs and LTMs) packet priority (P-bit value) is 
user-configurable at MEP level.  
CC Messages 
Continuity Check Messages (CCMs) are sent from the service source to the destination node at regular 
periodic intervals. They are used to detect loss of continuity or incorrect network connections. A CCM is 
multicast to each MEP in a MA at each administrative level. CCM status information is available at the 
MEP and RMEP levels. 
11. Monitoring and Diagnostics 
AIS 
When a MEP detects a connectivity failure at a physical port, it propagates an Alarm Indication Signal 
(AIS) in the direction away from the detected failure to the next higher level. The AIS is sent over the 
MEP Rx flow with the level as configured by the client MD level (default is the MEP level + 1) for the 
following trigger events: 
• 
LOC 
• 
LCK 
• 
Rx AIS.  
The signal is carried in dedicated AIS frames. The transmit interval is configured per MEP and can be set 
to one frame per second (default) or one frame per minute. The AIS message priority is set per MEP via 
P-bit (0–7) configuration. 
Port B
Port A
Tx Flow
Rx Flow
MEP
AIS, LCK, LOC
AIS
(with client MD level)
 
AIS Transmission 
RDI 
When a downstream MEP detects a defect condition, such as a receive signal failure or AIS, it sends a 
Remote Defect Indication (RDI) upstream in the opposite direction of its peer MEP or MEPs. This informs 
the upstream MEPs that there has been a downstream failure. The Tx RDI is also initiated when a LOC is 
detected on at least one of the associated RMEPs. 
CCM Interval 
CCM interval is user-configurable at the MA level to 3.33 ms, 10 ms, 100 ms, 1s, 1m, 10m. 
Loopback Messages 
MEPs send loopback messages (LBMs) to verify connectivity with another MEP for a specific MA. 
Loopback is a ping-like request/reply function. A MEP sends a loopback request message to another 
MEP, which generates a subsequent LBR (loopback response). LBMs/LBRs are used to verify bidirectional 
connectivity.  
11. Monitoring and Diagnostics 
The LBMs are always marked green. LBM priority uses the CCM priority that is configurable as a P-bit 
value at the MEP level. LBM CoS is set according to a P-bit-to-CoS profile, with up to four such profiles 
per chassis. 
LBMs are generated on demand and sent up to 500 times. 
Link Trace Messages 
MEPs multicast LTMs on a particular MA to identify adjacency relationships with remote MEPs at the 
same administrative level.  
LTMs can also be used for fault isolation. The message body of an LTM includes a destination MAC 
address of a target MEP that terminates the link trace. When a MIP or MEP receives an LTM, it 
generates a unicast LTR to the initiating MEP. It also forwards the LTM to the target MEP destination 
MAC address. An LTM effectively traces the path to the target MEP.  
LTM Priority  
The LTMs are always marked green. LTM priority uses the CCM priority that is configurable as a P-bit 
value at the MEP level”. 
LTM Response and Relay Behavior 
This section describes how MEPs relay and respond to LTMs, according to the Y.1731 requirements. 
In the following figure, the MEP responds with LTR if the target MAC address of the received LTM is the 
same as the MEP MAC address (inherited from the port to which the MEP is bound). LTM is not relayed. 
Main Card 
Port B
Main Card 
Port A
LTM
MEP
LTR
 
MEP with LTM Sent from the Card Port in Point-to-Point Service  
Performance Monitoring  
Megaplex-4 Ethernet service OAM PM functionality complies with the Y.1731 requirements. Megaplex-4 
provides per-service loss and delay measurement and event reporting. 
The following performance parameters are measured by appropriate OAM messages: 
11. Monitoring and Diagnostics 
• 
Frame Loss Ratio (FLR) – FLR is defined as a ratio, expressed as a percentage, of the number of 
service frames not delivered divided by the total number of service frames during a time 
interval, where the number of service frames not delivered is the difference between the 
number of service frames sent to an ingress UNI and the number of service frames received at 
an egress UNI. 
Megaplex-4 supports single-ended loss measurement (LM) with on-demand LMM transmission 
and automatic LM response. OAM MEPs measure frame loss only if statistic counters have been 
enabled on the incoming and outgoing flows. LM is not supported over tunnels. 
• 
Frame Delay (FD) – FD is specified as round trip delay for a frame, where FD is defined as the 
time elapsed since the start of transmission of the first bit of the frame by a source node until 
the reception of the last bit of the loop backed frame by the same source node, when the 
loopback is performed at the frame’s destination node. 
Megaplex-4 supports dual-ended delay measurement (DM) with on-demand DMM transmission 
and automatic DM response. Measurement is performed for delay of up to 1 second with full 
DM over tunnels. 
Configuring OAM  
 To configure the service OAM: 
1. Configure general OAM parameters   
2. Add and configure maintenance domain(s) (MD). 
3. Configure maintenance associations for the added MDs. 
4. If you want to define global MIP operation, enable the necessary MD level MIP from 0 to 7.  
5. If Megaplex-4 is acting as a MEP: 
d. Configure MA endpoints, referred as MEPs. 
e. Configure MEP services. 
f. Configure Destination NEs.  
g. Configure the necessary flows from and to the unit(s). 
Configuring OAM CFM General Parameters 
If necessary you can define general OAM CFM parameters. You can also display OAM CFM information.   
11. Monitoring and Diagnostics 
Configuring Multicast MAC Address 
 To configure the OAM CFM multicast MAC address: 
• 
Navigate to the CFM (Connectivity Fault Management) context (config>oam>cfm) and enter:  
multicast-addr <mac-address> 
Configuring Measurement Bin Profiles 
You can define measurement bin profiles to define sets of threshold ranges for displaying delay 
measurements in destination NEs. 
 To define measurement bin profiles: 
1. Navigate to configure oam cfm. 
The config>oam>cfm prompt is displayed. 
2. Enter the measurement bin profile level by typing the following: 
 
measurement-bin-profile <name> 
The prompt config>oam>cfm>measurement-bin-prof(<name>)# is displayed. 
3. Specify the thresholds (single value, or values separated by commas). 
 
thresholds <thresholds-list> 
Each value is used as the upper range of a set of thresholds, up to 5,000,000. For instance, 
entering thresholds 500,1000,15000 results in this set of threshold ranges: 
 
0–500 
 
501–1,000 
 
1,001–15,000 
 
15,001–5,000,000. 
4. Specifying the Ethertype expected in Ethernet packet). 
 
Ethertype  <0x0000-0xFFFF>  
Configuring and Displaying Delay Measurement Bins (Example) 
 To configure and display delay measurement bins: 
• 
Bin1 used for round trip delay measurements, with threshold ranges:  
 
0–15,000 
 
15,001– 49,000 
 
49,001–55,000 
11. Monitoring and Diagnostics 
 
55,001–250,000 
 
250,001–5,000,000. 
• 
Bin2 used for round trip delay variation measurements, with threshold ranges: 
 
0–15,000 
 
15,001– 55,000 
 
55,001–105,000 
 
105,001–205,000 
 
205,001–5,000,000. 
config>oam>cfm# measurement-bin-profile bin1 
config>oam>cfm>measurement-bin-prof(bin1)# thresholds 15000,49000,55000,250000 
config>oam>cfm>measurement-bin-prof(bin1)# exit 
config>oam>cfm# measurement-bin-profile bin2 
config>oam>cfm>measurement-bin-prof(bin2)# thresholds 15000,55000,105000,205000 
config>oam>cfm>measurement-bin-prof(bin2)# exit 
config>oam>cfm# ma 1 ma 1 mep 1 serv 1 dest-ne 3 
config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)>dest-ne(3)# delay-measurement-bin profile bin1 
config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)>dest-ne(3)# delay-var-measurement-bin profile 
bin2 
config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)>dest-ne(3)# show delay-measurement-bins rt-delay 
all 
Type : rt Delay 
 
Current 
----------------------------------------------------------------------------- 
Bin  range                    Rx DMR 
     (us) 
----------------------------------------------------------------------------- 
1    0..15000                 0 
2    15001..49000             0 
3    49001..55000             0 
4    55001..250000            0 
5    250001..5000000          0 
 
Type : rt Delay 
 
Interval  Bin  range                    Rx DMR 
               (us) 
----------------------------------------------------------------------------- 
1         1    0..15000                 36 
1         2    15001..49000             0 
1         3    49001..55000             0 
1         4    55001..250000            0 
1         5    250001..5000000          0 
2         1    0..15000                 753 
2         2    15001..49000             0 
2         3    49001..55000             0 
2         4    55001..250000            0 
11. Monitoring and Diagnostics 
2         5    250001..5000000          0 
3         1    0..15000                 713 
3         2    15001..49000             0 
3         3    49001..55000             0 
3         4    55001..250000            0 
3         5    250001..5000000          0 
 
config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)>dest-ne(3)# show delay-measurement-bins 
rt-delay-var all 
Type : rt Delay Var 
 
Current 
----------------------------------------------------------------------------- 
Bin  range                    Rx DMR 
     (us) 
----------------------------------------------------------------------------- 
1    0..15000                 0 
2    15001..55000             0 
3    55001..105000            0 
4    105001..205000           0 
5    205001..5000000          0 
 
Type : rt Delay Var 
 
Interval  Bin  range                    Rx DMR 
               (us) 
----------------------------------------------------------------------------- 
1         1    0..15000                 36 
1         2    15001..55000             0 
1         3    55001..105000            0 
1         4    105001..205000           0 
1         5    205001..5000000          0 
2         1    0..15000                 753 
2         2    15001..55000             0 
2         3    55001..105000            0 
2         4    105001..205000           0 
2         5    205001..5000000          0 
3         1    0..15000                 713 
3         2    15001..55000             0 
3         3    55001..105000            0 
3         4    105001..205000           0 
3         5    205001..5000000          0 
Displaying OAM CFM Information 
You can display OAM CFM information by typing show summary, as shown in the following. 
# configure oam cfm 
# config>oam>cfm# show summary 
 
 
 
md 
slot/ classifi 
admin mep 
ok/total 
md/ma/mepid 
md/ma name 
 
lvl 
port 
cation status def 
r.meps 
 
11. Monitoring and Diagnostics 
001/001/001 
MD1/MA1 
 
3 
eth1 
100 
enable off 
1/1 
002/002/8191 1234567890123456789012 
3 
eth1 
0 
disable 
 
34567890/1234567801234 
002/005/123 
1234567890123456789012 
3 
eth1 
100/ 
enable off 
0/2 
 
34567890/155  
 
 
200 
002/006/101 
1234567890123456789012 
3 
eth3 
untagged 
enable off 
0/3 
003/001/001 
/iccname 
 
4 
eth1 
100.1 enable off 
0/1 
004/001/001 
20-64-32-AB-CD-64 120/ 
0 
eth1 
4000 
enable off 
0/1 
 
MA1 
004/002/001 
20-64-32-AB-CD-64 120/ 
0 
eth1 
3000/ enable off 
0/3 
 
12345678901234567890123 
Configuring Maintenance Domains 
MDs are domains for which the connectivity faults are managed. Each MD is assigned a name that must 
be unique among all those used or available to an operator. The MD name facilitates easy identification 
of administrative responsibility for the maintenance domain.  
 To add a maintenance domain: 
• 
At the config>oam>cfm# prompt, enter maintenance-domain <mdid> 
where <mdid> is 1–128. 
The maintenance domain is created and the config>oam>cfm>md(<mdid>)$ prompt is 
displayed. 
 To delete a maintenance domain: 
• 
At the config>oam>cfm# prompt, enter no maintenance-domain <mdid>. 
The maintenance domain is deleted. 
 To configure a maintenance domain: 
1. Navigate to configure oam cfm maintenance-domain <mdid> to select the maintenance domain 
to configure. 
The config>oam>cfm>md(<mdid>)# prompt is displayed 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Configuring maintenance 
association for the MD 
maintenance -association <maid> 
no maintenance –association <maid> 
Refer to Error! Reference source not 
found.. 
no maintenance –association <maid> 
deletes the MA 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Specifying the 
maintenance domain level 
md-level <md-level> 
The allowed range for md-level is 0–7 
Note: If pre-standard OAM protocol is 
being used, the only value allowed for 
the maintenance domain level is 3. 
Specifying the name 
format and name of the 
maintenance domain 
name string <md-name-string> 
name dns <md-name-string> 
name mac-and-uint <md-name-mac> 
<md-name-uint> 
no name 
• Maximum length of md-name-string 
is 43 characters 
• Maximum combined length of 
md-name-string and ma-name-string 
(maintenance association name) is 
48 characters 
• Format mac-and-uint – Specify 
md-name-mac as xx-xx-xx-xx-xx-xx, 
and md-name-uint as an unsigned 
integer decimal number (0–65535) 
• If prestandard OAM protocol is being 
used, the maintenance domain must 
have no name (use command no 
name). 
Specifying the OAM 
protocol type 
no proprietary-cc 
proprietary-cc 
• Use no proprietary-cc for standard 
OAM protocol 
• Use proprietary-cc for prestandard 
OAM protocol. 
Note: The MD must have no name (via 
no name) and the level must be 3 
before you can set the protocol to 
prestandard. 
Displaying information on 
configured MAs 
show maintenance-association <maid> 
 
Configuring Maintenance Associations 
A maintenance domain contains maintenance associations, for each of which you can configure the 
continuity check interval and maintenance endpoints (MEPs). 
 To add a maintenance association (MA): 
• 
At the config>oam>cfm>md(<mdid>)# prompt enter: maintenance-association <maid> 
where <maid> is 1–128. 
11. Monitoring and Diagnostics 
The maintenance association is created and the config>oam>cfm>md(<mdid>)>ma(<maid>)$ 
prompt is displayed. 
 To delete a maintenance association: 
• 
At the config>oam>cfm>md(<mdid>)# prompt enter: no maintenance-association <maid>. 
The maintenance association is deleted. 
 To configure a maintenance association: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
to select the maintenance association to configure. 
The config>oam>cfm>md(<mdid>)>ma(<maid>)# prompt is displayed 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying the interval 
between continuity check 
messages 
ccm-interval {3.33ms | 10ms | 
100ms | 1s | 10s | 1min | 
10min} 
 
Associating the MA with a 
VLAN 
classification vlan <vlan-id> 
Verify that the VLAN is the same as the VLAN 
associated with the MEP 
Note: If a classifier profile is associated with 
the MEP, the VLAN should be set to 0. 
Configuring MEP for the MA 
mep <mepid> 
Refer to Error! Reference source not found.  
Configuring Maintenance Endpoints 
Maintenance endpoints reside at the edge of a maintenance domain. They initiate and respond to 
CCMs, link trace requests, and loopbacks, in order to detect, localize, and diagnose connectivity 
problems. Megaplex-4 supports up to 128 MEPs.  
 To add a maintenance endpoint (MEP): 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)# prompt, enter: 
 mep <mepid> 
where <mepid> is 1–8191. 
The MEP is created and the prompt 
config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)$ is displayed. 
11. Monitoring and Diagnostics 
 To delete a maintenance endpoint: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)# prompt, enter: 
no mep <mepid> 
 
The maintenance endpoint is deleted. 
Note 
You can remove a maintenance endpoint regardless of whether it contains 
services.  
 To configure a maintenance endpoint: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid>to select the maintenance endpoint to configure. 
The prompt config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Enabling sending AIS and 
defining the interval  
ais [ interval { 1s | 1min }] 
[priority <priority>] 
To disable AIS sending, enter no ais 
Binding the MEP to an Ethernet 
port, Logical Mac, bridge port, 
or LAG  
 
bind ethernet <slot/port> 
[/tributary]> 
bind logical-mac <slot/port> 
bind bridge-port <bridge-
number><port> 
bind lag <lag name> 
To remove the MEP from a port, enter 
no bind 
 
Enabling initiation of continuity 
check messages (CCM) 
ccm-initiate  
To disable initiating continuity check 
messages, enter no ccm-initiate 
Specifying the priority of CCMs, 
LBMs and LTMs transmitted by 
the MEP 
ccm-priority <priority> 
The allowed range for <priority> is 0–7 
Associating the MEP with a 
classifier profile or VLAN 
classification vlan <vlan-id> 
classification profile 
<profile-name> 
 
You can associate more than one MEP 
to the same VLAN if the MEPs belong to 
MDs with different levels 
Verify that the VLAN is the same as the 
VLAN associated with the MA 
Defining client MD level 
client-md-level <md_level> 
Client MD level is a level for sending 
upstream AIS 
Defining the MEP direction 
direction {up | down} 
 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Specifying continuity 
verification method 
continuity-verification <cc-based 
| lb-based> 
This parameter is visible only in 
prestandard mode and can be 
configured only if ccm-initiate is 
enabled as explained above. Use 
lb-based only for RAD proprietary OAM 
functionality. 
Defining the MAC address type 
sent in OAM continuity check 
messages (CCM) and 
performance measurement 
messages (PM) 
dest-addr-type [ccm {unicast | 
multicast}] [pm {unicast | 
multicast}] 
If more than one remote MEP ID has 
been defined for the MEP and you 
change the CCM destination address 
type from multicast to unicast, all 
remote MEP IDs are deleted except for 
the lowest remote MEP ID. 
If the MAC address type for PM 
messages is unicast, then the MAC 
address for the transmission of PM 
messages is determined by the 
configuration of the destination NE. If a 
remote MAC address is configured for 
the destination NE, that MAC is used. 
Otherwise if a remote MEP ID is 
configured for the destination NE, the 
remote MAC address is learned from 
CCM messages. Refer to Error! 
Reference source not found. for details. 
Defining a unicast MAC address 
if you defined unicast MAC 
address type for CCM messages 
with the dest-addr-type 
command 
dest-mac-addr <mac-addr> 
MAC address is in format 
xx-xx-xx-xx-xx-xx 
Defining direction 
direction { up | down } 
E-line service to Gbe ports does not 
work with UP MEP when two CL 
modules are configured. 
Defining forwarding method 
forwarding-method 
{ e-line | e-lan }  
Currently only e-line is supported. 
 
Defining the queue for the MEP 
queue fixed <queue-id> 
[block <level-id>/<queue-id>] 
queue queue-mapping 
<queue_mapping_profile_nam
e> 
[block <level_id>/<queue_id>] 
To delete queue assignment, enter no 
queue queue-mapping 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Performing OAM link trace 
linktrace 
See Error! Reference source not found.  
Activating OAM loopback 
lbm 
See Error! Reference source not found.  
Defining remote MEP with 
which the MEP communicates 
remote-mep <remote_mep_id> 
no remote-mep 
<remote_mep_id> 
Allowed range for remote MEP is 1–
8191 
The MEP ID and the remote MEP ID 
must be different. You can define up to 
511 remote MEPs for the local MEP if 
standard OAM protocol is being used 
for the MD and the destination address 
type is multicast; otherwise you can 
define only one remote MEP. 
To delete remote MEP, enter no 
remote-mep <remote_mep_id> 
Configuring service for the MEP 
service <service_id> 
Refer to Configuring Maintenance 
Endpoint Services  
Displaying MEP status 
show status  
 
Displaying remote MEP status 
show remote-mep 
<remote-mep-id> status  
 
Administratively enabling MEP 
no shutdown 
To deactivate the MEP, enter shutdown 
Configuring Maintenance Intermediate Points  
Megaplex-4 provisions a MIP for each flow at each physical port, bridge port, and ring port. This type of 
MIPs is called MD-level MIP. If you want to define global MIP operation, enable the necessary MD level 
MIP from 0 to 7.  
 To add an MD-level MIP: 
• 
At the config>oam>cfm# prompt, enter md-level-mip <md-level-list> in the range of 0 to 7. 
The MD levels in the list can be separated by a comma or given as a range, for example: 1..3,5. 
Note 
Do not type a space after any commas in the list.  
Typing no md-level-mip <md-level-list> removes the specified MD-level MIP. 
11. Monitoring and Diagnostics 
Examples 
Configuring MD, MA, and MEP 
This example illustrates configuring the following: 
• 
MD ID 1 
• 
MA ID 1 
• 
MEP ID 1:  
 
Remote MEP ID 2 
 
Classification VLAN 100. 
 To configure MD, MA, and MEP:  
#**************************Configure MD  
exit all 
configure oam cfm 
maintenance-domain 1 
 
#**************************Configure MA 
maintenance-association 1 
classification vlan 100 
 
#**************************Configure MEP 
mep 1 
classification vlan 100 
bind ethernet cl-a 1 
queue fixed 1 block 0/1 
remote-mep 2 
no shutdown 
exit all 
 To display the configured MD, MA, and MEP:  
# configure oam cfm maintenance-domain 1 
config>oam>cfm>md(1)# info detail 
    no proprietary-cc 
    md-level  3 
    name  string  "MD1" 
        maintenance-association  1 
        name  string  "MA1" 
        ccm-interval  1s 
        classification vlan  100 
                mep  1 
11. Monitoring and Diagnostics 
            bind  ethernet cl-a 1 
            classification  vlan  100 
            queue  fixed  0 block  0/1 
            remote-mep  2 
            dest-addr-type ccm  multicast pm  unicast 
            ccm-initiate 
            ccm-priority  0 
            forwarding-method  e-line 
            direction  down 
            client-md-level  4 
            no ais 
            no shutdown 
        exit 
    exit 
Displaying MEP Status and Remote MEP Status 
The following illustrates displaying MEP status and remote MEP status. 
 To display MEP status: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, enter: show 
status. 
The MEP status information is displayed. 
config>oam>cfm>md(1)>ma(1)>mep(100)# show status 
Port      : Ethernet                 cl-a/1 
Direction : Down 
VLAN      : 10           Priority  : 0 
 
MD Name               : MD1 
MA Name               : MA1 
Administrative Status : Up 
 
MEP Defect                                          Status 
Rx LCK                                              Off 
Rx AIS                                              Off 
Cross Connected CCM (Mismatch; Unexpected MD Level) Off 
Invalid CCM (Unexpected MEP; Unexpected CCM Period) Off 
 
Remote MEP  Remote MEP Address  Operational Status 
---------------------------------------------------------------1           00-20-D2-
50-0F-D9   OK 
11. Monitoring and Diagnostics 
 To display Remote MEP status: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, enter: show 
remote-mep <remote-mep ID> status. 
The MEP status information is displayed. 
config>oam>cfm>md(1)>ma(1)>mep(100)# show remote-mep 1 status 
Remote MEP Address : 00-20-D2-50-0F-D9 
Operational Status : OK 
Configuring Maintenance Endpoint Services 
You can configure up to 8 services on a MEP. The service configures performance monitoring (Y.1731) 
functionality for loss and delay measurements. 
 To add a MEP service: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, enter: service 
<serviceid> 
where <serviceid> is 1–8. 
The prompt config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service(<serviceid>)$ 
is displayed. 
 To configure a MEP service: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid> service <serviceid> to select the service to configure (<serviceid> is1–8). 
The prompt config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service(<serviceid>)# 
is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Associating this service with 
a priority for LMMs and 
DMMs 
classification priority-bit <p-bit> 
The allowed range is 0–7 
Specifying delay threshold in 
microseconds 
delay-threshold <delay-thresh> 
The allowed range for delay 
threshold is: 1–5,000,000. If 
the threshold is exceeded, the 
service is declared as 
degraded. 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Specifying delay variation 
threshold in microseconds 
delay-var-threshold 
<delay-var-thresh> 
The allowed range for delay 
variation threshold is:  
1–5,000,000. If the threshold 
is exceeded, the service is 
declared as degraded. 
Specifying the interval for 
delay measurement 
messages, to be used by all 
remote NEs defined for 
service 
dmm-interval {100ms | 1s | 10s} 
 
Specifying the interval for 
loss measurement 
messages, to be used by all 
remote NEs defined for 
service 
lmm-interval {100ms | 1s | 10s} 
 
Configuring destination NE 
for service 
dest-ne <dest-ne-index> 
See Error! Reference source 
not found. below. The value 
range is 
1–255. One NE per service is 
allowed. 
To delete a destination NE, 
enter no dest-ne. 
Activating the MEP service 
no shutdown 
You can activate a service only 
if the corresponding MEP is 
active and you have defined 
at least one destination NE 
Configuring Destination NEs 
For performance measurement, the exact address of the destination NE must be known. You can 
configure the remote MAC address of the NE, or Megaplex-4 can learn it from the CCM messages.  
If the remote MAC address is not configured and needs to be learned, performance measurement 
messages are sent with all 0s in the MAC address until the address is learned.  
 To add a destination NE: 
• 
At the prompt config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service 
(<serviceid>)#, enter: dest-ne <dest-ne-index> 
11. Monitoring and Diagnostics 
where <dest-ne-index> is 1–255. 
The prompt config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service(<serviceid>)> 
dest-ne(<dest-ne-index>)$ is displayed. 
 To configure a destination NE: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid> service <serviceid> dest-ne <dest-ne-index> to select the destination NE to 
configure. 
The prompt 
config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service(<serviceid>)>dest-
ne(<dest-ne-index>)# is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Enabling two-way delay  
measurement method 
delay two-way 
[data-tlv-length <length-val>] 
 
Defining the delay 
measurement bin profile 
to use as delay bin policy 
delay-measurement-bin 
profile <name> 
The delay measurement bin profiles 
are defined in the conf>oam>cfm level 
Assigning the delay 
variation measurement 
bin profile 
delay-var-measurement-bin 
profile <name> 
The delay measurement bin profiles 
are defined in the conf>oam>cfm level 
Defining single-ended loss  
measurement method 
loss single-ended [{ synthetic | 
user-data | lmm-synthetic }] 
• user-data – This method measures 
user data and CCM messages. 
• synthetic – This method measures 
DM frames. It is recommended 
when working with devices that do 
not count user data frames 
• lmm-synthetic – This method 
measures synthetic frames as well. 
Defining the MAC address 
of the destination NE 
remote mac-address <mac> 
If the MAC address is 
00-00-00-00-00-00, the statistic 
counters for the destination NE do not 
increment 
Defining the remote MEP 
ID of the destination NE 
remote mep-id 
<remote-mep-id> 
 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Displaying the delay 
measurement bins for 
delay measurements via 
DMRs  
show delay-measurement-bins 
show delay-measurement-bins 
{rt-delay | rt-delay-var} current 
 - show 
delay-measurement-bins 
{rt-delay | rt-delay-var} interval 
<interval-num> 
 - show 
delay-measurement-bins 
{rt-delay | rt-delay-var} all  
Relevant only if profiles were assigned 
via delay-measurement-bin, 
delay-var-measurement-bin 
Displaying statistics data 
show statistics  
 
Clearing statistics 
clear-statistics  
 
Configuring OAM CFM Service Event Reporting 
In addition to the regular OAM statistics collection, Megaplex-4 supports proactive SLA measurements 
per OAM service, as per RMON-based RFC 2819. The device sends reports when one of the counters 
rises above or drops below the set thresholds within the specified sampling period of time. These 
reports can be sent as SNMP traps to the defined network management stations, or written to the event 
log.  
The following counters can be monitored: 
• 
Far End Frame Loss Ratio – Total number of OAM frames lost from the local MEP to the remote 
MEP, divided by the total number of OAM frames transmitted since the service was activated 
• 
Near End Frame Loss Ratio – Total number of OAM frames lost from the remote MEP to the 
local MEP, divided by the total number of OAM frames transmitted since the service was 
activated 
• 
Frames Above Delay – Number of frames that exceeded the delay threshold 
• 
Frames Above Delay Variation – Number of frames exceeding the delay threshold 
• 
Far End Unavailability Ratio – Total number of far end unavailable seconds divided by the time 
elapsed since the service was activated 
• 
Near End Unavailability Ratio – Total number of near end unavailable seconds divided by the 
time elapsed since the service was activated. 
11. Monitoring and Diagnostics 
 To configure the event reporting for a service: 
1. Navigate to configure fault cfm. 
2. Specify the service and counter for which you wish to configure event reporting: 
service md <mdid> ma <maid> mep <mepid> service <serviceid> {above-delay | 
above-delay-var | far-end-loss-ratio | near-end-loss-ratio | far-end-unavailability-ratio | 
near-end-unavailability-ratio} 
The prompt config>fault>cfm>service(<mdid>/<maid>/<mepid>/<serviceid>)# is displayed. 
3. Specify the type of event reporting for the counter: 
 
For counters above-delay and above-delay-var: 
frames-report [event {none | log | trap | logandtrap}] [rising-threshold <rising-threshold>] 
[falling-threshold <falling-threshold>] [sampling-interval <value>] 
 
For counters near-end-loss-ratio or far-end-loss-ratio: 
frames-report [event {none | log | trap | logandtrap}] [rising-threshold {1e-3 | 1e-4 | 1e-5 
| 1e-6 | 1e-7 | 1e-8 | 1e-9 | 1e-10}] [falling-threshold {1e-3 | 1e-4 | 1e-5 | 1e-6 | 1e-7 | 
1e-8 | 1e-9 | 1e-10}] 
 
For counters near-end-unavailability-ratio or far-end-unavailability-ratio: 
frames-report [event {none | log | trap | logandtrap}] [rising-threshold <rising-threshold>] 
[falling-threshold <falling-threshold>]  
4. Type no shutdown to activate the event reporting for the counter. 
Parameter 
Description 
Possible Values 
event 
Specifies the type of event reporting 
none – The event is not reported 
log – The event is reported via the event 
log 
trap –An SNMP trap is sent to report the 
event 
logandtrap –The event is reported via 
the event log and an SNMP trap 
11. Monitoring and Diagnostics 
Parameter 
Description 
Possible Values 
rising-threshold 
falling-threshold 
A value above rising-threshold 
within the sampling interval for the 
particular event is considered a rising 
event occurrence 
A value below falling-threshold 
within the sampling interval for the 
particular event is considered a  
falling event occurrence 
• For counters above-delay or 
above-delay-var:  
1–60 
• For counters near-end-loss-ratio or 
far-end-loss-ratio: 
1e-3 
1e-4 
1e-5 
1e-6 
1e-7 
1e-8 
1e-9 
1e-10 
• For counters 
near-end-unavailability-ratio or 
far-end-unavailability-ratio: 
1–100 
Note: Rising threshold must be greater 
than falling-threshold. 
sampling-interval 
Specifies the interval in seconds over 
which the data is sampled and 
compared to the rising and falling 
thresholds 
Notes:  
• Relevant only for counters 
above-delay or above-delay-var 
• Sampling interval value must be at 
least double rising threshold. 
For example: 
 To configure OAM CFM event reporting: 
• 
Configure counters for the following service, as shown in the table below: 
 
Maintenance domain 5 
 
Maintenance association 8 
 
MEP 3  
 
Service 4. 
The delay and delay variation (jitter) threshold for this service are set to 10 and 5 milliseconds 
respectively. The reporting counters for this service are set as shown in the table below. 
11. Monitoring and Diagnostics 
Counter 
Event Type 
Rising Threshold 
Falling 
Threshold 
Sampling 
Interval 
Frames Above Delay 
Log and 
trap 
4 
2 
8 
Frames Above Delay 
Variation 
Log 
10 
5 
30 
Far End Frame Loss Ratio 
Trap 
1e-4   
1e-8 
 
Near End Frame Loss Ratio 
Log and 
trap 
1e-9   
1e-10 
 
Far End Unavailability Ratio  
Trap 
40 
20 
 
Near End Unavailability 
Ratio 
Log 
50 
25 
 
In this example, an SNMP trap and an event are generated as notification of the rising threshold if during 
an 8-second sample interval, four DMM packets or more exceed the 10-milliseconds delay threshold of 
this service. The alarm is cleared (falling threshold) if Megaplex-4 detects an 8-second sample interval in 
which two or fewer packets cross the thresholds. 
A rising or falling threshold event is generated if a specific ratio is exceeded. For example, an SNMP trap 
is sent if the far end Frame Loss Ratio (from Megaplex-4 to the network) exceed 10^-4, i.e. more than 
one frame out of 10,000 LMMs sent for this service are lost. 
 To define the service delay thresholds: 
# configure oam cfm ma 5 ma 8 mep 3 service 4 
config>oam>cfm>md(5)>ma(8)>mep(3)>service(4)delay-threshold 10 
config>oam>cfm>md(5)>ma(8)>mep(3)>service(4) delay-var-threshold 5 
 
 To define the service event reporting counters: 
# configure fault cfm 
config>fault>cfm# service md 5 ma 8 mep 3 service 4 above-delay 
config>fault>cfm>service(5/8/3/4/above-delay)$ frames-report event logandtrap rising-
threshold 4 falling-threshold 2 sampling-interval 8 
config>fault>cfm>service(5/8/3/4/above-delay)$ no shutdown 
config>fault>cfm>service(5/8/3/4/above-delay)$ exit 
 
config>fault>cfm# service md 5 ma 8 mep 3 service 4 above-delay-var 
config>fault>cfm>service(5/8/3/4/above-delay-var)$ frames-report event log rising-
threshold 10 falling-threshold 5 sampling-interval 30 
11. Monitoring and Diagnostics 
config>fault>cfm>service(5/8/3/4/above-delay-var)$ no shutdown 
config>fault>cfm>service(5/8/3/4/above-delay-var)$ exit 
 
config>fault>cfm# service md 5 ma 8 mep 3 service 4 far-end-loss-ratio 
config>fault>cfm>service(5/8/3/4/far-end-loss-ratio)$ frames-report event trap 
rising-threshold 1e-4 falling-threshold 1e-8 
config>fault>cfm>service(5/8/3/4/far-end-loss-ratio)$ no shutdown 
config>fault>cfm>service(5/8/3/4/far-end-loss-ratio)$ exit 
 
config>fault>cfm# service md 5 ma 8 mep 3 service 4 near-end-loss-ratio 
config>fault>cfm>service(5/8/3/4/near-end-loss-rati)$ frames-report event logandtrap 
rising-threshold 1e-9 falling-threshold 1e-10 
config>fault>cfm>service(5/8/3/4/near-end-loss-rati)$ no shutdown 
config>fault>cfm>service(5/8/3/4/near-end-loss-rati)$ exit 
 
config>fault>cfm# service md 5 ma 8 mep 3 service 4 far-end-unavailability-ratio 
config>fault>cfm>service(5/8/3/4/far-end-unavailabi)$ frames-report event trap 
rising-threshold 40 falling-threshold 20 
config>fault>cfm>service(5/8/3/4/far-end-unavailabi)$ no shutdown 
config>fault>cfm>service(5/8/3/4/far-end-unavailabi)$ exit 
 
config>fault>cfm# service md 5 ma 8 mep 3 service 4 near-end-unavailability-ratio 
config>fault>cfm>service(5/8/3/4/near-end-unavailab)$ frames-report event log 
rising-threshold 50 falling-threshold 25 
config>fault>cfm>service(5/8/3/4/near-end-unavailab)$ no shutdown 
config>fault>cfm>service(5/8/3/4/near-end-unavailab)$ exit 
 To display the defined service event reporting counters: 
config>fault>cfm# info detail 
    service md  5 ma  8 mep  3 service  4  above-delay 
        frames-report event  logandtrap rising-threshold  4 falling-threshold  2 
sampling-interval  8 
        no shutdown 
    exit 
    service md  5 ma  8 mep  3 service  4  above-delay-var 
        frames-report event  log rising-threshold  10 falling-threshold  5 sampling-
interval  30 
        no shutdown 
    exit 
    service md  5 ma  8 mep  3 service  4  far-end-loss-ratio 
        frames-report event  trap rising-threshold  1e-4 falling-threshold  1e-8 
        no shutdown 
    exit 
    service md  5 ma  8 mep  3 service  4  near-end-loss-ratio 
        frames-report event  logandtrap rising-threshold  1e-9 falling-threshold  
1e-10 
11. Monitoring and Diagnostics 
        no shutdown 
    exit 
    service md  5 ma  8 mep  3 service  4  far-end-unavailability-ratio 
        frames-report event  trap rising-threshold  40 falling-threshold  20 
        no shutdown 
    exit 
    service md  5 ma  8 mep  3 service  4  near-end-unavailability-ratio 
        frames-report event  log rising-threshold  50 falling-threshold  25 
        no shutdown 
    exit 
Displaying OAM CFM Statistics 
You can display end-to-end performance monitoring data for the OAM services and destination NEs. The 
statistics for a service are calculated from the statistics for its destination NEs. 
Megaplex-4 measures performance in fixed 15-minute intervals. It also stores performance data for the 
last 12 hours (48 intervals).  
You can view the following types of statistics for services and destination NEs: 
• 
Running –OAM statistics collected since the corresponding service was activated 
• 
12 hours – OAM statistics for the last 12 hours, or the amount of time since the service was 
activated, if less than 12 hours. 
• 
Interval – OAM statistics for the current interval or a selected interval. You can select an interval 
only if it has already ended since the corresponding service was activated.  
When a service is first activated, you can view statistics for only the current interval. The 
statistics data is shown for the time elapsed since the beginning of the interval. When the 
current interval ends, it becomes interval 1 and you can select it for viewing interval statistics. 
After each interval ends, you can select it for viewing interval statistics. 
 To display the OAM CFM statistics for a service or destination NE: 
1. Navigate to the level corresponding to the OAM service or destination NE for which you wish to 
view the statistics (configure oam cfm maintenance-domain <mdid> 
maintenance-association <maid> mep <mepid> service <serviceid> or configure oam cfm 
maintenance-domain <mdid> maintenance-association <maid> mep <mepid> 
service <serviceid> dest-ne <dest-ne-index>). 
The prompt for service or destination NE is displayed: 
config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service(<serviceid>)# 
11. Monitoring and Diagnostics 
config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service(<serviceid>)> 
dest-ne(<dest-ne-index>)# 
2. Enter all necessary commands according to the tasks listed below. 
Note 
The service for which you wish to view the statistics must be active. If the 
service is not active, the commands to view statistics are not recognized 
 
Task 
Command 
Comments 
Viewing running statistics 
show statistics running 
The statistics are displayed; 
refer to the tables below.   
Viewing statistics for the 
current interval 
show statistics current 
The statistics for the current 
interval are displayed; refer to 
the tables below.  
Viewing the statistics for a 
selected interval 
show statistics interval 
<interval-num> 
• Allowed values for 
interval-num: 1–48 
• The statistics for the 
selected interval are 
displayed; refer to the 
tables below. 
• If you specified an interval 
that has not yet ended 
since the service was 
activated, a message is 
displayed that the interval 
doesn’t exist. 
Viewing statistics for 12 hours   
show statistics 12-hours   
The statistics for the past 12 
hours are displayed; refer to 
the tables below. 
Viewing running statistics, 
statistics for the current 
interval, statistics for all 
intervals, and 12-hour 
statistics 
show statistics all 
The statistics are displayed; 
refer to the tables below. 
Viewing statistics for all 
intervals 
show statistics all-intervals 
The statistics for all intervals 
are displayed; refer to the 
tables below. 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Clearing the statistics for the 
service or destination NE 
clear-statistics 
All statistics data for the 
service or destination NE are 
cleared, including the stored 
interval data, except for the 
elapsed time since the start of 
the current interval 
OAM Statistic Counters 
Parameter 
Description 
Far End Tx Frames  
Total number of frames transmitted from local destination NE to 
remote destination NE since the service was activated (the type of 
frames counted is either user data or synthetic, according to the 
method configured by the loss single-ended command) 
Far End Rx Frames 
Total number of frames received by remote destination NE since 
the service was activated (the type of frames counted is either 
user data or synthetic, according to the method configured by the 
loss single-ended command) 
Far End Lost Frames 
Total number of frames lost from local destination NE to remote 
destination NE since the service was activated (Far End Tx Frames 
- Far End Rx Frames) (the type of frames counted is either user 
data or synthetic, according to the method configured by the loss 
single-ended command) 
Far End Frame Loss Ratio (%) 
Far End Lost Frames divided by Far End Tx Frames 
11. Monitoring and Diagnostics 
Parameter 
Description 
Far End Unavailable Seconds (Sec) 
Number of seconds the remote destination NE is considered 
unavailable. The definition of unavailability differs according to 
user data or synthetic measurement mode, as configured by the 
loss single-ended command: 
• User data – The destination NE is considered unavailable  after 
10 consecutive seconds with SES (Severely Errored Second) 
events; the 10 seconds are part of the unavailable time. An SES 
is considered to have occurred if more than one frame out of 
1000 is lost. The destination NE is considered available again 
after 10 consecutive non-SES events; the 10 seconds are part 
of the available time.  
• Synthetic mode – The destination NE is considered unavailable  
after 3.5 consecutive seconds with no reception of synthetic 
frames; the 3.5 seconds are part of the unavailable time. The 
destination NE is considered available again when a synthetic 
frame is received. 
Near End Tx Frames  
Total number of frames transmitted from remote destination NE 
to local destination NE since the service was activated (the type of 
frames counted is either user data or synthetic, according to the 
method configured by the loss single-ended command) 
Near End Rx Frames 
Total number of frames received by local destination NE since the 
service was activated (the type of frames counted is either user 
data or synthetic, according to the method configured by the loss 
single-ended command) 
Near End Lost Frames 
Total number of frames lost from remote destination NE to local 
destination NE since the service was activated 
(Near End Tx Frames - Near End Rx Frames) (the type of frames 
counted is either user data or synthetic, according to the method 
configured by the loss single-ended command) 
Near End Frame Loss Ratio (%) 
Near End Lost Frames divided by Near End Tx Frames 
Near End Unavailable Seconds 
(Sec) 
Number of seconds the local destination NE is considered 
unavailable. Refer to the description of Far End Unavailable 
Seconds for the definition of unavailability. 
Current Delay (uSec)  
Current delay received in the last Delay Measurement Reply 
(DMR)  
Current Delay Variation (uSec) 
Difference between the current delay value and the previous 
current delay value  
Average Two Way Delay (uSec)  
Average of all frame delay values received in DM frames 
11. Monitoring and Diagnostics 
Parameter 
Description 
Average Two Way Delay Var 
(uSec) 
Average difference between the frame delay values received in 
DM frames 
Frames Above Delay Threshold 
Number of DM frames whose delay value exceeded the delay 
threshold configured for the service 
Frames Above Delay Variation 
Threshold 
Number of DM frames whose delay variation exceeded the delay 
variation threshold configured for the service 
Elapsed Time (sec)   
Time (in seconds) elapsed since the service was activated 
OAM Delay and Loss Measurement Counters  
Parameter 
Description 
Transmitted LMMs 
Number of transmitted loss measurement messages 
Transmitted DMMs 
Number of transmitted delay measurement messages 
Received LMRs 
Number of received loss measurement replies 
Received DMRs 
Number of received delay measurement replies 
The requested statistics is dispayed, for example as follows. 
config>oam>cfm>md(1)>ma(1)>mep(100)>service(1)>dest-ne(1)# show statistics 
running 
Running Counters 
--------------------------------------------------------------- 
Far End TX Frames                      : 1483 
Far End RX Frames                      : 1483 
Far End Lost Frames                    : 0 
Far End Unavailable Seconds (Sec)      : 0 
 
Near End TX Frames                     : 1483 
Near End RX Frames                     : 1483 
Near End Lost Frames                   : 0 
Near End Unavailable Seconds (Sec)     : 0 
 
Current Delay (mSec)                   : 0.066 mSec 
Current Delay Variation (mSec)         : 0.000 mSec 
Frames Above Delay Threshold           : 1431 
Frames Above Delay Variation Threshold : 1 
 
Elapsed Time (sec)                     : 1469 
 
Loss and Delay Measurements Messages  
--------------------------------------------------------------- 
11. Monitoring and Diagnostics 
                                                         : Transmitted 
LMMs                                                     : 1435 
DMMs                                                     : 1435 
                                                         : Received 
LMRs                                                     : 1435 
DMRs                                                     : 1435 
 To clear the statistics for an Ethernet port: 
• 
At the corresponding prompt (Destination NE or Service)#, enter clear-statistics. 
config>oam>cfm>md(1)>ma(1)>mep(100)>service(1)>dest-ne(1)# clear-statistics 
The statistics for the specified level are cleared. 
Performing OAM Loopback 
This diagnostic utility verifies OAM connectivity on Ethernet connections. You can execute the loopback 
according to the destination MAC address or the remote MEP number.  
Note 
The option for remote MEP ID is available only if Megaplex-4 can resolve at 
least one remote MEP MAC address.  
 To run an OAM loopback: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, enter all necessary 
commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying remote MEP by 
MAC address  
lbm address <mac-address> [repeat 
<repeat-num>] [data-tlv-length 
<length-val>] 
• MAC address is in the 
format 
<xx-xx-xx-xx-xx-xx> 
• Allowed range of 
repeat-num is 1–500 
• Allowed range of 
data-tlv-length is 0–1900 
 
Specifying remote MEP by 
MEP ID 
lbm remote-mep <mep-id> [repeat 
<repeat-num>] [data-tlv-length 
<length-val>] 
Sending LBM messages to 
default multicast MAC 
address 
lbm multicast [repeat <repeat-num>] 
 
Checking OAM loopback 
results 
show lbm-results 
 
11. Monitoring and Diagnostics 
For example: 
config>oam>cfm>md(1)>ma(1)>mep(100)# show lbm-results 
Remote MEP ID             : 1 
Destination Address       : 00-20-D2-50-0F-D9 
Messages Sent             : 1 
Replies In Order          : 1 
Replies Out Of Order      : 0 
Messages Lost/Timed Out   : 0 
Messages Lost/Timed Out % : 0 
Performing OAM Link Trace 
This diagnostic utility traces the OAM route to the destination, specified either by the MAC address or 
the maintenance end point (MEP).  
Note 
The option to specify the destination MEP ID is available only if Megaplex-4 
can resolve at least one remote MEP MAC address.  
 To run an OAM link trace: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, enter all necessary 
commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying remote MEP by 
MAC address 
linktrace address <mac-address> 
[ttl <1–64>] 
• MAC address is in the 
format 
<xx-xx-xx-xx-xx-xx> 
• Allowed range for 
ttl-value is 1–64. This 
parameter specifies 
number of hops. Each 
unit in the link trace 
decrements the TTL until 
it reaches 0, which 
terminates the link trace. 
Specifying remote MEP by ID 
linktrace remote-mep <mep-id> 
[ttl <1–64>] 
Checking the OAM link trace 
results 
show linktrace-results 
 

## 11.5 Ethernet OAM (EFM)  *(p.880)*

11. Monitoring and Diagnostics 
For example: 
config>oam>cfm>md(1)>ma(1)>mep(100)# show linktrace-results 
 
Ingress 
--------------------------------------------------------------- 
 
Hop           : 1           MAC Address     : 00-20-D2-50-0F-D9 
Relay Action  : Hit         Ingress Action  : Ingress OK 
Port Sub Type : Interface Alias 
 
Port ID : ETH 1 
 
 
Egress 
-------------------------------------------------------------- 
11.5 Ethernet OAM (EFM)  
This section covers the monitoring of the Ethernet links using OAM EFM (OAM Ethernet at the First 
Mile). 
Megaplex-4 can act as the active or passive side in an IEEE 802.3-2005 application.  
When link OAM (EFM) is enabled for a port, you can view its status by displaying the port status (show 
status). You can also display the OAM (EFM) parameters and OAM (EFM) statistics. You can configure 
OAM EFM for the GbE ports of CL.2 and M-ETH modules. 
Standards 
IEEE 802.3-2005 
Benefits 
Ethernet OAM (EFM) provides remote management and fault indication for the Ethernet links. Remote 
link failure can be detected via OAM (EFM). 
11. Monitoring and Diagnostics 
Functional Description 
The OAM (EFM) discovery process allows a local data terminating entity (DTE) to detect Ethernet OAM 
capabilities on a remote DTE. Once Ethernet OAM support is detected, both ends of the link exchange 
state and configuration information, such as mode, PDU size, loopback support, etc. If both DTEs are 
satisfied with the settings, OAM is enabled on the link. However, the loss of a link or a failure to receive 
OAMPDUs for five seconds may cause the discovery process to restart.  
DTEs may either be in active or passive mode. DTEs in active mode initiate the ETH-OAM (EFM) 
communications and can issue queries and commands to a remote device. DTEs in passive mode 
generally wait for the peer device to initiate OAM communications and respond to commands and 
queries, but do not initiate them. 
A flag in the OAMPDU allows an OAM entity to convey the failure condition Link Fault to its peer. Link 
Fault refers to the loss of signal detected by the receiver; A Link Fault report is sent once per second 
with the Information OAMPDU. 
Factory Defaults 
By default, OAM EFM is not enabled for Ethernet ports.  
Configuring OAM EFM 
There are two available OAM EFM descriptors. Each can be configured to indicate active or passive OAM 
EFM.   
 To configure OAM EFM descriptor: 
1. Navigate to configure oam efm. 
The config>oam>efm# prompt is displayed. 
2. Enter: 
 descriptor <number> {active | passive} 
 To configure link OAM (EFM) for Ethernet port: 
1. Navigate to configure port ethernet <slot>/<port>. 
The prompt config>port>eth(<port-num>)# is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Enabling link OAM 
(EFM)  
efm descriptor <1–
2> 
The EFM descriptor must exist before you can assign it to 
a port 
In order for link OAM (EFM) to function properly, the 
relevant Ethernet port must be associated with an L2CP 
profile that specifies peer action for MAC 01-80-C2-00-
00-02.  
Disabling link OAM 
(EFM) 
no efm 
 
Displaying link 
OAM (EFM) 
parameters 
show oam-efm 
Relevant only if link OAM (EFM) is enabled. 
Displaying link 
OAM (EFM) 
statistics 
show 
oam-efm-statistics 
Relevant only if link OAM (EFM) is enabled. 
Commands in level efm  
Enabling loopback  
loopback 
Type no loopback to disable loopback 
Example 
 To enable active link OAM (EFM) for Ethernet port CL-A/1: 
 
#************** Configure L2CP profile for OAM EFM 
configure port l2cp-profile mac2peer 
mac  01-80-C2-00-00-02 peer 
commit  
 
#************** Configure OAM EFM descriptor 
exit all 
configure oam  efm-descriptor 1 active 
exit 
efm-descriptor 2 passive 
commit 
 
 
#************** Configure Ethernet port CL-A/1: 
#************** Associate L2CP profile and OAM EFM descriptor 
configure port ethernet cl-a/1 
11. Monitoring and Diagnostics 
l2cp profile mac2peer 
efm descriptor 1 
exit 
no shutdown 
commit 
 
 
#************** Configure Ethernet port CL-A/1: 
#************** Associate L2CP profile and OAM EFM descriptor 
configure port ethernet cl-a/1 
l2cp profile mac2peer 
efm descriptor 1 
no shutdown 
exit all 
 
#************** Activate an EFM loopback 
config>port>eth(cl-a/1)>efm#  
loopback 
 
 
#****To display the link OAM (EFM) status for Eth port CL-A/1: 
       
configure port ethernet cl-a/1 
      show oam-efm 
 
config>port>eth(cl-a/1)# show oam-efm 
Administrative Status : Enabled 
Operational Status    : Operational 
Loopback Status       : Remote 
 
OAM EFM Information 
-------------------------------------------------------------- 
                 Local                     Remote 
MAC Address    : 00-20-D2-50-30-2D         00-20-D2-F6-8E-A3 
Mode           : Active                    Passive 
Unidirectional : Supported                 Not Supported 
Vars Retrieval : Supported                 Supported 
Link Events    : Supported                 Supported 
Loopback       : Not Supported             Supported 
PDU Size       : 1518                      1518 
Vendor OUI     : 0x0020D2                  0x0020D2 
 

## 11.6 In-Service Ping  *(p.884)*

11. Monitoring and Diagnostics
11.6 In-Service Ping 
Benefits 
In-service ping provides a simple connectivity test across L2 service paths. 
Functional Description 
In-Service Ping enables a single CLI command to perform a simple connectivity check across L2 service 
paths without the need for complicated configuration such as required in other tools. 
In addition, In-Service Ping includes a mechanism to enable a connectivity test across the flow inside the 
device, by configuring the entry point of ICMP packets to the flow.  
L2 (VPLS)
Network
Megaplex-4
Megaplex-4
IP/MPLS
Network
IP Interface
Over the EVC
IP Interface
Over the EVC
Ping
In-Service Ping is supported for the following topologies: 
•
Point-to-point E-line service
•
Multipoint-to-multipoint E-LAN (Bridge) services.
In-Service ping is supported for IPv4 IP interfaces only (for both point-to-point and multipoint-to-
multipoint). One In-Service Ping instance is supported. In-Service Ping runs independently of working 
routers and occupies a dedicated virtual router interface. 
Megaplex-4 can initiate the connectivity test, as well as respond to In-Service Ping requests sent over L2 
services to a configured IP address. 
You can invoke two types of command: 
•
In-service ping request –run this command at the device generating the ping test
•
In-service ping response –run this command at the device that responds to the ping-request
packets with ping-response packets. This command configures the IP stack to listen to ping-
requests being sent over a particular flow, targeted to a provisioned IP address.
11. Monitoring and Diagnostics 
Note 
In-service Ping is not supported over Multicast IP.  
In-service ping is available from the ‘flow’ level of the CLI. 
Factory Defaults  
Command 
Default  
vlan 
-1 (untagged) 
inner-vlan 
-1 (untagged) 
p-bit 
0 
inner-p-bit 
0 
number-of-packets  
5 
payload-size  
32 bytes 
Performing the Ping 
 To initiate an in-service ping request: 
1. Navigate to configure>flows. 
2. Enter all necessary commands according to the tasks listed below. 
Note 
The probe-scope parameter appearing in the CLI is not supported in the 
current version.  
 
 
11. Monitoring and Diagnostics 
In-service Ping Request/Response Command Parameters 
Task 
Command 
Comments 
Perform standard in-
service ping for 
egress ports 
 
 
 
service-ping local-ip <src-ip-
address/mask> dst-ip <dst-ip-
address> next-hop <next-hop-ip-
address> { egress-
port {ethernet <[slot/]port> | lag 
<number> | logical-mac 
<[slot/]port> }} [vlan <vlan-id 
0..4095> ] [inner-vlan <inner-
vlan-id 0..4095> ] [ p-bit <p-bit-id 
0..7> ] [inner-p-bit <inner-p-bit-id 
0..7>]  [number-of-
packets <1..10000>] [payload-
size <32.. 1450 bytes>]  
 
 
 
 
 
 
local-ip – The temporary IP address 
provisioned on the sender/responder for 
the duration of the test, combined with 
subnet-mask. 
dst-ip – The IP address to which in-service 
ping request packets are destined.  
next-hop – Next hop to use when 
destination IP is out of the source subnet.  
egress-port  – This is either physical or 
logical interface to which the ping request 
is sent . The supported egress ports are: 
ethernet, lag or logical-mac. 
vlan (optional) – the VLAN ID defining the 
flow the service runs in  
inner-vlan (optional) –inner VLAN ID 
defining the flow the service runs in  
p-bit –The service VLAN priority bit used 
when encapsulating the ping packet 
inner-p-bit –The inner-VLAN priority bit 
used when encapsulating the ping packet  
The vlan-related parameters are possible 
only in the following combinations:  
• You cannot configure p-bit without 
vlan. 
• You cannot configure inner-p-bit 
without inner-vlan. 
• You cannot configure inner-vlan 
without vlan. 
number-of-packets – Number of in-
service ping request packets for the test 
<1-10000> (default=5) 
payload-size – Payload size of the in-
service ping request packets <32-1450> 
(default=32) 
The dst-ip IP address must be the same as 
the IP address in local-ip in the service-
ping-response command configured on 
the opposite device. 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Perform standard in-
service ping for 
bridge ports 
 
 
service-ping local-ip <src-ip-
address/mask> dst-ip <dst-ip-
address> next-hop <next-hop-ip-
address> bridge <number>  
vlan <vlan-id 0..4095> [inner-
vlan <inner-vlan-id 
0..4095> ]  [number-of-packets 
<1..10000>]  payload-size <32.. 
1450 bytes>]  
 
 
 
 
 
 
local-ip – The temporary IP address 
provisioned on the sender/responder for 
the duration of the test, combined with 
subnet-mask. 
dst-ip – The IP address to which in-service 
ping request packets are destined.  
next-hop – Next hop to use when 
destination IP is out of the source subnet.  
bridge – Number of the bridge to which 
the ping request is sent.  
vlan (mandatory) – the VLAN ID defining 
the flow the service runs in  
inner-vlan (optional) –inner VLAN ID 
defining the flow the service runs in  
number-of-packets – Number of in-
service ping request packets for the test  
payload-size – Payload size of the in-
service ping request packets  
The dst-ip IP address must be the same as 
the IP address in local-ip in the service-
ping-response command configured on 
the opposite device. 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Initiate an in-service 
ping response for 
egress ports 
 
service-ping-response local-
ip <src-ip-address/mask>  next-
hop <next-hop-ip-address> { 
egress-
port {ethernet <[slot/]port> | lag 
<number> | logical-mac 
<[slot/]port> }} [vlan <vlan-id 
0..4095> ] [inner-vlan <inner-
vlan-id 0..4095> ] [ p-bit <p-bit-id 
0..7> ] [inner-p-bit <inner-p-bit-id 
0..7>]   
local-ip – The temporary IP address 
provisioned on the sender/responder for 
the duration of the test, combined with 
subnet-mask. 
next-hop – Next hop to use when 
destination IP is out of the source subnet.  
egress-port  – This is either physical or 
logical interface from which the ping 
response is received. The supported 
egress ports are: ethernet, lag or logical-
mac. 
vlan (optional) – the VLAN ID defining the 
flow the service runs in  
inner-vlan (optional) –inner VLAN ID 
defining the flow the service runs in 
p-bit –The service VLAN priority bit used 
when encapsulating the ping packet  
inner-p-bit –The inner-VLAN priority bit 
used when encapsulating the ping packet  
The vlan-related parameters are possible 
only in the following combinations:  
• You cannot configure p-bit without 
vlan. 
• You cannot configure inner-p-bit 
without inner-vlan. 
• You cannot configure inner-vlan 
without vlan. 
The IP address in local-ip  command must 
be the same as the dst-ip IP address in the 
service-ping command configured on the 
opposite device 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Initiate an in-service 
ping response for 
bridge ports 
 
service-ping-response local-
ip <src-ip-address/mask>  next-
hop <next-hop-ip-
address> bridge <number> 
vlan <vlan-id 0..4095> [inner-
vlan <inner-vlan-id 0..4095> ]   
 
 
 
 
 
local-ip – The temporary IP address 
provisioned on the sender/responder for 
the duration of the test, combined with 
subnet-mask 
next-hop – Next hop to use when 
destination IP is out of the source subnet  
bridge –Number of the bridge from which 
the ping request is received  
vlan (mandatory) – the VLAN ID defining 
the flow the service runs in  
inner-vlan (optional) –inner VLAN ID 
defining the flow the service runs in  
The IP address in local-ip  command must 
be the same as the dst-ip IP address in the 
service-ping command configured on the 
opposite device 
Examples  
Pinging 10.10.10.28 with 32 bytes of data (default payload size): 
config>flows# service-ping local-ip 10.10.10.20/24 dst-ip 10.10.10.28 next-hop 
10.10.10.1 egress-port ethernet 1/1 vlan 100 
 
 
Pinging 10.10.10.28 with 32 bytes of data: 
 
 
Reply from 10.10.10.28 bytes=32 time=0ms seq=1 
Reply from 10.10.10.28 bytes=32 time=0ms seq=2 
Reply from 10.10.10.28 bytes=32 time=0ms seq=3 
Reply from 10.10.10.28 bytes=32 time=0ms seq=4 
Reply from 10.10.10.28 bytes=32 time=0ms seq=5 
 
 
--- Ping Statistics --- 
Packets: Sent = 5, Received = 5, Lost = 0 (0% loss) 
Responding to ping sent to the owner of the IP address 10.10.10.28:  

## 11.7 LEDs  *(p.890)*

11. Monitoring and Diagnostics 
service-ping-response local-ip 10.10.10.28/24 next-hop 10.10.10.1 egress-port 
ethernet 1/1 vlan 100 
Terminating the Ping  
You can terminate the in-service ping test before the indicated number of packets (in the example 
below – 10) has been transmitted by pressing Ctrl-C. 
config>flows# 
config>flows# service-ping local-ip 10.10.10.20/24 dst-ip 10.10.10.28 next-hop 
10.10.10.1 egress-port ethernet 1/1 vlan 100 number-of-packets 10 
 
Pinging 10.10.10.28 with 32 bytes of data: 
 
Reply from 10.10.10.28 bytes=32 time=0ms seq=1 
Reply from 10.10.10.28 bytes=32 time=0ms seq=2 
Reply from 10.10.10.28 bytes=32 time=0ms seq=3 
Control-C 
 
--- Ping Statistics --- 
Packets: Sent = 3, Received = 3, Lost = 0 (0% loss) 
You can also block responses from the target and ping requests from the source, using the following 
commands: 
no service-ping 
The device stops sending requests. A termination message and test 
summary are displayed. Note: To perform this command, open 
another session in Telnet. 
config>flows# no service-ping-response 
current in-service test is interrupted 
no service-ping-
response 
The device stops listening to in-ping-requests and clears any 
generated command context (the local IP address and routing 
entry).  
11.7 LEDs 
Megaplex-4 modules and the Megaplex-4 chassis itself have various status indicators that can be used to 
identify problems. 

## 11.8 Performance Management  *(p.891)*

11. Monitoring and Diagnostics 
Refer to Chapter 2 of this manual for details regarding the functions and indications of each system 
indicator and to Chapter 3 of this manual for normal indications after power-up. Also refer to Megaplex-
4 I/O Modules Installation and Operation Manual for details regarding the functions and indications of 
each module indicator. 
11.8 Performance Management  
Megaplex-4 maintains performance management (PM) statistics for selected entities in the device. The 
PM statistics are collected into a file periodically, for retrieval by RADview, for display in the RADview 
PM portal (refer to the RADview System User’s Manual for further details on the PM portal). The PM 
collection process can be globally enabled or disabled for the entire device. In addition, the statistics 
collection can be enabled for all entities of a specific type, or for specific entities. 
Standards  
ITU-T G.826. 
Benefits 
The PM data is useful for analyzing Megaplex-4 service quality. The flexible statistics collection allows 
only the necessary data to be collected.  
Functional Description 
PM statistics collection is configured for the device, entity type, and specific entities. PM statistics are 
collected for the following types of entities: 
• 
Ethernet ports 
• 
Flows 
• 
OAM CFM services 
• 
E1 Ports (external and internal) 
• 
T1 Ports (external and internal) 
• 
SDH/SONET Ports 
11. Monitoring and Diagnostics 
• 
SDH/SONET Path Level 
• 
SDH/SONET VC/VT Level. 
Note 
• 
PM statistics collection is performed only if it is enabled for the entire 
device, regardless of whether it is enabled for any entity 
• 
PM statistics are not collected for entities that are administratively 
disabled.  
If PM statistics collection is disabled for a particular entity type, then no PM statistics collection is done 
for any entity of that type, except those for which PM statistics collection is enabled. 
When PM statistics collection is enabled for all entities of the same type, then when a new entity of that 
type is added the device automatically starts collecting PM statistics for it. 
Note 
If you are using the RADview PM Portal, it is recommended to enable PM 
statistics collection for all relevant entities. See Error! Reference source not 
found. for a script that you can use for this purpose.  
PM statistics collection is performed at user-configurable intervals of one second to 15 minutes. A 
different interval can be configured for each entity type, and for specific entities. 
If different intervals are scheduled for collection at the same time, Megaplex-4 collects the PM statistics 
starting with the interval that has the highest frequency, and ending with the interval that has the 
lowest frequency. If Megaplex-4 has not finished collecting the statistics for an interval when the 
scheduled time for another interval arrives, the following action is taken according to whether the new 
interval is the next interval, or an interval with higher frequency: 
• 
If it is the next interval, then the next interval is canceled, and a PM record indicating the 
cancellation is inserted in the PM data 
• 
If it is an interval with higher frequency, then Megaplex-4 collects the higher frequency interval 
statistics and then resumes collecting the lower frequency interval statistics. The PM data is 
retrieved from Megaplex-4 by RADview via TFTP or SFTP. After PM data is retrieved, Megaplex-4 
deletes the file and opens a new one for further data. 
Factory Defaults 
PM statistics collection in the device (pm command) is globally enabled by default. PM statistics 
collection for each separate entity (such as pm-collection eth, pm-collection flow etc) is disabled. 
11. Monitoring and Diagnostics 
Configuring Performance Management 
PM statistics collection is configured for the entire device via the pm command, and for entity types via 
the pm-collection command, in the reporting level. For specific entities, PM statistics collection is 
configured via pm-collection, in the specific entity level.  
The interval parameter for the pm-collection command can range from 1 sec to 900 seconds 
(15 minutes). The recommended interval is 1 min. Different intervals can be specified for an entity type 
and for specific entities of that type. For example, if the PM statistics collection interval for all flows is 
configured to 15 minutes, and the PM statistics collection interval for flow-1 is configured to 1 minute, 
the data displayed in the RADview PM portal shows flow data for every 15 minutes, and flow-1 data for 
every minute. 
The following shows the PM statistics collection configuration tasks, and their corresponding commands, 
as well as the level of each command. 
Task 
Level under config 
Command 
Comments 
Globally enabling PM 
statistics collection for 
device 
reporting 
pm 
Type no pm to disable all PM 
statistics collection in 
Megaplex-4 
Enabling PM statistics 
collection for Ethernet 
ports  
reporting  
pm-collection eth 
interval <seconds> 
{ethernet | e1 | t1 | 
e1-i | t1-i | sdh-sonet } 
Type no pm-collection 
followed by the port type to 
disable PM statistics 
collection for this type of 
port 
Enabling PM statistics 
collection for flows  
reporting 
pm-collection flow 
interval <seconds> 
Type no pm-collection flow 
to disable PM statistics 
collection for flows 
Enabling PM statistics 
collection for OAM CFM 
services 
reporting 
pm-collection 
oam-cfm-service 
interval <seconds> 
Type no pm-collection 
oam-cfm-service to disable 
PM statistics collection for 
OAM CFM services 
Enabling PM statistics 
collection for a specific 
port  
port {ethernet | e1 | t1 | 
e1-i | t1-i | sdh-sonet} 
(<slot>/<port>) 
pm-collection interval 
<seconds> 
Type no pm-collection to 
disable PM statistics 
collection for the port 
Enabling PM statistics 
collection for a specific 
flow and defining 
interval 
flows > flow 
(<flow-name>) 
pm-collection interval 
<seconds> 
Type no pm-collection to 
disable PM statistics 
collection for the flow 
11. Monitoring and Diagnostics 
Task 
Level under config 
Command 
Comments 
Enabling PM statistics 
collection for a specific 
OAM CFM service and 
defining interval 
oam > cfm > md(<mdid>) 
> ma(<maid>) > 
mep(<mepid>) > 
service(<serviceid>) 
pm-collection interval 
<seconds> 
Type no pm-collection to 
disable PM statistics 
collection for the service 
Enabling PM statistics 
collection for a 
VC-4/STS-1 and 
defining interval 
port >  sdh-sonet 
(<slot>/<port>) continued 
by:  
SDH: 
aug (<aug number 1..4>) 
tug3 (<tug3 number 
1..3>)#  
 
SONET: 
oc3 <oc3 number 1..4>)  
sts1 <sts1 number 1..3>) # 
pm-collection interval 
<seconds> 
 
Type no pm-collection to 
disable PM statistics 
collection for the service 
Enabling PM statistics 
collection for a 
VC-12/VT1.5 and 
defining interval 
port >  sdh-sonet 
(<slot>/<port>) continued 
by:  
SDH: 
aug (<aug number 1..4>) 
tug3 (<tug3 number 1..3>) 
vc12 (<tug2 number 
1..7>)/<tributary number 
1..3>)#  
 
SONET: 
oc3 <oc3 number 1..4>)  
sts1 <sts1 number 1..3>)  
vt1-5 <tug2 number 
1..7>)/ <tributary number 
1..4>)# 
pm-collection interval 
<seconds> 
 
Type no pm-collection to 
disable PM statistics 
collection for the service 
 
Note 
PM statistics are collected for entities for which PM statistics collection is 
specifically enabled in the entity level via pm-collection, even if PM statistics 
collection for the entity type is disabled.  
11. Monitoring and Diagnostics 
Viewing Performance Management Configuration 
You can use the info detail command to view the performance management configuration. 
 To view the performance management configuration for the device and for entity types: 
1. Navigate to configure reporting. 
2. Enter info detail | include pm to view PM-related commands in the configuration. 
 To view the performance management configuration for specific entities: 
1. Navigate to the specific entity level. 
2. Enter info detail | include pm to view PM-related commands in the configuration. 
Examples 
 To enable PM for all relevant entities in Megaplex-4: 
• 
PM statistics collection enabled for device 
• 
PM statistics collection enabled for all relevant entities, every five minutes. 
exit all 
configure reporting 
#**** Enable PM in device 
pm 
#**** Enable PM for Eth ports, collection interval=5 min 
  pm-collection eth interval 300 
#**** Enable PM for flows, collection interval=5 min 
  pm-collection flow interval 300 
#**** Enable PM for OAM CFM services, collection interval=5 min 
  pm-collection oam-cfm-service interval 300 
exit all 
save 
 To configure the following PM: 
• 
PM statistics collection enabled for device 
• 
PM statistics collection enabled for Ethernet ports, every two minutes 
• 
PM statistics collection enabled for flows, every five minutes 
• 
PM statistics collection for Ethernet port cl-a/1 configured to every minute  

## 11.9 Ping Test  *(p.896)*

11. Monitoring and Diagnostics 
• 
PM statistics collection enabled for OAM CFM services, every 15 minutes 
exit all 
configure reporting 
#**** Enable PM in device 
pm 
#**** Enable PM for Eth ports, collection interval=2 min 
  pm-collection eth interval 120 
#**** Enable PM for flows, collection interval=5 min 
  pm-collection flow interval 300 
#**** Enable PM for OAM CFM services, collection interval=15 min 
  pm-collection oam-cfm-service interval 900 
exit all 
 
#**** Configure PM statistics collection interval for Eth port cl-a/1, to 1 min 
configure port ethernet cl-a/1 
  pm-collection interval 60 
exit all 
save 
 To display PM configuration from above example: 
mp4100# configure reporting 
mp4100>config>reporting# info detail | include pm 
    pm 
    pm-collection eth interval 120 
    pm-collection flow interval 300 
    pm-collection oam-cfm-service interval 900 
    mp4100>config>reporting# exit all 
 
mp4100# configure port ethernet cl-a/1 
mp4100>config>port>eth(cl-a/1)# info detail | include pm 
    pm-collection interval 60 
11.9 Ping Test  
You can perform a ping test to check the Megaplex-4 IP connectivity.  
 To perform a ping test: 
1. At any level, start pinging the desired host specifying its IP address and, optionally, the number 
of packets to be sent, and payload size: 
11. Monitoring and Diagnostics 
ping <1.1.1.1–255.255.255.255> [number-of-packets <1–10000>] [payload-size <32–1450 
bytes>] 
2. To stop the ping test, enter Ctrl-C. 
3. Example: 
mp4100# ping 172.17.170.81 number-of-packets 2 payload-size 64 
 
Pinging 172.17.170.81 with 64 bytes of data: 
 
Reply from 172.17.170.81 bytes=64 ttl=64 time=10ms seq=1 
Reply from 172.17.170.81 bytes=64 ttl=64 time=0ms seq=2 
mp4100# 
 
--- Ping Statistics --- 
Packets: Sent = 2, Received = 2, Lost = 0 (0% loss) 
When checking the hosts connected to Megaplex-4 via PW connectivity, this command must be 
performed via PW router (2). 
Example:  
mp4100>config>router(2)# ping 2.2.2.2 number-of-packets 10 payload-size 60 
 
Pinging 2.2.2.2 with 60 bytes of data: 
 
Reply from 2.2.2.2 bytes=60 time=0ms seq=1 
Reply from 2.2.2.2 bytes=60 time=0ms seq=2 
Reply from 2.2.2.2 bytes=60 time=0ms seq=3 
Reply from 2.2.2.2 bytes=60 time=0ms seq=4 
Reply from 2.2.2.2 bytes=60 time=0ms seq=5 
Reply from 2.2.2.2 bytes=60 time=0ms seq=6 
Reply from 2.2.2.2 bytes=60 time=10ms seq=7 
Reply from 2.2.2.2 bytes=60 time=10ms seq=8 

## 11.10 Statistic Counters  *(p.898)*

11. Monitoring and Diagnostics 
Reply from 2.2.2.2 bytes=60 time=0ms seq=9 
Reply from 2.2.2.2 bytes=60 time=10ms seq=10 
 
--- Ping Statistics --- 
Packets: Sent = 10, Received = 10, Lost = 0 (0% loss) 
11.10 Statistic Counters 
Megaplex-4 collects statistics per physical and logical ports (see the list below) for 15-minute intervals. 
This enables the network operator to monitor the transmission performance, and thus the quality of 
service provided to users, as well as identify transmission problems. Performance parameters for all the 
active entities are continuously collected during equipment operation.  
Statistics for the last 24 hours are stored in the device and can be retrieved at the network management 
station.  
Statistic counters provide information on possible abnormal behavior and failures. You can display 
statistics of the following: 
• 
RADIUS server  
• 
Ethernet, SDH/SONET, E1/T1, VCG, GFP, HDLC and PW ports 
• 
Flows  
The statistic counters are activated by “show statistics” command from the corresponding level and 
cleared by clear-statistics command. In addition, you can also activate the clear-statistics command from 
the root level. It clears all the Ethernet ports statistics and the flows statistics. This command is used 
when the user wants to clear all the Ethernet and flow statistics by one command instead of moving 
from one entity to the other. 
For further information, refer to the relevant sections in Chapters 5, 6 and 8 and the relevant sections in 
the troubleshooting chart. 

## 11.11 Syslog  *(p.899)*

11. Monitoring and Diagnostics 
11.11 Syslog  
Megaplex-4 uses the Syslog protocol to generate and transport event notification messages over IP 
networks to Syslog servers.  
Standards and MIBs 
RFC 3164, RFC 5674. 
Benefits 
The Syslog protocol collects heterogeneous data into a single data repository. It provides system 
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
Product operation management. 
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
11. Monitoring and Diagnostics 
Functional Description 
The Syslog protocol provides an instrument for generating and transporting event notification messages 
from Megaplex-4 to the server across IP networks. 
PSN
Syslog 
Server
Messages
Messages
Megaplex-4100
Megaplex-4100
 
Elements 
A typical Syslog topology includes message senders (devices) and message receivers (servers). 
Megaplex-4 supports up to 5 Syslog servers. The receiver displays, stores or forwards logged 
information. The standard designates two types of receivers: 
• 
Relay, which forwards messages 
• 
Collector which displays and stores messages. 
Transport Protocol 
Syslog uses User Datagram Protocol (UDP) for its transport. The UDP port that has been assigned to 
Syslog is 514, but devices and servers can agree to use any port for communication. 
Message Format 
The length of a Syslog message is 1024 bytes or less. It contains the following information: 
• 
Facility and severity (see below) 
• 
Host name or IP address of the device 
• 
Timestamp 
• 
Message content. 
A typical Syslog message looks like this: <145>Jan 15 13:24:07 172.17.160.69 Eth 1: Loss of signal (LOS) 
11. Monitoring and Diagnostics 
Facilities and Severities 
Facility designates a device or application that sends a message. The standard includes some pre-
defined facilities in the 0–15 range. Megaplex-4 uses facilities local1–7 for originator identification. 
Severity is assigned to a message to specify its importance. Megaplex-4 uses the following severity 
designations: 
Code 
Syslog Type 
Description 
0 
Emergency 
Emergency message, not in use 
1 
Alert 
Critical alarm 
2 
Critical 
Major alarm 
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
Syslog Configuration 
When configuring Syslog parameters, it is necessary to define Syslog device and servers. 
 To configure a Syslog device: 
Navigate to the syslog device context (config>system>syslog device). 
The config>system>syslog(device)# prompt is displayed. 
1. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining a facility from which 
Syslog messages are sent 
facility {local1 | local2 | local3 
| local4 | local5 | local6 | 
local7} 
 
Defining Syslog device UDP port 
for communication 
port <udp-port-number> 
Range 1–65535 
Port configuration is allowed 
only if a Syslog device is 
administratively disabled 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining severity level 
severity-level { emergency | 
alert | critical | error | warning 
| notice | informational | 
debug} 
The log messages that contain 
severity level above or equal the 
specified level are transmitted 
Administratively enabling Syslog 
device 
no shutdown 
shutdown administratively 
disables Syslog device 
Displaying statistics 
show statistics 
 
Clearing statistics 
clear-statistics 
 
      
An example below illustrates procedure for defining a Syslog device. 
• 
Facility: local2 
• 
UDP port: 155 
• 
Severity level: major. 
mp-4100# configure system syslog device 
mp-4100>config>system>syslog(device)# 
mp-4100>config>system>syslog(device)# facility local2 
mp-4100>config>system>syslog(device)# port 155 
mp-4100>config>system>syslog(device)# severity-level critical 
mp-4100>config>system>syslog(device)# no shutdown 
 To display Syslog statistics: 
Navigate to the syslog device context (config>system>syslog device). 
The config>system>syslog(device)# prompt is displayed. 
1. At the config>system>syslog(device)# prompt, enter show statistics. 
mp-4100>config>system>syslog(device)# show statistics 
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
11. Monitoring and Diagnostics 
 To clear Syslog statistics: 
1. Navigate to the syslog device context (config>system>syslog device). 
The config>system>syslog(device)# prompt is displayed. 
2. At the config>system>syslog(device)# prompt, enter clear-statistics. 
The Syslog statistic counters are set to 0. 
 To define a Syslog server: 
1. Navigate to system context (config>system). 
The config>system# prompt is displayed. 
2. At the config>system# prompt, enter server <server-ID> to specify server to receive Syslog 
messages, from 1 to 5. 
The config>system>syslog(server/1–5)# prompt is displayed. 
3. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining Syslog server IP 
address  
<0.0.0.0–255.255.255.255> 
 
Defining Syslog server UDP 
port for communication 
port <udp-port-number> 
Range 1–65535 
Port configuration is allowed only if a 
Syslog server is administratively disabled 
Administratively enabling 
Syslog server 
no shutdown 
shutdown administratively disables 
Syslog server 
For example: 
• 
Server IP address: 178.16.173.152 
• 
UDP port: 155 
mp-4100# configure system syslog server 1 
mp-4100>config>system>syslog(server/1)# 
mp-4100>config>system>syslog(server/1)# address 178.16.173.152 
mp-4100>config>system>syslog(server/1)# port 155 
mp-4100>config>system>syslog(server/1)# no shutdown 

## 11.12 Troubleshooting  *(p.904)*

11. Monitoring and Diagnostics 
11.12 Troubleshooting 
Preliminary Checks 
If a problem occurs, perform the following preliminary checks: 
• 
If the problem is detected when Megaplex-4 is put into operation (for the first time), perform 
the following checks: 
 
Check for proper chassis and module installation, and correct cable connections, in 
accordance with the system installation plan. 
 
Check that system and module configuration parameters are in accordance with the specific 
application requirements, as provided by the system administrator. 
 
If the Megaplex-4 nodal clock is to be locked to the clock recovered from one of the ports of 
a module installed in the chassis, make sure a suitable additional clock source is configured 
and provides a good clock signal. 
• 
When two CL modules are installed, check the ON LINE indicators: the ON LINE indicator of the 
active module must light steadily, and that of the standby must flash. If not, check the 
configuration. 
• 
Check the displayed alarm messages and refer to Error! Reference source not found. section for 
their meaning and corrective actions.  
Troubleshooting Procedure  
If the problem cannot be corrected by performing the actions listed above, refer to the table below. 
Identify the best-fitting trouble symptoms and perform the actions listed under “Corrective Measures” 
in the order given, until the problem is corrected. 
No. 
Trouble 
Symptoms 
Probable Cause 
Corrective Measures 
1 
Megaplex-4 
does not turn on 
1. No power 
Check that power is available at the power outlets or power 
distribution panel serving the Megaplex-4.  
Check that both ends of all the Megaplex-4 power cables are 
properly connected. 
2. Defective PS 
module  
Replace the suspected PS module  
11. Monitoring and Diagnostics 
No. 
Trouble 
Symptoms 
Probable Cause 
Corrective Measures 
3. Defective 
Megaplex-4 
Replace Megaplex-4 
2 
The local 
Megaplex-4 
cannot be 
configured 
through its 
CONTROL DCE 
port 
1. Connection made 
to the inactive CL 
module  
Check that the connection is made to the CONTROL DCE 
connector of the CL module whose ON LINE indicator lights 
steadily 
2. Configuration 
problem 
Restore the default parameters as explained in Chapter 10 
and then perform the preliminary supervision terminal 
configuration instructions in accordance with chapter 4  
3. External problem 
Check the equipment serving as a supervision terminal, and 
the connecting cable.  
If the supervision terminal is connected through a data link to 
the Megaplex-4, check the equipment providing the data link 
for proper operation  
4. Software not yet 
loaded into CL 
module, or 
corrupted  
Download the appropriate Megaplex-4 software to the CL 
modules in accordance with Chapter 12  
5. Defective CL 
module  
Replace the corresponding CL module  
3 
The local 
Megaplex-4 
cannot be 
managed 
through its 
CONTROL ETH 
port 
1.Configuration 
problems 
Check the CONTROL ETH port configuration. 
Check that the ON LINE indicator of the CL module lights 
steadily 
2. Problem in the 
connection between 
the CONTROL ETH 
port and the LAN 
Check that the LINK indicator of the CONTROL ETH port is lit. 
If not, check for proper connection of the cable between the 
LAN and the CONTROL ETH port. Also check that at least one 
node is active on the LAN, and that the hub or Ethernet 
switch to which the Megaplex-4 CONTROL ETH port is 
connected is powered 
3. External problem 
Check the external equipment (for example, the default 
gateway and other routers/switches) that process the traffic 
coming from the local Megaplex-4 CONTROL ETH port 
4. Defective CL 
module  
Replace the corresponding CL module  
5. Defective 
Megaplex-4 
Replace Megaplex-4  

## 11.13 Technical Support  *(p.906)*

11. Monitoring and Diagnostics 
No. 
Trouble 
Symptoms 
Probable Cause 
Corrective Measures 
4 
The LOS 
indicator of an 
SDH/SONET port 
is on  
1. Cable connection 
problems 
Check for proper connections of the cables to the SDH/SONET 
connector of each CL.2 port.  
Repeat the check at the user’s equipment connected to the 
port. 
2. External problem 
Activate the remote loopback at the local SDH/SONET module 
port.  
If the user equipment connected to the SDH/SONET 
connector does not receive its own signal, check its 
operation, and replace if necessary 
If the problem is not in the equipment connected to the 
SDH/SONET port, replace the CL.2 module  
5 
The status 
indicator of a 
local I/O module 
port lights in red 
1. Cable connection 
problems 
Check for proper connections of the cables to the module 
connector.  
Repeat the check at the user equipment connected to the 
port. 
2. External problem  
Activate the local physical loopback on the corresponding 
port. If the indicator of the corresponding local port lights in 
green while the loop is connected, the problem is external. 
Check cable connections, and the transmission equipment 
providing the link to the remote unit. 
3. Defective I/O 
module  
Replace the I/O module  
6 
The LOS 
indicator of the 
CLOCK port 
lights in red 
1. Cable connection 
problems 
Check for proper connections of the cables to the connector.  
Repeat the check at the equipment providing the station 
clock signal to the Megaplex-4. 
2. Defective CL 
module  
Replace the CL module  
11.13 Technical Support 
For technical support of registered products, contact your local authorized RAD partner or go to 
RADcare Online (if you have a valid RADcare service package).  
11. Monitoring and Diagnostics 
RAD Data Communications would like your help in improving its product documentation. Please send us 
an e-mail with your comments. 
Thank you for your assistance! 
 