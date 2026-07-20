# MiNID Miniature Programmable Network Interface Device

<!-- datasheet product=minid family=minid kind=system source=minid_2_6_ds_ga.pdf -->

*Datasheet `minid_2_6_ds_ga.pdf`, 5 pages. Product `minid`, family `minid` (system).

## MiNID Miniature Programmable Network Interface Device  *(p.1)*

- Field programmable Network Interface Device (NID) for
service providers, wholesalers, and mobile operators
- Part of RAD’s Distributed Network Functions
Virtualization (D-NFV) portfolio
- Patent-protected design for seamless integration and
enhancement of any existing network device
- Service demarcation, SLA assurance and diagnostic tools
at Layer 2, 3, and 4
- Low OpEx due to decreased power consumption, space
and installation costs
RAD’s patent-protected MiNID® is a field-programmable
miniature L2/L3 network interface device (NID), available in an
SFP form factor, SFP sleeve form factor with integrated optics, or
in a standalone enclosure. As part of RAD’s Distributed Network
Functions Virtualization (D-NFV) offering, MiNID enriches the
Service Assured Access portfolio with software-defined network
functionalities, including enhanced demarcation, remote
monitoring, and fault isolation. MiNID programmability is based
on a powerful FPGA that enables field updates to the product
software and application.
The SFP sleeve is a revolutionary platform for service providers
seeking to upgrade their networks to deliver reliable bandwidth
with end-to-end SLA assurance. MiNID’s innovative patent-based
design breaks through the barriers of cost and complexity to
make Carrier Ethernet available to everyone, everywhere. The
SFP sleeve patent-protected design is easily pluggable into
standard SFP ports, eliminating the use of external power, and
reducing space, and cabling expenses.
MiNID provides instant Carrier Ethernet functionality for
switches, routers, DSLAMs, and mobile base stations. It offers
comprehensive tools for service activation, performance
monitoring, and fault diagnostics, providing ongoing SLA reports
while reducing costs associated with fault isolation.
MiNID transparently envelops a large variety of SFPs, enabling
full reuse of customer equipment and seamless deployment over
multiple access infrastructure types, such as short-haul and long-
haul fiber connections, bidirectional single-fiber links, and
copper lines.
MiNID is also available as an SFP with integrated optical module.
In its standalone version, MiNID offers a compact, low power,
low-cost two-port solution. When equipped with combo
interfaces, it allows seamless installation in any field scenario;
when equipped with copper interfaces, it also offers bypass
relays that bypass the device in the event of critical failure.
MiNID is a true plug-and-play solution. Its zero-touch
provisioning capabilities enable easy installation by anyone.

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

As an important part of the toolkit offered by RAD’s Service
Assured Access portfolio, MiNID is the perfect solution for
service assurance in residential and mobile backhauling
networks, small cells, business services, and wholesale services.
As a service demarcation device, MiNID ensures proper service
handling throughout the service provider’s network by policing
customer traffic, attaching service VLANs, and adding priority
marking to multiple services at the customer premises.
Simultaneously, MiNID offers multi-layer performance
monitoring tools for every service. At Layer-2, it offers OAM and
PM tools that actively measure key performance indicators
including delay, jitter, and packet loss rate. At Layer-3, its
integrated TWAMP Light controller/responder and UDP echo
responder allow seamless monitoring across any packet network
and in multi-vendor environments.
For the mobile backhauling, MiNID can offer Sync-E support
including transparent ESSM message forwarding.
**ETHERNET**
MiNID can be ordered as an FE or FE/GbE device. The GbE option
features auto-negotiation and supports both rates.

## MiNID  *(p.2)*

For service demarcation, MiNID provides:
- Port-based and flow-based classification of multiple services
- Flow classification per VLAN, 2 VLANS, VLAN range, P-bits,
DSCP, EtherType or source/destination MAC address
- Per flow, MEF 10.3 policing
- VLAN or 2 VLAN addition, VLAN replacement per flow with
priority marking per P-bits and DSCP
- Layer-2 control protocol tunneling with optional MAC change
(L2PT)

## MONITORING AND DIAGNOSTICS  *(p.2)*

