# MiCLK 1588 Grandmaster on an SFP with Built-in GNSS

<!-- datasheet product=miclk family=- kind=system source=miclk_2_3_ga_ds.pdf -->

*Datasheet `miclk_2_3_ga_ds.pdf`, 5 pages. Product `miclk`, no inventory family (system).
*Note: standalone SFP product; no chassis banner and no inventory family yet*

## MiCLK 1588 Grandmaster on an SFP with Built-in GNSS  *(p.1)*

- Fully-featured Primary Reference Time Clock (PRTC) and
IEEE 1588-2008 (PTP) Grandmaster
- Built-in GNSS receiver
- Miniature, pluggable device fits in any MSA-Compliant
1G SFP port
- Ideal for 4G/5G small cell deployments
- Cost-effective upgrade solution for 3G/4G/5G networks
MiCLK® offers a pluggable, easy-to-replace, cost-effective
migration path for providing robust synchronization near the
network edge. It enables flexible deployment and easy
integration into existing networks. The cutting-edge embedded
GNSS receiver features excellent time accuracy even under
challenging deployment scenarios, such as building walls and
urban canyons that are typical for small-cell installations. Design
and timing redundancy techniques provide resiliency against
local GNSS outage.
MiCLK supports both Layer-2 and Layer-3 PTP distribution in
unicast and multicast modes.

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

Deployment scenarios include mobile networks, such as LTE and
LTE-A, with a particular focus on small cell applications.
Furthermore, support of simultaneous L2/L3 PTP distribution
also provides a cost-effective upgrade solution for legacy
networks, by supporting SDH replacement scenarios.
MiCLK’s deployment location is versatile. Due to its pluggability
and cost-effectiveness, MiCLK can be placed close to base
stations in order to reduce packet delay variation and
asymmetry. Furthermore, MiCLK saves CAPEX by adding timing
capabilities to existing aggregation points, servicing dozens of
base stations.

## TIMING AND SYNCHRONIZATION  *(p.1)*

MiCLK incorporates RAD’s advanced SyncTop synchronization
and timing over packet feature set to support mobile
heterogeneous network (HetNet) topology.
The device combines Synchronous Ethernet (SyncE) with
IEEE 1588v2 Precision Time Protocol per ITU-T G.8265.1,
G.8275.1, and G.8275.2 Telecom profiles for cost-effective
synchronization of frequency and phase.
With an integrated GNSS receiver and 1588v2 Grandmaster
support, MiCLK offers a Distributed GMTM solution, allowing
mobile operators and service providers to cost-effectively
provide reliable frequency and phase accuracy for LTE-A.
The device also supports 1588v2 ordinary clock (OC), boundary
clock (BC), and transparent clock (TC), as well as a dual master
operating simultaneously in G.8265.1 and G.8275.1 modes.

## FULL-FEATURED PTP GRANDMASTER  *(p.1)*

MiCLK distributes frequency and time simultaneously, according
to both ITU-T G.8265.1 (IP/unicast) and ITU-T G.8275.1
(L2/multicast), and G.8275.2 (IP/unicast) PTP telecom profiles.
This is especially effective in hybrid cellular environments that
comprise co-located 3G/4G/5G base station technologies. When
working in ITU-T G.8265.1 or G.8275.2 mode, MiCLK supports up
to 128 simultaneous slaves (symmetric 128 packets/second).

## PRIMARY REFERENCE TIME CLOCK  *(p.1)*

MiCLK is used as an ITU-T G.8272 Primary Reference Time Clock
(PRTC), providing information on GNSS time and frequency
information to the network, by supplying a Sync-E distribution
chain (Sync-E Ethernet SSM messages) and using its 1-PPS
external interface output.

## RESILIENCY  *(p.1)*

To achieve network-wide resiliency, operators may allow two or
more PTP flows to reach every slave (base station), as it is the
slave who selects the best master available.
One option is to install two or more MiCLK units in
geographically separated network elements located in the same
backhaul network section.
Alternatively, two MiCLK units can be plugged into the same
router/switch (connected to the same GNSS antenna via a
standard passive RF splitter).
Operators may choose a combination of both resiliency types.
MiCLK supports multiple GNSS backup schemes. If the underlying
network already supports Sync-E, MiCLK exploits the incoming
Sync-E reference to maintain its accurate time during a GNSS
outage.

## MiCLK  *(p.2)*

Another resiliency option is the Assisted Partial Timing Support
(APTS). MiCLK simultaneously functions as a Grandmaster (GM)
and a slave of 1588. The slave inside MiCLK synchronizes to an
incoming PTP stream received from the central GM. During a
GNSS outage, MiCLK recovers the frequency from the central GM
to maintain its accurate time.
**Specifications CAPACITY**
Master
Capacity
128 slaves (Symmetric 128 packets/sec)

## INTERFACES  *(p.2)*

PTP/Sync-E/
MGMT
GE PTP/Sync-E/MGMT input/output and
management over SFP or SFP+ 1000BASE-X (MSA
compliant)
GNSS
L1 GNSS input port, COAX DIN 1.0/2.3(F) screw-
locking connector, 50 Ohm
1PPS/CLK
1-PPS output over COAX DIN 1.0/2.3(F) screw-
locking connector (50 Ohm)

## MANAGEMENT  *(p.2)*

Multilevel User
Access
up to 4 sessions
Dedicated IP
address/subnet
IPv4, IPv6
VLAN 802.1Q
Saving User
Default
Configuration
Zero Touch
DHCP
DHCP client
Protocols
Remote SW upgrade via SFTP or TFTP
DSCP
Configuration
Options
Graphical web interface
Remote CLI (Telnet/SSH)

