# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 6.3 Management Access Control

*Manual `MiNID_ver_2_6_mn.pdf`, pages 117–122.*


## Applicability and Scaling  *(p.117)*


## Functional Description  *(p.117)*

6. Management and Security 
TACACS+ statistic counters are set to 0. 
 To clear TACACS+ statistics in the CLI: 
1. At the config>mngmnt>tacacsplus>server(<ip-address>)# prompt, type:  
clear-statistics. 
TACACS+ statistic counters are set to 0. 
6.3 Management Access Control 
You can enable or disable management access via either port ({SFP/MSA}/{1/2}). You cannot disable 
access for both ports simultaneously. In addition, you can configure access via 
HTTP/SNMP/SSH/Telnet/TFTP/SFTP applications. By disabling Telnet, SSH, or SNMP, you can prevent 
unauthorized access to the system when the security of the MiNID IP address has been compromised. 
By denying specific IP addresses or subnets, you can block unauthorized access to the system. 
Note 
To allow management, enable at least one protocol. 
Applicability and Scaling 
For loaned IP access, only four applications can be opened simultaneously out of six available 
applications (SNMP, TFTP/SFTP, SSH, Telnet, HTTP, and RPCAP). 
Functional Description 
Access via HTTP/SNMP/SSH/Telnet/TFTP/SFTP is configured according to the IP address mode 
configured in the router interface parameter settings: 
• 
If the IP address is configured statically or via DHCP, then the access can be enabled or disabled 
per access type (HTTP/SNMP/SSH/Telnet/TFTP/SFTP). If a management packet contains the 
standard TCP/UDP port number of an enabled access type, then it is processed by MiNID, 
otherwise it is discarded.  
• 
If the IP address is loaned from the host device, then in addition to specifying whether a 
particular access type is enabled, you also specify which TCP/UDP port number is used to 
indicate to MiNID whether to process the packet or forward it to the host device: 

## Factory Defaults  *(p.118)*


## Configuring Management Access  *(p.118)*

6. Management and Security 
 
Automatic – A predefined TCP/UDP port number is associated with the access type. The 
predefined TCP/UDP port numbers are: 
 
SNMP port – 58888 
 
TFTP/SFTP port – 58889 
 
Telnet port – 0 
 
SSH port – 58888 
 
HTTP port – 0 
 
Port number configured by user – You configure the TCP/UDP port number associated with 
the access type.  
If a management packet with a predefined/configured TCP/UDP port number associated with an 
enabled access type is received by MiNID, then the packet is processed by MiNID, otherwise it is 
forwarded to the host device.  
Access can be granted by authorization via a local or TACACS+ server. 
Factory Defaults 
By default, access to both ports and all applications (predefined TCP/UDP port in the case of loaned IP) is 
enabled. 
By default, SNMP read-only mode is disabled, which means that SNMP messages are available for 
reading and writing. 
For Loaned IP access, RPCAP mode is disabled by default. 
By default, authorization is performed via a local server; authorization via a TACACS+ server is disabled. 
Parameter 
Default Value 
auth-policy 
local 
wait-to-restore-auth-method 
No wait-to-restore-auth-method 
Configuring Management Access 
 To configure management access: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Management > Management Access: 
6. Management and Security 
MiNID 
  
 
 
 Configuration – System – Management - Management Access 
  
 
 
 MSA/Port 1 
 
Enable 
 SFP/Port 2 
 
Enable 
  
 
 
 SNMP Read Only 
 
Disable 
  
 
 
 Static IP/DHCP Access: 
 
 
 SNMP 
 
Enable 
 TFTP/SFTP 
 
Enable 
 SSH 
 
Enable 
 TELNET 
 
Enable 
 HTTP 
 
Enable 
  
 
 
 Loaned IP Access: 
 
 
 SNMP mode 
 
Auto 
 SNMP port 
 
58888 
 TFTP/SFTP mode 
 
Auto 
 TFTP/SFTP port 
 
58889 
 SSH mode 
 
Auto 
 SSH port 
 
58888 
 TELNET mode 
 
Auto 
 TELNET port 
 
