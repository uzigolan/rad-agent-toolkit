# 6 Management and Security

*Manual `ETX-1p_6.4_Mn_05-26_GA.pdf`, pages 273–421.*


## (chapter introduction)  *(p.273)*

6. Management and Security 
6 Management and Security  
This chapter describes the following:   
• 
Access Control List (ACL)  
• 
Management access methods 
• 
Management and configuration options  
• 
Management-related features 
 
Usually, initial configuration of the management parameters is performed via an ASCII terminal. Once a 
router interface has been configured, it is possible to access ETX-1p via NETCONF or SNMP for operation 
configuration. For details on configuring the router, refer to Router.  
The following table summarizes management options for ETX-1p. 
 
Port 
Manager 
Location 
Transport 
Method 
Management 
Protocol 
Application 
CONTROL 
 
Local 
Out-of-band 
N/A 
Terminal emulation applications such 
as HyperTerminal, Procomm, Putty, 
SecureCRT, Tera Term (refer to 
Working with Terminal). 
Ethernet 
FE/GbE 
 
Local, remote 
Inband 
SSH 
Terminal emulation application (refer 
to Working with SSH) 
SNMP 
Third-party NMS 
 
Note 
By default, the terminal and SNMP management access methods are enabled. 
See the following section for details on enabling/disabling a particular 
method.  

## 6.1 Access Control List (ACL)  *(p.274)*

6. Management and Security 
6.1 Access Control List (ACL)  
ETX-1p supports Access Control Lists (ACLs) to flexibly filter incoming and outgoing IPv4 and IPv6 traffic.  
Applicability and Scaling 
This feature is applicable to all versions of ETX-1p. 
The number of rules an ACL can contain is limited by the hardware device. 
Standards Compliance 
RFC 1812 -  Requirements for IP Version 4 Routers 
Benefits 
Service providers use ACLs to maintain network security by preventing malicious traffic from entering 
the device. ACLs can be used to save network resources by dropping unwanted packets.  
Functional Description 
Devices featuring ACLs can flexibly filter management and user traffic, by denying or permitting IP 
packets to enter the host, according to the packet’s source/destination address, protocol type, or other 
criteria. 
ACL entries are sequentially numbered rules containing statements (Deny, Permit, or Remark) and 
conditions. Statements in the access list are sorted and checked in ascending order of the statements’ 
sequence numbers. Remarks are free-text ACL entries used for commenting and visually organizing 
ACLs. 
Packets are permitted or denied access, based on the following mandatory conditions: 
• 
protocol (IP, TCP, UDP, and ICMP) 
• 
source IP address 
• 
destination IP address 
6. Management and Security 
The following parameters are optional: 
• 
source port, if the protocol is TCP or UDP 
• 
destination port, if the protocol is TCP or UDP 
• 
DSCP value 
• 
sequence number 
• 
ICMP type and code, if the protocol is ICMP 
• 
IP protocol number, if the protocol is IP 
The ACL structure is illustrated in the Management-Level Tasks section. 
If there is a need to add a rule between already existing rules with consecutive numbers, the rules can 
be interspaced to accommodate additional rules between them. For example, if you apply resequencing 
to an ACL including rules 1, 2, and 3, with an interspacing value of 30, the rule numbers change to 30, 60 
and 90. Sequence numbers can also be set at the rule level. 
ACLs are referred by name, which have to be unique, even for different IP version ACLs. To be active an 
ACL has to be bound to an entity, which could be physical or logical port. The ACL can filter incoming or 
outgoing traffic. One IPv4 and one IPv6 may be bound to an entity in each direction. 
Binding Access Control Lists 
Once created, ACLs are applied (bound) to an entity, which could be physical or logical port. The ACL can 
filter incoming or outgoing traffic. One IPv4 and one IPv6 may be bound to an entity in each direction. 
If an entity bound to an ACL is deleted, all associated ACLs are automatically detached. 
Multiple access lists can be configured; however, only one IPv4 ACL can be attached per management 
entity (and it must be in the incoming direction) or port. An additional IPv6 ACL may coexist with one 
IPv4 access list on the same interface / management entity. 
Filtering 
Packets attempting to enter an entity to which the ACL is bound are checked against the access list rules, 
one by one. Access of matching packets is denied (packets are dropped) or permitted (packets are 
forwarded), as directed by the ACL statement. ACL has three types of rules: 
Remark 
Free-text comment used as a bookmark in an ACL for better arrangement 
Deny 
ACL rule specifying fields to match. Matching packet is dropped if it was not permitted by a 
previous rule. 
6. Management and Security 
Permit 
ACL rule specifying fields to match. Matching packet is permitted if it was not denied by a 
previous rule. 
Fields to match are IP addresses, upper-layer protocols, ports, and other IP packet fields. After a match, 
the rest of the rules are ignored. Packets not matching any rule are dropped. Empty ACLs deny access of 
all packets matched to them. 
If a packet is denied, ETX-1p sends an ICMP Destination Unreachable message. To protect the network 
from bandwidth exhaustion attack, the unreachable messages rate is limited for all denied packets.  
When a rule match occurs, an entry is added to the event log if logging is enabled. To prevent log 
overflow, it is possible to disable logging (per rule or device) or define the minimal logging interval of 
packets matching ACL entries (per device).  
Note 
By default, logging is disabled. If you choose to enable it, the default logging 
interval is five minutes.  
Two packets matching the same rule on the same entity in the same direction are logged only if the time 
between them exceeds the logging interval.  
Firewall Additions to ACL Lists  
You can configure packet limits for an ACL permit rule. Setting a limit means that packets matching the 
rule are permitted up to the limit. Over the limit packets are discarded. The following arguments are 
supported: 
• 
Packets arriving at a higher rate than limit-rate (1-4294967295 PPS) are discarded. A burst of up 
to rate-burst (1-4294967295) packets is allowed.  
• 
Packets arriving at a higher rate than limit-size (1-4294967295 Kbytes per second) are discarded. 
A burst of up to size-burst (1-429967295) packets is allowed.  
• 
limit-connections is the maximum number of simultaneous connections (1-4294967295) allowed 
for an ACL rule. Packets of a new connection matching the rule, and arriving after limit-
connections has been reached, are discarded. 
Statistics 
The device collects ACL statistics per router, ETX-1p and management entity. The statistic counters 
include the number of rule matches that occurred since the counters were last cleared. The statistic 
counters are cleared upon device reboot. The user may also clear ACL statistics of any entity. 
6. Management and Security 
Factory Defaults 
Parameter defaults are alphabetically listed in the tables below. 
Topic 
Parameter 
Default Value 
Access List 
access-list type 
ipv4 
All ACL Rules 
ACL statement sequence 
Highest number in use in the ACL plus 10 
Deny/Permit Rule 
dst-port-range 
All values are filtered. 
rate-burst (permit only) 
0  
sequence-number 
The last sequence number in use increased by 
ten. 
size-burst (permit only) 
5 
src-port-range 
All values are filtered. 
Configuring ACL via CLI  
The ACL configuration tasks are performed at the access control and management levels. 
 To configure ACL: 
1. Create an access control list. 
2. Add deny and permit rules to the ACL. 
3. Bind the ACL to a management entity (See Configuring Ethernet Port Parameters for binding an 
Ethernet port or Configuring VLAN Port Parameters for binding a VLAN port). 
Access-Control-Level Tasks 
The following commands are available in the CLI access-control context: config>access-control#. The 
exception to this are the deny, permit, and remark commands, which are performed in the access-list 
(acl_name) context: configure>access-control>access-list (acl_name)#.  
 
