# Feature Reference – 5 Traffic Processing – 5.1 Bridge

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 863–891.*


## Applicability and Scaling  *(p.863)*


## Standards Compliance  *(p.863)*

5 Traffic Processing 
5.1 Bridge 
The ETX-2i bridge, a Layer-2 VLAN-aware or VLAN-unaware forwarding entity, delivers E-LAN and E-Tree 
services. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products, with the following conditions: 
• 
PCS port is relevant to ETX-2i with an SHDSL or VDSL2 module. 
• 
RSTP/MSTP is not applicable to ETX-2i-100G. 
• 
DHCP Layer-3 Relay for bridge is applicable to a device with an embedded router or bridge. 
• 
There is one configurable bridge per device. 
• 
Number of bridge ports are as follows: 
 
Up to 44 for ETX-2i, ETX-2i-B 
 
Up to 80 for ETX-2i-10G, ETX-2i-100G  
 
Up to 32 for ETX-2i-10G-B/8SFPP (full and half 19-inch) 
 
Up to 128 for ETX-2i-10G-E 
Standards Compliance 
IEEE 802.1D 
IEEE 802.1Q  
IEEE 802.1ad 

## Functional Description  *(p.864)*

ETX-2i Devices 
5. Traffic Processing 
Functional Description 
The bridge can operate in VLAN-aware or VLAN-unaware mode. 
When the bridge works in VLAN-aware mode: 
• 
Bidirectional flows are supported. 
• 
Each VLAN can work in E-LAN or E-Tree mode. 
When the bridge works in VLAN-unaware mode: 
• 
Bidirectional flows are not supported.  
• 
Only one egress flow per bridge port can be configured. 
• 
The bridge can work in E-LAN or E-Tree mode. 
Traffic through the bridge is configured via flows between non-bridge ports (e.g., Ethernet, ETP, logical 
MAC, PCS, SVI) and bridge ports, allowing editing action at the bridge ports.  
Note 
• 
Flow classifications source/destination MAC address or source/destination 
IP address are not supported via bridge. 
• 
If flows use the same queue before relevant MAC addresses are learned, 
the policing does not function properly. 
Different flows from the same port can be mapped to different bridge ports. However, different flows 
from one bridge port cannot be mapped to different ports, with the exception that multiple SVIs can be 
mapped to the same bridge port. 
 
Flows Mapped from Same Port to Different Bridge Ports – Allowed  
ETX-2i Devices 
5. Traffic Processing 
Flows Mapped from Same Bridge Port to Different Ports (other than SVI) – Not Allowed 
Admission to Bridge 
In order for a frame to be admitted to the bridge, its classification must match the flow classification 
configured for the bridge port. 
In VLAN-aware mode, VLAN membership is read-only and automatically learned from the VLAN 
classification used in bridge port flows. Additionally, flows with untagged classification must have a push 
editing action. 
In VLAN-unaware mode, any packet may be admitted according to the configured flow classifications. 
Packet Editing on Reverse Flows 
In the case of a bidirectional flow, the editing action can be specified for the flow to the bridge port, but 
not for the reverse direction. ETX-2i performs editing on the reverse direction according to the flow 
classification and specified editing actions. The following table shows the editing action on the reverse 
flow, as well as the VLAN learned from the flow. 
Classification 
Editing of Flow with Bridge 
Port as Egress Port 
Editing of Reverse 
Directional Flow  
VLAN Value 
VLAN X + any 
None  
None 
X 
VLAN X..Y 
None  
Not allowed 
Not allowed 
Untagged 
None  
None 
Not supported; use 
push action  
VLAN X   
Inner VLAN Y 
None 
None 
X 
ETX-2i Devices 
5. Traffic Processing 
Classification 
Editing of Flow with Bridge 
Port as Egress Port 
Editing of Reverse 
Directional Flow  
VLAN Value 
Any classification 
(including untagged) 
Push X  
p-bit fixed/copy/profile  
Pop 
X 
Any classification 
(including untagged and 
all) 
Push X push inner Y 
p-bit and inner p-bit 
fixed/copy/profile 
Pop twice 
X 
VLAN X   
Inner vlan Y 
Pop 
Push X 
Y 
VLAN X 
Inner vlan Y..Z 
Pop 
Not allowed 
Not allowed 
VLAN X 
Pop 
Not allowed 
Not allowed 
VLAN X + any  
Swap VLAN Y 
p-bit fixed/copy/profile  
Swap VLAN X 
Y 
VLAN X   
Inner VLAN Y 
Swap VLAN Z 
p-bit fixed/copy/profile 
Swap VLAN X 
Z 
VLAN Y..Z 
Swap VLAN Y 
p-bit fixed/copy/profile 
Not allowed 
Not allowed 
VLAN X 
Push VLAN Y, swap VLAN Z 
p-bit fixed/copy/profile 
Pop, swap X 
Y 
VLAN Y..Z 
Push VLAN X, swap VLAN Z 
p-bit fixed/copy/profile 
Not allowed 
Not allowed 
VLAN X  
Inner VLAN Y 
Pop, swap VLAN Z 
p-bit fixed/copy/profile 
Push X  
Inner swap to Y 
Z 
VLAN X 
Inner VLAN Y..Z 
Pop, swap 200 
p-bit fixed/copy/profile 
Not allowed 
Not allowed 
VLAN X  
Inner VLAN Y 
Swap VLAN Z,  
inner swap VLAN K 
p-bit fixed/copy/profile 
Swap X, inner swap Y 
Z 
VLAN X 
Inner VLAN Y..Z 
Swap VLAN Z,  
inner swap VLAN K 
p-bit fixed/copy/profile 
Not allowed 
Not allowed 
ETX-2i Devices 
5. Traffic Processing 
Management via Bridge 
In order to manage via the bridge, you need to configure the following (see VLAN-Aware Bridge for an 
example of configuring the bridge for management): 
• 
Router interface for management, bound to SVI 
• 
Flow between SVI and bridge port (only one SVI<->bridge port flow can be created per bridge 
port) 
• 
Flow between Ethernet port and bridge port 
 
