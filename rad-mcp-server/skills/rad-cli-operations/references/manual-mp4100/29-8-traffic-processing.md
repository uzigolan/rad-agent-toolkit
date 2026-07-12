# 8 Traffic Processing

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 632–776.*


## 8.1 Bridge  *(p.632)*

This chapter explains how to configure network-related features: management bridge and router, flows, 
pseudowire environment and cross-connections. 
8.1 Bridge  
The Megaplex-4 bridge is a VLAN-aware Layer-2 forwarding entity.  
Applicability and Scaling  
11 bridge instances can be created in the device: one bridge for the dual CL.2 modules and one bridge 
for each M-ETH module. 
The maximum number of bridge ports that can be bound to logical MAC ports is 62. 
Standards 
IEEE 802.1D, 802.1Q 
Benefits 
The bridge is used to deliver EPLAN and EVPLAN (any-to-any) services. 
Factory Defaults 
By default, no bridge instances exist in the Megaplex-4 system. 
8. Traffic Processing 
Functional Description 
A bridge is a forwarding entity used by Megaplex-4 for delivering E-LAN services and G.8032 ring 
protection. 11 bridge instances can be defined in Megaplex-4: one bridge for the CL subsystem (always 
bridge 1) and one bridge per M-ETH module.  In total, Megaplex-4 provides up to 170 bridge ports, 
subdivided as follows: 
• 
80 ports on the CL.2 bridge 
• 
9 ports per M-ETH module bridge (8 external + 1 internal) – maximum 90 ports per chassis. 
The bridge operates in VLAN-aware mode (IVL) with ingress filtering. It accepts tagged frames only. To 
be admitted to the bridge, a frame’s VID must be configured as a part of the bridge port VLAN member 
set. Untagged frames must receive a relevant VID at port ingress (tag push) or they will be dropped. 
The Megaplex-4 bridge supports up to 64 broadcast domains (bridge/VLAN) and a MAC table with up to 
16K entries. The MAC table flush is supported per bridge instance. MAC address aging time is configured 
per chassis in the range of 60 to 3000 seconds (Default=300 seconds).  
Megaplex-4 supports RSTP which can be used to prevent loops in Layer 2 networks and provides rapid 
convergence of the spanning tree.  
Bridge Model 
A bridge is defined by a bridge number, bridge ports and a VLAN membership table that specifies which 
bridge ports are members in a certain broadcast domain (VLAN).  
Traffic in and out of a bridge port is configured using flows. This allows editing action at ingress and 
egress bridge ports.  
Bridge port to physical port mapping is always 1:1.  
Deleting Bridge Elements 
Deletion of bridge elements is performed in the following manner: 
• 
All flows on the VLAN must be deleted before a VLAN member can be deleted from a bridge 
port. 
• 
All VLAN members of a bridge port must be deleted before the bridge port can be deleted.  
• 
All bridge ports must be deleted before the bridge can be deleted. 
8. Traffic Processing 
Using the Bridge for Management  
Megaplex-4  management tasks are organized as shown below. The diagram shows the VLAN-aware 
management bridge, the management router 1 and their interconnections with management flows.  
Note 
There are two routers in the Megaplex-4 architecture: Router 1 is used for 
inband management, while Router 2 is used for pseudowire routing. Router 2 
is explained in the Error! Reference source not found. section.  
Router 1 basic functionality is in connecting to control management stations (such as PC) and accessing 
the Common Logic. By default, Megaplex-4 is managed by Router 1, via Layer-3. If you want to manage 
the device via a management VLAN (Layer-2 management), the bridge must be configured. 
 
Bridge#1 Aware
BP#3
1
BP#2
Router
RI#1
RI#2
RI#3
DTS
PPP
DCC
PPP
Host
mng-eth 
cl-a
mng-eth 
cl-b
SVI#1
BP#1
 
Management Connectivity Diagram  
The default management entities are created automatically by the system and are in “no shutdown” 
state by default. These entities include Router 1 interface and SVI port 1 connecting the router interface 
to the bridge. This SVI is not connected to the bridge but represents Ethernet Control ports of both CL.2 
modules. 
The following table summarizes the default configuration file entities and their automatically assigned ID 
numbers, which you can change later, if needed.  
Default Configuration File Entities  
Entity 
Number 
Router 1 interface 
1 
SVI port connecting the router interface to the bridge 
1 
8. Traffic Processing 
Management traffic flowing through Ethernet connections is normally assigned a dedicated VLAN. 
Within the Megaplex-4, inband management traffic can reach the management subsystem on the CL 
modules through Ethernet ports, GFP port or virtually concatenated groups carrying Ethernet traffic.  
Admission to Bridge  
In order for a frame to be admitted to the bridge, its classification must match the flow classification 
configured for the bridge port. 
In VLAN-aware mode, an Egress tagged port must be defined. Additionally, flows with untagged 
classification must have a push editing action. 
In VLAN-unaware mode (M-ETH bridges only), any packet may be admitted according to the configured 
flow classifications. 
Packet Editing on Reverse Flows  
In the case of a bidirectional flow, the editing action can be specified for the flow to the bridge port, but 
not for the reverse direction (while only reverse flows can be configured between bridge ports and 
other ports of Megaplex-4). Megaplex-4 performs editing on the reverse direction according to the flow 
classification and specified editing actions. The following table shows the editing action on the reverse 
flow, as well as the VLAN learned from the flow. 
Packet Editing on Reverse Flows  
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
Any classification 
(including untagged) 
Push X  
p-bit  fixed/copy/profile  
Pop 
X 
Any classification 
(including untagged and 
all) 
Push X  push inner Y 
p-bit and inner p-bit 
fixed/copy/profile 
Pop twice 
X 
8. Traffic Processing 
Classification 
Editing of Flow with Bridge 
Port as Egress Port 
Editing of Reverse 
Directional Flow  
VLAN Value 
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
Swap VLAN  X 
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
Spanning Tree Protocol  
Spanning Tree Protocols (STPs) are Layer-2 loop avoidance techniques used in Ethernet networks. Loops 
are created in bridge-based networks with more than one path between two endpoints, when the 
bridges repeatedly rebroadcast the broadcast/multicast messages, flooding the network. So, STPs are 
used to identify the best path to the destination, and block all other paths. The blocked links are not 
always discarded. They are connected and kept inactive, creating automatic backup links. 
8. Traffic Processing 
The figure below illustrates STP operation. Bridge 3 is connected directly to Bridge 1 and Bridge 2. 
Another physical link connects directly Bridge 1 to Bridge 2. Under normal conditions, there will be 
looping of data, causing broadcast congestion on the network. When an STP is applied, Link A is blocked 
from transmitting any data, but it remains on standby and listens to the network. If Link B or Link C fails, 
Link A is activated, providing link and switch redundancy in the network. 
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
 
STP Operation 
STP Bridge Types 
The root bridge is the central reference bridge in the STP. It serves as a reference for other bridges to 
determine their best cost path. Bridge 3 in the figure above serves as a root in the application. 
The root bridge is elected by selecting the bridge with the lowest bridge ID. It can be done manually, or 
the bridges in the network elect a root bridge themselves automatically. If the root bridge fails, the 
other bridges select a new root device. The other bridges in the network are referred to as designated 
bridges. 
Link Cost 
Every link in the network receives a certain cost. Usually, higher-bandwidth links that are adjacent to the 
root bridge are assigned a lower cost. Lower-bandwidth links that are multiple hops away from the root 
bridge are assigned a higher cost. Once link costs are estimated, STP determines the lowest cost 
connections from each designated bridge to the root bridge to determine the lowest-cost path. It also 
blocks all the other higher cost links to prevent loops in the network.  
Bridge Protocol Data Units 
The bridges use Bridge Protocol Data Units (BPDUs) to exchange information about network topology, 
bridge IDs, link costs etc. BPDUs help establish the best route (least cost path) to the root bridge. 
When there is a change in the network, relevant BPDUs are sent to all the bridges/bridge ports by the 
root bridge. The designated bridges adjust their tables to determine the new routes to the terminals. 
8. Traffic Processing 
Rapid Spanning Tree Protocol 
Rapid Spanning Tree Protocol (RSTP) provides significantly faster spanning tree convergence after a 
topology change, supporting a loop-free Layer-2 forwarding over a mesh/ring physical topology. In RSTP, 
link status of each port are monitored pro-actively (instead of waiting for the BPDU messages) to detect 
changes in network topology. 
RSTP is supported on the following Megaplex-4 ports: 
• 
GbE and Logical MAC ports of CL.2/A modules 
• 
GbE ports of M-ETH modules 
• 
Logical MAC ports of VS modules 
Configuring the Bridge 
Configuring for Traffic 
To configure the bridge for traffic, perform the following steps: 
2. Configure a bridge instance (1–11).   
3. Configure the bridge ports.  
4. Configure VLANs (CL bridge ports only). For E-Tree service in a VLAN, configure VLAN mode to 
E-Tree and configure root. 
5. Configure flows between non-bridge ports and bridge ports (bridge ports are defined as egress 
tagged VLAN members). 
Configuring for Management  
In order to manage the device via the bridge, you need to configure the following: 
1. Configure the router (1) interface for management, bound to SVI. 
2. Configure the flow between the SVI and bridge port. 
3. Configure the flow between a non-bridge port and bridge port. 
8. Traffic Processing 
Configuring the Bridge  
 To configure a bridge: 
1. At the configure prompt, enter bridge followed by bridge number (1–11). 
A bridge instance with the specified number is created and the config>bridge(1)# prompt is 
displayed.  
2. Configure the bridge as illustrated and explained below. 
Note 
Using no before bridge (bridge_number) deletes a bridge instance.  
3. Configure the new bridge port and bind it to the bridge as illustrated and explained in the table 
below.  
Task 
Command 
Comments 
Defining aging time for MAC 
table entries (seconds) 
aging-time <60–3000> 
Default: 300 
Clearing addresses in MAC 
table 
clear-mac-table 
 
Configuring bridge ports (see 
below) 
port <port-number> 
The range is:  
1–80 for CL bridge  
1-9 for M-ETH bridges 
To delete a bridge port, enter 
no port <port-number> 
Enabling Layer 2 bridging 
according to the  VLAN tag 
vlan-aware             
no vlan- aware disables Layer 2 
bridging according to the VLAN tag 
Enabling or disabling filtering 
filtering 
In Megaplex-4, filtering is always 
enabled  
8. Traffic Processing 
Task 
Command 
Comments 
Defining VLANs (see below) 
vlan <vlan-id>  
 
Range is 1–4094 
To delete a VLAN, enter 
no vlan <vlan-id> 
In order to make sure that all 
devices are reached in case of 
traffic load, it is recommended that 
the VLAN intended for 
management (in Bridge 1) is 
mapped to queue 0 (highest 
priority). This mapping is done 
while configuring the egress-port of 
a flow as bridge-port of Bridge 1 
(see Defining Classifier Profiles).  
Configuring spanning tree (see 
below) 
spanning-tree 
Only CL.2/A modules support this  
feature 
If the bridge port is set as a 
member in RSTP, it cannot be a 
member of LAG, Ethernet group or 
ERP at the same time.  
Displaying MAC address table 
for all ports/VLANs or selected 
VLAN/port 
show mac-address-table all 
[vlan <vlan-id > | ports <port-
number > ]  
Up to the first 100 entries are 
displayed on the screen.  
vlan option is used only for aware 
bridge mode.  
The following commands are available in the spanning-tree level, at the config>bridge(1)> spanning-
tree# prompt.  
Task 
Command 
Comments 
Defining the time duration in 
listening and learning states 
that precede the forwarding 
state, in seconds 
forward-time <4-30> 
You cannot assign forward-time 
a value less than max-age/2+1. 
Defining the time interval in 
seconds between BPDU 
transmissions (seconds) 
hello-time <1-10> 
 
Defining the maximum age of 
the configuration BPDU can be 
maintained on a device 
(seconds). 
max-age <6-40> 
You cannot assign max-age a 
value that is less than 2*(hello-
time+1) or more than 
2*(forward-time–1). 
8. Traffic Processing 
Task 
Command 
Comments 
Defining the operation mode 
for spanning-tree 
mode {mstp | rstp} 
 
mstp is not supported. 
 
Assigning the bridge priority 
value 
 
priority <0, 4096, 8192, 12288, 
16384, 20480, 24576, 28672, 
32768, 36864, 40960, 45056, 
49152, 53248, 57344, 61440> 
  
Configuring the maximum 
number of BPDUs transmitted 
tx-hold-count <number> 
The value is 1-10. 
Displaying the spanning-tree 
status 
show status 
 
The following commands are available in the port level, at the config>bridge(1)>port(<port-number>)# 
prompt. 
Task 
Command 
Comments 
Assigning a name to the bridge port 
name <port-name> 
To delete the bridge port name, 
enter no name  
Administratively enabling the bridge 
port 
no shutdown 
To administratively disable the 
bridge port, enter shutdown  
Binding the bridge port to an M-ETH 
Ethernet port 
bind ethernet <slot/port>  
 
M-ETH external bridge ports only 
To remove the binding, enter no 
bind 
Assigning a default VLAN ID to an 
access port (for untagged or  priority-
tagged frames) to designate the virtual 
LAN segment to which this port is 
connected  
pvid <vlan-id> 
 
Not relevant for Bridge 1 ports 
Configuring spanning tree for port (see 
below)  
spanning-tree 
 
The following commands are available in the vlan level, at the config>bridge(1)>vlan(<vlan-id>)# 
prompt.  
Task 
Command 
Comments 
Defining maximum MAC table size 
supported by the VLAN 
maximum-mac-addresses 
<max-mac> 
Range: 0..16384 
0 – all MAC addresses, without 
restriction 
8. Traffic Processing 
Task 
Command 
Comments 
Configuring VLAN to work in E-Tree 
or E-LAN mode  
mode {e-tree | e-lan} 
CL bridge ports only 
If you change to E-Tree, you need to 
define a bridge port as root. 
Assigning a name to the VLAN  
name <vlan-name> 
To delete the VLAN name, enter no 
name  
Defining bridge ports as egress 
tagged VLAN members (part of 
“VLAN table”) 
tagged-egress 
<bridge_port_number> 
 
Bridge ports in a list can be separated 
by a comma or given as a range, for 
example: 1..3, 5. 
Using no before the command deletes 
VLAN membership for the bridge port. 
Configuring bridge port as root port 
in E-Tree mode 
 
root <bridge-port> 
This command is available only if the 
VLAN mode is E-Tree 
When all E-Tree bridge ports are 
defined as root, the bridge actually 
functions as E-LAN.  
The following commands are available in spanning tree level of port, at the 
config>bridge(1)>port(<port-number>) >spanning-tree# prompt.  
Task 
Command 
Comments 
Enabling the port as an edge port  
admin-edge 
To cancel the edge port, enter no 
admin-edge.  
Enabling the port as the edge port 
automatically 
auto-edge 
Using no before the command cancels 
the setting. 
Setting the path cost for the port 
cost <number> 
If a loop occurs, the path cost is used to 
select an interface to place into the 
forwarding state. 
A lower path cost represents higher 
speed links.   
Forcing the port to transmit RST 
BPDUs 
mcheck 
 
Assigning the priority value on the 
port 
priority <0, 16, 32, 48, 64, 80, 
96, 112, 128, 144, 160, 176, 
192, 208, 224, 240> 
 
Administratively enabling the 
spanning-tree on the port 
no shutdown 
shutdown disables the spanning-tree 
on the port. 
8. Traffic Processing 
Task 
Command 
Comments 
Displaying the spanning-tree status 
on the port 
show status 
 
Examples 
Layer-2 Management Access  
The following figure shows Layer-2 management connectivity via the CL bridge. The connection consists 
of the following sections: 
• 
RI #1 bound to SVI #1 
• 
Flow 1 connecting SVI #1 to BP (bridge port) 1 (this flow must be defined in two directions and 
consists of two sub-flows: bp-svi and svi-bp)  
• 
BP 1 and BP 7 interbridge connectivity (based on VLAN membership that must be configured 
with same VLAN values as VLAN configured in the flows) 
• 
Flow 10 between BP 7 and the management Ethernet port of CL-A module. (this flow must be 
defined in two directions and consists of two sub-flows: eth-mng-bp and bp-eth-mng)  
Bridge#1 Aware
BP 1 8
BP 1 9
ERP#2
E
W
GbE cl-a 1
GbE cl-b 1
10
Router
RI#1
BP 1 2
Bind
Flow
BP 1 4
GbE cl-a 2
L. MAC
BP 1 5
BP 1 5
MNG flow pop/push, bi-
directional flow in all 
CL.2 assemblies
BP 1 3
1
mng-eth 
cl-b
BP 1 6
RI#2
RI#3
DTS
PPP
DCC
PPP
BP 1 7
BP 1 1
SVI#1
mng-eth 
cl-a
 
Layer-2 Management Access  
This connection is configured as follows. 
### Define the SVI#### 
configure port svi 1 
no shutdown 
exit all 
8. Traffic Processing 
 
### Define the CL Bridge#### 
configure bridge 1 
vlan-aware 
port 1 
no shutdown 
exit all 
configure bridge 1 
port 7 
no shutdown 
exit all 
vlan 100 
tagged-egress 1 
tagged-egress 7 
exit all 
 
### Define the physical management port 1 of CL-A module#### 
configure port 
mng-ethernet cl-a/1 
no shutdown 
exit 
 
### Define the Router Interface#### 
configure 
router 1 interface 1 address 172.18.171.121/24 
router 1 interface 1 bind svi 1 
router 1 static-route 0.0.0.0/0 address 172.18.171.1 
exit all 
 
### Define the Flows. The Bridge is working on VLAN 100. The MNG ‘host’ is untagged#### 
 
# Flow # 1: SVI <-> BP 1 1 
 
configure flows 
 
flow svi-bp 
ingress-port svi 1 
egress-port bridge-port 1 1 
classifier mng-untagged 
vlan-tag push vlan 100 p-bit fixed 7 
no shutdown 
exit 
 
flow bp-svi 
ingress-port bridge-port 1 1 
egress-port svi 1 
classifier mng-100 
vlan-tag pop vlan 
no shutdown 
exit 
 
# Flow # 10: MNG ETH <-> BP 
8. Traffic Processing 
 
flow eth-mng-bp 
ingress-port mng-ethernet cl-a/1 
egress-port bridge-port 1 7 
classifier mng-untagged 
vlan-tag push vlan 100 p-bit fixed 7 
no shutdown 
exit 
 
flow bp-eth-mng 
ingress-port bridge-port 1 7 
egress-port mng-ethernet cl-a/1 
classifier mng-100 
vlan-tag pop vlan 
no shutdown 
exit 
 
Layer-2 VLAN-aware Bridging between CL and M-ETH Ports   
The following figure shows three ports sharing the same VLAN (200):  GbE port CL-B/2 and M-ETH ports 
1/3 and 2/8. Since these ports are located on different modules, the bridging between them must be 
done via the CL bridge. 
The connection consists of the following sections: 
• 
Flow 20 between GbE port 2 of CL-A to BP  1 4  
• 
BP 1 4 and BP 1 5 intrabridge connectivity (via VLAN 200 table) 
• 
Flow 21 between BP 1 5 and the GbE port 3 of M-ETH #1 module 
• 
Flow 22 between BP 1 3 and the GbE port 8 of M-ETH #2 module. 
All the flows are bidirectional, i.e. you only need to define one flow from a port to a bridge port, and 
specify the reverse-direction command. 
This connection is configured as follows. 
8. Traffic Processing 
M-ETH in slot #1
Bridge#1 Aware
BP 1 8
BP 1 9
ERP#2
E
W
BP 4 2
BP 4 1
Eth 1 2
Eth 1 1
ERP#3
E
W
Bridge #4
BP 4 3
GbE cl-a 1
GbE cl-b 1
mng-eth 
cl-a
SVI#1
BP 1 7
BP 1 1
Router
RI#1
BP 1 2
Bind
Flow
20
L. MAC
BP 1 5
MNG flow pop/push, bi-
directional flow in all 
CL.2 assemblies
M-ETH in slot #2
BP 7 8
BP 7 5
Bridge #7
BP 7 1
BP 1 3
22
mng-eth 
cl-b
BP 1 6
RI#2
RI#3
DTS
PPP
DCC
PPP
21
Eth 1 3
Eth 2 2
eth 2 1
Eth 2 8
BP 1 4
BP 1 5
GbE cl-a 2
 
Layer-2 VLAN-aware Bridging between CL and M-ETH Ports  
####QoS Configuration###### 
exit all 
configure qos 
shaper-profile b-s 
bandwidth cir 50000 
exit 
policer-profile 10m  
bandwidth cir 10000 eir 0 
exit 
queue-group-profile b-s 
queue-block 0/1 
profile DefaultQueue1 
shaper profile b-s 
exit all 
#### Configuration Physical Ports ###### 
8. Traffic Processing 
configure port 
ethernet cl-a/2 
no shutdown 
queue-group-profile b-s 
exit all 
configure port 
ethernet 1/3 
no shutdown 
queue-group-profile b-s 
exit all 
configure port 
ethernet 2/8 
no shutdown 
queue-group-profile b-s  
exit all 
 
#### Configuring CL Bridge 1 (Ports 1 3, 1 4 and 1 5)###### 
config bridge 1 
vlan-aware 
port 3 
no shutdown 
exit 
port 4 
no shutdown 
exit 
port 5 
no shutdown 
exit 
vlan 200 
tagged-egress 3 
tagged-egress 4 
tagged-egress 5 
exit all 
 
######Configuring the Flow Connection – Consists of 3 flows:  
#flow 20 between Ethernet port CL-A/2 and BP 1 4 
#flow 21 between Ethernet port 1/3 (M-ETH in slot 1) and BP 1 5 
#flow 22 between Ethernet port 2/8 (M-ETH in slot 2) and BP 1 3       ######  
exit all 
config flows 
classifier vlan200 match-any 
match vlan 200 
exit 
 
flow 20 
class vlan200 
ingress Ethernet cl-a/2 
egress bridge-port 1 4 
reverse-direction queue 0 block 0/1 
policer-profile 10m 
no shutdown 
exit 
8. Traffic Processing 
 
flow 21 
class vlan200 
ingress Ethernet 1/3 
egress bridge-port 1 5 
reverse-direction queue 0 block 0/1 
policer profile 10m 
no shutdown 
exit 
 
flow 22 
class vlan200 
ingress Ethernet 2/8 
egress bridge-port 1 3 
reverse-direction queue 0 block 0/1 
policer-profile 10m 
no shutdown 
exit 
 
Cascading Bridges on Different M-ETH Modules via CL Bridge  
The following figure shows cascading bridges on different M-ETH modules via the CL bridge. This 
configuration can be used for extending the number of available bridge ports. 
8. Traffic Processing 
M-ETH in slot #1
Bridge#1 Aware
BP 1 8
BP 1 9
ERP#2
E
W
Bridge #4
GbE cl-a 1
GbE cl-b 1
mng-eth 
cl-a
SVI#1
BP 1 7
BP 1 1
Router
RI#1
Eth 1 3
30
BP 1 2
Bind
Flow
BP 1 4
GbE cl-a 2
L. MAC
BP 1 5
BP 1 5
MNG flow pop/push, bi-
directional flow in all 
CL.2 assemblies
M-ETH in slot #2
Bridge #7
BP 1 3
31
Eth 2 8
mng-eth 
cl-b
BP 1 6
RI#2
RI#3
DTS
PPP
DCC
PPP
BP 4 3
BP 4 2
BP 4 1
BP 7 8
BP 7 5
Eth 2 2
eth 2 1
BP 7 1
Eth 1 2
Eth 1 1
 
Cascading Bridges on Different M-ETH Modules via CL Bridge  
The connection consists of the following sections: 
• 
BP 4 1 bound to Eth 1/1, BP 4 2 bound to Eth 1/2  
• 
BP 4 1, BP 4 2 and BP 4 3 interbridge connectivity (via VLAN 200 table) 
• 
Flow 30 between BP 1 2 (CL bridge) and BP 4 3 (M-ETH module in Slot 1) 
• 
BP 1 2 and BP 1 3 interbridge connectivity (via VLAN 200 table) 
• 
Flow 31 between BP 1 3 (CL bridge) and BP 7 1 (M-ETH module in Slot 2) 
• 
BP 7 1, BP 7 5 and BP 7 8 interbridge connectivity (via VLAN 200 table) 
• 
BP 7 5 bound to Eth 2/1, BP 7 8 bound to Eth 2/2  
8. Traffic Processing 
All the flows are bidirectional, i.e. you only need to define one flow from a port to a bridge port, and 
specify the reverse-direction command. 
This connection is configured as follows. 
####QoS Configuration###### 
exit all 
configure qos 
shaper-profile b-s 
bandwidth cir 50000 
exit 
policer-profile 10m  
bandwidth cir 10000 eir 0 
exit 
queue-group-profile b-s 
queue-block 0/1 
profile DefaultQueue1 
shaper profile b-s 
exit all 
 
 
####Physical Port Configuration (2 Ethernet ports per each M-ETH module)###### 
 
configure port 
ethernet 2/2 
no shutdown 
queue-group profile b-s 
exit all 
 
configure port 
ethernet 2/1 
no shutdown 
queue-group profile b-s 
exit all 
 
configure port 
ethernet 1/2 
no shutdown 
queue-group profile b-s 
exit all  
 
configure port 
ethernet 1/1 
no shutdown 
queue-group profile b-s 
exit all 
 
 
####Bridge 1 Configuration###### 
config bridge 1 
vlan-aware 
port 1 2 
8. Traffic Processing 
no shutdown 
exit 
port 1 3 
no shutdown 
exit 
 
#Configuring Bridge 1 VLAN table#  
vlan 200 
tagged-egress 2 
tagged-egress 3 
exit all 
 
####Bridge 7 Configuration######  
config bridge 7 
vlan-aware 
port 1 
no shutdown 
exit 
 
port 8 
no shutdown 
bind Ethernet 2/2 
exit 
 
port 5 
no shutdown 
bind Ethernet 2/1 
 
exit 
 
#Configuring Bridge 7 VLAN table#  
vlan 200 
tagged-egress 1  
tagged-egress 8 
tagged-egress 5 
exit all 
 
####Bridge 4 Configuration######  
config bridge 4 
vlan-aware 
 
port 1 
no shutdown 
exit 
bind Ethernet 1/1 
 
port 2 
no shutdown 
exit 
bind Ethernet 1/2 
 
port 3 
8. Traffic Processing 
no shutdown 
exit 
 
#Configuring Bridge 7 VLAN table#  
vlan 200 
tagged-egress 1 
tagged-egress 2 
tagged-egress 3 
exit all 
 
######Flow Configuration######  
 
exit all 
config flows 
classifier vlan200 match-any 
match vlan 200 
exit 
 
flow 30 
class vlan200 
ingress bridge-port 1 2 
egress bridge-port 4 3 
reverse-direction queue 0 block 0/1 
policer-profile 10m 
no shutdown 
exit 
 
flow 31 
class vlan200 
ingress bridge-port 1 3 
egress bridge-port 7 1 
reverse-direction queue 0 block 0/1 
policer-profile 10m 
no shutdown 
exit 
RSTP Basic Application  
The following example illustrates the use of the RSTP: 
8. Traffic Processing 
Megaplex-4_B
ETX-1_C
Megaplex-4_A
CL.2 A 
ETH cl-a/1
CL.2 A 
ETH cl-a/1
ETH1
ETH2
NMS
ETH5
CL.2 A 
ETH cl-a/2
CL.2 A 
ETH cl-a/2
M-ETH
ETH 2/1
VS-6/E&M
ETH 2/1
 
Note 
To use RSTP, the MAC address of BPDU packet must be set as 01-80-C2-00-00-
00 peer.  
The connection consists of the following sections.  
Device Megaplex-4_A: 
• 
Assign previously configured queue group profile to the I/O card port, l2cp profile to CL.2 card 
port and enable the ports. 
• 
Enable bridge ports 
• 
Define the bridge port VLAN membership and root port 
• 
Define the flows 
• 
Configure spanning-tree on bridge port level 
• 
Configure spanning-tree on bridge level 
This connection is configured as follows. 
 
#******************** QoS Configuring  
config qos queue-group-profile rstp 
exit all 
 
#************** Configure L2CP profile  
configure port 
    l2cp-profile RSTP mac 01-80-C2-00-00-00 peer 
 
#*********** Configure Ethernet port and associate L2CP profile, queue-group profile 
ethernet cl-a/1  
no shutdown 
8. Traffic Processing 
l2cp profile RSTP 
exit 
 
