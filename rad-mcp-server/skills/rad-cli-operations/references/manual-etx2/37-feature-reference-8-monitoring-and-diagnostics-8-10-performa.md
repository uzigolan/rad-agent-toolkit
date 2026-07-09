# Feature Reference – 8 Monitoring and Diagnostics – 8.10 Performance Management

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1541–1556.*


## Examples  *(p.1541)*


## Applicability and Scaling  *(p.1541)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Examples 
In the following example, all the inbound traffic into port 0/3 and outbound traffic from port 0/4, is 
mirrored to Ethernet port 0/1. 
ETX-2i>configure mirroring-session 1 
ETX-2i>config>mirroring-session(1)# source port ethernet 0/3 rx 
ETX-2i>config>mirroring-session(1)# source port ethernet 0/4 tx 
ETX-2i>config>mirroring-session(1)# destination ethernet 0/1 
ETX-2i>config>mirroring-session(1)# no shutdown 
exit               
In the following example, all the inbound traffic into and outbound traffic from port 0/4, is mirrored to 
Ethernet port 0/2. 
ETX-2i>configure mirroring-session 2 
ETX-2i>config>mirroring-session(2)# source port ethernet 0/4 tx-rx 
ETX-2i>config>mirroring-session(2)# destination ethernet 0/2 
ETX-2i>config>mirroring-session(2)# no shutdown 
exit               
8.10 Performance Management 
ETX‑2i supports collection of performance management (PM) statistics for analyzing the device’s service 
quality. The device periodically collects PM statistics into a pm-0 binary file for retrieval and analysis by 
RADview and for display in the RADview PM portal (refer to the RADview System User Manual for 
further details on the PM portal).  
The PM collection process can be globally enabled (the default) or disabled for the entire device. In 
addition, the statistics collection can be enabled for all entities of a specific type, or for specific entities, 
enabling collection of necessary data only. 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products and to PMC in ETX-2i, with the following condition: 
• 
Scripts containing port numbers may have to be edited according to the product port 
numbering. 

## Functional Description  *(p.1542)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Functional Description 
PM Statistics Collection 
PM statistics collection is configured for the device, entity type, and specific entities. PM statistics are 
collected for the following types of entities: 
• 
Ethernet ports 
• 
Flows 
• 
OAM CFM services 
• 
OAM CFM destination NEs 
• 
System parameters: memory usage and CPU utilization 
If PM statistics collection is disabled for a particular entity type, then no PM statistics collection is done 
for any entity of that type, except those for which PM statistics collection is enabled. 
When PM statistics collection is enabled for all entities of the same type, then when a new entity of that 
type is added, the device automatically starts collecting PM statistics for it as soon as PM statistics 
maintenance (if applicable) is enabled for the entity. 
Note 
If you are using the RADview PM Portal, it is recommended to enable PM 
statistics collection for all relevant entities. See Examples for a script that you 
can use for this purpose. 
PM statistics collection is performed at user-configurable intervals of one second to 15 minutes. A 
different interval can be configured for each entity type, and for specific entities. 
If different intervals are scheduled for collection at the same time, ETX‑2i collects the PM statistics 
starting with the interval that has the highest frequency and ending with the interval that has the lowest 
frequency. If ETX‑2i has not finished collecting the statistics for an interval when the scheduled time for 
another interval arrives, the following action is taken according to whether the new interval is the next 
interval, or an interval with higher frequency: 
• 
If it is the next interval, then the next interval is canceled, and a PM record indicating the 
cancellation is inserted in the PM data. 
• 
If it is an interval with higher frequency, then ETX‑2i collects the higher frequency interval 
statistics and then resumes collecting the lower frequency interval statistics. The PM data is 
retrieved from ETX‑2i by RADview via TFTP or SFTP. After PM data is retrieved, ETX‑2i deletes 
the file and opens a new one for further data. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
The PM file includes the following information: buffer (kernel) memory utilization and TCA, CPU 
utilization, memory utilization, flash memory utilization, and device uptime. 
PM File Conversion to CSV 
ETX‑2i collects and saves PM statistics as raw data into a pm-0 binary file that is compact (up to 5 Mega) 
but complex and not comprehensible to humans and other management systems. ETX‑2i supports the 
pm-csv command to convert the pm-0 binary contents to CSV format and send as a pm-csv file (larger 
but more understandable than the binary file,) to an external server. Users can open the CSV file using 
Excel or similar software; also, management systems other than RADview can use the data.  
In a PM file in CSV format, the default CSV delimiter is the comma character, and newline is CR and LF. 
Using the pm-csv command in the reporting level (see table below), you can change the default values, 
to the following: 
• 
delimiter – any ASCII character 
• 
newline  
 
