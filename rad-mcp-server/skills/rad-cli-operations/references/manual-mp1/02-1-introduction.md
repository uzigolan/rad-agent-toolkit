# 1 Introduction

*Manual `MP-1-mn_ver 2.2.pdf`, pages 47–67.*


## 1.1 Overview  *(p.47)*

Megaplex-1 
1. Introduction 
1 Introduction 
1.1 Overview  
Megaplex-1 is a compact multiservice pseudowire gateway that transports analog and TDM traffic 
(originating from legacy circuit-switched networks) over packet-switched networks (PSNs).  
Product Options   
The table below lists all the device options available for ordering and shows the number of ports of each 
type available in each option.  
Table 1-1.  Megaplex-1 Assembly Options  
 
E1/T1 
Serial 
E&M 
FXS 
C37 
FE 
(UTP) 
GbE 
(SFP) 
GbE 
(UTP) 
Power 
Supply 
MP-1/PSR/2GES/4FEU/6S/C37 
- 
6 
- 
- 
2 
4 
2 
- 
2 
MP-1/PSR/2GEU/4FEU/6S/C37 
- 
6 
- 
- 
2 
4 
- 
2 
2 
MP-1/PSR/2GES/4FEU/6S/4E&M 
- 
6 
4 
- 
- 
4 
2 
- 
2 
MP-1/PSR/2GEU/4FEU/6S/4E&M 
- 
6 
4 
- 
- 
4 
- 
2 
2 
MP-1/PSR/2GES/4FEU/8FXS/4E&M 
- 
- 
4 
8 
- 
4 
2 
- 
2 
MP-1/PSR/2GEU/4FEU/8FXS/4E&M 
- 
- 
4 
8 
- 
4 
- 
2 
2 
MP-1/PSR/2GES/4FEU/6S/8E1T1 
8 
6 
- 
- 
- 
4 
2 
- 
2 
MP-1/PSR/2GEU/4FEU/6S/8E1T1 
8 
6 
- 
- 
- 
4 
- 
2 
2 
MP-1/PS/2GEU/3S/2FEU 
- 
3 
- 
- 
- 
2 
2 
- 
1 
MP-1/PS/2GES/3S/2FEU 
- 
3 
- 
- 
- 
2 
- 
2 
1 
MP-1/PS/2GEU/4E&M/2FEU 
- 
- 
4 
- 
- 
2 
2 
- 
1 
MP-1/PS/2GES/4E&M/2FEU 
- 
- 
4 
- 
- 
2 
- 
2 
1 
Megaplex-1 
1. Introduction 
The GbE ports can be ordered with one of the following interfaces: 
• 
10/100/1000BASE-T (UTP) copper ports. This type of ports support auto-negotiation, with 
user-specified advertised data rate (10, 100 or 1000 Mbps) and operating mode (half- or 
full-duplex).  
• 
SFP sockets, for installing SFP plug-in modules.  
Applications  
Various users can benefit from the Megaplex-1 solution:  
• 
Users with mixed Ethernet and TDM services 
• 
Users looking for a future-proof migration path to IP connectivity 
• 
Owners of facilities sensitive to space or climate constraints. 
Its ability to handle a broad range of Ethernet, data and voice services in a single compact managed 
node, makes Megaplex-1 an ideal access solution for diverse network operators and service providers. It 
also provides a perfect fit for utilities and transportation companies that require an efficient way to 
transport and provision multiple legacy and next-generation services over their high capacity pipes. 
Megaplex-1 provides a variety of services, via its many user interfaces, such as:  
• 
IEEE C37.94 fiber optic teleprotection ports 
• 
Serial synchronous/asynchronous data ports 
• 
Voice ports (FXS, E&M) 
• 
Fast Ethernet (10/100BaseT). 
The following figures illustrates Megaplex-1 assuring substation connectivity over packet network.  
Error! Objects cannot be created from editing field codes. 
Substation Connectivity over Packet Network 
Megaplex-1 
1. Introduction 
GbE
Main Site
Video
Conferencing
4 x FXO
PSTN
Serial
V.35,V.24, X21
PBX
4 E&M 
Modems
Video
Conferencing
FE
4 E&M
Serial
V.35,V.24, X21
8 FXS
4 E&M
Hot Line
Modems
Remote Locations
GbE
GbE
Packet
Network
Megaplex-1
Megaplex-1
Megaplex-4
Modems
 
