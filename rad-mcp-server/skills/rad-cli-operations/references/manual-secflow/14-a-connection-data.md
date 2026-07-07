# A Connection Data

*Manual `SecFlow-1p_6.4_Mn_05-26_GA.pdf`, pages 772–775.*


## A.1 Ethernet Connector  *(p.772)*

Connection Data 
A.1 Ethernet Connector
The Ethernet electrical interfaces terminate in 8-pin RJ-45 connectors, of type 10/100BaseT or 
10/100/1000BaseT, wired in accordance with the table below. The connector supports both MDI and 
MDIX modes. 
10/100/1000BaseT Connector Pinout 
Pin 
MDI 
MDIX 
1 
A+ 
B+ 
2 
A- 
B- 
3 
B+ 
A+ 
4 
C+ 
D+ 
5 
C- 
D- 
6 
B- 
A- 
7 
D+ 
C+ 

## A.2 Serial Port  *(p.773)*

Pin  
MDI 
MDIX 
8 
D- 
C- 
 
A.2 Serial Port 
The SecFlow-1p UART serial ports are terminated with RJ-45 connectors. SecFlow-1p acts as a DCE 
communication device. 
Serial hardware protocols RS-232 and RS-485 are defined according to the ordering options. 
Refer to the table below for the RJ-45 connector pinout. 
Serial Port Pin Assignment 
RJ45 Connector Pin 
RS232 DCE Signal as per EIA-561  
1 
- 
2 
-  
3 
RTS 
4 
GND 
5 
RxD 
6 
TxD 
7 
CTS 
8 
- 
 
RAD recommends using the RS-232 adapter cable CBL-RJ45/D9/F/6FT to connect to user serial 
equipment terminated with a DB9 male connector. 
 
CBL-RJ45/D9/F/6FT Cable 
The cable pinout is shown in the table below. 
CBL-RJ45/D9/F/6FT Cable Pinout for Serial Port 
RJ45 DCE Side 
Direction 
DB-9 DTE Side 
Signal 
Pin 
Pin 
Signal 
-
1
-
6
- 
- 
2 
-
1
- 
RTS 
3 

4
RTS 
GND 
4 
-
5
GND 
RxD 
5 

2
RxD 
TxD 
6 

3
TxD 
CTS 
7 

8
CTS 
-
8
-
7
- 
RS-485 user equipment can be connected using RAD’s CBL-SF-RJ45-RS485 shielded cable. 
CBL-SF-RJ45-RS485
DRAIN WIRE
CBL-SF-RJ45-RS485 
CBL-SF-RJ45-RS485 Cable Pinout 
RJ45 
Color 
Open 2W 
1 
 
 
2 
 
 
3 
white/orange 
+  Tx/Rx 
4 
blue 
GND 
5 
 
 
6 
orange 
- Tx/Rx 
7 
 
 
 
 