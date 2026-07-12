# 12 Software Upgrade

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 908–928.*


## 12.1 Compatibility Requirements  *(p.908)*

This chapter explains how to upgrade Megaplex-4.  
Software upgrades may be required to fix product limitations, to enable new features, or to make the 
unit compatible with other devices that are already running the new software version. New software 
releases are distributed as *.bin files, to be downloaded to Megaplex-4.  
Megaplex-4 can store four software versions, each in one of the four partitions of its flash memory, 
which also contains a boot program. The software is stored in compressed format.  
Note 
If your system has two CL modules, you must upgrade both modules to the 
same software version to ensure seamless redundancy after the upgrade.  
12.1 Compatibility Requirements 
Following are the CL software releases that can be upgraded to version 4.91 as well as the hardware 
revisions that can accept the software version 4.91: 
• 
Software –Ver. 4.71.xx and above 
• 
CL.2 Hardware – 0.1 and above 
• 
CL.2/A Hardware – 1.0 and above. 
Note 
Upgrading software Ver. 4.71.xx and lower to Ver 4.91 needs a special 
procedure. For more information, contact RADcare Online.  
Sync-E timing is supported with the CL.2/A module assembly (HW rev 1.1 and up).     
Application software can be downloaded to Megaplex-4 via CLI (using TFTP) or via the boot menu (using 
TFTP). The upgrade consists of two stages. 
First the application software is downloaded from a PC to Megaplex-4 flash disk. This can be done in the 
following ways: 
• 
via CLI (using TFTP) using “file>copy” command  

## 12.2 Impact  *(p.909)*


## 12.3 Prerequisites  *(p.909)*

12. Software Upgrade 
• 
via the boot commands (“download”, using TFTP).  
Then the software pack is downloaded from the flash disk to the CL and I/O modules. This can be done 
in the following ways: 
• 
via the CLI “admin>software>install” command (both for CL and I/O modules) 
• 
via the boot “set-active” command (CL modules only).  
12.2 Impact 
Megaplex-4 is upgraded once the unit has been reset. 
12.3 Prerequisites 
This section details the software file names and outlines system requirements needed for the upgrade 
procedure. 
Software Files 
New version releases are distributed as software files named *.bin, for example sw-pack.bin. The files 
can be obtained from the local RAD business partner from whom the device was purchased. 
The software upgrade utility includes four partitions called sw-pack-1, sw-pack-2, sw-pack-3, sw-pack-4 
for downloading and storing the software versions. To activate the specified software version, one of 
these partitions is set to active.  
Each software pack consists of a set of image files for each (CL or I/O) module with appropriate headers. 
The software pack can be ordered either for the entire chassis, or for specific modules only.  
Caution 
When upgrading from a version lower than 4.81, verify that the device 
contains no more than two SW-PACKs of CL.2 and/or VS, before the upgrade 
procedure is initiated.  

## 12.4 Upgrading Software using the CLI (TFTP)  *(p.910)*

12. Software Upgrade 
System Requirements 
Before starting the upgrade, verify that you have the following: 
• 
For upgrade via TFTP:  
 
Megaplex-4 unit with a router interface bound to the management interface used, and a 
static route defined to a PC with the TFTP server application (such as 3Cdaemon or 
PumpKIN), and a valid IP address. 
 
Software file stored on the PC. 
Note 
Megaplex-4 communicates with TFTP servers via Ethernet ports only.  
Also verify whether there is enough storage space on the device by ensuring that the number of free 
bytes exceeds the size of the new .bin file. 
A device may contain up to 5 SW-pack-x folders, each containing one SW version. To avoid memory 
issues RAD recommends uploading 2 CL card SW files and 2 or 3 more I/O module SW files depending on 
the free bytes available. 
 To delete an unused SW pack 
4. Go to file>dir> and type delete sw-pack-3. 
12.4 Upgrading Software using the CLI (TFTP) 
Network administrators use the TFTP protocol to distribute new software releases to all the managed 
Megaplex-4 units in the network from a central location. The central application is a PC on the network 
with a TFTP server application such as the PumpKIN server installed on it. 
Ethernet
PC with an Active  
TFTP Server and 
Application File
Ethernet
Application file is 
transferred to 
Megaplex-4100
Megaplex-4100
 
