# 10 Administration

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 802–822.*


## 10.1 CPU and Memory Utilization  *(p.802)*

This chapter covers administrative tasks such as entering contact info, file management, viewing CPU 
and memory utilization, etc. In addition, this section instructs you on resetting the unit. 
10.1 CPU and Memory Utilization  
You can view CPU and memory pool usage. 
Viewing CPU Utilization 
 To display CPU usage: 
• 
From the system context (config>system), enter: 
show cpu-utilization 
The CPU usage is displayed for each CL module.  
config>system# show cpu-utilization 
CPU Utilization 
----------------------------------------------------------------- 
Slot      Min       Cur       Max       Average 
          (%)       (%)       (%)       (%) 
----------------------------------------------------------------- 
cl-a      0         14        100       13 
cl-b      0         15        99        15 
Viewing Memory Pool Utilization   
 To display memory pool usage: 
4. From the system context (config>system), enter show memory. 

## 10.2 Device Information  *(p.803)*

10. Administration 
The memory pool usage is displayed for each CL module, showing the total amount allocated to 
the pool, as well as the amount that is free.  
config>system# show memory 
                       Kernel      Kernel 
                     Total (KB)  Free (KB) 
----------------------------------------------------------------- 
Memory CL-A            130969      59829 
Memory CL-B            130969      64071 
10.2 Device Information 
The Megaplex-4 management software allows you to assign a name to the unit, add its description, 
specify its location to distinguish it from the other devices installed in your system, and assign a contact 
person. 
 To configure device information:  
5. Navigate to configure system. 
The config>system# prompt is displayed. 
6. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning device name 
name <device-name> 
The length of the device name is unlimited, but if 
you enter a name containing more than 
20 characters, the prompt displays only the first 
20 characters followed by 0.  
For example, this command that defines a 
25-character device name:  
# config sys name Megaplex _NYC _Building_1 
results in this prompt that shows the first 
20 characters, followed by 0: 
Megaplex_NYC_Build0# 
no name removes user-assigned device name 
Specifying location 
location 
<device-location> 
no location removes user-assigned location 
Specifying contact person 
contact 
<contact-person> 
no contact removes user-assigned contact 
information 

## 10.3 MAC Address Allocation  *(p.804)*

10. Administration 
Task 
Command 
Comments 
Displaying device 
information, MAC address, 
and amount of time the 
device has been running 
show device-information 
 
 
Note 
For configuring the system clock and date&time, refer to Chapter 9. 
 To display device information: 
• 
At the config>system# prompt, enter show device-information. 
For example: 
# configure system 
config>system# name  
config>system# location floor-8 
config>system# contact Engineer-1 
 
config>system# show device-information 
Description    : MP-4100,  HW: 0,  SW: 4.0 
Name           :  
Location       : floor-8 
Contact        : Engineer-1 
MAC Address    : 00-20-D2-51-62-5A    
System Up Time : 000 Days 00:22:06         
10.3 MAC Address Allocation 
Each Megaplex-4 CL module has 18 unique MAC addresses to be assigned to its ports. Each of the 
following ports is assigned a different MAC address: 
• 
Two CL GbE ports (the 1st MAC address is assigned to GBE port 1, the 2nd MAC address – to GBE 
port 2) 
• 
16 Logical MAC ports bound to first 16 VCG ports (in the order of their creation): MAC addresses 
3-18 are assigned to VCGs 1-16. 
Logical MACs bound to VCGs 17-32 inherit their MAC address from the CL on which they are defined.  

## 10.4 Managing the Licenses  *(p.805)*

10. Administration 
The MAC clients in the device (e.g. router interfaces, MEPs, etc., inherit their MAC addresses from the 
relevant port). 
You can view the MAC address assigned to an Ethernet or Logical MAC port via show status command 
(see corresponding section in Chapter 6). For information on which MAC address is used by a particular 
feature, refer to the relevant section in this manual.   
You can display the number of MAC addresses and the first MAC address defined on a specific chassis 
slot as follows.  
 To display MAC addresses defined on the slot: 
• 
At the config>chassis# prompt, enter show manufacture-info slot <slot_number> to display 
information on items installed in a specific slot. 
• 
For example: 
M-ETH module: 
 
config>chassis# show manufacture-info slot 7 
First MAC Address : 00-01-C1-00-00-07     
Number of MACs    : 1 
 
