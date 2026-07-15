# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 6.2 Authentication via TACACS+ Server

*Manual `MiNID_ver_2_6_mn.pdf`, pages 104–116.*


## (chapter introduction)  *(p.104)*

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

## Applicability and Scaling  *(p.105)*


## Standards Compliance  *(p.105)*


## Benefits  *(p.105)*


## Functional Description  *(p.105)*

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

## Factory Defaults  *(p.106)*

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

## Configuring Authentication via TACACS+ Server  *(p.107)*

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

## Examples  *(p.113)*

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

## Viewing TACACS+ Statistics  *(p.114)*

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