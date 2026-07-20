# SecFlow-1p Industrial IoT Gateway

<!-- datasheet product=secflow-1p family=secflow kind=system source=secflow-1p_ds.pdf -->

*Datasheet `secflow-1p_ds.pdf`, 8 pages. Product `secflow-1p`, family `secflow` (system).

## SecFlow-1p Industrial IoT Gateway  *(p.1)*

- Ruggedized IOT gateway, SCADA protocol gateway for
**IEC-101, IEC-104, Modbus-RTU/TCP***
- Edge computing by hosting 3rd party container software
**for customized applications**
- Zero Touch provisioning
- Terminal server
- One or two embedded cellular modems (optional

## second cellular modem, Wi-Fi access point and client, or LoRaWAN)  *(p.1)*

- Two SIM cards for maximum link resiliency
- Serial tunneling to TCP/IP, including DNP3
- Dry contacts
- GPS for location reporting
- Zone-based stateful firewall
SecFlow®­1p, a member of RAD’s SecFlow suite of ruggedized
Ethernet products, is an industrial IoT gateway. Besides its
communication capabilities, it is an open platform for hosting
third-party software.
SecFlow®­1p features a security hardened operating system,
optimized to provide maximum performance with small SW
footprint.
With its maximum configuration, SecFlow-1p features four GbE
copper ports and two GbE SFP ports, two serial ports (single
RS-232 port or one RS-232 plus one RS-485/2W), a built-in Wi-Fi
modem, a GPS receiver for location indication and a cellular
modem with two SIM cards or two modems for maximum link
resiliency.
SecFlow-1p is equipped with serial interfaces for connectivity to
legacy equipment. As a gateway, it converts legacy serial
protocols to modern IP-based protocols, enabling seamless
communication from IP SCADA to both old and new RTUs. This
provides a single-box solution for multi-service applications and
smooth migration to all-IP networks.
When equipped with LoRaWAN radio, SecFlow-1p aggregates
multiple low-power low-bandwidth sensors/meters deployed
over a wide area. This provides an ideal solution for rural and
other non-dense areas saving CAPEX and OPEX.
SecFlow-1p features DIN-rail mounting, IP30 protection level,
and wide operating temperature range (-40°C to 65°C) without
fans. Powering options include an embedded, isolated DC power
supply, to meet the harsh environmental requirements.

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

SecFlow-1p addresses the Industrial IoT market, with
applications such as:
- Secure and resilient SCADA transport
- IIoT asset management
- Advanced resilient satellite communication
- Smart grid monitoring for power utilities
- Water resources management
- Smart meter concentration

## SINGLE/DUAL LTE MODEMS AND GPS  *(p.1)*

SecFlow-1p features flexible configuration for one LTE modem
with two SIM cards, or two embedded LTE modems, for
maximum resiliency. GPS for location reporting is also supported.
5G wireless technology employed by SecFlow-1p is designed to
provide higher peak data speeds of multiple Gbps, ultra-low
latency, more reliability, massive network capacity, increased
availability, higher performance and improved power efficiency.
* This feature will be released in a future version.

## SecFlow-1p RESILIENCY  *(p.2)*

A link redundancy mechanism allows tracking connectivity to
specific IP addresses using fault propagation and IP monitoring
capabilities.
**ROUTING**
SecFlow-1p features static routing, OSPF and BGP.

## VPN SERVICES  *(p.2)*

The device features a VPN gateway with two operation modes:
- Inter-site connectivity using 30 IPsec tunnels
- Remote user access using SSH
Inter-site VPN-based encrypted link ensures L3 transparent
connection of the Ethernet networks sites.
For remote access, the router uses an SSH-encrypted tunnel,
with user authentication and specific access authorization.

## CONTAINERS – NEXT LEVEL OF FLEXIBILITY  *(p.2)*

SecFlow-1p can host containerized edge applications, supporting
any 3rd party containers, which extend its original functionality to
a new level for Industrial IoT solutions.
Containers can easily be installed and managed via the Docker
CLI.

## MANAGEMENT AND SECURITY  *(p.2)*

Management
SecFlow-1p can be managed via Web, CLI, or by NETCONF.
RADview supports fault management, task management and
web shortcuts.
Embedded Advanced Security
For meeting the evolving security needs of distributed
environments, SecFlow-1p includes embedded security features
and options, such as stateful, zone-based firewall, and threat
protection.

## ZERO TOUCH PROVISIONING  *(p.2)*

For easy and safe mass-deployment, RAD offers Zero Touch
provisioning thus reducing OPEX and providing a simple way to
securely deploy thousands of elements in the network.
SecFlow-1p also supports a variety of access protocols including
SFTP.
Secure Industrial IoT with Edge Computing
-
Zero-touch server
-
PKI enrollment
-
SIEM
-
Firewall conf.

## Control Center Remote Locations  *(p.2)*

Containers
SecFlow-1p
Ethernet
& Serial
Containers
SecFlow-1p
Secure tunnels over any network for SCADA and management traffic
Firewall, 802.1x, Access list
**SecFlow-1p Specifications MEMORY AND STORAGE**
DRAM
1 Gb, 2 Gb
Flash Storage  8 Gb, 32 Gb

## INTERFACES  *(p.3)*

GNSS
GPS – American (default)
Galileo – European
Female SMA antenna connector
Ethernet
2 x 10/100/1000BASE-T ports
2 x 1000FX, 4 x 10/100/1000BASE-T ports
Cellular
5G, LTE modem with dual SIM
Female SMA antenna connector
SD Card
Max size: 32 Gb
Serial
1 RS-232 interface
2 RS-232 interfaces (non-isolated or isolated)
1 RS-232, 1 RS-485 interfaces (non-isolated or
isolated)
Connector: RJ-45
Wi-Fi
802.11b/g/n/ac dual band
RP-SMA antenna connector

## CELLULAR AND GPS  *(p.3)*

Cellular
Authentication
PAP, CHAP
Firmware
Upgrade
FOTA (Firmware upgrade Over the Air)
GPS
Location reporting
LTE
Dual LTE modems
Dual SIM
Single SIM
eSIM support: removable SIM with eUICC
Cellular bands – see Table 1
Multi APN
Supported for L450A/L450B
Operation
Modes
PPP, IP
SIM Card
Mini SIM, 25 mm x 15 mm (0.98 in x 0.59 in)
Form factor: 2 FF
Transmission
Modes
Diversity
MIMO

## LORAWAN  *(p.3)*

LoRaWAN
Module
EU868, RU864, US915, AS923 (1-4), AU915, KR920,
IN865 bands
SX1303 baseband processor
8 x 8 channels LoRa packet detectors
8 x SF5-SF12 LoRa demodulators,
8 x SF5-SF10 LoRa demodulators
LoRaWAN Class A, B, C
Packet forwarder

## SecFlow-1p  *(p.4)*

Table 1.  Integrated Cellular Modems
LTE
Ordering
Code
Modem Category and Frequency Bands
L1
CAT 4 EMEA/Korea/Thailand
LTE FDD: B1, B3, B5, B7, B8, B20
LTE TDD: B38, B40, B41
WCDMA: B1, B5, B8
GSM: B3, B8
L3
CAT 4 Australia/New Zealand/Taiwan/Brazil
LTE FDD: B1, B2, B3, B4, B5, B7, B8, B28
LTE TDD: B40
WCDMA: B1, B2, B5, B8
GSM: B2, B3, B5, B8
L4
CAT 4 North America, Verizon wireless + AT&T LTE
LTE FDD: B2, B4, B5, B12, B13, B14, B66, B71
WCDMA: B2, B4, B5
L4P
CAT 4 North American private networks (Anterix &
CBRS) + Public networks
LTE TDD: B48
LTE FDD: Anterix B8
LTE FDD: B2, B4, B5, B12, B13, B14, B26, B66
L4T
CAT 4 North America TAA (ready for PoC)
LTE: B1, B2, B4, B5, B12, B13, B14, B25, B26, B66,
B71
L450A
CAT 4 450 MHz for private LTE networks
LTE-FDD: B3, B7, B20, B31, B72
L450B
CAT 4 450 MHz for private LTE networks
LTE-FDD: B3, B20, B87
L5
CAT 4 Japan
LTE FDD: B1, B3, B8, B18, B19, B26
LTE TDD: B41
WCDMA: B1, B6, B8, B19
5G
5G NR sub-6 with Global support
FR1 (sub-6GHz): n1, n2, n3, n5, n28, n41, n48, n66,
n71, n77, n78, n79
LTE: B1, B2, B3, B4, B5, B7, B8, B12, B13, B14, B17,
B18, B19, B20, B25, B26, B28, B29, B30, B32, B34,
B38, B39, B40, B41, B46, B48, B66, B71
WI-FI
2.4/5 GHz
Mode
Access Point, Client
Radio Mode
802.11a/b/g/n/ac
Security
WPA2-AES
Users
8 concurrent
HaLow
Radio Mode
802.11ah Wi-Fi HaLow
Bands
902.0 ~ 928.0 MHz
Bandwidth
1/2/4 MHz
Security
OPEN, WPA2-PSK (AES), WPA3-OWE, WPA3-SAE
OFDM modulation with AES-CCMP encryption
Users
**Max. 22 concurrent**
Mode
Access point
Station mode
Simultaneous GATT server & client
Data Rate
Up to 4 Mbps
**Range**
Up to 1 km
Tx Power Gain +23 dBm
Max Input
Level
-10 dBm

## MANAGEMENT  *(p.4)*

Console Port
Ethernet port with the highest port number (4 or 6,
according to the device ordered), RJ-45 connector
Note: Console cable is not included and must be
ordered separately (see Optional Accessories)
Configuration Web-based interface using HTTPS
CLI with password-protected access
DHCP Server
IPv4, IP subnet pools support 256 addresses
Protocols
NETCONF server (v1.0/v1.1)/ YANG
SNMP v2/v3
SSH v2, HTTPS server, TFTP/SFTP
Users
User roles and privileges

## SecFlow-1p SECURITY  *(p.5)*

Trusted
Platform
Module
Secure boot
TPM2.0
Access Lists
Standard and extended
Authentication Locally, RADIUS, TACACS+ (also for authorization
and accounting)
Port-based: 802.1X on Ethernet and Wi-Fi
Multi-factor authentication (MFA)
One-time password (OTP)
Features
Login lockout
Firewall
Zone-based, stateful ACL rules
Public Keys
Public Key Infrastructure with X.509 certification for
Zero Touch
TLS 1.2/1.3
Certificates with SCEP or EST CA server
Session
Monitoring and limiting
IoT
Terminal server
SCADA protocol gateway*
Serial tunneling, IEC 101 to IEC 104*

## OAM  *(p.5)*

SLA
Monitoring
ICMP echo, UDP echo
ZTP
On-net
Off-net (over unsecured network) performs secure
“call home” using Public Key Infrastructure (X.509)

## ZONE-BASED FIREWALL  *(p.5)*

Type
Stateless
Stateful
IPv4 and IPv6
NAT
SNAT, DNAT
REDIRECT
NAPT/NAT
Configuration via Web GUI, SSH and SNMP
Rules
Interfaces are assigned to zones, for which a set of
rules is configured
IPv4 and IPv6
Limit maximum number of simultaneous
connections
Limit rules by traffic (kilobyte per second/packet
per second)
Rule hits reported to local LINUX Syslog*
DoS
Prevention
Blocklist
Defend from IP sweep

## IP ADDRESSING AND ROUTING  *(p.5)*

Addressing
IPv4 and IPv6
DHCP
Client, server, relay
IP helper addresses
DNS
Server
NAT
Static/dynamic
NAPT/NAT
Routing
Protocols
OSPF v2, BGP v4
VRRP
IP-BFD for fast route propagation*
Routing
Technologies
Static
Policy-based
VRF (10), router Interfaces (32)

## RESILIENCY  *(p.5)*

Link
Redundancy
Tracking connectivity to specific IP addresses using
fault propagation and IP monitoring
ERPS
Ethernet Ring Protection Switching

## DIAGNOSTICS  *(p.5)*

Features
Traceroute, ping
Syslog
Port mirroring
Alarm and event logs
IoT
Setting dry contacts based on pre-defined events,
generating syslog and device log event
SNMP traps on events
Dry Contacts
2 In, 2 Out (default)
3 In, 1 Out (special ordering option)
LEDs
Including alarm indication and cellular RSSI level
**TIMING**
Date and Time Local time setting
Protocol
SNTPv4
* This feature will be released in a future version.

## SecFlow-1p IP QUALITY OF SERVICE  *(p.6)*

Classification Port-based, IP-based, DSCP
Egress Queues 8 queues per port
Queuing
Class-based, SPQ, WFQ
Scheduling
Strict Priority/WRR
Traffic Class
Actions
CoS mapping (queues)
Marking, remarking (DSCP)
Traffic
Processing
Shaping

## IP VPNS  *(p.6)*

IPsec
Up to 30 tunnels
DH Groups
1 (768-bit modulus)
2 (1024-bit modulus)
5 (1536-bit modulus)
14 (2048-bit modulus)
19 (256-bit elliptic curve)
20 (384-bit elliptic curve)
ESP
Algorithms
AES CTR 128, 256 and 192, AES GCM 128 and 256,
ChaCha20-Poly1305
IKE Algorithms ECDH-SHA2 NISTP 521, 384 and 256, Curve25519-
SHA256, DH-Group18-SHA512, DH-Group17-
SHA512, DH-Group16-SHA512, DH-Group15-
SHA512, DH-Group14-SHA256, DH-GEX-SHA256
IKE Hashing
Algorithms
SHA2-256-128-HMAC, SHA2-512-256-HMAC
Protocols
Policy- and route-based IPsec, GRE
GREoIPsec
IKEv1, IKEv2
DMVPN client, DMVPN phase 3
L3 IPsec VPN
PPPoE supporting Broadband or LTE access
Technologies
NAT traversal
Interoperability with SCEP server 2012 and higher
**EDGE COMPUTING (CONTAINERS)**
Containers
Docker

## INTEGRATED ROUTING AND BRIDGING (IRB)  *(p.6)*

Bridges
Max 4
Bridge Ports
Max 32
MAC
Addresses per
Bridge
Max 512
Operation
Mode
VLAN-aware VLAN-unaware
Static or dynamic MAC addresses

## GENERAL  *(p.6)*

Compliance
EMC: EN 55032, EN 55035, EN 50121-4*, ETSI EN
301 489-1, ETSI EN 301 908-1, CFR 47 FCC, VCCI-
CISPR 32, AS/NZS CISPR 32
EU: CE
FCC and TUV for North America
Safety:  UL 62368-1, IEC/EN 62368-1
Industry standards: IEC 61850-3, IEEE 1613**
Hazardous locations (Hazloc) standards: UL 121201,
CSA C22.2 (Class I & II – Div 2) & (Class III - Div 1 & 2)
For use in Class I, Division 2 Groups A, B, C, D)
Temp. Class T4**
US Carrier: PTCRB, AT&T, Verizon*, T-Mobile
** Please contact the PLM for a certified platform
Environment
Storage
Temperature
-40 to 85°C (-40 to 185°F)
Operating
Temperature
DIN rail: -40 to 65°C (-40 to 149°F)
Humidity
Up to 90%
Physical
Height mm
(in)
138 (5.43)
Width
53.3 (2.1)
Depth
123.3 (4.85)
Weight
0.88 kg (1.94 lb)
Power
DC
12-48 VDC (10-60 VDC)
Non-isolated
WDC
24-48 VDC (20-60 VDC)
12-24-48 VDC (10-60 VDC)*
Isolated
12V
12- 24 VDC (11-30 VDC)
Isolated
EXT AC Power
Supply
90–240VAC
Power
Consumption
< 5W
Idle: 3.0W**
Typical: 3.6W**
Maximum: 4.5W**
**On a platform with one LTE modem
* This feature will be released in a future version.

