# Feature Reference – 3 Management and Security

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 697–801.*


## 3.1 Access Control List (ACL)  *(p.697)*

3 Management and Security 
3.1 Access Control List (ACL) 
Access control lists are used to flexibly filter and mark incoming and management traffic.  
Service providers use ACLs to maintain network security by preventing malicious traffic from entering 
the device. ACLs can be used to save network resources by dropping unwanted packets.  
When user or management data is marked via ACLs, service providers can apply various traffic 
management techniques to the marked packets, such as allocating more bandwidth to a certain traffic 
type. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products under the following condition: 
• 
ETX-2i-10G and ETX-2i-100G – ACL can be applied only to management packets. 
• 
ETX-2i and ETX-2i-B – ACL can be applied to management packets and router interfaces. 
Both IPv4 and IPv6 ACLs are supported. 
A device supports one IPv4 and one IPv6 ACL for management access. 
Up to 64 management ACRs (ACL rules) are supported for either IPv4 or IPv6. 
Only inbound management ACL is supported. 
 
 
ETX-2i Devices 
3. Management and Security 
It is possible to configure ACL to allow the following management access per manager: 
• 
Telnet  
• 
SSH  
• 
SNMP  
• 
NETCONF  
• 
All traffic per source IP address (version 6.8.2 (3.75)) 
Implicit and Explicit Deny All functionality is relevant for version 6.8.2 (3.75). 
Standards Compliance 
Relevant sections of RFC 1812 
Functional Description 
Devices featuring ACLs can flexibly filter user or management traffic, by denying or permitting IP packets 
to enter the host, according to the packet’s source/destination address, protocol type, or other criteria. 
ACL entries are sequentially numbered rules containing statements (Deny, Permit, or Remark) and 
conditions. Remarks are free-text ACL entries used for commenting and visually organizing ACLs.  
Packets are permitted or denied access, based on the following conditions: 
• 
IP source and destination address or address range 
• 
IP protocol 
• 
TCP port – TCP/23 (TELNET), TCP/22 (SSH), TCP/830 (NETCONF) 
• 
UDP port – UDP/161 (SNMP) 
The ACL structure is illustrated in the Example section. 
If there is a need to add a rule between already existing rules with consecutive numbers, the rules can 
be interspaced to accommodate additional rules between them. For example, if you apply resequencing 
to an ACL including rules 1, 2, and 3, with an interspacing value of 30, the rule numbers will change to 
30, 60 and 90. Sequence numbers can also be set at the rule level. 
ETX-2i Devices 
3. Management and Security 
Binding Access Control Lists 
Once created, ACLs are applied (bound) to router interfaces for filtering user traffic, or to the virtual 
management entity for filtering management traffic. For the management entity and router interfaces, 
ACLs can be used in the inbound direction only. If a router interface is deleted, all associated ACLs are 
automatically detached. 
Only one IPv4 ACL is supported per router interface / management entity. An additional IPv6 ACL may 
coexist with one IPv4 access list on the same interface / management entity. 
Filtering and Marking 
Packets attempting to enter an entity to which the ACL is bound are checked against the access list rules, 
one by one. Access of matching packets is denied (packets are dropped) or permitted (packets are 
forwarded and possibly marked), as directed by the ACL statement. 
Packets matching a Deny statement (rule) are dropped unless permitted by a previous rule.  
Packets matching a Permit statement (rule) are permitted to access an entity unless denied by a 
previous statement. Permit statements may also set the ToS byte or Layer-2 priority of packets matching 
them.  
When a rule match occurs, an entry is added to the event log if logging is enabled. To prevent log 
overflow, it is possible to disable logging (per rule or device) or define the minimal logging interval of 
packets matching ACL entries (per device).  
Note 
By default, logging is disabled. If you choose to enable it, the default logging 
interval is five minutes.  
Two packets matching the same rule on the same entity in the same direction are logged only if the time 
between them exceeds the logging interval.  
After a match, the rest of the rules are ignored.  
Implicit and Explicit Deny All 
Packets not matching any rule are handled as follows: 
• 
Implicit deny rule is applied on the following packet types only: 
 
TCP port 22 (SSH) 
 
TCP port 23 (TELNET) 
 
TCP port 830 (NETCONF) 
 
UDP port 161 (SNMP) 
ETX-2i Devices 
3. Management and Security 
• 
Other non-matching packets are allowed into the host (e.g., ICMP). 
• 
User can use an explicit deny all rule (last rule in ACL): ‘deny ip any any’. This rule drops (denies) 
any non- matching packets.   
Statistics 
The device collects ACL statistics per router, router interface, and management entity. The statistic 
counters include the number of rule matches that occurred since the counters were last cleared. The 
statistic counters are cleared upon device reboot. The user may also clear ACL statistics of any entity. 
Factory Defaults 
Parameter defaults are alphabetically listed in the tables below. 
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
ETX-2i Devices 
3. Management and Security 
Topic 
Parameter 
Default Value 
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
2. Add deny and permit rules to the ACL. 
3. Bind the ACL to a router interface or management entity. 
4. Configure additional ACL parameters (logging interval, ICMP Unreachable messages, etc.), if 
necessary. 
Access-Control-Level Tasks 
The following commands are available in the CLI access-control context: config>access-control#. The 
exceptions to this are the deny, permit and remark commands, which are performed in the access-
list(acl_name) context: config>access-control>access-list(acl_name)#. 
 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Creating and 
deleting an ACL 
access-list [{ ipv4 | ipv6 }] <acl_name> 
no access-list <acl_name> 
Creating an ACL is 
performed by assigning a 
name and specifying the ACL 
IP type. The ACL names must 
be unique. 
The ACL name contains up to 
80 alphanumeric characters. 
Note: If you delete an ACL 
that is bound to an entity, 
the device behaves (i.e., 
traffic passes) as if no ACL is 
bound.  
Adding deny 
rules to an ACL 
deny { tcp | udp } { any | <src-address> [/<src-prefix-
length>] } [<src-port-range>] { any | <dst-address>[/<dst-
prefix-length>] } [<dst-port-range>] [dscp <dscp-value> | 
precedence <ip-precedence-value>] [log] [sequence 
<sequence-number>] 
deny icmp { any | <src-address> [/<src-prefix-length>] } 
{any|<dst­address> [/<dst­prefix-length>]} [icmp-type 
<icmp-type-number> [icmp­code <icmp-code-number>]] 
[dscp <dscp-value> | precedence <ip­precedence­value>]  
[log] [sequence <sequence-number>] 
deny ip [protocol <ip-protocol-number>] { any | <src-
address> [/<src-prefix-length>] } { any 
|<dst­address>[/<dst­prefix-length>] } [dscp <dscp-value> | 
precedence <ip­precedence-value>] [log] [sequence 
<sequence­number>] 
The arguments of the deny 
rule vary depending on the 
protocol (TCP, UDP, ICMP, 
IP).  
DSCP and IP Precedence 
cannot be used together. 
Management-bound ACLs 
have the following 
configuration limitations: 
• TCP-, UDP-, and IP-based 
rules can be defined. 
• The destination IP 
address must be any. 
• For TCP/UDP, the 
destination port must be 
tcp/23 (Telnet), tcp/22 
(SSH), tcp/830 
(NETCONF), udp/161 
(SNMP), or any.  
• The source port must 
remain any (i.e., optional 
src-port-range field 
should not be 
configured). 
• DSCP and IP Precedence 
are not supported. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
log enables logging match 
events of the rule into the 
event log and sending SNMP 
traps. 
Possible values for  
ip-protocol-number: 0-255 
sequence-number:  
1–2147483648. 
Note:  
• If the ACL already has a 
statement with the same 
sequence number, the 
old statement is replaced 
with the new one. 
• These rules do not apply 
to out-of-band (OOB) 
ports. 
Adding permit 
rules to an ACL 
permit { tcp | udp } { any | <src-address>[/<src-prefix-
length>] } [<src-port-range>] { any|<dst-address>[/<dst-
prefix-length>] } [<dst-port-range>] [dscp <dscp-value> | 
precedence <ip-precedence-value>] [set {dscp < dscp-
marking-value> | precedence <ip-precedence-marking-
value> | pbit <pbit-marking-value>}] [log] [sequence 
<sequence-number>] 
permit icmp { any | <src-address>[/<src-prefix-length>] } { 
any | <dst­address>[/<dst­prefix-length>] } [icmp-type 
<icmp-type-number> [icmp­code <icmp-code-number>]] 
[dscp <dscp-value> | precedence <ip­precedence­value>] 
[set { dscp < dscp-marking-value> | precedence 
<ip­precedence-marking-value> |  
pbit <pbit-marking-value> }] [log] [sequence <sequence-
number>] 
permit ip [protocol <ip-protocol-number>] {any | <src-
address>[/<src-prefix-length>]} {any 
|<dst­address>[/<dst­prefix-length>]} [dscp <dscp-value> | 
precedence <ip­precedence-value>] [set {dscp < dscp-
marking-value> | precedence <ip-precedence-marking-
value> | pbit <pbit-marking-value>}] [log] [sequence 
<sequence­number>] 
The arguments of the permit 
rule vary depending on the 
protocol (TCP, UDP, ICMP, 
IP).  
DSCP and IP Precedence 
cannot be used together. 
Management-bound ACLs 
have the following 
configuration limitations: 
TCP-,UDP-, or IP-based rules 
can be defined. 
The destination IP address 
must be any. 
For TCP/UDP, the 
destination port must be 
tcp/23 (Telnet), tcp/22 
(SSH), tcp/830 (NETCONF), 
udp/161 (SNMP), or any.  
The source port must remain 
any (i.e., optional src-port-
range field should not be 
configured). 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
DSCP and IP Precedence are 
not supported. 
log enables logging match 
events of the rule into the 
event log and sending SNMP 
traps. 
Possible values for 
sequence:1–2147483648 
Note:  
• If the ACL already has a 
statement with the same 
sequence number, the 
old statement is replaced 
with the new one. 
• These rules do not apply 
to out-of-band (OOB) 
ports. 
Adding remarks 
to an ACL 
remark <description> [sequence <sequence-number>] 
The description contains up 
to 255 characters. 
Resequencing 
the rules in an 
ACL 
resequence access-list <acl-name> [<value>] 
Possible values for value:  
1–100000 
Removing rules 
from an ACL 
delete <sequence-number> 
Possible values for 
sequence-number:   
1–2147483648. 
Setting the 
logging interval 
of all ACLs 
logging access-list <value> 
no logging access-list 
Enable logging at the 
maximum rate of the value 
set at Access Control level. 
<0> is equivalent to no 
logging access-list 
command. 
no logging access-list 
disables event logging for all 
rules in the ACL. 
ETX-2i Devices 
3. Management and Security 
Router-Level Tasks 
The following commands are available in the CLI router-interface context: router(number)> 
interface(number)#. The exceptions to this are the show access-list summary and show statistics 
access-list commands, which can be used in the router(number) context as well.  
 
Task 
Command 
Comments 
Binding the ACL to a router interface and 
defining the ACL direction 
access-group <acl-name> in 
no access-group in { ipv4 | ipv6 }  
 
Sending/stop sending ICMP Unreachable 
messages 
unreachables 
no unreachables 
 
