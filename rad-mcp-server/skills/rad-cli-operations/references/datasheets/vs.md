# VS Multiservice Module

<!-- datasheet product=vs family=mp4100 kind=card source=vs_ds.pdf -->

*Datasheet `vs_ds.pdf`, 11 pages. Product `vs`, family `mp4100` (card).

## Megaplex-4  *(p.1)*

VS

## Multiservice Module  *(p.1)*

- Broad variety of services
- E1/T1, FXS, FXO or E&M toll-quality analog voice
channels, input/output binary command ports, OCU-DP
– DDS, IEEE C37.94 dual optical link
- 6/12 serial sync/async data interfaces, configurable (per
port) serial interface types and data rates of 2.4 kbps to
1984 kbps
- Bidirectional broadcast for easy interconnection of
multiple control centers to remote RTUs/IEDs
- Pseudowire or Ethernet over PDH support
VS multiservice modules provide a variety of interfaces, including
serial, binary command, OCU-DP – DDS, C37.94, voice, and
E1/T1. The modules employ an embedded pseudowire engine
used for low-latency transmission of TDM services over
packet-switched networks.

## 2BARCHITECTURE  *(p.1)*

VS-12 modules consist of two identical submodules each
featuring a serial interface with 6 sync/async channels.
VS-6/BIN consists of the following submodules:
- Upper: serial interface submodule with 6 sync/async
channels
- Lower: binary command submodule with 8 inbound (cmd-in)
and 8 outbound (cmd-out) ports.
VS-6/703 consists of the following submodules:
- Upper: serial interface submodule with 6 sync/async
channels
- Lower: G.703 submodule with 8 G.703 codirectional 64-kbps
ports.
VS-6/C37 consists of the following submodules:
- Upper: serial interface submodule with 6 sync/async
channels
- Lower: C37.94 submodule with 2 IEEE C37.94 fiber optic
ports.
VS-6/FXS, VS-6/FXO, VS-6/E&M modules consist of the following
submodules:
- Upper: serial interface submodule with 6 sync/async
channels
- Lower: voice submodule with 8 FXS, 8 FXO or 4 E&M ports.
FXS/E&M module consists of the following submodules:
- Upper: voice submodule with 8 FXS ports.
- Lower: voice submodule with 4 E&M ports.
VS-OCU-DP/E&M module consists of the following submodules:
- Upper: OCU-DP – DDS submodule with 2 OCU-DP – DDS ports
- Lower: voice submodule with 4 E&M ports.
VS-6/E1T1 consists of the following submodules:
- Upper: serial interface submodule with 6 sync/async
channels and 8 E1 or T1 ports
- Lower: E1/T1 submodule with 8 soft-selectable E1/T1 ports.
VS-16E1T1 consists of two identical E1/T1 submodules each
featuring 8 soft-selectable E1/T1 ports.

## 3BSERIAL INTERFACE  *(p.1)*

The serial data rates in the VS modules are independently
selectable for each channel and depend on the selected
encapsulation mode.
The interface terminates in 68-pin SCSI-4 female connectors.
Each submodule contains 2 connectors; each connector includes
3 channels. The module provides a simple and easy SW-
configurable selection of serial interface (V.35, RS-422 or RS-232)
according to the deployment needs.
Adapter cables, available upon order, are offered by RAD to split
each module connector into three separate channel interfaces
with standard connectors: V.35, RS-530, RS-232, X.21 or V.36/RS-
449.
VS
Encapsulation Modes
VS modules behave like different types of modules on selection
of the specific encapsulation mode:
- None: each channel operates at high-speed rates of n×56 or
n×64 kbps, where n = 1 to 31 (that is, maximum 1984 kbps).
- V110: each channel operates at low-speed rates of 2.4, 4.8,
9.6, 19.2 or 38.4 kbps, performing rate adaptation in
accordance with ITU-T Rec. V.110.
- 3-bit transitional: the module provides transitional encoding
to transmit asynchronous data at rates up to 19.2/38.4 kbps.
It operates by encoding asynchronous data in a 3-bit
transitional code, which is then transmitted over the
Megaplex uplink at a rate of 64/128 kbps.
- R111: the module provides transitional encoding to transmit
asynchronous data at the rates of up to 19.2 kbps. It operates
by encoding data in a 3-bit transitional code, which is then
transmitted over the Megaplex uplink at a rate of 64 kbps.
- HCM (High-Capacity Multiplexing): the module transmits
synchronous/asynchronous data over 64 kbps based on
multiplexing with a DS0 timeslot. This Newbridge proprietary
rate-adaption and sub-rate multiplexing scheme provides a
bandwidth granularity of 800 bps throughout a network, by
formatting low speed data into 10 bytes frame.
Interface Control Signals
Each channel has local support for interface control signals (CTS,
RTS, DCD, DSR and DTR). Alternately, each channel can be
configured to transmit control signals end-to-end.
Sub-Stations
STM-1
GbE
FO
RTU
MSAP Node
9.6 kbps
FO
RS-232
V.35
FXS
X.21
PBX
V.35/RS-449
Low Speed
Data
RTU
RS-232
Megaplex-4
PSN
SDH Access
Network
ADM
Megaplex-4
Megaplex-4
E&M
FXO
PBX
RTU
C37.94
V.35
E&M
PBX
Figure 1.  Substation Data Services Connectivity
VS

