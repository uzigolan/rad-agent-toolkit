# Megaplex-4 Next Generation Multiservice Access Nodes

<!-- datasheet product=megaplex-4 family=mp4100 kind=system source=Megaplex-4.pdf -->

*Datasheet `Megaplex-4.pdf`, 9 pages. Product `megaplex-4`, family `mp4100` (system).

## Megaplex-4 Next Generation Multiservice Access Nodes  *(p.1)*

- Carrier-class multiservice platform: Ethernet services,
**high speed, low speed, analog voice, data, fiber multiplexing and pseudowire connectivity**
- Central solution aggregating Ethernet and TDM services
**over fiber/copper from RAD CPEs towards SDH/SONET and/or PSN core networks**
- MEF CE 2.0 certified, support of MEF applications: E-

## Line, E-LAN and E-TREE, with flexible mapping of user traffic into Ethernet flows  *(p.1)*

- Certified for IEEE-1613
Central site solution, major building block of RAD’s portfolio for
service providers, carriers and utilities, Megaplex-4 functions as
a carrier-class, TDM and Ethernet aggregator, as well as a high
capacity DS0 cross connect and next generation multiservice
access node. It transports legacy and next-generation services
over any infrastructure for seamless migration.
The Megaplex-4 family includes two devices: a larger 10-slot
Megaplex-4100 and a compact 4-slot Megaplex-4104.
When deployed as a carrier-class Ethernet aggregator,
Megaplex-4 can terminate Ethernet traffic carried over
E1/T1/SHDSL/SHDSL.bis/fiber links or native Ethernet copper and
fiber, as well as through a VCG in the SDH/SONET circuits. This
traffic can then be switched either to a different PDH/TDM trunk
or to Ethernet ports.
With RAD’s Service Assured Access (SAA) capabilities, Megaplex-
4 provides Carrier Ethernet functionalities, such as traffic
management (TM), standards-based operations, Administration
and Monitoring and Performance Monitoring (OAM&P).
Using pseudowire, Megaplex-4 provides legacy services over
packet-switched networks (PSN) making it a fundamental
building block in RAD’s Service Migration Hybrid Access solution.
Megaplex-4 converts the data stream from TDM/serial modules
in the MP-4100/4104 chassis (E1/T1, SHDSL, data or voice ports)
into IP or MPLS packets for transmission over Ethernet, IP or
MPLS networks.

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

Various users can benefit from the Megaplex-4 solution:
- SDH/SONET customers who need to maximize bandwidth
utilization of their network
- Subscribers with mixed Ethernet and TDM services
- Subscribers looking for a future-proof migration path to IP
connectivity
- Dual network owners using SDH/SONET for voice, and packet
for data.
Its ability to handle a broad range of Ethernet, data and voice
services, as well as a large variety of network technologies in a
single compact managed node, makes Megaplex-4 an ideal
core/edge solution for carriers and service providers. It also
provides a perfect fit for large enterprises, utilities and
transportation companies that require an efficient way to
transport and provision multiple legacy and next-generation
services over their high capacity pipes.

## Megaplex-4 RESILIENCY  *(p.2)*

Carrier-Class Reliability
Carrier-class service reliability ensures continuous availability
and sub-50ms restoration in the event of network outages
through system redundancy options, link and path protection
schemes and enhanced support for diverse ring topologies.
Traffic Duplication
Traffic Duplication, a unique technology available in Megaplex-4,
allows networks with mission-critical applications to enhance
reliability and performance. It can be used to minimize delay on
critical utility applications (such as Teleprotection) by capitalizing
on Carrier Ethernet reduced latency at higher speeds. Mission-
critical traffic can be transported over a new Carrier Ethernet
network running in parallel with the existing SDH/SONET
network, while preparing for future, full service migration.

## MANAGEMENT AND SECURITY  *(p.2)*

Megaplex-4 offers carrier-class provisioning features, including
end-to-end path management, to ensure continuous service
availability. Advanced SNMP management capabilities enable
Megaplex-4 to control and monitor all network elements:
SDH/SONET access and ring units, as well as remote POP and
first mile broadband access feeders and CPEs.
Figure 1.  Megaplex-4 as Multiservice Platform with Diverse Interfaces and Access Topologies for U&T Market Segment

## Megaplex-4 Specifications SDH/SONET INTERFACE  *(p.3)*