TDM to Packet Migration 
Features  
Ethernet Switch 
Megaplex-1 features a powerful internal Layer-2 Ethernet switch that provides Ethernet user ports with 
rate limiting and VLAN-based/port-based classification capabilities.  
Megaplex-1 includes the following Ethernet ports: 
• 
Two fiber optic or copper Gigabit Ethernet network (NNI) ports  
• 
Four or two copper Fast Ethernet user (UNI) ports  
• 
One copper FE port for out-of-band management.  
The GbE Network (NNI) ports provide the physical connection to the packet switched network. These 
ports provide Megaplex-1 with a multirate FE/GE interface, for optical or electrical media, and can be 
ordered with one of the following interfaces: 
• 
10/100/1000BASE-T copper ports. This type of ports support autonegotiation, with 
user-specified advertised data rate (10, 100 or 1000 Mbps) and operating mode (half- or 
full-duplex).  
The ports also support automatic polarity and crossover detection, and polarity correction, for 
connection through any type of cable to any type of Ethernet port (hub or station).  
Megaplex-1 
1. Introduction 
Alternatively, autonegotiation can be disabled and the rate and operating mode be directly 
specified. 
• 
SFP sockets, for installing 100/1000BASE-X SFP plug-in modules. Support for standard SFP 
optical transceivers for the GbE link interfaces enables selecting the optimal interface for each 
application. This type of ports does not support autonegotiation. RAD offers a wide variety of 
SFPs, for meeting a wide range of operational requirements.  
The UNI Ethernet port has 10/100BASE-TX interface terminated in 2 or 4 RJ-45 connectors, capable of 
autonegotiation. The user can configure the advertised data rate (10 or 100 Mbps) and operating mode 
(half-duplex or full-duplex). Alternatively, autonegotiation can be disabled, and the rate and operating 
mode be directly specified. In addition to autonegotiation, MDI/MDIX polarity and cross-over detection 
and automatic cross-over correction are also supported.  
Pseudowire   
The device uses its embedded pseudowire engine to encapsulate the user services for low-latency 
transmission over packet-switched networks.  
The powerful pseudowire engine in the devices with 8 E1/T1 ports provides up to 16 protected (or up to 
32 unprotected) PWs with up to 31 timeslots per each PW port. All other Megaplex-1 devices provide up 
to 6 protected (or up to 12 unprotected) PWs with up to 31 timeslots per each PW port. A remote 
pseudowire device converts the packets back to the original user traffic format.  
Packet formats can be selected on a per-pseudowire basis for optimal transmission over UDP/IP or 
Ethernet-based networks. Each pseudowire can be independently routed to any destination. 
The payload encapsulation method is CESoPSN (with or without CAS): 
• 
Structure locked encapsulation without CAS as defined in Y.1453 9.2.1 and RFC 5086 
• 
Structure locked encapsulation with CAS as defined in Y.1453 (structure locked encapsulation 
with CAS)  and RFC 5086 ( 5.4 : NxDS0 Services with CAS) 
Megaplex-1 also supports high performance adaptive recovery capabilities for end to end clock 
synchronization over the packet network. 
Resiliency 
Service reliability in Megaplex-1 is based on the following resiliency features: 
• 
Fanless operation 
• 
Dual power supply  
• 
Hitless PW protection.  
Megaplex-1 
1. Introduction 
Management and Security  
The device can be managed via RADview, RAD’s carrier-class NMS, or any SNMP-based management 
system. Megaplex-1 supports a variety of access protocols, including CLI over Telnet, SNMPv3, and TFTP. 
Security features include SNMPv3, RADIUS (client authentication), TACACS+ (client authentication, 
authorization, and accounting), SSH, and SFTP. Access Control Lists (ACL) can also be used to flexibly 
filter and mark management traffic, enabling service providers to maintain network security by dropping 
unwanted packets.  
Security  
User access to Megaplex-1 is restricted via user name and password. For more information, refer to 
Management Access Methods in Chapter 6. 
Telnet-like management can be secured using a Secure Shell (SSH) client/server program. Instead of 
sending plain-text ASCII-based commands and login requests over the network, SSH provides a secure 
communication channel. 
SFTP (Secure File Transfer Protocol, also known as SSH File Transfer Protocol) is supported, to provide 
secure (encrypted) file transfer using SSHv2. 
In addition, Megaplex-1 supports SNMP version 3, providing secure access to the device by 
authenticating and encrypting packets transmitted over the network.  
The RADIUS protocol allows centralized authentication and access control, avoiding the need of 
maintaining a local user database on each device on the network. For more information, refer to 
Authentication via RADIUS Server Mechanism  in Chapter 6. 
Diagnostics  
Comprehensive diagnostic capabilities include:  
• 
Local and remote loopbacks 
• 
Real-time alarms to alert the user on fault conditions.  
When a problem occurs, Megaplex-1 offers a set of diagnostic functions that efficiently locate the 
problem and rapidly restore full service. 
The diagnostic functions are based on the activation of loopbacks at various ports. These loopbacks 
enable identifying whether a malfunction is caused by Megaplex-1 or by an external system component 
(for example, equipment, cable, or transmission path connected to the Megaplex-1). A detailed 
description of the test and loopback functions is given in Chapter 5, under the corresponding section 
(for example, Serial Ports, Voice Ports etc). 
Megaplex-1 
1. Introduction 
Megaplex-1 maintains a cyclic event log file that stores up to 256 time-stamped events. In addition, an 
internal system log agent can send all reported events to a centralized repository or remote server. For 
additional information, refer to Handling Events in Chapter 11. 
Performance Monitoring  
Megaplex-1 collects statistics per physical port and per connection for 15-minute intervals, which 
enables the network operator to monitor the transmission performance and thus the quality of service 
provided to users, as well as identify transmission problems. Performance parameters for all the active 
entities are continuously collected during equipment operation.  
Statistics for the last 24 hours are stored in the device and can be retrieved by the network management 
station. For additional information, refer to the Statistics section for the relevant entity (for example 
Viewing Ethernet Port Statistics under Ethernet Ports in Chapter 5, Displaying PW Statistics in 
Chapter 8). 
PM Portal 
Megaplex-1 maintains performance management (PM) statistics for selected entities in the device (NNI 
and UNI Ethernet ports). The PM statistics are collected into a file periodically, for display in the 
RADview PM portal (refer to the RADview User’s Manual for further details on the PM portal). The PM 
collection process can be globally enabled or disabled for the entire device. In addition, the statistics 
collection can be enabled for all entities of a specific type, or for specific entities.  
Timing  
Flexible timing options enable reliable distribution of timing together with flexible selection of timing 
sources, including external station clock for daisy-chaining the clock signals to other equipment.  
The user can define the following clock sources: 
• 
ACR Adaptive clock recovered from a pseudowire circuit  
• 
External station clock. 
Multiple clock sources can be set and assigned corresponding priority. 
For detailed information about the different system timing modes, refer to Clock Selection in Chapter 9.  
Megaplex-1 
1. Introduction 
Simple Network Time Protocol  
The Simple Network Time Protocol (SNTP) provides the means of synchronizing all managed elements 
across the network to a clock source provided by NTP servers. Megaplex-1 supports the client side of a 
simple network time protocol (SNTP) v.3 (RFC 1769).  
Management 
Complete control over the Megaplex-1 functions can be attained via the following applications: 
• 
CLI-driven terminal utility for management via a local ASCII-based terminal connection (see 
Working with Terminal in Chapter 3 and Control Port in Chapter 6). Telnet access is supported 
via IP-based connection. 
• 
RADview – RAD’s SNMP-based element management system, providing a dedicated PC/Unix-
based GUI for controlling and monitoring the unit from a network management station. It also 
includes northbound CORBA interface for integration into any third-party NMS (network 
management system). For more information, refer to the RADview User's Manual. 
• 
Shelf View – RAD’s SNMP-based standalone application with fully FCAPS-compliant element 
management. It displays a dynamic graphic representation of the device panel(s), providing an 
intuitive, user-friendly GUI.  
For more information about configuration alternatives, refer to Configuration and Management in 
Chapter 3. 
The unit can be managed by and report to up to 10 different users simultaneously. Accounts of existing 
and new users can be defined/changed remotely, using a dedicated RADIUS server as explained under 
Authentication via RADIUS Server in Chapter 6. 
A wide range of inband and out-of-band management options provide organizations with the means 
needed to integrate the equipment within the organizational management network, as well as transfer 
their management traffic seamlessly through the Megaplex-1-based network.  
Databases and scripts of commonly used commands can be easily created and applied to multiple units 
using command line interface. 
Preset configuration files can be downloaded/uploaded to/from Megaplex-1 via TFTP or SFTP. For more 
information and instructions, refer to Chapter 12. 
Syslog  
The syslog protocol is a client/server-type protocol, featuring a standard for forwarding log messages in 
an IP network and supports up to four syslog servers at present. A syslog sender sends a small text 

