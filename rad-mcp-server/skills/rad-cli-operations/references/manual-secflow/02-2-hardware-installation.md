# 2 Hardware Installation

*Manual `SecFlow-1p_6.4_Mn_05-26_GA.pdf`, pages 72–100.*


## 2.1 Pre-installation  *(p.72)*

This chapter provides installation instructions for the SecFlow-1p systems including:  
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
SecFlow-1p connects to the service provider’s NOC (Network Operations Center) over private or public 
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
Previous training in installation, operation, maintenance, and troubleshooting of 
SecFlow-1p and software, and awareness of the potential hazards. 
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
equipment to install SecFlow-1p. 
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
safe use of SecFlow-1p and management software. 
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
 
Caution 
 SecFlow-1p does not have a power switch, and therefore will start 
operating as soon as power is applied to one of the power supply inlets. 
The external circuit breaker used to protect the input power line can be used 
as an ON/OFF power switch, or an external ON/OFF switch may be installed. 
Available power input versions and their respective maximum current are shown in the table below. 
Power Inputs and Max Current  
DC Power Input 
Max Input Current [A] 
12V 
1A 
24V 
0.5 
 
Note 
Refer also to the Connecting AC Mains and Connecting DC Power sections in 
the Front Matter of this manual. 
2. Hardware Installation 
Environmental Factors 
The ambient storage temperature range of SecFlow-1p is -40 to 85°C (-40 to 185°F). Operating 
temperature is -20 to 65°C (-4 to 149°F); humidity up to 90%.  
SecFlow-1p has no fans and is cooled mainly by free air convection. Keep 10 cm distance from top and 
bottom between SecFlow-1p and any other nearby device for proper cooling using natural air flow. 
       
 
Site Security 
 
Caution 
 SecFlow-1p is intended for installation in a Restricted Access Location. 
 
Site Safety 
It is recommended to install the unit in locations where children are not likely to be present. 
 
Warning 
SecFlow-1p must be installed by qualified personnel according to the 
National Electrical Code or Local Electrical Regulation. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. 
Protection from Hazards 
You may have to open a unit for servicing or hot swapping of power supplies. Therefore, it is 
recommended to install the unit in an area that takes into consideration water, moisture, dust, smoke, 
chemicals, noise, pollution, and electromagnetic interference. 
 
 
Warning 
This is a radio device. To avoid radiation-related health problems per EN 
62311:2008, the minimum distance from the human body to an operating 
product should be at least 25 cm.  
 
 
2. Hardware Installation 
Installing SecFlow-1p in Hazardous Locations 
The SecFlow-1p options suitable for installing in hazardous locations are marked, in their Marketing item 
option, with the extension:  /GO 
 
Warning 
Before installing a /GO device in a hazardous location, make sure that it has  
the following label: 
 
 
 
 
Warning 
 
Install the devices only in type rated enclosures suitable for the  
environment, where the internal components are accessible only by using  
a tool. 
 
 
Warning 
 
N'installez les appareils que dans des boitiers dont les specificités sont  
adaptés à l'environnement et dont les composants internes ne sont 
accessibles qu'à l'aide d'un outil. 
 
 
 
Warning 
Before connecting or disconnecting any cable or part, turn off the unit  
power. 
 

## 2.2 Installation Process  *(p.79)*

2. Hardware Installation 
 
Warning 
Avant de connecter ou de déconnecter un câble ou un élément,  
mettez l'appareil hors tension. 
 
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
2. Hardware Installation 
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
b. Lift the cap by using the handles on the right-side and left-side to open the box. 
5. Lift the tray from the top of the shelf and set it aside. 
 