CL module: 
 
config>chassis# show manufacture-info slot cl-a 
First MAC Address : 00-20-D2-F3-BC-D3   
Number of MACs    : 18 
10.4 Managing the Licenses  
By default, the CL.2 modules are supplied with STM-1/OC-3 ports and GbE ports with 10/100 Mbps rate. 
To enable the STM-4/OC-12 and/or 1000 Mbps rate functionality, the following software license keys 
are required:  
• 
STM-4/OC-12: MP-4100-LIC/622SK for Megaplex-4100 and MP-4104-LIC/622SK for Megaplex-
4104.  
• 
1000 Mbps: MP-GBE-LIC 
You can order the license keys together with the product or later, when the upgrade is needed. The 
license is based on the module MAC address and must be ordered separately for each CL.2 module. 
10. Administration 
You can download two license files, one for a feature, or a single file holding both features. 
Checking the License Availability 
There are two ways to display whether your device features any of the licensed functionalities.  
 To display the license availability – method 1: 
1. Navigate to show configure system license. 
An example of display is shown below: 
# show configure system license 
Feature                      Status  Slot    File Name 
--------------------------------------------------------------- 
STM-4/OC-12                  Enable  CL-A    license-1 
Ethernet Port Speed 1000Mbps Enable  CL-A    license-1 
STM-4/OC-12                  Disable CL-B    N/A 
Ethernet Port Speed 1000Mbps Disable CL-B    N/A 
# 
This display means that both STM-4/OC-12 and 1000 Mbps functionalities are installed in CL-A 
module. Both licenses are contained in license-1 file. 
No licenses have been installed in the CL-B module. 
 To display the license availability – method 2: 
1. Navigate to admin license show summary. 
An example of display is shown below: 
#admin>license# show summary 
Feature Name              Status                   In Use 
------------------------------------------------------------------------- 
OC12STM4-CLA              Enabled                   Yes 
OC12STM4-CLB              Disabled                  No 
GbE-CLA                   Enabled                   Yes 
GbE-CLB                   Disabled                  No 
This display means that both STM-4/OC-12 and 1000 Mbps functionalities are installed in CL-A module 
(Status=Enabled). No licenses have been installed in the CL-B module. 
The right column (“In use”) indicates if there is a configuration using the feature. In this configuration: 
• 
The SDH/SONET port is configured for the rate of 622Mbps and it is in use. 
• 
There is a flow using the Ethernet cl-a/1 or cl-a/2 at the rate of 1000 Mbps.  
10. Administration 
Ordering the license is described in the following section. 
Ordering the License  
In order to activate the STM-4/OC-12 and/or 1000 Mbps functionality, the license file must be 
downloaded and activated. Once purchased, the license is permanent and does not expire. 
The licenses are based on the CL.2 module MAC address and distributed as software files named *.txt, 
for example LIC_0020D2500C48.txt. The files can be obtained from the local RAD Partner from whom 
the device was purchased. Each license is ordered per CL module.  
 To display the MAC Address of CL-A/CL-B: 
• 
Use configure>chassis>show manufacture-info command as illustrated in the following 
example.  
# configure 
config# chassis 
config>chassis# 
config>chassis# show manufacture-info slot cl-a 
First MAC Address : 00-20-D2-50-0E-93 
Number of MACs    : 1 
 
config>chassis# 
config>chassis# show manufacture-info slot cl-b 
First MAC Address : 00-20-D2-50-05-B0 
Number of MACs    : 1 
You can also use the following syntax:  
# show configure chassis manufacture-info slot cl-a 
First MAC Address : 00-20-D2-50-0C-48 
Number of MACs    : 1 
 
# 
# show configure chassis manufacture-info slot cl-b 
First MAC Address : 00-20-D2-50-05-B0 
Number of MACs    : 1 
The “Number of MACs” field value in the case of Megaplex-4 is always “1”. 
The software upgrade utility includes four partitions called license-1, license -2, license -3, license -4 for 
downloading and storing the licenses.  
You can download the license file to Megaplex-4 via CLI using TFTP.  
10. Administration 
Downloading the License File Using TFTP 
 To download the license file using TFTP: 