## 1.2 New in this Version  *(p.54)*


## 1.3 Physical Description  *(p.54)*

Megaplex-1 
1. Introduction 
message of less than 1024 bytes to the syslog receiver. Syslog messages are sent via UDP in cleartext. 
The Syslog server acts as a centralized repository for all elements in the network, providing for a unified 
logging infrastructure, easier troubleshooting and forensics, lower operational risks and costs and higher 
availability and SLA through faster response time. 
Alarm Collection and Reporting  
Megaplex-1 continuously monitors critical signals and signal processing functions. If a problem is 
detected, the Megaplex-1 generates time-stamped alarm messages. The time stamp is provided by an 
internal real-time clock.  
For continuous system monitoring, the user can monitor alarm messages through the supervisory port. 
Alarm messages can also be automatically sent as traps to user-specified network management stations. 
The alarms can be read on-line by the network administrator using a Telnet host, an SNMP-based network 
management station, or a supervision terminal.  
Note 
Megaplex-1 can also monitor one external sense input, and will report its 
activation as any other internally-detected alarm.  
In addition to the alarm collection and reporting facility, the Megaplex-1 has two alarm relays with 
floating change-over contacts: one relay for indicating the presence of major alarms and the other for 
minor alarms. Each relay changes state whenever the first alarm is detected, and returns to its normal 
state when all the alarms of the corresponding severity disappear. The relay contacts can be used to 
report internal system alarms to outside indicators, e.g., lights, buzzers, bells, etc., located on an alarm 
bay or remote monitoring panel. 
1.2 New in this Version  
The following new functionalities have been added in version 2.2:  
• 
Three serial ports – New ordering option with 3 serial ports instead of 6  
• 
Two UNI ports – New ordering option as an alternative to four FE UNI ports   
1.3 Physical Description 
Below is a general view of the Megaplex-1 chassis. 

