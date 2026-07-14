# 10 Administration

*Manual `MP-1-mn_ver 2.2.pdf`, pages 377–404.*


## 10.1 MAC Address Allocation  *(p.377)*

This chapter covers administrative tasks such as entering contact info, file management, etc. In addition, this 
section instructs you on resetting the unit. 
This chapter describes administrative features: 
• 
CPU and Memory Utilization 
• 
Device Information 
• 
Environment 
• 
File Operations 
• 
Inventory 
• 
Login Banner 
• 
Reset 
• 
Tech-Support Commands 
10.1 MAC Address Allocation  
There are several entities that are MAC addresses ‘clients’. The table below describes the MAC allocation in 
Megaplex-1. 
Entity 
Comment 
MAC Address  
Displayed Under 
Host  
 
Used as device identifier in some 
protocols 
MAC1 
 
system# show device-
information 
 
PW with MEF-8 
encapsulation 
 
ETH MNG port 
 
 

## 10.2 Memory Utilization  *(p.378)*

Megaplex-1 
10. Administration 
Entity 
Comment 
MAC Address  
Displayed Under 
MNG RI  
Management RI is identified by 
‘allow-all’ attribute under 
config>router(1)# interface 
<int-num> management-access 
 
RI used for PW with 
UDP/IP encapsulation  
PW RI is identified by ‘allow-
ping’ attribute under 
config>router(1)# interface 
<int-num> management-access 
All such RIs share the same MAC 
(while residing on different 
VLANs) 
MAC2 
svi(<svi number>)# show 
status 
Ethernet ports 
For future use with GbE 1, GbE 2 
and FE ports, respectively 
MAC3, MAC4, 
MAC5 
 
 
Note 
All the four entities (Host, MEF, ETH-MNG and MNG-RI) are using the same 
MAC (MAC1).  
10.2 Memory Utilization 
You can view the memory buffer and pool usage. 
 To display memory pool usage: 
1. From the system context (config>system), enter the following to display memory pool usage: 
show memory 
The memory pool usage is displayed, showing the total amount allocated to the pool, as well as the 
amount that is free.  
config>system# show memory 
                       Kernel      Kernel 
                     Total (KB)  Free (KB) 
--------------------------------------------------------------- 
Memory               3166141899  1051027919 
2. From the system context (config>system), enter the following to display details of memory pool usage: 
show memory–details 

## 10.3 Device Information  *(p.379)*

Megaplex-1 
10. Administration 
config>system# show memory-details 
Kernel Total(KB)    : 3166141899         Free     : 1051027919 
10.3 Device Information 
The Megaplex-1 management software allows you to assign a name and description to the unit, specify its 
location to distinguish it from the other devices installed in your system, and assign a contact person. 
Standards 
The commands below are based on RFC 3841. 
Configuring Parameters 
 To configure device information: 
3. Navigate to configure system. 
The config>system# prompt is displayed. 
4. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning device name 
name <device-name> 
The device name can be any length; however, the 
device prompt displays only up to 20 characters, 
therefore if you enter a name with more than 
20 characters, the prompt displays the first 
19 characters followed by *. You can view the 
complete device name by typing 
show device-information. 
For example, a command that defines a device with a 
name longer than 20 characters: 
# config sys name 
12345678901234567Megaplex-1 
results in this prompt: 
12345678901234567Me*# 
Specifying location 
location <device-location> 
 

## 10.4 Environment  *(p.380)*

Megaplex-1 
10. Administration 
Task 
Command 
Comments 
Specifying contact 
person 
contact <contact-person> 
 
Displaying device 
information, MAC 
address, and amount 
of time device has 
been running 
show device-information 
 
 
Example
 To display device information:  
MP-1>config>system# show device-information 
Description     : MP-1,  HW: 0.0,  SW: 2.00(0.23) 
Name            : MP-1 
Location        : The location of this device 
Contact         : Name of contact person 
MAC Address     : 00-20-D2-58-92-ED 
Engine Time     : 2 days, 00:39:06 
 
10.4 Environment  
You can define the temperature threshold of a chassis and display information about chassis components. 
Configuring the Temperature Threshold 
You can define minimum and maximum temperature thresholds, as well as temperature unit (Celsius or 
Fahrenheit), in order to receive trap notification that the device temperature has left the allowed range or 
returned to the allowed range.  
Megaplex-1 
10. Administration 
You can optionally use a hysteresis mechanism to avoid sending an excessive amount of traps when a threshold 
is repeatedly crossed. The hysteresis defines the margin around the temperature thresholds for sending trap 
notification of temperature threshold crossed: 
• 
Sends trap notification of temperature too high when the temperature rises above <maximum 
temperature + hysteresis value>.  
• 
After sending a trap notification of temperature too high, it sends a trap notification of temperature OK 
when the temperature falls below <maximum temperature - hysteresis value>.  
• 
Sends trap notification of temperature too low when the temperature falls below <minimum 
temperature - hysteresis value>. 
• 
After sending a trap notification of temperature too low, it sends the trap notification of temperature 
OK when the temperature rises above <minimum temperature + hysteresis value>. 
 To configure the temperature threshold: 
