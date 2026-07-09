# ETX-2i Devices User Manual (Version 6.8.5)

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1–32.*


## (chapter introduction)  *(p.1)*

Carrier Ethernet Demarcation 
Version 6.8.5 
 
 
 
User Manual 
© 1988–2026 RAD Data Communications Ltd. 
This manual contains information that is proprietary to RAD Data Communications Ltd. ("RAD"). No part 
of this publication may be reproduced in any form whatsoever without prior written approval by RAD 
Data Communications. 
Right, title and interest, all information, copyrights, patents, know-how, trade secrets, and other 
intellectual property or other proprietary rights relating to this manual and to the ETX-2i Devices and 
any software components contained therein are proprietary products of RAD protected under 
international copyright law and shall be and remain solely with RAD. 
ETX-2i Devices is a registered trademark of RAD. The ETX-2i Devices product name is owned by RAD. No 
right, license, or interest to such trademark is granted hereunder, and you agree that no such right, 
license, or interest shall be asserted by you with respect to such trademark. This product is protected by 
patents; see ipr.rad.com. The RAD name, logo, logotype, and the product names Airmux, IPmux, MiNID, 
MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data Communications Ltd. All other 
trademarks are the property of their respective holders. 
You shall not copy, reverse compile, or reverse assemble all or any portion of the Manual or the ETX-2i 
Devices. You are prohibited from, and shall not, directly or indirectly, develop, market, distribute, 
license, or sell any product that supports substantially similar functionality as the ETX-2i Devices, based 
on or derived in any way from the ETX-2i Devices. Your undertaking in this paragraph shall survive the 
termination of this Agreement. 
This Agreement is effective upon your opening of the ETX-2i Devices package and shall continue until 
terminated. RAD may terminate this Agreement upon the breach by you of any term hereof. Upon such 
termination by RAD, you agree to return to RAD the ETX-2i Devices and all copies and portions thereof. 
 
 
 
 
 
For further information, contact RAD at the address below, or contact your local business partner. 
International Headquarters 
24 Raoul Wallenberg St., Tel Aviv 6971920, Israel 
Tel/Fax 972-52-4748272 | Fax 972-3-6498250 
Email market@rad.com 
North American Headquarters 
900 Corporate Drive, Mahwah, NJ 07430, USA 
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777 
Email market@radusa.com 
www.rad.com | radcare-online.rad.com 
Publication No. 547-200-06/26 
 

## Limited Warranty  *(p.3)*

Limited Warranty 
RAD warrants to DISTRIBUTOR that the hardware in the ETX-2i Devices to be delivered hereunder shall 
be free of defects in material and workmanship under normal use and service for a period of twelve (12) 
months following the date of shipment to DISTRIBUTOR.  
If, during the warranty period, any component part of the equipment becomes defective by reason of 
material or workmanship, and DISTRIBUTOR immediately notifies RAD of such defect, RAD shall have the 
option to choose the appropriate corrective action: a) supply a replacement part, or b) request return of 
equipment to its plant for repair, or c) perform necessary repair at the equipment's location. In the 
event that RAD requests the return of equipment, each party shall pay one-way shipping costs. 
RAD shall be released from all obligations under its warranty in the event that the equipment has been 
subjected to misuse, neglect, accident, or improper installation, or if repairs or modifications were made 
by persons other than RAD's own authorized service personnel, unless such repairs by others were made 
with the written consent of RAD. 
The above warranty is in lieu of all other warranties, expressed or implied. There are no warranties 
which extend beyond the face hereof, including, but not limited to, warranties of merchantability and 
fitness for a particular purpose, and in no event shall RAD be liable for consequential damages. 
RAD shall not be liable to any person for any special or indirect damages, including, but not limited to, 
lost profits from any cause whatsoever arising from or in any way connected with the manufacture, sale, 
handling, repair, maintenance, or use of the ETX-2i Devices, and in no event shall RAD's liability exceed 
the purchase price of the ETX-2i Devices. 
DISTRIBUTOR shall be responsible to its customers for any and all warranties which it makes relating to 
ETX-2i Devices and for ensuring that replacements and other adjustments required in connection with 
the said warranties are satisfactory. 
Software components in the ETX-2i Devices are provided "as is" and without warranty of any kind. RAD 
disclaims all warranties including the implied warranties of merchantability and fitness for a particular 
purpose. RAD shall not be liable for any loss of use, interruption of business, or indirect, special, 
incidental or consequential damages of any kind. In spite of the above, RAD shall do its best to provide 
error-free software products and shall offer free Software updates during the warranty period under 
this Agreement. 
RAD's cumulative liability to you or any other party for any loss or damages resulting from any claims, 
demands, or actions arising out of or relating to this Agreement and the ETX-2i Devices shall not exceed 
the sum paid to RAD for the purchase of the ETX-2i Devices. In no event shall RAD be liable for any 
indirect, incidental, consequential, special, or exemplary damages or lost profits, even if RAD has been 
advised of the possibility of such damages. 
This Agreement shall be construed and governed in accordance with the laws of the State of Israel. 

## Safety and Disposal (English)  *(p.4)*

Safety and Disposal (English) 
General Safety Instructions 
The following instructions serve as a general guide for the safe installation and operation of 
telecommunications products. Additional instructions, if applicable, are included inside the manual. 
This equipment is not suitable for use in locations where children are likely to be present. 
Safety Symbols 
This symbol indicates potential safety hazards regarding product operation 
or maintenance to the equipment. 
 Warning 
This symbol may appear on the equipment or in the text. It indicates 
potential safety hazards regarding product operation or maintenance to 
operator or service personnel. 
Attention. Before carrying out any work with devices, read and follow the 
safety instructions and user manual. 
Danger of electric shock! Avoid any contact with the marked surface while 
the product is energized or connected to outdoor telecommunication lines. 
Safety and Disposal (English) 
 
Shock Hazard!  
Observe the following label on top of the ETX-2i-100G device. 
 
Disconnect all power supply cords before servicing. 
 
Hot surface! Contact may cause burn. Do not touch.  
 
This symbol appears on the top of the ETX-2i-10G/H half 19” model.  
Hot surface! Contact may cause burn. Do not touch.  
 
Protective ground: the marked lug or terminal should be connected to the 
building protective ground bus (to be performed by skilled personnel only). 
 
Safety and Disposal (English) 
 
