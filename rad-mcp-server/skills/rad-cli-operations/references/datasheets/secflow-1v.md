# SecFlow-1v Ruggedized Multiservice Gateway

<!-- datasheet product=secflow-1v family=secflow kind=system source=secflow-1v_ds_ver_2_3_mr_plc.pdf -->

*Datasheet `secflow-1v_ds_ver_2_3_mr_plc.pdf`, 8 pages. Product `secflow-1v`, family `secflow` (system).

## SecFlow-1v Ruggedized Multiservice Gateway  *(p.1)*

- Enhanced security capabilities: stateful firewall, VPNs,
automated PKI
- Resilient HSPA+/LTE cellular network uplink for
maximum service continuity and built-in GNSS for
location reporting
- Reduced OPEX with secure Zero Touch provisioning
- Hosting of third-party software for customized
applications (edge computing)
- SCADA protocol gateway for IEC-101, IEC-104, Modbus-
RTU/TCP, and DNP3 protocols
- Option for second cellular modem, WiFi, or LoRaWAN
- Embedded, isolated DC power supply
- Enhanced EMI and immunity according to IEC 61850-3,
IEEE 1613*, EN 50121-4
- Certified for use in AT&T, T-Mobile and Verizon wireless
networks
SecFlow®­1v is a multiservice gateway optimized for industrial IoT
and other mission-critical applications, a member of RAD’s
SecFlow suite of ruggedized Ethernet products.
In addition to its communication capabilities, SecFlow-1v is an
open platform suitable for quick introduction of new capabilities,
by hosting third-party software, using Linux containers.
SecFlow-1v features four GbE Copper ports with PoE options and
one GbE SFP port, two serial RS-232 ports or one RS-232 and one
RS-485/2W port, and a cellular modem with two SIM cards for
maximum link resiliency.
SecFlow-1v is equipped with serial interfaces for connectivity of
legacy RTUs with new IP-based IED systems. SecFlow-1v gateway
converts legacy IEC-101 protocol to IP-based IEC-104,
Modbus-RTU to Modbus/TCP and encapsulated DNP3 serial to
DNP over IP, enabling seamless communication from IP SCADA
to both old and new RTUs. This provides a single box solution for
multi-service applications and smooth migration to all-IP
networks.
In addition to its cellular uplink that provides wireless connection
towards the network, thanks to its modular architecture
SecFlow-1v can be equipped with additional wireless
technologies. When equipped with WiFi, SecFlow-1v acts as an
access point, aggregating several users, such as on-site
technicians or sensors, saving
the need for wired
connection or multiple costly
cellular connections from
each device.
When equipped with
LoRaWAN radio, SecFlow-1v
aggregates multiple low-power low-bandwidth sensors/meters
deployed over a wide area. This provides an ideal solution for
rural and other non-dense areas saving CAPEX and OPEX.
The gateway is designed for installation under harsh
environmental conditions. It features DIN-rail mount, IP30
protection level, wide operating temperature range (-40°C to
75°C) without fans, and EMI immunity (IEC 61850-3, IEEE 1613
and EN 50121-4).
SecFlow-1v supports several powering options that all use an
embedded isolated DC power supply, to meet the harsh
environmental requirements.

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

SecFlow-1v addresses Industrial IoT, for example:
- Distributed automation in secondary substations
- Smart meter and sensors concentration
- Water resources management
- Industry 4.0
- Smart and safe cities
- Out-of-band management using cellular uplink
- Smart retail

## INTEROPERABILITY  *(p.1)*

SecFlow-1v operates with RAD SecurityGateway, SecFlow-1,
SecFlow-2, and with third party VPN aggregators.
* This feature will be released in a future version.

## SecFlow-1v ROUTER AND VPN SERVICES  *(p.2)*

SecFlow-1v features static routing, RIPv2, OSPF, BGP, VRF and
NAT/NAT-Traversal.
The device features a VPN gateway with two operation modes:
- Inter-site connectivity using IPsec or Open VPN tunnels
- Remote user access, using SSH
Inter-site VPN-based encrypted link ensures L3 transparent
connection of the Ethernet networks sites.
For remote access, the router uses an SSH-encrypted tunnel,
with user authentication and specific access authorization.

## LAYER-2 SWITCH  *(p.2)*

