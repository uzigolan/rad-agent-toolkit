# SecFlow-1c-5G Industrial 5G Cellular Router

<!-- datasheet product=secflow-1c-5g family=secflow kind=system source=secflow-1c-5g_ds.pdf -->

*Datasheet `secflow-1c-5g_ds.pdf`, 4 pages. Product `secflow-1c-5g`, family `secflow` (system).

## SecFlow-1c-5G Industrial 5G Cellular Router  *(p.1)*

- Industrial Design, DIN Rail Mounting Supported
- 5G SA/NSA
- Reliable Connectivity with Dual SIM
- Wi-Fi 6/5/2.4 GHz
- VPN Secure Connection
- 4 Ethernet Interfaces (1 WAN, 3 LAN)
- 1 x RS-232 + 1 x RS-485 Serial Ports
- GNSS Location
- BLE 5.2
SecFlow-1c-5G is a premier solution for industrial connectivity,
offering cutting-edge 5G technology for high-speed and reliable
data transfer. With Dual SIM functionality, it provides continuous
communication and network redundancy. APN/VPDN private
network access and dual SIM backup design guarantee data
transmission security and provide high-speed, reliable routing
and data transmission capabilities. Equipped with 5 Gbps
Ethernet ports, Wi-Fi 6.0, RS-232/RS-485 port, it can be widely
used in telecommunications, finance, information media, branch
office, smart city and smart factory.

## SecFlow-1c-5G Specifications HARDWARE  *(p.2)*

Ethernet Ports 1 x WAN (10/100/1000 Mbps), 3 x LAN
(10/100/1000 Mbps)
Mobile
5G SA/NSA + 4G LTE + WCDMA
Wi-Fi
IEEE 802.11 b/g/n/ac/ax, 2.4/5G/6GHz
Serial Ports
1 x RS-232
1 x RS-485
TF Slot
WiFi Antennas 3 x RP-SMA
GNNS Antenna 1 x SMA
GPIO
1 x DI, 1 x DO
LED indicators
Power, Network Connection, Wi-Fi, GNSS, Mobile
Status and Signal Strength, WAN
Reset Button

## CELLULAR AND GPS  *(p.2)*

SIM Slots
SIM Switch
2 SIM cards, auto-switch cases: weak signal, data
limit, data connection fail
Mobile Antennas  4 x SMA for 5G
Protocols
Cellular IP Context. PPP, PAP, CHAP, APN per SIM
GPS
GPS, GLONASS, BeiDou, Galileo, NMEA forwarding
(if GPS is hardware-supported)
LTE Bands
EU
Cat 19 (Downlink) / Cat 18 (Uplink)
LTE-FDD: B1/B3/B5/B7/B8/B20/B28/B32
LTE-TDD: B38/B40/B41/B42/B43
WCDMA: B1/B5/B8
AU
Cat 19 (Downlink) / Cat 18 (Uplink)
LTE-FDD: B2/B4/B5/B7/B8/B26/B28/B66
LTE-TDD: /B38/B40/B42/B43
WCDMA: B2/B4/B5
NA
Cat 19 (Downlink) / Cat 18 (Uplink)
LTE-FDD: B2/B4/B5/B7/B12/B13/B14/
B17/B25/B26/B29/B30/B66/B71
LTE-TDD: B38/B41/B42/B43/B48
5G NR Bands
EU
3GPP Rel-16 NSA/SA operation, Sub-6 GHz
5G NR NSA: n1/n3/n5/n7/n8/n20/n28/n38/n
40/n41/n75/n76/n77/n78
5G NR SA: n1/n3/n5/n7/n8/n20/n28/n38/n
40/n41/n75/n76/n77/n78
AU
3GPP Rel-16 NSA/SA operation, Sub-6 GHz
5G NR NSA: n2/n5/n7/n8/n28/n38/n40/n6
6/n71/n78
5G NR SA: n2/n5/n7/n8/n28/n38/n40/n6
6/n71/n78
NA
3GPP Rel-16 NSA/SA operation, Sub-6 GHz
5G NR NSA: n2/n5/n7/n12/n13/n14/n25/n26
/n29/n30/n38/n41/n48/n66/n70 /n71/n77/n78
5G NR SA: n2/n5/n7/n12/n13/n14/n25/n26
/n29/n30/n38/n41/n48/n66/n70 /n71/n77/n78
WI-FI
Mode
Access Point, Client
Radio Mode
IEEE 802.11 b/g/n/ac/ax, 2.4/5G/6GHz z

