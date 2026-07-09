# Feature Reference – 5 Traffic Processing – 5.10 Routing Protocol BGP

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1084–1117.*


## Applicability and Scaling  *(p.1084)*

ETX-2i Devices 
5. Traffic Processing 
The fields above are: 
Field 
Description 
Translated packets Inside 
to Outside 
Number of packets translated by NAT at the Inside to Outside direction 
Translated packets 
Outside to Inside 
Number of packets translated by NAT at the Outside to Inside direction  
Entries Created 
Number of entries created in the translation table  
Entries Expired 
Number of entries expired and deleted in the translation table 
Dropped Packets 
Number of packets dropped by NAT 
Failed Mapping 
Number of entries that failed to be created in the translation table due to table 
full or lack of UDP/TCP ports for allocation 
5.10 Routing Protocol BGP 
Border Gateway Protocol (BGP) is a path-vector protocol for dynamic routing, used for route distribution 
between Autonomous Systems (AS) across the internet and other large networks. 
Dynamic routing protocols enable routing tables to automatically adapt to changing networks. BGP is 
the de-facto standard in the internet for communicating routing information between Autonomous 
Systems (AS), making it the only option for AS boundary routers (ASBR) to enable route communication 
with other ASes. 
BGP supports the AS‑Override protocol, which is a BGP mechanism that enables correct route 
propagation when a customer uses the same AS number at multiple sites. In standard BGP operation, a 
BGP speaker rejects routes that contain its own AS number in the AS‑Path attribute. In multi‑site 
customer deployments where the same customer AS is reused, this behavior prevents legitimate routes 
from being accepted. 
When The AS‑Override protocol is enabled on a BGP neighbor, the ETX‑2i device replaces the customer 
AS number in the AS‑Path with its own local AS number before advertising routes to that neighbor. This 
allows the receiving CE device to accept the routes without detecting a loop. 
Applicability and Scaling 
Applicable to all ETX-2i devices that support BGP routing. 

## Standards Compliance and MIBs  *(p.1085)*


## Functional Description  *(p.1085)*

ETX-2i Devices 
5. Traffic Processing 
Standards Compliance and MIBs 
The BGP feature adheres to the following standards: 
Reference 
Title 
RFC 4271 
A Border Gateway Protocol 4 (BGP-4) 
RFC 4893 
BGP Support for Four-octet AS Number Space 
RFC 5396 
Textual Representation of Autonomous System (AS) Numbers 
RFC 2385 
Protection of BGP Sessions via the TCP MD5 Signature Option 
RFC 2545 
Use of BGP-4 Multiprotocol Extensions for IPv6 Inter-Domain Routing 
The following BGP features are not supported: 
• 
Graceful restart (RFC 4724) 
• 
Interaction with ECMP 
Functional Description 
In the context of RAD devices, BGP is intended for use on customer-premises equipment (CPE) at the 
boundary of a large customer network that is an independent ‘stub’ AS connected to only one other AS 
(the service provider network).  
BGP functionality is explained in the following sections. 
Dynamic Routing Protocols 
Routers direct packets through their various interfaces according to their routing tables, which specify 
an exit interface for each destination IP network. While routing tables can include static, manually 
configured routes, an optimized routing table requires knowledge of remote network topology and 
complex path calculations. Dynamic routing protocols define how routers communicate network 
topology with each other and how they accordingly calculate optimized network paths and create their 
routing tables. 
The internet is divided into Autonomous Systems (AS). An AS is usually the network of an Internet 
Service Provider (ISP) or another large organization that administers the AS-internal routing policy. 
Routing information inside each AS is communicated and determined by an Interior Gateway Protocol 
(IGP) such as OSPF; routing information between ASes is communicated by the Border Gateway Protocol 
(BGP). 
ETX-2i Devices 
5. Traffic Processing 
BGP: Path-Vector Routing 
BGP is a path-vector routing protocol. As opposed to link-state protocols, in which network topology is 
communicated throughout a network, and as opposed to distance-vector protocols, in which routers 
communicate destination distances, routers using a path-vector protocol communicate actual paths, or 
routes, to destinations. 
In BGP, communicated paths for each destination contain the IP address of the first hop, and the list of 
ASes, by AS numbers (ASN), which need to be traversed to reach the destination. BGP aggregates routes, 
and, to prevent loops and to choose among the path alternatives, each BGP router decides which actual 
routes to adopt among BGP updates received from its neighbors and which of its known routes to 
advertise to its neighbors. BGP makes these decisions using optimization algorithms and (in other BGP 
implementations) additional criteria from a locally configurable policy. 
BGP Neighbors 
BGP is configured only on AS Boundary Routers (ASBR). Each BGP router recognizes a limited list of BGP 
neighbors from which it receives route updates and to which it advertises route updates. A BGP 
neighbor relationship needs to be manually defined on both BGP routers. BGP routers identify neighbors 
by their IP addresses and AS numbers. 
BGP neighbors always belong to the IPv4 unicast address family and can optionally belong to the IPv6 
unicast address family. 
AS-Internal Destination Injection 
To be able to advertise its local AS-internal destinations to the rest of the internet, BGP needs to know 
what destination networks are included in its local AS. BGP can become aware of these networks in 
several configurable ways: 
• 
BGP can be configured to redistribute static routes from the router’s routing table. 
• 
BGP can be configured to redistribute connected networks. 
• 
BGP can be configured to redistribute routes from the AS’ IGP (OSPF). Supported only for IPv4 
address family. 
• 
Specified network addresses can be manually configured in BGP. These destinations are 
advertised only if they are found in the local routing table. 
ETX-2i Devices 
5. Traffic Processing 
AS Numbers (ASN) 
BGP communicates paths as a list of numbers of the ASes that need to be traversed to reach 
destinations. Generally, AS numbers uniquely define the AS, and are allocated for the individual AS by 
the Internet Assigned Numbers Authority (IANA); however, ISPs can define private ASes for their 
customer networks with AS numbers in the range 64512–65534. 
Limiting Received Routes 
The number of routes received can be limited for each neighbor. When the number of received routes 
reaches 90% of the configured value, the device generates an alarm and sends an SNMP trap. When the 
configured value is exceeded, the session goes down for five minutes. 
BGP Session Timers 
BGP neighbors send each other keep-alive messages to confirm the connection’s health. Two 
parameters are defined: 
keepalive is the interval, in seconds, between messages confirming connection health to the neighbor. If 
the value is 0, these messages are disabled. 
holdtime is the interval, in seconds, after which the connection with the neighbor is considered down if 
no keep-alive messages have been received from the neighbor. If the value is 0, the neighbor is never 
considered down. 
Upon session initiation, the neighbors negotiate for each of these two parameters and then both use the 
lower of their values. Negotiated values can be viewed (see Viewing Neighbor Connection Status). 
Either both parameters must be non-zero, or both must be zero. 
Routing Preferences 
When there are conflicts between routes received from different sources, such as static routes, 
connected networks, OSPF routes, and BGP routes, the router’s Routing Table Manager (RTM) chooses 
among the sources according to configurable source preference indices (lowest number indicates 
highest priority). Separate preference indices are defined for BGP routes received from BGP neighbors in 
the same AS (Internal BGP) and for BGP routes received from BGP neighbors in other ASes (External 
BGP). 
ETX-2i Devices 
5. Traffic Processing 
BGP Path Attributes 
Path attributes are contained in BGP update packets. The path attributes of advertised routes are used 
to select the route from multiple routes, and to propagate policy. 
BGP path attributes have the following types: 
Well-known 
mandatory 
Must be supported and propagated 
Well-known 
discretionary 
Must be supported; propagation optional 
Optional transitive 
Marked as partial if unsupported by neighbor 
Optional 
nontransitive 
Deleted if unsupported by neighbor 
The following table lists the BGP path attributes. 
Name  
Description  
Path Type 
1 Origin  
Origin type (IGP, EGP, or unknown)  
Well-known mandatory 
2 AS Path  
List of autonomous systems which the advertisement 
has traversed  
Well-known mandatory 
3 Next Hop  
External peer in neighboring AS  
Well-known mandatory 
5 Local Preference  
Metric for internal neighbors to reach external 
destinations (default 100)  
Well-known discretionary 
6 Atomic Aggregate  
Includes ASes that have been dropped due to route 
aggregation  
Well-known discretionary 
7 Aggregator  
ID and AS of summarizing router 
Well-known discretionary 
8 Community  
Route tag 
Well-known discretionary 
4 Multiple Exit 
Discriminator (MED)  
Metric for external neighbors to reach the local AS 
(default 0) 
Optional nontransitive 
9 Originator ID  
The originator of a reflected route 
Optional nontransitive 
10 Cluster List  
List of cluster IDs 
Optional nontransitive 
13 Cluster ID  
Originating cluster 
Optional nontransitive 
-- Weight  
Cisco proprietary, not communicated to peers (default 
0) 
Optional nontransitive 
ETX-2i Devices 
5. Traffic Processing 
BGP Policies 
The BGP functionality provides a flexible filtering mechanism to ensure that the router processes only 
relevant BGP update packets. The filtering is done by means of defining BGP policy profiles of the 
following types: 
Prefix lists 
Filter by prefix and prefix length, where prefix is specified by IP address and mask, with 
prefix length between 24 and 26 
Route maps 
Permit/deny if packet matches community in the form x:y. The community is a BGP 
path attribute (see Table 8-32) that is usually set by each network. 
BGP policy profiles are assigned per IPv4/IPv6 unicast address family per neighbor. One of each policy 
profile type can be assigned in the inbound direction (to be applied to received packets) and outbound 
direction (to be applied to advertised packets), per IPv4/IPv6 unicast address family per neighbor. 
BGP policy profiles comprise sequentially numbered rules, each of which can be one of the following: 
Permit action 
Specifies criteria for permitting packet, and optionally sets action in 
case of route map profile 
Deny action 
Specifies criteria for dropping a packet 
Remark 
Used for commenting and visually organizing rules 
If there is a need to add a rule between already existing rules with consecutive sequence numbers, the 
rules can be interspaced to accommodate additional rules between them. 
• 
The packet filtering is done as follows: Each BGP update packet is checked according to the 
associated prefix list policy (if exists), and then the associated route map policy (if exists), 
starting with the first rule.  
• 
If the packet doesn’t match a rule, the next rule according to the sequence number is checked.  
• 
If the packet matches a deny rule, it is dropped, and the filtering ends. 
• 
If the packet matches a permit rule, the packet is permitted. Any set operation in the rule is 
performed, in the case of route map profile. 
• 
If the packet doesn’t match any rule, it is dropped. 
 
 

