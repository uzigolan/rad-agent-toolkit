# 4 Service Provisioning

*Manual `MP-1-mn_ver 2.2.pdf`, pages 130–141.*


## 4.1 Service Entities  *(p.130)*

This chapter shows the data flow and configuration steps for services. 
The diagrams and tables in Sections 4.2 to 4.4 illustrate typical Megaplex-1 services. 
4.1 Service Entities 
This section describes the managed elements that need to be configured during service provisioning. 
Service provisioning elements are as follows: 
• 
Profiles 
• 
Scheduling and shaping entities 
• 
Physical ports (Ethernet – NNI and UNI, Voice, Serial, DS1-opt) 
• 
Logical ports (SVI, DS1) 
• 
Forwarding entities (flow, bridge, router) 
• 
Pseudowires (PW). 
Profiles 
Most traffic processing features are defined by creating and applying various profiles. Profiles comprise 
sets of attributes related to a specific service entity. Profiles must be defined prior to other managed 
objects. 
Profile Types  
Applied to 
Profile Type 
Description 
Scale per Chassis 
Described in 
Flow 
Classifier 
Defines criteria for flow 
classification 
20 
Chapter 8 
Megaplex-1 
4. Service Provisioning 
Applied to 
Profile Type 
Description 
Scale per Chassis 
Described in 
Port 
Policer  
Controls the egress 
bandwidth utilization for 
Ethernet ports by defining 
CIR and CBS 
12 
Chapter 8 
Port 
Queue group 
Defines level 0 scheduling 
elements and structures 
within queue group 
24 (2 default + 22 
additional) 
Chapter 8 
Port 
Queue mapping 
Defines method and 
values for mapping packet 
attributes (P-bit only) to 
internal priority queues 
3 (default + 2 
additional) 
Chapter 8 
Queue 
block 
within 
queue 
group 
Shaper  
Controls the egress 
bandwidth utilization by 
defining CIR and CBS 
1 shaper profile in 
each queue-group 
configured in the 
queue-block  
Total per chassis: 
126  
Chapter 8 
Queue 
block 
Queue internal  
Internal queues are tier-1 
scheduling elements, that 
use strict or WFQ 
scheduling techniques. At 
a later stage, they are 
combined into queue 
blocks.  
8 for GbE ports 
4 for FE ports  
Total per chassis: 9 
Chapter 8 
Queue 
block 
within 
queue 
group 
Queue block 
Defines queue block 
parameters (queues, 
scheduling scheme, 
weights) 
1 profile in queue-
group 
Total chassis: 10 
Chapter 8 
Voice 
ports 
Analog 
Signaling 
Specifies translation rules 
for signaling information 
2** 
Chapter 5 
• 
*1 for each Ethernet port: 4 UNI + 2 NNI ports  
• 
** Two signaling profiles are needed for FXS/E&M assembly 
Megaplex-1 
4. Service Provisioning 
Scheduling and Shaping Entities  
Megaplex-1 schedules traffic using the following hierarchical scheduling entities:  
• 
Queue – a lowest-level scheduling element. Its priority can be strict or weight fair.  
• 
Queue block (also referred to as scheduling element, or SE) – a mid-level scheduling element 
that consists of several queues. Queue blocks are created by associating queues with queue 
block profiles. Megaplex-1 has one level of queue blocks. Queue blocks have shaper profiles 
assigned to them.  
• 
Queue group – a top-level scheduling element that consists of one or several queue blocks. In 
Megaplex-1 it consists of one queue block. Queue groups are created by associating queue 
group profile to ports. 
The shaping tool provided by Megaplex-1 is Single leaky bucket shaper (CIR). 
Physical Ports 
Services provided by Megaplex-1 are based on its physical ports. These are Ethernet – NNI and UNI, 
E1/T1, Voice, Serial, and DS1-opt ports. 
Logical Ports 
Logical ports maintained by Megaplex-1 do not have physical port attributes and serve different 
purposes, depending on the service provided by the module/system physical ports. The following logical 
ports exist: 
• 
Service Virtual Interface (SVI) used for binding flows to bridge ports, router interfaces or Layer-2 
TDM pseudowires. SVIs serve as intermediaries for router interfaces and also serve as 
aggregation points for TDM PWs. 
• 
DS1 Ports used to connect between pseudowires and tributary (serial/voice/ds1-opt) ports.  
Forwarding Entities 
Several internal entities carry traffic and make forwarding and switching decisions. These are: 
• 
Flows – the main traffic-carrying elements 
• 
Bridge – traffic-forwarding element for Layer-2 E-LAN services 
Megaplex-1 
4. Service Provisioning 
• 
Router – traffic-forwarding element for Layer-3 services. 
Flows 
Flows interconnect two physical or logical ports and are the main traffic-carrying elements in Megaplex-
1 architecture. You can use classifier profiles to specify the criteria for flows. The classification is per port 
and is applied to the ingress port of the flow. 
Only bidirectional flows are used in Megaplex-1. 
Flow processing is performed as follows: 
• 
Ingress traffic is mapped in flows using classification match criteria defined via a classification 
profile. 
• 
User priority (P-bit) is mapped into queues according to a queue mapping profile assigned per 
port. 
• 
VLANs can be edited per flow by stacking (pushing), removing (popping) on single-, or double-
tagged packets. P-bit values are either copied or fixed based on flow editing configuration.  
• 
A flow is mapped to a queue block 0/1 within a queue group associated with egress port.  
Bridge 
The bridge is a forwarding entity used by Megaplex-1 for delivering any services in point-to-point or 
multipoint-to-multipoint topology. The bridge uses 18 bridge ports for connecting to logical and physical 
ports.  
The bridge is defined by bridge ports and a VLAN membership table that specifies which bridge ports are 
members in a certain broadcast domain (VLAN). The bridge supports one level of VLAN editing on 
ingress and one level on egress. The editing is performed at the flow level.  
Router  
The Megaplex-1 IPv4 static router is used for management and PW purposes only.  
The router uses service virtual interfaces (SVIs) for connecting to bridge ports. The connection is always 
made by directing flows from a SVI to bridge port. 
Megaplex-1 
4. Service Provisioning 
Pseudowires  
Pseudowires are an emulation of Layer-2 point-to-point connection-oriented services over packet-
switching networks (PSN). Each pseudowire can be independently routed to any destination.  
Megaplex-1 Port Reference 
The following table shows how to refer to the Megaplex entities when configuring them with CLI 
commands. 
Megaplex-1 Port Reference  
 Entity 
