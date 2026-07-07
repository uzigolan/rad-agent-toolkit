# 11 Administration

*Manual `ETX-1p_6.4_Mn_05-26_GA.pdf`, pages 650–678.*


## 11.1 Product Information  *(p.650)*

11.1 Product Information 
The ETX-1p management software allows you to assign a name and description to the product, and 
assign a contact person. 
Applicability and Scaling 
This feature is applicable to all the device versions. 
Standards Compliance 
RFC 3841 - Caller Preferences for the Session Initiation Protocol (SIP)  
Setting Parameters 
 To configure product information: 
1. Navigate to configure system. 
The config>system# prompt is displayed. 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying contact person 
contact <contact-person> 
Typing no contact removes contact person. 
11. Administration 
Task 
Command 
Comments 
Assigning product name 
name <product-name> 
The product name can be 0-255 characters; 
however, the product prompt displays only up to 
20 characters, therefore if you enter a name with 
more than 20 characters, the prompt displays 
the first 19 characters followed by *.  
For example, a command that defines a product 
with a name longer than 20 characters: 
config sys name 12345678901234567ETX-1p  
  
results in this prompt: 
12345678901234567vC*# 
You can view the complete product name by 
typing show device-information. 
Typing no name removes the name entirely. 
Specifying location 
location <device-location> 
 
Displaying copyright 
information 
show copyright 
 
Displaying product 
information, MAC address, 
and amount of time product 
has been running 
show device-information 
 
Displaying information 
output of a predefined 
series of commands 
show tech-support  
Unified output of the following commands: 
• show configure system system-date 
• show configure system device-information 
• show file sw-pack 
• show file copy 
• show configure port summary 
• show configure router 1 arp-table 
• show configure router 1 routing-table 
• show configure management users-details 
Example 
 To configure ETX-1p product information: 
• 
Product name – ETX-1p 
11. Administration 
• 
Location – floor-8 
• 
Contact – Engineer-1 
exit all 
configure system 
  name ETX-1p 
  location floor-8 
  contact Engineer-1 
  exit all 
 
 To display configuration for your needs or for technical support: 
config>system# show tech-support 
# Execute tech-support-script 
 
 
# 2019-08-14 08:41:28 UTC +00:00, system uptime: 67645 seconds 
show configure system system-date 
2019-08-14   08:41:28  UTC  +00:00 
 
 
# 2019-08-14 08:41:28 UTC +00:00, system uptime: 67645 seconds 
show configure system device-information 
Description    : ETX-1p Hw: 0.4, Sw: 5.0.5.23 
Name           : ETX-1p 
Model          : ETX-1P 
Firmware       : ETX-1P/ACEX/1SFP1UTP/4UTP/L1/L1 
Location       : The location of this device                              
Contact        : Name of contact person                                   
MAC Address    : 00-08-A2-0A-BF-68                                        
Engine Time    : 18:44:48   
 
 
# 2019-08-14 08:41:28 UTC +00:00, system uptime: 67645 seconds 
show file sw-pack  
Name           Version      Creation Time          Actual 
----------------------------------------------------------------------------- 
sw-pack-1      5.0.0.40     2019-07-16   06:02:00  active  
 
 
# 2019-08-14 08:41:28 UTC +00:00, system uptime: 67646 seconds 
show file copy 
 
 
# 2019-08-14 08:41:28 UTC +00:00, system uptime: 67646 seconds 
show configure port summary 
 
config>port# show summary 
Panel               Name                     Admin  Oper      Speed 
11. Administration 
----------------------------------------------------------------------------- 
Ethernet wan1       Ethernet wan1            Down   Down      0 
Ethernet wan2       Ethernet wan2            Up     Up        100000000 
Ethernet lan1       Ethernet lan1            Up     Up        100000000 
Ethernet lan2       Ethernet lan2            Down   Down      0 
Ethernet lan3       Ethernet lan3            Down   Down      0 
Ethernet lan4       Ethernet lan4            Up     Up        1000000000 
Cellular lte        Cellular lte             Up     Up        0 
BP 1/1              BP 1/1                   Up     Up        0 
BP 1/2              BP 1/2                   Up     LLD       0 
BP 1/3              BP 1/3                   Up     LLD       0 
Virtual 1           Virtual 1                Down   Down      0 
Virtual 2           Virtual 2                Down   Down      0 
Virtual 3           Virtual 3                Down   Down      0 
Virtual 4           Virtual 4                Down   Down      0 
Virtual 5           Virtual 5                Down   Down      0 
Virtual 6           Virtual 6                Down   Down      0 
Virtual 7           Virtual 7                Down   Down      0 
Virtual 8           Virtual 8                Down   Down      0 
Virtual 9           Virtual 9                Down   Down      0 
Virtual 10          Virtual 10               Down   Down      0 
 
 
 
 # 2019-08-14 08:41:29 UTC +00:00, system uptime: 67646 seconds 
