# ETX-2i (1G devices) IP and Carrier Ethernet Demarcation with D-NFV

<!-- datasheet product=etx-2i-1g family=etx2 kind=system source=etx-2i_1g_ds_0.pdf -->

*Datasheet `etx-2i_1g_ds_0.pdf`, 9 pages. Product `etx-2i-1g`, family `etx2` (system).

## ETX‑2i (1G devices) IP and Carrier Ethernet Demarcation with D‑NFV  *(p.1)*

- Feature-rich demarcation and aggregation suite,
offering a complete Service Assured Access (SAA)
solution, line rate Layer-3 services, and vCPE
applications
- Ideal for service providers, wholesalers, and mobile
operators, seeking to deliver and monitor SLA-based
MEF-certified CE 2.0, Layer-3 VPN, and TDM over PSN
- Versatile offering of Ethernet over fiber, SHDSL, VDSL,
GPON, PDH, and TDM, assuring unified service delivery
over any access technology
- TWAMP and Layer-2 OAM, diagnostics for scalable and
accurate traffic monitoring, quick fault detection, and
troubleshooting of Layer-2 and Layer-3 networks
FLEXIBLE SERVICE DELIVERY AND ASSURANCE AT 1G
The ETX-2i IP and Carrier Ethernet Demarcation with D‑NFV
device is the main component of RAD’s Service Assured Access
solution, providing:
- Ethernet service uniformity over multiple access technologies
including GbE, SHDSL, VDSL, PDH, and SONET/SDH
- Operation in diverse topologies including ring, daisy chain,
and hub and spoke
- PW functionality for mobile backhauling and business services
- Synchronization for mobile 2G, 3G, LTE, and LTE-A
backhauling networks
- Network Function Virtualization (NFV) for vCPE solutions
ETX‑2i is offered in a variety of product options: ETX-2i, ETX-2i-B,
ETX-2i-10G, and ETX-2i-100G. (Details on ETX-2i 10G devices and
ETX-2i 100G devices can be found in dedicated data sheets.)
ETX-2i is a next-generation hybrid L2 and L3 demarcation device.
The ETX-2i-B branch office device is an optimized access box
adapted to the requirements of next-generation vCPE networks.
The tables below provide further information on the capabilities
offered by the ETX-2i and ETX-2i-B devices.
MARKET SEGMENTS AND APPLICATIONS
ETX‑2i is ideal for carriers, service providers, municipalities,
wholesale providers, and mobile operators seeking to offer
unified SLA-based Ethernet business services, such as E-Line,
E-LAN, E-Tree, and E-Access, as well as L3 VPNs and value-added
services using virtualization at the customer edge.
INTEROPERABILITY
The ETX-2i family features and services are standard based and
can work with any 3rd party equipment using standard based
features and services.
NETWORK TOPOLOGIES
ETX‑2i supports several network topologies such as linear, daisy
chain, and self-healing rings (G.8032v2), working with ETX-5 or
third-party Ethernet devices.
CARRIER ETHERNET 2.0 SERVICES
ETX‑2i incorporates a complete set of CE 2.0-certified Ethernet
service tools that allow service providers to distinguish between
high- and low-priority traffic and optimize TCP sessions.
ETX‑2i provides MEF 10.3 color aware and unaware Policers,
delivering high-scale multi-CoS services with hierarchical Quality
of Service (HQoS).
It supports advanced scheduling, WRED per CoS, shaping per
EVC, with flexible classification rules and access lists.
DHCP Snooping
ETX-2i supports DHCP Snooping with Option 82 for protection of
DHCP transactions.
Layer-2 Control Processing
ETX‑2i can be configured to forward or discard Layer-2 control
frames (including other vendors’ L2CP frames).
MEF Services
ETX‑2i delivers E-Line (EVL, EVPL), E-LAN (EPLAN, EVPLAN),
E-Tree (EP-TREE, EVP-TREE), and E-Access services compliant
with MEF 3.0 and CE 2.0 certifications.
MLDv2 Snooping
With MLDv2 snooping, multicast data is selectively forwarded
only to a list of self-learned ports (per multicast group
membership), instead of being flooded to all ports in a VLAN.