Some products may be equipped with a laser diode. In such cases, a label 
with the laser class and other warnings as applicable is attached near the 
optical transmitter. The laser warning symbol may be also attached.  
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
 
 
Some products may be equipped with a replaceable battery. There is danger 
of explosion if batteries are mishandled or incorrectly replaced. On systems 
with replaceable batteries, replace only with the same manufacturer and 
type or equivalent type recommended by the manufacturer per the 
instructions provided in the product service manual. Do not disassemble 
batteries or attempt to recharge them outside the system. Do not dispose of 
batteries in fire. Dispose of batteries properly in accordance with the 
manufacturer’s instructions and local regulations.  
In some cases, the users may insert their own SFP laser transceivers into the product. Users are alerted 
that RAD cannot be held responsible for any damage that may result if non-compliant transceivers are 
used. In particular, users are warned to use only agency approved products that comply with the local 
laser safety regulations for Class 1 laser products. 
Products ordered with the NULL power supply ordering option are shipped without their designated 
power supplies. Inasmuch as RAD is responsible for the product functionality and safety and EMC 
effects, such liability is limited only if the product includes the power supplies it was designed to be used 
with and are covered by RAD EMC and safety reports.  
It’s the customer’s responsibility to install only the power supplies defined by RAD for this product and 
are covered by RAD safety and EMC test reports. In case the customer installs any other power supply 
which was not approved or designated by RAD, RAD will have no liability whatsoever to the product 
functionality and/or on any safety or EMC issues that may occur due to the customer action. Any use of 
non-RAD power supplies can cause irrevocable damage to the product or cause hazardous results which 
RAD has no liability for!  
Safety and Disposal (English) 
Always observe standard safety precautions during installation, operation, and maintenance of this 
product. Only qualified, authorized, and skilled service personnel should carry out adjustment, 
maintenance, or repairs to this product. No installation, adjustment, maintenance, or repairs should be 
performed by either the operator or the user. 
ETX-2i units are intended for use in horizontal orientation only. In case of vertical mounting orientation, 
install the unit on top of concrete or other non-combustible surface, such as an external baffle or tray, 
due to safety considerations. 
Handling Energized Products 
General Safety Practices 
Do not touch or tamper with the power supply when the power cord is connected. Mains voltages may 
be present inside certain products even when the power switch (if installed) is in the OFF position or a 
fuse is blown. For DC-powered products, although the voltages levels are usually not hazardous, energy 
hazards may still exist. 
Before working on equipment connected to mains or telecommunication lines, remove jewelry or any 
other metallic object that may come into contact with energized parts.  
Unless otherwise specified, all products are intended to be grounded during normal use. Grounding is 
provided by connecting the mains plug to a wall socket with a protective ground terminal. If a ground 
lug is provided on the product, it should be connected to the protective ground at all times, by a wire of 
diameter 18 AWG or wider. Rack-mounted equipment should be mounted only in grounded racks and 
cabinets. These procedures should be performed by skilled personnel only.  
Always make the ground connection first and disconnect it last. Do not connect telecommunication 
cables to ungrounded equipment. Make sure that all other cables are disconnected before 
disconnecting the ground. 
Some products may have panels secured by thumbscrews with a slotted head. These panels may cover 
hazardous circuits or parts, such as power supplies. These thumbscrews should therefore always be 
tightened securely with a screwdriver after both initial installation and subsequent access to the panels. 
 
Warning 
Before connecting or disconnecting the AC or DC mains connector to/from 
the device, the user should validate that the Power switch in the control 
panel is set to OFF.  
The Power switch can be activated only after the AC or DC mains connector 
is connected to the device. 
Safety and Disposal (English) 
Connecting AC Mains 
Make sure that the electrical installation complies with national and regional regulations. 
Always connect the AC plug to a wall socket with a protective ground. 
The maximum permissible current capability of the branch distribution circuit that supplies power to the 
product is 16A (20A for USA and Canada). The circuit breaker in the building installation should have 
high breaking capacity and must operate at short-circuit current exceeding 35A (40A for USA and 
Canada). 
Always connect the power cord first to the equipment and then to the wall socket. If a power switch is 
provided in the equipment, set it to the OFF position. If the power cord cannot be readily disconnected 
in case of emergency, make sure that a readily accessible circuit breaker or emergency switch is installed 
in the building installation. 
In cases when the power distribution system is IT type, the switch must disconnect both poles 
simultaneously.  
Note 
The Denmark power cord is not provided with the equipment and should 
comply with IEC and the local electrical code. 
Connecting DC Power 
Unless otherwise specified in the manual, the DC input to the equipment is floating in reference to the 
ground. Any single pole can be externally grounded. 
Due to the high current capability of DC power systems, when connecting the DC supply, pay attention 
to avoid short-circuits and fire hazards. 
Make sure that the DC power supply is electrically isolated from any AC source and that the installation 
complies with the local codes. 
The maximum permissible current capability of the branch distribution circuit that supplies power to the 
product is 16A (20A for USA and Canada). The circuit breaker in the building installation should have 
high breaking capacity and must operate at short-circuit current exceeding 35A (40A for USA and 
Canada). 
Before connecting the DC supply wires, ensure that power is removed from the DC circuit. Set to OFF the 
circuit breaker of the panel board that services the equipment and switch it to the OFF position. When 
connecting the DC supply wires, first connect the ground wire to the corresponding terminal, then the 
positive pole, and last the negative pole. Switch the circuit breaker back to the ON position. 
Safety and Disposal (English) 
A readily accessible disconnect device that is suitably rated and approved should be incorporated in the 
building installation. 
If the DC power supply is floating, the switch must disconnect both poles simultaneously. 
Connecting Data and Telecommunication Cables 
Data and telecommunication interfaces are classified according to their safety status. 
The following table lists the status of several standard interfaces. If the status of a given port differs 
from the standard one, a notice is given in the manual. 
Ports 
Safety Status 
V.11, V.28, V.35, V.36, RS-530, X.21, 
10BASE-T, 100BASE-T, 1000BASE-T, 
Unbalanced E1, E2, E3, STM, DS-2, DS-3, 
S-Interface ISDN, Analog voice E&M  
xDSL (without feeding voltage), 
Balanced E1, T1, Sub E1/T1, POE 
Input DC Voltage up to 60 VDC 
ES1 
Electrical energy source class 1  
 
Ports which do not present a safety hazard. Usually up to 
  
30 VAC or 60 VDC. 
FXS, FXO 
Input DC Voltage up to 72 VDC 
ES2 
Electrical energy source class 2 
 
AC power source declared 
ES3 
Electrical energy source class 3 
Always connect a given port to a port of the same safety status. If in doubt, seek the assistance of a 
qualified safety engineer. 
Always make sure that the equipment is grounded before connecting telecommunication cables. Do not 
disconnect the ground connection before disconnecting all telecommunication cables. 
Some ES1 and ES2 (ES3) circuits use the same connectors. Use caution when connecting cables. Extra 
caution should be exercised during thunderstorms. 
When using shielded or coaxial cables, verify that there is a good ground connection at both ends. The 
grounding and bonding of the ground connections should comply with national and regional regulations.  
The telecommunication wiring in the building may be damaged or present a fire hazard in case of 
contact between exposed external wires and the AC power lines. In order to reduce the risk, there are 
restrictions on the diameter of wires in the telecom cables, between the equipment and the mating 
connectors. 
 
Safety and Disposal (English) 
 
Warning 
To reduce the risk of fire, use only No. 26 AWG or larger telecommunication 
line cords. 
 
