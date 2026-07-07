# 3 Operation and Maintenance

*Manual `SecFlow-1p_6.4_Mn_05-26_GA.pdf`, pages 101–138.*


## 3.1 Turning On the Unit  *(p.101)*


## 3.2 Indicators  *(p.101)*

3.1 Turning On the Unit  
When turning on SecFlow-1p, it is useful to monitor the power-up sequence. 
 
Caution 
SecFlow-1p does not have a power on/off switch, and will start operating as 
soon as power is applied. 
 To turn on SecFlow-1p: 
1. Connect SecFlow-1p to power (see detailed instructions in Connecting to Power). The PWR and 
RUN indicators light up and remain lit as long as SecFlow-1p is powered. The PWR indicator 
lights up immediately upon turning on, while the RUN indicator lights up in about two minutes. 
2. After startup ends, you may log in, using the supervision terminal. 
3.2 Indicators  
  
The SecFlow-1p unit’s LED indicators are located on the device’s front panel. These LEDs enable the user 
to quickly observe the state of the device. Each LED has a default “normal” functionality. 
Note 
Depending on the ordering option, some LEDs may not exist. 
The following tables summarize the normal functions of the SecFlow-1p LED indicators per device.  
 
3. Operation and Maintenance 
 
SecFlow-1p Front Panel 
 
 
LED Indicators 
Name 
LED Color 
Function 
ALM  
Green/Red 
Red on: The device has at least one active alarm 
Green blinking: The device is under test 
Note: Only tests that stop port traffic (such as Ethernet port loopback), 
affect the ALM LED. 
RUN 
Green 
On: Normal operation, system is up 
Off: No power or at early boot stage 
• Fast blinking: Linux loading 
Blinking: During Zero Touch procedure, see also the Zero Touch table 
below. 
3. Operation and Maintenance 
Name 
LED Color 
Function 
AUX 
Green/Red 
Red blinking: ZTP is in process 
Green on: Device has a running container 
Green blinking: Reboot without ZTP is in process 
PWR  
Green 
On – Power is on 
Off – Power is off 
LINK/ACT 1 to 6 
Green 
On – Link is synchronized 
Blinking – Data is being transmitted or received on the link 
SIM1, SIM2 
Green 
Single LTE modem platform:  
• On – SIM card is enabled and inserted 
• Off – no SIM card in the slot or SIM card is disabled 
• Blinking –  SIM card is connected to mobile network 
Dual LTE modem platform (SIM1 and SIM2 are acting as LTE modem 1 
and modem 2 LEDs):  
• On – SIM card is enabled and inserted 
• Off – no SIM card in the slot or SIM card is disabled 
• Blinking –  SIM card is connected to mobile network 
LTE 
Green 
Presents RSSI indication, as follows: 
• Four LEDs ON – Excellent signal; RSSI [dBm}: S > -60 
• Three lower LEDs ON – Good signal; RSSI [dBm}: -60 > S > -75 
• Two lower LEDs ON – Fair signal; RSSI [dBm}: -75 > S > -85 
• One lower LED ON – Poor signal; RSSI [dBm}: -85 > S > -105 
• All LEDs OFF – No signal; RSSI [dBm}:  S < -105 
Notes:  
• RSSI value and LEDs are updated every five seconds. 
• LEDs indicate status according to maximal value between two 
antennas. For example, if one antenna RSSI is -90 dBm and the 
second is -70 dBm, this means that the signal strength is good and 
the three lower LEDs should be on. 
• In the dual-LTE modem platform, the RSSI indication is presented 
for the modem in slot 1 only 
• In the dual-LTE modem platform, SIM1 and SIM2 are acting as LTE 
modem 1 and modem 2 LEDs 
WiFI 
Green 
On: WiFi physical link is up 
Blinking: WiFi passes data 
Note:  Wi-Fi LED indicator is working only on devices with WiFi 
functionality (“WF” ordering options) 

## 3.3 FD Button  *(p.104)*

3. Operation and Maintenance 
Name 
LED Color 
Function 
Serial S1-S2 
TX/RX LED 
Green  
TX blinking – Port is transmitting data 
RX blinking – Port is receiving data 
 
The stages of Zero Touch procedure are displayed by the RUN and ALM LEDs as in the table below. In 
addition to the LEDs, the particular ZTP operation is displayed by corresponding messages in the CLI. 
Zero Touch Status – RUN LED 
RUN LED - Green 
Status 
Blinking: one long, then three short and fast 
Bootstrapping phase of Zero Touch is performed 
Blinking: one long, then one short and fast 
Bootstrapping is in progress: connecting to bootstrap server, 
downloading configuration, downloading software, rebooting 
Blinking: long 
Call-home phase of Zero Touch is performed 
On 
Zero Touch procedure is completed successfully 
ALM LED is blinking at the same rate as RUN to 
indicate the current Zero Touch stage 
Zero Touch procedure error 
3.3 FD Button  
 
You can restore the device to Default configuration using the Factory Default Button present on the 
bottom panel.  
 
 

## 3.4 Startup  *(p.105)*

3. Operation and Maintenance 
 To restore the device to Factory Default configuration:  
