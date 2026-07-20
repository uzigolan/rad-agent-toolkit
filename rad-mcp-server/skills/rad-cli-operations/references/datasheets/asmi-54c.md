# ASMi-54C Ethernet and TDM over SHDSL/SHDSL.bis 8-Port Modules

<!-- datasheet product=asmi-54c family=mp4100 kind=card source=asmi-54c_ds.pdf -->

*Datasheet `asmi-54c_ds.pdf`, 4 pages. Product `asmi-54c`, family `mp4100` (card).

## Megaplex-4 ASMi-54C Ethernet and TDM over SHDSL/SHDSL.bis 8-Port Modules  *(p.1)*

- 16-wire modules for Ethernet and TDM services over 8W (4-pair), 4W (2-pair), or 2W
(1-pair) SHDSL/SHDSL.bis lines
- SHDSL: Data rates of up to 22.8 Mbps for 8W, up to 11.4 Mbps for 4W and up to
5.7 Mbps for 2W
- EFM extended rate for ASMi-54L: Data rates of up to 15.3 Mbps per 2W
- Remote power feeding over 4 wires
- Extended range with RAD’s SHDSL/SHDSL.bis repeater
- Two copper/fiber Ethernet interface ports for local Ethernet termination
- EFM (Ethernet First Mile) or M-pair bonding over SHDSL/SHDSL.bis
ASMi-54C is a family of SHDSL/SHDSL.bis
Ethernet and TDM modules for the
Megaplex-4 chassis that delivers digital
data to customer premises over existing
copper cables of the distribution network.
SHDSL/SHDSL.BIS
ASMi-54C modules provide a simple,
low-cost connectivity solution using High
Speed Digital Subscriber Line
(SHDSL/SHDSL.bis) technology.
The ASMi-54C family includes three main
module types:
-
ASMi-54C/ETH –Ethernet over
SHDSL.bis 8-port module with EFM
support
-
ASMi-54C/E1/N - E1 over
SHDSL/SHDSL.bis 8-Port module
(starting from version 3.0)
-
ASMi-54C/E1/ETH/N –E1 and Ethernet
over SHDSL/SHDSL.bis 8-port module,
with optional remote power feeding.
(starting from version 3.0)
Note: ASMi-54C/E1/N and ASMi-54C/E1/ETH/N
modules cannot work with a mix of ASMi-54/54L
and ASMi-52/52L modems at the far end.
Each SHDSL/SHDSL.bis port is a multirate
SHDSL/SHDSL.bis modem transmitting at
user-selectable data rates of up to
5.7 Mbps on each pair.
Using TC-PAM 64 line coding technology,
the modems operate in full-duplex mode
at up to 15 Mbps per port.
ASMi-54C can operate as a Central
SHDSL.bis (STU-C) or Remote (STU-R)
SHDSL.bis Termination Unit working with
up to 8 standalone ASMi or ETX family
devices or another ASMi-54C module.
When providing Ethernet services and
operating as STU-R, ASMi-54C performs
line probing according to G.991.2. The DSL
interface can be configured to adapt its
rate to the condition of the line (noise,
loop attenuation, etc.) or operate at a
fixed user-selected rate. The SHDSL line
performs TPS-TC framing 64/65 for EFM
(IEEE 802.3) and HDLC (G.991.2).
The processing and switching of Ethernet
traffic over TDM (SHDSL) links is
configured by means of PCS (Physical
Coding Sublayer) using EFM or HDLC as the
Layer-2 protocol.
EFM bonding on the Ethernet interface
ensures that a failure or addition of a link
does not drop the traffic being
transmitted over the other wires in the
group. The capacity of the group is not
affected when a new link is added at a
lower rate.
ETHERNET
The Ethernet services are provided by
means of an internal Layer-2 Ethernet
switch that fully complies with the IEEE
802.3/Ethernet V.2 standards, and has full
VLAN support.
The external Ethernet ports can be
ordered with two types of interfaces:
-
10/100BaseTx interfaces terminated in
RJ-45 connectors.
-
SFP Sockets for Fast Ethernet
transceivers. RAD offers a wide variety
of SFPs, for meeting a wide range of
operational requirements.
The Ethernet switch switches traffic
between the module Ethernet ports and
bundles, including ETH over SHDSL, and
the CL module Ethernet subsystem (for
connection via the CL GbE ports to a
packet-switched network, or for
transmission through the SDH network via
virtually concatenated groups (VCGs).
ASMi-54C implements the IEEE's 802.1Q
standards to provide VLAN-tagging with

## ASMi-54C  *(p.2)*

levels of prioritization, enabling carriers to
offer differentiated Ethernet services.
VLAN tagging can also be employed to
separate traffic, ensuring transparency of
the customer traffic and bolstering
security of management traffic.
TDM
E1 services are provided by /N options of
the ASMi-54C module.
To increase the available SHDSL range,
two or four pairs can be bonded to
operate in the M-pair (HDLC) mode
specified in ITU-T Rec. G.991.2. Bonding is
available for lines handled by the same
SHDSL section (the section handling either
ports 1 to 4, or ports 5 to 8).
The external line ports feature user-
selectable, balanced (120Ω) or unbalanced
(75Ω) DSU interfaces. The framing mode
is also user-selectable, in accordance with
the required processing of the port traffic:
G.704 basic with or without CRC-4, or
unframed.
The DS0 cross-connect matrix of the
Megaplex-4 chassis enables flexible
payload routing in the ASMi-54C/N
modules, independently configurable for
each port, at the individual timeslot (DS0)
level.
REMOTE POWER FEEDING AND
EXTENDED RANGE
All the ASMi-54C modules have a remote
power feeding version that delivers power
and data over 4 wires to remote
SHDSL/SHDSL.bis modems or repeaters.
Power feeding for each individual line is
connected/disconnected via a software
command. The power feeding status for
each line and report of current overload
conditions are displayed via CLI.
SDHSL EFM data transmission range can
be significantly extended with RAD’s new
S-RPT/EFM repeater, using EFM bonding
technology with local or remote power
feeding, thus greatly enhancing RAD’s
solution for migration to Next Generation
networks.
The module receives the power from the
external MPF power feeder.
MANAGEMENT
Setup, control, and diagnostics are
performed in the following ways:
-
Via ASCII terminal connected to a
supervisory port on the Megaplex-4 CL
module
-
Via management station connected to
a dedicated 10/100BaseT Ethernet
port on the Megaplex-4 CL module
-
Using inband management with
dedicated VLAN for managing remote
units (ASMi-54/ASMi-54L)
-
Using EOC from the central ASMi-54C
module for managing remote units
(ASMi-52/ASMi-52L/ASMi-53).
MONITORING AND DIAGNOSTICS
Performance statistics for the SHDSL,
Ethernet, PCS (Physical Coding Sublayer)
and E1 ports may be obtained and
analyzed via the Megaplex-4 management
system.
ETH
Headquarters
STM-4/
OC-12
Branch
E1
Branch
FE
SHDSL/SHDSL.bis
FE
GbE
NMS
SHDSL/SHDSL.bis
IP/MPLS
SDH/SONET
Router
PBX
Megaplex-4
ASMi-54L/
ASMi-53
ASMi-52/
ASMi-54/
ASMi-53
5.7/11.4 Mbps (ASMi-53)
2W/4W (EFM)
15/30 Mbps (ASMi-54L)
SHDSL.bis
Branch
FE
ASMi-54L
S-RPT/EFM
LAN
S-RPT/EFM
120 VDC
MPF
Figure 1. TDM/Ethernet Services over Copper and Fiber Infrastructure and Ethernet Service Extension over Copper
Leased Lines
Table 1. Typical Ranges over 2W@26 AWG Cable
Data Rate
[kbps]
Ranges
[km]                [mi]
6.6h
4.1
1536
4.9
3.0
2048
4.5
2.8
4096
3.2
2.0
4608
3.0
1.9
5696
2.6
1.6
15296
0.70
0.43
Notes
1. The SHDSL data rate depends on the module type,
distance, number of wires and far-end device.
2. 15296 kbps is for TC-PAM 64 only.
3. The typical ranges are based on error-free lab tests
without noise and obtained on a 26 AWG cable line
simulator (DLS-400).
4. For ASMi-52/52L on the far end, only data rates up
to 2048 are relevant.

## Specifications  *(p.3)*

SHDSL/SHDSL.bis INTERFACE
Number of Ports
Number of Wires
2, 4, 8
Compliance
ITU-T G.991.2, ETSI TS 101524
EFM bonding per IEEE 802.3ah,
clauses 61, 63
Max. Data Rate
See Table 2
Line Coding
With remote ASMi-52/52L: TC-PAM 16
With remote ASMi-54, ASMi-53,
ETX-203AM, ETX-2i: TC-PAM 16/32
With remote ASMi-54L: TC-PAM 16/32/64
Impedance
135Ω
Connectors
DB-26 convertible to 8 RJ-45 connectors
via adaptor cable (regular model)
Typical Range
See Table 1
FAST ETHERNET INTERFACE
Number of Ports
2 UTP (RJ-45 shielded) or 2 SFP sockets
SFP Transceivers
For full details, see the SFP Transceivers
data sheet on www.rad.com
Note. It is strongly recommended to order this
device with original RAD SFPs. RAD cannot
guarantee full compliance to product specifications
for units using non-RAD SFPs.
Data Rate
10/100 Mbps (Fast Ethernet)
Autonegotiation (copper only)
Maximum Frame Size
ASMi-54C/N (all models): 9600 bytes
ASMi-54C/ETH: 1522 bytes
E1 INTERFACE
Number of Ports
Coding
HDB3
Line Impedance
Balanced E1: 120Ω
Unbalanced E1: 75Ω  (via adapter cable)
E1 Jitter Performance
As per ITU-T G.823
Connector
DB-44 convertible to RJ-45 or BNC
connectors via adaptor cables or patch
panel
DIAGNOSTICS
(ASMi-54C/N only)
-
Local and remote loopbacks on local
E1 ports, per port and per timeslot
-
Local and remote loopbacks on local
E1-i ports connected to the
corresponding remote SHDSL ports,
per port and per timeslot
-
Remote-on-remote inband loopbacks
on SHDSL ports, per port
-
BER Test on local framed E1 and E1-i
ports, per timeslot
-
BER Test on local unframed and
whole framed E1 and E1-i ports,
per port
Performance Monitoring
Per ITU-T Rec G.991.2, G.826
GENERAL
Environment
Operating temperature:
ASMi-54C/ETH: -10°C to 55°C (14°F
to  131°F)
ASMi-54C/N: 0°C to 45°C (32°F to
113°F)
Storage temperature: -20°C to 70°C
(-4°F to 158°F)
Humidity: up to 95%, non-
condensing
Indicators (per ETHERNET port)
ASMi-54C/N
LINK/ACT (green)
10/100 (yellow)
ASMi-54C
LINK (green) – LAN link integrity
ACT (yellow) – LAN data activity
Power Consumption
ASMi-54C/ETH: 14.5W
ASMi-54C/ETH/UTP/RPF: 14.8 W
ASMi-54C/E1/N: 7.3W
ASMi-54C/E1/ETH/N: 12W
ASMi-54C/E1/ETH/UTP/N/RPF: 12.3W
Note:  When power feeding is enabled, additional
power consumption from MPF (see MPF Data
Sheet) should be taken into account.
Remote Power Feed
Number of Remote Units: Up to 8
Power Feeding: 120 VDC at 70 mA
maximum per line
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
Order this publication by Catalog No. 803832
464-153-11/15  Specifications are subject to change without prior notice.  1988–2015 RAD Data Communications Ltd. The RAD name, logo, logotype, and the terms EtherAccess, TDMoIP and TDMoIP Driven, and
the product names Optimux and IPmux, are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.

## ASMi-54C Ordering  *(p.4)*

RECOMMENDED CONFIGURATIONS
MP-4100M-ASMi-54C/E1/N
E1 over SHDSL/SHDSL.bis 8-Port Module
MP-4100M-ASMi-54C/ETH/UTP
Ethernet over SHDSL.bis 8-port module
with UTP connectors
MP-4100M-ASMi-54C/E1/ETH/UTP/N
E1 and Ethernet over SHDSL/SHDSL.bis
8-port module with UTP connectors
SPECIAL CONFIGURATIONS
Please contact your local RAD partner for
additional configuration options.
OPTIONAL ACCESSORIES
CBL-DB26-8SHDSL
Cable for splitting a single 26-pin
SHDSL.bis connector to 8 x RJ-45
connectors
Note: This cable is required for the module
operation. It can either be ordered from RAD or
manufactured by the customer according to pinouts
provided in the manual.
CBL-G703-8/RJ45/ST
Cable for splitting the 44-pin E1 connector
to 8 E1 balanced RJ-45 connectors
CBL-G703-8/RJ45/X
Cross-cable for splitting the 44-pin E1
connector to 8 E1 balanced RJ-45
connectors
CBL-G703-8/COAX
Cable for splitting the 44-pin E1 connector
to 8 pairs of E1 unbalanced BNC
connectors
CBL-G703-8/OPEN/2M
Open-ended cable with DB-44 connector
for balanced E1 applications
All cables are 2m (6.6 ft) long.
MP-PATCH-16-BNC/DB44
Low-cost adapter patch panel terminated
in BNC connectors at the user’s end, for
connecting several ASMi-54C/N modules
to equipment with unbalanced E1
interfaces
CBL-DB44-DB44
Cable for connecting each DB-44
connector of the module to the
corresponding DB-44 connector of the
patch panel
Table 2. ASMi-54C Module Comparison
ASMi-54C/ETH
ASMi-54C/E1/N
ASMi-54C/E1/ETH/N
Line type
SHDSL.bis
SHDSL/SHDSL.bis
SHDSL/SHDSL.bis
Remote CPE and
number of wires
2W
4W
8W
2W
4W
8W
2W
4W
8W
ASMi-52
N/A
N/A
N/A
+
+
-
+
+
-
ASMi-52L
N/A
N/A
N/A
+
+
-
+
+
-
ASMi-54
+
+
+
+
+
+
+
+
+
ASMi-54L
+
+
-
+
+
-
+
+
-
ASMi-53
+
+
-
+
+
-
+
+
-
ETX-203AM, ETX-2i
+
+
+
-
-
-
-
-
-
Data transfer
Ethernet data over 1, 2 or 4
pairs
E1 data over 1, 2 or 4
pairs
E1 and Ethernet data over
1, 2 or 4 pairs
Central/Remote
STU-C/ STU-R
STU-C/ STU-R
STU-C/ STU-R
EFM/M-pair
EFM/M-pair
M-pair
M-pair
Maximum data rate, kbps ASMi family
30592 (2 pairs)
22784 (4 pairs)
22784 (4 pairs)
ETX-203AM, ETX-2i
22784 (4 pairs)
Supported in
Ver 2.x, Ver 3.x, Ver 4.x
Ver 3.x, Ver 4.x
Ver 3.x, Ver 4.x