Some ports are suitable for connection to intra-building or non-exposed wiring or cabling only. In such 
cases, a notice is given in the installation instructions. 
Do not attempt to tamper with any carrier-provided equipment or connection hardware. 
Electromagnetic Compatibility (EMC) 
The equipment is designed and approved to comply with the electromagnetic regulations of major 
regulatory bodies. The following instructions may enhance the performance of the equipment and 
provide better protection against excessive emission and better immunity against disturbances. 
A good ground connection is essential. When installing the equipment in a rack, make sure to remove all 
traces of paint from the mounting points. Use suitable lock-washers and torque. If an external grounding 
lug is provided, connect it to the ground bus using braided wire as short as possible. 
The equipment is designed to comply with EMC requirements when connecting it with unshielded 
twisted pair (UTP) cables with the exception of 1000BaseT ports that must always use shielded twisted 
pair cables of good quality (CAT 5E or higher). However, the use of shielded wires is always 
recommended, especially for high-rate data. In some cases, when unshielded wires are used, ferrite 
cores should be installed on certain cables. In such cases, special instructions are provided in the 
manual. 
Disconnect all wires which are not in permanent use, such as cables used for one-time configuration. 
The compliance of the equipment with the regulations for conducted emission on the data lines is 
dependent on the cable quality. The emission is tested for UTP with 80 dB longitudinal conversion loss 
(LCL). 
Unless otherwise specified or described in the manual, ES1 and ES2 electrical energy sources provide 
protection against surges on the data lines. Primary protectors should be provided in the building 
installation. 
The equipment is designed to provide adequate protection against electrostatic discharge (ESD). 
However, it is good working practice to use caution when connecting cables terminated with plastic 
connectors (without a grounded metal hood, such as flat cables) to sensitive data lines. Before 
connecting such cables, discharge yourself by touching ground or wear an ESD preventive wrist strap. 
Safety and Disposal (English) 
FCC-15 User Information 
This equipment has been tested and found to comply with the limits of the Class A digital device, 
pursuant to Part 15 of the FCC rules. These limits are designed to provide reasonable protection against 
harmful interference when the equipment is operated in a commercial environment. This equipment 
generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with 
the Installation and Operation manual, may cause harmful interference to the radio communications. 
Operation of this equipment in a residential area is likely to cause harmful interference in which case the 
user will be required to correct the interference at his own expense. 
Canadian Emission Requirements 
This Class B digital apparatus meets all the requirements of the Canadian Interference-Causing 
Equipment Regulations. 
Warning per EN 55032 (CISPR 32) 
 
 Warning 
This equipment is compliant with Class A of CISPR 32. In a residential 
environment, this equipment may cause radio interference. 
Product Disposal 
 
To facilitate the reuse, recycling and other forms of recovery of waste 
equipment in protecting the environment, the owner of this RAD product is 
required to refrain from disposing of this product as unsorted municipal 
waste at the end of its life cycle. Upon termination of the unit’s use, 
customers should provide for its collection for reuse, recycling, or other form 
of environmentally conscientious disposal. 
 

## Sécurité et Elimination (Français)  *(p.12)*

Sécurité et Elimination (Français) 
Instructions générales de sécurité 
Les instructions suivantes servent de guide général d'installation et d'opération sécurisées des produits 
de télécommunications. Des instructions supplémentaires sont éventuellement indiquées dans le 
manuel. 
Cet équipement ne convient pas pour une utilisation dans des endroits où des enfants sont 
susceptibles d’être presents. 
Symboles de sécurité 
Ce symbole indique des dangers potentiels pour la sécurité relatifs  au 
fonctionnement du produit ou la maintenance de l'équipement. 
 
 
Avertissement 
Ce symbole peut apparaitre sur l'équipement ou dans le texte. Il indique des 
risques potentiels de sécurité pour l'opérateur ou le personnel de service, 
quant à l’utilisation du produit ou à sa maintenance. 
 
 
Attention. Avant d'effectuer tout travail avec les appareils, lisez et suivez les 
consignes de sécurité et le manuel d'utilisation. 
 
 
Danger de choc électrique ! Evitez tout contact avec la surface marquée tant 
que le produit est sous tension ou connecté à des lignes externes de 
télécommunications. 
 
Sécurité et Elimination (Français) 
 
Risque d'électrocution !  
Respectez l'étiquette suivante sur le dessus de l'appareil ETX-2i-100G. 
 
Débranchez tous les cordons d'alimentation avant l’entretien. 
 
Surface chaude! Tout contact peux causer des brulures. Ne pas toucher. 
 
 
Mise à la terre de protection : la cosse ou la borne marquée devrait être 
connectée à la prise de terre de protection du bâtiment (à effectuer 
uniquement par du personnel qualifié).  
 
Sécurité et Elimination (Français) 
 
