# SecFlow-4 Modular Ruggedized SCADA-Aware Ethernet Switch/Router

<!-- datasheet product=secflow-4 family=secflow kind=system source=SecFlow-4.pdf -->

*Datasheet `SecFlow-4.pdf`, 4 pages. Product `secflow-4`, family `secflow` (system).

## SecFlow®-4 Modular Ruggedized SCADA-Aware Ethernet Switch/Router  *(p.1)*

- High-density, modular, ruggedized Ethernet switch, deployed in harsh industrial
environments  with up to 28 GbE ports and optional PoE
- Advanced security package, including SCADA-aware firewall, IEEE 802.1X port-based
Network Access Control, L-2/3/4 ACL for incoming traffic and L-2/3 VPN with IPsec
- Integrated RS-232 and RS-485 serial interfaces with protocol gateway and tunneling
functionality for easy migration of legacy services to IP
- Ethernet switching, IP routing and Ethernet Ring protection per ITU-T G.8032
- IEC61850 compliant
The SecFlow-4 industrial Ethernet
switch/router combines ruggedized Ethernet
platform with unique SCADA-aware
processing engine to fit the mission-critical
industrial applications.
SecFlow-4 is a modular device with
7 interface slots. Each interface slot can
house either an Ethernet module or a
serial RS-232 module, enabling a flexible
network configuration.
The system overall capacity can scale up to
28xGbE full-duplex throughput, with
wire-speed switching for both Ethernet and
IP.
SecFlow-4 is designed for installation
under harsh environmental conditions. It
features DIN-rail mount, IP30 protection
level, wide temperature operating range
(-0°C to +75°C) without fans, EMI
immunity (IEC 61850-3, IEEE 1613, and
EN 50121-4).
MULTI-SERVICE GATEWAY
SecFlow-4 utilizes Ethernet ports for new
IEC 61850 compliance IEDs for automation
and teleprotection applications in
substations. Additionally, SecFlow-4 is
equipped with the serial interfaces for
connectivity of legacy RTUs with new IP
based IEDs. SecFlow-4 gateway converts
legacy IEC-101 protocol to IP-based
IEC-104, enabling seamless
communication from the IP SCADA to both
the old and new RTUs. This provides a
single box solution for multi-service
applications and smooth migration to
all-IP networks.
MARKET SEGMENTS AND
APPLICATIONS
SecFlow-4 addresses the following
markets:
-
Utility installations (electricity, water,
gas and oil)
-
Intelligent transportation (highway,
railway)
-
Manufacturing facilities (chemical, food
industry)
-
Military and defense applications (HLS,
safe city).
SCADA-AWARE FIREWALL
SecFlow-4 supports an integrated firewall
per port, providing a network-based
distributed security designed especially for
SCADA applications (IEC 104, Modbus TCP,
and DNP3 DCP). The device monitors
SCADA commands, using deep packet
inspection, to validate if they fit the
intended application purpose. Additionally,
the device features a VPN gateway with
two operation modes:
-
Inter-site connectivity, using IPSec
tunnels
-
Remote user access, using SSH.
Inter-site VPN based on GRE tunnels over
an IPSec encrypted link ensures L2/L3
transparent connection of the Ethernet
networks sites.
For remote access, the switch uses an
SSH-encrypted tunnel, with user
authentication and specific access
authorizations.
ETHERNET QUALITY OF SERVICE
Flexible QoS techniques ensure
differentiated service delivery end-to-end.
SecFlow-4 utilizes the following traffic
management methods: strict priority,
Weighted Round Robin (WRR), MDDR, and
egress traffic shaping.
SecFlow-4 IP address might be private
behind NAT, or public.
OAM
SecFlow-4 provides these types of
Ethernet OAM:
-
Single-segment (link) OAM according
to IEEE 802.3-2005 (formerly 802.3ah)
for remote management and fault
indication
-
End-to-end connectivity OAM based on
IEEE 802.1ag to monitor Ethernet
services proactively and guarantee that
customers receive the contracted SLA
-
End-to-end service and performance
monitoring based on ITU-T Y.1731.
Fault monitoring and end-to-end
performance measurement.

