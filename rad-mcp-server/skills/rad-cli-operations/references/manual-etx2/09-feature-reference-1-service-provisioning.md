# Feature Reference – 1 Service Provisioning

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 503–530.*


## 1.1 Service Entities  *(p.503)*

ETX-2i Devices 
1. Service Provisioning 
1 Service Provisioning 
This chapter shows the data flow and configuration steps for services.  
The diagrams and tables in Sections 4.2 to 4.6 illustrate typical ETX-2i services. 
Services can be discovered using the RADview service discovery function (refer to Preconfiguration for 
Service Discovery). 
1.1 Service Entities 
This section describes the managed elements that need to be configured during service provisioning. 
Service provisioning elements are as follows: 
• 
Profiles 
• 
Scheduling and shaping entities 
• 
Physical ports – E1/E3/T1/T3 (depending on product), Ethernet, SHDSL, VDSL 
• 
Logical ports – LAG, logical MAC, PCS (for ETX-2i with an SHDSL or VDSL2 module), DS1, GFP, and 
SVI 
• 
Forwarding entities – flow, bridge, router 
• 
Pseudowires (PW) 
Profiles 
Most packet processing features are defined by creating and applying various profiles. Profiles comprise 
sets of attributes related to a specific service entity. Profiles must be defined before other managed 
objects. 
Note 
Refer to the Technical Specifications section in the Introduction chapter for 
information on the number of configurable profiles per profile type.  
 
