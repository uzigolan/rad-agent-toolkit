# 6 Management and Security

*Manual `MiNID_ver_2_6_mn.pdf`, pages 101–137.*


## 6.1 Access Control List  *(p.101)*

6.1 Access Control List 
Access control lists are used to flexibly filter incoming management traffic by the source IP address. 
Applicability and Scaling 
A single access group list can be configured per device. 
Standards Compliance 
Relevant sections of RFC 1812. 
Benefits 
The service providers use the ACLs to maintain the network security by preventing the malicious traffic 
from entering the device. The ACLs can be used to save the network resources by dropping the 
unwanted packets.  
Functional Description 
Devices featuring ACLs can flexibly filter management traffic, by denying or permitting IP packets to 
enter or exit entities in the device, according to the packet’s IP address and mask. 
ACL entries are sequentially numbered rules containing statements (Deny or Permit). 
Packets are permitted or denied access, based on the following conditions: 
• 
IP source 
6. Management and Security 
• 
Mask 
For the ACL to take effect, it must be enabled using the configure access-control command in CLI or via 
Configuration>System> Management>Access Control page in the web interface. 
When ACL is enabled, by default, MiNID denies any management packet, unless there is a matching rule 
that permits the source IP address of the packet. 
Note 
• 
Working with ACL and IPv6, you must create a permit rule for the Link 
Local IP in addition to the Global IP address. 
• 
You have to add rules to permit IP addresses of any server that 
communicates with MiNID (RADview, NTP, etc.) for proper operation, 
otherwise the traffic from these servers will be blocked by ACL. 
Factory Defaults 
By default, no access list is defined on the MiNID. 
Configuring ACL Using the Web Interface 
 To configure ACL: 
1. Navigate to Configuration > System > Management > Access Control. 
2. In the New ACL Name field, type the ACL name. 
MiNID 
  
 
 
 Configuration – System – Management – Access Control 
  
 
 
 New ACL Name 
 
AccesMng 
  
 
 
 Apply 
 
 
  
 
 
 ACL Name 
 
 
  
 
  
3. Click <Apply>. 
6. Management and Security 
4. In the table, click the ACL name to configure the list. 
The ACL Configuration page opens. 
 MiNID 
  
 
 
 Configuration – System – Management – Access Control – Config 
ACL AccessMng 
  
 
 
 Action Permit IP-net 
0.0.0.0. /32 
Sequence 10 
Add 
 
  
 
 
 Access list records 
 
 
 Sequence # 
Action 
IP net 
 
  
 
 
 Activate 
Disable 
 
  
 
 
 Apply 
 
 
  
 
 
 
5. Create the access list: 
a. Select the desired action: Deny/Permit. 
b. In the IP-net field, type the IP address and mask (the default mask is 32). 
c. Click <Add>. 
The item is added to the Access list records table. 
6. In the Activate field, select Enable to activate the ACL.  
7. Click <Apply>. 
Configuring ACL Using the CLI 
The ACL configuration tasks are performed at the access control and management levels. 
 To configure ACL: 
1. Configure the ACL using the commands listed in the table below: 
Task 
Command 
Comments 
Create ACL name 
access-list <acl-name> 
 

## 6.2 Authentication via TACACS+ Server  *(p.104)*

6. Management and Security 
Task 
Command 
Comments 
Add statements to the list 
permit ip <source-IP>/ <src-
prefix-length> <sequence-number>  
• In this step you can configure 
the IP address/mask and the 
sequence number. 
• A mask and sequence number 
are automatically assigned if 
none are configured. 
• You can either “permit” or 
“deny” a source IP 
• The sequence number is 
generated automatically if not 
configured. 
Delete a statement from the 
ACL 
delete <sequencce-number> 
 
Attach access list to 
management 
config>management>access>[no] 
access-group <acl-name> 
 
Example: 
MiNID>config>access-control# access-list accessmng 
MiNID>config>access-control# access-list (accessmng)# permit ip 168.15.168.5/32  
Config>management>access> access-group <accessmng> 
 
MiNID>config>access-control# access-list accessoki 
MiNID>config>access-control# access-list (accessokig)# deny ip 168.15.169.5/32  
Config>management>access> access-group <accessoki> 
 