SecFlow-1v provides local switching capabilities with and without
VLAN support, maintaining 2K MAC addresses and 16 broadcast
domains (VLAN IDs).
QoS:
- Ingress policer, egress shaper
- Classification based on: Port, 802.1p, IPv4 DCSP
- Scheduling
- Four priority queues
- Strict and Weighted Round Robin (WRR)

## MANAGEMENT AND SECURITY  *(p.2)*

The device can be managed via the SecFlow web-based interface
(HTTP/HTTPS).
For easy and safe deployment, RAD offers Zero Touch
provisioning thus reducing OPEX and providing a simple way to
securely deploy thousands of elements in the network.
SecFlow-1v also supports a variety of access protocols, including
CLI and TFTP/SFTP.
Remote Terminal Unit/Programmable Logic Controller
Ordering options with Programmable Logic Controller (PLC)
present an all-in-one-box solution from a single source for
distribution automation, industrial automation, building
automation, etc., supporting Modbus, DNP3, IEC-104 and
BACnet SCADA masters. The devices can be programmed using:
- Ladder logic in accordance with EC 61131-3
- Instruction List (IL)
- Functional Block Diagram (FBD)
- Sequential Function Chart (SFC)
- Structured Text (ST)
SecFlow-1v devices with PLC module offer comprehensive cyber
security relying on stateful firewall or SCADA firewall (optional),
VPNs such as IPsec and OpenVPN, automated PKI, as well as
RADview management with SIEM. Zero Touch provisioning
allows secure service activation and maintenance, with low
OPEX.
SecFlow-1v
Remote Site
Public/Private Cloud
Microsoft
Amazon
Goggle
Cloud
Data Center
Mobile
PSN
Centralized Site Options
HQ
Remote
Access
Network/App
Server
Portal
RADview
FO
SecurityGateway/
3rd party secure Hub
RTU
Camera
RTU
Serial
ETH
PoE
Figure 1. Industrial IoT Backhaul
**SecFlow-1v Specifications CAPACITY**
Memory
1 GB RAM (unless otherwise specified)

## ETHERNET INTERFACES  *(p.3)*

Fiber
1 x 1000FX, SFP socket (see Ordering Options)
Copper
4 x 10/100/1000BASE-T
PoE (optional)
2 x 30W, 4 x 15W, 1 x 60W*
Max Frame Size 1.5 kB

## SERIAL INTERFACES  *(p.3)*

Isolation
Non-isolated/Isolated (for specific ordering options)
Serial
Interface
2 x RS-232 ports
1 x RS-232 + 1 x RS-485 ports

## BRIDGE  *(p.3)*

Compliance
IEEE 802.1Q
Max. Number of
Concurrent VLANs
(Broadcast domains)
MAC Address Table 2K
Operation Mode
VLAN-aware learning bridge

## MODEMS  *(p.3)*