ETX-2i Devices 
1. Service Provisioning 
Applied to 
Profile Type 
Description 
Described in 
Ethernet port 
Fat pipe (aka 
elephant flow) 
detection 
Rate limits high BW sessions.  
For ETX-2i-10G half 19-inch, ETX-2i-10G-B full 
and half 19-inch models, ETX-2i-10G-B/8SFPP 
ports 1 to 4, ETX-2i-10G-E and ETX-2i-
100G/4QSFP user ports. 
Traffic 
Processing 
chapter 
Ethernet port, flow 
Policer, Policer 
aggregate 
Defines CIR, CBS, EIR, and EBS parameters 
Traffic 
Processing 
chapter 
Ethernet/logical MAC 
port, PCS flow 
L2CP  
Defines actions for L2CP processing (drop, peer, 
tunnel, and tunnel with MAC swap) 
Traffic 
Processing 
chapter 
Ethernet/logical MAC 
port/PCS port 
Queue group 
Defines the group of queue blocks in a two-stage 
hierarchy 
Also sets the queue block profiles used and the 
queue block Shaper profile 
Traffic 
Processing 
chapter 
ETP/bridge 
flow/MultiCoS flow (10.3 
Policer) 
CoS mapping  
Defines method and values for mapping packet 
attributes (P-bit, DSCP, IP precedence) to internal 
CoS values  
Traffic 
Processing 
chapter 
Flow 
Classifier 
Defines criteria for flow classification 
Traffic 
Processing 
chapter 
Flow 
Color mapping 
Defines method and values for mapping packet 
attributes (P-bit, DSCP, IP precedence) to internal 
color values 
Traffic 
Processing 
chapter 
Flow 
Marking 
Defines method of mapping internal CoS or 
packet attributes (p-bit, DSCP, IP Precedence), 
and packet color values into (S-Tag) P-bit and DEI 
Traffic 
Processing 
chapter 
Flow 
Envelope 
Policer 
Defines Policer attributes per rank, per MEF 10.3 
Traffic 
Processing 
chapter 
Flow 
Queue 
mapping 
Defines method and values for mapping packet 
attributes (P-bit, DSCP, IP precedence, CoS) to 
internal priority queues 
Traffic 
Processing 
chapter 
Queue 
WRED 
Defines yellow packet thresholds and drop 
probabilities 
Traffic 
Processing 
chapter 
ETX-2i Devices 
1. Service Provisioning 
Applied to 
Profile Type 
Description 
Described in 
Queue block within 
queue group 
Queue block 
Defines queue and queue parameters. This 
includes defining all the queues forming the 
queue block and defining per queue its 
parameters, such as scheduling mode (strict, 
WFQ, BE), queue depth, and queue WRED 
profile. 
Traffic 
Processing 
chapter 
Queue, queue block 
Shaper 
Controls the egress bandwidth utilization by 
defining CIR and CBS 
Traffic 
Processing 
chapter 
Scheduling and Shaping Entities 
ETX-2i schedules traffic using the following hierarchical scheduling entities: 
Queue 
A lowest-level scheduling element. Its priority can be strict, weight fair, or best effort. 
Queues have Shaper and WRED profiles assigned to them, as well as a configurable 
depth. 
Queue block 
Also referred to as scheduling element (SE) – a mid-level scheduling element that 
consists of several queues. Queue blocks are created by associating queues with queue 
block profiles. ETX-2i has two levels of queue blocks. Queue blocks may have Shaper 
profiles assigned to them. 
Queue Group 
A top-level scheduling element that consists of several queue blocks. Queue groups are 
created by associating queue group profiles to ports. 
ETX-2i supports the Single Token Bucket Shaper (CIR) as shaping tool. Congestion avoidance proceeds 
per color: 
Green 
Tail drop 
Yellow 
WRED profile 
Physical Ports 
Ethernet ports serve as ingress (UNI) and egress (NNI) ports for Ethernet flows. The following packet 
processing attributes are assigned to them: 
• 
Tag EtherType for identifying VLAN-tagged frames at ingress and setting EtherType value for 
VLAN editing (stack, swap) at egress 
ETX-2i Devices 
1. Service Provisioning 
• 
Fat pipe detection profile for detecting exceptionally high BW sessions (micro flows) (ETX-2i-10G 
half 19-inch and ETX-2i-10G-B full and half 19-inch models, ETX-2i-10G-B/8SFPP ports 1 to 4, as 
well as ETX-2i-100G/4QSFP user ports). 
• 
L2CP profile for defining L2CP frame handling (discard, peer, tunnel, or tunnel with MAC swap) 
• 
Queue group profile for associating a port with a queue group 
• 
Policer profile for broadcast/multicast traffic (BUM filter) 
Logical Ports 
Logical ports maintained by ETX-2i serve as internal aggregation or forwarding points for Ethernet flows. 
The following logical ports exist: 
GFP 
Provides a logical link to built-in E1/T1/T3 ports, smart SFP E1/T1/T3/SDH/SONET ports, 
or modular E1/T1/T3 ports. Required to run EoPDH.  
Logical MAC 
Provides a logical port to access smart SFP ports (via GFP ports) 
Link Aggregation 
Group (LAG) 
Provides link protection. LAGs have the same attributes as the physical ports that serve 
as their members. 
PCS 
Provides a logical port to access SHDSL or VDSL2 ports 
Service Virtual 
Interface (SVI) 
Binds flows to router interfaces or GRE tunnel interfaces 
VCG 
Groups multiple modular E1/T1/T3 ports 
Forwarding Entities 
Several internal entities carry traffic and make forwarding and switching decisions. These are: 
• 
Flows – Traffic-forwarding interconnection elements 
• 
Bridge 
• 
Router 
Flows 
Flows are entities that interconnect two physical or logical ports and are the main traffic-carrying 
elements in ETX-2i architecture. Flow processing is performed as follows: 
ETX-2i Devices 
1. Service Provisioning 
• 
Ingress traffic is mapped in flows using classification match criteria defined via a classification 
profile. 
• 
L2CP frames are handled per flow according to L2CP profile settings. 
• 
User priority (P-bit, IP Precedence, DSCP) is mapped into internal queue according to a queue 
mapping profile or assignment per flow. 
• 
Packet attributes may map packets to the ingress color, which together with the color-aware 
Policer (if applied), sets the egress packet color. Packet color may be used in the marking and 
congestion avoidance process. 
Alternately, packet attributes (L2-L4) can be mapped to an internal CoS, which maps to queues 
(1:1). This scheme is supported by certain configuration scenarios. 
• 
VLANs can be edited per flow by stacking (pushing), removing (popping), or swapping (marking) 
tags on single or double-tagged packets. P-bit and DEI values are either copied or set according 
to a marking profile (per packet attributes or internal CoS).  
• 
A single Policer can be applied to a flow, or a Policer aggregate can be assigned to a group of 
flows. Envelope Policer is also supported and can be assigned to a flow. 
• 
A flow is mapped to a queue block or queue group associated with the egress port.  
Bridge 
The bridge is a forwarding entity used by ETX-2i for delivering E-LAN and E-Tree services in multipoint-
to-multipoint topology and G.8032 ring protection. The bridge uses SVIs to connect logical and physical 
ports.  
The bridge is defined by bridge ports and a VLAN membership table that specifies which bridge ports are 
members in a certain broadcast domain (VLAN). The bridge supports up to two VLAN editing actions, on 
ingress and/or egress. The editing is performed at the flow level. 
Router 
The embedded router (ETX-2i and ETX-2i-B) provides IPv4 and IPv6 routing. Each router interface is 
assigned IP address(es) and should be bound to an SVI. 
The router uses service virtual interfaces (SVIs) to connect to logical and physical ports. The connection 
is always established by directing flows from a port to an SVI, and then binding the SVI to a router 
interface. 
Device management, as well as other L3 ‘modules’, such as 1588 (8265.1), TDM PW (UDP/IP), and 
TWAMP, use the ETX-2i routing scheme. 

## 1.2 Resource Allocation Considerations  *(p.508)*