Displaying ACL statistics 
show statistics [{ ipv4 | ipv6 }] 
access-list {in}  
See Viewing Statistics 
below. 
Clearing ACL statistics 
clear-statistics access-list  
clear-statistics access-list [interface 
<router-interface>  
Router interface level 
Router level 
Displaying the summary of ACLs bound to 
router interface 
show access-list summary 
Displays ACL status at the 
current level 
See Viewing Status below. 
 
 
ETX-2i Devices 
3. Management and Security 
Management-Level Tasks 
The following commands are available in the CLI management context: config>mngmnt>access#. 
 
Task 
Command 
Comments 
Binding the ACL to a 
management entity and 
defining the ACL direction 
access-group 
<acl-name> in 
[{ipv4 | ipv6}] 
no access-group 
in {ipv4 | ipv6} 
The management entity supports the ACLs only in the in 
direction. 
When binding the ACL to the management entity, or when 
adding/editing rules in an ACL that is bound to the 
management entity, the rules must conform to the 
following limitations: 
• The protocol rules must be of TCP/UDP type. 
• The destination address must be set to any. 
• The source port must be set to any. 
• The destination port must be tcp/830 (NETCONF), 
tcp/23 (Telnet), tcp/22 (SSH), udp/161 (SNMP), or any. 
• DSCP, IP precedence, and P-bit cannot be used. 
Note: If you delete an entity that is bound to the ACL, the 
binding is deleted, but the ACL remains. If the entity is 
created again, the ACL binding is not reconfigured 
automatically. 
Displaying ACL statistics 
show statistics 
[{ipv4 | ipv6}] 
access-list {in} 
See Viewing Statistics below. 
Clearing ACL statistics 
clear-statistics 
[{ipv4 | ipv6}] 
access-list {in} 
 
Displaying the summary of 
ACLs bound to a 
management entity 
show access-list 
summary 
Displays ACL status at the current level 
See Viewing Status below. 
Encrypting an SFTP password 
ztc-xml-
generate-
encrypted-
password 
<cleartext> 
cleartext – Unencrypted (cleartext) password 
Supported length: 1-32 characters 
Supported characters: Comma (,), space, ~, !, #, $, %, &, ‘, (, 
), *, +, `, -, _, ., /, :, ;, <, =, >, @, [, |, ], ^, {, |, } 
ETX-2i Devices 
3. Management and Security 
Examples 
Management ACL 
The examples below illustrate typical ACLs applied to incoming management traffic. 
Example 1: 
• 
Allows SSH (TCP port 22) traffic from any source 
• 
Permits and logs incoming Telnet (TCP port 23) connections from 192.168.1.0 subnet 
• 
Denies and logs Telnet traffic from any source 
• 
Implicit deny (no explicit command); see behavior description above for implicit deny 
access-control>access-list(mng1)# 
remark Allow incoming SSH traffic 
permit tcp any any 22 
remark Allow Telnet traffic coming from 192.168.1.0 subnet 
permit tcp 192.168.1.0/24 any 23 
remark Deny and log incoming Telnet traffic 
deny tcp any any 23 log 
The table below summarizes the rules configured for the ACL. Items in red are either implied or 
unavailable for the current parameter. 
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
192.168.1.0/24 
Any 
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
Example 2: 
• 
Permits traffic from IP subnet 20.20.20.00/24 
• 
Permit traffic from IP address 10.10.10.10 
• 
Permit SSH traffic from 30.30.30.30 only. 
• 
Explicit deny all command (deny any non-matching traffic). 
access-control>access-list(mng2)# 
permit ip 20.20.20.00/24 any sequence 10 
permit ip 10.10.10.10 any sequence 20 
permit tcp 30.30.30.30 any 22 sequence 30 
deny ip any any sequence 40 
ETX-2i Devices 
3. Management and Security 
The table below summarizes the rules configured for the ACL. Items in red are either implied or 
unavailable for the current parameter. 
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
IP 
20.20.20.20 
N/A 
Any 
N/A 
No 
20 
Permit 
IP 
10.10.10.10 
N/A 
Any 
N/A 
No 
30 
Permit 
TCP 
30.30.30.30 
Any 
Any 
22 
No 
40 
Deny 
IP 
Any 
N/A 
Any 
N/A 
No 
 
Router ACL 
The examples below illustrate two typical ACLs applied to the incoming and outgoing traffic. 
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
The table below summarizes the rules configured for the ACL. Items in red are either implied or 
unavailable for the current parameter or serve as system settings that cannot be changed. The deny rule 
appearing in the bottom row is a system rule that is used to deny all non-compliant data. 
 
Sequence 
Number 
Actio
n 
Protocol 
IP 
Protocol 
Source IP 
TCP/UDP  
Source Port 
Dest. IP 
TCP/UDP 
Dest. Port 
ICM
P 
Typ
e 
ICMP 
Code 
ToS 
Mar
k 
Lo
g 
10 
Permi
t 
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
Permi
t 
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
Permi
t 
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
40 
Deny 
IP 
Any 
Any 
N/A 
Any 
N/A 
N/A 
N/A 
Any 
N/A 
No 
ETX-2i Devices 
3. Management and Security 
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
Actio
n 
Protoco
l 
IP 
Protocol 
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
Mar
k 
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
Permi
t 
IP 
Any 
192.168.1.10 
N/A 
Any 
Any 
N/A 
N/A 
Any 
– 
No 
30 
Permi
t 
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
40 
Deny 
IP 
Any 
Any 
N/A 
Any 
N/A 
N/A 
N/A 
Any 
N/A 
No 
 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Description 
Cannot add statement; sequence 
number is out of range 
Invalid sequence number of the rule. Allowed sequence number range is 
1–2147483648. 
Cannot bind; invalid statement 
An access list with statements, which are not supported by the 
management ACL, cannot be attached to the management entity. 
Cannot bind; no such access list 
A non-existing ACL cannot be bound to the router interface or the 
management entity. 
Cannot clear; no such router 
interface 
Statistic counters cannot be cleared on the non-existing router interface. 
Cannot execute; invalid statement 
Only TCP, UDP, or IP rules can be 
in management ACL 
Invalid matching rule. For example, binding the ACL with a rule, using a 
protocol other than TCP, UDP, or IP to the management entity. 
ETX-2i Devices 
3. Management and Security 
Message 
Description 
Cannot resequence; sequence 
number out of range 
Resequencing has failed because the ACL interspace value is invalid. 
Cannot show; no such router 
interface 
Statistic counters cannot be displayed on the non-existing router 
interface. 
Destination IP must be ‘any’ in 
management ACL 
The ACL is bound to management and the destination IP is not any. 
Destination port must be ‘any’ in 
management ACL 
The ACL is bound to management and the destination port is not any. 
DSCP and IP precedence are not 
allowed in the same rule 
The user tried to configure both DSCP and IP precedence. 
DSCP is not allowed in 
management ACL 
The ACL is bound to management and the rule contains DSCP 
configuration. 
Invalid destination port for 
management ACL 
The ACL is bound to management and the destination port is not tcp/23 
(telnet), tcp/22 (ssh), udp/161 (snmp), tcp/830 (netconf) or any. 
IP precedence is not allowed in 
management ACL 
The ACL is bound to management and the rule contains IP precedence 
configuration. 
Maximum number of ACLs has 
been reached 
The user tried to configure more than 128 ACLs. 
Maximum number of rules 
exceeded 
The user tried to add more rules than the device can support per ACL. 
Source port must be ‘any’ in 
management ACL 
The ACL is bound to management and the source port is not any. 
Viewing Status 
The ACL status displays information on the ACL name, type (IPv4 or IPv6), and the entity that the ACL is 
bound to. The ouput lines are sorted by ACL name and IP version. The status information is available for 
the ACLs at the router, router interface, and management access levels. 
 To display the ACL status (router): 
1. Navigate to the required prompt (router(number)#, router(number)> interface(number)#). 
2. Enter the show access-list summary command. 
The following status information is displayed: 
ETX-2i Devices 
3. Management and Security 
ACL Name|Type|Bound to  |Direction 
--------|----|----------|--------- 
my-acl  |IPv4|RI 2      |In 
 To display the ACL status (management): 
• 
In the config>mngmnt>access# prompt, enter the show access-list summary command. 
The following status information is displayed: 
ACL Name     Type    Bound to    Direction 
--------------------------------------------------------------- 
MNG_port_1   IPv4    management  inbound 
Viewing Statistics 
The ACL statistic counters gather information on the number of rule matches registered on the ACL since 
the last reboot or counter clearing.  
 
Note 
All ACLs have an implied last rule that denies all packets. The device does not 
provide statistic counters for this rule. If you intend to collect statistics on the 
number of packets discarded by the default ACL mechanism, you must add the 
deny ip any any rule at the end of the ACL.  
 To display the ACL statistics (router): 
1. Navigate to the required level: router or router-interface. 
2. Enter the show statistics [{ipv4 | ipv6}]access-list command as explained in the tables above. 
The following statistic information is displayed: 
IPv4 access list: block-invalid-traffic-in (in) 
Bound to: 
  Router: 1, Interface: 2  
Matches counted for: 7 seconds 
  10 deny tcp any any dscp 17 (5 matches) 
 To display the ACL statistics (management): 
1. Navigate to the management access level. 
2. In the config>mngmnt>access# prompt, enter show statistics ipv4 access-list (for IPv4) or show 
statistics ipv6 access-list (for IPv6). 
The following statistical information is displayed: 

## 3.2 Authentication via RADIUS Server  *(p.712)*

ETX-2i Devices 
3. Management and Security 
IPv4 access list: MNG_port_1                (in) 
Bound to: Management 
Matches counted for: 0 days 0 hours 2 minutes 33 seconds 
--------------------------------------------------------------- 
10    permit  tcp 172.17.154.154/24  any  22  log   (0 matches) 
20    permit  tcp 172.17.154.154/24  any  23  log   (0 matches) 
30    permit  udp 172.17.154.154/24  any  161 log   (0 matches) 
 
IPv4 access list: MNG2                      (in) 
Bound to: Management 
Matches counted for: 0 days 1 hours 1 minutes 20 seconds 
--------------------------------------------------------------- 
10    permit      any          any  (0 matches) 
20    deny        10.10.10.10  any  (0 matches) 
30    permit  tcp 20.20.20.20  any  (0 matches) 
3.2 Authentication via RADIUS Server 
RADIUS (Remote Authentication Dial-In User Service) is an AAA (authentication, authorization, and 
accounting) client/server protocol that secures networks against unauthorized access. It is used to 
authenticate users and authorize their access to the requested system or service. The RADIUS client 
communicates with the RADIUS server using a defined authentication sequence.  
The RADIUS protocol allows centralized authentication and access control, avoiding the need to 
maintain a local user database on each device in the network. 
Due to its generic nature, the RADIUS protocol can easily be used by service providers and enterprises to 
manage access to the Internet, internal networks, wireless networks, and integrated email services. 
These networks may incorporate DSL, access points, VPNs, network ports, and more. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products.  
Standards Compliance 
RFC 2865, Remote Authentication Dial In User Service (RADIUS)  
RFC 2618, RADIUS Authentication Client MIB 
ETX-2i Devices 
3. Management and Security 
Functional Description 
RADIUS servers have built-in mapping of users to service-types (see table below). Note that each user 
has the rights of all users above it. All users have default password 1234. It is highly recommended to 
change the default password when setting up your device (Refer to Changing Password on how to 
change a password). 
Name 
Prompt 
RADIUS Service-Type (User Access Level) 
user 
ETX-2i% 
1 (login) 
tech 
ETX-2i% 
7 (NAS prompt) 
oper 
ETX-2i# 
8 (authenticate only) 
su 
ETX-2i# 
6 (administrative) 
When a user attempts to log in to ETX-2i, the following occurs: 
1. User is prompted to enter their username and password. 
2. RADIUS client submits an authentication request to the RADIUS server. The username and 
encrypted password are transmitted over the network. (A hash code is generated over the 
entered password and a previously defined shared secret (string of free text) is transmitted 
between the RADIUS server and ETX-2i unit.) 
3. The RADIUS server verifies the user information against a database stored at the RADIUS server, 
and sends one of the following responses:  
 
Access Rejected – User is not authenticated and access to all resources is denied. User is 
prompted to reenter their username and password. 
 
Access Accepted – User is authenticated. Access to the requested network resources is 
granted. The RADIUS service type is sent, indicating what services the user can access. 
RADIUS Server
ETX-2i
Shared Secret
Management Work Station
Logon request to ETX-2i
Verifying credentials and privileges via RADIUS data base
Logging on to ETX-2i or
returning authentication error
Access accepted or denied
Network
 
ETX-2i Devices 
3. Management and Security 
Factory Defaults 
By default, four RADIUS servers are predefined, configured as shown below. 
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
Configuring RADIUS Authentication 
ETX-2i provides connectivity to up to four RADIUS authentication servers. You have to specify access 
parameters such as Radius server ID, associated server IP address, the number of allowed authentication 
request attempts, etc. 
 To define a RADIUS server: 
1. Navigate to configure management radius. 
2. At the config>mngmnt>radius# prompt, enter server <1..4> to specify which server to 
configure. 
The config>mngmnt>radius>server(<1..4>)# prompt is displayed. 
3. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning an IP address to the server 
address <ip-address> 
A valid unicast IP address 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Defining a non-disclosed string 
(shared secret) used to encrypt the 
user password. 
key <string> [hash] 
The shared secret is a secret 
key consisting of free text 
known to the client and the 
server for encryption.  
The hash keyword denotes 
that the string is sn, rather 
than clear text; usually it is 
added by the device after 
hashing the clear text that 
the user enters, before 
saving it in the database. 
If you enter the password as 
a text string, do not use the 
hash parameter. Use it only 
if you are specifying the 
password as a hashed value 
(obtained by entering the 
info command to display 
RADIUS data). 
Length: 1 – 79 characters 
Possible characters: Space, 
comma (,), ~, ?, “, !, #, $, %, 
&, ‘, (, ), *, +, `, -, _, ., /, :, ;, <, 
=, >, @, [, |, ], ^, {, |, } 
0-9 
A-Z 
a-z 
Note: If “ is used in a 
password, the password 
must start and end with “. 
Defining the number of 
authentication request attempts 
retry <number-of-retries> 
Possible values: 0–10 
Defining timeout (in seconds) for 
response from RADIUS server 
timeout <seconds> 
Possible values: 1–5 
Defining the UDP port to be used for 
authentication  
auth-port <udp-port-number> 
Possible values: 1–65535 
Administratively enabling server 
no shutdown 
Enter shutdown to 
administratively disable the 
server. 

## 3.3 Authentication via TACACS+ Server  *(p.716)*

ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Displaying status 
show status 
 
Viewing RADIUS Statistics 
 To display RADIUS statistics: 
1. Navigate to configure management radius. 
2. At the config>mngmnt>radius# prompt, enter: 
show statistics 
RADIUS statistics appear as shown below. 
ETX-2i>config>mngmnt>radius# show statistics  
 
Server1 
Server2 
Server3 
Server4 
-------------------------------------------------------------------------- 
Access Requests 
: 
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
Timeouts 
: 
0 
0 
0 
0 
Unknown Types : 
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
 To clear the statistics for RADIUS: 
• 
At the config>mngmnt>radius# prompt, enter: 
clear-statistics 
The RADIUS statistics are cleared. 
3.3 Authentication via TACACS+ Server 
TACACS+ (Terminal Access Controller Access Control System Plus) is a security application that provides 
access control for routers, network access servers, and other networked computing devices via one or 
more centralized servers. TACACS+ provides separate authentication, authorization, and accounting 
ETX-2i Devices 
3. Management and Security 
services. It is used to communicate between the switch and an authentication database. As TACACS+ is 
based on TCP, implementations are typically resilient against packet loss. 
The TACACS+ protocol allows centralized authentication and access control, avoiding the need to 
maintain a local user data base on each device on the network. The TACACS+ server encrypts the entire 
body of the packet but leaves a standard TACACS+ header. 
Customers do not have to adapt their TACACS+ server privilege levels to RAD CLI default values; CLI 
levels can be remapped in accordance with the customer’s TACACS+ levels.  
Applicability and Scaling 
This feature is applicable to all ETX-2i products.  
Standards Compliance 
TACACS+ Protocol Version 1.78 (IETF draft-grant-tacacs-02) 
TACACS+ accounting is supported per RFC 8907.  
Factory Defaults 
By default, no TACACS+ servers are defined. When the TACACS+ server is first defined, it is configured as 
shown below. 
Parameter 
Default Value 
key 
“” hash 
retry 
1 
timeout 
5 seconds 
priority 
100 
authentication-port 
49 
accounting-port 
49 
Administrative status 
shutdown 
Accounting group membership 
no group 
ETX-2i Devices 
3. Management and Security 
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
Note 
TACACS+ performs authorization according to the user level; it does not send 
each command to the server for authorization.  
The TACACS+ client can be configured to use authentication/authorization with or without accounting 
functionality. 
When configuring users on external TACACS+ servers, define authorization levels for ETX-2i standard 
users (see table below). Note that each user has the rights of all users below it, in addition to those 
explained in its description. 
 
Level 
User 
Allowed 
Actions 
Description 
3 
user 
Monitoring 
Commands that do not affect services, traffic, or configuration 
6 
tech 
Diagnostics 
Commands that may affect services and traffic, but are not saved in the 
database 
9 
oper 
Configuration 
Commands that change configuration parameters permanently 
12, 15 
su 
User 
management 
Commands that manage users in the database 
Components 
The TACACS+ remote access environment has three major components: access client, TACACS+ client, 
and TACACS+ server.  
• 
The access client is an entity that seeks the services offered by the network.  
• 
TACACS+ client, running on ETX-2i, processes the requests from the access client and passes this 
data to TACACS+ server for authentication.  
ETX-2i Devices 
3. Management and Security 
• 
TACACS+ server authenticates the request and authorizes services over the connection. The 
TACACS+ server does this by matching data from the TACACS+ client`s request with entries in a 
trusted database. 
TACACS+ server decides whether to accept or reject the user's authentication or authorization. Based on 
this response from the TACACS+ server, the TACACS+ client decides whether to establish the user's 
connection or terminate the user's connection attempt. The TACACS+ client also sends accounting data 
to the TACACS+ server to record in a trusted database. 
TACACS+ uses TCP for its transport and encrypts the body of each packet. TACACS+ client and server can 
agree to use any port for authentication and accounting. TACACS+ supports authentication by using a 
username and a fixed password. 
TACACS+ Server Prioritization 
ETX-2i enables configuring the required priority of each TACACS+ server, giving the user more flexibility 
in prioritizing the servers (regardless of whether the server IP address value is higher or lower). 
When authenticating, the device first attempts to access the server with the highest priority, and if this 
fails, tries the remaining servers in descending order of priority. If multiple servers have the same 
priority, the device first tries to access the one with the lowest IP address, and if this fails, tries accessing 
servers in ascending order of their IP addresses. 
TACACS+ Single Server Accounting 
ETX-2i supports the single-server-accounting command to enable the sending of accounting messages 
to a single server. 
By default, this command is disabled, and the device sends messages to all the servers in the group. 
When enabling this feature, the device tries sending accounting messages to the server with the highest 
priority. If the server doesn’t send a reply within the configured timeout (1-30 seconds; default: five 
seconds), the server with the highest priority among the remaining servers is tried, and so on, until a 
server replies, or all the servers are exhausted. If multiple servers have the same priority, the one with 
the lowest IP address is tried first, followed by the one with the second lowest, and so on. 
Accounting 
ETX-2i supports up to five accounting groups, with up to five TACACS+ servers per group. However, each 
TACACS+ server can be bound to a single accounting group only. 
A group can be defined with its own accounting level: 
ETX-2i Devices 
3. Management and Security 
• 
Shell accounting, which logs the following events: 
 
Successful logon 
 
Logon failure 
 
Logoff 
 
ETX-2i - terminated management session 
• 
System accounting, which records system events/alarms registered in local log file 
• 
Command accounting, which logs the following events: 
 
Any shell command that was successfully executed by ETX-2i 
 
Any level that was successfully changed in a shell 
Note 
The password that you enter when creating a new user (configure 
management login-user <name> password <password>, or when copying a 
file (file copy <source-file-url> <destination-file-url> 
sftp://<username>:<password>) is masked in TACACS+. The password entered 
appears in the TACACS+ command log as asterisks (*), thus providing 
protection from sniffers.  
You can enter the syntax for copying files also without <password>, if you 
wish to enter it separately when prompted. Also in this case, the characters of 
the entered password appear as asterisks (*). 
Mapping Privilege Levels 
ETX-2i supports configuration of mapping CLI levels to TACACS+ privilege levels.   
• 
There are 16 TACACS+ privilege levels. 
• 
You can map a CLI level to multiple TACACS+ levels. 
• 
You cannot map a TACACS+ level to multiple CLI levels. If the command is repeated for a 
TACACS+ level, the new mapping replaces the old one. 
• 
You can unmap both TACACS+ and CLI levels except for su, which must be mapped to at least 
one TACACS+ level. 
TACACS+ Server/User Messaging 
ETX-2i supports the TACACS+ ability to pass messages between the server and user (utilizing the 
server_msg and user_msg fields). This can be used for example to implement multifactor 
authentication, by passing the challenge and response messages via these fields. 
ETX-2i Devices 
3. Management and Security 
Configuring TACACS+ Authentication 
You configure the TACACS+ authorization, the TACACS+ server and the TACACS+ accounting groups. 
Configuring the TACACS+ Authorization 
When configuring the TACACS+ authorization, you map CLI levels to TACACS+ privileges and define how 
command parameters/arguments are sent for authorization. 
 To configure the TACACS+ authorization: 
1. Navigate to configure management tacacsplus. 
The config>mngmnt>tacacsplus# prompt appears. 
2. At the config>mngmnt>tacacsplus# prompt, enter the commands as explained in the table 
below. 
Task 
Command 
Comments 
Define how command 
parameters/arguments are sent 
for authorization 
authorization-arguments {with-
command | separated} 
with-command (default) – 
The command is sent in a 
single message. 
separated – The command is 
sent in a message format 
compatible with Cisco ISE, 
with each argument clearly 
separated 
Mapping CLI Levels to TACACS+ 
Privilege Levels 
privilege-level <tacacs-privilege-
level> {su|oper|tech|user} 
The four CLI levels are su, 
oper, tech, user 
Removing the TACACS+ privilege 
level mapping 
No privilege-level <tacacs-
privilege-level> 
 
Configuring TACACS+ Server 
ETX-2i provides connectivity to up to five TACACS+ authentication servers. You must specify the 
associated server IP address, key, etc.  
 
Note 
If you intend to use TACACS+ for authentication, verify that TACACS+ is 
selected as a level-1 authentication method (refer to Access Policy in the 
Configuration and Management Methods chapter).  
ETX-2i Devices 
3. Management and Security 
 To configure a TACACS+ server: 
1. At the config>mngmnt>tacacsplus# prompt, enter server <ip-address> to specify the server IP 
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
group <group-name> 
See Configuring 
Accounting Groups below 
on how to define the 
accounting group. 
no group detaches 
accounting group from 
server. 
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
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
If you enter the password 
as a text string, do not 
use the hash parameter. 
Use it only if you are 
specifying the password 
as a hashed value 
(obtained by entering the 
info command to display 
TACACS+ data). 
Length: 1-80 characters 
Supported characters: 
Comma, space, ~, ?, “, !, 
#, $, %, &, ‘, (, ), *, +, `, -, 
_, ., /, :, ;, <, =, >, @, [, |, ], 
^, {, |, } 
Note: If “ is used in a key, 
the key must start and 
end with “. 
Setting priority of TACACS+ server  
priority <priority-value> 
priority-value – priority 
of server 
During authentication, 
device attempts accessing 
highest-priority TACACS+ 
servers, and if this fails, 
goes to next highest 
priority. 
Possible values: 1-254 
Note: You can also use 
the priority command 
when single server 
accounting is enabled, to 
determine the order in 
which to try the servers.  
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
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Displaying statistics 
show statistics 
 
