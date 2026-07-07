# 2 Hardware Installation

*Manual `ETX-1p_6.4_Mn_05-26_GA.pdf`, pages 67–88.*


## 2.1 Pre-installation  *(p.67)*

This chapter provides installation instructions for the ETX-1p systems including:  
• 
General description of the equipment enclosure and its panels 
• 
Mechanical and electrical installation instructions 
After the system is installed, it must be configured in accordance with the specific user's requirements. 
The preliminary system configuration is always performed by means of a supervision terminal 
(procedures for using the terminal are detailed in the Operation and Maintenance chapter). After the 
preliminary configuration, the system can also be managed by means of SNMP-based network 
management stations, e.g., RADview with an integrated  Network Management tool. 
2.1 Pre-installation 
Storage and Transportation 
This product fulfills several environmental conditions, such as ambient temperatures and relative 
humidity levels. These conditions apply to storage, transportation, and stationary operation of the 
equipment. You can find specifications about these environmental conditions in the Technical 
Specifications section. 
 
 
Warning 
Ensure that your site meets the required ambient temperatures and relative 
humidity levels to store, transport, and operate the equipment. Failing to do 
so may damage the equipment. 
 
2. Hardware Installation 
Power supplies stored in warehouse and unoperated for more than 24 months, need to 
undergo a periodic activation for component rejuvenation, once every 24 months.  
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
Staging  
Staging includes any actions required before shipping products to their installation sites, including 
installing the device SW, config files, and enrolling various certificates.  
Staging prior to shipment to the installation site may be required for automatic mass-deployment, also 
known as Zero Touch Provisioning (ZTP).  
Zero Touch (ZT) is a technology for automatic mass-provisioning of network devices. Upon first boot, 
ETX-1p connects to the service provider’s NOC (Network Operations Center) over private or public 
networks, based on preparation steps performed at various locations. It requires the RADview NMS 
(Network Management System). 
For a description of all aspects of ZT provisioning, including security considerations, read RAD’s Zero 
Touch Provisioning document. 
2. Hardware Installation 
The staging content is always defined together with the service provider and is normally done by RAD 
(though it can be in combination with the partner (if exists) and/or the service provider). 
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
Previous training in installation, operation, maintenance, and troubleshooting of ETX-1p 
and software, and awareness of the potential hazards. 
• 
Understanding of all safety guidelines outlined in this guide and the willingness to follow 
them. 
2. Hardware Installation 
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
equipment to install ETX-1p. 
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
safe use of ETX-1p and management software. 
2. Hardware Installation 
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
Power 
Note 
Before connecting this product to a power source, make sure to read the 
Handling Energized Products section at the beginning of this manual. 
 
 
 
Using any adapter other than the external 12V AC/DC power adaptor 
supplied by RAD is strictly forbidden. 
 
Note 
Before connecting this product to a power source, make sure to read the 
Handling Energized Products section at the beginning of this manual. 
 
 
Caution  
ETX-1p does not have a power switch, and therefore will start operating as 
soon as power is applied to one of the power supply inlets. 
The external circuit breaker used to protect the input power line can be used 
as an ON/OFF power switch, or an external ON/OFF switch may be installed. 
2. Hardware Installation 
 
Note 
Refer also to the Connecting AC Mains and Connecting DC Power sections in 
the Front Matter of this manual. 
Environmental Factors 
       
 
The ambient storage temperature range of ETX-1p is -40 to 85°C (-40 to 185°F). Operating temperature 
is 0°C to 50°C (32 to 122°F), at a relative humidity of 5% to 90%, non-condensing.  
ETX-1p has no fans and is cooled mainly by free air convection. Keep 10 cm distance from top and 
bottom between ETX-1p and any other nearby device for proper cooling using natural air flow. 
 
 
Site Safety 
It is recommended to install the unit in locations where children are not likely to be present. 
 