6. Management and Security 
Task 
Command 
Comments 
Creating and 
deleting an ACL 
access-list [{ipv4 | ipv6}] <acl_name> 
no access-list <acl_name> 
You create an ACL by assigning a name and 
specifying the ACL IP type. The ACL names 
must be unique. 
The ACL name contains up to 
80 alphanumeric characters.  
access-list level commands (delete, deny, permit, remark) 
Removing rules 
from an ACL 
delete <sequence-number> 
Possible values for sequence-number:   
1–2147483648. 
Adding permit 
rules to an ACL 
permit {tcp|udp} {any|<src-address>[/<src-
prefix-length>]} [<src-port-range>] 
{any|<dst-address>[/<dst-prefix-length>]} 
[<dst-port-range>] [dscp <dscp-value>] 
[limit-rate <max-pps>] [rate-burst <max-
burst-packets>] [limit-size <max-kbytes-
sec>] [size-burst <max-burst-kbytes>] [limit-
connections <max-connections>]   [log] 
[inactive] [sequence <sequence-number>] 
permit icmp {any|<src-address>[/<src-
prefix-length>]} 
{any|<dst­address>[/<dst­prefix-length>]} 
[icmp-type <icmp-type-number> [icmp­code 
<icmp-code-number>]] [dscp <dscp-value>] 
[limit-rate <max-pps>] [rate-burst <max-
burst-packets>] [limit-size <max-kbytes-
sec>] [size-burst <max-burst-kbytes>] [limit-
connections <max-connections>]   [log] 
[inactive] [sequence <sequence-number>] 
permit ip [protocol <ip-protocol-number>] 
{any|<src­address> [/<src­prefix­length>]} 
{any|<dst­address>[/<dst­prefix­length>]} 
[dscp <dscp­value>] [limit-rate <max-pps>] 
[rate-burst <max-burst-packets>] [limit-size 
<max-kbytes-sec>] [size-burst <max-burst-
kbytes>] [limit-connections <max-
connections>]  [ [log] [inactive] [sequence 
<sequence­number>] 
Possible values for sequence:   
1–2147483648. 
log enables logging match events of the 
rule into the event log and sending SNMP 
traps. 
inactive enables changing ACL statement 
administrative state  
Note: If the ACL already has a statement 
with the same sequence number, the old 
statement is replaced with the new one. 
 
6. Management and Security 
Task 
Command 
Comments 
 
deny {tcp|udp} {any|<src-address>[/<src-
prefix-length>]} [<src-port-range>] 
{any|<dst-address>[/<dst-prefix-length>]} 
[<dst-port-range>] [dscp <dscp-value>]  [log] 
[inactive] [sequence <sequence-number>] 
deny icmp {any|<src-address>[/<src-prefix-
length>]} {any|<dst­address>[/<dst­prefix-
length>]} [icmp-type <icmp-type-number> 
[icmp­code <icmp-code-number>]] [dscp 
<dscp-value>]   [log] [inactive] [sequence 
<sequence-number>] 
deny ip [protocol <ip-protocol-number>] 
{any|<src-address>[/<src-prefix-length>]} 
{any|<dst­address>[/<dst­prefix-length>]} 
[dscp <dscp-value>]   [log] [inactive] 
[sequence <sequence­number>] 
Possible values for sequence:   
1–2147483648 
log enables logging match events of the 
rule into the event log and sending SNMP 
traps. 
inactive enables changing ACL statement 
administrative state  
Note: If the ACL already has a statement 
with the same sequence number, the old 
statement is replaced with the new one. 
 
Adding remarks 
to an ACL 
remark <description> [inactive] [sequence 
<sequence-number>] 
inactive enables changing ACL statement 
administrative state  
The description contains up to 255 
characters. 
Resequencing the 
rules in an ACL 
resequence access-list <acl-name> 
[<number>] 
number – difference between consecutive 
ACL rule numbers 
Possible values for number:  
1–100000 
Setting the 
logging interval 
of all ACLs 
logging access-list <interval> 
no logging access-list 
Enable logging at the maximum rate of the 
value set at Access Control level. <0> is 
equivalent to no logging access-list 
command. 
no logging access-list disables event 
logging for all rules in the ACL. 
Management-Level Tasks 
The following commands are available in the CLI management context: 
configure>management>access#. 
6. Management and Security 
Task 
Command 
Comments 
Binding the ACL to a 
management entity 
and defining the ACL 
direction 
access-group <acl-name>  
no access-group {in} {ipv4 | ipv6} 
When binding the ACL to the management entity, 
or when adding/editing rules in an ACL that is 
bound to the management entity, the rules must 
conform to the following limitations: 
• The protocol rules must be of TCP/UDP type. 
• The destination address must be set to any. 
• The source port must be set to any. 
• The destination port must be tcp/830 
(NETCONF), tcp/22 (SSH), udp/161 (SNMP), or 
any 
• DSCP, IP precedence, and P-bit cannot be used. 
Clearing ACL 
statistics 
clear-statistics {ipv4|ipv6} 
 
Displaying ACL 
statistics 
show statistics {ipv4|ipv6}  
See Management Statistics below. 
Displaying the 
summary of ACLs 
bound to a 
management entity 
show access-list summary 
Displays ACL status at the current level 
Examples 
 To create a management ACL: 
The example below illustrates a typical ACL applied to the incoming management traffic: 
• 
Allows SSH (TCP port 22) traffic from any source 
• 
Denies incoming SNMP (UDP PORT 161) connections from any source, except for 192.168.1.0 
subnet 
access-control>access-list(mng)# 
remark Allow incoming SSH traffic 
permit tcp any any 22 
remark Allow SNMP traffic coming from 192.168.1.0 subnet 
permit udp 192.168.1.0/24 any 161 
remark Deny incoming SNMP traffic 
deny udp any any 161 
6. Management and Security 
The table below summarizes the rules configured for the ACL. Items in red are either implied or 
unavailable for the current parameter or serve as system settings that cannot be changed. The deny rule 
appearing in the bottom row is a system rule that is used to deny all non-compliant data. 
Sequence 
Number 
Action 
Protocol 
Source IP 
TCP/UDP  
Source Port 
Dest. IP 
TCP/UDP Dest. Port 
Log 
10 
Permit 
TCP 
Any 
Any 
Any 
22 
No 
20 
Permit 
UDP 
192.168.1.0/24 
Any 
Any 
161 
No 
30 
Deny 
UDP 
Any 
Any 
Any 
161 
Yes 
 
Configuring ACL via Web GUI 
1. Navigate to Configure>Access Control. 
 
2. In the Access List box, choose the ACL type (IPv4/IPv6) and type its name. 
3. Click Submit. 
6. Management and Security 
 
4. Enter the ACL you have created and click on 
to add the rules to it: 
 
permit/deny/remark sequence number 
 
5. Click Submit. 
6. Management and Security 
 
6. Click on any item in the Rule box to edit the ACL source, destination and other parameters (which 
depend whether you selected ip, icmp etc). 
 
7. Click Submit. 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Maximum number of rules 
(total, in all ACLs) has been 
reached 
You tried to add more rules than the 
device can support 
Delete unnecessary rules and add a 
new rule once again.  
Only TCP, UDP or IP rules can 
be in traffic 
The ACL is bound to an entity and ICMP 
protocol is used. 
Choose TCP, UDP or IP protocols. 
6. Management and Security 
Message 
Cause 
Corrective Action 
Only TCP or UDP rules can be 
in management ACL 
The ACL is bound to management and a 
protocol other than TCP or UDP is used. 
Choose TCP or UDP protocol. 
Sequence number is out of 
range 
The specified or calculated sequence 
number is out of the allowed range 
Change the number. 
No such access-list 
A non-existing ACL cannot be bound to 
the entity. 
Check if the ACL name is correct. 
Inconsistent address and 
prefix length 
The specified address is not a subnet 
address for the specified prefix length. 
 
Cannot resequence; sequence 
number out of range 
Resequencing results in a statement 
sequence number out of the allowed 
range 
 
Only interzone or 
management ACL may have 
limit-connections keyword 
Only interzone or management ACL 
support limit-connections keyword  
Remove the limit-connections 
keyword from the ACL before 
binding to non-management or 
interzone entity 
limit-connections applies only 
to interzone or management 
ACL 
Only interzone or management ACL 
support limit-connections keyword 
 
Viewing ACL Status 
The ACL status displays information on the ACL name, type (IPv4 or IPv6), direction, and the entity that 
the ACL is bound to at the respective level. 
 To display the ACL status (management): 
• 
At the config>mngmnt>access# prompt, enter show access-list summary. 
The following status information is displayed: 
ACL Name     Type    Bound to    Direction 
--------------------------------------------------------------- 
4v           IPv4    mng         In 

## 6.2 Authentication via RADIUS Server  *(p.285)*

6. Management and Security 
Viewing ACL Statistics 
The ACL statistic counters gather information, per router, router interface or for management, on the 
number of rule matches registered on the ACL since the last reboot or counter clearing. 
 
Note 
All ACLs have an implied last rule that denies all packets. The device does not 
provide statistic counters for this rule. If you intend to collect statistics on the 
number of packets discarded by the default ACL mechanism, you must add the 
deny ip any any rule at the end of the ACL.  
Management Statistics 
 To display the ACL statistics (management): 
1. At the config>mngmnt>access# prompt, enter show statistics ipv4 access-list (for IPv4) or show 
statistics ipv6 access-list (for IPv6). 
The following statistic information is displayed: 
IPv4 access list: 4v                (in) 
Bound to: Management 
Matches counted for: 0 days 0 hours 2 minutes 33 seconds 
--------------------------------------------------------------- 
10    permit  tcp 172.17.154.154/24  any  22  (0 matches) 
20    permit  tcp 172.17.154.154/24  any  830 (0 matches) 
30    permit  udp 172.17.154.154/24  any  161 (0 matches) 
 To delete ACL statistics (management): 
• 
At the config>mngmnt>access# prompt, enter clear-statistics. 
The statistics counters are cleared. 
6.2 Authentication via RADIUS Server  
RADIUS (Remote Authentication Dial-In User Service) is an AAA (authentication, authorization, and 
accounting) client/server protocol that secures networks against unauthorized access. RADIUS is used to 
authenticate users and authorize their access to the requested system or service. The RADIUS client 
communicates with the RADIUS server using a defined authentication sequence.  
 
6. Management and Security 
Note 
ETX-1p supports RADIUS functionality; it cannot function as a RADIUS server.  
Applicability and Scaling 
This feature is applicable to all the device versions. 
ETX-1p doesn’t support RADIUS accounting. 
Standards Compliance 
RFC 2865, Remote Authentication Dial In User Service (RADIUS)  
RFC 2618, RADIUS Authentication Client MIB 
Benefits 
The RADIUS protocol allows centralized authentication and access control, avoiding the need to 
maintain a local user database on each device in the network. 
Due to its generic nature, service providers and enterprises use the RADIUS protocol to easily manage 
access to the Internet, internal networks, wireless networks, and integrated email services. These 
networks may incorporate DSL, access points, VPNs, network ports, and more. 
Functional Description 
RADIUS servers have built-in mapping of users to service-types. Note that each user has the rights of all 
users above it. All users have default password 1234. It is highly recommended to change the default 
password when setting up your device. (Refer to Working with SSH on how to change a password.)  
RADIUS Service-Types 
Name 
Prompt 
RADIUS Service-Type (User Access Level) 
user 
device-name% 
1 (login) 
tech 
device-name% 
7 (NAS prompt) 
oper 
device-name# 
8 (authenticate only) 
6. Management and Security 
Name 
Prompt 
RADIUS Service-Type (User Access Level) 
su 
device-name# 
6 (administrative) 
When a user attempts to log in to ETX-1p, the following occurs: 
1. User is prompted to enter their username and password. 
2. RADIUS client submits an authentication request to the RADIUS server. The username and 
encrypted password is transmitted over the network. (A hash code is generated over the entered 
password and a previously defined shared secret (string of free text) is transmitted between the 
RADIUS server and ETX-1p.) 
3. The RADIUS server verifies the user information against a database stored at the RADIUS server, 
and sends one of the following responses:  
 
Access Rejected – User is not authenticated and access to all resources is denied. User is 
prompted to reenter their username and password. 
 
Access Accepted – User is authenticated. Access to the requested network resources is 
granted. The RADIUS service-type is sent, indicating what services the user can access. 
Error! Objects cannot be created from editing field codes. 
Factory Defaults 
By default, no RADIUS servers are defined. When the RADIUS server is first defined, it is configured as 
shown below. 
Parameter 
Description 
Default Value 
address 
IP address of server 
0.0.0.0 
key 
Key 
“ “ hash 
retry 
Max number of authentication attempts 
3 
timeout 
Time interval between two authentication attempts 
3 seconds 
auth-port 
UDP port used for authentication  
1812 
Configuring RADIUS Server Parameters 
ETX-1p provides connectivity to up to four RADIUS authentication servers. You have to specify access 
parameters such as Radius server ID, associated server IP addresses, the number of allowed 
authentication request attempts, etc. 
6. Management and Security 
 To define RADIUS server parameters: 
1. At the config>mngmnt>radius# prompt, type server <server-id> to specify which server to 
configure. server-id can be 1-4. 
The config>mngmnt>radius>server(<server-id>)# prompt is displayed. 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning an IP address to the RADIUS 
server 
address <ip-address> 
A valid unicast IP address 
Defining the UDP port to be used for 
authentication key 
auth-port <udp-port-number> 
Possible values: 1–65535 
Defining a non-disclosed string 
(shared secret) used to encrypt the 
user password.  
key <string>  
The shared secret is a secret 
key consisting of free text 
(1-79 characters) known to 
the client and the server for 
encryption.  
 
Defining the number of 
authentication request attempts 
retry <number-of-retries> 
Possible values: 0–10 
Defining timeout (in seconds) for 
response from RADIUS server 
timeout <seconds> 
Possible values: 1–5 
Viewing RADIUS Statistics 
 To display RADIUS statistics: 
• 
At the config>mngmnt>radius# prompt, enter: 
show statistics. 
RADIUS statistics appear as shown below. 
config>mngmnt>radius# show statistics  
 
 
 
Server1   Server2   Server3  Server4 
-------------------------------------------------------------------------- 
Access Requests 
: 
0 
0 
0 
0 
Access Retransmits : 
0 
0 
0 
0 
Access Accepts 
: 
0 
0 
0 
0 
Access Rejects 
: 
0 
0 
0 
0 
Access Challenges 
: 
0 
0 
0 
0 
Malformed Response : 
0 
0 
0 
0 
Bad Authenticators : 
0 
0 
0 
0 
6. Management and Security 
Pending Requests 
: 
0 
0 
0 
0 
Timeouts 
 
: 
0 
0 
0 
0 
Unknown Types  
: 
0 
0 
0 
0 
Packets Dropped 
: 
0 
0 
0 
0 
Counter Discontinuity: 
0 
0 
0 
0 
 
Counter 
Description 
Access Requests 
Number of Access-Requests packets sent to RADIUS server 
Access Retransmits 
The number of RADIUS Access-Request packets retransmitted to RADIUS 
server 
Access Accepts 
Number of Access-Accept packets sent to RADIUS server 
Access Rejects 
Number of Access-Reject packets received from the RADIUS server 
Access Challenges 
Number of Access-Challenge packets sent to RADIUS server 
Malformed Response 
Number of malformed Access-Requests packets received 
Bad Authenticators 
Number of Access-Requests packets with invalid Signature attributes 
received 
Pending Requests 
The number of RADIUS Access-Request packets destined for this server 
that have not yet timed out or received a response.  This counter is 
incremented when an Access-Request is sent and decremented due to 
receipt of an Access-Accept, Access-Reject or Access-Challenge, a timeout 
or retransmission. 
Timeouts 
Number of times a server did not respond, and the RADIUS server re-sent 
the packet 
Unknown Types 
Number of RADIUS packets of unknown type which were received 
Packets Dropped 
Number of incoming packets silently discarded for some reason other 
than malformed, bad authenticators or unknown types 
Counter Discontinuity 
Number of centiseconds since the last discontinuity in the RADIUS Client 
counters.  A discontinuity may be the result of a reinitialization of the 
RADIUS Client module within the managed entity. 
 To clear RADIUS statistics: 
• 
At the config>mngmnt>radius# prompt, enter: 
clear statistics 
The RADIUS statistics are cleared. 

## 6.3 Authentication via TACACS+ Server  *(p.290)*

6. Management and Security 
6.3 Authentication via TACACS+ Server  
TACACS+ (Terminal Access Controller Access Control System Plus) is a security application that provides 
access control for routers, network access servers, and other networked computing devices via one or 
more centralized servers. TACACS+ provides separate authentication, authorization, and accounting 
services. It is used to communicate between the switch and an authentication database. As TACACS+ is 
based on TCP, implementations are typically resilient against packet loss. 
Applicability and Scaling 
This feature is applicable to all the device versions. 
Standards Compliance 
TACACS+ Protocol Version 1.78 (IETF draft-grant-tacacs-02) 
Benefits 
The TACACS+ protocol allows centralized authentication and access control, avoiding the need to 
maintain a local user data base on each device on the network. The TACACS+ server encrypts the entire 
body of the packet, but leaves a standard TACACS+ header. 
Customers do not have to adapt their TACACS+ server privilege levels to RAD CLI default values; CLI 
levels can be remapped in accordance with the customer’s TACACS+ levels.  
Functional Description 
TACACS+ is a protocol that provides access control for routers, network access servers, and other 
networked computing devices via one or more centralized servers. TACACS+ is based on the AAA model: 
• 
Authentication – The action of determining identity of a user 
• 
Authorization – The action of determining what a user is allowed to do. It can be used to 
customize the service for the particular user.  
• 
Accounting – The action of recording what a user is doing, and/or has done 
 
6. Management and Security 
Note 
TACACS+ performs authorization according to the user level; it does not send 
each command to the server for authorization.  
The TACACS+ client can be configured to use authentication/authorization with or without accounting 
functionality. 
When configuring users on external TACACS+ servers, see User Access to define authorization levels for 
ETX-1p users. Note that each user has the rights of all users below it, in addition to those explained in its 
description. 
 
Level 
User 
Allowed Actions 
Description 
3 
user 
Monitoring 
Commands that do not affect services, traffic, or 
configuration 
6 
tech 
Diagnostics 
Commands that may affect services and traffic, but are 
not saved in the database 
9 
oper 
Configuration 
Commands that change configuration parameters 
permanently 
12 
su 
User management 
Commands that manage users in the database 
Components 
The TACACS+ remote access environment has three major components: access client, TACACS+ client, 
and TACACS+ server.  
• 
The access client is an entity which seeks the services offered by the network.  
• 
TACACS+ client, running on ETX-1p, processes the requests from the access client and passes 
this data to TACACS+ server for authentication.  
• 
TACACS+ server authenticates the request, and authorizes services over the connection. The 
TACACS+ server does this by matching data from the TACACS+ client`s request with entries in a 
trusted database. 
TACACS+ server decides whether to accept or reject the user's authentication or authorization. Based on 
this response from the TACACS+ server, the TACACS+ client decides whether to establish the user's 
connection or terminate the user's connection attempt. The TACACS+ client also sends accounting data 
to the TACACS+ server to record in a trusted database. 
TACACS+ uses TCP for its transport and encrypts the body of each packet. TACACS+ client and server can 
agree to use any port for authentication and accounting. TACACS+ supports authentication by using a 
user name and a fixed password. 
6. Management and Security 
Accounting 
ETX-1p supports up to five accounting groups, with up to five TACACS+ servers per group. However, 
each TACACS+ server can be bound to a single accounting group only. 
A group can be defined with its own accounting level: 
• 
Shell accounting, which logs the following events: 
 
Successful logon 
 
Logon failure 
 
Logout 
 
ETX-1p - terminated management session 
• 
System accounting, which logs alarms and events 
• 
Command accounting, which logs CLI commands and level changes executed by the user or the 
ETX-1p scheduler 
Mapping Privilege Levels 
ETX-1p supports software configuration of mapping CLI levels to TACACS+ privilege levels.   
• 
There are 16 TACACS+ privilege levels. 
• 
You can map a CLI level to multiple TACACS+ levels. 
• 
You cannot map a TACACS+ level to multiple CLI levels. If the command is repeated for a 
TACACS+ level, the new mapping replaces the old one. 
• 
You can unmap both TACACS+ and CLI levels, with the exception of su, which must be mapped 
to at least one TACACS+ level. 
Factory Defaults 
By default, no TACACS+ servers are defined. When the TACACS+ server is first defined, it is configured as 
shown below. 
 
Parameter 
Default Value 
key 
Empty string 
retry 
1 
6. Management and Security 
Parameter 
Default Value 
timeout 
5 seconds 
authentication-port 
49 
accounting-port 
49 
Administrative status 
shutdown 
Accounting group membership 
None 
Configuring TACACS+ Entities 
TACACS+ Server 
ETX-1p provides connectivity to up to five TACACS+ authentication servers. You must specify the 
associated server IP address, key, number of retries, etc. 
 
Note 
If you intend to use TACACS+ for authentication, verify that TACACS+ is 
selected as a level-1 authentication method.  
 To configure a TACACS+ server: 
1. At the config>mngmnt>tacacsplus# prompt, type server <ip-address> to specify the server IP 
address. 
The config>mngmnt>tacacsplus>server (<ip-address>)# prompt is displayed. 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining the TCP port to be 
used for accounting  
accounting-port 
<port-number> 
Possible values: 1–65535 
Defining the TCP port to be 
used for authentication  
authentication-port 
<port-number> 
Possible values: 1–65535 
Binding accounting group to 
TACACS+ server 
group <string> 
no group detaches accounting group from 
server. 
6. Management and Security 
Task 
Command 
Comments 
Defining a non-disclosed 
string (shared secret) used to 
encrypt the user password 
key <string> [hash] 
The shared secret is a secret key consisting of 
free text known to the client and the server 
for encryption.  
The hash keyword denotes that the string is 
hashed, rather than clear text; usually it is 
added by the device after hashing the clear 
text that the user enters, before saving it in 
the database. 
If you enter the password as a text string, do 
not use the hash parameter. Use it only if you 
are specifying the password as a hashed 
value (obtained by using the info command 
to display TACACS+ data). 
Defining the number of 
authentication request 
attempts 
retry 
<number-of-retries> 
Permanently set to 1 
Defining timeout (in 
seconds) for response from 
TACACS+ server 
timeout <seconds> 
Possible values: 1–30 
Administratively enabling 
server 
no shutdown 
shutdown administratively disables the 
server 
Displaying statistics 
show statistics 
 
Clearing statistics 
clear-statistics 
 
Accounting Groups 
 To configure accounting groups: 
1. At the config>mngmnt>tacacsplus# prompt, type group <group-name> to configure an 
accounting group with the specified name.  
The config>mngmnt>tacacsplus>group (<group-name>)# prompt is displayed.  
2. To define the accounting for the group, enter:  
accounting [shell] [system] [commands] 
 
6. Management and Security 
Note 
• 
You can enter any combination of the parameters shell, system, or 
commands, but you must enter at least one of them. 
• 
Type no accounting to disable TACACS+ accounting for the group.  
 
3. Type exit to return to the TACACS+ level. 
The config>mngmnt>tacacsplus# prompt is displayed. 
4. Type server <ip-address> to select the TACACS+ server to which to bind the group. 
The config>mngmnt>tacacsplus>server (<ip-address>)# prompt is displayed.  
5. At the config>mngmnt>tacacsplus>server (<ip-address>)# prompt, enter group < group-name> 
to bind the previously defined accounting group to the TACACS+ server. 
Mapping CLI Levels to TACACS+ Privilege Levels 
 To map a CLI level to a TACACS+ privilege level: 
1. At the config>mngmnt>tacacsplus# prompt, type   
privilege-level <tacacs-privilege-level> { su | oper | tech | user}.  
The tacacs-privilege-level value can be 0-15.  
 
Note 
Type no privilege-level <tacacs-privilege-level> to remove TACACS+ privilege 
level mapping.  
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
6. Management and Security 
 To display the configuration from the above example: 
# configure management tacacsplus server 175.18.172.150 
config>mngmnt>tacacsplus>server(175.18.172.150)# information detail 
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
Bound to server defined in the example above.  
exit all 
configure management tacacsplus 
  group TAC1 
    accounting shell system commands 
    exit 
  server 175.18.172.150 
    group TAC1 
exit all 
configure management tacacsplus server 175.18.172.150 
config>mngmnt>tacacsplus>server(175.18.172.150)# info detail 
    key "244055BF667B8F89829AB8AB0FE50885" hash 
    retry 1 
    timeout 5 
    authentication-port 49 
    accounting-port 49 
    group "TAC1" 
    no shutdown 
Mapping CLI Level to Privilege Level 
 To map TACACS+ level 7 to the CLI user level:  
configure management tacacsplus privilege-level 7 user 
 To delete the mapping of TACACS+ level 7 to the CLI user level:  
configure management tacacsplus no privilege-level 7  
6. Management and Security 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
 
Message 
Cause 
Corrective Action 
su level must be mapped to a 
TACACS+ level 
You tried removing the last mapping of su, but su 
must be mapped to at least one TACACS+ level. 
Leave at least one 
mapping of su. 
Creating Linux user <name> is 
not allowed 
(<name> is replaced by the 
username the user was trying 
to give) 
 
A linux user (linux-user, linux-net-admin or linux-
tech) cannot have any of the following reserved 
names: rad, syncope, syslog, dnfv, auth, control, 
schannel, root, docker.  
A linux user name cannot start with __ 
characters.  
 
Viewing TACACS+ Statistics 
 To display TACACS+ statistics: 
• 
At the config>mngmnt>tacacsplus>server (<ip-address>)# prompt, type: 
show statistics. 
The TACACS+ statistic counters are displayed.  
config>mngmnt>tacacsplus>server(175.18.172.150)$ show statistics 
Requests               0 
Request Timeouts       0 
Unexpected Responses   0 
Server Error Responses 0 
Incorrect Responses    0 
Transaction Successes  0 
Transaction Failures   0 
Pending Requests       0 
 
Counter 
Description 
Requests 
Number of authentications performed toward a specific TACACS+ 
server 
Request Timeouts 
Number of transaction timeouts that occurred between the client 
and server 

## 6.4 IEEE 802.1X - Port-based Network Access Control  *(p.298)*

6. Management and Security 
Counter 
Description 
Unexpected Responses 
Number of times the TACACS+ client receives a TACACS+ packet that 
is not expected at that time. Usually, this occurs due to a delayed 
response to a request that has already timed out 
Server Error Responses 
Number of errors received from the TACACS+ server 
Incorrect Responses 
Number of times the TACACS+ client: 
• Fails to decrypt the packet  
• Detects an invalid field in the TACACS+ packet  
• Receives a response that is not valid according to the initial 
request 
Transaction Successes 
Number of successful transactions between the client and TACACS+ 
server 
Transaction Failures 
Number of times the TACACS+ client’s request is aborted by the 
TACACS+ server or the server fails to respond after maximum retry is 
exceeded 
Pending Requests 
Number of TACACS+ client’s requests minus number of TACACS+ 
server responses or timeouts 
 To clear TACACS+ statistics: 
• 
At the config>mngmnt>tacacsplus>server (<ip-address>)# prompt, type:  
clear-statistics. 
TACACS+ statistic counters are set to 0. 
 
6.4 IEEE 802.1X - Port-based Network Access Control  
IEEE 802.1X is an IEEE Standard for Port-based Network Access Control (PNAC). It provides 
an authentication mechanism to devices wishing to attach to a LAN or WLAN.   
The host that is seeking access to the network is known as the Supplicant, and the system providing the 
point of access to the network is the Authenticator. 
Authenticator role can be configured for physical and virtual (switch) Ethernet ports and WiFi access 
points. The supplicant role is supported by Ethernet ports only. 
If Ethernet switch ports are configured in the device, the behavior depends on the bridge configuration: 
6. Management and Security 
• 
If a bridge is configured, 802.1X configuration on its Ethernet port members is ignored; the one 
on the switch port is effective. 
• 
If a bridge is not configured, 802.1X configuration on the Ethernet ports is effective; the one on 
the (inactive) switch port is ignored. 
Authenticator and supplicant cannot be enabled on the same port at the same time. 
Standards Compliance 
IEEE Std 802.1X-2010 – Port-Based Network Access Control 
RFC 3580 – IEEE 802.1X RADIUS, Usage Guidelines 
RFC 7268 – RADIUS Attributes for IEEE 802 Networks 
Benefits 
802.1X protocol provides secured access to the customer network. 
Factory Defaults 
The parameter defaults are listed in the table below. 
Parameter  
Description 
Default Value 
authenticator 
reauthentication period Configuring reauthentication period (sec) 
3600 
Enabling/disabling 
authenticator 
functionality  
no [shutdown] 
shutdown 
  
Configuring 
authentication mode 
authentication mode  
multi-supplicants 
 
supplicant 
held-period  
Configuring held period after authentication failure (sec) 
60 
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
Functional Description 
Components 
802.1X authentication involves three parties: a supplicant, an authenticator, and an authentication 
server.  
• 
The supplicant is a client device that wishes to attach to the LAN.  
• 
The authenticator is a network access device, such as an Ethernet switch or wireless access 
point, granting or denying supplicants access to the network, following an authentication 
process 
• 
The authentication server is typically a host running software supporting 
the RADIUS and EAP protocols. The server asks whether or not a supplicant is authorized to use 
the network.  
RAD’s 802.1X package supports the authenticator and supplicant roles. For authentication server RAD 
relies on a standard RADIUS server.  
The authenticator acts like a security guard to a protected network. The supplicant (i.e. the client device) 
is not allowed access through the authenticator to the protected side of the network until the 
supplicant’s identity has been validated and authorized.  
With 802.1X port-based authentication, the supplicant provides credentials, such as user 
name/password, to the authenticator, and the authenticator forwards the credentials to the 
authentication server for verification. If the authentication server determines the credentials are valid, 
the supplicant (client device) is allowed to access resources located on the protected side of the 
network. 
The authenticator (if enabled) initiates a reauthentication process of all the connected supplicants, by 
sending a multicast EAP-Request. The supplicant (if enabled) initiates reauthentication with its 
authenticator. 
The authentication process involves frame exchange between the supplicant and the authenticator, and 
between the authenticator and the RADIUS server. 
6. Management and Security 
The authentication process can be initiated by either the supplicant or the authenticator. The 
authenticator does not authenticate or authorize supplicants; it forwards messages between the 
supplicant and the authentication server and opens or closes the port according to the authentication 
process results. 
If during the authentication process the authenticator does not receive a response to an EAP frame from 
the supplicant, it tries twice after waiting 30 seconds. If the maximum number of retransmissions is 
exhausted without a response, the authentication attempt is considered to fail. The authentication 
process then restarts, twice if needed. After three failures the authenticator sets the port state as 
unauthorized, enters a held state, and waits a quiet period of 60 seconds, after which it restarts the 
whole process. 
Authenticator 
The following authentication modes are used in the device: 
• 
Multi supplicants – Each supplicant is authenticated independently and can only forward traffic 
after being authenticated 
• 
Port – The first authenticated supplicant opens the port, after which traffic is allowed from any 
source. 
• 
Single supplicant – The first authenticated supplicant is allowed to forward traffic while others 
are rejected. They cannot be authenticated even if they have good credentials. 
 
Note 
In WiFi APs the command is masked and the mode is multi-supplicants. The 
number of supplicants can be set to 1-22 with the max-clients command in the 
configure>port>wlan>access-point level (1 is equivalent to the single 
supplicant mode). Static MAC addresses bypass 802.1X authentication, so that 
the device uncapable of doing 802.1X (e.g. dumb printer) can be manually 
configured. 
 
Periodic reauthentication of connected supplicants can be performed by the authenticator, to check 
that the user has not logged off the authenticated host. 
 
The authenticator uses the RADIUS servers configured in the CLI management>radius level (see 
Authentication via RADIUS Server). The supported RADIUS frames and attributes are assumed to 
conform to [RFC 3580] and [RFC 7268]. 
6. Management and Security 
If no RADIUS server is configured, the authenticator cannot be initialized and supplicant requests will be 
silently discarded. If a server is later configured the authenticator will start the authentication process. 
After a successful authentication the port, or supplicant, enters the authorized state, in which it can 
send any kind of traffic. This traffic is subjected to bridge configuration and to VLAN assignment 
accepted from the RADIUS server, when applicable. 
Supplicant 
Two authentication methods are available:  
• 
PEAP MSCHAPv2 – The supplicant is authenticated by challenge-response. The user has to 
provide a RADIUS password (the configured identity doubles duty as RADIUS username). 
• 
EAP TLS – The supplicant is authenticated with a self-certificate, which must be specified by the 
user. 
In both methods the authenticator is authenticated by a certificate. The device must have the 
authenticator’s CA certificate; otherwise authentication would fail. The device automatically locates the 
correct CA certificate (assuming it has it), the user does not specify it. 
 
Supplicant configuration is available on the Ethernet port only and not available on WiFi access points. 
Configuring 802.1X Access Control 
 To configure 802.1X: 
1. Type the following: 
 
 For the Ethernet port: At the config>port>ethernet <port name># prompt, type dot1x 
command. 
 
For the WLAN port: At the config>port>wlan <port-name> access-point <ap-number># 
prompt, type dot1x command. 
 
For the Wi-Fi client: At the config>port>wifi-client [1] # prompt, type dot1x command.  
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Initializing 802.1X 
initialize 
Displaying 802.1X status 
show status 
 
6. Management and Security 
Task 
Command 
Comments 
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
The following commands are available in the autenticator level, under the dot1x level. 
Task 
Command 
Comments 
Enabling periodic 
reauthentication 
reauthentication [period 
<seconds>] 
no reauthentication 
Reauthentication is disabled by default. 
When enabled, the user can configure 
the reauthenticated period to 1-65535 
seconds. If no period is specified, the 
default is 3600. 
Enabling/disabling authenticator 
functionality  
no [shutdown] 
 
Default: shutdown 
The authenticator and supplicant roles 
cannot be both enabled on the same 
port. 
If PSK is enabled for a WiFi access point, 
802.1X cannot be enabled for that AP.  
Configuring authentication mode 
authentication mode 
{multi-supplicants | port | 
single-supplicant} 
Default: multi-supplicants 
Note: This is the only possibility for WiFi 
APs. 
The following commands are available in the supplicant level, under the dot1x level. 
Task 
Command 
Comments 
Configuring held period after 
authentication failure (sec) 
held-period <0 – 65535> 
 
6. Management and Security 
Task 
Command 
Comments 
Configuring authentication 
parameters 
authentication identity 
<identity> method {peap-
mschapv2 radius password 
<password> [hash] | eap-tls 
certificate <certificate-name>} 
no authentication 
 
identity - Supplicant identity 
Possible Values: 1-244 characters 
password – RADIUS password 
Possible Values: 
• 1-244 characters for hashed 
password 
• 1-119 characters for cleartext 
password 
hash - password is hashed 
certificate-name - Name of device self 
certificate 
Possible Values: 1-64 characters 
Configuring the maximum 
number of authentication 
attempts 
max-authentication <1 – 65535>  
 
Configuring the time to wait 
before retransmitting EAP frame 
(sec) 
tx-period <1 – 65535> 
 
Disabling authenticator 
functionality 
no [shutdown] 
The authenticator and supplicant roles 
cannot be both enabled on the same 
port 
Examples 
The examples below illustrate the 802.1X protocol operation. 
To enable the authenticator, make sure that: 
• 
RADIUS is configured 
• 
Router interface of the same port is configured 
****RADIUS configuration**** 
# configure management radius 
config>mngmnt>radius# server 1 
config>mngmnt>radius>server(1)# key ALPHA 
config>mngmnt>radius>server(1)# address 172.17.232.207 
config>mngmnt>radius>server(1)# no shutdown 
 
****Configuring Router interface 3**** 
6. Management and Security 
# configure router 1 
config>router(1)# interface 3 
config>router(1)>interface(3)# address 20.20.20.1/24 
config>router(1)>interface(3)# bind ethernet lan4 
config>router(1)>interface(3)# no shutdown 
config>router(1)>interface(3)# 
 
****Enable authenticator on Ethernet port**** 
 
config port ethernet lan4 
dot1x 
authenticator 
no shutdown 
 
****Enable supplicant on Ethernet port (peap-mschapv2)**** 
 
config port ethernet wan2 
dot1x 
authentication identity "radius1" method peap-mschapv2 radius password 1234 
no shutdown 
 
****Enable supplicant on ethernet port (eap-tls)**** 
 
config port ethernet wan2 
dot1x 
authentication identity "radius1" method eap-tls certificate "client_certificate" 
no shutdown 
 
Displaying Statistics 
 To display 802.1X statistics:  
 
*****Authenticator enabled, Ethernet ports***** 
 
 
config>port>eth(lan4)>dot1x# show statistics 
Port EAPOL Frames 
----------------------------------------------------------------------------- 
Rx EAP Total          : 43 
Rx Start              : 3 
Rx Logoff             : 0 
Rx Invalid            : 0 
Rx Length Error       : 0 
Rx Last Frame Version : 1 
6. Management and Security 
Rx Last Frame MAC     : 00-55-88-DD-BB-AA 
Tx Start              : 0 
Tx Logoff             : 0 
Tx Authenticator      : 33 
Tx Supplicant         : 0 
 
 
EAPOL Frames For      : 00-55-88-DD-BB-AA 
Rx EAP Total          : 27 
Rx Start              : 2 
Rx Logoff             : 0 
Rx Invalid            : 0 
Rx Length Error       : 0 
Rx Last Frame Version : 1 
Tx Start              : 0 
Tx Logoff             : 0 
Tx Authenticator      : 22 
Tx Supplicant         : 0 
 
EAPOL Frames For      : 18-06-F5-EE-13-E4 
Rx EAP Total          : 16 
Rx Start              : 1 
Rx Logoff             : 0 
Rx Invalid            : 0 
Rx Length Error       : 0 
Rx Last Frame Version : 1 
Tx Start              : 0 
Tx Logoff             : 0 
Tx Authenticator      : 11 
Tx Supplicant         : 0 
 
*****Authenticator enabled, WiFi ports***** 
 
config>port>wlan(2.4g)>ap(1)>dot1x# show statistics  
Port EAPOL Frames 
----------------------------------------------------------------------------- 
Rx EAP Total          : 27 
Rx Start              : 0 
Rx Logoff             : 0 
Rx Invalid            : 0 
Rx Length Error       : 0 
Rx Last Frame Version : 1 
Rx Last Frame MAC     : 00-23-14-85-13-7C 
Tx Start              : 0 
Tx Logoff             : 0 
Tx Authenticator      : 30 
Tx Supplicant         : 0 
 
 
EAPOL Frames For      : 00-23-14-85-13-7C 
Rx EAP Total          : 27 
6. Management and Security 
Rx Start              : 0 
Rx Logoff             : 0 
Rx Invalid            : 0 
Rx Length Error       : 0 
Rx Last Frame Version : 1 
Tx Start              : 0 
Tx Logoff             : 0 
Tx Authenticator      : 30 
Tx Supplicant         : 0 
 
*****Supplicant enabled and authenticated, Ethernet ports***** 
config>port>eth(wan2)>dot1x# show statistics 
Port EAPOL Frames 
----------------------------------------------------------------------------- 
Rx EAP Total          : 105 
Rx Start              : 0 
Rx Logoff             : 0 
Rx Invalid            : 3 
Rx Length Error       : 0 
Rx Last Frame Version : 2 
Rx Last Frame MAC     : 00-55-66-77-01-82 
Tx Start              : 4 
Tx Logoff             : 0 
Tx Authenticator      : 0 
Tx Supplicant         : 55 
                            
802.1X Statistic Counters 
Counter 
Description 
Rx EAP Total 
Number of EAPOL-EAP frames received 
Rx Start  
Number of EAPOL-Start frames received 
Rx Logoff  
Number of EAPOL- Logoff frames received 
Rx Invalid  
Number of invalid EAPOL frames received 
Rx Length Error  
Number of EAPOL frames with wrong length received 
Last Rx Frame Version  
Version of last received EAPOL frame 
Last Rx Frame Source 
Source MAC address of last received EAPOL frame 
Tx Start  
Number of EAPOL-Start frames transmitted 
Tx Logoff  
Number of EAPOL-Logoff frames transmitted 
Tx Authenticator   
Number of EAPOL-EAP frames transmitted by the authenticator 
Tx Supplicant 
Number of EAPOL-EAP frames transmitted by the supplicant 
6. Management and Security 
 To clear 802.1X statistics: 
• 
At the config>port>ethernet <port-name> dot1x # or 
config>port>wlan(<number>)>ap(<number>)>dot1x# or config>port>wifi-client [1] >dot1x# 
prompt, type clear statistics.  
The device clears the statistics of the physical port, as well as all virtual ports bound to it. 
Viewing the 802.1X Status 
This section explains how to display the status of the 802.1X protocol operation. 
 To display 802.1X status:  
 
*****Authenticator enabled, Ethernet ports***** 
 
config>port>eth(lan4)>dot1x# show status 
Authenticator 
----------------------------------------------------------------------------- 
Administrative State : Enabled 
Authentication Mode  : Multi Supplicants 
 
Supplicants 
----------------------------------------------------------------------------- 
Connected   : 2 
Max Allowed : 10 
 
Supplicants 
----------------------------------------------------------------------------- 
MAC Address                   Status 
----------------------------------------------------------------------------- 
00-55-88-DD-BB-AA             Authenticated 
18-06-F5-EE-13-E4             Authenticated 
 
Supplicant 
----------------------------------------------------------------------------- 
Administrative State : Disabled 
Operational status   : Unauthenticated 
 
*****Authenticator enabled, WiFi ports***** 
 
config>port>wlan(2.4g)>ap(1)>dot1x# show status  
Authenticator 
----------------------------------------------------------------------------- 
Administrative State : Enabled 
Authentication Mode  : Multi Supplicants 
6. Management and Security 
 
Supplicants 
----------------------------------------------------------------------------- 
Connected   : 1 
Max Allowed : 21 
 
Supplicants 
----------------------------------------------------------------------------- 
MAC Address                   Status 
----------------------------------------------------------------------------- 
00-23-14-85-13-7C             Authenticated 
 
*****Supplicant enabled and authenticated, Ethernet ports***** 
 
config>port>eth(wan2)>dot1x# show status 
Authenticator 
----------------------------------------------------------------------------- 
Administrative State : Disabled 
Authentication Mode  : Multi Supplicants 
 
Supplicants 
----------------------------------------------------------------------------- 
Connected   : 0 
Max Allowed : 10 
 
Supplicant 
----------------------------------------------------------------------------- 
Administrative State : Enabled 
Operational status   : Authenticated 
 The status display provides information about: 
• 
Authenticator role admin status 
• 
Authenticator authentication mode 
 
Multi Supplicants 
 
Port 
 
Single Supplicant 
• 
Number of connected supplicants 
• 
Maximum number of supplicants allowed on this port 
• 
Connected supplicant MAC address 
• 
Connected supplicant status 
 
Pending 
 
Unauthenticated 

## 6.5 DHCP Server  *(p.310)*

6. Management and Security 
 
Authenticated 
• 
Supplicant role admin status (this section is irrelevant and not displayed for WiFi access points) 
 
Disabled 
 
Enabled 
• 
Supplicant role oper status 
 
Authenticated 
 
Unauthenticated 
• 
Reason of supplicant authorization failure 
 
(No Valid CA Certificate)  
 
(No Valid Self Certificate) 
Note 
The table of supplicants is empty if no RADIUS server is configured (since the 
authenticator cannot be initialized). 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
 
Message 
Cause 
Corrective Action 
Cannot enable authenticator while 
supplicant is enabled  
Cannot enable supplicant while 
authenticator is enabled 
The authenticator and supplicant 
roles cannot be both enabled on 
the same port or access point. 
 
PSK authentication is enabled on 
this access point 
If PSK is enabled for a WiFi access 
point, 802.1X cannot be enabled 
for this AP.  
 
No valid certificate with the 
specified name 
There is no valid certificate with 
the specified name 
Create a valid certificate with the 
specified name 
6.5 DHCP Server  
ETX-1p supports Dynamic Host Configuration Protocol (DHCP) server functionality for IPv4 clients. Based 
on the Bootstrap Protocol (BOOTP), DHCP server assigns to DHCP clients IPv4 addresses from configured 
6. Management and Security 
pools, as well as various configuration parameters (DHCP options), in response to the broadcast 
requests of DHCP clients. This functionality eliminates the need to manually assign an IP address for 
each potential client. 
It is possible to configure a single DHCP server instance. It can be bound to any VRF. 
 
Note 
• 
DHCP server, client applications are independent. You can configure 
neither or any combination of them. 
• 
DHCP server is not supported on tunnel interfaces.  
Applicability and Scaling 
This feature is applicable to all ETX-1p versions.  
Standards Compliance 
RFC 951 – Bootstrap Protocol 
RFC 1542 – Clarifications and Extensions for the Bootstrap Protocol (relay agent requirements) 
RFC 2131 – Dynamic Host Configuration Protocol 
RFC 2132 – DHCP Options and BOOTP Vendor Extensions (basic DHCP options) 
Benefits 
The main benefits of DHCP servers are: 
• 
Reduced costs of IP addresses – There is no need to buy and manage an IP address for each 
potential client. For example, there is no need to manually assign an address for each machine 
that is connected to the network, even briefly or rarely. 
• 
Reduced access costs – Dynamic addresses are cheaper than static addresses. 
• 
Reduced client configuration costs – DHCP ease of configuration leads to fast deployment and 
less operational overhead. There is no need to manually configure connectivity parameters on 
each client, except for very basic configuration (and sometimes not even this). The DHCP server 
can even start a zero touch configuration process, which completely configures the client 
without network manager intervention. 
6. Management and Security 
• 
Centralized management – Network managers only need to configure a single central server. If a 
global parameter, e.g. DNS server, is changed, there is no need to manually configure all the 
clients in the network. 
Functional Description 
The following describes the DHCP flow, from the time the client sends a broadcast DHCP request and 
until the IP addresses are distributed. 
1. The DHCP client sends to the DHCP server a broadcast DHCP request. 
2. Any listening DHCP server can assign an IP address to the DHCP client (based on information sent 
by the client), as well as other options. Before assigning an IP address, the server pings it. If a reply 
is received, this means the address is a conflict, meaning it is an address that is already occupied. 
The conflict enters the conflicts table.  
3. DHCP server sends back to the client a lease offer, containing an IP address and possibly other 
parameters. It sends its IP address in option 54 (server identifier) to the client. 
 
Note 
If the DHCP server offers a lease and the client then sends a DHCP request 
with an IP address of a different server (in option 54), the server assumes that 
the request is no longer relevant, and return the offered address to the pool of 
available addresses.  
4. The DHCP client accepts the offer. If the DHCP client received more than one lease offer, it 
chooses a lease; usually the first one it received. 
5. Before accepting a lease, a typical client sends a gratuitous ARP to the IP address it is about to use. 
If two replies are received, the client should decline the lease, and the server places the IP address 
into the conflicts table. 
6. The server acknowledges the lease.  
ETX-1p saves the lease in a database that includes all active and inactive leases. The lease database with 
address binding (IP address to client hardware address) resides in permanent memory that withstands 
reboot. If possible, ETX-1p assigns to clients the same IP addresses they previously had.  
The lease is usually granted for a limited time; therefore, the DHCP client should renew it before it 
expires. A DHCP client may also release a lease once is no longer needed. 
The server does not delete a binding from the database when a lease expires. However, if a new client 
asks for an address and the server does not have a free address, then one of the unused addresses from 
the database may be used.  
6. Management and Security 
The server also saves a table of conflicts. A conflict is an IP address that the server tried to assign but 
found out it is already occupied. The server does not assign an address from the conflicts table unless all 
non-conflicting addresses belong to active leases. 
If you change the configuration so that it renders active leases invalid (such as changing a pool’s range of 
addresses or network, excluding an address), the server removes the leases from the binding database. 
Addresses in the conflict database that are no longer valid are also removed. 
The device may function as DHCP client or server at the same time.  
DHCP Options 
The following Tx options (i.e. sent from server to client) are supported by RAD DHCP server and RAD 
clients: 
• 
Default routers (3) – one or two 
• 
Lease time (51) – offered lease time  
• 
Server identifier (54) – IP address of the server offering the lease; not configurable 
The following Tx options are supported by RAD DHCP server, but unsupported by RAD clients: 
• 
Domain name system (DNS) servers (6) – one or two 
• 
Domain name (15) 
• 
NetBIOS name server (44) 
• 
NetBIOS node type [b, p, m, or h] (46) 
The following Rx options (i.e. sent from client to server) are supported by RAD DHCP server and RAD 
clients: 
• 
Lease time (51) – requested lease time 
• 
Server identifier (54) – IP address of the server whose offer is accepted (also used by clients to 
send unicast messages to the server) 
• 
Client identifier (61) – client unique identifier (typically MAC address, but can be any other 
string) 
The following Rx options are supported by RAD clients, but ignored by RAD DHCP server: 
• 
Host name (12) – client host name 
• 
Vendor class identifier (60) – client vendor identifier  
 
6. Management and Security 
Note 
• 
Options 66 (TFTP server name), 67 (boot file name), and 150 (TFTP server 
address) are not supported by RAD DHCP server although RAD clients use 
them for the zero touch configuration process. 
• 
Unsupported received DHCP options are ignored. They do not invalidate a 
request.  
Manual Bindings 
In cases when it is important that a client, usually a router or server, not change its address, it is possible 
to configure manual bindings, i.e. IP addresses that are manually mapped to clients. This directs the 
server to grant fixed addresses to specific clients (usually recognized by their MAC address). 
DHCP Lease Offer Message 
When offering a lease, the server builds a DHCPOFFER message, locates the assigned IP address, and 
adds the following options: 
• 
DHCP message type (53) – 2, in case of a DHCP offer 
• 
Subnet mask (1) – The subnet mask of the client, taken from the host or network command of 
the pool configuration. 
• 
Lease time (51) – Time the lease is valid 
• 
Renewal (T1) time value (58) – time (in seconds) at which the client should transition to the 
renewing state.  
 
If the offered lease time is infinite, this option is not sent. Otherwise it is set to the default, 
which is 0.5 of the lease time. 
• 
Rebinding (T1) time value (59) – Time (in seconds) at which the client should transition to the 
rebinding state.  
 
If the offered lease time is infinite, this option is not sent. Otherwise, it is set to the default, 
which is 0.875 of the lease time. 
• 
Server identifier (54) – IP address of the server  
• 
Any of the following options, if configured: 
 
Default router (3) – one or two IP addresses 
 
DNS server (6) – one or two IP addresses 
 
Domain name (15) – a string 
 
TFTP server name (66) – a string 
 
NetBIOS name server (14) – one or two IP addresses. 
6. Management and Security 
 
NetBIOS node type (46) – b, p, m, or h 
• 
The end option (255) – Marks the end of valid information in the vendor field. 
Factory Defaults 
By default, no DHCP server or DHCP server pool is defined. When a DHCP server or DHCP server pool is 
first defined, it is configured as shown below. 
Parameter 
Default Value 
DHCP server 
 
number 
1 
clear 
-- 
bind 
router 1 
exclude-address 
-- 
shutdown 
no shutdown 
pool  
no pool 
tftp-server-name  
no tftp-server-name 
DHCP server pool 
 
address-range 
no address-range 
client-identifier 
no client-identifier 
default-router 
no default-router 
dns-server 
no dns-server 
domain-name 
no domain-name 
hardware-address 
no hardware-address 
host 
no host 
lease-default 
no lease-default 
netbios-name-server 
no netbios-name-server 
netbios-node type 
no netbios-node type 
network 
no network 
relay-information 
no relay-information  
6. Management and Security 
Configuring DHCP Server 
You can configure a single DHCP server as follows: 
1. Globally enable DHCP server functionality (the default). 
2. By default, no DHCP server exists. Create a single instance of DHCP server. 
3. Exclude addresses that should never be assigned to clients; typically addresses that are statically 
configured on servers or routers. 
4. Configure DHCP pools containing: 
 
Range of addresses (or a single address) to assign to clients 
 
Various DHCP options to send to clients 
 
Definitions of clients eligible to get lease from the pool 
5. Host and subnetwork inherit options from larger networks (simplifying the configuration): 
 
For example, a global pool (e.g. 192.168.0.0) can contain global options, such as domain 
name. 
 
Additional pools are set for subnets (e.g. 192.168.1.0 and 192.168.2.0), each with its own 
default gateway. 
 To configure the DHCP server: 
1. Navigate to configure system [no] dhcp-server [<number>}. 
The config>system>dhcp-server# prompt is displayed. 
 
Note 
• 
<number> is the number of the dhcp-server, which can only be 1.  
• 
Type no dhcp-server to remove the DHCP server from the router.  
 
2. At the config>system>dhcp-server# prompt, enter the necessary commands according to the 
tasks listed below. 
Task 
Command 
Comments 
Binding DHCP server to 
router 
bind router <number> 
number – router number 
Note: The DHCP server works only 
on the router to which it is bound. 
If the bound router does not exist, 
the DHCP server is idle. 
6. Management and Security 
Task 
Command 
Comments 
Clearing DHCP server 
bindings, conflicts, or 
statistics 
clear {binding {address <ipv4-
address> | all} | conflict 
{address <ipv4-address> | all}} 
 
• You can clear the entire DHCP 
server binding database, or 
binding of a specific address. 
• When clearing a specific 
address, if ipv4-address does 
not exist in the database, an 
error message is generated:  
No such address. 
• You can clear the entire 
conflicts database, or a 
specific conflicting address. 
• Clearing all conflicts clears 
both abandoned (declined by 
clients) and blocked (already 
in use) addresses. 
Configuring the IP address 
that is not to be offered to a 
client 
[no] exclude-address <ipv4-
address> 
A single address to be excluded 
can be configured per command.  
Repeating this command adds 
new excluded addresses; it does 
not replace previous excluded 
addresses. 
Note: Excluded addresses are 
typically addresses that are 
statically configured on servers or 
routers.show  
Configuring DHCP server pool 
[no] pool 
See Configuring DHCP Server 
Pool. 
Typing no pool removes the DHCP 
server pool and the configuration 
related to it (IP address ranges 
and DHCP options). 
Displaying DHCP server 
bindings 
show binding 
See Viewing DHCP Server Binding 
Displaying DHCP server 
conflicts 
show conflict 
See Viewing DHCP Server Conflict 
Displaying DHCP server 
statistics 
show statistics 
See Viewing DHCP Server 
Statistics 
6. Management and Security 
Task 
Command 
Comments 
Disabling/enabling DHCP 
server functionality 
[no] shutdown 
DHCP server functionality is 
enabled by default. 
Notes:  
• The DHCP client functions are 
not affected by this command. 
• When disabled, the rest of the 
server configuration is 
ignored. 
Configuring DHCP Server Pool 
By default, no DHCP server pool exists. The following procedure describes how to create a DHCP server 
pool. Each pool must be assigned a unique name.  
The DHCP server offers leases based on the pools’ configurations.   
 To configure the DHCP server pool: 
1. Navigate to configure system [no] dhcp-server pool [name]. 
The config>system>dhcp-server>pool# prompt is displayed. 
2. At the config>system>dhcp-server>pool# prompt, enter the necessary commands according to 
the tasks listed below. 
Note 
• 
Typing no pool removes the DHCP server pool, as well as the configuration 
related to it. 
• 
You must assign a unique pool name of 1 to 80 characters 
 
Task 
Command 
Comments 
Configuring range of IP 
addresses that server can 
assign to clients  
(relevant only for pool 
bound to network) 
[no] address-range 
<start-ip> <end-ip> 
start-ip – lowest IPv4 address of the range 
end-ip – highest IPv4 address of the range 
Notes: 
• An address range can be configured only if 
the pool is bound to a network. It is 
irrelevant if the pool is bound to a host. 
• The address range must be inside the 
pool’s subnet (configured with the 
network command). 
6. Management and Security 
Task 
Command 
Comments 
• If no range is configured, the default value 
is the entire subnet of the pool. 
• A single range can be configured per pool. 
• Typing no address-range <start-ip> <end-
ip> deletes an existing range. If the 
specified range is not exactly the one 
configured by the command, range is not 
deleted. 
Configuring client 
identifier (DHCP option 
61) 
client-identifier <unique-
identifier>  
no client-identifier 
Client identifier (option 61) is used for manual 
binding, i.e. assigning a preconfigured IP 
address to a specific client. 
unique-identifier – client identifier; 1-255 
character string 
Notes: 
• Client identifier can be configured only if 
the pool is bound to a host (using host 
command). 
• If the command is repeated, it replaces 
the previous one. 
• Either client identifier or hardware 
address can be configured; not both. 
• You cannot configure a client identifier 
already configured on another pool. 
• Typing no client-identifier removes the 
client identifier from the pool. 
• Client identifier can be a hexadecimal 
number or a string 
• String format is <string> 
• Hexadecimal number format is  1:<hex>  
Configuring default 
router (DHCP option 3) 
default-router <address> 
[<address-2>] 
no default-router 
address – default router IPv4 address 
address-2 – second default router IPv4 
address 
Notes:  
• Repeating this command replaces the 
previous one. 
• address-2 must be different than address-
1. 
6. Management and Security 
Task 
Command 
Comments 
Configuring Firewall 
server (DHCP option 6) 
dns-server <address> 
[<address-2>] 
no dns-server 
 
address – DNS server IPv4 address 
(mandatory) 
address-2 – second DNS server IPv4 address 
(optional) 
Notes:  
• Repeating this command replaces the 
previous one. 
• address-2 must be different than address-
1. 
Configuring domain 
name (DHCP option 15) 
domain-name <domain> 
no domain-name 
Domain – domain name; 1-255 character 
string 
Note: Repeating this command replaces the 
previous one. 
Configuring client 
hardware address (MAC 
address) 
hardware-address <mac-
address> 
no hardware-address 
MAC address is used for manual binding, i.e. 
assigning a preconfigured IP address to a 
specific client. 
mac-address – client MAC address 
Notes:  
• The hardware address can be configured 
only if the pool is bound to a host 
(configured with the host command). 
• Repeating this command replaces the 
previous one. 
• Either client identifier or hardware 
address can be configured; not both.  
• You cannot configure a hardware address 
already configured on another pool. 
Configuring client IP 
address and prefix length 
host <ipv4-address>/ 
<prefix-length> 
no host 
Ipv4-address – client IPv4 address 
Prefix-length – client IP prefix length 
                       Possible values: 1-32 
Notes:  
• If no host is invoked while client identifier 
or hardware address is configured, the 
device deletes the configured client 
identifier or hardware address. 
• Repeating this command replaces the 
previous one. 
6. Management and Security 
Task 
Command 
Comments 
• Either the host or network command can 
be configured; not both.  
• The address (while taking into account the 
prefix length) must be a unicast address. 
• The same pair of address and prefix length 
may not be configured on more than one 
pool. 
• The mask (reflecting the prefix length) is 
passed to the client in option 1. 
Learning pool 
configuration from DHCP 
client 
[no] learn-from-dhcp-
client router <router> 
interface <interface> 
router, interface – router interface from 
which to learn DHCP information 
Configuring lease default 
validity time (DHCP 
option 51) 
lease-default {time 
<days> [<hours> 
[<minutes>]] | infinite} 
no lease-default 
Possible values: 60-8640000 seconds (100 
days); infinite (lease never expires, unless the 
client releases it.) 
Notes: 
• If you configure lease validity time to 
between 60 and 8640000 (100 days) 
seconds, the server grants it. 
• If you configure less than 60 seconds, the 
server offers 60 seconds. 
• If you configure more than 8640000 
seconds, the server offers 8640000 
seconds. 
• If the client does not send option 51, i.e. it 
does not state for how much time it 
requires the lease, the server offers the 
default lease time (one day, unless 
otherwise configured). 
• Repeating this command replaces the 
previous one. 
Configuring NetBIOS 
name server (DHCP 
option 44) 
netbios-name-server 
<address> [<address-2>] 
no netbios-name-server 
 
address – NetBIOS name server IPv4 address 
address-2 – Second NetBIOS name server IPv4 
address 
Note: Repeating this command replaces the 
previous one. 
Configuring NetBIOS 
node type (DHCP option 
46) 
netbios-node-type 
<type> 
Type – NetBIOS node type 
Possible values: b, p, m, h 
6. Management and Security 
Task 
Command 
Comments 
no netbios-node-type 
Note: Repeating this command replaces the 
previous one. 
Configuring client 
network IPv4 address and 
mask 
network <ipv4-
address>/<prefix-length> 
no network 
Ipv4-address – client IP address 
Prefix-length – client IP prefix length 
Possible values: 1-32 
Notes:  
• If the network is deleted or changed in 
such a way that the configured ranges are 
not in it, the device deletes the ranges 
that are out of the newly configured 
network. 
• Repeating this command replaces the 
previous one. 
• Either the host or network command can 
be configured; not both.  
• The IP address (while taking into account 
the prefix length) must be a subnet 
address. 
• The same pair of address and prefix length 
cannot be configured on more than one 
pool. 
Configure relay agent 
information (DHCP 
option 82) 
relay-information circuit-
id <circuit-id> 
relay-information 
remote-id <remote-id> 
no relay-information 
Matching the received option 82 with the 
configuration determines the clients that can 
receive offers of the pool. 
Notes:  
• Repeating this command replaces the 
previous one. 
• Either circuit-id or remote-id can be 
specified, as only one of them can be 
matched with received option 82. 
• Option 82 cannot be matched with a hex 
pattern. 
• The relay agent information option can be 
configured only if the pool is bound to a 
network. 
The same pair of address and prefix length 
cannot be configured on more than one pool. 
6. Management and Security 
Task 
Command 
Comments 
Configure TFTP server 
name (DHCP option 66) 
tftp-server-name 
<name> 
no tftp-server-name 
 
Viewing DHCP Server Binding 
You can display the DHCP server binding database, which includes all IP addresses that have already 
been assigned, lease expiration time and date, and the hardware addresses of the clients. 
 To display the DHCP server binding information: 
• 
At the config>system>dhcp-server# prompt, enter show binding. 
The DHCP server binding information is displayed. 
IP Address   : 192.168.1.1 
Binding State: active 
Bound to     : 
    MAC      : 11:22:33:44:55:66 
    ID       : 0x01 rad111 
Lease Time   : 864000 seconds 
Expires At   : 1949/10/01 01:11:12 
DHCP Server Binding Parameters 
Counter 
Description 
IP Address 
Lease IPv4 address 
Binding State 
Binding state. 
Possible values: free, offered, active, expired, 
released, abandoned, permanent, bootp, 
blocked 
Bound to MAC 
Client MAC address 
Possible values: MAC address, formatted 
xx:xx:xx:xx:xx:xx 
Bound to ID 
Client ID 
Possible values: Hex string. Readable characters 
are printed as is; for non-readable, the hex 
value is printed preceded by 0x; for example: 
0x01 rad111. 
6. Management and Security 
Counter 
Description 
Lease Time 
Lease time in seconds 
Expires At 
Lease expiration date and time, formatted as 
other date and time parameters in the device 
Viewing DHCP Server Conflict 
You can display the DHCP server conflict information, which includes all address conflicts that have been 
recorded by the DHCP server, including: 
• 
Abandoned addresses – addresses that clients have declined (they expire after a timeout) 
• 
Blocked addresses – addresses that were in use without the server assigning them. 
 To display the DHCP server conflict information: 
• 
At the config>system>dhcp-server# prompt, enter show conflict. 
The DHCP server conflict information is displayed. 
IP Address       Expires in  
--------------------------- 
1.1.1.1          --  seconds 
100.100.100.100  390 seconds 
DHCP Server Conflict Parameters 
Counter 
Description 
IP Address 
Conflict IPv4 address 
Expires in 
Time (in seconds) remaining before the conflict expires 
Possible values:  
--  –  if there is no expiration time, such as for blocked 
addresses 
number – if there is an expiration time, such as for 
abandoned addresses 
Viewing DHCP Server Statistics 
You can display the DHCP server statistics. 
6. Management and Security 
 To display the DHCP server statistics: 
• 
At the config>system>dhcp-server# prompt, enter show statistics. 
The DHCP server statistics are displayed. 
Address Type  Total  
------------------- 
Free          10 
Offered       1 
Active        100 
Expired       2 
Released      -- 
Abandoned     -- 
Permanent     -- 
Bootp         -- 
Blocked       1 
DHCP Server Statistics Counters 
Counter 
Description 
Free 
Total number of free addresses 
Offered 
Total number of offered addresses 
Active 
Total number of active addresses 
Expired 
Total number of expired addresses 
Released 
Total number of released addresses 
Abandoned 
Total number of abandoned addresses 
Permanent 
Total number of permanent addresses 
Bootp 
Total number of bootp addresses 
Blocked 
Total number of blocked addresses 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
 
Message 
Cause 
Corrective Action 
No such address 
You tried clearing an IPv4 address 
that does not exist in the database. 
Make sure the address is in the 
database. 
6. Management and Security 
Message 
Cause 
Corrective Action 
The pool is not bound to network 
You tried to configure a range of 
addresses for a pool that has not 
been bound to a network. 
Bind the pool to a network using 
the network command.  
Range is not inside the pool’s 
network 
You tried to configure a range that 
is not in the pool’s subnet.  
Configure a range inside the pool’s 
subnet, using the network 
command. 
Range is already configured 
You can only configure a single 
range per pool. You already 
configured a range for the pool. 
Delete the existing address range, 
and then configure a new range. 
Range does not exist 
You tried to delete an address 
range that is not exactly the same 
as the one configured.  
Delete the exact address range that 
you configured. 
The pool is not bound to host 
You tried to configure a network 
while a host is configured. 
Unbind the pool from the network, 
and bind it to a host using the host 
command.  
You tried to configure a client 
identifier (option 61) or hardware 
address (MAC) for a pool that is not 
bound to a host.  
Bind the pool to a host using the 
host command. 
Cannot have both client-identifier 
and hardware-address 
You configured a client identifier 
when a hardware address is 
already configured, or vice versa. 
Remove the client identifier or 
hardware address configuration. 
Client identifier configured on 
different pool 
You tried to configure a client 
identifier that has already been 
configured on another pool. 
Configure a unique client identifier. 
Hardware address configured on 
different pools. 
You tried to configure a hardware 
address that has already been 
configured on another pool. 
Configure a unique hardware 
address. 
The pool is bound to network 
You tried configuring a host while 
pool was bound to a network. 
Unbind the pool from the network. 
Invalid address or prefix length 
You entered a non-unicast address. 
Enter a valid unicast address 
(taking into account the prefix 
length). 
Address and prefix configured on 
another pool 
You configured the same pair of 
address and prefix length on 
another pool. 
Configure a unique address and 
prefix length pair. 

## 6.6 DHCPv6 Server  *(p.327)*

6. Management and Security 
Message 
Cause 
Corrective Action 
The pool is bound to host 
You tried configuring a network 
while pool was bound to a host. 
Unbind the pool from the host. 
Invalid address or prefix length 
In case of a host: You entered a 
non-unicast address.  
Enter a valid unicast IP address 
(taking into account the prefix 
length). 
In case of a network: You entered a 
non-subnet address. 
Enter a valid subnet IP address 
(while taking into account the 
prefix length). 
6.6 DHCPv6 Server  
ETX-1p supports Dynamic Host Configuration Protocol Version 6 (DHCPv6) server functionality for IPv6 
clients. DHCPv6 server assigns to DHCPv6 clients IPv6 addresses from configured pools, in response to 
broadcast requests of DHCPv6 clients. This functionality eliminates the need to manually assign an IP 
address for each potential client. In addition, layer-2 or layer-3 DHCP relays can negotiate DHCP 
information on behalf of a client, if the client and server are not directly connected.  
You can configure a single DHCP server on any VRF (router instance). 
Note 
• 
DHCPv6 server, relay, and client applications are independent. You can 
configure neither or any combination of them. 
• 
DHCP server is not supported on tunnel interfaces.  
 
Applicability and Scaling 
This feature is applicable to ODM HW devices with an embedded router.  
Standards Compliance 
 [RFC 3315] – Dynamic Host Configuration Protocol for IPv6 (DHCPv6) 
[RFC 3633] – IPv6 Prefix Options for DHCPv6 
[RFC 3646] – DNS Configuration Options for DHCPv6 
6. Management and Security 
[RFC 4862] – IPv6 Stateless Address Autoconfiguration 
Benefits 
The main benefits of DHCP servers are: 
• 
Reduced costs of IP addresses – There is no need to buy and manage an IP address for each 
potential client. For example, there is no need to manually assign an address for each machine 
that is connected to the network, even briefly or rarely. 
• 
Reduced access costs – Dynamic addresses are cheaper than static addresses. 
• 
Reduced client configuration costs – DHCP ease of configuration leads to fast deployment and 
less operational overhead. There is no need to manually configure connectivity parameters on 
each client, except for very basic configuration (and sometimes not even this). The DHCP server 
can even start a zero touch configuration process, which completely configures the client 
without network manager intervention. 
• 
Centralized management – Network managers only need to configure a single central server. If a 
global parameter, e.g. DNS server, is changed, there is no need to manually configure all the 
clients in the network. 
Functional Description 
DHCPv6 server can operate in two modes: 
• 
Stateless mode – The client derives its IP address from Router Advertisements (RA) and the 
server only provides options that cannot be obtained by RA, such as DNS server address.  
• 
Stateful mode – The server provides IP addresses as well, and saves the bindings (IP address to 
hardware address) in permanent memory. This enables it to grant clients the same addresses 
they previously had, to minimize the possibility of their addresses being replaced.  
If it is important to preconfigure an address, typically of a router or a server, it is possible to configure a 
manual binding, which directs the server to grant a fixed address to a specific client (recognized by MAC 
address or other data). 
The following describes the DHCP flow, from the time the client sends a broadcast DHCP request and 
until the IP addresses are distributed. 
1. The DHCP client sends to the DHCP server a broadcast DHCP request (requesting a lease). If the 
client and server are not directly connected to each other, the DHCP messages can be forwarded 
by a DHCP Layer 2 or Layer 3 relay agent. 
6. Management and Security 
2. The DHCP relay agent (if one exists) intercepts the request and broadcasts it toward the DHCP 
server. 
3. Any listening DHCP server can assign an IP address to the DHCP client (based on information sent 
by the client or relay agent), as well as other options.  
4. DHCPv6 server sends the client a client identifier option (1) in DHCPv6 messages. The identifier it 
carries is called DUID (DUID types: LLT, EN, and LL). 
Note 
If the DHCP server offers a lease and the client then sends a DHCP request 
with an IP address of a different server (in option 54), the server assumes that 
the request is no longer relevant, and returns the offered address to the pool 
of available addresses.  
5. The relay agent (if one exists) forwards the lease offer to the client. 
6. The DHCP client accepts the offer. If the DHCP client received more than one lease offer, it 
chooses a lease; usually the first one it received. 
7. Before accepting a lease, a typical client sends a gratuitous ARP to the IP address it is about to use. 
If two replies are received, the client should decline the lease, and the server places the IP address 
into the conflicts table. 
8. The server acknowledges the lease.  
ETX-1p saves the lease in a database that includes all active and inactive leases. The lease database with 
address binding (IP address to client hardware address) resides in permanent memory that withstands 
reboot. If possible, ETX-1p assigns to clients the same IP addresses they previously had.  
The lease is usually granted for a limited time; therefore, the DHCP client should renew it before it 
expires. A DHCP client may also release a lease once is no longer needed. 
The server does not delete a binding from the database when a lease expires. However, if a new client 
asks for an address and the server does not have a free address, then one of the unused addresses from 
the database may be used.  
ETX-1p may function as DHCP client or server at the same time.  
In cases when it is important that a client, usually a router or server, not change its address, it is possible 
to configure manual bindings, i.e. IP addresses that are manually mapped to clients. This directs the 
server to grant fixed addresses to specific clients (usually recognized by their MAC address). 
6. Management and Security 
Factory Defaults 
By default, no DHCPv6 server or DHCPv6 server pool is defined. When a DHCPv6 server or DHCPv6 
server pool is first defined, it is configured as shown below. 
Parameter 
Default Value 
DHCP server 
 
number 
1 
pool 
no pool 
DHCP server pool 
 
address-prefix 
no address-prefix 
length 
64 
valid-lifetime 
86400 (one day) 
preffered-lifetime 
86400 (one day) 
dns-server 
no dns-server 
domain-search-list 
no domain-search-list 
learn-from-dhcpv6-client 
no learn-from-dhcpv6-client 
Configuring DHCPv6 Server 
You can configure the DHCP server as follows: 
1. By default, no DHCPv6 server exists. Create a single instance of DHCPv6 server over any VRF 
supported in the router. 
2. Configure DHCP pools containing: 
 
Range of addresses (or a single address) to assign to clients 
 
Various DHCP options to send to clients 
 
Definitions of clients eligible to get lease from the pool 
3. Host and subnetwork inherit options from larger networks (simplifying the configuration): 
 
For example, a global pool (e.g. 192.168.0.0) can contain global options, such as domain 
name. 
 
Additional pools are set for subnets (e.g. 192.168.1.0 and 192.168.2.0), each with its own 
default gateway. 
6. Management and Security 
 To configure the DHCPv6 server: 
1. Navigate to configure system dhcpv6-server [<number>]. 
Note 
• 
<number> is the number of the dhcpv6-server, which can only be 1.  
• 
Type no dhcpv6-server to remove the DHCPv6 server from the router.  
2. At the config>system>dhcpv6-server (1)# prompt, perform the required tasks according to the 
following table. 
Task 
Command 
Comments 
Configuring DHCP server pool 
[no] pool 
See Configuring DHCP Server Pool. 
Typing no pool removes the DHCP 
server pool and the configuration 
related to it (IP address ranges and 
DHCP options). 
Displaying DHCP server bindings 
show binding 
See Viewing DHCP Server Binding  
 
Note 
Unlike DHCPv4 server, the DHCPv6 server (once created) is always enabled 
and there is no command to disable it. However, you have to bind it to an 
interface to make it work. 
Configuring DHCP Server Pool 
By default, no DHCPv6 server pool exists. The following procedure describes how to create a DHCPv6 
server pool. Each pool must be assigned a unique name.  
The DHCPv6 server offers leases based on the pools’ configurations.   
 To configure the DHCPv6 server pool: 
1. Navigate to configure system dhcp-server pool [name]. 
2. At the config>system>dhcp-server>pool# prompt, perform the required tasks according to the 
following table. 
Note 
• 
Typing no pool removes the DHCPv6 server pool, as well as the 
configuration related to it. 
• 
You must assign a unique pool name of 1 to 80 characters.  
 
6. Management and Security 
Task 
Command 
Comments 
Configuring IPv6 prefix for 
address assignment 
 
address-prefix <prefix>/<length> 
[lifetime {<valid-lifetime> 
<preferred-lifetime> | infinite}] 
no address-prefix <prefix>/<length> 
prefix – IPv6 prefix 
length – IPv6 prefix; 0-128 
valid-lifetime – 60-8640000 (one 
minute to one hundred days) 
preferred-lifetime – 60-8640000 
(one minute to one hundred days) 
Notes: 
• A pool may be associated with 
multiple address prefixes. If the 
command is repeated with a 
different prefix and length it is 
added to the configuration. If it is 
repeated with the same prefix 
and length it replaces the 
previous command for that prefix 
and length. The reason to do this 
is to change the lifetime. 
• There may not be more than one 
pool with the same address 
prefix. If you try to configure this, 
the command is rejected, with 
the error: Address prefix in use in 
another pool 
• If infinite is specified, octets 18-
21 and 22-25 are 0xffffffff. 
• preferred-lifetime may not be 
greater than valid-lifetime. If you 
configure this, the command is 
rejected, with the error: 
Preferred lifetime may not be 
greater than valid lifetime 
Configuring DNS server (DHCPv6 
option 23) 
dns-server <ipv6-address> [<ipv6-
address-2>]  
no dns-server 
ipv6-address – DNS server IPv6 
address  
ipv6-address-2 – second DNS server 
IPv6 address  
Notes:  
• Repeating this command replaces 
the previous one. 
• address-2 must be different than 
address-1. 
6. Management and Security 
Task 
Command 
Comments 
Configuring domain search list 
(DHCPv6 option 24) 
domain-search-list <domain-name> 
no domain-search-list [<domain-
name>] 
domain-name - 1-255 character 
string 
Notes:  
• Repeating this command adds it 
to the configuration. 
• If domain-name is omitted (in the 
no form), the entire list is 
deleted. 
• If the name is not FQDN, ETX-1p 
rejects the command and prints: 
cli_error: Name must be FQDN 
Learning pool configuration 
from DHCPv6 client 
[no] learn-from-dhcpv6-client 
router <router> interface 
<interface>  [stateless] 
 
router, interface – router interface 
from which to learn DHCPv6 
information 
no learn-from-dhcpv6-client  -  
DHCPv6 server does not pass to 
clients information learned from a 
DHCPv6 client. 
learn-from-dhcpv6-client  - DHCPv6 
server passes to clients information 
learned from a DHCPv6 client, 
including IP addresses learned from 
PD. 
learn-from-dhcpv6-client stateless  -  
DHCPv6 server passes to clients 
information learned from a DHCPv6 
client, except IP addresses learned 
from PD. 
Viewing DHCP Server Binding 
You can display the DHCP server binding database, which includes all IP addresses that have already 
been assigned, lease expiration time and date, and the hardware addresses of the clients. 
 To display the DHCP server binding information:   
• 
At the config>system>dhcp-server# prompt, enter show binding. 
The DHCP server binding information is displayed. 
config>system>dhcp6-server(1)# show binding 
6. Management and Security 
Interface           : Ethernet wan1 
Client DUID         : LL 1 00:01:02:03:04:05 
Client IPv6 Address : dead:beef:ffff:1::1/128 
State               : Bound  
Lease Time (seconds): 86400 
Expires (seconds)   : 125  
DHCPv6 Server Binding Parameters 
Counter 
Description 
Interface 
Interface from which the lease request was received 
Client DUID 
Possible sets of values (depends on DUID type): 
• LLT, hardware type (a number), time, link-layer address 
• EN, enterprise number, identifier (string) 
• LL, hardware type (a number), link-layer address 
Client IPv6 Address 
Lease IPv6 address / prefix length 
State 
Binding state.  
Possible values: Abandoned, Bound, Init, Reconfigure, Release, 
Renewing, Requesting, Selecting 
Lease Time 
Lease time in seconds 
Possible values: Infinite, <number of seconds> 
Expires  
Lease expiration time in seconds 
Possible values: Infinite, <number of seconds> 
Configuration Errors  
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
Message 
Cause 
Corrective Action 
No such address 
You tried clearing an IPv6 
address that does not exist in 
the database. 
Make sure the address is in the 
database. 
 
An address cannot be 
configured more than once 
You configured the same 
value for address-2 and 
address. 
address-2 must be different from 
address.  

## 6.7 Enrollment Notification  *(p.335)*

6. Management and Security 
Message 
Cause 
Corrective Action 
A different prefix name is 
associated with this interface 
You tried to repeat the 
command with a different 
prefix name than previously 
configured. 
Repeat the command with the same 
prefix name as previously 
configured. 
Address prefix in use in  
another pool 
You configured another pool 
with the same prefix. 
Configure pool with a unique address 
prefix. 
DHCP client is configured on 
this interface 
The DHCPv6 client, server 
and relay functions are 
mutual exclusive on an 
interface.  
You tried to configure the 
DHCPv6 server or relay on 
the same interface on which 
a DHCPv6 client is enabled 
 
DHCP relay is configured on 
this interface 
The DHCPv6 client, server 
and relay functions are 
mutual exclusive on an 
interface.  
You tried to configure the 
DHCPv6 server or client on 
the same interface on which 
a DHCPv6 client is enabled 
 
Preferred lifetime may not be 
greater than valid lifetime 
You configured preferred 
lifetime to a value greater 
than valid lifetime. 
Configure preferred lifetime to a 
value not greater than valid lifetime. 
Name must be FQDN 
The domain name 
configured under domain-
search-list command is not a 
fully qualified domain name 
(FQDN). 
Configure a fully qualified domain 
name. 
 
6.7 Enrollment Notification  
ETX-1p supports a mechanism that sends enrollment notification to management system when device 
configuration is set and run. 
 
6. Management and Security 
Applicability and Scaling 
This feature is applicable to all ETX-1p devices.   
Standards Compliance  
Enrollment notification is RAD proprietary functionality.  
Benefits 
This feature allows automatic notification to the management system when the device configuration is 
set and run. 
Functional Description 
When enrollment notification is enabled, the device sends the enrollment notification to the target 
periodically, until the command no enrollment-notification is entered, or until getting acknowledge that 
the message was communicated and received. If ETX-1p reboots before the acknowledge, it resumes 
sending the notification after it completes its startup. 
Factory Defaults 
By default, enrollment notification is not configured. 
Configuring Enrollment Notification 
You can configure the enrollment notification as follows. 
 To configure the enrollment notification: 
3. Configure the device name (config>system#name), if not yet configured (see Product Information 
in Administration Chapter).  
4. Configure the management address as described in Management Source IP Address in this 
chapter. 
6. Management and Security 
5. At the config>mngmnt>access# prompt, perform the required tasks according to the following 
table. 
Task 
Command 
Comments 
Transmitting enrollment 
notification to NMS 
 
enrollment-notification-nms 
<address> 
no enrollment-notification-nms 
<address>  
 
See Configuring the NMS Level 
<address>: valid IPv4 or IPv6 unicast 
address 
Default: The enrollment is not 
configured. 
Displaying enrollment status 
show enrollment-status  
 
See Viewing Enrollment Notification 
Information  
Configuring the NMS Level 
Once you enable enrollment notification to a specific NMS as shown above, you can configure its 
parameters.   
 To configure the notification to a specific NMS: 
1. Navigate to configure management access enrollment-notification-nms <address>. 
2. At the config>mngmnt>access#>enrollment-notification-nms# prompt, perform the required 
tasks according to the following table. 
 
Task 
Command 
Comments 
Configuring NMS username and 
password  
 
nms-username <name> password 
<password> [hash] 
[no] nms-username 
Possible Values: 1-80 characters 
Disabling enrollment 
notification 
[no] shutdown 
 
Default: shutdown 
Configuring SNMP profile 
snmp-profile <name> 
[no] snmp-profile 
Possible Values: 1-80 characters 
 
Configuring SSH username and 
password  
 
ssh-username <name> password 
<password> [hash] 
[no] ssh-username 
Possible Values: 1-80 characters 
 
6. Management and Security 
Viewing Enrollment Notification Information 
You can display the enrollment notification information, which includes the Enrollment Notification 
Target and the notification status. 
 To display the enrollment notification information:   
• 
At the config>mngmnt>access# prompt, enter show enrollment-status. 
The enrollment notification information is displayed. 
>config>mngmnt>access# show enrollment-status  
Enrollment Notification Target : 10.205.205.165 
Status                         : Configuration Missing 
Enrollment Notification Parameters 
Counter 
Description 
Enrollment Notification Target  
IPv4 or IPv6 unicast address 
Status             
Enrollment notification status: 
• ON – device is waiting for acknowledge from the NMS. 
• ACKNOWLEDGE – notification was acknowledged. 
• Authentication Failure – authentication failure with NMS. 
• Permission Failure – permission failure with NMS. 
• Configuration Missing – missing configuration for communication 
with NMS. 
Example 
config>mngmnt>access# info 
    echo "NMS Enrollment notification configuration" 
#   NMS Enrollment notification configuration 
    enrollment-notification-nms 10.205.205.165 
        shutdown 
        nms-username "admin_rest" password "7A2722F2D3DC3F7D70C7A2CF5BECB79F" hash 
        ssh-username "su" password "EE680A96684DDB93" hash 
        snmp-profile "(V3) RAD-V3" 
    exit 
 
config>mngmnt>access# show enrollment-status  
Enrollment Notification Target : 10.205.205.165 
Status                         : Configuration Missing 

## 6.8 Firewall  *(p.339)*

6. Management and Security 
Configuration Errors  
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
Message 
Cause 
Corrective Action 
IP address must be a valid 
unicast 
The specified enrollmet IP 
address is not a valid unicast 
address. 
 
Maximum number of NMS has 
been reached 
 
Up to four NMS can be 
configured. You are trying to 
configure the fifth one 
 
6.8 Firewall  
ETX-1p features a zone-based stateful firewall. Interfaces are assigned to zones, and interzones (each 
comprising an “in zone” and “out zone”) are defined for which a set of ACL rules is configured. The 
firewall supports both IPv4 and IPv6 rules. The rules include IP source and destination networks, IP host 
addresses, TCP/IP ports and IP protocols.  
Applicability and Scaling 
The device supports up to 100 interzones, up to 32 zones and up to 32 members (in all zones).  
Standards Compliance  
 The ETX-1p firewall is similar to the industry standard. 
Benefits  
A firewall acts as a barrier between networks (typically a private internal network and the public 
Internet). The main purpose of using a network security firewall in the network system is to allow non-
threatening traffic in and to keep dangerous traffic out of the network. 
6. Management and Security 
Functional Description 
Zone 
A firewall zone is a collection of entities sharing a firewall policy. Users can create zones and bind 
supported interfaces to them. 
A hardcoded management zone is created by the device at startup. It cannot be deleted and users 
cannot add members to it.  
Possible members (of non-management zones) are Ethernet port, Ethernet vlan, cellular port, tunnel 
interface and WiFi access point. The device supports up to 32 members (in all zones).  
When a zone is deleted all its member bindings are deleted as well. If it is recreated it will have no 
members. 
Interzone 
Firewall interzone is a relationship between two zones, on which firewall functionality is configured. 
Packets moving from the in zone to the out zone are flowing in the outbound direction, while packets 
moving from the out zone to the in zone are flowing in the inbound direction. ACL can be attached to 
either direction and each packet is filtered according to the first ACL rule it matches. Packets unmatched 
by any ACL rule are filtered according to the firewall policy, which is (by default) to permit outbound 
connections and deny inbound connections. The user can change the policy in either direction. For more 
detail, refer to Firewall Additions to ACL Lists in this chapter. 
When a packet enters in interzone, the device tries to match it against the ACL rules and acts according 
to the first matching rule. If there is no match, the packet is handled according to the policy defined by 
the packet-filter command. You can bind one IPv4 and one IPv6 ACL in either direction, inbound or 
outbound. If the direction is unspecified the ACL will be bound in the outbound direction.  
By default, inbound connections (from the out zone to the in zone) are denied and outbound 
connections (in to out) are permitted. 
This command applies to any traffic not matched by the ACL attached to the interzone (all traffic if ACL is 
not attached). Thus, you can create a basic firewall, by allowing any traffic to originate from the “in” 
zone towards the “out” zone, but not allowing connections to originate from the “out” zone towards the 
in zone.  
Unlike ACLs bound to an interface, those bound to a firewall interzone have no IPv4 or IPv6 default 
rules. The default firewall policy allows all outbound connections and blocks inbound ones. 
The firewall is disabled by default on an interzone. 
6. Management and Security 
Packet Filtering Behavior 
Invalid packets, the ones that are not legal in an IP network (e.g. incoming packets with source IP 
address owned by the firewall, with source or destination address 127.0.0.1...) are always silently 
discarded by the firewall. 
ACL deny rules discard all packets matching their conditions, in either the inbound or the outbound 
direction. 
ACL permit rules allow packets matching their conditions in either the inbound or the outbound 
direction (with source and destination reversed), except for the first packet of a connection, which is 
permitted only in the direction the ACL is bound to (i.e., for outbound ACL the first packet of a 
connection must come from the in zone and be destined to the out zone; for inbound ACL it must come 
from the out zone and be destined to the in zone). Packets related to the connection (e.g., ICMP 
redirects initiated by it, active FTP data connection...) are permitted as well. 
Unlike ACLs bound to an interface, those bound to a firewall interzone have no IPv4 or IPv6 default 
rules. The default firewall policy allows all outbound connections and blocks inbound ones. 
The firewall is disabled by default on an interzone. 
Blacklist   
Sometimes it is desirable to prevent an IP address from sending anything through the firewall, either 
temporarily or permanently. The firewall keeps a blacklist for this purpose, to which users can relegate 
IP addresses. In some cases, the firewall can identify an IP address launching a DoS (or other) attack, and 
quarantine it in the blacklist.  
By default, addresses are permanent, but you can specify the number of minutes (1-4294967295) the 
address should be blacklisted. Only permanent addresses are saved in configuration and survive reboot. 
Time-limited addresses are not saved in configuration and are released from the list once their time is 
up, or if the device reboots, whichever occurs first. 
Packets from blacklisted addresses to any entity protected by the firewall are discarded, regardless of 
any other (including firewall) configuration.  
In case of no blacklist, if the address exists in both the configured and the learned tables, it should be 
removed from both. 
The firewall actually keeps two blacklists, of user-configured addresses and of learned ones (as a result 
of an attack). An address can be in both lists, optionally with different aging times (this can only happen 
if a user blacklists an address that was learned before; the other way around is impossible since packets 
from a blacklisted address are silently discarded). An address is considered blacklisted unless it is not in 
any of the lists.   
6. Management and Security 
If a user configures a blacklisted address that already exists in the configured list, the time of the new 
configuration replaces the current one, no matter which is higher. 
Note: Once an address is blacklisted, packets from it are silently discarded until its aging time is over. 
Further attacks it launches while being quarantined will not be detected.  
Coping With Attacks  
The firewall can detect and stop some attacks. These capabilities are enabled by default but can be 
disabled if unwanted.  
You can use the ip-sweep-defend command to enable detection and defense against IP sweep attack. 
This attack is launched by sending lot of ICMP packets in short time to many addresses on a network. If a 
machine sends packets at a rate higher than the configured one, the firewall blacklists the attacker 
address for a preconfigured time, during which packets from the attacker are discarded, regardless of 
any other (including firewall) configuration. 
Defense against IP sweep attack is enabled by default, in any zone in which the firewall is enabled. 
By default, IP sweep attack is determined if a machine sends packets at rate higher than 2000 PPS. You 
can configure anything between 10-100000. 
Attacking address is blacklisted for 20 minutes by default. You can change this to anything between 1-
10080. 
Factory Defaults  
By default, no firewall is defined. When a firewall is first defined, it is configured as shown below.  
Parameter 
Default Value 
interzone 
 
access-group 
outbound 
packet-filter default-inbound  
deny 
packet-filter default-outbound  
permit 
shutdown  
shutdown 
zone 
 
member 
No entity is bound to the zone 
ip-sweep-defend  
 
6. Management and Security 
Parameter 
Default Value 
blacklist-time 
20 (min) 
max-rate  
2000 pps  
Configuring the Firewall 
You can configure the firewall as follows: 
 To configure the firewall: 
1. Navigate to configure>access-control>firewall. 
2. At the config>access-control>firewall# prompt, perform the required tasks according to the 
following table. 
Task 
Command 
Comments 
Blacklisting an IP address 
blacklist <ip-address> [expiration-
time <minutes>] 
no blacklist <ip-address> 
 
Removing IP address from the 
blacklist 
blacklist-clear 
[{configured|learned] 
 
Entering the interzone level 
interzone in-zone <zone1-name> 
out-zone <zone2-name> 
no interzone in-zone <zone1-
name> out-zone <zone2-name> 
The device supports up to 100 
interzones 
Zone name possible values: 1-79 
characters 
The two zones comprising the 
interzone must exist before the 
interzone is created.  
Protecting the device from IP 
sweep DoS attack 
ip-sweep-defend [blacklist-time 
<minutes>] [max-rate <pps>] 
no ip-sweep-defend 
Default: ip-sweep-defend 
blacklist-time – Number of minutes 
to quarantine attacker in blacklist 
Possible Values: 1-10080 
Default: 20 
max-rate – Rate considered as 
attack 
Possible Values: 10-100000 
Default: 2000 
6. Management and Security 
Task 
Command 
Comments 
Displaying the blacklist 
show blacklist-summary {address 
<ip-address> | learned | 
configured} 
 
Entering the Zone level 
 
zone <zone-name> 
no zone <zone-name> 
 
If a zone is deleted all its members 
are deleted as well 
zone-name possible values: 1-79 
characters (case-sensitive)  
ACL names are not allowed to 
contain spaces or the following 
characters: 
!@$%^&*(){}[]+=\/?~`|:;#'>< 
Up to 32 zones can be configured 
Interzone Level 
The following commands are available in the interzone context: config>access-control>firewall> 
interzone#:  
Task 
Command 
Comments 
Binding the ACL to an 
interzone and 
defining the ACL 
direction 
access-group <acl-name> [{inbound|outbound}] 
no access-group <acl-name> 
 
Clearing ACL 
statistics 
clear-access-list-statistics [{in|out}] [{ipv4|ipv6}] 
 
Configuring the 
firewall default 
packet filtering 
packet-filter default-inbound deny | permit} 
default-outbound {deny | permit} 
 