## Factory Defaults  *(p.1090)*

ETX-2i Devices 
5. Traffic Processing 
Maintained Information 
BGP maintains the following network information, all of which can be viewed (see Viewing BGP Status): 
• 
Neighbor connectivity details 
• 
Per-neighbor received routes 
• 
Per-neighbor advertised routes 
• 
Per-neighbor policy profiles 
• 
Per-neigbor communities 
• 
Per-neighbor RIB 
• 
Per neighbor summary 
Factory Defaults 
By default, BGP is not configured on RAD routers. The following tables show the default values when it is 
configured. 
Router 
The following parameters determine BGP behavior for the whole router, for all interfaces: 
Parameter 
Description 
Default Value 
bgp 
Whether BGP is defined (but not necessarily enabled) on 
this router, and the local ASN 
no bgp 
router-id 
ID for router in BGP communications, in IP address 
format  
-- 
(mandatory configuration) 
shutdown 
Enable (no shutdown) / disable (shutdown) BGP on the 
router 
shutdown 
IPv4 and IPv6 Unicast Address Family 
The following parameters characterize behavior for the IPv4/IPv6 unicast address families, for all BGP 
neighbors. The parameters for IPv4 and IPv6 have the same names but are defined in separate levels. 
ETX-2i Devices 
5. Traffic Processing 
Parameter 
Description 
Default Value 
external-preference 
Preference index for external BGP routes. See Routing 
Preferences. 
20 
internal-preference 
Preference index for internal BGP routes. See Routing 
Preferences. 
200 
network 
AS-internal networks that should be advertised to BGP 
neighbors. See AS-Internal Destination Injection. 
no network 
redistribute 
Sources other than BGP of routes that should be advertised 
to BGP neighbors. See AS-Internal Destination Injection.  
no redistribute 
Neighbor 
The following parameters determine BGP behavior per neighbor: 
Parameter 
Description 
Default Value 
active 
Whether IPv6 is enabled (active) or disabled (no active) 
for the neighbor 
no active 
local-address 
The local IP address from which to advertise BGP updates 
to the neighbor 
-- 
(Uses closest interface to 
neighbor) 
max-prefixes 
The maximum number of destination networks to 
receive from the neighbor 
0 
(=no limit) 
password 
Secret key for authentication of and to the neighbor 
no password 
remote-as 
The neighbor’s ASN 
-- 
(mandatory configuration) 
shutdown 
Whether the neighbor is administratively enabled (no 
shutdown) or disabled (shutdown) for  
shutdown 
keepalive 
Interval, in seconds, between messages confirming 
connection health to the neighbor 
30 
holdtime 
Interval, in seconds, after which the connection with the 
neighbor is considered down if no keepalive messages 
have been received from the neighbor 
90 

## Configuring BGP  *(p.1092)*

