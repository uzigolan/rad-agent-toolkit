# 4 Service Provisioning

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 197–234.*


## (chapter introduction)  *(p.197)*

This chapter presents information on the service elements and services provided by Megaplex-4. 
4.1 Service Elements 
This section details the managed elements that need to be configured during service provisioning. 
Service provisioning elements are as follows:  
• 
Profiles 
• 
Physical ports (User Ethernet, E1, T1, T3, Voice, Serial, DS1-opt (fiber optic links of VS-6/C37 
modules), SDH/SONET, Teleprotection and VS-6/BIN CMD CHANNEL, CMD-IN, CMD-OUT ports) 
• 
Logical ports (Logical MAC, VCG, GFP, SVI, Internal DS1, PW, LAG, LRE, Teleprotection CMD-IN-I 
and CMD-OUT-I) 
• 
Forwarding entities (flow, bridge, router). 
Profiles 
Most traffic processing features are defined by creating and applying various profiles. Profiles comprise 
sets of attributes related to a specific service entity. Profiles must be defined prior to other managed 
objects. 
Profile Types  
Applied to 
Profile Type 
Description 
Scale per 
Chassis 
Described 
in 
Flow 
Classifier 
Defines criteria for flow 
classification 
128 
Chapter 8 
4. Service Provisioning 
Applied to 
Profile Type 
Description 
Scale per 
Chassis 
Described 
in 
Flow 
Policer 
Define CIR, CBS, EIR and EBS 
parameters 
60 
Chapter 8 
Flow 
Marking 
Defines method of mapping 
CoS values into P-bit 
12 
Chapter 8 
Port, flow 
L2CP  
Defines actions for L2CP 
processing (drop, peer, 
tunnel) 
6 
 
Chapter 5 
Port (E1/T1) 
Signaling 
Specifies translation rules for 
signaling information 
5 
Chapter 5 
Port (Ethernet) 
Queue group 
Defines level-0 and -1 
scheduling elements and 
structures within queue group 
15  
Chapter 8 
Port (GFP, HDLC, 
E1, E1-I, AUG, T1, 
T1-I, OC3) 
VC 
Defines the handling of 
SDH/SONET (VC/VT/STS) 
traffic 
64 
Chapter 5 
Port (voice) 
Analog Signaling 
Specifies translation rules for 
signaling information 
8 
Chapter 5 
Queue, queue 
block 
Shaper 
Defines CIR, CBS, EIR and EBS  
parameter 
30 
Chapter 8 
Queue 
WRED 
Defines green and yellow 
packet thresholds and drop 
probabilities  
8 
Chapter 8 
Queue block 
within queue 
group 
Queue block 
Defines queue block 
parameters (queues, 
scheduling scheme, weights) 
128 
 
Chapter 8 
Scheduling and Shaping Entities 
Megaplex-4 schedules traffic using the following hierarchical scheduling entities:  
• 
Queue – a lowest-level scheduling element. Its priority can be strict or weight fair. Queues have 
shaper and WRED profiles assigned to them. 
• 
Queue block (also referred to as scheduling element, or SE) – a mid-level scheduling element 
that consists of several queues. Queue blocks are created by associating queues with queue 
4. Service Provisioning 
block profiles. There are two levels of queue blocks for CL GbE ports and one level for other 
Ethernet ports. Queue blocks have shaper profiles assigned to them. 
• 
Queue group – a top-level scheduling element that consists of several queue blocks. Queue 
groups are created by associating queue group profile to ports. 
Megaplex-4 provides the following shaping tools: 
• 
Dual leaky bucket shaper (CIR/EIR) 
• 
Single leaky bucket shaper (CIR). 
Congestion is avoided by using the WRED mechanism. 
Physical Ports 
Services provided by Megaplex-4100/4104 are based on its physical ports. These ports are located on 
the following modules (which can sometimes be interchangeable in providing specific services): 
• 
SDH/SONET –CL.2  
• 
GbE – CL.2, M-ETH 
• 
VS-16E1T1-EoP, VS-16E1T1-PW   
• 
T1 – VS-16E1T1-EoP, VS-16E1T1-PW  
• 
T3 – T3  
• 
Voice  – VC-4/VC-8/VC-4A/VC-8A/VC-16, VS Voice family    
• 
Serial  – VS family 
• 
DS1-Opt (VS fiber optic links) – VS-6/C37       
• 
CMD CHANNEL, CMD-IN, CMD-OUT – TP (Teleprotection), VS-6/BIN 
Logical Ports 
Logical ports maintained by Megaplex-4 do not have physical port attributes and serve different 
purposes, depending on the module and on the service provided by the module/system physical ports. 
The following logical ports exist: 
• 
Switched Virtual Interface (SVI) located on CL.2 modules and used for binding flows to bridge 
ports, router interfaces or Layer-2 TDM pseudowires. SVIs serve as intermediaries for bridges 
4. Service Provisioning 
and routers, which must comply with standards of their own (VLAN domains for bridge ports or 
IP address for router interfaces) and. They also serve as aggregation points for TDM PWs 
• 
VCG, GFP and HDLC ports located on CL.2 modules and used for efficient transport of Ethernet 
traffic over the SDH/SONET network. GFP and HDLC ports are mapped either directly to the 
physical layer or to VCG. In the latter case, the binding is done in two stages and the VCG is 
further bound to the physical layer.  
• 
VCG and GFP ports located on T3 modules and used for efficient transport of Ethernet traffic 
over the T1/T3 networks. GFP ports are mapped either directly to the physical layer or to VCG. 
In the latter case, the binding is done in two stages and the VCG is further bound to the physical 
layer.  
• 
VCG and GFP ports located on VS-16E1T1-EoP modules and used for efficient transport of 
Ethernet traffic over the E1/T1 networks. VCG ports are bound directly to GFP.   
• 
Logical MAC ports located on CL.2, T3, VS-16E1T1-EoP modules used to describe and map the 
Ethernet traffic passing over different media (E1/T1, T3, SDH/SONET, etc) and representing the 
MAC layer of the entity. Logical MAC ports are bound to a GFP or HDLC ports, which, in its turn, 
are bound to the physical layer.   
• 
Internal DS1 Ports located on VS modules and used to connect between pseudowires and serial 
ports. 
• 
CMD-IN-I and CMD-OUT-I ports located on Teleprotection module and used to manipulate the 
logical Rx/Tx information over the corresponding CMD CHANNEL 
• 
PW ports located on VS modules. 
Forwarding Entities 
Several internal entities carry traffic and make forwarding and switching decisions. These are: 
• 
Flows – the main traffic-carrying elements 
• 
Bridge – traffic-forwarding element for Layer-2 E-LAN services 
• 
Router – traffic-forwarding element for Layer-3 services. 
Flows 
Flows interconnect two physical or logical ports and are the main traffic-carrying elements in Megaplex-
4 architecture. You can use classifier profiles to specify the criteria for flows. The classification is per port 
and is applied to the ingress port of the flow. 
4. Service Provisioning 
Flows defined in Megaplex-4100/4104 can be unidirectional (between physical/logical ports) or 
bidirectional (between physical/logic ports and brigde ports of CL modules).  
Note 
Bridge ports in M-ETH modules are bound directly (without using flows).  
Flow processing is performed as follows:  
• 
Ingress traffic is mapped in flows using classification match criteria defined via classification 
profile. 
• 
L2CP frames are handled per flow according to L2CP profile settings. 
• 
User priority (P-bit, IP Precedence, DSCP) is mapped into internal Class of Service (CoS) 
according to assignment per flow. 
• 
User priority (P-bit, IP Precedence, DSCP) can be mapped into packet color (yellow or green) 
according to assignment per flow.  
• 
VLANs can be edited per flow by stacking (pushing), removing (popping), or swapping (marking) 
tags on single-, or double-tagged packets. P-bit values are either copied or set according to CoS 
marking profile.  
• 
A single policer can be applied to a flow, using policer profile.  
• 
A flow is mapped to a specific queue block within a queue group associated with egress port.  
Bridge 
The bridge is a forwarding entity used by Megaplex-4 for delivering E-LAN services in multipoint-to-
multipoint topology and G.8032 ring protection. With up to 11 bridge instances, Megaplex-4 provides up 
to 170 bridge ports, subdivided as follows: 
• 
80 ports on the CL.2 bridge 
• 
9 ports per M-ETH module bridge (8 external + 1 internal) – maximum 90 ports per chassis. 
The bridge uses bridge ports for connecting to logical and physical ports.  
The bridge is defined by a bridge number, bridge ports and a VLAN membership table that specifies 
which bridge ports are members in a certain broadcast domain (VLAN). The bridge supports one level of 
VLAN editing on ingress and one level on egress. The editing is performed at the flow level.  
Router 
The Megaplex-4 router is an internal Layer-3 interworking device that forwards traffic between its 
interfaces. Each router interface is assigned an IP address and can be bound to one of the following:  
4. Service Provisioning 
• 
Physical/logical E1/T1/DS1-opt (via DTS) or SDH/SONET (via DCC) port  
• 
SVI port connected via flow to a bridge port (which provides access to any Ethernet-type 
physical/logical port) 
The router uses switched virtual interfaces (SVIs) for connecting to logical and physical ports. The 
connection is always made by directing flows from a port to an SVI, and then binding the SVI to a router 
interface. 
4.2 Services Provided by Megaplex-4 
Both carriers and transportation and utility services providers can benefit from Megaplex-4 capabilities. 
The services for carriers and service providers (TDM and/or ETH grooming) are as follows.  
Carrier and utility services provided by Megaplex-4 include: 
• 
Aggregation Services: 
 
