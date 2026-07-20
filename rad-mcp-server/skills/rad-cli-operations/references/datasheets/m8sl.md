# M8SL 8-Port SHDSL E1 Module

<!-- datasheet product=m8sl family=mp4100 kind=card source=m8sl.pdf -->

*Datasheet `m8sl.pdf`, 4 pages. Product `m8sl`, family `mp4100` (card).

## Megaplex-4100 Module  *(p.1)*

M8SL

## 8-Port SHDSL E1 Module  *(p.1)*

- Up to 2048 kbps payload per port over 2-wire copper cables
- Up to three 10/100BaseT Ethernet ports, copper or fiber
- Integral L2 Ethernet switch with full VLAN support
- Range of up to 10.6 km (6.6 miles) over 26 AWG 2-wire cable
- Remote or Central functionality programmable per channel
- Inband management (EOC) according to G.991.2 or dedicated TS

## Extension of E1 and Ethernet traffic over SHDSL copper lines  *(p.1)*

The Megaplex M8SL module employs
Single-pair High speed Digital Subscriber
Line (SHDSL) technology, as standardized
by ITU-T Rec. G.991.2. This SHDSL E1
module offers a cost-effective solution for
delivering digital data to customer
premises over the existing copper cables
of the distribution network while
eliminating the need for repeaters.
In addition to providing SHDSL interfaces
for Megaplex-4100 units, M8SL modules
enable packet-based Fast Ethernet
services.
M8SL modules have two types of external
ports:
-
Eight SHDSL independently
configurable external ports for SHDSL
services
-
Three 10/100 Mbps Ethernet ports, for
packet-based services.
TDM SERVICES
Each M8SL port is a multirate SHDSL
modem operating at user-selectable data
rates which are multiples of 64 kbps,
starting from 192 kbps up to 2048 kbps
(32 timeslots). Data rates and distances
are adaptive: as the data rate increases,
the range decreases. Table 1 lists
typical ranges versus the payload
data rates.
The M8SL module is user-configurable for
operation in accordance with the following
standards:
-
ITU-T Rec. G.991.2. Annex B (for
compatibility with European or similar
networks)
-
Annex A (for compatibility with North
American or similar networks).
The module can operate as a Central
(STU-C) or Remote (STU-R) SHDSL
Terminal Unit (programmable per module
channel) opposite RAD’s ASMi-52, DXC,
FCD-IP, FCD-IPM devices, another M8SL
module or Megaplex-2100/2104 MSL-8
module.
ETHERNET SERVICES
The Ethernet services are provided by means
of an internal Layer-2 Ethernet switch that
fully complies with the IEEE 802.3/Ethernet
V.2 standards, and has full VLAN support.
The total Ethernet traffic per module (from
1, 2 or 3 ports) is up to 100 Mbps.
M8SL
The 3-port 10/100BaseT interface includes
a built-in flow classification engine that
performs single or double VLAN tagging
according to IEEE 802.1Q and 802.1p. The
interface features autonegotiation for
plug-and-play Ethernet connectivity and
complies with IEEE 802.3/Ethernet V.2
standards.
The external Ethernet ports can be
ordered with two types of interfaces:
-
10/100BaseTx interfaces terminated in
RJ-45 connectors.
-
Sockets for SFP Fast Ethernet
transceivers. RAD offers several types
of SFPs with optical interfaces, for
meeting a wide range of operational
requirements (SFPs with copper
interfaces are also available).
It is strongly recommended to order this
device with original RAD SFPs installed.
This will ensure that prior to shipping, RAD
has performed comprehensive functional
quality tests on the entire assembled unit,
including the SFP devices. RAD cannot
guarantee full compliance to product
specifications for units using non-RAD
SFPs.
The Ethernet switch switches traffic
between the module Ethernet ports and
the CL module Ethernet subsystem (for
connection via the CL GbE ports to a
packet-switched network, or for
transmission through the SDH network via
virtually concatenated groups (VCGs)), and
between module Ethernet ports and
bundles.
The processing and switching of Ethernet
traffic over TDM (SHDSL) links is
configured by means of bundles using
HDLC as the Layer-2 protocol. An HDLC
bundle is always defined on a single
SHDSL port, and its bandwidth depends
on the port framing mode:
-
In framed mode, the user can
configure the assigned bandwidth by
specifying the timeslots included in the
bundle. In this case, each port
supports up to four HDLC bundles. Up
to 32 bundles can be configured per
M8SL module.
-
In unframed mode, the full E1 port
bandwidth (2048 kbps) is
automatically assigned to the HDLC
bundle.
DIAGNOSTICS
Diagnostic capabilities include local and
remote loopbacks on the SHDSL ports and
local and remote loopback per timeslot on
internal E1 ports.
Performance statistics for the SHDSL and
Ethernet ports may be obtained and
analyzed via the Megaplex management
system.
SHDSL Access to SDH/SONET Networks
Dual-Color Indicator (per link)
Table 1. Typical Ranges

## Specifications  *(p.3)*

