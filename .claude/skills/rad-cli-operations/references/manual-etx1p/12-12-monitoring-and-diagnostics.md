# 12 Monitoring and Diagnostics

*Manual `ETX-1p_6.4_Mn_05-26_GA.pdf`, pages 679–704.*


## 12.1 Generating Log Report  *(p.679)*

12. Monitoring and Diagnostics 
12 Monitoring and Diagnostics 
12.1 Generating Log Report  
ETX-1p has a special command for collecting various diagnostics of the system for Technical support 
process.  
Functional Description 
If you have a problem with your device and cannot troubleshoot it, you can generate a file including all 
possible system and kernel log files and send it to RAD Global Services in order to get a solution. ETX-1p 
can store up to three such files inside the device. 
Configuring Log Report Generation 
The procedure consists of generating a log-report file and exporting it via copy command. 
 
 To generate a log report file: 
• 
Navigate to configure system and type generate-log-report. 
The log report file is generated in the following format: ‘log/log_20250630_081019.tar.gz’ 
(the first 8 characters show the date, the second six show the daytime). 
    To view all log report files available in the device: 
• 
At the file# prompt, enter user-file-dir. 
 To delete a log reports file: 
1. At the file# prompt, enter:  
delete <file-name> 
You are prompted to confirm the deletion. 

## 12.2 Syslog  *(p.680)*

12. Monitoring and Diagnostics 
2. Confirm the deletion. 
 To export a log report: 
• 
Use copy command, as described in Copying Files section. 
12.2 Syslog 
ETX-1p uses the Syslog protocol to generate and transport event notification messages over IP networks 
to Syslog servers.  
Syslog protocol collects heterogeneous data into a single data repository. It provides system 
administrators with a single point of management for collecting, distributing, and processing audit data. 
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
Applicability and Scaling 
This feature is applicable to all the device versions. 
Standards Compliance 
RFC 3164 - The BSD syslog Protocol 
RFC 5674 - Alarms in Syslog 
12. Monitoring and Diagnostics 
Functional Description 
The Syslog protocol provides an instrument for generating and transporting event notification messages 
from ETX-1p to servers across IP networks. 
Elements 
Typical Syslog topology includes message senders (clients) and message receivers (servers). ETX-1p 
supports Syslog client functionality. It can send messages to up to five Syslog servers. The receiver 
displays, stores, or forwards logged information.  
Transport Protocol 
Usually, Syslog uses UDP port 514 for its transport, but devices and servers can be defined to use any 
port for communication. 
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
facilities in the 0–15 range. For originator identification, ETX-1p can be configured to use facilities 
local1– local7; local1 is the default facility. 
Severity is assigned to a message to specify its importance. ETX-1p uses the following severity 
designations: 
 
12. Monitoring and Diagnostics 
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
Cleared alarm and accounting message 
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
shutdown 
shutdown 
Configuring Syslog Parameters 
When configuring Syslog parameters, it is necessary to enable Syslog device (client) and define Syslog 
servers. The remaining configuration is optional. 
 To configure Syslog device: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. Enter the necessary commands according to the tasks listed below. 
12. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining a facility from 
which Syslog messages 
are sent 
facility {local1 | local2 | local3 | 
local4 | local5 | local6 | local7} 
 
Defining Syslog device 
UDP port for 
communication 
port <udp-port-number> 
Possible values: 1–65535 
Port configuration is allowed only if 
a Syslog device is administratively 
disabled. 
Defining severity level 
severity-level { emergency | alert | 
critical | error | warning | notice | 
informational | debug} 
The log messages that contain 
severity level above or equal to the 
specified level are transmitted. 
• emergency – emergency 
messages 
• alert – critical alarms 
• critical – major alarms 
• error – minor alarms 
• warning – events 
• notice – cleared alarms, 
accounting messages 
• informational – informational 
messages; not in use 
• debug – debug messages; not in 
use 
Administratively enabling 
Syslog device 
no shutdown 
shutdown administratively disables 
the Syslog device. 
Displaying Syslog 
statistics 
show statistics 
See Viewing Syslog Statistics 
Clearing Syslog statistics 
clear-statistics 
 
 To configure a Syslog server: 