Certains produits peuvent être équipés d'une diode laser. Dans de tels cas, 
une étiquette indiquant la classe laser (ainsi que d'autres avertissements le 
cas échéant) sera jointe près du transmetteur optique. Le symbole 
d'avertissement laser peut aussi être joint.  
Veuillez observer les précautions suivantes : 
• 
Avant la mise en marche de l'équipement, assurez-vous que le câble de 
fibre optique est intact et qu'il est connecté au transmetteur. 
• 
Ne tentez pas d'ajuster le courant de la commande laser. 
• 
N'utilisez pas des câbles ou connecteurs de fibre optique cassés ou sans 
terminaison et n'observez pas directement un rayon laser. 
• 
L'usage de périphériques optiques avec l'équipement augmentera le 
risque pour les yeux. 
• 
L'usage de contrôles, ajustages ou procédures autres que celles 
spécifiées ici pourrait résulter en une dangereuse exposition aux 
radiations. 
ATTENTION : Le rayon laser peut être invisible ! 
 
 
Certains produits peuvent être équipés d'une pile remplaçable. Il existe un 
risque d'explosion si les piles sont manipulées ou remplacées de manière 
incorrecte. Sur les systèmes dotés de piles remplaçables, remplacez celles-ci 
uniquement par des piles de même marque et de même type ou un type 
équivalent recommandé par le fabricant conformément aux instructions 
fournies dans le manuel d'entretien du produit. Ne démontez pas les piles et 
n'essayez pas de les recharger en dehors du système. Ne jetez pas les piles 
au feu. Jetez les piles conformément aux instructions du fabricant et aux 
réglementations locales. 
Les utilisateurs pourront, dans certains cas, insérer leurs propres émetteurs-récepteurs Laser SFP dans le 
produit. Les utilisateurs sont avertis que RAD ne pourra pas être tenue responsable de tout dommage 
pouvant résulter de l'utilisation d'émetteurs-récepteurs non conformes. Plus particulièrement, les 
utilisateurs sont avertis de n'utiliser que des produits approuvés par l'agence et conformes à la 
réglementation locale de sécurité laser pour les produits laser de classe 1. 
Les produits commandés avec l'option de commande d'alimentation NULL sont expédiés sans leurs 
alimentations désignées. Dans la mesure où RAD est responsable de la fonctionnalité du produit et de 
ses effets sur la sécurité et la CEM, cette responsabilité est limitée uniquement si le produit comprend 
les alimentations avec lesquelles il a été conçu et qui sont couvertes par les rapports de sécurité et de 
CEM de RAD.  
Sécurité et Elimination (Français) 
Il est de la responsabilité du client d'installer uniquement les alimentations définies par RAD pour ce 
produit et qui sont couvertes par les rapports de test de sécurité et de CEM de RAD.  
Dans le cas où le client installe une autre alimentation qui n'a pas été approuvée ou désignée par RAD, 
RAD ne sera pas responsable de la fonctionnalité du produit et/ou de tout problème de sécurité ou de 
CEM qui pourrait survenir en raison de l'action du client. Toute utilisation d'alimentations non RAD peut 
causer des dommages irrévocables au produit ou provoquer des résultats dangereux pour lesquels RAD 
n'a aucune responsabilité ! 
Respectez toujours les précautions standards de sécurité durant l'installation, l'opération et la 
maintenance de ce produit. Seul le personnel de service qualifié, autorisé et compétent devrait 
effectuer l'ajustage, la maintenance ou les réparations de ce produit. Aucune opération d'installation, 
d'ajustage, de maintenance ou de réparation ne devrait être effectuée par l'opérateur ou l'utilisateur. 
Manipuler des Produits sous Tension 
Règles Générales de Sécurité 
Ne pas toucher ou altérer l'alimentation en courant lorsque le câble d'alimentation est branché. Des 
tensions secteur peuvent être présentes dans certains produits, même lorsque le commutateur (s'il est 
installé) est en position OFF ou si le fusible est rompu. Pour les produits alimentés par CC, les niveaux de 
tension ne sont généralement pas dangereux mais des risques de courant peuvent toujours exister. 
Avant de travailler sur des équipements connectés ausecteur ou aux lignes de télécommunication, 
retirez vos bijoux ou tout autre objet métallique pouvant venir en contact avec les pièces sous tension.  
Sauf s'il en est autrement indiqué, tous les produits sont destinés à être mis à la terre durant l'usage 
normal. La mise à la terre est fournie par la connexion de la fiche principale à une prise murale équipée 
d'une borne protectrice de mise à la terre. Si une cosse de mise à la terre est fournie avec le produit, elle 
devrait être connectée à tout moment à une mise à la terre de protection par un conducteur de 
diamètre 18 AWG ou plus. L'équipement monté en châssis ne devrait être monté que sur des châssis et 
dans des armoires mises à la terre. Ces procédures doivent être effectuées uniquement par du 
personnel qualifié. 
Branchez toujours la mise à la terre en premier et débranchez-la en dernier. Ne branchez pas des câbles 
de télécommunications à un équipement qui n'est pas mis à la terre. Assurez-vous que tous les autres 
câbles sont débranchés avant de déconnecter la mise à la terre. 
Sécurité et Elimination (Français) 
 
Avertissement 
Avant de brancher ou de débrancher le connecteur secteur AC ou DC de 
l'appareil, l'utilisateur doit vérifier que l'interrupteur d'alimentation du 
panneau de commande soit bien sur OFF. 
L'interrupteur d'alimentation ne peut être activé qu'après que le connecteur 
secteur AC ou DC soit connecté à l'appareil. 
Connexion au Courant du Secteur 
Assurez-vous que l'installation électrique est conforme à la réglementations nationales et régionales. 
Branchez toujours la fiche de secteur à une prise murale équipée d'une borne protectrice de mise à la 
terre. 
La capacité maximale permissible en courant du circuit de distribution de la connexion alimentant le 
produit est de 16A (20A aux Etats-Unis et Canada). Le coupe-circuit dans l'installation du bâtiment 
devrait avoir une capacité élevée de rupture et devrait fonctionner sur courant de court-circuit 
dépassant 35A (40A aux Etats-Unis et Canada). 
Branchez toujours le câble d'alimentation en premier à l'équipement puis à la prise murale. Si un 
commutateur est fourni avec l'équipement, fixez-le en position OFF. Si le câble d'alimentation ne peut 
pas être facilement débranché en cas d'urgence, assurez-vous qu'un coupe-circuit ou un disjoncteur 
d'urgence facilement accessible est installé dans le bâtiment. 
Le disjoncteur devrait déconnecter simultanément les deux pôles si le système de distribution de 
courant est de type IT.  
Note 
Le cordon d'alimentation du Danemark n'est pas fourni avec l'équipement et 
doit être conforme à la CEI et au code électrique local. 
Connexion d'alimentation CC 
Sauf s'il en est autrement spécifié dans le manuel, l'entrée CC de l'équipement est flottante par rapport 
à la mise à la terre. Tout pôle doit être mis à la terre en externe. 
A cause de la capacité de courant des systèmes à alimentation CC, des précautions devraient être prises 
lors de la connexion de l'alimentation CC pour éviter des courts-circuits et des risques d'incendie. 
Assurez-vous que l'alimentation CC est isolée de toute source de courant CA (secteur) et que 
l'installation est conforme à la réglementation locale. 
La capacité maximale permissible en courant du circuit de distribution de la connexion alimentant le 
produit est de 16A (20A aux Etats-Unis et Canada). Le coupe-circuit dans l'installation du bâtiment 
Sécurité et Elimination (Français) 
devrait avoir une capacité élevée de rupture et devrait fonctionner sur courant de court-circuit 
dépassant 35A (40A aux Etats-Unis et Canada). 
Avant la connexion des câbles d'alimentation en courant CC, assurez-vous que le circuit CC n'est pas 
sous tension. Localisez le coupe-circuit dans le tableau desservant l'équipement et fixez-le en position 
OFF. Lors de la connexion de câbles d'alimentation CC, connectez d'abord le conducteur de mise à la 
terre à la borne correspondante, puis le pôle positif et en dernier, le pôle négatif. Remettez le coupe-
circuit en position ON. 
Un disjoncteur facilement accessible, adapté et approuvé devrait être intégré à l'installation du 
bâtiment. 
Le disjoncteur devrait déconnecter simultanément les deux pôles si l'alimentation en courant CC est 
flottante. 
Connexion de Câbles de Données et de Télécommunications 
Les interfaces de données et de télécommunications sont classées selon leur niveau de sécurité.  
Le tableau suivant liste les statuts de plusieurs interfaces standards. Si le statut d’un port donné diffère 
d’un standard, une notification sera fournie dans le manuel. 
Ports 
Niveau de sécurité 
V.11, V.28, V.35, V.36, RS 530, X.21, 
10BASE-T, 100BASE-T, 1000BASE-T, 
asymétrique E1, E2, E3, STM, DS-2, DS-
3, S Interface ISDN (RNIS), Voix 
analogique E&M  
xDSL (sans tension d’alimentation), 
symétrique E1, T1, Sub E1/T1, POE 
Tension d'entrée DC jusqu'à 60 VDC 
ES1 
Source d'énergie électrique de classe 1 
 
Ports qui ne présentent pas un danger pour la sécurité. 
 