ETX-2i Devices 
5. Traffic Processing 
Configuring BGP 
You can configure BGP on a RAD router that is at the boundary of an AS, after the router itself has been 
properly configured. To configure BGP properly, you need to know your network BGP design, including 
the router’s IP address and ASN, designated BGP neighbors’ IP addresses and ASNs, whether IPv6 is 
required, and the desired method of passing AS-internal destinations to BGP. 
When multiple VPN routers are configured on a device, each router should be configured with its own 
instance of BGP. All of these BGP instances must share the same ASN. 
BGP parameters are configured at the following levels: 
• 
Configuring BGP at Router Level: Parameters that determine BGP behavior for the whole 
router, for all IP families and neighbors 
• 
Configuring BGP Neighbors: Per-neighbor parameters 
• 
Configuring IPv4/IPv6 Unicast Address Families: Parameters that characterize BGP behavior for 
IPv4/IPv6 unicast address families. 
Follow these steps to configure BGP: 
1. Define the BGP router IP address and ASN (see Configuring BGP at Router Level). 
2. Administratively enable BGP. 
3. Define any necessary BGP neighbors, along with the remote AS to which the neighbor belongs 
(see Configuring BGP Neighbors). 
4. Administratively enable the BGP neighbors. 
5. If it is necessary for BGP to be aware of AS-internal destinations that need to be advertised, 
configure redistribution (of OSPF routes, static routes, and/or connected networks) or explicit 
networks, for IPv4 and IPV6 unicast address families (see Configuring IPv4/IPv6 Unicast Address 
Families). 
6. For each BGP neighbor, if network design requires any non-default values for IPv4 and IPV6 
unicast address families, configure the parameters (see Configuring Neighbor Parameters). 
Configuring BGP at the Router Level 
 To configure BGP: 
1. At the config>router(<number>)# prompt, type: 
[no] bgp <ASN> 
The config>router(<number>)>bgp(<ASN>)# prompt is displayed. 
ETX-2i Devices 
5. Traffic Processing 
Note 
• 
<ASN> is the number of the local AS where the router is located 
• 
Enter no bgp <ASN> to remove BGP from the router (if no neighbors are 
defined). 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Enabling BGP on the 
router 
[no] bgp <ASN> 
<ASN> is the number of the local AS where the 
router is located. 
Restarting BGP session 
with neighbor and 
reloading BGP policy 
profiles 
clear-neighbor <IP-address> 
[soft] 
<IP-address> is the neighbor’s IP address (IPv4 or 
IPv6). 
If you specify soft, the link with the neighbor is 
not reset, but the BGP policy profiles are 
reloaded. 
Configuring BGP 
parameters for IPv4 or 
IPv6 unicast address 
family 
ipv4-unicast-af 
ipv6-unicast-af 
See Configuring IPv4/IPv6 Unicast Address 
Families. 
Configuring BGP 
neighbor 
neighbor <IP-address> 
<IP-address> is the neighbor’s IP address (IPv4 or 
IPv6). See Configuring BGP Neighbors. 
no neighbor <IP-address> removes the neighbor 
from BGP configuration. 
Defining IP address for 
the router in BGP 
communications 
router-id <IP-address> 
To simplify management, the IP address can be 
the actual IP address of one of the router’s 
interfaces, or there may be some other 
organizational convention. 
Defining or changing the router IP address 
requires BGP to be administratively disabled 
(shutdown). 
Displaying the IPv4 or 
IPv6 community table 
show community { ipv4 | ipv6 } 
See Viewing BGP Communities. 
Displaying the IPv4 or 
IPv6 RIB (Routing 
Information Base) table 
show rib { ipv4 | ipv6 } 
See Viewing BGP RIB. 
Displaying summary of 
neighbor connections 
information 
show summary 
See Viewing BGP Summary. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Administratively 
enabling or disabling 
BGP on the router 
[no] shutdown 
To disable: shutdown; to enable: no shutdown 
When BGP is disabled, operational status of BGP 
neighbors moves down. 
 
Configuring BGP Neighbors 
You can define BGP neighbors to represent neighboring routers from which the BGP router entity 
receives route updates and to which it advertises route updates. 
 To configure BGP neighbors: 