1. Insert a pin into the opening marked FD and hold it pressed for 5 seconds (or more).  
2. Wait for the ping reply to default IP 169.254.1.1 via Port 6.  
3. Then you can open a SSH session to the device. 
 
 
3.4 Startup  
Applicability and Scaling 
All configuration and software files, as well as the loading sequence, are applicable to all SecFlow-1p 
versions. 
Configuration and Software Files 
SecFlow-1p supports the following files:  
• 
Software (two software packs: sw-pack-1, 2). The software files are named according to the 
current version, for example Syncope-v6.4.0.5002.iso, where 6.4.0.5 is the version number. The 
file Syncope-v6.4.0.5002.iso is the SecFlow-1p image used for installation onto a disk on key. 
• 
Configuration – running-config, rollback-config, startup-config, user-default-config, factory-
default-config, restore-point-config 
• 
Zero touch configuration – zero-touch-config-xml 
• 
DB schema – db-schema 
• 
DB configuration – db-config 
• 
Scheduler log – schedule-log 
• 
Alarm and event logs – log, brief-log 
• 
Performance management data – pm-0 
3. Operation and Maintenance 
• 
User files – You can store files under any name, for any purpose (e.g. configuration or log 
backup) in the user directory. 
• 
Syslog accounting local log – accounting-log 
Refer to File Operations in the Administration chapter for details on file operations. 
Software Files 
At any time, SecFlow-1p has at least one and possibly two software packs, named sw-pack-1 and 
sw-pack-2. Only one of these software packs is installed and active. 
Configuration Files 
SecFlow-1p supports the following configuration files, containing configuration settings: 
• 
factory-default-config – contains the manufacturer default settings. At startup, 
factory-default-config is loaded if startup-config, rollback-config, and user-default-config are 
missing or invalid. 
• 
rollback-config – serves as a backup for startup-config. At startup, rollback-config is loaded if it 
exists and is valid, and if startup-config is missing or invalid. 
• 
restore-point-config – created by SecFlow-1p when software is installed with restore point 
option.  
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
startup-config and rollback-config, are missing or invalid.  
 
Note 
Configuration files should contain only printable ASCII characters (0x20–0x7E), 
<Enter> (0x0D), <Line Feed> (0x0A), and <Tab> (0x09).  

## 3.5 Upgrading the Software  *(p.107)*

3. Operation and Maintenance 
Loading Sequence 
At startup, the device attempts to load configuration files in the following sequence until a valid one is 
found: 
• 
startup-config 
• 
rollback-config 
• 
user-default-config 
• 
factory-default-config 
If an error is encountered while loading a file, the default is to ignore the error and continue loading. 
You can use the on-configuration-error command to change this behavior, to either stop loading the file 
when the first error is encountered, or reject the file and reboot; after rebooting, the next file in the 
loading sequence is loaded). 
To display the parameter values after startup, use the info [detail] command. 
3.5 Upgrading the Software  
This section explains how to upgrade SecFlow-1p for software version 6.x.x. 
Software upgrade is required to fix product limitations, enable new features, or make the unit 
compatible with other devices that are already running the new software version. 
The device can store up to two software images, referred to as software packs. It is recommended to 
name these software packs sw-pack-1 and sw-pack-2. You can designate any of the software packs as 
active.  
SecFlow-1p also supports partial software updates. Partial software updates include “update” in the 
software image name. They should be downloaded to the device as sw-update-1 and sw-update-2 and 
installed. Each update includes patches and contains all the previous updates of the same baseline 
software. During installation, the device installs all the updates that are not already installed. Software 
update files and are usually delivered as small size files for saving installation time and bandwidth.  
Each software pack is protected by a digital signature, signed by a dedicated RAD CA (Certification 
Authorization). The signature verifies the following: 
• 
This is SecFlow-1p software  
• 
This software was created by RAD 
3. Operation and Maintenance 
• 
The software was not changed 
Any unsigned software pack will be rejected. This security mechanism prohibits the unauthorized 
software to be installed.  
The information in this chapter includes the following: 
• 
Software packs that can be loaded into each device 
• 
Detailed conditions required for the upgrade 
• 
Any impact the upgrade may have on the system 
• 
Description of downloading options 
Application software can be downloaded to SecFlow-1p using the copy command via FTP, FTPS, SFTP, or 
SCP.  
You can install the downloaded device software pack as the active software via the admin software 
install sw-pack-n command, admin software install sw-update-n command. 
 
Note 
Software upgrade relates to upgrading from the product’s previous version to 
current version. To upgrade from an older version, you may not be able to 
upgrade directly to the latest version, but may be required to upgrade one 
version at a time. Refer to the relevant User Manual for upgrade instructions.   
Compatibility Requirements 
The following software releases can be upgraded to Ver. 5.x.x: Ver. 5.x.x.  
Impact 
During the software upgrade process, service is disrupted. 
Prerequisites 
SFTP/FTP/TFTP Prerequisites  
Prior to upgrading via SFTP/FTP/TFTP, verify that you have the following: 
3. Operation and Maintenance 
• 
Operational SecFlow-1p unit with valid IP parameters configured  
• 
Connection to a PC with an SFTP/FTP/TFTP server application and a valid IP address 
• 
Software image file stored on the PC. The image file (and exact name) can be obtained from the 
local RAD business partner from whom the device was purchased. 
Software Packs 
SecFlow-1p software download options include two sw-packs and two sw-updates from the available 
options listed in the following table.  
Device 
File Name 
Description 
SecFlow-1p  
sw-pack-x.x.x.xx.tar.gz 
sw-update-x.x.x.xx.tar.gz 
sw-pack filename 
sw-update filename 
 
Upgrading Software  
 
The recommended software downloading method (both for CLI and Web GUI) is to use the copy 
command. 
Network administrators can use this procedure to distribute new software releases to all the managed 
SecFlow-1p units in the network from a central location. 
Use the following procedure to download software release 6.x.x to SecFlow-1p: 
1. Verify that the image file is stored on the PC with the SFTP/TFTP server application. 
2. Verify that the SecFlow-1p router has been configured with valid IP parameters. 
3. Ping the PC to verify the connection. 
4. Activate the SFTP/TFTP server application. 
5. Download the image file from the PC to SecFlow-1p. 
6. Install the image as the active software. 
 
