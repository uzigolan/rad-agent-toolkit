# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.11 Handling Alarms and Events

*Manual `MiNID_ver_2_6_mn.pdf`, pages 369–371.*


## Defining Alarm Types  *(p.369)*

11. Monitoring and Diagnostics 
For further information, refer to the relevant sections in Chapter 6 –10 and the relevant sections in the 
troubleshooting chart. 
11.11 Handling Alarms and Events 
This section describes how to display and clear the event log, and lists the  events and traps. 
Defining Alarm Types 
The alarm type can be defined as the “legacy” alarms or the new SOAM alarms supported by MEF 36. 
 To define the alarm type using the web interface: 
1. Navigate to Configuration > OAM > CFM. 
 
  
 
 
 Configuration>OAM>CFM 
  
 
 
 Alarm Type 
Legacy/SOAM 
 
  
 
 
 Add New MD 
 
 
  
 
 
  
 
 
 Apply 
 
 
  
 
 
1. Select the relevant alarm type: 
 
Legacy: Previous alarm set 
 
SOAM: New MEF 36 alarm set. This mode supports alarm suppression. 
 To define the alarm type using the CLI: 
1. Navigate to MiNID>config>oam>cfm#. 
2. Use the following command to select alarm type: 

## Working with the Event Log  *(p.370)*

11. Monitoring and Diagnostics 
 
alarm-type {legacy | soam} 
Working with the Event Log 
The event log contains the events that have occurred since the last startup of . The event log can hold up 
to 300 events. If it reaches that limit, further events are stored in a wraparound fashion, i.e. the later 
events overwrite the earlier events. The file entries are time-stamped with the time since the last 
startup. 
 To display the event log: 
Do one of the following: 
• 
In the web interface, go to Monitoring > System, and click Events Log:  
MiNID 
  
 
 
 Monitoring - System 
  
 
 
 Device Management MAC address 00-20-D2-51-7E-2D 
 
 Router Int2,4 MAC address 
00-20-D2-51-7E-2F 
 
 Device Services MAC address 
00-20-D2-51-7E-2E 
 
 System Up Time (hh:mm:ss) 
05:35:48 
 
 DIP Switches Mode 
Normal 
 
  
 
 
 Current date 
10 May 2025 14:15:51+00:00 
 
 Summer time 
not configured 
 
  
 
 
 NTP 
 
 
 Events Log 
 
 
  
 
 
Monitoring System 
11. Monitoring and Diagnostics 
MiNID 
 
 
 
 
 
 
Monitoring>System>Events Log 
 
 
 
 
 
 
Log Page 
 
1 
 
 
Time 
Event 
Severity 
Description 
 
00:04:38 
LOC 
MAJOR 
OFF, MEP [2.MA1.1.55] 
 
00:04:20 
LOC 
MAJOR 
ON, MEP [2.MA1.1.55] 
 
00:04:12 
UPLOAD FILE 
MINOR 
Upload log-file success via 
SFTP 
 
00:01:01 
TELNET MESSAGE 
MINOR 
CLI Parsing startup-config 
Success 
 
00:00:53 
LINK UP 
MAJOR 
SFP Port (sleeve) 
 
00:00:46 
LINK DOWN 
MAJOR 
SFP Port (sleeve) 
 
00:00:31 
LOGIN SUCCESS 
MAJOR 
User: su (telnet) 
 
 
 
 
 
 
Clear table 
 
 
 
 
 
 
 
 
Displaying Event Log 
• 
In the CLI, go to the configure reporting level, and enter show log. 
>config>report# show log 
Time         Event            Severity     Description 
--------------------------------------------------------- 
00:04:38     LOC              MAJOR        OFF, MEP [2.MA1.1.55] 
00:04:20     LOC              MAJOR        ON, MEP [2.MA1.1.55] 
00:04:12     UPLOAD FILE      MINOR        Upload log file success via SFTP 
00:01:01     TELNET MESSAGE   MINOR        CLI Parsing startup-config Success 
00:00:53     LINK UP          MAJOR        SFP Port (sleeve) 
00:00:46     LINK DOWN        MAJOR        SFP Port(sleeve) 
00:00:31     LOGIN SUCCESS    MAJOR        User: su (telnet) 
 To clear the event log: 
Do one of the following: 
• 
In the web interface, go to Monitoring > System> Log File as described in the above procedure 
to display the event log, and click Clear table. 
• 
In the CLI, go to the configure reporting level, and enter clear-log. 
>config>report# clear-log 