# 5 Cards and Ports – 5.16 Management Ethernet Port – Controlled Forwarding

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 342–344.*


## Benefits  *(p.342)*


## Configuring the Out-Of-Band Management Port  *(p.342)*

5. Cards and Ports 
Benefits 
Configuring a dedicated management port eliminates the possibility of management traffic reducing 
bandwidth and/or causing interruptions in the traffic flow caused by the management. 
Configuring the Out-Of-Band Management Port 
The following parameters can be configured for the management Ethernet port: 
• 
Port name 
• 
Administrative status. 
 To configure the Management Ethernet port parameters: 
1. Navigate to configure port mng-ethernet <slot>/<port> to select the Ethernet port to 
configure. 
The config>port>mng-ethernet>(<slot>/<port>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning short description to port 
name <string> 
Using no before name removes the name 
Administratively enabling port 
no shutdown   
Using shutdown disables the port 
Configuring collection of 
performance management statistics 
for the port, that are presented via 
the RADview Performance 
Management portal 
 
pm-collection interval <seconds> 
Note: You can enable PM statistics collection 
for all Ethernet ports rather than enabling it 
for individual ports. In addition to enabling 
PM statistics collection for the ports, it must 
be enabled for the device. Refer to the 
Performance Management section in the 
Monitoring and Diagnostics chapter for 
details. 
5.16 Management Ethernet Port – Controlled Forwarding  
A set of special parameters allows the network manager (NoC operator) to control the usage of the ETH 
OOB MNG by the personnel of a remote substation. These parameters lock the management port from 

## Benefits  *(p.343)*


## Functional Description  *(p.343)*

5. Cards and Ports 
the remote users and allow its opening only for a specific time interval. During this management 
timeout, data forwarding is allowed and the personnel will be able to manage the port. 
Benefits 
Configuring a management activity timeout assures more security due to controlled use of the 
Megaplex-4 host management port. 
Functional Description 
By default the management port at the remote site is disabled. Via remote access from the NoC, the 
network manager sets the port to be active for a configurable duration.  
Since the command is on the system level, OOB ports of both CL modules are configured identically.  
Unless configured and saved otherwise, after power up the port returns to “enable”.    
In case the timeout is activated and OOB cable is not connected the timer will start only after the OOB 
cable is reconnected. This function is needed to simplify the synchronization between the substation 
personnel and the network manager. 
CL Activity change or reconnecting mng-ethernet cable stops the timer and a new command is needed 
to start the session again. 
The flow chart below describes in a single diagram all events involved in management timeout 
activation. 

## Configuring the Out-Of-Band Management Port Controlled Forwarding  *(p.344)*

5. Cards and Ports 
 
Configuring the Out-Of-Band Management Port Controlled Forwarding 
 To configure the Management Ethernet port parameters: 
1. Navigate to config>mngmnt#. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Enable traffic forwarding between 
the mng-ethernet port and the 
remote sub-station user 
enable-mng-ethernet-traffic 
no enable-mng-ethernet-traffic command 
disables traffic forwarding (default state) 
This activation/deactivation command does 
not require commit command. 