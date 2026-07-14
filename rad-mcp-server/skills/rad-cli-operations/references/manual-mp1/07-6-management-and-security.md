# 6 Management and Security

*Manual `MP-1-mn_ver 2.2.pdf`, pages 216–268.*


## 6.1 Access Control List (ACL)  *(p.216)*

This chapter describes the following:   
• 
Access Control List (ACL)  
• 
Management access methods 
• 
Authentication via RADUIS and TACACs+ 
• 
Other management-related features 
Usually, initial configuration of the management parameters is performed via an ASCII terminal. Once 
the management flows and corresponding router interface have been configured, it is possible to access 
Megaplex-1 via Telnet (IPv4 only) or SNMP for operation configuration. See Preconfiguring Megaplex-1 
for SNMP Management in Chapter 3 for an example of management configuration. For details on 
configuring the router, refer to the Networking chapter. 
6.1 Access Control List (ACL)  
Access control lists are used to flexibly filter and mark incoming and management traffic.  
Standards   
Relevant sections of RFC 1812 
Benefits 
Operators use ACLs to maintain network security by preventing malicious traffic from entering the 
device. ACLs can be used to save network resources by dropping unwanted packets.  
Megaplex-1 
6. Management and Security 
When user or management data is marked via ACLs, operators can apply various traffic management 
techniques to the marked packets, such as allocating more bandwidth to a certain traffic type. 
Functional Description 
Devices featuring ACLs can flexibly filter management traffic, by denying or permitting IP packets to 
enter the host, according to the packet’s source/destination address, protocol type, or other criteria. 
ACL entries are sequentially numbered rules containing statements (Deny, Permit, or Remark) and 
conditions. Remarks are free-text ACL entries used for commenting and visually organizing ACLs. 
Packets are permitted or denied access, based on the following conditions: 
• 
IP source and destination address or address range 
• 
IP protocol 
• 
TCP port – TCP/23 (TELNET), TCP/22 (SSH) 
• 
UDP port – UDP/161 (SNMP). 
The ACL structure is illustrated in the Example section. 
If there is a need to add a rule between already existing rules with consecutive numbers, the rules can 
be interspaced to accommodate additional rules between them. For example, if you apply resequencing 
to an ACL including rules 1, 2, and 3, with an interspacing value of 30, the rule numbers will change to 
30, 60 and 90. Sequence numbers can also be set at the rule level. 
Binding Access Control Lists 
Once created, ACLs are applied (bound) to router interfaces for filtering user traffic, or to the virtual 
management entity for filtering management traffic. For the management entity and router interfaces, 
ACLs can be used in the inbound direction only. If a router interface is deleted, all associated ACLs are 
automatically detached. 
Only one IPv4 ACL is supported per router interface / management entity.  
Filtering and Marking 
Packets attempting to enter an entity to which the ACL is bound are checked against the access list rules, 
one by one. Access of matching packets is denied (packets are dropped) or permitted (packets are 
forwarded and possibly marked), as directed by the ACL statement. 
Megaplex-1 
6. Management and Security 
Packets matching a Deny statement (rule) are dropped unless permitted by a previous rule.  
Packets matching a Permit statement (rule) are permitted to access an entity unless denied by a 
previous statement. Permit statements may also set the ToS byte or Layer-2 priority of packets matching 
them.  
Packets matching a Permit statement (rule) are permitted to access an entity unless denied by a 
previous statement.  
ACL rules in Megaplex-1 are used for management. Valid rules are listed below: 
• 
The access list must not contain statements other than tcp or udp  
• 
Destination address must be ‘any’ 
• 
Source port must be ‘any’ 
• 
Destination port must be tcp/23 (telnet), tcp/22 (ssh) or udp/161 (snmp). 
When a rule match occurs, an entry is added to the event log if logging is enabled. To prevent log 
overflow, it is possible to disable logging (per rule or device) or define the minimal logging interval of 
packets matching ACL entries (per device).  
Note 
By default, logging is disabled. If you choose to enable it, the default logging 
interval is five minutes.  
Two packets matching the same rule on the same entity in the same direction are logged only if the time 
between them exceeds the logging interval.  
After a match, the rest of the rules are ignored. Packets not matching any rule are dropped. Empty ACLs 
deny access of all packets matched to them. 
Statistics 
The device collects ACL statistics per router, router interface, and  management entity. The statistic 
counters include the number of rule matches that occurred since the counters were last cleared. The 
statistic counters are cleared upon device reboot. The user may also clear ACL statistics of any entity. 
Factory Defaults 
Parameter defaults are alphabetically listed in the tables below. 
Megaplex-1 
6. Management and Security 
Topic 
Parameter 
Default Value 
Access Control 
logging minimum interval 
300 (seconds) 
Access List 
access-list type 
ipv4 
All ACL Rules 
ACL statement sequence 
Highest number in use in the ACL plus 10 
Management 
access-list direction 
in 
Deny/Permit Rule 
dscp-value 
All values are filtered. 
dst-port-range 
All values are filtered. 
icmp-code 
All values are filtered. 
icmp-type-number 
All values are filtered. 
ip-precedence-value 
All values are filtered. 
ip-protocol-number 
All values are filtered. 
log 
Disable 
sequence-number 
– 
src-port-range 
All values are filtered. 
Router 
clear-statistics access-list direction 
in  
 
icmp rate-limit unreachable 
500 
 
show access-list statistics direction 
in 
Router Interface 
access-list direction 
in  
 
clear-statistics access-list direction 
in  
 
icmp unreachable 
Enable 
 
show access-list statistics direction 
in  
Management 
access-list direction 
in 
Configuring ACL 
The ACL configuration tasks are performed at the access control, router interface, and management 
levels. 
 To configure ACL: 
1. Create an access control list. 
Megaplex-1 
6. Management and Security 
2. Add deny and permit rules to the ACL. 
3. Bind the ACL to a router interface or management entity. 
4. Configure additional ACL parameters (logging interval, ICMP Unreachable messages etc), if 
necessary. 
Access-Control-Level Tasks 
The following commands are available in the CLI access-control context: config>access-control#. The 
exception to this are the deny, permit and remark commands, which are performed in the access-
list(acl_name) context: configure>access-control>access-list(acl_name)#. 
Task 
Command 
Comments 
Creating and 
deleting an ACL 
access-list ipv4 <acl_name>  
no access-list <acl_name> 
 