ethernet cl-a/2  
no shutdown 
l2cp profile RSTP 
exit 
 
ethernet 2/1  
no shutdown 
queue-group profile rstp 
exit 
exit all 
 
#*********** Bridge configuration 
configure bridge 1 
port 1 no shutdown  
port 2 no shutdown  
port 3 no shutdown  
 
#*********** Configure Bridge VLAN table and configure VLAN to work in E-Tree mode 
vlan 100  
tagged-egress 1..3  
maximum-mac-addresses 0  
mode e-tree  
root 1  
root 3  
exit 
exit all 
 
#************** Flow configuration 
configure flows  
classifier-profile "v100" match-all match vlan 100 
 
flow cl-a/1_b1  
classifier "v100"  
ingress-port ethernet cl-a/1  
egress-port bridge-port 1 1  
reverse-direction queue 0 block 0/1  
no shutdown  
exit 
 
flow cl-a/2_b2  
classifier "v100"  
ingress-port ethernet cl-a/2  
egress-port bridge-port 1 2  
reverse-direction queue 0 block 0/1  
no shutdown  
exit 
 
flow 2/1_b3  
8. Traffic Processing 
classifier "v100"  
ingress-port ethernet 2/1  
egress-port bridge-port 1 3  
reverse-direction queue 0 block 0/1  
no shutdown  
exit 
exit all 
 
#******************** Configuring_spanning tree on port  
configure bridge 1 port 1 spanning-tree no shutdown  
configure bridge 1 port 2 spanning-tree no shutdown 
 
#******************** Configuring_spanning tree for bridge  
configure bridge 1 spanning-tree priority 4096 
Device Megaplex-4_B: 
• 
Assign previously configured queue group profile to the I/O card port, l2cp profile to CL.2 card 
port and enable the ports. 
• 
Enable bridge ports 
• 
Define the bridge port VLAN membership and root port 
• 
Define the flows 
• 
Configure spanning-tree on bridge port level 
• 
Configure spanning-tree on bridge level 
This connection is configured as follows. 
#******************** QoS Configuring  
config qos queue-group-profile rstp 
exit all 
 
#************** Configure L2CP profile  
configure port 
    l2cp-profile RSTP mac 01-80-C2-00-00-00 peer 
 
#*********** Configure Ethernet port and associate L2CP profile, queue-group profile 
ethernet cl-a/1  
no shutdown 
l2cp profile RSTP 
exit 
 
ethernet cl-a/2  
no shutdown 
l2cp profile RSTP 
exit 
 
8. Traffic Processing 
ethernet 2/1  
no shutdown 
queue-group profile rstp 
exit 
exit all 
 
#*********** Bridge configuration 
configure bridge 1 
port 1 no shutdown  
port 2 no shutdown  
port 3 no shutdown  
 
#*********** Configure Bridge VLAN table and configure VLAN to work in E-Tree mode 
vlan 100  
tagged-egress 1..3  
maximum-mac-addresses 0  
mode e-tree  
root 1  
root 3  
exit 
exit all 
 
#************** Flow configuration 
configure flows  
classifier-profile "v100" match-all match vlan 100 
 
flow cl-a/1_b1  
classifier "v100"  
ingress-port ethernet cl-a/1  
egress-port bridge-port 1 1  
reverse-direction queue 0 block 0/1  
no shutdown  
exit 
 
flow cl-a/2_b2  
classifier "v100"  
ingress-port ethernet cl-a/2  
egress-port bridge-port 1 2  
reverse-direction queue 0 block 0/1  
no shutdown  
exit 
 
flow 2/1_b3  
classifier "v100"  
ingress-port ethernet 2/1  
egress-port bridge-port 1 3  
reverse-direction queue 0 block 0/1  
no shutdown  
exit 
exit all 
 
8. Traffic Processing 
#******************** Configuring_spanning tree on port  
configure bridge 1 port 1 spanning-tree no shutdown  
configure bridge 1 port 2 spanning-tree no shutdown 
 
#******************** Configuring_spanning tree for bridge  
configure bridge 1 spanning-tree priority 20480 
Device ETX-1_C: 
• 
Enable bridge ports 
• 
Define the bridge port VLAN membership  
• 
Configure spanning-tree on bridge level 
This connection is configured as follows. 
#*********** Bridge configuration  
configure bridge 1 
port 1 spanning-tree no shutdown  
port 2 spanning-tree no shutdown  
port 3 spanning-tree no shutdown  
 
#*********** Configure Bridge VLAN table 
vlan 100  
tagged-egress 1..5  
exit 
 
#******************** Configuring_spanning tree for bridge  
spanning-tree  
priority 8192  
exit 
exit all 
Configuration Errors  
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 
Configuration Error Messages  
Code 
Type 
Syntax 
Meaning 
540 
Error 
BRIDGE PORT IS SHUTDOWN 
One of the following: 
• Bridge port must be bound to SVI 
• Bridge port cannot be at shutdown if it has a VLAN 
defined in Bridge 1.  
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
541 
Error 
MORE THAN ONE SVI BOUND 
TO BRIDGE PORT 
Bridge port should be bound to a single SVI 
 
542 
Error 
SVI PORT IS NOT CONNECTED 
SVI is enabled (“no shutdown”) but not bound  
543 
Error 
SAME SVI BOUND TO 
DIFFERENT BRIDGE PORTS 
SVI must be bound to bridge port 1:1 
544 
Error 
BRIDGE PORT NOT BOUND TO 
PORT 
A bridge port is defined but not bound to any other port. 
548 
Error 
ILLEGAL 
BRIDGE 
PORT 
BINDING 
 
You cannot bind more than one physical port to a bridge 
port. 
549 
Error 
SAME SVI BOUND TO PW 
AND RI 
You cannot bind the same SVI to a PW and a router 
interface. 
550 
Error 
SVI NUMBER  BOUND TO PW 
IS EQUAL TO RI NUMBER 
The number of SVI bound to a PW cannot be equal to the 
router interface number. 
600 
Error 
2 SVI FROM SAME CARD 
CAN’T USE SAME VLAN  
Two SVI ports connected to two PWs defined on the same 
module cannot use the same VLAN. 
700 
Error 
NUM OF BRIDGE PORTS 
EXCEEDED MAX 
The maximum number of bridge ports is as follows: 
• 80 for bridge number 1 (CL modules) 
• 9 bridge pors for each M-ETH bridge 
701 
Error 
VLAN MEMBER AND FL CONF 
MISMATCH 
The VLAN table does not match the bridge/flow 
configuration  
702 
Error 
PORT ALREADY IN USE 
• Two flows with the same VLAN classification use the 
same port.  
703 
Error 
REVERSE DIRECTION IS 
MISSING 
This flow must be configured in the reverse direction. 
705 
Error 
DEFAULT QUEUE IS NOT 
PERMITTTED  
This flow must have a valid non-default queue group 
profile.     
706 
Error 
NUM OF FLOWS OVER M-ETH 
BRIDGE EXCEEDS ONE 
M-ETH bridge cannot be connected to more than one flow. 
707 
Error 
INVALID VLAN IDENTIFIER 
Flows connected to a bridge must have a VLAN 
classification 
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
708   
 
Error 
WRONG FLOW ON 
PROTECTED PORT 
A port protected by Ethernet group protection cannot 
serve as a flow ingress/egress port 
709 
Error 
BRIDGE PORT MUST BE 
EGRESS 
 
When configuring a flow between a physical port and a 
bridge port, the ingress and egress ports must be set as 
follows: 
• physical port= ingress port 
• bridge port = egress port. 
710 
Error 
SVI NOT CONNECTED TO ANY 
ENTITY 
An SVI port participating in a PW traffic flow must be 
connected to a PW. 
Displaying MAC Address Table  
You can display a Megaplex-4 MAC table, which provides information on dynamic MAC addresses, 
bridge ports and VLANs associated with them. The regular show mac-address-table command displays 
only 100 entries. To display the complete MAC address table (up to 16384 addresses), you can use 
file>copy mac-table command described below.  
 To display MAC address table for all ports and VLANs (up to 100 entries): 
• 
At the config>bridge(bridge_number)# prompt, enter show mac-address-table all. 
The MAC address table is displayed.  
# configure bridge 1 
config>bridge(1)# show mac-address-table all 
 
Total MAC Addresses   : 20 
 
 
Vlan  MAC Address       Port Status 
--------------------------------------------------------------- 
3     00-00-00-00-00-CA 80   Dynamic 
3     00-00-00-00-01-01 1    Dynamic 
3     00-00-00-00-02-01 3    Dynamic 
3     00-00-00-00-03-01 5    Dynamic 
3     00-00-00-00-10-01 6    Dynamic 
4     00-00-00-00-00-CA 80   Dynamic 
4     00-00-00-00-01-01 1    Dynamic 
4     00-00-00-00-02-01 3    Dynamic 
4     00-00-00-00-03-01 5    Dynamic 
4     00-00-00-00-10-01 6    Dynamic 
5     00-00-00-00-00-CA 80   Dynamic 
5     00-00-00-00-01-01 1    Dynamic 
8. Traffic Processing 
5     00-00-00-00-02-01 3    Dynamic 
5     00-00-00-00-03-01 5    Dynamic 
5     00-00-00-00-10-01 6    Dynamic 
6     00-00-00-00-00-CA 80   Dynamic 
6     00-00-00-00-01-01 1    Dynamic 
6     00-00-00-00-02-01 3    Dynamic 
6     00-00-00-00-03-01 5    Dynamic 
6     00-00-00-00-10-01 6    Dynamic 
 
 To display MAC address table for a specific VLAN/port:  
• 
At the config>bridge (bridge_number)# prompt, enter show mac-address-table all [vlan <vlan-
id > | ports <port-number> ]. VLAN option is used only for VLAN-aware bridge ports. 
The MAC address table for the selected VLAN/port is displayed. For example, the table below is 
for vlan 10, bridge ports 11-15:  
config>bridge(1)# show mac-address-table all vlan 10 ports 11..15 
 
Total MAC Addresses   : 5 
 
 
Vlan  MAC Address       Port Status 
--------------------------------------------------------------- 
10    00-00-00-00-02-03 11   Dynamic 
10    00-00-00-00-03-02 13   Dynamic 
10    00-00-00-00-10-03 15   Dynamic 
 To display all the MAC address table entries (up to 16384 addresses):  
1. Open a TFTP Server for file transfer to a folder selected on a PC. 
2. At the file# prompt, enter copy mac-table tftp://<PC IP address>/<filename> 
file# copy mac-table tftp://172.17.151.59/MAC_TAB.txt 
 Are you sure? [yes/no] _ y 
file# 
***** 
File copy command was completed.***** 
 
*****mac-table copied to tftp://172.17.151.59/MAC_TAB.txt successfully***** 
 
*****1210 bytes copied in 1 secs (1210 bytes/sec)***** 

## 8.2 Cross-Connections  *(p.661)*

8. Traffic Processing 
3. Open the created text file with an appropriate text viewer (that allows viewing table format).  
Now all the MAC addresses can be displayed in one file. 
Bridge  VLAN   MAC Address          
Port   Status  Name    
------  -----  
-----------------     -----  
------- 
1       
500    00-00-00-00-00-bf    
20     
Learned   
MAC1 
1       
500    00-00-00-00-aa-07    80     
Learned    
MAC2 
1       
500    00-00-00-00-00-bb    20     
Learned    
MAC3 
1       
500    00-00-00-00-00-c3    20     
Learned     ---   
1       
500    00-00-00-00-aa-03    80     
Learned    
MAC4 
1       
500    00-00-00-00-00-bd    20     
Learned     ---   
1       
500    00-00-00-00-aa-05    80     
Learned    
MAC14       
1       
500    00-00-00-00-00-c1    20     
Learned     ---    
1       
500    00-00-00-00-aa-01    80     
Learned     ---   
1       
500    00-00-00-00-aa-06    80     
Learned     ---   
1       
500    00-00-00-00-00-c2    20     
Learned     ---   
1       
500    00-00-00-00-aa-02    80     
Learned     ---   
2       
500    00-00-00-00-00-bc    20     
Learned     ---   
2       
500    00-00-00-00-00-c4    20     
Learned     ---   
2       
500    00-00-00-00-aa-04    80     
Learned     ---   
1       
500    00-00-00-00-aa-08    80     
Learned     ---   
1       
500    00-00-00-00-00-c0    20     
Learned     ---     
1       
500    00-00-00-00-aa-00    80     
Learned     ---    
 
8.2 Cross-Connections  
The matrix in the figure below describes all possible cross-connections you can perform in the 
Megaplex-4.  
8. Traffic Processing 
 
Cross-Connections in Megaplex-4   
The matrix cells are color-coded to indicate which option (command) to choose for the various 
modules/ports/timeslots/entities at both ends, as follows: 
Color 
Command 
Meaning 
 
ds0, tdm, split-ts  
cross-connect on the DS0 or DS1 level and/or split timeslot cross-connect 
DS 
ds0 
cross-connect on the DS0 level (no split timeslot cross-connect) 
8. Traffic Processing 
Color 
Command 
Meaning 
 
ds0, tdm 
cross-connect on the DS0 level and/or split timeslot cross-connect 
bind 
cross-connect for Ethernet-over-TDM traffic 
sdh-sonet 
SDH/SONET cross-connect 
 
pw-tdm 
Pseudowire cross-connect  
A number inside the cell refers to a special note regarding this type of cross-connect. 
Examples of using the table: 
• 
To cross-connect a t1-i port to vt1.5 virtual tributary or e1-i to sdh, you have to use sdh-sonet 
cross-connect  
• 
To map the entire e1 port to an e1-i port, you can use either ds1 or ds0 cross-connect 
• 
To cross-connect an hdlc port to e1, you have to use the bind command 
• 
To cross-connect unframed stream, you have to use the ds1 command. 
Split timeslot cross-connect is possible for the same ports where ds0 cross-connect is used, when 
working with the following modules: VC-4A, VC-8A, VS serial ports operating in V.110 mode. Voice ports 
of VS modules and cmd channels of TP and VS-6/BIN modules do not support split timeslot 
cross-connect. 
Factory Defaults 
No cross-connections exist in Megaplex-4 by default. 
Benefits 
Cross-connections allow flexible mapping of individual DS0 channels, full DS1 streams, pseudowire or 
VC/VT entities. 
8. Traffic Processing 
Functional Description  
Timeslot Types 
When configuring the cross-connect, it is necessary to instruct each port how to handle the traffic flow 
and signaling information. This is performed by defining the timeslot type.  
The selections are as follows:  
• 
data: the timeslot is handled as a data channel. This means that any signaling information 
associated with the channel is ignored. 
• 
voice: the timeslot is handled as a voice channel. This means two things: 
 
It is necessary to select a link framing mode that supports channel associated signaling, e.g., 
G.704 multiframe (G.732S) for E1, SF (D4) or ESF for T1. 
 
The signaling information of the channel is routed (automatically) in parallel with the 
channel payload. 
Full Timeslot versus Split Timeslot Assignment (Split Timeslot Cross-Connect) 
For user ports that do not require a full timeslot (eight bits, equivalent to a bandwidth of 64 kbps), 
Megaplex-4 also permits split timeslot assignment, that is, assignment of individual bits in a selected 
timeslot. This functionality is used for ports operating at channel rates lower than 38.4 kbps.  
Split timeslot assignment increases the bandwidth utilization efficiency for TDM modules or channels, 
because it enables the allocation of link bandwidth in smaller (sub-DS0) units: the split timeslot 
assignment unit is 16 kbps (a pair of consecutive bits in a timeslot).  
Split timeslot assignment is supported by voice modules (ADPCM encoding) and low-speed data 
modules.  
The split timeslot assignment is performed in coordination with the modules having sub-DS0 ports. It is 
not possible to mix bits from different modules in the same DS0 timeslot. 
The location of data bits in a timeslot depends on the port data rate and is shown in the diagram below: 
• 
For 2.4, 4.8 or 9.6 kbps data rates, the data can occupy bits 1-2, 3-4, 5-6 or 7-8. 
• 
For 19.2 kbps data rate, the data can occupy bits 1-4 or 5-8. 
• 
MSB and LSB denote most significant bit and least significant bit, respectively. 
8. Traffic Processing 
Data Allocation in a Timeslot 
Rate 
Data Location in Timeslot 
2.4, 4.8, 9.6 
MSB                                                      LSB 
1 
2 
3 
4 
5 
6 
7 
8 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
19.2 
MSB                                                      LSB 
1 
2 
3 
4 
5 
6 
7 
8 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Bidirectional Transfer Mode  
The bidirectional transfer mode is used to transfer data/voice simultaneously in both receive and 
transmit directions.   
Unidirectional Broadcast Function  
The unidirectional broadcast mode enables a user at a central location to send data or voice to multiple 
users connected to remote ports via the  
Megaplex-4 links (simplex communication). In this mode, any message is simultaneously received by all 
the remote unidirectional users, but none of them can send back data to the originator.  
This capability is achieved by separating the handling of the receive and transmit paths for timeslots 
assigned to unidirectional channels.  
You can specify the operating mode of each unidirectional channel or E1/T1 timeslot either as 
unidirectional transmit, or unidirectional receive: 
• 
Unidirectional transmit: the channel/timeslot transmits, but cannot receive (its receive path is 
disconnected). The information transmitted by the channel can be routed to any number of 
E1/T1/E1-i/T1-i ports for distribution to multiple remote Megaplex-4 units.  
8. Traffic Processing 
• 
Unidirectional receive: the channel/timeslot receives, but cannot transmit (its transmit path is 
disconnected). The user can select the source port (E1/T1/E1-i/T1-i or compatible I/O port) from 
which the channel receives, and the specific timeslot. The same source port or a range of 
timeslots can be connected to several channels operating in the unidirectional receive mode. 
The unidirectional broadcast function is available only for ds0 cross-connect. 
The unidirectional broadcast capabilities depend on the module type: 
• 
Modules with internal or external E1 and T1 ports (see below): the payload received by a 
unidirectional broadcast timeslot is distributed in parallel to multiple destination timeslots of 
other E1 or T1 links, or to modules with unidirectional receive capabilities. 
• 
Voice and data I/O modules (see below): not all the modules support unidirectional capabilities, 
but only modules which require a single timeslot per channel, and that do not require 
handshaking for setting up a link. Therefore, unidirectional broadcast is supported by VC-
4/4A/8/8A/16 voice modules with E&M and FXS interfaces, or VS data modules. In addition, VS-
6/E&M and FXS/E&M modules support unidirectional receive capabilities.  
Unidirectional Broadcast for E1/T1 Ports  
I/O Modules 
Ports 
unidirection-tx  
unidirection-rx  
CL.2 
Internal E1/T1 
√ 
√ 
T3  
Internal T1 
√ 
√ 
Unidirectional Broadcast in Voice and Data I/O Modules 
Bidirectional Broadcast Applications  
The bidirectional broadcast mode enables a user at a central location to communicate with several users 
connected to remote Megaplex-4 units, using polled communications.  
This mode is supported by the following modules: 
I/O Modules 
Ports 
unidirection-tx  
unidirection-rx  
VC-4/4A/8/8A/16 
FXS & E&M 
√ 
√ 
VC-4/4A/8/8A/16 
FXO 
- 
- 
VS-12, VS-6/BIN 
serial  
√ 
√ 
VS-6/E&M, FXS/E&M 
E&M 
- 
√ 
8. Traffic Processing 
• 
VS modules, whose serial ports are operating in 3-bit-transitional (at the rate of 64 kbps) and 
R.111 mode (see Encapsulation Modes in in VS Modules chapter of Megaplex-4 I/O Modules).  
• 
VS-6/E&M and FXS/E&M VS voice modules. 
Broadcast is achieved as follows:  
• 
At the central (source) location, a specific timeslot is assigned to each remote site (Rx). The 
same data received from the source channel is broadcast (Tx) in parallel to all the timeslots.   
• 
At each remote (destination) site, the corresponding timeslot is connected to the corresponding 
VC/VS module channel (with regular bi-directional connection) 
When the equipment connected to a remote channel identifies a polling addressed to itself, the 
remote device answer is forwarded to the source location (such as Regional Center node in the 
figure below). The Megaplex device located in the National Center takes in the channel with 
active data back to the SCADA master port, located at the Regional Center.  
VS Modules 
The logic to select the active channel can be based on end-to-end control with RTS signaling (end-to-
end-control is selected) or data activity (no end-to-end-control). The choice depends on the connected 
equipment: if central/remote device supports RTS signaling, use ene-to-end control signaling. 
A basic bidirectional broadcast application is shown below. 
8. Traffic Processing 
Control Center
E1 1/1 TS 1
VS-12
Megaplex-4
SCADA
64 kbps
VS-12
Megaplex
RTU
64 kbps
VS-12
Megaplex
RTU
64 kbps
VS-12
Megaplex
RTU
Up to 30 
nodes
VS serial port 3/1:
bidirection-rx 
E1 5/1 TS 1
E1-i CL-A/1 TS 1
SDH
E1
E1
VS serial port:
bi-direction 
VS serial port:
bi-direction 
VS serial port:
bi-direction 
64 kbps
 
Bidirectional Broadcast: Serial Port is Sending Data to Different E1 Ports of Remote RTUs 
Additional applications are possible using a virtual entity defined on VS modules, which is called TDM 
bridge.  
In the figure below, a VS-12 module installed in a Regional Center uses the TDM bridge to send and 
receive data to/from 3 remote RTUs, while a VS-12 module installed in a National center performs data 
monitoring of the RTU replies/statuses.   
 
 
8. Traffic Processing 
E1 1/1 TS 1
64 kbps
Up to 30 
Nodes
E1 5/1 TS 1
E1-i CL-A/1 TS 1
SDH
E1
E1
VS Serial Port:
bi-direction
VS Serial Port 3/2
Megaplex-4
National Center (Monitoring)
Megaplex-4
SCADA
VS-12
RTU
E1 6/1 TS 1
VS-12
64 kbps
VS Serial Port:
bi-direction
RTU
VS-12
64 kbps
VS Serial Port:
bi-direction
RTU
VS-12
VS-12
Regional Center
Serial Port
SCADA
TDM 
Bridge
Bind
tdm-bridge3/1
bidirection-rx
Megaplex
Megaplex
Megaplex
tdm-bridge3/1
unidirection-rx
VS Serial Port:
Unidirection-rx
64 kbps
64 kbps
 
Bidirectional Broadcast to/from Remote RTUs with Monitoring over E1   
FXS/E&M and VS-6/E&M Modules 
The logic to select the active channel can be based on voice signaling (bidirection-rx) or voice-grade data 
activity (bi-direction). The choice depends on the connected equipment: if the central/remote device 
supports signaling, use bidirection-rx mode, otherwise use bi-direction mode.  
The bidirectional broadcast capacity of the E&M module is 30 timeslots. Only one internal voice port per 
external port of E&M module can be connected using “bidirection-rx” DS0 cross connect option. Other 
ports are usually configured as bi-direction DS0 cross-connect. A typical application is shown below. The 
application of VS-6/E&M modules is similar with FXS/E&M modules. 
E1 1/1 TS 1
Voice
Megaplex
Megaplex
Megaplex
Up to 30 
Nodes
E1 5/1 TS 1
E1-i CL-A/1 TS 1
SDH
E1
E1
voice port:
bi-direction
voice port:
bi-direction
voice port:
bi-direction 
Regional Centers
Network
SCADA
Voice port 9/9:
bidirection-rx
Megaplex-4
National Center
Megaplex-4
SCADA
FXS/E&M
RTU
RTU
RTU
FXS/E&M
Voice
Voice
E1 6/1 TS 1
E1
Voice port 9/4:
bi-direction
 
Bidirectional Voice Grade Data Broadcast 1:n  
8. Traffic Processing 
V.24 Conference Applications  
In addition to bidirectional broadcast, VS-6/BIN modules support V.24 conference applications, where 
conference members are able to communicate in any-to-any configuration. Each port can transmit and 
all other conference port members can receive the data. Each conference session can include up to 31 
members (local port vs. 30 remote ports). 
In the example below, VS-6/BIN module enables V.24 conference between SCADA center and any of 
Remote RTUs. The central module must be VS-6/BIN set to the conference mode, while the modules 
connected to RTUs can be any VS module with serial ports (set to regular bi-directional mode). 
Encapsulation must be 3-bit transitional and the data rate 64-kbps (enables asynchronous data rates up 
to 19.2Kbps). All RTUs can communicate between each other, on condition that two of them 
communicate simultaneously, while other are transmitting idle code value (e.g 0xFF or 0xC0).   
Control Center
E1 1/1 TS 1
VS-12
Megaplex-4
SCADA
64 kbps
VS-6/BIN
Megaplex
RTU
64 kbps
Megaplex
RTU
64 kbps
Megaplex
RTU
Up to 30 
nodes
VS serial port 3/1:
conference mode
bidirection-rx 
E1 5/1 TS 1
E1-i CL-A/1 TS 1
SDH
E1
E1
VS serial port:
bi-direction 
VS serial port:
bi-direction 
VS serial port:
bi-direction 
64 kbps
VS-6/FXS
VS-6/BIN
 
VS-6/BIN Module enabling V.24 Conference Session 
8. Traffic Processing 
Configuring a DS0 Cross-Connection  
 To configure a DS0 cross-connection:  
1. At the config# prompt, enter cross-connect or cr. 
The config>xc# prompt appears. 
2. Configure the cross-connection as illustrated and explained below for the various interfaces. 
 
Task 
Command 
Comments 
Cross-connecting timeslot x 
(or range of sequential 
timeslots x1..x2) of the 
e1/t1/e1-i/t1-i/ds1/ds1-opt 
port to timeslot y (or range of 
sequential timeslots starting 
from y1) on the e1 port and 
setting its/their type and 
direction 
ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>] ts 
{<x> | <[x1..x2]>} e1 
<slot>/<port>/[<tributary>]   
{ts <y> | start-ts <y1>} {data | 
voice} [bi-direction | 
unidirection-rx | unidirection-
tx] 
 
no ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>] ts {<x> 
| <[x1..x2]>} e1 <slot>/<port>/ 
[<tributary>] {ts <y> | start-ts 
<y1>} removes cross-connection  
If one of the timeslots is defined 
as voice and the CL module has no 
SDH/SONET ports, this cross-
connect is impossible for internal 
T1 ports 17 to 28 of the T3 module 
(due to insufficient signaling 
bandwidth). 
See Examples 3,4 
Cross-connecting timeslot x 
(or range of sequential 
timeslots x1..x2) of the 
e1/t1/e1-i/t1-i/ds1/ds1-opt 
port to timeslot y (or range of 
sequential timeslots starting 
from y1) on the t1 port and 
setting its/their type and 
direction  
 
ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>] ts 
{<x> | <[x1..x2]>} t1 
<slot>/<port>/[<tributary>]  
{ts <y> | start-ts <y1>} {data | 
voice} [bi-direction | 
unidirection-rx | unidirection-
tx] 
  
no ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>] ts {<x> 
| <]x1..x2]>} t1 <slot>/<port>/ 
[<tributary>] {ts <y> | start-ts 
<y1>} removes cross-connection  
If one of the timeslots is defined 
as voice and the CL module has no 
SDH/SONET ports, this cross-
connect is impossible for internal 
T1 ports 17 to 28 of the T3 module 
(due to insufficient signaling 
bandwidth). 
See Examples 3,4 
8. Traffic Processing 
Task 
Command 
Comments 
Cross-connecting timeslot x 
of the e1/t1/e1-i/t1-i/ds1 
port to a voice port and 
setting its direction  
ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port> ts <x> voice 
<slot>/<port> [bi-direction | 
unidirection-rx | unidirection-tx 
| bidirection-rx }    
no ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port> ts <x> voice 
<slot>/<port> removes 
cross-connection 
bidirection-rx mode is available 
only for the following modules: 
• E&M interfaces of VS-6/E&M 
and FXS/E&M modules. 
This selection is available only for 
a single internal port (tributary) 
per each external port. 
If the CL model does not have 
SDH/SONET ports, this 
cross-connect is impossible for 
internal T1 ports 17 to 28 of the T3 
module (due to insufficient 
signaling bandwidth). 
see Examples 1, 5, 7 
Cross-connecting timeslot x 
of the e1/t1/e1-i/t1-
i/ds1/ds1-opt port to ds0-
g703 port  
ds0 {e1 | t1 | e1-i | t1-i | ds1| 
ds1-opt } 
<slot>/<port>/[<tributary>] ts 
<x> } ds0-g703 <slot>/<port>]   
no ds0 {e1 | t1 | e1-i | t1-i | ds1 | 
ds1-opt } 
<slot>/<port>/[<tributary>] ts {<x> 
| <[x1..x2]>} e1 <slot>/<port>/ 
[<tributary>] {ts <y> | start-ts 
<y1>} removes cross-connection  
If one of the timeslots is defined 
as voice and the CL module has no 
SDH/SONET ports, this cross-
connect is impossible for internal 
T1 ports 17 to 28 of the T3 module 
(due to insufficient signaling 
bandwidth). 
See Examples 3,4 
Cross-connecting timeslot x  
of the e1/t1/e1-i/t1-
i/ds1/ds1-opt port to cmd-
channel and setting its 
direction 
 
ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>] ts 
<x> cmd-channel <slot>/<port> 
[bi-direction | unidirection-rx | 
unidirection-tx]  
no ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>] ts <x> 
cmd-channel <slot>/<port> 
removes cross-connection  
This command is available in TP 
and VS-6/BIN modules. See 
Example in Chapter 14, 
Teleprotection Module section. 
8. Traffic Processing 
Task 
Command 
Comments 
Cross-connecting timeslot x 
(or range of sequential 
timeslots x1..x2) of the 
e1/t1/e1-i/t1-i/ds1/ds1-opt 
port to a serial port and 
setting its direction  
ds0 {e1 | t1 | e1-i | t1-i | ds1| 
ds1-opt} <slot>/<port> ts <x> 
serial <slot>/<port> 
[bi-direction | unidirection-rx | 
unidirection-tx | bidirection-rx }  
 