Number of Ports 2 per CL.2 module (4 per chassis)
Link Protection  1+1 unidirectional / bidirectional APS (G.841,
Clause 7.1)
1+1 bidirectional optimized APS (G.841 Annex B.
Linear Multiplex Section (MSP)
Path Protection 1+1 unidirectional APS (G.842,Clause 6.2.3)  -
Ring interworking with a SNCP ring
Line Coding
NRZ
Connectors
SFP socket
Data Rate
STM-4/OC-12: 622.08 Mbps ± 4.6 ppm
STM-1/OC-3:155.52 Mbps ± 4.6 ppm
Compliance
SDH: ITU-T G.957, G.798, G.783
SONET: ANSI T1.105-1995, GR-253-core
GFP (Generic Framing Procedure): ITU-T G.7041,
ANSI T1-105.02, framed mode
LCAS (Link Capacity Adjustment Scheme): ITU-T
G.7042
Framing
SDH: ITU-T G.707, G.708, G.709
SONET: GR-253-core

## ETHERNET INTERFACES  *(p.3)*

Number of Ports 2 per CL.2 module (4 per chassis)
Data Rate
10/100/1000 Mbps
Autonegotiation (copper interface only)
Connectors (per
port)
RJ-45, shielded
SFP socket
Maximum Frame
Size
9600 bytes (for max. frame sizes supported by
different I/O modules, see individual data sheets)
Compliance
CE 2.0, MEF 6 (E-Line – EPL and EVPL, E-LAN –
EPLAN and EVPLAN, E-TREE), MEF 10, MEF 9,
MEF 8 MEF 14, MEF 20, IEEE 802.3, 802.3u,
802.1q, 802.1p, 802.1X, 802.3ad, 802.3-2005,
802.3ah, 802.1ag, ITU-T Y.1731, G.8032
Service
EPL and EVPL (flow-based)
E-LAN (EP-LAN and EVP-LAN), bridge-based
E-TREE (bridge-based)
Bandwidth
Profile
CIR/CBS, EIR/EBS per flow
Forwarding
Mode
Flow-based, bridge-based
MAC Address
Table
Up to 16K entries with configurable limiter
Operation Mode VLAN-aware, VLAN-unaware
ETH
STM-1/
OC-3
Voice
Data
E3 Chanellized
E1/T1
FE
STM-4/
OC-12
ETH
FE
FE
Wireless
FE/GbE
POP
PSN
SDH/SONET
Megaplex-2100/
Megaplex-2104
ETX
Router
Video
Airmux
Megaplex-4104
Radio
Radio
T3
T3
Airmux
RV Station
Megaplex-4
Figure 2.  Megaplex-4 as a Central Site Aggregator for different RAD CPEs, Ethernet and TDM Aggregator for SDH/SONET and PSN

## Megaplex-4  *(p.4)*

OAM
IEEE 802.3ah
IEEE 802.1ag: CCM, Loopback, link trace, MEP
ITU-T Y.1731, Frame-loss, Frame-delay, Frame-
delay-variation, PM
Protection
Link aggregation supporting link and equipment
protection
Ethernet Ring Protection Switching complying
with ITU-T G.8032 Hitless Switching Redundancy
in Ring topology according to IEC 62439-3
RSTP on network ports (CL.2/A)

## SDH/SONET AND GBE SFPS  *(p.4)*

For full details, see the Pluggable Transceivers data sheet at
- All SFPs listed for STM-4/OC-12 and STM-1/OC-3 are
supported by the SDH/SONET link except for those with
external calibration
- All SFPs listed for GbE are supported by the GbE link, except
for those with external calibration and SGMII.
Note: It is strongly recommended to order this device with original RAD
SFPs installed. This will ensure that prior to shipping, RAD has performed
comprehensive functional quality tests on the entire assembled unit,
including the SFP devices. RAD cannot guarantee full compliance to
product specifications for units using non-RAD SFPs.
**I/O MODULES**
See Table 1. For detailed description, see separate data sheets.

## MANAGEMENT  *(p.4)*

Ethernet
Management
Port
Interface: 10/100BaseT
Connector: RJ-45
Control Port
Interface: RS-232/V.24 (DCE)
CL.2 connectors: DB-9
CL.2/4104 connectors: MINI-USB
Connectivity
Out-of-band
Inband, via the STM-4/OC-12/STM-1/OC-3 links or
over a dedicated timeslot in any E1/T1 or SHDSL link
or via any of the user Ethernet ports
Tools
Telnet/SSHv2, SNMPv2, SNMPv3, SFTP
RADIUS, TACACS+
Options
CLI
RADview management and VF orchestration suite
Standalone Shelf View application

## Megaplex-4 TIMING  *(p.5)*

Clock Sources Recovered from the STM-4/OC-12/
STM-1/OC-3 interface, including automatic
selection, based on SSM (Synchronization Status
Messaging)
Sync-E clock, recovered from the GbE interface
(CL.2/A modules only)
Internal crystal free-running oscillator-based clock
Derived from the Receive clock of a specified user
port
Adaptive clock recovered (ACR) from a pseudowire
circuit
Clock distribution mechanism (SSM-like) over E1
TS0 interoperable with Nokia proprietary timing
mechanism.
Station Clock  1.544 Mbps (T1) (AMI)
1544 sine wave (via AMI-SINE-1544-WAVE-CONV
optional accessory)
2.048 Mbps (E1) (AMI)
2.048 MHz squarewave
Connector: RJ-45

## SECURITY  *(p.5)*

Port-Based
Network Access
Control (PNAC)
As per IEEE 802.1X-2100
Port-based authorization
Supplicant for CL.2/A GbE ports
Authenticator applicable on M-ETH modules and VS
modules with Ethernet ports
MAC-based
authentication
support
802.1X-based
Key exchange based on 802.1X

## DIAGNOSTICS  *(p.5)*

Alarm Relay
1 inbound relay – RS-232 levels (dry contact)
2 outbound relays triggered by major/minor alarms
Operation: normally open, normally closed, using
different pins
CL.2 connector: DB-9, female
CL.2/4104 connector: 9-pin, flat
Figure 3. TDM Migration

## Megaplex-4  *(p.6)*

Table 1. Megaplex-4 I/O Modules
Module
Description
Operating in
MP-2100/2104
System Modules
CL.2/A
Common Logic module, Carrier Ethernet class
PS
AC or DC power supply module
I/O Modules
(in alphabetical order of names)
M-ETH
8-port GbE interface module
T3
T3 multiplexer module
TP (Teleprotection)
4-input, 8-output port teleprotection module with selectable trip voltage
VC-4/4A/8/8A/16
4/8/16-port FXS/FXO/E&M PCM and ADPCM analog voice modules
Yes
VC-4/OMNI
4-port PCM omnibus voice module
Yes
Note: For specific HW/SW versions of Megaplex-210x modules supported by the Megaplex-4 chassis, please contact your local RAD partner.

## Megaplex-4 GENERAL  *(p.7)*

Environment
Storage
Temperature
-20°C to +70°C (-4°F to +160°F)
Operating
Temperature,
MP-4100
Regular: -10°C to 55°C (14°F to 131°F)
IEEE-1613 “no-fan” compliant system and modules:
-20°C to 55°C (-4°F to 131°F)
Operating
Temperature,
MP-4104
-10°C to 55°C (14°F to 131°F)
Humidity
up to 95%, non-condensing
Note: Actual operating temperature range is determined by the specific
modules installed in the chassis. For extended operating temperature
ranges, contact your local RAD Business Partner.
Physical - Chassis
MP-4100 (4U-
high)
MP-4104 (2U-high)
Power supply module
slots
CL. 2 module slots
Slots for I/O modules
Height
18 cm (7 in) (4U)
9 cm (3.5 in) (2U)
Width
44 cm (17 in)
44 cm (17 in)
Depth (regular)
33 cm (13 in)
33 cm (13 in)
Depth
(IEEE-1613-compliant)
37 cm (14.6 in)
-
Weight, max (fully
loaded chassis)*
15.3 kg (33.8 lb)
7.54 kg (16.6 lb)
Note: The chassis weight depends of the type and number of installed
modules.
Physical – CL Modules
CL.2
CL.2/4104
Height
17.3 cm (6.8 in)
17.3 cm (6.8 in)
Width
4.5 cm (1.8 in)
2.5 cm (1 in)
Depth (regular)
32.5 cm
32.5 cm (12.8 in)
Depth (IEEE-1613-
compliant)
35 cm (13.8 in)
-
Max weight (regular)
630g (1.3 lb)
540 g (1.2 lb)
Max weight (IEEE-1613-
compliant)
2030g
-
Table 1. Megaplex-4 I/O Modules (cont.)
Module
Description
Operating in
MP-2100/2104
VS-12
12-port serial module with 2 Ethernet ports
VS-6/703
6-port serial module with 8 64-kbps G.703 codirectional interfaces and 1 Ethernet port
VS-6/BIN
6-port serial module with 8 binary in/out command ports and 1 Ethernet port
VS-6/C37
6-port serial module with 2 fiber optic C37.94 ports and 1 Ethernet port
VS-6/E&M
6-port serial module with 4 E&M voice ports and 1 Ethernet port
VS-8/E&M
Voice module with 8 E&M ports
VS-FXS/E&M
Voice module with 4 E&M ports and 8 FXS ports
VS-6/FXO
6-port serial module with 8 FXO voice ports and 1 Ethernet port
VS-6/FXS
6-port serial module with 8 FXS voice ports and 1 Ethernet port
VS-16E1T1
16-port E1/T1 module with PW or EOP support
VS-6/E1T1
6-port serial module with 8 E1/T1 ports, 1 Ethernet port and PW support
VS-OCU/E&M
2-channel OCU-DP module  with 4 E&M ports

## Megaplex-4  *(p.8)*

Power
MP-4100
Power Supply
Input
AC: 115 /230 VAC (allowed range: 85 to 264 VAC),
50/60 Hz
HVDC support: 100 to 360 VDC
DC: 48 VDC (allowed range: -36 to -56 VDC);
selectable ground reference or floating ground
MP-4104
Power Supply
Input
AC: 90 to 264 VAC, 50/60 Hz
HVDC support: 110 to 300 VDC
DC:  48 VDC (allowed range: -36 to -56 VDC);
selectable ground reference or floating ground
Maximum
Input Power
MP-4100: 315W + power supplied for ring and feed
voltage
MP-4104: 200W + power supplied for ring and feed
voltage
Maximum
Output Power
MP-4100 Regular: 250W
MP-4100 IEEE-1613 “no-fan” compliant system and
modules: 175W
MP-4104: 160W + power supplied for ring and feed
voltage
Power
Consumption
Per CL, max: 27.75W
**Ordering**
Megaplex-4 must be ordered with the RADcare Basic Plus service
package for one year.

## CHASSIS  *(p.8)*

MP-4100-MN
Megaplex-4100 chassis (regular) with
no PS or CL.2 module
MP-4100-MN/H1
Megaplex-4100 IEEE-1613 compliant
chassis with no PS or CL.2 module
MP-4100-2/!/*/SA
Megaplex-4100 chassis equipped with
PS and CL.2 modules
MP-4100-1613/!/*/SA IEEE-1613 compliant Megaplex-4100
chassis equipped with IEEE-1613
compliant PS and IEEE-1613 compliant
CL.2 modules
!
Power supply modules
115R
Single/dual, 115 VAC (including HVDC
support of 100 to 360 VDC)
230R
Single/dual, 230 VAC (including HVDC
support of 100 to 360 VDC)
48R
Single/dual, -48 VDC
AC48
One AC PS (HVDC support of 100 to
360 VDC) + one -48 VDC PS
MP-4104-MN
Megaplex-4104 chassis with no PS or
CL.2 module
MP-4104-2/!/*/SA
Megaplex-4104 chassis equipped with
PS and CL.2 modules
!
Power supply modules
48R
Dual, -48 VDC
ACR
Dual, 90 VAC to 260 VAC  (including
HVDC support of 110 to 300 VDC)
*
Link
DS0
DS0R
Single/dual CL.2 modules without
SDH/SONET and without GbE links
622GBEASFP
622GBEAUTP
622GBEASFPR
622GBEAUTPR
Single/dual CL.2 modules with
SDH/SONET SFP sockets and GbE,
Carrier Ethernet class
GBEASFP
GBEASFPR
Single/dual CL.2 modules without
SDH/SONET sockets and with GbE,
Carrier Ethernet class
SA
SW key activation for full STM-4/OC-12 capabilities
(Default=full STM-4/OC-12 capabilities)
155SK
SW key activation for
STM-4/OC-12
Recommended Chassis Configurations
MP-4100-2/48R/622GBEASFPR
MP-4104-2/48R/622GBEASFPR
MP-4100-2/230R/622GBEASFPR
MP-4100-2/115R/622GBEASFPR
MP-4104-2/ACR/622GBEASFPR
MP-4100-2/115R/GBEASFPR
MP-4104-2/48R/GBEASFPR
MP-4100-2/48R/DS0R
MP-4104-2/48R/DS0R

## POWER SUPPLY MODULES  *(p.8)*

MP-4100M-PS/~
Power supply module for MP-4100
~
Power
Single, 115 VAC  (including HVDC
support of 100 to 360 VDC)
115/H1
Single, 115 VAC  (including HVDC
support of 100 to 360 VDC),
IEEE-1613 compliant
Single, 230 VAC  (including HVDC
support of 100 to 360 VDC)
Single, -48 VDC
48/H1
Single, -48 VDC, IEEE-1613
compliant
MP-4104M-PS/~
Power supply module for MP-4104
~
Power
Single, -48 VDC
AC
Single, 90 VAC to 260 VAC
(including HVDC support of 110 to
300 VDC)

## Megaplex-4  *(p.9)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel/Fax 972-52-4748272 | Fax 972-3-6498250
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
464-101-12/24 (4.91) Specifications are subject to change without prior notice. © 1988–2024 RAD Data Communications Ltd. The RAD name, logo, logotype, and the product
names Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their
respective holders.

## CL MODULES  *(p.9)*

MP-4100M-CL.2/#/SA/$
CL.2 module for Megaplex-4100
MP-4104M-CL.2/#/SA
CL.2 module for Megaplex-4104
#
Link
DS0
No SDH/SONET and no GbE links
622GBEAUTP
622GBEASFP
SDH/SONET SFP sockets and GbE
interface, Carrier Ethernet class
GBEAUTP
GBEASFP
No SDH/SONET sockets, GbE
interface, Carrier Ethernet class
SA
SW key activation for full STM-4/OC-12 capabilities
(Default=full STM-4/OC-12 capabilities)
155SK
SW key activation for STM-4/OC-12
$
IEEE-1613 compliance for CL module (Default=not
compliant):
H1
IEEE-1613 compliant
Note: CLI prompt and/or SDH/SONET path trace string can be changed
(factory-set) according to the customer request.
Recommended CL Configurations
MP-4100M-CL.2/622GBEASFP
MP-4104M-CL.2/622GBEASFP
MP-4100M-CL.2/GBEASFP
MP-4104M-CL.2/GBEASFP
MP-4100M-CL.2/DS0
MP-4104M-CL.2/DS0

## SUPPLIED ACCESSORIES (MEGAPLEX-4100)  *(p.9)*

CBL-SP-9/SH
Dual DB-9 to single DB-9 control cable (only with MP-4100-2)
RM-MP-MX-23/19
Hardware kit for mounting one MP-4100 unit into both 19-inch
and 23-inch racks (only with MP-4100-2)

## SUPPLIED ACCESSORIES (MEGAPLEX-4104)  *(p.9)*

CBL-MUSB-DB9F
Mini-USB to DB-9 control cable (only with MP-4104-2)
PLUG-DC/TB/S/E
DC plug
RM-42
Hardware kit for mounting one MP-4104 unit in a 19-inch rack
(only with MP-4104-2)

## OPTIONAL ACCESSORIES (MEGAPLEX-4100)  *(p.9)*

MP-2100-RM-ETSI/19
Hardware kit for mounting one MP-4100 unit into ETSI racks (fits
also 10-inch racks)
Note: This RM can be either ordered in addition to RM-MP-MX-
23/19 or received for free instead of it.
RM-51
Thermal isolation panel for mounting two fanless MP-4100
devices in 19" rack

## OPTIONAL ACCESSORIES (MEGAPLEX-4104)  *(p.9)*

CBL-MP-4104/AR/OPEN/2M
Open-ended alarm cable
PLUG-DC/TB/S/E
DC plug
RM-42-CM
Hardware kit for mounting one MP-4104 unit in a 19-inch rack
with cable management
WM-42
Hardware kit for installing MP-4104 unit on a wall
WM-42-CM
Hardware kit for installing a MP-4104 unit on a wall with cable
management

## LICENSES  *(p.9)*

MP-4100-LIC/622SK
SW license key for enabling STM-4/OC-12 in Megaplex-4100 (per
CL module, only when 155SK option is ordered)
MP-4104-LIC/622SK
SW license key for enabling STM-4/OC-12 in Megaplex-4104 (per
CL module, only when 155SK option is ordered)