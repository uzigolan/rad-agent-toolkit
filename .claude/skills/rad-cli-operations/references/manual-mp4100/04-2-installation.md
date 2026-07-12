# 2 Installation

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 120–162.*


## 2 Installation  *(p.120)*

This chapter provides installation instructions for Megaplex-4 devices.  
The chapter presents the following information: 
• 
General description of equipment enclosure and its panels. 
• 
Mechanical and electrical installation instructions for the enclosure itself and for system 
modules, that is, PS and CL modules. 
After installing the system, it is necessary to configure it in accordance with the specific user's 
requirements:  
• 
The preliminary system configuration is always performed by means of a supervision terminal 
(procedures for using the terminal are given in Chapter 4). The software necessary for using the 
terminal is stored in the CL module: if the CL module is not yet loaded with the required 
software, refer to Chapter 12 for detailed software installation instructions. 
• 
After the preliminary configuration, the system can also be managed by means of Telnet hosts 
and/or SNMP-based network management stations, e.g., RADview. Refer to the User's Manual 
of the network management station for operating instructions. 
2.1 Storage and Transportation 
This product fulfills several environmental conditions, such as ambient temperatures and relative 
humidity levels. These conditions apply to storage, transportation, and stationary operation of the 
equipment. You can find specifications about these environmental conditions in the Technical 
Specifications section. 
 
 
Warning 
Ensure that your site meets the required ambient temperatures and relative 
humidity levels to store, transport, and operate the equipment. Failing to do 
so may damage the equipment. 
2. Installation 
Power supplies stored in warehouse and unoperated for more than 24 months, need to undergo a 
periodic activation for component rejuvenation, once every 24 months.  
Run the periodic activation for 4 hours with a 50% load of the maximum power. 
There are two methods for loading the power supply with 50% power during the start-up process:  
• 
Connecting the power supply to a compatible product and running it. 
• 
Connecting the power supply to a variable electronic load and setting the load intensity to 50%. 
For products with two power supplies, first remove one of the power supplies to allow the product to 
run only with the remaining power supply. 
After the process is completed, place a sticker on the power supply, containing: 
Maintenance cycle performed by: _________ 
Date of the next maintenance cycle: _____________ 
For boxes containing a large number of power supplies, place the sticker on the outer box. 
 
 
Warning 
RAD products must be transported to installation sites in their original 
packaging. Failing to do so may damage the equipment and voids the 
warranty. 
2.2 Safety 
Safety Precautions 
 
Warning 
No internal settings, adjustment, maintenance, and repairs may be 
performed by either the operator or the user; such activities may be 
performed only by a skilled technician who is aware of the hazards involved. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. 
 
 
2. Installation 
Caution 
Megaplex-4 modules contain components sensitive to electrostatic 
discharge (ESD). To prevent ESD damage, always hold the module by its 
sides, and do not touch the module components or connectors.  
Delicate electronic components are installed on both sides of the printed 
circuit boards (PCBs) of the Megaplex-4 modules. To prevent physical 
damage: 
• 
Always keep modules in their protective packaging until installed in the 
Megaplex-4 chassis, and return them to the packaging as soon as they 
are removed from the enclosure.  
• 
Do not stack modules one above the other, and do not lay any objects 
on PCBs. 
When inserting a module into its chassis slot, align it carefully with the 
chassis slot guides, and then push it in gently. Make sure the module PCB 
does not touch the adjacent module, nor any part of the chassis. If 
resistance is felt before the module fully engages the mating backplane 
connector, retract the module, realign it with the slot guides and then insert 
again. 
 
 
Warning 
Before connecting this product to a power source, make sure to read the 
Handling Energized Products section at the beginning of this manual. 
Grounding  
 
Grounding 
For your protection and to prevent possible damage to equipment when a 
fault condition, e.g., a lightning stroke or contact with high-voltage power 
lines, occurs on the lines connected to the equipment, the Megaplex-4 case 
must be properly grounded (earthed) at any time. Any interruption of the 
protective (grounding) connection inside or outside the equipment, or the 
disconnection of the protective ground terminal can make this equipment 
dangerous. Intentional interruption is prohibited.  
 
2. Installation 
 
Warning 
Dangerous voltages may be present on the electrical cables connected to 
the Megaplex-4 and its modules. 
• 
Never connect cables to Megaplex-4 if not properly installed and 
grounded. 
• 
Disconnect all the cables connected to the electrical connectors of the 
Megaplex-4 before disconnecting its grounding connection.  
Before connecting any other cable and before applying power to this equipment, the protective ground 
(earth) terminal of the equipment must be connected to protective ground. Megaplex-4 grounding 
terminals are located on the Megaplex-4 PS module panels.  
Whenever Megaplex-4 units are installed in a rack, make sure that the rack is properly grounded and 
connected to a reliable, low-resistance grounding system, because the rack can also provide a 
connection to ground. 
In addition, the grounding connection is also made through each one of the AC power cables. Therefore, 
the AC power cable plug must always be inserted in a socket outlet provided with a protective ground. 
Laser Safety  
 