Warning 
ETX-1p must be installed by qualified personnel according to the National 
Electrical Code or Local Electrical Regulation. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. 
Protection from Hazards 
You may have to open a unit for servicing or hot swapping of power supplies. Therefore, it is 
recommended to install the unit in an area that takes into consideration water, moisture, dust, smoke, 
chemicals, noise, pollution, and electromagnetic interference. 
 

## 2.2 Installation Process  *(p.73)*

2. Hardware Installation 
2.2 Installation Process 
Note 
 The sections are listed in the required order of the installations: SIM and 
memory cards first; power last. 
Unpacking and Inspection 
Keep shipping boxes for a minimum period of 24 hours in the installation location to prevent rapid 
thermal shock from rapid temperature change and surface condensation when you unpack the boxes. 
Leave the shelf in its shipping box until the site is ready for installation. If you need to wait to unpack the 
shelf and temporarily store the shipping boxes, follow these guidelines: 
• 
Examine the outside of the shipping boxes for dents and punctures that might indicate possible 
shipping damage. Note and report any damage as necessary. 
• 
Place each shipping box in an area that meets the climatic conditions specified in EN 300019-1-1 
V2.2.1(2014-04). 
• 
Do not expose shipping boxes to: 
 
High levels of dust, smoke, or moisture. 
 
Direct sunlight or heat sources. 
RAD securely packages each product in shipping boxes. Examine the outside of the shipping boxes for 
dents and punctures that might indicate possible shipping damage. Note and report any damage as 
necessary. 
Keep all associated ancillary equipment with its relevant equipment. 
Use an appropriate carrying device such as a hand truck, pushcart, or dolly, to move the shipping boxes 
to the location.  
Store the shipping boxes where you have enough space to safely unpack the shelf. 
Place the shipping boxes off the ground no lower than knee height to reduce the height of the lifting 
required 
Required tools and equipment: 
• 
Utility knife or scissors 
• 
ESD-preventive wrist strap or other personal grounding device 
• 
Suitable grounded surface or a static-dissipative mat 
2. Hardware Installation 
Unpacking procedure:  
Attach a ground strap to your wrist and snap the ground wire to the wrist band. Insert the ground 
plug into a grounded ESD jack. 
1. Inspect each shipping box for evidence of damage during shipment. You must promptly assert any 
claims for damage caused during shipment with the transportation company involved. If any 
damage or other signs of mishandling are evident, inform both the freight carrier and RAD before 
you unpack the equipment. Your freight carrier can provide you with the procedures necessary to 
file a claim for damages. 
2. Move the shipping boxes to a staging area as close to the installation site as possible where you 
have enough space to remove the component from the boxes. 
3. Open each shipping box:  
a. Use a utility knife or scissors to cut open the band-clamp straps from the box. 
b. Lift the cap by using the handles on the right-side and left-side to open the box. 
4. Lift the tray from the top of the shelf and set it aside. 
 
5. Remove the component from each shipping box. 
6. Move the component to a stable surface in the work area, and then place it on a static dissipative 
mat. Wait until the component is secure before you release your grip. 
ELECTROSTATIC CAUTION: Risk of damage due to electrostatic discharge! Keep the component in its ESD 
protective bag until you are ready to inspect it. 
CAUTION: Do not drop the equipment on a hard surface, which can result in damage to internal 
components. If you drop any components, return them to RAD for examination and repair. 
7. Remove the ESD protective bag from the shelf and set it aside. 
8. Open the accessory kits and boxes. Use your hands to open the boxes. Using a knife to open the 
boxes can result in damaged equipment. 
2. Hardware Installation 
9. Carefully look at the product and accessories for external damage, dirt, any deformation in the pin 
holes shape, or impurities. If necessary, use canned, dry, oil-free compressed air to blow away any 
impurities.  
10. If any damage occurred during transportation, immediately report the extent of damage by filing a 
claim with the transportation company. Notify your RAD customer service representative. Have 
this information ready: 
 
