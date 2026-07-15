# 1 Introduction

*Manual `ETX-2V-CA_AC_2CMB_4U_D_mn.pdf`, pages 31–36.*


## 1.1 Processor and Chipset Overview  *(p.31)*


## 1.2 System Hardware Specification  *(p.31)*

ETX-2v-CA is an x86-based open platform, which can host virtual functions (VFs) and applications. It is 
optimized for use with RAD’s vCPE-OS or pCPE-OS (a carrier-grade operating system for network edge 
virtualization with optimized data plane), or any other third-party operating system.  
RAD’s vCPE-OS includes a standard KVM hypervisor to host third-party applications (VFs) or integrate 
opposite third-party service orchestrators (see separate documentation on vCPE-OS). 
ETX-2v-CA platforms can also use third party Operation systems, like SDWAN application to run as bare 
metal or as VNF over vCPE-OS. Please confirm interoperability with third party OS vendor in case of 
“bare metal” project. 
1.1 Processor and Chipset Overview 
Built upon the functionality and the capability of the Intel® Atom™ Processor C3000 SoC processors, 
ETX-2v-CA provides the performance and feature required for one processor based workstation 
platform. 
1.2 System Hardware Specification 
Platform 
Intel® Atom™ Processor 2core-C3338/4core-C3558 SOC (codenamed “Denverton”) 
BIOS 
AMI BIOS 
System Memory 
Socket: 1 x 260-pin SO-DIMM 
Technology: Single Channel DDR4 1866 SO-DIMM (Support ECC/Non-ECC) 
Max. Capacity: 16GB 
ETX-2V-CA/AC/2CMB 
1. Introduction 
Networking 
Ethernet Ports & Controllers: 
2x Intel X553 RJ45/SFP GbE port with auto media detection (combo ports) 
4x Intel I211 RJ45 GbE port with optional 2 segment gen 3.4 bypass 
Bypass: 1-pairs Generation 3.4 
Expansion 
1 x M.2 A + E Key Connector w/PCI-E signals) 
1 x M.2 B Key Connector for LTE module (Sierra EM7455/7430), with SIM holder. Please see 
available LTE bands in a separate section  
There are two types of LTE options differentiated by geographical (available bands) location. 
The table below (Supported RF Bands) lists the available bands on each option (“LE” or “LA” 
PN suffix). 
Storage 
1 x SATA 3.0 Connector 
1 x mini mSATA 3.0 Connector 
Standard options – 128G, 256G and 512G 
I/O Interface 
DC Jack 
Power on/off button 
F/D button 
1 x RJ-45 console 
2 x USB 3.0 
Supplied Accessories  AC/DC power adaptor  
Optional Accessories 
CBL-SGW-RJ45-D9-F-6FT – RJ-45 to DB-9 cable for connecting to terminal  
RM-ETX-2V-CA/AC/2CMB/4U – 19" Rack mount Kit 
System Cooling 
Fanless 
OS Support 
Linux 
Power 
External 40W Power Adapter with AC INPUT: 100~240V, 1.5A, 50-60Hz to 12vDC 
Operating 
Environment 
0°C to 40°C, 10 to 90% RH 
Storage Environment -20°C to 70°C, 5 to 95% RH@55°C 
Chassis Color 
Standard Pantone Black-C 
Dimensions 
231.6(W) x 174.6(D) x 44 (H) mm 
Certification 
CE/FCC/UL 
 
ETX-2V-CA/AC/2CMB 
1. Introduction 
 
 
Supported RF Bands  
 
1 2 3 4 
5 7 8 12 13 18 19 
20 
21 
25 
26 
28 
29 
30 
38 
39 40 
41 
APAC Bands (LA) 
F  
F  
F F F  
 
F 
F 
 
F 
 
 
F 
 
 
T 
T 
T 
T 
EU/USA Bands (LE) F F F F 
F F F F 
F 
 
 
F 
 
F 
F 
 
F 
F 
 
 
 
T 

## 1.3 System Block Diagram  *(p.34)*


## 1.4 Physical Description  *(p.34)*

ETX-2V-CA/AC/2CMB 
1. Introduction 
 
1.3 System Block Diagram 
 
1.4 Physical Description 
The figures below shows the ETX-2v-CA/AC/2CMB device. 
 

## 1.5 Description of LEDs  *(p.35)*

ETX-2V-CA/AC/2CMB 
1. Introduction 
 
 
1.5 Description of LEDs 
Bypass LED x2 
Color 
Bypass 0 Status 
(Lower LED) 
Bypass 1 Status 
(Upper LED) 
Green 
Normal Mode 
Normal Mode 
Red 
Bypass Mode 
Bypass Mode 
LAN0~LAN3 LED x2  
Color 
ACT/Link Status 
(Lower LED) 
Color 
Speed Status 
(Upper LED) 
Green 
ACT/Link 
Green 
100M 
ETX-2V-CA/AC/2CMB 
1. Introduction 
Color 
ACT/Link Status 
(Lower LED) 
Color 
Speed Status 
(Upper LED) 
Off 
No Link 
Orange 
1G 
Power & HDD Access LED x2 
Color 
Power Status 
(Lower LED) 
Color 
HDD Access Status 
(Upper LED) 
Green 
System Power On 
Blue 
Data Access 
LTE RSSI LED x4  
Color 
LTE RSSI Status (1x4 LED) 
Green 
LTE RSSI 
Red 
SFP/LAN P0~P1 LED x2 (SFP Only 1000BASE-X) 
Color 
ACT/Link Status 
(Lower LED) 
Color 
Speed Status 
(Upper LED) 
Green 
ACT/Link 
Green 
100M 
Off 
No Link 
Orange 
1G 
WiFi Link & Backup LED x2 
Color 
WiFi Link Status  
(Lower LED) 
Color 
Back Up Status 
(Upper LED) 
Green 
WiFi 
Orange 
Back up 
 