show configure router 1 arp-table 
IP Address          MAC Address         Status 
----------------------------------------------------------------------------- 
 
 
# 2019-08-14 08:41:29 UTC +00:00, system uptime: 67646 seconds 
show configure router 1 routing-table 
IP Address/Prefix Length Next Hop         Interface      Protocol   Metric 
----------------------------------------------------------------------------- 
169.254.0.0/16           0.0.0.0          32             Local      0 
 
IPv6 Address/Prefix Length   via Next Hop       Interface  Protocol    Metric 
----------------------------------------------------------------------------- 
fe80::/64 
via 
0.0.0.0                                         32         Local       0 
 
 
# 2019-08-14 08:41:32 UTC +00:00, system uptime: 67649 seconds 
show configure management users-details 
User:su  Level:su  Popup:Enabled 
        From:Serial  For(sec):438 
 

## 11.2 File Operations  *(p.654)*

11. Administration 
11.2 File Operations 
You can perform the following operations: 
• 
Transfer files via SFTP/SCP/FTP/FTPs 
• 
Copy files within ETX-1p  
• 
Display files 
• 
Delete files 
Applicability and Scaling 
File operations are applicable to all the device versions. 
Functional Description 
For the list of files that ETX-1p supports, refer to Configuration and Software Files. 
User Directory 
The ETX-1p file system contains a directory for user files, called user. The size of the user directory varies 
per device and is determined by the disk space that the device can allocate. You can copy files to and 
from the user directory, and delete files that are not in use. User file names are strings between 1 and 
32 characters long. 
Commands for Copying Files 
You can copy or transfer files via the copy command, or via the commands shown in the table below.  
Some commands that reset ETX-1p also erase the saved user configuration by copying another file to it 
before the reset. 
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
Changes 
11. Administration 
Command 
Level 
Copies… 
Additional 
Actions 
Manual Section 
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
Using SFTP or SCP 
You can download or upload files to ETX-1p via SFTP/SCP. Normally the types of files copied are 
configuration files and software files. 
For details on upgrading the product software, refer to Software Upgrade. 
SFTP Application 
The SFTP protocol is used to provide secure file transfers via the product's Ethernet interface. SFTP is a 
version of FTP that encrypts commands and data transfers, keeping your data secure and your session 
private. For SFTP file transfers, an SFTP server application must be installed on the computer.  
A variety of third-party applications offers SFTP server software. For more information, refer to the 
documentation of these applications. 
 
Note 
SFTP file transfers are carried out through any TCP port (default is 22). You 
should check that the firewalls you are using on the computer and Windows 
allow communication through the port defined for SFTP connection. If not, 
configure the firewall settings to open the desired TCP port.  
SCP Application 
The SCP protocol is typically used to provide secure file transfers between a local host and a remote 
host. For SCP file transfers, an SCP server application must be installed on the computer.  
A variety of third-party SCP applications are available that allow the instant creation of a SCP server on a 
client computer. For more information, refer to the documentation of these applications. 
 
11. Administration 
Note 
SCP file transfers are carried out through TCP port 22. You should check that 
the firewalls you are using on the computer and Windows allow 
communication through this port. If not, configure the firewall settings to 
open TCP port 22. 
Copying Files  
You can use the CLI copy command to copy files within the device, as well as to download/upload files 
to the device via SFTP/SCP. You can also download/upload software pack files via FTP and FTPs. 
 
Note 
The Firewall database cannot be uploaded/downloaded using the CLI 
command. 
 
Note 
The Syslog local accounting-log file can be uploaded; it cannot be 
downloaded.  
In the Web GUI, this is done via the File menu.  
 To copy files via CLI: 