## 1.4 Functional Description  *(p.55)*

Megaplex-1 
1. Introduction 
Refer to the Installation and Setup chapter for a detailed description of the Megaplex-1 interface 
connections.  
1.4 Functional Description 
Megaplex-1 Architecture 
The device architecture and main building blocks is described in the below diagram: 
 
Megaplex-1 
1. Introduction 
 
Megaplex-1 Data path 
The Megaplex-1 data path is described in the below diagram: 
 
 
E1/T1
Voice
C.37
ETH
TDM Interfaces
PW Engine
Forwarding 
Engine
Timing Unit
Host
Serial 
Megaplex-1 
1. Introduction 
 
 
Traffic handling stages appearing in the above diagram are as follows: 
 
Processing Stage 
Description 
Cross-Connect 
Assigning TDM source traffic (serial, voice, c.37) to DS1 (internal) timeslots 
PW 
DS1 timeslots are mapped over Ethernet or UDP/IP using CESoPSN 
Router 
PW UDP/IP traffic is forwarded via the Router (according to PW 
Peer IP attribute). 
Note: Router access to the Network Ethernet ports is done via the Bridge 
Bridge 
MEF-8 PW is forwarded directly via the Bridge. 
Note: All Ethernet and PW traffic to and from Megaplex-1 is 
accessed via the Bridge. 
Classifier 
Ethernet traffic classification according to VLAN or port 
Policer 
Port level policing (supported at the Ethernet port ingress)  
VLAN Edit 
VLAN actions on Ethernet traffic (optionally include pushing)  
Queue mapping 
Mapping traffic to the different queues (up to 8) of the Egress port using a mapping 
profile (p-bit to queue).  
DS1-1
DS1-12
PW1
E1/T1
Voice
C.37
UDP/IP PW 
FRWRD via Router
Bridge
PW12
ETH
Classifier
Policer
ETH
Port level queues 
scheduler
Router
Cross 
Connect
(TDM to DS1 
map) 
MEF-8 PW 
FRWRD via Bridge
Queue
Map
Port level 
Shaper
VLAN Edit
VLAN 
Edit
Scheduling
(WFQ, SP)
Serial 
Megaplex-1 
1. Introduction 
Processing Stage 
Description 
Scheduler 
Port level scheduler. Schedules various queues to transmit according to the 
queue priority and weight. 
Shaper 
Port level shaper. Shapes the aggregate Egress traffic. 
E1/T1 Data Traffic 
Megaplex-1 has 8 independently configurable E1/T1 ports.  
The E1 interface is compatible with all carrier-provided E1 services, meeting the requirements of ITU-T 
Rec. G.703, G.704 and G.732.  
It operates in framed mode as per G.732, as well as in unframed mode. CRC-4 is also supported, 
complying with G.704 recommendations. Zero suppression over the line is HDB3.  
The T1 interface is compatible with ANSI requirements. Both SF and ESF framing formats are supported. 
Line code is selectable for AMI or B8ZS.  
Serial Data Traffic  
The serial data rates are independently selectable for each channel and depend on the selected 
encapsulation mode:  
• 
None: each channel operates at high speed rates of n×56 or n×64 kbps, where n = 1 to 31 (that 
is, maximum 1984 kbps). 
• 
V110: each channel operates at low speed sync rates of 2.4, 4.8, 9.6, 19.2 or 38.4 kbps, 
performing rate adaptation in accordance with ITU-T Rec. V.110. 
• 
3-bit transitional: the interface provides transitional encoding to transmit asynchronous data at 
rates up to 19.2/38.4 kbps. It operates by encoding asynchronous data in a 3-bit transitional 
code, which is then transmitted over the Megaplex uplink at a rate of 64/128 kbps. This mode 
covers all asynchronous character formats. 
The interface terminates in one or two 68-pin SCSI-4 female connectors. Each connector includes 3 
channels. This provides a simple and easy SW-configurable selection of serial interface (V.35, RS-422 or 
RS-232) according to the deployment needs. 
Adapter cables, available upon order, are offered by RAD to split each connector into three separate 
channel interfaces with standard connectors: V.35, RS-530, RS-232, X.21 or V.36/RS-449.  
Megaplex-1 
1. Introduction 
Each channel has local support of interface control signals (CTS, RTS, DCD, DSR and DTR). In addition, 
each channel can be configured to transmit control signals end-to-end.  
Optical Teleprotection 
The interface can be used for both user and network ports – either for inter-substation communication 
or for transmitting distance teleprotection information. 
The dual-port fiber optic interface operates at a nominal wavelength of 850 nm and nominal line rate of 
2.048 Mbps. Each port is terminated in a pair of ST connectors for connection to standard multimode 
fiber. 
The interface complies with IEEE C37.94 standard for distances of up to 2 km. 
Voice Traffic  
The voice interface provides 8 FXS or 4 E&M toll-quality analog voice channels. Voice signals are 
digitized using PCM, in compliance with ITU-T G.711 and AT&T Pub. 43801 standards.  
Encoding and decoding are in full compliance with ITU-T requirements G.711. Voice channel 
companding is selectable for A-law or µ-law. 
The E&M interface operates with different types of E&M signaling: EIA RS-464 Types I, II, III and 
V (British Telecom SSDC5).  
Both 2-wire and 4-wire lines are supported (user-selectable).  
The E&M interface provides EIA RS-464 Type I signaling without the need for an external DC power 
supply. For other signaling types, the internal -12 VDC provided by the chassis is sufficient for 
connection to most PBX systems. 
However, for full support of EIA RS-464 Types II, III and V (BT SSDC5) standards, a  
-48 VDC power source is required.  
The E&M interface provides signaling at +12V for applications that require positive signaling voltage (for 
example, radio transmitters) and perform fault propagation. In this mode, the voice port sends signaling 
to the radio transmitters by connecting GND to the E pin.  
The FXS interface employs both loop-start and wink-start signaling methods. FXS interfaces are typically 
used for direct connection to 2-wire telephones in the following loop-start applications: 
• 
Off-Premises Extension (OPX), where a local telephone on the PBX can be connected to an 
off-premises telephone, by dialing only the extension number; 