## SecFlow-4  *(p.2)*

RESILIENCY
SecFlow-4 supports Ethernet protection
ring according to G.8032, enabling fast
failure detection and switchover.
Traditional resiliency protocols such as
RSTP (Rapid Spanning Tree Protocol) and
MSTP (Multiple Spanning Tree Protocol)
per IEEE 802.1D are also supported.
Link aggregation is performed according
to IEEE 802.3ad with LACP allowing
aggregation of point-to-point links
operating at the same data rate. This
enables the switches to take advantage of
increased bandwidth.
INTEROPERABILITY
SecFlow-4 is compatible with SecFlow-2.
In addition, it operates with RAD’s Airmux
broadband wireless radios, providing PoE
feeding to the Airmux outdoor units (see
Ordering).
MANAGEMENT
The device can be managed via RADview,
RAD’s carrier-class NMS for Windows and
Unix, and SecFlow Network Manager that
provides end-to-end management for
SecFlow devices.
SecFlow-4 also supports a variety of
access protocols, including CLI, Telnet,
Web, SNMPv3, and TFTP.

## Specifications  *(p.2)*

CAPACITY
Throughput
Line rate L2/L3 switching throughput
Switching
Switching latency below 10 μsec
Max. Number of MAC Addresses
32K
Max. Number of VLANs
4K
ETHERNET
4×100/1000BaseTx ports (optional PoE
with max 30W per port/180W per chassis)
on SF4-M-4GbE module
4×10/100/1000BaseFX SFP ports on
SF4-M-4GbE module
Max Frame Size
12 kB
SERIAL INTERFACE
4×RS-232 ports
2xRS-232 + 1xRS-485
Transparent tunneling serial streams
Protocol gateway – serial to Ethernet,
IEC 101/104
Terminal server
SecFlow-2
SecFlow-2
Remote Site B
Modbus
RTUs
Modbus
RTU
104 Client
Modbus Client
SCADA
NMS
Central Site
PSN
Modbus RTU
IEC 101
Remote Site A
IEC 101
ASDU3
ASDU2
IEC 101
Modbus
RTU
Modbus
RTU
ID 12
ID 11
ID 13
IEC-104
UDP/IP
SSH (T. Server)
Modbus TCP
ASDU1
Modbus RTU
SecFlow-4
Figure 1.  Aggregating Traffic from Remote Substations with Protocol Gateway Functionality
QUALITY OF SERVICE (QoS)
VLAN segregation per IEEE 802.1q
VLAN tagging according to L2–L3 headers
L2 multicast with guaranteed QoS
IGMP snooping for traffic optimization
DSCP to 802.1p QoS mapping
LLDP
DHCP client
DHCP relay, option 82
ROUTER
Static routing, OSPF, RIPv2 routing, NAT
MANAGEMENT
Control Port
RS-232
USB Port
Local USB port for emergency boot
Management Options
Command-line interface with password
protected access, authorization levels
Telnet/SSH, SNMPv1, SNMPv2,
RADview-EMS, iSIM, SFTP
RADIUS, TACACS+
Date/Time Synchronization
SNTP
SECURITY
Access Control
Enable/disable port
Port access filter per MAC/IP addresses
Port-based authentication per IEEE 802.1x
Protection against DoS attacks
Service Validation
Egress filtering per VLAN
SCADA firewall per port (IEC 101/104,
DNP3.0)
Industrial VPN Agent
Remote access using SSH tunnel
Layer 2 GRE Transparent Ethernet Bridging
Layer 3 mGRE DM-VPN
X.509 certified IPSec encryption:
-
User policy for traffic type
-
IKE, AES or 3DES encryption
-
Dynamic key exchange
Remote Access Agent
Remote access using reverse SSH tunnel
Limited access authorizations per user
Local and remote user authentication and
authorizations
Traffic activity log for trail audit
TIMING
PTP transparent clock per 1588v2
NTP v.2
RESILIENCY
Ethernet Ring
Per ITU-T G.8032v2
Link Aggregation
LAG with LACP per IEEE 802.3ad
Rapid Spanning Tree
MSTP per IEEE 802.1s, RSTP per 802.1w
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
Order this publication by Catalog No. 805054
614-100-08/15 (3.6) Specifications are subject to change without prior notice.  2013–2015 RAD Data Communications Ltd. The RAD name, logo, logotype, and the terms EtherAccess, TDMoIP and TDMoIP Driven,
and the product names Optimux and IPmux, are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.