• 
At any prompt, enter: 
copy <source-file-url> <destination-file-url> 
Where: 
• 
<file-url> = <url-prefix> <file> 
• 
<url-prefix> can be empty, or one of the following: 
 tftp://<ipv4-address>/ 
 tftp://[<ipv6-address>]/  
 sftp://<username>:<password>@<ipv4-address>[:<port>]/ 
 sftp://<username>:<password>@[<ipv6-address>][:<port>]/ 
 scp:// user:password@ipv4-address:port/ 
 scp://user:password@[ipv6-address]:port/ 
 ftp://<username>:<password>@<ipv4-address>:<port>/ 
 ftp://<username>:<password>@[<ipv6-address>]:<port>/ 
 ftps://<username>:<password>@<ipv4-address>:<port>/ 
 ftps://<username>:<password>@[<ipv6-address>]:<port>/ 
11. Administration 
 
Notes 
• 
The length of the SFTP server URL and of the filename is limited to 96 
characters. 
• 
It is not necessary to specify <port> when using a well-known port. 
 
• 
<file> can be empty, one of the following files, or the file name on a remote computer if 
applicable. If <file> is on a remote computer, it can contain a path and file name, or just a file 
name. 
 
startup-config 
 
restore-point-config 
 
rollback-config 
 
running-config 
 
user-default-config 
 
factory-default-config 
 
sw-pack-1, sw-pack-2 
 
zero-touch-config-xml 
 
pm-0 
 
db-schema 
 
db-config 
 
schedule-log 
 
user/<filename> 
 
<file> = 
 
      startup-config 
 
      restore-point-config 
 
      rollback-config 
 
      running-config 
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
      zero-touch-config-xml 
 
      banner-text 
 
      pm-0 
11. Administration 
 
      db-schema 
 
      db-config 
 
      ltm_1 
 
      ltm_9 
 
      schedule-log 
 
      accounting-log 
 
      sniffer-file 
 
      user-script 
 
      script-result 
 
      sw-update-1 
 
      sw-update-2 
 
• 
The maximum length/range is: 
 
<username> – 1–60 characters 
 
<password> – 1–60 characters 
 
<file> – 1–96 characters 
 
<port> – 1–65535 
 To copy files via Web GUI: 
1. Navigate to Home>File. 
 
2. Into the “Source file” field, enter the location of the source file: 
11. Administration 
• 
<file-url> = <url-prefix> <file> 
• 
<url-prefix> can be empty, or one of the following: 
 tftp://<ipv4-address>/ 
 tftp://[<ipv6-address>]/  
 sftp://<username>:<password>@<ipv4-address>[:<port>]/ 
 sftp://<username>:<password>@[<ipv6-address>][:<port>]/ 
 scp:// user:password@ipv4-address:port/ 
 scp://user:password@[ipv6-address]:port/ 
 ftp://<username>:<password>@<ipv4-address>:<port>/ 
 ftp://<username>:<password>@[<ipv6-address>]:<port>/ 
 ftps://<username>:<password>@<ipv4-address>:<port>/ 
 ftps://<username>:<password>@[<ipv6-address>]:<port>/ 
In the example below we use SFTP for copying the installation file into sw-pack-2, which we 
will later use for new software installation. 
 
3. Click “Submit”. 
11. Administration 
In the bottom of the screen, we now see both packs: the old one (6.3.0.65) is active and the 
new one (6.3.0.83) is ready for installation. For activation of this new version via 
Web, see Activating the Device Software under Upgrading Software via Web GUI . 
 
Viewing Copy Status 
You can display the status of current and past copy operations, sorted by session start time. 
 To display copy status: 
• 
At the file# prompt, enter: 
show copy [summary] 
Viewing Information on Files  
You can display the following information: 
• 
ETX-1p files  
• 
ETX-1p user files 
• 
Information on the configuration files 
• 
Contents of configuration text files 
• 
Information on the software files (software packs and updates). 
11. Administration 
Viewing ETX-1p Files 
You can display a list of all non-hidden files on the ETX-1p host. The list is sorted by type, and then by 
name.  
 
Note 
• 
If time of creation is unknown, ETX-1p displays the time when it became 
aware of the file’s existence. 
• 
If the file size is unknown, ETX-1p displays the size as ‘--’. 
 To display ETX-1p files: 