## 4BE1/T1 INTERFACE  *(p.3)*

E1/T1 modules feature various combinations of E1/T1 and serial
ports per module with optional PW or Ethernet over PDH
support.
PW options can act as servers for other I/O modules, providing
up to 16 protected PW connections. E1/T1 traffic is transported
over CES/SAToP, including adapting timing support (ACR).
A special option provides ETHoPDH connectivity over E1/T1 links.
E1/T1 options are SW-selectable.

## 5B INARY COMMAND INTERFACE  *(p.3)*

The VS-6/BIN module provides the following functions:
- 8 binary input ports (cmd-in) – enable the management
system to read inbound indications from external sources.
- 8 binary output ports (cmd-out) – provide outbound
indications and control signals by means of dry relay
contacts.
- Two cmd-channels (1, 2) are used to transport binary
information over the telecommunications network via end-
to-end reporting: the input command is transferred to the
remote location via a selected timeslot and affects the
corresponding output.
The user can monitor the state of each inbound or outbound
port by means of indicators located on the VS-6/BIN front panel
or from the management system status display.
The binary commands can be locally output or be carried to a
peer card/Megaplex over a TDM network or over a packet
switched network. Up to 4 in/out commands can be carried over
a single DS0.
Backup
Power
Main Power
Loss Monitor
Control Fan
Alarm
External Equipment
Alarm Relay
Remote Site #1
CMD-Out
CMD-In
CMD Channel 2
VS-6/BIN
Warning
Buzzer
Cooling Fan
Activation
Backup
Power
Main Power
Loss Monitor
Control Fan
Alarm
External Equipment
Alarm Relay
Central Site
NMS
Megaplex-4
Megaplex-4
Remote Site #2
CMD-In
Megaplex-4
Warning
Buzzer
Cooling Fan
Activation
Backup
Power
Control Fan
Alarm
CMD Channel 1
CMD-Out
VS-6/BIN
VS-6/BIN
Figure 2.  Input/Output Binary Relay Commands in a Point-to-Multipoint Deployment of a VS-6/BIN Module
VS
Binary Inbound (CMD-IN) Ports
The VS-6/BIN module has 8 inbound ports, which enable it to
report alarms external to the Megaplex-4 unit, and report
physical conditions in remote locations to a central management
station.
The VS-6/BIN module can be configured by the user to interpret
the state of each input and report events to the CL module of the
local Megaplex-4. For each event, the CL module sends the
corresponding alarm message/SNMP trap to the supervision
terminal and network management stations. Each event can be
associated with a user-selected message that describes the
situation or prompts the remote user to take a prescribed action.
Binary Outbound (CMD-OUT) Ports
The VS-6/BIN module has 8 outbound ports equipped with
change-over dry relay contacts. The default state (the state of
the relay contacts when Megaplex-4 is operating) can be
selected by the user, individually for each outbound port.
The relay contacts report internal system alarms to outside
indicators and control external devices or applications. Each
relay can be controlled by a specific event in the network, in
accordance with configuration.

