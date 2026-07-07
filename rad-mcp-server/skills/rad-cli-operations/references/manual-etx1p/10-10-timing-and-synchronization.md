# 10 Timing and Synchronization

*Manual `ETX-1p_6.4_Mn_05-26_GA.pdf`, pages 636–649.*


## 10.1 GNSS Location Reporting  *(p.636)*

10. Timing and Synchronization 
10 Timing and Synchronization 
10.1 GNSS Location Reporting 
GNSS (Global Navigation Satellite System) is a part of satellite navigation system which allow users to 
determine their current position from the signals received from satellite systems called constellations. 
Each constellation consists of a set of satellites which continuously transmits signals towards the Earth.  
GNSS satellites continuously broadcast satellite position and timing data. The antenna in the device 
receives the RF signals from at least 4 satellites and these signals are passed to the GNSS receiver for 
computing the actual position. The receiver does not transmit any signal to the satellite. 
Functional Description 
The device supports GPS, GLONASS, BeiDou and Galileo satellite constellations depending upon the 
hardware used. 
GPS is always ON and works as the only primary GNSS system. Glonass, Galileo or BeiDou can be set as 
secondary system. If BeiDou is set, at least one of the other systems must be set too. 
When GNSS is enabled, the device starts receiving signals from the satellites and begins the tracking 
process. It must be locked to the satellite as long as the satellite is visible.  
Note 
Depending on the satellite constellation and other factors, time to satellite 
locking (time taken by the device to acquire satellite data and calculate 
position) can take as much as approximately 1 minute, if sufficient number of 
satellites are available. 
Factory Defaults 
The default configuration of GNSS is shown below.  
 
Parameter  
Default Value 
name 
gnss<port-number>  
10. Timing and Synchronization 
Parameter  
Default Value 
shutdown 
no shutdown 
secondary-system  
no secondary-system 
Configuring GNSS 
 To configure the GNSS receiver in the CLI: 
1. Navigate to configure system clock gnss. 
The config>system>clock>gnss# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning the name to GNSS 
port 
name <port-name> 
no name 
1-64 characters 
Administratively enabling 
GNSS receiver 
no shutdown 
Using shutdown disables the GNSS 
receiver 
Defining secondary GNSS 
system 
secondary-system [glonass] 
[galileo] [beidou] 
no secondary-system 
At least one system must be specified 
If Beidou is set, at least one of the 
other systems must be set as well 
Viewing GNSS status 
show status 
See Viewing GNSS Status 
Viewing GNSS Status 
You can view the GNSS status to see if the GNSS receiver is fully locked to the GNSS signals, and view the 
satellite statuses, if applicable.  
The information depends upon the track-status (Not tracking, Tracking satellites or Locked – see below). 
If GNSS functionality is lost after a position was received, the current position information is retained 
until a new position is acquired. 
 To view the GNSS status: 
• 
Navigate to configure system clock gnss. 
10. Timing and Synchronization 
The config>system>clock>gnss# prompt is displayed. 
• 
Enter: 
show status 
The GNSS status is displayed followed by the Satellite Status table. The GNSS status displays the 
following (depending on the tracking status): 
• 
Administrative Status 
• 
Operational Status. The operational status depends upon the administrative status and the 
actual operation status of GNSS. Operational status is down if the device is not tracking satellites 
and becomes up if the device starts tracking the satellites 
• 
Primary System (always GPS) 
• 
Secondary Systems (Glonass, Galileo, Beidou) 
• 
Tracking status: 
 
GNSS Disabled – GNSS is administratively disabled 
 
GNSS Locked – GNSS is fully operational (locked to satellites) 
 
Not Tracking Satellites – GNSS is not operational (not tracking satellites) 
 
Tracking Satellites – GNSS is tracking satellites, but not locked 
The table of satellites displays the following: 
• 
Satellite number 
• 
GNSS system (GPS, Glonass, Galileo, Beidou) 
• 
Signal to noise ratio (dB) 
• 
Satellite health (Yes, No) 
• 
Azimuth (degrees) 
• 
Elevation (degrees)  
Note 
If track-status is Not Tracking, the table of satellites is not printed. 
Examples 
 To configure GLONASS as secondary system: 
