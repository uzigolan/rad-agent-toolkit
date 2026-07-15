# 8 Traffic Processing

*Manual `MiNID_ver_2_6_mn.pdf`, pages 142–216.*


## 8.1 Flows  *(p.142)*

8.1 Flows 
Traffic is classified into flows, which are unidirectional entities that have an action on traffic. MiNID 
supports the following port-level classification mechanisms: 
• 
Port Classification (see Port Mode) 
• 
Flow Classification (see Flow Classification) 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
IEEE 802.1q  
IEEE 802.1ad  
RFC 862 – Echo Protocol  
Benefits 
Flows enable traffic differentiation for different customers and for different traffic types, thus creating 
separate Ethernet services. For example, a VLAN can be added to MSA-to-SFP/ Port 2-to-Port 1 traffic 
and removed from SFP-to-MSA/ Port 1-to-Port 2 traffic to function as an S-tag to create an EVC. VLAN 
p-bits can be applied according to C-tag p-bits or according to DSCP to maintain a desired SLA. 
Port mode is appropriate when other services are handled on other ports, for clearer service separation 
and simpler SLA measurement. On the other hand, flow-based mode enables handling different service 
8. Traffic Processing 
types on device, providing a cheaper, more scalable solution. Per-flow statistics enable per-service SLA 
measurements. 
The layer-3/4 loopback feature allows you to define loopback tests according to IP/UDP parameters, 
enabling MiNID to support diagnostics tests for Layer-3 networks. 
Functional Description 
MiNID can work in port or flow-based mode. 
Port Mode 
In port mode (all-in-one bundling), MiNID processes customer and network traffic data frames 
consistently for all traffic coming into each of its two ports (SFP/Port 1 and MSA/Port 2); see Physical 
Ethernet Ports). 
When switching from flow-based mode to port mode, configured flows are disabled but retained. From 
port mode you can only change to the last configured flow classification mode, upon which the 
configured flows are again available. 
Flow Classification 
In flow-based mode, MiNID classifies frames by any of the following: 
• 
Customer VLAN ID range and P-bit range 
Note 
• 
VLAN ID ranges of different flows may not overlap. 
• 
Double VLAN classification is supported. 
• 
One flow can be marked as Untagged. 
• 
DSCP 
• 
MAC addresses: 
 
MAC source address 
 
MAC destination address 
• 
Ethertype 
In flow-based mode, up to 64 flows can be configured (not including management traffic; includes 
disabled flows. Each flow applies to only one direction (SFP/Port 1 to MSA/Port 2 or MSA/Port 2 to 
SFP/Port 1); up to 32 flows per direction can be configured). All configured flows classify traffic 
according to the same criterion type. 
8. Traffic Processing 
Changing from one flow classification mode to another deletes all configured flows. 
Flow Actions 
For each configured flow, and for the unclassified (non-matched) incoming traffic of each port, any of 
the following actions can be defined: 
Drop 
Drop the frame 
Pass 
Through 
Pass the traffic through the device without changes 
VLAN 
Push (add) for single and double VLANs, pop (remove) for single and double VLANs, or replace a 
VLAN tag, as specified. 
Pushing adds a VLAN tag before the existing tag, if there is one. Popping removes the first tag, if 
there is at least one. Replacing overwrites the first tag, if there is at least one. 
When pushing or replacing a VLAN tag, the new tag’s P-bit can be configured to be set in any of 
the following ways, per flow: 
• Fixed Value for the flow 
• C-Tag Copy: The new tag’s P-bit is copied from the originating frame’s P-bit 
• DSCP Marking: The new tag’s P-bit is set according to a separately configured mapping of 
originating frames’ DSCP values to P-bit values. All flows configured for DSCP-to-P-bit mapping 
use the same mapping. 
• C-Tag Marking: The new tag’s P-bit is set according to a separately configured mapping of 
originating frames’ P-bit values to new P-bit values. All flows configured for P-bit-to-P-bit 
mapping (not copying) use the same mapping. 
Loopback 
The traffic is echoed back through the same port, with or without swapping the source and 
destination addresses (MAC, and where relevant also IP), as specified. The looped traffic is passed 
through to the other port (intrusive loopback). 
 
Note 
If the configured flow action is not supported by the arriving frame (e.g. 
non-IP frame for DSCP remarking or untagged frame for C-tag remarking), the 
new tag’s P-bit is set to 0. 
The Drop Eligible bit can be set to fixed value (Yes / No) or defined 
automatically by Policer if it is enabled. 
8. Traffic Processing 
L2CP/L2PT 
MiNID can discard, pass through, tunnel, or peer packets that are classified per flow or per port as 
corresponding to a particular L2CP/L2PT protocol.  
L2PT protocol classification is based on the packet destination MAC address, Ethertype, and Subtype as 
specified in the following table.  
L2PT Protocol Classification 
Protocol 
MAC Address 
Ethertype 
Subtype 
STP 
01-80-C2-00-00-00 
All 
0x42 
OAM 
01-80-C2-00-00-02 
0x8809 
0x03 
PAgP 
01-00-0C-CC-CC-CC 
0x0104 
0xAA 
LLDP 
01-80-C2-00-00-0E 
0x88CC 
All 
CDP 
01-00-0C-CC-CC-CC 
0x2000 
0xAA 
VTP 
01-00-0C-CC-CC-CC 
0x2003 
0xAA 
UDLD 
01-00-0C-CC-CC-CC 
0x0111 
0xAA 
DTP 
01-00-0C-CC-CC-CC 
0x2004 
0xAA 
PVSTP 
01-00-0C-CC-CC-CD 
0x010B 
All 
LACP 
01-80-C2-00-00-02 
0x8809 
0x01 
LAMP 
01-80-C2-00-00-02 
0x8809 
0x02 
ESMC 
01-80-C2-00-00-02 
0x8809 
0x0A 
PTP-Peer-Delay 
01-80-C2-00-00-0E 
0x88F7 
All 
L2CP protocol classification is user-configurable and based on the destination MAC address 
01-80-C2-00-00-XX, where XX is 00–2F (excluding values used in the table above).  
For each L2PT protocol, you can define changing the destination MAC address to a user-configured 
value. 
If you configure a new L2CP protocol classification, or a change to an L2PT MAC address, that counts as 
an L2CP/L2PT entry. MiNID supports up to 31 L2CP/L2PT entries; 13 entries are already occupied by the 
predefined L2PT classifications, therefore you can configure up to 18 additional entries. 
The L2CP/L2PT handling is done by creating L2CP profiles and associating them with a port or a flow. In 
an L2CP profile, you can configure an action for each protocol: 
8. Traffic Processing 
• 
Discard – Packet is dropped 
• 
Pass through – Packet is transmitted unchanged to the egress port; MAC address is not changed 
• 
Peer – Packet is delivered to host treatment (OAM protocol only) 
• 
Tunnel – Packet is classified to a flow and handled accordingly; MAC address is changed if a new 
MAC address has been defined 
Note 
The action for OAM protocol must be set to peer in order for link OAM to 
function. However, when packets such as ESSM packets are received with 
MAC address corresponding to OAM protocol (01-80-C2-00-00-02), and OAM 
action is set to peer, they are discarded. If the OAM action is set to pass 
through, then the ESSM packets are not discarded, but link OAM does not 
function. 
When you add an L2CP/L2PT entry by configuring an L2CP protocol classification or an L2PT MAC 
address change, the entry is added to any existing L2CP/L2PT profile, with the action set to tunnel. 
Note 
• 
You can create up to eight L2CP profiles. 
• 
An L2CP profile can be associated with a flow only if the flow classification 
mode is VID+Pbits Range. 
Loopbacks 
MiNID provides the following types of loopbacks: 
• 
Layer-2 loopbacks (see Layer-2 Loopbacks) 
• 
Layer-3/4 loopbacks (see Layer-3/4 Loopbacks) 
Layer-2 Loopbacks 
To enable testing flow connectivity without interrupting traffic, you can configure MiNID with dedicated 
source and/or destination MAC addresses, representing testing devices whose frames should be looped 
back. 
Up to four source MAC addresses and up to four destination MAC addresses for MiNID as a whole can 
be configured for layer-2 loopback (referred to in the Web and CLI as in-service loopback). Frames with 
these MAC addresses can be looped back, according to service flow configuration. Flow configuration 
defines the following: 
• 
The mode for matching flow-matching traffic to MAC addresses. One of: 
 
SA: According to only source MAC address 
 
DA: According to only destination MAC address 
8. Traffic Processing 
 
SA+DA: Only when matching both source and destination MAC addresses 
• 
Which of the four (or eight, in SA+DA mode) MAC addresses are enabled and which disabled for 
layer-2 loopback. Traffic is looped if it matches a flow for which its MAC address is enabled for 
layer-2 loopback. 
Each flow’s layer-2 loopback (for all the flow’s enabled MAC addresses) can be configured to include 
source and destination swap. Source and destination swap is of MAC addresses, and, when the frame 
includes an IP header, of IP addresses. 
Layer-3/4 Loopbacks 
To enable testing flow connectivity without interrupting traffic, you can configure MiNID with a 
dedicated IP address and UDP port, representing testing devices whose frames should be looped back. 
You can configure a dedicated IP address (and UDP port if applicable) for each layer-3/4 loopback mode, 
to be used as criteria whether to perform layer-3/4 loopbacks, and configure the layer-3/4 loopback 
mode per flow or per port (if port mode is enabled). The loopback modes are as follows: 
• 
IP loop – Loopback packets whose destination IP address matches the dedicated IP address, with 
MAC + IP swap 
• 
UDP loop – Loopback packets whose destination IP address matches the dedicated IP address, 
and UDP destination port matches the dedicated UDP port, with MAC + IP + UDP swap 
• 
UDP echo – Perform UDP echo for packets whose destination IP address matches the dedicated 
IP address, and UDP destination port matches the dedicated UDP port.  
The UDP echo is a mechanism where the source sends packets, and the responder sends the 
packets back to the source. If you want to work according to RFC 862 standard, configure the 
dedicated UDP port to 7.   
IP Agnostic Loops 
IP agnostic loops enable you to run UDP loop\UDP Echo or TWAMP tests without configuring the 
IP address. Only the UDP port is configured; the test runs for any IP address. 
TWAMP Light Responders 
Flows can be bound to TWAMP (Two-Way Active Measurement Protocol) responders, to be 
used to reflect TWAMP test packets (see OAM (TWAMP)). Flows are bound to TWAMP 
responders by specifying the flow layer-3/4 loopback type as TWAMP responder, and then 
selecting the TWAMP responder.  
Note 
Each flow can be bound to a single TWAMP responder. 
8. Traffic Processing 
Factory Defaults 
By default, no flows are configured. 
General Flow Parameters 
The following general (not per flow) classification and flow parameters can be configured in: 
• 
The CLI config>flows context 
• 
The Web interface, in and below Configuration > Physical Port > Flows Classification port name. 
Flow General Parameter Defaults 
Parameter 
Description 
Default Value 
classification mode per port 
How incoming frames should be classified: 
uniformly (port mode) or by a specified criterion 
vlan-pbits-range 
dscp-marking 
Mapping of DSCP values to P-bit values, for 
enabled flows configured to push or replace VLAN 
tags with P-bits using this mapping 
Each eight DSCP values (0-7, 
8–15, …, 56–63) are mapped 
sequentially to the eight P-bit 
values (0–7) 
fallback-action 
Action for frames from a specified ingress port that 
don’t match any enabled flows, if the classification 
mode is not port mode 
pass-through (for both ports) 
fallback-l2cp 
Set L2CP profile for the unclassified flow of the 
relevant port (for flow mode)  
no fallback-l2cp  
fallback-pm-collection 
Set PM collection for the unclassified flow of the 
relevant port (for flow mode) 
no fallback-pm-collection 
fallback-policer 
Set Policer profile for the unclassified flow of the 
relevant port (for flow mode) 
 
in-service-mac 
MAC addresses (four source and four destination) 
to be made available to per flow loopback 
in-service-mac src-addr <n> 
and 
in-service-mac dst-addr <n>, 
where n=1–4, all set to 
00-00-00-00-00-00 
inner-vlan-marking 
Mapping of originating frame P-bit values to new 
tag P-bit values, for flows configured to push or 
replace VLAN tags with P-bits using this mapping 
Each P-bit value is mapped to 
the same value 
l2cp-mac 
L2CP protocol classification 
None 
8. Traffic Processing 
Parameter 
Description 
Default Value 
l2cp-protocol  
L2PT protocol MAC address changes 
None (see L2PT Protocol 
Classification table for a list of 
the supported L2PT protocols) 
l2cp-profile 
Configuring L2CP/L2PT profile  
None 
port-l2cp 
Defining L2CP/L2PT profile to use if classification 
mode is port mode  
None 
port-mode-action 
Action for frames from a specified ingress port if 
the classification mode is port mode 
pass-through (for both ports) 
tpid-outer-vlan 
TPID value used in flow packets and as the outer 
TPID of double-tagged OAM packets 
0x88a8 (for both ports) 
tpid-inner-vlan 
TPID value for enabled flows configured to push or 
replace VLAN tags, for a specified traffic direction 
0x8100 (for both ports) 
Per-Flow Parameters 
The following per-flow parameters can be configured in: 
• 
The CLI config>flows>flow(<flow-name>) context 
• 
The Web interface, in: 
 
For new flows: Configuration > Physical Port > Flows > Flows Classification Port name>Add 
flow. 
 
For existing flows: Configuration > Physical Port > Flows Classification port name> Config 
Flow > flow name 
 