Clearing statistics 
clear-statistics 
 
Configuring Accounting Groups 
 To configure accounting groups: 
1. At the config>mngmnt>tacacsplus# prompt, enter group <group-name> to configure an 
accounting group with the specified name.  
The config>mngmnt>tacacsplus>group(<group-name>)# prompt is displayed.  
2. Enter the necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Defining the accounting for the group 
accounting [shell] [system] 
[commands] 
You can enter any 
combination of the shell, 
system, or commands 
parameters, but you must 
enter at least one of 
them. 
Enter no accounting to 
disable TACACS+ 
accounting for the group. 
Sending accounting messages to a 
single server 
single-server-accounting 
Note: You can use the 
priority command, to 
determine the order in 
which to try the servers. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Configuring the time during which a 
nonresponding server should not be 
tried for authentication 
wait-to-restore-server 
This command is not 
configured by default. 
Possible values: 1-86400 
seconds. 
Note: If a server does not 
respond and the number 
of retries is exhausted, 
the server is considered 
as operationally down for 
the time configured. 
During this time the 
server must not be tried 
for authentication or 
authorization attempts. If 
the timer is active for all 
servers, the next 
authentication method 
(e.g., local) will be tried. 
If a server enters the 
wait-to-restore state, the 
tacacs_server_wtr event 
is generated. 
If a server which was 
previously in the wait-to-
restore state is disabled, 
deleted, or the timer 
expires, the 
tacacs_server_wtr_off 
event is generated. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Configuring the method by which 
servers are selected 
server-selection { priority | 
cached-first } 
Default: priority 
priority - The server with 
the highest configured 
priority (highest 
numerical value) will be 
selected. If there are 
multiple servers with the 
same configured priority, 
the one with the lowest 
IP address is selected. If 
the server does not 
respond for the 
configured number of 
retries, the server with 
the second highest 
priority is selected, and so 
on. 
cached-first - The last 
server that previously 
responded to an 
authentication or 
authorization attempt will 
be selected first. If the 
server does not respond 
for the configured 
number of retries, the 
priority method is used 
instead. 
3. Enter exit to return to the TACACS+ level. 
The config>mngmnt>tacacsplus# prompt is displayed. 
4. Enter server <ip-address> to select the TACACS+ server to which to bind the group. 
The config>mngmnt>tacacsplus>server(<ip-address>)# prompt is displayed.  
5. At the config>mngmnt>tacacsplus>server(<ip-address>)# prompt, enter group  
< group-name> to bind the previously defined accounting group to the TACACS+ server. 
ETX-2i Devices 
3. Management and Security 
Examples 
Defining Server 
The example below illustrates the procedure for defining a TACACS+ server. 
• 
Server IP address: 175.18.172.150 
• 
Key: TAC_server1 
• 
Priority: 6 
exit all  
configure management tacacsplus 
  server 175.18.172.150 
    key TAC_server1 
    priority 6 
    no shutdown 
exit all 
save 
 To display the configuration from the above example: 
ETX-2i# configure management tacacsplus server 175.18.172.150 
ETX-2i>config>mngmnt>tacacsplus>server(175.18.172.150)# info detail 
    key "244055BF667B8F89225048C6571135EF" hash 
    retry 1 
    timeout 5 
    authentication-port 49 
    accounting-port 49 
    no group 
    priority 6 
    no shutdown 
Defining Accounting Group 
The example below illustrates the procedure for defining an accounting group. 
• 
Group name: TAC1 
• 
Accounting: Shell, system, and commands 
• 
Bound to server defined above  
exit all 
configure management tacacsplus 
  group TAC1 
    accounting shell system commands 
    single-server-accounting 
    exit 
ETX-2i Devices 
3. Management and Security 
  server 175.18.172.150 
    group TAC1 
exit all 
 To display the configuration from the above example: 
ETX-2i# configure management tacacsplus server 175.18.172.150 
ETX-2i>config>mngmnt>tacacsplus>server(175.18.172.150)# info detail 
    key "244055BF667B8F89829AB8AB0FE50885" hash 
    retry 1 
    timeout 5 
    authentication-port 49 
    accounting-port 49 
    group "TAC1"  
    priority 6   
    no shutdown 
Mapping CLI Level to Privilege Level 
 To map TACACS+ level 7 to the CLI user level:  
ETX-2i# configure management tacacsplus privilege-level 7 user 
 To delete the mapping of TACACS+ level 7 to the CLI user level:  
ETX-2i# configure management tacacsplus no privilege-level 7  
Configuration Errors 
The following table lists the messages generated by ETX-2i when a configuration error is detected. 
Message 
Cause 
Corrective Action 
su level must be mapped to a 
TACACS+ level 
You tried removing the last 
mapping of su, but su must be 
mapped to at least one 
TACACS+ level. 
Leave at least one mapping of su. 
ETX-2i Devices 
3. Management and Security 
Viewing TACACS+ Statistics 
 To display TACACS+ statistics: 
• 
At the config>mngmnt>tacacsplus>server(<ip-address>)# prompt, enter: 
show statistics. 
The TACACS+ statistic counters are displayed (see table below).  
ETX-2i>config>mngmnt>tacacsplus>server(175.18.172.150)$ show statistics 
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
The number of authentications performed toward a specific TACACS+ server 
Request Timeouts 
The number of transaction timeouts that occurred between the client and server 
Unexpected 
Responses 
The number of times the TACACS+ client receives a TACACS+ packet that is not expected at 
that time. Usually, this occurs due to a delayed response to a request that has already 
timed out 
Server Error 
Responses 
The number of errors received from the TACACS+ server 
Incorrect 
Responses 
The number of times the TACACS+ client: 
• Fails to decrypt the packet  
• Detects an invalid field in the TACACS+ packet  
• Receives a response that is not valid according to the initial request 
Transaction 
Successes 
The number of successful transactions between the client and TACACS+ server 
Transaction 
Failures 
The number of times the TACACS+ client’s request is aborted by the TACACS+ server or the 
server fails to respond after maximum retry is exceeded 
Pending Requests 
The number of TACACS+ client’s requests minus number of TACACS+ server responses or 
timeouts 

## 3.4 Authentication via TACACS+ Using X.509 Certificates  *(p.730)*

ETX-2i Devices 
3. Management and Security 
 To clear TACACS+ statistics: 
• 
At the config>mngmnt>tacacsplus>server(<ip-address>)# prompt, enter:  
clear-statistics 
TACACS+ statistic counters are set to 0. 
3.4 Authentication via TACACS+ Using X.509 Certificates 
ETX-2i-10G devices supports X.509 providing a standard for public key certificates that are applied in 
various applications. In case of ETX-2i-10G devices, it is used for secure login via TACACS+ servers. 
Applicability and Scaling 
This feature is currently applicable to ETX-2i-10G products. 
Standards Compliance 
RFC 5280 - Internet X.509 Public Key Infrastructure Certificate. 
Factory Defaults 
N/A 
Functional Description 
X.509 certificates are used for initial authentication . 
X.509 certificates can be understood as ‘digital passports’. They link an identity such as a website’s 
domain, an organization or a specific user to a public key. This link is guaranteed by a trusted third party 
called CA (Certificate Authority), which digitally signs the certificate. 
 
 
ETX-2i Devices 
3. Management and Security 
X.509 certificates contain the following data fields: 
• 
Subject: The identity that is certified. 
• 
Issuer: The CA (Certificate Authority) that issues and signs the certificate. A CA can be a 
business, a government or an internal department that is responsible for issuing and managing 
digital certificates. 
• 
Public Key: The key used for encryption or signature verification. 
• 
Validity Period: The specific timeframe during which the certificate is trusted (start and end 
dates). 
• 
Signature: The CA’s encrypted hash, which proves the authenticity. 
Configuring the X.509 Login 
To configure the X.509 login, do the following: 
1. Navigate to config management login-user. 
The config>mngmnt>login-user prompt appears. 
2. Enter authentication-method x509. 
3. Import the certificates of the CAs (Certificate Authorities) you trust for signing certificates for 
SSH login. To do so, navigate to ETX-2i>config>crypto>pki and enter import-certificate 
certificate-name <certificate-name> [certificate-url <certificate-url> [fingerprint <fingerprint>]]. 
4. Define these CAs as trusted for approving SSH login. To do so, navigate to 
config>mngmnt>access>ssh-server and enter trusted-ca. 
5. If desired, add a certificate revocation check by entering revocation-check at the  
ETX-2i>config>crypto>ca(name) level. 
Configuring the Method to verify the Revocation Status of the X.509 Certificate 
 To configure the method to verify the revocation status of the X.509 certificate: 
1. Navigate to the relevant CA by entering configure crypto ca(name). 
2. At the ETX-2i>config>crypto>ca(name) prompt, define how the revocation status is verified by 
entering the following: 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Configuring the method to 
verify the revocation 
status of the certificate. 
revocation-check ocsp [none] 
• Currently, only ocsp is supported. OCSP 
stands for Online Certificate Status Protocol 
and verifies the revocation status of a digital 
certificate in real-time. 
• If the second method is none and a CA is not 
accessible, the certificate is accepted without 
revocation check, if it is otherwise valid. 
If no second method is specified and a CA is 
not accessible, the certificate is not accepted 
even if it is otherwise valid. 
• If a CA is accessible, the OCSP verdict 
(revoked or not) is final, and the second 
method is not called. 
Specifying the location of 
the OCSP protocol. 
ocsp <URL> 
Enter the URL of the OCSP protocol. 
Configuring the X.509 Infrastructure 
 To generate and configure the public key pair: 
1. Navigate to the relevant CA by entering configure crypto key. 
2. At the ETX-2i>config>crypto>key prompt, generate and view the public key pair as follows: 
Task 
Command 
Comments 
Generating the public key 
pair 
generate key-name <key-name> type 
{ecdsa size {256 | 384 | 521} | rsa size 
{2048 | 3072 | 4096}} [application {x509 
| sftp-client [no-activation] | ssh [no-
activation] | sftp-client ssh [no-
activation]}] 
 
Displaying the public key 
show public-key 
• This command lists all the public 
keys configured for the device. 
• This command is not saved in the 
configuration file. 
 
 
ETX-2i Devices 
3. Management and Security 
 To issue X.509-certificate related commands: 
1. Navigate to the relevant level by entering configure crypto pki. 
2. At the ETX-2i>config>crypto>pki prompt, issue X.509-certificate related commands as explained 
in the table below. 
Task 
Command 
Comments 
Importing a CA certificate 
authenticate certificate-name 
<certificate-name> [certificate-url 
<certificate-url> [fingerprint 
<fingerprint>]] 
• This command is not saved in the 
configuration file. If the device 
reboots after issuing this command 
and before the CA certificate was 
imported, the user has to run the 
command again. 
• The certificate must be PEM 
encoded (ASCII base 64); CER 
formatting is commonly used, but 
other formats (e.g. CRT) work as 
well. 
• The certificate may only contain 
printable characters. 
Enrolling a certificate 
enroll [use-key <key-name>] 
[certificate-url <certificate-url>] 
[certificate-name <certificate-name>]  
[common-name <cn>] [locality 
<locality>] [state <state>] [email 
<email>] [organization <org>] 
[organizational-unit <ou>] [country 
<country>] [challenge-password 
<password>] [serial-number {dmi | 
value <serial-number>}] 
• This command is not saved in the 
configuration file. If the device 
reboots after issuing this command 
and before the CA certificate was 
imported, the user has to run the 
command again. 
If the CN (common name) is not 
specified, the device uses 
hostname.ip-domain-name  
hostname is a device MAC address 
by default, but may be configured 
with a namesake command at the 
config>system level.  
Displaying the certificate 
in ASCII Base 64 format 
show certificate certificate-name 
<certificate-name> 
 
Define the type of 
certificate to be displayed 
show certificate-summary [owner {self 
| ca}] [valid-only | invalid-only] 
 
Deleting the certificate 
delete-certificate certificate-name 
<certificate-name> 
 

## 3.5 DHCP Layer-2 Relay  *(p.734)*