ETX-2i Devices 
1. Service Provisioning 
1.2 Resource Allocation Considerations 
Applicability and Scaling 
This feature is applicable to ETX-2i-100G/4QSFP. 
Functional Description 
In terms of resource allocation, ETX-2i-100G/4QSFP ports are divided into two main groups, as follows: 
• 
Group 1: 100G ports 3/1 and 3/2 
• 
Group 2: All other ports (100G ports 3/3 and 3/4 and 10G ports 1/1 to 1/8 and 2/1 to 2/8)  
Resource allocation and functional design are reflected as follows: 
• 
In terms of bandwidth, each group can ingress or Egress half of the declared total Ingress or 
Egress. For a classic aggregation/NID application, it is recommended to place all UNI ports in 
Group 2 and all NNI ports in Group 1. In case of MASH topology, the network design takes into 
consideration the total expected ingress and egress traffic of each group. 
• 
When defining LAG protection, the two protected ports/paths should be from the same group. 
100G LAG protection mode can be set between the ports in Group 1 and 10G LAG protection 
mode between ports in Group 2. 
• 
Ingress/egress traffic can pass between ports within the same group or between the two 
groups. Ingress/egress traffic on a specific port is logged under the group to which the port 
belongs. For ETX-2i-100G/4QSFP, traffic on ports 3/1 and 3/2 is logged under Group 1, and 
traffic on any other port is logged under Group 2. 
• 
Maximum 1860 flows per device; 930 per group 

## 1.3 E-LAN Service  *(p.509)*

ETX-2i Devices 
1. Service Provisioning 
1.3 E-LAN Service 
Ethernet to Bridge 
The rectangles in the figure below illustrate the E-LAN traffic data flow for user traffic from an Ethernet 
port to a bridge port. The rounded rectangles indicate the features that need to be configured, 
numbered according to the order of configuration. The table shows the configuration steps 
corresponding to the numbers. 
Sequence 
Step 
Commands 
Comments 
1 
Configuring the Bridge 
mode e-lan  
port 
Refer to Traffic Processing chapter. 
2 
Configuring a Classifier 
Profile 
classifier-profile 
match 
The classifier profile defines the criteria 
for the flow.  
Refer to Traffic Processing chapter. 
3 
Marking Profiles 
marking-profile 
mark 
Necessary only if a profile is needed for 
non-default mapping of p-bit, IP 
precedence, DSCP, or CoS 
classifications to egress priority tags. 
Refer to Traffic Processing chapter. 
4 
CoS Mapping Profiles 
cos-map-profile 
map 
Necessary only if a profile is needed for 
non-default mapping of user priorities 
to CoS. 
Refer to Traffic Processing chapter. 
5 
Configuring a Policer Profile 
policer-profile 
bandwidth 
color-aware 
compensation 
coupling-flag 
traffic-type 
Refer to Traffic Processing chapter. 
6 
Ethernet Ports 
auto-negotiation 
classifier 
efm 
egress-mtu 
fec 
• Necessary only if you need to define 
non-default configuration for the 
egress port 
• l2pt-network is only configurable 
on user ports. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
functional-mode 
l2cp 
l2pt-network 
lldp 
policer 
max-capability 
max-ql 
name 
speed-duplex 
queue-group 
rate-measure 
tag-ethernet-type 
shutdown 
silent-start 
tx-ssm 
• classifier, max-capability, max-ql, 
silent-start, and speed-duplex are 
not relevant for ETX-2i-100G. 
• auto-negotiation is configurable on 
1G interfaces only. 
• fec is configurable on  
ETX-2i-100G/4QSFP 100GbE ports 
only. 
Refer to Cards and Ports chapter. 
7 
Configuring Flows 
classifier 
cos-mapping 
ingress-port 
egress-port 
l2cp  
mark 
marking-profile 
policer 
reverse-direction 
vlan-tag 
shutdown 
You must define the flow for the user 
traffic from the Ethernet port to the 
bridge port. 
Refer to Traffic Processing chapter. 
Bridge to Ethernet 
In the figure below, the rectangles illustrate the E-LAN traffic data flow for user traffic from a bridge port 
to an Ethernet port. The rounded rectangles indicate the features that need to be configured, numbered 
according to the order of configuration. The table below shows the configuration steps corresponding to 
the numbers. 
ETX-2i Devices 
1. Service Provisioning 
Classification
Flow
Queueing 
level 0
Shaping
8) Ethernet ports
5) Shaping
7) WRED
6) Queue blocks
3) Marking
4) CoS mapping
9) Flows
2) Classification
Ingress bridge 
port
Egress 
Ethernet port
Queueing 
level 1
6) Queue blocks
1) Bridge ports
 
 
Sequence 
Step 
Commands 
Comments 
1 
Configuring the Bridge 
port 
mode e-lan 
Refer to Traffic Processing chapter. 
2 
Configuring a Classifier 
Profile 
classifier-profile 
match 
The classifier profile defines the criteria 
for the flow. 
Refer to Traffic Processing chapter. 
3 
Marking Profiles 
marking-profile 
mark 
Necessary only if a profile is needed for 
non-default mapping of p-bit, IP 
precedence, DSCP, or CoS classifications 
to egress priority tags. 
Refer to Traffic Processing chapter. 
4 
CoS Mapping Profiles 
cos-map-profile 
map 
Necessary only if a profile is needed for 
non-default mapping of user priorities 
to CoS. 
Refer to Traffic Processing chapter. 
5 
Configuring Shaper Profiles 
shaper-profile 
bandwidth 
compensation 
Necessary only if you need to define 
non-default bandwidth limits or 
overhead compensation for the 
outgoing traffic of the flow (via 
attaching Shaper profile to queue group 
profile attached to egress port). 
Refer to Traffic Processing chapter. 
6 
Configuring Queue Block 
Profile Parameters 
queue-block-profile 
queue 
scheduling 
depth 
Necessary only if you need to define 
non-default queue configuration for the 
flow, or the egress port. 
Refer to Traffic Processing chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
7 
WRED Profiles 
wred-profile 
color 
Necessary only if you need to define 
non-default WRED configuration for the 
queue blocks. 
Refer to Traffic Processing chapter. 
8 
Ethernet Ports 
auto-negotiation 
classifier 
efm 
egress-mtu 
fat-pipe-detection 
fec 
functional-mode 
l2cp 
l2pt-network 
lldp 
policer 
max-capability 
max-ql 
name 
speed-duplex 
queue-group 
rate-measure 
tag-ethernet-type 
shutdown 
silent-start 
tx-ssm 
• Necessary only if you need to define 
non-default configuration for the 
egress port 
• auto-negotiation is configurable on 
1G interfaces only. 
• Fat pipe is relevant for ETX-2i-10G 
half 19-inch, ETX-2i-10G-B (full and 
half 19-inch), ETX-2i-10G-B/8SFPP 
ports 1 to 4, as well as for  
ETX-2i-100G/4QSFP user ports. 
• l2pt-network is only configurable on 
user ports. 
• classifier, max-capability, max-ql, 
silent-start, and speed-duplex are 
not relevant for ETX-2i-100G. 
• fec is configurable on 
 
