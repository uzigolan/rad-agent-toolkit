# 3 Operation

*Manual `MiNID_ver_2_6_mn.pdf`, pages 59–88.*


## 3.1 Turning On the Unit  *(p.59)*


## 3.2 Indicators  *(p.59)*


## 3.3 Startup  *(p.59)*

3.1 Turning On the Unit 
MiNID SFP sleeve and MiNID SFP receive power from its host device, therefore they start to function 
when inserted into SFP-CA.2 or a host unit, or when the host device is powered on. 
3.2 Indicators 
MiNID SFP sleeve and MiNID SFP do not have LED indicators. 
3.3 Startup 
Configuration and Software Files 
The following system files contain configuration settings or application software: 
• 
factory-default-config – Contains the manufacturer default settings. At startup, 
factory-default-config is loaded if startup-config and user-default-config are missing or invalid. 
• 
running-config – Contains the current configuration that the device is running 
• 
startup-config – Contains saved non-default user configuration. You can use the save or copy 
command to create startup-config, or click <Save Configuration> in the Web interface. At 
startup, startup-config is loaded if it exists and is valid. 
• 
user-default-config – Contains default user configuration. This file is not automatically created. 
You can use the copy command or Utilities > File > Copy screen to create it. At startup, 
user-default-config is loaded if startup-config is missing or invalid 

## 3.4 Working with Custom Configuration Files  *(p.60)*

3. Operation 
• 
sw-pack-1 or sw-pack-2 – Contains application software. One of the software packs is 
designated as active.  
Loading Sequence 
At startup, the device attempts to load configuration files in the following sequence until a valid one is 
found: 
• 
startup-config 
• 
user-default-config 
• 
factory-default-config 
If an error is encountered while loading a file, MiNID stops loading that file, sends an event to indicate 
the error, and then looks for the next file in the sequence. 
To display MiNID  parameter values after startup, use the info command. 
3.4 Working with Custom Configuration Files 
In large deployments, often a central network administrator sends configuration files to the remote 
locations and all that remains for the local technician to do is to replace the IP address in the file or 
other similar minor changes, and then download the file to the device. Alternatively, the technician can 
download the file as is to the device, log in to the device and make the required changes, then save the 
configuration. 
To download the configuration file, use the copy command (refer to Administration). After downloading 
the configuration file, the unit must be reset in order to execute the file. After the unit completes its 
startup, the custom configuration is complete. 
If you have an appropriate existing MiNID  configuration file, you can use Zero Touch provisioning (see 
On-net Zero Touch Provisioning) to have the configuration file automatically fetched by all your  MiNID 
devices. Otherwise, you need to manually configure all your  MiNID devices with any additional 
non-default settings. 
There is no startup sequence other than Zero Touch, if enabled (see On-net Zero Touch Provisioning for 
further details). 
3. Operation 
On-net Zero Touch Provisioning 
Zero Touch provisioning allows  MiNID to acquire an IP address from a DHCP server and fetch 
configuration files from a TFTP server, eliminating the need to manually log into  MiNID to provision it.  
Zero Touch provisioning is enabled by configuring the following: 
• 
DHCP must be enabled (DHCP in menu Configuration > System > Management > Host IP; dhcp in 
level config>mngmt>host) 
• 
If the user management traffic is via a specific VLAN, the management VLAN must be configured 
(Host VLAN, Host VLAN ID, and Host VLAN Priority in menu Configuration > System > 
Management > Host IP; vlan-id and vlan-pbits in level config>mngmt>host). 
 
Note 
Zero touch must be enabled (Zero Touch in menu Configuration > System > 
Management > Zero Touch; zero-touch in level config>mngmt>host), 
however this is the default setting. 
 