## 6BG.703 INTERFACE  *(p.4)*

The VS-6/703 module provides Megaplex-4 with 8 64-kbps G.703
codirectional data channels (ports). Each channel can be
independently enabled or disabled by software configuration.

## 7BC37.94 INTERFACE  *(p.4)*

The VS modules feature a dual-port fiber optic interface,
operating at a nominal wavelength of 830 nm and nominal line
rate of 2.048 Mbps. Each port is terminated in a pair of ST
connectors for connection to standard multimode fiber.
The interface complies with IEEE C37.94 standard for distances
of up to 2 km.
The interface can be used for both user and network ports –
either for inter-substation communication or for transmitting
distance Teleprotection information.

## 8BOCU-DP – DDS INTERFACE  *(p.4)*

The OCU-DP – DDS interface provides direct connection to
products with a built-in CSU/DSU. It is also used with standalone
CSU/DSU products for connection to DDS networks.
Each OCU-DP – DDS channel is compatible with AT&T PUB 62310
(Standard DDS) and BELLCORE TA-TSY-0000777, and operates at
data rates of 56 and 64 kbps.

## 9BVOICE INTERFACE  *(p.4)*

The VS voice submodules provide 8 FXS, 8 FXO or 4 E&M
toll-quality analog voice channels. Voice signals are digitized
using PCM, in compliance with ITU-T G.711 and AT&T Pub. 43801
standards.
Encoding and decoding are in full compliance with ITU-T
requirements G.711. Voice channel companding is selectable for
A-law or µ-law.
The modules are available with E&M, FXO and FXS interface
types.
VS-6/FXS, VS-6/FXO, VS-6/E&M and VS-8/E&M modules are
available in additional, advanced versions featuring enhanced
PW capabilities – in particular, adaptive clock recovery (ACR).
The E&M interface operates with different types of E&M
signaling: EIA RS-464 Types I, II, III and V (British Telecom SSDC5).
Both 2-wire and 4-wire lines are supported (user-selectable).
The E&M modules provide EIA RS-464 Type I signaling without
the need for an external DC power supply. For other signaling
types, the internal -12 VDC provided by the chassis is sufficient
for connection to most PBX systems.
However, for full support of EIA RS-464 Types II, III and
V (BT SSDC5) standards, a -48 VDC power source is required. This
voltage can be supplied via Megaplex PS AC or DC modules.
The FXS interface employs both loop-start and wink-start
signaling methods. FXS interfaces are typically used for direct
connection to 2-wire telephones.
When operating in PCM mode, battery polarity is reversed for
wink-start signaling, used in direct inward dialing (DID)
applications.
The FXO interface employs both loop-start and wink-start
signaling methods. It can be used for connection to PBX
extension lines in point-to-point, loop-start applications, with a
corresponding FXS VS or VC module at the remote Megaplex
connecting to the remote extension. The battery polarity is
reversed for wink-start signaling.
Gain control is user-selectable for both the receive and transmit
directions, enabling easy installation in all environments.

## 10BPSEUDOWIRE  *(p.4)*

A powerful pseudowire engine can act as a server card to other
I/O modules. Depending on the card type, the engine provides
up to 12 or 16 protected PWs per module with up to 32 timeslots
per each PW port.
The module features direct mapping of the local interfaces to
PW port with reduced latency and built-in jitter buffer with
configurable depth.
VS
A series of PW-enhanced VS modules have independent adaptive
clock recovery (ACR) mechanisms for each pseudowire, which
recover the original timing (clock rate) of the far-end source of
each pseudowire, according to ITU G.8261, G.823, G.824 and
MEF 22 recommendations. The clock recovery mechanisms can
provide recovered clock signals to serve as timing references for
Megaplex-4.
1BVS modules perform fault propagation.

## 12BETHERNET OVER PDH  *(p.5)*

VS modules transport Ethernet traffic over PDH infrastructure via
the following technologies:
- Generic Framing Procedure (GFP G.8040)
- Virtual Concatenation (VCAT G.7043)
- Link Capacity Adjustment Scheme (VCAT G.7042).

## 13BCROSS-CONNECT  *(p.5)*

