# Megaplex-1 Multiservice Pseudowire Access Gateway

<!-- datasheet product=megaplex-1 family=mp1 kind=system source=mp-1_ds-2_2_0.pdf -->

*Datasheet `mp-1_ds-2_2_0.pdf`, 10 pages. Product `megaplex-1`, family `mp1` (system).

## Megaplex-1 Multiservice Pseudowire Access Gateway  *(p.1)*

- Grooming, consolidating and transmitting analog voice
and TDM-based services over Ethernet, IP or MPLS
networks using standard-compliant pseudowire
technology
- Bridge functionality for packet switched networks with 2
optical/copper GbE uplinks and up to 4 FE user
interfaces
- Hitless PW redundancy
- Wide range of services including: E1/T1, FXS or E&M
toll-quality analog voice channels, IEEE C37.94-
compliant optical tele-protection, programmable serial
ports
- 1U, 19” fanless enclosure with redundant wide-range
power supply (AC and DC)
Megaplex-1 is a multiservice pseudowire gateway that
transports analog and TDM traffic (originating from legacy
circuit-switched networks) over packet-switched networks
(PSNs).

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

Various customers can benefit from the Megaplex-1 solution:
- Users with mixed Ethernet and TDM services
- Users looking for a future-proof migration path to IP
connectivity
- Owners of facilities sensitive to space or climate constraints
Its ability to handle a broad range of Ethernet, data and voice
services in a single compact managed node, makes Megaplex-1
an ideal access solution for diverse network operators and
service providers. It also provides a perfect fit for utilities and
transportation companies that require an efficient way to
transport and provision multiple legacy and next-generation
services over their high capacity pipes.
EN50121-4 compliant ordering options are certified for railway
applications.

## SERVICES  *(p.1)*

Megaplex-1 provides a variety of services, via its many user
interfaces, such as:
-
E1/T1
-
IEEE C37.94 fiber optic teleprotection
-
Serial synchronous/asynchronous data
-
Voice (FXS, E&M)
-
Fast Ethernet (10/100BASE-T)

## ETHERNET SWITCH  *(p.1)*

Megaplex-1 features a powerful internal Layer-2 Ethernet switch
that provides Ethernet user ports with rate limiting and VLAN-
based/port-based classification capabilities.
Megaplex-1 includes the following Ethernet ports:
- Two fiber optic or copper Gigabit Ethernet network (NNI)
ports
- Four or two copper Fast Ethernet user (UNI) ports (depending
on ordering options)
- One copper FE port for out-of-band management.

## Megaplex-1  *(p.2)*

The GbE Network (NNI) ports provide the physical connection to
the packet switched network. These ports provide Megaplex-1
with a multirate FE/GE interface, for optical or electrical media,
and can be ordered with one of the following interfaces:
- 10/100/1000BASE-T copper ports. These ports support
autonegotiation, with user-specified advertised data rate (10,
100 or 1000 Mbps) and operating mode (half- or full-duplex).
Alternatively, autonegotiation can be disabled and the rate
and operating mode be directly specified.
The ports also support automatic polarity and crossover
detection, and polarity correction, for connection through
any type of cable to any type of Ethernet port (hub or
station).
- SFP sockets, for installing 100/1000BASE-FX SFP plug-in
modules. Support for standard SFP optical transceivers for
the GbE link interfaces enables selecting the optimal
interface for each application. These ports do not support
autonegotiation. RAD offers a wide variety of SFPs, for
meeting a wide range of operational requirements.
The UNI Ethernet interface has two or four 10/100BASE-T
interface terminated in RJ-45 connectors capable of
autonegotiation. Users can configure the advertised data rate
(10 or 100 Mbps) and operating mode (half-duplex or
full-duplex). Alternatively, autonegotiation can be disabled, and
the rate and operating mode be directly specified. In addition to
autonegotiation, MDI/MDIX polarity and cross-over detection
and automatic cross-over correction are also supported.

## PSEUDOWIRE  *(p.2)*