## SecFlow-4  *(p.4)*

GENERAL
Physical
Height: 14.5 cm (5.70 in)
Width:  38.0 cm (14.96 in)
Depth:  13.9 cm (5.47 in)
Weight: 2.4–4 kg (5.51–8.81 lb)
DIN rail mounting, optional wall mount
Power
Dual DC power supply: 24, 48 VDC
Power Consumption
Maximum power consumption for
SecFlow-4:
65W without PoE
250W with PoE
Maximum power consumption per module:
SF4-PS-24/48VDC – 8W
SF4-M-MNG – 18W
SF4-M-Service – 10W
SF4-M-Serial – 4.5W
SF4-M-4GBE/U – 4W
SF4-M-4GBE/S – 6W
Environment
Temperature:
Operating: -40 to 75°C (-40 to 167°F)
Storage: -40 to +85°C (-40 to 185°F)
Humidity: 5 to 95%
Rugged enclosure – fanless, IP 30-rated
Substation automation per
IEC 61850-3/IEEE1613 EMI
Voltage transient immunity per EN50121-4
Vibration and shock resistance per
IEC 60255-21

## Ordering  *(p.4)*

RECOMMENDED CONFIGURATIONS
Chassis
Switch Configuration
SF4/SP/48DCR
SecFlow-4 chassis, L-2 switch
functionalities, central processing and
management module, dual 48 VDC power
supply
SF4/SP/24DCR
SecFlow-4 chassis, L-2 switch
functionalities, central processing and
management module, dual 24 VDC power
supply
Router/Switch Configuration
SF4/RP/48DCR
SecFlow-4 chassis, L-2/3 router/switch
functionalities, central processing and
management module, dual 48 VDC power
supply
SF4/RP/24DCR
SecFlow-4 chassis, L-2/3 router/switch
functionalities, central processing and
management module, dual 24 VDC power
supply
Modules
SF4-PS-24VDC
24 VDC power supply
SF4-PS-48VDC
48 VDC power supply
SF4-M-4GBE-U
SecFlow-4 module with four
100/1000BasteT UTP Ethernet ports
SF4-M-4GBE-POE
SecFlow-4 module with four
100/1000BasteT UTP Ethernet ports and
30W PoE
SF4-M-4GBE-S
SecFlow-4 module with four
10/100/1000BasteFx SFP Ethernet ports
SF4-M-4RS232
SecFlow-4 module with four RS-232 serial
ports
SF4-M-2RS232-1RS485
SecFlow-4 module with two RS-232 serial
ports and one RS-485 serial port
SF4-M-Service
Service module with firewall, serial
tunneling, VPN functionalities and discrete
input/output interfaces
SF4-M-MNG
Central processing and management
module with local terminal and out-of-
band management ports
SUPPLIED ACCESSORIES
CBL-SF-RJ45-CONSOLE
Console cable (delivered with SF4-M-MNG)
OPTIONAL ACCESSORIES
SF4/RM1
Kit for mounting SecFlow-4 into a 19-inch
rack
CBL-RJ45-DB9/null
Serial cable, DCE wiring