Warning 
Megaplex-4 modules may be equipped with a laser diode. In such cases, a 
label with the laser class and other warnings as applicable will be attached 
near the optical transmitter. The laser warning symbol may also be 
attached.  
For your safety: 
• 
Before turning on the equipment, make sure that the fiber optic cable is 
intact and is connected to the optical transmitter. 
• 
Do not use broken or unterminated fiber-optic cables/connectors. 
• 
Do not  look straight at the laser beam and into the optical connectors 
while the unit is operating.  
• 
Do not attempt to adjust the laser drive current. 
• 
The use of optical instruments with this product will increase eye 
hazard. Laser power up to 1 mW at 1300 nm and 1550 nm could be 
collected by an optical instrument. 
• 
Use of controls or adjustment or performing procedures other than 
those specified herein may result in hazardous radiation exposure.  
ATTENTION:  The laser beam may be invisible!  
2. Installation 
Megaplex-4 modules equipped with laser devices provided by RAD comply with laser product performance 
standards set by governmental agencies for Class 1 laser products. The modules do not emit hazardous light, 
and the beam is totally enclosed during all operating modes of customer operation and maintenance.  
In some cases, the users may insert their own SFP laser transceivers into Megaplex-4 modules. Users are 
alerted that RAD cannot be held responsible for any damage that may result if non-compliant 
transceivers are used. In particular, users are warned to use only agency approved products that comply 
with the local laser safety regulations for Class 1 laser products. 
Wherever applicable, Megaplex-4 modules are shipped with protective covers installed on all the optical 
connectors. Do not remove these covers until you are ready to connect optical cables to the connectors. 
Keep the covers for reuse, to reinstall the cover over the optical connector as soon as the optical cable is 
disconnected.  
Protection against ESD 
Electrostatic discharge occurs between two objects when an object carrying static electrical charges 
touches, or is brought near enough, the other object.  
Static electrical charges appear as result of friction between surfaces of insulating materials, separation 
of two such surfaces, and may also be induced by electrical fields. Routine activities such as walking 
across an insulating floor, friction between garment parts, friction between objects, etc. can easily build 
charges up to levels that may cause damage, especially when humidity is low. 
Caution 
Megaplex-4 modules contain components sensitive to electrostatic 
discharge (ESD). To prevent ESD damage, always hold a module by its sides, 
and do not touch the module components or connectors. If you are not using 
a wrist strap, before touching a module, it is recommended to discharge the 
electrostatic charge of your body by touching the frame of a grounded 
equipment unit.  
Whenever feasible, during installation works use standard ESD protection wrist straps to discharge 
electrostatic charges. It is also recommended to use garments and packaging made of antistatic 
materials or materials that have high resistance, yet are not insulators. 
2. Installation 
2.3 Site Requirements and Prerequisites 
AC Power Requirements  
AC-powered Megaplex-4 units should be installed within 1.5m (5 feet) of an easily-accessible grounded AC 
outlet capable of furnishing 150/230 VAC (nominal), 50/60 Hz.  
Caution 
Use only the power cord supplied with the product.   
安全のために付属の電源コード以外を使用したり、付属の電源コードを他の
製品に使用したりしないでください。 
DC Power Requirements  
DC-powered Megaplex-4 units require a -48 VDC (-36 to -56 VDC) power source (in accordance with the 
nominal mains voltage of the ordered PS module).  
Caution 
• 
Megaplex-4 PS modules have no power switch and start operating as 
soon as power is applied. Therefore, an external power ON/OFF switch 
is required (for example, the circuit breaker that protects the power line 
can also serve as an ON/OFF switch). 
• 
Internal jumpers on the DC PS modules can be set to match operational 
requirements that need either the + (positive) or – (negative) terminal of 
the power source to be grounded. The normal factory setting is for a 
power source with the +(positive) terminal grounded (the power supply 
module jumpers are installed in the BGND=FGND and GND=FGND 
positions). When it is necessary to use a power source with the – 
(negative) terminal grounded, or a floating power source, the jumpers 
must be disconnected (set to NO). 
Check the position of jumpers in the Megaplex-4 power supply module 
(see Typical Megaplex-4100 PS Module (Lateral View), Location of 
Internal Jumpers and Typical Megaplex-4104 PS Module (Top View), 
Location of Internal Jumpers) before connecting the DC supply voltage.  
Certain I/O modules may still cause BGND to be connected to FGND or 
GND, even after setting the jumpers to NO. Refer to the Installation and 
Operation Manuals of the modules installed in the chassis for proper 
setting of their ground-control jumpers.  
2. Installation 
• 
If the Megaplex-4 chassis must be operated with floating ground, it may 
also be necessary to disconnect the ground reference on the power 
supply modules, and check the ground and shield wiring on the cables 
connected to the chassis. This may require replacing the cables with 
cables suitable to your specific application. 
• 
Megaplex-4 chassis must always be connected to FGND (protective 
ground). 
Special ordering options with preconfigured floating ground settings are 
available. Contact your local RAD Partner for more information. When 
working with FXS voice modules, see also the VC-4/4A/8/8A/16 section in 
Appendix B.  
Front and Rear Panel Clearance 
Allow at least 90 cm (36 inches) of frontal clearance for operator access. Allow the same clearance at the 
rear of the unit for interface cable connections and module replacement. 
Ambient Requirements 
Megaplex-4100 – Regular Chassis  
The Megaplex-4100 I/O modules are cooled by free air convection.  
The ambient operating temperature range of Megaplex-4100 is -10 to +55°C (14 to 131°F), at a relative 
humidity of up to 95%, non-condensing. The storage temperature is -20°C to +70°C (-4°F to +160°F). 
Actual operating temperature range is determined by the specific modules installed in the chassis. 
The Megaplex-4100 chassis has no fans and is cooled mainly by free air convection. Cooling vents are 
located in the bottom and upper covers. Do not obstruct these vents. When the chassis is installed in a 
19" rack, allow at least 1U of space below and above the unit. 
The PS power supply modules have a miniature cooling fan installed on their front panels: this fan 
operates only when the temperature is high.  
CL.2 modules also have internal fans.  
2. Installation 
Megaplex-4100 – IEEE-1613 Compliant Chassis  
RAD offers a special Megaplex-4100 IEEE-1613 Compliant chassis. This chassis includes a heat sink on the 
front panel and two special fixtures replacing the vertical walls of the CL module slots to allow more 
airflow into the CL modules. These fixtures use I/O 5 and I/O 6 slots, on both sides of CL modules. 
To fully comply with IEEE-1613 standard including “No Fans operation”, this chassis must be ordered 
with special options of CL and PS system modules.  
The I/O modules supported in this chassis are as follows: 
• 
VS, T3 modules (all flavors)  
• 
M-ETH, TP (specific flavors).  
The following modules do not require a special ordering option: 
• 
VS 
• 
T3  
• 
TP/CV/SSR. 
The rest of the supported modules require a special ordering option (if needed, please contact your local 
RAD Business Partner).   
Megaplex-4104  
The Megaplex-4104 chassis has 2 cooling fans on its right side. Do not obstruct these vents. When the 
chassis is installed in a 19" rack, allow at least 10 cm of spacing at the sides of the device. 
The Megaplex-4104 PS power supply and CL.2 modules do not include fans.  
The ambient operating temperature range of Megaplex-4104 is -10 to +55°C (14 to 131°F), at a relative 
humidity of up to 95%, non-condensing. The storage temperature is -20°C to +70°C (-4°F to +160°F). 
Actual operating temperature range is determined by the specific modules installed in the chassis.  
Electromagnetic Compatibility Considerations 
The Megaplex-4 is designed to comply with the electromagnetic compatibility (EMC) requirements of 
Sub-Part J of FCC Rules, Part 15, for Class A electronic equipment, and additional applicable standards 
such as EN55022 and EN55024. Megaplex-4 also complies with all the requirements of the CE mark. 
To meet these standards, it is necessary to perform the following actions: 
2. Installation 
• 
Connect the Megaplex-4 case to a low-resistance grounding system. 
• 
Install blank panels to cover all empty slots. Appropriate blank panels can be ordered from RAD. 
• 
Whenever possible, use shielded telecommunication cables. In particular, it is recommended to 
use a shielded RS-232 to connect to the CL module serial control port. 
Note 
The serial control port is normally used only during preliminary configuration, 
and for maintenance purposes. If you cannot obtain a shielded control cable, 
connect the cable only for the minimum time required for performing the task.  
• 
In certain cases, the use of shielded cables or twisted pairs, or use of ferrite cores, is 
recommended. Refer to the individual module Installation and Operation Manual for details. 
 
Warning 
Covering all empty slots is also required for reasons of personal safety. 
 
Optical Cable Requirements 
The cables connected to Megaplex-4 optical ports should use 2-mm optical fibers terminated in the 
corresponding type of connectors. When routing fibers, make sure to observe the minimum bending 
radius (35 mm). RAD recommends installing plastic supports on each cable connector: these supports 
determine the fiber bending radius at the connector entry point and also prevent stress at this point. 
Protection from Hazards 
You may have to open a unit for servicing or hot swapping of power supplies. Therefore, it is 
recommended to install the unit in an area that takes into consideration water, moisture, dust, smoke, 
chemicals, noise, pollution, and electromagnetic interference. 
2.4 Package Contents 
Megaplex-4100 Package Contents 
The Megaplex-4100 package (P/N beginning with MP-4100-2) includes the following items: 
• 
Megaplex-4100 chassis, including CL and PS modules in accordance with order  
2. Installation 
• 
Power cables in accordance with order (for the DC power cable, also includes a DC plug) 
• 
Supervision terminal cable, CBL-DB9F-DB9M-STR 
• 
Rack installation kit in accordance with order: 
 
