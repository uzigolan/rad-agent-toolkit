# Feature Reference – 8 Monitoring and Diagnostics – 8.7 Syslog

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1476–1484.*


## Applicability and Scaling  *(p.1476)*


## Standards  *(p.1476)*


## Functional Description  *(p.1476)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
8.7 Syslog 
ETX‑2i uses the Syslog protocol to generate event notification messages and transport them over IP 
networks to Syslog servers.  
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
This feature is applicable to all ETX‑2i products. 
Standards 
RFC 3164, RFC 5674 
Functional Description 
When an alarm or event occurs, if it is not masked for logging, it is saved in the log file. The Syslog 
protocol provides an instrument for generating and transporting event notification messages from 
ETX‑2i logs to servers across IP networks.  
Optionally, you can enable Syslog servers to also log accounting commands. 
You can log these events on remote Syslog servers, or locally (i.e., on the device), in which case you 
configure a local Syslog server with IP address 127.0.0.1 (see Local Syslog Accounting below). 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Note 
The password that you enter when creating a new user (configure 
management login-user <name> password <password>, or when copying a 
file (file copy <source-file-url> <destination-file-url> 
sftp://<username>:<password>) is masked in Syslog under CLI command 
accounting. The password entered appears in the Syslog command-log as 
asterisks (*), thus providing protection from sniffers. 
In addition, the <password> can be omitted from the command and entered 
separately (interactively) when prompted. 
 
ETX-2i
ETX-2i-B
PSN
Syslog 
Server
 
 
Syslog Functionality 
Elements 
Typical Syslog topology includes message senders (clients) and message receivers (servers). ETX‑2i 
supports Syslog client functionality. It can send messages to up to five Syslog servers. The receiver 
displays, stores, or forwards logged information. The standard designates two types of receivers: 
Relay 
Forwards messages 
Collector 
Displays and stores messages 
Transport Protocol 
Usually, Syslog uses UDP port 514 for its transport, but devices and servers can be defined to use any 
port for communication. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message Format 
A Syslog message contains up to 1024 bytes and includes the following information: 
• 
Facility and severity (see below) 
• 
Timestamp – local time of the device when it sent the message  
• 
Hostname – IP address (default) or system name (recommended) of the device that sent the 
message  
• 
Message content – tag and message content.  
 
Tag:  
 
For an alarm or event – Tag is the source of the alarm/event, which is a string combining 
source type and source ID (such as system, Eth 1, E1 1/1).  
 
For an accounting command – Tag is CMD_ACCT.  
 
Message content – a colon (:) followed by: 
 
For an alarm or event – the alarm/event description, as sent in SNMP traps. 
 
For an accounting command – user@device: command, where 
user – username logged in or out. If the command was executed by the device 
scheduler, the user is sched.  
device – IP address of the user’s machine (in case of Telnet or SSH), console if the 
session is from the local ACSII terminal, or sched if the command was executed by the 
device scheduler. 
command – command or level change that was executed, e.g., level-1 or no shutdown. 
A typical Syslog message for an event looks like this: 
<145>Jan 15 13:24:07 172.17.160.69 Eth 1: Loss of signal (LOS) 
A typical Syslog message for an accounting command looks like this: 
<146>Jan 22 13:00:08 172.17.160.69 CMD_ACCT: sched sched no shutdown 
Facilities and Severities 
Facility designates a device or application that sends a message. The standard includes some predefined 
facilities in the 0–15 range. For originator identification, you can configure ETX‑2i to use facilities local1– 
local7; local1 is the default facility. 
Severity is assigned to a message to specify its importance. The device sends messages to Syslog servers 
with severity equal to or higher than the configured severity level.  
Note 
Alarms and events masked for logging are not sent to Syslog regardless of the 
severity. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
ETX‑2i uses the following severity designations: 
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
Local Syslog Accounting 
ETX‑2i supports saving into a local cyclic accounting file, called accounting-log, each CLI configuration 
command. This includes NETCONF RPC converted into CLI commands.   
You can configure local Syslog accounting by configuring a local Syslog server with IP address 127.0.0.1, 
and using the regular Syslog commands (except port, which is irrelevant).  
Accounting messages are saved in the accounting-log file in the same format used when sending them 
to external Syslog servers. 
The accounting-log file has the following features: 
• 
The file has two partitions. When both partitions become full, the partition with the older 
records is cleared.  
• 
The file can be cleared of its records, but not deleted. 
• 
The file is not affected by device reboot, as it is saved in permanent memory. 
• 
The file can be uploaded using the copy command but cannot be downloaded. 
You can display the accounting-log file using the show accounting-log command (see Viewing the Syslog 
Local Accounting Log), or clear it using the clear-accounting-log command (see Clearing the Syslog Local 
Accounting Log). 

## Factory Defaults  *(p.1480)*


## Configuring Syslog  *(p.1480)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Factory Defaults 
By default, Syslog operation is disabled. When enabled, the default parameters are as follows: 
Parameter 
Default Value 
Syslog device 
 
facility 
local1 
hostname 
ip-address 
port 
514 
severity-level 
informational 
shutdown 
shutdown 
Syslog server 
 
address 
0.0.0.0 
port 
514 
accounting 
no accounting 
shutdown 
shutdown  
Configuring Syslog  
When configuring Syslog parameters, it is mandatory to enable the Syslog device (client) and define 
Syslog servers. The remaining configuration is optional. 
Configuring the Syslog Device 
 To configure the Syslog device: 
1. Navigate to configure system syslog device. 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Clearing Syslog statistics 
clear-statistics 
See Viewing Syslog Statistics. 
Defining a Syslog facility from which 
Syslog messages are sent 
facility { local1 | local2 | local3 | 
local4 | local5 | local6 | local7 7} 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining the hostname in the Syslog 
message  
hostname { ip-address | sysname } ip-address – default; a dotted 
decimal notation of the IP 
address from which the message 
was sent (e.g., 127.0.0.1) 
sysname – recommended; the 
string stored in the SNMP 
sysName object 
Defining Syslog device UDP port for 
communication 
port <udp-port-number> 
Possible values: 1–65535 
Port configuration is allowed 
only if a Syslog device is 
administratively disabled. 
Defining severity level 
severity-level { emergency | alert | 
critical | error | warning | notice | 
informational | debug } 
The log messages that contain 
severity level above or equal to 
the specified level are 
transmitted. 
emergency – emergency 
messages 
alert – critical alarms 
critical – major alarms 
error – minor alarms 
warning – events 
notice – cleared alarms, 
accounting messages 
informational – informational 
messages 
debug – debug messages 
Administratively enabling Syslog device 
no shutdown 
shutdown administratively 
disables the Syslog device. 
Displaying Syslog statistics 
show statistics 
See Viewing Syslog Statistics.  
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuring the Syslog Server 
 To configure the Syslog server: 
1. Navigate to configure system. 
2. At the config>system# prompt, enter syslog server <server-ID> to specify the server to receive 
Syslog messages, where server-ID is 1 to 5. 
The config>system>syslog(server/<server-ID>)# prompt is displayed. 
3. Enter the necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Enabling Syslog accounting (i.e., logging) 
of command entries  
[no] accounting commands 
To disable command logging, 
enter no accounting. 
Note: Currently, only commands 
accounting is available. 
Defining Syslog server IP address 
address <ip-address> 
Possible values: 
0.0.0.0–255.255.255.255 
Note: For local Syslog 
accounting, enter ip-address 
127.0.0.1. 
Defining Syslog server UDP port for 
communication 
port <udp-port-number> 
Possible values: 1–65535 
Note: For local Syslog accounting 
(server 127.0.0.1), the Syslog 
port is not open to packets 
entering from out of the device. 
In this case, port command is 
not available. 
Administratively enabling Syslog server  
no shutdown 
shutdown administratively 
disables Syslog server. 
Note: shutdown command is 
available only after you assign an 
IP address to the Syslog server. 

## Viewing Syslog Statistics  *(p.1483)*


## Viewing the Syslog Local Accounting Log  *(p.1483)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing Syslog Statistics 
 To display Syslog statistics: 
1. Navigate to configure system syslog device. 
2. At the config>system>syslog(device)#, enter show statistics. 
Syslog statistics appear as shown below. The counters are described in the following table. 
ETX‑2i>config>system>syslog(device)# show statistics 
Total Tx Messages 
 
 
: 356 
Non-queued Dropped Messages 
 
 
: 265 
Parameter 
Description 
Total Tx Messages 
The total number of Syslog messages transmitted 
Non-queued Dropped Messages 
The total number of Syslog messages that were dropped before being 
queued 
 To clear Syslog statistics: 
1. Navigate to configure system syslog device. 
2. At the config>system>syslog(device)# prompt, enter clear-statistics. 
The Syslog statistic counters are set to 0. 
Viewing the Syslog Local Accounting Log 
 To display the Syslog local accounting log: 
1. Navigate to configure reporting. 
2. At the config>reporting# prompt, enter show accounting-log. 
The Syslog local accounting log is displayed, as shown in the following example.  
ETX‑2i>config>reporting# show accounting-log 
<141>Jan 1 00:08:47 127.0.0.1 CMD_ACCT:su@172.17.230.68: no shutdown 
<141>Jan 1 00:08:47 127.0.0.1 CMD_ACCT:su@172.17.230.68: exit 
<141>Jan 1 00:08:56 127.0.0.1 CMD_ACCT:su@172.17.230.68: configure reporting 
<141>Jan 1 00:09:00 127.0.0.1 CMD_ACCT:su@172.17.230.68: show accounting-log 
<141>Jan 1 00:09:10 127.0.0.1 CMD_ACCT:su@172.17.230.68: exit 
<141>Jan 1 00:09:12 127.0.0.1 CMD_ACCT:su@172.17.230.68: system 
<141>Jan 1 00:09:29 127.0.0.1 CMD_ACCT:su@172.17.230.68: syslog server 1 
<141>Jan 1 00:10:00 127.0.0.1 CMD_ACCT:su@172.17.230.68: no shutdown 
<141>Jan 1 00:10:03 127.0.0.1 CMD_ACCT:su@172.17.230.68: exit 

## Clearing the Syslog Local Accounting Log  *(p.1484)*


## Configuration Errors  *(p.1484)*


## Example  *(p.1484)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Clearing the Syslog Local Accounting Log 
You can clear the local accounting-log file of its contents. You cannot delete the file. 
 To clear the Syslog accounting log: 
1. Navigate to configure reporting. 
2. At the config>reporting# prompt, enter clear-accounting-log. 
Configuration Errors 
The following table lists messages generated by ETX‑2i when a configuration error is detected. 
Message 
Description 
Syslog Port is out of range 
Selected UDP port value is out of allowed range (1–65535). 
Port is illegal or Device Port is already in 
use 
Selected UDP port is already in use. 
Parameter cannot be changed if Logging 
Status/Server Access is enabled 
Device/server UDP port or server IP address cannot be changed 
while Syslog server is enabled. 
Illegal Severity 
Invalid severity value 
Illegal Facility 
Invalid facility value 
Illegal Server IP Address 
Invalid server IP address 
Example 
• 
Syslog device 
 
Facility: local2 
 
UDP port: 155 
 
Severity level: major 
• 
Syslog server 
 
Server IP address: 178.16.173.152 
 
UDP port: 155 
 
 