6.2 Authentication via TACACS+ Server 
TACACS+ (Terminal Access Controller Access Control System Plus) is a security application that provides 
access control for routers, network access servers, and other networked computing devices via one or 
more centralized servers. TACACS+ provides separate authentication, authorization, and accounting 
services. It is used to communicate between MiNID and an authentication database. Because TACACS+ is 
based on TCP, implementations are typically resilient against packet loss. 
6. Management and Security 
Applicability and Scaling 
Authentication with TACACS+ is applicable to all MiNID devices. 
MiNID supports up to five accounting groups, with up to five TACACS+ servers. Each TACACS+ server can 
be bound to a single accounting group only. 
Standards Compliance 
TACACS+ Protocol Version 1.78 (IETF draft-grant-tacacs-02) 
Benefits 
The TACACS+ protocol allows centralized authentication and access control, avoiding the need to 
maintain a local user data base on each device on the network. The TACACS+ server encrypts the entire 
body of the packet but leaves a standard TACACS+ header. 
Functional Description 
TACACS+ is a protocol that provides access control for routers, network access servers and other 
networked computing devices via one or more centralized servers. TACACS+ is based on AAA model: 
• 
Authentication – The action of determining identity of a user. 
• 
Authorization – The action of determining what a user is allowed to do. It can be used to 
customize the service for the particular user.  
• 
Accounting – The action of recording what a user is doing, and/or has done. 
The TACACS+ client can be configured to use authentication/authorization functionality, accounting 
functionality, or both. 
Components 
The TACACS+ remote access environment has three major components: access client, TACACS+ client, 
and TACACS+ server.  
• 
The access client is an entity which seeks the services offered by the network.  
6. Management and Security 
• 
TACACS+ client, running on MiNID, processes the requests from the access client and passes this 
data to TACACS+ server for authentication.  
• 
The TACACS+ server authenticates the request, and authorizes services over the connection. The 
TACACS+ server does this by matching data from the TACACS+ client’s request with entries in a 
trusted database. 
TACACS+ server decides whether to accept or reject the user's authentication or authorization. Based on 
this response from the TACACS+ server, the TACACS+ client decides whether to establish the user's 
connection or terminate the user's connection attempt. The TACACS+ client also sends accounting data 
to the TACACS+ server to record in a trusted database. 
TACACS+ uses TCP for its transport and encrypts the body of each packet. TACACS+ client and server can 
agree to use any port for authentication and accounting. TACACS+ supports authentication by using a 
user name and a fixed password. 
Accounting 
MiNID supports up to five accounting groups, with up to five TACACS+ servers. Each TACACS+ server can 
be bound to a single accounting group only. 
A group can be defined with its own accounting level: 
• 
Shell accounting, which logs the following events: 
 
Successful logon 
 
Logon failure 
 
Logoff 
 
Terminated management session 
• 
System accounting, which records system events/alarms registered in local log file 
• 
Command accounting, which logs the following events: 
 
Any command entered by the user and successfully executed by MiNID 
TACACS+ server log displays the exact commands as they were typed. 
Factory Defaults 
The following default values are defined: 
6. Management and Security 
Parameter 
Default Value 
privilege level 
su = 12, user = 3 
wait-to-restore-server 
0 
By default, no TACACS+ servers are defined. When the TACACS+ server is first defined, it is configured as 
shown below. 
Parameter 
Default Value 
administrative status 
shutdown 
accounting port  
49 
authentication-port 
49 
key 
empty string 
retry 
3 
timeout 
5 seconds 
 
Note 
When MiNID is set to the Config operation mode, authentication with 
TACACS+ server is disabled. 
Configuring Authentication via TACACS+ Server 
Configuring Access 
To configure the authentication method, refer to the Configuring Management Access section. 
Configuring Privilege Levels 
You can define custom authorization levels by mapping the TACACS+ levels (from 0 to 15) to MiNID user 
levels (user, su). 
6. Management and Security 
TACACS+ Privilege Levels 
Level 
User 
Allowed Actions 
Description 
3 
user 
Monitoring 
Commands that do not affect services, 
traffic, or configuration 
12 
su 
User management 
Commands that manage users in the 
database 
A user type can be mapped to multiple TACACS+ privilege levels, i.e. su can have level of 10, 12, and 15 
simultaneously. 
The TACACS+ privilege level should be mapped to only one user type. 
 To configure a custom privilege level in the web interface: 
1. Navigate to Configuration>System>Management>TACACS Plus. 
2. In the levels table, select the boxes with the desired authorization levels. 
3. Click <Apply>. 
 To delete a custom privilege level in the web interface: 
1. In the levels table, unselect the boxes that you do not need.  
2. Click <Apply>. 
 To configure a custom privilege level in the CLI: 
1. At the config>mngmnt>tacacsplus# prompt, enter privilege-level <tacacs-privilege-level> {su | 
user}. 
 To delete a custom privilege level in the CLI: 
