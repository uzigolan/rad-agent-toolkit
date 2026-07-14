# 12 Software Upgrade

*Manual `MP-1-mn_ver 2.2.pdf`, pages 427–437.*


## 12.1 Compatibility Requirements  *(p.427)*

This chapter explains how to upgrade Megaplex-1 for software version 2.2. 
Software upgrade is required to fix product limitations, enable new features, or to make the unit 
compatible with other devices that are already running the new software version. 
The device can store up to two software images, referred to as software packs and named sw-pack-1 
and sw-pack-2. You can designate any of the software packs as active. The non-active software packs 
serve as backups that can be used if the active software becomes corrupted.  
The information in this chapter includes the following: 
• 
Detailed conditions required for the upgrade 
• 
Any impact the upgrade may have on the system 
• 
Description of downloading options. 
Application software can be downloaded to Megaplex-1 via SFTP/TFTP with the copy command, or via 
XMODEM, FTP or TFTP, using the boot menu. 
The downloaded software pack can be installed as the active software via the admin software install 
command, or by using the boot menu. 
12.1 Compatibility Requirements 
Following are the software releases that can be upgraded to version 2.1, as well as the hardware 
revisions that can accept the software version 2.1. 
• 
Software – Ver. 2.0.0(0.27) 
• 
Hardware –  0.0  and above 

## 12.2 Prerequisites  *(p.428)*


## 12.3 Upgrading the Device Software via CLI  *(p.428)*

Megaplex-1 
12. Software Upgrade 
12.2 Prerequisites 
Before starting the upgrade, verify that you have the following: 
• 
For upgrade via SFTP/FTP/TFTP: 
 
Operational Megaplex-1 unit with valid IP parameters configured  
 
Connection to a PC with an SFTP/FTP/TFTP server application and a valid IP address 
 
Software image file stored on the PC. The image file (and exact name) can be obtained from 
the local RAD business partner from whom the device was purchased. 
• 
For upgrade via XMODEM:  
 
Operational Megaplex-1 unit 
 
Connection to a PC via a terminal emulation program 
 
Software image file stored on the PC. The image file (and exact name) can be obtained from 
the local RAD business partner from whom the device was purchased. 
12.3 Upgrading the Device Software via CLI 
The recommended software downloading method is to use the copy command. 
Network administrators can use this procedure to distribute new software releases to all the managed 
Megaplex-1 units in the network from a central location. 
Use the following procedure to download software release 2.1 to Megaplex-1 via CLI. 
1. Verify that the image file is stored on the PC with the SFTP/TFTP server application. 
2. Verify that the Megaplex-1 router has been configured with valid IP parameters. 
3. Ping the PC to verify the connection. 
4. Activate the SFTP/TFTP server application. 
5. Download the image file from the PC to Megaplex-1. 
6. Install the image as the active software. 
Note 
Configuration values shown in this chapter are examples only.  
Megaplex-1 
12. Software Upgrade 
Verifying the IP Parameters 
In order to be able to establish communication with the SFTP/TFTP server, the Megaplex-1 router must 
have IP parameters configured according to your network requirements. Refer to the following manual 
sections for additional information: 
• 
Connecting to a Terminal in the Installation and Setup chapter 
• 
Working with Terminal in the Management and Security chapter  
• 
Router in the Networking chapter. 
Pinging the PC 
Check the integrity of the communication link between Megaplex-1 and the PC by pinging the PC from 
Megaplex-1. 
 To ping the PC: 
1. In any level, start pinging the PC specifying its IP address and optionally the number of packets 
to send: 
ping <ip-address> [number-of-packets <num-packets>] 
A reply from the PC indicates a proper communication link. 
2. If the ping request times out, check the link between Megaplex-1 and the PC (physical path, 
configuration parameters, etc.)  
Activating the SFTP Server 
Once the SFTP server is activated on the PC, it waits for any SFTP file transfer request originating from 
the product, and carries out the received request automatically.  
SFTP file transfers are carried out through TCP port 22. Make sure that the firewall you are using on the 
server allows communication through this port (refer to the Administration chapter for details).  
Activating the TFTP Server 
Once the TFTP server is activated on the PC, it waits for any TFTP file transfer request originating from 
the product, and carries out the received request automatically.  
Megaplex-1 
12. Software Upgrade 
TFTP file transfers are carried out through port 69. Make sure that the firewall you are using on the 
server allows communication through this port (refer to the Administration chapter for details).  
Note 
Configure the connection timeout of the TFTP server to be more than 
30 seconds to prevent an automatic disconnection during the backup partition 
deletion (about 25 seconds).  
Downloading the Software 
This procedure is used to download the new software release. 
 To copy the image file to the Megaplex-1 unit: 
