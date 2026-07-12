# A Connection Data

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 1186–1195.*


## A.1 CONTROL DCE Connectors  *(p.1186)*

Connection Data 
A.1 CONTROL DCE Connectors
Megaplex-4100 Connector 
The Megaplex-4100 CONTROL DCE connector is a 9-pin D-type female connector with RS-232 
asynchronous DCE interface, intended for direct connection to a supervision terminal. The connector is 
wired as follows. 
Megaplex-4100 CONTROL DCE Connector Wiring 
Pin 
Function 
Direction 
1 
Data Carrier Detect (DCD) 
From Megaplex-4 
2 
Receive Data (RD) 
From Megaplex-4 
3 
Transmit Data (TD) 
To Megaplex-4 
4 
Data Terminal Ready (DTR) 
To Megaplex-4 
5 
Signal Ground (SIG) 
Common reference and DC power supply ground 
6 
Data Set Ready (DSR) 
From Megaplex-4 
7 
Request to Send (RTS) 
To Megaplex-4 
8 
Clear to Send (CTS) 
From Megaplex-4 
9 
Ring Indicator (RI) 
To Megaplex-4 
Megaplex-4104 Connector 
The Megaplex-4104 CONTROL DCE port has a mini USB connector with RS-232 asynchronous DCE 
interface, intended for direct connection to a supervision terminal. The connector is wired as follows. 
A. Connection Data 
Megaplex-4104 CONTROL DCE Connector Wiring 
Pin 
Designation 
Function 
Direction 
1 
– 
CAP to GND 
– 
2 
TX 
Transmit 
Output 
3 
RX 
Receive 
Input 
4 
DSR  
 RS-232 Enable 
Input 
5 
GND 
Ground 
– 
Control Cables 
Straight Control Cable for Megaplex-4100 
For Megaplex-4100, RAD supplies a special control cable CBL-DB9F-DB9M-STR, for connection of the DB-
9 CONTROL DCE connector to the supervision terminal. This cable is wired as follows.  
To Terminal
Modem Side
TD
RTS
CTS
DSR
DCD
RI
DTR
GND
RD
3
2
7
8
6
1
9
4
5
3
2
7
8
6
1
9
4
5
9-Pin
Connector
9-Pin
Connector
To 
CONTROL DCE
Connector
CL Side
 
9-Pin Straight Cable Wiring - Connection to CONTROL DCE Connector  
A. Connection Data 
Straight Control Cable for Megaplex-4104 
For Megaplex-4104, RAD supplies a special control cable, CBL-MUSB-DB9F, for connection of the mini-
USB connector to the supervision terminal. This cable is wired as follows.  
To Terminal
Terminal Side
TD
GND
RD
2
3
2
3
9-Pin
Connector
Mini-USB
Connector
To 
CONTROL DCE
Connector
CL Side
TD
RD
4, 5
GND
5
 
9-Pin Straight Cable Wiring - Connection to CONTROL DCE Connector  
Additional Control Cables 
The connections of the Megaplex-4100 and Megaplex-4104 CONTROL DCE ports to a supervision 
terminal with 9-pin connector are made by means of the above CBL-DB9F-DB9M-STR and CBL-MUSB-
DB9F cables, respectively. 
If additional connection options are needed, you can manufacture your own cables according to the 
drawings below:  
• 
Connection to a supervision terminal with 25-pin connector: by means of a cable wired in 
accordance with CBL-DB9F-DB9M-STR wiring.  
• 
Connection to a modem with 25-pin connector (for communication with remote supervision 
terminal): by means of a cable wired in accordance with CBL-DB9F-DB9M-STR wiring. 
• 
Connection to a modem with 9-pin connector (for communication with remote supervision 
terminal): by means of a crossed cable wired in accordance with CBL-MUSB-DB9F wiring.  
• 
For Megaplex-4104, use these cables in conjunction with CBL-MUSB-DB9F. 
A. Connection Data 
To Terminal
To
CONTROL DCE
Connector
CL Side
Terminal Side
TD
RTS
CTS
DSR
DCD
RI
DTR
GND
RD
3
2
7
8
6
1
9
4
5
2
3
4
5
6
8
22
20
7
25 Pin
Connector
9 Pin
Connector
 