The bidirectional broadcast mode enables a user at a central
location to communicate with several users connected to remote
Megaplex-4 units, using polled communications.
It is used mainly for SCADA applications in which a SCADA
controller is polling multiple RTUs/IEDs at a central site (see
Figure 3).
Each remote device is listening to the traffic sent by the central
controller and responds when it is being polled.
At the central site all the traffic from the remote site is
aggregated by the VS card.
**14BMANAGEMENT**
All module operating parameters are soft-selectable through the
Megaplex management.

## 0BSpecifications 15BSERIAL INTERFACE  *(p.5)*

Async
Character
Format
Length: 5,6,7,8
Parity bit: yes, no
Stop bits: 1,2
Clock Mode
DCE (VS channel provides both RX and TX clocks to
the user DTE)
Connectors
Four/two 68-pin SCSI, female (one per 3 data
channels)
Diagnostics
(per port)
Local digital loopback
Remote digital loopback
Data Channels
per Module
VS-12: 12
Other VS modules: 6
Encapsulation
Modes and
Data Rates
None: n×56 or n×64 kbps (n = 1 to 31)
V110: 2.4, 4.8, 9.6, 19.2, 38.4 kbps
R.111: 2.4, 4.8, 9.6, 19.2 kbps
3-bit-transitional: 64 kbps, 128 kbps
HCM: 2.4, 4.8, 9.6, 19.2, 38.4 kbps
Interface
(Electrical)
V.24/RS-232, V.35 or V.11/RS-422
RS-485 (4-wire only)
Interface
(Physical)
V.24/RS-232, V.35, V.36/RS-449, RS-530, X.21 (via
adaptor cables)
Interface
Control
Signals
Local support for all types of control signals
End-to-end transfer of local RTS and DTR lines
Signal Format Asynchronous or synchronous, full duplex

## 16B INARY INTERFACE  *(p.5)*

Compliance
IEEE 1613 (USA standard for equipment in electrical
switching stations)
Connector
DB-44
Inbound Ports Number: 8
Maximum Input Control voltage: ±60 VDC
Command trip point:
-
Above – 24 VDC ON
-
Below – 18 VDC OFF
Isolation
All input and outputs are galvanically isolated
LED Indicators Name: CMD IN/OUT
Number: 8
Color: Green/Yellow
Green blinking: cmd-in port is active
Red blinking: cmd-out port is active
Green/Red blinking: cmd-in and cmd-out ports are
both active
Off – port is not active or not connected
VS
Outbound
Ports
Number: 8
Relay type:
-
Electro-mechanical relay (EMR)
-
Solid-state relay (SSR)
Closed Contact Parameters:
-
Impedance: < 0.1 Ohm
-
Maximum current:
-
EMR:

AC: 8A, 250 VAC

DC: 8A, 30 VDC – 0.3A, 300 VDC
-
SSR: 0.12A
-
Minimum current (SSR only): 0.1 mA
Maximum DC voltage across open contacts: 60 VDC

## 17BG.703 INTERFACE  *(p.6)*

Compliance
ITU-T Rec. G.703, Section 1.1.4.1
Connectors
RJ-45 (one for each channel)
LED Indicators
ALM (red):
-
Lights steadily – the corresponding port
detects LOS
-
Flashes – the corresponding port detects
OOS pattern
Off – the corresponding port is not connected.
Nominal Data
Rate
64 kbps
Number of Ports

## 18BC37.94 INTERFACE  *(p.6)*

Compliance
IEEE C37.94, optical part
Connectors
Pair of ST connectors, female
Diagnostics (per
port)
Local digital loopback
Remote digital loopback
Fiber Type
62.5/125 µm multimode
9/125 µm single mode
50/125 µm multimode
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
Minimum
Receiver
Sensitivity
Multimode: -32 dBm
Single mode: -35 dBm
Maximum
Receiver Input
Power
Multimode: -11 dBm
Single mode: -5 dBm
Nominal Data
Rate
2.048 Mbps
Number of Ports
Power Coupled
into Fiber
62.5/125 µm: -11 to -19 dBm
9/125µm single mode: -5 to -10 dBm
50/125 µm: -11 to -23 dBm
Range (Typical)
Multimode: 2 km/1.25 miles
Single mode: 40 km/25 miles
Receiver Dynamic
Range
Multimode: 21 dB
Single mode: 30dB
Transmitter Type Multimode: LED
Single mode: Laser
Wavelength
Multimode: 850nm ± 40nm
Single mode: 1310nm ± 50nm

