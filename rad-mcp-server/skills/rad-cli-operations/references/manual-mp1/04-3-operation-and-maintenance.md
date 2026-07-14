# 3 Operation and Maintenance

*Manual `MP-1-mn_ver 2.2.pdf`, pages 92–129.*


## 3.1 Turning On the Unit  *(p.92)*


## 3.2 Indicators  *(p.92)*

This chapter: 
• 
Explains power-on and power-off procedures  
• 
Provides a detailed description of the front panel controls and indicators and their functions 
• 
Describes the startup sequence of Megaplex-1 
• 
Explains management and configuration options  
• 
Explains working with a terminal connected to the Megaplex-1 control port 
• 
Describes the command line interface (CLI) and using scripts. 
3.1 Turning On the Unit 
 To turn on Megaplex-1: 
• 
Connect the power cord to the mains. 
The PWR indicator lights up and remains lit as long as Megaplex-1 receives power. 
Megaplex-1 requires no operator attention once installed, with the exception of occasional monitoring 
of front panel indicators. Intervention is only required when Megaplex-1 must be configured to its 
operational requirements, or diagnostic tests are performed. 
3.2 Indicators 
The following drawings show LED indicators in various Megaplex-1 configurations. The table below 
describes the functions of the Megaplex-1 LED indicators. 
Megaplex-1 
3. Operation and Maintenance 
 
  
 
 
 
Megaplex-1 Front Panel Controls and Indicators  
Name 
Color 
State 
POWER SUPPLY PS1, 
PS2 
 Green 
On – the corresponding PS is on  
Off – the corresponding PS is off 
ON LINE 
 
Yellow/Gre
en 
Lights in yellow – Diagnostic loopback is active 
Lights in green – the device is online 
Off – the device is off 
ALM  
 
Red 
On – There is at least one active alarm in the device. 
Off – No active alarms are present in the device. 
Blinking – there is at least one critical or major alarm in the 
device.  
Ethernet Ports 
(User/Network/ 
Management) 
 
 
LINK  
Green 
On – Ethernet interface is synchronized. 
Off – Ethernet link is not detected 
ACT  
Yellow 
On – Data is being transmitted/received at the Ethernet link. 
Off –  ETH frames are not received and transmitted 
Station CLOCK Port 
 
 
Megaplex-1 
3. Operation and Maintenance 
Name 
Color 
State 
ON  
Green 
On –  the station clock port is configured as no shutdown 
Off –  the station clock port is configured as shutdown 
LOS  
Red 
On –  loss-of-signal (when station clock port configured as 
connected)  
Off – no loss-of-signal 
C37.94 Interface 
 
 
SYNC 
 Green/Red 
 
Lights steadily in green – the corresponding port is operating 
properly 
Flashes in green –the corresponding port is operating properly, 
but serves as the standby port when link protection is enabled 
Lights in red – the corresponding port detects loss of 
synchronization or loss of signal 
Flashes in red – the corresponding port serves as the standby 
port, and detects loss of synchronization 
REM SYNC 
 Yellow 
 
On – the corresponding port detects loss of remote 
synchronization 
Off – the corresponding port is not connected. 
FXS Interface 
 
 
LOC/REM 
Green/Yell
ow 
 
Lights steadily in green – Local “OFF-HOOK” 
Lights steadily in yellow – Remote “OFF-HOOK” 
Flashes in green/yellow – Local and Remote “OFF-HOOK” 
(conversation state) 
Off – port is not connected or both directions of signaling is 
“ON-HOOK” 
E&M Interface 
 
 
M 
Green 
On when the M line of the corresponding channel is off-hook 
(channel in use). 
E 
Green 
On when the E line of the corresponding channel is off-hook 
(channel in use) 
FD 
 
Push button for setting the unit to default configuration 
   

## 3.3 Startup  *(p.95)*

Megaplex-1 
3. Operation and Maintenance 
3.3 Startup  
Configuration and Software Files 
Software files are named sw-pack-1 and sw-pack-2. One of the software packs is designated as active. 
The following files contain configuration settings: 
• 
factory-default-config – contains the manufacturer default settings. At startup, 
factory-default-config is loaded if startup-config and user-default-config are missing or invalid. 
• 
running-config – contains the current configuration that the device is running. This file is deleted 
and rebuilt at device reboot. 
• 
startup-config – contains saved non-default user configuration. This file is not automatically 
created. You can use the save or copy command to create it. At startup, startup-config is loaded 
if it exists and is valid. 
• 
user-default-config – contains default user configuration. This file is not automatically created. 
You can use the copy command to create it. At startup, user-default-config is loaded if 
startup-config is missing or invalid.  
Note 
Configuration files should contain only printable ASCII characters (0x20–0x7E), 
<Enter> (0x0D), <Line Feed> (0x0A), and <Tab> (0x09).  
Refer to the File Operations section in the Administration chapter for details on file operations. 
Loading Sequence 
At startup, the device attempts to load configuration files in the following sequence until a valid one is 
found: 
• 
startup-config 
• 
user-default-config 
• 
factory-default-config 
If an error is encountered while loading a file, the default is to ignore the error and continue loading. 
You can use the on-configuration-error command to change this behavior, to either stop loading the file 
when the first error is encountered, or reject the file and reboot; after rebooting, the next file in the 
loading sequence is loaded). 

## 3.4 Working with Custom Configuration Files  *(p.96)*

Megaplex-1 
3. Operation and Maintenance 
To display the parameter values after startup, use the info [detail] command. 
3.4 Working with Custom Configuration Files 
In large deployments, often a central network administrator sends configuration files to the remote 
locations and all that remains for the local technician to do is to replace the IP address in the file or 
other similar minor changes, and then download the file to the device. Alternatively, the technician can 
download the file as is to the device, log in to the device and make the required changes, then save the 
configuration. 
To download the configuration file, use the copy command (refer to the Administration chapter). After 
downloading the configuration file, the unit must be reset in order to execute the file. After the unit 
completes its startup, the custom configuration is complete. 
Saving Configuration Changes 
You must save your configuration if you wish to have it available, as it is not saved automatically. 
You can save your configuration as follows: 
• 
Use the save command to save running-config as startup-config. 
• 
Use the copy command to copy running-config to startup-config or user-default-config. 
Additionally, some commands erase the configuration saved in startup-config by copying another file to 
it and then resetting the device. The following fugure indicates the commands that copy to 
startup-config, and whether the device resets after copying. 