Note 
Configuration values shown in this chapter are examples only.  
3. Operation and Maintenance 
Verifying the Host Parameters 
In order to be able to establish communication with the SFTP/TFTP server, the SecFlow-1p router must 
have IP parameters configured according to your network requirements. Refer to the following manual 
sections for additional information: 
• 
Connecting to a Management Console in the Installation and Setup chapter  
• 
Working with SSH in the Configuration and Management chapter  
• 
Router in the Traffic Processing chapter 
Pinging the PC 
Check the integrity of the communication link between SecFlow-1p and the PC by pinging the PC from 
SecFlow-1p.  
 To ping the PC: 
1. In any level, start pinging the PC specifying its IP address and optionally the number of packets 
to send: 
ping <ip-address> [number-of-packets <num-packets>][payload-size <bytes>] 
Where 
num-packets can be 1-10,000 or 0 (forever) for a continuous ping. Default is 5. 
bytes can be 32-1450.  
A reply from the PC indicates a proper communication link. 
2. If the ping request times out, check the link between SecFlow-1p and the PC (physical path, 
configuration parameters, etc.).  
3. Note: in the current version, ping is available via CLI only. 
Activating the SFTP Server 
Once the SFTP server is activated on the PC, it waits for any SFTP file transfer request originating from 
the product and carries out the received request automatically.  
SFTP file transfers are carried out through TCP port 22. Make sure that the firewall you are using on the 
server allows communication through this port (refer to the Administration chapter for details).  
In the Web GUI, this is done via the screen below. 
3. Operation and Maintenance 
 
Activating the TFTP Server  
Once the TFTP server is activated on the PC, it waits for any TFTP file transfer request originating from 
the product and carries out the received request automatically.  
TFTP file transfers are carried out through port 69. Make sure that the firewall you are using on the 
server allows communication through this port.  
Note 
Configure the connection timeout of the TFTP server to be more than 
30 seconds to prevent an automatic disconnection during the backup partition 
deletion (about 25 seconds).  
Downloading the New Device Software Release File 
This procedure is used to download a new SecFlow-1p software version. 
 To copy the image file to the SecFlow-1p unit via CLI: 
• 
In any level, enter: 
copy sftp://<username>:<password>@<ip-address>/<image-file-name> {<sw-pack-n> | 
<sw-update-n>} 
Where <ip-address> is the IP address of the PC where the SFTP server is installed and <n> is the 
index of the software pack/update. 
3. Operation and Maintenance 
Or 
copy tftp://<tftp-ip-address>/<image-file-name> <sw-pack-n>  
Where tftp-ip-address is the IP address of the PC where the TFTP server is installed and <n> is 
the index of the software pack. 
 To copy the image file to the SecFlow-1p unit via Web GUI: 
1. Navigate to Home>File. 
2. In the Source File field, enter: 
copy sftp://<username>:<password>@<ip-address> 
where <ip-address> is the IP address of the PC where the SFTP server is installed  
Or 
copy tftp://<tftp-ip-address> 
where tftp-ip-address is the IP address of the PC where the TFTP server is installed  
3. In the Destination File field, enter: 
<image-file-name> {<sw-pack-n> | <sw-update-n>}  
where <n> is the index of the software pack/update. 
 
 
 
3. Operation and Maintenance 
Notes 
Choose an index that is not being used by the active software, or by a 
software pack that you do not want to overwrite.  
Update packs are available for SFTP only. 
4. Click Submit. 
The software download is performed. See Activating the Device Software for instructions on 
installing the downloaded software as the active software.  
Activating the Device Software  
After software is downloaded to SecFlow-1p, it has to be installed via the install command as the active 
software. When you install software, by default SecFlow-1p creates a restore point, so that if there is a 
problem with the new software pack, you can perform a rollback to the previous software pack and 
startup-config file. This ensures that if you changed the startup-config file before noticing that 
something was wrong with the newly installed software, you can restore the startup-config that was 
running before the last installation. 
Note 
The file startup-config must exist before you can install software with creation 
of a restore point.  
Prior to installing the software, you can request (via command software-confirm-required) that the user 
confirm the next installed software (via command software-confirm) following the next SecFlow-1p 
reboot. This software confirmation command verifies that the user has regained connection to the 
device following installation. If confirmation is requested, but the user does not confirm the software 
(via command software-confirm) within the configured timeout period, SecFlow-1p automatically falls 
back to its previous software. This precaution prevents a permanent loss of connection to the remote 
device following installation.  
 To request software confirmation: 
• 
At the admin>software# prompt, enter: 
software-confirm-required [time-to-confirm <minutes>] 
The confirmation timeout can be from five minutes to 24 hours. If you do not specify it, the 
default is five minutes. 
Note 
You can cancel the software confirmation request by entering 
no software-confirm-required.  
Next time SecFlow-1p reboots and loads new software, it starts a confirmation timer. See the 
following procedure for more details on the confirmation. 
3. Operation and Maintenance 
 To install a device software pack as active: 
Note 
• 
If startup-config does not exist, you must install the software pack 
without creating a restore point. 
• 
As a defective startup-config can cause a loss of connection, it is not 
recommended to install software and change startup-config at the same 
time. However, if you must do both at the same time, first install the 
software and only after verifying it, make the needed configuration 
changes (or vice versa).  
1. At the admin>software# prompt, enter: 
install {sw-pack-1|sw-pack-2|sw-update-1|sw-update-2} [no-restore-point] 
Where n is 1 or 2, provided sw-pack-n is a non-active software pack. If you specify 
no-restore-point, then after the software is installed, it is not possible to roll back to the 
previous software.  
You are prompted to confirm the operation. 
!Device will install file and reboot. Are you sure? [yes/no] _  
2. Type yes to confirm. 
If a restore point is being created, then startup-config is copied to restore-point-config. 
SecFlow-1p designates the specified software pack as active, then reboots. If a software 
confirmation request is active, SecFlow-1p starts a timer with the specified timeout period. 
Note 
While the confirmation timer is running, SecFlow-1p does not allow any 
commands that change its configuration.  
3. If the software-confirm command is entered before the timer expires, the software is 
considered to be confirmed. 
If the software-confirm command is not entered before the timer expires, then restore-point-config is 
deleted, SecFlow-1p designates the previously active software pack as active, then reboots. 
Note 
If the software pack is activated on SecFlow-1p, the device reboots.  
Activating the Software  
To activate a software pack, you need to designate it as active and load it. 
 To activate a software pack: 