1. At the config>router(<number>)>bgp(<ASN>)# prompt, type: 
neighbor <IP-address> 
The config>router(<number>)>bgp(<ASN>)> neighbor(<IP-address>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Defining the local IP 
address from which to 
advertise BGP updates to 
the neighbor 
[no] local-address 
[<IP-address>] 
local-address <IP-address> sets a parameter 
value; no local-address clears the parameter. 
When no local address is set (default), BGP uses 
the closest interface to the neighbor. 
The change takes effect only after 
clear-neighbor or shutdown. 
Setting the maximum 
number of routes to 
accept from the neighbor 
max-prefixes <prefixes> 
<prefixes> is a number in range: 
0–2147483647. 0 means no limit. 
See Limiting Received Routes. 
Change takes effect only after clear-neighbor or 
shutdown. 
Setting password for 
neighbor session 
[no] password <password> 
[hash] 
The <password> can be up to 80 characters. 
hash specifies that the password should be 
encrypted. 
no password deletes the password. 
Change takes effect only after clear-neighbor or 
shutdown. 
Defining neighbor’s ASN 
remote-as <ASN> 
Available only when communication with the 
neighbor is disabled (shutdown). 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Setting keepalive and 
holdtime timers 
timers <keepalive> <holdtime> 
See BGP Session Timers. 
Change takes effect only after clear-neighbor or 
shutdown. 
Viewing connectivity 
details 
show neighbor-connection 
See Viewing Neighbor Connection Status. 
Enabling or disabling BGP 
communication with the 
neighbor 
[no] shutdown 
To enable: no shutdown (requires remote-as to 
have been configured) 
To disable: shutdown  
 
Note 
Certain versions allow you to configure AS-Override for a BGP neighbor. For 
further information and instructions, refer to. the v6.8.5 (1.137) release note 
dated 05/26. 
Configuring IPv4/IPv6 Unicast Address Families 
The parameters for IPv4/IPv6 unicast address families are configured in the levels configure router 
<number> bgp <ASN> ipv4-unicast-af and configure router <number> bgp <ASN> ipv6-unicast-af, 
respectively. You can configure general parameters for the unicast address families, or neighbor 
parameters. 
Configuring Unicast Address Family Parameters 
 To configure IPv4/IPv6 unicast address families: 
1. At the config>router(<number>)>bgp(<ASN>)# prompt, type one of the following, according to 
whether you wish to configure BGP parameters for IPv4 or IPv6 unicast address families: 
 
ipv4-unicast-af 
 
ipv6-unicast-af 
The prompt config>router(<number>)>bgp(<ASN>)>ipv4-unicast-af# or 
config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af# is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Defining the preference 
index for external BGP 
routes 
external-preference <priority> 
<priority> should be an integer in range 0–255. 
See Routing Preferences. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Defining the preference 
index for internal BGP 
routes 
internal-preference <priority> 
Priority can be changed at any time. 
Specifying a neighbor 
router 
neighbor <IP-address> 
See Configuring Neighbor Parameters. 
Defining an explicit 
network that should be 
advertised to BGP 
neighbors as a 
destination in this AS 
network 
<IP-address>/<netmask> 
<IP-address> is the network’s IP address, and 
<netmask> is the length of the network part 
(CIDR notation). 
Each added network requires a separate 
command. 
To delete the network entity: no network 
<IP-address>/<netmask See AS-Internal 
Destination Injection. 
Defining non-BGP sources 
of routes that should be 
advertised to BGP 
neighbors 
[no] redistribute {connected |  
static | ospf} 
 
To disable distribution: no redistribute  
{ connected | static | ospf}. 
Each source protocol (connected, static, ospf) 
requires a separate command. 
For IPv6, only the connected and static options 
are supported. 
See AS-Internal Destination Injection. 
Configuring Neighbor Parameters  
 To configure BGP neighbor parameters under IPv4/IPv6 unicast address families: 
1. At the prompt config>router(<number>)>bgp(<ASN>)> ipv4-unicast-af# or 
config>router(<number>)>bgp(<ASN>)> ipv6-unicast-af#, type: 
neighbor <IP-address> 
The prompt config>router(<number>)>bgp(<ASN>)>ipv4-unicast-af> 
neighbor(<IP-address>)# or config>router(<number>)>bgp(<ASN>)> 
ipv6-unicast-af neighbor>(<IP-address>)# is displayed. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Enabling or disabling 
IPv4 or IPv6 BGP for 
the neighbor 
[no] active 
Enable – active 
Disable – no active  
You cannot type no active for IPv4, as the address family IPv4 
unicast is always enabled for all neighbors. 
Associating prefix list 
BGP policy with the 
neighbor unicast 
address family for 
incoming or outgoing 
direction 
prefix-list-bind 
<name> {in | out} 
Type no before the command to remove the association with 
the prefix list. 
Associating route map 
BGP policy to the 
neighbor unicast 
address family for 
incoming or outgoing 
direction 
route-map-bind 
<name>{in | out} 
Type no before the command to remove the association with 
the route map. 
Viewing routes 
advertised to the 
neighbor 
show 
advertised-route 
See Viewing Advertised Routes. 
Displaying any 
associated prefix list 
policy profiles and 
rules related to a BGP 
neighbor per AF 
show prefix-list 
See Viewing BGP Policy Profiles. 
Viewing routes 
received from the 
neighbor 
show 
received-route 
See Viewing Received Routes. 
Displaying any 
associated route map 
policy profiles and 
rules related to a BGP 
neighbor per AF 
show route-map 
See Viewing BGP Policy Profiles. 
 
Configuring BGP Policy Profiles 
BGP policy profiles are configured at the router level. They can be prefix list or route map policy profiles 
(see BGP Policies for more information). After changing a policy profile, you should use the command 
ETX-2i Devices 
5. Traffic Processing 
clear-neighbor with the soft parameter, to ensure that the change is applied to the neighbor BGP 
policies. 
 To configure BGP policy profiles: 
1. Navigate to configure router <number>. 
2. Enter the necessary commands according to the table below. 
3. See Configuring Prefix List Rules or Configuring Route Map Rules respectively, for commands to 
configure the rules in a prefix list policy profile or route map policy profile 
Task 
Command 
Comments 
Configuring prefix list policy 
profile, for IPv4/IPv6 
prefix-list <name> {ipv4 | ipv6} 
Enter no prefix-list <name> to delete the 
prefix list. 
Configuring route map policy 
profile 
route-map <name> 
Enter no before the command to delete 
the route map. 
Resequencing the rules in a 
policy profile 
resequence <name> 
[<number>] 
This command can be used when you 
need to insert rules in the middle of a 
policy profile. 
<name> – name of the policy profile  
<number> – steps to insert between the 
rule sequence numbers. For instance, if 
you specify 10, the rule sequence 
numbers are changed to 10, 20, 30, etc. 
Range for <number>: 1–100000. 
Configuring Prefix List Rules 
 To configure the rules in a prefix list policy profile: 
1. Navigate to configure router prefix-list <name> {ipv4 | ipv6}. 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Removing a rule 
delete <sequence> 
<sequence> – sequence number of the 
rule to delete 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Adding a deny 
rule 
deny <prefix>/<length> [ge <ge-value>] 
[le <le-value>] [sequence <sequence>] 
• <prefix>/<length> – prefix and 
length identifying the network that 
this rule matches, in the following 
form according to IPv4 or IPv6: 
(IPv4) <IPv4 address>/<1–32> 
(IPv6) <IPv6 address>/<1–128> 
• ge – Rule matches packets with 
prefix length greater than or equal 
to <ge-value>. 
• le – Rule matches packets with 
prefix length less than or equal to 
<le-value>. 
• sequence – assigns <sequence> as 
the sequence number of the rule. 
Sequence number range: 
1–2147483648 
The ge and le parameters are validated 
as follows: 
• (IPv4) Prefix length <ge < le <= 32  
• (IPv6) Prefix length <ge < le <= 128 
Adding a permit 
rule 
permit <prefix>/<length> [ge <ge-value>] 
[le <le-value>] [sequence <sequence>] 
For an explanation of the parameters, 
see the comments above for the deny 
rule. 
Adding a 
remark 
remark [<description>] [sequence 
<sequence>] 
The description can contain up to 
252 characters. 
 
Configuring Route Map Rules 
 To configure the rules in a route map policy profile: 
1. Navigate to configure router route-map <name>. 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Removing a 
rule 
delete <sequence> 
sequence – sequence number of the rule 
to delete 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Adding a deny 
rule 
deny [match [as-path string] 
[community string] [ prefix-list string] 
][sequence sequence>] 
• as-path – BGP AS Path that this rule 
uses to match to a route in ASCII 
format; in regular expression format 
(permitted length 0–127 characters). 
Note: AS numbers are matched as 
decimal numbers. For example, the AS 
number '0x0123' should be represented 
in the regular expression string as '291'. A 
NULL string indicates that the field is not 
in use. 
• community – BGP community that 
this rule matches, in the form aa:nn  
(permitted length 0–127 characters). 
If community is not specified, this rule 
matches all packets. 
Note: Community has the new-format 
decimal notation. For example, the 
community '0x00120101' should be 
represented in the string as '18:257'. 
• prefix-list - BGP policy prefix-list 
profile name that this rule matches; 
permitted length 0–80 characters 
• sequence – Assigns <sequence> as 
the sequence number of the rule.  
Sequence number range: 
1–2147483648  
Adding a 
permit rule, 
and optionally 
specifying set 
actions 
permit[match [as-path string] 
[community string] [ prefix-list string] 
][set [as2-path-prepend string] [as4-
path-prepend string] [community 
string] [local-preference number] [med 
number] ][sequence sequence>] 
• as-path – BGP AS Path that this rule 
uses to match to a route in ASCII 
format; in regular expression format 
(permitted length 0–127 characters). 
Note: AS numbers are matched as 
decimal numbers. For example, the AS 
number '0x0123' should be represented 
in the regular expression string as '291'. A 
NULL string indicates that the field is not 
in use. 
• community – BGP community that 
this rule matches, in the form aa:nn 
(permitted length 0–127 characters). 
If community is not specified, this rule 
matches all packets.  
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Note: Community has the new-format 
decimal notation. For example, the 
community '0x00120101' should be 
represented in the string as '18:257'. 
• prefix-list - BGP policy prefix-list 
profile name that this rule matches; 
permitted length 0–80 characters 
• set – Specify set actions for BGP path 
attributes (see Table 8-32). 
• as2-path-prepend/as4-path-prepend 
– Set AS prepend (for 2/4 octets AS 
size) to <string>; permitted length 0–
127 characters 
Note: You can define only one as-path-
prepend statement - as2-path-prepend or 
as4-path-prepend. 
• community – Set community to a 
string in the form aa:nn (permitted 
length 0–127 characters.  
• local-preference – Set local 
preference to <number>.  
Possible values: 0–4294967295 
• med – Set Multiple Exit Discriminator 
(MED) to <number>.  
Possible values: 0–4294967295 
• sequence – Assigns <sequence> as 
the sequence number of the rule.  
Sequence number range: 
1–2147483648 
Adding a 
remark 
remark [<description>] 
[sequence <sequence>] 
The description can contain up to 
255 characters. 
 
 
 
ETX-2i Devices 
5. Traffic Processing 
Examples 
This section illustrates configuring BGP policy profiles. 
 To configure prefix list (IPv4): 
• 
BGP AS = 65530 
• 
Neighbor IP address = 120.120.120.120 
• 
Permit routes with prefix 100.102.0.0/11, and prefix length 24–26 
exit all 
#****** Configure the prefix list 
configure router 1 
  prefix-list subnetsIN ipv4 
    permit 100.102.0.0/11 ge 24 le 26 sequence 10 
    remark "permit 100.102.0.0/11 with prefix length 24 to 26" sequence 10000 
  exit  
 
#****** Bind the prefix list  
  bgp 65530 ipv4-unicast-af neighbor 120.120.120.120 
    prefix-list-bind subnetsIN in 
  exit all 
 
#****** Reload BGP policy profiles for the neighbor 
configure router 1 bgp 65530 
  clear-neighbor 120.120.120.120 soft 
  save 
 To configure the prefix list (IPv6): 
• 
BGP AS = 65530 
• 
Neighbor IP address = 78:78:78::78 
• 
Permit routes with prefix 123a:bbb1::/28 and prefix length 50–66 
exit all 
#****** Configure the prefix list 
configure router 1 
  prefix-list subnetsIN ipv6 
    permit 123a:bbb1::/28 ge 50 le 66 sequence 10 
    remark "permit 123a:bbb1::/28 with prefix length 50 to 66" sequence 10000   
  exit  
 
#****** Bind the prefix list 
  bgp 65530 ipv6-unicast-af neighbor 78:78:78::78 
    prefix-list-bind subnetsIN in 
  exit all 
 
 
ETX-2i Devices 
5. Traffic Processing 
#****** Reload BGP policy profiles for the neighbor 
configure router 1 bgp 65530 
  clear-neighbor 78:78:78::78 soft 
save 
 To configure the route map (IPv4): 
• 
BGP AS = 65530 
• 
Neighbor IP address = 120.120.120.120 
• 
Deny subnets with community 1:10 
exit all 
#****** Configure the route map 
configure router 1 
  route-map commIN 
    deny match community 1:10 sequence 10 
    remark "deny subnets with community 1:10" sequence 10000 
  exit  
 
#****** Bind the route map 
  bgp 65530 ipv4-unicast-af neighbor 120.120.120.120 
    route-map-bind commIN in 
  exit all 
 
#****** Reload BGP policy profiles for the neighbor 
configure router 1 bgp 65530 
  clear-neighbor 120.120.120.120 soft 
  save 
 To configure the route map (IPv6): 
• 
BGP AS = 65530 
• 
Neighbor IP address = 78:78:78::78 
• 
Permit subnets with community 1:10 
exit all 
#****** Configure the route map 
configure router 1 
  route-map commIN 
    permit match community 1:10 sequence 10 
    remark "permit subnets with community 1:10" sequence 10000 
  exit  
 
#****** Bind the route map 
  bgp 65530 ipv6-unicast-af neighbor 78:78:78::78 
    route-map-bind commIN in 
  exit all 
 

## Configuration Example  *(p.1104)*

ETX-2i Devices 
5. Traffic Processing 
#****** Reload BGP policy profiles for the neighbor 
configure router 1 bgp 65530 
  clear-neighbor 78:78:78::78 soft 
  save 
Configuration Example 
In this example, a customer-premises RAD device has been placed at the boundary of an organization’s 
network, which is an independent AS. The RAD device needs to be configured for BGP. 
The only BGP neighbor is the Provider Edge (PE) router. Since this is a stub AS, it has been decided that 
AS-internal destinations should be aggregated and manually defined (with the network command) 
rather than enabling automatic redistribution. IPv6 is required for this network. 
 
Device 
IP 
ASN 
CPE ASBR (the device being configured for BGP) 
10.10.1.1 
64515 
PE (BGP neighbor) 
10.10.10.1 
613 
The configuration process for this example is: 
#***** Configure BGP on router 
configure router 1 
    bgp 64515 
      router-id 10.10.1.1 
      no shutdown 
#***** define AS-internal networks for advertisement 
      ipv4-unicast-af 
        network 10.10.1.0/24 
      exit 
      ipv6-unicast-af 
        network fc00:1234:a1b1:0000:0000:0000:0000:0000/48 
      exit 
#***** configure neighbor 
      neighbor 10.10.10.1 
        remote-as 613 
        no shutdown 
      exit all 
save 
 
 

## Configuration Errors  *(p.1105)*

ETX-2i Devices 
5. Traffic Processing 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Cannot delete; BGP neighbor 
exist 
You tried to run no bgp, but 
there are configured BGP 
neighbors. 
Delete all neighbors and try again. 
Cannot create; AS number 
must be equal for all BGP 
entities 
You tried to define BGP with 
an ASN different from the 
BGP ASN configured for 
another router on this 
device. 
Use the same ASN for BGP on all the 
device’s routers. 
Cannot clear; unknown 
neighbor 
You tried to run 
clear-neighbor on an IP 
address that is not 
configured for any defined 
BGP neighbor. 
Use the correct IP address 
configured for the neighbor. 
Cannot set; AS number change 
requires deletion of all BGP 
entities 
You tried changing the BGP 
ASN before deleting all BGP 
entities. 
Delete all BGP entities, and then 
change the ASN. 
Cannot set; change requires 
bgp shutdown 
You tried to set the router-id 
with BGP running. 
Run shutdown and then try again. 
Cannot activate; router-id 
number must be set 
You tried to enable BGP (no 
shutdown) without having 
set the router-id. 
Set the router-id and try again. 
Cannot set; No such neighbor 
You tried to enter an IP / 
neighbor context, but you 
specified an IP address that 
is not configured for any 
neighbor. 
Use the correct IP address 
configured for the neighbor. 
Cannot set; ipv4 unicast 
address family always enable 
You tried using the active 
command in the IPv4 
neighbor CLI context. 
IPv4 cannot be disabled for any 
neighbors. If you meant to enable or 
disable IPv6, navigate to 
config>router(<number>)>bgp(<ASN
>)>ipv6-unicast-af>neighbor(<IP-add
ress>)# and try again. 
ETX-2i Devices 
5. Traffic Processing 
Message 
Cause 
Corrective Action 
Cannot activate; remote IP 
address and AS number must 
be set 
You tried to run no 
shutdown for a BGP 
neighbor, but this neighbor 
does not yet have an ASN. 
Set the neighbor’s ASN (with the 
remote-as command) and then try 
again. 
Cannot set; Hold time should 
be greater than the keepalive 
time 
You tried to run the timers 
command with hold time 
less than or equal to 
keepalive time. 
Run the command again with hold 
time greater than keepalive time.  
Cannot bind; policy profile 
type does not match 
You tried to bind a policy 
profile that does not match 
the required policy type 
(prefix-list-ipv4 or prefix-list-
ipv6).  
Change policy type to prefix-list-ipv4 
or prefix-list-ipv6). 
Cannot bind; prefix-list profile 
already in use in match 
statement 
You tried to bind prefix-list 
profile when route-map 
profile with ‘match prefix-
list’ statement is already 
bound to the same BGP 
connection.  
Unbind route-map profile with 
‘match prefix-list’ statement from 
the BGP connection. 
Cannot bind; no such policy 
profile 
You tried to bind a policy 
profile that does not exist. 
Create the policy profile that you 
want to bind. 
Cannot bind; policy profile 
type does not match 
You tried to bind a policy 
profile that does not match 
the required type (route-
map) 
Bind the policy profile to route-map. 
Cannot bind; address-family 
mismatch with match 
statement 
You tried to bind a route-
map profile with ‘match 
prefix-list’ statement with a 
prefix-list address-family that 
is not identical to bound 
connection address-family. 
Create a prefix-list address-family 
that is identical to bound connection 
address-family. 
Cannot bind; prefix-list profile 
already bound 
You tried to bind a route-
map profile with ‘match 
prefix-list’ statement when 
prefix-list profile is bound to 
the same BGP connection. 
Unbind prefix-list profile from the 
BGP connection. 
Cannot delete; prefix list is 
matched in a route-map 
You tried to delete a prefix –
list that is matched in a 
route-map. 
Unbind the policy profile from all 
entities bound to it.  
ETX-2i Devices 
5. Traffic Processing 
Message 
Cause 
Corrective Action 
Cannot create; name already 
in use 
You tried creating a prefix-
list policy profile with a 
name that already exists in 
the system. 
Choose a unique name for the newly 
created prefix-list policy profile. 
Cannot add statement; wrong 
prefix address type 
You tried adding a rule with 
an address type (ipv4 or 
ipv6) that is not related to 
the profile type. 
Use the appropriate address type. 
Cannot add statement; wrong 
length parameters 
You tried adding a rule with 
incorrect length parameters.  
Correct the length parameters so 
that length < ge-value <= le-value <= 
address length of family (32 or 128). 
Cannot add statement; regular 
expression is incorrect 
The regular expression that 
you entered does not 
translate into a valid AS path.  
Enter a new regular expression for 
the AS path. 
Cannot add statement; no 
such policy profile 
You tried adding a statement 
with a prefix-list profile that 
does not exist. 
Create the prefix-list profile or use an 
existing prefix-list profile. 
Cannot add statement; prefix-
list address-family mismatch 
You tried adding a statement 
with a prefix-list profile 
address-family that is 
different than similar 
previous statements. 
Use a prefix-list profile address-
family that is similar to previous 
statements. 
Cannot add statement; the 
route-map is bound to bgp 
connection with bound prefix-
list 
You tried adding a 
statement, but the route-
map profile (with the new 
‘match prefix-list’ statement) 
is bound to a connection 
with a bound prefix-list 
profile. 
Unbind the route map from the bgp 
connection. 
Warning: prefix list profile 
contains permit statement 
You used a prefix-list profile 
that contains at least one 
“permit” statement. 
Use another prefix-list profile or 
remove all “permit” statements from 
the current prefix-list profile. 
Set timer to ‘0’ requires 
holdtime = keepalive = 0 
You tried to run the timers 
command with one 0 value. 
Either both or neither must 
be 0. 
Run the command again with either 
both or neither parameter being 0. 

## Viewing BGP Status  *(p.1108)*

ETX-2i Devices 
5. Traffic Processing 
Viewing BGP Status 
You can view the current configuration (see Viewing the Current Configuration), status of the 
connection with each configured neighbor (see Viewing Neighbor Connection Status), and routes 
received from and advertised to each neighbor (see Viewing Received Routes and Viewing Advertised 
Routes). This information can be used for testing (see Testing BGP) and debugging. 
Viewing the Current Configuration 
To view the configuration, use the commands info (to include only non-default configuration) and info 
detail (to include default configuration). 
You can view this info at any of the following configuration levels: 
 
Level 
Context Prompt 
Router 
config>router(<number>)>bgp(<ASN>)# 
IPv4/IPv6 unicast 
address family 
config>router(<number>)>bgp(<ASN>)>ipv4-unicast-af#  
config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af#  
Neighbor 
config>router(<number>)>bgp(<ASN>)>neighbor(<IP-address>)# 
IPv6 neighbor 
config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af>neighbor 
(<IP-address>)#  
For example: 
ETX-2i>config>router(1)>bgp(64515)# info detail 
    router-id 10.10.1.1 
    no shutdown 
    echo "BGP Neighbor Configuration"# 
#   BGP Neighbor Configuration 
    neighbor 10.10.10.1 
        local-address 0.0.0.0 
        max-prefixes 0 
        password "" hash 
        remote-as 613 
        no shutdown 
        timers keepalive 30 holdtime 90 
        exit 
        echo "IPv4 Unicast Address Family Configuration" 
#   IPv4 Unicast Address Family Configuration 
    ipv4-unicast-af 
        external-preference 20 
        internal-preference 200 
        redistribute ospf 
        echo "IPv4 Unicast Address Family - Neighbor Configuration" 
ETX-2i Devices 
5. Traffic Processing 
#       IPv4 Unicast Address Family - Neighbor Configuration  
        neighbor 10.10.10.1 
            active 
        exit 
    exit 
    echo "IPv6 Unicast Address Family Configuration" 
#   IPv6 Unicast Address Family Configuration 
    ipv6-unicast-af 
        external-preference 20 
        internal-preference 200 
        echo "IPv6 Unicast Address Family - Neighbor Configuration" 
#       IPv6 Unicast Address Family - Neighbor Configuration 
        neighbor 10.10.10.1 
        no active 
        exit 
    exit 
Viewing Neighbor Connection Status 
You can view connectivity details with any configured BGP neighbor by using the show 
neighbor-connection command. This command is available in the BGP neighbor CLI context: 
config>router(<number>)>bgp(<ASN>)>neighbor(<IP-address>)#. You can use this information for 
troubleshooting and testing.  
For example: 
ETX-2i>config>router(1)>bgp(64515)>neighbor(10.10.10.1)# show neighbor-connection 
Remote Host: 10.10.10.1 
Remote Port: 179 
Local Host : 0.0.0.0 
Local Port : 36586 
Remote AS  : 613 
 
BGP State: Active             Up for 12d 06:23:53 
Hold Time (seconds) : 180     Keepalive Interval (seconds): 60 
 
Last Error : None 
 
Neighbor Advertised Capabilities 
--------------------------------------------------------------------------- 
Address Family IPv4 Unicast : Advertised and received 
Address Family IPv6 Unicast : Advertised and received 
Route refresh               : Advertised and received 
Graceful Restart            : None 
Four Octet AS               : Received 
ETX-2i Devices 
5. Traffic Processing 
Viewing Received Routes 
You can view the database of routes received from a particular neighbor by using the show received-
route command. This command is available in the CLI contexts for IPv4 or IPv6 unicast address families, 
at the neighbor level: config>router(<number>)>bgp(<ASN>)>ipv4-unicast-af>neighbor(<IP-address>)# 
or config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af> 
neighbor(<IP-address>)#. 
To display the received routes for IPv4 unicast address families: 
ETX-2i>config>router(1)>bgp(1)>ipv4-unicast-af>neighbor(2.2.2.2)# show received-route 
Network            > Next Hop        MED    LocPrf Path  
================================================================================ 
0.0.0.0/0          > 172.17.171.1    1000   2000   3000 1000 100 2333 
111.222.111.220/30 > 111.222.111.223 65200  65200  4000 800 65500 
 To display the received routes for IPv6 unicast address families: 
ETX-2i>config>router(1)>bgp(1)>ipv6-unicast-af>neighbor(1:1:1:1::2)# show received-route 
Network              > Next Hop             MED    LocPrf Path  
================================================================================ 
::/0                 > 11:11:11:11::1       1000   2000   3000 1000 100 2333 
11:11:11:11::/64     > ::                   1000   2000   3000 1000 100 
abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126      
> abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200  65200  4000 80 65500 
The above fields are: 
Field 
Description 
Network 
IPv4 or IPv6 network address (prefix and prefix length) 
IPv4 prefix length can be 0–32; IPv6 prefix length can be 0–128. 
Next Hop 
Neighbor IPv4 or IPv6 address 
MED 
Number of Multi-exit Discriminators (in decimal value) 
Possible values: 0–4294967295 
LocPrf 
Local preference 
Possible values: 0–4294967295 
Path 
 
Viewing Advertised Routes 
You can view the database of routes that are advertised to a particular neighbor by using the show 
advertised-route command. This command is available in the CLI contexts for IPv4 or IPv6 unicast 
address families, at the neighbor level: config>router(<number>)>bgp(<ASN>)>ipv4-unicast-
ETX-2i Devices 
5. Traffic Processing 
af>neighbor(<IP-address>)# or config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af> 
neighbor(<IP-address>)#.  
 To display the advertised routes for IPv4 unicast address families: 
ETX-2i>config>router(1)>bgp(1)>ipv4-unicast-af>neighbor(1.1.1.1)# show advertised-route 
A = advertised, S = suppressed, E = endingWithdrawal W = withdrawn 
   Network            > Next Hop        MED    LocPrf Path  
================================================================================ 
A  0.0.0.0/0          > 172.17.171.1    1000   2000   3000 1000 100 2333 
A  111.222.111.220/30 > 111.222.111.223 65200  65200  4000 800 65500 
 To display the advertised routes for IPv6 unicast address families: 
ETX-2i>config>router(1)>bgp(1)>ipv6-unicast-af>neighbor(1:1:1:1::2)# show advertised-route 
A = advertised, S = suppressed, E = endingWithdrawal W = withdrawn 
   Network              > Next Hop             MED    LocPrf Path  
================================================================================ 
A  ::/0                 > 11:11:11:11::1       1000   2000   3000 1000 100 2333 
S  11:11:11:11::/64     > ::                   1000   2000   3000 1000 100     
A  abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126      
   > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200  65200  4000 80 65500 
The above fields are: 
Field 
Description 
Status 
Status of route 
Possible values are: 
• A – advertised 
• S – suppressed 
• E – endingWithdrawal 
• W – withdrawn 
Neighbor  
IPv4 or IPv6 network address (prefix and prefix length) 
IPv4 prefix length can be 0–32; IPv6 prefix length can be 0–128. 
Next hop 
Neighbor IPv4 or IPv6 address 
MED 
Number of Multi-exit Discriminators (in decimal value) 
Possible values: 0–4294967295 
LocPrf 
Local preference 
Possible values: 0–4294967295 
Path 
 
ETX-2i Devices 
5. Traffic Processing 
Viewing BGP Policy Profiles 
You can view the BGP policy profiles assigned to a particular neighbor by using the command show 
prefix-list or show route-map. These commands are available in the CLI contexts for IPv4 or IPv6 unicast 
address families, at the neighbor level: config>router(<number>)>bgp(<ASN>)>ipv4-unicast-
af>neighbor(<IP-address>)# or config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af> 
neighbor(<IP-address>)#.  
 To display the prefix list policy profiles assigned to the neighbor 1.1.1.1 IPv4 unicast family: 
ETX-2i>config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(1.1.1.1)# show prefix-list 
 
Name: aaaaaAAAAAbbbbbBBBBBcccccCCCCCdddddDDDDD (In) 
 10 deny 10.10.10.0/24 (hit count: 2) 
 20 permit 3.3.3.0/24 ge 25 le 27 (hit count: 35) 
Name: XXXX (Out) 
 100000 permit 2.2.2.0/24 10 (hit count: 35) 
 To display the prefix list policy profiles assigned to the neighbor 10:10:10::10 IPv6 unicast family: 
ETX-2i>config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10:10:10::10)# show prefix-list 
 
