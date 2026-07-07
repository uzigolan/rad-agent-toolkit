# 4 Configuration and Management

*Manual `SecFlow-1p_6.4_Mn_05-26_GA.pdf`, pages 139–222.*


## 4.1 CLI-Based Configuration  *(p.139)*

4. Configuration and Management 
4 Configuration and Management  
Usually, initial configuration of the management parameters is performed via an ASCII terminal. Once 
the management flows and corresponding router interface have been configured, it is possible to access 
SecFlow-1p via NETCONF or SNMP for operation configuration. See Configuring SecFlow-1p for SNMP 
Management Access for an example of management configuration. For details on configuring the 
router, refer to the Router section in the Traffic Processing chapter. 
The following table summarizes management options for SecFlow-1p.   
Port 
Manager 
Location 
Transport Method 
Management 
Protocol 
Application 
Ethernet 
FE/GbE/ 
10GbE 
 
 
Local, remote 
Inband 
SSH 
RADview (see Working with 
RADview below) 
Terminal emulation application (see 
Working with SSH below) 
NETCONF 
Third-party NETCONF client 
See NETCONF-Based Network 
Management below. 
SNMP 
Third-party NMS (see SNMP-Based 
Network Management below) 
 
 
Note 
By default, the terminal, SSH, NETCONF, and SNMP management access 
methods are enabled. See Configuring Management Access for details on 
how to enable/disable a particular method.  
4.1 CLI-Based Configuration  
SecFlow-1p supports the RAD-OS CLI engine. CLI sessions should be open remotely, by SSH. 
SecFlow-1p supports up to ten concurrent CLI sessions – one local and nine remote. 
4. Configuration and Management 
Working with SSH  
You can connect to SecFlow-1p via SSH using a program, such as PuTTY. 
Typically, the SSH host is a PC or Unix station with the appropriate suite of TCP/IP protocols.  
The management port is the Ethernet port with the highest number, according to the device ordered:  
• 
6 for 4U2S configurations 
• 
4 for 2U configurations. 
The management interface is set in factory defaults as follows.  
For 4U2S (superset) configurations:  
interface 32 
                address 169.254.1.1/16 
                bind ethernet 6 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
For 2U configurations:  
interface 32 
                address 169.254.1.1/16 
                bind ethernet 4 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
You can use a SSH host connected directly or via a local area network.  
4. Configuration and Management 
 
Login 
SecFlow-1p supports various access levels to prevent unauthorized modification of the operating 
parameters. Refer to User Access in the Management and Security chapter for more information on the 
access levels, as well as a list of the default users defined in the device and information on configuring 
additional users. 
Note 
The superuser (su) can perform all the activities supported by the SecFlow-1p 
management facility.  
You can log into your device with your username and password. 
If you fail to log in to the terminal five times (due to wrong username or password) in less than five 
minutes, from the same IP address, the device does the following: 
• 
Blocks further login attempts from the same IP for five minutes. Attempts from remote are 
answered with immediate TCP reset, without trying to authenticate the user. Blocks any 
management protocol from the same IP, such as SNMP and NETCONF, for five minutes. 
• 
Logs the failed login event, with the maximum number of attempts exceeded string. 
4. Configuration and Management 
When the locking period is over, the device lifts the block, even if there were further attempts during 
this time. Afterwards, you can fail five more attempts before being locked again. 
Note 
• 
An SNMP access attempt with wrong credentials does not count as a 
failed login attempt, and the user is not blocked due to it. 
• 
You can display information on recent failed login attempts (of sources 
that failed since last being unblocked) by invoking the show failed-login-
attempts command (under the management level). Refer to Viewing 
Failed Login Attempts in the Management and Security chapter. 
• 
<CR> for either username or password is ignored and is not considered a 
failed login attempt.  
 
Logging In  
 To log in to SecFlow-1p with non-linux user: 
1. At the user prompt (user>), enter the username and press <Enter>.  
The password prompt (password>) appears. 
2. Enter the password (default is 1234) and press <Enter>. 
If OTP is not configured, the base prompt SF-1p# appears.  
If OTP is configured (see OTP Authentication), the device prints verification code: on the CLI 
screen and sends a onetime password to the user’s preconfigured phone number. 
Note: You have five minutes to enter the verification code. After that (or in case a wrong code is 
entered) the authentication attempt fails. 
3. Enter received the verification code into the device. 
The base prompt SF-1p# appears.  
 
Note 
You can display a banner at login. Refer to the Administration chapter for 
details.  
 
 To log in to SecFlow-1p with linux-tech user: 
1. Login with the default user “su” via SSH (see Working with SSH above).  
2. Type “admin login” and press <Enter>. 
3.  At the user prompt (user>), enter the linux-tech username and press <Enter>.  
4. Configuration and Management 
The password prompt (password>) appears. 
4. Enter the password and press <Enter>. 
Changing Password  
It is recommended that you change the users’ default passwords to prevent unauthorized access to the 
unit using the special option chngpass. This option is also useful in case the user has forgotten their 
password.  
 To change/restore a password:  