OAM
MiNID provides the following OAM tools per EVC.COS or
untagged traffic:
- IEEE-802.1ag (CFM) for continuity check, loopback, and link
trace
- ITU-T Y.1731 for loss (synthetic and real traffic), delay, and
delay variation measurements, as well as fault propagation
(AIS/RDI)
- MEF 36-based MIBS for PM reports
- EEE 802.3-2005 link OAM and dying gasp trap
- RFC-5357 TWAMP Light controller and responder with
multiple session reflectors offering hardware-based time
stamping.
Loopback Tests
MiNID can perform on-demand intrusive and non-intrusive
Layer-2/3/4 loopbacks at wire speed, with optional MAC, IP and
UDP port swap per flow. MiNID also offers UDP echo responder
functionality.
Service Activation Tests
MiNID responds to RFC-2544 and Y.1564 service activation tests
at wire speed. It can also initiate Layer-3 SAT with its own
generator.
Within the Platinum package, MiNID enables smart packet
capturing remotely. It can transport classified traffic to any
standard Wireshark station for further analysis. For best
efficiency, MiNID can send truncated packets.
Digital Diagnostic Monitoring
Digital Diagnostics Monitoring (DDM) information read from an
SFP plugged into a MiNID is stored on the MiNID. This
information can be forwarded to the host and retrieved directly
from the device via a remote management system.

## MiNID  *(p.3)*

Microburst Monitoring
Within the Platinum package, MiNID offers the ability to monitor
network traffic, on a per-flow or multiple-flows basis, and detect
unexpected bursts of data in very short time intervals measured
in microseconds. It provides clear indication of traffic and bursts
passed, dropped, or exceeding thresholds based on CIR/CBS and
EIR/EBS. In addition, it helps facilitate bandwidth on demand.
Auto Responder
MiNID can automatically detect and respond to L2, L3, L4
loopbacks and OAM traffic with minimal installation effort and
no configuration. The auto-responder mode is transparent to
user traffic and provides a smooth introduction of service
visibility into the network.

## MANAGEMENT AND SECURITY  *(p.3)*

Management Options
MiNID can be managed via the following interfaces:
- Web-based and menu-driven interface in English and Chinese
- Command Line Interface (CLI) via secured Telnet (SSH)
- SNMPv2
- Inband management (VLAN-based)
- Out-of-band management and software configuration from
any Ethernet port in the host device
MiNID supports secure management using TACACS+ (client
authentication, authorization, and accounting).
MiNID is equipped with two MAC addresses; one for
management and one for services. This enables the device to
work and be managed in a Layer-2 untagged environment, as
well as VLAN and double VLAN-tagged.
MiNID acquires Time of Day through NTP.
Access Control List (ACL)
The ACL enables permission/denial of management access to
specified IP addresses for increased security.
Application software can be downloaded to MiNID via the
following:
- SFTP or TFTP for remote software download
- SFP-CA.2 unit, using YMODEM protocol for the SFP sleeve
option
- Serial interface for the standalone option
Zero Touch Provisioning
Host IP address and configuration files can be automatically
obtained using standard DHCP client functionality.
Loaned IP
MiNID can be managed without a dedicated IP address, by
loaning the IP address of the hosting device.
Network Management with RADview
RADview manages MiNID, and the RADview PM portal provides
SLA reports based on PM counters and utilization
measurements.
**MiNID Specifications CAPACITY**
Max. Frame
Size
12,000 bytes

## ETHERNET INTERFACES  *(p.4)*

SFP Sleeve
SFP-based, MSA-compliant edge connectors,
100BASE-FX/1000BASE-FX
SFP Transceivers
for MiNID SFP
Electrical: 100BASE-T/1000BASE-T
Optical: Dual/single, multi-mode/single mode
fiber:
FE: 100BASE-FX/LX/BX
GbE: 1000BASE-SX/LX/ZX/BX and CWDM
Standalone
Two SFPs/Copper/Combo ports: 100/1000BASE-
T, 100BASE-FX, or 1000BASE-FX

## DIAGNOSTICS  *(p.4)*