Invoice number of shipper 
 
Name of the damaged unit 
 
Serial number and item number of the damaged unit 
 
Description of damage 
 
Effect of damage on the installation 
If you need to return damaged equipment to the factory, see Returned Material Authorization (RMA). 
Order any replacement equipment, if necessary.  
11. Set aside the packaging material, and then verify whether the equipment is operational.  
12. Store all the shipping boxes and packaging material so that you can repack the components if you 
need to return any item for needed repair or for possible transport to another installation site. 
Caution 
Use caution when you handle and transport an empty device without 
modules. To avoid damage to the backplane connectors, make sure that no 
items fall into the shelf or onto the backplane.  
Package Contents 
Note the following: 
Depending on the components that you specify in your order, a complete <product> can consist of 
multiple boxes. All boxes include a summary of contents and the number of shipped boxes. Each 
<product> ships with the appropriate accessories. Individual modules of any type, spare parts, 
replacement parts, or other equipment ship in separate boxes. Check with Ronit 
Examine the outside of the shipping boxes for dents and punctures that might indicate possible shipping 
damage. Note and report any damage as necessary. 
Open the box(es) and verify all items in the packing list are included.  The package includes the basic 
package content, along with relevant antennas (model dependent), and any optional items. 
Take inventory. Find the packing slip on the front side of the cap. Use the purchase order copy or 
equipment list that RAD provides to compare the contents of the box and ensure complete and 
accurate shipment. Make note of missing items, if necessary. 
2. Hardware Installation 
Verify that you have the proper component type by using the product ID label for identification. 
If a standard item is missing or the configuration of the system does not conform to the one you have 
ordered, notify your RAD customer service representative immediately. 
 
The ETX-1p package includes the following items: 
• 
ETX-1p unit  
• 
External 12V AC/DC power adaptor  
• 
Optional: CBL-RJ45/D9/F/6FT – Control port cable with male RJ-45 and female DB-9 connector  
• 
Optional: Two cellular antennas as per ordering option  
• 
Optional: Two WiFi antennas as per the ordering option  
• 
Optional: A GPS antenna as per the ordering option  
• 
Optional: LoRaWAN antenna, 3 dBi, as per the ordering option 
• 
Optional: RM-33-2 – Hardware kit for mounting  ETX-1p device in a 19-inch rack 
Mounting the ETX-1p Unit 
ETX-1p is designed for installation as a desktop unit in horizontal orientation only. It can also be 
mounted in a 19" rack or on a wall.  
 
Warning 
ETX-1p units are intended for use in horizontal orientation only. 
In case of vertical mounting orientation, install the unit on top of concrete or 
other non-combustible surface, such as an external baffle or tray, due to 
safety considerations.  
For rack mounting instructions, refer to the associated installation kit manual. 
If you are using ETX-1p as a desktop unit, place and secure the unit on a stable, non-movable surface.  
See the clearance and temperature requirements in Site Requirements and Prerequisites. 
2. Hardware Installation 
Installation Safety Warnings 
Using any adapter other than the external 12V AC/DC power adaptor 
supplied by RAD is strictly forbidden. 
 
 
Warning 
This is a radio device. To avoid radiation-related health problems per EN 
62311:2008, the minimum distance from the human body to an operating 
product should be at least 25 cm.  
 
 
Caution 
This equipment contains Electrostatic Discharge (ESD) sensitive components. 
Use ESD protection before servicing or installing components of this system. 
 
Caution 
Changes or modifications made to this device that are not expressly 
approved by the party responsible for compliance could void the user’s 
authority to operate the equipment. 
 
Caution 
Remove the power cord from a power-supply unit before installing it or 
remove it from the device.  Otherwise, as a result, the power supply or the 
device could be damaged.  (The device can be running while a power supply 
is being installed or removed, but the power supply itself should not be 
connected to a power source.) 
 
