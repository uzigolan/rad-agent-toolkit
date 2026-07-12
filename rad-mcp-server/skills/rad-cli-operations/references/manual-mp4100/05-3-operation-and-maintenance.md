# 3 Operation and Maintenance

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 163–196.*


## 3 Operation and Maintenance  *(p.163)*

This chapter: 
• 
Explains power-on and power-off procedures. 
• 
Describes the Megaplex-4 LED indicators and their function. 
3.1 Turning On the Unit 
When turning Megaplex-4 on, it is useful to monitor the power-up sequence. 
You can monitor the power-up sequence using any standard ASCII terminal (dumb terminal or personal 
computer emulating an ASCII terminal) equipped with an RS-232 communication interface (same 
terminal that can be used to control the Megaplex-4 operation). 
 To monitor Megaplex-4: 
4. Configure the terminal for 9600 bps, one start bit, eight data bits, no parity, and one stop bit.  
5. Select the full-duplex mode, echo off, and disable any type of flow control. Make sure to use 
VT-100 terminal emulation: using a different terminal type will cause display problems, for 
example, the cursor will not be located at the proper location, text may appear jumbled, etc. 
 To prepare Megaplex-4 for first-time turn-on: 
6. Before first-time turn-on, inspect Megaplex-4 installation and check that the required cable 
connections have been correctly performed in accordance with Chapter 2. 
7. To monitor the Megaplex-4 during power up and to perform preliminary configuration 
procedures, connect a terminal to the CONTROL DCE connector of the CL module installed in 
Megaplex-4 slot CLX-A (this module will be, by default, the active CL module).  
Note 
On the supervision terminal screens, the slots assigned to CL modules are 
identified as CL-A, and CL-B.  
3. Operation and Maintenance 
 To turn the Megaplex-4 on: 
Caution 
When an external feed and ring voltage source is connected to the PS 
modules installed in Megaplex-4, always turn that source on only after the 
PS module(s) have been turned on.  
1. Turn the power on.  
Note 
The Megaplex-4 PS modules do not include a power switch. Use an external 
power ON/OFF switch, for example, the circuit breaker used to protect the 
power lines.  
2. Wait for the completion of the power-up initialization process. During this interval, monitor the 
power-up indications: 
 
After a few seconds, Megaplex-4 starts decompressing its software.  
 
After software decompression is completed, all the indicators turn off for a few seconds 
(except for the POWER indicators) as Megaplex-4 performs its power-up initialization.  
You can monitor the decompression and initialization process on the terminal connected to the 
Megaplex-4.  
3. After the power-up initialization ends, all the POWER indicators must light, the ON LINE 
indicator of the active CL module lights in green and that of the other CL module flashes slowly 
in green. At this stage, the indicators display the actual Megaplex-4 status.  
3.2 Indicators 
The following tables summarize the function of all LED indicators in  
Megaplex-4. The normal indications on power-up (provided the corresponding port is connected) are 
marked in bold.  
CL.2 Front Panel Indicators 
The figure below shows typical dual-slot CL.2 module panels with SDH/SONET and GbE interfaces (all 
possible CL.2 panels are described in Chapter 2). Indicators for single-slot CL.2 modules of Megaplex-
4104 are identical. The tables below describe the functions of the panel components.  
3. Operation and Maintenance 
 
ON
LINE
CL-2
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
1
2
LOS
S
D
H
/
S
O
N
E
T
1
2
LASER
CLASS
1
 
ON
LINE
CL-2
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
LOS
S
D
H
/
S
O
N
E
T
1
2
1
2
LASER
CLASS
1
 
Copper GbE Interfaces 
Optical GbE 
Interfaces 
 
 
 
 
CL.2 Module Panels  
CL.2 System LED Indicators 
Name 
LED Color 
Function 
ON LINE  
 
Yellow/green 
• On (green): CL module is active or software 
decompression 
• Blinking slowly (green): CL module is on standby 
• On (yellow): a test is being performed (active 
module only) 
3. Operation and Maintenance 
Name 
LED Color 
Function 
ALM  
Red 
• On: alarms have been detected in the  
Megaplex-4, but the highest alarm severity is minor 
or warning. 
• Blinking: a major and/or critical alarm has been 
detected in Megaplex-4 
• Off: No active alarms 
Note 1: On the standby CL module, this indicator is 
always off, even while an alarm condition is present 
Note 2: The LED still remains on even when active 
alarms are already cleared. It only turns off once active 
alarms have been cleared via clear-alarm-log all-logs 
command.   
SDH/SONET Link LED Indicators 
Name 
LED Color 
Function 
ON LINE  
Green/Yellow 
On (green): the corresponding port is active (carries 
SDH/SONET traffic, and there is no major alarm 
condition, nor any test on this port) 
Blinking (green) – the port is in protection mode 
On (yellow): a test is active on the port 
Off: no traffic or test on the port 
LOS  
Red 
On: loss-of-signal at the corresponding port  
Off: no loss-of-signal 
Note: Any other alarm condition related to 
SDH/SONET traffic handled by the port is indicated 
only by the CL general alarm (ALM) indicator 
 
Note 
Status indicators for SDH/SONET ports are active only when the corresponding 
port is equipped with an SFP and configured as no shutdown.  
3. Operation and Maintenance 
Gigabit Ethernet Port LED Indicators 
Name 
LED Color 
Function 
LINK (per port) 
 