Syslog
Loopback Tests
Intrusive and non-intrusive L2/L3/L4 loopbacks,
with optional MAC, IP, and UDP port swap per
flow
Service
Activation Tests
RFC-2544 responder
ITU-T Y.1564 responder
L3 SAT generator

## GENERAL  *(p.4)*

Compliance
IEEE 802.3, MEF CE 2.0
Power Consumption
SFP Sleeve
1.2W without SFP
1.65W (including standard 10km SFP)
Standalone
max 3.75W
Physical
SFP sleeve
MiNID SFP
Standalone
Height
12.7 mm (0.50 in)
12.7 mm (0.50 in)
30 mm (1.18 in)
Width
14.3 mm (0.56 in)
14.3 mm (0.56 in)
113 mm (4.45 in)
Depth
81.1 mm (3.19 in)
81.1 mm (3.19 in)
113 mm (4.45 in)
Weight
30.0 g (1.0 oz)
40.0 g (1.4 oz)
0.3 kg (0.66 lb)
Environment
Case/Ambient
Temperature
SFP sleeve, MiNID SFP: -40 to 85°C (-40 to 185°F)
Standalone: 0 to 50°C (32 to 122°F)
Storage
Temperature
-40 to 85°C (-40 to 185°F)
Humidity
Up to 90%, non-condensing
Note: Reaching the operating temperature of
-20/-40 to 65°C (-4/-40 to 149°F) requires the use of industrial SFPs.

## MiNID  *(p.5)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel 972-3-6458181 | Fax 972-3-7604732
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
679-100-11/22 (2.3) Specifications are subject to change without prior notice. © 1988–2022 RAD Data Communications Ltd. This product is protected by patents, see
ipr.rad.com. The RAD name, logo, logotype, and the product names Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data
Communications Ltd.. All other trademarks are the property of their respective holders.

## Ordering  *(p.5)*

The information below represents examples of supported
configurations. For additional configuration options, please
contact your local RAD partner.
Hardware:
MiNID/SLV/GE
MiNID/SFP/5DH/GE
MiNID/SFP/6DH/GE
MiNID/STU/GE/ACEX/CMB
MiNID/STU/GE/ACEX/BPS/UTP
MiNID/STU/GE/ACEX/CMB/SYE
MiNID/STU/GE/ACEX/BPS/CMB
Software:
MiNID-SW/DEMARC
MiNID-SW/PLATINUM
Note: Order a hardware and a software option.

## ORDERING OPTIONS  *(p.5)*

Some options are not supported by all models. Some option
combinations are invalid or may require a minimum order. To
determine the BOM for your application, please contact your
local RAD partner.
Bypass Relay
Default
No bypass relay
BPS
Bypass relay
Enclosure
SLV
SFP sleeve enclosure
SFP
SFP enclosure
STU
Standalone enclosure
Ethernet Ports CMB
2 combo Ethernet ports
UTP
2 RJ-45 Ethernet ports
Fiber Type
5DH
850 nm, 300m (984ft) 62.5/125
multimode, 550m (1804ft) 50/125
multimode
6DH
1310 nm, 10km (6.2mi) 62.5/125 single
mode
Power Supply
ACEX
External 100-240 VAC power supply
(mandatory for standalone versions)
Sync-E
Default
No Sync-E
SYE
Sync-E
Software:
MiNID-SW/DEMARC
Service demarcation application software
MiNID-SW/PLATINUM
Platinum application software, includes demarcation application
software and additional features
Note: Order a hardware and a software option.
**SPECIAL CONFIGURATIONS**
Please contact your local RAD partner for configuration options.
**SUPPLIED ACCESSORIES**
P/S-AC/5/2000/UNIVERSAL-W/LOCK
External AC power supply for MiNID standalone AC ordering
options

## OPTIONAL ACCESSORIES  *(p.5)*

CBL-MUSB-DB9F
Mini-USB cable to connect MiNID standalone to a serial port
SFP-CA.2
Adapter to connect MiNID to a PC (when ordered, comes with
the PS and cable listed below)
PS-AC/5/1200/GND
Power Supply for SFP-CA.2 (can be also ordered separately)
CBL-USB-A-B
Communication cable for SFP-CA.2