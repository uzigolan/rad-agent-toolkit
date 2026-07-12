# 1 Introduction

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 57–119.*


## 1.1 Overview  *(p.57)*

1.1 Overview  
RAD’s Megaplex-4 multiservice next generation access nodes are high-capacity, carrier-class multiservice 
concentrators, which transport traffic over fiber or copper and provide multiple Legacy and next-
generation services on PDH/SDH/SONET or packet-switched networks (PSN). The Megaplex-4 family 
includes two devices: a powerful 10-slot Megaplex-4100 and a compact 4-slot Megaplex-4104. 
Megaplex-4 is an ideal solution for carriers and private network operators in migrating their networks 
and services to next-generation communications. Featuring dual star connection architecture with 
hybrid TDM-Ethernet modules allows native TDM and native Ethernet traffic handling with minimal 
encapsulation delays and zero bandwidth overhead. In networks with SDH/SONET backbone, Ethernet 
can be carried over VCG. In addition, it is equipped with a full standards-based pseudowire emulation 
suite, ensuring TDM service quality is maintained when migrating the services from TDM network to 
packet switched network.  
Carrier class service reliability is ensured with system redundancy options, link and path protection 
schemes and enhanced support for diverse ring topologies.  
Handling a broad range of SDH/SONET, E1/T1, Ethernet, data and voice services, various network 
topologies and versatile access media in a single compact managed node, makes Megaplex-4 a versatile 
and cost-effective next-generation multiservice access node solution for large enterprises, including 
utilities, transportation and campuses, as well as for carriers and service providers. 
Product Options   
Chassis 
Megaplex-4 systems are available in two chassis sizes: 
• 
Megaplex-4100 – 4U-high chassis can accommodate up to 10 I/O modules. 
1. Introduction 
• 
Megaplex-4104 – compact 2U-high chassis can accommodate up to 4 I/O modules. It is a 
cost-effective alternative for power utility substations, service providers, and small POP or 
branch office applications or for sites with limited space.  
IEEE-1613 Compliance  
Special Megaplex-4100 chassis ordering options are available complying with IEEE-1613 environmental 
requirements (for teleprotection/communications devices in the power utilities substations as well as 
other markets, see Chapter 2 for details).  
CL Modules  
The CL.2 modules are provided in several flavors, to cater for specific needs of each customer. The 
following table lists the functionalities supported by each CL.2 option. A short description of CL.2/A, 
CL.2/DS0 and /AP options is given in this section below. 
Note 
Starting from Megaplex release 4.81, CL.2 Non-A versions are moved to 
mature operation  and the CL types provided by RAD will be available are 
CL.2/A(P) and CL.2/DS0. Customers who purchased the “non-A” CL version will 
be able to order it with Megaplex SW versions 4.71 and lower.  RAD will 
continue to support all systems and CL types according to RAD’s standard 
support policies.  
Features Supported by CL.2 Options  
CL.2/622GBEA 
CL.2/622GBEAP 
CL.2/GBEA 
CL.2/GBEAP 
CL.2/622GBE  CL.2/DS0 
SDH/SONET 
+ 
- 
+ 
- 
DS0 Cross-Connect 
+ 
+ 
+ 
+ 
E-line 
+ 
+ 
+ 
Inside 
modules only 
E-LAN 
+ 
+ 
M-ETH only 
M-ETH only 
E-Tree 
+ 
+ 
- 
- 
Management VLAN via VCG 
+ 
- 
- 
- 
Flow between modules (CL and I/O)  
+  
+  
+  
-  
Traffic Management  
(Scheduling/Shaping) 
+  
+  
-  
-  
1. Introduction 
CL.2/622GBEA 
CL.2/622GBEAP 
CL.2/GBEA 
CL.2/GBEAP 
CL.2/622GBE  CL.2/DS0 
Maximum number of VS-6/E1, VS-6/T1 or T3 
modules per chassis (see the corresponding 
module manual) 
10 
9 
10 
9  
Maximum number of other VS modules per 
chassis (see the corresponding module 
manual) 
9 
9 
9 
9  
Ethernet Protection 
  
ERPS 
+ 
+ 
- 
- 
LAG + LACP 
+ 
+ 
- 
- 
LAG 
+ 
+ 
+ 
- 
RSTP  
+ 
+ 
- 
- 
Ethernet group protection 
- 
- 
+ 
- 
Security 
  
802.1x  
+ 
+ 
- 
-  
Service Assured Access 
CIR, CBS, EIR and EBS per flow 
+ 
+ 
- 
- 
CIR, CBS per port 
+ 
+ 
- 
- 
Classification per P-Bit/DSCP 
+ 
+ 
- 
- 
Classification per single or double VLAN   
+ 
+ 
+ 
- 
Ethernet OAM 
+ 
+ 
- 
- 
VLAN editing 
Inner + Outer 
Inner + 
Outer 
Outer 
Outer 
Ethernet PM 
+ 
+ 
- 
- 
Timing 
Internal Clock Quality 
ST-3E 
ST-3E 
ST-3E 
ST-4 
Clock Quality Status (SSM) 
+ 
+ 
- 
-     
SyncE 
+ 
+ 
- 
Diagnostics 
Ethernet BERT 
+ 
+ 
+ 
- 
1. Introduction 
CL.2/622GBEA 
CL.2/622GBEAP 
CL.2/GBEA 
CL.2/GBEAP 
CL.2/622GBE  CL.2/DS0 
TDM BERT  
+ 
+ 
+ 
+   
In-Service Ping  
+ 
+ 
- 
- 
Carrier Ethernet (CL.2/A Assembly)  
The CL.2/A assembly provides carrier Ethernet capabilities, such as Ethernet traffic management (TM), 
standards-based Ethernet Operations, Administration and Maintenance and Performance Monitoring 
(OAM&P), as well as carrier grade Ethernet functionality. 
These functionalities are available on any MAC entity, such as the CL module GbE ports, VCG, Ethernet 
module (M-ETH) ports, etc.  
This assembly can be ordered with or without SDH/SONET interface. 
SDH/SONET Interface  
Two SDH/SONET ports located on the CL.2 modules can be ordered in two versions: 
• 
STM-1/OC-3 only, with software key license upgrade to STM-4/OC-12 if required 
• 
Software-configurable to STM-4/OC-12 or STM-1/OC-3, with software key license built-in.  
The panels and terminal identification for the STM-1/OC-3 and STM-4/OC-12 versions are identical. 
GbE Interface 
The GbE ports can be ordered with one of the following interfaces: 
• 
10/100/1000BASE-T (UTP) copper ports. This type of ports support auto-negotiation, with 
user-specified advertised data rate (10, 100 or 1000 Mbps) and operating mode (half- or 
full-duplex).  
• 
SFP sockets, for installing SFP plug-in modules.  
DS0 Cross-Connect  
A basic low-cost version of CL.2 modules is supplied without SDH/SONET and GbE ports.  

## 1.2 New in this Version  *(p.61)*

