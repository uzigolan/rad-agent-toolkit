# SecFlow-2 Ruggedized SCADA-Aware Ethernet Switch/Router

<!-- datasheet product=secflow-2 family=secflow kind=system source=secflow-2_4.3_ds_ga.pdf -->

*Datasheet `secflow-2_4.3_ds_ga.pdf`, 7 pages. Product `secflow-2`, family `secflow` (system).

## SecFlow-2 Ruggedized SCADA-Aware Ethernet Switch/Router  *(p.1)*

- Compact ruggedized Ethernet switch/router with up to
16×10/100BASE-T, and 2×100/1000BASE-FX ports with
optional PoE for deployment in harsh industrial
environments
- Advanced security package, including IEEE 802.1X port-
based Network Access Control, L-2/3/4 ACL for incoming
traffic, and L-2/3 VPN with IPsec
- Integrated serial interface with protocol gateway and
tunneling functionality
- Ethernet switching, IP routing with integrated VPN and
link protection per ITU-T G.8032, with optional cellular
2G/3G/HSPA+/4G (LTE) uplink for maximum service
continuation
- IEC61850 design*
- IPsec VPN over cellular and fiber with X.509 certificates
- Wide range of AC or DC power input options
SecFlow®-2 is a ruggedized Ethernet switch/router with a unique
built-in packet processing SCADA-aware engine to fit the
mission-critical industrial applications.
SecFlow-2 features two Gigabit Ethernet ports, up to 16 Fast
Ethernet ports, and serial ports for legacy services. The device is
designed for installation under harsh environmental conditions.
It enables DIN-rail mount, ensures IP30 protection level, wide
temperature operating range (-40 to 70°C) without fans, EMI
immunity (IEC61850-3, IEEE1613 and EN50121-4).
SecFlow-2 complies with the IEC 61850 standard to provide
Intelligent Electronic Device (IED) solutions for electrical
substations automation.
Additionally, SecFlow-2 is equipped with the serial interfaces for
connectivity between legacy RTUs and new IP-based IEDs.
SecFlow-2 gateway converts legacy DNP3-Serial to DNP3-TCP,
IEC-101 protocol to IP-based IEC-104, and Modbus RTU to
Modbus TCP, enabling seamless IP SCADA communication to
both old and new RTUs. This provides a single box solution for
multi-service applications and smooth migration to all-IP
networks.

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

SecFlow-2 addresses the following markets:
- Utility installations (electricity, water, gas and oil)
- Intelligent transportation (highway, railway)
- Manufacturing facilities (chemical, food industry)
- Military and defense applications (HLS, safe city)

## INTEROPERABILITY  *(p.1)*

SecFlow-2 is compatible with SecFlow-1, SecFlow-1v and
SecFlow-4. In addition, it operates with RAD’s Airmux broadband
wireless multiplexer, providing PoE feeding to the Airmux
outdoor units (see Ordering).

## ETHERNET  *(p.1)*

Flexible QoS techniques ensure differentiated service end-to-end
delivery.
SecFlow-2 utilizes the following traffic management methods:
strict priority, Weighted Round Robin (WRR), ingress policing and
egress traffic shaping.

## ROUTER AND VPN SERVICES  *(p.1)*

SecFlow-2 features static routing, OSPF, RIPv2, VRRP, NAT.
In addition, the device features a VPN gateway with two
operation modes:
- Inter-site connectivity, using IPsec tunnels
- Remote user access, using SSH
Inter-site VPN, based on GRE tunnels over an IPsec encrypted
link and DMVPN, ensures L2/L3 Ethernet networks sites’
transparent connection.
For remote access, SecFlow-2 uses an SSH-encrypted tunnel with
user authentication and specific access authorizations.

## SecFlow-2 OAM  *(p.2)*

SecFlow-2 provides the following Ethernet OAM types:
- Single-segment (link) OAM according to IEEE 802.3-2005
(formerly 802.3ah) for remote management and fault
indication
- End-to-end connectivity OAM, based on IEEE 802.1ag, to
monitor Ethernet services proactively and guarantee the
contracted SLA
- End-to-end fault, service, and performance monitoring based
on ITU-T Y.1731