1. Assign the IP address to the Megaplex-4 device as described in Configuring the Router Interface 
section (Chapter 8). 
2. Download the valid license obtained from RAD using file>copy command as follows. 
3. For example: 
 
Host IP (PC) address is 172.17.170.38. 
 
License file for CL-A is LIC_0020D2500C48.txt 
 
License file for CL-B is LIC_0020D25005B0.txt. 
# file copy tftp://172.17.170.38/LIC_0020D2500C48.txt license-1  
 Are you sure? [yes/no] _ y 
# 
File copy command was completed. 
tftp://172.17.170.38/LIC_0020D2500C48.txt copied to license-1 successfully 
139 bytes copied in 2 secs (69 bytes/sec) 
 
# 
# file copy tftp://172.17.170.38/LIC_0020D25005B0.txt license-2 
 Are you sure? [yes/no] _ y 
# 
File copy command was completed. 
tftp://172.17.170.38/LIC_0020D25005B0.txt copied to license-2 successfully 
139 bytes copied in 1 secs (139 bytes/sec) 
4. Type “commit”. 
Now the license file is downloaded to the device.  
You can see the installed license via the command file>dir: 
#file>dir  
Name                 Type Size(Bytes) Creation Date Status 
10. Administration 
 
db-config                   --         2-6-2019     File In Use 
                                       11:31:43 
db-schema                   --         2-6-2019     Read Only 
                                       11:31:43 
pm-0                        18         2-6-2019     File In Use 
                                       11:31:43 
sw-pack-1              S    4733442    25-5-2019    valid 
                                       16:25:30 
sw-pack-2              S    26615026   21-4-2019    File In Use 
                                       08:45:29 
startup-config         C    30017      27-5-2019    valid 
                                       16:26:32 
factory-default-config C    5217       2-6-2019     valid 
                                       11:31:22 
running-config         C    --         2-6-2019     File In Use 
                                       11:32:28 
license-1              L    139        2-6-2019     valid 
                                       13:32:06 
log                    LO   880000     19-10-2017   Read Only 
                                       08:48:31 
Installing the License for Redundant CL Modules 
If two redundant modules (CL-A and CL-B) are installed in the chassis, the license must be installed in 
both CL modules.   
 To ensure this, proceed as follows: 
1. Install both CL modules in the chassis. 
2. Download the license file to CL-A (for example, to “license-1”). 

## 10.5 Inventory  *(p.810)*

10. Administration 
3. Reset the CL-A module. 
Now the CL-B module becomes active (working) and you can download the license to it. 
4. Download the license file to CL-B (for example, to “license-1”). 
5. Reset the CL-B module. 
Now the modules can operate at STM-4/OC-12 rates as a redundant pair. 
10.5 Inventory  
The Megaplex-4 inventory table displays the unit’s components, hardware, software and firmware 
revisions. You can display an inventory table that shows all installed components, and you can display 
more detailed information for each component. 
Standards and MIBs 
The inventory feature is implemented according to RFC 4133 – Entity MIB (RFC 2737 was made obsolete 
by RFC 4133 version 3). 
Benefits 
You can monitor the installed components and hardware/software revisions. 
Displaying Inventory Information 
The Megaplex-4 inventory table displays the unit’s components, hardware, software and firmware 
revisions. 
 To display the inventory table: 
• 
In the config>chassis# prompt, enter show summary-inventory. 
The inventory table is displayed (refer to Example to see a typical inventory table output). 
10. Administration 
Displaying Inventory Component Information 
You can display more information for each installed inventory component. To do this, enter the 
inventory level with the corresponding inventory component index. The component index is determined 
by the position of the corresponding row in the output of show inventory-summary, which changes 
according to what is installed in the unit.  
 To display the inventory component information: 