1. At the config>mngmnt>tacacsplus# prompt, enter no privilege-level <tacacs-privilege-level> {su 
| user}. 
Note 
At least one privilege level must be assigned to the su user level. 
Configuring TACACS+ Servers 
MiNID provides connectivity to up to five TACACS+ authentication servers. You must specify the 
associated server IP address, key, number of retries, etc.  
6. Management and Security 
Note 
If you intend to use TACACS+ for authentication, verify that TACACS+ is 
selected as level-1 authentication method (refer to the Management Access 
Control section). 
 To configure a TACACS+ server in the web interface: 
1. Navigate to Configuration>System>Management>TACACS Plus as shown below. 
MiNID 
 
 
 
 
 
Configuration>System>Management>Server 
 
 
 
 
 
Wait To Restore Server 
0 
 
 
 
 
 
 
CLI Level/TACACS+ Level 
0 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
11 
12 
13 
14 
15  
 
SU 
 
 
 
 
 
 
 
 
 
 
 
 
v 
 
 
 
 
 
USER 
 
 
 
v  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Apply 
 
 
 
 
 
 
 
Add New Group 
 
 
 
Group Name 
 
 
 
Add New Server 
 
 
 
Server IP 
Admin Status 
 
 
 
1.1.1.1 
Active 
Remove 
 
 
 
10.10.10.10 
Not Active 
Remove 
 
 
 
1.1.14.1 
Active 
Remove 
 
 
 
 
 
 
TACACS+ Levels Configuration 
1. For a new server, click Add New Server.  
The TACACS+ server configuration page is displayed. 
6. Management and Security 
MiNID 
  
 
 
 Configuration>System>Management>TACACS Plus>New Server 
  
 
 
 IP Address 
0.0.0.0 
 
 Accounting Port 
49 
 
 Authentication Port 
49 
 
 Group 
None 
 
 Key 
 
 
 Retry 
3 
 
 Timeout[s] 
5 
 
 Admin Status 
Disable 
 
  
 
 
 Apply 
 
 
  
 
 
2. Enter the IP Address (IPv4 or IPv6) of the server.  
3. Enter the rest of the parameters according to the tasks listed in the table below. 
4. Click <Apply>. 
 To configure a TACACS+ server in the CLI: 
1. At the config>mngmnt>tacacsplus# prompt, type server <ip-address> to specify the server IP 
address. 
The config>mngmnt>tacacsplus>server(<ip-address>)# prompt is displayed. 
2. Enter the necessary commands according to the tasks listed below. 
TACACS+ Server Configuration Parameters 
Task 
Command 
Comments 
Defining the TCP port to be used for 
accounting 
accounting-port <port-number> 
Possible values: 1–65535 
Defining the TCP port to be used for 
authentication  
authentication-port <port-number> Possible values: 1–65535 
Binding server to a group 
[no] group <group-name> 
6. Management and Security 
Task 
Command 
Comments 
Defining a non-disclosed string 
(shared secret) used to encrypt the 
user password 
key <string> [hash] 
The shared secret is a secret key 
consisting of free text known to the 
client and the server for encryption. 
The hash keyword denotes that the 
string is hashed, rather than clear text; 
usually it is added by the device after 
hashing the clear text that the user 
enters, before saving it in the database. 
If you enter the password as a text 
string, do not use the hash parameter. 
Use it only if you are specifying the 
password as a hashed value (obtained 
by using the info command to display 
TACACS+ data). 
Note: In the web interface, you can only
enter a text string. Any hashed string is 
interpreted as plain text. 
Defining the number of recurrent 
authentication request attempts 
retry <number-of-retries> 
Possible values: 1–10 
Defining the time period (in 
seconds) between two requests to 
the TACACS+ server 
timeout <seconds> 
Possible values: 1–255 
Note: TACACS+ server reply is expected 
within 1 second. 
Administratively enabling server 
no shutdown 
shutdown administratively disables the 
server 
Displaying statistics 
show statistics 
Clearing statistics 
clear-statistics 
Sometimes, TACACS+ server doesn’t reply, so another server should be connected. You can define how 
much time MiNID should wait before trying the non-replying server again. 
 To define the time to wait for the server restoration: 
1. At the config>mngmnt>tacacsplus# prompt, type wait-to-restore <seconds> to define the 
period of time in seconds. 
6. Management and Security 
Configuring Accounting Groups 
 To configure accounting groups in the web interface: 
1. Navigate to Configuration>System>Management>TACACS Plus. 
2. For a new group, click Add New Group.  
The group configuration page is displayed. 
MiNID 
  
 
 
 Configuration>System>Management>TACACS Plus>New Group 
  
 
 
 Group Name 
Group1 
 
 Accounting Shell 
Disable 
 
 Accounting System 