ETX-2i Devices 
3. Management and Security 
3.5 DHCP Layer-2 Relay 
ETX-2i supports DHCP Layer-2 relay for receiving, intercepting, and forwarding DHCP requests and 
replies not destined to the device itself.  
Note 
Packets sent from or to the device itself are not related to the DHCP relay 
functionality.  
Applicability and Scalability 
A device can function as a DHCP client, relay, and server at the same time on different interfaces.  
Only one DHCP entity (client, relay, or server) can function on a single interface. 
DHCP relay applies to DHCPv4 only. 
Standards Compliance 
[RFC 1542] – Clarifications and Extensions for the Bootstrap Protocol 
[RFC 2131] – Dynamic Host Configuration Protocol 
[RFC 2132] – DHCP Options and BOOTP Vendor Extensions 
[RFC 3046] – DHCP Relay Agent Information Option 
Functional Description 
An ETX-2i device, configured to function as a DHCP relay agent at Layer-2 functions over ETX-2i Layer-2 
services (Bridge) and performs the following functionalities:  
• 
DHCP Snooping – verifies DHCP transactions and protects against rogue DHCP servers and 
clients 
• 
DHCP Option 82 – adds information to the DHCP request, including Remote ID and Circuit ID 
The above DHCP Layer-2 Relay features can be configured on a device or on specific services. When the 
DHCP relay feature is configured on a particular service, it is applied to all flows associated with that 
service. For example, in a bridge, all flows related to the same VLAN are typically associated with the 
ETX-2i Devices 
3. Management and Security 
same service. Enabling DHCP relay for that service applies the DHCP relay to all flows related to that 
service. 
The following table [per RFC 2131] describes the various DHCP client and server messages: 
Message 
Use 
Sent By 
DHCPDISCOVER 
Locate available servers. 
Client 
DHCPOFFER 
Offer configuration parameters in response to DHCPDISCOVER. 
Server 
DHCPREQUEST   
Accept, confirm, or extend an offer, implicitly declining others. 
Client 
DHCPACK 
Commit client request. 
Server 
DHCPNAK 
Decline client request. 
Server 
DHCPDECLINE 
Indicate that the committed address is already in use. 
Client 
DHCPRELEASE 
Relinquish address and cancel remaining lease. 
Client 
DHCPINFORM 
Ask for configuration; address has been externally configured. 
Client 
DHCP Snooping 
ETX-2i supports Layer-2 DHCP snooping, for verification of DHCP transactions and protection against 
rogue DHCP servers. DHCP Snooping uses the concept of trusted and untrusted ports to filter DHCP 
packets received by the switch.  
If DHCP snooping is enabled, ETX-2i supports the configuration of each port through which DHCP 
packets can be received and sent (Ethernet, internal Ethernet, LAG, Logical MAC, and PCS), as DHCP 
trusted or untrusted (refer to the Cards and Ports chapter - configuration of dhcp-trust parameter in 
Ethernet, LAG, Logical MAC, and PCS ports). Packets from servers and relay ports should be set as 
trusted, and client ports set to untrusted.  
ETX-2i supports enabling and disabling DHCP snooping, for the entire device or a specific service. If it is 
enabled for a device, snooping applies to all services, regardless of the service-specific configuration. If it 
is not enabled for the device, snooping applies only to those services for which it is explicitly enabled.  
DHCP servers are assumed to reside in trusted locations, usually behind network ports, while DHCP 
clients reside in untrusted locations, usually behind user ports.  
 
 
ETX-2i Devices 
3. Management and Security 
In addition to verifying the validity of incoming DHCP messages, when enabled, the DHCP relay does the 
following: 
• 
Drops server DHCP messages (DHCPOFFER, DHCPACK, and DHCPNACK) arriving from untrusted 
ports; allows from trusted ports. 
• 
Drops client DHCP messages (DHCPDISCOVER, DHCPREQUEST, DHCPDECLINE, DHCPRELEASE and 
DHCPINFORM) when they arrive from trusted ports; allows from untrusted ports. 
• 
Forwards DHCP server packets only to untrusted ports and DHCP client packets only to trusted 
ports. 
Untrusted
DHCP Server
DHCP Snooping Enable
Switch
Trusted
ETX-2i
DHCP Pseudo-server
DHCP Client
ETX-2i
Untrusted
DHCP Reply from DHCP Server
DHCP Reply from DHCP Pseudo-server
 
DHCP Information Option - Option 82  
ETX-2i supports the DHCP relay agent information option – Option 82, which adds information to DHCP 
requests.  
This additional information includes: 
• 
Circuit ID – Port ID of the switch from which the request was received; locally unique. Can be 
one of the following, according to configuration (default or user): 
 
VLAN (0-4095), card number, and port number from which the client DHCP packet was 
received (the default) 
 
text string 
• 
Remote ID - agent identification; globally unique. Can be one of the following, according to 
configuration (default or user): 
 
MAC address (default) - MAC address of the port from which the client DHCP packet was 
received. If this MAC address doesn’t exist, it is the lowest MAC address that the device 
owns. 
 
Hostname – system name 
 
Text string 
 
SNMP Engine ID – MAC address of the entire unit (common to several ports). 
ETX-2i Devices 
3. Management and Security 
Circuit ID and Remote ID can be configured in two flavors (formats): 
• 
short-format – Circuit ID and Remote ID do not include the suboption type and length. 
• 
long-format – the default; Circuit ID and Remote ID include the suboption type and length. 
 
Notes 
• 
It is possible to enable DHCP option 82 sub-options (Circuit ID and Remote 
ID) for the entire device, as well as for specific services. This means that if 
there is a service-specific configuration it is used; otherwise, the global 
configuration applies. 
• 
You cannot disable option 82 on a specific service if it is globally enabled. 
• 
DHCP Option 82 is relevant for regular classifiers only; not port classifiers. 
The figure below describes the flow of DHCP packets through a relay when option 82 is enabled.  
1. The DHCP client broadcasts a DHCP request. 
2. The DHCP relay agent intercepts the request, and performs a sanity check on the packet. 
3. If it is not valid, it discards the message. 
4. Otherwise, if it is valid, DHCP relay agent adds Option 82 (Remote ID and Circuit ID) to DHCP 
request and broadcasts it toward the DHCP server.  
5. DHCP server uses the appended information (Circuit ID and Remote ID) for the IP address 
allocation scheme, statistics and more. 
6. Based on the appended information, the DHCP server returns the DHCP request with the proper 
IP address and policies. 
7. DHCP relay agent performs a sanity check on the packet and strips option 82 (Remote ID and 
Circuit ID fields) off the packet before forwarding the packet to the client. 
 
ETX-2i Devices 
3. Management and Security 
Factory Defaults 
By default, no DHCP relay parameters are configured for ports. The system DHCP relay parameters have 
the default values shown in the following table. 
Parameter 
Default  
Remarks 
dhcp-option-82 
no dhcp-option-82 
 
dhcp-snooping 
no dhcp-snooping 
 
circuit-id 
vlan-card-port 
 
remote-id 
mac 
 
Configuring DHCP Layer-2 Relay  
 To configure DHCP Layer-2 Relay parameters: 
1. Navigate to configure system dhcp-relay. 
The config>system>dhcp-relay# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Enabling 
DHCP 
option 82 
dhcp-option-82 { all | service 
<service-name> } [circuit-id 
{hostname-svlan-cvlan-card-
port ascii | string <circuit-id-
string> | vlan-card-port 
[ascii]}]  
[remote-id { chassis-mac ascii 
| hostname | mac [ascii] | 
snmp-engine-id | string 
<remote-id-string> } [short-
format] 
no dhcp-option-82 { all | 
service <service-name> } 
service – the service on which to enable option 82 
Possible values: all (all services), service name (1-31 characters) 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
circuit-id – circuit ID format 
Possible values:  
hostname-svlan-cvlan-card-port ascii – comprises the hostname, 
SVLAN, CVLAN, card number, and port number, from which the 
client DHCP packet was received. 
string <circuit-id-string> – 1-253 character ASCII string; default 
empty string 
vlan-card-port [ascii] – hexadecimal (the default) or ASCII string 
comprising CVLAN (two bytes), card number (one byte), and port 
number (one byte), from which the client DHCP packet was 
received 
remote-id – remote ID formatPossible values:  
chassis-mac ascii – device chassis MAC address (ASCII string, 17 
bytes formatted 0A:0A:0A:0A:0A:0A (letters are capital)). If there 
is more than one address, the lowest is used.  
hostname – device sysName 
mac – the default; MAC address of the port (hexadecimal, six 
bytes) from which the client DHCP packet was received. If the 
port does not have a MAC address (e.g., in bridge application), 
the lowest MAC address the device owns is used. 
mac ascii - MAC address of the port from which the client DHCP 
packet was received (ASCII string, 17 bytes formatted 
0A:0A:0A:0A:0A:0A (letters are capital)). If the port does not have 
a MAC address (e.g., in bridge application), the lowest MAC 
address the device owns is used  
snmp-engine-id – The device snmpEngineID; defines the MAC 
address of the entire unit (common to several ports) 
string <remote-id-string>} – 1-253 character ASCII string, 
configured by the user; default empty string 
circuit-id and remote-id can be configured in two flavors 
(formats): 
• short-format – circuit-id and remote-id do not include the 
suboption type and length. 
• long-format – the default; circuit-id and remote-id include 
the suboption type and length 
Note: 
• You repeat the command for each service that you configure. 

## 3.6 DHCP Server  *(p.740)*

ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
• If hostname is chosen, if SNMP sysName is > 253 characters, 
or if SNMP sysName > 253 characters is configured while it is 
in use by option 82, the following message is displayed: Only 
first 253 characters of hostname are used in DHCP option 82 
remote ID. Similarly, only first 253 characters of Circuit ID 
string, Remote ID string, and SNMP engine ID are displayed. 
• Option 82 suboptions format can be configured for a specific 
service to be different from the global configuration; 
however, option 82 cannot be disabled on a specific service if 
it is globally enabled.  
• Both circuit-ID and remote-ID suboptions are always sent if 
option 82 is enabled.  
Enabling 
DHCP 
snooping 
[no] dhcp-snooping { all | 
service <service-name> } 
service – the service on which to enable snooping.  
Possible values: all, service name (1-31 characters) 
all – All ports traffic is subjected to snooping functionality. 
3.6 DHCP Server 
ETX-2i supports Dynamic Host Configuration Protocol (DHCP) server functionality for IPv4 clients. Based 
on the Bootstrap Protocol (BOOTP), DHCP server assigns to DHCP clients IPv4 addresses from configured 
pools, as well as various configuration parameters (DHCP options), in response to the broadcast 
requests of DHCP clients. In addition, DHCP relays can negotiate DHCP information on behalf of a client, 
if the client and server are not directly connected. This functionality eliminates the need to manually 
assign an IP address for each potential client. 
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
can even start a Zero Touch configuration process, which completely configures the client 
without network manager intervention. 
ETX-2i Devices 
3. Management and Security 
• 
Centralized management – Network managers only need to configure a single central server. If a 
global parameter, e.g., DNS server, is changed, there is no need to manually configure all the 
clients in the network. 
Note 
Device can function as DHCP server, relay, and client at the same time. 
Applicability and Scaling 
This feature is applicable to ETX-2i with an embedded router and ETX-2i with a bridge. 
Relevant for DHCPv4 server. 
You can configure a single DHCPv4 server on any VRF (router instance). 
DHCP server is not supported on tunnel interfaces. 
Standards Compliance 
[RFC 951] – Bootstrap Protocol 
[RFC 1542] – Clarifications and Extensions for the Bootstrap Protocol (relay agent requirements) 
[RFC 2131] – Dynamic Host Configuration Protocol 
[RFC 2132] – DHCP Options and BOOTP Vendor Extensions (basic DHCP options) 
[RFC 3046] – DHCP Relay Agent Information Option (DHCP option 82) 
Functional Description 
The following describes the DHCP flow, from the time the client sends a broadcast DHCP request and 
until the IP addresses are distributed. If the client and server are not directly connected to each other, 
the DHCP messages can be forwarded by a DHCP Layer 2 or Layer 3 relay agent. Otherwise, DHCP Layer 
2 and Layer 3 are not relevant; skip steps 2 and 5. 
1. The DHCP client sends to the DHCP server a broadcast DHCP request. 
2. The DHCP relay agent (if one exists) intercepts the request, optionally inserts the relay agent 
information option (option 82) into the packet and broadcasts it toward the DHCP server. 
3. Any listening DHCP server can assign an IP address to the DHCP client (based on Option 82 
information sent by the client or relay agent), as well as other options. Before assigning an IP 
ETX-2i Devices 
3. Management and Security 
address, the server pings it. If a reply is received, this means the address is a conflict, meaning it 
is an address that is already occupied. The conflict enters the conflicts table.  
4. DHCP server sends back to the client a lease offer, containing an IP address and possibly other 
parameters. It sends its IP address in option 54 (server identifier) to the client. 
 
Note 
If the DHCP server offers a lease and the client then sends a DHCP request 
with an IP address of a different server (in option 54), the server assumes that 
the request is no longer relevant, and return the offered address to the pool of 
available addresses.  
5. The relay agent (if one exists) strips Option 82 from the packet (if one exists), and then forwards 
the lease offer to the client. 
6. The DHCP client accepts the offer. If the DHCP client received more than one lease offer, it 
chooses a lease; usually the first one it received. 
7. Before accepting a lease, a typical client sends a gratuitous ARP to the IP address it is about to 
use. If two replies are received, the client should decline the lease, and the server places the IP 
address into the conflicts table. 
8. The server acknowledges the lease.  
ETX-2i saves the lease in a database that includes all active and inactive leases. The lease database with 
address binding (IP address to client hardware address) resides in permanent memory that withstands 
reboot. If possible, ETX-2i assigns to clients the same IP addresses that they previously had.  
The lease is usually granted for a limited time; therefore, the DHCP client should renew it before it 
expires. A DHCP client may also release a lease once is no longer needed. 
The server does not delete a binding from the database when a lease expires. However, if a new client 
asks for an address and the server does not have a free address, then one of the unused addresses from 
the database may be used.  
The server also saves a table of conflicts. A conflict is an IP address that the server tried to assign but 
found out it is already occupied. The server does not assign an address from the conflicts table unless all 
non-conflicting addresses belong to active leases. 
If you change the configuration so that it renders active leases invalid (such as changing a pool’s range of 
addresses or network, excluding an address), the server removes the leases from the binding database. 
Addresses in the conflict database, which are no longer valid, are also removed. 
The device may function as DHCP client, relay, or server at the same time.  
ETX-2i Devices 
3. Management and Security 
DHCP Options 
The following Tx options (i.e., sent from server to client) are supported by RAD DHCP server and RAD 
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
The following Rx options (i.e., sent from client to server) are supported by RAD DHCP server and RAD 
clients: 
• 
Lease time (51) – requested lease time 
• 
Server identifier (54) – IP address of the server whose offer is accepted (also used by clients to 
send unicast messages to the server) 
• 
Client identifier (61) – client unique identifier (typically MAC address) 
The following Rx options are supported by RAD clients, but ignored by RAD DHCP server: 
• 
Hostname (12) – client hostname 
• 
Vendor class identifier (60) – client vendor identifier 
Note 
• 
Options 66 (TFTP server name), 67 (boot file name), and 150 (TFTP server 
address) are not supported by RAD DHCP server although RAD clients use 
them for the Zero Touch configuration process. 
• 
Unsupported received DHCP options are ignored. They do not invalidate a 
request.  
Manual Bindings 
In cases when it is important that a client, usually a router or server, not change its address, it is possible 
to configure manual bindings, i.e., IP addresses that are manually mapped to clients. This directs the 
server to grant fixed addresses to specific clients (usually recognized by their MAC address). 
ETX-2i Devices 
3. Management and Security 
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
If the offered lease time is infinite, this option is not sent. Otherwise, it is set to the default, 
which is 0.5 of the lease time. 
• 
Rebinding (T1) time value (59) – Time (in seconds) at which the client should transition to the 
rebinding state.  
 
If the offered lease time is infinite, this option is not sent. Otherwise, it is set to the default, 
which is 0.875 of the lease time. 
• 
Server identifier (54) – IP address of the server,  
• 
Any of the following options, if configured: 
 
Default router (3) – one or two IP addresses 
 
DNS server (6) – one or two IP addresses 
 
Domain name (15) – a string 
 
NetBIOS name server (14) – one or two IP addresses. 
 
NetBIOS node type (46) – b, p, m, or h 
• 
Relay agent information option (82). 
 
If the relay information option was received from the client, the server sends it back. 
• 
The end option (255) – Marks the end of valid information in the vendor field. 
Factory Defaults 
By default, no DHCP server or DHCP server pool is defined. When a DHCP server or DHCP server pool is 
first defined, it is configured as shown below. 
ETX-2i Devices 
3. Management and Security 
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
No pool 
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
Configuring DHCP Server 
You can configure the DHCP server as follows: 
1. Globally enable DHCP server functionality (the default). 
2. By default, no DHCP server exists. Create a single instance of DHCP server over any one of the n 
VRFs supported in the ETX-2i embedded router. 
3. Exclude addresses that should never be assigned to clients; typically addresses that are statically 
configured on servers or routers. 
ETX-2i Devices 
3. Management and Security 
4. Configure DHCP pools containing: 
 
Range of addresses (or a single address) to assign to clients 
 
Various DHCP options to send to clients 
 
Definitions of clients eligible to get lease from the pool 
Host and subnetwork inherit options from larger networks (simplifying the configuration): 
• 
For example, a global pool (e.g., 192.168.0.0) can contain global options, such as domain name. 
• 
Additional pools are set for subnets (e.g., 192.168.1.0 and 192.168.2.0), each with its own 
default gateway. 
 To configure the DHCP server: 