For flow layer-2 loopback parameters: Configuration > Physical Port > Flows > General 
Params > In-Serv Loops 
Per-Flow Parameter Defaults 
Parameter 
Description 
Default Value 
classifier match 
Frame values considered a 
match for this flow 
Default values by Classification Mode are: 
 
 
Classification Mode 
Classifier Default 
 
 
DSCP 
dscp 0 
 
 
Ethertype 
ether-type 0x0000 
8. Traffic Processing 
Parameter 
Description 
Default Value 
 
 
Source MAC address 
src-mac 00-00-00-00-00-00 
 
 
Destination MAC 
address 
dst-mac 00-00-00-00-00-00 
 
 
VID range and P-bit 
range 
vlan-min 0 pbit-min 0 
vlan-max 0 pbit-max 0 
flow-action 
The ingress port of frames to 
which this flow applies, and 
the flow action 
ingress-port sfp/1 action drop 
in-service-l3-l4-loops 
Layer-3/4 loop mode 
Disabled 
l2cp 
L2CP profile assigned to flow 
None 
service-name 
Service name assigned to flow 
None 
shutdown 
Whether the flow is enabled 
(no shutdown) or disabled 
(shutdown) 
shutdown 
Configured in in-service-loops context: 
in-serv-action 
Layer-2 loopback with or 
without source-destination 
address swap 
loop-mac-ip-swap 
in-serv-mode 
Mode for matching 
flow-matching traffic to MAC 
addresses (see Layer-2 
Loopbacks) 
src-dst 
in-serv-dst-mac 1 to 
in-serv-dst-mac 4 
Indicates whether this MAC 
destination address is enabled 
for layer-2 loopback for this 
flow 
disable 
in-serv-src-mac 1 to 
in-serv-src -mac 4 
Indicates whether this MAC 
source address is enabled for 
layer-2 loopback for this flow 
disable 
8. Traffic Processing 
Flow Configuration Tasks 
General Tasks 
The following tasks can be performed in the CLI config>flows context (unless otherwise specified), or in 
the Web interface. 
General Configuration Tasks 
Task 
CLI Command 
Web Interface Location 
Comments 
Define how incoming 
frames should be 
classified: uniformly 
(port mode) or by a 
specified criterion 
classification mode <mode> 
Configuration > Physical Port 
> Flows  > Classification 
Mode 
<mode> is one of the 
following: 
• port 
• dscp 
• ethertype 
• src-mac (source MAC 
address) 
• dst-mac (destination MAC 
address) 
• vlan-pbits-range (VLAN ID 
range and P-bit range) 
Map a DSCP value to a P-
bit value, for enabled 
flows configured to push 
or replace VLAN tags 
with P-bits using DSCP 
marking 
dscp-marking dscp <DSCP 
value> s-pbit <new P-bit> 
Configuration > Physical Port 
> Flows > General Params > 
DSCP->S-Tag Mapping 
 
Configure action for 
frames from a specified 
ingress port that don’t 
match any enabled 
flows, if not in port 
mode 
fallback-action ingress-port 
<sfp/1 | msa/2> action 
<action> [<VLAN 
parameters>] 
Configuration > Physical Port 
> Flows > General Params > 
General Params [SFP/Port 1 | 
MSA/ Port 2]> Unclassified 
Action 
<sfp/1 | msa/2>defines the 
traffic direction that this flow 
applies to, by defining the 
ingress port as either 
SFP/port 1 or MSA/ port 2. 
For details of the <action> 
<VLAN parameters> 
parameters, see Action 
Parameters table 
8. Traffic Processing 
Task 
CLI Command 
Web Interface Location 
Comments 
Bind the unclassified 
flow to the specified 
L2CP profile 
fallback-l2cp profile <profile-
name> ingress-port <sfp/1 | 
msa/2> 
Configuration > Physical Port 
> Flows > General Params > 
General Params [SFP/Port 1 | 
MSA/ Port 2]> Fallback L2CP 
Profile 
 
Enable PM collection 
and set the PM interval 
for the unclassified flow 
fallback-pm-collection 
interval <interval-time> 
Configuration > Physical Port 
> Flows > General Params > 
General Params [SFP/Port 1 | 
MSA/ Port 2]> Fallback PM 
Collection 
 
Enable policer profile 
and bind it to the 
unclassified flow  
fallback-policer ingress-port 
{1|2} policer {profile|regular-
accounting-only} <policer-
profile-name> 
Configuration > Physical Port 
> Flows > General Params > 
General Params [SFP/Port 1 | 
MSA/ Port 2]> Fallback 
Policer Type 
 
Configure MAC 
destination or source 
address to be available 
for layer-2 loopback 
in-service-mac dst-addr 
<index> <address> 
or 
in-service-mac src-addr 
<index> <address> 
Configuration > Physical Port 
> Flows > General Params > 
In-Service Loop MACs 
 
Specify the IP address to 
match to packet 
destination IP addresses 
for IP loop layer-3/4 
loopback 
ip-loop ip-address <ip-dest-
addr> 
Configuration > Physical Port 
> Flows > General Params > 
In-Service L3\L4> IP Loop 
Note: This must be a different 
IP address than the MiNID 
host IP address, or any IP 
address specified for a 
different loopback type or 
TWAMP responder. 
Specify the IP address to 
match to packet 
destination IP addresses 
for UDP loop layer-3/4 
loopback  
udp-loop ip-address 
<ip-dest-addr> 
Configuration > Physical Port 
> Flows > General Params > 
In-Service L3\L4> UDP Loop 
Note: The combination of the 
IP address and UDP port 
specified for UDP loop must 
be different than specified for 
UDP echo 
Specify the UDP port to 
match to packet 
destination IP addresses 
for UDP loop layer-3/4 
loopback  
udp-loop udp-port 
<udp-dest-port> 
Configuration > Physical Port 
> Flows > General Params > 
In-Service L3\L4> UDP Loop 
UDP port range 1–65535 
See above note 
8. Traffic Processing 
Task 
CLI Command 
Web Interface Location 
Comments 
Specify the IP address to 
match to packet 
destination IP addresses 
for UDP echo layer-3/4 
loopback  
udp-echo ip-address 
<ip-dest-addr> 
Configuration > Physical Port 
> Flows > General Params > 
In Service L3\L4> UDP Echo 
Note: The combination of the 
IP address and UDP port 
specified for UDP echo must 
be different than specified for 
UDP loop 
Specify the UDP port to 
match to packet 
destination IP addresses 
for UDP echo layer-3/4 
loopback  
udp-echo udp-port 
<udp-dest-port> 
Configuration > Physical Port 
> Flows > General Params > 
In Service L3\L4> UDP Echo 
UDP port range 1–65535 
See above note 
Configure port mode 
action for frames from a 
specified ingress port 
port-mode-action 
ingress-port <sfp/1 | msa/2> 
action <action> [<VLAN 
parameters>] 
Configuration > Physical Port 
> Flows > General Params > 
General Params [SFP/ Port 1 
| MSA/ Port 2] > Port Mode 
Action 
See Configuring Port Mode. 
<sfp/1 | msa/2> defines the 
traffic direction that this 
action applies to, by defining 
the ingress port as either 
SFP/port 1 or MSA/ port 2. 
For details of the <action> 
<VLAN parameters> 
parameters, see Action 
Parameters table 
Define L2CP/L2PT profile 
to use for frames from 
specified ingress port, 
when in port mode  
port-l2cp profile 
<profile-name> ingress-port 
{sfp/1 | msa/2} 
Configuration > Physical Ports 
> Flows > General Params > 
[SFP/ Port 1 | MSA/ Port 2]> 
Port L2CP Profile 
 
Create new named flow 
and (in CLI) enter its 
command context 
[no] flow <name> 
Configuration > Physical Port 
> Flows > Add Flow > Flow 
Name 
<name> is the flow’s (new) 
name 
 
Configure existing flow / 
in CLI: enter flow’s 
command context 
flow <name> 
Configuration > Physical Port 
> Flows > Config Flow > flow 
name 
 
Map an originating 
frame P-bit value to a 
new tag P-bit value, for 
flows configured to push 
or replace VLAN tags 
with P-bits using C-tag 
marking 
inner-vlan-marking c-pbit 
<original P-bit> s-pbit <new 
P-bit> 
Configuration > Physical Port 
> Flows > General Params > 
C-Tag->S-Tag Mapping 
 
8. Traffic Processing 
Task 
CLI Command 
Web Interface Location 
Comments 
Configure changing 
destination MAC address 
to user-specified value, 
for a particular L2PT 
protocol  
l2cp-protocol {stp | oam | 
lldp | pagp | udld | cdp | vtp 
| dtp | pvstp} mac-change 
<mac-addr> 
Configuration > Physical Port 
> Flows > General Params > 
L2CP\L2PT > L2PT > Mac 
Change 
 
Configure L2CP protocol 
classification 
l2cp-mac <last-mac-byte> 
Configuration > Physical Port 
> Flows >General Params > 
L2CP\L2PT > L2CP > Last MAC 
Byte (Hex.) 
 
Create a new L2CP/L2PT 
profile and (in CLI) enter 
its command context 
[no] l2cp-profile 
<profile-name> 
Configuration > Physical Port 
> Flows > General Params > 
L2CP\L2PT > Profiles > New 
Profile Name 
<profile-name> is the profile’s 
(new) name. 
Configure existing 
L2CP/L2PT profile / 
in CLI: enter profile’s 
command context 
l2cp-profile <profile-name> 
Configuration > Physical Port 
> Flows > General Params > 
L2CP\L2PT > Profiles > profile 
name 
 
Configure L2CP protocol 
action for L2CP/L2PT 
profile 
mac <last-mac-byte> {tunnel 
| pass-through | peer | 
discard} 
Configuration > Physical Port 
> Flows > General Params > 
L2CP\L2PT > Profiles > profile 
name 
Command is in the profile 
context 
config>flows>profile(<profile-
name>) 
Configure L2CP/L2PT 
profile action for L2PT 
protocol 
protocol {stp | oam | lldp | 
pagp | udld | cdp | vtp | dtp 
| pvstp} [l2pt] {tunnel | 
pass-through | peer | 
discard} 
Configuration > Physical Port 
> Flows > General Params > 
L2CP\L2PT > Profiles > profile 
name 
Command is in the profile 
context 
config>flows>profile(<profile-
name>) 
Define outer TPID value 
for flow packets and 
double-tagged OAM 
packets 
tpid-outer-vlan <ethertype> 
ingress-port {sfp/1 | msa/2} 
Configuration > Physical Port 
> Flows > General Params > 
General Params [SFP/ Port 1 
| MSA/ Port 2] > TPID For 
Outer VLAN 
 
Define TPID value for 
new VLAN tags of 
enabled flows 
configured to push or 
replace VLAN tags, for 
specified ingress port 
tpid-pushed-replaced-vlan 
<ethertype> ingress-port 
{sfp/1 | msa/2} 
Configuration > Physical Port 
> Flows > General Params > 
General Params [SFP/ Port 1 
| MSA/ Port 2] > Tag Value 
TPID For Inner VLAN 
 
8. Traffic Processing 
Task 
CLI Command 
Web Interface Location 
Comments 
View a convenient 
summary of the 
classification mode and 
configured flows 
show summary 
-- 
 
View traffic handling 
statistics for unclassified 
(fallback) traffic 
show unclassified-statistics 
Monitoring > Physical Port > 
Classification > Unclassified 
Traffic > Unclassified [SFP/ 
Port 1 | MSA/ Port 2] 
 
Clear traffic handling 
statistics for unclassified 
(fallback) traffic 
clear-statistics 
 
 
Per-Flow Tasks 
If you want MiNID to treat all traffic in each direction uniformly, configure flows as in Configuring Port 
Mode. Otherwise, configure flows as in Configuring Flows  or in Configuring Flows Using the CLI. 
The following tasks are performed in the CLI config>flow(<name>) context, or in the Web interface. 
Per-Flow Configuration Tasks 
Task 
CLI Command 
Web Interface Location 
Comments 
Define frame values to be 
considered a match for this 
flow 
classifier match <criteria> 
Configuration > Physical Port > Flows > 
[SFP/ Port 1 | MSA/ Port 2] 
or Configuration > Physical Port > Flows > 
Config Flow > flow name 
. 
Define the ingress port of 
frames to which this flow 
applies, and the flow action 
flow-action ingress-port 
<sfp/1 | msa/2> action 
<action> [<VLAN 
parameters>] 
 
Configure flow mode for 
frame matching for layer-2 
loopback 
in-service-loops > 
in-serv-mode <mode> 
Configuration > Physical Port > Flows > 
Config Flow > In-Serv Loops 
 
Enable/disable addresses 
that should be matched for 
layer-2 loopback 
in-service-loops > 
in-serv-dst-mac <index> 
{enable|disable}  
or  
in-service-loops > 
in-serv-src-mac <index> 
{enable|disable} 
<index> is 1–4 
8. Traffic Processing 
Task 
CLI Command 
Web Interface Location 
Comments 
Define whether this flow’s 
layer-2 loopbacks should 
just loop or also swap 
addresses 
in-service-loops > 
in-serv-action {loop | 
loop-mac-ip-swap} 
 
Assign Layer-3/4 loopback 
or TWAMP responder 
in-service-l3-l4-loops > in-
serv-l3-l4-mode 
Configuration > Physical Port > Flows > 
Add Flow 
or Configuration > Physical Port > Flows > 
Config Flow > flow name or Configuration 
> Physical Port > Flows > General Params 
> In Service L3\L4 Loops  
 
Assign L2CP profile to flow 
that has classification 
VID+Pbits Range 
l2cp profile 
<profile-name> 
Configuration > Physical Port > Flows > 
Add Flow 
or Configuration > Physical Port > Flows > 
Config Flow > flow name 
 