RM-MP-MX-23/19: hardware kit for installing one Megaplex-4100 in either a 19-inch or 23-
inch rack 
 
MP-2100-RM-ETSI/19: hardware kit for installing one Megaplex-4100 in a 23-inch ETSI rack 
(can also be used for installation in 19-inch rack)  
• 
Air buffer for installation of the Megaplex-4100 IEEE-1613 chassis (if ordered) 
• 
Manual download form. 
I/O modules are shipped either separately, or preinstalled in the chassis, in accordance with your order. 
Megaplex-4104 Package Contents 
The Megaplex-4104 package (P/N beginning with MP-4104-2) includes the following items: 
• 
Megaplex-4104 chassis, including CL and PS modules in accordance with order 
• 
Power cables in accordance with order, and a DC plug for the DC power cable 
• 
Supervision terminal cable, CBL-MUSB-DB9F  
• 
Open-ended alarm cable, CBL-MP-4104/AR/OPEN/2M 
• 
Rack installation kit in accordance with order:  
 
RM-42: hardware kit for installing one Megaplex-4104 in a 19-inch rack (supplied with the 
device) 
 
RM-42-CM: hardware kit for installing one Megaplex-4104 in a 19-inch rack  with cable 
management 
 
WM-42: wall-mounting kit for installing Megaplex-4104  
 
WM-42-CM: wall-mounting kit for installing Megaplex-4104  with cable management 
• 
Manual download form. 
I/O modules are shipped either separately, or preinstalled in the chassis, in accordance with your order. 
2. Installation 
2.5 Required Equipment  
The additional cables you may need to connect to the Megaplex-4 device depend on the Megaplex-4 
application.  
You can use standard cables or prepare the appropriate cables yourself in accordance with the 
information given in Appendix A, and in the Installation and Operation Manuals of the installed 
modules.  
2.6 Mounting the Products 
This section presents instructions for installing Megaplex-4 units. To help you familiarize with the 
equipment, it also presents a physical description of the Megaplex-4 versions. 
 
Warning 
Do not connect any cables to the Megaplex-4 before it is installed in the 
designated position.  
Installing the Regular Megaplex-4100 Chassis 
Megaplex-4100 is intended for installation on shelves and racks. Do not connect power to the enclosure 
before it is installed in the designated position. 
Installing in a 19” Rack 
For rack installation, it is necessary to install two brackets to the sides of the unit. As illustrated below, 
you may install the brackets in two ways, to orient the unit in accordance with your requirements (either 
with the 
Megaplex-4100 front panel toward the front of the rack, or the module panels toward the front). 
2. Installation 
 
Attachment of Brackets to Megaplex-4100 Case for Installing in 19” Rack 
Installing in 23” Rack 
The same set of brackets can also be used to install the Megaplex-4100 unit in a 23” rack. The figure 
below shows how to attach the brackets for installation in 23” racks (only front installation is shown in 
this figure).  
Install Brackets Here if
You Want the Front Panel
toward the Front of the Rack
2. Installation 
 
Attachment of Brackets for Installation of Megaplex-4100 Unit in 23” Rack 
After attaching the brackets, fasten the enclosure to the rack by four screws (two on each side).  
After installing the enclosure, check and install the required modules, in accordance with the installation 
plan. 
Installing the IEEE-1613 Compliant Megaplex-4100 Chassis in a 19” Rack 
For installation of a single IEEE-1613 Compliant Megaplex-4100 Chassis in a 19” rack, see the previous 
section.   
If you need to install two chassis one above the other, you need a special separating tray (thermal 
isolation panel) RM-51. You may install the brackets in two ways, to orient the units in accordance with 
your requirements (either with the Megaplex-4100 front panel toward the front of the rack, or the 
module panels toward the front). These cases are shown in the figure below. Pay attention to the 
position of the tray in both cases:  
• 
When the front panel is accessed from the front of the rack, the tray is installed with the bottom 
up 
• 
When the module panels are accessed from the front of the rack, the tray is installed with the 
bottom down.  
 
2. Installation 
 
  
Installing Two Megaplex-4100 IEEE-1613 Compliant Chassis in 19” Rack: Accessing Megaplex 
Front Panel from the Front of the Rack   
 
2. Installation 
  
Installing Two Megaplex-4100 IEEE-1613 Compliant Chassis in 19” Rack: Accessing Module 
Panels from the Front of the Rack   
Installing the Megaplex-4104 Chassis  
Megaplex-4104 can be installed on shelves, racks and mounted on the wall. Do not connect power to 
the enclosure before it is installed in the designated position. 
For rack and wall-mount installation, refer to the leaflets supplied with RM-42, RM-42-CM, WM-42 and 
WM-42-CM rack-mount and wall-mount kits.  
2. Installation 
2.7 Installing Modules 
Installing PS Modules 
 
Warning 
Dangerous voltages are present inside the PS module when it is connected 
to power. Do not connect the PS module to power before it is properly 
installed within the Megaplex-4 enclosure. Always disconnect the input 
power from the PS module before removing it from the enclosure. The 
installation and preparation of the module shall be done by a qualified 
person who is aware of the hazards involved.  
Megaplex-4100 Module Panels  
The following PS versions are offered for Megaplex-4100:  
• 
DC-powered modules, PS/48: 250W modules, operating on -48 VDC (nominal) 
• 
AC-powered module, PS/AC: 250W module, operates on 115 VAC or 230 VAC, 50/60Hz (nominal 
voltage is marked on the module panel) and includes HVDC support of 100 to 360 VDC.  
• 
IEEE-1613 compliant DC-powered modules, PS/48/H1: 175W modules, operating on -48 VDC 
(nominal) 
• 
IEEE-1613 compliant AC-powered module, PS/AC/H1: 175W module, operates on 115 VAC or 
230 VAC, 50/60Hz (nominal voltage is marked on the module panel) and includes HVDC support 
of 100 to 360 VDC.  
Typical PS panels are shown below. PS modules do not include a power on/off switch and start 
operating as soon as power is applied. It is recommended to use an external power on/off switch, for 
example, the circuit breaker used to protect the supply line to the Megaplex-4100 may also serve as the 
on/off switch. 
2. Installation 
 
 
AC-Powered Module 
-48 VDC-Powered Module 
Typical Megaplex-4100 PS Module Panels  
2. Installation 
 
 
AC-Powered Module, IEEE-1613 
Compliant 
DC-Powered Module, IEEE-1613 
Compliant 
Typical Megaplex-4100 PS Module Panels  
The PS modules connect to an external feed and ring voltage source, e.g., a Ringer-2200N standalone 
unit offered by RAD:  
• 
The AC-powered PS versions have a separate connector, designated VDC-IN, for the external -48 
VDC and +72 VDC voltages. 
• 
The connection of the +72 VDC voltage to the DC-powered PS versions is made through the 
VDC-IN input connector. The DC feed voltage is derived from the DC input voltage, and 
therefore has the same voltage and polarity. 
The regular PS modules have a miniature cooling fan on the front panel. Make sure to keep the fan 
opening free of obstructions.  
Megaplex-4104 Module Panels  
The following PS versions are offered for Megaplex-4104:  
• 
DC-powered modules, PS/48: 160W modules, operating on -48 VDC (-36 to -56 VDC) 
2. Installation 
• 
AC-powered module, PS/AC: 160W module, operates on 100 VAC to 260 VAC, 50/60Hz 
(including HVDC support of 110 to 300 VDC) 
Typical PS panels are shown below. PS modules do not include a power on/off switch and start 
operating as soon as power is applied. It is recommended to use an external power on/off switch, for 
example, the circuit breaker used to protect the supply line to the Megaplex-4104 may also serve as the 
on/off switch. 
 
 
AC-Powered Module  
DC-Powered Module 
Typical Megaplex-4104 PS Module Panels  
The PS modules connect to an external feed and ring voltage source, e.g., a Ringer-2200N standalone 
unit offered by RAD:  
• 
The AC-powered PS versions have a separate connector, designated VDC-IN, for the external -48 
VDC and +72 VDC voltages. 
• 
The connection of the +72 VDC voltage to the DC-powered PS versions is made through the 
VDC-IN input connector. The DC feed voltage is derived from the DC input voltage, and 
therefore has the same voltage and polarity. 
The PS modules connect to an external feed and ring voltage source, e.g., a Ringer-2200N standalone 
unit offered by RAD. The connection of the +72 VDC voltage to the DC-powered PS is made through the 
VDC-IN input connector. The DC feed voltage is derived from the DC input voltage, and therefore has the 
same voltage and polarity. 
Megaplex-4100 Internal Jumpers  
The PS modules include two internal jumpers that control the connection of frame ground to the 
internal ground lines.  
 