0 
 HTTP mode 
 
Auto 
 HTTP port 
 
0 
 RPCAP mode 
 
Disabled 
 Authentication Policy 
 
 
 First Level 
Local 
Second Level 
none 
 Wait to restore auth 
method 
 
 
  
 
 
 Apply 
 
 
  
 
 
6. Management and Security 
a. Enable or Disable either of the ports. 
b. Enable or Disable SNMP read-only mode: 
 
Disable – SNMP is in the read-and-write mode 
 
Enable – SNMP is in the read-only mode 
c. According to the IP addressing mode configured in the host settings: 
 
Static IP or DHCP – Enable or disable each type of access 
 
Loaned IP – For each type of access, set the mode (and port if applicable) as follows: 
 
Disabled – Access is not allowed via this access type 
 
Auto –If a management packet is received by MiNID with a TCP/UDP port number that 
matches the predefined port for this access type, then the packet is processed by MiNID 
(see Functional Description for a list of the predefined TCP/UDP port numbers), 
otherwise the packet is forwarded to the host device. 
 
Port – If a management packet is received by MiNID with a TCP/UDP port number that 
matches the configured port number for this access type, then the packet is processed 
by MiNID, otherwise the packet is forwarded to the host device. 
Note 
RPCAP port can be configured only using Packet Capture configuration. Refer 
to the Packet Capture section in Chapter 11 for more details. 
d. Authentication Policy: 
 
First Level – authentication method that is applied first 
 
Second Level – authentication method that is applied after the first method 
e. Click <Apply> to implement the changes, and then click <Save Configuration>. 
• 
In the CLI: 
a. Go to the config>mngmnt>access level. 
b. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Setting the authentication 
policy 
auth-policy 1st-level {local|tacacs+} 
[2nd-level {local|tacacs+|none}] 
By default, only local authentication 
is set. 
See Authentication via TACACS+ 
Server 
Setting the time period for the 
previously failed method to be 
restored  
wait-to-restore-auth-method <seconds> 
 
Enabling or disabling MSA port 
msa 
Use no msa to disable the port 
Enabling or disabling SFP port 
sfp 
Use no sfp to disable the port 
6. Management and Security 
Task 
Command 
Comments 
Enabling or disabling SNMP 
read-only mode 
[no] snmp-read-only 
 
Commands in level config>mngmnt>access>static-ip-access, to be used when loaned IP is not enabled in the host 
settings 
Enabling access for the various 
access types  
snmp  
tftp  
ssh  
telnet  
http 
The tftp command configures access 
for TFTP/SFTP 
Disabling access for the various 
access types  
no snmp  
no tftp  
no ssh  
no telnet  
no http 
The tftp command configures access 
for TFTP/SFTP 
6. Management and Security 
Task 
Command 
Comments 
Commands in level config>mngmnt>access>loaned-ip-access, to be used when loaned IP is enabled in the 
management router interface settings 
Enabling access for the various 
access types and specifying 
predefined or configured 
TCP/UDP port number  
snmp loaned-ip {auto|port} <port-num> 
tftp loaned-ip {auto|port} <port-num> 
ssh loaned-ip {auto|port} <port-num> 
telnet loaned-ip {auto|port} 
<port-num> 
http loaned-ip {auto|port} <port-num> 
rpcap loaned-ip {auto} 
• auto – If a management packet is 
received by MiNID with a 
TCP/UDP port number that 
matches the predefined port for 
this access type, then the packet 
is processed by MiNID (see 
Functional Description for a list 
of the predefined TCP/UDP port 
numbers), otherwise the packet 
is forwarded to the host device. 
In this case, you do not specify 
the <port-num> parameter 
• port – If a management packet is 
received by MiNID with a 
TCP/UDP port number that 
matches <port-num>, then the 
packet is processed by MiNID, 
otherwise the packet is 
forwarded to the host device. 
Note: The tftp command configures 
access for TFTP/SFTP. 
 
Disabling access for the various 
access types 
no snmp  
no tftp  
no ssh  
no telnet  
no http 
no rpcap 
Note: The tftp command configures 
access for TFTP/SFTP. 
 