1. Navigate to configure chassis inventory <index>. 
2. Enter show status. 
Information for the corresponding inventory component is displayed. 
Inventory Parameters 
Parameter 
Description 
Description 
Description of component type 
Contained In 
Index of the component that contains the component for which information is 
being displayed.  
Physical Class 
Class of component. Possible values: Stack, Chassis, Container, Module, Port 
Relative Position 
Contains the relative position of this component  in relation to other 
component with the same “Contained In” value 
Name 
Name of component 
HW Rev 
Hardware revision  
SW Rev 
Software revision  
FW Rev 
Firmware revision  
Serial No. 
Serial number (read-write field, can be edited by the user; it is recommended 
to type here the number on the sticker that is attached to the component 
when it leaves RAD) 
MFG Name 
Manufacturer name (blank if unknown for component) 
Module Name 
The component information: type, slot, port etc  
Alias 
Alias name for component (read-write field, can be edited by the user)  
Asset ID  
Identification information for component (read-write field, can be edited by 
the user; it is recommended to type here the HW configuration letter CSL) 
FRU 
Indicates whether this component is a field replaceable unit that can be 
replaced on site (True/False) 
10. Administration 
Setting Administrative Inventory Information 
If necessary, you can configure the alias, asset ID, and serial number for inventory components of I/O 
modules. To configure the information, you need to enter the inventory level with the corresponding 
inventory component index as determined by the position of the corresponding row in the output of 
show summary-inventory.  
 To set inventory component information: 