Assign service name to flow, 
to enable network 
management systems to 
locate entities related to 
specific services 
service-name 
<service-name> 
 
Enable or disable the flow 
[no] shutdown 
To disable: 
shutdown.  
To enable: no 
shutdown 
View traffic handling 
statistics for the ffllow 
show statistics 
Monitoring > Physical Port > Classification 
>[SFP/ Port 1 | MSA/ Port 2]> Statistics 
 
Clear traffic handling 
statistics for the flow 
clear-statistics 
 
The CLI commands for flows (flow-action), unclassified traffic (fallback-action), and port mode 
(port-mode-action) include the <action> [<VLAN parameters>] parameters. The following table gives 
more details on the parameters. 
8. Traffic Processing 
Action Parameters 
Parameter 
Description 
<action>  
One of the following (see Flow Actions): 
• drop 
• pass-through 
• push-vlan (single \ double) 
• pop-vlan (single \ double) 
• replace-vlan-tag 
• loop 
• loop-mac-ip-swap 
<VLAN parameters> 
Use only if the <action> is push-vlan or replace-vlan-tag, to define 
the properties of the new VLAN tag. <VLAN parameters> is: 
vlan-id <VID> priority <P-bit mode> drop-eligible <yes|no> 
The above parameters are: 
 
Parameter 
Description 
 
<VID> 
The new tag’s VLAN ID (0-4095) 
 
<P-bit mode> 
One of the following (See Flow Actions, 
under VLAN): 
• A fixed P-bit value in range 0-7 
• For C-tag Marking: inner-vlan-
marking 
• For C-tag Copy: inner-vlan-copy 
• For DSCP Marking: dscp-marking 
 
<yes|no|by-policer> 
The new tag’s Drop Eligible Indicator 
(DEI) bit value (yes for 1) 
The by-policer option is available only 
for outer VLAN. 
Configuring Port Mode 
For a description of port mode, see Port Mode. 
8. Traffic Processing 
 To configure port mode: 
Do one of the following: 
• 
Use the CLI: 
i. 
Go to the configure flows context, and enter: 
classification mode port 
j. 
Define the action for each traffic direction by entering, for each of sfp/Port 1 and 
msa/Port 2: 
port-mode-action ingress-port <sfp/1 | msa/2> action <action> [<VLAN parameters>] 
<sfp/1 | msa/2> defines the traffic direction that the action applies to, by defining the 
ingress port as either sfp/Port 1 or msa/Port 2. For details of the <action> <VLAN 
parameters> parameters, see Action Parameters table. 
• 
Use the web interface: 
k. Go to Configuration > Physical Port > Flows. 
l. 
By Classification Mode, select Port Mode, and click <Apply> to implement the changes, and 
then click <Save Configuration>: 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows 
  
 
 
 Classification 
Mode 
 
Port Mode 
  
 
 
  
 
 
Port Mode 
m. Go to Configuration > Physical Port > Flows > General Params > SFP/Port 1.  
8. Traffic Processing 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>General Params>SFP/Port 1 
  
 
 
 TPID For Outer VLAN 
 
0x88a8 
 TPID For Inner VLAN 
 
0x8100 
  
 
0x8100 
  
 
0x8100 
 Port Mode Policer Type 
 
Disabled 
 Port Mode PM Collection 
 
Disable 
 Port Mode Action 
 
Pass Through 
 L2CP Profile 
 
kl2cp 
 
IP Agnostic loop 
 
Disable (option available In 
“port mode” only) 
 In-Service L2 Loops (Port Mode) 
 
 LBM reflector  
 
 In-Service L3\L4 Loops (Port Mode) 
 
  
 
 
General Params [SFP/Port 1] – Port Mode 
n. Set the Port Mode Action (see Flow Actions) for SFP-to-MSA/ port 1–to–port 2 traffic. If you 
select Push VLAN or Replace VLAN, the additional following VLAN settings appear: 
 
VID: The new tag’s VLAN ID (0–4095) 
 
Pbits Mode: See Flow Actions (under VLAN) 
 
Pbits Value: The new tag’s p-bit value if Pbits Mode is set to Fixed Value (0–7) 
 
Drop Eligible: The new tag’s Drop Eligible Indicator (DEI) bit value (Yes for 1, No for 0 and 
“by policer” for outer VLAN only, takes the DEI bit from the policer) 
o. Port L2CP Profile: Select an L2CP profile if necessary for your application 
p. If you want to configure LBM reflectors, click LBM reflector (see Configuring LBM Reflector). 
q. Click <Apply> to implement the changes, and then click <Save Configuration> 
r. Go to Configuration > Physical Port > Flows > General Params> MSA/Port 2, set the same 
parameters in the same way for MSA-to-SFP/ port 2–to–port 1 traffic, and click <Apply> to 
implement the changes, and then click <Save Configuration>. 
8. Traffic Processing 
Configuring Flows Using the Web Interface 
Configuring General Parameters 
 To configure general flow parameters: 
1. To configure flow classification mode, go to Configuration > Physical Port > FlowsPort Name, 
and select the Classification Mode from one of the following, to set the criterion by which all 
traffic in both directions will be classified (see Flow Classification): 
 
DSCP 
 
EtherType 
 
MAC SRC 
 
MAC DST 
 
Port Mode 
 
VID + Pbits Range 
Note 
If you change the flow classification mode, all configured flows are deleted. 
 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>Flows SFP/Port 1 or 
MSA/Port 2 
  
 
 
 Classification 
Mode 
 
VID + Pbits Range 
  
 
 
 Add Flow 
 
 
 Config Flow 
 
 
  
 
 
Classification Mode 
1. Click <Apply> to apply the changed flow classification mode, and then click 
<Save Configuration>. 
2. Go to Configuration > Physical Port > Flows > General Params > SFP/Port 1, set the following 
fields for SFP-to-MSA/ port 1–to–port 2 traffic, and click <Apply> to implement the changes, and 
then click <Save Configuration>; then, go into General Params > MSA/Port 2  and set the same 
fields for MSA-to-SFP/ port 2–to–port 1 traffic: 
8. Traffic Processing 
 
TPID For Outer VLAN – Applied to flow packets and as the outer TPID of double-tagged 
OAM packets 
 
TPID For Inner VLAN –Applied to packets for this traffic direction if VLAN tags are pushed or 
replaced  
 
Fallback L2CP Profile – Binds the L2CP profile to the unclassified flow of the port 
 
Unclassified Action – Applied to all traffic in this direction that is not matched by any 
enabled flow. Available actions are the same as for flows. 
If you want to configure LBM reflectors, click LBM reflector (see Configuring LBM Reflector for 
details). 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>General Params>SFP/Port 1  
  
 
 
 TPID For Outer VLAN 
 
0x88a8 
 TPID For Inner VLAN 
 
0x8100 
  
 
0x8100 
  
 
0x8100 
 Fallback Policer Type 
 
Disabled 
 Fallback PM Collection 
 
Disable 
 Fallback L2CP Profile 
 
 
 Unclassified Action 
 
Pass Through 
 Port Mode Action 
 
Pass Through 
  
 
 
 LBM reflector 
 
 
  
 
 
General Parameters [SFP/Port 1] – Flow Mode 
1. If you have any flows with Push or Replace VLAN actions with a P-bits Mode of C-Tag Marking, 
go to Configuration > Physical Port > Flows Classification > General Params > C-Tag->S-Tag 
Mapping, configure the P-bits-to-P-bits mapping and click <Apply> to implement the changes, 
and then click <Save Configuration>: 
8. Traffic Processing 
MiNID 
 
 
 
 
 
Configuration>Physical Ports>Flows>General Params>CTag Remap 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
00  
0 
 
01  
0 
 
02 
 
3 
 
03  
3 
 
 
 
04  
3 
 
05  
3 
 
06 
 
7 
 
07  
0 
 
 
 
 
 
P-bit-to-P-bit Mapping 
1. If you have any flows with Push or Replace VLAN actions with a P-bits Mode of DSCP Marking, 
go to Configuration > Physical Port > Flows Classification > General Params > DSCP->S-Tag 
Mapping, configure the DSCP-to-P-bits mapping and click <Apply> to implement the changes, 
and then click <Save Configuration>: 
8. Traffic Processing 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>General Params>DSCP Remap 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 0
0 
 
01 
 
02 
 
03 
 
04 
 
05 
 
06 
 
07 
 
 0 
 
1 
 
2 
 
3 
 
4 
 
5 
 
6 
 
7 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 0
8 
 
09 
 
10 
 
11 
 
12 
 
13 
 
14 
 
15 
 
 0 
 
1 
 
2 
 
3 
 
4 
 
5 
 
6 
 
7 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 1
6 
 
17 
 
18 
 
19 
 
20 
 
21 
 
22 
 
23 
 
 0 
 
1 
 
2 
 
3 
 
4 
 
5 
 
6 
 
7 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 2
4 
 
25 
 
26 
 
27 
 
28 
 
29 
 
30 
 
31 
 
 0 
 
1 
 
2 
 
3 
 
4 
 
5 
 
6 
 
7 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 3
2 
 
33 
 
34 
 
35 
 
36 
 
37 
 
38 
 
39 
 
 0 
 
1 
 
2 
 
3 
 
4 
 
5 
 
6 
 
7 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 4
0 
 
41 
 
42 
 
43 
 
44 
 
45 
 
46 
 
47 
 
 0 
 
1 
 
2 
 
3 
 
4 
 
5 
 
6 
 
7 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 4
8 
 
49 
 
50 
 
51 
 
52 
 
53 
 
54 
 
55 
 
 0 
 
1 
 
2 
 
3 
 
4 
 
5 
 
6 
 
7 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 5
6 
 
57 
 
58 
 
59 
 
60 
 
61 
 
62 
 
63 
 
 0 
 
1 
 
2 
 
3 
 
4 
 
5 
 
6 
 
7 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
8. Traffic Processing 
DSCP-to-P-bit Mapping 
1. To configure layer-2 loopback general parameters, go to Configuration > Physical Port > Flows > 
General Params > In Service Loop MACs, and define the Source and Destination MAC addresses 
to be available for flow layer-2 loopback: 
MiNID 
 
 
 
 
 
Configuration>Physical Port>Flows>General Params>In Service Loop MACs 
 
 
 
 
 
Source Addresses 
Destination Addresses 
 
 
12-34-56-78-90-ab 
cd-ef-12-34-56-78 
 
 
00-00-00-00-00-00 
00-00-00-00-00-00 
 
 
00-00-00-00-00-00 
00-00-00-00-00-00 
 
 
00-00-00-00-00-00 
00-00-00-00-00-00 
 
 
 
 
In-Service Loopback MACs 
1. Click <Apply> to implement the changes to the layer-2 loopback MAC addresses, and then click 
<Save Configuration>. 
2. To configure layer-3/4 loopback general parameters, go to Configuration > Physical Port > Flows 
> General Params > In Service L3\L4 Loops. 
MiNID 
 
 
 
 
 
Configuration > Physical Port > Flows > General Params > In-Serv L3\L4 Loops 
 
 
 
 
In-Service L3\L4:IP Loop 
 
 
 
In-Service L3\L4:UDP Loop 
 
 
 
In-Service L3\L4:UDP Echo 
 
 
 
 
 
 
In-Service Layer-3/4 Loopback General Parameters 
1. Select the loop type for which you wish to configure the general parameters: 
 
IP Loop – Click <In-Service L3\L4:IP Loop> 
 
UDP Loop – Click <In-Service L3\L4: UDP Loop> 
 
UDP Echo – Click <In-Service L3\L4: UDP Echo>. 
8. Traffic Processing 
MiNID 
 
 
 
 
 
Configuration > Physical Port > Flows > General Params > In-Serv L3\L4 Loops > 
IP Loop 
 
 
 
 
Destination IP Address 
 
192.168.205.100 
 
 
 
 
In-Service Layer-3/4 Loopback General Parameters – IP Loop 
MiNID 
 
 
 
 
 
Configuration > Physical Port > Flows > General Params > In-Serv L3\L4 Loops > 
UDP Loop 
 
 
 
 
Destination IP Address 
 
192.168.205.101 
 
Destination UDP Port 
 
153 
 
 
 
 
In-Service Layer-3/4 Loopback General Parameters – UDP Loop 
MiNID 
 
 
 
 
 
Configuration > Physical Port > Flows > General Params > In-Serv L3\L4 Loops > 
UDP ECHO 
 
 
 
 
Destination IP Address 
 
192.168.205.102 
 
Destination UDP Port 
 
222 
 
 
 
 
In-Service Layer-3/4 Loopback General Parameters – UDP Echo 
1. Set the general parameters (see General Configuration Tasks table). 
Note 
When IP agnostic loop is enabled, the IP loop option under In-Serv L3\L4 Loops 
is not available. In addition, configuration of an IP address for UDP loop, UDP 
Echo and TWAMP responder is not relevant (the option is blocked). 
8. Traffic Processing 
Configuring Flows 
 To add or configure flows: 
1. To add a new flow, go to Configuration > Physical Port > Flows > SFP/Port 1 or MSA/Port 2, and 
click <Add Flow>. 
MiNID 
  
 
 
 Configuration>Physical Port>Flows> Add Flow 
  
 
 
 Flow Name 
 
Flow 11 
 Service Name 
 
Gold 
 Flow Enable 
 
Enable 
 Ingress Port 
 
SFP/Port 1 
 L2CP Profile 
 
kl2cp 
 L3L4 Loop 
 
Disabled 
 PM Collection 
 
Disable 
 Policer Type 
 
Disabled 
 Classification Tag Mode 
 
Single 
 Min VID Value 
 
0 
 Max VID Value 
 
4095 
 Min Pbit Value 
 