Name: aaaaaAAAAAbbbbbBBBBBcccccCCCCCdddddDDDDD (In) 
 100000 permit 1234:1234:1234:1234:1234:1234:1234:1234/100 ge 110 le 120 
        (hit count: 4294967295) 
Name: XXXX (Out) 
 20 permit 2:2:2::0/64 (hit count: 15) 
 To display the route map policy profiles assigned to the neighbor 1.1.1.1 IPv4 unicast family: 
ETX-2i>config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(1.1.1.1)# show route-map 
Name: aaaaaAAAAAbbbbbBBBBBcccccCCCCCdddddDDDDD (In) 
  10 permit (hit count: 0) 
    match  community 1:2 
    set  community 2:3  med 456799  local-pref 123456 
  20 deny (hit count: 2) 
    match community 1000:2000 
Name: XXXX (Out) 
  10 permit (hit count: 10) 
    match community 3000:4000 
    set community 1000:2000 local-pref 110  
  20 permit (hit count: 1) 
    match community 100:200 
  40 permit (hit count: 2) 
    match as-path _150$ prefix-list AAAA community 10:20 
    set as2-path-prepend “100 100” community 30:40 
ETX-2i Devices 
5. Traffic Processing 
 To display the route map policy profiles assigned to the neighbor 10:10:10::10 IPv6 unicast family: 