Généralement jusqu’à 30 VAC (courant alternatif) ou 60 VDC 
 
(courant continu). 
FXS, FXO 
Tension d'entrée DC jusqu'à 72 VDC 
ES2 
Source d'énergie électrique de classe 2 
Source d'énergie CA déclarée 
ES3 
Source d'énergie électrique de classe 3 
Toujours connecter un port donné à un port de même niveau de sécurité. En cas de doute, solliciter 
l’assistance d’un ingénieur de sécurité qualifié. 
Toujours s’assurer que l’équipement est relié à la terre avant de connecter des câbles de 
télécommunications. Ne pas déconnecter la connexion à la terre avant la déconnexion de tous les câbles 
de télécommunications. 
Sécurité et Elimination (Français) 
Certains circuits ES1 et ES2 (ES3) utilisent les memes connecteurs. Soyez prudents lors de la connexion 
des câbles. Une extrême prudence est requise en cas d’orages. 
En cas d’utilisation de cables blindés ou coaxiaux, vérifier qu’il y a bien une connexion à la terre aux deux 
extrémités. Le raccordement à la terre et la liaison à la prise de terre doivent être conformes à la 
réglementations nationales et régionales.  
Il se peut que le câblage de télécommunications dans le bâtiment soit endommagé ou présente un 
danger d’incendie en cas de contact entre des câbles externes dénudés et les lignes électriques AC 
(courant alternatif). Afin de réduire le risque, il y a une limitation du diamètre des fils dans les câbles de 
télécommunications, entre l’équipement et les connecteurs homologues. 
 
Avertissement 
Pour réduire les risques d’incendie, utiliser seulement des cordons de 
télécommunications 26 AWG ou de section supérieure. 
 
Certains ports sont uniquement adaptés à une connexion à un câblage interne ou à un câblage non 
exposé. Dans ce cas, une notification sera fournie dans les instructions d’installation. 
Ne pas tenter de démonter l’équipement ou le matériel de connexion. 
Compatibilité Electromagnétique (CEM) 
L'équipement est conçu et approuvé pour se conformer aux réglementations électromagnétiques des 
principaux organismes de réglementation. Les instructions suivantes peuvent améliorer les 
performances de l'équipement et fournir une meilleure protection contre les émissions excessives et 
une meilleure immunité contre les perturbations. 
Une bonne connexion à la terre est essentielle. Lors de l'installation de l'équipement dans un rack, 
veillez à éliminer toute trace de peinture des points de montage. Utilisez des rondelles de blocage et un 
couple appropriés. Si une cosse de mise à la terre externe est fournie, connectez-la au bus de terre à 
l'aide d'un fil tressé aussi court que possible. 
L’équipement est conçu pour répondre aux exigences CEM lors de la connexion avec des câbles à paires 
torsadées non blindées (UTP), à l’exception des ports 1000BaseT, qui doivent toujours utiliser des câbles 
à paires torsadées blindés de bonne qualité (CAT 5E ou supérieure). Cependant, l'utilisation de câbles 
blindés est toujours recommandée, en particulier pour les données à haut débit. Dans certains cas, 
lorsque des câbles non blindés sont utilisés, des noyaux en ferrite doivent être installés sur certains 
câbles. Dans ce cas, des instructions spéciales sont fournies dans le manuel. 
Sécurité et Elimination (Français) 
Débranchez tous les câbles qui ne sont pas utilisés de manière permanente, tels que les câbles utilisés 
pour une configuration unique. 
La conformité de l'équipement à la réglementation en matière d'émission conduite sur les lignes de 
données dépend de la qualité du câble. L'émission est testée pour des câbles UTP avec un 
affaiblissement de conversion longitudinale (LCL) de 80 dB. 
Sauf indication contraire ou décrite dans le manuel, les sources d'énergie électrique ES1 et ES2 offrent 
protection contre les surtensions sur les lignes de données. Des protections primaires doivent être 
fournies dans l’installation du bâtiment. 
L'équipement est conçu pour fournir une protection adéquate contre les décharges électrostatiques 
(DES). Toutefois, il est recommandé de faire preuve de prudence lors du raccordement de câbles munis 
de connecteurs en plastique (sans capot métallique mis à la terre, tels que des câbles plats) sur des 
lignes de données sensibles. Avant de connecter ces câbles, déchargez-vous en touchant le sol ou portez 
un bracelet antistatique. 
FCC-15 Information Utilisateur 
Cet équipement a été testé et déclaré conforme aux limites d’un appareil numérique de classe A, 
définies à la section 15 du règlement de la FCC. Ces limites sont conçues pour fournir une protection 
raisonnable contre les interférences nuisibles lorsque l'équipement est utilisé dans un environnement 
commercial. Cet équipement génère, utilise et peut émettre de l'énergie de fréquence radio, s'il n'est 
pas installé et utilisé conformément au Manuel d'Installation et d'Utilisation, il peut provoquer des 
interférences nuisibles aux communications radio. L'utilisation de cet équipement dans une zone 
résidentielle est susceptible de provoquer des interférences nuisibles, dans ce cas, l'utilisateur sera tenu 
de corriger les interférences à ses frais. 
Exigences d’Emissions Canadiennes 
Cet appareil numérique de Classe B répond a toutes les exigences de la réglementation canadienne sur 
les équipements causant des interférences. 
Avertissement: EN 55032 (CISPR 32) 
 
Avertissement 
Cet appareil est conforme a la Classe A de la CISPR 32. Dans un 
environnement résidentiel, il peut provoquer des interférences radio. 
Sécurité et Elimination (Français) 
Élimination du Produit 
 
Afin de faciliter la réutilisation, le recyclage ainsi que d'autres formes de 
récupération d'équipement mis au rebut dans le cadre de la protection de 
l'environnement, il est demandé au propriétaire de ce produit RAD de ne pas 
mettre ce dernier au rebut en tant que déchet municipal non trié, une fois 
que le produit est arrivé en fin de cycle de vie. Le client devrait proposer des 
solutions de réutilisation, de recyclage ou toute autre forme de mise au 
rebut de cette unité dans un esprit de protection de l'environnement, 
lorsqu'il aura fini de l'utiliser. 

## Sicherheit und Entsorgung (Deutsch)  *(p.21)*

Sicherheit und Entsorgung (Deutsch) 
Allgemeine Sicherheitsanleitung 
Die folgenden Anleitungen dienen als allgemeiner Leitfaden für die sichere Installation und Bedienung 
von Telekommunikationsprodukten. Zusätzliche Anleitungen sind im Nutzerhandbuch vorhanden. 
Dieses Gerät ist nicht für die Verwendung an Orten geeignet, an denen sich Kinder aufhalten können. 
Sicherheitssymbole 
Dieses Symbol weist auf potenzielle Sicherheitsgefahren im Zusammenhang 
mit dem Betrieb oder der Wartung des Geräts hin. 
 
 
 Achtung 