• 
At the file# prompt, enter:  
dir 
A list of the file names and types is displayed. 
Viewing User Directory Files 
ETX-1p supports the user-file-dir command to list the user files in its user directory, sorted by name. 
 To display user files: 
• 
At the file# prompt, enter user-file-dir. 
 
Note 
It is optional to enter folder-name, as user is currently the only available 
folder.  
Viewing Configuration Files 
You can display a list of configuration files in the system, and when each was last modified, and if valid. 
 To display information on the configuration files: 
• 
At the file# prompt, enter:  
show configuration-files 
Information on the configuration files is displayed. 
Viewing Configuration Text File Contents 
You can display the contents of each configuration text file stored in the file system. 
11. Administration 
 To display the contents of non-user configuration text files: 
• 
At the file# prompt, enter one of the following: 
 
show factory-default-config 
 
show rollback-config 
 
show startup-config 
 
show user-default-config 
The contents of the specified configuration file are displayed. 
 To display the contents of user text files (i.e. files stored in the /user directory): 
• 
At the file# prompt, enter show user-dir <filename>. 
 
Note 
You can display the contents of a user file that is not binary and contains only 
printable characters.  
 To display the contents of the running-config file: 
• 
From any level (global command), enter show running-config. 
Viewing Software File Details 
ETX-1p supports a command to display details of installed software packs.  
 To display information on the software files: 
• 
At the file# prompt, enter:  
show sw-pack [refresh [<sec>]] 
where sec represents the refresh timeout, with range 3–100. 
Information on the software files is displayed. The State of a SW file can be one of the following: 
active, ready, corrupted, downloading, previous active. 
Deleting Files 
You can delete the following files: 
• 
restore-point-config 
• 
sw-pack-<n> 
11. Administration 
• 
sw-update-<n> 
• 
rollback-config 
• 
startup-config 
• 
user-default-config 
• 
zero-touch-config-xml 
 
Note 
• 
Use caution in deleting files.  
• 
You cannot delete the active software pack 
When software packs are downloaded, ETX-1p extracts software packs into corresponding partitions. If a 
software pack is deleted, ETX-1p erases its corresponding partition. 
Deleting software updates does not affect the active software, even if the update has been already 
installed. 
 To delete a file: 
1. At the file# prompt, enter:  
delete <file-name> 
You are prompted to confirm the deletion. 
2. Confirm the deletion. 
Examples 
Copying Files within the Device 
• 
Source file name – running-config 
• 
Destination file name – startup-config 
copy running-config startup-config 
Downloading via SFTP 
• 
SFTP server address – 192.20.20.20 
• 
SFTP user name – admin 
• 
SFTP password – 1234 
11. Administration 
• 
Source file name – bin/ETX-1p.img 
• 
Destination file name – sw-pack-2 
copy sftp://admin:1234@192.20.20.20/bin/ETX-1p.img sw-pack-2  
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
Viewing ETX-1p Files 
file 
file# dir 
Codes: C-Configuration  S-Software  L-License  LO-Log  O-Other  B-Banner 
 
Name                 Type Size(Bytes) Creation Date Status 
 
db-config              LO   --         2017-06-07   File In Use 
                                       13:00:46 
db-schema              LO   --         2017-06-07   Read Only 
                                       13:00:46 
pm-0                   LO   9858       2078-12-01   File In Use 
                                       12:48:02 
schedule-log           LO   1202       2017-06-07   Read Only 
                                       13:00:46     File In Use 
sw-pack-1              S    22355036   2017-04-12 
                                       15:10:50 
sw-pack-2              S    22398987   2017-05-29   File In Use 
                                       10:42:45 
startup-config         C    964        2017-06-07 
                                       12:58:58 
rollback-config        C    94753      2017-05-29 
                                       16:19:40 
user-default-config    C    784        2017-05-29 
                                       15:01:10 
factory-default-config C    144        2017-06-07   Read Only 
                                       13:00:48 
running-config         C    --         2017-06-12   File In Use 
                                       12:40:39 
restore-point-config   C    784        2017-06-04   Prev In Use 
11. Administration 
                                       17:37:48 
log                    LO   126        2017-10-21   Read Only 
                                       18:11:14 
zero-touch-config-xml  X    31124      2017-10-21 
                                       18:29:28 
 
Total Bytes : 2781732864Free Bytes  : 1150779392 
 
