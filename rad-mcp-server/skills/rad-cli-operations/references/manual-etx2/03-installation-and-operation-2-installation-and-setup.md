# Installation and Operation – 2 Installation and Setup

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 85–182.*


## 2.1 Storage and Transportation  *(p.85)*

2 Installation and Setup 
2.1 Storage and Transportation 
This chapter describes installation and setup procedures for the ETX‑2i unit.   
After installing the unit, refer to the Operation and Maintenance chapter for operating instructions and 
the Management and Security chapter for management instructions. 
If you encounter a problem, refer to the Monitoring and Diagnostics chapter for test and diagnostic 
instructions. 
The following table describes the stages of the installation and setup. 
Stage 
Comments 
Preparing the site 
 
Unpacking and inspection 
 
Preparing tools and equipment for installation 
 
Installing the air baffle 
Relevant for ETX-2i-10G-B/8SFPP 19-inch 
Mounting the unit 
 
Installing GNSS antenna 
Relevant for ETX-2i-10G-B/8SFPP Outdoor 
Grounding and bonding 
 
Connecting to power 
 
Connecting to Ethernet equipment 
 
Connecting to alarm equipment 
 
Connecting to E1/T1 equipment 
Relevant for ETX-2i with E1/T1 network module, or 64 
built-in E1 ports    
Connecting to the station clock 
Relevant for ETX-2i or ETX-2i-10G ordered with a timing 
option that includes a station clock port 

## 2.2 Staging  *(p.86)*

ETX-2i Devices 
2. Installation and Setup 
Stage 
Comments 
Connecting to synchronization equipment 
Relevant for ETX-2i, ETX-2i-B, ETX-2i-10G/4SFPP, ETX-2i-
10G-B/4SFPP, and ETX-2i-10G-B/8SFPP ordered with a 
timing option that includes the EXT CLK/1PPS ports 
and/or the ToD/1PPS port 
Connecting to T3 equipment 
Relevant for ETX-2i with T3 network module  
Connecting to a terminal 
Via RS-232 interface (designated CONTROL) 
Connecting to an NMS 
Via MNG-ETH 
Performing basic connectivity tests 
For example, ping 
2.2 Staging 
Staging includes any actions required before shipping products to their installation sites, including 
installing the device SW, config files, and enrolling various certificates.  
Staging prior to shipment to the installation site may be required for automatic mass-deployment, also 
known as Zero Touch Provisioning (ZTP).  
Zero Touch (ZT) is a technology for automatic mass-provisioning of network devices. Upon first boot, 
<product name> connects to the service provider’s NOC (Network Operations Center) over private or 
public networks, based on preparation steps performed at various locations. It requires the RADview 
NMS (Network Management System). 
For a description of all aspects of ZT provisioning, including security considerations, read RAD’s Zero 
Touch Provisioning document. 
The staging content is always defined together with the service provider and is normally done by RAD 
(though it can be in combination with the partner (if exists) and/or the service provider). 
Staging may include “Golden Config”/“Base Config” (where we adjust the product’s factory default 
setting to fit the needs of the Service Provider), and can include some initial configuration settings, 
default IP, ZTP related settings, and more. 
There are also custom configuration options that enable/disable certain functions using the custom-
config-x base command 

## 2.3 Hardware Installation  *(p.87)*

ETX-2i Devices 
2. Installation and Setup 
 To configure custom-config-a: 
1. Navigate to license>license-enable # prompt. 
2. Enter custom-config-a 
The following functions are disabled: 
• 
Xpermission events from TxError (IfOutError) 
• 
The 802.1x authenticator reauthentication command 
In some cases, staging may also include adding transceivers and/or other accessories to the device. 
 
 
Warning 
RAD products must be transported to installation sites in their original 
packaging. Failing to do so may damage the equipment and voids the 
warranty. 
2.3 Hardware Installation 
Prerequisites for Service Personnel  
 
Warning 
• 
Only qualified, authorized, and skilled service personnel should carry out 
adjustment, maintenance, or repairs to this product. Operators and 
users should not perform installation, adjustment, maintenance, or 
repairs. 
• 
Always observe standard safety precautions during installation, 
operation, and maintenance of this product. Precautions listed in this 
document are supplements to local safety regulations for installation. 
• 
RAD shall be released from all obligations under its warranty in the 
event that the equipment has been subjected to misuse, neglect, 
accident, or improper installation, or if repairs or modifications were 
made by persons other than RAD's own authorized service personnel, 
unless such repairs by others were made with the written consent of 
RAD. 
These are the minimum qualifications to install, maintain, or service a device, depending on the 
type of installation: 
ETX-2i Devices 
2. Installation and Setup 
• 
Competent knowledge of electrical engineering and electronics. 
• 
Awareness of the electrical safety precautions necessary to avoid personal injury and 
damage to equipment. 
• 
Willingness to adhere to all safety and handling guidelines that the IEC publishes, and 
relevant national regulatory agencies designate for laser hazard levels and classes. 
• 
Basic knowledge of computers and optical-fiber communication systems. 
• 
Practical knowledge of lasers, laser classification, and laser hazards based on ANSI. 
• 
Z136.1. general knowledge of safety precautions for when you work in the vicinity of 
lasers. 
• 
Awareness of ESD-prevention precautions to avoid ESD damage to equipment. 
• 
Previous training in installation, operation, maintenance, and troubleshooting of ETX‑2i 
and software, and awareness of the potential hazards. 
• 
Understanding all safety guidelines outlined in this guide and the willingness to follow 
them. 
• 
Knowledge of the standard practices to prevent accidents and training in how to render 
first aid. 
Personnel who handle power cables, connect the power, and ground the equipment should 
have these minimum qualifications: 
• 
Training as an electrician and knowledge of the national grounding systems, standard 
electrical safety, and electrical wiring and connection practices for electrical equipment 
installation. 
• 
Awareness of precautions necessary to avoid personal injury and damage to equipment. 
Previous safety training on the potential hazards in relation to electrical equipment. 
• 
The required skills and experience with DC power, power cabling, and the electrical 
equipment to install ETX‑2i. 
• 
Knowledge of these electrical codes and standards: 
 
EU: EN 50110-1-2, EN 50310, ETSI EN 30012-2, ETSI EN 300253, IEC 60364, Part 1 
through Part 7 
 
NA: UL 62368-1, NFPA 70, CSA C22.1  
• 
Knowledge of relevant local and national electrical codes is imperative if these 
standards are unavailable. 
 
 
ETX-2i Devices 
2. Installation and Setup 
Personnel who handle, connect, and clean the optical cables should have these minimum 
qualifications: 
• 
Knowledge about handling fiber-optic cables and awareness of the precautions to avoid 
damage to the cables. 
• 
Familiarity with handling optical fibers and optical test equipment, and about cleaning 
optical connectors. 
• 
Previous training in laser-based technology and optical-fiber communication systems. 
• 
Education about these relevant laser safety standards: 
 
EU: IEC/EN 60825-1, IEC/EN 60825-2 
 
NA: ANSI Z136.1, 21CFR1040.10, 21CFR1040.11 
 
International: ITU-T G.664, ITU-T G.665 
• 
Knowledge about the appropriate eye safety precautions and understanding about the 
safe use of ETX‑2i and management software. 
Site Requirements 
Floor Plan 
Follow these clearance requirements: 
• 
Allow at least 90 cm (36 in) of frontal clearance for operating and maintenance accessibility.  
• 
Allow at least 10 cm (4 in) clearance at the rear of the unit for signal lines and interface cables, 
and to ensure that cables do not block airflow.  
• 
In devices that have “side-to-side” airflow, allow at least 10 cm (4 in) clearance on sides for 
proper airflow. 
• 
Do not place any equipment on top of the unit as it may block airflow. 
• 
Do not place equipment below a unit, as it results in heat flow toward the unit. 
• 
Allow a 1U high space between units with passive airflow.  
AC/DC Power 
It is advisable to install AC-powered units within 3 m (10 ft) of an easily-accessible grounded AC outlet 
capable of furnishing the voltage in accordance with the nominal supply voltage.  
ETX-2i Devices 
2. Installation and Setup 
To protect equipment from surges on AC lines that exceed 500V, install a suitable surge protection 
device (SPD) at the AC power service entrance. The SPD should be an approved component according to 
local regulations and codes and be capable of handling 6000V/3000A surges.  
DC-powered units require a -48 VDC power source. When a DC power supply is employed, incorporate 
in the building installation a readily accessible disconnect device that is suitably rated and approved. The 
disconnect device comprises the circuit breakers that are part of the external ROC system. Use a readily 
accessible double pole with a suitably certified circuit breaker, rated not more than 20 A and having 
contact separation not less than 3 mm. Adequately isolate the units from the main supply. 
Ground ETX‑2i units installed in a Central Office (CO) to a common bonding network. This is the 
grounding system where all metal parts and construction materials of the building and installation are 
deliberately bonded together and to the structure’s ground electrodes.  
Carefully design the grounding system to prevent high voltages between various types of site 
equipment, due to ground potential rise. 
Note 
Refer also to the Connecting AC Mains and Connecting DC Power sections in 
the Front Matter of this manual. 
Environmental Factors 
The following table displays the ambient operating temperature of ETX‑2i products.  
Device 
Temperature 
ETX-2i  
Regular enclosure: 0 to 50°C (32 to 122°F) 
Temperature-hardened enclosure (fixed and modular options only): -40 to 65°C (-40 to 149°F) 
ETX-2i-B 
Regular enclosure: -5 to 55°C (23 to 131°F). 
Device with D-NFV: 0 to 50°C (32 to 122°F) 
Temperature-hardened device with 10 ports (2U), fanless: -20 to 65°C (-4 to 149°F) 
ETX-2i-10G 
Regular enclosure: 0 to 50°C (32 to 122°F) 
Temperature-hardened enclosure: -40 to 65°C (-40 to 149°F)  
ETX-2i-10G-B 
Regular enclosure: 0 to 50°C (32 to 122°F) 
Temperature-hardened or outdoor enclosures: -40 to 65°C (-40 to 149°F) 
ETX-2i-100G 
Regular enclosure: 0 to 50°C (32 to 122°F) 
Temperature-hardened enclosure: -20 to 65°C (-4 to 149°F) 
 
The ambient operating temperature of ETX‑2i is at a relative humidity of 5% to 90%, non-condensing. 
ETX-2i Devices 
2. Installation and Setup 
Site Security 
 
Warning 
Install ETX-2i-10G and ETX-2i-10G-B half 19-inch hardened in a Restricted 
Access Location only (i.e., access allowed only to authorized personnel who 
control the access devices, such as lock and key). 
Site Safety 
It is recommended to install the unit in locations where children are not likely to be present. 
 
Warning 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. Precautions listed in this document are 
supplements to local and national safety regulations for installation. 
Protection from Hazards 
You may have to open a unit for servicing or hot swapping of power supplies. Therefore, it is 
recommended to install the unit in an area that takes into consideration water, moisture, dust, smoke, 
chemicals, noise, pollution, and electromagnetic interference. 
Unpacking and Inspection 
RAD securely packages each product in shipping boxes. Examine the outside of the shipping boxes for 
dents and punctures that might indicate possible shipping damage. Note and report any damage as 
necessary. 
Keep shipping boxes for a minimum period of 24 hours in the installation location to prevent rapid 
thermal shock from rapid temperature change and surface condensation when you unpack the boxes. 
Place each shipping box in an area that meets the climatic conditions specified in EN 300019-1-1 
V2.2.1(2014-04). 
Do not expose shipping boxes to: 
• 
High levels of dust, smoke, or moisture 
• 
Direct sunlight or heat sources 
Place the shipping boxes off the ground no lower than knee height to reduce the height of the lifting 
required. 
ETX-2i Devices 
2. Installation and Setup 
Store the shipping boxes where you have enough space to safely unpack the shelf. 
Leave the shelf in its shipping box until the site is ready for installation.  
Keep all associated ancillary equipment with its relevant equipment. 
Use an appropriate carrying device such as a hand truck, pushcart, or dolly, to move the shipping boxes 
to the location.  
Required tools and equipment: 
• 
Utility knife or scissors 
• 
ESD-preventive wrist strap or other personal grounding device 
• 
Suitable grounded surface or a static-dissipative mat 
Unpacking procedure:  
1. Attach a ground strap to your wrist and snap the ground wire to the wrist band. Insert the 
ground plug into a grounded ESD jack. 
2. Inspect each shipping box for evidence of damage during shipment. You must promptly assert 
any claims for damage caused during shipment with the transportation company involved. If any 
damage or other signs of mishandling are evident, inform both the freight carrier and RAD 
before you unpack the equipment. Your freight carrier can provide you with the procedures 
necessary to file a claim for damages. 
3. Move the shipping boxes to a staging area as close to the installation site as possible where you 
have enough space to remove the component from the boxes. 
4. Open each shipping box: 
a. Use a utility knife or scissors to cut open the band-clamp straps from the box. 
b. Lift the cap by using the handles on the right side and left side to open the box. 
5. Lift the tray from the top of the shelf and set it aside.  
6. Remove the component from each shipping box. 
7. Move the component to a stable surface in the work area and then place it on a static 
dissipative mat. Wait until the component is secure before you release your grip. 
Caution 
• 
Risk of damage due to electrostatic discharge! Keep the component in 
its ESD protective bag until you are ready to inspect it. 
• 
Do not drop the equipment on a hard surface, which can result in 
damage to internal components. If you drop any components, return 
them to RAD for examination and repair. 
ETX-2i Devices 
2. Installation and Setup 
8. Remove the ESD protective bag from the shelf and set it aside. 
9. Open the accessory kits and boxes. Use your hands to open the boxes. Using a knife to open the 
boxes can result in damaged equipment. 
10. Carefully look at the product and accessories for external damage, dirt, any deformation in the 
pin holes shape, or impurities. If necessary, use canned, dry, oil-free compressed air to blow 
away any impurities.  
11. If any damage occurred during transportation, immediately report the extent of damage by 
filing a claim with the transportation company. Notify your RAD customer service 
representative. Have this information ready: 
 
Invoice number of the shipper 
 
Name of the damaged unit 
 
Serial number and item number of the damaged unit 
 
Description of damage 
 
Effect of damage on the installation 
12. If you need to return damaged equipment to the factory, see Returned Material Authorization 
(RMA). 
13. Order any replacement equipment, if necessary.  
14. Set aside the packaging material and then verify whether the equipment is operational. 
15. Store all the shipping boxes and packaging material so that you can repack the components if 
you need to return any item for repair or possible transport to another installation site. 
 