Dieses Symbol kann auf ihren Geraeten oder im Text auftauchen. Es weist 
den Nutzer oder das Servicepersonal auf möglche Gefahren bei der 
Bedienung der Geräte hin. 
 
Beachtung. Lesen und befolgen Sie vor allen Arbeiten an Geräten die 
Sicherheitshinweise und die Bedienungsanleitung. 
 
 
Gefahr eines elektrischen Schlages! Vermeiden Sie jeglichen Kontakt mit der 
gekennzeichneten Oberfläche während das Gerät unter Spannung steht 
oder an auβenliegende Telekommunikationsleitungen angeschlossen ist. 
 
Sicherheit und Entsorgung (Deutsch) 
 
Gefahr von Stromschlägen! 
Beachten Sie das folgende Etikett auf der Oberseite des ETX-2i-100G-Geräts. 
 
Ziehen Sie vor der Wartung alle Netzkabel ab. 
 
Heiße Oberfläche! Berührung kann Verbrennungen verursachen. Nicht 
berühren. 
 
 
Schutzerdung: Die gekennzeichnete Mutter oder das Terminal müssen an 
den Anschluss der Haupterdung des Gebäudes angeschlossen sein (nur von 
Fachpersonal durchzuführen). 
 
Sicherheit und Entsorgung (Deutsch) 
 
Einige Produkte können mit einer Laserdiode ausgestattet sein. In solchen 
Fällen muβ ein Aufkleber mit der Laserklasse und entsprechenden 
Warnungen neben dem optischen Transmitter angebracht sein. Das 
Warnsymbol für Laser kann zusätzlich angebracht sein. 
Bitte beachten Se die folgenden Vorsichtsmaβnahmen: 
• 
Vor der Inbetriebnahme des Gerätes, vergewissern Sie sich, daβ das 
optische Glasfaserkabel unbeschädigt ist und an den Transmitter 
angeschlossen ist. 
• 
Versuchen Sie nicht, den durch den Laser fliessenden Strom zu 
regulieren. 
• 
Verwenden Sie keine gebrochenen oder anderweitig unvollständige 
Glasfaserkabel oder Stecker. Blicken Sie nicht in den Laserstrahl. 
• 
Die Benutzung optischer Komponenten zusammen mit Ihrem Gerät 
erhöhen die Gefahr für Ihre Augen. 
• 
Die Benutzung von Bedienelementen, die Geräteeinstellung oder die 
Ausführung von Prozessen, die hier nicht aufgeführt sind, können zu 
gefährlicher Strahlung führen. 
ACHTUNG: Der Laserstrahl kann unsichtbar sein! 
 
 
Einige Produkte können mit einer austauschbaren Batterie ausgestattet 
sein. Es besteht Explosionsgefahr, wenn die Batterien falsch gehandhabt 
oder falsch ausgetauscht werden. Bei Systemen mit austauschbaren 
Batterien dürfen diese nur durch Batterien desselben Herstellers und 
desselben Typs oder eines gleichwertigen, vom Hersteller empfohlenen Typs 
gemäß den Anweisungen im Wartungshandbuch des Produkts ersetzt 
werden. Nehmen Sie die Batterien nicht auseinander und versuchen Sie 
nicht, sie außerhalb des Systems wieder aufzuladen. Entsorgen Sie die 
Batterien nicht im Feuer. Entsorgen Sie die Batterien ordnungsgemäß in 
Übereinstimmung mit den Anweisungen des Herstellers und den örtlichen 
Vorschriften. 
In einigen Fällen werden Nutzer eigene SFP-Lasertransceiver in das Gerät einführen. Nutzer sind darauf 
hingewiesen, dass RAD nicht verantwortlich zeichnet für Beschädigungen, die von nicht kompatiblen 
Transceivern herrühren. Nutzer seien ferner darauf hingewiesen, daβ ausschlieβlich amtlich zugelassene 
Produkte eingesetzt werden sollten, die den ortsüblichen Sicherheitsbestimmungen für Lasergeräte der 
Laserklasse 1 entsprechen. 
Produkte, die mit der Bestelloption NULL Netzteile bestellt werden, werden ohne die vorgesehenen 
Netzteile geliefert. Da RAD für die Produktfunktionalität sowie die Sicherheits- und EMV-Auswirkungen 
Sicherheit und Entsorgung (Deutsch) 
verantwortlich ist, ist diese Haftung nur dann beschränkt, wenn das Produkt die Netzteile enthält, für die 
es konzipiert wurde und die durch die EMV- und Sicherheitsberichte von RAD abgedeckt sind.  
Es liegt in der Verantwortung des Kunden, nur die von RAD für dieses Produkt definierten Netzteile zu 
installieren, die durch RADs Sicherheits- und EMV-Testberichte abgedeckt sind. Falls der Kunde ein 
anderes Netzteil installiert, das nicht von RAD genehmigt oder bestimmt wurde, übernimmt RAD 
keinerlei Haftung für die Produktfunktionalität und/oder für etwaige Sicherheits- oder EMV-Probleme, 
die aufgrund der Aktion des Kunden auftreten könnten. Die Verwendung von Nicht-RAD-Netzteilen kann 
das Produkt unwiderruflich beschädigen oder zu gefährlichen Ergebnissen führen, für die RAD keine 
Haftung übernimmt! 
Beachten Sie ferner die üblichen Sicherheitsmaβnahmen während der Installation, des Betriebs, der 
Wartung oder der Reparatur des Gerätes. Installationen, Einstellungen und Reparaturen sollten 
ausschließlich vom Nutzer oder von qualifiziertem und autorisiertem Service-Fachpersonal 
vorgenommen werden. 
Umgang mit Geräten unter Spannung 
Grundlegende Sicherheitsmaβnahmen 
Berühren oder verändern Sie das Netzteil nicht wenn das Stromkabel angeschlossen ist. In bestimmten 
Produkten kann Netzspannung vorhanden sein, selbst wenn sich der Netzschalter (falls installiert) in der 
Position AUS befindet oder eine Sicherung durchgebrannt ist. Für Produkte, die unter 
Gleichstromspannung (DC) stehen, besteht ebenfalls die Gefahr eines elektrischen Schlages, auch wenn 
die angelegte Spannung in der Regel nicht gefährlich ist. 
Legen Sie Schmuck oder sonstige Metallobjekte ab, bevor Sie mit Geräten arbeiten, die an Netz- oder 
Telekommunikationsleitungen angeschlossen sind, um zu verhindern, daβ dies mit spannungsgeladenen 
Bauteilen in Berührung kommen. 
Falls nicht anders angegeben, sollten alle Produkte bei normalem Gebrauch geerdet werden. Die Erdung 
erfolgt durch den Anschlss an eine Steckdose mit Schutzerdung. Wenn das Gerät mit einer 
Erdungslasche ausgestattet ist, sollte diese immer an die Schutzerde angeschlossen sein mit einem 
Kabel, das einen Durchmesser von mindestens 18 AWG aufweist. Geräte für die Rack-Montage sollten 
ausschlieβlich in geerdeten Racks oder Schränken montiert werden. Diese Verfahren sollten nur von 
Fachpersonal durchgeführt werden. 
Schlieβen Sie grundsätzlich zuerst die Schutzerde an und klemmen Sie diese zuletzt ab. Schlieβen Sie 
keine Telekommunikationskabel an nicht geerdete Geräte an. Stellen Sie sicher, dass alle anderen Kabel 
abgeklemmt sind, bevor Sie die Erdung abklemmen. 
Sicherheit und Entsorgung (Deutsch) 
Die Frontpanele einiger Geräte sind mit Flügelschrauben mit Schlitz gesichert. Diese Paneele decken 
gefährliche Schalkreise oder Teile, wie zum Beispiel Netzteile ab. Diese Flügelschrauben sollten daher 
immer mittels eines Schraubenziehers sicher angezogen werden nach der Erstinstallation und jedem 
späterem Zugriff auf die Paneele. 
 
 Achtung 