5. Navigate to configure chassis. 
The config>chassis# prompt is displayed.  
6. Type:  
temperature-threshold {celsius | fahrenheit} min <min-value-30..10, default -15> max <max-value 
60..90, default 80> [hysteresis <hysteresis-value 2..10, default 5> ] 
The temperature thresholds are set as specified.  
Viewing Environment Information  
You can display information about the type and status of the power supplies.  
 To display the information: 
7. Navigate to configure chassis. 
The config>chassis# prompt is displayed. 
8. Enter: 
show environment  
The information is displayed as shown in the examples below.  
The power supply type is indicated as AC, DC, or -- (if it is absent or has failed). 

## 10.5 Inventory  *(p.382)*

Megaplex-1 
10. Administration 
Examples 
 To define temperature thresholds: 
• 
Minimum temperature = -20 degrees Celsius 
• 
Maximum temperature = 50 degrees Celsius 
• 
Hysteresis = 4 
exit all 
>configure chassis 
>config chassis#  
  temperature-threshold celsius min -20 max 50 hysteresis 4 
  exit all 
save 
 
 To view environment information: 
configure chassis 
config>chassis# show environment 
        
Power Supply   Type      Status 
--------------------------------------------------------------- 
1              AC-DC    OK 
2              AC-DC    Failed 
3              DC           OK 
10.5 Inventory  
The Megaplex-1 inventory table displays the unit’s components, hardware and software revisions, and power 
supply types. You can display an inventory table that shows all installed components, and you can display more 
detailed information for each component. You can configure an alias name, asset ID, and serial number for 
inventory components.  
Standards 
The inventory feature is implemented according to RFC 4133 – Entity MIB (RFC 2737 was made obsolete by 
RFC 4133 version 3). 
Megaplex-1 
10. Administration 
Benefits 
You can monitor the installed components and hardware/software revisions. 
Viewing Inventory Information 
 To display the inventory table: 
• 
At the config>chassis# prompt, enter: 
show summary-inventory 
The inventory table is displayed (see Example for a typical inventory table output). 
You can display more information for each installed inventory component. To do so, you need to enter the 
inventory level with the corresponding inventory component index, which is displayed in the Index column in 
the output of show summary-inventory.  
 To display the inventory component information: 
1. Navigate to configure chassis inventory <index>. 
2. Enter: 
show status 
Information for the corresponding inventory component is displayed (for information on the parameters 
see the following table). 
Parameter 
Description 
Description 
Description of component type, in the form: 
RAD.<device-name>.< Physical  Class> 
Contained In 
Index of the component that contains the component for which information is 
being displayed. This is 0 for the chassis, as it is not contained in any component, 
and 1001 for all other components, as they are all contained in the chassis. 
Physical Class 
Class of component 
Possible values: Chassis, CPU, Power Supply, Fan, Sensor, Port, Container, 
Module 
Relative Position 
Contains the relative position of this component among other components in 
the same index range (e.g. index 4001–4002, etc.) 
 
 
Megaplex-1 
10. Administration 
Parameter 
Description 
Name 
Name of component.  
Possible values (according to component type):  
1001    Chassis        MP-1                      
3002    Container      Gbe SFP 1 
3003    Container      Gbe SFP 2 
4001    Power Supply   PS_DC               
4002    Power Supply   PS_AC/DC                  
4003    Power Supply   PS_AC/DC                  
4004    Sensor         SENSOR                    
5001    Module         Data Interface Module     
5004    Module         SERIAL Interface Module   
5005    Module         E1/T1 Interface Module    
7001    Port           E1/T1.Port 1 
7002    Port           E1/T1.Port 2 
7003    Port           E1/T1.Port 3 
7004    Port           E1/T1.Port 4 
7005    Port           E1/T1.Port 5 
7006    Port           E1/T1.Port 6 
7007    Port           E1/T1.Port 7 
7008    Port           E1/T1.Port 8 
7009    Port           Serial.Port 1 
7010    Port           Serial.Port 2 
7011    Port           Serial.Port 3 
7012    Port           Serial.Port 4 
7013    Port           Serial.Port 5 
7014    Port           Serial.Port 6 
7019    Port           Gbe Port 1 
7020    Port           Gbe Port 2 
7021    Port           Fe Port 3 
7022    Port           Fe Port 4 
7023    Port           Fe Port 5 
7024    Port           Fe Port 6 
7025    Port           MNG Port 
7026    Port           Clock RJ45 Port 
7027    Port           RS_232 Control Port 
7028    Port           Alarm Port 
 
 
HW Rev 
Hardware version (relevant only for chassis) 
SW Rev 
Software version (relevant only for chassis) 
 