1. To set the software as active, enter: 
set-active <index>. 

## 3.6 Working with Custom Configuration Files  *(p.115)*

3. Operation and Maintenance 
A confirmation similar to the following is displayed: 
SW set active 2 completed successfully. 
2. To load the active software, type: run. 
A sequence of messages similar to the following is displayed: 
Loading/un-compressing sw-pack-2... 
Starting the APPLICATION off address 0x10000... 
After a few more seconds, the login prompt is displayed. 
 
3.6 Working with Custom Configuration Files  
In large deployments, often a central network administrator sends configuration files to the remote 
locations and all that remains for the local technician to do is replace the IP address in the file or other 
similar minor changes, and then download the file to the device. Alternatively, the technician can 
download the file as is to the device, log in to the device and make the required changes, and then save 
the configuration. 
To download the configuration file, use the global copy command (refer to the Administration chapter). 
After downloading the configuration file, the unit must be reset in order to execute the file. After the 
unit completes its startup, the custom configuration is complete. 
To ease deployment of large numbers of devices, you can automatically distribute software and 
configuration files in the following ways:  
• 
Use On-Net Zero Touch provisioning (ZTP) to enable units to automatically receive an IP address, 
and software and configuration files (see On-Net Zero Touch for details). 
• 
Use PPPoE (Point-to-Point Protocol over Ethernet) to establish a management channel through 
which an IP address can be acquired (refer to Point-to-Point Protocol over Ethernet (PPPoE) in 
the Management and Security chapter, for details). For instance, the IP address can be acquired 
from a broadband remote access server (BRAS). The BRAS then notifies a Radius server, which in 
turn reports to a management system, such as RADview, that a new device is up. The 
management system then sends software and configuration files to the device. 
Applicability and Scaling 
Zero Touch is applicable to all the SecFlow-1p versions.  
3. Operation and Maintenance 
Factory Defaults 
Off-Net Zero Touch via bootstrap server is by default disabled (no ztc-bootstrap). 
Saving Configuration Changes 
You must save your configuration if you wish to have it available, as it is not saved automatically. 
You can save your configuration as follows: 
• 
Use the save command to save running-config as startup-config. 
• 
Use the copy command to copy running-config to startup-config or user-default-config. 
Additionally, some commands erase the configuration saved in startup-config by copying another file to 
it and then resetting the device. The figure below indicates the commands that copy to startup-config, 
and whether the device resets after copying. 
 
 To save the user configuration in startup-config: 
1. Enter: save 
2. At any level, enter: copy running-config startup-config 
 To save the user default configuration in user-default-config:  
• 
At any level, enter: copy running-config user-default-config. 
 
3. Operation and Maintenance 
Confirming the Startup Configuration File 
SecFlow-1p supports the enabling of active confirmation of the startup-config file following reboot. 
Confirmation of startup-config prevents loss of the management link to a remote device due to 
erroneous configuration. 
If you enable the startup-confirm-required request, the next time the device reboots, you must enter 
the global command startup-config-confirm in order to confirm startup-config within the configured 
timeout period. (This command is only relevant if you run startup-confirm-required and then reboot the 
device; otherwise, it is masked.) 
If you confirm the new startup-config within the configured timeout period, SecFlow-1p loads startup-
config and copies running-config or any other user-specified configuration file to rollback-config.  
If you do not succeed to confirm the new startup-config before timeout, the device rejects 
startup-config, reboots, and attempts to load the next available configuration file (rollback-config, 
user-default-config, factory-default-config). 
 To enable startup-config confirmation following reboot; 
• 
At the admin# prompt enter: 
startup-confirm-required [time-to-confirm <minutes>] [rollback {startup-config | 
user-default-config | factory-default-config | running-config}] 
The <minutes> parameter defines the confirmation timeout, range 1–65535 (default 5). If 
rollback <config-file> is specified, the specified configuration file is copied to rollback-config.  
For example, entering rollback user-default-config copies user-default-config to rollback-config. 
 
Note 
If rollback is not specified and rollback-config is invalid or does not exist, the 
device copies running-config to rollback-config upon execution of 
startup-confirm-required.  
On-Net Zero Touch  
The on-net Zero Touch feature allows SecFlow-1p to receive software and configuration files 
automatically, when SecFlow-1p is located in the same network, eliminating the need to manually log 
into SecFlow-1p in order to transfer the required files to it.  
The following zero touch mechanisms enable automatic provisioning of SecFlow-1p: 
• 
Zero Touch via DHCP – SecFlow-1p retrieves configuration information from the DHCPv4 server 
(see Zero Touch via DHCP/DHCPv6). 
3. Operation and Maintenance 
• 
Zero Touch via DHCPv6 – SecFlow-1p retrieves configuration information from the DHCPv6 
server (see Zero Touch via DHCP/DHCPv6). 
• 
Zero Touch via trap – SecFlow-1p sends a notification trap to the management system (see Zero 
Touch via Trap), so that the management system can perform the appropriate provisioning. 
Zero Touch via DHCP/DHCPv6 
This section describes Zero Touch provisioning via DHCP (for IPv4) or DHCPv6 for (DHCPv6).  
Prerequisites  
• 
A Zero Touch Configuration (ZTC) XML file, containing directives regarding downloading and 
installation of software and configuration files. See ZTC File Structure for details on how to 
prepare this file. 
• 
A DHCPv4/DHCPv6 server for providing the TFTP server address, in addition to the usual IP 
address, default gateway, etc. 
• 
A TFTP server from which to download the following: 
 
ZTC file  
 