6. Remove the component from each shipping box. 
2. Hardware Installation 
7. Move the component to a stable surface in the work area, and then place it on a static 
dissipative mat. Wait until the component is secure before you release your grip. 
ELECTROSTATIC CAUTION: Risk of damage due to electrostatic discharge! Keep the component in its ESD 
protective bag until you are ready to inspect it. 
CAUTION: Do not drop the equipment on a hard surface, which can result in damage to internal 
components. If you drop any components, return them to RAD for examination and repair. 
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
12. Set aside the packaging material, and then verify whether the equipment is operational.  
13. Store all the shipping boxes and packaging material so that you can repack the components if 
you need to return any item for needed repair or for possible transport to another installation 
site. 
Caution 
Use caution when you handle and transport an empty device without 
modules. To avoid damage to the backplane connectors, make sure that no 
items fall into the shelf or onto the backplane.  
Package Contents 
Note the following: 
2. Hardware Installation 
Depending on the components that you specify in your order, a complete <product> can consist of 
multiple boxes. All boxes include a summary of contents and the number of shipped boxes. Each 
<product> ships with the appropriate accessories. Individual modules of any type, spare parts, 
replacement parts, or other equipment ship in separate boxes. Check with Ronit 
Examine the outside of the shipping boxes for dents and punctures that might indicate possible shipping 
damage. Note and report any damage as necessary. 
Open the box(es) and verify all items in the packing list are included.  The package includes the basic 
package content, along with relevant antennas (model dependent), and any optional items. 
14. Take inventory. Find the packing slip on the front side of the cap. Use the purchase order copy 
or equipment list that RAD provides to compare the contents of the box and ensure complete 
and accurate shipment. Make note of missing items, if necessary. 
15. Verify that you have the proper component type by using the product ID label for identification. 
If a standard item is missing or the configuration of the system does not conform to the one you have 
ordered, notify your RAD customer service representative immediately. 
 
Basic Package 
 
 
 
Unit 
Power Adapter 
Alarm Adapter 
 
 
 
 
LTE* 
Antennas 
GPS* 
Antenna 
WiFi* 
Antennas 
LoRa* 
Antenna 
Accessories 
 
Console cable 
2. Hardware Installation 
 
 
SF-AC-12VDC-20W-EX  
(Without DIN rail bracket) 
SF-AC-12VDC-20W 
(With DIN rail bracket) 
*Provided antennas are model dependent. 
 
Installation Safety Warnings 
Danger of electric shock! Avoid any contact with the marked surface while 
the product is energized or connected to outdoor telecommunication lines. 
 
Protective earth: the marked lug or terminal should be connected to the 
building protective earth bus. 
 
 
LINE VOLTAGE 
Before connecting the product to the power line, make sure the voltage of 
the power source matches the requirements of the product, as marked on 
the label located near the power connectors. 
 
Caution 
This equipment contains Electrostatic Discharge (ESD) sensitive components. 
Use ESD protection before servicing or installing components of this system. 
 
Caution 
Changes or modifications made to this device that are not expressly 
approved by the party responsible for compliance could void the user’s 
authority to operate the equipment. 
 
2. Hardware Installation 
Caution 
Remove the power cord from a power-supply unit before installing it or 
remove it from the device.  Otherwise, as a result, the power supply or the 
device could be damaged.  (The device can be running while a power supply 
is being installed or removed, but the power supply itself should not be 
connected to a power source.) 
 
Caution 
The unit is designated to operate in environments of up to 75 degrees 
ambient temperature. 
 
Caution 
Use Safety approved AC/DC adapter, according to IEC/EN 60950-1 or IEC/EN 
62368-1 with rated voltage of 12/24 VDC, certified as LPS. 
 
 
 
 
SecFlow-1p includes Class 1 lasers. For your safety: 
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
 
 
For your protection and to prevent possible damage to equipment when a 
fault condition, e.g., a lightning stroke or contact with high voltage power 
lines, occurs on the lines connected to the equipment, the  chassis must be 
properly grounded (earthed) at any time. Any interruption of the protective 
(grounding) connection inside or outside the equipment, or the 
disconnection of the protective ground terminal can make this equipment 
dangerous. Intentional interruption is prohibited. 
Caution 
Installing or removing a SIM card during modem operation can damage the 
modem. Make sure either the modem is disabled (cellular disable) or 
SecFlow-1p is turned off, before manipulating the SIM card. 
2. Hardware Installation 
Required Tools and Equipment  
 
No special tools are required for  SecFlow-1p installation.  
The cables needed to connect to SecFlow-1p depend on your specific application. You can prepare the 
appropriate cables yourself in accordance with the information given in the Connection Data appendix, 
or you can order cables from RAD. 
Installing a SIM Card  
SecFlow-1p provides cellular interface that requires an active SIM card. The SIM cards compartment on 
the bottom panel can house up to two SIM cards ensuring redundancy and backup of network 
connectivity. 
Note 
SIM changing on-the-fly is not allowed. To change the SIM cards, you have to 
power the device off and turn it on again once the process is completed.  
 To install SIM card(s) into SecFlow-1p: 
1. Make sure the device power is turned off.  
2. Open the screw fastening the cover of the SIM 
compartment, and remove the cover.  
3. Insert the SIM card into the SIM1 bottom slot. 
Make sure the card direction match the 
corresponding icon on the front panel. If 
ordered, insert the second SIM card in the SIM2 
top slot.  
4. Close the cover and fasten the screw with the 
screwdriver. 
5. 
 
