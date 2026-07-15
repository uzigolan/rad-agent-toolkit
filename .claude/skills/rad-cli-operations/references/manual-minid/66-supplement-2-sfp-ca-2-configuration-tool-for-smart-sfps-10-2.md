# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 10.2 File Operations

*Manual `MiNID_ver_2_6_mn.pdf`, pages 227–234.*


## SFTP Application  *(p.227)*

10. Administration 
• 
In the CLI, go to the configure system context, and configure any of the following (to empty the 
parameter, use no): 
 
[no] contact <contact name> 
 
[no] device-name <device name> 
 
[no] location <location> 
Note 
The device information that you enter should not contain spaces, in both the 
web interface and CLI. 
10.2 File Operations 
You can perform the following file operations: 
• 
Copy application software, boot software, or configuration files, either locally in MiNID or 
between MiNID and a remote PC via SFTP or TFTP 
• 
Display information on the configuration files and software files (software packs) 
• 
Delete files 
SFTP Application 
The SFTP protocol is used to provide secure file transfers via the product's Ethernet interface. SFTP is a 
version of FTP that encrypts commands and data transfers, keeping your data secure and your session 
private. For SFTP file transfers, an SFTP server application must be installed on the local or remote 
computer.  
A variety of third-party applications offer SFTP server software. For more information, refer to the 
documentation of these applications. 
Ethernet
PC with an active SFTP 
server and software/
configuration file
Software/
configuration file is 
transferred to MiNID
Switch
MiNID
 
Downloading a Software or Configuration File via SFTP 

## TFTP Application  *(p.228)*


## Copying Files  *(p.228)*

10. Administration 
If you use a local laptop and SFTP is the preferred transfer method, an SFTP server application must be 
installed on it. SFTP file transfers are carried out through TCP port 22. You should check that the firewall 
you are using on the server computer allows communication through this port. 
TFTP Application 
The TFTP protocol is typically used for remote IP-to-IP file transfers via the product's Ethernet interface. 
It can be used, however, for local file transfer as well, as the transfer rate of the Ethernet interface is 
much faster than using a terminal emulation program with the SFP-CA.2 adaptor for the SFP sleeve. 
For TFTP file transfers, a TFTP server application must be installed on the local or remote computer. As it 
runs in the background, the TFTP server waits for any TFTP file transfer request originating from the 
product, and carries out the received request automatically.  
A variety of third-party TFTP applications are available that allow the instant creation of a TFTP server on 
a client computer. For more information, refer to the documentation of these applications. 
Ethernet
PC with an active TFTP 
server and software/
configuration file
Software/
configuration file is 
transferred to MiNID
Switch
MiNID
 
Downloading a Software or Configuration File via TFTP 
If you use a local laptop and TFTP is the preferred transfer method, a TFTP server application must be 
installed on it. TFTP file transfers are carried out through port 69. You should check that the firewall you 
are using on the server computer allows communication through this port. 
Copying Files 
You can use the Web interface or CLI to copy files within the MiNID unit, or download/upload files to the 
MiNID unit via SFTP/TFTP. 
After a file copying operation completes, an event is written in the event log that indicates the result of 
the file copy. 
If a configuration file is downloaded to MiNID, it is executed after the next device reset if applicable 
according to the MiNID startup sequence (refer to Operation).  
10. Administration 
The following files can be uploaded or downloaded: 
• 
boot – Boot software (can be downloaded only) 
• 
log-file – Event log file (can be uploaded only) 
• 
running-config – Configuration file containing current configuration that the device is running  
(can be uploaded only) 
• 
startup-config – Configuration file containing saved non-default user configuration  
• 
sw-pack-1, sw-pack-2 – Application software files (can be downloaded only) 
• 
user-default-config – Configuration file containing default user configuration 
The following files can be copied within the MiNID unit: 
• 
Source file can be startup-config, running-config or user-default-config 
• 
Destination file can be startup-config or user-default-config 
 
Note 
• 
A file cannot be copied to itself 
• 
A configuration file cannot be copied to the log file, and the log file cannot 
be copied to a configuration file. 
 
Copying Files Using the Web Interface 
 To copy files via the web interface: 
1. Go to Utilities > File > Copy. 
10. Administration 
MiNID  
  
 
 
 Utilities>File>Copy 
  
 
 Protocol 
 
TFTP 
 Server IP 
 
0.0.0.0 
 Direction 
 
Remote to Local 
 Remote File Name 
 
sw-pack-1 
 Local File Name 
 
sw-pack-1 
  
 
 
2. Fill in the parameters according to the table below. 
3. Click <Apply> to initiate the file copy. 
You are asked to confirm the copying. 
4. Click <Yes> to confirm. 
The file copying is performed.  
Copy File Web Parameters 
 