1. At the User prompt (config>mngmnt# user>), enter chngpass and press <Enter> to receive a 
temporary password. With this password you can enter as user and change the password to 
your own.   
A key code is displayed. 
2. Send the key code to RAD Technical Support department. 
RAD technical support department will generate a temporary password which is valid for a 
single login. 
3. Use this temporary password to log in and set a new permanent password. 
Lost Superuser Password 
If you have lost your superuser password, contact Technical Support via the RADcare Online portal or by 
email. 
Using the CLI  
The CLI consists of commands organized in a tree structure of levels, starting at the base level. Each level 
(also referred to as context) can contain levels and commands (see Navigating for more information on 
the levels and commands available in SecFlow-1p). The level is indicated by the CLI prompt. 
Note 
Most commands are available only in their specific context. Global commands 
are available in any context. You can enter ? at any level to display the 
available commands.  
4. Configuration and Management 
CLI Prompt 
The base level prompt contains the device name, which is SecFlow-1p by default (the device name can 
be configured in the system level; refer to Device Information in the Administration chapter). The 
prompt ends with $, #, or >, depending on the type of entity being configured and the user level. 
If a new dynamic entity is being configured, the last character of the prompt is $. Examples of dynamic 
entities include flows, QoS profiles, and OAM CFM entities.  
If a new dynamic entity is not being configured, the last character of the prompt is > (for tech or user 
access levels) or # (for other access levels). 
Note 
The examples in this manual use # as the last character of the prompt, unless 
the creation of a new dynamic entity is being illustrated.  
After you type a command at the CLI prompt and press <Enter>, SecFlow-1p responds according to the 
command entered. 
CLI Inactivity Timeout 
If a CLI session is inactive (i.e. no input received) for ten minutes (the default) or the number of minutes 
configured in the inactivity timer (refer to timeout and console-timeout configuration in the 
Management Ports section of the Management and Security chapter), the device terminates the session 
and logs the logout event, with the due to inactivity timeout string. 
Navigating 
To navigate down the tree, enter the name of the next level. The prompt then reflects the new location. 
To navigate up, use the global command exit. To navigate all the way up to the root, enter exit all.  
At the prompt, one or more level names separated by a space can be typed, followed (or not) by a 
command. If only level names are typed, navigation is performed and the prompt changes to reflect the 
current location in the tree. If the level names are followed by a command, the command is executed, 
but no navigation is performed and the prompt remains unchanged. 
Note 
To use show commands without navigating, type show followed by the level 
name(s) followed by the rest of the show command.  
In the following example, the levels and command were typed together and therefore no navigation was 
performed, so the prompt did not change. 
configure system date-and-time date-format yyyy-mm-dd 
show configure system system-date 
2013-06-10   15:08:20  UTC  +00:00 
4. Configuration and Management 
In the following example, the levels were typed separately and the navigation is reflected by the 
changing prompt. 
configure 
config# system 
config>system# date-and-time 
config>system>date-time# date-format yyyy-mm-dd 
config>system>date-time# exit 
config>system# show system-date 
2013-06-10   15:13:23  UTC  +00:00 
 
config>system# 
Full-Path Command  
Full-path command allows you to enter a CLI command anywhere in the tree as if the current level was 
the CLI root, by preceding the command or level change with a backslash character. The device executes 
the command as if it were invoked from the CLI root. 
If you enter a level change (preceded by \) without a command, the CLI does not return to the prompt of 
the level that the command was invoked from, but remains at the changed level. For example, the 
\configure system command, when invoked from any level in the CLI tree, returns the SF-
1p>config>system# prompt. However, if you enter a level change followed by a command, the system 
performs the command and then returns the prompt of the level that the command was invoked from. 
For example, if following the command SF-1p>admin>scheduler#, you enter \configure system name 
my-device, the latter command sets the device name to my-device and then returns the prompt my-
device>admin>scheduler#. 
Note 
Before executing a full path command, the CLI engine exits to the CLI root. 
Some commands (e.g. ping) behave differently, depending on the location 
they were executed from. The following command, for example, would use a 
router 1 source address, although executed from router 2:  
SF-1p>config>router(2)# \configure router 1 ping 192.168.1.1 
Command Tree 
The tree command displays a hierarchical list of all the commands in the CLI tree, starting from the 
current context.  
 To view the entire CLI tree (commands only): 
1. At the root level, type tree. 
SF-1p# tree 
| 
4. Configuration and Management 
+---admin 
|   | 
|   +---factory-default-all 
|   | 
|   +---factory-default 
|   | 
|   +---license 
|   |   | 
|   |   +---license-enable 
|   |   | 
|   |   +---show summary 
|   |   | 
|   |   +---show SF-1p-id|   | 
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
config# tree detail 
configure 
| 
+---access-control 
|   | 
|   +---access-list [{ipv4|ipv6}] <acl-name> 
|   |   no access-list <acl-name> 
|   |   | 
|   |   +---delete <sequence-number> 
|   |   | 
|   |   +---deny udp <src-address> [<src-port-range>] <dst-address> 
                 [<dst-port-range>] [dscp <dscp-value>] [log] [sequence 
                 <sequence>] 
|   |   |   deny tcp <src-address> [<src-port-range>] <dst-address> 
                 [<dst-port-range>] [dscp <dscp-value>] [log] [sequence 
                 <sequence>] 
|   |   |   deny icmp <src-address> <dst-address> [icmp-type <icmp-type-number>] 
                  [icmp-code <icmp-code-number>] [dscp <dscp-value>] [log] 
                 [sequence <sequence>] 
|   |   |   deny ip [protocol <ip-protocol-number>] <src-address> <dst-address> 
4. Configuration and Management 
3. Press <Enter> to see more or <CTRL-C> to return to the prompt. 
Command Structure 
CLI commands have the following basic format: 
command [parameter]{ value1 | value2 | … | valuen } [ optional-parameter <value> ]  
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
4. Configuration and Management 
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
4. Configuration and Management 
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
      admin                          + Administrative commands 
      configure                      + Configure device 
      file                           + File commands 
      logon                          - Logon as Debug user 
      on-configuration-error         - Behavior for configuration error 
Global commands: 
      copy                           - Copy file 
      echo                           - Displays a line of text (command) on the 
                                       screen 
      exec                           - Execute script of CLI commands 
      exit                           - Returns to the next higher command level 
                                       (context) 
      help                           - Displays information regarding commands 
                                       in the current level 
      history                        - Displays the history of commands issued 
                                       since the last restart 
      info                           - Displays the current device configuration 
      level-info                     - Displays the current device configuration 
                                        - commands from the current level only 
      logout                         - Logs the device off 
      ping                           - Ping 
 [no] popup-suspend                  - Suspends popup messages 
      save                           - Save current settings 
 [no] schedule                       - Schedule a command to run in a future 
                                       time 
      trace-route                    - Traceroute 
      tree                           - Displays the command levels from the 
                                       current context downwards 
Hotkeys: 
      Ctrl-H, Del, Backspace          -Delete character left of cursor 
      Ctrl-D                          -Delete character right of cursor 
      Ctrl-U                          -Delete text up to cursor 
      Ctrl-K                          -Delete text from cursor to end of line 
      Ctrl-W                          -Delete word left of cursor 
      Alt-D, Esc-D                    -Delete word right of cursor 
      Ctrl-Y                          -Paste last deleted text 
      Tab                             -Completion token 
4. Configuration and Management 
      ?                               -Interactive help token 
      Ctrl-P, Up arrow                -History forward 
      Down arrow                      -History backward 
      Ctrl-B, Left arrow              -Move cursor left one character 
      Right arrow                     -Move cursor right one character 
      Ctrl-A                          -Move cursor to beginning of line 
      Ctrl-E                          -Move cursor to end of line 
      Alt-B, Esc-B                    -Move cursor left one word 
      Alt-F, Esc-F                    -Move cursor right one word 
      Ctrl-L                          -Redisplay current line 
      Ctrl-S                          -Pause transmission (XOFF) 
      Ctrl-Q                          -Resume transmission (XON) 
      Ctrl-C                          -Interrupt current command 
      Ctrl-G                          -Return to upper level 
      Ctrl-Z                          -Return to CLI root 
      Ctrl-_                          -Exit CLI 
Output Modifiers (usage: 'command | modifier'): 
      begin <regular-expression>      -Start printing once expression found 
      exclude <regular-expression>    -Print lines not containing expression 
      include <regular-expression>    -Print lines containing expression 
Show commands can be printed repeatedly by appending 'refresh' to them 
 
SF-1p Installation and Operation Manual  : https://www.rad.com/docs/877 
Command Help 
Enter help <command> to display command and parameter information. 
config>system# help name 
 - name <name-of-device> 
 - no name 
 <name-of-device>  : Device name [0..255 chars] 
Level Help 
Enter ? at the command prompt to display the commands available in the current level. 
file# ? 
      delete                         - Delete file 
      dir                            - Display file directory 
 
 show banner-text                    - Display banner 
 show configuration-files            - Displays configuration files properties 
 show copy                           - Display Copy progress 
 show factory-default-config         - Display factory-default-config 
 show rollback-config                - Display rollback-config 
 show schedule-log                   - Display schedule-log 
 show startup-config                 - Display startup-config 
 show sw-pack                        - Display SW packs 
 show user-default-config            - Display user-default-config 
4. Configuration and Management 
Command-Line Completion 
Command-line completion saves you command-line entry time and reminds you the syntax of 
command-line entities (levels, commands, parameters, and profiles).  
In a command-line, SecFlow-1p completes command-line entities, when you press <Tab> immediately 
following a string (one or more characters). 
Some user-defined entity names can be completed as well. If you enter an entity name that does not 
exist in the database, SecFlow-1p creates this entity with the selected name.  
• 
If the command-line entity name can be completed in only one way, when you press <Tab>, 
SecFlow-1p autocompletes the entire name and appends a space. 
• 
If the command-line entity name can be completed in more than one way, SecFlow-1p appends 
the characters that are common to all possibilities, and displays a list of the completion 
possibilities beginning with those characters.  
• 
If the string is already a complete entity name (level/command/parameter/ profile) or cannot be 
completed to a complete name, no completion is done. 
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
config>sys 
name 
name 
name 
config 
mgm 
No possibilities 
mgm 
4. Configuration and Management 
Interactive Help 
To get interactive help, type ?. 
In general, typing a ? directly after a string displays possibilities for string completion, while typing 
<space> and then a ? displays possibilities of the next argument. 
When a <CR> appears in a ? list, the string you entered is itself a valid command needing no further 
additions. Pressing <Enter> executes the command or navigates to the indicated level. 
Typing ? immediately after a command or partial command with no space before the ?, tells SecFlow-1p 
to display all possibilities for completing the string. Help output is always followed by the string you 
typed with the cursor at the end of the string waiting for input. 
config>system# date? 
date-and-time                  - Configure date and time 
config>system# date  
admin# fact? 
factory-default-all            - Return to factory default and reboot 
factory-default                - Return to factory default configuration and 
                                 reboot  
admin# fact 
admin# factory-default? 
factory-default-all             - Return to factory default and reboot 
 <CR> 
admin# factory-default 
Current configuration will be erased and device will reboot with factory default 
configuration. Are you sure   ? [yes/no] _ 
When a string cannot be completed, SecFlow-1p displays “cli error: Invalid Command”. 
admin# stac? 
# cli error: Invalid Command 
admin# stac 
 
file# da ? 
# cli error: Invalid Command 
file# da 
Typing <?> after a space between a command or level name and the ? tells SecFlow-1p to display 
possibilities of the next argument. If the string preceding the ? is ambiguous or invalid, an explanatory 
message is displayed. The string does not have to be a complete command. 
If there is only one possible command starting with that string, pressing <Enter> will execute the 
command. If there is more than one command that starts with the string, the CLI displays a message 
that it can’t clarify which command you want. 
admin# factory? 
 
factory-default-all              - Return to factory default and reboot 
4. Configuration and Management 
factory-default                  - Return to factory default configuration         
                                   and reboot 
A command followed by a ? without a space, shown above, returns a list of possible completions. The 
same command followed by a space and then ? returns an ambiguous command message. This means 
the string entered could be completed to more than one command and is therefore ambiguous, as 
shown below.  
admin# factory ? 
# cli error: Ambiguous Command 
admin# factory 
A string that is a complete command name followed by a space ? displays all possible command 
parameters. 
The next example shows a complete command to which a parameter could be appended. It also shows 
how a string that is a complete command is executed by pressing <CR>, or <Enter>. 
config>reporting# pm-collection system interval ?  
 <seconds>            : Duration [1..900] 
Scheduling CLI Commands 
You can schedule the execution of CLI commands at a future date and time. By default, no scheduling is 
configured. 
The global schedule command is used to configure the scheduling of a command. You can specify any 
command to be scheduled except the logout command.  
 When you schedule a command, before saving it, SecFlow-1p prefixes the command with the path from 
which the schedule command was executed. To specify a CLI command with a full CLI level path, you 
should schedule it at the CLI root level. 
SecFlow-1p tests the command that is configured as scheduled in the same way that it would be tested 
when executed; if the tests fail, you are notified of this, but the command is still scheduled, since it may 
be valid when the scheduled time arrives. 
The following types of schedules can be configured: 
In <minutes> 
Executed once, after the specified number of minutes. This type of 
schedule is not saved in nonvolatile (permanent) SecFlow-1p 
memory; it is deleted at device reboot whether or not it was 
executed. 
At <date-and-time> 
Executed once at the specified date and time. This type of schedule 
can be optionally saved in permanent memory, in order to be 
available after device reboot. 
4. Configuration and Management 
 
Note 
Schedules for date and time are saved in system local time. If the local time 
changes, SecFlow-1p does not modify the schedules to compensate for the 
change; therefore, changing the time can cause schedules to be executed 
twice or not executed at all.  
Schedules are marked as finished after they are executed.  
When executing scheduled commands, SecFlow-1p assumes a Yes answer for any confirmation 
questions. When a scheduled command is executed, it is sent to TACACS+ and Syslog accounting, as if it 
were executed by a CLI user. 
Configuring Command Scheduling 
 To schedule a command: 
• 
In any level, enter the schedule command according to the type of schedule: 
 
In <minutes> – Enter: 
schedule <name> in <minutes> [repeat-forever] “<command>” 
The schedule is saved with its name set to <name>, and the specified <command> is executed 
after the specified amount of <minutes> has elapsed, regardless of changes to the local system 
time.  
Range for <minutes>: 1–14400 [10 days] 
repeat-forever: Repeat schedule at specified intervals forever. 
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
 
4. Configuration and Management 
Note 
Schedules can be added or deleted, but not changed. If you wish to change the 
details of a schedule, you have to delete it and then recreate it with the changes.  
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
Daylight Saving Time) 
Note 
You can also enter the info command from the root of the device to view all 
commands of the device, including scheduled commands (see Viewing the 
Device Configuration below).  
 To view scheduling without command details: 