Caution 
The unit is designated to operate in environments of up to 50 degrees 
ambient temperature. 
 
 
Caution 
Installing or removing a SIM card during modem operation can damage the 
modem. Make sure either the modem is disabled (cellular disable) or ETX-1p 
is turned off, before manipulating the SIM card. 
2. Hardware Installation 
 
ETX-1p includes Class 1 lasers. For your safety: 
• 
Do not look directly into the optical connectors while the unit is 
operating. The laser beams are invisible. 
• 
Do not attempt to adjust the laser drive current. 
The use of optical instruments with this product will increase eye hazard. 
Laser power up to 1 mW at 1300 nm and 1550 nm could be collected by an 
optical instrument. 
Use of controls or adjustment or performing procedures other than those 
specified herein may result in hazardous radiation exposure. 
 
Required Tools and Equipment  
Prior to installing the unit, prepare the following, as required: 
• 
Phillips screwdriver to mount the ETX-1p unit in a rack. 
• 
External 12V AC/DC power adaptor  
• 
CBL-RJ45/D9/F/6FT control port cable 
• 
Any other cables required to connect the unit to remote equipment as per the specific 
application. 
 
Installing Antennas  
Installing LTE Antennas  
ETX‑1p with LTE option comes with two antennas.  It is re required to install both antennas to achieve an 
LTE connection. 
The MAIN and AUX connectors are located on the unit rear panel (see the figures below for single-
modem and dual-modem options). 
 To install the LTE antennas: 
1. Make sure both antennas are articulated horizontally on their mounts. 
2. Hardware Installation 
2. Screw the coaxial end of one antenna onto the MAIN connector. 
3. Screw the coaxial end of the other antenna onto the AUX connector. 
4. Articulate the antennas vertically (at a 90 degree angle with the unit). 
Note 
Position the device for optimal reception. Place device outside any metal or 
thick walled (concrete, brick, etc.) enclosure, preferably either close to a 
window or on a higher floor (e.g. not in a basement). When four LTE LEDs are 
ON, this indicates that the antennas are in a location with good reception. 
 
 
 
Antenna Connectors (MAIN, AUX)  
 
Note 
RAD has tested and approved external LTE antennas with 2m and 5m cables 
only.  
If outdoor installation requires longer cables, make sure that the combination 
of the antenna, cable and location provides sufficient gain and signal strength 
for good operation. In these cases, consult with experts in antenna, cable, 
location specifications to choose a right solution.  
 
