# 14 M-ETH, T3, Teleprotection and VC Modules

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 1089–1185.*


## (chapter introduction)  *(p.1089)*

Modules 
This chapter describes the main features, applications and installation procedures for the the following 
I/O modules operating in the Megaplex-4 chassis with CLI management:  
Module  
Description 
M-ETH 
Module with 8 GbE interfaces supporting optical or electrical media and providing 9 
Gbps switching capacity (up to 1 Gbps capacity to the CL.2 module and 8 Gbps shared 
among its 8 external ports). The capacity can be allocated among the 8 interfaces with a 
granularity of 100 Kbps. 
T3 
Single-port multiplexer module, providing access to standard T3 equipment over 
unbalanced copper lines with full duplex data rates of 44.7 Mbps.   
TP (Tele-
protection) 
Command In/Out teleprotection module with four selectable voltage inputs and eight 
outputs, secured and reliable end-to-end commands transmission. 
VC-16, 
VC-8, 
VC-4, 
VC-8A, 
VC-4A 
 
Analog voice modules VC-16, VC-8 and VC-4 provide 16, 8 or 4 PCM-encoded toll-quality 
voice channels.  
The modules are available in three models: 
• E&M: 4-wire or 2-wire interfaces with E&M signaling per RS-464 Types I, II, III and V, 
and BT SSDC5  
• FXS: 2-wire interfaces for direct connection to telephone sets 
• FXO: 2-wire interfaces for direct connection to PBX extension lines. 
VC-8A and VC-4A are similar to VC-8 and VC-4 modules, except that they also support 
ADPCM. 

## 14.1 M-ETH  *(p.1090)*

14. M-ETH, T3, Teleprotection and VC Modules 
14.1 M-ETH  
This section describes the technical characteristics, applications, installation and operation of the 
dedicated 8 GbE-port M-ETH module for the use in the  
Megaplex-4 Next Generation Multiservice Access Nodes, ver 4.0 and higher.  
Applications  
Typical M-ETH applications are shown in the figures below. 
SDH/SONET
Ring
PSN
STM-4/OC-12
GbE
Megaplex-4100/4104
E&M
V.35/449
FXS
Low Speed
Data
RTU
Teleprotection
G.8032
Ring
Megaplex/ETX
Megaplex/ETX
G.8032
Ring
Megaplex/ETX
Megaplex/ETX
ETH
Up to 5 Rings
ETH
ETH
ETH
Megaplex/ETX
Megaplex/ETX
Megaplex/ETX
Megaplex/ETX
 
Access and Aggregation with Multiple Ethernet Rings 
14. M-ETH, T3, Teleprotection and VC Modules 
SDH/SONET
Ring
PSN
PBX
Router
FXS
ETH RTU
STM-1/OC-3
STM-4/OC-12
GbE
Server
Video 
Camera
PC
Megaplex-4100
ETH
ETH
ETH
ETH
ETH
Substation/Train Station/Control Tower
 
 Aggregating Multiple Ethernet Devices 
Product Options   
The module has two assembly options – with 8 copper (UTP) or 8 SFP ports.  
An IEEE-1613 compliant option of the M-ETH module can be ordered from RAD. For more information, 
contact your local Business Partner.  
Features 
M-ETH Bridge 
Each M-ETH module features a single bridge including 9 bridge ports: 8 external and 1 internal. The 
bridge ports can be used as part of the local bridge in the module or as end points of a flow. 
The module bridge supports both VLAN-aware and VLAN-unaware functionalities. The bridge port can 
be configured as a member in VLAN table or just be member of unaware bridge. 
The architecture of Megaplex-4 bridges (CL and M-ETH) and an example of the data flow is illustrated in 
the figure below. The diagram shows the CL.2 bridge #1 (always aware) and two bridge instances (#4 
and #7) implemented in two M-ETH modules. 
14. M-ETH, T3, Teleprotection and VC Modules 
M-ETH in slot #1
Bridge#1 Aware
BP 1 8
BP 1 9
ERP#2
E
W
BP 4 2
BP 4 1
Eth 1 2
Eth 1 1
ERP#3
E
W
Bridge #4
BP 4 3
GbE cl-a 1
GbE cl-b 1
mng-eth 
cl-a
SVI#1
10
BP 1 7
BP 1 1
Router
RI#1
Eth 1 3
2
BP 1 2
Bind
Flow
BP 1 4
GbE cl-a 2
L. MAC
BP 1 5
BP 1 5
MNG flow pop/push, bi-
directional flow in all 
CL.2 assemblies
M-ETH in slot #2
BP 7 8
BP 7 5
Eth 2 2
eth 2 1
Bridge #7
BP 7 1
BP 1 3
3
6
1
Eth 2 8
5
mng-eth 
cl-b
BP 1 6
12
4
RI#2
RI#3
DTS
PPP
DCC
PPP
 
Megaplex-4 Bridges  
Bridge #4 defined on the M-ETH module in slot 1 has one internal bridge port (4 3) and two external 
bridge ports (4 1 and 4 2) participating in an ERP ring: 
• 
External port 4 1 is bound to M-ETH port 1/1 and serves as a West port in ERP Ring 3. 
• 
External port 4 2 is bound to M-ETH port 1/2 and serves as an East port in ERP Ring 3. 
• 
Internal port 4 3 is connected to GbE port 2 of CL-A module (via Flow 6) and to Bridge port 1 2 of 
CL module Bridge 1 (via Flow 2). 
Bridge #7 defined on the M-ETH module in slot 2 has two external bridge ports (7 5 and 7 8): 
• 
External port 7 5 is bound to M-ETH port 2/1  
• 
External port 7 8 is bound to M-ETH port 2/2  
14. M-ETH, T3, Teleprotection and VC Modules 
For examples on configuring M-ETH bridges, see Configuring Bridges in Chapter 8. No direct connection 
can be done between two bridges of different M-ETH modules (see dotted lines in the diagram); this 
connection must be done via the CL ports. 
In a CL.2/DS0 assembly option only unaware flow between ports are supported.  
The bridge functionality is used to allow forwarding traffic between more than two ports or in case MNG 
VLAN is used. When ports are working in E-line mode, no management traffic can be passed between 
the ports.  
Management 
All operating parameters of the M-ETH module are soft-selectable via the management system. 
Physical Description  
The M-ETH module occupies one I/O slot in the Megaplex-4 chassis. The module panels are shown 
below.  
 
14. M-ETH, T3, Teleprotection and VC Modules 
 
 
Module with UTP 
Connectors 
Module with SFP 
Connectors 
 M-ETH/UTP and M-ETH/SFP Module Panels  
LED Indicators 
The table below explains the functions of the indicators located on the module panel. 
  M-ETH Indicators  
Indicator 
Color 
Description 
LINK  
Green 
On: the port is connected to an active Ethernet 
hub or switch 
Off: Ethernet link is not detected 
ACT  
Yellow 
On or Blinking (in accordance with the traffic): 
ETH frames are received or transmitted 
Off: ETH frames are not received and transmitted  
14. M-ETH, T3, Teleprotection and VC Modules 
Technical Specifications 
GbE Ports 
Number of Ports  
• 8 
 
External Ports  
In accordance with order: 
• 8 GbE ports with SFP modules  
• 8 GbE ports with copper (RJ-45) interfaces  
 
Maximum Frame Size  
9600 bytes  
Copper Ports 
Interface Type  
10/100/1000BASE-T, full- or half-duplex, with 
autonegotiation   
 
Connectors (per port) 
RJ-45, shielded 
Optical GbE Ports   
Interface Type  
100/1000BASE-X, full-duplex  
Link Connectors 
SFP-based (see the SFP/XFP Transceivers data sheet on 
www.rad.com)  
Note. SGMIII interface (SFP-30) 
is not supported.  
Bridges 
Number of bridge ports 
8 external  
1 internal 
 
Mode 
VLAN-aware  
VLAN-unaware  
Protection 
 
ERP 
Indicators 
 
LINK (green) 
On: the port is connected to an active Ethernet hub or 
switch 
Off: Ethernet link is not detected 
 
 
ACT (yellow) 
On or Blinking (in accordance with the traffic): ETH 
frames are received or transmitted 
Off: ETH frames are not received and transmitted  
Power Consumption 
 
10W max (excluding SFPs) 
Configuration 
 
Programmable via Megaplex-4 management system  
Environment 
 
Storage temperature  
-20°C to 70°C (-4°F to 158°F) 
 
Humidity 
Up to 95%, non-condensing 
 
Operating temperature 
-10°C to 55°C (14°F to 131°F) 
14. M-ETH, T3, Teleprotection and VC Modules 
Preparing the Module for Installation 
 
Warning 
Before performing any internal settings, adjustment, maintenance, or 
repairs, first disconnect all the cables from the module, and then remove the 
module from the Megaplex-4 enclosure. 
No internal settings, adjustment, maintenance, and repairs may be 
performed by either the operator or the user; such activities may be 
performed only by a skilled technician who is aware of the hazards involved. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. 
 
Caution 
The modules contain components sensitive to electrostatic discharge (ESD). 
To prevent ESD damage, always hold the module by its sides, and do not 
touch the module components or connectors.  
 
Caution 
To prevent physical damage to the electronic components assembled on the 
two sides of the module printed circuit boards (PCB) while it is inserted into 
its chassis slot, support the module while sliding it into position and make 
sure that its components do not touch the chassis structure, nor other 
modules.  
M-ETH modules may be installed in an operating chassis (hot insertion). 
Note 
M-ETH software can be updated by downloading from the CL module. 
Therefore, if the M-ETH module is not yet loaded with the required software 
version, refer to Chapter 12 for detailed software downloading instructions.  
Before installing M-ETH modules, it may be necessary to install, or replace, SFPs: 
• 
To install an SFP, use the procedure prescribed in Installing an SFP below. 
• 
SFPs may be replaced using the procedure given in Replacing an SFP below.  
M-ETH modules equipped with RAD-supplied SFP plug-in modules comply with laser product performance 
standards set by government agencies for Class 1 laser products. The modules do not emit hazardous light, 
and the beam is totally enclosed during all operating modes of customer operation and maintenance.  
 
14. M-ETH, T3, Teleprotection and VC Modules 
 
Warning 
Third-party SFP optical transceivers may be also used, provided they are 
approved by an internationally recognized regulatory agency, and comply 
with the national laser safety regulations for Class 1 laser equipment. 
However, RAD strongly recommends ordering RAD SFPs, as this permits full 
performance testing of the supplied equipment.  
M-ETH modules are shipped with protective covers installed on all the optical connectors. Keep the 
covers for reuse, to reinstall the cover over the optical connector as soon as the optical cable is 
disconnected.  
 
Warning 
SFPs installed on M-ETH modules may be equipped with a laser diode. In 
such cases, a label with the laser class and other warnings as applicable will 
be attached near the SFP socket. The laser warning symbol may be also 
attached.  
For your safety: 
• 
Before turning on the equipment, make sure that the fiber optic cable is 
intact and is connected to the optical transmitter. 
• 
Do not use broken or unterminated fiber-optic cables/connectors. 
• 
Do not look straight at the laser beam, and do not look directly into the 
optical connectors while the module is operating.  
• 
Do not attempt to adjust the laser drive current. 
• 
The use of optical instruments with this product will increase eye 
hazard. Laser power up to 1 mW could be collected by an optical 
instrument. 
• 
Use of controls or adjustment or performing procedures other than 
those specified herein may result in hazardous radiation exposure.  
ATTENTION:  The laser beam may be invisible!  
 
Caution 
When calculating optical link budget, always take into account adverse 
effects of  temperature changes, optical power degradation and so on. To 
compensate for the signal loss, leave a 3 dB margin. For example, instead of 
the maximum receiver sensitivity of -28 dBm, consider the sensitivity 
measured at the Rx side to be -25 dBm. Information about Rx sensitivity of 
fiber optic interfaces is available in SFP/XFP Transceivers data sheet.  
 
14. M-ETH, T3, Teleprotection and VC Modules 
Installing an SFP  
 
Warning 
When installing an optical SFP in an operating module, be aware that it may 
immediately start generating laser radiation.  
 
Caution 
During the installation of an SFP with optical interfaces, make sure that all 
the optical connectors are closed by protective caps. 
Do not remove the covers until you are ready to connect optical fibers to the 
connectors.  
 
Note 
The following procedures all have illustrations showing typical SFPs with 
optical interfaces. Your SFPs may look different.  
 To install the SFP: 
Lock the latch wire of the SFP module by lifting it up until it clicks into place, 
as illustrated in the figure below.  
Note 
Some SFP models have a plastic door instead of a latch wire. 
 
 Locking the Latch Wire of a Typical SFP 
Carefully remove the dust covers from the corresponding SFP socket of the M-ETH module, and from the 
SFP electrical connector. 
Orient the SFP as shown in the figure, and then insert the rear end of the SFP into the module socket. 
Slowly push in the SFP to mate the connectors, until the SFP clicks into place. If you feel resistance 
before the connectors are fully mated, retract the SFP using the latch wire as a pulling handle, and then 
repeat the procedure. 
If necessary, repeat the procedure for the other SFP. 
14. M-ETH, T3, Teleprotection and VC Modules 
Replacing an SFP  
SFPs can be hot-swapped. It is always recommended to coordinate SFP replacement with the system 
administrator. Note that during the replacement of SFPs, only the traffic on the affected optical link is 
disrupted (the other optical link can continue to carry traffic). 
 To replace an SFP: 
If necessary, disconnect any cables connected to the SFP connectors. 
Push down the SFP locking wire, and then pull the SFP out. 
Reinstall protective covers on the SFP electrical and optical connectors. 
Install the replacement SFP as described above. 
Installing a Module in the Chassis 
M-ETH modules may be installed in an operating chassis (hot insertion). 
 
Warning 
The M-ETH module starts operating as soon as it is inserted in an operating 
chassis.  
 To install an M-ETH module: 
3. Refer to the system installation plan and identify the prescribed module slot. 
Check that the fastening screws at the module sides are free to move. 
4. Insert the module in its chassis slot and slide it in as far as possible. 
5. Secure the module by tightening its two fastening screws. 
The module starts operating as soon as it is plugged into an operating enclosure. At this stage, 
ignore the alarm indications. 
Configuration Sequence 
The list of tasks that can be performed on the M-ETH modules and the recommended configuration 
sequence are described in the table below. For detailed descriptions, refer to Chapter 5. The second 

## 14.2 T3  *(p.1100)*

14. M-ETH, T3, Teleprotection and VC Modules 
column indicates the configuration context for this task. The third column refers to the reference tables 
and relevant sections that should be consulted when planning the module operation. 
Task 
Configuration Context 
Comments and References 
Configuring an M-ETH module 
and putting it into service 
configure>slot>card-type  
card-type=ethernet m8eth 
Configuring the Ethernet ports 
configure>port>ethernet 
User Ethernet Ports in Chapter 5 
Configuring the module bridge 
ports 
configure>bridge 
Bridge in Chapter 8 
Configuring ingress and egress 
flows on the M-ETH Ethernet 
ports  
configure>flows 
 
 
Configuring ERP protection 
configure>protection>erp 
 
14.2 T3  
This section describes the technical characteristics, applications, installation and operation of the T3 I/O 
module for use in the Megaplex-4 Next Generation Multiservice Access Node, ver 4.5 and higher. Up to 
10 modules can be installed in a single Megaplex-4100 chassis, and up to 4 modules in a single 
Megaplex-4104 chassis. 
Note 
In the Megaplex-4100 systems equipped with VS or T3 modules there might be 
a limitation for 9 such modules in the chassis. The remaining slot can be used 
for any other I/O module. For the conditions of this limitation, refer to Table 1-
1 in Chapter 1.  
 
Applications  
The figure below shows a campus application with multiservice aggregation over T3. 
14. M-ETH, T3, Teleprotection and VC Modules 
POP
PBX
Megaplex-4
RTU
RS-232
T3
Radio
Radio
T3
T3
SONET
OC-12
T3
Megaplex-4
PBX
T3
Megaplex-4
PBX
 
Multiservice Aggregation over T3 for Campus Application 
Features  
Ports 
The module architecture and data flow is shown below. The table lists the T3 module entities (ports) and 
their hierarchy.  
  T3 Module Architecture Entities and their Hierarchy  
Name 
Number of 
Ports  
Possible Values 
Remarks 
T3 
1 
slot/1  
 
T1 
28 
slot/1/1 .. slot/1/28 
 
Logical MAC  
16 
slot/1 .. slot/16 
 
GFP  
16 
slot/1 .. slot/16 
 
VCG 
16 
slot/1 .. slot/16 
 
14. M-ETH, T3, Teleprotection and VC Modules 
Ethernet over T3 
The following figure shows the relationship between the entities involved in the Ethernet over T3/T1 
functionality.  
 
DS0/1
24*E1
CL.2 DS0/1
Cross connect
GbE
L. MAC 1..16
GFP 1..16
1:1
1:1
1:1..16
1:1
VCG 1..16
Switch
CL.2 Ethernet 
Engine
T1 
1/ 1..28
T3
 