no ds0 {e1 | t1 | e1-i | t1-i | ds1| 
ds1-opt} <slot>/<port> ts <x> 
serial <slot>/<port> removes 
cross-connection  
bidirection-rx mode is available 
only in VS modules operating in 3-
bit transitional mode at the rate of 
64 kbps.  
see Examples 1, 2, 6, 8 
Cross-connecting timeslot x 
of the e1/t1/e1-i/t1-
i/ds1/ds1-opt port to a ds0-
g703 port  
ds0 {e1 | t1 | e1-i | t1-i | ds1 | 
ds1-opt} <slot>/<port> ts <x> 
ds0-g703<slot>/<port>  
 
no ds0 {e1 | t1 | e1-i | t1-i | ds1| 
ds1-opt} <slot>/<port> ts <x> 
serial <slot>/<port> removes 
cross-connection  
Cross-connecting timeslot x 
of the e1/t1/e1-i/t1-i/ds1 
port to a tdm bridge of VS 
module and setting its 
direction in bidirectional 
broadcast applications 
ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port> ts <x> tdm-bridge 
<slot>/<port> [bi-direction | 
unidirection-rx | bidirection-rx }  
 
bi-direction –not used in this 
version 
unidirection-rx – can be used in 
monitoring applications  
bidirection-rx  - use for 
connections to RTUs 
see Example 9 
Cross-connecting timeslot x 
(or range of sequential 
timeslots x1..x2) of the 
e1/t1/e1-i/t1-i/ds1/ds1-opt 
port to timeslot y (or range of 
sequential timeslots starting 
from y1) on the e1-i port and 
setting its/their type and 
direction 
ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>] ts 
{<x> | <[x1..x2]>} e1-i 
<slot>/<port>/[<tributary>]  {ts 
<y> | start-ts <y1>} {data | 
voice} [bi-direction | 
unidirection-rx | unidirection-
tx] 
  
no ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/ 
[<tributary>] ts {<x> | <[x1..x2]>} 
e1-i <slot>/<port>/ [<tributary>] 
{ts <y> | start-ts <y1>} removes 
cross-connection  
See Examples 3,4 
 
Cross-connecting timeslot x 
(or range of sequential 
timeslots x1..x2) of the 
e1/t1/e1-i/t1-i/ds1/ds1-opt 
port to timeslot y (or range of 
sequential timeslots starting 
from y1) on the t1-i port and 
setting its/their type and 
direction 
ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>] ts 
{<x> | <[x1..x2]>} t1-i 
<slot>/<port>/[<tributary>]  {ts 
<y> | start-ts <y1>} {data | 
voice} [bi-direction | 
unidirection-rx | unidirection-
tx] 
  
no ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/ 
[<tributary>] ts {<x> | <[x1..x2]>} 
t1-i <slot>/<port>/ [<tributary>] 
{ts <y> | start-ts <y1>} removes 
cross-connection  
See Examples 3,4 
 
8. Traffic Processing 
Task 
Command 
Comments 
Cross-connecting timeslot x 
(or range of sequential 
timeslots x1..x2) of the 
e1/t1/e1-i/t1-i/ds1/ds1-opt 
port to timeslot y (or range of 
sequential timeslots starting 
from y1) on the ds1 port and 
setting its/their type and 
direction 
ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>] ts 
{<x> | <[x1..x2]>} ds1 
<slot>/<port>/[<tributary>]  {ts 
<y> | start-ts <y1>} {data | 
voice} [bi-direction | 
unidirection-rx | unidirection-
tx] 
  
no ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/ 
[<tributary>] ts {<x> | <[x1..x2]>} 
ds1 <slot>/<port>/ [<tributary>]  
{ts <y> | start-ts <y1>} removes 
cross-connection  
Note: When following {e1 | t1 | e1-i | t1-i | ds1} options, the optional <tributary> index relates to 
Megaplex T3 modules and denotes their internal T1 ports. Therefore, the cross-connect side involving these 
tributary ports is relevant only for t1 port options, not for e1, e1-i, t1-i, or ds1.   
Example. Bidirectional DS0 Cross-Connect: CL <-> I/O Modules, Single Timeslot              
• 
CL-A, port E1-i port 1/1, timeslot 1 to voice port 8/1 
• 
CL-A, port E1-i port 1/1, timeslot 2 to serial port 9/1 
config 
cr 
ds0 e1-i cl-a/1 ts 1 voice 8/1 bi-direction 
ds0 e1-i cl-a/1 ts 2 serial 9/1 bi-direction 
Configuring a TDM Cross-Connection 
 To configure a TDM cross-connection: 
1. At the config# prompt, enter cross-connect or cr. 
The config>xc# prompt appears. 
2. Configure the cross connection as illustrated and explained below for the various interfaces. 
8. Traffic Processing 
Task 
Command 
Comments 
Cross-connecting 
the full payload 
from this e1/t1/e1-
i/t1-i/ds1 port with 
another port of the 
same type and 
configuration 
tdm {e1 | t1 | e1-i | t1-i | ds1 } 
<slot>/<port>  {e1 | t1 | e1-i | t1-i | ds1 } 
<slot>/<port>  
 
• no 
tdm {e1 | t1 | e1-
i | t1-i } 
<slot>/<port> com
mand disables the 
cross-connection 
Unframed T1 port of 
M16T1 module cannot 
be cross-connected 
with T1-i port of CL 
module  
If the CL module has no 
SDH/SONET ports, this 
cross-connect is 
impossible for 
unframed E1/T1 port 
of VS-16E1T1-PW and 
VS-6/E1T1 module.  
Cross-connecting 
the full t1 payload 
from this tributary 
port with another 
port of the same 
type and 
configuration 
tdm t1  <slot>/<port>/<tributary>  t1 <slot>/<port>/<
tributary>  
 
T3 modules only  
• no tdm t1 
<slot>/<port>/ 
<tributary> 
command disables 
the cross-
connection 
Configuring a Split Timeslot Cross-Connection 
 To configure a split timeslot cross-connection: 
1. At the config# prompt, enter cross-connect or cr. 
The config>xc# prompt appears. 
2. Configure the cross connection as illustrated and explained below for the various interfaces. 
8. Traffic Processing 
Task 
Command 
Comments 
Cross-connecting the 
timeslot bits of the 
e1/t1/e1-i/t1-i/ds1 port 
with this voice port 
(defining the selected 
data rate on the voice 
port)  
split-ts {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>] ts  <ts 
x> bits <bit  y> 
voice  <slot/port[/tributary]>} 
 
Used for VC-4A/VC-8A modules 
working in ADPCM mode 
no ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>]  ts <ts x> 
bits <bit y> voice <slot>/<port> 
removes cross-connection  
The entire number of 
cross-connected timeslot bits should 
match the selected data rate 
Cross-connecting the 
timeslot bits of the 
e1/t1/e1-i/t1-i/ds1 port 
with this serial port 
(defining the selected 
data rate on the serial 
port)  
split-ts {e1 | t1 | e1-i  | t1-i | ds1} 
<slot>/<port>[<tributary>] ts <ts 
x> bits <bit y> serial 
<slot/port[/tributary]>}  
  
no ds0 {e1 | t1 | e1-i | t1-i | ds1} 
<slot>/<port>/[<tributary>]  ts <ts x> 
bits <bit y> serial <slot>/<port> 
removes cross-connection  
The entire number of 
cross-connected timeslot bits should 
match the selected data rate 
Configuring an SDH/SONET Cross-Connection  
 To configure an SDH/SONET cross-connection: 
1. At the config# prompt, enter cross-connect. 
The config>xc# prompt appears. 
2. Configure the cross connection as illustrated and explained below for the various interfaces. 
Task 
Command 
Comments 
Cross-connecting the E1 port 
of an I/O module with a 
vc12-vt2 from an SDH port 
(“transparent clocking”) 
sdh-sonet vc12-vt2 
<slot>/<port>/<au4>/ <tug3>/ 
<tug2>/<vc12-vt2> e1<slot>/<port>    
  
• Adding no before the full 
command  disables the 
cross-connection  
• This command is available only for 
unframed E1 links in VS-16E1T1-
EoP, VS-16E1T1-PW, and VS-
6/E1T1 modules 
8. Traffic Processing 
Task 
Command 
Comments 
Cross-connecting the vc12-
vt2 from an SDH port with 
an e1-i port of an I/O 
module  
sdh-sonet vc12-vt2 
<slot>/<port>/<au4>/<tug3>/ 
<tug2>/<vc12-vt2> e1-i <slot>/<port>   
• Adding no before the full 
command disables the 
cross-connection  
• For VS-16E1T1-EoP module, this 
command is available only when 
the line-type of e1-i port is set as 
g.732n-crc. 
Cross-connecting the vc12-
vt2 from an SDH port with a 
ds1 port of an I/O module  
sdh-sonet vc12-vt2 
<slot>/<port>/<au4>/<tug3>/ 
<tug2>/<vc12-vt2> ds1  <slot>/<port> 
• Adding no before the full 
command disables the 
cross-connection  
• This command is available only for 
unframed DS1 port in VS-16E1T1-
PW and VS-6/E1T1 modules.  
Cross-connecting two vc12-
vt2 containers  
  
sdh-sonet vc12-vt2 
<slot>/<port>/<au4>/ 
<tug3>/ <tug2>/<vc12-vt2> vc12-vt2 
<slot>/<port>/<au4>/ <tug3>/<tug2>/ 
<vc12-vt2>    
• Adding no before the full 
command  disables the 
cross-connection 
Number of vc-vt containers per CL 
module is limited to 252.  
Cross-connecting the T1 port 
of an I/O module with a 
vc11-vt1.5 from a SONET 
port (“transparent clocking”) 
sdh-sonet vc11-vt1.5 
<slot>/<port>/<au4>/<tug3>/  
<tug2>/<vc11-vt5> t1 <slot>/<port>  
 
• Adding no before the full 
command  disables the 
cross-connection 
• This command is available only for 
unframed T1 links in M16T1 VS-
16E1T1-EoP, VS-16E1T1-PW and 
VS-6/E1T1 modules 
Cross-connecting the 
vc11-vt1.5 from a SONET 
port with a ds1 port of an 
I/O module  
sdh-sonet vc11-vt1.5 
<slot>/<port>/<au4>/<tug3>/ 
<tug2>/<vc11-vt1.5> 
ds1  <slot>/<port> 
• Adding no before the full 
command disables the 
cross-connection  
• This command is available only for 
unframed DS1 port in VS-16E1T1-
PW and VS-6/E1T1 modules.  
Cross-connecting two 
vc11-vt1.5 containers 
 
sdh-sonet vc11-vt1.5 
<slot>/<port>/<au4>/<tug3>/ 
<tug2>/<vc12-vt2> vc11-vt1.5 
<slot>/<port>/<au4>/ 
<tug3>/<tug2>/<vc11-vt1.5>    
• Adding no before the full 
command  disables the 
cross-connection 
Number of vc-vt containers per CL 
module is limited to 252 
8. Traffic Processing 
Task 
Command 
Comments 
Cross-connecting two vc3-
sts1  
 
sdh-sonet vc3-sts1 
<slot>/<port>/<au4>/<tug3> vc3-sts1 
<slot>/<port>/<au4>/<tug3> 
• Adding no before the full 
command  disables the 
cross-connection 
 
Cross-connecting two 
vc4-sts3c  
sdh-sonet vc4-sts3c 
<slot>/<port>/<au4> vc4-sts3c 
<slot>/<port>/<au4> 
• Adding no before the full 
command  disables the 
cross-connection 
Configuring a PW-TDM Cross-Connection 
 To configure a pw-tdm cross connection: 
1. At the config# prompt, enter cross-connect or cr. 
The config>xc# prompt appears. 
2. Configure the cross connection as illustrated and explained below for the various interfaces. 
Task 
Command 
Comments 
Establishing cross-
connection 
between this 
pseudowire and 
ds1, e1-i, e1, or t1 
port 
 
pw-tdm pw <pw number> {ds1 <slot>/<port> 
| e1 <slot>/<port>  | t1 <slot>/<port> | e1-i 
<slot>/<port>} time-slots <ts list> 
 
e1 and t1 ports are relevant to VS-6/E1T1 
and VS-16E1T1/PW modules only. 
e1-i ports are relevant to the 
SH-16/E1/PW module only. 
The ds1 port should be populated by 
using additional ds0 cross-connect 
command between ds1 and other ports in 
Megaplex-4 (see example below) 
Timeslots in a list can be separated by a 
comma or given as a range, for example: 
1..3, 5. 
Using no before the command removes 
the cross-connection 
Cross-connect cannot be configured to 
PWs defined as protection ports. 
A single PW can be connected to a single 
DS1 or to a single serial port.  
8. Traffic Processing 
Task 
Command 
Comments 
Establishing cross-
connection 
between this 
pseudowire and 
serial or ds0-g703 
port 
pw-tdm pw <pw number> { serial | ds0-g703} 
<slot>/<port>  
 
Using no before the command removes 
the cross-connection 
Cross-connect cannot be configured to 
PWs defined as protection ports. 
A single PW can be connected to a single 
serial/ds0-g703 port. The timeslots on the 
DS1 port are connected automatically in 
accordance with the rate defined on the 
serial/ds0-g703 port. 
Example. PW-TDM Cross-connection between PW 1 and Serial Port located on the same VS 
Module   
This section provides an example on creating a TDM pseudowire cross-connection between PW 1 and a 
serial port located on the same VS module. 
PW-TDM cross-connect between: 
• 
Pseudowire (PW) 1. 
• 
VS  module installed in slot 1, DS1 port 1, TS 1. 
DS0 cross-connect between: 
• 
VS  serial   module installed in slot 1, port 1. 
• 
VS  module installed in slot 1, DS1 port 1, TS 1.  
configure cross-connect pw-tdm pw 1 serial 1/1 time-slots 1 
Configuration Errors 
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 
8. Traffic Processing 
Cross-Connect Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
190 
Error 
ILLEGAL DEST SLOT/PORT 
CONNECTION 
 
One of the following conditions has been detected: 
• One or more module channels are connected to a 
disabled port (that is, a port configured to 
shutdown). 
• One or more module channels are connected to a 
port that cannot provide the required connection 
(for example, the port is connected to another I/O 
port). 
• For a tdm cross-connection: the port definitions 
are not symmetrical 
191 
Error 
ILLEGAL TIMESLOT 
ASSIGNMENT 
The required number of timeslots must be exactly the 
same as the number of timeslots assigned on the 
relevant module port 
192 
Error 
ILLEGAL CROSS CONNECT 
The number of timeslots routed between two module 
ports must be the same for both modules 
193 
Error 
TS-16 IS RESERVED FOR 
CAS SIGNALING 
To bypass signaling information between E1 ports on 
different modules, timeslot 16 of one module must 
be bound to timeslot 16 on the other module. Both 
ports must use G732S framing, with or without CRC-4 
(G732S, G723S-CRC4). 
194 
Error 
ILLEGAL POSITION OF TS 
BIT ASSIGNMENT 
When using split timeslot assignment: 
• 2-bit assignments must start at bit 1, 3, 5 and/or 
7. 
• 4-bit assignments must start at bit 1 and/or 5. 
Consecutive bits must be assigned to the same 
channel  
195 
Error 
TS ASSIGNMENT/TS 
REQUEST MISMATCH 
The timeslot bit assignment does not match the 
requirements for such timeslots 
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
196 
Error 
INCORRECT TS TYPE 
 
The definition of the timeslot must correspond to the 
type of information generated by the module using 
the timeslot:  
• Timeslot cross-connected to serial port: the type 
must be data (this also applies to timeslots cross-
connected to HSF modules). 
• Timeslot cross-connected to voice I/O module: the 
type must be voice. 
In addition, the types of timeslots cross-connected 
between links must be identical. 
197 
Warni
ng 
TS DATA TYPE DOESN’T 
MATCH B7ZS LINE CODE 
For T1 links, do not use the B7ZS line code when one 
or more timeslots are defined as data timeslots 
198 
Error 
ILLEGAL BROADCAST 
DEFINITION 
The ds0 cross-connect for the specified channel is not 
correct.  
199 
Error 
NOT COMPLETE 
BROADCAST DEFINITION 
The timeslot assignment for the specified port is not 
complete.  
203 
Error 
SPLIT TS BITS X-
CONNECTED TO DIFF SLOTS 
 
When configuring split timeslot assignment, shared 
bits of the same E1/T1 timeslot must be cross-
connected with serial/voice ports belonging to the 
same slot. 
204 
Error 
PORT IS UP BUT NOT X-
CONNECTED 
A port is set to “no shutdown”, but no E1/T1 timeslot 
is cross-connected with the port. 
205 
Error 
ILLEGAL TS DIRECTION 
One of the following:  
• If a timeslot  is assigned to a tdm-bridge port, its 
direction must be defined as either bidirection-rx 
or unidirection-rx (any other option is illegal). 
• If a serial port is set to conference mode, port 
timeslot direction must be bidirection-rx  
206 
Error 
ASYMMETRIC BI-DIR TS 
CROSS CONNECT 
When using bi-direction cross-connect between two 
e1/e1-i/t1/t1-i/ds1/ds1-opt ports, the command must 
be repeated in both directions. For example: 
config cr  
ds0 e1 1/2 ts [1..31]  e1-i 9/1 start-ts 1 data bi-
direction 
ds0 e1-i 9/1 ts [1..31]  e1 1/2 start-ts 1 data bi-
direction 
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
207 
Error 
XC OF VOICE TS WITH SIG 
IS NOT SUPPORTED 
 
When CL is CL2-DS0 or CL2-GBEA, some I/O module 
ports cannot be cross-connected to voice ports using 
cas or rbmf (robbed bit multiframe) signaling: 
• SH-16/E1/PW: DS1 ports 1-16 
• VS-6/E1T1: DS1 9-16  
• VS-16E1T1/PW:  E1/T1 9-16 and DS1 9-16. 
Note: For the voice port using “no signaling” or rbf 
(robbed bit frame) signaling, this cross-connect is 
possible.  
208 
Error 
DS0 CROSS CONNECTION IS 
ILLEGAL 
You are trying to configure DS0 cross-connection for 
the MLF-2E1 DS1-opt port. This port supports TDM 
cross-connect only.  
319 
Error 
 
ILLEGAL TDM CROSS 
CONNECT 
Unframed T1 port of M16T1 or T3 module cannot be 
cross-connected with T1-i port of CL module. 
320 
Error 
SPLIT TS IN 3BIT TRANS 
ENCAPSULATION MODE 
N/A” 
Split-ts assignment is illegal for a port configured with 
3-bit-transitional encapsulation.  
434 
Error 
PORT LINE TYPE 
MISMATCH 
TDM cross-connect on MLF-2E1 modules can be done 
only with E1/E1-i ports with the same line-type: 
g732n or g732n-crc. 
TDM cross connect on other modules can be done 
only for unframed E1/T1 ports. 
750  
 
 
Error 
 
NUM OF BI-DIRECTION-RX 
TS EXCEEDS 30 
The total number of timeslots on the VS module serial 
port or tdm-bridge port configured to bidirectional-rx 
cross-connect (bidirectional broadcast) cannot exceed 
30. 
751 
Error 
 
PORT IS UP BUT NOT 
BOUND TO SERIAL 
The tdm-bridge port is up but not bound to a serial 
port. 
 
752 
Error 
BOUND SERIAL PORT IS IN 
SHUTDOWN STATE 
The tdm-bridge port is bound to the serial port which 
is in shutdown state. 
753 
Error 
 
PORT IS BOUND TO 
MULTIPLE SERIAL PORTS 
The tdm-bridge port is bound to more than one serial 
ports. 
754 
Error 
 
ILLEGAL SERIAL SLOT/PORT 
BOUND 
The tdm-bridge port is bound to a serial port in 
another slot (the slot of the serial port and tdm-
bridge port bound to it must be the same). 
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
755 
Error 
 
ILLEGAL ENCAPSULATION 
MODE FOR BOUND PORT 
The serial port to which the tdm-bridge port is bound 
must be configured to 3-bit-transitional encapsulation 
mode. 
756 
Error 
 
PORT IS BOUND TO 
MULTIPLE TDM-BRIDGE 
PORTS 
The serial port is bound to more than one tdm-bridge 
ports. 
Viewing the Cross-Connect Summary  
You can view a summary of the cross connections configured in the system. 
 To view the cross-connections summary: 
• 
At the config>cross-connect# prompt, enter show summary followed by the options listed 
below. 
8. Traffic Processing 
Task 
Command 
Comments 
Display all DS0 connections in the system 
ds0 all 
 
 
Display all DS0 connections in the system 
for a specific port type 
ds0 port-type {e1 | t1 | e1-i | t1-i | ds1| ds1-
opt}  
 
 
Display all DS0 connections in the system 
for a specific port  
ds0 port-index {e1 | t1 | e1-i | t1-i | ds1| 
ds1-opt } <slot>/<port> 
 
Display all TDM connections in the 
system 
tdm all 
 
 
Display all TDM connections in the 
system for a specific port type 
tdm port-type {e1 | t1 | e1-i | t1-I | 
ds1 | ds1-opt} 
 
 
 
Display all TDM connections in the 
system for a specific port  
tdm port-index {e1 | t1 | e1-i | t1-i | 
ds1 | ds1-opt} [slot/]port[/tributary]  
 
Display all PW-TDM connections in the 
system 
pw all 
  
 
Display PW-TDM connections for a 
specific port  
pw number  <pw-num> 
 
 
Display all SDH-SONET connections in 
the system 
sdh-sonet all 
 
 
Display all SDH-SONET connections in 
the system for a specific VC/VT port type 
sdh-sonet vc-port-type  {vc12-vt2 | vc3-sts1 | 
vc4-sts3c}  
 
 
Display all SDH-SONET connections for a 
specific vc12-vt2  port  
sdh-sonet vc-port-type-and-index  vc12-vt2  
<vc-port-index> 
 
Display all SDH-SONET connections for a 
specific vc3-sts1  port  
sdh-sonet vc-port-type-and-index  vc3-sts1  
<vc-port-index> 
 
Display all SDH-SONET connections for a 
specific vc4-sts3  port  
sdh-sonet vc-port-type-and-index  vc4-sts3  
<vc-port-index> 
 
Example 1. Viewing all DS0 Connections in the System 
config>xc# show summary ds0 all 
DS0 XC 
----------------------------------------------------------------------------- 
8. Traffic Processing 
T1-I     cl-a/1   TS  1       BITS    Serial   3/1       TS           Data   Bi-
Direction 
T1-I     cl-a/2   TS  [1..2]  BITS    T1       3/2       TS  [1..2]   Data   Bi-
Direction 
T1-I     cl-a/2   TS  [3..5]  BITS    T1       3/2       TS  [3..5]   Voice  Bi-
Direction 
T1-I     cl-a/3   TS  1       BITS    Serial   3/2       TS           Data   Bi-
Direction 
T1-I     cl-a/4   TS  [1..4]  BITS    T1       3/4       TS  [1..4]   Data   Bi-
Direction 
T1-I     cl-a/4   TS  [5..6]  BITS    T1       3/4       TS  [5..6]   Voice  Bi-
Direction 
T1        3/2     TS  [1..2]  BITS    T1-I     cl-a/2    TS  [1..2]   Data   Bi-
Direction 
T1        3/2     TS  [3..5]  BITS    T1-I     cl-a/2    TS  [3..5]   Voice  Bi-
Direction 
T1        3/4     TS  [1..4]  BITS    T1-I     cl-a/4    TS  [1..4]   Data   Bi-
Direction 
T1        3/4     TS  [5..6]  BITS    T1-I     cl-a/4    TS  [5..6]   Voice  Bi-
Direction 
Example 2. Viewing all DS0 Connections in the System for T1-i Ports 
config>xc# show summary ds0 port-type t1-i 
DS0 XC 
----------------------------------------------------------------------------- 
T1-I     cl-a/1   TS  1       BITS    Serial   3/1       TS           Data   Bi-
Direction 
T1-I     cl-a/2   TS  [1..2]  BITS    T1       3/2       TS  [1..2]   Data   Bi-
Direction 
T1-I     cl-a/2   TS  [3..5]  BITS    T1       3/2       TS  [3..5]   Voice  Bi-
Direction 
T1-I     cl-a/3   TS  1       BITS    Serial   3/2       TS           Data   Bi-
Direction 
T1-I     cl-a/4   TS  [1..4]  BITS    T1       3/4       TS  [1..4]   Data   Bi-
Direction 
T1-I     cl-a/4   TS  [5..6]  BITS    T1       3/4       TS  [5..6]   Voice  Bi-
Direction 
 
Example 3. Viewing all TDM Connections in the System  
config>xc# show summary tdm all  
TDM XC 
DS1       7/3          E1        2/1 
E1-I      CL-A/4       E1        2/2 
E1        2/1          DS1       7/3 
E1        2/2          E1-I      CL-A/4 
 

## 8.3 Flows  *(p.686)*

8. Traffic Processing 
Example 4. Viewing all SDH/SONET Connections in the System for VC11  
config>xc# show summary sdh-sonet vc-port-type vc12-vt2  
 
SDH/SONET XC 
----------------------------------------------------------------- 
VC12    cl-a/1/1/3/1/1   E1-I    cl-a/1 
VC12    cl-a/1/1/3/1/3   E1-I    cl-a/2 
VC12    cl-a/1/1/3/7/4   E1-I    cl-a/3 
VC12    cl-a/1/1/3/7/2   E1-I    cl-a/4 
VC12    cl-a/1/1/3/1/2   E1       3/1 
VC12    cl-a/1/1/3/7/3   E1       3/3 
VC12    cl-b/1/1/3/2/3   E1-I    cl-b/1 
VC12    cl-b/1/1/3/1/3   E1-I    cl-b/2 
VC12    cl-b/1/1/3/7/4   E1-I    cl-b/3 
VC12    cl-b/1/1/3/7/2   E1-I    cl-b/4 
 
Example 5. Viewing all PW Connections in the System  
show summary pw all 
 