## RESILIENCY  *(p.2)*

SecFlow-2 supports Ethernet protection ring according to
G.8032, enabling fast failure detection and switchover.
Traditional resiliency protocols, such as RSTP (Rapid Spanning
Tree Protocol) and MSTP (Multiple Spanning Tree Protocol) per
IEEE 802.1D, are also supported.
Link aggregation is performed according to IEEE 802.3ad. LACP
aggregates the point-to-point links operating at the same data
rate. This enables SecFlow-2 to take advantage of increased
bandwidth.

## MANAGEMENT AND SECURITY  *(p.2)*

The device can be managed via:
- RADview, RAD’s carrier-class NMS for Windows and Linux
- Standalone Shelf View
SecFlow-2 also supports a variety of access protocols including
Telnet, SSH, SNMPv3, and TFTP/SFPT.

## Specifications CAPACITY  *(p.2)*

Throughput
Line rate L2/L3 switching throughput for hardware-based router
Switching
Switching latency below 10 μsec
Max. Number of MAC Addresses
16K
Max. Number of VLANs
4K
Internal Memory
1 GB DRAM
Remote Site B
IEC 104
RTU
104 Client
DNP3 Client
SCADA
NMS
Central Site
PSN
IEC 104
IEC 101
Remote Site A
IEC 101
ASDU3
ASDU2
IEC 101
IEC-104, DNP3
UDP/TCP
SSH (T. Server)
IEC 104
ASDU1
IEC 104
SecFlow-2
DNP3
RTU
DNP3
RTU
DNP3
RTU
SecFlow-2
HUB Device
Serial
Serial
Figure 1.  Connecting Legacy RTUs, Using Protocol Gateway and Stateful Firewall

## SecFlow-2 ETHERNET INTERFACES  *(p.3)*

Gigabit Ethernet Port
2 x SFP sockets
Fiber SFP: 100BASE-FX/1000BASE-SX/LX
Copper SFP: 100/1000BASE-TX
Fast Ethernet Port
8 x 10/100BASE-T RJ-45 ports
16 x 10/100BASE-T RJ-45 ports
8 x 10/100BASE-T RJ-45 + 8 x 100BASE-FX SFP ports
Copper ports are available with several PoE ordering options
Autonegotiation IEEE 802.3ab
Max Frame Size
9216 Bytes
**POE**
Compliance
IEEE 802.3af-2003 up to 15W per port
IEEE 802.3at-2009 up to 30W per port

## SERIAL INTERFACES  *(p.3)*

Up to 4 × RS-232 ports
Up to 2 x RS-485 ports
Transparent tunneling of serial streams
SCADA protocol gateway – serial over IP
Terminal Server
**CELLULAR**
Dual SIM GPRS/UMTS/LTE cellular modem

## ETHERNET  *(p.3)*

VLAN segregation per IEEE 802.1q
VLAN tagging according to L2–L4 headers
User policy for traffic type
L2 multicast with guaranteed QoS
IGMP Snooping (v1, v2, v3) for traffic optimization
**ROUTER**
Static Routing, OSPF, BGP, VRF, RIPv2 Routing, VRRP, NAT

## MANAGEMENT  *(p.3)*

Control Port
RS-232
USB Port
Local USB port for emergency boot
Management Capabilities
Command-line interface with password protected access and
authorization levels,
Telnet/SSH, SNMPv1, SNMPv2, SNMPv3, RADview-EMS, SFTP
Tools
RADIUS, TACACS+
Conditioned/scheduled system reboot
Remote management and upgrade
G.8032
Central Site
NMS
Serial
ETH
Remote Sites
RTUs
Serial
ETH
RTUs
SCADA
Server
SecFlow-2
SecFlow-2
SecFlow-2
Figure 2.  Operational WAN for CI
**SecFlow-2**
TFTP/SFTP Client
Syslog
LLDP discovery per IEEE802.1AB
DHCP client
DHCP relay, option 82
**TIMING**
NTP v2
Date/Time Setting
SNTP