1. Navigate to configure system. 
The config>system# prompt is displayed. 
2. At the config>system# prompt, enter syslog server <server-ID> to specify the server to receive 
Syslog messages, where <server-ID> is 1 to 5. 
The config>system>syslog(server/<server-ID>)# prompt is displayed. 
3. Enter the necessary commands according to the tasks listed below. 
12. Monitoring and Diagnostics 
 
Task 
Command 
Comments 
Enabling Syslog commands 
accounting (logging of 
command entries)  
[no] accounting 
commands 
To disable command logging, enter no 
accounting  
Defining Syslog server IP 
address 
address <ip-address> 
ip-addrees – Syslog server IP address 
Possible values: 
0.0.0.0–255.255.255.255 
Defining Syslog server UDP 
port for communication 
port 
<udp-port-number> 
udp-port-number – UDP port 
Possible values: 1–65535 
Administratively enabling 
Syslog server 
no shutdown 
shutdown administratively disables Syslog 
server. 
Note: This command is available only after 
you define the Syslog server IP address. 
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
Configuration Errors 
The following table lists messages generated by ETX-1p when a configuration error is detected. 
 
Message 
Description 
Syslog Port is out of range 
Selected UDP port value is out of allowed range (1–65535). 
12. Monitoring and Diagnostics 
Message 
Description 
Port is illegal or Device Port is already 
in use 
Selected UDP port is already in use. 
Parameter cannot be changed if 
Logging Status/Server Access is 
enabled 
Device/server UDP port or server IP address cannot be changed 
while Syslog server is enabled. 
Illegal Severity 
Invalid severity value 
Illegal Facility 
Invalid facility value 
Illegal Server IP Address 
Invalid server IP address 
Viewing Syslog Statistics 
 To display Syslog statistics: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. At the config>system>syslog(device)#, enter show statistics. 
Syslog statistics appear as shown below. The counters are described in the following table. 
config>system>syslog(device)# show statistics 
Total Tx Messages 
 
 
: 356 
Non-queued Dropped Messages 
: 265 
 
Parameter 
Description 
Total Tx Messages 
The total number of Syslog messages transmitted 
Non-queued Dropped 
Messages 
The total number of Syslog messages that were dropped before being 
queued 
 To clear Syslog statistics: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. At the config>system>syslog(device)# prompt, enter clear-statistics. 
The Syslog statistic counters are set to 0. 

## 12.3 IP Monitoring  *(p.686)*

12. Monitoring and Diagnostics 
12.3 IP Monitoring  
IP Monitoring serves as a tool for the link redundancy feature in ETX-1p. For the description of link 
redundancy, see Link Redundancy in Chapter 7. 
Applicability and Scaling 
This feature is applicable to all the device versions.  
Functional Description 
IP monitoring entity is operated as a connectivity trigger for fault propagation. 
To activate IP monitoring, the following procedure is used:  
1. Create the ip-monitor entity and attach it to the device entity (router or tunnel interface), as 
described in Fault Propagation section. 
2. Under configure oam ip-monitoring, set the target IP address and other parameters. 
The IP monitoring entity is activated and start continues periodic ping transmission while IP 
monitoring entity is active. Transmit pings are sent according to the transmit interval and the 
result is declared according to icmp timeout. Fail criteria are checked over the sliding window. 
 
The IP monitoring mechanism is functioning as follows: 
• 
A ping is sent once in transmit-interval time 
• 
Ping timeout is defined with icmp-timeout parameter 
• 
During sliding window time, results of the pings included in the sliding-window are checked: 
 
𝑛𝑛𝑛𝑛𝑛𝑛𝑛𝑛𝑛𝑛𝑛𝑛 𝑜𝑜𝑜𝑜 𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝 𝑖𝑖𝑖𝑖 𝑡𝑡ℎ𝑒𝑒 𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤=
sliding-window time
transmit-interval time  
• 
The internal notifications are sent according to fail-criteria 
The diagram below illustrates the following example: 
• 
transmit-interval = 1 sec, icmp-timeout = 5 sec 
• 
window size = 5 sec 
• 
fail criteria = 60 
12. Monitoring and Diagnostics 
Note: ip-monitoring by default sends ping every 1 sec, fail criteria – 3 out of 5 ping failures  
 
 
 
 
 
 
Sliding window 
Ping timeout 
Transmit interval 
12. Monitoring and Diagnostics 
Configuring IP Monitoring  
 To define and configure an IP monitoring entity: 