Vor dem Anschließen oder Trennen des AC- oder DC-Netzsteckers an 
das/vom Gerät, sollte der Benutzer sicherstellen, dass der Netzschalter im 
Bedienfeld auf OFF gestellt ist. 
Der Netzschalter kann erst aktiviert werden, nachdem der AC- oder DC-
Netzstecker mit dem Gerät verbunden ist. 
Anschluss an eine Wechselstromquelle (AC) 
Stellen Sie sicher, daβ die elektrische Installation den nationalen und regionalen Bestimmungen 
entspricht. 
Stecken Sie den Stecker immer in eine Steckdose mit Schutzerdung ein. 
Der maximal mögliche Stromfluss im Bereich des Verteilerstromkreis, der die Stromversorgung des 
Gerätes sicherstellt, ist 16 A (20A in den USA und in Kanada). Der Schutzschalter in der 
Gebäudeinstallation muss starke Ströme unterbrechen können und muss den Stromfluss bei 35A (40A in 
den USA und Kanada) unterbrechen. 
Schlieβen Sie das Netzkabel zuerst an das Gerät und dann an die Steckdose an. Falls ein Ein/Aus-Schalter 
zur Verfügung steht, schalten Sie diesen auf AUS (OFF). Falls das Netzkabel im Notfall nicht schnell 
herausgezogen werden kann, stellen Sie sicher, daβ ein Schutzschalter oder Notschalter Bestandteil der 
elektrischen Installation des Gebäudes ist. 
Falls die Stromversorgung über einen IT Netz-Verteiler erfolgt, muss der Schalter die Stromversorgung 
zu beiden Polen gleichzeitig unterbrechen. 
Note 
Das dänische Netzkabel ist nicht im Lieferumfang des Geräts enthalten und 
sollte der IEC und den örtlichen Elektrovorschriften entsprechen. 
Anschluss an eine Gleichstromquelle (DC) 
Falls im Benutzerhandbuch (Manual) nicht anderweitig beschrieben, schwankt die Gleichstromzufuhr 
relativ zur Erdung. Jeder einzelne Pol kann von aussen geerdet werden. 
Aufgrund der Fähigkeit, hohe Stromflüsse zu verarbeiten, muss sorgfältig vorgegangen werden beim 
Anschluss der Gleichstromquelle, um Kurzschlüsse und Brände zu vermeiden. 
Stellen Sie sicher, daβ Gleichstromquellen (DC) von Wechselstromquellen (AC) isoliert sind und daβ die 
Installation den örtlichen Richtlinien entspricht. 
Sicherheit und Entsorgung (Deutsch) 
Der maximal mögliche Stromfluss im Bereich des Verteilerstromkreis, der die Stromversorgung des 
Gerätes sicherstellt, ist 16 A (20A in den USA und in Kanada). Der Schutzschalter in der 
Gebäudeinstallation muss starke Ströme unterbrechen können und muss den Stromfluss bei 35A (40A in 
den USA und Kanada) unterbrechen. 
Vor dem Anschluss der Gleichstrom-Speisekabel ist sicher zu stellen, daβ kein Strom über den 
Gleichstromkreis flieβt. Finden Sie den Schutzschalter an der Schalttafel, die das Gerät bedient, und 
schalten Sie ihn auf AUS (OFF). Wenn Sie die Gleichstrohmdrähte anschlieβen, schliessen Sie zuerst den 
Erdungsdraht an das zugehörige Terminal an, dann den Pluspol und zuletzt den Minuspol. Schalten Sie 
den Schutzschalter zurück auf AN (ON). 
Ein verfügbares nicht angeschlossenes Gerät, das ordnungsgemäβ genehmigt und abgenommen wurde, 
sollte in die bestehende Installation eingebaut werden. 
Falls die Gleichstromspannung schwankt, muss der Schalter beide Pole gleichzeitig trennen. 
Anschluss von Daten- und Telekommunikationskabeln 
Daten- und Telekommunikationsschnittstellen sind gemäβ ihrem Sicherheitsstatus klassifiziert. 
Verschiedene Standardschnittstellen sind zusammen mit ihrem jeweiligen Sicherheitsstatus in der 
folgenden Tabelle aufgeführt. Auf eventuelle Abweichungen vom Standardsicherheitsstatus wird im 
Benutzerhandbuch (Manual) gesondert hingewiesen. 
Schnittstellen 
Sicherheitsstatus 
V.11, V.28, V.35, V.36, RS 530, X.21, 
10BASE-T, 100BASE-T, 1000BASE-T, 
Unsymmetrisches E1, E2, E3, STM, DS-2, 
DS-3, S-Schnittstelle ISDN, 
Analogsprache E&M  
xDSL (ohne einspeisende Spannung), 
symmetrisches E1, T1, Sub-E1/T1, POE  
Eingangs-Gleichspannung bis zu 60 VDC 
ES1 
Elektrische Energiequelle Klasse 1 
 
Anschlüsse, die kein Sicherheitsrisiko darstellen, 
 
normalerweise bis zu 30 VAC oder 60 VDC. 
FXS, FXO 
Eingangs-Gleichspannung bis zu 72 VDC 
ES2 
Elektrische Energiequelle Klasse 2 
AC-Spannungsquelle deklariert 
ES3 
Elektrische Energiequelle Klasse 3 
Verbinden Sie Anschlüsse, die denselben Sicherstatus aufweisen. Wenn Sie nicht sicher sind, wenden Sie 
sich bitte an einen qualifizierten Sicherheitsingenieur. 
Sicherheit und Entsorgung (Deutsch) 
Vergewissern Sie sich immer, daβ das Gerät geerdet ist bevor Sie Telekommunikationskabel 
anschlieβen. Klemmen Sie die Erdung nie ab, bevor Sie Telekommunikationskabel abklemmen. 
Einige ES1 und ES2 (ES3)-Stromkreise nutzen dieselben Stecker. Seien Sie vorsichtig, wenn Sie Kabel 
anschlieβen. Seien Sie besonders vorsichtig während einem Gewitter. 
Wenn Sie abgeschirmte -, oder Koaxialkabel nutzen, stellen Sie sicher, daβ diese an beiden Enden eine 
gute Erdung aufweisen. Die Erdung und Verbindung der Masseanschlüsse sollte den nationalen und 
regionalen Vorschriften entsprechen. 
Wenn auβenliegende Kabel und Wechselstromleitungen (AC) in Kontakt kommen, kann die Verkabelung 
innerhalb des Gebäudes beschädigt werden oder einen Brand auslösen. Um dieses Risiko zu verringern, 
gibt es Bestimmungen zum Durchmesser von Telekommunikationskabeln zwischen den Geräten und 
den Anschlüssen. 
 
