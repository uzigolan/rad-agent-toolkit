# MPW-1 TDM Pseudowire Access Gateway Module

<!-- datasheet product=mpw-1 family=mp4100 kind=card source=mpw.pdf -->

*Datasheet `mpw.pdf`, 4 pages. Product `mpw-1`, family `mp4100` (card).

## Megaplex-4 MPW-1 TDM Pseudowire Access Gateway  *(p.1)*

- TDM multiplexing and Ethernet switching for transmitting voice and sync/async data
over packet-switched networks
- Pseudowire/circuit emulation as per TDMoIP, CESoPSN, SAToP, HDLCoPSN, and more
- Industry-leading adaptive clock recovery mechanism over packet-based networks
- Extensive OAM and performance monitoring capabilities
- Three Ethernet ports with auto-detection of Fast Ethernet SFP or UTP 10/100BaseT
- Three timing modes: Internal, External, or Adaptive clock from network
Megaplex-4 equipped with the MPW-1
module provides legacy services over
packet-switched networks (PSN). MPW-1
receives the data stream from other
modules in the Megaplex-4 chassis (E1/T1,
SHDSL, data or voice ports) via the
Megaplex backplane, and converts it into
IP or MPLS packets for transmission over
Ethernet, IP or MPLS networks.
The packets are transmitted to the PSN
via any MPW-1 Ethernet port or any
Ethernet port (GbE, FE or VCG) of a
module installed in the chassis. A remote
pseudowire device converts the packets
back to the original user traffic format.
PSEUDOWIRE
The ASIC-based architecture provides a
robust and high performance pseudowire
solution with minimal processing delay.
MPW-1 transports legacy TDM traffic over
packet according to a variety of standards,
including TDMoIP, CESoPSN, SAToP, and
HDLCoPSN.
The proper balance between the PSN
throughput and delay is achieved via
configurable packet size.
A jitter buffer compensates for packet
delay variation (jitter) of up to 180 msec
in the network.
Optimal handling of pseudowire traffic
within the PSN is achieved by configuring
the following parameters:
-
For Ethernet transport networks:
outgoing pseudowire packets are
assigned to a dedicated VLAN ID
according to 802.1Q and marked for
priority using 802.1p bits.
-
For IP transport networks: outgoing
pseudowire packets are marked for
priority using DSCP, ToS, or Diffserv
bits. This allows TDMoIP packets to be
given the highest priority in IP
networks.
-
For MPLS transport networks: outgoing
pseudowire packets are assigned to a
specific MPLS tunnel, and marked for
priority using the EXP bits.
ETHERNET
The 3-port 10/100BaseT interface includes
a built-in flow classification engine that
performs single or double VLAN tagging
according to IEEE 802.1Q and 802.1p. The
interface performs autonegotiation for
plug-and-play Ethernet connectivity and
complies with IEEE 802.3/Ethernet V.2
standards.
The external Ethernet ports can be
ordered with two types of interfaces:
-
10/100BaseTx interfaces terminated in
RJ-45 connectors
-
Sockets for Fast Ethernet SFP
transceivers. RAD offers several types
of SFPs with optical interfaces, for
meeting a wide range of operational
requirements (SFPs with copper
interfaces are also available).
It is strongly recommended that this
device be ordered with original RAD SFPs
installed. This will ensure that
comprehensive functional quality tests on
the entire assembled unit, including the
SFP devices, have been performed by RAD
prior to shipping. RAD cannot guarantee
full compliance with product specifications
for units using non-RAD SFPs.
The Ethernet switch routes traffic between
the module Ethernet ports, the PW engine
and the CL module Ethernet traffic
subsystem (for connection via the CL GbE
ports to a packet-switched network, or for
transmission through the SDH network via
virtually concatenated groups (VCGs)), and
between module Ethernet ports and PWs.

## MPW-1  *(p.2)*