1. Navigate to configure system [no] dhcp-server [<number>}. 
The config>system>dhcp-server (<number>)# prompt is displayed. 
Note 
• 
<number> is the number of the dhcp-server, which can only be 1.  
• 
Enter no dhcp-server to remove the DHCP server from the router.  
2. At the config>system>dhcp-server (1)# prompt, enter the necessary commands according to 
the tasks listed below. 
Task 
Command 
Comments 
Binding DHCP server to router 
bind router <number> 
number – router (VRF)  number 
Note: The DHCP server works only on 
the router to which it is bound. If the 
bound router does not exist, the 
DHCP server is idle. 
Clearing DHCP server bindings, 
conflicts, or statistics 
clear { binding { address <ipv4-
address> | all} | conflict { address 
<ipv4-address> | all } } 
• You can clear the entire DHCP 
server binding database, or 
binding of a specific address. 
• When clearing a specific address, 
if ipv4-address does not exist in 
the database, an error message is 
generated:  
No such address. 
• You can clear the entire conflicts 
database, or a specific conflicting 
address. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
• Clearing all conflicts clears both 
abandoned (declined by clients) 
and blocked (already in use) 
addresses. 
Configuring the IP address that 
is not to be offered to a client 
[no] exclude-address <ipv4-
address> 
A single address to be excluded can 
be configured per command.  
Repeating this command adds new 
excluded addresses; it does not 
replace previous excluded addresses. 
Note: Excluded addresses are 
typically addresses that are statically 
configured on servers or routers. 
Configuring DHCP server pool 
[no] pool 
See Configuring DHCP Server Pool. 
Entering no pool removes the DHCP 
server pool and the configuration 
related to it (IP address ranges and 
DHCP options). 
Displaying DHCP server bindings 
show binding 
See Viewing DHCP Server Binding. 
Displaying DHCP server conflicts 
show conflict 
See Viewing DHCP Server Conflict. 
Displaying DHCP server statistics 
show statistics 
See Viewing DHCP Server Statistics. 
Disabling/enabling DHCP server 
functionality 
[no] shutdown 
DHCP server functionality is enabled 
by default. 
Note:  
• The DHCP relay and client 
functions are not affected by this 
command. 
• When disabled, the rest of the 
server configuration is ignored. 
Configuring DHCP Server Pool 
By default, no DHCP server pool exists. The following procedure describes how to create a DHCP server 
pool. Each pool must be assigned a unique name.  
The DHCP server offers leases based on the pools’ configurations.   
ETX-2i Devices 
3. Management and Security 
 To configure the DHCP server pool: 
1. Navigate to configure system [no] dhcp-server pool [name]. 
The config>system>dhcp-server>pool# prompt is displayed. 
2. At the config>system>dhcp-server>pool# prompt, enter the necessary commands according 
to the tasks listed below. 
Note 
• 
Entering no pool removes the DHCP server pool, as well as the 
configuration related to it. 
• 
You must assign a unique pool name of 1 to 80 characters.  
 
Task 
Command 
Comments 
Configuring range of IP 
addresses that server can assign 
to clients  
(relevant only for pool bound to 
network) 
[no] address-range <start-ip> <end-
ip> 
start-ip – lowest IPv4 address of the 
range 
end-ip – highest IPv4 address of the 
range 
Note: 
• An address range can be 
configured only if the pool is 
bound to a network. It is 
irrelevant if the pool is bound to a 
host. 
• The address range must be inside 
the pool’s subnet (configured 
with the network command). 
• You can configure address ranges 
with any prefix length. However, 
since the device cannot handle 
very large address ranges (prefix 
length less than 16 bits), only the 
first /16 addresses are used. 
• If no range is configured, the 
default value is the entire subnet 
of the pool. 
• A single range can be configured 
per pool. 
• Entering no address-range <start-
ip> <end-ip> deletes an existing 
range. If the specified range is not 
exactly the one configured by the 
command, range is not deleted. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Configuring client identifier 
(DHCP option 61) 
client-identifier <unique-identifier>  
no client-identifier 
Client identifier (option 61) is used 
for manual binding, i.e., assigning a 
preconfigured IP address to a specific 
client. 
unique-identifier – client identifier; 
1-255 character-string 
Note: 
• Client identifier can be configured 
only if the pool is bound to a host 
(entering host command). 
• If the command is repeated, it 
replaces the previous one. 
• Either client identifier or 
hardware address can be 
configured; not both. 
• You cannot configure a client 
identifier already configured on 
another pool. 
• Entering no client-identifier 
removes the client identifier from 
the pool.  
Configuring default router 
(DHCP option 3) 
default-router <address> 
[<address-2>] 
no default-router 
address – default router IPv4 address 
address-2 – second default router 
IPv4 address 
Note:  
• Repeating this command replaces 
the previous one. 
• address-2 must be different than 
address-1. 
Configuring DNS server (DHCP 
option 6) 
dns-server <address> [<address-2>] 
no dns-server 
address – DNS server IPv4 address 
(mandatory) 
address-2 – second DNS server IPv4 
address (optional) 
Note:  
• Repeating this command replaces 
the previous one. 
• address-2 must be different than 
address-1. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Configuring domain name 
(DHCP option 15) 
domain-name <domain> 
no domain-name 
domain – domain name; 1-255-
character string 
Note: Repeating this command 
replaces the previous one. 
Configuring client hardware 
address (MAC address) 
hardware-address <mac-address> 
no hardware-address 
MAC address is used for manual 
binding, i.e., assigning a 
preconfigured IP address to a specific 
client. 
mac-address – client MAC address 
Note:  
• The hardware address can be 
configured only if the pool is 
bound to a host (configured with 
the host command). 
• Repeating this command replaces 
the previous one. 
• Either client identifier or 
hardware address can be 
configured; not both.  
• You cannot configure a hardware 
address already configured on 
another pool. 
Configuring client IP address and 
prefix length 
host <ipv4-address>/<prefix-
length> 
no host 
• ipv4-address – client IPv4 address 
• prefix-length – client IP prefix 
length 
Possible values: 1-32 
Note:  
• If no host is invoked while client 
identifier or hardware address is 
configured, the device deletes 
the configured client identifier or 
hardware address. 
• Repeating this command replaces 
the previous one. 
• Either the host or network 
command can be configured; not 
both.  
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
• The address (while taking into 
account the prefix length) must 
be a unicast address. 
• The same pair of address and 
prefix length may not be 
configured on more than one 
pool. 
• The mask (reflecting the prefix 
length) is passed to the client in 
option 1. 
Configuring lease default validity 
time (DHCP option 51) 
lease-default { time <days> 
[<hours> [<minutes>]] | infinite } 
no lease-default 
Possible values: 60-8640000 seconds 
(100 days); infinite (lease never 
expires unless the client releases it.) 
Note: 
• If you configure lease validity 
time to between 60 and 8640000 
(100 days) seconds, the server 
grants it. 
• If you configure less than 60 
seconds, the server offers 60 
seconds. 
• If you configure more than 
8640000 seconds, the server 
offers 8640000 seconds. 
• If the client does not send option 
51, i.e., it does not state for how 
much time it requires the lease, 
the server offers the default lease 
time (one day, unless otherwise 
configured). 
• Repeating this command replaces 
the previous one. 
Configuring NetBIOS name 
server (DHCP option 44) 
netbios-name-server <address> 
[<address-2>] 
no netbios-name-server 
address – NetBIOS name server IPv4 
address 
address-2 – Second NetBIOS name 
server IPv4 address 
Note: Repeating this command 
replaces the previous one. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Configuring NetBIOS node type 
(DHCP option 46) 
netbios-node-type <type> 
no netbios-node-type 
Type – NetBIOS node type 
Possible values: b, p, m, h 
Note: Repeating this command 
replaces the previous one. 
Configuring client network IPv4 
address and mask 
network <ipv4-address>/<prefix-
length> 
no network 
Ipv4-address – client IP address 
Prefix-length – client IP prefix length 
Possible values: 1-32 
Note:  
• If the network is deleted or 
changed in such a way that the 
configured ranges are not in it, 
the device deletes the ranges 
that are out of the newly 
configured network. 
• Repeating this command replaces 
the previous one. 
• Either the host or network 
command can be configured; not 
both.  
• The IP address (while considering 
the prefix length) must be a 
subnet address. 
• You can configure network 
ranges with any prefix length. 
However, since the device cannot 
handle very large network ranges 
(prefix length less than 16 bits), 
only the first /16 addresses are 
used. 
• The same pair of address and 
prefix length cannot be 
configured on more than one 
pool. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Configure relay agent 
information (DHCP option 82) 
relay-information circuit-id <circuit-
id> 
relay-information remote-id 
<remote-id> 
no relay-information 
Matching the received option 82 
with the configuration determines 
the clients that can receive offers of 
the pool. 
Note:  
• Repeating this command replaces 
the previous one. 
• Either circuit-id or remote-id can 
be specified, as only one of them 
can be matched with received 
option 82. 
• Option 82 cannot be matched 
with a hex pattern. 
• The relay agent information 
option can be configured only if 
the pool is bound to a network. 
• The same pair of address and 
prefix length cannot be 
configured on more than one 
pool. 
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
Counter 
Description 
IP Address 
Lease IPv4 address 
ETX-2i Devices 
3. Management and Security 
Counter 
Description 
Binding State 
Binding state. 
Possible values: free, offered, active, expired, released, abandoned, 
permanent, bootp, blocked 
Bound to MAC 
Client MAC address 
Possible values: MAC address, formatted xx:xx:xx:xx:xx:xx 
Bound to ID 
Client ID 
Possible values: Hex string. Readable characters are printed as is; for 
non-readable, the hex value is printed preceded by 0x; for example: 
0x01 rad111. 
Lease Time 
Lease time in seconds 
Expires At 
Lease expiration date and time, formatted as other date and time 
parameters in the device 
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
 
Counter 
Description 
IP Address 
Conflict IPv4 address 
ETX-2i Devices 
3. Management and Security 
Counter 
Description 
Expires in 
Time (in seconds) remaining before the conflict expires 
Possible values:  
--  –  if there is no expiration time, such as for blocked addresses 
number – if there is an expiration time, such as for abandoned 
addresses 
Viewing DHCP Server Statistics 
You can display the DHCP server statistics. 
 To display the DHCP server statistics: 
• 
At the config>system>dhcp-server# prompt, enter show statistics. 
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
ETX-2i Devices 
3. Management and Security 
Configuration Errors  
The following table lists the messages generated by ETX-2i when a configuration error is detected. 
Message 
Cause 
Corrective Action 
The router is already bound to 
DHCP server 
 
 
No such address 
You tried clearing an IPv4 
address that does not exist in 
the database. 
Make sure the address is in the 
database. 
The pool is not bound to network 
You tried to configure a range 
of addresses for a pool that has 
not been bound to a network. 
Bind the pool to a network using the 
network command.  
You tried to configure the relay 
agent information option for a 
pool that has not been bound 
to a network. 
Range is not inside the pool’s 
network 
You tried to configure a range 
that is not in the pool’s subnet.  
Configure a range inside the pool’s 
subnet, using the network command. 
Range is already configured 
You can only configure a single 
range per pool. You already 
configured a range for the pool. 
Delete the existing address range and 
then configure a new range. 
Range does not exist 
You tried to delete an address 
range that is not exactly the 
same as the one configured.  
Delete the exact address range that you 
configured. 
The pool is not bound to host 
You tried to configure a 
network while a host is 
configured. 
Unbind the pool from the network and 
bind it to a host using the host 
command.  
You tried to configure a client 
identifier (option 61) or 
hardware address (MAC) for a 
pool that is not bound to a 
host.  
Bind the pool to a host using the host 
command. 
Cannot have both client-identifier 
and hardware-address 
You configured a client 
identifier when a hardware 
address is already configured, 
or vice versa. 
Remove the client identifier or hardware 
address configuration. 

## 3.7 DSCP Marking of Management Traffic  *(p.757)*

ETX-2i Devices 
3. Management and Security 
Message 
Cause 
Corrective Action 
Client identifier configured on 
different pool 
You tried to configure a client 
identifier that has already been 
configured on another pool. 
Configure a unique client identifier. 
Hardware address configured on 
different pools. 
You tried to configure a 
hardware address that has 
already been configured on 
another pool. 
Configure a unique hardware address. 
The pool is bound to network 
You tried configuring a host 
while pool was bound to a 
network. 
Unbind the pool from the network. 
Invalid address or prefix length 
You entered a non-unicast 
address. 
Enter a valid unicast address 
(considering the prefix length). 
Address and prefix configured on 
another pool 
You configured the same pair of 
address and prefix length on 
another pool. 
Configure a unique address and prefix 
length pair. 
The pool is bound to host 
You tried configuring a network 
while pool was bound to a host. 
Unbind the pool from the host. 
Invalid address or prefix length 
In case of a host: You entered a 
non-unicast address.  
Enter a valid unicast IP address 
(considering the prefix length). 
In case of a network: You 
entered a non-subnet address. 
Enter a valid subnet IP address (while 
considering the prefix length). 
3.7 DSCP Marking of Management Traffic 
ETX-2i supports configuring a specific DSCP value for marking management traffic. 
Management packets transmitted by the router have a configurable DSCP value, so that each router 
entity can control its traffic priority by setting its DSCP value for its management protocols. Supported 
protocols include ICMP, TFTP, Telnet Client, SNMP, SNTP, Syslog, TACACAS+, RADIUS, and SSH (SFTP). 
ETX-2i does not support the DSCP value on ping replies (part of ICMP protocol), and therefore when the 
device receives a ping message, it does not reply with the configured DSCP value.  
Note 
This section describes configuring the DSCP value for management packets. 
Refer to Configuring the Router in the Traffic Processing chapter to configure 
the DSCP value for control packets.  

## 3.8 Minimum Access Level  *(p.758)*

ETX-2i Devices 
3. Management and Security 
Applicability and Scaling 
This feature is applicable to all ETX-2i products. 
Configuring DSCP Marking  
 To configure the management DSCP value: 
1. Navigate to configure management. 
2. Enter dscp <dscp-value>. dscp-value can be 0-63. 
3.8 Minimum Access Level 
Users at the su level can change the predefined default minimum level authorized to execute a CLI 
command. For example, a user can limit the ‘save’ command for su rather than su and oper (the 
default). 
Applicability and Scaling 
This feature is applicable to all ETX-2i products. 
The access-level command is applicable, as follows: 
• 
Configurable by ‘su’ level users only. 
• 
Minimum access level is configurable on a full path command only.  
• 
Minimum access level command cannot be set on the ‘no’ form of the command.  
For example: admin access-level command “configure port ethernet no shutdown” min-level 
su is illegal. The user should enter the legal command:  
admin access-level command “configure port ethernet shutdown” min-level su   
• 
For show commands: The user must type show at the start of the full path. For example:  
admin access-level command “show configure port ethernet status” min-level su 
 
 
ETX-2i Devices 
3. Management and Security 
• 
When you set the minimum level of a command, all its sub-commands are set to that same 
minimum. For example: admin access-level command “configure port ethernet” min-level su 
sets all the commands under ethernet port to the minimum access level of su. 
• 
It is possible set the minimum access level and then to exclude some commands from that 
minimum access level and set to another minimum. For example: 
admin access-level command “configure port ethernet” min-level su 
admin access-level command “show configure port ethernet status” min level user 
Standards Compliance 
NA 
Functional Description 
Users at a level below the authorized level (minimum level) are not able to execute the command, as 
described in the following table:  
Authorized level  
User levels that can execute the command  
su 
su 
oper 
oper, su 
tech 
tech, oper, su 
user 
All levels - user, tech, oper, su 
Factory Defaults 
Each command has its own default minimum level. 
 
 
ETX-2i Devices 
3. Management and Security 
Configuring Access Level Command 
 To configure the minimum access level of a command: 
1. Navigate to admin. 
2. At the admin# prompt,  
enter access-level command <command> min-level {su|oper|tech|user}. 
Where  
command can be any CLI command (that is not in its no form).  
min-level is the minimum level allowed to execute the command. 
 To return a command to its default minimum access level: 
1. Navigate to admin. 
2. At the admin# prompt, enter no access-level command <command>. 
Examples 
save command is supported for su access level only: 
ETX-2i# admin access-level command "save" min-level su 
copy command is supported for tech, su, and oper access levels only: 
ETX-2i# admin access-level command "copy" min-level tech 
admin user-default command is supported for ‘su’ and ‘oper’ access levels only: 
ETX-2i# admin access-level command "admin user-default" min-level oper 
admin factory-default-all command is supported for su level only: 
ETX-2i# admin access-level command "admin factory-default-all" min-level su 
 
Note 
The commands in the first two examples are global. The commands in the 
second two examples are only relevant under the “admin” path. 
 
 

## 3.9 Point-to-Point Protocol (PPP)  *(p.761)*