Note 
It is recommended to manage ETX-2i via the bridge only if the bridge is 
VLAN-aware. 
DHCP Layer-3 Relay for Bridge 
ETX-2i supports a DHCP Layer-3 Relay agent to pass DHCP requests and replies between clients and 
servers that are not on the same subnet. 
For a detailed description of the DHCP Layer-3 Relay model for Bridge, see DHCP Layer-3 Relay below. 
Spanning Tree Protocol 
Spanning Tree Protocol (STP) (802.1Q; previously 802.1D) is a Layer-2 loop avoidance technique used in 
Ethernet networks. Loops are created in bridge-based networks with more than one path between two 
endpoints. STP is used to identify the best path to the destination and block all other paths. The blocked 
links are connected and kept inactive, creating automatic backup links. 
The figure below illustrates STP operation. Bridge 3 is directly connected to Bridge 1 and Bridge 2. 
Another physical link directly connects Bridge 1 to Bridge 2. Under normal conditions, there is looping of 
data, causing broadcast congestion on the network. When an STP is applied, Link A is blocked from 
transmitting any data, but it remains on standby and listens to the network. If Link B or Link C fails, Link 
A is activated, providing link and switch redundancy in the network. 
ETX-2i Devices 
5. Traffic Processing 
STP Operation 
ETX-2i supports a single STP instance per chassis. 
STP Bridge Types 
The root bridge is the central reference bridge in the STP. It serves as a reference for other bridges to 
determine their best cost path. Bridge 3 in the figure below serves as a root in the application. 
The root bridge is elected by automatically selecting the bridge in the network with the lowest bridge ID. 
If the root bridge fails, the other bridges select a new root device.  
Link Cost 
Each link in the network is allocated a certain cost. Usually, higher-bandwidth links that are adjacent to 
the root bridge are assigned a lower cost. Lower-bandwidth links that are multiple hops away from the 
root bridge are assigned a higher cost. Once link costs are estimated, STP determines the lowest cost 
connections from each bridge to the root bridge to determine the lowest-cost path. It also blocks all the 
other higher cost links to prevent loops in the network.  
Bridge Protocol Data Units 
The bridges use Bridge Protocol Data Units (BPDUs) to exchange information about network topology, 
bridge IDs, link costs etc. BPDUs help establish the best route (least cost path) to the root bridge. 
When there is a change in the network, relevant BPDUs are sent to all the bridges/bridge ports by the 
root bridge. The bridges adjust their tables to determine the new routes to the terminals. 
 
 
Bridge 1
Bridge 2
Bridge 3
Bridge 1
Bridge 2
Bridge 3
Link A
Link B
Link C
Link A
Link B
Link C
Physical Topology
Logical Topology
ETX-2i Devices 
5. Traffic Processing 
Rapid Spanning Tree Protocol and Multiple Spanning Tree Protocol 
Rapid Spanning Tree Protocol (RSTP) (802.1Q; previously 802.1W) is an evolution of STP with some 
protocol enhancements, providing significantly faster spanning tree convergence following a topology 
change. In RSTP, the link status of each port is monitored proactively (instead of waiting for the BPDU 
messages) to detect changes in network topology. 
ETX-2i supports a single instance of RSTP over a VLAN aware or VLAN unaware bridge (ETX-2i supports 
only one bridge).  
Multiple Spanning Tree Protocol (MSTP) (802.1Q; previously 802.1S) supports several instances of 
forwarding topology on the same physical topology for load balancing purposes (per a group of VLANs). 
MSTP is supported over a VLAN-aware bridge only. MSTP maps a group of VLANs (that have been 
configured at the bridge ports) into a single Multiple Spanning Tree instance (MSTI). This means that the 
Spanning Tree Protocol is applied separately for a set of VLANs instead of every VLAN in the whole 
network. Different root bridges and different STP parameters can be individually configured for each 
MSTI. So, one link can be active for one MSTI and the other link active for the second MSTI. This enables 
some degree of load-balancing and generally two MSTIs are used in the network for easier 
implementation. ETX-2i supports up to 16 MSTIs per chassis, excluding MSTI0 (IST). All VLANs in the 
bridge that are not configured to a specific MSTI, belong to MSTI0 (IST). 
The figure below illustrates MSTP operation. MSTI 1 is used for forwarding traffic marked with VLANs 10 
and 20; MSTI 2 is used for VLANs 30 and 40; MSTI 0 – for the remaining VLANs in the network. 
Bridge 1
Bridge 2
Bridge 3
Bridge 1
Bridge 2
Bridge 3
Physical Topology
MSTI 0 Logical Topology
Bridge 1
Bridge 2
Bridge 3
MSTI 1 Logical Topology
Bridge 1
Bridge 2
Bridge 3
MSTI 2 Logical Topology
Root
Root
Root
 
