# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 3.4 Working with Custom Configuration Files

*Manual `MiNID_ver_2_6_mn.pdf`, pages 60–61.*


## Loading Sequence  *(p.60)*

3. Operation 
• 
sw-pack-1 or sw-pack-2 – Contains application software. One of the software packs is 
designated as active.  
Loading Sequence 
At startup, the device attempts to load configuration files in the following sequence until a valid one is 
found: 
• 
startup-config 
• 
user-default-config 
• 
factory-default-config 
If an error is encountered while loading a file, MiNID stops loading that file, sends an event to indicate 
the error, and then looks for the next file in the sequence. 
To display MiNID  parameter values after startup, use the info command. 
3.4 Working with Custom Configuration Files 
In large deployments, often a central network administrator sends configuration files to the remote 
locations and all that remains for the local technician to do is to replace the IP address in the file or 
other similar minor changes, and then download the file to the device. Alternatively, the technician can 
download the file as is to the device, log in to the device and make the required changes, then save the 
configuration. 
To download the configuration file, use the copy command (refer to Administration). After downloading 
the configuration file, the unit must be reset in order to execute the file. After the unit completes its 
startup, the custom configuration is complete. 
If you have an appropriate existing MiNID  configuration file, you can use Zero Touch provisioning (see 
On-net Zero Touch Provisioning) to have the configuration file automatically fetched by all your  MiNID 
devices. Otherwise, you need to manually configure all your  MiNID devices with any additional 
non-default settings. 
There is no startup sequence other than Zero Touch, if enabled (see On-net Zero Touch Provisioning for 
further details). 

## On-net Zero Touch Provisioning  *(p.61)*

3. Operation 
On-net Zero Touch Provisioning 
Zero Touch provisioning allows  MiNID to acquire an IP address from a DHCP server and fetch 
configuration files from a TFTP server, eliminating the need to manually log into  MiNID to provision it.  
Zero Touch provisioning is enabled by configuring the following: 
• 
DHCP must be enabled (DHCP in menu Configuration > System > Management > Host IP; dhcp in 
level config>mngmt>host) 
• 
If the user management traffic is via a specific VLAN, the management VLAN must be configured 
(Host VLAN, Host VLAN ID, and Host VLAN Priority in menu Configuration > System > 
Management > Host IP; vlan-id and vlan-pbits in level config>mngmt>host). 
 
Note 
Zero touch must be enabled (Zero Touch in menu Configuration > System > 
Management > Zero Touch; zero-touch in level config>mngmt>host), 
however this is the default setting. 
 
Prerequisites 
• 
A DHCP server for providing the TFTP server address and configuration file information, in 
addition to the usual IP address, default gateway, etc. 
• 
A TFTP server with a configuration file, consisting of valid CLI commands. 
Sequence 
At reboot, when MiNID obtains a DHCP lease from the DHCP server, the lease provides the TFTP server 
address, either via option 150, or as a string (‘xxx.xxx.xxx.xxx’) via option 66. The DHCP lease provides 
the path and file name of the configuration file via DHCP option 67, if zero touch is to be used. 
1. If the lease specified a configuration file, MiNID  loads the configuration file from the TFTP 
server. If no configuration file was specified, the zero touch process does not start.  
2. If the TFTP download fails,  MiNID does the following: 
a. Send the trap systemDownloadEnd (with failed indication) to any configured network 
managers 
b. Start a 10-minute timer. 
c. When the timer expires,  MiNID attempts again to download the configuration file.  
3. If the configuration file is received successfully from the TFTP server,  MiNID  does the following: 