1. Navigate to configure oam ip-monitoring <name>. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Configuring fail criteria 
fail-criteria <fail-thr-percents> 
<fail-thr-percents> – The threshold, in 
percents, over which a monitoring failure is 
declared  
Possible Values: 1..100 
Default: 60 
Configuring monitoring 
target IP address 
target <ip-address> 
 
<ip-address> – The IP Address of the ICMP-
echo target in IPv4 or IPv6 format 
Configuring monitoring 
transmit interval (in 
seconds) 
transmit-interval <seconds> 
<seconds> – The interval period between 
monitoring transmissions 
Possible Values: 1..30 
Default: 1 
Configuring monitoring 
icmp timeout (in seconds) 
icmp-timeout <seconds> 
<seconds> – The timeout to decide on failure 
after icmp transmission 
Possible Values: 1..30 
Default: 5 
Configure monitoring 
sliding window-size (in 
seconds) 
window-size <seconds> 
<seconds> – The size of sliding window 
Possible Values: 1..30 
Default: 5 
Displaying ip-monitoring 
entity status 
show status 
See below 
Viewing IP Monitoring Status 
You can display the current IP monitoring status. 

## 12.4 Performance Management  *(p.689)*

12. Monitoring and Diagnostics 
 To display IP monitoring status: 
• 
At the config>oam>ip-monitoring# prompt, enter: 
show status 
The IP monitoring status is displayed. 
Status Parameters 
Parameter 
Description 
Tracked interface 
The device interface tracked by IP monitoring entity 
Target IP 
Target IP address 
Status 
 
IP monitoring entity status 
Possible Values: 
Inactive  
UP  
DOWN  
Last change time 
Last change date and time  
Configuration Errors 
The following table lists the messages displayed by ETX-1p when a configuration error is detected.  
Message 
Description 
The IP monitoring entity is not in use 
 
The IP monitoring entity is not attached to any fault propagation 
rule. 
12.4 Performance Management  
ETX-1p supports collection of performance management (PM) statistics for analyzing the device’s service 
quality. The device periodically collects PM statistics into a pm-0 binary file for retrieval and analysis by 
RADview and for display in the RADview PM portal (refer to the RADview System User Manual for 
further details on the PM portal).  
12. Monitoring and Diagnostics 
The PM collection process can be globally enabled (the default) or disabled for the entire device. In 
addition, the statistics collection can be enabled for all entities of a specific type, or for specific entities, 
enabling collection of necessary data only. 
Functional Description 
PM Statistics Collection 
PM statistics collection is configured for the device, entity type, and specific entities. PM statistics are 
collected for the following types of entities: 
• 
Ethernet ports 
• 
System parameters: memory usage and CPU utilization 
If PM statistics collection is disabled for a particular entity type, then no PM statistics collection is done 
for any entity of that type, except those for which PM statistics collection is enabled. 
When PM statistics collection is enabled for all entities of the same type, then when a new entity of that 
type is added the device automatically starts collecting PM statistics for it, as soon as PM statistics 
maintenance (if applicable) is enabled for the entity. 
Note 
If you are using the RADview PM Portal, it is recommended to enable PM 
statistics collection for all relevant entities. See Examples for a script that you 
can use for this purpose. 
PM statistics collection is performed at user-configurable intervals of one second to 15 minutes. A 
different interval can be configured for each entity type, and for specific entities. 
If different intervals are scheduled for collection at the same time, ETX-1p collects the PM statistics 
starting with the interval that has the highest frequency, and ending with the interval that has the 
lowest frequency. If  the OS has not finished collecting the statistics for an interval when the scheduled 
time for another interval arrives, the following action is taken according to whether the new interval is 
the next interval, or an interval with higher frequency: 
• 
If it is the next interval, then the next interval is canceled, and a PM record indicating the 
cancellation is inserted in the PM data. 
• 
If it is an interval with higher frequency, then ETX-1p collects the higher frequency interval 
statistics and then resumes collecting the lower frequency interval statistics. The PM data is 
retrieved from ETX-1p by RADview via TFTP or SFTP. After PM data is retrieved, ETX-1p deletes 
the file and opens a new one for further data. 
12. Monitoring and Diagnostics 
The PM file includes the following information: buffer (kernel) memory utilization and TCA, CPU 
utilization, memory utilization, flash memory utilization, and device uptime. 
Factory Defaults 
Command 
Level under config 
Default  
Remarks 
pm 
reporting 
pm 
PM statistics collection in device is 
globally enabled by default. 
pm-collection  
Specific entity level 
Disabled 
PM statistics collection for specific 
entities is not explicitly configured 
by default; therefore, it is disabled 
until statistics collection is enabled 
for the entity type or entity.  
pm-collection 
ethernet 
reporting 
Disabled 
PM statistics collection for 
Ethernet ports is not explicitly 
configured by default; therefore, it 
is disabled.  
pm-collection system 
reporting 
Disabled 
PM statistics collection for 
memory usage and CPU utilization 
is not explicitly configured by 
default; therefore, it is disabled. 
 
 
Configuring Performance Management 
You can configure PM statistics collection for the entire device via the pm command, and for entity 
types via the pm-collection command, in the reporting level. For specific entities, you can configure PM 
statistics collection via pm-collection, in the specific entity level.  
You can configure the device to record statistics at fixed intervals using the pm-collection interval 
<seconds> command. For parameters that are not zeroed regularly, it is recommended to record 
statistics at fixed intervals. The interval parameter for the pm-collection command can range from 1 to 
900 seconds (15 minutes); however, the value must divide evenly into 3600. It is also recommended to 
set the interval value at 60 seconds or higher. Different intervals can be specified for an entity type and 
for specific entities of that type, up to a supported maximum number of intervals. For example, if the 
PM statistics collection interval for all Ethernet ports is configured to 15 minutes, and the PM statistics 
collection interval for Ethernet 1 port is configured to 1 minute, the data displayed in the RADview PM 
portal shows Ethernet data for every 15 minutes, and Ethernet 1 data for every minute.  
12. Monitoring and Diagnostics 
The following shows the PM statistics collection configuration tasks, and their corresponding 
commands, as well as the level of each command.  
Task 
Level under config 
Command 
Comments 
Enabling PM 
statistics collection 
for a specific 
Ethernet port  
port > 
ethernet(<port-name>) 
 
