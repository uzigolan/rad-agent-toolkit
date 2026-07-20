# ETX-2v Open uCPE White Box Platforms

<!-- datasheet product=etx-2v family=etx2v kind=system source=etx-2v_ds.pdf -->

*Datasheet `etx-2v_ds.pdf`, 4 pages. Product `etx-2v`, family `etx2v` (system).

## ETX-2v Open uCPE White Box Platforms  *(p.1)*

- Versatile suite of carrier-grade white boxes, supporting
wide range of business customers and scenarios with
different VNF based applications, suitable for uCPE,
pCPE or “bare-metal” deployments
- Flexible network connectivity options
- Flexible design allows matching configuration to any
network needs
ETX-2v is an x86-based open platform, which can host virtual
functions (VFs) and applications. It is optimized for use with
RAD’s vCPE-OS or pCPE-OS (a carrier-grade operating system for
network edge virtualization with optimized data plane), or any
other third-party operating system.
RAD’s vCPE-OS combines powerful networking capabilities with
virtualization for hosting SD-WAN and any other value-added
virtual network function (VNF) applications from any vendor (see
separate documentation on vCPE-OS).

## ARCHITECTURE  *(p.1)*

ETX-2v family is very flexible in HW networking connectivity,
which include RJ-45 10/100/1000BaseTx, SFP, SFP+, QSFP+,
QSFP28, PoE, WiFi, LTE, VDSL, and pluggable RAD Smart SFPs.
ETX-2v family addresses different site requirements in terms of
hosted applications, network connectivity and needed
performance by using appropriate CPU and memory size. The
basic differentiation is by defining the platform type matching
site size, such as “Small” or “Medium”.
For the “Small” site the most appropriate platform option is
ETX-2V-CA/AC/2CMB/4U/DY, where “D” defines the CPU type
which is ATOM C3000 series (Denverton) with Y=2 or 4, defining
the number of cores. The number of cores is important to
understand how many VNFs (if needed) it is possible to run on
this platform. This platform uplinks are 1G with 2 COMBO ports
(“2CMB”). The unit has desktop form factor with external AC-DC
adapter.
For the “Medium” site the most appropriate platform option is
ETX-2V-CA/AC/2SP/6U/DY, where “D” defines the CPU type
which is ATOM C3000 series (Denverton) with Y=4 to 16, defining
the number of cores. This platform uplinks are 1G/10G with 2
SFP+ ports (“2SP”). 6 RJ-45 ports are available with an option to
have PoE+ on two of them. In some cases, especially with the 16
cores option, this platform can also support relatively “large”
sites with multiple VNFs (distributed scheme). The unit is
desktop form format with external AC-DC adapter. Dual
redundant power supplies are also available as ordering option.
Both the “Small” and “Medium” site platforms have options for
integrated Wi-Fi, LTE or VDSL.

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

For business service applications,  ETX-2v fits centralized,
decentralized, or a mix of both implementation modes.
In centralized deployments,  ETX-2v acts as a “pCPE” by
decoupling the operating system networking and NFVI
capabilities.
In decentralized deployments, ETX-2v functions as a “uCPE”
(universal CPE), hosting an array of VNFs (see separate
documentation on vCPE-OS).

## ETX-2v Specifications MAIN CHARACTERISTICS  *(p.2)*

See Table 1 (according to Ordering Options)
Table 1. ETX-2v Platforms Ordering Options and Specifications
Specification
Small site
Medium site
Ordering
ETX-2V-CA/AC/2CMB/4U/D
ETX-2V-CA/AC/2SP/6U/D
CPU
Intel ATOM
2 Core – C3338
4 Core – C3558
Intel ATOM
8 Core – C3758
4 Core – C3558
16 Core – C3958
Memory
DDR4 SO-DIMM, ECC support
Max. capacity: 16 GB (single slot)
2x DDR4 SO-DIMM, ECC support
Max. capacity: 32 GB (2 slots)
Networking
(Ethernet)
2 x 1 GbE Copper/SFP Combo WAN ports
4 x RJ-45 10/100/1000 Mbps Ethernet ports (4x LAN chip
Intel i211)
2x 10 GbE SFP+ WAN ports
2x RJ-45 10/100/1000 Mbps ports
4x RJ-45 10/100/1000 Mbps ports via Intel i350
VDSL (Optional)
No
Yes
PoE+ (Optional)
No
Yes
Wifi/LTE (Optional) Yes
Yes
System Health
Monitoring
(Optional)
No
IPMI
Trust Platform
Module (TPM)
Yes
Yes
Peripheral I/O
1 x Console RJ-45
2x USB 3.0
1 x Console RJ-45
1x micro USB
2x USB 2.0
Storage
MLC SSD From 64GB to 1TB size
MLC SSD From 64GB to 1TB size
Power Supply
External AC power adapter: 100~240V, 1.5A, 50-60Hz, to
12V
External AC power adapter: 100~240V, 1.5A, 50-60Hz, to 12V
Dimensions
Height: 44 mm (1.73”)
Width: 231.6 mm (9.12” )
Depth: 174.6 mm (6.87”)
Height: 44 mm (1.73”)
Width: 248.4 mm (9.8“)
Depth: 251.5 mm (9.9“)
Operating
Environment
0°C to 40°C (32 to 104°F)
10 to 90% RH
0 to 40°C (32 to 104°F),
20 to 90% RH
Storage
Environment
-20°C to 70°C (-4 to 158°F),
5 to 95% RH@55°C
-10 to 70°C (14 to 158°F),
5 to 95% RH @ 55°C
Weight
2.5 kg (4.5 lb)
3.2 kg (5.8 lb)
Certifications
CE, FCC, UL
CE, FCC, UL