CR-LF - for Windows 
 
CR – for Apple 
 
LF – for Linux 
Note 
• 
Both pm-0 and pm-csv are listed in the dir command and marked in-use in 
the file system. This means that they cannot be directly overridden or 
deleted. 
• 
Users can copy the files or configure periodic push of them. 
• 
The device deletes the file when PM is disabled or after a file has been 
retrieved. 
Performance Monitoring CSV File Structure 
This section describes the PM CSV file, used by management systems other than RADview. (RADview 
uses the default binary file, which is more compact but not trivial to parse.) 
• 
The CSV file fields are separated by the configured delimiter and newline characters, making 
them more comprehensible. (In the diagrams below, each field is in a table cell.) 
• 
The pattern is written first, followed by an explanation of its fields. Fields to be replaced with 
actual values are enclosed in <> (<> is not written in the file). 
• 
The fields are similar to those of the binary file; however, some are simplified, and unnecessary 
ones are omitted. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
The structure of the PM CSV file is as follows: 
• 
PM Header 
• 
PM records 
PM Header 
The PM CSV file starts with the following header: 
Version 1 Device ID: <device id> Reboot Text Configuration Card Switchover 
 
 
 
 
 
The following are the field descriptions: 
<device-id> 
Device primary MAC address (used for management and as zero touch UUID), 
formatted 010203040506 
Reboot 
Printed in the first file following a device reboot. 
Text Configuration 
Printed in the first file following a device reboot if the device has loaded a text 
configuration (rather than binary configuration). 
Card Switchover 
Printed if the device has more than one main card, and the file opened after 
an unplanned main card switchover. 
 
Note 
• 
Unlike the binary file, the CSV file does not have checksum. Instead, the 
file ends with: End of File. 
• 
The system uptime flag, and the base and finish time fields of the binary 
file are omitted, as times in the CSV file are written before every sample 
(see the first header under PM Records below). 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
PM Records 
The file header is followed by PM records. They can contain PM data or special information. 
A PM data record comprises: 
• 
Time header 
• 
Table fields header 
• 
Time change record, when relevant 
• 
Interval state record 
• 
Canceled interval record, when relevant 
Each PM data record starts with the following Time header: 
Table 
Name 
Entry 
OID 
Date And Time 
(Local) 
Date And Time 
(UTC) 
System Uptime 
(Seconds) 
Current End 
<name> 
<oid> 
<local date and 
time> 
<utc date and 
time> 
<system uptime> 
Instance 
<#> 
 
 
 
 
 
 
The following are the field descriptions: 
<local date and time> 
Device date and time in UTC, formatted yyyy/mm/dd hh:mm:ss 
<utc date and time> 
Device date and time in UTC, formatted yyyy/mm/dd hh:mm:ss 
<system uptime> 
Number of seconds since the last device startup 
Text Configuration 
Printed in the first file following a device reboot if the device has loaded a text 
configuration (rather than binary configuration). 
Current End 
Printed if the record contains the last sample of current counters before they 
are being saved as interval-1 and reset. 
Instance <#> 
Printed if the table has multiple instances, with different SNMP context (as 
some router tables were implemented). The number in the SNMP context is 
printed as <#> in this case. 
A second PM data record header describes the table fields, followed by the values of the entire table. 
<field 1 id> 
<field 2 id> 
… <field n id> 
<field 1 name> <field 2 name> … <field n name> 
ETX-2i Devices 
8. Monitoring and Diagnostics 
<value 1, 1> 
<value 1, 2> 
… <value 1, n> 
<value 2, 1> 
<value 2, 2> 
… <value 2, n> 
… 
… 
… … 
<value m, 1> 
<value m, 2> 
… <value m, n> 
 
 
 
 
Table fields include the table indexes and the collectable objects.  
For fields of the table written in the header, <field id> is the last number of that field OID (combining it 
with the entry OID from the header gives the field OID). Some table indexes are taken from other tables. 
For such indexes, <field id> is the full OID (not just the last number). 
If the time, date, time zone, or daylight-saving time of the device has changed (by configuration or 
dynamic mechanism such as NTP), and if the change is of at least one second, the device does the 
following: 
• 
Recalculates the time of all future intervals to the nearest time that will make them aligned with 
the next round hour. Pending intervals at the time of recalculation might become shorter or 
longer than they should have been. 
• 
Inserts the following special PM record before continuing with regular records of PM data: 
Time Changed 
Time Zone Changed 
Daylight Saving Time Changed 
Time Delta (Seconds): <delta> 
New Time (Local): <local> 
New Time (UTC): <utc> 
 
 
 