RSTP and MSTP uses OOB MNG MAC as the Bridge Identifier.  
ETX-2i Devices 
5. Traffic Processing 
Note 
Before using RSTP or MSTP, you are required to configure trapping of  
01-80-C2-00-00-00 using an L2CP profile with a peer action for  
01-80-C2-00-00-00. 
ETX-2i supports RSTP and MSTP per 802.1Q over a bridge with the following port types:  
• 
Ethernet User  
• 
Ethernet Network  
• 
PCS  
• 
Logical MAC 
Note 
ETX-2i does not support RSTP and MSTP over a bridge with the following port 
types:  
• 
OOB 
• 
LAG group 
• 
Ports configured with ETH protection 
• 
Ports configured as G.8032 ring nodes 
• 
Ports not connected to a physical port (such as a router interface or MEF 8 
PW) 
STP interoperability is supported per bridge port; when the RSTP/MSTP bridge identifies STP messages 
on a port, it reverts to STP mode on that port.  
MAC Address Learning (for Bridge) 
ETX-2i supports a Bridge MAC table containing learned MAC addresses. ETX-2i supports searching for a 
specific MAC address, or all MAC addresses of a specific VLAN. It also supports searching for all dynamic 
MACs, static MACs, or both. The retrieved information includes: VLAN, MAC address, Bridge port, and 
status (Dynamic/Static). See Viewing Learned MAC Addresses on Bridge below. 
Note 
ETX-2i also supports a MAC table at the Flow level, which includes all MAC 
addresses learned for a specific flow, regardless of whether the flow is 
connected to a bridge port. See MAC Address Learning Per Flow below. 
Duplicate MAC Rejection 
The ETX-2i family supports duplicate MAC rejection for both VLAN aware (duplicate MAC+VLAN) and 
VLAN unaware (duplicate MAC) bridges. 

## Factory Defaults  *(p.871)*

ETX-2i Devices 
5. Traffic Processing 
When duplicate MAC rejection is enabled, the following describes the processing of a duplicate packet 
that enters the bridge in a different port than an existing MAC entry: 
• 
The MAC entry does not change (no learning). 
• 
The frame is dropped. 
• 
A Duplicate MAC event is issued. 
• 
A Duplicate MAC event is sent if no other event was sent in the last five minutes. 
A Duplicate MAC event at the bridge port level (Ingress bridge port of the duplicate MAC) is issued once 
for all the different duplicate entries from this bridge port (MAC VLAN). The event is supported for all 
duplicate MAC rejection modes: enable, disable, and alarm only. The event includes the following 
information: 
• 
Existing entry: MAC+VLAN and Bridge port (BP of the existing entry) 
• 
Counter for Duplicate MAC event that includes the number of duplicate MAC occurrences on 
this bridge port since the last event.  
Factory Defaults 
By default, the bridge is not created in ETX-2i. When the bridge is created, its default configuration is 
VLAN-aware, filtering enabled, with no bridge ports or VLANs, and with no duplicate MAC rejection. 
When VLANs are created, the default configuration is E-LAN mode. 
ETX-2i>config# bridge 1 
ETX-2i>config>bridge(1)$ info detail 
    name "BRIDGE 1" 
    vlan-aware 
    filtering 
    aging-time 300 
    no duplicate-mac-rejection 
    echo "Spanning Tree Configuration" 
#   Spanning Tree Configuration 
    spanning-tree 
        mode rstp 
        max-age 20 
        forward-time 15 
        hello-time 2 
        priority 32768 
        tx-hold-count 6 
    exit 
    echo "MLD Snooping" 
 
 
ETX-2i Devices 
5. Traffic Processing 
#   MLD Snooping 
    mld-snooping 
        shutdown 
        host-aging-interval 260 
        router-aging-interval 260 
    exit 
ETX-2i>config>bridge(1)$ vlan 333 
ETX-2i>config>bridge(1)>vlan(333)$ info detail 
    maximum-mac-addresses 0 
    mode e-lan 
The default STP parameters are as follows: 
Parameter 
Default Value 
admin-edge 
Disable 
auto-edge 
Enable 
cost (bridge port) 
0 
forward-time 
15 sec 
hello-time 
2 sec 
max-age 
20 sec 
max-hops 
20 
mcheck 
Disable 
mode 
rstp 
name 
empty string 
priority (bridge port) 
128 
priority (bridge) 
32768 
restricted-role 
Disable 
restricted-tcn 
Disable 
revision 
0 
tx-hold-count 
6 
 
 

## Configuring the Bridge  *(p.873)*

ETX-2i Devices 
5. Traffic Processing 
Configuring the Bridge 
 To configure the bridge, perform the following steps: 
1. Configure the bridge. 
2. Configure the bridge ports. 
3. If working in VLAN-unaware mode: 
 
For E-Tree service, configure bridge mode to E-Tree and configure root. 
4. If working in VLAN-aware mode: 
 
Configure VLANs. For E-Tree service in a VLAN, configure VLAN mode to E-Tree and 
configure root. 
5. Configure flows between non-bridge ports and bridge ports. 
6. Configure RSTP/MSTP (optional). 
7. Configure spanning tree L2CP profile. 
Note 
In Bridge configuration, different bridge ports that egress to the same ETH 
port with different VLAN editing cannot share the same queue block. 
 To configure the bridge: 
1. At the config# prompt, enter:  
bridge 1 
The config> bridge(1)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Defining aging time for MAC 
table entries (seconds) 
aging-time <seconds>  
Possible values: 60–3000 
 