ETX-2i>config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10:10:10::10)# show route-map 
 
Name: aaaaaAAAAAbbbbbBBBBBcccccCCCCCdddddDDDDD (In) 
  10 permit (hit count: 0) 
    match  community 1:2 
    set  community 2:3  med 456799  local-pref 123456 
  20 deny (hit count: 2) 
    match community 1000:2000 
Name: XXXX (Out) 
  10 permit (hit count: 10) 
    match community 3000:4000 
    set community 1000:2000 local-pref 110  
  20 permit (hit count: 1) 
    match community 100:200 
  40 permit (hit count: 2) 
    match as-path _150$ prefix-list AAAA community 10:20 
    set as2-path-prepend “100 100” community 30:40  
The above fields are: 
Field 
Description 
Name 
• Profile name 
(In)/(Out)  
Policy direction: inbound or outbound 
sequence number 
Policy rule sequence number 
Type 
Policy rule type 
Possible options are: 
• Deny 
• Permit 
route map rule 
information 
 
Viewing BGP Communities 
You can view the received communities of all neighbors by using the command show community. This 
command is available in the CLI contexts for IPv4 or IPv6, at the BGP level: 
config>router(<number>)>bgp(<ASN>) #.  
 
 
ETX-2i Devices 
5. Traffic Processing 
 To display the IPv4 BGP communities received by all neighbors: 