## SecFlow-1c-5G MANAGEMENT  *(p.3)*

Access Control
Flexible access control of SSH, Web interface, CLI,
RADIUS
Management access control. Possible to block
access from local ports, or to block specific
protocols (Web, SSH, etc.)
Protocols and
Security
SSH (v1, v2), TLS 1.2, 1.3
SSH from LAN, WAN (ETH/Cellular)
HTTPS From LAN, WAN (ETH/Cellular)
SNMP (v1, v2, v3), SNMP Traps, access rights
SYSLOG
WEB UI
Status, configuration, SW update, CLI,
troubleshooting, availability notifications, event
log, system log, kernel log, Internet status,
configuration backup, FOTA
Serial Functions Console, Serial over IP, Modem, MODBUS
gateway
MQTT
MQTT Broker, MQTT publisher
Modbus MQTT
GW
Allows sending commands and receiving data
from MODBUS server through MQTT broker
Modbus
Modbus master, Modbus client
SMS
SMS based device emergency actions
Reboot, switch SIM card, get status, restore
factory setting
Programmable
Reboot
Every day/week, or cellular interface restart
Continuous ICMP
Ping
Every X seconds to central IP
Configuration
Management
Config download/upload using HTTPS or using CLI
(sFTP)
Firmware
Management
Firmware upload using HTTPS or using CLI (sFTP)
Statistics
Ports & CPU statistics available via
CLI/Web/SNMP

## RESILIENCY  *(p.3)*

Network Backup
Automatic failover between Mobile, Wi-Fi
WAN and wired links
Load Balancing
Auto load balance over Mobile, Wired or WiFi
links

## NETWORKING CAPABILITIES  *(p.3)*

Network Protocols
NTP (Server, GPS synchronization)
DNS, DDNS: DNS Client, Bind dynamic IP to
static hostname
DHCP
Server, Client, Static and dynamic IP
allocation
VPN
PPTP, L2TP, IPsec, GRE, OpenVPN
VLAN
802.1q
Firewall
L2/L3/L4 ACL
Web Filter
IP/Domain Filter
Blacklist, Whitelist
NAT/SNAT/DNAT
MAC Filter
DDOS Prevention
Routing
Static Routing
Dynamic routing (RIP)

## DIAGNOSTICS  *(p.3)*

Features
Tcpdump
Ping
Tracert
IP Monitoring
Ping Reboot
LCP and ICMP for link inspection
Timing Task
DI /DO /AI
Status, report, switch

## SecFlow-1c-5G  *(p.4)*

24 Raoul Wallenberg St., Tel Aviv 6971920, Israel
Tel/Fax 972-52-4748272 | Fax 972-3-6498250
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
787-103-05/25 (1.0) Specifications are subject to change without prior notice. © Error! Switch argument not specified. RAD Data Communications Ltd. RAD
products/technologies are protected by registered patents. To review specifically which product is covered by which patent, please see ipr.rad.com. The RAD name, logo,
logotype, and the product names MiNID, Optimux, Airmux, IPmux, and MiCLK are registered trademarks of RAD Data Communications Ltd. All other trademarks are the
property of their respective holders.

## GENERAL  *(p.4)*

Environment
Casing
Material
Aluminum housing
Operating
Temperature
-30⁰C - +70⁰C
Storage
Temperature
-40⁰C - +85⁰C
Physical
Height
45 mm
Width
130 mm
Depth
100 mm
Weight
552g
Power
Power Socket PWR, ACC detection, GND
Operating
Voltage
8 – 32 VDC

## Ordering  *(p.4)*

SF-1C-Q3/5G/NA
SecFlow-1c-5G, North America region LTE bands
SF-1C-Q3/5G/EU
SecFlow-1c-5G, European region LTE bands
SF-1C-Q3/5G/AU
SecFlow-1c-5G, Oceania region LTE band
**SUPPLIED ACCESSORIES**
SF-1C-AC-12VDC-48W-4A
External AC to 12 VDC 48W 4A power supply