FW Rev 
Firmware version (relevant only for chassis) 
Serial No. 
Serial number (blank if unknown for component) 
MFG Name 
Manufacturer name (blank if unknown for component) 
Model Name 
Model name (blank if unknown for component) 
Megaplex-1 
10. Administration 
Parameter 
Description 
Alias 
Alias name for component  
Asset ID  
Identification information for component  
FRU 
Indicates whether this component is a field replaceable unit that can be 
replaced on site. 
Setting Administrative Inventory Information 
If necessary, you can configure the alias, asset ID, and serial number for inventory components. To configure the 
information, you need to enter the inventory level with the corresponding inventory component index shown in 
the Index column in the output of show summary-inventory.  
 To set inventory component information: 
1. Navigate to configure system inventory <index>. 
The config>system>inventor(<index>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning user-defined alias to 
component  
alias <string> 
Using no before alias removes 
the alias. 
Note: Configuring the alias is 
meaningful only for the chassis 
component. It can be used by a 
network manager as a 
non-volatile identifier for the 
device. 
Assigning user-specific asset 
identifier to the component 
(usually for  removable physical 
components) 
asset-id <id> 
Using no before asset-id 
removes the asset ID. 
Assigning vendor-specific serial 
number to the component 
serial-number <string> 
Using no before serial-number 
removes the serial number. 
Examples  
 
Megaplex-1 
10. Administration 
 To display inventory summary for MP-1/PSR/2GES/4FEU/6S/4E&M:  
MP-1>config>system# show summary-inventory 
 
Index   Physical Class Name                     HW Ver    SW Ver     FW Ver 
---------------------------------------------------------------------------- 
 
1001    Chassis        MP-1                     0.0/A/0.0  2.20(0.35) 0x2131 
3002    Container      Gbe SFP 1 
3003    Container      Gbe SFP 2 
4001    Power Supply   PS_DC                    0.0 
4002    Power Supply   PS_AC/DC                 0.0 
4003    Power Supply   PS_AC/DC                 0.0 
4004    Sensor         SENSOR                   0.0 
5001    Module         Data Interface Module    1.0/0.1 
5004    Module         SERIAL Interface Module  0.0/0.0 
5005    Module         E&M Interface Module     0.0/0.0 
7001    Port           Serial.Port 1 
7002    Port           Serial.Port 2 
7003    Port           Serial.Port 3 
7004    Port           Serial.Port 4 
7005    Port           Serial.Port 5 
7006    Port           Serial.Port 6 
7007    Port           Voice(E&M).Port 1 
7008    Port           Voice(E&M).Port 2 
7009    Port           Voice(E&M).Port 3 
7010    Port           Voice(E&M).Port 4 
7019    Port           Gbe Port 1 
7020    Port           Gbe Port 2 
7021    Port           Fe Port 3 
7022    Port           Fe Port 4 
7023    Port           Fe Port 5 
7024    Port           Fe Port 6 
7025    Port           MNG Port 
7026    Port           Clock RJ45 Port 
7027    Port           RS_232 Control Port 
7028    Port           Alarm Port 
    
 To display inventory summary for MP-1/PSR/2GES/4FEU/6S/8E1T1: 
MP-1>config>chassis# show summary-inventory 
Index   Physical Class Name                     HW Ver    SW Ver     FW Ver 
---------------------------------------------------------------------------- 
1001    Chassis        MP-1                     0.0/B/0.0 2.20(0.35) 0x2131 
Megaplex-1 
10. Administration 
3002    Container      Gbe SFP 1 
3003    Container      Gbe SFP 2 
4001    Power Supply   PS_DC                    0.0 
4002    Power Supply   PS_AC/DC                 0.0 
4003    Power Supply   PS_AC/DC                 0.0 
4004    Sensor         SENSOR                   0.0 
5001    Module         Data Interface Module    1.0/0.1 
5004    Module         SERIAL Interface Module  0.0/0.0 
5005    Module         E1/T1 Interface Module   0.0/0.0 
7001    Port           E1/T1.Port 1 
7002    Port           E1/T1.Port 2 
7003    Port           E1/T1.Port 3 
7004    Port           E1/T1.Port 4 
7005    Port           E1/T1.Port 5 
7006    Port           E1/T1.Port 6 
7007    Port           E1/T1.Port 7 
7008    Port           E1/T1.Port 8 
7009    Port           Serial.Port 1 
7010    Port           Serial.Port 2 
7011    Port           Serial.Port 3 
7012    Port           Serial.Port 4 
7013    Port           Serial.Port 5 
7014    Port           Serial.Port 6 
7021    Port           Fe Port 3 
7022    Port           Fe Port 4 
7023    Port           Fe Port 5 
7024    Port           Fe Port 6 
7025    Port           MNG Port 
7026    Port           Clock RJ45 Port 
7027    Port           RS_232 Control Port 
7028    Port           Alarm Port 
 To display inventory information for the Megaplex-1 chassis: 
MP-1>config>system>inventory(1001)# show status 
Description       : MP-1.chassis MP-1/PSR/2GES/4FEU/6S/4E&M 
Contained In      : 0 
Physical Class    : Chassis 
Relative Position : 0 
Name              : MP-1 
HW Ver            : 0.0/A/0.0 
SW Ver            : 2.20(0.35) 
FW Ver            : 0x2131 
Serial Number     : 00-20-D2-5B-00-FF 

## 10.6 Login Banner  *(p.388)*

Megaplex-1 
10. Administration 
MFG Name          : RAD 
Module Name       : chassis 
Alias             : chassis 
Asset ID          : 
FRU               : True 
 To display inventory information for the Et1/T1 Port 6: 
MP-1>config>chassis>inventory(5005)# show status 
Description       : E1/T1 
Contained In      : 1001 
Physical Class    : Module 
Relative Position : 6 
Name              : E1/T1 Interface Module 
HW Ver            : 0.0/0.0 
SW Ver            :  
FW Ver            :  
Serial Number     : 
MFG Name          : RAD 
Module Name       : IntModule-MP-1/E1/T1 
Alias             : IntModule-MP-1/E1/T1 
Asset ID          : 
FRU               : True 
 
10.6 Login Banner 
Defining Login Banners 
You can define a banner to be displayed before the login prompt for user name, as well as a banner to be 
displayed following successful login. You can define the pre-login banner using the CLI command login-message, 
and the post-login banner using the CLI command announcement. A banner file can also be used to define a 
pre-login banner, provided it is supported in the device. Although the banner file is maintained for backward 
compatibility, it is recommended to use a CLI command to define the pre-login banner. Note that a device 
cannot simultaneously support a banner file and banner command.  
Note 
If you are accessing Megaplex-1 via SSH, the banner is printed between the 
user name prompt and the password prompt.  
Megaplex-1 
10. Administration 
Defining Login Banners via CLI Commands 
You can define a banner to be displayed before login, as well as another banner to be displayed following login. 
Pre-login and post-login banner messages must satisfy the following: 
• 
Message must be enclosed in single quotation marks. 
• 
Pressing <Enter> before entering a closing quotation mark, results in the device displaying the warning 
message: 
Enter message.  End with the single quotation character (‘). 
• 
A message that spans multiple lines is interpreted as if it were written in one line; <cr> and <lf> between 
lines in the configuration file or command are ignored.  
• 
A message can contain printable characters, as well as the following special characters (only relevant for 
CLI; from SNMP, these characters should be entered normally): 
 
\n – new line 
 
\t – horizontal tab 
 
\’ – single quotation mark 
 
\\ – backslash 
• 
Usage of special characters reduces the maximum number of printable characters that the banner can 
contain. For example, if the banner contains \n, up to 1998 additional printable characters can be used. 
• 
The banner can be up to 2000 characters (including the escape / characters). If you try to configure a 
longer banner, the device prints the following CLI error: Banner may not exceed 2000 characters. 
 To configure a pre-login banner: 
1. Navigate to configure system. 
The config>system# prompt is displayed. 
2. Type login-message <message>, enclosing the message in quotes. 
At the next login, this pre-login banner is displayed. 
If a banner­text file already exists in the device, the device rejects the command and displays the CLI 
error message: 
Cannot configure banner while banner­text file exists 
Note 
Type no login-message to remove a previously configured pre-login banner.  
 To configure a post-login banner: 
Navigate to configure system. 
The config>system# prompt is displayed. 
Megaplex-1 
10. Administration 
3. Type announcement <message>, enclosing the message in quotes. 
After the next login, this post-login banner is displayed. 
Note 
Type no announcement to remove a previously configured post-login banner.  
You can display the banners configured for Megaplex-1 by navigating to the device level and entering info. For 
example:  
info  
    configure  
        echo "System Configuration" 
#       System Configuration 
        system  
            login-message 'Authorized Users Only'  
            announcement 'Successful Login!'  
        exit 
The configured banners are displayed before and after login, as shown below. 
Authorized Users Only 
user>su 
password>**** 
 
 
Successful Login! 
# 
Defining Pre-Login Banner Using a Banner File 
 To define the banner using a banner file: 
Create a text file called banner-text that contains the banner to display. 
Note 
• 
The banner must contain only printable ASCII characters (0x20–0x7E), 
<Enter> (0x0D), <Line Feed> (0x0A), and <Tab> (0x09) 
• 
The banner can contain up to 2,000 characters.  
4. Transfer the file banner-text to Megaplex-1. 
At the next login, the banner is displayed. 
If the device already contains the pre-login CLI command login-message, the device rejects the banner-
text file download and displays the CLI error: Cannot load banner­text file while login-message is 
configured. 
You can display the banner defined for Megaplex-1 by navigating to the file level and entering show 
banner-text, as shown in the example below. 

## 10.7 Reset  *(p.391)*

Megaplex-1 
10. Administration 
# file  
file# show banner-text 
******* Authorized users only ******* 
Given the above banner file, the banner is displayed before login, as shown below. 
******* Authorized users only ******* 
user> 
10.7 Reset 
 
Note 
This section describes how to reset using CLI commands. You can also reset 
the device to its factory defaults or user configured defaults by pressing the 
push button on the front panel. For details, refer to the description on 
resetting the device in the Operation chapter.  
Megaplex-1 supports the following types of reset: 
• 
Reset to factory defaults  
• 
Reset to user defaults 
• 
Overall reset (restart) of the device. 
Resetting to Factory Defaults 
Megaplex-1 can be reset to its factory defaults using either of the following commands:  
• 
factory-default – for customer use 
• 
factory-default-all – for use by RAD Operations personnel prior to releasing the device for shipment, in 
order to revert the device to its prior-to-shipment state 
The factory-default and factory-default-all commands have the following differences:  
• 
factory-default always reloads the device with factory-default-config. factory-default-all reloads the 
device with user-default-config, if it exists; otherwise, with factory-default-config. 
• 
factory-default only deletes startup-config.  
factory-default-all clears the log files and deletes most files, with the exception of 
factory-default-config, user-default-config, banner, software, mac-table, pm (including the legacy 
statistics collection file), db-schema,  and db-config. It also resets file creation times in the file system.  
Megaplex-1 
10. Administration 
• 
factory-default-all resets the snmpEngineBoots parameter to 1. This parameter counts the number of 
times the SNMP engine was restarted, and is maintained throughout reboots to prevent replay attacks. 
Note 
It is not recommended for customers to use the factory-default-all command, 
as it resets the SNMP object (snmpEngineBoots), which could lead the 
management station to assume that the original device was replaced by 
another impersonating device, and therefore refusing to communicate with it. 
In such cases, the manager must manually delete the device from the map 
and then redraw it. Therefore, to avoid issues resulting from the resetting of 
snmpEngineBoots, it is recommended to use instead user-default or 
factory-default and then manually delete unneeded files and clear logs, as 
required.  
 To reset Megaplex-1 to factory defaults: 
At the admin# prompt enter: 
factory-default 
A confirmation message is displayed: 
Current configuration will be erased and device will reboot with 
factory default configuration. Are you sure? [yes/no] 
5. Enter yes to confirm resetting to factory defaults. The device automatically reboots. 
 To reset Megaplex-1 to factory defaults and revert the device to its prior-to-shipment state: 
6. At the admin# prompt enter: 
factory-default-all 
A confirmation message is displayed: 
The device will delete its entire database and reboot. Are you sure? 
[yes/no] 
7. Enter yes to confirm the reset to factory defaults with configuration and counter reset. 
The configuration and counter reset explained above is performed, the unit resets, and after it 
completes its startup the factory defaults are loaded. If a startup-config confirm request was active, it is 
canceled. 
Resetting to User Defaults 
You can use the user-default command to reset Megaplex-1 to the configuration stored in user-default-config, a 
file which contains user default parameters that are usually different from RAD’s factory default parameters. 

## 10.8 Tech-Support Commands  *(p.393)*

Megaplex-1 
10. Administration 
 To reset Megaplex-1 to user defaults: 
8. At the admin# prompt enter: 
user-default 
A confirmation message is displayed: 
Current configuration will be erased and device will reboot with user 
default configuration. Are you sure? [yes/no] 
 
9. Enter yes to confirm resetting to user defaults. The device automatically reboots. 
Restarting the Unit 
If necessary, you can restart Megaplex-1 without interrupting the power supply. 
 To restart Megaplex-1: 
At the admin# prompt enter: 
reboot 
A confirmation message is displayed: 
Device will reboot. Are you sure? [yes/no] 
10. Enter yes to confirm the reset. 
The unit restarts. 
 
.  
10.8 Tech-Support Commands  
Megaplex-1 supports a show tech-support command, which you can use to display on the terminal or store in a 
script file a predefined series of CLI commands, such as general device status and statistics.  
Benefits 
You can view or save in a file general device status and statistics. 
Megaplex-1 
10. Administration 
Factory Defaults 
By default, the show tech-support command is predefined with the following commands in order:  
• 
show configure system system-date 
• 
show configure system device-information 
• 
show configure system memory-details 
• 
show configure system buffers 
• 
show configure system summary-inventory 
• 
show file sw-pack 
• 
show file copy 
• 
show configure port summary 
• 
show configure service   
• 
show configure pwe summary 
• 
show configure system clock domain1 status 
• 
show configure router 1 routing-table 
• 
show configure management users-details 
• 
show configure reporting active-alarms 
Functional Description 
When the tech-support command is invoked, its output is displayed on your terminal or stored in a script file 
called script-result, which can afterwards be displayed or downloaded. 
For each command, the following is displayed: 
• 
A timestamp – formatted <date> <time> UTC {+|-}<hours>:<minutes>; for example: 2015-05-35 11:10:09 
UTC +02:00 
• 
The executed command 
• 
The command output, including errors and other messages, provided that the command was invoked 
with the terminal argument (If the file argument is invoked, the command output is stored in a file 
instead of being displayed on the CLI terminal.) 
Unlike other commands, the output is sent to the screen continuously, without pausing after each page. 

## 10.9 File Operations  *(p.395)*

Megaplex-1 
10. Administration 
The CLI prompt does not return until all commands included in the script are executed, or you stop the 
execution. 
The terminal inactivity timer does not decrease while the script is being executed, so the terminal remains open 
even if it takes a long time. 
The script-result file is automatically cleared each time the show tech-support command is invoked.  
Showing the Tech-Support Commands 
 To show the tech support commands: 
Navigate to configure system. 
The config>system# prompt is displayed. 
1. At the config>system# prompt, enter show tech-support [file | terminal]. 
The commands and their output are displayed. 
10.9 File Operations  
You can perform the following operations: 
• 
Transfer files via SFTP/TFTP 
• 
Copy files within the unit 
• 
Display files 
• 
Delete files 
You can copy or transfer files via the copy command, or via the commands shown in Table 10-2. As shown in the 
table, some commands that reset the device also erase the saved user configuration by copying another file to it 
before the reset. 
Megaplex-1 
10. Administration 
Commands That Copy Files 
Command 
Level 
Copies… 
Additional 
Actions 
Manual Section 
save 
Global 
running-config to startup-config 
None 
Saving Configuration 
Changes (in Operation 
chapter) 
factory-default 
Admin 
factory-default to startup-config 
Unit resets 
after copying 
Resetting to Factory 
Defaults 
user-default 
Admin 
user-default-config to 
startup-config 
Unit resets 
after copying 
Resetting to User 
Defaults 
Using SFTP or TFTP 
You can download or upload files to the Megaplex-1 unit via SFTP/TFTP. Normally the types of files copied are 
configuration files and software files. 
The software files can also be downloaded to Megaplex-1 via the Boot Manager, using XMODEM, FTP, or TFTP. 
For details on upgrading the device software, refer to the Software Upgrade chapter. 
SFTP Application 
The SFTP protocol is used to provide secure file transfers via the product's Ethernet interface. SFTP is a version 
of FTP that encrypts commands and data transfers, keeping your data secure and your session private. For SFTP 
file transfers, an SFTP server application must be installed on the local or remote computer. 
A variety of third-party applications offer SFTP server software. For more information, refer to the 
documentation of these applications. 
If you use a local laptop and SFTP is the preferred transfer method, a SFTP server application must be installed 
on it.  
As mentioned above, third-party applications are available and you should refer to their setup documentation. 
Note 
SFTP file transfers are carried out through TCP port 22. You should check that 
the firewalls you are using on the server and Windows allow communication 
through this port. If not, configure the firewall settings to open TCP port 22.  
Megaplex-1 
10. Administration 
TFTP Application 
The TFTP protocol is typically used for remote IP-to-IP file transfers via the product's Ethernet interface. It can be 
used, however, for local file transfer as well, as the transfer rate of the Ethernet interface is much faster than 
that of the RS-232 interface. 
For TFTP file transfers, a TFTP server application must be installed on the local or remote computer. As it runs in 
the background, the TFTP server waits for any TFTP file transfer request originating from the product, and 
carries out the received request automatically.  
A variety of third-party TFTP applications are available that allow the instant creation of a TFTP server on a client 
computer. For more information, refer to the documentation of these applications. 
If you use a local laptop and TFTP is the preferred transfer method, a TFTP server application must be installed 
on it.  
As mentioned above, third-party applications are available and you should refer to their setup documentation. 
Note 
TFTP file transfers are carried out through TCP port 69. You should check that 
the firewalls you are using on the server and Windows allow communication 
through this port. If not, configure the firewall settings to open TCP port 69.  
Copying Files 
You can use the copy command to copy files within the Megaplex-1 unit, or download/upload files to the 
Megaplex-1 unit via SFTP/TFTP.  
 To copy files: 
• 
At any prompt, enter: 
copy <source-file-url> <destination-file-url> 
Where: 
• 
<file-url> = <url-prefix> <file> 
• 
<url-prefix> can be empty, or one of the following: 
 
tftp://<ipv4-address>/ 
 
sftp://<username>:<password>@<ipv4-address>[:<port>]/ 
 
xmodem: 
Note 
It is not necessary to specify <port> when using the well-known SFTP port.  
Megaplex-1 
10. Administration 
• 
<file> can be empty, or one of the following files, or the file name on a remote computer if applicable. If 
<file> is on a remote computer it can contain a path and file name, or just a file name.  
 
startup-config 
 
running-config 
 
candidate-config 
 
user-default-config 
 
factory-default-config 
 
log 
 
sw-pack-1 
 
sw-pack-2 
 
banner-text 
 
db-schema 
 
mac-table 
 
db-config 
• 
The maximum length/range is: 
 
<username> – 1–60 characters 
 
<password> – 1–32 characters 
 
<file> – 1–96 characters 
 
<port> – 1–65535 
Examples 
Copying Files Within Device 
• 
Source file name – running-config 
• 
Destination file name – startup-config 
copy running-config startup-config 
 Example 1: 
• 
Source file name – running-config  
• 
Destination file name – startup-config. 
# file 
file# copy running-config startup-config 
Example 2: 
Megaplex-1 
10. Administration 
• 
Source file name – log  
• 
Destination file name – LOG_oos1 on tftp://172.17.151.59. 
file# copy log tftp://172.17.151.59/LOG_oos1 
Are you sure? [yes/no] _ y 
file# 
***** 
File copy command was completed.***** 
 
*****log copied to tftp://172.17.151.59/LOG_oos1 successfully***** 
*****1025606 bytes copied in 4 secs (256401 bytes/sec)***** 
Note 
Due to a large file volume, copying starts after 30 sec of processing .  
 To display the last copy command result: 
• 
At the file# prompt, enter: show copy. 
# show file copy 
Network to Device, Transferring Data 
Src: tftp://172.17.174.56/mp4cl2_03_00b06.bin 
Dst: sw-pack-4 
Started: 14.3.2011 8:50:52 
Transferred : 665600 Bytes in: 16 seconds (41600 Bytes/Second) 
 To view the copy command history:  
• 
At the file# prompt, enter: show copy summary. 
For example: 
file# show copy summary 
Direction      Source            Destination       End Time        
Status 
1   Local      running-config    user-default-conf 13-3-2011    Ended 
OK 
                                                   14:6:51 
2   Local      running-config    startup-config    13-3-2011    Ended 
OK 
                                                   14:7:35 
3   Dev to Net startup-config    DB                13-3-2011    Ended 
OK 
                                                   14:7:40              
 
Megaplex-1 
10. Administration 
Downloading via TFTP  
• 
TFTP server address – 192.10.10.10  
• 
Source file name – d:/img/MP-1.bin 
• 
Destination file name – sw-pack-2 
copy tftp://192.10.10.10/d:/img/MP-1.bin sw-pack-2 
Uploading via TFTP 
• 
TFTP server address – 192.10.10.10 
• 
Source file name – startup-config 
• 
Destination file name – c:/mp/config/db1conf.cfg 
copy startup-config tftp://192.10.10.10/c:/mp/config/db1conf.cfg 
Downloading via SFTP 
• 
SFTP server address – 192.20.20.20 
• 
SFTP user name – admin 
• 
SFTP password – 1234 
• 
Source file name – bin/MP-1.bin 
• 
Destination file name – sw-pack-2 
copy sftp://admin:1234@192.20.20.20/bin/MP-1.bin sw-pack-2  
Note 
Destination file name can be only sw-pack-1 or sw-pack-2.  
Uploading via SFTP 
• 
SFTP server address – 192.20.20.20 
• 
SFTP user name – admin 
• 
SFTP password – 1234 
• 
Source file name – startup-config 
• 
Destination file name – config/db1conf.cfg 
copy startup-config sftp://admin:1234@192.20.20.20/config/db1conf.cfg 
Megaplex-1 
10. Administration 
Viewing Copy Status 
You can display the status of current and past copy operations. 
 To display copy status: 
• 
At the file# prompt, enter: 
show copy [summary] 
Viewing Information on Files  
You can display the following information: 
• 
Files within the device 
• 
Information on the configuration files 
• 
Contents of configuration text files 
• 
Information on the software files (software packs). For information on upgrading to a different software 
pack, refer to the Software Upgrade chapter. 
 To display the files within the device: 
• 
At the file# prompt, enter:  
dir 
A list of the file names and types is displayed.  
For example:  
HyQ_C>file# dir 
Codes: C-Configuration  S-Software  L-License  LO-Log  O-Other 
 
Name                 Type Size(Bytes) Creation Date Status 
 
sw-pack-1              S    13439930   20-5-2014    valid 
                                       11:45:49 
sw-pack-2              S    14052947   5-6-2014     File In Use 
                                       14:30:30 
startup-config         C    37268      21-5-2014    valid 
                                       11:37:1 
user-default-config    C    11983      2-3-2014     valid 
                                       10:18:24 
factory-default-config C    680        1-1-1970     Read Only 
Megaplex-1 
10. Administration 
                                       0:0:9 
running-config         C    --         18-6-2014    Read Only 
                                       15:44:25 
log                    LO   --         18-6-2014    Read Only 
                                       15:44:25 
Total Bytes : 101367808 Free Bytes  : 31295488 
 To display information on the configuration files: 
• 
At the file# prompt, enter:  
show configuration-files 
Information on the configuration files is displayed. 
Example  
MP-1>file# show configuration-files 
Configuration         Last Modified       Valid 
----------------------------------------------------------------------------
- 
startup-config        2017-11-09 15:01:14 Yes 
factory-default-config2017-11-27 15:50:34 Yes 
running-config        2017-11-27 15:51:43 Yes 
 
Device loaded from : startup-config 
 
startup-config equals running-config 
 To display the contents of configuration text files: 
• 
At the file# prompt, enter one of the following: 
 
show factory-default-config 
 
show startup-config 
 
show user-default-config 
The contents of the specified configuration file are displayed. 
 To display information on the software files: 
• 
At the file# prompt, enter:  
show sw-pack [refresh [<sec>]] 
where sec represents the refresh timeout, with range 3–100. 
Information on the software files is displayed. 
Megaplex-1 
10. Administration 
Example  
MP-1>file# show sw-pack 
Name      Version      Creation Time          Actual 
------------------------------------------------------- 
sw-pack-1 2.00(0.07)   2017-08-03   15:07:07  active 
sw-pack-2 2.00(0.02)   2010-12-29   15:15:11  ready 
 
 
sw-pack-1 Size (Bytes)  : 13896488 
 
Type      Name           Version      H/W Ver   Size 
                                                (Bytes) 
--------------------------------------------------------- 
main      main.bin       2.00(0.07)   0.1       13896248 
 
 
sw-pack-2 Size (Bytes)  : 15595868 
 
Type      Name           Version      H/W Ver   Size 
                                                (Bytes) 
--------------------------------------------------------- 
main      main.bin       2.00(0.02)   0.1       15595628 
 
 
MP-1>file# 
Deleting Files 
You can delete files. Before deleting the file, make sure the file is not in use. For additional information on 
configuration files and the consequences of deleting, refer to Configuration Files and Loading Sequence  in 
Chapter 3.  
 To delete a file: 
1. At the file# prompt, enter: delete <file-name>. 
You are prompted to confirm the deletion. 
For example:  
# file 
file# delete sw-pack-1 
File will be erased. Are you sure?? [yes/no] _yes 
Megaplex-1 
10. Administration 
Confirm the deletion. 
The unit reverts to the factory default. 
 