## RESILIENCY  *(p.4)*

Ethernet Ring
Ethernet ring per ITU-T G.8032v2
IEEE 802.1s MSTP
IEEE 802.1w RSTP
Link Aggregation
LAG with LACP per IEEE 802.3ad
**DIAGNOSTICS**
Alarms
LEDs, including Alarm and status interfaces
Dry contact 2-in and 2-out

## SECURITY  *(p.4)*

Enable/disable port
Port-based authentication per IEEE 802.1X
Protection against DoS attacks
L2, L3, L4 Access Lists
OS Image Protection
Industrial VPN Agent
Remote access using SSH tunnel
Layer 2 GRE Transparent Ethernet Bridging
Layer 3 mGRE DMVPN
IPsec VPN
- Policy-based
- Route-based
- IKE, AES or 3DES encryption
- Dynamic key exchange
- X.509 certificates, IPsec CRL server, IPsec CA server

## GENERAL  *(p.4)*

Compliance
Safety regulations:
- UL 60950-1
- IEC/EN 60950-1
EMC regulations:
- EN 55032 Class A
- FCC Class A
Physical
Height: 148 mm (5.6 in)
Width: 72 mm (2.8 in)(8-port DC),
95 mm (3.7 in)(16-port DC),
151.5 mm (5.96 in)(AC)
Depth: 123.0 mm (4.8 in)
Weight: 1.7 kg (3.75 lb)(8-port DC),
2.07 kg (4.56 lb)(16-port AC)
Power
AC: 100–240 VAC
DC: 48VDC (20–60 VDC), 24VDC (20–32 VDC), 12VDC (10–18
VDC), 110VDC
(94–132 VDC)
Power Consumption
15W (regular operation / no PoE)
48 VDC: 135W (120W for PoE)*
AC-powered units: 135W or 255W (120W or 240W for PoE)
* Note: 48VDC options must be powered with 46VDC or 52VDC and up,
to support PoE or PoE+, respectively.
Environment
Storage Temperature: -40 to 85°C (-40 to 185°F)
Operating Temperature**: -40 to 70°C (-40 to 158°F)
Humidity: up to 90%
Operating temperature of SF-AC-48VDC-120W power unit:
- Without POE (power less than 15W):
-20 to 70°C (-4 to 158°F)
- With POE: -20 to 60°C (-4 to 140°F)
Rugged enclosure – fanless, IP 30-rated
Substation automation per IEC 61850-3/IEEE1613 EMI**
Vibration and shock resistance per EN50121-4
**Note: The operating temperature range and availability of some
certifications can vary depending on the ordering option. For more
information, refer to the SecFlow-2 Installation and Operation Manual.

## SecFlow-2 Ordering RECOMMENDED CONFIGURATIONS  *(p.5)*