Software image file, if required by the directives 
 
Configuration file, if required by the directives 
Sequence  
1. Select the port you to want to use for ZTP and set it to “no shutdown”. 
2. Define the router interface and bind it to the selected port. 
3. Configure the DHCPv4 (or DHCPv6) client and set the router interface to “no shutdown”. 
4. Save the configuration. 
5. SecFlow-1p obtains a DHCPv4 lease from the DHCPv4 server and/or a DHCPv6 lease from the 
DHCPv6 server. If SecFlow-1p receives more than one lease that contains ZTC directives (from 
multiple interfaces), it processes them one by one. After the first one is finished, either 
successfully or not (e.g. reaching a timeout during file download), the device proceeds with the 
directives received in the second lease. 
6. For DHCP: The lease provides the device IP address (for device management), TFTP server IP 
address, either via option 150, or as a string via option 66 (the string is interpreted as an IP 
address rather than a device name). Option 66 is valid only if the string is formatted as 
(‘xxx.xxx.xxx.xxx’). Optionally, the DHCP lease provides the path and/or the file name of the ZTP 
file via DHCP option 67. 
3. Operation and Maintenance 
7. For DHCPv6: The lease provides the device IP address (for device management), TFTP server 
address via CableLabs vendor-specific (17) sub-option 32, provided that SecFlow-1p supports it. 
If multiple TFTP server addresses are received, only the first one is used. Optionally, the DHCPv6 
lease provides the path and/or the file name of the ZTP file via DHCPv6 sub-option 33. 
8. If a valid file name is not obtained, SecFlow-1p tries to download the file considering the option 
67 as a path, and the default file name rad.xml is added to it. If this attempt fails as well, the 
third time SecFlow-1p uses the path rad/ with the file name rad.xml.  
9. If the last attempt fails, the ZTC process finishes unsuccessfully and SecFlow-1p sends the event 
download_end with error indication. 
10. If the ZTC file is loaded successfully, SecFlow-1p sends the event download_end (with success 
indication) to any configured network managers, and saves the ZTC file as 
zero-touch-config-xml. 
11. If zero-touch-config-xml contains directives for a software file, SecFlow-1p does one of the 
following, according to the action specified in the directives: 
 
upgrade-only – Load software file if it is newer than the active software image. 
 
downgrade-only – Load software file if it is older than the active software image. 
 
replace – Load software file if different from the active software image. 
12. If zero-touch-config-xml contains directives for a configuration file, then if the action specified 
in the directives is replace-cfg, SecFlow-1p loads the specified configuration file if it is different 
than the last configuration file loaded via the ZTC mechanism, and saves it as specified by 
startup-config. 
13. If a software file was downloaded, SecFlow-1p installs it as the active software pack. 
14. If a software file and/or configuration file was downloaded, SecFlow-1p reboots. After startup, 
the normal startup loading sequence is performed, so that if startup-config is loaded in the 
sequence, SecFlow-1p executes the CLI commands in the file. 
If the ZTC process ends successfully, SecFlow-1p sends the event download_end (with success 
indication) to any configured network managers. 
If an error occurs in the ZTC process, SecFlow-1p does the following: 
• 
Sends the event download_end (with failed indication) to any configured network managers 
• 
Starts a timer lasting about 2-4 minutes 
• 
When the timer expires, SecFlow-1p again attempts the ZTC process. 
3. Operation and Maintenance 
ZTC File Structure 
This section describes the ZTC directives in the ZTC file, which is written in standard XML, based on the 
NETCONF schema. The file can contain directives for one or more devices. This flexibility enables the use 
of one ZTC file per device, or one ZTC file for all devices. ZTC File Example shows a ZTC file containing 
directives for SecFlow-1p.  
The directives are enclosed in the element pair <zero-touch-configuration> 
</zero-touch-configuration>. The ZTC directives for a particular device are enclosed by an element pair. 
The element contents are according to the chassis name in the inventory display (refer to Resetting to 
Default). The file can contain software-related directives and/or configuration-related directives for 
each device. 
The following software directives supply information about the software file to download: 
• 
sw-version – version of the software to download; must be formatted in the same way as the 
chassis software revision displayed in the inventory display (refer to Inventory). 
• 
sw-action – software installation to perform: 
 
upgrade-only – Load software file if sw-version specifies a newer version than the chassis 
software revision. 
 
downgrade-only – Load software file if sw-version specifies an older version than the 
chassis software revision. 
 
replace – Load software file if sw-version specifies a version that is different from the 
chassis software revision. 
• 
sw-src-file – path and name of the software to download 
• 
sw-dst-file – file name for saving the downloaded software: 
 
sw-pack-<n> – File is saved as the specified name, if it is not the active software. 
 
auto – File is saved as follows: 
 
If there is an unused software pack number, and there is enough space in the file 
system, then the file is saved as sw-pack-<n>, where <n>is the smallest unused software 
pack number. 
 
If all software packs numbers are in use, or if there is not enough space to save the 
software, then the file is saved as sw-pack-<n>, where <n>is the software pack number 
of the oldest version. 
The following configuration directives supply information about the configuration file to download: 
• 
cfg-version – version of configuration to download  
• 
cfg-action – action to take regarding configuration: 
3. Operation and Maintenance 
 
replace-cfg – Load configuration file if cfg-version is different than the last ZTC configuration 
version. 
• 
cfg-src-file – path and name of the configuration file to download 
• 
cfg-dst-file – specifies the name under which to save the downloaded configuration file; must 
contain startup-config 
ZTC File Examples  
In this example, the software pack is to be chosen automatically (auto). 
<rpc message-id="1" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> 
<edit-config> 
<target> 
<running/> 
</target> 
 