Disable 
 
 Accounting Commands 
Disable 
 
  
 
 
 Apply 
 
 
  
 
 
1. Set the Enable/Disable status for each accounting profile. 
2. Click <Apply>. 
3. Click <Back> to edit the server parameters. 
4. Click the server name. 
5. In the Group list, choose the desired group name to bind the group to the TACACS+ server. 
6. Click <Apply>. 
 To configure accounting groups in the CLI: 
1. At the config>mngmnt>tacacsplus# prompt, type group <group-name> to configure an 
accounting group with the specified name.  
The config>mngmnt>tacacsplus>group(<group-name>)# prompt is displayed.  
2. To define the accounting for the group, enter:  
accounting [shell] [system] [commands] 
6. Management and Security 
Note 
• 
You can enter any combination of the parameters shell, system, or 
commands, but you must enter at least one of them 
• 
Type no accounting to disable TACACS+ accounting for the group. 
 
3. Type exit to return to the TACACS+ level. 
The config>mngmnt>tacacsplus# prompt is displayed. 
4. Type server <ip-address> to select the TACACS+ server to which to bind the group. 
The config>mngmnt>tacacsplus>server(<ip-address>)# prompt is displayed.  
5. At the config>mngmnt>tacacsplus>server(<ip-address>)# prompt, enter group < group-name> 
to bind the previously defined accounting group to the TACACS+ server. 
Examples 
Defining Server 
The example below illustrates the procedure for defining a TACACS+ server. 
• 
Server IP address: 175.18.172.150 
• 
Key: TAC_server1 
exit all  
configure management tacacsplus 
  server 175.18.172.150 
    key TAC_server1 
    no shutdown 
exit all 
save 
 To display the configuration from the above example: 
# configure management tacacsplus server 175.18.172.150 
>config>mngmnt>tacacsplus>server(175.18.172.150)# info 
    authentication-port 49 
    key 244055BF667B8F89225048C6571135EF hash 
    retry 3 
    timeout 5 
        no shutdown 
6. Management and Security 
Defining Accounting Group 
The example below illustrates the procedure for defining an accounting group. 
• 
Group name: TAC1 
• 
Accounting: Shell, system, and commands 
• 
Bound to server defined in Defining Server. 
exit all 
configure management tacacsplus 
  group TAC1 
    accounting shell system commands 
    exit 
  server 175.18.172.150 
    group TAC1 
exit all 
 To display the configuration from the above example: 
# configure management tacacsplus server 175.18.172.150 
>config>mngmnt>tacacsplus>server(175.18.172.150)# info 
    key "244055BF667B8F89829AB8AB0FE50885" hash 
    retry 1 
    timeout 5 
    authentication-port 49 
    accounting-port 49 
    group "TAC1" 
    no shutdown 
Viewing TACACS+ Statistics 
Information presented by statistic counters refers only to authentication, not to authorization. 
 To display TACACS+ statistics in the web interface: 
1. Navigate to Configuration>System>Management>TACACS Plus. 
2. Click the IP address of the server. 
The TACACS+ server update page is displayed. 
6. Management and Security 
MiNID 
  
 
 
 Configuration>System>Management>TACACS Plus>Update Server 
  
 
 
 Statistics 
 
 
 IP Address 
175.18.172.150 
 
 Authentication Port 
49 
 
 Key 
244055BF667B8F89225048C6571135EF  
 Retry 
3 
 
 Timeout[s] 
5 
 
 Admin Status 
Enable 
 
  
 
 
 Apply 
 
 
  
 
 
3. Click Statistics. 
The TACACS+ server statistics page is displayed. For statistics counters description, refer to the 
table below. 
 
  
 
 
 Configuration>System>Management>TACACS Plus>Statistics 
  
 
 
 Requests 
5 
 
 Request Timeouts 
60 
 
 Unexpected Responses 
12 
 
 Server Error Responses 
2 
 
 Incorrect Responses 
3 
 
 Transaction Successes 
256 
 
 Transaction Failures 
5 
 
 Pending Requests 
1 
 
  
 
 
 Clear Statistics 
 
 
  
 
 
TACACS+ Server Statistics 
6. Management and Security 
 To display TACACS+ statistics in the CLI: 