Syntax and Values 
ETH 1-4 – UNI (Fast Ethernet) ports 
ethernet <0/3..0/6 
GbE 1 – NNI port 1  
ethernet 0/1 
GbE 2 – NNI port 2  
ethernet 0/2 
MNG-ETH – Management Ethernet Port 
mng-ethernet 0/0 
Bridge ports 
bridge-port <1 1..1 18>  
Pseudowire 
pw <1..32>  
SVI ports 
svi <1..12> 
Router interface  
router 1 interface <1..10>  
DS1 ports 
ds1 <1/1..1/16>  
DS1 optical ports 
ds1-opt <1/1, 1/2> 
E&M voice ports 1..4 (6S/4E&M option) 
voice <1/1..1/4> 
 
E&M voice ports 1..4 (8FXS/4E&M option) 
voice <1/9..1/12> 
 
FXS voice ports 1..8 
voice <1/5..1/12> 
Serial ports 1..6 
serial <1/1..1/6> 
E1/T1 ports 1...8 
e1/t1 <1/1..1/8> 
 

## 4.2 Ethernet Service  *(p.135)*

Megaplex-1 
4. Service Provisioning 
4.2 Ethernet Service 
The diagram below shows the Ethernet service.  
1. Profiles
2. Physical Ports
Optional
Mandatory
Legend:
4. Flows
3. Logical Ports 
Configure 
Ethernet port
Ethernet Port
Configure 
ethernet port
Set Ethernet 
port parameters
Assign 
ingress and 
egress ports
Assign 
classifier 
profile
Configure flow 1
Define vlan 
editing 
actions
Flow 1a
Flow 1b
Assign 
ingress and 
egress ports
Define vlan 
editing 
actions
Assign 
classifier 
profile
 Bridge
BP
Flow 1
Flow 2
Set Ethernet 
port parameters
Configure flow 2
BP
Ethernet Port
classifier 
profile
queue mapping 
profile
queue mapping 
profile
classifier 
profile
Define bridge ports
 