## 3.5 Configuration and Management  *(p.97)*

Megaplex-1 
3. Operation and Maintenance 
 
Commands That Reset Device/Copy Configuration Files 
 To save the user configuration in startup-config: 
1. In any level, enter: save. 
2. At the file# prompt, enter: copy running-config startup-config. 
 To save the user default configuration in user-default-config:  
• 
At the file# prompt, enter: copy running-config user-default-config. 
3.5 Configuration and Management 
Usually, initial configuration of the management parameters is performed via an ASCII terminal. Once 
the management flows and corresponding router interface have been configured, it is possible to access 
Megaplex-1 via Telnet or SNMP for operation configuration. See Preconfiguring Megaplex-1 for SNMP 
Management for an example of management configuration. For details on configuring the router, refer 
to the Router section in the Traffic Processing chapter. 
The following table summarizes management options for Megaplex-1. 

## 3.6 Factory Default Push Button  *(p.98)*

Megaplex-1 
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
CONTROL 
Local 
Out-of-band 
RS-232 
Terminal emulation applications 
such as HyperTerminal, Procomm, 
Putty, SecureCRT, Tera Term (see 
Working with Terminal below) 
MNG-ETH 
Local, remote 
Out-of-band 
Telnet (IPv4 
only), SSH 
Terminal emulation application (see 
Working with Telnet and SSH 
below) 
SNMP 
RADview (see Working with 
RADview below) 
Third-party NMS (see Working with 
other SNMP-Based NMS below) 
Ethernet 
FE/GbE 
Local, remote 
Inband 
Telnet, SSH 
RADview (see Working with 
RADview below) 
Terminal emulation application (see 
Working with Telnet and SSH 
below) 
SNMP 
Third-party NMS (see Working with 
other SNMP-Based NMS below) 
 
Note 
By default, the terminal, Telnet (SSH) and SNMP management access methods 
are enabled. See Management Access Methods in Chapter 6 for details on 
enabling/disabling a particular method.  
 
3.6 Factory Default Push Button  
Megaplex-1 has an external push button for setting the unit’s software to its default.  
• 
The unit is restored to its factory default. 
• 
If the user default has been configured, the unit boots up with the user-default-config file.  

## 3.7 CLI-Based Configuration  *(p.99)*

Megaplex-1 
3. Operation and Maintenance 
 To reset the unit to its default configuration: 
• 
While the unit is up and running, press and hold the push button for five seconds.  
3.7 CLI-Based Configuration 
Working with Terminal 
Megaplex-1 has a V.24/RS-232 asynchronous DCE port, designated CONTROL, and terminated in a RJ-45 
connector. The control port continuously monitors the incoming data stream and immediately responds 
to any input string received through this port. You can use any terminal emulation program (such as 
HyperTerminal or PuTTY) to manage Megaplex-1 via the control port. The following procedure shows 
how to start a terminal control session using HyperTerminal. 
 To start a terminal control session: 
3. Make sure that Megaplex-1 is connected to a PC or laptop, as explained in Connecting to a 
Terminal section in the Installation and Setup chapter.  
4. Start the terminal emulation program. 
For example, start HyperTerminal by navigating to 
Start>Programs>Accessories>Communications>HyperTerminal. 
5. From the menu of the New Connection –HyperTerminal window that opens, create a new 
terminal connection by selecting File>New Connection, and in the Connection Description 
window that opens, assign a Name to the connection, and click OK. 
Megaplex-1 
3. Operation and Maintenance 
 
6. In the Connect To window that opens, in Connect using, select COM1, and then click OK. 
The Com Properties window opens. 
7. In the Com Properties window, configure the following laptop/PC communication port 
parameters, and then click OK. 
 
Bits per second (speed) – baud rate of 9.6 kbps (9600) 
 
Data bits – 8 bits/character 
 
Parity – no parity  
 
Stop bits – 1 stop bit  
 
Flow control – no flow control 
 
8. Configure character delay by navigating in the home page menu to File>Properties, and in the 
Serial Properties window that opens, clicking the Settings tab, and then the Ascii Setup button. 
Megaplex-1 
3. Operation and Maintenance 
In Character delay, select 10, and then click OK. The terminal input delay between characters is 
now at least 10 msec. 
 
9. Power-up Megaplex-1. 
The boot manager of Megaplex-1 starts, and displays a message that you can stop the auto-boot 
and enter the boot manager by pressing any key. A running countdown of the number of 
seconds remaining until auto-boot is displayed. If it reaches 0 before you press a key, then after 
a few seconds a message is displayed showing that the active software pack is being loaded. 
After a few more seconds, the login prompt is displayed. See Login for details on logging in.  
Megaplex-1 
3. Operation and Maintenance 
 
Working with Telnet and SSH 
Typically, the Telnet/SSH host is a PC or Unix station with the appropriate suite of TCP/IP protocols. 
Telnet is supported in IPv4 only.  
To enable the Telnet/SSH host to communicate with Megaplex-1, it is necessary to configure the 
Megaplex-1 IP address settings (refer to the Router section for details). This is usually done via a 
terminal emulation program (see Working with Terminal). After this preliminary configuration, you can 
use a Telnet/SSH host connected directly or via a local area network.  
The following procedure describes how to connect to Megaplex-1 via Telnet. You can connect to 
Megaplex-1 via SSH (more secure) using a program, such as PuTTY. 
 To connect to Megaplex-1 via Telnet: 
1. At the Telnet host, enter the necessary command (e.g. at a PC enter: 
telnet <IP-address>). 
The Telnet login window appears for the device as shown below. 
Megaplex-1 
3. Operation and Maintenance 
 
2. Log into the device as explained below. 
Login  
To prevent unauthorized modification of the operating parameters, Megaplex-1 supports various access 
levels. Refer to User Access for more information on the access levels, as well as a list of the default 
users defined in the device and information on configuring additional users.  
Logging In 
 To log in to Megaplex-1: 