exit all 
configure system clock gnss gnss1 
secondary-system glonass  
10. Timing and Synchronization 
exit all 
save 
 To view the GNSS status: 
config>system>clock>gnss(gnss1)# show status 
 
***state is Not Tracking and there are active alarms*** 
Port Name            : gnss 1 
Administrative Status: Up 
Operational Status   : Down 
Primary System       : GPS 
Secondary Systems    : Glonass, Galileo 
Position Mode        : Auto 
Tracking Status      : Not Tracking Satellites 
 
***state is Not Tracking and there is no active alarm*** 
Port Name            : gnss 1 
Administrative Status: Up 
Operational Status   : Down 
Primary System       : GPS 
Secondary Systems    : Glonass, Galileo 
Position Mode        : Auto 
Tracking Status      : Not Tracking Satellites 
 
***state is other than Not Tracking)*** 
Port Name            : gnss 1 
Administrative Status: Up 
Operational Status   : Up 
Primary System       : GPS 
Secondary Systems    : -- 
Position Mode        : Auto 
Tracking Status      : Tracking Satellites 
 
Latitude             : N22:11:00.001 
Longitude            : E111:22:00.111 
Height               : 12345 
 
Satellite Status 
Num | System | SNR | Healthy | Azimuth | Elevation  
-------------------------------------------------- 
1   | GPS    | 42  | Yes     | 57      | 24 
15  | GPS    | 40  | Yes     | 240     | 47 

## 10.2 Date and Time  *(p.640)*

10. Timing and Synchronization 
10.2 Date and Time  
You can configure the ETX-1p internal real-time clock as free running or with Network Time Protocol 
(NTPv4).  
Applicability and Scaling 
This feature is relevant for all the device versions.  
Standards Compliance 
RFC 3231 – Definitions of Managed Objects for Scheduling Management Operations 
RFC 2863 – The Interfaces Group MIB 
RFC 3418 – Management Information Base (MIB) for the Simple Network Management Protocol (SNMP) 
RFC 4330 –Simple Network Time Protocol (SNTP) Version 4 for IPv4, IPv6 and OSI 
Benefits 
NTP synchronizes the internal clocks of network devices to a single time reference source. It provides 
comprehensive mechanisms to access national time dissemination services, organize the NTP subnet of 
servers and clients, and adjust the system clock in each participant. It improves the timekeeping quality 
of the network by using redundant reference sources and diverse paths for time distribution. 
Functional Description 
Network Time Protocol (NTP) is a networking protocol for clock synchronization  between computer 
systems over packet-switched, variable-latency data networks. NTP, a large and very complex 
application for the synchronization of computers and computer networks, incorporates complex 
statistical algorithms that filters out small discrepancies in time and makes time adjustments. It 
synchronizes all participating computers to within a few milliseconds of Coordinated Universal Time 
(UTC). 
10. Timing and Synchronization 
Factory Defaults 
The default system date and time parameters are as follows: 
Parameter 
Default Value 
date-format 
yyyy-mm-dd 
zone utc  
+00:00 
By default, no NTP servers are defined. 
When an NTP server is defined, its default configuration is: 
Parameter 
Default Value 
address  
0.0.0.0 
prefer 
no prefer 
shutdown 
shutdown 
Configuring Date and Time 
 To set the system date and time via CLI: 
1. Navigate to configure system date-and-time.  
The config>system>date-time# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying the desired date 
format 
date-format {yyyy-mm-dd | 
dd-mm-yyyy | mm-dd-yyyy | 
yyyy-dd-mm} 
 
Defining the date 
date <date> 
Date is according to the 
configured date format. 
Configuring NTP 
ntp 
 
10. Timing and Synchronization 
Task 
Command 
Comments 
Scheduling adjustment of 
product time for daylight 
saving time start and stop 
[no] summer-time 
Typing no summer-time 
removes daylight saving time 
scheduling. 
See Configuring Daylight 
Saving Time Scheduling 
Displaying daylight saving time 
scheduling information 
show summer-time 
See Viewing Scheduled 
Daylight Saving Time 
Defining the time 
time <hh:mm[:ss]> 
 
Defining the time zone relative 
to Universal Time Coordinated 
(UTC) 
zone utc [<[{+|-}]hh[:mm]>] 
Possible values: 
 -12:00 to +12:00, in 