Logical Entities Representing Ethernet Traffic over T3 Media  
• 
T3 modules allow encapsulating Ethernet traffic with the GFP protocol and transferring it over 
T3 or T1 media. In both cases Ethernet ports are connected to Logical MAC ports via flows, and 
these Logical MAC ports are bound to GFP ports. Starting from the GFP ports, two ways are 
available: 
• 
To transfer Ethernet over T3, only one GFP/Logical MAC port is created and T3 port is bound 
directly to it. 
• 
To transfer Ethernet over T1, up to 16 Logical MAC, GFP and VCG ports are created, so that the 
VCG ports are bound to GFP ports and VCG ports are bound to Logical MAC ports. Up to 16 T1 
ports can be bound to each VCG ports, but the total T1 number is limited by 28 T1 ports per T3 
module. 
14. M-ETH, T3, Teleprotection and VC Modules 
Cross-Connections 
The T3 modules support both DS0 and TDM cross-connections, selectable at the level of the individual 
T1 port: 
• 
ds0 cross-connect –used when necessary to control the routing of individual timeslots, and 
therefore relevant only when using a framed mode. The DS0 cross-connect enables connecting 
payload between E1 to T1 ports.   
• 
tdm cross-connect mode  – used when necessary to transparently transfer the entire stream to 
a selected destination port using the unframed mode.  
Protection  
The external T3 ports of the T3 module feature TDM group protection (see TDM Group Protection in 
Chapter 7). Once this type of protection is configured for the T3 port, the following occurs: 
• 
TDM group protection is also automatically configured on all the open internal T1 ports 
belonging to this T3 module. The two T1 members belonging to such a group have the same 
tributary numbers.  
• 
Ethernet group protection is automatically configured on all the open Logical MAC ports 
belonging to this T3 module. The two members belonging to such a group have the same port 
numbers.  
The numbers of such TDM protection/Ethernet protection groups start from 200.  
You can also configure TDM group protection on individual selected T1 ports or logical MAC ports if their 
T3 ports are not configured to protection.  
Timing  
T3 modules recover the timing of each received T1 or T3 stream, and therefore can also provide timing 
reference signals derived from a selected T1 or T3 stream for the nodal Megaplex-4 timing subsystem. 
The module transmit timing can be locked to the Megaplex-4 nodal timing.  
Management 
All operating parameters of T3 module are soft-selectable via the management system. The operating 
mode of each channel is independently selectable. 
14. M-ETH, T3, Teleprotection and VC Modules 
Physical Description  
The T3 module occupies one I/O slot in the Megaplex-4 chassis. The module panel shown in the figure 
below includes two BNC connectors, designated as follows: 
• 
TX – serves as the DS3 transmit (output) connector 
• 
RX – serves as the DS3 receive (input) connector. 
 
 
T3 Module Panel  
LED Indicators 
The functions of the module indicators are as follows: 
14. M-ETH, T3, Teleprotection and VC Modules 
T3 Module Indicators 
Indicator 
Number 
Color 
Description 
SYNC  
1  
Green/Red 
Lights in green when the port is active and operating 
properly 
Lights in red when the port is active and detects a LOS, 
LOF or AIS alarm indication 
Off: not active or not connected 
REM SYNC 
1 
Yellow 
Lights when the port detects loss of remote 
synchronization. 
Technical Specifications 
General 
Function 
DS3 multiplexer  
 
External Ports 
Single T3 port 
 
Internal Ports 
28 internal T1 ports  
T3 Port  
Data Rate 
44.736 Mbps 
Applicable Standards 
Bellcore TR-NWT-000499, GR-253-CORE, ANSI T1.102, 
and ITU-T Rec. G.703 
Framing Options  
• C-bit parity per ANSI T1.107 and ANSI T1.107a 
• Synchronous M13 (SYNTRAN) per ANSI T1.107 and 
ANSI T1.107a 
• Unframed (will be supported in the next version) 
 
Line Code 
B3ZS  
 
Line Impedance 
75Ω 
 
Pulse Shape 
Per ANSI T1.102 
 
Connectors 
Two BNC female connectors  
Internal T1 Ports 
 
Applicable Standards 
AT&T TR-62411, ANSI T1.403, and ITU-T Rec. G.704 
Framing Options 
D4 (SF), ESF, unframed 
 
Nominal Data Rate 
1.544 Mbps 
Timing  
 
System clock source 
• T3 port 
• Any T1 port (when working with CL modules that 
have no SDH/SONET ports)  
14. M-ETH, T3, Teleprotection and VC Modules 
Indicators 
SYNC (green/red) 
Lights in green when the port is active and operating 
properly 
Lights in red when the port is active and detects a LOS, 
LOF or AIS alarm indication 
Off: not active or not connected 
 
REM SYNC (yellow) 
Lights when the port detects loss of remote 
synchronization 
Diagnostics 
Local and remote loopbacks 
T3 ports: per port 
T1 ports: per port and per 
timeslot 
 
Performance Monitoring 
RFC-3896 
Power Consumption 
 
10.4W Max.  
 
Environment 
Operating temperature 
Storage temperature 
Humidity: 
-10°C to 55°C (14°F to 131°F)  
-20°C to +70°C (-4°F to +160°F)  
Up to 95%, non-condensing   
Configuration 
Programmable via Megaplex system management 
 
Preparing the Modules for Installation 
 
Warning 
Before performing any internal settings, adjustment, maintenance, or 
repairs, first disconnect all the cables from the module, and then remove the 
module from the Megaplex-4 enclosure. 
No internal settings, adjustment, maintenance, and repairs may be 
performed by either the operator or the user; such activities may be 
performed only by a skilled technician who is aware of the hazards involved. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. 
 
Caution 
The modules contain components sensitive to electrostatic discharge (ESD). 
To prevent ESD damage, always hold the module by its sides, and do not 
touch the module components or connectors.  
14. M-ETH, T3, Teleprotection and VC Modules 
 
Caution 
To prevent physical damage to the electronic components assembled on the 
two sides of the module printed circuit boards (PCB) while it is inserted into 
its chassis slot, support the module while sliding it into position and make 
sure that its components do not touch the chassis structure, nor other 
modules.  
 
Installing a Module in the Chassis 
The modules may be installed in an operating chassis (hot insertion). 
 
Warning 
The module starts operating as soon as it is inserted in an operating chassis.  
 
 To install a T3 module: 
1. Refer to the system installation plan and identify the prescribed module slot. 
2. Check that the fastening screws at the module sides are free to move. 
3. Insert the module in its chassis slot and slide it in as far as possible. 
4. Secure the module by tightening its two fastening screws. 
The module starts operating as soon as it is plugged into an operating enclosure. At this stage, 
ignore the alarm indications. 
Normal Indications  
Once the equipment connected to T3 ports is operational, the following indications appear for normal 
operation: 
• 
The SYNC indicator lights steadily in green 
• 
The REM SYNC indicator is off.  
14. M-ETH, T3, Teleprotection and VC Modules 
Connecting to Remote Equipment 
5. Identify the cable(s) intended for connection to this module.  
6. Connect the cable(s) to the appropriate connector(s). Pay attention to correct connection:  
• 
Transmit cable - to the TX connector. 
• 
Receive cable - to the RX connector. 
Configuration Considerations 
T3 Module Capacity and Cross-Connect Constraints in Megaplex-4 
This section describes some capacity constraints of T3 modules with different Common Logic options as 
well as looking at specific applications of interest that have noteworthy constraints. 
CL.2 with no SDH/SONET Ports 
When using the CL.2 with no SDH/SONET ports, the TDM connection from the T3 I/O module to the 
backplane is via the TDM bus.  The TDM bus supports 16 T1s with CAS signaling support and 16 T1s 
without CAS signaling. Therefore voice services with signaling requirements are limited to maximum of 
16 T1s out the maximum of 28 T1s in a T3 link.  The remaining capacity of the T3 link can be used for 
service not in need of signaling support.  Examples include data service, always on audio like E&M 
without signaling, or T1s with out-of-band band signaling like PRI.  
CL.2 with SONET Assembly Ordering Option, DACS Application 
When using the CL.2 with the SONET ordering option for a DACS application, the signaling constraint 
described above is not applicable since the T3 module would now be using the PDH bus and not the 
TDM bus.  In an application for a DACS, the PDH bus offers system support for up to 120 E1/T1s 
including signaling support.  This would support a little more than 4 T3 modules per system (i.e., 120/28) 
with unconstrained full DS0 cross-connect support.  
 
CL.2 with SONET Assembly Ordering Option, SONET Mux Application with DS0 Grooming 
When using the CL.2 with the SONET ordering option and cross-connecting at the DS0 level to the 
internal T1 ports, another constraint comes into play.  The 120 E1/T1 DS0 cross-connect capacity of the 
PDH is still applicable. However, in addition to this, the T1 constraint is now present.  The T1’s are the 
14. M-ETH, T3, Teleprotection and VC Modules 
internal grooming entity to cross-connect at the DS0 level between I/O slots and the SONET uplink. 
There are 84 T1’s for SONET and this would become the limiting constraint in this application.  
CL.2 with SONET Assembly Ordering Option, SONET Mux Application 
When using the CL.2 with the SONET ordering option and cross connecting the T1’s inside the T3 link 
directly to a VT1.5 in a SONET uplink, the DS0 cross-connect limitations are not relevant.  In this case the 
constraint is imposed by the CL.2 end of the connection from the I/O interface.  Specifically, there is a 
capacity allocation per slot at the CL.2 of six TUG-2’s (24 T1’s). The CL.2 has three spare TUG-2’s that can 
be paired with the six TUG-2’s terminating the connection from any slot. Therefore, the system can 
support up to 3 full T3 modules by pairing the three spare TUG2’s with any three slots to provide the full 
seven TUG-2’s (28 T1’s) needed to terminate a full T3.  After three T3 modules, then only 24 T1’s can be 
supported per slot. 
Selecting a T3/T1 Port as System Timing Reference  
After an external T3 or internal T1 port of T3 module is configured and at no shutdown, its receive clock 
can be selected as a timing reference for the Megaplex-4 system. 
To modify the system timing reference with the supervision terminal, use the following commands at 
the config>system>clock>domain(1)# prompt: 
source <src-id> rx-port t3 <slot>/<port> 
source <src-id> rx-port t1 <slot>/<port>/<tributary> 
For detailed instructions, refer to Chapter 9. 
Note 
The T1 ports of T3 modules can serve as a clock source only when working 
with CL modules that do not have SDH/SONET ports.  
 
Configuration Sequence 
The list of tasks that can be performed on the T3 module and the recommended configuration sequence 
are described in the table below. For detailed descriptions, refer to Chapter 5. The second column 
indicates the configuration context for this task, under which it can be found in Chapter 5. The third 
column refers to the reference tables that should be consulted when planning the module operation. 
Task 
Configuration Context 
Reference  
Configure a module and put it into 
service 
configure>slot>card-type  
card-type=e3-t3 mt3 
14. M-ETH, T3, Teleprotection and VC Modules 
Task 
Configuration Context 
Reference  
Configure the T3 port parameters  
configure>port>t3 
T3 Ports in Chapter 5 
Configure the T1 port parameters  
configure>port>t1 
T1 Ports in Chapter 5 
Configure the VCG parameters and 
bind T1 ports to the VCG  
configure>port>vcg 
VCG Ports in Chapter 5 
Configure the GFP port parameters 
and bind T3 or VCG port to this GFP 
port 
configure>port>gfp 
GFP Ports in Chapter 5 
Configure the Logical MAC and bind 
GFP port to it 
configure>port>logical-mac 
Logical MAC Ports in Chapter 5 
Configure flows between the 
Logical MAC and Ethernet ports 
configure>flow 
Flows in Chapter 8 
Select a T3 or T1 Port as system 
timing reference  
config>system>clock>domain(1) 
Chapter 9 
Note: You must also configure the CL.2 or uplink module port parameters (depending on the T3 module 
application). For the uplink module configuration procedure, refer to the appropriate section of this Appendix.  
Configure timeslot assignment for  
internal T1 ports (DS0 cross-
connect for E1/T1 ports) 
configure>cr>ds0 
DS0 Cross-Connect in Chapter 8 
 
Cross-connect the full payload from 
the internal t1 port with another 
port of the same configuration and 
type (unframed) 
configure>cr>tdm   
TDM Cross-Connect in Chapter 8 
 
Configuration Example 
#=====================================# 
#      Configuring T3 module in SLOT 3   
#=====================================# 
configure slot 3 card-type e3-t3 mt3 
#======================================# 
#       Configuring T3 port 3/1  
#======================================# 
configure port t3 3/1 no shutdown 
#======================================# 
# Configuring T1 ports 3/1/1 and 3/1/2  
#======================================# 
 
configure port t1 3/1/1 no shutdown 
14. M-ETH, T3, Teleprotection and VC Modules 
configure port t1 3/1/2 no shutdown 
#================================================# 
# Configuring VCG port and binding T1 ports to it  
#================================================# 
 
configure port vcg 3/1 
no shutdown 
bind t1 3/1/1 
bind t1 3/1/2 
exit 
#================================================# 
# Configuring GFP port and binding VCG port to it  
#================================================# 
gfp 3/1 
no shutdown 
bind vcg 3/1 
exit 
#==================================================# 
# Configuring L.MAC port and binding GFP port to it  
#==================================================# 
logical-mac 3/1 
no shutdown 
bind gfp 3/1 
exit all 
 
 
#==================================================# 
# Configuring GBE port CL-A/1  
#==================================================# 
 
configure port ethernet cl-a/1 no shutdown 
#=============================================================# 
# Configuring flows between CL-A/1 and L.MAC port on T3 Module  
#=============================================================# 
configure 
flows  
classifier-profile v-1 match-all 
match vlan 1 
exit 
 
flow 1 
no shutdown 
classifier v-1 
egress-port ethernet cl-a/1 
ingress-port logical-mac 3/1 
exit 
 
flow 2 
no shutdown 
classifier v-1 
egress-port logical-mac 3/1 
ingress-port ethernet cl-a/1 

## 14.3 Teleprotection (TP)  *(p.1112)*

14. M-ETH, T3, Teleprotection and VC Modules 
exit all 
Monitoring and Diagnostics 
Diagnostics include local and remote loopbacks on the T3 ports (per port) and local and remote 
loopbacks on internal T1 ports (per port and per timeslot) (see T3 Ports and T1 Ports, respectively, in 
Chapter 5). 
For performance monitoring and statistics on the T3 ports, GFP ports, VCG Ports, Logical MAC Ports and 
internal T1 ports, see T3 Ports, GFP Ports, VCG Ports, Logical MAC Ports and T1 Ports, respectively, in 
Chapter 5.  
Troubleshooting  
If a problem occurs, check the displayed alarm messages and refer to Chapter 11 for their interpretation.  
14.3 Teleprotection (TP) 
This section describes the technical characteristics, applications, installation and operation of the TP 
distance teleprotection module for use in the Megaplex-4 Next Generation Multiservice Access Node, 
ver 3.3 and higher.  
Teleprotection Equipment is crucial for the overall protection of the Power Network. It plays a vital role 
in the fast isolation of faults on the network and prevents outages and blackouts. Isolation of the 
relevant segment from the network must be done as soon as possible to avoid domino effect.  At the 
second stage the relevant components in the network must be adjusted to work without the 
disconnected circuit.  
Megaplex-4 with its teleprotection modules delivers teleprotection commands and automation with 
mission-critical accuracy over dedicated fiber, TDM or IP, to help central control better manage the 
power grid load and to protect termination and transformation equipment from severe damages 
resulting from faulty high-voltage lines. 
Applications  
A typical point-to-point TP application: 
14. M-ETH, T3, Teleprotection and VC Modules 
TP
Teleprotection
Unit
Teleprotection
Unit
Teleprotection
Comm Channel
Substation
Teleprotection
Comm Channel
Substation
TP
PDH/SDH/SONET Network or Point-to-Point Dark Fiber
 
Point-to-Point TP Application 
The following figure shows a T-Line application, which allows broadcast of a trip event to several nodes 
via drop and insert on Trip level.  
 
Teleprotection
Unit
Teleprotection
Comm Channel
Substation
Teleprotection
Unit
Teleprotection
Comm Channel
Substation
Teleprotection
Unit
Teleprotection
Comm Channel
Substation
Teleprotection
Unit
Teleprotection
Comm Channel
Substation
 
T-Line Application 
In addition to the TDM capabilities, TP modules can perform encapsulation of Teleprotection commands 
into a PWE session over PSN. The direct encapsulation provides an effective way to keep the overall 
delay within the applications boundaries. The figure below shows a Megaplex solution for distant 
TPoPSN. 
Substation
Substation
GbE
Relay
PSN
Megaplex
Megaplex
GbE
Relay
 