ETX-2i-100G/4QSFP 100GbE ports 
only. 
Refer to Cards and Ports chapter. 

## 1.4 E-Line Service  *(p.513)*

ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
9 
Configuring Flows 
classifier 
cos-mapping 
ingress-port 
egress-port 
l2cp 
mark 
marking-profile 
policer 
reverse-direction 
vlan-tag 
shutdown 
You must define the flow for the user 
traffic from the bridge port to the 
Ethernet port. 
Refer to Traffic Processing chapter. 
1.4 E-Line Service 
User to Network 
In the figure below, the rectangles illustrate the data flow for Ethernet user traffic from a user port to a 
network port. The rounded rectangles indicate the features that need to be configured, numbered 
according to the order of configuration. The table below shows the configuration steps corresponding to 
the numbers. 
Policing
Classification
Flow
Queueing 
level 0
Shaping
8) Queue groups
9) Ethernet ports
5) Shaping
7) WRED
6) Queue blocks
4) Policing
2) Marking
3) Queue mapping
10) Flows
1) Classification
9) Ethernet ports
Ingress UNI
Egress NNI
Queueing 
level 1
6) Queue blocks
 
 
Sequence 
Step 
Commands 
Comments 
1 
Configuring a Classifier 
Profile 
classifier-profile 
match 
The classifier profile defines the criteria 
for the user-to-network flow.  
Refer to Traffic Processing chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
2 
Marking Profiles 
marking-profile 
mark 
Necessary only if a profile is needed for 
non-default mapping of p-bit, IP 
precedence, DSCP, or CoS classifications 
to egress priority tags for the 
user-to-network flow. 
Refer to Traffic Processing chapter. 
3 
Queue Mapping Profiles 
queue-map-profile 
map 
Necessary only if a profile is needed for 
non-default mapping of user priorities 
to queues for the user-to-network flow. 
Refer to Traffic Processing chapter. 
4 
Configuring Policer Profiles 
policer-profile 
bandwidth 
compensation 
color-aware 
coupling-flag 
traffic-type 
Necessary only if you need to define 
non-default bandwidth limits or 
overhead compensation for the 
incoming traffic of the user-to-network 
flow. 
Refer to Traffic Processing chapter. 
5 
Configuring Shaper Profiles 
shaper-profile 
bandwidth 
compensation 
Necessary only if you need to define 
non-default bandwidth limits or 
overhead compensation for the 
outgoing traffic of the user-to-network 
flow (via attaching Shaper profile to 
queue group profile attached to egress 
port). 
Refer to Traffic Processing chapter. 
6 
Configuring Queue Block 
Profile Parameters 
queue-block-profile 
queue 
scheduling 
depth 
Necessary only if you need to define 
non-default queue configuration for the 
user-to-network flow, or the egress 
port. 
Refer to Traffic Processing chapter. 
7 
WRED Profiles 
wred-profile 
color 
Necessary only if you need to define 
non-default WRED configuration for the 
queue blocks. 
Refer to Traffic Processing chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
8 
Queue Group Profiles 
queue-group-profile 
queue-block 
name 
profile 
shaper 
Necessary only if you need to define 
non-default queue group configuration 
for the egress port. 
Refer to Traffic Processing chapter. 
9 
Ethernet Ports 
auto-negotiation 
classifier 
efm 
egress-mtu 
fat-pipe 
fec 
functional-mode 
l2cp 
l2pt-network 
lldp 
policer 
max-capability 
max-ql 
name 
speed-duplex 
queue-group 
rate-measure 
tag-ethernet-type 
shutdown 
silent-start 
tx-ssm 
Necessary only if you need to define 
non-default configuration for the egress 
port 
l2pt-network is only configurable on 
user ports. 
classifier, max-capability, max-ql, 
silent-start, and speed-duplex are not 
relevant for ETX-2i-100G. 
auto-negotiation is configurable on 1G 
interfaces only. 
Fat pipe is relevant for ETX-2i-10G half 
19-inch, ETX-2i-10G-B (full and half 19-
inch), ETX-2i-10G-B/8SFPP ports 1 to 4, 
as well as for ETX-2i-100G/4QSFP user 
ports. 
fec is configurable on  
ETX-2i-100G/4QSFP 100GbE ports only. 
Refer to Cards and Ports chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
10 
Configuring Flows 
classifier 
cos-mapping 
ingress-port 
egress-port 
l2cp 
mark 
marking-profile 
policer 
reverse-direction 
vlan-tag 
shutdown 
You must define the flow for the user 
traffic from the user port to the 
network port. 
Refer to Traffic Processing chapter. 
Network to User 
In the figure below, the rectangles illustrate the E-Line traffic data flow for Ethernet user traffic from a 
network port to a user port. The rounded rectangles indicate the features that need to be configured, 
numbered according to the order of configuration. The table below shows the configuration steps 
corresponding to the numbers. 
 
