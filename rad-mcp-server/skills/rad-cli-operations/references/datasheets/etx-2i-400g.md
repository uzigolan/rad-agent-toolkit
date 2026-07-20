# ETX-2i-400G High-Density 400G Demarcation & Aggregation Platform

<!-- datasheet product=etx-2i-400g family=etx2 kind=system source=etx-2i-400g_ds_03-26_ca_0.pdf -->

*Datasheet `etx-2i-400g_ds_03-26_ca_0.pdf`, 5 pages. Product `etx-2i-400g`, family `etx2` (system).
*Note: Controlled Availability datasheet (03-26)*

## ETX-2i-400G High‑Density 400G Demarcation & Aggregation Platform  *(p.1)*

- 400G Ethernet demarcation and aggregation device
designed to deliver SLA‑based, high‑performance
networking services for massive data transfer across
data centers, clouds and enterprise sites
- High‑scale aggregation of multiple 100GbE services into
a single 400G uplink
- Line rate MACsec* with Quantum Key Distribution
(QKD) and Post Quantum Cryptography (PQC) readiness
- Compact 1RU form factor with low power consumption
- Carrier‑grade resiliency, OAM, and SLA assurance
capabilities.
Today’s AI driven world requires massive bandwidth, low latency
and high security.
ETX-2i-400G is a high density, carrier grade demarcation and
aggregation platform designed to address the bandwidth,
latency, and security requirements of AI driven networks.
Optimized for 400G Ethernet environments, the system
consolidates multiple lower speed services into a single 400G
uplink, reducing network complexity, footprint, and power
consumption.
Built on RAD’s proven ETX-2i platform, the ETX-2i-400G delivers
advanced traffic management, security enhancement, post-
quantum data cryptography-readiness, together with
comprehensive service assurance in a compact 1RU form factor.
ETX-2i-400G provides MEF 10.3 color-aware and unaware
policers, delivering high-scale multi-CoS services with
hierarchical Quality of Service (HQoS). It supports advanced
scheduling, WRED per CoS, shaping per EVC and per port, with
flexible classification rules and access lists.
ETX-2i-400G can be configured to forward or discard Layer-2
control frames (including other vendors’ L2CP frames).

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

Cloud migration, storage replication, disaster recovery, hybrid
cloud architectures, and multi-site business applications -
continue to fuel the need for high capacity, low latency
connectivity, in addition to recent years of even higher
bandwidth requirements for AI training and AI inferring. Suitable
for massive east–west traffic is generated as organizations train
models, and operationalize distributed inference across
enterprise sites, data centers and clouds. The ETX-2i-400G is
engineered to meet the ultra-high capacity, low latency, and
security demands of modern data center interconnect. It delivers
assured performance with advanced traffic management,
hierarchical QoS, readiness for line rate MACsec encryption, and
a quantum safe security framework, supporting massive data
transfer across data centers, clouds and enterprise sites.
The ETX 2i 400G incorporates a comprehensive set of Carrier
Ethernet service tools, making it ideal for carriers, service
providers, municipalities, wholesale providers, and mobile
operators. It supports unified, SLA based Ethernet business
services including E Line, E LAN, and E Tree service models
certified to MEF 3.0 and CE 2.0.
ETX-2i-400G enables operators to deliver service level
guarantees, by supporting multi-layer diagnostics, fine-grained
SLA enforcement, and accurate performance monitoring. Built-in
service activation testers verify end-to-end network
performance.

## INTEROPERABILITY  *(p.1)*

ETX-2i-400G features and services are standard-based and
should work with any 3rd party equipment using standard based
features and services.

## NETWORK TOPOLOGIES  *(p.1)*

The ETX 2i 400G supports multiple network topologies, including
linear, daisy chain, and self-healing ring architectures
(G.8032v2). It interoperates with any standard compliant
Ethernet device to enable flexible network design. s.

## SERVICES  *(p.1)*

ETX-400G delivers services of up to 400 GbE using a mix of
400GbE and 100GbE interfaces, supporting CE 2.0/MEF 3.0
compliant service models.

## RESILIENCY  *(p.1)*

ETX 2i 400G provides fast protection against network failures
across linear, ring, and dual homing topologies. Supported
mechanisms include IEEE 802.3ad link aggregation, G.8032v2
Ethernet ring protection, and G.8031 Ethernet linear protection,
ensuring sub 50 ms service restoration.

## ETX-2i-400G MONITORING AND DIAGNOSTICS  *(p.2)*