TDM (E1/T1) service aggregation over copper/fiber lines into SDH/SONET backbone 
 
TDM (E1/T1) service aggregation over copper/fiber lines into PSN backbone 
 
TDM (E1/T1) and Ethernet service aggregation over copper/fiber lines into SDH/SONET 
backbone 
 
TDM (E1/T1) and Ethernet service aggregation over copper/fiber lines into SDH/SONET and 
PSN backbone (TDM to TDM, Ethernet to PSN) 
 
TDM (E1/T1) and Ethernet service aggregation over copper/fiber lines into PSN backbone 
 
Ethernet service aggregation over copper/fiber lines into PSN. 
 
Voice aggregation to T3 backbones. 
• 
Cross-connect services: 
 
Legacy (Voice, serial) services cross-connect for interbranch connectivity  
 
Multiplexing any traffic (Legacy/TDM/Ethernet) for cross-connect services. 
 
T3 traffic to SONET (via T1 x-connect).  
Transportation and utility services provided by Megaplex-4 include: 
• 
TDM- and Ethernet service aggregation to SDH/SONET backbones  
• 
Legacy and new Ethernet-based service aggregation to SDH/SONET and PSN backbones (keeping 
mission-critical services towards the TDM backbone) 
• 
Legacy and new Ethernet-based service aggregation to PSN backbones  
4. Service Provisioning 
• 
Resilient ring topology for legacy and Ethernet services with minimal downtime 
• 
Teleprotection over SDH/SONET. 
Selected services from the above list are summarized in the table below and schematic diagrams in the 
figures below. Modules shown in diagrams as examples are listed in the following table in bold. If you 
want to draw a diagram for a specific service provided by another module, you can use the relevant 
elements of sample services to draw a service of your own.  
Table 4-1.  Selected Services Provided by Megaplex-4  
No 
Description 
I/O Modules Providing the 
Service 
Schematic 
Diagram  
Configuration 
Procedure 
3 
Shared E-LAN service with multiple drops 
per node over SDH/SONET  
M-ETH 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found.  
4 
High-Speed service aggregation into PSN 
backbone (low-latency) 
VS  
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found.  
Error! 
Reference 
source not 
found. 
6 
Voice aggregation to SDH/SONET 
backbones 
VC-4/VC-8/ VC-4A/ 
VC-8A/VC-16 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found. Error! 
Reference 
source not 
found. 
4. Service Provisioning 
No 
Description 
I/O Modules Providing the 
Service 
Schematic 
Diagram  
Configuration 
Procedure 
6a 
Voice service aggregation into PSN 
backbone 
VS Voice 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found. 
7 
Teleprotection over SDH/SONET  
TP 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found. Error! 
Reference 
source not 
found.  
8 
Voice aggregation to T3 backbones 
T3  
VC-4/VC-8/ VC-4A/ 
VC-8A/VC-16, VS Voice 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found.  
Error! 
Reference 
source not 
found. 
9 
T3 traffic to SONET  
T3 
Figure 4-11 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found. 
10a 
Ethernet traffic over PDH to SDH/SONET  
VS-16E1T1-EoP 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found. 
4. Service Provisioning 
No 
Description 
I/O Modules Providing the 
Service 
Schematic 
Diagram  
Configuration 
Procedure 
10b 
Ethernet traffic over PDH to TDM (E1/T1) 
VS-16E1T1-EoP 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found. 
Error! 
Reference 
source not 
found. 
The following figures schematically describe selected services provided by Megaplex-4.  
M-ETH
DS0 
X-Connect
CL.2
L.MAC
ETH 
Engine
GFP
VCAT
GbE
SDH/SONET
X-Connect
SDH/SONET 
Link
E1-i/T1-i
3
VC-4/4A/8/8A/16
Shared E-LAN service with multiple drops per node over SDH/SONET
SDH/
SONET
PSN
L.MAC
ETH 
Engine
 