25-Pin Terminal Cable Wiring - Connection to CONTROL DCE Connector 
To Modem
Modem Side
TD
RTS
CTS
DSR
DCD
RI
DTR
GND
RD
3
2
7
8
6
1
9
4
5
2
3
8
7
4
1
9
6
5
9-Pin
Connector
9-Pin
Connector
To
CONTROL DCE
Connector
CL Side
 
9-Pin Crossed Cable Wiring - Connection to CONTROL DCE Connector  

## A.2 CONTROL ETH Connector  *(p.1190)*

A. Connection Data 
A.2 CONTROL ETH Connector 
Connector Data 
Each Megaplex-4 CONTROL ETH port has a 10/100BASE-TX Ethernet station interface terminated in an 
RJ-45 connector. The port supports the MDI/MDIX crossover function, and therefore it can be connected 
by any type of cable (straight or crossed) to any type of 10/100BASE-TX Ethernet port. The port also 
corrects for polarity reversal in the 10BASE-T mode. 
Connector pin functions for the MDI state are listed in the following table. In the MDIX state, the 
receive and transmit pairs are interchanged. 
CONTROL ETH Interface Connector, Pin Functions  
Pin 
Designation 
Function 
1 
TxD+ 
Transmit Data output, + wire 
2 
TxD– 
Transmit Data output, – wire 
3 
RxD+ 
Receive Data input, + wire  
4, 5 
– 
Not connected 
6 
RxD– 
Receive Data input, – wire 
7, 8 
– 
Not connected 
Connection Data 
Use a standard station cable to connect the CONTROL ETH connector to any type of 10/100BASE-TX 
Ethernet port. 

## A.3 ALARM Connectors  *(p.1191)*

A. Connection Data 
A.3 ALARM Connectors 
Connector Data 
The ALARM connector provides connections to the following functions:  
• 
Major and minor alarm relay contacts 
• 
+5V auxiliary voltage output (through 330 Ω series resistor)  
• 
External alarm sense input, accepts RS-232 levels. Can be connected to the +5V auxiliary output 
by external dry contacts.  
ALARM connectors are different for different chassis (CL modules): 
• 
Megaplex-4100 has a 9-pin D-type female connector  
• 
Megaplex-4104 has a 9-pin flat connector. 
Connector pin functions are listed in the following table for Megaplex-4100. For Megaplex-4104 pinout, 
see the CBL-MP-4104/AR/OPEN/2M Cable drawing.   
Caution 
To prevent damage to alarm relay contacts, it is necessary to limit, by 
external means, the maximum current that may flow through the contacts 
(maximum allowed current through closed contacts is 1 A; load switching 
capacity is 60 W). The maximum voltage across the open contacts must not 
exceed 60 VDC/30 VAC.  
Megaplex-4100 ALARM Connector, Pin Functions 
Pin 
Function  
1 
Major alarm relay – normally-open (NO) contact 
2 
Major alarm relay – normally-closed (NC) contact 
3 
Ground 
4 
Minor alarm relay – normally-open (NO) contact 
5 
Minor alarm relay – normally- closed (NC) contact 
6 
Major alarm relay – center contact 
7 
External alarm input 
8 
+5V auxiliary output (through 330 Ω series resistor) 
A. Connection Data 
9 
Minor alarm relay – center contact 
CBL-MP-4104/AR/OPEN/2M 
The CBL-MP-4104/AR/OPEN/2M alarm relay cable serves for connecting the 9-pin Molex connector to 
the user alarm equipment.  It includes one female Molex 9-pin connector and one open-ended 
connector. The cable is 2m (6.5 ft) long. The figure below shows the cable, the connector pinout and the 
diagram of dry contacts. The cable is supplied by RAD. 
 