5 
 Max Pbit Value 
 
5 
 Flow Action 
 
Push VLAN 
  
 
 
 
 Apply 
 
 
 
  
 
 
Add Flow with Single Tag VLAN 
8. Traffic Processing 
MiNID 
  
 
 
 Configuration>Physical Port>Flows>Add Flow 
  
 
 
 Flow Name 
 
Flow 11 
 Service Name 
 
Gold 
 Admin Status 
 
Enable 
 Ingress Port 
 
SFP/Port 1 
 L2CP Profile 
 
kl2cp 
 L3L4 Loop 
 
Disabled 
 PM Collection 
 
Disable 
 Policer Type 
 
Disabled 
 Classification Tag Mode 
 
Double 
 Outer VID Value 
 
 
 Outer Min Pbit Value: 
 
 
 Outer Max Pbit Value 
 
 
 Inner Min VID Value 
 
 
 Inner Max VID Value 
 
 
 Inner Min P-bit Value 
 
 
 Inner Max P-bit Value 
 
 
 Flow Action 
 
Push VLAN 
  
 
 
 Outer VLAN Information: 
 
 
 VID 
Pbits Mode 
Pbits Value (Fixed 
Value Only) 
Drop Eligible 
 2222 
Fixed Value 
3 
No 
  
 
 
Add Flow with Double Tag VLAN 
8. Traffic Processing 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>Add Flow 
  
 
 
 Flow Name 
 
Flow 11 
 Service Name 
 
Gold 
 Admin Status 
 
Enable 
 Ingress Port 
 
SFP/Port 1 
 L2CP Profile 
 
kl2cp 
 L3L4 Loop 
 
Disabled 
 PM Collection 
 
Disable 
 Policer Type 
 
Envelope 
 Envelope Profile 
 
 
 Cos Map Profile 
 
 
 Classification Tag Mode 
 
Single 
 Min VID Value 
 
 
 Max VID Value 
 
 
 Min Pbit Value 
 
 
 Max Pbit Value 
 
 
 Flow Action 
 
Push VLAN 
  
 
 
 Outer VLAN Information: 
 
 
 VID 
Pbits Mode 
Pbits Value (Fixed 
Value Only) 
Drop Eligible 
 2222 
Fixed Value 
3 
No 
  
 
 
Add Flow with Policer 
1. To configure an existing flow: 
s. Go to Configuration > Physical Port > Flows > Classification SFP/MSA, and click <Config 
Flow>. 
8. Traffic Processing 
MiNID 
 
 
 
 
 
 
 
 
 
Configuration>Physical Port>Flows>Config Flow 
 
 
 
 
 
 
 
 
 
Flow 
Name 
Service 
Name 
 
 
 
 
 
 
22 
Gold 
Disable Flow 
In-Serv Loops 
In-Serv 
L3\L4 Loops 
Test 
Delete 
Flow 
 
 
11 
Gold 
Disable Flow 
In-Serv Loops 
In-Serv 
L3\L4 Loops 
Test 
Delete 
Flow 
 
 
 
 
 
 
 
 
 
Configure Flows 
 
u. If necessary, click Disable Flow in the row corresponding to the flow, as the flow must be 
administratively disabled in order to edit it.  
v. Click the flow name to display the Flow Info screen. 
 
8. Traffic Processing 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>Flow (Flow name) > Flow 
Info 
  
 
 
 Flow Name 
 
Flow 11 
 Service Name 
 
Gold 
 Flow Enable 
 
Disable 
 Ingress Port 
 
SFP/Port 1 
 L2CP Profile 
 
kl2cp 
 L3L4 Loop 
 
TWAMP Responder 
 TWAMP Session 
 
tw1 
 Min VID Value: 
 
0 
 Max VID Value: 
 
4095 
 Min P-bit Value: 
 
5 
 Max P-bit Value: 
 
5 
 Flow Action 
 
Push VLAN 
  
 
 
 VLAN Header 
Information: 
 
 
 VID 
Pbits Mode 
Pbits Value (Fixed 
Value Only) 
Drop Eligible 
 2222 
Fixed Value 
3 
No 
  
 
 
Flow Info 
1. In the Add Flow or Flow Info screens, configure the settings: 
 
Flow Name (if adding the flow) 
 
Service Name – The service name enables network management systems to locate entities 
related to specific services 
 
Admin Status (if adding the flow) – A disabled flow retains its configuration for future use, 
and is included in the count of flows in connection to the maximum of 16 configured flows.  
 
Ingress Port – MSA/Port 2 for customer-to-provider/Ethernet port 2 traffic or SFP/Port 1 for 
provider-to-customer /Ethernet port 1 traffic 
 
L2CP Profile – Select an L2CP profile if necessary for your application (this parameter 
appears only if classification mode is VID+Pbits Range) 
8. Traffic Processing 
 
L3L4 Loop – Set the flow layer-3/4 loopback mode to one of the following (see Layer-3/4 
Loopbacks for more information on the layer-3/4 loopback types): 
 
Disabled 
 
IP Loop – Layer 3/4 loopback, type IP loop 
 
UDP Loop – Layer 3/4 loopback, type UDP loop 
 
UDP Echo – Layer 3/4 loopback, type UDP echo 
Note 
Before setting layer-3/4 loopback mode to IP Loop, UDP Loop, or UDP Echo, 
you need to configure the general layer-3/4 loopback parameters as described 
in Configuring General Parameters. 
 
 
TWAMP responder – associate the flow with a TWAMP responder 
If this option is selected, the TWAMP Session parameter appears in the screen, and you 
can select from a dropdown list of the configured TWAMP responders. See OAM 
(TWAMP) for more information on TWAMP responders. 
Note 
The flow layer-3/4 loopback mode can also be set via the In Serv L3\L4 Loops 
screen (see Configuring Layer-3/4 Loopbacks). 
 
 
PM Collection – The PM Collection enables setting a PM Interval for monitoring microbursts 
in network traffic 
 
PM Interval – Set the duration of the time period for measuring the microbursts 
 
Policer Type –Standardized according to MEF 10.2 
 
Test – This command allows the user to change the flow action to either of the following: 
 
Loop With MAC (IP) Swap 
 
Discard 
without changing the flow action by configuration. This command cannot be saved in a 
database, so if the unit is reset, the flow action returns to its configured action. This 
command can be used for temporary change of the flow action.  
 
Flow criteria – These appear differently depending on the current classification mode. 
If the classification mode is VID+Pbits Range and you want to define a flow by just VLAN ID, 
configure it for the full range of possible P-bits (0-7) and specify the desired VLAN ID range. 
Similarly, if you want to define the flow by just priority, configure it for the full range of 
possible VLAN IDs (0-4095) and specify the desired P-bit range. 
If the Classification Tag Mode is “Double”, configure the following parameters: 
 
Outer VID Value: The VID of the outer VLAN 
 
Outer Min P-bit Value: Minimum P-bit value for outer VLAN 
 
Outer Max P-bit Value: Maximum P-bit value for outer VLAN 
 
Inner Min VID Value: Minimum VLAN ID value for inner VLAN 
 
Inner Max VID Value: Maximum VLAN ID value for inner VLAN 
8. Traffic Processing 
 
Inner Min P-bit Value: Minimum P-bit value for inner VLAN 
 
Inner Max P-bit Value: Maximum P-bit value for inner VLAN 
Single flow under this classification can be set as “Untagged”. 
 
Flow Action – See Flow Actions. 
If the Flow Action is Push VLAN or Replace VLAN, the additional following VLAN settings 
appear: 
 
VID: The new tag’s VLAN ID (0-4095) 
 
Pbits Mode: See Flow Actions (under VLAN) 
 
Pbits Value: The new tag’s P-bit value if Pbits Mode is set to Fixed Value (0-7) 
 
Tag Ether Type: The VLAN Ethertype 
 
Drop Eligible: The new tag’s Drop Eligible Indicator (DEI) bit value (Yes for 1) 
2. Click <Apply> to implement the changes, and then click <Save Configuration>. 
Configuring Layer-2 Loopbacks 
This procedure describes how to configure flow/port layer-2 loopbacks. Before configuring layer-2 
loopbacks, configure the general layer-2 loopback parameters as described in Configuring General 
Parameters. 
 To configure layer-2 loopbacks: 
1. If flow classification is not per port: 
w. Go to Configuration > Physical Port > Classification > Config Flow. 
x. In the row corresponding to the flow, click In-Serv Loops.  
8. Traffic Processing 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>Flow (cust-traf)>In-Serv Loops 
  
 
 
 In-Service Action 
 
Loop With MAC (IP) Swap 
 In-Service Mode 
 
SA+DA 
  
 
 
 In-Service Source Addresses: 
 
 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
 In-Service Destination 
Addresses: 
 
 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
  
 
 
Layer-2 Loop Configuration – Flow  
1. If flow classification is per port: 
y. Go to Configuration > Physical Port > Flows> General Params [SFP/Port 1] to configure 
layer-2 parameters for SFP/Port 1  
z. In the General Params[SFP/Port 1] screen, click In-Service L2 Loops (Port Mode) 
8. Traffic Processing 
MiNID  
  
 
 
 Configuration>Physical Ports>Flows>SFP/Port 1> In-Service L2 
Loops (Port Mode) 
  
 
 
 In-Service Action 
 
Loop With MAC (IP) Swap 
 In-Service Mode 
 
SA+DA 
  
 
 
 In-Service Source Addresses: 
 
 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
 In-Service Destination 
Addresses: 
 
 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
 00-00-00-00-00-00 
 
Disable 
  
 
 
Layer-2 Loop Configuration – SFP/Port 1 
1. By In-Service Action, define whether the flow/port layer-2 loopbacks should just Loop or Loop 
with MAC (IP) Swap (See Layer-2 Loopbacks). 
2. By In-Service Mode, set the flow/port mode for frame matching (See Layer-2 Loopbacks). 
3. Enable each MAC address that should be matched for layer-2 loopback for the flow/port. 
4. Save. 
5. Click <Apply> to implement the changes, and then click <Save Configuration>. 
6. If flow classification is per port, go to Configuration > Physical Port > Flows > General Params 
[MSA/Port 2], set the same parameters in the same way for MSA/port 2, and click <Apply> to 
implement the changes, and then click <Save Configuration>. 
8. Traffic Processing 
Configuring Layer-3/4 Loopbacks 
This procedure describes how to configure flow/port layer-3/4 loopbacks, or bind a TWAMP responder 
to a flow/port. Before configuring layer-3/4 loopback, configure the general layer-3/4 loopback 
parameters as described in Configuring General Parameters. 
 To configure layer-3/4 loopbacks: 
1. If flow classification is not per port: 
a. Go to Configuration > Physical Port > Classification > Config Flow. 
b. In the row corresponding to the flow, click In-Serv L3\L4 Loops. 
Note 
The flow layer-3/4 loopback parameters can also be configured by clicking the 
flow name to edit the flow parameters (see Configuring Flows). 
 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>Flow (data1)>In-Serv L3\L4 Loops 
  
 
 
  
 
 
 In-Service L3\L4 Mode 
 
UDP Loop 
  
 
 
 In-Service IP Destination 
Address: 
 
192.168.205.101 
 In-Service UDP Destination 
Port 
 
153 
  
 
 
Layer-3/4 Loop Mode Configuration – Flow  
1. If flow classification is per port: 
a. Go to Configuration > Physical Port > Flows > General Params > SFP/Port 1 to configure 
layer-3/4 loopback mode for SFP/Port 1. 
b. In the General Params [SFP/Port 1] screen, click In-Service L3\L4 Loops (Port Mode). 
8. Traffic Processing 
MiNID 
  
 
 
 Configuration > Physical Ports > Flows > SFP/Port 1 > In-Service L3\L4 
Loops (Port Mode) 
  
 
 
  
 
 
 In-Service L3\L4 Mode 
 
UDP Loop 
  
 
 
 In-Service IP Destination 
Address: 
 
192.168.205.101 
 In-Service UDP Destination 
Port 
 
153 
  
 
 
Layer-3/4 Loopback Mode Configuration – SFP/Port 1 
1. By In-Service L3\L4 Mode, set the flow/port layer-3/4 loopback mode to one of the following 
(see Layer-3/4 Loopbacks for more information on the layer-3/4 loopback types): 
 
Disabled 
 
IP Loop – Layer 3/4 loopback, type IP loop 
 
UDP Loop –Layer 3/4 loopback, type UDP loop 
 
UDP Echo – Layer 3/4 loopback, type UDP echo  
 
Note 
If the IP address (and UDP port if applicable) have not been set for a particular 
layer-3/4 loopback type, it does not appear in the dropdown list for In-Service 
L3\L4 Mode 
 
TWAMP responder – associate the flow/port with a TWAMP responder. 
If this option is selected, the TWAMP Session parameter appears in the screen, and you can 
select from a dropdown list of the configured TWAMP responders. See OAM (TWAMP) for 
more information on TWAMP responders. 
2. Click <Apply> to implement the changes, and then click <Save Configuration>. 
3. If flow classification is per port, go to Configuration > Physical Port > Flows > General Params> 
MSA/Port 2, set the same parameters in the same way for MSA/port 2, and click <Apply> to 
implement the changes, and then click <Save Configuration>. 
8. Traffic Processing 
Configuring IP-Agnostic Loops 
Note 
When IP agnostic loop is enabled, the IP loop option under In-Serv L3\L4 Loops 
is not available. In addition, configuration of an IP address for UDP loop, UDP 
Echo and TWAMP responder is not relevant (the option is blocked). 
 
Note 
IP-agnostic loops can be configured in “Port Mode” only. 
 To configure IP-agnostic loops: 