The following are the field descriptions: 
<delta> 
New time minus old time, in hundredth of seconds (if the time moves 
backwards it is preceded by a - sign) 
<local> 
Device local date and time, formatted yyyy/mm/dd hh:mm:ss ±z 
<utc> 
Device date and time in UTC, formatted yyyy/mm/dd hh:mm:ss 
 
Note 
One or more of the above is printed, depending on the change (note that Time 
Changed is printed for both time and date changes). 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Before an interval starts, and when an interval ends, ETX‑2i inserts the following interval state record.  
Interval State: <state> Interval Length (Seconds): <length> 
 
 
The following are the field descriptions: 
<state> 
About To Begin or Just Ended 
<length> 
Interval length in seconds 
At each interval, the ETX‑2i collects all counters configured to be read at that interval, giving priority to 
higher frequency intervals.  
If ETX‑2i has not finished gathering information of an interval while the time of another interval, of 
higher frequency is reached, the device suspends gathering for the lower frequency interval, gathers the 
counters of the higher frequency interval, and then resumes gathering for the lower frequency interval. 
For example, if counter A is configured to be collected every two minutes and counter B every four 
minutes, both counters are collected every four minutes (A being additionally collected between the 
four-minute intervals). At the four-minute intervals, A is always collected before B. 
If ETX‑2i cannot finish collecting all the counters of an interval before the same interval arrives again, the 
device does the following: 
• 
Cancels the latter interval. 
• 
Inserts a special PM record before continuing with PM data records. 
Cancelled Interval Interval Length: <length> 
 
 
The following is the field description: 
<length> 
Interval length in seconds 
Automatic PM File Upload  
ETX‑2i supports the pm-file-push command to automatically upload (push) the binary or CSV PM file at 
periodic intervals, instead of manually uploading the file (using the copy command). This command 
requires setting the IP address of the server that receives the pushed file, file format (binary or CSV), file 
transfer protocol (TFTP or SFTP), and push interval.  