Clearing addresses in MAC 
table 
clear-mac-table 
Clears bridge MAC table 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Enabling duplicate MAC 
rejection 
duplicate-mac-rejection { enable | 
alarm-only } 
[no] duplicate-mac-rejection 
enable – does not learn the 
new (duplicate) MAC entry 
and discards the frame; 
supports duplicate MAC 
event and counters. 
alarm-only – learns the new 
(duplicate) MAC entry; 
supports duplicate MAC 
event and counters. 
Entering no duplicate-mac-
rejection learns the new 
(duplicate) MAC entry; does 
not support duplicate MAC 
event and counters.  
Enabling/disabling filtering 
forwarding mode 
[no] filtering 
To disable filtering 
forwarding mode, type no 
filtering. 
Configuring multicast snooping 
at the bridge level 
mld-snooping 
Refer to MLDv2 Snooping in 
the Management and 
Security chapter. 
Configuring VLAN-unaware 
bridge to E-LAN or E-Tree 
mode 
mode { e-tree | e-lan } 
Changing to E-Tree mode 
requires you to define at 
least one bridge port as root. 
Note: This command is 
available only for 
VLAN-unaware bridge. 
Assigning a name to the bridge  
name <bridge-name> 
bridge-name – 1-32- 
character string 
Configuring bridge ports  
[no] port <port-number> 
port-number – number of 
bridge port 
Possible values:  
1-44 for ETX-2i, ETX-2i-B 
1-80 for ETX-2i-10G, 
ETX-2i-100G 
1-32 for ETX-2i-10G-B/8SFPP 
See Configuring Bridge Ports. 
To delete a bridge port, enter 
no port <port-number>. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Configuring bridge port as root 
port in E-Tree mode 
root <bridge-port> 
Note:  
• This command is available 
only if the bridge is 
VLAN-unaware and the 
mode is E-Tree. 
• Supports more than one 
root; the number of roots 
supported is equivalent to 
the number of bridge 
ports. 
Displaying learned MAC 
addresses (static, dynamic, or 
all) 
show mac-address-table { static | 
dynamic | all } 
See Viewing Learned MAC 
Addresses on Bridge. 
 
Displaying all MAC addresses 
learned on a specific VLAN or 
displaying a specific MAC 
address 
show mac-table [vlan <vlan>] 
[mac-address <mac-address>] 
vlan – VLAN with learned 
MAC addresses 
mac-address – specific MAC 
address to display 
See Viewing Learned MAC 
Addresses on Bridge. 
 
Displaying VLAN information, 
including which bridge ports 
have been automatically 
added as tagged VLAN 
members 
show vlans 
Note: This command is 
available only if the bridge is 
VLAN-aware. 
Configuring STP parameters at 
the bridge level 
spanning-tree  
See Configuring Bridge-Level 
RSTP Parameters. 
Configuring static MAC address 
[no] static-mac <vlan-id> 
<mac-address> <bridge-port> 
Note: Before creating the 
static MAC, you must create 
a flow with the bridge port, 
and VLAN (if applicable). 
Defining VLANs (see below) 
[no] vlan <vlan-id>  
Possible values: 1–4094 
To delete a VLAN, enter 
no vlan <vlan-id> 
Note: This command is 
available only if the bridge is 
VLAN-aware. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Setting mode to VLAN-aware 
or VLAN-unaware 
[no] vlan-aware 
To set mode to 
VLAN-unaware, enter 
no vlan-aware. 
Note: The VLAN aware mode 
cannot be changed if bridge 
port flows exist. 
Configuring Bridge Ports 
The following commands are available in the port level, at the config>bridge(1)>port(<port-number>)# 
prompt. 
Task 
Command 
Comments 
Assigning a name to the bridge port 
name <port-
name> 
To delete the bridge port name, enter no name. 
Administratively enabling the bridge port 
no shutdown 
To administratively disable the bridge port, 
enter shutdown. 
Note: Shutting down the bridge port does not 
stop the traffic. 
Configuring STP parameters at the 
bridge port level 
spanning-tree 
See Configuring Bridge-Port-Level RSTP/MSTP 
Parameters. 
Configuring VLAN 
Note 
• 
You can add a VLAN-ID to a bridge manually (as described in this section); 
otherwise, it is added automatically once relevant flows (accessing bridge 
ports with the same VPN) are defined. VLANs are not automatically 
removed once their defined flows are deleted or shut down. You must 
remove these unused VLANs (without defined flows) manually 
(no vlan <vlan-id>). 
• 
Once the table exceeds the maximum available VPNs, no additional VLANs 
are added to the list. This applies even if the relevant flows of a previous 
VLAN were deleted and replaced by flows bearing a different VLAN. Please 
note that operationally the new VLAN forwards traffic.  
The following commands are available in the vlan level, at the config>bridge(1)>vlan(<vlan-id>)# 
prompt. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Defining maximum MAC 
table size supported by the 
VLAN 
maximum-mac-
addresses <max-mac> 
Possible values: 0–32000 
When using the bridge VLAN MAC table limitation 
(maximum-mac-addresses limit), the first frame of 
each learned MAC address is dropped. 
Configuring VLAN to work 
in E-Tree or E-LAN mode 
mode { e-tree | e-lan } 
If you change to E-Tree, you need to define at least 
one bridge port as root. 
Configuring bridge port as 
root port in E-Tree mode 
root <bridge-port 
number> 
no root < bridge-
port_number> 
Possible values: 1–16. 
no root defines a bridge port as a leaf in E-Tree mode. 
Note:  
• This command is available only if the VLAN mode is 
E-Tree. 
• Supports more than one root per VLAN; the 
number of roots supported is equivalent to the 
number of bridge ports. 
Configuring RSTP/MSTP 
RSTP and MSTP are configured at the bridge and bridge-port levels. 
Configuring BPDU Peers 
When configuring RSTP/MSTP, attach L2CP profile directly to the physical port, with MAC 0x00 and 
action set to peer.  
The following example shows the necessary configuration. 
 To configure an L2CP profile for MAC 0x00 with peer action: 