The device uses its embedded pseudowire engine to encapsulate
the user services for low-latency transmission over
packet-switched networks.
The powerful pseudowire engine in devices with 8 E1/T1 ports
provides up to 16 protected (or up to 32 unprotected) PWs with
up to 31 timeslots per each PW port. All other Megaplex-1
devices provide up to 6 protected (or up to 12 unprotected) PWs
with up to 31 timeslots per each PW port.
A remote pseudowire device converts the packets back to the
original user traffic format.
E1/T1
Megaplex-1 has 8 independently configurable E1/T1 ports.
The E1 interface is compatible with all carrier-provided E1
services, meeting the requirements of ITU-T Rec. G.703, G.704
and G.732.
It operates in framed mode as per G.732, as well as in unframed
mode. CRC-4 is also supported, complying with G.704
recommendations. Zero suppression over the line is HDB3.
The T1 interface is compatible with ANSI requirements. Both D4
and ESF framing formats are supported. Line code is selectable
for AMI or B8ZS.

## SERIAL DATA TRAFFIC  *(p.2)*

The serial data rates are independently selectable for each
channel and depend on the selected encapsulation mode:
- None: each channel operates at high-speed rates of n×56 or
n×64 kbps, where n = 1 to 31 (that is, maximum 1984 kbps).
- V110: each channel operates at low-speed sync rates of 2.4,
4.8, 9.6, 19.2 or 38.4 kbps, performing rate adaptation in
accordance with ITU-T Rec. V.110.
- 3-bit transitional: the interface provides transitional
encoding to transmit asynchronous data at rates up to
19.2/38.4 kbps. It operates by encoding asynchronous data in
a 3-bit transitional code, which is then transmitted over the
Megaplex uplink at a rate of 64/128 kbps. This mode covers
all asynchronous character formats.
The interface terminates in one or two 68-pin SCSI-4 female
connectors (according to the ordering option). Each connector
includes 3 channels. This provides a simple and easy
SW-configurable selection of serial interface (V.35, RS-422 or
RS-232) according to the deployment needs.
Adapter cables, available upon order, are offered by RAD to split
each connector into three separate channel interfaces with
standard connectors: V.35, RS-530, RS-232, X.21 or V.36/RS-449.
Each channel has local support of interface control signals (CTS,
RTS, DCD, DSR and DTR). In addition, each channel can be
configured to transmit control signals end-to-end.
Table 1.  Transmit and Receive Levels for Voice Interfaces
Interface
Transmit
[dbm]
Receive
[dbm]
min
max
min
max
E&M 2W
-8
+5
-17
+2
E&M 4W (when there is a
mix of 2W/4W ports)
-8
+5
-17
+3.5
E&M 4W (all ports)
-17
+5
-17
+9
FXS
-5
+5
-17
+1

## Megaplex-1 OPTICAL TELEPROTECTION  *(p.3)*

The interface can be used for both user and network ports –
either for inter-substation communication or for transmitting
distance teleprotection information.
The dual-port fiber optic interface operates at a nominal
wavelength of 850 nm and nominal line rate of 2.048 Mbps. Each
port is terminated in a pair of ST connectors for connection to
standard multimode fiber.
The interface complies with IEEE C37.94 standard for distances
of up to 2 km.

## VOICE TRAFFIC  *(p.3)*

The voice interface provides 8 FXS or 4 E&M toll-quality analog
voice channels. Voice signals are digitized using PCM, in
compliance with ITU-T G.711 and AT&T Pub. 43801 standards.
Encoding and decoding are in full compliance with ITU-T
requirements G.711. Voice channel companding is selectable for
A-law or µ-law.
The E&M interface operates with different types of E&M
signaling: EIA RS-464 Types I, II, III and V (British Telecom SSDC5).
Both 2-wire and 4-wire lines are supported (user-selectable).
The E&M interface provides EIA RS-464 Type I signaling without
the need for an external DC power supply. For other signaling
types, the internal -12 VDC provided by the chassis is sufficient
for connection to most PBX systems.
However, for full support of EIA RS-464 Types II, III and
V (BT SSDC5) standards, a -48 VDC power source is required.
The E&M interface provides signaling at +12V for applications
that require positive signaling voltage (for example, radio
transmitters) and perform fault propagation.
The FXS interface employs both loop-start and wink-start
signaling methods. FXS interfaces are typically used for direct
connection to 2-wire telephones in the following loop-start
applications:
- Off-Premises Extension (OPX), where a local telephone on
the PBX can be connected to an off-premises telephone, by
dialing only the extension number;
- Private Line, Automatic Ringdown application (PLAR) (also
referred to as Hot Line), where two telephones are
connected directly via the E1/T1 link. When the telephone on
one side goes off-hook, the other telephone rings;
- Direct connection to 2-wire telephones in PSTN applications.
ETH
ETH
Packet
Network
ETH
Voice
IED
Hot Line
RTU
Dry Contacts
Megaplex-1
Teleprotection
Megaplex-1/
Megaplex-4
ETH
IED
Hot Line
RTU
RADview
Dry Contacts
Teleprotection
E1/T1
Figure 1.  Substation Connectivity over Packet Network