J1, 9 PIN 
(1 x 9)
Brown
Black
Gray
Purple
Blue
Green
Yellow
Orange
Red
9
8
7
6
5
4
3
2
1
Molex 
Connector Pin
Major Relay - Normally closed (NC)
Major Relay - Central Contact
Major Relay - Normally open (NO)
Minor Relay - Normally closed (NC)
Minor Relay - Central Contact
Minor Relay - Normally open (NO)
+5V auxiliary output
External alarm input
  
CBL-MP-4104/AR/OPEN/2M Cable 
 CL CLOCK Connector 
Connector Data 
The CLOCK interface located on CL modules has one RJ-45 eight-pin connector. The following table lists 
the connector pin functions. 
CL CLOCK Connector, Pin Functions 
Pin 
Direction 
Function 
1 
Input 
Clock In (ring)  
2 
Input 
Clock In (tip)  
3 
↔ 
Signal Ground (connection controlled by internal jumper) 
4 
Output 
Clock Out (ring)  
5 
Output 
Clock Out (tip)  
A. Connection Data 
6 
↔ 
Frame Ground (connection controlled by internal jumper) 
7 
– 
Not connected  
8 
– 
Not connected  
Connection Cable for Unbalanced Interface, CBL-RJ45/2BNC/E1/X 
To connect the CL CLOCK connector to equipment with unbalanced interface, it is necessary to convert 
the RJ-45 connector to the standard pair of BNC female connectors used for unbalanced interfaces. 
For this purpose, RAD offers a 15-cm long adapter cable, CBL-RJ45/2BNC/E1/X, which has one RJ-45 plug 
for connection to CL CLOCK connector and two BNC female connectors at the other end. Cable wiring is 
given in the following figure. 
RJ-45
BNC
Female
Clock Input
(Green)
Clock Output
(Red)
1
2
3
4
5
6
7
8
CLOCK IN Ring
CLOCK IN Tip
NC
CLOCK OUT Ring
CLOCK OUT Tip
NC
Cable Sense (option)
GND
Output
(Red BNC)
Input
(Green BNC)
...
...
 
Unbalanced CLOCK Interface Adapter Cable, CBL-RJ45/2BNC/E1/X, Wiring Diagram 
Connection Cable for Balanced Interface  
The cable used for connecting the CL CLOCK connector to equipment with balanced interface should 
include only two twisted pairs, one for the clock output and the other for the clock input.  
The cable end intended for connection to the CL must be terminated in an RJ-45 plug. Make sure that 
pin 7 in the RJ-45 plug is not connected. 

## A.4 Power Connectors  *(p.1194)*

A. Connection Data 
A.4 Power Connectors 
AC PS Module Connections  
The AC-powered PS modules have one standard IEC three-pin socket for the connection of the AC 
power.  
In addition, the AC-powered PS modules include a three-pin connector, designated VDC-IN, for the 
connection of external phantom feed and ring voltages. Connector wiring is listed in the table below. 
VDC-IN Connector on AC-Powered Modules, Pin Functions 
Pin 
Function 
 
1 
Common reference (0V ground), BGND  
2 
+72 VDC ring and feed voltage input 
3 
-48 VDC ring and feed voltage input 
DC PS Module Connections  
The DC-powered PS modules have a single three-pin VDC-IN connector, for the connection of the supply 
voltage (48 VDC), as well as a +72 VDC input for ring and phantom feed purposes.  
Connector wiring is listed in the table below, together with a view of the connector itself. The nominal 
supply voltage appears in the table under the connector. 
VDC IN Connector on DC-Powered Module, Pin Functions 
Pin 
Function 
48 VDC Module 
1 
Common reference (0V ground), BGND 
 
2 
+72 VDC ring and feed voltage input 
3 
-24 or -48 VDC supply voltage input 
 
RTN
+72
-48
72V
48V
-
  +      -
  +      
A. Connection Data 
Note 
RAD supplies mating connectors for the DC power connectors. For information 
on preparing cables using the supplied connectors, refer to the DC Power 
Supply Connection Supplement.  
Ground Connection 
All PS modules are equipped with a grounding screw on the module panel for connecting the protective 
ground. 
 
 