TP over PSN 
14. M-ETH, T3, Teleprotection and VC Modules 
Product Options  
Output Relay 
Two relay types are available and can be selected in accordance with applications as ordering options: 
Electro-mechanical relay (EMR) and Solid-state relay (SSR). 
Nominal Input Control Voltage 
The nominal input control voltage can be ordered as follows: 
• 
110 VDC 
• 
220 VDC  
• 
Soft-selectable nominal input control voltage, selectable per port: ±24, ±48, ±110, ±125, ±220 or 
±250 VDC.  
For description, see below.  
IEEE-1613 Compliance 
An IEEE-1613 compliant option of the TP module can be ordered from RAD. For more information, 
contact your local Business Partner.  
Features 
Teleprotection Services 
Teleprotection signals from protective relays are among the most critical data transmitted across utility 
networks, as they protect the power network from severe damages resulting from faulty high-voltage 
lines. By enabling immediate fault clearance, Teleprotection has a decisive role in ensuring 
uninterrupted power supply and therefore requires special attention with regards to network 
performance and reliability. Specifically, protection commands must be assured immediate delivery 
when problems are detected, so that faulty equipment can be disconnected before causing a system-
wide damage. 
The most common schemes for power system protection, specifically for protecting high-voltage 
transmission lines, use either current differential protection, distance (impedance) protection, or a 
combination of both. The former typically measures the current entering and leaving the protection 
14. M-ETH, T3, Teleprotection and VC Modules 
zone to decide if the monitored segment should be disconnected. This requires communication between 
the relays on both ends of the zone, and is available using the Megaplex variety of teleprotection 
communication channel interfaces, including C37.94, X.21, E1/T1, E&M, and V.35. In addition to the 
digital interfaces, the Megaplex distance TP module enables impedance-based TP end equipment to 
send commands to the remote TP end equipment when impedance measurements results vary from 
those taken under normal conditions. 
Megaplex-4 with its teleprotection modules delivers teleprotection commands and automation with 
mission-critical accuracy over dedicated fiber, TDM or IP, to help central control better manage the 
power grid load and to protect termination and transformation equipment from severe damages 
resulting from faulty high-voltage lines. 
The TP module supports up to 4 command inputs and 8 outputs, enabling teleprotection equipment to 
utilize the advanced transport capabilities offered by Megaplex. 
It also includes three independent groups of CMD channels: 
• 
East – CMD channels 1 (working) and 2 (protection) 
• 
West – CMD channels 3 (working) and 4 (protection). 
• 
Automation – CMD channels 5 and 6. 
The teleprotection commands can be locally output or be carried to a peer card/Megaplex over a 
TDM/SDH network or over a packet switch network. Up to 4 commands can be carried over a single DS0. 
The Megaplex advanced carrier Ethernet & pseudowire capabilities guarantees mandating the 
performance levels when migrating to packet networks with hard QoS, as well as robust latency and 
jitter protection. 
The module operates in conjunction with other Megaplex modules catering for a variety of interfaces, 
such as voice, high speed, low speed and others, to provide any possible service needed in a substation. 
Pseudowire Services  
TP modules provide TDM pseudowire access gateway or PWE server functionality over packet-switched 
networks (Ethernet and IP) for TDM traffic (E1, T1, SHDSL, ISDN, high-speed and low-speed data, voice, 
teleprotection) received via the Megaplex-4 TDM buses from other modules. This is done via 
independently-configurable internal DS1 ports available in the module.  
The number of DS1 ports is 4. The number of PW ports is 8. When PW redundancy is used, 4 ports out of 
these 8 are used as working ports and other 4 as protection ports.  
TP modules provide pseudowire emulation services over packet-switched networks using the CESoPSN 
(structure-aware TDM circuit emulation over PSN) protocols in accordance with RFC5086. 
14. M-ETH, T3, Teleprotection and VC Modules 
The pseudowire services enable converting TDM payload to packets and transferring these packets 
through PSN defined in the Megaplex-4.   
Packet structure is independently selectable for each pseudowire, for compatibility with the PSN type 
(UDP/IP or ETH). For maximum flexibility in system applications, the framing format of the pseudowire 
device at the destination (referred to as a pseudowire peer) can also be taken into account. DS1 ports 
can be used as converters between E1 and T1 at two end points. 
Any Fast Ethernet, GbE, Logical MAC, PCS or bridge port of any module installed in the chassis can be 
used as interfaces of the PW traffic towards the network. The selectable exit ports are bound to SVI 
ports.  
Note 
Unlike MPW-1, SH-16/E1/PW, VS-6/E1T1 and VS-16E1T1-PW modules, TP 
modules do not support adaptive clock recovery (see Features Supported by 
PW-Equipped I/O Modules table in Chapter 8).  
 
Nominal Input Control Voltage  
The teleprotection procedure works as follows:  
1. Measuring transformers take samples of the 50 Hz signal and deliver them to the protection 
relay using “sampled values” messages. 
2. The protection relay analyses this information and makes decision on whether to trip the line or 
not.  
3. The trip decision is translated from a signal with 220 VDC, 110 VDC, or soft-selectable trigger 
voltage level. 
The voltage levels at which command on and off are guaranteed are listed below for each nominal input 
control voltage. The result for voltages between these two levels (on or off) cannot be guaranteed. 
Trip Voltages  
TP Module Option 
Command on Guaranteed 
(“Rising Edge”) 
Command off Guaranteed (“Falling 
Edge”) 
24 VDC nominal 
> 19.2 VDC 
< 16 VDC 
48 VDC nominal 
> 38.4 VDC 
< 32 VDC 
110 VDC nominal 
> 88 VDC 
< 73.3 VDC 
125 VDC nominal 
> 100 VDC 
< 83.3 VDC 
220 VDC nominal 
> 176 VDC 
< 146.7 VDC 
14. M-ETH, T3, Teleprotection and VC Modules 
TP Module Option 
Command on Guaranteed 
(“Rising Edge”) 
Command off Guaranteed (“Falling 
Edge”) 
250 VDC nominal 
> 200 VDC 
< 166.7 VDC 
Automation  
The TP module is also used for the automation processes by responding to commands from the control 
center and activating the corresponding output relays, thus allowing for uninterruptable power supply 
throughout the grid when a fault occurs. 
In this application, the input signal is received from the controller via regular cmd-in command. This 
command is multiplexed in a cmd channel, and the cmd channel is broadcast via DS0 cross-connect to 
any number of timeslots in any number of E1/T1 links. On the receive site (in the substation)the ports 
serving this feature are CMD channels 5 and 6. These channels are operating in uni-directional mode 
(see below). 
Teleprotection Frame Structure  
The figure below describe the frame structure, the location and usage of bits for a single cmd channel (4 
bytes, 64 kbps data rate) 
 
TS#1 E1 Frame# n 
 
TS#1 E1 Frame# n+1 
 
TS#1 E1 Frame# n+2 
 
TS#1 E1 Frame# n+3 
1 2 3 4 5 6 7 8 … 
1 2 3 4 5 6 7 8 … 
1 2 3 4 5 6 7 8 … 
1 2 3 4 5 6 7 8 
 
 
 
 
 
1 1 4  
8 7 6 5  
2 2 3  
 
 
 
 
 
3 3 2  
 
 
 
 
 
4 4 1 
1
3 
3
0 
2
9 
2
8 
2
7 
2
6 
2
5 
2
4  
2
3 
2
2 
2
1 
2
0 
1
9 
1
8 
1
7 
1
6 
 
1
5 
1
4 
1
3 
1
2 
1
1 
1
0 
9 8  
7 6 5 4 3 2 1 0 
Color coding is as follows: 
 
TDM frame alignment 
 
RAI – Remote alarm. RX Sync loss or continues Address mismatch 
 
FP, Fault propagation. FP is currently not supported, the bit is used as a trigger to 
display latency alarm 
 
ACT, Active – “1”, Non active – “0”. This bit indicates if this cmd-channel is at 
working or protection state 
14. M-ETH, T3, Teleprotection and VC Modules 
 
 
 
 
 
 
 
 
 
 
 
Teleprotection Frame Structure 
Bit 
# 
Frame # 1 
Frame  #2 
Frame  
#3 
Frame  
#4 
1 
TDM frame alignment 
Address field to prevent wrong 
switching of the timeslot. Rx address is 
compared to the expected Tx address. 
 
Timestamp for 
latency check 
 
2 
RAI – Remote alarm. RX Sync loss or 
continues Address mismatch 
Timestamp for 
latency check 
 
3 
FP, Fault propagation. FP is currently not 
supported, the bit is used as a trigger to 
display latency alarm 
Timestamp for 
latency check 
 
4 
ACT, Active – “1”, Non active – “0”. This 
bit indicates if this cmd-channel is at 
working or protection state 
Timestamp for 
latency check 
 
5 
SW communication channel (SCC in CPU with HDLC) 
6 
Command bits 
7 
Commands bit error detection 
 
SW communication channel (SCC in CPU with HDLC) 
 
Address field to prevent wrong switching of the timeslot. Rx address is compared to 
the expected Tx address. 
 
Command bits 
 
Commands bit error detection 
 
Timestamp for latency check 
14. M-ETH, T3, Teleprotection and VC Modules 
Bit 
# 
Frame # 1 
Frame  #2 
Frame  
#3 
Frame  
#4 
8 
Address field to prevent wrong switching of the timeslot. Rx address is compared to the expected Tx 
address. 
Ports  
The module architecture and data flow is shown below.  
Note 
Out of 8 PW ports of a TP module only 4 can be configured as working PW 
ports. Other 4 ports are reserved for protection PW ports.  
The table below lists the Teleprotection module entities (ports) and their hierarchy.  
 
Trip Cross-connect
Primary 
Trip Out
Secondary 
Trip Out
East
West
Automation
 
ds1
1..4
PW 1..8
CL.2 Ethernet 
Engine
Switch
CL.2 DS0/1
Cross-connect
4 x E1
FE
cmd-out-i
#4
cmd-out-i
#1
cmd-out
#5
1:n
cmd-channel
#6
cmd-channel
#5
cmd-channel
#4
cmd-channel
#3
cmd-channel
#2
cmd-channel
#1
Trip In
cmd-out
#8
cmd-out-i
#4
cmd-out-i
#4
cmd-out-i
#1
cmd-out-i
#4
cmd-out-i
#1
cmd-out-i
#4
cmd-out-i
#1
cmd-out-i
#4
cmd-out-i
#4
cmd-out-i
#1
cmd-out-i
#4
cmd-out-i
#1
cmd-out-i
#1
RTU
DS0
4 x E1
cmd-out-i
#1
TP
 