1. At the user prompt (user>), enter the user name and press <Enter>.  
The password prompt (password>) appears. 
2. Enter the password (default is 1234) and press <Enter>. The number of password characters 
must be in the range of 1 to 20. 
The base prompt MP-1# appears.  
Note 
You can display a banner at login. Refer to the Administration chapter for 
details.  
Lost Superuser Password 
If you have lost your superuser password, contact Technical Support via the RADcare Online portal or by 
email. 
Megaplex-1 
3. Operation and Maintenance 
Using the CLI  
The CLI consists of commands organized in a tree structure of levels, starting at the base level. Each level 
(also referred to as context) can contain levels and commands (see Navigating for more information on 
the levels and commands available in Megaplex-1). The level is indicated by the CLI prompt. 
Note 
Most commands are available only in their specific context. Global commands 
are available in any context. You can type ? at any level to display the 
available commands.  
CLI Prompt 
The base level prompt contains the device name, which is MP-1 by default (the device name can be 
configured in the system level; refer to the Device Information section in this manual). The prompt ends 
with $, #, or >, depending on the type of entity being configured and the user level. 
If a new dynamic entity is being configured, the last character of the prompt is $. Examples of dynamic 
entities include flows, QoS profiles, and PW entities.  
If a new dynamic entity is not being configured, the last character of the prompt is > (for tech or user 
access levels) or # (for other access levels). 
Note 
The examples in this manual use # as the last character of the prompt, unless 
the creation of a new dynamic entity is being illustrated.  
After you type a command at the CLI prompt and press <Enter>, Megaplex-1 responds according to the 
command entered. 
Navigating 
To navigate down the tree, type the name of the next level. The prompt then reflects the new location. 
To navigate up, use the global command exit. To navigate all the way up to the root, type exit all.  
At the prompt, one or more level names separated by a space can be typed, followed (or not) by a 
command. If only level names are typed, navigation is performed and the prompt changes to reflect the 
current location in the tree. If the level names are followed by a command, the command is executed, 
but no navigation is performed and the prompt remains unchanged. 
Note 
To use show commands without navigating, type show followed by the level 
name(s) followed by the rest of the show command.  
In the following example, the levels and command were typed together and therefore no navigation was 
performed, so the prompt did not change. 
Megaplex-1 
3. Operation and Maintenance 
# configure system date-and-time date-format yyyy-mm-dd 
# show configure system system-date 
2017-06-10   15:08:20  UTC  +00:00 
# 
In the following example, the levels were typed separately and the navigation is reflected by the 
changing prompt. 
# configure 
config# system 
config>system# date-and-time 
config>system>date-time# date-format yyyy-mm-dd 
config>system>date-time# exit 
config>system# show system-date 
2017-06-10   15:13:23  UTC  +00:00 
 
config>system# 
Full-Path Command 
Full-path command allows you to enter a CLI command anywhere in the tree as if the current level was 
the CLI root, by preceding the command or level change with a backslash character. The device executes 
the command as if it were invoked from the CLI root. 
If you enter a level change (preceded by \) without a command, the CLI does not return to the prompt of 
the level that the command was invoked from, but remains at the changed level. For example, the MP-
1\configure system command, when invoked from any level in the CLI tree, returns the 
rados>config>system# prompt. However, if you enter a level change followed by a command, the 
system performs the command and then returns the prompt of the level that the command was invoked 
from. For example, if following the command admin>scheduler#, you type \configure 
system name my-device, the latter command sets the device name to my-device and then 
returns the prompt my-device>admin>scheduler#.  
Command Tree 
The tree command displays a hierarchical list of all the commands in the CLI tree, starting from the 
current context.  
 To view the entire CLI tree (commands only): 
1. At the root level, type tree.  
# tree 
| 
Megaplex-1 
3. Operation and Maintenance 
+---admin 
|   | 
|   +---factory-default-all 
|   | 
|   +---factory-default 
|   | 
|   +---reboot 
|   | 
|   +---scheduler 
|   |   | 
|   |   +---clear-finished-schedules 
more.. 
2. Press <Enter> to see more or <CTRL-C> to return to the prompt. 
When adding the detail parameter, the output also includes the parameters and values for each 
command. 
 To view the CLI tree including all parameters and values: 
1. Navigate to the required context by typing level names separated by a space and press <Enter>. 
2. Type tree detail and press <Enter>.  
MP-1# tree detail 
| 
+---admin 
|   | 
|   +---factory-default-all 
|   | 
|   +---factory-default 
|   | 
|   +---reboot 
|   | 
|   +---scheduler 
|   |   | 
|   |   +---clear-finished-schedules 
|   |   | 
|   |   +---clear-schedule-log 
|   |   | 
|   |   +---show scheduler 
|   |   | 
|   |   +---show scheduler-details 
|   | 
|   +---software 
|   |   | 
Megaplex-1 
3. Operation and Maintenance 
|   |   +---install {sw-pack-1|sw-pack-2} 
|   |   +---undo-install 
|   |   | 
|   |   +---show status 
|   | 
|   +---user-default 
|   | 
|   +---show reboot 
| 
+---configure 
|   | 
|   +---access-control 
|   |   | 
|   |   +---access-list [ipv4] <acl-name> 
|   |   |   no access-list <acl-name> 
|   |   |   | 
|   |   |   +---delete <sequence-number> 
| 
more..  
3. Press <Enter> to see more or <CTRL-C> to return to the prompt. 
Command Structure 
CLI commands have the following basic format: 
command [parameter]{ value1 | value2 | … | valuen } 
[ optional-parameter <value> ]  
 
