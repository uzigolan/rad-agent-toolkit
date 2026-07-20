# ETX-1p CPE for VPN and Cloud Access, Services/IoT Gateway

<!-- datasheet product=etx-1p family=etx1p kind=system source=etx-1p_ds.pdf -->

*Datasheet `etx-1p_ds.pdf`, 7 pages. Product `etx-1p`, family `etx1p` (system).

## ETX-1p CPE for VPN and Cloud Access Services/IoT Gateway  *(p.1)*

- Branch office router, optimized for cloud access services
**via IP-VPN, broadband or LTE networks**
- IoT gateway
- Edge computing by hosting 3rd party container software
**for customized applications**
- Zero Touch provisioning
- One or two embedded cellular modems (optional

## second cellular modem, Wi-Fi access point and client, or LoRaWAN)  *(p.1)*

- Two SIM cards for maximum link resiliency
- Wi-Fi access point and client
- GPS for location reporting
- Zone-based stateful firewall

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

Digital transformation accelerates the adoption pace of new
services. Service providers deliver value-added services from
their data centers, including networking (e.g., voice, secure
Internet access) and IT (e.g., cloud on-ramp) services.
ETX-1p is a branch office CPE, enabling business customer
transition to the cloud.
ETX-1p features a security hardened operating system, optimized
to provide maximum performance with small SW footprint.
By combining powerful networking capabilities with flexible
connectivity options, rich management interfaces, and
embedded security services, ETX-1p enables service providers to
deliver advanced IP-VPN services, as well as value added virtual
services from the data center to the customer branch.
When equipped with LoRaWAN radio, ETX-1p aggregates
multiple low-power low-bandwidth sensors/meters deployed
over a wide area. This provides an ideal solution for rural and
other non-dense areas saving CAPEX and OPEX.
Reduced Total Cost of Ownership
The all-in-one form factor includes full-featured routing, security,
switching, LTE and Wi-Fi, making it easy to connect branches to
the Internet and critical applications, without the need for extra
hardware or complicated configurations.
The comprehensive, multi-service functionality together with a
variety of interfaces, enables ETX-1p to support multiple use-
cases and market segments in a single device, while reducing
capital costs and simplifying logistics and operations.
Flexible Overlay and Underlay
ETX-1p is the service provider’s demarcation point at branch
offices, enabling underlay connectivity to IP-VPN and broadband
networks, as well as overlay connectivity to the service
provider’s data center. Branch offices consume their networking
services from the service provider’s data center, including IP-VPN
connectivity to other branch offices, Internet access and public
cloud access.
ETX-1p serves as an endpoint for the underlay and overlay
networks at the branch site, offering resilient connectivity over
multiple links to IP-VPN and fixed/mobile broadband networks.
It can also serve as an endpoint for overlay connectivity to the
service provider’s data center to provide value added services
running at the data center and deploy centralized vCPE.
Branch site underlay connectivity is resilient with a backup link,
typically connected to a broadband network.
IoT
ETX-1p addresses the IoT market, with applications such as:
- Secure and resilient transport
- IoT asset management
- Advanced resilient satellite communication
- SMB IoT remote monitoring & management
- Smart meter concentration
**INTEROPERABILITY**
ETX-1p is compatible and can interwork with SecFlow-1p and any
routers that support standard protocols.

## VPN SERVICES  *(p.1)*

The device features a VPN gateway with two operation modes:
- Inter-site connectivity using 30 IPsec tunnels
- Remote user access using SSH

## ETX-1p  *(p.2)*

An inter-site VPN-based encrypted link ensures transparent L3
connection of the Ethernet networks.
For remote access, the router uses an SSH-encrypted tunnel,
with user authentication and specific access authorization.
**ROUTING**
ETX-1p features static routing, OSPF and BGP.

## SINGLE/DUAL LTE MODEMS AND GPS  *(p.2)*

ETX-1p features flexible configuration for one LTE modem with
two SIM cards, or two embedded LTE modems, for maximum
resiliency. GPS for location reporting is also supported. The
ETX-1p HW is ready for future support of 5G modems.

## CONTAINERS – NEXT LEVEL OF FLEXIBILITY  *(p.2)*

ETX-1p can host containerized edge applications, supporting any
3rd party containers, which extend its original functionality to a
new level. Containers can easily be installed and managed via
the Docker CLI.

## RESILIENCY  *(p.2)*

A link redundancy mechanism allows tracking connectivity to
specific IP addresses, using fault propagation and IP monitoring
capabilities.

## MANAGEMENT AND SECURITY  *(p.2)*

Management
ETX-1p can be managed via Web, CLI or by RADview.
To automate the setup of overlay connectivity to the data
center.
RADview supports fault management, task management and
web shortcuts.
Embedded Advanced Security
For meeting the evolving security needs of distributed
environments, ETX-1p includes embedded security features and
options, such as stateful, zone-based firewall, and threat
protection.

## DESIGNED FOR ZERO TOUCH AND EASY OPERATION  *(p.2)*

ETX-1p is designed to simplify operations, while providing service
providers visibility to their branch office demarcation.
ETX-1p incorporates secure Zero-Touch-Provisioning
mechanisms for agile and seamless vCPE deployment, reducing
truck rolls and minimizing mass deployment operating costs.
ETX-1p Business Services over Fiber and 4G/LTE
**ETX-1p Specifications MEMORY AND STORAGE**
DRAM
1 Gb, 2 Gb
Flash Storage  8 Gb, 32 Gb

## INTERFACES  *(p.3)*

GNSS
GPS – American (default)
Galileo – European
Female SMA antenna connector
LAN
4 GbE UTP (RJ-45)
Cellular
LTE modem with dual SIM
Female SMA antenna connector
WAN
1 GbE SFP and 1 GbE UTP (RJ-45) ports
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
LTE bands – see Table 1
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
EU868, RU864, US915, AS923 (1-4), AU915,
KR920, IN865 bands
SX1303 baseband processor
8 x 8 channels LoRa packet detectors
8 x SF5-SF12 LoRa demodulators,
8 x SF5-SF10 LoRa demodulators
LoRaWAN Class A, B, C
Packet forwarder
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
L450A
CAT 4 450 MHz for private LTE networks
LTE FDD: B3, B7, B20, B31, B72
L450B
CAT 4 450 MHz for private LTE networks
LTE FDD: B3, B20, B87
L5
CAT 4 Japan
LTE FDD: B1, B3, B8, B18, B19, B26
LTE TDD: B41
WCDMA: B1, B6, B8, B19
LTA
CAT 4 North America, TAA-compliant
LTE: B2, B4, B5, B12, B13, B14, B25, B26, B66, B71
WCDMA: B2, B4, B5
WI-FI
Frequency
2.4/5 GHz
Mode
Access Point, Client
Radio Mode
802.11a/b/g/n/ac
Security
WPA2-AES
Users
Max. 8 concurrent

## ETX-1p MANAGEMENT  *(p.4)*

Control Port
RS-232 interface, RJ-45 connector
Note: Control port cable is not included and must be
ordered separately (see Optional Accessories)
Configuration Web-based interface using HTTPS
CLI with password-protected access
DHCP Server
IPv4, IP subnet pools support 256 addresses
Protocols
SNMP v2/v3
SSH v2, HTTPS server, TFTP/SFTP
Users
User roles and privileges

## SECURITY  *(p.4)*

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

## ZONE-BASED FIREWALL  *(p.4)*

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

## IP ADDRESSING AND ROUTING  *(p.4)*

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

## OAM  *(p.4)*

SLA
Monitoring
ICMP echo, UDP echo
ZTP
On-net
Off-net (over unsecured network) performs secure
“call home” using Public Key Infrastructure (X.509)

## RESILIENCY  *(p.4)*

Link
Redundancy
Tracking connectivity to specific IP addresses using
fault propagation and IP monitoring
ERPS
Ethernet Ring Protection Switching

## DIAGNOSTICS  *(p.4)*

Features
Traceroute, ping
Syslog
Port mirroring
Alarm and event logs
LEDs
Including alarm indication and cellular RSSI level
**TIMING**
Date and Time Local time setting
Protocol
SNTPv4
* This feature will be released in a future version.

## ETX-1p IP QUALITY OF SERVICE  *(p.5)*

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

## IP VPNS  *(p.5)*

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

## INTEGRATED ROUTING AND BRIDGING (IRB)  *(p.5)*

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

## GENERAL  *(p.5)*

Compliance
EMC: EN 55032, EN 55035, ETSI EN 301 489-1, ETSI
EN 301 908-1, CFR 47 FCC, VCCI-CISPR 32, AS/NZS
CISPR 32, ICES-003
EU: CE
FCC and TUV for North America
Safety:  UL 62368-1, IEC/EN 62368-1
Environment
Temperature
Operating: -10 to 50°C (32 to 122°F)
Storage: -40 to 65°C (-40 to 149°F)
Humidity
5% to 90%, non-condensing
Physical
Enclosure
Plastic Box
Height
44 mm (1.73”)
Width
230 mm (9.05”)
Depth
175 mm (6.9”)
Weight
Net: 0.5 kg (1.1 lb)
Max (including device + package + power supply
+ cable adaptor + 2 LTE antennas + 2 Wi-Fi
antennas): 1.04 kg (2.3 lb)
Power
Power Supply
External 90–240 VAC
Power
Connector
12/24 VDC, unified polarity type DC jack
Ø2.0 mm
Power Consumption < 5W
Idle: 3.0W**
Typical: 3.6W**
Maximum: 4.5W**
**On a platform with one LTE modem

## ETX-1p Ordering  *(p.6)*

The information below represents examples of supported
configurations. For additional configuration options, please
contact your local RAD partner.
ETX-1P/ACEX/1SFP1UTP/4UTP/L1
ETX-1P/ACEX/1SFP1UTP/4UTP/L1/WF
ETX-1P/ACEX/1SFP1UTP/4UTP/L3
ETX-1P/ACEX/1SFP1UTP/4UTP/L4/WF
ETX-1P/ACEX/1SFP1UTP/4UTP/WF
ETX-1P/ACEX/1SFP1UTP/4UTP/L4/LRA/2R

## ORDERING OPTIONS  *(p.6)*

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
LTE modem for North America, Verizon wireless +
AT&T
L450A
LTE modem 450 MHz for private LTE networks, LTE-
FDD: B3/7/20/31/72
L450B
LTE modem 450 MHz for private LTE networks, LTE-
FDD: B3/20/87
L5
LTE modem for Japan
LTA
LTE modem for North America, TAA-compliant
Notes:
-
In options with dual modems, both modems are of the same
type (L1, L3, L4, L450A or L450B).
-
The cellular modem is supplied with two matching antennas
(see Supplied Accessories).
Ethernet LAN
Ports
4UTP
4 x RJ-45 GbE UTP
Ethernet WAN
Ports
1SFP1UTP
1 x 1000FX, 4 x 10/100/1000BASE-T
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
L9
LoRaWAN modem with 8 channels and
frequency scheme selectable for US915,
AS923, AU915, KR920, TAA compliant
Note: The LoRaWAN modem is supplied with one antenna
matching the frequency ordered.
Power Supply
ACEX
External AC power adaptor
RAM
Default 1G RAM
2R
2G RAM
Wi-Fi Interface WF
Wi-Fi 2.4 GHz/5 GHz
Note: The WiFi modem is supplied with two matching antennas  (see
Supplied Accessories).

## SUPPLIED ACCESSORIES  *(p.6)*

External AC to DC power supply
SF-ANT-GPS-PAS-3DBI-MAG/3M
GPS passive antenna, 3m, for options with integrated GPS
SF-ANT-LTE699-4DBI-SMA
LTE antenna, 4dBi, for options with LTEx modems
SF-ANT-WIFI-DUALBAND-3DBI-SMA
WiFi dual band antenna, 3 dBi, for options with WiFi modem
SF-ANT-LoRA-3DBI-SMA
LoRaWAN antenna, 3 dBi, for options with LoRaWAN modem
Note: The LoRaWAN modem is supplied with one antenna matching
the frequency ordered: EU868, AU915, US915, AS923 (1-4), RU864,
KR920, IN865

## ETX-1p  *(p.7)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel/Fax 972-52-4748272 | Fax 972-3-6498250
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
768-100-02/26 (6.4) Specifications are subject to change without prior notice. © 2019–2026 RAD Data Communications Ltd. The RAD name, logo, logotype, and the product
names Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their
respective holders.

## OPTIONAL ACCESSORIES  *(p.7)*

CBL-RJ45/D9/F/6FT
Control port cable with male RJ-45 and female DB-9 connector
SF-ANT4G-2M
Outdoor antenna for 4G cellular modem, 2m connecting cable,
3 dBi, 699-960 MHz/1710-2170 MHz/2500-2690 MHz
SF-ANT4G-5M
Outdoor antenna for 4G cellular modem, 5m connecting cable,
3 dBi, 699-960 MHz/1710-2170 MHz/2500-2690 MHz
SF-ANT-LTE700-7DBI-MGNT
Outdoor magnetic base antenna for ETX-1p LTE options and for
LoRaWAN 868 and 915 MHz, 7 dBi
RM-33-2
Hardware kit for mounting an ETX-1p device in a 19-inch rack