## ETX‑2i  *(p.2)*

VCPE
ETX-2i and ETX-2i-B leverage Network Functions Virtualization
(NFV), allowing carriers to provide a vCPE solution in various
models, including Centralized and Decentralized architectures.
This solution reduces CAPEX and OPEX by eliminating the
physical appliance required for hosting network functions.
The D-NFV options allow for seamless insertion of x86 cards as
optional modules. The D-NFV module hosts virtual machines
providing virtual network functions (VFs) or value-added service
capabilities. This enables service providers to quickly and easily
provide new services and implement new network capabilities,
with the benefit of function localization at the customer
premises.
ROUTING
ETX-2i and ETX-2i-B models with enabled routing offer Virtual
Routing and Forwarding (VRF) instances, allowing service
providers to deploy Layer-2 and Layer-3 VPNs. The forwarding
engine capability ranges from 1 to 8 Gbps, allowing Carrier
Ethernet and IP services to be offered in a single device providing
high-capacity performance monitoring, network function
virtualization (NFV), and more.
ETHERNET OVER IP/GRE
ETX-2i and ETX-2i-B models with enabled routing offer Ethernet
over IP/GRE tunneling, allowing service providers to extend
Layer-2 services to out of footprint sites over IP transport.
Access Aggregation with SLA-Based Services
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

## ETX‑2i  *(p.3)*

SDN READY MANAGEMENT
ETX‑2i can be managed via RADview, RAD’s carrier-class NMS, or
any SNMP-based management system. The device supports a
variety of access protocols, including CLI over Telnet, SNMPv3,
and TFTP.
Security features include SNMPv3, RADIUS (client
authentication), TACACS+ (client authentication, authorization,
and accounting), SSH, and SFTP.
Access Control Lists (ACL) can also be used to flexibly filter and
mark management traffic, enabling service providers to maintain
network security by dropping unwanted packets.
NETCONF/YANG
XML-based network configuration protocol NETCONF is
supported and provides an easy interface for NFV/SDN
orchestrators to install, manipulate, and delete the configuration
of ETX-2i.
Zero Touch
ETX‑2i implements RAD’s unique ZT process, allowing devices to
onboard automatically and securely without human intervention
and enabling operators to provision services easily and reliably.
TDM PSEUDOWIRE
ETX-2i 64E1 and ETX-2i/ETX-2i-B with smart SFP (MiTOP) provide
pseudowire (PWE) services. The PWs can be encapsulated using
CESoPSN per IETF RFC 5086 or SAToP per IETF RFC 4553.
ETHERNET OVER PDH
ETX‑2i provides Ethernet over PDH (EoPDH) services via a smart
SFP (RAD’s MiRICi), including the following NG-PDH technologies:
- Generic Framing Procedure (GFP G.7041)
- GFP or PDH (G.8040)
- PDH Virtual Concatenation (VCAT G.7043)
- Link Capacity Adjustment Scheme (VCAT G.7042).
NG-PDH solutions improve overall network availability by
reducing latency and optimizing line utilization and throughput.
Integrated management of MiRICi smart SFPs provides TDM
(E1/T1/E3/T3/OC-3/STM-1) connectivity over PDH or SDH legacy
networks.
RESILIENCY
ETX‑2i offers fast protection for virtually any kind of failure, in
any linear, ring, or dual-homed topology. The device employs
IEEE 802.3ad link aggregation (1:1 LAG), ITU-T G.8032v2 Ethernet
ring protection, and ITU-T G.8031 Ethernet linear protection, to
ensure continuous availability and sub-50 ms restoration in the
event of network outages.
It also provides MSTP and RSTP (IEEE 802.1Q) to support loop-
free bridge forwarding over mesh or ring physical topology.
Table 1. Interfaces
Specifications
ETX-2i
Fixed Ports
ETX-2i 64E1
ETX-2i/M &
D-NFV
ETX-2i-B
ETX-2i-B D-NFV
FE/GbE SFP
8 SFP/UTP combo
6 SFP/UTP combo
4 (2 additional with GbE module)
SFP/UTP combo
4, 6 or 10 SFP/UTP
combo
Port 1 SFP only
6 SFP (Ports 1
and 2)/copper
(Ports 3 to 6)
RJ-45
Network interface module –
–
+
–
–
D-NFV
–
–
19V ordering option
V ordering option
+
E1/T1/T3
–
64 TDM PW E1/T1
ports
4/8 EoPDH E1/T1 network ports
–
–
Router (embedded)
+ (8G)
+ (8G)
+ (8G)
+ (4G)
+(4G)
SHDSL module
–
–
+
–
–
VDSL2 module
–
–
+
–
–
E1/T1/T3/STM-1/OC3
EoPDH
Via integrated Smart SFP (MiRIC)
E1/T1/T3 PW services
Via integrated Smart SFP (MiTOP)
Timing
2 MHz, 2 Mbps,
1PPS, ToD
–
2 MHz, 2 Mbps, 1PPS, ToD
(excluding D-NFV option)
2 MHz, 2 Mbps,
1PPS, ToD
–
Note: It is strongly recommended to order this device with original RAD SFP/XFP transceivers. RAD cannot guarantee full compliance to product
specifications for units using non-RAD transceivers. For full details on SFP/XFP transceivers, see the Pluggable Transceivers data sheet.