Policing
Classification
Flow
Shaping
8) Queue groups
9) Ethernet ports
5) Shaping
7) WRED
6) Queue blocks
4) Policing
2) Marking
3) Queue mapping
10) Flows
1) Classification
9) Ethernet ports
Ingress NNI
Egress UNI
Queueing 
level 0
  
 
Sequence 
Step 
Commands 
Comments 
1 
Configuring a Classifier 
Profile 
classifier-profile 
match 
The classifier profile defines the criteria 
for the network-to-user flow. 
Refer to Traffic Processing chapter.  
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
2 
Marking Profiles 
marking-profile 
mark 
Necessary only if a profile is needed for 
non-default mapping of p-bit, IP 
precedence, DSCP, or CoS 
classifications to egress priority tags for 
the network-to-user flow. 
Refer to Traffic Processing chapter. 
3 
Queue Mapping Profiles 
queue-map-profile 
map 
Necessary only if a profile is needed for 
non-default mapping of user priorities 
to queues for the network-to-user flow. 
Refer to Traffic Processing chapter. 
4 
Configuring Policer Profiles 
policer-profile 
bandwidth 
compensation 
color-aware 
coupling-flag 
traffic-type 
Necessary only if you need to define 
non-default bandwidth limits or 
overhead compensation for the 
incoming traffic of the network-to-user 
flow. 
Refer to Traffic Processing chapter. 
5 
Configuring Shaper Profiles 
shaper-profile 
bandwidth 
compensation 
Necessary only if you need to define 
non-default bandwidth limits or 
overhead compensation for the 
outgoing traffic of the network-to-user 
flow (via attaching Shaper profile to 
queue group profile attached to egress 
port). 
Refer to Traffic Processing chapter.  
6 
Configuring Queue Block 
Profile Parameters 
queue-block-profile 
queue 
scheduling 
depth 
Necessary only if you need to define 
non-default queue configuration for the 
network-to-user flow. 
Refer to Traffic Processing chapter. 
7 
WRED Profiles 
wred-profile 
color 
Necessary only if you need to define 
non-default WRED configuration for the 
queue blocks. 
Refer to Traffic Processing chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
8 
Queue Group Profiles 
queue-group-profile 
queue-block 
name 
profile 
shaper 
Necessary only if you need to define 
non-default queue group configuration 
for the egress port. 
Refer to Traffic Processing chapter. 
9 
Ethernet Ports 
auto-negotiation 
classifier 
efm 
egress-mtu 
fec 
functional-mode 
l2cp 
l2pt-network 
lldp 
policer 
max-capability 
max-ql 
name 
speed-duplex 
queue-group 
rate-measure 
tag-ethernet-type 
shutdown 
silent-start 
tx-ssm 
Necessary only if you need to define 
non-default configuration for the 
egress port 
l2pt-network is only configurable on 
user ports. 
classifier, max-capability, max-ql, 
silent-start, and speed-duplex are not 
relevant for ETX-2i-100G. 
auto-negotiation is configurable on 1G 
interfaces only. 
fec is configurable on  
ETX-2i-100G/4QSFP 100GbE ports only. 
Refer to Cards and Ports chapter. 