## 1.5 Technical Specifications  *(p.60)*

Megaplex-1 
1. Introduction 
• 
Private Line, Automatic Ringdown application (PLAR) (also referred to as Hot Line), where two 
telephones are connected directly via the E1/T1 link. When the telephone on one side goes off-
hook, the other telephone rings; 
• 
Direct connection to 2-wire telephones in PSTN applications. 
• 
Direct Inward Dialing (DID), where battery polarity is reversed for wink-start signaling.  
Gain control is user-selectable for both receive and transmit directions, enabling easy installation in all 
environments.  
1.5 Technical Specifications  
GbE Ports 
Number of Ports  
2  
 
Maximum Frame Size  
9600 bytes  
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
SFP-based  
 
 
Note: For detailed specifications of SFP transceivers, see the 
RAD SFP Transceivers data sheet. 
E1 Interface 
Compliance 
ITU-T G.703, G.704, G.732 
 
Framing 
• Framed per G.732: 
• with or without CAS 
• with or without CRC-4 
• Unframed 
 
Data Rate (per port) 
2.048 Mbps 
 
Line Code 
HDB3 
 
Jitter Performance 
As per ITU-T G.823 
 
Impedance 
 
Balanced 4-wire: 120Ω 
Unbalanced coax: 75Ω 
Megaplex-1 
1. Introduction 
 