• 
At the config>mngmnt>tacacsplus>server(<ip-address>)# prompt, type: 
show statistics. 
The TACACS+ statistic counters are displayed.  
>config>mngmnt>tacacsplus>server(175.18.172.150)# show statistics 
Requests               5 
Request Timeouts       60 
Unexpected Responses   12 
Server Error Responses 2 
Incorrect Responses    3 
Transaction Successes  256 
Transaction Failures   5 
Pending Requests       1 
TACACS+ Statistic Counters 
Counter 
Description 
Requests 
Number of authentications performed toward a specific TACACS+ server 
Request Timeouts 
Number of transaction timeouts that occurred between the client and 
server 
Unexpected Responses 
Number of times the TACACS+ client receives a TACACS+ packet that is not 
expected at that time. Usually, this occurs due to a delayed response to a 
request that has already timed out 
Server Error Responses 
Number of errors received from the TACACS+ server 
Incorrect Responses 
Number of times the TACACS+ client: 
• Fails to decrypt the packet  
• Detects an invalid field in the TACACS+ packet  
• Receives a response that is not valid according to the initial request 
Transaction Successes 
Number of successful transactions between the client and TACACS+ server 
Transaction Failures 
Number of times the TACACS+ client’s request is aborted by the TACACS+ 
server or the server fails to respond after maximum retry is exceeded 
Pending Requests 
Number of TACACS+ client’s requests minus number of TACACS+ server 
responses or timeouts 
 To clear TACACS+ statistics in the web interface: 
1. Navigate to Configuration>System>Management>TACACS Plus>Statistics as shown on the above 
figure. 
2. Click Clear Statistics. 

## 6.3 Management Access Control  *(p.117)*

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
 

## 6.4 Network Managers  *(p.123)*

6. Management and Security 
6.4 Network Managers 
You can define up to two network managers to receive alarms/events/traps from MiNID. 
Factory Defaults 
By default, no SNMP Managers are configured (both manager IP addresses are set to 0.0.0.0). 
Configuring Network Managers 
 To define network managers: 
Do one of the following: 
• 
In the web interface, go to Configuration> System > Management > Manager List, enter one or 
two IP addresses of network manager servers, and click <Apply> to implement the changes, and 
then click <Save Configuration>: 
MiNID 
  
 
 
 Configuration – System- Management - Manager List 
  
 
 
 Manager1  
192.168.42.248 
 Manager2  
10.10.36.61 
  
 
 
 
Network Managers 
• 
In the CLI, go to the config>mngmt level, and enter manager <IP address>. 
You can do this twice to have two network managers. To remove a specific manager, enter no 
manager <IP address>. 

## 6.5 Router Interface  *(p.124)*

6. Management and Security 
6.5 Router Interface 
MiNID supports up to five router interfaces. 
Management traffic is transmitted via the router interface number 1 based on the configured IP address, 
static route and mask. 
The router interface can be set with VLAN parameters, which will be added as a VLAN tag to the traffic 
transmitted via this interface. 
Note 
If VLAN is not configured, traffic is transmitted untagged. 
Functional Description 
You can define the IP address as: 
• 
DHCP – MiNID receives its IP address from a DHCP server for management router interface 
Note 
If DHCP is enabled, option 61 (client identifier) is supported by sending the 
device MAC address to the DHCP server. 
• 
Static – A specific IP address is configured for MiNID that is used for all types of access 
• 
Loaned IP – MiNID uses the IP address of the host device. When packets arrive at MiNID, the 
packets are forwarded to the host device or are processed by MiNID, depending on the packet 
TCP/UDP port number (see Management Access Control for details).  
The loaned IP feature allows a network management system such as RADview to communicate 
with MiNID and the MiNID host device by sending management packets to the same IP address 
but with different TCP/UDP port values, according to which packets should be processed by 
MiNID and which should be forwarded to its host device. 
Note 
If loaned IP address is enabled, TWAMP, Packet Capture and L3SAT 
configurations based on Router Interface # 1 cannot be enabled. However, 
TWAMP, Packet Capture and L3SAT configurations based on another router 
interface can be successfully enabled. 
 
Note 
For loaned IP configuration having EtherType other than 0x8100, the 
EtherType should be defined specifically by config flows tpid-outer-vlan 
command. 
 
6. Management and Security 
 
 
Factory Defaults 
 IP address is statically configured to 192.168.205.1. 
No management VLAN is configured. 
By default, only the router interface #1, which includes additional functionality for host management, is 
defined. No additional router interface is defined. 
By default, IPv6 address is disabled. 
Configuring Router Interface 
 To configure a router interface using the web interface: 
1. Navigate to Configuration > Router > Interface. 
 
 
 
  
 
 
 
 
Configuration – Router - Interface 
 
 
 
Add new Interface 
 
 
 
ID 
Admin Status 
Interface IP 
 
 
 
 
 
1 
Enabled 
192.168.205.1/24 
Delete Interface 
 
 
 
 
 
Configuring a Router Interface 
1. To add a new router interface: 
 