2. Installation 
Caution 
If the Megaplex-4100 chassis must be operated with floating ground, it may 
also be necessary to disconnect the ground reference on all the installed 
modules and check the ground and shield wiring on the cables connected to 
the chassis. This may require changing the hardware settings on the 
installed modules and appropriate cables. 
Special ordering options with preconfigured settings are available. Contact 
your local RAD Partner for more information.  
The jumpers of a typical PS module (PS/DC or PS/AC) are identified below. 
 
GND = FGND
Signal Ground 
Connected to 
Frame Ground
YES
NO
BGND = FGND
48 VDC Positive Line 
Connected to Frame 
Ground
YES
NO
NO    YES
NO    YES
Signal Ground 
not Connected to 
Frame Ground
48 VDC Positive Line 
not Connected
to Frame Ground
Front Panel
 
Typical Megaplex-4100 PS Module (Lateral View), Location of Internal Jumpers 
• 
The jumper designated GND=FGND controls the connection between the internal signal ground 
and the frame (enclosure) ground. The module is normally delivered with the jumper set to YES. 
If necessary, you can set the jumper to NO to float the signal ground with respect to the frame 
ground.  
• 
The jumper designated BGND=FGND controls the connection between the positive (+) line of 
the external 48 VDC voltage and the frame (enclosure) ground. The module is normally delivered 
with the jumper set to YES. If necessary, you can set the jumper to NO to float the external 
48 VDC positive line with respect to the frame ground. This is usually necessary when the DC 
voltage is used to feed or ring voltages. 
2. Installation 
Note 
PS/DC and PS/AC modules can also use a positive supply voltage. In this case, 
always disconnect BGND from FGND (set the jumper to NO).  
If two power supply modules are installed, make sure that the internal jumpers are set to the 
same position on both modules. 
Caution 
Certain I/O modules may still cause BGND to be connected to FGND or GND, 
even after setting the jumpers to NO. Refer to the appropriate sections of 
Appendix B describing the modules installed in the chassis for proper setting 
of their ground-control jumpers.  
Megaplex-4104 Internal Jumpers  
Megaplex-4104 PS modules include two sets of internal jumpers that control the connection of frame 
ground to the internal ground lines.  
 
Caution 
If the Megaplex-4104 chassis must be operated with floating ground, it may 
also be necessary to disconnect the ground reference on all the installed 
modules and check the ground and shield wiring on the cables connected to 
the chassis. This may require changing the hardware settings on the 
installed modules and appropriate cables. 
Special ordering options with preconfigured settings are available. Contact 
your local RAD Partner for more information.  
The jumpers of a typical PS module (PS/DC) are identified below. 
2. Installation 
BGND = FGND
48 VDC Positive Line 
Connected to Frame 
Ground
YES
NO
48 VDC Positive Line 
not Connected
to Frame Ground
GND = FGND
Signal Ground 
Connected to 
Frame Ground
YES
NO
Signal Ground 
not Connected to 
Frame Ground
YES  NO
YES
NO
Front Panel
 
Typical Megaplex-4104 PS Module (Top View), Location of Internal Jumpers  
• 
The jumper designated GND=FGND controls the connection between the internal signal ground 
and the frame (enclosure) ground. The module is normally delivered with the jumper set to YES. 
If necessary, you can set the jumper to NO to float the signal ground with respect to the frame 
ground.  
• 
The jumper designated BGND=FGND controls the connection between the positive (+) line of 
the external 48 VDC voltage and the frame (enclosure) ground. The module is normally delivered 
with the jumper set to YES. If necessary, you can set the jumper to NO to float the external 
48 VDC positive line with respect to the frame ground. This is usually necessary when the DC 
voltage is used to feed or ring voltages. 
Note 
PS/DC and PS/AC modules can also use a positive supply voltage. In this case, 
always disconnect BGND from FGND (set the jumper to NO).  
If two power supply modules are installed, make sure that the internal jumpers are set to the 
same position on both modules. 
Caution 
Certain I/O modules may still cause BGND to be connected to FGND or GND, 
even after setting the jumpers to NO. Refer to the appropriate sections of 
Appendix B describing the modules installed in the chassis for proper setting 
of their ground-control jumpers.  
2. Installation 
Installing a PS Module 
 
Warning 
Do not connect the power and/or ring and feed voltage cable(s) to a PS 
module before it is inserted in the Megaplex-4 chassis. Disconnect the 
cable(s) from the module before it is removed from the chassis.  
2. Insert the PS module in the PS-A slot, and fasten it with the two screws. 
3. Connect the power cable according to the voltages indicated on the panel. 
4. If an additional redundant module is used, install it in the PS-B slot. 
Note 
You can install a redundant module in an operating enclosure without turning 
the Megaplex-4 power off. In this case: 
• 
First insert the module in its slot 
• 
Connect its power cable.  
Removing a PS Module 
1. Disconnect the power cable(s) connected to the module. 
2. Release the two module screws 
3. Pull the PS module out. 
Installing CL Modules 
Megaplex-4100 accommodates two dual-slot CL.2 modules. A special compact single-slot CL.2 module 
version is available, allowing the use of two CL.2 modules in the Megaplex-4104 chassis. Megaplex-4104 
can also use the regular dual-slot module (one per chassis).   
The modules include the chassis management and timing subsystem, and a cross-connect matrix for 
TDM traffic, two SDH/SONET ports (with STM-1/OC-3 or STM-4/OC-12 interfaces, in accordance with 
order) and two GbE ports (with SFPs or with copper interfaces, in accordance with order). The panels for 
the STM-1/OC-3 or STM-4/OC-12 versions are identical. A special version without SDH/SONET and GbE 
ports can be used for DS0 cross-connect services only.  
Megaplex-4100 Module Panels  
The Megaplex-4100 chassis can be equipped with two CL modules. At any time, only one module is 
active, and the other serves as hot standby.  
2. Installation 
The figures below show the following versions of CL.2 module panels: 
• 
CL.2  
• 
CL.2/A, regular  
• 
CL.2/A, IEEE-1613-compliant  
• 
CL.2/DS0 only, IEEE-1613-compliant. 
The table below describes the functions of the panel switches. For description of LED indicators, see 
Chapter 3. 
 
 
ON
LINE
CL.2
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
1
2
LOS
S
D
H
/
S
O
N
E
T
1
2
LASER
CLASS
1
 