## Megaplex-1  *(p.4)*

When operating in PCM mode, battery polarity is reversed for
wink-start signaling, used in direct inward dialing (DID)
applications.
Megaplex-1 includes power components required for E&M and
FXS interfaces.
Gain control is user-selectable for both receive and transmit
directions, enabling easy installation in all environments.

## RESILIENCY  *(p.4)*

Service reliability in Megaplex-1 is based on the following
resiliency features:
- Fanless operation
- Redundant wide range power supply
- Dual NNI ports
- Hitless PW protection

## MANAGEMENT AND SECURITY  *(p.4)*

The device can be managed via RADview, RAD’s carrier-class
NMS, or any SNMP-based management system. Megaplex-1
supports a variety of access protocols, including CLI over Telnet,
SNMPv3, and TFTP. Security features include SNMPv3, RADIUS
(client authentication), TACACS+ (client authentication,
authorization, and accounting), SSH, and SFTP. Access Control
Lists (ACL) can also be used to flexibly filter and mark
management traffic, enabling service providers to maintain
network security by dropping unwanted packets.

## MONITORING AND DIAGNOSTICS  *(p.4)*

Comprehensive diagnostic capabilities include:
- Local and remote loopbacks
- Real-time alarms to alert the user on fault conditions
Megaplex-1 collects statistics per physical port and per
connection for 15-minute intervals, which enables the network
operator to monitor the transmission performance and thus the
quality of service provided to users, as well as identify
transmission problems. Statistics for the last 24 hours are stored
in the device and can be retrieved by the network management
station.
The Performance Management Portal is an SLA assurance system
that is part of the RADview management system, enabling real-
time monitoring of Ethernet service performance by collecting
KPI data from RAD devices.
2-Way Radio
2-Way Radio
FXS
Ring Down
4E&M
Megaplex-1
Carrier
PSN
FXS
Ring Down
ETH
4E&M
ETH
Megaplex-1
Base Station
Base Station
Figure 2.  TDM Leased Line Services Migration to Packet Switched Networks operating with FXS Ring Down and E&M (2 or 4
Wire)

## Megaplex-1 Specifications E1 INTERFACE  *(p.5)*

Compliance
ITU-T G.703, G.704, G.732
Framing
Framed per G.732:
-
with or without CAS
-
with or without CRC-4
Unframed
Data Rate (per
port)
2.048 Mbps
Line Code
HDB3
Signal Level
Receive: 0 to -12 dBm
Transmit:
Balanced:  ±3V (±10%)
Unbalanced:  ±2.37V (±10%)
Jitter
Performance
As per ITU-T G.823
Impedance
Balanced 4-wire: 120Ω
Unbalanced coax: 75Ω

## T1 INTERFACE  *(p.5)*

Compliance
ANSI T1.107 and T1.403
Framing
ESF, D4
Data Rate (per
port)
1.544 Mbps
Line Code
AMI, B8ZS
Signal Level
Receive: 0 to -12 dBm
Transmit: 0.6, 1.2, 1.8, 2.4, 3.0 dBm
user-adjustable, measured at 0 to 655 ft
Jitter
Performance
As per AT&T TR-62411
Impedance
Balanced 4-wire: 100Ω
Connectors
DB-44, female (see Ordering for cables available
from RAD)

## SERIAL INTERFACE  *(p.5)*

Encapsulation
Modes and
Data Rates
None: n×56 or n×64 kbps (n = 1 to 31)
V110: 2.4, 4.8, 9.6, 19.2, 38.4 kbps
3-bit-transitional: 64 kbps, 128 kbps
Interface
(Electrical)
V.24/RS-232, V.35 or V.11/RS-422
RS-485 (4-wire master only)
Interface
(Physical)
V.24/RS-232, V.35, V.36/RS-449, RS-530, X.21 (via
adaptor cables)
Connectors
One/two 68-pin SCSI, female (one per 3 data
channels)
Interface
Control
Signals
Local support for all types of control signals
End-to-end transfer of local RTS and DTR lines
Signal Format Asynchronous or synchronous, full duplex
Clock Mode
DCE (channel provides both RX and TX clocks to the
user DTE)
Diagnostics
(per port)
Local digital loopback
Remote digital loopback