Click Add new Interface. 
6. Management and Security 
 
 
 
 
 
Configuration – Router – Interface - New Interface 
 
 
 
 
Admin Status 
Disable 
 
 
Interface ID 
2 
 
 
IPv4 Address 
0.0.0.0 
 
 
Network Mask 
0.0.0.0 
 
 
Interface Vlan 
Untagged 
 
 
Port 
Port 1 
 
 
 
 
Apply 
 
 
 
 
 
New Router Interface 
 
Fill in the parameters as specified in the following table. 
 
Click <Apply> to create the router interface. 
The Configuration>Router>Interface screen (see above) appears, with an entry containing the 
new router interface. 
1. To delete a router interface, click Delete Interface in the corresponding row. 
The router interface is deleted. 
2. Click <Save Configuration>. 
 To configure a router interface using the CLI: 
1. Navigate to configure router interface <number>. 
The config>router>interface<number>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Router Interface Parameters 
Task 
Command 
Comments 
Assigning an IP address to the 
router interface 
address <ip-address/mask> 
The controller should have the same IP 
address as in the router interface 
Associating router interface 
with VLAN 
[no] vlan <vlan-id> pbit <p-bit> [inner-bit 
<vlan-id> inner-pbit <p-bit>] 
 
6. Management and Security 
Task 
Command 
Comments 
Binding router to Ethernet port  
bind ethernet <1|2> or <SFP|MSA> 
For Router Interfaces 2-5, you can bind 
the router to either SFP or MSA port. 
For Router Interface 1, you can bind the 
router to both. 
Administratively enabling or 
disabling the router 
[no] shutdown 
Enter shutdown to administratively 
disable the router 
 To disable a router interface: 
1. Go to configure router interface <number>. 
2. Type shutdown. 
Configuring Router Interface for Management 
 To configure the router interface in the web interface: 
1. Navigate to the Configuration > Router > Interface. 
2. Click 1 in the row of the default router interface to change its parameters.  
6. Management and Security 
 
 Configuration – Router – Interface - Update Management Interface 
  
 
 
 IPv4 Configuration: 
 
 
 IP addressing mode 
Static IP 
 
 IP Address 
192.168.205.1 
 
 Network Mask 
255.255.255.0 
 
  
 
 
 IPv6 Configuration: 
 
 
 Static Address 
Disable 
 
 Autoconfig 
Disable 
 
 DHCPv6-Client 
Disable 
 
  
 
 
 General Configuration: 
 
 
 Bind 
Both 
 
 Host VLAN 
Untagged 
 
  
 
 
 Apply  
 
 
  
 
 
Management Router Interface Configuration 
1. Enter all necessary commands according to the tasks listed in the table below. 
2. Click <Apply>. 
 To configure the router interface for management in the CLI: 
Do one of the following: 
1. Use a unified command: 
a. Go to the config>router level. 
b. Enter management configuration parameters: 
management-cfg {router-interface} <ri-number> {address} <ri-ip-address-mask> [vlan 
<value> pbit <value> [inner-vlan <value> inner-pbit <value>]] {static-route} <dest-subnet> 
{address} <next-hop ip address> 
2. Use a set of commands according to the tasks listed below. 
6. Management and Security 
Router Interface for Management 
Task 
Command 
Comments 
Configuring the IP address, 
if DHCP is not enabled 
[no] address <ip-address/mask> 
Specify the mask in CIDR notation, which 
means that it is a decimal number that 
specifies the number of high-order 
consecutive bits set to 1 in the mask. For 
example, the CIDR notation for mask 
255.255.255.0, is 24. 
For router interface #1, the IP address can 
have IPv4 (e.g. 10.10.10.1) or IPv6 format 
(e.g. 10:10:10:10:10:10:10:10). 
• Note: Only IPv6 address can be deleted 
by entering no address in the router 
interface # 1. 
Binding router to Ethernet 
port 
bind ethernet {1} {2} 
 
Enabling or disabling DHCP 
[no] dhcp 
Use the no form to disable the mode (for 
management interface) 
You cannot enable DHCP (for IPv4) in the 
following cases: 
• Router interface is bound to a PPP 
port. 
• IPv4 address is configured. 
• Router interface is not unnumbered. 
DHCPv6 is enabled. 
Enabling or disabling 
DHCPv6 client for the router 
interface 
[no] dhcpv6-client 
You can enable DHCPv6 client provided 
that the following conditions exist: 
• Router entity is Router # 1. 
• There is no other DHCPv6 client 
defined in the device. 
DHCPv4 is not enabled. 
Enabling or disabling IPv6 
autoconfiguration on the 
router interface 
[no] ipv6-autoconfig  
Enter no ipv6-autoconfig to disable IPv6 
autoconfiguration. 
Enabling or disabling loaned 
IP address mode 
[no] loaned-ip 
Use the no form to disable the mode. 
If loaned IP address is enabled, then DHCP 
cannot be enabled. 
6. Management and Security 
Task 
Command 
Comments 
Displaying router interface 
status 
show status 
See Viewing Router Interface Status 
Creating a management 
traffic VLAN by configuring 
the management VLAN ID 
and specifying its priority by 
setting the VLAN p-bits 
[no] vlan <vlan-id> pbit <p-bit> 
[inner-vlan <vlan-id> inner-pbit <p-
bit>] 
Possible values for pbit: 0–7 
 