ETX-2i>config>router(1)>bgp(1)# show community ipv4 
 
Network                Community  
=============================================================== 
Neighbor 2.2.2.2 
 0.0.0.0/0              65000:65000 
 111.222.111.220/30     20:20 
Neighbor 33.33.33.33 
 0.0.0.0/0              1000:2000 
 111.222.111.220/30     100:100 200:200 300:300 400:400 
 To display the IPv6 BGP communities received by all neighbors: 
ETX-2i>config>router(1)> bgp(1)# show community ipv6 
 
Network                                      Community 
============================================================================= 
Neighbor 2:2:2:2::2 
 ::/0                 > 11:11:11:11::1       65000:65000 1000:2000 3000:1000 
 11:11:11:11::/64     > ::                   1000:2000 
 abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126 
 > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200:65200 
Neighbor 33:33:33:33::33 
 ::/0                 > 11:11:11:11::1       20:30 
 11:11:11:11::/64     > ::                   400:400 
 abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126 
 > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200:65200 4000:65500 
The above fields are: 
Field 
Description 
Neighbor  
Neighbor IPv4 or IPv6 address 
Network 
IPv4 or IPv6 network address (prefix and prefix length) 
IPv4 prefix length can be 0–32; IPv6 prefix length can be 0–128. 
Community 
Decimal value, in format xxxx:yyyy 
Possible values: 00000:00000–65535:65535 
Viewing BGP RIB 
You can view the BGP RIB (Routing Information Base) for each neighbor by using the command show rib. 
This command is available in the CLI contexts for IPv4 or IPv6, at the BGP level: 
config>router(<number>)>bgp(<ASN>) #.  
ETX-2i Devices 
5. Traffic Processing 
 To display the IPv4 BGP RIB: 