where: 
{} 
Indicates that one of the values must be selected 
[] 
Indicates an optional parameter 
<> 
Indicates a value to be typed by the user according to parameter 
requirements 
You can type only as many letters of the level, command, or parameter as required by the system to 
identify it. For example, you can enter config manag to navigate to the management level. 
To finish configuration changes, type commit. If this command is performed successfully, OK is 
displayed. Otherwise, Megaplex-1 displays the relevant error message. 
To verify whether the applied configuration changes are valid (before applying commit), use the sanity-
check command. 
Megaplex-1 
3. Operation and Maintenance 
You can remove all configuration activity after the last commit command using the discard-changes 
command. 
Special Keys 
The following keys are available at any time: 
? 
List all commands and levels available at the current level. 
<Tab> 
Command-line completion; complete the unambiguous characters 
of the command, and display a list of available commands 
beginning with those characters (as when pressing ?). 
↑ 
Display the previous command (history forward). 
↓ 
Display the next command (history backward). 
<Backspace> 
Delete character before cursor. 
<Delete> 
Delete character before cursor. 
<- 
Move cursor one character left. 
-> 
Move cursor one character right. 
<Alt>+B, <Esc>+B 
Move cursor left one word (or go to start of word). 
<Alt>+D, <Esc>+D 
Delete until end of word starting from the cursor. 
<Alt>+F, <Esc>+F 
Move cursor right one word (or go to end of word). 
<Ctrl>+<_> 
or 
<Ctrl>+<Shift>+<-> 
Exit CLI. 
<Ctrl>+A 
Move cursor to start of line. 
<Ctrl>+B 
Move cursor one character left. 
<Ctrl>+C 
Interrupt current command. 
<Ctrl>+D 
Delete character to right of cursor. 
<Ctrl>+E 
Move cursor to end of line. 
<Ctrl>+G 
Return to upper level. 
<Ctrl>+H 
Delete character to left of cursor. 
<Ctrl>+K 
Delete text from cursor to end of line. 
<Ctrl>+L 
Redisplay current line. 
<Ctrl>+P 
Display the previous command (history forward). 
<Ctrl>+Q 
Resume transmission (XON). 
Megaplex-1 
3. Operation and Maintenance 
<Ctrl>+S 
Pause transmission (XOFF). 
<Ctrl>+U 
Delete text up to cursor. 
<Ctrl>+W 
Delete word to the left of cursor. 
<Ctrl>+Y 
Paste text last deleted by a shortcut. 
<Ctrl>+Z 
Navigate to base level. 
Getting Help 
You can get help in the following ways: 
• 
Type help to display general help (see General Help). 
• 
Type help <command> to display information on a command and its parameters (see Command 
Help). 
• 
Type ? to display the commands available in the level (see Level Help). 
• 
Use <Tab> while typing commands and parameters, for string completion (see Command-Line 
Completion). 
• 
Use ? after typing a command or parameter, for interactive help (see Interactive Help). 
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
Output modifiers for filtering output 
• 
URLs for device manual and shelf view manual 
Example of help command output from the root level: 
1. Full help - 'help <cmd>'. 
2. To complete level name, command, keyword, argument - <tab> ('conf<tab>' => 
    'configuration'). 
3. To display all currently valid levels, commands, keywords or arguments - 
   '?' ('name ?' => '<name-of-device>'). 
Commands and levels: 
      admin                            + Adminstrative commands 
Megaplex-1 
3. Operation and Maintenance 
      clear-statistics                 - Clear all statistics 
      configure                        + Configure device 
      debug                            + 
      file                             + File commands 
      logon                            - Allows to logon to debug level 
      on-configuration-error           - Determines the device behavior when 
                                         encountering an error in configuration 
                                         file 
Global commands: 
      copy                             - Copy file 
      echo                             - Displays a line of text (command) on 
                                         the screen 
      exec                             - Execute script of CLI commands 
      exit                             - Returns to the next higher command 
                                         level (context) 
      help                             - Displays information regarding commands 
                                          in the current level 
      history                          - Displays the history of commands issued 
                                          since the last restart 
      info                             - Displays the current device 
                                         configuration 
      level-info                       - Displays the current device 
                                         configuration - commands from the 
                                         current level only 
      logout                           - Logs the device off 
      ping                             - Ping request to verify reachability of 
                                         remote host 
[no] popup-suspend                    - Suspends popup messages 
      save                             - Save current settings 
[no] schedule                         - Schedule a command to run in a future 
                                         time 
      telnet                           - Open telnet client session 
      trace-route                      - Checks the path connectivity to a 
                                         remote device 
      tree                             - Displays the command levels from the 
                                         current context downwards 
Hotkeys: 
      Ctrl-H, Del, Backspace            -Delete character left of cursor 
      Ctrl-D                            -Delete character right of cursor 
      Ctrl-U                            -Delete text up to cursor 
      Ctrl-K                            -Delete text from cursor to end of line 
      Ctrl-W                            -Delete word left of cursor 
      Alt-D, Esc-D                      -Delete word right of cursor 
      Ctrl-Y                            -Paste last deleted text 
      Tab                               -Completion token 
      ?                                 -Interactive help token 
      Ctrl-P, Up arrow                  -History forward 
      Down arrow                        -History backward 
      Ctrl-B, Left arrow                -Move cursor left one character 
      Right arrow                       -Move cursor right one character 
      Ctrl-A                            -Move cursor to beginning of line 
      Ctrl-E                            -Move cursor to end of line 
      Alt-B, Esc-B                      -Move cursor left one word 
      Alt-F, Esc-F                      -Move cursor right one word 
Megaplex-1 
3. Operation and Maintenance 
      Ctrl-L                            -Redisplay current line 
      Ctrl-S                            -Pause transmission (XOFF) 
      Ctrl-Q                            -Resume transmission (XON) 
      Ctrl-C                            -Interrupt current command 
      Ctrl-G                            -Return to upper level 
      Ctrl-Z                            -Return to CLI root 
      Ctrl-_                            -Exit CLI 
Output Modifiers (usage: 'command | modifier'): 
      begin <regular-expression>      -Start printing once expression found 
      exclude <regular-expression>    -Print lines not containing expression 
      include <regular-expression>    -Print lines containing expression 
Show commands can be printed repeatedly by appending 'refresh' to them 
 
Command Help 
Enter help <command> to display command and parameter information. 
config>system# help name 
 - name <name-of-device> 
 - no name 
 <name-of-device>  : Adds free text to specify the device name [0..255 chars] 
Level Help 
Enter ? at the command prompt to display the commands available in the current level. 
file# ? 
      delete                           - Delete file 
      dir                              - Display file directory 
 
 show banner-text                      - Display banner 
 show configuration-files              - Display configuration files 
                                          properties 
 show copy                             - Display Copy progress 
 show factory-default-config           - Display factory-default-config 
 show schedule-log                     - Display schedule-log 
 show startup-config                   - Display startup-config 
 show sw-pack                          - Display SW packs 
 show user-default-config              - Display user-default-config 