ETX-2i# configure port 
ETX-2i >config>port# l2cp-profile RSTP  
ETX-2i >config>port>l2cp-profile RSTP# mac 0x00 peer 
exit 
Configuring Bridge-Level RSTP/MSTP Parameters 
 To configure the bridge-level RSTP/MSTP parameters: 
• 
In the config>bridge(bridge_number)# prompt, enter spanning-tree and configure the bridge-
level RSTP/MSTP parameters as illustrated and explained below. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Configuring the amount of time 
that a port remains in the 
listening and learning states 
before entering the forwarding 
state 
forward-time <seconds> sec 
Possible values: 4-30 
Default: 15 seconds 
When configuring the 
forwarding delay, follow this 
rule:  
2 × (forwarding delay - 1) => 
maximum aging time 
Defining how often ETX-2i 
broadcasts hello messages to 
other devices to indicate that the 
bridge is alive 
hello-time <seconds> sec 
Possible values: 1-10 
Default: 2 seconds 
When configuring hello-time, 
follow this rule:  
2 × (hello-time - 1) <= max-age. 
Defining maximum aging time for 
spanning tree operation 
max-age <seconds> sec 
Possible values: 6-40 
Default: 20 seconds 
Defining the number of hops in 
an MST region before the BDPU is 
discarded and the port 
information is aged out 
max-hops <number> 
Possible values: 6-40 
Default: 20 
Selecting spanning tree operation 
mode  
mode { rstp | mstp } 
MSTP-related parameters are 
masked when the bridge 
operates in RSTP mode. 
Configuring bridge-level MST 
instance level 
mst <1–4094> 
no mst 
no mst (msti_number) deletes 
MST instance. 
See configuration instructions 
below. 
Specifying spanning tree priority 
of the bridge 
priority <0, 4096, 8192, 12288, 16384, 
20480, 24576, 28672, 32768, 36864, 
40960, 45056, 49152, 53248, 57344, 
61440> 
This is the value of the first two 
octets of the bridge ID. It is used 
to make the bridge more (or 
less) likely to be chosen as the 
root bridge. 
The lower the number, the 
more likely the bridge will be 
chosen as the root bridge. 
Defining MSTP configuration 
name 
name <string> 
For two or more bridges to be in 
the same MST region, they must 
have the same configuration 
revision number and name. 
Defining MSTP configuration 
revision number 
revision <0–65535> 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Displaying bridge-level spanning 
tree status 
show status 
See Displaying Spanning Tree 
Status below. 
Selecting the maximum number 
of BPDUs that can be transmitted 
to a port in one second 
tx-hold-count <1–10> BPDUs per sec 
Possible values: 1-10 
Default: 6 
 To configure bridge-level MST instance: 
• 
In the config>bridge(bridge_number)>spanning-tree # prompt, enter mst (msti_number) and 
configure the bridge-level MSTI parameters as illustrated and explained below. 
Task 
Command 
Comments 
Specifying MSTI priority 
priority <0, 4096, 8192, 12288, 16384, 
20480, 24576, 28672, 32768, 36864, 
40960, 45056, 49152, 53248, 57344, 
61440> 
 
Mapping VLANs to MST instance 
vlan <1–4094> 
no vlan 
Map list of VLANs to MST 
instance. 
no vlan (vlan_lsit) removes 
VLAN mapping from the MSTI. 
This command can be repeated 
to configure additional VLAN 
mappings. 
For two or more bridges to be in 
the same MST region, they must 
have the same VLAN-to-MSTI 
mapping. 
Displaying bridge-level MSTI 
status 
show status 
See Displaying Spanning Tree 
Status below. 
Configuring Bridge-Port-Level RSTP/MSTP Parameters 
 To configure the bridge-port-level RSTP/MSTP parameters: 