Green  
On: the port is connected to an active Ethernet hub or 
switch 
Off: Ethernet link is not detected 
ACT (per port) 
Yellow 
On or Blinking (in accordance with the traffic): ETH 
frames are received or transmitted 
Off: ETH frames are not received and transmitted  
 
Note 
GbE Status indicators are active only when the corresponding port is 
configured as no shutdown, and for optical ports – when the port is equipped 
with an SFP 
Management Ethernet Port LED Indicators 
Name 
LED Color 
Function 
LINK (per port) 
 
Green  
On: the port is connected to an active Ethernet hub or switch 
Off: Ethernet link is not detected 
ACT (per port) 
Yellow 
On or Blinking (in accordance with the traffic): ETH frames are 
received or transmitted 
Off: ETH frames are not received and transmitted  
Clock LED Indicators 
Name 
LED Color 
Function 
ON  
Green 
 
On: the station clock port is configured as no shutdown 
Off: no traffic or test on the port 
LOS  
Red 
On: loss-of-signal (when station clock port configured as connected)  
Off: no loss-of-signal 
Front Panel Indicators 
The front panels of the Megaplex-4100 and Megaplex-4104 chassis include additional system status 
indicators. The figures below identify the front panel indicators, and the table below describes indicator 
functions. 
3. Operation and Maintenance 
MEGAPLEX-4100
POWER SUPPLY
B
A
SYSTEM
ALARM
TEST
 
Megaplex-4100 Chassis, Front Panel 
 
Megaplex-4104 Chassis, Front Panel 
System LED Indicators  
Name 
Color 
Function 
POWER SUPPLY A, B 
Green 
• On: the corresponding PS module is on (and one of the CL 
modules is active) 
• Off: Power supply is off 
SYSTEM TEST  
Yellow 
• On: a test (or loopback) is being performed in the Megaplex-
4100 
• Off: No active tests 
SYSTEM ALARM 
Red 
• Blinking: a major and/or critical alarm has been detected in 
Megaplex-4100   
• On: a minor alarm has been detected in Megaplex-4100   
• Off: No active alarms 
3. Operation and Maintenance 
3.3 Startup 
Configuration Files 
The following files contain configuration settings: 
• 
factory-default contains the manufacturer default settings 
• 
running-config contains the current configuration that is different from the default 
configuration 
• 
startup-config contains the saved non-default user configuration. This file is not automatically 
created. You can use the save or copy command to create it.  
• 
user-default-config contains default user configuration. This file is not automatically created. 
You can use the copy command to create it. 
• 
candidate stores any configuration before it is copied to running-config via commit command.  
• 
main-sw contains the active software image. 
Loading Sequence 
At startup, the device boots from the startup-config file, the user-default file, or the factory-default file, 
in the sequence shown in the figure below. If none of these files exist, the device boots using 
hard-coded defaults.  
3. Operation and Maintenance 
Startup-config exist?
Start
User-default-config 
exist?
No
Yes
Boot from
Startup-config
Yes
Boot from
User-default-config
End
No
Boot from
Factory-default-config
Sanity 
Check
Sanity 
Check
Pass
Pass
Fail
Fail
 
Loading Sequence 
If the loading of startup-config or the user-default file fails, the loading failure event is registered in the 
event log. 
To display the parameter values after startup, use the info [detail] command. 
3.4 Working with Custom Configuration File 
In large deployments, often a central network administrator sends configuration scripts to the remote 
locations and all that remains for the local technician to do is to replace the IP address in the script or 
other similar minor changes (using any text editor), and then download the file to the device. 
3. Operation and Maintenance 
To download the configuration file, use the copy command. It is recommended to copy the file to both 
startup-config and the user-default file and check that the device passes the sanity test (no 
configuration errors are displayed). 
After downloading the configuration file to startup-config, you have to execute the file. This can be 
done in two ways: 
• 
Reset the unit. After the unit completes its startup, the custom configuration is complete. 
• 
Instead of resetting the unit, you can simply copy the configuration file to the running-config file 
(see File Operations in Chapter 10). 
• 
The figure below shows the commands that can copy configuration files in a visual diagram. For 
details on file operations, refer to File Operations in Chapter 10. 
• 
 
Configuration 
Session
(Candidate DB)
Running-config
Commit
Sanity 
check
Startup-Config
Save
User-Default -
Config
Factory-Default 
TFTP
Admin user-default
Copy
Admin factory-default
Copy
Copy
TFTP
 
Commands that Copy Configuration Files  
3.5 Configuration and Management   
The following table summarizes management alternatives for Megaplex-4.  
3. Operation and Maintenance 
Management Alternatives 
Port 
Manager 
Location 
Transport 
Method 
Management 
Protocol 
Application 
CONTROL DCE 
Local 
Out-of-band 
RS-232 
Terminal emulation programs 
(HyperTerminal, Procomm, 
Putty). See Management Access 
Methods below. 
CONTROL ETH, any 
user ETH port on 
CL or I/O modules 
 
Local, 
remote 
Out-of-band 
(via 
CONTROL 
ETH only), 
Inband 
 
Telnet, SSH over 
Ethernet 
Procomm, Putty (see Error! 
Reference source not found. 
below) 
STM-1/STM-4/ 
OC-3/OC-12 links 
Remote 
Inband 
Telnet, SSH over 
DCC (IP/PPP or 
IP/HDLC) 
Procomm, Putty (see Error! 
Reference source not found. 
below) 
Any E1/T1 link 
 