Note 
IPv6 autoconfiguration must be enabled before you start configuring static 
address and DHCPv6 client. 
 
Note 
Router Interface parameters cannot be changed if the interface is used for 
configuring TWAMP, Packet Capture, or L3SAT parameters. 
Configuring Static Route 
 To configure the static route in the web interface: 
1. Navigate to Configuration > Router > Static Route. 
2. Click Add new Static Route. 
 
 Configuration – Router - Static Route - New Static Route 
  
 
 
 IP Address 
0.0.0.0 
 
 Subnet Mask 
0.0.0.0 
 
 Next Hop Address 
0.0.0.0 
 
 Apply  
 
 
  
 
 
1. Set the parameters and click <Apply>. 
 To configure the static route in the CLI: 
1. Go to the config>router level. 
6. Management and Security 
2. Type static-route <ip-address/mask> address <next-hop-ip-address>.  
You can define two separate entities for IPv4 and IPv6 default gateway. 
Configuring Default Gateway 
The default gateway can be configured, if DHCP is not enabled. You can set two separate entries: one for 
IPv4 address and another for IPv6 address. 
 To configure the default gateway in the web interface: 
1. Navigate to Configuration > Router > Static Route. 
MiNID 
 Configuration – Router - Static Route 
  
 
 
 Add new Static Route 
 
 
  
 
 
 
Static Route IP 
Network 
Mask 
Next Hop IP 
 
 
 
0.0.0.0/0 
0 
0.0.0.0 
Delete Static 
Route 
 
 
::/0 
0 
:: 
Delete Static 
Route 
 
  
 
 
1. In the Next Hop IP column, click the 0.0.0.0 entry to edit the IPv4 default gateway, or the :: 
entry, to edit the IPv6 default router. 
2. Enter the default gateway address and click Apply. 
 To configure the default gateway in the CLI: 
1. Go to the config>router level. 
2. For IPv4 default gateway, type static-route 0.0.0.0/0 address <next-hop-ip-address>. 
For IPv6 default router, type static-route 0::0/0 address <next-hop-ip-address>. 
6. Management and Security 
Viewing the Configured Router Interface Parameters 
 To view the configured router interface parameters in the web interface: 
1. Navigate to Configuration > Router > Interface. 
2. In the row of the router interface 1, click 1. 
The router interface parameters are displayed. 
 To view the configured router interface parameters in the CLI: 
1. Go to the config>router level. 
2. Type info. 
interface 1 
 
ipv6-autoconfig 
 
address 192.168.205.11/24 
 
no vlan 
 
bind ethernet sfp msa 
 
no dhcp 
 
no loaned-ip 
 
no dhcpv6-client 
exit 
static-route 0.0.0.0/0 address 192.168.205.11 
static-route 0::0/0 address :: 
Viewing Router Interface Status 
You can view the router interface status by using the show status command:  
config>router>interface(<interface-num>)>show status. 
 To display the router interface status in the web interface: 
1. Navigate to Configuration > Router > Interface and click the interface row in the table. 
 To display the router interface status in the CLI: 
MiNID>config>router>interface(1)# show status 
Admin: up           Oper: Up 
IP Addresses: 
  101.101.101.1/24                            (manual)            (preferred) 
  1234:1234:1234:1234:1234:1234:1234:1234/126 (auto-configuration)(preferred) 
  FE80::220:D2FF:FE12:3456/64                 (link layer)        (preferred) 
 