Disabling the firewall 
on this interzone 
shutdown 
no shutdown 
 
Displaying ACL 
statistics 
show access-list-statistics [{in|out}] 
[{ipv4|ipv6}] 
See Viewing ACL Statistics below.  
Zone Level 
The following commands are available in the config>access-control>firewall>zone# context:  
6. Management and Security 
Task 
Command 
Comments 
Binding entity to 
zone 
[no] member cellular < port-index> 
[no] member ethernet <port-
index> [vlan <vlan-number>] 
[no] member tunnel-interface 
<router-number> <interface-
number> 
[no] member wifi-client [number]  
[no] member wlan <port-index> 
access-point <ap-number> 
The device supports up to 32 members (in all 
zones) 
Default: no entity is bound to the zone. 
 
Examples 
The following configuration permits “lan” to only access 1.1.1.1, and “wifi” to only access 8.8.8.8: 
 
configure 
        access-control 
            access-list "11" 
                permit ip any 1.1.1.1 sequence 10 
            exit 
            access-list "88" 
                permit ip any 8.8.8.8 sequence 10 
            exit 
            firewall 
                zone "wan" 
                    member ethernet 1 
                exit 
                zone "lan" 
                    member ethernet 4 
                exit 
                zone "wifi" 
                    member wlan 2.4g access-point 1  
                interzone in-zone "lan" out-zone "wan" 
                    access-group "11" 
                    packet-filter default-outbound deny 
                   no shutdown 
                exit 
                interzone in-zone "wifi" out-zone "wan" 
                    access-group "88" 
                    packet-filter default-outbound deny 
                   no shutdown 
                exit 
            exit 
