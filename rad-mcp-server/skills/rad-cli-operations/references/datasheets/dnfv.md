# D-NFV / D-NFV-L Virtualization Modules

<!-- datasheet product=dnfv family=mp4100 kind=card source=dnfv_dnfv-l.ds_.pdf -->

*Datasheet `dnfv_dnfv-l.ds_.pdf`, 2 pages. Product `dnfv`, family `mp4100` (card).

## Megaplex-4 D-NFV Virtualization Modules  *(p.1)*

- Distributed network functions virtualization (DNFV) for rapid rollout of new services,
network capabilities and functions.
- Integration of higher-level applications (firewall, encryption, SCADA etc) with a
communication platform in a single device
- Reduced number of physical network devices for better reliability and simpler
operation
- x86 Quad/Dual cores engine
- Reduced customer site equipment footprint, less power consumption
The D-NFV modules add to Megaplex-4 a
built-in standard Intel x86 core that hosts
virtual machines providing virtual network
functions (VFs) or value-added service
capabilities. This new capability provides a
quick and easy way to introduce new
services and applications with the benefit
of function localization at the customer
premises. For U&T the modules provide a
way to implement new functionalities and
applications into the multiservice platform
and to integrate OT and IT equipment into
one chassis.  They also provide an easy way
to cope with new regulatory requirements
(such as NERC-CIP).
The modules are available in two flavors:
-
DNFV: x86-based virtualization I/O
module, Intel I7 core processor
-
DNFV-L: x86-based virtualization I/O
module, Intel Atom® processor C2000
(formerly Rangeley).
The modules occupy two module slots in
the Megaplex-4 chassis. They are based on
a Main board and a Carrier board. The
Carrier board (X86 piggy) interfaces the
Main board and carries a compact COM
Express module.
The carrier board includes the following:
-
DNFV: 4 FE ports, local USB and UART
Control ports, 8 GB RAM, an SSD
memory connected via mSATA
interface and one external GBE
Ethernet port terminated with a UTP
connector.
-
DNFV-L: local USB and UART Control
ports, 4 GB RAM, an SSD memory
connected via M.2 interface.
In the basic application, the D-NFV
modules accommodate virtual functions
(VF), such as MPLS switch, CES processor,
router, firewall, encryption engine or
traffic monitor.
SONET/SDH
PSN
TP
IED
CCTV
Voice
Megaplex-4
with Firewall and
Encryption
.
Figure 1. DNFV Accommodating VF Functions
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
Order this publication by Catalog No. 805071
464-113-01/18  Specifications are subject to change without prior notice.  1988–2018 RAD Data Communications Ltd. RAD products/technologies are protected by registered patents. To review specifically which
product is covered by which patent, please see ipr.rad.com. The RAD name, logo, logotype, and the product names MiNID, Optimux, Airmux, IPmux, and MiCLK are registered trademarks of RAD Data Communications
Ltd. All other trademarks are the property of their respective holders.

## D-NFV Specifications  *(p.2)*

ETHERNET INTERFACE (DNFV ONLY)
Fast Ethernet Interfaces
Number of Ports: 4
Data Rate: 10/100 Mbps
Type: 10/100BASE-T,
full-duplex, autonegotiation
Maximum Frame Size: 9600 bytes
Connectors: Shielded RJ-45
GbE Interface
Number of Ports: 1
Type: 10/100/1000BASE-T,
full-duplex, autonegotiation
Maximum Frame Size: 9600 bytes
Connectors (per port): RJ-45, shielded
CONTROL PORT
Interface: RS-232, UART
Baud Rate: 115200 bps
Connector: RJ-45
USB PORT
Type: USB2
Max Feeding Power: 2.5W
Voltage: 5 VDC
Max current: 0.5A
Note: This port will be used in future versions and
is currently for factory use only.
DNFV OS
Linux OS + KVM Hypervisor
DNFV: Linux Ubuntu distribution version
14.04.3 LTS
DNFV-L: Linux Ubuntu distribution version
16.04.3 LTS
OpenStack ComputeNode
RADview D-NFV orchestrator or customer
OpenStack controller
GENERAL
Processor
DNFV: i7 x86 engine with 4 cores
(Intel® Core™ i7-4700EQ)
DNFV-L: C2358 x86 engine with 2 cores
(Intel Atom® Processor C2358)
RAM
DNFV: 8 GB
DNFV-L: 4 GB
Hard Drive
SSD-based storage, 128 GB
LED Indicators
RDY (green): Initialization of COM Express
is finished and x86 processor is up and
running
LINK (green) – per port (DNFV only):
-
On: the port is connected to an active
Ethernet hub or switch
-
Off: Ethernet link is not detected
ACT (yellow) – per port (DNFV only):
-
On or Blinking (in accordance with the
traffic): ETH frames are received or
transmitted
-
Off: ETH frames are not received and
transmitted
Power Consumption
DNFV: 35W max (at CPU operating
frequency 1 GHz)
DNFV-L: 35W max (at CPU operating
frequency 1.7GHz)
Environment
Operating temperature:
-10°C to 55°C (14°F to 131°F)
Storage temperature: -20°C to 70°C (-4°F
to 158°F)
Humidity: up to 95%, non-condensing

## Ordering  *(p.2)*

RECOMMENDED CONFIGURATIONS
MP-4100M-DNFV/I7/128S/GBEUTP
DNFV: x86-based virtualization I/O module,
Intel I7 core processor
MP-4100M-DNFV/R2C/128S/4R
DNFV-L: x86-based virtualization I/O
module, Intel Atom® processor C2000
(formerly Rangeley)
The module must be ordered
together with a RADcare Package and
RADcare Project Assurance Package.
.