pm-collection  
interval <seconds>  
PM collection can be enabled 
at a defined interval.  
It is recommended to set the 
interval value at 60 seconds or 
higher.  
Enter no pm-collection to 
disable PM statistics collection 
for the Ethernet port. 
Globally enabling PM 
statistics collection 
for device 
reporting 
pm 
Enter no pm to disable all PM 
statistics collection in ETX-1p. 
Note: no pm stops all PM 
collection regardless of other 
PM configuration; however, it 
does not change other 
configurations.  
It deletes any collected PM 
data and PM files, as well. 
Enabling PM 
statistics collection 
for Ethernet ports  
reporting 
pm-collection 
ethernet  
{interval <seconds>} 
PM collection can be enabled 
at a defined interval.  
It is recommended to set the 
interval value at 60 seconds or 
higher.  
Enter no pm-collection eth to 
disable PM statistics collection 
for Ethernet ports. 
Enabling PM 
statistics collection 
for system 
parameters 
reporting 
 
 
pm-collection 
system {interval 
<seconds> }  
 
PM collection can be enabled 
at a defined interval.  
It is recommended to set the 
interval value at 60 seconds or 
higher.  
Enter no pm-collection system 
to disable PM statistics 
collection for system 
parameters. 
 
12. Monitoring and Diagnostics 
Note 
PM statistics are collected for entities for which PM statistics collection is 
specifically enabled in the entity level via pm-collection, even if PM statistics 
collection for the entity type is disabled. 
Viewing Performance Management Configuration 
You can use the info detail command to view the performance management configuration. 
 To view the performance management configuration for the device and for entity types: 
1. Navigate to configure reporting. 
23. Enter info detail | include pm to view PM-related commands in the configuration. 
 To view the performance management configuration for specific entities: 
1. Navigate to the specific entity level. 
24. Enter info detail | include pm to view PM-related commands in the configuration. 
Examples 
 To enable PM for all relevant entities in the device: 
• 
PM statistics collection enabled for device 
• 
PM statistics collection enabled for all relevant entities, every five minutes. 
exit all 
configure reporting 
#**** Enable PM in device 
pm 
#**** Enable PM for Eth ports, collection interval=5 min 
  pm-collection ethernet interval 300 
exit all 
save 
 To configure the following PM: 