• 
In the config>bridge(bridge_number)>port(port_number)# prompt, enter spanning-tree and 
configure the bridge-port-level RSTP/MSTP parameters as illustrated and explained below. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Defining bridge port as an edge 
port 
admin-edge 
no admin-edge 
no admin-edge disables edge 
port functionality. 
An edge port is put into the 
forwarding state upon linkup, 
for faster convergence. 
An edge port connected to a 
bridge could prevent the 
spanning tree from detecting 
and disabling loops. 
Enabling/disabling automatic 
identification of edge ports  
auto-edge 
no auto-edge 
no auto-edge disables 
automatic edge port 
identification. 
The edge status of an auto edge 
port is automatically disabled 
upon receiving a BPDU 
(regardless of the configured 
admin-edge value). 
Defining port path cost 
cost <0–200000000> 
If a loop occurs, the path cost is 
used to select an interface to 
place into the forwarding state. 
A lower path cost represents 
higher speed links. It is 
recommended to use the 
default cost value (0) to let ETX-
2i to compute the best possible 
cost according to the link 
bandwidth. 
Activating migration check by the 
port 
mcheck 
If a port connects to a bridge 
running STP, this port 
automatically migrates to the 
STP-compatible mode and does 
not revert automatically back to 
MSTP/RSTP mode. 
mcheck forces protocol 
renegotiation with neighboring 
devices, to check if they are 
MSTP/RSTP-compatible. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Configuring bridge-port-level 
MSTI 
mst <1–4094> 
no mst 
no mst (msti_number) deletes 
MST instance. 
See configuration instructions 
below. 
Defining bridge port priority 
port-priority <0, 16, 32, 48, 64, 80, 96, 
112, 128, 144, 160, 176, 192, 208, 224, 
240> 
This is the value of the first 
octet of the bridge port ID. If a 
loop occurs, MSTP/RSTP uses 
the port priority, when selecting 
an interface to put into the 
forwarding state.  
The lower the number, the 
higher the port priority (the 
lowest numbered port is 
selected if a tie breaker is 
needed). 
Preventing/allowing bridge port 
to become a root port 
restricted-role 
no restricted-role 
no restricted-role removes 
bridge port restriction. 
Restricted port cannot become 
a root port, even it is the most 
likely candidate. 
Enabling/disabling propagation of 
topology changes by the port 
restricted-tcn 
no restricted-tcn 
no restricted-tcn enables 
propagation of topology 
changes by the port. 
A restricted-tcn port does not 
propagate received topology 
change notifications and 
topology changes to other 
ports. 
Restricting propagation of 
topology changes can be used 
to prevent bridges external to a 
network core influencing the 
active spanning tree topology. 
Usually, it is applied to bridges 
which are not under the full 
control of the network 
administrator. 
Displaying bridge port spanning 
tree status 
show status 
See Viewing Spanning Tree 
Status below. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Activating spanning tree on the 
bridge port 
shutdown 
no shutdown 
shutdown disables spanning 
tree on bridge port. 
Bandwidth Values for Bridge Port Path Cost 
Link Bandwidth 
Cost 
<= 100 kbps 
200 000 000 
1 Mbps 
20 000 000 
10 Mbps 
2 000 000 
100 Mbps 
200 000 
1 Gbps 
20 000 
10 Gbps 
2 000 
100 Gbps 
200 
1 Tbps 
20 
10 Tbps 
2 
 To configure bridge-port-level MST instance: 
• 
In the config>bridge(bridge_number)>port(port_number)>spanning-tree # prompt, enter mst 
(msti_number) and configure the bridge-level MSTI parameters as illustrated and explained 
below. 
Task 
Command 
Comments 
Defining MSTI port path cost 
cost <0–200000000> 
 
Specifying MSTI port priority 
port-priority <0, 16, 32, 48, 64, 80, 
96, 112, 128, 144, 160, 176, 192, 
208, 224, 240> 
 
Displaying bridge-port-level 
MSTI status 
show status 
See Viewing Spanning Tree 
Status below. 

## Examples  *(p.883)*

ETX-2i Devices 
5. Traffic Processing 
Examples 
VLAN-Aware Bridge 
This section illustrates the following configuration: 
• 
VLAN-aware bridge, with bridge ports 1–4 
• 
VLAN 51 used for management, in E-LAN mode 
• 
VLAN 100 used for traffic, in E-Tree mode, with root bridge port 2 
• 
VLAN 200 used for traffic, in E-LAN mode 
• 
Management flows (unidirectional) between SVI 1 and bridge port 1 
• 
Traffic flows (bidirectional) between: 
 
Ethernet port 1/1 and bridge port 2, with classification VLAN 100 and VLAN 200 
 
Ethernet port 0/3 and bridge port 3, with classification VLAN 100 
 
Ethernet port 0/4 and bridge port 4, with classification VLAN 100 
#*******Configure SVI 
configure port svi 1 
  no shutdown 
  exit all 
 
#*******Configure bridge  
configure bridge 1 
  vlan-aware 
 
#*******Configure bridge ports 
  port 1 
     no shutdown 
    exit 
  port 2 
    no shutdown 
    exit 
  port 3 
    no shutdown 
    exit 
  port 4 
    no shutdown 
    exit 
 
#*******Configure VLANs 
  vlan 51 
    exit 
 
 
ETX-2i Devices 
5. Traffic Processing 
  vlan 100 
    mode e-tree 
    root 2 
    exit 
  vlan 200 
    exit all 
 
#*******Configure classifier profiles 
configure flows 
  classifier-profile 51 match-any 
    match vlan 51 
    exit 
  classifier-profile 100 match-any 
    match vlan 100 
    exit 
  classifier-profile 200 match-any 
    match vlan 200 
    exit 
  classifier-profile unt match-any 
    match untagged 
    exit 
 
#*******Configure management flows 
  flow mng_in 
    classifier 51 
    ingress-port bridge-port 1 1 
    egress-port svi 1 queue 0 
    no policer 
    no shutdown 
    exit 
 
  flow mng_out 
  classifier unt 
  ingress-port svi 1 
  egress-port bridge-port 1 1 
  vlan-tag push vlan 51 p-bit fixed 0 
  no shutdown 
  exit 
 
#*******Configure management flow to physical port 
  flow 1toBP2_51 
  classifier 51 
  ingress-port ethernet 1/1 
  egress-port bridge-port 1 2 
  reverse-direction block 0/1 
  no shutdown 
  exit 
 
 
 
ETX-2i Devices 
5. Traffic Processing 
#*******Configure bidirectional traffic flows 
flow 1toBP2_100 
  classifier 100 
  ingress-port ethernet 1/1 
  egress-port bridge-port 1 2 
  reverse-direction block 0/1 
  no shutdown 
  exit 
 
flow 1toBP2_200 
  classifier 200 
  ingress-port ethernet 1/1 
  egress-port bridge-port 1 2 
  reverse-direction block 0/1 
  no shutdown 
  exit 
 