Remote 
Inband 
Telnet, SSH over 
a dedicated 
timeslot (IP/PPP 
or IP/FR) 
Procomm, Putty (see Error! 
Reference source not found. 
below) 
 
 
 
SNMP over a 
dedicated 
timeslot (IP/PPP 
or IP/FR) 
RADview (see Configuring 
Management Access below) 
3rd-party NMS (see Working 
with other SNMP-based NMS 
below)  
 
Note 
By default, the terminal, Telnet (SSH), and SNMP management access 
methods are enabled.  
The following functions are supported by the Megaplex-4 management software: 
• 
Viewing system information 
• 
Modifying configuration and mode of operation, including setting system default values and 
resetting the unit 
• 
Monitoring performance 
• 
Initiating connectivity tests 
• 
Uploading and downloading software and configuration files. 
3. Operation and Maintenance 
3.6 Management Access Methods  
Two methods used to access the Megaplex-4 management host are via Layer 2 or Layer 3 networks. By 
default, Megaplex-4 is managed by Router 1, via Layer-3. If you want to manage the device via a 
management VLAN (Layer-2 management), the bridge must be configured. 
Layer-3 Management Access 
The following figure illustrates a typical Layer-3 management scheme.  
Megaplex-4 and remote CPE devices are managed using: 
• 
Out-of-band traffic via a dedicated Ethernet management port, or 
• 
Inband traffic via E1/T1 and SDH/SONET ports.  
mng-eth 
cl-a
Router
mng-eth 
cl-b
RI#1
SVI#1
RI#2
RI#3
DTS
PPP
DCC
PPP
Host
 
Layer-3 Management Access 
The Megaplex-4 host can be accessed by defining IP address and enabling management on any of the 
internal router interfaces. 
By default, Megaplex-4 has router interface 1 connected to out-of-band Ethernet management port 
internally (when no flows are configured between the bridge and the out-of-band Ethernet 
management port). 
For description of Layer-3 management access, see Management Router section in Chapter 3. 
3. Operation and Maintenance 
Layer-2 Management Access 
The following figure illustrates a typical Layer-2 management scheme. Megaplex-4 and remote CPE 
devices share the same Layer-2 broadcast domain (VLAN X) and Layer-2 forwarding entity (bridge) is 
used for access. 
In this scheme, Megaplex-4 and remote CPE devices can be managed using: 
• 
Out-of-band traffic via a dedicated Ethernet management port, or 
• 
Inband traffic via any Ethernet port. 
The Megaplex-4 host is an IP address of a router interface, connected to a bridge port. 
Bridge#1 Aware
BP#3
1
BP#2
Router
RI#1
RI#2
RI#3
DTS
PPP
DCC
PPP
Host
mng-eth 
cl-b
mng-eth 
cl-a
BP#1
SVI#1
 
Layer-2 Management Access 
For description of Layer-2 management access, see Bridge section in Chapter 3. 
3.7 Services for Management Traffic 
To gain access to the devices, as explained in Error! Reference source not found., you must provision an 
E-LAN (Layer-2) or routing (Layer-3) service. Services are explained in Chapter 4. 
 
3. Operation and Maintenance 
3.8 CLI-Based Configuration 
Working with Terminal 
Megaplex-4 has a V.24/RS-232 asynchronous DCE port, designated CONTROL DCE and terminated in a 9-
pin D-type female connector. The control port continuously monitors the incoming data stream and 
immediately responds to any input string received through this port.  
 To set up terminal control: 
1. Verify that all the cables are properly connected. For more information, refer to Chapter 2. 
2. Connect Megaplex-4 to a PC equipped with HyperTerminal. Refer to  
Connecting to a Terminal in Chapter 2 for additional information on connecting to the control 
port. 
3. Turn on the control terminal or start the PC terminal emulation. To do so, go to Start> All 
Programs> Accessories> Communications>HyperTerminal to create a new terminal connection. 
The HyperTerminal application opens, and the Connection Description dialog box is displayed. 
 
1. Enter a name for the terminal connection. 
2. Select an icon to represent the terminal connection, or leave the default icon selected. 
3. Click <OK>. 
The Connect To dialog appears. 
3. Operation and Maintenance 
 
4. Select a PC COM port to be used to communicate with Megaplex-4 and click <OK>. 
The COM Properties dialog appears. 
 
5. Configure the communication port parameters as follows: 
 
Bits per second: 9,600 
 
Data bits: 8 
 
Parity: None 
 
Stop bits: 1 
 
Flow control: None. 
6. Click <OK>. 
HyperTerminal is now ready for communication with the unit. 
3. Operation and Maintenance 
7. Power-up the unit by connecting the power cable(s). 
Megaplex-4 boots up and self-test results appear on the terminal screen. Once the test has been 
completed successfully, the ON LINE LED becomes green and a login prompt appears.  
 
8. Refer to the next section for details on logging on. 
Working with Telnet and SSH 
Typically, the Telnet host is a PC or a Unix station with the appropriate suite of TCP/IP protocols.  
To enable a Telnet host to communicate, it is necessary to assign its IP address to the management 
router (1) interface 1. This interface is configured by default and connected to the out-of-band Ethernet 
management port (CONTROL ETH). After this preliminary configuration, you can use a Telnet host 
connected to it directly or via a local area network.  
Working with Telnet  
Telnet uses the terminal utility screens for configuration. The only difference is that Telnet management 
access is possible only after performing a preliminary configuration of the Megaplex-4. 
 To configure router interface #1 for management: 