ON
LINE
CL.2
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
LOS
S
D
H
/
S
O
N
E
T
1
2
1
2
LASER
CLASS
1
 
CL.2
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
 
CL.2 with Copper 
GbE Interfaces 
CL.2 with Optical 
GbE Interfaces 
CL.2 for DS0 Cross-
connect only  
 
 
CL.2 Module Panels  
2. Installation 
 
ON
LINE
CL.2
A
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
1
2
LOS
S
D
H
/
S
O
N
E
T
1
2
LASER
CLASS
1
 
ON
LINE
CL.2
A
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
LOS
S
D
H
/
S
O
N
E
T
1
2
1
2
LASER
CLASS
1
 
CL.2
A
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
1
2
 
CL.2
A
C
O
N
T
R
O
L
D
C
E
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
1
2
 
CL.2/A with Copper 
GbE Interfaces 
CL.2/A with Optical 
GbE Interfaces 
CL.2/A (GbE only) with 
Copper GbE Interfaces 
CL.2/A (GbE only) with 
Optical GbE Interfaces 
 
CL.2/A Module Panels 
  
2. Installation 
 
 
 
 
 
CL.2/A with Copper 
GbE Interfaces 
CL.2/A with Optical 
GbE Interfaces 
CL.2/A (GbE only) with 
Copper GbE Interfaces 
CL.2/A (GbE only) with 
Optical GbE Interfaces 
 
CL.2/A/1613 Module Panels  
 
2. Installation 
 
CL.2/DS0/1613 Module Panel 
Module CL.2 for Megaplex-4100, Panel Components 
Item 
Function 
CLOCK Connector  
RJ-45 connector for the station clock input and output signals  
CONTROL ETH Connector  
RJ-45 connector for the 10/100BaseT Ethernet management port  
CONTROL DCE Connector 
9-pin D-type female connector with RS-232 DCE interface, for connection to 
system management. Connector pin allocation is given in Appendix A 
ALARM Connector  
9-pin D-type female connector, for connection to the Megaplex-4100 alarm relay 
outputs, and an external alarm input. Connector pin allocation is given in 
Appendix A 
SDH/SONET 1, 2 Connectors  Sockets for installing SFP transceivers for the corresponding SDH/SONET ports  
GbE 1, 2 Connectors  
Sockets for installing SFP transceivers for the corresponding GbE ports,  
or RJ-45 connectors   
2. Installation 
Megaplex-4104 Module Panels 
A special compact single-slot CL.2 module allows the use of two CL.2 modules in the Megaplex-4104 
chassis. At any time, only one module is active, and the other serves as hot standby.  
Megaplex-4104 can also use the regular dual-slot module (one per chassis).   
The figures below show the following versions of CL.2 module panels: 
• 
CL.2  
• 
CL.2/A  
The table below describes the functions of the panel switches. For description of LED indicators, see 
Chapter 3. 
 
 
CL.2
ON
LINE
C
O
N
T
R
O
L
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LOS
S
D
H
/
S
O
N
E
T
1
2
D
C
E
LINK
ACT
G
b
E
1
2
LASER
CLASS
1
 
CL.2
ON
LINE
C
O
N
T
R
O
L
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
LOS
S
D
H
/
S
O
N
E
T
1
2
1
2
D
C
E
LASER
CLASS
1
 
CL.2
C
O
N
T
R
O
L
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
D
C
E
 
CL.2 with Copper 
GbE Interfaces 
CL.2 with Optical 
GbE Interfaces 
CL.2 for DS0 Cross-
connect only  
2. Installation 
 
 
CL.2/4104 Module Panels  
 
CL.2
A
ON
LINE
C
O
N
T
R
O
L
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LOS
S
D
H
/
S
O
N
E
T
1
2
D
C
E
LINK
ACT
G
b
E
1
2
LASER
CLASS
1
 
CL.2
A
ON
LINE
C
O
N
T
R
O
L
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
LOS
S
D
H
/
S
O
N
E
T
1
2
1
2
D
C
E
LASER
CLASS
1
 
CL.2
A
C
O
N
T
R
O
L
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
D
C
E
LINK
ACT
G
b
E
1
2
CL.2
A
 
CL.2
A
C
O
N
T
R
O
L
A
L
A
R
M
LINK
ACT
E
T
H
C
L
O
C
K
ON LINE
ALM
ON/LOS
LINK
ACT
G
b
E
1
2
D
C
E
 
CL.2/A with Copper 
GbE Interfaces 
CL.2/A with Optical 
GbE Interfaces 
CL.2/A (GbE only) with 
Copper GbE Interfaces 
CL.2/A (GbE only) with 
Optical GbE Interfaces 
 
CL.2/A/4104 Module Panels 
Module CL.2 for Megaplex-4104, Panel Components 
Item 
Function 
CLOCK Connector  
RJ-45 connector for the station clock input and output signals  
2. Installation 
Item 
Function 
CONTROL ETH Connector  
RJ-45 connector for the 10/100BaseT Ethernet management port 
CONTROL DCE Connector 
MINI-USB connector, for connection to system management. Connector pin 
allocation is given in Appendix A 
ALARM Connector  
9-pin flat connector, for connection to the Megaplex-4104 alarm relay outputs, 
and an external alarm input. Connector pin allocation is given in Appendix A 
SDH/SONET 1, 2 Connectors  Sockets for installing SFP transceivers for the corresponding SDH/SONET ports  
GbE 1, 2 Connectors  
Sockets for installing SFP transceivers for the corresponding GbE ports,  
or RJ-45 connectors   
Installing and Replacing SFPs  
Before installing a CL 
 
module, you may have to install the prescribed types of SFPs . 
Installing an SFP  
 
 
Warning 
When installing an optical SFP in an operating module, be aware that it may 
immediately start generating laser radiation.  
 
Caution 
During the installation of an SFP with optical interfaces, make sure that all 
optical connectors are closed by protective caps. 
Do not remove the covers until you are ready to connect optical fibers to the 
connectors. Be aware that when inserting an SFP into a working module, the 
SFP transmitter may start transmitting as soon as it is inserted.  
 
Note 
All the following procedures are illustrated for typical SFPs with optical 
interfaces. However, the same procedures apply for SFPs with electrical 
(copper) interfaces 
 
2. Installation 
 
 Warning 