The system features multi-layer OAM and performance
monitoring tools implemented in hardware for scale and
accuracy. Supported capabilities include IEEE 802.1ag, IEEE
802.3ah, TWAMP Light, ICMP Echo, Y.1564, and RFC2544 service
activation testing, enabling rapid fault isolation and SLA
verification.

## MANAGEMENT AND CONTROL  *(p.2)*

ETX-2i-400G runs RAD’s carrier-grade operating system,
providing a consistent provisioning and maintenance experience
across the ETX-2/2i family. Management options include
RADview NMS, SNMP-based systems, CLI access, and
NETCONF/YANG for SDN orchestration.
The platform supports Zero Touch provisioning for secure,
automated onboarding and service deployment.

## Specifications ETHERNET INTERFACE PORTS  *(p.2)*

400G-2QDD-4QSFP
2 QSFP-DD 400GbE
4 QSFP28 100GbE
Note: It is strongly recommended to order this device with original RAD
transceivers. RAD cannot guarantee full compliance to product
specifications for units using non-RAD transceivers. For full details on
SFP/SFP+/QSFP28/QSFP+ transceivers, see the Pluggable Transceivers
data sheet.

## BRIDGE  *(p.2)*

Compliance
802.1D, 802.1Q, 802.1ad
Frame Size
(max)
9600 bytes
Mode
VLAN-aware, VLAN-unaware
VLAN Editing
Inner/outer VLAN editing per VLAN and p-bit
values
ETX-2i-400G Demarcation and Aggregation
Pre-aggregation
Wholesale
Network
100G to 400G
Agg/Preaggregation
towards the PE
Multi-tenant NTE deployment,
NNI (1:1)x400G
Wholesale service with service
assurance
UNI aggregation to 400G
400G
100/400G
HQ/DC/Large Branch
L2 + L3
Services
HQ or DC  Interconnect
Service or Service aggregation
opposite remote branches
MTU Site
ETX
400G
100G
Service Assurance
vice Assurance
Central NTE
400G

## ETX-2i-400G NETWORKING CAPABILITIES  *(p.3)*

Flow
Classification
Rules
Outer VLAN or outer + inner VLAN
PCP
TOS/DSCP
EtherType
IP/MAC source/destination address
Layer-2
Forwarding
Jumbo frame support
Policing
Color aware/unaware dual token bucket with
user-configurable CIR + CBS and EIR + EBS
2-rate/3-color policing per EVC.CoS
Bandwidth policing per MEF 10.3
Hierarchical envelope policer per MEF 10.3
MultiCoS EVCs per MEF 10.3
Handle elephant flows through a ‘fat‑pipe
detection’ mechanism
Scheduling
8 × CoS per EVC scheduling elements
Strict Priority (SP) and Weighted Fair Queue (WFQ)
Services
Ethernet E-LAN, E-Line, E-Tree
MEF CE2.0 compliant
Layer-2 services with available bandwidth
Shaping
Per port
Per EVC
Per EVC.CoS

## DIAGNOSTICS  *(p.3)*

Connectivity Fault
Management (CFM)
Per IEEE 802.1ag
Counters
RMON2 port-level counters
Delay and Loss
Measurements
Per MEF 36
EFM Link-fault OAM
Per IEEE 802.3ah
ICMP Echo
Over L2 and L3 services
Tests IP connectivity (PING)
KPI Measurements
Accurate one-way KPI measurements
Limiting Multicast
Traffic Flooding
DHCP and MLDv2 snooping
Link-Level OAM
Per IEEE 802.3-2005
LLDP Discovery
Per IEEE 802.1AB
Loop Prevention
Using MSTP and RSTP
Loopback Tests
Non-disruptive loopback per flow, with
MAC/IP address swap
Loopbacks at Ethernet port level
On-demand Layer-2 and 3 loopbacks
Service Activation
Tests
RFC-2544: 8 built-in wirespeed testers
ITU-T Y.1564: 8 built-in wirespeed testers
Service Utilization and
Performance
Monitoring
Per ITU-T Y.1731.2012, including synthetic
loss measurement
TWAMP
RFC 5618 TWAMP responder and receiver
TWAMP sender
RFC 5357 TWAMP – Light generator and
responder (SW license)
ITU-T Y.1731 PM (SLM; DM)

## RESILIENCY  *(p.3)*