Bytes Available for PM : 4990142 
Viewing User Directory Files 
file 
file# user-file-dir 
Name               Type  Size (bytes)  Creation Date     Status 
-------------------------------------------------------------------- 
my-default-config  U     2500          01.10.2017        read only 
                                       00:00:10 
Total Bytes : 4004028416 Free Bytes  : 1958920192 
Viewing Configuration Files 
file 
file# show configuration-files 
Configuration         Last Modified       Valid 
-----------------------------------------------------------------------------startup-config        
2017-06-07 12:58:58 Yes 
rollback-config       2017-05-29 16:19:40 Yes 
user-default-config   2017-05-29 15:01:10 Yes 
factory-default-config2017-06-07 13:00:48 Yes 
running-config        2017-06-12 12:40:39 Yes 
 
Device loaded from : startup-config 
 
startup-config equals running-config 
Viewing Configuration File Contents 
file# show startup-config 
# configuration file 
exit all 
     
    configure 
#       Management configuration 
        management 
#           SNMP Configuration 
            snmp 
                snmp-engine-id mac 00-00-00-00-00-00 
            exit 
        exit 

## 11.3 Resetting to Default  *(p.666)*

11. Administration 
        router 1 
            name "Router#1" 
            interface 1 
                address 172.17.161.37/24 
                name "eth0" 
                bind ethernet lan4  
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 0.0.0.0/0 address 172.17.161.1 metric 1 
        exit 
    exit 
Viewing Software Pack Information  
show file sw-pack 
Name           Version      Creation Time          Actual 
----------------------------------------------------------------------------- 
sw-pack-1      5.0.0.40     2020-09-06   11:04:57  active 
sw-pack-2      5.0.0.39     2020-09-02   18:52:56  ready 
 
Deleting a File 
file# delete startup-config 
! The file will be erased. Are you sure? [yes/no] _yes 
11.3 Resetting to Default  
ETX-1p supports the following types of reset: 
• 
Reset to factory defaults  
• 
Reset to user defaults 
• 
Overall reset (restart) of the product 
 
Note 
You can request that the active software pack be confirmed after the next 
reboot of ETX-1p. Refer to the description of installing software in the Error! 
Reference source not found. chapter for details.  
11. Administration 
Resetting to Factory Defaults  
ETX-1p can be reset to its factory defaults using either of the following commands:  
• 
factory-default – for customer use 
• 
factory-default-all – not recommended for customer use 
The factory-default and factory-default-all commands have the following differences:  
• 
factory-default always reloads ETX-1p with factory-default-config. factory-default-all reloads 
ETX-1p with user-default-config, if it exists; otherwise, with factory-default-config. 
• 
factory-default copies factory-default-config into startup-config.  
factory-default-all clears the log files and deletes most files, with the exception of 
factory-default-config, user-default-config, software, pm, db-schema, and db-config. It also 
resets file creation times in the file system.  
• 
factory-default-all resets the snmpEngineBoots parameter to 1. This parameter counts the 
number of times the SNMP engine was restarted, and is maintained throughout reboots to 
prevent replay attacks. 
Note 
The Firewall database cannot be reset using the CLI command. 
 
 
Note 
It is not recommended for customers to use the factory-default-all command, 
as it resets the SNMP object (snmpEngineBoots). This can result in the 
management station incorrectly assuming that the original device was 
replaced by another impersonating device, and therefore the management 
station will refuse to communicate with the device. In such cases, the 
manager must manually delete the device from the map and then redraw it. 
To avoid such issues resulting from the resetting of snmpEngineBoots, it is 
recommended to use instead user-default or factory-default and then 
manually delete unneeded files and clear logs, as required 
 
Caution 
Setting ETX-1p to factory defaults deletes all existing virtualization 
entities and instances, regardless of the configured management mode.  
 To reset ETX-1p to factory defaults via CLI: 
1. At the admin# prompt enter: 
factory-default 
11. Administration 
A confirmation message is displayed: 
Current configuration will be erased and device will reboot with 
factory default configuration. Are you sure? [yes/no] 
2. Enter yes to confirm the reset to factory defaults. 
The factory-default-config file is copied to the startup-config file. The unit resets, and after it 
completes its startup the factory defaults are loaded. If a startup-config confirm request was 
active, it is canceled. 
 To reset ETX-1p to factory defaults via Web GUI:  