Command-Line Completion 
Command-line completion saves you command-line entry time and reminds you the syntax of 
command-line entities (levels, commands, parameters, flows, and profiles).  
In a command-line, Megaplex-1 completes command-line entities, when you press <Tab> immediately 
following a string (one or more characters). 
Megaplex-1 
3. Operation and Maintenance 
Some user-defined entity names, such as flow names or profile names, can be completed as well. If you 
enter an entity name (flow, profile, or similar) that does not exist in the database, Megaplex-1 creates 
this entity with the selected name.  
• 
If the command-line entity name can be completed in only one way, when you press <Tab>, 
Megaplex-1 autocompletes the entire name and appends a space. 
• 
If the command-line entity name can be completed in more than one way, Megaplex-1 appends 
the characters that are common to all possibilities, and displays a list of the completion 
possibilities beginning with those characters.  
• 
If the string is already a complete entity name (level/command/parameter/flow/profile) or 
cannot be completed to a complete name, no completion is done. 
• 
Pressing <Tab> following a complete command name (followed by a space), displays a list of 
available command arguments, if they exist (same behavior as ?). 
• 
Pressing <Tab> following a string and a space returns a CLI error: Ambiguous Command. This is 
because the string entered could be completed to more than one command and is therefore 
ambiguous. 
• 
Pressing <Tab> at the beginning of a command line behaves like a regular tab, and unlike ?, does 
not display a list of available commands. 
The following tables show examples of string completion.  
String Completion 
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
show 
configuration-files<space> 
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
flows# flow my-
flow-1 
my-flow-1 
my-flow-1<space>  
Megaplex-1 
3. Operation and Maintenance 
Level 
String  
Possibilities for Completion 
Result After Pressing <Tab> 
config>flows 
flows# flow my-
flow-3 
No possibilities 
my-flow-3 
This is a new flow, as my-
flow-3 did not exist before. 
Interactive Help 
To get interactive help, type ?. 
In general, typing a ? directly after a string displays possibilities for string completion, while typing 
<space> and then a ? displays possibilities of the next argument. 
When a <CR> appears in a ? list, the string you entered is itself a valid command needing no further 
additions. Pressing <Enter> executes the command or navigates to the indicated level. 
Typing ? immediately after a command or partial command with no space before the ?, tells Megaplex-1 
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
When a string cannot be completed, Megaplex-1 displays “cli error: Invalid Command”. 
admin# stac? 
# cli error: Invalid Command 
admin# stac 
 
file# da ? 
# cli error: Invalid Command 
file# da 
Typing <?> after a space between a command or level name and the ? tells Megaplex-1 to display 
possibilities of the next argument. If the string preceding the ? is ambiguous or invalid, an explanatory 
message is displayed. The string does not have to be a complete command. 
Megaplex-1 
3. Operation and Maintenance 
If there is only one possible command starting with that string, pressing <Enter> will execute the 
command. If there is more than one command that starts with the string, the CLI displays a message 
that it can’t clarify which command you want. 
admin# factory? 
 
factory-default-all              - Return to factory default and 
reboot 
factory-default                  - Loads factory default configuration 
A command followed by a ? without a space, shown above, returns a list of possible completions. The 
same command followed by a space and then ? returns an ambiguous command message. This means 
the string entered could be completed to more than one command and is therefore ambiguous, as 
shown below.  
admin# factory ? 
# cli error: Ambiguous Command 
admin# factory 
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
Scheduling CLI Commands  
You can schedule the execution of CLI commands at a future date and time. By default, no scheduling is 
configured. 
Megaplex-1 
3. Operation and Maintenance 
The global schedule command is used to configure the scheduling of a command. You can specify any 
command to be scheduled except the logout command.  
When you schedule a command, before saving it, Megaplex-1 prefixes the command with the path from 
which the schedule command was executed. To specify a CLI command with a full CLI level path, you 
should schedule it at the CLI root level. 
To save the scheduled command, type commit. 
Megaplex-1 tests the command that is configured as scheduled in the same way that it would be tested 
when executed; if the tests fail, you are notified of this, but the command is still scheduled, since it may 
be valid when the scheduled time arrives. 
The following types of schedules can be configured: 
In <minutes> 
Executed once, after the specified number of minutes. This type of 
schedule is not saved in nonvolatile (permanent) Megaplex-1 
memory; it is deleted at device reboot whether or not it was 
executed. 
At <date-and-time> 
Executed once at the specified date and time. This type of schedule 
can be optionally saved in permanent memory, in order to be 
available after device reboot. 
Note 
Schedules for date and time are saved in system local time. If the local time 
changes, Megaplex-1 does not modify the schedules to compensate for the 
change; therefore, changing the time can cause schedules to be executed 
twice or not executed at all.  
Schedules are marked as finished after they are executed.  
When executing scheduled commands, Megaplex-1 assumes a Yes answer for any confirmation 
questions. When a scheduled command is executed, it is sent to TACACS+ and Syslog accounting, as if it 
were executed by a CLI user.  
Configuring Command Scheduling 
 To schedule a command: 
• 
In any level, enter the schedule command according to the type of schedule: 
 
In <minutes> – Enter: 
schedule <name> in <minutes> “<command>” 
Megaplex-1 
3. Operation and Maintenance 
The schedule is saved with its name set to <name>, and the specified <command> is executed 
after the specified amount of <minutes> has elapsed, regardless of changes to the local system 
time.  
Range for <minutes>: 1–14400 [10 days] 
 
At <date-and-time> – Enter: 
schedule <name> at {january | february | march | april | may | june | july | august | 
september | october | november | december} <dd> <yyyy> <hh>:<mm> <command> 
[volatile | nonvolatile] 
The schedule is saved with its name set to <name> (in permanent memory if nonvolatile was 
specified), and the specified <command> is executed at the specified date and time. If the local 
system time is changed after the schedule is configured, the scheduled command might not be 
executed, or might be executed twice. 
Note 
An invalid date and time is not allowed; however, a date and time in the past 
is allowed; a schedule with its date and time in the past will never be executed 
unless the device date/time is changed such that the schedule date and time is 
no longer in the past 
 
Note 
Schedules can be added or deleted, but not changed. If you wish to change the 
details of a schedule, you have to delete it and then recreate it with the 
changes.  
 To delete schedules: 