• 
Navigate to the admin scheduler level and enter: 
show scheduler 
admin scheduler 
admin>scheduler# show scheduler 
Current date:   13 June 2017       09:36:55  UTC  +00:00 
 
Schedule Name                     Type       Prm Fin Activation               
--------------------------------------------------------------- 
reportpm                          Once (In)  No  Yes --                       
schedulepm                        Once (In)  No  Yes --                       
Syslogfacility                    Once (In)  No  No   0 day(s),   00:04:03    
 
 
Summer Time 
 
Start (Date) : 21 June 2017 01:00 
End   (Date) : 27 October 2017 12:59 
Offset       : 60 
 
 
4. Configuration and Management 
Reboot is not scheduled 
 To view scheduling with command details: 
• 
Navigate to the admin scheduler level and enter: 
show scheduler-details 
admin scheduler 
admin>scheduler# show scheduler-details 
Current date:   13 June 2017       09:40:00  UTC  +00:00 
 
 
Schedule Name           : reportpm 
Type                    : Once (In) 
Permanent               : No 
Finished                : Yes 
Activation In(Seconds)  : -- 
 
Command : configure system date-and-time config reporting pm 
 
 
Schedule Name           : schedulepm 
Type                    : Once (In) 
Permanent               : No 
Finished                : Yes 
Activation In(Seconds)  : -- 
 
Command : config reporting pm 
 
 
Schedule Name           : Syslogfacility 
Type                    : Once (In) 
Permanent               : No 
Finished                : No 
Activation In(Seconds)  : 0 day(s), 00:00:38 
 
Command : configure system syslog device facility local1 
 
 
 
Summer Time 
 
Start (Date) : 21 June 2017 01:00 
End   (Date) : 27 October 2017 12:59 
Offset       : 60 
 
 
Reboot is not scheduled 
4. Configuration and Management 
Scheduling Display Parameters 
Parameter 
Description 
Current date 
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
4. Configuration and Management 
Parameter 
Description 
Offset 
Number of minutes to move the clock during daylight saving time 
Configuration Errors 
The following table lists the messages generated by SecFlow-1p when a command scheduling 
configuration error is detected. 
Message 
Cause 
Corrective Action 
Schedule with this name 
already configured 
You tried to create a new schedule 
with a name that is used by an 
existing schedule. 
Specify a name that is not being used by 
an existing schedule. 
Warning: Scheduled 
command failed sanity 
The command that you specified to 
schedule may fail when executed. 
Check the command; if changes are 
needed, delete the schedule and 
re-enter it with the changed command. 
The logout command may 
not be scheduled 
You specified the logout command as 
the command to schedule. 
None. You are not allowed to schedule 
the logout command. 
Viewing the Device Configuration 
You can enter the info command at the device root, to view all commands that have been configured for 
the device. This includes scheduled commands, as they are global commands. See an example in the 
Examples below. 
 To view commands of a device: 
• 
At the device root, type info.  
Refreshing Output 
You can specify that SecFlow-1p should periodically refresh the output of a show command. 
 To periodically refresh the output of a show command: 
• 
Append refresh [<sec>] to the command. The allowed range for <sec> is 3–100 seconds (default 
is 5 seconds). 
4. Configuration and Management 
SecFlow-1p enters refresh mode and displays the output of the command periodically, along 
with an indication of how to exit refresh mode, at the interval specified by <sec>. You cannot 
enter any commands while SecFlow-1p is in refresh mode. 
To exit refresh mode, type <ESC> or <Ctrl>+C. 
The example below shows the result of refreshing the RADIUS statistics every 15 seconds, and typing 
<Ctrl>+C after the status is displayed twice. 
config# show management radius statistics refresh 15 
                 Server 1   Server 2   Server 3   Server 4 
--------------------------------------------------------------- 
Access Requests       0          0          0          0 
Access Retransmits    0          0          0          0 
Access Accepts        0          0          0          0 
Access Rejects        0          0          0          0 
Access Challenges     0          0          0          0 
Malformed Response    0          0          0          0 
Bad Authenticators    0          0          0          0 
Pending Requests      0          0          0          0 
Timeouts              0          0          0          0 
Unknown Types         0          0          0          0 
Packets Dropped       0          0          0          0 
Counter Discontinuity 0          0          0          0 
To exit the refresh-mode press ESC or Ctrl+C 
Filtering Output 
Some commands, such as info and show display large amounts of information as their output. It is 
possible to control the type and amount of information displayed, by filtering the output. 
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
4. Configuration and Management 
The following example illustrates filtering output. 
config>system# info detail | include date 
    date-and-time 
        date-format yyyy-mm-dd 