Creating an ACL is performed by assigning a name 
(ipv4) and specifying the ACL IP type. The ACL 
names must be unique. 
The ACL name contains up to 80 alphanumeric 
characters. 
Adding deny 
rules to an ACL 
deny {tcp | udp} {any | <src-address> 
[/<src-prefix-length>]} [<src-port-range>] 
{any | <dst-address>[/<dst-prefix-
length>]} [<dst-port-range>] [dscp <dscp-
value> | precedence <ip-precedence-
value>]  [log] [sequence <sequence-
number>] 
deny icmp {any | <src-address> [/<src-
prefix-length>]} {any|<dst­address> 
[/<dst­prefix-length>]} [icmp-type <icmp-
type-number> [icmp­code <icmp-code-
number>]] [dscp <dscp-value> | 
precedence <ip­precedence­value>]  
[log] [sequence <sequence-number>] 
deny ip [protocol <ip-protocol-number>] 
{any | <src-address> [/<src-prefix-
length>]} {any 
|<dst­address>[/<dst­prefix-length>]} 
[dscp <dscp-value> | precedence 
<ip­precedence-value>] [log] [sequence 
<sequence­number>] 
The arguments of the deny rule vary depending 
on the protocol (TCP, UDP, ICMP, IP). The 
command is repeated three times, each protocol 
with its relevant arguments. 
DSCP and IP Precedence cannot be used 
together. 
Management-bound ACLs have the following 
configuration limitations: 
• Only TCP- or UDP-based rules can be defined. 
• The destination IP address must be any. 
• For TCP/UDP, the destination port must be 
tcp/23 (Telnet), tcp/22 (SSH) or udp/161 
(SNMP).  
• The source port must remain any (i.e. 
optional src-port-range field should not be 
configured). 
• DSCP and IP Precedence are not supported. 
Possible values for sequence:   
1–2147483648. 
log enables logging match events of the rule into 
the event log and sending SNMP traps. 
Megaplex-1 
6. Management and Security 
Task 
Command 
Comments 
Adding permit 
rules to an ACL 
permit {tcp | udp} {any | <src-
address>[/<src-prefix-length>]}  [<src-
port-range>] {any|<dst-address>[/<dst-
prefix-length>]} [<dst-port-range>] [dscp 
<dscp-value> | precedence <ip-
precedence-value>]  [set {dscp < dscp-
marking-value> | precedence <ip-
precedence-marking-value> | pbit <pbit-
marking-value>}]  [log] [sequence 
<sequence-number>] 
permit icmp {any | <src-address>[/<src-
prefix-length>]} {any | 
<dst­address>[/<dst­prefix-length>]} 
[icmp-type <icmp-type-number> 
[icmp­code <icmp-code-number>]]  
[dscp <dscp-value> | precedence 
<ip­precedence­value>] [set {dscp < 
dscp-marking-value> | precedence 
<ip­precedence-marking-value> | pbit 
<pbit-marking-value>}] [log] [sequence 
<sequence-number>] 
permit ip [protocol <ip-protocol-
number>] {any | <src-address>[/<src-
prefix-length>]} {any 
|<dst­address>[/<dst­prefix-length>]} 
[dscp <dscp-value> | precedence 
<ip­precedence-value>] [set {dscp < 
dscp-marking-value> | precedence <ip-
precedence-marking-value> | pbit <pbit-
marking-value>}] [log] [sequence 
<sequence­number>] 
The arguments of the permit rule vary depending 
on the protocol (TCP, UDP, ICMP, IP). The 
command is repeated three times, each protocol 
with its relevant arguments. 
DSCP and IP Precedence cannot be used 
together. 
Management-bound ACLs have the following 
configuration limitations: 
• Only TCP- or UDP-based rules can be defined. 
• The destination IP address must be any. 
• For TCP/UDP, the destination port must be 
tcp/23 (Telnet), tcp/22 (SSH), or udp/161 
(SNMP).  
• The source port must remain any (i.e. 
optional src-port-range field should not be 
configured). 
• DSCP and IP Precedence are not supported. 
Possible values for sequence:    
1–2147483648. 
log enables logging match events of the rule into 
the event log and sending SNMP traps. 
Adding remarks 
to an ACL 
remark <description> [sequence 
<sequence-number>] 
The description contains up 
to 255 characters. 
Reseqencing 
the rules in an 
ACL 
resequence access-list <acl-name> 
[<value>] 
Possible values for value: 1–
100000 
Removing rules 
from an ACL 
delete <sequence-number> 
Possible values for sequence-number:   
 1–2147483648. 
Megaplex-1 
6. Management and Security 
Task 
Command 
Comments 
Setting the 
logging interval 
of all ACLs 
logging access-list <value> 
no logging access-list 
Enable logging at the maximum rate of the value 
set at Access Control level. <0> is equivalent to 
no logging access-list command. 
no logging access-list disables event logging for 
all rules in the ACL. 
Router-Level Tasks 
The following commands are available in the CLI router-interface context: router(number)> 
interface(number)#. The exception to this are the show access-list summary and show access-list 
statistics commands, which can be used in the router(number) context as well. 
 
Task 
Command 
Comments 
Binding the ACL 
to a router 
interface and 
defining the 
ACL direction 
access-group <acl-name> in 
no access-group in  
 
Sending/stop 
sending ICMP 
Unreachable 
messages 
unreachables 
no unreachables 
 