Prerequisites 
• 
A DHCP server for providing the TFTP server address and configuration file information, in 
addition to the usual IP address, default gateway, etc. 
• 
A TFTP server with a configuration file, consisting of valid CLI commands. 
Sequence 
At reboot, when MiNID obtains a DHCP lease from the DHCP server, the lease provides the TFTP server 
address, either via option 150, or as a string (‘xxx.xxx.xxx.xxx’) via option 66. The DHCP lease provides 
the path and file name of the configuration file via DHCP option 67, if zero touch is to be used. 
1. If the lease specified a configuration file, MiNID  loads the configuration file from the TFTP 
server. If no configuration file was specified, the zero touch process does not start.  
2. If the TFTP download fails,  MiNID does the following: 
a. Send the trap systemDownloadEnd (with failed indication) to any configured network 
managers 
b. Start a 10-minute timer. 
c. When the timer expires,  MiNID attempts again to download the configuration file.  
3. If the configuration file is received successfully from the TFTP server,  MiNID  does the following: 

## 3.5 Configuration and Management  *(p.62)*

3. Operation 
a. Send the trap systemDownloadEnd (with success indication) to any configured network 
managers 
b. Verify that the file contains valid CLI commands 
c. Execute the commands in the file. 
Saving Configuration Changes 
When you make changes to the MiNID configuration, you need to save the changes so that they are 
available after the next device reset. You can save your configuration as follows: 
• 
Web: Click <Save Configuration> 
CLI: Use the save command to save running-config as startup-config 
• 
Web: Use the Utilities > File > Copy screen to copy running-config to startup-config or 
user-default-config 
CLI: Use the copy command to copy running-config to startup-config or user-default-config. 
3.5 Configuration and Management 
MiNID provides the following management interfaces: 
• 
Web interface over HTTP 
• 
CLI interface over Telnet / secure Telnet (SSH) 
Once MiNID is accessible via IP address, it can be configured via Web or Telnet/ secure Telnet (SSH). 
By default, MiNID can transmit management data over both of its ports. The MiNID SFP sleeve and 
MiNID SFP ports are designated as follows: 
• 
SFP –Provides socket where an SFP can be inserted into MiNID 
• 
MSA – Enables inserting MiNID into a customer device 
Management can be disabled on either port (see Management Access Control); it cannot be disabled 
for both ports simultaneously. 
MiNID SFP sleeve and MiNID SFP can be configured via the SFP-CA.2 adaptor, or via a switch that acts as 
a host device. See Configuration of MiNID SFP via SFP-CA.2 (Telnet/SSH/Web) and Configuration via 
Host (Telnet/SSH and CLI/Web Interface/RADview/SNMP). 

## 3.6 CLI-Based Configuration  *(p.63)*

3. Operation 
3.6 CLI-Based Configuration 
Working with Telnet/SSH 
You can use any Telnet/SSH client to connect to the MiNID CLI interface.  
Logging In 
 To connect to MiNID via Telnet/SSH: 
1. Point the Telnet/SSH client to MiNID’s IP address. Depending on the client, this may be done 
with the command: 
telnet <IP-address> 
3. Operation 
Or, you may need to type the IP address and select Telnet/SSH, and then select regular Telnet 
access or secure Telnet (SSH) access: 
 
Regular Telnet Connection with the PuTTY Client 
3. Operation 
 
Secure Telnet Connection with the PuTTY Client 
A login prompt appears. 
 
CLI Login Prompt – Regular Telnet 
3. Operation 
 
CLI Login Prompt – Secure Telnet 
2. Enter the relevant credentials (see User Access). 
Login 
To prevent unauthorized modification of the operating parameters,  supports various access levels. 
Refer to User Access in the Management and Security chapter for more information on the access 
levels, as well as a list of the default users defined in the device. 
 To log in to : 