Metacharacters 
Metacharacters are characters with special meaning. They allow you to define filter criteria, while not 
being part of the filter criteria themselves. Some are placeholders or wildcards. Some allow you to 
define ranges of characters to either include or exclude. You can construct complex filter expressions to 
see the exact output you want. The following table describes filter metacharacters. 
 
Metacharacter 
Description 
Example 
. 
Matches any single character. 
r.t matches the strings rat, rut, and r t, but not 
root. 
$ 
Matches the end of a line. 
device$ matches the end of the string header 
device but not the string header device-name. 
^ 
Matches the beginning of a line. 
^device matches the beginning of the string 
device loaded from but not the string header 
device-name. 
* 
Matches zero or more occurrences of 
the preceding character.  
.* means match any number of any characters. 
\ 
This character is used to treat the 
following metacharacter as an 
ordinary character. 
\$ is used to match the $ character rather than 
match the end of a line. 
\. is used to match a period rather than match 
any single character. 
[ ]  
[c1-c2]  
[^c1-c2] 
Matches any one of the characters 
between the brackets. 
Ranges of characters are specified by 
a beginning character (c1), a hyphen, 
and an ending character (c2); multiple 
ranges can be specified as well. 
To match any character except those 
in the range, use ^ as the first 
character after the opening bracket. 
r[aou]t matches rat, rot, and rut, but not ret. 
[0-9] matches any digit. 
[A-Za-z] matches any upper or lower case 
letter. 
[^269A-Z] matches any character except 2, 6, 9, 
and uppercase letters. 
| 
Logical OR two conditions together 
(band|comp) matches the lines bandwidth cir 
999936 cbs 65535 and compensation 0. 
4. Configuration and Management 
Metacharacter 
Description 
Example 
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
A[0-9]{3} matches A followed by exactly three 
digits, i.e. it matches A123 but not A1234. 
[0-9]{4,6} matches any sequence of 4, 5, or 6 
digits. 
Regular Expression Syntax 
A filter expression is a regular expression. A regular expression can be composed of characters and 
metacharacters. Any combination of metacharacters can be used. If you want spaces as part of the filter 
expression, enclose the expression with quote metacharacters. All characters found after a space not 
enclosed by quotes are ignored by the CLI. 
The following table provides some example of regular expressions and the resulting string that will be 
used to filter the CLI output. 
 
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
 
4. Configuration and Management 
Enabling Entities 
Some dynamic entities are created as inactive by default. After the configuration is completed, the 
no shutdown command activates the entity, as shown below. 
configure system syslog device 
config>system>syslog(device)# severity-level critical 
config>system>syslog(device)# no shutdown 
config>system>syslog(device)# exit 
config>system# 
The shutdown command is also used to deactivate/disable a hardware element (such as a port), while 
no shutdown enables/activates it. 
Using Scripts 
CLI commands can be gathered into text files. They may be created using a text editor, by recording the 
user commands or by saving the current configuration. 
These files can be configuration files or scripts. Configuration files have specific names and contain CLI 
commands that SecFlow-1p can use to replace the current configuration, while scripts contain CLI 
commands that add to the current configuration. Configuration files can be imported from and exported 
to RAD devices via file transfer protocols. 
For more information on configuration files, refer to the description in the Administration chapter. 
In order to execute a CLI script, you have to copy/paste it to the CLI terminal, or send it to SecFlow-1p 
via the RADview Jobs mechanism, CLI script option. 
To execute a script, run the commit command. 
Examples  
 To schedule shutdown of the syslog device in five minutes: 
config>system>syslog(device)# schedule sched1 in 5 "shutdown"  
 To schedule copying a log file in two hours: 
schedule sched-copy-2hrs in 120 “copy log tftp://1.1.1.1” 

## 4.2 Web-based Configuration  *(p.163)*

4. Configuration and Management 
 To schedule copying a log file on April 2 at 6:00, with the schedule saved in permanent memory: 
schedule sched-copy-Apr2 at april 2 2015 06:00 “copy log tftp://1.1.1.1” permanent 
save 
 To display commands configured for the device (including scheduled shutdown command): 
SF-1p# info  
configure 
        echo "System Configuration" 
#       System Configuration 
        system 
            date-and-time 
                date-format mm-dd-yyyy 
                echo "NTP (Network Time Protocol)" 
#               NTP (Network Time Protocol) 
                ntp 
                    server 1 
                    exit 
                exit 
                summer-time date june 21 2017 01:00 october 27 2017 12:59 
             
        exit 
     
 
    schedule "sched1" in 5 "configure system syslog device shutdown" 
4.2 Web-based Configuration  
SecFlow-1p Web-based Configuration Management offers the user a simple, fluid, intuitive, and efficient 
digital interaction. It  ensures easy access to the content and help the users intuitively locate exactly 
what they are looking for. The main principles of the SecFlow-1p Web GUI are described in the section 
below. 
Logging In 
You can configure and manage SecFlow-1p locally or remotely using its web interface. Supported 
browsers are the following: 
• 
Google Chrome 
• 
Microsoft Internet Explorer 
• 
Microsoft Edge 
4. Configuration and Management 
• 
Apple Safari 
• 
Mozilla Firefox 
 
Note 
To prevent configuration errors, flush the browser’s cache whenever you 
return to the same screen. 
 If you have trouble with the web interface: 
• 
Enable scripts. 
• 
Make sure that local and organizational firewalls allow access to the destination IP address. 
• 
Disable pop-up blocking software, such as Google Popup Blocker. You may also have to 
configure spyware and adware protecting software to accept traffic from/to the destination IP 
address. 
 To log into SecFlow-1p via the web interface:  
1. In the web browser, navigate to the SecFlow-1p IP address, using HTTPS protocol (https://). 
The SecFlow-1p login prompt appears. 
2. Enter the relevant credentials (Default: Username = su, Password = 1234), and click <Login>.  
If OTP is not configured, the dashboard summarizing the status of the device and the main menu 
are displayed.  
If OTP is configured (see OTP Authentication), the device sends a onetime password to the 
user’s preconfigured phone number. 
 
3. Enter the received verification code into the device. 
4. 
Note: You have five minutes to enter the verification code. After that (or in case a 
wrong code is entered) the authentication attempt fails. 
5.  
6. 
 
The dashboard summarizing the status of the device and the main menu are displayed.   
4. Configuration and Management 
 
 
You can log out by clicking Admin ->  
 icon on the top right. After 5 minutes of user 
inactivity, the logout is performed automatically, and you are returned to the login page. 
If you have lost your superuser password, contact Technical Support via the RADcare Online portal or by 
email. 
Navigating the Web Interface  
You can navigate between the dialogs using the following methods: 
• 
Navigation tree (on the left of the screen)  
• 
Top path 
• 
Web browser ‘Back’ and ‘Forward’ controls 
• 
Clicking on an entry in a table 
• 
Creating a new entry in a dynamic table 
4. Configuration and Management 
A navigation tree is displayed on the left, as shown below. The tree featuring expandable/collapsible 
branches is organized according to the CLI hierarchy.  
 
 
Graphical Controls 
The WEB GUI commands are similar to the CLI commands with the following main differences: 
• 
A CLI action command or a Boolean CLI command (command with a no-form but without 
arguments) is presented by an On/Off switch 
• 
“shutdown” is an exception and presented as pull-down menu. 
• 
A CLI command with a no-form and one or more arguments is presented as an On/Off switch 
(for the no-form) and the appropriate fields for the arguments 
The ‘Save’ button 
 in the top right corner copies the running-config to the startup-config. 
The ‘Reboot’ button 
  in the top right corner is used to reboot the device. When clicked, the 
following display appears: 
4. Configuration and Management 
 
Click “Reboot Now” to confirm. 
Dynamic Tables  
Dynamic tables are used in screens serving to add and remove entries. For example, in the screen below 
you can add SNMP users.  
 
Clicking on an 
 button opens a new dialog (navigation) with the parameters and information of the 
selected entity. Fill in the fields of the new entry. 
Two buttons, ‘Submit’/’Submit All’ and 
 act as follows: 
• 
 ‘Submit’ – commits the data entered so far in the dialog to the device and opens a new dialog 
(navigation) with the parameters and information of the selected entity. In the case of failure, 
an error message is displayed. 
• 
 – clears the data entered so far in the dialog (reads again the current configuration from 
the device).  
Clicking on the “Set” icon 
 provides a fast link to the port setup page, serving a shortcut for Quick 
Setup > Port action).  
4. Configuration and Management 
File Management via Web GUI 
The Web GUI allows the following actions in the area of file management: 
• 
Working with script files  
• 
Working with configuration files 
• 
Uploading software/software patch files. 
When selecting File from the Main menu, you can see all these options. 
7. 
 
 
 
