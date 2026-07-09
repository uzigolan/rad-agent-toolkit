# Installation and Operation – 1 Introduction

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 36–84.*


## 1.1 Overview  *(p.36)*

ETX-2i Devices 
1. Introduction 
1 Introduction 
1.1 Overview 
ETX-2i is a family of next-generation NTU, delivering RAD’s Service Assured Access solution, by extending 
packet networks to customer premises over various infrastructure types. 
Product Overview 
The table below provides an overview of all available ETX products and their typical locations. 
Typical Locations 
ETX-2i Platform 
• POP 
• Small-Medium Branch 
• Mobile xHaul 
ETX-2i 
High performance L2 demarcation and HW data router 
 
• Branch office 
• Small cells 
ETX-2i-B 
Cost effective L2/L3 VPN services with HW router 
 
 
 
 
• POP 
• HQ CPE 
• Medium-Large Branch  
• Mobile xHaul 
• 1588v2 GM 
ETX-2i-10G 
Advanced medium-high capacity 10G demarcation 
 
ETX-2i Devices 
1. Introduction 
Typical Locations 
ETX-2i Platform 
• Branch Office 
• Cell sites 
ETX-2i-10G-B 
High capacity 10G demarcation for core Carrier Ethernet service, Layer 
2/3 VPNs and basic CPEs 
 
 
 
 
 
ETX-2i-10G-B 
ETX-2i-10G outdoor unit with 8SFPP ports via Gland connectors 
 
 
ETX-2i-10G-B 
ETX-2i-10G outdoor unit with 8SFPP ports via three Conduit connectors 
 
• Branch Office 
• Cell sites 
ETX-2i-10G-E 
Power consumption optimized high capacity 10G demarcation 
 
 
• POP 
• HQ CPE 
• Large Branch  
• Data Center 
 
