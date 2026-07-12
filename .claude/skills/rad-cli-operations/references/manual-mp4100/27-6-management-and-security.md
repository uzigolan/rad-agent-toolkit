# 6 Management and Security

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 485–548.*


## 6.1 Access Control List (ACL)  *(p.485)*

6.1 Access Control List (ACL)  
Access control lists are used to flexibly filter and mark incoming network traffic. 
Standards and MIBs 
Relevant sections of RFC 1812 
Benefits 
The service providers use the ACLs to maintain the network security by preventing the malicious traffic 
from entering the device.  
Functional Description 
Devices featuring ACLs can flexibly filter management traffic, by denying or permitting IP packets to 
enter entities in the device, according to the packet’s source address, protocol type or other criteria. 
ACL entries are sequentially numbered rules, or ACEs (Access Control Elements) containing statements 
(Deny, Permit) and conditions. You can create up to 3 ACL and up to 128 ACEs per system. 
Packets are permitted or denied access, based on the following conditions: 
• 
IP source address  
• 
TCP and UDP port. 
The ACL structure is illustrated in the Error! Reference source not found. section. 
If there is a need to add a rule between already existing rules with consecutive numbers, the rules can 
be interspaced to accommodate additional rules between them.  
6. Management and Security 
Binding Access Control Lists 
Once created, ACLs are applied (bound) to the virtual management entity for filtering management 
traffic (only inbound direction is supported). 
Filtering  
Packets attempting to enter an entity to which the ACL is bound are checked against the access list rules, 
one by one. Access of matching packets is denied (packets are dropped) or permitted, as directed by the 
ACL statement. 
Packets matching a Deny statement (rule) are dropped unless permitted by a previous rule.  
Packets matching a Permit statement (rule) are permitted to access an entity unless denied by a 
previous statement.  
After a match, the rest of the rules are ignored. Packets not matching any rule are dropped. Empty ACLs 
deny access of all packets matched to them. 
Statistics 
The device collects ACL statistics per management entity. The statistic counters include the number of 
rule matches that occurred since the counters were last cleared. The statistic counters are cleared upon 
device reboot. The user may also clear ACL statistics of any entity and direction pair. 
Factory Defaults 
By default there are no ACL lists configured. 
Configuring ACL 
The ACL configuration tasks are performed at the access control and management levels.  
 To configure an ACL: 
3. Create an access control list. 
4. Add deny and permit rules to the ACL. 
5. Bind the ACL to a management entity 
6. Management and Security 
Access-Control-Level Tasks 
The following commands are available in the CLI access-control context: config>access-control#. The 
exception to this are the deny and permit commands, which are performed in the access-list(acl_name) 
context: configure>access-control>access-list(acl_name)#. 
Access-Control-Level Commands 
Task 
Command 
Comments 
Creating and 
deleting an ACL 
access-list  <acl_name> 
no access-list <acl_name> 
      
 
You can create up to 3 ACLs per system. 
Creating an ACL is performed by assigning a 
name. The ACL names must be unique and 
contain up to 252 alphanumeric characters. 
Adding deny rules 
to an ACL 
deny {tcp | udp} <src-address>[<src-port-
range>] <dst-address>[<dst-port>]  [log] 
[sequence <sequence-number>] 
 
 
Management-bound ACLs have the 
following configuration limitations: 
• <src-port-range>  must be any port – do 
not indicate specific ports 
• The destination IP address (<dst-
address>) must be any 
•  The destination port must be tcp/23 
(Telnet), tcp/22 (SSH) or udp/161 
(SNMP)  
Sequence number range is 1–2147483648. 
log – not in use in the current version 
Adding permit 
rules to an ACL 
permit {tcp | udp} <src-address>[<src-port-
range>] <dst-address> [<dst-port-range>]  
[log] [sequence <sequence-number>] 
 
 
Management-bound ACLs have the 
following configuration limitations: 
• <src-port-range>  must be any port – do 
not indicate specific ports 
• The destination IP address (<dst-
address>) must be any 
•  The destination port must be tcp/23 
(Telnet), tcp/22 (SSH) or udp/161 
(SNMP)  
Sequence number range is 1–2147483648. 
log – not in use in the current version 
Removing rules 
from an ACL 
delete <sequence-number> 
The value range is 1–2147483647 seconds 
6. Management and Security 
Task 
Command 
Comments 
Setting the 
logging interval of 
all ACLs 
logging access-list <value> 
no logging access-list 
Enable logging at the maximum rate of the 
value set at Access Control level. 
no logging access-list disables event logging 
for all rules in the ACL. 
Management-Level Tasks 
The following commands are available in the CLI management context: 
configure>management>access#. 
 Management-Level Commands 
Task 
Command 
Comments 
Binding the ACL to a 
management entity  
access-group <acl-name> in  
no access-group  
The management entity supports the ACLs 
only in the in direction. 
Displaying ACL statistics 
show access-list statistics 
See Displaying Statistics below 
Clearing ACL statistics 
clear-statistics access-list 
 
Displaying the summary 
of ACLs bound to a 
management entity 
show access-list summary 
Displays ACL status at the current level 
See Error! Reference source not found. 
below 
Example 
 To create an ACL: 
The example below illustrates a typical ACL applied to the incoming management traffic: 
• 
Allows SNMP (UDP port 161) traffic from source 172.17.170.81/32 
• 
Allows SSH (TCP port 22) traffic from source 172.17.170.81/32  
• 
Allows Telnet (TCP port 23) traffic from source 172.17.170.81/32 
configure 
access-control 
access-list mng1 
permit udp 172.17.170.81/32 any 161 sequence 1 
permit tcp 172.17.170.81/32 any 22 sequence 2 
permit tcp 172.17.170.81/32 any 23 sequence 3 
 
6. Management and Security 
Note 
You cannot edit a rule with the same sequence number. To edit a rule, delete 
the existing one and create a new rule with a new sequence number. 
The table below summarizes the rules configured for the ACL. Items in red are either implied or 
unavailable for the current parameter or serve as system settings that cannot be changed.  
Sequence 
Number 
Action 
Protocol Source IP 
TCP/UDP  
Source Port 
Dest. IP 
TCP/UDP Dest. Port 
1  
Permit 
UDP 
172.17.170.81/32 
Any 
Any 
161 
2 
Permit 
TCP 
172.17.170.81/32 
Any 
Any 
22 
3 
Permit 
TCP 
172.17.170.81/32 
Any 
Any 
23 
Displaying Status 
The ACL status displays information on the ACL name, type (IPv4), the entity that the ACL is bound to 
and its direction. The status information is available for the ACLs at the management access levels. 
 To display the ACL status: 
• 
In the config>mngmnt>access# prompt, enter the show access-list summary command. 
The following status information is displayed: 
ACL    Name    Type        Bound to    Direction 
--------------------------------------------------------------- 
mng1   IPv4    management  inbound 
Displaying Statistics 
The ACL statistic counters gather information on the number of rule matches registered on the ACL since 
the last reboot or counter clearing. 
Note 
All ACLs have an implied last rule that denies all packets. The device does not 
provide statistic counters for this rule. If you intend to collect statistics on the 
number of the packets discarded by the default ACL mechanism, you must add 
the deny ip any any rule at the end of the ACL. 
 To display the ACL statistics: 
• 
In the config>mngmnt>access# prompt, enter the show access-list statistics command. 

## 6.2 Access Policy  *(p.490)*

6. Management and Security 
The following statistic information is displayed: 
IPv4 access list: mng1    (in) 
Bound to: Management 
Matches counted for: 0 days 0 hours 2 minutes 33 seconds 
--------------------------------------------------------------- 
10    permit  tcp 172.17.154.154/24  any  22  (0 matches) 
20    permit  tcp 172.17.154.154/24  any  23  (0 matches) 
30    permit  udp 172.17.154.154/24  any  161 (0 matches) 
6.2 Access Policy 
The access policy allows specifying up to three user authentication methods (local, RADIUS, TACACS+). If 
an authentication method is not available or the user is not found, the next method is used if applicable.  
Factory Defaults 
By default, authentication is via the locally stored database (1st-level local). 
Configuring Access Policy 
 To define the access policy: 
• 
In the config>mngmnt>access# prompt, enter the necessary commands according to the 
tasks listed below. 

## 6.3 Authentication via RADIUS Server  *(p.491)*

6. Management and Security 
Task 
Command 
Comments 
Specifying authentication 
method preferably via 
RADIUS/TACACS+, then 
optionally TACACS+/RADIUS, 
then optionally local 
auth-policy 1st-level radius [2nd-level 
tacacs+ [3rd-level {local | none}]] 
auth-policy 1st-level tacacs+ [2nd-level 
radius [3rd-level {local | none}]] 
Megaplex-4 first attempts authentication via 
the server specified by 1st-level. If the server 
does not answer the authentication request, 
then Megaplex-4 attempts to authenticate 
via the server specified by 2nd-level. If the 
server does not answer the authentication 
request, then Megaplex-4 attempts to 
authenticate according to 3rd-level: 
local – Megaplex-4 authenticates via the local 
database 
none –No further authentication is done, and 
the authentication request is rejected. 
Note: If at any time in this process, an 
authentication server rejects an 
authentication request, Megaplex-4 ends the 
authentication process and does not attempt 
authentication at the next level. 
Specifying authentication 
method preferably via TACACS+, 
then optionally local 
auth-policy 1st-level tacacs+ [2nd-level { 
local | none } ] 
If 2nd-level is set to local, authentication is 
performed via the TACACS server. If the 
TACACS server does not answer the 
authentication request, then Megaplex-4 
authenticates via the local database. .If the 
TACACS server rejects the authentication 
request, Megaplex-4 ends the authentication 
process. 
If 2nd-level is set to none, authentication is 
performed via the TACACS server only. 
6.3 Authentication via RADIUS Server  
Megaplex-4 provides connectivity to up to four Radius authentication servers. You have to specify access 
parameters such as assigning Radius server IDs, specifying the associated server IP addresses and the 
number of retries. 
6. Management and Security 
Standards 
RFC 2865, Remote Authentication Dial In User Service (RADIUS).  
RFC 2618, RADIUS Authentication Client MIB. 
Benefits 
The RADIUS protocol allows centralized authentication and access control, avoiding the need of 
maintaining a local user database on each device on the network. 
Because of its generic nature, the RADIUS protocol can easily be used by service providers and 
enterprises to manage access to the Internet, internal networks, wireless networks, and integrated e-
mail services. These networks may incorporate DSL, access points, VPNs, network ports etc. 
Functional Description 
A work station attempts to log on to a Megaplex unit, which in turn submits an authentication request 
to the RADIUS server.  
The password is not transmitted over the network. A hash code is generated over it instead and a 
previously defined shared secret (string of free text) between the RADIUS server and the Megaplex unit 
is transmitted. 
RADIUS Server
Megaplex-4
Shared Secret
Management Work Station
Logon request to Megaplex-4
Verifying credentials and privileges via RADIUS data base
Logging on to Megaplex-4 or
returning authentication error
Access accepted or denied
Network
 
RADIUS Server Operation Scheme 
The RADIUS server verifies the user information against a database stored at the RADIUS server. The 
RADIUS server replies in one of the following ways: 
• 
Access Rejected. Access to all resources denied. 
• 
Access Accepted. Access to the requested network resources granted. 
6. Management and Security 
Factory Defaults 
Description 
Default Value 
The max number of authentication attempts. 
2 
Time interval between two authentication attempts. 
2 seconds 
UDP port used for the authentication channel 
1812 
Configuring the RADIUS  
Megaplex-4 provides connectivity to up to four Radius authentication servers. You have to specify access 
parameters such as assigning Radius server IDs, specifying the associated server IP addresses and the 
number of retries. 
This section explains how to define and configure a RADIUS server, activate and de-activate it. 
 To configure RADIUS parameters: 