## ETX‑2i  *(p.4)*

TIMING AND SYNCHRONIZATION
ETX‑2i incorporates RAD’s advanced SyncTop synchronization
and timing over the packet feature set to support mobile
heterogeneous network topology.
Synchronous Ethernet (SyncE) with IEEE 1588v2 Precision Time
Protocol per ITU-T G.8265.1, G.8275.1, and G.8275.2 telecom
profiles provide cost-effective synchronization of frequency and
phase. ETX‑2i also supports ordinary clock (OC), boundary clock
(BC), and transparent clock (TC), as well as a dual master
operating simultaneously in G.8265.1 and G.8275.1 modes. ETX-
2i utilizes the best master clock algorithm (BMCA) to select the
best clock from the ports that are provisioned as slave.
MONITORING AND DIAGNOSTICS
Featuring multi-layer OAM and PM tools, ETX‑2i offers
hardware-based monitoring and diagnostics at high scale and
precision. End-to-end connectivity OAM (IEEE 802.1ag), as well
as single-segment OAM (IEEE 802.3-2005), ensure flow-level
fault management and performance monitoring over Layer-2
networks and also quickly detect connectivity failures for robust
protection.
Layer-2 and 3 wirespeed loopbacks offer flexible diagnostic tools.
RFC-5357 TWAMP Light delivers the same functionality over
Layer-3 networks, as well as one-way TWAMP and two-way
ICMP Echo, with counters for loss, delay, fragmented packets,
reorders, and duplication, in addition to configurable test packet
size. Multi-VRF supports the robust TWAMP setup.
The Performance Management Portal is an SLA assurance system
that is part of the RADview management system, enabling
real-time monitoring of service performance.
Digital Diagnostics Monitoring
ETX‑2i supports digital diagnostics monitoring (DDM) SFP
functions according to SFF-8472, excluding external DDM
calibration.
Service Activation Tests
The ETX‑2i family offers service activation tools with multiple
RFC-2544, Y.1564, and L3 SAT testers.
VIRTUALIZATION ARCHITECTURE
The ETX-2i and ETX-2i-B D-NFV options are provided with RAD’s
vCPE-OS software platform on their D-NFV modules.
D-NFV module is a Linux based, carrier-class operating system for
vCPE applications, with open management interfaces. vCPE-OS
runs on any white box server and can be preloaded in RAD’s
virtual CPE (vCPE) platforms. It combines powerful networking
capabilities with virtualization for hosting SD-WAN and any other
value-added virtual network function (VNF) applications from
multiple vendors.
For more information on vCPE-OS, please refer to the vCPE-OS
datasheet.
Table 2. Timing and Synchronization
Specifications
ETX-2i
Fixed Ports
ETX-2i 64E1
ETX-2i/M &
D-NFV
ETX-2i-B
ETX-2i-B
D-NFV
Best Master Clock
Algorithm (BMCA)
+
+
+
-
IEEE-1588v2 precision time
protocol (PTP) per
G.8265.1, G.8275.1, and
G.8275.2 Telecom profiles
OC, TC, BC
Slave clock
TC
OC, TC, BC
Slave clock
(excluding D-NFV option)
TC
PTP ports
ToD/1PPS (RJ-45), External
clock (CONN.COAX SMA),
1PPS (CONN.COAX SMA), 2M
(SMA)
-
ToD/1PPS (RJ-45), External clock
(CONN.COAX SMA), 1PPS (CONN.COAX SMA), 2M
(SMA)
(excluding D-NFV option)
-
Station clock
Balanced E1, unbalanced E1
(via adapter cable); RJ-45
connector
-
Balanced E1, unbalanced E1 (via adapter cable);
RJ-45 connector
(excluding D-NFV option)
-
SyncE recovery from PDH
module to Ethernet ports
+
-
+
(excluding D-NFV option)
-
Synchronous Ethernet
(SyncE), eSYNCE
ITU-T G.8261-G.8264
-
ITU-T G.8261-G.8264
(excluding D-NFV option)
-