TP Module Architecture  
The module includes the following blocks:  
• 
Four cmd channels (1,2,3,4) are used to transport teleprotection information over the 
telecommunications network. The teleprotection information transported over cmd channels is 
based on the command x-connect logic (see below).  
14. M-ETH, T3, Teleprotection and VC Modules 
• 
Another two cmd channels (5,6) are used for the automation processes by responding to 
commands from the control center and activating the corresponding output relays 
• 
Four cmd-in ports house the logic to manipulate the physical inputs to the module. 
• 
Four cmd-out ports (#1..#4) house the logic to manipulate the physical outputs from the 
module.  
• 
Additional four cmd-out ports (#5..#8) can be used as follows: 
 
Serve as secondary cmd-out ports – in this case they are bound to the primary ports and 
automatically copy their configuration. 
 
Used to report alarms to outside indicators (such as lights, buzzers and bells located on a 
bay alarm or remote monitoring panel), and to control external devices or applications (such 
as fans, dialers and backup power sources). Each relay can be controlled by a specific event 
in the network, in accordance with the configuration defined by means of the bind-alarm-
to-relay and bind-alarm-source-to-relay commands. These commands are performed under 
reporting context, as described in Chapter 11.  
• 
Four cmd-in-i ports for each cmd channel (1,3) and four cmd-out-i  ports for each cmd channel 
(1,3,5,6) house the logic to manipulate the logical Rx/Tx information over the corresponding 
cmd channel. This logic is capable to perform either basic transparent command cross-connect 
or logical operation (and/or function) between the external/internal inputs/outputs and 
teleprotection information transported over cmd channels. 
• 
8 pw and 4 ds1 ports provide PWE direct encapsulation of Teleprotection commands into a PWE 
session over PSN. 
Note 
Out of 8 PW ports of a TP module only 4 can be configured as working PW 
ports. Other 4 ports are reserved for protection PW ports.  
Teleprotection Architecture Entities and their Hierarchy  
Name 
Number of 
Ports  
Possible Values 
Remarks 
cmd-in 
4 
slot/1 …… slot /4 
 
cmd-in-i 
8 
slot /1/1 …… slot /1/4 
for cmd-channel 1 (2) 
 
 
slot /3/1 …… slot /3/4 
for cmd-channel 3 (4) 
cmd-out 
8 
slot /1 …… slot /4 
Primary ports 
 
 
slot /5 …… slot /8 
Secondary ports 
cmd-out-i 
16 
slot /1/1 …… slot /1/4 
for cmd-channel 1 (2) 
 
 
slot /3/1 …… slot /3/4 
for cmd channel 3 (4) 
14. M-ETH, T3, Teleprotection and VC Modules 
Name 
Number of 
Ports  
Possible Values 
Remarks 
 
 
slot /5/1 …… slot /5/4 
for cmd-channel 5 
 
 
slot /6/1 …… slot /6/4 
for cmd-channel 6 
cmd-channel 
6 
slot /1 …… slot /6 
1, 3 – working channels 
2, 4 – protection channels  
5, 6 – automation channels 
ds1 
4  
slot/1… slot/4 
 
pw 
8 
slot/1… slot/8 
 
Cross-Connect 
The data flow in the TP module is shown in the diagram below. As seen from the diagram, 3 types of 
cross-connect are used in the module: trip (command) cross-connect, ds0 cross-connect and pw-tdm 
cross-connect. 
 
Command (Trip) Cross-Connect  
The figure below shows the command cross-connect diagram in the TP module.   
Each white circle denotes that the selected output is controlled by the selected input. In case of multiple 
selections and/or logical operators are used.  
For each cmd-out or cmd-in-i port you can create a group of cmd-out-i or  
cmd-in  ports that will serve as trigger sources for the current port. This is done by means of the trigger-
bind command. The trip value of each port is 0 or 1. Using logical and/or operators you can set the 
required conditions for the ports in the group. 
 
cmd-
channel#1
Trip cross connect
cmd-
channel#6
cross connect
ds0
ds#1
ds#4
cross connect
pw-tdm
cmd-pw#1
cmd-pw#8
Router
Peer/RI
ETH
ETH
14. M-ETH, T3, Teleprotection and VC Modules 
Logical AND/OR
Selected cross connect
Primary CMD selection
CMD OUT 1..4 – Primary
CMD OUT 5..8 - Secondary
CMD slot:port
CMD slot:port:tributary
CMD In #1
CMD Out #1
CMD-CH 1/2
or
or
or
or
CMD-CH 3/4
CMD-CH 1/2
CMD-CH 3/4
CMD In #2
CMD In #3
CMD In #4
CMD Out #2
CMD Out #3
CMD Out #4
CMD Out #5
CMD Out #6
CMD Out #7
CMD Out #8
CMD-OUT-I #1
CMD-OUT-I #2
CMD-OUT-I #3
CMD-OUT-I #4
CMD-OUT-I#1
CMD-OUT-I #2
CMD-OUT-I #3
CMD-OUT-I #4
CMD-IN-I #1
CMD-IN-I #2
CMD-IN-I #3
CMD-IN-I #4
CMD-IN-I #1
CMD-IN-I #2
CMD-IN-I #3
CMD-IN-I #4
CMD-CH 5/6
CMD-OUT-I #1
CMD-OUT-I #2
CMD-OUT-I#3
CMD-OUT-I #4
 
Command Cross-Connect in TP Module  
DS0 Cross-Connect  
The routing of the individual CMD channel timeslots (timeslot assignment) is configured via ds0 cross-
connect. The cross-connect is performed between the cmd-channel and timeslots on the 
E1/T1/DS1/DS1-opt ports of the uplink module.  
The TP module supports the following cross-connect modes: 
• 
Bidirectional mode (see below): In this mode the CMD channel is cross-connected to timeslots 
on the E1/T1 link in bidirectional way. The purpose of this mode is to provide bidirectional 
connectivity between two sites, mainly for Distance Relay Protection scenarios. In this case the 
bidirectional connectivity exists as part of the service, meaning that the latency can be checked 
periodically, without user intervention. 
14. M-ETH, T3, Teleprotection and VC Modules 
 
cmd channel
Link
Link
cmd in/out
cmd channel timeslot
MP
MP
 
Bidirectional Cross-Connect  
• 
Unidirectional – Command report (see below). In this mode the bidirectional functionality of 
the CMD channel can be used, since each command input at the substation has a corresponding 
command in the Control Center. 
T
P
R
T
P
R
SCADA
Computer
Link
Link
Link
Link
Cmd channel
Cmd channel timeslot 
Cmd in/out
MP#1
MP#n
cmd out
cmd out
cmd in
cmd in
MP#1
MP#n
Site A
Site B
 
Unidirectional Rx Cross-Connect (Command Report)  
• 
Unidirectional – Command Respond (see below). As a result of getting a command report from 
one of the TP relays, the SCADA computer responds by transmitting this command to several 
substations. 
14. M-ETH, T3, Teleprotection and VC Modules 
Substations
Control Center
SCADA
Computer
Link
Link
E1
E1
Cmd channel
Cmd channel timeslot 
Cmd in/out
MP#1
MP#n
cmd-out
cmd-in
cmd-out
MP
 
Unidirectional Tx Cross-Connect  (Command Respond)  
PW-TDM Cross-Connect  
Cmd-channel ports are connected to PWs via DS1 ports, as shown in the diagram below.  
PW 
Static 
Router
cmd-channel
pw
1/1
cross connect 
dso
flow
RI
ETH
peer
ds1
1/1
1:1
cross connect 
pw-tdm
cmd-channel
 
TP modules can be also used as servers for other modules not equipped with PW. In the diagram below, 
any Megaplex-4 service port is cross-connected to the DS1 port of the TP module (DS0 cross-connect); 
DS1 ports are cross-connected to PW (PW-TDM cross-connect). 
PW 
Static 
Router
Any port
pw
1/1
cross connect 
dso
flow
RI
ETH
peer
ds1
1/1
1:1
cross connect 
pw-tdm
Any port
Any Megaplex-4  
module
VS module
 
Addresses Point-to-Point  
In order to recognize and in this way to prevent a false DS0 cross-connect of teleprotection data in the 
cmd channels, each transmission frame contains an address. This address is checked for each frame. If 
there is a mismatch between the Rx address and the expected Tx address, the frame is discarded. After 
detection of an address failure an alarm is raised and the command outputs are blocked.  
14. M-ETH, T3, Teleprotection and VC Modules 
Latency Check 
The latency check in the Teleprotection module is based on echo-timing of dedicated bits located in the 
TP frame. Based on the user configuration, one side is transmitting the time stamp that is changing 
every 125 µsec and the other side is echoing these bits back. Based on the difference between the Tx 
and Rx values, the originator side is calculating the latency. The maximum latency value supported by 
this mechanism is 32 msec.  
The table below describes the functionality of the latency check mechanism depending on the 
configured Rx/Tx address values. 
Address Values 
Functionality 
Configured tx-address > 
configured rx-address 
Cmd-channel echoes the timestamp originated by the opposite side 
Configured tx-address < 
configured rx-address 
Cmd-channel calculates the latency based on the received value 
compared to the transmit value.  
Configured tx-address = 
configured rx-address 
CLI error 
Configured tx-address = 
configured rx-address=254 
Checking the latency when cmd-channel is looped. Cmd-channel 
calculates the latency based on the received value compared to the 
transmit value. The calculated value is not transmitted to the 
opposite side over the cmd channel frame 
Bounce Override and Preset Duration  
Due to electrical transience in the station, an incoming trip signal (cmd-in) may bounce. This problem is 
resolved in two stages. The first stage is to filter the incoming signal from transient noises – this is 
performed with the help of the bounce-override parameter. The cmd-in signal is sampled during the 
time defined by this parameter, and 90% of the dominating value is set as a new signal value.  
The bounce-override period value is a sum of two intervals: bouncing period itself (interval t1 in the 
diagram below) and the additional time interval (t2) allowed for assuring the signal to get finally 
stabilized. The t1 value should be set as specified in the documentation of the connected RTU 
equipment relay. 
The action of this parameter is schematically shown in the figure below.  
14. M-ETH, T3, Teleprotection and VC Modules 
0
1
2
3
4
5
6
7
8
9
Keying Stimulus
cmd-in
bounce override
0
1
2
3
4
5
t1
t2
 
Bounce Override Functionality  
Once the command is active and the new signal value is set, its duration can be extended by means of 
the preset-duration parameter. The action of this parameter is schematically shown in the figure below.  
0
1
2
3
4
5
6
7
8
9
Keying Stimulus
cmd-in
preset duration
0
1
2
3
4
5
6
7
8
9
0
1
2
3
0
1
2
3
4
5
6
7
8
9
Keying Stimulus
cmd-in
preset duration
0
1
2
3
4
5
6
7
8
9
0
1
2
3
preset duration
Input Pulse is longer than Preset Duration
Input Pulse is shorter than Preset Duration
 
Preset Duration  
14. M-ETH, T3, Teleprotection and VC Modules 
Command Prolongation and Pulse Duration  
If the received pulse period of cmd-out-i signal (received via cmd-channel) is shorter than prolongation 
value, the cmd-out pulse duration will be extended to the value of prolongation parameter. If this value 
is 0, no prolongation is performed.  
If the received pulse period of cmd-out-i signal (received via cmd-channel) is longer than the value of 
pulse duration, the cmd-out pulse duration will be shortened to this value. If this value is 0, no pulse 
duration is performed. 
The value Pulse duration must be always higher than prolongation, otherwise a configuration error 
message is generated.  
Protection  
The TP module features the following types of protection: 
• 
TDM group protection between DS1 ports of the TP module and DS1/DS1-opt/E1/T1/E1-i/T1-i 
ports of other Megaplex-4 modules (see TDM Group Protection in Chapter 7)  
• 
TDM group protection between cmd-channel ports (see TDM Group Protection in Chapter 7): 
Channels 1 and 3 serve as working ports and Channels 2 and 4 – as their protection ports, 
respectively.  
• 
Direct PW protection between two PW ports of the TP module (see PW Protection in Chapter 7). 
TDM Group Protection on DS1 Ports 
When pseudowires are configured on redundant internal DS1 ports, the pseudowire traffic is 
automatically protected as well. The protection mode is 1+1, meaning that the traffic is also sent on the 
protection DS1 port.  
The figure below illustrates the DS1 TDM group protection. For each protection group, you must first 
configure the internal DS1 port that will serve as the working port; this configuration is copied to the 
other port of the group. In addition, it is necessary to configure pseudowires from each internal DS1 port 
in the protection group to the desired destinations.  
 
14. M-ETH, T3, Teleprotection and VC Modules 
GbE
CL-A/1
GbE
CL-B/1
I/O 
Serial Port
DS1 #1
Working
PW #1
PW #2
SVI #1
SVI #2
DS1 #2
Protection 
TDM Group
 
TDM Group Protection for DS1 Ports   
PW Protection  
For PW protection, two PW ports on the same module are connected to the same DS1 port. A typical 
configuration is shown in the figure below.  
GbE
CL-A/1
GbE
CL-B/1
I/O 
Serial Port
DS1
PW #1
Working 
PW #2
Protection
SVI #1
SVI #2
 
PW Protection  
During normal operation, both PW ports process as usual the transmit and receive signals, but the receive 
output of the protection port is disconnected. The operational state of the protection port is continuously 
monitored to ensure that it is operating properly. If the working link fails, the corresponding port is 
disconnected, and the protection port takes over.  
For two ports configured to PW protection, the following parameters must be the same for both ports: 
• 
psn type (udp-over-ip or Ethernet)  
• 
tdm-oos  
• 
tdm-payload. 
Cross-connect can be configured only to working PW ports. 
14. M-ETH, T3, Teleprotection and VC Modules 
Timing  
The TP module has an internal timing generator that receives the nodal timing and clock signals from the 
Megaplex-4 chassis and generates the internal timing and clock signals needed for module operation.  
Note 
Unlike MPW-1, SH-16/E1/PW, VS-6/E1T1 and VS-16E1T1-PW modules, VS 
voice modules do not support adaptive clock recovery (see Features Supported 
by PW-Equipped I/O Modules table in Chapter 8).  
 
Management 
All operating parameters of the TP module are soft-selectable via the management system. 
Physical Description  
The TP module occupies one I/O slot in the Megaplex-4 chassis. The module panel is shown below.  
 
TP Module Panel 
14. M-ETH, T3, Teleprotection and VC Modules 
LED Indicators  
Teleprotection Indicators 
The table below explains the functions of the indicators located on the module panel. 
TP Indicators 
Indicator 
Number 
Color 
Description 
CMD CHANNEL  
4  
Red/green 
Green On: Port synchronized 
Red On: RAI/LOF/Add mismatch  
Red Blinking: CRC Errors  
Off: Shutdown  
 
CMD IN  
4 
Red/green 
Green: No alarms 
 
Red On: Alarm state 
 
Off: Shutdown 
CMD OUT  
8 
Red/green 
Green: Steady State 
 
Red On: Alarm State 
 
Off: Shutdown 
ALM 
1 
Red 
Red Blinking: Events detected 
 
Off: No events  
Latched LEDs 
Due to severity of Teleprotection events the module LEDs provide a visual record of events that 
happened in the past, to inform the operator of teleprotection events that occurred when he was not 
present in the site. 
The LEDs related to the TP IN and TP OUT ports support two modes of operation: 
• 
Latched – the LED is on once the related command become active; turning the LED off is done 
via a user command. 
• 
Event – the LED follows the command activity. 
14. M-ETH, T3, Teleprotection and VC Modules 
Technical Specifications  
Compliance  
Teleprotection performance  
complies with the IEC 60834-1 standard. 
Input  
Connector 
Terminal block, 8-pin 
 
Number of command inputs 
4 
 
Nominal input control voltage 
• ± 110 VDC 
• ± 220 VDC  
• Soft-selectable: ±24, ±48, ±110, ±125, ±220 or 
±250 VDC 
 
Configurable debounce for noise 
filtering  
 
 
Wire diameter 
up to 2.5 sq. mm 
Output  
Connectors 
2 Terminal blocks, 8-pins each 
 
Total number of outputs 
 
• 8 (4 primary + 4 secondary): 
• For each secondary output one primary 
command can be selected. 
• More than one secondary output can be bound 
to one primary command 
• Ports 5 to 8 can be used to report internal 
system alarms to outside indicators. 
 
Relay type 
Electro-mechanical relay (EMR) 
Solid-state relay (SSR) 
 
Switching 
 
up to 250 VDC, 0.25A on inductive load 
 
Wire diameter 
up to 2.5 sq. mm 
 
Rx/Tx processing 
Independent  
 
Prolongation time 
Command-configurable 
Optimization 
 
Security- or speed-optimized according to 
application  
Event Reporting 
 
 
Events Time stamping with 1 msec accuracy 
Accepting GPS time via IEC-60870-5-104 or SNTP 
Protection  
 
Equipment protection 
On-board CMD Channel protection 
Megaplex traffic (TDM-group) protection 
14. M-ETH, T3, Teleprotection and VC Modules 
PW group protection 
 
Recovery 
Less than 10 msec  
Pseudowire 
Number of Pseudowires 
Up to 640 pseudowires per Megaplex-4 
Up to 8 pseudowires (4 working + 4 protection) per 
TP module 
 
Pseudowire Protocol 
CESoPSN in accordance with RFC5086 
 
Packet Switched Network Types 
• UDP over IP 
• MEF-8 Ethernet 
 
Jitter Buffer Size 
250 µsec to 8000 µsec, in 1-µsec steps.  
Note: The value entered by the user is rounded 
upward to the closest n*125 µsec value.  
Diagnostics 
 
• Remote loopback per command 
• End-to-end delay measurements 
Isolation 
 
2500 VRMS between protection circuits and chassis 
Indicators 
 
See Error! Reference source not found.Error! 
Reference source not found.Error! Reference 
source not found. 
Power Consumption  
5W max 
Configuration 
 
Programmable via Megaplex-4 management system  
Preparing the Module for Installation 
 
Warning 
Before performing any internal settings, adjustment, maintenance, or 
repairs, first disconnect all the cables from the module, and then remove the 
module from the Megaplex-4 enclosure. 
No internal settings, adjustment, maintenance, and repairs may be 
performed by either the operator or the user; such activities may be 
performed only by a skilled technician who is aware of the hazards involved. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. 
 
14. M-ETH, T3, Teleprotection and VC Modules 
Caution 
The TP modules contain components sensitive to electrostatic discharge 
(ESD). To prevent ESD damage, always hold the module by its sides, and do 
not touch the module components or connectors.  
 
Caution 
To prevent physical damage to the electronic components assembled on the 
two sides of the module printed circuit boards (PCB) while it is inserted into 
its chassis slot, support the module while sliding it into position and make 
sure that its components do not touch the chassis structure, nor other 
modules.  
 
Installing a Module in the Chassis 
TP modules may be installed in an operating chassis (hot insertion). 
 
Warning 
The TP module starts operating as soon as it is inserted in an operating 
chassis.  
 
 To install a TP module: 
1. Refer to the system installation plan and identify the prescribed module slot. 
2. Check that the fastening screws at the module sides are free to move. 
3. Insert the TP module in its chassis slot and slide it in as far as possible. 
4. Secure the TP module by tightening its two fastening screws. 
5. The module starts operating as soon as it is plugged into an operating enclosure. At this stage, 
ignore the alarm indications. 
Connecting to Remote Equipment  
Before starting, identify the cables intended for connection to each port of this module, in accordance 
with the site installation plan.  
14. M-ETH, T3, Teleprotection and VC Modules 
The module has 3 8-pin Terminal Block connectors. The upper connector serves for connection to CMD-
IN ports. Two other connectors serve for connection to CMD-OUT ports. The tables below list the 
connector pin assignment.  
CMD IN Connector  
Pin  
Function 
1 } 
CMD-IN 1 
2 
 
3 } 
CMD-IN 2 
4 
 
5 } 
CMD-IN 3 
6 
 
7 } 
CMD-IN 4 
8 
 
Upper CMD OUT Connector  
Pin  
Function 
1 } 
CMD-IN 1 
2 
 
3 } 
CMD-IN 2 
4 
 
5 } 
CMD-IN 3 
6 
 
7 } 
CMD-IN 4 
8 
 
14. M-ETH, T3, Teleprotection and VC Modules 
 
Lower CMD OUT Connector  
Pin  
Function 
1 } 
CMD-OUT 5 
2 
 
3 } 
CMD- OUT 6 
4 
 
5 } 
CMD- OUT 7 
6 
 
7 } 
CMD- OUT 8 
8 
 
Configuration Sequence 
The list of tasks that can be performed on the TP module and the recommended configuration sequence 
are described in the table below.  
Task 
Configuration Context 
Reference  
Configuring a TP module and putting 
it into service 
configure>slot>card-type  
card-type=alarm-relay tp 
Note: you must also configure the CL.2 or uplink module port parameters (depending on the TP 
module application). For the uplink module configuration procedure, refer to the appropriate section 
of this Appendix. 
Configuring the cmd-in ports  
configure>port>cmd-in 
Configuring CMD-IN Ports in 
Chapter 5 
Configuring the cmd-in-i ports  
configure>port>cmd-in-i 
Configuring CMD-IN-I Ports in 
Chapter 5 
Configuring the cmd-out ports  
configure>port>cmd-out 
Configuring CMD-OUT Ports in 
Chapter 5 
14. M-ETH, T3, Teleprotection and VC Modules 
Task 
Configuration Context 
Reference  
Binding an alarm of specific source 
type (optionally on a specific user 
port) to an alarm output port (cmd-
out 5..8 only) 
configure>reporting 
 
Configuring Alarm Reporting in 
Chapter 11  
Configuring the cmd-out-i ports  
configure>port>cmd-out-i 
Configuring CMD-OUT-I Ports 
in Chapter 5 
Configuring the cmd-channels  
configure>port>cmd-
channel 
Configuring CMD-CHANNEL 
Ports in Chapter 5 
Configuring cross-connect 
 
 
Configuring DS0 cross-connect 
between the serial/cmd-
channel/DS1 port or the module 
and timeslots on the 
E1/T1/DS1/DS1-opt ports of the 
uplink module)  
configure>cr>ds0 
DS0 Cross-Connect in 
Chapter 8 
 
Establishing cross-connection 
between the pseudowire and 
timeslots on the ds1 port 
configure>cr>pw-tdm  
 
PW-TDM Cross-Connect in 
Chapter 8 
 
Configuring protection 
 
 
Configuring cmd-channel protection 
configure>protection>tdm-
group 
TDM Group Protection in 
Chapter 7  
Configuring protection for internal 
DS1 ports 
configure>protection>tdm-
group 
TDM Group Protection in 
Chapter 7 
 
Configuring protection for PWs 
configure>protection>pw 
 
Cross-connecting the DS1 port with 
a vc12-vt2/vc11-vt1.5 from an 
SDH/SONET port  
configure>cr>sdh-sonet   
 
SDH/SONET Cross-Connect 
in Chapter 8 
 
Configuring pseudowire services   
 
14. M-ETH, T3, Teleprotection and VC Modules 
Task 
Configuration Context 
Reference  
Routing parameters for the 
Megaplex-4 PW router 
(interfaces, associated static 
routes, default gateway) 
configure>router (2) 
Pseudowire Router in 
Chapter 8 
Adding pseudowire peers  
configure>pwe>pw>peer 
Peer in Chapter 8 
Configuring the PW peer 
parameters 
configure>peer 
Peer in Chapter 8 
Adding pseudowires terminated 
at the MPW-1 internal DS1 ports 
configure>pwe 
Pseudowires in Chapter 8 
Configuring the pseudowires  
configure>pwe>pw 
Pseudowires in Chapter 8 
Configuring the internal DS1 
ports  
configure>port>ds1  
DS1 Ports in Chapter 5 
Configuring flows  
 
 
Configuring ingress and egress 
flows between the SVI port 
(bound to Router 2 interface) 
and Logical MAC port or Ethernet 
port  
configure>flows 
 
Flows in Chapter 8 
Creating an alarm input and setting 
the alarm description  
configure>reporting 
Configuring Alarm Reporting in 
Chapter 11 
Configuration Example 
#==============================# 
#       SLOT config  
#==============================# 
exit all 
configure slot ps-a card-type power-supply ps 
configure slot cl-a card-type cl cl2-ds0 
configure slot 4 card-type alarm-relay tp 
commit 
 
#==============================# 
14. M-ETH, T3, Teleprotection and VC Modules 
# TP card                    # 
#==============================# 
exit all 
 
#==============================# 
#Cmd-In configuration 
#=============================== 
configure port cmd-in 4/1 no shutdown 
 
mp4100>config>port>cmd-in(4/1)# info detail 
    name  "IO-4 Cmd in 01" 
    no shutdown 
    preset-duration  0 
    bounce-override  1000 
    no led-latched 
    input-active high 
    switching-voltage  48 
 
#==============================# 
#Cmd-In-I configuration 
#=============================== 
configure port cmd-in-i 4/1/1 no shutdown 
configure port cmd-in-i 4/1/1 trigger-bind 1 cmd-in 4/1 
 
mp4100>config>port>cmd-in-i(4/1/1)# info detail 
    name  "IO-4 Cmd in-i 01" 
    no shutdown 
    trigger-bind  1  cmd-in  4/1  none 
     
#==============================# 
#Cmd-Out-I configuration 
#=============================== 
configure port cmd-out-i 4/1/1 no shutdown 
 
mp4100>config>port>cmd-out-i(4/1/1)# info detail 
    name  "IO-4 Cmd out-i 01" 
    no shutdown 
    oos-code  last-valid-state 
 