Ethernet Service  
Provisioning Ethernet Service 
Sequence 
Step 
Commands 
Comments 
Defining 
Classifier Profiles 
 
flows flow classifier-
profile 
Create classifier profile “match-all” (see 
Chapter 8) 
Queue Mapping 
Profiles 
qos queue-mapping-
profile 
Configuring queue-mapping profiles (to be 
assigned to Ethernet ports) (see Chapter 8) 

## 4.3 TDM Service over UDP IP PW  *(p.136)*

Megaplex-1 
4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
2. Configure physical  
ports 
Ethernet Ports 
 
port ethernet 
Configuring physical parameters of 
Ethernet ports (see Chapter 5) 
Bind queue mapping profile (optional) (see 
Chapter 5) 
 
 
 
Bridge 
bridge port 
Configuring bridge ports (see Chapter 5) 
Configuring VLAN membership – optional 
(see Chapter 8) 
Flows 
flows>flow 
Define flow 1 and 2 
Assign classifier profile  
Define VLAN editing actions  
(see Chapter 8) 
  
4.3 TDM Service over UDP IP PW 
The diagram shows the serial/voice/DS1 TDM service over PSN using the UDP IP PW.  
Megaplex-1 
4. Service Provisioning 
1. Profiles
2. Physical ports
Optional
Mandatory
Legend:
7. Flows
4. Peer IP
6. Cross-connect
5. Pseudowires
3. Logical ports
Configure serial/
voice/ds1-opt port
Configure ds0 
cross-connect
TDM Port
DS1 Port
Ethernet
Configure 
ethernet port
Set Ethernet 
port parameters
Configure 
ds1 port
Define remote 
PW peer
Configure 
pw-tdm 
cross-connect
Assign 
ingress and 
egress ports
Assign 
classifier 
profile
Configure flow 
1
Define vlan 
editing 
actions
Router
Flow 1a
SVI
Flow 1b
RIF
Define RIFs
Define router 
interfaces
Bind router 
interfaces to SVIs
Add and 
configure a 
pseudowire
Assign 
ingress and 
egress ports
Configure flow 
2
Define vlan 
editing 
actions
Assign 
classifier 
profile
 Bridge
BP
Flow 1
Flow 2
classifier 
profile
Bind
Define SVI
PW
Peer IP
queue mapping 
profile
analog 
signaling profile
classifier 
profile
Define bridge ports
BP
 
Serial/Voice/DS1 service over PSN using the UDP IP PW  
 
Megaplex-1 
4. Service Provisioning 
TDM Service over UDP IP PW Provisioning 
Sequence 
Step 
Commands 
Comments 
1. Define profiles 
Defining 
Classifier Profiles 
 
flows flow classifier-
profile 
Create classifier profile “match-all” (see 
Chapter 8) 
Queue Mapping 
Profiles 
qos queue-mapping-
profile 
Configure queue-mapping profiles (to be 
assigned to Ethernet ports) (see Chapter 8) 
Analog Signaling 
Profiles 
port analog-
signaling-profile 
Define analog signaling profile for voice 
ports (see Chapter 5) 
2. Configure physical 
ports 
TDM Ports  
port serial 
port voice 
port ds1-opt 
Configure physical parameters of TDM 
ports (see Chapter 5)  
Ethernet Ports 
 
port ethernet 
Configure physical parameters of Ethernet 
ports (see Chapter 5) 
Bind queue mapping profile – optional (see 
Chapter 5) 
3. Configure logical ports 
DS1 Ports 
 
port ds1 
Configuring physical parameters of DS1 
ports (see Chapter 5)  
Router interface 
router interface  
Add interfaces to the router  
Bind the RIFs to the SVIs  
Define static routing table (optional) (see 
Chapter 8) 
Bridge ports 
bridge port 
Configuring bridge ports 
Configuring VLAN membership – optional 
(see Chapter 8) 
Service Virtual 
Interface 
port svi 
Define an SVI port (see Chapter 5) 
4. Define PW 
peer 
Peer 
peer 
Configure remote pseudowire peer 
Assign IP address 
Assign next hop IP address – optional (see 
Chapter 8) 