## C37.94 INTERFACE  *(p.5)*

Compliance
IEEE C37.94, optical part
Number of Ports
Connectors
Pair of ST connectors, female
Nominal Data
Rate
2.048 Mbps
Wavelength
850nm ± 40nm
Fiber Type
62.5/125 µm multimode
50/125 µm multimode
Transmitter Type LED
Power Coupled
into Fiber
62.5/125 µm: -11 to -19 dBm
50/125 µm: -11 to -23 dBm
Minimum
Receiver
Sensitivity
-32 dBm
Maximum
Receiver Input
Power
-11 dBm
Receiver Dynamic
Range
21 dB
Range (Typical)
2 km/1.25 miles

## Megaplex-1  *(p.6)*

LED Indicators
SYNC (green/red):
-
Lights steadily in green – the corresponding
port is operating properly
-
Flashes in green – the corresponding port is
operating properly, but serves as the
standby port when link protection is
enabled
-
Lights in red – the corresponding port
detects loss of synchronization or loss of
signal
-
Flashes in red – the corresponding port
serves as the standby port, and detects loss
of synchronization
REM SYNC (yellow):
-
On – the corresponding port detects loss of
remote synchronization
-
Off – the corresponding port is not
connected.
Diagnostics (per
port)
Local digital loopback
Remote digital loopback

## VOICE INTERFACE – GENERAL  *(p.6)*

Voice Encoding
Technique
Per ITU-T G.711 and AT&T Pub. 43801, µ-law or
A-law
Diagnostics
Local digital loopback for each channel, towards
the local user equipment
Remote digital loopback for each channel,
towards the remote user equipment
1 kHz, 0 dBm0 test tone injection for each
channel, towards the remote user equipment
1 kHz, 0 dBm0 backward test tone injection for
each channel, towards the local user equipment
Nominal level
0 dBm
Nominal
Impedance
600Ω
Return loss (ERL)
at 300 to 3400 Hz: better than 20 dB
Frequency
response
(Ref:1020 Hz)
±0.5 dB at 300 to 3000 Hz
±1.1 dB at 250 to 3400 Hz
Level adjustment Soft-selectable, see Table 1
Steps
0.5 dB (±0.5 dB), nominal
Signal to total
distortion (G.712)
-30 to 0 dBm0: better than 33 dB
-45 to +3 dBm0: better than 22 dB
Idle channel noise better than -65 dBm0 (+25 dBrnc)
Far-end cross-talk
(2W&4W)
-65dBm0 max
Go-to-return
cross-talk (4W)
-60dBm0 max

## E&M INTERFACE  *(p.6)*

Number of Ports
Line Type
4-wire or 2-wire (soft-selectable)
Connectors
4 x RJ-45
Signaling Method
(selectable)
EIA RS-464 Type I
EIA RS-464 Types II, III, and
V (British Telecom SSDC5) using -12 VDC in
place of -48 VDC
Note: For full support of Types II, III, and V
(SSDC5) signaling standards, -48 VDC power
supply is required.
Pulse Dial Distortion ±2 ms max
Transformer
Isolation
1500 VRMS
Indicators
M – On when the M line of the corresponding
channel is off-hook (channel in use)
E – On when the E line of the corresponding
channel is off-hook (channel in use)

## FXS INTERFACE  *(p.6)*

Number of Ports
Line Type
2-wire (ITU-T standard: G.712)
Connectors
4 x RJ-12 (one per two channels)
Signaling Methods
EIA RS-464 loop-start or wink-start
On-Hook/Off-Hook
Threshold
Off-Hook: Loop current >11 mA
On-Hook: Loop current <8 mA
Indicators
Number: 8
Color: green/yellow
Name: LOC/REM
Lights steadily in green – Local “OFF-HOOK”
Lights steadily in yellow – Remote
“OFF- HOOK”
Flashes in green/yellow – Local and Remote
“OFF-HOOK”/conversation state
Off: port is not connected or both directions
of signaling are “ON-HOOK”
Loop Resistance
Min: 300Ω
Max: 1600Ω
Feed Current
20 mA (±10%) per active channel
Reverse Polarity
Pulse Distortion
6 ms max
**Megaplex-1**
-48 VDC (nominal)
Current
Consumption
30 mA (±10%) per active channel