## 1.5 E-Tree Service  *(p.519)*

ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
10 
Configuring Flows 
classifier 
cos-mapping 
ingress-port 
egress-port 
mark 
marking-profile 
policer 
reverse-direction 
vlan-tag 
shutdown 
You must define the flow for the user 
traffic from the network port to the 
user port. 
Refer to Traffic Processing chapter. 
1.5 E-Tree Service 
The E-Tree service is the same as E-LAN service (above), except for the following changes to Step 1 
(Configuring the Bridge), summarized in the following table: 
• 
Define the bridge as VLAN-unaware (no vlan-aware) 
• 
Define a bridge port as root 
• 
Configure bridge in e-tree mode (mode e-tree instead of mode e-lan). 
• 
Under bridge VLAN, configure bridge port as root, other bridge ports as leaves, and VLAN to 
work in E-Tree mode. 
Sequence 
Step 
Commands 
Comments 
1 
Configuring the Bridge 
mode e-tree  
no vlan-aware 
root  
port 
vlan mode e-tree 
vlan root 
vlan no root 
Refer to Traffic Processing chapter. 

## 1.6 Smart SFP Service  *(p.520)*

ETX-2i Devices 
1. Service Provisioning 
1.6 Smart SFP Service 
Note 
ETX-2i-100G does not support smart SFP service. 
Network to User 
The following figure illustrates the TDM user traffic data flow from a network port provisioned as a TDM 
port via a smart SFP, to an Ethernet user port. The table below shows the configuration steps 
corresponding to the figure callouts. 
 
 
 
Sequence 
Step 
Commands 
Comments 
1 
Smart SFPs  
smart-sfp 
type 
shutdown 
You must provision the smart SFP for 
the network port.  
Refer to Cards and Ports chapter. 
2 
E1 Ports  
e1 
name 
line-code 
line-type 
rx-sensitivity 
tx-clock-source 
shutdown 
Necessary only if non-default 
configuration is needed for the TDM 
port 
Note: The specific step is according 
to the TDM port type. 
Refer to Cards and Ports chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
T1 Ports 
t1 
name 
line-code 
line-length 
line-type 
rx-sensitivity 
tx-clock-source 
shutdown 
E3 Ports 
e3 
name 
tx-clock-source 
shutdown 
T3 Ports 
t3 
name 
line-length 
line-type 
shutdown 
SDH/SONET Ports 
sdh-sonet 
name  
frame-type 
threshold 
tim-response 
tx-clock-source 
shutdown 
3 
GFP Ports 
gfp 
bind 
fcs-payload 
name 
You must configure a GFP port and 
bind the TDM port to it. 
Refer to Cards and Ports chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
4 
Logical MAC Ports 
logical-mac 
name 
bind 
egress-mtu 
queue-group 
tag-ethernet-type 
shutdown 
You must configure a logical MAC 
port and bind the GFP port to it. The 
logical MAC port is used as the 
ingress port of the flow. 
Refer to Cards and Ports chapter. 
5 
Configuring a Classifier 
Profile 
classifier-profile 
match 
The classifier profile defines the 
criteria for the network-to-user flow.  
Refer to Traffic Processing chapter. 
6 
Marking Profiles 
marking-profile 
mark 
Necessary only if a profile is needed 
for non-default mapping of p-bit, IP 
precedence, DSCP, or CoS 
classifications to egress priority tags 
for the network-to-user flow. 
Refer to Traffic Processing chapter.  
7 
Queue Mapping Profiles 
queue-map-profile 
map 
Necessary only if a profile is needed 
for non-default mapping of user 
priorities to queues for the 
network-to-user flow. 
Refer to Traffic Processing chapter. 
8 
Configuring Policer 
Profiles 
policer-profile 
bandwidth 
compensation 
Necessary only if you need to define 
non-default bandwidth limits or 
overhead compensation for the 
incoming traffic of the 
network-to-user flow. 
Refer to Traffic Processing chapter. 
9 
Configuring Queue Block 
Profile Parameters 
queue-block-profile 
queue 
scheduling 
depth 
Necessary only if you need to define 
non-default queue configuration for 
the network-to-user flow. 
Refer to Traffic Processing chapter. 
10 
WRED Profiles 
wred-profile 
color 
Necessary only if you need to define 
non-default WRED configuration for 
the queue blocks. 
Refer to Traffic Processing chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
11 
Configuring Flows 
classifier 
ingress-port 
egress-port 
policer 
mark 
vlan-tag 
shutdown 
You must define the flow for the user 
traffic from the network port (logical 
MAC port) to the user port. 
Refer to Traffic Processing chapter. 
12 
Configuring Shaper 
Profiles  
shaper-profile 
bandwidth 
compensation 
Necessary only if you need to define 
non-default bandwidth limits or 
overhead compensation for the 
outgoing traffic of the 
network-to-user flow (via attaching 
Shaper profile to queue group profile 
attached to egress port). 
Refer to Traffic Processing chapter. 
13 
Queue Group Profiles 
queue-group-profile 
queue-block 
name 
profile 
shaper 
Necessary only if you need to define 
non-default queue group 
configuration for the egress port. 
Refer to Traffic Processing chapter. 
14 
Ethernet Ports 
auto-negotiation 
classification-key 
classifier 
dhcp-trust 
efm 
egress-mtu 
fat-pipe-detection  
fec 
max-capability 
max-ql 
name 
speed-duplex 
queue-group 
rate-measure 
release-fat-pipe 
Necessary only if you need to define 
non-default configuration for the 
egress port 
auto-negotiation is configurable on 
1G interfaces only. 
fat-pipe-detection and release-fat-
pipe are configurable on 
ETX-2i-10G half 19-inch and  
ETX-2i-10G-B full and half 19-inch 
models, ETX-2i-10G-B/8SFPP ports 1 
to 4, as well as  
ETX-2i-100G/4QSFP user ports. 
fec is configurable on  
ETX-2i-100G/4QSFP 100GbE ports 
only. 
Refer to Cards and Ports chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
tag-ethernet-type 
shutdown 
silent-start 
tx-ssm 
User to Network 
The following figure illustrates the TDM user traffic data flow from a user port provisioned as a TDM 
port via a smart SFP, to an Ethernet network port. The table below shows the configuration steps 
corresponding to the figure callouts. 
 
 
 