30-minute increments 
 To set the system date and time via Web GUI: 
1. Navigate to Home>Admin.  
In this screen you can configure the following: 
 
Schedule adjustment of product time for daylight saving time start and stop 
 
Set the date and time 
 
Define the date format 
 
Define the time zone relative to Universal Time Coordinated (UTC) 
2. Click Submit. 
 
You can configure the time on the ETX-1p internal clock with the time on an NTP server.  
10. Timing and Synchronization 
This section explains how to receive the clock signal from NTP servers in the network. One of the active 
NTP servers can be designated the preferred server, so that NTP requests are sent to the preferred 
server. If there is no preferred server or if the preferred server does not answer, NTP requests are sent 
to any enabled servers. 
 To configure NTP: 
1. Navigate to configure system date-and-time ntp. 
The config>system>date-time>ntp# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining and configuring NTP 
servers  
server <server-id> 
Typing no server removes 
NTP server.  
Displaying NTP status 
show status 
See Viewing NTP Status 
Configuring source IP address of 
NTP packets 
source-address outbound-interface-
address  
no source-address 
Selecting outbound-interface-
address forces the NTP 
packets source address to be 
that of the interface from 
which the packet is to be sent, 
regardless of other 
configuration. 
 To configure an NTP server: 
1. Navigate to config system date-and-time ntp. 
The config>system>date-time>ntp# prompt is displayed. 
2. Type server <server-id> to define an NTP server with ID <server-id>. 
The following prompt is displayed: config>system>date-time>ntp>server(<server-id>)$. 
3. Enter all necessary commands according to the tasks listed below.  
 
10. Timing and Synchronization 
Task 
Command 
Comments 
Setting the IP address or name of 
the NTP server 
address {<ip-address> | <server-name>} 
Possible values:  IPv4 or IPv6 
valid unicast address (ip-
address), or 1-255 characters 
(server-name) 
[0.0.0.0|0:0:0:0::0|host-
name] 
Set NTP server as preferred server. 
prefer 
Type no prefer to remove 
preference. 
Note: Only one server can be 
preferred. 
Administratively enabling server 
no shutdown 
Entering shutdown disables 
the server. 
Sending an NTP polling request to 
check server status 
query-server 
 
 
Examples 
Setting Date and Time 
 To set the date and time: 
• 
Format = mm-dd-yyyy 
• 
Date = May 17, 2017 
• 
Time = 5:40 pm 
• 
Zone = UTC –4 hours and 30 minutes 
exit all 
configure system date-and-time 
  date-format mm-dd-yyyy 
  date 05-17-2017 
  time 17:40 
  zone utc -04:30 
10. Timing and Synchronization 
Defining the NTP Server 
 To define the NTP server: 
• 
Server ID = 1 
• 
IP address = 172.17.171.141 
• 
Preferred 
• 
Administratively enabled 
exit all 
configure system  
  date-and-time 
  zone utc +03:00 
  ntp 
  server 1 
    address 172.17.171.141 
    prefer      
    no shutdown 
exit 
Viewing Status 
Viewing Date and Time Status 
 To display the date and time: 
• 
From the system context (config>system), enter: 
show system-date 
config>system# show system-date 
2017-06-13   09:15:05  UTC  +00:00 
Viewing NTP Status  
 To display the NTP status: 
1. Navigate to config system date-and-time ntp. 
The config>system>date-time>ntp# prompt is displayed. 
2. Type show status. 
The following screen is displayed. 

## 10.3 Daylight Saving Time  *(p.646)*

10. Timing and Synchronization 
config>system>date-time>ntp# show status 
System Uptime       : 000 Days 18:45:45 
System Time (Local) : 2017-10-31                               09:28:22 
 
Current Source : NTP 
 
Locking Status : In Limits 
 
NTP Server                              Prefer    Admin     Stratum 
----------------------------------------------------------------------------- 
172.17.171.141                          Prefer    Enabled   1 
 