Third-party SFP optical transceivers must be agency-
approved, complying with the local laser safety regulations 
for Class 1 laser equipment.  
 
 To install the SFP module: 
1. Lock the wire latch of the SFP module by lifting it up until it clicks into place. 
Note 
Some SFP models have a plastic door instead of a wire latch 
 
2. Carefully remove the dust covers from the corresponding SFP socket of the CL module, and from 
the SFP electrical connector. 
3. Orient the SFP as shown above, and then insert the rear end of the SFP into the module socket. 
4. Push SFP slowly backwards to mate the connectors, until the SFP clicks into place. If you feel 
resistance before the connectors are fully mated, retract the SFP using the wire latch as a pulling 
handle, and then repeat the procedure. 
5. If necessary, repeat the procedure for the other SFP.  
Caution 
Insert the SFP gently. Using force can damage the connecting pins.  
6. Remove the protective rubber caps from the SFP modules. 
 To remove the SFP module: 
1. Disconnect the fiber optic cables from the SFP module. 
2. Unlock the wire latch by lowering it downwards (as opposed to locking). 
3. Hold the wire latch and pull the SFP module out of the port.  
2. Installation 
Caution 
Do not remove the SFP while the fiber optic cables are still connected. This 
may result in physical damage (such as a chipped SFP module clip or socket) 
or cause malfunction (e.g., the network port redundancy switching may be 
interrupted).  
Replacing an SFP  
SFPs can be hot-swapped. It is always recommended to coordinate SFP replacement with the system 
administrator. During the replacement of SFPs with optical interfaces, only the traffic on the affected 
link is disrupted (the other link can continue to carry traffic). 
 To replace an SFP: 
1. If necessary, disconnect any cables connected to the SFP connectors. 
2. Push down the SFP locking wire, and then pull the SFP out. 
3. Reinstall protective covers on the SFP electrical and optical connectors. 
4. Install the replacement SFP in accordance with the Error! Reference source not found. section. 
Installing a CL Module  
CL modules are installed in the CLX-A and/or CLX-B slots. When two CL modules are installed, 
redundancy is available. In this case, the module installed in slot CLX-A will be automatically selected as 
the master module, provided that it operates normally and stores all the required configuration 
parameters. 
 To install a CL module: 
1. Check that the two fastening screws of the module are free to move. 
2. Insert the CL module in its chassis slot and slide it backward as far as it goes. 
3. Simultaneously press the extractor handles toward the center of the module to fully insert its 
rear connector into the mating connector on the backplane. 
4. Secure the CL module by tightening its two screws.  
Removing a CL Module 
 To remove a CL module: 
1. Fully release the two screws fastening the module to the chassis. 
2. Installation 
2. Simultaneously push the extractor handles outward, to disengage the rear connector. 
3. Pull the module out. 
Replacing a CL Module during Equipment Operation –Megaplex-4 Chassis with two CL 
Modules 
In a Megaplex-4 equipped with two functional CL modules, the standby module can be 
removed/replaced with minimal disruption of Megaplex-4 services: when you replace the on-line CL 
module, Megaplex-4 will automatically switch to the standby module, provided that module is 
operational.  
The expected disruptions can be minimized in the following ways: 
• 
An active CL module also provides routing services and clock signals to other Megaplex-4 
subsystems, as well as an out-of-band connection to management. Simply removing the active 
CL module will therefore cause a disruption, however short, in all the services provided by the 
Megaplex-4 chassis. It is therefore important to prevent this type of disruption, and this can be 
achieved by first switching (flipping) to the standby CL module before replacing the on-line CL 
module.  
• 
Removing a module always disconnects the traffic carried by the active payload interfaces (GbE 
and/or SDH/SONET) located on the replaced module. Note that these traffic interfaces can be 
active even on the standby CL module, and therefore the only way to avoid traffic 
disconnections is to use automatic protection for these interfaces: for example, APS can be used 
to protect SDH/SONET traffic, and LAG protection can be used to protect Ethernet traffic. 
You can identify the active and standby modules by their ON LINE indicators. 
Caution 
To prevent service disruption, check that the ON LINE indicator of the CL 
module you want to remove is flashing. If not, use the supervisory terminal 
(or any other management facility) to reset the module to be replaced, and 
wait for execution of this command before continuing: this will cause the 
Megaplex-4 to flip to the other CL module within 50 msec.  
 To flip to the other CL module using the supervision terminal: 
1. Identify the on-line CL module: this is the module with the lit ON LINE indicator. 
2. Whenever possible, connect the supervision terminal directly to the CONTROL DCE connector of 
the on-line CL module, and log in as administrator. 
3. At the mp4100>admin# prompt, type reboot active to send a reset command to the module to 
be replaced. 
2. Installation 
4. Wait for the flipping to be executed. After it is executed, the ON LINE indicator of the CL module 
the supervision terminal is connected to starts flashing, while that of the other module stops 
flashing and lights steadily. 
5. You can now disconnect the supervision terminal, and remove the module. 
6. When installing a CL module in the slot of the removed module, you may cause flipping to the 
original module by resetting the current on-line CL module. 
Replacing a CL Module during Equipment Operation –Megaplex-4 Chassis with Single CL 
Module 
In a Megaplex-4 equipped with a single CL module, before replacing the CL module it is recommended 
that a functional CL module of the same type be installed in the free CL slot. The replacement can be 
temporary.  
After inserting the additional CL module, it is necessary to let it update its database from the 
information provided by the existing CL module:  
1. If necessary, program the additional module in the Megaplex-4 database.  
2. Enter commit to update the databases, and then wait until the CL DB CHECKSUM IS DIFFERENT 
alarm is off. 
3. At this stage, continue in accordance with the steps listed above for a  
Megaplex-4 with two CL modules.  
If the only CL module in the chassis is replaced, Megaplex-4 services will always be disrupted to some 
extent while no CL module is present. Therefore, be prepared and perform the replacement as rapidly as 
possible.  
Among other steps, make sure to upload the existing configuration database to a host, using TFTP. After 
replacement is completed, download the database to the new CL module, to continue normal operation 
in accordance with the previous configuration. 
Adding a Protection CL Module to a Working Module Configured as SONET  
When the working CL module is configured as SONET, inserting a new CL module for protection requires 
the following configuration steps: 
1. Retrieve the “startup-config” file.   
2. Add the protection CL to the retrieved “startup-config” script (if the working module is CL-A, add 
the following string: “configure slot cl-b card-type cl2-622gbe…” etc.) 
3. Copy the new script to the database. 
2. Installation 
4. Save the changes. 
5. Insert the module into the chassis. 
6. Reboot the device. 
Installing System Modules in Megaplex-4104 Chassis  
Refer to the above sections for MP-4100. The only difference is that the power supply has a different 
shape.  
Caution 
To prevent physical damage to the electronic components assembled on the 
two sides of the module printed circuit boards (PCB) while it is inserted into 
its chassis slot, support the module while sliding it into position and make 
sure that its components do not touch the chassis structure, nor other 
modules. 
This precaution is particularly important when installing modules into the 
two lower I/O slots (1 and 4) of the Megaplex-4104 chassis: take special 
care to support the module from below, while pushing it in gently. 
Installing I/O Modules  
Install each I/O module in the prescribed I/O slot, in accordance with the installation plan.  
For installation instructions, refer to the corresponding section of Appendix B.  
Installing Blank Panels 
Install blank panels in all the chassis slots that are not occupied by modules. 
2.8 Connecting to Power  
Grounding Megaplex-4  
2. Installation 
 
