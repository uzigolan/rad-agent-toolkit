# 9 Timing and Synchronization

*Manual `MiNID_ver_2_6_mn.pdf`, pages 217–225.*


## 9.1 Network Time Protocol (NTP)  *(p.217)*

9.1 Network Time Protocol (NTP) 
Network Time Protocol (NTP) is a networking protocol for clock synchronization between computer 
systems over packet-switched, variable-latency data networks. 
Factory Defaults 
The default configuration for NTP parameters: 
• 
No NTP servers defined 
• 
Poll interval set “fast mode” 
• 
Date-format “yyyy-mm-dd” 
• 
No “summer time” 
Configuring NTP 
 To configure NTP in the web interface: 
1. Navigate to Configuration > System > Date and Time. 
9. Timing and Synchronization 
 
  
 
 
 Configuration>System>Date and Time 
  
 
 
 NTP 
 
 
  
 
 
 Date Format 
yyyy-mm-dd 
 
 Date 
2016-3-29 
 
 Time 
12:02:46 
 
 Zone (utc) 
00:00 
 
 Summer Time 
Type 
No summer time 
 
  
 
 
 Apply 
 
 
  
 
 
1. Fill in the fields according to the tasks listed below: 
 
Date Format: Available formats (yyyy-mm-dd | dd-mm-yyyy | mm-dd-yyyy | yyyy-dd-mm) 
 
Date: Current date 
 
Time: Current time (hh:mm[:ss]) 
 
Zone: Desired time zone (Allowed range of values: 
 -12:00 to +12:00, in 30-minute increments) 
 
Summer-Time Type:  
 
No summer time – No summer time differences 
 
Recurring – Define a scheme for the range of summer time dates, including the Offset in 
minutes 
 
Date – Define a specific date and time, including the Offset in minutes 
2. Click <Apply> to save changes. 
3. Click NTP. 
9. Timing and Synchronization 
 
  
 
 
 Configuration>System>Date and Time>Config NTP 
  
 
 
 Add New NTP Server 
 
 
  
 
 
 Poll-Interval 
Fast-Mode 
 
  
 
 
 Apply 
 
 
  
 
 
 NTP Server 
 
 
  
 
 
1. Select the desired poll interval and click <Apply>. 
2. Click Add New NTP Server. 
 
  
 
 
 Configuration>System>Date and Time>NTP> Add NTP Server 
  
 
 
 Server Index 
 
 
 Admin Status 
 
Enable/Disable 
 Server IP Address 
 
 
 UDP Port Number 
 
 
  
 
 
 Apply 
 
 
  
 
 
3. Fill in the fields according to the tasks listed below: 
 
Server Index: The index is automatically selected 
 
Admin Status: Enable/Disable 
 
Server IP Address: NTP server’s IP address 
 
UDP Port Number: The port used by the NTP server 
4. Click <Apply> to save the configuration. 
9. Timing and Synchronization 
 To display NTP Server Information: 
• 
Navigate to Monitoring > System > NTP. 
 
 
 
 
 
 
Monitoring>System> NTP  
 
 
 
 
NTP 
Server 
Address 
Type 
UDP Port   TStamp DateTime (UTC)  Stratum  
Received 
 
 
 
Query-Server 
 
 
 
 
 
 
 
 
All existing NTP servers and information are displayed. 
Setting the Date and Time 
 To set the system date and time in the CLI: 
1. Navigate to configure system date-and-time.  
The config>system>date-time# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying the desired 
date format 
date-format {yyyy-mm-dd | dd-mm-yyyy | 
mm-dd-yyyy | yyyy-dd-mm} 
 
Defining the date 
date <date> 
Date is according to the 
configured date format 
Defining the time zone 
relative to Coordinated 
Universal Time (UTC) 
zone utc [<[{+|-}]<hh>[:<mm>]>] 
Allowed range of values: 
 -12:00 to +13:00, in 1-hour 
increments 
Defining the time 
time <hh:mm[:ss]> 
 
9. Timing and Synchronization 
Displaying the Date and Time 
 To display the date and time in the CLI: 
• 
From the system context (config>system), enter: 
show time 
Setting NTP Parameters 
 To configure NTP parameters in the CLI: 
1. Navigate to configure system date-and-time ntp. 
The config>system>date-time>ntp# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Setting polling interval (in 
minutes) for NTP requests 
poll-interval <minutes>  
Allowed range is 8–131072 
Defining and configuring NTP 
servers  
server <server-id> 
 
Displaying NTP status 
show status 
 
Defining NTP Servers  
 To define an NTP server in the CLI: 