SF2/B/AC/2GE8UTP
Basic option with Ethernet features, 90–240 VAC power supply,
2×GbE SFP and 8x10/100BASE-T Ethernet ports
SF2/B/AC/2GE16UTP/POE240W
Basic option with Ethernet features, 90-240 VAC power supply,
2×GbE SFP and 16 x 10/100BASE-T Ethernet ports, PoE on
8 x 10/100BASE-T ports up to 240W
SF2/B/48VDC/2GE8UTP/POE
Basic option with Ethernet features, 48 VDC (20–60 VDC) power
supply, 2 x GbE SFP and 8 x 10/100BASE-T Ethernet ports, Power
over Ethernet on 8 × 10/100BASE-T ports
SF2/B/48VDC/2GE16UTP/POE
Basic option with Ethernet features, 48 VDC (20–60 VDC) power
supply, 2 x GbE SFP and 16 x 10/100BASE-T Ethernet ports,
Power over Ethernet on 8 × 10/100BASE-T ports
SF2/B/48VDC/2GE16UTP/POE240W
Basic option with Ethernet features, 48 VDC (20–60 VDC) power
supply, 2 x GbE SFP and 16 x 10/100BASE-T Ethernet ports,
Power over Ethernet on 8 × 10/100BASE-T ports up to 240W
SF2/B/48VDC/2GE8UTP8SFP/POE
Basic option with Ethernet features, 48 VDC (20–60 VDC) power
supply, 2 x GbE SFP, 8 x 10/100BASE-T and 8 x 100BASE-FX ports,
Power over Ethernet on 8 × 10/100BASE-T ports
SF2/B/110VDC/2GE8UTP8SFP
Basic option with Ethernet features, 110 VDC (94–132 VDC)
power supply, 2 x GbE SFP, 8 x 10/100BASE-T, and
8 x 100BASE-FX Ethernet ports
SF2/S/48VDC/2GE8UTP
Routing with secured VPN and serial gateway, 48 VDC (20–60
VDC) power supply, 2 × GbE SFP and 8 x 10/100BASE-T Ethernet
ports
SF2/S/48VDC/2GE8UTP8SFP
Routing with secured VPN and serial gateway, 48 VDC (20–60
VDC) power supply, 2 × GbE SFP, 8 x 10/100BASE-T and
8 x 100BASE-FX Ethernet ports
SF2/S/48VDC/2GE16UTP
Routing with secured VPN and serial gateway, 48 VDC (20–60
VDC) power supply, 2 × GbE SFP and 16 x 10/100BASE-T Ethernet
ports
SF2/S/24VDC/2GE8UTP
Routing with secured VPN and serial gateway, 24 VDC (20–32
VDC) power supply, 2 × GbE SFP and 8 x 10/100BASE-T Ethernet
ports
SF2/S/24VDC/2GE8UTP8SFP
Routing with secured VPN and serial gateway, 24 VDC (20–32
VDC) power supply, 2 × GbE SFP, 8 x 10/100BASE-T Ethernet
ports, and 8 × 100BASE-FX Ethernet ports
SF2/S/12VDC/2GE8UTP
Routing with secured VPN and serial gateway, 12 VDC (10-18
VDC) power supply, 2 × GbE SFP and 8 x 10/100BASE-T Ethernet
ports
SF2/S/AC/2GE8UTP
Routing with secured VPN and serial gateway, 90–240 VAC
power supply, 2 × GbE SFP and 8 x 10/100BASE-T Ethernet ports
SF2/S/AC/2GE16UTP
Routing with secured VPN and serial gateway, 90–240 VAC
power supply, 2 × GbE SFP and 16 x 10/100BASE-T Ethernet ports

## SecFlow-2  *(p.6)*