PW XC 
----------------------------------------------------------------- 
1     DS1              7/1        TS  : 1 
3     DS1              7/2        TS  : 2 
5     Serial           7/1        TS  : 0 
8.3 Flows  
Flows are the main traffic-carrying elements in Megaplex-4 architecture. They are unidirectional entities 
that interconnect two physical or logical ports. You can use classifier profiles to specify the criteria for 
flows. The classification is per port and is applied to the ingress port of the flow. 
Flows defined in Megaplex-4 can be unidirectional (between physical/logical ports) or bidirectional 
(between physical/logic ports and brigde ports of CL modules).  
Note 
Bridge ports in M-ETH modules are bound directly (without using flows).  
This section explains how to define the flows according to specific criteria such as VLAN. You can use 
classifier profiles to specify the criteria for flows. The classification is per port and is applied to the 
ingress port of the flow. 
8. Traffic Processing 
Applicability and Scaling 
Megaplex-4 supports up to 512 unidirectional Ethernet data flows, which can be used to provide E-line 
or E-LAN service delivery over Metro Ethernet networks. Each Ethernet flow connects two ports. 
Ethernet flows are unidirectional, or bidirectional in the case of bridge flows. For unidirectional flows, 
you have to define two flows between two ports, one for each direction. For bidirectional flows, you 
only need to define one flow from a port to a bridge port, and specify the reverse-direction command. 
Standards 
MEF 6 (E-Line – EPL and EVPL), MEF 10, MEF 9, MEF 14: EPL and EVPL, MEF 20, 
IEEE 802.3, 802.3u, 802.1q, 802.1p, 802.3ad, 802.3-2005  
Benefits  
The user traffic can be classified into different Ethernet flows (EVC.CoS) to provide services in a flexible 
manner, using better traffic management and QoS. 
Factory Defaults 
By default, no flows exist.  
Functional Description 
Ethernet Entities 
Ethernet services are provided by means of the Megaplex-4 I/O modules with traffic Ethernet ports, 
which can serve as customer’s edge network interfaces, and by means of the CL.2 and M-ETH modules, 
which provide GbE ports that can serve as service provider’s edge interfaces. 
The customer’s edge traffic accepted by Ethernet ports on I/O modules is directed to other interfaces 
that can transfer the traffic to the transport network. These interfaces are as follows: 
• 
GbE ports located on the Megaplex-4 CL.2 modules (ethernet or lag in the CLI language) and on 
the M-ETH modules (ethernet in the CLI language).  
8. Traffic Processing 
• 
Logical MAC ports (logical-mac). A Logical MAC port is bound to a gfp or hdlc port, which, in its 
turn, should be bound to the physical layer. The meaning of the gfp or hdlc ports and their 
further mapping depends on the Ethernet traffic media:  
 
GFP ports represent VCGs (Virtual Concatenation Groups) with GFP encapsulation and exist 
in two flavors: 
 
GFP ports defined on CL.2 modules and used for efficient transport of Ethernet traffic 
over the SDH/SONET networks. GFP ports can be mapped either directly to the physical 
layer or to VCG. In the latter case the binding is done in two stages and this VCG should 
be further bound to the physical layer. 
 
GFP ports located on T3 modules and used for efficient transport of Ethernet traffic over 
the T1/T3 networks. GFP ports are mapped either directly to the physical layer or to 
VCG. In the latter case, the binding is done in two stages and the VCG is further bound 
to the physical layer. 
 
HDLC ports defined on CL.2 modules represent VCGs (Virtual Concatenation Groups) with 
LAPS encapsulation. They can be mapped either directly to the physical layer or to another 
VCG. In the latter case the binding is done in two stages and this VCG should be further 
bound to the physical layer  
• 
A switched virtual interface (SVI) is a VLAN of switch ports represented by one interface to a 
routing or bridging system. There is no physical interface for the VLAN, and the SVI provides this 
interface for VLANs participating in management and PW traffic.  
 
In Megaplex-4 management, an SVI port is an intermediate Ethernet entity between the 
Bridge/Router and another Ethernet port (bound one-to-one) providing the Layer 3 
processing for packets from all switch ports associated with the VLAN. It also serves as an 
ingress or egress port for terminating management flows. The flow is configured between 
the physical port, which is the management source, and the corresponding SVI port bound 
to the bridge port. This flow will classify the management traffic to be forwarded to the 
bridge port. For illustration, see Example under Management Bridge in Chapter 8. There is 
one-to-one mapping between a VLAN and SVI, thus only a single SVI can be mapped to a 
VLAN. 
 
PW traffic created in the Megaplex-4 is switched to the external network via flows with SVI 
as one of the flow endpoints. Same SVI can share multiple PW’s with a VLAN-based 
classifier, defined in the PW menu. 
The incoming Ethernet traffic is forwarded to a bridge port based on the flow configured between the 
above entity and a bridge port. Then it is switched between bridge ports inside the bridge based on MAC 
and VLAN (IVL) switching. The last stage is forwarding traffic from the other bridge port to the other 
entitiy via a flow. 
8. Traffic Processing 
Aware and Unaware Traffic  
In general, a given bridge port can serve as the termination point of several flows (the maximum 
number of traffic flows that can be defined on a Megaplex-4 is 512). Therefore, each flow must 
discriminate among the Ethernet frames (be aware of the frame VLANs) reaching an associated bridge 
port in order to determine how to handle customers’ edge traffic. In general, this action is based on the 
user’s VLAN identifier (VLAN ID) received in each frame. For untagged or priority-tagged traffic, a special 
VLAN ID is automatically assigned by the Megaplex-4 for handling the Ethernet traffic.  
The range of specific VLAN IDs that can be used for Ethernet traffic with IEEE 802.1Q tags is 1 to 4094 
(for the management flow on non-A CL.2 options, only the range of 1 to 3999 is allowed).  
Note 
When working with CL.2 (non-A) options, ingress VLAN ID within the 3800-
4095 VLAN ID range may not be filtered.  
The internal Ethernet switch of the module can also handle other types of frames, such as untagged 
frames, and priority-tagged frames (frames with IEEE 802.Q tags with 0 as the VLAN ID). Megaplex-4 
modules also enable the user to configure flows to handle traffic with or without IEEE 802.Q tags: this 
traffic is forwarded only between the bridge ports mapped to a given flow. This forwarding mode is 
usually referred to as VLAN-unaware. In order to transmit unclassified frames, its classification should be 
set to ‘match-all’. 
The following list summarizes the configuration restrictions applying to the types of flows to which any 
given bridge port can be mapped: 
• 
A bridge port can terminate only one flow classified as unaware (i.e., which does not 
discriminate Ethernet traffic in accordance with VLANs). 
• 
When a bridge port is mapped to more than one flow, the bridge port can terminate several 
flows with specific VLAN IDs, but only one flow classified as unaware. 
• 
A bridge port can terminate flows with different VLAN IDs (aware flow mode).  
VLAN tagging, stacking and striping options enable transporting users’ traffic transparently, thereby 
keeping all the user’s VLAN settings intact.  
Tagging and Marking 
Megaplex-4 supports several options for marking and tagging.  
You can perform the following marking actions: 
• 
Overwrite inner or outer VLAN with a new value  
• 
Overwrite inner or outer VLAN p-bit with a new value. 
8. Traffic Processing 
You can perform the following tagging actions: 
• 
Add (push) outer VLAN, with p-bit value that can be copied from the original value or set to a 
new value. When you add a new VLAN, the original outer VLAN becomes the inner VLAN. 
• 
Remove (pop) outer VLAN and p-bit. When you remove a VLAN, the inner VLAN becomes the 
outer VLAN. 
• 
Add (push) inner VLAN, with p-bit value that can be copied from the original value or set to a 
new value 
• 
Remove (pop) inner VLAN and p-bit. 
Only certain combinations of actions on the outer and inner VLAN are allowed. Refer to Packet Editing 
on Reverse Flows for details on the permitted combinations of actions.  
Defining Classifier Profiles  
You can define up to 128 classifier profiles to apply to flows to ensure the desired flow classification.  
Note 
When a classification profile is assigned to a flow, each match in the profile is 
allocated one of the 1000 available internal classification match entries, 
according to the flow ingress port.  
For example, if a classification profile is defined with matches to two different 
VLANS, then if the profile is assigned to two flows that use different ingress 
ports, the result is that four internal classification match entries are allocated. 
If the profile is assigned to two flows that use the same ingress port, the result 
is that two internal classification match entries are used.  
 To define a classifier profile: 
1. Navigate to the flows context (config>flows). 
2. Define a classifier profile and assign a name to it: 
classifier-profile <profile-name> match-any 
The system switches to the context of the classifier profile (config>flows>classifier-
profile(<profile-name>)). 
3. Specify the criteria for the classifier profile:  
[no] match [ vlan <vlan-range> ] [ inner-vlan <inner-vlan-range> ] [ p-bit <p-bit-range> ] 
[ inner-p-bit <inner-p-bit-range> ] [ ip-precedence <ip-precedence-range> ] 
[ ip-dscp <ip-dscp-range> ] [ether-type <ether-type>] [untagged] [non-ip] [all]  
 
8. Traffic Processing 
Note 
The ‘vlan range’ classification is not applicable in the case when a bridge is 
configured. 
 
4. When you have completed specifying the criteria, enter exit to exit the classifier profile context. 
Examples: 
 To create classifier profile with criteria VLAN 100 to VLAN 150: 
exit all 
configure flows classifier-profile v100_150 match-any 
match vlan 100..150 
exit all 
 To create classifier profile with criteria VLAN 20 and inner VLAN 30: 
exit all  
configure flows classifier-profile v20_inner_30 match-any 
match vlan 20 inner-vlan 30 
exit all 
 To create classifier profile that matches all criteria: 
exit all  
configure flows classifier-profile all match-any 
match all 
exit all 
Configuring Flows  
 To create and configure a flow: 
1. Navigate to the flows context (config>flows). 
2. Define a flow and assign a name to it: 
flow <flow-name> 
The system switches to the respective flow context (config>flows>flow(<flow-name>)) 
3. Specify the flow as explained in the table below.  
8. Traffic Processing 
Task 
Command 
Comments 
Administratively enabling 
the flow (the flow is created 
as inactive by default) 
no shutdown 
You can activate a flow only if it is 
associated with at least a classifier 
profile, ingress port, and egress 
port. 
Using shutdown disables the flow  
Mapping the previously 
configured classifier profile 
to the flow 
classifier-profile <classifier-
profile name> 
no classifier removes the mapping 
Specifying the egress port 
(ethernet, lag, logical-mac,  
svi), the egress queue block 
and the queue (or queue 
map profile) within the block  
 
egress-port {ethernet | logical-
mac } <slot/port> [queue-map-
profile  <queue-map-profile-
name> block 
<level_id/queue_id>] 
egress-port {ethernet | logical-
mac} <slot/port> [<tributary>] 
[queue  <queue-id> block 
<level_id/queue_id>] 
egress-port lag <port-number> 
[queue-map-profile <queue-
map-profile-name> block 
<level_id/queue_id>] 
egress-port lag <port-number>  
[queue  <queue-id> block 
<level_id/queue_id>] 
egress-port  bridge-port 
<slot><port> (Note: if ingress-
port is a port of I/O module, see 
reverse-direction  command 
below)  
egress-port  {svi } <port 
number> 
egress-port mng-ethernet 
<slot/port>  
 
All VLANs defined on the same 
egress bridge port must use the 
same queue-map-profile and 
block values.  
no egress-port removes the flow 
association with the egress port 
When working with 2 non-A CL 
modules,  a flow between ingress-
port=logical mac and egress-
port=lag cannot be set. 
Local switching (flows between 
Ethernet ports on the same 
module) is possible in the following 
cases: 
• Within the I/O modules with FE 
ports in systems equipped with 
CL.2/A modules  
• Within the M-ETH module in 
systems equipped with any CL.2 
modules 
8. Traffic Processing 
Task 
Command 
Comments 
Specifying the opposite flow, 
the egress queue block and 
the queue (or queue map 
profile) within the block 
reverse-direction [queue-map-
profile  <queue-map-profile-
name> block 
<level_id/queue_id>] 
reverse-direction [queue  
<queue-id> block 
<level_id/queue_id>] 
reverse-direction is used in the 
following cases: 
• When egress-port is bridge-port 
and ingress-port is a port of I/O 
module. 
• When configuring a PWE flow 
connected to a bridge. An 
alternative to this is configuring 
two consecutive uni-directional 
flows without other non-related 
flows in between. 
Specifying the ingress port 
(ethernet, lag, logical-mac,  
svi) 
ingress-port ethernet 
<slot><port> 
ingress-port {logical-mac | 
bridge-port} <slot><port> 
ingress-port  {svi | lag } <port 
number> 
ingress-port mng-ethernet 
<slot/port> 
  
no ingress-port removes the flow 
association with the ingress port 
When working with 2 non-A CL 
modules,  a flow between ingress-
port=logical mac and egress-
port=lag cannot be set.  
Local switching (flows between 
Ethernet ports on the same 
module) is possible in the following 
cases: 
• Within the I/O modules with FE 
ports in systems equipped with 
CL.2/A modules  
• Within the M-ETH module in 
systems equipped with any CL.2 
modules 
Associating the flow with a 
policer profile  
policer-profile <policer-profile-
name> 
no policer removes the flow 
association with the policer 
Discarding traffic 
transmitted via the flow 
drop  
 
Defining marking actions for 
the flow such as overwriting 
the VLAN ID or inner VLAN 
ID or setting the priority 
mark all 
 
Refer to the following table for the 
marking actions 
8. Traffic Processing 
Task 
Command 
Comments 
Adding VLAN ID with p-bit 
set to specific value, and 
optionally adding inner 
VLAN ID with p-bit set to 
specific value 
vlan-tag push vlan <sp-vlan> 
p-bit fixed <fixed-p-bit> 
[inner-vlan <inner-sp-vlan> 
p-bit fixed <inner-fixed-p-bit>] 
 
Adding VLAN ID with p-bit 
set to specific value, and 
optionally adding inner 
VLAN ID with p-bit set via 
marking profile 
vlan-tag push vlan <sp-vlan> 
p-bit fixed <fixed-p-bit> [inner-
vlan <inner-sp-vlan> 
p-bit profile <inner-marking-pr
ofile-name>] 
 
Adding VLAN ID with p-bit 
set to specific value, and 
optionally adding inner 
VLAN ID with p-bit set by 
copying from the incoming 
frame 
vlan-tag push vlan <sp-vlan> p-
bit fixed <fixed-p-bit> [inner-
vlan <inner-sp-vlan> p-bit 
copy]  
 
Adding VLAN ID with p-bit 
set via marking profile, and 
optionally adding inner 
VLAN ID with p-bit set to 
specific value 
vlan-tag push vlan <sp-vlan> 
p-bit profile <marking-profile-n
ame> 
[inner-vlan <inner-sp-vlan> 
p-bit fixed <inner-fixed-p-bit>] 
 
Adding VLAN ID with p-bit 
set via marking profile, and 
optionally adding inner 
VLAN ID with p-bit set via 
marking profile 
vlan-tag push vlan <sp-vlan> 
p-bit profile <marking-profile-n
ame> 
[inner-vlan <inner-sp-vlan> 
p-bit profile <inner-marking-pr
ofile-name>] 
 
Adding VLAN ID with p-bit 
set via marking profile, and 
optionally adding inner 
VLAN ID with p-bit set by 
copying from the incoming 
frame 
vlan-tag push vlan <sp-vlan> 
p-bit profile <marking-profile-n
ame> 
[inner-vlan <inner-sp-vlan> 
p-bit copy]  
 
Adding VLAN ID with p-bit 
set by copying from the 
incoming frame, and 
optionally adding inner 
VLAN ID with p-bit set to 
specific value: 
vlan-tag push vlan <sp-vlan> 
p-bit copy 
[inner-vlan <inner-sp-vlan> 
p-bit fixed <inner-fixed-p-bit>] 
 
8. Traffic Processing 
Task 
Command 
Comments 
Adding VLAN ID with p-bit 
set by copying from the 
incoming frame, and 
optionally adding inner 
VLAN ID with p-bit set via 
marking profile 
vlan-tag push vlan <sp-vlan> 
p-bit copy 
[inner-vlan <inner-sp-vlan> 
p-bit profile <inner-marking-pr
ofile-name>] 
 
Adding VLAN ID with p-bit 
set by copying from the 
incoming frame, and 
optionally adding inner 
VLAN ID with p-bit set by 
copying from the incoming 
frame 
vlan-tag push vlan <sp-vlan> 
p-bit copy 
[inner-vlan <inner-sp-vlan> 
p-bit copy]  
 
Removing VLAN ID, and 
optionally removing inner 
VLAN ID 
vlan-tag pop vlan [inner-vlan] 
 
 
Removing pushing of inner 
VLAN 
no vlan-tag [push inner-vlan] 
 
Administratively enabling 
the flow 
no shutdown 
• You can activate a flow only if it 
is associated with at least a 
classifier profile, ingress port, 
and egress port 
• Flows are created as inactive by 
default 
• Type shutdown to disable the 
flow 
The following marking actions can be performed in the mark level, at the 
config>flows>flow(<flow-name>)>mark# prompt. 
8. Traffic Processing 
Task 
Command 
Comments 
Overwriting p-bit 
according to marking 
profile 
marking-profile 
<marking-profile-name> 
If a marking profile is used, it must be 
compatible with the classification criteria 
of the flow, e.g. if the flow classification is 
according to DSCP then the marking 
classification should not be according to p 
bit 
If a color-aware marking profile is applied 
for the outer VLAN of a flow, then if 
marking is applied to the inner VLAN, 
either the same color-aware marking 
profile must be used for the inner VLAN, 
or a non-color-aware marking profile 
must be used for the inner VLAN. 
Typing no marking-profile or 
no inner-marking-profile removes the 
overwriting of marking profile or inner 
marking profile respectively 
Overwriting inner p-bit 
according to marking 
profile 
inner-marking-profile 
<inner-marking-profile-name
> 
See comments for marking-profile 
Overwriting p-bit with a 
new value 
p-bit <p-bit-value> 
Typing no p-bit removes the overwriting 
of p-bit 
Overwriting inner p-bit 
with a new value 
inner-p-bit 
<inner-p-bit-value > 
Typing no inner-p-bit removes the 
overwriting of inner p-bit 
Overwriting VLAN ID with 
a new value 
vlan <vlan-value> 
Typing no vlan removes the overwriting 
of VLAN ID 
Overwriting inner VLAN ID 
with a new value 
inner-vlan <inner-vlan-
value> 
Typing no inner-vlan removes the 
overwriting of inner VLAN ID 
Exiting the marking 
context and returning to 
the flow context 
exit 
 
For examples see Configuring the Bridge section below: bridge configuration examples include flow 
configuration as well. 
8. Traffic Processing 
Configuration Errors 
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 
Code 
Type 
Syntax 
Meaning 
559 
Error 
INGRESS AND EGRESS PORTS 
ARE MEMBERS OF THE SAME 
BRIDGE 
Ingress and egress ports of a flow cannot both be bridge 
ports of the same bridge. 
560 
Error 
UP TO 240 FLOWS FOR DATA 
The maximum number of unidirectional flows for data for 
CL.2 (non-A option) is 240.  
561 
Error 
UP TO 192 FLOWS FOR 
MANAGENENT 
The maximum number of management flows for CL.2 
(non-A option) is 192. 
562 
Error 
FLOW MUST CONSIST OF 
TWO PORTS 
Flow must connect 2 ports. 
563 
Error 
SAME INGRESS AND EGRESS 
PORTS 
Ingress and egress ports must be different. 
 
564 
Error 
FLOW MUST HAVE A 
CLASSIFIER 
A classifier profile must be bound to the flow. 
565 
Error 
FLOW BETWEEN TWO SVI 
NOT ALLOWED 
A flow cannot connect between 2 SVI ports. 
 
566 
Error 
CL L. MAC CAN’T BE MEMBER 
IN MNG FLOW 
A Logical MAC with a VCG bound to it cannot be a member 
in a management flow 
567 
Error 
ILLEGAL FLOW BETWEEN ETH 
PORTS 
A flow between external or internal Ethernet ports on the 
same I/O slot is not allowed. 
568 
Error 
CLASSIFIER PROFILE MUST BE 
MATCH ALL 
If an ingress port is SVI bound to BP (management flow), 
the classifier must be “match all”. 
569 
Error 
MNG VLAN MUST BE LESS 
THAN 4000 
When working with CL.2 module option, management flow 
VLAN ID must be less than 4000 (not relevant for CL.2/A 
option). 
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
570 
Error 
ILLEGAL CLASSIFIER FOR PORT 
The selected classification is not supported by this port. 
Correction required according to the following: 
• Command match vlan inner-vlan is valid only for flows 
between GbE and/or LAG ports defined on CL modules 
• Commands match vlan inner-vlan or match vlan are 
obligatory for flows between GbE and/or LAG ports 
defined on CL modules, no other classifier can be used 
on these ports 
• I/O port classifier can be only match vlan or match all.  
571 
Error 
VLAN TAG ACTION PUSH NOT 
ALLOWED 
VLAN tag push action is not allowed in the following cases: 
• At egress port of flows between GbE and/or LAG ports 
defined on CL modules  
• On ports of I/O modules participating in non-
management (data) flows. 
572 
Error 
VLAN TAG ACTION POP NOT 
ALLOWED 
VLAN tag pop action is not allowed in the following cases: 
• At egress ports of flows using classifier match all 
• When both ends of the flow reside on the same I/O slot 
• When both ends of the flow reside on GbE or LAG ports 
defined on CL modules  
573 
Error 
VLAN ACTION MUST BE POP 
Pop action is obligatory in the following cases: 
• Egress port is SVI bound to a bridge port (management 
flow)  
• Ingress port has inner VLAN as classifier (used only in 
Logical macs defined on CL), and egress port is GBE or 
LAG  
If one of these cases is yours, define VLAN pop action. 
574 
Error 
VLAN ACTION MUST BE PUSH 
Push action is obligatory in the following cases: 
• Ingress port is SVI bound to a bridge port (management 
flow).  
• I/O or CL Logical-mac classifier is ‘match all’ (push VLAN 
must be added at the egress GBE/LAG port). 
If one of these cases is yours, define VLAN push action. 
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
575 
Error 
CLASSIFIER/PUSHED 
VLAN/P-BIT MUST BE THE 
SAME 
 
Pay attention to one of the following: 
• All the flows where egress port is SVI bound to bridge 
port (management flow) must have the same VLAN 
number in classifier 
• All the flows where ingress port is SVI bound to bridge 
port (management flow) must have the same push vlan 
number and p-bit value. 
• The VLAN number in classifier must be identical to the 
push vlan number. 
If the mentioned numbers/values are not the same, 
correct according to the above. 
576 
Error 
MANAGEMENT FLOW MUST 
BE BI-DIRECTIONAL 
When a management flow is configured and SVI bound to 
a bridge port is its egress port, another flow (with SVI 
bound to the bridge port as ingress port) must be 
configured and vice versa. In addition, this SVI cannot 
participate in another flow. 
577 
Error 
VLAN CAN'T BE REPEATED 
BTW CL ETH/LAG PORTS 
 
Pay attention to the following: 
• For non-management (data) flows the classifier profile 
VLAN of each GbE/LAG port defined on CL module 
must be unique. (Note: This is not relevant in case 
when both flow ends reside on GbE/LAG ports defined 
on CL module). 
• For the flows with classifier based on outer&inner 
VLAN, the inner VLAN can’t be repeated on GbE/LAG 
ports defined on CL module 
• Push SP-VLAN cannot be repeated on GbE/LAG ports 
defined on the same CL module 
If your case is different, correct according to the above. 
578 
Error 
FLOWS BETWEEN PORTS 
CAN’T BE SPLIT 
If ingress port of several flows is the same I/O port, the 
egress ports of these flows cannot be different. 
579 
Error 
VLAN ID IS UNIQUE PER SLOT 
VLAN ID (number) must be unique per slot (except for the 
management flows) 
580 
Error 
ONLY SINGLE FLOW IS 
ALLOWED FOR MATCH ALL 
If the classifier is 'match all', only a single flow is allowed 
for the port. 
582 
Error 
CLASSIFIERS CONFLICT ON 
PORT  
All flows terminating on a specific port must use the same 
classifier criteria. 
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
584 
Error 
NUMBER OF OUTER VLAN’S 
ON PORT OUT OF RANGE 
 
When the classifier on a GBE or LAG port is match vlan 
inner-vlan, only up to 4 different VLANs (outer VLANs) can 
be configured per port. In addition, the inner VLAN IDs 
should be different from (outer) VLAN IDs.  
585 
Error 
FLOW CONNECTED TO PORT 
IN SHUTDOWN STATE 
Flow can be connected to ports only in ‘no shutdown’ 
state. 
586 
Error 
ILLEGAL FLOW WHEN PORT 
MEMBER IN MNG FLOW  
A local flow (a flow within the same module) cannot be 
started/terminated on an SVI port bound to the 
management router.  
587 
Warnin
g 
SUM OF POLICERS RATE 
EXCEED SUPPORTED BW  
The total sum of bandwidths defined in policer profiles for 
all 8 ports of the M-ETH module must not exceed 1 GbE. 
588 
Error 
INCORRECT POLICER 
PARAMETERS       
The values of cbs/cir/ebr/eir parameters defined for 
bandwidth do not satisfy one of the conditions listed in 
the configuration table under Configuring Policer 
Profiles. 
589 
Error 
ILLEGAL FLOW BETWEEN 
GBE/LAG PORTS 
 
The following flows are iilegal: 
• Between two GbE ports (on CL module) 
• Between two LAGs  
• Between a LAG and a GbE port (on CL module)  
590 
Error 
VLAN 4000 IS ILLEGAL FOR 
DATA PORTS 
Data flow VLAN ID cannot take the value of 4000 
  
591 
Error 
UP TO 512 FLOWS FOR DATA 
For CL.2/A the maximum number of unidirectional flows is 
512. 
592 
Error 
FLOW EDITING NOT 
SUPPORTED 
The editing is not according to allowed VLAN editing 
options   
593 
Error 
ONE LEVEL 0 BLOCK 
ALLOWED 
The maximum number of level-0 queue blocks on a VCG 
port is 1 
594 
Error 
UP TO 8 LEVEL 0 BLOCKS 
ALLOWED 
The maximum number of level-0 queue blocks on the GbE 
port of CL module is 8 
597 
Error 
ERP VLAN AND CLASSIFIER 
CONFLICT 
The same VLAN cannot be defined for data and R-APS 
messages. 
598 
Error 
FLOW CONNECTED TO AN 
UNDEFINED PORT 
The ingress or egress port of the flow  do not exist 
anymore (for example, the corresponding svi port was 
deleted). 
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
599 
Error 
CLASSIFIER IS UNIQUE PER 
INGRESS SLOT/PORT 
You cannot use the same classifier for two different flows 
on the same port. 
Viewing the Flow Summary  
You can display a brief or detailed summary of all flows that exist in the system. 
 To display brief flow summary: 
• 
In the config>flows# prompt, enter show summary brief. 
The brief flow summary is displayed. 
config>flows# show summary brief  
Name                              Ingress                Tx 
Admin | Oper | Classification     Egress                 Rx 
 
LM_CLA                            Logical MAC  cl-a/1     0 
Ena | Up | v1000                  Bridge port  1 1        0 
 
 
LM_CLA                            --                      0 
Ena | Up |                        --                      0 
 
 
LM_CLA2                           Logical MAC  cl-a/1     0 
Ena | Up | v100                   Bridge port  1 1        0 
 
 
LM_CLA2                           --                      0 
Ena | Up |                        --                      0 
 
 
LM_CLB                            Logical MAC  cl-b/1     0 
Ena | Up | v1000                  Bridge port  1 2        0 
 
 
LM_CLB                            --                      0 
Ena | Up |                        --                      0 
 
 
LM_CLB2                           Logical MAC  cl-b/1     0 
Ena | Up | v100                   Bridge port  1 2        0 
 
 
LM_CLB2                           --                      0 
Ena | Up |                        --                      0 
8. Traffic Processing 
 
 
EMS_ETH                           Ethernet      1/1       0 
Ena | Down | All                  Bridge port  1 3        0 
 To display detailed flow summary: 
• 
In the config>flows# prompt, enter show summary details. 
config>flows# show summary details 
 
Name             : LM_CLA 
Type             : Based 
Admin Status     : Up 
Oper Status      : Up 
Test             : Off 
Classifier       : v1000 
Policer          : Policer1 
Rx Total Packets : 0 
Tx Total Packets : 0 
 
Ingress Port : Logical MAC  cl-a/1 
Egress Port  : Bridge port  1 1 
 
 
 
Name             : LM_CLA 
Type             : Reverse 
Admin Status     : Up 
Oper Status      : Up 
Test             : Off 
Classifier       : 
Policer          : Policer1 
Rx Total Packets : 0 
Tx Total Packets : 0 
 
Ingress Port : -- 
Egress Port  : -- 
 
 
 
Name             : LM_CLA2 
Type             : Based 
Admin Status     : Up 
Oper Status      : Up 
Test             : Off 
Classifier       : v100 
Policer          : Policer1 
Rx Total Packets : 0 
Tx Total Packets : 0 
8. Traffic Processing 
Testing the Flows  
The Megaplex flows can be tested by independently activating a loop per each specific flow as shown in 
the diagram below. The test can be performed on any Ethernet-based port of Megaplex-4. 
 
 
Megaplex-4
CL
ETH Engine
GbE
Network
3rd Party Product
Traffic 
Generator
Traffic 
Counter
 