Dual SIM Cellular
Modem
LTE bands
HSPA+/EVDO networks (technology backward
compatible)
UMTS/HSPA+ fallback
FOTA
Firmware upgrade Over the Air
Configurable
Cellular
Authentication
PAP, CHAP
Certification (L4) Verizon Wireless
AT&T
T-Mobile
PTCRB
SIM Card
Mini SIM, 25 mm x 15 mm (0.98 in x 0.59 in
Form factor: 2FF
LoRaWAN
Modem
433MHz/868MHz/915MHz/923MHz bands
SX1301 base band processor emulating 49 x LoRa
demodulators, 10 parallel demodulation paths
8 uplinks channel and 1 downlink channel
2 x SX125x Tx/Rx front-ends high/low
Tx power up to 25 dBm, Rx sensitivity down to -
139 dBm @ SF12, BW 125 kHz
UDP packet forwarder
LoRaWAN Server
(optional)
As per specification v1.0.4
WiFi Module
IEEE 802.11ac/a/b/g/n
Dual band 2.4GHz or 5GHz (software selectable)
Up to 8 users
Table 1. Modem Frequency Bands
LTE
Ordering
Code
Modem Category and Frequency Bands
L1
CAT 4 EMEA/Korea/Thailand
LTE FDD: B1/B3/B5/B7/B8/B20
LTE TDD: B38/B40/B41
WCDMA: B1/B5/B8
GSM: B3/B8
L3
CAT 4 Australia/New Zealand/Taiwan/Brazil
LTE FDD: B1/B2/B3/B4/B5/B7/B8/B28
LTE TDD: B40
WCDMA: B1/B2/B5/B8
GSM: B2/B3/B5/B8
L4
CAT 4 North America
LTE FDD: B2/B4/B5/B12/B13/B14/B66/B71
WCDMA: B2/B4/B5
L4A
CAT 6 North America, Anterix network 900MHz (B8)
LTE FDD: B1/B2/B3/B4/B5/B7/B8/B12/B13/B20/B25/
B26/B29/B30
TDD: B41
HSPA+: B1/B2/B3/B4/B5/B8
L4B
CAT 7 North America, CBRS 3500MHz (B48)
LTE FDD: B2/B4/B5/B7/B12/B13/B14/B25/B26/B41/
B42/B43/B48/B66/B71
HSPA+: B2/B4/B5
L4C
CAT 12 North America, CBRS 3500MHz (B48)
LTE FDD: B1/B2/B3/B4/B5/B7/B8/B9/B12/B13/B14/
B18/B19/B20/B26/B29/B30/B32/B41/B42/B43/B46/B4
8/B66
HSPA+: B1/B2/B4/B5/B6/B8/B9/B19
**NETWORKING**
VPN
L3 mGRE DMVPN
L3 IPsec VPN
OpenVPN client
Gateway
SCADA gateway for IEC101/104, Modbus RTU/TCP
and DNP3

## SecFlow-1v QUALITY OF SERVICE (QOS)  *(p.4)*

Policing
Per port ingress policer, L1 rate, CIR
Egress Queues
4 queues per port
Queue Mapping Per ingress port; P-bit mapping, DSCP mapping
Scheduling
Strict Priority / WRR
Shaping
Per port egress shaper, L1 rate, CIR
*This feature will be released in a future version.
**ROUTER**
Protocols
RIPv2, OSPFv2, BGP, VRF, IPv4, IPv6, NAT, NAT-T
VRRP based on RFC 2338
Static routing

## RTU/PLC  *(p.4)*

Inputs
6 x digital inputs, max DC input voltage 24 VDC
6 x analog inputs as ordering options:
-
0-5 VDC
-
0-12 VDC
-
0-24 VDC
Outputs
6 x digital outputs:
-
relay-based ordering option: 3 pins;
NO/COM/NC, 250 VAC/5A max, 400 VDC/5A
max
-
solid state relay-based ordering option for
Class I/DIV 2 certified (Hazloc) devices: 2 pins;
NO/COM, 100 VAC/100 mA max, 125 VDC/100
mA max
Web GUI
Northbound
to SCADA
Masters
Modbus, DNP3, IEC-104, BACnet
Masters
Up to 5 concurrent masters
Modbus TCP
DNP3 TCP or BACnet TCP
IEC-104
Additional I/O
Points
Up to 400
Split between 2 Modbus-RTU
Slaves
Up to 10 Modbus-TCP slaves

## MANAGEMENT  *(p.4)*

Control Port
RS-232 interface, RJ45 connector
DHCP
DHCP client
DHCP server for WiFi clients
Protocols
TFTP/SFTP
Web-based interface using HTTPS or HTTP
Options
CLI with password-protected access
SMS commands
USB 2.0 host for software upload*
SD memory card*
*This feature will be released in a future version.
Central Site
Remote Site
Relay Output
Leased
FO
ETH
Sensor
RTU
SecFlow-1v
PLC
RTU
IP/TCP
Serial
ETH
Master
SCADA
Digital/Analog Inputs
Controlled
Device
ISP PSN
3G/LTE
BTS/eNB/
gNB
CAT-M1/
LTE
Figure 2. Automation Gateway with PLC/RTU
**SecFlow-1v TIMING**
Timing
Local time setting
SNTP

## SECURITY  *(p.5)*

Firewall
Stateful firewall
Login
Login lockout
ACL
ACL with MAC white list
TACACS+
Multiuser TACACS+
IPsec
AES128 and AES256 GCM encryption
PKI with X.509 certification
IKEv1, IKEv2, SHA2
Interoperability with SCEP server 2012 and higher
Port-Based
Network
Access
Control
(PNAC)
As per IEEE 802.1X-2100
Port-based authorization
PEAP-MSCHAPv2. PEAP
EAP-TLS authentication methods

## RESILIENCY  *(p.5)*

Routing
Dynamic routing, OSPFv2, BGP
Cellular ISP
Redundancy
SIM cards backup or dual modem support
IPsec VPN
Redundancy
Policy-based
Route-based
**MONITORING**
GNSS
GPS – American (default)
Galileo – European

## DIAGNOSTICS  *(p.5)*

Interface
Counters
Per port
Syslog
SNMPv3
GET and traps
LEDs
Including alarm indication
Dry Contacts
2-in and 2-out
SMS
Status indication

## GENERAL  *(p.5)*

Compliance
Enhanced EMI and immunity according to
EN 50121-4
IEC 61850-3
IEEE 1613*
Environment
Storage
Temperature
-40 to 85°C (-40 to 185°F)
Operating
Temperature
Enclosure 1:   -40 to 65°C (-40 to 149°F)
Enclosure 2:   -40 to 75°C (-40 to 167°F) w/o PoE
-40 to 65°C (-40 to 149°F) with PoE
Enclosure 3: -40 to 60°C (-40 to 140°F)
Humidity
Up to 90%
Note: The actual chassis and operating temperature depend on the
ordering options.
Physical
Table 2.Dimensions and Weight
Enclosure 1 (E1)
Enclosure 2 (E2)
Enclosure 3 (E3)
Height
mm (in)
138 (5.43)
157.2 (6.19)
146 (5.74)
Width
53.3 (2.1)
82.8 (3.25)
91.2 (3.59)
Depth
123.3 (4.85)
150 (5.9)
132.6 (5.22)
Weight
0.88 kg (1.94 lb)
1.4 kg (3.1 lb)
1.6 kg (3.5 lb)
Power
Power Supply Embedded isolated power supply
12V: 11–30 VDC
48V: 44–57 VDC (Dual power inlet)
WDC: 20–60 VDC (Dual power inlet)
Power
Consumption
Enclosure 1: < 10 W
Enclosure 2:
-
Without PoE: 17W
-
With PoE: 77W (17W regular + 60W PoE)
Enclosure 3:
-
Without PoE: 18W
-
With PoE: 78W (18W regular + 60W PoE)
*This feature will be released in a future version.

## SecFlow-1v Ordering  *(p.6)*

Legend
SF-1V/Ex/@/R/#/$/%/Lx/*/Lx/&/LRx/PLC/^/!/**/CN
Ex
Chassis
E1
E1 enclosure
E2
E2 enclosure
E3
E3 enclosure
@
Power Supply
12V
12 VDC (11–30 VDC)
48V
48 VDC (44–57 VDC)
WDC
Wide-range 20–60 VDC
R
Random-access memory (RAM)
2R
2GB
#
Ethernet Ports
4U1S
1 x 1000FX, 4 x 10/100/1000BASE-T ports
$
Power over Ethernet (PoE)
POE
POE on 4 x 10/100/1000BASE-T
2PA
PoE on 2 x 10/100/1000BASE-T for RAD’s
Airmux (except for Airmux-5000D) and
standard PoE for the remaining
2 x 10/100/1000BASE-T ports
%
Serial Ports
2RS
2 x RS-232 ports
2RSM
1 x RS-232 port, 1 x RS-485 port
Lx
Cellular Ports
HSP
HSPA+ (high-speed packet access)
modem, 3.5 Gb
L1
LTE CAT-4 modem for Europe
L3
LTE CAT-4 modem for Oceania and Latin
America
L4
LTE CAT-4 modem for North America
L4A
CAT 6 North America, certified for Anterix
network 900MHz (B8)
L4B
LTE-A CAT-7 modem for North America,
certified for CBRS private networks
L4C
LTE-A CAT-12 modem for North America,
certified for CBRS private networks
Notes:
-
L1(3,4,4A,4B,4C) means that any of L1/L3/L4/4A/
/4B/L4C options can be ordered.
-
In options with dual modems, both modems are of
the same type (HSP, L1, L3, L4, L4A, L4B or L4C).
-
The cellular modem is supplied with two matching
antennas (see Supplied Accessories).
*
GNSS
G
Integrated GPS
Note: The GPS modem is supplied with one antenna (see
Supplied Accessories).
&
WiFi Interface
WF
Wireless LAN
Note: The WiFi modem is supplied with two matching antennas
(see Supplied Accessories).
LRx
LoRaWAN Modem
LR1
LoRaWAN modem with 8 channels and
frequency scheme according to EU433
LR2
LoRaWAN modem with 8 channels and
frequency scheme according to EU868
LR3
LoRaWAN modem with 8 channels and
frequency scheme according to AU915
LR4
LoRaWAN modem with 8 channels and
frequency scheme according to US915
LR6
LoRaWAN modem with 8 channels and
frequency scheme according to AS923
Note: The LoRaWAN modem is supplied with one antenna
matching the frequency ordered.
PLC Programmable Logic Controller
PLC
6 digital inputs, 6 digital outputs, 6 analog
inputs, 5 VDC
PLC12
6 digital inputs, 6 digital outputs, 6 analog
inputs, 12 VDC
PLC24
6 digital inputs, 6 digital outputs, 6 analog
inputs, 24 VDC
PLCGO
Class I/DIV 2 certified (Hazloc) - 6 digital
inputs, 6 digital outputs, 6 analog inputs
5 VDC, solid-state relay-based
PLCGO12
Class I/DIV 2 certified (Hazloc) - 6 digital
inputs, 6 digital outputs, 6 analog inputs
12 VDC, solid-state relay-based
PLCGO24
Class I/DIV 2 certified (Hazloc) - 6 digital
inputs, 6 digital outputs, 6 analog inputs
24 VDC, solid-state relay-based
Note: PLC software is included upon ordering the /PLC ordering
option.
^
Ruggedized Options
RG
IEC 61850-3 compliant
RL
EN 50121-4 certified
GO
Class I/DIV 2 certified
!
uCESP Container
CSP
RS232 control signals (DTR and DCD) on S1
port managed by the uCESP container
**
Analog current loop ports with 4-20mA support
3CL
3 ports
6CL
6 ports
CN
LoRaWAN Container
AP
Actility LRR with enterprise TPE
OCP support (on premise Actility servers)
AS
Actility LRR with enterprise TPE SAAS support
(tenant on Actility cloud servers)
AW
Actility LRR with Service providers TPW
support (Actility server for service providers)
AE
Actility LRR for PoC with limited support of
gateways and sensors

## SecFlow-1v RECOMMENDED CONFIGURATIONS  *(p.7)*

SF-1V/E1/12V/4U1S/2RS/HSP
SF-1V/E1/12V/4U1S/2RS/HSP/G
SF-1V/E1/12V/4U1S/2RS/L1(3,4,4A,4B,4C)
SF-1V/E1/12V/4U1S/2RS/L1(3,4,4A,4B,4C)/G
SF-1V/E1/12V/4U1S/2RSM/HSP
SF-1V/E1/12V/4U1S/2RSM/L1(3,4,4A,4B,4C)
SF-1V/E1/WDC/4U1S
SF-1V/E1/WDC/4U1S/2RS/RL
SF-1V/E1/WDC/4U1S/2RS/HSP
SF-1V/E1/WDC/4U1S/2RS/L1(3,4,4A,4B,4C)
SF-1V/E2/12V/4U1S/2RS/HSP/G/WF
SF-1V/E2/12V/4U1S/2RS/HSP/G/HSP
SF-1V/E2/12V/4U1S/2RS/L1(3,4,4A,4B,4C)/L1(3,4,4A,4B,4C)
SF-1V/E2/12V/4U1S/2RS/L1(3,4,4A,4B,4C)/G/L1(3,4,4A,4B,4C)
SF-1V/E2/12V/4U1S/2RS/L1(3,4,4A,4B,4C)/G/WF
SF-1V/E2/12V/4U1S/2RS/L4/G/GO
SF-1V/E2/12V/4U1S/2RSM
SF-1V/E2/48V/4U1S/POE
SF-1V/E2/48V/4U1S/POE/2RS
SF-1V/E2/48V/4U1S/POE/2RS/HSP
SF-1V/E2/48V/4U1S/POE/2RS/HSP/G/WF
SF-1V/E2/48V/4U1S/POE/2RS/L1(3,4,4A,4B,4C)
SF-1V/E2/48V/4U1S/POE/2RS/L1(3,4,4A,4B,4C)/L1(3,4,4A,4B,4C)
SF-1V/E2/48V/4U1S/POE/2RS/L1(3,4,4A,4B,4C)/G/WF
SF-1V/E2/48V/4U1S/POE/2RS/L1(3,4,4A,4B,4C)/G/L1(3,4)
SF-1V/E2/48V/4U1S/POE/2RS/L1/G/LR1
SF-1V/E2/48V/4U1S/POE/2RS/L1/G/LR2
SF-1V/E2/48V/4U1S/POE/2RS/L3/G/LR3
SF-1V/E2/48V/4U1S/POE/2RS/L3/G/LR6
SF-1V/E2/48V/4U1S/POE/2RS/L4/G/LR4
SF-1V/E2/48V/4U1S/POE/2RSM/L1/G/LR2
SF-1V/E3/WDC/4U1S/2RSM/L4/G/PLCGO
SF-1V/E1/WDC/4U1S/2RSM/L4/G
SF-1V/E2/48V/4U1S/POE/2RSM/L4/G/LR4
SF-1V/E3/48V/4U1S/POE/2RSM/L4/PLC
SF-1V/E2/48V/4U1S/POE/2RS/L1(3,4,4A,4B,4C)/WF
SF-1V/E2/48V/4U1S/2PA/2RS
SF-1V/E2/WDC/4U1S
SF-1V/E2/WDC/4U1S/L1/WF
SF-1V/E2/WDC/4U1S/2PA/2RS/HSP
SF-1V/E2/WDC/4U1S/2PA/2RS/L1(3,4,4A,4B,4C)
SF-1V/E2/WDC/4U1S/2RS/L1(3,4,4A,4B,4C)/WF
SF-1V/E2/WDC/4U1S/2RS/HSP/WF
SF-1V/E2/WDC/4U1S/2RS/HSP/G/HSP
SF-1V/E2/WDC/4U1S/2RS/L1(3,4,4A,4B,4C)/G/L1(3,4,4A,4B,4C)
SF-1V/E2/WDC/4U1S/2RSM
SF-1V/E3/48V/4U1S/POE/2RS/L1(3,4,4A,4B,4C)/PLC
SF-1V/E3/48V/4U1S/POE/2RSM/L1(3,4,4A,4B,4C)/PLC12
SF-1V/E3/48V/4U1S/POE/2RSM/L1(3,4,4A,4B,4C)/PLC24
SF-1V/E3/WDC/2R/4U1S/2RS/L4/G/L4/PLC
SF-1V/E3/WDC/2R/4U1S/2RS/L4/G/PLC
SF-1V/E1/12V/4U1S/2RS/L1(4)/G/RG
SF-1V/E1/12V/4U1S/2RSM/L1(4)/G/RG
SF-1V/E1/WDC/4U1S/2RS/L1(L4)/G/RG
SF-1V/E1/WDC/4U1S/2RS/CSP*
SF-1V/E1/WDC/4U1S/2RS/L1/CSP*
SF-1V/E1/WDC/4U1S/2RSM/L1/G/RG
SF-1V/E2/WDC/4U1S/2RS/L1(3,4,4A,4B,4C)/RG
SF-1V/E3/48V/4U1S/POE/2RSM/L1/G/PLC/3CL
SF-1V/E3/48V/4U1S/POE/2RSM/L1/G/PLC/6CL
SF-1V/E2/48V/4U1S/POE/2RSM/L1(3,4,4A,4B,4C)/G/LR4/AP
SF-1V/E2/48V/4U1S/POE/2RSM/L1(3,4,4A,4B,4C)/G/LR4/AS
SF-1V/E2/48V/4U1S/POE/2RSM/L1(3,4,4A,4B,4C)/G/LR4/AW
SF-1V/E2/48V/4U1S/POE/2RSM/L1(3,4,4A,4B,4C)/G/LR4/AE
SF-1V/E2/48V/4U1S/POE/2RS/L4B/G
SF-1V/E2/48V/4U1S/POE/2RS/L4C/G
Please contact RAD Sales for more details on future products.

## SPECIAL CONFIGURATIONS  *(p.7)*

Zero Touch Provisioning
PS-ZT-PRE_CONFIGURATION
One Zero Touch pre-configuration service package per each
SecFlow-1v unit
and either of the following:
PS-ZT-STAGING
Local Zero Touch staging service package (one per project)
PS-ZT-ONSITE-STAGING
Onsite Zero Touch staging service package (one per project)
Please contact your local RAD partner for additional
configuration options.
* This ordering option is part of RAD’s roadmap. Regarding
availability, follow updates of official rollout and release
announcements.

## SecFlow-1v  *(p.8)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel 972-3-6458181 | Fax 972-3-7604732
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
715-100-10/22 (2.3) Specifications are subject to change without prior notice. © 2018–2022 RAD Data Communications Ltd. The RAD name, logo, logotype, and the product
names Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their
respective holders.

## SUPPLIED ACCESSORIES  *(p.8)*

SF-ANT-GPS-PAS-3DBI-MAG/3M
GPS passive antenna, 3m, for options with integrated GPS
SF-ANT-HSP-2DBI-SMA
HSP antenna, 2 dBi, for options with HSPA+ (high-speed packet
access) modem
SF-ANT-LTE699-4DBI-SMA
LTE antenna, 4dBi, for options with LTEx modems
SF-ANT-WIFI-DUALBAND-3DBI-SMA
WiFi dual band antenna, 3 dBi, for options with WiFi modem
SF-ANT-LoRA-3DBI-SMA
LoRaWAN antenna, 3 dBi, for options with LoRaWAN modem
Note: The LoRaWAN modem is supplied with one antenna
matching the frequency ordered: EU433, EU868, AU915, US915,
AS923.

## OPTIONAL ACCESSORIES  *(p.8)*

CBL-RJ45/D9/F/6FT
Serial console and RS-232 data ports cable
CBL-RJ45/D9/F/DM
RJ45 to DB9 female shielded cable for /CSP option, 2m
CBL-SF-RJ45-RS485
RS485 open-ended shielded cable
CBL-SERIAL-RJ45C-RJ45R
RAD to CISCO adapter cable
RM-DIN-SINGLE
Rack Mount adaptor for single DIN RAIL device
RM-DIN-19
19” Rack Mount adaptor for DIN RAIL device
USB holder kit
For SF-1V/E2/12V/4U1S/2RS/L4/G/GO ordering option
Power Supplies
SF-AC-48VDC-40W (to be used with non-POE options)
External DIN rail AC to 48 VDC power supply, 40 W, -20 to 60°C
(-4 to 140°F); 20 W at 60°C (140°F) and above
SF-AC-48VDC-120W
External DIN rail AC to 48 VDC power supply, 120 W, -20 to 60°C
(-4 to 140°F); 60 W at 65°C (149°F) and above
SF-24VDC-48VDC-240W
24 VDC to 48 VDC power supply, 240 W, -40 to 50°C (-40 to
122°F); 120 W at 65°C (149°F) and above
SF-AC-12VDC-40W
AC to 12 VDC power supply, 40 W, -20 to 60°C (-4 to 140°F);
20 W at 65°C (149°F) and above
Antennas
SF-ANT3G-2M
Outdoor antenna for SecFlow 3G cellular modem, 2m connecting
cable, 2.2 dBi, 824-894 MHz/900 MHz/1800 MHz/1900 MHz
SF-ANT3G-5M
Outdoor antenna for SecFlow 3G cellular modem, 5m connecting
cable, 2.2 dBi, 824-894 MHz/900 MHz/1800 MHz / 1900 MHz
SF-ANT4G-2M
Outdoor antenna for SecFlow 4G cellular modem, 2m connecting
cable, 3 dBi, 699-960 MHz/1710-2170 MHz/2500-2690 MHz
SF-ANT4G-5M
Outdoor antenna for SecFlow 4G cellular modem, 5m connecting
cable, 3 dBi, 699-960 MHz/1710-2170 MHz/2500-2690 MHz
SF-ANT-LTE700-7DBI-MGNT
Outdoor magnetic base antenna for SecFlow-1v LTE options and
for LoRaWAN 868 and 915 MHz, 7 dBi
Transceivers
For the list of available transceivers, see the Pluggable
Transceivers data sheet at www.rad.com
Note: It is strongly recommended to order this device with original RAD
SFPs installed. This will ensure that prior to shipping, RAD has performed
comprehensive functional quality tests on the entire assembled unit,
including the SFP devices. RAD cannot guarantee full compliance to
product specifications for units using non-RAD SFPs.