#==============================# 
#Cmd-Out configuration 
#=============================== 
configure port cmd-out 4/1 no shutdown 
configure port cmd-out 4/1 trigger-bind 1 cmd-out-i 4/1/1 
configure port cmd-out 4/1 secondary-bind 4/5 
 
mp4100>config>port>cmd-out(4/1)# info detail 
    name  "IO-4 Cmd out 01" 
    no shutdown 
    prolongation  0 
    alarm-state-energized  yes 
    secondary-bind 4/5 

## 14.4 VC-4, VC-4A, VC8, VC-8A and VC16  *(p.1139)*

14. M-ETH, T3, Teleprotection and VC Modules 
    no led-latched 
    trigger-bind  1  cmd-out-i  4/1/1  
 
#==============================# 
#Cmd-Channel configuration 
#=============================== 
configure port cmd-channel 4/1 no shutdown 
 
mp4100>config>port>cmd-channel(4/1)# info detail 
    name  "IO-4 CMD Channel 01" 
    no shutdown 
    tx-address  1 
    rx-address  2 
    rate  64 
    trigger-mode  speed-optimized 
 
configure cr ds0 e1 1/1 ts 1 cmd-channel 4/1 bi-direction 
commit 
exit 
Monitoring and Diagnostics  
The TP module features remote digital loopback, activated from cmd-out-i ports. The loopback can be 
performed independently per each entity. 
For more detail, see Testing Teleprotection Ports in Chapter 5. 
14.4 VC-4, VC-4A, VC-8, VC-8A and VC-16  
This section describes the main features, applications and installation procedures for the voice I/O 
modules operating in the Megaplex-4 chassis with CLI management: 
• 
VC-4/4A/8/8A/16 – 4/8/16-port FXS/FXO/E&M PCM and ADPCM analog voice modules 
 
This section describes the technical characteristics, applications, installation and operation of the VC-4, 
VC-4A, VC-8, VC-8A and VC-16 voice interface modules for use in the Megaplex-4 Next Generation 
Multiservice Access Node, ver 3.0 and higher.  
For multifunction voice modules VS-6/E&M, VS-6/FXO, VS-6/FXS and FXS/E&M, see Versatile Modules 
chapter in this manual.  
14. M-ETH, T3, Teleprotection and VC Modules 
The VC-16 module provides 16 voice channels using toll-quality 64 kbps PCM voice encoding in 
compliance with ITU-T Rec. G.711 and AT&T Pub. 43801. The VC-8 and VC-4 modules are similar, except 
that they provide 8 or 4 channels, respectively. 
The VC-8A and VC-4A modules provide 8, respectively 4, voice channels using one of two user-selectable 
voice encoding modes: 
• 
Toll-quality 64 kbps PCM voice encoding in compliance with ITU-T Rec. G.711 and AT&T Pub. 
43801 
• 
Toll-quality 32 kbps ADPCM voice compression encoding in compliance with ITU-T Rec. G.726 
and G.727. 
Note 
The VC-4A/8A module family, as opposed to the VC-4/8/16 family, has been 
designed to provide mainly ADPCM services. If you need PCM services only, 
the  
VC-4/8/16 family will fully satisfy your needs. However, in addition to their 
main destination, the VC-4A/8A modules also support the PCM voice 
encoding. 
 
The modules offer flexible configuration of all their operational parameters, including automatic 
selection of the signaling information format in accordance with the operation mode. 
Each voice channel of the VC modules supports Caller ID by transparently transferring the FSK modem 
tones between the incoming rings. With this feature, a customer subscribed to a Caller ID service can 
see the Caller ID of an incoming or waiting call with any Caller ID display equipment. 
The voice channels of the VC-4, VC-8 and VC-16 modules support SMS message transfer between the 
telephones using DECT protocol. 
In ADPCM encoding mode, each channel requires only half a timeslot. Therefore, a single E1 link can 
carry up to 31 x 2=61 voice channels and a single T1 link can carry up to 24 x 2=48 voice channels.  
Product Options 
The VC modules are available in the following versions:   
• 
E&M –for operating with different types of E&M signaling: EIA RS-464 Types I, II, III and V (British 
Telecom SSDC5). This version is typically used for connection of tie lines between PBXs. Both 2-
wire and 4-wire lines are supported (user-selectable). A special E&M/POS version of VC-8 and 
VC-16 with positive signaling is available for use in those applications (for example, radio 
transmitters) in which positive signaling voltage is required, enabling the module signaling 
operation at +5V or +12V. A special E&M/EXT version can be ordered for working with the 
standard E&M (–48 VDC) voltage. 
14. M-ETH, T3, Teleprotection and VC Modules 
Note 
The E&M/POS version operates only with Type II Signaling 
• 
FXS – for direct connection to 2-wire telephones employing both loop-start and wink-start 
signaling methods, with battery polarity reversal.  
• 
FXO – for connection to PBX extension lines employing both loop-start and wink-start signaling, 
with battery polarity reversal. 
Special /MET ordering options of FXS and FXO modules are available for payphone metering support. 
Note 
In this section, the generic term VC is used when the information is applicable 
to all the VC-4, VC-4A, VC-8, VC-8A and VC-16 module versions. The complete 
designation is used only for information applicable to a specific version. 
Applications  
Basic VC-16/E&M Applications  
The following figure shows a basic E&M tie line application using VC-16/E&M modules. 
In this application, one VC-16/E&M module is used to provide 16 E&M tie lines between two analog 
PBXs through the SDH/SONET link interconnecting the Megaplex systems. 
 
Basic Application for VC-16/E&M Modules  
Off-Premises Extension (OPX) Applications 
In a typical OPX application, one FXO module located at the PBX side is used in a link with an FXS module 
to provide up to 16 off-premises extensions for an analog PBX connected to the FXO module channels.  
14. M-ETH, T3, Teleprotection and VC Modules 
 
OPX Application for FXO and FXS Modules  
The system configuration shown above permits using telephones connected to the channels of an FXS 
module installed in the Megaplex unit located at the other end of the link as extensions of an analog 
PBX. Each remote telephone then becomes a regular local PBX subscriber, which can be dialed by other 
subscribers using standard procedures, and can also dial any other PBX subscriber and use all the 
services available to local PBX subscribers. 
Each pair of telephones (local and remote) can then communicate directly without dialing: when one 
telephone goes off-hook, the other telephone rings. 
PSTN Access Applications  
Due to the flexible signaling configuration capabilities, the FXO modules can also be used on links ending 
in the public switched telephone network (PSTN). A typical PSTN access application is shown below.  
 
PSTN Application for FXO Modules  
In the application shown above, the extension lines of an analog PBX are connected to the channels of 
an FXO module, installed in a Megaplex unit connected to the PSTN through an E1/T1 or STM-1/OC-
14. M-ETH, T3, Teleprotection and VC Modules 
3/STM-4/OC-12 trunk line. This enables the PBX subscribers to dial PSTN subscribers through the 
Megaplex link, and PSTN subscribers can dial to PBX subscribers. 
Direct Inward Dialing (DID) Applications  
FXS and FXO modules support battery voltage polarity reversal for wink-start signaling, which is used in 
direct inward dialing (DID) applications.  
With DID, a PSTN subscriber first dials the number of one of the PBX external (trunk) lines, and after 
getting the PBX dial tone, can continue dialing the number of desired particular PBX extension, without 
requiring the assistance of the PBX operator.  
The following figure shows a typical DID application.  
 
Wink-Start Trunk Extension for DID Application using FXO and FXS Modules  
As shown above, the analog PBX trunk lines are connected to the PSTN through a Megaplex link.  The 
FXO module channels connect to the PBX extensions, and the central office (PSTN switch) lines that use 
wink-start signaling are connected to the corresponding FXS module channels. 
Payphone Applications 
Payphone applications use 12 kHz or 16 kHz pulses for metering line utilization. The FXO module 
supports the detection of 12 or 16 kHz metering pulses at the central office or PBX side, and the FXS 
module supports the generation of 12 or 16 kHz metering pulses, for direct connection to public 
payphones.   
Therefore, a Megaplex link can be used to connect payphones to a central office or PBX: 
14. M-ETH, T3, Teleprotection and VC Modules 
 
Payphone Application using FXO and FXS Modules  
In the typical payphone application shown above, an FXO module is installed at the PBX or central office 
side, and the public payphones are connected to an FXS module installed in the off-premises Megaplex.  
The remote payphone then becomes a regular local PBX subscriber, which can be dialed by other 
subscribers using standard procedures, and can also dial any other PBX subscriber, while transferring the 
metering signaling for billing purposes. 
Payphone applications are restricted to special ordering options.  
Broadcast Applications  
In addition to the normal (bidirectional) mode of operation, the VC modules support the unidirectional 
broadcast mode. For a description of this mode, refer to Unidirectional Broadcast Function under Cross-
Connections in Chapter 8.  
Features 
E&M Modules  
E&M modules are supplied in several panel versions, as described below in Error! Reference source not 
found.. 
The E&M modules have user-selectable 2-wire or 4-wire analog interfaces using E&M signaling. The 
interface type (2-wire or 4-wire) can be independently selected for each pair of channels (1, 2; 3, 4; etc.). 
A special 4-wire version with enhanced gain control is available for any E&M module.  
14. M-ETH, T3, Teleprotection and VC Modules 
Note 
4-wire E&M module versions with enhanced gain control do not operate in 2-
wire mode. 
The E&M modules support four types of E&M signaling: EIA RS-464 types I, II, III and V (similar to British 
Telecom SSDC5). The figure below shows the equivalent signaling circuits for the different signaling 
modes. 
The signaling type can be independently selected for each group of four channels (1, 2, 3, 4; 5, 6, 7, 8; 
etc.).  
• 
EIA RS-464 Type I signaling standard is supported without any external power supply. 
• 
EIA RS-464 Type II, III and V (BT SSDC5) signaling standards are supported by means of the 
internal -12 VDC power supply of the chassis. The -12 VDC voltage is suitable for most PBX 
systems. However, for full support of the EIA RS-464 Type II, III and V (BT SSDC5) signaling 
standards, a -48 VDC signaling voltage is required. For this purpose, a special E&M/EXT version 
can be ordered from RAD. 
The required -48 VDC voltage is always available when the Megaplex chassis is powered from a -
48 VDC source.  
Note 
For details on DC power sources and connection methods, see Connecting the 
Signaling and Feed Voltage Source in Chapter 2. 
 
A special E&M/POS version of VC-8 and VC-16 with positive signaling enables the module 
signaling operation at +5V or +12V (see Figure E). In this mode, the VC module sends signaling to 
the PBX by connecting GND to the SG pin. The E pin is permanently connected to GND and is not 
used. This version operates only with Type II Signaling. 
 
14. M-ETH, T3, Teleprotection and VC Modules 
 
PBX
-48VDC
M Lead
E Lead
E&M
Interface
M Lead
E&M
Interface
- 48VDC
E Lead
- 48VDC
SB Lead
SG Lead
M Lead
E&M
Interface
E Lead
- 48VDC
SB Lead
SG Lead
+12 VDC
+5 VDC
+12 VDC
M
M
 
 
L
L
e
e
a
a
d
d
E
SG
 
 
L
L
e
e
a
a
d
d
E
E
&
&
M
M
I
I
n
n
t
t
e
e
r
r
f
f
a
a
c
c
e
e
- 4
1.2 kΩ
1.2 kΩ
8VDC
A. RS-464 Type I
On-Hook
Off-Hook
  GND
- 48VDC
Condition
M
E
Open
GND
On-Hook
Off-Hook
  Open
- 48VDC
Condition
M/SB
E/SG
Open
GND
O
Idle
n-Hook
Off-Hook
 
 
 
 
O
O
p
p
e
e
n
n
 
 
 
 
G
G
N
N
D
D
C
C
o
o
n
n
d
d
i
i
t
t
i
i
o
o
n
n
M
M
E
SG
O
O
p
p
e
e
n
n
G
G
N
N
D
D
On-Hook
Off-Hook
  Open
- 48VDC
Condition
M/SB
E/SG
Open
GND
PBX
PBX
PBX
PBX
B. RS-464 Type II
C. RS-464 Type III
D. RS-464 Type V, SSDC5
E. E&M/POS Version (Type II only)
Active
+24 VDC
+24 VDC
M Lead
E Lead
E&M
Interface
Idle
  Open
  GND
Condition
M
E
Open
GND
LEGEND
= Signaling Detector Circuit
PBX
F. E&M/RJ/POS/24 Version 
Active
*E&M/EXT ordering option
(-48 VDC requires external 
DC feed)
*E&M/EXT ordering option
(-48 VDC requires external 
DC feed)
*E&M/EXT ordering option
(-48 VDC requires external 
DC feed)
-48 VDC*
-12 VDC
-48 VDC*
-12 VDC
-48 VDC*
-12 VDC
 
E&M Equivalent Signaling Circuits  
14. M-ETH, T3, Teleprotection and VC Modules 
FXS and FXO Modules  
The FXS and FXO modules are used to connect regular telephone sets (and other equipment with similar 
interface properties) to central office (PSTN) and PBX extension lines.  
FXS and FXO modules are intended for operation in a link, with the FXS module at the subscriber side 
and the FXO module at the central office or PBX side. However, FXS modules can also operate in a link 
with E&M modules. 
FXS Module Characteristics 
FXS modules are supplied in several panel versions, as described below in Error! Reference source not 
found.. 
The FXS modules have 2-wire analog interfaces and support FXS loop-start signaling, for direct 
connection to subscriber telephone sets.  
The FXS modules also support wink-start signaling. For VC-4 and VC-8 modules, the selection is made for 
the entire group of the module channels. For VC-16/FXS modules, the signaling mode (loop-start or 
wink-start) can be independently selected for each group of eight channels (1 to 8 and 9 to 16). 
To enable wink-start signaling, the FXS modules support feed voltage (battery) polarity reversal.  
For direct connection to payphones, the FXS modules (special FXS/MET ordering options) also support 
metering pulse generation. The user can select the metering pulses frequency (12 kHz or 16 kHz).  
The FXS modules require -48 VDC to supply the subscriber feed and ring voltages. The ring voltage is 
generated on the module itself, by an internal ringer.  
The required voltage can be supplied via the internal supply voltage connector of the module, from the 
chassis voltage distribution bus (see Connecting the Signaling and Feed Voltage Source in Chapter 2 for 
details). 
FXO Module Characteristics  
FXS modules are supplied in several panel versions, as described below in Error! Reference source not 
found.. 
The FXO modules have 2-wire analog interfaces and support FXO loop-start signaling for direct 
connection to central office and PBX extension lines.  
The FXO modules also support wink-start signaling. For VC-16/FXO modules, the signaling mode (loop-
start or wink-start) can be independently selected for each group of eight channels (1 to 8 and 9 to 16). 
14. M-ETH, T3, Teleprotection and VC Modules 
To enable wink-start signaling, the FXO module supports the detection of feed voltage (battery) polarity 
reversal.  
To permit connection to payphones, the FXO modules (special ordering options FXO/MET) also support 
metering pulse detection. The user can select the metering pulse detection frequency (12 kHz or 
16 kHz). 
The FXO modules do not require any external supply voltage. 
System Capacity  
The maximum capacity of transmitting VC channels in a chassis depends on the following parameters: 
• 
The number and type of modules with E1/E1-i/T1/T1-i/DS1 ports installed in the chassis 
• 
The number of free I/O slots for VC modules to be installed and the type of VC modules 
• 
Operating mode (PCM or ADPCM). 
The maximum MP-4100 chassis capacity is equivalent to 126 E1-i (over SDH) or 168 T1-i (over SONET) 
trunks. 
TDM Mapping 
The DS0 cross-connect matrix of the Megaplex-4 chassis enables flexible payload routing in the VC 
modules, independently configurable for each port, at the individual timeslots (DS0) level.  
Management 
All the module operational parameters are controlled by means of the Megaplex system management. 
Physical Description  
The VC modules occupy one module slot in the Megaplex-4 chassis.  
The module panels are described below.  
VC-16 Front Panels 
The following figure shows typical panels of VC-16 modules. 
 
14. M-ETH, T3, Teleprotection and VC Modules 
VC-16/FXS
VC-16/E&M
VC-16
FXS
VC-16/FXO
Voice Channel 
Connector 
(for all channels)
VC-16
E&M
CH
1-8
VC-16
FXO
CH
9-16
Voice Channel 
Connector 
(for all channels)
Voice Channels
9 to 16 
Connector 
Voice Channels
1 to 8 
Connector 
 
VC-16 Module Panels  
The VC-16 module panels have voice channel connectors only, and no indicators. 
The VC-16/E&M modules have two 68-pin female SCSI connectors, one for voice channels 1 to 8 and the 
other for voice channels 9 to 16. 
VC-16/FXS and VC-16/FXO modules have one 50-pin female Telco connector, for connection of all the 
voice channels. 
14. M-ETH, T3, Teleprotection and VC Modules 
VC-8 and VC-8A Front Panels 
The following figure shows typical panels of VC-8 modules. 
 
VC-8/E&M
VC-8
E&M
CH
1-8
VC-8/RJ/FXO
VC-8/RJ/FXS
VC-8/RJ
FXS
LOC
REM
CH-5
LOC
REM
CH-1
CH-6
CH-2
LOC
LOC
REM
REM
CH-7
CH-3
LOC
LOC
REM
REM
CH-8
CH-4
LOC
LOC
REM
REM
VC-8/RJ
FXO
CH-5
RING
REM
CH-1
RING
REM
CH-6
CH-2
RING
RING
REM
REM
CH-7
CH-3
RING
RING
REM
REM
CH-8
CH-4
RING
RING
REM
REM
VC-8/FXS
VC-8
FXS
VC-8/FXO
VC-8
FXO
 