6. Management and Security 
        exit 
 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
Message 
Cause 
Corrective Action 
The two zones must be different 
ones 
You specified the same zone 
twice. 
Specify two different zones. 
Interzone with these zones in the 
reverse order exists  
 
An interzone with the same 
zones in reverse order already 
exists. 
 
The zone does not exist 
 
The two zones comprising the 
interzone must exist before it is 
created.  
 
This ACL is bound in the reverse 
direction 
The same ACL cannot be bound 
in both directions 
 
The management zone cannot be 
deleted 
 
You tried to delete the 
permanent management zone 
created by the device at startup  
 
The zone is part of an interzone 
 
You tried to delete a zone that 
is part of an interzone 
 
Members may not be added to 
the management zone 
 
This command cannot be 
executed, and is masked, in the 
management zone. You tried to 
execute the command in the 
management zone, which is 
impossible 
 
Entity is member of a different 
zone 
The entity is already a member 
of a zone 
 
6. Management and Security 
Message 
Cause 
Corrective Action 
Unexpected argument 
 
Arguments in the deny and 
permit commands are expected 
at the order they appear in the 
CLI (for example, configuring 
sunday before Monday is not 
allowed) 
 
Name cannot contain 
!@$%^&*(){}[]+=\/?~`|:;#'><, or 
spaces  
 
ACL names are not allowed to 
contain spaces or the following 
characters: 
!@$%^&*(){}[]+=\/?~`|:;#'><,  
 
