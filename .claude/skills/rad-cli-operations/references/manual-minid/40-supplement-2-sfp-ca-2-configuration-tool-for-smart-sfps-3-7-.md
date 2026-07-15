# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 3.7 Web-Based Configuration

*Manual `MiNID_ver_2_6_mn.pdf`, pages 72–84.*


## Using Scripts  *(p.72)*


## Logging in  *(p.72)*

3. Operation 
The next example shows a complete command to which a parameter could be appended. It also shows 
how a string that is a complete command is executed by pressing ”?”. 
MiNID>config>oam>cfm>md(1)>ma(1)>mep(1)# vlan 100? 
- vlan <vlan> [p-bit <p-bit>] [tag-ether-type <ether-tag>] 
Using Scripts 
CLI commands can be gathered into text files. They may be created using a text editor, by recording the 
user commands or by saving the current configuration. 
These files can be configuration files or scripts. Configuration files have specific names and contain CLI 
commands that MiNID can use to replace the current configuration, while scripts contain CLI commands 
that add to the current configuration. Configuration files can be imported from and exported to RAD 
devices via file transfer protocols. 
For more information on configuration files, refer to the description in the Operation chapter. 
In order to execute a CLI script, you have to copy/paste it to the CLI terminal, or send it to MiNID via the 
RADview Jobs mechanism, CLI script option. 
3.7 Web-Based Configuration 
Logging in 
You can configure and manage MiNID locally or remotely using its web interface. Supported browsers 
are the following: 
• 
Internet Explorer 10 or above 
• 
Google Chrome 
 
Note 
To prevent configuration errors, flush the browser’s cache whenever you 
return to the same screen. 
 If you have trouble with the web interface: 
• 
Enable scripts. 
3. Operation 
• 
Make sure that local and organizational firewalls allow access to the destination IP address. 
• 
Disable pop-up blocking software, such as Google Popup Blocker. You may also have to 
configure spyware and adware protecting software to accept traffic from/to the destination IP 
address. 
 To log into the  via the web interface: 
1. In the web browser, navigate to the  IP address (see Router Interface for instructions on setting 
the IP address). 
The MiNID login prompt appears. 
 
MiNID SFP Sleeve Login 

## Using the Web Interface  *(p.74)*

3. Operation 
 
MiNID SFP Login 
 To switch languages: 
1. Click the desired language in the top right corner (next to Logout) in the web interface. 
 
Switching the Language of the Web Interface 
Using the Web Interface 
A navigation tree is displayed on the left, as shown below. You can Logout of the interface by clicking 
the <Logout> icon on the top right. 
 
MiNID Main Menu 
3. Operation 
You can display the interface in Chinese by clicking the Chinese language 
 icon on the top right, next 
to the <Logout> icon. When you click this icon, you are logged out of the current interface, and the login 
page is displayed. Log in again to start working in the chosen interface. 
 
Web Interface in Chinese 
Use the tree on the left to navigate to the various menus. Click the right arrow ( ) to expand a subtree, 
or downward arrow (
) to collapse the subtree. You can also click a tree entry to toggle between 
expanding/collapsing the submenu. Tree entries without a  or 
 represent menus that can be opened 
by clicking the entry. The individual menus display information or provide configuration options. For 
example: 
3. Operation 
 
MiNID Web Interface 
If you change a parameter setting and then click <Apply> to save the change in the device, the change is 
saved only in the device running configuration. Therefore any time that you change the device running 
configuration, a <Save Configuration> icon appears under the <Logout> icon. 
 
When you click <Save Configuration>, the device running configuration is copied to the startup 
configuration, and the <Save Configuration> icon disappears. 

## Menu Map  *(p.77)*

3. Operation 
Menu Map 
The main menu options are: 
Inventory: 
View hardware and software information 
Configuration: 
Set MiNID operational parameters 
Monitoring: 
View statuses, logs, and traffic statistics 
Utilities: 
Copy files 
Delete files 
Ping 
The following figures detail the available display and configuration items.  
 