1. Navigate to Home>Admin.  
The Admin Screen opens.  
 
2. Set “Factory Default” button to “On”.  
17. Click Submit. 
The warning is displayed. 
 
18. Click I Agree. 
11. Administration 
The device resets, and after it completes its startup the factory defaults are loaded. 
 To reset ETX-1p to factory defaults via CLI and delete its entire database: 
1. At the admin# prompt enter factory-default-all. 
A confirmation message is displayed: 
The device will delete its entire database and reboot. Are you sure? 
[yes/no] 
2. Enter yes to confirm the reset to factory defaults with configuration and counter reset. 
The configuration and counter reset explained above is performed, the unit resets, and after it 
completes its startup the factory defaults are loaded. If a startup-config confirm request was 
active, it is canceled. 
 To reset ETX-1p to factory defaults via Web GUI and delete its entire database:  
1. Navigate to Home>Admin.  
The Admin Screen opens.  
 
2. Set “Factory Default All” button to “On”.  
19. Click Submit. 
A warning is displayed. 
11. Administration 
 
20. Click I Agree. 
The device resets, and after it completes its startup the factory defaults are loaded. 
 
Resetting to User Defaults 
You can use the user-default command to reset ETX-1p to the configuration stored in user-default-
config, a file which contains user default parameters that are usually different from RAD’s factory 
default parameters. 
 To reset ETX-1p to user defaults via CLI: 
1. At the admin# prompt enter: user-default 
A confirmation message is displayed: 
Current configuration will be erased and device will reboot with user 
default configuration. Are you sure? [yes/no] 
2. Enter yes to confirm the reset to user defaults. 
The user-default-config file is copied to the startup-config file. The unit resets, and after it 
completes its startup the user defaults are loaded. If a startup-config confirm request was 
active, it is canceled. 
 To reset ETX-1p to user defaults via Web GUI: 
1. Navigate to Home>Admin.  
The Admin Screen opens.  
11. Administration 
 
2. Set “User Default” button to “On”.  
21. Click Submit. 
A warning is displayed. 
 
22. Click I Agree. 
The device resets, and after it completes its startup the user defaults are loaded. 
Restarting ETX-1p 
If necessary, you can restart ETX-1p without interrupting the power supply.  
 To restart ETX-1p: 
1. At the admin# prompt enter reboot 
A confirmation message is displayed: 
Device will reboot. Are you sure? [yes/no] 

## 11.4 Inventory  *(p.672)*

11. Administration 
2. Enter yes to confirm the reset. 
The unit restarts. 
11.4 Inventory 
ETX-1p supports the display of an inventory table of all the third-party device components, hardware 
and software revisions, and power supply types. You can display an inventory table that shows all 
installed components, and you can display more detailed information for each component. The 
inventory display differs for each product according to the different chassis components and port 
configurations.   
 
Applicability and Scaling 
This feature is applicable to all the device versions. 
Standards Compliance 
RFC 4133 – Entity MIB 
Benefits 
You can monitor the installed components and hardware/software revisions. 
Viewing Inventory Information 
 To display the inventory table: 
• 
At the config>system# prompt, enter: 
show summary-inventory 
The inventory table is displayed (see Example for a typical inventory table output). 
11. Administration 
You can display more information for each installed inventory component. To do so, you need to enter 
the inventory level with the corresponding inventory component index, which is displayed in the Index 
column in the output of show summary-inventory.  
 To display the inventory component information: 
1. Navigate to configure system inventory <index>. 
2. Enter: 
show status 
Information for the corresponding inventory component is displayed according to the following 
parameters: 
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
Name 
Name of component 
Possible values (according to component type):  
<device-name> – Chassis 
CPU 
PS-AC/DC <n> 
PS-AC <n> 
PS-DC <n> 
Fan <n> 
Temperature Sensor <n> 
External Clock 
ETH Port [<slot>/]<n> 
MNG Port 
RS-232 Control Port 
Time of Day Port 
11. Administration 
Parameter 
Description 
Mini BNC 
External Clock Port  
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
Alias 
Alias name for component  
Asset ID  
Identification information for component  
FRU 
Indicates whether this component is a field replaceable unit that can be 
replaced on site. 
Processor 
Processor name 
Possible processors: 
Intel Atom Rangeley C2558 
Intel Atom Rangeley C2758 
Cores 
Core size 
Possible values: 
4 – Quad  
8 – Octal 
Core Frequency 
2.4 GHz 
RAM 
RAM volume 
8 GByte 
HD Type 
Hard Drive type 
SSD M2.0 format  
HD Volume 
128 GByte 
11. Administration 
Examples  
 To display inventory summary:  