Parameter 
Description 
Protocol 
Specifies protocol for copying: 
• TFTP – File transfer via TFTP server 
• SFTP – File transfer via SFTP server 
Local – Copy files within the MiNIDunit 
SFTP User Name 
User name for SFTP server 
Note: Appears only if protocol is SFTP 
SFTP Password 
Password for SFTP server 
Note: Appears only if protocol is SFTP 
Server IP 
IP address of the PC where the SFTP/TFTP server is located 
Note: Appears only if protocol is SFTP or TFTP 
10. Administration 
Parameter 
Description 
Direction 
• Remote to Local – File transfer from SFTP/TFTP server to 
MiNID 
• Local to Remote – File transfer from MiNID to SFTP/TFTP 
server 
Note: Appears only if protocol is SFTP or TFTP 
Remote File Name 
Name of file on remote PC 
Note: Appears only if protocol is SFTP or TFTP 
Direction 
• Remote to Local – File transfer from SFTP/TFTP server to 
MiNID 
• Local to Remote – File transfer from MiNID to SFTP/TFTP 
server 
Note: Appears only if protocol is SFTP or TFTP 
Remote File Name 
Name of file on remote PC 
Note: Appears only if protocol is SFTP or TFTP 
Local File Name 
Name of local file, can be one of the following: 
• startup-config 
• user-default-config 
• running-config 
• log-file 
Note: Appears only if protocol is SFTP or TFTP 
Source File Name 
Source file for local copy, must be one of the following: 
• startup-config 
• user-default-config 
• running-config 
Note: Appears only if protocol is Local 
Destination File Name 
Destination file for local copy, must be one of the following: 
• startup-config 
• user-default-config 
Note: Appears only if protocol is Local 

## Deleting Files  *(p.232)*

10. Administration 
Copying Files Using the CLI 
 To copy files: 
1. Navigate to the file level. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Copying file from remote PC 
via SFTP/TFTP server to 
MiNID 
copy 
sftp://<username>:<password>@<ipv4-addr
ess>/ 
<remote-file-name> { sw-pack-1 | sw-pack-2 
| boot | startup-config | user-default-config  
copy 
tftp://<ipv4-address>/<remote-file-name> { 
sw-pack-1 | sw-pack-2 | boot | 
startup-config | user-default-config} 
<username> – User name for 
SFTP server 
<password> – Password for SFTP 
server 
<ipv4-address> – IP address of 
the PC where the SFTP/TFTP 
server is located 
<remote-file-name> – Name of 
file on remote PC 
Copying file from MiNID to 
remote PC via SFTP/TFTP 
server 
copy { startup-config | running-config | 
user-default-config | log-file } 
sftp://<username>:<password>@<ipv4-addr
ess>/ 
<remote-file-name> 
copy { startup-config | running-config | 
user-default-config | log-file } 
tftp://<ipv4-address>/<remote-file-name> 
See above for parameter 
descriptions 
Copying file within MiNID 
copy {startup-config | running-config | 
user-default-config } {startup-config | 
user-default-config } 
 
Deleting Files 
You can delete the following files: 
• 
startup-config 
• 
user-default-config 
10. Administration 
 To delete a file: 
Do one of the following: 
• 
In the web interface: 
a. Go to Utilities > File > Delete. 
 
MiNID 
  
 
 
 Utilities>File>Delete 
  
 
 Image Type 
 
startup-config 
  
 
 
 
b. Select the file to delete, and click <Apply>. 
 
Note 
The Image Type dropdown list contains only the files that can be deleted, and 
exist in the device. 
 
You are prompted to confirm the deletion. 
c. Confirm the deletion. 
The file is deleted. 
• 
In the CLI: 
a. At the file# prompt, enter:  
delete <file-name> 
You are prompted to confirm the deletion. 
b. Confirm the deletion. 
The file is deleted. 
Example 
>file# delete user-default-config 
Are You Sure? [y/n] y 
>file# 
*****user-default-config Deleted Successful***** 

## Displaying File Information  *(p.234)*

10. Administration 
Displaying File Information 
You can display the following: 
• 
Information on the software files, including the status and contents of the active software 
version and the software packs, as well as the date the software packs were downloaded if 
applicable. For information on installing a software pack as active, refer to Chapter 12 (Upgrade) 
for details. 
• 
Contents of startup and user configuration files (CLI only). 
Displaying File Information Using the Web Interface 
 To display information on the software files: 
• 
Navigate to Configuration > System > Install SW-Pack . 
MiNID 
  
 
 
 
 
 Configuration > System > Install 
  
 
 
 
 Image Type 
 
sw-pack-1 
 
 
  
 
 
 
 
 Apply 
 
 
 
 
  
 
 
 
 
 Name 
Status 
Version 
Date 
 
 Active 
Exist 
2.4.0 (0.37) 
 
 
 sw-pack-1 
Exist 
2.4.0 (0.37) 
21-06-2016 
 
 sw-pack-2 
Exist 
2.1.0 (0.53) 
17-05-2015 
 
Display Software File Information 
Displaying File Information Using the CLI 
 To display information on the software files: 
• 
At the file# prompt, enter:  
show sw-pack  
MiNID# file 
MiNID>file# show sw-pack 