Note 
Some menus or menu items may not be available, depending on 
configuration. 
 
 
 
3. Operation 
Main Menu
Inventory
Configuration
Monitoring
System
Packet Capture
Utilities
Copy
Protocol
SFTP User Name
File 
SFTP Password
5
Fault Propagation
Propagate LOS Signal
Transmit AIS
Set Factory Defaults
Reset Device
Disable Host PHY
Propagate TX Disable Signal
Propagate TX Fault Signal
Name
Description
HW version
CSL
FP Rev
FW Rev
Performance Monitoring
PM Mode
System
Mngmnt MAC Address
Summer time
NTP
OAM
2
SW Rev
BootVer
SW Date/Time
Clock / Date and Time
Sync-E Clock Source
S/N
1
Physical Port
OAM CFM Fault Direction
Board Type
Server IP
Direction
Remote File Name
Delete
Image Type
Local File Name
Source File Name
Destination File Name
PM File Interval Duration
PM Interval Duration
Set User Defaults
Install SW Pack
Image Type
Ping
Router
OAM
QoS
Test
Physical Port
4
Cos Map Profile
Policer Profile
Envelope Profile
L3SAT
Peer Profile
Session Profile
Generator
Management
6
CP Rev
Services MAC Address
System Up Time
DIP Switches Mode
Current date
Events log
System dump file
Syslog
7
3
 
Menu Map (Except Physical Port Monitoring, OAM Monitoring, Router, Physical Port Configuration, OAM 
Configuration, Management, and Syslog) 
3. Operation 
SFP
Operational Status
Statistics
Total Frames
Total Correct Frames
Total Correct Octets
Frames Discarded (FIFO Full)
FCS Errors
Undersize Frames
MSA
Flows Classification
Flows Traffic
Rate (Mbps)
LBM Reflector Octets
Flow Name
Status
Statistics
Unclassified Traffic
Total Frames
Total Bytes
Clear Statistics
Monitoring
Main Menu
1
Physical Port
Ethernet
Total Matched Frames
Total Matched Bytes
Total Matched In-Service MAC Frames
Total Matched In-Service MAC Bytes
Total Matched In-Service L3/L4 Frames
Total Matched In-Service L3/L4 Bytes
Clear Statistics
Total Matched L2CP Frames
Total Matched L2CP Bytes
Oversize Frames
LBM Reflector Frames
Clear Statistics
 