Warning 
Before connecting any cables and before switching on this instrument, the 
protective ground terminals of this instrument must be connected to the 
protective ground conductor of the (mains) power cord. The mains plug shall 
only be inserted in a socket outlet provided with a protective ground 
contact. Any interruption of the protective (grounding) conductor (inside or 
outside the instrument) or disconnecting the protective ground terminal can 
make this instrument dangerous. Intentional interruption is prohibited. 
Make sure that only fuses of the required rating are used for replacement. 
Use of repaired fuses and the short-circuiting of fuse holders is forbidden. 
Whenever it is likely that the protection offered by fuses has been impaired, 
the instrument must be made inoperative and be secured against any 
unintended operation.  
Connect a short, thick copper braid between the grounding screw on each PS module panel and a 
nearby grounding point. 
Connecting to Power 
 
Caution 
Megaplex-4 does not have a power on/off switch and will start operating as 
soon as power is applied to at least one of its PS modules. It is 
recommended to use an external power on/off switch to control the 
connection of power to Megaplex-4. For example, the circuit breaker used to 
protect the supply line to Megaplex-4 may also serve as the on/off switch. 
Power should be connected only after completing cable connections.  
Connect the power cable(s) first to the connector on the PS module, and then to the power outlet. For 
DC cables, pay attention to polarity. The gauge for DC cable is 18 AWG to 12 AWG. 
Note 
When redundant power supply modules are used, it is recommended to 
connect the power cables to outlets powered by different circuits.  
Connecting to External Feed Voltages 
External feed voltages are required by the following modules: 
• 
Voice modules installed in AC-fed chassis 
• 
ISDN modules 
2. Installation 
• 
SHDSL modules.  
The recommended source for external voltages in the case of voice and ISDN modules is Ringer-2200N 
offered by RAD. Ringer-2200N is a standalone unit intended for rack mounting, capable of providing 
power for up to 120 voice channels. Refer to the Ringer-2200N Installation and Operation Manual for 
connection instructions.  
The recommended source for external phantom feed voltages in the case of SHDSL modules is MPF 
(Megaplex Power Feed) offered by RAD. standalone unit intended for rack mounting, MPF provides 
power for Megaplex SHDSL modules that require DC voltage to remote DSL repeaters or modems (up to 
40 active SHDSL modems or repeaters operating in 4-wire mode). Refer to the MPF Installation and 
Operation Manual for connection instructions. 
 
Caution 
Turn on the Ringer-2200N/MPF external voltage source, or connect the 
external voltages, only after Megaplex-4 is turned on. 
Turn off the Ringer-2200N/MPF external voltage source, or disconnect the 
external voltages, only before Megaplex-4 is turned off.  
2.9 Connecting Megaplex-4 to a Terminal 
Two of the four connectors available on CL.2 modules (CONTROL DCE and ALARM) are different for 
Megaplex-4100 and Megaplex-4104 CL.2 modules. Be sure to refer to the correct section below.  
Megaplex-4100 CL.2 Module  
The CL supervisory port has a serial RS-232 asynchronous DCE interface terminated in a 9-pin D-type 
female connector, designated CONTROL DCE.  
This port can be directly connected to terminals using a cable wired point-to-point. A cross cable is 
required to use the DTE mode, for example, for connection through modems or digital multiplexer 
channels.  
Ethernet ports of redundant CL modules do not require any special connections: each one can be 
connected to a separate Ethernet hub port. 
2. Installation 
 To connect to the CONTROL DCE port:  
The connections to the CONTROL DCE connector are made as follows: 
• 
Connection to a supervision terminal with 9-pin connector: by means of a straight cable (a cable 
wired point-to-point).  
• 
Connection to modem with 9-pin connector (for communication with remote supervision 
terminal): by means of a crossed cable.  
Additional connection options are presented in Appendix A. 
 To connect to an ASCII terminal: 
1. Connect the male 9-pin D-type connector of CBL-DB9F-DB9M-STR straight cable available from 
RAD to the CONTROL DCE connector. 
2. Connect the other connector of the CBL-DB9F-DB9M-STR cable to an ASCII terminal. 
Caution 
Terminal cables must have a frame ground connection. Use ungrounded 
cables when connecting a supervisory terminal to a DC-powered unit with 
floating ground. Using improper terminal cable may result in damage to 
supervisory terminal port.  
Megaplex-4104 CL.2 Module 
The CL.2/4104 supervisory port has a serial RS-232 asynchronous DCE interface terminated in a mini-USB 
connector, designated CONTROL DCE.  
This port can be directly connected to terminals using a cable wired point-to-point. A cross cable is 
required to use the DTE mode, for example, for connection through modems or digital multiplexer 
channels. 
Note 
Ethernet ports of redundant CL modules do not require any special 
connections: each one can be connected to a separate Ethernet hub port.  
 To connect to the CONTROL DCE port:  
The connections to the CONTROL DCE connector are made as follows: 
• 
Connection to a supervision terminal with 9-pin connector: by means of the CBL-MUSB-DB9F 
cable supplied by RAD.  
2. Installation 
• 
Connection to modem with 9-pin connector (for communication with remote supervision 
terminal): by means of an additional crossed cable connected to the CBL-MUSB-DB9F cable.  
Additional connection options are presented in Appendix A. 
 To connect to an ASCII terminal: 
1. Connect the mini-USB connector of the CBL-MUSB-DB9F cable available from RAD to the 
CONTROL DCE connector.  
2. Connect the other connector of the CBL-MUSB-DB9F cable to an ASCII terminal. 
Caution 
Terminal cables must have a frame ground connection. Use ungrounded 
cables when connecting a supervisory terminal to a DC-powered unit with 
floating ground. Using improper terminal cable may result in damage to 
supervisory terminal port.  
2.10 Connecting to a Management Station or Telnet Host 
The CL modules have 10BASE-T/100BASE-TX Ethernet interfaces terminated in RJ-45 connectors, 
designated CONTROL ETH.  
These interfaces support MDI/MDIX crossover and therefore the ports can always be connected through 
a “straight” (point-to-point) cable to any other type of 10/100BASE-T Ethernet port (hub or station). 
 To connect to a management station or Telnet host: 