## GBE INTERFACE  *(p.7)*

Number of Ports
2 UTP copper (RJ-45 shielded) or 2 SFP
sockets
Data Rate
UTP: 10/100/1000 Mbps
SFP: 100/1000 Mbps
Autonegotiation
copper only
Frame Size
9140 bytes
LED Indicators
LINK On (green): Link is up
LINK Off: Link is down
ACT Flashes (yellow): Data is being
transferred
ACT Off: No data transfer
SFP Transceivers
For full details, see the SFP/XFP Transceivers
data sheet on www.rad.com
Note. It is strongly recommended to order
this device with original RAD SFPs. RAD
cannot guarantee full compliance to product
specifications for units using non-RAD SFPs.

## FAST ETHERNET INTERFACE  *(p.7)*

Number of Ports
4 x 10/100BaseT
Data Rate
10/100 Mbps (Fast Ethernet)
Autonegotiation
Connectors
RJ-45, shielded
Frame Size
9140 bytes
LED Indicators
LINK On (green): Link is up
LINK Off: Link is down
ACT Flashes (yellow): Data is being
transferred
ACT Off: No data transfer

## PSEUDOWIRE  *(p.7)*

Standard
Compliance
IETF: RFC 4553 (SAToP), RFC 5086 (CESoPSN)
MEF 8
Number of PW
Connections
Unprotected:
-
Device with 8 E1/T1 ports – up to 32
-
Other models – up to 12
Fully protected:
-
Device with 8 E1/T1 ports – up to 16
-
Other models – up to 6
Jitter Buffer Size
0.25 –256 ms, in 1 μs steps with 125 μs
granularity (the value entered by the user is
rounded upward to the closest n*125 μs
value)
Diagnostics (per DS1
port or timeslot)
Local digital loopback
Remote digital loopback

## MANAGEMENT  *(p.7)*

Connectivity
Out-of-band, via serial control or Ethernet
management port
Inband, via NNI Ethernet ports
Control Port
RS-232 interface, RJ-45 connector
Ethernet
Management
Port
Interface: 10/100/1000BASE-T
Autonegotiation
Connector: RJ-45
Tools
Telnet/SSHv2, SNMPv3, SFTP
RADIUS, TACACS+
Options
CLI
RADview management and VF orchestration suite
Standalone Shelf View application

## Megaplex-1 TIMING  *(p.8)*

Clock Sources Internal crystal free-running oscillator-based clock
Derived from the receive clock of a specified user
port
Adaptive clock recovered (ACR) from a pseudowire
circuit
External station clock
Internal Clock
Quality
ST-4
ACR (Adaptive
Clock
Recovery)
Supports jitter and wander requirements according
to G.8261, G.823 and G.824 traffic interface
recommendations with quality precision of ±16 ppb
Station Clock
Line code: AMI/HDB3/B8ZS
Mode: Input and output
Impedance:
120Ω, balanced
75Ω, unbalanced (via adapter cable)
Bit rate:
2.048 Mbps (E1)
1.544 Mbps (T1)
Connector: RJ-45

## DIAGNOSTICS  *(p.8)*

Alarm Relay
1 inbound relay – RS-232 levels (dry contact)
2 outbound relays triggered by major/minor alarms
Operation: normally open, normally closed, using
different pins
Loopbacks
Local and remote loopbacks (see under various
interfaces)
BERT per timeslot of internal DS1 port

## GENERAL  *(p.8)*

Power
Power Supply
AC: 100-240 VAC (±10%), 50/60 Hz
DC: 48 VDC (40-300 VDC)
Autodetection
Power
Consumption
35W (max)
28W (typical)
22W (min)
Physical
Height
44 mm (1.73 in)
Width
440 mm (17 in)
Depth
325 mm (12.8 in)
Weight
4.1 kg (9 lb) max.
Environment
Designed for future IEEE-1613 compliance
Storage
Temperature
-20°C to +70°C (-4°F to +160°F)
Operating
Temperature
-10°C to 65°C (14°F to 149°F)
Notes:
- For extended operating temperature ranges, contact
your local RAD Business Partner.
- When working with other devices, operating
temperature depends on their temperature limits:
for example, with MiTOP-E3T3-GbE it is up to 55°C
(131°F).
Humidity
up to 95%, non-condensing

