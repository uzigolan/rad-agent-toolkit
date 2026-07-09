# Installation and Operation – A Connection Data

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 295–300.*


## A.1 Alarm Relay Connector  *(p.295)*


## A.2 Ethernet Connector  *(p.295)*

A 
Connection Data 
A.1 Alarm Relay Connector 
The alarm relay dry contact interface terminates in a 9-pin Molex flat female connector. 
The following table lists the alarm relay pin assignments in ETX-2i, ETX-2i-B, ETX-2i-10G, and  
ETX-2i-100G/4Q. 
Pin 
Function 
1 
NC 
2 
Major alarm relay – normally-open (NO) contact  
3 
Major alarm relay – center contact 
4 
Major alarm relay – normally-closed (NC) contact 
5 
+12V auxiliary output (through 340Ω resistor) 
6 
RS-232 input 1 
7 
RS-232 input 2 
8 
RS-232 input 3 
9 
Ground 
A.2 Ethernet Connector 
The Ethernet electrical interfaces terminate in 8-pin RJ-45 connectors, of type 10/100BASE-T or 
10/100/1000BASE-T, wired in accordance with the table below. The connector supports both MDI and 
MDIX modes. 

## A.3 E1/T1 Connector  *(p.296)*

ETX-2i 
A. Connection Data 
10/100/1000BASE-T Connector Pinout 
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
8 
D- 
C- 
A.3 E1/T1 Connector 
Note 
This section is relevant for ETX-2i ordered with a four or eight-port E1/T1 
module or with 64 built-in E1 ports.  
The E1/T1 connectors are wired as follows, according to the device type: 
• 
ETX-2i with Ethernet Uplink E1/T1 module having four or eight E1/T1 ports – The E1/T1 ports 
terminate in four RJ-45 connectors. In module with four E1/T1 ports, each connector provides 
one port; in module with eight E1/T1 ports, each connector provides two ports. The tables 
below list the pin assignments for four and eight E1/T1 ports, respectively. In the case of eight 
E1/T1 ports, you can use RAD cable CBL-E1-SPLT to connect ETX-2i to the E1/T1 equipment. 
• 
ETX-2i-64E1 – A single E1 terminates with a single RJ-45 connector.  
E1/T1 Connector Pinout – One E1/T1 Port per Connector (for ETX-2i with 4-port E1/T1 module, ETX-2i-64E1)  
PIN 
Function 
Direction 
1 
RX Ring 
Input 
2 
RX Tip 
Input 
3 
NC 
NC 
4 
TX Ring 
Output 

## A.4 CONTROL Connector  *(p.297)*

ETX-2i 
A. Connection Data 
PIN 
Function 
Direction 
5 
TX Tip 
Output 
6 
NC 
NC 
7 
NC 
NC 
8 
NC 
NC 
E1/T1 Connector Pinout – Two E1/T1 Ports per Connector (ETX-2i with 8-port E1/T1 module) 
 
PIN 
Channels 1–4 
Channels 5–8 
Function 
Direction 
Function 
Direction 
1 
RX Ring 
Input 
NC 
NC 
2 
RX Tip 
Input 
NC 
NC 
3 
NC 
NC 
TX Ring 
Output 
4 
TX Ring 
Output 
NC 
NC 
5 
TX Tip 
Output 
NC 
NC 
6 
NC 
NC 
TX Tip 
Output 
7 
NC 
NC 
RX Ring 
Input 
8 
NC 
NC 
RX Tip 
Input 
 
Note 
Do not connect wires to the NC pins.  
A.4 CONTROL Connector 
The CONTROL connector is a Mini USB (ETX-2i, ETX-2i-B, ETX-2i-10G, ETX-2i-10G-B/4SFPP), Micro USB 
(ETX-2i-10G-B/8SFPP, ETX-2i-100G/4QSFP)), or (ETX-2i-10G-B/8SFPP/ODU). The following table lists the 
CONTROL connector pin assignments.  
Pin  
Name 
Function 
ETX-2i-10G-B/8SFPP/ODU with an 8-pin RJ-45 connector 
ETX-2i devices that use a Mini USB or Micro USB connector 
1 
N.A. 
- 

## A.5 EXT CLK Connector  *(p.298)*


## A.6 MNG Connector  *(p.298)*

ETX-2i 
A. Connection Data 
Pin  
Name 
Function 
2 
TXD 
Transmit data  
3 
RXD 
Receive data 
4 
N.A. 
- 
5 
GND 
Ground 
A.5 EXT CLK Connector 
Note 
This section is relevant only if a timing option was ordered.  
The station clock port terminates in an 8-pin RJ-45 connector, wired in accordance with the following 
table.  
Pin 
Direction 
Function 
1,2 
Input 
T3 (Input) 
3 
– 
Not connected  
4,5 
Output 
T4 (Output) 
6, 7, 8 
– 
Not connected  
A.6 MNG Connector 
The ETX-2i Ethernet management port terminates in an RJ-45, 8-pin connector that supports MDI and 
MDIX modes. The following table lists the pin assignments. 
Pin 
Designation 
Function 
1 
RxD+ 
Receive Data output, + wire 
2 
RxD– 
Receive Data output, – wire 
3 
TxD+ 
Transmit Data input, + wire  
4,5 
– 
Not connected 
6 
TxD- 
Transmit Data input, – wire  

## A.7 SHDSL Connector  *(p.299)*


## A.8 VDSL Connector  *(p.299)*

ETX-2i 
A. Connection Data 
Pin 
Designation 
Function 
7,8 
– 
Not connected 
A.7 SHDSL Connector 
Note 
This section is relevant for devices with SHDSL module. One 8-pin RJ-45 
connector is used for the 4-wire ordering option, and two 8-pin RJ-45 
connectors are used for the 8-wire ordering option. Each pin is wired as in the 
table below.  
The SHDSL electrical interface is an 8-pin RJ-45 connector, wired in accordance with the following table.  
Pin  
Function 
1 
NC 
2 
NC 
3 
Loop 2 
4 
Loop 1 
5 
Loop 1 
6 
Loop 2 
7 
NC 
8 
NC 
 
Note 
Do not connect wires to the NC pins.  
A.8 VDSL Connector 
Note 
This section is relevant only for ETX-2i with a VDSL module.  
The VDSL AIO electrical interface is made up of two 8-pin RJ-45 connectors – one connector for Loop 1 
and Loop 2; the other for Loop 3 and Loop 4. Each connector is wired in accordance with the following 
table.  

## A.9 ToD/1PPS Connector  *(p.300)*

ETX-2i 
A. Connection Data 
Pin  
Function 
1 
NC 
2 
NC 
3 
Loop 2 / Loop 4 
4 
Loop 1 / Loop 3 
5 
Loop 1 / Loop 3 
6 
Loop 2 / Loop 4 
7 
NC 
8 
NC 
 
Note 
Do not connect wires to the NC pins.  
A.9 ToD/1PPS Connector 
Note 
This section is relevant for ETX-2i if a PTP option was ordered.  
The ToD/1PPS interface terminates in an RS-422 (half duplex) 8-pin RJ-45 connector. The following table 
lists the pin assignments.  
Pin 
Function 
1 
Option, NC 
2 
Option, NC 
3 
Tx/Rx 1PPS -   
4 
GND 
5 
GND 
6 
Tx/Rx 1PPS +   
7 
Tx/Rx TOD -    
8 
Tx/Rx TOD +   
 