config>system# show summary-inventory  
Index Physical Class Name                     HW Ver    SW Ver            FW Ver 
----------------------------------------------------------------------------- 
1001  Chassis        ETX-1p                   1.0/a     5.0.0.55_1.0.4           
4001  Sensor         Temperature Sensor 1                                        
4002  Power Supply   PS 1                                                        
7001  Port           RS-232 Control Port                                                 
7002  Port           Ethernet wan1                                               
7003  Port           Ethernet wan2                                               
7004  Port           Ethernet lan1                                               
7005  Port           Ethernet lan2                                               
7006  Port           Ethernet lan3                                               
7007  Port           Ethernet lan4                                               
7008  Port           Cellular lte                                                
8001  CPU            CPU                 
 
 
 To display inventory information for power supply (index 4002):  
config system 
config>system# inventory 4002 
config>system>inventory(4002)# show status 
Description       : Power Supply 
Contained In      : 1001 
Physical Class    : Power Supply 
Relative Position : 2 
Name              : PS 1 
HW Ver            : 
SW Ver            : 
FW Ver            : 
Serial Number     : 
MFG Name          : RAD 
Model Name        : 
Alias             : 
Asset ID          : 
FRU               : False 
 
config>system>inventory(4002)# 
 To display inventory information for chassis (index 1001): 
 
 
 
 

## 11.5 Login Banner  *(p.676)*

11. Administration 
config>system>inventory(1001)# show status 
Description       : Chassis 
Contained In      : 0 
Physical Class    : Chassis 
Relative Position : 1 
Name              : ETX-1p 
HW Ver            : 1.0/a 
SW Ver            : 5.0.1.138 
FW Ver            : 
Serial Number     : 00-55-66-77-01-B2 
MFG Name          : RAD 
Model Name        : ETX-1P_ACEX/1SFP1UTP/4UTP/L1/WF 
Alias             : 
Asset ID          : 
FRU               : True 
 
11.5 Login Banner 
You can define a banner to be displayed before the login prompt for user name (using the CLI command 
login-message), as well as a banner to be displayed following successful login (using the CLI command 
announcement). 
 
Note 
If you are accessing ETX-1p via SSH, the banner is printed between the user 
name prompt and the password prompt. 
Applicability and Scaling 
This feature is applicable to all the device versions. 
Functional Description 
Pre-login and post-login banner messages must satisfy the following: 
• 
Message must be enclosed in single quotation marks. 
• 
Pressing <Enter> before entering a closing quotation mark, results in the warning message: 
Enter message.  End with the single quotation character (‘). 
11. Administration 
• 
A message that spans multiple lines is interpreted as if it were written in one line; <cr> and <lf> 
between lines in the configuration file or command are ignored.  
• 
A message can contain printable characters, as well as the following special characters (only 
relevant for CLI; from SNMP, these characters should be entered normally): 
 
\n – new line 
 
\t – horizontal tab 
 
\’ – single quotation mark 
 
\\ – backslash 
• 
Usage of special characters reduces the maximum number of printable characters that the 
banner can contain. For example, if the banner contains \n, up to 1998 additional printable 
characters can be used. 
• 
The banner can be up to 2000 characters (including the escape / characters). An attempt to 
configure a longer banner results in the CLI error: Banner may not exceed 2000 characters. 
Configuring Login Banners 
 To configure a pre-login banner: 
1. Navigate to configure system. 
The config>system# prompt is displayed. 
2. Type login-message <message>, enclosing the message in quotes. 
At the next login, this pre-login banner is displayed. 
 
Note 
Type no login-message to remove a previously configured pre-login banner.  
 To configure a post-login banner: 
1. Navigate to configure system. 
The config>system# prompt is displayed. 
2. Type announcement <message>, enclosing the message in quotes. 
After the next login, this post-login banner is displayed. 
 
Note 
Type no announcement to remove a previously configured post-login banner.  
You can display the banners configured for ETX-1p by navigating to the product level and entering info.  
11. Administration 
Example 
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
 