## Megaplex-1 Ordering  *(p.9)*

The information below represents examples of supported
configurations. For additional configuration options, please
contact your local RAD partner.
MP-1/PSR/2GEU/4FEU/6S/8E1T1
MP-1/PSR/2GEU/4FEU/6S/C37
MP-1/PSR/2GES/4FEU/6S/4E&M*
MP-1/PSR/2GEU/4FEU/8FXS/4E&M
MP-1/PSR/2GES/4FEU/8FXS/4E&M
MP-1/PS/2GES/2FEU/3S*
MP-1/PS/2GEU/2FEU/4E&M
MP-1/PSR/2GES/4FEU/8FXS/4E&M/RG
MP-1/PSR/2GEU/4FEU/8FXS/4E&M/RG
*certified for Railway applications with EN50121-4

## ORDERING OPTIONS  *(p.9)*

Some options are not supported by all models. Some option
combinations are invalid or may require a minimum order. To
determine the BOM for your application, please contact your
local RAD partner.
Note: With non-RG options, the FXS ringer is built in the product
and powered via the main power supply inlet (PS-A).
External
Ringer
RG
External ringer
Power
Supply
PS
Single power supply
PSR
Redundant power supplies
Uplink
Ports
2GEU
2 GbE ports with 10/100/1000BASE-T copper
interfaces
2GES
2 GbE ports with empty SFP receptacles
User
Ports
3S*
3 serial ports
6S
6 serial ports
2FEU
2 Fast Ethernet copper ports
4FEU
4 Fast Ethernet copper ports
C37
2 C37.94 ports
4E&M*
4 E&M voice ports
8FXS
8 FXS voice ports
8E1T1
8 E1/T1 ports

## SUPPLIED ACCESSORIES  *(p.9)*

Alarm connector
2 DC power inlet adapters
2 AC power cables
CBL-RJ45/D9/F/6FT
Control cable
RM-50
Hardware kit for mounting one Megaplex-1 unit in a 19-inch rack

## OPTIONAL ACCESSORIES  *(p.9)*

CBL-SCS68/3/*/#/&
Cable for converting each of the VS 68-pin SCSI connectors into
3 separate channel connectors with the physical interface
specified.
Note: A separate cable is required for each of the 2 channel connectors.
Legend
*
Interface:
V.24/RS-232, 25-pin
V35
V.35 interface, 34-pin
V36
V.36/RS-449, 37-pin
RS-530, 25-pin
X21
X.21, 15-pin
#
Length (Default=2m / 6.5 ft):
3M
for 3m (9.8 ft)
5M
for 5m (16.4 ft)
&
Connector:
F
female
M
male
CBL-G703-8/RJ45
Splitter cable for splitting 44-pin E1/T1 connector to 8 E1 or 8 T1
balanced RJ-45 connectors
CBL-G703-8/RJ45/X
Splitter cross-cable for splitting 44-pin E1/T1 connector to 8 E1
or 8 T1 balanced RJ-45 connectors
CBL-G703-8/COAX
Splitter cable for splitting 44-pin connector to 8 pairs of
unbalanced connectors for E1 applications

## Megaplex-1  *(p.10)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel/Fax 972-52-4748272 | Fax 972-3-6498250
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
694-100-04/26 (2.2) Specifications are subject to change without prior notice. © 2016–2026 RAD Data Communications Ltd. RAD products/technologies are protected by
registered patents. To review specifically which product is covered by which patent, please see ipr.rad.com. The RAD name, logo, logotype, and the product names MiNID,
Optimux, Airmux, IPmux, and MiCLK are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.
CBL-G703-8/OPEN
Open-ended cable with DB-44 connector on the Megaplex side
for balanced E1 or T1 applications
The cable is 2m (6.6 ft) long. For additional cable lengths
available, contact your local sales representative.
CBL-VS-VOICE
Cable for splitting each of the four RJ-12 connectors of FXS
interface into two RJ-12 connectors intended for end-user
equipment
The default cable length is 1m/3.3 ft. For additional cable lengths
available, contact your local sales representative