flow 3toBP3_100 
  classifier 100 
  ingress-port ethernet 0/3 
  egress-port bridge-port 1 3 
  reverse-direction block 0/1 
  no shutdown 
  exit  
 
flow 4toBP4_100 
  classifier 100 
  ingress-port ethernet 0/4 
  egress-port bridge-port 1 4 
  reverse-direction block 0/1 
  no shutdown 
  exit all 
 
#*******Configure router interface 
configure router 1 
  interface 1 
    address 10.10.10.20/24 
    bind svi 1 
    dhcp-client 
      client-id mac 
      exit 
   no shutdown 
   exit all 
save 
 
Displaying VLAN Information 
This section illustrates displaying VLAN information after performing the configuration specified in 
VLAN-Aware Bridge. The VLAN information shows the following: 
VLAN 51 
Bridge ports 1 to 2 were automatically added as tagged ports. 
VLAN 100 
Bridge ports 2 to 4 were automatically added as tagged ports. 
VLAN 200 
Bridge port 2 was automatically added as a tagged port. 
 
ETX-2i# configure bridge 1 
ETX-2i>config>bridge(1)# show vlans 
 
VLAN ID : 51 
 
Tagged Ports   : 1..2 
Untagged Ports : 0 
 
 
VLAN ID : 100 
 
Tagged Ports   : 2..4 
Untagged Ports : 0 
 
 
VLAN ID : 200 
 
Tagged Ports   : 2 
Untagged Ports : 0 
VLAN-Unaware Bridge 
This section illustrates the following configuration: 
• 
VLAN-unaware bridge, with bridge ports 1–4 
• 
Traffic flows (unidirectional), with classification to match all, between: 
 
Ethernet port 0/1 and bridge port 2 
 
Ethernet port 0/3 and bridge port 3 
 
Ethernet port 0/4 and bridge port 4 
#*******Configure bridge  
configure bridge 1 
  no vlan-aware 
 
 
 
ETX-2i Devices 
5. Traffic Processing 
#*******Configure bridge ports 
  port 1 
     no shutdown 
    exit 
  port 2 
    no shutdown 
    exit 
  port 3 
    no shutdown 
    exit 
  port 4 
    no shutdown 
    exit all 
 
#*******Configure classifier profile 
configure flows 
  classifier-profile all match-any 
    match all 
    exit 
 
#*******Configure unidirectional traffic flows 
  flow 1toBP2 
    class all 
    ingress-port ethernet 0/1 
    egress-port bridge-port 1 2 
    no shutdown 
    exit 
 
  flow BP2to1 
    class all 
    ingress-port bridge-port 1 2  
    egress-port ethernet 0/1 block 0/1 
    no policer 
    no shutdown 
    exit 
 
  flow 3toBP3 
    class all 
    ingress-port ethernet 0/3 
    egress-port bridge-port 1 3 
    no shutdown 
    exit 
 
  flow BP3to3 
    class all 
    ingress-port bridge-port 1 3  
    egress-port ethernet 0/3 block 0/1 
    no policer 
    no shutdown 
    exit 
 
 
 

## Viewing Learned MAC Addresses on Bridge  *(p.888)*

ETX-2i Devices 
5. Traffic Processing 
  flow 4toBP4 
    class all 
    ingress-port ethernet 0/4 
    egress-port bridge-port 1 4 
    no shutdown 
    exit 
 
  flow BP4to4 
    class all 
    ingress-port bridge-port 1 4  
    egress-port ethernet 0/4 block 0/1 
    no policer 
    no shutdown 
    exit 
Creating Static MAC Address 
This section illustrates creating a static MAC address after performing the configuration specified in 
VLAN-Aware Bridge.  
exit all 
configure bridge 1 
static-mac 100 01-02-03-04-05-06 2 
exit all 
Viewing Learned MAC Addresses on Bridge 
ETX-2i provides two commands for displaying learned MAC addresses at the bridge level: 
• 
show mac-address-table {static | dynamic | all} – command used to search for and count static, 
dynamic, or all learned addresses. The output displays the total number of static, dynamic, 
and/or all learned MAC addresses, the number of duplicate MAC address packets, and a table 
showing the bridge port and VLAN associated with each MAC address. 
• 
show mac-table [vlan <vlan>] [mac-address <mac-address>] – command used to do either of 
the following: 
 
Search for all MAC addresses learned on all VLANs or on a specific VLAN 
 
Search for a specific MAC address.  
The output displays the learned MAC addresses in ascending order of VLAN, as well as each MAC 
address’s associated bridge port and status (Static or Dynamic). (When searching for a specific 
MAC address, there is only one entry.) 
ETX-2i Devices 
5. Traffic Processing 
Note 
The output of the show mac-address-table and show mac-table commands, 
in ETX-2i-10G full and half devices, displays the following MAC addresses 
relevant for internal use only, and not for users: 
• 
Static MAC addresses 33-33-00-00-00-xx – related to ETX support of IP 
dual stack (IPv4 and IPv6).  
• 
Entries with bridge port 0 – related to ETX hardware (FPGA) and software 
communication. 
 To display the number of learned MAC addresses, as well as their information: 
• 
At the config>bridge(bridge_number)# prompt, enter show mac-address-table {static | 
dynamic | all}. 
The MAC address table is displayed. 
 
Note 
ETX-2i displays only the first 1000 entries. To view the entire MAC table, 
download it to your PC, using SFTP. Refer to File Operations in the 
Administration chapter. 
 