Working with Script Files  
 To upload a script file: 
1. From the File Transfer window, click upload-script-file. You can either select a script file from 
the folder or drag-and-drop it to the window.  
4. Configuration and Management 
2. 
 
The file (AAA.txt) is selected. The File Transfer Status field and the progress bar show the data 
transfer status. You see the file transfer status: user script source, destination, the time it 
started and ended and the size. 
3. 
 
Now the transfer process is complete and you can see the Execute Script button. 
4. Configuration and Management 
4. 
 
 To execute a script file: 
1. Click the Execute Script button. 
2. 
4. Configuration and Management 
Working with Configuration Files  
 To download a configuration file: 
 
3. Click “Start download”. 
 
 
The file is saved in the default Download folder. 
 To upload a configuration file: 
1. Choose the upload-configuration-file option. 
2. 
 
4. Configuration and Management 
 
3. Select the file. 
4. 
 
5. Confirm your choice. 
4. Configuration and Management 
6. 
Now the startup.txt file has been copied to startup config. 
Working with Software Files 
 To upload a software file: 
1. Choose the upload-software-file option. 
2. 
 
3. Select the file from the local repository. 
4. 
 
4. Configuration and Management 
 
4. Configuration and Management 
 
The upload process begins. It passes through three stages: 
 
Preparing the upload 
 
Transferring the data 
 
Extracting the data. 
Uploading the software patch file is similar to uploading a software file. 
 
5. After uploading the SW to the device, you have to install it. 
4. Configuration and Management 
 To install the software file. 
1. In the “Install and Reboot” window, choose the software pack to install. 
 
2. Confirm the software installation followed by the device reboot. 
  
The device restarts with the new software. 
Quick Setup 
The Web GUI Quick Setup improves usability. Quick Setup functionality allows the user to quickly 
configure the device router and ports by saving a number of configuration steps to establish the 
connectivity. 
Quick Setup offers three levels:  
4. Configuration and Management 
• 
Ports to configure the device ports  
• 
Router to configure the static route 
• 
VPN to configure tunnels. 
Configuring Ports 
Ports Table  
When selecting Port, the list of the ports available on the device opens, showing the port name, status, 
speed and (when relevant) the attached router/router interface. Once you select the port, you can 
configure the specific port type parameters. 
3. 
From the main menu, open Quick Setup sub-menu and click on Port. The list of 
ports available on the device opens.  
 
 
Configuring an Ethernet Port  
In the example below we will show how to simply configure Ethernet 5 with Admin status UP and IP 
address 10.10.10.10/24. 
4. Configuration and Management 
Note: Alternatively, you can enable DHCP. This will be shown in other configuration examples below.  
 To configure an Ethernet port: 
1. From the Port Table, click Ethernet 5. The Port configuration window opens.  
2. Set the ADMIN STATUS to “Up”:  
4. 
 
 To configure an Ethernet port with bridge connection: 
1. If you want to connect the port to a bridge (unaware only), set “Connect to Bridge” to “Enable”. 
The IP configuration disappears, and you can enter the Bridge Management Address to connect 
the bridge to the router. 
2.  
3.  
4. Configuration and Management 
 
3. Click on “+” in the Bridge Management Address field. 
 
4. 
4. Configuration and Management 
 
4. Fill in the address and click “Submit All”. 
. 
 
4. Configuration and Management 
 
 
 To configure a VLAN:  
1. In the Port Table, click on “+” on the left of the port name and assign the VLAN ID. 
5.  
4. Configuration and Management 
6. 
 
7. 
2. Click “Submit All”. VLAN 20 is created on port Ethernet 3. 
 
8. 
 
5. Click on the VLAN to edit it. You can either assign an IP address in the Address frame or set DHCP 
to “On”. 
6. Click “Submit all”. 
4. Configuration and Management 
9. 
 
10.  
11.  
12.  
The router interface 1/2 is created and VLAN 20 is bound to this interface. 
13.   
14. 
 
 To remove a VLAN: 
15. Note: You cannot delete a VLAN that is connected to a Router interface.  
1. Set DHCP to “Off” or remove the IP address (if defined).  
4. Configuration and Management 
2. The router interface is deleted. 
3. Go back to Port Table and check the VLAN to be removed. 
4. Click “Submit All”. 
5.  
6. 
 
The VLAN is deleted.  
Configuring a Cellular Port  
 To configure a cellular port: 
1. From the Port Table, select Cellular lte. 
The Cellular Port configuration window opens.  
4. Configuration and Management 
2. 
 
3.  
4. Set DHCP to “On” and the ADMIN STATUS to “Up”. 
At this stage a router interface is automatically created and connected. 
5. Select other parameters: 
 
Mode: sim/dual-sim. If sim is selected, also select sim 1 or sim 2. 
 
IPV6 autoconfig – if you want to use IPv6 instead of IPv4 (default), set the switch to “On”. 
6.  
4. Configuration and Management 
7. 
 
8. Select the SIM (SIM 1 or SIM 2, in this case SIM 1 is selected). 
9. Set APN name to “On” and type a selected name. 
10. Select the following: 
 
Radio access technology (radio-2g-3g-4g/radio-3g-4g/radio-4g/radio-3g/radio-2g) 
 
LTE band: any/b1/b2… 
 
PDP type: ip/relayed-ppp. 
11.  
4. Configuration and Management 
12. 
 
13. In the upper right corner of the screen, click “Submit All”.  
The display below shows the Port Admin Status at Up. We also see that router interface 1/2 
has been created.  
Note: Port operation status will be up only when the IP address is assigned. 
4. Configuration and Management 
14. 
 
The dashboard displays the Cellular LTE port up and running, with IP address 10.175.134.218.  
15. 
 
Now the operating status is also Up (green). 
16.  
4. Configuration and Management 
17. 
 
Configuring a WiFi Port  
 To configure a WiFi access point: 
1. From the Port Table, select the required WiFi port, in this example WLAN2.4g. 
The Port configuration window opens.  
2. 
 
4. Configuration and Management 
3.  
4. Set DHCP to “On” or assign an IP address. In this example we assign the IP address 
192.168.1.1/24. 
5. Set the ADMIN STATUS to “Up”. 
At this stage a router interface is automatically created and connected. 
6. Select other parameters: 
 
Channel: auto/channel-number. If the channel option is selected, also select its number 
(1..13) 
 
Radio mode: 802.11ng/802.11g/802.11b 
 
Security: wpa2-psk/wpa2-dot1x/none 
 
IPV6 autoconfig – if you want to use IPv6 instead of IPv4 (default). 
 
WiFi country code  
7. Set SSID to “On” and type its selected name. 
8. Set password to “On” and type the selected password. 
9. In the upper right corner of the screen, click “Submit All”. 
The below screen displays that the Port Administrative status is Up and a router interface 1/2 
is created.  
4. Configuration and Management 
 
10. The dashboard displays the WiFi port up and running, with no connected clients.  
11. 
 
4. Configuration and Management 
 To configure a WiFi client: 
1. From the Port Table, select WiFi client 1. 
The WiFi Client configuration window opens.  
2. 
 
3.  
4. Set DHCP to “On” or assign an IP address. In this example we use the DHCP option. 
5. Set the ADMIN STATUS to “Up”. 
6. Select other parameters: 
 
Connection method: last/best/priority 
 