6. 
SIM Slots 
 To remove a SIM card from SecFlow-1p: 
1. Make sure power to the device is off.  
2. Unscrew the screw fastening the cover of the SIM compartment, and remove the cover. 
3. Gently press on the SIM card until it pops out. Use any suitable tool such as a small screwdriver or 
a pen. 
2. Hardware Installation 
4. Close the cover and secure he screw with a screwdriver. 
Installing a Memory Card (Optional) 
 To install a memory card to SecFlow-1p: 
Verify power to the unit is OFF. Insert the memory card in the unit side 
panel, SD slot (adjacent to the SIM slots). 
 
Memory Card 
 To remove a memory card from SecFlow-1p: 
Press on the memory card against the horizontal slot. Use any suitable tool, such as a small screwdriver 
or a pen. 
Grounding  
Use the ground lug (located on the side panel), to earth the 
unit chassis to a protection earth.   
 
Ground Lug 
 To install the grounding wire:  
1. Prepare a grounding wire terminated by a crimped lug with hole diameter 11-14 AWG as shown 
in the below figure.  
2. Use a suitable crimping tool to fasten the lug securely to the wire.  
3. Adhere to your company’s policy as to the wire gauge and the number of crimps on the lug. 
 
SecFlow-1p Grounding Lug 
11-14 AWG 
2. Hardware Installation 
4. Apply some antioxidant onto the metal surface. 
5. Mount the lug on the grounding posts, replace the spring-washers and fasten the bolts. Avoid 
using excessive torque. 
 
Caution 
Do not remove the earth connection unless all power supply connections are 
disconnected. 
 