ETX-2i# configure bridge 1 
ETX-2i>config>bridge(1)# show mac-address-table all 
Total MAC Addresses          : 22 
Static MAC Addresses         : 12 
Dynamic MAC Addresses        : 10 
Duplicate MAC Address packets: 26 
 
 
VLAN  MAC Address       Port Status 
--------------------------------------------------------------- 
20    00-00-00-00-00-01 2    Static 
40    00-00-00-00-00-01 2    Static 
50    00-00-00-00-00-01 2    Static 
60    00-00-00-00-00-01 2    Static 
60    00-00-00-00-00-E1 7    Dynamic 
100   00-00-00-00-00-E1 7    Dynamic 
100   01-02-03-04-05-06 2    Static 
130   00-00-00-00-00-E1 7    Dynamic 
150   00-00-00-00-00-E1 7    Dynamic 
160   00-00-00-00-00-E1 7    Dynamic 
170   00-00-00-00-00-01 2    Static 
180   00-00-00-00-00-01 2    Static 
190   00-00-00-00-00-01 2    Static 
200   00-00-00-00-00-01 2    Static 
200   00-00-00-00-00-E1 7    Dynamic 
230   00-00-00-00-00-E1 7    Dynamic 
250   00-00-00-00-00-E1 7    Dynamic 

## Viewing Spanning Tree Status  *(p.890)*

ETX-2i Devices 
5. Traffic Processing 
260   00-00-00-00-00-E1 7    Dynamic 
270   00-00-00-00-00-01 2    Static 
280   00-00-00-00-00-01 2    Static 
290   00-00-00-00-00-01 2    Static 
290   00-00-00-00-00-E1 7    Dynamic   
 
 To display all learned MAC addresses on VLAN 100: 
ETX-2i>config>bridge(1)# show mac-table vlan 100 
 
VLAN  MAC Address       Port Status 
--------------------------------------------------------------- 
100   00-20-D2-51-0C-50 2    Dynamic 
100   00-20-D2-51-17-4B 4    Static 
100   00-20-D2-51-41-D2 2    Dynamic 
100   00-20-D2-52-98-71 2    Dynamic 
100   00-20-D2-53-A7-4B 2    Dynamic 
100   00-20-D2-53-DF-CB 2    Dynamic 
100   00-20-D2-54-4D-5C 1    Dynamic 
100   00-20-D2-54-53-13 2    Dynamic 
100   00-20-D2-57-E7-E8 2    Dynamic 
100   00-20-D2-58-58-BB 2    Dynamic 
100   00-20-D2-58-94-86 2    Dynamic 
100   00-20-D2-5B-0D-7F 2    Dynamic 
100   00-20-D2-5B-5D-5F 2    Dynamic 
100   00-20-D2-E1-69-45 2    Dynamic 
100   28-C7-CE-F4-68-C7 2    Dynamic 
100   A0-48-1C-7D-80-F5 2    Dynamic 
100   BC-30-5B-A5-B1-9A 2    Dynamic 
100   BC-30-5B-CC-64-72 2    Dynamic 
100   C4-0A-CB-38-66-1C 2    Dynamic 
 To display information on MAC address C4-0A-CB-38-66-1C 2: 
ETX-2i>config>bridge(1)# show mac-table mac-address C4-0A-CB-38-66-1C 
 
VLAN  MAC Address       Port Status 
--------------------------------------------------------------- 
100   C4-0A-CB-38-66-1C 2    Dynamic 
Viewing Spanning Tree Status 
You can display spanning tree status at the following levels: 
• 
Bridge 
• 
Bridge MSTI 
ETX-2i Devices 
5. Traffic Processing 
• 
Bridge port 
• 
Bridge port MSTI 
 To display spanning tree status: 
• 
At the relevant prompt (bridge, bridge MSTI, bridge port, bridge port MSTI), type show status. 
The relevant status screen is displayed. 
Spanning Tree Status – Bridge Level 
Mode MSTP, Root, Regional Root 
Bridge: Priority 32768, Address 00:11:22:33:44:55 
Root: Priority 32768, Address 00:11:22:33:44:55,  
    Cost 012, Port 1 (Eth 1/2) 
Regional Root: Priority 32768, Address 00:11:22:33:44:55, cost 012 
Configured Times:  
    Max Age 01, Hello 01, Forward Delay 01 
Actual Times: 
    Max Age 01, Hello 01, Forward Delay 01, Hold 01 
Topology Change Total 012, Since Last 2 days 00:11:22 
Spanning Tree Status – Bridge MSTI Level 
MST Instance 1, Root 
VLANs Mapped 1-10, 20 
Bridge: Priority 32768, Address 00:11:22:33:44:55, Root 
Root: Priority 32768, Address 00:11:22:33:44:55 
    Cost 32768, Port 1 (Eth1/1) 
Topology Change: Total 1234, Since Last 2 days 22:11:00  
 
BP Interface Role       State       
-- --------- ---------- ----------  
01 Eth1/1    Backup     Blocking    
02 Eth1/2    Designated Forwarding 
Spanning Tree Status – Bridge Port Level 
Port 1 (Eth1/1), Root, Forwarding, Edge (default) 
    Path Cost 200000000, Priority 128, Up 2 days 00:11:22 
Designated Root: Priority 32768, Address 00:11:22:33:44:55 
Designated Bridge: Priority 32768, Address 00:11:22:33:44:55 
    Port 1, Port Priority 128, Cost 200000000 
Regional Root: Priority 32768, Address 00:11:22:33:44:55, Cost 200000000 
Hello Timer 10 
Forward Transitions: 11 