1. At the user prompt (user>), enter su and press <Enter>. 
The password prompt (<password>) appears. 
2. Enter the password (default is 1234) and press <Enter>. 
The base prompt MiNID# appears. 
If you have lost your superuser password, contact Technical Support via the RADcare Online portal or by 
email. 
Using the CLI 
The CLI consists of commands organized in a tree structure of levels, starting at the base level. Each level 
(also referred to as context) can contain levels and commands (refer to the Navigating section for more 
information on the levels and commands available in MiNID). The level is indicated by the CLI prompt. 
3. Operation 
Note 
Most commands are available only in their specific context. Global commands 
are available in any context. You can type ? at any level to display the 
available commands. 
CLI Prompt 
The base level prompt contains the device name, which is MiNID by default (the device name can be 
configured in the system level; refer to the Device Information section in this manual). The prompt ends 
with #. 
After you type a command at the CLI prompt and press <Enter>, MiNID responds according to the 
command entered. 
Navigating 
To navigate down the tree, type the name of the next level. The prompt then reflects the new location. 
To navigate up, use the global command exit. To navigate all the way up to the root, type exit all or 
press <CTRL> + ‘Z’.  
At the prompt, one or more level names separated by a space can be typed, followed (or not) by a 
command. If only level names are typed, navigation is performed and the prompt changes to reflect the 
current location in the tree. If the level names are followed by a command, the command is executed, 
but no navigation is performed and the prompt remains unchanged. 
Note 
To use show commands without navigating, type show followed by the level 
name(s) followed by the rest of the show command. 
In the following example, the levels and command were typed together and therefore no navigation was 
performed, so the prompt did not change. 
MiNID# configure system date-and-time date-format yyyy-mm-dd 
MiNID# show configure system system-date 
2013-06-10   15:08:20  UTC  +00:00 
MiNID# 
In the following example, the levels were typed separately and the navigation is reflected by the 
changing prompt. 
MiNID# configure 
MiNID>config# system 
MiNID>config>system# date-and-time 
MiNID>config>system>date-time# date-format yyyy-mm-dd 
MiNID>config>system>date-time# exit 
MiNID>config>system# show system-date 
2013-06-10   15:13:23  UTC  +00:00 
 
3. Operation 
MiNID>config>system# 
Command Tree 
The tree command displays a hierarchical list of all the commands in the CLI tree, starting from the 
current context.  
 To view the entire CLI tree (commands only): 
1. At the root level, type tree. 
 
MiNID# tree 
| 
+---admin 
|   | 
|   +---factory-default-all 
|   | 
|   +---factory-default 
|   | 
|   +---reboot 
|   | 
|   +---software 
|   |   | 
|   |   +---install 
|   |   | 
|   |   +---software-confirm-required 
|   |   | 
|   |   +---undo-install 
|   |   | 
|   |   +---show status 
|   | 
|   +---startup-confirm-required 
more.. 
2. Press <Enter> to see more or <CTRL-C> to return to the prompt. 
Command Structure 
CLI commands have the following basic format: 
command [parameter]{ value1 | value2 | … | valuen } 
[ optional-parameter <value> ]  
 
where: 
{} 
Indicates that one of the values must be selected 
[] 
Indicates an optional parameter 
3. Operation 
<> 
Indicates a value to be typed by the user according to parameter 
requirements 
You can type only as many letters of the level, command, or parameter as required by the system to 
identify it. For example you can enter config manag to navigate to the management level. 
Special Keys 
The following keys are available at any time: 
? 
List all commands and levels available at the current level 
<Tab> 
Complete a string while typing commands and parameters 
<Backspace> 
Delete character before cursor 
<Delete> 
Delete character before cursor 
Left/right arrow 
Move cursor one character left/right 
Up/down arrow 
Command history for current level ( keeps the last five commands 
per level) 
<CTRL> + ‘Z’ 
Exit all 
Getting Help 
You can get help in the following ways: 
• 
Type ? to display general help (see General Help below) 
• 
Type <command> ? to display information on a command and its parameters (see Command 
Help) 
• 
Type ? to display the commands available in the level (see Level Help) 
• 
Use <Tab> while typing commands and parameters, for string completion (see String 
Completion) 
• 
Use ? after typing a command or parameter, for interactive help (see Interactive Help). 
General Help 
Type help or ? to display general CLI help, including: 
• 
Commands and levels available at the current level 
• 
Globally available commands. 
3. Operation 
Example of help or ? command output from the root level: 
MiNID# ? 
admin 
configure 
inventory 
file 
 
-- Global Commands -- 
exit 
info 
logout 
help 
tree 
ping 
save 
Command Help 
• 
Enter <command> ? to display command and parameter information. 
MiNID>config>mngmnt# timeout ? 
- timeout <minutes> 
Level Help 
Enter ? at the command prompt to display the commands available in the current level. 
MiNID>config#? 
access-control 
management 
router 
oam 
qos 
flows 
port 
reporting 
service 
system 
test 
String Completion 
MiNID automatically completes levels, commands, and parameters when you press <Tab> immediately 
after a string. 
If the string can be completed in more than one way, MiNID appends the characters that are common to 
all the possibilities. 
If the string can be completed in only one way, MiNID completes it and appends a space. 
3. Operation 
If the string is already a complete level/command/parameter or cannot be completed to a 
level/command/parameter, no completion is done. 
Pressing <Tab> a second time displays any available command parameters. 
Interactive Help 
 To get interactive help: 