Signal Level     
 
• Receive: 0 to -12 dBm 
• Transmit: 
• Balanced:  ±3V (±10%)  
• Unbalanced:  ±2.37V (±10%) 
 
Connectors 
• Dual DB-44, female  
T1 Interface 
Compliance 
• ANSI T1.107 and T1.403 
 
Framing 
• ESF, SF  
 
Data Rate (per port) 
• 1.544 Mbps 
 
Line Code 
• AMI, B8ZS 
 
Signal Level 
• Receive: 0 to -12 dBm   
• Transmit: 0.6, 1.2, 1.8, 2.4, 3.0 dBm user-adjustable, 
measured at 0 to 655 ft 
 
Jitter Performance 
• As per AT&T TR-62411 
 
Impedance  
• Balanced 4-wire: 100Ω 
 
Connectors 
• Dual DB-44, female  
Serial Interface 
Number of Channels and 
Transmission Format 
3 or 6 data channels per submodule, sync/async, 
user-selectable  
 
Connectors 
68-pin SCSI female connector per each 3 data channels 
(2 connectors per device) 
 
Electrical Interface  
 
• V.35 
• V.11/RS-422 
• V.24/RS-232 
 
Physical Interface (via 
adapter cables) 
• V.35  
• V.36/RS-449, RS-530, or X.21  
• RS-232  
 
Encapsulation Modes 
None 
V110 (sync only)  
3-bit-transitional 
 
Channel Data Rates 
 
 
 encapsulation-mode=none 
n×56 or n×64 kbps rates, independently selectable per 
channel: n = 1 to 31  
 
encapsulation-mode=v110 
2.4, 4.8, 9.6, 19.2, 38.4 kbps  
 
encapsulation-mode=3-bit-
transitional)  
64 kbps, 128 kbps 
Megaplex-1 
1. Introduction 
 
Timing Mode  
DCE (serial port provides both RX and TX clocks to the 
user DTE)  
 
Interface Control Signals 
• Local support 
• End-to-end transfer  
 
Local support 
• Local DCD is ON when the uplink is synchronized and 
there is no LOF alarm on the channel 
• Local CTS tracks local RTS state, or is constantly ON 
(user-selectable) 
• DSR (encapsulation-mode = v110) always ON when 
module is powered (unless end-to-end transmission 
is enabled) 
 
End-to-end transfer 
(user-selectable)  
 
 
encapsulation-mode = none  
• Local RTS line to remote DCD line (only for rates n x 
56 kbps)  
 
encapsulation-mode = v110, 
hcm 
• Local RTS line to remote DCD line 
• Local DTR line to remote DSR line 
 
encapsulation-mode = 3bit-
transitional 
• Local RTS line to remote DCD line  
 
Voice Interface 
Modulation Technique  
PCM, per ITU-T Rec. G.711 and AT&T Pub. 43801 
 
Companding 
µ-law or A-law (user-selectable)  
Note: PW multiframe needed for signaling transport in 
both companding modes is always according to ITU-T 
G.703 standard.  
 
Nominal Level 
0 dBm  
 
Nominal Impedance 
600Ω 
 
Return Loss (ERL)  
Better than 20 dB 
 
Frequency Response (Ref: 1020 
Hz) 
0 dB ±0.5 dB, at 300 to 3000 Hz 
0 dB ±1.1 dB, at 250 to 3400 Hz 
 
Transmit and Receive Levels 
User-selectable in 0.5 dB ±0.15 dB steps, see Voice 
Ports in Chapter 5.  
 