Downloading a Software Application File to Megaplex-4 via TFTP 
12. Software Upgrade 
Use the following procedure to download the software release to Megaplex-4 using the copy command. 
5. Verify that the required image file is stored on the PC together with the TFTP server application. 
6. Verify that Megaplex-4 has a router interface assigned to it, as explained in Adding and 
Configuring Router Interfaces in Chapter 8. 
7. Verify that a static route is configured to the PC, as explained in Configuring Static Routes and 
Default Gateway in Chapter 8. 
8. Ping the PC to verify the connection. 
9. Activate the TFTP server application, as explained in Activating the TFTP Server. 
10. Download the image file to the unit, as explained in Downloading the New Software Release 
File to Megaplex-4 Flash Disk. 
Note 
Configuration values shown in this chapter are examples only.  
Verifying the IP Settings 
Megaplex-4 must have a router interface with IP parameters configured according to your network 
requirements. In addition, a static route must be established to the TFTP server to establish a 
communication session with the TFTP server. 
For example: 
configure router 1 interface 1 address 11.11.11.29/30 
configure router 1 static 0.0.0.0/0 address 11.11.11.1 
 To verify the IP parameters: 
• 
At the router(1)# prompt, enter info detail. 
The router interface configuration information is displayed.  
mp4100>config>router(1)# info detail 
    interface  1 
        address  11.11.11.29/30 
        name  "Put your string here" 
        bind  svi  1 
        no vlan 
        no shutdown 
    exit 
    arp-timeout  1200 
12. Software Upgrade 
Pinging the PC 
Check the integrity of the communication link between Megaplex-4 and the PC by pinging the Megaplex-
4 from the PC. 
Activating the TFTP Server 
Once the TFTP server is activated on the PC, it waits for any TFTP file transfer request originating from 
the product, and carries out the received request automatically.  
 To run the TFTP server: 