VC-8/E&M/RJ/
POS/24
VC-8/RJ
E&M
CH1
CH2
CH3
CH4
E
M
E
M
E
M
E
M
CH5
CH6
CH7
CH8
E
M
E
M
E
M
E
M
 
VC-8/E&M/DS
VC-8
E&M/DS
CH
1-4
CH
5-8
 
VC-8 Module Panels  
14. M-ETH, T3, Teleprotection and VC Modules 
The following figure shows typical panels of VC-8A modules. 
VC-8A/E&M
Voice 
Channel 
Connector 
(for all 
channels)
VC-8A
E&M
CH
1-8
VC-8A/FXS
VC-8A
FXS
VC-8A/FXO
VC-8A
FXO
LOC
REM
CH-5
CH-5
LOC
REM
RING
REM
CH-1
CH-1
RING
REM
CH-6
CH-6
CH-2
CH-2
LOC
LOC
RING
RING
REM
REM
REM
REM
CH-7
CH-7
CH-3
CH-3
LOC
LOC
RING
RING
REM
REM
REM
REM
CH-8
CH-8
CH-4
CH-4
LOC
LOC
RING
RING
REM
REM
REM
REM
 
VC-8A Module Panels  
The VC-8/E&M and VC-8A/E&M module interfaces have one 68-pin female SCSI connector.  
The VC-8 FXS and FXO modules have two modifications with different type of connectors: VC-8 and VC-
8/RJ. 
In VC-8 modules, all the module channels are terminated in a 50-pin female Telco connector. The VC-
8/RJ module interface and the VC-8A module interfaces are terminated in eight RJ-12 connectors – one 
per channel.  
VC-4 and VC-4A Front Panels 
The following figures show typical panels of VC-4 and VC-4A modules, respectively. 
The 4-channel E&M module interface is terminated in four RJ-45 connectors – one per channel.  
The 4-channel FXS and FXO module interfaces are terminated in four RJ-12 connectors – one per 
channel. 
14. M-ETH, T3, Teleprotection and VC Modules 
VC-4/FXS
VC-4/E&M
VC-4
FXS
VC-4/FXO
VC-4
FXO
CH1
LOC
REM
CH1
RING
REM
CH2
CH2
LOC
RING
REM
REM
CH3
CH3
LOC
RING
REM
REM
CH4
CH4
LOC
RING
REM
REM
VC-4
E&M
CH1
CH2
CH3
CH4
E
M
E
M
E
M
E
M
 
 VC-4 Module Panels  
 
 
14. M-ETH, T3, Teleprotection and VC Modules 
VC-4A/FXS
VC-4A/E&M
VC-4A
FXS
VC-4A/FXO
VC-4A
FXO
CH1
LOC
REM
CH1
RING
REM
CH2
CH2
LOC
RING
REM
REM
CH3
CH3
LOC
RING
REM
REM
CH4
CH4
LOC
RING
REM
REM
VC-4A
E&M
CH1
CH2
CH3
CH4
E
M
E
M
E
M
E
M
 
 VC-4A Module Panels  
LED Indicators 
VC-16 modules do not have LED indicators. All VC modules with RJ connectors have separate LED 
indicators for each channel listed in the tables below.  
E&M Channel Indicators 
Name 
Description 
M  
On when the M line of the corresponding channel is off-hook (channel 
in use). 
E  
On when the E line of the corresponding channel is off-hook (channel in 
use). 
  FXS Channel Indicators 
Name 
Description 
REM  
On when a call initiated by the remote subscriber is being handled by 
the corresponding channel (channel is busy). 
14. M-ETH, T3, Teleprotection and VC Modules 
LOC  
On when the local subscriber of the corresponding channel is off-hook 
(busy). 
  FXO Channel Indicators 
Name 
Description 
REM  
On when the remote subscriber of the corresponding channel is 
off-hook (busy). 
RING  
On when ringing is received on the corresponding channel. 
Technical Specifications 
Number of  
VC-4, VC-4A 
4 
Channels 
VC-8, VC-8A 
8 
 
VC-16 
16 
Voice Processing 
Modulation Technique  
 
PCM: per ITU-T Rec. G.711 and AT&T Pub. 43801 
ADPCM: per ITU-T G.726 and G.727 
 
Echo Cancellation 
4 ms per channel as per G.168  
 
Companding 
µ-law or A-law (user-selectable)  
Bandwidth Requirements 
PCM  
ADPCM 
64 kbps per enabled channel (one timeslot) 
32 kbps per enabled channel (one timeslot per 
pair of channels) as per G.726 
24 kbps per enabled channel (one timeslot per 
pair of channels) as per G.727  
Analog Interface 
Interface Type 
 
 
 
E&M  
4-wire or 2-wire (user-selectable) 
 
Note: A special 4-wire version with enhanced gain control is available (see Transmit 
and Receive Levels for Various Interfaces below)  
 
 
FXS, FXO 
2-wire 
 
Compliance 
ITU-T Rec. G.712 
Analog Parameters 
Nominal Level 
0 dBm  
14. M-ETH, T3, Teleprotection and VC Modules 
 
Nominal Impedance 
600Ω 
 
Return Loss (ERL) at  
300 to 3400 Hz 
Better than 20 dB 
 
Frequency Response 
(Ref: 1020 Hz) 
0 dB ±0.5 dB, at 300 to 3000 Hz 
0 dB ±1.1 dB, at 250 to 3400 Hz 
 
Transmit and Receive 
Levels 
User-selectable in 0.5 dB ±0.15 dB steps (see Transmit 
and Receive Levels for Various Interfaces below) 
 
Signal to Total Distortion 
Using ITU-T Rec. G.712 
(8-bit PCM encoding) 
-30 to 0 dBm0:  
better than 33 dB 
-45 to +3 dBm0:  
better than 22 dB 
 
Idle Channel Noise 
Better than -65 dBm0 (+20 dBrnc) 
 
Transformer Isolation 
1500 VRMS 
  Transmit and Receive Levels for Various Interfaces  
Module Interface 
Transmit 
[dbm] 
          min               max 
Receive 
[dbm] 
         min               max 
E&M regular 2W  
-8 
+5 
-17 
+2 
E&M regular 4W   
-8 
+5 
-17 
+3.5 
E&M 4W enhanced 
-17 
+5 
-17 
+9 
FXS 
-5 
+5 
-17 
+1 
FXO 
-3.5 
+5 
-17 
+1 
 
E&M Interface 
Characteristics 
Signaling Method 
(User-Selectable) 
• EIA RS-464 Type I 
• EIA RS-464 Type II, III and V (British Telecom SSDC5) 
using internal -12 VDC in place of -48 VDC 
Note: For full support of Types II, III, and V (SSDC5) signaling 
standards, a -48 VDC supply is required.  
 
Dial Pulse Distortion 
±2 ms max 
FXS Interface 
Characteristics 
Signaling Modes  
EIA RS-464 loop-start and wink-start, user-selectable 
14. M-ETH, T3, Teleprotection and VC Modules 
 
On-Hook/Off-Hook 
Threshold  
(VIN = -20  to -54 VDC) 
• Off-hook state: 3V to 80% Vin between tip and ring 
• On-hook state: more than 83% Vin between tip and 
ring  
 
Feed Current 
24 mA (±10%) 
 
Ringer Characteristics
 
Ring Voltage  
 
• 54 VRMS with up to 1 REN load 
• 45 VRMS with up to 5 REN load 
• Protected against overload 
 
 
Ring Frequency  
22 Hz (±10%) 
 
 
Ring Cadence 
1 second ON, 3 seconds OFF 
 
Metering Pulse Generation 
(PCM only, special ordering 
options) 
12 kHz or 16 kHz (±2 Hz), user-selectable 
1.7 VRMS  
 
Reversal Polarity Pulse 
Distortion  
6 ms max 
FXO Interface 
Characteristics 
Signaling Modes  
EIA RS-464 loop-start and wink-start, user-selectable 
 
DC Resistance 
• Off-hook: 100 Ω at 100 mA feed, 230 Ω at 25 mA 
feed. 
• On-hook: more than 1 MΩ  
 
Ring Detector  
20 kΩ for 70 VRMS, 20 Hz ring signal 
 
Detection Thresholds 
• Detection:  > 20 VRMS, 17 to 25Hz 
• No detection:  < 5 VRMS 
 
Metering Pulse Detection 
Frequency (PCM only, 
special ordering options) 
12 kHz or 16 kHz (±200 Hz), user-selectable 
 
 
Reversal Polarity Pulse 
Distortion  
6 ms max 
End-to-End  
T1 Uplinks 
User-selectable sampling rate: 
Signaling 
 
Robbed Bit 
Multiframe  
(RBMF) 
Signaling  
• 667 samples per second with SF (D4) framing 
• 333 samples per second with ESF framing 
 
E1 Uplinks 
User-selectable as per ITU-T Rec. G.704, para. 3.3.32 
14. M-ETH, T3, Teleprotection and VC Modules 
Diagnostics 
 
• Local digital loopback  
• Remote digital loopback  
• Forward tone injection (1 kHz, 0 dBm0) 
• Backward tone injection (1 kHz, 0 dBm0) 
Connectors 
E&M Modules 
• VC-4, VC-4A, VC-8/RJ/POS/24: RJ-45 connector for 
each channel 
• VC-8, VC-8A: 68-pin female SCSI connector for all 
channels 
• VC-8/DS: two 68-pin female SCSI connectors, one for 
channels 1 to 4 and the other for channels 5 to 8 
• VC-16: two 68-pin female SCSI connectors, one for 
channels 1 to 8 and the other for channels 9 to 16 
 
FXO and FXS Modules 
• VC-4, VC-4A, VC-8A, VC-8/RJ: RJ-12 connector for 
each channel 
• VC-8, VC-16: One 50-pin female Telco connector for 
all channels  
Indicators  
E&M  Ports 
E-lead, M-lead indicators per channel 
 
FXS Ports 
Remote call and local off-hook indicators per channel 
 
FXO Ports 
Ring and remote off-hook indicators per channel 
Environment 
Operating Temperature 
-10°C to 55°C (14°F to 131°F)  
 
 
Storage Temperature 
-20°C to 70°C  (-4°F to 160°F)   
 
Humidity 
Up to 95%, non-condensing 
         Power Consumption 
 
See below 
Configuration 
Programmable via Megaplex system management 
Power Consumption (in Watt) from Megaplex Power Supply  
(without -48 VDC) 
Module vs Interface Type 
FXS  
FXO 
E&M 
VC-4 
2.5 
1.9 
2.8 
VC-4A 
3.3 
2.7 
3.6 
VC-8 
2.8 
2.0 
3.4 
14. M-ETH, T3, Teleprotection and VC Modules 
Module vs Interface Type 
FXS  
FXO 
E&M 
VC-8A 
3.7 
2.8 
4.2 
VC-16 
4.7 
2.5 
5.2 
Preparing the Module for Installation 
 
Warning 
Before performing any internal settings, adjustment, maintenance, or 
repairs, first disconnect all the cables from the module, and then remove the 
module from the Megaplex-4 enclosure. 
No internal settings, adjustment, maintenance, and repairs may be 
performed by either the operator or the user; such activities may be 
performed only by a skilled technician who is aware of the hazards involved. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. 
 
Caution 
The VC modules contain components sensitive to electrostatic discharge 
(ESD). To prevent ESD damage, always hold the module by its sides, and do 
not touch the module components or connectors. 
Installing a Module in the Chassis 
VC modules may be installed in an operating chassis (hot insertion). 
 
Warning 
A VC module starts operating as soon as it is inserted in an operating 
chassis. 
 
 To install a module in the chassis: 
6. Refer to the system installation plan and identify the prescribed module slot. 
Note 
When TDM group protection with inband management over E1 is needed in 
the chassis, do not install VC modules in I/O slot 6. 
7. Check that the fastening screws at the module sides are free to move. 
14. M-ETH, T3, Teleprotection and VC Modules 
8. Insert the module in its chassis slot and slide it in as far as possible. 
9. Secure the module by tightening its two fastening screws. 
10. The module starts operating as soon as it is plugged into an operating enclosure. At this stage, 
ignore the alarm indications. 
Connecting to Remote Equipment 
Before starting, identify the cables intended for connection to each port of this module, in accordance 
with the site installation plan.  
E&M Modules  
The VC-4/E&M and VC-4A/E&M module interfaces have four RJ-45 connectors.  
The following table lists the wiring of the RJ-45 connectors used for the VC-4/E&M and VC-4A/E&M 
modules. 
  RJ-45 Connector Wiring 
Pin 
Designation 
Function 
1 
SB 
Signaling battery 
2 
M 
M lead input 
3 
R1-OUT 
Voice output (4W) 
Voice input/output (2W) 
4 
R-IN 
Voice input (4W) 
5 
T-IN 
Voice input (4W) 
6 
T1-OUT 
Voice output (4W) 
Voice input/output (2W) 
7 
SG 
Function depends on signaling mode: 
• 
RS-464 Type I, III: Direct connection to signal ground 
• 
RS-464 Type V, SSDC5: Connection to signal ground 
through 1.2 kΩ resistor 
• 
RS-464 Type II: SG lead 
8 
E 
E lead output 
14. M-ETH, T3, Teleprotection and VC Modules 
Each group of VC-8/VC-8A/VC-16 eight channels is terminated in a 68-pin female SCSI connector located 
on the module panel. To connect these modules to user equipment by splitting a single VC-8/E&M or 
VC-16/E&M 68-pin SCSI connector, RAD offers the following families of splitter cables: 
• 
CBL-KVF8/E&M family: CBL-KVF8/E&M, CBL-KVF8/E&M/4METER, CBL-KVF8/E&M/10METER, 
CBL-KVF8/E&M/12METER, CBL-KVF8/E&M/25METER – Cables with 8 x RJ-45 connectors, 2m, 
4m, 10m, 12m, 25m long respectively 
• 
CBL-KVF8/E&M/OPEN family: CBL-KVF8/E&M/OPEN, CBL-KVF8/E&M/OPEN/4METER, CBL-
KVF8/E&M/OPEN/10METER, CBL-KVF8/E&M/OPEN/12METER, CBL-KVF8/E&M/OPEN/25METER 
– Open-end cables with stranded core, 2m, 4m, 10m, 12m, 25m long respectively 
• 
CBL-KVF8/E&M/OPEN/SOLID/12METER – Open-end cable with solid core, 12m long. 
CBL-KVF8/E&M Family Cables 
CBL-KVF8/E&M family are adapter cables terminated in eight RJ-45 male connectors, for direct 
connection of the individual channels to the user equipment. The following figure shows a general view 
of the CBL-KVF8/E&M cable, and the table below lists the cable wiring, together with functions of the 
individual connector pins. 
 
CBL-KVF8/E&M 
CBL-KVF8/E&M Cable Wiring and Connector Pin Functions 
Channel 
68-Pin SCSI 
Designation 
Function 
RJ-45 Connector 
1 
37 
SB 
Signaling Battery  
1 } Twisted Pair 
38 
M 
M Lead Input 
2 
1 
R-IN 
Voice Input (4-wire) 
4 } Twisted Pair 
2 
T-IN 
Voice Input (4-wire) 
5 
14. M-ETH, T3, Teleprotection and VC Modules 
Channel 
68-Pin SCSI 
Designation 
Function 
RJ-45 Connector 
3 
R1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
3 
} Twisted Pair 
4 
T1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
6 
35 
SG 
Signaling Ground  
7 } Twisted Pair 
36 
E 
E Lead Output 
8 
2 
43 
SB 
Signaling Battery  
1 } Twisted Pair 
44 
M 
M Lead Input 
2 
7 
R-IN 
Voice Input (4-wire) 
4 } Twisted Pair 
8 
T-IN 
Voice Input (4-wire) 
5 
9 
R1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
3 
} Twisted Pair 
10 
T1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
6 
41 
SG 
Signaling Ground  
7 } Twisted Pair 
42 
E 
E Lead Output 
8 
3 
49 
SB 
Signaling Battery  
1 } Twisted Pair 
50 
M 
M Lead Input 
2 
13 
R-IN 
Voice Input (4-wire) 
4 } Twisted Pair 
14 
T-IN 
Voice Input (4-wire) 
5 
15 
R1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
3 
} Twisted Pair 
16 
T1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
6 
47 
SG 
Signaling Ground  
7 } Twisted Pair 
48 
E 
E Lead Output 
8 
4 
55 
SB 
Signaling Battery  
1 } Twisted Pair 
56 
M 
M Lead Input 
2 
19 
R-IN 
Voice Input (4-wire) 
4 } Twisted Pair 
20 
T-IN 
Voice Input (4-wire) 
5 
14. M-ETH, T3, Teleprotection and VC Modules 
Channel 
68-Pin SCSI 
Designation 
Function 
RJ-45 Connector 
21 
R1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
3 
} Twisted Pair 
22 
T1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
6 
53 
SG 
Signaling Ground  
7 } Twisted Pair 
54 
E 
E Lead Output 
8 
5 
61 
SB 
Signaling Battery  
1 } Twisted Pair 
62 
M 
M Lead Input 
2 
25 
R-IN 
Voice Input (4-wire) 
4 } Twisted Pair 
26 
T-IN 
Voice Input (4-wire) 
5 
27 
R1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
3 
} Twisted Pair 
28 
T1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
6 
59 
SG 
Signaling Ground  
7 } Twisted Pair 
60 
E 
E Lead Output 
8 
6 
67 
SB 
Signaling Battery  
1 } Twisted Pair 
68 
M 
M Lead Input 
2 
31 
R-IN 
Voice Input (4-wire) 
4 } Twisted Pair 
32 
T-IN 
Voice Input (4-wire) 
5 
33 
R1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
3 
} Twisted Pair 
34 
T1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
6 
65 
SG 
Signaling Ground  
7 } Twisted Pair 
66 
E 
E Lead Output 
8 
7 
45 
SB 
Signaling Battery  
1 } Twisted Pair 
46 
M 
M Lead Input 
2 
5 
R-IN 
Voice Input (4-wire) 
4 } Twisted Pair 
6 
T-IN 
Voice Input (4-wire) 
5 
14. M-ETH, T3, Teleprotection and VC Modules 
Channel 
68-Pin SCSI 
Designation 
Function 
RJ-45 Connector 
11 
R1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
3 
} Twisted Pair 
12 
T1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
6 
39 
SG 
Signaling Ground  
7 } Twisted Pair 
40 
E 
E Lead Output 
8 
8 
57 
SB 
Signaling Battery  
1 } Twisted Pair 
58 
M 
M Lead Input 
2 
17 
R-IN 
Voice Input (4-wire) 
4 } Twisted Pair 
18 
T-IN 
Voice Input (4-wire) 
5 
23 
R1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
3 
} Twisted Pair 
24 
T1-OUT 
Voice Output (4-wire) 
Voice Input/Output (2-wire) 
6 
51 
SG 
Signaling Ground  
7 } Twisted Pair 
52 
E 
E Lead Output 
8 
CBL-KVF8/E&M/OPEN Family Cables 
CBL-KVF8/E&M/OPEN, CBL-KVF8/E&M/OPEN/4METER, CBL-KVF8/E&M/OPEN/10METER, CBL-
KVF8/E&M/OPEN/12METER and CBL-KVF8/E&M/OPEN/25METER are open-end splitter cables with 
stranded core, for connecting the SCSI-68 connector to the E&M user equipment. This cable includes 
one male SCSI-68 and 8 open-ended connectors. The cables are 2m, 4m, 10m, 12m and 25m long, 
respectively. See their drawing and pinout in the figure and table below. 
14. M-ETH, T3, Teleprotection and VC Modules 
 