## SecFlow-1p Ordering  *(p.7)*

The information below represents examples of supported
configurations. For additional configuration options, please
contact your local RAD partner.
SF-1P/E1/DC/4U2S/2RS/L450A/2R
SF-1P/E1/DC/4U2S/2RS/2R
SF-1P/E1/DC/4U2S/2RS/L1/G/2R
SF-1P/E1/DC/4U2S/2RS/L1/G/L1/2R
SF-1P/E1/DC/4U2S/2RS/L3/G/2R
SF-1P/E1/DC/4U2S/2RS/LRA/2R
SF-1P/E1/DC/4U2S/2RSM/5G/2R
SF-1P/E1/DC/4U2S/2RSM/5G/G/LRB/2R
SF-1P/E1/DC/4U2S/2RSM/5G/LRA/2R
SF-1P/E1/DC/4U2S/2RSM/L1/G/LRA/2
SF-1P/E1/DC/4U2S/2RSM/L1/G/WF/2R
SF-1P/E1/DC/4U2S/2RSM/L3/G/2R
SF-1P/E1/DC/4U2S/2RSM/L3/G/L3/2R
SF-1P/E1/DC/4U2S/2RSM/L4/G/LRA/2R
SF-1P/E1/WDC/4U2S/2RMI/L4/RG/2R