Note 
In the dual-LTE modem platform, GPS antenna is connected to the modem in 
slot 1 (specified as Lx1 in the ordering string ETX-1p/@/#/$/Lx1/Lx2/&) and 
coordinates are sent from modem slot one only. 
2. Hardware Installation 
Installing Wifi Antennas  
Note the following: 
• 
ETX‑1p with Wifi option comes with two antennas.  
• 
You are required to install both antennas to achieve a Wifi connection. 
• 
The MAIN and AUX connectors are located on the unit rear panel (see the figure below). 
 To install the Wifi antennas: 
1. Make sure both antennas are articulated horizontally on their mounts.  
2. Screw the coaxial end of one antenna onto the MAIN connector. 
3. Screw the coaxial end of the other antenna onto the AUX connector. 
4. Articulate the antennas vertically (at a 90 degree angle with the unit). 
Note 
Position the device for optimal reception. Place device outside any metal or 
thick walled (concrete, brick, etc.) enclosure, preferably either close to a 
window or on a higher floor (e.g. not in a basement). When four LTE LEDs are 
ON, this indicates that the antennas are in a location with good reception 
 
 
Antenna Connectors (MAIN, AUX)  
Installing the LoRaWAN Antenna  
The figure below shows an example of rear panel for Dual LTE, GPS and LoRa ordering option. 
2. Hardware Installation 
 
This antenna can be connected only to the LoRa connector, and it supports both Rx and Tx. 
Installing the GNSS Antenna  
Use of ETX­1p with the GNSS ordering option requires installation of a GNSS antenna on the roof of the 
building.  
Positioning the GNSS Antenna 
Damage to an antenna or GNSS receiver is more often due to lightning strikes on nearby objects, rather 
than direct strikes on the antenna. These direct or indirect lightning strikes are likely to induce damaging 
voltages in the antenna system. Therefore, it is advisable to place the GNSS antenna below and at least 
15 meters away from towers, lightning rods, or structures that attract lightning.  
Mounting the Lightning Arrestor 
It is recommended to install a Lightning Arrestor to further protect your GNSS circuit from lightning 
strikes. A Lightning Arrestor is able to handle lightning currents by reducing the pulse energy of the input 
surge.  
 
 
GNSS In-Line Lightning Arrestor 
 To mount the Lightning Arrestor: 
1. Mount the Lightning Arrestor on good earth ground (low impedance), between the GNSS antenna 
and the point where the cable enters the building. 
2. Hardware Installation 
2. Connect the GNSS antenna on the roof to the surge side connector at the top of the Lightning 
Arrestor using the shortest possible interconnection cable. 
3. Connect the protected side connector at the bottom of the Lightning Arrestor to the GPS receiver 
(the device) using a coax cable.  
4. If the coax cable length connecting the Lightning Arrestor to the GPS receiver is no longer than 20 
m, no further safety measures are required. 
For longer cable distances, a further fine protector may be needed to protect the receiver against 
induced voltages caused by magnetic coupling. If this is the case, contact RAD Technical Support 
for more information.  
  
Mounting GNSS In-Line Lightning Arrestor 
Installing a SIM Card  
ETX-1p provides cellular interface that requires an active SIM card. The SIM cards compartment on the 
rear panel can house up to two SIM cards ensuring redundancy and backup of network connectivity. 
Note 
SIM changing on-the-fly is not allowed. To change the SIM cards, you have to 
power the device off and turn it on again once the changing is completed.  
 
2. Hardware Installation 
 
 To install a SIM card into the unit: 
1. Make sure the device power is turned off.  
2. Release and remove the screws fastening the SIM compartment cover. 
3. Open the cover and insert the SIM card all the way into the slot until it clicks into place. You can 
use any suitable tool, for example a small screwdriver or a pen. Make sure the card direction 
matches the corresponding icon on the front panel.  
4. Close the cover and fasten the screws with the screwdriver. 
 To remove a SIM card from the unit: 
1. Make sure the device power is turned off. 
2. Release and remove the screws fastening the SIM compartment cover. Remove the cover 
3. Insert the SIM card and gently press on the card until it clicks into place. Use any suitable tool such 
as a pen or a small screwdriver.  
4. Close the cover and secure the screws with the screwdriver.. 
Installing an SFP 
You can install a recognized SFP module with an RJ-45 copper or LC fiber optic connector in the Ethernet 
SFP port. 
 
 
Third-party SFP optical transceivers must be agency-approved, complying 
with the local laser safety regulations for Class I laser equipment. The laser 
product must be safety approved to IEC 60825 and CDRH registered. 
 
2. Hardware Installation 
Caution 
When calculating optical link budget, always take into account adverse 
effects of temperature changes, optical power degradation, and so on. To 
compensate for signal loss, leave a 3 dB margin. For example, instead of 
maximum receiver sensitivity of -28 dBm, consider the sensitivity measured 
at the Rx side to be -25 dBm. Information about Rx sensitivity of fiber optic 
interfaces is available in the Pluggable Transceivers data sheet. 
 To install the SFP: 
1. Lock the wire latch of the SFP module by lifting it up until it clicks into place, as illustrated on the 
picture below. 
 
Note 
Some SFP models have a plastic door instead of a wire latch. 
 
 
Locking the SFP Wire Latch 
2. Carefully remove the dust covers from the SFP slot. 
3. Insert the rear end of the SFP into the socket, and push slowly backwards until the SFP clicks into 
place. If you feel resistance before the connectors are fully mated, retract the SFP using the wire 
latch as a pulling handle, and then repeat the procedure. 
 
Caution 
Insert the SFP gently. Using force can damage the connecting pins. 
 
4. Remove the protective rubber caps from the SFP modules. 
 To remove the SFP module: 
1. Disconnect the fiber optic cables from the SFP module. 
2. Unlock the wire latch by lowering it downwards (as opposed to locking). 
3. Hold the wire latch and pull the SFP module out of the Ethernet port.  
2. Hardware Installation 
 
Caution 
Do not remove the SFP while the fiber optic cables are still connected. This 
may result in physical damage (such as a chipped SFP module clip or socket), 
or cause malfunction (e.g., the network port redundancy switching may be 
interrupted). 
Connecting to Power  
ETX-1p units are supplied with an external 12V AC/DC power adaptor. 
Using any adapter other than the external 12V AC/DC power adaptor 
supplied by RAD is strictly forbidden. 
 To connect to power: 
1. Connect the external power supply connector to the power connector on ETX-1p.  
2. Turn the connector clockwise to lock it tightly in the socket. 
3. Connect the power supply to the mains outlet. 
4. The unit turns on automatically once connected to the mains. 
 
 
 To disconnect from power: 
1. Disconnect the power supply from the mains outlet. 
2. Turn the connector counterclockwise to unlock. 
3. Pull the external power supply connector out of the socket. 
2. Hardware Installation 
You can connect the ETX-1p RS-232 interface (designated CONTROL) to a laptop equipped with an ASCII 
terminal emulation application, such as PuTTY, via an 8-pin RJ-45 connector. Refer to the Connection 
Data appendix for the connector pinout. 
Caution 
Terminal cables must have a frame ground connection. Use ungrounded 
cables when connecting a supervisory terminal to a DC-powered unit with 
floating ground. Using improper terminal cable may result in damage to the 
supervisory terminal port.  
 To connect to an ASCII terminal: 
1. Connect the RJ-45 connector of CBL-RJ45/D9/F/6FT cable, available from RAD, to the unit’s 
CONTROL connector (RS-232 interface). 
2. Connect the other end of the CBL-RJ45/D9/F/6FT cable to a computer equipped with an ASCII 
terminal emulation application. 
 
Note 
After completing the configuration of the terminal, disconnect the terminal 
and leave the CONTROL port open.  
 
CONTROL Connector 
Connecting to Ethernet Equipment 
ETX-1p is connected to Ethernet equipment via the following interfaces: 
• 
WAN side: one fiber GbE optic SFP transceiver + one electrical GbE port with the standard RJ-45 
connectors  
• 
LAN side: 4 UTP (RJ-45) GbE ports 
 To connect to Ethernet equipment with the fiber optic interface: 
• 
Connect ETX-1p to the Ethernet equipment at customer premises using the standard fiber optic 
cable terminated with LC connector. 
2. Hardware Installation 
 Note 
Use shielded cables when connecting to Ethernet ports.  
 
  
 To connect to Ethernet equipment with copper interface: 
• 
Connect ETX-1p to the Ethernet equipment at customer premises using the standard CAT5 cable 
or better terminated with RJ-45 connector.   
Note 
In order to comply with electromagnetic compatibility requirements, it is 
recommended to use Category 6E shielded twisted pairs (STP) cables.  
 
Inspection after Installation 
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
2. Hardware Installation 
No. 
Item 
7 
Labels on both ends of the data cable should be correct, distinct, and neat. 
8 
Power cables and ground cables are connected correctly and reliably. 
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
Before leaving the installation site, it is highly recommended that you test 
network connectivity between the device and the remote network 
management station (for example, by sending a ping). 
 
 