• 
PM statistics collection enabled for device. 
• 
PM statistics collection enabled for Ethernet ports, every two minutes. 
12. Monitoring and Diagnostics 
• 
PM statistics collection for Ethernet port lan1  lan1 configured to every minute.  
exit all 
configure reporting 
#**** Enable PM in device 
pm 
#**** Enable PM for Eth ports, collection interval=2 min 
  pm-collection eth interval 120 
exit all 
 
 
#**** Configure PM statistics collection interval for Ethernet port lan1 lan1 , to 1 min 
configure port ethernet lan1 lan1   
  pm-collection interval 60 
exit all 
save 
 To display PM configuration from above example: 
# configure reporting 
config>reporting# info detail | include pm 
    pm 
    pm-collection ethernet interval 120 
     
config>reporting# exit all 
 
# configure port ethernet lan1   lan1 
config>port>eth(lan1  )# info detail | include pm 
    pm-collection interval 60 
Configuration Errors 
The following table lists the messages displayed by ETX-1p when a configuration error is detected.  
Message 
Description 
Invalid interval; must divide evenly into 
3600 
The pm-collection command was entered with an interval value 
that does not divide evenly into 3600. 
Cannot execute; too many different 
intervals 
Attempt was made to configure more than 5 different intervals.  

## 12.5 Port Mirroring  *(p.695)*

12. Monitoring and Diagnostics 
12.5 Port Mirroring  
ETX-1p features local port mirroring (also called traffic mirroring), enabling you to constantly monitor 
and diagnose network traffic passing through ports, without disrupting traffic. A traffic analyzer at the 
destination port can receive, record and analyze the traffic, sending an alert when a problem or error 
occurs.  
ETX-1p supports both inbound Rx mirroring of port ingress traffic and outbound Tx mirroring of port 
egress traffic.  
Applicability and Scaling 
This feature is applicable to all device options, with support for the following: 
• 
Up to five mirroring sessions 
• 
Up to ten sources can be configured on all the sessions in the device. 
Port mirroring supports the following interfaces as sources for mirrored traffic: 
• 
Cellular port 
• 
Wi-Fi port 
• 
Ethernet port 
• 
VLAN 
• 
Tunnel interface 
All devices support a single mirror (destination) port, which can be one of the following: 
• 
Ethernet port 
• 
VLAN 
Standards 
N/A  
12. Monitoring and Diagnostics 
Functional Description 
You configure port mirroring by defining a mirroring session, its sources, the traffic direction of each 
source (Rx, Tx, or Rx-Tx), and a single destination. 
The mirror port (destination port) is dedicated solely for mirroring and does not support forwarding of 
traffic (other than mirrored packets). 
At any time, you can monitor in your device inbound (Rx) traffic to one port and/or outbound (Tx) traffic 
from another port, or both Rx and Tx traffic of a single port. You can configure mirroring of Rx and Tx 
traffic in one mirroring session to the same destination port or in two mirroring sessions to two separate 
destination ports.  
You connect a PC or other capturing device that has a traffic analyzer to an unused port of your device 
(destination port). Then, you activate a mirroring session to capture the traffic going into or out of the 
source port and send it to the destination port for analysis. 
Note 
In port mirroring you must configure the source and destination on two 
different ports. Otherwise, this results in an endless loop of traffic. 
A mirroring session source can be added while the session is running. Configuration of a new mirror 
destination overrides the existing one; there is no need to delete the existing destination. 
The device issues an event in the following two cases: 
• 
A port mirroring session is activated. 
• 
A port mirroring session is stopped. 
The device also issues an alarm when a port mirroring session is set. 
Factory Defaults  
By default, no port mirroring session is configured; when one is added, it is disabled by default, and has 
neither source nor destination configured. 
Configuring Port Mirroring 
 To configure port mirroring: 
1. Navigate to configure mirroring-session <num>. 
12. Monitoring and Diagnostics 
Note 
• 
<num> is the number of the mirroring session.  
• 
Enter no mirroring-session (num) to disable the mirroring session. 
25. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Adding/removing source port 
to/from the mirroring session 
 