## MiCLK TIMING  *(p.3)*

PTP
Full featured IEEE 1588-2008 Grandmaster
1-step clock supported as slave
1-step clock supported as master
ITU-T G.8265.1 or 8275.2 (IP/unicast) Telecom
profile frequency and time distribution (IPv4, IPv6)
ITU-T G.8275.1 (Eth/multicast) Telecom profile
frequency and time distribution
APTS opposite G.8275.2 GM over UDP/IP
PTP/Sync-E hybrid (Sync-E for frequency and PTP for
time)
VLAN 802.1Q
BC (Boundary clock)
DSCP configuration for PTP (G.8265.1 and G.8275.2)
packets
Synchronous
Ethernet
(Sync-E)
Sync-E Primary Reference Clock (PRC) output with
Ethernet SSM according to G.8262 and G.8264 (with
GNSS)
Sync-E reference input (with Ethernet SSM
handling) for GNSS backup
Internal
Oscillator
Stratum 3E OCXO (complies with MTIE under
variable temperature defined in G.8263)
Time Accuracy Normal GNSS operation: Time error <UTC +/-
100nsec and MTIE<100nsec according to ITU-T
G.8272 and ITU-T G.8273.1
Sync-E based GNSS backup
APTS based GNSS backup: Time error complies with
test cases defined in G.8261
Holdover time w/o any inputs: Time error < UTC +/-
1.5 µsec for at least 2 hours
Frequency
Accuracy
Compliant with G.811 PRC requirements (during
both GNSS normal and backup operation)
GNSS Receiver 72-channel multi-GNSS receiver engine
Dual frequency GNSS
GPS L1C/A /QZSS L1 C/A
SBAS L1 C/A: WAAS, EGNOS, MSAS
GLONASS L1OF (L1 band)
3.3 VDC antenna voltage supply

## SECURITY  *(p.3)*

ACL
ACL security for management
TACACS+
TACACS+ Authentication, Authorization and
Accounting
Figure 1. Timing and Synchronization with MiCLK
**MiCLK DIAGNOSTICS**
Performance
Monitoring
for timing
Syslog
Indicators
GNSS operation status LED
General fault indication LED

## GENERAL  *(p.4)*

Environment
Operating Case
Temperature
-20 to 85°C (-4 to 185°F)
Relative Humidity Up to 95%
Figure 2. Outdoor Antenna Installation

## MiCLK  *(p.5)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel/Fax 972-52-4748272 | Fax 972-3-6498250
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
593-100-10/25 (2.3) Specifications are subject to change without prior notice. © 1988–2026 RAD Data Communications Ltd. This product is protected by patents, see
ipr.rad.com. The RAD name, logo, logotype, and the product names Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data
Communications Ltd.. All other trademarks are the property of their respective holders.
Power
Power Supply Receives power from its host device.
Power
Consumption <1.65W
Physical
Height
12.4 mm (0.488 in)
Width
14.0 mm (0.55 in)
Depth
79.0 mm (3.11 in)
Extending
from chassis: 31.0 mm (1.22 in)
**Ordering**
Legend
MiCLK/#
#
Maximum number of slaves
8S
8 slaves
24S
24 slaves
64S
64 slaves
128S
128 slaves
**RECOMMENDED CONFIGURATIONS**
MICLK/8S
MICLK/24S
MICLK/64S
MICLK/128S

## OPTIONAL ACCESSORIES  *(p.5)*

CBL-SMA/F-1023/M/PROT
SMA/Female to DIN 1.0/2.3 internal adaptor cable, 1m (3.2 ft),
with integrated low level, 500V surge protector, connecting
MiCLK with LMR-400 cable (required for minimum installation).
Can be ordered separately or as part of the MICLK-GNSS-ANT-KIT
kit.
CBL-TNC/F-1023/M/PROT
TNC/Female to DIN 1.0/2.3 internal adaptor cable, 1m (3.2 ft),
with integrated low level, 500V surge protector, connecting
MiCLK with LMR-400 cable (required for minimum installation).
CBL-MINIBNC-BNC/F
Adaptor cable (75 Ohm) to connect MiCLK’s 1PPS/CLK connector
to external equipment
MICLK-LIGHTARR-KIT/10M
GNSS lightning arrestor kit for MiCLK, including a lightning
arrestor and 10m (32.8ft) outdoor cable with male TNC
connectors on both sides
MICLK-GNSS-ANT-KIT/$
GNSS antenna kit including roof antenna with mounting kit,
SMA/Female to DIN 1.0/2.3 cable and outdoor RF cable. Order
this kit if your application requires antenna and long cabling.
The kit includes the following:
- CBL-SMA/F-1023/M/PROT cable (see above)
- CBL-GSU-INT-20M/60M/120M – LMR-400 cable
20m/60m/120m long, connecting the adaptor cable to the
lightning protection kit or antenna
- GPS antenna (PCTEL), 40 dB gain, with pipe mount adaptor –
T-GPS-8178D-HR-DH-W-TAD
- General antenna mounting hardware kit, including a pipe
adapter and an L-shaped stainless steel bracket mount –
MMK1925
Note: MICLK-GNSS-ANT-KIT/$ kit does not include the lighting protector
which is part of MICLK-LIGHTARR-KIT/10M kit (see below).
Legend
MICLK-GNSS-ANT-KIT/$
$
LMR-400 cable length
20M
20m (65.6 ft)
60M
60m (196.85 ft)
120M
120m (393.7 ft)
SFP-CA.2
Adapter to connect MiCLK to a PC