Security: wpa2-psk/wpa2-dot1x/none 
 
Priority: 1-254 
 
IPV6 autoconfig – if you want to use IPv6 instead of IPv4 (default). 
7. Select SSID to “On” and type the name of the network you want to connect. 
8. Set password to “On” and type the selected password. 
9. In the upper right corner of the screen, click “Submit All”. 
The below screen displays that the Port Administrative and Operational Status are Up and a 
router interface 1/2 is created.  
4. Configuration and Management 
10. 
 
11. The dashboard displays the WiFi port up and running, serving both as an AP and a client. 
12. 
 
13.  
 
4. Configuration and Management 
Configuring a Serial Port  
 To configure a Serial port: 
1. From the Port Table, select the required serial port, in this example Serial 1. 
The Port configuration window opens.  
2. 
 
3. Set the ADMIN STATUS to “Up”. 
4. Select other parameters: 
 
Latency: 2-255 msec  
 
Baud Rate: 300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200 
 
Bus Idle: auto/bits. If “bits” is selected, also select the number of bits (The maximum value is 
100000. The minimum depends on the configured baud rate) 
 
Data Bits: 5..8 
 
Parity: none/even/odd 
 
Stop bits: 1/2 
 
Tx Delay: 1-10000 msec 
Now you can configure either a terminal server or a serial tunneling application. Terminal server and 
serial tunneling are mutually exclusive.  
4. Configuration and Management 
Configuring a Terminal Server  
The terminal server is an application that can be configured over serial ports. It translates serial traffic 
incoming from a serial port to IP packets (TCP or UDP), which are sent over an IP network (and vice 
versa). This way a user with an IP device such as a laptop can manage a serial device such as RTU. 
The user can telnet the terminal server (on a TCP or UDP port) and be connected to the serial port the 
terminal server is configured on. The terminal server converts the user’s IP traffic to serial traffic, and 
vice versa. 
A complementary terminal server application is to configure a Telnet TCP server on one device and a 
client on another. The client opens a connection, a kind of tunnel, to the server, allowing serial devices 
connected to the two devices to pass serial traffic between them, over an IP network. 
Terminal server parameters are configured on the system and the serial port levels, as follows: 
• 
parameters that are relevant to both serial ports are configured on the system level; these 
parameters have the same values for both ports.  
• 
shutdown of the entire feature is also configured on the system level (per device)  
• 
the actual terminal server with its proper protocol per port is configured on the port level. 
 To configure a terminal server: 
1. Click on the “+” on the right of “Terminal Server”. 
2. 
 
3. Type the terminal server number. 
4. Configuration and Management 
Note: Only one terminal server can be configured per port.  
4. Click “Submit”. 
The following options are displayed on the next screen.  
5. 
 
6. Set the “Local Address” to “On”. This is the local IP address (i.e. owned by the device), on which 
the terminal server listens. A user telnetting this address will be connected by the terminal 
server to the serial port on which it is configured. Traffic sent by the user will appear on any 
device connected to the serial port, and vice versa. Configuring the local address is mandatory. 
7. Enable the null CR mode if required (some terminal clients require the null-CR mode 
functionality, some of them require this mode to be enabled, and some disabled). 
8. Click on “+” in the frame of the desired option. 
 
For the Telnet Client TCP: define the number of TCP Telnet server port (2001..65534) and 
type in the Telnet server IP address. 
 
For the Telnet Server TCP: define the number of the port the Telnet server listens on 
(2001..65534) 
 
For the Telnet Server UDP: define the number of the port the Telnet server listens on 
(2001..65534) and type in the Telnet client IP address. 
9. Click “Submit”. 
10. Go to the System level and select Serial>Terminal Server. 
11. Define the required parameters: 
 
Buffer mode: byte/frame 
4. Configuration and Management 
 
Dead peer detection timeout: <minutes>: 1..1440 min (for terminal server traffic over TCP 
only) 
12. Set Admin Status to “Up”. 
13. Click “Submit”.  
14. 
 
The below screen displays that the Port Administrative status and Operational status are Up 
and the terminal server application is up and running.  
4. Configuration and Management 
 
Configuring Serial Tunneling 
Serial tunneling is an application that can be configured over a serial port, to create an IP tunnel 
between one or more opposite devices with serial ports. Serial traffic passes through the tunnel 
encapsulated in IP packets, between the tunnel endpoints. 
 To configure a serial tunnel: 
1. Click on the “+” on the right of “Tunnel” and type its Service ID. 
4. Configuration and Management 
2. 
 
The tunnel parameters are displayed on the next screen. 
 
3. Define the following: 
 
Transport layer: udp/tcp 
 
Buffer mode: byte/frame 
 
Local and remote address 
 
Whether the master is local or remote 
4. Set the Admin Status to “Up”. 
4. Configuration and Management 
 
5. 
 
6. Click “Submit” In the Address frame. 
The following screen is displayed.  
7. 
 
8. Click “Submit” in the upper right corner of the screen. Now the tunnel is up and running. 
4. Configuration and Management 
Configuring LoRa  
LoRa is enabled by default. It requires configuration of frequency plan mandatory parameter. 
The gateway requires LNS (LoRa Network Server) to be operational and its configuration is under 
customer responsibility. 
The available packet forwarding methods for LoRA are: 
• 
 UDP forwarding – GW communication with LNS based on UDP packets.  
• 
 ChirpStack (the default) – GW communication with LNS based on MQTT. 
Configuring LoRa with UDP Forwarding 
In this CLI example we are configuring a LoRa Gateway with frequency EU 868. 
 
UDP forward configuration and status: 
config>port>lora(1)# info 
    frequency plan eu868 
    gateway 
        operation-mode udp-forward 
        server ip-address 1.1.1.1 port 1680 
        server ip-address 2.2.2.2 port 1681 
        no shutdown 
    exit 
 
 
config>port>lora(1)# 
config>port>lora(1)>lora-gateway# show status 
Administrative Status   : Up 
LoRa Operational Status : Down 
Gateway ID (EUI)        : 0016c001f1615b32 (auto) 
Frequency Plan          : EU868 
Operation Mode          : Udp Forward 
Udp Forwarder Status    : Down 
 
Server                                            Port 
----------------------------------------------------------------------------- 
1.1.1.1                                           1680 
2.2.2.2                                           1681 
 
 
 
4. Configuration and Management 
 To configure LoRa (udp-forward) via Web: 
1. Under Quick Setup, navigate to Port>Lora1. 
2. Under “Frequency Plan”, select EU868, RU864, US915, AS923 (1-4), AU915, KR920, IN865 
(according to the user LoRa modem). In this case it is EU868. 
3. In the Gateway field, set Admin Status to UP 
4. Select the Operation Mode (udp-forward). 
5. Select the Gateway ID: auto/string (usually “auto” is used). 
 
6. Click on “+” to configure the server. 
7. Define the LoRa server ip-address or url and UDP port (default UDP port is 1680). 
8. Click “Submit All”.  
4. Configuration and Management 
 
Configuring LoRa with MQTT server (for working with Chirpstack) 
In this CLI example we are configuring a LoRa Gateway with frequency EU 868, working with MQTT 
server AAA. 
Configuring a LoRa server via Web GUI consists of two stages: 
• 
Configuring the LoRa gateway (according to the CLI script below) 
config>port>lora(1)# info 
    frequency plan eu868 
    gateway 
        mqtt-server "AAA" 
        no shutdown 
    exit 
• 
Configuring MQTT server with IP address or URL, protocol and port (according to the CLI script 
below). When working with LCM there is a need to add another MQTT server configuration for 
management: 
config>system>mqtt# info 
    server "AAA" 
        address ip 1.1.1.1 protocol ssl port 1883 
        certificate "AAA-CERT" trusted-ca "CAServer" 
    exit 
    server "AAA-MNG" 
        address ip 1.1.1.1 protocol ssl port 1883 
        certificate "AAA-CERT" trusted-ca "CAServer" 
        management-channel 
    exit 
4. Configuration and Management 
config>system>mqtt# server AAA-MNG 
config>system>mqtt>server(AAA-MNG)# show status 
 
