# Feature Reference – 7 Administration

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1219–1274.*


## 7.1 CPU and Memory Utilization  *(p.1219)*

7 Administration 
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
Licensing 
• 
Login Banner 
• 
Sending a Message to Connected Users 
• 
Reset  
• 
Tech-Support Commands 
7.1 CPU and Memory Utilization 
You can view CPU and memory pool usage. 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. 
ETX-2i Devices 
7. Administration 
Viewing Utilization Data 
Viewing CPU Utilization 
 To display CPU usage: 
• 
From the system context (config>system), enter: 
show cpu-utilization 
The CPU usage is displayed.  
ETX‑2i>config>system# show cpu-utilization 
CPU Utilization 
----------------------------------------------------------------------------- 
Min (%) : 0         Cur (%)  : 5         Max (%)  : 99       Average (%)  : 5  
Viewing Memory Pool Utilization 
 To display memory pool usage: 
1. From the system context (config>system), enter the following to display memory pool usage: 
show memory 
The memory pool usage is displayed, showing the total amount allocated to the pool, as well as 
the amount that is free.  
ETX‑2i>config>system# show memory 
                     Kernel        Kernel 
                     Total (KB)    Free (KB) 
--------------------------------------------------------------- 
Memory               3166141899    1051027919 
 
2. From the system context (config>system), enter the following to display details of memory pool 
usage: 
show memory–details 
ETX‑2i>config>system# show memory-details 
Slot              : Memory 
Kernel Total(KB)    : 368474              Free        : 262408 

## 7.2 Device Information  *(p.1221)*

ETX-2i Devices 
7. Administration 
7.2 Device Information 
The ETX‑2i management software allows you to assign a different name to the unit, specify its location 
to distinguish it from the other devices installed in your system, and assign a contact person.  
It also enables you to view device information (show device-information command below), including 
description (default RAD-assigned device name, unconfigurable), HW version, SW version, name 
(configurable system device name, appears in the command prompt), location, contact, MAC address, 
engine time, manufacturer serial number, connectors side, and CLEI code. 
 