## ETX‑2i Specifications  *(p.5)*

E1/T1 INTERFACES (TDM PSEUDOWIRE)
(ETX-2i 64E1 with built-in TDM PWE E1/T1 ports)
Number of Ports
Compliance
E1: G.703
T1: ANSI T1.101, ANSI T1.403
Data Rate
E1: 2.048 Mbps
T1: 1.544 Mbps
Line Coding
E1: HDB3
T1: B8ZS
Framing
E1: Framed (G.732N with or without
CRC)
Framed with CAS (G.732S with or
without CRC)
Unframed
T1: Unframed or ESF
Impedance
E1: 120Ω, balanced
75Ω, unbalanced (via adapter cable)
T1: 100Ω, balanced
Connectors
Electrical, RJ-45
Payload Encapsulation
CESoPSN, SAToP
Network Encapsulation
MEF 8, UDP/IP
ENVIRONMENTAL
Storage
Temperature
-40 to 85°C (-40 to 185°F)
Operating
Temperature
Regular:
0 to 50°C (32 to 122°F): ETX-2i
-5 to 55°C (23 to 131°F): ETX-2i-B
Temperature hardened:
-40 to 65°C (-40 to 149°F): ETX-2i
-20 to 65°C (-4 to 149°F): ETX-2i-B w/ 10 ports (2U)
A single SFP-30H is supported at temperature up
to 62°C.
Humidity
5% to 90%, non-condensing
PHYSICAL
8.5-inch
Enclosures
Height: 43.7 mm (1.7 in)
ETX-2i-B 2U: 88.2 mm (3.5 in)
Width: ETX-2i - 215.5 mm (8.5 in)
ETX-2i-B - 220 mm (8.7 in)
Depth: ETX-2i - 300 mm (11.8 in)
ETX-2i-B - 170 mm (6.7 in)
ETX-2i-B/D-NFV - 280 mm (11 in)
Weight:
ETX-2i/M - 2.16 kg (4.76 lb) maximum
M (module): 0.91 kg (2.01 lb)
ETX-2i-B 1U - 0.7 kg (1.54 lb)
ETX-2i-B 2U – 1.34 kg (2.95 lb)
ETX-2i-B/DNFV - 2.01 kg (4.4 lb) (Module: 0.91 kg
(2.01 lb))
19-inch
Enclosures
Height:
All devices except ETX-2i 64E1 - 43.7 mm (1.7 in)
ETX-2i 64E1 - 132.7 mm (5.2 in)
Width: 440 mm (17.4 in)
Depth: 240 mm (9.5 in)
ETX-2i/M - 300 mm (11.8 in)
ETX-2i/D-NFV - 350 mm (13.78 in)
Weight:
ETX-2i Fixed Ports - 3.6 kg (7.9 lb) maximum
ETX-2i 64E1 - 7.15 kg (15.87 lb) maximum
ETX-2i/M module: 0.91 kg (2.01 lb)
RESILIENCY
Dual Homing
Dual homed link redundancy
Ethernet Path
Protection
G.8031 linear 1:1 protection
Ethernet Ring
G.8032v2 rings with sub 50 ms protection for
Ethernet traffic
Link
Aggregation
IEEE 802.1ax (802.3ad) 1:1 LAG with LACP for
pairs of network or user Ethernet ports
LAG with load balancing
Table 3. Power
Specifications
ETX-2i
Fixed Ports
ETX-2i 64E1
ETX-2i/M &
D-NFV
ETX-2i-B
ETX-2i-B D-NFV
Power Supply
AC: 100-240 VAC (-10%, +6%), 50/60 Hz, 0.9A
DC: 48 VDC (40-60 VDC), 2A
ETX-2i, ETX-2i-B 8.5” – Dual DC feed
ETX-2i-B - Wide-range AC/DC with auto detection
Power Supply Redundancy
+
+
+
+
-
Power Consumption
Non-modular
product base
(8 GbE): 35W max
AC PS: 74W max;
DC PS: 60W max
Modular base: 30W
Modular uplink: 5W max
VDSL: 10W max
D-NFV: 30W
23W
30W