Signal to Total Distortion Using 
ITU-T Rec. G.712 (8-bit PCM 
encoding) 
-30 to 0 dBm0:  better than 33 dB 
-45 to +3 dBm0:  better than 22 dB 
 
Idle Channel Noise 
Better than -65 dBm0 (+20 dBrnc) 
Megaplex-1 
1. Introduction 
 
Diagnostics 
Local digital loopback  
Remote digital loopback  
Forward tone injection (1 kHz, 0 dBm0) 
Backward tone injection (1 kHz, 0 dBm0) 
E&M Interface  
Number of Ports 
4 
 
Interface Type 
4-wire or 2-wire (user-selectable) 
 
Connectors 
RJ-45 per channel 
 
Signaling Method 
(User-Selectable) 
• EIA RS-464 Type I 
• EIA RS-464 Type II, III and V (British Telecom SSDC5) 
using internal -12 VDC in place of -48 VDC 
Note: For full support of Types II, III, and V (SSDC5) signaling 
standards, a -48 VDC supply is required.  
 
Dial Pulse Distortion 
±2 ms max 
 
Indicators 
M: On when the M line of the corresponding channel is 
off-hook (channel in use). 
 
 
E: On when the E line of the corresponding channel is 
off-hook (channel in use). 
 
Transformer Isolation 
1500 VRMS  
FXS Interface  
Number of Ports 
8 
 
Interface Type 
2-wire 
 
Connectors 
RJ-12 per two channels 
 
Signaling Modes  
EIA RS-464 loop-start and wink-start, user-selectable 
 
On-Hook/Off-Hook Threshold  
• Off-hook Threshold: Loop current >11mA 
• On-hook Threshold: Loop current <8mA  
 
Feed Current 
20 mA (±10%) 
 
-48 VDC (Nominal) Current 
Consumption 
35 mA (±10%) per active channel 
 
Ringer Characteristics  
• 54 VRMS with up to 1 REN load 
• Protected against overload  
 
Ring Frequency  
• 22 Hz (±10%) 
 
Ring Cadence 
• 1 second ON, 3 seconds OFF 
 
Reversal Polarity Pulse 
Distortion  
6 ms max 
Megaplex-1 
1. Introduction 
 
Indicators 
LOC/REM (Green/Yellow): 
Lights steadily in green – Local “OFF-HOOK” 
Lights steadily in yellow – Remote “OFF-HOOK” 
Flashes in green/yellow – Local and Remote “OFF-HOOK” 
(conversation state) 
Off: port is not connected or both directions of signaling 
is “ON-HOOK” 
C37.94 Interface 
Compliance  
IEEE C37.94, optical part  
 
Number of Ports 
2 
 
Connectors   
Pair of ST connectors, female 
 
Nominal Data Rate 
2.048 Mbps 
 
Wavelength 
850nm ± 40nm 
 
Fiber Type 
62.5/125 µm multimode 
 
Transmitter Type 
LED  
 
Power Coupled into Fiber 
62.5/125 µm: -11 to -19 dBm (15 dBm typical) 
 
Mininum Receiver Sensitivity 
-32 dBm 
 
Maximum Receiver Input 
Power 
-11 dBm 
 
Optical Budget  
13 dB 
 
Receiver Dynamic Range 
21 dB 
 
Range (Typical) 
2 km/1.25 miles (with 6.8 dB margin) 
 
Indicators 
 
SYNC (Green/Red): 
Lights steadily in green – the corresponding port is 
operating properly 
Flashes in green – the corresponding port serves as the 
standby port and is operating properly 
Lights in red – the corresponding port detects loss of 
synchronization or loss of signal 
Flashes in red – the corresponding port serves as the 
standby port, and detects loss of synchronization 
 
 
REM SYNC (Yellow): 
On – the corresponding port detects loss of remote 
synchronization 
Off – the corresponding port is not connected. 
Megaplex-1 
1. Introduction 
Fast Ethernet 
Interface (UNI) 
Number of Ports 
2 or 4  
 
Data Rate 
10/100 Mbps, with autonegotiation  
 
Maximum Frame Size 
9140 bytes  
 
Connector 
Shielded RJ-45 (per port) 
Ethernet 
Management Port 
(CONTROL)  
Interface 
10/100/1000BaseT, with autonegotiation 
Connector 
RJ-45 
Timing 
Clock Sources 
 