ETX-2i Devices 
3. Management and Security 
Configuration Errors 
The following table lists the messages generated by ETX-2i when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Command may not contain 
arguments 
The command contains 
arguments. 
Select a command without arguments. 
No such command; full-path 
command is expected 
There is no such full-path 
command. 
Select an existing full path command. 
3.9 Point-to-Point Protocol (PPP) 
ETX-2i supports PPP over Ethernet (PPPoE) interfaces. 
Point-to-Point Protocol (PPP) provides a standard method for transporting multiprotocol packets over 
point-to-point links.  
PPP over Ethernet (PPPoE) is used to build PPP sessions and encapsulate PPP packets over Ethernet. It 
allows ETX-2i to connect to a remote access concentrator to establish a PPPoE session and then build a 
PPP link to the peer at the other end of the PPP link. PPPoE can be used in the process of device auto-
configuration, typically for authentication. 
PPPoE in ETX-2i is used to establish a management channel through which an IP address can be 
acquired, and the unit can be managed. You can connect ETX-2i to a central server for authentication 
and to acquire an IP address and establish a management channel that a remote management system 
can use to send software and configuration files and manage ETX-2i. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products. 
 
 
ETX-2i Devices 
3. Management and Security 
Standards Compliance 
RFC 1332 – The PPP Internet Protocol Control Protocol (IPCP) 
RFC 1334 – PPP Authentication Protocols 
RFC 1661 – The Point-to-Point Protocol (PPP) 
RFC 1994 – PPP Challenge Handshake Authentication Protocol (CHAP) 
RFC 2516 – A Method for Transmitting PPP Over Ethernet (PPPoE) 
RFC 5072 – IP Version 6 over PPP 
Functional Description 
PPPoE is used to build PPP sessions and encapsulate PPP packets over Ethernet. PPPoE is useful for 
device auto-configuration, typically for authentication.  
You can have a single PPPoE session on one router interface. 
On Ethernet interfaces, you are required to establish a PPPoE session before starting PPP negotiation. 
You can establish the PPPoE session only on a router interface that is bound to a PPP port that is bound 
to an operational SVI port.  
 
Note 
There is no command to explicitly enable PPPoE. Once the PPP port is bound 
to an SVI port, PPP starts after a PPPoE session has been established.  
Factory Defaults 
By default, no PPP port exists. When a PPP port is created, it is configured as shown below.  
Parameter 
Description or value 
name 
PPP <ppp-port-num>, e.g., PPP 1 for PPP port 1 
no refuse-chap 
Do not refuse CHAP authentication. 
refuse-no-auth 
Refuse skipping authentication. 
refuse-pap 
Refuse PAP authentication. 
ETX-2i Devices 
3. Management and Security 
Configuring PPP and PPPoE 
PPPoE and PPP can function once the PPP port is bound to an underlying level: SVI port. If it is bound to 
SVI, the SVI may only be bound to an Ethernet or Ethernet-like port.  
Then, you bind the PPP port to a router interface; additionally, you configure incoming and outgoing 
flows over the SVI port. You can bind one ETX-2i router interface to a PPP port. 
Configuring PPP Port 
 To configure a PPP port: 