Define IP address of the management interface (#1). 
Note 
The IP address must be configured to a value different from 1.1.1.x.  
1. Define the default gateway (static-route 0.0.0.0/0).  
3. Operation and Maintenance 
# configure 
config# router 1 
config>router(1)# interface 1 
config>router(1)>interface(1)# address 172.18.170.77/24 
config>router(1)>interface(1)#exit 
config>router(1)# static-route 0.0.0.0/0 address 172.18.170.1 
config>router(1)#commit 
2. Enable Telnet access if it is disabled. By default, Megaplex-4 has Telnet access enabled.  
 To enable or disable access via Telnet: 
1. At the config>mngmnt# prompt, enter access. 
The config>mngmnt>access# prompt appears. 
2. Type telnet to enable or no telnet to disable Telnet access. The access is enabled by default. 
Using SSH 
 To prepare for using SSH: 
1. If your Megaplex-4 is not yet configured for management, configure router interface #1 as 
shown above for Telnet (if you already have Telnet configured, no need to do this). 
2. Enable SSH access if it is disabled. By default, Megaplex-4 has SSH access enabled.  
 To enable or disable access via SSH: 
1. At the config>mngmnt# prompt, enter access. 
The config>mngmnt>access# prompt appears. 
2. Type ssh to enable or no ssh to disable Telnet access. The access is enabled by default. 
3. Connect the Ethernet port of the PC to the CONTROL ETH port of the active CL module, or to the 
same LAN the CONTROL ETH port is attached to.  
4. Start the SSH client program, and select the following parameters:  
 
Connection type: SSH  
 
IP address: use the preconfigured host IP address 
 
Port: 22 (the default SSH port) 
3. Operation and Maintenance 
 
5. Click Open to open the SSH session with the Megaplex-4. 
6. You will see the log-in prompt: type the prescribed user name, for example, su, and then press 
<Enter>. 
7. You will see a request for password: enter the prescribed password, for example, 1234, and then 
press <Enter>. 
8. If login is successful, you will see the main menu. 
Login 
To access the unit's management/configuration/monitoring options, you must log in. 
Megaplex-4 supports the following access levels:  
• 
Superuser (su) can perform all the activities supported by the Megaplex-4 management facility, 
including defining new users of any level and changing their passwords.  
• 
Operator (oper) can perform all the activities except defining new users and changing 
passwords.  
3. Operation and Maintenance 
• 
User (user) can only monitor the device or change his/her own password  
• 
Technician (tech) can monitor the device, perform diagnostics and clear alarms) 
 To enter the Megaplex-4100 CLI: 
1. At the User prompt (user>), enter the access level (su | oper | tech | user) and press <Enter>. 
2. The Password prompt (password>) appears. 
Enter 1234 as password and press <Enter>. 
The base prompt # appears. 
Note 
It is recommended to change default passwords to prevent unauthorized 
access to the unit.  
A special option (chngpass) is provided for the case when the user has forgotten his/her password.  
 To change/restore the password:  
