# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.12 Performance Monitoring

*Manual `MiNID_ver_2_6_mn.pdf`, pages 372–373.*


## Alarm, Event and Trap Lists  *(p.372)*


## Applicability and Scaling  *(p.372)*


## Benefits  *(p.372)*

11. Monitoring and Diagnostics
>config>report#
Alarm and Event Lists 
You can view the full lists of alarms and events supported by , along with the traps corresponding to 
each alarm or event.  
 To view the alarms table: 
•
Double-click the paperclip image on the following line.
 To view the events table: 
•
Double-click the paperclip image on the following line.
11.12 Performance Monitoring 
 maintains performance management (PM) statistics that are collected into a file periodically, for 
retrieval by RADview, for display in the RADview PM portal (refer to the RADview System User’s Manual 
for further details on the PM portal). The PM file can also be retrieved by a third-party network 
management system.  
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Benefits 
The PM data is useful for analyzing  service quality. The flexible statistics collection allows only the 
necessary data to be collected. 

## Functional Description  *(p.373)*


## Factory Defaults  *(p.373)*


## Configuring Performance Monitoring  *(p.373)*

11. Monitoring and Diagnostics
Functional Description 
PM statistics collection is configured globally for MiNID. When it is enabled,  collects PM data. When it is 
disabled,  deletes any PM data previously collected and stops collecting PM data. 
MiNID  stores PM data at user-configurable intervals (1, 5, 10, or 15 minutes). Additionally the interval 
for collecting the PM data from  can be configured to 1, 5, 10, or 15 minutes. 
Note 
•
If the PM file reaches 90% capacity,  sends the PM SPACE OVERFLOW
event; if PM data cannot be saved due to insufficient space,  stops
collecting PM data and sends the PM PROCESS DISABLED event
•
If performance monitoring is enabled, ensure that the data is collected by
RADview or a third-party NMS, otherwise one or both of the alarms is
triggered. If it is not possible to collect the data, then disable performance
monitoring.
Factory Defaults 
Parameter 
Default 
Remarks 
pm 
pm 
PM statistics collection in device is 
globally enabled by default 
interval-duration 
15 
PM interval is 15 minutes by 
default 
file-interval-duration 
5 
PM file is collected every 5 minutes 
by default 
Configuring Performance Monitoring 
 To configure PM collection: 
Do one of the following: 
•
In the web interface:
a.
Go to Configuration > System > Performance Monitoring.
b.
Set PM Mode to Enable or Disable.