# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.9 Syslog

*Manual `MiNID_ver_2_6_mn.pdf`, pages 361–367.*


## Applicability and Scaling  *(p.361)*


## Standards Compliance  *(p.361)*


## Benefits  *(p.361)*


## Functional Description  *(p.361)*

11. Monitoring and Diagnostics 
11.9 Syslog 
MiNID uses the Syslog protocol to generate and transport event notification messages over IP networks 
to Syslog servers. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
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
from MiNID to servers across IP networks. 
11. Monitoring and Diagnostics 
Elements 
Typical Syslog topology includes message senders (devices) and message receivers (servers). MiNID 
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
facilities in the 0–15 range. For originator identification, MiNID uses facilities local1– local7. 
Severity is assigned to a message to specify its importance. MiNID uses the following severity 
designations: 
Syslog Severities 
Code 
Syslog Type 
Description 
0 
Emergency 
Emergency message 
1 
Alert 
Critical alarm 

## Factory Defaults  *(p.363)*


## Configuring Syslog Parameters  *(p.363)*

11. Monitoring and Diagnostics 
Code 
Syslog Type 
Description 
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
 
Note 
The Syslog operation is not supported if  uses a loaned IP address. 
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
 To configure Syslog device in the CLI: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. Enter the necessary commands according to the tasks listed below. 
11. Monitoring and Diagnostics 
Syslog Configuration Parameters 
Task 
Command 
Comments 
Defining a facility from which Syslog 
messages are sent 
facility {local1 | local2 | local3 | 
local4 | local5 | local6 | local7} 
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
informational | debug} 
The log messages that contain 
severity level above or equal to 
the specified level are 
transmitted. 
Administratively enabling Syslog device 
no shutdown 
shutdown administratively 
disables the Syslog device. 
Displaying statistics 
show statistics 
Clearing statistics 
clear-statistics 
 To configure a Syslog server in the CLI: 
1. Navigate to configure system). 
The config>system# prompt is displayed. 
2. At the config>system# prompt, enter syslog server <server-ID> to specify the server to receive 
Syslog messages, where <server-ID> is 1 to 5. 
The config>system>syslog(<server-ID>)# prompt is displayed. 
3. Enter the necessary commands according to the tasks listed below. 
Syslog Server Parameters 
Task 
Command 
Comments 
Enabling logging of command entries  
accounting commands 
To disable command logging, 
enter no accounting commands 
Defining Syslog server IP address 
address <ip-address> 
Possible values: 
0.0.0.0–255.255.255.255 
Defining Syslog server UDP port for 
communication 
port <udp-port-number> 
Possible values: 1–65535 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Administratively enabling Syslog server 
no shutdown 
shutdown administratively 
disables Syslog server. 
 To configure Syslog device in the web interface: 
1. Go to Configuration > System > Syslog. 
 
  
 
 
 Configuration – System - Syslog 
  
 
 
 Device Configuration: 
 
 
 Facility 
Local1 
 
 Severity Level 
informational 
 
 Port 
514 
 
 Admin Status 
Disable 
 
  
 
 
 Apply 
 
 
  
 
 
 Server Configuration 
 
 
 
Server ID 
Address 
Accounting Commands 
Port 
Admin Status 
 
 
1 
FE80:B5BA:59E4:1A3D:F3CD 
ENABLED 
514 
ENABLED 
 
 
2 
192.168.205.55 
ENABLED 
514 
ENABLED 
 
 
3 
192.168.205.2 
ENABLED 
514 
ENABLED 
 
 
4 
0.0.0.0 
DISABLED 
514 
DISABLED 
 
 
5 
0.0.0.0 
DISABLED 
514 
DISABLED 
 
  
 
 
 Statistics: 
 
 
 Total Tx Messages 
356 
 
 Non-queued Dropped Messages 
10 
 
 Clear Statistics 
 
 
  
 
 
Syslog Configuration 
2. Set the device configuration according to Syslog Server Parameters table. 
3. Click <Apply>. 

## Viewing Syslog Statistics  *(p.366)*

11. Monitoring and Diagnostics 
 To configure a Syslog server in the web interface: 
1. Under Server Configuration, click the ID number of the server to receive Syslog messages. 
 
  
 
 
 Configuration – System - Syslog - Server Update 
  
 
 
 Server ID 
2 
 
 Address 
192.168.205.55 
 
 Accounting Commands 
Enable 
 
 Port 
514 
 
 Admin Status 
Enable 
 
  
 
 
 Apply 
 
 
  
 
 
1. Enter the necessary commands according to Syslog Statistic Parameters table. 
2. Click <Apply>. 
Viewing Syslog Statistics 
 To display Syslog statistics in the CLI: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. At the config>system>syslog(device)#, enter show statistics. 
Syslog statistics appear as shown below. The counters are described in the table below. 
MiNID>config>system>syslog(device)# show statistics 
Total Tx Messages  
 
: 356 
Non-queued Dropped Messages 
 
 
: 265 
Syslog Statistic Parameters 
Parameter 
Description 
Total Tx Messages 
The total number of Syslog messages transmitted 

## Example  *(p.367)*

11. Monitoring and Diagnostics 
Parameter 
Description 
Non-queued Dropped Messages 
The total number of Syslog messages that were dropped 
before being queued 
 To clear Syslog statistics in the CLI: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. At the config>system>syslog(device)# prompt, enter clear-statistics. 
The Syslog statistic counters are set to 0. 
 
 To display Syslog statistics in the web interface:  
1. Go to Configuration > System > Syslog.  
2. Syslog statistics are displayed at the bottom. The counters are described in the table above.  
 To clear Syslog statistics in the web interface:  
1. Go to Configuration > System > Syslog. 
2. Click Clear Statistics.  
The Syslog statistic counters are set to 0. 
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