Note 
You cannot change the description of the unit (the default device name), the 
manufacturer serial number (programmed on the device’s board), or the CLEI 
code. 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. 
Device information display of manufacturer serial number and CLEI code was introduced in version 6.8.2 
(0.35). 
Functional Description 
Device Name, System Name 
The device name (description, unconfigurable) is set by RAD to identify the unit’s ordering option.   
The system name is displayed in the CLI prompt before the pound sign (#). By default, this is the same as 
the device name, unless configured by the user to another meaningful name.  
The output of the show device-information command shows both the device name (in the Description 
field) and the system name (in the Name field). 
 
 
ETX-2i Devices 
7. Administration 
The following table shows the RAD-assigned device names for the available ETX‑2i devices. 
Ordering Option Key Features  
Device Name 
ETX-2i 
ETX-2i 
ETX-2i      
ETX-2i/64E1 
ETX-2i-64E1 
ETX-2i/M/NFV  
ETX-2i-x86 
ETX-2i-B 
ETX-2i-B 
ETX-2i-B 
ETX-2i-B/NFV 
ETX-2i-B-x86 
ETX-2i-B/PTP 
ETX-2i-B-PTP 
ETX-2i-B/10SFP 
ETX-2i-B-10x1G 
ETX-2i-10G 
ETX-2i-10G/4SFPP/12SFP/12UTP or SFP 
ETX-2i-10G-24X1G 
ETX-2i-10G-B 
ETX-2i-10G-B 
ETX-2i-10G-B/8SFPP 
ETX-2i-10G-B-8SFPP 
ETX-2i-10G-B/8SFPP/H 
ETX-2i-10G-B-8SFPP/H 
ETX-2i-10G-B/8SFPP/PTP (No GNSS) 
ETX-2i-10G-B-8SFPP-P 
ETX-2i-10G-B/8SFPP/GNSS 
ETX-2i-10G-B-8SFPP-G 
ETX-2i-10G-B/8SFPP Outdoor 
ETX-2i-10G-B-8SFPP-O 
ETX-2i-10G-B/8SFPP/GNSS Outdoor 
ETX-2i-10G-B-8SFPP-GNSS-ODU 
ETX-2i-10G-E/8SFPP 
ETX-2i-10G-E-8SFPP 
ETX-2i-100G 
ETX-2i-100G/4QSFP 
ETX-2i-100G-4QSFP 
ETX-2i-100G/40G 
ETX-2i-100G-40G 
 
 
ETX-2i Devices 
7. Administration 
Manufacturer Serial Number 
During device production, a unique manufacturer serial number consisting of ASCII printable characters, 
is programmed on the device board.  
ETX‑2i supports reading the manufacturer serial number from the device and presenting its first 16 
characters. 
 
Note 
The manufacturer serial number is different than the available read/write 
inventory serial number (in system>inventory serial-number), which 
customers can configure. 
Device CLEI Code 
Some ETX‑2i devices support a 10-character alphanumeric CLEI code that represents the device ordering 
option.  
In supported devices, the show device-information report displays the CLEI code. In unsupported 
devices (i.e., the CLEI code is 10 characters of ‘0’), the report displays ‘not available’.  
Standards Compliance 
The commands below are based on RFC 3841. 
Configuring Device Information 
 To configure device information: 
1. Navigate to configure system. 
The config>system# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying contact 
person 
contact <contact-person> 
no contact 
Entering no contact removes the contact person. 
Contact-person – contact name 
Possible values: 0-255 characters 
Default: “Name of contact person” 
ETX-2i Devices 
7. Administration 
Task 
Command 
Comments 
Assigning system 
name 
name <system-name> 
no name 
The system name can be 0-255 characters; however, 
the CLI prompt displays only up to 42 characters, 
therefore if you enter a name with more 
than 42 characters, the prompt displays the 
first 41 characters followed by *. 
For example, a command that defines a system device 
name longer than 42 characters: 
ETX-2# config sys name 
123456789012345678901234567890123456789ETX-2 
results in the prompt: 
123456789012345678901234567890123456789ET*# 
You can view the complete system name by 
entering show device-information. 
Entering no name removes the name entirely. 
Default: <system name> (see Name below) 
Note: The system name can consist of up to 42 
characters. 
Specifying location 
location <device-location> 
no location 
Default: “The location of this device” 
Displaying device 
information  
show device-information 
Device information includes the following: 
• Description – default device name; unconfigurable 
 
• Hw – the hardware version number; unconfigurable  
• Sw – the software version number followed by SR if 
the device uses a Static Router license  
• Name – user-configurable system device name (by 
default, the device name in Description above) 
• Location – location of device 
• Contact – name of contact person 
• MAC address 
• Engine Time – the amount of time the device has 
been running 
• Manufacturer Serial Number – 10-character 
numeric manufacturer serial number that has been 
programmed on the device’s board 
If there is no serial number, displays Not available. 
• Connectors Side – the location of the connectors 
(Front or Rear).  
ETX-2i Devices 
7. Administration 
Task 
Command 
Comments 
• CLEI Code – 10-character alphanumeric CLEI code 
that represents the device ordering option. 
If the device reads a CLEI string of all zeroes, 
displays Not available. 
If the device reads a non-alphanumeric CLEI string, 
displays Error. 
Examples 
 To configure device information for ETX-2i/64E1: 
• 
Device name – ETX-2i-64E1 
• 
Location – floor-8 
• 
Contact – Engineer-1 
exit all 
configure system 
  name ETX-2i-64E1 
  location floor-8 
  contact Engineer-1 
  exit all 
 To display device information for ETX-2i-10G: 
ETX-2i-10G>config>system# show device-information 
 
Description :ETX-2I-10G-B Hw: 0.2/A, Sw: 6.8.2(3.73)            
Name        :2i10G_1                                   
Location    : floor-8                                        
Contact     : Engineer-1                                     
MAC Address : 00-20-D2-30-CC-9D                              
Engine Time : 05:13:31 
Manufacturer Serial Number : Not available 
 
 

## 7.3 Environment  *(p.1226)*

ETX-2i Devices 
7. Administration 
 To display the default device information for ETX-2i-100G: 
ETX-2I-100G>config>system# show device-information 
Description    : ETX-2I-100G Hw: 0.0/B, Sw: 6.7.0(0.10) 
Name           : ETX-2I-100G 
Location       : The location of this device 
Contact        : Name of contact person 
MAC Address    : 00-20-D2-5A-1D-99 
Engine Time    : 00:24:49 
 
Manufacturer Serial Number : 201812345678 
 To display the default device information for ETX-2i-10G: 
ETX-2I-10G# show con sys device-information 
Description : ETX-2I-10G Hw: 0.1/A, Sw: 6.4.0(0.68) 
Name : ETX-2I-10G 
Location : The location of this device 
Contact : Name of contact person 
MAC Address : 00-20-D2-58-08-9F 
Engine Time : 2 days, 01:55:50 
 
Connectors Side : Front 
7.3 Environment 
You can define the chassis temperatures at which to send trap notifications of crossed temperature 
thresholds, enable or disable device automatic shutdown on overheat, and display information about 
chassis components and sensors status. 
Applicability and Scaling 
These features are applicable to all ETX‑2i products. 
ETX-2i Devices 
7. Administration 
Functional Description 
Device Temperature  
You can define minimum and maximum temperature thresholds, as well as temperature unit (Celsius or 
Fahrenheit), in order to receive trap notification that the device temperature has left the allowed range 
or returned to the allowed range.  
You can optionally use a hysteresis mechanism to avoid sending an excessive number of traps when a 
threshold is repeatedly crossed. The hysteresis defines the margin around the temperature thresholds 
for sending trap notification of temperature threshold crossed: 
• 
Sends trap notification of temperature too high when the temperature rises above <maximum 
temperature + hysteresis value>.  
• 
After sending a trap notification of temperature too high, it sends a trap notification of 
temperature OK when the temperature falls below <maximum temperature - hysteresis value>.  
• 
Sends trap notification of temperature too low when the temperature falls below <minimum 
temperature - hysteresis value>. 
• 
After sending a trap notification of temperature too low, it sends the trap notification of 
temperature OK when the temperature rises above <minimum temperature + hysteresis value>. 
Device Fan 
The device fan is activated when the temperature of the device exceeds a certain limit (defined by RAD 
HW engineers; unconfigurable). When the device temperature once again drops below that limit, the 
fan stops. 
A Fan Failure alarm is issued if the device fan stops working or its speed drops below 100RPM. 
Overheat Auto Shutdown 
Thermal shutdown of a device serves to prevent permanent damage of main components and avoid 
safety issues with the system. ETX‑2i supports automatic shutdown upon overheat detection. If enabled 
(the default), the device shuts down if it operates outside the normal operating range or if a component 
fails to cool the system (such as fan failure). When the core temperature of critical components 
measured by the system (with a built-in internal temperature sensor), approaches the high threshold at 
which permanent damage occurs, the system automatically shuts down to prevent it. The shutdown 
point varies from component to component (according to the manufacturer’s declaration) and therefore 
ETX-2i Devices 
7. Administration 
the threshold point varies per device. The temperature value for shutdown on overheat is statically 
defined for each device type and is not user configurable. 
 
Note 
• 
Temperature is of internal temperature sensors; not related to 
environmental temperature. 
• 
High and low temperature thresholds are preconfigured and set for each 
device by HW/Mechanical Engineering. They are not related to the 
environmental temperature.  
• 
All physical interfaces (ETH, SFP lasers), including Rx and Tx, shut down. 
• 
FPGA remains in reset state. 
• 
CPU remains in low power mode.  
ETX‑2i leaves an overheat shutdown state when the device temperature drops below the low 
temperature threshold. The device then automatically resets and boots up.   
Configuring the Chassis  
 To configure the chassis: 
1. Navigate to configure chassis. 
The config>chassis# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Enabling overheat 
auto shutdown 
[no] overheat-auto-
shutdown 
By default, the device automatically shuts down on 
overheat (overheat-auto-shutdown is enabled).  
Note: The temperature that determines overheating of 
the device is non-user configurable and varies 
according to the device. 
Setting lowest and 
highest allowed device 
temperature  
temperature-threshold 
{ celsius | fahrenheit } 
min <min-value> 
max <max-value> 
[ hysteresis <hysteresis- 
value> ] 
These user-configurable thresholds are used only for 
determining the sending of trap notifications.  
Note: These thresholds are not used for overheat 
automatic shutdown of the device; internal, 
unconfigurable temperature sensors are used for this. 
ETX-2i Devices 
7. Administration 
Task 
Command 
Comments 
Displaying 
environment 
information 
show environment 
Displays information about the following: 
• Type and status of the power supplies – AC, DC, DC 
Inlet, or -- (if it is absent or has failed) 
• Status of fans – indicates whether the fan is present 
and functioning properly, is absent (does not exist), 
or has failed 
• Temperature sensor – indicates the temperature, 
and whether the sensor is functioning correctly 
See Viewing Environment Information. 
Viewing Environment Information 
 To view environment information for ETX-2i: 
ETX-2i # configure chassis 
ETX-2i >config>chassis# show environment 
Power Supply   Type      Status          
--------------------------------------------------------------- 
1              AC        OK          
2              --        Not exist              
 
FAN                      Status     
--------------------------------------------------------------- 
1                        OK         
2                        OK         
 
Sensor    Value                         Status          
--------------------------------------------------------------- 
1.        32             Celsius        OK              
 To view environment information for ETX-2i-10G-B/8SFPP Outdoor: 
 
 
ETX-2i-10G-B-8SFPP-ODU>config>chassis# show environment  
 
Power Supply   Type      Status          
----------------------------------------------------------------------------- 
1              AC        OK              
2              --        Not exists          
 
 
 
ETX-2i Devices 
7. Administration 
FAN       Status     
----------------------------------------------------------------------------- 
 
Sensor    Value                         Status          
----------------------------------------------------------------------------- 
1.        43             Celsius        OK              
 
 To view environment information for ETX-2i-10G/8SFPP and ETX-2i-10G-B/8SFPP with 24 VDC PS 
ETX-2i-10G-B-8SFPP>config>chassis# show environment 
 
Power Supply   Type      Status          
----------------------------------------------------------------------------- 
1              --       Not exist              
2              DC       OK          
 
FAN       Status     
----------------------------------------------------------------------------- 
 
Sensor    Value                         Status          
----------------------------------------------------------------------------- 
1.        43             Celsius        OK              
 To view environment information for ETX-2i-10G/8SFPP and ETX-2i-10G-B/8SFPP with 24 VDC PS 
ETX-2i-10G-B-8SFPP>config>chassis# show environment 
 
Power Supply   Type      Status          
----------------------------------------------------------------------------- 
1              --        Not exist             
2              24Vdc     OK          
 
FAN       Status     
----------------------------------------------------------------------------- 
 
Sensor    Value                         Status          
----------------------------------------------------------------------------- 
1.        43             Celsius        OK              
 
 To view environment information for ETX-2i-100G: 
ETX-2i-100G>config>chassis# show environment 
Power Supply   Type      Status 
--------------------------------------------------------------- 
1              --        OK 
 
 
 

## 7.4 File Operations  *(p.1231)*

ETX-2i Devices 
7. Administration 
FAN       Status 
--------------------------------------------------------------- 
1         OK 
2         OK 
3         OK 
4         OK 
5         OK 
6         OK 
7         OK 
8         OK 
 
Sensor    Value                         Status 
--------------------------------------------------------------- 
1.        30             Celsius        OK 
Examples 
 To define temperature thresholds: 
• 
Minimum temperature = -20 degrees Celsius 
• 
Maximum temperature = 50 degrees Celsius 
• 
Hysteresis = 4 
exit all 
ETX‑2i>configure chassis 
ETX‑2i>config chassis#  
  temperature-threshold celsius min -20 max 50 hysteresis 4 
  exit all 
save 
7.4 File Operations 
You can perform the following operations on files: 
• 
Transfer device files via SFTP/TFTP 
• 
Transfer integrated module files via SFTP 
• 
Add a description to a file 
 
 
ETX-2i Devices 
7. Administration 
• 
Copy files within the ETX‑2i unit 
• 
Display files 
• 
Display file details and contents 
• 
Delete files 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products, with the following conditions:  
• 
x86 module is relevant for ETX-2i and ETX-2i-B with D-NFV. 
• 
Copy via TFTP is not relevant for x86 module; only via SFTP. 
Functional Description 
Device Files 
ETX‑2i supports the following files: 
• 
Device software files: sw-pack-1..sw-pack-4 
• 
Integrated module software files: im-sw-pack-1, im-sw-pack-2 (for ETX-2i and ETX-2i-B with 
D-NFV) 
• 
Integrated module software updates: im-sw-update-1, im-sw-update-2 (for ETX-2i and ETX-2i-B 
with D-NFV) 
• 
License files: license-1..license-n 
• 
Configuration files: running-config, rollback-config, startup-config, user-default-config, factory-
default-config, restore-point-config 
• 
Alarm and event logs: log, brief-log 
• 
Performance management (binary format): pm-0. This file collects the performance 
management information (statistics) gathered by the pm-collection command (for example: pm-
collection system interval <seconds>). 
• 
Performance management (CSV format): pm-csv. ETX‑2i converts the binary contents of pm-0 to 
CSV format, provided the user ran the reporting > pm-csv command. 
• 
Banner file: banner-text 
ETX-2i Devices 
7. Administration 
• 
Zero touch configuration file: zero-touch-config-xml 
• 
DB schema file: db-schema 
• 
DB configuration file: db-config 
• 
Scheduler log: schedule-log. If scheduled commands have been executed, the commands and 
their outputs are saved in this file. 
• 
User script: user-script. This file can contain a CLI script, which can be executed by a user. 
• 
Script result: script-result. The results of an executed CLI user script are saved here. 
• 
Compute node backup information: cn-backup-file (for ETX-2i/ETX-2i-B with D-NFV) 
• 
User files: user/<filename>  
• 
Syslog accounting log: accounting-log 
User Directory 
The ETX‑2i file system supports a directory for user files, called user. The size of the user directory varies 
per device and is determined by the disk space that the device can allot. You can copy files to and from 
the user directory and delete files that are not in use. User file names are strings between 1 and 32 
characters long. 
Commands for Copying Files 
You can copy or transfer files via the copy command, or via the commands shown in the following table. 
As shown in the table, some commands that reset the device also erase the saved user configuration by 
copying another file to it before the reset. 
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
and Maintenance 
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
ETX-2i Devices 
7. Administration 
Using SFTP or TFTP 
You can download or upload files to the ETX‑2i unit via SFTP/TFTP. However, you can download or 
upload files to the x86 module in ETX-2i and ETX-2i-B with D-NFV via SFTP only. Normally the types of 
files copied are configuration files and software files.  
The software files can also be downloaded to ETX‑2i via the Boot Manager, using XMODEM, SFTP, or 
TFTP. For details on upgrading the device software, refer to the Software Upgrade chapter. 
SFTP Application 
The SFTP protocol is used to provide secure file transfers via the product's Ethernet interface. SFTP is a 
version of FTP that encrypts commands and data transfers, keeping your data secure and your session 
private. For SFTP file transfers, an SFTP server application must be installed on the local or remote 
computer.  
A variety of third-party applications offer SFTP server software. For more information, refer to the 
documentation on these applications. 
Setting up SFTP Server 
If you use a local laptop and SFTP is the preferred transfer method, an SFTP server application must be 
installed on it.  
As mentioned above, third-party applications are available, and you should refer to their setup 
documentation. 
Note 
SFTP file transfers are carried out through TCP port 22. You should check that 
the firewalls you are using on the server and Windows allow communication 
through this port. If not, configure the firewall settings to open TCP port 22. 
TFTP Application 
The TFTP protocol is typically used for remote IP-to-IP file transfers via the product's Ethernet interface. 
It can be used, however, for local file transfer as well, as the transfer rate of the Ethernet interface is 
much faster than that of the RS-232 interface. 
For TFTP file transfers, a TFTP server application must be installed on the local or remote computer. As it 
runs in the background, the TFTP server waits for any TFTP file transfer request originating from the 
product and carries out the received request automatically.  
A variety of third-party TFTP applications are available that allow the instant creation of a TFTP server on 
a client computer. For more information, refer to the documentation on these applications.  
ETX-2i Devices 
7. Administration 
Setting up a TFTP Server 
If you use a local laptop and TFTP is the preferred transfer method, a TFTP server application must be 
installed on it.  
As mentioned above, third-party applications are available, and you should refer to their setup 
documentation.  
Note 
TFTP file transfers are carried out through UDP port 69. You should check that 
the firewalls you are using on the server and Windows allow communication 
through this port. If not, configure the firewall settings to open UDP port 69. 
Configuring TFTP Server Timeout Settings 
You can set the following TFTP server timeout settings from the system context. 
• 
retry-timeout – the minimum number of seconds between attempts to reconnect to the TFTP 
server. If the TFTP server connection fails, the device can resend a request only after the time 
defined in retry-timeout has elapsed. Retries to reconnect to the TFTP server can continue until 
the time defined in timeout (following command) has elapsed.  
• 
timeout – TFTP session timeout in seconds. When the TFTP connection fails for the defined 
timeout (in seconds), despite retries, the connection to the TFTP server times out, and a timeout 
error message is generated. 
 To set the TFTP timeouts: 
1. Navigate to configure system. 
2. At the config>system prompt, perform the required tasks from the following table. 
Task 
Command 
Comments 
Setting the number of 
seconds required 
between attempts to 
reconnect to TFTP 
server 
retry-timeout <seconds> 
timeout-seconds – the number of seconds required 
between attempts to reconnect to the TFTP server  
Possible values: 1-60  
Default: 15  
Setting the TFTP server 
connection timeout 
timeout <timeout-
seconds> 
timeout-seconds – the number of seconds after which 
the TFTP server connection terminates  
Possible values: 60-1000  
Default: 60  
ETX-2i Devices 
7. Administration 
Adding a File Description 
You can use the description command to attach a description to any file.  
Note 
Although you can add a description to any file, it is typically added to user 
files. 
 To add a description to a file: 
• 
At the file prompt, enter description <filename> <string> 
If a user file, filename comprises the directory name (user) followed by a / and the filename. For 
example: user/my-user-file. 
string – up to 255 characters. If string is more than one word, it should be enclosed in quotes 
(“”). 
Note 
You can remove the file description by entering no description. This sets the 
description to an empty string (the default). 
Copying Files  
You can use the copy command to copy files within the ETX‑2i unit or download/upload files to the 
ETX‑2i unit via SFTP/TFTP. You can also use the copy command to download/upload files to a unit’s 
integrated module (IM) via SFTP only (relevant for the x86 module in ETX­2i/ETX­2i-B with D-NFV). 
You can also use the copy command to download (send out of ETX‑2i) the PM file (pm-0 or pm-csv). If 
the command is executed while the device is in the middle of PM collecting, ETX‑2i finishes the record it 
is processing, and then closes the file and copies it. 
The file contains all the collected data (including the buffer open for writing if there is one). The data is 
concatenated back-to-back on a single copy session in order of creation (oldest first). 
While the file is being downloaded, ETX‑2i continues reading and saving aside PM counters, as required. 
Note 
You cannot manually copy a PM file (pm-0 or pm-csv) if pm-file-push is 
configured. In this case, the device exports it at fixed intervals. 
Once the file is successfully transferred, ETX‑2i does the following: 
• 
Deletes all data that was sent in the file.  
• 
Opens a new file and stores in it any PM counters that were read while the old file was being 
downloaded. 
ETX-2i Devices 
7. Administration 
• 
If the file transfer was initiated by a CLI session, sends a popup message to that session (version 
6.8.2 (2.75). 
If the file fails to be transferred, ETX‑2i does the following: 
• 
Reopens the file for writing. 
• 
Removes the Finish Time field (in case of pm-0; pm-csv does not have this field). 
• 
Inserts a special PM record (in case of pm-0; in pm-csv the time is written before every data 
record, and the base time is not used). 
• 
If the file transfer was initiated by a CLI session, sends a popup message to that session (version 
6.8.2 (2.75). 
Note 
• 
The x86 module in ETX­2i/ETX­2i-B with D-NFV has software images of its 
own (integrated module software files im-sw-pack-1, im-sw-pack-2) and 
its own integrated module software updates (im-sw-update-1, im-sw-
update-2), which are not part of the ETX­2i/ETX­2i-B software image. 
Nevertheless, ETX‑2i enables you to run the copy im-sw-pack-n and copy 
im-sw-update-n (where n is 1 or 2) commands from within the device 
itself to copy software packs/updates via SFTP only to the integrated 
module. In this case, the hosting device (ETX­2i/ETX­2i-B) passes the copy 
command to the x86 module for execution. The module executes the 
command and reports the results to the hosting device for further 
processing (e.g., displays a message, generates an event). 
• 
The Syslog local accounting-log file can be uploaded; it cannot be 
downloaded.  
• 
Before downloading a file to the user directory, verify that there is 
sufficient space by checking the number of Free Bytes on the output of the 
dir command (see Viewing Device Files example below). 
 To copy files: 
1. At any prompt, enter: 
copy <source-file-url> <destination-file-url> [hash] 
Where <file-url> = <url-prefix> <file> 
 
 
ETX-2i Devices 
7. Administration 
 
<url-prefix> can be empty, or one of the following: 
 
tftp://<ipv4-address>/ 
 
tftp://<ipv6-address>/ 
 
sftp://<username>:<password>@<ipv4-address>[:<port>]/ 
 
sftp://<username>@<ipv4-address>[:<port>]/ 
 
sftp://<username>:<password>@<ipv6-address>[:<port>]/ 
 
sftp://<username>@<ipv6-address>[:<port>]/ 
 
xmodem: 
Note 
• 
It is not necessary to enter <port> when using the well-known SFTP port. 
• 
The password that you enter for a user in the above sftp commands, is 
masked in TACACS+ and Syslog, appearing in the TACACS+ and Syslog 
command logs as asterisks (*), thus providing protection from sniffers. 
• 
Passwords can be passed in the CLI or entered separately. If you choose to 
pass it separately, omit it from the CLI command and enter it when 
prompted. 
 
<file> can be empty, or one of the following files, or the file name on a remote computer if 
applicable. If <file> is on a remote computer it can contain a path and file name, or just a file 
name. 
 
startup-config 
 
restore-point-config 
 
rollback-config 
 
running-config 
 
user-default-config 
 
factory-default-config 
 
log 
 
sw-pack-1, …, sw-pack-4 
 
im-sw-pack-1, im-sw-pack-2 (for x86 module in ETX-2i and ETX-2i-B with D-NFV) (via 
SFTP only) 
 
im-sw-update-1, im-sw-update-2 (for x86 module in ETX-2i and ETX-2i-B with D-NFV) 
(via SFTP only) 
 
zero-touch-config-xml 
 
banner-text 
 
pm-0 
 
pm-csv 
 
db-schema 
 
mac-table 
 
db-config 
 
ltm_1 
ETX-2i Devices 
7. Administration 
 
ltm_2 
 
ltm_9 
 
schedule-log 
 
accounting-log (can be uploaded; not downloaded) 
 
user-script 
 
script-result 
 
cn-backup-file (for ETX-2i/ETX-2i-B with D-NFV) 
 
The maximum length/range is: 
 
<username> – 1–60 characters 
 
<password> – 1–60 characters 
 
<file> – 1– 500 characters (250 characters for the full path and 250 characters for the 
filename) 
 
<port> – 1–65535 
 
Optional hash parameter indicates that the SFTP password is encrypted 
 
Password encryption can be configured using the command config>mngmnt>access# 
ztc-xml-generate-encrypted-password <cleartext> 
2. If the destination-file is on the device, respond to the following confirmation message that is 
displayed: 
! Are you sure? [yes/no] 
After all the sanity checks have passed and before starting the file transfer, the device displays 
the following message: 
! Starting file transfer… 
When copy finishes successfully, the device displays the following message: 
! <source-file> copied to <destination-file> successfully 
In case of non-local (i.e., upload or download) copy, a second line is displayed: 
! <file-size> bytes copied in <time-of-copy> secs (%rate bytes/sec) 
Viewing Copy Status 
You can display the status of current and past copy operations. 
 To display copy status: 
• 
At the file# prompt, enter: 
show copy [summary] 
ETX-2i Devices 
7. Administration 
Viewing Information on Files  
You can display the following information: 
• 
Files within the device 
• 
Files within the integrated module 
• 
User files within the User directory 
• 
Information on the configuration files 
• 
Contents of configuration text files 
• 
File details 
• 
Information on the software files (software packs). For information on upgrading to a different 
software pack, refer to the Software Upgrade chapter.  
Viewing Device Files 
ETX‑2i supports the dir command to show a list of all non-hidden files on the device, sorted by type and 
then by name. The command output also displays integrated module software packs (im-sw-pack-n) and 
integrate module software updates (im-sw-update-n) stored on the integrated x86 module (in 
ETX­2i/ETX­2i-B with D-NFV). 
 
Note 
• 
cn-backup-file is not displayed, as it is not saved on the device. 
• 
The output of the dir command lists pm-0 and pm-csv, both marked as 
File In Use in the file system, although the output of the pm-csv file does 
not really exist until a user tries to copy it. 
 To display the files within the device: 
• 
At the file# prompt, enter dir. 
 
 
ETX-2i Devices 
7. Administration 
Viewing User Directory Files 
ETX‑2i supports the dir folder [user] command to list the user files in the device’s user directory, sorted 
by name. 
 To display user files: 
• 
At the file# prompt, enter dir folder [user]. 
Note 
It is optional to enter folder-name, as user is currently the only available folder 
in the device. 
Viewing Device Configuration Files 
 To display information on the configuration files: 
• 
At the file# prompt, enter show configuration-files 
Information on the configuration files is displayed. 
Viewing File Details 
You can use the file-details command to display details of specific files. Possible Status values are: --, 
error in file, invalid header, not confirmed, loading failed, CRC error, temporarily in use, read only, copy 
in progress, corrupted, migration failed, error in migration, valid, File in Use.  
 To display file details: 
• 
At the file# prompt, enter:  
show file-details <filename> 
filename - for a user file, comprises the directory name (user) followed by a / and the filename. 
For example: user/my-user-file. 
 
 
ETX-2i Devices 
7. Administration 
Viewing Configuration Text File Contents 
You can use the show command to display the contents of text files stored in the file system.  
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
 To display the contents of user text files (i.e., files stored in the /user directory): 
• 
At the file# prompt, enter show user-dir <filename>. 
Note 
You can only display the contents of a user file that is not binary. 
 To display the contents of the running-config file: 
• 
From any level (global command), enter show running-config. 
Viewing Software File Details 
You can use the show sw-pack command to display details of installed software packs. 
 
Note 
The command output also lists general information on the software packs 
stored on the integrated x86 module (in ETX­2i/ETX­2i-B with D-NFV). It does 
not display the contents of the integrated x86 module. 
 To display information on the software files: 
• 
At the file# prompt, enter:  
show sw-pack [refresh [<sec>]] 
where sec represents the refresh timeout, with range 3–100. 
Information on the software files is displayed. The State of a SW file can be one of the following: 
active, ready, corrupted, downloading, previous active. 
ETX-2i Devices 
7. Administration 
Deleting Files 
You can delete the following files: 
• 
restore-point-config 
• 
rollback-config 
• 
script-result 
• 
startup-config 
• 
sw-pack-<n> (the inactive software pack) 
• 
user-default-config 
• 
user-script 
• 
zero-touch-config-xml 
Note 
You cannot delete cn-backup-file as it is not saved on the device. 
The output of the dir command lists pm-0 and pm-csv, both marked File In 
Use. This means that these files cannot be directly overridden or deleted. 
When you delete or override a software pack file, ETX‑2i displays a message:  
Previous software deleted; restore point lost. 
When you delete the restore-point-config file, ETX‑2i displays a message:  
restore-point-config delete; restore point lost. 
You delete im-sw-pack-# (integrated module software) via the ETX-2i/ETX-2i-B interface. In this case, 
ETX-2i/ETX-2i-B passes the delete command to the x86 module for execution. The x86 module executes 
the command and reports the results to ETX-2i/ETX-2i-B for further processing (e.g., displays a message, 
generates an event). 
 
Note 
Use caution in deleting files. 
 To delete a file: 
1. At the file# prompt, enter:  
delete {sw-pack-2|startup-config| rollback-config|user-default-config|zero-touch-config-
xml|restore-point-config|user-script|script-result} 
You are prompted to confirm the deletion:  
! The file will be erased. Are you sure? [yes/no] 
2. Confirm the deletion. 
ETX-2i Devices 
7. Administration 
Examples 
Copying Files within Device 
• 
Source file name – running-config 
• 
Destination file name – startup-config 
copy running-config startup-config 
Downloading via TFTP 
Copy software version to ETX‑2i: 
• 
TFTP server address – 192.10.10.10  
• 
Source file name – d:/img/ETX‑2i.img 
• 
Destination file name – sw-pack-2 
copy tftp://192.10.10.10/d:/img/ETX‑2i.img sw-pack-2 
Uploading via TFTP 
• 
TFTP server address – 192.10.10.10 
• 
Source file name – startup-config 
• 
Destination file name – c:/etx/config/db1conf.cfg 
copy startup-config tftp://192.10.10.10/c:/etx/config/db1conf.cfg 
Downloading via SFTP 
Copy software version to ETX‑2i: 
• 
SFTP server address – 192.20.20.20 
• 
SFTP username – admin 
• 
SFTP password – 1234 
• 
Source file name – bin/ETX‑2i.img 
• 
Destination file name – sw-pack-2 
copy sftp://admin:1234@192.20.20.20/bin/ETX‑2i.img sw-pack-2  
 
 
ETX-2i Devices 
7. Administration 
Copy software version to x86 module in ETX-2i/ETX-2i-B : 
• 
SFTP server address – 192.20.20.20 
• 
SFTP username – admin 
• 
SFTP password – 1234 
• 
Source file name – etx2i_1.1.0.100.tar.gz 
• 
Destination file name – im-sw-pack-1 
copy sftp://admin:1234@192.20.20.20/etx2i_ 1.1.0.100.tar.gz im-sw-pack-1 
Uploading via SFTP 
• 
SFTP server address – 192.20.20.20 
• 
SFTP username – admin 
• 
SFTP password – 1234 
• 
Source file name – startup-config 
• 
Destination file name – config/db1conf.cfg 
copy startup-config sftp://admin:1234@192.20.20.20/config/db1conf.cfg 
Viewing Device Files 
ETX‑2i# file 
ETX‑2i>file# dir 
Codes: C-Configuration  S-Software  L-License  LO-Log  O-Other  B-Banner U-User X-XML 
 
Name                                  Type Size(Bytes) Creation Date Status 
 
accounting-log                        LO   --         2015-07-31   Read Only     
                                                      00:00:34     File In Use   
db-config                             LO   --         2015-07-31   File In Use   
                                                      00:00:34                   
db-schema                             LO   --         2015-07-31   Read Only     
                                                      00:00:34                   
mac-table                             LO   --         2015-07-31   Read Only     
                                                      00:00:34                   
pm-0                                  LO   5278       2015-07-31   File In Use   
                                                      09:14:28                   
schedule-log                          LO   2500       2015-07-31   Read Only     
                                                      00:00:34     File In Use   
sw-pack-1                             S    30310086   2015-07-31   File In Use   
                                                      02:05:01                   
sw-pack-2                             S    33071119   2015-07-31   Prev In Use   
                                                      06:35:05                   
ETX-2i Devices 
7. Administration 
im-sw-pack-1                          S    249295130  2015-07-31 
                                                      02:05:03 
im-sw-pack-2                          S    249147392  2015-07-31   Read Only 
                                                      02:05:03 
startup-config                        C    7596       2015-07-31                 
                                                      00:10:08                   
rollback-config                       C    --         2015-07-31                 
                                                      00:01:05                   
user-default-config                   C    7596       2015-07-31                 
                                                      00:11:03                   
factory-default-config                C    902        2015-07-31   Read Only     
                                                      00:00:35                   
running-config                        C    --         2015-07-31   File In Use   
                                                      00:10:06                   
restore-point-config                  C    10339      2015-07-31   Prev In Use   
                                                      06:21:37                   
log                                   LO   660000     1970-01-03   Read Only     
                                                      16:17:51                   
xml-schema/port-summary.xsd           X    885        2015-07-31   Read Only     
                                                      00:00:35                   
xml-schema/system-summary-inventory.x X    931        2015-07-31   Read Only     
                                                      00:00:35                   
user-script                           U    --         2015-07-31                 
                                                      00:01:05                   
 
Total Bytes : 85618688  Free Bytes  : 20985856 
 
Bytes Available for PM : 4994722 
 
Note 
Information on im-sw-pack-1, im-sw-pack-2, im-sw-update-1, and im-sw-
update-2 only appears in dir output for ETX-2i/ETX-2i-B with x86 module. 
These files are displayed by the hosting device although they are actually 
stored on the integrated module. 
Viewing User Directory Files 
ETX‑2i# file 
ETX‑2i>file# user-file-dir 
Name               Type  Size (bytes)  Creation Date     Status 
------------------------------------------------------------------ 
my-default-config  U     2500          01.10.2017        read only 
                                       00:00:10 
 
Total Bytes : 28278784  Free Bytes  : 2402304 
Viewing Device Configuration Files 
ETX‑2i# file 
ETX-2i Devices 
7. Administration 
ETX‑2i>file# show configuration-files 
Configuration          Last Modified       Valid 
----------------------------------------------------------------------------- 
startup-config         2012-08-02 18:19:07 Yes 
factory-default-config 2012-08-13 17:18:07 Yes 
running-config         2012-04-10 00:00:06 Yes 
 
Device loaded from : startup-config 
 
running-config has been modified since last time it was equal to startup-config 
Viewing File Details 
ETX‑2i# file 
ETX‑2i>file# show file-details user/my-user-file 
 
Name        : user/my-user-file 
Size (bytes): 5000 
Created     : 2019-06-07 01:45:58 
Status      : valid 
Description : Running configuration backup from 1 October 
Viewing Software File Details 
ETX‑2i# file 
ETX‑2i>file# show sw-pack 
Name           Version      Creation Time          Actual 
--------------------------------------------------------------- 
sw-pack-1      6.7.0(0.21)  2019-05-12   11:00:00  active 
sw-pack-2      6.7.1(0.7)   2019-05-21   14:00:00  ready 
im-sw-pack-1   1.1.0.0      2019-03-17   09:24:00  ready 
im-sw-pack-2   1.1.0.1      2019-05-05   16:43:00  active 
 
 
sw-pack-1 Size (Bytes)  : 12670953 
 
Type      Name           Version      H/W Ver   Size 
                                                (Bytes) 
--------------------------------------------------------------- 
main      main.bin       6.7.0(0.21)  0.0       11774435 
yang      yang.bin       6.7.0(0.21)  0.0       693158 
e1t1      e1t1.bin       3.5.0(0.3)   0.0       203120 
 
 
 
 
ETX-2i Devices 
7. Administration 
sw-pack-2 Size (Bytes)  : 12679007 
 
Type      Name           Version      H/W Ver   Size 
                                                (Bytes) 
--------------------------------------------------------------- 
main      main.bin       6.7.1(0.7)   0.0       11782489 
yang      yang.bin       6.7.1(0.7)   0.0       693158 
e1t1      e1t1.bin       3.5.0(0.3)   0.0       203120 
 
Note 
Output of show sw-pack command shows general information of all sw-packs, 
including im-sw-pack-1 and im-sw-pack-2 of ETX-2i/ETX-2i-B with x86 module. 
It shows detailed information of device sw-packs only.  
Deleting a File 
ETX‑2i# file 
ETX‑2i>file# delete startup-config 
! The file will be erased. Are you sure? [yes/no] _yes 
Configuration Errors 
The following table lists messages generated by ETX‑2i when a configuration error is detected. 
Message 
Description 
Cannot copy, destination file is labeled in-
use 
You attempted to copy to a file on the device that is in use. 
Cannot copy, destination file is labeled 
read-only 
You attempted to copy to a read-only file on the device. 
Cannot copy, incorrect file name 
You attempted to copy to a file on the device, but the file is not 
supported by the device. 
Cannot copy; maximum number of 
software packs exceeded 
You tried to copy to the device more software packs than the 
device supports. 
Cannot copy; only local configuration files 
may override candidate-config 
You tried to copy a non-local (not on the device) configuration file 
to the candidate-config file. 
Cannot execute; copy in progress 
You tried running another command to copy or delete either the 
source or the destination file of the copy, while a current copy is in 
progress. 
ETX-2i Devices 
7. Administration 
Message 
Description 
You tried running a command that would change configuration 
permanently (e.g., enter the database, while a copy of running-
config to startup-config is in progress. 
You tried installing software or a license while a copy is in 
progress. 
Cannot override restore-point-config 
You tried overriding restore-point-config. (You are only allowed to 
delete it.) 
Could not apply cn-backup-file 
The destination was cn-backup-file, but the copy failed because 
the device could not apply it (after it was received) 
Could not copy, maximum number of 
active copy sessions has been reached 
You tried copying a file while the maximum number allowed copy 
sessions are active. 
Could not copy <source-file> to 
<destination-file>, protocol is not allowed 
You attempted to perform the copy command, but TFTP is 
disabled. 
You attempted to perform the copy command, but SFTP is 
disabled. 
Could not create cn-backup-file 
The source was cn-backup-file, but the copy failed because the 
device could not create it. 
Could not establish connection with 
server 
The server does not respond to the copy, or if connection with the 
server could not be established. 
Could not find file 
Copy failed because the source file could not be found. 
Destination file access violation 
You tried accessing a destination-file with insufficient user rights, 
user authentication failed (in case of SFTP), or cipher (key 
exchange) mismatched (in case of SFTP). 
File may not be copied while pm-file-push 
is configured 
You tried copying a file although the pm-file-push command is 
configured. 
Insufficient storage space 
Copy failed due to lack of space. 
Integrated module user directory full 
You tried copying a file to the integrated module user directory, 
but it does not have sufficient space to accommodate the file. 
Invalid source file 
You tried copying a source-file that is marked as invalid to a 
destination-file on the device. 
Source file access violation 
You tried accessing a source-file with insufficient user rights, user 
authentication failed (in case of SFTP), or cipher (key exchange) 
mismatched (in case of SFTP). 

## 7.5 Inventory  *(p.1250)*

ETX-2i Devices 
7. Administration 
Message 
Description 
Source file labeled invalid 
You tried copying an invalid banner file or configuration file 
(starup-config, rollback-config, candidate-config, user-default-
config) to the device. 
User directory full 
You tried copying a file to the user directory, but it does not have 
sufficient space to accommodate the file. 
7.5 Inventory 
ETX‑2i supports inventory display, enabling you to view and monitor the unit’s components, hardware 
and software revisions, and power supply types. You can display an inventory table that shows all 
installed components, and you can display more detailed information for each component. You can 
configure an alias name, asset ID, and serial number for inventory components. 
You can save the output of the inventory summary command to an XML file in the user directory. The 
XML schema of the output file is stored in the read-only system-summary-inventory.xsd file in the 
RADOS file system xml-schema directory. 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products; however, the inventory display differs for each product 
according to the different chassis components and port configurations. 
 
 
Note 
PMC does not support the show summary-inventory command. However, 
inventory information is stored in the MIB table entityTable, which can be 
read via SNMP. 
Standards Compliance 
The inventory feature is implemented according to RFC 4133 – Entity MIB (RFC 2737 was made obsolete 
by RFC 4133 version 3). 
ETX-2i Devices 
7. Administration 
Viewing Inventory Information 
 To display the inventory table: 
• 
At the config>system# prompt, enter: 
show summary-inventory 
The inventory table is displayed (see Examples for a typical inventory table output). 
You can display more information for each installed inventory component. To do so, you need to enter 
the inventory level with the corresponding inventory component index, which is displayed in the Index 
column in the output of show summary-inventory.  
 To display the inventory component information: 
1. Navigate to configure system inventory <index>. 
2. Enter show status. 
Information for the corresponding inventory component is displayed (see Examples for typical 
inventory information outputs). The following table contains information on the parameters: 
Parameter 
Description 
Description 
Description of component type, in the form: 
RAD.<device-name>.< Physical  Class>, e.g., RAD.ETX‑2i.Port 
Contained In 
Index of the component that contains the component for which information is 
displayed. This is 0 for the chassis, as it is not contained in any component, and 
1001 for all other components, as they are all contained in the chassis. 
Physical Class 
Class of component 
Possible values: Chassis, CPU, Power Supply, Fan, Sensor, Port, Container, 
Module 
Relative Position 
Contains the relative position of this component among other components in 
the same index range (e.g., index 4001–4002, etc.) 
ETX-2i Devices 
7. Administration 
Parameter 
Description 
Name 
Name of component 
Possible values (according to component type):  
<device-name> – Chassis 
CPU 
DC Inlet 
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
CLEI Code 
CLEI code (relevant only for power supply) 
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
For ETX‑2i this is normally true only for the chassis, and for the dual power 
supplies. 
ETX-2i Devices 
7. Administration 
Parameter 
Description 
Intel Atom/Xeon D 
Processor name 
Possible processors: 
C2558 – Intel Atom Rangeley C2558 
C2758 – Intel Atom Rangeley C2758 
D1517 – Intel Xeon D D1517 
D1537 – Intel Xeon D D1537 
Quad/Octal Core 
Core size 
Possible values: 
4 – Quad  
8 – Octal 
Core Frequency 
Possible values: 2.4GHz, 2.3GHz, 2.2GHz 
Volume 
RAM volume 
Possible values: 8 GByte, 16 GByte, 24 GByte 
HD Type 
Hard Drive type 
SSD M2.0/2.5” 
HD Volume 
128 GByte w/wo PLP, 256 GByte 
 To save the inventory summary to an XML file: 
1. Enter configure system xml-export summary-inventory <filename>. 
filename is the unique 1-32 characters string name of the XML file to be saved in the user 
directory; it cannot contain a path (i.e., slashes and backslashes).  
2. If filename exists, the following message appears:  
/user/<filename> exists. Overwrite it? [Yes/No] 
Enter Yes to overwrite the existing file. 
Enter No to cancel the command. In this case, the CLI prompt returns (without further 
messages). 
3. If the file is successfully written, the following message appears: 
The output was written to /user/<filename>. 
ETX-2i Devices 
7. Administration 
Setting Inventory Information 
If necessary, you can configure the alias, asset ID, and serial number for inventory components. To 
configure the information, you need to enter the inventory level with the corresponding inventory 
component index shown in the Index column in the output of show summary-inventory.  
 To set inventory component information: 
1. Navigate to configure system inventory <index>. 
The config>system>inventory(<index>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Assigning user-defined alias to 
component  
alias <string> 
Entering no alias removes the 
alias. 
Note: Configuring the alias is 
meaningful only for the chassis 
component. It can be used by 
a network manager as a 
non-volatile identifier for the 
device. 
Assigning user-specific asset 
identifier to the component (usually 
for removable physical components) 
asset-id <id> 
Entering no asset-id removes 
the asset ID. 
Assigning vendor-specific serial 
number to the component 
serial-number <string> 
Entering no serial-number 
removes the serial number. 
Note: This configurable 
vendor-specific serial number 
is not related to the read-only 
manufacturer serial number. 
Examples 
  
 To display inventory summary for ETX-2i: 
ETX-2i# configure system 
ETX-2i# config>system# show summary-inventory 
 
 
ETX-2i Devices 
7. Administration 
Index Physical Class Name                HW Ver SW Ver       FW Ver 
----------------------------------------------------------------------------- 
1001  Chassis       ETX-2i               0.1/   6.8   5.0.0.0.0.36     
4001  Fan           Fan 1                                                
4002  Sensor        Temperature Sensor 1                                 
4003  Power Supply  PS 1                                                 
4007  Power Supply  PS 2                                                 
7001  Port          Time of Day Port                                     
7002  Port          Mini BNC                                             
7003  Port          External Clock Port                                  
7004  Port          RS-232 Control Port                                  
7005  Port          MNG Port                                             
7006  Port          ETH Port 0/1                                         
7007  Port          ETH Port 0/2                                         
7008  Port          ETH Port 0/3                                         
7009  Port          ETH Port 0/4                                         
7010  Port          ETH Port 0/5                                         
7011  Port          ETH Port 0/6                                         
7012  Port          ETH Port 0/7                                         
7013  Port          ETH Port 0/8     
 To display inventory information for ETX-2i port 0/1: 
ETX-2i>config>system# inventory 7006 
ETX-2i>config>system>inventory(7006)# show status 
Description       : ETX-2i Ethernet Port 
Contained In      : 1001 
Physical Class    : Port 
Relative Position : 6 
Name              : ETH Port 0/1 
HW Ver            : 
SW Ver            : 
FW Ver            : 
Serial Number     : 
MFG Name          : RAD 
Model Name        : 
Alias             : 
Asset ID          : 
FRU               : False 
 To display inventory information for ETX-2i chassis: 
ETX‑2i>config>system# inventory 1001 
ETX‑2i>config>system>inventory(1001)# show status 
Description       : ETX‑2i Ethernet Port 
Contained In      : 1001 
Physical Class    : Port 
Relative Position : 6 
 
 
ETX-2i Devices 
7. Administration 
Name              : ETH Port 0/1 
HW Ver            : 
SW Ver            : 
FW Ver            : 
Serial Number     : 
MFG Name          : RAD 
Model Name        : 
Alias             : 
Asset ID          : 
FRU               : False 
TBD 
Intel Atom        : C2558/2758  
Quad/Octal Core 
Core Frequency    : 2.4GHz 
Volume            : 8 GByte 
HD Type           : SSD M2.0/2.5” 
HD volume         : 128 GByte w/wo PLP 
 To display  inventory information for ETX-2i power supply: 
ETX‑2i>config>system# inventory 4007 
ETX‑2i>config>system>inventory(4007)# show status 
Description       : ETX‑2i Power Supply 2 
Contained In      : 1001 
Physical Class    : Power Supply 
Relative Position : 7 
Name              : 24 VDC 2 
HW Ver            : 0 
SW Ver            : 
FW Ver            : 
Serial Number     : TD200021175 
CLEI Code         : E5PSN24ACF 
MFG Name          : RAD 
Model Name        : PS100DC-12V-I2C 
Alias             : 
Asset ID          : 
FRU               : True 
 To display inventory summary for ETX-2i with VDSL module: 
ETX-2i>config>system# show summary-inventory 
Index Physical Class Name          HW Ver    SW Ver          FW Ver 
----------------------------------------------------------------------------- 
1001  Chassis        ETX-2i        0.1/      5.9.1(0.22)     5.0.0.0.0.62 
3001  Container      Slot 1 
3002  Container      Slot 2 
4001  Fan            Fan 1 
4002  Sensor         Temperature Sensor 1 
4003  Power Supply   PS-AC 1 
5001  Module         VDSL-MODULE              ACB       1.00(UHZ.0)b10    1.2 
5006  Port           PCS PORT 1 
ETX-2i Devices 
7. Administration 
7001  Port           External Clock Port 
7002  Port           RS-232 Control Port 
7003  Port           MNG Port 
7004  Port           ETH Port 0/1 
7005  Port           ETH Port 0/2 
7006  Port           ETH Port 0/3 
7007  Port           ETH Port 0/4 
8001  CPU            CPU 
 
 To display inventory information for ETX-2i VDSL module: 
ETX-2i>config>system# inventory 5001 
ETX-2i>config>system>inventory(5001)# show status 
Description       : VDSL-MODULE 
Contained In      : 0 
Physical Class    : Module 
Relative Position : 0 
Name              : VDSL-MODULE 
HW Ver            : ACB 
SW Ver            : 1.00(UHZ.0)b10 
FW Ver            : 1.2 
Serial Number     : 1505250004 
MFG Name          : 
Model Name        : ETX-M/VDSL-ISDN 
Alias             : 
Asset ID          : Put your string here 
FRU               : 
 
 To display inventory summary for ETX-2i-B with x86 Rangeley card: 
ETX-2i-B-10x1G # configure system 
ETX-2i-B-10x1G >config>system# show summary-inventory 
Index Physical Class Name            HW Ver    SW Ver            FW Ver 
1001  Chassis ETX-2IB-10x1G          0.0/A     6.8       5.2.B.0.0.6 
4001  Fan            Fan 1 
4002  Sensor         Temperature Sensor 1 
4003  Power Supply   PS 1 
7001  Port           RS-232 Control Port 
7002  Port           MNG Port 
7003  Port           ETH Port 0/1 
7004  Port           ETH Port 0/2 
7005  Port           ETH Port 0/3 
7006  Port           ETH Port 0/4 
7007  Port           ETH Port 0/5 
7008  Port           ETH Port 0/6 
7009  Port           ETH Port 0/7 
7010  Port           ETH Port 0/8 
8001  CPU            CPU 

## 7.6 Licensing  *(p.1258)*

ETX-2i Devices 
7. Administration 
 To display inventory summary for ETX-2i-10G-B/8SFPP Outdoor: 
Index Physical Class Name                     HW Ver    SW Ver            FW Ver            
----------------------------------------------------------------------------- 
1001  Chassis        ETX-2i-10G-B-8SFPP       0.0/      6.8.2(0.07)       6.8.0.8SFPB.0.1.0 
4001  Sensor         Temperature Sensor 1                                                   
4002  Power Supply   PS-AC 1                  0                                             
4003  Power Supply   PS-DC 2                  0                                             
7001  Port           Time of Day Port                                                       
7002  Port           Mini BNC                                                               
7003  Port           External Clock Port                                                    
7004  Port           RS-232 Control Port                                                    
7005  Port           MNG Port                                                               
7006  Port           ETH Port 0/1                                                           
7007  Port           ETH Port 0/2                                                           
7008  Port           ETH Port 0/3                                                           
7009  Port           ETH Port 0/4                                                           
7010  Port           ETH Port 0/5                                                           
7011  Port           ETH Port 0/6                                                           
7012  Port           ETH Port 0/7                                                           
7013  Port           ETH Port 0/8                                                           
8001  CPU            CPU                                        
Configuration Errors 
The following table lists messages generated by ETX‑2i when a configuration error is detected. 
 Message 
Description 
Filename may not contain / or \ 
You attempted to save the show summary-inventory command to 
an XML file containing a path.  
Insufficient storage space 
The XML file containing the show summary-inventory output is too 
large to save in the user directory.  
7.6 Licensing 
Some features require a license to be enabled before the feature can be configured. The license 
mechanism enables fewer software version variants to be produced and can also be used to track 
licensed feature usage. 
 
 
ETX-2i Devices 
7. Administration 
The following licenses are available: 
• 
TWAMP 
• 
Traffic Management Fault Propagation (TMFP) 
• 
SFP+ 10GbE Rate (ETX-2i-10G) license (two or four-port) 
 
Note 
You should only activate features on a device after acquiring the appropriate 
license from RAD (through a license order or specific device ordering options). 
Activating a license-based feature without acquiring the appropriate license 
shall be considered a breach of your undertakings and entitles RAD to stop 
supporting the device and may also result in legal action. 
Applicability and Scaling 
SFP+ 10GbE rate licenses are relevant for ETX-2i-10G only. 
In ETX-2i-100G, licensing is not required for both 10G and 100G rates.  
TWAMP and TMFP licenses are applicable to all ETX‑2i products. 
Factory Defaults 
By default, feature licenses are disabled. 
Functional Description 
A feature that requires a license can be configured only if the feature license is enabled.  
For backward compatibility, if a feature was defined as requiring a license after having already been 
released without a license in a previous software release, the feature configuration is allowed if it was 
done in a release that did not require a license. In this case, a command enabling the license is 
automatically added to the running-config file.  
If ETX‑2i loads a configuration file that configures a feature requiring a license when the license is not 
enabled, the device rejects that feature’s configuration if the configuration file was created by a 
software version that requires a license. 
ETX-2i Devices 
7. Administration 
Fault Propagation Event Manager License  
Use of standard fault propagation features does not require a license. However, use of enhanced Fault 
Propagation Event Manager actions, such as shaper-swap (for changing queue block Shaper rate) and 
policer-swap (for changing flow Policer rate), as well as use of enhanced triggers, requires an enabled 
Traffic Management Fault Propagation (TMFP) license. 
SFP+ 10GbE Rate License 
Note 
The SFP+ 10GbE rate license is only required for ETX-2i-10G. It is not required 
for ETX-2i-100G. 
ETX-2i-10G devices have up to four SFP+ ports with each port’s rate preconfigured to 1GbE or 10GbE, 
according to the specific ordering option. 
The ordering option is indicated by the sfp-plus-factory-10g-rate and can be: 
• 
None: Ports 1-4 are 1G; no 10G capability 
• 
2: Ports 1-2 are 1/10G (default rate: 10G); ports 3-4 are 1G 
• 
4: Ports 1-4 are 1/10G (default rate: 10G) 
In the case that the ordering option specifies four 10GbE SFP+ ports, all SFP+ Ethernet ports are 
supported with 10GbE, and sfp-plus-10g-rate license is not applicable.  
In the case that the ordering option specifies two 10GbE SFP+ ports, two SFP+ Ethernet ports are 
supported with 1/10GbE, and a two-port sfp-plus-10g-rate license can be applied. In this case,  
sfp-plus-10g-rate is 2.   
An ordering option without any 10G capability for the SFP+ is also available. In this case, a two or four 
10G license may be applied. 
It is possible to upgrade the SFP+ ports (two or four) that are not set to 10GbE by the ordering option, 
using the two-port or four-port license provided by RAD.  
• 
If two SFP+ ports are set to 10GbE rate according to the ordering option, only SFP+ ports 3 and 4 
can be configured to the 10GbE rate using the two-port license.  
• 
If no SFP+ ports are set to 10GbE rate according to the ordering option, any two SFP+ ports can 
be configured to the 10GbE rate using the two-port license. 
If at any stage, a device returns to its factory default settings, the  
user-configurable sfp-plus-10g-rate license is deleted. 
ETX-2i Devices 
7. Administration 
Configuring Licenses 
The ETX‑2i TWAMP, enhanced Fault Propagation Event Manager features, as well as the ETX-2i-10G 
SFP+ Ethernet port rate upgrade to 10GbE, require a license. 
Traffic Management Fault Propagation (TMFP) license and TWAMP license in a VNF (not in a device) are 
protected by a hardcoded password only known to you. Configuration of the enhanced FP Event 
Manager or TWAMP (in VNF) features requires you to enable the respective password-protected 
licenses. 
The SFP+ Factory 10G Rate license is set in the factory. You cannot enable or disable it but can view its 
status and whether it is in use.  
 To enable licenses: 
1. Navigate to admin license. 
The admin>license# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Enabling TWAMP 
license in device  
license-enable twamp 
 
Enabling TWAMP 
license in VNF 
license-enable twamp 
<password> [hashed] 
password – hardcoded password assigned to the 
device. 
hashed – If this option is specified, the device assumes 
the entered password is hashed. If not specified, the 
device assumes the password is plain text (non-
encrypted), and if correct, hashes the password, and 
saves the hashed result in the license hard password 
feature. 
Enabling Traffic 
Management Fault 
Propagation (TMFP) 
license 
license-enable tmfp 
<password> [hashed] 
Enabling SFP Plus 10g 
rate license 
license-enable sfp-plus-
10g-rate <amount> 
amount – number of SFP+ ports that can be upgraded 
to 10GbE 
Possible values: 2, 4 
ETX-2i Devices 
7. Administration 
Task 
Command 
Comments 
Disabling license 
no license-enable 
<feature> 
feature – licensed feature 
Possible values: 
sfp-plus-10g-rate 
tmfp  
twamp 
Note: 
• You can disable a license, provided running-config 
does not contain a configuration that is prohibited 
without a license. 
• You can disable the TMFP license, provided 
enhanced Fault Propagation Event Manager actions 
have not been configured. 
• You can disable the TWAMP license, provided 
TWAMP entities have not been configured. 
 
Viewing License Status Summary 
You can generate a summary of all the feature licenses in the device.  
This example displays the license summary. 
ETX-2i-10G>admin>license# show summary 
Feature                  Status   Amount In Use 
----------------------------------------------- 
  
Feature Name                            Status    Amount    In Use 
----------------------------------------------------------------------------- 
TWAMP                                   Disabled  --        -- 
Traffic Management Fault Propaga        Enabled   --        Yes 
SFP+ 10G Rate                           Enabled   2         1 
SFP+ Factory 10G Rate                   Enabled   4         4 
 
ETX-2i Devices 
7. Administration 
Parameter 
Description 
Feature 
Feature name 
Possible values: 
SFP+ 10G Rate 
SFP+ Factory 10G Rate (not configurable; indicates the ordering option)   
Traffic Management Fault Propagation 
TWAMP 
Status 
License status 
Possible values: Enabled, Disabled 
Amount 
License amount 
Possible values:  
• -- : not applicable (for TMFP and TWAMP)  
• <1-4>: number of 10GbE licensed SFP+ ports  
In Use 
Indicates whether the license is in use.  
Possible values: 
• -- : not applicable (for disabled license) 
• Yes/No: indicates whether enabled TMFP or TWAMP license is in use 
• <1-4>: number of 10GbE licensed SFP+ ports in use. The feature is considered in use 
if the port is configured as 1s0GbE and enabled in running-config.  
Configuration Errors 
The following table lists messages generated by ETX‑2i when a configuration error is detected. 
  Message 
Description 
License needed by running configuration 
You attempted to disable the license for a feature that is 
configured in the device running configuration. 
License required 
You attempted to configure a feature that requires a license, and 
the license is disabled. 
Wrong password 
You failed to set the correct password for the device. 
 

## 7.7 Login Banner  *(p.1264)*

ETX-2i Devices 
7. Administration 
7.7 Login Banner 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. 
Functional Description 
You can define a banner to be displayed before the login prompt for username, as well as a banner to be 
displayed following successful login. You can define the pre-login banner using the CLI command login-
message, and the post-login banner using the CLI command announcement. A banner file can also be 
used to define a pre-login banner, provided it is supported in the device. Although the banner file is 
maintained for backward compatibility, it is recommended to use a CLI command to define the pre-login 
banner. Note that a device cannot simultaneously support a banner file and banner command.  
 
Note 
If you are accessing ETX‑2i via SSH, the banner is printed between the 
username prompt and the password prompt 
Defining Login Banners via CLI Commands 
You can define a banner to be displayed before login, as well as another banner to be displayed 
following login. 
Pre-login and post-login banner messages must satisfy the following: 
• 
Message must be enclosed in single quotation marks if it is longer than 600 characters or 
includes special characters. (Otherwise, if a message has no more than 600 characters and only 
includes alphanumeric characters, it does not have to be enclosed in single quotes.)  
• 
A message that spans multiple lines is interpreted as if it were written in one line; <cr> and <lf> 
between lines in the configuration file or command are ignored.  
• 
A message can contain printable characters, as well as the following special characters (only 
relevant for CLI; from SNMP, these characters should be entered normally): 
 
\n – new line 
 
\r – carriage return 
 
\r\n – carriage return to beginning of next line 
ETX-2i Devices 
7. Administration 
 
\t – horizontal tab 
 
\’ – single quotation mark 
 
\\ – backslash 
• Usage of special characters reduces the maximum number of printable characters that the banner can contain. 
For example, if the banner contains \n, up to 1998 additional printable characters can be used. The banner can 
be up to 2000 characters (including the escape / characters), in groups of up to 600 characters, provided you 
press <Enter> before or once you reach the 600th character of a group, and before entering a closing quotation 
mark.  
Note that when you press <Enter> before entering a closing quotation mark, although it is valid to do so, the 
device displays the warning message: 
Enter message.  End with the single quotation character (‘). 
• 
If you try to configure a banner longer than 600 characters, without pressing <Enter>, the device 
displays the following error message: 
# cli error: input token too big 
# maximum token size is 600 
• 
If you try to configure a banner totaling more than 2000 characters, the device displays the 
following error message: 
# cli error: invalid message 
 To configure a pre-login banner: 
1. Navigate to configure system. 
The config>system# prompt is displayed. 
2. Type login-message <message>, enclosing the message in quotes. 
At the next login, this pre-login banner is displayed. 
If a banner­text file already exists in the device, the device rejects the command with the error 
message: 
Cannot configure banner while banner­text file exists 
Note 
Type no login-message to remove a previously configured pre-login banner. 
 To configure a post-login banner: 
1. Navigate to configure system. 
The config>system# prompt is displayed. 
2. Type announcement <message>, enclosing the message in quotes. 
After the next login, this post-login banner is displayed. 
Note 
Type no announcement to remove a previously configured post-login banner. 
ETX-2i Devices 
7. Administration 
You can display the banners configured for ETX‑2i by navigating to the device level and entering info. For 
example: 
ETX‑2i# info  
version "3.01A14" sw "5.9.1(0.08)"  
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
ETX‑2i# 
Defining Pre-Login Banner Using a Banner File 
 To define the banner using a banner file: 
1. Create a text file called banner-text that contains the banner to display. 
Note 
• 
The banner must contain only printable ASCII characters (0x20–0x7E), 
<Enter> (0x0D), <Line Feed> (0x0A), and <Tab> (0x09) 
• 
The banner file can contain up to 2000 characters. 
2. Transfer the file banner-text to ETX‑2i. 
At the next login, the banner is displayed. 
If the device already contains the pre-login CLI command login-message, the device rejects the 
banner-text file download and displays the CLI error:  
Cannot load banner­text file while login-message is configured. 
You can display the banner defined for ETX‑2i by navigating to the file level and entering show 
banner-text, as shown in the example below. 
ETX‑2i# file  
ETX‑2i>file# show banner-text 
******* Authorized users only ******* 
 
 

## 7.8 Sending a Message to Connected Users  *(p.1267)*

ETX-2i Devices 
7. Administration 
Given the banner file above, the banner is displayed before login, as shown below. 
******* Authorized users only ******* 
user> 
7.8 Sending a Message to Connected Users 
ETX‑2i enables any connected su level user – local or remote (console, TELNET, SSH, and more) to send a 
message of up to 2000 characters to all other connected CLI users. Allowing users to send messages to 
other users simplifies on-site operation. 
• 
The command is not saved in the configuration file and cannot be invoked from a configuration 
file.  
• 
The message cannot be sent while the running configuration is being saved. 
 To send a message: 
1. Navigate to admin. 
2. Execute send <message>. 
where message is a character string up to 2000 characters long. 
Confirmation is requested to send the message: 
Send message? [yes/no] 
3. Enter yes to confirm sending the message. 
The device outputs the following: 
*** 
*** Message from <terminal name> to all terminals: 
*** 
<message> 
Where <terminal name> is either tty or vty#. 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. 

## 7.9 Reset  *(p.1268)*

ETX-2i Devices 
7. Administration 
Example 
This example displays sending a message to other users. 
ETX‑2i>admin# send Reminder: System rebooting at 21:00 
 Send message? [yes/no] _ yes 
*** 
*** Message from vty1 to all terminals: 
*** 
Reminder: System rebooting at 21:00 
Configuration Errors 
The following table lists the message generated by ETX‑2i when a configuration error is detected. 
Message 
Description 
Message may not exceed 2000 characters 
You entered a message longer than 2000 characters. 
7.9 Reset 
Note 
This section describes how to reset using CLI commands. You can also reset 
the device to its factory defaults or user configured defaults by pressing the 
push button on the front panel. For details, refer to Resetting Unit to Default 
in the Operation and Maintenance chapter. 
ETX‑2i supports the following types of reset: 
• 
Reset to factory defaults  
• 
Reset to user defaults 
• 
Overall reset (restart) of the device 
Note 
You can request that the active software pack be confirmed after the next 
reboot of ETX‑2i. Refer to the description of installing software in the 
Software Upgrade chapter for details. 
ETX-2i Devices 
7. Administration 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. 
Resetting to Factory Defaults 
You can reset ETX‑2i to its factory defaults using either of the following commands:  
• 
factory-default – for customer use 
• 
factory-default-all – for use by RAD Operations personnel prior to releasing the device for 
shipment to revert the device to its prior-to-shipment state 
The factory-default and factory-default-all commands have the following differences:  
• 
factory-default always reloads the device with factory-default-config. factory-default-all 
reloads the device with user-default-config, if it exists; otherwise, with factory-default-config. 
• 
factory-default only deletes startup-config.  
factory-default-all clears the log files and deletes most filesexcept for factory-default-config, 
user-default-config, licenses, banners, software, mac-table, pm (including the legacy statistics 
collection file), db-schema, and db-config. It also resets file creation times in the file system.  
• 
factory-default-all resets the snmpEngineBoots parameter to 1. This parameter counts the 
number of times the SNMP engine was restarted and is maintained throughout reboots to 
prevent replay attacks. 
 
Note 
• 
It is not recommended for customers to use the factory-default-all 
command, as it resets the SNMP object (snmpEngineBoots). This can 
result in the management system incorrectly assuming that the original 
device was replaced by another impersonating device, and therefore the 
management system refuses to communicate with the device. In such 
cases, the manager must manually delete the device from the map and 
then redraw it. To avoid such issues resulting from the resetting of 
snmpEngineBoots, it is recommended to use instead user-default or 
factory-default and then manually delete unneeded files and clear logs, as 
required. 
• 
The ETX-2i-10G Four SFP+ Ethernet Ports license is not affected by the 
device reset to factory defaults. 
ETX-2i Devices 
7. Administration 
 To reset ETX‑2i to factory defaults: 
1. At the admin# prompt enter: 
factory-default 
A confirmation message is displayed: 
Current configuration will be erased and device will reboot with factory default 
configuration. Are you sure? [yes/no] 
2. Enter yes to confirm the reset to factory defaults. 
The factory-default-config file is copied to the startup-config file. The unit resets, and after it 
completes its startup the factory defaults are loaded. If a startup-config confirm request was 
active, it is canceled. 
 To reset ETX‑2i to factory defaults and revert the device to its prior-to-shipment state: 
1. At the admin# prompt enter: 
factory-default-all 
A confirmation message is displayed: 
The device will delete its entire database and reboot. Are you sure? [yes/no] 
2. Enter yes to confirm the reset to factory defaults with configuration and counter reset. 
The configuration and counter reset explained above is performed, the unit resets, and after it 
completes its startup the factory defaults are loaded. If a startup-config confirm request was 
active, it is canceled. 
Note 
• 
If you perform admin factory-default or admin factory-default-all while 
the save command is being processed, these operations are blocked until 
save completes. 
• 
In case the saving process takes too much time or has complications, you 
can perform force-reboot from the admin prompt. 
 
 
 
ETX-2i Devices 
7. Administration 
Resetting to User Defaults 
You can use the user-default command to reset ETX‑2i to the configuration stored in user-default-config, 
a file which contains user default parameters that are usually different from RAD’s factory default 
parameters. 
 To reset ETX‑2i to user defaults: 
1. At the admin# prompt enter: 
user-default 
A confirmation message is displayed: 
Current configuration will be erased and device will reboot with user default 
configuration. Are you sure? [yes/no] 
2. Enter yes to confirm the reset to user defaults. 
The user-default-config file is copied to the startup-config file. The unit resets, and after it 
completes its startup the user defaults are loaded. If a startup-config confirm request was 
active, it is canceled. 
Restarting the Unit 
If necessary, you can restart ETX‑2i without interrupting the power supply. 
 To restart ETX‑2i: 
1. At the admin# prompt enter: 
reboot 
A confirmation message is displayed: 
Device will reboot. Are you sure? [yes/no] 
2. Enter yes to confirm the reset. 
The unit restarts. 
 
Note 
• 
If you perform admin reboot while the save command is being processed, 
reboot is blocked until save completes. 
• 
In case the saving process takes too much time or has complications, you 
can perform force-reboot from the admin prompt. 

## 7.10 Tech-Support Commands  *(p.1272)*

ETX-2i Devices 
7. Administration 
Resetting the x86 (Rangeley or Xeon D) Card 
When restarting the ETX-2i or ETX-2i-B unit with x86 card using admin reboot, the x86 (Rangeley) card 
on ETX-2i-B also restarts; however, the x86 (Xeon D card) on ETX-2i does not reset.  
This section describes how to reset the x86 card (Rangeley or Xeon D), without rebooting the device. 
 
Note 
You can reset the x86 (Rangeley and Xeon D) cards from the x86 screen only 
(chassis ve-module).  
 To reset the x86 Rangeley and Xeon D cards: 
1. Navigate to configure chassis ve-module. 
The config>chassis>ve-module# prompt is displayed. 
2. Enter: 
reset 
If the x86 card (Rangeley or Xeon D) is up and running, it resets. 
7.10 Tech-Support Commands 
ETX‑2i supports a show tech-support command, which you can use to display on the terminal a 
predefined series of CLI commands, such as general device status and statistics, and if specified, store in 
a script file.  
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. 
 
 
ETX-2i Devices 
7. Administration 
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
show configure flows summary details 
• 
show configure oam cfm summary  
• 
show configure pwe summary 
• 
show configure system clock domain1 status 
• 
show configure protection erp-summary   
• 
show configure router 1 arp-table 
• 
show configure router 1 routing-table 
• 
show configure management users-details 
• 
show configure reporting active-alarms 
 
 
ETX-2i Devices 
7. Administration 
Functional Description 
When the tech-support command is invoked, its output is displayed on your terminal, and if specified, 
stored in a script file called script-result, which can afterwards be displayed or downloaded. 
For each command, the following is displayed: 
• 
A timestamp – formatted <date> <time> UTC {+|-} <hours>:<minutes>; for example: 2015-05-35 
11:10:09 UTC +02:00 
• 
The executed command 
• 
The command output, including errors and other messages, provided that the command was 
invoked with the terminal argument. If the file argument is invoked, the command output is 
stored in a file instead of being displayed on the CLI terminal. 
Unlike other commands, the output is sent to the screen continuously, without pausing after each page. 
The CLI prompt does not return until all commands included in the script are executed, or you stop the 
execution. 
The terminal inactivity timer does not decrease while the script is being executed, so the terminal 
remains open even if it takes a long time. 
The script-result file is automatically cleared each time the show tech-support command is invoked.  
Showing the Tech-Support Commands 
 To show the tech support commands: 
1. Navigate to configure system. 
2. At the config>system# prompt, enter show tech-support [file | terminal]. 
The commands and their output are displayed. 