SHDSL PORTS
Number of Ports per Module
Compliance
ITU-T G.991.2 Annex A/B
(SHDSL Standard)
Line Power
Up to 16.8 dBm
Signal Format
TC-PAM
Transmission Line
Single unconditioned twisted pair
Impedance
135Ω
Connector
SCSI-40, convertible to 8 RJ-45 connectors
via adaptor cable
Typical Ranges
Depend on the data rate and the cable
diameter. For 26 AWG (0.4mm) cable with
13.5 dBm line power, see Table 1.
SFP Characteristics
For full details, see the SFP Transceivers
data sheet at www.rad.com
Lights steadily in green when the port is
connected and carries traffic
Data Rate
Range
Flashes in red during handshaking
between the M8SL port and the remote
unit
[kbps]
[km]
[ft]
10.6
35.000
8.2
27.000
Flashes in green when the port is
connected and is the standby port in a
redundancy pair
6.5
21.500
1544
4.9
16.200
2048
4.0
13.000
Lights in red during local loss of
synchronization or red alarm
Off when not connected
DIAGNOSTICS
ETHERNET PORTS
Performance Monitoring
Per ITU-T Rec G.991.2, G.826
Number of Ports
3 fiber-optic or 3 UTP
Loopbacks
Local and remote loopback on each SHDSL
port
Data Rate
10/100 Mbps (Fast Ethernet)
Autonegotiation
Local and remote loopback per timeslot on
each internal E1 port
Total Bandwidth per Module
100 Mbps per module
GENERAL
Maximum Frame Size
Power Consumption
1600 bytes
13.7W
Connectors
Environment
3 x RJ-45, shielded
3 x SFP socket (for transceivers, see
Ordering)
Operating temperature: -10°C to 50°C
(14°F to 122°F)
Storage temperature: -20°C to +70°C
(-4°F to +158°F)
Humidity: up to 95%, non-condensing
Indicators (ports ETH1, ETH2)
LINK (green) – LAN link integrity
ACT (yellow) – LAN data activity
M8SL
464-123-06/11 Specifications are subject to change without prior notice. © 1988–2011 RAD Data Communications Ltd. The RAD name, logo, logotype, and the terms EtherAccess, TDMoIP and TDMoIP Driven, and the
product names Optimux and IPmux, are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.

## Ordering  *(p.4)*

STANDARD CONFIGURATIONS
MP-4100M-8SL/3XUTP
SPECIAL CONFIGURATIONS
MP-4100M-8SL/#
Legend
# Interface and Connectors:
3XUTP
3 UTP (RJ-45 connectors)

## 3XNULL 3 SFP sockets without SFP transceivers  *(p.4)*

3XSFPa  3 SFP sockets including SFP
transceivers (see below for a)
a
SFP transceivers
Ethernet 100BaseFx Interface
Fast Ethernet/STM-1, 1310 nm,
multimode, LED, 2 km
(1.2 miles)
1D
Fast Ethernet/STM-1, DDM,
internal calibration, 1310 nm,
multimode, LED, 2 km
(1.2 miles)
Fast Ethernet/STM-1, 1310 nm,
single mode, laser, 15 km
(9.3 miles)
2D
Fast Ethernet/STM-1, DDM,
internal calibration, 1310 nm,
single mode, laser, 15 km
(9.3 miles)
Fast Ethernet/STM-1, 1310 nm,
single mode, laser, 40 km
(24.8 miles)
3D
Fast Ethernet/STM-1, DDM,
internal calibration, 1310 nm,
single mode, laser, 40 km
(24.8 miles)
10a
Fast Ethernet/STM-1,
Tx - 1310 nm, Rx - 1550 nm,
single mode (single fiber), laser
(WDM), 20 km (12.4 miles)
10b
Fast Ethernet/STM-1,
Tx - 1550 nm, Rx - 1310 nm,
single mode (single fiber), laser
(WDM), 20 km (12.4 miles)
18a
STM-1/OC-3, Tx - 1310 nm,
Rx - 1550 nm, 9/25 single mode
(single fiber), laser (WDM),
40 km (24.8 miles)
18b
STM-1/OC-3, Tx - 1550 nm,
Rx - 1310 nm, 9/25 single mode
(single fiber), laser (WDM),
40 km (24.8 miles)
19a
STM-1/OC-3, Tx - 1490 nm,
Rx - 1570 nm, 9/25 single mode
(single fiber), laser (WDM),
80 km (49.7 miles)
19b
STM-1/OC-3, Tx - 1570 nm,
Rx - 1490 nm, 9/25 single mode
(single fiber), laser (WDM),
80 km (49.7 miles)
Ethernet 100BaseTx (Electrical)
Interface
9F*
Fast Ethernet, RJ-45 connector,
100m (238 ft)
* Order this option only if an SFP electrical
transceiver is needed. Otherwise we
recommend the lower-cost 3xUTP option for
Fast Ethernet interface.
Notes.
-
For the complete list of SFPs, refer to the
SFP Transceivers data sheet.
-
It is strongly recommended to order M8SL with
original RAD SFPs installed. This will ensure that
prior to shipping, RAD has performed
comprehensive functional quality tests on the
entire assembled unit, including the SFP
devices. RAD cannot guarantee full compliance
to product specifications for M8SL units using
non-RAD SFPs.
OPTIONAL ACCESSORIES
CBL-MSL8-SCS40/RJ45
Cable for splitting the M8SL single 40-pin
SCSI connector to 8 x RJ-45 connectors.
Cable length is 2m (6 ft).
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