<config> 
<zero-touch-configuration xmlns="http://www.rad.com/schema/zero-touch-
configuration/1.0"> 
<SF-1p> 
<sw-version>5.0.0(0.05)</sw-version>  
<sw-action>replace</sw-action> 
<sw-src-file>sw-pack_test.bin</sw-src-file> 
<sw-dst-file>auto</sw-dst-file> 
<cfg-version>pcpe_2.2</cfg-version> 
<cfg-action>replace-cfg</cfg-action> 
<cfg-src-file>cfg_file.txt</cfg-src-file> 
<cfg-dst-file>startup-config</cfg-dst-file> 
</SF-1p> 
 
</zero-touch-configuration> 
</config> 
</edit-config> 
</rpc> 
 
In this example, the software pack is entered manually (sw-pack-2). 
<rpc message-id="1" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> 
<edit-config> 
<target> 
<running/> 
</target> 
 
<config> 
<zero-touch-configuration xmlns="http://www.rad.com/schema/zero-touch-
configuration/1.0"> 
 
<SF-1p> 
<sw-version>5.0.0(0.05)</sw-version> 
<sw-action>replace</sw-action> 
3. Operation and Maintenance 
<sw-src-file>sw-pack_test.bin</sw-src-file> 
<sw-dst-file>sw-pack-2</sw-dst-file> 
<cfg-version>rados_2</cfg-version> 
<cfg-action>replace-cfg</cfg-action> 
<cfg-src-file>cfg_file.txt</cfg-src-file> 
<cfg-dst-file>startup-config</cfg-dst-file> 
</SF-1p>  
 
</zero-touch-configuration> 
</config> 
</edit-config> 
</rpc> 
Zero Touch via Trap 
SecFlow-1p supports a bootstrap trap.  
If a management station address is configured (typically in user-config), you can specify that SecFlow-1p 
send a trap periodically to the management station (usually RADview) to notify it of its existence in the 
network (by default, this trap is not sent).  
 To enable sending the trap: 
1. Navigate to configure management snmp. 
The config>mngmnt>snmp# prompt is displayed. 
2. Configure target and target-params (Refer to Configuring SNMPv3 Parameters for more 
information). 
3. Enter: 
bootstrap-notification 
SecFlow-1p sends the systemBootstrap trap every 120–240 seconds, until the command 
no bootstrap-notification is entered, or the management station acknowledges the trap. If 
SecFlow-1p reboots before the trap is acknowledged, it resumes sending the trap after it 
completes its startup. 
Off-Net Zero Touch 
This section describes Zero Touch provisioning with bootstrap server over public network. 
During off-net Zero Touch process, SecFlow-1p retrieves an Artifact file containing bootstrapping data 
from the bootstrap server to establish a secured connection with NOC. 

## 3.7 Information elements essential for Zero Touch procedure (se  *(p.123)*

3. Operation and Maintenance 
Prerequisites 
3.7 Information elements essential for Zero Touch procedure 
(see MQTT Server  
This section describes how to configure MQTT servers. 
Applicability and Scaling 
This feature is applicable to all SecFlow-1p devices.   
Up to two MQTT servers can be configured. 
Benefits 
This feature facilitates efficient and reliable communication 
between devices for use in constrained environments and low-
bandwidth networks, enabling devices to send and receive data 
with minimal network overhead. 
Functional Description 
MQTT, which stands for Message Queuing Telemetry Transport, 
is a lightweight messaging protocol designed for use in 
constrained environments and low-bandwidth networks. It 
employs a publish/subscribe model, facilitating efficient and 
3. Operation and Maintenance 
reliable communication between devices. MQTT is commonly 
used in IoT (Internet of Things) applications, enabling devices to 
send and receive data with minimal network overhead. 
MQTTS is the secured version of this protocol. 
You can open a device management channel over MQTT with 
the server of this level. When enabled, the device can be 
managed over MQTT by the server. Only one server can serve 
as a management channel. 
When configuring the MQTTS protocol, an X.509 certificate 
name (1-64 characters) must be provided. The certificate 
should be a device certificate, signed by a CA. It is the 
responsibility of the user to make sure that the certificate exists 
and is valid.  
By configuring a certificate, MQTTS mode is implied. If no 
certificate is configured the device works with MQTT. 
The MQTTS implementation only accepts peers’ certificates 
signed by a CA that was preconfigured as trusted. Therefore, 
you must provide the trusted CA name (1-20 characters). 
Note: MQTTS needs a valid device certificate, the certificate (or 
chain of trust) of the CA that signed its certificate and that of 
the CA that signed the peer’s certificate (if it is not the same 
CA).  
3. Operation and Maintenance 
You can also configure the user credentials for MQTT 
authentication (a username and password, both can be 1-64 
characters, not configured by default). This can be done 
exclusively or in addition to an X.509 certificate (depending on 
whether the certificate command is configured).  
Factory Defaults 
By default, no MQTT server is defined. When an MQTT server is 
first defined, it is configured as shown below. 
Parameter 
Default Value 
protocol  
ssl 
port 
1883 
username 
no user 
certificate-name  
no certificate 
ca-name 
Trusted CA is not 
configured 
management-channel 
no management-
channel  
 
3. Operation and Maintenance 
Configuring MQTT Server 
You can configure the MQTT server as follows. 
To configure the MQTT Server: 
1. Navigate to config>system>mqtt#. 
1. Define the server config>system>mqtt>server<server-
name, 1..32 characters>#. You can configure up to two 
servers in the device. 
2. At the config>system>mqtt>server <server-name> # 
prompt, perform the required tasks according to the 
following table.  
3. Operation and Maintenance 
Task 
Command 
Comments 
Configuring the 
server IP 
parameters 
address ip <ip-
address> [protocol 
{ssl|tcp}] [port 
<port-number>] 
address url <url-
string> [protocol 
{ssl|tcp}] [port 
<port-number>] 
no address 
<ip-address> – valid 
IPv4 or IPv6 unicast 
address 
<url-string> - a valid 
URL (to be resolved 
with DNS). 
protocol – MQTT 
transport protocol 
(ssl or tcp) 
port – MQTT 
transport port 
(1..65535) 
Configuring the 
X.509 certificate 
for MQTTS 
authentication 
certificate 
<certificate-name> 
trusted-ca <ca-
name> 
no certificate 
<certificate-name> 
MQTTS certificate 
<certificate-name> –  
string, 1-64 
characters) 
<ca-name>– MQTTS 
trusted CA, string, 1-
20 characters 
3. Operation and Maintenance 
Task 
Command 
Comments 
Opening a 
management 
channel with the 
server 
management-
channel 
no management-
channel 
 