## 19BE1/T1 INTERFACE  *(p.6)*

Connectors (per
submodule)
DB-44, female for each 8 ports (see Ordering for
cables available from RAD)
Diagnostics (per
port and per
timeslot)
Local digital loopback
Remote digital loopback
BER Test on E1 ports of selected VS modules
Ports
8 E1/T1 ports per submodule
E1 or T1 option soft-selectable, same for all
module ports
VS

## 20BE1 INTERFACE  *(p.7)*

Compliance
ITU-T G.703, G.704, G.732 (Including CRC-4 and
E bit)
Framing
2 frames (G732N), or 16 frames (G732S) per
multiframe, with or without CRC-4
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

## 21BT1 INTERFACE  *(p.7)*

Compliance
ANSI T1.107 and T1.403
Data Rate (per
port)
1.544 Mbps
Framing
ESF
Impedance
Balanced 4-wire: 100Ω
Jitter
Performance
As per AT&T TR-62411
Line Code
Bipolar AMI
Zero Suppression Transparent, B7, B8ZS
Signal Level
Receive: 0 to -12 dBm
Transmit: 0.6, 1.2, 1.8, 2.4, 3.0 dBm
user-adjustable, measured at 0 to 655 ft

## 2BOCU-DP – DDS INTERFACE  *(p.7)*

Number of
Data Channels
Interface
Compatible with AT&T PUB 62310 (Standard DDS),
BELLCORE TA-TSY-000077
Connectors
RJ-45 per channel
Diagnostics
(per channel)
Local loopback
Remote loopback (OCU loopback)
Remote loopback on external unit (CSU loopback)
Alarms (per
channel)
Loss of signal
Out of service (OOS), 56 kbps only
Idle state (end-to-end support), 56 kbps only
Data Rates
56 or 64 kbps, full-duplex
Line Rates
56 kbps: 56 kbps
64 kbps: 72 kbps
Mapping to
Megaplex
Timeslots
56 kbps: single DS0
64 kbps: two DS0
Line Code
AMI
Timing
Locked to the Megaplex nodal timing
LED Indicators
(per channel)
LOS (red): Lights steadily when a loss of signal
condition is detected by the channel
TEST (yellow): Lights steadily when a local or
remote loopback is activated

## 23BVOICE INTERFACE – GENERAL  *(p.7)*

Bandwidth
Requirement
64 kbps (one timeslot) per enabled channel
Connectors
E&M interface: 4xRJ-45
FXS/FXO interface: 4xRJ-12 (one per two
channels)
Diagnostics
Local digital loopback for each channel, towards
the local user equipment
Remote digital loopback for each channel,
towards the remote user equipment
1 kHz, 0 dBm0 test tone injection for each
channel, towards the remote user equipment
1 kHz, 0 dBm0 backward test tone injection for
each channel, towards the local user equipment
Far-end Cross-talk
(2W&4W)
-65dBm0 max
Frequency
Response
(Ref:1020 Hz)
±0.5 dB at 300 to 3000 Hz
±1.1 dB at 250 to 3400 Hz
Go-to-return
Cross-talk (4W)
-60dBm0 max
Idle channel noise better than -65 dBm0 (+25 dBrnc)
Level Adjustment Soft-selectable, see Table 1
Line Type
E&M: 4-wire or 2-wire (soft-selectable)
FXS, FXO: 2-wire
ITU-T standard: G.712
Nominal Level
0 dBm
Nominal
Impedance
600Ω
Number of Voice
Channels
FXS/FXO: 8 ports per submodule
E&M: 4 ports per submodule
Return Loss (ERL) at 300 to 3400 Hz: better than 20 dB
Steps
0.5 dB (±0.5 dB), nominal
Signal to Total
Distortion (G.712)
-30 to 0 dBm0: better than 33 dB
-45 to +3 dBm0: better than 22 dB
Voice Encoding
Technique
Per ITU-T G.711 and AT&T Pub. 43801, µ-law or
A-law
VS