Application        : Management Channel         
Server Address/URL : 1.1.1.1                              
MQTT Status        : Not Configured                       
 
Missing Configuration 
----------------------------------------------------------------------------- 
Certificate Does Not Exist 
 To configure the LoRa gateway with MQTT server by WEB UI:  
1. Under Quick Setup, navigate to Port>Lora1. 
2. Under “Frequency Plan”, select EU868, RU864, US915, AS923 (1-4), AU915, KR920, IN865 
(according to the user LoRa modem). In this case it is EU868. 
3. In the Gateway field, set Admin Status to UP. 
4. Leave chirpstack as operation mode (this is default setting). 
5. Set the MQTT Server to On and define its name (in this case AAA). 
 
 To configure the MQTT server “AAA”:  
1. Click on “+” to enter the server. 
2. Select “ip” and set the MQTT broker IP address. 
Note: you can also select “url” and in this case type the URL name.  
4. Configuration and Management 
3. Select SSL or TCP (default is SSL) and the port number. 
4. Set Certificate to “On”. 
5. Enter the name of the certificate and a trusted CA (CA-server in our case). 
6.  
 
7. If there is a need for MQTT management server for LCM, configure MQTT server with 
‘MANAGEENT CHANNEL’ On 
8. Click Submit All. 
9.  
4. Configuration and Management 
10. 
 
We see that the valid certificate “AAA” is not configured yet. To configure it, refer to Configuring X.509 
Entities. 
Once the valid certificate “AAA” is configured, we have both MQTT servers configured as well. 
 
11.  
12.  
4. Configuration and Management 
Configuring the Router  
 To configure a router:  
1. From the main menu, open the Quick Setup sub-menu and click on Router.  
The list of available routers opens (currently there is a single router). In this screen you can also 
get a shortcut to the NAT configuration and set the default gateway (in most configurations you 
need only default gateway and nothing more). 
 
2. Set “NAT” and “Default Gateway” to “On” and type in the default gateway IP address. 
 
 
3. Click on the Router number.  
4. Configuration and Management 
The Static Route screen opens.  
 
4. Define the static route and the next hop IP address. 
5. 
 
6. Click Submit. The Static route is created. 
4. Configuration and Management 
VPN Tunneling Configuration 
RAD’s SecFlow-1p VPN support IPsec-based security for both device management traffic and customer 
data traffic.  The procedures for both uses are generally similar, consisting of the following steps: 
7. 1. Setting up the tunnel physical connection – tunnel WAN connectivity. 
8. 2. Configuring the authentication method – ISAKMP Policy 
9. 3. Configuring the encryption method – IPsec Transform Set 
10. 4. Configuring the actual tunnels 
Quick Setup provides quick access to all the configuration options. This section provides a brief 
description of the process. Detailed information is available in the relevant chapters of this manual: 
Ports, and Traffic Processing,  
Tunnel WAN Connectivity 
Before you start the VPN configuration process, verify that the tunnel end-devices are physically 
interconnected, and that you have the connectivity information of the remote (peer) device: Ethernet 
IP, and gateway. Both devices must be in the same subnet, and their configuration must match. 
 To configure the SecFlow-1p WAN source interface: 
1. Under Quick Setup, click the Port sub-menu. The Port Table dialog appears displaying port 
information.  
2. Click on the port to be used for tunneling. The port configuration dialog appears.   
The top area displays port status and other information. The two Port Name fields display the 
interconnected ports on either end of the tunnel to be created.  
 
4. Configuration and Management 
 
  
 
3. Configure the port physical parameters according to your network:  
a. Securing management – enable IPV6 Autoconfig if IPv6 services are supported. Set Admin 
Status to Up. All other options are usually disabled. 
b. Securing customer traffic – set all options according to your network and offered services.  
4. Under Address, click ‘+’, and define the port IP Address and management network mask.  Both 
end devices must be in the same subnet.  
5. Click Submit All to save the definitions.  
ISAKMP Policy 
The ISAKMP Policy defines the security rules for the tunnel handshake. This includes peer authentication 
and encryption methods, and how secure keys are generated and managed.   
Multiple ISAKMP policies can be defined for each VPN entity.  The policies are compared by the peers 
during IKE Phase 1 negotiation, and the first matching policy (according to priority/order) is selected.  
This allows interoperability with different peers or migration between security profiles.  
Note 
Both end-devices must have matching ISAKMP policies. 
 To define the ISAKMP policy: 
1. Under Quick Start menu, click the VPN sub-menu. In the displayed dialog, under ISAKMP Policy 
click ‘+’ to add a policy.  The ISAKMP policy parameters appear.  
4. Configuration and Management 
  
2. Under ISAKMP Policy, assign the policy number. This number prioritizes the order in which the 
device tries policies when negotiating Phase 1 (IKE). Lower numbers have a higher priority and are 
tried first.  
3. Set the following parameters:  
 
Encryption – Choose the encryption method from the dropdown menu.   
 
 
Group – defines the DH group strength of the tunnel key exchange. A higher group number 
provides stronger encryption with a higher prime number, mathematical complexity and 
cryptographic strength – but, adds some delay.  
 
 
HASH – ensures data integrity over the channel.  Choose the HASH method. 
4. Configuration and Management 
 
4. Click Submit All to save.  If the definitions are accepted, the response will be a green banner 
with ‘Success!’. A green banner without ‘Success’ indicate that the definitions are not strong 
enough (but are still valid). 
5. To define another ISAKMP policy, click the ‘+’ sign and repeat the process.  
Note 
To delete a policy, click the adjacent Trash icon. 
IPsec Transform Set 
The IPsec transform set defines the encryption and authentication of the data carried by the tunnel.   
Note 
Both end-devices must have matching IPsec Transform Set definitions.  
 To define the IPsec Transform set: 
1. In the side menu, under the Quick Start, click the VPN sub-menu.  
2. In the displayed dialog, under IPsec, click on the ‘+’ sign. The IPsec parameters appear. 
 
3. Assign the IPsec Transform Set name – it is recommended to assign a name that reflects the IPsec 
transform set definitions.  For example, ESP-AES256-SHA1.  
4. Configuration and Management 
4. Define the following: 
 
Algorithms (encryption method) – Select the same value as previously set for the ISAKMP 
policy.  For example, esp-aes-cbc-256. 
 
Hash – select the same suffix integrity method as set for the ISAKMP policy.  For example, if 
HASH 1 was set under ISAKMP, set espHASH1 under IPsec Transform.  
(The prefix ‘esp’ – e.g. espHash1, indicates that the HASH is used with ESP, and makes it 
clear that the HASH is applied to ESP traffic not just the IKE negotiation.)  
 
Mode – determines tunnel implementation:  
 
Tunnel – The entire packet is encrypted, and a new VPN header is added for routing.  
 
Transport – only the payload is encrypted.  
5. Click Submit All at the top of the dialog, and verify ‘Success!’ appears on a green background (or 
just the green background if the definitions are a little weak). 
Tunnel Definitions 
Once the ISAKMP and IPsec policies have been defined according to the previous sections, the actual 
tunnels are configured.  The procedure consists of defining router and tunnel identification, and the 
network parameters. 
This section provides basic information on the tunnel definition options and how to navigate them. For 
more information, refer to the relevant sections in the following chapters: 
• 
Ports chapter – sections: Cellular Ports, Ethernet Ports, VLAN Ports 
• 
Traffic Processing chapter: DMVPN, GRE Tunneling, IPsec 
  
Notes 
The selected Tunnel Type determines the network parameters that require 
configuration. 
Be sure to click Submit All a the end of the process, to save all configurations. 
 To configure the tunnels: 
1. Under Quick Setup, click the VPN sub-menu and under Tunnel, click ‘+’. The Tunnel configuration 
parameters appear. Each group of parameters will be described in the order in which they appear. 
2. Under Tunnel, define the following:  
 
Tunnel number (upper field) – unique identifier for the tunnel on the router or firewall.  It 
allows the device to manage multiple tunnels. Range: 1-30 
 