• Internal crystal free-running oscillator-based clock 
• Derived from the receive clock of a specified user 
port 
• Adaptive clock recovered (ACR) from a pseudowire 
circuit 
• External station clock 
 
Internal Clock Quality 
Quality level is Stratum-4 with quality precision of 
±32ppm. 
 
ACR (Adaptive Clock Recovery) 
Supports jitter and wander requirements according to 
G.8261, G.823 and G.824 traffic interface 
recommendations with quality precision of ±16 ppb 
 
Station Clock Interface 
Rate: 
• 2.048 Mbps  
• 1.544 Mbps 
 
Line Code  
AMI/HDB3 
 
Mode 
Input and output 
 
Impedance 
120Ω, balanced 
75Ω, unbalanced (via adapter cable)  
 
 
Interface (software-selectable): 
• ITU-T Rec. G.703, HDB3 coding for 2.048 Mbps 
• ITU-T Rec. G.703, B8ZS coding for 1.544 Mbps 
 
Connector 
RJ-45, shielded 
Diagnostics 
Tests 
Local and remote loopbacks per link and per timeslot  
 
 
Alarms 
Time and date stamped 
 
Performance Statistics 
Ethernet and PW ports  
Megaplex-1 
1. Introduction 
Indicators 
POWER SUPPLY PS1,  
PS2
 
(green) 
• On: the corresponding PS is on  
• Off: the corresponding PS is off  
 
ON LINE 
 
• Lights in yellow: Diagnostic loopback is active 
• Lights in green: the device is online 
• Off: the device is off 
 
ALM (red)  
 
• On: There is at least one active alarm in the device. 
• Off: No active alarms are present in the device. 
• Blinking: there is at least one critical or major alarm 
in the device. 
 
Ethernet Ports (User/Network/ 
Management) 
 
 
 
LINK (green) 
On: Ethernet interface is synchronized. 
Off: Ethernet link is not detected 
 
 
ACT (yellow) 
ON: Data is being transmitted/received at the Ethernet 
link. 
Off: ETH frames are not received and transmitted  
 
Station CLOCK Port 
 
 
 
ON (green) 
On: the station clock port is configured as no shutdown 
Off: the station clock port is configured as shutdown 
 
 
LOS (red) 
On: loss-of-signal (when station clock port configured as 
connected)  
Off: no loss-of-signal 
 
Note: For C37.94 and voice interface indicators, see the corresponding table section. 
Alarm Relay Port  
Port Functions 
• 1 inbound RS-232 alarm input, +/- 12V threshold 
• 2 outbound (dry contact) relays triggered by 
major/minor alarms, with floating change-over 
contacts  
 
Connector 
• 9-pin Molex flat, female  
 
 
Maximum allowed current  
• 1 ADC through closed contacts  
• 0.5 AAC through closed contacts  
 
Maximum voltage across open 
contacts  
• 30 VDC 
• 125 VAC  
•  
 
Auxiliary voltage output 
• 
+12V (through a 1600 Ohm series resistor) 
Megaplex-1 
1. Introduction 
 
Operation 
Normally open, normally closed, using different pins 
FD (Factory Default) 
External push button  
 
Performs ‘set to default’ in the following scenario: 
• In normal operation (device up and running): when 
push button pressed for 5 seconds, the unit is 
restored to its factory default. 
• If the user default has been configured, the unit 
boots up with the user-default-config file. 
Power  
 
Autodetection 
 
AC 
100–240 VAC nominal (±10%) 50/60 Hz  
 
DC 
VDC (40-300 VDC) 
 
Power Consumption 
Maximum: 35W 
Typical : 28W 
Minimum :22W 
Physical  
Height 
43.7 mm (1.7 in)  
 
Width 
440 mm (17.4 in) 
 
Depth 
325 mm (12.8 in)  
 
Weight  
Weight: 4.1 kg (9 lb) max.  
RM Kit 
RM-50: rack-mount kit for mounting Megaplex-1 unit in a 19" rack  
Environment 
Operating Temperature 
-10°C to 65°C (14°F to 149°F) 
Note:  For extended operating temperature ranges, contact your 
local RAD Business Partner. 
 
Note: When working with other devices, operating temperature 
depends on their temperature limits. 
Storage Temperature 
-20°C to +70°C (-4°F to +160°F) 
Humidity 
Up to 95%, non-condensing 
 
 
 
 