Figure 4-1.  Service 3  
DS0 
X-Connect
CL.2
L.MAC
ETH 
Engine
GFP
VCAT
GbE
VS
SDH/SONET
X-Connect
SDH/SONET 
Link
E1-i/T1-i
4
High-Speed service aggregation to SDH/SONET backbones 
TP
PSN
SDH/
SONET
Serial
 
4. Service Provisioning 
Figure 4-2.  Service 4 
 
 
 
VS Voice
DS0 
X-Connect
CL.2
L.MAC
ETH 
Engine
GFP
VCAT
GbE
SDH/SONET
X-Connect
SDH/SONET 
Link
E1-i/T1-i
6
Voice aggregation to SDH/SONET backbones
SDH/
SONET
PSN
Voice
TP
 
Figure 4-3.  Service 6  
DS0 
X-Connect
CL.2
L.MAC
ETH 
Engine
GFP
VCAT
GbE
Voice
VS Voice
SDH/SONET
X-Connect
SDH/SONET 
Link
E1-i/T1-i
6a
Voice service aggregation into PSN backbone
PSN
SDH/
SONET
SVI
PW 
Router
PW
1/1
PW 
X-Connect
DS1
1/1
DS1/PW 1:1
  
Figure 4-4.  Service 6a  
4. Service Provisioning 
DS0 
X-Connect
CL.2
L.MAC
ETH 
Engine
GFP
VCAT
GbE
SDH/SONET
X-Connect
SDH/SONET 
Link
E1-i/T1-i
7
Teleprotection Traffic over SDH/SONET
SDH/
SONET
PSN
Voice
CMD
Channel
CMD-IN-I
CMD-OUT-I
CMD-IN
CMD-OUT
TP
 
Figure 4-5.  Service 7  
CL.2
L.MAC
ETH 
Engine
GFP
VCAT
GbE
SDH/SONET
X-Connect
SDH/SONET 
Link
SDH/
SONET
PSN
TP
DS0 
X-Connect
VC-4/4A/8/8A/16
T1
Voice
8
T3 to SONET
T3
T3
9
T3
T3
T1
Voice aggregation to SDH/SONET backbones
 
Figure 4-6.  Services 8,9  
4. Service Provisioning 
CL.2
VCAT
 VS-16E1T1-EoP
Ethernet Traffic over PDH to SDH/SONET 
10a
GFP
L.MAC
PSN
GbE
10b
 Ethernet Traffic over PDH to TDM(E1/T1) 
E1i
L.MAC
ETH 
Engine
M-ETH
SDH/SONET
X-Connect
SDH/SONET 
Link
SDH/
SONET
E1
GFP
VCG
ETH 
Engine
 
Figure 4-7.  Services 10a,10b  
Sections 4.3 to 4.23 summarize the steps required to configure selected services shown in the above 
diagrams. For further details on a configuration step, refer to the corresponding section indicated in the 
service provisioning table. 
Note 
• 
Applications in the following diagrams may be implemented in a different 
way; Sections 4.3 to 4.23 just show typical service elements.  
• 
The diagrams below display all possible protection alternatives. In most 
cases there is no need to configure all of them and it is recommended to 
select the one most suitable for your application.  
4. Service Provisioning 
4.3 E1/T1 Traffic to SDH/SONET via Direct Transparent 
Mapping (1a)  
Error! Reference source not found. illustrates an E1/T1 to SDH/SONET service via direct transparent 
mapping. This service is used for unframed E1/T1 ports of all I/O modules. Error! Reference source not 
found. details configuration steps needed for service provisioning. 
1. Define profiles
2. Configure ports
3. Configure 
cross-connect
Configure I/O 
card e1/t1 port
vc profile
I/O Module, 
E1/T1 Port
Configure 
sdh-sonet 
cross-connect
SDH/SONET Link
Configure link
Set sdh-sonet link 
parameters
Assign vc profile 
for each aug/oc-3 
VC-12/VT1.5
Optional
Mandatory
Legend:
Configure vc-path 
protection
Configure aps 
protection
4. Configure 
protection
E1/T1
 
Figure 4-8.  E1/T1 to SDH/SONET Service via Direct Transparent Mapping  
4. Service Provisioning 
Table 4-2.  E1/T1 to SDH/SONET Service Provisioning – Direct Transparent Mapping  
Sequence 
Step 
Commands 
Comments 
VC Profiles 
port vc-profile 
Configuring VC Profiles (to be assigned to 
AUG/OC-3 ports) (Chapter 5) 
E1 Ports 
T1 Ports 
port {e1 | t1} 
Configuring physical E1/T1 ports of I/O 
module (Chapter 5) 
SDH/SONET 
Ports  
port sdh-sonet 
Configuring physical SDH/SONET ports 
Selecting aug/oc3 group  
Assigning vc profile to aug/oc3 (Chapter 5) 
SDH/SONET 
Cross-Connect  
cross-connect sdh-
sonet  
Cross-connecting between E1/T1 ports and 
VC-12/VT1.5 containers (CL.2 module) 
(Chapter 5) 
Path Protection 
for SDH/SONET 
Payload 
protection vc-path 
Protecting SDH/SONET payload units 
(Chapter 7) 
APS Protection 
protection aps 
Protecting SDH/SONET links (Chapter 7) 
4.4 Shared E-LAN Service with Multiple Drops per Node over 
SDH/SONET (3)  
Error! Reference source not found. illustrates a shared E-LAN service with multiple drops per node over 
SDH/SONET, schematically shown in Error! Reference source not found.. The table below details 
configuration steps needed for service provisioning.  
4. Service Provisioning 
M-ETH 
Bridge
BP
BP
BP
Bind
 
SDH/SONET Link
VCG Port
GFP Port
1. Define profiles
2. Configure ports
3. Configure bridge and ERP
Configure 
Ethernet port 
VC profile
Set Ethernet 
port parameters
GFP Port
SDH/SONET Link
Configure link
Set sdh-sonet 
link parameters
Assign vc 
profile
Assign vc 
profile for each 
aug/oc-3 
Configure GFP 
port
Set gfp port 
parameters
VC-12/VT1.5
Optional
Mandatory
Legend:
Assign vc 
profile
Configure VCG 
port
Set vcg port 
parameters
Define logical 
mac port and 
bind gfp port
Bind vcg port
Bind vc/vt
Configure flows 
1a, 1b
Assign ingress 
and egress ports
Assign classifier 
profile
Define vlan 
editing actions
CL Bridge (1)
Flow 3
Flow 2
Classifier
Queue group
Marking
Queue block 
WRED
Shaper
Queue
Define VLANs
Configure bridge 
ports as VLAN 
members
Configure MAC 
table size
Flows 
1a, 1b
BP
BP
BP
Define ERP
Configure East 
and West ports
Configure RPL 
owner
Logical 
MAC
Logical 
MAC
VCG Port
M-ETH Module, 
GbE Ports
Bind queue 
group profile
Bind
4. Configure flows
Configure flows 
2,3
Bind ingress and 
egress ports
Bind classifier 
profile
Bind queue 
mapping profile
Bind queue 
block instance
ERP
Configure VLAN 
membership
Configure ERP
Define a bridge
Define a bridge
Define bridge 
ports
Define bridge 
ports
Bind to M-ETH 
Ethernet port
 