Menu Map – Physical Port Monitoring 
3. Operation 
Link OAM
Monitoring
Main Menu
Status
Operational Status
Administrative Status
Loopback Mode
MAC Address 
OAM Mode 
Variable Retrieval
Link Events
PDU Max Size
Unidirectional Support
Loopback Support
Local and 
Remote
Statistics
Information Messages
Loopback Ctrl
Event Notification
Unsupported Codes
Clear
Tx and 
Rx
CFM / PM
MA Info
MD Level
MA Name
MA Format
Service Name
VLAN ID
Priority
CCM Interval
VLAN Tag Mode
Inner VLAN ID
Inner Priority
Outer VLAN ID
Outer Priority
OAM
2
MEP ID
Ingress Port
CCM Enable
CCM Transmission Mode
Client MD Level
Admin Status
MEP Status
MisMerge
Unexpected MEP
Unexpected MD Level
Unexpected Period
Rx AIS
Remote MEP
Sys Up Time
Last MAC Address Received
Loss Of Continuity
State
AIS Enable
Loopback Status
LBM Sent
Replies in Order
Replies out of Order
MSG Lost/Timeout
MSG Lost/Timeout (%)
Dest Address
Linktrace Status
TTL
Last Egress ID
Relay Action
MAC Address
Last RDI Bit STate
MEP Info
Service Info
Service Priority
Loss Threshold 
DEI Bit Color
Delay Threshold
Delay Var Threshold 
Service Interval
Admin Status
Dest NE Info
Dest NE ID
Remote MEP ID
Loss Measurement Service
Admin Status
Delay Measurement Service
Running Statistics
Statistics
Elapsed Time 
Two-Way Delay
Two-Way Delay Variation
One-Way Delay Variation
Frames Exceed Delay Variation Threshold
Tx Frames Forward/Backward
Dest NE State
Rx Frames Forward/Backward
Frame Loss Ratio Forward/Backward
Available Seconds Forward/Backward
Unavailable Seconds Forward/Backward
Two-Way Delay Bins Measurement
Two-Way Delay Variation Bins Measurem.
One-Way Delay Bins Measurement
Transmitted SLMs
Transmitted DMMs
Received SLRs
Received DMRs
Current Statistics
Statistics
Elapsed Time
Two-Way Delay
Two-Way Delay Variation
One-Way Delay Variation
Frames Exceed Delay Variation Threshold
Tx Frames Forward/Backward
Dest NE State
Rx Frames Forward/Backward
Frame Loss Ratio Forward/Backward
Available Seconds Forward/Backward
Unavailable Seconds Forward/Backward
Two-Way Delay Bins Measurement
Two-Way Delay Variation Bins Measurem.
One-Way Delay Bins Measurement
Transmitted SLMs
Transmitted DMMs
Received SLRs
Received DMRs
Frames Exceed Delay Threshold
Frame Loss Forward/Backward
Frames Exceed Delay Threshold
Frame Loss Forward/Backward
Interval Statistics
Interval Duration
Status
Two-Way Delay
Two-Way Delay Variation
One-Way Delay Variation
Frames Exceed Delay Variation Threshold
Tx Frames Forward/Backward
Interval Number
Rx Frames Forward/Backward
Frame Loss Ratio Forward/Backward
Available Seconds Forward/Backward
Unavailable Seconds Forward/Backward
Delay Bins Measurement
Delay Variation Bins Measurement
One-Way Delay Bins Measurement
Transmitted SLMs
Transmitted DMMs
Received SLRs
Received DMRs
Frames Exceed Delay Threshold
Frame Loss Forward/Backward
Previous
Next
Total Interval Statistics
Statistics
Two-Way Delay Min/Average/Max
Two-Way Delay Variation Min/Aver./Max
One-Way Delay Variation Min/Aver./Max
Frames Exceed Delay Threshold
Tx Frames Forward/Backward
Rx Frames Forward/Backward
Frame Loss Forward/Backward
Available Seconds Forward/Backward
Unavailable Seconds Forward/Backward
Two-Way Delay Bins Measurement
Two-Way Delay Variation Bins Measurem.
One-Way Delay Bins Measurement
Transmitted SLMs
Transmitted DMMs
Received SLRs
DMRs Received
Frames Exceed Delay Variation Threshold
Frame Loss Ratio Forward/Backward
Clear Statistics
Clear Statistics
 
Menu Map – OAM Monitoring 
3. Operation 
Configuration
Main Menu
3
Router
Static Route
Add New Static Route
IP Address
Subnet Mask
Next Hop Address
Interface
Add New Interface
Admin Status
Interface ID
IPv4 Address
Network Mask
Interface VLAN
Port
Management Interface
IPv4 Configuration
IP addressing mode
IP Address
Network Mask
IPv6 Configuration
Static Address
Autoconfig
DHCPv6-Client
General Configuration
Bind
Host VLAN
Default Gateway
Default GW (IPv4)
Default Router
Default Router (IPv6)
 