[no] source port cellular <port-index> 
[tx | rx | tx-rx] 
[no] source port ethernet <port-index> 
[vlan <vid>] [tx | rx | tx-rx] 
[no] source tunnel-interface <router> 
<number> [tx | rx | tx-rx] 
[no] source port wlan <port-index> 
access-point <number> [tx | rx | tx-rx] 
tx – enable mirroring of outbound traffic. 
rx – enable mirroring of inbound traffic. 
tx-rx – enable mirroring of both 
outbound and inbound traffic. 
Note: Source and destination must be 
configured on two different ports.  
Adding/removing destination 
port/VLAN to/from the mirroring 
session 
destination ethernet <port-index> 
[vlan <vid>] 
no destination 
 
Notes:  
• A destination port can be used in one 
mirroring session only. 
• Source and destination must be 
configured on two different ports. 
Administratively enabling port 
mirroring 
no shutdown 
Enter shutdown to administratively 
disable the mirroring session. 
This command enables you to keep the 
mirror configuration and activate it only 
when needed. 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
Message 
Possible Cause 
Corrective Action 
Maximum number of 
sources has been reached 
 
Up to ten sources can be configured on all the 
sessions in the device; you tried to configure 
more 
 
Source configured as 
session destination 
You tried to configure the source as a session 
destination 
 
Destination configured as 
session source 
You tried to configure the destination as a 
session source 
 

## 12.6 Detecting Problems  *(p.698)*

12. Monitoring and Diagnostics 
Message 
Possible Cause 
Corrective Action 
Destination configured as 
another session destination 
A destination port can be used in one 
mirroring session only. 
Define a different destination 
for each session. 
Destination may not be 
bound to upper layer 
The destination cannot be bound to a router 
interface, bridge port or PPP port. 
 
Maximum number of 
sessions has been reached 
You can only configure up to five sessions 
 
Examples 
In the following example, all the inbound traffic into and outbound traffic from cellular LTE port and 
tunnel interface 1/1 is mirrored to Ethernet port 1.  
#   Mirroring Session Configuration 
    mirroring-session 20 
        source port cellular lte 
        source tunnel-interface 1 1 
        destination ethernet wan1 
        no shutdown 
    exit 
Note: There is no need to specify the direction since tx-rx is the default value. 
12.6 Detecting Problems  
An alarm is an indication of a fault in ETX-1p. An event is an occurrence in ETX-1p that may be a fault, 
user login, change in port status, etc. An SNMP trap can be sent to management stations as the result of 
an alarm or event. Besides traps, Syslog messages can also be sent as a result of alarms or events (see 
Generating Log Report above). In addition, NETCONF notifications are sent to each NETCONF client that 
has created a notification subscription (see NETCONF-Based Network Management in the Management 
and Security chapter). 
You can configure alarms and events to pop up on the serial CLI terminal. 
Alarms and events have the following properties: 
12. Monitoring and Diagnostics 
Source Type  
An entity for which alarms and events can be generated. The 
source consists of a source type (e.g. Ethernet port) and source ID 
(e.g. port number, in case of Ethernet port)   
Available source types: system, bgp-peer, gre-tunnel 
Name 
Unique alphanumeric identification of the alarm/event, up to 
32 characters 
Description 
Alphanumeric description that provides details on the 
alarm/event 
Trap Name 
ID 
Default Severity 
Name of trap 
Unique numeric identification of the alarm/event 
Alarms only; Critical, Major, or Minor 
 
Controlling Popup Behavior 
Alarms and events are displayed (pop up) on active CLI terminals as soon as they occur. You can disable 
the popups per management session. It is relevant only for a management session (serial or SSH) for 
which it is configured, and does not affect any other active session. 
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
 
Alarms and Events  
You can view the full lists of alarms and events supported by ETX-1p. 

## 12.7 Running a Ping Test  *(p.700)*

12. Monitoring and Diagnostics 
Note 
When viewing this file online, embedded attachments may not open due to 
your browser settings. Downloading this file from www.rad.com and viewing 
it offline guarantees that embedded files always open. 
 
 To view the alarms table: 
• 
Double-click the paper clip image 
 on the following line. 
 
 To view the events table: 
• 
Double-click the paper clip image 
 on the following line. 
 
 
Note 
Virtualization alarms and events are not relevant to this version of ETX-1p. 
12.7 Running a Ping Test 
You can ping a remote host (IPv4/IPv6 address or URL) to check the ETX-1p IP connectivity with that 
host.  
Applicability and Scaling 
This feature is applicable to all the device versions. 
Functional Description 
You can define the number of pings (packets) to generate or configure a continuous ping (infinite). The 
ping generator continues to generate ping requests according to the number of configured pings, or 
until you manually disrupt it (by pressing Ctrl+C). 
12. Monitoring and Diagnostics 
Configuring a Ping Test  
 To ping an IP host: 