Dual Homing
Dual-homing link redundancy
Ethernet Path
Protection
G.8031 linear 1:1 protection
Ethernet Ring
G.8032v2 rings with sub 50 ms protection
for Ethernet traffic
Link Aggregation
Load balancing LAG with up to 4 ports in a
LAG group

## ETX-2i-400G MANAGEMENT AND SECURITY  *(p.4)*

Management
Options
Local management via LAN port or serial port
Remote management via in-band VLAN
Plug and Play
Zero Touch
Provisioning
DHCP auto-configuration
XML configuration files download via TFTP/SCP
Configuration backup and restore
Protocols and
Security
Password-protected access
Authorization levels
SSH (Secure CLI)
Telnet
SNMPv3
SFTP
NETCONF/YANG management interface
Dual Stack IPv4 and IPv6
RADIUS or TACACS+ authentication
Access Control List (ACL)
Control Port
Interface
V.24/RS-232 DCE
Connector
RJ-45
Format
Asynchronous
Data Rate
9.6, 19.2, or 115.2 kbps
Ethernet Management Port
Type
10/100BASE-T
Connector
RJ-45

## PHYSICAL  *(p.4)*

Height
44 mm (1.7 inch)
Width
440 mm (17.3 inch)
Depth
377.5 mm (14.2 inch)
Weight
7.35 kg (16.2 lb) – when using 2 power supplies
6.58 kg (14.5 lb) – when using 1 power supply

## ENVIRONMENTAL  *(p.4)*

Storage
Temperature
-40 to 85°C (-40 to 185°F)
Operating
Temperature
Regular: 0 to 50°C (32 to 122°F)
Humidity
5% to 90%, non-condensing
Fans
5+2 (simultaneous fan operation; automatic fan
level control)
Airflow
Front to back airflow

## POWER  *(p.4)*

Power Supply
Hot swappable, redundant AC and/or DC PS
AC: 100-240 VAC nominal (±10%),
2.5A/1A, 50/60 Hz
DC: 48 VDC (40-60 VDC),
5A
Power
Consumption
180-220W (max)
120-140W (average/typical)
110W (minimum)

## STANDARDS COMPLIANCE  *(p.4)*

CE
CE 2.0 / MEF 3.0
MEF 3.0
E-Access: Access EPL, Access EVPL
E-LAN: EP-LAN, EVP-LAN
E-LINE: EPL, EVPL
E-Tree: EP-Tree, EVP-Tree
MEF 6
E-Line: EPL and EVPL
E-LAN: EPLAN and EVPLAN
MEF
MEF 9, MEF10, MEF 14, MEF 20, MEF 36, MEF
IEEE
802.3, 802.3u, 802.1D, 802.1Q, 802.1p, 802.3ad,
802.3-2005, 802.1ax, 802.1ag
ITU-T
Y.1731, G.8031, G.8262, G.8265, RFC-2544,
Y.1564

## ETX-2i-400G  *(p.5)*

24 Raoul Wallenberg St., Tel Aviv 6971920, Israel
Tel/Fax 972-52-4748272 | Fax 972-3-6498250
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
547-103-03/26 (6.8.5) Specifications are subject to change without prior notice. © 1988–2026 RAD Data Communications Ltd. RAD products/technologies are protected by
registered patents. To review specifically which product is covered by which patent, please see ipr.rad.com. The RAD name, logo, logotype, and the product names MiNID,
Optimux, Airmux, IPmux, and MiCLK are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.

## Ordering  *(p.5)*

The information below represents the currently supported
configurations. For additional configuration options, please
contact your local RAD partner.
**ETX-2i-400G HARDWARE**
ETX-2i-400G/ACR/2QDD/4Q (2 QSFP-DD 400G, 4 QSFP28 100G)
ETX-2i-400G/DCR/2QDD/4Q (2 QSFP-DD 400G, 4 QSFP28 100G)

## SUPPLIED ACCESSORIES  *(p.5)*

AC power cord (for AC models)
DC power cord (for DC models)
RM-50/19
HW kit for mounting ETX-2i-400G in a 19-inch rack (flat
installation)

## OPTIONAL ACCESSORIES  *(p.5)*

ETX-2i-400G-PS/AC
ETX-2i-400G-PS/DC
RM-50/19/A
Mounting kit for ETX-2i-400G 100mm deep installation on
19-inch rack, this RM can be used for flat installation too
RM-50/23
Hardware kit for mounting ETX-2i-400G into a 23-inch rack
RM-50/23F
Hardware kit for mounting ETX-2i-400G into a 23-inch frame