## ETX‑2i  *(p.6)*

IP ADDRESSING AND ROUTING
Addressing
IPv4 and IPv6
Rate
ETX-2i-B: Up to 4 Gbps
ETX-2i: Up to 8 Gbps
Routing
Protocols
Dynamic routing: OSPFv2, BGPv4, VRRPv2,
and VRRPv3
Static routing
Bidirectional forwarding detection (IP-BFD
single hop) for fast path failure detection
and fast route propagation
Ethernet over IP/GRE tunneling
Routing
Technologies
Static
Policy-based
VRF (10), RIF (32)
NAT
Static/dynamic
NAPT/NAT
DHCP
Client, server, relay
IP helper addresses
DNS
Server
NETWORKING CAPABILITIES
Services
Ethernet E-LAN, E-Tree, E-Access
MEF CE2.0 compliant
Layer-2 services with available bandwidth
Layer-2 Forwarding Jumbo frame support
Flow Classification
Rules
Outer VLAN or outer + inner VLAN
PCP
TOS/DSCP
EtherType
IP/MAC source/destination address
Port Classification
Per port
5-tuple ACL
Policing
Color aware/unaware dual token bucket with
user-configurable CIR + CBS and EIR + EBS
2-rate/3-color policing per EVC.CoS
Bandwidth policing per MEF 10.3
Hierarchical envelope policer per MEF 10.3
MultiCoS EVCs per MEF 10.3
Scheduling
8 × CoS per EVC scheduling elements
Strict Priority (SP)
Weighted Fair Queue (WFQ)
Shaping
Per EVC
Per EVC.CoS
DIAGNOSTICS
Alarm Relay
(optional)
Type: Dry contacts with three “in”
Connector: Terminal block, 9-pin
Connectivity Fault
Management
(CFM)
Per IEEE 802.1ag
EFM Link-fault
OAM
IEEE 802.3ah
Link-level OAM
Per IEEE 802.3-2005
Counters
RMON2 port-level counters
Delay and Loss
Measurements
Per MEF 36
ICMP Echo
Over L2 and L3 services
Tests IP connectivity (PING )
KPI Measurements Accurate one-way KPI measurements
Limiting Multicast
Traffic Flooding
DHCP and MLDv2 snooping
Loop Prevention
Using MSTP and RSTP
Loopback Tests
Non-disruptive loopback per flow, with
MAC/IP address swap
Loopbacks at Ethernet port level
On-demand Layer-2 and 3 loopbacks
LLDP Discovery
Per IEEE 802.1AB
Service Activation
Tests
RFC-2544: Eight built-in wirespeed testers
ITU-T Y.1564: Eight built-in wirespeed testers
Service Utilization
and Performance
Monitoring
Per ITU-T Y.1731.2012, including synthetic loss
measurement
TWAMP
RFC 5357 TWAMP light generator and
responder (SW license)
ITU-T Y.1731 PM (SLM; DM)
RFC 5618 TWAMP responder and receiver
TWAMP sender
PM Controller (PMC)
GENERAL
Compliance
MEF 3.0
CE 2.0
MEF 6 (E-Line – EPL and EVPL, E-LAN – EPLAN
and EVPLAN)
MEF 9, MEF 10, MEF 14, MEF 20, MEF 36, MEF
IEEE 802.3, 802.3u, 802.1D, 802.1Q, 802.1p,
802.3ad, 802.3-2005, 802.1ax, 802.1ag
ITU-T Y.1731, G.8031, G.8032v2, G.8262,
G.8265, RFC-2544, ITU-T Y.1564
Push Buttons
FD push button for setting unit to default
configuration