1. Introduction 
CL Module for “No Fans” Operation  
There are special CL.2 options complying with IEEE-1613 to support “No Fans operation” requirement. 
These CL options have to be ordered together with a special IEEE-1613-compliant Megaplex-4100 
chassis. 
PS Modules  
PS modules for Megaplex-4100 and Megaplex-4104 have different shape and technical characteristics 
(see table above. AC or DC power supplies are available for both chassis. The DC modules can be 
ordered with selectable ground reference or floating ground. 
Megaplex-4 can be ordered with one power supply module, or with two power supply modules, for 
redundancy.  
The Megaplex-4100 chassis also has a selection of PS options complying with IEEE-1613 to support “No 
Fans operation” requirement. These options have to be ordered together with a special IEEE-1613-
compliant chassis. 
Applications  
Central Solution for RAD CPE Devices 
Megaplex-4 offers a complete, end-to-end solution as a central aggregation platform for diverse CPE 
devices managed together under RADview.  
The following figure illustrates Megaplex-4 as a central site solution, Ethernet and TDM aggregator for 
SDH/SONET and PSN networks. 

## 1.3 Physical Description  *(p.62)*

1. Introduction 
E1/T1
ETH
ETH
ETH
ETH
STM-1/
OC-3
E1
E1
ETH
ETH
n x E1
Voice
Data
E3 Chanellized
n x E1
STM-1
STM-1/OC-3
E1/T1
FE
FE
SHDSL.bis
FO
STM-4/
OC-12
ETH
FE
FE
Wireless
E1/V.35
FE/GbE
POP
PSN
SDH/SONET
RV Station
RICi-8
DXC-8R
MP-2100/2104
FCD-155E
IPmux
ASMi
ETX
Optimux
FCD-IP
Router
Video
Airmux
Airmux
ASMi-53
FCD-E1E
DXC-4
Megaplex-4
SHDSL
Megaplex-4104
Radio
Radio
T3
T3
SHDSL.bis
SHDSL
E1/V.35
 
Megaplex-4 as a Central Site Aggregator for different RAD CPEs, Ethernet and TDM Aggregator for 
SDH/SONET and PSN  
TDM and Ethernet Multiservice Access  
Enterprises, campuses and utility companies can deploy Megaplex-4 as a core or an edge device to 
create a diversity of STM-1/STM-4/OC-3/OC-12 or Ethernet rings, multiplexing voice, fax, data, and other 
low speed traffic. Megaplex-4 can also groom and cross-connect between channels and terminate 
Ethernet traffic. Megaplex-4 can work with industry-specific devices, such as Teleprotection and 
Omnibus units: 

## 1.4 Functional Description  *(p.63)*

1. Introduction 
SDH/SONET/ETH
LAN
PA
FXS
E&M
FO
SHDSL.bis
FO
E1/T1
GbE
Control Center
E1/T1
ASMi
Airmux-400
Airmux-400
LAN
PBX
Optimux
LAN
PBX
TAC
PSN
LAN
PA
FXS
E&M
TAC
SCADA
Megaplex-4100
Megaplex-4100
Megaplex-4104
Megaplex-4104
Megaplex-2100
 
Megaplex-4 as Multiservice Platform for Transportation and Power Utilities  
Carrier Ethernet Services  
Megaplex-4 delivers Ethernet services as defined by the MEF standards. MEF  identifies  three  types  of  
standardized  Carrier  Ethernet  services,  each  of  which corresponds with a set of UNI attributes and 
EVC attributes: 
• 
E-Line: A point-to-point connection, where each EVC links two UNIs. E-Line services can be of 
either of two variants: 
 
Ethernet Private Line (EPL):  An E-Line-type service in which only one point-to-point EVC  is 
supported  by  the  same  physical  interface  at  both  UNIs,  i.e.  no service multiplexing is 
allowed. EPL may be delivered as a guaranteed bandwidth service, whereby the carrier 
provides SLA-based rate and performance commitments and allocates network resources 
accordingly, similar to a leased line service. 
 
Ethernet Virtual Private Line (EVPL): An E-Line service (see below) allowing service 
multiplexing so that a  single UNI  supports  multiple  EVCs.  As data  frames  may  be  
mapped  to different EVCs, an EVPL service is not required to provide full frame 
transparency, unlike  an  EPL  service.  User traffic is distinguished by  different  VLAN  IDs  
and transported over   common   network resources, thereby necessitating traffic 
policing/shaping functionalities at the provider network ingress. 
• 
E-LAN (Ethernet Local Area Network): A multipoint-to-multipoint topology, where each EVC 
links more than two UNIs. The following are designated as E-LAN services: 
1. Introduction 
 
Ethernet Private LAN (EPLAN): A multipoint service (see below), requiring a dedicated UNI 
per EVC, in which service multiplexing is prohibited. Other service attributes are similar to 
those of a point-to-point EPL service. 
 
Ethernet  Virtual  Private LAN (EVPLAN):  An  E-LAN-type  service (see below) allowing  EVC 
multiplexing at the UNI, similar in attributes to an EVPL. A flow based EVPLAN service 
enables   service   multiplexing   for   applications   such   as   departmental   LAN 
differentiation – by service, location or user function – at the UNI level. 
• 
E-Tree: A service using a multipoint rooted EVC, whereby one or more of the UNIs are classified 
as “Roots”, while all other UNIs are designated as “Leaves”. Traffic delivery is permitted 
between a Root and a Leaf, in both directions, but prohibited between Leaves. Specific 
Root/Leaf subsets and the corresponding traffic delivery rules depend on particular service 
definitions. 
 
 
EPL (Ethernet Private Line) Service  
1. Introduction 
 
EVPL (Ethernet Virtual Private Line) Service 
 
EP-LAN (Ethernet Private LAN) Service  
 

## 1.5 Technical Specifications  *(p.66)*


## 2.1 Storage and Transportation  *(p.66)*


## 2.2 Safety  *(p.66)*

1. Introduction 
 
EVP-LAN (Ethernet Virtual Private LAN) Service 
Features  
PDH Access 
Megaplex-4 delivers PDH Access at E1/T1 and fractional E1/T1 level with up to 160 E1/T1 ports per 
chassis over copper or fiber. 
Data Services  
Megaplex-4 provides up to 120 multichannel sub-DS0 low speed data, 64-kbps codirectional G.703 
channels, teleprotection channels, and n×64 kbps high speed data (up to 2.048 Mbps for E1 
environments, or up to 1.544 Mbps for T1 environments). 
Voice Services  
Voice services are provided by analog and digital voice modules (up to 4800 voice channels per chassis 
for E1 ports, up to 3840 voice channels for T1 ports), with support for special services such as omnibus 
and party lines. Voice channel processing can include user-defined signaling translations.  

## 2.3 Site Requirements and Prerequisites  *(p.67)*


## 2.4 Package Contents  *(p.67)*


## 2.5 Required Equipment  *(p.67)*


## 2.6 Mounting the Products  *(p.67)*

1. Introduction 
SDH/SONET Services 
SDH/SONET services are provided by up to 4 separately configurable STM-1/STM-4 or OC-3/OC-12 links 
per node, with support for APS (Automatic Protection Switching) for line redundancy.  
Ethernet Layer 2 Services  
Ethernet Layer 2 services are supported by various I/O modules with Ethernet ports, and 4 GbE ports on 
CL modules. Up to eight separately configurable Ethernet ports are available per I/O module; each CL 
module has two GbE ports, for up to four separately configurable GbE ports per chassis. Megaplex-4 can 
provide Ethernet traffic termination for transport over E1, T1 uplinks, virtually concatenated group 
uplinks and high and low-order SDH/SONET VC-12/VC1.5 virtual containers. It can also serve as Ethernet 
access concentrator with GbE uplinks. 
Incoming Ethernet traffic is classified and mapped according to port-based (all-in-one) bundling or by 
user port and CE VLAN-ID, VLAN priority, DSCP, IP precedence, and Ethertype. This offers operators the 
flexibility to differentiate services using traffic management TM tools, such as traffic policing, queuing 
and shaping, and enforce SLA per service.  
Megaplex-4 supports powerful bandwidth profiles such as CIR/CBS and EIR/EBS for differentiated 
Ethernet services and includes comprehensive Ethernet OAM (Operation, Administration, and 
Maintenance) and Ethernet Performance Monitoring functionality together with SLA monitoring.  
Forwarding Schemes 
Traffic forwarding is performed using point-to-point (E-Line) or bridge (E-LAN, E-TREE) mechanisms.  
Service Types 
Megaplex-4 provides port- and flow-based services. 
Port-Based Service 
In a typical port-based (all-to-one bundling) application Megaplex-4 receives different services via 
different user ports. This method achieves clearer service separation, it does not require any customer 
marking for CoS. 

## 2.7 Installing Modules  *(p.68)*

1. Introduction 
Customer Premises
GbE
Service Provider Node
Packet Switched 
Network
(Ethernet, IP or MPLS)
PE
GbE
GbE
Megaplex-4
VoIP
Best Effort
Data
Premium
Data
 
Port-Based Service  
Flow-Based Service 
In a typical flow-based application different services are assigned to different Ethernet flows received by 
the same user port. This provides a cheaper, more scalable solution, with a possibility of mixing different 
service types. 
Customer Premises
GbE
Service Provider Node
Megaplex-4
Packet Switched 
Network
(Ethernet, IP or MPLS)
PE
VoIP
Premium
Data
Best Effort
Data
 
Flow-Based Service 
Flow Classification 
The ingress user traffic is mapped to the Ethernet flows using the following list of per-port classification 
criteria. In the classifications, VLAN refers to the service provider (outer) VLAN, previously referred to as 
SP-VLAN, while inner VLAN refers to the Customer Entity VLAN, previously referred to as CE-VLAN. 
• 
Port-based (All to one bundling) 
• 
VLAN  
• 
VLAN + VLAN priority 
• 
VLAN + IP precedence  
• 
VLAN + DSCP 
• 
VLAN + inner VLAN 
• 
VLAN + VLAN priority + inner VLAN  
• 
VLAN + Ethertype 

## 2.8 Connecting to Power  *(p.69)*


## 2.9 Connecting Megaplex-4 to a Terminal  *(p.69)*

1. Introduction 
• 
VLAN priority 
• 
IP precedence 
• 
DSCP 
• 
Ether Type 
• 
Untagged 
Megaplex-4 supports up to 512 Ethernet flows. Flows between external Ethernet ports and the CL.2/A 
bridge are bidirectional. All other flows are unidirectional. 
Tagging and Marking  
Megaplex-4 supports several options for marking and tagging.  
You can perform the following marking and tagging actions: 
• 
Overwrite inner or outer VLAN with a new value  
• 
Overwrite inner or outer VLAN p-bit with a new value.  
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
Only certain combinations of actions on the outer and inner VLAN are allowed. Refer to Chapter 8 for 
details on the permitted combinations of actions. 
L2CP Handling   
Megaplex-4 can be configured to pass through (“tunnel”) Layer-2 control frames (including other 
vendors’ L2CP frames) across the network, to peer supported protocols, or to discard L2CP frames. 

## 2.10 Connecting to a Management Station or Telnet Host  *(p.70)*


## 2.11 Connecting to a Station Clock  *(p.70)*

1. Introduction 
Fault Propagation 
The user can configure fault propagation between any two ports in Megaplex-4, as shown in the figure 
below.The fault propagation behavior is according to the port type (refer to Chapter 7 for details). 
 
Packet Switched 
Network
(Ethernet, IP or MPLS)
Megaplex-4
CPE
Network Termination 
Unit
 
Fault Propagation 
Traffic Management and Service Level Agreement (SLA) Monitoring, Troubleshooting and 
Measurement 
Powerful tools assure Megaplex-4’s ability to analyze the current traffic load and dynamically make 
necessary adjustments to accommodate the different types of traffic or changing conditions. RAD also 
provides effective service-level agreement (SLA) monitoring tools such as Ethernet service OAM (CFM), 
Ethernet link OAM (EFM) etc. 
Quality of Service (QoS)  
Megaplex-4 efficiently handles multi-priority traffic on a per-flow basis, that enables simultaneous 
processing of hundreds of service flows. The device enables multi-criteria traffic classification as well as 
metering, policing and shaping to help carriers rate-limit user traffic according to predefined CIR 
(committed information rate) and EIR (excess information rate) profiles. 
Enhanced quality of service is further supported by up to 2-level hierarchical scheduling mechanism that 
combines Strict Priority (SP) and weighted fair queue (WFQ) scheduling, to efficiently handle real-time, 
premium and best-effort traffic. Scheduling and shaping are supported at the EVC, and port levels. 
Megaplex-4 also uses weighted random early detection (WRED) policy for intelligent queue 
management and congestion avoidance. Packet editing capabilities include 802.1ad Q-in-Q tagging and 
color-sensitive P-bit re-marking, which ensures metering continuity across color-aware and color-blind 
Metro networks and WANs. 
1. Introduction 
Different service types require different levels of QoS to be provided end-to-end. QoS can be defined 
per subscriber as well as per flow. QoS has three aspects: policing (rate limitation), traffic prioritization  
and traffic shaping. 
Traffic Policing  
A policer is per flow. The policers meter, mark and rate-limit the traffic according to the dual token 
bucket mechanism (CIR+CBS, EIR+EBS). A special mechanism compensates for Layer 1 headers. Traffic 
can be limited to the line rate or the data rate. 
In addition, Megaplex-4 features unique p-bit re-marking capabilities that assign color-specific p-bit 
values to Ethernet frames at network ingress to ensure metering continuity across the Metro Ethernet 
network. User traffic that was marked “yellow” according to the CIR/EIR parameters by the device QoS 
engine is assigned a new p-bit value to signal its status and priority, so that it is dropped first by 802.1Q 
and 802.1ad (a.k.a IEEE 802.1QinQ ) network elements in the event of congestion. This is especially 
useful in color-blind as well as color-aware networks with no “discard eligible” (“yellow”) marking. 
Traffic Prioritization (Queuing) 
Once traffic is classified to a flow, it can be mapped to Strict (Strict Priority) queues or WFQ (Weighted 
Fair Queues): 
• 
Strict. The data flow set to the highest priority is transmitted first. If this data flow stops, all 
tasks at lower priorities move up by one priority level. For example, the data flow set to the 
second-highest priority is then transmitted at the highest priority. 
• 
WFQ. Allows different scheduling priorities to statistically multiplex data flows with different 
shares on the service. Each data flow has a separate FIFO queue. A link transmitting at a data 
rate R, all non-empty data flows N are served simultaneously according to the assigned share w, 
each at an average rate of R/(w1 + w2 + w3 + … +wN).  If one data flow stops, the remaining data 
flows each receive a larger share w. 
The WRED mechanism ensures that queues are not congested and high-priority traffic is maintained. 
Each queue is assigned a WRED profile for which you can configure the thresholds and probability to suit 
your needs. 
1. Introduction 
Level 1
UNI
Flow1
Flow2
Flow3
Queue
Block 1
Queue
Block 0
Queue Group
3
4
1
2
3
4
1
2
Level 0
3
1
2
1
2
 
Queue Structure – Towards CL.2/A GbE Port 
Level 0 contains up to 8 queue blocks per CL.2/A GbE port. Each block has up to eight queues and its 
own scheduling (Strict and WFQ). For each queue block in level 0, there is a queue in level 1 that 
represents the scheduling between the queue blocks in level 0. Flows can be bound to each queue block 
in level 0. 
1. Introduction 
Level 0
UNI
Flow1
Flow2
Flow3
Queue Group
3
1
2
 
Queue Structure – Towards User Ethernet or VCG Ports  
Level 0 contains a single queue block per Ethernet port. Each block has up to eight queues and its own 
scheduling (Strict and WFQ). Flows can be bound to each queue block in level 0. 
Queue Mapping  
For the network ports (CL.2/A GbE), Megaplex-4 supports up to 8 queue blocks per queue group. 
Towards the user ports, a single queue block with up to eight queues is supported. Flows that are in the 
direction user port to network port can be bound to one of up to 8 queue blocks, and flows that are in 
the direction network port to user port can be bound to one of eight queues. 
The queue mapping functionality associates the user priorities with queue numbers (CoS). 
The queue mapping functionality is bound to each flow.  
Hardware-Based SLA Monitoring and Troubleshooting (Ethernet OAM) and Measurement (Performance 
Monitoring) 
Featuring ultra-fast, hardware-based processing capabilities, Megaplex-4 performs OAM and PM 
measurements in under1 ms with maximum precision. 
Megaplex-4 provides OAM to monitor and troubleshoot an Ethernet network and quickly detect failures: 

## 2.12 Connecting to Alarm Equipment  *(p.74)*


## 2.13 Connecting to SDH/SONET Equipment  *(p.74)*


## 2.14 Connecting to E1 and T1 Equipment  *(p.74)*

1. Introduction 
• 
CFM OAM (End-to-end OAM) based on IEEE 802.1ag and Y.1731 for continuity check, non-
intrusive loopback and link-trace, and performance monitoring 
• 
EFM OAM (Link OAM) according to IEEE 802.3-2005 (formerly IEEE 802.3ah) for remote 
management and fault indication, including discovery, link monitoring, remote fault detection 
(dying gasp) and remote loopback. 
Megaplex-4 offers advanced Ethernet service assurance tools, including user-defined KPI (key 
performance indicators) threshold configuration for delay (latency), delay variation (jitter), packet loss 
and availability. Other tools include real-time SLA violation alerts and per-flow statistics reporting. 
Flexible Ethernet Transport over TDM 
Flexible Ethernet transport options over TDM links provide full support for Ethernet services over 
existing TDM infrastructures with efficient bandwidth utilization for each type of application, and also 
enable cost-effective migration to packet switched transport. The available Ethernet transport options 
include: 
• 
HDLC bundles with selectable number of timeslots over individual external E1 and T1 links, and 
internal PDH ports of the SDH/SONET subsystem  
• 
Wideband, multilink MLPPP bundles over E1 links, with a bandwidth of up to 16.384 Mbps (the 
equivalent of eight E1 links) 
• 
Virtually concatenated groups over SDH/SONET links, with selectable granularity down to VC-
12/VT1.5/VC-3/VC-4/STS-1/STS-3C, Megaplex-4 performs low-order and high-order virtual 
concatenation, including GFP encapsulation per ITU-T Rec. G.7041 or LAPS per ITU-T Rec. 
X.85/X.86. For reliable transmission, Megaplex-4 also supports LCAS per ITU-T Rec. G.7042. 
Flexible TDM Transport over Ethernet  
Megaplex-4 supports TDM pseudowire (PW) circuit emulation for E1 and T1 over IP and MPLS packet-
switched networks. It complies with the pseudowire edge-to edge emulation (PWE3) standards, 
including TDMoPSN, HDLCoPSN, CESoPSN and SAToP. 
Fiber Multiplexing  
Megaplex-4 also features multiport fiber multiplexing modules, for transporting 4 or 16 E1 streams, 
together with Ethernet traffic of up to 100 Mbps, over proprietary fiber optic links to compatible 
standalone units offered by RAD for use at customers’ premises. 

## 2.15 Connecting to Ethernet Equipment  *(p.75)*


## 3.1 Turning On the Unit  *(p.75)*

1. Introduction 
DS0 Cross-Connect  
Megaplex-4 features an internal DS0 cross connect matrix of up to 8384/6080 channels. Traffic from any 
channel can be cross-connected directly to any other channel. 
These capabilities enable Megaplex-4 to function as a service differentiation point at the headquarters, 
handing off traditional voice and data services to the transport network. 
At the remote offices or customer premises, Megaplex-4 may also be deployed to effectively fan out 
multiple voice and data services. 
A special low-cost version of CL.2 modules is supplied without SDH/SONET and GbE ports. This version 
provides an improved price/performance solution for DS0 cross-connect and channel-bank applications 
(see Maximum DS0 Matrix Capacity (DS0 only option) for maximum capacity) and LRS-102 
replacement. It also creates a platform that allows upgrade from a transparent rack to an aggregation 
with GbE & STM-4/OC-12/STM-4/OC-3 solutions by simple replacement of a CL module.  
Protection 
The modular, distributed architecture of Megaplex-4 enables redundancy at different levels of the 
network and provides a resilient system with no single point of failure. Hardware redundancy is 
provided through an optional redundant power supply and CL modules, with switchover to the backup 
CL links within 50 msec.  
Each combined common logic, cross-connect matrix and broadband link module (CL) provide automatic 
switchover between each two STM-1/STM-4/OC-3/OC-12 links within 50 msec, for 1+1 protection 
against hardware, network or cable failure. The SDH/SONET employs APS 1+1 protection against link or 
hardware failure as well as subnetwork connection protection according to ITU-T Rec G.841 (SNCP for 
SDH and UPSR for SONET) for path protection and ring topology. This provides end-to-end service 
protection. 
The CL Ethernet GbE ports employ LAG protection against link or hardware failure. With the CL.2/A 
capabilities, Megaplex-4 supports Ethernet Ring Protection Switching (ERPS) per ITU-T G.8032v1. 
Selected I/O modules can also be configured for redundancy and can be hot-swapped, allowing for 
continuous service. 
For more detailed information about different redundancy types, refer to the following: 
• 
CL –  Common Logic (CL.2) Modules in this chapter 
• 
PS redundancy – Power Supply (PS) Modules in this chapter  
• 
APS – Automatic Protection Switching section in Chapter 7 

## 3.2 Indicators  *(p.76)*


## 3.3 Startup  *(p.76)*


## 3.4 Working with Custom Configuration File  *(p.76)*

1. Introduction 
• 
Path protection – Path Protection for SDH/SONET Payload section in Chapter 7 
• 
I/O module redundancy – TDM Ring Protection, and TDM Group Protection and I/O Group 
Protection sections in Chapter 7  
• 
Ethernet protection – Configuring the LAG section in Chapter 7 
• 
Ethernet group (Logical MAC-based) protection – Ethernet Group Protection section in 
Chapter 7  
• 
Ethernet Ring Protection – Ethernet Ring Protection (ERP) section in Chapter 7 
• 
DS0 SNCP Protection – DS0 SNCP (DS0-Bundle) Protection section in Chapter 7.  
Diversity of Rings 
In addition to supporting standard SDH/SONET and Ethernet rings, Megaplex-4 can be used to create E1, 
T1, TDM over fiber, or a mix of ring topologies. For more detailed information, refer to TDM Ring 
Protection section in Chapter 7. 
Megaplex-4 provides a perfect solution in combining low-rate service provisioning and ring protection. 
Modularity and Flexibility 
Megaplex-4 is available in two basic chassis: 
• 
Megaplex-4100 is a 4U-high chassis providing slots for up to 2 AC or DC power supplies, 2 
common logic and 10 I/O modules.  
• 
Megaplex-4104 is a compact low-cost 2U-high chassis providing slots for up to 2 AC or DC power 
supplies, 2 common logic and 4 I/O modules.  
Both chassis allow for a “pay as you grow” approach and enable CapEx optimization. 
Next-Generation ADM/Terminal 
STM-1/STM-4/OC-3/OC-12 network owners can extend the use of existing ADM equipment or terminal 
multiplexers, saving replacement or expansion costs, by implementing VCAT protocols to carry the 
Ethernet traffic in a more efficient way and minimize wasted bandwidth. 
Megaplex-4 performs STM-1/STM-4/OC-3/OC-12 add/drop multiplexing for grooming LAN and TDM 
traffic over SDH/SONET networks. Ethernet traffic can be mapped into n x VC-12/VC-3/VC-4 or n x 
VT1.5/STS-1/STS-3C virtual containers.  

## 3.5 Configuration and Management  *(p.77)*

1. Introduction 
Megaplex-4 brings Ethernet economics and packet-switching efficiency to existing SDH/ SONET/TDM 
infrastructures. It thereby enables utilities and other private fiber network owners to reduce both Opex 
and Capex as they use their optical bandwidth for reselling revenue generating Ethernet services. New 
business opportunities can be created by leveraging existing equipment to support clear channel data 
streams and the latest high bandwidth services. 
Megaplex-4 eliminates the need for two separate units (ADM and multiplexer) for private networks 
where voice, Ethernet and data services are required.  
Timing  
Flexible timing options enable reliable distribution of timing together with flexible selection of timing 
sources, including external station clock for daisy-chaining the clock signals to other equipment. 
Megaplex-4 also provides traceable timing quality and supports automatic selection of best-quality 
timing reference. 
Megaplex-4 timing is fully redundant, i.e., each CL module has its own timing subsystem, and can supply 
all the clock signals required by the system via the chassis timing bus. However, at each time, only one 
CL module (the active module) actually drives the timing bus, while the other (standby) module is 
disconnected from the bus, but continuously monitors the state of the main module timing subsystem. 
If a problem is detected in the active timing subsystem, the standby subsystem hitlessly takes over.  
The user can define the following clock sources: 
• 
Recovered from the STM-1/STM -4/OC-3/OC-12 interface, including automatic selection, based 
on SSM (Synchronization Status Messaging) 
• 
Recovered from the GbE interface (CL modules only), including automatic selection based on 
ESMC (Ethernet Synchronization Messaging Channel) 
• 
Internal crystal free-running oscillator-based clock 
• 
Derived from the receive clock of a specified module user port 
• 
ACR Adaptive clock recovered from a pseudowire circuit (VS modules with /PW option)  
• 
External station clock. 
Multiple clock sources can be set and assigned corresponding quality and priority. 
Megaplex-4 uses the highest quality stratum available, determined by monitoring the synchronization 
status messages (SSM) of the configured SDH/SONET clock sources. 
For detailed information about the different system timing modes, refer to the following sources: 
• 
Clock Selection in Chapter 9  

## 3.6 Management Access Methods  *(p.78)*


## 3.7 Services for Management Traffic  *(p.78)*

1. Introduction 
• 
Chapters 13 and 14. 
Simple Network Time Protocol  
The Simple Network Time Protocol (SNTP) provides the means of synchronizing all managed elements 
across the network to a clock source provided by NTP servers. Megaplex-4 supports the client side of a 
simple network time protocol (SNTP) v.3 (RFC 1769).  
Management 
Megaplex-4 offers carrier-class service provisioning features, including end-to-end path management, to 
ensure continuous service availability. Advanced SNMP management capabilities provide control and 
monitoring of all network elements: SDH/SONET access and ring units as well as remote POP and Last 
Mile broadband access feeders and CPEs. 
Complete control over the Megaplex-4 functions can be attained via the following applications: 
• 
CLI-driven terminal utility for management via a local ASCII-based terminal connection (see 
Working with Terminal and Terminal Control Port in Chapter 3). Telnet access is supported via 
IP-based connection. 
• 
RADview – RAD’s SNMP-based element management system, providing a dedicated PC/Unix-
based GUI for controlling and monitoring the unit from a network management station. It also 
includes northbound CORBA interface for integration into any third-party NMS (network 
management system). For more information, refer to the RADview User's Manual. 
• 
Shelf View – RAD’s SNMP-based standalone application with fully FCAPS-compliant element 
management. It displays a dynamic graphic representation of the device panel(s), providing an 
intuitive, user-friendly GUI.  
For more information about configuration alternatives, refer to Management Alternatives in Chapter 3. 
The unit can be managed by and report to up to 10 different users simultaneously. Accounts of existing 
and new users can be defined/changed remotely, using a dedicated RADIUS server as explained under 
Authentication via RADIUS Server in Chapter 6. 
A wide range of inband and out-of-band management options provide organizations with the means 
needed to integrate the equipment within the organizational management network, as well as transfer 
their management traffic seamlessly through the Megaplex-4-based network.  
Remote units can be managed in the following ways: 
• 
Out-of-band, using the 10/100 Ethernet management port (for more information, see 
Configuring the Out-Of-Band Management Port in Chapter 5) 

## 3.8 CLI-Based Configuration  *(p.79)*


## 3.9 GUI-Based Configuration  *(p.79)*

1. Introduction 
• 
Inband, using IP/PPP or IP/HDLC over DCC, via the STM-1/STM-4/OC-3/OC-12 links (for more 
information, see SDH/SONET Ports in Chapter 5) 
• 
Inband, using the IP/PPP or IP/FR over a dedicated timeslot in any E1/T1 link (for more 
information, see the description of a relevant port in Chapter 5, for example, Configuring E1 
Ports). 
• 
Inband, via any of the user Ethernet ports, including the CL module GbE ports (see Configuring 
Flows in Chapter 8) 
• 
Via a network management station running RADview, RAD’s SNMP element management 
application.  
Databases and scripts of commonly used commands can be easily created and applied to multiple units 
using command line interface. 
Software upgrades can be downloaded to CL and selected I/O modules. Preset configuration files can be 
downloaded/uploaded to/from Megaplex-4 via TFTP or SFTP. For more information and instructions, 
refer to Chapter 12. 
Syslog  
The syslog protocol is a client/server-type protocol, featuring a standard for forwarding log messages in 
an IP network and supports up to four syslog servers at present. A syslog sender sends a small text 
message of less than 1024 bytes to the syslog receiver. Syslog messages are sent via UDP in cleartext. 
The Syslog server acts as a centralized repository for all elements in the network, providing for a unified 
logging infrastructure, easier troubleshooting and forensics, lower operational risks and costs and higher 
availability and SLA through faster response time. 
Diagnostics  
When a problem occurs, Megaplex-4 offers a set of diagnostic functions that efficiently locate the 
problem (in the Megaplex-4 chassis, one of I/O modules, a connecting cable, or external equipment) and 
rapidly restore full service. 
The diagnostic functions are based on the activation of loopbacks at various ports. These loopbacks 
enable identifying whether a malfunction is caused by Megaplex-4 or by an external system component 
(for example, equipment, cable, or transmission path connected to the Megaplex-4). A detailed 
description of the test and loopback functions is given in Chapter 5, under the corresponding section 
(for example, E1 Ports, T1 Ports). 
Comprehensive diagnostic capabilities include: 
• 
Local and remote loopbacks 

## 3.10 SNMP-Based Network Management  *(p.80)*


## 3.11 Turning Off the Unit  *(p.80)*

1. Introduction 
• 
Real-time alarms to alert the user on fault conditions  
• 
SDH/SONET link monitoring 
• 
Ethernet traffic counters 
• 
Ethernet, E1/T1 and Optical interface status monitoring.  
Alarm Collection and Reporting  
Megaplex-4 continuously monitors critical signals and signal processing functions. If a problem is 
detected, the Megaplex-4 generates time-stamped alarm messages. The time stamp is provided by an 
internal real-time clock.  
For continuous system monitoring, the user can monitor alarm messages through the supervisory port. 
Alarm messages can also be automatically sent as traps to user-specified network management stations. 
The alarms can be read on-line by the network administrator using a Telnet host, an SNMP-based network 
management station, or a supervision terminal.  
Note 
Megaplex-4 can also monitor one external sense input, and will report its 
activation as any other internally-detected alarm.  
In addition to the alarm collection and reporting facility, the Megaplex-4 has two alarm relays with 
floating change-over contacts: one relay for indicating the presence of major alarms and the other for 
minor alarms. Each relay changes state whenever the first alarm is detected, and returns to its normal 
state when all the alarms of the corresponding severity disappear. The relay contacts can be used to 
report internal system alarms to outside indicators, e.g., lights, buzzers, bells, etc., located on an alarm 
bay or remote monitoring panel. 
Performance Monitoring 
Megaplex-4 collects statistics per physical port and per connection for 15-minute intervals, which 
enables the network operator to monitor the transmission performance and thus the quality of service 
provided to users, as well as identify transmission problems. Performance parameters for all the active 
entities are continuously collected during equipment operation.  
Statistics for the last 24 hours are stored in the device and can be retrieved by the network management 
station. For additional information, refer to the Statistics section for the relevant port (for example 
Viewing Ethernet Port Statistics under Ethernet Ports in Chapter 5). 
Megaplex-4 maintains a cyclic event log file that stores up to 256 time-stamped events. In addition, an 
internal system log agent can send all reported events to a centralized repository or remote server. For 
additional information, refer to Handling Events in Chapter 11. 

## 4.1 Service Elements  *(p.81)*


## 4.2 Services Provided by Megaplex-4  *(p.81)*

1. Introduction 
RADview Performance Management   
Megaplex-4 maintains performance management (PM) statistics for selected entities in the device. The 
PM statistics are collected into a file periodically, for display in the RADview PM portal (refer to the 
RADview System User’s Manual for further details on the PM portal). The PM collection process can be 
globally enabled or disabled for the entire device. In addition, the statistics collection can be enabled for 
all entities of a specific type, or for specific entities. 
Security 
User access to Megaplex-4 is restricted via user name and password. For more information, refer to 
Management Access Methods in Chapter 3. 
Telnet-like management can be secured using a Secure Shell (SSH) client/server program. Instead of 
sending plain-text ASCII-based commands and login requests over the network, SSH provides a secure 
communication channel. 
SFTP (Secure File Transfer Protocol, also known as SSH File Transfer Protocol) is supported, to provide 
secure (encrypted) file transfer using SSHv2. 
In addition, Megaplex-4 supports SNMP version 3, providing secure access to the device by 
authenticating and encrypting packets transmitted over the network. For more information, refer to The 
SNMPv3 Mechanism in Chapter 6. 
The RADIUS protocol allows centralized authentication and access control, avoiding the need of 
maintaining a local user database on each device on the network. For more information, refer to 
Authentication via RADIUS Server Mechanism in Chapter 6. 
1.2 New in this Version  
The following new functionalities have been added in version 4.91:  
• 
New VS-8/E&M module – New option for the VS voice module with 8 E&M voice ports  
• 
ERP over LAG – G.8032 ring over GBE links now also protected with LAG   
• 
Enhanced redundancy for M-ETH – Improved recovery time upon CL HW failure   
• 
Configurable MTU for management data channel – Management router MTU configuration is 
no longer hard-coded to 200 bytes. It can be now configured in the range of 1260 to 1500 bytes 
or set to 200 bytes 
   
1. Introduction 
1.3 Physical Description 
System Structure 
Megaplex-4 units use modular chassis. The chassis has physical slots in which modules are installed by 
the user to obtain the desired equipment configuration.  
Megaplex-4 configuration includes the following main subsystems: 
• 
I/O subsystem, provides interfaces to the user’s equipment. The number of user interfacing 
modules that can be installed in a chassis is up to 10 for Megaplex-4100 and 4 for Megaplex-
4104 
• 
Multiplexing, timing and control subsystem, located on the common logic and cross-connect 
(CL.2) modules.  
• 
Power supply subsystem, located on the power supply (PS) modules 
• 
Chassis. The main function of the chassis is to provide interconnections between the various 
modules, and in particular to connect between the user interfacing (I/O) modules, and the CL 
modules that provide the multiplexing function and the optional connections to SDH/SONET 
and/or Ethernet networks.  
CL and PS modules are always installed in their dedicated chassis slots, whereas the user interfacing 
modules can be installed in any of the other chassis slots (called I/O slots). 
Any operational Megaplex-4 system must include at least one CL module and one PS module. These 
modules are thus referred to as system modules. User interfacing modules, called I/O modules, are 
added to this basic configuration.  
Megaplex-4 system modules are critical components, because a failure in any one of these modules 
could disable the whole system, whereas a failure in an I/O module affects only a small part of the 
system, and can be generally overcome by using alternate routes, putting unused capacity into service, 
etc. Therefore, in most applications Megaplex-4 units should be equipped with an additional redundant 
system module of each type. Redundancy is also available for the network interfacing subsystems. 
The Megaplex-4 system is designed to automatically put a redundant module or subsystem in service in 
case the corresponding system component fails, thereby ensuring continuous system operation in the 
event of any single module failure. Moreover, redundant modules may be inserted or removed even 
while the system operates. 

## 4.3 E1/T1 Traffic to SDH/SONET via Direct Transparent Mapping (1a)  *(p.83)*

1. Introduction 
Description of Megaplex-4100 Chassis 
The figure below shows a general view of a regular Megaplex-4100 chassis.  
Megaplex-4100 is built in a 4U-high chassis that is intended for installation in 19” and 23” racks, using 
brackets attached to the sides of the chassis, near the front or rear panel. Thus, a Megaplex-4100 can be 
installed in accordance with the specific requirements of each site, either with the Megaplex-4100 front 
panel toward the front of the rack (per ANSI practice), or with the module panels toward the front (per 
ETSI practice).  
System status indicators are located on both the front panels and on the CL module panels. Additional 
indicators are located on the module panels. The cable connections are made directly to the module 
panels. 
 
Typical Megaplex-4100 Chassis, General View 
Rear View 
The figure below shows a typical rear panel of the Megaplex-4100 chassis and identifies the slots and 
their use. The chassis has 14 slots:  
• 
Two slots are reserved for power supply (PS) modules 
• 
Two slots are reserved for CL modules  
• 
The other 10 slots, arranged in two groups of 5 each, are intended for I/O modules. Each I/O slot 
can accept any type of I/O module.  
Note the labels which designate the type of module that can be installed in each slot:  

## 4.4 Shared E-LAN Service with Multiple Drops per Node over SDH/SONET (3)  *(p.84)*

1. Introduction 
• 
Slots labeled PS-A and PS-B (identified as ps-a and ps-b on supervision terminal screens): power 
supply modules 
• 
Slots labeled I/O-1 to I/O-10 (identified as slot 1 to slot 10 on supervision terminal screens): I/O 
modules 
• 
Slots labeled CLX-A and CLX-B (identified as cl-a and cl-b on supervision terminal screens): CL 
modules. 
In addition, each slot is keyed, therefore it is not possible to install a wrong module type. 
Caution 
To prevent physical damage to the electronic components assembled on the 
two sides of the module printed circuit boards (PCB) while it is inserted into 
its chassis slot, support the module while sliding it into position and make 
sure that its components do not touch the chassis structure, nor other 
modules.  
Slot
PS-A
PS-B
IO-1
IO-2
IO-4
IO-5
IO-3
CL-A
CL-B
IO-6
IO-7
IO-8
IO-9
IO-10
PS Slots
I/O Slots
I/O Slots
CL Slots
PS-A
PS-B
I/O 1
I/O 2
I/O 3
I/O 4
I/O 5
CL-A
CL-B
I/O 6
I/O 7
I/O 8
I/O 9
I/O 10
P S/D C
P S/D C
ON
LI NE
C L-2
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LI NK
AC T
E
T
H
C
L
O
C
K
ON LI NE
ALM
ON /LOS
LI NK
AC T
G
b
E
LOS
S
D
H
/
S
O
N
E
T
1
2
1
2
L A S E R
C L A S S
1
ON
LI NE
C L-2
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LI NK
AC T
E
T
H
C
L
O
C
K
ON LI NE
ALM
ON /LOS
LI NK
AC T
G
b
E
LOS
S
D
H
/
S
O
N
E
T
1
2
1
2
L A S E R
C L A S S
1
LOC
CH-1
REM
LOC
CH-2
REM
LOC
CH-3
REM
LOC
CH-4
REM
LOC
CH-5
REM
LOC
CH-6
REM
LOC
CH-7
REM
LOC
CH-8
REM
CH-1
CH-2
CH-3
CH-4
E
M
E
M
E
M
E
M
M 8E1
STAT US
1
2
3
4
6
8
5
7
L
I
N
K
LI NK
1-8
AC T
LI NK
E
T
H
1
AC T
LI NK
E
T
H
2
AC T
LI NK
E
T
H
3
LI NK
A CT
ET H1
ET H2
L A S E R
C L A S S
1
E
T
H
1
E
T
H
2
E
T
H
3
LI NK /
A CT
LO SS
L A S E R
C L A S S
1
A
E
T
H
A IS
L
I
N
K LO SS
B
A IS
100
A CT
L A S E R
C L A S S
1
S
H
D
S
L
.
b
I
s
E
T
H
LI NK
1
2
A CT
O
P
B
LO SS
1
2
LI NK /
A CT
E
T
H
100
3
4
O
P
A
L
I
N
K
LASER
CLASS
1
O
P
A
O
P
B
M 8E1
STAT US
1
2
3
4
6
8
5
7
L
I
N
K
LI NK
1-8
L A S E R
C L A S S
1
Tx
R x
AC T
LI NK
E
T
H
1
Tx
R x
AC T
LI NK
E
T
H
2
Tx
R x
AC T
LI NK
E
T
H
3
+72V
-48V
P S/A C
VD C-I N
100-120VA C
RT N
200-240VA C
ON
-
+
72V
+
-
48V
P S/D C
ON
VD C-I N
 
Megaplex-4100 Chassis, Typical Rear View  
Front Panel 
The front panel of the Megaplex-4100 chassis is shown in beflow. For description of LED indicators, see 
Chapter 3. 
1. Introduction 
MEGAPLEX-4100
POWER SUPPLY
B
A
SYSTEM
ALARM
TEST
 
Megaplex-4100 Chassis, Front Panel 
Description of IEEE-1613 compliant Megaplex-4100 Chassis 
A special IEEE-1613 compliant chassis includes a heat sink on the front panel and two special fixtures 
replacing the vertical walls of the CL module slots, to allow more airflow into the CL modules. These 
fixtures use I/O 5 and I/O 6 slots, on both sides of CL modules. 
The figures below show a general view of an IEEE-1613 compliant Megaplex-4100 chassis. The chassis is 
intended for installation in 19” rack, using brackets attached to the sides of the chassis, near the front or 
rear panel.   
 
1. Introduction 
 
IEEE-1613 Compliant Megaplex-4100 Chassis, Rear View  
 
IEEE-1613 Compliant Megaplex-4100 Chassis, Front View 
1. Introduction 
Rear View 
The figure below shows a typical rear panel of the Megaplex-4100 IEEE-1613 compliant chassis and 
identifies the slots and their use. The chassis has 14 slots:  
• 
Two slots are reserved for power supply (PS) modules (special ordering options) 
• 
Two slots are reserved for CL modules (special ordering options) 
• 
8 slots, arranged in two groups of 4 each (I/O 1,2,3,4 and I/O 7,8,9,10), are intended for I/O 
modules. Each I/O slot can accept any type of I/O module 
• 
I/O slots 5 and 6 are reserved for accommodation of CL module cooling fixtures.  
Each slot is keyed, therefore it is not possible to install a wrong module type. 
Caution 
To prevent physical damage to the electronic components assembled on the 
two sides of the module printed circuit boards (PCB) while it is inserted into 
its chassis slot, support the module while sliding it into position and make 
sure that its components do not touch the chassis structure, nor other 
modules.  
 
 
IEEE-1613 Compliant Megaplex-4100 Chassis, Rear View  
1. Introduction 
Front Panel 
The front panel of the IEEE-1613 Compliant Megaplex-4100 chassis is shown above. For description of 
LED indicators, see Chapter 3. 
 
IEEE-1613 Compliant Megaplex-4100 Chassis, Front Panel  
Description of Megaplex-4104 Chassis  
The figure below shows a general view of the Megaplex-4104 chassis. 
 
Megaplex-4104 Chassis  
The chassis has 8 slots:  
• 
Two slots are reserved for power supply (PS) modules 
• 
Two slots are reserved for CL modules  
1. Introduction 
• 
The other 4 slots are intended for I/O modules. Each I/O slot can accept any type of I/O module.  
The Megaplex-4104 chassis is supplied with brackets for installation in racks. The brackets are attached to 
the sides of the chassis, as explained in Chapter 2.  
The figure below shows a typical front view of the Megaplex-4104 chassis equipped with two CL.2/4104 
modules, and identifies the slots and their use.  
 
Megaplex-4104 Chassis, Front View  
The rear panel of the Megaplex-4104 chassis is shown below. For description of LED indicators, see 
Chapter 3. 
 
Megaplex-4104 Chassis, Rear Panel 
I/O Modules  
The table below lists the I/O modules currently offered for the Megaplex-4 in the alphabetical order of 
their names. Contact RAD Marketing for information on additional modules that may be available for 
your specific application requirements. 
1. Introduction 
Megaplex-4 I/O Modules  
 
 
Module  
Description 
M-ETH 
Module with 8 GbE interfaces supporting optical or electrical media and providing 9 
Gbps switching capacity (up to 1 Gbps capacity to the CL.2 module and 8 Gbps shared 
among its 8 external ports). The capacity can be allocated among the 8 interfaces with 
a granularity of 100 Kbps. 
T3 
Single-port multiplexer module, providing access to standard T3 equipment over 
unbalanced copper lines with full duplex data rates of 44.7 Mbps.   
TP (Tele-
protection) 
Command In/Out teleprotection module with four selectable voltage inputs and eight 
outputs, secured and reliable end-to-end commands transmission. 
VC-16, 
VC-8, 
VC-4, 
VC-8A, 
VC-4A 
 
Analog voice modules VC-16, VC-8 and VC-4 provide 16, 8 or 4 PCM-encoded 
toll-quality voice channels.  
The modules are available in three models: 
• E&M: 4-wire or 2-wire interfaces with E&M signaling per RS-464 Types I, II, III and V, 
and BT SSDC5  
• FXS: 2-wire interfaces for direct connection to telephone sets 
• FXO: 2-wire interfaces for direct connection to PBX extension lines. 
VC-8A and VC-4A are similar to VC-8 and VC-4 modules, except that they also support 
ADPCM. 
VS Modules 
 
Multiservice versatile module with broad variety of services available in a single 
module:  
• VS-12: 12 serial data ports  
• VS-6/BIN: 6 serial data ports, 8 in/out binary command ports and 1 Ethernet port. 
• VS-6/C37: 6-port serial module with 2 fiber optic C37.94 ports  
• VS-6/703: 6-port serial module with 2 64-kbps G.703 codirectional interfaces 
 
• FXS/E&M: Voice module with 4 E&M ports and 8 FXS ports 
• VS-8/E&M: Voice module with 8 E&M ports  
• VS-6/E&M: 6-port serial module with 4 E&M voice ports  
• VS-6/FXO: 6-port serial module with 8 FXO voice ports  
• VS-6/FXS: 6-port serial module with 8 FXS voice ports  
• VS-16E1T1-EoP 16-port E1/T1 module with EoP support 
• VS-16E1T1-PW: 16-port E1/T1 module with pseudowire support  
• VS-6/E1T1: 6 serial data ports, 8 E1/T1 ports  
• VS-OCU/E&M: 2 OCU-DP – DDS ports, 4 E&M ports  
1. Introduction 
 
Common Logic (CL.2) Modules  
The Common Logic (CL.2) module controls the Megaplex operation and is the interface for its 
configuration and management.  
CL.2 houses the TDM and Packet processing engines, as well as the GbE and SDH/SONET uplinks. 
For direct connection to the SDH/SONET network, CL.2 features two standard network ports with a 
software-configurable STM-1/STM-4 or OC-3/OC-12 interface. The dual ports on the CL.2 module can be 
used either for operation in parallel or for redundancy. 
For direct connection to packet-based networks, CL.2 has two UTP or SFP-based GbE ports. The UTP 
interface features autonegotiaton speed detection capabilities.   
Megaplex-4 allows the installation of two CL.2 modules of the same type, to ensure continuous 
operation when one module is reset, restarted, or stops operating for any reason. In such a case, the 
redundant main module immediately takes over the unit, using its own pre-configured settings. The 
switch-over to the protecting module occurs automatically upon detection of failure in the active 
module, or upon removing the active module from the chassis. The SDH/SONET and/or Ethernet traffic 
subsystems located on the CL modules operate independently of the management subsystems. For 
instructions on extracting and inserting a CL module, refer to Removing/Installing the CL Module in 
Chapter 2. 
Power Supply (PS) Modules 
PS Modules  
Two PS modules can be installed in the chassis. Only one PS module is required to provide power to a 
fully equipped Megaplex-4; installing a second module provides redundancy. While both modules 
operate normally, they share the load; in case one fails or does not receive power, the other module 
continues to provide power alone. Switch-over is automatic and does not disturb normal operation. For 
instructions on extracting and inserting a power supply, refer to Removing/Installing the PS Module  in 
Chapter 2.  
PS modules for Megaplex-4100 and Megaplex-4104 have different shape and technical 
characteristics. -48 VDC nominal DC power supplies are available for both chassis. In addition, 
Megaplex-4100 can be ordered with AC (115 or 230 VAC nominal) power supply modules. For the full list 
1. Introduction 
of module options for the Megaplex-4100 and Megaplex-4104 chassis, see Power Supplies table in 
Technical Specification section.   
1.4 Functional Description 
Megaplex-4 Architecture 
Megaplex-4 unique dual star topology architecture connects the common logic processing engines to 
any of the 10 I/O slots independently. In addition each of the I/O slots is connected by a TDM path, as 
well as an Ethernet path, allowing true native TDM and Ethernet traffic handling with minimal 
encapsulation delays, no overhead and dual TDM-Ethernet mode modules. 
 
Common Logic
GbE
GbE
STM-n/OC-n
I/O
Ethernet
Interface
STM-n/OC-n
Ethernet
Interface
TDM
Interface
TDM
Interface
I/O
Ethernet
Interface
Ethernet
Interface
TDM
Interface
TDM
Interface
I/O
Ethernet
Interface
Ethernet
Interface
TDM
Interface
TDM
Interface
Each I/O Module has an
Independent “Traffic Highway”
10/4 x I/O
Packet
Engine
Ethernet
Interface
Ethernet
Interface
Ethernet
Interface
TDM
Interface
TDM
Engine
TDM
Interface
TDM
Interface
Dual Star
Topology Connection
 
Megaplex-4 Internal Architecture 
The Megaplex-4 architecture includes the following main subsystems: 
1. Introduction 
• 
I/O subsystem: provides interfaces to the user’s equipment. For description, see I/O Modules 
section below. 
• 
TDM engine:  
 
DS0 cross-connect matrix: handles the TDM traffic. The matrix also handles the signaling 
information associated with TDM traffic. 
 
DS1 cross-connect matrix: provides direct timing-independent cross-connect of E1/T1 
streams directly to any selected VC-12/VT1.5.  
 
PDH mapper and framer: handle the TDM traffic directed to the network, and enable 
mapping any E1/T1 port to any VC-12/VT1.5, respectively. 
• 
SDH/SONET engine: includes the circuits needed to interface to an SDH/SONET network: 
 
Low-order/high-order (LO/HO) cross-connect matrix: controls the routing of VCs/VTs at all 
the levels among the PDH mapper, and the SDH/SONET links. Also provides automatic 
protection switching (APS) for the network links, and path protection.  
 
SDH/SONET interfaces: provide the physical interfaces for the SDH/SONET links. 
• 
Ethernet (packet) engine: includes the circuits needed to interface to a packet-switched 
network. The Ethernet traffic handling subsystem includes: 
 
Packet processor: controls the forwarding of Ethernet traffic within the Megaplex-4 
(including forwarding from internal ports, Ethernet-over-TDM and virtually concatenated 
groups) to external Ethernet ports as well as carrier Ethernet functionality (traffic-
management, OAM&P) and carrier grade capabilities (G.8032v1 ERPS) when using the 
CL.2/A assembly  
 
HO/LO mapper and VCAT engine: handle the Ethernet traffic directed for transport over the 
SDH/SONET network by means of virtually concatenated groups, with optional LCAS support 
(per ITU-T Rec. G.7042).  
 
GbE interfaces: provide the physical interfaces for the packet switched network links. 
• 
Timing subsystem: provides timing signals to all the Megaplex-4 circuits, and external (station) 
clock interfaces. For redundancy, two independent subsystems, each located in a CL module, are 
used. For more information, see Clock Selection in Chapter 9. 
• 
Management subsystem: controls Megaplex-4 operation, stores its software and configuration, 
and provides interfaces for local and remote management, and for alarm reporting. The 
management subsystem is also redundant: two independent subsystems, each located in a CL 
module, are used. For more information, see Management Access Methods in Chapter 3, 
Management Bridge and Management Router in Chapter 8, as well as Chapter 12, Software 
Upgrade.  
• 
Power supply subsystem: includes power supply modules that provide power to the internal 
circuits, and an interface for external line feed. For redundancy, two power supply modules can 
1. Introduction 
be installed in the chassis. For more information, see Power Supply (PS) Modules in this chapter 
and Installing PS Modules in Chapter 2. 
The following figure illustrates the position and the contents of the TDM, SDH/SONET and Packet 
engines in the Megaplex-4 Data Flow Block Diagram.  
 
SDH/SONET 
Engine
Packet Engine
TDM Engine
HO/LO 
and VCAT
Mapper
VCAT
Engine
Packet
Processor
ETH
GbE Ports
E1/T1
Mapper
E1/T1
Framer
DS1
Cross-Connect 
Matrix
DS0
SDH/SONET Ports
SDH/SONET 
Framers and 
HO/LO VC/VT
Cross-Connect 
Matrix
DS1
DS0
Cross-Connect 
Matrix
 
Data Flow Block Diagram  
TDM Engine 
TDM traffic can be switched between any of the following entities on the specific level: 
• 
DS0 (analog and digital interfaces: voice, serial, framed E1/T1, E1/T1 over PW, E1/T1 coming 
from VC-12/VT1.5)  
• 
SDH/SONET (high and low level cross connect between SDH/SONET ports).  
The cross-connect level can be selected to DS1 or DS0 operation mode per port. 
1. Introduction 
DS0 Cross-Connect Matrix  
The DS0 cross-connect matrix located on CL modules provides fully non-blocking 1/0 cross-connect 
among I/O modules and PDH ports of the CL.2 modules. This matrix operates in coordination with the 
cross-connect matrices located on most types of I/O modules. 
The DS0 cross-connect matrix provides full control over the routing of individual timeslots. This is 
needed for handling the payload of E1 ports with G.704 framing, T1 ports with SF or ESF framing, and for 
the inband management timeslot. The traffic associated with sub-E1 ports (such as ISDN, voice or serial 
interfaces} is always handled in the DS0 mode. Accordingly, Megaplex-4 distinguishes among three main 
types of payload per timeslot:  
• 
Voice: timeslots carrying PCM-encoded payload.  
Channel-associated signaling (CAS) information is always associated with voice timeslots, and 
therefore it must also be converted when cross-connecting timeslots from ports using different 
standards. 
• 
Data: data timeslots are transparently transferred from port to port. In general, it is assumed 
that no CAS is associated with data timeslots.  
• 
Management: one timeslot can be assigned in any E1 or T1 port to carry inband management 
traffic to the end user’s equipment. Such timeslots are always directed to the CL management 
subsystem, for processing. 
The flow of payload carried by data and voice timeslots is normally bidirectional (full duplex connection). 
However, for individual timeslots, it is also possible to define unidirectional flows, called unidirectional 
broadcasts, from one source (a timeslot of a source port) to multiple destinations (each destination 
being a selected timeslot of another port). For more information, see the Unidirectional Broadcast 
Function section under Cross-Connections in Chapter 8. 
DS1 Cross-Connect Matrix  
The DS1 cross-connect matrix provides direct timing-independent cross-connect of E1/T1 streams 
directly to any selected VC-12/VT1.5. The E1/T1 traffic from VS modules can be mapped directly to 
SONET/SDH without passing the DS0 matrix, thus maintaining independent timing of the E1/T1 links. 
When using the DS1 cross-connect for Megaplex-4100, up to 160 E1/T1 links can be added and dropped 
at each node when connected over STM-4/OC-12. The DS1 cross-connect matrix has a capacity of 160 × 
DS1 for the I/O side. On the CL.2 side, the matrix capacity is 252 × VC-12/VT1.5 per Megaplex-4 node.  
The 252 x VC/VT is the total budget of cross-connected LO (VC-12/VC-3/VT1.5) and HO (VC-4/STS-1) 
containers.  

## 4.11 Voice to T3 via DS0 CrossConnect (9)  *(p.96)*

1. Introduction 
E1/T1 Framers and Mappers 
The TDM payload directed to the network is structured by the DS0 cross-connect matrix and applied to 
the E1/T1 framers. Each framer behaves as a logical E1/T1 port, with user-selectable framing: each CL.2 
module can have up to 63 E1 ports, or up to 84 T1 ports, in accordance with the SDH/SONET framing 
mode.  
The operation mode of each framer can be configured by the user:  
• 
For SDH network interfaces, E1 ports are supported 
• 
For SONET network interfaces, T1 ports are supported. 
The frame type is also selectable, separately for each port: 
• 
For E1 ports, either basic G.704 framing (identified as G732N) or G.704 multiframe (G.732S) can 
be selected.  
• 
For T1 ports, the selections are SF (D4) and ESF. 
Each framer adds the appropriate overhead and creates the frame structure. The data stream provided 
by each framer is applied to the E1/T1 mappers: 
• 
For E1 ports, the mapper enables mapping the port data stream to any of the 63/252 VC-12 in 
the STM-1/STM-4 signal.  
• 
For T1 ports, the mapper enables mapping the port data stream to any of the 84/336 VT1.5 in 
the OC-3/OC-12 signal.  
SDH/SONET Engine  
The SDH/SONET engine includes the following parts:  
• 
Network port interfaces 
• 
SDH/SONET framers and high-order (HO – STS-1/VC-4) cross-connect matrix. 
The SDH/SONET subsystem is integrated with the Ethernet over SDH/SONET engine. 
SDH/SONET Network Port Interfaces 
Each CL.2 module has two STM-1/OC-3/STM-4/OC-12 ports. The ports can be ordered either with the 
following interfaces: 
• 
STM-1/OC-3:155.52 Mbps ±4.6 ppm 

## 4.12 Ethernet Traffic over PDH to SDH/SONET (10a)  *(p.97)*

1. Introduction 
• 
STM-4/OC-12: 622.08 Mbps ±4.6 ppm. 
Each port has an SFP socket that provides the physical interface. For more information, see SDH/SONET 
Ports in Chapter 5.  
SDH/SONET Framer and LO/HO Cross-Connect Matrix 
The SDH/SONET framer subsystem provides the frame assembly/disassembly services and SDH/SONET 
overhead processing for the link to the network. The framer operating modes (SDH or SONET, STM-
1/OC-3 or STM-4/OC-12) are selected by software configuration.  
The low-order/high-order (LO/HO) cross-connect matrix controls the routing of VCs/VTs at all the levels 
between the E1/T1 mapper, VCAT mapper, and the SDH/SONET links. It also provides automatic 
protection switching (APS) for the network links, and path protection.  
The LO part supports low-order cross-connections (VC-12 and VC-3 for SDH links, VT1.5 for SONET links), 
while the HO part enables the routing of the high-order payload (VC-4 for SDH links and STS-1 for SONET 
links) in the SDH/SONET mode. 
Packet Engine 
The Packet (Ethernet) Engine is a state-of-the-art, multi-port GbE switching and aggregating block, which 
enables hardware-based Ethernet capabilities, such as traffic management and performance 
monitoring, between any of the Ethernet entities.  
This Ethernet flow-based traffic can be terminated by any of the following entities: 
• 
Fast Ethernet and GbE ports located on I/O modules 
• 
Internal Ethernet ports of I/O modules carrying traffic generated by CPE devices and transferred 
over E1/T1 circuits  
• 
Two Gigabit Ethernet ports located on CL.2 modules 
• 
SDH/SONET ports by using Virtual or Contiguous concatenation (up to 32 VCG per CL.2) with GFP 
or LAPS and optional LCAS support.  
The Ethernet engine flow classification mechanism is based on port (unaware mode) or VLAN (aware 
mode with pop/push or preserve capabilities).  

## 4.13 Ethernet Traffic over PDH to E1/T1 (10b)  *(p.98)*

1. Introduction 
Packet Processor  
The GbE packet processor is a high-capacity Ethernet processor with classifier, capable of 
handling a wide range of VLAN and port-based flows.  
The processor includes GbE and Fast Ethernet ports, which are used as follows: 
• 
Two external GbE ports, one connected to the GbE 1 interface and the other to the GbE 2 
interface. The two ports can be configured to operate as a redundancy pair, using hardware-
based path and link failure for rapid switching to the backup link. 
• 
Fast Ethernet ports are used for Ethernet traffic from I/O modules, one from each I/O slot. 
• 
Two GbE ports are internally connected to the Ethernet processor of the other CL module 
installed in the Megaplex-4. 
• 
8 GbE ports on the dedicated M-ETH module, with 1 GbE uplink to the CL.2 modules, supporting 
VLAN-aware bridging inside the module between all its ports  
• 
Each Ethernet port is supported by an independent MAC controller that performs all the 
functions required by the IEEE 802.3 protocol. The maximum frame size supported by the basic 
Ethernet switch is 9600 bytes. For maximum frame sizes supported by different I/O modules, 
see Configuring User Ethernet Ports in Chapter 5.  
• 
The frames passed by the MAC controllers are analyzed by the ingress rate policy controller of 
the corresponding port before being transferred, through the switch fabric, to an internal port 
controller, which controls the frame egress priorities and inserts them in separate queues. The 
switch supports up to four transmission classes (queues) for the Fast Ethernet ports, and up to 8 
transmission classes for the GbE ports. The queues are connected to the ports through port 
egress policy controllers. This approach provides full control over traffic flow, and ensures that 
congestion at one port does not affect other ports.  
Note 
In the Megaplex equipped with CL.2/A assembly, the queue mapping 
functionality associates the user priorities with queue numbers (CoS) and the 
marking functionality maps the user priority to the SP priority, according to 
p-bit/DSCP/IP precedence. In the Megaplex with regular CL.2 module, queue 
mapping is fixed and based on p-bit. 
The available number of queues depends on flow classification and flow 
editing (for details, see Chapter 8).  
• 
The processor includes a flow classification engine categorizing packets into flows in accordance 
with user-defined classification rules. Classification takes place at full wire speed. The processor 
recognizes standard frame types.  

## 5.1 Cards  *(p.99)*

1. Introduction 
In addition to the Ethernet traffic handling subsystem components located on the CL.2 modules, 
I/O modules with Ethernet ports (M-ETH) also include a local Ethernet handling subsystem. This 
subsystem includes: 
 
Ethernet port interfaces: provide 10/100/1000 Mbps physical interfaces for external 
Ethernet links.  
 
Layer 2 Ethernet switch: provides the local Ethernet VLAN classification.  
 
GbE (data ports 
Carrier Ethernet (CL.2/A Assembly)  
In addition to the basic functionality described above, the CL.2/A assembly provides carrier Ethernet 
capabilities, such as Ethernet traffic management (TM), standards-based Ethernet Operations, 
Administration and Maintenance and Performance Monitoring (OAM&P), as well as carrier grade 
Ethernet functionality. 
These functionalities are available on any MAC entity, such as the CL module GbE ports, VCG, Ethernet 
module (M-ETH) ports, etc.  
The figures below show the data flow in the device equipped with CL.2/A for the CL.2 GbE ports and 
other ports supporting hierarchical scheduling, respectively. The table below provides an overview of 
the traffic handling stages.  
1. Introduction 
 
 
Data Flow in the Megaplex equipped with CL.2/A – CL.2 GbE ports 
 
Data Flow in the Megaplex equipped with CL.2/A – other MAC Ports  
 
1. Introduction 
Traffic Handling Stages  
Processing Stage 
Relevant 
Profiles 
Applied to 
Description 
L2CP processing 
L2CP 
Port, flow 
Defines actions for L2CP processing (discard, peer, 
tunnel) 
Classification  
Classifier 
Flow  
Classifying traffic such as email traffic, content 
streaming, large document transmission, etc.  
Policing 
Policer 
Flow 
Policing the traffic within the flow (CIR, CBS, EIR and 
EBS parameters) 
Mapping of flow to 
queue 
CoS 
mapping 
Flow 
Dividing the services using a 3-bit field, specifying a 
priority value between 0 (signifying best-effort) and 
7 (signifying highest priority) 
Defines method and values for mapping packet 
attributes (P-bit, DSCP, IP-Precedence) to internal 
CoS Values 
Scheduling 
(between CoS) 
 
 
‘Storing’ data that is transmitted according to the 
CoS level specified  
Scheduling and ‘regulating’ traffic 
 
WRED 
Queue 
Defines green and yellow packet thresholds and 
drop probabilities 
 
Queue 
Queue 
block 
Defines queue type with shaper and WRED profile 
 
Queue 
block 
Queue 
block 
within 
queue 
group 
Defines queue block parameters (queues, 
scheduling scheme, weights) 
 
Queue 
group 
Port 
Defines level-1, -2 and -3 scheduling  elements and 
structures within queue group 
Shaping 
Shaper 
Queue, 
queue 
block 
Ensuring that traffic is shaped to the desired rate 
(CIR, CBS Parameter) 
Scheduling 
(between EvC) (GbE 
ports only) 
 
 
‘Storing’ data that is transmitted according to the 
CoS level specified  
Scheduling and ‘regulating’ traffic 

## 5.2 Port-Related Profiles  *(p.102)*


## 5.3 Binary Command Ports  *(p.102)*

1. Introduction 
Processing Stage 
Relevant 
Profiles 
Applied to 
Description 
 
WRED 
Queue 
Defines green and yellow packet thresholds and 
drop probabilities 
 
Queue 
Queue 
block 
Defines queue type with shaper and WRED profile 
 
Queue 
block 
Queue 
block 
within 
queue 
group 
Defines queue block parameters (queues, 
scheduling scheme, weights) 
 
Queue 
group 
Port 
Defines level-1, -2 and -3 scheduling  elements and 
structures within queue group 
 
 
VLAN 
Editing  
Performing VLAN manipulations, such as push s-tag, 
pop, mark, and more, as well as marking the p-bit 
on the outer VLAN header (per packet attribute or 
internal CoS). 
Editing and Marking 
Marking 
Flow 
Adding or removing VLAN IDs, as well as marking 
the priority on the outer VLAN header (defines 
method of mapping CoS and packet color values 
into P-bit) 
VCAT Engine  
The VCAT Engine handles all the functions related to the use of virtual concatenation, and the 
preparation of Ethernet traffic for efficient transport over the SDH/SONET network. 
The Ethernet mapper subsystem includes the following functions: 
• 
LAPS encapsulation  
• 
GFP encapsulation  
• 
Virtually concatenated group mapper. 
HO/LO Mapper  
The HO/LO mapper maps the Ethernet traffic for transmission over the SDH/SONET network, and 
creates the virtually concatenated groups (VCGs) that enable the user to control the utilization of the 
bandwidth available on the link to the SDH/SONET network.  

## 5.4 Control Port  *(p.103)*


## 5.5 DS0-Bundle Ports  *(p.103)*

1. Introduction 
The routing of the VCG payload is defined by means of cross-connections, which means selection of 
specific VCs/VTs to be used to carry each VCG, in the number needed to provide the required 
bandwidth. This operation creates the trails that are needed to connect the local users to remote 
locations through the SDH/SONET network. 
Ethernet over SDH/SONET, Full/Channelized T3, E1/T1 - General Concept  
To describe and map the Ethernet traffic passing over different media (E1/T1, SDH/SONET, T3 etc), the 
Megaplex-4 architecture uses a concept of Logical MAC ports. Logical MAC represents the Ethernet part 
of the entity. It should be bound to a gfp, hdlc or mlppp port, which, in its turn, should be bound to the 
physical layer.  
The meaning of the gfp, hdlc or mlppp ports and their further mapping depends on the Ethernet traffic 
media: 
• 
GFP ports exist on CL.2, VS-16E1T1-EoP and T3 modules and represent VCGs (Virtual 
Concatenation Groups) with GFP encapsulation. They can be mapped either directly to the 
physical layer or to VCG. In the latter case the binding is done in two stages and this VCG should 
be further bound to the physical layer.  
• 
HDLC ports defined on CL.2 modules represent VCGs (Virtual Concatenation Groups) with LAPS 
encapsulation. They can be mapped either directly to the physical layer or to another VCG. In 
the latter case the binding is done in two stages and this VCG should be further bound to the 
physical layer  
Ethernet over SDH/SONET 
To carry Ethernet payload without wasting bandwidth over SDH/SONET link, Megaplex-4 uses the Virtual 
Concatenation method. In this method, the contiguous bandwidth of the payload signal is divided into 
several streams, each having the rate necessary for insertion into individual VCs (SDH) or SPEs (SONET). 
With virtual concatenation, the individual VCs or SPEs are transported over the SDH or SONET network 
in the usual way, and then recombined to restore the original payload signal at the end point of the 
transmission path, using a technology similar to inverse multiplexing.  
14. At the source end, the inverse multiplexing subsystem splits the payload signal into several 
streams at a rate suitable for transmission over the desired type of VC (VC-12, VC-3 or VC-4) or 
SPE. The required information (type and number of VCs or SPEs) are defined when the virtually 
concatenated group (VCG) is defined.  
15. The resulting streams are mapped to the desired VCs/SPEs, also configured by management. 
The Path Overhead (POH) byte carried by all the group members is used to transfer to the far 
endpoint the information needed to identify: 
1. Introduction 
 
The relative time difference between arriving members of the virtual group. 
 
The sequence number of each arriving member. 
16. Each member of the virtual group is independently transmitted through the network. The 
network need not be aware of the type of payload carried by the virtual members of the group. 
17. At the receiving end, the phase of the incoming VCs/SPEs is aligned and then the original 
payload data stream is rebuilt. This requires using a memory of appropriate size for buffering all 
the arriving members of the group at the receiving end. The memory size depends on the 
maximum expected delay, therefore to minimize latency the maximum delay to be 
compensated can be defined by management. 
The following figure shows the relationship between the entities involved in the Ethernet over 
SDH/SONET functionality. Ethernet is mapped to SDH/SONET in the following steps.  
1. Bind VC/VT/STS containers to GFP or HDLC ports. This can be done in two ways: 
 
Directly 1:1 without using virtual concatenation ( no VCAT) 
 
Using virtual concatenation (VCAT). In this case VC/VT/STS should be first bound n:1 to a 
VCG port and then this VCG should be bound to a GFP/ HDLC port. 
2. Bind a GFP/HDLC port to a Logical MAC port (1 to 32). 
3. Create ingress/egress flows.  
Note 
The maximum total number of GFP and HDLC ports per CL.2 is 32.  
 

## 5.6 DS1 Ports  *(p.105)*

1. Introduction 
Bind 1:1
OR
Logical MAC
32
Logical MAC
1
Flow
Egress/Ingress Port
GFP 1..32
HDLC 1..32
VCG 
1..32
Bind 1:1
VC12/VT1.5
VC3/STS-1
VC4/STS-3C
VC4-4C/
STS-12C
Bind 1:n
Bind 1:1
VCAT No
ETH Group
OR
 
Logical Entities Representing Ethernet Traffic over SDH/SONET Media 
Ethernet over Full/Channelized T3  
1. T3 modules allow encapsulating Ethernet traffic with the GFP protocol and transferring it over 
full or channelized T3 media. In both cases Ethernet ports are connected to Logical MAC ports 
via flows, and these Logical MAC ports are bound to GFP ports. Starting from the GFP ports, two 
ways are available: 
• 
To transfer Ethernet over full T3, only one GFP/Logical MAC port is created and T3 port is bound 
directly to it. 
• 
To transfer Ethernet over channelized T3, up to 16 Logical MAC, GFP and VCG ports are created, 
so that the VCG ports are bound to GFP ports and VCG ports are bound to Logical MAC ports. Up 
1. Introduction 
to 16 T1 ports can be bound to each VCG port, but the total T1 number is limited by 28 T1 ports 
per T3 module. On the remaining T1s, regular TDM traffic can be mapped.  
The following figure shows the relationship between the entities involved in the Ethernet over T3/T1 
functionality.  
Bind 1:1
Logical MAC
16
Flow
Egress/Ingress Port
GFP 1
GFP 16
VCG 1..16
Bind 1:1
T3
T1
Bind 1:n
Bind 1:1
ETH Group
OR
Logical MAC
1
Bind 1:1
 
Logical Entities Representing Ethernet Traffic over Full/Channelized T3 Media  
Megaplex-4 Architecture Entities  
The figure below illustrates Architectural Entities involved in the Megaplex-4 I/O modules. Each entity is described 
in detail in Chapter 5 under the section for corresponding type of ports: E1, T1, Ethernet, Serial, Logical Mac, 
Teleprotection etc.  
1. Introduction 
Voice
1..4/8/16
DS0
VC-4/8/16
ETH 1..8
M-ETH
8 x E1/T1
16 x E1
DS0
ETH 1..2
tdm-bridge
1..4
Serial
1..12
GbE
12 x E1
Bind
13 x E1/T1
tdm-bridge
1..6
GbE
6 x E1/T1
Bind
cmd-channel 1
cmd-channel 2
serial
1..6
cmd-in/out 
2.1..2.4
cmd-in/out 
1.1..1.4
64 kdps
64 kdps
VS-12
VS-6/BIN
6 x E1/T1
4 x E1/T1
ETH 1
Switch
C37.94
1..2
Serial
1..6
tdm-bridge
1..6
26 x E1/T1
6 x E1/T1
DS0
DS1
1..12
PW 1..24
12 x E1/T1
DS0
DS1
1...12
PW
1...24
12 x E1/T1
12 x E1/T1
12 x E1/T1
DS1
1...12
PW
1...24
12 x E1/T1
12 x E1/T1
12 x E1/T1
Switch
13 x E1
Voice 9..12
(E&M)
GbE
4 x E1
FXS/E&M
DS1
1...8
PW
1...16
8 x E1
8 x E1
Switch
Voice 1...8
(FXS)
1 x E1
29 x E1
tdm-bridge
1..6
GbE
6 x E1
Bind
serial
1..6
1 x E1
VS-6/FXS, VS-6/FXO, VS-6/E&M
6 x E1
DS0
DS1
1...12
PW
1...24
12 x E1
12 x E1/T1
Voice 1...8
(FXS)
Voice 1...4
(E&M)
4 x E1
GbE
Bind
6 x E1/T1
2 x E1/T1
12 x E1/T1
12 x E1/T1
VS-6/C37
ETH 1
Switch
Trip Cross-connect
Primary Trip 
Out
Secondary Trip 
Out
East
West
Automation
ds1
1..4
PW 1..24
Switch
4 x E1
FE
cmd-out-i
#4
cmd-out-i
#1
cmd-out
#5
1:n
cmd-channel
#6
cmd-channel
#5
cmd-channel
#4
cmd-channel
#3
cmd-channel
#2
cmd-channel
#1
Trip In
cmd-out
#8
cmd-out-i
#4
cmd-out-i
#4
cmd-out-i
#1
cmd-out-i
#4
cmd-out-i
#1
cmd-out-i
#4
cmd-out-i
#1
cmd-out-i
#4
cmd-out-i
#4
cmd-out-i
#1
cmd-out-i
#4
cmd-out-i
#1
cmd-out-i
#1
RTU
DS0
4 x E1
cmd-out-i
#1
TP
DS0/1
L. MAC 1..16
GFP 1..16
VCG 1..16
Switch
T1 
1/ 1..28
T3
24 x E1
GbE
1:1..16
1:1
1:1
1:1
T3
GbE
Switch
ETH 1
Switch
DS0
10 x E1
Voice 1..4
(E&M)
GbE
4 x E1
VS-OCU/E&M
DS1
1...12
PW
1...16
8 x E1
8 x E1
Switch
Serial 1..2
(OCU)
1 x E1
DS0
 
I/O Modules and their Architectural Entities 
1. Introduction 
The following table lists the possible values and hierarchy of different Megaplex-4 architecture entities 
involved in the Megaplex-4 I/O modules.  
Megaplex-4 Architecture Entities and their Hierarchy  
Modules 
Port Type 
Hierarchy 
Possible Values 
CL.2 
sdh-sonet 
slot: port 
slot/1..2 
aug 
slot: au4 
speed 155: slot/1 
speed 622: slot/1..4 
vc-12 
slot:port:au4:tug3:tug2: 
tributary 
(port = sdh-sonet) 
(tributary = vc12) 
slot/port/au4/tug3/tug2/ 
1..63 
vc3-sts1 
slot:port:au4:tug3 
slot/port/au4/tug3/1..3 
vt1.5 
slot:port:au4:tug3:tug2: 
tributary 
(port = sdh-sonet) 
(tributary = vt1.5) 
slot/port/au4/tug3/tug2/ 
1..84 
oc-3 
slot: oc-3 
speed 155:  slot/1 
speed 622:  slot/1..4  
e1-i 
slot:port:tributary 
(tributary = e1-i) 
slot/port/1..63 
t1-i 
slot:port:tributary 
(tributary = t1-i) 
slot/port/1..84 
hdlc 
slot:hdlc 
slot/1..32 
gfp 
slot:gfp 
slot/1..32 
vcg 
slot:vcg 
slot/1..32 
logical-mac 
slot: logical-mac 
slot/1..32 
ethernet 
slot:port 
slot/1..2 
mng-
ethernet 
slot:port 
slot/1 
station 
id 
cl-a; cl-b 
M-ETH 
ethernet 
slot:port 
slot/1..8  
T3 
t3 
slot:port 
slot/1  
1. Introduction 
Modules 
Port Type 
Hierarchy 
Possible Values 
t1 
slot:port 
slot/1/1 .. slot/1/28 
logical-mac  
slot:port 
slot/1 .. slot/16 
gfp  
slot:port 
slot/1 .. slot/16 
vcg 
slot:port 
slot/1 .. slot/16 
VC-4/4A/8/8A/16 
voice 
slot:port 
slot/1..4, slot/1..8, slot/1..16 
TP 
(Teleprotection) 
 
 
cmd-in 
slot:port 
slot/1..4 
cmd-in-i 
slot:port:tributary 
(port = cmd-channel) (tributary = 
internal) 
slot/1/1..1/4 
slot/3/1..3/4 
cmd-out 
slot:port  
slot/1..4, 5..8 
cmd-out-i 
slot:port:tributary 
(port = cmd-channel) (tributary = 
internal) 
slot/1/1..1/4 
slot/3/1..3/4 
cmd-
channel 
slot:port  
slot/1..4 
ds1 
slot:port 
slot/1.. slot/8 
pw 
 
slot:port 
slot/1.. slot/8 
VS-12  
serial 
slot:port 
slot/1… slot/12 
tdm-bridge 
slot:port 
slot/1… slot/4 
ds1 
slot:port 
slot/1.. 12 
pw 
slot:port 
slot/1.. 24 
VS-6/BIN 
serial 
slot:port 
slot/1… slot/6  
tdm-bridge 
slot:port 
slot/1… slot/6 
ethernet 
slot:port 
slot/1 
cmd-in 
slot:port:tributary 
(port = cmd-channel) (tributary = 
internal) 
slot /1/1 …… slot /1/4  
slot /2/1 …… slot /2/4 
cmd-out 
slot:port:tributary 
(port = cmd-channel) (tributary = 
internal) 
slot /1/1 …… slot /1/4  
slot /2/1 …… slot /2/4 
cmd-
channel 
slot:port 
slot /1, slot /2 
1. Introduction 
Modules 
Port Type 
Hierarchy 
Possible Values 
ds1 
slot:port 
slot/1.. 12 
pw 
slot:port 
slot/1.. 24 
VS-6/C37 
serial 
slot:port 
slot/1… slot/6  
ethernet 
slot:port 
slot/1  
ds1-opt 
slot:port 
slot /1, slot/2 
ds1 
slot:port 
slot/1.. 12 
pw 
slot:port 
slot/1.. 24 
VS-6/FXS 
serial 
slot:port 
slot/1… slot/6  
tdm-bridge 
slot:port 
slot/1… slot/6 
ethernet 
slot:port 
slot/1 
voice 
slot:port 
slot/1.. 8 
ds1 
slot:port 
slot/1.. 12 
pw 
slot:port 
slot/1.. 24 
VS-6/FXO 
serial 
slot:port 
slot/1… slot/6  
tdm-bridge 
slot:port 
slot/1… slot/6 
ethernet 
slot:port 
slot/1 
voice 
slot:port 
slot/1.. 8 
ds1 
slot:port 
slot/1.. 12 
pw 
slot:port 
slot/1.. 24 
VS-6/E&M 
serial 
slot:port 
slot/1..6  
tdm-bridge 
slot:port 
slot/1..6 
ethernet 
slot:port 
slot/1 
voice 
slot:port 
slot/1..4 
ds1 
slot:port 
slot/1..12 
pw 
slot:port 
slot/1..24 
VS-8/E&M 
voice 
slot:port 
slot/1..8  
ds1 
slot:port 
slot/1.. 8 
pw 
slot:port 
slot/1..16 
1. Introduction 
Modules 
Port Type 
Hierarchy 
Possible Values 
FXS/E&M 
voice (FXS) 
slot:port 
slot/1..8 
voice 
(E&M) 
slot:port 
slot/9..12 
ds1 
slot:port 
slot/1..8 
pw 
slot:port 
slot/1..16 
VS-OCU/E&M 
serial (OCU) 
slot:port 
slot/1..2 
 
voice 
(E&M) 
slot:port 
slot/1..4 
 
ds1 
slot:port 
slot/1..12 
 
pw 
slot:port 
slot/1..16  
VS-16E1T1-EoP  
e1-i/t1-i 
slot:port 
slot/1..16 
e1/t1 
slot:port 
slot/1..16 
vcg 
slot:port 
slot/1..16 
gfp 
slot:port 
slot/1..16 
logical mac 
slot:port 
slot/1..16 
VS-16E1T1-PW  
e1/t1 
slot:port 
slot/1..16 
ds1 
slot:port 
slot/1..16 
pw 
slot:port 
slot/1..128 
VS-6/E1T1 
serial 
slot:port 
slot/1..6  
ethernet 
slot:port 
slot/1  
e1/t1 
slot:port 
slot/1..8 
ds1 
slot:port 
slot/1..16 
pw 
slot:port 
slot/1..128 
VS-6/703 
serial 
slot:port 
slot/1..6  
ethernet 
slot:port 
slot/1  
ds0-g703 
slot:port 
slot/1..8 
ds1 
slot:port 
slot/1..12 
pw 
slot:port 
slot/1..24 
1. Introduction 
1.5 Technical Specifications 
Note 
For I/O module technical specifications, refer to Chapters 13 and 14. 
 
STM-1/STM-4/ 
OC-3/OC-12 Ports 
Number of Ports  
• 2 per CL module  
• 4 per chassis 
Bit Rate 
• STM-1/OC-3:155.52 Mbps ± 4.6 ppm 
• STM-4/OC-12: 622.08 Mbps ± 4.6 ppm  
 
Compliance 
• SDH: ITU-T G.957, G.783, G.798 
• SONET: GR-253-CORE  
 
Line Code 
NRZ 
 
Framing 
• SDH: ITU-T Rec. G.707, G.708, G.709, G.783 
• SONET: ANSI T1.105-1995, GR-253-CORE 
 
Ethernet over SDH/SONET 
 
• GFP (Generic Framing Procedure): ITU-T G.7041, 
ANSI T1-105.02, framed mode  
• LAPS (Links Access Procedure); X.86 
• LCAS (Link Capacity Adjustment Scheme): ITU-T 
G.7042 
 
Protection 
• 1+1 unidirectional APS (G.842) 
• 1+1 bidirectional APS (G.841, Clause 7.1). 
• 1+1 bidirectional optimized APS (G.841 Annex B. 
Linear Multiplex Section (MSP); compatible with 1:1 
bidirectional switching) 
• Path Protection (Telecordia UPSR standard and ITU-T 
SNCP recommendation) 
 
Connectors 
SFP-based in accordance with RAD’s SFP/XFP 
Transceivers data sheet.  
GbE Ports 
Number of Ports  
• 2 per CL module  
• 4 per chassis 
 
External Ports  
In accordance with order: 
• Two GbE ports with SFP modules  
• Two GbE ports with copper (RJ-45) interfaces  
 
Maximum Frame Size  
9600 bytes (for max. frame sizes supported by different 
I/O modules, see Configuring User Ethernet Ports in 
Chapter 5)  
1. Introduction 
 
Protection  
On the same CL module (link protection) or between CL 
modules (link and equipment protection):  
• LAG with or without LACP 
• ERPS (G.8032v1) 
Copper GbE Ports 
Interface Type  
10/100/1000BASE-T port, full-duplex, with 
autonegotiation  
 
Connectors (per port) 
RJ-45, shielded 
Optical GbE Ports   
Interface Type  
1000 Mbps full-duplex port  
Link Connectors 
SFP-based in accordance with the table below 
 
 
Note: For detailed specifications of SFP transceivers, see the 
RAD SFP Transceivers data sheet. 
SFP Connector Modules for GbE Interfaces 
Transceiver 
Wavelength 
Fiber Type  
Transmitte
r 
Type 
Connecto
r Type 
Input power 
(dBm) 
Output Power 
(dBm) 
Typical Max. 
Range 
(min) 
(max) 
(min) 
(max) 
(km) 
(miles) 
SFP-5 
850 nm 
50/125 µm, 
multi-mode 
VCSEL 
LC 
-17 
0 
-9.5 
0 
0.55 
0.3 
SFP-6 
1310 nm 
9/125 µm, 
single mode 
Laser 
LC 
-20 
-3 
-9.5 
-3 
10 
6.2 
SFP-7 
1550 nm 
9/125 µm, 
single mode 
Laser 
LC 
-22 
-3 
0 
+5 
80 
49.7 
SFP-8d 
1310 nm 
9/125 µm, 
single mode 
Laser 
LC 
-21 
-3 
0 
-4 
40 
24.8 
 
Serial Control Port 
(CONTROL DCE) 
Interface 
RS-232/V.24 (DCE) 
Data Rate 
9.6, 19.2, 38.4, 57.6, 115.2 kbps asynchronous  
 
Connector 
• CL.2: DB-9 
• CL.2/4104: MINI-USB 
Ethernet Management 
Port (CONTROL ETH)  
Interface 
10/100BaseT with autonegotiation 
Connector 
RJ-45 
1. Introduction 
Timing 
Clock Sources 
• Recovered from the STM-4/STM-1/OC-12/OC-3 
interface, including automatic selection based on 
SSM (Synchronization Status Messaging) 
• Internal crystal free-running oscillator-based clock 
• Derived from the receive clock of a specified user 
port 
• Adaptive clock recovered (ACR) from a pseudowire 
circuit 
• External station clock 
 
Internal Clock Quality 
CL.2/622GBEA: ST-3E 
 
CL.2/GBEA: ST-3E 
 
CL.2 ST-3E: 
CL.2/DS0: ST-4 
 
Station Clock Interface 
Rate: 
• 2.048 MHz 
• 2.048 Mbps  
• 1.544 Mbps 
 
 
Interface (software-selectable): 
• RS-422 squarewave  
• ITU-T Rec. G.703, HDB3 coding for 2.048 MHz and 
2.048 Mbps 
• ITU-T Rec. G.703, B8ZS coding for 1.544 Mbps 
 
Connector 
RJ-45 
Diagnostics 
Tests 
Local and remote loopbacks per link  
 
Alarms 
Time and date stamped 
 
Performance Statistics 
Ethernet, SDH/SONET, E1/T1, VCG, GFP, HDLC and PW 
ports  
Indicators  
Front Panel  
 
 
POWER SUPPLY A, B 
 
(green) 
• On: the corresponding PS module is on (and one of 
the CL modules is active) 
• Off: Power supply is off 
 
 
SYSTEM TEST (yellow) • On: a test (or loopback) is being performed in the 
Megaplex-4 
• Off: No active tests 
1. Introduction 
 
 
SYSTEM ALARM (red) • Blinking: a major and/or critical alarm has been 
detected in Megaplex-4  
• On: a minor alarm has been detected in Megaplex-4  
• Off: No active alarms 
 
CL.2 Module  
 
 
 
 
 
ON LINE 
(green/yellow) 
• On (green): CL module is active or software 
decompression 
• Blinking slowly (green): CL module is on standby 
• On (yellow): a test is being performed (active 
module only) 
 
 
ALM (red) 
• On: alarms have been detected in the  
Megaplex-4, but the highest alarm severity is minor 
or warning. 
• Blinking: a major and/or critical alarm has been 
detected in Megaplex-4 
• Off: No active alarms 
 
SDH/SONET Ports  
 
 
 
ON LINE 
(green/yellow) 
On (green): the corresponding port is active (carries 
SDH/SONET traffic, and there is no major alarm 
condition, nor any test on this port) 
Blinking (green) – the port is in protection mode 
On (yellow): a test is active on the port 
Off: no traffic or test on the port 
 
 
LOS (red) 
On: loss-of-signal at the corresponding port  
Off: no loss-of-signal 
 
GbE Ports  
 
 
 
LINK (green) 
On: the port is connected to an active Ethernet hub or 
switch 
Off: Ethernet link is not detected 
 
 
ACT (yellow) 
On or Blinking (in accordance with the traffic): ETH 
frames are received or transmitted 
Off: ETH frames are not received and transmitted  
 
Management Ethernet Ports 
 
 
 
LINK (green) 
On: the port is connected to an active Ethernet hub or 
switch 
Off: Ethernet link is not detected 
1. Introduction 
 
 
ACT (yellow) 
On or Blinking (in accordance with the traffic): ETH 
frames are received or transmitted 
Off: ETH frames are not received and transmitted  
 
Station CLOCK Port 
 
 
 
ON (green) 
On: the station clock port is configured as no shutdown 
Off: no traffic or test on the port 
 
 
LOS (red) 
On: loss-of-signal (when station clock port configured as 
connected)  
Off: no loss-of-signal 
Alarm Relay Port 
Port Functions 
• 1 inbound RS-232 alarm input 
• 2 outbound (dry contact) relays triggered by 
major/minor alarms 
 
Operation 
Normally open, normally closed, using different pins 
 
Connector 
 
• CL.2: DB-9, female 
• CL.2/4104: 9-pin, flat 
Power Consumption 
 
27.75 W (per CL, max) 
Power Supplies 
See below 
 
 
Caution 
The DC input is primarily designed for negative input voltage (grounded 
positive pole). However, the DC input voltage can be floated with respect to 
Megaplex-4 ground by means of field-selectable jumpers. Internal jumpers 
can also be set to match operational requirements that need either the + 
(positive) or – (negative) terminal of the power source to be grounded. 
Contact your nearest RAD Partner for detailed information.  
Power Supplies  
MP-4100 
 
MP-4104 
 
PS/AC 
PS/DC 
PS/AC 
PS/DC 
Operating Range 
115 VAC/230 
VAC (85 to 264 
VAC) 
-48 VDC  
(-36 to -56 VDC) 
90 VAC to 260 
VAC 
 
-48 VDC (-36 to -56 VDC) 
Frequency 
50/60Hz 
- 
50/60Hz 
- 
HVDC support 
100 to 360 VDC 
- 
110 to 300 
VDC 
- 
1. Introduction 
MP-4100 
 
MP-4104 
 
PS/AC 
PS/DC 
PS/AC 
PS/DC 
Maximum AC input 
power 
315W + power supplied for ring and 
feed voltage purposes  
200W + power supplied for ring and feed 
voltage purposes  
Total output 
power 
250W* + power supplied for ring 
and feed voltage purposes (drawn 
directly from external source) 
160W + power supplied for ring and feed 
voltage purposes (drawn directly from 
external source) 
Selectable ground 
reference or 
floating ground  
- 
Yes 
- 
Yes 
* IEEE-1613 “no-fan” compliant system and modules: 175W 
 
 
Megaplex-4100 
Chassis 
Number of Module Slots 
14-slot chassis 
Slot Usage 
• 2 power supply slots 
• 2 common logic slots 
• 10 identical slots for I/O modules 
Megaplex-4104 
Chassis 
Number of Module Slots  
8-slot chassis 
Slot Usage 
• 2 power supply slots (of different shape) 
• 2 common logic slots (can also accommodate a single dual-
slot CL.2 module) 
• 4 identical slots for I/O modules 
Chassis Dimensions 
 
Height 
Width 
Depth (without handles) 
 
Megaplex-4100 
18 cm/7 in (4U) 
44 cm/17 in 
33 cm/13 in (regular chassis) 
37 cm/14.6 in (IEEE-1613- 
compliant chassis) 
Megaplex-4104 
9 cm/3.5 in (2U) 
44 cm/17 in 
33 cm/13 in 
 
 
 
 
 
Maximum Power Supply Output Currents 
Regulated Output Voltage  
+3.3V 
+5V 
-5V 
+12V 
-12V 
PS/4100 
30A 
40A 
6.5A 
2A 
2A 
 
PS/4104 
25A 
15A 
2.4A 
2A 
0.8A 
1. Introduction 
 
Weight (fully loaded 
chassis) 
15.3 kg/33.8 lb max. 
7.54 kg/16.6 lb max. 
CL.2 Dimensions 
 
Height 
Width 
CL.2/4100 
17.3 cm (6.8 in) 
4.5 cm (1.8 in) 
CL.2/4104 
17.3 cm (6.8 in) 
2.5 cm (1 in) 
 
Depth – Regular  
Depth – IEEE-1613- 
compliant 
32.5 cm (12.8 in) 
35 cm (13.8 in) 
32.5 cm (12.8 in) 
 
 
Weight – Regular  
Weight – IEEE-1613- 
compliant 
630 g (1.3 lb) 
2030 g (2.27 lb) 
540 g (1.2 lb) 
Rack Installation Kits 
Megaplex-4100  
RM-MP-MX-23/19: hardware kit for installing one Megaplex-
4100 in either a 19-inch or 23-inch rack 
MP-2100-RM-ETSI/19: hardware kit for installing one 
Megaplex-4100 in a 23-inch ETSI rack (can also be used for 
installation in 19-inch rack) 
Megaplex-4104 
RM-42: hardware kit for installing one Megaplex-4104 in a 19-
inch rack 
RM-42-CM:  hardware kit for installing one Megaplex-4104 in a 
19-inch rack with cable management 
WM-42: wall-mounting kit for installing Megaplex-4104  
WM-42-CM: wall-mounting kit for installing Megaplex-4104  
with cable management 
 
Note 
Chassis handles installed on the rack mount brackets add 4 cm (1.6 in) to the 
total depth 
 
Environment 
Operating Temperature 
-10°C to 55°C (14°F to 131°F) 
Note:  For extended operating temperature ranges, and for “no-
fans” Megaplex-4104 chassis temperature ranges, refer to 
Ambient Requirements section in Chapter 2. For additional 
questions, contact your local RAD Business Partner. 
Storage Temperature 
-20°C to +70°C (-4°F to +160°F) 
Humidity 
Up to 95%, non-condensing 
 
1. Introduction 
Note 
Actual operating temperature range is determined by the specific modules 
installed in the chassis.  
 
 
 