IPv4 Default Router:  1.1.1.254 
IPv6 Default Router:  FE80::2AC7:CEFF:FEF4:68C4 
6. Management and Security 
The above fields are: 
Router Interface Status Parameters 
Field 
Description 
Admin 
Administrative status: 
• up – ready to pass packets 
• down  
Oper 
Operational status: 
• up – ready to pass packets 
• down  
IP Addresses 
IP Address/prefix 
length 
IPv4 or IPv6 address and prefix length  
Note: Supported for DHCPv6 
origin 
Origin of the IP address. 
Possible origins are:  
• other 
• manual 
• DHCP 
• link layer 
• random 
status 
Status of the IP address. 
Available statuses (from the IPv6 Stateless Address Autoconfiguration 
protocol) are: 
• preferred (default) 
• deprecated 
• invalid 
• inaccessible 
• unknown 
• tentative 
• duplicate 
• optimistic 
IPv4 Default Router 
IP address of the IPv4 default router 
IPv6 Default Router 
IP address of the IPv6 default router 

## 6.6 Session Timeout  *(p.134)*


## 6.7 SNMP Communities  *(p.134)*

6. Management and Security 
6.6 Session Timeout 
Both management interfaces (web and CLI) disconnect the user session after a configurable time period 
without user action. The timeout value is a whole number of minutes in the range 1–60. 
Factory Default 
The default timeout is 5 minutes. 
Configuring the Session Timeout 
 To configure the session timeout: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Management > Management Timeout, set 
the Timeout and click <Apply> to implement the changes, and then click <Save Configuration>: 
MiNID 
  
 
 
 Configuration>System>Management>Management Timeout 
  
 
 
 Timeout 
(Min.) 
 
5 
  
 
 
 
• 
In the CLI, go to the config>mngmnt level, and enter timeout <minutes>. 
6.7 SNMP Communities 
You can configure the names for the read-only, read/write, and trap communities used for SNMPv1/v2 
access. 

## 6.8 User Access  *(p.135)*

6. Management and Security 
 To configure the SNMP communities: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Management > SNMP 
MiNID 
  
 
 
 Configuration>System>Management>SNMP 
  
 
 
 Community Read/Write 
 
private 
 Community Read only 
 
public 
 Community Trap 
 
public 
  
 
 
SNMP Communities 
a. Set Community Read/Write to the name of a community with read/write authorization. 
b. Set Community Read only to the name of a community with read-only authorization. 
c. Set Community Trap to the name of a community for sending traps. 
d. Click <Apply> to implement the changes, and then click <Save Configuration>. 
• 
In the CLI, go to the config>mngmnt>snmp level, and enter the following command: 
snmp community {rw|ronly|trap} <name> 
Where: 
 
rw – indicates configuring read/write community to <name> 
 
ronly – indicates configuring read-only community to <name> 
 
trap – indicates configuring trap community to <name>. 
6.8 User Access 
Two user accounts exist for both of the two configuration interfaces (web and CLI). The usernames are 
fixed: 
• 
su: Superuser account with permission for all configuration. 
• 
user: Read-only user. Can view all current configuration. 
6. Management and Security 
The initial password for both accounts is: 1234. For better security, change the password as explained 
below. 
Up to four user sessions are accepted by the device at any one time. It is recommended not to exceed 
one web session at a time, which means that you can have one web session and three more CLI sessions 
simultaneously. 
As the superuser (su), you can modify the username and password for both user accounts (su and user). 
As the read-only user, you cannot configure your password. The following procedure is for the superuser 
to change credentials. 
 To configure the user accounts: 
Do one of the following: 
• 
Use the web interface: 
a. In the web interface, go to Configuration> System > Management > User Access: 
The User access screen appears. If you are logged in as the superuser, you can change your 
password or the read-only user password. If you’re logged in as the read-only user, you cannot 
modify any parameters. 
MiNID 
  
 
 
 Configuration>System>Management>User Access 
  
 
 
 User Level 
 
Super User 
 User Name 
 
su 
 Old Password  
 
**** 
 New Password  
 
 
 Confirm New 
Password 
 
 
  
 
 
 
User Access – Logged In as Superuser 
6. Management and Security 
MiNID 
  
 
 
 Configuration>System>Management>User Access 
  
 
 
 User Level 
 
User 
 User Name 
 
user 
  
 
 
 
User Access – Logged In as Read-Only User 
b. In User Level, select Super User or User, according to which user credentials you wish to 
configure. 
c. Define the User Name. 
d. Type the Old Password, type the New Password and Confirm it. 
e. Click <Apply> to implement the changes, and then click <Save Configuration>. 
• 
Use the CLI: 
a. Log into the CLI as the superuser, and go to the config>mngmnt level. 
b. To define the username and password of the superuser, enter: 
user <new username> level su password <new password> 
c. To define the username and password of the regular user, enter: 
user <new username> level user password <new password> 
If you’re logged in as the read-only user (not the superuser), the command user is not 
available. 
Note 
Make sure not to assign the same username to the super user and the 
read-only user. 
 
You can view the current usernames by going to the config>mngmnt level and entering show users. 