## 4.4 TDM Service over MEF-8 PW  *(p.139)*

Megaplex-1 
4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
5. Define 
pseudowire 
Pseudowires 
pwe 
Add and configure pseudowires 
Bind pseudowire to the peer (see Chapter 
8) 
 
6
. 
C
o
DS0 Cross-
connect  
cross-connect ds0 
Configure cross-connect between serial 
ports and timeslots of DS1 ports (see 
Chapter 8) 
PW-TDM 
Cross-connect  
cross-connect pw-tdm  
Configure cross-connect between 
serial/voice/ds1-opt ports and timeslots of 
DS1 port (see Chapter 8) 
Flows 
flows flow 
Define flow 1 and 2 
Assign classifier profile  
Define VLAN editing actions (see Chapter 8) 
4.4 TDM Service over MEF-8 PW 
The diagram shows the serial/voice/DS1-opt TDM service over PSN using the MEF-8 PW.  
Megaplex-1 
4. Service Provisioning 
1. Profiles
2. Physical ports
Optional
Mandatory
Legend:
6. Flows
5. Cross-connect
4. Pseudowires
3. Logical ports
Configure serial/
voice/ds1-opt port
Configure ds0 
cross-connect
TDM Port
DS1 Port
Ethernet
Configure 
ethernet port
Set Ethernet 
port parameters
Configure 
ds1 port
Configure 
pw-tdm 
cross-connect
Assign 
ingress and 
egress ports
Assign 
classifier 
profile
Configure flow 
1
Define vlan 
editing 
actions
Flow 1a
SVI
Flow 1b
Add and 
configure a 
pseudowire
Assign 
ingress and 
egress ports
Configure flow 
2
Define vlan 
editing 
actions
Assign 
classifier 
profile
 Bridge
BP
BP
Flow 1
Define bridge ports
Flow 2
classifier 
profile
Bind
Define SVI
PW
queue mapping 
profile
analog 
signaling profile
classifier 
profile
 
Serial/Voice/DS1-opt Service over MEF-8 PW  
TDM Service over MEF-8 PW Provisioning 
Sequence 
Step 
Commands 
Comments 
1. 
Defin
e 
profil
Defining 
Classifier Profiles 
 
flows flow classifier-
profile 
Create classifier profile “match-all” (see 
Chapter 8) 
Queue Mapping 
Profiles 
qos queue-mapping-
profile 
Configure queue-mapping profiles (to be 
assigned to Ethernet ports) (see Chapter 8) 
Analog Signaling 
Profiles 
port analog-
signaling-profile 
Define analog signaling profile for voice 
ports (see Chapter 5) 
Megaplex-1 
4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
2. Configure physical  
ports 
TDM Ports  
port serial 
port voice 
port ds1-opt 
Configure physical parameters of TDM 
ports (see Chapter 5)  
Ethernet Ports 
 
port ethernet 
Configure physical parameters of Ethernet 
ports  
Bind queue mapping profile – optional (see 
Chapter 5) 
3. Configure logical ports 
DS1 Ports 
 
port ds1 
Configure physical parameters of DS1 ports 
(see Chapter 5)  
Bridge ports 
bridge port 
Configure bridge ports 
Configure VLAN membership – optional 
(see Chapter 8) 
Service Virtual 
Interface 
port svi 
Define an SVI port (see Chapter 5)  
4. Define 
PW peer 
Peer 
peer 
Configure remote pseudowire peer 
Assign mac-address (see Chapter 8) 
 
5. Define 
pseudowire 
Pseudowires 
pwe 
Add and configure pseudowires 
Bind pseudowire to the peer (see Chapter 
8) 
 
6. Configure 
cross-connections 
DS0 Cross-
connect  
cross-connect ds0 
 
 
 
Configure cross-connect between 
serial/voice/ds1-opt ports and timeslots of 
DS1 port (see Chapter 8) 
PW-TDM 
Cross-connect  
cross-connect pw-tdm  
Configure cross-connect between timeslots 
of DS1 port and PW (see Chapter 8) 
7. 
Configure 
 flows 
Flows 
flows flow 
Define flow 1 and flow 2 
Assign classifier profile  
Define VLAN editing actions (see Chapter 8) 
 
 