## ETX‑2i  *(p.7)*

BRIDGE
Max. Frame Size
9600 bytes
Compliance
802.1D, 802.1Q, 802.1ad
Mode
VLAN-aware, VLAN-unaware
VLAN Editing
Inner/outer VLAN editing per VLAN and p-bit
values
MANAGEMENT AND SECURITY
Management
Options
Local management via LAN port or serial port
Remote management via in-band VLAN
Protocols and
Security
SSH (Secure CLI)
Telnet
SNMPv3
SFTP
NETCONF/YANG management interface
Password-protected access
Authorization levels
RADIUS or TACACS+ authentication
Dual Stack IPv4 and IPv6 routing
IP forwarding
Static routing
Access Control List (ACL)
Large
Deployments
Plug and play zero touch provisioning (DHCP,
PPPoE, XML configuration files download via
TFTP/SCP)
Configuration backup and restore
Control Port
Interface
V.24/RS-232 DCE
Connector
Mini-USB
Format
Asynchronous
Data rate
9.6, 19.2, or 115.2 kbps
Ethernet Management Port
Type
10/100/1000BASE-T
Connector
RJ-45

## ETX‑2i Ordering  *(p.8)*

<product>/?/@/$/#/+/&/~/%
?
Temperature Range
Regular
H
Temperature hardened
HN
NEBS compliant, temperature-hardened
N
NEBS compliant
@
Power Supply
AC
AC power supply
ACDC
Dual AC and DC power supplies
DCHP
High power DC power supply for D-NFV
and non D-NFV
ACHP
High power AC power supply for D-NFV
ACR
Dual AC power supply
DC
DC power supply
DCR
Dual DC power supply
DDC
Dual DC feed power supply
WR
Wide range
$
Enclosure size (inches)/Modular
19”
19" 1U metal box (ETX-2i)
M
8.5” modular uplink (ETX-2i)
V
8.5” with D-NFV module slot (ETX-2i-B)
19V
19" with D-NFV module slot (ETX-2i)
+
64E1T1
64 E1/T1 ports (ETX-2i)
DRC
2 IN dry contacts
~
Timing Options
SYE
SyncE
PTP
1588v2 timing and SyncE
RECOMMENDED CONFIGURATIONS
Note: For temperature-hardened options, use SFPs with maximum
operating temperature 85°C (185°F).
ETX-2i:
ETX-2i/AC/19
ETX-2i/AC/M
ETX-2i/DDC/M/PTP
ETX-2i/H/AC/19/PTP
ETX-2i/H/ACR/19/PTP
ETX-2i/HN/AC/19/PTP
ETX-2i/N/ACHP/19V
ETX-2i/H/AC/M/VDSL8W/POTS
ETX-2i/H/AC/M/VDSL8W/ISDN
ETX-2i/DC/19/64E1T1/SYE
ETX-DNFV-M/?/*/&/^
D-NFV modules based on Xeon D (for ETX-2i)
?
Intel® processor name and # cores
X4C
Xeon D with 4 Cores
X8C
Xeon D with 8 Cores
*
SSD
Solid state drive rate
128S
128 GB
256S
256 GB
^
RAM
16R
16 GB RAM
24R
24 GB RAM
ETX-DNFV-M/X4C/128S/16R
ETX-DNFV-M/X8C/256S/24R
ETX-M/?/^
Ethernet network uplink module
?
Uplink module ports (Default = no uplink module)
2ETH
Eth uplink module with 2 combo ports
ETX-M/2ETH
Note: Any ETX-2i with D-NFV option must be ordered together with a
RADcare Package and RADcare Project Assurance Package.
ETX-2i-B:
ETX-2i-B/WR/2SFP/2CMB
ETX-2i-B/WR/2SFP/2CMB/DRC
ETX-2i-B/WR/2SFP/4UTP
ETX-2i-B/H/WR/2SFP/8SFP
Note: Although this device option has ten active ports, processing
capability is limited to six GbE.
ETX-2i-B/AC/V/2SFP/4UTP
ETX-2i-B/DDC/V/2SFP/4UTP
ETX-DNFV-M/?/*/&/^
D-NFV modules based on Intel® Atom Rangeley (for ETX-2i-B)
?
Intel® Atom Rangeley model processor name and # cores
R4C
C2558 4-core
R8C
C2758 8-core
BLNK
Blank
*
SSD
Solid state drive rate
128S
128 GB
^
RAM
8R
8 GB RAM
16R
16 GB RAM
$
Acceleration
ACC
DPDK acceleration
ETX-DNFV-M/R4C/128S/8R
ETX-DNFV-M/R4C/128S/8R/ACC
ETX-DNFV-M/R8C/128S/8R
ETX-DNFV-M/R8C/128S/8R/ACC
ETX-DNFV-M/R8C/128S/16R
ETX-DNFV-M/R8C/128S/16R/ACC
ETX-DNFV-M/BLNK
SPECIAL CONFIGURATIONS
Please contact your local RAD partner for additional
configuration options
SOFTWARE LICENSES
ETX-2-SW TWAMP
SW license to activate and operate TWAMP related
functionalities in ETX-2 and ETX-2i.

