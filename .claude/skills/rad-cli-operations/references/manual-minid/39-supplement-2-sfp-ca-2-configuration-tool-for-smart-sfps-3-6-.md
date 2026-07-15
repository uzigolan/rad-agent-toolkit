# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 3.6 CLI-Based Configuration

*Manual `MiNID_ver_2_6_mn.pdf`, pages 63–71.*


## Working with Telnet/SSH  *(p.63)*

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

## Login  *(p.66)*


## Using the CLI  *(p.66)*

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