Loopback per Flow  
In addition, CL.2/A modules feature loopbacks on flows with exchange of source and destination MAC 
addresses of incoming packets, as shown in the following diagram. This applies to all the data associated 
with the flow. This test is supported only on flows where the ingress port is CL.2/A GbE port or M-ETH 
GbE port and applied over a dedicated configured flow with a test mac-swap attribute.  
Note 
When mac-swap is specified, if there is an IP header in the frames, then MACs 
are swapped while IP addresses are not.  
MP-4
CL.2
ETH Engine
Network
GbE
Classifier
Flows
Traffic 
Counter
Traffic 
Generator
  
Loopback per Flow with MAC Swap towards the Network Side (NNI) 
8. Traffic Processing 
MP-4
CL.2
ETH Engine
Network
GbE
Classifier
IO
Flows
Traffic 
Counter
Traffic 
Generator
 
Loopback per Flow with MAC Swap towards the I/O Port/User Side (UNI)   
 To perform a test on a flow with MAC swap: 
1. Create a flow.  
2. Navigate to configure flows flow <flow-name> to select the above flow. 
The config>flows>flow(<flow-name>)# prompt is displayed. 
3. Set the flow to “no shutdown”. 
4. Enter:  
test mac-swap  
The flow is activated, and the TEST LED is turned on. The test duration is infinite. 
 To display the test status:  
1. Navigate to the config>flows>flow(<flow-name>) prompt. 
2. Type show test. 
3. The display shows the following: 
• 
The test status: Off or MAC Swap  
• 
Test duration: Forever, always displayed in the current version. 
• 
No TTL – “no time to leave”, always displayed in the current version. 
Example 1. 
config>flows>flow(2)$ show test 
Test : MAC Swap   Forever No TTL 
Example 2. 
config>flows>flow(1)# info 
    classifier "all" 
    policer profile "Policer1" 
    ingress-port ethernet cl-a/1 
    egress-port ethernet 1/1 
    no shutdown 
8. Traffic Processing 
config>flows>flow(1)# test mac-swap 
 To end the test: 
1. Navigate to configure flows flow <flow-name> to select the flow being tested. 
The config>flows>flow(<flow-name>)# prompt is displayed. 
2. Enter:  
no test. 
Alternatively, you can delete the flow on which the test is based. 
Displaying Flow Statistics  
You can display the number of forwarded and discarded packets and bytes for a flow. 
 To display the statistics for a flow: 
• 
At the relevant flow context (config>flows>flow(<flow-id>)), enter: 
show statistics running. 
Flow statistics are displayed.  
 To clear the statistics for a flow: 
• 
At the relevant flow context (config>flows>flow(<flow-id>)), enter: 
clear-statistics. 
The statistics for the flow are cleared. 
For example: 
 To display flow statistics: 
# configure flows flow f10_out 
config>flows>flow(f10_out)# show statistics running 
Rate Sampling Window 
----------------------------------------------------------------------------- 
Window Size [Min.]        : 15 
Window Remain Time [Min.] : 12 
 
Rx Statistics 
----------------------------------------------------------------------------- 
          Total 
Packets : 0 
Bytes   : 0 

## 8.4 Peer  *(p.706)*

8. Traffic Processing 
 
Drop Statistics 
----------------------------------------------------------------------------- 
 
               Packets              Bytes 
Total        : 0                    0 
Green        : 0                    0 
Yellow       : 0                    0 
Red          : 0                    0 
Total(Rate)  : 0                    0 
Green(Rate)  : 0                    0 
Yellow(Rate) : 0                    0 
Red(Rate)    : 0                    0 
 
Tx Statistics 
----------------------------------------------------------------------------- 
             Total                Green                Yellow 
Packets    : 0                    0                    0 
Rate [pps] : 0                    0                    0 
Bytes      : 0                    0                    0 
Rate [bps] : 0                    0                    0 
 
Peak Measurement 
----------------------------------------------------------------------------- 
                      Min.         Max. 
Tx Bit Rate [bps]   : 0            0 
Drop Bit Rate [bps] : 0            0 
8.4 Peer  
Remote devices that serve as destinations for pseudowire traffic are referred to as peers. 
Applicability and Scaling 
You can define up to 100 peers. 
Factory Defaults 
No peers exist by default. 
8. Traffic Processing 
Benefits 
Peers serve as destinations for pseudowire connections for transporting a TDM payload over packet-
switched networks. 
Functional Description 
Peers are remote devices operating opposite router interfaces. These devices serve as destinations for 
pseudowire connections for transporting a TDM payload over packet-switched networks. You can define 
up to 100 peers, each assigned a unique index number. The index number is then used to specify the 
pseudowire destination, instead of directly providing the necessary destination information. 
To configure a UDP/IP peer, it is necessary to provide its IP address, and as an option – the next hop IP 
address (if the peer IP address is not within a router interface subnet).  
For MEF-8 peers, you must specify the either an IP address or a MAC address of the destination device.  
When the MEF-8 peer is a MAC address, the central Megaplex device is configured with a static MAC. In 
this case when the remote device fails needs to be replaced with a different device (with different MAC), 
the peer must be reconfigured with the new MAC to start working. 
When the MEF-8 peer is an IP address, the VS module learns the remote MAC by ARPs, and the remote 
device failure does not require reconfiguring the peer. 
Adding and Configuring Remote Peers  
Peers are remote devices operating opposite router interfaces. These devices serve as destinations for 
pseudowire connections for transporting a TDM payload over packet-switched networks. You can define 
up to 100 peers. 
 To add a remote peer:  
• 
At the config>peer # prompt, type the peer number in the range of 1 to 100.  
 To configure a remote peer: 
• 
At the config>peer (peer number) # prompt, enter all necessary commands according to the 
tasks listed below:  
8. Traffic Processing 
Task 
Command 
Comments 
Defining IP address of a 
remote peer in IP/UDP, MPLS 
or MEF-8 Ethernet networks  
ip <valid IP address> 
 
Assigning a name to a remote 
peer 
name <alphanumeric string > 
 
Specifying the IP address of 
the next port to which packets 
directed to the selected peer 
will be sent 
 
next-hop-ip <valid IP 
address> 
 
You need to specify a next hop IP 
address only when the peer IP 
address is not within the IP subnet of 
the router interface that will be used 
to send packets to this peer.  
The default value, 0.0.0.0, means 
that no next hop IP address is 
defined 
Note: If you need to change the next 
hop, first delete the peer and then 
reconfigure it again. 
Defining MAC address of a 
remote peer in MEF-8 
Ethernet networks 
mac<valid MAC address> 
 
 To remove a remote peer:  
• 
At the config>peer (peer number) # prompt, type no peer (peer number).  
Note 
Setting remote peers as destinations is done under configure pwe context.  
Viewing the Remote Peer Summary  
You can view a summary of the remote peers configured in the system, both IP- and MAC-based. 
 To view the remote peer summary: 
• 
At the config# prompt, enter show peer-summary. 
The summary of all configured remote peers appears. 
config# show peer-summary 
 
Number : 1 
Name   : Peer 1 
8. Traffic Processing 
MAC    : 00-01-02-03-04-05 
 
Number : 2 
Name   : Peer 2 
IP     : 172.17.173.23 
Examples  
 To configure remote peer 1 for UDP/IP PSN:  
• 
IP address: 9.9.9.9 
• 
Next hop IP address: 0.0.0.0 
• 
Name: peer1. 
configure peer 1 ip 9.9.9.9 name peer1 next-hop-ip 0.0.0.0 
 To configure remote MAC peer 1 for MEF-8 PSN: 
• 
MAC address: 00-20-d6-54-bf-05 
• 
Name: peer2. 
configure peer 1 mac 00-20-d6-54-bf-05 name peer2  
 To configure remote IP peer 1 for MEF-8 PSN: 
• 
IP address: 9.9.9.9 
• 
Name: peer2. 
configure peer 1 ip 9.9.9.9 name peer2  
 To delete remote peer 1:  
config# no peer 1 
Configuration Errors 
See Pseudowire Configuration Error Messages. 

## 8.5 Pseudowires  *(p.710)*

8. Traffic Processing 
8.5 Pseudowires  
Pseudowires are an emulation of Layer-2 point-to-point connection-oriented services over packet-
switching networks (PSN). In Megaplex-4, they are available for VS and TP modules. 
Packet formats can be selected on a per-pseudowire basis for optimal transmission over UDP/IP, MPLS- 
or Ethernet-based networks. Each pseudowire can be independently routed to any destination.  
The following user-configurable protocols are supported, independently for each pseudowire:  
• 
CESoPSN (structure-aware TDM circuit emulation over PSN) in accordance with RFC5086.  
• 
SAToPSN (structure-agnostic TDM over PSN) in accordance with RFC4553.  
Applicability and Scaling 
The maximum number of PW (connection) configurations that may be stored in the Megaplex-4 is 640, 
where each pseudowire is assigned a unique index number in the range of 1 to 640. The actual 
maximum number, however, depends on the number and type of modules installed in the chassis.  
The pseudowire subsystem is located on the VS and TP modules.  
The table below lists the PW-related features and parameters supported by different I/O modules. 
These parameters are described in sections below.  
Features Supported by PW-Equipped I/O Modules  
I/O Module 
Payload 
Encapsulation 
Methods  
No of 
DS1 
Ports 
No of Supported 
PWs,  
PW Protection 
DS1 
Protection  
Mode 
End-to-End 
Latency 
Direct 
Mapping 
Adaptive 
Timing 
TP 
ces-psn-data 
4 
4+4* 
1+1 
Low 
Yes 
No  
VS-12, VS FXS/FXO 
Voice with serial 
ports (basic) 
ces-psn-data 
12 
12+12* 
 
1+1 
Low 
Yes 
No  
VS-6/C37 
ces-psn-data 
12 
12+12* 
 
1+1 
Low 
Yes 
No  
VS E&M Voice with 
serial ports (basic) 
ces-psn-data 
12 
12+12* 
 
1+1 
Low 
Yes 
No  
VS-6/BIN 
ces-psn-data 
12 
12+12* 
 
1+1 
Low 
Yes 
No  
8. Traffic Processing 
I/O Module 
Payload 
Encapsulation 
Methods  
No of 
DS1 
Ports 
No of Supported 
PWs,  
PW Protection 
DS1 
Protection  
Mode 
End-to-End 
Latency 
Direct 
Mapping 
Adaptive 
Timing 
VS-FXS/E&M 
ces-psn-data 
8 
8+8* 
1+1 
Low 
No 
No 
VS FXS/FXO Voice 
(PW-enhanced) 
VS-6/703  
ces-psn-data 
12 
12+12* 
1+1 
Low 
Yes 
Yes  
VS E&M Voice 
(PW-enhanced)  
ces-psn-data 
12 
12+12* 
1+1 
Low 
Yes 
Yes  
 
VS-6/8E1T1/PW 
ces-psn-data, 
e1satop, 
t1satop 
16 
128 
1+1 
Low 
Yes 
Yes 
VS-16E1T1/PW 
ces-psn-data, 
e1satop, 
t1satop 
16 
128 
1+1 
Low 
Yes 
Yes 
*”X+X PWs” means X active PWs + X PWs for protection purpose. 
Standards   
For protocols supported by different Megaplex-4 modules, see the table above (Features Supported by 
PW-Equipped I/O Modules).  
In addition, some of the VS modules meet the requirements for edge-to-edge simulation of TDM circuits 
over PSN in accordance with RFC4197, including high-performance adaptive timing recovery capabilities. 
Benefits 
Pseudowire circuit emulation technology enables packet-based infrastructure to provide TDM services 
with the service quality of an SDH/SONET network.  
Functional Description  
The pseudowire services convert TDM payload to packets and transfer these packets through Layer-2 or 
Layer-3 (router) services. 
Any PW-equipped module can serve as PW server for other modules, not equipped with PW.  
8. Traffic Processing 
The traffic to the internal DS1 ports is directed by means of a pseudowire cross-connect matrix (a 
timeslot cross-connect matrix similar to the TDM cross-connect matrix), which routes traffic from the 
internal DS1 ports to the pseudowire packet processors.  
Multiple VS and TP modules can be installed in the Megaplex-4 chassis, in accordance with the required 
pseudowire transport capacity.  
Note 
For additional information on the Megaplex-4 pseudowire system, see also 
the following sections:   
• 
Error! Reference source not found. 
• 
Internal DS1 Ports (in Chapter 5)  
• 
PW-TDM Cross-Connect (in this Chapter) 
• 
Fault Propagation (in Chapter 7) 
• 
VS Modules and Teleprotection Modules in Chapter 13 and Chapter 14.  
Pseudowire Packet Processing Subsystem  
The packet processors in the VS/TP packet processing subsystem perform the functions necessary for 
converting TDM traffic directed to the internal DS1 ports into packetized traffic for transmission over 
pseudowires.  
The maximum number of pseudowires that can be processed for each DS1 port, provided the port uses 
the DS0 cross-connect mode, is 16 (only one pseudowire is supported when the port uses the TDM 
cross-connect mode).  
A pseudowire can process traffic from only one internal DS1 port. 
The basic format of a TDM-PW packet is illustrated below: 
Ethernet Header 
PSN and Multiplexing Layer 
Headers 
Control Word 
Packetized TDM Data (Payload) 
Ethernet Header 
The Ethernet header contains the DA, SA and Ethernet type information. It may also contain an optional 
VLAN tag. 
8. Traffic Processing 
UDP over IP  
For UDP/IP-type PSN, the Ethernet header is as follows: 
• 
SA MAC – MAC address of the router interface used for packet forwarding 
• 
DA MAC – MAC address of the resolved next hop 
• 
VLAN –VLAN assigned to the router interface used for packet forwarding 
• 
P-bit – CoS of PW is set to 1. P-bit is a RIF attribute (CoS > P-bit). 
MEF-8  
For the MEF-type PSN, the Ethernet header is as follows: 
• 
DA MAC – MAC address of the peer 
• 
VLAN – Flow (E-Line/E-LAN) VLAN 
• 
P-bit – CoS of PW is set to 1. P-bit is a flow attribute (marking profile, CoS > P-bit) 
• 
Packet color – green. 
PSN and Multiplexing Layer Headers 
Each pseudowire has a header whose structure depends on the selected PSN type, and includes labels 
that specify the uniquely specify the pseudowire source and destination. 
Note 
• 
Different source and destination labels can be used. In this case, it is 
necessary to ensure that the source (inbound) label selected at one 
pseudowire endpoint is configured as the destination (outbound) label at 
the other pseudowire endpoint, and vice versa. 
• 
The inbound Input PW label must be unique.  
Megaplex-4 supports the following PSN types: 
• 
UDP over IP 
• 
MPLS 
• 
Ethernet (MEF-8). 
UDP over IP 
For UDP/IP-type PSN, the TDM-PW packet structure is as follows: 
6 
6 
2 
2 
2 
20 
8 
4 
 
8. Traffic Processing 
DA 
SA 
Type 8100 
VLAN Tag 
Type 800 
IP Header 
UDP Header 
CW 
TDM Payload 
Where: 
• 
DA – MAC address of the next hop (taken from the forwarding table) 
• 
SA – MAC address of the applicable router interface 
• 
VLAN type 0x8100 + VLAN tag, optional 
• 
Type – 0x800 (IP packet) 
• 
IPv4 Header – the protocol field of the IP header is set to 17 (UDP)  
• 
UDP Header – the PW label/s, manually configured (see below) 
For UDP/IP-type PSN IP, the TOS byte in the IP header can be configured per PW. 
The UDP header is used to multiplex between the different PWs. For CESoPSN and SAToPSN bundles 
using packet payload Version V2:  
UDP Source Port = C000 + Destination PW Number. 
This means that all the UDP ports numbers are higher than C000 hexa (49152 decimal). 
MEF-8  
For MEF-8-type PSN, the TDM-PW packet structure is as follows: 
6 
6 
2 
2 
2 
4 
4 
 
DA 
SA 
Type 8100 
VLAN Tag 
Type 88D8 
ECID 
CW 
TDM Payload 
Where: 
• 
DA – MAC address of the peer device 
• 
SA – MAC address of the associated SVI (per E5-cTDM-4 card) 
• 
VLAN type 0x8100 + VLAN tag, optional 
• 
Type – 0x88D8 (CESoETH packet) 
• 
ECID – Emulated Circuit Identifier, a manually configured unique label which identifies the PW. 
Control Word 
The control word structure is illustrated below. 
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
 
 
 
 
15 
16 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
31 
0 0 0 0 L R M/RSV FRG LEN (6) 
Sequence Number (16) 
8. Traffic Processing 
Bits 0-3 – Set to zero. 
L – local attachment circuit abnormal condition. If set, indicates that the source has detected or has 
been notified of a TDM fault condition that is affecting the data to be transmitted. If the TDM fault is 
cleared, the L bit is also cleared. 
R – remote loss of frame. If set, indicates that packet loss or buffer underflow condition is detected at 
the PSN. 
M/RSV – a 2-bit modifier field in CESoPSN. If L=0, it allows detection of signaling packets, carrying RDI 
across the PSN. If L=1, only value ‘00’ for M bits is currently defined. In SAToP it is reserved and must be 
set to 0. 
L & M can be treated as a 3-bit code point that is described in the table below. 
L & M Code Point Interpretations 
L 
M 
Code Point Interpretation 
0 
00 
Normal situation, no failure 
0 
01 
Reserved 
0 
10 
RDI condition of the attachment circuit (TDM link). The payload is received, and upon 
configuration RDI can be generated on the outgoing TDM trunk. 
0 
11 
Reserved for CESoPSN signaling packets. 
1 
00 
TDM data is invalid. The payload is replaced by an “Idle” bit pattern towards the TDM trunk. 
Additionally, it can be pro configured to generate an AIS pattern or “Channel Idle” signal 
towards the local CE on the TDM trunk.   
1 
01 
Reserved 
1 
10 
Reserved 
1 
11 
Reserved 
FRG – fragmentation field. This field is used for fragmenting multiframe structures into multiple packets 
in case of structured CESoPSN with CAS bundles. Must be set to zero. 
LEN – the length of the TDM-PW packet (header + payload) if it is less than 64 bytes. Otherwise, it is set 
to zero. 
Sequence Number – provides the common PW sequencing function as well as detection of lost packets. 
Its generation rules: 
• 
Its space is a 16-bit unsigned circular number 
• 
Its initial value is random (unpredictable) 
8. Traffic Processing 
• 
It is incremented with each TDM-PW data packet sent in the specific PW. 
TDM Payload  
The TDM payload encapsulation methods supported by different I/O modules are listed in Features 
Supported by PW-Equipped I/O Modules. Each payload encapsulation method can be independently 
selected for each pseudowire.  
SAToPSN  
SAToPSN is used to transfer transparently a bit stream at the nominal port rate (2.048 Mbps). Therefore, 
SAToPSN can be used only when the port uses the unframed mode, and thus only one pseudowire can 
be configured per port.  
SAToPSN packet payload consists of a user-specified number of raw TDM bytes (VS-16E1T1-PW and VS-
6/E1T1: 32 to 1440 bytes), and is treated as data payload.  
Note 
The SAToPSN packet overhead is large, and therefore, for efficient bandwidth 
utilization, the number of raw TDM bytes per packet should be as large as 
possible.  
The receiving end restores the original bit stream, and therefore a SAToPSN pseudowire can only be 
directed to another unframed E1 port, or to an n×64 kbps protocol (where n must be 32, that is, to a 
high-speed serial port operating at a rate of 2048 kbps). 
CESoPSN  
CESoPSN transports raw TDM data, that is, packets are formed by inserting a user-specified number of 
complete TDM frames in the packet payload area. CESoPSN pseudowires can only be configured on 
framed ports.  
The TDM frames are considered as serial data, even if they carry voice and CAS. Since a CESoPSN 
pseudowire transports raw TDM frames, a CESoPSN pseudowire can only be directed to another E1 
framed port. 
PSN Configuration Parameters  
Each pseudowire is handled in accordance with the user-configured PSN parameters, considering the 
user-selected pseudowire parameters, and the framing and signaling mode of the associated internal 
DS1 port.  
Megaplex-4 enables the user to select the PSN type (UDP/IP, MPLS or Ethernet), and configure the PSN 
transport parameters. 
8. Traffic Processing 
The PSN parameters, which are reflected in the pseudowire header structure, enable specifying the 
requested priority or quality of service for pseudowire traffic generated by the VS/TP module. The 
applicable parameters depend on PSN type: 
• 
When the PSN is based on Layer 2 forwarding, the user can specify the VLAN priority (per IEEE 
802.1p) for the Ethernet frames carrying pseudowire packets. The priority is always selectable 
for traffic forwarded through the Megaplex-4 GbE ports, because for these ports VLAN tagging is 
always enabled; when using other bridge ports as pseudowire exit ports, it is necessary to 
enable VLAN tagging in order to request a specific priority. 
• 
When the PSN uses IP routing, the user can specify the Type of Service (ToS) per RFC791; if the 
PSN supports RFC2474, ToS is interpreted as a DiffServ codepoint per RFC2474. 
• 
When the PSN uses MPLS, the user can specify the EXP bits. In addition, the user can also add 
ingress and egress tunnel labels, which enable network operators to plan preferential 
forwarding of pseudowire traffic using the specified tunnel labels. 
Pseudowire QoS/CoS  
To enable optimal handling of pseudowire traffic within the PSN, the following parameters can be 
configured: 
• 
For Ethernet transport networks: outgoing pseudowire packets are assigned to a dedicated 
VLAN ID according to 802.1Q and marked for priority using 802.1p bits. 
• 
For IP transport networks: outgoing pseudowire packets are marked for priority using DSCP or 
ToS bits.  
• 
For MPLS transport networks: outgoing pseudowire packets are assigned to a specific MPLS 
tunnel, and marked for priority using the EXP bits. 
The proper balance between the PSN throughput and delay is achieved via configurable packet size. A 
jitter buffer with selectable size compensates for packet delay variation (jitter) of up to 200 msec in the 
network. 
The maximum JB size depends on the module type: 
• 
VS-12, VS-6/BIN, VS-6/C37, TP and VS Voice basic modules: 8000 µsec 
• 
Other modules: 256 msec. 
ToS  
The ToS specifies the Layer 3 priority assigned to the traffic generated by this pseudowire. 
8. Traffic Processing 
For IP networks, this priority is indicated by the IP type-of-service parameter for this pseudowire. The 
specified value is inserted in the IP TOS field of the pseudowire IP packets. 
When supported by an IP network, the type-of-service parameter is interpreted, in accordance with 
RFC791 or RFC2474, as a set of qualitative parameters for the precedence, delay, throughput and 
delivery reliability to be provided to the IP traffic generated by this pseudowire. 
These qualitative parameters may be used by each network that transfers the pseudowire IP traffic to 
select specific values for the actual service parameters of the network, to achieve the desired quality of 
service. 
You can also specify a Layer 2 priority by means of the vlan priority command. 
Jitter Buffer  
The packets of each pseudowire are transmitted by PW-equipped modules at essentially fixed intervals 
towards the PSN. The packets are transported by the PSN and arrive to the far end after some delay. 
Ideally, the PSN transport delay should be constant: in this case, the packets arrive at regular intervals 
(these intervals are equal to the intervals at which they had been transmitted). However, in reality 
packets arrive at irregular intervals, because of variations in the network transmission delay. The term 
Packet Delay Variation (PDV) is used to designate the maximum expected deviation from the nominal 
arrival time of the packets at the far end device.  
Note 
The deviations from the nominal transmission delay experienced by packets 
are referred to as jitter, and the PDV is equal to the expected peak value of 
the jitter. Note however that nothing prevents the actual delay from 
exceeding the selected PDV value.  
To compensate for deviations from the expected packet arrival time, the module uses jitter buffers that 
temporarily store the packets arriving from the PSN (that is, from the far end equipment) before being 
transmitted to the local TDM equipment, to ensure that the TDM traffic is sent to the TDM side at a 
constant rate. 
For each pseudowire, the jitter buffer must be configured to compensate for the jitter level expected to 
be introduced by the PSN, that is, the jitter buffer size determines the Packet Delay Variation Tolerance 
(PDVT).  
Two conflicting requirements apply: 
• 
Since packets arriving from the PSN are first stored in the jitter buffer before being transmitted 
to the TDM side, TDM traffic suffers an additional delay. The added delay time is equal to the 
jitter buffer size configured by the user. 
8. Traffic Processing 
• 
The jitter buffer is filled by the incoming packets and emptied out to fill the TDM stream. If the 
PSN jitter exceeds the configured jitter buffer size, underflow/overflow conditions occur, 
resulting in errors at the TDM side: 
 
A jitter buffer overrun occurs when it receives a burst of packets that exceeds the 
configured jitter buffer size + packetization delay. When an overrun is detected, the module 
clears the jitter buffer, causing an underrun. 
 
A jitter buffer underrun occurs when no packets are received for more than the configured 
jitter buffer size, or immediately after an overrun. 
When the first packet is received, or immediately after an underrun, the buffer is automatically filled 
with a conditioning pattern up to the PDVT level in order to compensate for the underrun. Then, the 
module starts processing the packets and empty out the jitter buffer toward the TDM side.  
To minimize the possibility of buffer overflow/underflow events, two conditions must be fulfilled: 
• 
The buffer must have sufficient capacity. For this purpose, the buffer size can be selected by the 
user in accordance with the expected jitter characteristics, separately for each pseudowire. 
• 
The read-out rate must be equal to the average rate at which frames are received from the 
network. For this purpose, the read-out rate must be continuously adapted to the packet rate, a 
function performed by the adaptive clock recovery mechanism of each packet processor. 
Adaptive Timing  
A number of Megaplex-4 I/O modules have independent adaptive clock recovery mechanisms for each 
pseudowire, which recover the original timing (clock rate) of the far-end source of each pseudowire. The 
clock recovery mechanisms can provide recovered clock signals to serve as timing references for the 
Megaplex-4 nodal timing subsystem. 
The receive path of each pseudowire must use a clock recovery mechanism to recover a clock signal at 
the original payload transmit rate used at the far end. This mechanism is referred to as adaptive clock 
recovery mechanism.  
Each pseudowire has its own adaptive timing recovery mechanism, in accordance with the options listed 
in RFC4197. The recovered pseudowire clocks can be used as timing reference signals for the nodal 
Megaplex-4 timing subsystem, and therefore the I/O module allows flexible timing distribution.  
The adaptive clock recovery mechanism estimates the average rate of the payload data received in the 
frames arriving from the packet-switched network. Assuming that the packet-switched network does 
not lose data, the average rate at which payload arrives will be equal to the rate at which payload is 
transmitted by the source.  
8. Traffic Processing 
Note 
Generally, lost packets, as well as packets that did not arrive in the correct 
order, are replaced by special dummy packets. However, for CESoPSN and 
SAToPSN, packets can be reordered.  
The method used to recover the payload clock of a pseudowire is based on monitoring the fill level of 
the selected pseudowire jitter buffer: the clock recovery mechanism monitors the buffer fill level, and 
generates a read-out clock signal with adjustable frequency. The frequency of this clock signal is 
adjusted so as to read frames out of the buffer at a rate that keeps the jitter buffer as near as possible to 
the half-full mark. This condition can be maintained only when the rate at which frames are loaded into 
the buffer is equal to the rate at which frames are removed. Therefore, the adaptive clock recovery 
mechanism actually recovers the original payload transmit clock.  
The performance of the clock recovery mechanism can be optimized for the operating environment, by 
specifying the following parameters: 
• 
The accuracy of the original timing source, in accordance with the standard SDH/SONET 
terminology (Stratum 1, 2, 3, 3E, or 4/unknown) 
• 
The type of PSN that transports the traffic: router-based network (for example, UDP/IP) versus 
switch-based network (for example, MPLS/Ethernet). 
You can select a total of 10 pseudowire recovered clocks per Megaplex-4.  
VS-16E1T1-PW, VS-6/E1T1, VS-6/703 and PW-enhanced VS voice modules have the full support of 
adaptive timing.  
Adaptive timing is not supported by other PW-equipped modules.  
Jitter Buffer Centering  
Megaplex-4 includes a Jitter Buffer (JB) Centering mechanism designed to maintain a stable end-to-end 
delay for a pseudowire (PW), especially in networks with high jitter. Normally, when a PW is established 
or after underrun/overrun events, the jitter buffer is centered to protect traffic from network delay 
variations and bursts. However, in highly jittered networks, the initial buffer state after centering may 
still be inaccurate, causing inconsistent end-to-end delay following PW recovery events. 
To address this, Megaplex-4 can verify the jitter buffer position after PW setup or underrun/overrun 
recovery. Once TDM playout starts, the system samples the jitter buffer fill level and calculates the 
average fill level. If the average deviates from the expected center by more than a configurable 
threshold, the jitter buffer is flushed and re-centered automatically. This functionality is configured per 
PW and can be enabled or disabled using the jitter-buffer-centering deviation <%> command. By 
default, the feature is disabled. 
8. Traffic Processing 
Factory Defaults 
By default, no pseudowires are configured: you must define your own in accordance with your 
application requirements. Other parameter defaults are listed in the table below. 
Parameter  Default Value 
psn  
udp-over-ip 
type  
ces-psn-data 
tos 
0 
tunnel-index 
0 (for ingress and egress) 
jitter-buffer [sec} 
2500  
jitter-buffer centering 
Disabled  
tdm-payload  
4  
vlan priority 
0 
label 
For udp-over-ip and ethernet: same as the PW index number  
For mpls: PW  index number + 15  
udp-mux-method  
src-port 
oos parameters: 
data 
00 
voice 
00 
Configuring Pseudowires  
New pseudowire bundles are added by defining their number (1–640), type (connection mode) and a 
PSN type. 
 To define and configure a pseudowire: 