Displaying ACL 
statistics 
show access-list statistics  
See Displaying Statistics below.  
Clearing ACL 
statistics 
clear-statistics access-list  
clear-statistics access-list [interface 
<router-interface>  
Router interface level 
Router level 
Displaying the 
summary of 
ACLs bound to 
router interface 
show access-list summary 
Displays ACL status at the current level 
See Displaying Status below. 
 
Megaplex-1 
6. Management and Security 
Management-Level Tasks 
The following commands are available in the CLI management context: 
configure>management>access#. 
 
Task 
Command 
Comments 
Binding the ACL to a 
management entity 
and defining the ACL 
direction 
access-group <acl-name> in  
no access-group in  
The management entity supports the ACLs only 
in the in direction. 
When binding the ACL to the management 
entity, or when adding/editing rules in an ACL 
that is bound to the management entity, the 
rules must conform to the following limitations: 
• The protocol rules must be of TCP/UDP 
type. 
• The destination address must be set to any. 
• The source port must be set to any. 
• The destination port must be tcp/23 
(Telnet), tcp/22 (SSH) or udp/161 (SNMP). 
• DSCP, IP precedence, and P-bit cannot be 
used. 
Displaying ACL 
statistics 
show access-list statistics 
See Displaying Statistics below. 
Clearing ACL statistics 
clear-statistics access-list 
 
Displaying the 
summary of ACLs 
bound to a 
management entity 
show access-list summary 
Displays ACL status at the current level 
See Displaying Status below. 
Examples 
Management ACL 
 To create management ACL: 
The example below illustrates a typical ACL applied to the incoming management traffic: 
• 
Allows SSH (TCP port 22) traffic from any source 
Megaplex-1 
6. Management and Security 
• 
Denies and logs incoming Telnet (TCP port 23) connections from any source, except for 
192.168.1.0 subnet 
access-control>access-list(mng)# 
remark Allow incoming SSH traffic 
permit tcp any any 22 
remark Allow Telnet traffic coming from 192.168.1.0 subnet 
permit tcp 192.168.1.0/24 any 23 
remark “Deny and log incoming Telnet traffic” 
deny tcp any any 23 log 
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
TCP 
192.168.1.0/24 Any 
Any 
23 
No 
30 
Deny 
TCP 
Any 
Any 
Any 
23 
Yes 
 
Router ACL 
 To create router ACLs: 
The example below illustrates two typical ACLs applied to the incoming and outgoing traffic. 
Incoming traffic ACL: 
• 
Allows TCP traffic from ports 1024 or higher 
• 
Allows and logs incoming SMTP connections to 192.168.1.100 
• 
Allows incoming pings 
access-control>access-list(permit_incoming)# 
remark Allow incoming TCP traffic from ports 1024 or higher 
permit tcp any 192.168.1.0/24 1024..65535 
remark Allow and log incoming SMTP connection to 192.168.1.100 
permit tcp any  192.168.1.100 25 log 
remark Allow incoming pings 
permit icmp any 192.168.1.0/24 
Megaplex-1 
6. Management and Security 
The table below summarizes the rules configured for the ACL. Items in red are either implied or 
unavailable for the current parameter or serve as system settings that cannot be changed. The deny rule 
appearing in the bottom row is a system rule that is used to deny all non-compliant data. 
Sequence 
Number 
Action 
Protocol 
IP Protocol 
Source IP 
TCP/UDP  
Source Port 
Dest. IP 
TCP/UDP 
Dest. Port 
ICMP 
Type 
ICMP 
Code 
ToS 
Mark 
Log 
10 
Permit 
TCP 
N/A 
Any 
Any 
192.168.1.0/24 
1024..65535 
N/A 
N/A 
Any 
– 
No 
20 
Permit 
TCP 
N/A 
Any 
Any 
192.168.1.100 
25 
N/A 
N/A 
Any 
– 
Yes 
30 
Permit 
ICMP 
N/A 
Any 
N/A 
192.168.1.0/24 
N/A 
Any 
Any 
Any 
– 
No 
Outgoing traffic ACL: 
• 
Denies Web access from 192.168.1.10, allows other traffic  
• 
Permits Web access for the other stations on the 192.168.1.0 subnet 
access-control>access-list(outgoing_rules)# 
remark Deny 192.168.1.10 web access; allow other traffic 
deny tcp 192.168.1.10/32 any 80 
permit ip 192.168.1.10/32 any 
remark Permit others on the 192.168.1.0 subnet web access 
permit tcp 192.168.1.0/24 any 80 
The table below summarizes the rules configured for the ACL. Items in red are either implied or 
unavailable for the current parameter or serve as system settings that cannot be changed. The deny rule 
appearing in the bottom row is a system rule that is used to deny all non-compliant data. 
Sequence 
Number 
Action 
Protocol 
IP Protocol 
Source IP 
TCP/UDP  
Source Port 
Dest. IP 
TCP/UDP 
Dest. Port 
ICMP 
Type 
ICMP 
Code 
ToS 
Mark 
Log 
10 
Deny 
TCP 
N/A 
192.168.1.10 
Any 
Any 
80 
N/A 
N/A 
Any 
N/A 
No 
20 
Permit 
TCP 
N/A 
192.168.1.0/24 
Any 
Any 
80 
N/A 
N/A 
Any 
– 
No 
 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Description 
Cannot execute; invalid statement 
Invalid matching rule. For example, binding the ACL with a 
rule, using a protocol other than TCP or UDP to the 
management entity. 
Cannot add statement; sequence 
number out of range 
Invalid sequence number of the rule. Allowed sequence 
number range is 1–2147483648. 
Megaplex-1 
6. Management and Security 
Message 
Description 
Cannot resequence; sequence number 
out of range 
Resequencing has failed because the ACL interspace value is 
invalid. 
Cannot clear; no such router interface 
Statistic counters cannot be cleared on the non-existing 
router interface. 
Cannot bind; no such access list 
A non-existing ACL cannot be bound to the router interface 
or the management entity. 
Cannot show; no such router interface 
Statistic counters cannot be displayed on the non-existing 
router interface. 
Cannot bind; invalid statement 
An access list with statements, which are not supported by 
the management ACL, cannot be attached to the 
management entity. 
Displaying Statistics 
The ACL statistic counters gather information on the number of rule matches registered on the ACL since 
the last reboot or counter clearing. 
Note 
All ACLs have an implied last rule that denies all packets. The device does not 
provide statistic counters for this rule. If you intend to collect statistics on the 
number of packets discarded by the default ACL mechanism, you must add the 
deny ip any any rule at the end of the ACL.  
 To display the ACL statistics (router): 
1. Navigate to the required prompt (router(number)#, router(number)> interface(number)#). 
2. Enter the show access-list statistics command as explained in the tables above. 
The following statistic information is displayed: 
IPv4 access list: block-invalid-traffic-in (in) 
Bound to: 
  Router: 1, Interface: 2  
Matches counted for: 7 seconds 
  10 deny tcp any any dscp 17 (5 matches) 
 To display the ACL statistics (management): 
• 
In the config>mngmnt>access# prompt, enter the show access-list statistics command. 
The following statistic information is displayed: 

## 6.2 Access Policy  *(p.227)*

Megaplex-1 
6. Management and Security 
IPv4 access list: MNG_port_1                (in) 
Bound to: Management 
Matches counted for: 0 days 0 hours 2 minutes 33 seconds 
--------------------------------------------------------------- 
10    permit  tcp 172.17.154.154/24  any  22  log   (0 matches) 
20    permit  tcp 172.17.154.154/24  any  23  log   (0 matches) 
30    permit  udp 172.17.154.154/24  any  161 log   (0 matches) 
6.2 Access Policy  
The access policy allows specifying up to three user authentication methods (local, RADIUS, TACACS+). If 
an authentication method is not available, the next method is used if applicable.  
Factory Defaults 
By default, authentication is via the locally stored database (1st-level local). 
Configuring Access Policy 
 To define the access policy: 
• 
At the config>mngmnt>access# prompt, enter the necessary commands according to the 
tasks listed below. 
Task 
Command 
Comments 
Specifying authentication via 
locally stored database 
auth-policy 1st-level local 
 
Megaplex-1 
6. Management and Security 
Task 
Command 
Comments 
Specifying authentication 
method preferably via TACACS+, 
then optionally local 
auth-policy 1st-level tacacs+ 
[2nd-level { local | none } ] 
If 2nd-level is set to local, 
authentication is performed via the 
TACACS server. If the TACACS server 
does not answer the authentication 
request, then Megaplex-1 
authenticates via the local database. 
.If the TACACS server rejects the 
authentication request, Megaplex-1 
ends the authentication process. 
If 2nd-level is set to none, 
authentication is performed via the 
TACACS server only. 
Specifying authentication 
method preferably via RADIUS/ 
TACACS+, then optionally 
TACACS+/ RADIUS, then 
optionally local 
auth-policy 1st-level radius 
[2nd-level tacacs+ [3rd-level {local 
| none}]] 
auth-policy 1st-level tacacs+ 
[2nd-level radius [3rd-level {local | 
none}]] 
Megaplex-1 first attempts 
authentication via the server 
specified by 1st-level. If the server 
does not answer the authentication 
request, then Megaplex-1 attempts 
to authenticate via the server 
specified by 2nd-level. If the server 
does not answer the authentication 
request, then Megaplex-1 attempts 
to authenticate according to 
3rd-level: 
• local – Megaplex-1 authenticates 
via the local database 
• none – No further authentication 
is done, and the authentication 
request is rejected. 
Note: If at any time in this process, 
an authentication server rejects an 
authentication request, Megaplex-1 
ends the authentication process and 
does not attempt authentication at 
the next level. 
 

## 6.3 Authentication via RADIUS Server  *(p.229)*

Megaplex-1 
6. Management and Security 
6.3 Authentication via RADIUS Server  
RADIUS (Remote Authentication Dial-In User Service) is an AAA (authentication, authorization and 
accounting) client/server protocol that secures networks against unauthorized access. It is used to 
authenticate users and authorize their access to the requested system or service. The RADIUS client 
communicates with the RADIUS server using a defined authentication sequence.  
Standards 
RFC 2865, Remote Authentication Dial In User Service (RADIUS)  
RFC 2618, RADIUS Authentication Client MIB 
Benefits 
The RADIUS protocol allows centralized authentication and access control, avoiding the need to 
maintain a local user data base on each device on the network. 
Functional Description 
You configure users’ authorization levels on RADIUS servers, according to the levels defined in the 
following table. Note that each user has the rights of all users below it, in addition to those explained in 
its description. In RADIUS, there is no level mapped for the oper level. 
Level 
User 
Allowed Actions 
Description 
1 
user 
Monitoring 
Commands that do not 
affect services, traffic, or 
configuration 
6 
su 
User management 
Commands that manage 
users in the database 
7 
tech 
Diagnostics 
Commands that may affect 
services and traffic, but are 
not saved in the database 
When a login attempt occurs at Megaplex-1, it submits an authentication request to the RADIUS server. 
The RADIUS server checks the database and replies with either Access Rejected or Access Accepted. 
Megaplex-1 
6. Management and Security 
Factory Defaults 
By default, no RADIUS servers are defined. When the RADIUS server is first defined, it is configured as 
shown below. 
Description 
Default Value 
IP address of server 
0.0.0.0 
Key 
Empty string 
Max number of authentication attempts 
3 
Time interval between two authentication attempts 
3 seconds 
UDP port used for authentication  
1812 
Configuring RADIUS Parameters 
Megaplex-1 provides connectivity to up to four RADIUS authentication servers. You have to specify 
access parameters such as assigning Radius server IDs, specifying the associated server IP addresses and 
the number of retries, etc. 
 To define RADIUS parameters: 
1. At the config>mngmnt>radius# prompt, type server <server-id> to specify which server to 
configure. 
The config>mngmnt>radius>server(<server-id>)# prompt is displayed. 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning an IP address to the server 
address <ip-address> 
A valid unicast IP address 
Megaplex-1 
6. Management and Security 
Task 
Command 
Comments 
Defining a non-disclosed string 
(shared secret) used to encrypt the 
user password. 
key <string> [hash] 
 
The shared secret is a secret key 
consisting of free text known to 
the client and the server for 
encryption.  
The hash keyword denotes that 
the string is hashed, rather than 
clear text; usually it is added by 
the device after hashing the clear 
text that the user enters, before 
saving it in the database. 
If you enter the password as a text 
string (1 to 80 characters), do not 
use the hash parameter. Use it 
only if you are specifying the 
password as a hashed value 
(obtained by using the info 
command to display RADIUS data). 
Defining the number of 
authentication request attempts 
retry 
<number-of-retries> 
Possible values: 0–10 
Defining timeout (in seconds) for 
response from RADIUS server 
timeout <seconds> 
Possible values: 1–5 
Defining the UDP port to be used for 
authentication  
auth-port 
<udp-port-number> 
Possible values: 1–65535 
Administratively enabling server 
no shutdown 
Type shutdown to administratively 
disable the server. 
Displaying status 
show status 
 
Viewing RADIUS Statistics 
 To display RADIUS statistics: 
• 
At the config>mngmnt>radius# prompt, enter: 
show statistics 
RADIUS statistics appear as shown below. 
config>mngmnt>radius# show statistics  
 
Server1 
Server2 
Server3 
Server4 

## 6.4 Authentication via TACACS+ Server  *(p.232)*

Megaplex-1 
6. Management and Security 
----------------------------------------------------------------------
---- 
Access Requests : 
0 
0 
0 
0 
Access Retransmits 
: 
0 
0 
0 
0 
Access Accepts : 
0 
0 
0 
0 
Access Rejects : 
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
Malformed Response 
: 
0 
0 
0 
0 
Bad Authenticators 
: 
0 
0 
0 
0 
Pending Requests 
: 
0 
0 
0 
0 
Timeouts : 
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
Packets Dropped : 
0 
0 
0 
0 
 To clear the statistics for RADIUS: 
• 
At the config>mngmnt>radius# prompt, enter: 
clear-statistics 
The RADIUS statistics are cleared. 
6.4 Authentication via TACACS+ Server  
TACACS+ (Terminal Access Controller Access Control System Plus) is a security application that provides 
access control for routers, network access servers, and other networked computing devices via one or 
more centralized servers. TACACS+ provides separate authentication, authorization, and accounting 
services. It is used to communicate between the switch and an authentication database. Because 
TACACS+ is based on TCP, implementations are typically resilient against packet loss. 
Standards 
TACACS+ Protocol Version 1.78 (IETF draft-grant-tacacs-02) 
Benefits 
The TACACS+ protocol allows centralized authentication and access control, avoiding the need to 
maintain a local user data base on each device on the network. The TACACS+ server encrypts the entire 
body of the packet but leaves a standard TACACS+ header.  
Megaplex-1 
6. Management and Security 
Factory Defaults 
By default, no TACACS+ servers are defined. When the TACACS+ server is first defined, it is configured as 
shown below. 
Parameter 
Default Value 
key 
Empty string 
retry 
1 
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
Functional Description 
TACACS+ is a protocol that provides access control for routers, network access servers and other 
networked computing devices via one or more centralized servers. TACACS+ is based on AAA model: 
• 
Authentication – The action of determining identity of a user 
• 
Authorization – The action of determining what a user is allowed to do. It can be used to 
customize the service for the particular user.  
• 
Accounting – The action of recording what a user is doing, and/or has done 
The TACACS+ client can be configured to use authentication/authorization with or without accounting 
functionality. 
When configuring users on external TACACS+ servers, see the following table to define authorization 
levels for Megaplex-1 standard users. Note that each user has the rights of all users below it, in addition 
to those explained in its description. 
Level 
User 
Allowed Actions 
Description 
3 
user 
Monitoring 
Commands that do not 
affect services, traffic, or 
configuration 
Megaplex-1 
6. Management and Security 
Level 
User 
Allowed Actions 
Description 
6 
tech 
Diagnostics 
Commands that may affect 
services and traffic, but are 
not saved in the database 
9 
oper 
Configuration 
Commands that change 
configuration parameters 
permanently 
12, 15 
su 
User management 
Commands that manage 
users in the database 
Components 
The TACACS+ remote access environment has three major components: access client, TACACS+ client, 
and TACACS+ server.  
• 
The access client is an entity which seeks the services offered by the network.  
• 
TACACS+ client, running on Megaplex-1, processes the requests from the access client and 
passes this data to TACACS+ server for authentication.  
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
Megaplex-1 supports up to five accounting groups, with up to five TACACS+ servers per group. However, 
each TACACS+ server can be bound to a single accounting group only. 
A group can be defined with its own accounting level: 
• 
Shell accounting, which logs the following events: 
 
Successful logon 
Megaplex-1 
6. Management and Security 
 
Logon failure 
 
Logoff 
 
Megaplex-1 - terminated management session 
• 
System accounting, which records system events/alarms registered in local log file 
• 
Command accounting, which logs the following events: 
 
Any shell command that was successfully executed by Megaplex-1 
 
Any level that was successfully changed in a shell 
Configuring TACACS+ Server 
Megaplex-1 provides connectivity to up to five TACACS+ authentication servers. You must specify the 
associated server IP address, key, number of retries, etc.  
Note 
If you intend to use TACACS+ for authentication, verify that TACACS+ is 
selected as level-1 authentication method (refer to the Access Policy section).  
 To configure a TACACS+ server: 
1. At the config>mngmnt>tacacsplus# prompt, type server <ip-address> to specify the server IP 
address. 
The config>mngmnt>tacacsplus>server(<ip-address>)# prompt is displayed. 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining the TCP port to be used for 
accounting  
accounting-port <port-number> 
Possible values: 1–65535 
Defining the TCP port to be used for 
authentication  
authentication-port 
<port-number> 
Possible values: 1–65535 
Binding accounting group to TACACS+ 
server 
group <string> 
no group detaches 
accounting group from 
server. 
Megaplex-1 
6. Management and Security 
Task 
Command 
Comments 
Defining a non-disclosed string (shared 
secret) used to encrypt the user 
password 
key <string> [hash] 
 
The shared secret is a 
secret key consisting of 
free text known to the 
client and the server for 
encryption.  
The hash keyword 
denotes that the string is 
hashed, rather than clear 
text; usually it is added by 
the device after hashing 
the clear text that the 
user enters, before saving 
it in the database. 
If you enter the password 
as a text string (1 to 80 
characters), do not use 
the hash parameter. Use 
it only if you are 
specifying the password 
as a hashed value 
(obtained by using the 
info command to display 
TACACS+ data). 
Defining the number of authentication 
request attempts 
retry <number-of-retries> 
Permanently set to 1 
Defining timeout (in seconds) for 
response from TACACS+ server 
timeout <seconds> 
Possible values: 1–30 
Administratively enabling server 
no shutdown 
shutdown 
administratively disables 
the server. 
Displaying statistics 
show statistics 
 
Clearing statistics 
clear-statistics 
 
Megaplex-1 
6. Management and Security 
Configuring Accounting Groups 
 To configure accounting groups: 
1. At the config>mngmnt>tacacsplus# prompt, type group <group-name> to configure an 
accounting group with the specified name.  
The config>mngmnt>tacacsplus>group(<group-name>)# prompt is displayed.  
2. To define the accounting for the group, enter:  
accounting [shell] [system] [commands] 
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
Example – Defining Server 
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
config>mngmnt>tacacsplus>server(175.18.172.150)# information detail 
Megaplex-1 
6. Management and Security 
    key "244055BF667B8F89225048C6571135EF" hash 
    retry 1 
    timeout 5 
    authentication-port 49 
    accounting-port 49 
    no group 
    no shutdown 
Example – Defining Accounting Group 
The example below illustrates the procedure for defining an accounting group. 
• 
Group name: TAC1 
• 
Accounting: Shell, system, and commands 
• 
Bound to server defined in Example – Defining Server 
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
config>mngmnt>tacacsplus>server(175.18.172.150)# info detail 
    key "244055BF667B8F89829AB8AB0FE50885" hash 
    retry 1 
    timeout 5 
    authentication-port 49 
    accounting-port 49 
    group "TAC1" 
    no shutdown 
Megaplex-1 
6. Management and Security 
Viewing TACACS+ Statistics 
 To display TACACS+ statistics: 
• 
At the config>mngmnt>tacacsplus>server(<ip-address>)# prompt, type: 
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

## 6.5 Control Port  *(p.240)*

Megaplex-1 
6. Management and Security 
 To clear TACACS+ statistics: 
• 
At the config>mngmnt>tacacsplus>server(<ip-address>)# prompt, type:  
clear-statistics 
TACACS+ statistic counters are set to 0. 
6.5 Control Port  
You can configure the serial port parameters, which include specifying the data rate, security timeout, 
and screen size from which you are accessing the device. You can also disable management via the 
console serial port.  
Factory Defaults 
By default, data rate is set to 9600 bps. 
Configuring Control Port Parameters 
 To define the control port parameters:  
• 
At the config>terminal# prompt, enter the necessary commands according to the tasks listed 
below. 
Task 
Command 
Comments 
Specifying the desired data 
rate 
baud-rate { 9600bps | 19200bps | 
38400bps | 57800bps | 115200bps 
The default data rate is 9,600 bps. 
 
Defining whether in case of 
inactivity, device remains 
connected or disconnects after 
a specified time period 
timeout forever 
timeout limited <minutes> 
If you define a timeout, the 
timeout value can be 0–60. The 
default is 10 minutes. 

## 6.6 Management Access Methods  *(p.241)*

Megaplex-1 
6. Management and Security 
Task 
Command 
Comments 
Disabling the control port  
serial-port-disable 
no serial-port-enable (default)  
Once this command is issued, 
console access is denied for normal 
operation. Access is allowed only 
during boot process. 
Management connectivity can be 
resumed in one of the following 
ways: 
• Entering no serial-port-enable 
command via remote access 
(Inband or OOB via Telnet, 
SNMP). 
• Setting to default configuration, 
by pressing the external push 
button on the front panel.  
Specifying the number of rows 
to display 
length <number-of-rows> 
The number of rows can be 0, to 
indicate no limit on the number of 
lines displayed, or 20. 
6.6 Management Access Methods  
You can enable or disable access to the Megaplex-1 management system via Telnet (IPv4 only), SSH, or 
SNMP applications. By disabling Telnet, SSH, or SNMP, you prevent unauthorized access to the system 
when security of the Megaplex-1 IP address has been compromised. When Telnet, SSH, and SNMP are 
disabled, Megaplex-1 can be managed via an ASCII terminal only. Additionally, you can enable or disable 
file transfer via SFTP/TFTP. 
Functional Description 
The Megaplex-1 host is an IP address of a router interface. Two types of Megaplex-1 management 
access are supported: 
• 
Inband – Megaplex-1 host (management RI) resides directly on a VLAN over a Bridge.  
 
Megaplex-1 
6. Management and Security 
Router
Bridge
NNI
NNI
Bridge Port
MNG RI 
(Megaplex-1 
Host)
GbE port 1
GbE port 2
UNI
Fast Ethernet 
port
 
Megaplex-1 Host over Bridge  
• 
Out-of-band (OOB) – MNG access via OOB port is supported to access the device host both 
directly and over VLAN Bridge domain.  
 
Router
MNG RI 
(Megaplex-1  Host)
OOB 
Manage-
ment Port
 
Megaplex-1 Host over OOB Port 
Factory Defaults   
By default, access is enabled for all the applications. 
In the default factory configuration, Megaplex-1 allows management from the OOB management port.  
The default factory configuration includes the following:  
Megaplex-1 
6. Management and Security 
• 
Allows untagged management access from the OOB port  
• 
Default IP address of the Router Interface is 169.254.1.1/16 
• 
No default Gateway configuration 
• 
Allows local management access using a PC to an ‘out of the box’ Megaplex-1 device: 
 
When PC uses DHCP, access to Megaplex-1 device is automatically established (PC address 
defaults to 169.254.x.y as no DHCP server  Microsoft protocol). 
 
This configuration can be deleted by the user. 
• 
Includes flows to and from an SVI Router (1) and a Router Interface (1) with a fixed and set IP 
address (direct, not via bridge). 
• 
SVI, RI, and flow are assigned with reserved flow name (mng_access_default) and the following 
indexes: 
 
SVI #: 1 (lowest valid SVI index) 
 
RI #: 1 (lowest valid RI number)   
• 
Not backward compatible to user configuration CLI scripts that configure OOB port 
Router
MNG RI 
(Megaplex-1 Host)
SVI
OOB
MNG
Port
Untagged
Untagged
 
The factory default configuration is only loaded if there is no startup-config or user-default-config (for 
example, after executing the factory-default command).  
If you copy a script and paste it to the terminal after factory-default-config is loaded, it is important to 
verify that the configuration in the script does not conflict with the factory default configuration. 
You can delete the factory default configuration. You can also replace the factory-default with a 
download of a fresh startup-config, by performing Reset. 
You can add an additional IP address over the RI to allow remote access. 
When accessing remotely, it is possible to delete the local IP 169.254.1.1/16. 

## 6.7 RSA Key Generation  *(p.244)*

Megaplex-1 
6. Management and Security 
Configuring Management Access 
This section describes how to configure general management parameters.  
Note 
There is no explicit configuration for inband and outband management 
access.  
 To configure management access: 
• 
At the configure management access prompt enter the necessary commands according to the 
tasks listed below. 
Task 
Command 
Comments 
Allowing SFTP access 
sftp 
Typing no sftp blocks access by SFTP. 
Allowing SSH (Secure Shell) access 
ssh 
Typing no ssh blocks access by SSH. 
Allowing SNMP access 
snmp 
Typing no snmp blocks access by 
SNMP. 
Allowing Telnet access (for IPv4 only) 
telnet 
Typing no telnet blocks access by 
Telnet. 
Allowing TFTP access 
tftp 
Typing no tftp blocks access by TFTP. 
6.7 RSA Key Generation  
Megaplex-1 features generating an RSA key of a configurable key size: 1024 or 2048. 
Applicability and Scaling 
This feature is applicable to all Megaplex-1 models.  
Functional Description 
In cases where a device does not have an RSA key, the SW automatically generates an RSA key. 
When a device is upgraded to a new version, it keeps its old key, and therefore does not generate a new 
key automatically.  
Megaplex-1 
6. Management and Security 
Megaplex-1 supports the generate-rsa command for users who prefer to generate their own RSA key 
pair. Or for customers who are using a RAD device that comes with a 1024-long key and would like to 
upgrade to a more secure 2048-long key.  
When upgrading an RSA key using this command, the SW deletes the existing RSA key and reboots the 
device. The SW keeps the timestamp from when the generate-rsa command was executed, so it will be 
available following reboot. This timestamp is displayed when you run the show my-public-rsa-key 
command to display the public RSA key information. 
Configuring RSA Key Generation 
 To configure an RSA key pair: 
1. Navigate to configure>crypto>key. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Generating the RSA key 
generate-rsa [size <key-size>] 
application <application-name> 
• key-size – RSA key size (in 
bits) 
Possible values: 1024, 2048 
Default: 2048 
• application-name – 
application(s) that use this 
RSA key 
Possible values: ssh 
Default value: ssh  
Note: The device requests 
approval to execute the 
command: 
The device will delete the 
existing key, reboot, and create 
the new key. 
Continue (the device will reboot 
immediately)? 
Showing the RSA key 
show my-public-rsa-key 
See Viewing the RSA Key. 
Configuration Errors 
The following table lists the messages generated by the device when an error is detected. 
Megaplex-1 
6. Management and Security 
Message 
Cause 
Corrective Action 
Maximum number of 
RSA keys was exceeded. 
You tried to generate more than one RSA 
key. 
 
Viewing the RSA Key  
You can display the generated public RSA key information, including the timestamp in which the RSA key 
was generated. 
 To display the RSA key information: 
• 
At the configure>crypto>key # prompt, enter show my-public-rsa-key. 
MP-1>config>crypto>key# show my-public-key-rsa 
 
Generated at : 08-01-2000 06:44:11 UTC 
Name         : RAD.MP1.ssh_key 
Size         : 1024 
Application  : SSH 
 
8BB81A0E298872637B5A724A816D9426AB0D1426DDF16D76F63873032A506307061093A16F66DA18 
5F6E9F2B7BAED39F73EFCFF16FC48AD7D85F85F8E7A3801AC04C0D772E3690298804363859F5A51D 
EC9A154C92D170AC4E5A488A12204BEEC23541BD4935520DA57BD1D3AD56ED3600A1FF7213F2407C 
8CB0E8C917A60B97CCA0901293B53D0BA758CE78A070A29DBF6BE143D864FBEB74EE73364A4D021B 
5CB0E3ACE6562D98BF1B0FEFE4A9D1A1394FC422709BC2A4D5517CB6B47FF1ED22D35E079026DB0F 
75415ADF66A5314C54883FDEE010FC4D6CC30F675DB12D8AB4CEE5C3BB642C01E2DA68F2152C0258 
4A3370FE3C4FFC27DC0B313579FACC4099263ACF45841A2E456E76DDD8AAC9E49B57752374A5F923 
0A91D22C67BCD5E0E2BC3C50B5C5A4379A2B6AD6FA4FDA29BAE620A934A44CC366E6AC32E2AC53D1 
C0048F564C60E38A71A70D1EAD8D8D4D2FC4038A4FEE6C926FEFAD37BD1F2558A5F0507544F50196 
F1029FB0BE16F8C72F5AD5FD608BB6D2AEA7B98E8F3572836181967D09EE774B0D7AB6294AF7BF21 
86D2957EC149C699F18947E3822531809EE3410E9DADD1660A3F2B29E2F5AEA5F591F167EDA9823B 
45F9A775B946819CD9FB54A3BE3AD0E5F02AE3AD90CB463A6FEE3993E13D2C38B3C8E4DC2AE1B477 
3FA3A0518962CC9CDAE8E66B3ED694FA 

## 6.8 SNMP Management  *(p.247)*

Megaplex-1 
6. Management and Security 
Note 
In the above example, the time that the RSA key is generated is not available, 
and therefore a not valid time is displayed. 
Time information is not available in the following two cases: 
• 
On a new device, when SW is loaded and run on it for the first time. In this 
case, the device automatically generates the RSA key, and as NTP is not 
locked, there is no valid time available. In this case, the time displayed in 
the output is as follows: Generated at: 01-01-1970  
• 
When upgrading from an older version. In this case, the RSA key exists and 
is therefore not generated automatically. However, the time information 
is not available, as older versions do not support it. As a result, following 
upgrade, the time displayed is all zeros, and the output is as follows:  
Generated at: 00-00-0000 00:00:00 UTC 
6.8 SNMP Management  
Simple Network Management Protocol (SNMP) is an application layer protocol that provides a message 
format for communication between managers and agents.  
Megaplex-1 supports SNMPv3, the latest SNMP version to date. SNMPv3 provides secure access to 
devices in the network by using authentication and data encryption. 
Standards 
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
Megaplex-1 
6. Management and Security 
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
• 
RFC 3415, View-Based Access Control Model (VACM) for the Simple Network Management 
Protocol (SNMP) 
• 
RFC 3416, Update for RFC 1904 
Benefits  
SNMP allows you to remotely manage multiple units from a central workstation using a network 
management system. 
SNMPv3 allows data to be collected securely from SNMP devices. Confidential information such as 
SNMP commands can thus be encrypted to prevent unauthorized parties from being able to access 
them. 
Functional Description 
In an SNMP configuration, one or more administrative computers manage a group of hosts or devices. 
Each managed system continuously executes a software component called agent, which reports 
information via SNMP back to the managing workstations. 
Megaplex-1 
6. Management and Security 
Factory Defaults 
The following is the default configuration of the SNMP parameters (see Configuring SNMPv3 
Parameters for explanations of the parameters): 
• 
SNMP engine ID set to device MAC address 
• 
View named “internet” providing access to IETF MIBs and IEEE MIBs 
• 
User named "initial", with security level no authentication and no privacy 
• 
Group for SNMPv3 named "initial": 
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
SNMP version 3, provides secure SNMP access to the device by authenticating and encrypting packets 
transmitted over the network. 
The SNMPv3 manager application in RADview-EMS provides a user-friendly GUI interface to configure 
SNMPv3 parameters. If you intend to use it, you must first use the device CLI to create users with the 
required encryption method and security level, as the application can create users based only on 
existing users; the new user has the same encryption method, and the same security level or lower. The 
Megaplex-1 default configuration provides one standard user named “initial” with no encryption and 
the lowest security level (see Factory Defaults for details). 
A Network Management Station (NMS) relies on traps in order to display device alarms. As traps are not 
reliable, the NMS needs to be aware which traps got lost and be able to ask a device to resend them. 
This mechanism is called trap synchronization. 
NMSs (targets; such as RADview or third party) may be organized into trap sync groups in order to 
provide redundancy between these NMSs. You can define the tags and target parameters in each trap 
sync group – for example, you can define one trap sync group for critical alarms such as linkDown and 
coldStart, and another group for all other traps. 
Each trap is sent to all targets attached to the group, and therefore it is recommended to set identical 
traps masking for all group members. 
Megaplex-1 
6. Management and Security 
Note 
• 
Megaplex-1 supports up to two trap synchronization groups. 
• 
A single trap synchronization group can support multiple NMS. 
• 
If you would like all NMS to receive all traps, there is no need to configure 
trap synchronization groups.  
Follow this procedure to configure SNMPv3: 
1. Set SNMP engine ID if necessary. 
2. Add users, specifying authentication protocol and privacy protocol. 
3. Add groups, specifying security level, protocol, and views. 
4. Connect users to groups. 
5. Add notification entries with assigned traps and tags. 
6. Configure target parameter sets to be used for targets.  
7. Configure targets (SNMPv3 network management stations to which Megaplex-1 should send 
trap notifications), specifying target parameter sets, notification tags, and trap synchronization 
groups if applicable. 
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
access-group <group-
name> 
{ snmpv2c | usm } 
{ no-auth-no-priv | auth-
no-priv | auth-priv } 
snmp 
Using no access-group 
deletes the group.  
Megaplex-1 
6. Management and Security 
Task 
Command 
Level 
Comments 
Defining how to match the 
context sent in frames by the 
NMS  
context-match {exact | 
prefix} 
snmp>access-grou
p 
exact – Match the entire 
context. 
prefix – Match the first 
part of the context.  
Note: Megaplex-1 
automatically identifies 
the NMS context, 
therefore you can 
configure exact match. 
Normally prefix is used for 
devices with multiple 
instances. 
Setting view for traps 
notify-view <name> 
snmp>access-grou
p 
See the description of the 
view command for 
information on how to 
limit the parts of the MIB 
hierarchy that the view 
can access.  
Setting view with read-only 
access  
read-view <name> 
snmp>access-grou
p 
Setting view with write access  
write-view <name> 
snmp>access-grou
p 
Administratively enabling 
group 
no shutdown 
snmp>access-grou
p 
Using shutdown disables 
the group. 
Configuring community 
community <community-
index> 
snmp 
 
Configuring name 
name <community-string
> 
snmp>community 
 
Configuring security name 
sec-name <security-nam
e> 
snmp>community 
 
Configuring transport tag 
tag <transport-tag> 
snmp>community 
This should normally be 
left set to the default 
value. 
Administratively enabling 
community 
no shutdown 
snmp>community 
Using shutdown disables 
community. 
Configuring notification  
notify <notify-name> 
snmp> 
 
Assigning trap to notification 
bind <trap-name>  
snmp>notify 
You can assign more than 
one trap to a notification, 
in separate commands. 
Megaplex-1 
6. Management and Security 
Task 
Command 
Level 
Comments 
Assigning tag to notification, to 
be used to identify the 
notification entry when 
configuring target  
tag <tag-value> 
snmp>notify 
 
Administratively enabling 
notification 
no shutdown 
snmp>notify 
 
Configuring notification filter 
to define access to a particular 
part of the MIB hierarchy for 
trap variables 
notify-filter <name> 
<sub-tree-oid> 
snmp 
• name – Name of filter  
• sub-tree-oid – OID that 
defines the MIB 
subtree  
Specifying the part of the 
subtree OID to use in order to 
define the MIB subtree 
mask [<mask>] 
snmp>notify-filter 
The mask is comprised of 
binary digits (for example, 
the mask 1.1.1 converts 
OID 1.3.6.7.8 to 1.3.6). It is 
not necessary to specify a 
mask if sub-tree-oid is the 
OID that should be used to 
define the MIB subtree. 
Defining whether traps with 
trap variables belonging to the 
MIB subtree are sent 
type {included | 
excluded} 
snmp>notify-filter 
• included – Traps with 
trap variables 
belonging to the MIB 
subtree are sent. 
• excluded – Traps with 
trap variables 
belonging to the MIB 
subtree are not sent. 
Administratively enabling 
notification filter 
no shutdown 
snmp>notify-filter 
 
Configuring notification filter 
profile 
notify-filter-profile 
<params-name> 
snmp 
params-name – specifies 
the target parameter set 
to associate with the 
profile 
Configuring notification filter 
profile name 
profile-name 
<argument> 
snmp>filter-profile 
argument – specifies 
notification filter to 
associate with the profile 
Administratively enabling 
notification filter profile 
no shutdown 
snmp>filter-profile 
 
Megaplex-1 
6. Management and Security 
Task 
Command 
Level 
Comments 
Connecting security name to 
group (e.g. connecting user or 
community to group)  
security-to-group 
{ snmpv2c | usm } 
sec-name <security-nam
e> 
snmp 
Using 
no security-to-group 
removes security-to-group 
entity. 
Specifying group to which to 
connect security name 
group-name 
<group-name> 
snmp>security-to-g
roup 
 
Administratively enabling 
security-to-group entity 
no shutdown 
snmp>security-to-g
roup 
Using shutdown disables 
the security-to-group 
entity. 
Setting SNMP engine ID, as 
MAC address or IP address or 
string 
snmp-engine-id 
mac [ <mac-address> ] 
snmp-engine-id 
ipv4 [ <ip-address> ] 
snmp-engine-id 
text <string> 
snmp 
If you use the mac option 
and don’t specify the MAC 
address, the SNMP engine 
ID is set to the device MAC 
address. 
If you use the ipv4 option 
and don’t specify the IP 
address, the SNMP engine 
ID is set to the device IP 
address. 
Configuring target (SNMPv3 
network manager) 
target <target-name> 
snmp 
Using no target removes 
target.  
Specifying target address as IP 
address or OAM port 
address udp-domain 
<ip-address> 
address oam-domain 
<oam-port> 
snmp>target 
 
Assigning tag(s) to target (the 
tag(s) must be defined in 
notification entries) 
tag-list <tag> 
tag-list [ <tag> ] 
tag-list [ <tag1> 
<tag2>…<tagn> ] 
snmp>target 
If you specify more than 
one tag, you must enclose 
the list in quotes; 
however, if you are 
specifying just one tag, the 
quotes are optional. 
Specifying set of target 
parameters for target 
target-params 
<params-name> 
snmp>target 
 
Megaplex-1 
6. Management and Security 
Task 
Command 
Level 
Comments 
Specifying the trap 
synchronization group to be 
associated with the SNMP 
target (NMS) 
trap-sync-group 
<group-id>  
snmp>target 
• If the group does not 
exist, it is created. 
• Enter no 
trap-sync-group 
<group-id> to remove 
the manager (NMS) 
from the group. If the 
removed manager was 
the last to be 
associated with the 
trap-sync-group, the 
group is automatically 
deleted. 
• Megaplex-1 supports 
up to two trap 
synchronization 
groups. 
Administratively enabling 
target  
no shutdown 
snmp>target 
Using shutdown disables 
the target.  
Configuring set of target 
parameters, to be assigned to 
target 
target-params 
<target-param-name> 
snmp 
Using no target-params 
removes target 
parameters. 
Specifying message processing 
model (SNMP version) to be 
used when generating SNMP 
messages for the set of target 
parameters 
message-processing-mo
del 
{ snmpv2c | snmpv3 } 
snmp>target 
 
Specifying user on whose 
behalf SNMP messages are to 
be generated for the set of 
target parameters 
security 
[ name <security-name> 
] 
[ level { no-auth-no-priv 
| 
auth-no-priv  | auth-priv
 } ] 
snmp>target 
 
Specifying SNMP version to be 
used when generating SNMP 
messages for the set of target 
parameters 
version { snmpv2c | 
usm } 
snmp>target 
Use usm for SNMPv3 
version. 
Megaplex-1 
6. Management and Security 
Task 
Command 
Level 
Comments 
Administratively enabling 
target parameters 
no shutdown 
snmp>target 
Using shutdown disables 
target parameters. 
Configuring target parameters 
and tags for trap 
synchronization group  
trap-sync-group 
<group-id> 
snmp 
The trap synchronization 
group must be previously 
defined at the target level. 
Specifying tags in trap-sync-
group 
tag-list <list> 
snmp>trap-sync-gr
oup 
To remove the tag list, 
enter: no tag-list. 
Specifying set of target 
parameters in trap-sync-group 
target-params 
<params-name> 
snmp>trap-sync-gr
oup 
To remove the set of 
target parameters, enter: 
no target-params 
<params-name>. 
Configuring user 
user <security-name> 
[md5-auth [ {des | aes12
8 | none} ] ] 
user <security-name> 
[sha-auth [ {des | aes128
 | none} ] ] 
user <security-name> 
[none-auth] 
snmp 
If you don’t specify the 
authentication method 
when creating a user, the 
default is MD5 with DES 
privacy protocol. To create 
a user with no 
authentication, specify 
none-auth. 
Typing 
no user <security-name> 
deletes the user. 
Setting user authentication 
password and optional key for 
changes 
authentication 
[ password <password> ] 
[ key <key-change> ] 
snmp>user 
Using no authentication 
disables the 
authentication protocol. 
Note: Password minimum 
length is 8 characters. The 
maximum password 
length is 76 characters. 
Setting user privacy password 
and optional key for changes 
privacy 
[ password <password> ] 
[ key <key-change> ] 
snmp>user 
 
Using no privacy disables 
privacy protocol 
Note: Password minimum 
length is 10 for AES128 
and 8 for DES. The 
maximum password 
length is 76 characters. 
Megaplex-1 
6. Management and Security 
Task 
Command 
Level 
Comments 
Administratively enabling user 
no shutdown 
snmp>user 
• You must define the 
authentication and 
privacy method before 
you can enable the 
user, unless the user 
was defined with no 
authentication 
(none-auth). 
• Using shutdown 
disables the user. 
Defining access to a particular 
part of the MIB hierarchy 
view <view-name> 
<sub-tree-oid> 
snmp 
view-name – name of 
view, which can be 
associated to a group as a 
notify, read, or write view 
sub-tree-oid – OID that 
defines the MIB subtree 
(for example 1.3.6.1 
represents the Internet 
hierarchy) 
Specifying the part of the 
subtree OID to use in order to 
define the MIB subtree 
mask <mask> 
snmp>view 
The mask is comprised of 
binary digits (for example, 
the mask 1.1.1 converts 
OID 1.3.6.7.8 to 1.3.6). It is 
not necessary to specify a 
mask if sub-tree-oid is the 
OID that should be used to 
define the MIB subtree. 
Defining whether access to the 
MIB subtree is allowed  
type {included | 
excluded} 
snmp>view 
included – Allow access to 
the subtree. 
excluded – Do not allow 
access to the subtree. 
Administratively enabling view 
no shutdown 
snmp>view 
 
Displaying trap synchronization 
groups and members for 
SNMPv3 manager groups 
show trap-sync 
snmp 
 
Megaplex-1 
6. Management and Security 
Task 
Command 
Level 
Comments 
Displaying SNMPv3 
information, such as the 
number of times the SNMPv3 
engine has booted, and how 
long since the last boot 
show snmpv3 
information 
snmp 
 
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
#********* Configure user MD5_priv with authentication method MD5 with DES privacy 
protocol 
  user MD5_priv md5-auth des 
    privacy password MD654321 
    authentication password MD654321 
    no shutdown 
    exit 
 
#******** Configure access group MD5Group with various authentication and privacy 
options 
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
Megaplex-1 
6. Management and Security 
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
Megaplex-1 
6. Management and Security 
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
Megaplex-1 
6. Management and Security 
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
 
#******** Configure target parameters 
  target-params snv1 
    message-processing-model snmpv1 
    version snmpv1 
    security name v1_trap level no-auth-no-priv 
    no shutdown 
    exit 
 
Megaplex-1 
6. Management and Security 
#******** Configure target 
  target NMSsnmpv1 
    target-params snv1 
    tag-list unmasked 
    address udp-domain  192.5.6.7 
    no shutdown 
    exit all 
save 
 To display SNMPv3 information: 
# configure management snmp 
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
  target NMS4 
    trap-sync-group 2 
      exit 
    trap-sync-group 1 

## 6.9 User Access  *(p.262)*

Megaplex-1 
6. Management and Security 
      tag-list “port power” 
      target-params TargParam1 
      exit all 
save 
 To display trap synchronization configured in above example: 
config>mngmnt>snmp# show trap-sync 
Group ID  Member 
--------------------------------------------------------------- 
1         NMS1 
1         NMS2 
2         NMS3 
2         NMS4 
 
6.9 User Access 
Megaplex-1 management software allows you to define new users, and their management and access 
rights.  
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
The default users cannot be deleted, but can be disabled (shut down). 
Functional Description 
Megaplex-1 supports the following four user access levels: 
Megaplex-1 
6. Management and Security 
• 
Superuser (su) can perform all the activities supported by the system, including creating new 
users, changing its and other user access levels and passwords, deleting and disabling other 
users. 
• 
Operator (oper) can perform all the activities, except for defining, deleting or disabling other 
users. 
• 
Technician (tech) can monitor the device (info, show status, show statistics).  
• 
User (user) can monitor the device (info, show status, show statistics). 
The regular users (oper, tech, user) cannot define, delete or disable other users, or change their own 
access levels. They are allowed to change their current passwords. All users can view all CLI levels. 
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
SSH Authentication 
In addition to password, Megaplex-1 can be configured to use more robust and secure public key user 
authentication method for SSH sessions. 
Configuring Users 
 To add a new user: 
1. Verify that you are logged on as superuser (su). 
Megaplex-1 
6. Management and Security 
2. Navigate to the management context (config>mngmnt). 
3. Enter login-user, followed by a new user name if you intend to create a new user, or an existing 
name, if you intend to change previously defined user. 
Note 
Maximum user name length is 20 characters.  
4. The prompt changes to config>mngmnt>login-user<user-name>#. 
5. Enter the necessary commands according to the tasks listed in the table below. 
 To delete an existing user: 
1. Verify that you are logged on as superuser (su). 
2. Navigate to the management context (config>mngmnt).  
3. Enter no login-user, followed by the name of the user that you intend to delete. 
Task 
Command 
Comments 
Specifying user 
authentication method 
authentication-method {password | 
public-key} 
 
The default user 
authentication method is 
password 
If you change the 
authentication method of 
a user with access level su 
to public key, and no 
public key has been 
defined, you are warned 
that the super user is going 
to be disabled, and 
prompted to confirm the 
operation. 
Defining a user access level 
level { su | oper | tech | user } 
 
Specifying user password 
 password <password> [hash] 
Maximum password length 
is as follows: 
• Non-hashed – 20 
characters 
• Hashed – 40 characters 
The use of hash function is 
illustrated in the example 
below. 
Megaplex-1 
6. Management and Security 
Task 
Command 
Comments 
Setting user public key for 
authentication 
public-key <public-key> 
no public-key deletes the 
public key.  
Public key configuration is 
relevant only for the public 
key authentication 
method. 
Use the Base64 encoding 
(ASCII ‘A’ to ‘Z’, ‘a’ to ‘z’, 
‘0’ to ‘9’, ’+’, ‘/’ and 
‘space’) for the public key 
configuration. 
Set the key string using the 
following format: 
• Begin and end with “ 
• Include: ’ssh-rsa’, 
‘space’, public key 
string, ‘space’, 
comment 
Enabling/disabling a user 
shutdown  
no shutdown 
Default users (su, oper, 
tech, user) can be disabled, 
but cannot be deleted. 
Example – Defining Users 
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
no shutdown 
exit 
Megaplex-1 
6. Management and Security 
 To add a new user with a hashed password: 
1. Define a new user with a text password. 
2. Use info detail to display the password hash value. 
3. Define another user with the hashed password from the info detail output. 
The second user can log in with the text password defined in step 1. 
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
no shutdown 
exit 
 
exit all 
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
Megaplex-1 
6. Management and Security 
 To delete an existing user: 
• 
At the config>mngmnt# prompt, enter no login-user <user_name>. 
The specified user is deleted. 
 To view all connected users: 
• 
At the config>mngmnt# prompt, enter show users. 
A list of all connected users is displayed, showing their access level, the type of connection, and 
the IP address from which they are connected. 
Example – Displaying Users 
# configure management 
config>mngmnt# show users 
Num       User                          Access Level  Source    IP 
Address 
----------------------------------------------------------------------
------- 
1.        su                            Su            Terminal  
0.0.0.0 
Viewing User Information 
The details of the currently logged-in users are available in the show users-details screen.  
The screen for show users-details provides the following information: 
User 
User name 
Level 
User access level 
Popup 
Alarm/event popup status (enabled or disabled) 
From 
Source IP address of the management session, followed by protocol 
type (serial, Telnet, SSH)  
For (sec) 
Duration of the current management session in seconds 
Connected To 
Destination IP/ protocol type of the active client Telnet session (to a 
remote device) 
For (sec) 
Duration of the active client Telnet session (to a remote device) in 
seconds 
Megaplex-1 
6. Management and Security 
 To display the user information:  
• 
In the configure>management# prompt, enter show users-details.  
# configure management 
config>mngmnt# show users-details 
User:1234  Level:su  Popup:Disabled 
    From:1.1.1.1/SSH  For(sec):120  
User:123456  Level:oper  Popup:Disabled 
    From:100.100.100.100/Telnet  For(sec):120  
    Connected To:1111:2222:3333:4444:5555:6666:7777:8888/Telnet  
For(sec):100 
User:su  Level:su  Popup:Enabled 
        From:Serial  For(sec):94 
Viewing SSH Server Information  
You can display the fingerprint of the SSH server public key. 
 To display the SSH server information: 
• 
At the config>mngmnt# prompt, enter show ssh-server fingerprint. 
The SSH fingerprint information stored on the SSH server is displayed. 
# configure management  
config>mngmnt# show ssh-server fingerprint 
RSA key fingerprint is ef:ab:28:81:53:c2:a3:8d:77:0d:06:e7:89:2b:81:9c 
 
 
 