• 
In any level, enter: 
copy sftp://<username>:<password>@<ip-address>/<image-file-name> 
<sw-pack-n>  
Where <ip-address> is the IP address of the PC where the SFTP server is installed, and <n> 
is the index of the software pack. 
Or 
copy tftp://<tftp-ip-address>/<image-file-name> <sw-pack-n>  
Where tftp-ip-address is the IP address of the PC where the TFTP server is installed, and 
<n> is the index of the software pack. 
Note 
Choose an index that is not being used by the active software, or by a 
software pack that you do not want to overwrite.  
The software download is performed. See Installing Software for instructions on installing the 
downloaded software as the active software.   
Installing Software 
After software is downloaded to Megaplex-1, it has to be installed via the install command as the active 
software.  
Note 
The file startup-config must exist before you can install software.  

## 12.4 Upgrading the Device Software via the Boot Menu  *(p.431)*

Megaplex-1 
12. Software Upgrade 
 To install a software pack as active: 
1. At the admin>software# prompt, enter: 
install <filename> The parameter <filename> can be any of the non-active software 
packs (sw-pack-1 or sw-pack-2). The following is displayed: 
Device will install file and reboot! Are you sure? [yes/no] _ 
2. Type yes to confirm. 
12.4 Upgrading the Device Software via the Boot Menu 
Software downloading can also be performed using the Boot menu. The Boot menu can be reached 
while Megaplex-1 performs initialization, such as after power-up.  
You may need to start the loading from the Boot menu if you are unable to use the copy command (for 
example, because the Megaplex-1 software has not yet been downloaded or is corrupted). 
Caution 
The Boot menu procedures are recommended only for use by authorized 
personnel, because this menu provides many additional options that are 
intended for use only by technical support personnel.  
The following software downloading options are available from the Boot menu: 
• 
Downloading using the XMODEM protocol. This is usually performed by downloading from a PC 
directly connected to the CONTROL DCE port of the unit.  
• 
Downloading using FTP/TFTP. This is usually performed by downloading from a remote location 
that provides an IP communication path to an Ethernet port of Megaplex-1. 
Accessing the Boot Menu 
The boot menu can be accessed when the device is powered up, before logging in. 
 To access the boot menu: 
1. Connect the ASCII terminal or PC with terminal emulation to the Megaplex-1 CONTROL port. 
2. Configure the communication parameters of the selected PC serial port for asynchronous 
communication with 9,600 bps, no parity, one start bit, eight data bits, and one stop bit. Turn all 
types of flow control off. 
Megaplex-1 
12. Software Upgrade 
3. Power off Megaplex-1. 
4. Activate the terminal application. 
5. Power on Megaplex-1 and immediately start pressing the <Enter> key several times in sequence 
until you see the prompt to press any key to stop the autoboot.  
6. Press any key. 
The boot screen appears. A typical boot screen is shown below (the exact version and date 
displayed by your Megaplex-1 unit may be different).   
Note 
If you miss the timing, Megaplex-1 performs a regular reboot process (this 
process starts with Loading/un-compressing sw-pack-<n> and ends with the 
login screen).  
                           System Boot 
 
          Copyright 1984-2008  RAD Data Communications, Ltd. 
 
 
                Boot version: 1.04 [03-DEC-17] 
 
 
CPU        : Freescale MPC8313E 
OS version : VxWorks 6.9 
BSP version: 1.08 
Boot-Manager version: 3.02 [Oct 19 2014] 
 
Use '?'/help to view available commands 
 
 
 
Press any key to stop auto-boot... 
7. Enter ? to display a list of boot commands. 
Commands: 
 ?/help                           - print this list 
 p                                - print boot parameters 
 c [param]                        - change boot parameter(s) 
 v                                - print boot logo with versions information 
 run                              - load active sw pack and execute 
 delete <FileName>                - delete a file 
 dir                              - show list of files 
 show <index>                     - show sw pack info 
 download <index> [,<FileName|x>] - download a sw pack to specific index (x - by 
Xmodem) 
 set-active <index>               - Set a sw pack index to be the active 
application 
 control-x/reset                  - reboot/reset 
8. Enter p to display all boot parameters.  
The boot parameters appear. A typical boot parameter list is shown below: 
Megaplex-1 
12. Software Upgrade 
[boot]: p 
 
file name       (fn) : vxWorks 
device IP       (ip) : 10.10.10.101 
device mask     (dm) : 255.255.255.0 
server IP      (sip) : 10.10.10.2 
gateway IP       (g) : 10.10.10.2 
user             (u) : vxworks 
ftp password    (pw) : ******* 
device name     (dn) : Megaplex-1 
quick autoboot   (q) : no 
protocol         (p) : ftp 
baud rate        (b) : 9600 
 
Parameter 
Command 
Description 
file name  
fn 
The binary software pack file (*.bin) name to be downloaded via 
FTP/TFTP 
device ip 
ip 
Megaplex-1 IP address  
device mask 
dm 
Megaplex-1 IP subnet mask  
server IP 
sip 
FTP/TFTP server IP address 
gateway ip 
g 
FTP/TFTP server default gateway IP address 
user 
u 
User name for FTP server 
Note: Displayed only when using FTP protocol. 
ftp password 
pw 
User password for FTP server 
Note: Displayed only when using FTP protocol. 
device name 
dn 
Megaplex-1 
quick autoboot 
q 
Enables or disables the quick autoboot feature 
protocol 
p 
File transfer protocol to use: FTP or TFTP 
baud rate 
 
 
b 
Transmission bit rate (in kbps): 9600, 19200, or 115200  
9. Enter c to configure the boot parameters.  
The boot parameters are displayed line by line. For each parameter, you can type a different 
value, or click <Enter> to go to the next parameter. The example below illustrates changing the 
file name to Megaplex-1.bin, and the protocol to TFTP. 
'.' = clear field;  '-' = go to previous field;  ^D = quit 
 