## Factory Defaults  *(p.1548)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
The device exports the PM file every push interval (configured) plus or minus a random number of 0-30 
seconds, which is automatically generated by the SW, to avoid a storm of many devices simultaneously 
trying to export files.  
• 
If the push time arrives and there is no data to send, the device waits for the next interval 
without taking any action. 
• 
If the push time arrives while the device is in the middle of collecting, it finishes the record it has 
begun collecting, and then closes the file and copies it. 
If an export fails, the device does the following: 
• 
Generates the download_end event. 
• 
Continues saving PM data to the original file. 
As long as the next push time has not arrived, you can try copying the file again after waiting a minute 
(with filename reflecting the new time), until succeeding. The event is sent, if needed, after each failure.  
Once the PM file (binary or CSV) is uploaded, the device deletes its contents and begins filling it with 
new PM data. 
Factory Defaults 
Command 
Level under config 
Default  
Remarks 
pm 
reporting 
pm 
PM statistics collection in device is globally 
enabled by default. 
pm-collection  
Specific entity level 
Disabled 
PM statistics collection for specific entities is not 
explicitly configured by default; therefore, it is 
disabled until statistics collection is enabled for 
the entity type or entity.  
pm-collection dest-ne reporting 
Disabled 
PM statistics collection for OAM CFM 
destination NEs is not explicitly configured by 
default; therefore, it is disabled. 
pm-collection eth 
reporting 
Disabled 
PM statistics collection for Ethernet ports is not 
explicitly configured by default; therefore, it is 
disabled.  
pm-collection flow 
reporting 
Disabled 
PM statistics collection for flows is not explicitly 
configured by default; therefore, it is disabled. 