## ETX-2v OPTIONAL INTERFACES  *(p.3)*

VDSL Port
Compliance
G.inp, G.vector and PhyR
ITU-TG.992.5, ITU-T G.992.3, ITU-T G.992.1.
ANSI T1.413 issue 2. AnnexM
G.992.5(ADSL2+) ,G.992.3(ADSL2), G.DMT
(mainly France)
G.993.2 (supporting profile 8a, 8b, 8d, 12a,
12b, 17a)
G.Fast 212a, vDSL.2, 35b
Data Rate
G.992.5(ADSL2+):
Downstream: 24Mbps, Upstream: 1.3 Mbps
G.992.3(ADSL2):
Downstream: 12Mbps, Upstream 1.3Mbps
G.DMT:
Downstream: 8Mbps, Upstream: 832Kbps
Impulse
Overvoltage
Protection
6 kV with K.21 enhanced
Wifi Module
Output power
(per chain)
Dual band
2.4GHz: max 21dBm
5GHz max 20dBm
Compliance
IEEE 802.11ac
Backward compatible with 802.11a/b/g/n
Supports IEEE 802.11d, e, h, i, k, r, v time
stamp, and w standards
2x2 MIMO
Up to 867Mbps
DFS
Supports Dynamic Frequency Selection
LTE module
Any ETX-2v-CA device can be ordered with /LE or /LA LTE option
RF bands
See Table 2. F=FDD; T= TDD
Data rates,
downlink (Cat 6)
FDD: 300 Mbps
TDD: 222 Mbps
Data Rates, uplink
(Cat 6)
FDD: 50 Mbps
TDD: 26 Mbps
Table 2. Supported RF Bands for LTE
1 2 3
39 40
APAC Bands (LA)
F
F
F
F
F
F
F
F
F
T
T
T
T
EU/USA Bands (LE)
F
F
F
F
F
F
F
F
F
F
F
F
F
F
T
Figure 1. vCPE Business Services

## ETX-2v  *(p.4)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel/Fax 972-52-4748272 | Fax 972-3-6498250
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
691-150-03/26 (2.0) Specifications are subject to change without prior notice. © 2018–2026 RAD Data Communications Ltd. The RAD name, logo, logotype, and the product
names Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their
respective holders.

## Ordering  *(p.4)*

The information below represents examples of supported
configurations. For additional configuration options, please
contact your local RAD partner.
ETX-2V-CA/AC/VD/2SP/6U/D4C/64S/8R/LE
ETX-2V-CA/AC/2SP/6U/D8C/128S/8R/LA
ETX-2V-CA/AC/2SP/6U/D16C/256S/32R
ETX-2V-CA/ACEXR/2SP/6U/D16C/256S/32R
ETX-2V-CA/AC/2CMB/4U/D4C/128S/8R

## ORDERING OPTIONS  *(p.4)*

Some options are not supported by all models. Some option
combinations are invalid or may require a minimum order. To
determine the BOM for your application, please contact your
local RAD partner.
Power
AC
AC-DC External adaptor for ETX-2V-CA
Supply
ACEXR
AC-DC External dual adaptors for ETX-2V-CA
VDSL Port VD
VDSL WAN interface for ETX-2V-CA medium
size platform
WAN Port 2CMB
2 GE Combo ports
2S
2 SFP Ethernet ports
2SP
2 SFP+ Ethernet ports
LAN Port
2P
2 10/100/1000BaseT PoE ports
4P
4 10/100/1000BaseT PoE ports
2U
2 Ethernet UTP ports
4U
4 Ethernet UTP ports
6U
6 Ethernet UTP ports
8U
8 Ethernet UTP ports
10U
10 Ethernet UTP ports
12U
12 Ethernet UTP ports
Expansion M2
2 Expansion slots
M4
4 Expansion slots
CPU
D4C
4 Cores DNV CPU
D8C
8 Cores DNV CPU
Hard
64S
64 GB MLC SSD
Drive
128S
128 GB MLC SSD
256S
256 GB MLC SSD
512S
512 GB MLC SSD
1000S
1000 GB MLC SSD
RAM
4R
4 GB RAM
8R
8 GB RAM
16R
16 GB RAM
32R
32 GB RAM
64R
64 GB RAM
128R
128 GB RAM
Interface
Type
LA
LTE with APAC (Asia) bands
LE
LTE with EU/USA bands
Wifi
W
Wifi module
**SUPPLIED ACCESSORIES**
AC/DC power adaptor for ETX-2V-CA

## OPTIONAL ACCESSORIES  *(p.4)*

VCPE-OS
Carrier-grade operating system for virtualization
CBL-SGW-RJ45-D9-F-6FT
RJ-45 to DB-9 cable for connecting to terminal
CBL-ETX-2V-CA/OPEN/2M
Cable for connecting ETX-2V-CA to DC power source with locking
connector on one side and open 2 wires on the other, 2m long
Mounting Kits
RM-ETX-2V-CA/AC/2CMB/4U
19" Rack mount Kit for ETX-2V-CA/AC/2CMB/4U
RM-ETX-2V-CA/AC/2SP/6U
19" Rack mount Kit for ETX-2V-CA/AC/2SP/6U