1. Navigate to configure chassis inventory <index>. 
The config>chassis>inventory(<index>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning user-defined alias to 
component  
alias <string> 
no alias removes the alias. 
Configuring the alias is 
meaningful only for the chassis 
component. It can be used by a 
network manager as a 
non-volatile identifier for the 
device. 
Assigning user-specific asset identifier 
to the component (usually for 
removable physical components) 
asset-id <id> 
no asset-id removes the asset ID 
Assigning vendor-specific serial number 
to the component 
serial-number <string> 
no serial-number removes the 
serial number 
Example 
 To display the following inventory information: 
• 
Inventory table 
• 
Inventory information for T1 port 1 of M8T1 module installed in I/O slot 1. 
# configure chassis 
config>chassis# show summary-inventory 
Index Physical Class Name                     HW Ver    SW Ver            FW Ver 
----------------------------------------------------------------------------- 
1     Stack          stack 
2     Chassis        chassis 
101   Power Supply   PS-A 
10. Administration 
103   Module         CL A                     0.0       4.10.07 
105   Module         IO Card-1 
201   Container      PS-A 
202   Container      PS-B 
203   Container      slot a 
204   Container      slot b 
205   Container      slot 1 
206   Container      slot 2 
207   Container      slot 3 
208   Container      slot 4 
3001  Port           RS-232 Control Port CL-A 
3002  Port           MNG Ethernet CL-A/1 
3003  Port           Station Clock CL-A 
5001  Port           T1 IO-1/1 
5002  Port           T1 IO-1/2 
5003  Port           T1 IO-1/3 
5004  Port           T1 IO-1/4 
5005  Port           T1 IO-1/5 
5006  Port           T1 IO-1/6 
5007  Port           T1 IO-1/7 
5008  Port           T1 IO-1/8 
5009  Port           Ethernet IO-1/1 
5010  Port           Ethernet IO-1/2 
5011  Port           Ethernet IO-1/3 
103004Container      slot a port 1 
103005Container      slot a port 2 
103006Container      slot a port 1 
103007Container      slot a port 2 
 
config>chassis# 
config>chassis# inventory 5001 
config>chassis>inventory(5001)# show status 
Description       : MP-4100.T1 IO-1/1 
Contained In      : 105 
Physical Class    : Port 
Relative Position : 1 
Name              : T1 IO-1/1 
HW Ver            : 
SW Ver            : 
FW Ver            : 
Serial Number     : 
MFG Name          : RAD 
Module Name       : T1 IO-1/1 
Alias             : IO-1 t1 01 
Asset ID          : 
FRU               : False 
config>chassis>inventory(5001)# 

## 10.6 File Operations  *(p.814)*

10. Administration 
10.6 File Operations 
You can perform the following operations: 
• 
Copy files within the Megaplex-4 unit 
• 
Display files within the Megaplex-4 unit 
• 
Delete files. 
File Names in the Unit 
Megaplex-4 uses the following reserved file names: 
• 
factory-default – Contains the factory default settings 
• 
running-config – Contains the current user configuration that is different from the default 
configuration. 
• 
startup-config – Contains saved user configuration. You must save the file startup-config; it is 
not automatically created. Refer to Saving the Configuration for details on how to save the user 
configuration.  
• 
user-default-config – Contains default user configuration. Refer to Saving the Configuration for 
details on how to save the default user configuration. 
• 
candidate – Stores any configuration before it is copied to running-config via commit command.   
• 
sw-pack-1, sw-pack-2, sw-pack-3, sw-pack-4 – Contains up to four software images 
• 
log –Contains alarm and event log (5000 alarms/events)  
• 
mac-table – Contains the MAC address table (see Displaying MAC Address Table in Chapter 8 for 
description) 
You can copy files via the copy command, or via the following commands. 
Commands That Copy Files  
Command 
Level 
Copies… 
Manual Section 
factory-default 
admin 
factory-default to candidate   
(then use commit to copy factory-default 
to running-config and then save to copy it 
to startup-config)  
Resetting to Factory 
Defaults 
 
10. Administration 
Command 
Level 
Copies… 
Manual Section 
user-default-config  
admin 
user-default-config to candidate   
(then use commit to copy 
user-default-config to running-config and 
then save to copy it to startup-config) 
Resetting to User 
Defaults 
save  
global 
running-config to startup-config 
Saving the Configuration 
Copying Files within Megaplex-4 
You can copy files within the Megaplex-4 unit with the copy command. The figure below shows 
commands that can copy configuration files in a visual diagram.  
 
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
 To copy files within the device: 
• 
At the file# prompt, enter: 
copy <source-file> <dest-file>. 
Example 1: 
• 
Source file name – running-config  
10. Administration 
• 
Destination file name – startup-config. 
# file 
file# copy running-config startup-config 
Example 2: 
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
Due to a large file volume, copying starts after 30 sec of processing. 
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
Direction      Source            Destination       End Time        Status 
1   Local      running-config    user-default-conf 13-3-2011    Ended OK 
                                                   14:6:51 
10. Administration 
2   Local      running-config    startup-config    13-3-2011    Ended OK 
                                                   14:7:35 
3   Dev to Net startup-config    DB                13-3-2011    Ended OK 
                                                   14:7:40               
Displaying Files within Megaplex-4 
The dir command is used to display the files within the device. 
 To display the files: 
• 
At the file# prompt, enter dir. 
A list of the file names and types is displayed. 
For example:  
HyQ_C>file# dir 
Codes: C-Configuration  S-Software  L-License  LO-Log  O-Other 
 
Name                 Type Size(Bytes) Creation Date Status 
 
sw-pack-1              S    13439930   20-5-2014    valid 
                                       11:45:49 
sw-pack-2              S    14052947   5-6-2014     valid 
                                       14:30:30 
sw-pack-3              S    14025662   2-4-2014     valid 
                                       14:3:34 
sw-pack-4              S    14056358   16-6-2014    File In Use 
                                       11:47:29 
startup-config         C    37268      21-5-2014    valid 
                                       11:37:1 
user-default-config    C    11983      2-3-2014     valid 
                                       10:18:24 
factory-default-config C    680        1-1-1970     Read Only 
                                       0:0:9 
running-config         C    --         18-6-2014    Read Only 
                                       15:44:25 
log                    LO   --         18-6-2014    Read Only 
                                       15:44:25 
Total Bytes : 101367808 Free Bytes  : 31295488 
10. Administration 
Deleting Files 
You can delete files. Before deleting the file, make sure the file is not in use. For additional information 
on configuration files and the consequences of deleting, refer to Configuration Files and Loading 
Sequence in Chapter 3.  
 To delete a file: 
1. At the file# prompt, enter: delete <file-name>. 
You are prompted to confirm the deletion. 
For example:  
# file 
file# delete sw-pack-1 
File will be erased. Are you sure?? [yes/no] _yes 
2. Confirm the deletion. 
The unit reverts to the factory default. 
Saving the Configuration  
You must save your configuration if you wish to have it available, as it is not saved automatically. You 
can save your configuration as outlined below. Additional information on config files is available under 
Configuration Files in Chapter 3. 
 To save your current configuration in the startup-config file: 
• 
At any level, enter save. 
• 
At the file# prompt enter:  
copy running-config  startup-config. 
Downloading/Uploading Files  
You can download or upload files to the Megaplex-4 unit via SFTP. The following types of files can be 
uploaded or downloaded: 
• 
startup-config 
• 
user-default-config 
10. Administration 
• 
factory-default-config (upload only) 
• 
log (upload only) 
• 
sw-pack-1, -2, -3, -4 
The maximum allowed values for SFTP parameters are: 
• 
Username – 1 – 60 characters 
• 
Password –1– 60 characters 
• 
File name – 1–100 characters 
• 
Port – 1–65535. 
Caution 
Always wait until all main cards installed in the chassis are up and running 
before executing any file operation commands. 
The SFTP protocol is used to provide secure file transfers via the device’s Ethernet interface. SFTP is a 
version of FTP that encrypts commands and data transfers, keeping your data secure and your session 
private. For SFTP file transfers, an SFTP server application must be installed on the local or remote 
computer. SFTP file transfers use Port 22. You must check that the firewall you are using on the server 
computer allows communication through this port. 
A variety of third-party applications offer SFTP server software. For more information, refer to the 
documentation of these applications. 
Ethernet
PC with an Active 
SFTP Server and 
Application File
Application file is 
transferred to MP
MP-4100/4104
 
Example – Download via SFTP 
• 
SFTP server address – 192.20.20.20 
• 
SFTP user name – admin 
• 
SFTP password – 1234 
• 
Source file name – .bin 
• 
Destination file name – sw-pack-1. 
# file 
file# copy sftp://admin:1234@192.20.20.20/.bin sw-pack-1 

## 10.7 Resetting Megaplex-4  *(p.820)*

10. Administration 
 
Note 
Destination file name can be only sw-pack-1, sw-pack-2, sw-pack-3 or sw-
pack-4. 
Example – Upload via SFTP 
• 
SFTP server address – 192.20.20.20 
• 
SFTP user name – admin 
• 
SFTP password – 1234 
• 
Source file name – startup-config 
• 
Destination file name –db1conf.cfg 
# file 
file# copy startup-config sftp://admin:1234@192.20.20.20/db1conf.cfg 
 
Note 
The source file name can be one of the following: startup-config or user-
default-config. 
10.7 Resetting Megaplex-4  
Megaplex-4 supports the following types of reset: 
• 
Reset to factory defaults 
• 
Reset to user defaults 
• 
Overall reset (restart, reboot) of the device.  
Resetting to Factory Defaults 
 To reset Megaplex-4 to factory defaults:  
1. At the device prompt, enter admin. 
The admin> prompt appears. 
2. Enter factory-default. 
10. Administration 
A confirmation message is displayed: 
Current configuration will be erased with factory default configuration. Are you sure?? [yes/no] 
3. Enter yes to confirm resetting to factory defaults. 
The factory-default file is copied to the candidate file.  
4. Enter commit to complete the operation. 
The factory-default file via Candidate DB is copied to the running-config file. Now at the device 
startup, the factory defaults are loaded. 
Resetting to User Defaults 
 To reset Megaplex-4 to user defaults: 
1. At the device prompt, enter admin. 
The admin> prompt appears. 
2. Enter user-default. 
A confirmation message is displayed: 
Current configuration will be erased with user default configuration. Are you sure?? [yes/no] 
3. Enter yes to confirm resetting to user defaults. 
The user-default-config file is copied to the candidate file.  
4. Enter commit to complete the operation. 
The user-default config file via Candidate DB is copied to the running-config file. Now at the 
device startup, the user defaults are loaded. 
Rebooting the Megaplex-4 Chassis 
 To reboot the chassis: 
1. At the admin# prompt, enter the reboot command.  
A confirmation message is displayed: 
Chassis will reboot. Are you sure?? [yes/no] 
2. Enter yes to confirm the reset. 
The chassis restarts.  
10. Administration 
Note 
If at this moment the CL modules are in synchronization state, the reboot 
request is denied and the following message is displayed:  "Unprotected data, 
main cards in sync process, please wait... " In this case try rebooting the 
chassis later. 
Rebooting the Module 
Use the following procedure to reboot a module installed in a specified slot. 
Note 
Resetting a module will temporarily disrupt services supported by that 
module. 
 To reboot a module: 
1. Navigate to configure slot <slot>. 
The config>slot<slot># prompt is displayed. 
2. Enter reset. 
A confirmation message is displayed: 
Card will reset. Are you sure?? [yes/no] 
3. Enter yes to confirm the reset. 
The module restarts.  
Note 
When trying to reboot CL modules in synchronization state, the reboot request 
is denied and the following message is displayed:  "Unprotected data, main 
cards in sync process, please wait... " In this case try rebooting the CL module 
later. 
 