SUFFIX
Optional Power over Ethernet (PoE) + Interface
SF2/S/24VDC/2GE8UTP/&
Routing with secured VPN and serial gateway, 24 VDC (20–32 VDC) power supply, 2×GbE SFP and 8x10/100BASE-T Ethernet ports
&
RS232
4 x RS-232 ports
RS232/CEL
4 x RS-232 ports, GPRS/UMTS cellular modem
LTEEU
LTE cellular modem with European bands
RS232/HSPAP
4 x RS-232 ports, high-speed packet access modem, 3.5G
RS232/LTEEU
4 x RS-232 ports, LTE cellular modem with European bands
RS232/LTENA
4 x RS-232 ports, LTE cellular modem with North American bands
SF2/B/AC/2GE8UTP/$
Basic option with Ethernet features, 90–240 VAC power supply, 2×GbE SFP and 8x10/100BASE-T Ethernet ports
$
CEL
GPRS/UMTS cellular modem
POE/RS232
PoE on 8 x 10/100BASE-T ports up to 120W, 4 x RS-232 ports
POE/RS232/CEL
PoE on 8 x 10/100BASE-T ports up to 120W, 4 x RS-232 ports, GPRS/UMTS cellular modem
RS232
4 x RS-232 ports
RS232/CEL
GPRS/UMTS cellular modem
POE
PoE on 8 x 10/100BASE-T ports up to 120W
POE240W
PoE on 8 x 10/100BASE-T ports up to 240W
SUFFIX
Optional Power over Ethernet (PoE) + Interface
SF2/S/48VDC/2GE8UTP/*
Routing with secured VPN and serial gateway, 48 VDC (20–60 VDC) power supply, 2×GbE SFP and 8x10/100BASE-T Ethernet ports
*
POE/CEL
PoE on 8 x 10/100BASE-T ports up to 120W, GPRS/UMTS cellular modem
POE/RS232
PoE on 8 x 10/100BASE-T ports up to 120W, 4 x RS-232 ports
POE/LTEEU
PoE on 8 x 10/100BASE-T ports up to 120W, LTE cellular modem with European bands
RS232
4 x RS-232 ports
RS232/CEL
4×RS-232 ports, GPRS/UMTS cellular modem
RS232/LTEEU
4×RS-232 ports, LTE cellular modem with European bands
POE/RS232/CEL
PoE on 8 x 10/100BASE-T ports up to 120W, 4 x RS-232 ports, GPRS/UMTS cellular modem
POE/RS232/LTEEU
PoE on 8 x 10/100BASE-T ports up to 120W, 4 x RS-232 ports, LTE cellular modem with European bands
POE2AM
PoE on 2 x 10/100BASE-T for RAD's Airmux and standard PoE for the remaining 6 x 10/100BASE-T ports
POE4AM/RS232
PoE on 4 x 10/100BASE-T for RAD's Airmux and standard PoE for the remaining 4 x 10/100BASE-T ports, 4 x RS-
232 ports
POE2AM/RS232/CEL PoE on 2 x 10/100BASE-T for RAD's Airmux and standard PoE for the remaining 6 x 10/100BASE-T ports, 4 x RS-
232 ports, GPRS/UMTS cellular modem
POE/RS232/HSPAP
PoE on 8 x 10/100BASE-T ports up to 120W, 4 x RS-232 ports, high-speed packet access modem, 3.5G
RS232/HSPAP
4 x RS-232 ports, high-speed packet access modem, 3.5G
RS232/LTEVZ
4 x RS-232 ports, LTE cellular modem with NA Verizon bands
RS232/LTENA
4 x RS-232 ports, LTE cellular modem with North American bands
POE/HSPAP
PoE on 8 x 10/100BASE-T ports up to 120W, high-speed packet access modem, 3.5G
POE/RS232/LTEVZ
PoE on 8 x 10/100BASE-T ports up to 120W, 4 x RS-232 ports, LTE cellular modem with NA Verizon bands
4RSM/LTEEU
2 x RS-232 and 2 x RS-485 ports, LTE cellular modem with European bands
POE/4RSM/LTEEU
PoE on 8 x 10/100BASE-T ports up to 120W, 2 x RS-232 and 2 x RS-485 ports, LTE cellular modem with European
bands
LTEEU
LTE cellular modem with European bands

## SecFlow-2  *(p.7)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel 972-3-6458181 | Fax 972-3-7604732
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
622-100-07/20 (4.3) Specifications are subject to change without prior notice. © 2013–2020 RAD Data Communications Ltd. The RAD name, logo, logotype, and the product
names Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their
respective holders.

## OPTIONAL ACCESSORIES  *(p.7)*

SF-AC-48VDC-120W
External DIN rail AC to 48 VDC power supply, 120W, -20 to 60°C
(-4 to 140°F); 60W at 65°C (149°F) and above
CBL-SF-RJ45-CONSOLE
Console port cable
CBL-RJ45/DB9/NULL
Serial port cable
CBL-SF-ALARM
SecFlow alarm port cable
SF-ANT3G-2M
Outdoor antenna for 3G cellular modem, 2m connecting cable
SF-ANT3G-5M
Outdoor antenna for 3G cellular modem, 5m connecting cable
SF-ANT4G-2M
Outdoor antenna for SecFlow 4G cellular modem, 2m connecting
cable, 3dBi, 699-960 MHz/1710-2170 MHz/2500-2690 MHz
SF-ANT4G-5M
Outdoor antenna for SecFlow 4G cellular modem, 5m connecting
cable, 3 dBi, 699-960 MHz/1710-2170 MHz/2500-2690 MHz