## Configuring Performance Management  *(p.1549)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Command 
Level under config 
Default  
Remarks 
pm-collection 
oam-cfm-service 
reporting 
Disabled 
PM statistics collection for OAM CFM services is 
not explicitly configured by default; therefore, it 
is disabled. 
pm-collection system 
reporting 
Disabled 
PM statistics collection for memory usage and 
CPU utilization is not explicitly configured by 
default; therefore, it is disabled. 
pm-csv 
reporting 
Disabled 
Saving of PM file in CSV format is disabled by 
default. 
pm-file-push 
reporting 
Disabled 
Export of PM file at fixed intervals is disabled by 
default. 
 
 
Configuring Performance Management 
You can configure PM statistics collection for the entire device via the pm command, and for entity 
types via the pm-collection command, in the reporting level. For specific entities, you can configure PM 
statistics collection via pm-collection, in the specific entity level.  
You can configure the device to record statistics at fixed intervals using the pm-collection interval 
<seconds> command or at the close of an interval using the pm-collection on-interval-close command. 
For parameters that are not zeroed regularly, it is recommended to record statistics at fixed intervals. 
For parameters zeroed at fixed intervals (interval statistics), it is recommended to record statistics 
whenever an interval is about to expire, i.e., right before the parameters are zeroed, in order to avoid 
losing data. This option is available for interval statistics only. The interval parameter for the 
pm-collection command can range from 1 to 900 seconds (15 minutes); however, the value must divide 
evenly into 3600. Different intervals can be specified for an entity type and for specific entities of that 
type, up to a supported maximum number of intervals. For example, if the PM statistics collection 
interval for all flows is configured to 15 minutes, and the PM statistics collection interval for flow-1 is 
configured to 1 minute, the data displayed in the RADview PM portal shows flow data for every 
15 minutes, and flow-1 data for every minute. You can also collect PM statistics on interval close.  
The following shows the PM statistics collection configuration tasks, and their corresponding commands, 
as well as the level of each command. It also shows the commands for saving the PM binary file in CSV 
format and automatically exporting it at fixed intervals. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Level under config 
Command 
Comments 
Enabling PM statistics 
collection for a specific 
flow  
flows > flow(<flow-name>) 
pm-collection  
{ interval <seconds> | 
on-interval-close } 
PM collection can be 
enabled at a defined 
interval or before an 
interval expires.  
Enter no pm-collection to 
disable PM statistics 
collection for the flow. 
Enabling PM statistics 
collection for a specific 
OAM CFM service  
oam > cfm > md(<md-id>) > 
ma(<ma-id>) > mep(<mep-
id>) > service(<service-id>) 
pm-collection  
{ interval <seconds> | 
on-interval-close } 
PM collection can be 
enabled at a defined 
interval or before an 
interval expires.  
Enter no pm-collection to 
disable PM statistics 
collection for the service. 
Enabling PM statistics 
collection for a specific 
OAM CFM destination 
NE  
oam > cfm > md(<md-id>) > 
ma(<ma-id>) > mep(<mep-
id>) > service(<service-id>) > 
dest-ne(<dest-ne-index>) 
pm-collection  
{ interval <seconds> | 
on-interval-close } 
PM collection can be 
enabled at a defined 
interval or before an 
interval expires.  
Enter no pm-collection to 
disable PM statistics 
collection for the 
destination NE. 
Enabling PM statistics 
collection for a specific 
Ethernet port (other 
than the management 
port)  
port > 
ethernet(<slot>/<port-num>) 
pm-collection  
{ interval <seconds> | 
on-interval-close } 
PM collection can be 
enabled at a defined 
interval or before an 
interval expires.  
Enter no pm-collection to 
disable PM statistics 
collection for the Ethernet 
port. 
Enabling PM statistics 
collection for the 
Ethernet management 
port  
port > mng-eth 
pm-collection  
{ interval <seconds> | 
on-interval-close } 
PM collection can be 
enabled at a defined 
interval or before an 
interval expires.  
Enter no pm-collection to 
disable PM statistics 
collection for the Ethernet 
management port. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Level under config 
Command 
Comments 
Globally enabling PM 
statistics collection for 
device 
reporting 
pm 
Enter no pm to disable all 
PM statistics collection in 
ETX‑2i. 
Note: no pm stops all PM 
collection regardless of 
other PM configuration; 
however, it does not 
change other 
configurations.  
It deletes any collected PM 
data and PM files, as well. 
Enabling PM statistics 
collection for OAM CFM 
destination NEs 
reporting 
pm-collection dest-ne  
{ interval <seconds> | 
on-interval-close } 
PM collection can be 
enabled at a defined 
interval or before an 
interval expires.  
Enter no pm-collection 
dest-ne to disable PM 
statistics collection for all 
OAM CFM destination NEs. 
Enabling PM statistics 
collection for Ethernet 
ports  
reporting 
pm-collection eth  
{ interval <seconds> | 
on-interval-close } 
PM collection can be 
enabled at a defined 
interval or before an 
interval expires.  
Enter no pm-collection eth 
to disable PM statistics 
collection for Ethernet 
ports. 
Enabling PM statistics 
collection for flows  
reporting 
pm-collection flow  
{ interval <seconds> | 
on-interval-close } 
PM collection can be 
enabled at a defined 
interval or before an 
interval expires.  
Enter no pm-collection 
flow to disable PM 
statistics collection for 
flows. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Level under config 
Command 
Comments 
Enabling PM statistics 
collection for OAM CFM 
services 
reporting 
pm-collection 
oam-cfm-service  
{ interval <seconds> | 
on-interval-close } 
PM collection can be 
enabled at a defined 
interval or before an 
interval expires.  
Enter no pm-collection 
oam-cfm-service to disable 
PM statistics collection for 
OAM CFM services. 
Enabling PM statistics 
collection for system 
parameters 
reporting 
pm-collection system  
{ interval <seconds> | 
on-interval-close } 
PM collection can be 
enabled at a defined 
interval or before an 
interval expires.  
Enter no pm-collection 
system to disable PM 
statistics collection for 
system parameters. 
Saving PM binary file in 
CSV format 
reporting 
pm-csv [delimiter 
<character>] [newline 
<newline-values>] 
character – CSV delimiter 
to replace comma (the 
default) 
Possible values: ASCII 
character 
newline-values – CSV value 
to indicate new line 
Possible values: 
• cr-1f – for Windows 
• cr – for Apple 
• 1f – for LINUX 
Note: Repeating the 
command replaces the 
previous instance. 
Automatically exporting 
PM file at fixed intervals 
 