• 
To delete a specific schedule, in any level enter: 
no schedule <name> 
• 
To delete all finished schedules, navigate to the admin scheduler level and enter: 
clear-finished-schedules 
Viewing Scheduling Information 
You can view the following scheduled information: 
• 
Commands, with or without details of the commands 
• 
Daylight saving time (For an explanation on the configuration of daylight saving time, refer to 
the Daylight Saving Time section in Chapter 9.) 
Note 
You can also enter the info command from the root of the device to view all 
commands of the device, including scheduled commands (see Viewing the 
Device Configuration section below).  
Megaplex-1 
3. Operation and Maintenance 
 To view scheduling without command details: 
• 
Navigate to the admin scheduler level and enter: 
show scheduler 
# admin scheduler 
admin>scheduler# show scheduler 
Current Time: 27 December 2014 00:01 (UTC +2) 
 
Schedule Name                     Type       Prm  Fin  Activation 
----------------------------------------------------------------------
----- 
sched-1                           Once (In)  No   No   1 day, 02:00:10 
sched-2                           Once (At)  Yes  Yes  -- 
sched-n                           Once (At)  Yes  No   1 October 2015 
12:21 
 
Summer Time 
Start (Recurring): Last Sunday of May, 02:00 
End   (Recurring): Last Thursday of October, 02:00 
Offset           : 60 minutes 
Start       : 31 May 2015 12:21 
End         : 25 October 2015 12:21 
 To view scheduling with command details: 
• 
Navigate to the admin scheduler level and enter: 
show scheduler-details 
# admin scheduler 
admin>scheduler# show scheduler-details 
Current Time: 16 September 2014 10:45 (UTC +2) 
Schedule Name               : sched-1 
Type                        : Once (At) 
Permanent                   : Yes 
Finished                    : No 
Activation (Local Time)     : 22 March 2015 09:00 
Activation In(Seconds)      : 186 days 22:45:00 
Command: copy log tftp://1.1.1.1 
 
Schedule Name               : sched-2 
Type                        : Once (In) 
Permanent                   : No 
Finished                    : No 
Activation In(Seconds)      : 207 days 12:45:00 
Megaplex-1 
3. Operation and Maintenance 
Command: copy log tftp://1.1.1.1 
 
Summer Time 
Start (Recurring): Last Sunday of May, 02:00 
End   (Recurring): Last Thursday of October, 02:00 
Offset           : 60 minutes 
Start       : 31 May 2015 12:21 
End         : 29 October 2015 12:21 
 
Parameter 
Description 
Current Time 
Current date and time, and current offset from UTC 
Schedule Name 
Name of schedule 
Type  
Type of schedule: 
• Once (In) – to be executed in specified number of minutes 
• Once (At) – to be executed at a specified date and time 
Prm/Permanent 
Indicates if schedule is saved in permanent memory 
Fin/Finished 
Indicates if schedule is marked as finished 
Activation 
In output of show scheduler, indicates the amount of time before the scheduled 
command will be executed, according to the type of schedule: 
• Once (In) – Amount of time before the scheduled command will be executed, in the 
form <hh:mm:ss>, <1 day hh:mm:ss> or <ddd days, hh:mm:ss> 
• Once (At) – Date and time at which the scheduled command will be executed 
• For either type, -- is displayed if the schedule is marked as finished. 
Activation (Local 
Time) 
In output of show scheduler-details for schedule type Once (At), displays the date and 
time at which the scheduled command will be executed. 
Activation In 
(Seconds) 
In output of show scheduler-details for schedule types Once (In) and Once (At), displays 
the amount of time before the scheduled command will be executed. 
Command 
In output of show scheduler-details, displays the scheduled command. 
Start (Date) 
For one-shot daylight saving time scheduling, displays daylight saving time start date and 
time. 
End (Date) 
For one-shot daylight saving time scheduling, displays daylight saving time end date and 
time. 
Start (Recurring) 
For recurring daylight saving time scheduling, displays the configured week of the 
month, weekday, month, and time for daylight saving time start. 
Megaplex-1 
3. Operation and Maintenance 
Parameter 
Description 
End (Recurring) 
For recurring daylight saving time scheduling, displays the configured week of the 
month, weekday, month, and time for daylight saving time end. 
Start 
For recurring daylight saving time scheduling: 
• If the device is currently not in daylight saving time, displays the next scheduled date 
and time for daylight saving time to start. 
• If the device is currently in daylight saving time, displays the date and time at which 
the daylight saving time started. 
End 
For recurring daylight saving time scheduling, displays the next scheduled date and time 
for daylight saving time end. 
Configuration Errors 
The following table lists the messages generated by the device when a command scheduling 
configuration error is detected. 
Configuration Error Messages 
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
Warning: Scheduled 
command failed sanity 
The command that you specified to 
schedule may fail when executed. 
Check the command; if changes are 
needed, delete the schedule and 
re-enter it with the changed 
command. 
The logout command 
may not be scheduled 
You specified the logout command as 
the command to schedule. 
None; Megaplex-1 does not allow 
the logout command to be 
scheduled. 
Viewing the Device Configuration 
You can enter the info command at the device root, to view all commands that have been configured for 
the device. This includes scheduled commands, as they are global commands. See an example in the 
Examples below. 
 To view commands of a device: 
• 
At the device root, type info.  
Megaplex-1 
3. Operation and Maintenance 
Refreshing Output 
You can specify that Megaplex-1 should periodically refresh the output of a show command. 
 To periodically refresh the output of a show command: 
• 
Append refresh [<sec>] to the command. The allowed range for <sec> is 3–100 seconds 
(default is 5 seconds). 
Megaplex-1 enters refresh mode and displays the output of the command periodically, along 
with an indication of how to exit refresh mode, at the interval specified by <sec>. You cannot 
enter any commands while Megaplex-1 is in refresh mode. 
To exit refresh mode, type <ESC> or <Ctrl>+C. 
The example below shows the result of refreshing the status of an Ethernet port every 15 seconds, and 
typing <Ctrl>+C after the status is displayed twice. 
Note 
The example uses a slot number to reference the port, which may not be 
applicable to every device.  
MP-1>config>port>eth(0/1)# show status refresh 15 
Name                  : ETH 0/1 
Administrative Status : Down 
Operational Status    : Down 
Connector Type        : SFP Out 
Auto Negotiation      : Configuring 
Flow Control          : Enabled Receive 
MAC Address           : 00-20-D2-BF-61-38 
To exit the refresh-mode press ESC or Ctrl+C 
 