Figure 4-9.  Shared E-LAN Service with Multiple Drops per Node over SDH/SONET  
Table 4-3.  Shared E-LAN over SDH/SONET Service Provisioning 
Sequence 
Step 
Commands 
Comments 
1. 
Define 
profile
s 
VC Profiles 
port vc-profile 
Configuring VC profiles (to be assigned to 
gfp, vcg and aug/oc3 ports) (Chapter 5) 
4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
Classifier Profiles 
classifier-profile 
Define classification profiles for Flows 1a, 
1b and bidirectional Flows 2 and 3.  
Flows 1a, 1b: 
• Use “match all” setting  
• Push/pop Data VLAN of the ERP. 
Flows 2 and 3: use “match all” setting.  
Data VLAN is part of ERP definition 
(Chapter 8) 
Priority Queue 
Mapping 
queue-map-profile 
Define profile for mapping CoS values to 
queues (Chapter 8)  
Congestion 
Avoidance 
(WRED) 
wred-profile 
Define WRED profiles to be attached to 
queue profiles (Chapter 8) 
Shaper 
shaper-profile 
Define shaper profiles to be attached to a 
queue and queue group profiles (Chapter 
8) 
Queue Block 
queue-block-profile 
Define queue block profiles to be attached 
to queue group profiles (Chapter 8) 
Queue Group 
queue-group-profile 
Define queue group profile for GbE CL 
ports (Chapter 8) 
Marking 
marking-profile 
Define profile for conversion of CoS and 
packet color values into P-bit when push or 
mark tag editing is used (Chapter 8) 
2. Configure physical 
and logical ports 
Ethernet Ports  
port ethernet 
Configure physical parameters of GbE port 
(M-ETH module) (Chapter 5) 
VCG Ports 
 
port vcg 
Configure physical parameters of VCG port 
Assign vc profile (Chapter 5) 
Bind the corresponding VC-4/STS-3c, 
VC-3/STS-1 or VC-12/VT1.5 to the VCG  
4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
GFP Ports 
port gfp 
Configure physical parameters of GFP port 
Assign vc profile 
Bind the corresponding VCG to the GFP 
port (Chapter 5) 
When Ethernet service contains a single 
VC-3/STS-1 or VC-12/VT1.5 container, the 
GFP port can be bound to it directly 
Logical MAC 
Ports 
port logical-mac 
Define logical MAC ports to establish 
connectivity between gfp ports of CL 
module and bp ports of CL Bridge (1).   
Bind the queue group profile intended for 
Flows 2, 3 to Logical Mac port (Chapter 5) 
SDH/SONET 
Ports  
 
port sdh-sonet 
Configure physical SDH/SONET ports 
Select aug/oc3 group  
Assign vc profile to aug/oc3 
(Chapter 5) 
3. Define 
bridge 
Bridge 
bridge 
Define, assign a number and configure 
bridge entities: 
• M-ETH bridge (aware or unaware) 
• CL bridge (always aware) with VLAN 
table where the Data VLAN of ERP is 
configured with proper bridge ports 
• (Chapter 8) 
4. Define 
bridge 
ports 
Bridge 
bridge 
Define bridge ports (Chapter 8) 
M-ETH Bridge: Bind to M-ETH GbE ports  
(Chapter 8) 
5. 
Configure 
VLAN 
members
Bridge 
bridge 
Add VLANs, define bridge ports as VLAN 
members and specify MAC table size for 
each VLAN (Chapter 8) 
6. 
Config
ure 
ERP 
Bridge 
protection 
Define ERP, configure RPL owner, 
configure East and West ports  (Chapter 7) 

## 4.5 High-Speed Traffic to SDH/SONET (4)  *(p.214)*

4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
7. Configure flows 
Flows 
flows>flow 
Define the following flows:  
• Flow 1a: ingress – BP (CL), egress – 
BP (M-ETH) 
• Flow 1b: ingress – BP (M-ETH), egress – 
BP (CL) 
• Flows 2,3: ingress – Logical Mac, egress 
– BP  
Define VLAN editing actions  
Bind classifier profiles to all flows  
Bind queue mapping profile to flows 2,3 
Bind queue block instance to flows 2,3 
Bind marking profile to flows 2, 3 
(Chapter 8) 
4.5 High-Speed Traffic to SDH/SONET (4) 
Error! Reference source not found. illustrates a high-speed to SDH/SONET service. The table below 
details configuration steps needed for service provisioning. 
 
4. Service Provisioning 
Timeslots n*64
1. Define profiles
2. Configure ports
3. Configure cross 
connect
Configure I/O 
card serial port
Configure ds0 
cross connect
vc profile
I/O Module, 
Serial Port
CL.2 Module,
E1-i/T1-i Ports
Configure 
sdh-sonet cross 
connect
E1/T1
SDH/SONET Link
Configure link
Set sdh-sonet 
link parameters
Assign vc profile
Assign vc profile 
for each aug/oc-3 
Configure 
e1-i/t1-i parameters
Set e1-i/t1-i 
port parameters
VC-12/VT1.5
Optional
Mandatory
Legend:
Configure vc-path 
protection
Configure aps 
protection
4. Configure 
protection
Configure tdm-
group protection
 
Figure 4-10.  High-Speed to SDH/SONET Service  

## 4.6 Low-Latency High-Speed Traffic to PSN (4)  *(p.216)*