10.3 Daylight Saving Time 
You can schedule ETX-1p to change its system time to daylight saving time (also known as summer 
time), at a specific date and time.  
Applicability and Scaling 
This feature is relevant for all the device versions. 
Functional Description 
You can specify when the device local system time should reflect the start of daylight saving time by 
adding an offset, and when it should reflect the end of daylight saving time by subtracting the offset. 
You can schedule daylight saving time in one of the following ways: 
One shot 
Daylight saving time starts and ends once, at a specified date and 
time (e.g. November 6 2017). 
Recurring 
Daylight saving time starts and ends every year at a specified time, 
and a date specified according to the weekday and month (e.g. first 
Sunday in October). 
The daylight saving time schedule is saved in nonvolatile (permanent) memory, in order to be available 
after device reboot. 
 
10. Timing and Synchronization 
Note 
ETX-1p logs the start and end of daylight saving time with the events 
summer_time_started and summer_time_ended, respectively. Each event is 
also sent as an SNMP notification to management stations.  
Factory Defaults 
By default, no scheduling is configured. 
The default value for daylight saving time offset is 60 minutes. 
Configuring Daylight Saving Time Scheduling 
When you configure daylight saving time scheduling, the first set of parameters in the commands 
specifies when daylight saving time starts, and the second set of parameters specifies when daylight 
saving time ends. 
 To configure daylight saving time: 
• 
Navigate to the config>system>date-time level and enter the summer-time command 
according to the type of schedule: 
 
One shot – Enter: 
summer-time date {january | february | march | april | may | june | july | august | 
september | october | november | december} <dd> <yyyy> <hh>:<mm> {january | 
february | march | april | may | june | july | august | september | october | november | 
december} <dd> <yyyy> <hh>:<mm> [<offset>] 
 
Recurring – Enter: 
summer-time recurring { 1 | 2 | 3 | 4 | last} {sunday | monday | tuesday | wednesday | 
thursday | friday | saturday} {january | february | march | april | may | june | july | 
august | september | october | november | december} <hh>:<mm> { 1 | 2 | 3 | 4 | last} 
{sunday | monday | tuesday | wednesday | thursday | friday | saturday} {january | 
february | march | april | may | june | july | august | september | october | november | 
december} <hh>:<mm>[<offset>] 
The parameter {1 | 2 | 3 | 4 | last} specifies the week of the month. 
For both schedule types, <offset> specifies (in minutes) the time to add at daylight saving time start, or 
subtract at daylight saving time end. Its range is 1–1440. 
10. Timing and Synchronization 
 To delete daylight saving time scheduling: 
• 
Navigate to the config>system>date-time level and enter: 
no summer-time 
Examples 
 To schedule daylight saving time starting March 27 2017 at 1:00 and ending October 27 2017 at 
2:00: 
config>system>date-time#summer-time date march 27 2017 01:00 october 27 2017 12:59 
 To schedule daylight saving time starting on the first Friday in March at 2:00 and ending on the 
last Sunday in October at 3:00: 
configure system date-and-time 
summer-time recurring 1 friday march 02:00 last sunday october 03:00 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Schedule with this 
name already 
configured 
You tried to create a new schedule 
with a name that is used by an existing 
schedule. 
Specify a name that is not being 
used by an existing schedule. 
Summer-time already 
configured 
You entered the summer-time 
command to configure daylight saving 
time, but the scheduling of 
summer-time has already been 
configured. 
Delete the existing summer-time 
configuration; and then re-enter 
the summer-time command. 
Recurring 
summer-time start 
and end must be on 
different months 
You tried to configure summer-time 
start and end in the same month. 
Enter the summer-time command 
with summer-time start and end in 
different months. 
Summer-time cannot 
end before it starts 
You entered the summer-time 
command (with one-shot schedule 
type) with summer-time end time 
earlier than summer-time start.  
Enter the summer-time command 
with summer-time start time 
earlier than the end time. 
 
10. Timing and Synchronization 
Viewing Scheduled Daylight Saving Time 
 To view daylight saving time: 
• 
Navigate to the config>system>date-time level and enter: 
show summer-time 
config>system>date-time# show summer-time 
Current date:   13 August 2019     10:30:51   +00:00 
 
Start (Date) : 29 March 2019 02:00 
End   (Date) : 27 October 2019 02:00 
Offset       : 60 
For details and an example on how to view in your device scheduled data, including daylight saving time, 
refer to Viewing Scheduling Information. 
 
 
 
 