Configuring user 
credentials for 
authentication 
with the MQTT 
server 
user name 
<username> 
password 
<password-string> 
[hash-2] 
no user 
<username>: 1-64 
characters  
<password-string>: 
1-64 characters 
hash-2 - password is 
hashed (encrypted) 
Displaying the 
server status 
show status  
See Viewing the 
MQTT Status below 
Example  
To define the MQTT server with MQTTS and SSL protocols: 
  
configure system mqtt 
            server "1" 
                address url "lns1.rad.com" protocol ssl port 7883 
                certificate "1p" trusted-ca "CA" 
            exit 
3. Operation and Maintenance 
 configure system mqtt 
            server "2" 
                address url "lns3.rad.com" protocol ssl port 5884 
                certificate "1p" trusted-ca "CA" 
                management-channel 
            exit 
 
Configuration Errors  
The following table lists the messages generated by SecFlow-1p 
when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Maximum numbers 
of servers have 
been reached 
You can configure no 
more than two MQTT 
servers 
 
Maximum number 
of management-
channel servers has 
been reached  
No more than one 
server can serve as a 
management 
channel 
 
3. Operation and Maintenance 
Message 
Cause 
Corrective Action 
Note: No valid self-
certificate with the 
specified name 
 
No valid self-
certificate of the 
specified name exists 
in the device 
Note: The command 
will be accepted, but 
MQTT would fail until 
the user addresses 
the problem 
 
Note: No such CA; 
it must be 
configured for 
MQTTS to work 
This CA does not 
exist 
Note: The command 
will be accepted, but 
MQTT would fail until 
the user addresses 
the problem 
 
3. Operation and Maintenance 
Message 
Cause 
Corrective Action 
Note: Import a 
valid chain of trust 
for the CA, for 
MQTTS to work 
The device does not 
have a valid chain of 
trust for the CA 
Note: The command 
will be accepted, but 
MQTT would fail until 
the user addresses 
the problem 
 
Viewing the MQTT Status  
This section explains how to display the status of the MQTT 
server. 
To display MQTT status:  
configure>system>mqtt>server()# show status 
Application  
 : LORA 
Server Address/URL   : ibs-lns 
MQTT Status  
 : Connected 
 The status display provides information about: 
• Application served by MQTT connection: 
 Management 
3. Operation and Maintenance 
 LORA (Attached to LoRa gateway) 
 (empty) 
• MQTT server address / URL 
• MQTT module status 
 Not configured – configuration is missing  
 Disconnected – connection fails after ‘Connected’ state 
 Connected – connection process succeeded 
 Connecting – trying to connect before first “Connected” 
state  
• MQTT configuration problem (MQTT cannot start due to 
missing configuration) 
 Undefined MQTT server in LoRa gateway 
 Undefined MQTT address 
 Undefined certificate or user 
 There is no certificate 
• 
Public Key Infrastructure for details on Certificates and X.509):  
 
UUID – Device MAC address  
 
a private key securely stored in the device 
 
X.509 v3 CA Certificate signed by RAD CA 
 
X.509 v3 Device Certificate signed by RAD CA (optionally) 
An additional element is the path to the bootstrap server. 
• 
A bootstrap server that holds the entire bootstrapping data. 
• 
An Artifact file created for the particular device, recognized by its UUID and stored on the 
bootstrap server. The Artifact is a zipped ZT file that can contain all or some of the following 
files: 
3. Operation and Maintenance 
 
bootstrap.cfg –configuration file 
 
config_manager.cer – configuration manager X.509 certificate file 
 
bootstrap.xml – SW pointer XML file 
• 
Configured NTP server (optionally)  
• 
Configured DHCP or DHCPv6 client (optionally) 
Sequence 
3. When SecFlow-1p device is powered on, it either obtains its networking configuration from a 
service-provider controlled DHCP server, or starts ZT process with a static IP if configured so. 
Then it connects to the bootstrap server via a secured connection, according to its 
preconfigured bootstrap server path and based on its preinstalled X.509 certificates. After 
mutual or one-way authentication, the device obtains the pre-prepared Artifact from the 
bootstrap server. In case of one-way authentication, a password should be configured. Upon 
extracting the bootstrapping data, SecFlow-1p acts according to the obtained bootstrapping 
data. 
4. After successful SecFlow-1p bootstrapping (which may include SW upgrade, applying configuration 
and device reboot), SecFlow-1p can open a secure connection to the IPsec/VPN Gateway in the 
NOC.  
5. When a secure connection between SecFlow-1p and the NOC is established, SecFlow-1p may call 
home, i.e. send an enrollment trap to the deployment-specific network manager. When network 
manager receives the device call, it acts according to the corresponding ZT entry, registers the 
device and performs complementary provisioning actions. 
ZT process with TFTP bootstrapping always precedes ZT with bootstrap server, in other words, if both ZT 
processes are enabled, only TFTP bootstrapping is performed. However, if during the ZT process DHCP 
options of TFTP server are not received, TFTP bootstrapping is not performed, while ZT connection to 
the bootstrap server is initiated. 
Exceptional Cases 
If the device fails to connect to the bootstrap server, it stops the ZT procedure and attempts to access 
the bootstrap server in intervals between two to four minutes. 
If the device successfully completed the Artifact downloading, but the Artifact is corrupted, according to 
the following criteria, it stops the ZT procedure: 
• 
The archived .gz file cannot be extracted by the device 
• 
After successful extraction, one of the following files is missing or having an unexpected name: 
3. Operation and Maintenance 
 