1. Go to Configuration>Physical Ports>Flows>Port Name and select Port Mode in Classification 
Mode. 
MiNID 
  
 
 
 Configuration > Physical Ports > Flows >Flows Port Name 
  
 
 
  
 
 
 Classification Mode 
 
Port Mode 
  
 
 
  
 
 
  
 
 
  
 
 
1. Go to Configuration> Physical Ports> Flows> General Params> SFP/Port 1/ MSA/Port 2 and 
enable the IP-agnostic loop. 
8. Traffic Processing 
MiNID 
  
 
 
 Configuration > Physical Ports > Flows >General Params> SFP/Port 1/ 
MSA/Port 2  
  
 
 
 TPID For Outer VLAN 
 
0×88a8 
 TPID For Inner VLAN 
 
0×8100 
  
 
0×8100 
  
 
0×8100 
 Port Mode Policer Type 
 
Disabled 
 Port Mode PM Collection 
 
Disable 
 L2CP Profile 
 
 
 Port Mode Action 
 
Pass Through 
 IP Agnostic Loop 
 
Enable 
 
 
 
 
IP-Agnostic Loop Configuration 
1. Click <Apply> to implement the changes, and then click <Save Configuration>. 
Configuring Flows Using the CLI 
Configuring General Parameters 
 To configure general flow parameters: 
1. Go to the configure flows context. 
2. Set the classification mode with the following command. This is the criterion by which all traffic 
in both directions will be classified (see Flow Classification for mode descriptions): 
classification mode <mode> 
where <mode> is one of: 
 
dscp 
 
ethertype 
 
src-mac (source MAC address) 
 
dst-mac (destination MAC address) 
8. Traffic Processing 
 
vlan-pbits-range (VLAN ID range and P-bit range) 
Note 
If you change the flow classification mode, all configured flows are deleted. 
3. By default, traffic that does not match any enabled flow is passed through. To change the action 
for unmatched traffic in either direction, enter: 
fallback-action ingress-port {sfp/1 | msa/2} action <action> [<VLAN parameters>] 
For details of the <action> <VLAN parameters> parameters, see Action Parameters table. 
4. The outer TPID value for flow packets and double-tagged OAM packets is specified by 
tpid-outer-vlan. To change the value for all flows of one direction, in the configure flows 
context, enter: 
tpid-outer-vlan <ethertype> ingress-port {sfp/1 | msa/2} 
where <ethertype> is the hexadecimal TPID value to apply, and {sfp/1 | msa/2}  is either sfp/1 
(for SFP-to-MSA/ port 1–to–port 2 traffic) or msa/2 (for MSA-to-SFP/ port 2–to–port 1 traffic). 
The inner TPID value for flow packets and double-tagged OAM packets is tpid-inner-vlan. To add 
or change the value in the configure flows context, enter: 
tpid-inner-vlan <ethertype> ingress-port {sfp/1|msa/2}. 
You can configure up to 3 inner TPIDs. To delete one, type [no] before one of the entries. 
5. All flows in each direction that push or replace VLAN tags apply the TPID value specified by 
tpid-inner-vlan. To change the value for all flows of one direction, in the configure flows 
context, enter: 
tpid-inner-vlan <ethertype> ingress-port {sfp/1 | msa/2} 
where <ethertype> is the hexadecimal TPID value to apply, and {sfp/1 | msa/2} is either sfp/1 
(for SFP-to-MSA/port 1–to–port 2 traffic) or msa/2 (for MSA-to-SFP/ port 2–to–port 1 traffic). 
6. If you have any flows with Push or Replace VLAN actions configured with P-bits mode of C-tag 
marking, configure the P-bits-to-P-bits mapping. For each P-bit value of the originating frame 
that needs to be mapped to a non-default value, enter: 
inner-vlan-marking c-pbit <original P-bit> s-pbit <new P-bit> 
7. If you have any flows with Push or Replace VLAN actions configured with P-bits Mode of DSCP 
Marking, configure the DSCP-to-P-bits mapping. For each DSCP value of the originating frame’s 
IP payload that needs to be mapped to a non-default value, enter: 
dscp-marking dscp <DSCP value> s-pbit <new P-bit> 
8. To configure up to four source MAC addresses and up to four destination MAC addresses for 
flow layer-2 loopback, enter: 
in-service-mac {src|dst}-addr <index> <address> 
where the above parameters are: 
8. Traffic Processing 
Parameters for in-service-mac  
Parameter 
Description 
<src|dst> 
Whether configuring a source address or a destination address 
<index> 
A number in range 1–4 identifying this source or destination 
address, for reference when enabling/disabling loopback for this 
address per-flow 
<address> 
The MAC address, in format xx-xx-xx-xx-xx-xx, where xx is a valid 
hexadecimal number in two digits 
9. To configure layer-3/4 loopback general parameters: 
a. Enter in-service-l3-l4, in order to go into the config>flows>in-serv-l3-l4 context. 
b. Enter all necessary commands according to the tasks listed below (see General 
Configuration Tasks table for more information on the parameters). 
10. To configure IP-agnostic loops: 
a. Enter classification mode port to enable IP agnostic loop. 
b. Enter all necessary commands according to the tasks listed below (see General 
Configuration Tasks table for more information on the parameters).  
Task 
Command 
Comments 
Specify IP agnostic loop 
ip-agnostic-loop {sfp/1 | msa/2} 
SFP sleeve option – Port mode must 
be configured to enable IP agnostic 
loop 
Specify the IP address to match to packet 
destination IP addresses for IP loop 
layer-3/4 loopback 
ip-loop ip-address <ip-dest-addr> 
<ip-dest-addr> – IP address in 
format aaa.bbb.ccc.ddd 
Specify the IP address to match to packet 
destination IP addresses for UDP loop 
layer-3/4 loopback 
udp-loop ip-address <ip-dest-addr> 
<ip-dest-addr> – IP address in 
format aaa.bbb.ccc.ddd 
Specify the UDP port to match to packet 
destination UDP ports for UDP loop 
layer-3/4 loopback 
udp-loop udp-port <udp-dest-port> 
<udp-dest-port> – UDP port number 
Specify the IP address to match to packet 
destination IP addresses for UDP echo 
layer-3/4 loopback 
udp-echo ip-address <ip-dest-addr> 
<ip-dest-addr> – IP address in 
format aaa.bbb.ccc.ddd 
8. Traffic Processing 
Task 
Command 
Comments 
Specify the UDP port to match to packet 
destination UDP ports for UDP echo 
layer-3/4 loopback 
udp-echo udp-port <udp-dest-port> 
<udp-dest-port> – UDP port number 
 
Configuring Flows 
 To configure flows: 
1. Go to the configure flows context, and enter: 
flow <flow-name>: 
where <name> is the flow name.  
The CLI enters the flow context. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Setting the flow classification 
classifier match <criteria> 
The parameter <criteria> depends on the 
current classification mode (see Classifier 
Criteria table) 
Associating the flow with a 
classifier profile 
classifier <classifier-profile-name> 
If the flow is multi-CoS, the classification must 
be one of the following: 
• VLAN, VLAN + inner VLAN, VLAN range 
• Match all 
• Untagged 
 