• 
Activate a TFTP server application, such as 3Cdaemon (available from www.3com.com) or 
PumpKIN (available from http://kin.klever.net/pumpkin/). 
• 
The recommended method for downloading software to the flash disk is to use the file copy 
command of the CLI environment. This can be done remotely and does not require booting. 
Only CL modules need to be reset after this procedure. 
• 
Megaplex-4 SW is upgraded in 3 stages: 
Stage 
Description 
 
Upload 
The SW version is transferred from a PC to an unused sw-pack-x 
folder in the Megaplex-4 flash disk. 
 
Installation 
The file is transferred from the flash disk to the CL or I/O modules. 
 
Activation 
The new SW starts running after reboot (service may be affected). 
 
Uploading the Software 
 To upload a new SW file via CLI using TFTP 
1. Type file>copy tftp://172.17.191.181/<filename.bin> sw-pack-2 
2. To monitor the copy progress: 
 
12. Software Upgrade 
3. To check the flash memory contents, type file>dir. 
Installing the Software 
 To install CL or I/O SW via CLI: 
1. Type admin>software>install sw-pack-x. 
Display examples after installing the SW version in sw-pack-2. 
 
 
2. To check the installation status 
 
If the CLI prompts regarding installation status are missing (this may occasionally happen), you can check 
this in the logs using “config>reporting>show log” command. 
 
12. Software Upgrade 
 
3. 
To display the SW version in the sw-pack directories: 
 
4. 
To verify the software versions installed on cards, go to config and type show cards-summary: 

## 12.5 Upgrading Software using the CLI (SFTP)  *(p.915)*

12. Software Upgrade 
 
Activating the Software 
After a new SW is installed on an I/O module, the module reboots automatically and service is affected. 
To activate the new software on the CL modules, reboot the chassis. 
12.5 Upgrading Software using the CLI (SFTP)  
The recommended method for downloading software to the flash disk is to use the file copy command 
of the CLI environment. This can be done remotely and does not require booting. Only CL modules need 
to be reset after this procedure. 
The upgrade consists of two stages:  
• 
The application software is downloaded from a PC to the Megaplex-4 flash disk. This is done via 
SFTP, using the file>copy command 
• 
The software pack is downloaded from the flash disk to the CL. This is done, using the 
admin>software>install command. 
Network administrators use the SFTP protocol to securely distribute new software releases to all the 
managed Megaplex-4 units in the network from a central location. A central SFTP server application is 
installed on a PC on the network. 
12. Software Upgrade 
Ethernet
PC with an Active 
SFTP Server and 
Application File
Application file is 
transferred to 
Megaplex
Megaplex-4100/4104
 
Downloading a Software Application File to Megaplex-4 via SFTP 
Use the following procedure to download the software release to  
Megaplex-4 using the copy command. 
5. Verify that the required image file is stored on the PC together with the SFTP server application. 
6. Verify that Megaplex-4 has a valid network connection to the PC 
7. Ping the PC to verify the connection. 
8. Activate the SFTP server application, as explained in Activating the SFTP Server. 
9. Download the image file to the unit, as explained in Downloading the New Software Release 
File to Megaplex-4 Flash Disk. 
Note 
Configuration values shown in this chapter are examples only.  
Pinging the PC 
Check the integrity of the communication link between Megaplex-4 and the PC by pinging the Megaplex-
4 from the PC. 
Activating the SFTP Server 
Once the SFTP server is activated on the PC, it waits for any SFTP file transfer request originating from 
the product, and executes the received request automatically.  
 To run the SFTP server: 
• 
Activate a third-party SFTP server application. 
12. Software Upgrade 
Downloading the New Software Release File to Megaplex-4 Flash Disk 
Use this procedure to download the new software release to the Megaplex-4 flash disk. 
 To download an application file to the Megaplex-4 flash disk via CLI: 
• 
At the file# prompt, enter the copy command, as follows:  
copy sftp://<SFTP_user_name>:<SFTP_password>@<sftp_ip_address>/ 
<image_file_name> sw-pack-<index 1..4> 
where sftp-ip-address is the IP address of the PC in which the SFTP server is installed. 
• 
For example, to download the sw-pack.bin file to sw-pack-4 partition from the PC at 10.10.10.10 
with user name admin and password 1234: 
mp4100>file# sftp://<admin>:<1234>@10.10.10.10/sw-pack.bin sw-pack-4    
You are prompted to confirm the request: 
Are you sure? [yes/no] _ y 
The application file begins downloading. 
Note 
Issuing the dir command (file# prompt) while installing a new software 
release causes the CLI to stop responding during the installation process. The 
CLI connection is restored after the SW installation is complete.  
 To check the flash memory contents: 
• 
At the file# prompt, enter the dir command, for example:  
mp4100>file# dir 
Codes      C - Configuration S - Software             LO – Log 
Name                 Type Size(Bytes) Creation Date Status 
sw-pack-1            S    6306207    21-12-2010   valid 
                                     13:44:58 
sw-pack-2            S    6305847    21-2-2011    valid 
                                     7:48:0 
sw-pack-3            S    6278526    21-2-2011    valid 
                                     9:57:47 
sw-pack-4            S    6289552    6-1-2011     valid 
                                     10:23:13 
startup-config       C    95872      13-3-2011    valid 
                                     14:7:35 
user-default-config  C    95872      13-3-2011    valid 
                                     14:6:51 
factory-default-conf C    796        1-1-1970     Read Only 
12. Software Upgrade 
                                     0:0:9 
running-config       C    0          1-1-1970     Read Only 
                                     0:0:9 
Total Bytes : 101367808   Free Bytes  : 63442944 
 To monitor the copy progress:  
• 
At the file# prompt, enter the show copy command, for example:  
# show file copy 
Network to Device, Transferring Data 
Src: sftp://mp4100:1234@172.17.150.95/mp4cl2_03_07_72.bin 
Dst: sw-pack-4 
Started: 14.3.2011 8:50:52 
Transferred : 665600 Bytes in: 16 seconds (41600 Bytes/Second)  
Finally, the application file is downloaded and saved in partition 4 of the flash disk. 
File copy command was completed. 
sftp://mp4100:1234@172.17.150.95/mp4cl2_03_07_72.bin copied to sw-pack-4 successfully 
6306207 bytes copied in 13 secs (47415 bytes/sec) 
 To display the partition contents: 
• 
At the file# prompt, enter the show sw-pack command, for example: 
>file# show sw-pack 
Name      Version      Creation Time          Actual 
------------------------------------------------------------------------ 
sw-pack-1 1.0.0(1.39)  2012-08-06   00:00:00  ready 
 
sw-pack-1 Size (Bytes)  : 77140261 
 
Type      Name           Version      H/W Ver   Size 
  
 
 
 
 
(Bytes) 
--------------------------------------------------------------- main      main.bin       3.00B6    0.1       6306207 
asmi54cn  asmi54cn.bin   3.4567    1.2       1625132 
asmi54c   asmi54c.bin    4.5678    2.3       1898111 
m8e1      m8e1.bin       7.6543    9.8       844767 
op34c     op34c.bin      7.5642    8.9       683210 
op108c    op108c.bin     2.9637    8.5       1053603  
12. Software Upgrade 
Installing the New Software Release File from the Flash Disk  
Once a file is saved on the Megaplex-4100 flash disk, it must be copied to the CL.2 or I/O modules to 
replace the current software. The sw-pack file includes the new software version for all the CL.2 and I/O 
modules, according to your purchase order.  
You can choose to download the new SW release file to all the CL.2 and I/O modules installed in the 
chassis simultaneously. In this case, if the chassis includes several modules of the same kind, the new 
software release will be installed in all of them. If you do not want this to happen, you can issue a 
command to install the software in one specific slot. 
 To download the new software release file from the flash disk to all the CL.2 and I/O modules 
installed in the chassis: 
1. At the admin>software # prompt, enter the install command. For example: 
mp4100# admin 
mp4100>admin# software 
mp4100>admin>software# install sw-pack-3 
The previous software pack is deleted from the active partition: 
deleting file /tffs0/Sw-Pack/Active/main.bin 
deleting file /tffs0/Sw-Pack/Active/mainHdr.bin 
deleting file /tffs0/Sw-Pack/Active/op-108c.bin 
deleting file /tffs0/Sw-Pack/Active/op-108cHdr.bin 
deleting file /tffs0/Sw-Pack/Active/m8e1.bin 
deleting file /tffs0/Sw-Pack/Active/m8e1Hdr.bin 
 
Wait until install command completed..... 
  
successfull install to cl-a 
successfull install to cl-b 
 
installation completed 
The software pack stored in sw-pack-3 partition is transferred to the active partition and sent to 
all the relevant modules that are found in the chassis. The I/O modules perform reboot 
automatically and are now ready for operation with new software version.  
2. To activate the new software release for the CL modules, you must perform reboot. Disconnect 
the power, wait a few seconds and then reconnect the power. 
Megaplex-4 is upgraded and starts with the new software version. 
mp4100# admin software install sw-pack-1 
deleting file /tffs0:2/Sw-Pack/Active/main.bin 
deleting file /tffs0:2/Sw-Pack/Active/mainHdr.bin  

## 12.6 Upgrading Megaplex-4 Software via the Boot Menu  *(p.920)*

12. Software Upgrade 
 To download the new software release file from the flash disk to a specified CL.2 or I/O module: 
• 
At the admin>software # prompt, enter the install command and add the specified slot number. 
For example: 
mp4100# admin software install sw-pack-1 slot 10 
deleting file /tffs0/Sw-Pack/Active/op-108c.bin 
deleting file /tffs0/Sw-Pack/Active/op-108cHdr.bin 
 
Wait until install command completed..... 
  
successful install to op-108c 
 
installation completed 
The OP-108C module installed in slot 10 is upgraded and starts with the new software version. 
12.6 Upgrading Megaplex-4 Software via the Boot Menu 
Software downloading may also be performed using the Boot menu. The Boot menu can be reached 
while Megaplex-4 performs initialization, for example, after power-up.  
You may need to start the loading from the Boot menu when it is not possible to activate TFTP using the 
CLI because, for example, the Megaplex-4 software has not yet been downloaded or is corrupted. 
Caution 
The Boot menu procedures are recommended for use only by authorized 
personnel, because this menu provides many additional options that are 
intended for use only by technical support personnel.  
You can upgrade via the Boot menu using TFTP.  
Note 
All the screens shown in this section are for illustration purposes only. Your 
Megaplex-4 may display different software versions and port profiles.  
The preparations needed for using the TFTP/FTP protocol via the Boot menu are similar to the 
preparations needed to download software using the TFTP protocol via the CLI. The main difference is 
that you need to define the IP communication parameters associated with the corresponding Ethernet 
port (IP addresses and the associated subnet mask and a default gateway IP address).  
12. Software Upgrade 
Starting Boot Manager 
Prior to initiating the VXWORKS Boot Manager functionality, connect the ASCII terminal or PC with 
terminal emulation to the CONTROL DCE (serial) port of Megaplex-4.  
 To start VXWORKS Boot Manager: 
1. Verify that the *.bin file is stored on the PC with the terminal application. 
2. Configure the communication parameters of the selected PC serial port for asynchronous 
communication for 115.2 kbps, no parity, one start bit, eight data bits and one stop bit. Turn all 
types of flow control off. 
3. Turn off Megaplex-4. 
4. Activate the terminal application. 
5. Turn on Megaplex-4. 
Information about the System Boot, Boot version, and information about CPU, OS-version, BSP 
version and Boot Manager version is displayed. 
The following message appears: 
Use '?'/help to view available commands. 
Press any key to stop auto-boot.... 
6. Press any key to stop the auto-boot and get a boot prompt. 
The boot prompt is displayed: 
[boot]: 
7. Press <?> to display the Help list. 
The Help list is displayed. 
• Commands: 
 ?/help                           - print this list 
 p                                - print boot parameters 
 c [param]                        - change boot parameter(s) 
 v                                - print boot logo with versions information 
 run                              - load active sw pack and execute  
 delete <FileName>                - delete a file 
 dir                              - show list of files 
 show <index>                     - show sw pack info 
 download <index> [,<FileName>] - download a sw pack to specific index 
set-active <index>               - Set a sw pack index to be the active application 
 control-x/reset                  - reboot/reset 
VXWORKS Boot Manager Help List 
8. Press <P> to display all boot parameters.  
12. Software Upgrade 
The boot parameters list appears. A typical boot parameters list is shown in the figure below. 
The parameters are described in the table below. 
[boot]: p 
 
file name       (fn) : vxworks 
device IP       (ip) : 10.10.10.88 
device mask     (dm) : 255.255.255.0 
server IP      (sip) : 10.10.10.10 
gateway IP       (g) : 10.10.10.10 
user             (u) : vxworks 
ftp password    (pw) : ******* 
device name     (dn) : MP4100 
quick autoboot   (q) : yes 
protocol         (p) : ftp 
baud rate        (b) : 9600  
Typical Boot Parameters Screen 
Boot Parameters 
Parameter 
Command 
Description 
file name  
fn 
The binary software pack file (*.bin) name 
device ip 
ip 
The IP address of Megaplex-4 
device mask 
dm 
The IP subnet mask of Megaplex-4 
server IP 
sip 
The TFTP server IP address 
gateway ip 
g 
The TFTP server default gateway IP-address if the server is located on 
a different LAN. 
Note: Be sure to select an IP address within the subnet of the 
assigned Megaplex-4 IP address. 
Note: If no default gateway is needed, for example, because the TFTP 
server is attached to the same LAN as Megaplex-4 being upgraded, 
enter 0.0.0.0. 
user 
u 
The user name, as registered at the FTP server. 
Note: Displayed only when using FTP Protocol. 
ftp password 
vx 
The user password, as registered at the FTP server. 
Note: Displayed only when using FTP Protocol. 
device name 
dn 
MP4100 
quick autoboot 
q 
Enabling or disabling the quick autoboot feature 
protocol 
p 
The file transfer protocol in use: TFTP or FTP 
12. Software Upgrade 
Parameter 
Command 
Description 
baud rate 
 
 
b 
Transmission bit rate (in kbps): 9600, 19200, 115200  
 
Note 
The CLI commands are case insensitive.  
9. Press <C> to change the boot parameters and type valid values in each field.  
 
Type  'c' to modify all parameters 
 
Type  'c [parameter]' to modify the specific parameter (for example, to change the filename 
to sw-pack.bin, type: c fn vxworks sw-pack.bin). 
'.' = clear field;  '-' = go to previous field;  ^D = quit 
 
file name       (fn) : vxworks sw-pack.bin 
device IP       (ip) : 10.10.10.88 
device mask     (dm) : 255.255.255.0 
server IP      (sip) : 10.10.10.10 
gateway IP       (g) : 10.10.10.10 
user             (u) : vxworks 
ftp password    (pw) (blank = use rsh): ******* 
device name     (dn) : MP4100 
quick autoboot [y/n] : y 
protocol  [tftp/ftp] : ftp 
baud rate [9600/19200/115200]: 9600 
10. To complete the upgrade and log on again, follow the onscreen instructions. 
Using the TFTP/FTP Protocol 
Use the following procedure to download software release to Megaplex-4 via TFTP. 
 To download software file(s) from the Boot menu to Megaplex-4 via TFTP/FTP: 
1. Verify that the *.bin file is stored on the PC with the TFTP server application. 
2. Activate the TFTP server application/FTP server. 
Note 
When working with FTP server, the user name and password in Boot 
parameters must be the same as defined in FTP server.  
3. Turn on Megaplex-4 and enter the Boot menu. Set TFTP or FTP protocol. 
12. Software Upgrade 
4. From the Boot menu, type download <index 1..4> [<FileName>] command to start downloading 
the software pack file from the PC to the corresponding partition of the Megaplex-4 flash disk.  
Note 
[<FileName>] is used if you did not specify the filename in the Boot menu 
earlier.  
For example: Download the file to sw-pack-2 
[boot]: download 2    
The file is being copied to sw-pack-2 partition: 
File transferring - 7580KB 
226 Transfer finished successfully. 
 
Please wait, old file is being erased and written with new one. 
File writing to flash: - 7580KB 
File downloaded successfully to :2 
[boot]: 
5. Using dir command, check which partition is currently active. In our example it is sw-pack-2.  
[boot]: dir 
  SIZE        FILE-NAME 
  796         factory-default-config 
  6296759     sw-pack-1 
  6305902     sw-pack-2 
  6278526     sw-pack-3 
  6289552     sw-pack-4 
Active SW-pack is: 2 
Total Bytes : 101367808   Free Bytes  : 69701632 
6. Use set-active command to activate the partition to which the file has been downloaded (in our 
example: sw-pack-2).  
[boot]: set-active 2   
set-active may take few minutes... 
deleting file /tffs0/Sw-Pack/Active/main.bin 
deleting file /tffs0/Sw-Pack/Active/mainHdr.bin 
SW set active 2 completed successfully. 
The new software release is now stored in partition 2 and will be activated after reset. 
7. Perform one of the following: 
 
Type “@” or “run”.  
The following message is displayed and the new software release is activated: 
[boot]: run 
External file header passed validation! 
Loading/un-compressing main.bin... 
Starting the APPLICATION off address 0x10000... 
 
Press <Ctrl + X> to perform a cold (hard) reboot with turning power off and then on. 

## 12.7 Verifying the Upgrade Results  *(p.925)*

12. Software Upgrade 
 
Type “reset” to perform a warm (soft) reboot without turning off power. 
The following message is displayed: 
Are you sure (y/n)? 
Press <Y>.  
When the downloading process is successfully completed, you will see a sequence of messages 
similar to the following: 
External file header passed validation! 
Loading/un-compressing main.bin... 
 
Starting the APPLICATION off address 0x10000... 
 
Instantiating /ram as rawFs,  device = 0x20001 
Formatting /ram for DOSFS 
Instantiating /ram as rawFs, device = 0x20001 
Formatting...Retrieved old volume params with %38 confidence: 
Volume Parameters: FAT type: FAT32, sectors per cluster 0 
  0 FAT copies, 0 clusters, 0 sectors per FAT 
  Sectors reserved 0, hidden 0, FAT sectors 0 
  Root dir entries 0, sysId (null)  , serial number 7d0000 
  Label:"           " ... 
Disk with 64 sectors of 512 bytes will be formatted with: 
Volume Parameters: FAT type: FAT12, sectors per cluster 1 
  2 FAT copies, 54 clusters, 1 sectors per FAT 
  Sectors reserved 1, hidden 0, FAT sectors 2 
  Root dir entries 112, sysId VXDOS12 , serial number 7d0000 
                                                               
Adding 71349 symbols for standalone. 
 
External file header passed validation! 
Loading/un-compressing main.bin... 
 
Starting the APPLICATION off address 0x10000... 
8. Press <Enter> to start working with the new SW release downloaded. 
Note 
The new parameters take effect only after the reset is completed.  
12.7 Verifying the Upgrade Results 
To verify that the upgrade was successful, log on to Megaplex-4 via HyperTerminal to view the Inventory 
summary. 

## 12.8 Restoring the Previous Software Version  *(p.926)*

12. Software Upgrade 
 To verify the upgrade result: 
• 
Type: show cards-summary in the config context and verify the active software version in the 
SW Ver column. 
config# show cards-summary 
• 
At the config# prompt, enter the show cards-summary command. 
# show configure cards-summary 
Slot  Actual          Provisioned     HW Ver    SW Ver 
      Type            Type 
--------------------------------------------------------------- 
PS-A  ps              ps              --        -- 
PS-B  --              --              --        -- 
CL-A  CL2 622GbEa     CL2 622GbEa     1.2       4.91.59 Active 
CL-B  --              --              --        4.91.59 
1     VS-OCU-EM       VS-OCU-EM       3         3.58 
2     --              --              --        -- 
3     --              --              --        -- 
4     VS-EM-8 PW      VS-EM-8 PW      3         3.58 
5     --              --              --        -- 
6     --              --              --        -- 
7     VS 6 E1-T1      VS-6-E1         3         3.58 
8     --              --              --        -- 
9     VS 6 E1-T1      VS-6-E1         3         3.58 
10    --              --              --        -- 
 
Note 
If downloading failed, repeat the entire procedure.  
12.8 Restoring the Previous Software Version  
The procedure of restoring the previous software version (downgrading) depends on its status inside the 
flash memory.   
Note 
Downgrading the software version from 4.91.xx to version 4.71.xx may impact 
login via SSH and is not recommended, regardless of the configuration 
database. 
 To display the flash memory/partition contents: 
• 
At the file# prompt, enter the show sw-pack command, for example: 
12. Software Upgrade 
>file# show sw-pack 
Name      Version   Creation Time          Status     Actual 
--------------------------------------------------------------- 
sw-pack-1 4.00B6    21-12-2010   13:44:58  Ready      Yes 
sw-pack-2 4.00B5    21-2-2011    7:48:0    Ready      -- 
sw-pack-3 4.00B4    21-2-2011    9:57:47   Ready      -- 
sw-pack-4 4.00B6    14-3-2011    9:32:56   Ready      -- 
  
sw-pack-1 Size (Bytes)  : 6306207 
  
Type      Name           Version   H/W Ver   Size 
                                             (Bytes) 
--------------------------------------------------------------- 
main      main.bin       4.00B6    0.1       6305967 
  
sw-pack-2 Size (Bytes)  : 6305847 
  
Type      Name           Version   H/W Ver   Size 
                                             (Bytes) 
--------------------------------------------------------------- 
main      main.bin       4.00B5    0.1       6305607 
  
sw-pack-3 Size (Bytes)  : 6278526 
  
Type      Name           Version   H/W Ver   Size 
                                             (Bytes) 
--------------------------------------------------------------- 
main      main.bin       4.00B4    0.1       6278286 
  
sw-pack-4 Size (Bytes)  : 12493650 
  
Type      Name           Version   H/W Ver   Size 
                                             (Bytes) 
--------------------------------------------------------------- 
main      main.bin       4.00B6    0.1       6306207 
asmi54cn  asmi54cn.bin   3.4567    1.2       1625132 
asmi54c   asmi54c.bin    4.5678    2.3       1898111 
m8e1      m8e1.bin       7.6543    9.8       844767 
op34c     op34c.bin      7.5642    8.9       683210 
op108c    op108c.bin     2.9637    8.5       1053603  
• 
If the desired version is stored in one of the four sw-pack partitions, make this partition active, 
as described in Installing the New Software Release File from the Flash Disk.    
• 
If the desired version does not appear in the list, you can restore the previous software version 
by following any of the procedures described in this section, as if it were a new version.   

## 12.9 Minimizing Service Disruption  *(p.928)*

12. Software Upgrade 
12.9 Minimizing Service Disruption 
When services are protected or configured only between I/O cards, service disruption can be minimized 
after the installation of the new software version on both CL-A and CL-B is completed. 
First, restart the standby Common Logic card. Once the standby Common Logic card is up and the 
mirroring process is completed, restart the active Common Logic card. 
 To shorten service disruption to under 50 ms: 
1. Reset the standby CL card (CL-B is standby) using the configure>slot cl-b>reset command. 
After the mirroring process is finished, the standby CL contains the new SW version. 
2. Reset the active CL card (CL-A is active), using the configure>slot cl-a>reset command. The 
standby CL becomes active and the services keep running. 
After the mirroring process is finished, the active CL card becomes the standby CL and contains 
the new SW version. 
 
 