CROSS-CONNECT
In the MPW-1 module, a pseudowire (PW)
transports a group of up to 31 timeslots
(individual or multiple).
Eight internal DS1 ports connect the
module to any module inside the
Megaplex-4 chassis.
MPW-1 handles up to 128 connections
(16 PWs per internal DS1 port); a chassis
can handle up to 640 connections. In
addition, the module’s Int-DS1 ports are
part of the Megaplex DS0 cross-connect
subsystem.
TIMING
MPW-1 can operate in three timing
modes:
-
Internal mode: The Megaplex internal
oscillator is the source for the timing
used by Ethernet links and other I/O
modules. MPW-1 is the sole clock
source for all the units in the network.
-
External mode: one of the I/O modules
is the source for the system timing.
-
Adaptive mode: the MPW-1 timing
clocks are regenerated using the
adaptive method, according to the
monitored received packet rate from
the IP network. The timing is then also
passed on to the I/O modules.
End-to-end synchronization between
circuits is maintained by deploying
advanced clock recovery mechanisms.
The system clock ensures a single clock
source for all TDM links, and uses master
and fallback timing sources for clock
redundancy.
Site A
Site B
E1
LS
Voice
PBX
E1
LS
Voice
ETH
PBX
RFER
Megaplex-4100
Megaplex-4100
PBX
E1
Site C
IPmux-24
Figure 1. Resilient Topology over Dark Fiber for Ethernet and TDM Traffic
RESILIENCY
DS1 Protection
The MPW-1 module provides redundancy
protection between internal DS1 ports,
and between an internal DS1 port and a
user-selected legacy TDM port (E1, T1,
SHDSL, PDH, etc.) with redundancy.
Therefore, the pseudowire traffic is also
protected by the redundancy function.
The pseudowire redundancy mode
depends on the use of OAM:
-
When OAM is disabled, the pseudowire
redundancy mode is 1+1, meaning that
the traffic is also sent on the standby
pseudowire
-
When OAM is enabled, the pseudowire
redundancy mode is 1:1, meaning that
only OAM packets are sent on the
standby pseudowire. This minimizes
packet traffic when a pseudowire is
inactive due to the redundancy
mechanism.
Resilient Fast Ethernet Ring
MPW-1 employs RAD’s Resilient Fast
Ethernet Ring (RFER) technology to
construct self-healing 100-Mbps Fast
Ethernet fiber or copper ring topologies
(ring resiliency functions similarly to that
of STM-1 networks). In the event of link
failure on any segment of the ring, RFER
reroutes the TDMoIP traffic within 50 ms,
fast enough to maintain the required voice
quality.
RFER enables enterprises, campuses,
power companies, transportation
companies and utilities to create highly
reliable networks, using dark fiber or dry
copper in a ring topology.
Survivability is further enhanced by RFER’s
scalable support for multiple rings, which
eliminates the risk of a single point of
failure. This is ideal for dispersed
applications, such as commuter railroads.
FAULT PROPAGATION
MPW-1 modules perform fault propagation
for pseudowires; if a problem is detected
on a pseudowire, the attached physical
port receives a fault indication and vice
versa.
OAM AND DIAGNOSTICS
LAN and IP layer network condition
statistics, such as packet loss and packet
delay variation (jitter), are monitored and
stored by the device.
Performance is monitored by storing
Ethernet and IP-layer network condition
statistics, such as packet sequence errors
(loss or misorder) and packet delay
variation (jitter).
RAD’s TDM PW OAM mechanism verifies
connectivity and prevents pseudowire
configuration mismatch.
16B
Central Site
GbE
Remote Sites
FE
GbE
FE/GbE
E1
LS
Voice
ETH
E1
LS
Voice
Megaplex-4100
PBX
PSN
Megaplex-2100
E1
LS
Voice
ETH
PBX
Megaplex-4100
PBX
PBX
PBX
E1
IPmux-24
Figure 2. Migrating Existing TDM-Based Services to Next Generation Packet Switched Network
24 Raoul Wallenberg Street
Tel Aviv 69719, Israel
Tel. 972-3-6458181
Fax 972-3-6498250, 6474436
E-mail market@rad.com
900 Corporate Drive
Mahwah, NJ 07430, USA
Tel. 201-5291100
Toll free 1-800-4447234
Fax 201-5295777
E-mail market@radusa.com
Order this publication by Catalog No.  803834
464-102-05/15  Specifications are subject to change without prior notice.  1988–2015 RAD Data Communications Ltd. The RAD name, logo, logotype, and the terms EtherAccess, TDMoIP and TDMoIP Driven, and
the product names Optimux and IPmux, are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.

## MPW-1 Specifications  *(p.4)*

ETHERNET INTERFACE
Number of Ports
3 fiber-optic or 3 UTP
Data Rate
10/100 Mbps (Fast Ethernet)
Autonegotiation (copper only)
Total Bandwidth per Module
100 Mbps per module
Maximum Frame Size
1600 bytes
Connectors
3 x RJ-45, shielded, or
3 x SFP socket (for transceivers, see
Ordering)
SFP Transceivers
For full details, see the SFP Transceivers
data sheet at www.rad.com
Indicators (per port)
LINK (green) – LAN link integrity
ACT (yellow) – LAN data activity
PSEUDOWIRE
Standard Compliance
IETF: RFC 4553 (SAToP), RFC 5087
(TDMoIP), RFC 5086 (CESoPSN)
ITU-T: Y.1413
MFA: IA 4.1, IA 8.0.0
Number of PW Connections
128 per module (up to 640 per chassis)
Jitter Buffer Size
0.5–200 msec (unframed) with 1 µsec
granularity
2.5–200 msec (framed) with 1 µsec
granularity
Clock Modes
Internal, External, Adaptive
DIAGNOSTICS AND STATISTICS
Diagnostics
Local and remote loopbacks on selected
timeslots of the internal DS1 ports
Ping test
Statistics
Ethernet Statistics (per RFC 2819)
Jitter buffer indication (overflow,
underflow, sequence error)
GENERAL
Power Consumption
8.5 W
Environment
Operating temperature:
-
Regular: -10°C to 55°C (14°F to 131°F)
-
IEEE-1613 certified options: -20°C to
55°C (-4°F to 131°F)
Storage temperature: -20°C to +70°C
(-4°F to +158°F)
Humidity: up to 95%, non-condensing

## Ordering  *(p.4)*

RECOMMENDED CONFIGURATIONS
MP-4100M-PW-1/3XUTP
TDM Pseudowire Access Gateway, 3 UTP
Ethernet connectors
SPECIAL CONFIGURATIONS
Please contact your local RAD partner for
additional configuration options.