Invalid argument if ACL is bound 
to firewall interzone 
 
If the ACL is bound to a firewall 
interzone, control flags are not 
allowed.  
 
Cannot configure rate burst 
without rate limit 
You tried to configure rate-
burst without rate-limit, this is 
not allowed. 
 
Cannot configure size burst 
without size limit 
 
You tried to configure size-
burst without limit-size, this is 
not allowed.  
 
End time cannot be earlier than 
start time 
You specified the end time 
earlier than the start time 
 
No such address in the list 
 
You used no blacklist for an 
address that does not exist in 
the blacklist   
 
Viewing ACL Statistics 
 To display the ACL statistics: 
1. At the config>access-control>firewall>interzone# prompt, enter show access-list-statistics ipv4 
(for IPv4) or show access-list-statistics ipv6 (for IPv6). 
The following statistic information is displayed: 
Note 
If you do not specify an IP version, the device displays the statistics of the IPv4 
ACL (if exists), followed by those of the IPv6 ACL (if exists).  
 
6. Management and Security 
IPv4 Access List   : block-invalid-traffic 
Matches Counted For: 7 Seconds 
 
Ena Number Action Prot Source      Port Destination Port Flags Log Matches 
-------------------------------------------------------------------------- 
Yes 10     Permit TCP  10.10.10.10 1000 20.20.20.20 2000 NERI  --  0 
 
Parameter 
Description 
Ena 
 
ACL statement administrative state 
 
Possible Values: Yes, --- 
Number 
ACL rule sequence number 
Action 
 
ACL rule 
Possible Values: Deny, Permit 
Prot 
 
ACL rule protocol 
Possible Values: ICMP, IP, TCP, UDP 
Source  
 
ACL rule source IP address 
Possible Values: Any, <IP address>[/<prefix length>] 
(Source) Port 
 
ACL rule source ports 
Possible Values:  
-- 
Any  
<port> 
<port1>-<port2>  
Destination  
 
ACL rule destination IP address 
Possible Values: Any, <IP address>[/<prefix length>] 
(Destination) Port 
 
ACL rule destination ports 
Possible Values:  
-- 
Any  
<port> 
<port1>-<port2> 
Flags 
 
ACL rule flags 
Possible values:  
• -- (No flag is set) 
• The corresponding letter of each set flag is printed (without spaces): 
[N]ew [E]stablished [R]elated [I]nvalid 
6. Management and Security 
Parameter 
Description 
Log 
ACL rule logging state 
Possible Values: --, Yes 
Matches 
Number of packets that matched the ACL rule since statistics were last 
cleared 
 To delete ACL statistics: 
1. At the config>access-control>firewall>interzone# prompt, enter clear-access-list-statistics [ipv4 | 
ipv6]. 
The statistics counters are cleared. 
Viewing the Blacklist   
You can view the blacklist  information. 
 To view the blacklist information:  
1. At the config>access-control>firewall# prompt, enter show blacklist-summary {address <ip-
address> | learned | configured}.  
 
 
The following information is displayed: 
Configured Blacklist 
---------------------------------------------------- 
Address         Entered On          Minutes To Aging 
---------------------------------------------------- 
100.100.100.100 1.Oct.1949 12:30:20 --          
 
Learned Blacklist 
----------------------------------------- 
Address         Reason   Minutes To Aging 
----------------------------------------- 
10.10.10.10     IP Sweep 20 
If no parameter is specified, the device displays the entire blacklist. 
 
Parameter 
Description 
Address 
Blacklisted IP address 

## 6.9 MQTT Server  *(p.350)*

6. Management and Security 
Parameter 
Description 
Reason 
Blacklisted IP address type 
Possible Values: Configured, IP Sweep 
 
Entered On 
Time the IP address entered the blacklist. The blacklist entry creation time 
is updated if the device time changes. 
Possible Values: Local date and time (computed from the MIB’s UTC data) 
Minutes to Ageing 
Number of minutes before the address would leave the blacklist 
Possible Values: 
• Permanent address: -- 
• Temporary address: Number 
 To remove an IP from the blacklist: 
• 
At the config>access-control>firewall# prompt, enter blacklist-clear [{configured|learned}]. 
The IP is removed from the blacklist. 
6.9 MQTT Server  
This section describes how to configure MQTT servers. 
Applicability and Scaling 
This feature is applicable to all ETX-1p devices.   
Up to two MQTT servers can be configured. 
Benefits 
This feature facilitates efficient and reliable communication between devices for use in constrained 
environments and low-bandwidth networks, enabling devices to send and receive data with minimal 
network overhead. 
6. Management and Security 
Functional Description 
MQTT, which stands for Message Queuing Telemetry Transport, is a lightweight messaging protocol 
designed for use in constrained environments and low-bandwidth networks. It employs a 
publish/subscribe model, facilitating efficient and reliable communication between devices. MQTT is 
commonly used in IoT (Internet of Things) applications, enabling devices to send and receive data with 
minimal network overhead. 
MQTTS is the secured version of this protocol. 
You can open a device management channel over MQTT with the server of this level. When enabled, the 
device can be managed over MQTT by the server. Only one server can serve as a management channel. 
When configuring the MQTTS protocol, an X.509 certificate name (1-64 characters) must be provided. 
The certificate should be a device certificate, signed by a CA. It is the responsibility of the user to make 
sure that the certificate exists and is valid.  
By configuring a certificate, MQTTS mode is implied. If no certificate is configured the device works with 
MQTT. 
The MQTTS implementation only accepts peers’ certificates signed by a CA that was preconfigured as 
trusted. Therefore, you must provide the trusted CA name (1-20 characters). 
Note: MQTTS needs a valid device certificate, the certificate (or chain of trust) of the CA that signed its 
certificate and that of the CA that signed the peer’s certificate (if it is not the same CA).  
You can also configure the user credentials for MQTT authentication (a username and password, both 
can be 1-64 characters, not configured by default). This can be done exclusively or in addition to an 
X.509 certificate (depending on whether the certificate command is configured).  
Factory Defaults 
By default, no MQTT server is defined. When an MQTT server is first defined, it is configured as shown 
below. 
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
Trusted CA is not configured 
6. Management and Security 
Parameter 
Default Value 
management-channel 
no management-channel  
 
Configuring MQTT Server 
You can configure the MQTT server as follows. 
 To configure the MQTT Server: 
2. Navigate to config>system>mqtt#. 
3. Define the server config>system>mqtt>server<server-name, 1..32 characters>#. You can 
configure up to two servers in the device. 
4. At the config>system>mqtt>server <server-name> # prompt, perform the required tasks 
according to the following table.  
Task 
Command 
Comments 
Configuring the server IP 
parameters 
address ip <ip-address> [protocol 
{ssl|tcp}] [port <port-number>] 
address url <url-string> [protocol 
{ssl|tcp}] [port <port-number>] 
no address 
<ip-address> – valid IPv4 or IPv6 
unicast address 
<url-string> - a valid URL (to be 
resolved with DNS). 
protocol – MQTT transport protocol 
(ssl or tcp) 
port – MQTT transport port 
(1..65535) 
Configuring the X.509 certificate 
for MQTTS authentication 
certificate <certificate-name> 
trusted-ca <ca-name> 
no certificate <certificate-name> 
MQTTS certificate 
<certificate-name> –  string, 1-64 
characters) 
<ca-name>– MQTTS trusted CA, 
string, 1-20 characters 
Opening a management channel 
with the server 
management-channel 
no management-channel 
 
6. Management and Security 
Task 
Command 
Comments 
Configuring user credentials for 
authentication with the MQTT 
server 
user name <username> password 
<password-string> [hash-2] 
no user 
<username>: 1-64 characters  
<password-string>: 1-64 characters 
hash-2 - password is hashed 
(encrypted) 
Displaying the server status 
show status  
See Viewing the MQTT Status below 
Example  
 To define the MQTT server with MQTTS and SSL protocols: 
  
configure system mqtt 
            server "1" 
                address url "lns1.rad.com" protocol ssl port 7883 
                certificate "1p" trusted-ca "CA" 
            exit 
 configure system mqtt 
            server "2" 
                address url "lns3.rad.com" protocol ssl port 5884 
                certificate "1p" trusted-ca "CA" 
                management-channel 
            exit 
 
Configuration Errors  
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Maximum numbers of servers have 
been reached 
You can configure no more than two 
MQTT servers 
 
Maximum number of 
management-channel servers has 
been reached  
No more than one server can serve as 
a management channel 
 
6. Management and Security 
Message 
Cause 
Corrective Action 
Note: No valid self-certificate with 
the specified name 
 
No valid self-certificate of the 
specified name exists in the device 
Note: The command will be accepted, 
but MQTT would fail until the user 
addresses the problem 
 
Note: No such CA; it must be 
configured for MQTTS to work 
This CA does not exist 
Note: The command will be accepted, 
but MQTT would fail until the user 
addresses the problem 
 
Note: Import a valid chain of trust 
for the CA, for MQTTS to work 
The device does not have a valid chain 
of trust for the CA 
Note: The command will be accepted, 
but MQTT would fail until the user 
addresses the problem 
 
Viewing the MQTT Status  
This section explains how to display the status of the MQTT server. 
 To display MQTT status:  
configure>system>mqtt>server()# show status 
Application  
 : LORA 
Server Address/URL   : ibs-lns 
MQTT Status  
 : Connected 
 The status display provides information about: 
• 
Application served by MQTT connection: 
 
Management 
 
LORA (Attached to LoRa gateway) 
 
(empty) 
• 
MQTT server address / URL 
• 
MQTT module status 
 
Not configured – configuration is missing  
 
Disconnected – connection fails after ‘Connected’ state 
 
Connected – connection process succeeded 

## 6.10 Management Access Methods  *(p.355)*

6. Management and Security 
 
Connecting – trying to connect before first “Connected” state  
• 
MQTT configuration problem (MQTT cannot start due to missing configuration) 
 
Undefined MQTT server in LoRa gateway 
 
Undefined MQTT address 
 
Undefined certificate or user 
 
There is no certificate 
6.10 Management Access Methods  
ETX-1p can be managed either locally from a terminal directly attached to the serial port, or remotely, 
through any port, via SSH, SNMP, Web or NETCONF. Management can be limited by ACLs or by 
configuring router ports as non-forwarding (effectually limiting them to management traffic). 
 
Note 
The device can be managed with IP only on router 1.  
Applicability and Scaling 
This feature is applicable to all ETX-1p options. 
Functional Description 
You can enable or disable access to the ETX-1p management system via SSH, SNMP, or NETCONF 
applications. By disabling SSH, SNMP, or NETCONF, you prevent unauthorized access to the system 
when security of the ETX-1p IP address has been compromised. When SSH, SNMP, and NETCONF are 
disabled, ETX-1p can be managed via an ASCII terminal only. A CLI session can be opened locally from 
the terminal connected to the dedicated serial port. Additionally, you can enable or disable file transfer 
via SFTP/SCP. 
Factory Defaults 
By default, access is enabled for all the applications. 
In the default factory configuration, ETX-1p allows management from the OOB management port.  
6. Management and Security 
The default factory configuration includes the following:  
• 
Allows untagged management access from the OOB port  
• 
Default IP address of the Router Interface is 169.254.1.1/16  
• 
No default Gateway configuration 
• 
Allows local management access using a PC to ETX-1p:  
 
When PC uses DHCP, access to ETX-1p is automatically established (PC address defaults to 
169.254.x.y as no DHCP server  Microsoft protocol). 
• 
Not backward compatible to user configuration CLI scripts that configure OOB port 
The factory default configuration is only loaded if there is no startup-config or user-default-config (for 
example, after executing the factory-default command).  
If you copy a script and paste it to the terminal after factory-default-config is loaded, it is important to 
verify that the configuration in the script does not conflict with the factory default configuration. 
You can delete the factory default configuration. You can also replace the factory-default with a 
download of a fresh startup-config, by performing Reset. 
You can add an additional IP address over the RI to allow remote access. 
When accessing remotely, it is possible to delete the local IP 169.254.1.1/16. 
Configuring Management Access 
This section describes how to configure general management parameters for SFTP, SNMP, SCP and SSH. 
See NETCONF-Based Network Management section for management by NETCONF. 
 To configure management access: 
1. Navigate to configure management access. 
2. At the config>mngmnt>access# prompt, enter the necessary commands according to the tasks 
listed below. 
Task 
Command 
Comments 
Allowing SFTP access 
sftp 
Typing no sftp blocks access by SFTP 
Allowing SNMP access 
snmp 
Typing no snmp blocks access by SNMP 
Allowing SSH (Secure Shell) access 
ssh 
Typing no ssh blocks access by SSH 

## 6.11 Management Ports  *(p.357)*

6. Management and Security 
Task 
Command 
Comments 
Allowing SCP access 
scp 
Typing no scp blocks access by SCP 
6.11 Management Ports  
ETX-1p can be managed either from a terminal directly attached to the CONTROL RS-232 serial port, or 
from remote, through any port.  
You can configure the Control port parameters, including the security timeout and screen size from 
which you are accessing the device. You can also disable management via the Control port.  
Applicability and Scaling 
This feature is applicable to all the device versions. 
Factory Defaults 
Parameter 
Default Value 
console-timeout limited  
10 (minutes) 
length 
20 
serial-port-disable 
no serial-port-disable 
timeout limited 
10 (minutes) 
Configuring the Console Port Parameters  
 To define the console port parameters via CLI:  
• 
At the config>terminal# prompt, enter the necessary commands according to the tasks listed 
below. 
6. Management and Security 
Task 
Command 
Comments 
Defining whether in case of 
serial console inactivity, device 
remains connected or 
disconnects after a specified 
time period 
console-timeout forever 
console-timeout limited 
<minutes> 
console-timeout forever – no timeout. 
If you define a timeout, the timeout 
value can be 1–60. The default is 10 
minutes. 
Defining the terminal screen 
size (number of rows to 
display) 
length <number-of-rows> 
The number of rows to print before 
pausing, or 0 for no pausing (no limit on 
the number of lines displayed). 
Possible values: 0-255 
Disabling the control port  
serial-port-disable 
  
Once this command is issued, console 
access is denied for normal operation.  
Management connectivity can be 
resumed in one of the following ways: 
• Entering no serial-port-disable 
command via remote access (Inband 
or OOB via SNMP). 
• Setting to default configuration, by 
pressing the external push button on 
the front panel.  
Defining whether in case of 
SSH session inactivity, device 
remains connected or 
disconnects after a specified 
time period 
timeout forever 
timeout limited 
<minutes> 
timeout forever – no timeout. 
If you define a timeout, the timeout 
value can be 1–60. The default is 10 
minutes. 
 To define the console port parameters via Web GUI:  
1. Navigate to Configure>Terminal. 

## 6.12 Management Source IP Address  *(p.359)*

6. Management and Security 
 
2. Use the Timeout button to define whether in case of SSH session inactivity, the device remains 
connected or disconnects after a specified period: 
 
Forever – no timeout 
 
Limited – to set the timeout in minutes (1-60) 
3. Use the Console Timeout button to define whether in case of serial console inactivity, the device 
remains connected or disconnects after a specified period: 
 
Forever – no timeout 
 
Limited – to set the timeout in minutes (1-60) 
4. Use the Serial Port Disable button to enable or disable the console. 
6.12 Management Source IP Address 
The management source IP address provides a single point of contact for management applications that 
interface with ETX-1p. 
Applicability and Scaling 
This feature is applicable to all the device versions. 

## 6.13 NETCONF-Based Network Management  *(p.360)*

6. Management and Security 
Functional Description 
When a router interface responds to management packets, the responding packet source IP address is 
set to the router interface IP address. If the router interface sends a management packet that is not a 
response, the packet source IP address is set to the ETX-1p management source IP address. If the 
management source IP address is not configured or the corresponding router interface is down, the 
packet source IP address is set to the router interface IP address. You can configure a single 
management source address for IPv4 and IPv6 to be used in all client management applications, 
including: SNMPv3 (for trap), RADIUS, TACACS+, Syslog, SNTP, SFTP, and SCP. 
Configuring the Management Protocols Source IP Address 
 To configure the management protocols source IP address: 
1. Navigate to configure management. 
The config> mngmnt# prompt is displayed. 
2. Type management-address <ip-address> 
 
Note 
According to the format of the IP address (IPv4 or IPv6), it is saved as the IPv4 
or IPv6 management source IP address.  
 
The management protocols source IP address is set to the specified IP address. 
3. To delete the IPv4 or IPv6 management address, type: 
no management-address {ipv4 | ipv6} 
6.13 NETCONF-Based Network Management  
NETCONF/YANG, a management interface equivalent to SNMP/MIB, enables the remote manager to 
configure and monitor the device.  
• 
Network Configuration Protocol (NETCONF) 1.1 – a protocol that provides mechanisms to install, 
manipulate, and delete the configuration of network devices. NETCONF carries configuration 
data and operations as requests and replies using RPCs encoded in XML over a connection-
oriented transport (SSH). 
6. Management and Security 
• 
YANG – a data modeling language used to model configuration and state data manipulated by 
the NETCONF, NETCONF RPCs, and NETCONF notifications.  
Applicability and Scaling 
This feature is applicable to all the device versions. 
Standards Compliance 
The supported NETCONF versions are based on the following standards: 
• 
RFC 6241 (06/2011), Network Configuration Protocol (NETCONF) 1.1 
• 
RFC 6020 (10/2010), YANG 1.0 - A Data Modeling Language for the Network Configuration 
Protocol (NETCONF) 
• 
RFC 6022, YANG Module for NETCONF Monitoring 
• 
RFC 6243, With-defaults Capability for NETCONF 
• 
RFC 5277, NETCONF Event Notifications 
• 
RFC 6470, NETCONF Base Notifications 
Benefits 
• 
Based on transactions, NETCONF reduces the burden on the network management station. 
• 
Error recovery and sequencing tasks are removed from the management side. 
• 
YANG enables writing automatic scripts on the management side. YANG models are richer than 
MIB, in that you can formally specify capability options, i.e. what is allowed and not allowed on 
the device. In MIB, you can only write a description. 
• 
Enhanced capabilities, in comparison to SNMP. 
Functional Description 
NETCONF is a session-based network management protocol that uses XML-encoded remote procedure 
calls (RPCs) and configuration data to manage network devices. 
6. Management and Security 
The mandatory transport protocol for NETCONF is SSH. The default TCP port assigned for this mapping is 
830. A NETCONF server implementation listens for connections to the NETCONF subsystem on this port. 
Use of a dedicated port makes it easier for the NETCONF server to identify and filter NETCONF traffic.  
The following are characteristics of transactions: 
• 
Transactions are indivisible; all-or-nothing. 
• 
There is no internal order inside a transaction. It is a set of all-at-once changes; not a sequence. 
• 
Parallel transactions do not interfere with each other; no-crosstalk. 
• 
Committed data always-sticks, i.e. it remains in the system even if fail-over, power failure, 
restart, or more occurs; done-is-done. 
The following deployment model shows the communication between the device (NETCONF server; 
equivalent to SNMP agent) and management station (NETCONF client; equivalent to SNMP manager).  
 
NETCONF/YANG Deployment Model 
 
Note 
NETCONF sessions, similar to CLI sessions, generate session start and session 
end events. These generated events are added by default to the event log.  
NETCONF Support 
Configuration Data Stores 
<running>  
 
6. Management and Security 
<startup> 
• Running and Startup data stores locking 
• Copy of Running  Startup 
• Copy of Startup  Running  (requires reboot) 
Base Capabilities 
:base:1.1 
 
:writable-running 
Direct writes to the <running> configuration data store. 
:startup 
Separate running and startup configuration data stores 
:rollback-on-error 
Upon error in <edit-config> operation, the processing is stopped 
and the configuration is restored to its previous state. 
Other Capabilities  
:with-defaults 
• Default-handling modes supported by the server 
• The only supported mode is “trim”. 
:notifications 
• The ability to process and send event notifications 
:interleave 
• The same NETCONF session is used for normal operations and 
for notifications 
Base Operations  
<get> 
• <get> (filter)  data 
• <get-config> (source, filter)  data 
• The only supported Filter type is “subtree”.  
• Subtree filtering: Supports namespace selection, containment 
nodes, selection nodes, and content match nodes; when a 
content match node is used, it must be a list key. 
<get-config> 
<edit-config> 
• Target 
• Default-operation 
• Test-option: Default behavior is test-then-set. 
• Error-option: stop-on-error, continue-on-error, rollback-on-error 
• Config 
<copy-config> 
•  
<delete-config> 
•  
<lock> 
•  
<unlock> 
•  
<close-session> 
•  
<kill-session> 
•  
6. Management and Security 
Additional Operations 
<get-schema> 
• per RFC 6022, schema retrieval from the server 
Miscellaneous Features 
NETCONF sessions 
Up to 10 concurrent 
AAA 
• Common NETCONF and CLI users 
• SSH does the authentication and authorization. 
Default credentials 
Username = su, Password = 1234 
NETCONF port 
indexes: 
Ethernet ports on the chassis "main/1", "main/2", etc. (instead of 
"ethernet wan1", "ethernet wan2" in CLI). 
YANG Support 
All ETX-1p features are supported with private YANG models, which are based on the CLI tree and 
commands.  
The models are organized in hierarchical order. Each private model has its defined prefix, which is used 
in the model itself and when imported by other models. 
The corresponding file names are the same as the model name with the extension “.yang”. 
Module Tree  
rad-root_ETX-1p (includes global commands – schedule) 
| 
+---rad-admin_ETX-1p 
|   | 
|   +---rad-admin-scheduler_ETX-1p 
|   | 
|   +---rad-admin-software_ETX-1p 
| 
+---rad-configure_ETX-1p (includes terminal level and fault level) 
|   | 
|   +---rad-configure-access-control_ETX-1p 
|   | 
|   +---rad-configure-bridge_ETX-1p 
|   | 
|   +---rad-configure-crypto_ETX-1p 
|   | 
|   +---rad-configure-management_ETX-1p 
|   |   | 
|   |   +---rad-configure-management-access_ETX-1p 
|   |   | 
|   |   | 
|   |   +---rad-configure-management-netconf_ETX-1p 
6. Management and Security 
|   |   | 
|   |   +---rad-configure-management-radius_ETX-1p 
|   |   | 
|   |   +---rad-configure-management-snmp_ETX-1p 
|   |   | 
|   |   +---rad-configure-management-tacacsplus_ETX-1p 
|   | 
|   +---rad-configure-port_ETX-1p 
|   |   | 
|   |   +---rad-configure-port-cellular_ETX-1p 
|   |   | 
|   |   +---rad-configure-port-ethernet_ETX-1p 
|   |   |   | 
|   |   |   +---rad-configure-port-ethernet-show_ETX-1p 
|   |   | 
|   |   |   +---rad-configure-port-ppp_ETX-1p 
|   |   | 
|   |   +---rad-configure-port-virtual_ETX-1p 
|   |   |   | 
|   |   |   +---rad-configure-port-virtual-show_ETX-1p 
|   | 
|   +---rad-configure-reporting_ETX-1p 
|   | 
|   +---rad-configure-router_ETX-1p 
|   |   | 
|   |   +---rad-configure-router-bgp_ETX-1p 
|   |   |   | 
|   |   |   +---rad-configure-router-bgp-show_ETX-1p 
|   |   | 
|   |   +---rad-configure-router-bgp-policy_ETX-1p (contains prefix-list and 
            route-map levels) 