## ORDERING OPTIONS  *(p.7)*

Some options are not supported by all models. Some option
combinations are invalid or may require a minimum order. To
determine the BOM for your application, please contact your
local RAD partner.
Cellular
Ports
L1
LTE modem for Europe
L3
LTE modem for Oceania and Latin America
L4
L5
LTE modem for North America, Verizon wireless +
AT&T
LTE modem for Japan
L450A
LTE modem 450MHz for private LTE networks, LTE-
FDD: B3/7/20/31/72
L450B
LTE modem 450MHz for private LTE networks, LTE-
FDD: B3/20/87
L4P
LTE modem for North American private networks
(Anterix & CBRS) + Public networks
5G
5G modem with SA and NSA global support with
fallback to LTE or 3G
L4T (Ready for PoC)
Notes:
-
In options with dual modems, both modems are of the same type
(L1, L3, L4, L4P, L450A or L450B).
-
The cellular modem is supplied with two matching antennas (see
Supplied Accessories).
Certification
RG
IEC 61850-3 and IEEE-1613 compliant
Dry Contacts
Default 2 input + 2 output
3DI
3 input + 1 output
Ethernet Ports
2U
2 x UTP ports
4U2S
4 x 10/100/1000BASE-T and 2 x SFP ports
GNSS
G
Integrated GPS
Note: The GPS modem is supplied with one antenna (see
Supplied Accessories).
LoRaWAN
Modem
LRA
LoRaWAN modem with 8 channels and
frequency scheme selectable for US915,
AU915, AS923-(1-4), or KR920
LRB
LoRaWAN modem with 8 channels and
frequency scheme selectable for EU868,
IN865, or RU864
Note: The LoRaWAN modem is supplied with one antenna
matching the frequency ordered.
Power Supply
DC
12/24/48V input voltage (10–60 VDC), non-
isolated
WDC
24/48 input voltage (20–60 VDC), isolated
12V
12/24 input voltage (11–30 VDC), isolated
RAM
Default 1G RAM
2R
2G RAM
Serial Ports
1RS
1 RS-232 interface
2RS
2 RS-232 interfaces
2RSM
1 RS-232, 1 RS-485 interfaces
2RSI
2 RS-232 interfaces, isolated
2RMI
1 RS-232, 1 RS-485 interfaces, isolated
Wi-Fi Interface WF
Wi-Fi 2.4 GHz/5 GHz
WH
Wi-Fi 900 MHz HaLow
Note: The WiFi modem is supplied with two matching antennas
(see Supplied Accessories).