4. Service Provisioning 
Table 4-4.  High-Speed to SDH/SONET Service Provisioning 
Sequence 
Step 
Commands 
Comments 
1. 
Define 
profile
s
VC Profiles 
port vc-profile 
Configuring VC Profiles (to be assigned to 
E1-i/T1-i and AUG/OC-3 ports) (Chapter 5) 
2. Configure physical 
and logical ports 
Serial Ports  
port serial 
Configuring physical serial ports of I/O 
module (Chapter 5) 
E1 Ports 
T1 Ports 
port { e1-i | t1-i} 
Configuring physical parameters of E1-i/T1-
i ports (CL.2 module) 
Assigning vc profile 
(Chapter 5) 
SDH/SONET 
Ports  
port sdh-sonet 
Configuring physical SDH/SONET ports 
Selecting aug/oc3 group  
Assigning vc profile to aug/oc3 
(Chapter 5) 
3. Configure timeslot cross-
connections 
DS0 cross-
connect  
cross-connect ds0 
Cross-connecting between serial ports of 
high-speed module and timeslots of e1-
i/t1-i ports of CL.2 module 
(Chapter 8) 
SDH/SONET 
cross-connect  
cross-connect sdh-
sonet  
 
 
Cross-connecting between timeslots of 
E1-i/T1-i ports and VC-12/VT1.5 containers 
(CL.2 module) (Chapter 8) 
3. Configure 
protection 
TDM Group 
Protection 
protection tdm-group 
Protecting E1/T1 service (Chapter 7) 
Path Protection 
for SDH/SONET 
Payload 
protection vc-path 
Protecting SDH/SONET payload units 
(Chapter 7) 
APS Protection 
protection aps 
Protecting SDH/SONET links (Chapter 7) 
4.6 Low-Latency High-Speed Traffic to PSN (4)  
Error! Reference source not found. illustrates in detail low-latency high-speed to PSN (Ethernet) services 
using the pseudowire engine of RAD’s versatile VS modules, schematically shown in Error! Reference 
source not found.. 
4. Service Provisioning 
• 
Service 4: The traffic from serial port is forwarded to GbE port, which serves as a pseudowire 
exit port toward the PSN.  
Cross-connection of multiple ports has to be done via DS1 ports.  
The table below details configuration steps needed for service provisioning. 
4. Service Provisioning 
TS x 64 kbps
1. Define profiles
2. Configure ports
Configure I/O 
card serial port
classifier 
profile
VS Module, 
Serial Port
CL.2/GbE or 
any FE  
 port
Configure 
ethernet port
Set Ethernet 
port parameters
Assign policer 
profile
Optional
Mandatory
Legend:
9. Configure 
protection
Configure pw-
tdm protection 
8. Configure flows
3. Define SVI
Define SVI port
Define remote 
PW peer
5. Define PW peer
7. Configure 
cross-connections
6. Add a pseudowire
Configure pw-tdm 
cross-connect
Assign 
ingress and 
egress ports
Assign 
classifier 
profile
Configure flow 
1b
Define vlan 
editing 
actions
PW
Router
Flow 1a
SVI
Flow 1b
RIF
policer 
profile
Define RIFs
Define router 
interfaces
Bind router 
interfaces to 
SVIs
4. Define and bind 
router interfaces
VS Module, 
PW
Add and configure
a pseudowire
Assign 
ingress and 
egress ports
Configure flow 
1a
Define vlan 
editing 
actions
Add static 
routing table
Assign 
classifier 
profile
 
Figure 4-11.  Low-Latency High-Speed to Ethernet Service  
4. Service Provisioning 
Table 4-5.  Low-Latency High-Speed to Fast Ethernet Service Provisioning 
Sequence 
Step 
Commands 
Comments 
1. Define profiles 
Defining 
Classifier Profiles 
 
flows flow 
classifier-
profile 
Create classifier profile “match-all” (Chapter 8) 
Policer Profiles 
qos policer-
profile 
Configuring policer profiles (to be assigned to Fast 
Ethernet ports) (Chapter 8) 
2. Configure 
physical 
and logical 
Serial Ports  
port serial 
Configuring physical parameters of serial ports of 
I/O module (Chapter 5) 
Ethernet Ports 
 
port ethernet 
Configuring physical parameters of GbE port (CL.2 
module) (Chapter 5) 
3. Define SVIs 
Switched Virtual 
Interface 
port svi 
Define an SVI port.  
Keep in mind that PW SVI represents untagged 
traffic termination point. This means that VLAN tags 
must be pushed on exiting it and popped on the 
flows terminating at SVI. 
(Chapter 8) 
4. Add RIFs 
and bind them 
to SVIs 
Pseudowire 
Router 
router (2) 
Add interfaces to the router  
Define static routing table 
Bind the RIFs to the SVIs 
(Chapter 8) 
5. 
Defi
ne 
PW
Peer 
peer 
Configure remote pseudowire peer (Chapter 8) 
6. 
Defi
ne 
pse
Pseudowires 
pwe 
Add and configure pseudowires (Chapter 8) 
7. 
Config
ure 
cross c
PW-TDM 
Cross-connect  
cross-connect 
pw-tdm  
Cross-connecting between serial ports of high-speed 
module and PW (Chapter 8) 
8. Configure flows 
Flows 
flows>flow 
Define two flows: 
• Flow 1a: ingress – SVI, egress – Fast Ethernet 
port of I/O module 
• Flow 1b: ingress – Ethernet port of I/0 module, 
egress –SVI 
Assign classifier profile to flows 1a and 1b 
Define VLAN editing actions  
(Chapter 8) 
9. 
Con
figu
re
PW Protection 
protection pw 
Protecting PW service (Chapter 7) 

## 4.7 Voice Traffic to SDH/SONET (6)  *(p.220)*

4. Service Provisioning 
4.7 Voice Traffic to SDH/SONET (6)  
Error! Reference source not found. illustrates voice to SDH/SONET service. The table below details 
configuration steps needed for service provisioning. 
Voice
1. Define profiles
2. Configure ports
3. Configure cross 
connect
Configure I/O 
card voice port
Configure ds0 
cross connect
vc profile
I/O Module, 
Voice Port
CL.2 Module,
E1-i/T1-i Ports
Configure 
sdh-sonet cross 
connect
E1/T1
SDH/SONET Link
Configure link
Set sdh-sonet 
link parameters
Assign vc profile
Assign vc profile 
for each aug/oc-3 
Configure 
e1-i/t1-i parameters
Set e1-i/t1-i 
port parameters
VC-12/VT1.5
Optional
Mandatory
Legend:
Configure vc-path 
protection
Configure aps 
protection
4. Configure 
protection
Configure tdm-
group protection
 
Figure 4-12.  Voice to SDH/SONET Service 
Table 4-6.  Voice to SDH/SONET Service Provisioning 
Sequence 
Step 
Commands 
Comments 
VC Profiles 
port vc-profile 
Configuring VC Profiles (to be assigned to 
E1-i/T1-i and AUG/OC-3 ports) (Chapter 5) 
2
. 
C
o
Voice Ports  
port voice 
Configuring physical voice ports of I/O 
module (Chapter 5) 
E1 Ports 
T1 Ports 
port { e1-i | t1-
i} 
Configuring physical parameters of E1-i/T1-i 
ports (CL.2 module) 
Assigning vc profile 
(Chapter 5) 

## 4.8 Voice Traffic to PSN (6a)  *(p.221)*