1. At the User prompt (config>mngmnt# user>), enter chngpass and press <Enter>. 
2. Enter user as user name and press <Enter> to receive a temporary password. With this 
password you can enter as user and change the password to your own.   
A key code is displayed. 
3. Send the key code to RAD Technical Support department. 
RAD technical support department will generate a temporary password which is valid for a 
single login. 
4. Use this temporary password to login and set new permanent user name and password. 
Using the CLI  
The CLI consists of commands organized in a tree structure of levels, starting at the base level. Each level 
(also referred to as context) can contain levels and commands (refer to the Error! Reference source not 
found. section for more information on the levels and commands available in Megaplex-4). The level is 
indicated by the CLI prompt. 
Note 
Most commands are available only in their specific context. Global commands 
are available in any context. You can type ? at any level to display the 
available commands.  
3. Operation and Maintenance 
CLI Prompt 
The base level prompt contains the device name, which is mp4100 by default (the device name can be 
configured in the system level; refer to the Device Information section in this manual). The prompt ends 
with $, #, or >, depending on the type of entity being configured and the user level.  
Commands that are not global are available only at their specific tree location, while global commands 
can be typed at any level. To find out what commands are available at the current location, type ?. 
If a new dynamic entity is being configured, the last character of the prompt is $. Examples of dynamic 
entities include flows, QoS profiles, and OAM CFM entities.  
If a new dynamic entity is not being configured, the last character of the prompt is > (for tech or user 
access levels) or # (for other access levels). 
In addition to being the default prompt, the # symbol also indicates a static or already configured entity. 
The $ symbol indicates a new dynamic entity that takes several commands to configure. The dynamic 
entity is created as inactive. After the configuration is completed, it is activated by using the 
no shutdown command, as shown in the following example. 
# configure port logical-mac 5/1 
config>port>log-mac(5/1)$ bind mlppp 5/1 
config>port>log-mac(5/1)$ no shutdown 
config>port>log-mac(5/1)$ commit  
Creating and Activating Dynamic Entity 
The shutdown command disables a hardware element (such as a port), while no shutdown 
enables/activates it. 
Note 
The examples in this manual use # as the last character of the prompt, unless 
the creation of a new dynamic entity is being illustrated.  
After you type a command at the CLI prompt and press <Enter>, Megaplex-4 responds according to the 
command entered. 
Navigating 
To navigate down the tree, type the name of the next level. The prompt then reflects the new location, 
followed by #. To navigate up, use the global command exit. To navigate all the way up to the root, type 
exit all.  
At the prompt, one or more level names separated by a space can be typed, followed (or not) by a 
command. If only level names are typed, navigation is performed and the prompt changes to reflect the 
3. Operation and Maintenance 
current location in the tree. If the level names are followed by a command, the command is executed, 
but no navigation is performed and the prompt remains unchanged. 
Note 
To use show commands without navigating, type show followed by the level 
name(s) followed by the rest of the show command.  
In the example below the levels and command were typed together and therefore no navigation was 
performed, so the prompt has not changed. 
# configure port ppp 5/1 bind e1 5/1 
# configure port ppp 5/2 bind e1 5/2 
# configure port ppp 5/3 bind e1 5/3 
# configure port ppp 5/4 bind e1 5/4 
# configure port ppp 5/5 bind e1 5/5 
# configure port ppp 5/6 bind e1 5/6 
# configure port ppp 5/7 bind e1 5/7 
# configure port ppp 5/8 bind e1 5/8 
Commands without Level Navigation 
In the following example, the levels were typed separately and the navigation is reflected by the 
changing prompt. 
#  
# configure  
config# port 
config>port# ppp 5/1  
config>port# ppp(5/1)# bind e1 5/1  
config>port# ppp(5/1)#  
Commands with Level Navigation 
Note 
Level names are abbreviated in the prompt.  
Command Tree 
The tree command displays a hierarchical list of all the commands in the CLI tree, starting from the 
current context.  
 To view the entire CLI tree (commands only): 
1. At the root level, type tree. 
 
# tree 
| 
+---admin 
|   | 
3. Operation and Maintenance 
|   +---factory-default 
|   | 
|   +---reboot 
|   | 
|   +---software 
|   |   | 
|   |   +---install 
|   |   | 
|   |   +---show status 
more.. 
2. Press <Enter> to see more or <CTRL-C> to return to the prompt. 
When adding the detail parameter, the output also includes the parameters and values for each 
command. 
 To view the CLI tree including all parameters and values: 
1. Navigate to the required context by typing level names separated by a space and press <Enter>.  
2. Type tree detail and press <Enter>. 
config# tree detail 
configure 
| 
+---access-control 
|   | 
|   +---access-list [ipv4] <acl-name> 
|   |   no access-list <acl-name> 
|   |   | 
|   |   +---delete <sequence-number> 
|   |   | 
|   |   +---deny udp <src-address> [<src-port-range>] <dst-address> 
                [<Dst-port>] [log] [sequence 
                 <sequence>] 
|   |   |   deny tcp <src-address> [<src-port-range>] <dst-address> 
                 [<dst-port >] [log] [sequence 
                 <sequence>] 
3. Press <Enter>to see more or <CTRL-C> to return to the prompt. 
Command Structure 
CLI commands have the following basic format: 
command [parameter]{value1 | value2 | … | valuen} [optional parameter <value>]  
where: 
{} 
Indicates that one of the values must be selected 
[] 
Indicates an optional parameter 
3. Operation and Maintenance 
<> 
Indicates a value to be replaced by user text 
You can type only as many letters of the level, command, or parameter as required by the system to 
identify it. For example, you can enter config manag to navigate to the management level. 
To finish configuration changes, type commit. If this command is performed successfully, OK is 
displayed. Otherwise, Megaplex-1 displays the relevant error message. 
To verify whether the applied configuration changes are valid (before applying commit), use the sanity-
check command. 
You can remove all configuration activity after the last commit command using the discard-changes 
command. 
Special Keys 
The following keys are available at any time:  
? 
List all commands and levels available at the current level 
<Tab> 
Command autocomplete 
↑ 
Display the previous command (history forward) 
↓ 
Display the next command (history backward) 
<Backspace> 
Delete character before cursor 
<Delete> 
Delete character before cursor 
<- 
Move cursor one character left 
-> 
Move cursor one character right 
<Ctrl-E> 
Log out 
<Ctrl>+Z 
Navigate to base level 
The following commands are available at any time and at any level:  
echo [<text-to-echo>] 
Echoes the specified text 
exec <file-name> [echo] 
Executes a file, optionally echoing the commands 
help [hotkeys] [globals] 
Displays general help, or optionally just the hotkeys 
and/or global commands  
history 
Displays the command history for the current 
session (by default the history contains the last 10 
commands) 
info [detail] 
Displays information on the current configuration 
3. Operation and Maintenance 
tree [detail] 
Displays all lower command levels and commands 
accessible from the current context level 
Getting Help 
You can get help in the following ways: 
• 
Type help to display general help (see Error! Reference source not found.) 
• 
Type help <command> to display information on a command and its parameters 
• 
Type ? to display the commands available in the level (see Error! Reference source not found.) 
• 
Use <Tab> while typing commands and parameters, for string completion  
• 
Use ? after typing a command or parameter, for interactive help (see Error! Reference source 
not found.). 
General Help 
Enter help at any level to display general CLI help, including: 
• 
Short description of CLI interactive help 
• 
Commands and levels available at the current level 
• 
Globally available commands  
• 
CLI special keys (hotkeys) 
• 
Output modifiers for filtering output. 
Example of help command output from the root level: 
1. Full help - 'help <cmd>'. 
2. To complete level name, command, keyword, argument - <tab> ('conf<tab>' => 
    'configuration'). 
3. To display all currently valid levels, commands, keywords or arguments - 
   '?' ('name ?' => '<name-of-device>'). 
Commands and levels: 
      admin                           + Administrative commands 
      configure                       + Configure device 
      file                            + File commands 
       
Global commands: 
      commit                - Update the candidate database to the running 
                              database 
      discard-changes       - Resets to last-saved parameter profile 
      echo                  - Displays a line of text (command) on the screen 
3. Operation and Maintenance 
      exec                  - Executes a file (enables downloading a file including CLI      
commands to user-script file and running this script file)  
 
      exit                  - Returns to the next higher command level (context) 
      help                  - Displays information regarding commands in the 
                              current level 
      history               - Displays the history of commands issued since the 
                              last restart 
      info                  - Displays the current device configuration 
      level-info            - Displays the current device configuration - 
                              commands from the current level only 
      logout                - Logs the device off 
      ping                  - Ping request to verify reachability of remote host 
      sanity-check          - Initiates a self test of the device 
      save                  - Saves current settings 
      startup-config-confi* - Confirm configuration (When downloading a startup-config file, 
the user can ask for confirmation, if the user is afraid that 
the device may get stuck with new configuration. This command 
activates the timer after rebooting the device with the new 
startup-config; if the timer expires without the user’s 
confirmation, the device will reboot and return to the previous 
configuration) 
      tree                  - Displays the command levels from the current 
                              context downwards 
      virtual-terminal      - Enter the virtual terminal 
Hotkeys: 
       DEL                    -delete character 
      <-                     -move cursor right 
      ->                     -move cursor left 
      TAB                    -complete token 
      ?                      -help 
      Arrow up               -history forward 
      Arrow down             -history backward 
      BACKSPACE              -delete character 
      ^Z                     -return to configuration root 
      ^E                     -exit cli 
Command Help 
Enter help <command> to display command and parameter information. 
config>system# help name 
 - name <name-of-device> 
 - no name 
 <name-of-device>  : Adds free text to specify the device name [0..255 chars] 
Level Help 
Enter ? at the command prompt to display the commands available in the current level. 
file# ? 
3. Operation and Maintenance 
      copy 
 
- Copies a file  
 
delete                  - Deletes a file from the device 
      dir                     - Lists all files in the device 
 
show copy                     - Displays copy status 
show sw-pack                  - Displays the existing sw-packs and their content 
String Completion 
Megaplex-4 automatically completes levels, commands, and parameters when you press <Tab> 
immediately after a string. 
If the string can be completed in more than one way, Megaplex-4 appends the characters that are 
common to all the possibilities. 
If the string can be completed in only one way,  Megaplex-4 completes it and appends a space. 
If the string is already a complete level/command/parameter or cannot be completed to a 
level/command/parameter, no completion is done. 
Pressing <Tab> a second time displays any available command parameters. 
Some user-defined strings such as flow names or profile names can be completed as well. If the user 
enters an entity name (flow, profile or similar) that does not exist in the database, Megaplex-4 creates 
this entity with the selected name.  
The following table shows examples of string completion.  
Level 
String  
Possibilities for Completion 
Result After Pressing <Tab> 
file 
show c 
show configuration-files 
show copy 
show co 
file 
show con 
show configuration-files 
show configuration-files<space> 
config>flows 
class 
classifier-profile 
classifier-profile<space> 
config>sys 
name 
name 
name 
config 
mgm 
No possibilities 
mgm 
config>flows 
flows# flow my-f 
my-flow-1 
my-flow-2  
my-flow-  
config>flows 
flows# flow my-flow-1 
my-flow-1 
my-flow-1<space>  
config>flows 
flows# flow my-flow-3 
No possibilities 
my-flow-3 
This is a new flow, as my-flow-3 did 
not exist before. 
3. Operation and Maintenance 
Interactive Help 
To get interactive help, type ?.  
In general, typing a ? directly after a string performs string completion, while typing <space> and then a 
? executes the command. 
When a <CR> appears in a ? list, the string you entered is itself a valid command needing no further 
additions. Pressing <Enter> executes the command or navigates to the indicated level. 
Typing ? immediately after a command or partial command with no space before the ?, tells Megaplex-4  
to display all possibilities for completing the string. Help output is always followed by the string you 
typed with the cursor at the end of the string waiting for input. 
config>flows# classifier-profile myclass m? 
match-any 
config>flows# classifier-profile myclass m 
admin# fact? 
factory-default-all             - Resets all configuration and counter 
factory-default                 - Loads factory default configuration 
admin# fact 
admin# factory-default? 
factory-default-all             - Resets all configuration and counters 
 <CR> 
admin# factory-default 
When a string cannot be completed, Megaplex-4 displays “cli error: Invalid Command”. 
admin# stac? 
# cli error: Invalid Command 
admin# stac 
 
file# da ? 
# cli error: Invalid Command 
file# da 
Typing <?> after a space between a command or level name and the ? tells Megaplex-4 to try to execute 
the command. The space tells the CLI that you are finished typing and to try to match the string to an 
appropriate command. The string does not have to be a complete command. 
If there is only one possible command starting with that string, pressing <Enter> will execute the 
command. If there is more than one command that starts with the string, the CLI displays a message 
that it can’t clarify which command you want. 
172_17_155_24>admin# factory? 
 
factory-default-all              - Resets all configuration and counters 
factory-default                  - Loads factory default configuration 
 
3. Operation and Maintenance 
A command followed by a ? without a space, shown above, returns a list of possible completions. The 
same command followed by a space and then the ? returns an ambiguous command message. This 
means the string entered could be completed to more than one command is therefore ambiguous, as 
shown below.  
172_17_155_24>admin# factory ? 
# cli error: Ambiguous Command 
172_17_155_24>admin# factory 
A string that is a complete command name followed by a space ? displays all possible command 
parameters. 
config>flows# show ? 
      summary                - Displays list of flows 
config>flows# show  
config>flows# classifier-profile ? 
 <classification-n*>  : [1..32 chars] 
config>flows# classifier-profile  
The next example shows a complete command to which a parameter could be appended. It also shows 
how a string that is a complete command is executed by pressing <CR>, or <Enter>. 
config>access-control# resequence access-list acl_1 ? 
 <CR> 
 <number>             : [0..100000] 
The next example shows a complete command that has no parameters. 
config>flows# classifier-profile myclass match-any ? 
 <CR> 
config>flows# classifier-profile myclass match-any  
 
Using Scripts 
CLI commands can be gathered into text files. They may be created using a text editor, by recording the 
user commands or by saving the current configuration. 
These files can be configuration files or scripts. Configuration files have specific names and contain CLI 
commands that Megaplex-4 can use to replace the current configuration, while scripts contain CLI 
commands that add to the current configuration. Configuration files can be imported from and exported 
to RAD devices via file transfer protocols. 
3. Operation and Maintenance 
Note 
Although scripts can be created using a text editor, it is recommended to save 
the configuration file and then edit it rather than write a script from scratch. 
The sequence of the commands is very important and if a script fails during 
startup at a certain command, the entire configuration file is discarded.  
For more information on configuration files, refer to the description in the Operation chapter. 
In order to execute a CLI script, you have to copy/paste it to the CLI terminal, or send it to Megaplex-4 
via the RADview Jobs mechanism, CLI script option. 
To execute a script, perform the commit command. 
3.9 GUI-Based Configuration 
The Standalone Shelf View is an SNMP-based, FCAPS-compliant element management application. It 
displays a dynamic graphic representation of the device panel(s), providing an intuitive, user-friendly 
GUI, including port and card interfaces and their operational and communication statuses.  
The Standalone Shelf View is distributed as an executable (*.exe) file accompanied by a readme file, 
complete with installation instructions. The application and readme file are available via RAD partners or 
RAD Support. Once you installed the application, a user guide is accessible via the Help button. 
3.10 SNMP-Based Network Management  
Preconfiguring Megaplex-4 for SNMP Management 
Megaplex-4 can be managed by any SNMP-based network management station, such as the RADview 
family of network management stations, provided IP communication is possible with the management 
station, as well as with the standalone RADview stations.  
To manage the Megaplex-4 from a remote NMS, it is necessary to preconfigure the basic parameters 
using a supervision terminal connected to the Megaplex-4 CONTROL DCE port. RAD recommends Layer-
3 management access via out-of-band Ethernet management port. 
3. Operation and Maintenance 
 To preconfigure Megaplex-4 for Layer-3 management access: 
1. Add a router interface, bind it to the SVI and add a static route to the next hop. 
Note 
The IP address must be configured to a value different from 1.1.1.x.  
2. Configure SNMPv3 parameters:  
 
OID tree visibility, mask and type 
 
Access group 
 
Trap report policy. 
Script below provides all necessary configuration steps. Replace IP addresses and entity names with 
values relevant for your network environment. 
### Defining the Router Interface#### 
configure 
router 1 interface 1 address 172.18.171.121/24 
router 1 interface 1 bind svi 1 
router 1 static-route 0.0.0.0/0 address 172.18.171.1 
exit all 
 
#*********************Configuring_SNMP_View/Mask/Type************************ 
configure management snmp 
view internet 1 
mask 1 
type included 
no shutdown 
exit all 
#**********************************End*************************************** 
 
#*********************Enabling_SNMP_V3*************************************** 
configure management snmp 
snmpv3 
no shutdown 
exit all 
#**********************************End*************************************** 
 
#*********************Configuring_SNMP_Access_Group************************ 
configure management snmp 
access-group initial usm no-auth-no-priv 
context-match prefix 
exit all 
#**********************************End*************************************** 
 
#**************************Configring_SNMP_Traps***************************** 
configure management snmp 
target-params p 
message-processing-model snmpv3 
version usm 
security name initial level no-auth-no-priv 
3. Operation and Maintenance 
no shutdown 
exit 
target a 
target-params p 
tag-list unmasked 
address udp-domain 172.17.176.35 
no shutdown 
exit 
notify unmasked 
tag unmasked 
no shutdown 
trap-sync-group 1  
 
exit all 
#**********************************End************************************ 
Configuring Management Access  
This section describes how to configure general management parameters. It also describes the 
command for selecting a subset of the supported SSH encryption algorithms, when using SSH 
management access.  
Note 
There is no explicit configuration for inband and outband management 
access.  
 To configure management access: 
• 
At the configure management access prompt enter the necessary commands according to the 
tasks listed below. 
Task 
Command 
Comments 
Allowing SFTP access 
sftp 
Typing no sftp blocks access by SFTP. 
Allowing SSH (Secure Shell) access 
ssh 
Typing no ssh blocks access by SSH. 
Selecting acceptable SSH encryption 
algorithms 
 
ssh-encryption {all | 
algorithm 
<algorithm-1> 
[algorithm-2] 
[algorithm-3] 
[aorithm-4] 
[algorithm-5] 
[algorithm-6]} 
Possible values: 
all – all algorithms are accepted 
(default) 
algorithm-1 to algorithm-6 – one of 
the following: aes-cbc-128, aes-cbc-
192, aes-cbc-256, aes-ctr-128, aes-ctr-
192, aes-ctr-256, 3des-cbc-168, arc4-
128, arc4-256 
Notes:  
3. Operation and Maintenance 
Task 
Command 
Comments 
• If all is selected, there is no need to 
select any algorithms, and if you 
do, your selection is ignored. 
• If the command is repeated, the 
latest instance replaces the 
previous one. 
• If all is not selected, you must 
select at least one algorithm. 
• If multiple algorithms are selected, 
they must be different ones. 
• The order of the algorithms is not 
important; usually the strongest is 
negotiated first. 
Selecting strong SSH key exchange algorithms 
 
ssh-key-exchange 
{all | algorithm 
<algorithm-1> 
[algorithm-2]} 
all – all algorithms are accepted 
(default) 
algorithm-1, algorithm-2 – at least 
one of the following algorithms is 
selected:  
• dh-group1-sha1: diffie-hellman-
group-exchange-sha1 
• dh-group14-sha1: diffie-hellman-
group14-sha1  
Entering ssh-key-exchange with at 
least one value enables the SSH key 
exchange for the specified algorithm. 
 
Notes:  
• If the command is repeated, the 
latest instance replaces the 
previous one. 
• If all is not selected, you must 
select at least one algorithm. 
• If multiple algorithms are selected, 
they must be different ones. 
The order of the algorithms is not 
important; usually the strongest is 
negotiated first. 
3. Operation and Maintenance 
Task 
Command 
Comments 
Selecting the authentication algorithm 
 
ssh-mac {all | 
algorithm 
<algorithm-1> 
[algorithm-2] 
[algorithm-3] 
[algorithm-4]} 
Possible values: 
all – all algorithms are accepted 
(default) 
algorithm-1 to algorithm-4 – one of 
the following: sha1-96, sha1-160, 
md5-96, md5-128 
Allowing SNMP access 
snmp 
Typing no snmp blocks access by 
SNMP. 
Allowing Telnet access (for IPv4 only) 
telnet 
Typing no telnet blocks access by 
Telnet. 
Allowing TFTP access 
tftp 
Typing no tftp blocks access by TFTP. 
Working with RADview  
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
Megaplex-4 works with EMS, SM and PM applications. Megaplex-4 older versions can be also managed 
by the RV-SC/TDM service management application. 
 
Warning 
To prevent conflicts and ensure a stable and consistent network setup, 
provision services using either RADview Service Manager or CLI, but not 
both simultaneously. 
The Megaplex-4 element and network management systems include a CORBA northbound interface, 
enabling easy integration into the customer’s umbrella NMS. CORBA enables interconnectivity and 
communication across heterogeneous operating systems and telecommunications networks. CORBA 
effectively supplies a software interface that defines data models used between various management 
layers. It supports multi-vendor distributed network management applications, providing the data 
interface between clients and servers. 
3. Operation and Maintenance 
For more details about the RADview network management software, and for detailed instructions on 
how to install, set up, and use RADview, contact your local RAD representative. 
Working with Other SNMP-Based NMS  
Megaplex-4 can be integrated into 3rd-party management systems at different levels: 
• 
Viewing device inventory and receiving traps (see Chapter 11 for trap list)   
• 
Managing device, including configuration, statistics collection, diagnostics, using standard and 
private MIBs:  
 
IANAifType-MIB 
 
IETF Syslog Device MIB  
 
IEEE8023-LAG-MIB 
 
MEF-R MIB 
 
RAD private MIB 
 
RFC 2819 (RMON-MIB) 
 
RFC 2863 (IF-MIB) 
 
RFC 3273 (Remote Network Monitoring MIB) 
 
RFC 3411  (SNMP-FRAMEWORK-MIB) 
 
RFC 3413 (SNMP-TARGET-MIB) 
 
RFC 3414 (SNMP-USER-BASED-SM-MIB) 
 
RFC 3415 (SNMP-VIEW-BASED-ACM-MIB) 
 
RFC 3418 (SNMPv2-MIB) 
 
RFC 3636 (MAU-MIB) 
 
RFC 4668 (RADIUS-AUTH-CLIENT-MIB) 
 
RFC 4836.MIB (MAU-MIB) 
 
RFC 3592 SONET MIB 
 
RFC 4805 DS1-MIB. 
3. Operation and Maintenance 
3.11 Turning Off the Unit 
 To turn the Megaplex-4 unit off: 
• 
Disconnect the power cord from the power source. 
 