## ETX‑2i  *(p.9)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel 972-3-6458181 | Fax 972-3-7604732
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
547-100-01/23 (6.8.2) Specifications are subject to change without prior notice. © 1988–2023 RAD Data Communications Ltd. RAD products/technologies are protected by
registered patents. To review specifically which product is covered by which patent, please see ipr.rad.com. The RAD name, logo, logotype, and the product names MiNID,
Optimux, Airmux, IPmux, and MiCLK are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.
SUPPLIED ACCESSORIES
AC power cord (with AC models)
DC connector kit PLUG-DC/TB-S/J (for ETX-2i DC models)
DC connector kit PLUG-DC-MC1/BS for ETX-2i-B DC DNFV option
See the Mounting Kits table.
OPTIONAL ACCESSORIES
CBL-MUSB-DB9F
Mini USB cable to connect device to a serial port
ETX-2i-PS/!/^
Extractable power supply for ETX-2i/64E1
!
Power supply
AC
Single AC power supply
DC
Single DC power supply
ACHP
Single high power AC power supply
^
E1 ports (Default = no E1 ports)
ETX-2i-64E1
ETX-2i-PS/DC/64
DC PS, 64E1T1 device
ETX-2i-PS/AC/64
100-240 VAC, 64E1T1 device
ETX-2i-PS/ACHP
High-power AC power supply for ETX-2i/DNFV
SFP-GPON-1DH
GPON optical network terminal SFP
See the Mounting Kits table.
Table 4. Mounting Kits
Product
19” Rack
Wall
ETX-2i (8.5”)
RM-35/P1 – one unit
RM-35/P2 – two units
WM-35
ETX-2i (19”)
RM-34 (supplied) – one unit
WM-34
ETX-2i-64E1
(19” 3U)
RM-52 (supplied) – one unit without cable
management
CM-52 – one unit with cable management
-
ETX-2i-DNFV (19”)
RM-34 (supplied) – one unit
-
ETX-2i-B (8.5”)
RM-35/P1 – one unit
RM-35/P2 – two units
WM-35-TYPE4
ETX-2i-B 2U (8.5” 2U)
RM-54/A – one unit
RM-54/A2 – two units
-
ETX-2i-B-DNFV (8.5”)
RM-35/P1 – one unit
RM-35/P2 – two units
WM-35