Name                  : ETH 0/1 
Administrative Status : Down 
Operational Status    : Down 
Connector Type        : SFP Out 
Auto Negotiation      : Configuring 
Flow Control          : Enabled Receive 
MAC Address           : 00-20-D2-BF-61-38 
To exit the refresh-mode press ESC or Ctrl+C 
Filtering Output 
Some commands, such as info and show display large amounts of information as their output. It is 
possible to control the type and amount of information displayed, by filtering the output. 
Megaplex-1 
3. Operation and Maintenance 
To filter a command’s output, append to the command: 
 | [include | exclude | begin] <filter-expression> 
Keyword 
Description 
include 
The output includes only lines that match the filter expression. 
exclude 
The output includes only lines that do not match the filter 
expression. 
begin 
The output starts with the first line that matches the filter 
expression and continues with all further lines. 
<filter-expression> 
A filter expression is a regular expression that defines what to 
exclude, include or match at the beginning. Filter expressions can 
contain letters, numbers, and metacharacters (see below). Filter 
expressions are case sensitive. 
One and only one keyword is allowed. If no keyword is specified, no filtering is performed. 
The following example illustrates filtering output. 
config>system# info detail | include date 
    date-and-time 
        date-format yyyy-mm-dd 
Metacharacters 
Metacharacters are characters with special meaning. They allow you to define filter criteria, while not 
being part of the filter criteria themselves. Some are placeholders or wildcards. Some allow you to 
define ranges of characters to either include or exclude. You can construct complex filter expressions to 
see the exact output you want. Filter metacharacters are: 
 
Metacharacte
r 
Description 
Example 
. 
Matches any single character. 
r.t matches the strings rat, rut, and r t, but 
not root. 
$ 
Matches the end of a line. 
device$ matches the end of the string header 
device but not the string header 
device-name. 
^ 
Matches the beginning of a line. 
^device matches the beginning of the string 
device loaded from but not the string header 
device-name. 
Megaplex-1 
3. Operation and Maintenance 
Metacharacte
r 
Description 
Example 
* 
Matches zero or more occurrences 
of the preceding character.  
.* means match any number of any 
characters. 
\ 
This character is used to treat the 
following metacharacter as an 
ordinary character. 
\$ is used to match the $ character rather 
than match the end of a line. 
\. is used to match a period rather than 
match any single character. 
[ ]  
[c1-c2]  
[^c1-c2] 
Matches any one of the characters 
between the brackets. 
Ranges of characters are specified by 
a beginning character (c1), a hyphen, 
and an ending character (c2); 
multiple ranges can be specified as 
well. 
To match any character except those 
in the range, use ^ as the first 
character after the opening bracket. 
r[aou]t matches rat, rot, and rut, but not ret. 
[0-9] matches any digit. 
[A-Za-z] matches any upper or lower case 
letter. 
[^269A-Z] matches any character except 2, 6, 
9, and uppercase letters. 
| 
Logical OR two conditions together 
(band|comp) matches the lines bandwidth 
cir 999936 cbs 65535 and compensation 0. 
+ 
Matches one or more occurrences of 
the character or filter expression 
immediately preceding it. 
9+ matches 9, 99, and 999 
“” 
Matches the string enclosed in the 
quotation marks. The string may 
include spaces. See Regular 
Expression Syntax. 
“e s” matches "double star" 
{i}  
{i,j} 
Matches a specific number (i) or 
range (i through j) of instances of the 
preceding character. 
A[0-9]{3} matches A followed by exactly 
three digits, i.e. it matches A123 but not 
A1234. 
[0-9]{4,6} matches any sequence of 4, 5, or 6 
digits. 
Regular Expression Syntax 
A filter expression is a regular expression. A regular expression can be composed of characters and 
metacharacters. Any combination of metacharacters can be used. If you want spaces as part of the filter 
expression, enclose the expression with quote metacharacters. All characters found after a space not 
enclosed by quotes are ignored by the CLI. 
Megaplex-1 
3. Operation and Maintenance 
The following table provides some example of regular expressions and the resulting string that will be 
used to filter the CLI output. 
Examples of Regular Expression Syntax 
Regular Expression 
Resulting Filter String 
“str” 
str 
“s t r” 
s t r 
“str 
“str 
“str\”str” 
str”str 
“str\”str 
“str\”str 
“str”str 
str 
\”str” 
\”str” 
“str1” | include str2 
First expression – str1, second expression – str2 
 
Enabling Entities 
Some dynamic entities are created as inactive by default. After the configuration is completed, the 
no shutdown command activates the entity, as shown below. 
#*******Configure SVI 
configure port svi 1 
  no shutdown 
  exit all 
 
#*******Configure bridge  
configure bridge 1 
  vlan-aware 
 
#*******Configure bridge ports 
  port 1 
     no shutdown 
    exit 
  port 2 
    no shutdown 
    exit 
  port 3 
    no shutdown 
    exit 
  port 4 
Megaplex-1 
3. Operation and Maintenance 
    no shutdown 
    exit 
 
#*******Configure VLANs 
  vlan 51 
    exit 
  vlan 100 
    exit 
  vlan 200 
    exit all 
The shutdown command is also used to deactivate/disable a hardware element (such as a port), while 
no shutdown enables/activates it. 
Using Scripts 
CLI commands can be gathered into text files. They may be created using a text editor, by recording the 
user commands or by saving the current configuration. 
These files can be configuration files or scripts. Configuration files have specific names and contain CLI 
commands that Megaplex-1 can use to replace the current configuration, while scripts contain CLI 
commands that add to the current configuration. Configuration files can be imported from and exported 
to RAD devices via file transfer protocols. 
For more information on configuration files, refer to the description in the Operation chapter. 
In order to execute a CLI script, you have to copy/paste it to the CLI terminal, or send it to Megaplex-1 
via the RADview Jobs mechanism, CLI script option. 
To execute a script, perform the commit command. 
Examples 
 To schedule copying a log file in two hours: 
schedule sched-copy-2hrs in 120 “copy log tftp://1.1.1.1” 
 To schedule copying a log file on April 2 at 6:00, with the schedule saved in permanent memory: 
schedule sched-copy-Apr2 at april 2 2015 06:00 “copy log 
tftp://1.1.1.1” permanent 

## 3.8 GUI-Based Configuration  *(p.125)*

Megaplex-1 
3. Operation and Maintenance 
save 
 To schedule shutdown of the device in five minutes: 