|   |   | 
|   |   +---rad-configure-router-interface_ETX-1p 
|   |   |   | 
|   |   |   +---rad-configure-router-interface-ospf_ETX-1p 
|   |   |   | 
|   |   |   +---rad-configure-router-interface-show_ETX-1p 
|   |   | 
|   |   +---rad-configure-router-nat_ETX-1p 
|   |   | 
|   |   +---rad-configure-router-ospf_ETX-1p 
|   |   | 
|   |   +---rad-configure-router-show_ETX-1p 
|   |   | 
|   |   +---rad-configure-router-tunnel-interface_ETX-1p 
|   | 
|   +---rad-configure-system_ETX-1p 
|   |   | 
|   |   +---rad-configure-system-date-and-time_ETX-1p 
|   |   | 
|   |   +---rad-configure-system-dhcp-server_ETX-1p 
|   |   | 
6. Management and Security 
|   |   +---rad-configure-system-syslog_ETX-1p 
|   | 
|   +---rad-configure-virtualization_ETX-1p 
| 
+---rad-file_ETX-1p 
Prefixes  
No. 
Module 
Prefix 
1 
rad-root 
root 
2 
rad-admin 
admin 
3 
rad-admin-scheduler 
rad-scheduler 
4 
rad-admin-software 
software 
5 
rad-configure 
configure 
6 
rad-configure-access-control 
access-control 
7 
rad-configure-bridge 
bridge 
8 
rad-configure-crypto 
crypto 
9 
rad-configure-management 
mgmt 
10 
rad-configure-management-access 
mgmt-access 
12 
rad-configure-management-netconf 
mgmt-netconf 
13 
rad-configure-management-radius 
radius 
14 
rad-configure-management-snmp 
rad-snmp 
15 
rad-configure-management-tacacsplus 
tacacs 
16 
rad-configure-oam 
oam 
22 
rad-configure-port 
port 
23 
rad-configure-port-cellular 
cellular 
24 
rad-configure-port-ethernet 
eth 
25 
rad-configure-port-ethernet-show 
eth-show 
28 
rad-configure-port-ppp 
ppp 
30 
rad-configure-port-virtual 
virtual 
31 
rad-configure-port-virtual-show 
virtual-show 
32 
rad-configure-reporting 
reporting 
33 
rad-configure-router 
router 
6. Management and Security 
34 
rad-configure-router-bgp 
bgp 
35 
rad-configure-router-bgp-show 
bgp-show 
36 
rad-configure-router-bgp-policy 
bgp-policy 
37 
rad-configure-router-interface 
rif 
38 
rad-configure-router-interface-ospf 
rif-ospf 
39 
rad-configure-router-interface-show 
rif-show 
40 
rad-configure-router-nat 
nat 
41 
rad-configure-router-ospf 
ospf 
42 
rad-configure-router-show 
router-show 
43 
rad-configure-router-tunnel-interface 
tunnel-interface 
44 
rad-configure-system 
system 
45 
rad-configure-system-date-and-time 
tod 
46 
rad-configure-system-dhcp-server 
dhcp-server 
47 
rad-configure-system-syslog 
syslog 
48 
rad-configure-virtualization 
virt 
49 
rad-file 
file 
 
Note 
RAD recommends getting the YANG models of the actual units from the 
product’s schema, using the <get schema> NETCONF operation.  
CLI commands, not used for configuration tasks, are mapped to YANG RPCs.  
Read-only nodes (config false in YANG) are always under “show” containers. The “show” containers are 
interleaved with config true nodes, i.e. not in separate state branches. Show commands have an implicit 
“all” parameter, i.e. the entire data is provided without a filtering possibility. 
NETCONF Notifications 
Event notifications can be received over a NETCONF session by means of subscription, which serves as 
an agreement and method to receive the notifications. Subscription is bound to the session lifetime. 
Using this functionality, ETX-1p can: 
• 
Create notification subscription 
• 
Allow event filtering upon subscription creation 
6. Management and Security 
• 
Send event notifications to the NETCONF client as the events occur within the system 
• 
Support replay of locally logged notifications 
The same NETCONF session is used for both normal operations and for notifications. 
ETX-1p supports NETCONF base notifications. 
For each RAD generic alarm or event, there is a corresponding private NETCONF notification. 
ETX-1p supports masking of NETCONF notifications using common alarm module capabilities. 
To create a subscription and initiate a flow of notifications, the following message sequence is 
established between NETCONF client(C) and server(S). The subscription specifies a <startTime>, so the 
server starts by replaying logged notifications. 
 
In the following example, the subscription specifies a <startTime> and <stopTime>, so it starts by 
replaying logged notifications. Then it returns to the state of a normal command-response NETCONF 
session, after the <replayComplete> and <notificationComplete> notifications are sent, and it is 
available to process <rpc> requests. 
6. Management and Security 
 
Subscription Creation 
Only the default NETCONF event stream is supported, i.e. the stream that includes all the notifications. 
It is not possible to create other event streams. 
It is possible to create a single notification subscription per NETCONF session. 
Multiple simultaneous notification subscriptions are supported, one subscription per NETCONF session. 
Logging and Replay 
When NETCONF is enabled, usually, upon the device startup, a designated notification log is created. 
This cyclic volatile notification log is large enough to store the last 1000 notifications. The log creation 
does not depend on the subscription requests. 
Alarm acknowledgement and manual clearing of the alarm log  affect neither the notification log, nor 
the replayLogCreationTime parameter. 
6. Management and Security 
Notification transmission rate in a replay is limited to 10pps in total, for all notification subscriptions. 
Replay notifications are sent before any notification that have occurred during the replay. In other 
words, notifications are sent in ascending order of eventTime. 
Standard Notifications 
The following standard notifications are supported: 
• 
netconf-capability-change - Generated when the NETCONF server detects that the server 
capabilities have changed 
• 
netconf-session-start - Generated when a NETCONF server detects that a NETCONF session has 
started 
• 
netconf-session-end - Generated when a NETCONF server detects that a NETCONF session has 
terminated 
Standard YANG model as per RFC 6470 is supported. 
Private Notifications 
Private notifications are associated with RAD common (generic) alarms and events. When an alarm or 
event is generated, the corresponding NETCONF notification is generated as well. 
A private notification includes the following attributes: 
• 
Source ID - the name of the entity that caused the notification 
• 
Description - the compound description of the notification 
• 
Severity - severity values according to ITU-T X.733 
• 
Clear Reason - the reason for clearing the alarm (relevant only for cleared alarms) 
Notification transmission rate is limited to 10pps in total, for all notification subscriptions.  
Private notifications can be masked using the relevant reporting CLI commands, e.g. alarm-source-
attribute, mask-minimum-severity. 
Factory Defaults 
The following is the default configuration of NETCONF.  
6. Management and Security 
Parameter 
Description or value 
inactivity-timeout 
time 10 (ten minutes) 
shutdown 
NETCONF is disabled 
Configuring NETCONF Parameters 
 To configure NETCONF parameters: 
1. Navigate to configure management netconf. 
The config>mngmnt>netconf# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining NETCONF session 
inactivity timeout 
inactivity-timeout {time 
<minutes> | infinite} 
minutes: 1-60 
Disabling NETCONF 
shutdown  
Type no shutdown to enable 
NETCONF. 
Examples 
 To configure NETCONF session inactivity timeout to 15 minutes: 
config>mngmnt>netconf# inactivity-timeout time 15 
config>mngmnt>netconf# 
 To configure NETCONF session inactivity timeout to be infinite: 
config>mngmnt>netconf# inactivity-timeout infinite 
 To disable NETCONF: 
config>mngmnt>netconf# shutdown 

## 6.14 MQTT Server  *(p.372)*

6. Management and Security 
6.14 MQTT Server  
This section describes how to configure MQTT servers. 
Applicability and Scaling 
This feature is applicable to all ETX-1p devices.   
Up to two MQTT servers can be configured. 
Benefits 
This feature facilitates efficient and reliable communication between devices for use in constrained 
environments and low-bandwidth networks, enabling devices to send and receive data with minimal 
network overhead. 
Functional Description 
MQTT, which stands for Message Queuing Telemetry Transport, is a lightweight messaging protocol 
designed for use in constrained environments and low-bandwidth networks. It employs a 
publish/subscribe model, facilitating efficient and reliable communication between devices. MQTT is 
commonly used in IoT (Internet of Things) applications, enabling devices to send and receive data with 
minimal network overhead. 
MQTTS is the secured version of this protocol. 
You can open a device management channel over MQTT with the server of this level. When enabled, the 
device can be managed over MQTT by the server. Only one server can serve as a management channel. 
When configuring the MQTTS protocol, an X.509 certificate name (1-64 characters) must be provided. 
The certificate should be a device certificate, signed by a CA. It is the responsibility of the user to make 
sure that the certificate exists and is valid.  
By configuring a certificate, MQTTS mode is implied. If no certificate is configured the device works with 
MQTT. 
The MQTTS implementation only accepts peers’ certificates signed by a CA that was preconfigured as 
trusted. Therefore, you must provide the trusted CA name (1-20 characters). 
6. Management and Security 
Note: MQTTS needs a valid device certificate, the certificate (or chain of trust) of the CA that signed its 
certificate and that of the CA that signed the peer’s certificate (if it is not the same CA).  
You can also configure the user credentials for MQTT authentication (a username and password, both 
can be 1-64 characters, not configured by default). This can be done exclusively or in addition to an 
X.509 certificate (depending on whether the certificate command is configured).  
Factory Defaults 
By default, no MQTT server is defined. When an MQTT server is first defined, it is configured as shown 
below. 
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
Trusted CA is not configured 
management-channel 
no management-channel  
 
Configuring MQTT Server 
You can configure the MQTT server as follows. 
 To configure the MQTT Server: 
3. Navigate to config>system>mqtt#. 
4. Define the server config>system>mqtt>server<server-name, 1..32 characters>#. You can 
configure up to two servers in the device. 
5. At the config>system>mqtt>server <server-name> # prompt, perform the required tasks 
according to the following table.  
6. Management and Security 
Task 
Command 
Comments 
Configuring the server IP 
parameters 
address ip <ip-address> [protocol 
{ssl|tcp}] [port <port-number>] 
address url <url-string> [protocol 
{ssl|tcp}] [port <port-number>] 
no address 
<ip-address> – valid IPv4 or IPv6 
unicast address 
<url-string> - a valid URL (to be 
resolved with DNS). 
protocol – MQTT transport protocol 
(ssl or tcp) 
port – MQTT transport port 
(1..65535) 
Configuring the X.509 certificate 
for MQTTS authentication 
certificate <certificate-name> 
trusted-ca <ca-name> 
no certificate <certificate-name> 
MQTTS certificate 
<certificate-name> –  string, 1-64 
characters) 
<ca-name>– MQTTS trusted CA, 
string, 1-20 characters 
Opening a management channel 
with the server 
management-channel 
no management-channel 
 
Configuring user credentials for 
authentication with the MQTT 
server 
user name <username> password 
<password-string> [hash-2] 
no user 
<username>: 1-64 characters  
<password-string>: 1-64 characters 
hash-2 - password is hashed 
(encrypted) 
Displaying the server status 
show status  
See Viewing the MQTT Status below 
Example  
 To define the MQTT server with MQTTS and SSL protocols: 
  
configure system mqtt 
            server "1" 
                address url "lns1.rad.com" protocol ssl port 7883 
                certificate "1p" trusted-ca "CA" 
            exit 
 configure system mqtt 
            server "2" 
                address url "lns3.rad.com" protocol ssl port 5884 
                certificate "1p" trusted-ca "CA" 
                management-channel 
            exit 
 
6. Management and Security 
Configuration Errors  
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Maximum numbers of servers have 
been reached 
You can configure no more than two 
MQTT servers 
 
Maximum number of 
management-channel servers has 
been reached  
No more than one server can serve as 
a management channel 
 
Note: No valid self-certificate with 
the specified name 
 
No valid self-certificate of the 
specified name exists in the device 
Note: The command will be accepted, 
but MQTT would fail until the user 
addresses the problem 
 
Note: No such CA; it must be 
configured for MQTTS to work 
This CA does not exist 
Note: The command will be accepted, 
but MQTT would fail until the user 
addresses the problem 
 
Note: Import a valid chain of trust 
for the CA, for MQTTS to work 
The device does not have a valid chain 
of trust for the CA 
Note: The command will be accepted, 
but MQTT would fail until the user 
addresses the problem 
 
Viewing the MQTT Status  
This section explains how to display the status of the MQTT server. 
 To display MQTT status:  
configure>system>mqtt>server()# show status 
Application  
 : LORA 
Server Address/URL   : ibs-lns 
MQTT Status  
 : Connected 
 The status display provides information about: 
• 
Application served by MQTT connection: 
 
Management 

## 6.15 Public Key Infrastructure  *(p.376)*

6. Management and Security 
 
LORA (Attached to LoRa gateway) 
 
(empty) 
• 
MQTT server address / URL 
• 
MQTT module status 
 
Not configured – configuration is missing  
 
Disconnected – connection fails after ‘Connected’ state 
 
Connected – connection process succeeded 
 
Connecting – trying to connect before first “Connected” state  
• 
MQTT configuration problem (MQTT cannot start due to missing configuration) 
 
Undefined MQTT server in LoRa gateway 
 
Undefined MQTT address 
 
Undefined certificate or user 
 
There is no certificate 
6.15 Public Key Infrastructure  
ETX-1p supports X.509 standard that provides infrastructure for public key certificates. It is used in 
various applications, such as Zero Touch configuration. 
Applicability and Scaling 
This feature is applicable to all the device versions. 
The certificates supported by ETX-1p have CER format and PEM encoding. Other formats and encodings 
of certificate files should be converted to CER and PEM before you can use them in ETX-1p. 
Authentication with Certificate Authority allows secured communication over public network with off-
net Zero Touch provisioning. 
Standards Compliance 
RFC 5280   Internet X.509 Public Key Infrastructure Certificate  
6. Management and Security 
Functional Description 
The certificate is used for initial authentication when ETX-1p applies to a third-party entity to establish a 
secured tunnel or secured association (SA). When the SA (SSL, TLS) is established, it starts with a mutual 
handshake process, when each side of SA has to provide authentication (mutual authentication). It is 
secure and handy to use X.509 certificates (using RSA/ECDSA keys) during the process. When both sides 
proved their authentication, they can proceed, exchange the keys and start to encrypt the transmitted 
packets. 
A certificate signed by RAD’s CA can be provided to each device. 
There are two types of certificates to check the identity of the opposite side:  
• 
device certificate 
• 
CA server certificate 
Signing the device’s certificate is done by a private key of the CA. CA has a public key and a private key. 
The public key is located in its certificate. When the device certificate is created, it is sent to the CA 
server, which signs the certificate with its private key and returns it to the sender. At the end of the 
process, the device certificate is created that relates, for example, the serial number of the device with 
the public key of the device and all is signed in a secured way by the private key of the CA server. 
For authentication, it is enough to send the device certificate. The other side can see the public key of 
the device is related to the same device with a specific serial number. Now, it should be proved that the 
certificate is authentic. The other side should have the certificate of CA. It takes the CA certificate 
(containing the CA public key), runs it over the signature made by the private key of the CA and sees if it 
is authentic. It means that binding (serial number and the device public key) is authentic and secure. It 
can then identify the device by its public key. 
CA Configuration 
Each CA the device can work with is identified by a name (1-20 characters) provided by the user.  
You can enable auto renewal of certificates (disabled by default). When enabled, the device tries to 
renew each certificate signed by the CA, starting 60 days before expiration. A daily attempt is made if 
renewal fails, until a successful renewal.  
If the device acquires a certificate that is valid for less than 60 days, renewal starts at half the certificate 
lifetime. 
You can also enable CRL auto renewal (disabled by default). When enabled, if the device has a CRL 
imported from the CA, it tries to renew it, starting 1440 minutes before expiration. An hourly attempt is 
made if renewal fails, until a successful renewal. If the device acquires a CRL that is valid for less than 
6. Management and Security 
1440 minutes, renewal starts at half the CRL lifetime. If a CRL was downloaded on a specified port 
(contained in the HTTP URL), it will be renewed on the same port. 
If a CA is deleted, keys, certificates and CRLs obtained or signed by it are not deleted. The device may 
keep using self certificates and CRL files that were obtained from a deleted CA, but they will not be 
automatically renewed (unless the CA is reconfigured). 
If a CA IP address, URL or other property is reconfigured, certificates associated with the CA would 
remain so, as the association is through the name the user has given the CA, which is not affected by 
such configuration changes. Note though, that if a CA IP address or URL points to a different machine, 
renewals will probably fail due to invalid signature. 
Communication Protocol 
You can configure the protocol with which to communicate with the CA. The protocol can be EST or 
SCEP. 
If the protocol is EST, you must specify a certificate with which the device will communicate with the CA.  
TLS modes that do not require a certificate are not supported. Self-signed certificates, though 
technically possible, are not allowed as they are not secure.  
Working with RSA/ECDSA Key Pairs  
The device can generate a key pair (private and public).  
Private keys are protected by the TPM. 
You have to specify the key type and size, which can be as follows: 
• 
ECDSA: 256, 384 or 521. 
• 
RSA: 2048, 3072, or 4096. 
If you prefer to create your own key pair rather than trust ones created by the device, you can use the 
import command to import a key pair. In this case the key type (algorithm and length) is not specified by 
the user. The device infers it from the imported key.  
The “key” context commands are not saved in configuration and may not be executed from a 
configuration file. If the device reboots after the command was invoked and before the key pair was 
imported, you will have to rerun the command. 
Factory default and user default commands do not affect keys the device has. 
You can delete the key pair from the device. 
6. Management and Security 
This command cannot be undone and deleted keys cannot be recovered. Once the keys are deleted, the 
device cannot use them or certificates associated with them. After deleting keys, you have to perform 
several additional tasks: 
• 
Ask CA administrators to revoke certificates based on the deleted keys. A CA administrator may 
ask for the challenge password created during certificate enrollment.  
• 
Delete certificates based on the deleted keys from the device.  
• 
Reconfigure applications using the deleted keys or certificates based on them. 
Factory Defaults 
Auto renewal of certificates and CRL is disabled by default. 
By default, no RSA/ECDSA keys are defined. 
Configuring X.509 Entities  
This section describes how to manage ETX-1p certificates and keys. 
 To configure CA:  
1. Navigate to configure crypto ca <ca-name> (1-20 characters). 
2. Enter all necessary commands according to the tasks listed below. 
 
6. Management and Security 
Task 
Command 
Comments 
Configuring the CA 
address 
address {ip <ca-ip-address> | url 
<ca-url>} 
no address 
<ca-ip-address>: IPv4 or IPv6 valid unicast address 
<ca-url>: String that resolves to CA IP address, 1-
256 characters 
Default: no address 
If you configure one CA with IP address and 
another with a URL, and both point to the same 
machine, this is not prevented, from two reasons: 
1) There may be no way to resolve the URL at the 
time of configuration. 
2) The IP address associated with a URL may 
change. 
It would still be possible to work with such a 
configuration, except for corner cases. For 
example, if renew is not configured for one CA, 
and a certificate is associated with the second CA, 
it will not be renewed. 
Enabling certificate auto 
renewal 
[no] certificate-auto-renew  
Default: no certificate-auto-renew 
 
Enabling CRL auto 
renewal 
[no] crl-auto-renew   
Default: no crl-auto-renew 
Configuring the protocol 
to communicate with the 
CA 
protocol {est certificate 
<certificate-name> | scep} 
no protocol 
certificate-name – Certificate for EST TLS phase, 
1-64 characters 
- 
 To configure RSA/ECDSA keys: 
1. Navigate to configure crypto key. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Deleting key pair 
delete key-name <name> 
 
If the deleted key was active, make 
sure to: 
• Reconfigure apps using it or 
certificates based on it 
• Delete certificates based on it 
and ask the CA administrator to 
revoke them 
6. Management and Security 
Task 
Command 
Comments 
Generating a key pair 
generate key-name <name> type 
ecdsa size {256|384|521} 
[application x509] 
generate key-name <name> type 
rsa size {2048|3072|4096} 
[application x509] 
 
Importing a key pair 
import key-name <name> key-url 
<key-url> [application x509] 
The following URLs are valid: 
• tftp://<server-ip-
address>/<path-and-filename> 
• tftp://<server-
hostname>/<path-and-
filename> 
IPv6 addresses must be enclosed in 
square brackets. 
Displaying public keys 
show public-key 
 
The command prints all the public 
keys stored in the device  
 To configure public key infrastructure (PKI):  
1. Navigate to configure crypto pki.  
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Authenticating CA by 
importing CA certificate 
authenticate certificate-name 
<certificate-name> [certificate-url 
<url> [fingerprint <fingerprint>]] 
 
The certificate size is limited to 64kB 
certificate-url – CA certificate URL 
Deleting the certificate 
delete-certificate certificate-
name <certificate-name> 
 
Deleting the CRL 
delete-crl crl-name <crl-name> 
 
6. Management and Security 
Task 
Command 
Comments 
Creating CSR for 
enrollment by a CA 
enroll [certificate-folder-url 
<certificate-folder-url>] 
[certificate-name <certificate-
name>] [fingerprint <fingerprint>] 
[common-name <cn>] [locality 
<locality>] [state <state>] [email 
<email>] [organization <org>] 
[organizational-unit <ou>] 
[country <country>] [challenge-
password <password>] [serial-
number {dmi | value <serial-
number>}] 
<certificate-folder-url>: string 1-200 characters 
The following formats are valid: 
• TFTP: 
tftp://<server-ip-address>/<path> 
tftp://<server-hostname>/<path> 
• SCEP: 
http://<ca-ip-address>/<path> 
http://<ca-hostname>/<path> 
Before enrolling with SCEP, you must import the 
certificate of the signing CA (with the 
authenticate command). 
Make sure not to set every parameter-string 
value with its maximum length, keeping in mind 
that the total maximum CLI command length is up 
to 650 characters.  
6. Management and Security 
Task 
Command 
Comments 
<fingerprint>: string 1-128 characters 
 
Certificate name and fingerprint are only used by 
SCEP (other methods require them in the import 
command) 
<common-name> (string up to 64 characters) - 
CSR common name that you can specify. If it is 
not specified, the device uses the configured 
<hostname>.<IP domain name> (or <hostname> if 
the domain name is not configured) 
<locality>: string 1-128 characters 
 
<state>: string 1-128 characters 
<email>: string 1-128 characters  
<org>: string 1-64 characters describing the 
organization 
 
<ou>: string 1-32 characters describing the 
organizational unit 
<country>: ISO 3166 two-letter country code 
<password>: string 1-80 characters; this password 
is not part of the certificate; you should save it in 
a secured place, as it may be asked by the CA 
manager in the case when changes (e.g. revoking 
the certificate) are desired  
Device hardware serial number: 
• dmi (the serial number is taken from the linux 
command dmidecode -s system-serial-
number) 
• value <0-64 characters> 
Exporting CRL 
export-crl crl-name <crl-local-
name> url <destination-url> 
 
Importing certificate 
import-certificate certificate-
name <certificate-name> 
[certificate-url <url> [fingerprint 
<fingerprint-string>]] 
 
Importing CRL 
import-crl crl-name <crl-local-
name> crl-url <crl-url> 
 
6. Management and Security 
Task 
Command 
Comments 
Creating permanent self-
signed certificate 
self-sign-certificate certificate-
name <certificate-name> 
[common-name <cn>] 
 
Displaying certificates 
stored in the device 
show certificate-summary [owner 
{self|ca}] [{valid-only|invalid-
only}] 
 
Displaying a certificate by 
name 
show certificate certificate-name 
<certificate-name> 
 
 
Displaying all the CRLs in 
the device 
show crl-summary 
 
 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Maximum number of RSA keys 
was exceeded  
You tried configuring more than 
one pair of RSA keys. 
Currently, only a single pair of keys is 
supported. Delete the keys and 
generate a new pair. 
Common name (hostname.ip-
domain-name) too long 
The common name comprised 
of “hostname” and “ip-domain-
name” exceeds 64 characters. 
Specify a common name that is less than 
64 characters. 
Common name too long 
You specified a CSR common 
name that exceedes 64 
characters 
Specify a common name that is less than 
64 characters 
Maximum number of keys was 
exceeded 
You tried to generate more 
than one key pair. 
 
Illegal character; command 
aborted 
You entered a non-printable 
character. 
Repeat your input with printable 
characters only. 
File is too big; command aborted 
You tried using a larger 
certificate file. 
Use certificates which size do not 
exceed 64kB. 
Invalid certificate; command 
aborted 
You entered an invalid 
certificate. 
Enter a valid certificate. 
6. Management and Security 
Message 
Cause 
Corrective Action 
CA name cannot be resolved; 
command aborted 
CA name does not match one 
configured or received by DNS. 
Provide another CA name, check the 
path and connection to the server. 
TFTP to the CA failed; command 
aborted 
TFTP connection to CA fails. 
Check the path and connection to TFTP. 
Wrong fingerprint; command 
aborted 
The fingerprint does not match 
the one in the certificate.  
Verify the fingerprint. 
Key pair with this name already 
exists  
A key pair with the name you 
specified already exists. 
 
Key pair does not exist 
The device does not have the 
specified key pair 
 
Certificate name already exists 
A certificate of this name exists  
Specify another certificate name. 
No such certificate 
A certificate of this name does 
not exist  
 
Certificate name must be 
specified 
In case of SCEP, certificate 
name must be specified. 
 
Certificate name is only used by 
SCEP 
You specified a certificate name 
with a method other than SCEP 
 
Fingerprint is only used by SCEP 
You specified a fingerprint with 
a method other than SCEP 
 
Cannot find valid CA certificate 
that was imported with SCEP 
 
You are trying to enroll without 
a valid CA certificate that was 
imported with SCEP 
 
EST certificate may not be self 
signed 
The device has a self-signed 
certificate with the certificate-
name you specified for EST 
protocol, this is not allowed  
 
Cannot find CA certificate for 
authentication  
You are trying to enroll without 
a valid CA certificate for 
authentication 
 
Cannot find CA certificate for 
encryption 
You are trying to enroll without 
a valid CA certificate for 
encryption 
 
No such CRL  
The CRL to delete or export 
does not exist. 
 
6. Management and Security 
Message 
Cause 
Corrective Action 
CRL name already exists 
A CRL of this name already 
exists. 
Specify another CRL-name. 
CA address must be a valid 
unicast IP address 
You entered an invalid IP 
address. 
Enter a unicast IPv4 or IPv6 address. 
 
This CA is not configured 
No CA with ca-ip-address or ca-
hostname is configured 
 
Address is already configured on 
a different CA 
This ca-ip-address or ca-url is 
already configured for a 
different CA 
Note: If the user configures one 
CA with IP address and another 
with a URL, and both point to 
the same machine, this is not 
prevented 
 