1. If you intend to use UDP/IP PSN type, verify that the router interface with valid IP address has 
been configured (see Error! Reference source not found.). 
2. At the config>pwe# prompt, enter the syntax illustrated in the table below. 
The config>pwe>pw(<pw-number>)# prompt appears. 
8. Traffic Processing 
Note 
An internal DS1 port becomes active only if at least one enabled pseudowire 
with a valid cross-connection is assigned to the port 
 
Task 
Command 
Comments 
Assigning the pseudowire number, 
selecting the encapsulation protocol 
for the selected pseudowire and 
specifying the PSN type (selecting the 
type of PSN header)  
 
pw <pw-number> [type 
{ces-psn-data | e1satop 
| t1satop| [psn { 
ethernet | mpls | udp-
over-ip}]  
        
  
• PW number: 1..640  
PW type (must be configured for 
the first time): 
• e1satop: SAToPSN protocol, 
for carrying unframed E1 data 
streams 
• t1satop: SAToPSN protocol, 
for carrying unframed T1 data 
streams 
• ces-psn-data: CESoPSN 
protocol, for carrying framed 
data streams 
To check PW types supported by 
different PW modules, see the 
table “Features Supported by PW-
Equipped I/O Modules”.  
psn (must be configured for the 
first time): 
• udp-over-ip – UDP over IP 
network encapsulation 
• ethernet – MEF-8 Ethernet 
network encapsulation 
Using no before pw <number> 
deletes the pseudowire 
3. At the config>pwe>pw(<pw-number>)# prompt, enter the parameters specified in the table 
below. 
Task 
Command 
Comments 
Assigning a name to the 
pseudowire 
name <up to 32 
characters> 
 
8. Traffic Processing 
Task 
Command 
Comments 
Specifying the PW label 
used in the inbound and 
outbound directions 
label  [in <number>] 
[out < number>] 
Out PW label: 
• For udp-over-ip: Specifies the UDP source 
port number used by the pseudowire  
• For mpls: Specifies the outer (tunnel) MPLS 
label used by the pseudowire.  
• For ethernet: Specifies the Emulated Circuit 
ID (ECID) for Tx PW packets 
In PW label: 
• For udp-over-ip: Specifies the UDP source 
port number used by the pseudowire for the 
Tx PW packets (destination port for Rx PW 
packets) 
• For mpls: Specifies the inbound MPLS label 
used by the pseudowire  
• For ethernet: Specifies the expected 
Emulated Circuit ID (ECID) Rx PW packets 
Each PW must have a unique in (source) label. 
Do not reuse the same out (destination) value on 
bundles terminating at the same peer, and/or 
using the same VLAN ID (when VLAN tagging is 
enabled). 
For udp-over-ip and ethernet, the allowed range 
is 1 to 8191. 
For mpls, the allowed range is 16 to 1048575.  
Controlling whether the 
next-hop MAC is 
periodically monitored 
according to the ARP table 
arp-table-refresh 
no arp-table-refresh 
 
For udp-over-ip only 
When using arp-table-refresh, PW transmission 
will be stopped once the next hop ARP entry is 
flushed from the ARP table, otherwise the PW 
will keep transmitting. 
Transmitting an 
out-of-service signal (OOS) 
on PW failure and 
selecting the code 
transmitted by the port 
during out-of-service 
periods on the timeslots 
defined as data and voice 
timeslots.  
 
tdm-oos [voice <00 
to FF (hexa)>] [data 
<00 to FF (hexa)>]    
  
tdm-oos voice and data are hexadecimal 
numbers in the range of 00 to FF (two digits). 
The selected code for data is also sent during 
out-of-service periods instead of the external 
data stream when the unframed mode is used 
8. Traffic Processing 
Task 
Command 
Comments 
Defining the jitter buffer 
size in µsec 
jitter-buffer <value 
in µsec>  
Use the shortest feasible buffer, to minimize 
connection latency 
For VS-16E1T1/PW and VS-6/E1T1 modules: 
250 µsec to 256000 µsec, in 1-µsec steps (the 
value entered by the user is rounded upward to 
the closest n*125 µsec value). 
For other VS and TP modules: 250 µsec to 
8000 µsec, in 1-µsec steps (the value entered by 
the user is rounded upward to the closest n*125 
µsec value).  
ETX-205/IPmux-216  jitter buffer configuration 
refers to the middle point of the jitter buffer 
while Megaplex-4 jitter buffer configuration 
refers to the whole buffer size. Thus, when 
working with IPmux-216 or ETX-205, the jitter 
buffer value of the Megaplex-4 must be 
configured as twice the value configured on the 
IPmux-216/ETX-205.  
Enabling Jitter Buffer (JB) 
Centering mechanism and 
configuring the deviation 
threshold 
jitter-buffer-
centering deviation 
<value in %>  
 
Default: no jitter-buffer-centering 
Defining a remote peer 
terminating this PW 
peer <1–640> 
1 to 640  
Using no peer removes the remote peer  
Specifying the number of 
TDM payload bytes to be 
inserted in each packet  
 
tdm-payload <1–
360> 
 
  
A larger value increases the bandwidth utilization 
efficiency, but also increases the connection 
intrinsic latency.  
The number is specified as a multiple of 48 bytes, 
for example, 1 means 48 bytes, and 30 means 
1440 bytes.  
The values for CESoPSN are:  
• For VS-16E1T1-PW and VS-6/E1T1 modules: 1 
to 61. 
• For other VS and TP modules: 1 to 64.   
The values for SAToPSN are: 
• For VS-16E1T1-PW and VS-6/E1T1 modules: 
32 to 1440. 
8. Traffic Processing 
Task 
Command 
Comments 
Specifying the value for 
the TOS byte used on 
outbound traffic 
tos <tos  number> 
   
This parameter is relevant only when psn is 
udp-over-ip. 
Range: from 0 to 255.  
In accordance with RFC 2474, it is recommended 
to use only values which are multiples of 4.  
Enabling and configuring 
VLAN tagging and priority 
on every transmitted 
packet 
vlan [priority <0..7> 
tag  <1..4094>] 
       
 
VLAN priority: The allowed range in accordance 
with IEEE 802.1p is 7 (highest priority) to 0 
(lowest priority). 
Using the tag command allows the same SVI to 
be used for several PWs. 
Note: If the traffic on the specific PW must be 
assigned priority, the priority parameter must be 
configured in this context (not as part of flow 
configuration) and then mapped via queue-map-
profile configuration. 
Controlling whether the 
PW carries a failure 
indication if the local 
domain clock fails 
domain-failure-
indication 
no domain-failure-
indication 
 
Defining the conditions 
when the PW is 
considered failed for the 
CSM 
source-clock-fail 
[pw-down] [remote-
domain-down] 
pw-down – PW failure (always enabled) 
remote-domain-down – Once the PW receives 
an indication of failure from the far-end side, the 
PW clock moves to the fail state 
Enabling and specifying 
the ingress and egress 
MLPS tunnel indices 
tunnel-index 
[ingress <ingress-
label>] [egress 
<egress-label>] 
 
Relevant for MPLS PSN only  
If an ingress label is configured, the egress label 
must be configured as well, and vice versa. 
The supported range is 16 to 1048575.  
• Adding no before the command removes the 
labels  
Assigning egress port for 
L2 forwarding 
egress-port svi 
<svi_number> 
This parameter is relevant only when psn is 
ethernet 
8. Traffic Processing 
Task 
Command 
Comments 
Specifying the UDP port 
multiplexing method 
 
  
udp-mux-method  
{dst-port | src-port }    
This parameter is relevant only when psn is 
udp-over-ip. 
dst-port: 
UDP destination port = 0xC000 + <out-PW-label>  
UDP source port is 0xC000 + <in-PW-label> 
src-port: 
UDP destination port = 0x85E+ <out-PW-label> 
UDP source port is 0xC000  
Examples 
 To configure a SAToP PW with UDP/IP network encapsulation: 
• 
PW number 1 
• 
PW type – SAToP 
• 
PSN type – UDP/IP 
• 
Out (destination) label – 3 
• 
In (source) label – 2 
• 
Jitter buffer – 10 000 
• 
Peer – 1 (further configuration – under configure>peer) 
• 
TDM payload size – 30. 
config>pwe# pw 1 type e1satop psn udp-over-ip  
config>pwe>pw(1) label out 3 in 2 
config>pwe>pw(1) jitter-buffer 10000 
config>pwe>pw(1) peer 1 
config>pwe>pw(1) tdm-payload 30 
 To configure a MEF-8 pseudowire: 
• 
PW number 1 
• 
PW type –SAToP 
• 
PSN type – Ethernet 
• 
Out (destination) label – 1 
8. Traffic Processing 
• 
In (source) label – 1 
• 
Jitter buffer – 300 
• 
Peer – 1 
• 
Egress port – SVI 1 
• 
TDM payload size – 30  
config>pwe# pw 1 type t1satop psn ethernet  
config>pwe>pw(1) label out 1 in 1 
config>pwe>pw(1) jitter-buffer 300 
config>pwe>pw(1) peer 1 
config>pwe>pw(1) egress-port svi 1 
config>pwe>pw(1) tdm-payload 30 
Displaying PW Statistics  
PW ports of VS and TP modules feature the collection of statistical diagnostics, thereby allowing the 
carrier to monitor the transmission performance of the links. 
The pseudowire transmission statistics enable analyzing pseudowire traffic volume, evaluate the end-to-
end transmission quality (as indicated by sequence errors), and jitter buffer performance. By resetting 
the status data at the desired instant, it is possible to ensure that only current, valid data is taken into 
consideration. 
 To display the PW statistics: 
• 
At the prompt config>slot>pwe>pw(<PW number>)#, enter show statistics followed by 
parameters listed below.  
Task 
Command 
Comments 
Displaying statistics 
show statistics {total | all | 
all-intervals | current}  
  
• current - Displays the current 
statistics 
• all-intervals – Displays statistics 
for all valid intervals (without 
current statistics) 
• all –all statistics: first current 
statistics, then statistics for all 
valid intervals, and finally total 
statistics 
• total – Displays total statistics of 
last 96 intervals 
8. Traffic Processing 
Task 
Command 
Comments 
Displaying statistics for a 
specific interval 
show statistics interval 
<interval-num 1..96> 
 
PW statistics are displayed.  The counters are described in the tables below. 
For example: 
Current Statistics:  
config>pwe>pw(1)# show statistics current 
Time Elapsed (Sec)                 : 1401 
Valid Intervals                    : 0 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 0 
Jitter Buffer Overflows Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Level  (uSec)    : 441 
Max Jitter Buffer Deviation (uSec) : 441 
Statistics for interval 2: 
config>pwe>pw(1)# show statistics interval 2 
Interval Number : 2 
 
Sequence Errors Seconds            : 0 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 1 
Jitter Buffer Overflows Seconds    : 3 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 2005 
Max Jitter Buffer Level  (uSec)    : 6500 
Max Jitter Buffer Deviation (uSec) : 7800 
All statistics:  
config>pwe>pw(1)# show statistics all 
Time Elapsed (Sec)                 : 1235 
Valid Intervals                    : 0 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 0 
Jitter Buffer Overflows Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Level  (uSec)    : 441 
8. Traffic Processing 
Max Jitter Buffer Deviation (uSec) : 441 
Interval Number : 1 
 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 0 
Jitter Buffer Overflows Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Level  (uSec)    : 488 
Max Jitter Buffer Deviation (uSec) : 488 
 
Interval Number : 2 
 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 0 
Jitter Buffer Overflows Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Deviation (uSec) : 0 
 
Interval Number : 3 
 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 0 
Jitter Buffer Overflows Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Deviation (uSec) : 0 
All Intervals Statistics: 
config>pwe>pw(1)# show statistics all-intervals 
 
Interval Number : 1 
 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 0 
Jitter Buffer Overflows Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Level  (uSec)    : 488 
Max Jitter Buffer Deviation (uSec) : 488 
 
8. Traffic Processing 
Interval Number : 2 
 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 0 
 
Jitter Buffer Overflows Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Deviation (uSec) : 0 
 
Interval Number : 3 
 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 0 
Jitter Buffer Overflows Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Deviation (uSec) : 0 
 
Interval Number : 4 
 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 0 
Jitter Buffer Overflows Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Deviation (uSec) : 0 
 
Interval Number : 5 
 
Missing Packets                    : 0 
Mis-order Dropped Packets          : 0 
Reordered Packets                  : 0 
Jitter Buffer Underflows Seconds   : 0 
Jitter Buffer Overflows Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Min Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Level  (uSec)    : 0 
Max Jitter Buffer Deviation (uSec) : 0 
more.. 
 
Total Statistics:  
8. Traffic Processing 
config>pwe>pw(1)# show statistics total  
 
Total 
--------------------------------------------------------------- 
Rx Frames                        : 1391711 
Tx Frames                        : 4798604 
Jitter Buffer Underflows Seconds : 0 
Jitter Buffer Overflows Seconds  : 0 
Sequence Errors Seconds          : 0 
PWE Statistics Parameters – Current 15-Minute Interval  
Parameter 
Description 
Time Elapsed 
(Sec) 
The elapsed time (in seconds) since the beginning of the current interval, in 
seconds. The range is 1 to 900 seconds 
Valid Intervals 
The number of elapsed finished 15-min intervals for which statistics data can be 
displayed, in addition to the current (not finished) interval (up to 96). 
Sequence Errors 
Seconds 
Displays the number of seconds during which sequence errors have been 
detected. 
In accordance with the applicable standards, the transmitted packets carry a 
sequence number that is automatically assigned, such that consecutive packets 
are automatically consecutive sequence numbers. At the receive side, these 
numbers are checked by the receive mechanism, which expects each new 
incoming packet to carry the next number in the sequence, relative to the 
previous one (i.e., packet 5 must be received after packet 4). Any deviation from 
the this rule indicates a problem with packet flow integrity (and hence with the 
pseudowire payload (data or voice) integrity), and in this case the sequence errors 
count is incremented by 1. 
There are two main reasons for a sequence error event: 
• One or more packets have been lost somewhere in the network. 
• Packets have been reordered within the network. Packet reordering may 
occur due to queuing mechanisms, rerouting by the network, or when the 
router updates include very large routing tables 
In VS, SH and TP modules, this number is the total number of seconds when the 
Missing Packets, Mis-order Dropped Packets and Reordered Packets events 
occurred. 
Missing Packets 
(VS Modules only) 
Number of missing packets as detected via Control Word sequence number gaps. 
This count does not include misordered dropped packets.  
Mis-order 
Dropped Packets 
(VS Modules only) 
 
Number of packets detected via Control Word sequence number to be out of 
sequence, and could not be re-ordered, or could not fit in the jitter buffer. This 
count includes duplicated packets. 
8. Traffic Processing 
Parameter 
Description 
Reordered 
Packets (VS 
Modules only) 
Number of packets detected via Control Word sequence number to be out of 
sequence, but successfully reordered. 
Jitter Buffer 
Underflows 
Seconds  
Displays the number of seconds during which at least one jitter buffer underflow 
event has been detected.  
PW-containing modules are equipped with a Packet Delay Variation Tolerance 
buffer, also called a “jitter buffer”, which is used to automatically compensate for 
packet network delay variation (jitter). Each pseudowire has its own jitter buffer. 
Although packets leave the transmitting PW-module at a constant rate, they will 
usually reach the far end at a rate which is not constant, because in practice the 
network transmission delay varies (due to factors such as congestion, rerouting, 
queuing mechanisms, transport over wireless or half-duplex media, etc.).  
TDM equipment at both ends of a pseudowire require a constant flow of data, 
and cannot tolerate delay variation. Therefore, the receive side jitter buffer is 
required to provide the TDM equipment with a synchronous and constant flow. 
For this purpose, when a pseudowire is set up (and at any time after 
communication is restored), the jitter buffer is loaded with packets up to its 
middle point: only after this point it starts outputting TDM data towards the 
connected TDM equipment. The stored packets assure that the TDM equipment 
will continue receiving data even if the network delay momentarily increases. 
Obviously, if packets are delayed too long, the buffer is gradually emptied out 
until it underflows (this situation is called buffer starvation, and it affects the end-
to-end voice/data integrity).  
Each underflow event increases the jitter buffer underflow counter by 1.   
Jitter Buffer 
Overflows 
Seconds 
Displays the number of seconds during which at least one jitter buffer overflow 
event has been detected.   
As explained above, during steady state, the jitter buffer is filled up to its middle 
point, which means that it has space to hold additional packets. An overflow will 
occur when the network delay suddenly decreases, for example, when a large 
burst of packets reaches the PW module. If the burst includes more packets than 
the jitter buffer can store at that instant, the buffer will be filled up to its top. In 
this case, an unknown number of excess packets are dropped. To correct the 
situation, Megaplex-4 initiates a forced underflow by flushing (emptying) the 
buffer. Therefore, an overflow always results in an immediate underflow. After 
the buffer is flushed, the process of filling up the buffer is started again 
8. Traffic Processing 
Parameter 
Description 
Jitter Buffer 
Centering Events 
 
Displays the number of times the jitter buffer centering mechanism has been 
triggered. A centering event may occur during the initial PW setup or following a 
jitter buffer underrun or overrun condition. The purpose of the centering 
mechanism is to ensure that the jitter buffer operates around its optimal middle 
position, protecting the PW from excessive delay variations and packet bursts in 
highly jittered networks. 
After a centering event is triggered and TDM playout begins, Megaplex-4 
periodically samples the jitter buffer fill level and calculates an average buffer 
position. If the measured average deviates from the expected center by more 
than the configured threshold, the jitter buffer is flushed and re-centered 
automatically. This mechanism helps maintain a stable end-to-end delay and 
prevents incorrect jitter buffer positioning after recovery from underrun or 
overrun events. 
Min Jitter Buffer 
Level (usec) 
Actual minimum size of the jitter buffer recorded for this pseudowire in the 
selected interval, in µsec (not relevant for HDLC pseudowires).  
Max Jitter Buffer 
Level (usec) 
Actual maximum size of the jitter buffer recorded for this pseudowire in the 
selected interval, in µsec (not relevant for HDLC pseudowires). 
Max Jitter Buffer 
Deviation (usec) 
The maximum jitter buffer deviation (variation of delay, in µsec) reported during 
the selected interval (not relevant for HDLC pseudowires). This is the maximum 
jitter level that had to be compensated for in the selected interval  
PWE Statistics Parameters – All Intervals Statistics 
Parameter 
Description 
Valid Intervals 
The number of elapsed finished 15-min intervals for which statistics data can be 
displayed, not including the current (not finished) interval (up to 96) 
8. Traffic Processing 
Parameter 
Description 
Sequence Errors 
Seconds 
Displays the number of seconds during which sequence errors have been 
detected. 
In accordance with the applicable standards, the transmitted packets carry a 
sequence number that is automatically assigned, such that consecutive packets 
are automatically consecutive sequence numbers. At the receive side, these 
numbers are checked by the receive mechanism, which expects each new 
incoming packet to carry the next number in the sequence, relative to the 
previous one (i.e., packet 5 must be received after packet 4). Any deviation from 
the this rule indicates a problem with packet flow integrity (and hence with the 
pseudowire payload (data or voice) integrity), and in this case the sequence errors 
count is incremented by 1. 
There are two main reasons for a sequence error event: 
• One or more packets have been lost somewhere in the network. 
• Packets have been reordered within the network. Packet reordering may 
occur due to queuing mechanisms, rerouting by the network, or when the 
router updates include very large routing tables 
Missing Packets 
(VS Modules only) 
Number of missing packets as detected via Control Word sequence number gaps. 
This count does not include misordered dropped packets.  
Mis-order 
Dropped Packets 
(VS/SH/TP 
Modules only) 
Number of packets detected via Control Word sequence number to be out of 
sequence, and could not be re-ordered, or could not fit in the jitter buffer. This 
count includes duplicated packets. 
Reordered 
Packets 
(VS/SH/TP 
Modules only) 
Number of packets detected via Control Word sequence number to be out of 
sequence, but successfully reordered. 
Min Jitter Buffer 
Level (usec) 
Actual minimum size of the jitter buffer recorded for this pseudowire in the 
selected interval, in µsec (not relevant for HDLC pseudowires). 
Max Jitter Buffer 
Level (usec) 
Actual maximum size of the jitter buffer recorded for this pseudowire in the 
selected interval, in µsec (not relevant for HDLC pseudowires). 
Max Jitter Buffer 
Deviation (usec) 
The maximum jitter buffer deviation (variation of delay, in µsec) reported during 
the selected interval (not relevant for HDLC pseudowires). This is the maximum 
jitter level that had to be compensated for in the selected interval  
PWE Statistics Parameters – Total Statistics 
Parameter 
Description 
Tx Frames 
Total number of frames transmitted toward the PSN 
8. Traffic Processing 
Parameter 
Description 
Rx Frames 
Total number of frames received from the PSN 
Sequence Errors Seconds 
Total number of seconds during which sequence errors have been 
detected. 
In VS modules, this number is the total number of seconds when the 
Missing Packets, Mis-order Dropped Packets and Reordered Packets 
events occurred. 
Jitter Buffer Underflows 
Seconds 
Total number of jitter buffer underflow events (not relevant for HDLC 
pseudowires).  
Jitter Buffer Overflows 
Seconds 
Total number of jitter buffer overflow events (not relevant for HDLC 
pseudowires).  
 To clear the PW statistics: 
• 
At the prompt config>pwe>pw<PW number>)#, enter clear-statistics. 
The statistics for the specified PW are cleared. 
Viewing the Pseudowire Status and Summary  
 To display a single PW status: 
1. At the config#pwe prompt, enter the desired pseudowire (pw <number>). 
The config>pwe>pw(<number>)$ prompt appears. 
2. Enter show status. 
The status screen appears. For information on the connectivity status values, refer to the table 
below. 
config# pwe 
config>pwe# pw 2 
config>pwe>pw(2)# show status 
PW : pw-2 
 
Name                                      : pw-1 
PW Type                                   : CES PSN Data 
PSN Type                                  : UDP Over IP 
Connectivity Status                       : Up 
Out Label                                 : 2 
In Label                                  : 2 
Peer IP Address                           : 20.20.11.1 
Next Hop MAC Address                      : 00-00-00-00-00-00 
8. Traffic Processing 
The table below explains the connectivity status values of the selected pseudowire. 
Pseudowire Connectivity Status Values 
Parameter Displayed 
Description 
Disable 
The pseudowire is disabled 
Up 
  
The pseudowire carries traffic, and both the remote and the local pseudowire 
endpoints receive Ethernet frames. However, there may be problems such as 
sequence errors, underflows, overflows, etc., which may be displayed using 
the Statistics function. 
Unavailable 
  
The pseudowire reports loss of connectivity. This is often caused by network 
problems, or configuration errors. 
Down 
The pseudowire is waiting for timeslot assignment 
Local Fail 
 
A failure has been detected at the local pseudowire endpoint. 
Remote Fail 
A failure is reported by the remote pseudowire endpoint. 
 To display PW configuration summary:  
• 
At the config>pwe# prompt, enter the show summary command. 
For example:  
billingssvc>config>pwe# show summary 
 
PW       : 1                         Name     : pw-1 
PSN Type : Ethernet                  PW Type  : CES PSN Data 
Oper     : Down 
 
Peer                   : 1 
IP Addr                : 0.0.0.0 
Next Hop Mac           : 00-00-00-00-00 
Out Label              : 1 
In Label               : 1 
Jitter Buffer          : 2500            Payload Size         : 1        
Configuration Errors  
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 
8. Traffic Processing 
Pseudowire Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
460 
Error 
SAME IP FOR ROUTER INTERF 
& D.GATEWAY 
The same IP address has been defined for both the default 
gateway and for one of the router interfaces. This is not 
allowed. 
Note however that this error may also appear because the 
default IP address (0.0.0.0) have not yet been changed. 
463 
Error 
IN PW LABEL IS NOT UNIQUE 
This message, which is generated only after the specified 
pseudowire is switched to the no shutdown state, 
indicates that two or more pseudowires have the same 
source UDP port number (the check is made irrespective of 
the pseudowire PSN type, UDP/IP or Ethernet). This is not 
allowed. 
464 
Error 
IP & NEXT HOP ARE THE 
SAME FOR STATIC ROUTE 
 
This message is generated after the specified static route is 
updated, and indicates that the next hop IP address and 
the destination IP address of the route are the same.  
This is not allowed – the addresses must be different. If the 
next hop IP address is not needed, leave the default value, 
0.0.0.0. 
Note however that this error may also appear because the 
default IP addresses (0.0.0.0) have not yet been changed. 
465 
Error 
STATIC ROUTE IP IS NOT 
UNIQUE 
This message, which is generated only after the specified 
static route is updated, indicates that the route destination 
IP address is already used in another static route. 
This is not allowed – only one static route may be defined 
for any specific destination IP address. 
Note however that this error may also appear because the 
default IP addresses (0.0.0.0) have not yet been changed 
466 
Error 
ROUTER INTERF CAN'T BE ON 
THE SAME SUBNET 
The IP addresses assigned to the router interfaces must be 
in different IP subnets. 
467 
Error 
MORE THAN 16 PWS FOR DS1 
PORT 
You are trying to connect too many pseudowires to the 
same ds1 port (the maximum is 16 pseudowires per port). 
469 
Error 
DS1 PORT OF PW IS DOWN 
The ds1 port assigned to a pseudowire is set to shutdown. 
Change its setting to no shutdown. 
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
471 
Error 
NUMBER OF BYTES IN FRAME 
EXCEEDS MAXIMUM  
 
In CESoPSN, Payload data length is equal to {tdm-payload 
size * (number of timeslots cross-connected between the 
PW and DS1 port)}. 
Depending on the module type, this number must not 
exceed the following value:  
• VS-12, VS-6/BIN, VS-6/C37, TP and VS Voice basic 
modules: 256 bytes 
• VS modules with E1/T1 ports: 1900 bytes 
In SAToP, Payload data length is equal to {tdm-payload 
size}. 
This number must not exceed 1900 bytes 
476 
Error 
PROTECTED PORTS HAVE 
ASSYMETRIC PARAMETERS 
When TDM protection is configured between two DS1 
ports, all their physical layer parameters must be identical  
477 
Error 
PEER DOESN'T EXIST 
You have specified a peer index during the creation of a 
pseudowire, but the peer has not yet been created. 
478 
Error 
PEER NEEDS ROUTER 
INTERFACE 
It is not possible to configure peers before at least one 
router interface has been configured. 
480 
Error 
PEER NOT ATTACHED TO PW 
You have created a PEER without attaching it to any 
pseudowire.  
493 
Error 
STATIC ROUTE ADDRESS 
DOES NOT MATCH 
Next hop address of static route is invalid  
494 
Warning 
WRONG PAYLOAD SIZE FOR 
SIGNALING 
 
 
In the case of voice with signaling transferred with 
CESoPSN protocol, the following restrictions apply 
depending on the type of port bound to this PW.  
E1 port:  tdm-payload size value must be 1, 2, 4, 8, or 16.  
T1 port:  tdm-payload size value must be 1, 2, 3, 4, 6, 8, 
12, or 24.  
Payload data length is equal to {tdm-payload size * 
(number of timeslots cross-connected between the PW 
and DS1 port)} 
Payload data length should be at least 4 bytes.  
498 
Warning 
ILLEGAL IP ADDRESS 
Overlapping of subnets between RI in Router1 & Router 2   
8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
499 
Error 
ILLEGAL JITTER BUFFER 
DEFINITION 
 
Maximum JB Size  
The maximum JB size depends on the module type: 
• VS-12, VS-6/BIN, VS-6/C37, TP and VS Voice basic 
modules: 8000  µsec 
• Other VS modules: 256 msec. 
Minimum JB Size 
The minimum JB size depends on the PW type and payload 
type: 
• CES over PSN 
When working without signaling: 
Minimum JB size = TDM payload size * 125  µsec * 2 = 250 
µsec. 
When working with signaling: 
Minimum JB size = 16(E1)/24(T1)*125 µsec * 2 
(E1 – 4000  µsec, T1 – 6000  µsec). 
• SATOP 
Minimum JB size = (TDM payload size * 125  µsec / 32) * 2 
757 
Error 
PORT CAN BE BOUND TO 
SINGLE PW ONLY  
A DS1/Serial port can be cross-connected with only one 
PW port. 
759 
Error 
PW TYPE NOT SUPPORTED 
 
VS modules with E1/T1 ports support both CESoPSN and 
SAToP PW types. Other VS modules support CESoPSN only. 
760 
Error 
SERIAL PORT OF PW IS DOWN 
The serial port cross-connected with this PW, is in 
“shutdown” state. 
765  
Error 
ILLEGAL TUNNEL INDEX LABEL 
 
If an ingress label is configured for psn=mpls, the egress 
label must be configured as well, and vice versa. 
800 
Error 
BANDWIDTH EXCESSIVE 
COMBINATION 
For VS-12, VS-6/BIN, VS-6/C37, TP and VS Voice basic 
modules, the total Ethernet bandwidth available for PW is 
limited to 100M  
801 
Error 
EXCESSIVE PWS IN SLOT 
The number of PWs defined on the same slot exceeds the 
number indicated in Configuration Error Messages. 
802 
Error 
WRONG SVI EGRESS PORT  
When working with a MAC address peer, you have to 
configure and connect an SVI as an egress port to this PW. 
803 
Error 
PW XC TS ALREADY USED 
The same slot/port cannot be connected twice to the same 
PW. 

## 8.6 Quality of Service (QoS)  *(p.740)*

8. Traffic Processing 
Code 
Type 
Syntax 
Meaning 
804 
Error 
PW XC TS 16 IN G732S USED 
If the E1 port cross-connected to the PW is using 
G732S/G732S-CRC framing, it cannot use timeslot 16.  
805 
Error 
WRONG PAYLOAD SIZE TS 
COMBINATION 
 
The following restrictions are valid for VS-6/703, 
SH-16/E1/PW, VS E1/T1 and VS voice PW-enhanced 
modules working with CESoPSN protocol. 
In CESoPSN, Payload data length is equal to {tdm-payload 
size * (number of timeslots cross-connected between the 
PW and DS1 port)}.   
The tdm-payload size value must not exceed 61.  
The minimum value of Payload data length can be equal to 
1 if the PW is attached to a serial or g703 port.  
In other cases, if the PW payload is without signaling, this 
value must be at least 2. If the PW payload is with 
signaling, this value must be at least 4. 
806 
Error 
PWS FROM DIFF SLOTS 
DEMAND DIFF RI/SVI  
The same Router Interface and/or SVI cannot be used for 
PWs residing on different I/O slots.  
820 
Error 
ONLY ONE PW PER DS1 IS 
ALLOWED 
You cannot connect more than one pseudowire to the DS1 
port of the PW-equipped VS modules (with the exception 
of VS-8E1T1/PW modules: in this case you can connect up 
to 16 PWs).                
8.6 Quality of Service (QoS)  
Megaplex-4 devices employ various traffic engineering techniques to optimize service delivery and 
ensure end-to-end QoS. They enable multi-criteria traffic classification as well as metering, policing and 
shaping to rate-limit user traffic according to CIR and EIR profiles. 
A 3-level hierarchical scheduling mechanism combines strict priority and weighted fair queue scheduling 
to handle different types of traffic. 
Weighted random early detection (WRED) policy is used for intelligent queue management and 
congestion avoidance. 
8. Traffic Processing 
Applicability and Scaling 
Most QoS features are defined by creating and applying various profiles. Profiles comprise sets of 
attributes related to a specific service entity. Profiles must be defined prior to other managed objects. 
Profile Types  
Applied to 
Profile Type 
Description 
Scale per Chassis 
Flow 
Classifier 
Defines criteria for flow 
classification 
128 
Flow 
Policer 
Define CIR, CBS, EIR and EBS 
parameters 
60 
Flow 
Marking 
Defines method of mapping CoS 
values into P-bit 
12 
Port (Ethernet) 
Queue group 
Defines level-0 and -1 scheduling 
elements and structures within 
queue group 
15  
Queue, queue 
block 
Shaper 
Defines CIR, CBS, EIR and EBS  
parameter 
30 
Queue 
WRED 
Defines green and yellow packet 
thresholds and drop probabilities  
8 
Queue block 
within queue 
group 
Queue block 
Defines queue block parameters 
(queues, scheduling scheme, 
weights) 
128 
 
Factory Defaults 
Refer to the following sections for the specific default for each type of QoS. 
Bandwidth Profiles 
Megaplex-4 supports the following bandwidth profiles: 
• 
Shaper profile – Applied to queue group blocks  
• 
Policer profile – Applied to flows to limit flow traffic, or to Ethernet ports to limit 
broadcast/multicast traffic   
8. Traffic Processing 
Note 
You can control the egress bandwidth utilization by defining the committed 
information rate and committed burst size in shaper and policer profiles. You 
can also define the excessive information rate and the excessive burst size in 
policer profiles.  
CIR: Defines the Committed Information Rate (CIR) for the current profile. The CIR specifies a bandwidth 
with committed service guarantee (“green bucket” rate). 
CBS: Defines the Committed Burst Size (CBS) for the current profile. The CBS specifies the maximum 
guaranteed burst size (“green bucket” size). 
EIR: Defines the Excess Information Rate (EIR). The EIR specifies an extra bandwidth with no service 
guarantee (“yellow bucket” rate). 
EBS: Defines the Excess Burst Size (EBS). The EBS specifies the extra burst with no service guarantee 
(“yellow bucket” size). 
Compensation: You can specify the amount of bytes that the shaper or policer can compensate for the 
layer 1 overhead (preamble and IFG) and the overhead for the added VLAN header in case of stacking. 
Factory Defaults 
Megaplex-4 provides default bandwidth profiles, as specified in the following table. The default policer 
profile Policer1 is the same for all kinds of ports, while the default shaper profile depends on the type of 
port: 
• 
GbeShaper for GbE ports of CL modules 
• 
MeShaper for GbE ports of M-ETH modules 
• 
LMShaper for Logical Mac ports 
Default Bandwidth Profiles 
Profile Type 
Shaper 
Policer 
Profile Name 
GbeShaper  
MeShaper 
LMShaper 
Policer1 
cir 
500000 
100000 
150000 
1000000 
cbs 
65535    
65535    
65535    
1048575 
eir 
– 
 
– 
– 
0 
ebs 
– 
 
– 
– 
0 
compensation 
0 
 
0 
0 
0 
8. Traffic Processing 
Profile Type 
Shaper 
Policer 
traffic-type 
– 
 
– 
– 
all 
Configuring Shaper Profiles  
You can define up to 30 shaper profiles. 
 To define a shaper profile: 
1. At the configure>qos# prompt, enter shaper-profile followed by profile name. 
The config>qos> shaper-profile(profile_name)$ prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying the CIR (Kbps) and 
CBS (bytes) bandwidth limits  
 
bandwidth [cir <cir-kbit-sec>] [cbs 
<cbs-bytes>] 
Typing no bandwidth removes 
the bandwidth limits. 
CIR allowed values: 0–1000000. 
CBS allowed values:  
• M-ETH: 4096–258048 
(4-252 Kbytes) 
• Other modules: 0, or 64–
1048575. 
Specifying the compensation 
(bytes) 
compensation <0–63> 
 
Example 
 To create and configure a shaper profile named Shap2: 
• 
CIR = 99,840 kbps 
• 
CBS = 32,000 bytes 
• 
Compensation = 48. 
# configure qos shaper-profile Shap2 
config>qos>shaper-profile(Shap2)$ bandwidth cir 99840 cbs 32000 
config>qos>shaper-profile(Shap2)$ compensation 48 
config>qos>shaper-profile(Shap2)$ 
8. Traffic Processing 
Configuring Policer Profiles 
When the flows are established, a metering and policing function can be applied to each flow on 
indirectly-attached ports to regulate traffic according to the contracted CIR, EIR, CBS and EBS bandwidth 
profiles.  
There is a restriction on the number of flows in the system employing “high-speed policers”, that is, 
policers that have total CIR + EIR greater than 100 Mbps. High-speed policer(s) cannot be used in more 
than 16 flows. Regular policers can be used without restriction.  
 To define a policer profile: 
1. At the configure>qos# prompt, enter policer-profile followed by profile name. 
The config>qos>policer-profile(profile_name)$ prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
8. Traffic Processing 
Task 
Command 
Comments 
Specifying the CIR 
(Kbps), CBS (bytes), EIR 
(Kbps), and EBS (bytes) 
bandwidth limits  
bandwidth [cir <cir-kbit-sec>] 
[cbs <cbs-bytes>] [eir <eir-kbit-sec>] 
[ebs <ebs-bytes>] 
 
 
Typing no bandwidth removes the 
bandwidth limits. 
CIR & EIR allowed values: 0–1000000. 
EBS allowed values: 0, or 64–1048575.  
CBS allowed values:  
• M-ETH: 4096–258048 (4-252 Kbytes) 
• Other modules: 0, or 64–1048575. 
CIR can be set to zero only if CBS is set to 
zero. 
EIR can be set to zero only if EBS is set to 
zero. 
CIR + EIR must not exceed the maximum 
available bandwidth. 
CBS should be greater than the maximum 
frame size. 
For policer profiles that will be attached 
to Ethernet ports to limit 
broadcast/multicast traffic, only the CIR 
and CBS parameters are relevant (EIR and 
EBS should be set to 0). 
The CIR and EIR granularity depend on 
the configured values. 
The CBS must be greater than or equal to 
the CIR divided by policer granularity. 
Specifying the 
compensation (bytes) 
compensation <0–63> 
 
Specifying the traffic 
type 
traffic-type {all | broadcast | multicast 
| unknown-unicast }  
Note: Traffic types other than all are 
relevant only for policer profiles attached 
to ports. 
8. Traffic Processing 
Granularity Rounding Down of CIR/EIR  
Policer Type 
CBS/EBS <= 
64,000 Bytes 
64,000 Bytes < 
CBS/EBS <= 
128,000 Bytes 
128,000 Bytes < 
CBS/EBS <= 
256,000 Bytes 
256,000 Bytes < 
CBS/EBS <= 
512,000 Bytes 
512,000 Bytes < 
CBS/EBS <= 
1,048,575 Bytes 
Port policer, or 
flow policer 
with CIR and 
EIR < 
100,000 Kbps 
64 Kbps  
128 Kbps  
256 Kbps  
512 Kbps  
1 Mbps  
Flow policer 
with CIR or EIR 
>= 
100,000 Kbps 
500 Kbps  
1 Mbps  
2 Mbps  
4 Mbps  
8 Mbps  
Note: The info command displays the CIR/EIR value: 
• Rounded down to 64 Kbps granularity for low-speed policers 
• Rounded down to 500 Kbps granularity for high-speed policers. 
Example 
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
Compensation = 56. 
Note 
CIR and EIR are rounded down to 64K granularity, as this is a low-speed 
policer with burst size < 64,000 bytes.  
# configure qos policer-profile Policer4 
config>qos>policer-profile(Policer4)$ bandwidth cir 50000 cbs 28000 eir 30000 ebs 20000 
config>qos>policer-profile(Policer4)$ compensation 56 
config>qos>policer-profile(Policer4)$ info detail 
    bandwidth cir  49984 cbs  28000 eir  29952 ebs  20000 
    traffic-type  all  
    compensation  56  
config>qos>policer-profile(Policer4)$ 
8. Traffic Processing 
 To create and configure a policer profile named PolicerPort: 
• 
CIR = 960 Kbps 
• 
CBS = 1,000 bytes  
• 
EIR = 0 
• 
EBS = 0  
• 
Traffic type = broadcast and multicast. 
# configure qos policer-profile PolicerPort 
config>qos>policer-profile(PolicerPort)$ bandwidth cir 960 cbs 1000 eir 0 ebs 0 
config>qos>policer-profile(PolicerPort)$ traffic-type broadcast-and-multicast 
config>qos>policer-profile(PolicerPort)$ info detail 
    bandwidth cir  960 cbs  1000 eir  0 ebs  0  
    traffic-type  broadcast-and-multicast 
    compensation  0 
config>qos>policer-profile(PolicerPort)$ exit all 
# configure port ethernet 5 
config>port>eth(5)# policer profile PolicerPort 
config>port>eth(5)# 
Queue Mapping Profiles  
Queue mapping profiles are used to convert the following user priorities into internal priority queues. 
Megaplex-4 supports up to 12 queue mapping profiles. 
• 
p-bit, when the ingress traffic is prioritized according to the 802.1p requirements 
• 
ip-dscp, when the ingress traffic is prioritized according to DSCP 
• 
ip-precedence, when the ingress traffic is prioritized according to IP precedence 
 
For each profile, you have to define the queue mapping to map the user priority values to the internal 
queue values. The internal queues are combined into a queue profile, which can be assigned to a queue 
block. 
8. Traffic Processing 
Factory Defaults 
Default Queue Mapping Profile 
Megaplex-4 provides a default queue mapping profile named CosProfile1, which can be used when the 
ingress traffic is prioritized according to the 802.1p requirements. It is defined with classification p-bit, 
and the following mappings: 
• 
Map p-bit 0 to queue 7 
• 
Map p-bit 1 to queue 6 
• 
Map p-bit 2 to queue 5 
• 
Map p-bit 3 to queue 4 
• 
Map p-bit 4 to queue 3 
• 
Map p-bit 5 to queue 2 
• 
Map p-bit 6 to queue 1 
• 
Map p-bit 7 to queue 0. 
Default Configuration for IP Precedence Classification  
When a new queue mapping profile is created with classification IP precedence, it contains the following 
mappings: 
• 
Map ip-precedence 0 to queue 7 
• 
Map ip-precedence 1 to queue 6 
• 
Map ip-precedence 2 to queue 5 
• 
Map ip-precedence 3 to queue 4 
• 
Map ip-precedence 4 to queue 3 
• 
Map ip-precedence 5 to queue 2 
• 
Map ip-precedence 6 to queue 1 
• 
Map ip-precedence 7 to queue 0. 
Default Configuration for DSCP Classification  
When a new queue mapping profile is created with classification DSCP, it contains the following 
mappings: 
8. Traffic Processing 
• 
Map ip-dscp XX to queue 7 
• 
Map ip-dscp XX to queue 6 
• 
Map ip-dscp XX to queue 5 
• 
Map ip-dscp XX to queue 4 
• 
Map ip-dscp XX to queue 3 
• 
Map ip-dscp XX to queue 2 
• 
Map ip-dscp XX to queue 1 
• 
Map ip-dscp XX through 63 to queue 0 
Adding Queue Mapping Profiles  
When you create a queue mapping profile, you specify the name and the classification method (p-bit, IP 
precedence, or DSCP). 
 To add a queue mapping profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type: 
queue-map-profile <queue-map-profile-name> classification {p-bit | ip-precedence | ip-dscp } 
A queue mapping profile with the specified name and classification method is created and the 
following prompt is displayed: 
config>qos>queue-map-profile (<queue-map-profile-name>)$. The mappings for the new 
profile are configured by default as described in Priority Queue Mapping. 
3. Configure the queue profile mappings as described in Error! Reference source not found.. 
Configuring Queue Mappings 
1. Navigate to config qos queue-map-profile <queue-map-profile-name> to select the queue 
mapping profile to configure. 
The following prompt is displayed: 
config>qos>queue-map-profile(<queue-map-profile-name>)# 
2. Map the user priorities to queue IDs as necessary: 
 
Classification p-bit or IP precedence: 
map <0-7> to-queue <0-7> 
8. Traffic Processing 
 
Classification DSCP: 
map <0-63> to-queue <0-7> 
 
Classification CoS: 
map <0-7> to-queue <0-7> 
Examples 
 To create and configure a queue mapping profile named QMapPbit with classification p-bit: 
• 
Map priority 0 to queue 3 
• 
Map priority 4 and 6 to queue 2. 
exit all 
configure qos queue-map-profile QMapPbit classification p-bit 
  map 0 to 3 
  map 4 to 2 
  map 6 to 2 
  exit all 
 To display the configuration information for queue mapping profile QMapPbit:  
# configure qos queue-map-profile QMapPbit 
config>qos>queue-map-profile(QMapPbit)# info detail 
    map  0 to-queue  3  
    map  1 to-queue  6  
    map  2 to-queue  5  
    map  3 to-queue  4  
    map  4..6 to-queue  2  
    map  7 to-queue  0 
 To create and configure a queue mapping profile named QMapIPprec with classification IP 
precedence: 
• 
Map priority 2 and 3 to queue 3. 
exit all 
configure qos queue-map-profile QMapIPprec classif ip-precedence 
  map 2 to 3 
  map 3 to 3 
  exit all 
 To display the configuration information for queue mapping profile QMapIPprec: 
# configure qos queue-map-profile QMapIPprec 
config>qos>queue-map-profile(QMapIPprec)# info detail 
    map  0 to-queue  7  
    map  1 to-queue  6  
8. Traffic Processing 
    map  2..4 to-queue  3  
    map  5 to-queue  2  
    map  6 to-queue  1  
    map  7 to-queue  0 
 To create and configure a queue mapping profile named QMapDSCP with classification DSCP: 
• 
Map priority 7 to queue 6 
• 
Map priority 55 to queue 4 
• 
Map priority 63 to queue 5. 
exit all  
configure qos queue-map-profile QMapDSCP classif ip-dscp 
  map 7 to 6 
  map 55 to 4 
  map 63 to 5 
  exit all 
 To display the configuration information for queue mapping profile QMapDSCP: 
# configure qos queue-map-profile QMapDSCP 
config>qos>queue-map-profile(QMapDSCP)# info detail 
    map  0 to-queue  7  
    map  1 to-queue  6  
    map  2 to-queue  5  
    map  3 to-queue  4  
    map  4 to-queue  3  
    map  5 to-queue  2  
    map  6 to-queue  1  
    map  7 to-queue  6  
    map  8..54 to-queue  0  
    map  55 to-queue  4  
    map  56..62 to-queue  0  
    map  63 to-queue  5 
Marking Profiles  
Marking profiles map the P-bit, IP precedence, DSCP, or CoS classifications to the egress priority tags. 
The marking can also be done per color (green and/or yellow), to support color re-marking, optionally 
specifying the Drop Eligible Indicator (DEI) bit in the frame header. Megaplex-4 supports up to 12 
marking profiles. 
8. Traffic Processing 
Factory Defaults 
Megaplex-4 provides a default non color-aware marking profile named MarkingProfile1, which can be 
used when the ingress traffic is prioritized according to the 802.1p requirements. It is defined with 
classification p-bit and method p-bit, and the following markings: 
• 
P-bit 0 => priority 0 
• 
P-bit 1 =>priority 1 
• 
P-bit 2 =>priority 2 
• 
P-bit 3 =>priority 3 
• 
P-bit 4 =>priority 4 
• 
P-bit 5 =>priority 5 
• 
P-bit 6 =>priority 6 
• 
P-bit 7 =>priority 7. 
When a non color-aware marking profile is created, it has the same configuration as MarkingProfile1. 
Configuring Marking Profiles 
 To define a marking profile and assign a priority mark to it: 
1. Navigate to the qos context (config>qos). 
2. Define the marking profile and assign a classification and a method to it: 
3. marking-profile <marking-profile-name>  
[classification {p-bit | ip-precedence | ip-dscp} [method p-bit] [color-aware {none | 
green-yellow}    
To define a color-aware profile, specify color-aware green-yellow.  
Queue Block Profiles 
In order to facilitate congestion management, you can sort traffic by applying queue block profiles to 
queue block entities. A queue block profile contains entries for queues 0–7, with the following 
parameters: 
• 
Scheduling method: 
8. Traffic Processing 
 
Strict – High-priority queues that are always serviced first. If a lower-priority queue is being 
serviced and a packet enters a higher queue, that queue is serviced immediately. 
 
WFQ (weighted fair queuing) – If one port does not transmit, its unused bandwidth is shared 
by the ‘transmitting’ queues according to the assigned weight. 
In configurations with Strict and WFQ queues, the WFQ frames are transmitted only after the 
transmission of frames associated with the Strict queues is completed. 
Note 
If one of the internal queues is configured to WFQ, queues with a higher 
queue ID cannot be configured to Strict.  
• 
Depth (queue size), in bytes. 
Factory Defaults 
Megaplex-4 provides a default queue block profile (for level 0) named DefaultQueue1, which defines 
queues 0–7 as follows:  
• 
Congestion avoidance: WRED profile corresponding to queue 
• 
Scheduling method: WFQ, with weight set to 100 
• 
Depth: 49152 bytes.   
Default queue block profiles for level 1 are defined as "Scheduling1" to "Scheduling8", with no 
congestion avoidance and Scheduling method WFQ, with weight set to 100. 
Adding Queue Block Profiles 
You can define up to 16 queue block profiles.The Megaplex-4 device may create up to 16 additional 
queue block profiles for internal usage. 
 To add a queue block profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type:  
queue-block-profile <queue-block-profile-name> 
A queue block profile with the specified name is created and the 
config>qos>queue-block-profile(<queue-block-profile-name>)$ prompt is displayed. The 
queues for the new profile are configured by default as described in Error! Reference source not 
found.. 
3. Configure the queue block profile as described in Error! Reference source not found.. 
8. Traffic Processing 
Configuring Queue Block Profile  
 To configure a queue block profile: 
1. Navigate to config qos queue-block-profile <queue-block-profile-name> to select the queue 
block profile to configure. 
The config>qos>queue-block-profile(<queue-block-profile-name>)# prompt is displayed. 
2. Perform the following for each queue that you wish to configure: 
a. To configure a queue, enter: 
queue <queue-ID> 
The following prompt is displayed: 
config>qos>queue-block-profile(<queue-block-profile-name>)>queue(<queue-ID>)#. 
b. Enter all necessary commands according to the tasks listed below. 
c. Type exit to return to the queue block profile context. 
Task 
Command 
Comments 
Setting scheduling 
method  
scheduling { strict | wfq 
<weight>} 
The weight range is 3–110 
Specifying queue 
depth (in bytes) 
depth <value>  
 
Allowed range: 0–1048576 
Notes:  
• The queue depth that you configure might be 
changed by Megaplex-4 due to granularity 
(see table below). After you configure the 
queue depth, it is recommended to use info 
detail to see the actual value 
• A queue block has 1 MB available, therefore 
the sum of the depths of its eight queues 
must be no greater than 1,048,576 
. 
Assigning a WRED 
profile to the 
internal queue  
congestion-avoidance 
wred profile <wred-profile-
name> 
 
You can assign a default profile 
(DefaultWREDProfile) to the internal queue or 
modify it, if needed. 
no congestion-avoidance wred removes a WRED 
profile association. 
8. Traffic Processing 
Queue Depth Granularity 
Entered Via CLI 
Granularity 
0–1024 
64 
1025–16383 
1024 
16384–262143 
16384 
262144–1048576 
262144 
Example 
 To create and configure a queue block profile named QBlockProf1: 
• 
Queue 0 set to strict scheduling and depth 524,288 
• 
Queue 1 set to strict scheduling and depth 212,992 
• 
Queue 7 set to WFQ scheduling with weight 75. 
# configure qos queue-block-profile QBlockProf1 
config>qos>queue-block-profile(QBlockProf1)$ queue 0 
config>qos>queue-block-profile(QBlockProf1)>queue(0)$ scheduling strict 
config>qos>queue-block-profile(QBlockProf1)>queue(0)$ depth 524288 
config>qos>queue-block-profile(QBlockProf1)>queue(0)$ exit 
config>qos>queue-block-profile(QBlockProf1)# queue 1 
config>qos>queue-block-profile(QBlockProf1)>queue(1)# scheduling strict 
config>qos>queue-block-profile(QBlockProf1)>queue(1)# depth 212992 
config>qos>queue-block-profile(QBlockProf1)>queue(1)# exit 
config>qos>queue-block-profile(QBlockProf1)# queue 7 
config>qos>queue-block-profile(QBlockProf1)>queue(7)# scheduling wfq 75 
config>qos>queue-block-profile(QBlockProf1)>queue(7)# 
Queue Group Profiles 
In order to facilitate congestion management, you can sort traffic by applying one queue group profile 
per port. You can define up to 8 queue group profiles per Megaplex-4 unit.  Each queue group can 
contain up to 8 queue blocks in level 0 and one queue block in level 1.  
Factory Defaults 
Megaplex-4 provides default five queue group profiles. The profiles depend on the type of port and are 
as follows: 
8. Traffic Processing 
• 
"GbeDefaultQueueGroup" for GbE ports of CL modules: 
#   queue-group-profile  "GbeDefaultQueueGroup" 
        queue-block  1/1 
            name  "Level1QueueBlock" 
            profile  "Scheduling1" 
        exit 
        queue-block  0/1 
            name  "Put your string here" 
            profile  "DefaultQueue1" 
            bind queue  0 queue-block  1/1 
            shaper profile  "GbeShaper" 
        exit 
• 
"MeDefaultQueueGroup" for GbE ports of M-ETH modules 
#   queue-group-profile  "MeDefaultQueueGroup" 
        queue-block  1/1 
            name  "Level1QueueBlock" 
            profile  "Scheduling5" 
        exit 
        queue-block  0/1 
            name  "Put your string here" 
            profile  "DefaultQueue1" 
            bind queue  0 queue-block  1/1 
            shaper profile  "MeShaper" 
        exit 
• 
“LMDefaultQueueGroup” for Logical Mac ports 
#   queue-group-profile  "LMDefaultQueueGroup" 
        queue-block  1/1 
            name  "Level1QueueBlock" 
            profile  "Scheduling4" 
        exit 
        queue-block  0/1 
            name  "Put your string here" 
            profile  "DefaultQueue1" 
            bind queue  0 queue-block  1/1 
            shaper profile  "LMShaper" 
        exit 
For the default profiles mentioned in the above screens see the following sections: 
• 
Shaper profiles – Error! Reference source not found.  
• 
DefaultQueue1, Scheduling{1-5}  – Error! Reference source not found.  
8. Traffic Processing 
Adding Queue Group Profiles 
 To add a queue group profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type: 
queue-group-profile <queue-group-profile-name>. 
A queue group profile with the specified name is created and the following prompt is displayed:  
config>qos>queue-group-profile(<queue-group-profile-name>)$ 
3. Configure the queue group profile as described in Error! Reference source not found.. 
Configuring Queue Group Parameters 
 To configure a queue group profile: 
1. Navigate to config qos queue-group-profile <queue-group-profile-name> to select the queue 
group profile to configure. 
The config>qos>queue-group-profile(<queue-group-profile-name>)# prompt is displayed. 
2. Select a queue block in level 0 or 1 to configure: 
queue-block 0/<1–8>  
queue-block 1/1 
Note 
Level 1 Queue Block profile must be unique per Queue Group 
The following prompt is displayed: 
config>qos>queue-group-profile(<q-grp-profile-name>)>queue-block(<level/ID>)# 
3. Enter all necessary commands according to the tasks listed below. 
4. If you wish to configure another queue block, type exit to return to the queue group profile 
context, and start again at Step 2. 
Task 
Command 
Comments 
Assigning a name to the queue 
block  
name <block-name> 
 
Note 
Normally there is no need for you to enter the bind command. When you add 
a queue block in level 0 to the profile, bind is done automatically. 
You cannot use the bind command if the queue group contains a single 
queue block in level 0.  
8. Traffic Processing 
Example 
Note 
This example uses the shaper profile and queue block profile created in the 
examples in the preceding sections.  
 To create and configure a queue group profile named QGroupProf1: 
• 
Queue block 0/1: 
 
Queue block profile: QBlockProf1 
 
Shaper profile: Shap2. 
Note 
Queue blocks 1/1 and 0/2 are automatically created.  
# configure qos queue-group-profile QGroupProf1 
config>qos>queue-group-profile(QGroupProf1)$ queue-block 0/1 
config>qos>queue-group-profile(QGroupProf1)>queue-block(0/1)$ profile QBlockProf1 
config>qos>queue-group-profile(QGroupProf1)>queue-block(0/1)$ shaper profile Shap2 
config>qos>queue-group-profile(QGroupProf1)>queue-block(0/1)$ exit 
config>qos>queue-group-profile(QGroupProf1)$ info detail 
    queue-block  1/1 
        name  "Level1QueueBlock" 
        profile  "Scheduling2" 
    exit 
    queue-block  0/1 
        name  "Put your string here" 
        profile  "QBlockProf1" 
        bind queue  0 queue-block  1/1 
        shaper profile  "Shap2" 
    exit 
    queue-block  0/2 
        name  "Put your string here" 
        profile  "DefaultQueue1" 
        bind queue  1 queue-block  1/1 
        shaper profile  "Shaper1" 
    exit 
WRED Profiles 
The WRED mechanism defines the probability of dropping yellow packets depending on the current 
queue usage. This avoids traffic congestion and ensures the forwarding of green packets. You can 
configure the following: 
• 
Minimum threshold – Defines the queue usage at which the WRED mechanism starts to drop 
yellow packets 
8. Traffic Processing 
• 
Maximum threshold – Defines the queue usage above which the WRED mechanism drops all 
yellow packets 
• 
Probability –Determines the percentage of packets to be dropped when the queue usage 
reaches the maximum threshold 
There are eight WRED profiles available, named WREDProfile0 through WREDProfile7. They are bound 
to the queues automatically: WREDProfile0 is bound to queue 0, WREDProfile1 is bound to queue 1, etc. 
You cannot delete the WRED profiles, and you cannot add more WRED profiles. The binding of the 
profiles to the queues is set and cannot be changed, but you can change the profile parameters. You can 
view the assignment of WRED profiles to queues via the info command in the queue block profile level. 
Note 
The WRED mechanism is activated only when you use a policer profile with EIR 
set to a nonzero value.  
Factory Defaults 
There are eight WRED profiles available, named WREDProfile0 through WREDProfile7, bound to the 
corresponding queues.  
Configuring WRED Profiles 
 To configure WRED profiles: 
1. Navigate to configure qos and type wred-profile WREDProfile<n> where n is 0 through 7. 
The config>qos>wred-profile(WREDProfile<n>)# prompt is displayed. 
2. Enter: 
color yellow min <min-threshold> max <max-threshold> [probability <max-probability>] 
 
min-threshold –Queue usage minimum threshold in percentage, 0–100 
 
max-threshold –Queue usage maximum threshold in percentage, 0–100 
 
max-probability – Percentage of packets to be dropped when the queue usage reaches the 
maximimum limit. 
Note 
You can configure the parameters for the color yellow only.  
Example 
 To configure WRED profile 4: 
• 
Minimum threshold 64 

## 8.7 Router (Management)  *(p.760)*

8. Traffic Processing 
• 
Maximum threshold 100 
• 
Probability 50. 
# configure qos wred-profile WREDProfile4 
config>qos>wred-profile(WREDProfile4)# color yellow min 64 max 100 probability 50  
config>qos>wred-profile(WREDProfile4)# info detail 
    color  yellow min  64 max  100 probability  50 
config>qos>wred-profile(WREDProfile4)# 
8.7 Router (Management)  
Each router interface is assigned an IP address and can be bound to one of the Megaplex-4 ports. 
Management Router is configured at the router(1) level. 
Note 
There are two routers in the Megaplex-4 architerchure: Router 1 is used for 
inband management, while Router 2 is used for pseudowire routing. Router 2 
is explained in the Error! Reference source not found. section.  
Megaplex-4 supports Proxy ARP functionality defined in RFC 1027.  
Note 
Only IP addresses that are not included in the Interface #1 subnet can be 
represented by Proxy-ARP. These IP addresses must be learned from the 
management ports operating with RIP routing protocol.  
Applicability and Scaling 
The router supports up to 128 interfaces for binding TDM (E1, T1, E1-i, T1-i) ports and up to 4 interfaces 
for binding SDH/SONET ports. 
Benefits 
Router is used for segmenting a LAN, increasing network performance and making packet forwarding 
more efficient.  
Factory Defaults  
The router interface RI#1 is created automatically and included into the default configuration file.  
8. Traffic Processing 
Configuring Inband Management  
To define inband management through E1/T1 and SDH/SONET ports with its parameters (dcc 
encapsulation, mode and routing-protocol for sdh-sonet ports), protocol and routing-protocol for e1, t1, 
e1-i, t1-i ports), refer to the relevant section in Chapter 5: E1 ports for e1 and e1-i ports, T1 ports for t1 
and t1-i ports, SDH/SONET ports for sdh-sonet ports. 
Since inband management is transported over low speed channels and routing is done by Host SW, the 
recommended quantity of nodes managed inband (DCC or DTS) is 5. Larger chains must be fragmented 
by connecting node#6 via high speed out-of-band link, for example VCG or Serial Bundle over full 
E1/T1.   
In applications based on Megaplex-4 ver 3.0 and up, only RIP-2 protocol must be used due to its 
capability to advertize subnets and single IP addresses, compared to Proprietary RIP that supports 
advertizing only single IP addresses. Use Proprietary RIP only on links attached to older Access+ products 
such as Megaplex-2100/2104, DXC, FCD etc. 
Loopback Router Interface 
A loopback router interface is a virtual interface, whose IP address can be used as IP address of the 
Megaplex device. Its IP address is not in either of the Router subnets and published to the Router via 
RIP.  
The loopback interface is not part of Factory default and is not bound to any physical or virtual port. 
Once configured, it is always up, and its IP address is used as device address, as an alternative of the IP 
address of RI#1.  
Any Router 1 interface can be declared a loopback type, excluding #1.  
Configuring the Management Router 
Router configuration includes the following steps: 
1. Adding a router instance 
2. Add and configure router interfaces (1–132, 1) 
Each router interface is assigned an IP address and can be bound to one of the Megaplex-4 ports.  
8. Traffic Processing 
 To configure a router instance: 
1. Navigate to config>router(1)#.  
Note 
Configuring Router 2 is explained in the Error! Reference source not found. 
section.  
2. Configure the router as illustrated and explained below.  
Task 
Command 
Comments 
Enabling address aging 
function 
arp-timeout   
 
Using no arp-timeout disables address 
aging function 
Administratively enabling the 
router interface 
no shutdown 
Using shutdown  administratively 
disables the router interface  
Configuring router interfaces, 
see below 
interface <1–132> 
 
Using no interface <port_number> 
deletes the router interface 
Interface #1 is already defined as part 
of the Default configuration. However 
it can be configured at the interface 
level (see below) 
Configuring the static route 
and the next gateway (next 
hop) using the next hop’s IP 
address 
static-route <IP-address/ 
IP-mask-of-static-route> 
address 
<IP-address-of-next-hop> 
priority  <1..255> 
The next hop must be a subnet of one 
of the router interfaces 
A particular case of a static route is 
default gateway, which is defined in 
Megaplex-4 by configuring a static 
route 0.0.0.0/0.  
Displaying the router ARP table 
show arp-table              
 
Displaying the routing table 
show routing-table  
 
• 
 
Note 
The following IP addresses cannot be used for router interfaces: 
• 
 255.255.255.255 – limited broadcast  
• 
 127.x.x.x   – loopback network 
• 
 0.0.0.0  –  this host 
• 
 224.x.x.x  – classes D and E 
• 
 x.y.z.255  – directed broadcast for net 
• 
 1.1.1.x or zero mask.  
8. Traffic Processing 
The following actions can be performed at the interface level, at the 
config>router(1)>interface(interface_number)# prompt. 
Task 
Command 
Comments 
Assigning a short name to 
the router interface 
name <string> 
Using no name removes the name 
Administratively enabling 
the router interface 
no shutdown 
Using shutdown  administratively 
disables the router interface  
Defining the router 
interface to be of the 
loopback type 
loopback 
The loopback interface cannot be 
bound to any physical or logical port. 
Only one loopback interface can be 
defined for the Megaplex device. 
Assigning IP address and 
subnet mask to the router 
interface 
address <IP-address/IP-mask> 
 
 
     
 
For creating subnets, RAD 
recommends using an IP subnet 
calculator, for example 
http://www.wildpackets.com/. Use 
the following guidelines: 
• When designing a ring, assign to 
each interface a small subnet 
which contains a minimum of IP 
addresses (2 -3).  
• Subnets inside the ring should 
not overlap, that is the ring no 
two addresses inside the ring 
should be identical. 
• IP-mask for loopback interface 
must be /32. 
Binding the router 
interface to an sdh-sonet, 
e1, t1, e1-i, or t1-i port  
bind { sdh-sonet | e1 | t1 | e1-i 
| t1-i } <slot/port> 
 
To remove the binding, you must 
delete the router interface (use no 
interface command)  
Binding the router 
interface #1 to an SVI port 
bind svi <port-number>  
 
 
 
Router interface #1 is bound to SVI 
port #1 by default. It is not 
recommended to change this 
binding. 
Using no before bind removes the 
binding 
8. Traffic Processing 
Task 
Command 
Comments 
Enabling/disabling IP 
forwarding 
ip-forwarding  
no ip-forwarding  
 
 
Disabling ip-forwarding (setting to 
no ip-forwarding) will prevent 
transferring any packet from other 
interfaces towards this interface. 
Setting maximum frame 
size (in bytes) to transmit 
(frames above the 
specified size are 
discarded) 
mtu <bytes> 
 
Possible values are: 200, 1280..1500 
bytes. 
Default values: 
• For inband management over 
dedicated time slot: 200 
• Other cases: 1500. 
Enabling RIP-2 protocol 
(interface #1 only) 
rip  v2 
This option is possible only after 
RI#1 is bound to SVI. 
Using no rip disables the protocol 
Displaying the Routing Table 
The routing table displays the following entries: 
• 
Interfaces configured by the user provided they are synchronized (#27, #28, #29 in our 
example). These interfaces are marked with Protocol “Local”.  
• 
Static routes configured by the user, including the default gateway, or static route 0.0.0.0/0 (in 
our example #1). These interfaces are marked with Protocol “Static”.  
• 
Interfaces learned from different protocols (in the example, the rest of the interfaces have been 
learned from the RIP protocol). 
For each interface the routing table includes the following: 
• 
IP Address/Mask     
• 
IP Address of the next hop  
• 
Routing protocol 
• 
Distance between this interface and the router IP addresses in hops (Metric-1). In the case of a 
static route Metric-1 denotes priority. 
8. Traffic Processing 
 To display a routing table: 
• 
At the config>router(1)# prompt, enter show routing-table. 
The routing table is displayed. 
 
Num IP Address/Mask     Next Hop       Protocol   Metric-1 
--------------------------------------------------------------- 
1.  0.0.0.0/0           172.17.173.1   Static     1 
2.  172.17.173.0/24     172.18.197.49  RIP        5 
3.  172.17.173.2/32     172.18.197.49  RIP        5 
4.  172.18.197.4/30     172.18.197.49  RIP        4 
5.  172.18.197.5/32     172.18.197.49  RIP        5 
6.  172.18.197.6/32     172.18.197.49  RIP        4 
7.  172.18.197.8/30     172.18.197.49  RIP        5 
8.  172.18.197.9/32     172.18.197.49  RIP        5 
9.  172.18.197.10/32    172.18.197.49  RIP        6 
10. 172.18.197.12/30    172.18.197.49  RIP        3 
11. 172.18.197.13/32    172.18.197.49  RIP        4 
12. 172.18.197.14/32    172.18.197.49  RIP        3 
13. 172.18.197.16/30    172.18.197.58  RIP        5 
14. 172.18.197.17/32    172.18.197.58  RIP        5 
15. 172.18.197.18/32    172.18.197.49  RIP        6 
16. 172.18.197.24/30    172.18.197.49  RIP        4 
17. 172.18.197.25/32    172.18.197.49  RIP        4 
18. 172.18.197.28/30    172.18.197.58  RIP        5 
19. 172.18.197.29/32    172.18.197.58  RIP        5 
20. 172.18.197.32/30    172.18.197.49  RIP        6 
21. 172.18.197.33/32    172.18.197.49  RIP        6 
22. 172.18.197.36/30    172.18.197.49  RIP        3 
23. 172.18.197.37/32    172.18.197.49  RIP        3 
24. 172.18.197.40/30    172.18.197.49  RIP        2 
25. 172.18.197.41/32    172.18.197.49  RIP        3 
26. 172.18.197.42/32    172.18.197.49  RIP        2 
27. 172.18.197.50/30    0.0.0.0        Local      0 
28. 172.18.197.53/30    0.0.0.0        Local      0 
29. 172.18.197.57/30    0.0.0.0        Local      0 
30. 172.18.197.58/32    172.18.197.58  RIP        2 
Configuration Errors  
The table below lists messages generated by Megaplex-4 when a configuration error is detected. 
8. Traffic Processing 
Configuration Error Messages  
Code 
Type 
Syntax 
Meaning 
405 
Error 
MORE THAN ONE TRAP 
SOURCE ADDRESS 
Only one loopback trap source address can be defined in 
Megaplex-4 
 
406 
Error 
TRAP SOURCE ADDRESS DOES 
NOT MATCH 
The configured trap source address matches neither of IP 
addresses existing in the Megaplex device  
445 
Error 
MORE THAN ONE LOOPBACK 
INTERFACE 
Only one loopback interface can be defined in Megaplex-4 
 
446 
Error 
LOOPBACK INTERFACE MUST 
BE HOST 
The loopback interface mask must be /32 
447 
Error 
MORE THAN ONE SVI PORT 
BOUND 
Only one SVI port can be bound to the router 1 interface 
448 
Error 
RI NOT BOUND TO PORT OR 
PORT SHUTDOWN 
This router interface is either not bound to any port or 
bound to a port which is in shutdown state 
449 
Error 
ILLEGAL IP ADDRESS 
 
One of the following: 
• The IP address is illegal (for example, it is a subnet ID or 
subnet broadcast ID)   
• The IP address of the interface in Router 2 overlapped 
the IP address of our intercommunication address 
1.1.1.x 
Example 
Management Connectivity Diagram shows an application with four Megaplex-4 nodes (MP1, MP2, MP3, 
MP4) connected by an SDH ring. The central node (MP1) is connected via its control port to the 
Management router which manages the entire network. The nodes are connected via small subnets, 
and four different colors designate IP addresses from the same subnet (for example, the yellow line 
from MP1 CL.A link 1 to MP2 CL.B link 1 connects two addresses from the same subnet: 172.17.197.5/30 
and 172.17.197.6/30).  
In each Megaplex the configuration procedure is as follows: 
1. Configure 2 SDH ports with DCC management 
2. Configure 2 router interfaces with subnets and bind them to SDH ports 
8. Traffic Processing 
Note 
Router interface 1 and SVI port 1 are present in the Megaplex-4 configuration 
as part of the factory default file and need not be created. By default, SVI port 
1 is bound to Router interface 1.  
In addition, for the central Megaplex-4 MP1 (IP address 172.17.173.1) you must configure the default 
gateway (static-route 0.0.0.0/0) and the next hop (static route). 
 
CL.B
2
172.17.173.1
172.17.174.1
1
CL.A
2
1
MP 4
CL.B
2
1
CL.A
2
1
MP 3
CL.B
2
1
CL.A
2
1
MP 2
CL.B
2
1
CL.A
2
1
MP 1
PC
172.17.174.54
 
Four Megaplex-4 Nodes in an SDH Ring 
Router (not part of the MP configuration) 
Next hop 172.17.197.0 172.17.173.2 
172.17.179.1/24 
MP 1 
Static Route* 
CL A 
172.17.173.2/24 
SVI 
Control 
172.17.173.2/24 
0.0.0.0/0 172.17.173.1 
CL A 
L1 
172.17.197.5/30 
CL B 
L1 
172.17.197.9/30 
8. Traffic Processing 
MP 2 
SVI 
172.17.197.25/30 
CL A 
L1 
172.17.197.13/30 
CL B 
L1 
172.17.197.6/30 
MP 3 
SVI 
172.17.197.29/30 
CL A 
L1 
172.17.197.17/30 
CL B 
L1 
172.17.197.14/30 
MP 4 
SVI 
172.17.197.33/30 
CL A 
L1 
172.17.197.10/30 
CL B 
L1 
172.17.197.18/30 
 
 
* A static-route is needed on the router to subnet 172.17.197.X 
#MP 1 
 
exit all 
configure slot cl-b card-type cl cl2-622gbe 
configure router 1 interface 1 address 172.17.173.2/24 
configure router 1 static-route 0.0.0.0/0 address 172.17.173.1 
 
configure port sdh-sonet cl-a/1 no shutdown 
configure port sdh-sonet cl-a/1 dcc encapsulation hdlc mode d1-to-d3 routing-protocol 
rip2 
configure router 1 interface 1 address 172.18.197.5/30 
configure router 1 interface 1 bind sdh-sonet cl-a/1 
configure router 1 interface 1 no shutdown 
 
configure port sdh-sonet cl-b/1 no shutdown 
configure port sdh-sonet cl-b/1 dcc encapsulation hdlc mode d1-to-d3 routing-protocol 
rip2 
configure router 1 interface 2 address 172.18.197.9/30 
configure router 1 interface 2 bind sdh-sonet cl-b/1 
configure router 1 interface 2 no shutdown 
commit 
save 
8. Traffic Processing 
 
#MP 2 
exit all 
configure slot cl-b card-type cl cl2-622gbe 
configure router 1 interface 1 address 172.18.197.25/30 
 
configure port sdh-sonet cl-a/1 no shutdown 
configure port sdh-sonet cl-a/1 dcc encapsulation hdlc mode d1-to-d3 routing-protocol 
rip2 
configure router 1 interface 1 address 172.18.197.13/30 
configure router 1 interface 1 bind sdh-sonet cl-a/1 
configure router 1 interface 1 no shutdown 
 
configure port sdh-sonet cl-b/1 no shutdown 
configure port sdh-sonet cl-b/1 dcc encapsulation hdlc mode d1-to-d3 routing-protocol 
rip2 
configure router 1 interface 2 address 172.18.197.6/30 
configure router 1 interface 2 bind sdh-sonet cl-b/1 
configure router 1 interface 2 no shutdown 
 
commit 
save 
#MP 3 
exit all 
configure slot cl-b card-type cl cl2-622gbe 
configure router 1 interface 1 address 172.18.197.29/30 
 
configure port sdh-sonet cl-a/1 no shutdown 
configure port sdh-sonet cl-a/1 dcc encapsulation hdlc mode d1-to-d3 routing-protocol 
rip2 
configure router 1 interface 1 address 172.18.197.17/30 
configure router 1 interface 1 bind sdh-sonet cl-a/1 
configure router 1 interface 1 no shutdown 
 
configure port sdh-sonet cl-b/1 no shutdown 
configure port sdh-sonet cl-b/1 dcc encapsulation hdlc mode d1-to-d3 routing-protocol 
rip2 
configure router 1 interface 2 address 172.18.197.14/30 
configure router 1 interface 2 bind sdh-sonet cl-b/1 
configure router 1 interface 2 no shutdown 
 
commit 
save 
 
#MP 4 
exit all 
configure slot cl-b card-type cl cl2-622gbe 

## 8.8 Router (Pseudowire)  *(p.770)*

8. Traffic Processing 
configure router 1 interface 1 address 172.18.197.33/30 
 
configure port sdh-sonet cl-a/1 no shutdown 
configure port sdh-sonet cl-a/1 dcc encapsulation hdlc mode d1-to-d3 routing-protocol 
rip2 
configure router 1 interface 1 address 172.18.197.10/30 
configure router 1 interface 1 bind sdh-sonet cl-a/1 
configure router 1 interface 1 no shutdown 
 
configure port sdh-sonet cl-b/1 no shutdown 
configure port sdh-sonet cl-b/1 dcc encapsulation hdlc mode d1-to-d3 routing-protocol 
rip2 
configure router 1 interface 2 address 172.18.197.18/30 
configure router 1 interface 2 bind sdh-sonet cl-b/1 
configure router 1 interface 2 no shutdown 
 
commit 
save  
 
 
8.8 Router (Pseudowire)  
The Megaplex-4 Router 2 function is used to route pseudowire packets generated by the VS and TP 
modules installed in the chassis to their destination (peers).  
Applicability and Scaling  
 
Attribute 
System 
VS 
TP 
Scaling/Comments 
Router 
✓ 
✓ 
✓ 
 
Router 
interfaces/ 
Peers (max) 
100 
12* 
4* 
*Per module 
Functional Description 
The terms and parameters needed by the Megaplex-4 router function to support pseudowire routing 
are explained below: 
8. Traffic Processing 
• 
Router interfaces: the Megaplex-4 Router 2 function supports up to 100 router interfaces, each 
assigned a unique index number. Each router interface has its own IP address; you must also 
specify an IP subnet mask, and the module and port on which interface is located.  
For each router interface, you can also enable the use of VLAN tagging and specify a VLAN ID, to 
enable differentiating the traffic carried by this router. Note that when the router interface is 
connected (via SVI) to a GbE port or a VCG, VLAN tagging is always enabled. 
Each VS or TP module supports up to 12 or 4 different router interfaces, respectively; additional 
interfaces can be configured on any bridge port in the Megaplex-4. The IP address of the 
appropriate interface is automatically inserted as the pseudowire source IP address. 
• 
Pseudowire peers: the pseudowire destination is referred to as the pseudowire peer. Megaplex-
4 supports up to 100 peers, each assigned a unique index number. The index number is then 
used to specify the pseudowire destination, instead of directly providing the necessary 
destination information. To configure a peer, it is necessary to provide its IP address, and as an 
option – the next hop IP address. The peers (the pseudowire destinations) and the associated 
routing information are defined under configure peer context.   
• 
Static routes: to control the paths used to reach the pseudowire destinations, the Megaplex-4 
router function supports the definition of up to 100 static routes, in addition to a default 
gateway.  
Within the Megaplex-4, pseudowires are forwarded to the appropriate exit port (always a router 
interface) by internal E-line Ethernet flows (an E-line flow is a type of Ethernet logical connection that 
interconnects two bridge ports).  
Each router interface serves as a bridge port for the pseudowires using it (in addition, each Megaplex-4 
Ethernet port also serves as a bridge port).  
To help you design the routing information, the flow chart below summarizes the process used to select 
the router interface for each pseudowire peer. The priority of the various router interfaces, as 
determined by the routing process, is as follows: 
1. If the peer IP address is in the subnet of a router interface, that interface will always be used. 
2. If the peer IP address is not within a router interface subnet, then the router checks if the 
specified peer next hop address is within the subnet of a router interface. If such a router 
interface is found, it is selected to serve as the pseudowire exit port. 
3. If neither of the previous conditions is fulfilled, the router checks if the specified peer next hop 
address is specified in a static route that is within the subnet of a router interface. 
4. The last priority is to use the router interface that is within the default gateway subnet.  
8. Traffic Processing 
DB Update
Peer IP address
in the subnet
of one of the
router interfaces
No
Yes
Peer Next Hop
in the subnet
of one of the
router interfaces
No
Look in static routes
table, for peer Next Hop in
the subnet of one
of the router interfaces
Find a router interface in
the default gateway
subnet
Select as the router interface in use
Yes
Yes
No
 
Selecting the Active Router Interface for an Ethernet Flow Serving a Pseudowire  
The PW Router is configured at the router(2) level. 
Adding and Configuring Router Interfaces 
Each router interface is assigned an IP address and can be bound to one of the Megaplex-4 ports.  
8. Traffic Processing 
Adding a Router Interface 
 To add a router interface: 
1.  Navigate to configure router 2. 
The config>router(2)# prompt is displayed.  
2. Type the interface command and enter an interface number in the 1–100 range.  
An interface is added and the config>router(2)>interface(number)# prompt is displayed. 
For example: 
 To add router interface 5: 
# config router 2 
config>router(2)# interface 5 
config>router 2 interface 5 bind svi 4 
 To delete router interface 5: 
config router 1 no interface 5 
Configuring the Router Interface 
After adding a router interface, you have to configure it. Once configuration is completed, you can 
display the routing table (see below). 
 To configure a router interface: 
• 
At the config>router(2)>interface(number)# prompt, enter all necessary commands according 
to the tasks listed below:  
Task 
Command 
Comments 
Assigning a short name 
to the router interface 
name <string> 
Using no name removes the name 
Administratively 
enabling the router 
interface 
no shutdown 
Using shutdown  administratively 
disables the router interface  
8. Traffic Processing 
Task 
Command 
Comments 
Assigning IP address and 
subnet mask to the 
router interface 
address <valid IP address with mask 
in the address/mask format> 
 
For creating subnets, RAD 
recommends using an IP subnet 
calculator, for example 
http://www.wildpackets.com/. Use 
the following guidelines: 
• Router interfaces must be on 
different subnets  
• When designing a ring, assign to 
each interface a small subnet 
which contains a minimum of IP 
addresses (2 -3)  
• Subnets inside the ring should 
not overlap, that is no two 
addresses inside the ring should 
be identical. 
Binding the PW router 
interface to an SVI port  
bind  svi  <port> 
 
This SVI port will be further 
connected (via flows) to an ethernet 
or logical mac port.  
Using no before svi removes the 
binding. 
  
Note 
The following IP addresses cannot be used for router interfaces: 
• 
 255.255.255.255 – limited broadcast  
• 
 127.x.x.x   – loopback network 
• 
 0.0.0.0  –  this host 
• 
 224.x.x.x  – classes D and E 
• 
 x.y.z.255  – directed broadcast for net 
• 
 1.1.1.x or zero mask.  
For example:  
 To configure a router interface 5:  
• 
IP address 172.17.171.217, subnet mask 24 
• 
Bound to SVI port 2 
# config router 2 
config>router(2)# interface 5 
8. Traffic Processing 
config>router 2 interface 5 bind svi 2 
 To delete router interface 5: 
config router 2 no interface 5 
Displaying the Routing Table 
The routing table displays the following entries: 
• 
Interfaces configured by the user on condition that they are synchronized (in our example #2, 
#3, #4). These interfaces are marked with Protocol “Local”.  
• 
Static routes configured by the user, including the default gateway, or static route 0.0.0.0/0 (in 
our example #1). These interfaces are marked with Protocol “Static”.  
For each interface the routing table includes the following: 
• 
IP Address/Mask     
• 
IP Address of the next hop  
• 
Routing protocol 
• 
Distance between this interface and the router IP addresses in hops (Metric-1). In the case of a 
static route Metric-1 denotes priority.  
 
Note 
Routing protocols for PW service are not supported. Thus when working with 
PWE services and configuring Router interface, the routing info for PWE 
service is updated in the routing table as soon as Peer IP is configured. 
 To display a routing table:   
# config router 2 
config>router(2)# show routing-table 
 
Num IP Address/Mask     Next Hop       Protocol   Metric-1 
----------------------------------------------------------- 
1.  0.0.0.0/0           172.18.170.1   Static     1 
2.  172.18.170.75/24    0.0.0.0        Local      0 
3.  172.17.151.55/24    0.0.0.0        Local      0 
8. Traffic Processing 
Configuring Static Routes and Default Gateway  
To control the paths used to reach the pseudowire destinations, the PW router supports the definition 
of up to 100 static routes, in addition to a default gateway.  
You can add fixed (static) routes to the Megaplex-4 routing table. A particular case of a static route is 
default gateway, which is defined in Megaplex-4 by configuring a static route 0.0.0.0/0.  
 To configure a static route:  
• 
At the config>router(2) # prompt, enter the static-route command as follows: 
• 
static-route <IP address/mask> address  <IP address of a next hop host> priority  <priority 1 to 
255> 
For example: 
 To configure a static route: 
• 
IP address – 10.10.10.10 
• 
Mask – 24 
• 
Next hop address –172.17.144.1 
• 
Priority – 5.  
configure router 2 static-route 10.10.10.10/24 address 172.17.144.1 priority 5 
 To delete a static route: 
configure router 2 no static-route 10.10.10.10/24 address 172.17.144.1 
 To configure a default gateway at the host with IP address 172.17.173.1: 
• 
Navigate to configure router 2. 
The config>router(2)# prompt is displayed. 
configure router 2 static-route 0.0.0.0/0 address 172.17.173.1 
 To remove a default gateway: 
config router 2 no static-route 0.0.0.0/0 address 172.17.173.1 
 