pm-file-push server  
<ip-address> file-type 
{bin | csv} protocol 
{tftp | sftp username 
<username> 
password <password> 
[hash]} [port <port>] 
[directory <path>] 
push-interval 
<minutes> 
ip-address – IP address of 
server where PM file is to 
be pushed 
username – SFTP 
username;  
Possible values: 1–32-
character string 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Level under config 
Command 
Comments 
no pm-file-push 
password – SFTP password 
Possible values: 1–32-
character string 
port – file transfer protocol 
port (optional) 
Possible values: 1-65535 
Default: 22 for SFTP; 69 for 
TFTP 
directory – directory where 
PM files are to be saved 
(optional) 
Possible values: 1–64-
character string; string 
cannot end with \ 
push-interval – time in 
minutes between 
consecutive file pushes 
Possible values: 1-10080 
Note:  
• A device can send a 
single file format to a 
single server. If the 
command is repeated, 
the device rejects it and 
prints: PM file push is 
already configured. 
• Command sets a 
hashed password, 
regardless of whether 
you specify hash. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Level under config 
Command 
Comments 
• It is recommended to 
set push-interval to less 
than the number of 
minutes it takes for the 
pm-o file to fill up to its 
maximum capacity (5 
Mega). Otherwise, 
collected PM data will 
be lost. (You can time 
how long it takes the 
PM file to reach the size 
displayed in the output 
of the dir command.) 
• To avoid a storm of 
many devices trying to 
simultaneously export 
files, the system 
automatically adds to 
or removes from the 
configured push-
interval value, a 
random number 
between 0-30 seconds, 
and uses this as the 
effective push interval. 
• You cannot manually 
upload a file using the 
copy command, if the 
pm-file-push command 
is configured. 
 
Note 
PM statistics are collected for entities for which PM statistics collection is 
specifically enabled in the entity level via pm-collection, even if PM statistics 
collection for the entity type is disabled. 
 
 

## Viewing Performance Management Configuration  *(p.1555)*


## Examples  *(p.1555)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing Performance Management Configuration 
You can use the info detail command to view the performance management configuration. 
 To view the performance management configuration for the device and for entity types: 
1. Navigate to configure reporting. 
2. Enter info detail | include pm to view PM-related commands in the configuration. 
 To view the performance management configuration for specific entities: 
1. Navigate to the specific entity level. 
2. Enter info detail | include pm to view PM-related commands in the configuration. 
Examples 
 To enable PM for all relevant entities in ETX‑2i: 
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
#**** Enable PM for OAM CFM dest NEs, collection interval=5 min 
  pm-collection dest-ne interval 300 
exit all 
save 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure the following PM: 
• 
PM statistics collection enabled for device. 
• 
PM statistics collection enabled for Ethernet ports, every two minutes. 
• 
PM statistics collection enabled for flows, every five minutes. 
• 
PM statistics collection for Ethernet port 0/3 configured to every minute. 
• 
PM statistics collection enabled for OAM CFM services, every 15 minutes. 
• 
PM statistics collection enabled for OAM CFM dest NEs, every 15 minutes. 
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
#**** Enable PM for OAM CFM dest NEs, collection interval=15 min 
  pm-collection dest-ne interval 900 
exit all 
 
 
#**** Configure PM statistics collection interval for Eth port 0/3, to 1 min 
configure port ethernet 0/3 
  pm-collection interval 60 
exit all 
save 
 To display PM configuration from the example above: 
ETX‑2i# configure reporting 
ETX‑2i>config>reporting# info detail | include pm 
    pm 
    pm-collection eth interval 120 
    pm-collection flow interval 300 
    pm-collection oam-cfm-service interval 900 
    pm-collection dest-ne interval 900 
ETX‑2i>config>reporting# exit all 
 
ETX‑2i# configure port ethernet 0/3 
ETX‑2i>config>port>eth(0/3)# info detail | include pm 
    pm-collection interval 60 