Sequence 
Step 
Commands 
Comments 
1 
Smart SFPs  
smart-sfp 
type 
shutdown 
You must provision the smart SFP for 
the user port.  
Refer to Cards and Ports chapter. 
2 
E1 Ports  
e1 
name 
line-code 
line-type 
rx-sensitivity 
tx-clock-source 
shutdown 
Necessary only if non-default 
configuration is needed for the TDM 
port 
Note: The specific step is according 
to the TDM port type. 
Refer to Cards and Ports chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
T1 Ports 
t1 
name 
line-code 
line-length 
line-type 
rx-sensitivity 
tx-clock-source 
shutdown 
E3 Ports 
e3 
name 
tx-clock-source 
shutdown 
T3 Ports 
t3 
name 
line-length 
line-type 
shutdown 
SDH/SONET Ports 
sdh-sonet 
name  
frame-type 
threshold 
tim-response 
tx-clock-source 
shutdown 
3 
GFP Ports 
gfp 
bind 
fcs-payload 
name 
You must configure a GFP port and 
bind the TDM port to it. 
Refer to Cards and Ports chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
4 
Logical MAC Ports 
logical-mac 
name 
bind 
egress-mtu 
queue-group 
tag-ethernet-type 
shutdown 
You must configure a logical MAC 
port and bind the GFP port to it. The 
logical MAC port is used as the 
ingress port of the flow. 
Refer to Cards and Ports chapter. 
5 
Configuring a Classifier 
Profile 
classifier-profile 
match 
The classifier profile defines the 
criteria for the user-to-network flow. 
Refer to Traffic Processing chapter.  
6 
Marking Profiles 
marking-profile 
mark 
Necessary only if a profile is needed 
for non-default mapping of p-bit, IP 
precedence, DSCP, or CoS 
classifications to egress priority tags 
for the user-to-network flow. 
Refer to Traffic Processing chapter. 
7 
Queue Mapping Profiles 
queue-map-profile 
map 
Necessary only if a profile is needed 
for non-default mapping of user 
priorities to queues for the 
user-to-network flow. 
Refer to Traffic Processing chapter. 
8 
Configuring Policer 
Profiles 
policer-profile 
bandwidth 
compensation 
Necessary only if you need to define 
non-default bandwidth limits or 
overhead compensation for the 
incoming traffic of the 
user-to-network flow. 
Refer to Traffic Processing chapter. 
9 
Configuring Queue Block 
Profile Parameters 
queue-block-profile 
queue 
scheduling 
depth 
Necessary only if you need to define 
non-default queue configuration for 
the user-to-network flow, or the 
egress port. 
Refer to Traffic Processing chapter. 
10 
WRED Profiles 
wred-profile 
color 
Necessary only if you need to define 
non-default WRED configuration for 
the queue blocks. 
Refer to Traffic Processing chapter. 
ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
11 
Configuring Flows 
classifier 
ingress-port 
egress-port 
policer 
mark 
vlan-tag 
shutdown 
You must define the flow for the user 
traffic from the user port to the 
network port. 
Refer to Traffic Processing chapter. 
12 
Configuring Shaper 
Profiles  
shaper-profile 
bandwidth 
compensation 
Necessary only if you need to define 
non-default bandwidth limits or 
overhead compensation for the 
outgoing traffic of the 
user-to-network flow (via attaching 
Shaper profile to queue group profile 
attached to egress port). 
Refer to Traffic Processing chapter.  
13 
Queue Group Profiles 
queue-group-profile 
queue-block 
name 
profile 
shaper 
Necessary only if you need to define 
non-default queue group 
configuration for the egress port. 
Refer to Traffic Processing chapter. 
14 
Ethernet Ports 
auto-negotiation 
classification-key 
classifier 
dhcp-trust 
efm 
egress-mtu 
fat-pipe-detection  
max-capability 
max-ql 
name 
speed-duplex 
queue-group 
rate-measure 
release-fat-pipe 
tag-ethernet-type 
Necessary only if you need to define 
non-default configuration for the 
egress port 
auto-negotiation is configurable on 
1G interfaces only. 
fat-pipe-detection and release-fat-
pipe are configurable on 
ETX-2i-10G half 19-inch, ETX-2i-10G-
B full and half 19-inch models,  
ETX-2i-10G-B/8SFPP ports 1 to 4, as 
well as for ETX-2i-100G/4QSFP user 
ports. 
Refer to Cards and Ports chapter. 