## SecFlow-1p  *(p.8)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel/Fax 972-52-4748272 | Fax 972-3-6498250
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
743-100-02/26 (6.4) Specifications are subject to change without prior notice. © 2019–2026 RAD Data Communications Ltd. The RAD name, logo, logotype, and the product
names Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their
respective holders.

## SUPPLIED ACCESSORIES  *(p.8)*

SF-ANT-GPS-PAS-3DBI-MAG/3M
GPS passive antenna, 3m, for options with integrated GPS
SF-ANT-LTE699-4DBI-SMA
LTE antenna, 4dBi, for options with LTEx modems
SF-ANT-WIFI-DUALBAND-3DBI-SMA
WiFi dual band antenna, 3 dBi, for options with WiFi modem
SF-ANT-LoRA-3DBI-SMA
LoRaWAN antenna, 3 dBi, for options with LoRaWAN modem
Note: The LoRaWAN modem is supplied with one antenna
matching the frequency ordered: EU868, AU915, US915, AS923
(1-4), RU864, KR920, IN865
SF-1P-CONN/TB
TB connectors for the DC power and dry contacts

## OPTIONAL ACCESSORIES  *(p.8)*

For an AC power supply, order a DC option +one of the two
power supplies below.
SF-AC-12VDC-20W-EX
External AC to 12 VDC 20W power supply
SF-AC-12VDC-16W-JP
External AC power supply for Japanese market

## SF-AC-12VDC-20W  *(p.8)*

External DIN Rail AC to 12 VDC 20W power supply
CBL-ETH/STP/STR/1M
Console port cable
CBL-RJ45/D9/F/6FT
Serial RS-232 data port cable
CBL-SF-RJ45-RS485
Serial RS-485 data port cable
RM-DIN-SINGLE
Adaptor for mounting a single device in a 19-inch/23-inch DIN
rail
RM-DIN-19
Adaptor for mounting a single/multiple devices in a 19-inch DIN
rail
SF-ANT-LTE700-7DBI-MGNT
Outdoor magnetic base antenna for SecFlow-1p LTE options and
for LoRaWAN 868 and 915 MHz, 7 dBi
SF-ANT4G-2M
LTE screw antenna, 2m (6.5 ft) cable, 3 dBi, 699-960 MHz/
1710-2170 MHz/2500-2690 MHz
SF-ANT4G-5M
LTE screw antenna, 5m (16.4 ft) cable, 3 dBi, 699-960 MHz
/1710-2170 MHz/2500-2690 MHz
SF-ANT-GPS-PAS-3DBI-MAG/3M
GPS passive antenna, 3m