## 24BE&M INTERFACE  *(p.8)*

Indicators
M – On when the M line of the corresponding
channel is off-hook (channel in use)
E – On when the E line of the corresponding
channel is off-hook (channel in use)
Pulse Dial Distortion ±2 msec max
Signaling Method
(selectable)
EIA RS-464 Type I
EIA RS-464 Types II, III, and
V (British Telecom SSDC5) using -12 VDC in
place of -48 VDC
Note: For full support of Types II, III, and V
(SSDC5) signaling standards, -48 VDC power
supply is required.
Transformer
Isolation
1500 VRMS

## 25BFXS INTERFACE  *(p.8)*

Feed Current
20 mA (±10%) per active channel
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
Number of Channels Ringer-2100R: up to 40
Ringer-2000: up to 100
Ringer-2200N: up to 200
On-Hook/Off-Hook
Threshold
Off-Hook: Loop current >11 mA
On-Hook: Loop current <8 mA
Ringer
Overload protected, 1 sec ON, 3 sec OFF
54 VRMS with up to 1 REN load
45 VRMS with up to 5 REN load
Reverse Polarity
Pulse Distortion
6 msec max
-48 VDC (nominal)
Current
Consumption
30 mA (±10%) per active channel
Signaling Methods
EIA RS-464 loop-start or wink-start

## 26BFXO INTERFACE  *(p.8)*

DC Impedance
Off-Hook:
160Ω at 50 mA feed
270Ω at 25 mA feed
On-Hook: 20 MΩ
Indicators
Number: 8
Color: green/yellow
Name: RING/REM
Lights steadily in yellow – Remote “OFF-
HOOK”
Lights steadily in green – Ringing is received
on the corresponding channel
Off:  Port is not connected or Remote “ON-
HOOK” state with ringing not received on the
corresponding channel
Reverse Polarity
Pulse Distortion
6 msec max
Ring Detector
Ring Impedance: 20 MΩ
Detection: >16.5 VRMS, 13–68 Hz
No detection: <13.5 VRMS
Signaling Methods
EIA RS-464 loop-start or wink-start
VS

## 27BPSEUDOWIRE  *(p.9)*

Standard
Compliance
IETF: RFC 4553 (SAToP), RFC 5086 (CESoPSN)
MFA Forum: IA 8.0.0
MEF 8
Note. Non-E1/T1 VS modules do not support
SAToP.
Number of PW
Connections
32 per module (up to 640 per chassis)
Jitter Buffer Size
All /PW modules: 0.25–256 msec, in 1 µsec
steps with 125 µsec granularity (the value
entered by the user is rounded upward to the
closest n*125 µsec value)
Other VS modules: 0.25 –8 msec, in 1 µsec
steps with 125 µsec granularity (the value
entered by the user is rounded upward to the
closest n*125 µsec value)

## 28BDIAGNOSTICS  *(p.9)*

Local and remote
digital loopback per
DS1 port timeslot
all VS modules
Local and remote
digital loopback per
entire DS1 port
VS-6/E1T1, VS-16E1T1/PW, VS-6/703, VS-
6/FXS/PW, VS-6/FXO/PW, VS-6/E&M/PW

## 29BGENERAL  *(p.9)*

Power Consumption (max.)
VS-12
RS-422: 16.7W
RS-232: 13.5W
V.35: 15.9W
VS-6/BIN
RS-422: 14.7W
RS-232: 13.0W
V.35: 14.2W
VS-6/C37
RS-422: 12.9W
RS-232: 11.3W
V.35: 12.5W
VS-6/4E&M
RS-422: 17.0W
RS-232: 15.4W
V.35: 16.6W
VS-8/E&M
17.4W
VS-6/8FXO
RS-422: 13.9W
RS-232: 12.3W
V.35: 13.5W
VS-6/8FXS
RS-422: 14.7W
RS-232: 13.1W
V.35: 14.3W
VS-6/703
RS-422: 16.0W
RS-232: 14.4W
V.35: 15.6W
VS-8FXS/4E&M
15.1W
VS-OCU-DP/4E&M 11.5W
VS-16E1T1-EoP
14.5W
VS-16E1T1-PW
14.5W
VS/8E1T1/PW
RS-422: 16.1W
RS-232: 14.5W
V.35: 15.7W
Configuration
Programmable via the Megaplex management system
Environment
Operating
Temperature
-10°C to +55°C (14°F to 131°F)
Storage
temperature
-20°C to +70°C (-4°F to +160°F)
Humidity
up to 95%, non-condensing
VS