Caution 
Protective earth: the marked lug or terminal should be connected to the 
building protective earth bus. 
Installing Antennas  
The number and type of antennas supplied with SecFlow-1p depends on the ordering option. For the 
technical specifications of the supplied antennas, refer to Antennas.  
This section describes the installation of the LTE, WiFi, and LoRaWAN Antennas. The GNSS antenna 
installation is described in a dedicated section. 
LTE/WiFi/LoRaWAN Antennas 
Note the following: 
• 
LTE – For optimal signal performance, it is recommended to connect both antennas of the same 
type provided with the device. If only a single antenna is used, connect to the MAIN front panel 
connector. In this case, the MAIN antenna supports both Rx and Tx.  When two antennas are 
used, one handles Tx functionality and the other Rx.  
• 
RAD has tested and approved only external LTE antennas with 2m and 5m cables. If outdoor 
installation requires longer cables, make sure that the combination of the antenna, cable and 
location provides sufficient gain and signal strength for good operation. In these cases, consult 
with experts in antenna, cable, and location specifications to choose the right solution. 
• 
In the dual-LTE modem platform, GPS antenna is connected to the modem in slot 1 (specified as 
Lx1 in the ordering string SF-1P/@/#/$/Lx1/Lx2/&/H1) and coordinates are sent from modem 
slot one only. 
• 
Connectors:  
o LTE and GPS antenna connectors – SMA female  
o WiFi antenna connectors –  RP-SMA  
2. Hardware Installation 
• 
LoRaWAN  antenna is connected to the LORA connector. It supports both Rx and Tx. 
 
Caution 
Make sure you use the correct connector for each antenna type. 
 
 To install all provided antennas: 
6. Connect LTE antennas to the front 
panel Main and Aux connectors.  
 
 
LTE Antennas 
7. Connect any additional antennas to the 
relevant panel connectors.  
For example: LTE, LoRa, GPS, WiFi/WH. 
 
Additional Antennas  
2. Hardware Installation 
GNSS Antenna  
Using SecFlow­1p with the GNSS ordering option requires installation of a GNSS antenna on the roof of 
the building.  
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
1. Mount the Lightning Arrestor on a good earth ground (low impedance), between the GNSS 
antenna and the point where the cable enters the building. 
2. Connect the GNSS antenna on the roof to the surge side connector at the top of the Lightning 
Arrestor using the shortest possible interconnection cable. 
3. Connect the protected side connector at the bottom of the Lightning Arrestor to the GPS receiver 
(the device) using a coax cable.  
4. If the coax cable length connecting the Lightning Arrestor to the GPS receiver is less than 20 m, no 
further safety measures are required. 
For cable distances longer than 20 m, a further fine protector may be needed to protect the 
receiver against induced voltages caused by magnetic coupling. If this is the case, contact RAD 
Technical Support for more information.  
2. Hardware Installation 
  
Mounting GNSS In-Line Lightning Arrestor 
Installing an SFP 
You can install a recognized SFP module with an RJ-45 copper or LC fiber optic connector in the Ethernet 
SFP port. 
 
 
Third-party SFP optical transceivers must be agency-approved, complying 
with the local laser safety regulations for Class I laser equipment. The laser 
product must be safety approved to IEC 60825 and CDRH registered. 
 
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
 
2. Hardware Installation 
 
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
 
Caution 
Do not remove the SFP while the fiber optic cables are still connected. This 
may result in physical damage (such as a chipped SFP module clip or socket), 
or cause malfunction (e.g., the network port redundancy switching may be 
interrupted). 
Connecting to a Dry Contacts Terminal  
SecFlow-1p performs discrete IO tunneling via a dry-contact terminal block. When the administrative 
status of the dry contacts is enabled, on the state change (SET/CLEAR) of any defined input or output 
alarm, the following reports are sent: 
• 
Syslog event 
2. Hardware Installation 
• 
Device log event 
• 
SNMP trap 
 
Supported input alarm: typical – 48 VDC (9 VDC min to 60 VDC max) 
 
 
 
Alarm Adapter 
 
Assembly Connector 
3DI x 1DO Option 
Dry Contacts Pinout (3in x 1out) – Ordering Option 
DC CON Pin 
6 
5 
4 
3 
2 
1 
Signal Name 
DIN2 
COM-DIN 
DIN1 
COM-DOUT 
DOUT2 
DIN3 
 
 
1
3
2
4
5
6
N/O
 
Note 
A circuit intended for connection to the Dry Contact interface should be 
limited to 60 VDC maximum, 1A maximum, 37.5 VA maximum, under normal 
and single fault condition. 
2. Hardware Installation 
3DI x 1DO Option 
Dry Contacts Pinout (3in x 1out) – Ordering Option 
DC CON Pin 
6 
5 
4 
3 
2 
1 
Signal Name 
DIN2 
COM-DIN 
DIN1 
COM-DOUT 
DOUT2 
DIN3 
 
 
1
3
2
4
5
6
N/O
 
Alarm Connections 
 To connect the discrete channel to digital input/output: 
1. Strip the insulation of your power supply wires according to the dimensions shown below. 
 
Terminal Block Wire Stripping 
2. Place each wire lead into the appropriate TB plug terminal according to the terminal block 
scheme. 
3. Tighten the terminal screws to close them. 
4. Isolate the exposed terminal screws/wire leads using a plastic sleeve or insulating tape to avoid 
a short circuit. 
2. Hardware Installation 
Connecting to Power  
SecFlow-1p has the DC power input designated according to the device ordering option. 
 
 
Before connecting any cables and before switching on this instrument, the 
protective ground terminal of this instrument must be connected to the 
protective ground conductor. Any interruption of the protective (grounding) 
conductor (inside or outside the instrument) or disconnecting the protective 
ground terminal can make this instrument dangerous. Intentional 
interruption is prohibited. 
Connecting to DC Power  
When using the DC power, the power supply must be provided by the customer. RAD provides a 3-prong 
terminal block power plug for DC power connection. 
 
Caution 
When working with DC, WDC and 12V devices, an appropriate disconnect 
device such as 16A external circuit break shall be provided as part of the 
building installation. 
 
 
Caution 
SecFlow-1p should be powered from external, separately approved and 
suitably rated power supply, providing SELV output. The external Power 
Supply should have at least the following approvals (all of them): 
• 
In Europe:  IEC/EN 62368-1, EN 55032, EN 55032.   
• 
 In North America: UL 62368-1, FCC CFR 47 Part 15 Subpart B.  
When using an external Power Supply not provided by RAD, the 
responsibility for the proper functionality of the whole system (External 
Power Supply and SecFlow-1p is on the entity that made the installation.  
To wire the voltage, use the supplied plug connector (see figures below), according to the pinout shown 
on the DC power terminal located on the device bottom panel. 
2. Hardware Installation 
 
 
Plug Connector Wiring 
DC Power Terminal 
 To connect the device to a DC power source:  
1. Strip 7 mm (1/4 inch) of insulation from the leads (copper wire within the range of 10 to 18 
AWG).  
2. Release two terminal screws on the plug. 
3. Push the lead into the plug terminal block up to its insulating sleeve.  
4. When the lead is in position, fasten the screw to secure the lead. 
5. Verify that the lead is securely held. 
6. Insert the plug into the socket on the device. 
7. Secure the plug by tightening the two screws. 
8. Connect the leads to an external DC power source (color code the wiring according to local 
standards to ensure that the input power and ground lines are easily distinguished). 
9. Turn on the power to the feed lines at the supply circuit-breaker. 
10. Verify that the power supply PWR LED is green. 
Connecting to AC Power  
The unit operates on DC power.  To connect to an AC power source, use one of the converters (ordered 
separately).  Both converters are shown below.  
2. Hardware Installation 
                
      
                  
SF-AC-12VDC-20W-EX – no DIN railing (desktop) 
SF-AC-12VDC-20W – with DIN railing 
2. Hardware Installation 
 To connect the device to an AC power source:  
1. Wire the power plug as shown below (+v in right socket, -v to middle socket).  
2. Insert the plug into the SecFlow-1p power terminal and secure using the two side screws.  
3. Connect the PS cable to the AC power source.  Verify that the SecFlow-1p PWR LED is green. 
 
 
 
Power Plug 
Terminal Example 
Mounting SecFlow-1p  
SecFlow-1p is a fixed unit, designed for mounting on an industry-standard DIN rail, – either on a wall or 
in a rack. The DIN-rail mount is the default for the SecFlow-1p.  The unit is supplied with a bracket for 
DIN-rail mounting.  
 
Warning 
When SecFlow-1p is intended to be installed in compliance with IEC 61850-
3/IEEE-1613 standards, it is mandatory to mount it in a rack. Customers may 
use RAD-provided racks (such as ROC-19) or use their own, on condition that 
it complies to common related standards.  
Two rack options are available (ordered separately): 
Mounting Option 
Mounting Kit 
Single device in 19-inch/23-inch DIN rail  
RM-DIN-SINGLE 
Single/multiple devices in 19-inch DIN rail 
RM-DIN-19 
2. Hardware Installation 
 To mount SecFlow-1p: 
Place the device with the DIN rail guide on the upper edge of the DIN rail, and snap it in with a 
downward motion. 
 
Notes 
When handling SecFlow-1p in a rack, the person involved should be a certified 
technician, grounded with the appropriate equipment.  
Be sure to install the unit in a vertical position. 
If installing several units in a rack, maintain at least 5mm between units and 
at least 1U below and above the units. 
 
 
 
 
Mounted SecFlow-1p Rear View  
Mounted SecFlow-1p Front View  
   To Unmount the unit: 
Pull the latch downwards with the aid of a screwdriver to loosen the lower clamp, and slide the unit out 
and upwards. 
Connecting to a Management Console 
You can connect one of the SecFlow-1p Ethernet ports to a laptop equipped with a management 
application, such as PuTTY, via an 8-pin RJ-45 connector. This port is the Ethernet port with the highest 
number, according to the device ordered:  
2. Hardware Installation 
• 
6 for 4U2S configurations 
• 
4 for 2U configurations. 
Refer to the Connection Data appendix for the connector pinout. 
Caution 
Console cables must have a frame ground connection. Use ungrounded 
cables when connecting a supervisory terminal to a DC-powered unit with 
floating ground. Using improper console cable may result in damage to the 
supervisory terminal port.  
 To connect to a management console: 
1. Connect the RJ-45 connector of CBL-ETH/STP/STR/1M cable, available from RAD, to the unit’s 
Ethernet port 4. 
2. Connect the other end of the CBL-ETH/STP/STR/1M cable to a computer equipped with an ASCII 
terminal emulation application.  
 
Note 
After completing the configuration of the management console, disconnect 
the cable and leave the Ethernet port open.  
Connecting to Ethernet Equipment 
SecFlow-1p is connected to Ethernet equipment via the fiber optic SFP transceiver with LC connector or 
the electrical port with the standard RJ-45 connectors. 
 To connect to Ethernet equipment with the fiber optic interface: 
• 
Connect SecFlow-1p to the Ethernet equipment at customer premises using the standard fiber 
optic cable terminated with LC connector. 
 To connect to Ethernet equipment with copper interface: 
• 
Connect SecFlow-1p to the Ethernet equipment at customer premises using the standard CAT5 
cable or better terminated with RJ-45 connector. 
Connecting to Serial Equipment  
SecFlow-1p serial ports are terminated in RJ-45 connectors. The user serial equipment standard ports 
have DB-9 connectors. Refer to the Connection Data appendix for the RJ-45 connector pinout.  
2. Hardware Installation 
 To connect to serial equipment: 
• 
Connect the RJ-45 serial port to serial equipment at customer premises using 
CBL-RJ45/D9/F/6FT cable terminated with the RJ-45 connector. 
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
 
 