Associating the flow with a CoS 
mapping profile 
cos-mapping profile <cos-mapping-
profile-name> 
See CoS Map Porfiles in Chapter 11. 
Enter no cos-mapping to disable the profile 
Specifying flow action 
flow-action ingress-port {sfp/1 | 
msa/2} action <action> <VLAN 
parameters> 
See Flow Actions.  
The parameter {sfp/1 | msa/2} defines the 
traffic direction that this flow applies to, by 
defining the ingress port as SFP/port 1 or 
MSA/ port 2. 
For details of the <action> <VLAN parameters> 
parameters, see Action Parameters table. 
Configuring layer-2 loopbacks 
in-service-loops 
See Configuring Layer-2 Loopbacks  
8. Traffic Processing 
Task 
Command 
Comments 
Configuring layer-3/4 
loopbacks 
in-service-l3-l4-loops 
See Configuring Layer-3/4 Loopbacks 
Associating an L2CP profile 
with the flow 
l2cp profile <profile-name> 
Relevant only if classification mode is 
vlan-pbits-range 
Enabling PM collection and 
setting the duration of the 
collection in seconds 
pm-collection interval <seconds> 
See Microburst Monitoring in Chapter 11 
Enter no pm-collection to disable the 
collection 
Setting the policer type used 
for the flow 
policer [profile | regular-accounting-
only | envelope] 
The following policer types can be defined: 
• profile – Regular policer profile (See 
Policer Profiles in Chapter 11) 
• regular-accounting-only – Profile used to 
only count the statistics, without limiting 
the traffic (See  
• envelope – Envelope profile (See Envelope 
Bandwidth Profiles in Chapter 11). 
Enter no policer to disable the policer 
Associating a service name to 
with the flow, to enable 
network management systems 
to locate entities related to 
specific services 
service-name <service-name> 
 
Test 
test <loop-mac-ip-swap>/<discard> 
Enter no test to remove test 
Administratively enabling or 
disabling flow 
shutdown 
Enter no shutdown to enable the flow 
Clearing flow statistics 
clear-statistics 
 
Viewing flow statistics 
show statistics 
See Viewing Flow Statistics 
 
Classifier Criteria 
Classification Mode 
<criteria> 
Example 
DSCP 
dscp <value> 
classifier match dscp 63 
Ethertype 
ether-type <hexadecimal value> 
classifier match ether-type 0x8100 
Source MAC 
src-mac <MAC address> 
classifier match 
src-mac 12-34-56-78-90-ab 
8. Traffic Processing 
Classification Mode 
<criteria> 
Example 
Destination MAC 
dst-mac <MAC address> 
classifier match 
dst-mac cd-ef-12-34-56-78 
Source and destination 
MACs 
src-mac <source MAC> dst-mac 
<destination MAC> 
classifier match 
src-mac 12-34-56-78-90-ab 
dst-mac cd-ef-12-34-56-78 
VLAN ID and P-Bit 
vlan-min <VID minimum> pbit-min <P-bit 
minimum> vlan-max <VID maximum> 
pbit-max <P-bit maximum> 
classifier match vlan-min 0 pbit-min 4 
vlan-max 4095 pbit-max 4 
 
Configuring Layer-2 Loopbacks  
This procedure describes how to configure flow/port layer-2 loopbacks. Before configuring layer-2 
loopbacks, configure the general layer-2 loopback parameters as described in Configuring General 
Parameters. 
 To configure layer-2 loopback: 
1. Go to the configure flows flow(<flow-name>) context. 
2. According to the flow classification: 
 
Any classification other than per port – Enter in-service-loops to go into the 
config>flows>flow(<flow-name>)>in-serv context 
 
Classification per port – Enter one of the following, according to which port you want to 
configure: 
 
in-service-loops sfp/1 to go into the context config>flows>in-serv(sfp/1) 
 
in-service-loops msa/2 to go into the context config>flows>in-serv(msa/2) 
3. Configure the flow/port mode for layer-2 loopback frame matching, by entering: 
in-serv-mode <mode> 
where <mode> is one of (see Layer-2 Loopbacks): 
 
src 
 
dst 
 
src-dst 
4. For each MAC address that should be matched for layer-2 loopback for the flow/port, enter: 
[no] in-serv-<src|dst>-mac <index>  
where the above parameters are: 
8. Traffic Processing 
in-serv Parameters 
Parameter 
Description 
<src|dst> 
Whether enabling a source address or a destination address 
<index> 
A number in range 1–4 identifying this source or destination 
address, referring to the addresses configured in step 3 above 
5. Define whether the flow/port layer-2 loopbacks should just loop or also swap addresses (see 
Layer-2 Loopbacks). Enter: 
in-serv-action <loop|loop-mac-ip-swap> 
Configuring Layer-3/4 Loopbacks 
This procedure describes how to configure flow/port layer-3/4 loopbacks, or bind a TWAMP responder 
to a flow/port. Before configuring layer-3/4 loopbacks, configure the general layer-3/4 loopback 
parameters as described in Configuring General Parameters. 
 To configure layer-3/4 loopbacks: 
1. Go to the configure flows flow(<flow-name>) context. 
2. According to the flow classification: 
 
Any classification other than per port – Enter in-service-l3-l4-loops to go into the 
config>flows>flow(<flow-name>)>in-serv -l3-l4 context 
 
Classification per port – Enter one of the following, according to which port you want to 
configure: 
 
in-service-l3-l4-loops sfp/1 to go into the context config>flows>in-serv-l3-l4(sfp/1) 
 
in-service-l3-l4-loops msa/2 to go into the context config>flows>in-serv-l3-l4(msa/2) 
3. Configure the layer-3/4 loopback mode by entering the following command: 
[no] in-serv-l3-l4-mode <{ip-loop | udp-loop | udp-echo-loop | twamp} 
Note 
Before setting layer-3/4 loopback mode to IP Loop, UDP Loop, or UDP Echo, 
you need to configure the general layer-3/4 loopback parameters as described 
in Configuring General Parameters. 
4. If you specified twamp as the loopback mode, enter the following command to bind a TWAMP 
responder to the flow (see OAM (TWAMP) for more information on TWAMP responders): 
responder <responder-name> 
8. Traffic Processing 
Configuring IP-Agnostic Loops 
Note 
IP-agnostic loops can be configured in “Port Mode” only. 
 To configure IP-agnostic loops: 
1. Configure classification mode “Port”. 
2. Enable IP-agnostic loop for SFP port 1 MSA/port 2.   
MiNID>config>flows# classification mode port 
MiNID>config>flows# ip-agnostic-loop {sfp/1 | msa/2}   
3. Save the configuration. 
Configuring LBM Reflector 
You can configure a generic LBM reflector that enables replying with LBR to any LBM packet received 
with any VLAN and selected MD levels, per SFP/port 1 or MSA/port 2. By default, the LBM reflector is 
disabled. 
When the LBM reflector is enabled, LBRs are sent in reply to any received LBM with an MD level for 
which the LBM reflector is enabled. 
You can view counters for each port that show how many LBM packets have been received (see Viewing 
Port Statistics). 
Configuring LBM Reflector Using the Web Interface 
 To configure LBM reflector parameters: 
1. Navigate to the General Parameters screen for the SFP/port 1 or MSA/port 2, according to which 
port’s parameters you want to configure.  
2. Click LBM reflector. 
Note 
The figure below illustrates the screen for Configuration>Physical 
Ports>Flows>General Params>SFP/Port 1>LBM Reflector, which is the same 
screen as Configuration>Physical Ports>Flows>General 
Params>MSA/Port 2>LBM Reflector except for the menu path at the top of 
the screen. 
 
8. Traffic Processing 
MiNID  
 
 
 
 
 
Configuration>Physical Ports>Flows>General Params>SFP/Port 1>LBM 
Reflector 
 
 
 
 
 
Admin Status 
 
Disable 
 
 
 
0 
1 
2 
3 
4 
5 
6 
7 
 
 
MD Level: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Apply 
 
 
LBM Reflector – SFP/Port 1 (Disabled) 
3. Set Admin status according to whether you want to enable or disable the LBM reflector: 
 
If you enable the LBM reflector, all MD levels are automatically selected. You can select and 
deselect MD levels as needed, by clicking the corresponding levels. 
 
If you disable the LBM reflector, all MD levels are automatically deselected. 
MiNID 
 
 
 
 
 
Configuration>Physical Ports>Flows>General Params>SFP/Port 1>LBM 
Reflector 
 
 
 
 
 
Admin status 
 
 Enable 
 
 
 
0 
1 
2 
3 
4 
5 
6 
7 
 
 
MD Level: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
LBM Reflector – SFP/Port 1  (Enabled)   
4. Click <Apply> to implement your changes, and then click <Save Configuration>. 
Configuring LBM Reflector Using the CLI 
 To configure LBM reflector parameters: 
1. Navigate to configure flows lbm-reflector sfp/1 or configure flows lbm-reflecto msa/2, 
according to whether you want to configure the parameters for SFP/port 1 or MSA/ port 2. 
8. Traffic Processing 
The config>flows>lbm-reflector(sfp/1)# or config>flows>lbm-reflector(msa/2)# prompt is 
displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying MD level for which 
to send LBR in response to 
LBM received with the 
specified MD level  
md-level 
<md-level> 
Enter no md-level <md-level> in order to 
stop replying to LBMs received with 
the specified MD level 
MD level range: 0–7 
To specify multiple MD levels, use the md-level 
command for each MD level 
Administratively enabling 
LBM reflector 
no shutdown 
Enter shutdown to disable the LBM reflector. When you 
disable, all MDs are deselected (same as typing 
no md-level <md-level> for all MD 
levels). 
Note: At least one MD level must be selected via 
command md-level before you can enable the LBM 
reflector. 
Example 
 To configure MiNID to answer LBMs with MD level 2, 4, or 7, received from SFP/port 1: 
exit all  
configure flows lbm-reflector sfp/1 
  shutdown 
  md-level 2 
  md-level 4 
  md-level 7 
  no shutdown 
 
Configuring L2CP/L2PT 
You can configure the following: 
• 
MAC address change for packets classified to L2PT protocols (see Configuring L2PT Protocol 
MAC Change Using the Web Interface and Configuring L2PT Protocol MAC Change Using the 
CLI) 
8. Traffic Processing 
• 
L2CP protocol classification (see Configuring L2CP Protocol Classification Using the Web 
Interface and Configuring L2CP Protocol Classification Using the CLI), based on the destination 
MAC address 01-80-C2-00-00-XX, where XX is 00–2F (excluding values used in Flow General 
Parameter Defaults table) 
• 
L2CP/L2PT profiles (see Configuring L2CP/L2PT Profiles Using the Web Interface and 
Configuring L2CP/L2PT Profiles Using the CLI). Any configured L2CP protocol classifications or 
L2PT MAC address changes are added to existing profiles, and appear in the list of protocols 
when configuring profiles. 
Configuring L2PT Protocol MAC Change Using the Web Interface 
 To configure MAC address change: 
1. In the web interface, go to Configuration > Physical Port > Flows Classification > General 
Params>L2CP\L2PT > L2PT. 
8. Traffic Processing 
 
 
MiNID 
 
  
 
 
 
 Configuration>Physical Ports>Flows>General Params>L2PT 
  
 
 
 
 Protocol 
Name 
 
MAC Change 
 
 STP 
 
00-00-00-00-00-00 
Mac Change 
 OAM 
 
00-00-00-00-00-00 
Mac Change 
 PAgP 
 
00-00-AA-CC-00-BB Mac Change 
 LLDP 
 
00-00-00-00-00-00 
Mac Change 
 CDP 
 
00-00-00-00-00-00 
Mac Change 
 VTP 
 
00-00-00-00-00-00 
Mac Change 
 UDLD 
 
00-00-00-00-00-00 
Mac Change 
 DTP 
 
00-DD-00-02-00-04 
Mac Change 
 PVSTP 
 
00-00-00-00-00-00 
Mac Change 
 LACP 
 
00-00-00-00-00-00 
Mac Change 
 LAMP 
 
00-00-00-00-00-00 
Mac Change 
 ESMC 
 
00-00-00-00-00-00 
Mac Change 
 PTP-Peer-
Delay 
 
00-00-00-00-00-00 
Mac Change 
  
 
 
 
  
 
 
 
L2PT Protocol MAC Changes 
Note 
The value 00-00-00-00-00-00 in the MAC Change field indicates that no MAC 
change is done. 
2. To configure a change of destination MAC address for a particular protocol, click <Mac Change> 
in the corresponding entry. 
8. Traffic Processing 
MiNID 
 
 
 
 
 
Configuration>Physical Ports>Flows>General>L2PT>Mac Change 
 
 
 
 
 
Mac Change 
 
00-00-00-00-00-00 
 
 
 
 
MAC Change 
3. In the MAC Change field, enter the MAC address to which the destination MAC address should 
be changed, and then click <Apply> to apply the change, then click <Save Configuration>. 
Configuring L2PT Protocol MAC Change Using the CLI 
 To configure MAC address change: 
1. Navigate to the configure flows context, and enter: 
l2cp-protocol {stp | oam | lldp | pagp | udld | cdp | vtp | dtp | pvstp} mac-change <mac-addr> 
where <mac-addr > specifies the MAC address to which the destination MAC address should be 
changed for the particular protocol. 
For example, to specify changing MAC address to 00-00-AA-CC-00-BB for LLDP protocol: 
MiNID>config>flows# l2cp-protocol lldp mac-change 00-00-AA-CC-00-BB 
2. You can display the configured L2PT protocol MAC changes by typing info, and searching the 
output for lines beginning with l2cp-protocol: 
MiNID>config>flows# info 
l2cp-protocol stp mac-change 00-00-00-00-00-00 
l2cp-protocol oam mac-change 00-00-00-00-00-00 
l2cp-protocol pagp mac-change 00-00-00-00-00-00 
l2cp-protocol lldp mac-change 00-00-AA-CC-00-BB 
l2cp-protocol cdp mac-change 00-00-00-00-00-00 
l2cp-protocol vtp mac-change 00-00-00-00-00-00 
l2cp-protocol udld mac-change 00-00-00-00-00-00 
l2cp-protocol dtp mac-change 00-DD-00-02-00-04 
l2cp-protocol pvstp mac-change 00-00-00-00-00-00 
8. Traffic Processing 
Configuring L2CP Protocol Classification Using the Web Interface 
 To configure L2CP protocol classification: 
1. In the web interface, go to Configuration > Physical Port > Flows Classification > General 
Params>L2CP\L2PT > L2CP. 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>General>L2CP 
  
 
 
 Last MAC Byte 
(Hex.) 
 
 
  
 
 
 01-80-C2-00-00-01 
Remove 
 
 01-80-C2-00-00-0F 
Remove 
 
  
 
 
L2CP Protocol Last MAC Byte 
Note 
A list of configured L2CP protocol classifications, if any exist, is displayed on 
the screen. 
2. Enter the value for the last byte (e.g. to classify packets with destination MAC address 
01-80-C2-00-00-07, enter 07), and then click <Apply> to apply the change, then click 
<Save Configuration>. 
Configuring L2CP Protocol Classification Using the CLI 
 To configure L2CP protocol classification: 
1. Navigate to the configure flows context, and enter: 
l2cp-mac <last-mac-byte> 
where <last-mac-byte> is a value from 0x00–0x2F that specifies the last byte of the MAC address 
01-80-C2-00-00-XX. You cannot use values that are already used in Flow General Parameter 
Defaults table or have already been used to configure an L2CP profile classification. 
For example, to specify classifying packets with destination MAC address 01-80-C2-00-00-0F: 
MiNID>config>flows# l2cp-mac 0x0f 
8. Traffic Processing 
2. You can display the configured L2CP classifications by typing info, and searching the output for 
lines beginning with l2cp-mac: 
MiNID>config>flows# info 
l2cp-mac 0x01 
l2cp-mac 0x0f 
Configuring L2CP/L2PT Profiles Using the Web Interface 
 To create a new L2CP/L2PT profile: 
1. In the web interface, go to Configuration > Physical Port > Flows Classification > General 
Params>L2CP\L2PT > Profiles. 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>L2CP Profiles 
  
 
 
 New Profile Name 
 
rl2cp 
  
 
 
 Profile Name 
 
 
 kl2cp 
Remove 
 
 ml2cp 
Remove 
 
  
 
 
L2CP Profiles 
2. Enter the name of the profile in New Profile Name, and then click <Apply>, to create the profile 
and add it to the list of profiles, and then click <Save Configuration>. 
 To configure an existing L2CP/L2PT profile: 
1. In the web interface, go to Configuration > Physical Port > Flows Classification > General 
Params>L2CP\L2PT > Profiles (see the figure above). 
2. Click the name of the profile that you want to configure. 
The profile screen displays an entry for each L2PT protocol specified in Flow General Parameter 
Defaults table, as well as entry for each configured L2PT protocol MAC change and each 
configured L2CP protocol classification.  
8. Traffic Processing 
 
MiNID 
 
  
 
 
 Configuration>Physical Ports>Flows>L2CP Profile>Cfg Profile 
  
 
 
 Profile Name 
 
 
 STP 
 
Tunnel 
 OAM 
 
Peer 
 PAgP 
 
Tunnel 
 LLDP 
 
Tunnel 
 CDP 
 
Tunnel 
 VTP 
 
Tunnel 
 UDLD 
 
Tunnel 
 DTP 
 
Tunnel 
 PVSTP 
 
Pass-Through 
 LACP 
 
Tunnel 
 LAMP 
 
Tunnel 
 ESMC 
 
Tunnel 
 PTP-Peer-Delay 
 
Tunnel 
 PagpL2PT 
 
Tunnel 
  
 
 
L2CP Profile 
3. Configure the protocol actions (Discard, Pass-Through, Tunnel, or Peer for OAM protocol), and 
click <Apply> to apply your changes, then click <Save Configuration>. 
Configuring L2CP/L2PT Profiles Using the CLI 
 To add or configure an L2CP/L2PT profile: 
1. Navigate to configure flows l2cp-profile <profile-name>, where <profile-name> is the name of 
the profile. 
The config>flows>profile (<profile-name>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
8. Traffic Processing 
Task 
Command 
Comments 
Specifying the action for 
L2CP protocol 
mac <last-mac-byte> {tunnel | 
pass-through | peer | discard} 
<last-mac-byte> is a value from 
0x00–0x2F that specifies the last 
byte of the MAC address 
01-80-C2-00-00-XX. You cannot use 
values that are already used in Flow 
General Parameter Defaults table or 
have already been used to configure 
an L2CP profile classification 
tunnel – Frames are classified to flow 
and handled according to flow 
pass-through –Frames are 
transmitted unchanged to egress 
port 
peer – Frames are delivered to host 
treatment (OAM only) 
discard –Frames are dropped 
Specifying the action for 
L2PT protocol 
protocol {stp | oam | lldp | pagp | udld | 
cdp | vtp | dtp | pvstp |lacp | lamp | 
esmc | ptp-peer-delay} [l2pt] {tunnel | 
pass-through | peer | discard} 
 
See above for an explanation of the 
actions 
 
Examples 
Loopback in Port Mode 
The following example assumes an initial connectivity testing phase, during which all traffic should be 
looped back. To achieve this, MiNID is configured for port mode on each port, with a loopback action 
with source-destination address swap. 
configure 
flows 
classification mode port sfp/1 
classification mode port msa/2 
port-mode-action ingress-port sfp/1 action loop-mac-ip-swap 
port-mode-action ingress-port msa/2 action loop-mac-ip-swap 
8. Traffic Processing 
Filtering Traffic by VID and Applying an S-Tag 
In the following example, only customer network traffic with VIDs in the 100-200 range are to be 
accepted by the provider network, and an S-tag should be applied with VID 1000 and the same P-bit as 
in the C-tag. In the opposite direction, only provider traffic with VID 1000 should be passed through to 
the customer, with the S-tag removed. 
configure 
flows 
classification mode vlan-pbits-range sfp/1 
flow cust 
classifier match vlan-min 100 pbit-min 0 vlan-max 200 pbit-max 7 
copies P-bit from C-tag 
flow-action ingress-port sfp/1 action push-vlan vlan-id 1000 priority inner-vlan-copy 
tag-ether-type 0x8100 drop-eligible no 
no shutdown 
exit 
 
flow net 
classifier match vlan-min 1000 pbit-min 0 vlan-max 1000 pbit-max 7 
flow-action ingress-port sfp action pop-vlan 
no shutdown 
exit 
fallback-action ingress-port sfp/1 action drop 
fallback-action ingress-port msa/2 action drop 
Tpid-outer-vlan 0x88a8 ingress-port sfp/1  
Layer-2 Loopback 
In the following example, there is a testing device on each side of MiNID, and traffic should be looped 
back only when one is communicating with the other, in the single flow that is configured for each 
direction. The loopback should include address swap. 
The address of the testing device on the customer side is: 12-34-56-78-90-ab. 
The address of the testing device on the provider side is: cd-ef-12-34-56-78 
configure 
flows 
in-service-mac src-addr 1 12-34-56-78-90-ab 
in-service-mac dst-addr 1 cd-ef-12-34-56-78 
in-service-mac src-addr 2 cd-ef-12-34-56-78 
in-service-mac dst-addr 2 12-34-56-78-90-ab 
flow cust-traf 
in-service-loops 
in-serv-mode src-dst 
in-serv-src-mac 1  
in-serv-dst-mac 1  
in-serv-action loop-mac-ip-swap 
exit 
exit 
8. Traffic Processing 
flow net-traf 
in-service-loops 
in-serv-mode src-dst 
in-serv-src-mac 2  
in-serv-dst-mac 2  
in-serv-action loop-mac-ip-swap 
exit all 
Configuration Errors 
The following messages may be generated by MiNID when a configuration error is detected. 
Flow Configuration Errors 
Message 
Cause 
Corrective Action 
A Parameter Is Missing 
You entered a command in 
invalid syntax 
Try again with valid syntax 
P-Bit Value Is Out Of Range (0-7) 
You tried to define a flow 
classification with an 
out-of-range P-bit 
Try again with valid P-bit values 
DSCP Value Is Out Of Range (0-63) 
You tried to define a flow 
classification with an 
out-of-range DSCP value 
Try again with a valid DSCP value 
Vlan Id Is Out Of Range (0-4095) 
You tried to define a flow 
classification with an 
out-of-range VID 
Try again with valid VIDs 
Min Vlan Id Is Bigger Then Max Vlan 
Id 
In VID+P-bit classification mode 
you tried to define a flow 
classification with a vlan-min 
greater than the vlan-max 
Try again with valid values 
Vlan-Id\Pbits Can Not Be Overlapped 
In VID+P-bit classification 
mode, you tried to define a 
flow classification with values 
already defined for another 
flow 
Design your flows differently 
MAC Address Format Is Invalid 
You entered a command with a 
MAC address parameter in an 
invalid format 
Try again with format 
XX-XX-XX-XX-XX-XX 
(each XX a valid hexadecimal 
number) 
8. Traffic Processing 
Message 
Cause 
Corrective Action 
The Requested Flow Classification 
Already Exist 
You tried to define a flow 
classification with a value for 
which a flow already exists 
Delete or reconfigure the other flow 
The Requested Flow Name Already 
Exist 
In the web interface, you tried 
to Add a flow with a name 
already used for another flow 
Use a different name 
The Requested Flow Does Not Exist 
 
 
Flow Name Can't Be Empty 
In the web interface, you tried 
to save a new flow without a 
name 
Enter a name and try again 
Flow Name Too Long, Max Name 
Length Is 10 Chars 
You tried to create a flow with a 
name longer than ten 
characters 
Shorten the name 
Can't Enable a Flow Without a 
Classification Value 
You tried to Enable (or, in CLI: 
no shutdown) a flow without a 
classification criterion 
Configure the classification criterion 
and try again 
Can't Enable a Flow Without an 
Action 
You tried to Enable (or, in CLI: 
no shutdown) a flow without a 
flow action 
Configure the flow action and try 
again 
Can't Change Flow Configuration 
While Flow Is Enable 
In CLI, you tried to reconfigure 
an enabled flow 
Disable the flow and try again 
Can’t Add A New Flow, Resources 
Unavailable 
You tried to create a new flow, 
but there are already the 
maximum number of flows 
configured (including disabled)  
Delete a flow and try again 
Viewing Flow Summary 
In the web interface, you can view a list of existing flows in Configuration > Physical Port > Flows 
Classification > Config Flow. From the list, you can Enable / Disable or Delete each flow. Clicking a 
flow’s name displays its details, and if the flow is disabled you can then edit the details. You can also 
view the list and details (but not make any changes) in Monitoring > Physical Port > Flows Classification 
> Flows Traffic. 
8. Traffic Processing 
In the CLI, you can view flow details with the info command, for an individual flow in its context or for all 
flows in the config>flows context. You can also view a convenient (but less detailed) summary of the 
classification mode and configured flows by going to the config>flows context and entering: 
show summary 
For example: 
MiNID>config>flows# show summary 
Classification Mode:    VID+Pbits Range 
 
Name:           cust 
Status:         Enable 
Action:         push-vlan 
Ingress-Port:   SFP/1 
Match Value:    VID Range [100-200]+ P-bit [0-7] 
 
Name:           net 
Status:         Enable 
Action:         pop-vlan 
Ingress-Port:   MSA/2 
Match Value:    VID Range [1000-1000]+ P-bit [0-7] 
 
MiNID>config>flows# 
Viewing Flow Statistics 
You can view traffic handling statistics for each flow and for unclassified (fallback) traffic. The statistics 
for each of these can be manually cleared, and changing the classification mode clears all of them. 
Viewing Statistics for Unclassified (Fallback) Traffic 
Statistics include the number of handled frames and the number of handled bytes, for both ports. 
 To view or clear statistics for unclassified (fallback) traffic: 
Do one of the following: 
• 
In the CLI configure flows context: 
 
View the statistics by entering: 
show unclassified-statistics 
For example: 
MiNID# configure flows 
MiNID>config>flows# show unclassified-statistics 
Unclassified Port 1: 
8. Traffic Processing 
Total Unclassified Frames:       18678103 
Total Unclassified Bytes:        1771890591 
Total Unclassified In-Service MAC Frames:        0 
Total Unclassified In-Service MAC Bytes:         0 
Total Unclassified In-Service L3\L4 Frames:      0 
Total Unclassified Matched In-Service L3\L4 Bytes:       0 
Total Unclassified L2CP Frames:  341207 
Total Unclassified L2CP Bytes:   21837248 
Unclassified Port 2: 
Total Unclassified Frames:       18678103  
Total Unclassified Bytes:        1771890591 
Total Unclassified In-Service MAC Frames:        0  
Total Unclassified In-Service MAC Bytes:         0  
Total Unclassified In-Service L3\L4 Frames:      0 
Total Unclassified Matched In-Service L3\L4 Bytes:       0 
Total Unclassified L2CP Frames:  341207 
Total Unclassified L2CP Bytes:   21837248 
 
Clear the statistics by entering: 
clear-statistics 
• 
In the web interface, go to Monitoring > Physical Port > Classification > Unclassified 
traffic>Unclassified Port <Name>. 
8. Traffic Processing 
MiNID 
  
 
 
 Monitoring>Physical Ports>Classification>Unclassified Port 1 
Statistics 
  
 
 
 Total Matched Frames 
 
18682494 
 Total Matched Bytes 
 
1772301596 
 Total Matched In-Service MAC Frames 
 
0 
 Total Matched In-Service MAC Bytes 
 
0 
 Total Matched In-Service L3\L4 Frames  
0 
 Total Matched In-Service L3\L4 Bytes 
 
0 
 Total Matched L2CP Frames 
 
341286 
 Total Matched L2CP Bytes 
 
21842304 
  
 
 
  
 
 
 
 
  
 
Green 
Bytes 
Yellow 
Bytes 
Red Bytes 
 Total Matched Cos 0 
 
0 
0 
0 
 Total Matched Cos 1 
 
0 
0 
0 
 Total Matched Cos 2 
 
0 
0 
0 
 Total Matched Cos 3 
 
0 
0 
0 
 Total Matched Cos 4 
 
0 
0 
0 
 Total Matched Cos 5 
 
0 
0 
0 
 Total Matched Cos 6 
 
0 
0 
0 
 Total Matched Cos 7 
 
0 
0 
0 
 Total Matched Green 
Bytes 
 
0 
0 
0 
 Total Matched Yellow 
Bytes 
 
0 
0 
0 
 Total Matched Red 
Bytes 
 
0 
0 
0 
  
  
 
 
Statistics for Unclassified Traffic 
You can click Back and clear these statistics by clicking Clear Statistics. 
Note 
The above statistics are shared between both ports. 
8. Traffic Processing 
Viewing Statistics for a Specified Flow 
Statistics include the number of handled frames and the number of handled bytes. Layer-2 (in-service) 
and layer-3/4 loopback statistics are also displayed. The layer-3/4 statistics include any TWAMP looped 
packets and bytes if the flow is bound to a TWAMP responder. 
 To view or clear statistics for a specified flow: 
Do one of the following: 
• 
In the flow’s CLI config>flows>flow(name) context: 
 
View the statistics by entering: 
show statistics 
For example: 
MiNID>config>flows# flow net 
MiNID>config>flows>flow(net)# show statistics 
Total Matched Frames                 :       17962 
Total Matched Bytes                  :       1235401 
Total Matched In-Service MAC Frames  :       0 
Total Matched In-Service MAC Bytes   :       0 
Total Matched In-Service L3\L4 Frames:       0 
Total Matched In-Service L3\L4 Bytes :       0 
Total Matched L2CP Frames            :       0 
Total Matched L2CP Bytes             :       0 
MiNID>config>flows>flow(net)# 
 
To view statistics of all flows, use the show summary command. 
 
Clear the statistics by entering: 
clear-statistics 
• 
In the web interface, go to Monitoring > Physical Port > Classification > Port name, and in the 
relevant row, click Statistics: 
MiNID 
  
 
 
 
 
 Monitoring>Physical Ports>Classification>Flow Traffic port name 
  
 
 
 
 
  
Flow Name 
Status 
 
 
  
cust 
Disable 
Statistics 
 
  
net 
Enable 
Statistics 
 
  
 
 
 
 
Statistics for Flow Traffic 
8. Traffic Processing 
The statistics are displayed: 
MiNID 
  
 
 
 Monitoring>Physical Ports>Classification>Statistics  
  
 
 
 Total Matched Frames 
 
0 
 Total Matched Bytes 
 
0 
 Total Matched In-Service MAC Frames 
 
0 
 Total Matched In-Service MAC Bytes 
 
0 
 Total Matched In-Service L3\L4 Frames 
 
0 
 Total Matched In-Service L3\L4 Bytes 
 
0 
 Total Matched L2CP Frames 
 
0 
 Total Matched L2CP Bytes 
 
0 
  
 
 
 Clear Statistics 
 
 
  
 
 
Displayed Flow Statistics 
You can Clear these statistics. 
Viewing Statistics for a Flow with Envelope Policer 
 To view or clear statistics for a specified flow: 
Do one of the following: 
• 
In the flow’s CLI config>flows>flow(name) context: 
 
View the statistics by entering: 
show statistics 
For example: 
MiNID>config>flows>flow(Silver)# show statistics 
Total Matched Frames                    :       0 
Total Matched Bytes                     :       0 
Total Matched In-Service MAC Frames     :       0 
Total Matched In-Service MAC Bytes      :       0 
Total Matched In-Service L3\L4 Frames   :       0 
Total Matched In-Service L3\L4 Bytes    :       0 
Total Matched L2CP Frames               :       0 
Total Matched L2CP Bytes                :       0 
Cos Number :    4 
8. Traffic Processing 
--------------------------------------------- 
Total Matched Green Bytes               :       0 
Total Matched Yellow Bytes              :       0 
Total Matched Red Bytes                 :       0 
 
 
Cos Number :    5 
--------------------------------------------- 
Total Matched Green Bytes               :       0 
Total Matched Yellow Bytes              :       0 
Total Matched Red Bytes                 :       0 
 
 
Cos Number :    7 
--------------------------------------------- 
Total Matched Green Bytes               :       0 
Total Matched Yellow Bytes              :       0 
Total Matched Red Bytes                 :       0 
 
To view statistics of all flows, use the show summary command. 
 
Clear the statistics by entering: 
clear-statistics 
• 
In the web interface, go to Monitoring > Physical Port >  Classification > Flows Traffic port 
name, and in the relevant row, click Statistics: 
8. Traffic Processing 
The statistics are displayed: 
MiNID 
  
 
 
 Monitoring>Physical Port>Classification>Statistics  
  
 
 
 Total Matched Frames 
 
0 
 Total Matched Bytes 
 
0 
 Total Matched In-Service MAC Frames 
 
0 
 Total Matched In-Service MAC Bytes 
 
0 
 Total Matched In-Service L3\L4 Frames 
 
0 
 Total Matched In-Service L3\L4 Bytes 
 
0 
 Total Matched L2CP Frames 
 
0 
 Total Matched L2CP Bytes 
 
0 
  
 
 
 
  
Green Bytes Yellow Bytes 
Red Bytes 
 Total Matched Cos 0 
0 
0 
0 
 Total Matched Cos 1 
0 
0 
0 
 Total Matched Cos 2 
0 
0 
0 
 Total Matched Cos 3 
0 
0 
0 
 Total Matched Cos 4 
0 
0 
0 
 Total Matched Cos 5 
0 
0 
0 
 Total Matched Cos 6 
0 
0 
0 
  
 
 
0 
 Clear Statistics 
 
 
  
 
 
Displayed Statistics for Envelope Policer Flow 
You can Clear these statistics. 
Testing Flow Configuration 
 To test flow configuration: 
1. Send various types of traffic via MiNID, according to each flow, in both directions. 
2. Check that the traffic arrives properly at its destination. 

## 8.2 Quality of Service (QoS)  *(p.205)*

8. Traffic Processing 
3. View MiNID statistics (see Viewing Flow Statistics) and check that no traffic has been lost. 
8.2 Quality of Service (QoS) 
The MiNID Quality of Service (QoS) parameters include the following profiles: 
• 
CoS map profiles 
• 
Policer profiles 
• 
Envelope profiles 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
MEF 10.3 
Benefits 
• 
QoS allows you to optimize bandwidth, avoiding the need to allocate excessive bandwidth to 
facilitate the necessary bandwidth for traffic at different requirements of speed and quality. 
CoS Map Profiles 
Class of Service (CoS) mapping profiles map the following user priorities to internal CoS values:  
• 
p-bit — when ingress traffic is prioritized according to 802.1p requirements 
Factory Defaults 
By default, there are no CoS mapping profiles. When you create a CoS mapping profile, it is configured 
as follows: 
8. Traffic Processing 
• 
Classification p-bit 
• 
Mappings: 
 
Map 0 to CoS 7 
 
Map 1 to CoS 6 
 
Map 2 to CoS 5 
 
Map 3 to CoS 4 
 
Map 4 to CoS 3 
 
Map 5 to CoS 2 
 
Map 6 to CoS 1 
 
Map 7 to CoS 0 
Configuring CoS Mapping Profiles 
 To define a CoS profile: 
1. Navigate to the qos context (config>qos). 
2. Define a CoS profile and assign a classification to it: 
cos-map-profile <cos-mapping-profile-name> 
3. Map the user priority to a CoS value (user priority values 0–7 for p-bit CoS values 0–7): 
map <0-7> to <0-7> 
Examples 
 To create and configure a CoS mapping profile: 
• 
Profile name: my-p-bit 
• 
Map priority 6–7 to CoS 0 
• 
Map priority 3–5 to CoS 1 
• 
Map priority 0–2 to CoS 2 
exit all  
configure qos cos-map-profile my-p-bit  
  map 6..7 to-cos 0 
  map 3..5 to-cos 1 
  map 0..2 to-cos 2 
   exit all 
8. Traffic Processing 
 To create and configure a CoS mapping profile for a multi-CoS flow: 
• 
Profile name: p-bit-multi 
• 
Map priority 0 to CoS 7 
• 
Map priority 7 to CoS 0 
• 
Map untagged traffic to CoS 0 
exit all  
configure qos cos-map-profile p-bit-multi classification p-bit 
untagged-map to-cos 0 
   exit all 
Envelope Bandwidth Profiles 
An envelope profile as defined in MEF 10.3 contains a set of bandwidth profiles, each of which has been 
assigned a unique rank from 1 (lowest) to 4 (highest). Excess bandwidth from a higher rank can overflow 
to a lower rank to be shared, either to the committed or to the excess bucket. In MiNID, each profile 
corresponds to a separate CoS. The figure below illustrates an envelope profile with three CoSs. The 
coupling flags specify the path of overflow bandwidth. For the CoS coupling flags (CFi), 0=committed 
token bucket of the next lower rank, and 1=excess token bucket of the same rank. For coupling flag 0, 
0=discard, and 1=excess token bucket of the highest rank.  
CIR3
CBS3
EIR3
1
0
CIR2
CF3
EIR2
1
0
CBS2
CIR2
EIR1
1
0
CBS1
CF2
CF1
1
0 CF0
EBS3
EBS2
EBS1
Rank #3
Rank #2
Rank #1
Envelope
 
MEF 10.3 Bandwidth Profiles 
8. Traffic Processing 
When the envelope profile is assigned to a multi-CoS flow, it enables the flow to share excess 
bandwidth. The bandwidth sharing can be overflowed to the excess bucket or independent from the 
excess bucket.  
CIR3
CBS3
EIR3
1
CIR2
CF3
EIR2
1
CBS2
CIR2
EIR1
1
CBS1
CF2
CF1
EBS3
EBS2
EBS1
 
Sharing Excess Bandwidth 
CIRenv
CBS3
CF3
CBS2
CBS1
CF2
CF1
EBS3
EBS2
EBS1
EIRenv
0
0
0
 
Uncoupled from EIR/EBS 
8. Traffic Processing 
Configuring Envelope Profiles Using the Web Interface 
 To configure an envelope profile: 
1. Navigate to Configuration > QoS > Envelope Profile. 
1. MiNID 
2.  
 
 
 
 
 
Configuration>QoS> Envelope Profiles 
 
 
 
 
New Profile Name 
 
 
 
 
 
Apply 
 
 
 
 
 
Profile Name 
 
 
 
 
 
 
 
2. In the New Profile Name field, type the envelope profile name. 
3. Click <Apply>. 
The new envelope profile is added to the list. 
MiNID 
 
 
 
 
 
Configuration>QoS> Envelope Profile 
 
 
 
 
New Profile Name 
 
 
 
 
 
Apply 
 
 
 
 
 
Profile Name 
 
 
1 
Remove 
 
 
 
 
4. Click the desired profile to configure profile parameters. 
8. Traffic Processing 
MiNID 
 
 
 
 
 
Configuration>QoS> Envelope Profile>Cfg Profile 1 
 
 
 
 
CF Policy 
sharing-excess-bw 
 
Color Aware 
Disable 
 
Compensation 
0 
 
Cos 
0 
 
CIR 
0 
 
CIR Max 
1000000 
 
CBS 
0 
 
EIR 
1000000 
 
 
EIR Max 
1000000 
 
EBS 
32767 
 
 
Coupling Flag 
 
 
 
 
 
 
 
 
Apply 
 
 
5. Configure the profile: 
 
CIR: Defines the Committed Information Rate (CIR) for the current profile. The CIR specifies 
a bandwidth with committed service guarantee (“green bucket” rate). 
 
CBS: Defines the Committed Burst Size (CBS) for the current profile. The CBS specifies the 
maximum guaranteed burst size (“green bucket” size). 
 
EIR: Defines the Excess Information Rate (EIR). The EIR specifies an extra bandwidth with no 
service guarantee (“yellow bucket” rate). 
 
EBS: Defines the Excess Burst Size (EBS). The EBS specifies the extra burst with no service 
guarantee (“yellow bucket” size). 
 
Compensation: You can specify the amount of bytes that the policer can compensate for the 
layer 1 overhead (preamble and IFG) and the overhead for the added VLAN header in case 
of stacking. 
 
Color Aware: The policer profile can be specified as color aware. 
6. Click <Apply>. 
Configuring Envelope Profiles Using the CLI 
This section explains how to configure envelope profiles, to apply to multi-Cos flows per MEF 10.3.  
8. Traffic Processing 
Adding Envelope Policer Profiles 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type: 
envelope-profile <envelope-profile-name> 
An envelope profile with the specified name is created and the following prompt is displayed: 
config>qos>envelope-profile(<envelope-profile-name>)$  
The new envelope profile parameters are configured by default.  
3. Configure the envelope profile as described in Configuring Envelope Profile Parameters. 
Configuring Envelope Profile Parameters 
1. Navigate to configure qos envelope-profile <envelope-profile-name> to select the envelope 
profile to configure. 
The config>qos>policer-profile(<envelope-profile-name>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining policy for 
excess bandwidth 
sharing  
cf-policy {sharing-excess-bw 
| uncoupled-bw-sharing} 
sharing-excess-bw –Excess bandwidth is shared to 
excess token bucket (see Sharing Excess 
Bandwidth figure). Selecting this parameter 
automatically sets coupling-flag-0 to 0, and sets 
each CoS coupling flag to 1.  
uncoupled-bw-sharing – Excess bandwidth is 
shared independently from EIR/EBS (see 
Uncoupled from EIR/EBS figure). Selecting this 
parameter automatically sets coupling-flag-0 to 0, 
and sets each CoS coupling flag to 0. 
If you enter no cf-policy, then coupling-flag-0 and 
each CoS coupling flag determine the bandwidth 
sharing. 
Specifying if the 
envelope profile is 
color aware 
color-aware 
 
Specifying the 
compensation (bytes) 
compensation <value> 
<value> is –(–32)-31 
8. Traffic Processing 
Task 
Command 
Comments 
Specifying the CIR 
(Kbps), CBS (bytes), 
EIR (Kbps), and EBS 
(bytes) bandwidth 
limits, for a particular 
CoS 
cos <value> bandwidth 
[cir <cir-kbit-sec>] 
[cir-max <cir-max-kbit-sec>] 
[cbs <cbs-bytes>] 
[eir <eir-kbit-sec>] 
[eir-max <eir-max-kbit-sec>] 
[ebs <ebs-bytes>] 
[coupling-flag <coupling-fla
g>] 
Range for cos value is 0–7; you can define up to 
four or eight cos values in an envelope profile. 
Range for <cir-kbit-sec>, 
<cir-max-kbit-sec>, <eir-kbit-sec>, 
and <eir-max-kbit-sec>: 
0–1000000 (0–1 Gbps) 
Range for <cbs-bytes>, <ebs-bytes>:  
0–1000000 (0–1Mbytes) 
<cir-max-kbit-sec> must be greater 
than or equal to <cir-kbit-sec>. 
<eir-max-kbit-sec> must be greater 
than or equal to <eir-kbit-sec>. 
coupling-flag controls the path of 
overflow tokens: 0=overflow to 
committed token bucket, 1= 
overflow to excess token bucket. 
Specifying path of 
overflow bandwidth 
(see CF0 in MEF 10.3 
Bandwidth Profiles 
figure) 
coupling-flag-0 <value> 
<value> is 0–1: 
0=discard, and 1=excess token bucket of the 
highest rank 
Policer Profiles 
This section explains how to configure non-envelope policer profiles to limit traffic. The profiles can be 
applied to flows. 
Configuring Policer Profiles Using the Web Interface 
 To configure a policer profile: 
1. Navigate to Configuration > Qos > Policer Profile. 
8. Traffic Processing 
MiNID 
 
 
 
 
 
Configuration>QoS> Policer Profiles 
 
 
 
 
New Profile Name 
 
 
 
 
 
Apply 
 
 
 
 
 
Profile Name 
 
 
 
 
 
 
 
2. In the New Profile Name field, type the profile name. 
3. Click <Apply>. 
The new policer profile is added to the list. 
MiNID 
 
 
 
 
 
Configuration>QoS> Policer Profiles 
 
 
 
 
New Profile Name 
 
 
 
 
 
Apply 
 
 
 
 
 
Profile Name 
 
 
1 
Remove 
 
 
 
 
4. Click the desired profile to configure profile parameters. 
8. Traffic Processing 
MiNID 
 
 
 
 
 
Configuration>QoS> Policer Profile>Cfg Profile 
 
 
 
 
CIR [Kbps] 
0 
 
CBS [Bytes] 
0 
 
 
EIR [Kbps] 
1000000 
 
EBS [Bytes] 
32767 
 
 
Coupling Flag 
Disable 
 
 
Color Aware 
Disable 
 
Compensation 
0 
 
 
 
 
 
Apply 
 
 
5. Use the table below to fill in and select the desired parameters. 
6. Click <Apply>. 
Configuring Policer Profiles Using the CLI 
 To add a policer profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type: 
policer-profile <policer-profile-name> 
A policer profile with the specified name is created and the following prompt is displayed: 
config>qos>policer-profile(<policer-profile-name>)$  
The new policer profile parameters (except for name) are configured by default as described in 
the table below. 
3. Configure the policer profile as described in Configuring Policer Profile Parameters. 
 To configure policer profile parameters: 
1. Navigate to configure qos policer-profile <policer-profile-name> to select the policer profile to 
configure. 
The config>qos>policer-profile(<policer-profile-name>)# prompt is displayed. 
8. Traffic Processing 
2. Enter all necessary commands according to the tasks listed below. 
Policer Profile Parameters 
Task 
Command 
Comments 
Specifying the CIR (Kbps), 
CBS (bytes), EIR (Kbps), and 
EBS (bytes) bandwidth 
limits  
bandwidth [cir <cir-kbit-sec>] 
[cbs <cbs-bytes>] 
[eir <eir-kbit-sec>] 
[ebs <ebs-bytes>] 
Notes: 
• CIR & EIR allowed values: 
 
0–1000000 
• CBS & EBS allowed values: 
 
0–1000000 
• CIR can be set to zero only if CBS is 
set to zero and vice versa 
• EIR can be set to zero only if EBS is 
set to zero 
• CBS should be greater than the 
maximum frame size 
Specifying if the policer 
profile is color aware 
color-aware 
 
Specifying the 
compensation (bytes) 
compensation <-32–31> 
 
Specifying whether to 
check CIR+EIR when 
determining packet color 
coupling-flag 
Relevant only for color-aware policer 
profile in  
 
Examples 
 To create and configure a policer profile named Policer4: 
• 
CIR = 50,000 Kbps 
• 
CBS = 28,000 bytes  
• 
EIR = 30,000 Kbps 
• 
EBS = 20,000 bytes 
• 
Compensation = 30 
exit all 
configure qos policer-profile Policer4 
  bandwidth cir 50000 cbs 28000 eir 30000 ebs 20000 
  compensation 30 
8. Traffic Processing 
exit all 
 To display the configuration information for policer profile Policer4: 
MiNID# configure qos policer-profile Policer4 
MiNID>config>qos>policer-profile(Policer4)# info 
    bandwidth cir  49984 cbs  28000 eir  29952 ebs  20000 
    compensation  30  
 
 