Achtung 
Um das Brandrisiko zu reduzieren, setzen Sie ausschließlich 26 AWG oder 
dickere Telekommunikationskabel ein. 
Einige Anschlüsse eignen sich lediglich für Verbindungen zu gebäude-internen oder nicht 
außenliegenden Verkabelungen. Auf solche Fälle wird in der Installationsanleitung gesondert 
hingewiesen. 
Versuchen Sie nicht, die vom Carrier erhaltene Ausrüstung oder Verbindungselemente zu manipulieren. 
Elektromagnetische Kompatibilität (EMC) 
Die Ausrüstung ist ausgelegt und anerkannt für die Erfüllung elektromagnetischer Bestimmungen der 
Regulierungsbehörden. Die nachfolgenden Anleitungen sind darauf ausgerichtet, die Leistungsfähigkeit 
der Ausrüstung zu erhöhen und besseren Schutz gegen extreme Emissionen und besseren Schutz gegen 
Störungen zu gewährleisten. 
Eine gute Erdung ist wesentlich. Wenn die Ausrüstung in einem Rack montiert wird, stellen Sie sicher, 
daβ jegliche Farbspuren von den Befestigungspunkten entfernt sind. Benutzen Sie geeignete 
Sicherungsscheiben und das richtige Drehmoment. Falls eine externe Erdungsmutter zur Verfügung 
steht, schließen Sie diese an den Erdbus an mittels kürzestmöglichem verdrillten Draht. 
Die Ausrüstung ist ausgelegt, um den Anforderungen der EMC zu entsprechen, wenn man sie mit nicht 
abgeschirmten und verdrillten (UTP) Kabeln anschließt mit Ausnahme von 1000BaseT-Anschlüssen, die 
grundsätzlich mit abgeschirmten verdrillten Kabeln hoher Qualität (CAT 5E oder besser) erfordern. Im 
Allgemeinen ist die Verwendung von abgeschirmten Kabeln immer empfohlen, besonders für schnellen 
Datendurchsatz. Beim Einsatz nicht abgeschirmter Kabel wird in manchen Fällen empfohlen, einen 
Sicherheit und Entsorgung (Deutsch) 
Ferritkern an bestimmten Kabeln anzubringen. In diesen Fällen werden im Benutzerhandbuch 
gesonderte Anleitungen bereitgestellt. 
Klemmen Sie alle Kabel ab, die nicht permanent in Gebrauch sind, wie zum Beispiel solche, die fuer eine 
einmalige Konfiguration eingesetzt wurden. 
Die Einhaltung der Regeln für elektromagnetische Leitungsemissionen an den Datenleitungen hängt von 
der Kabelqualität ab. Die Emission wurde für UDP mit 80 db Längsumwandlungsdämpfung (LCL) 
getestet. 
Falls im Benutzerhandbuch nicht anders spezifiziert oder beschrieben, Elektrische Energiequelles ES1 
und ES2 Anschlüsse lediglich Schutz gegen Überspannungen in den Datenleitungen. Primäre Protektoren 
müssen innerhalb der Gebäudeinstallation bereitgestellt werden. 
Die Ausrüstung ist ausgelegt, ausreichenden Schutz gegen elektrostatische Entladung (ESD) zu bieten. Es 
ist jedoch empfehlenswert, vorsichtig zu agieren, wenn Kabel mit Plastikanschlüssen (ohne geerdete 
Metallhalterung wie bei flachen Kabeln) und empfindliche Datenleitungen angeschlossen werden. Vor 
dem Anschliessen solcher Kabel, entladen Sie sich selbst durch Berührung des Bodens oder durch das 
Tragen eines ESD-präventiven Bandes um das Handgelenk. 
FCC-15 Informationen für Nutzer 
Diese Ausrüstung wurde getestet und bewegt sich innerhalb der Grenzwerte für Class A-Digitalgeräte 
gemäß Artikel 15 der FCC-Regeln. Diese Grenzwerte wurden festgelegt, um angemessenen Schutz gegen 
schädliche Einflüsse sicherzustellen wenn die Geräte in einer kommerziellen Umgebung betrieben 
werden. Diese Geräte produzieren, konsumieren und strahlen möglicherweise Energie im 
Radiofrequenzbereich ab, die schädliche Auswirkungen auf den Funkverkehr haben kann, falls sie nicht 
gemäß dem Benutzerhandbuch (Installation and Operation Manual) installiert wurden. Es ist 
wahrscheinlich, daβ der Betrieb dieser Geräte in einem Wohngebiet zu Störungen führt, die der 
Betreiber auf eigene Kosten zu beseitigen hat. 
Kanadische Emissionsbestimmungen 
Dieses digitale Gerät der Klasse B erfüllt alle Vorgaben der Kanadischen Regulierungen für Geräte, die 
Störeffekte haben können (Canadian Interference-Causing Equipment Regulation). 
Sicherheit und Entsorgung (Deutsch) 
EN 55032 (CISPR 32) Warnung 
 
Achtung 
Das vorliegende Gerät fällt  unter die Funkstörgrenzwertklasse A. In 
Wohngebieten können beim Betrieb dieses Gerätes Rundfunkströrungen 
auftreten, für deren Behebung der Benutzer verantwortlich ist. 
Entsorgung des Produktes 
 
Um die Wiedernutzung, die Wiederverwertung oder andere Formen der 
Wiederaufbereitung von stillgelegten Geräten zum Schutz der Umwelt zu 
gewährleisten, ist der Besitzer des RAD-Produktes verpflichtet, die 
Entsorgung als unsortierter Abfall am Ende des Lebenszyclus des Produktes 
zu unterlassen. Wenn das Gerät ausser Betrieb genommen wird, hat der 
Kunde dieses Gerät einer umweltverträglichen Wiederverwendung, 
Wiederverwertung oder Entsorgung zuzuführen. 
 

## EU Declarations of Conformity  *(p.30)*

EU Declarations of Conformity 
ETX-2i Declaration of Conformity 
ETX-2i-B Declaration of Conformity 
ETX-2i-10-G Declaration of Conformity 
ETX-2i-10G-B Declaration of Conformity 
ETX-2i-100G Declaration of Conformity 
 

## Environmental Compliance Statement  *(p.31)*

Environmental Compliance Statement 
Environmental Compliance Statement 
 
 
 
Environmental Compliance Statement 
 
 
 