Router Number (lower field) – router associated with the tunnel. Range 1-10. Default = 1 
4. Configuration and Management 
 
 
In the Tunnel Type field, define the encapsulation mode. (The Network parameters will vary 
according to the Tunnel Type selection.) 
 
 
IPsec - Encrypts traffic to provide confidentiality, integrity, and authentication. Most 
commonly used for site-to-site VPNs. 
 
GRE-ip - used for packet encapsulation and routing multiple protocols over networks 
that do not natively support that protocol. No encryption.  
 
GRE-over-IPsec Tunnel Mode - GRE tunnel is encapsulated inside an IPsec tunnel using 
tunnel mode.  The entire GRE packet (including the original IP header) is encrypted 
Traffic inside the GRE tunnel by IPsec. Used in site-to-site VPN where multiple protocols 
or routing updates secure transfer. 
 
GRE-over-IPsec Transport Mode - GRE tunnel is combined with IPsec using transport 
mode.  Only the payload of the GRE packet is encrypted. Used in situations where the 
header must remain visible.  
 
Assign Name – tunnel name. It is recommended to assign the tunnel a recognizable name. 
For example, vpn-mgmt-hq. 
 
Set Admin Status as Up. This allows functioning channel to be monitored.   (Set as Down for 
maintenance, testing, temporarily unused, etc.). 
3. Define the Network parameters. The parameters vary according to the Tunnel Type.  Below is 
the gre-over-ipsec-tunnel-mode example, and the screen, showing all the parameters.  
4. Configuration and Management 
 
Example of a GRE-IPSEC Over Wired Topology 
 
Note 
Multipoint and tunnel underlay parameters are not relevant for all tunnel types. The 
relevant tunnel types will be indicated in the parameter descriptions. 
 
 
Gre-over-ipsec-tunnel-mode Screen 
The following parameters are relevant for all tunnel types:  
 
Tunnel Source interface – interface sourcing traffic to be routed through the tunnel. 
Select either Port or IP. Additional parameters will become available according to your 
selection: 
 
Port – Cellular (with supported service), or Ethernet (configure port and 
optionally VLAN). 
 
IP – set the source address (e.g. 10.10.10.10) 
 
Tunnel Destination – IP Address of peer device to which packets are addressed (e.g. 
10.10.10.50). 
 
IP Address – internal IP address of tunnel: 
4. Configuration and Management 
 
Static – manually configured address on both ends. Assign any address (e.g. 
40.40.40.1/24) 
 
Negotiated – dynamically assigned during tunnel setup.   
The following parameters are relevant for specific tunnel types: 
 
Multipoint – for all tunnel types other than ipsec. When enabled, supports multipoint 
remote peers. If enabled, set NHRP, and NHRP Registration Timeout to ON.  
 
Underlay – only for gre-over-ip-tunnel-mode. The underlay parameters define the real 
routable IP address of the tunnel: 
- Tunnel Underlay Source – Port or IP, where Port can be Cellular or Ethernet with 
optional VLAN. The IP can be Static or Dynamic according to your network.  For 
example, static IP with the source address 192.168.10.11. 
-  Tunnel Underlay Destination address – e.g. 192.158.50.11. 
4. Configure the Local Subnet and Remote Subnet to 0.0.0.0/0 so that all devices in the subnet are 
supported by the tunnel: 
 
5. Configure the Authentication. 
 
 
Authentication Method: 
 
pre-share key – provided encryption key. If selected, enter a password (to be shared). If 
you want to encrypt the key display, choose hash or hash-2.  
 
rsa-signature – provided authentication certificate. If selected, enter the certificate 
name. 
 
IKE Version – Select the IKE version compatible with your products: 
 
IKEv2 (2) default 
 
IKEv1 (1) usually for legacy devices 
4. Configuration and Management 
6. Phase 1 – identity strings used by each side for identification during authentication. The identity 
types must match on the local and remote devices. Select from the drop-down menus, the 
relevant options: 
 
IKE Local ID – how this device identifies itself to the peer. Options are as follows: 
 
Default-address (default) – device sends interface IP address automatically as the Local 
ID.   
 
Address (Manual IP) – device sends a manually defined IP address as the Local ID.  
 
Default-hostname – device sends the system hostname as the Local ID.  
 
Hostname (Manual FQDN) – device sends a manually defined specific FDQN string.  
 
IKE Remote ID – identity expected from the remote side. Options are as follows: 
 
Default-address (default) – the system expects the peer to identify itself as its real IP 
address.  
 
Address (Manual IP) – expects peer to send a specifically defined IP address as its IKE 
identity.   
 
Hostname (Manual FQDN) – expects the peer to identify as a specifically defined FQDN.  
 
IKE SA Lifetime – sets the duration of the IKE (Phase I) tunnel and determines how often 
new encryption keys are generated by the control channel. (It does not control the IPsec 
data traffic lifetime). Default = 86400 (sec). 
 
 
7. Phase 2 parameters. 
 
Define as follows: 
 
Transform Set – assign the channel number assigned in IPsec Transform Set. 
 
Group – assigned the group number set in the ISAKMP Policy. 
 
SA Lifetime – security definitions for expiration of key. Rekey required when the defined 
limit in time or in traffic KB is reached.  
 
Seconds – Range: 60 to 86400; Default = 3600 
 
Kilobytes – 76800 to 110592000; Default = 4608000 
8. Click Submit All. 
4. Configuration and Management 
Verifying Definitions and Monitoring Tunnels 
1. In the side menu, click Configure, and in the displayed dialog, click on the Router number. 
 
2. Scroll to Tunnel Interface.  
 
3. Click on the tunnel to be monitored (e.g. gre-ip). The tunnel interface parameters screen appears. 
Parameters can be turned on and off. To save changes, click Submit. 
 
Additional screen areas show traffic and other parameters. Below is a partial screen. 
 
4. Configuration and Management 
 

## 4.3 SNMP-Based Network Management  *(p.220)*

4. Configuration and Management 
 
4.3 SNMP-Based Network Management  
Configuring SecFlow-1p for SNMP Management Access 
SecFlow-1pcan be managed via SSH or by any SNMP-based network management station (NMS), 
provided you preconfigure the basic parameters using a terminal connected to the SecFlow-1p control 
port. 
In the case that SecFlow-1p is to be managed by the RADview family of network management stations, 
IP communication must be established with the management station, as well as with the standalone 
RADview stations. 
 To configure SecFlow-1p for management access: 
1. Add a router interface, bind it to the Ethernet port, and add a static route to the next hop. 
#*********************Configuring_Router_Interface************* 
configure router 1 
  interface 1 
    bind Ethernet 1  
    address 172.18.141.39/24 
    no shutdown 
  exit 
  static-route 172.17.0.0/16 address 172.18.141.1 
exit all 
save 
 

## 4.4 NETCONF-Based Network Management  *(p.221)*

4. Configuration and Management 
Working with RADview  
RADview is a Windows- or Linux-based modular, client server, scalable management system that can be 
used in a distributed network topology or single-station configuration. RADview features Element 
Manager System (EMS) functionality (referred to as ‘system’) and the following optional modules: 
RADview is a Windows- or Linux-based modular, client server, scalable management system that can be 
used in a distributed network topology or single-station configuration. RADview features Element 
Manager System (EMS) functionality (referred to as ‘system’) and the following optional modules: 
• 
Domain Orchestrator –creates, configures, and manages virtual machines and containers within 
RAD’s customer edge devices.  
• 
Service Manager (SM) – end-to-end intuitive, error-free Carrier Ethernet service provisioning for 
Ethernet and TDM products; calculates the shortest path.  
• 
Performance Monitor (PM) – portal for service SLA monitoring for both carriers and their 
customers. 
RADview supports the following optional modules and functionalities for SecFlow-1p products, as 
described in the following table: 
Modules/Functionalities 
SecFlow-1p 
Element Management System 
(EMS) 
- 
Service Manager (SM) 
- 
Performance Monitor (PM) 
  
D-NFV Orchestrator 
Container Management 
Tasks 
 
Faults 
 
Shelf View 
- 
4.4 NETCONF-Based Network Management 
This feature is applicable to all SecFlow-1p versions. 
For a full explanation and instructions on how to configure and monitor the device using NETCONF, see 
the NETCONF-Based Network Management chapter below.  
4. Configuration and Management 
 