## 1.7 Service Summary  *(p.528)*

ETX-2i Devices 
1. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
shutdown 
silent-start 
tx-ssm 
 
1.7 Service Summary 
You can display the associations between service names and their associated flows/MEPs. 
Viewing the entities associated with service names is useful for service administration, and to ensure 
correct discovery of service-related entities by network management systems. 
Functional Description 
If you have defined service names for flows, you can display the flows and corresponding MEPs 
associated with the service names. 
Viewing Service Summary 
You can view a list of defined service names, as well as information about the associated flows and 
MEPs.  
 To view the service information: 
• 
In the CLI, go to the config>service <service name> context, and enter one of the following: 
show status 
summary 
For specific service name, display summary information of 
associated flows/MEPs. 
show status details 
For specific service name, display details of associated flows/MEPs. 
ETX-2i Devices 
1. Service Provisioning 
Examples 
 To view summary information of flows/MEPs associated with service Service20: 
ETX-2i>config>service(Service20) # show status summary 
 
Flows 
----------------------------------------------------------------------------- 
Name                              Admin Oper  Egress Port   MEP 
----------------------------------------------------------------------------- 
Rx_v20                            Up    Down  ETH 0/3       3 
Tx_v20                            Up    Down  ETH 0/1       3 
 
OAM CFM MEPs 
----------------------------------------------------------------------------- 
 
MD       : 1                                               MA  : 2 
MD Level : 3 
MD Name  : MD1 
MA Name  : MA2 
 
MEPs 
----------------------------------------------------------------------------- 
ID    Status  Defects Service Pbit      RMEPs OK/Total 
----------------------------------------------------------------------------- 
3     up      No      ---               0/1 
 To view details of flows/MEPs associated with service Service20: 
ETX-2i>config>service(Service20)# show status Details 
 
Flows 
--------------------------------------------------------------- 
Name               : Rx_v20 
Admin              : Up 
Operational Status : Down 
Test Status        : Off 
Classifier Profile : v20 
Ingress Port       : Ethernet                           0/1 
Egress Port        : Ethernet                           0/3 
 
Name               : Tx_v20 
Admin              : Up 
Operational Status : Down 
Test Status        : Off 
Classifier Profile : v20 
Ingress Port       : Ethernet                           0/3 
Egress Port        : Ethernet                           0/1 
 
 
OAM CFM MEPs 
ETX-2i Devices 
1. Service Provisioning 
--------------------------------------------------------------- 
 
MD       : 1                                               MA  : 2 
MD Level : 3 
MD Name  : MD1 
MA Name  : MA2 
 
MEPs 
--------------------------------------------------------------- 
ID      : 3 
Status  : up 
Defects : No 
 
Remote MEP  Remote MEP 
--------------------------------------------------------------- 
4           Fail