ETX-2i-100G 
High capacity 100GBE demarcation (with extended memory) 
General Product Description 
The ETX-2i family includes demarcation devices varying from 1G to 100G interfaces, the branch office 
devices of ETX-2i and ETX-2i-B, the branch office device ETX-2i-B for 1GbE business applications, and the 
ETX-2i-10G and ETX-2i-10G-B devices that support 1GbE and 10GbE ports. It also includes ETX-2i-100G, 
capable of delivering up to 100GbE services using a mix of 1GbE/10GbE/25GbE, 40GbE, and 100GbE 
interfaces, while offering Carrier Ethernet 3.0 compliant service models, service monitoring, flexibility, 
ETX-2i Devices 
1. Introduction 
and manageability. ETX-2i-100G/4Q (with 4x100G QSFP28 ports, 8x10G/25 SFP28 ports and 8x1/10G 
SFP+ ports) is designed to address the ever-growing demand for bandwidth and for agile, reliable, and 
assurable service demarcation and aggregation at data rates that reach up to 100GbE. 
The ETX-2i family provides Ethernet business services, Layer-3 VPNs, and TDM services, as well as value 
added services using virtualization at the customer edge, for carriers, mobile operators, and 
wholesalers. 
The ETX-2i family provides MEF CE2.0 E-LAN, E-Line, and E-Tree, and E-Access Ethernet services over 
FE/GbE, 10GbE, 40GbE, and 100GbE interfaces. It offers the same services over PDH connections and 
SONET/SDH infrastructure. ETX-2i supports an integrated Bridge functionality to allow full support of 
E-LAN and E-Tree services, as well as ring topologies. In addition to its extensive L2 features, ETX-2i 
supports an optional embedded router with high-rate L3 forwarding capabilities. Multiple VRFs (up to 
10) are supported when the Dynamic Router license or TWAMP license is enabled. 
The ETX-2i family supports a rich offering of QoS functionality, including MEF 10.3 rank Policers that 
deliver high-scale multi-CoS services with hierarchical Quality of Service (HQoS). Per-service queueing, 
and scheduling mechanisms that allow service providers to offer multiple services using the same 
physical port with guaranteed SLA. Each service can be differentiated by rate limitation, WRED per 
EVC.CoS, traffic shaping per EVC, traffic prioritization, and flexible classification rules with flexible access 
lists. Additionally, it supports multicast with MLD snooping. 
Using hardware-powered processing, ETX-2i performs OAM and PM measurements at Layer-2 and 
Layer-3 with up to one microsecond precision, including collection of unidirectional and bidirectional PM 
parameters (frame loss, delay, and delay variation) with Y.1731 and TWAMP standards. It also offers 
immediate detection of loss of continuity (LOC), triggering sub 50 ms protection switching in ring 
topologies (G.8032v2) and end-to-end service protection (G.8031). 
ETX-2i provides these types of Ethernet OAM: 
• 
Single-segment (link) OAM according to IEEE 802.3-2005, active and passive mode  
• 
End-to-end connectivity OAM based on IEEE 802.1ag  
• 
End-to-end service and performance monitoring based on ITU-T Y.1731 
ETX-2i supports Layer-3 PM measurements based on TWAMP Light. It also offers diagnostic tools that 
include MAC and IP-based intrusive and non-intrusive loopbacks with MAC and IP swap, as well as 
advanced RFC-2544, Y.1564, and L3 SAT generators and analyzers for service activation tests that 
generate “birth certificate” reports. 
Furthermore, incorporating RAD’s SyncToP platform of synchronization and timing over packet feature 
set, ETX-2i offers an extended timing suite comprised of IEEE 1588v2 transparent clock (TC), slave clock, 
and boundary clock, as well as synchronous Ethernet to ensure highly accurate timing delivery in 
ETX-2i Devices 
1. Introduction 
packet-based mobile backhaul networks.  ETX-2i-10G-B/8SFPP/ODU can also act as an IEEE 1588v2 
grandmaster (GM) with an integrated GNSS receiver.  
Product Options 
Several product options of the unit are available, offering different combinations of ports, enclosures, 
and functionalities. Available product options in the ETX-2i family are ETX-2i, ETX-2i-B, ETX-2i-10G, ETX-
2i-10G-B, ETX-2i-10G-E and ETX-2i-100G. 
ETX-2i 
ETX-2i is available with the following options: 
• 
Four, six, or eight fixed Ethernet SFP/copper combo ports, available in 19-inch or 8.5-
inch enclosure 
• 
64 E1 ports that provide TDM pseudowire functionality (ETX-2i-64E1)  
• 
Modular option, in 19-inch or 8.5-inch enclosure, available with GbE (two SFP/copper combo 
ports). 
NEBS-compliant enclosures, dry contacts, and SyncE/PTP options are available (with ports specified in 
Timing and Synchronization).  
ETX-2i-B 
The ETX-2i-B device has up to ten 1GbE interfaces in an 8.5-inch metal enclosure, and is available in the 
following options: 
• 
Network ports – two 1GbE SFP  
• 
User ports – two 1GbE SFP/copper combo ports, four 1Gbe copper UTP ports, four SFP ports, or 
eight SFP ports (2U hardened option) 
• 
Single AC, Dual DC inlet, or wide-range AC/DC with auto detection 
• 
Click here to enter text.ETX-2i-B can be ordered with the SyncE/PTP and the dry contact (DRC) 
option, in which case the device provides the ports specified in Timing and Synchronization. 
ETX-2i Devices 
1. Introduction 
ETX-2i-10G, ETX-2i-10G-B 
The ETX-2i-10G product option includes ETX-2i-10G, ETX-2i-10G-B/4SFPP, ETX-2i-10G-B/8SFPP full and 
half 19-inch devices, and ETX-2i-10G-B/8SFePP/ODU, an ordering option for outdoor installations 
(introduced in version 6.8.2 (0.21). The various ETX-2i-10G and ETX-2i-10G-B ordering options support 
up to eight 10GbE interfaces and up to 24 1GbE interfaces in a half (8.5-inch) or full (19-inch) metal 
enclosure, and are available in the following options: 
• 
Whenever ETX-2i-10G-B is used, it represents both ETX-2i-10G and ETX-2i-10G-B, unless noted 
otherwise. 
• 
10GbE interface (license enabled) – two, four, or eight SFP+ (1/10 GbE) ports with the following 
characteristics: 
 
Configurable SFP+ rate (1/10GbE) 
 
Automatic recognition of SFP+ rate (1/10GbE) 
 
Auto-negotiation and max capability relevant for 1GbE SFP+ only; not for 10GbE interface 
 
Digital-diagnostic-monitoring (DDM) support (provides a user with critical information 
concerning the status of transmitted and received signals) 
 
Flow control support for Rx only 
 
When sold without the 10GbE license, ETX-2i-10G requires an activation license to use the 
10GbE SFP+ ports. 
 
Supports 1G copper SFP (1G rate only)  
 
Supports 10G copper SFPP 
 
Supports DAC-10G cable (versions 6.8.2 (0.59), 6.8.2 (0.60)) 
 
100 Mbps copper SFP supported when inserted into the SFP side of a MiNID that is in an 
SFPP port (ETX-2i-10G-B/8SFPP). 
• 
1GbE interface – 0, 8, 12, or 24 ports, composed of SFP, UTP, and/or SFP/UTP combo ports: 
 
Eight 1GbE (4xSFP and 4xUTP) ports (ETX-2i-10G half 19-inch and ETX-2i-10G-B/4SFPP full 
and half 19-inch; see catalog for other available SFP/UTP port combinations.)  
 
12 1GbE SFP and 12 1GbE UTP ports (ETX-2i-10G full 19-inch only) 
 
24 1GbE SFP ports (ETX-2i-10G full 19-inch only) 
 
12 1GbE SFP + 12 1GbE UTP combo ports (ETX-2i-10G full 19-inch only) 
 
SFP+ ports, without the 10G license, function as 1GbE ports. 
 
Supports 1G Copper SFP (1G rate only) 
 
DDM support 
 
Auto negotiation support 
 
Flow control support for Rx only 
ETX-2i Devices 
1. Introduction 
• 
Mini USB console port (in ETX-2i-10G and ETX-2i-10G-B/4SFPP full and half 19-inch ordering 
options) 
• 
Micro USB console port (in ETX-2i-10G-B/8SFPP full and half 19-inch ordering options) 
• 
RJ-45 console port (in ETX-2i-10G-B/8SFPP/ODU) 
• 
ETX-2i-10G-B/8SFPP/ODU is enclosed in an aluminum IP66 protected enclosure  
• 
Supports timing (in ETX-2i-10G and ETX-2i-10G-B/4SFPP full and half 19-inch ordering options, 
and in ETX-2i-10G-B/8SFPP with PTP and eSyncE full 19-inch (introduced in version 6.8.2 (0.21)); 
supports additional G.8275.1 BC Class C timing option on ETX-2i-10G-B/4SFPP/4S/4U/PTP and 
ETX-2i-10G/12SFP12UTP fiber ports 
• 
Modular Single or Dual AC/DC power supply, or a combination of DC and AC power supplies (19-
inch enclosure)  
• 
Integrated Single AC, DC, or Dual DC inlet front access power supply (half 19-inch enclosure) 
• 
Dual integrated AC and DC power supply, or a combination of DC and AC power supplies  
(ETX-2i-10G-B/4SFPP 19-inch enclosure) 
• 
Dual integrated AC or DC redundant power supply (ETX-2i-10G-B/8SFPP with PTP full 19-inch) 
• 
Available in NEBS enclosure (ETX-2i-10G-B/19/N/8SFPP) in any combination of power supplies 
(AC/DC/ACR/DCR/ACDC) as follows: 
 
ETX-2i-10G-B/19/HN/ACDC/8SFPP 
 
ETX-2i-10G-B/19/HN/ACR/8SFPP 
 
ETX-2i-10G-B/19/HN/DCR/8SFPP 
 
ETX-2i-10G-B/19/N/ACDC/8SFPP 
 
ETX-2i-10G-B/19/N/ACR/8SFPP 
 
ETX-2i-10G-B/19/N/DCR/8SFPP 
 
ETX-2i-10G/19/HN/ACDC/8SFPP 
 
ETX-2i-10G/19/HN/ACR/8SFPP 
 
ETX-2i-10G/19/HN/DCR/8SFPP 
 
ETX-2i-10G/19/N/ACDC/8SFPP 
 
ETX-2i-10G/19/N/ACR/8SFPP 
 
ETX-2i-10G/19/N/DCR/8SFPP 
• 
Hot swappable power supply; ACAC, DCDC, or ACDC (ETX-2i-10G-B/4SFPP/4S/4U/PTP 19-inch 
enclosure); ACR, DCR (ETX-2i-10G-B/8SFPP with PTP full 19-inch) 
ETX-2i Devices 
1. Introduction 
Note 
As ETX-2i-10G-B and ETX-2i-10G enclosures are identical, a sticker with the  
product name is affixed to the ETX-2i-10G-B bottom panel to distinguish it 
from ETX-2i-10G.  
ETX-2i-10G-B can be ordered with NEBS-compliant enclosures, front-to-back airflow,  SyncE/PTP, and dry 
contacts options, in which case the device provides the ports specified in Timing and Synchronization. 
ETX-2i-10G-E 
The ETX-2i-10G-E product option is an 8.5-inch indoor 10G platform featuring a total of 8x10GbE 
(SFP/SFPP) ports and optional PTP. It is available as product option ETX-2i-10G-E/AC/8.5/8P. 
ETX-2i-10G-E increases the scale of the different services, reduces device power consumption, offers 
10G Fiber/1G UTP combo-ports and supports timing. 
ETX-2i-100G/4Q 
The ETX-2i-100G/4Q platform supports a total of 20 fixed interfaces in a full 19-inch 1U metal enclosure, 
and is available in the following option:  
• 
100GbE interface – four QSFP28 ports with the following characteristics: 
 
No auto negotiation 
 
Only full duplex mode 
 
DDM support 
 
FEC configuration support 
 
Link Fail Signaling (LFS) support 
• 
25GbE interface – 8 SFP28 (1/10/25 GbE) ports with the following characteristics: 
 
No auto negotiation 
 
Only full duplex mode 
 
DDM support 
 
FEC configuration support 
 
Link Fail Signaling (LFS) support 
• 
10GbE interface – 8 SFP+ (1/10 GbE) ports with the following characteristics: 
 
Configurable SFPP speed 
 
1/10G multirate SFPPs 
 
Auto-negotiation and max capability relevant for 1GbE SFP+ only; not for 10GbE interface 
 
DDM support 
ETX-2i Devices 
1. Introduction 
 
Auto negotiation support 
 
Flow control for Rx only 
 
LFS support 
 
Supports 1GbE copper SFPs 
 
Supports SFP-30 (copper) 
 
Supports 10G copper SFPPs 
 
Supports DAC-10G cable 
• 
MEF-compliant service topologies, including E-Line, E-LAN, E-Tree, and E-Access services 
• 
IEEE 802.3ad link aggregation (1:1 LAG), ITU-T G.8031 Ethernet linear protection, and TU-T 
G.8032v2 Ethernet ring protection with sub-50ms restoration time 
• 
Advanced QoS with hierarchical policing and bandwidth shaping per EVC and EVC.CoS 
• 
Accurate, scalable hardware-based OAM and PM (ITU-T Y.1731 and TWAMP) 
• 
ITU-T Y.1564 service activation testing at wire speed 
• 
Advanced management capabilities, fully compatible with the ETX-2i family and supported by 
RADview EMS/NMS and Performance Monitoring portal 
• 
NETCONF/YANG support for intelligent service orchestration 
• 
Zero-touch provisioning (ZTP) for scalable, secure, rapid service roll-out, and lower cost of 
operation 
• 
Two front access redundant hot swappable power supplies: AC or DC  
• 
Micro USB console port 
• 
Low power consumption for cost effective operation 
ETX-2i-100G-40G 
The ETX-2i-100G/40G platform (introduced in version 6.8.2 (0.21)) supports a total of 20 fixed interfaces 
in a full 19-inch 1U metal enclosure, and is available in the following option:  
• 
100GbE interface – two ETH QSFP28 ports with the same characteristics as ETX-2i-100G/4Q. 
• 
40GbE interface – two ETH QSFPP ports with the following characteristics: 
 
DDM support 
 
No auto-negotiation  
 
Full duplex mode only 
• 
10GbE interface – 16 SFP+ (1/10 GbE) ports with the same characteristics as ETX-2i-100G/4Q. 
ETX-2i Devices 
1. Introduction 
Applications 
Ethernet Demarcation for Retail and Wholesale Services 
ETX-2i can function as an Ethernet demarcation device, separating the service provider network, the 
access provider network, and the customer network. The figure below illustrates a complete access 
solution with full-service visibility. ETX-2i, placed at connection points in the network, greatly 
contributes to monitoring and troubleshooting the network, using its enhanced Ethernet OAM and 
performance monitoring capabilities. 
 
The following figure shows ETX-2i-100G demarcation and aggregation: 
Access Network First Mile
Access Aggregation 
10 GbE Ring
1/10 GbE
Ring
xDSL
GbE
ETX-2i
SDH/
SONET
PDH/
SDH
ETX-2i
ETX-2i
ETX-2i
Cell-Site
Customer 
Premises
ETX-2i-10G
1/10 GbE
FE/GbE
ETX-2i
ETX-2i-10G
MSAN
ETX-2i-10G
MiNID
100 GbE
ETX-2i-10G
RADview
Cloud
Data Center
Data Center
ETX-2i-100G
Data Center Gateway
100 GbE/
n x 10 GbE
Single Tenant EAD
n x 10 GbE / 100 GbE UNI
Multi-Tenant EAD
n x 10 GbE UNI
ETX-2i-10G
10 GbE to 10 GbE
Aggregation
100 GbE
100 GbE
100 GbE
100 GbE
Service Assured Access
ETX-2i-100G
ETX-2i-100G
100 GbE
PSN Core
ETX-2i-10G
ETX-2i-100G
Access Aggregation
ETX-2i Devices 
1. Introduction 
Mobile Demarcation Device for Mobile Backhauling Applications 
As a mobile demarcation device (MDD), ETX-2i is installed at the operator tower and controller sites 
equipped with an Ethernet port, connecting the IP-NodeB or eNodeB to the packet network (see below). 
It features sophisticated traffic management and service assurance capabilities, including proactive 
service monitoring and fault identification throughout the entire network. Furthermore, statistical 
analysis allows backhaul wholesalers to execute effective capacity planning to overcome the “peak to 
mean” gap, such that bandwidth is added only when needed, based on actual usage. ETX-2i also 
backhauls legacy 2G and 3G E1/T1 traffic with TDM pseudowire services offering a “one box solution” 
for mixed Ethernet and TDM services over a unified packet network.  
G.8032 v2
1/10 GbE
Ring
ETH
TDM
BTS
Node B
G.8032 v2
1/10 GbE
Ring
RADview
IP/MPLS
Macro or Small
Cells
Transport Network
Mobile Network
ETH
TDM
End-to-End SLA Assurance, Circuit Validation, Traffic Management, TDM PWE
n x STM-1/
OC-3
Timing (1588PTP/SYNC-E)
ETX
GPS
eNB
ETX-2i
BTS
Node B
ETX-2i
ETX-2i
ETX-2i
ETX-2i
BSC
Router
RNC/aGW
MiNID
ETX-2i-10G
 
ETX-2i Devices 
1. Introduction 
Features 
Traffic Processing 
ETX-2i incorporates a complete set of CE 2.0-certified Ethernet service tools that allow the service 
provider to distinguish between high- and low-priority traffic, and to optimize TCP sessions. 
Forwarding 
Traffic forwarding is performed via point-to-point, bridge, or L3 forwarding (router) mechanisms. 
Traffic forwarding is performed via point-to-point, bridge, or L3 forwarding (router) mechanisms. 
The ETX-2i bridge operates in VLAN-aware or VLAN-unaware mode.  
The ingress user traffic is mapped to Ethernet flows using flexible per-port classification criteria. VLAN 
editing can be performed on the flows such as overwriting the VLAN, adding a new VLAN (push), or 
removing a VLAN (pop). 
TDM Pseudowire 
Note 
This feature is applicable to ETX-2i-64E1 with built-in E1 ports, and devices 
that support smart SFP MiTOP functionality. It is not applicable to ETX-2i-
100G.  
ETX-2i can be ordered with 64 E1 interfaces for TDM over packet pseudowire services. Devices that have 
integrated MiTOPs also allow TDM over packet pseudowire services. Each TDM pseudowire (PW) carries 
a single bundle (group of timeslots) to a predefined far-end bundle. 
The following standard payload encapsulation methods are supported: 
CESoPSN  
(with or without CAS) 
CES (Circuit Emulation Services) over PSN, for framed traffic, according to  
IETF RFC 5086 
SAToP 
Structure-Agnostic TDM over Packet, for unframed traffic, according to IETF RFC 4553 
The pseudowire connections can be encapsulated by the device for the following types of PSN transport 
networks: 
• 
MEF 8 (Ethernet) (not supported in ETX-2i-64E1) 
• 
UDP over IP 
ETX-2i Devices 
1. Introduction 
Fat Pipe Detection and Rate Limiting 
The Fat pipe mechanism (AKA Elephant flow or LFP – Large Flow Prevention; in ETX-2i-10G half 19-inch, 
ETX-2i-10G-B full and half 19-inch, and ETX-2i-100G/4Q) detects high bandwidth sessions going over 
limited bandwidth paths, thus allowing the operator to rate limit these sessions. This reduces congestion 
and drops for all traffic going over these paths. 
Ethernet over GRE (ETHoGRE) Tunnel 
ETX-2i and ETX-2i-B with an embedded router support Ethernet over GRE (ETHoGRE), a Layer-2 
tunneling technology that allows transport of Layer-2 frames and services over an IP/MPLS network 
using IP/GRE encapsulation.  
Layer-2 Control Processing (L2CP) 
You can create L2CP profiles to define the handling of Layer-2 Control Protocol traffic. You can assign a 
profile to Ethernet ports and flows. ETX-2i then tunnels, discards, or peers L2CP packets, according to 
the profile definition. 
Link Layer Discovery Protocol (LLDP) 
LLDP packets are sent periodically between ETX-2i and neighboring devices on the same physical LAN, 
advertising information about itself and obtaining neighbor information. This automated discovery of 
devices simplifies management and network maintenance, reducing general setup costs of new 
equipment. 
MLDv2 Snooping 
ETX-2i IPv6 routers support Multicast Listener Discovery Version 2 (MLDv2) protocol to discover 
multicast listeners on attached links and addresses that are of interest to them. Bridges use MLDv2 
Snooping to reduce multicast traffic by analyzing MLDv2 messages and limiting multicast traffic to ports 
interested in it. 
Routing 
ETX-2i (except for ETX-2i-64E1) and ETX-2i-B support a high-performance, dual-stack, IPv4/IPv6 
embedded router.  
 
 
ETX-2i Devices 
1. Introduction 
ETX-2i and ETX-2i-B are offered with two software licenses per ordering option: 
• 
Dynamic embedded router: 
 
Layer-3 HW forwarding 
 
Supports the following:  
 
OSPFv2 and BGPv4 routing protocols 
 
BFD for fast forwarding path failure detection 
 
IPv4/IPv6 ACLs 
 
VRRPv2/v3 
 
Static Router: Same as Dynamic Router, but routing protocols are not supported. 
A change to Dynamic Router from Static Router software license is supported; however, a change to 
Static Router from Dynamic Router software license is supported only when the device is set to default. 
Note 
ETX-2i-64E1, ETX-2i-10G, ETX-2i-10G-B, ETX-2i-10G-E and ETX-2i-100G are not 
offered with a dynamic router ordering option.  
Device management, as well as other L3 ‘modules’, such as 1588 (8265.1), TDM PW (UDP/IP), and 
TWAMP, use the ETX-2i routing scheme. 
When the dynamic router or TWAMP license is enabled, ETX-2i supports multiple VRFs (up to 10); 
management is supported over VRF1 only.  
Resiliency and Optimization 
ETX-2i provides the following to ensure five nines (99.999%) availability and sub-50 ms restoration in the 
event of network outages: 
• 
Link redundancy in a LAG architecture that supports the LACP protocol according to 802.3-2005.  
• 
LAG delivery of link protection and link redundancy between two network ports or two user 
ports. 
• 
Dual homing technology in a 1:1 architecture allows ETX-2i to be connected to two different 
upstream devices. 
 
 
ETX-2i Devices 
1. Introduction 
• 
Ethernet protection switching in the following modes for network ports per ITU-T G.8031: 
 
1:1 bidirectional with APS protocol – Endpoints negotiate using APS protocol.  
 
1:1 unidirectional without APS protocol – Endpoints act independently and do not negotiate 
with each other. Unidirectional mode is suitable for EVC level dual homing applications.  
• 
Ethernet Ring Protection per G.8032v2 Layer-2 to protect against link and node failures. This 
supports ring topology and delivers low-cost traffic protection and rapid service restoration, 
with SDH/SONET type resilience. 
The ETX-2i fault propagation mechanism enables propagating user port failures to the network and the 
remote end, as well as propagating network failures back to the user port. The mechanism has a set of 
triggers and actions (i.e., rules) that are based on the physical layer (e.g., port failure), ETH OAM (AIS, 
RDI, LOC, etc.), or VRRP group. Up to 32 fault propagation rules can be defined. 
A Traffic Management Fault Propagation (TMFP) license can be enabled to provide the Fault Propagation 
mechanism with a set of triggers and actions for Queue Block Shaper and flow Policer (Event Manager).  
The additional fault propagation actions are: 
• 
Change Policer rate 
• 
Change Shaper rate 
Configuration of these actions enables you to implement network/application level redundancy schemes 
while controlling the bandwidth of the different redundant paths. 
Timing and Synchronization 
Note 
Timing is relevant only when ETX-2i, ETX-2i-B, ETX-2i-10G-B, ETX-2i-10G-E, or 
ETX-2i-10G are ordered with the appropriate timing options. ETX-2i-100G/4Q, 
ETX-2i-100G/40G, and ETX-2i-10G-B half 19-inch do not support timing. 
The unit’s SyncToP™ suite includes clock recovery using IEEE 1588v2 Precision Timing Protocol, 
Synchronous Ethernet (SyncE), and a built-in input/output clock interface.  
The ETX-2i domain (system) clock is selected from up to two user-configurable sources. Each source can 
be an Ethernet port (recovered SyncE clock), the station clock, the internal GPS (for device with GNSS), 
or the recovered 1588v2 clock (i.e., 1588v2 slave clock; relevant only for devices without GNSS).  
The clock selection mechanism (CSM) selects the best clock according to its quality level (by SSM) and 
configured priority. The selected domain clock and its quality level are distributed to all Ethernet ports 
(Tx SyncE and SSM) and is the reference clock for the 1588v2 master. 
ETX-2i Devices 
1. Introduction 
The Network Time Protocol (NTP) provides the means of synchronizing all managed elements across the 
network to a reliable clock source provided by multiple servers. ETX-2i supports the client side of NTPv4 
(RFC 5905). 
ETX-2i, ETX-2i-B, ETX-2i-10G, ETX-2i-10G-B/8SFPP and ETX-2i-10G-E, ordered with the timing option 
(PTP), support the following features: 
• 
Clock selection mechanism to select and distribute the device system clock, including the 
holdover mechanism 
• 
SyncE 
• 
1588 slave 
• 
1588 BC 
In this option, the device also provides these additional timing ports: 
• 
Station clock port (RJ-45) 
• 
ToD/1PPS RS-422 port (RJ-45)  
• 
SMA port supplying external clock 
• 
SMA port supplying 1 pps 
• 
G.8275.2  
• 
ETX-2i-10G_TA/12SFP12UTP, ETX-2i-10G /12SFP12UTP, and ETX-2i-10G-B/4SFPP/4S/4U/PTP 
support the following additional timing options: 
 
G.8275.1 BC Class C on fiber ports 
 
ESMC enhancements to support eSyncE per G.8264  
Management and Security 
ETX-2i access control lists (ACLs) are used to flexibly filter and mark incoming and management traffic. 
ETX-2i can be managed as follows: 
• 
Local management via ASCII terminal, connected to the V.24/RS-232 DCE control port. 
• 
Local management via dedicated out-of-band management port. 
• 
Remote management via an Ethernet port using Telnet, SSH, NETCONF, or RADview, RAD’s 
SNMP-based management system. 
ETX-2i Devices 
1. Introduction 
• 
Remote management using Point-to-Point Protocol over Ethernet (PPPoE) – establishes a 
management channel that a remote management system can use to send software and 
configuration files and manage ETX-2i. 
ETX-2i supports a variety of access protocols including CLI over Telnet, SNMP, NETCONF, and TFTP/SFTP. 
You can create databases and scripts of commonly used commands and easily apply them to multiple 
units in your infrastructure. 
To ensure client-server communication privacy and correct user authentication, ETX-2i supports the 
security protocols listed below: 
• 
SNMPv3 (provides secure access to the device by authenticating and encrypting packets 
transmitted over the network) 
• 
RADIUS (client authentication) 
• 
TACACS+ (client authentication) 
• 
SSH for Secure Shell communication session 
The ETX-2i DHCP client enables plug-and-play zero touch provisioning via standard TFTP functionality. 
This includes downloading the latest SW version and configuration files. 
ETX-2i provides integrated management for RAD’s smart SFP devices, allowing TDM over packet 
pseudowire services (using MiTOP devices), and Ethernet over TDM (using MiRICi devices). The following 
devices are supported: 
• 
MiRICi-E1/T1/E3/T3 
• 
MiTOP-E1/T1/E3/T3 
ETX-2i devices managed via Telnet, SSH, NETCONF and local terminal connections automatically save 
device configuration changes when this option is enabled. 
Monitoring and Diagnostics 
ETX-2i offers several types of diagnostic procedures: 
• 
Ping test – checks IP connectivity by pinging remote IP hosts. 
• 
In-service ICMP Echo ping test – checks the connectivity across Layer-2 service paths. 
• 
Trace route – quickly traces a route from ETX-2i to any other network device. 
 
 
ETX-2i Devices 
1. Introduction 
• 
Loopback tests: 
 
Layer-1 loopback performed at the PHY of the physical ports. When the loopback is active, 
the data forwarded to a port is looped from the Tx path to the Rx path, disrupting the traffic. 
This loopback cannot pass through Ethernet bridges. 
 
Layer-2/Layer-3 loopback on flows, with optional MAC and/or IP address swapping. When 
the loopback is active, ETX-2i can exchange the source and destination MAC/IP addresses of 
the incoming packets. This loopback passes through Ethernet bridges and routers and does 
not disrupt traffic flows that are not being tested. 
• 
Service activation tests: 
 
RFC-2544 traffic generator and analyzer 
 
L3 SAT for Layer-3 testing 
 
ITU-T Y.1564 traffic generator and analyzer for Layer-2 testing 
• 
Syslog – protocol that generates and transports event notification messages from the device to 
servers across IP networks. 
• 
Port mirroring – duplicates port traffic to a single destination port, where a traffic analyzer 
receives, records, and analyzes the traffic. 
Hardware-Based Ethernet OAM and Performance Monitoring 
Featuring ultra-fast, hardware-based processing capabilities, ETX-2i performs OAM and PM 
measurements in under 1 microsecond with maximum precision. The device has a comprehensive 
Ethernet OAM suite that includes Ethernet Service OAM (IEEE 802.1ag), Ethernet link OAM 
(IEEE 802.3-2005, formerly IEEE 802.3ah), and Performance Monitoring (ITU-T Y.1731), providing tools to 
monitor and troubleshoot an Ethernet network and quickly detect failures.  
Quality of Service (H-QoS) 
ETX-2i efficiently handles multi-priority traffic on a per-flow basis, with ultra-high capacity that enables 
simultaneous processing of multiple service flows. The device enables multi-criteria traffic classification 
as well as metering, policing, and shaping to help carriers rate-limit user traffic according to predefined 
CIR (committed information rate) and EIR (excess information rate) profiles. Additionally, 
ETX-2i, ETX-2i-B, ETX-2i-10G, ETX-2i-10G-B, ETX-2i-10G-E and ETX-2i-100G provide MEF 10.3 rank 
Policers, delivering high-scale multi-CoS services with hierarchical Quality of Service (HQoS).  
Enhanced quality of service is further supported by a hierarchical scheduling mechanism that combines 
strict priority (SP), weighted fair queue (WFQ), and best effort (BE) scheduling, to efficiently handle real-
time, premium, and best-effort traffic. Scheduling and shaping are supported at the EVC and port levels. 

## 1.2 New in This Version  *(p.53)*

ETX-2i Devices 
1. Introduction 
The queue mapping functionality associates user priorities (packet attributes) with egress queues. The 
marking functionality maps user priorities (packet attributes) and the packet color (green/yellow) to the 
SP priority (p-bit) and DEI. The user priority can be p-bit/DSCP or IP precedence. ETX-2i also supports 
mapping of L2-L4 packet attributes to CoS levels, which map accordingly to the appropriate queues 
(queue mapping), SP p-bits (CoS to SP p-bit marking) and envelope ranks, if applicable.   
ETX-2i also uses weighted random early detection (WRED) policy for intelligent queue management and 
congestion avoidance. Packet editing capabilities include IEEE 802.1ad Q-in-Q tagging and color-sensitive 
P-bit re-marking, which ensures metering continuity across color-aware and color-blind Metro networks. 
RADview Performance Management  
The Performance Management (PM) portal is an SLA assurance system that is part of the RADview 
management system, enabling real-time monitoring of Ethernet service performance by collecting KPI 
(key performance indicators) data from RAD devices. Measured metrics are based on ITU-T Y.1731 and 
include Frame Delay, Delay Variation, Frame Loss, and Availability. Latency and jitter results are based 
on round-trip measurements. It allows service providers to easily evaluate actual performance over time 
and compare it to their committed SLA guarantees. In addition, it enables immediate detection of 
service degradation, so that remedial actions are taken to quickly restore performance levels. 
 
Note 
In order to ensure discovery of the Ethernet services by RADview, you need to 
assign a service name to the relevant flows, as well as ensure that collecting 
performance monitoring data is enabled for the relevant flows, services, and 
destination NEs.  
1.2 New in This Version 
The following features have been added with versions 6.8.5 (1.108), 6.8.5 (1.116), 6.8.5 (1.120),  
6.8.5 (1.143) and 6.8.5 (1.150): 
 
New Feature 
Comments 
Enclosure, Cards 
and Ports 
ETX-2i-10G-E platform. 
6.8.5 (1.116) 
Relevant for ETX-2i-10G-E/AC/8.5/8P 
Product Options in Chapter 1, 
Installation and Operation 
ETX-2i Devices 
1. Introduction 
New Feature 
Comments 
Automatically enable or disable FEC depending 
on the specific transceiver in use. 
6.8.5 (1.108) 
Relevant for ETX-2i-100G/4Q 
Configuring Ethernet Port Parameters 
in Chapter 2, Feature Reference 
Self-tuning, wavelength (WL) settings coherent 
100G QSFP28. 
6.8.5 (1.108) 
Relevant for ETX-2i-100G/4Q 
Configuring Ethernet Port Parameters 
in Chapter 2, Feature Reference 
Hardened 100GBase QSFP28-11DH LR1 and 
QSFP28-5DH ZR transceivers. 
6.8.5 (1.108) 
Relevant for ETX-2i-100G/4Q 
Management and 
Security 
Interactive login option that prompts the user to 
enter the SFTP password manually, in addition to 
the existing non-interactive option of passing the 
password in the command line 
6.8.5 (1.150) 
Downloading the New Device 
Software Release File in Chapter 2, 
Installation and Operation. 
SSH TACACS login based on X.509 Certificate 
Authentication. 
6.8.5 (1.143) 
Authentication via TACACS+ Using 
X.509 Certificates in Chapter 3, 
Feature Reference 
Extending support from 32 to 64 management 
ACRs (ACL Rules) 
6.8.5 (1.108) 
Applicability and Scaling in Chapter 3, 
Feature Reference 
Monitoring and 
Diagnostics 
PM (Performance Management) interval file 
mechanism. 
6.8.5 (1.120) 
Interval PM File in Chapter 12, 
Monitoring and Diagnostics 
L3 SAT responder functionality that allows the 
responder to use the Loaned IP Address 
parameter on the client router. 
6.8.5 (1.108) 
Relevant for IPv4 and the following 
devices: 
ETX-2i-10G-B/8SFPP,  
ETX-2i-10G (none B) 
Configuring L3 SAT Entities in Chapter 
8, Feature Reference 
UNI to NNI policer at the L3 SAT responder path. 
6.8.5 (1.108) 
Relevant for ETX-2i-10G-B/8SFPP 
Configuring L3 SAT Entities in Chapter 
8, Feature Reference 

## 1.3 Product Description  *(p.55)*

ETX-2i Devices 
1. Introduction 
New Feature 
Comments 
SFP events and alarms that include mismatch 
alarm and SFP status with thresholds. 
6.8.5 (1.108) 
Enhanced Y.1564 responder to support a 
compensated bandwidth policer at the 
responder test path. 
6.8.5 (1.108) 
Configuring Y.1564 Test in Chapter 8, 
Feature Reference 
1.3 Product Description 
Hardware Description 
The following figures show the ETX-2i devices (additional product variants exist). 
• 
Top – ETX-2i-10G (half 19-inch) 
• 
Middle – ETX-2i-B branch office device 
• 
Bottom – ETX-2i 
 
The following figure shows the ETX-2i-10G full 19-inch device with four SFP+, 12 SFP, 12 UTP, PTP, and 
two DC power supplies. 
ETX-2i Devices 
1. Introduction 
The following figure shows the ETX-2i-10G-B/4SFPP full 19-inch device with four SFP+, four SFP, four 
UTP, PTP, and integrated AC and DC power supplies. 
 
The following figures show the following: 
• 
ETX-2i-10G-B/8SFPP with eight SFP+ ports in full 19-inch enclosure with PTP (left-to-right 
airflow) 
• 
Full 19-inch NEBS enclosure (front-to-back airflow) 
• 
Half 19-inch enclosures. 
 
ETX-2i Devices 
1. Introduction 
 
The following figure shows the ETX-2i-10G-B/8SFPP Outdoor unit. 
 
The following figure shows the ETX-2i-10G-B/8SFPP/CD Outdoor unit. 
ETX-2i Devices 
1. Introduction 
 
The following figure shows the ETX-2i-10G-E 8.5-inch device with 8 SFP. 
 
The following figure shows the ETX-2i-100G/4Q device with four QSFP28, 8 SFP28, and 8 SFP+ ports. 
 
Refer to the Installation and Setup chapter for a detailed description of the ETX-2i interface 
connections. 
Functional Description 
The following figure shows the data flow in the device.  
ETX-2i Devices 
1. Introduction 
EVC 1
EVC 2
EVC n
WFQ
Shaping
Scheduling 
(WFQ, SP, 
BE)
EVC 1
EVC n
CoS/Queue
Mapping
Flow: Video 
CIR/EIR
Policing
CoS/Queue
Mapping
Flow: Data 
CIR/EIR
Policing
Shaping
CoS/Queue
Mapping
Flow: Voice 
CIR/EIR
Policing
CoS/Queue
Mapping
Flow: Mngt. 
CIR/EIR
Policing
CoS/Queue
Mapping
Flow: Clock 
CIR/EIR
Policing
Shaping
Classification
Color
Mapping
Color
Mapping
Color
Mapping
Color
Mapping
Color
Mapping
VLAN 
Editing
VLAN 
Editing
VLAN 
Editing
VLAN 
Editing
VLAN 
Editing
Scheduling 
(WFQ, SP, 
BE)
 
Data Flow Including Scheduling and Shaping at Level 0 and 1  
The following table provides an overview of the traffic handling stages. 
Processing Stage 
Description 
Classification  
Classifying traffic by flows per EVC/EVC.Cos 
CoS/queue mapping 
Mapping traffic to queues by packet attributes (or to a specific queue). 
Another method to map traffic to queues is by internal Cos assignment; used in 
certain configuration scenarios. 
Color mapping 
Mapping traffic to ingress color by packet attributes (or to a specific color) 
Policer per Flow or Group of 
Flows 
Policing the traffic of the flow or group of flows. 
If color aware Policer, uses the packet ingress color as set by color mapping. 
VLAN Editing  
Performing VLAN manipulations, such as push s-tag, pop, mark, and more, as 
well as marking the p-bit and DEI on the outer VLAN header (per packet 
attribute or internal CoS). 
Queues 
Egress traffic buffered into configurable size queues. Congestion avoidance 
policy is per color: 
• Green packets – tail drop 
• Yellow packets – per WRED profile 
Scheduling and Shaping at 
Level 0 (EVC Level) 
Scheduling the various queues to transmit per queue priority and weight 
Shaping the aggregate EVC traffic 
Scheduling and Shaping at 
Level 1 (Port Level)  
Scheduling the various queues to transmit per queue priority and weight 
 

## 1.4 Technical Specifications  *(p.60)*

ETX-2i Devices 
1. Introduction 
1.4 Technical Specifications 
Interfaces 
1GbE Interfaces 
The following table summarizes the ETX-2i 1GbE products. 
Specifications 
ETX-2i 
Fixed Ports 
 
ETX-2i 64E1 
 
ETX-2i-B 
 
 
ETX-2i-B D-NFV 
 
FE/GbE SFP  
8 SFP, UTP combo 
6 SFP, UTP combo 
4, 6 or 10 SFP,  
UTP combo 
Port 1, SFP only 
6 SFP (Ports 1 and 2), 
copper  
(Ports 3 to 6), RJ-45 
Network interface 
module 
– 
– 
– 
– 
1GbE Fiber Optic (SFP-based) 
 
1000BASE-SX, 1000BASE-LX, 100BASE-FX (full 
duplex only) 
10/100/1000BASE-T (full duplex only) 
Electrical Operation Mode 
 
10/100 Mbps or 10/100/1000 Mbps, full 
duplex, auto-negotiation, MDI/MDIX 
Connector 
SFP slot or RJ-45; LC 
combo 
 
 
 
E1/T1/T3 
– 
64 TDM PW E1/T1 ports – 
– 
Router (embedded) + (8G) 
+ (8G) 
+ (4G) 
+(4G) 
SHDSL module 
– 
– 
– 
– 
VDSL2 module 
– 
– 
– 
– 
E1/T1/T3/STM-1/OC3 EoPDH 
 
Via integrated Smart SFP (MiRIC) 
E1/T1/T3 PW services  
 
Via integrated Smart SFP (MiTOP) 
Timing  
2 MHz, 2 Mbps, 
1PPS, ToD 
– 
2 MHz, 2 Mbps, 
1PPS, ToD 
– 
 
ETX-2i Devices 
1. Introduction 
Note 
It is strongly recommended to order this device with original RAD optical 
transceivers. RAD cannot guarantee full compliance with product 
specifications for units using non-RAD transceivers. For full details on optical 
transceivers, see the Pluggable Transceivers data sheet. 
10GbE Interfaces 
The following table summarizes the ETX-2i 10GbE products. 
Specifications 
ETX-2i-10G/4SFPP 
(4+24) 
 
ETX-2i-10G-B/ 
4SFPP (4+8), 
ETX-2i-10G/ 
4SFPP (4+8) 
 
ETX-2i-10G-B/8SFPP 
ETX-2i-10G/8SFPP 
 
ETX-2i-10G-
E/8.5/8SFPP 
 
ETX-2i-10G/ 
8SFPP/ODU 
ETX-2i-10G-B/ 
8SFPP/ODU 
ETX-2i-10G/ 
8SFPP/ODU/CD 
 
 
1/10GbE SFP+ 
(with 1G/10G 
multirate 
support) 
4 SFP+ 
 
8 SFP+ 
8 SFP ports 
1/10GbE Fiber 
Optic 
(SFP+-based) 
 
 
1000BASE-LX/SX 
1/10GBASE-SR/LR/ER/ZR 
FE/GbE SFP   
12 or 24 SFP,  
12 ports SFP/RJ-45 
combo 
4 SFP and 4 UTP,  
8 SFP, or 4 SFP only 
 
 
8 GbE 
 
1GbE Fiber 
Optic 
(SFP-based) 
1000BASE-SX (MM 850nm),  
1000BASE-LX (SM 1310nm),  
100BASE-FX, 1000BASE-T 
 
 
1000BASE-SX, 
1000BASE-LX, 
1000BASE-T 
E1/T1/T3/STM-
1/OC-3  
 
 
Via integrated Smart SFP (MiRIC) 
E1/T1/T3 PW  
 
 
Via integrated Smart SFP (MiTOP) 
ETX-2i Devices 
1. Introduction 
Specifications 
ETX-2i-10G/4SFPP 
(4+24) 
 
ETX-2i-10G-B/ 
4SFPP (4+8), 
ETX-2i-10G/ 
4SFPP (4+8) 
 
ETX-2i-10G-B/8SFPP 
ETX-2i-10G/8SFPP 
 
ETX-2i-10G-
E/8.5/8SFPP 
 
ETX-2i-10G/ 
8SFPP/ODU 
ETX-2i-10G-B/ 
8SFPP/ODU 
ETX-2i-10G/ 
8SFPP/ODU/CD 
 
 
Timing  
 
 
2 MHz, 2 Mbps, 1PPS, ToD (In ETX-2i-10G-
B/8SFPP/ODU, connectors are internal) 
GNSS 
– 
SMA 
 
TNC 
CLI serial port 
Mini USB 
Micro USB 
 
RJ-45 
 
Note 
• 
It is strongly recommended to order this device with original RAD 
SFP/SFP+ transceivers. RAD cannot guarantee full compliance to product 
specifications for units using non-RAD transceivers. For full details on 
SFP/SFP+ transceivers, see the Pluggable Transceivers data sheet. 
• 
ETX-2i-10G offers license-based activation of the 10G/1G (SFP+) ports. 
ETX-2i-10G may be ordered with zero, two, four, or eight 10G activated 
SFP+ ports. The 10G ports may be field activated by purchasing a 10G port 
activation license. Non-activated SFP+ ports are limited to operation at 1 
Gbps. Activated SFP+ ports allow both 1G and 10G operation. 
100GbE Interfaces 
The following table summarizes the ETX-2i 100GbE products. 
Specifications 
ETX-2i-100G/4Q 
ETX-2i-100G/40G 
100GbE QSFP28 
4 
2 
40GbE QSFPP 
– 
2 
1/10/25GbE SFP28 
8 
- 
ETX-2i Devices 
1. Introduction 
Specifications 
ETX-2i-100G/4Q 
ETX-2i-100G/40G 
1/10GbE SFP+ (with 1G/10G 
multirate support) 
8 x 1000BASE-LX/SX 
1/10GBASE-SR/LR/ER/ZR 
16 x 1000BASE-LX/SX 
1/10GBASE-SR/LR/ER/ZR 
E1/T1/T3/STM-1/OC-3  
Via integrated Smart SFP (MiTOP) 
Via integrated Smart SFP (MiTOP) 
E1/T1/T3 PW  
2 MHz, 2 Mbps, 1PPS, ToD 
2 MHz, 2 Mbps, 1PPS, ToD 
GNSS 
SMA (HW ready) 
– 
Connector 
SFP slot or RJ-45; LC combo 
SFP slot or RJ-45; LC combo 
E1/T1/T3 
64 TDM PW E1/T1 ports 
4/8 EoPDH E1/T1 network ports 
Timing  
2 MHz, 2 Mbps, 1PPS, ToD 
2 MHz, 2 Mbps, 1PPS, ToD  
(excluding D-NFV option) 
D-NFV and Modular x86 Interface 
Provided with ETX-2i and ETX-2i-B. 
ETX-2i 
ETX-2i-B 
Processors and 
Cores 
Intel® Xeon-D D-1517 – four cores 
Intel® Xeon-D D-1537 – eight cores 
Intel® Atom Rangeley C2558 – four cores 
Intel® Atom Rangeley C2758 – eight cores 
Core Frequency 
Intel® Xeon-D D-1517 – 2.2GHz 
Intel® Xeon-D D-1537 – 2.3GHz 
2.4GHz 
Hard Drive 
Type: SSD 
Volume: Intel® Xeon-D D-1517 – 128GByte 
               Intel® Xeon-D D-1537 – 256GByte 
Type: SSD M2.0/2.5-inch format 
Volume: 128GByte with or without PLP 
RAM 
Intel® Xeon-D D-1517 – 16GByte ECC 
Intel® Xeon-D D-1537 – 24GByte ECC 
8GByte 
Connectors 
USB: USB 2.0 type A port, master architecture 
Console: RS-232 terminal interface 
 
 
ETX-2i Devices 
1. Introduction 
E1/T1 Interfaces (TDM Pseudowire) 
(ETX-2i/64E1: built-in TDM PW E1/T1 ports) 
Operation Mode 
GFP – single VCG 
Number of Ports 
64 
Compliance 
E1: G.703, G.732N, G.732S 
T1: ANSI T1.101, ANSI T1.403 
Data Rate 
E1: 2.048 Mbps 
T1: 1.544 Mbps 
Line Coding 
E1: HDB3 
T1: B8ZS 
Framing 
E1: Framed (G.732N with or without CRC)  
      Framed with CAS (G.732S with or without CRC) 
      Unframed 
T1: Unframed or ESF 
Impedance 
E1: 120Ω, balanced 
      75Ω, unbalanced (via adapter cable) 
T1: 100Ω, balanced 
Connectors 
Electrical, RJ-45 
Operation Mode 
GFP – single VCG 
Payload Encapsulation 
CESoPSN, SAToP 
Network Encapsulation 
MEF 8, UDP/IP 
Number of PWs 
128 
ETX-2i Devices 
1. Introduction 
PTP Interface (optional) 
Station Clock (ETX-2i, ETX-2i-10G, ETX-2i-10G-E, ETX-2i-10G-B full 19-inch) 
Mode 
Input and output 
Bit Rate 
2.048 MHz/2.048 Mbps (E1) 
Line Code   
AMI/HDB3 
Nominal Impedance 
120Ω balanced 
75Ω unbalanced (via adapter cable) 
Connector 
RJ-45 shielded 
ToD/1PPS (ETX-2i, ETX-2i-10G, ETX-2i-10G-E, ETX-2i-10G-B full 19-inch) 
Mode 
Output  
Line/connector 
RS-422 RJ-45 (NMEA 0183)   
 
 
ETX-2i Devices 
1. Introduction 
1PPS (ETX-2i, ETX-2i-B, ETX-2i-10G, ETX-2i-10G-E, ETX-2i-10G-B full 19-inch) 
Mode 
Output  
Signal type  
Square wave 
Amplitude 
2.0 Vpp (5.0 unloaded) 
Nominal Impedance 
50Ω unbalanced 
Connector 
DIN 1.0/2.3 
External Clock (ETX-2i, ETX-2i-10G, ETX-2i-10G-E, ETX-2i-10G-B full 19-inch) 
Mode 
Output  
Signal type  
Square wave 
Bit Rate 
2.048 MHz 
Amplitude 
2.0 Vpp (5.0 unloaded) 
Nominal Impedance 
50Ω unbalanced 
Connector 
DIN 1.0/2.3 
USB Interface 
Provided with ETX-2i and ETX-2i-10G 
Type 
USB2  
Rating 
5v/500 ma 
Protection 
Thermal shutdown 
Short circuit protection 
 
 
ETX-2i Devices 
1. Introduction 
Bridge 
Instances 
1 
Max. Number Bridge Ports 
ETX-2i, ETX-2i-B, ETX-2i-10G (half 19-inch): 80 
ETX-2i-10G (full 19-inch): 80 
ETX-2i-10G-B/8SFPP (full and half 19-inch): 80 
ETX-2i-10G-E/8SFPP: 128 
ETX-2i-100G/4Q: 24 
Max. Number MAC Table Entries (per 
device/per VLAN) 
ETX-2i: 32000 
ETX-2i-B, ETX-2i-10G (half 19-inch); ETX-2i-10G-B/4SFPP (full and half 
19-inch): 8000 
ETX-2i-10G-B/8SFPP (full and half 19-inch, Outdoor): 2000 
ETX-2i-10G-B/8SFPP (full and half 19-inch, high scale): 8000 
ETX-2i-10G-E/8SFPP: 8000 
ETX-2i-10G (full 19-inch), ETX-2i-100G: 16000 
Max. Number Broadcast Domains 
(VLANs)  
ETX-2i: 128 
ETX-2i-B, ETX-2i-10G-B/8SFPP (full and half 19-inch), ETX-2i-10G-E: 40 
ETX-2i-10G (half 19-inch), ETX-2i-10G-B (full and half 19-inch): 150 
ETX-2i-10G (full 19-inch), ETX-2i-100G: 300 
Max. Frame Size 
9600 bytes 
Compliance 
IEEE 802.1D, 802.1Q, 802.1ad 
Operation Mode 
VLAN-aware, VLAN-unaware 
VLAN Editing 
Inner/outer VLAN editing per VLAN and p-bit values 
Flows 
Flow Classification  
Rules 
Outer VLAN or outer + inner VLAN 
PCP 
TOS/DSCP 
EtherType 
IP/MAC source/destination address 
ETX-2i Devices 
1. Introduction 
Flows 
Max Number Flows / Classification Profiles 
ETX-2i:1000  
ETX-2i-B, ETX-2i-10G (half 19-inch), ETX-2i-10G-B/4SFPP (full and half 
19-inch), ETX-2i-10G-B/8SFPP (full and half 19-inch, Outdoor): 2000 
ETX-2i-10G (full 19-inch), ETX-2i-100G: 1860 per device; 930 per group 
ETX-2i-10G-E: 2000 
Max. Number Classification Matches per Device 
ETX-2i, ETX-2i-B, ETX-2i-10G (half 19-inch): 4000  
ETX-2i-10G-B/8SFPP: 4000, 2000 for ports 1-4; 2000 for ports 5-8. 
ETX-2i-10G (full 19-inch): 930 matches for ports 3-16; 930 matches for 
ports 1-2, 17-28 
Note: In ETX-2i-10G (full 19-inch), classification matches may also be a 
scaling factor. 
ETX-2i-100G/4Q: 930 matches for ports 3/1-3/2 (100G); 930 matches 
for all other ports 
Max. Number Flow Classification ACLs: 256 
Max. Number Classification Matches (rules) per Profile: 30 
Max. Number Flows in a Unidirectional Hub: 5 
Max. Number Unidirectional Hubs per Device: 7 
Port Classification 
Per port  
5-tuple ACL 
Maximum port classification matches: 
ETX-2i: 768 
ETX-2i-64E1: 500 
ETX-2i-B, ETX-2i-10G (half 19-inch, full 19-inch): 300 
Note: ETX-2i-100G does not support port classification. 
Max. Number Port Classification Matches per Rule: 5 
 
 
ETX-2i Devices 
1. Introduction 
Networking Capabilities 
Services 
Ethernet E-LAN, E-Line, E-Tree 
MEF CE2.0 compliant 
Layer-2 services with available bandwidth 
Layer-2 Forwarding 
Jumbo frame support 
OAM 
CFM 
8021.1ag, Y.1731 
Max. Number MDs per Device  
ETX-2i, ETX-2i-B, ETX-2i-10G/4SFPP and ETX-2i-10G-B/4SFPP (4x10G + 
8x1G, full and half 19-inch), ETX-2i-10G/8SFPP and ETX-2i-10G-B/8SFPP 
(full and half 19-inch):  127 
ETX-2i-10G/4SFPP (4x10G + 24x1G, full 19-inch), ETX-2i-100G: 255 
Max. Number MAs per Device  
ETX-2i, ETX-2i-B, ETX-2i-10G/4SFPP and ETX-2i-10G-B/4SFPP (4x10G + 
8x1G, full and half 19-inch), ETX-2i-10G/8SFPP and ETX-2i-10G-B/8SFPP 
(full and half 19-inch): 127 
ETX-2i-10G/4SFPP (4x10G + 24x1G, full 19-inch), ETX-2i-100G: 255 
Max. Number MEPs per MA 
Up to eight (configuration on EVC.cos) 
Max. Number MEPs per Device 
ETX-2i, ETX-2i-B, ETX-2i-10G/4SFPP and ETX-2i-10G-B/4SFPP (4x10G + 
8x1G, full and half 19-inch), ETX-2i-10G/8SFPP and ETX-2i-10G-B/8SFPP 
(full and half 19-inch, Outdoor): 503 
ETX-2i-10G-E/8SFPP: 500 
ETX-2i-10G/4SFPP (4x10G + 24x1G, full 19-inch): 255 
ETX-2i-100G: 1024 
Max. Number Remote MEPs per Device  ETX-2i-B, ETX-2i-10G/4SFPP and ETX-2i-10G-B/4SFPP (4x10G + 8x1G, 
full and half 19-inch), ETX-2i-10G/8SFPP and ETX-2i-10G-B/8SFPP (full 
and half 19-inch), ETX-2i-10G-E/8SFPP: 2000 
ETX-2i, ETX-2i-10G/4SFPP (4x10G + 24x1G, full 19-inch): 1024 
ETX-2i-100G: 4000 
ETX-2i Devices 
1. Introduction 
Max. Number MD-level MIPs 
Eight 
Max. Number Services (CoS) per MEP 
Eight 
Max. Number Dest NEs (PM sessions – 
LM/DM pairs) per Device 
ETX-2i, ETX-2i-B, ETX-2i-10G/4SFPP and ETX-2i-10G-B/4SFPP (4x10G + 
8x1G, full and half 19-inch), ETX-2i-10G/8SFPP and ETX-2i-10G-B/8SFPP 
(full and half 19-inch, Outdoor), ETX-2i-10G-E/8SFPP: 256 
ETX-2i-10G/4SFPP (4x10G + 24x1G, full 19-inch): 511 
ETX-2i-100G: 1024 
Notes:  
• Loss Measurement (LM) can be LMM or SLM. 
• Single SLM session per Dest NE is supported. 
• Single Test ID per EVC.CoS and RMEP are supported. 
OAM TWAMP 
Max. Number TWAMP Entities 
(Controllers or Responders) 
Layer-2 E-Line service: three 
Layer-2 E-LAN service over bridge: seven 
Layer-3: 15 
Max. Number Sessions Per Device 
150 
Max. Rate Supported for TWAMP 
Sessions Per Device 
150 pps 
Max. Number Peers Supported for 
TWAMP Controllers 
15 (all devices except ETX-2i-10G) 
150 (ETX-2i-10G) 
Max. Rate Per Session 
10 pps 
PMC TWAMP (ETX-2i) 
Max. Number TWAMP Controllers 
64 
Max. Number TWAMP Responders 
Eight 
Max. Number Sessions  
3000 
ETX-2i Devices 
1. Introduction 
Max. Number Peers  
3000 
Max. Rate per TWAMP Session 
10 pps for Full TWAMP and TWAMP Light 
1 pps for ICMP Echo and UDP Echo 
Hierarchical Quality of Service (HQOS) 
Max. Number WRED Profiles 
8 
Max. Number Queue Group Profiles 
28 
Max. Number Queue Block Profiles 
80 
Max. Number Marking Profiles 
12 
Max. Number Queue Mapping Profiles 
12 
Max. Number Queue Blocks in Device 
ETX-2i, ETX-2i-B, ETX-2i-10G (half 19-inch), ETX-2i-10G-B/4SFPP (full 
and half 19-inch): 128 
ETX-2i-10G (full 19-inch), ETX-2i-100G/4Q: 250 
ETX-2i-10G-B/8SFPP (full and half 19-inch, Outdoor): 64 
ETX-2i-10G-E/8SFPP: 240 
Max Number Queue Blocks per Port 
ETX-2i, ETX-2i-B, ETX-2i-10G (half 19-inch), ETX-2i-10G-B/4SFPP (full 
and half 19-inch), ETX-2i-10G-B/8SFPP (full and half 19-inch, outdoor): 
Network ports: 63; User ports: 8 
ETX-2i-10G-E/8SFPP: 
Network ports: 128, User ports: 8 
ETX-2i-10G (full 19-inch): Network port 0/1: 239; Network port 0/2: 80; 
all other ports: 8 
ETX-2i-100G/4Q: 3/1, 3/2 (100G ports): 128 per port; 2/1, 2/2 (10G 
ports): 116 per port; all other ports: 8 per port 
ETX-2i-100G/40G: 3/1, 3/2 (40G ports): 128 per port; 3/3, 3/4 (100G 
ports): 128 per port; all other ports: 8 per port 
Max Queue Size 
ETX-2i, ETX-2i-B, ETX-2i-100G: 16k (16383) frame buffers, 32 Mbytes 
ETX-2i-10G (full and half 19-inch), ETX-2i-10G-B: 4k (4095) frame 
buffers, 8 Mbytes 
ETX-2i Devices 
1. Introduction 
Total Frame Buffers 
ETX-2i, ETX-2i-10G (full 19-inch): 128k, 256 Mbytes 
ETX-2i-B, ETX-2i-10G (half 19-inch): 64k, 128 Mbytes 
ETX-2i-10G-B/8SFPP (full and half 19-inch, outdoor): 32k, 64Mbytes 
ETX-2i-100G/4Q: 64k, 128 Mbytes per port group  
ETX-2i-10G-E/8SFPP: 64k, 128 Mbytes 
Policing 
Color aware/unaware dual token bucket with user-configurable 
CIR + CBS and EIR + EBS; coupling flag support 
2-rate/3-color policing per EVC.CoS 
Bandwidth policing per MEF 10.3  
Hierarchical Envelope Policer per MEF 10.3 
MultiCoS EVCs per MEF 10.3  
Max number Policer instances 
ETX-2i, ETX-2i-10G (full 19-inch): 1000 
ETX-2i-B, ETX-2i-10G (half 19-inch), ETX-2i-10G-B/4SFPP (full and half 
19-inch), ETX-2i-10G-B/8SFPP (full and half 19-inch, Outdoor): 256  
ETX-2i-10G/8SFPP and ETX-2i-10G-B/8SFPP (full and half 19-inch, 
Outdoor): 1024 
ETX-2i-10G-E/8SFPP: 1016 
ETX-2i-100G/4Q: 1860 
Max number Policer profiles 
ETX-2i-B, ETX-2i-10G (full and half model), ETX-2i-10G-B/4SFPP (full 
and half 19-inch), ETX-2i-10G-B/8SFPP (full and half 19-inch, Outdoor), 
ETX-2i-100G: 256  
ETX-2i-10G/8SFPP and ETX-2i-10G-B/8SFPP (full and half 19-inch, 
Outdoor): 1024 
ETX-2i-10G-E/8SFPP: 1016 
ETX-2i: 1000 (envelope/regular/aggregate); up to 250 different profiles 
Max. Policer Aggregates: 160 
Max. Flows per Policer Aggregate: 100 
Large flow policing (Fat pipe) – ETX-2i-10G/4SFPP, ETX-2i-10G/4SFPP; 
ETX-2i-10G-B/8SFPP ports 1-4; ETX-2i-100G/4Q user ports,  
ETX-2i-100G/40G user ports 
ETX-2i Devices 
1. Introduction 
Envelope Policer 
Max. Number Envelope Profile Instances: 
ETX-2i: 
4-rank mode: 250 
8-rank mode: 125 
ETX-2i-B, ETX-2i-10G (half 19-inch), ETX-2i-10G-B/4SFPP (full and half 
19-inch), ETX-2i-10G-B/8SFPP (full and half 19-inch, Outdoor): 
4-rank mode: 64 
8-rank mode: 32 
ETX-2i-10G-B/8SFPP and ETX-2i-10G-B/8SFPP (full and half 19-inch, 
Outdoor):  
4-rank mode: 256 
8-rank mode: 128 
ETX-2i-10G-E/8SFPP: 
4-rank mode: 254 
8-rank mode: 126 
ETX-2i-10G (full 19-inch):  
4-rank mode: 1000 
8-rank mode: 500 
ETX-2i-100G/4Q:  
4-rank mode: 500 
8-rank mode: 250 
Max. Number Ranks in Envelope Policer: 
4 or 8 (user configurable at the device level) 
Max. Number Envelope Profiles: 
ETX-2i, ETX-2i-B, ETX-2i-10G (full and half models), 
ETX-2i-10G-B/4SFPP (full and half 19-inch), ETX-2i-10G-B/8SFPP (full 
and half 19-inch, Outdoor), ETX-2i-100G: 
4-rank mode: 512 
8-rank mode: 32 
Scheduling 
8 × CoS per EVC scheduling elements 
Strict Priority (SP) 
Weighted Fair Queue (WFQ) 
Shaping 
Per port  
Per EVC 
ETX-2i Devices 
1. Introduction 
Per EVC.CoS 
Max. number Shaper profiles: 128 
Management Router 
General  
Static router 
Management Router, e.g., host management, TDM PW, PTP, 
TWAMP, L3SAT  
VRFs 
(Router Instances) 
10 
PMC in ETX-2i: four 
Number of Router Interfaces 
ETX-2i, ETX-2i-B: 31  
ETX-2i-10G, ETX-2i-100G: 32 
PMC in ETX-2i: 64 
Notes:   
• Only one router interface is supported when working 
with PWs. 
• Only two router interfaces can be configured for 
management. 
• In PMC, one router interface can be shared between the 
TWAMP controller/responder and management access. 
Default 
Router 1, Router Interface 32 (ETX-2i-10G) 
Router 1, Router Interface 31 (ETX-2i, ETX-2i-B, ETX-2i-100G) 
IP address 169.254.1.1/1 
Supported functionalities 
Timing ports, bridge, Smart SFP MiTOP  
NTP Multicast client 
HW (Data) Router (ETX-2i, ETX-2i-B) 
General  
IPv4, IPv6, dynamic router 
Routing Protocols 
OSPFv2, BGPv4, NAT, DHCP Relay 
Protocols  
BFD, VRRPv3 
ETX-2i Devices 
1. Introduction 
VRFs 
(Router Instances) 
ETX-2i: 10 
ETX-2i-B: 5 
IPv4 Routing Table Entries 
ETX-2i: 4000 
ETX-2i-B: 2000 
IPv6 Routing Table Entries 
ETX-2i: 3500 
ETX-2i-B: 2000 
Router ACLs 
ETX-2i: 128 
ETX-2i-B: 64 
ARP table entries (IPv4 and IPv6) 
ETX-2i, ETX-2i-B: 256 
Management and Security 
Protocols and Security 
SSH (Secure CLI) 
Telnet  
SNMPv3  
SFTP 
NETCONF/YANG management interface  
Dual stack IPv4 and IPv6 routing (ETX-2i, ETX-2i-B) 
IP forwarding (ETX-2i, ETX-2i-B) 
Static routing 
Password-protected access 
Authorization levels 
RADIUS or TACACS+ authentication 
Access Control List (ACL) 
Large Deployments 
Plug and play zero touch provisioning (DHCP, PPPoE, XML 
configuration files download via TFTP/SCP) 
Configuration backup and restore 
 
 
ETX-2i Devices 
1. Introduction 
Management Options 
Local management via LAN port or serial port 
Remote management via inband VLAN 
Control Port 
Interface 
V.24/RS-232 DCE (optional native USB available for ETX-2i-100G/4Q) 
Connector 
Mini USB – ETX-2i, ETX-2i-B, ETX-2i-10G/4SFPP, ETX-2i-10G-B/4SFPP 
Micro USB – ETX-2i-10G-B/8SFPP, ETX-2i-100G/4Q, ETX-2i-100G/40G 
RS232 (RJ-45) – ETX-2i-10G-E/8SFPP, ETX-2i-10G-B/ODU/8SFPP 
Format 
Asynchronous 
Data Rate 
9.6 (default), 19.2, 38.4, 57.6, or 115.2 kbps (user configurable) 
Note: Data rates 38.4 and 57.6 are supported only after the device is up 
and running. 
Ethernet Management Port  
Type 
10/100BASE-T 
Connector 
RJ-45 (In ETX-2i-10G-B/ODU/8SFPP, the connector is internal.) 
Timing and Synchronization 
 
ETX-2i 
ETX-2i-B 
ETX-2i-10G,  
ETX-2i-10G-B, ETX-2i-10G-E 
ETX-2i-100G 
Best Master Clock 
Algorithm (BMCA) 
– 
– 
+ 
+ 
Clock Domains 
– 
– 
One (master and fallback) 
One (master and 
fallback) 
Clock Sources 
Up to two inputs for selection mechanism 
1588v2 recovered, station (BITS/GPS), ETH port Rx 
GNSS 
– 
– 
Connector: SMA (HW ready) 
Connector: SMA 
(HW ready) 
ETX-2i Devices 
1. Introduction 
ETX-2i 
ETX-2i-B 
ETX-2i-10G,  
ETX-2i-10G-B, ETX-2i-10G-E 
ETX-2i-100G 
IEEE-1588v2 
precision time 
protocol (PTP) per 
G.8265.1, G.8275.1, 
and G.8275.2 
Telecom profiles 
Transparent clock 
(TC) 
TC 
Ordinary clock (OC), TC, 
Boundary clock (BC), slave 
clock 
ETX-2i-10G-B/ 8SFPP: 
Grandmaster (GM) with 
integrated GNSS 
OC 
TC 
BC (Class C ready) 
Dual master 
operating 
simultaneously in 
G.8265.1 and 
G.8275.1 modes 
Phase and 
frequency 
synchronization 
 
Note 
Full IEEE-1588v2 support is available only if the unit was purchased with the 
/PTP or the /G ordering option. 
Resiliency 
Dual Homing 
Dual homed link redundancy; also known as Link Protection; IEEE 802.3ad 
Ethernet Path Protection 
G.8031 linear 1:1 protection, optionally using APS protocol 
Ethernet Ring 
G.8032v2 rings with sub 50 ms protection for Ethernet traffic 
Fault Propagation 
IEEE 802.1ag-D8, ITU-T Y.1731 
Hardware Redundancy 
IEEE 802.1ax (802.3ad) 1:1 LAG with LACP for pairs of network or user Ethernet ports 
Link  
Aggregation 
LAG with load balancing. Up to 4 ports in a LAG group on 10G ports. 
Diagnostics 
Alarm relay (optional) 
Type: Dry contacts with three “in”  
Connector: Terminal block, 9-pin 
Connectivity Fault Management (CFM) 
Per IEEE 802.1ag 
ETX-2i Devices 
1. Introduction 
Connectivity Verification Tools 
Ping, Trace Route 
Counters 
RMON2 port-level counters 
Delay and Loss Measurements 
Per MEF 36 
EFM Link-fault OAM 
Per IEEE 802.3ah 
ICMP Echo 
Over L2 and L3 services 
Tests IP connectivity (PING) 
KPI Measurements 
Accurate one-way KPI measurements 
Limiting Multicast Traffic Flooding 
DHCP and MLDv2 snooping 
Link-Level OAM 
Per IEEE 802.3-2005 
LLDP Discovery 
Per IEEE 802.1AB 
Loop Prevention 
Using MSTP and RSTP 
Loopback Tests 
Non-disruptive loopback per flow, with MAC/IP address swap 
Loopbacks at Ethernet port level 
On-demand Layer-2 and 3 loopbacks 
Service Activation  
Tests 
RFC-2544: 8 built-in wirespeed testers 
ITU-T Y.1564: 8 built-in wirespeed testers 
Service Utilization and Performance 
Monitoring 
Per ITU-T Y.1731.2012, including synthetic loss measurement 
TWAMP 
RFC 5618 TWAMP responder and receiver 
TWAMP sender 
RFC 5357 TWAMP – Light generator and responder (SW license) 
ITU-T Y.1731 PM (SLM; DM) 
PM Controller (PMC) (ETX-2i) 
ETX-2i Devices 
1. Introduction 
General 
Compliance 
CE 
CE 2.0 
MEF 
MEF 9, MEF 10, MEF 14, MEF 20, MEF 36, MEF 46 
MEF 3: 
E-Access: Access EPL, Access EVPL 
E-LAN: EPLAN, EVPLAN 
E-Line: EPL, EVPL 
E-Tree: EP-Tree, EVP-Tree 
MEF 6: 
E-LAN: EPLAN, EVPLAN  
E-Line: EPL, EVPL 
IEEE 
802.3, 802.3u, 802.1D, 802.1Q, 802.1p, 802.3ad, 802.3ae, 802.3-2005, 
802.1ax, 802.1ag-D8 
ITU-T 
Y.1731, G.8031, G.8032v2, G.8262, G.8264, G.8265, RFC-2544, Y.1564, 
G.8273.2, G.8275.1, G.8275.2, 1588v2 
Environment 
Storage Temperature 
-40 to 85°C (-40 to 185°F) 
Operating Temperature 
ETX-2i, ETX-2i-10G, ETX-2i-10G-B, ETX-2i-10G-E, ETX-2i-100G regular: 
0 to 50°C (32 to 122°F) 
ETX-2i-B (1U): -5 to 55°C (23 to 131°F) 
Temperature hardened, NEBS: 
ETX-2i-B (2U), ETX-2i-100G: -20 to 65°C (-4 to 149°F) 
ETX-2i, ETX-2i/m, ETX-2i-10G, ETX-2i-10G-B temperature hardened, 
outdoor, NEBS: -40 to 65°C (-40 to 149°F); cold start above -20°C (-4°F) 
Note: In the temperature-hardened devices, a single SFP-30H is 
supported at temperature up to 62°C (143°F). 
Humidity 
5% to 90%, non-condensing 
ETX-2i Devices 
1. Introduction 
Fans 
ETX-2i-10G, ETX-2i-10G-B: Up to 4 
ETX-2i-10G-B/8SFPP/ODU: None 
ETX-2i-100G: 8 (simultaneous fan operation; automatic fan level 
control) 
Airflow 
ETX-2i-10G, ETX-2i-10G-B 19-inch enclosures: Left to right (unless 
otherwise specified) 
ETX-2i-10G, ETX-2i-10G-B Half 19-inch enclosures, ETX-2i-100G:  
Front to back  
ETX-2i-10G-B/8SFPP Outdoor: None (passive airflow) 
Physical 
8.5-inch Enclosures 
Height: 
ETX-2i, ETX-2i/m, ETX-2i-B 1U, ETX-2i-10G, ETX-2i-10G-B:  
43.7 mm (1.7 in) 
ETX-2i-B 2U: 88.2 mm (3.5 in) 
Width: 
ETX-2i, ETX-2i/m, ETX-2i-10G, ETX-2i-10G-B: 215.5 mm (8.5 in) 
ETX-2i-B metal: 220 mm (8.7 in) 
Depth: 
ETX-2i, ETX-2i/m, ETX-2i-10G, ETX-2i-10G-B: 301 mm (11.9 in) 
ETX-2i-B: 170 mm (6.7 in) 
Weight: 
ETX-2i/M: 2.16 kg (4.76 lb) maximum 
M (module): 0.91 kg (2.01 lb) 
ETX-2i-B 1U: 0.7 kg (1.54 lb) 
ETX-2i-B 2U: 1.34 kg (2.95 lb) 
ETX-2i-10G, ETX-2i-10G-B: 2.3 kg (5.1 lb) 
19-inch Enclosures 
Height:  
All indoor devices except ETX-2i 64E1: 43.7 mm (1.7 in) 
ETX-2i 64E1: 132.7 mm (5.2 in) 
Width: 440 mm (17.3 in) 
ETX-2i Devices 
1. Introduction 
Depth:  
ETX-2i, ETX-2i-10G, ETX-2i-10G-B: 240 mm (9.5 in) 
ETX-2i-10G-B/8SFPP NEBS: 300 mm (11.8 in) 
ETX-2i/M: 00 mm (11.8 in) 
ETX-2i-100G: 400 mm (15.8 in) 
Weight:  
ETX-2i Fixed Ports: 3.6 kg (7.9 lb) maximum 
ETX-2i 64E1: 7.15 kg (15.87 lb) maximum 
ETX-2i/M module: 0.91 kg (2.01 lb) 
ETX-2i-10G: 3.1 kg (6.8 lb) 
ETX-2i-10G-B with two power supplies: 3.8 kg (8.4 lb) 
ETX-2i-10G-B with one power supply: 2.5 kg (5.5 lb) 
ETX-2i-10G-B/8SFPP NEBS with two AC power supplies: 4.44 kg (9.8 lb) 
ETX-2i-100G with two power supplies: 7.4 kg (16.3 lb) 
ETX-2i-100G with one power supply: 6.6 kg (14.5 lb) 
Aluminum IP66 Outdoor Unit 
Enclosure  
Height: 465.0 mm (18.3 in) 
Width: 300.0 mm (11.8 in) 
Depth: 106 mm (4.2 in) 
Weight: 9.3 kg (20.5 lb) (when using two power supplies) 
Power 
All devices with SFPP ports support a power consumption of at least 2W per SFPP port and at least 1W 
per SFP port, although not all devices support the same temperature in this case. 
Some devices with MiTOP inserted support up to 1.5W per MiTOP port, but it affects the maximum 
temperature that the relevant devices can reach. 
 
 
ETX-2i Devices 
1. Introduction 
1GbE Devices 
The following table shows the power specifications for ETX-2i 1G devices. 
ETX-2i 
Fixed Ports 
 
ETX-2i 64E1 
 
ETX-2i/M & 
D-NFV 
 
ETX-2i-B 
 
 
ETX-2i-B D-NFV 
 
AC: 100-240 VAC (-10%, +6%), 50/60 Hz, 0.9A 
DC: 48 VDC (40-60 VDC), 2A 
ETX-2i, ETX-2i-B 8.5-inch – Dual DC feed 
ETX-2i-B - Wide-range AC/DC with auto detection 
+ 
+ 
+ 
+ 
- 
Non-modular 
product base 
(8 GbE): 35W (max) 
AC PS: 74W (max)  
DC PS: 60W (max) 
Modular base: 30W 
Modular uplink: 5W 
VDSL: 10Wmax) 
D-NFV: 30W 
23W 
30W 
10GbE Devices 
The table below shows the power specifications for ETX-2i 10G devices. 
Power Spec 
ETX-2i-10G/ 
4SFPP (4+24) 
 
 
 
ETX-2i-10G-B/ 
4SFPP (4+8) 
ETX-2i-10G/ 
4SFPP (4+8) 
 
ETX-2i-10G-B/ 
8SFPP 
ETX-2i-10G/ 
8SFPP 
 
 
 
ETX-2i-10G-
E/8.5/8SFPP 
 
 
 
ETX-2i-10G-
B/8SFPP/ODU 
ETX-2i-
10G/8SFPP/ODU 
ETX-2i-10G/ 
8SFPP/ODU/CD 
 
 
Power 
Supply 
AC: 100-240 VAC nominal (-10%, +6%), 50/60 Hz, 0.9A 
DC: -48 VDC (40-60 VDC), 2A 
DC: 24 VDC (20-60 VDC), 2A for ETX-2i-10G/8SFPP and ETX-2i-10G-B/8SFPP in the US only 
ETX-2i Devices 
1. Introduction 
Power Spec 
ETX-2i-10G/ 
4SFPP (4+24) 
 
 
 
ETX-2i-10G-B/ 
4SFPP (4+8) 
ETX-2i-10G/ 
4SFPP (4+8) 
 
ETX-2i-10G-B/ 
8SFPP 
ETX-2i-10G/ 
8SFPP 
 
 
 
ETX-2i-10G-
E/8.5/8SFPP 
 
 
 
ETX-2i-10G-
B/8SFPP/ODU 
ETX-2i-
10G/8SFPP/ODU 
ETX-2i-10G/ 
8SFPP/ODU/CD 
 
 
Power 
Supply 
Redundancy 
+ 
Power 
Consumption 
120W (max) 
110W (aver) 
100W (min) 
ETX-2i-10G/4SFPP  
8.5-inch enclosure:  
90W (max) 
72W (aver) 
65W (min) 
ETX-2i-10G/4SFPP 
19-inch enclosure:  
95W (max) 
ETX-2i-10G-B/4SFPP 
19-inch enclosure: 
95W (max) 
75W (max) 
70W (aver) 
35W (max) 
AC: 87W (max) 
DC: 67W (max) 
 
 
ETX-2i Devices 
1. Introduction 
100GbE Devices 
The following table shows the power specifications for ETX-2i-100G/4Q devices. 
Power Supply 
Hot swappable, redundant AC or DC PS, no mix 
AC: 100-240 VAC nominal (±10%), 2.5A/1A, 50/60 Hz 
DC: 48 VDC (40-60 VDC), 5A 
Power Consumption 
ETX-2i-100G/4Q: 200-250W (max) 
 
 120W (average) 
 
 100W (minimum) 
 
 Up to 5.5W per QSFP28 slot 
 
 2W per SFPP slot (at 0-50°C working temperature) 
 