• 
 type ?.  
In general, typing a ? directly after a string performs string completion, while typing <space> and then a 
? executes the command. 
When a <CR> appears in a ? list, the string you entered is itself a valid command needing no further 
additions. Pressing <Enter> executes the command or navigates to the indicated level. 
Typing ? immediately after a command or partial command with no space before the ?, tells MiNID to 
display all possibilities for completing the string. Help output is always followed by the string you typed 
with the cursor at the end of the string waiting for input. 
MiNID>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)# loss? 
loss-threshold 
loss-dei-bit-color 
Typing <?> after a space between a command or level name and the ? tells MiNID to try to execute the 
command. The space tells the CLI that you are finished typing and to try to match the string to an 
appropriate command. The string does not have to be a complete command. 
If there is only one possible command starting with that string, pressing <Enter> will execute the 
command.  
MiNID# con 
MiNID>config# 
If there is more than one command that starts with the string, the CLI displays a list of possible 
completions. 
MiNID>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)# loss ? 
loss-threshold 
loss-dei-bit-color 
A string that is a complete command name followed by a space ? displays all possible command 
parameters. 
MiNID>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)# loss-threshold ? 
loss-threshold 

## 3.7 Web-Based Configuration  *(p.72)*

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

## 3.8 SNMP-Based Network Management  *(p.85)*

3. Operation 
3.8 SNMP-Based Network Management 
Note 
Make sure that SNMP is enabled and not set in the “read-only” mode (see 
Management Access Control) before starting to work with RADview or other 
SNMP-based NMSs. 
Working with RADview 
RADview is a user-friendly and powerful SNMP-based element management system, used for planning, 
provisioning and managing heterogeneous networks. RADview provides a dedicated graphical user 
interface (GUI) for monitoring RAD products via their SNMP agents. RADview for MiNID is bundled in the 
RADview package for Windows or UNIX.  
RADview is a Windows-based modular, client-server, scalable management system that can be used in a 
distributed network topology or a single-station configuration. RADview consists of the system (EMS) 
and the following optional modules: 
• 
Service Manager (SM) – end-to-end Carrier Ethernet service provisioning for Ethernet Access 
products. This module includes the Service Center (SC) module, which is an end-to-end Carrier 
Ethernet and TDM service provisioning for CI (Critical infrastructure) products.  
• 
Performance Monitor (PM) – portal for service SLA monitoring for both carriers and their 
customers. 
 
Warning 
To prevent conflicts and ensure a stable and consistent network setup, 
provision services using either RADview Service Manager or CLI, but not 
both simultaneously. 
 
For more details about this network management software, and for detailed instructions on how to 
install, set up, and use RADview, contact your local RAD partner. See Working with Other SNMP-Based 
NMSs for details on the SNMP MIBs used by MiNID. 
RADview for MiNID supports autodiscovery and alarms, as well as configuration via SNMP. You can 
double-click the MiNID icon in RADview to activate a connection to the MiNID web interface, or 
right-click the MiNID icon in RADview and select the option to open a Telnet session. 

## 3.9 Configuration of MiNID SFP via SFP-CA.2 (Telnet/SSH/Web)  *(p.86)*