4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
SDH/SONET Ports  
port sdh-sonet 
Configuring physical SDH/SONET ports 
Selecting aug/oc3 group  
Assigning vc profile to aug/oc3 
(Chapter 5) 
3. 
Config
ure 
timeslo
DS0 cross-connect  
cross-connect 
ds0 
Cross-connecting between serial ports of 
high-speed module and timeslots of e1-i/t1-i 
ports of CL.2 module 
(Chapter 8) 
SDH/SONET 
cross-connect  
cross-connect 
sdh-sonet  
 
 
Cross-connecting between timeslots of 
E1-i/T1-i ports and VC-12/VT1.5 containers 
(CL.2 module) (Chapter 8) 
TDM Group Protection 
protection 
tdm-group 
Protecting E1/T1 service (Chapter 7) 
Path Protection for 
SDH/SONET Payload 
protection vc-
path 
Protecting SDH/SONET payload units 
(Chapter 7)  
APS Protection 
protection aps 
Protecting SDH/SONET links (Chapter 7) 
4.8 Voice Traffic to PSN (6a)  
The following diagram illustrates in detail high-speed to PSN (Ethernet) services schematically shown in 
Error! Reference source not found..  
• 
Service 6a: The traffic from voice port is forwarded to GbE port, which serves as a pseudowire 
exit port toward the PSN.  
These services use the pseudowire engine of the VS voice module. The table below details configuration 
steps needed for service provisioning. 
4. Service Provisioning 
 64 kbps
1. Define profiles
2. Configure ports
Configure I/O card 
voice  port
classifier 
profile
VS Voice Module, 
Voicel Port
CL.2/GbE  
 port
Configure 
ethernet port
Set Ethernet 
port parameters
Assign policer 
profile
Optional
Mandatory
Legend:
8. Configure flows
3. Define SVI
Define SVI port
Define remote 
PW peer
5. Define PW peer
7. Configure 
cross-connections
6. Add a pseudowire
Configure pw-tdm 
cross-connect
DS1/PW 1:1
Assign 
ingress and 
egress ports
Assign 
classifier 
profile
Configure flow 
1b
Define vlan 
editing 
actions
PW
Router
Flow 1a
SVI
Flow 1b
RIF
policer 
profile
Define RIFs
Define router 
interfaces
Bind router 
interfaces to 
SVIs
4. Define and bind 
router interfaces
 PW
Add and configure
a pseudowire
Assign 
ingress and 
egress ports
Configure flow 
1a
Define vlan 
editing 
actions
Add static 
routing table
Assign 
classifier 
profile
Configure ds0 
cross-connect
VS Voice 
Module,
DS1 Ports
Configure ds1 
port
 
Figure 4-13.  Voice to Ethernet Service  
4. Service Provisioning 
Table 4-7.  Voice to Ethernet Service Provisioning 
Sequence 
Step 
Commands 
Comments 
1. Define profiles 
Defining 
Classifier Profiles 
 
flows flow 
classifier-
profile 
Create classifier profile “match-all” (Chapter 8) 
Policer Profiles 
qos policer-
profile 
Configuring policer profiles (to be assigned to 
Ethernet ports) (Chapter 8) 
2. Configure physical  
and logical ports 
Voice Ports  
port voice 
Configuring physical parameters of voice ports of 
I/O module (Chapter 5) 
DS1 Ports 
 
port ds1 
Configuring physical parameters of DS1 ports (I/O 
module) (Chapter 5) 
Ethernet Ports 
 
port ethernet 
Configuring physical parameters of GbE port (CL.2 
module, Service 6a) (Chapter 5) 
3. Define SVIs 
Switched Virtual 
Interface 
port svi 
Define an SVI port (Chapter 5)  
Keep in mind that PW SVI represents untagged 
traffic termination point. This means that VLAN tags 
must be pushed on exiting it and popped on the 
flows terminating at SVI.  
4. Add RIFs 
and bind them 
to SVIs 
Pseudowire 
Router 
router (2) 
Add interfaces to the router  
Define static routing table 
Bind the RIFs to the SVIs 
(Chapter 8) 
5. 
Defi
ne 
PW
Peer 
peer 
Configure remote pseudowire peer (Chapter 8) 
6. 
Define 
pseudo
wire
Pseudowires 
pwe 
Add and configure pseudowires (Chapter 8) 
Voice channels are sharing same PW. 
7. Configure 
cross-connecti
ons 
DS0 Cross-
connect  
cross-connect 
ds0 
Cross-connecting between voice ports and timeslots 
of DS1 ports of VS voice module (Chapter 8) 
PW-TDM 
Cross-connect  
cross-connect 
pw-tdm  
Cross-connecting between timeslots of DS1 ports 
and PW (Chapter 8) 

## 4.9 Teleprotection Traffic to SDH/SONET (7)  *(p.224)*

4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
8. Configure flows 
Flows 
flows>flow 
Define two flows: 
• Flow 1a: ingress – SVI, egress – Fast Ethernet 
port of I/O module 
• Flow 1b: ingress – Ethernet port of I/0 module, 
egress –SVI 
Assign classifier profile to flows 1a and 1b 
Define VLAN editing actions  
(Chapter 8) 
4.9 Teleprotection Traffic to SDH/SONET (7) 
Error! Reference source not found. illustrates teleprotection over SDH/SONET service. The table below 
details configuration steps needed for service provisioning. 
4. Service Provisioning 
Configure tdm-
group protection
64/128 kbps
1. Define profiles
2. Configure ports
3. Configure cross 
connect
Configure ds0 
cross connect
vc profile
I/O Module, 
CMD Channel 
Ports
CL.2 Module,
E1-i/T1-i Ports
Configure 
sdh-sonet cross 
connect
E1/T1
SDH/SONET Link
Configure link
Set sdh-sonet 
link parameters
Assign vc profile
Assign vc profile 
for each aug/oc-3 
Configure 
e1-i/t1-i parameters
Set e1-i/t1-i 
port parameters
VC-12/VT1.5
Optional
Mandatory
Legend:
Configure vc-path 
protection
Configure aps 
protection
4. Configure 
protection
Configure tdm-
group protection
Configure 
cmd-in-i port
I/O Module, 
CMD-IN-I Ports
Configure cmd-in 
port
I/O Module, 
CMD-IN Ports
Set cmd-in-i 
port parameters
Bind cmd-in 
port
Configure 
cmd-out-i port
I/O Module, 
CMD-OUT-I 
Ports
Configure cmd-
out port
I/O Module, 
CMD-OUT Ports
Set cmd-out 
port parameters
Bind cmd-out-i 
port
Configure cmd-
channel port
Configure TP 
cross connect
 
