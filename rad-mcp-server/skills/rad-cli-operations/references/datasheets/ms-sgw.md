# MS-SGW VPN Aggregator, Router and Firewall Module

<!-- datasheet product=ms-sgw family=mp4100 kind=card source=ms-sgw.pdf -->

*Datasheet `ms-sgw.pdf`, 3 pages. Product `ms-sgw`, family `mp4100` (card).

## Megaplex-4 MS-SGW VPN Aggregator, Router and Firewall  *(p.1)*

- Static and dynamic routing
- Secured by design with L2/L3 VPNs, stateful firewall,

## and Radius  *(p.1)*

- Automated PKI (X.509) with integrated DNS resolver
- User-friendly, easy to use web-based GUI
- High availability (optional)
Part of the Megaplex multiservice module family, MS-SGW adds
to Megaplex-4 routing, L2/L3 VPN capabilities and stateful firewall
with an extensive networking feature set.
MS-SGW provides a future-proof, cost-effective solution for
secured L3 communication like SCADA communication
backhauling.
The module occupies two module slots in the Megaplex-4 chassis.
**INTEROPERABILITY**
MS-SGW interoperates with RAD’s SecurityGateway and SecFlow
product line.

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

MS-SGW aggregates multiple VPNs from remote SecFlow devices
and addresses Industrial IoT application, for example:
- Distributed automation in secondary substations
- Smart meter concentration
- Water resources management
- Smart retail.
MS-SGW is usually located behind the organizational firewall. It
may also serve as WAN gateway, depending on the customer
needs.

## MANAGEMENT AND SECURITY  *(p.1)*

In addition to routing, MS-SGW features rich security capabilities
(e.g. firewall, automated PKI, and RADIUS).
The device can be managed via the MS-SGW web-based
interface. Local or remote (SSH) menu-driven access is also
supported for basic and initial configuration.
MS-SGW is supported by RADview (RAD’s network management
system).
**Specifications STANDARDS**
IEEE 802.3, 802.3u, 802.1D, 802.1Q, 802.1p
**ETHERNET INTERFACE**
0BNumber of
Ports
1 internal GbE port (facing Megaplex-4
backplane)
Maximum
Frame Size
9600 bytes

## BRIDGE  *(p.1)*

Compliance
802.1D
IRB
Integrated Routing & Bridging Mode (one of the
bridge ports must have an IP address)
Mode
VLAN-unaware
Loop
avoidance
STP, RSTP
Multiple
bridges
Port mirroring

## MS-SGW ROUTER  *(p.2)*

Protocols
OSPFv2 (IPv4), OSPFv3 (IPv6)
Routing
Static and dynamic routing
Dual stack IPv4/IPv6 (the interface can have both
IPv4 and IPv6 addresses)
Single unicast router (single VRF)
DNS Resolver
Routing
interface
Resides on:
-
Physical Ethernet port
-
VLAN sub-interface
-
Double VLAN sub-interface
Policy Based
Routing
Based on Firewall rules
NAT
Static NAT (1:1)
NAPT
Port forwarding (hole punching)

## MANAGEMENT  *(p.2)*

Control Port
RS-232, UART interface, RJ-45 connector,
115200 bps
DHCP
DHCP client and server
DHCP relay
Options
Password-protected access, authorization levels
WEB GUI (full configuration and monitoring)
Local terminal via front panel control port (limited
configuration menus)
SSH (basic configuration menus)
RADview
Syslog
IPv4/IPv6 protocols
**TIMING**
Timing
NTP client and server

## SECURITY  *(p.2)*

VPN
OpenVPN
L2TP
Firewall
Stateful firewall
Configurable rules:
-
Per interface
-
Rule can apply to IPv4/ IPv6 L3 and L4 attributes
Firewall Rules: 200
RADIUS
RADIUS authentication
IPsec
IPv4 , IPv6
Transport/Tunnel mode
Multiple concurrent IPsec sessions
Built-in SCEP client
IPSec Authentication:
- User-configurable
- IKEv1, IKEv2
- Certificates (SCEP)
- PSK ( Pre Shared Key)
Encryption algorithms: AES-CBC, AES-GCM
128/192/256, Blow-Fish, 3DES, CAST 128
Hash algorithms: MD-5, SHA-1, SHA-256/384/512,
AES-XCBC
PKI with X.509 certification
IPSec 300 concurrent tunnels
NAT-T (NAT Traversal)
**RESILIENCY**
High
availability
State synchronization
Configuration synchronization
Common Address Redundancy Protocol
**DIAGNOSTICS**
LED Indicators RDY (green): The module is up and running
**USB PORT**
For factory use only

## MS-SGW  *(p.3)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel 972-3-6458181 | Fax 972-3-7604732
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
464-117-06/20 Specifications are subject to change without prior notice. © 1988–2020 RAD Data Communications Ltd. The RAD name, logo, logotype, and the product names
Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective
holders.

## GENERAL  *(p.3)*

Processor
2C Rangeley (Intel Rangeley ATOM 2 core
processor)
Environment
Operating
Temperature
-10°C to +55°C (14°F to 131°F)
Storage
Temperature
-20°C to 70°C (-4°F to 158°F)
Humidity
up to 95%, non-condensing
Power
Power
Consumption 35W max

## Ordering  *(p.3)*

MP-4100M-MS/SGW/R2C
Megaplex-4 multiservice module, Security gateway, 2C Rangeley
(Intel Rangeley ATOM 2 core processor)
The module must be ordered together with a RADcare Package
and RADcare Project Assurance Package.