• 
In any level, start pinging the host specifying its IP address (IPv4 or IPv6) and optionally the 
number of packets to send, payload size (in bytes), router entity number and source address: 
ping <ip-address> [number-of-packets <packets>] [payload-size <bytes>] 
[router-entity <number>] [source-address <address>]  
Ping Test Parameters 
Parameter 
Description 
Value 
<ip-address> 
Destination IP address or URL 
IP address can be a valid IPv4 or 
IPv6 address (any unicast address)  
Note: Multicast address is not 
allowed. 
If a URL is specified, the ping will 
start after the URL is resolved to an 
IP address, with DNS or static 
configuration. Make sure you have 
DNS server configuration or static 
configuration of ip-host (see 
Configuring the Router).  
number-of-packets 
Number of pings 
Possible values:  
0 (forever), 1-10000 
Default: 5 
payload-size 
Packet size 
Possible values:  
32-1450 bytes 
router-entity 
Related router-entity 
Possible values: 1-max-vrf-number 
source-address 
Source IP address 
Valid IPv4 or IPv6 address (any 
unicast address)  
 
If the remote host answers, ETX-1p displays the ping results including the round trip delay, rounded as in 
the following table. 
12. Monitoring and Diagnostics 
Ping Round Trip Results  
Round Trip Delay 
Displayed in Ping Results 
<= 10 msec 
time < 10 ms 
>= 11 msec and <= 20 msec 
time < 20 ms 
>= 21 msec and <= 30 msec 
time < 30 ms 
>= 31 msec and <= 40 msec 
time < 40 ms 
Examples 
#ping 10.10.10.10 
 
Reply from 10.10.10.10: bytes = 32, packet number = 0, time < 10 ms 
Reply from 10.10.10.10: bytes = 32, packet number = 1, time < 10 ms 
Reply from 10.10.10.10.44: bytes = 32, packet number = 2, time < 10 ms 
 
config>router(1)# ping 35.35.35.2 source-address 12.12.12.12 
 
Reply from 35.35.35.2: bytes = 32, packet number = 0, time <= 1 ms 
Reply from 35.35.35.2: bytes = 32, packet number = 1, time <= 1 ms 
Reply from 35.35.35.2: bytes = 32, packet number = 2, time <= 1 ms 
Reply from 35.35.35.2: bytes = 32, packet number = 3, time <= 1 ms 
Reply from 35.35.35.2: bytes = 32, packet number = 4, time <= 1 ms 
5 packets transmitted. 5 packets received, 0% packet loss 
round-trip (ms) min/avg/max = 1/1/1 
 
config# ping google.com 
 
Reply from 8.8.8.8: bytes = 32, packet number = 0, time <= 60 ms 
Reply from 8.8.8.8: bytes = 32, packet number = 1, time <= 61 ms 
Reply from 8.8.8.8: bytes = 32, packet number = 2, time <= 60 ms 
Reply from 8.8.8.8: bytes = 32, packet number = 3, time <= 60 ms 
Reply from 8.8.8.8: bytes = 32, packet number = 4, time <= 59 ms 
5 packets transmitted. 5 packets received, 0% packet loss 
round-trip (ms) min/avg/max = 59/60/61 

## 12.8 Tracing the Route  *(p.703)*


## 12.9 Technical Support  *(p.703)*

12. Monitoring and Diagnostics 
12.8 Tracing the Route 
This diagnostic utility traces the route through the network from ETX-1p to the destination host. The 
trace route utility supports up to 30 hops. 
Applicability and Scaling 
This feature is applicable to all the device versions. 
Running Trace Route 
 To trace a route: 
• 
In any level, start the trace route and specify the IP address (IPv4 or IPv6) of the host to which 
you intend to trace route: 
trace-route <1.1.1.1–255.255.255.255> 
12.9 Technical Support 
For technical support of registered products, contact your local authorized RAD partner or go to 
RADCare Online (if you have a valid RADCare service package). 
RAD would like your help in improving its product documentation. Please send us an e-mail with your 
comments. 
Thank you for your assistance! 
 