Figure 4-14.  Teleprotection Service  
Table 4-8.  TP to SDH/SONET Service Provisioning 
Sequence 
Step 
Commands 
Comments 
1. 
Define 
profile
s
VC Profiles 
port vc-profile 
Configuring VC Profiles (to be assigned to 
E1-i/T1-i and AUG/OC-3 ports) (Chapter 5) 
2. Configure physical  
and logical ports 
CMD-IN Ports  
port cmd-in 
Configuring cmd-in ports (Chapter 5) 
CMD-IN-I Ports  
port cmd-in-i 
Configuring cmd-in-i ports  
Binding the cmd-in port to the cmd-in-i port 
(Chapter 5) 
CMD-OUT Ports  
port cmd-out 
Configuring cmd-out ports  
Binding the cmd-out-i port to the cmd-out 
port 
(Chapter 5) 
4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
CMD-OUT-I Ports  
port cmd-out-i 
Configuring cmd-out-i ports (Chapter 5) 
CMD-CHANNEL Ports  
port cmd-
channel 
Configuring cmd channels (Chapter 5) 
E1 Ports 
T1 Ports 
port {e1-i | t1-i} 
Configuring physical parameters of E1-i/T1-i 
ports (CL.2 module) 
Assigning vc profile 
(Chapter 5) 
SDH/SONET Ports  
port sdh-sonet 
Configuring physical SDH/SONET ports 
Selecting aug/oc3 group  
Assigning vc profile to aug/oc3 
(Chapter 5) 
3. Configure timeslot 
cross-connections 
DS0 cross-connect 
cross-connect 
ds0 
Cross-connecting between the cmd-channel 
and timeslots on the E1/T1 ports of the uplink 
module (Chapter 8) 
SDH/SONET 
cross-connect  
cross-connect 
sdh-sonet  
 
 
Cross-connecting between timeslots of 
E1-i/T1-i ports and VC-12/VT1.5 containers 
(CL.2 module) (Chapter 8) 
3. Configure protection 
TDM Group Protection 
protection 
tdm-group 
Protecting E1/T1 service 
Protecting CMD channels 
(Chapter 7) 
Path Protection for 
SDH/SONET Payload 
protection vc-
path 
Protecting SDH/SONET payload units 
(Chapter 7) 
APS Protection 
protection aps 
Protecting SDH/SONET links (Chapter 7) 
 

## 4.10 T3 Traffic to SONET (8)  *(p.227)*

4. Service Provisioning 
4.10 T3 Traffic to SONET (8)  
Error! Reference source not found. illustrates a T3 to SONET service using T3 module. The table below 
details configuration steps needed for service provisioning. 
Fixed 
connection
1. Define profiles
2. Configure ports
3. Configure 
cross-connect
Configure I/O 
card T3 port
vc profile
T3 I/O Module, 
T3 Port
T3 Module,
T1 Ports
Configure 
sdh-sonet 
cross-connect
SONET Link
Configure link
Set sdh-sonet 
link parameters
Assign vc profile 
for each aug/oc-3 
Configure 
t1 parameters
Set t1 port 
parameters
VT1.5
Optional
Mandatory
Legend:
Configure aps 
protection
Configure tdm-
group protection
4. Configure 
protection
T1
 
Figure 4-15.  T3 to SDH/SONET Service  
Table 4-9.  T3 to SDH/SONET Service Provisioning  
Sequence 
Step 
Commands 
Comments 
1. 
Define 
profile
s
VC Profiles 
port vc-profile 
Configuring VC Profiles (to be assigned to 
OC-3 ports) (Chapter 5) 
2. Configure physical  
and logical ports 
T1 Ports 
configure port e1-t1 t1 
Configuring parameters of T1 ports (T3 
module) (Chapter 5) 
T3 Ports  
configure port e3-t3 t3 
Configuring physical T3 ports (Chapter 5) 
SONET Ports  
port sdh-sonet 
Configuring physical SONET ports 
Selecting oc3 group  
Assigning vc profile to oc3 
(Chapter 5) 
4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
3. Configure cross-
connections 
SDH/SONET 
Cross-Connect  
cross-connect sdh-
sonet  
Cross-connecting between T1 ports (T3 
module) and VT1.5 containers (CL.2 
module) 
(Chapter 8) 
 
 
 
4. 
Configure 
protection 
TDM Group 
Protection 
protection tdm-group 
Protecting T3 and T1 services (Chapter 7) 
APS Protection 
protection aps 
Protecting SDH/SONET links (Chapter 7) 
4.11 Voice to T3 via DS0 Cross-Connect (9) 
Error! Reference source not found. illustrates a voice to T3 service via DS0 cross-connect. The table 
below details configuration steps needed for service provisioning.  
1. Configure ports
2. Configure 
cross-connect
Configure I/O 
card voice port
Configure DS0 
cross-connect
I/O Module, 
Voice Port
T3 Module,
T1 Ports
T3 Module,
T3 Port
Configure t3 port
Set t3 link 
parameters
Configure 
t1 parameters
Set t1 port 
parameters
Optional
Mandatory
Legend:
Configure 
tdm-group 
protection
3. Configure 
protection
Fixed 
connection
Configure 
tdm-group 
protection
 
Figure 4-16.  Voice Aggregation to T3 Link 
4. Service Provisioning 
Table 4-10.  Voice Aggregation to T3 Link Provisioning  
Sequence 
Step 
Commands 
Comments 
Voice Ports 
 
configure port voice 
Configuring physical voice ports of I/O 
module (Chapter 5) 
T1 Ports 
configure port e1-t1 t1 
Configuring parameters of internal T1 ports 
(T3 module) (Chapter 5) 
T3 Ports  
configure port e3-t3 t3 
Configuring physical T3 ports (Chapter 5) 
DS0 Cross-
Connect  
cross-connect ds0 
Cross-connecting between the voice port 
of VC module and internal T1 port of T3 
module (Chapter 8) 
TDM Group 
Protection 
protection tdm-group 
Protecting T3 ports (Chapter 7) 
TDM Group 
Protection 
protection tdm-group 
Protecting T1 ports (Chapter 7) 
4.12 Ethernet Traffic over PDH to SDH/SONET (10a)  
Error! Reference source not found. illustrates an Ethernet traffic over PDH to SDH/SONET service. This 
service is shown in Figure 4-10 on the example of VS-16E1T1-EoP module. The table below details 
configuration steps needed for service provisioning. 
4. Service Provisioning 
1. Define profiles
2. Configure ports
4. Configure flows
Configure 
Ethernet port 
VC profile
Set Ethernet 
port parameters
CL.2/GbE  
 port 
SDH/SONET Link
Configure link
Set sdh-sonet 
link parameters
Configure vc-
path protection
Assign vc 
profile
Assign vc 
profile for each 
aug/oc-3 
Configure GFP 
port
Set gfp port 
parameters
VC-12/VT1.5
Optional
Mandatory
Legend:
5. Configure protection
Logical 
MAC
VCG Port
Assign vc 
profile
Configure VCG 
port
Set vcg port 
parameters
Policer profile
Classifier 
profile
Assign policer 
profile
Define logical 
mac port and 
bind gfp port
Configure aps 
protection
Bind vcg port
Bind vc/vt
Configure flow 
1b
Configure flow 
1a
Assign 
ingress and 
egress ports
Assign 
classifier 
profile
Define vlan 
editing 
actions
Flow 1a
Flow 1b
Assign 
ingress and 
egress ports
Assign 
classifier 
profile
Define vlan 
editing 
actions
E1-i/T1-i Port
E1/T1
Assign vc profile
Configure 
e1-i/t1-i 
parameters
Set e1-i/t1-i port 
parameters
3. Configure 
cross-connect
Configure 
sdh-sonet 
cross-connect
GFP Port
 