CBL-KVF8/E&M/OPEN Cables 
CBL-KVF8/E&M/OPEN Pinout 
 
Open-Ended Connector Pin 
SCSI-68 
Connector Pin 
1 
Blue 
Signal Battery 
37 
White/Blue  
Signaling E Lead Output 
38 
Orange 
Voice Rx Input 
1 
White/Orange 
Voice Rx Input 
2 
Green  
Voice Tx Output 
3 
White/Green 
Voice Tx Output 
4 
Brown 
Signal GND 
35 
White/Brown 
Signaling E Lead Output 
36 
2 
Blue 
Signal Battery 
43 
White/Blue  
Signaling E Lead Output 
44 
Orange 
Voice Rx Input 
7 
14. M-ETH, T3, Teleprotection and VC Modules 
 
Open-Ended Connector Pin 
SCSI-68 
Connector Pin 
White/Orange 
Voice Rx Input 
8 
Green  
Voice Tx Output 
9 
White/Green 
Voice Tx Output 
10 
Brown 
Signal GND 
41 
White/Brown 
Signaling E Lead Output 
42 
3 
Blue 
Signal Battery 
49 
White/Blue  
Signaling E Lead Output 
50 
Orange 
Voice Rx Input 
13 
White/Orange 
Voice Rx Input 
14 
Green  
Voice Tx Output 
15 
White/Green 
Voice Tx Output 
16 
Brown 
Signal GND 
47 
White/Brown 
Signaling E Lead Output 
48 
4 
Blue 
Signal Battery 
55 
White/Blue  
Signaling E Lead Output 
56 
Orange 
Voice Rx Input 
19 
White/Orange 
Voice Rx Input 
20 
Green  
Voice Tx Output 
21 
White/Green 
Voice Tx Output 
22 
Brown 
Signal GND 
53 
White/Brown 
Signaling E Lead Output 
54 
5 
Blue 
Signal Battery 
61 
White/Blue  
Signaling E Lead Output 
62 
Orange 
Voice Rx Input 
25 
White/Orange 
Voice Rx Input 
26 
Green  
Voice Tx Output 
27 
White/Green 
Voice Tx Output 
28 
Brown 
Signal GND 
59 
White/Brown 
Signaling E Lead Output 
60 
6 
Blue 
Signal Battery 
67 
White/Blue  
Signaling E Lead Output 
68 
14. M-ETH, T3, Teleprotection and VC Modules 
 
Open-Ended Connector Pin 
SCSI-68 
Connector Pin 
Orange 
Voice Rx Input 
31 
White/Orange 
Voice Rx Input 
32 
Green  
Voice Tx Output 
33 
White/Green 
Voice Tx Output 
34 
Brown 
Signal GND 
65 
White/Brown 
Signaling E Lead Output 
66 
7 
Blue 
Signal Battery 
45 
White/Blue  
Signaling E Lead Output 
46 
Orange 
Voice Rx Input 
5 
White/Orange 
Voice Rx Input 
6 
Green  
Voice Tx Output 
11 
White/Green 
Voice Tx Output 
12 
Brown 
Signal GND 
39 
White/Brown 
Signaling E Lead Output 
40 
8 
Blue 
Signal Battery 
57 
White/Blue  
Signaling E Lead Output 
58 
Orange 
Voice Rx Input 
17 
White/Orange 
Voice Rx Input 
18 
Green  
Voice Tx Output 
23 
White/Green 
Voice Tx Output 
24 
Brown 
Signal GND 
51 
White/Brown 
Signaling E Lead Output 
52 
CBL-KVF8/E&M/OPEN/SOLID/12METER Cable 
CBL-KVF8/E&M/OPEN/SOLID/12METER is an open-end splitter cable with solid core, for connecting the 
SCSI-68 connector to the E&M user equipment. This cable includes one male SCSI-68 and one open-
ended connector. The cable is 12m (39.3 ft) long. See its drawing and pinout in the figure and table 
below. 
14. M-ETH, T3, Teleprotection and VC Modules 
 
CBL-KVF8/E&M/OPEN/12M Cable 
CBL-KVF8/E&M/OPEN/12M Pinout 
 
Open-Ended Connector Pin 
SCSI-68 
Connector Pin 
Notes 
1 
Blue 
Signaling M Lead Input 
38 
 
White 
Voice Rx Input 
1 
Twisted 
Orange 
Voice Rx Input 
2 
White 
Voice Tx Output 
3 
Twisted 
Green 
Voice Tx Output 
4 
Brown 
Signaling E Lead Output 
36 
 
2 
Gray 
Signaling M Lead Input 
44 
 
White 
Voice Rx Input 
7 
Twisted 
White/Blue 
Voice Rx Input 
8 
White 
Voice Tx Output 
9 
Twisted 
Orange/Blue 
Voice Tx Output 
10 
Green/Blue 
Signaling E Lead Output 
42 
 
3 
Brown/Blue 
Signaling M Lead Input 
50 
 
White 
Voice Rx Input 
13 
Twisted 
Gray/Blue 
Voice Rx Input 
14 
White 
Voice Tx Output 
15 
Twisted 
White/Orange 
Voice Tx Output 
16 
Orange/Green 
Signaling E Lead Output 
48 
 
4 
Orange/Brown 
Signaling M Lead Input 
56 
 
White 
Voice Rx Input 
19 
Twisted 
Gray/ Orange 
Voice Rx Input 
20 
White 
Voice Tx Output 
21 
Twisted 
White/Green 
Voice Tx Output 
22 
Green/Brown 
Signaling E Lead Output 
54 
 
14. M-ETH, T3, Teleprotection and VC Modules 
 
Open-Ended Connector Pin 
SCSI-68 
Connector Pin 
Notes 
5 
Gray/Green 
Signaling M Lead Input 
62 
 
White 
Voice Rx Input 
25 
Twisted 
White/Brown 
Voice Rx Input 
26 
White 
Voice Tx Output 
27 
Twisted 
Gray/Brown 
Voice Tx Output 
28 
White/Gray 
Signaling E Lead Output 
60 
 
6 
Blue 
Signaling M Lead Input 
68 
 
Yellow 
Voice Rx Input 
31 
Twisted 
Orange 
Voice Rx Input 
32 
Yellow 
Voice Tx Output 
33 
Twisted 
Green 
Voice Tx Output 
34 
Brown 
Signaling E Lead Output 
66 
 
7 
Gray 
Signaling M Lead Input 
46 
 
Yellow 
Voice Rx Input 
5 
Twisted 
White/Blue 
Voice Rx Input 
6 
Yellow 
Voice Tx Output 
11 
Twisted 
Orange/Blue 
Voice Tx Output 
12 
Green/Blue 
Signaling E Lead Output 
40 
 
8 
Brown/Blue 
Signaling M Lead Input 
58 
 
Yellow 
Voice Rx Input 
17 
Twisted 
Gray/Blue 
Voice Rx Input 
18 
Yellow 
Voice Tx Output 
23 
Twisted 
White/Orange 
Voice Tx Output 
24 
Orange/Green 
Signaling E Lead Output 
52 
 
Drain Wire 
Shell 
VC-8/E&M/DS module SCSI Connectors Pinout 
A special VC-8/E&M/DS module has two SCSI 68-pin connectors. The following table lists the connector 
pinout, together with functions of the individual connector pins. 
14. M-ETH, T3, Teleprotection and VC Modules 
 VC-8/E&M/DS SCSI Connector Pinout  
Channel 
68-Pin 
SCSI 
Designation 
 
Function 
1, 5 
37 
SB1 
Signaling Battery 
  
38 
M1 
M Lead Input 
  
1 
R-IN 
Voice Input (4-wire) 
  
2 
T-IN 
Voice Input (4-wire) 
  
3 
R1-OUT 
Voice Output (4-wire) 
  
Voice Input/Output (2-wire) 
  
4 
T1-OUT 
Voice Output (4-wire) 
  
Voice Input/Output (2-wire) 
  
35 
SG1 
Signaling Ground 
  
36 
E1 
E Lead Output 
  
61 
SB2 
Signaling Battery 
  
62 
M2 
M Lead Input 
  
59 
SG2 
Signaling Ground 
  
60 
E2 
E Lead Output 
2, 6 
43 
SB1 
Signaling Battery 
  
44 
M1 
M Lead Input 
  
7 
R-IN 
Voice Input (4-wire) 
  
8 
T-IN 
Voice Input (4-wire) 
  
9 
R1-OUT 
Voice Output (4-wire) 
  
Voice Input/Output (2-wire) 
  
10 
T1-OUT 
Voice Output (4-wire) 
  
Voice Input/Output (2-wire) 
  
41 
SG1 
Signaling Ground 
  
42 
E1 
E Lead Output 
  
67 
SB2 
Signaling Battery 
  
68 
M2 
M Lead Input 
14. M-ETH, T3, Teleprotection and VC Modules 
Channel 
68-Pin 
SCSI 
Designation 
 
Function 
  
65 
SG2 
Signaling Ground 
  
66 
E2 
E Lead Output 
3, 7 
49 
SB1 
Signaling Battery 
  
50 
M1 
M Lead Input 
  
13 
R-IN 
Voice Input (4-wire) 
  
14 
T-IN 
Voice Input (4-wire) 
  
15 
R1-OUT 
Voice Output (4-wire) 
  
Voice Input/Output (2-wire) 
  
16 
T1-OUT 
Voice Output (4-wire) 
  
Voice Input/Output (2-wire) 
  
47 
SG1 
Signaling Ground 
  
48 
E1 
E Lead Output 
  
45 
SB2 
Signaling Battery 
  
46 
M2 
M Lead Input 
  
39 
SG2 
Signaling Ground 
  
40 
E2 
E Lead Output 
4, 8 
55 
SB1 
Signaling Battery 
  
56 
M1 
M Lead Input 
  
19 
R-IN 
Voice Input (4-wire) 
  
20 
T-IN 
Voice Input (4-wire) 
  
21 
R1-OUT 
Voice Output (4-wire) 
  
Voice Input/Output (2-wire) 
  
22 
T1-OUT 
Voice Output (4-wire) 
  
Voice Input/Output (2-wire) 
  
53 
SG1 
Signaling Ground 
  
54 
E1 
E Lead Output 
  
57 
SB2 
Signaling Battery 
14. M-ETH, T3, Teleprotection and VC Modules 
Channel 
68-Pin 
SCSI 
Designation 
 
Function 
  
58 
M2 
M Lead Input 
  
51 
SG2 
Signaling Ground 
  
52 
E2 
E Lead Output 
FXS and FXO Modules  
The FXS and FXO versions of VC-8 have two modifications with different types of connectors: VC-8 and 
VC-8/RJ. 
The VC-4, VC-4A, VC-8A and VC-8/RJ module interface is terminated in four or eight RJ-12 connectors – 
one per channel.  
In the VC-16 and VC-8 modules, all module channels are terminated in a 50-pin female TELCO connector. 
RAD offers two adapter cables terminated in RJ-12 male connectors, for direct connection of the 
individual channels to user equipment: 
• 
CBL-VC16/FXSO, intended for use with VC-16/FXS and VC-16/FXO modules, which is terminated 
in 16 RJ-12 male connectors 
• 
CBL-VC8/FXSO, intended for use with VC-8/FXS and VC-8/FXO modules, which is terminated in 8 
RJ-12 male connectors. 
The following table lists the wiring of the RJ-12 connectors used for the FXO and FXS modules. 
  RJ-12 Connector Wiring 
Pin 
Function 
1, 2 
Not connected 
3 
Ring 
4 
Tip 
5, 6 
Not connected 
The following figure shows a general view of CBL-VC16/FXSO. CBL-VC8/FXSO is similar, except that it has 
only 8 RJ-12 connectors.  
14. M-ETH, T3, Teleprotection and VC Modules 
The following table lists the wiring of the CBL-VC16/FXSO cable, together with the functions of the VC-16 
module connector. For VC-8 modules and CBL-VC8/FXSO cables, only the pins assigned to channels 1 to 
8 are connected. 
 
CBL-VC16/FXSO, General View 
CBL-VC16/FXSO Cable Wiring and Connector Pin Functions 
Channel 
50-Pin TELCO 
Function 
RJ-12 Pin 
1 
12 } Twisted Pair 
Ring 
3 
13 
Tip 
4 
2 
9 } Twisted Pair 
Ring 
3 
10 
Tip 
4 
3 
6 } Twisted Pair 
Ring 
3 
7 
Tip 
4 
4 
49 } Twisted Pair 
Ring 
3 
50 
Tip 
4 
5 
46 } Twisted Pair 
Ring 
3 
47 
Tip 
4 
6 
24 } Twisted Pair 
Ring 
3 
25 
Tip 
4 
7 
3 } Twisted Pair 
Ring 
3 
4 
Tip 
4 
8 
26 } Twisted Pair 
Ring 
3 
27 
Tip 
4 
14. M-ETH, T3, Teleprotection and VC Modules 
Channel 
50-Pin TELCO 
Function 
RJ-12 Pin 
9 
29 } Twisted Pair 
Ring 
3 
30 
Tip 
4 
10 
21 } Twisted Pair 
Ring 
3 
22 
Tip 
4 
11 
18 } Twisted Pair 
Ring 
3 
19 
Tip 
4 
12 
15 } Twisted Pair 
Ring 
3 
16 
Tip 
4 
13 
43 } Twisted Pair 
Ring 
3 
44 
Tip 
4 
14 
40 } Twisted Pair 
Ring 
3 
41 
Tip 
4 
15 
37 } Twisted Pair 
Ring 
3 
38 
Tip 
4 
16 
34 
35 } Twisted Pair 
Ring  
Tip 
3 
4 
In harsh environments, such as heavy industry or electrical switching stations, it is recommended to use 
ferrite cores in order to reduce the effect of electromagnetic interference.  
The recommended ferrite core depends on the connector cable type. 
• 
For modules with RJ-12 connectors for each channel (VC-4, VC-4A, VC-8A, VC-8/RJ), use FAIR 
RITE catalog number 0443167251 or equivalent for small-diameter cables. The ferrite core must 
be installed on the cable close to the RJ-12 connector as shown below: 
• 
 
14. M-ETH, T3, Teleprotection and VC Modules 
• 
For modules with a single 50-pin female Telco connector for all channels (VC-8, VC-16) use FAIR 
RITE catalog number 0444173551 or equivalent. The ferrite core must be installed on the main 
cable as shown below: 
 
 
 To install the ferrite core on FXS/FXO modules: 
11. Run the cable through the open core. 
12. If cable thickness allows, wrap it around the core and run it through again. 
Allow no more than 2 inches (5 cm) between the core and the cable connector to the unit. 
13. Snap the core shut. 
14. Connect the cables into the appropriate connectors. 
Connecting the Cables to Module Connector  
Identify the cables intended for connection to each module connector, and connect them into the 
appropriate connectors. 
Caution 
When using a CBL-KVF8/E&M, CBL-VC16/FXSO or CBL-VC8/FXSO cable, pay 
attention not to touch the exposed contacts of RJ-45 or RJ-12 connectors. 
 