config>flows>flow(v100in)$ schedule sched1 in 5 “shutdown”  
 To display commands configured for the device:  
# info 
. 
Bridge Configuration 
        bridge 1 
            name "BRIDGE 1" 
            echo "Bridge Port Configuration" 
#           Bridge Port Configuration 
            port 1 
                no shutdown 
                exit 
                no shutdown 
            exit 
            port 2 
                no shutdown 
                exit 
                no shutdown 
            exit 
#  
3.8 GUI-Based Configuration 
The Standalone Shelf View is an SNMP-based, FCAPS-compliant element management application. It 
displays a dynamic graphic representation of the device panel(s), providing an intuitive, user-friendly 
GUI, including port and card interfaces and their operational and communication statuses.  
 
The Standalone Shelf View is distributed as an executable (*.exe) file accompanied by a readme file, 
complete with installation instructions. The application and readme file are available via RAD partners or 
RAD Support. Once you installed the application, a user guide is accessible via the Help button. 
 

## 3.9 SNMP-Based Network Management  *(p.126)*

Megaplex-1 
3. Operation and Maintenance 
3.9 SNMP-Based Network Management  
Preconfiguring Megaplex-1 for SNMP Management 
Megaplex-1 can be managed by any SNMP-based network management station, such as via the 
RADview family of network management stations, provided IP communications is possible with the 
management station, as well as by the standalone RADview stations. 
To manage Megaplex-1 from a remote NMS, it is necessary to preconfigure the basic parameters using a 
supervision terminal connected to the Megaplex-1 CONTROL port.  
 To configure Megaplex-1 for management access: 
1. Add an SVI port. 
2. Create classifier profiles for matching all traffic and matching untagged traffic. 
3. Add a flow connecting the out-of-band Ethernet management port and the SVI. 
4. Add a router interface and bind it to the SVI. 
The following script provides the necessary configuration steps for Megaplex-1. Replace IP addresses 
and entity names with values suitable for your network environment. 
#************************Adding_SVI**************************** 
config port  
  svi 99  
    no shutdown 
exit all 
 
#*********************Adding Classifier_Profiles***************  
config flows 
  classifier-profile all match-any match all 
   
#**********************Configuring_Flows*********************** 
  flow mng_oob 
    classifier all 
     
    ingress-port mng-ethernet 0/0  
    egress-port svi 1 
     reverse 
    no shutdown 
  exit  
 
Megaplex-1 
3. Operation and Maintenance 
   
exit all 
#******************Configuring_Router_Interface**************** 
configure router 1 
  interface 1 
    bind svi 99 
    address 172.18.141.39/24 
    no shutdown 
  exit 
  exit all 
commit 
save 
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
Enabling the SFTP server 
sftp-server 
Typing no sftp-server disables the SFTP server. 
The SFTP server is disabled by default. 
Selecting acceptable SSH encryption 
algorithms 
ssh-encryption {all | 
algorithm 
<algorithm-1> 
[algorithm-2] 
[algorithm-3] 
[algorithm-4] 
[algorithm-5] 
[algorithm-6]} 
Possible values: 
all – all algorithms are accepted (default) 
algorithm-1 to algorithm-6 – one of the 
following: aes-cbc-128, aes-cbc-192, aes-cbc-
256, aes-ctr-128, aes-ctr-192, aes-ctr-256, 3des-
cbc-168, arc4-128, arc4-256 
Notes:  
Megaplex-1 
3. Operation and Maintenance 
Task 
Command 
Comments 
• If all is selected, there is no need to select 
any algorithms, and if you do, your selection 
is ignored. 
• If the command is repeated, the latest 
instance replaces the previous one. 
• If all is not selected, you must select at least 
one algorithm. 
• If multiple algorithms are selected, they must 
be different ones. 
• The order of the algorithms is not important; 
usually the strongest is negotiated first. 
Selecting the authentication 
algorithm 
 
ssh-mac {all | 
algorithm 
<algorithm-1> 
[algorithm-2] 
[algorithm-3] 
[algorithm-4]} 
Possible values: 
all – all algorithms are accepted (default) 
algorithm-1 to algorithm-4 – one of the 
following: sha1-96, sha1-160, md5-96, md5-128 
Allowing SNMP access 
snmp 
Typing no snmp blocks access by SNMP. 
Allowing Telnet access (for IPv4 
only) 
telnet 
Typing no telnet blocks access by Telnet. 
Allowing TFTP access 
tftp 
Typing no tftp blocks access by TFTP. 
Working with RADview 
RADview is a Windows-based modular, client-server, scalable management system that can be used in a 
distributed network topology or a single-station configuration. RADview consists of the main system 
(EMS) and the following optional modules: 
• 
Service Manager (SM) – end-to-end Carrier Ethernet service provisioning for Ethernet Access 
products. This module includes the Service Center (SC) module, which is an end-to-end Carrier 
Ethernet and TDM service provisioning for CI (Critical infrastructure) products.  
• 
Performance Monitor (PM) – portal for service SLA monitoring for both carriers and their 
customers. 
Megaplex-1 works with EMS, SM and PM applications. 

## 3.10 Turning Off the Unit  *(p.129)*

Megaplex-1 
3. Operation and Maintenance 
 
Warning 
To prevent conflicts and ensure a stable and consistent network setup, 
provision services using either RADview Service Manager or CLI, but not 
both simultaneously. 
 
The Megaplex-1 element and network management systems include a CORBA northbound interface, 
enabling easy integration into the customer’s umbrella NMS. CORBA enables interconnectivity and 
communication across heterogeneous operating systems and telecommunications networks. CORBA 
effectively supplies a software interface that defines data models used between various management 
layers. It supports multi-vendor distributed network management applications, providing the data 
interface between clients and servers. 
For more details about the RADview network management software, and for detailed instructions on 
how to install, set up, and use RADview, contact your local RAD partner. 
Working with other SNMP-Based NMS 
Megaplex-1 can be integrated into third-party network management systems at the following levels: 
• 
Viewing device inventory and receiving traps (refer to the Monitoring and Diagnostics chapter 
for trap list)   
• 
Managing device, including configuration, statistics collection, and diagnostics.  
3.10 Turning Off the Unit 
 To power off the unit: 
• 
Remove the power cord from the power source. 