• 
The link to network management stations using SNMP, and/or Telnet hosts is made to the RJ-45 
connector designated CONTROL ETH.  
• 
You can use any standard cable (straight or crossed) to connect to any type of Ethernet port 
(hub or station). 
2.11 Connecting to a Station Clock  
The station clock ports located on the CL modules can accept 2.048 MHz or 1.544 MHz signals (framed 
2.048 Mbps or 1.544 Mbps signals are also accepted). The port can also output the clock signal: this 
2. Installation 
output provides a convenient means for distributing clock signals, including the Megaplex-4 nodal clock 
signal, to other equipment.  
The station clock port is terminated in one RJ-45 connector, designated CLOCK, which supports two 
interfaces:  
• 
100 Ω/120 Ω balanced interface for operation over two twisted pairs 
• 
75 Ω unbalanced interface for operation over coaxial cables. This interface can be used only for 
2.048 MHz or 2.048 Mbps clock signals.  
At any time, only one interface is active. The selection of the active interface is made by the user. In 
addition, provisions are made to sense the type cable connected to the port:  
• 
The cable used for connecting to equipment with balanced interface should include only two 
twisted pairs, one for the clock output and the other for the clock input.  
Note 
One of the contacts in the station clock connector is used to sense the 
connection of the unbalanced adapter cable (see Appendix A). Do not connect 
cables with more than two pairs when you want to use the balanced interface.  
• 
To connect to equipment with unbalanced interface, it is necessary to convert the CL RJ-45 
connector to the standard pair of BNC female connectors used for unbalanced ITU-T Rec. G.703 
interfaces. For this purpose, RAD offers a 15-cm long adapter cable, CBL-RJ45/2BNC/E1/X. This 
cable has one RJ-45 plug for connection to CL station clock connector, and two BNC female 
connectors at the other end.  
Note 
When using redundant CL modules, one of the two station clock ports must be 
connected to a station clock source. For best protection, it is recommended to 
connect the two station ports to two separate station clock sources.  
2.12 Connecting to Alarm Equipment 
The alarm port is terminated in a 9-pin D-type female (Megaplex-4100 CL module) or 9-pin flat 
(Megaplex-4104 CL module) connector located on the CL module, designated ALARM. This port includes: 
• 
Floating change-over dry-contact outputs for the major and minor alarm relays. The alarm relay 
contacts are rated at maximum 60 VDC/30 VAC across open contacts, and maximum 1 ADC through 
closed contacts (total load switching capacity of 60 W). 
Caution 
Protection devices must be used to ensure that the contact ratings are not 
exceeded. For example, use current limiting resistors in series with the contacts, 
and place voltage surge absorbers across the contacts.  
2. Installation 
The relays are controlled by software, and therefore the default state (that is, the state during 
normal operation) can be selected by the user in accordance with the specific system 
requirements. 
• 
+5V auxiliary voltage output (through a 330 Ω series resistor). 
• 
External alarm sense input. The input accepts an RS-232 input signal; it can also be connected by 
means of a dry-contact relay to the auxiliary voltage output. 
 To connect to the ALARM connector: 
Refer to Appendix A for connector pin functions. The alarm cable for Megaplex-4104 is supplied by RAD. 
Caution 
To prevent damage to the internal alarm relay contacts, it is necessary to 
limit, by external means, the maximum current that may flow through the 
contacts (maximum allowed current through closed contacts is 1A). The 
maximum voltage across the open contacts must not exceed 60 VDC.  
2.13 Connecting to SDH/SONET Equipment 
Note 
SFP transceivers can also be installed in the field by the customer, however 
RAD strongly recommends to order modules with preinstalled SFPs, as this 
enables performing full functional testing of equipment prior to shipping.  
Connecting Optical Cables to the SDH/SONET Links 
The optical fibers intended for connection to equipment installed in a rack should pass through fiber 
spoolers, located at the top or bottom of the rack, in accordance with the site routing arrangements 
(overhead or under-the-floor routing). The spoolers must contain enough fiber for routing within the 
rack up to the CL optical connectors, and for fiber replacement in case of damage (splicing repairs). 
From the spoolers, the optical fibers should be routed through cable guides running along the sides of 
the rack frame to the level of the equipment to which they connect.  
When connecting optical cables, make sure to prevent cable twisting and avoid sharp bends (unless 
otherwise specified by the optical cable manufacturer, the minimum fiber bending radius is 35 mm). 
Always leave some slack, to prevent stress. RAD recommends installing plastic supports on each cable 
connector: these supports determine the fiber bending radius at the connector entry point and also 
prevent stress at this point. 
2. Installation 
Caution 
When calculating optical link budget, always take into account adverse 
effects of  temperature changes, optical power degradation and so on. To 
compensate for the signal loss, leave a 3 dB margin. For example, instead of 
the maximum receiver sensitivity of -28 dBm, consider the sensitivity 
measured at the Rx side to be -25 dBm. Information about Rx sensitivity of 
fiber optic interfaces is available in SFP/XFP Transceivers data sheet.  
Caution 
Make sure all the optical connectors are closed at all times by the 
appropriate protective caps, or by the mating cable connector.  
Do not remove the protective cap until an optical fiber is connected to the 
corresponding connector, and immediately install a protective cap after a 
cable is disconnected. 
Before installing optical cables, it is recommended to clean thoroughly their connectors using an 
approved cleaning kit. 
 To connect optical cables to the SDH/SONET links: 
1. For each optical interface, refer to the site installation plan and identify the cables intended for 
connection to the SFP serving the corresponding interface.  
2. Where two fibers are used, pay attention to TX and RX connections, and leave enough slack to 
prevent strain: 
 
Connect the prescribed transmit fiber (connected to the receive input of the remote 
equipment) to the TX connector of the SFP. 
 
Connect the prescribed receive fiber (connected to the transmit output of the remote 
equipment) to the RX connector of the SFP serving the same interface.  
Connecting Coaxial Cables to SDH/SONET Links 
The SFPs offered by RAD for the electrical SDH/SONET links are equipped with two mini-BNC connectors, 
one identified as TX (transmit output) and the other as RX (receive input).  
To convert to BNC connectors, RAD offers the CBL-MINIBNC-BNC adapter cable, terminated in two BNC 
connectors. 
 To connect coaxial cables to the SDH/SONET links: 
1. For each electrical interface, identify the cables intended for connection to this interface in 
accordance with the site installation plan. 
2. Installation 
Note 
If you are using the CBL-MINIBNC-BNC adapter cable, first connect its 
mini-BNC connectors to the corresponding connectors of the SDH links (note 
TX and RX designations), and then proceed with the connection of the external 
cables.   
2. Connect the prescribed coaxial transmit cable (connected to the receive input of the remote 
equipment) to the TX connector of the interface. 
3. Connect the prescribed coaxial receive cable (connected to the transmit output of the remote 
equipment) to the RX connector of the same interface. 
2.14 Connecting to E1 and T1 Equipment 
The maximum allowable line attenuation between a Megaplex-4 E1/T1 external port and the network 
interface depends on the type of port interface, and therefore it is given in the Installation and 
Operation Manual of each specific module. 
The electrical E1 and T1 interfaces of Megaplex-4 systems must not be connected directly to 
unprotected public telecommunication networks. Use primary protectors in the MDF or IDF for 
additional protection. 
2.15 Connecting to Ethernet Equipment 
SFP transceivers can also be installed in the field, by the customer, however RAD strongly recommends 
ordering modules with preinstalled SFPs, as this enables performing full functional testing of equipment 
prior to shipping.  
Caution 
When calculating optical link budget, always take into account adverse 
effects of temperature changes, optical power degradation and so on. To 
compensate for the signal loss, leave a 3 dB margin. For example, instead of 
the maximum receiver sensitivity of -28 dBm, consider the sensitivity 
measured at the Rx side to be -25 dBm. Information about Rx sensitivity of 
fiber optic interfaces is available in SFP/XFP Transceivers data sheet.  
 