3. Operation 
Working with Other SNMP-Based NMSs 
MiNID can be integrated into third-party network management systems (NMS) with basic autodiscovery 
and alarm functionality, by having MiNID send basic status SNMP traps to the NMS. MiNID must be 
configured to define the NMS as an SNMP Manager. 
SNMP (Simple Network Management Protocol) is an application-layer protocol that provides a message 
format for communication between managers and agents. MiNID acts as an SNMP agent, sending SNMP 
traps to up to two configured SNMP Managers. MiNID supports SNMPv1 and SNMPv2. 
The supported SNMP features are based on the following standards: 
Reference 
Title 
RFC 3418 
Management Information Base (MIB) for the Simple Network 
Management Protocol (SNMP) 
RFC 2863 
The Interfaces Group MIB 
The MiNID OIDs are: 
• 
For SPF sleeve – 1.3.6.1.4.1.164.6.1.6.36 
• 
For  SFP – 1.3.6.1.4.1.164.6.1.6.54 
3.9 Configuration of MiNID SFP via SFP-CA.2 
(Telnet/SSH/Web) 
You can use RAD’s SFP-CA.2 module for the following: 
• 
Configure MiNID SFP and MiNID SFP Sleeve by using SFP-CA.2 as a hosting device (possible only 
with a PC that has Windows XP SP2 installed) 
• 
Access the boot menu in order to upgrade MiNID software (possible only with a PC that has 
Windows XP SP2, Windows 7, or Windows 10 installed). Refer to Chapter 12 for more 
information on upgrading 
Note 
All SFP-CA.2 modules have the MAC address 00-00-E8-00-00-01. 
3. Operation 
Preconfiguration for SFP-CA.2 
When you connect SFP-CA.2 to a specific PC for the first time, if you wish to configure MiNID via 
SFP-CA.2 then you have to install the SFP-CA.2 driver on that PC, and configure the PC network 
parameters for communication with SFP-CA.2. Refer to the SFP-CA.2 supplement for instructions on how 
to download and install the driver. 
 To configure the PC network parameters for the SFP-CA.2 connection to MiNID: 
1. Connect the SFP-CA.2 configuration unit to a USB port on your PC.  
The New Hardware is Detected notice appears. 
2. Right-click My Network Places. 
A new local area network connection appears in the list of network connections.  
3. Right-click the new local area connection and rename it SFP-CA. 
4. Right-click Properties, click Configure, and select the Advanced tab 
The Network Connection Properties dialog box appears. 
5. Choose Select Media and under Value, choose Home LAN, and then click OK. 
The dialog box closes and your settings are applied. 
6. Right-click the SFP-CA connection and click Properties. 
The Local Area Connection Properties dialog box appears. 
7. Select Internet Protocol (TCP/IP) and click Properties. 
The Internet Protocol (TCP/IP) dialog box appears. 
8. To enable entering TCP/IP settings, select Use the following IP Address. 
The IP Address and Subnet Mask fields become available. 
9. Enter the following TCP/IP settings and then click OK: 
 
IP Address: 192.168.205.20 
 
Subnet Mask: 255.255.255.0 
10. Close My Network Places. 
The PC is ready to communicate with MiNID. 
Connecting SFP-CA.2 
For instructions on how to connect SFP-CA.2, see the Inserting  into an SFP-CA.2 section in Chapter 2. 

## 3.10 Configuration via Host (Telnet/SSH and CLI/Web Interface/RADview/SNMP)  *(p.88)*


## 3.11 Turning Off the Unit  *(p.88)*

3. Operation 
3.10 Configuration via Host (Telnet/SSH and CLI/Web 
Interface/RADview/SNMP) 
A similar procedure to configuring via SFP-CA.2 can be used to configure MiNID SFP sleeve and MiNID 
SFP when it is inserted into the SFP port of a host device, as long as connectivity is established to an 
available Ethernet port. 
 To configure MiNID via a host: 
1. Disconnect MiNID from any device. 
2. If you use MiNID SFP sleeve, insert any compatible SFP into it. 
3. Set MiNID to Configuration mode, using its DIP switches (refer to Setting the DIP Switches in 
Chapter 2). 
Note 
While MiNID is in Configuration mode, it responds to the default IP address 
192.168.205.1, with no host VLAN, even if a different IP address was 
configured. 
4. Insert MiNID SFP sleeve or MiNID SFP into an available SFP socket of the switch. 
5. Connect the available switch port to which connectivity has been established, to your PC, using 
an IP address in the subnet 192.168.205.XX. 
6. Using either your browser or Telnet, connect to 192.168.205.1 and log in with su credentials 
(see User Access). 
3.11 Turning Off the Unit 
 SFP sleeve and SFP receive power from their host device, therefore they stop functioning when 
removed from SFP-CA.2 or a host unit, or when the host device is powered off. 
 