configuration file (.cgf) 
 
SW image pointer XML file 
 
RV Configuration manager X.509 certificate 
• 
After successful extraction, the format of one of the following files is corrupt: 
 
 configuration file (.cgf) 
 
SW image pointer XML file 
 
RV Configuration manager X.509 certificate 
If the device successfully completed the Artifact downloading, but software download failed, it stops the 
ZT procedure, terminates all configuration actions (for example, copying received configuration file to 
startup-config) and attempts to access the bootstrap server in intervals between two to four minutes. 
If the device successfully completed the bootstrapping phase, but failed during the call-home phase, it 
stops the ZT procedure, applies user-default-config to startup-config, saves and reboots. The ZT 
procedure is repeated after the reboot. The failure of the call-home is defined according to the following 
criteria: 
• 
The entry in bootstrapServerTable is configured with bootstrapServerRevertiveMode = yes (3)  
• 
ZT with the bootstrap server is not confirmed by manager (bootstrapServerConfirmCmd is not 
set to off (2)) within a timeout of 600 sec. 
Configuring Off-Net Zero Touch 
 To configure ZTC parameters: 
1. Navigate to config>mngmnt>access# prompt.  
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Start Zero Touch 
Configuration process after 
the next reboot 
ztc-after-reboot 
Type no ztc-after-reboot to start 
ZTC immediately. 
Enabling off-net Zero Touch 
Configuration with bootstrap 
server 
ztc-bootstrap [url <url-string>] 
[non-revertive] [password 
<password-string> [hash]] 
Type no ztc-bootstrap to disable 
off-net ZTC with bootstrap server. 
url-string–URL of the bootstrap 
server 
3. Operation and Maintenance 
Task 
Command 
Comments 
non-revertive - SecFlow-1p does 
not wait for confirmation of ZTC 
process by ztc-bootstrap-confirm 
password-string – Bootstrap server 
password 
Confirming successful 
completion of off-line Zero 
Touch 
ztc-bootstrap-confirm 
If ZTC revertive mode is set (by 
omitting non-revertive in ztc-
bootstrap), you need to confirm 
successful completion; otherwise, 
ZTC process will be initiated again 
after rollback. 
Disabling off-net Zero Touch 
TFTP provisioning 
[no] ztc-tftp disable 
 
 
Note 
You have to enable the bootstrapping revertive mode to allow the RADview 
configuration manager to confirm the entire ZT process as a part of call-home 
phase, before device re-initiate the entire ZT process. Nevertheless, this is an 
optional procedure that you may choose not to use.  
Example 
The following is an example of the configuration required for ZTP.  
#===============Define config for ZTP  ==========# 
configure management 
     access 
    ztc-bootstrap no-revertive 
    ztc-tftp-disable 
exit all 
 
 
#===============Define VLAN for Management/Service  ==========# 
configure port 
ethernet 1  
vlan <WAN_VLAN_ID> 
no shutdown 
exit all 
 
 
configure Router 1 
name "Router#1" 
    dhcp-client 
3. Operation and Maintenance 
        duid-type en 
          dhcpv6-option-request vendor-specific-information-17 
    exit 
      interface 1  
                bind ethernet 1 vlan <WAN_VLAN_ID>  
dhcp 
                dhcp-client  
                    client-id mac  
exit 
dhcpv6-client  
        ipv6-autoconfig 
no shutdown 
 
 
Note 
The dhcpv6-option-request vendor-specific-information-17 command in the 
above configuration, requests the DHCP server to provide the address of the 
bootstrap server to SecFlow-1p. 
Verifying Upgrade Results 
You can verify that the upgrade was successful by logging on to SecFlow-1p via a terminal emulation 
program, and in the Inventory table (show summary-inventory at prompt config>system#), checking 
the active software version in the SW Rev column. 
Restoring the Previous Version 
If the installed software malfunctions and was installed with a restore point (restore-point-config must 
exist on device), you can perform rollback to the previous active software. 
 To roll back to the previous active software pack: 
1. At the admin>software# prompt, enter: 
undo-install 
You are prompted to confirm the operation. 
! Falling back to restore point ! Are you sure? [yes/no] _ 
2. Type yes to confirm. 
The file restore-point-config is renamed to startup-config. SecFlow-1p designates the previously 
active software pack as active, then reboots. 

## 3.8 Periodical Maintenance  *(p.137)*

3. Operation and Maintenance 
3.8 Periodical Maintenance 
Caution 
• 
Only qualified, authorized, and skilled service personnel should carry out 
adjustment, maintenance, or repairs to this product. Operators and 
users should not perform installation, adjustment, maintenance, or 
repairs. 
• 
Always observe standard safety precautions during installation, 
operation, and maintenance of this product. Precautions listed in this 
document are supplements to local safety regulations for installation. 
• 
RAD shall be released from all obligations under its warranty in the 
event that the equipment has been subjected to misuse, neglect, 
accident, or improper installation, or if repairs or modifications were 
made by persons other than RAD's own authorized service personnel, 
unless such repairs by others were made with the written consent of 
RAD. 
 
 
 

## 3.9 Turning Off the Unit  *(p.138)*

3. Operation and Maintenance 
When an outdoor device requires servicing, open the external door of the unit using a Phillips 
screwdriver. Opening the door clicks the rails into place, thus securing the door into its open position, so 
that it doesn’t close on its own on windy days. 
When done servicing the device, push the rails upward to release the door, close the door, and then 
secure it closed using a Phillips screwdriver.  
3.9 Turning Off the Unit 
 To power off the unit: 
• 
Remove the power cord from the power source. 