14. M-ETH, T3, Teleprotection and VC Modules 
When using any of the adapter cables listed above, plug each channel connector at the other end of the 
cable into the prescribed user’s equipment connector, in accordance with the site installation plan. 
Caution 
The E&M module ports have a HARDWARE default corresponding to EIA 
RS-464 type III signaling circuits (see diagram in E&M Equivalent Signaling 
Circuits). When the chassis is not powered and/or the module ports are not 
open, the module takes automatically this configuration. Using these modules 
for alternative applications (other than shown in E&M Equivalent Signaling 
Circuits) may result in a module failure or even damage. 
Connecting the Signaling and Feed Voltage Source 
The subscriber feed voltage used by FXS modules, or the -48 VDC signaling battery voltage used by 
E&M/EXT modules for full compliance with the EIA RS-464 Type II, III and V (BT SSDC5) signaling 
standards is supplied to the VC module from the chassis DC power distribution bus. 
The required -48 VDC voltage is always available when the Megaplex chassis is powered from a -48 VDC 
source.  
Caution 
Since an external voltage source can supply voltage even when the 
Megaplex is not operating, observe the following precautions: 
• 
Always turn off the external source, before the Megaplex chassis is turned 
off. 
• 
Never connect external DC voltages to modules installed in a Megaplex 
chassis if it is not operating. 
Do not connect/disconnect the ringer while it is operating.  
Normal Indications 
The module starts operating as soon as it is plugged into an operating Megaplex enclosure. During 
normal operation, the two indicators of each channel indicate the channel activity:  
• 
For E&M channels, the E and M indicators indicate the activity on the signaling leads of the 
corresponding channel 
• 
For FXO channels, the RING indicator lights when ringing is received from the local switch or PBX 
on the corresponding channel, and the REM indicator lights when the remote subscriber is in the 
off-hook state 
14. M-ETH, T3, Teleprotection and VC Modules 
• 
For FXS channels, the REM indicator lights when a call initiated by the subscriber connected to 
the remote side is being handled by the corresponding channel, and the LOC indicator lights 
when the local subscriber is in the off-hook state. 
Configuration Considerations 
General Module Parameters 
Each VC port can be independently configured in accordance with the system requirements. However, 
some configurable parameters pertain to the entire VC module and/or to groups of ports.  
The following parameters must be set to the same value for all the module ports:  
• 
meter-rate (FXS/FXO modules) 
• 
coding  
• 
signaling  
• 
compression (VC-4A/VC-8A). 
The following parameters must be set to the same value for a group of ports:  
• 
analog-signaling (FXS/FXO modules, for each group of 8 ports) 
• 
signaling-feedback (FXO modules, for each group of 8 ports) 
• 
e-m-type (for each group of four channels 1, 2, 3, 4; 5, 6, 7, 8; etc) 
• 
wires (E&M modules, for each pair of channels (1, 2; 3, 4; etc.) 
This is done by forcing the last choice to all the module/group ports. 
Selection of Transmit and Receive Levels  
Transmit Level (tx-gain) selects the nominal input level of the transmit path. The input level can be set in 
0.5 dB steps in the range defined by Transmit and Receive Levels for Various Interfaces. 
Select the transmit level to match the transmission level point (TLP-transmit) of the equipment 
connected to the channel. The following figure explains how to determine the required level setting. 
Note that the application of an input signal at the nominal transmit level results in a 0 dBm digital level, 
and a far-end output signal equal to the far-end nominal receive level. 
14. M-ETH, T3, Teleprotection and VC Modules 
Receive Level (rx-sensitivity) selects the nominal output level of the receive path. The output level can 
be set in 0.5 dB steps in the range defined by Transmit and Receive Levels for Various Interfaces Error! 
Reference source not found.. Select the receive level to match the TLP-receive of the equipment 
connected to the channel: 
Transmit TLP:
-8dB
Receive TLP:
-2dB
VC Channel
 
Transmit
Input Circuit
Receive
Output Circuit
   T
   R
   T1
   R1
Signal
Processor
 
 
Adjust level (Tx Gain) to -8dBm
Adjust level (Rx Sensitivity) to -2dBm
 
Nominal Level
= 0 dBm
 
 Selection of Transmit and Receive Levels 
Configuring DS0 Cross-Connect  
The routing of the individual port timeslots (timeslot assignment) is configured via ds0 cross-connect. 
You can assign only timeslots of ports that have already been configured, and are configured as no 
shutdown.  
Timeslots can be assigned to the following ports: 
• 
External E1/T1 ports of any I/O module 
• 
Internal E1/T1 ports of any I/O or CL module  
• 
DS1 and PW ports of the MPW-1 or VS module  
The VC-4/8/16 modules use 64 kbps PCM encoding, and therefore require one uplink timeslot per voice 
channel. The user can freely route each voice channel to any uplink port. The voice channel data is 
provided in DS-0 (8 bits) compatible format, permitting voice channel routing by DACS cross-connect 
systems.  
The VC-4A/8A modules require one aggregate timeslot per voice channel in PCM mode, or one timeslot 
per pair of voice channels in ADPCM mode. The uplink bandwidth required by a module depends on the 
encoding method, PCM or ADPCM:  
14. M-ETH, T3, Teleprotection and VC Modules 
• 
With PCM encoding, the modules require one uplink timeslot, per voice channel, and provide 
the data in a DS-0 (8-bits) compatible format, permitting voice channel switching in a DACs-
based cross-connect system. When working with PCM encoding, use ds0 command. 
• 
With ADPCM encoding, the module requires only one uplink timeslot for each pair of voice 
channels. Note that consecutive channels (e.g. CH 1–2,  
3–4, … 15-16) must be assigned to share the same timeslot). When working with ADPCM 
encoding, use split-ts command. 
OOS Signaling  
When choosing the OOS signaling option in the modules with E1/E1-i/T1/T1-i/DS1 ports working in one 
chassis with VC modules (see E1 Ports, T1 Ports or DS1 Ports in Chapter 5), take into account the 
following:   
• 
force-idle and busy-idle options are suitable for use with all the VC module types. 
• 
force-busy and idle-busy options are suitable for use with E&M and FXO modules, but not with 
FXS modules. 
Handling of Signaling Information  
The VC modules automatically adapt the generation and interpretation of the signaling information to 
their analog interface type (E&M, FXS or FXO) and to the signaling mode selected by the user (loop-start 
or wink-start). 
The following sections describe the handling of the signaling information in VC modules. 
Signaling Methods 
You can select the format of the signaling information generated by VC modules in accordance with the 
application requirements. 
The signaling information of each channel is carried by means of up to four bits (signaling bits), 
designated by the applicable standards as bits A, B, C, and D. The number of bits actually available for 
carrying signaling information, and the data rate at which signaling information can be transferred, 
depend on the uplink type (E1 or T1), the framing mode and the encoding type (PCM or ADPCM) being 
used:  
• 
For E1 trunks with G.732N framing, no signaling information is transmitted. 
• 
For E1 trunks with G.732S framing, which use a 16-frame multiframe structure, the standard 
signaling method is Channel Associated Signaling (CAS). In the PCM mode, timeslot 16 carries 
14. M-ETH, T3, Teleprotection and VC Modules 
four signaling bits for each payload timeslot. In ADPCM mode two signaling bits are available for 
each channel. 
• 
For T1 trunks with ESF framing, which use a 24-frame multiframe structure, the standard 
signaling method is inband Robbed Bit Multiframe (RBMF) signaling. The ESF multiframe 
structure includes four signaling bits for each payload timeslot. When this method is used, the 
least significant bit of each channel is periodically overwritten with signaling information. In 
ADPCM mode two signaling bits are available for each channel. 
• 
T1 trunks with SF (D4) framing, which use a 12-frame multiframe structure, also use the RBMF 
signaling method. Because of the shorter multiframe structure, in this case only two signaling 
bits (A and B) are available for each payload timeslot. In ADPCM mode only one signaling bit is 
available for each channel. 
• 
RAD Proprietary “Robbed Bit Frame” (RBF) signaling, applicable for both E1 and T1 trunks, 
avoids the need for multiframe synchronization. This method allocates the least significant bit of 
each channel to its own signaling information. Therefore, signaling is transparently transferred 
within the timeslot carrying the encoded audio signal, but because PCM encoding is effectively 
done with 7-bit resolution, there is a slight decrease in transmission quality. This proprietary 
method allows the transmission of 31 voice channels by a Megaplex system with E1 links, when 
using G.732N framing. The RBF option is used for VC-4A/VC-8A modules only.  
For applications which do not require end-to-end signaling, or can use only inband signaling (e.g., 
DTMF), the user can disable the transfer of signaling information. 
For your convenience, the following table lists the number of signaling bits as a function of voice 
encoding and framing method.  
Number of Available Signaling Bits 
Voice  
Encoding 
Signaling Type 
G.732S 
G.732N 
ESF 
SF (D4) 
PCM 
CAS 
4 
Not supported 
Not supported 
Not supported 
 
Robbed Bit Multiframe 
(RBMF) 
Not supported 
Not supported 
4 
2 
 
Robbed Bit Frame (RBF) 
1 
1 
1 
1 
ADPCM 
CAS 
2 
Not supported 
Not supported 
Not supported 
 
Robbed Bit Multiframe 
(RBMF) 
Not supported 
Not supported 
2 
1 
 
Robbed Bit Frame (RBF) 
1 
1 
1 
1 
14. M-ETH, T3, Teleprotection and VC Modules 
Signaling for ADPCM Mode 
The signaling is slightly different when using ADPCM voice encoding: 
• 
With E1 trunks – timeslot 16 consists of four bits –A, B, C, D (as in PCM) – for a specific timeslot. 
However, since in ADPCM mode each channel requires only half a timeslot, the first two bits 
serve the first channel and the last two bits serve the second channel.  
A
B
A
B
CH1
A
B
A
B
CH2
CH(N)
CH(N+1)
TS1
TS17
 
• 
With T1 trunks – the A, B, C and D bits of each channel are transmitted through the following 
frames: 
 
ESF Framing: 6,12,18 and 24. Each channel has two signaling bits. 
 
SF Framing:  6 and 12 only. Each channel has a single signaling bit. 
B
A
CH1
A
B
CH1
CH2
CH2
Frame
6
Frame
12
Frame
18
Frame
24
In ESF Mode Only
 
Note 
When VC modules operate in ADPCM mode and RBMF signaling with T1 links 
in the SF framing mode, the Tx/Rx Translation of the M8T1 module must be 
configured in accordance with T1/SF Link Signaling Profile for Working with 
ADPCM Modules. 
Signaling Information  
The signaling information exchanged by the channels of VC modules is used for the following purposes: 
• 
Determine the state of the E and M leads 
• 
Report the detection of on-hook/off-hook conditions, and control DC closure across the line 
• 
Report the detection of ringing and control the sending of ringing 
14. M-ETH, T3, Teleprotection and VC Modules 
• 
Control the generation and detection of feed voltage polarity reversal (PCM mode only) 
• 
Control the generation and detection of metering pulses (PCM mode only) 
Each type of VC module generates and interprets signaling information in accordance with the analog 
interface type (E&M, FXS or FXO) and the signaling mode selected by the user (loop-start or wink-start).  
The format of the signaling information generated by a VC module operating in the PCM mode, which 
depends on the analog interface type (E&M, FXS or FXO) and the signaling mode (loop-start or wink-
start), is given in the following tables. The identification of the signaling bit states is consistent with the 
Megaplex default profile designations.  
 Default Signaling Bit States for E&M Modules (PCM mode) 
Direction 
Analog Interface 
State 
Signaling Bits 
A 
B 
C 
D 
Tx 
On-Hook 
0 
1 
0 
1 
Off-Hook 
1 
1 
0 
1 
Rx 
Ring 
1 
X 
X 
X 
No Ring 
0 
X 
X 
X 
 Default Signaling Bit States for FXS Modules (PCM mode) 
Signaling 
Mode  
Direction 
Analog Interface State 
Signaling Bits 
A 
B 
C 
D 
Loop Start 
Tx 
On-Hook 
0 
1 
0 
1 
Off-Hook 
1 
1 
0 
1 
Rx 
Ring 
1 
X 
X 
X 
No Ring 
0 
X 
X 
X 
Wink Start 
Tx 
On-Hook 
0 
1 
0 
1 
Off-Hook 
1 
1 
0 
1 
Rx 
Ring 
1 
 
 
X 
No Ring 
0 
 
 
X 
Reversed Polarity 
 
0 
0 
X 
Not Reversed Polarity 
 
1 
0 
X 
14. M-ETH, T3, Teleprotection and VC Modules 
Metering Pulse 
 
1 
1 
X 
No Metering Pulse 
 
1 
0 
X 
 Default Signaling Bit States for FXO Modules (PCM mode) 
Signaling 
Mode 
Direction 
Analog Interface State 
Signaling Bits 
A 
B 
C 
D 
Loop Start 
Tx 
No Ring 
0 
1 
0 
1 
Ring Detected 
1 
1 
0 
1 
Rx 
Remote On-Hook 
0 
X 
X 
X 
Remote Off-Hook 
1 
X 
X 
X 
Wink Start 
Tx 
No Ring 
0 
 
 
1 
Ring Detected 
1 
 
 
1 
Reversed Polarity 
 
0 
0 
1 
Not Reversed Polarity 
 
1 
0 
1 
Metering Pulse 
 
1 
1 
1 
No Metering Pulse 
 
1 
0 
1 
Rx 
Remote On-Hook 
0 
X 
X 
X 
Remote Off-Hook 
1 
X 
X 
X 
 
 
 
 Default Signaling Bit States in ADPCM Mode 
Direction 
Analog Interface 
State 
Signaling Bits 
 
 
A1 
B1 
A2 
B2 
Tx 
On-Hook 
0 
1 
0 
1 
 
Off-Hook 
1 
1 
1 
1 
Rx 
Ring 
1 
x 
1 
x 
 
No-Ring 
0 
x 
0 
x 
 
Note 
In the tables above, X indicates that the corresponding bit is not relevant. 
14. M-ETH, T3, Teleprotection and VC Modules 
 
Note 
In most applications, the user need not be concerned with the issue of 
signaling information. 
Signaling Profiles (M8E1, M8T1, M8SL) 
The additional flexibility needed to meet the requirements of special applications is provided by means 
of signaling profiles, which control the processing of signaling information received and transmitted by 
each uplink:  
• 
A signaling profile enables the user to select the translation of each individual signaling bit. The 
available selections are A, B, C, D (value copied from the corresponding incoming bit), ~A, ~B, 
~C, ~D (inverted value of corresponding incoming bit), 0 (always 0), and 1 (always 1). 
• 
In addition to the translation of individual bits, the receive path conversion section can also be 
used to define the signaling bit patterns that indicate the busy and idle states. 
Signaling Feedback 
Certain types of PBX and central office switches require confirmation that the signaling information has 
been received, a function referred to as signaling-feedback in the Megaplex CLI.   
Signaling feedback can be enabled only for FXO modules. For VC-4, VC-4A, VC-8 and VC-8A modules, the 
selection is made for the entire group of all the module channels. For VC-16/FXO modules, the function 
can be separately enabled on each group of eight channels (1 to 8 and 9 to 16). 
Configuration Sequence 
The list of tasks that can be performed on the VC modules and the recommended configuration 
sequence are described in the table below. For detailed descriptions, refer to Chapter 5. The second 
column indicates the configuration context for this task, under which it can be found in Chapter 5. The 
third column refers to the reference tables that should be consulted when planning the module 
operation. 
Task 
Configuration Context 
Reference  
Configuring a VC module and putting it 
into service 
configure>slot>card-type  
card-type=voice {vc4fxs | vc4fxo | 
vc4e-m | vc8fxs | vc8fxo | vc8e-m 
| vc16fxs | vc16fxo | vc16e-m } 
Configuring the voice port parameters  
configure>port>voice 
 
14. M-ETH, T3, Teleprotection and VC Modules 
Task 
Configuration Context 
Reference  
Configuring DS0 cross-connect (timeslot 
assignment for PCM voice ports) 
configure>cr>ds0 
To find which ports on which modules 
can be cross-connected with PCM 
voice ports, see Cross-Connect Table in 
Chapter 8.  
Configuring split timeslot cross-connect 
(timeslot assignment for ADPCM voice 
ports) 
configure>cr>split-ts 
To find which ports on which modules 
can be cross-connected with ADPCM 
voice ports, see Cross-Connect Table in 
Chapter 8. 
Monitoring and Diagnostics  
The test and diagnostics functions available on each module channel are: 
• 
Local digital loopback  
• 
Remote digital loopback  
• 
Forward tone injection 
• 
Backward tone injection. 
For more detail, see Voice Ports  in Chapter 5. 
Troubleshooting  
The test tone injection functions and the loopbacks available on the VC module provide a rapid and 
efficient way to identify the general location of a fault in either of the two VC modules connected in a 
link, in the external equipment, or in the connections to the channels.  
If a complaint is received from one of the subscribers connected to the VC channels, first activate the VC 
local test loop at the side where the complaint comes from. The local subscriber must receive its own 
signal. 
If the signal is not received, the problem is at the local end: 
• 
Check the connections to the subscriber equipment. 
• 
Replace the local VC module. 
If the local subscriber receives its own signal when the local loop is activated, activate test tone injection 
toward the complaining subscriber. If the subscriber receives the test tone, the problem is probably in 
14. M-ETH, T3, Teleprotection and VC Modules 
the connections at the remote side (the side that sends the tone). You can check the computer path of 
the remote module channel by activating the remote loopback and the tone injection toward the 
remote subscriber, and checking that the local subscriber receives the test tone. 
If the problem is not corrected, the procedure must be repeated at the other side of the link. Deactivate 
the local loop and activate the remote loop on the remote Megaplex unit. 
 
 
 
 
 