1. Navigate to config system date-and-time ntp. 
The config>system>date-time>ntp# prompt is displayed. 
2. Type server <server-id> to define an NTP server with ID <server-id>. 
The following prompt is displayed: config>system>date-time>ntp>server(<server-id>)$. . 
3. Configure the NTP server parameters as needed, as described in Setting NTP Server Parameters. 
Setting NTP Server Parameters 
 To configure NTP server parameters in the CLI: 
1. Navigate to config system date-and-time ntp. 
9. Timing and Synchronization 
The config>system>date-time>ntp# prompt is displayed. 
2. Type server <server-id> to select the NTP server to configure. 
The following prompt is displayed: config>system>date-time>ntp>server(<server-id>)# 
3. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Setting the IP address of the 
server 
address <IP-address> 
 
Setting UDP port for NTP 
requests, to a specific UDP port or 
to default UDP port (123) 
udp port <udp-port> 
• Allowed value 123 or 
• Allowed range of 1024–
65535 
Enabling and defining summer 
time parameters 
summer time <recurring/date> 
• Recurring- Define dates for 
a recurring summer time 
• Date- Manually define 
summer time dates 
Administratively enabling server 
no shutdown 
Using shutdown disables the 
server 
Sending query to server and 
displaying result 
query-server 
 
Examples 
 To set the date and time: 
• 
Format = mm-dd-yyyy 
• 
Date = May 17, 2016 
• 
Time = 5:40pm 
• 
Zone = GMT –4 hours and 30 minutes. 
exit all 
configure system date-and-time 
  date-format mm-dd-yyyy 
  date 05-17-2016 
  time 17:40 
  zone utc -04:00 
9. Timing and Synchronization 
 To define NTP server: 
• 
Server ID = 1 
• 
IP address = 192.1.1.1 
• 
Administratively enabled. 
exit all 
configure system date-and-time ntp 
  server 1 
    address 192.1.1.1 
    no shutdown 
 To display server information: 
# configure system date-and-time ntp server 1 
>config>system>date-time>ntp>server(1)# query-server 
Query Server Reply 
----------------------------------------------------------------------------- 
Server  : 192.1.1.1       UDP   : 123      
Date    : 00-00-0      Time  : 00:00:00 
Stratum : 0                                
>config>system>date-time>ntp>server(1)# exit 
>config>system>date-time>ntp# show status 
System Uptime : 006 Days 116:19:55                                  
System Time   : 2016-05-04                 13:01:09   
 
 
NTP Server  Type    UDP Port Tstap Date Time(UTC)  Stratum Received        
192.1.1.1   Enable  123      00-00-0000 00:00:00   1       000 Days 00:00:25    
 
 

## 9.2 Sync-E Clock Source  *(p.224)*

9. Timing and Synchronization 
9.2 Sync-E Clock Source  
 SFP sleeve and SFP unit can transparently transfer the Sync-E clock and ESSM packets between its ports. 
You can define whether to transfer from the MSA port or the SFP port. 
Applicability and Scaling 
Copper SFPs do not support Sync-E transfer, except for SFP-ToC, which supports only the direction SFP 
to MSA. 
Standards Compliance 
ITU-T G.8262 
Benefits 
You have the flexibility to define which port transfers the Sync-E clock. 
Functional Description 
You can configure the Sync-E clock source as the MSA port (to transfer the Sync-E clock from the MSA 
port to the SFP port), or the SFP port (to transfer the Sync-E clock from the SFP port to the MSA port). 
If a physical fault (LOS) occurs on the clock source port,  automatically sets the clock source to the 
system internal oscillator. 
When the port fault is cleared, the clock source returns to the user-configured clock source.  
 
Note 
Port status polling rate is 400 ms, therefore it can take up to 400 ms for the 
clock source to change back to the configured source. 
Factory Defaults 
By default,  transfers the Sync-E clock from the MSA port to the SFP port. 
9. Timing and Synchronization 
Configuring the Sync-E Clock Source 
 To define the Sync-E clock source: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Clock, select SFP/Port 2 to transfer timing 
packets from the SFP/Port 2 port to the MSA/Port 1 port; or MSA/Port 1 to transfer timing 
packets from the MSA/Port 1 port to the SFP/Port 2 port; then click <Apply> to implement the 
changes, and then click <Save Configuration>. 
 
MiNID 
  
 
 
 Configuration>System>Clock 
  
 
 
 Sync-E Clock 
Source 
 
MSA/Port 1 
  
 
 
 
• 
In the CLI, navigate to the configure system clock context, and do one of the following: 
 
To transfer timing packets from the SFP/Port 2 port to the MSA/Port 1 port, enter: 
sync-e-src sfp 
 
To transfer timing packets from the MSA/Port 1 port to the SFP/Port 2 port, enter: 
sync-e-src msa 
 
 