URL must be tftp:// 
The URL you specified does not 
start with tftp:// 
 
URL must contain a filename and 
(optionally) a path 
The URL does not contain path-
and-filename, or ends with a /  
 
Viewing Certificates Status  
 To display the ETX-1p CA-signed or self-signed certificates: 
 
config>crypto# pki show certificate self 
 
# Certificate data: 
-----BEGIN CERTIFICATE----- 
MIIDTjCCAjYCAXgwDQYJKoZIhvcNAQELBQAwYjELMAkGA1UEBhMCSUwxEzARBgNV 
BAgMClNvbWUtU3RhdGUxDDAKBgNVBAcMA1RMVjEMMAoGA1UECgwDUkFEMRAwDgYD 
VQQLDAdDQS1URVNUMRAwDgYDVQQDDAdDQS1URVNUMB4XDTE4MDIxNDA2MTg1OFoX 
DTE5MDIxNDA2MTg1OFoweDELMAkGA1UEBhMCLi4xKTAnBgNVBAMMIDAwLTA4LUEy 
LTBELTFGLUUwLnNpdGUtMy5yYWQuY29tMQ4wDAYDVQQHDAVibGFuazEOMAwGA1UE 
CgwFYmxhbmsxDjAMBgNVBAgMBWJsYW5rMQ4wDAYDVQQLDAVibGFuazCCASIwDQYJ 
KoZIhvcNAQEBBQADggEPADCCAQoCggEBAN02nc6BV6LK9MnYlU6uKDlQMn+EdKTZ 
yycUlRoyun1sfAPDQ0PvSQOUSO4BCbheAdlAwk56aa0C2GrGfW2Va73n1Cr5deFw 
KbycCIJ6FzsNiMgc2mHt4L1qf88VUGLfKFBpgylxwMYwJ7HvYzI+jpHBV34safYI 
wXgz78Cy0um7rgBzxLMx1XQk/n+q4nPowPcjCe/OoC61yMLFj6a0HS1uUDNVyNkF 
hstN6I0AviD4ehiyz3VyAuTYElTCXcY+gH30bS0XnfQ4U3iTn7E+zw1S+3fRqdXk 
6. Management and Security 
8BS4jpbzuB+Wx3VeH9EwTnWOvlM+ZrwjEZDdPuKTG+HhsB3QDd0EFMsCAwEAATAN 
BgkqhkiG9w0BAQsFAAOCAQEAW+/1dMRK6nilOOkuJczkUQD9ea14hW+V2lFESID3 
qZwpE+0oZ8jNNNhjwhyk5ziH05hE0s2ZilA9L7eI0MPS3RYzI8wAIUAvLA0n0YqR 
wuRcDrwo68gqPPA7hPjiACyVzbQ0AWRfIqdasOz6PlQ2JHv5cqV59fhf9DV85KwI 
IdiYsmkmPmXdkAo5VBA71RlPOCbfSV9nsyagzPndADqf44GOLI1gDLPodfq+hJaP 
rn5aQG1nMNZigroDyQvsTypzBDMrA8mEOS7QvbhV6gamcyGjYbVY7o1wTUYADg0X 
c7Dc9K/+4dFEO8X4ZSWRujiIKviTwKOy1zr/+KgjrJnm7A== 
-----END CERTIFICATE----- 
 
config>crypto# pki show certificate ca 
# Certificate data: 
-----BEGIN CERTIFICATE----- 
MIIDlzCCAn+gAwIBAgIJAIgL2Jgnyb72MA0GCSqGSIb3DQEBCwUAMGIxCzAJBgNV 
BAYTAklMMRMwEQYDVQQIDApTb21lLVN0YXRlMQwwCgYDVQQHDANUTFYxDDAKBgNV 
BAoMA1JBRDEQMA4GA1UECwwHQ0EtVEVTVDEQMA4GA1UEAwwHQ0EtVEVTVDAeFw0x 
ODAxMjkxNTQ5NTlaFw0yODAxMjcxNTQ5NTlaMGIxCzAJBgNVBAYTAklMMRMwEQYD 
VQQIDApTb21lLVN0YXRlMQwwCgYDVQQHDANUTFYxDDAKBgNVBAoMA1JBRDEQMA4G 
A1UECwwHQ0EtVEVTVDEQMA4GA1UEAwwHQ0EtVEVTVDCCASIwDQYJKoZIhvcNAQEB 
BQADggEPADCCAQoCggEBAMSstTvj6PgpJsv2dRDdfOC+YK5PCHjlgIzhuzerCVvA 
Nx++3+U/DxEHHVF8mEjcSU+2ACqcQq1LVIvMwcPx5skewEDD+pEU8lkF7jnyNnI6 
MYGfMgxha1u8P73N3OJ6+TFhiRY/9s3LYkPKmIreEa8BuVi+t7kLMaygEKg9IZ8e 
mNZDl+jjWUZrXBFkGZF6OS+mf6VUzuYxWMfHUQGGaGT+AHEQaMezsjhZ8QE8xIlc 
y9crtmPl0hyQylINMdptq+7Mtdv5t3wO+RK+elfRKPVpgOiyRSnoEz250q2QHsMb 
p0ZeMYUBCLxPxF2pTXu2aeF4vvw+NWhfa6JGnqSZJ18CAwEAAaNQME4wHQYDVR0O 
BBYEFHQ3m+px3avGAnj5o7FC2cZWfOYMMB8GA1UdIwQYMBaAFHQ3m+px3avGAnj5 
o7FC2cZWfOYMMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAKbEwTTx 
32JqnirOZ6PYANrIfEwbpwUZxcqkmz4pFF6V7kK5cJAiv/O0Cj7k3zPdwRhGeMD7 
t0wZVPU29tqfZRdXHcmyY7uB1tc4Hr2FvaaEqoB4DWk2C6jgTreyNrm8GbcnLMyW 
ZxpZztX/6NU1FvY0LKKmpKOIlKIkCZn4knBcjMFlOx88eHfGnScak6Pn6DIf8SqK 
xKm3pkg1ACdWfyKpM0X5aJ29nRwjnceupGZpN7kVIuFXfR1oIligujgFpsSAczpO 
PnIZb8+dzJDevz9mm1cjJQh+djdvxkxR9rDwfuE24UTEj6tTzdrqVPSb+t2FzLYt 
EUZUQ8cBTlDym3Y= 
-----END CERTIFICATE----- 
 
 
Viewing the Public Keys  
 To display the public keys: 
config>crypto>key# generate key-name AdirKey type rsa size 4096 application x509 
*****Generating RSA 4096 keys for X.509***** 
 
config>crypto>key# 
*****Finished generating RSA 4096 keys named AdirKey for X.509***** 
 
config>crypto>key# show public-key 
 
Applications : X.509 
6. Management and Security 
Status       : Active 
Generated On : 2025-06-30 
Name         : AdirKey 
Type         : RSA  4096 
 
Public Key Data: 
-----BEGIN PUBLIC KEY----- 
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA+BTik4dIrMTKsufIQziK 
ypNVVGfIZPDR9Vhyexvk6D2sL4JvhtqhbG2Nd4/tlgY16vQNREVMCcPw/iFGo6Q2 
9ct1Jif3SnmACEpDYecBS+vPRWmdlTGNXYBdLHwaacmmoEo91UE7heoGu7H9j1RR 
5qST6HYonPLAk7TLrSBBM4jm/90bJkaizn4c7ETSIm/XsPqt2rjPO3wZZGwlH90v 
8pqgf7yPIrTl0kZ1cbpHyLML19du0NREB8msdqF6yS16imezIMXjUEDTxtJAltfw 
jzw5vTwl7vUzo9Ovv7YIYz7PDxB031+J8kBcVSD3M/4n7ZF27JHjaWxdDyPuLEcV 
qwnV2Vjq+Bi++9EpGte9hAeWH5N7OkmPiBumAktBunkMmXSgM7KmEM78KsGzid5f 
3bhXTbRnMBRuW1Caewzm69UmiSHEwqd6Y3xwQzA4Xvz0d56KLSlSgf5/7TsszVmt 
0BGt1eUfkpNXlH6DdQ36zHMXaU46AHn+qiaItDH2rRQy55YAhS9TkVtV94TBzg8W 
eu0HcXpe26sk9obNMECBDDm3yNgCwaV+ApQLNJqTYf5doeVnGc2lzXRp+8z/ojIU 
I1Zp9MYCRqwhjAexmS7aB2+TW2h0EU8UMcwtSZc9jgh315vGaSsIYc1XUvvCb3KV 
4nfEv/ImWPEAlZLOyANBNSsCAwEAAQ== 
-----END PUBLIC KEY----- 
 
The following is displayed: 
• 
Applications that use this key: 
 
SFTP Client 
 
SSH 
 
X509  
• 
Key status 
 
Active 
 
Being Generated 
 
Waiting For Activation 
• 
Date and time the key was generated at 
• 
Key name 
• 
Key type 
 
ECDSA 
 
RSA 
• 
Key size 
 
256, 384, 521 (if the key type is ECDSA) 
 
2048, 3072, 4096 (if the key type is RSA) 
• 
Key data (PEM encoded key, printed from the key file)  

## 6.16 SNMPv3 Management  *(p.389)*

6. Management and Security 
6.16 SNMPv3 Management  
Simple Network Management Protocol (SNMP) is an application layer protocol that provides a message 
format for communication between managers and agents.  
ETX-1p supports SNMPv3, the latest SNMP version to date, including SNMPv2 coexistence mode. 
SNMPv3 provides secure access to devices in the network by using authentication and data encryption. 
SNMP allows you to remotely manage multiple units from a central workstation using a network 
management system. 
SNMPv3 allows data to be collected securely from SNMP devices. Confidential information such as 
SNMP commands can thus be encrypted to prevent unauthorized parties from being able to access 
them. 
 
Note 
SNMPv1 is not supported.  
Applicability and Scaling 
This feature is applicable to all the device versions. 
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
6. Management and Security 
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
• 
RFC 3415, View-Based Access Control Model (VACM) for the Simple Network Management 
Protocol (SNMP) 
• 
RFC 3416, Update for RFC 1904 
Functional Description 
In an SNMP configuration, one or more administrative computers manage a group of hosts or devices. 
Each managed system continuously executes a software component called agent, which reports 
information via SNMP back to the managing workstations. 
Factory Defaults 
The following is the default configuration of the SNMP parameters: 
• 
SNMP engine ID set to device MAC address 
• 
View named “internet” providing access to IETF MIBs and IEEE MIBs 
• 
User named "initial", with security level no authentication and no privacy 
• 
Group for SNMPv3 named "initial": 
6. Management and Security 
 
Security levels – no authentication and no privacy, authentication and no privacy, 
authentication and privacy 
 
User – “initial” 
 
Views for read/write/notify – "internet" 
• 
Notifications with tag “unmasked” for the device traps 
Configuring SNMPv3 Parameters 
SNMPv3 provides secure SNMP access to the device by authenticating and encrypting packets 
transmitted over the network. 
The SNMPv3 manager application in RADview-EMS provides a user-friendly GUI interface to configure 
SNMPv3 parameters. If you intend to use it, you must first use the device CLI to create users with the 
required encryption method and security level, as the application can create users based only on 
existing users; the new user has the same encryption method, and the same security level or lower. The 
ETX-1p default configuration provides one standard user named “initial” with no encryption and the 
lowest security level (see Factory Defaults for details). 
A Network Management Station (NMS) relies on traps in order to display device alarms. As traps are not 
reliable, the NMS needs to be aware which traps got lost and be able to ask a device to resend them. 
This mechanism is called trap synchronization. 
NMSs (targets; such as RADview or third party) may be organized into trap sync groups in order to 
provide redundancy between these NMSs. You can define the tags and target parameters in each trap 
sync group – for example, you can define one trap sync group for critical alarms such as linkDown and 
coldStart, and another group for all other traps. 
Each trap is sent to all targets attached to the group, and therefore it is recommended to set identical 
traps masking for all group members. 
 
Note 
• 
ETX-1p supports up to ten trap synchronization groups. 
• 
A single trap synchronization group can support multiple NMS. 
• 
If you would like all NMS to receive all traps, there is no need to configure 
trap synchronization groups.  
Follow this procedure to configure SNMPv3: 
1. Set SNMP engine ID if necessary. 
2. Add users, specifying authentication protocol and privacy protocol. 
6. Management and Security 
3. Add groups, specifying security level, protocol, and views. 
4. Connect users to groups. 
5. Add notification entries with assigned traps and tags. 
6. Configure target parameter sets to be used for targets.  
7. Configure targets (SNMPv3 network management stations to which ETX-1p should send trap 
notifications), specifying target parameter sets, notification tags, and trap synchronization groups 
if applicable. 
 To configure SNMPv3 parameters via CLI: 
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
access-group <group-name> 
{  snmpv1c | snmpv2c | usm } 
{ no-auth-no-priv | auth-no-priv
 | auth-priv } 
snmp 
Entering no access-group <group-
name> {snmpv1|snmpv2c|usm} 
{no-auth-no-priv|    auth-no-
priv|auth-priv} deletes the group.  
Defining how to 
match the context 
sent in frames by 
the NMS  
context-match {exact | prefix} 
snmp>access-group 
exact – Match the entire context. 
prefix – Match the first part of the 
context.  
Note: ETX-1p automatically 
identifies the NMS context, 
therefore you can configure exact 
match. Normally prefix is used for 
devices with multiple instances. 
Setting view for 
traps 
notify-view <name> 
snmp>access-group 
See the description of the view 
command for information on how 
to limit the parts of the MIB 
hierarchy that the view can access.  
Setting view with 
read-only access  
read-view <name> 
snmp>access-group 
Setting view with 
write access  
write-view <name> 
snmp>access-group 
6. Management and Security 
Task 
Command 
Level 
Comments 
Administratively 
enabling group 
no shutdown 
snmp>access-group 
Using shutdown disables the 
group. 
Enabling bootstrap 
notification 
bootstrap-notification 
snmp 
Entering no bootstrap-notification 
disables bootstrap notification. 
Configuring 
community 
community <community-index> 
snmp 
 
Configuring name 
name <community-string> 
snmp>community 
 
Configuring 
security name 
sec-name <security-name> 
snmp>community 
 
Configuring 
transport tag 
tag <transport-tag> 
snmp>community 
This should normally be left set to 
the default value. 
Administratively 
enabling 
community 
no shutdown 
snmp>community 
Entering shutdown disables 
community. 
Notifying of 
configuration 
change 
config-change-notification 
snmp> 
Entering no config-change-
notification does  not notify of 
configuration change. 
Configuring 
notification  
notify <notify-name> 
snmp> 
 
Assigning trap to 
notification 
bind <trap-name>  
snmp>notify 
You can assign more than one trap 
to a notification, in separate 
commands. 
Assigning tag to 
notification, to be 
used to identify 
the notification 
entry when 
configuring target  
tag <tag-value> 
snmp>notify 
 
Administratively 
enabling 
notification 
no shutdown 
snmp>notify 
 
6. Management and Security 
Task 
Command 
Level 
Comments 
Configuring 
notification filter 
to define access to 
a particular part of 
the MIB hierarchy 
for trap variables 
notify-filter <name> 
<sub-tree-oid> 
snmp 
• name – Name of filter  
• sub-tree-oid – OID that defines 
the MIB subtree  
Specifying the part 
of the subtree OID 
to use in order to 
define the MIB 
subtree 
mask [<mask>] 
snmp>notify-filter 
The mask is comprised of binary 
digits (for example, the mask 1.1.1 
converts OID 1.3.6.7.8 to 1.3.6). It is 
not necessary to specify a mask if 
sub-tree-oid is the OID that should 
be used to define the MIB subtree. 
Defining whether 
traps with trap 
variables 
belonging to the 
MIB subtree are 
sent 
type {included | excluded} 
snmp>notify-filter 
• included – Traps with trap 
variables belonging to the MIB 
subtree are sent. 
• excluded – Traps with trap 
variables belonging to the MIB 
subtree are not sent. 
Administratively 
enabling 
notification filter 
no shutdown 
snmp>notify-filter 
 
Configuring 
notification filter 
profile 
notify-filter-profile 
<params-name> 
snmp 
params-name – specifies the target 
parameter set to associate with the 
profile 
Configuring 
notification filter 
profile name 
profile-name <argument> 
snmp>filter-profile 
argument – specifies notification 
filter to associate with the profile 
Administratively 
enabling 
notification filter 
profile 
no shutdown 
snmp>filter-profile 
 
Connecting 
security name to 
group (e.g. 
connecting user or 
community to 
group)  
security-to-group 
{ snmpv2c | usm } 
sec-name <security-name> 
snmp 
Using no security-to-group 
removes security-to-group entity. 
6. Management and Security 
Task 
Command 
Level 
Comments 
Specifying group to 
which to connect 
security name 
group-name <group-name> 
snmp>security-to-g
roup 
 
Administratively 
enabling 
security-to-group 
entity 
no shutdown 
snmp>security-to-g
roup 
Using shutdown disables the 
security-to-group entity. 
Setting SNMP 
engine ID, as MAC 
address, IPv4 
address, IPv6 
address, or string 
snmp-engine-id 
mac [ <mac-address> ] 
snmp-engine-id 
ipv4 [ <ip-address> ] 
snmp-engine-id 
ipv6 [ <ip-address> ] 
snmp-engine-id text <string> 
snmp 
If you use the mac option and don’t 
specify the MAC address, the SNMP 
engine ID is set to the device MAC 
address. 
If you use the ipv4 or ipv6 option 
and don’t specify the IP address, 
the SNMP engine ID is set to the 
device IP address. 
Configuring target 
(SNMPv3 network 
manager) 
target <target-name> 
snmp 
Using no target removes target.  
Specifying target 
address as IP 
address or OAM 
port 
address udp-domain 
<ip-address> 
address oam-domain 
<oam-port> 
snmp>target 
 
Assigning tag(s) to 
target (the tag(s) 
must be defined in 
notification 
entries) 
tag-list <tag> 
tag-list [ <tag> ] 
tag-list [ <tag1> 
<tag2>…<tagn> ] 
snmp>target 
If you specify more than one tag, 
you must enclose the list in quotes; 
however, if you are specifying just 
one tag, the quotes are optional. 
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
Specifying the trap 
synchronization 
group to be 
associated with 
the SNMP target 
(NMS) 
trap-sync-group <group-id>  
snmp>target 
• If the group does not exist, it is 
created. 
• Enter no trap-sync-group 
<group-id> to remove the 
manager (NMS) from the group. 
If the removed manager was 
the last to be associated with 
the trap-sync-group, the group 
is automatically deleted. 
• ETX-1p supports up to ten trap 
synchronization groups. 
Administratively 
enabling target  
no shutdown 
snmp>target 
Using shutdown disables the 
target.  
Configuring set of 
target parameters, 
to be assigned to 
target 
target-params 
<target-param-name> 
snmp 
Using no target-params removes 
target parameters. 
Specifying 
message 
processing model 
(SNMP version) to 
be used when 
generating SNMP 
messages for the 
set of target 
parameters 
message-processing-model 
{ snmpv1 |snmpv2c | snmpv3 } 
snmp>target 
 
Specifying user on 
whose behalf 
SNMP messages 
are to be 
generated for the 
set of target 
parameters 
security 
[ name <security-name> ] 
[ level { no-auth-no-priv | 
auth-no-priv  | auth-priv } ] 
snmp>target 
 
Specifying SNMP 
version to be used 
when generating 
SNMP messages 
for the set of 
target parameters 
version { snmpv1 | snmpv2c | 
usm } 
snmp>target 
Use usm for SNMPv3 version. 
6. Management and Security 
Task 
Command 
Level 
Comments 
Administratively 
enabling target 
parameters 
no shutdown 
snmp>target-
params 
Using shutdown disables target 
parameters. 
Configuring target 
parameters and 
tags for trap 
synchronization 
group  
trap-sync-group <group-id> 
snmp 
The trap synchronization group 
must be previously defined at the 
target level. 
Specifying tags in 
trap-sync-group 
tag-list <list> 
snmp>trap-sync-gr
oup 
To remove the tag list, enter: no 
tag-list. 
Specifying set of 
target parameters 
in trap-sync-group 
target-params <params-name> 
snmp>trap-sync-gr
oup 
To remove the set of target 
parameters, enter: no 
target-params <params-name>. 
Configuring user 
user <security-name> 
[md5-auth [ {des | aes128 | non
e} ] ] 
user <security-name> 
[sha-auth [ {des | aes128 | none
} ] ] 
user <security-name> 
[none-auth] 
snmp 
If you don’t specify the 
authentication method when 
creating a user, the default is MD5 
with DES privacy protocol. To 
create a user with no 
authentication, specify none-auth. 
Typing no user <security-name> 
deletes the user. 
Setting user 
authentication 
password and 
optional key for 
changes 
authentication 
[ password <password> ] 
[ key <key-change> ] 
snmp>user 
Using no authentication disables 
the authentication protocol. 
Setting user 
privacy password 
and optional key 
for changes 
privacy 
[ password <password> ] 
[ key <key-change> ] 
snmp>user 
Using no privacy disables privacy 
protocol 
Note: Password minimum length is 
10 for AES128 and 8 for DES. 
Administratively 
enabling user 
no shutdown 
snmp>user 
• You must define the 
authentication and privacy 
method before you can enable 
the user, unless the user was 
defined with no authentication 
(none-auth). 
• Using shutdown disables the 
user. 
6. Management and Security 
Task 
Command 
Level 
Comments 
Defining access to 
a particular part of 
the MIB hierarchy 
view <view-name> 
<sub-tree-oid> 
snmp 
view-name – name of view, which 
can be associated to a group as a 
notify, read, or write view 
sub-tree-oid – OID that defines the 
MIB subtree (for example 1.3.6.1 
represents the Internet hierarchy) 
Specifying the part 
of the subtree OID 
to use in order to 
define the MIB 
subtree 
mask <mask> 
snmp>view 
The mask is comprised of binary 
digits (for example, the mask 1.1.1 
converts OID 1.3.6.7.8 to 1.3.6). It is 
not necessary to specify a mask if 
sub-tree-oid is the OID that should 
be used to define the MIB subtree. 
Defining whether 
access to the MIB 
subtree is allowed  
type {included | excluded} 
snmp>view 
included – Allow access to the 
subtree. 
excluded – Do not allow access to 
the subtree. 
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
information, such 
as the number of 
times the SNMPv3 
engine has booted, 
and how long since 
the last boot 
show snmpv3 information 
snmp 
 
 To configure SNMPv3 parameters via Web GUI: 
1. Navigate to Configure>Management>SNMP. 
The config>mngmnt>snmp# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
6. Management and Security 
Note 
When you enter password parameters, they should contain at least eight 
characters 
 
 
Enabling/disabling bootstrap notification 
 
Notifying of configuration change 
 
 
Setting SNMP engine ID, as MAC address, IPv4 address, IPv6 address, or string  
Note 
If you use the mac option and don’t specify the MAC address, the SNMP 
engine ID is set to the device MAC address. 
If you use the ipv4 or ipv6 option and don’t specify the IP address, the SNMP 
engine ID is set to the device IP address. 
 
In the User dialog box, you can configure the user and specify the authentication method: 
md5-auth or sha-auth. In these cases you will also specify the privacy protocol: des, aes128 
or none]. The default is md5-auth with des privacy protocol. To create a user with no 
authentication, specify none-auth. 
 
In the Access Group dialog box you can specify SNMP version to be used when generating 
SNMP messages for the set of target parameters (snmpv1c, snmpv2c or usm ) and  specify 
the security level (no-auth-no-priv, auth-no-priv, auth-priv) 
 
In the Security To Group dialog box you can connect security name to group (e.g. connect 
user or community to group) and specify SNMP version to be used when generating SNMP 
messages for the set of target parameters (snmpv1c, snmpv2c or usm)  
 
In the Notify dialog box, you can configure notifications, assigning traps and tags to them. 
 
In the View dialog box, you can setting view for traps (read-only or write) 
Examples 
 To create an SNMPv3 user and connect it to group: 
• 
User named “MD5_priv”: 
 
Security level – MD5 authentication, DES privacy 
• 
Group named "MD5Group": 
 
All security levels 
 
Contains set of views named "internet" (from default configuration) 
exit all 
configure management snmp 
#********* Configure user MD5_priv with authentication method MD5 with DES privacy protocol 
  user MD5_priv md5-auth des 
6. Management and Security 
    privacy password MD654321 
    authentication password MD654321 
    no shutdown 
    exit 
 
#******** Configure access group MD5Group with various authentication and privacy options 
  access-group MD5Group usm no-auth-no-priv  
    context-match exact 
    read-view internet 
    write-view internet 
    notify-view internet 
    no shutdown  
    exit 
  access-group MD5Group usm auth-no-priv  
    context-match exact 
    read-view internet 
    write-view internet 
    notify-view internet 
    no shutdown  
    exit 
  access-group MD5Group usm auth-priv 
    context-match exact 
    read-view internet 
    write-view internet 
    notify-view internet 
    no shutdown  
    exit 
 
#******** Connect user MD5_priv to group MD5Group 
  security-to-group usm sec-name MD5_priv 
    group-name MD5Group 
    no shutdown 
    exit all 
save 
 To create notifications: 
• 
Notification  named “TrapPort”: 
 
Tag=“Port” 
 
Bound to ethLos, sfpRemoved 
• 
Notification  named “TrapPower”: 
 
Tag=“Power” 
 
Bound to powerDeliveryFailure, systemDeviceStartup 
exit all 
configure management snmp 
#******** Configure notification TrapPort 
    notify TrapPort 
    tag Port 