1. At the config>mngmnt# prompt, enter radius. 
The config>mngmnt>radius# prompt appears. 
2. Define the parameters as illustrated and explained in the table below. 
Task 
Command 
Sending RADIUS request with NAS-IP-Address 
included in packets (in addition to user-name 
and password. By default the request is sent 
with user-name and password only. 
attribute-send nas-ip-address 
Handling response message with unknown 
service-type. Receiving reply without service-
type will be handled at the level of 
user/technician/operator/superuser. 
unmapped (default) means the reply will be 
handled as login fail. 
 
map-service-type unknown <unmapped | user | tech | 
oper | su>           
 
       
6. Management and Security 
 To define a Radius server: 
1. At the config>mngmnt# prompt, enter radius. 
The config>mngmnt>radius# prompt appears. 
2. Enter server <1..4>. 
The config>mngmnt>radius>server <1..4># prompt appears. 
3. Define the parameters for the relevant Radius server as illustrated and explained in the table 
below. 
Task 
Command 
Assigning an IP address to the server 
address <1.1.1.1..255.255.255.255> 
Defining a non-disclosed string (shared secret) 
used to encrypt the user password. 
key <string of free text> 
Defining the number of authentication request 
attempts 
retry <0..10> 
Defining the period of time during which 
Megaplex-4 waits for a response from the 
RADIUS server. 
timeout <1..5> 
Specifying the UDP port used for the 
authentication channel 
auth-port <1..65535> 
Viewing the RADIUS Server Profile Status 
This section explains how to display the status of the RADIUS servers. 
 To display the RADIUS server profile status: 
• 
At the config>mngmnt>radius# prompt, enter show status. 
The status of the four RADIUS server entries appears regardless if they are configured and 
enabled or not. 
nfig>mngmnt>radius# show status 
rver 
IP Address 
 
Access Status 
-------------------------------------------------------------------------- 
172.17.143.3  
Enable Connected 
0.0.0.0  
Disable Not connected 

## 6.4 Authentication via TACACS+ Server  *(p.495)*

6. Management and Security 
0.0.0.0  
Disable Not connected 
0.0.0.0  
Disable Not connected 
nfig>mngmnt>radius# 
Viewing RADIUS Statistics 
This section explains how to display RADIUS sever statistics. 
 To display RADIUS statistics: 
• 
At the config>mngmnt>radius# prompt, enter show statistics. 
RADIUS statistics appear as illustrated below.  
config>mngmnt>radius# show statistics  
 
   
Server1                  Server2 Server3 Server4 
--------------------------------------------------------------- 
Access Requests 
: 0 
0 
0 
0 
Access Retransmits : 0 
0 
0 
0 
Access Accepts 
: 0 
0 
0 
0 
Access Rejects 
: 0 
0 
0 
0 
Access Challenges : 0 
0 
0 
0 
Malformed Response : 0 
0 
0 
0 
Bad Authenticators : 0 
0 
0 
0 
Pending Requests 
: 0 
0 
0 
0 
Timeouts 
: 0 
0 
0 
0 
Unknown Types 
: 0 
0 
0 
0 
Packets Dropped 
: 0 
0 
0 
0 
6.4 Authentication via TACACS+ Server 
TACACS+ (Terminal Access Controller Access Control System Plus) is a security application that provides 
access control for routers, network access servers, and other networked computing devices via one or 
more centralized servers. TACACS+ provides separate authentication, authorization, and accounting 
services. It is used to communicate between the switch and an authentication database. Because 
TACACS+ is based on TCP, implementations are typically resilient against packet loss. 
6. Management and Security 
Standards 
RFC 1492, An Access Control Protocol, sometimes called TACACS. 
Benefits 
The TACACS+ protocol allows centralized authentication and access control, avoiding the need to 
maintain a local user data base on each device on the network. The TACACS+ server encrypts the entire 
body of the packet but leaves a standard TACACS+ header.  
Factory Defaults 
By default, no TACACS+ servers are defined. When the TACACS+ server is first defined, it is configured as 
shown below. 
Parameter 
Default Value 
retry 
1 
timeout 
5 seconds 
authentication-port 
49 
accounting-port 
49 
Functional Description 
TACACS+ is a protocol that provides access control for routers, network access servers and other 
networked computing devices via one or more centralized servers. TACACS+ is based on AAA model: 
• 
Authentication – The action of determining who a user is.  
• 
Authorization – The action of determining what a user is allowed to do. It can be used to 
customize the service for the particular user.  
• 
Accounting – The action of recording what a user is doing, and/or has done. 
The TACACS+ client can be configured to use authentication/authorization with or without accounting 
functionality. 
6. Management and Security 
Components 
The TACACS+ remote access environment has three major components: access client, TACACS+ client, 
and TACACS+ server.  
• 
The access client is an entity which seeks the services offered by the network.  
• 
TACACS+ client running on Megaplex-4, processes the requests from the access client and pass 
this data to TACACS+ server for authentication.  
• 
The TACACS+ server authenticates the request, and authorizes services over the connection. The 
TACACS+ server does this by matching data from the TACACS+ client`s request with entries in a 
trusted database. 
TACACS+ server decides whether to accept or reject the user's authentication or authorization. Based on 
this response from the TACACS+ server, the TACACS+ client decides whether to establish the user's 
connection or terminate the user's connection attempt. The TACACS+ client also sends accounting data 
to the TACACS+ server to record in a trusted database. 
TACACS+ uses TCP for its transport and encrypts the body of each packet. TACACS+ client and server can 
agree to use any port for authentication and accounting. TACACS+ supports authentication by using a 
user name and a fixed password. 
Accounting 
Megaplex-4 supports up to five accounting groups, with up to five TACACS+ servers per group. However, 
each TACACS+ server can be bound to a single accounting group only. 
A group can be defined with its own accounting level: 
• 
Shell accounting, which logs the following events: 
 
Successful logon 
 
Logon failure 
 
Successful logoff 
 
Megaplex-4-terminated management session. 
• 
System accounting, which records system events/alarms registered in local log file 
• 
Command accounting, which logs the following events: 
 
Any shell command that was successfully executed by Megaplex-4 
 
Any level that was successfully changed in a shell. 
6. Management and Security 
Defining TACACS+ Server 
Megaplex-4 provides connectivity to up to five TACACS+ authentication servers. You must specify the 
associated server IP address, key, number of retries, etc.  
 To define TACACS+ server: 
1. If you intend to use TACACS+ for authentication, verify that TACACS+ is selected as level-1 
authentication method (see Error! Reference source not found.). 
2. At the config>mngmnt>tacacsplus# prompt, type server <ip-address> to specify the server IP 
address. 
The config>mngmnt>tacacsplus>server(<ip-address>)# prompt is displayed. 
3. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining a new TACACS+ server 
server <ip-address> 
no server deletes a TACACS+ 
server 
Defining a non-disclosed string (shared 
secret) used to encrypt the user password 
key <string> [hash] 
The shared secret is a secret key 
consisting of free text known to 
the client and the server for 
encryption. It is hashed if 
specified. 
Defining the TCP port to be used for 
accounting  
accounting-port <tcp-port-number> Range 1–65535 
Defining the TCP port to be used for 
authentication  
authentication-port 
<tcp-port-number> 
Range 1–65535 
Binding accounting group to TACACS+ 
server 
group <string> 
no group detaches accounting 
group from server 
Defining the number of authentication 
request attempts 
retry <number-of-retries> 
Permanently set to 1 
Defining timeout (in seconds) for response 
from TACACS+ server 
timeout <seconds> 
Range 1–10 
Administratively enabling server 
no shutdown 
shutdown administratively 
disables the server 
Displaying statistics 
show statistics 
Clearing statistics 
clear-statistics 
6. Management and Security 
Configuring Accounting Groups 
 To configure accounting groups: 
1. At the config>mngmnt>tacacsplus# prompt, type group <group-name> to configure an 
accounting group with the specified name. 
The config>mngmnt>tacacsplus>group(<group-name>)# prompt is displayed. 
2. To define the accounting for the group, enter accounting [shell] [system] [commands] 
Note 
You can enter any combination of shell, system, and commands, but you must 
enter at least one of them. 
3. Type exit to return to the TACACS+ level. 
The config>mngmnt>tacacsplus# prompt is displayed. 
4. Type server <ip-address> to select the TACACS+ server to which to bind the group. 
The config>mngmnt>tacacsplus>server(<ip-address>)# prompt is displayed. 
5. At the config>mngmnt>tacacsplus>server(<ip-address>)# prompt, enter group < group-name> 
to bind the previously defined accounting group to the TACACS+ server. 
Task 
Command 
Comments 
Creating an accounting group 
group 
no group deletes accounting 
group 
Enabling TACACS+ accounting for the 
group 
accounting [shell] [system] 
[commands] 
Accounting can be of any 
combination  
no accounting disables TACACS+ 
accounting for the group 
Examples 
 Defining Server 
The example below illustrates the procedure for defining a TACACS+ server. 
• 
Server IP address: 175.18.172.150 
• 
Key: TAC_server1. 
# configure management tacacsplus 
config>mngmnt>tacacsplus# server 175.18.172.150 
6. Management and Security 
config>mngmnt>tacacsplus>server(175.18.172.150)$ key TAC_server1 
config>mngmnt>tacacsplus>server(175.18.172.150)$ no shutdown 
config>mngmnt>tacacsplus>server(175.18.172.150)$ information detail 
    key "244055BF667B8F89225048C6571135EF" hash 
    retry 1 
    timeout 5 
    authentication-port 49 
    accounting-port 49 
    no group 
    no shutdown 
Defining Accounting Group 
The example below illustrates the procedure for defining an accounting group. 
• 
Group name: TAC1 
• 
Accounting: Shell, system, and commands 
• 
Bound to server defined above 
# configure management tacacsplus 
config>mngmnt>tacacsplus# group TAC1 
config>mngmnt>tacacsplus>group(TAC1)$ accounting shell system commands 
config>mngmnt>tacacsplus>group(TAC1)$ info detail 
    accounting shell system commands 
 
config>mngmnt>tacacsplus>group(TAC1)$ exit 
config>mngmnt>tacacsplus# server 175.18.172.150 
config>mngmnt>tacacsplus>server(175.18.172.150)# group TAC1 
config>mngmnt>tacacsplus>server(175.18.172.150)# info detail 
    key "244055BF667B8F89829AB8AB0FE50885" hash 
    retry 1 
    timeout 5 
    authentication-port 49 
    accounting-port 49 
    group "TAC1" 
    no shutdown 
Displaying Statistics 
 To display TACACS+ statistics: 
• 
At the config>mngmnt>tacacsplus>server <ip-address># prompt, type: 
show statistics. 
The TACACS+ statistic counters are displayed.  
config>mngmnt>tacacsplus>server(175.18.172.150)$ show statistics 
6. Management and Security 
Requests               0 
Request Timeouts       0 
Unexpected Responses   0 
Server Error Responses 0 
Incorrect Responses    0 
Transaction Successes  0 
Transaction Failures   0 
Pending Requests       0 
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
 To clear TACACS+ statistics: 
• 
At the config>mngmnt>tacacsplus>server <ip-address># prompt, type clear statistics. 
TACACS+ statistic counters are set to 0. 

## 6.5 IEEE 802.1X - Port-based and MAC-based Network Access Control  *(p.502)*

6. Management and Security 
6.5 IEEE 802.1X - Port-based and MAC-based Network Access 
Control  
IEEE 802.1X is an IEEE Standard for Port-based Network Access Control (PNAC). It provides 
an authentication mechanism to devices wishing to attach to a LAN or WLAN. IEEE 802.1X defines the 
encapsulation of the Extensible Authentication Protocol (EAP) over IEEE 802 which is known as "EAP 
over LAN" or EAPOL.   
The host that is seeking access to the network is known as the Supplicant, and the system providing the 
point of access to the network is the Authenticator. 
Authenticator role can be configured for CL.2/A GbE ports, physical Ethernet ports of M-ETH and VS 
modules. The supplicant role is supported by CL.2/A GbE ports. 
Authenticator and supplicant cannot be enabled on the same port at the same time. 
IEEE 802.1X access control is not supported on the ports configured for HSR, LAG or ERP protection.  
Standards 
IEEE 802.1X 
Benefits 
802.1X protocol provides secured access to the customer network. 
Factory Defaults 
The parameter defaults are listed in the table below. 
Parameter  
Description 
Default Value 
authenticator 
quiet-period  
Configuring quiet period after authentication failure (sec) 
60 
re-authentication-period  Configuring reauthentication period (sec) 
3600 
max-authentication  
Configuring the maximum number of authentication 
attempts 
2 
6. Management and Security 
Parameter  
Description 
Default Value 
tx-period  
Configuring the time to wait before retransmitting EAP 
frame (sec) 
30 
max-frame-tx  
Configure the maximum number of EAP frame 
retransmissions 
2 
supplicant 
held-period  
Configuring held period after authentication failure (sec) 
60 
max-authentication  
Configuring the maximum number of authentication 
attempts 
2 
tx-period  
Configuring the time to wait before retransmitting EAP 
frame (sec) 
30 
max-frame-tx  
Configure the maximum number of EAP frame 
retransmissions 
2 
Functional Description 
Components 
802.1X authentication involves three parties: a supplicant, an authenticator, and an authentication 
server.  
• 
The supplicant is a client device that wishes to attach to the LAN.  
• 
The authenticator is a network device, such as an Ethernet switch or wireless access point.  
• 
The authentication server is typically a host running software supporting 
the RADIUS and EAP protocols.  
The authenticator acts like a security guard to a protected network. The supplicant (i.e. the client device) 
is not allowed access through the authenticator to the protected side of the network until the 
supplicant’s identity has been validated and authorized.  
With 802.1X port-based authentication, the supplicant provides credentials, such as user 
name/password, to the authenticator, and the authenticator forwards the credentials to the 
authentication server for verification. If the authentication server determines the credentials are valid, 
the supplicant (client device) is allowed to access resources located on the protected side of the 
network. 
6. Management and Security 
EAPOL operates at the network layer on top of the data link layer, and in Ethernet II framing protocol 
has an EtherType value of 0x888E. 
Megaplex-4
Authenticator:
M-ETH/VS-ETH
Supplicant
Initiation:
EAPOL Request/Response
Authentication (Radius Message)
EAP Negotiation
Authentication Algorithm
Radius Message
EAP – Success/Failure
PSN
RV EMS 
Server
Radius Frames
EAPOL Frames
Authentication
Radius Server
CPE
CPE
Initiation:
EAPOL Request/Response
EAPOL Frames
 
Port-based Network Access Control for Physical Ports  
 
Virtual Port-based Network Access Control  
Typical Authentication Progression 
Initialization. On detection of a new supplicant, the port on the switch (authenticator) is enabled and 
set to the "unauthorized" state. In this state, only 802.1X traffic is allowed; other traffic, such as 
the Internet Protocol (and with that TCP and UDP), is dropped. 
Initiation. To initiate authentication, the authenticator will periodically transmit EAP-Request Identity 
frames to a special Layer 2 address on the local network segment. The supplicant listens on this address, 
and on receipt of the EAP-Request Identity frame it responds with an EAP-Response Identity frame 
containing an identifier for the supplicant such as a User ID. The authenticator then encapsulates this 
Identity response in a RADIUS Access-Request packet and forwards it on to the authentication server. 
6. Management and Security 
The supplicant may also initiate or restart authentication by sending an EAPOL-Start frame to the 
authenticator, which will then reply with an EAP-Request Identity frame. 
Negotiation. The authentication server sends a reply (encapsulated in a RADIUS Access-Challenge 
packet) to the authenticator, containing an EAP Request specifying the EAP Method (the type of EAP 
based authentication it wishes the supplicant to perform). The authenticator encapsulates the EAP 
Request in an EAPOL frame and transmits it to the supplicant. At this point the supplicant can start using 
the requested EAP Method, or do an NAK ("Negative Acknowledgement") and respond with the EAP 
Methods it is willing to perform. 
Authentication. If the authentication server and the supplicant agree on an EAP Method, EAP Requests 
and Responses are sent between the supplicant and the authentication server (translated by the 
authenticator) until the authentication server responds with either an EAP-Success message 
(encapsulated in a RADIUS Access-Accept packet), or an EAP-Failure message (encapsulated in a RADIUS 
Access-Reject packet). If authentication is successful, the authenticator sets the port to the 
"Authenticated" status and normal traffic is allowed. If it is unsuccessful the port remains in the 
"Unauthenticated" status. When the supplicant logs off, it sends an EAPOL-logoff message to the 
authenticator, the authenticator then sets the port to the "Unauthenticated" status, once again blocking 
all non-EAP traffic. 
Configuring 802.1X Access Control 
To configure 802.1X access control, you must first enable it on the system level and then configure it for 
all authenticator and supplicant ports. 
 To enable 802.1X on the system level: 
1. Navigate to the config>system>dot1x# prompt and enter the necessary commands according to 
the tasks listed below.  
Task 
Command 
Comments 
Enabling 802.1X  
access-control      
no access-control disables 802.1X 
access control 
Displaying supported EAPOL and 
MKA versions  
show version-information 
 To configure 802.1X on the port level: 
1. At the config>port>ethernet <slot>/<port># prompt, type dot1x command. 
The config>port>ethernet(<slot>/<port>)dot1x# prompt is displayed. 
6. Management and Security 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Reinitializing 802.1X 
initialize 
Enabling authenticator role 
authenticator-enable 
no authenticator-enable 
disables authenticator role 
A port cannot be authenticator 
and supplicant at the same time. 
Enabling virtual ports  
virtual-ports-enable  
no virtual-ports-enable disables 
virtual ports 
The max number of enabled 
virtual ports is 20. 
Enabling supplicant role 
supplicant-enable 
no supplicant-enable disables 
supplicant role 
A port cannot be authenticator 
and supplicant at the same time. 
Displaying 802.1X status 
show status 
 
Displaying 802.1X statistics 
show statistics  
Clearing 802.1X statistics 
clear statistics  
Authenticator configuration level (see 
below) 
authenticator 
Supplicant configuration level (see 
below) 
supplicant 
The following commands are available in the autenticator level, at the config> port ethernet 
(<slot><port>)dot1x>authenticator# prompt. 
Task 
Command 
Comments 
Enabling periodic 
reauthentication 
re-authentication-periodic 
re-authentication-periodic disables 
periodic reauthentication 
Configuring quiet period after 
authentication failure (sec) 
quiet-period <0 – 65535> 
 
Configuring reauthentication 
period (sec) 
re-authentication-period <0 – 
65535> 
 
6. Management and Security 
Task 
Command 
Comments 
Configuring the maximum 
number of authentication 
attempts 
max-authentication <1 – 65535>  
 
Configuring the time to wait 
before retransmitting EAP frame 
(sec) 
tx-period <1 – 65535> 
 
Configuring the maximum 
number of EAP frame 
retransmissions 
max-frame-tx <1 – 10> 
 
The following commands are available in the supplicant level, at the config> port 
ethernet(<slot><port>) dot1x > supplicant# prompt. 
Task 
Command 
Comments 
Configuring held period after 
authentication failure (sec) 
held-period <0 – 65535> 
 
Configuring the maximum 
number of authentication 
attempts 
max-authentication <1 – 65535>  
 
Configuring RADIUS username 
and password 
radius-credentials username 
<name 1-244 characters> 
password <password 1-244 
characters> 
no radius-credentials cancels the 
current RADIUS username and 
password 
 
Configuring the time to wait 
before retransmitting EAP frame 
(sec) 
tx-period <1 – 65535> 
 
Configure the maximum number 
of EAP frame retransmissions 
max-frame-tx <1 – 10> 
 
Note 
In order for 802.1x access control to function properly, the relevant Ethernet 
ports must be associated with an L2CP profile that specifies peer action for 
MAC 01-80-C2-00-00-03.  
Example  
The example below illustrates the 802.1X protocol operation. 
6. Management and Security 
• 
Authenticators: ports of M-ETH module installed in MP 1 slot 2 
• 
Supplicant: CL-A/1 port of MP 2 
• 
All the authenticator/supplicant parameters are at their defaults. 
############# MP-Authenticator M-ETH  Vs. MP - Supplicant ######## 
####### using Radius EAP Authentication method = EAP-MDS ##### 
 
 
############################################################################# 
############ 1st script MP-Authenticator M-ETH port  ######################### 
############################################################################# 
 
#######################IP-Address and Card_Types ################ 
configure router 1 interface 1 address 172.18.92.254/24 
configure router 1 static-route 0.0.0.0/0 address 172.18.92.1 
exit all 
 
configure slot cl-a card-type cl cl2-622gbea 
configure slot 2 card-type eth meth 
 
############## Define radius client servers ############################ 
 
config management radius 
 
server 1 
address 172.18.92.219 
auth-port 1812 
key ALPHA 
no shutdown 
exit all 
 
 
############## Enable l2cp  for 802.1x on ethernet port ################### 
 
configure port l2cp-profile L2cpDefaultProfile mac 01-80-C2-00-00-03  peer 
 
############## Enable 802.1x on all ethernet ports ################### 
 
 
configure system dot1x access-control  
 
configure qos 
queue-group-profile qg1 
queue-block  1/1 
exit 
queue-block  0/1 
bind queue  0 queue-block  1/1 
exit all 
 
 
conf port ethernet cl-a/1 no shutdown 
6. Management and Security 
 
configure port ethernet 2/1 queue-group profile qg1 
configure port ethernet 2/1 dot1x authenticator-enable 
configure port ethernet 2/1 l2cp profile L2cpDefaultProfile 
configure port ethernet 2/1 no shutdown 
 
configure port ethernet 2/2 queue-group profile qg1 
configure port ethernet 2/2 dot1x authenticator-enable 
configure port ethernet 2/2 l2cp profile L2cpDefaultProfile 
configure port ethernet 2/2 no shutdown 
 
configure port ethernet 2/3 queue-group profile qg1 
configure port ethernet 2/3 dot1x authenticator-enable 
configure port ethernet 2/3 l2cp profile L2cpDefaultProfile 
configure port ethernet 2/3 no shutdown 
 
configure port ethernet 2/4 queue-group profile qg1 
configure port ethernet 2/4 dot1x authenticator-enable 
configure port ethernet 2/4 l2cp profile L2cpDefaultProfile 
configure port ethernet 2/4 no shutdown 
 
configure port ethernet 2/5 queue-group profile qg1 
configure port ethernet 2/5 dot1x authenticator-enable 
configure port ethernet 2/5 l2cp profile L2cpDefaultProfile 
configure port ethernet 2/5 no shutdown 
 
 
configure port ethernet 2/6 queue-group profile qg1 
configure port ethernet 2/6 dot1x authenticator-enable 
configure port ethernet 2/6 l2cp profile L2cpDefaultProfile 
configure port ethernet 2/6 no shutdown 
 
configure port ethernet 2/7 queue-group profile qg1 
configure port ethernet 2/7 dot1x authenticator-enable 
configure port ethernet 2/7 l2cp profile L2cpDefaultProfile 
configure port ethernet 2/7 no shutdown 
 
configure port ethernet 2/8 queue-group profile qg1 
configure port ethernet 2/8 dot1x authenticator-enable 
configure port ethernet 2/8 l2cp profile L2cpDefaultProfile 
configure port ethernet 2/8 no shutdown 
 
conf bridge 1 port 1 no shutdown 
conf bridge 1 port 3 no shutdown 
conf bridge 1 port 21 no shutdown 
conf bridge 1 port 22 no shutdown 
conf bridge 1 port 23 no shutdown 
conf bridge 1 port 24 no shutdown 
conf bridge 1 port 25 no shutdown 
conf bridge 1 port 26 no shutdown 
conf bridge 1 port 27 no shutdown 
conf bridge 1 port 28 no shutdown 
6. Management and Security 
conf bridge 1 vlan-aware 
 
conf bridge 1 
vlan 100 
tagged-egress 1,3,21,22,23,24,25,26,27,28 
exit all 
 
conf flows classifier-profile untag match-any match untagged 
conf flows classifier-profile all match-any match all 
conf flows classifier-profile mng match-any match vlan 100 
conf flows classifier-profile traffic match-any match vlan 50 
 
                 
conf flows flow mng3 classifier all 
conf flows flow mng3 ingress-port  svi 1 
conf flows flow mng3 egress-port bridge-port 1 1 
conf flows flow mng3 vlan-tag  push  vlan  100  p-bit  fixed  7  
conf flows flow mng3 no shutdown 
                 
conf flows flow mng4 classifier mng 
conf flows flow mng4 ingress-port bridge-port 1 1 
conf flows flow mng4 egress-port  svi 1 
conf flows flow mng4 vlan-tag  pop vlan  
conf flows flow mng4 no shutdown               
 
conf flows flow mng21 classifier all 
conf flows flow mng21 ingress-port ethernet 2/1 
conf flows flow mng21 egress-port bridge-port 1 21 
conf flows flow mng21 vlan-tag  push  vlan  100  p-bit  fixed  7  
conf flows flow mng21 reverse-direction queue 0 block 0/1 
conf flows flow mng21 no shutdown 
 
conf flows flow mng22 classifier all 
conf flows flow mng22 ingress-port ethernet 2/2 
conf flows flow mng22 egress-port bridge-port 1 22 
conf flows flow mng22 vlan-tag  push  vlan  100  p-bit  fixed  7  
conf flows flow mng22 reverse-direction queue 0 block 0/1 
conf flows flow mng22 no shutdown 
 
conf flows flow mng23 classifier all 
conf flows flow mng23 ingress-port ethernet 2/3 
conf flows flow mng23 egress-port bridge-port 1 23 
conf flows flow mng23 vlan-tag  push  vlan  100  p-bit  fixed  7  
conf flows flow mng23 reverse-direction queue 0 block 0/1 
conf flows flow mng23 no shutdown 
 
conf flows flow mng24 classifier all 
conf flows flow mng24 ingress-port ethernet 2/4 
conf flows flow mng24 egress-port bridge-port 1 24 
conf flows flow mng24 vlan-tag  push  vlan  100  p-bit  fixed  7  
conf flows flow mng24 reverse-direction queue 0 block 0/1 
conf flows flow mng24 no shutdown 
6. Management and Security 
 
conf flows flow mng25 classifier all 
conf flows flow mng25 ingress-port ethernet 2/5 
conf flows flow mng25 egress-port bridge-port 1 25 
conf flows flow mng25 vlan-tag  push  vlan  100  p-bit  fixed  7  
conf flows flow mng25 reverse-direction queue 0 block 0/1 
conf flows flow mng25 no shutdown 
 
conf flows flow mng26 classifier all 
conf flows flow mng26 ingress-port ethernet 2/6 
conf flows flow mng26 egress-port bridge-port 1 26 
conf flows flow mng26 vlan-tag  push  vlan  100  p-bit  fixed  7  
conf flows flow mng26 reverse-direction queue 0 block 0/1 
conf flows flow mng26 no shutdown 
 
conf flows flow mng27 classifier all 
conf flows flow mng27 ingress-port ethernet 2/7 
conf flows flow mng27 egress-port bridge-port 1 27 
conf flows flow mng27 vlan-tag  push  vlan  100  p-bit  fixed  7  
conf flows flow mng27 reverse-direction queue 0 block 0/1 
conf flows flow mng27 no shutdown 
 
conf flows flow mng28 classifier all 
conf flows flow mng28 ingress-port ethernet 2/8 
conf flows flow mng28 egress-port bridge-port 1 28 
conf flows flow mng28 vlan-tag  push  vlan  100  p-bit  fixed  7  
conf flows flow mng28 reverse-direction queue 0 block 0/1 
conf flows flow mng28 no shutdown 
 
conf flows flow 1 classifier untag 
conf flows flow 1 ingress-port ethernet cl-a/1 
conf flows flow 1 egress-port ethernet 2/1  
conf flows flow 1 vlan-tag push vlan 50 p-bit fixed 1 
conf flows flow 1 no shutdown 
 
conf flows flow 2 classifier traffic 
conf flows flow 2 ingress-port ethernet 2/1 
conf flows flow 2 egress-port ethernet cl-a/1 
conf flows flow 2 vlan-tag pop vlan 
conf flows flow 2 no shutdown 
 
commit 
 
############################################################################# 
############2nd  script MP-Supplicant  cl-a/1 #port  ######################### 
############################################################################# 
 
 
conf slot cl-a card-type cl cl2-622gbea 
configure slot 1 card-type versatile vs-12 
 
conf router 1 interface 1 address 172.18.92.251/24 
6. Management and Security 
conf router 1 static-route 0.0.0.0/0 address 172.18.92.1 
exit all 
 
############## Enable l2cp  for 802.1x on ethernet port ################### 
 
configure port l2cp-profile L2cpDefaultProfile mac 01-80-C2-00-00-03  peer 
 
############## Enable 802.1x on all ethernet ports ################### 
 
configure system dot1x access-control  
 
configure qos 
queue-group-profile  qg1 
queue-block  1/1 
exit 
queue-block  0/1 
bind queue  0 queue-block  1/1 
exit all 
 
configure port ethernet cl-a/1 queue-group profile qg1 
configure port ethernet cl-a/1 l2cp profile L2cpDefaultProfile 
configure port ethernet cl-a/1 dot1x supplicant-enable 
configure port ethernet cl-a/1 dot1x supplicant 
radius-credentials user-name HU password 4321 
exit all 
 
conf port ethernet cl-a/1 no shutdown 
 
conf port ethernet 1/1 queue-group profile qg1 
conf port ethernet 1/1 no shutdown 
 
conf bridge 1 port 1 no shutdown 
conf bridge 1 port 2 no shutdown 
 
conf bridge 1 vlan-aware 
 
conf bridge 1 
   vlan 100 
   tagged-egress 1,2 
   exit all 
 
conf flows classifier-profile untag match-any match untagged 
conf flows classifier-profile all match-any match all 
conf flows classifier-profile v100 match-any match vlan 100 
conf flows classifier-profile traffic match-any match vlan 50 
 
 
conf flows flow MNG classifier all 
conf flows flow MNG ingress-port ethernet cl-a/1 
conf flows flow MNG egress-port bridge-port 1 1 
conf flows flow MNG vlan-tag  push  vlan  100  p-bit  fixed  7  
conf flows flow MNG reverse-direction queue 0 block 0/1 
6. Management and Security 
conf flows flow MNG no shutdown 
                    
conf flows flow mng_1 classifier all       
conf flows flow mng_1 ingress-port svi 1 
conf flows flow mng_1 egress-port bridge-port 1 2 
conf flows flow mng_1 vlan-tag push vlan 100 p-bit fixed 7        
conf flows flow mng_1 no shutdown 
 
conf flows flow mng_2 classifier v100       
conf flows flow mng_2 ingress-port bridge-port 1 2 
conf flows flow mng_2 egress-port svi 1 
conf flows flow mng_2 vlan-tag pop vlan  
conf flows flow mng_2 no shutdown 
 
conf flows flow 1 classifier untag 
conf flows flow 1 ingress-port ethernet 1/1 
conf flows flow 1 egress-port ethernet cl-a/1  
conf flows flow 1 vlan-tag push vlan 50 p-bit fixed 1 
conf flows flow 1 no shutdown 
 
conf flows flow 2 classifier traffic 
conf flows flow 2 ingress-port ethernet cl-a/1 
conf flows flow 2 egress-port ethernet 1/1  
conf flows flow 2 vlan-tag pop vlan 
conf flows flow 2 no shutdown 
 
commit  
Displaying Statistics 
The statistics can be displayed either per physical port or per virtual port. If a MAC address is specified in 
the command, the output is the statistics of the virtual port belonging to that address; if MAC address is 
not specified the output is the statistics of the physical port. The virtual-port option is available only for 
M-ETH modules.  
 To display 802.1X statistics:  
1. Navigate to configure port ethernet <slot>/<port> dot1x context. 
2. Type: show statistics [virtual-port <mac-address>] 
The 802.1X statistic counters are displayed.  
mp4100>config>port>eth(2/1)>dot1x# show statistics  
 
EAPOL Rx Frames Statistics 
----------------------------------------------------------------------------- 
Rx Invalid Frames         : 0 
Rx Length Error Frames    : 0 
6. Management and Security 
Rx Announcement Frames     : 0 
Rx Announcement Req Frames : 0 
Rx Unavailable Frames     : 0 
Rx Start Frames           : 0 
Rx Frames                 : 33 
Rx Logoff Frames          : 0  
Rx No Ckn Frames          : 0 
Rx MK Invalid Frames      : 0 
Rx Last Frame Version     : 3  
Rx Last Frame Source     : 00-01-C1-00-00-02  
 
EAPOL Tx Frames Statistics 
----------------------------------------------------------------------------- 
Tx Supp Frames            : 22 
Tx Logoff Frames          : 0 
Tx Announcement Frames     : 0 
Tx Announcement Req Frames : 0 
Tx Start Frames           : 20 
Tx Auth Frames            : 0 
Tx MKA Frames             : 0 
 
mp4100>config>port>eth(2/1)>dot1x# show statistics virtual-port B8-AC-6F-0D-D4-47 
 
EAPOL Rx Frames Statistics 
----------------------------------------------------------------------------- 
Rx Invalid Frames         : 0 
Rx Length Error Frames    : 0 
Rx Announcement Frames     : 0 
Rx Announcement Req Frames : 0 
Rx Unavailable Frames     : 0 
Rx Start Frames           : 8 
Rx Frames                 : 16 
Rx Logoff Frames          : 0 
Rx No Ckn Frames          : 0 
Rx MK Invalid Frames      : 0 
Rx Last Frame Version     : 1 
Rx Last Frame Source      : B8-AC-6F-0D-D4-47 
 
EAPOL Tx Frames Statistics 
----------------------------------------------------------------------------- 
Tx Supp Frames            : 0 
Tx Logoff Frames          : 0 
Tx Announcement Frames     : 0  
Tx Announcement Req Frames : 0 
Tx Start Frames           : 0 
Tx Auth Frames            : 19 
Tx MKA Frames             : 0 
6. Management and Security 
802.1X Statistic Counters 
Counter 
Description 
Rx Frames 
Number of EAPOL-EAP frames received 
Rx Start Frames 
Number of EAPOL-Start frames received 
Rx Logoff Frames   
Number of EAPOL- Logoff frames received 
*Rx Announcement Frames   
Number of EAPOL-Announcement frames received 
*Rx Announcement Req Frames  
Number of EAPOL-Announcement-Req frames received 
Rx Invalid Frames        
Number of invalid EAPOL frames received 
Rx Length Error Frames  
Number of EAPOL frames with wrong length received 
Rx Unavailable Frames 
Number of EAPOL frames discarded due to unavailable virtual port 
Rx No Ckn Frames      
Number of MKPDUs received with MKA disabled or CKN unrecognized 
Rx MK Invalid Frames  
Number of MKPDUs failing message authentication on Rx process 
Last Rx Frame Version  
Version of last received EAPOL frame 
Last Rx Frame Source 
Source MAC address of last received EAPOL frame 
Tx Auth Frames  
Number of EAPOL-EAP frames transmitted by the authenticator 
Tx Supp Frames 
Number of EAPOL-EAP frames transmitted by the supplicant 
Tx Start Frames  
Number of EAPOL-Start frames transmitted 
Tx Logoff Frames  
Number of EAPOL-Logoff frames transmitted 
*Tx Announcement Frames  
Number of EAPOL-Announcement frames transmitted 
*Tx Announcement Req Frame 
Number of EAPOL-Announcement-Req frames transmitted 
Tx MKA Frames  
Number of EAPOL-MKA frames with no CKN information transmitted 
*Not supported in the current version 
 To clear 802.1X statistics: 
• 
At the config>port>ethernet <slot>/<port> dot1x # prompt, type clear statistics. 
The device clears the statistics of the physical port, as well as all virtual ports bound to it. 
Viewing the 802.1X Status 
This section explains how to display the status of the 802.1X protocol operation. 
6. Management and Security 
 To display 802.1X status:  
1. Navigate to configure port ethernet <slot>/<port> dot1x. 
2.  Type show status. 
The 802.1X status is displayed.  
config>port>eth(2/1)>dot1x# show status 
Role           : Authenticator 
Connect Status : Authenticated  
If virtual ports are enabled, the last string does not make sense and it is not displayed. In this case use 
show virtual-ports command. 
The status display provides information about: 
• 
Role of the 802.1x port: 
 
 Authenticator  
 
Supplicant  
 
Authenticator (Virtual Ports Enabled) 
• 
Authentication process status: 
 
Pending 
 
Unauthenticated 
 
Authenticated 
 To display the virtual ports:  
1. Navigate to configure port ethernet <slot>/<port> dot1x. 
2.  Type show virtual-ports.  
The 802.1X virtual ports are displayed.  
Number of Virtual Ports 
----------------------- 
Maximum Supported            : 100 
Currently Running            : 12 
 
EAPOL Port Unavailable Frames: 0 
 
Virtual Port Peer MAC Address Status  
--------------------------------------------- 
B8-AC-6F-0D-D4-47             Authenticated 
00-19-B9-0E-8A-A3             Pending 
22-22-22-22-22-22             Unauthenticated 
The display provides information about: 

## 6.6 Managers  *(p.517)*

6. Management and Security 
• 
Maximum number of virtual ports that can be supported 
• 
Current number of virtual ports running 
• 
Number of EAPOL frames discarded due to inadequate resources or nonexistent virtual port 
• 
Virtual port status for all peer source MAC addresses: 
 
Pending 
 
Unauthenticated 
 
Authenticated. 
 To display the version information: 
• 
At the config>system>dot1x# prompt, enter version-information. 
The supported versions of EAPOL protocol and MKA protocols are displayed. 
# show configure system dot1x version-information 
EAPoL version : 3 
MKA version   : 0  
6.6 Managers  
This section explains how to add and remove managers. You can add up to 10 managers.  
 To add a manager: 
1. At the config# prompt, enter manager. 
The config>mngmnt# prompt appears. 
2. At the config>mngmnt# prompt, enter manager <0.0.0.0..255.255.255.255>. 
The specified manager has been added and the  
config>mngmnt>manager <0.0.0.0..255.255.255.255> prompt appears displaying the IP address 
of the manager you just added. 
 To remove a network manager: 
• 
To delete a manager, in the management context (config>mngmnt), enter no manager <ip-
address>/<ip-mask> 
• 
To delete all managers, enter no manager. 

## 6.7 Management Access  *(p.518)*

6. Management and Security 
6.7 Management Access  
You can enable or disable access to the Megaplex-4 management system via Telnet, SSH, or SNMP 
applications for a specific router interface. By disabling Telnet, SSH, or SNMP, you prevent unauthorized 
access to the system when security of the associated IP address has been compromised. When Telnet, 
SSH, and SNMP are disabled, Megaplex-4 cannot be managed using the relevant router interface. If 
Telnet, SSH and SNMP are disabled for all router interfaces, the unit can be managed via an ASCII 
terminal only. In addition, you can limit access to the device to only the defined management stations.  
In addition, Megaplex-4 can use up to four RADIUS servers to facilitate remote authentication. 
Introducing a RADIUS server allows configuring up to two authentication protocols according to a user-
configured order. If the first authentication method is unavailable or the user is not found, the next 
method is used. 
The table below lists management access implementation, according to the defined management access 
and whether network managers are defined.  
Access Method 
Mode  
Allowed to Access Megaplex-4 
Network Manager(s) Defined  
Network Manager(s) not 
Defined  
Telnet Access 
Enable 
Anybody 
Anybody 
Disable 
Nobody 
Nobody 
SSH Access (Secure Shell) 
Enable 
Anybody 
Anybody 
Disable 
Nobody 
Nobody 
SNMP Access 
Enable  
Anybody 
Anybody 
Disable 
Nobody 
Nobody 
Factory Defaults 
By default, access is enabled via Telnet, SSH, and SNMP. 
In the default factory configuration, Megaplex-4 allows management from the OOB management port.  
The default factory configuration includes the following:  
• 
Allows untagged management access from the OOB port  
• 
Default IP address of the Router Interface is 169.254.1.1/16 
6. Management and Security 
• 
No default Gateway configuration 
• 
Allows local management access using a PC to an ‘out of the box’ Megaplex-4 device: 
 
When PC uses DHCP, access to Megaplex-4 device is automatically established (PC address 
defaults to 169.254.x.y as no DHCP server  Microsoft protocol). 
 
This configuration can be deleted by the user. 
• 
SVI, RI are assigned with the following indexes: 
 
SVI #: 1 (lowest valid SVI index) 
 
RI #: 1 (lowest valid RI number)   
• 
Not backward compatible to user configuration CLI scripts that configure OOB port 
Router
MNG RI 
(Megaplex-4 Host)
SVI
OOB
MNG
Port
Untagged
Untagged
 
Untagged Management Access from OOB MNG Port 
The factory default configuration is only loaded if there is no startup-config or user-default-config (for 
example, after executing the factory-default command).  
If you copy a script and paste it to the terminal after factory-default-config is loaded, it is important to 
verify that the configuration in the script does not conflict with the factory default configuration. 
You can delete the factory default configuration. You can also replace the factory-default with a 
download of a fresh startup-config, by performing Reset. 
You can add an additional IP address over the RI to allow remote access. 
When accessing remotely, it is possible to delete the local IP 169.254.1.1/16. 
Configuring Access 
Follow the instructions below to enable/disable access via Telnet, SSH or SNMP. In addition, you have to 
configure the access policy. 

## 6.8 RSA Key Generation  *(p.520)*

6. Management and Security 
 To enable or disable access via management protocols: 
1. At the config>mngmnt# prompt, enter access. 
The config>mngmnt>access# prompt appears. 
2. Configure as illustrated and explained in the table below.  
Task 
Command 
Comments 
Enabling access via Telnet 
telnet 
 
Disabling acess via Telnet 
no telnet 
 
Enabling access via Secure Shell (SSH) 
ssh 
 
Disabling access via SSH 
no ssh 
 
Enabling access via SNMP 
snmp 
 
Disabling access via SNMP 
no snmp 
 
 To define the access policy:  
• 
At the config>mngmnt>access# prompt, configure the access levels as illustrated and explained 
in the table below. 
Task 
Command 
Comments 
Specifying authentication 
preferably via database 
stored on RADIUS server, 
then optionally local 
auth-policy 1st-level radius [2nd-level {local 
| none }] 
If 2nd-level is set to local, authentication 
is performed via the RADIUS server. If 
the RADIUS server does not answer the 
authentication request, then Megaplex-4 
authenticates via the local database. If 
the RADIUS server rejects the 
authentication request, Megaplex-4 
ends the authentication process. 
If 2nd-level is set to none, authentication 
is performed via the RADIUS server only 
6.8 RSA Key Generation  
Megaplex-4 supports generating an RSA key pair (private and public) of a configurable key size, enabling 
users to generate their own key, or to upgrade the key size from 1024 to 2048 bits (more secure). 
6. Management and Security 
Functional Description 
In cases where a device does not have an RSA key, the SW automatically generates an RSA key. 
When a device is upgraded to a new version, it keeps its old key, and therefore does not generate a new 
key automatically.  
Megaplex-4 supports the generate-rsa command for users who prefer to generate their own RSA key 
pair. Or for customers who are using a RAD device that comes with a 1024-long key and would like to 
upgrade to a more secure 2048-long key.  
When upgrading an RSA key using this command, the SW deletes the existing RSA key and reboots the 
device. As NTP is not available during device initialization (while the RSA key is actually generated), the 
SW keeps the timestamp from when the generate-rsa command was executed, so it will be available 
following reboot. This timestamp is displayed when you run the show my-public-rsa-key command to 
display the public RSA key information. 
Configuring RSA Key Generation 
 To configure an RSA key pair: 
1. Navigate to configure>crypto>key. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Generating the RSA key 
generate-rsa [size <key-size>] 
[application ssh] 
• key-size – RSA key size (in 
bits) 
Possible values: 1024, 2048 
Default: 2048 
Note: The device requests 
approval to execute the 
command: 
The device will delete the 
existing key. Need to reboot to 
create the new key Are you 
sure? [yes/no] 
Showing the RSA key 
show my-public-rsa-key 
See Error! Reference source not 
found.. 

## 6.9 SNMP Management  *(p.522)*

6. Management and Security 
Viewing the RSA Key  
You can display the generated public RSA key information, including the timestamp in which the RSA key 
was generated. 
 To display the RSA key information: 
• 
At the configure>crypto>key # prompt, enter show my-public-rsa-key. 
config>crypto>key# show my-public-key-rsa 
  
Generated at : 28-05-2023 14:28:02 UTC 
Name         : RAD.MP4.ssh_key 
Size         : 2048 
Application  : SSH 
  
8BB81A0E298872637B5A724A816D94269388E60E714513C1D97960CD5B3BC2D7390766251C7935B3 
410BA8F0BC1BED7ECBF2A536D002575519635AEC085B4007E309CD1EA59CAC5786A5526063FD0063 
E4D817043CEF12442FFA21540BB7DE6B843BE3B01FE87169127C215ADA728AF63B8236A65A2DCDDB 
3B7F19ABC714FFF1895DCD6A5E10C3A2D52B5D735D9F6BB21B9FB8010D80F2DB4678BEEBC1A7E70F 
825C6191EB62038F03A0A768024C569BDB50EDC6B8DD5F4007B71371C02F2FCC1588042B1BBEE2FE 
745578AE0B58738F23D49D3BF8D080A7F96D9423E79B8D34E3462C3ED30C78549E468FBCC9346E9A 
C0F83F36D93808B1209CFBE192D81B3E52EB6738810EE3883116BC02B84D6AF893F0AA3F472294B0 
E7378FCD3C3C1B7DD54CA21915B7508529DD00E5ACA135C3ED200FBF86E7BE0BCA71624922CB9204 
3ABC2A858CD1674AF6AE8430928543CE815FCC0FBDA17C3EC6618C09D5C734A1FB067CAC0B9E5A2B 
12C65A972159CCC32BB7671814EBA097229349150700FE8B99DD63E0F10708F973EF6D5A208F921D 
AB409EE360D8E490F4F34DE81DC5395831C73E3280A2ECE7F99F98C74513270346C7FB522F870EED 
5101BB512C2AF7F0E0A78206AB1A78073859AD2BEF49E768A0F8337AA4E90418B6DC32DB24CD4AAD 
55D7DA38BF3471146809066A0D551EDCB6CEB440077F6EE5A3A5D8A78A46DDBBF0822C9A12F319F7 
67DA333A57553A81045FBB7B4570792567A4D328CB138F3D02CDDDF14917D9AD64363BA66AF121A4 
62CC18DF2D164BEEACD759D04A10B310E8695F4809847CBA37EE642E2F72E8D60B00E3698E35DABB 
2114CDEBC91777643F3D9A0DC9C608B43A61DC93113C8C210BF0597DE54A44B9389ED7D52A10B7FE 
87787C7C4B76C182FBCC40308EE6D0DEF2A59710E2F09D5A16D3B16EF4D3E56579B67AF5E2073EDB 
878B334E48481E80F888113BD1492853A8643BD7C5F79937DA533F93F72724FF92F9E90FBFC2ADE4 
7DB097ABC5801F3419090640222417279005AF6CC6B1FC81D75F24EF5937474CE96BBCCABCE64AC6 
A86B9A61E0FC01FBBA206E7581C2C238F0AA8A0FD5CC25BF262C3580712C30776F2948837C934427 
DC4CCF18CBD23EBA6425019B94CE6D813827BF55093A17A48E7701BAB8B0964DCD8502AC13C5FFC8 
C1E1DA704EB70B6059798D0691020446F0F4A73361B4F5659DC257F7876E924C3F0A67D6C9BD5748 
567272D463E8DABB77EE3F396F8F1EFD07C2329C3C768B563FF8ED3B350BE649C18B8A7B5D9BE6A8 
9EB468DDD3F8C1CABEDDF7199E748ED55E3A74C4AF615363 
6.9 SNMP Management  
SNMP stands for ‘Simple Network Management Protocol’ and is an application layer protocol that 
provides a message format for the communication between managers and agents. SNMP systems 
consist of an SNMP manager, an SNMP agent and a MIB. The NMS can be part of a management 
6. Management and Security 
network system. To configure SNMP, you have to define the relationship between the manager and the 
agent. Megaplex-4 supports SNMPv3, the latest SNMP version to date. SNMPv3 provides secure access 
to devices in the network such as Megaplex units by using authentication and data encryption. 
Standards Compliance 
The supported SNMP versions are based on the following standards:  
• 
RFC 1901, Introduction to Community-Based SNMPv2. SNMPv2 Working Group 
• 
RFC 1902, Structure of Management Information for Version 2 of the Simple Network 
Management Protocol (SNMPv2). SNMPv2 Working Group 
• 
RFC 1903, Textual Conventions for Version 2 of the Simple Network Management Protocol 
(SNMPv2). SNMPv2 Working Group 
• 
 RFC 1904, Conformance Statements for Version 2 of the Simple Network Management 
Protocol (SNMPv2). SNMPv2 Working Group 
• 
RFC 1905, Protocol Operations for Version 2 of the Simple Network Management Protocol 
(SNMPv2). SNMPv2 Working Group 
• 
RFC 1906, Transport Mappings for Version 2 of the Simple Network Management Protocol 
(SNMPv2) 
• 
RFC 1907, Management Information Base for Version 2 of the Simple Network Management 
Protocol (SNMPv2). SNMPv2 Working Group 
• 
RFC 1908, Coexistence between Version 1 and Version 2 of the Internet-standard Network 
Management Framework. SNMPv2 Working Group 
• 
RFC 2104, Keyed Hashing for Message Authentication 
• 
RFC 2271, Architecture for Describing SNMP Management Frameworks 
• 
RFC 2272, message processing and dispatching for the Simple Network Management Protocol 
(SNMP) 
• 
RFC 2273, SNMPv3 Applications 
• 
RFC 2274, User-Based Security Model (USM) for version 3 of the Simple Network Management 
Protocol (SNMPv3) 
• 
RFC 3412, Version 3 Message Processing and Dispatching 
• 
RFC 3414, User-based Security Model for SNMPv3   
6. Management and Security 
• 
RFC 3415, View-Based Access Control Model (VACM) for the Simple Network Management 
Protocol (SNMP) 
• 
RFC 3416, Update for RFC 1904 
Benefits 
The SNMP protocol allows you to remotely manage multiple units from a central work station using 
RADview EMS. RADview EMS offers a graphical user interface that resembles the front panel of your unit 
with its interfaces and LEDs. 
Megaplex-4 supports SNMPv3, which allows data to be collected securely from SNMP devices. 
Confidential information such as SNMP commands can thus be encrypted to prevent unauthorized 
parties from being able to access them. 
Functional Description 
In an SNMP configuration, one or more administrative computers manage a group of hosts or devices. 
Each managed system continuously executes a software component called agent, which reports 
information via SNMP back to the managing systems. 
get_request
traps
Megaplex Unit
(MIB, SNMP Agent)
Work Station with 
RADview 
(SNMP Manager)
get_response
get_next_request
get_response
set_request
get_response
 
SNMP Network Scheme 
The SNMP agent contains MIB variables whose values the SNMP manager can request or change. A 
manager receives/transmits a value from/to an agent. The agent gathers data from the MIB 
(Management Information Base). A MIB module is actually the ‘store’ for data on network and device 
6. Management and Security 
parameters. In addition, the agent may set or get data according to manager commands. Commands are 
used to send and receive data as follows: 
• 
get. Retrieving specific management information. 
• 
get-next. Retrieving management information via traversal 
• 
set. Manipulating management information. 
• 
get-response. Sent by an agent to respond to any of the above. 
• 
trap. Messages on events such as improper authentication, link status, loss/restoration of 
connections etc, sent by the agent to notify the manager of the current conditions. 
SNMP Message Formats 
Megaplex-4 supports SNMPv1, SNMPv2c and SNMPv3. The SNMP message formats of those three 
standards are illustrated below. Additional SNMPv2 formats exist, but are not supported by Megaplex-4. 
SNMPv1 Message Format 
The SNMP general message format was originally used to define the format of messages in the original 
SNMP Protocol (SNMPv1), and was therefore relatively straight-forward. 
The general message format in SNMPv1 is a wrapper that consists of a small header and an 
encapsulated PDU as illustrated and explained below. 
There are not many header fields needed in SNMPv1 because of the simple nature of the community-
based security method in SNMPv1. 
SNMPv1 Header Fields 
Field Name 
Syntax 
Size (Bytes) 
Description 
Version 
Integer 
4 
Version Number. Describes the SNMP version number of this 
message; used for ensuring compatibility between versions. 
For SNMPv1, this value is 0. 
Community 
Octet string 
Variable 
Community String. Identifies the SNMP community in which 
the sender and recipient of this message are located. This is 
used to implement the simple SNMP community-based 
security mechanism. 
PDU 
-- 
Variable 
Protocol Data Unit. The PDU is communicated at the body of 
the message. 
6. Management and Security 
0
16
32
Version Number = 0
Community String
PDU Control Fields
PDU Variable Bindings
Message Body (PDU)
 
 SNMPv1 General Message Format 
SNMPv2c Message Format 
Amongst various approaches to introduce SNMPv2, SNMPv2c was the most accepted one. Its 
architecture is identical to SNMPv1 except for the version number, which is 1 instead of 0. 0 is the 
version number for SNMPv1. 
SNMPv3 Message Format 
SNMPv3 adds security methods and parameters and completes the respective approach that has been 
started with SNMPv2, but did not lead to a common standard. This standard has been established with 
SNMPv3. 
The significant changes made in SNMPv3 include a more flexible way of defining security methods and 
parameters, to allow the coexistence of multiple security techniques. 
The general message format for SNMPv3 still follows the idea of an overall message “wrapper” that 
contains a header and an encapsulated PDU, but it has been significantly refined. The fields in the 
header have been divided into those dealing with security and those not dealing with security. The ’non-
6. Management and Security 
security’ fields are common to all SNMPv3 implementations, while the use of the ‘security’ fields can be 
tailored by each SNMPv3 security model, and processed by the module in an SNMP entity that deals 
with security. The entire processing in SNMPv3 is described in RFC 3412. 
For a detailed illustration and explanation, refer to the figure and the table below. 
6. Management and Security 
0
16
32
Message Version Number = 3
PDU Control Fields
PDU Variable Bindings
Message Body (PDU)
Message Identifier
Maximum Message Size
Message Security Model
(bytes 1 to 3)
Message Security Parameters
Context Engine ID
Context Name
Scoped PDU
        Message Flags
      Message Security
            Model (byte 4)
0
4
8
Reserved
Reportable
Flag
Privacy
Flag
(Priv)
Authen-
tication
Flag
(Auth)
 
6. Management and Security 
SNMPv3 General Message Format 
SNMPv3 General Message Format 
Field Name 
Syntax 
Size (Bytes) 
Description 
Msg Version 
Integer 
4 
Message Version Number. Describes the SNMP version 
number of this message; used for ensuring compatibility 
between versions. For SNMPv3, this value is 3. 
Msg ID 
Integer 
4 
Message Identifier. A number used to identify an SNMPv3 
message and to match response messages to request 
messages. This field was created to allow the matching at the 
message processing level to protect against certain security 
attacks regardless of the PDU content. Thus, Msg ID and 
Request ID are used independently. 
Msg Max Size 
Integer 
4 
Maximum Message Size. The maximum size of message that 
the sender of this message can receive. Minimum value of 
this field is 484. 
Msg Flags 
Octet String 
1 
Message Flags. A set of flags tcontrols processing the 
message. The substructure of this field is illustrated in the 
SNMPv3 Message Flag Substructure table. 
Msg Security 
Model 
Integer 
4 
Message Security Model. An integer value indicating which 
security model was used for this message. For the user-based 
security model (default), this value is 3. 
Msg Security 
Parameter 
-- 
Variable 
Message Security Parameters. A set of fields that contain 
parameters required to implement the respective security 
model for this message. The contents of this field are 
specified in every document that describes an SNMPv3 
security model. For example, the parameters for the user-
based model are defined in RFC 3414. 
Scoped PDU 
-- 
Variable 
Scoped PDU. Contains the PDU to be transmitted along with 
parameters that identify an SNMP context, which describes a 
set of management information accessible by a particular 
entity. The PDU is referred to as ‘scoped’ because it is applied 
within the scope of this context. This field may or may not be 
encrypted, depending on the value of the Private Flag. The 
structure of the PDU field is illustrated in the Structure of the 
PDU Field table.  
6. Management and Security 
SNMPv3 Message Flag Substructure 
Field Name 
Size (Bytes) 
 
Reserved 
5/8 (5 bits) 
Reserved. For future use 
Reportable Flag 
1/8 (1 bit) 
Reportable Flag. If set to 1, a device receiving this message has to 
return a Report-PDU whenever conditions arise that require such a 
PDU to be generated. 
Priv Flag 
1/8 (1 bit) 
Privacy Flag. If set to 1, it indicates that the message was 
encrypted to ensure its privacy. 
Auth Flag 
1/8 (1 bit) 
Authentication Flag. If set to 1, it indicates that authentication was 
used to protect the authenticity of this message. 
Structure of the PDU Field 
Field Name 
Syntax 
Size (Bytes) 
Description 
Context Engine ID 
Octet String 
Variable 
Context Engine ID. Used to identify to which 
application the PDU will be sent for processing. 
Context Name 
Octet String 
Variable 
Context Name. An object identifier specifying the 
particular context associated with this PDU. 
PDU 
-- 
Variable 
PDU. The protocol data unit being transmitted. 
The SNMPv3 Mechanism 
SNMPv3 uses the basic SNMP protocol and adds the following security functionalities: 
• 
Message integrity. Ensuring that the package has not been tempered with during transmission. 
• 
Authentication. Verifying that the message comes from a valid source. 
• 
Encryption. Preventing snooping by unauthorized sources. 
SNMPv3 does not refer to managers and agents, but to SNMP entities. Each entity consists of an SNMP 
engine and one or more SNMP components. The new concepts define an architecture that separates 
different components of the SNMP system in order to make a secure implementation possible. The 
SNMPv3 components are explained in the following sections. 
The SNMPv3 Engine 
The SNMPv3 engine consists of four subsystems that address authentication and access authorization. 
6. Management and Security 
• 
Dispatcher. Sending and receiving messages. It tries to determine the SNMP version of each 
message (SNMPv1, SNMPv2c or SNMPv3) once it is handed over to the message processing 
subsystem. 
• 
Message processing subsystem. Prepares messages to be sent and extracts data from received 
messages.  
• 
Security subsystem. Provides authentication and privacy services. The authentication uses 
either community strings to support SNMP Versions 1 and 2, or user-based authentication for 
SNMPv3. SNMPv3 user-based authentication uses the MD5 or SHA algorithms to authenticate 
users without sending a clear password. The privacy service uses the DES algorithm to encrypt 
and decrypt SNMP messages. Currently, DES is the only algorithm used, though others may be 
added in the future. 
• 
Access control system. Managing the access control to MIB objects. You can define objects that 
a user can access as well as operations that a user is allowed to perform on those objects. For 
example, you may grant read-write access to certain parts of the MIB-2 tree, while allowing 
read-only access to the remaining parts of the tree. 
SNMPv3 Components 
SNMPv3 consists of components that deal with receiving/issuing requests, generating traps etc. These 
commands are listed and explained below. 
• 
Command generator. Generates the Get, Get-Next, Get-Bulk requests, Set requests, and 
processes the responses. This application is implemented by an NMS to issue queries and set 
requests against entities on routers, switches, Unix hosts etc. 
• 
Command responder. Responds to Get, Get-Next, Get-Bulk requests. The command responder 
is implemented by the SNMP agent. 
• 
Notification originator. Generates SNMP traps and notifications. This application is 
implemented by an entity on a router or host. 
• 
Proxy forwarder. Facilitates the passing of messages between entities.  
RFC 2571 allows additional applications to be defined over time, which is a significant advantage over 
the older SNMP versions. The figure below illustrates how the components fit together creating an 
entity. 
6. Management and Security 
SNMP Entity
SNMP Engine  (idntified by SnmpEngineID)
SNMPv3 Components
Dispatcher
Message
Processing
Subsystem
Security
Subsystem
Access
Control
Subsystem
Command Generator
Notification Receiver
Proxy Forwarder
Command Responder
Notification Originator
Other
 
SNMPv3 Entity 
Factory Defaults 
By default, SNMPv1 is enabled. SNMPv2c and SNMPv3 are disabled.  
Configuring SNMPv3 
Megaplex-4 supports SNMP version 3, providing secure SNMP access to the device by authenticating 
and encrypting packets transmitted over the network. 
The SNMPv3 manager application in RADview provides a user-friendly graphical interface to configure 
SNMPv3 parameters. If you intend to use it, you must first use the device CLI to create users with the 
required encryption method and security level, as the application can create users based only on 
existing users; the new user has the same encryption method, and the same security level or lower. The 
Megaplex-4 default configuration provides only one standard user named “initial” with no encryption 
and the lowest security level. 
 To configure SNMPv3: 
1. Set SNMP engine ID if necessary. 
2. Add users, specifying authentication protocol and privacy protocol.  
6. Management and Security 
3. Add groups, specifying security level and protocol. 
4. Connect users to groups. 
5. Add notification entries with assigned traps and tags. 
6. Configure target parameter sets to be used for targets. 
7. Configure targets (SNMPv3 network management stations to which Megaplex-4 should send 
trap notifications), specifying target parameter sets and notification tags. 
 To configure SNMPv3 parameters: 
1. Navigate to configure management snmp. 
The config>mngmnt>snmp# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Note 
When you enter password parameters, they should contain at least eight 
characters 
 
Task 
Command 
Level 
Comments 
Configuring group 
access-group <group-name> { snmpv2c | usm } 
{ no-auth-no-priv | auth-no-priv | auth-priv } 
snmp 
no access-group deletes the group  
Defining context 
matching 
context-match {exact | prefix} 
snmp>access-gro
up 
 
Setting notify view 
of group 
notify-view <name> 
snmp> 
access-group 
 
Setting read view of 
group 
read-view <name> 
snmp> 
access-group 
 
Setting write view of 
group 
write-view <name> 
snmp> 
access-group 
 
Administratively 
enabling group 
no shutdown 
snmp> 
access-group 
 
Configuring 
community 
community <community-index> 
snmp 
 
Configuring name 
name <community-string> 
snmp> 
community 
 
Configuring security 
name 
sec-name <security-name> 
snmp> 
community 
 
6. Management and Security 
Task 
Command 
Level 
Comments 
Configuring 
transport tag 
tag <transport-tag> 
snmp> 
community 
This should be normally set to the 
default value 
Administratively 
enabling community 
no shutdown 
snmp> 
community 
shutdown disables community 
Enabling/disabling 
generation of 
configuration 
change trap  
config-change-notification 
snmp> 
Configuration change trap is sent upon 
any configuration change in the device 
(initiated from CLI or SNMP). It contains 
information about all the modified 
entries and variables; if trap has too 
many variables, it is divided into several 
configuration change traps. 
Enable configuration change 
notifications only after I/O card have 
been provisioned, using the card-type 
command. Otherwise, the system will 
be flooded with mandatory 
notifications, generated, when a card 
type is changed. 
Configuring 
notifications  
notify <notify-name> 
snmp> 
 
6. Management and Security 
Assigning trap to 
notification 
bind {coldStart | linkDown | linkUp | 
authenticationFailure | 
systemDeviceTemperatureOra | 
systemSoftwareInstallEnd | 
systemAlternateConfigLoaded | 
systemDyingGasp | systemDeviceStartup | 
systemSwUnconfirmed | 
systemStartupConfigUnconfirmed | fanFailure 
| systemSuccessfulLogin | systemFailedLogin | 
systemLogout | powerDeliveryFailure | 
systemTrapHardSyncStart | 
systemTrapHardSyncEnd | systemUserReset | 
smartSfpMismatch | systemRfc2544TestStart | 
systemRfc2544TestEnd | 
clockDomainSystemClockUnlock | 
sourceClockFailure | stationClockLos | 
clockDomainStationClockUnlock | 
ptpRecoveredUnacceptableFrequencyAccuracy 
| ptpRecoveredMasterDisqualification | 
ptpRecoveredPtpStateChange | 
ptpRecoveredSevereFrequencyCondition | 
epsConfigurationMismatch | 
epsPortSwitchover | sfpRemoved | ethLos | 
oamEfmRemoteLoopback | 
oamEfmRemoteLoopbackOff | 
oamEfmCriticalLinkIndication | 
oamEfmFeCriticalLinkIndication | 
oamEfmDyingGaspIndication | 
oamEfmFeDyingGaspIndication | sdhSonetLos 
| e3t3Los | e1t1Los | systemDownloadEnd | 
oamCfmMepAis | oamCfmMepLck | 
oamCfmMepMismatch | oamCfmRmepLoc | 
oamCfmRmepRdi | oamCfmDestNeDelayTca | 
oamCfmDestNeDelayTcaOff | 
oamCfmDestNeDelayVarTca | 
oamCfmDestNeDelayVarTcaOff | 
oamCfmDestNeLossRatioTca | 
oamCfmDestNeLossRatioTcaOff | 
oamCfmDestNeLossRatioTcaFe | 
oamCfmDestNeLossRatioTcaFeOff | 
oamCfmDestNeUnavailableRatioTca | 
oamCfmDestNeUnavailableRatioTcaOff | 
oamCfmDestNeUnavailableRatioTcaFe | 
oamCfmDestNeUnavailableRatioTcaFeOff} 
snmp>notify 
You can assign more than one trap to a 
notification, in separate commands 
6. Management and Security 
Task 
Command 
Level 
Comments 
Assigning tag to 
notification, to be 
used to identify the 
notification entry 
when configuring 
target  
tag <tag-value> 
snmp>notify 
 
Administratively 
enabling notification 
no shutdown 
snmp>notify 
 
Configuring 
notification filter to 
define access to a 
particular part of the 
MIB hierarchy for 
trap variables 
notify-filter <name> <sub-tree-oid> 
snmp 
 
Specifying the part 
of the subtree OID 
to use in order to 
define the MIB 
subtree 
mask [<mask>] 
snmp>notify-filter  
Defining whether 
traps with trap 
variables belonging 
to the MIB subtree 
are sent 
type {included | excluded} 
snmp>notify-filter  
Administratively 
enabling notification 
filter 
no shutdown 
snmp>notify-filter  
Configuring 
notification filter 
profile 
notify-filter-profile <params-name> 
snmp>filter-profil
e 
 
Configuring 
notification filter 
profile name 
profile-name <argument> 
snmp>filter-profil
e 
 
Administratively 
enabling notification 
filter profile 
no shutdown 
snmp>filter-profil
e 
 
6. Management and Security 
Task 
Command 
Level 
Comments 
Connecting security 
name to group (e.g. 
connecting user or 
community to 
group)  
security-to-group { snmpv2c | usm } 
sec-name <security-name> 
snmp 
no security-to-group removes 
security-to-group entity 
Specifying group to 
which to connect 
security name 
group-name <group-name> 
snmp>security-to-
group 
 
Administratively 
enabling 
security-to-group 
entity 
no shutdown 
snmp>security-to-
group 
shutdown disables the 
security-to-group entity 
Setting SNMP 
engine ID, as MAC 
address or IP 
address or string 
snmp-engine-id mac [ <mac-address> ] 
snmp-engine-id ipv4 [ <ip-address> ] 
snmp-engine-id text <string> 
snmp 
If you use the mac option and don’t 
specify the MAC address, the SNMP 
engine ID is set to the device MAC 
address 
If you use the ipv4 option and don’t 
specify the IP address, the SNMP engine 
ID is set to the device IP address 
Configuring target 
(SNMPv3 network 
manager) 
target <target-name> 
snmp 
no target removes target  
Specifying target 
address as IP 
address or OAM 
port 
address udp-domain <ip-address> address 
oam-domain <oam-port> 
snmp>target 
 
Assigning tag(s) to 
target (the tag(s) 
must be defined in 
notification entries) 
tag-list <tag> 
tag-list [ <tag> ] 
tag-list [ <tag1>,<tag2>,…<tagn> ] 
snmp>target 
If you specify more than one tag, you 
must enclose the list in square brackets; 
if you  specify just one tag, the brackets 
are optional 
Specifying set of 
target parameters 
for target 
target-params <params-name> 
snmp>target 
 
6. Management and Security 
Task 
Command 
Level 
Comments 
Specifying trap 
synchronization 
group 
trap-sync-group <group-id> 
[import-trap-masking] 
• If the group does not exist, it is 
created 
• If you specify the 
import-trap-masking parameter, the 
manager’s trap masking is imported 
from the first manager in the group 
• Enter no trap-sync-group <group-id> 
to remove the manager from the 
group. If the manager was the last in 
the group, the group is deleted. 
Administratively 
enabling target  
no shutdown 
snmp>target 
shutdown disables target  
Configuring set of 
target parameters, 
to be assigned to 
target 
target-params <target-param-name> 
snmp 
no target-params removes target 
parameters 
Specifying message 
processing model 
(SNMP version) to 
be used when 
generating SNMP 
messages for the set 
of target parameters 
message-processing-model 
{ snmpv2c | snmpv3 } 
snmp>target 
 
Specifying user on 
whose behalf SNMP 
messages are to be 
generated for the 
set of target 
parameters 
security [ name <security-name> ] 
[ level { no-auth-no-priv | 
auth-no-priv  | auth-priv } ] 
snmp>target 
 
Specifying SNMP 
version to be used 
when generating 
SNMP messages for 
the set of target 
parameters 
version { snmpv2c | usm } 
snmp>target 
Use usm for SNMPv3 version 
Administratively 
enabling target 
parameters 
no shutdown 
snmp>target 
shutdown disables target parameters 
6. Management and Security 
Task 
Command 
Level 
Comments 
Configuring target 
parameters and tags 
for trap 
synchronization 
group  
trap-sync-group <group-id> 
snmp 
The trap synchronization group must be 
previously defined in the target level 
Specifying tags 
tag-list <list> 
snmp>trap-sync-g
roup 
To remove the tag list, enter: no tag-list 
Specifying set of 
target parameters 
target-params <params-name> 
snmp>trap-sync-g
roup 
To remove the tag list, enter: no 
target-params <params-name> 
Configuring user 
user <security-name> 
[md5-auth [ {des | none} ] ] 
user <security-name> 
[sha-auth [ {des | none} ] ] 
user <security-name> [none-auth] 
snmp 
If you don’t specify the authentication 
method when creating a user, the 
default is MD5 with DES privacy 
protocol. To create a user with no 
authentication, specify none-auth. 
no user <security-name> deletes the 
user 
Setting user 
authentication 
password and 
optional key for 
changes 
authentication [ password <password> ] 
[ key <key-change> ] 
snmp>user 
no authentication disables 
authentication protocol 
Setting user privacy 
password and 
optional key for 
changes 
privacy [ password <password> ] 
[ key <key-change> ] 
snmp>user 
no privacy disables privacy protocol 
Administratively 
enabling user 
no shutdown 
snmp>user 
• You must define the authentication 
and privacy method before you can 
enable the user, unless the user was 
defined with no authentication 
(none-auth) 
• shutdown disables the user. 
Defining access to a 
particular part of the 
MIB hierarchy 
view <view-name> <sub-tree-oid> 
snmp 
view-name –Name of view, which can 
be associated to a group as a notify, 
read, or write view  
sub-tree-oid – OID that defines the MIB 
subtree (for example 1.3.6.1 represents 
the Internet hierarchy) 
6. Management and Security 
Task 
Command 
Level 
Comments 
Specifying the part 
of the subtree OID 
to use in order to 
define the MIB 
subtree 
mask <mask> 
snmp>view 
The mask is comprised of binary digits 
(for example, the mask 1.1.1 converts 
OID 1.3.6.7.8 to 1.3.6). It is not 
necessary to specify a mask if 
sub-tree-oid is the OID that is used to 
define the MIB subtree 
Defining whether 
access to the MIB 
subtree is allowed  
type {included | excluded} 
snmp>view 
included – Allows access to the subtree 
excluded – Disables access to the 
subtree 
Administratively 
enabling view 
no shutdown 
snmp>view 
 
Displaying trap 
synchronization 
groups and 
members for 
SNMPv3 manager 
groups 
show trap-sync 
snmp 
 
Displaying SNMPv3 
information, such as 
the number of times 
the SNMPv3 engine 
has booted, and 
how long since the 
last boot 
show snmpv3 information 
snmp 
 
Mapping SNMPv1 to SNMPv3 
Megaplex-4 supports coexistence of different SNMP versions by mapping SNMPv1/SNMPv2 community 
names to the SNMPv3 security name values. The mapping is performed according to the RFC 3584 
requirements. 
 To set up an SNMPv3 community: 
• 
At the config>mngmnt>snmp# prompt, enter parameters as illustrated and explained below. 
The config>mngmnt>snmp>community(<community-index>)# prompt appears. 
6. Management and Security 
Task 
Command 
Comments 
Defining a community 
community <community-index> 
community-index. Free text, consisting of 
up to 32 alphanumeric characters. 
Removing a community 
no community <community-index> 
 
 To map an SNMPv1/SNMPv2 community to SNMPv3: 
• 
At the config>mngmnt>snmp>community(<community-index>)# prompt, enter parameters as 
illustrated and explained below. 
Task 
Command 
Comments 
Specifying the SNMPv1/SNMPv2 
community name for which the 
information is presented. 
name <community-string> 
community-string. Free text, 
consisting of up to 32 alphanumeric 
characters. 
Specifying the SNMPv3 security name to 
be mapped to the SNMPv1/SNMPv2 
community name 
sec-name <sec-name> 
sec-name. Free text, consisting of up 
to 32 alphanumeric characters 
Activating the community 
no shutdown 
 
De-activating the community 
shutdown 
The community is de-activated, but 
remains available. 
Specifying a set of the transport 
endpoints that are used in either of the 
following methods: 
• Specifying the transport endpoints 
from which an SNMP entity accepts 
management requests. 
• Specifying the transport endpoints 
to which a notification may be sent, 
using the community string 
matching the corresponding 
instance of community name. 
tag <transport-tag> 
As defined for each target 
Configuring SNMP Communities for SNMPv1  
This section instructs you on setting up read-, write-, and trap communities for SNMPv1. 
6. Management and Security 
 To set up communities: 
• 
Make sure that SNMPv3 is disabled and at the  
Megaplex-4>config>mngmnt>snmp# prompt, define the desired community as illustrated and 
explained below. 
Task 
Command 
Comments 
Defining a read community 
community read <name> 
Assign a name consisting of up to 20 
alphanumerical characters. 
Defining a write community 
community write <name> 
Assign a name consisting of up to 20 
alphanumerical characters. 
Defining a trap community 
community trap <name> 
Assign a name consisting of up to 20 
alphanumerical characters. 
 
Note 
The names you assign to the communities are case sensitive. 
Example 
 To create SNMPv3 user and connect it to group: 
• 
User named “MD5_priv”: 
 
Security level – MD5 authentication, DES privacy 
• 
Group named "SecureGroup": 
 
All security levels 
 
Contains set of views named "internet" (from default configuration). 
 
 
# configure management snmp 
config>mngmnt>snmp# user MD5_priv md5-auth des 
The picture can't be displayed.
6. Management and Security 
config>mngmnt>snmp>user(MD5_priv)$ privacy password MD654321 
config>mngmnt>snmp>user(MD5_priv)$ authentication password MD654321 
config>mngmnt>snmp>user(MD5_priv)$ no shutdown 
config>mngmnt>snmp>user(MD5_priv)$ exit 
config>mngmnt>snmp# access-group MD5Group usm no-auth-no-priv  
config>mngmnt>snmp>access-group(MD5Group/usm/no-auth-no-priv)$ context-match prefix 
config>mngmnt>snmp>access-group(MD5Group/usm/no-auth-no-priv)$ read-view internet 
config>mngmnt>snmp>access-group(MD5Group/usm/no-auth-no-priv)$ write-view internet 
config>mngmnt>snmp>access-group(MD5Group/usm/no-auth-no-priv)$ notify-view internet 
config>mngmnt>snmp>access-group(MD5Group/usm/no-auth-no-priv)$ no shutdown  
config>mngmnt>snmp>access-group(MD5Group/usm/no-auth-no-priv)$ exit 
config>mngmnt>snmp# access-group MD5Group usm auth-no-priv  
config>mngmnt>snmp>access-group(MD5Group/usm/auth-no-priv)$ context-match prefix 
config>mngmnt>snmp>access-group(MD5Group/usm/auth-no-priv)$ read-view internet 
config>mngmnt>snmp>access-group(MD5Group/usm/auth-no-priv)$ write-view internet 
config>mngmnt>snmp>access-group(MD5Group/usm/auth-no-priv)$ notify-view internet 
config>mngmnt>snmp>access-group(MD5Group/usm/auth-no-priv)$ no shutdown  
config>mngmnt>snmp>access-group(MD5Group/usm/auth-no-priv)$ exit 
config>mngmnt>snmp# access-group MD5Group usm auth-priv 
config>mngmnt>snmp>access-group(MD5Group/usm/auth-priv)$ context-match prefix 
config>mngmnt>snmp>access-group(MD5Group/usm/auth-priv)$ read-view internet 
config>mngmnt>snmp>access-group(MD5Group/usm/auth-priv)$ write-view internet 
config>mngmnt>snmp>access-group(MD5Group/usm/auth-priv)$ notify-view internet 
config>mngmnt>snmp>access-group(MD5Group/usm/auth-priv)$ no shutdown  
config>mngmnt>snmp>access-group(MD5Group/usm/auth-priv)$ exit 
config>mngmnt>snmp# security-to-group usm sec-name MD5_priv 
config>mngmnt>snmp>security-to-group(usm/MD5_priv)$ group-name MD5Group 
config>mngmnt>snmp>security-to-group(usm/MD5_priv)$ no shutdown 
config>mngmnt>snmp>security-to-group(usm/MD5_priv)$ exit 
config>mngmnt>snmp# 
 To create notifications: 
• 
Notification  named “TrapData”: 
 
Tag = “Data” 
 
Bound to agnStatusChangeTrap, agnUploadDataTrap. 
• 
Notification  named “TrapPower”: 
 
Tag = “Power” 
 
Bound to agnPowerFailureTrap, coldStart. 
# configure management snmp 
config>mngmnt>snmp# notify TrapPort 
config>mngmnt>snmp>notify(TrapPort)$ tag Port 
config>mngmnt>snmp>notify(TrapPort)$ bind ethLos  
config>mngmnt>snmp>notify(TrapPort)$ bind sfpRemoved 
config>mngmnt>snmp>notify(TrapPort)$ no shutdown 
config>mngmnt>snmp>notify(TrapPort)$ exit 
6. Management and Security 
config>mngmnt>snmp# notify TrapPower 
config>mngmnt>snmp>notify(TrapPower)$ tag Power 
config>mngmnt>snmp>notify(TrapPower)$ bind powerDeliveryFailure  
config>mngmnt>snmp>notify(TrapPower)$ bind systemDeviceStartup 
config>mngmnt>snmp>notify(TrapPower)$ no shutdown 
config>mngmnt>snmp>notify(TrapPower)$ exit 
config>mngmnt>snmp# 
 To create target parameters and target: 
• 
Target parameters  named “TargParam1”: 
 
Message processing model SNMPv3 
 
version USM 
 
User “MD5_priv”  
 
Security level authentication and privacy 
• 
Target named “TargNMS1”: 
 
Target parameters  “TargParam1” 
 
Tag list = “Data”, “Power” 
 
IP address 192.5.4.3. 
# configure management snmp 
config>mngmnt>snmp# target-params TargParam1 
config>mngmnt>snmp>target(TargParam1)$ message-processing-model snmpv3 
config>mngmnt>snmp>target(TargParam1)$ version usm 
config>mngmnt>snmp>target(TargParam1)$ security name MD5_priv level auth-priv 
config>mngmnt>snmp>target(TargParam1)$ no shutdown 
config>mngmnt>snmp>target(TargParam1)$ exit 
config>mngmnt>snmp# target TargNMS1 
config>mngmnt>snmp>target(TargNMS1)$ target-params TargParam1 
config>mngmnt>snmp>target(TargNMS1)$ tag-list [Port,Power] 
config>mngmnt>snmp>target(TargNMS1)$ address udp-domain 192.5.4.3 
config>mngmnt>snmp>target(TargNMS1)$ no shutdown 
config>mngmnt>snmp>target(TargNMS1)$ exit 
config>mngmnt>snmp# 
 To display SNMPv3 information: 
# configure management snmp 
 config>mngmnt>snmp# show snmpv3 information 
SNMPv3           : enable  
Boots            : 2          
Boots Time (sec) : 102        
EngineID         : 800000a4030020d2202416 
config>mngmnt>snmp# 

## 6.10 User Access  *(p.545)*

6. Management and Security 
6.10 User Access 
Megaplex-4 management software allows you to define new users, their management and access rights. 
Only superusers (su) can create new users, the regular users are limited to changing their current 
passwords, even if they were given full management and access rights.  
You can specify a user password as a text string. You can add a second user with the same password 
using the hash function as explained below. 
Factory Defaults 
By default, the following users exist, with default password 1234: 
• 
su 
• 
tech 
• 
user. 
 To add a new user: 
1. Make sure that you are logged on as superuser (su). 
2. Navigate to the Management context (config>mngmnt). 
3. Define a new user: user <name> [ level { su | tech | user } ] [[ password <password> [hash] ] 
Defining Users and Passwords 
Follow the instructions below to add users and assign passwords. 
6. Management and Security 
Notes 
• 
User passwords are stored in a database so that the system can perform 
password verification when a user attempts to log in. To preserve 
confidentiality of system passwords, the password verification data is 
typically stored after a one-way hash function is applied to the password, 
in combination with other data. When a user attempts to log in by 
entering a password, the same function is applied to the entered value 
and the result is compared with the stored value. 
• 
A cryptographic hash function is a deterministic procedure that takes an 
arbitrary block of data and returns a fixed-size bit string, the 
(cryptographic) hash value, such that any change to the data changes the 
hash value. 
 To add a new user: 
1. Make sure that you are logged on as superuser (su). 
2. At the user prompt config>mngmnt>, enter  
user <name> [level <debug | su | oper | tech | user>] [password <password of up to 40 
characters>]. 
The user name, the associated user level and the password are defined. 
 To add another user with the same password using the hash function: 
1. At the user prompt config>mngmnt> prompt, enter info. 
The first user’s password’s hash value appears as illustrated below. 
config>mngmnt# info 
user  "staff1" level  user  password  "3fda26f8cff4123ddcad0c1bc89ed1e79977acef"  hash  
2. Define another user with the hashed password obtained from the info output. 
The second user is added and can log on with the text password defined in step 1. 
 To delete an existing user: 
• 
At the config>mngmnt# prompt, enter no user <name>. 
The specified user is deleted. 
6. Management and Security 
Example 
 To add a super user with a text password and access to all possible ways of management: 
• 
Specify the user name staff for the user level su. 
• 
Assign the password 1234. 
config>mngmnt# user staff level su password 1234  
# Password is encrypted successfully 
Megaplex-4>config>mngmnt# 
 To add two new users with identical passwords using the hash function: 
• 
Assign the user name staff1. 
• 
Assign the password 4222. 
• 
Assign the user name staff2. 
• 
Assign the same password 4222 to staff2 by linking the hash output to staff2. 
config>mngmnt# user staff1 level user password 4222  
# Password is encrypted successfully 
Megaplex-4>config>mngmnt# info 
    user  "staff1" level  user  password  "3fda26f8cff4123ddcad0c1bc89ed1e79977acef"  
hash  
    user  "su" 
 
config>mngmnt# user staff2 level user password 
3fda26f8cff4123ddcad0c1bc89ed1e79977acef hash 
config>mngmnt# info 
    user  "staff1" level  user  password  
"3fda26f8cff4123ddcad0c1bc89ed1e79977acef"  hash  
    user  "staff2" level  user  password  
"3fda26f8cff4123ddcad0c1bc89ed1e79977acef"  hash 
    user  "su" 
 
6. Management and Security 
config>mngmnt# logout  
CLI session is closed  
user>staff2 
password>4222 
# 
Viewing Connected Users 
This section explains how to view users currently logged on to the unit. 
 To view all connected users: 
• 
At the config>mngmnt# prompt, enter show users. 
A list of all connected users is displayed, showing their access level, the type of connection, and 
the IP address from which they are connected. 
onfigure management 
nfig>mngmnt# show users 
er                          Access Level   Source         IP-address      
--------------------------------------------------------------------------- 
                           SU             Terminal       172.4.3.3         
 
 