1. Navigate to configure port ppp <ppp-port-num> to select the PPP port to configure. 
The config>port>ppp(<ppp-port-num>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Binding PPP port to lower layer 
(SVI) 
[no] bind svi <port-number> 
Note: A PPP port cannot be bound 
to an SVI that is bound to a non-
Ethernet port. 
Configuring CHAP hostname 
[no] chap-hostname <name> 
Defines hostname to send to PPP 
peer if CHAP authentication is 
used  
name – CHAP hostname 
Possible values: 1–80-character 
string  
Note: If the CHAP hostname is not 
configured, ETX-2i identifies itself 
by its device name (assigned via 
the name command in the system 
level). 
Configuring default password for 
CHAP authentication 
chap-password <password> [hash] 
[no] chap-password [name] 
pass – CHAP password 
Possible values: 1–80-character 
string 
hash – password encrypted 
Possible values: hash, “” 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
The default CHAP password is 
used for authentication if the 
username in a received CHAP 
challenge does not match any of 
the defined users. 
The hash keyword denotes that 
the string is hashed, rather than 
clear text; usually it is added by 
the device after hashing the clear 
text that the user enters, before 
saving it in the database. 
If you enter the password as a 
text string, do not use the hash 
parameter. Use it only if you are 
specifying the password as a 
hashed value (obtained by 
entering the info command to 
display PPP data). 
Note: 
• If you enter a clear password 
(chap-password), the device 
encrypts it, and saves the 
encrypted password in the 
database. 
• If you enter an encrypted 
password (chap-password 
hash), the device saves the 
encrypted password in the 
database. 
Defining name of PPP port 
[no] name <string> 
name – port name 
Possible values: 1–80-character 
string 
Configuring PAP credentials 
pap-username <name> 
password <password> [hash] 
[no] pap-username [name] 
name – PAP username; string 
Possible values: string up to 80 
characters 
pass – PAP password 
Possible values: string up to 80 
characters 
See above comments about the 
hash parameter. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Configuring PPPoE  
pppoe 
For detailed information on PPPoE 
configuration, see Configuring 
PPPoE below. 
Refusing CHAP authentication 
[no] refuse-chap 
Specifying whether to refuse 
CHAP authentication if it is 
offered by the peer. 
• If you do not want ETX-2i to use 
CHAP authentication for the 
PPP session, enter refuse-chap. 
• If you do want ETX-2i to use 
CHAP authentication if offered 
by the peer, enter 
no refuse-chap. 
Refusing no authentication 
[no] refuse-no-auth 
Specifies whether to refuse not 
using authentication (i.e., whether 
to refuse skipping authentication), 
if that is offered by the peer. 
• If you do not want ETX-2i to 
skip authentication for the PPP 
session, enter refuse-no-auth. 
• If you do want ETX-2i to skip 
authentication if offered by the 
peer, enter no refuse-no-auth. 
Refusing PAP authentication 
[no] refuse-pap 
Specifies whether to refuse PAP 
authentication if it is offered by 
the peer. 
• If you do not want ETX-2i to use 
PAP authentication for the PPP 
session, enter refuse-pap. 
• If you do want ETX-2i to use 
PAP authentication if offered by 
the peer, enter no refuse-pap. 
Displaying PPP port status 
show status 
See  
Viewing PPP Port Status. 
 
ETX-2i Devices 
3. Management and Security 
Configuring PPPoE 
 To configure PPPoE: 
1. Navigate to configure port ppp <ppp-port-num> pppoe. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Defining service name for PPPoE 
session 
service-name <string> 
[no] service-name [string] 
service-name –service name 
Possible values: string up to 80 
characters 
Note: If the service name is 
configured, ETX-2i accepts PPPoE 
offers only if the service name in 
the offer matches. 
Displaying PPPoE status 
show status 
See Viewing PPPoE Status. 
Example 
 To configure for PPPoE: 
• 
Bind to SVI 1, router interface 1. 
• 
Authentication – CHAP or PAP must be used. 
 
CHAP hostname=ETXCHAP, default password=ppp1 
 
PAP username=ETXPAP, password=ppp1 
• 
Incoming flow: Untagged, ingress ETH 3, egress SVI 1 
• 
Outgoing flow: Untagged, ingress SVI 1, egress ETH 3 
exit all 
    configure 
        port 
# Configure SVI 1  
            svi 1 
                no shutdown 
            exit 
#  Configure PPP port  
            ppp 1 
                bind svi 1 
                chap-hostname ETXCHAP 
                chap-password ppp1 
ETX-2i Devices 
3. Management and Security 
                pap-username ETXPAP password ppp1 
                no refuse-chap 
                no refuse-pap 
                refuse-no-auth 
            exit 
        exit 
        flows 
#  Configure classifier to match untagged packets  
            classifier-profile untagged match-any 
                match untagged 
            exit 
#  Configure incoming flow 
            flow ppp_in 
                classifier untagged 
                ingress-port ethernet 3 
                egress-port svi 1 
                no shutdown 
            exit 
#  Configure outgoing flow 
            flow ppp_out 
                classifier untagged 
                ingress-port svi 1 
                egress-port ethernet 3 queue 0 block 0/1 
                no shutdown 
            exit 
        exit 
#  Configure router interface bound to PPP port 
        router 1 
            interface 1 
                bind ppp 1 
                ipv6-autoconfig 
                no shutdown 
            exit 
        exit 
#  Save configuration 
    save 
exit all 
Configuration Errors 
The following table lists the message generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Password is too 
long 
You tried to configure an unencrypted password (PAP or CHAP) of 
more than 80 characters. 
Shorten the 
password. 
 
 
ETX-2i Devices 
3. Management and Security 
Viewing PPP Port Status 
You can display the status and configuration of an individual PPP port that is bound to a router interface. 
 
Note 
If the PPP port is not bound to a router interface, the following output is 
displayed: PPP is not bound to an interface.  
 To view the PPP port status: 
• 
At the config>port>ppp(<ppp-port-num>)# prompt, enter: 
show status  
The PPP port status is displayed as shown below.  
ETX-2i# configure port ppp 1 
ETX-2i>config>port>ppp(1)# show status 
Name : PPP 1                                                        
 
Router Interface : Router 1/If 1   
Physical Port    : svi 1           
 
LCP 
----------------------------------------------------------------------------- 
state     : Opened               
MRU Local : 1500                Peer  : 1500         
 
Authentication 
----------------------------------------------------------------------------- 
Of Us : CHAP                State  : Completed           Identity  : admin        
 
 
IPCP 
----------------------------------------------------------------------------- 
State               : Opened               
Local IPv4 address  : 22.22.22.22                 Negotiated           
Peer IPv4 address   : 10.0.0.1             
 
IPV6CP 
----------------------------------------------------------------------------- 
State               : Opened                                      
Local  IPv6 address : fe80::d31:494c:56c:71b0     Negotiated           
 
Peer   IPv6 address : fe80::8828:1bab:8cf5:2477                   
Global IPv6 address : 2001:db8::284d:3190:e15a:e814               
 
 
ETX-2i Devices 
3. Management and Security 
Parameter 
Description 
Router 
Interface 
Router/router interface 
Physical Port 
Physical interface under the router interface  
Possible values: string 
LCP 
 
State 
LCP state 
Possible values: Initial, Starting, Closed, Stopped, Closing, Stopping, Request-Sent, Ack-
Received, Ack-Sent, Opened 
MRU Local 
Local MRU 
Possible values: number 
Peer 
Peer MRU 
Possible values: number 
Authentication 
 
Of Us 
Authentication protocol (us) 
Possible values: CHAP, PAP, None 
State 
Authentication phase state (us) 
Possible values: Initial, Completed, In Progress, Failed 
Note: This line is displayed only if authentication protocol (us) is CHAP or PAP (Of Us value) 
and is in Opened state (under LCP and IPCP), i.e., connection was established, and 
authentication succeeded. 
Identity 
Authentication identity (us) 
Possible values: string 
Note: This line is displayed only if authentication protocol (us) is CHAP or PAP (Of Us value) 
and is in Opened state (under LCP and IPCP), i.e., connection was established, and 
authentication succeeded. 
IPCP 
 
State 
IPCP state 
Possible values: Initial, Starting, Closed, Stopped, Closing, Stopping, Request-Sent, Ack-
Received, Ack-Sent, Opened 
Local IPv4 
Address 
IPCP local IP address 
Possible values: IPv4 address, formatted “xxx.xxx.xxx.xxx”, “” 
Negotiated 
IPCP local IP address negotiated 
Possible values: Negotiated, “” 
Peer IPv4 
Address 
IPCP remote IP address 
Possible values: IPv4 address, formatted “xxx.xxx.xxx.xxx”, “” 
ETX-2i Devices 
3. Management and Security 
Parameter 
Description 
IPV6CP 
 
State 
IPV6CP state 
Possible values: Initial, Starting, Closed, Stopped, Closing, Stopping, Request-Sent, Ack-
Received, Ack-Sent, Opened 
Local IPv6 
Address 
IPV6CP local IP address 
Possible values: IPv6 address, formatted “xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx”, “” 
Negotiated 
IPV6CP local IP address negotiated 
Possible values: Negotiated, “” 
Peer IPv6 
Address 
IPV6CP remote IP address 
Possible values: IPv6 address, formatted “xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx”, “” 
Viewing PPPoE Status  
You can display the status and configuration of an individual PPP port, which is configured with PPPoE, 
provided it is bound to a router interface. 
Note 
If the PPP port, which is configured with PPPoE, is not bound to a router 
interface, the following output is displayed: PPP is not bound to an interface.  
 To view the status of PPP port 1 configured with PPPoE and bound to a RI: 
• 
At the config>port>ppp(<ppp-port-num>)>pppoe # prompt, enter: 
show status  
The PPPoE status is displayed as shown below (based on the configuration from Example). 
ETX-2i>config>port>ppp(1)# pppoe 
ETX-2i>config>port>ppp(1)>pppoe# show status 
Router Interface       : Router 1/If 1                  
Physical Port          : svi 1                          
State                  : Up                             
Service Name Requested :   
 
Parameter 
Description 
Router Interface 
Router/router interface 
Physical Port 
Physical interface under the router interface  
Possible values: string 

## 3.10 MLDv2 Snooping  *(p.771)*

ETX-2i Devices 
3. Management and Security 
Parameter 
Description 
State 
PPPoE state 
Possible values: Up, Down, Lower Layer Down, Admin Disabled 
Service Name Requested 
Service name 
Testing PPP Ports 
Not applicable 
Viewing PPP Port Statistics 
Not applicable 
3.10 MLDv2 Snooping 
Multicast Listener Discovery Version 2 (MLDv2) is a protocol used by IPv6 routers to discover multicast 
listeners on attached links and addresses that are of interest to them. 
MLDv2 Snooping, a practice employed by IPv6 bridges, analyzes MLDv2 messages and limits multicast 
traffic to those ports interested in receiving it. It enables reduction in multicast traffic by reducing the 
number of unneeded packets on the network. 
Applicability and Scaling 
This feature is supported on all ETX-2i products.  
ETX-2i supports MLDv2 Snooping on up to 16 VPNs. 
ETX-2i supports MLDV2 Snooping for VLAN aware and VLAN unaware bridge. 
 
Note 
MLDv1 is not supported. 
ETX-2i Devices 
3. Management and Security 
Standards Compliance  
RFC 3810 Multicast Listener Discovery Version 2 (MLDv2) for IPv6 
Factory Defaults 
By default, MLDv2 Snooping is disabled. 
Parameter 
Default  
 
Remarks 
host-aging-interval 
260 seconds 
 
member port aging timer 
router-aging-
interval 
260 seconds 
 
router port aging timer 
shutdown 
shutdown 
 
MLD snooping disabled 
Functional Description 
ETX-2i supports MLDv2 Snooping for both VLAN-unaware and VLAN-aware bridges. 
MLDv2 snooping can be enabled and disabled per bridge. In VLAN-aware bridges, it can also be enabled 
and disabled per VLAN. If snooping is disabled at the bridge level, the per-VLAN configuration is ignored. 
This allows MLDv2 snooping to be disabled on the entire bridge, without changing the per-VLAN 
configuration (e.g., for troubleshooting). 
When MLDv2 snooping is enabled, the bridge keeps two lists, per port (in VLAN-unaware bridges) or per 
port and VLAN (in VLAN-aware bridges). 
 
Router port list  
Ports from which MLDv2 router traffic is received 
Member port list 
Pairs of port and multicast group address, to which multicast traffic 
is to be forwarded 
The bridge listens to messages on all MLDv2-snooping-enabled ports and dynamically adds and removes 
ports to the router and member port lists.  
The router-port list is maintained per port in VLAN-unaware bridges and per port and VLAN in VLAN-
aware bridges. 
 
 
ETX-2i Devices 
3. Management and Security 
ETX-2i can receive multicast traffic from all ports and VLANs. MLDv2 snooping builds a multicast 
forwarding database, rather than always forwarding multicast traffic to all ports (in VLAN-unaware 
bridges) or all ports of a VLAN (in VLAN-aware bridges). 
 
Note 
Snooping is only enabled on a VLAN if it is enabled at both bridge and VLAN 
levels. A command at either level does not change configuration of other 
levels. 
MAC-based Forwarding 
MLDv2 snooping supports forwarding databases that are either IPv6-based or MAC-based. ETX-2i has a 
MAC-based forwarding database. However, there are some limitations when using MAC-based address 
forwarding. 
When using a MAC-based forwarding database, IPv6 addresses are mapped to MAC addresses by 
ANDing their last 32 bits with 0xffffffff and adding a prefix of 0x3333. The IPv6 multicast address group 
ID, however, is 112 bits long. Since the higher 80 bits of the group ID are omitted when mapping IPv6 
addresses to MAC addresses, then if the bits left of the right-most 32 bits are used in a group ID, then 
multiple multicast IP addresses could be mapped to the same MAC address. 
Since multiple IPv6 addresses could be mapped to single MAC addresses, the following limitations apply: 
• 
An IPv6 multicast address has the following format: ffxx.xxxx.xxxx.xxxx.xxxx.xxxx.zzxx.xxxx. If the 
bridge receives a multicast IPv6 address with zz = 0xff or 0x00, MLDv2 snooping is not 
performed on the packet, and it is forwarded to all ports in the VLAN except the port it was 
received from. These address scopes contain special addresses, e.g., all MLDv2-capable routers, 
which must be forwarded to all ports. 
• 
To avoid one MAC address affecting multiple IPv6 addresses, make use of only the lower 32 bits 
when choosing IPv6 multicast addresses. 
If the ETX-2i bridge receives a report asking to join a multicast group with an address of 
ffxx.xxxx.xxxx.xxxx.xxxx.xxxx.zzxx.xxxx, where zz = 0xff or 0x00, the mld_snooping_unsupported_ip 
event is generated. 
 
Note 
Data for unsupported addresses is forwarded to all ports, including ones 
behind which there is no host interested in the address. To avoid this, use 
addresses out of the unsupported ranges. 
 
 
ETX-2i Devices 
3. Management and Security 
ETX-2i maintains a table of learned multicast IPv6 addresses. When it receives a report asking to join a 
group that maps to the same MAC address as a different group in that table, the new address is ignored 
and the mld_snooping_duplicate_ip event is generated. 
 
Note 
Data for the duplicate address is forwarded to the ports used by the one 
already in the forwarding database. Duplicate addresses should either be 
changed or configured statically. 
 
Note 
ETX-2i does not analyze group-specific and group-and-source-specific queries. 
These queries are sent to group addresses, (unlike general queries, which are 
sent to a fixed address). Information that could be learned from these queries 
will eventually be learned from the periodic general queries, but it will take 
more time for MLDv2 Snooping to adjust to that information. 
Port Aging 
The router port is the ETX-2i port facing the multicast router. Router port is learned from receiving 
general queries and can age out. ETX-2i sets the router port aging timer when a port is added to the 
router port list. 
• 
The timer is rearmed when receiving an MLDv2 general query or an IPv6 PIM hello message with 
source address different from 0::0. 
• 
If the timer expires, the port is removed from the router port list. 
• 
The router port list is maintained per bridge port in VLAN-unaware bridges, or per VLAN and 
bridge port in VLAN-aware bridges. 
A member port is the ETX-2i port facing a multicast client. Member port is learned from report messages 
and is subjected to aging. ETX-2i sets the member port aging timer when a port joins an IPv6 multicast 
group.  
• 
The timer is rearmed when receiving an MLDv2 report message. 
• 
If the timer expires, the port is removed from the multicast group forwarding table. 
• 
The member port list is maintained per bridge port and multicast group in VLAN-unaware 
bridges, or per VLAN, bridge port and multicast group in VLAN-aware bridges. 
 
 
ETX-2i Devices 
3. Management and Security 
ETX-2i must listen to MLDv2 general queries, sent to the link-scope all-nodes multicast address (FF02::1), 
on all ports and all VLANs. General queries are sent periodically by MLDv2 queries, to find the ports on 
which group members reside. If a general query is received the bridge must: 
• 
Forward the query to all ports (VLAN-unaware bridges) of all ports in the VLAN (VLAN-aware 
bridges) except the receiving port. 
• 
If the receiving port is not on the router-port list, add it to the list and set the aging timer. 
• 
If the receiving port is on the router-port list, rearm its aging timer. 
ETX-2i must listen to MLDv2 reports, sent to FF02::16, to which all MLDv2 multicast routers listen, on all 
ports and all VLANs. Reports are sent by listeners as responses to router queriers or when asking to join 
or leave a multicast group. If MLDv2 report is received the bridge must: 
• 
Peruse the report and update the member port list accordingly. That is, if a host asks to join a 
group, add the receiving port to the member port list of the group. Conversely, if a host is 
leaving a group the receiving port is not immediately removed from the member list, since there 
may be other hosts interested in the group on the port. Ports are only removed from the 
member port list if the aging timer expires. 
• 
Forward it to all router ports (in VLAN-unaware bridges) or all router ports in the VLAN (in VLAN-
aware bridges). 
• 
If the receiving port is not on the member port list, add it to the list and set the aging timer. 
• 
If the receiving port is on the member port list, rearm the aging timer. 
ETX-2i must receive all multicast traffic from all ports and VLANs. If multicast packet that is not MLDv2 
protocol traffic is received, the device must: 
• 
In case of an unregistered multicast packet, i.e., a packet for a group with no current members, 
forward it to all router ports (in VLAN-unaware bridges) or all ports in the VLAN (in VLAN-aware 
bridges). 
• 
In case of a registered multicast packet, forward it to: 
 
All router ports (in VLAN-unaware bridges) or all router ports in the VLAN (in VLAN-aware 
bridges). 
 
All member ports (in VLAN-unaware bridges) or all member ports in the VLAN (in VLAN-
aware bridges) that are members of the multicast group. 
 
Note 
A static router port is always on the router port list; it is not subjected to timer 
aging. 
A static member port is always on the member port list; it is not subjected to 
timer aging. 
ETX-2i Devices 
3. Management and Security 
Source-Specific Multicast 
Source-Specific Multicast, or SSM, is a multicast service allowing hosts to subscribe to specific multicast 
sources, and thus further reducing multicast traffic in the network. 
In addition to subscribing to a multicast group, hosts may ask to receive traffic from a specific host. ETX-
2i, however, does not maintain a per-source database. This means that multicast traffic sent to a specific 
group will be forwarded to all members of that group, regardless of whether or not they are interested 
in the traffic source. 
MLD Snooping and Ethernet Ring Protection 
Note 
Ethernet ring protection is not supported by ETX-2i-100G. 
When an ERP ring port changes state, all nodes in the ring receive a Signal Failure (SF) message. If such a 
signal is received from a port on which MLDv2 snooping is enabled, ETX-2i removes from the multicast 
forwarding database all the addresses that are forwarded to either ring port (the addresses are removed 
from all ports, including ones that are not ring members). This causes multicast traffic to be forwarded 
to both ring ports until the new topology is learned from subsequent reports and queries. 
Configuring MLD Snooping 
MLD Snooping must be enabled globally. VLAN related commands and arguments apply only to VLAN-
aware bridges. 
 To configure MLD Snooping: 
1. At the config>bridge <x> prompt, enter mld-snooping. 
Where x is the bridge on which you want to configure MLD Snooping. 
The config> bridge(x)> mld-snooping# prompt is displayed. 
2. Perform the required tasks according to the following table. 
 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Comments 
Enable/disable MLD snooping  
[no] shutdown 
[no] shutdown enables/disables 
MLD Snooping globally on the 
bridge. In addition, if the bridge 
is VLAN aware you can enable 
and disable MLD snooping on 
specific VLANs, using the vlan 
command. 
Configure host aging interval 
host-aging-interval <seconds> 
Possible values: 3–11264 
Default: 260 
Configure router aging interval  
router-aging-interval 
Possible values: 3–11264 
Default: 260 
Display MLD snooping status  
show status  
See Viewing MLD Snooping 
Status. 
Configure static multicast 
group  
static-group <group-address> 
vlan <vid> port <port-number-
list> 
no static-group <group-address> 
[vlan <vid>] 
 
Configure static router port 
static-router-port vlan <vlan-id> 
port <port-number-list>  
no static-router-port vlan <vid> 
vlan-id – VLAN on which the 
router ports are statically 
configured 
Possible values: 1-4094  
port-number-list – bridge ports 
configured as multicast router 
ports 
Possible values:  n1-n2; n3 
Configure MLD snooping 
VLANs  
[no] vlan <vlan-list> 
vlan-list – MLD snooping VLANs 
Possible values:  n1-n2; n3 
If the command is repeated, it 
does not replace the current 
configuration; vid-list is either 
added to the current 
configuration or removed from 
it (using the no option). 
ETX-2i Devices 
3. Management and Security 
Viewing MLD Snooping Status 
 To display MLD Snooping status: 
• 
At the config>bridge x>mld-snooping# prompt, enter show status. 
MLD snooping is globally enabled 
MLD Snooping Is Enabled for VLAN 1-100, 200 
Aging Interval (seconds) 
  Host Ports  : 260 
  Router Ports: 260 
 
 
Router Ports: 
VLAN Type    Ports 
------------------ 
1    static  1-5, 7 
2000 learned 2, 7-10 
 
Host Ports: 
VLAN Group IP Address                        Type    Ports 
---------------------------------------------------------- 
100  ff00:1111:2222:3333:4444:5555:6666:7777 static  1-5, 7 
2000 ff11:1111:1111:1111:1111:1111:1111:1111 learned 2, 7-10 
 
Note 
Port member tables are sorted by VLAN, then (the host port list) IP address, 
and then type (static first).  
 
Parameter 
Description 
admin-state 
MLD snooping admin state at bridge level; possible values: enabled, 
disabled. 
snooping-vlans 
VLANs for which MLD snooping is enabled 
Aging interval host ports 
Aging time of host ports (in seconds) 
Aging interval router ports 
Aging time of router ports (in seconds) 
Router Ports 
 
VLAN 
VLAN the router ports of this entry are on; possible values: 1-4094. 
Type 
Type of this entry; possible values: static, learned 
Ports 
List of router ports 
Host Ports 
 
VLAN 
VLAN the host ports of this entry are on; possible values: 1-4094. 

## 3.11 RSA Key Generation  *(p.779)*

ETX-2i Devices 
3. Management and Security 
Parameter 
Description 
Group IP Address 
Multicast IPv6 address this entry is on 
Type 
Type of this entry; possible values: static, learned 
Ports 
List of host ports 
 
3.11 RSA Key Generation 
ETX-2i supports generating an RSA key pair (private and public) of a configurable key size, enabling users 
to generate their own key, or to upgrade the key size from 1024 to 2048 bits (more secure). 
Applicability and Scaling 
This feature is applicable to all ETX-2i products.  
RSA key size is configurable in versions 6.8.2 (0.31) and 6.8.2 (2.32). 
In ETX-2i devices without an x86 card, only ssh is supported. 
In ETX-2i devices with an x86 card, both application options (ssh and x509) are supported. 
Functional Description 
In cases where a device does not have an RSA key, the SW automatically generates an RSA key. 
When a device is upgraded to a new version, it keeps its old key and does therefore not generate a new 
key automatically.  
ETX-2i supports the generate-rsa command for users who prefer to generate their own RSA key pair. Or 
for customers who are using a RAD device that comes with a 1024-long key and would like to upgrade to 
a more secure 2048-long key.  
When upgrading an RSA key using this command, the SW deletes the existing RSA key and reboots the 
device. As NTP is not available during device initialization (while the RSA key is actually generated), the 
SW keeps the timestamp from when the generate-rsa command was executed, so it will be available 
following reboot. This timestamp is displayed when you run the show my-public-rsa-key command to 
display the public RSA key information. 
ETX-2i Devices 
3. Management and Security 
Configuring RSA Key Generation 
 To configure an RSA key pair: 
1. Navigate to config>crypto>key. 
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
Possible values: x509, ssh 
Default value: x509  
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
Message 
Cause 
Corrective Action 
Choose either ssh or 
x509 (not both) for this 
key 
You specified both ssh and x509, but the 
device can use only one application. 
Specify either ssh or x509; not both. 
Generating a key for this 
application is not 
supported. 
You chose x509 for a device without an 
x86 card. 
Choose the ssh application. 
ETX-2i Devices 
3. Management and Security 
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
This timestamp is available and valid only when the following two conditions are fulfilled: 
• 
The RSA key is generated with V6.8.2 (and later) 
• 
NTP is locked when the RSA key is generated. 
 To display the RSA key information: 
• 
At the config>crypto>key # prompt, enter show my-public-rsa-key. 
ETX-2i>config>crypto>key# show my-public-key-rsa 
 
Generated at : 00-00-0000 00:00:00 UTC 
Name         : RAD.ETX.ssh_key 
Size         : 1024 
Application  : SSH 
 
8BB81A0E298872637B5A724A816D9426AB0D1426DDF16D7642A3A4062A5010D44E9F87DC335BD408 
D8D32439E1A27FB5145D41B67AF79A39673A55E348317C240C8018C64760D2BD79F4631540711E3E 
5931E8F054742C146C27995A19F54E651B92D37FF0D30AB0A22F2D9D31088F2BD7AD0FD64AE36CD8 
D4235BD0428537AB201375307656B5A8040B440A57C27CB5ACF9EE24EC0252DC54DE81E5088F3E5C 
38858CD13A9550079DC3CE6E4E2C03F914205F9EAD4ABB89CF5CE4FB3D7D0C77E0E497728F0A0DB7 
821A2373C1AA8F0C9FCC280B85F119EE2AA3431D39F8AC2BB71B5DFC31833B1102098DCEC4346869 
8BA1B64D16252FA48CFC19259CC3075D7E8B2CA3565F64A8CF105516121972BB49083DA6DA66A8F6 
4303DEC86F1ACAB51D79910FBB3ACE462E2BA5A75815DE341679518382F3E8FC141E38C867D29D23 
4FD7F1895BE906DDC3FB4DB961C4F7EE2D2F06D4155E630B26E4558E58BA67C41DC814159D9C03E4 
C39B39810E552055D59CFEF776D6DAD1B2DBCC7F816CE81477B0FB83E3866E3A1D7C7D70BB0AE74F 
B73AE3675C0E468CF45A89EAEEB06DBAE21927166FE29E8568D5707F5A44CAFFCC0728DD8A4A4BCD 
633A053F7F3CC295B02093FB81043D1FA272F77AB6F6D7C2867F5BD9C68283A115EC4DBEFEE9ADEC 
959B7D0B799314E4F3FEA605C22933D7 

## 3.12 SNMP Management  *(p.782)*

ETX-2i Devices 
3. Management and Security 
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
3.12 SNMP Management 
Simple Network Management Protocol (SNMP) is an application layer protocol that provides a message 
format for communication between managers and agents. SNMP remotely monitors and manages from 
a central workstation using a network management system (such as RADview) network devices 
connected over an IP, including cable modems, routers, switches, servers, workstations, and printers. 
ETX-2i devices and PMC support SNMPv3, the latest SNMP version to date. SNMPv3 provides secure 
access to devices in the network by authenticating and encrypting data packets over the network. 
SNMPv3 allows data to be collected securely from SNMP devices. Confidential information such as 
SNMP commands can thus be encrypted to prevent unauthorized parties from being able to access 
them. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products and to PMC in ETX-2i. 
SNMPv3 authentication key encryption is relevant for versions 6.8.2 (0.52), 6.8.2 (0.55), and 6.8.2 (2.52). 
 
 
ETX-2i Devices 
3. Management and Security 
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
RFC 2275, View-Based Access Control Model (VACM) for the Simple Network Management 
Protocol (SNMP) 
• 
RFC 3412, Version 3 Message Processing and Dispatching 
• 
RFC 3414, User-based Security Model for SNMPv3 
• 
RFC 3416, Update for RFC 1904 
ETX-2i Devices 
3. Management and Security 
Functional Description 
In an SNMP configuration, one or more administrative computers manage a group of hosts or devices. 
Each managed system continuously executes a software component called agent, which reports 
information via SNMP back to the managing workstations. 
SNMPv3 Management Configuration 
SNMPv3 provides secure SNMP access to the device by authenticating and encrypting packets 
transmitted over the network. 
The SNMPv3 manager application in RADview-EMS provides a user-friendly GUI interface to configure 
SNMPv3 parameters. If you intend to use it, you must first use the device CLI to create users with the 
required encryption method and security level, as the application can create users based only on 
existing users; new users have the same encryption method, and the same security level or lower. The 
ETX-2i default configuration provides one standard user named “initial” with no encryption and the 
lowest security level (see Factory Defaults for details). 
A Network Management System (NMS) relies on traps in order to display device alarms. As traps are not 
reliable, the NMS needs to be aware which traps got lost and be able to ask a device to resend them. 
This mechanism is called trap synchronization. 
NMSs (targets, such as RADview or third party) may be organized into trap sync groups in order to 
provide redundancy between these NMSs. You can define the tags and target parameters in each trap 
sync group – for example, you can define one trap sync group for critical alarms such as linkDown and 
coldStart, and another group for all other traps. 
Each trap is sent to all targets attached to the group, and therefore it is recommended to set identical 
traps masking for all group members. 
 
Note 
• 
ETX-2i supports up to two trap synchronization groups. 
• 
A single trap synchronization group can support multiple NMS. 
• 
If you would like all NMS to receive all traps, there is no need to configure 
trap synchronization groups.  
 
 
ETX-2i Devices 
3. Management and Security 
SNMPv3 Security 
SNMPv3 supports two user-based security mechanisms: 
• 
Authentication – Checks that the message is from a valid source. Mechanism is based on: 
 
Message Digest Algorithm 5 (MD5) message digest algorithm in Hashed Message 
Authentication Code (HMAC) (the default) 
 
Provides data integrity checks (directly) 
 
Provides data origin authentication (indirectly) 
 
Uses a private 16-byte key known by the sender and receiver 
 
Secure Hash Algorithm (SHA), an optional alternative HMAC algorithm 
• 
Privacy – Encrypts the contents of data packets to prevent unauthorized sources from learning 
them. Mechanism is based on the following: 
 
Data Encryption Standard (DES) mode (the default) 
 
Provides data confidentiality 
 
Uses encryption 
 
Uses 16-byte key known by the sender and receiver 
 
Advanced encryption standard (128-bit keys) 
SNMPv3 supports the following security levels: 
• 
no-auth-no-priv – authentication by username 
• 
auth-no-priv – authentication based on MD5 or SHA algorithm; no encryption 
• 
auth-priv – authentication based on MD5 or SHA algorithm; DES 56-bit encryption  
SNMPv3 Credentials 
SNMPv3 authentication and encryption (privacy) uses keys. A key is calculated by the device as a 
function of the following: 
• 
User-configured password 
• 
Configurable SNMP engine-ID (By default, this is the device MAC address.) 
• 
Selected hashing algorithm (authentication) or selected encryption algorithm (privacy) 
By default, an SNMPv3 key is MAC-address dependent and therefore can only be used in the specific 
device where the key was calculated. ETX-2i does not store cleartext passwords in its configuration files. 
 
 
ETX-2i Devices 
3. Management and Security 
The customer has two options to store the configuration of SNMPv3 credentials (authentication and 
privacy): 
1. Store the calculated key. This is the legacy method and the configuration cannot be used in 
another device. 
2. Store an encrypted form of the configured passwords. This is a separate encryption, with a fixed 
internal key, which is then used to create the SNMPv3 encryption. (In this case, configuration is 
MAC-independent and can be used in other devices. For example, upon hardware failure of the 
unit, the backup configuration can be restored to a replacement unit.) 
The following describes how to set SNMPv3 credentials. 
Method 1: Storing an SNMP authentication or privacy key 
1. Configure a clear text password for the SNMP user.  
2. The device calculates the corresponding key based on the selected algorithm (MD5/SHA or 
DES/AES), cleartext password, and SNMP engine ID. 
3. The key is saved in the configuration file. 
Method 2: Storing an encrypted SNMP authentication or privacy password 
1. In an offline device, configure an SNMP user with a cleartext password.  
The device encrypts the password. 
2. Under the SNMP user in the offline device, run the show credentials command to view the 
encrypted passwords. 
3. Copy the encrypted passwords into a text file. 
4. In the online device, configure an SNMP user. 
5. Under the SNMP user, set the authentication and privacy passwords to the same strings from 
the text file with the addition of a hash keyword at the end of each line. 
Factory Defaults 
The following is the default configuration of the SNMP parameters (see Configuring SNMPv3  for 
explanations of the parameters): 
• 
SNMP engine ID set to device MAC address 
• 
View named “internet” providing access to IETF MIBs and IEEE MIBs 
ETX-2i Devices 
3. Management and Security 
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
Configuring SNMPv3 Management 
Follow this procedure to configure SNMPv3: 
1. Set SNMP engine ID if necessary. 
2. Add users, specifying authentication protocol and privacy protocol. 
3. Add groups, specifying security level, protocol, and views. 
4. Connect users to groups. 
5. Add notification entries with assigned traps and tags. 
6. Configure target parameter sets to be used for targets.  
7. Configure targets (SNMPv3 network management systems to which ETX-2i should send trap 
notifications), specifying target parameter sets, notification tags, and trap synchronization 
groups if applicable. 
 To configure SNMPv3 parameters: 
1. Navigate to configure management snmp. 
The config>mngmnt>snmp# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Note 
Entered password parameter should comprise at least eight characters.  
 
Task 
Command 
Level 
Comments 
Configuring group 
access-group <group-name> 
{ snmpv2c | usm } 
{ no-auth-no-priv | auth-no-priv | 
auth-priv } 
snmp 
Entering no access-
group deletes the group.  
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Level 
Comments 
Defining how to 
match the context 
sent in frames by 
the NMS  
context-match {exact | prefix} 
snmp>access-group 
exact – Match the entire 
context. 
prefix – Match the first 
part of the context.  
Note: ETX-2i 
automatically identifies 
the NMS context, 
therefore you can 
configure an exact 
match. Normally prefix is 
used for devices with 
multiple instances. 
Setting view for 
traps 
notify-view <name> 
snmp>access-group 
See the description of 
the view command for 
information on how to 
limit the parts of the MIB 
hierarchy that the view 
can access.  
Setting view with 
read-only access  
read-view <name> 
snmp>access-group 
Setting view with 
write access  
write-view <name> 
snmp>access-group 
Administratively 
enabling group 
no shutdown 
snmp>access-group 
Entering shutdown 
disables the group. 
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
This should normally be 
left set to the default 
value. 
Administratively 
enabling 
community 
no shutdown 
snmp>community 
Entering shutdown 
disables community. 
Configuring 
notification  
notify <notify-name> 
snmp> 
 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Level 
Comments 
Assigning trap to 
notification 
bind <trap-name>  
snmp>notify 
You can assign more 
than one trap to a 
notification, in separate 
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
 
Configuring 
notification filter 
to define access to 
a particular part of 
the MIB hierarchy 
for trap variables 
notify-filter <name> <sub-tree-oid> snmp 
name – Name of filter  
sub-tree-oid – OID that 
defines the MIB subtree  
Specifying the part 
of the subtree OID 
to use in order to 
define the MIB 
subtree 
mask [<mask>] 
snmp>notify-filter 
The mask is comprised 
of binary digits (for 
example, the mask 1.1.1 
converts OID 1.3.6.7.8 to 
1.3.6). It is not necessary 
to specify a mask if 
sub-tree-oid is the OID 
that should be used to 
define the MIB subtree. 
Defining whether 
traps with trap 
variables 
belonging to the 
MIB subtree are 
sent 
type {included | excluded} 
snmp>notify-filter 
included – Traps with 
trap variables belonging 
to the MIB subtree are 
sent. 
excluded – Traps with 
trap variables belonging 
to the MIB subtree are 
not sent. 
Administratively 
enabling 
notification filter 
no shutdown 
snmp>notify-filter 
 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Level 
Comments 
Configuring 
notification filter 
profile 
notify-filter-profile <params-name> snmp 
params-name – specifies 
the target parameter set 
to associate with the 
profile 
Configuring 
notification filter 
profile name 
profile-name <argument> 
snmp>filter-profile 
argument – specifies 
notification filter to 
associate with the 
profile 
Administratively 
enabling 
notification filter 
profile 
no shutdown 
snmp>filter-profile 
 
Connecting 
security name to 
group (e.g., 
connecting user or 
community to 
group)  
security-to-group 
{ snmpv2c | usm } 
sec-name <security-name> 
snmp 
Entering 
no security-to-group 
removes 
security-to-group entity. 
Specifying group to 
which to connect 
security name 
group-name <group-name> 
snmp>security-to-group 
 
Administratively 
enabling 
security-to-group 
entity 
no shutdown 
snmp>security-to-group 
Entering shutdown 
disables the 
security-to-group entity. 
Setting SNMP 
engine ID to MAC 
address, IP 
address, or string 
snmp-engine-id 
mac [ <mac-address> ] 
snmp-engine-id 
ipv4 [ <ip-address> ] 
snmp-engine-id text <string> 
snmp 
If you use the mac 
option and don’t specify 
the MAC address, the 
SNMP engine ID is set to 
the device MAC address. 
If you use the ipv4 
option and don’t specify 
the IP address, the 
SNMP engine ID is set to 
the device IP address. 
Configuring target 
(SNMPv3 network 
manager) 
target <target-name> 
snmp 
Entering no target 
removes target.  
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Level 
Comments 
Specifying target 
address as IP 
address or OAM 
port 
address udp-domain <ip-address> 
address oam-domain <oam-port> 
snmp>target 
 
Assigning tag(s) to 
target (the tag(s) 
must be defined in 
notification 
entries) 
tag-list <tag> 
tag-list [ <tag> ] 
tag-list [ <tag1> <tag2>…<tagn> ] 
snmp>target 
If you specify more than 
one tag, you must 
enclose the list in 
quotes; however, if you 
are specifying just one 
tag, the quotes are 
optional. 
Specifying set of 
target parameters 
for target 
target-params <params-name> 
snmp>target 
 
Specifying the trap 
synchronization 
group to be 
associated with 
the SNMP target 
(NMS) 
trap-sync-group <group-id>  
snmp>target 
If the group does not 
exist, it is created. 
Enter no 
trap-sync-group 
<group-id> to remove 
the manager (NMS) from 
the group. If the 
removed manager was 
the last to be associated 
with the trap-sync-
group, the group is 
automatically deleted. 
ETX-2i supports up to 
two trap synchronization 
groups. 
Administratively 
enabling target  
no shutdown 
snmp>target 
Entering shutdown 
disables the target.  
Configuring set of 
target parameters, 
to be assigned to 
target 
target-params 
<target-param-name> 
snmp 
Entering 
no target-params 
removes target 
parameters. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Level 
Comments 
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
{ snmpv2c | snmpv3 } 
snmp>target 
 
Specifying user on 
whose behalf 
SNMP messages 
are to be 
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
SNMP messages 
for the set of 
target parameters 
version { snmpv2c | usm } 
snmp>target 
Use usm for SNMPv3 
version. 
Administratively 
enabling target 
parameters 
no shutdown 
snmp>target 
Entering shutdown 
disables target 
parameters. 
Configuring target 
parameters and 
tags for trap 
synchronization 
group  
trap-sync-group <group-id> 
snmp 
The trap synchronization 
group must be 
previously defined at the 
target level. 
Specifying tags in 
trap-sync-group 
tag-list <list> 
snmp>trap-sync-group 
To remove the tag list, 
enter: no tag-list. 
Specifying set of 
target parameters 
in trap-sync-group 
target-params <params-name> 
snmp>trap-sync-group 
To remove the set of 
target parameters, 
enter: no target-params 
<params-name>. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Level 
Comments 
Configuring user 
user <security-name> 
[md5-auth [ {des | aes128 | none} ]
 ] 
user <security-name> 
[sha-auth [ {des | aes128 | none} ] ] 
user <security-name> [none-auth] 
snmp 
If you don’t specify the 
authentication method 
when creating a user, 
the default is MD5 with 
DES privacy protocol. To 
create a user with no 
authentication, specify 
none-auth. 
Entering 
no user <security-name> 
deletes the user. 
Setting user SNMP 
authentication 
password or 
entering calculated 
SNMP key value 
[no] authentication { password 
<password> [hash] | 
 key <key-value>} 
snmp>user 
<password> – clear-text 
password (minimum 
length 8, maximum 
length 76) or hashed 
password (if hash option 
is entered; obtained on 
an offline device by 
entering a cleartext 
password, and then 
under the SNMP user, 
running the show 
credentials command to 
view the encrypted 
passwords and copying 
them here (and into the 
configuration file)  
<key-value> – calculated 
from password, 
algorithm, and SNMP 
engine ID (for backward 
compatibility) 
Entering 
no authentication 
disables the 
authentication protocol. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Level 
Comments 
Setting user 
privacy password 
and optional key 
for changes 
[no] privacy { password 
<password> [hash] | key <key-
value>} 
snmp>user 
<password> – clear-text 
password (minimum 
length is 10 for AES128 
and 8 for DES, maximum 
length for both is 76) or 
hashed password (if 
hash option is entered); 
obtained on an offline 
device by entering a 
cleartext password, and 
then under the SNMP 
user, running the show 
credentials command to 
view the encrypted 
passwords and copying 
them here (and into the 
configuration file) 
<key-value> – calculated 
from password, 
algorithm, and SNMP 
engine ID (for backward 
compatibility). 
Entering no privacy 
disables the privacy 
protocol. 
Administratively 
enabling user 
no shutdown 
snmp>user 
You must define the 
authentication and 
privacy method before 
you can enable the user 
unless the user was 
defined with no 
authentication 
(none-auth). 
Entering shutdown 
disables the user. 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Level 
Comments 
Displaying user 
credentials 
show credentials 
snmp>user 
Masked when the user-
based security 
model (USM) is none-
auth.  
Can copy the shown 
encrypted passwords 
into the configuration 
file. 
Defining access to 
a particular part of 
the MIB hierarchy 
view <view-name> <sub-tree-oid> 
snmp 
view-name – name of 
view, which can be 
associated to a group as 
a notify, read, or write 
view 
sub-tree-oid – OID that 
defines the MIB subtree 
(for example 1.3.6.1 
represents the Internet 
hierarchy) 
Specifying the part 
of the subtree OID 
to use in order to 
define the MIB 
subtree 
mask <mask> 
snmp>view 
The mask is comprised 
of binary digits (for 
example, the mask 1.1.1 
converts OID 1.3.6.7.8 to 
1.3.6). It is not necessary 
to specify a mask if 
sub-tree-oid is the OID 
that should be used to 
define the MIB subtree. 
Defining whether 
access to the MIB 
subtree is allowed  
type {included | excluded} 
snmp>view 
included – Allow access 
to the subtree. 
excluded – Do not allow 
access to the subtree. 
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
 
ETX-2i Devices 
3. Management and Security 
Task 
Command 
Level 
Comments 
Displaying SNMPv3 
information, such 
as the number of 
times the SNMPv3 
engine has booted, 
and how long since 
the last boot 
show snmpv3 information 
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
ETX-2i Devices 
3. Management and Security 
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
Tag = “Port” 
 
Bound to ethLos, sfpRemoved 
• 
Notification  named “TrapPower”: 
 
Tag = “Power” 
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
 
 
ETX-2i Devices 
3. Management and Security 
 To create target parameters and target: 
• 
Target parameters named “TargParam1”: 
 
Message processing model SNMPv3 
 
Version USM 
 
User “MD5_priv”  
 
Security level authentication and privacy 
• 
Target named “TargNMS1”: 
 
Target parameters “TargParam1” 
 
Tag list = “Port”, “Power” 
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
 To create communities, target parameters, and target for network devices that work with 
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
 
 
ETX-2i Devices 
3. Management and Security 
• 
Community “trap”: 
 
Name: “public” 
 
Security name: “v1_trap” (defined in default configuration)  
• 
Target parameters named “snv1”: 
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
Target parameters “snv1” 
 
Tag list = “unmasked” 
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
 
 
 
ETX-2i Devices 
3. Management and Security 
#******** Configure target 
  target NMSsnmpv1 
    target-params snv1 
    tag-list unmasked 
    address udp-domain  192.5.6.7 
    no shutdown 
    exit all 
save 
 To display SNMPv3 information: 
ETX-2i# configure management snmp 
ETX-2i> config>mngmnt>snmp# show snmpv3 information 
SNMPv3           : enable  
Boots            : 2          
Boots Time (sec) : 102        
EngineID         : 800000a4030020d2202416 
 To display SNMPv3 user credentials: 
ETX-2i# configure management snmp user 
ETX-2i> config>mngmnt>snmp>user# show credentials 
Authentication Password 
: "jelrijwp03dln39" 
Privacy Password 
 
: "reirjfekj309u53fem" 
 To configure trap synchronization: 
• 
Trap synchronization group 1: 
 
Members NMS1 and NMS2 
 
Target parameters “TargParam1” (from previous example) 
 
Tag list = “Port”, “Power” (from previous example) 
 
 
ETX-2i Devices 
3. Management and Security 
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
      tag-list “port power” 
      target-params TargParam1 
      exit all 
save 
 To display trap synchronization configured in above example: 
ETX-2i>config>mngmnt>snmp# show trap-sync 
Group ID  Member 
--------------------------------------------------------------- 
1         NMS1 
1         NMS2 
2         NMS3 
2         NMS4 