Menu Map – Router 
3. Operation 
Flows 
Port Capability
Auto Negotiation
Physical Port
Configuration
Main Menu
4
Add Flow
Config Flow 
Classification Mode
Flow Name
Ingress Port
L2CP Profile
Admin Status
Min VID Value
Max VID Value
Min P-bit Value
Max P-bit Value
Flow Name
Enable / Disable Flow
In-Serv L2 Loops
In-Service Action
In-Service Source Addresses
In-Service Destination Addresses
In-Service Mode
Delete Flow
TPID For Outer VLAN
TPID For Pushed\Replaced VLAN
Unclassified Action
DSCP   Pbits Remapping
C-Tag   S-Tag Remapping
In-Service Loop MACs
Service Name
DSCP Value
Service Name
Port Mode Action
L2CP\L2PT
EtherType Value
VID 
Pbits Mode
Pbits Value
Drop Eligible
MAC SRC Value
MAC DST Value
Flow Action
Port L2CP Profile
L2PT
Mac Change (for each protocol)
L2CP
Last MAC Byte (Hex.)
Remove
Profiles
New Profile Name
STP
OAM
PAgP
lldp
CDP
VTP
UDLD
DTP
PVSTP
(Row for each L2PT MAC change/
L2CP classification)
Remove
In-Service L3\L4 Loops
Source Addresses
Destination Addresses
In-Serv L3\L4 Loops
In-Service L3\L4 Mode
Ethernet
SFP
MSA
Classification
L3L4 Loop
Ingress Port
L3L4 Loop
TWAMP Session
TWAMP Session
SFP
MSA
General Params
TWAMP Session
In-Service IP Destination Address
 In-Service UDP Destination Port
In-Service L3\L4:IP Loop
Destination IP Address
In-Service L3\L4:UDP Loop
Destination IP Address
Destination UDP Port
In-Service L3\L4:UDP Echo
Destination IP Address
Destination UDP Port
LBM Reflector
Admin Status
MD Level [0-7]
MTU
LACP
LAMP
ESMC
PTP-Peer-Delay
 
Menu Map – Physical Port Configuration 
3. Operation 
Link OAM
CFM / PM
OAM
Configuration
Main Menu
Remove
5
Add/Update MA
OAM Mode
Ingress Port
Add/Update MEP
Add/Update MIP
MD Level
MA Name
MA Format
Service Name
VLAN ID
Priority
CCM Interval
Admin Status
MEP ID
Ingress Port
CCM Enable
CCM Transmission Mode
Client MD Level
AIS Enable
Admin Status
Remove MEP / MIP
Config MEP
Config
Start Loopback Session
LBM Session Mode
Data TLV Length
Start Linktrace Session
LTM Session Mode
Target MAC Address
Add/Update PM Service
Service Priority
Loss Threshold 
DEI Bit Color
Delay Threshold
Delay Var Threshold 
Service Interval
Admin Status
Remove Service
VLAN Tag Mode
Inner VLAN ID
Inner Priority
Outer VLAN ID
Outer Priority
TWAMP 
Add New TWAMP Responder Session
Ad/Update Remote MEP
Remote MEP ID
TTL
Remove Remote MEP
Config Service
Add/Update Dest NE
Admin Status
Remote MEP ID
Loss Measurement Service
Delay Measurement Service
Dest NE ID
Remove Dest NE
Responder ID
Responder Name
IP Address
UDP Port
Use Loaned IP 
Admin Status
Profile
Responder
Controller
Add New Profile
Profile Name
Payload Length
Transmit Rate
Loss Timeout
Loss Ratio  Threshold
Delay Variation Threshold
Delay Threshold
Delay Variation Event 
Type
Add New Controller
Controller Name
IP Address
Admin Status
 
Menu Map – OAM Configuration 
3. Operation 
Device Info
Name
Location
Contact Person
Mngmnt Access
MSA
User Access
User Level
User Name
Old Password
Description
Manager List
Manager 1
Manager 2
SFP
New Password
Confirm 
Password
SNMP
TFTP/SFTP
SSH
TELNET
HTTP
SNMP mode
SNMP port
TFTP/SFTP mode
TFTP/SFTP port
TELNET mode
TELNET port
SSH mode
SSH port
HTTP mode
HTTP port
Management Timeout
Timeout (Min.)
Zero Touch
Zero Touch
SNMP
Community 
Read/Write
Community 
Read only
Community Trap
Configuration
Main Menu
6
System
Management
 
Menu Map – System Management 
Configuration
Main Menu
7
System
Syslog
Facility
Severity Level
Port
Admin Status
Server Configuration
Address
Accounting Commands
Port
Admin Status
 
Menu Map – System Syslog 