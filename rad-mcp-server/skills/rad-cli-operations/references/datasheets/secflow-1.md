# SecFlow-1 Ruggedized SCADA-Aware Router Gateway

<!-- datasheet product=secflow-1 family=secflow kind=system source=secflow-1_ds.pdf -->

*Datasheet `secflow-1_ds.pdf`, 4 pages. Product `secflow-1`, family `secflow` (system).

## SecFlow-1 Ruggedized SCADA-Aware Router Gateway  *(p.1)*

- Compact ruggedized SCADA-aware router gateway for
serial and Ethernet devices, supporting IEC-101, IEC-
104, Modbus, and DNP3 protocols
- Resilient 3G/HSPA+/LTE cellular network uplink for
maximum service continuity with multi-service Ethernet
and Serial (RS-232/RS-485) interfaces
- L3 VPN with IPsec for secure connection over public
networks
- Zero Touch provisioning
- Stateful Firewall
- IEC 61850-3/IEEE1613
- Withstands harsh environment
SecFlow®­1 is an Ethernet router gateway, a member of RAD’s
SecFlow suite of ruggedized Ethernet products.
With a unique built-in packet processing SCADA-aware engine, it
fits mission-critical industrial applications. It is most suitable for
infrastructure at utility companies with remotely distributed
sites, connected to a SCADA control center. SecFlow­1 is installed
at remote locations, forwarding Ethernet or serial traffic over
fiber optic or cellular links.
SecFlow­1 features one FE UTP port and one GbE SFP port, two
serial RS-232 ports or one RS-232 plus one RS-485, and a cellular
modem with two SIM cards for maximum link resiliency.
SecFlow­1 utilizes Ethernet ports for new IEC 61850 compliance
IEDs for automation in substations.
SecFlow­1 is equipped with serial interfaces for connectivity of
legacy RTUs with new IP-based IEDs. SecFlow­1 gateway converts
legacy IEC-101 protocol to IP-based IEC-104, enabling seamless
communication from the IP SCADA to both the old and new
RTUs. This provides a single box solution for multi-service
applications and smooth migration to all-IP networks.
The gateway is designed for installation under harsh
environmental conditions. It features DIN-rail mount, IP30
protection level, wide operating temperature range (-40°C to
70°C) without fans, and EMI immunity (IEC61850-3, IEEE1613,
and EN50121-4).

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

SecFlow­1 addresses the following Industrial IOT:
- Distributed automation in secondary substations
- Smart meter concentration
- Water Resources Management
- Retail
- Out-of-band management using cellular uplink
**INTEROPERABILITY**
SecFlow­1 operates with SecFlow-2 and SecurityGateway.

## ROUTER AND VPN SERVICES  *(p.1)*

SecFlow-1SecFlow-1 features static routing, OSPF, BGP, VRF and
NAT.
The device features a VPN gateway with two operation modes:
- Inter-site connectivity using IPsec tunnels
- Remote user access, using SSH
Inter-site VPN based on IPsec encrypted link ensures L3
transparent connection of the Ethernet networks sites.
For remote access, the router uses an SSH-encrypted tunnel,
with user authentication and specific access authorization.

## MANAGEMENT AND SECURITY  *(p.1)*

The device can be managed via:
- RADview, RAD’s carrier-class NMS management system
- SecFlow web-based interface (HTTP/HTTPS)
SecFlow­1 also supports a variety of access protocols, including
CLI and TFTP.
Stateful Firewall
Based on pre-defined rules, the stateful firewall monitors and
manages all the traffic passing through the device. Packets that
are out of communication context or not allowed are dropped,
and the relevant events are reported to the management
system. The firewall is set up using the Firewall configurator tool
that can configure multiple firewall rules.
For more information, refer to the RADview online help.

## SecFlow-1  *(p.2)*

Off-net Zero Touch Provisioning
Using Zero Touch mechanism, SecFlow-1 can securely connect to
a bootstrap server over the public network and download a
customized file containing bootstrapping data. This ensures
secure mass provisioning of configuration files and device
software to the remote devices.
For more information, refer to the SecFlow-1 installation and
operation manual, and RADview online help.

## Specifications ETHERNET INTERFACES  *(p.2)*

Fast Ethernet Port
1 x 10/100BASE-T, RJ-45 connector
Autonegotiation IEEE 802.3ab
GbE Port
SFP socket
100BASE-FX/1000BASE-SX/LX
10/100/1000BASE-TX
Autonegotiation IEEE 802.3ab
Max Frame Size
1.5 kB

## SERIAL INTERFACES  *(p.2)*

2 RS-232 ports
1 RS-485 (4-wire) + 1 RS-232 port
Serial transparent tunneling byte mode
Serial-to-Ethernet protocol gateway
(IEC-60870-5-101, IEC-60870-5-104)
Modbus RTU/TCP and DNP3
Terminal server frame and byte mode

## CELLULAR MODEM  *(p.2)*

Dual-SIM cellular modem for HSPA+/EVDO or LTE networks
(technology backward-compatible)
Configurable Cellular authentication using PAP or CHAP
SIM Card
Mini SIM, 25 mm x 15 mm (0.98 in x 0.59 in)
Form Factor: 2FF

## NETWORKING  *(p.2)*