Caution 
Be careful when you handle and transport an empty ETX‑2i without 
modules. To avoid damage to the backplane connectors, make sure that no 
items fall into the shelf or onto the backplane. 
Package Contents 
The ETX‑2i package includes the ordered unit, as well as the accessories (supplied and orderable) listed 
in the following tables. 
ETX-2i Devices 
2. Installation and Setup 
Supplied Accessories 
Package 
Contents 
ETX-2i 
ETX-2i-B,  
ETX-2i-10G,  
ETX-2i-10G-B, ETX-2i-10G-E 
ETX-2i-100G 
AC External 
Power Supply 
Cable  
Per AC power supply 
module 
Per AC power 
supply module 
Per AC power supply module 
(for indoor models) 
Per AC power 
supply module 
Blanking plugs 
for unused 
glands 
— 
— 
ETX-2i-10G-B/8SFPP Outdoor 
unit  
(WJ-DM-16-VPA) 
— 
Blanking plugs 
for unused 
power 
connector 
— 
— 
ETX-2i-10G-B/8SFPP Outdoor 
unit (28788_7)  
— 
Cable ties 
— 
— 
ETX-2i-10G-B/8SFPP Outdoor 
unit (two per power supply 
cable) 
— 
Circular 3-pin 
female DC 
power 
connector plug  
— 
— 
ETX-2i-10G-B/8SFPP Outdoor 
unit (2440_03_T09CB_T 
Optionally assembled with 
CBL-ETX-2i-10G-ODU-DC 
cable.  
— 
Circular 4-pin 
female AC 
power 
connector plug 
— 
— 
ETX-2i-10G-B/8SFPP Outdoor 
unit (2440_04_T09CB_T) per 
AC power module 
— 
DC Connector 
Kit 
Per DC power supply 
module  
(PLUG-DC/TB-S/J) 
Per DC power 
supply module 
(PLUG-DC-
MC1/BS) 
For DNFV option 
only 
Per DC power supply module 
(PLUG-DC/TB-S/J) 
(for indoor models) 
— 
DC External 
Power Supply 
Cable 
— 
— 
— 
Per DC power 
supply module 
A wire gauge of 
14-18 AWG is 
recommended 
(according to the 
device’s 
consumption) 
ETX-2i Devices 
2. Installation and Setup 
Package 
Contents 
ETX-2i 
ETX-2i-B,  
ETX-2i-10G,  
ETX-2i-10G-B, ETX-2i-10G-E 
ETX-2i-100G 
Mounting Kit 
See Mounting Kits below. 
Safety bracket 
— 
— 
ETX-2i-10G-B/8SFPP Outdoor 
unit 
— 
Orderable Accessories 
Package Contents 
ETX-2i 
ETX-2i-B 
ETX-2i-10G,  
ETX-2i-10G-B 
ETX-2i-10G-E 
ETX-2i-100G 
Waterproof cable 
joiner (adapter) 
— 
— 
ETX-2i-10G-B/8SFPP Outdoor 
unit (SC-L-UL11-03-YW) 
(for adding extension cable) 
— 
Control port cable 
Mini USB cable 
(CBL-MUSB-DB9F) 
Mini USB cable 
(CBL-MUSB-DB9F) 
ETX-2i-10G/4SFPP, 
ETX-2i-10G-B/4SFPP: Mini USB 
cable (CBL-MUSB-DB9F) 
ETX-2i-10G-B/8SFPP: Micro 
USB cable (CBL-UUSB-DB9F) 
ETX-2i-10G-B/8SFPP outdoor: 
RJ-45 cable 
(CBL-RJ45/D9/F/6FT) 
ETX-2i-10G-E: RJ-45 cable  
(CBL-RJ45/D9/F/6FT) 
ETX-2i-100G/4Q, 
ETX-2i-
100G/40G: 
Micro USB cable 
(CBL-USB-DB9F) 
 
Warning 
The Control port (Mini USB or Micro USB connector) acts as a serial port and 
should only be connected to a serial/RS-232 connector. 
Use of a native USB connector (as in a laptop or PC) may cause electrical 
damage.  
DAC-10G cable 
— 
— 
For SFPP ports of indoor models  
Cisco sfp-h10gb-cu3m – for 3 m 
Cisco sfp-h10gb-cu1m – for 1 m 
“copper pigtail” 
DC External Power 
Supply Cable 
— 
— 
ETX-2i-10G-B/8SFPP Outdoor 
unit 
CBL-ETX-2i-10G-ODU-DC (3C18-
2587-BLACK) assembled in 
circular 3-pin female DC power 
connector plug  
— 
ETX-2i Devices 
2. Installation and Setup 
Package Contents 
ETX-2i 
ETX-2i-B 
ETX-2i-10G,  
ETX-2i-10G-B 
ETX-2i-10G-E 
ETX-2i-100G 
Extractable AC 
power supply 
ETX-2i/64E1: 
ETX-2i-PS/AC/64 
(single AC PS) 
ETX-2i-DNFV: 
ETX-2i-PS/ACHP 
(single high-power 
AC PS) 
— 
ETX-2i-10G-B/8SFPP indoor 19-
inch:  
ETX-2i-10G-PS/AC   
ETX-2i-10G-B/8SFPP outdoor: 
ETX-2i-10G-B-PS/H/AC/ODU  
ETX-2i-100G/4Q: 
ETX-2i-100G-
PS/ACF 
Extractable DC 
power supply 
ETX-2i/64E1: 
ETX-2i-PS/DC/64 
(single DC PS) 
— 
ETX-2i-10G-B/8SFPP indoor 19-
inch:  
ETX-2i-10G-PS/DC   
ETX-2i-10G-B/8SFPP outdoor: 
ETX-2i-10G-B-PS/H/DC/ODU  
ETX-2i-100G/4Q: 
ETX-2i-100G-
PS/DCF 
GPON SFP 
SFP-GPON-1DH 
SFP-GPON-1DH 
— 
— 
Enhanced CBL-K21 
AC power cable 
ETX-2i/64E1  
(ETX-2i has built-in 
K.21E AC surge 
protection.) 
Excluding the 2U 
device that has 
built-in K.21E AC 
surge protection  
Full 19-inch  
(The outdoor unit and half 19-
inch models have built-in K.21E 
AC surge protection.) 
  
Lightning arrestor 
— 
— 
ETX-2i-10G-B/8SFPP Outdoor 
with GNSS option 
— 
Mounting Kit 
See Mounting Kits below. 
Optical 
Transceivers 
(Modules) 
SFP  
SFP  
SFP and SFPP  
SFP, SFPP, 
SFP28, QSFP28, 
and QSFPP  
Gland to conduit 
adapter 
— 
— 
Single gland (PG 13.5mm) to 
conduit (NPT 1.25") connector 
adapter, conduit cap (ETX-2i-
10G-ODU-CD-AD) 
— 
Gland to conduit 
adapter (x3) 
— 
— 
Pack of three gland (PG 
13.5mm) to conduit (NPT 
1.25") connector adapters, 
conduit caps (ETX-2i-10G-ODU-
3CD-AD) 
— 
 
ETX-2i Devices 
2. Installation and Setup 
Mounting Kits 
The following table lists the rack, wall, pole, frame, and H-frame mounting kits for ETX‑2i devices. 
Product 
19-inch  
Rack 
23-inch Rack/ 
Frame 
Wall 
Pole 
H-Frame 
ETX-2i  
(8.5-inch) 
RM-35/P1 – one unit 
 
RM-35/P2 – two units  
RM-35-23/P1 –  
one unit 
RM-35-23 –  
two units 
WM-35  
– 
– 
ETX-2i  
(19-inch) 
RM-34 (supplied) –  
one unit 
RM-34-23 –  
one unit 
WM-34 
– 
– 
ETX-2i-64E1 
(19-inch 3U) 
RM-52 (supplied) –  
one unit without cable 
management 
CM-52 – one unit with 
cable management 
– 
– 
– 
– 
ETX-2i-B  
(8.5-inch) 
RM-35/P1 – one unit 
 
RM-35/P2 – two units  
RM-35-23/P1 –  
one unit 
RM-35-23 –  
two units 
WM-35-TYPE4 
– 
– 
ETX-2i-B  
(8.5-inch 2U) 
RM-54/A – one unit 
RM-54/A2 – two units 
– 
– 
– 
– 
ETX-2i-10G 
(8.5-inch) 
RM-35/P1 – one unit 
 
RM-35/P2 – two units  
RM-35-23/P1 –  
one unit 
RM-35-23 –  
two units 
WM-35 
– 
– 
ETX-2i-10G  
(19-inch) 
RM-34 – one unit 
(supplied) 
RM-34-23 –  
one unit 
WM-34 
– 
– 
ETX-2i-10G-B 
(8.5-inch) 
RM-35/P1 – one unit 
 
RM-35/P2 – two units  
RM-35-23/P1 –  
one unit 
RM-35-23 –  
two units 
WM-35 
– 
– 
ETX-2i-10G-B 
(19-inch) 
RM-34 – one unit 
(supplied) 
– 
WM-34 
– 
– 
ETX-2i-10G-B-
8SFPP-ODU  
– 
– 
WM-35-
ODU/45  
(DC) 
WM-35-
ODU/45/H  
(AC/DC)  
WM-35-ODU/P/45 
(DC) 
WM-35-ODU/P/45/H 
(AC/DC) 
WM-35-ODU/45  
(DC) 
WM-35-ODU/45/H  
(AC/DC)  
– or – 
WM-35-ODU/P/45  
(DC) 
WM-35-ODU/P/45/H 
(AC/DC) 
ETX-2i Devices 
2. Installation and Setup 
Product 
19-inch  
Rack 
23-inch Rack/ 
Frame 
Wall 
Pole 
H-Frame 
ETX-2i-10G-E 
(8.5-inch) 
RM-35/P1 – one unit 
 
RM-35/P2 – two units  
RM-35-23/P1 –  
one unit 
RM-35-23 –  
two units 
WM-35 
– 
– 
ETX-2i-100G 
(19-inch) 
RM-50 (supplied) 
RM-53 
(100mm deep or flat 
installation) 
Note: RM-50/19/A  
can also be used for flat 
installation. 
Rack:  
RM-50/23 
Frame:  
RM-50/23F 
– 
– 
– 
Required Tools and Equipment 
Prior to installing the unit, prepare the following, as required: 
• 
Phillips screwdriver to mount the ETX‑2i unit in a rack or on the wall. 
• 
Standard AC external power cable – to connect the unit to a socket indoors.  
• 
DC external power cable – to connect the unit to a socket indoors (for ETX-2i-100G with DC 
power supply)  
• 
Enhanced CBL-K21 AC external power cable (per ITU-K.21 Enhanced mode) to connect the unit 
to a socket in an unprotected power network (such as AC cell site, AC street cabinet, AC pole, or 
rural area). Enhanced cable is selected according to the socket type: 
 
CBL-K21-EURO 
 
CBL-K21-GB 
 
CBL-K21-OPEN  
• 
CBL-MUSB-DB9F serial/RS-232 Mini USB cable to connect the unit’s CONTROL port (RS-232 
interface) to the ASCII supervision terminal. Relevant for ETX-2i, ETX-2i-B, ETX-2i-10G/4SFPP, 
and ETX-2i-10G-B/4SFPP. 
• 
CBL-UUSB-DB9F serial/RS-232 Micro USB to DB9 connector cable to connect the unit’s CONTROL 
port (RS-232 interface) to the ASCII supervision terminal. Relevant for 
ETX-2i-10G-B/8SFPP, ETX-2i-100G/4Q, and ETX-2i-100G/40G. 
• 
CBL-RJ45/D9/F/6FT CONTROL port cable; relevant for ETX-2i-10G-B/8SFPP/ODU (refer to 
Outdoor Unit Power Cable Requirements in Appendix A) 
ETX-2i Devices 
2. Installation and Setup 
• 
Any other cables that are required to connect the unit to remote equipment as per the specific 
application. 
Safety 
Electrostatic Discharge Safety 
The equipment is designed to provide adequate protection against electrostatic discharge (ESD). 
However, it is good working practice to use caution when connecting cables terminated with plastic 
connectors (without a grounded metal hood, such as flat cables) to sensitive data lines. Before 
connecting such cables, discharge yourself by touching the ground or wear an ESD preventive wrist 
strap.  
Grounding Safety 
The unit is intended to be connected to protective ground at all times during normal use. Only skilled 
personnel should perform grounding procedures. 
Provide protective earthing by connecting the mains plug to a wall socket with a protective ground 
terminal. Connect all protective earth terminals provided on the unit to protective ground at all times, 
using an 18 AWG wire or wider. 
 
Warning 
• 
When installing or performing maintenance on the unit, always make 
the protective ground connection first and disconnect it last.  
• 
Do not connect telecommunication cables to ungrounded equipment.  
• 
Make sure that all other cables are disconnected before disconnecting 
the protective ground. 
Laser Safety 
The following laser warning label is affixed near the optical transmitter. 
 
ETX-2i Devices 
2. Installation and Setup 
 
 
This product may be equipped with a laser diode. In such cases, a label with 
the laser class and other warnings as applicable is attached near the optical 
transmitter. The laser warning symbol may also be attached.  
Please observe the following precautions: 
• 
Before turning on the equipment, make sure that the fiber-optic cable is 
intact and is connected to the transmitter. 
• 
Do not attempt to adjust the laser drive current. 
• 
Do not use broken or unterminated fiber-optic cables/connectors or look 
straight at the laser beam. 
• 
The use of optical devices with the equipment increases eye hazard. 
• 
Use of controls, adjustments, or performing procedures other than those 
specified herein may result in hazardous radiation exposure. 
ATTENTION: The laser beam may be invisible! 
Users may insert their own SFP laser transceivers into the product. Users are alerted that RAD cannot be 
held responsible for any damage that may result if non-compliant transceivers are used. In particular, 
users are warned to use only agency approved products that comply with the local laser safety 
regulations for Class 1 laser products. 
Installing the Air Baffle 
In some settings, such as data centers and CO communication rooms, a tight air conditioning design 
mandates front-to-back airflow in order to maximize air conditioning effectiveness. In some settings, 
such as data centers and CO communication rooms, a tight air conditioning design mandates front-to-
back airflow in order to maximize air conditioning effectiveness. Unless your device came with the NEBS 
option that provides front-to-back airflow, you must install the air baffle provided by RAD as explained 
below. 
RAD provides the S2S-F2B-AB air baffle, to drive the side-to-side airflow of ETX-2i-10G-B/8SFPP to 
function as front-to-back airflow. 
Adding the S2S-F2B-AB air baffle to the original 19-inch device widens it to 23 inches, and therefore it 
can be installed in a 23-inch rack cabinet or frame. 
 
 
ETX-2i Devices 
2. Installation and Setup 
Kit Contents 
The Air Baffle kit includes the following: 
• Two airflow leads – 1.FRONT for installation on the left panel; 2.FRONT on the right side 
• Two covers 
• Twelve pan-headed screws 6-32 UNC, 7.9 mm length – six for each lead  
• Twelve spring washers – six for each lead 
• 20 flat-headed screws 4-40 UNC, 4.8 mm length – ten for each cover 
Required Equipment  
Phillips #1 screwdriver (not supplied) 
 
Warning 
Disconnect all cables, including the power cord, from ETX-2i-10G-B/19/8SFPP before 
installing the air baffle. 
 
To install the air baffle on ETX-2i-10G-B/8SFPP: 
1. Align the 1.FRONT air baffle lead with the ETX-2i-10G-B/19/8SFPP left panel with the 1.FRONT 
marking facing frontward, and the screw holes of the lead and device left panel overlapping. 
Correctly fitted baffle leads align with the product edges. Connecting the wrong baffle lead to 
the wrong side results in damaging airflow interruption. 
                    
 
2. Using a Phillips screwdriver, fasten the air baffle lead to the device left panel with the six 
provided pan-headed screws and washers – three on each side. Do not overtighten. 
3. Align the screw holes on the cover with the holes on the air baffle lead, making sure that the six 
round holes on the cover face frontward. 
4. Using a Phillips screwdriver, fasten the cover to the air baffle lead with the ten provided flat-
headed screws. 
5. For frame installation: Align the RM-34 bracket holes with the three back holes in the front 
center of the cover. 
ETX-2i Devices 
2. Installation and Setup 
 
Assembled Air Baffle – Frame Installation 
6. For rack installation: Align the RM-34 bracket holes with the three front holes in the front center 
of the cover. 
 
Assembled Air Baffle – Rack Installation 
7. Using a Phillips screwdriver, fasten the RM-34 bracket to the cover with the three flat-headed 
screws provided with the RM-34 kit.  
8. Repeat steps 1 to 6 to install the air baffle on the right panel of ETX-2i-10G-B/19/8SFPP using the 
2.FRONT air baffle lead.  
ETX-2i Devices 
2. Installation and Setup 
 
Assembling Air Baffle on ETX-2i-10G-B/19/8SFPP 
Mounting the Unit 
It is recommended to install indoor ETX‑2i units as a desktop unit in a horizontal position. In this case, 
place and secure the unit on a stable, non-movable surface.  
ETX‑2i can also be mounted in a 19-inch rack on a wall, on a pole, in a frame (ETX-2i-100G 19-inch), or in 
an H-frame, depending on the enclosure size.  
 
Warning 
ETX‑2i indoor units are intended for use in horizontal orientation only. 
In case of vertical mounting orientation, install the unit on top of concrete or 
other non-combustible surface, such as an external baffle or tray, due to 
safety considerations.  
For detailed instructions on all rack, wall, pole, frame, and H-frame mounting kits of devices covered in 
this manual, refer to the mounting kit supplements at the end of the manual (after the back cover). 
 
Warning 
Before mounting the unit(s), disconnect all cables including the power cord 
from the unit. 
ETX-2i Devices 
2. Installation and Setup 
Installing the D-NFV Module 
Note 
This section is relevant for ETX-2i and ETX-2i-B only.  
You can insert into the rear of the ETX-2i/ETX-2i-B unit, a D-NFV module with an integrated Intel® x86 
core, to enable hosting virtual machines providing virtual network functions (VFs). 
ETX­2i/ETX-2i-B supports hot swapping of the D-NFV module (card), meaning you can insert and extract 
the D-NFV module into the ETX-2i/ETX-2i-B device without interrupting the device’s operation (i.e., 
powering it down).  
Note 
• 
The following procedures are relevant for ETX-2i/ETX-2i-B with a hot-
swappable D-NFV module, indicated by a screw and latch at the top right 
edge on the rear of the ETX-2i/ETX-2i-B unit.  
• 
If you are using an ETX-2i unit that does not support hot swapping, you 
must power down the ETX-2i/ETX-2i-B unit, insert or remove the D-NFV 
module, and then power up the ETX-2i/ETX-2i-B unit again.  
Inserting the D-NFV Module (Hot Swapping)  
 To install the D-NFV module: 
1. For safe insertion of the D-NFV module, disable D-NFV operation by entering config> chassis> 
ve-module> shutdown.  
2. Release the lock knob screw, open the latch, and remove the dummy module. 
   
 
3. Insert the D-NFV module into the now empty device slot. 
ETX-2i Devices 
2. Installation and Setup 
 
4. Push the D-NFV module into the device until it clicks into place. 
 
5. Close all the D-NFV holding screws, close the latch, and secure it with the lock screw. 
 
Note 
Only after the lock is secured in place, the device recognizes that the D-NFV 
card has been inserted.  
6. Enable D-NFV operation by entering config> chassis> ve-module>no shutdown. 
The D-NFV LED turns green, indicating that D-NFV is operational.  
 
 
ETX-2i Devices 
2. Installation and Setup 
Extracting the D-NFV Module (Hot Swapping) 
 To remove the D-NFV module: 
1. In the ETX‑2i command line, enter config> chassis> ve-module> shutdown. 
Wait 60 seconds for the D-NFV green LED to turn off. D-NFV operation is disabled.  
During these 60 seconds, the x86 card downloads its processes, and when finished, performs 
shutdown. 
2. Release the screw and open the latch holding the module in place (see figure in step 4 above). 
3. Pull the D-NFV module out of the slot (see figure in step 3 above). 
4. Insert the dummy module into the slot, close all screws, close the latch, and secure it with the 
lock screw (see figures in step 2 above).  
Grounding and Bonding 
In addition to the general bonding and grounding instructions given in various parts of this manual, this 
section presents procedures that are needed for network telecommunication equipment that is installed 
in large telecommunication centers (central offices) and cell-sites. These requirements are an integral 
part of Telcordia GR-1089-CORE® but are applicable to all such systems. 
The main goals of adequate bonding and grounding are as follows: 
• 
Equalize the potential between several telecommunication units and reduce voltage differences 
that might damage the equipment or present safety hazards. 
• 
Ensure that overcurrent devices such as fuses and circuit breakers operate properly during a 
fault. 
• 
Divert as much as possible of unwanted energy from lightning strikes or transient phenomena 
on the mains supply to ground, by means of surge and transient absorbers. 
• 
Improve electromagnetic compatibility. 
Use the following methods to achieve proper bonding and grounding: 
• 
Connect the mains plug to a socket outlet with a ground connection; this method protects the 
user from electrical shock but is not sufficient to achieve adequate grounding and bonding. 
• 
Connect the ground lug on the front or rear panel of the equipment to a ground bus bar by 
means of a short grounding wire (see below). 
 
 
ETX-2i Devices 
2. Installation and Setup 
• 
Install the equipment in an adequately grounded rack by means of the mounting brackets 
provided with the equipment, to improve the ground connection of the ETX‑2i equipment. To 
mount ETX‑2i, connect the provided mounting adapters to ETX‑2i using star and spring washers. 
Remove any paint that may interfere with the connection. 
• 
Plan carefully the grounding system for the central office or cell-site. 
 
Warning 
If a ground lug is provided on the product, connect it to the protective 
ground at all times, using a wire of diameter 18 AWG or wider.  
ETX‑2i devices are provided with the following types of grounding lugs: 
• 
ETX‑2i NEBS-compliant enclosures for central office or cell-sites have a UL-recognized dual 
grounding lug. 
 
• 
ETX‑2i enclosures that are not NEBS-compliant are provided with a single ring tongue grounding 
lug.  
 
Screws are provided for attaching the grounding lug to ETX‑2i, as well as star or spring washers that 
ensure proper contact and preclude loosening of the screws. 
 
 
ETX-2i Devices 
2. Installation and Setup 
ETX‑2iETX-2i-10G-B/8SFPP, ETX-2i-10G/8SFPP, and ETX-2i-100G/4Q have two grounding lugs attached 
with screws to their front and back panels: 
• 
ETX‑2iETX-2i-10G-B/8SFPP, ETX-2i-10G/8SFPP – a small single hole grounding lug on the right 
side of the front panel  
 
ETX-2i-100G/4Q – a small lug on the left side of the front panel 
 
When connecting this grounding lug to protective ground, use 16 AWG wire.  
• 
A large dual hole grounding lug on the left side of the back panel 
 
ETX-2i-10G-B/8SFPP, ETX-2i-10G/8SFPP ETX‑2i– a horizontal lug on the right side of the back 
panel  
 
ETX-2i-100G/4Q– a vertical lug on the right side of the back panel  
 
When connecting this grounding lug to protective ground, use an 8 AWG wire. 
 To connect a grounded wire to the grounding lug: 
1. Remove the grounding lug from ETX‑2i, ensuring that you keep the washers. 
2. Use 8 AWG copper wire (approximately 6 mm2) for the dual hole grounding lug and 16 AWG 
copper wire (approximately 1.25 mm2) for the ring tongue grounding lug. 
Note 
Do not use any wires other than copper wires for grounding.  
ETX-2i Devices 
2. Installation and Setup 
3. If isolated wire is used, remove the insulation at the end. 
4. Coat the bare wire with an antioxidant material and crimp the bare wire end to the lug, using 
the proper tool. 
5. Reconnect the lug with the crimped wire to ETX‑2i, using the provided screws and washers, and 
connect the other end to the ground bar of the site, keeping the grounding wire as short as 
possible. Ensure that you remove paint that may interfere with good contact. 
Connecting to Power 
 
• 
Connect the unit’s earthing screw to protective ground prior to the 
supply connection.  
• 
Only a skilled person should perform the supply connection using 
permanent means, in accordance with the applicable national code and 
regulations. 
• 
Before connecting or disconnecting any cable, you must connect the 
protective ground terminals of this unit to the protective ground 
conductor of the mains (AC or DC) power cord. If you are using an 
extension cord (power cable), make sure it is grounded as well. 
• 
The suffix “W” must be marked on USA and Canada flexible power 
cables (cords) that are used outdoors.  
• 
Any interruption of the protective (grounding) conductor (inside or 
outside the instrument) or disconnecting of the protective ground 
terminal can make this unit dangerous. Intentional interruption is 
prohibited. 
• 
Remove any metallic object that may come into contact with energized 
parts. 
 
Notes 
• 
Refer also to the Connecting AC Mains and Connecting DC Power sections 
in the Front Matter of this manual.  
• 
Make sure that power cords and cables of outdoor units comply with local 
electrical codes. 
• 
When a unit with an AC or DC power supply loses power, it generates a 
dying gasp event. 
 
 
 
ETX-2i Devices 
2. Installation and Setup 
The following diagram shows the recommended way to connect the ODU to AC or DC power. 
 
Cable line to DC 
Input ODU (+, -)
1.0–1.5 mm²/ 18–16 AWG
UL Approved AC/DC 
charger with internal 
overcurrent and short 
circuit protection 
Two pole Circuit
Breaker 3 ÷ 5A
Two pole Circuit
Breaker 16A (20A)
Two pole Circuit
Breaker 16A (20A)
Battery. 
DC Mains: 40 ÷ 60V
Cable line to AC
Input ODU (L, N)
1.0–1.5 mm²/ 18–16 AWG
PE
Outdoor Power Unit
AC Mains: 
L, N, GND
 
The following warnings and cautions are relevant for Outdoor units. 
 
 
Warning 
• 
Power ETX-2i-10G-B/8SFPP Outdoor ETX‑2i from a ROC system, which 
contains suitable over-current protective devices, to reduce the 
installation category to Overvoltage Category II. 
• 
Before connecting or disconnecting the AC or DC mains connector 
to/from ETX-2i-10G-B/8SFPP Outdoor ETX‑2i, validate that the mains 
circuit breaker in the control panel is set to OFF.  
• 
Activate the Power switch only after the AC or DC mains connector is 
connected to the device. 
• 
Do not touch or tamper with the power supply when the power cord is 
connected. Line voltages may be present inside even when the power 
switch (if installed) is in the OFF position, or a fuse is blown. For DC-
powered products, although the voltage levels are usually not 
hazardous, energy hazards may still exist. 
ETX-2i Devices 
2. Installation and Setup 
 
Caution 
• 
Before turning ON the ETX‑2iAC/DC mains circuit breaker, make sure 
that the AC/DC power connector plugs are in the AC/DC power 
connectors that are installed in the unit, and the bracket is secured into 
place. 
• 
AC and DC sockets are physically different to avoid connecting an AC 
cord to a DC socket. You should not need to apply excessive force to 
make the connection. If in doubt, double-check to avoid damaging the 
equipment. 
AC Power Cables 
ETX‑2i units require a 3 m (10 ft) standard AC external power cable terminated by a standard 3-prong 
socket, to provide AC power to the unit.  
Hardened options of ETX‑2i units used in an unprotected power network, such as AC cell site, AC street 
cabinet, AC pole, or rural area, require an AC Surge Protection Unit to prevent hardware damage caused 
by current surges and voltage spikes. In this unit, a single-phase AC power supply line protector protects 
against lightning overvoltage for both common and differential modes.  
ETX-2i, ETX-2i-10G-B/4SFPP half 19-inch, ETX-2i-10G half 19-inch, and ETX-2i-10G-B/8SFPP Outdoor 
devices have a built-in AC Surge Protection Unit, and therefore, in unprotected power networks, can use 
the standard AC external power cable to provide AC power to the unit even if K.21E is required. 
ETX-2i-64E1, ETX-2i-B (Type 4), ETX-2i-10G 19-inch, ETX-2i-10G-B 19-inch, ETX-2i-10G-B/8SFPP half 19-
inch, and ETX-2i-100G hardened devices do not have a built-in AC Surge Protection unit, and therefore 
require an enhanced CBL-K21 AC external power cable (per ITU-K.21E). 
Under standard conditions, ETX-2i-B (2U) can use a standard AC external power cable for AC power. 
However, in unprotected power networks, you can use the enhanced CBL-K21 AC external power cable 
or ask for a special ordering option that supports K21E. 
The following table summarizes K.21E (enhanced) support in the ETX‑2i family: 
Device 
K.21E Support 
ETX-2i 
No additional support required; has built-in K.21E AC surge protection unit. 
ETX-2i-64E1 
Enhanced CBL-K21 AC external power cable 
ETX-2i-B (2U) 
Not supported in regular device. Requires a special ordering option that 
supports K.21E or enhanced CBL-K21 AC external power cable.  
ETX-2i-B (Type 4) 
Enhanced CBL-K21 AC external power cable 
ETX-2i Devices 
2. Installation and Setup 
Device 
K.21E Support 
ETX-2i-10G half 19-inch 
No additional support required; has built-in K.21E AC surge protection unit 
ETX-2i-10G 19-inch 
Enhanced CBL-K21 AC external power cable 
ETX-2i-10G-B half 19-inch 
ETX-2i-10G-B/4SFPP: No additional support required; has built-in K.21E AC 
surge protection unit. 
ETX-2i-10G-B/8SFPP: Requires enhanced CBL-K21 AC external power cable.  
ETX-2i-10G-B 19-inch 
Enhanced CBL-K21 AC external power cable 
ETX-2i-10G-B-8SFPP-ODU 
No additional support required; has built-in K.21E AC surge protection unit. 
ETX-2i-10G-E half 19-inch 
ETX-2i-10G-E/8SFPP: Requires enhanced CBL-K21 AC external power cable. 
ETX-2i-100G 
Enhanced CBL-K21 AC external power cable 
Connecting a Device with an Integrated PS to AC Power 
 To connect a device with an integrated PS to AC power: 
1. Insert the relevant power cable into the AC power connector on the device. 
 
For indoor installation – standard AC power cable  
 
For connection of hardened units to an unprotected power network – see above table. 
2. Secure the AC power cable with the power cord retainer to avoid unintentional extraction. For 
detailed instructions on securing the AC power cord in the retainer for the various devices, refer 
to Extracting and Inserting Power Supply Units in the Operation and Maintenance chapter. 
3. Connect the power cable to the mains outlet. The unit turns on automatically. 
AC Power Connector – ETX-2i (4 Combo) 
 
AC Power Connector – ETX-2i-B (2 SFP + 2 Combo) 
ETX-2i Devices 
2. Installation and Setup 
 
AC Connector – ETX-2i-B (6 SFP + 4 UTP) 
 
AC Connector – ETX-2i-10G Full 19-inch (4 SFP+, 12 Combo)) 
 
AC Connector – ETX-2i-100G/4Q Full 19-inch (4 QSFP28, 8 SFP28, and 8 SFP+) 
ETX-2i Devices 
2. Installation and Setup 
Note 
*If needed, you can install the power cord retainer into the ETX-2i-100G AC 
power supply by pushing the power cord retainer strap into the AC power 
supply opening(s) (one for Gospower; two for Delta) (see figure below) until it 
snaps into place. 
 
 
Connecting ETX-2i-10G-B/8SFPP Outdoor Unit to AC Power (Gland Connectors) 
The figure below shows ETX-2i-10G-B/H/ACR/ODU/8SFPP with two plastic 4-pin AC power input 
connectors installed in PWR-IN 1 and PWR-IN 2, located on the unit’s front panel.  
ETX-2i Devices 
2. Installation and Setup 
 
Two AC stickers are affixed to the PWR-IN 1 and PWR-IN 2 squares on the top panel of the unit, to 
indicate the types of the connectors (AC) installed in PWR-IN 1 and PWR-IN 2 on the unit’s front panel.  
 
Make sure that the electrical installation complies with local codes. 
Always connect the AC plug to a wall socket with a protective ground. 
The maximum permissible current capability of the branch distribution circuit that supplies power to the 
product is 20A (for USA and Canada).  
Connecting the Power Supply Cable to the Circular AC Power Connector Plug (ETX-2i-10G-B/8SFPP 
Outdoor) 
ETX-2i-10G-B/8SFPP Outdoor is supplied with a kit including two mating circular AC power connector 
plugs for assembling on the AC power supply cables. 
ETX-2i Devices 
2. Installation and Setup 
                                              
 
Power Connector for AC Cable (left) with AC Pinout Front View (right)  
ETX-2i-10G-B/H/ACR/ODU/8SFPP has two AC power supplies, which requires you to assemble both AC 
power connector plugs with AC power supply cables. Before doing so, you should remove the blanking 
plug (factory installed) from the AC power connector plug. 
ETX-2i-10G-B/H/AC/ODU/8SFPP has one AC power supply, which requires you to assemble one AC 
power connector plug with a AC power supply cable. For this model, you should keep the blanking plug 
(factory installed) in the other AC power connector plug. 
The AC power supply cable wiring requirements are as follows: 
• 
Solid or stranded wires 
• 
Wire gauge – 16-18 AWG according to product’s current consumption   
Connect the wires of your power supply cable to the circular AC connector plug, according to the voltage 
polarity and assembly instructions provided below. Repeat for the second AC power connector plug. 
Caution 
Prepare all connections to the circular AC connector plugs before inserting 
into the connectors installed in PWR-IN 1 and PWR-IN 2 on the front panel of 
the unit.   
 To assemble the power supply cables: 
1. Disassemble the circular AC power connector plug, as seen in the picture below. 
 
2. Thread the power cable through the disassembled parts of the AC power connector plug. 
Note 
It is recommended to label the cable as AC. 
3. Solder the three power cable wires to the three AC connector pins (see encircled pins in above 
photo), as follows:  
ETX-2i Devices 
2. Installation and Setup 
 
Brown wire to Pin 1 (P) 
 
Blue wire to Pin 2 (N) 
 
Green/yellow wire to Pin 3 (GND) 
4. Reassemble the circular AC power connector plug. 
5. Remove the blanking plug from the second AC power connector plug and perform steps 1 to 4. 
Connecting the Assembled AC Power Connector Plugs to the Unit (ETX-2i-10G-B/8SFPP Outdoor) 
After you have assembled the AC power connector plugs, connect them to the two circular 4-pin AC 
power input connectors installed in PWR-IN 1 and PWR-IN 2 on the unit. 
In the case that you assemble only one power supply, a blanking plug is supplied for sealing protection 
of the unused power connector.  
A safety bracket with a captive screw is supplied for installation around the power supplies, to prevent 
unintentional extraction of the installed cable connectors. 
Be sure to fix the power supply cables to the safety bracket using cable ties, so that the power 
connectors comply with strain relief requirements. 
 To connect the AC power supply connector plugs to the unit: 
1. Connect the circular AC connector plug (assembled with the power supply cable) into the 
circular AC connector installed in PWR-IN 1, matching the pins, until it snaps into place. 
2. Connect the second circular AC power connector plug (assembled with the power supply cable) 
into the circular AC connector installed in PWR-IN 2, matching the pins, until it snaps into place. 
ETX-2i Devices 
2. Installation and Setup 
 
ETX-2i-10G-B/8SFPP With Connected AC Power Connectors 
3. Install the supplied safety bracket, by positioning it around the power connector plugs, inserting 
its captive screw in the hole to the left of the power connectors (circled in above picture), and 
securing it into place. 
4. Fix each power cable to the safety bracket with two cable ties. 
                      
 
 To remove an AC power connector plug: 
1. Open the cable ties fixing the power cables to the safety bracket.  
2. Release the safety bracket’s captive screw and remove the bracket.  
3. Depress the pushbutton on the AC connector while pulling it out from the AC circular connector 
on the device. 
ETX-2i Devices 
2. Installation and Setup 
 
Connecting the Unit to AC Power 
 To connect the unit to AC power: 
1. Make sure the mains circuit breaker is set to OFF.  
2. Connect the AC mains to the unit. 
3. Turn ON the mains circuit breaker. 
Connecting an Indoor Unit to DC Power (ETX-2i, ETX-2i-10G, ETX-2i-10G-B, and ETX-2i-B) 
 
DC Power Connector – ETX-2i-B (8.5-inch dual DC, 2 SFP + 4 UTP) 
 
DC Power Connector – ETX-2i (19-inch ACDC, 8 Combo ports) 
 
DC Power Connectors – ETX-2i-10G-B (19-inch DCR, 8SFPP) 
AC/DC adapter (AD) plugs are available for establishing a wide-range DC power supply connection. 
Terminal block connectors are available for establishing a regular DC power supply connection. 
The following procedures describe how to connect to DC power.   
ETX-2i Devices 
2. Installation and Setup 
 To connect to DC power: 
1. Wire the DC connection to the power cable and connect the assembled DC power cable to the 
unit. 
See the relevant DC Power Supply Connection section below for detailed instructions: 
AC/DC Adapter (AD) Plug for Wide-Range DC Power Supply Connection 
OR 
Terminal Block Connector for Regular DC Power Supply Connection. 
2. Connect the power cable to the mains outlet. 
The unit turns on automatically. 
AC/DC Adapter (AD) Plug for Wide-Range DC Power Supply Connection 
Certain units are equipped with a wide-range AC/DC power supply. These units are equipped with a 
standard AC-type 3-prong power input connector located on the unit’s rear panel. This power input 
connector can be used for both AC and DC voltage inputs. 
For DC operation, a compatible straight AC/DC Adapter (AD) or 90-degree AD plug for attaching to your 
DC power supply cable is orderable with your RAD product. 
                                   
  
Straight AD Plug                                             90-Degree AD Plug 
The DC power supply cable wiring requirements are as follows: 
• 
Solid or stranded wires 
• 
Wire gauge – 14-18 AWG according to product’s current consumption  
You can connect the wires of your DC power supply cable to the AD plug, according to the voltage 
polarity and assembly instructions provided below. 
Note 
Prepare all connections to the AD plug before inserting it into the unit’s power 
connector. 
ETX-2i Devices 
2. Installation and Setup 
 To prepare the AD plug and connect it to the DC power supply cable: 
1. Loosen the cover screw on the bottom of the AD plug to open it (see figure below). 
2. Run your DC power supply cable through the removable cable guard and through the open cable 
clamp. 
3. Place each DC wire lead into the appropriate AD plug wire terminal according to the voltage 
polarity mapping shown. Afterwards, tighten the terminal screws closely. 
4. Fit the cable guard in its slot and then close the clamp over the cable. Tighten the clamp screws 
to secure the cable. 
5. Reassemble the two halves of the AD plug and tighten the cover screw. 
 To connect the assembled power supply cable to the unit:  
1. Connect the assembled power supply cable to the unit. After inserting the plug, verify that the 
blue (negative) wire is connected to POWER and the brown (positive) wire is connected to 
RETURN. 
 
AD Plug Details 
ETX-2i Devices 
2. Installation and Setup 
 
• 
Reversing the wire voltage polarity will not cause damage to the unit, 
but the internal protection fuse will not function. 
• 
Always connect a ground wire to the AD plug’s chassis (frame) ground 
terminal. Connecting the unit without a protective ground, or 
interrupting the grounding (for example, by using an extension power 
cord without a grounding conductor) can damage the unit or the 
equipment connected to it! 
• 
The AD adapter is not intended for field wiring. 
Terminal Block Connector for Regular DC Power Supply Connection  
Certain DC-powered units are equipped with a plastic 3-pin VDC-IN power input connector, located on 
the unit’s rear panel. Different variations of the connector are shown in the following figure. All are 
functionally identical. 
 
Supplied with such units is a kit including a mating Terminal Block (TB) type connector plug for attaching 
to your power supply cable. 
 
 
ETX-2i Devices 
2. Installation and Setup 
The DC power supply cable wiring requirements are as follows: 
• 
Solid or stranded wires 
• 
Wire gauge – 14-18 AWG according to product’s current consumption   
Connect the wires of your power supply cable to the TB plug, according to the voltage polarity and 
assembly instructions provided on the following pages. 
Caution 
Prepare all connections to the TB plug before inserting it into the unit’s 
VDC-IN connector.  
 To prepare and connect the power supply cable with the TB Plug: 
Note 
See the following figure for assistance.  
1. Strip the insulation of your power supply wires according to the dimensions shown. 
2. Place each wire lead into the appropriate TB plug terminal according to the voltage polarity 
mapping shown in the figure below. (If a terminal is not already open, loosen its screw.) 
Afterwards, tighten the three terminal screws to close them.  
3. Pull a nylon cable tie (supplied) around the power supply cable to secure it firmly to the TB plug 
grip, passing the tie through the holes on the grip. 
4. Isolate the exposed terminal screws/wire leads using a plastic sleeve or insulating tape to avoid 
a short circuit.  
 To connect the assembled power supply cable to the unit (ETX-2i, ETX-2i-10G, ETX-2i-10G-B, ETX-
2i-10G-E and ETX-2i-B): 
1. Insert the TB plug into the unit’s VDC-IN connector until it snaps into place. 
 
ETX-2i Devices 
2. Installation and Setup 
TB Plug Assembly  
 
Mapping of the Power Supply Wire Leads to the TB Plug Terminals  
 
• 
Reversing the wire voltage polarity can cause damage to the unit! 
• 
Always connect a ground wire to the TB plug’s chassis (frame) ground 
terminal. Connecting the unit without a protective ground, or 
interruption of the grounding (for example, by using an extension power 
cord without a grounding conductor) can cause harm to the unit or to 
the equipment connected to it and can be a safety hazard to personnel 
operating it! 
 
Note 
Certain TB plugs are equipped with captive screws for securing the assembled 
cable’s TB plug to the unit’s VDC-IN connector (C and E types only). To secure 
the plug, tighten the two screws on the plug into the corresponding holes on 
the sides of the input connector as shown in the following figure. 
ETX-2i Devices 
2. Installation and Setup 
 
TB Plug with Captive Screws (optional) 
 To disconnect the TB plug: 
1. If the TB plug is equipped with captive screws, loosen the captive screws (see figure above). 
2. If the unit’s VDC-IN connector is type B, lift the locking latch  
(see Connector B in the first figure of this section5). 
3. Pull out the TB plug carefully. 
Note 
Always lift the locking latch of type B connectors before disconnecting the 
TB plug, to avoid damaging the TB plug. 
Connecting ETX-2i-100G to DC Power 
 
DC Power Connectors – ETX-2i-10G-B (19-inch DCR, 4QSFP, 16SFPP) 
You can connect ETX-2i-100G to DC power, as follows: 
• 
A device with an AcBel DC power supply – using a DC PS cable  
(see Connecting ETX-2i-100G with an AcBel DC Power Supply to DC Power below). 
• 
A device with a Delta or Gospower DC power supply – using a DC adapter  
(see Connecting ETX-2i-100G with a Delta or Gospower DC Power Supply to DC Power below). 
ETX-2i Devices 
2. Installation and Setup 
For further description of these power supplies and how to extract/insert them from/into the device, 
refer to Extracting/Inserting an ETX-2i-100G Unit Power Supply in the Operation and Maintenance 
chapter. 
Connecting ETX-2i-100G with an AcBel DC Power Supply to DC Power 
ETX-2i-100G with an AcBel DC PS is supplied with a PS cable connected to a terminal block (TB) plug. 
Note 
It is not advisable to disconnect the power supply cable from the TB plug.  
 To connect to DC power: 
1. Insert the TB plug into the unit’s VDC-IN connector until it snaps into place.  
 
TB Plug Assembly (ETX-2i-100G) 
 
Mapping of the Power Supply Wire Leads to the TB Plug Terminals (ETX-2i-100G) 
2. Connect the power cable to the mains outlet. The unit turns on automatically. 
Connecting ETX-2i-100G with a Delta or Gospower DC Power Supply to DC Power 
ETX-2i-100G with a Delta or Gospower DC PS is supplied with a DC adaptor and three terminals for 
connecting DC wires. 
ETX-2i Devices 
2. Installation and Setup 
 To connect to DC power: 
1. Using a crimping tool, connect DC wires into the three terminals supplied with the adapter: one 
wire per terminal. 
2. On the adapter, remove the cover from the terminal blocks. 
3. Release the three silver terminal screws on the terminal blocks. 
4.  Insert each terminal into the appropriate terminal block, as follows: 
 
– black wire 
 
+ red wire 
 
Ground yellow/green wire  
 
5. Close the three silver terminal screws on the terminal blocks securely. 
6. Cover the DC adapter terminal blocks.  
ETX-2i Devices 
2. Installation and Setup 
 
7. Insert the DC adapter into the PSU’s D-Sub connector until it clicks into place and then close the 
black screws above and below the terminal block to secure it into place. 
Note 
The D-Sub adaptor on a Delta PS is identical to that on a Gospower PS; they 
are installed in opposite directions (rotated 180 degrees), and therefore the 
adaptor is inserted into the Delta with its terminals on the right, and into the 
Gospower, with its terminals on the left.  
      
 
Left: Inserting DC Adapter into Delta PS; Right: Inserting DC Adapter into Gospower PS 
8. Connect the DC power cord to the mains outlet. The unit turns on automatically. 
9. Check that the Power LED on the device front panel is green, and that the corresponding PS LED 
on the PSU panel is green. 
ETX-2i Devices 
2. Installation and Setup 
Connecting ETX-2i-10G-B/8SFPP Outdoor Unit to DC Power (Gland Connectors) 
The figure below shows ETX-2i-10G-B/H/DCR/ODU/8SFPP with two plastic 3-pin DC power input 
connectors installed in PWR-IN 1 and PWR-IN 2, located on the unit’s front panel.  
 
Two 48 VDC stickers are affixed to the PWR-IN 1 and PWR-IN 2 squares on the top panel of the unit, to 
indicate the types of the connectors (DC) installed in PWR-IN 1 and PWR-IN 2 on the unit’s front panel.  
 
ETX-2i-10G-B/8SFPP Outdoor is supplied with two mating circular DC power connector plugs, one with a 
blanking plug. 
Optionally, it can be ordered with the following: 
• 
A mating circular DC power connector plug per power supply, assembled with a DC power 
supply cable (CBL-ETX-2i-10G-ODU-DC) 
ETX-2i Devices 
2. Installation and Setup 
 
• 
A waterproof cable connector (adapter), used to add an extension cable (customer provided) to 
the DC power supply cable 
 
Connecting a Power Supply Cable to the Circular DC Power Connector Plug  
Note 
This section is only relevant for the circular DC power connector plug supplied 
without a DC power cable.  
The device is supplied with a kit including a mating circular DC power connector plug for assembling on a 
DC power supply cable, for each ordered DC power supply. 
Below is a DC power connector plug (without a cable) and the DC pinout front view. 
                                              
 
DC Power Connector Plug (left) with DC Pinout Front View (right) 
ETX-2i Devices 
2. Installation and Setup 
ETX-2i-10G-B/H/DCR/ODU/8SFPP has two DC power supplies, which requires you to assemble both DC 
power connector plugs with DC power supply cables. Before doing so, you should remove the blanking 
plug (factory installed) from the DC power connector plug. 
ETX-2i-10G-B /H/DC/ODU/8SFPP has one DC power supply, which requires you to assemble one DC 
power connector plug with a DC power supply cable. For this model, you should keep the blanking plug 
(factory installed) in the other DC power connector plug. 
The DC power supply cable wires meet the following requirements: 
• 
Solid or stranded wires 
• 
Wire gauge – 16-18 AWG according to product’s current consumption   
Connect the wires of your power supply cable to the circular DC connector plug, according to the voltage 
polarity and assembly instructions provided below.  
 To assemble the power supply cable: 
1. Disassemble the circular DC connector plug, as seen in the picture below. 
 
2. Thread the power cable through the disassembled parts of the connector plug. 
Note 
It is recommended to label the cable as DC. 
3. Solder the three power cable wires to the three DC connector pins (see encircled pins in above 
photo), as follows:  
 
Black wire to Pin 1 (-) 
 
Red wire to Pin 2 (+) 
 
Green/yellow wire to Pin 3 (GND)  
4. Reassemble the circular DC connector plug. 
5. For the DCR option, remove the blanking plug from the second DC power connector plug, and 
perform steps 1 to 4. 
Adding an Extension Cable to the DC Power Supply Cable 
Note 
This section is relevant when you add an extension cable to the DC power 
supply cable installed in the circular DC power connector plug.  
ETX-2i Devices 
2. Installation and Setup 
ETX-2i-10G-B can be ordered with a waterproof cable joiner (adapter) (PN: SC-L-UL11-03-YW) for joining 
the DC power supply cable to an extension cable. 
 
The following illustration shows the parts of the cable joiner. The left and right sides are symmetrical.  
 
The parts include: 
• 
Two end caps (gland nuts) with rubber grummets completely sealing both ends 
• 
Two yellow seals  
• 
Two gaskets (durable plastic housing) encasing the cylinder with a TB block (three-pole wire 
connector socket) on each end. 
 
 
• 
Reversing the wire voltage polarity can cause damage to the unit! 
• 
Always connect a ground wire to the TB plug’s ground terminal. 
Connecting the unit without a protective ground, or interruption of the 
grounding (for example, by using an extension power cord without a 
grounding conductor) can cause harm to the unit or to the equipment 
connected to it and can be a safety hazard to personnel operating it! 
 To add an extension cable to the DC power supply cable: 
1. Remove the connector cable joiner (adapter) from the packaging.  
2. Disassemble the connector cable joiner (adapter). Each side disassembles into a weatherproof 
end cap (gland nut), yellow seal, and gasket (plastic housing). 
ETX-2i Devices 
2. Installation and Setup 
 
3. Slide the end cap over the DC power supply cable, then the yellow seal, and then the gasket 
(three parts on the left).  
4. Push the seal into the gasket and tighten the end cap onto the gasket. 
5. Strip the insulation off the end of the DC power supply cable. Splice the three wires to ¼-inch 
and make sure that they are nicely twisted.  
6. In the TB adapter, unscrew the three screws on the left TB block in the TB plug. 
7. Place each DC power supply cable wire lead into the appropriate TB block terminal according to 
the voltage polarity mapping.  
 
Black wire to Pin L (-) 
 
Red wire to Pin N (+) 
 
Yellow/green wire to Pin 
 (GND) 
 
8. Tighten the three terminal screws to close them. Carefully use pliers to make sure that the wires 
are secured in place. 
9. Repeat steps 3 to 8 with the extension cable and the parts on the right side.  
10. Plug in to test that the connection is complete. 
Connecting the Assembled DC Power Supply Connector Plugs to the Unit  
The following procedure describes how to connect a DC power connector plug assembled with a DC 
power supply cable (RAD or customer provided) or a blanking plug, to the circular 3-pin DC power input 
connectors installed in PWR-IN 1 and PWR-IN 2 on the unit. 
A safety bracket with a captive screw is supplied for installation around the power supplies, to prevent 
unintentional extraction of the installed cable connector. 
ETX-2i Devices 
2. Installation and Setup 
Be sure to fix the power supply cables to the safety bracket using cable ties, so that the power 
connectors comply with strain relief requirements. 
Caution 
Prepare all connections to the circular DC connector plugs before inserting 
them into the unit’s PWR-IN 1 and/or PWR-IN 2 connectors.  
 To connect the DC power supply connector plugs to the unit: 
1. Connect the circular DC power connector plug (assembled with the DC power supply cable) to 
the circular DC connector installed in PWR-IN 1, matching the pins, until it snaps into place. 
2. Connect the second circular DC power connector plug (for the DCR model, assembled with a DC 
power supply cable; for the DC model, with a blanking plug) to the circular DC connector 
installed in PWR-IN 2, matching the pins, until it snaps into place. 
 
Connecting Two DC Connector Plugs to the Circular DC Power Connectors 
 
ETX‑2i With Connected DC Power Connectors 
ETX-2i Devices 
2. Installation and Setup 
3. Install the supplied safety bracket by positioning it around the power connector plugs, inserting 
its captive screw in the hole to the left of the power connector plugs (circled in above picture), 
and securing it in place. 
4. Fix each power cable to the safety bracket with two cable ties. 
          
 
 To remove a DC power connector plug: 
1. Open the cable ties fixing the power cables to the safety bracket. 
2. Release the safety bracket’s captive screw and remove the bracket.  
3. Depress the pushbutton on the DC power connector plug while pulling it out from the device. 
 
Connecting the Unit to DC power 
 To connect the unit to DC power: 
1. Make sure the mains circuit breaker is set to OFF. 
2. Connect the DC mains to the unit. 
3. Turn ON the mains circuit breaker. 
Connecting ETX-2i-10G-B/8SFPP/CD Outdoor Unit to DC Power (Conduit Connectors) 
The figure below shows the inside of ETX-2i-10G-B/H/DCR/ODU/8SFPP/CD with an example of a typical 
wiring setup. There are three liquid tight connectors (conduit adapter) through which the data and 
power wires are passed. Red wires are positive, black are negative, and yellow are ground.  
ETX-2i Devices 
2. Installation and Setup 
 
 
Note 
It is recommended to use the rightmost connector (labeled 3) for DC power. 
The other two can be used for data and management wires. 
 To connect DC power supply wiring to the unit: 
1. Slide the wiring cover (colored light blue in the above image) to expose the power terminal 
block. 
2. Thread your power supply wire bundle through the liquid tight connector. 
3. There are various latches in the open space inside the unit. Use these to secure your wires with 
cable ties: 
 
ETX-2i Devices 
2. Installation and Setup 
4. Wire as shown in the first image, above. Be sure to match positive, negative, and ground to the 
appropriate terminals. There is a label for positive and negative next to the terminals: 
 
5. Connect ground of each power supply to the two screws marked below: 
 
6. Return the wire cabinet cover to its original position and secure it with its screw. 
 
 
ETX-2i Devices 
2. Installation and Setup 
 To connect the outdoor unit to ground (method 1): 
1. Thread the ground cable through this gland: 
 
2. Fasten ground to the internal grounding lug marked in the image below: 
ETX-2i Devices 
2. Installation and Setup 
 
 
 
 
ETX-2i Devices 
2. Installation and Setup 
 To connect the outdoor unit to ground (method 2): 
• 
Fasten ground directly to the external grounding lug marked in the image below: 
 
Connecting the Unit to DC power 
 To connect the unit to DC power: 
1. Make sure the mains circuit breaker is set to OFF. 
2. Connect the DC mains to the unit. 
3. Turn ON the mains circuit breaker. 
 
 
ETX-2i Devices 
2. Installation and Setup 
Connecting to Ethernet Equipment 
You can connect an ETX‑2i device to Ethernet equipment, as follows: 
• 
By connecting its fiber optic Ethernet interface to the Ethernet port of a peer device via a fiber 
optic cable with an LC/MPO connector on each end. The fiber optic interface is an SFP (1G), SFPP 
(10G), SFP28 (25G), QSFPP (40G), or QSFP28 (100G) port. 
• 
By connecting its copper Ethernet interface (RJ-45 port) to the Ethernet port of a peer device via 
a copper Ethernet cable with an RJ45 8-pin connector on each end. 
You can connect ETX‑2i to Ethernet equipment via the connectors described in the following table, 
according to the relevant option: 
Device 
Connectors 
ETX-2i  
Fiber optic LC connector designated GbE/100Fx (combo port) 
8-pin RJ-45 electrical connector designated 10/100/1000BT (combo port) 
ETX-2i-B 
Fiber optic LC connector designated GbE/100Fx (standard port, combo port) 
8-pin RJ-45 electrical connector designated 10/100/1000BT (combo port) 
ETX-2i-10G 
Fiber optic LC connector designated GbE/100Fx (standard port, combo port) 
Fiber optic LC connector designated 10GbE 
8-pin RJ-45 electrical connector designated 10/100/1000BT 
ETX-2i-10G-B 
Fiber optic LC connector designated GbE/100Fx (standard port) 
Fiber optic LC connector designated 10GbE/1GbE 
8-pin RJ-45 electrical connector designated 10/100/1000BT 
ETX-2i-10G-E 
Fiber optic LC connector designated GbE/100Fx (standard port) 
Fiber optic LC connector designated 10GbE/1GbE 
ETX-2i-100G 
Fiber optic LC connector designated 100GbE 
Multi-fiber Push On optic MPO connector designated 100GbE 
Fiber optic LC connector designated 10GbE/1GbE 
Fiber optic LC connector designated 40GbE (for Fiber optic LC connector designated 
100GbE/40G) 
Connecting Ethernet Equipment with Fiber Optic Interface 
The following figures show the ETX‑2i device’s fiber optic ports that are used for connecting to Ethernet 
equipment. 
ETX-2i Devices 
2. Installation and Setup 
 
GbE Fiber Optic Ports – ETX-2i (4 Combo) 
 
GbE Fiber Optic Ports – ETX-2i-B (2 SFP + 2 Combo) 
 
GbE Fiber Optic Ports – ETX-2i-B (2 SFP + 4 UTP) 
 
GbE Fiber Optic Ports – ETX-2i-B 2U with 10 SFP 
ETX-2i Devices 
2. Installation and Setup 
 
GbE Fiber Optic Ports – ETX-2i-10G/ETX-2i-10G-B Half 19-inch (4 SFP+, 4 SFP, and 4 UTP) 
 
GbE Fiber Optic Ports – ETX-2i-10G-E Half 19-inch (8 SFP+) 
 
GbE Fiber Optic Ports – ETX-2i-10G Full 19-inch (4 SFP+, 12 Combo) 
  
GbE Fiber Optic Ports – ETX-2i-10G-B Full 19-inch (4 SFP+, 4 SFP, and 4 UTP) 
 
GbE Fiber Optic Ports – ETX-2i-10G-B (8 SFP+) Full 19-inch  
ETX-2i Devices 
2. Installation and Setup 
 
GbE Fiber Optic Ports – ETX-2i-10G-B (8 SFP+) Half 19-inch 
 
GbE Fiber Optic Ports – ETX-2i-10G-B (8 SFP+) Outdoor 
Note 
Removing the cap from the spare opening (enclosed in a green circle in the 
above front panel) will impact the IP rating and may void the warranty. 
 
 
GbE Fiber Optic Ports – ETX-2i-100G/4Q Full 19-inch (4 QSFP28, 8 SFP28, and 16 SFP+) 
You can connect ETX‑2i to Ethernet equipment in one of the following ways:  
• 
By inserting the LC/MPO connector of a relevant optical transceiver into an 
SFP/SFP+/SFP28/QSFP28/QSFP+ port of the device, connecting one end of the optical fiber in 
the transceiver, and the other end to the port in the Ethernet equipment.  
 
You can install into an ETX‑2i SFP (1G) Ethernet port, a RAD-approved SFP optical 
transceiver. 
ETX-2i Devices 
2. Installation and Setup 
 
You can install into an ETX‑2i SFP+ (1/10G) Ethernet port any of the following RAD-approved 
optical transceivers (modules): SFP, SFP+, or dual rate SFP (1GbE/10GbE). 
 
You can install into an ETX-2i-10G-B/8SFPP outdoor unit SFP+ (1/10G) Ethernet port PG-13.5 
cable gland, a RAD-approved SFP+ transceiver.  
 
You can install into an ETX-2i-10G-B/8SFPP/CD outdoor unit SFP+ (1/10G) Ethernet port 
liquid tight connector, a RAD-approved SFP+ transceiver.  
 
You can install into an ETX-2i-100G QSFP28 (100G) Ethernet port, a RAD-approved QSFP28 
optical transceiver. 
 
You can install into an ETX-2i-100G SFP28 (1/10/25G) Ethernet port, a RAD-approved SFP28 
optical transceiver. 
 
You can install into an ETX-2i-100G-40G QSFP+ (40G) Ethernet port, a RAD-approved QSFP+ 
optical transceiver. 
• 
By inserting the SFPP module at one end of a direct attach copper cable (DAC-10G) into the 
device SFP+ port, and the SFPP module at the other end into the Ethernet equipment port. Only 
relevant for connecting the SFP+ port of ETX-2i-10G/4SFPP, ETX-2i-10G-B/4SFPP, and  
ETX-2i-100G/4Q to Ethernet equipment up to 3 m away (versions 6.8.2 (0.59), 6.8.2 (0.60)).  
 
Note 
Use shielded cables when connecting to Ethernet ports.  
The following table summarizes the relevant optical transceivers. 
Optical Transceiver 
Rate 
Device 
Ports 
QSFP28 
100 G 
ETX-2i-100G/4Q 
100G ports 3/1, 3/2, 3/3, 3/4 
ETX-2i-100G-40G 
100G ports 3/3, 3/4 
QSFPP 
40 G 
ETX-2i-100G-40G 
40G ports 3/1 and 3/2 
SFP28 
25 G 
ETX-2i-100G/4Q 
1/10/25G ports 2/1 through 
2/8 
SFP 
1 G 
All devices with 1G and 1/10G ports 
1G and 1/10G ports 
SFPP  
1/10 G 
All devices with 1/10G ports 
1/10G ports 
 
 
Third-party SFP/SFP+/QSFP28/QSFP+ optical transceivers must be RAD-
approved, complying with the local laser safety regulations for Class I laser 
equipment, as well as safety approved to IEC 60825 and CDRH registered. 
Use of unapproved third-party transceivers voids the RAD warranty. 
ETX‑2i device speed can be set using the speed-duplex command. The following table provides the 
functional speed, which depends upon the inserted optical transceiver and speed & duplex setting. 
ETX-2i Devices 
2. Installation and Setup 
Inserted Optical 
Transceiver 
Speed&Duplex 
= 1G 
Speed&Duplex 
= 10G 
Speed&Duplex 
= 25G 
Speed&Duplex 
= 100G 
Speed&Duplex 
= Auto 
1G SFP 
1 Gb 
1 Gb 
NA 
NA 
1G 
10G SFPP 
NA 
10 Gb 
NA 
NA 
10G 
1/10G dual rate 
SFP 
1 Gb 
10 Gb 
NA 
NA 
10G 
SFP28 
NA 
NA 
25 Gb 
NA 
25G 
QSFP28 
NA 
NA 
NA 
100G 
NA 
MPO connector 
NA 
NA 
NA 
100G 
NA 
 
Note 
• 
Autodetection fails if there is a problem detecting the speed of the 
transceiver. 
• 
If the transceiver inserted into the SFPP port does not support 1GbE or 
10GbE, the transceiver inserted into the SFP28 port does not support 
25GbE, or the transceiver inserted into the QSFP28 port does not support 
100GbE, an SFP mismatch alarm is raised. The alarm clears when a valid 
transceiver is inserted. 
• 
When installing a QSFP28 optical transceiver, certain installation 
conditions such as long fiber lines or an attenuating environment, may 
require you to manually configure the FEC functionality to ON. 
 
Caution 
When calculating your optical link budget, always take into account adverse 
effects of temperature changes, optical power degradation, and so on. To 
compensate for signal loss, leave a 3 dB margin. For example, instead of 
maximum receiver sensitivity of -28 dBm, consider the sensitivity measured 
at the Rx side to be -25 dBm. 
Installing a DAC-10G Cable 
A DAC-10G cable consists of shielded Twinax copper cable with pluggable connectors on either end with 
varying gauges from 24 to 30 AWG. It can be used to connect an SFPP port of an ETX‑2i device to 
Ethernet equipment located up to three meters away.   
ETX-2i Devices 
2. Installation and Setup 
 
The following table describes the available DAC-10G cables. 
SFP Transceiver Module 
Transceiver Description 
SFP-H10GB-CU1M 
Cisco 10GBASE-CU passive Twinax SFP+ cable assembly, 1 meter 
SFP-H10GB-CU3M 
Cisco 10GBASE-CU passive Twinax SFP+ cable assembly, 3 meters 
 To install a DAC-10G cable: 
1. Attach an ESD wrist strap to yourself and a properly grounded point on the chassis or rack. 
2. Remove the dust cover from the DAC cable connector. 
3. Gently push the SFP module at the end of the DAC cable into the 10G fiber optic port until it 
clicks into place. 
 To remove a DAC-10G cable: 
1. Attach an ESD wrist strap to yourself and a properly grounded point on the chassis or rack. 
2. Hold the cable and gently pull the rubber pull release tab to pull out the transceiver SFP module. 
Installing an SFP/SFPP Optical Transceiver 
When installing SFP, SFPP and QSFP transceivers, verify that you insert them in the correct orientation. If 
the device has two rows of connectors, the ones in the lower row must be installed in the opposite 
orientation as the ones in the upper row as illustrated below for the QSFP modules: 
ETX-2i Devices 
2. Installation and Setup 
 
 To install an SFP or SFPP optical transceiver: 
1. Attach an ESD wrist strap to yourself and a properly grounded point on the chassis or rack. 
2. Lock the wire latch of the transceiver by lifting it up until it clicks into place, as illustrated for 
SFPs in the figure below. 
Note 
Some optical transceiver models have a plastic door instead of a wire latch.  
 
3. Carefully remove the dust covers from the SFP/SFPP port on the device. 
 
 
ETX-2i Devices 
2. Installation and Setup 
1. Insert the rear side of the SFP transceiver into the slot and push slowly backwards to mate the 
connectors until the transceiver clicks into place. If you feel resistance before the connectors are 
fully mated, retract the transceiver using the wire latch as a pulling handle, and then repeat the 
procedure (after making sure the port is free of obstacles). 
Caution 
Insert the SFP gently. Using force can damage the connecting pins.  
2. Remove the protective rubber caps from the transceivers. 
 To remove an SFP or SFPP transceiver: 
1. Attach an ESD wrist strap to yourself and a properly grounded point on the chassis or rack. 
2. Disconnect the fiber optic cables from the transceiver. 
3. Unlock the wire latch by lowering it (opposite direction of locking). 
4. Hold the wire latch and pull the transceiver out of the Ethernet port.  
Installing a QSFP28 or QSFPP Optical Transceiver 
 To install a QSFP28 or QSFPP optical transceiver: 
1. Attach an ESD wrist strap to yourself and a properly grounded point on the chassis or rack. 
2. Remove the QSFP28/QSFPP transceiver module from its protective packaging. 
 
3. Check the label on the QSFP28/QSFPP transceiver to verify that you have the correct model for 
your network. 
4. Remove the optical bore dust plug from the transceiver and set it aside. 
5. Carefully remove the dust covers from the QSFP28/QSFPP port on the device. 
6. Align the QSFP28/QSFPP transceiver in front of the QSFP28/QSFPP port and carefully slide it into 
the port until the transceiver makes contact with the port’s electrical connector and it clicks into 
place. The transceiver should slide in smoothly. 
ETX-2i Devices 
2. Installation and Setup 
Caution 
• 
Insert the optical transceiver gently. Using force can damage the 
connecting pins. 
• 
If you feel resistance before the connectors are fully mated, retract the 
transceiver using the handle as a pulling handle, and then repeat the 
procedure (after making sure the port is free of obstacles). 
• 
If the transceiver is not fully engaged in the port, you might accidentally 
disconnect it. 
7. Reinstall the dust plug into the transceiver’s optical bore until you attach the network interface 
cable.  
 To remove a QSFP28/QSFPP optical transceiver: 
1. Attach an ESD wrist strap to yourself and a properly grounded point on the chassis or rack. 
2. Disconnect the fiber optic cables from the QSFP28/QSFPP transceiver connector. 
3. Grasp the transceiver handle and pull it toward you. This releases the QSFP28/QSFPP transceiver 
from the QSFP28/QSFPP port electrical connector, and it slides out of the port smoothly. 
4. Install the dust plug into the transceiver’s optical bore. 
5. Install the dust covers on the QSFP28/QSFPP port. 
Installing an SFPP Optical Transceiver in an ETX-2i-10G-B/8SFPP Outdoor Unit (Gland Connectors) 
 To connect a fiber optic cable to an ETX-2i-10G-B/8SFPP outdoor unit SFPP port: 
1. Unscrew the top cap from the SFP+ cable gland connector. There is no need to unscrew the 
entire connector from the device. 
 
2. Remove the toothed bushing from the SFP+ cable gland connector. 
ETX-2i Devices 
2. Installation and Setup 
  
3. Remove the slotted rubber insert from the toothed bushing. 
 
4. Pass an optical LC or RJ cable through the cap, and then through the toothed bushing and 
rubber insert. 
 
 
5. Return the rubber insert into the toothed bushing. 
 
6. Insert the cable into the SFP+ cable gland connector. 
 
Insert the toothed bushing into the SFP+ cable gland connector and twist the top cap until the 
cable is tight with the rubber insert. 
ETX-2i Devices 
2. Installation and Setup 
       
 
 
Note 
The cable is not an outdoor standard and is shown for presentation purposes 
only. 
 
Note 
Liquid tight connectors can be inserted into the glands, using the ETX-2i-10G-
ODU-CD-AD gland to 0. adapter. An ETX-2i-10G-B/8SFPP outdoor unit 
supports up to three adapters. 
Installing an SFPP Optical Transceiver in an ETX-2i-10G-B/8SFPP/CD Outdoor Unit (Conduit Connectors) 
The figure below shows the inside of ETX-2i-10G-B/H/DCR/ODU/8SFPP/CD with an example of a typical 
wiring setup. There are three liquid tight connectors (conduit adapters) through which the data and 
power wires are passed. Light yellow wires in the image represent optical fiber. 
ETX-2i Devices 
2. Installation and Setup 
 
 
 
Note 
It is recommended to use the rightmost connector (labeled 3) for DC power. 
The other two can be used for data and management wires. 
 To connect a fiber optic cable to an ETX-2i-10G-B/8SFPP/CD outdoor unit SFPP port: 
1. Thread your fiber optic cable through the liquid tight connector. 
2. Secure the fiber to the latches in the open space inside the unit, as shown above. 
3. Insert the SFP transceiver into one of the SFP ports:  
ETX-2i Devices 
2. Installation and Setup 
 
4. Plug LC connectors into the SFP transceivers. 
 
Notes 
• 
Any unused conduits must be closed with a blank cover to avoid dust and 
moisture entering the unit. 
• 
These instructions assume a separate cable management box where fiber 
optic bundles are separated into individual optical cables. Alternatively, 
ETX-2i-10G-B/8SFPP/CD includes internal connectors for cable 
management. 
• 
The blank cover next to the connectors can alternatively be ordered as an 
RJ45 gland with an internal connection to a control port. 
Connecting to Ethernet Equipment with Copper Interface 
 To connect to Ethernet equipment having a copper interface: 
• 
Connect ETX‑2i to the Ethernet network equipment using a standard straight STP cable 
terminated with an RJ-45 connector. Refer to the Connection Data appendix for the RJ-45 
connector pinout. 
ETX-2i Devices 
2. Installation and Setup 
 
The following applies to all intra-building Ethernet ports with a copper 
interface (RJ-45): 
• 
The ports are suitable for connection to intra-building or unexposed 
wiring or cabling only. The intra-building port(s) of the equipment or 
subassembly MUST NOT be metallically connected to interfaces that 
connect to the OSP or its wiring. These interfaces are designed for use as 
intra-building interfaces only (Type 2 or Type 4 ports as described in 
GR-1089-CORE) and require isolation from the exposed OSP cabling. The 
addition of primary protectors is not sufficient protection in order to 
connect these interfaces metallically to OSP wiring. 
• 
The ports must use shielded intra-building cabling/wiring that is 
grounded at both ends. The ground connection must be stable and with 
low impedance, in order to ensure that surge currents, which can 
develop due to ground potential rise, do not cause very high voltages to 
develop on the ETH isolation transformer. 
 
Note 
To comply with electromagnetic compatibility requirements, it is 
recommended to use Category 6E shielded twisted pairs (STP) cables.  
 
 
Ethernet Electrical Connectors – ETX-2i (4 Combo) 
 
Ethernet Electrical Connectors – ETX-2i-B (2 SFP + 2 Combo) 
ETX-2i Devices 
2. Installation and Setup 
  
Ethernet Electrical Connectors – ETX-2i-10G/ETX-2i-10G-B Half 19-inch (4 SFP+, 4 SFP, and 4 UTP) 
 
Ethernet Electrical Connectors – ETX-2i-10G Full 19-inch (4 SFP+, 12 Combo) 
Connecting to Alarm Equipment  
Note 
This section is relevant for ETX-2i, ETX-2i-B, ETX-2i-10G, and ETX-2i-100G 
devices with alarm connectors. 
The alarm port is terminated in a 9-pin flat connector, designated ALARM. This port includes: 
• 
Floating change-over dry-contact outputs for the major and minor alarm relays. The alarm relay 
contacts are rated at maximum 30 VDC across open contacts, and maximum 2 ADC through 
closed contacts or 125 VAC across open contacts, and maximum 0.5 AAC through closed 
contacts (total load switching capacity of up to 60W resistive load). 
 
Caution 
Protection devices must be used to ensure that the contact ratings are not 
exceeded. For example, use current limiting resistors in series with the contacts, 
and place voltage surge absorbers across the contacts.  
The relays are controlled by software, and therefore the default state (that is, the state during 
normal operation) can be selected by the user in accordance with the specific system 
requirements. 
• 
+12V auxiliary voltage output (through a 1600Ω series resistor) 
• 
External alarm sense input. The input accepts an RS-232 input signal; it can also be connected by 
means of a dry-contact relay to the auxiliary voltage output. 
0
ETX-2i Devices 
2. Installation and Setup 
 To connect to the ALARM connector: 
• 
Connect a cable that meets the specific requirements of the site to the ALARM connector. Refer 
to Appendix A for connector pin functions. 
Caution 
To prevent damage to the internal alarm relay contacts, it is necessary to 
limit, by external means, the maximum current that may flow through the 
contacts (maximum allowed current through closed contacts is 2A). The 
maximum voltage across the open contacts must not exceed 30 VDC. 
 
 
Alarm Connector – ETX-2i (4 Combo) 
 
Alarm Connector – ETX-2i-B (2 SFP + 2 Combo) 
 
Alarm Connector – ETX-2i-B (6 SFP + 4 UTP) 
 
Alarm Connector – ETX-2i-10G Full 19-inch (4 SFP+, 12 Combo)) 
 
Alarm Connector - ETX-2i-100G/4Q Full 19-inch (4 QSFP28, 8 SFP28, and 8 SFP+) 
ETX-2i Devices 
2. Installation and Setup 
Connecting to E1/T1 Equipment 
Note 
This section is relevant only for the following: 
• 
ETX-2i with E1/T1 network module  
• 
ETX-2i with 64 built-in E1 ports 
If you ordered ETX‑2i with E1/T1 network ports, you can connect ETX‑2i to E1/T1 equipment via the 
RJ-45 connectors designated E1/T1.  
Note 
• 
You must configure the module with the correct module type (ETX-2i only). 
• 
Configure the E1/T1 ports as E1 or T1 ports. 
Refer to the Cards and Ports chapter for details on configuring the module 
type or E1/T1 ports.  
 To connect to E1 or T1 equipment: 
• 
Connect an E1 or T1 line to the RJ-45 connector designated E1/T1 (1–4/8). Refer to the 
Connection Data appendix for the RJ-45 connector pinout.  
 
E1/T1 Ports – ETX-2i 
 
64 E1 Ports – ETX-2i 
ETX-2i Devices 
2. Installation and Setup 
Connecting to the Station Clock 
Note 
This section is relevant only for ETX-2i or ETX-2i-10G ordered with a timing 
option that includes a station clock port.  
You can connect ETX‑2i to an external clock source via a dedicated station clock port, an RJ-45 connector 
designated EXT CLK. Refer to the Connection Data appendix for the connector pinout.  
 
EXT CLK Connector – ETX-2i 
 
EXT CLK Connector – ETX-2i-10G-B/8SFPP 
You can connect the station clock port to a balanced or unbalanced clock source. Make sure that you 
configure the station clock interface type accordingly (refer to the Timing and Synchronization chapter 
for details on configuring the station clock). 
Note 
The cable length between the station clock port and the external clock source 
must not exceed six meters (19.7 feet).  
Connecting to a Balanced Clock Source 
 To connect ETX‑2i to a balanced clock source: 
• 
Connect the station clock port to the clock source using a shielded standard UTP cable 
terminated with an RJ-45 connector. Refer to the Connection Data appendix for the RJ-45 
connector pinout. 
Connecting to an Unbalanced Clock Source 
Connecting to equipment with an unbalanced interface requires you to convert the RJ-45 connector to a 
pair of BNC female connectors, to receive the clock signal via one of the connectors and transmit the 
signal via the other.  
ETX-2i Devices 
2. Installation and Setup 
 To connect ETX‑2i to an unbalanced clock source: 
1. Connect the RJ-45 connector of the adapter cable to the station clock port. 
2. Connect the external clock source to the receiving BNC connector of the adapter cable. 
3. Connect the transmitting BNC connector of the adapter cable to the equipment that should 
receive the clock signal. 
Connecting to Synchronization Equipment 
Note 
This section is relevant only for ETX-2i, ETX-2i-B,  
ETX-2i-10G/4SFPP, ETX-2i-10G-B/4SFPP, and ETX-2i-10G-B/8SFPP ordered 
with a timing option that includes the EXT CLK/1PPS ports and/or the 
ToD/1PPS port.  
ETX‑2i can transmit a 1PPS signal for synchronization, as well as connect to an external clock, via two 
SMA connectors designated EXT CLK and 1PPS. Alternatively, the device can transmit a ToD (Time of 
Day) and 1PPS signal for synchronization, via an RS-422 RJ-45 connector designated ToD/1PPS. Refer to 
the Connection Data appendix for the ToD/1PPS connector pinout. 
Note 
The cable length between the ToD/PPS and EXT CLK/1PPS ports, and the 
external synchronization equipment, must not exceed six meters (19.7 feet).  
 To connect to EXT CLK and 1PPS: 
• 
Connect ETX‑2i to the synchronization equipment using standard SMA cables terminated with 
SMA connectors. 
 To connect to ToD/1PPS: 
• 
Connect ETX‑2i to the synchronization equipment using a proprietary RAD cable terminated with 
a male RS-422 RJ-45 connector. 
 
EXT CLK and 1PPS Connector – ETX-2i 
ETX-2i Devices 
2. Installation and Setup 
 
ToD/1PPS Connector – ETX-2i  
 
EXT CLK and 1PPS Connector – ETX-2i-10G Half 19-inch 
 
ToD/1PPS Connector – ETX-2i-10G Half 19-inch 
 
EXT CLK and 1PPS Connector –ETX-2i-10G-B/8SFPP Full 19-inch 
 
ToD/1PPS Connector –ETX-2i-10G-B/8SFPP Full 19 
Note 
ETX-2i-10G-B/8SFPP/ODU EXT CLK and 1PPS connectors are internal. 
ETX-2i Devices 
2. Installation and Setup 
Connecting to T3 Equipment 
Note 
This section is relevant only for the modular option with T3 network module.  
You can connect ETX-2i to T3 equipment via the BNC coaxial connectors on the network module. 
Note 
You must configure the module with the correct module type. Refer to the 
Cards and Ports chapter for details.  
 To connect to T3 equipment: 
1. Connect the Rx cable to the BNC connector labeled Rx. 
2. Connect the Tx cable to the BNC connector labeled Tx. 
 
T3 Ports – ETX-2i 
Connecting to a Terminal 
You can connect the ETX‑2i RS-232 interface (designated CONTROL) to a laptop equipped with an ASCII 
terminal emulation application, such as PuTTY, via an 8-pin RJ-45 connector (ETX-2i-10G-B/8SFPP/ODU), 
serial/RS-232 Mini USB connector (ETX-2i, ETX-2i-B, ETX-2i-10G/4SFPP, ETX-2i-10G-B/4SFPP) or 
serial/RS-232 Micro USB connector (ETX-2i-10G-B/8SFPP, ETX-2i-100G/4Q). Refer to the Connection 
Data appendix for the connector pinout. 
Caution 
• 
Terminal cables must have a frame ground connection.  
• 
Use ungrounded cables when connecting a supervisory terminal to a DC-
powered unit with floating ground.  
• 
Using an improper terminal cable may result in damage to the 
supervisory terminal port.  
• 
Connecting the RS-232 Micro-USB directly to a computer native USB 
connector (e.g., when using a regular mobile phone charging cable) may 
result in electrical damage. 
 
 
ETX-2i Devices 
2. Installation and Setup 
 To connect to an ASCII terminal: 
1. Connect the RJ-45 connector of CBL-RJ45/D9/F/6FT cable (ETX-2i-10G-B/8SFPP/ODU),  
serial/RS-232 Mini USB connector of CBL-MUSB-DB9F cable (ETX-2i, ETX-2i-B, ETX-2i-10G) or 
serial/RS-232 Micro USB connector of CBL-UUSB-DB9F cable (ETX-2i-10G-B/8SFPP, ETX-2i-
100G/4Q) , available from RAD, to the unit’s CONTROL connector (RS-232 interface). 
2. Connect the DB9 end of the CBL-RJ45/D9/F/6FT or CBL-MUSB-DB9F/CBL-UUSB-DB9F cable to a 
computer equipped with an ASCII terminal emulation application (or use a DB9 to USB 
conversion cable from RS-232 to native USB format – not supplied). 
 
Note 
After completing the configuration of the terminal, disconnect the terminal 
and leave the CONTROL port open.  
 
 
CONTROL Connector – ETX-2i 
 
CONTROL Connector – ETX-2i-B 
 
CONTROL Connector – ETX-2i-10G, ETX-2i-10G-B/4SFPP Half 19-inch 
ETX-2i Devices 
2. Installation and Setup 
 
Control Connector – ETX-2i-10G-B/4SFPP Half 19-inch 
 
Control Connector – ETX-2i-10G-B/8SFPP Full 19-inch  
 
Control Connector – ETX-2i-10G-B/8SFPP Half 19 
 
Control Connector – ETX-2i-10G-B/8SFPP Outdoor 
ETX-2i Devices 
2. Installation and Setup 
 
 
 
Control Connector – ETX-2i-100G/4Q Full 19-inch (4 QSFP28, 8 SFP28, and 8 SFP+) 
Connecting to a Network Management System 
You can connect ETX‑2i to a remote network management system via the dedicated Ethernet 
management port, an 8-pin RJ-45 connector designated MNG-ETH. Refer to the Connection Data 
appendix for the connector pinout. 
 To connect to an NMS: 
• 
Connect ETX‑2i to an Ethernet switch. 
 
Ethernet Management Connector – ETX-2i 
 
Ethernet Management Connector – ETX-2i-B 
ETX-2i Devices 
2. Installation and Setup 
 
Ethernet Management Connector – ETX-2i-10G Half 19-inch 
 
Ethernet Management Connector – ETX-2i-10G-B Half 19-inch 
 
Ethernet Management Connector – ETX-2i-100G/4Q Full 19-inch (4 QSFP28, 8 SFP28, and 8 SFP+) 
Inspection following Installation 
No. 
Item 
1 
Secure installation of device and connectors. 
2 
Screws are tightened securely. 
3 
Cables are correctly connected without loose ends. 
4 
Cable wiring meets design requirements. 
5 
Data cables and cable connectors are not damaged or broken.  
6 
The radius of curvature of an optical fiber should be 20 times greater than the diameter. 
In general, it should be greater than 40 mm. 
7 
Labels on both ends of the data cable should be correct, distinct, and neat. 
8 
Power cables and ground cables are connected correctly and reliably. 

## 2.4 Software Installation  *(p.167)*

ETX-2i Devices 
2. Installation and Setup 
No. 
Item 
9 
Power cables and ground cables comply with engineering design documents. 
10 
Power cables and data cables are laid separately. 
11 
If there is a screw for the power cable, the screw is tightened. 
12 
The power cable and ground cables are properly connected.  
13 
Space for heat dissipation is reserved around the device. No heavy object is laid on the device. 
 
Caution 
Before you leave the installation site, it is highly recommended that you test 
network connectivity between the device and the remote network 
management system (for example, by sending a ping). 
2.4 Software Installation 
ETX‑2i comes installed with the latest SW version. This section explains how to install the current SW 
version on existing HW (upgrade to the latest version).  
The following software releases can be upgraded to Ver. 6.8.5: Ver. 5.8x, 5.9x, 6.0x, 6.2x, 6.3x, 6.4x, 6.5x, 
6.6x, 6.7x, 6.8x. 
Software upgrade is required to fix product limitations, enable new features, or make the unit 
compatible with other devices that are already running the new software version. 
The device can store up to two software images, referred to as software packs. It is recommended to 
name these software packs sw-pack-1 and sw-pack-2. You can designate any of the software packs as 
active. 
Note 
You can define only two software packs simultaneously. Although the CLI 
allows you to name the SW packs sw-pack-1 through sw-pack-4, it is 
recommended to name them sw-pack-1 and sw-pack-2.   
The x86 module in ETX­2i and ETX­2i-B with DNFV can store up to two software images, named im-sw-
pack-1 and im-sw-pack-2. It can also store two software update files, named im-sw-update-1 and im-sw-
update-2. 
The non-active device software packs and integrated module software pack serve as backup if the active 
software becomes corrupted. 
ETX-2i Devices 
2. Installation and Setup 
Note 
If you need to install both the host and module software, install one of them, 
wait for the process to finish, and then install the other.  
• 
You can download application software to ETX‑2i via SFTP/TFTP using the copy command, or via 
XMODEM, FTP, or TFTP, from the Boot screen. Application software/update can be downloaded 
to the x86 module in ETX­2i and ETX­2i-B with DNFV via SFTP only, using the copy command. 
• 
You can install the downloaded device software pack as the active software via the admin 
software install sw-pack-n command, or from the Boot screen. 
• 
You can install the downloaded integrated module software pack/update as the active software 
from the hosting device (ETX­2i/ETX­2i-B) CLI via the admin software install im-sw-pack-n or 
admin software install im-sw-update-n command. 
The information in this section includes the following: 
• 
Software packs that can be loaded into each device and integrated module 
• 
Detailed conditions required for the software installation 
• 
Any impact the software installation may have on the system 
• 
Description of downloading options 
 
Note 
Software upgrade relates to upgrading from the product’s previous version to 
current version. To upgrade from an older version, you may not be able to 
upgrade directly to the latest version, but may be required to upgrade one 
version at a time. Refer to the relevant User Manual for upgrade instructions.   
Software Packs 
Each ETX‑2i software download can contain two sw-packs from the available options listed in the 
following table. 
Device 
File Name 
Description 
ETX-2i 
SW-PACK_2i_x_x_x-x_x.bin 
Device with router capabilities (i.e., 
includes OSPF and BGP dynamic routing 
protocols) 
Example: sw-pack_2i_6_8_5-1_27.bin 
SW-PACK_2i_sr_x_x_x-x_x.bin 
Device with capabilities of static router, 
i.e., without dynamic routing protocols 
ETX-2i Devices 
2. Installation and Setup 
Device 
File Name 
Description 
ETX-2i-B 
SW-PACK_2iB_x_x_x-x_x.bin 
Device with router capabilities 
SW-PACK_2iB_sr_x_x_x-x_x.bin 
Device with capabilities of static router  
ETX-2i-B-x86 
ETX-2i-B 10 ports 
SW-PACK_2iB_10x1G_x_x_x-x_x.bin 
Device with router capabilities 
SW-PACK_2iB_10x1G_sr_x_x_x-x_x.bin 
Device with capabilities of static router 
ETX-2i-10G 
ETX-2i-10G half 19-
inch 
ETX-2i-10G-B half 
19-inch 
SW-PACK_2i_10G_x_x_x-x_x.bin 
Device with capabilities of static router, 
i.e., without dynamic routing protocols 
SW-PACK_2i_10G_LC_x_x_x-x_x.bin 
ETX-2i-10G-
B/8SFPP 
ETX-2i-10G-
B/8SFPP 
ETX-2i-10G-E 
SW-PACK_2i_10G_B_8SFPP_x_x_x-x_x.bin 
Device for 10G aggregation with low-
scale services. 
SW-PACK_2i_10G_B_8SFPP_x_x_x-x_x.bin 
ETX-2i-100G/4Q 
SW-PACK_2i_100G_4Q_x_x_x-x_x.bin 
Device with capabilities of static router, 
i.e., without dynamic routing protocols 
Impact 
During the software upgrade process, service is disrupted. 
Prerequisites 
Prior to upgrading via SFTP/FTP/TFTP, verify that you have the following: 
• 
Operational ETX‑2i unit with valid IP parameters configured  
• 
Connection to a PC with an SFTP/FTP/TFTP server application and a valid IP address 
• 
Software image file stored on the PC. The image file (and exact name) can be obtained from the 
local RAD business partner from whom the device was purchased. 
Prior to upgrading via XMODEM, verify that you have the following: 
• 
Operational ETX‑2i unit 
• 
Connection to a PC via a terminal emulation program 
ETX-2i Devices 
2. Installation and Setup 
• 
Software image file stored on the PC. The image file (and exact name) can be obtained from the 
local RAD business partner from whom the device was purchased. 
Software Installation via CLI  
You can upgrade the following software using CLI commands: 
• 
ETX‑2i software 
• 
x86 module software (in ETX-2i and ETX-2i-B with DNFV) 
• 
PMC software (in ETX-2i) 
Note 
Old PMC software (with TWAMP Light only) cannot be upgraded to new PMC 
software (with Full TWAMP, TWAMP Light, ICMP Echo, and UDP Echo). 
Upgrades are available only after the new PMC has been installed.  
The recommended software downloading method is to use the copy command. 
Network administrators can use this procedure to distribute new software releases to all the managed 
ETX‑2i units in the network from a central location. 
Installing Software via TFTP/SFTP  
Use the following procedure to download software release 6.8.5 to ETX‑2i via TFTP/SFTP. 
1. Verify that the image file is stored on the PC with the SFTP/TFTP server application. 
2. Verify that the ETX‑2i router has been configured with valid IP parameters (see Verifying the 
Host Parameters). 
3. Ping the PC to verify the connection (see Pinging the PC). 
4. Activate the SFTP/TFTP server application (see Activating the SFTP Server or Activating the TFTP 
Server). 
5. Download the image file from the PC to ETX‑2i. 
6. Install the image. 
You can use the above procedure to download a new software release or update to the x86 module in 
ETX­2i and ETX­2i-B with DNFV, but via SFTP only. TFTP is not supported. 
Note 
Configuration values shown in this chapter are examples only.  
ETX-2i Devices 
2. Installation and Setup 
Verifying the Host Parameters 
In order to be able to establish communication with the SFTP/TFTP server, the ETX‑2i router must have 
IP parameters configured according to your network requirements. Refer to the following manual 
sections for additional information: 
• 
Connecting to a Terminal in the Installation and Setup chapter 
• 
Working with Terminal in the Configuration and Management Methods chapter  
• 
Router in the Traffic Processing chapter 
Pinging the PC 
Check the integrity of the communication link between ETX‑2i and the PC by pinging the PC from ETX‑2i.  
 To ping the PC: 
1. In any level, start pinging the PC specifying its IP address and optionally the number of packets 
to send: 
ping <ip-address> [number-of-packets <num-packets>][payload-size <bytes>] 
Where 
num-packets can be 1-10,000 or 0 (forever) for a continuous ping. Default is 5. 
bytes can be 32-1450.  
A reply from the PC indicates a proper communication link. 
2. If the ping request times out, check the link between ETX‑2i and the PC (physical path, 
configuration parameters, etc.).  
Activating the SFTP Server 
Once the SFTP server is activated on the PC, it waits for any SFTP file transfer request originating from 
the product and carries out the received request automatically.  
SFTP file transfers are carried out through TCP port 22. Make sure that the firewall you are using on the 
server allows communication through this port (refer to the Administration chapter for details).  
Activating the TFTP Server 
Once the TFTP server is activated on the PC, it waits for any TFTP file transfer request originating from 
the product and carries out the received request automatically.  
ETX-2i Devices 
2. Installation and Setup 
TFTP file transfers are carried out through port 69. Make sure that the firewall you are using on the 
server allows communication through this port (refer to the Administration chapter for details).  
Note 
Configure the connection timeout of the TFTP server to be more than 
30 seconds to prevent an automatic disconnection during the backup partition 
deletion (about 25 seconds).  
Downloading the New Device Software Release File 
This procedure is used to download a new ETX‑2i software version.  
You can now choose to pass the password interactively, which means entering it separately when 
prompted and not passing it with the syntax as illustrated below. 
When using the interactive option, each typed character is masked with an ‘*’, avoiding password 
exposure on the command line. When using the non-interactive option, the password is visible in the 
command line. 
Note 
The copy command is global, therefore do not issue it with any prefix. 
 To copy the image file to the ETX‑2i unit using SFTP and passing the password non-interactively: 
• 
On any level, enter: 
copy sftp://<username>:<password>@<ip-address>/<image-file-name> <sw-pack-n> 
Where <ip-address> is the IP address of the PC where the SFTP server is installed and <n> is the 
index of the software pack. 
 To copy the image file to the ETX‑2i unit using SFTP and passing the password interactively: 
• 
On any level, enter: 
copy sftp://<username>@<ip-address>/<image-file-name> <sw-pack-n> 
Where <ip-address> is the IP address of the PC where the SFTP server is installed and <n> is the 
index of the software pack.  
When using this option, you have to enter the password when prompted. 
 To copy the image file to the ETX‑2i unit using TFTP: 
• 
On any level, enter: 
copy tftp://<tftp-ip-address>/<image-file-name> <sw-pack-n>  
Where tftp-ip-address is the IP address of the PC where the TFTP server is installed and <n> is 
the index of the software pack. 
ETX-2i Devices 
2. Installation and Setup 
Note 
Choose an index that is not being used by the active software, or by a 
software pack that you do not want to overwrite.  
The software download is performed. See Activating the Software for instructions on installing 
the downloaded software as the active software.  
Downloading the New x86 Module Software Release/Update File 
This section describes how to download a new software version or update into the integrated x86 
module of ETX­2i/ETX­2i-B with DNFV, using SFTP (TFTP cannot be used).  
Note 
Although the x86 module has its own software images, which are not part of 
the ETX­2i/ETX­2i-B software images, you use the copy command from the 
hosting device (ETX­2i/ETX­2i-B) to download the x86 module software 
packs/updates. In this case, the hosting device passes the copy command to 
the x86 module for execution. The module executes the command and reports 
the results to the hosting device for further processing (e.g., displays a 
message, generates an event)  
 To copy the image file to the x86 module: 
• 
In any level, enter: 
copy sftp://<username>:<password>@<ip-address>/<image-file-name> 
{<im-sw-pack-n> | <im-sw-update-n>} 
Where <ip-address> is the IP address of the PC where the SFTP server is installed and <n> is the 
index of the x86 module software pack/update. 
The software download is performed. See Activating the Software  for instructions on installing 
the downloaded software as the active software.  
If you wish to separately enter the password when prompted, do not enter <password> in the 
syntax above. 
Installing the Device Software 
After software is downloaded to ETX‑2i, it has to be installed via the install command. When you install 
software, by default ETX‑2i creates a restore point, so that if there is a problem with the new software 
pack, you can perform a rollback to the previous software pack and startup-config file. This ensures that 
if you changed the startup-config file before noticing that something was wrong with the newly installed 
software, you can restore the startup-config that was running before the last installation. 
Note 
The file startup-config must exist before you can install software with creation 
of a restore point.  
ETX-2i Devices 
2. Installation and Setup 
Prior to installing the software, you can request (via command software-confirm-required) that the user 
confirm the next installed software (via command software-confirm) following the next ETX‑2i reboot. 
This software confirmation command verifies that the user has regained connection to the device 
following installation. If confirmation is requested, but the user does not confirm the software (via 
command software-confirm) within the configured timeout period, ETX‑2i automatically falls back to its 
previous software. This precaution prevents a permanent loss of connection to the remote device 
following installation.  
 To request software confirmation: 
• 
At the admin>software# prompt, enter: 
software-confirm-required [time-to-confirm <minutes>] 
The confirmation timeout can be from five minutes to 24 hours. If you do not specify it, the 
default is five minutes. 
Note 
You can cancel the software confirmation request by entering 
no software-confirm-required.  
Next time ETX‑2i reboots and loads new software, it starts a confirmation timer. See the 
following procedure for more details on the confirmation. 
 To install a device software pack: 
Note 
• 
If startup-config does not exist, you must install the software pack 
without creating a restore point. 
• 
As a defective startup-config can cause a loss of connection, it is not 
recommended to install software and change startup-config at the same 
time. However, if you must do both at the same time, first install the 
software and only after verifying it, make the needed configuration 
changes (or vice versa).  
1. At the admin>software# prompt, enter: 
install <sw-pack-n> [no-restore-point] 
Where n is 1 to 4, provided sw-pack-n is a non-active software pack. If you specify 
no-restore-point, then after the software is installed, it is not possible to roll back to the 
previous software. 
You are prompted to confirm the operation. 
!Device will install file and reboot. Are you sure? [yes/no] _ 
2. Type yes to confirm. 
ETX-2i Devices 
2. Installation and Setup 
If a restore point is being created, then startup-config is copied to restore-point-config. ETX‑2i 
designates the specified software pack as active, then reboots. If a software confirmation 
request is active, ETX‑2i starts a timer with the specified timeout period. 
Note 
While the confirmation timer is running, ETX‑2i does not allow any commands 
that change its configuration.  
3. If you enter the software-confirm command before the timer expires, the software is 
considered confirmed. 
If you do not enter software-confirm before the timer expires, installation of the new SW pack 
is not confirmed, restore-point-config is deleted, ETX‑2i rolls back to the previously active 
software pack (designates it as active), and then ETX‑2i reboots. 
Note 
If the software pack is activated on ETX­2i/ETX­2i-B that is host to an x86 
module, only the ETX­2i/ETX­2i-B host reboots; the x86 card does not reboot.  
 
Software Installation via Boot Screen  
Software downloading can also be performed from the Boot screen. The Boot screen can be reached 
while ETX‑2i performs initialization, such as after power-up.  
You may need to start the loading from the Boot screen if you are unable to use the copy command (for 
example, because the ETX‑2i software has not yet been downloaded or is corrupted). 
Caution 
The Boot screen procedures are recommended only for use by authorized 
personnel, as they provide many additional options that are intended for 
use only by technical support personnel.  
The following software downloading options are available from the Boot screen: 
• 
Downloading using the XMODEM protocol. This is usually performed by downloading from a PC 
directly connected to the CONTROL DCE port of the unit. 
• 
Downloading using FTP/TFTP. This is usually performed by downloading from a remote location 
that provides an IP communication path to an Ethernet port of ETX‑2i. 
The Boot screen can be accessed when the device is powered up, before logging in. 
 
 
ETX-2i Devices 
2. Installation and Setup 
 To access the Boot screen: 
1. Connect the ASCII terminal or PC with terminal emulation to the ETX‑2i CONTROL port. 
2. Configure the communication parameters of the selected PC serial port for asynchronous 
communication with 9600 bps, no parity, one start bit, eight data bits, and one stop bit. Turn all 
types of flow control off. 
3. Power off ETX‑2i. 
4. Activate the terminal application. 
5. Power on ETX‑2i and immediately start pressing the <Enter> key several times in sequence until 
you see the prompt to press any key to stop the autoboot.  
6. Press any key. 
The Boot screen appears. A typical Boot screen is shown below (the exact version and date 
displayed by your ETX‑2i unit may be different).   
 
Note 
If you miss the timing, ETX‑2i performs a regular reboot process (this process 
starts with Loading/un-compressing sw-pack-<n> and ends with the login 
screen).  
 
System Boot 
 
          Copyright 1984-2008  RAD Data Communications, Ltd. 
 
 
                Boot version: 1.05 [May 26 2015] 
 
 
CPU        : Freescale P1015E - Security Engine 
OS version : VxWorks 6.9 
BSP version: 1.0/3 
Boot-Manager version: 3.02 [Oct 19 2014] 
 
Use '?'/help to view available commands 
 
 
Press any key to stop auto-boot... 
1 
[boot]: 
 
 
ETX-2i Devices 
2. Installation and Setup 
7. Enter ? to display a list of boot commands. 
Commands: 
 ?/help                           - print this list 
 p                                - print boot parameters 
 c [param]                        - change boot parameter(s) 
 v                                - print boot logo with versions information 
 run                              - load active sw pack and execute 
 delete <FileName>                - delete a file 
 dir                              - show list of files 
 show <index>                     - show sw pack info 
 download <index> [,<FileName|x>] - download a sw pack to specific index (x - by Xmodem) 
 set-active <index>               - Set a sw pack index to be the active application 
 control-x/reset                  - reboot/reset 
8. Enter p to display all boot parameters.  
The boot parameters appear. A typical boot parameter list is shown below (see the following 
table for details on the boot parameters). 
[boot]: p 
 
file name       (fn) : vxWorks 
device IP       (ip) : 10.10.10.101 
device mask     (dm) : 255.255.255.0 
server IP      (sip) : 10.10.10.2 
gateway IP       (g) : 10.10.10.2 
user             (u) : vxworks 
ftp password    (pw) : ******* 
device name     (dn) : ETX‑2i 
quick autoboot   (q) : no 
protocol         (p) : ftp 
baud rate        (b) : 9600 
 
Parameter 
Command 
Description 
file name  
fn 
The binary software pack file (*.bin) name to be downloaded via 
FTP/TFTP 
device ip 
ip 
ETX‑2i IP address  
device mask 
dm 
ETX‑2i IP subnet mask  
server IP 
sip 
FTP/TFTP server IP address 
gateway ip 
g 
FTP/TFTP server default gateway IP address 
user 
u 
User name for FTP server 
Note: Displayed only when using FTP protocol. 
ftp password 
pw 
User password for FTP server 
Note: Displayed only when using FTP protocol. 
ETX-2i Devices 
2. Installation and Setup 
Parameter 
Command 
Description 
device name 
dn 
ETX‑2i 
quick autoboot 
q 
Enables or disables the quick autoboot feature 
protocol 
p 
File transfer protocol to use: FTP or TFTP 
baud rate 
b 
Transmission bit rate (in kbps): 9600, 19200, or 115200  
9. Enter c to configure the boot parameters.  
The boot parameters are displayed line by line. For each parameter, you can type a different 
value, or click <Enter> to go to the next parameter. The example below illustrates changing the 
file name to ETX‑2i.bin, and the protocol to TFTP. 
'.' = clear field;  '-' = go to previous field;  ^D = quit 
 
file name       (fn) : vxworks ETX‑2i.bin 
device IP       (ip) : 10.10.10.101  
device mask     (dm) : 255.255.255.0 
server IP      (sip) : 10.10.10.2 
gateway IP       (g) : 10.10.10.2 
user             (u) : vxworks 
ftp password    (pw) (blank = use rsh): ******* 
device name     (dn) : ETX‑2i 
quick autoboot [y/n] : n 
protocol  [tftp/ftp] : ftp tftp 
baud rate [9600/19200/115200]: 9600 
10. See the following sections for instructions on downloading via XMODEM, FTP, or TFTP.  
Installing Software via FTP  
Use the following procedure to download software release 6.8.5 to ETX‑2i via FTP. 
 To download software release via FTP: 
1. Verify that the image file is stored on the PC with the FTP server application. 
2. Enter the Boot screen and set the boot parameters as needed (see table above). For example, 
set the FTP user and password, and set protocol to FTP. 
 
 
ETX-2i Devices 
2. Installation and Setup 
3. At the boot prompt, enter: 
download <index>[, <FileName>] 
If no errors are detected, the downloading process starts, and the file is downloaded via FTP. 
Note 
• 
The <index> parameter corresponds to the software pack number to 
which to copy the image file. 
• 
If you have set the file name in the boot parameters, you do not need to 
specify <FileName>. 
For example, to download the file name configured in the boot parameters to sw-pack-2, enter: 
download 2 
4. See Activating the Software for instructions on activating the downloaded software. 
Installing Software via TFTP 
Use the following procedure to download software release 6.8.5 to ETX‑2i via TFTP. 
 To download software release via TFTP: 
1. Verify that the image file is stored on the PC with the TFTP server application. 
2. Enter the Boot screen and set the boot parameters as needed (see table above). For example, 
set protocol to TFTP.  
3. At the boot prompt, enter: 
download <index>[, <FileName>] 
If no errors are detected, the downloading process starts, and the file is downloaded via TFTP. 
Note 
• 
The <index> parameter corresponds to the software pack number to 
which to copy the image file 
• 
If you have set the file name in the boot parameters, you do not need to 
specify <FileName>. 
For example, to download the file name configured in the boot parameters to sw-pack-2, enter: 
download 2 
4. See Activating the Software for instructions on activating the downloaded software. 
 
 
ETX-2i Devices 
2. Installation and Setup 
Installing Software via XMODEM 
Use the following procedure to download software release 6.8.5 to ETX‑2i via XMODEM. 
 To download software release via XMODEM: 
1. Verify that the image file is stored on the PC with the terminal application. 
2. Enter the Boot screen and set the boot parameters as needed (see table above). 
3. At the boot prompt, enter: 
download <index>, x  
Note 
The <index> parameter corresponds to the software pack number to which to 
copy the image file.  
The process starts, and the following is displayed: 
The terminal will become disabled !!! 
Please send the file in XMODEM 
4. Start the transfer in accordance with the program you are using. For example, if you are using 
the Windows HyperTerminal utility: 
 
Select Transfer in the HyperTerminal menu bar, and then select Send File on the Transfer 
menu. 
The Send File window is displayed: 
 
Select the prescribed ETX‑2i software file name (you may use the Browse function to 
find it). 
 
In the Protocol field, select Xmodem. 
 
When ready, press Send in the Send File window.   
You can now monitor the progress of the downloading in the Send File window. 
When the downloading process has successfully completed, a sequence of messages similar to 
the following is displayed: 
File writing to flash: - 4030KB 
File downloaded successfully to :2 
5. See Activating the Software for instructions on activating the downloaded software. 
 
 
ETX-2i Devices 
2. Installation and Setup 
Bulk Software Installation via ZTP 
Upon first boot, staged ETX‑2i device connects to the service provider’s NOC (Network Operations 
Center) over private or public networks using the RADview Network Management System (NMS). For a 
description of all aspects of ZT provisioning, including security considerations, read RAD’s Zero Touch 
Provisioning document. 
Activating the Software  
To activate a software pack, you need to designate it as active and load it. 
 To activate a software pack: 
1. To set the software as active, enter: 
set-active <index>. 
A confirmation similar to the following is displayed: 
SW set active 2 completed successfully. 
2. To load the active software, type: run. 
A sequence of messages similar to the following is displayed: 
Loading/un-compressing sw-pack-2... 
Starting the APPLICATION off address 0x10000... 
After a few more seconds, the login prompt is displayed. 
Verifying Installation Results 
You can verify that the upgrade was successful by logging on to ETX‑2i via a terminal emulation program, 
and in the Inventory table (show summary-inventory at prompt config>system#), checking the active 
software version in the SW Rev column. 
Restoring the Previous Version 
If the installed software malfunctions and was installed with a restore point (restore-point-config must 
exist on device), you can perform rollback to the previous active software. 
Also, if the installed integrated-module software malfunctions, you can perform rollback to the previous 
active integrated-module software (ETX­2i/ETX­2i-B). 
ETX-2i Devices 
2. Installation and Setup 
 To roll back to the previous active software pack: 
1. At the admin>software# prompt, enter: 
undo-install 
You are prompted to confirm the operation. 
! Falling back to restore point ! Are you sure? [yes/no] _ 
2. Enter yes to confirm. 
The file restore-point-config is renamed to startup-config. ETX‑2i designates the previously 
active software pack as active, then reboots. 
 To roll back to the previous active integrated module software pack: 
1. At the admin>software# prompt, enter: 
undo-install integrated-module 
You are prompted to confirm the operation. 
! This action will revert system to restore point. Are you sure? [yes/no] _ 
2. Enter yes to confirm. 
The file restore-point-config is renamed to startup-config. x86 module designates the 
previously active integrated-module software pack as active, and then reboots. 
 