## 1BOrdering  *(p.10)*

MP-4100M-VS/16E1T1/EOP
MP-4100M-VS/6S/BIN/SSR
MP-4100M-VS/6S/BIN/EMR
MP-4100M-VS/6S/4E&M/PW
MP-4100M-VS/6S/C37
MP-4100M-VS/6S/C37/ST13L
MP-4100M-VS/6S/8FXO/PW
MP-4100M-VS/6S/8FXS/PW
MP-4100M-VS/12S
MP-4100M-VS/6S/8E1T1/PW
MP-4100M-VS/6S/703/PW
MP-4100M-VS/16E1T1/PW/M
MP-4100M-VS/8E&M/PW/M
MP-4100M-VS/8FXS/4E&M/M
MP-4100M-VS-OCU-DP/4E&M

## 30BORDERING OPTIONS  *(p.10)*

Some options are not supported by all models. Some option
combinations are invalid or may require a minimum order. To
determine the BOM for your application, please contact your
local RAD partner.
Serial Ports
Default
No serial ports
6S
6 serial ports
12S
12 serial ports
Other Ports
4E&M
4 E&M voice ports
8E&M
8 E&M voice ports
8FXS
8 FXS voice ports
8FX0
8 FX0 voice ports
OCU-DP
2 OCU-DP – DDS ports
8E1T1
8 E1/T1 links
16E1T1
16 E1/T1 links
8 G.703 64-kbps codirectional
ports
BIN/EMR
8 binary command ports with
electromechanical relay output
C37
2 C37.94 ports
EOP
Ethernet over PDH support
Pseudowire
Default
Regular PW support
PW
Enhanced PW with ACR support
Switching
M
Indicates Marvell-based switching
in some modules without serial
ports
VS
24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel/Fax 972-52-4748272 | Fax 972-3-6498250
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
464-121-06/25 Specifications are subject to change without prior notice. © 1988–2025 RAD Data Communications Ltd. The RAD name, logo, logotype, and the product names
Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective
holders.

## 31BOPTIONAL ACCESSORIES  *(p.11)*

CBL-SCS68/3/*/#/&
Cable for converting each of the VS 68-pin SCSI connectors into
3 separate channel connectors with the physical interface
specified.
Note: A separate cable is required for each of the 2/4 channel
connectors.
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
CBL-VS-VOICE
Cable for splitting each of the four RJ-12 connectors of FXS/FXO
interface into two RJ-12 connectors intended for end-user
equipment.
The default cable length is 1m/3.3 ft. For additional cable lengths
available, contact your local sales representative
CBL-G703-8/RJ45
Splitter cable for splitting each 44-pin VS E1/T1 module
connector to 8 E1 or 8 T1 balanced RJ-45 connectors
CBL-G703-8/RJ45/X
Splitter cross-cable for splitting each
44-pin VS E1/T1 module connector to 8 E1 or 8 T1 balanced RJ-
45 connectors
CBL-G703-8/COAX
Splitter cable for splitting each 44-pin VS E1 module connector to
8 pairs of unbalanced BNC connectors
CBL-G703-8/OPEN
Open-ended cable with DB-44 connector on the Megaplex side
for balanced E1 or T1 applications
CBL-VS-BIN
Open-ended cable with DB-44 connector on the Megaplex side
for binary (alarm control) applications
All VS cables listed in this section are 2m (6.6 ft) long. For
additional cable lengths available, see RAD catalog.
CBL-E1-SPLT
Cable for splitting each of the four RJ-45 connectors of the
VS-6/703 module interface into two RJ-45 connectors intended
for end-user equipment. The cable length is 1m/3.3 ft.