Figure 4-17.  Ethernet Traffic over PDH to SDH/SONET Service  
Table 4-11.  Ethernet traffic over PDH to SDH/SONET Service Provisioning 
Sequence 
Step 
Commands 
Comments 
1. Define profiles 
VC Profiles 
port vc-profile 
Configuring VC profiles (to be assigned to 
gfp, vcg and aug/oc3 ports) (Chapter 5) 
Policer Profiles 
qos policer-profile 
Configuring policer profiles (to be assigned 
to Ethernet ports) (Chapter 8) 
Classifier Profiles 
flows 
classifier-profile 
Define classification profile for traffic 
originating from the port (Chapter 8) 
2. 
Config
ure 
physic
Ethernet Ports  
port ethernet 
Configuring physical Ethernet ports CL.2 
module (Chapter 5) 
4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
Logical MAC 
Ports 
port logical-mac 
Defining logical MAC port to establish 
connectivity between gfp and ethernet 
ports (Chapter 5)   
GFP Ports 
port gfp 
Configuring physical parameters of GFP 
port 
 
Binding the corresponding VCG 
to the GFP port 
 
(Chapter 5)  
VCG Ports 
port vcg 
Configuring physical parameters of VCG 
port (Chapter 5) 
E1 Ports 
T1 Ports 
port { e1-i | t1-i} 
Configuring physical parameters of E1-
i/T1-i ports (VS-16E1T1-EoP module) 
(Chapter 5) 
SDH/SONET 
Ports  
port sdh-sonet 
Configuring physical SDH/SONET ports 
(Chapter 5) 
3. 
Configure 
cross-
connectio
SDH/SONET 
Cross-Connect  
cross-connect sdh-
sonet  
Cross-connecting between E1-i/T1-i ports 
(VS-16E1T1-EoP module) and VC-12/VT1.5 
containers (Chapter 8) 
4. Configure flows 
Flows 
flows>flow 
Define two flows: 
• Flow 1a: ingress – logical mac, egress –
GbE port of CL.2 modules 
• Flow 1b: ingress –GbE port of CL.2 
modules, egress –logical mac 
Assign classifier profile to flows 1a and 1b 
• Define VLAN editing actions 
• (Chapter 8) 
5. Configure 
protection 
Path Protection 
for SDH/SONET 
Payload 
protection vc-path 
Protecting SDH/SONET payload units 
(Chapter 7) 
APS Protection 
protection aps 
Protecting SDH/SONET links (Chapter 7) 
4. Service Provisioning 
4.13 Ethernet Traffic over PDH to E1/T1 (10b) 
Error! Reference source not found. illustrates an Ethernet traffic over PDH to E1/T1 service. This service 
is shown in Figure 4-10 on the example of VS-16E1T1-EoP module. The table below details configuration 
steps needed for service provisioning.  
M-ETH 
Bridge
BP
BP
BP
Bind
1. Define profiles
2. Configure ports
3. Configure bridge 
Configure 
Ethernet port 
Set Ethernet 
port parameters
GFP Port
Assign vc 
profile
Configure GFP 
port
Set gfp port 
parameters
Optional
Mandatory
Legend:
Assign vc 
profile
Configure VCG 
port
Set vcg port 
parameters
Define logical 
mac port and 
bind gfp port
Bind vcg port
Bind e1/t1 
port
Configure flows 
1a, 1b
Assign ingress 
and egress ports
Assign classifier 
profile
Define vlan 
editing actions
Define VLANs
Configure bridge 
ports as VLAN 
members
Configure MAC 
table size
Flows 
1a, 1b
VCG Port
M-ETH Module, 
GbE Ports
Bind
4. Configure flows
Configure VLAN 
membership
Define a bridge
Define bridge 
ports
Bind to M-ETH 
Ethernet port
E1/T1 Port
Configure 
e1/t1 port
VC profile
Classifier 
profile
Logical 
MAC
VC profile
 
Figure 4-18.  Ethernet traffic over PDH to E1/T1 Service 
4. Service Provisioning 
Table 4-12.  Ethernet traffic over PDH to E1/T1 Service Provisioning 
Sequence 
Step 
Commands 
Comments 
1. Define 
profiles 
VC Profiles 
port vc-profile 
Configuring VC profiles (to be assigned to 
gfp, vcg and aug/oc3 ports) (Chapter 5) 
Classifier Profiles 
classifier-profile 
Define classification profile for traffic 
originating from the port (Chapter 8) 
2. Configure physical 
and logical ports 
Ethernet Ports  
port ethernet 
Configure physical parameters of GbE port 
(M-ETH module) (Chapter 5) 
Logical MAC 
Ports 
port logical-mac 
Define logical MAC ports to establish 
connectivity between gfp ports of VS-
16E1T1-EoP module and bp ports of M-
ETH Bridge (Chapter 5)  
GFP Ports 
port gfp 
Configure physical parameters of GFP port 
Assign vc profile (Chapter 5) 
 
Bind the corresponding VCG to 
the GFP port (Chapter 5)  
VCG Ports 
port vcg 
Configure physical parameters of VCG port 
Assign vc profile  
 
Bind the corresponding E1/T1 
port to the VCG (Chapter 5) 
E1 Ports 
T1 Ports 
port {e1 | t1} 
Configuring physical parameters of E1/T1 
ports (VS-16E1T1-EoP module) (Chapter 5) 
3. Define 
bridge 
Bridge 
bridge 
Define, assign a number and configure 
bridge entities: M-ETH bridge (Chapter 8) 
Bridge 
bridge port 
Define bridge ports 
M-ETH Bridge: Bind to M-ETH GbE ports  
(Chapter 8) 
Bridge 
bridge vlan 
Add VLANs, define bridge ports as VLAN 
members and specify MAC table size for 
each VLAN (Chapter 8) 
4. Service Provisioning 
Sequence 
Step 
Commands 
Comments 
4. Configure flows 
Flows 
flows>flow 
Define the following flows:  
• Flow 1a: ingress – Logical Mac (VS-
16E1T1-EoP), egress – BP (M-ETH) 
• Flow 1b: ingress – BP (M-ETH), egress – 
Logical Mac (VS-16E1T1-EoP) 
Define VLAN editing actions  
Bind classifier profiles to all flows  
(Chapter 8) 
 
 
 