6. Management and Security 
    bind ethLos  
    bind sfpRemoved 
    no shutdown 
    exit 
 
#******** Configure notification TrapPower 
  notify TrapPower 
    tag Power 
    bind powerDeliveryFailure  
    bind systemDeviceStartup 
    no shutdown 
    exit all 
save 
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
Target parameters “TargParam1” 
 
Tag list=“Port”, “Power” 
 
IP address 192.5.4.3 
exit all 
configure management snmp 
#******** Configure target parameters TargParam1 
  target-params TargParam1 
    message-processing-model snmpv3 
    version usm 
    security name MD5_priv level auth-priv 
    no shutdown 
    exit 
 
#******** Configure target TargNMS1 
  target TargNMS1 
    target-params TargParam1 
    tag-list “port power” 
    address udp-domain 192.5.4.3 
    no shutdown 
    exit 
6. Management and Security 
 To create communities, target parameters, and target for network devices that are working with 
SNMPv1: 
• 
Community “read”: 
 
Name: “public” 
 
Security name: “v1_read” (defined in default configuration)  
• 
Community “write”: 
 
Name: “private” 
 
Security name: “v1_write” (defined in default configuration) 
• 
Community “trap”: 
 
Name: “public” 
 
Security name: “v1_trap” (defined in default configuration)  
• 
Target parameters  named “snv1”: 
 
Message processing model SNMPv1 
 
Version SNMPv1  
 
Security name: “v1_trap”  
 
Security level: no authentication and no privacy 
• 
Target named “NMSsnmpv1”: 
 
Target parameters  “snv1” 
 
Tag list=“unmasked” 
 
IP address 192.5.6.7 
exit all 
#******** Configure communities 
configure management snmp 
  snmpv3 
  community read 
    name public 
    sec-name v1_read 
    no shutdown 
    exit 
  community write 
    name private 
    sec-name v1_write 
    no shutdown 
    exit 
  community trap 
    name public 
    sec-name v1_trap 
    no shutdown 
    exit 
6. Management and Security 
 
#******** Configure target parameters 
  target-params snv1 
    message-processing-model snmpv1 
    version snmpv1 
    security name v1_trap level no-auth-no-priv 
    no shutdown 
    exit 
 
#******** Configure target 
  target NMSsnmpv1 
    target-params snv1 
    tag-list unmasked 
    address udp-domain  192.5.6.7 
    no shutdown 
    exit all 
save 
 To display SNMPv3 information: 
configure management snmp 
config>mngmnt>snmp# show snmpv3 information 
SNMPv3           : enable  
Boots            : 2          
Boots Time (sec) : 102        
EngineID         : 800000a4030020d2202416 
 To configure trap synchronization: 
• 
Trap synchronization group 1: 
 
Members NMS1 and NMS2 
 
Target parameters “TargParam1” (from previous example) 
 
Tag list=“Port”, “Power” (from previous example) 
• 
Trap synchronization group 2: 
 
Members NMS3 and NMS4 
exit all 
configure management snmp 
#******** Configure targets and trap synchronization group 
  target NMS1 
    trap-sync-group 1 
      exit 
  target NMS2 
    trap-sync-group 1 
      exit 
  target NMS3 
    trap-sync-group 2 
      exit 

## 6.17 User Access  *(p.404)*

6. Management and Security 
  target NMS4 
    trap-sync-group 2 
      exit 
    trap-sync-group 1 
      tag-list “port power” 
      target-params TargParam1 
      exit all 
save 
 To display trap synchronization configured in the above example: 
config>mngmnt>snmp# show trap-sync 
Group ID  Member 
--------------------------------------------------------------- 
1         NMS1 
1         NMS2 
2         NMS3 
2         NMS4 
6.17 User Access  
ETX-1p management software allows you to define new users, and their management and access rights.  
Applicability and Scaling 
This feature is applicable to all the versions of ETX-1p.  
Factory Defaults 
By default, the following users exist, with default password 1234: 
• 
su 
• 
oper 
• 
tech 
• 
user 
• 
netconf-su 
The default users cannot be deleted but can be disabled (shut down). 
6. Management and Security 
OTP default settings:  
• 
OTP is disabled 
• 
No phone number is configured by default 
• 
“skip-password” is not configured 
• 
“remote-access-only” is not configured 
Functional Description 
ETX-1p supports the following user access levels: 
• 
Superuser (su) can perform all the activities supported by the system, including creating new 
users, changing its and other user access levels and passwords, and deleting and disabling other 
users. 
• 
Operator (oper) can perform all the activities, including those that change configuration 
permanently. Cannot define, delete, or disable other users. 
• 
Technician (tech) can monitor the device (info, show status, show statistics). Can use commands 
that may temporarily impair services or traffic but not saved in database. 
• 
User (user) can monitor the device (info, show status, show statistics). Can use commands that 
do not impair services, affect traffic, or change configuration 
• 
Linux User (linux-user) can access and monitor the device Linux shell. This level can be accessed 
by a logged-in su. The user invoking this command undergoes re-authentication, after which 
ETX-1p opens a Linux bash shell with read-only rights. The initial ETX-1p session is suspended as 
long as the Linux shell is active. Once the Linux shell is logged off, the initial session resumes 
with ETX-1p CLI. The inactivity timeout for linux-user is inherited from the underlying su.  
• 
Netconf Superuser (netconf-su) can be used in Netconf sessions only. Can perform all the 
activities supported by the system, including creating new users, changing its and other user 
access levels and passwords, and deleting and disabling other users.  
• 
Linux Network Administrator (linux-net-admin) has rights to manage networking. 
• 
Linux Technician (linux-tech) has rights to manage virtualization, networking and processes. 
The regular, non-Linux users (oper, tech, user) cannot define, delete or disable other users, or change 
their own access levels. They are allowed to change their current passwords. All users can view all CLI 
levels. Each user can execute its allowed functionality, as well as those of lower levels. 
The Linux users do not have ETX-1p CLI, and they cannot execute any of its commands. 
6. Management and Security 
 
Caution 
Configuration changes are not saved in ETX-1p configuration files; they may 
conflict or interfere with ETX-1p and may not survive software installation.  
In addition to passwords, ETX-1p can be configured to use a more robust and secure public key user 
authentication method for SSH sessions. 
Access Policy 
The access policy allows specifying up to three user authentication methods (local, RADIUS, TACACS+). If 
an authentication method is not available, the next method is used, if applicable. 
It also defines if the Off-Net ZTP (see Off-Net Zero Touch) is used. 
Non-Linux users are authenticated by internal ETX-1p system with the methods configured in the 
auth­policy command in the management>access level (local, TACACS+, or RADIUS). 
Note 
While non-Linux users can be authenticated with TACACS+ or RADIUS, the 
Linux and Netconf-su users cannot, as they are limited to local authentication.  
By default, authentication is via the locally stored database (1st-level local). 
Password Hashing  
You can specify a user’s password as a text string or as a hashed value, that you obtain by using info 
detail to display user data. 
 
Note 
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
6. Management and Security 
SSH Authentication  
ETX-1p supports management by SSHv2, enabling user authentication using one of two methods: 
• 
Password (default) – ETX-1p has default usernames and passwords. 
• 
Public key (1024-bit RSA) – more robust and secure 
The device uses the following state-of-the-art strong SSH algorithms:  
• 
Encryption algorithms:  
 
aes-ctr-256 
 
 
aes-ctr-192 
 
 
aes-ctr-128 
 
 
aes-gcm-256 
 
 
aes-gcm-128 
 
 
chacha20-poly1305 
  
• 
Key exchange algorithms: 
 
ecdh-sha2-nistp521 
 
ecdh-sha2-nistp384 
 
ecdh-sha2-nistp256 
 
curve25519-sha256 
 
dh-group18-sha512 
 
dh-group17-sha512 
 
dh-group16-sha512 
 
dh-group15-sha512 
 
dh-group14-sha256 
 
dh-group-exchange-sha256 
• 
MAC (message authentication code) algorithms 
 
sha2-512 
 
sha2-256 
Other algorithms must not be used and will be rejected by the device if offered. 
The encryption algorithms are user-selectable. You can specify up to six algorithms using the ssh-
encryption command.  
6. Management and Security 
OTP Authentication  
The device supports the OTP (one-time password) authentication. 
One-Time Passwords (OTPs) are a key security measure in digital transactions and communications, 
ensuring multi-factor authentication (MFA) and secure delivery. OTPs are temporary, unique codes used 
for authentication, providing security by being valid for only one transaction or session. 
OTPs are delivered through various channels: 
• 
Local login – Serial port / Telnet 
• 
Remote login – SSH 
• 
External servers – RADIUS / TACACS 
OTP authentication can only be launched from non-linux sessions and applies for the non-linux users ( su 
| oper | tech | user netconf-su). It does not apply for Linux users (linux-user |  linux-net-admin | linux-
tech),  
By default, OTP authentication is performed in addition to the permanent password (which makes it a 
multifactor authentication). However, you can configure the skip-password keyword, for authenticating 
only with OTP. In this case you will receive the verification code right after you enter the username; 
otherwise, the code comes after both the user and password are entered: 
• 
skip-password is ignored for SSH sessions that are authenticated with a public key. In this case 
both public key and OTP verifications are performed.  
• 
If skip-password is enabled and the device is configured to authenticate with TACACS+ or 
RADIUS, the user will not be authenticated or authorized by an AAA server, and its level will be 
determined by the device. TACACS+ command authorization won’t work either for such a user. 
By default, OTP applies regardless of the connection method. However, using “remote-access-only” 
argument, you can set OTP not to function for connections through the console port. 
If both “skip-password” and “remote-access-only” are configured, “skip-password” applies for remote 
connections, but console connections will still require username and password authentication, since 
OTP is disabled for that port. 
Once the OTP authentication is enabled and you try to login, the device sends a verification code as part 
of the authentication process. 
OTP authentication is disabled by default. Authentication succeeds only if both the permanent password 
and the OTP are correct. 
6. Management and Security 
SMS Management  
Devices with cellular modems can be managed by SMS. The user can configure one or more numbers 
from which commands are accepted, along with the CLI level allowed for each number. The calling 
number can be (optionally) verified by a one-time code sent to it. 
 
Note 
The device phone number (MSISDN) is displayed in the show status command 
in the configure>port>cellular level. 
 
Up to 10 authorized numbers allowed to manage the device with SMS can be configured using the 
caller-id command in the configure>management>access>sms level. You can also specify the authorized 
CLI level (su, oper, tech or user), su being the default. 
Callers are independent and can send commands simultaneously. The device executes them in the order 
they were received. 
You can allow SMS management with and without authentication. If authentication is disabled, any SMS 
from a configured caller ID is respected. 
When OTP (one time password) authentication is enabled and the device receives an SMS from an 
authorized caller, it returns the following SMS, with a random 8-character password: 
 
The caller must return the password by SMS. 
If wrong password is returned or the password is not returned in 5 minutes, the command is not 
executed, and the device returns the following SMS:  
Authentication failed; the command is aborted.  
OTP authentication is disabled by default.  
 
The commands sent via SMS are the usual CLI commands, with the following characteristics: 
• 
The command must be a full path command; otherwise, it will fail. 
• 
A command may span multiple SMS messages.  
6. Management and Security 
Configuring Access Policy  
 To define the access policy: 
• 
At the config>mngmnt>access# prompt, enter the necessary commands according to the tasks 
listed below.  
Task 
Command 
Comments 
Binding the ACL to a 
management entity and 
defining the ACL direction 
access-group <acl-name> in 
[{ipv4|ipv6}] 
no access-group in {ipv4|ipv6} 
 
Specifying authentication 
method via local database or 
RADIUS/ TACACS+ servers,  
and the preferable order of 
methods 
auth-policy 1st-level {local | radius 
| tacacs+} [2nd-level {local | radius 
| tacacs+ | none}] [3rd-level {local 
| none}] 
ETX-1p first attempts 
authentication via the server 
specified by 1st-level. If the server 
does not answer the authentication 
request, then ETX-1p attempts to 
authenticate via the server 
specified by 2nd-level. If the server 
does not answer the authentication 
request, then ETX-1p attempts to 
authenticate according to 
3rd-level: 
• local – ETX-1p authenticates via 
the local database and doesn’t 
procced to any further level 
• none – No further 
authentication is done, and the 
authentication request is 
rejected. 
Notes:  
If at any time in this process, an 
authentication server rejects an 
authentication request, ETX-1p 
ends the authentication process 
and does not attempt 
authentication at the next level. 
Rejecting default login 
password 
[no] ban-default-login-password 
Logging in with the default user 
password is forbidden 
Selecting a certificate to use 
for FTPS 
ftps [certificate <certificate-name>] 
<certificate-name>: 1-64 characters 
 
6. Management and Security 
Task 
Command 
Comments 
Defining character 
combinations that may not 
be used in a login password 
login-password-black-list <banned-
string> 
no login-password-black-list 
[banned-string] 
banned-string - String not allowed 
in login password 
Possible values: 4-20 characters 
string 
Typing no login-password-black-list 
without the [banned-string] results 
in deleting all the black lists. 
Configuring requirements to 
provide a strong login 
password 
login-password-properties min-
characters <min-characters> min-
digits <min-digits> min-symbols 
<min-symbols> max-consecutive 
<max-consecutive> lifetime 
{infinite | days <number>} 
[no] login-password-properties 
min-character–Minimum number 
of characters a login password 
must contain 
min-digits–Minimum number of 
digits a login password must 
contain 
min-symbols–Minimum number of 
non-alphanumeric symbols a login 
password must contain 
max-consecutive–Maximum 
number of consecutive 
(incremental or decremental) 
alphanumeric characters a login 
password may contain 
infinite | days <number>–
Password lifetime 
Enabling/disabling REST get 
interface and selecting 
certificate to use for it 
rest-get [certificate <certificate-
name>]  
no rest-get 
<certificate-name>: 1-64 characters 
 
Configuring SMS 
management 
sms  
 
See Configuring SMS management  
Enabling/disabling/changing 
the port for SSH 
management 
 
ssh [port <tcp-port>] 
no ssh 
 
 
If SSH management is disabled, the 
device silently drops any incoming 
SSH packet. 
<tcp-port>: SSH TCP port 
Possible Values: 1-65535. 
Note: A set of numbers excluded 
from configuration are covered by 
sanity errors and not mentioned 
here.  
6. Management and Security 
Task 
Command 
Comments 
Default: 22   
Configuring the acceptable 
SSH encryption algorithms 
 
ssh-encryption {all | algorithm 
<algorithm-1> [algorithm-2] 
[algorithm-3] [algorithm-4] 
[algorithm-5] [algorithm-6]} 
All or any six of the following 
algorithms can be set: 
• aes-ctr-128 
• aes-ctr-192 
• aes-ctr-256 
• aes-gcm-256 
• aes-gcm-128 
• chacha20-poly1305 
Enabling/disabling 
virtualization REST 
management and selecting 
certificate to use for it 
virtualization-rest [certificate 
<certificate-name>] 
no virtualization-rest 
<certificate-name>: 1-64 characters 
 
Enabling/disabling web 
management and selecting 
certificate to use for it 
web [certificate <certificate-
name>] 
no web 
<certificate-name>: 1-64 characters 
 
Configuring SMS Management  
The following commands are available in the sms level, at the configure>management>access>sms#  
prompt.  
Task 
Command 
Comments 
Configuring SMS 
management 
authentication mode 
authentication {otp} 
no authentication 
[no] authentication {otp} 
Possible Values: authentication otp 
no authentication 
Default: authentication otp 
Configuring SMS 
management authorized 
caller  
caller-id <phone-number> [level 
<oper | su | tech | user>] 
no caller id <phone-number> 
 
 
phone-number – authorized caller number 
(string of up to 15 numeric characters). Phone-
number can contain digits only; it must also 
contain the country prefix (without +) 
No caller is configured by default.  
6. Management and Security 
Configuring Users  
 To add a new user: 
1. Verify that you are logged on as superuser (su). 
2. Navigate to the management context (config>mngmnt). 
3. Enter login-user, followed by a new user name if you intend to create a new user, or an existing 
name, if you intend to change previously defined user. 
 
Notes 
• 
Maximum user name length is 20 characters. 
• 
User names are not case-sensitive, that is, “user123” and “UsEr123” is the 
same name.  
• 
A linux user (linux-user, linux-net-admin or linux-tech) cannot have any of 
the following reserved names: rad, syncope, syslog, dnfv, auth, control, 
schannel, root, docker.  
• 
A linux user name cannot start with __ characters.  
4. The prompt changes to config>mngmnt>login-user<user-name>#. 
5. Enter the necessary commands according to the tasks listed in the table below. 
 
Task 
Command 
Comments 
Specifying user 
authentication method 
authentication-
method {password | 
public-key} 
Default user authentication method is 
password. ETX-1p has default usernames and 
passwords. 
If you change the authentication method of a 
user with access level su to public key, and no 
public key has been defined, you are warned 
that the super user is going to be disabled, and 
prompted to confirm the operation. 
Note: You can create a public key, by 
configuring config>mngmnt>login-user<user-
name> public-key <public-key>. Alternately, you 
can create a public key using any application 
that supports SSHv2 RSA 1024-bit key 
generation. 
OTP does not work if the user is authenticated 
with a public key.  
6. Management and Security 
Task 
Command 
Comments 
Defining a user access level 
level { su | oper | tech 
| user | linux-user | 
netconf-su | linux-net-
admin |linux-tech} 
su – superuser 
oper – operator 
tech – technician 
user – read only 
linux-user – linux read-only 
netconf-su –  Netconf superuser 
linux-net-admin –  linux network and 
virtualization administrator  
linux-tech –linux network, virtualization and 
processes technician 
If you change the user level from non-linux to 
linux (this always happens when a new user is 
created), the user password is reset to the 
default and the user state is set to “shutdown”. 
Enabling one-time 
password authentication 
otp-authentication 
phone <number> 
[skip-password] 
[remote-access-only] 
no otp-authentication 
<number> – phone number (7-15 digits, 
containing the country prefix (without +) to 
which an SMS should be sent 
skip-password – skip permanent password 
authentication  
remote-access-only – no OTP authentication on 
console port connection 
Specifying user password 
password <password> 
[hash] 
Maximum password length is as follows: 
• Non-hashed – 20 characters 
• Hashed: 
• 
40 characters for SHA1 
• 
144 characters for SHA512+SALT 
• 
103 characters for linux-user  
The use of the hash function is illustrated in the 
example below. 
Note: If you try to set a password that has been 
defined as a forbidden combination of 
characters, the password will be rejected with 
the following error message: Invalid password. 
6. Management and Security 
Task 
Command 
Comments 
Setting user public key for 
authentication 
public-key <public-
key> 
Public key configuration is relevant only for the 
public key authentication method. 
Public key format: “ ssh-rsa <space> public key 
string <space> comment “ [1..512 chars] 
Use the Base64 encoding (ASCII ‘A’ to ‘Z’, ‘a’ to 
‘z’, ‘0’ to ‘9’, ’+’, ‘/’ and ‘space’) for the public 
key configuration. 
Entering no public-key deletes the public key.  
Note: ETX-1p does not have default public keys.  
Enabling/disabling a user 
shutdown  
no shutdown 
Default users (su, oper, tech, user) can be 
disabled, but cannot be deleted. 
A Linux or Netconf user can be moved to “no 
shutdown” only if its password is different 
from the default one. 
You can delete dynamic users, including those at su level. You cannot delete default users. 
 To delete an existing user: 
• 
At the config>mngmnt# prompt, enter no login-user <user_name>. 
The specified user is deleted. 
 To view all connected users: 
• 
At the config>mngmnt# prompt, enter show users. 
A list of all connected users is displayed, showing their access level, the type of connection, and 
the IP address from which they are connected. 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
6. Management and Security 
Message 
Cause 
Corrective Action 
Too many characters 
Too little characters 
You tried to configure a 
string for a forbidden 
password containing more 
than 20 or less than 4 
characters  
Configure a string 4–20 characters 
long. 
Black list is full 
You tried to configure more 
than 100 combinations of 
forbidden passwords. 
Delete unnecessary combinations 
and configure a new one. 
min-symbols + min-digits may 
not exceed 20 
You tried to set the login-
password-properties 
command with the sum of 
min-symbols and min-digits 
greater than 20 (the 
maximum password size). 
Set other values for the min-symbols 
and min-digits parameters.  
Caller ID may be up to 15 
digits 
phone-number can contain 
digits only; it must also  
contain the country prefix 
(without +) 
 
Maximum number of callers is 
configured 
You tried to configure more 
than 10 numbers 
 
OTP is skipped if the user is 
authenticated with a public 
key 
 
OTP authentication is 
enabled but does not work, 
because you have already 
authenticated with a public 
key 
 
Cellular module is not installed 
 
You tried to configure a 
phone number on a device 
without a cellular module 
 
Phone number must be 7-15 
digits 
 
You provided an invalid 
phone number 
The phone number must be 7-15 
digits, containing the country prefix 
(without +), as defined by ITU-T E.164  
Cannot set – sd-iot module is 
active 
Bind is allowed only when 
sd-iot module is not active 
(see Configuring SD IoT).  
 
 
6. Management and Security 
Examples 
Defining Users 
 To define a new user: 
• 
User name – staff 
• 
Access level – su 
• 
Password – 1234 
exit all 
configure management 
login-user staff 
level su 
password 1234 
# Password is encrypted successfully 
no shutdown 
exit 
 To add a new user with a hashed password: 
1. Define a new user with a text password. 
2. Use info detail to display the password hash value. 
3. Define another user with the hashed password from the info detail output. 
The second user can log in with the text password defined in Step 1. 
For example, to add the following users: 
• 
User name – staff1 
• 
User password – 4222 
• 
User name – staff2 
• 
User password – hash of 4222 (user staff2 can log in with password 4222) 
exit all 
configure management 
login-user staff1 
level su 
password 4222 
# Password is encrypted successfully 
no shutdown 
exit 
 
exit all 
6. Management and Security 
configure management login-user staff1 info detail 
    level su 
    password "3fda26f8cff4123ddcad0c1bc89ed1e79977acef" hash 
    no shutdown 
 
exit all 
configure management 
login-user staff2 
level su 
password "3fda26f8cff4123ddcad0c1bc89ed1e79977acef" hash 
no shutdown 
exit 
 
exit all 
configure management login-user staff2 info detail 
    level su 
    password "3fda26f8cff4123ddcad0c1bc89ed1e79977acef" hash 
    no shutdown 
Deleting Users 
 To delete an existing user: 
1. Verify that you are logged on as superuser (su). 
2. Navigate to the management context (config>mngmnt).  
3. Enter no login-user, followed by the name of the user that you intend to delete. 
Configuring OTP via the Web Interface 
In the example below we will show how to configure OTP via the Web Interface. 
 To configure OTP via the Web Interface: 
1. From the main menu, navigate to Configure -> Management. 
2. Add a new user (in our case “noam”) and double-click on it to enter inside the User window. 
 
3. Enter the user phone number (digits only) 
6. Management and Security 
 
3. Set “OTP Authentication” to ON. 
4. In the boxes to the right of the phone number, select “skip password” and/or “remote-access-
only” if required (see description above in OTP Authentication). 
5. Click “Submit”. 
The OTP Authentication is configured. 
Viewing User Access Status 
Viewing Failed Login Attempts 
All unsuccessful user login attempts are registered and can be displayed using a show command. 
 To display the unsuccessful logging attempts: 
• 
At the config>mngmnt# prompt, enter show failed-login-attempts. 
The details of each attempt are displayed. 
Recent Failed Login Attempts 
 
Source           Attempts  First Attempt    Blocked for 
------------------------------------------------------- 
1.1.1.1          5         302 seconds ago  277 seconds 
6. Management and Security 
100.100.100.100  2         100 seconds ago  -- 
Source 
Source address of the unsuccessful login  
Attempts 
Number of failed login attempts since the source was unblocked for 
the last time 
First Attempt 
The first failed login attempt recorded from the source 
Blocked for 
Time remaining till the source will be unblocked for login 
Viewing SSH Server Information 
You can display the fingerprint of the SSH server public key. 
 To display the SSH server information: 
• 
At the config>mngmnt# prompt, enter show ssh-server fingerprint. 
The SSH fingerprint information stored on the SSH server is displayed. 
configure management 
config>mngmnt# show ssh-server fingerprint 
RSA key fingerprint is ef:ab:28:81:53:c2:a3:8d:77:0d:06:e7:89:2b:81:9c 
Viewing Users 
 To view all connected users: 
• 
At the config>mngmnt# prompt, enter show users. 
A list of all connected users is displayed, showing their access level, the type of connection, and 
the IP address from which they are connected. 
configure management 
config>mngmnt# show users 
Num       User                          Access Level  Source    IP Address 
----------------------------------------------------------------------------- 
1.        su                            Su            Terminal  0.0.0.0 
2.        su                            Su            Netconf   172.17.160.69 
3.        su                            Su            SSH       172.17.180.87    
Viewing User Information 
The details of the currently logged-in users are available in the show users-details screen.  
The screen for show users-details provides the following information: 
6. Management and Security 
User 
User name 
Level 
User access level 
Popup 
Alarm/event popup status (enabled or disabled) 
From 
Source IP address of the management session, followed by protocol 
type (serial, SSH, NETCONF) 
For (sec) 
Duration of the current management session in seconds 
 To display the user information: 
• 
In the configure>management# prompt, enter show users-details. 
configure management 
config>mngmnt# show users-details 
User:su  Level:su  Popup:Enabled 
        From:Serial  For(sec):94 
User:su  Level:su  Popup:Enabled 
        From:172.17.180.87/SSH  For(sec):13 
User:su  Level:su  Popup:Enabled 
        From:172.17.160.69/Netconf  For(sec):77 
 