SCADA gateway for IEC101/104,
Modbus RTU/TCP and DNP3
L3 mGRE DMVPN
L3 IPsec VPN
Operation Center
Remote Sites
Serial
ETH
RTU
RTU
NMS
Server
PSN
FO
SecFlow-1
IP Services
VPN
HUB Device
3G/LTE
Wireless Network
Private VPN
Figure 1.  Industrial IoT Backhaul
**SecFlow-1 ROUTER**
Static routing, OSPFv2, BGP, VRF, IPv4, NAT

## MANAGEMENT  *(p.3)*

Authentication
Multi-user TACACS+ (up to 5 authorized users configured on the
server or locally)
Control Port
Interface: RS-232
Connector: RJ-45
Management Options
RADview
Web-based interface using HTTP or HTTPS
CLI with password-protected access and authorization levels
SFTP
SSH
SNMPv3
Off-net Zero Touch
Reboot by an SMS message
**TIMING**
Local time setting
Simple Network Time Protocol (SNTP)
**SECURITY**
SFTP client
Stateful Firewall
IPsec
X.509 certification

## RESILIENCY  *(p.3)*

Conditioned/scheduled system reboot
OSPF v2
Cellular ISP redundancy (SIM cards backup)
Redundant VPN connectivity to SecurityGateway or other secure
hub
**DIAGNOSTICS**
Statistic counters per interface
Syslog
SNMPv3 GET and traps
LEDs
2 input and 2 output dry contacts

## GENERAL  *(p.3)*

Compliance
Rugged enclosure – fanless, IP30 rated
Substation automation per IEC 61850-3/ IEEE1613 EMI
Vibration and shock resistance per EN50121-4
Physical
DIN Rail
Height: 106 mm (4.17 in)
Width: 44.7 mm (1.76 in)
Depth: 120 mm (4.72 in)
Weight: 0.6–1.0 kg (1.3–2.2 lb)
Power
48 VDC: 20–60 VDC
24 VDC: 11–36 VDC
Power Consumption
8W
Environment
Temperature:
Operating: -40 to 70°C (-40 to 158°F)
Storage: -40 to 85°C (-40 to 185°F)
Operation humidity: up to 90%

## SecFlow-1  *(p.4)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel 972-3-6458181 | Fax 972-3-7604732
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
611-100-09/19 (4.4) Specifications are subject to change without prior notice. © 2013–2019 RAD Data Communications Ltd. RAD products/technologies are protected by
registered patents. To review specifically which product is covered by which patent, please see ipr.rad.com. The RAD name, logo, logotype, and the product names MiNID,
Optimux, Airmux, IPmux, and MiCLK are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.

## Ordering  *(p.4)*

SF1/48VDC/1UTP1GBE/2RS232/HSPAP
48 VDC (20-60 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces, cellular interface
SF1/48VDC/1UTP1GBE/2RS232/LTENA
48 VDC (20-60 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces, LTE cellular modem
with North American bands
SF1/48VDC/1UTP1GBE/2RS232/LTEVZ
48 VDC (20-60 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces, LTE modem with
North American Verizon bands
SF1/24VDC/1UTP1GBE/2RS232/LTEVZ
24 VDC (11-36 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces, LTE modem with
North American bands Verizon bands
SF1/48VDC/1UTP1GBE/2RS232/LTEEU
48 VDC (20-60 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces, LTE cellular modem
with European bands
SF1/24VDC/1UTP1GBE/2RS232/LTEEU
24 VDC (11-36 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces, LTE cellular modem
with European bands
SF1/24VDC/1UTP1GBE/2RS232/HSPAP
24 VDC (11-36 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces, cellular interface
SF1/48VDC/1UTP1GBE/2RS232
48 VDC (20-60 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces
SF1/48VDC/1UTP1GBE/2RSM
48 VDC (20-60 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 1 RS-232 and 1 RS-485 serial interfaces
SF1/24VDC/1UTP1GBE/2RS232
24 VDC (11-36 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces
SF1/48VDC/1UTP1GBE/2RS232/LTEOL
48 VDC (20-60 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces, LTE cellular modem
with Oceania and LATAM bands
SF1/24VDC/1UTP1GBE/2RS232/LTEOL
24 VDC (11-36 VDC), 10/100BASE-T Ethernet port and Gigabit
Ethernet SFP port, 2 RS-232 serial interfaces, LTE cellular modem
with Oceania and LATAM bands

## OPTIONAL ACCESSORIES  *(p.4)*

CBL-SF-RJ45-CONSOLE
Console port cable
CBL-RJ45/DB9/NULL
Serial port cable
SF-AC-48VDC-40W
AC to 48 VDC power supply, 40W, -20 to 60°C (-4 to 140°F);
20W at 60°C (140°F) and above
RM-DIN-SINGLE
Rack Mount adaptor for single DIN RAIL device
RM-DIN-19
19” Rack Mount adaptor for DIN RAIL device
SF-ANT3G-2M
Outdoor antenna for 3G cellular modem, 2m connecting cable
SF-ANT3G-5M
Outdoor antenna for 3G cellular modem, 5m connecting cable
SF-ANT4G-2M
Outdoor LTE antenna for 4G cellular modem, 2m connecting
cable, 3dBi, 699-960 MHz/1710-2170 MHz/2500-2690 MHz
SF-ANT4G-5M
Outdoor LTE antenna for 4G cellular modem, 5m connecting
cable, 3dBi, 699-960 MHz/1710-2170 MHz/2500-2690 MHz