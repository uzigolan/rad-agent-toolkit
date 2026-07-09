# Feature Reference – 5 Traffic Processing – 5.11 Routing Protocol OSPF

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1118–1138.*


## Applicability and Scaling  *(p.1118)*


## Standards Compliance and MIBs  *(p.1118)*

ETX-2i Devices 
5. Traffic Processing 
3. If IPv6 has been configured for this neighbor: 
a. Navigate to the IPv6 unicast address family neighbor context 
(config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af> 
neighbor(<IP-address>)#). 
b. Enter show advertised-route and check that the correct destination routes are being 
advertised. 
c. Enter show received-route and check that BGP routes are being received. 
4. Navigate out of the BGP context, to the router CLI context. 
5. Enter show routing-table and check that there are new routes marked as originating in BGP. 
5.11 Routing Protocol OSPF 
Open Shortest Path First (OSPF) is a link-state interior-gateway protocol for dynamic routing. The 
current implementation is OSPF v.2 (handles IPv4 only).  
Dynamic routing protocols enable routing tables to automatically adapt to changing networks. Link-state 
dynamic routing protocols such as OSPF quickly adapt to network changes, enable intelligent decisions 
for best routing paths, and are highly scalable. 
All the routers in an Autonomous System (AS) must use the same Interior Gateway Protocol (IGP). 
Applicability and Scaling 
This feature is applicable to ETX­2i and ETX-2i-B. 
Standards Compliance and MIBs 
The current implementation of OSPF adheres to the following standards: 

## Functional Description  *(p.1119)*

ETX-2i Devices 
5. Traffic Processing 
Reference 
Title 
Unsupported Features 
RFC 2328 
OSPF Version 2  
IPv6 (supported only in OSPF v.3) 
Multiple OSPF instances on a router 
Non-Broadcast Multiple Access (NBMA) 
networks 
Area-to-backbone virtual links 
RFC 3101 
The OSPF Not-So-Stubby Area (NSSA) 
Option 
 
RFC 3509 
Alternative Implementations of OSPF 
Area Border Routers 
 
RFC 3623 
Graceful OSPF Restart 
 
RFC 4750 
OSPF Version 2 Management Information 
Base 
 
RFC 4940 
IANA Considerations for OSPF 
 
 
Note 
OSPF does not support the BFD protocol. 
Functional Description 
OSPF functionality is explained in the following sections. 
Show Me Demo 
Click here to view an overview of OSPF. 
Dynamic Routing Protocols 
Routers direct packets through their various interfaces according to their routing tables, which specify 
an exit interface for each destination IP network. While routing tables can include static, manually 
configured routes, an optimized routing table requires knowledge of remote network topology and 
complex path calculations. Dynamic routing protocols define how routers communicate network 
topology with each other and how they accordingly calculate optimized network paths and create their 
routing tables. 
The internet is divided into Autonomous Systems (AS). An AS is usually the network of an Internet 
Service Provider (ISP) or another large organization that administers the AS-internal routing policy. 
ETX-2i Devices 
5. Traffic Processing 
Routing information inside each AS is communicated and determined by an Interior Gateway Protocol 
(IGP) such as OSPF; Routing information between ASes is communicated by the Border Gateway 
Protocol (BGP). 
Link-State Routing 
Link-state routing is one of the two main types of IGPs, along with distance-vector routing. OSPF is a link-
state routing protocol. 
In link-state protocols, each router creates and maintains a relatively full map of network connectivity. 
The connectivity map, called the Link-State Database (LSDB), includes information on which routers are 
connected to which other routers, and each connection’s cost metric, which takes into account factors 
such as roundtrip time, throughput, and link availability. The map’s completeness enables the router to 
intelligently calculate the optimal path from itself to any network destination, without having to rely on 
partial path calculations made in other parts of the network. These optimal paths are used to 
dynamically create a routing table. 
To supply information for LSDBs, each router in the network notifies the network about its own 
immediate neighboring routers and the costs of its connections with them. Routers collect this link-state 
information and issue Link-State Advertisements (LSAs) to their neighbors. Upon receiving an LSA, each 
router updates its LSDB. 
To inform their neighbors of their existence, routers send periodical HELLO messages. When HELLO 
messages stop coming from a router, the connection with that router is considered to have failed, and 
an LSA is generated to inform the network of the lost connection. 
OSPF Network Architecture 
To reduce routing traffic and LSDB size, an AS that uses OSPF is divided into OSPF areas. Each area is a 
group of contiguous networks which appears externally to OSPF as a single unit with an invisible internal 
topology. 
The AS must have a single designated backbone area so that each other area is directly connected to the 
backbone. A router that connects an area to the backbone (that is, it has an interface in the backbone 
and an interface in another area) is called an Area Border Router (ABR). An ABR summarizes its area’s 
topology for external distribution and maintains an LSDB for all areas to which it is connected. 
 
ETX-2i Devices 
5. Traffic Processing 
AS-External Information 
To enable routing to destinations outside the AS, designated Autonomous System Boundary Routers 
(ASBRs) receive topology information about other ASs, and distribute it to internal routers. ASBRs can be 
configured whether to distribute topology from specified external sources (static routes or from BGP). 
However, to reduce traffic, LSDB size, and routing table size, areas can be configured so that only the 
area ABR is aware of the AS-external topology, and the internal routers route traffic with destinations 
outside the AS through the ABR. Two types of such areas can be configured: 
Stub Area 
Cannot originate nor import AS-external topology. Internal routers 
in this area route through the ABR. 
Not So Stubby Area 
(NSSA) 
Cannot originate but can import AS-external topology 
An area which is neither stub nor NSSA is called a transit area. The backbone area must always be a 
transit area. 
Link-State Summarization 
For AS-internal topology information, there is by default no difference between the different types of 
non-backbone areas: ABRs of stub, NSSA and transit (except for backbone) areas summarize AS-internal, 
area-external link-state information for distribution to area-internal routers. However, a stub or NSSA 
ETX-2i Devices 
5. Traffic Processing 
ABR can be optionally configured to suppress summary-LSAs, instead becoming the area’s single default 
gateway. 
Designated Routers 
To reduce network traffic, each network selects a Designated Router (DR) to send LSAs outside of the 
network. A Backup Designated Router (BDR) is also selected in case of DR failure. Routers are selected 
according to configurable router priority indexes (lowest number indicates highest priority). 
Authentication 
OSPF can be configured to perform authentication, in which case OSPF information is accepted only 
from password-authenticated routers. 
Routing Preferences 
When there are conflicts between routes received from different sources, such as static routes, OSPF 
AS-internal routes, and OSPF AS-external routes, the Routing Table Manager (RTM) chooses among the 
sources according to configurable source preference indices (lowest number indicates highest priority).  
Graceful Restart 
OSPF can be configured for Graceful Restart. When Graceful Restart is enabled and a router is restarting 
OSPF, neighboring routers continue to consider the router to be available. 
When a router that is configured for OSPF Graceful Restart is going down in a planned fashion, or it 
begins coming up after an unplanned failure, the router sends a Grace LSA to inform its neighbors to 
consider it available and to continue forwarding traffic to it for a configurable, specified grace time 
period. Neighboring routers can then become Helpers and continue to update the network that there is 
an existing connection with the restarting router. 
Helpers can be configured to enable Strict LSA, in which case neighboring routers terminate the grace 
period if they receive LSAs that should affect the restarting router’s routing paths. 
Graceful Restart is supported only on devices with redundant cards supporting Switch Over and 
database mirroring, so that it is physically possible for traffic forwarding to continue when OSPF is down. 
Enabling Graceful Restart enables both planned and unplanned Graceful Restart. 

## Parameters and Factory Defaults  *(p.1123)*

ETX-2i Devices 
5. Traffic Processing 
Explicit Range Aggregation 
To reduce route lists, explicit ranges can be configured to replace included subnets. Specifically, internal 
IP address ranges can be configured to be summarized by a transit area ABR, or external IP address 
ranges can be aggregated by an NSSA ABR. For a transit area ABR, an internal range can also be 
configured to be hidden from other areas. 
Maintained Information 
OSPF maintains the following network information, all of which can be viewed (see Viewing OSPF 
Status): 
• 
Neighbor list 
• 
Interface information 
• 
LSDB 
• 
LSA counters (see Viewing OSPF Statistics) 
Parameters and Factory Defaults 
OSPF parameters are configured at these levels: 
• 
Configuring OSPF at the Router Level: Parameters that determine OSPF behavior for the whole 
router, for all interfaces 
• 
Configuring OSPF at the Area Level: Parameters that characterize an area, for all interfaces that 
are configured as belonging in this area 
• 
Configuring OSPF at the Interface Level: Per-interface parameters 
Router OSPF Parameters 
The following parameters determine OSPF behavior for the whole router, for all interfaces: 
Parameter 
Description 
Default Value 
asbr 
Whether the router should be an ASBR (distribute AS-
external routes). See AS-External Information. 
no asbr 
external-preference 
Preference index for OSPF AS-external routes. See 
Routing Preferences. 
110 
graceful-restart 
Enable/disable Graceful Restart. See Graceful Restart 
disable 
ETX-2i Devices 
5. Traffic Processing 
Parameter 
Description 
Default Value 
internal-preference 
Preference index for OSPF AS-internal routes. See 
Routing Preferences. 
10 
ospf 
Whether OSPF configuration is defined (but not 
necessarily enabled) on this router 
no ospf 
redistribute 
If an ASBR, whether to distribute routes from specified 
external sources (static or BGP) to the rest of the AS. See 
AS-External Information. 
no redistribute 
restart-interval 
Grace period, in seconds, for Graceful Restart. See 
Graceful Restart 
120 
router-id 
ID for router in OSPF communications, in format like IP 
address. Must be unique in AS 
-- 
(mandatory configuration) 
strict-lsa-checking 
Enable/disable Strict LSA mode on Graceful Restart 
Helper. See Graceful Restart. 
disable 
shutdown 
Enable (no shutdown) / disable (shutdown) OSPF on the 
router. 
shutdown 
Area OSPF Parameters 
The following parameters characterize an area (see OSPF Network Architecture), for all interfaces that 
are configured as belonging in this area: 
Parameter 
Description 
Default Value 
area-id 
ID for area in OSPF communications. Must be unique in AS. 
Format is like IP address. Can be same as IP address of a 
network in the area. Backbone area must have ID 0.0.0.0 
-- 
default-cost 
Cost metric of default route, for stub area ABR to advertise 
into the area. See Link-State Routing. 
1 
nssa 
Whether the area is NSSA, and whether the area ABR will 
provide area routers with summary LSAs (or just rely on its 
default route). See AS-External Information and Link-State 
Summarization. 
no nssa, no-summary 
range 
Internal IP address range(s) to be summarized or hidden by a 
transit area ABR, or external IP address range(s) to be 
aggregated by an NSSA ABR. See Explicit Range Aggregation. 
-- 
shutdown 
Enable (no shutdown) / disable (shutdown) the area 
shutdown 
ETX-2i Devices 
5. Traffic Processing 
Parameter 
Description 
Default Value 
stub 
Whether the area is a stub area, and whether the area ABR 
will provide area routers with summary LSAs (rather than 
just rely on its default route). See AS-External Information 
and Link-State Summarization. 
no stub, no-summary 
Interface OSPF Parameters 
The following parameters determine OSPF behavior per-interface: 
Parameter 
Description 
Default Value 
area 
ID of area to which interface belongs. See OSPF Network 
Architecture. 
no area 
authentication-key 
Password for OSPF authentication. See Authentication. 
-- 
authentication-type 
Whether OSPF information should be password-
authenticated. See Authentication. 
no authentication 
dead-interval 
Time after which the connection with a silent neighbor is 
considered failed. See Link-State Routing. 
40 
hello-interval 
Time, in seconds, between sending HELLO packets. See Link-
State Routing. 
10 
metric  
Explicit network cost of the interface for OSPF path 
calculation. See Link-State Routing. 
1 
ospf 
Whether OSPF configuration is defined (but not necessarily 
enabled) on this interface 
no ospf 
passive 
Whether OSPF packets can (no passive) or cannot (passive) 
be sent through this interface 
no passive 
priority 
Priority index for becoming DR or BDR. See Designated 
Routers. 
128 
retransmit-interval 
Time, in seconds, between retransmissions of 
unacknowledged adjacency LSAs and of other network 
advertisements. See Link-State Routing. 
5 
shutdown 
Enable (no shutdown) / disable (shutdown) OSPF on the 
interface 
shutdown 
transit-delay 
Time, in seconds, to be added to the LSA’s age before 
transmission. Should be the estimated time of LSA 
transmission over the interface including propagation delays 
1 

## Configuring OSPF  *(p.1126)*

ETX-2i Devices 
5. Traffic Processing 
Configuring OSPF 
OSPF is not configured by default on RAD routers. On a router that does not have OSPF defined, once 
the router itself and its interfaces have been properly configured, you can configure OSPF. To configure 
OSPF properly, you will need to know your network OSPF design. 
 To configure OSPF on a fresh router: 
1. Define OSPF on the router by entering the following commands in the device CLI: 
configure 
router <number> 
ospf 
OSPF is defined on the router, and the CLI ospf context is provided. 
2. In the router ospf context, define the router ID: 
router-id <id> 
where <id> is an ID for the router in OSPF communications, in IP address format (<0-255>.<0-
255>.<0-255>.<0-255>). The ID must be unique in the AS. To simplify management, the ID can 
be the actual IP address of one of the router’s interfaces, or there may be some other 
organizational convention. 
3. Where network design requires that this router have non-default values (see Parameters and 
Factory Defaults) for any router-level OSPF parameters, configure them (see Configuring OSPF 
at the Router Level). 
4. Still in the router ospf context, enable OSPF on the router by entering: 
no shutdown 
5. Configure each OSPF area (see OSPF Network Architecture) that the router should be in 
according to network design: 
a. In the router OSPF context (config>router(<router_number>)>ospf#), define the are ID: 
area <area-id> 
where <area-id> is an ID for the area in OSPF communications, in IP address format (<0-
255>.<0-255>.<0-255>.<0-255>). The ID must be unique in the AS. To simplify management, 
the ID can be the actual IP address of a network in the area, or there may be some other 
organizational convention. The backbone area ID must be 0.0.0.0 . 
The area is defined, and the CLI area context is provided. 
b. In the area context (config>router(<router_number>)>ospf>area(<area-id>)#): 
 
If according to network design the area should be a stub area, enter: 
stub 
ETX-2i Devices 
5. Traffic Processing 
 
If according to network design the area should be an NSSA area, enter: 
nssa 
c. Where network design requires that this router have non-default values (see Parameters 
and Factory Defaults) for any area-level OSPF parameters, configure them (see Configuring 
OSPF at the Area Level). 
d. Still in the area context, enable the area by entering: 
no shutdown 
An enabled area means that OSPF interfaces connected to it can be enabled, and that the 
area’s type (stub / NSSA / transit) cannot be changed. 
e. Exit the area context. 
6. Exit the router OSPF context to return to the router CLI context. 
7. Configure OSPF on each interface: 
a. Go into the interface CLI context (config>router(<router_number>)> 
interface(<interface_number>)#), and define OSPF on the interface: 
ospf 
OSPF is defined on the interface, and the CLI interface ospf context is provided. 
b. In the interface OSPF context, set the area with which to associate the interface: 
area <area-id> 
where <area-id> is the area’s ID, according to network design. 
c. Where network design requires that this interface have non-default values (see Parameters 
and Factory Defaults) for any interface-level OSPF parameters, configure them (see 
Configuring OSPF at the Interface Level). 
d. Still in the interface OSPF context, activate OSPF on the interface by entering: 
no shutdown 
e. Exit the interface OSPF context and exit the interface context. 
Configuring OSPF at the Router Level 
The following commands are available in the CLI router OSPF context: 
config>router(<router_number>)>ospf# . The exception to this is the ospf command itself, which is 
performed in the router context: config>router(<router_number>)# . 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Define OSPF on the 
router (if not yet 
defined), and provide 
the router CLI ospf 
context 
[no] ospf 
After defining OSPF on the router, OSPF still needs 
to be enabled (after setting router-id) with no 
shutdown. 
no ospf removes OSPF from the router (if no areas 
are defined). 
Define ID for the router 
in OSPF 
communications 
router-id <id> 
<id> is in IP address format: <0-255>.<0-255>.<0-
255>.<0-255> . The ID must be unique in the AS. 
To simplify management, the ID can be the actual 
IP address of one of the router’s interfaces, or 
there may be some other organizational 
convention. 
Enable / disable OSPF 
on the router 
[no] shutdown 
To disable: shutdown . To enable: no shutdown 
Define / remove OSPF 
area, with an ID for the 
area in OSPF 
communications 
[no] area <area-id> 
<area-id> is in IP address format: <0-255>.<0-
255>.<0-255>.<0-255>. The ID must be unique in 
the AS. To simplify management, the ID can be the 
actual IP address of a network in the area, or 
there may be some other organizational 
convention. The backbone area ID must be 0.0.0.0  
no area <area-id> removes the area from router 
OSPF configuration (if the area is not associated 
with any interfaces). 
To further configure the area, see Configuring 
OSPF at the Area Level 
Make router an ASBR 
(=distribute AS-external 
routes) 
[no] asbr 
OSPF must be disabled to run this command. 
See AS-External Information. 
Set ASBR to distribute 
routes from specified 
external sources (static 
or BGP) to the rest of 
the AS, or disable 
distribution 
[no] redistribute { static | bgp } 
To disable distribution: no redistribute. 
See AS-External Information. 
Set preference index for 
OSPF AS-external routes 
external-preference <priority> 
<priority> should be an integer in range 0-255. 
See Routing Preferences. 
Set preference index for 
OSPF AS-internal routes 
internal-preference <priority> 
<priority> should be an integer in range 0-255. 
See Routing Preferences. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Enable/disable Graceful 
Restart 
[no] graceful-restart 
To disable, use no graceful-restart. 
See Graceful Restart. 
Set grace period, in 
seconds, for Graceful 
Restart 
restart-interval <seconds> 
<seconds> should be in the range 1-1800. 
See Graceful Restart. 
Enable/disable Strict 
LSA mode on Graceful 
Restart Helper 
[no] strict-lsa-checking 
To disable, use no strict-lsa-checking. 
See Graceful Restart. 
View counters of LSAs 
show statistics 
See Viewing OSPF Statistics. 
View Link-State 
Database (LSDB) 
show database 
See Viewing OSPF Status.  
View OSPF interface 
information 
show interface-table 
View OSPF neighbors 
show neighbor-table 
Configuring OSPF at the Area Level 
The following commands are available in the CLI OSPF area context: 
config>router(<router_number>)>ospf>area(<area-id>)# . Note that the area command, which is 
performed in the router OSPF context: config>router(<router_number>)>ospf#, appears under 
Configuring OSPF at the Router Level. 
Task 
Command 
Comments 
Make area a stub area, 
or change a stub area 
back to a transit area 
[no] stub [summary | 
no-summary] 
All routers in a stub area must be configured as 
such. See AS-External Information. 
This command is effective regardless of the area’s 
current type (transit or NSSA). 
For the area ABR to just rely on its default route 
rather than provide area routers with summary 
LSAs, use stub no-summary. For it to go back to 
providing summary LSAs, use stub summary. See 
Link-State Summarization. 
To change a stub area back to a transit area, use no 
stub 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Make area an NSSA 
area, or change an 
NSSA area back to a 
transit area 
[no] nssa [summary | 
no-summary] 
All routers in an NSSA area must be configured as 
such. See AS-External Information. 
This command is effective regardless of the area’s 
current type (transit or stub). 
For the area ABR to just rely on its default route 
rather than provide area routers with summary 
LSAs, use nssa no-summary. For it to go back to 
providing summary LSAs, use nssa summary. See 
Link-State Summarization. 
To change an NSSA area back to a transit area, use 
no nssa 
Set cost metric of 
default route, for stub 
area ABR to advertise 
into the area 
default-cost <metric> 
Use only on stub area ABR.  
Possible values: 1–16777215 (24-bit) 
See Link-State Routing. 
Set internal IP address 
range(s) to be 
summarized or hidden 
by a transit area ABR, or 
external IP address 
range(s) to be 
aggregated by an NSSA 
ABR 
[no] range <ip-address>/ 
<mask-length> [advertise | 
not-advertise] [nssa] 
To set internal transit area summarization, on the 
transit ABR use: range <ip-address>/<mask-length> 
advertise . 
To set internal transit area hiding, on the transit 
ABR use: range <ip-address>/<mask-length> not-
advertise. 
To set external NSSA aggregation, on the NSSA ABR 
use range <ip-address>/<mask-length> advertise 
nssa. 
<ip-address> should represent an IP range, in IP 
address format. <mask-length> should be an integer 
in range 1–32, representing the number of first bits 
in <ip-address> that are the network mask. 
To delete a configured range, use: no range <ip-
address>/<mask-length>. 
See Explicit Range Aggregation. 
Enable / disable the 
area 
[no] shutdown 
To disable: shutdown. To enable: no shutdown 
 
 
ETX-2i Devices 
5. Traffic Processing 
Configuring OSPF at the Interface Level 
The following commands are available in the CLI interface OSPF context: 
config>router(<router_number>)>interface(<interface_number>)>ospf#. The exception to this is the 
interface ospf command, which is performed in the interface OSPF context: 
config>router(<router_number>)>interface(<interface_number>)# . 
 
Task 
Command 
Comments 
Define OSPF on the 
interface (if not yet 
defined), and provide the 
interface CLI ospf context 
ospf 
After defining OSPF on the interface, OSPF still 
needs to be enabled (after associating the 
interface with an area) with no shutdown. 
no ospf removes OSPF from the interface (if no 
areas are defined) 
Associate interface with an 
area 
[no] area <area-id> 
Specify the area with its <area-id>. 
To disassociate the interface from any area, 
use no area <area-id>. 
Enable / disable OSPF on 
the interface 
[no] shutdown 
To disable: shutdown. To enable: no 
shutdown 
Set the time between 
sending HELLO packets 
hello-interval <seconds> 
<seconds> should be in range 1–65535 
See Link-State Routing. 
Set the time after which 
the connection with a silent 
neighbor is considered 
failed 
dead-interval <seconds> 
Possible values: 1–2147483647 
See Link-State Routing. 
Set the priority index for 
becoming DR or BDR 
priority <priority> 
Possible values: 0–255. 
See Designated Routers 
Set the time to be added to 
the LSA’s age before 
transmission 
transit-delay <seconds> 
The estimated time of LSA transmission over 
the interface including propagation delays 
Possible values: 0–3600 
Set the time between 
retransmissions of 
unacknowledged adjacency 
LSAs and of other network 
advertisements 
retransmit-interval <seconds> 
Possible values: 0–3600 
See Link-State Routing. 

## Configuration Example  *(p.1132)*

ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Prevent OSPF packets from 
being sent through the 
interface 
[no] passive 
A passive interface is still advertised as an 
OSPF interface but doesn’t itself run the OSPF 
protocol. 
To re-enable sending OSPF packets, use no 
passive 
Set password 
authentication for OSPF 
communications 
[no] authentication-type 
[simple-password] 
To set authentication, use: authentication-
type password. To disable authentication, use: 
no authentication. 
See Authentication. 
Set password for OSPF 
authentication, if enabled 
authentication-key 
<authentication-key> [hash] 
<authentication-key> can be any combination 
of up to 8 ASCII characters. Use the hash 
option to specify that the provided key should 
be encrypted, in which case the key can be up 
to 22 characters. 
See Authentication. 
Explicitly set the network 
cost of the interface for 
OSPF path calculation 
metric <number> 
Possible values: 1–65535 
See Link-State Routing. 
Configuration Example 
In this example, a router needs to be configured for OSPF. According to network design, this router is a 
stub area ABR with two interfaces, one in the backbone and one in a stub area. Authentication is used in 
both areas, but each area uses a different password. 
The relevant part of the network design is: 
Router ID 
Interface 
Area 
Password 
10.10.1.1 
Interface 1 
0.0.0.0 
12345672 
Interface 2 
10.10.0.0 
abcdefgh 
 
 

## Configuration Errors  *(p.1133)*

ETX-2i Devices 
5. Traffic Processing 
The actual configuration process for this example is: 
configure 
router 1 
remark Configure OSPF on router 
ospf 
router-id 10.10.1.1 
no shutdown 
remark Configure OSPF Areas 
area 0.0.0.0 
no shutdown 
exit 
area 10.10.0.0 
stub no-summary 
no shutdown 
exit 
exit 
remark Configure OSPF with authentication on interfaces 
interface 1 
ospf 
area 0.0.0.0 
authentication-type simple-password 
authentication-key 12345678 
no shutdown 
exit 
exit 
interface 2 
ospf 
area 10.10.0.0 
authentication-type simple-password 
authentication-key abcdefgh 
no shutdown 
exit 
exit 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Cannot be modified; OSPF 
interface is administratively 
enabled 
You tried to associate an 
interface with an area, but the 
interface is OSPF-enabled 
Enter shutdown and try again. 
Cannot create OSPF interface; IP 
address wasn’t configured 
You tried to run ospf in the 
interface context, but the 
interface itself has no fixed IP 
address (it is possibly DHCP) 
Set a fixed IP address for the interface. 
ETX-2i Devices 
5. Traffic Processing 
Message 
Cause 
Corrective Action 
Cannot create OSPF interface; 
more than one IP address is 
configured 
You tried to run ospf in the 
interface context, but the 
interface itself has multiple IPv4 
addresses 
Remove interface IP addresses to 
leave only one and try again. 
Cannot delete area; There is an 
OSPF interface associated with 
the Area 
You tried to run no area (router 
OSPF context) on an area 
associated with an interface 
Go to the relevant interface OSPF 
context and enter no area <area-id>. 
Cannot delete ospf; ospf area or 
OSPF interface exist 
You tried to run no ospf (router 
context) with existing areas or 
OSPF interfaces 
Remove OSPF from all interfaces, 
delete all areas, and try again. 
cannot enable OSPF interface; 
area-id is not defined 
You tried to enable OSPF on an 
interface without an associated 
area 
Set an area for the interface and try 
again. 
Cannot enable OSPF; router-id is 
not configured 
You tried to run no shutdown 
(router OSPF context) with no 
OSPF router ID 
Set router-id and try again. 
Cannot enable redistribute; ASBR 
disabled 
You tried to run the redistribute 
command on a non-ASBR router 
If by network design this router should 
be an ASBR, enter asbr and try again. 
Cannot execute, license required 
You tried to run ospf (router 
context) without an OSPF license 
Contact your RAD sales representative 
to obtain a license. 
Cannot modify area parameter; 
area is administratively enable 
You tried to make an enabled 
area into a stub or NSSA 
Enter shutdown and try again. 
Cannot modify; OSPF is enabled 
You tried to change router-id or 
asbr with OSPF enabled 
Enter shutdown and try again. 
Cannot set area as nssa; area-id 
0.0.0.0 cannot be nssa 
You tried to make the backbone a 
stub or NSSA 
If this is not the backbone, change the 
area ID and try again. 
Cannot set metric; Area is a 
Transit 
You tried to run the default-cost 
command on a transit area 
If this area should be a stub area, 
enter stub and try again. 
Cannot set ranges for external 
routes for non NSSA 
You tried to run the range 
command with the nssa option, 
on a non-NSSA area 
If this area shouldn’t be an NSSA, 
enter no nssa and try again. 
OSPF entity shall be initiated 
before interface’s configuration 
You tried to run OSPin the 
interface context, but OSPF 
hasn’t been defined on the 
router 
Exit the router context and enter ospf. 
Then try again. 

## Viewing OSPF Status  *(p.1135)*

ETX-2i Devices 
5. Traffic Processing 
Viewing OSPF Status 
You can view the current configuration (see Viewing the Current Configuration), and you can also view 
several types of dynamic and traffic-based OSPF information (see sections below). This information can 
be used for testing (see Testing OSPF) and debugging. 
Viewing the Current Configuration 
To view the current configuration, use the standard RAD commands: info (to view only non-default 
configuration) and info detail (to include default configuration). 
You can view this info at any of the following configuration levels: 
Level 
Context Prompt 
Router 
config>router(<router_number>)>ospf# 
Area 
config>router(<router_number>)>ospf>area(<area-id>)#  
Interface 
config>router(<router_number>)>interface(<interface_number>)>ospf# 
For example: 
rad_os_p# configure 
rad_os_p>config# router 1 
rad_os_p>config>router(1)# ospf 
rad_os_p>config>router(1)>ospf# info detail 
 
router-id 1.2.3.4 
 
no asbr 
 
external-preference 110 
 
internal-preference 30 
 
no graceful-restart 
 
restart-interval 120 
 
strict-lsa-checking 
 
shutdown 
 
echo "OSPF AREA Configuration" 
# 
OSPF AREA Configuration 
 
area 0.0.0.0 
 
 
no nssa 
 
 
no stub 
 
 
no shutdown 
 
exit 
 
rad_os_p>config>router(1)>ospf# 
ETX-2i Devices 
5. Traffic Processing 
Viewing the Link-State Database 
You can view the current Link-State Database (LSDB) by using the show database command. This 
command is available in the CLI router OSPF context: (config>router(<router_number>)>ospf#), and can 
be used for testing (see Testing OSPF) and debugging. 
For example: 
Area ID 
Type 
LS ID Router ID 
Sequence 
Age 
Checksum 
-------------------------------------------------------------------------------- 
100.100.100.100 
1 
000.000.010.010 
000.000.010.010 
0x80000096 
938
 
0x609b 
100.100.100.100 
1 
050.050.050.020 
050.050.050.020 
0x80000006 
839
 
0x49d4 
000.000.000.000 
2 
020.020.020.020 
020.020.020.030 
0x80000008 
946
 
0x3c3a 
000.000.000.000 
3 
050.050.050.000 
000.000.010.010 
0x8000000d 
764
 
0xcbd9 
000.000.000.000 
4 
000.000.010.010 
050.050.050.020 
0x80000002 
840
 
0x83f7 
The above fields are: 
Field 
Description 
Area ID 
<area-id> of an OSPF area 
Type 
One of the following LSA types: 
• 1 – Router-LSA: Describes collected states of router's interfaces 
• 2 – Network-LSA: Describes routers attached to network 
• 3 – Network summary-LSA: Describes inter-area routes to networks, summarized by ABR 
• 4 – ASBR summary-LSA: Describes inter-area routes to ASBRs, summarized by ABR 
• 5 – AS-external-LSA: Originated by ASBR, describes routes to AS-external destinations or a 
default route for the AS 
• 7 – NSSA-external-LSA: Describes external route information within an NSSA 
LS ID 
Router ID or IP address (depending on Type) of domain described by the LSA 
Router ID 
ID of originating router 
Sequence 
Signed 32-bit integer, incremented each time the router originates a new instance of the LSA. 
Used to detect old and duplicate LSAs 
Age 
LSA age in seconds 
Checksum 
Checksum of complete LSA contents except for Age field 
ETX-2i Devices 
5. Traffic Processing 
Viewing OSPF Interface States 
You can view current interface states by using the show interface-table command. This command is 
available in the CLI router OSPF context: (config>router(<router_number>)>ospf#) and can be used for 
testing (see Testing OSPF) and debugging. 
For example: 
IP Address 
Area ID 
Type 
Priority 
DR 
BDR 
State 
------------------------------------------------------------------------------------- 
000.000.000.000 
000.000.000.001 
P-T-P 0001 
000.000.000.000 
000.000.000.000
 
Down 
192.168.001.001 
000.000.000.003 
BRDCST 0001 
192.168.001.007 
192.168.001.002
 
Up 
The above fields are: 
Field 
Description 
IP Address 
Interface IP address 
Area ID 
ID of area with which the interface is associated 
Type 
Broadcast or point-to-point 
Priority 
Priority index for becoming DR or BDR 
DR 
Designated Router in this network 
BDR 
Backup Designated Router in this network 
State 
UP if all of the following are true: OSPF is enabled (no shutdown), the IP interface’s 
operational status is UP, and the OSPF interface is enabled (no shutdown) 
Viewing OSPF Neighbors 
You can view the current OSPF neighbors by using the show neighbor-table command. This command is 
available in the CLI router OSPF context: (config>router(<router_number>)>ospf#) and can be used for 
testing (see Testing OSPF) and debugging. 
For example: 
Neighbor 
Neighbor ID 
Priority 
State Interface 
Port 
---------------------------------------------------------------------------- 
192.168.001.003 
192.168.001.009 
0001 
Full 
192.168.001.002 
Ethernet 0 
192.168.001.007 
000.000.000.004 
0004 
Full 
192.168.001.002 
Ethernet 0 
10.10.001.001 000.000.000.005 
0005 
Full 
10.10.001.002 Ethernet 1 
The above fields are: 

## Viewing OSPF Statistics  *(p.1138)*

ETX-2i Devices 
5. Traffic Processing 
Field 
Description 
Neighbor 
IP address used by this neighbor as its source address  
Neighbor ID 
The neighbor’s OSPF router-id 
Priority 
The neighbor’s priority index for becoming DR or BDR 
State 
The state of the connection with this neighbor. One of: 
• Down 
• Attempt 
• Init 
• Twoway 
• Exchangestart 
• Exchange 
• Loading 
• Full 
Interface 
IP address of the neighbor’s interface with which a connection is established 
Port 
Name of the neighbor’s interface with which a connection is established 
Viewing OSPF Statistics 
You can view LSA counters by using the show statistics command. This command is available in the CLI 
router OSPF context: (config>router(<router_number>)>ospf#). 
For example: 
 
Count Checksum 
-------------------------------------- 
External LSA 50 
0x3245 
AS LSA  
1059 
0x7843 
New LSAs Originated 45 
- 
New LSAs Received 
1024 
- 
The above fields are: 
Field 
Description 
Count 
The number of LSAs of this type 
Checksum 
32-bit sum of the checksums of the LSAs of this type. Can be used to check if an LSDB has 
changed or to compare LSDBs. 