file name       (fn) : vxworks Megaplex-1.bin Liat 
Megaplex-1 
12. Software Upgrade 
device IP       (ip) : 10.10.10.101  
device mask     (dm) : 255.255.255.0 
server IP      (sip) : 10.10.10.2 
gateway IP       (g) : 10.10.10.2 
user             (u) : vxworks 
ftp password    (pw) (blank = use rsh): ******* 
device name     (dn) : Megaplex-1 
quick autoboot [y/n] : n 
protocol  [tftp/ftp] : ftp tftp 
baud rate [9600/19200/115200]: 9600 
10. See the following sections for instructions on downloading via XMODEM, FTP, or TFTP.  
Using the XMODEM Protocol  
Use the following procedure to download software release 2.1 to Megaplex-1 via XMODEM. 
 To download software release via XMODEM: 
1. Verify that the image file is stored on the PC with the terminal application. 
2. Enter the boot menu and set the boot parameters as needed (see Accessing the Boot Menu). 
3. At the boot prompt, enter: 
download <index>, x  
Note 
The <index> parameter corresponds to the software pack number to which to 
copy the image file.  
The process starts, and the following is displayed: 
The terminal will become disabled !!! 
Please send the file in XMODEM 
4. Start the transfer in accordance with the program you are using. For example, if you are using 
the Windows HyperTerminal utility: 
 
Select Transfer in the HyperTerminal menu bar, and then select Send File on the Transfer 
menu. 
The Send File window is displayed: 
 
Select the prescribed Megaplex-1 software file name (you may use the Browse function 
to find it). 
 
In the Protocol field, select Xmodem. 
 
When ready, press Send in the Send File window.  
Megaplex-1 
12. Software Upgrade 
You can now monitor the progress of the downloading in the Send File window. 
When the downloading process has successfully completed, a sequence of messages similar to 
the following is displayed: 
File writing to flash: - 4030KB 
File downloaded successfully to :2 
5. See Activating Software for instructions on activating the downloaded software. 
Using FTP  
Use the following procedure to download software release 2.1 to Megaplex-1 via FTP. 
 To download software release via FTP: 
1. Verify that the image file is stored on the PC with the FTP server application. 
2. Enter the boot menu and set the boot parameters as needed (see Accessing the Boot Menu). 
For example, set the FTP user and password, and set protocol to FTP. 
3. At the boot prompt, enter: 
download <index>[, <FileName>] 
If no errors are detected, the downloading process starts, and the file is downloaded via FTP. 
Note 
• 
The <index> parameter corresponds to the software pack number to 
which to copy the image file 
• 
If you have set the file name in the boot parameters, you do not need to 
specify <FileName>. 
For example, to download the file name configured in the boot parameters to sw-pack-2, enter: 
download 2 
4. See Activating Software for instructions on activating the downloaded software. 
Using TFTP  
Use the following procedure to download software release 2.1 to Megaplex-1 via TFTP. 
 To download software release via TFTP: 
1. Verify that the image file is stored on the PC with the TFTP server application. 
Megaplex-1 
12. Software Upgrade 
2. Enter the boot menu and set the boot parameters as needed (see Accessing the Boot Menu). 
For example, set protocol to TFTP.  
3. At the boot prompt, enter: 
download <index>[, <FileName>] 
If no errors are detected, the downloading process starts, and the file is downloaded via TFTP. 
Note 
• 
The <index> parameter corresponds to the software pack number to 
which to copy the image file 
• 
If you have set the file name in the boot parameters, you do not need to 
specify <FileName>. 
For example, to download the file name configured in the boot parameters to sw-pack-2, enter: 
download 2 
4. See Activating Software for instructions on activating the downloaded software. 
Activating Software  
To activate a software pack, you need to designate it as active and load it. 
 To activate a software pack: 
1. To set the software as active, enter: 
set-active <index>. 
A confirmation similar to the following is displayed: 
SW set active 2 completed successfully. 
2. To load the active software, type: run. 
A sequence of messages similar to the following is displayed: 
Loading/un-compressing sw-pack-2... 
Starting the APPLICATION off address 0x10000... 
After a few more seconds, the login prompt is displayed. 

## 12.5 Verifying Upgrade Results  *(p.437)*

Megaplex-1 
12. Software Upgrade 
12.5 Verifying Upgrade Results 
To verify that the upgrade was successful, log on to Megaplex-1 via a terminal emulation program to 
view the Inventory table (show summary-inventory at prompt config>system#), and verify the active 
software version in the SW Rev column. 
 
 