ETX-2i>config>router(1)>bgp(1)# show rib ipv4 
 
* = Best Route 
   Network            > Next Hop        MED    LocPrf Path  
============================================================================= 
Neighbor 2.2.2.2 
*  0.0.0.0/0          > 172.17.171.1    1000   2000   3000 1000 100 2333 
*  111.222.111.220/30 > 111.222.111.223 65200  65200  4000 800 65500 
Neighbor 33.33.33.33 
   0.0.0.0/0          > 172.17.171.1    1000   2000   3000 1000 100 2333 
   111.222.111.220/30 > 111.222.111.223 65200  65200  4000 800 65500 
 To display the IPv6 BGP RIB: 
ETX-2i>config>router(1)> bgp(1)# show rib ipv6 
* = Best Route 
   Network              > Next Hop             MED    LocPrf Path  
============================================================================= 
Neighbor 2:2:2:2::2 
*  ::/0                 > 11:11:11:11::1       1000   2000   3000 1000 100 2333 
   11:11:11:11::/64     > ::                   1000   2000   3000 1000 100 
*  abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126 
   > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200  65200  4000 80 65500 
Neighbor 33:33:33:33::33 
   ::/0                 > 11:11:11:11::1       1000   2000   3000 1000 100 2333 
*  11:11:11:11::/64     > ::                   1000   2000   3000 1000 100 
   abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126 
   > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200  65200  4000 80 65500 
The above fields are: 
Field 
Description 
Neighbor  
Neighbor IPv4 or IPv6 address 
Status (Best Route) 
Marks with a “*” the ‘Best Route’, i.e., the route entry forwarded to the Router’s RIB 
(Routing Information Base) 
Network 
IPv4 or IPv6 network address (prefix and prefix length) 
IPv4 prefix length can be 0–32; IPv6 prefix length can be 0–128. 
Next hop 
Network prefix and prefix length 
MED 
Number of Multi-exit Discriminators (in decimal value) 
Possible values: 0–4294967295 
LocPrf 
Local preference 
Possible values: 0–4294967295 
ETX-2i Devices 
5. Traffic Processing 
Field 
Description 
Path 
 
Viewing BGP Summary 
You can view the summary of neighbor connections information by using the command show summary. 
This command is available in the CLI contexts for IPv4 and IPv6, at the BGP level: 
config>router(<number>)>bgp(<ASN>) #.  
IPv4 AF connections appear on top, followed by IPv6 AF connections. 
 To display the BGP summary: 
ETX-2i>config>router(1)>bgp(1)# show summary 
Neighbor                                 AS     Up/Down       State 
============================================================================= 
11:11:11:11::205                         209    never         Active 
3.3.3.2                                  3000   never         Idle 
172.17.171.205                           209    12d 06:23:53  Established            2 
172.17.171.218                           209    12d 06:23:53  Active 
abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd  65200  never         Active 
The above fields are: 
Field 
Description 
Neighbor  
Neighbor IPv4 or IPv6 address 
AS  
Remote AS number 
Possible values: 0..35655 or 0..4294967295 
Up/Down  
Amount of time that the underlying TCP connection has been in existence, i.e., how long this 
peer has been in the Established state. 
Note: Up/Down time is set to zero when a new peer is configured, or the router is booted. 
Possible values: 0 - 4294967295 seconds 
When up/down time = 0, displays “never”. 
Otherwise displays in format number of days, hours, minutes, and seconds, for example: 
“12d 06:23:53” 

## Testing BGP  *(p.1117)*

ETX-2i Devices 
5. Traffic Processing 
Field 
Description 
State 
BGP session state 
Possible values are: 
• Idle 
• Connect 
• Active 
• Opensent 
• Openconfirm 
• Established 
Testing BGP 
After configuring BGP on a router in an existing BGP environment, you should test that BGP is working 
properly. 
 To test BGP: 
1. Wait a few seconds after configuration for BGP communications to take place. 
2. For each configured BGP neighbor: 
d. Navigate to the BGP neighbor CLI context 
(config>router(<number>)>bgp(<ASN>)>neighbor(<IP-address>)#). 
e. Enter show neighbor-connection and check that communication has been successfully 
established. 
f. 
Navigate to the IPv4 unicast address family neighbor context 
(config>router(<number>)>bgp(<ASN>)>ipv4-unicast-af> 
neighbor(<IP-address>)#). 
g. Enter show advertised-route and check that the correct destination routes are being 
advertised. 
h. Enter show received-route and check that BGP routes are being received. 
 
 