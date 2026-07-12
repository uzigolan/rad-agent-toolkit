# 5 Cards and Ports – 5.9 E1 Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 300–322.*


## Applicability and Scaling  *(p.300)*

5. Cards and Ports 
5.9 E1 Ports  
Applicability and Scaling 
The following table shows the number of E1 and E1-i ports and their features supported by each 
Megaplex-4 module. The hierarchical position of e1 and e1-i ports is slot:port for all the modules. The 
digits in brackets (1 to 4) denote restrictions or other special remarks regarding implementation of this 
feature in specific modules.  
Features Supported by Megaplex-4 External E1 Ports 
Feature/ 
Command 
VS-16E1T1-EoP 
VS-16E1T1-PW 
VS-6/E1T1 
Number of ports 
16 
16 
8 
name 
√ 
√ 
√ 
shutdown 
√ 
√ 
√ 
inband-management  
√(8) 
√(1) 
√(1) 
interface-type 
√ 
√ 
√ 
line-type 
√(9) 
√ 
√ 
out-of-service (voice, 
data) 
 
√ 
√  
(2)(1) 
√ 
 (2)(1) 
rx-sensitivity 
√ 
√ 
√ 
idle-code 
√ 
√ (1) 
√ (1) 
vc-profile  
√ (7) 
√ (7) 
√ (7) 
tx-clock-source 
– 
√ (10) 
√ (10) 
Features Supported by Megaplex-4 Internal E1 Ports  
Feature/ 
Command 
CL.2    
VS-16E1T1-EoP 
Number of ports 
63 
16 
name 
√ 
√ 
shutdown 
√ 
√ 
inband-management  
√(1) 
– 

## Standards Compliance  *(p.301)*


## Functional Description  *(p.301)*

5. Cards and Ports 
Feature/ 
Command 
CL.2    
VS-16E1T1-EoP 
line-type 
√ 
√(9) 
out-of-service (voice, data) 
 
√ (2)(1) 
– 
idle-code 
√ (1) 
– 
vc-profile  
√  
√ 
 
1 - N/A for Unframed 
2 - OOS voice and signaling N/A for line-type=g732n/g732n-crc  
3 – Unframed not supported 
4 - N/A for line-type=g732n/g732n-crc 
5 – N/A 
6 - N/A for line-type=g732n-crc/g732n-crc 
7 - Applicable if line type is Unframed and the link is directly mapped to SDH-SONET 
vc12-vt2 
8 –N/A for E1 bound to VCG 
9 –When E1 is bound to VCG, line-type=g732n-crc only 
10 – Applicable when E1 is cross connected directly to PW 
Standards Compliance 
The E1 link interfaces meet the applicable requirements of ITU-T Rec. G.703, G.704, G.706, G.732, and 
G.823.  
Functional Description 
External E1 Link Interfaces are available in VS-6/E1T1, VS-16E1T1-PW, and VS-16E1T1-EoP I/O modules. 
Internal E1 ports are available in CL.2 and VS-16E1T1-EoP I/O modules.  
The parameters configurable for each module can be chosen from the table above. E1 port parameters 
are described in the following sections.  
  
5. Cards and Ports 
Framing  
The external and internal E1 ports can be independently configured in accordance with the desired ITU-T 
framing mode and signaling formats: 
• 
Basic G.704 framing (identified as G.732N) for applications that require CCS.  
• 
G.704 framing with timeslot 16 multiframe (identified as G.732S and referred to as G.704 
multiframe mode) for applications that require CAS. 
• 
Unframed mode for transparent transfer of 2.048 Mbps streams, including streams with 
proprietary framing. Also enables transferring framed E1 streams without terminating timeslot 
0, and timeslot 16. 
The framer automatically adds the appropriate overhead. Unused timeslots are filled with a 
user-specified idle code. The user can also select specific timeslots to be transferred (DS0 cross-
connect). 
The framing mode can be independently selected for each external or internal E1 port of the I/O 
module. It is configured by means of the line-type parameter. 
Interface Type 
The external ports support two line interfaces: 
• 
120Ω balanced line interface. The nominal balanced interface transmit level is ±3V. 
• 
75Ω unbalanced interface. The nominal unbalanced interface transmit level is ±2.37V. 
Only one of these interfaces can be active at any time. The active interface can be selected by the user, 
separately for each port.  
Receive Signal Attenuation (VS-6/E1T1, VS-16E1T1-PW and VS-16E1T1-EoP Modules) 
The E1 line interfaces have integral LTUs, which enable long-haul operation with line attenuation of up 
to 43 dB. The line interface can also emulate a DSU interface, for short-haul applications: in this case, 
the maximum line attenuation is 12 dB. The receive signal attenuation level is configured by means of 
the rx-sensitivity parameter. In addition, this parameter can be also configured to monitor E1 services, 
with line attenuation of up to12 dB. 
E1 Payload Processing  
Megaplex-4 E1 modules support two main types of payload per timeslot: 
5. Cards and Ports 
• 
Data timeslots: timeslots which are transparently transferred from port to port. In general, it is 
assumed that no CAS is associated with data timeslots.  
Timeslots assigned to HDLC ports are always processed as data timeslots. 
• 
Management timeslots: with framed signals, one timeslot per port can be assigned to carry 
management traffic. Such timeslots are always directed to the CL management subsystem, for 
processing. 
The flow of payload carried by voice timeslots is normally bidirectional (full duplex connection). 
However, it is also possible to define unidirectional flows, called unidirectional broadcasts, from one 
source (a timeslot of a source port) to multiple destinations (each destination being a selected timeslot 
of another port).  
In case of data timeslots, the flow of payload is normally unidirectional. If the application requires 
bidirectional flows, cross-connect must be configured symmetrically for both directions.  
Handling E1 Alarm Conditions  
External and internal E1 ports using framed mode support two types of indications in the individual 
timeslots:  
• 
Idle Timeslot Indication. A special code can be transmitted in empty timeslots (timeslots which 
do not carry payload).  
• 
OOS Indications. The OOS code is inserted in individual timeslots to signal the equipment routed 
to one of the E1 ports of the module that the link connected to the external port is 
out-of-service (e.g., because of loss of frame synchronization).  
For ports using a G.704 timeslot 16 multiframe mode, the CAS information can also be replaced 
by a selectable OOS indication.  
The idle code and OOS indications can be independently configured for each port. Moreover, separate 
OOS codes can be transmitted in the timeslots, in accordance with the type of payload carried by each 
timeslot (voice or data).  
OOS Signaling 
If the communication between modules located in different Megaplex units fails, e.g., because loss of 
main link synchronization, etc., it is necessary to control the state of the signaling information at the two 
ends of the link. This activity, called out-of-service (OOS) signaling, is performed by the E1 interfaces and 
can be selected in accordance with the specific application requirements, on a per-link basis.  
The OOS signaling options supported by the E1 module ports are as follows: 

## Factory Defaults  *(p.304)*

5. Cards and Ports 
• 
Signaling forced to idle state for the duration of the out-of-service condition (force-idle). This 
option is suitable for use with all the VC module types. 
• 
Signaling forced to busy state for the duration of the out-of-service condition (force-busy). This 
option is suitable for use with E&M and FXO modules, but not with FXS modules. 
• 
Signaling forced to idle state for 2.5 seconds, and then changed to busy state for the remaining 
duration of the out-of-service condition (idle-busy). This option is suitable for use with E&M and 
FXO modules, but not with FXS modules. 
• 
Signaling forced to busy state for 2.5 seconds, and then changed to idle state for the remaining 
duration of the out-of-service condition (busy-idle). This option is suitable for use with all the VC 
module types. 
Inband Management 
E1 and internal E1 ports of Megaplex-4 using a framed mode feature inband management access to the 
end user’s equipment provided by configuring a dedicated management timeslot.  
The transfer of inband management traffic is controlled by using synchronous PPP over HDLC 
encapsulation or Frame Relay encapsulation (under DLCI 100) in accordance with RFC 2427. 
RIP2 routing tables are transmitted as follows: 
• 
Proprietary RIP – Management traffic is routed using RAD proprietary routing protocol 
• 
RIP2 – In addition to the RAD proprietary routing protocol, RIP2 routing is also supported.  
Factory Defaults 
Megaplex-4 is supplied with all e1/e1-i ports disabled. Other parameter defaults are listed in the table 
below. 
Parameter  
Default Value 
line-type 
g732s  
rx-sensitivity  
short-haul  
interface-type  
balanced  
idle-code  
0x7f 
inband-management  
no inband-management (disabled) 
inband-management – routing-protocol  
none  

## Configuring E1 Ports  *(p.305)*

5. Cards and Ports 
Parameter  
Default Value 
out-of-service - voice  
0x00 
out-of-service - data  
0x00 
out-of-service - signaling   
force-idle 
signaling-profile  
no signaling-profile 
vc profile 
tug-structure  
clock-source-bit 
master: SA7  
loopback: SA8 
Configuring E1 Ports  
 To configure the E1 port parameters: 
1. Navigate to configure port e1 <slot>/<port> to select the E1 port to configure.  
The config>port>e1>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below (see Error! Reference source 
not found. for parameters supported in each module).  
Task 
Command  
Comments 
Assigning short 
description to port 
name <string> 
Using no name removes the name 
Administratively enabling 
port 
no shutdown 
Using shutdown disables the port 
Specifying E1 framing 
mode  
line-type {unframed | g732n  
| g732n-crc | g732s | g732s-crc} 
When the E1 port is bound to a VCG port, VS-
16E1T1-EoP supports g732n-crc option only. 
Setting attenuation level 
of the receive signal 
rx-sensitivity {short-haul | long-haul | 
monitor }  
VS E1T1 modules only:  
short-haul – low sensitivity (-12 dB) 
long-haul – high sensitivity (-43 dB) 
monitor – monitor sensitivity (-12 dB) 
Specifying port impedance  interface-type {balanced | unbalanced} 
 
5. Cards and Ports 
Task 
Command  
Comments 
Specifying  the code 
transmitted to fill unused 
timeslots in E1 frames 
idle-code { 00 to FF (hexa) }  
The available selections are [0x01 to 0xFF] 
with the following values that are illegal: 
0x00, 0x08, 0x10, 0x12, 0x21, 0x24, 0x42, 
0x49, 0x84, 0x92 
Enabling inband 
management and setting 
its parameters 
inband-management <timeslot> protocol 
{ppp | fr} [routing-protocol {none | prop-
rip | rip2} ] 
 
ppp – synchronous PPP over HDLC 
encapsulation  
fr –Frame Relay encapsulation (under DLCI 
100) in accordance with RFC 2427 
See also Configuring Inband Management in 
Chapter 8 for important considerations on 
selecting routing protocol.  
Not available for VS-16E1T1-EoP modules 
when this E1 port is bound to a VCG port 
Using no inband management  <timeslot> 
disables inband management through this 
timeslot 
Transmitting an 
out-of-service signal (OOS)   
out-of-service [voice <00 to FF (hexa)>] [ 
data <00 to FF (hexa)>] [signaling {force-idle 
| force-busy | idle-busy | busy-idle}]   
The hexadecimal number is in the range of 0 
to FF (two digits)  
The selected out-of-service data code is also 
sent during out-of-service periods instead of 
the external data stream when the unframed 
mode is used  
out-of-service voice selection is relevant only 
when the g732s or g732s-crc modes are 
selected  
Configuring collection of 
performance management 
statistics for this port, 
which are presented via 
the RADview Performance 
Management portal 
 
pm-collection interval <seconds> 
You can enable PM statistics collection for all 
E1 ports rather than enabling it for individual 
ports. In addition to enabling PM statistics 
collection for the ports, it must be enabled 
for the device. Refer to the Performance 
Management section in the Monitoring and 
Diagnostics chapter for details. 
5. Cards and Ports 
Task 
Command  
Comments 
Selecting the timing 
reference source used by 
the port for the 
transmit-to-network 
direction 
 
tx-clock-source loopback  
tx-clock-source domain <number>  
tx-clock-source through-timing 
loopback – Clock received from the E1/T1 
port 
domain – Clock provided by system clock 
domain 
through-timing – Clock received from 
VC12/VT1.5 or PW (according to the 
transport network) 
This field is valid for VS-16E1T1-PW and 
VS-6/E1T1 modules only. 
Assigning VC profile to the 
port 
vc profile <profile name> 
 
For creating VC profiles, see VC Profiles. 
Using no vc removes the profile  
 To configure the internal E1 port parameters: 
1. Navigate to configure port e1-i <slot>/<port> to select the internal E1 port to configure. 
The config>port>e1-i>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
Assigning short 
description to the port 
name <string> 
Using no name removes the name 
Administratively enabling 
the port 
no shutdown 
Using shutdown disables the port 
Specifying E1 framing 
mode  
line-type { unframed | g732n | g732n-crc | 
g732s | g732s-crc } 
When the internal E1 port is bound to a VCG 
port, VS-16E1T1-EoP supports g732n-crc 
option only.  
Specifying  the code 
transmitted to fill unused 
timeslots in E1 frames 
idle-code <00 to FF (hexa)>  
 
The available selections are [0x01 to 0xFF] 
with the following values that are illegal: 
0x00, 0x08, 0x10, 0x12, 0x21, 0x24, 0x42, 
0x49, 0x84, 0x92 

## Configuration Errors  *(p.308)*

5. Cards and Ports 
Task 
Command  
Comments 
Enabling inband 
management and setting 
its parameters 
inband-management <timeslot> protocol 
{ppp | fr} [routing-protocol {none | prop-
rip | rip2} ] 
 
ppp – synchronous PPP over HDLC 
encapsulation  
fr –Frame Relay encapsulation (under DLCI 
100) in accordance with RFC 2427 
See also Configuring Inband Management in 
Chapter 8 for important considerations on 
selecting the routing protocol. 
Using no inband management  <timeslot> 
disables inband management through this 
timeslot 
Transmitting an 
out-of-service signal (OOS)   
out-of-service [voice <00 to FF (hexa)>] [ 
data <00 to FF (hexa)>] [signaling {force-idle 
| force-busy | idle-busy | busy-idle}]   
The hexadecimal number is in the range of 0 
to FF (two digits)  
The selected out-of-service data code is also 
sent during out-of-service periods instead of 
the external data stream when the unframed 
mode is used  
out-of-service voice selection is relevant only 
when the g732s or g732s-crc modes are 
selected  
Configuring collection of 
performance management 
statistics for this port, 
which are presented via 
the RADview Performance 
Management portal 
 
pm-collection interval <seconds> 
You can enable PM statistics collection for all 
E1 ports rather than enabling it for individual 
ports. In addition to enabling PM statistics 
collection for the ports, it must be enabled 
for the device. Refer to the Performance 
Management section in the Monitoring and 
Diagnostics chapter for details. 
Assigning VC profile to the 
port 
vc profile <profile name>  
 
For creating VC profiles, see VC Profiles. 
Using no vc removes the profile  
Configuration Errors 
The following table lists messages generated by Megaplex-4 when a configuration error on E1 modules 
is detected.  
Code 
Type 
Syntax 
Meaning 
131 
Warning RESTORATION TIME DOES NOT 
MATCH THE STD 
For E1 links, the restoration time must be in accordance 
with ITU-T recommendations 

## Viewing an E1 Port Status  *(p.309)*

5. Cards and Ports 
Code 
Type 
Syntax 
Meaning 
132 
Error 
FRAME TYPE / PROFILE 
MISMATCH 
One of the following: 
• The selected framing mode does not support signaling 
profiles 
• When the station clock is configured to interface-type= 
e1 with tx-ssm enabled, line-type must be  g732n-crc 
141 
Error 
ROUTING PROTOCOL/ 
MNG TYPE MISMATCH 
The rip2 protocol on an I/O module port can be enabled 
only when the inband management method is configured to 
ppp or fr 
144 
Error 
ILLEGAL IDLE CODE SELECTION 
Code transmitted in idle timeslots is illegal. The available 
selections for E1/E1-i ports are [0x01 to 0xFF] with the 
following values that are illegal: 0x00, 0x08, 0x10, 0x12, 
0x21, 0x24, 0x42, 0x49, 0x84, 0x92 
434 
Error 
PORT LINE TYPE MISMATCH 
 
When the CL module has no SDH/SONET ports, line-type 
must not be configured as g732s or g732s-crc for the 
following modules/ports: 
• VS-E1-PW: ports E1 9..16 or DS1 9..16  
• VS-6-E1:  ports DS1 9..16.  
Error 434 may also appear for other port types – refer to the 
corresponding manual section.  
Viewing an E1 Port Status 
Follow the instructions below for viewing the status of the E1 port 5/1 as an example. 
 To view the E1 port status: 
• 
At the config>port>e1(<slot>/<port>)# prompt, enter show status. 
The status information appears as illustrated below.  
 
config>port>e1(5/1)# show status 
Name                  : 
Administrative Status : Down 
Operation Status      : Up 
Connector Type        : DB44 

## Testing E1 Ports  *(p.310)*

5. Cards and Ports 
Testing E1 Ports  
Megaplex-4 E1 ports feature test and loopback functions at the port and timeslot levels. The available 
loopbacks depend on the port type (E1, E1-i) and  specific module. The following table shows the 
loopbacks supported by E1 and E1-i ports on each Megaplex-4 module. The hierarchical position of e1 
and e1-i ports is slot:port for all the modules. The digits in brackets (1 to 3) denote restrictions or other 
special remarks regarding implementation of this loopback in specific modules.  
Loopbacks Supported by Megaplex-4 E1 and E1-i Ports  
Lopback Type 
VS-16E1T1-EoP 
VS-16E1T1-PW 
VS-6/E1T1  
CL.2   
VS-16E1T1-EoP 
Local Loop 
√ 
√ 
Remote Loop 
√ 
√ 
Loop per TS Local 
√ 
√ 
Loop per TS Remote 
√ 
√ 
Local on remote 
– 
– 
Remote on remote 
– 
– 
Ber Test 
√ 
√ 
 
1 - Loopback on local and remote devices 
2 - Only for local internal e1 ports. 
CL Modules 
The following sections briefly describe each type of loopback on E1-i ports of CL modules. The following 
table shows the paths of the signals when each loopback is activated.  
5. Cards and Ports 
Loopbacks on E1-i ports of CL.2 Modules 
 
Megaplex-4100
DS1
Cross-Connect
Matrix
CL
E1/T1
Mapper
SDH/
SONET
Framer
1
........
E1-i/T1-i 
Framers
2
SDH/SONET Interface 
VC/VT
Matrix
I/O Port
Local loopback on E1-
i port  
 
 
1
......
E1-i/T1-i Framers
2
 
 
 
 
Remote loopback on 
E1-i  port  
 
 
1
......
E1-i/T1-i Framers
2
 
 
 
 
Local loopback on 
timeslots of  
E1-i port  
 
 
1
......
E1-i/T1-i Framers
2
 
 
 
 
5. Cards and Ports 
 
Megaplex-4100
DS1
Cross-Connect
Matrix
CL
E1/T1
Mapper
SDH/
SONET
Framer
1
........
E1-i/T1-i 
Framers
2
SDH/SONET Interface 
VC/VT
Matrix
I/O Port
Remote loopback on 
timeslots of  
E1-i  port  
 
 
1
......
E1-i/T1-i Framers
2
 
 
 
 
Local Loopback on E1-i Port  
The local E1-i port loopback is used to test the intra-Megaplex-4 paths of the signals intended for 
transmission through a selected E1-i port: these paths start at the other Megaplex-4 port(s) connected 
to the tested E1-i port, pass through the DS1 cross-connect matrix in the CL module, and continue up to 
the framer of the E1-i port within the SDH/SONET link interface. Therefore, these paths include all of the 
Megaplex-4 local ports connected to the tested E1-i port, and in the particular the operation of the DS1 
cross-connect matrix circuits that handle the signals directed to the tested E1-i port within the CL 
module. 
As shown in the table above, the local E1-i port loopback is activated within the E1-i framer of a selected 
CL E1-i port.  
Remote Loopback on E1-i Port  
As shown in the table above, the E1-i port remote loopback is activated on the framer serving the port 
within the SDH/SONET link interface.  
5. Cards and Ports 
Local Loopback on E1-i Port Timeslots  
The local loopback on selected timeslots of an E1-i port is used to return the transmit payload carried by 
the selected timeslots through the same timeslots of the receive path. The timeslots looped back remain 
connected to the transmit path of the port, but the corresponding timeslots received from the remote 
end are disconnected. 
This test is recommended for testing the signal paths between the E1-i port and an I/O port of another 
module that uses only a fraction of the available E1-i port bandwidth. 
As shown in the table above, the loopback is activated only on the timeslots specified by the user during 
the activation of the loopback. As a result, there is no disturbance to services provided by means of the 
other timeslots of the same E1-i port, only the flow of payload carried by the specified timeslots is 
disrupted. 
The user can activate the loopback on any individual timeslot, or on several arbitrarily selected 
timeslots. It is not allowed to activate loopbacks on timeslots cross-connected with HDLC ports. 
Remote Loopback on E1-i Port Timeslots  
The remote loopback on selected timeslots of an E1-i port is used to return the receive payload carried 
by the selected timeslots through the same timeslots of the transmit path. The corresponding timeslots 
received from the local equipment are disconnected.  
This test is recommended for testing signal paths from a remote equipment unit, through the selected 
timeslots of the E1-i port, to an I/O port of another module that uses only a fraction of the available port 
bandwidth. 
As shown in the table above, the loopback is activated only on the timeslots specified by the user during 
the activation of the loopback. As a result, there is no disturbance to services provided by means of the 
other timeslots of the same E1-i port: only the flow of payload carried by the specified timeslots is 
disrupted. It is not allowed to activate loopbacks on timeslots assigned to HDLC ports.  
I/O Modules 
The following sections briefly describe each type of loopback on E1 and E1-i ports of I/O modules. The 
table below shows the paths of the signals when each loopback is activated.  
5. Cards and Ports 
  Loopbacks on E1 and E1-i Ports of I/O Modules  
 
 I/O CL 
Local loopback on E1/E1-i port (VS-
16E1T1-EoP modules) 
Port 
Interface
 1 
"   "
DS1
Cross-Connect
Matrix
 
Remote loopback on E1/E1-i port 
(VS-16E1T1-EoP modules) 
 
    Port 
    Interface
DS1
Cross-Connect
Matrix
 
Local loopback on E1/E1-i 
timeslots (VS-16E1T1-EoP 
modules) 
DS1
Cross-Connect
Matrix
1
.....
2
I/O Interface
 
Remote loopback on E1/E1-i 
timeslots (VS-16E1T1-EoP 
modules) 
1
.....
2
DS1
Cross-Connect
Matrix
I/O Interface
 
Local Loopback on E1 Port of I/O Module  
The local port loopback is used to test the path of the signals intended for transmission through a 
selected E1 port: this path starts at the other Megaplex-4 port(s) connected to the selected port, passes 
through the cross-connect matrix in the CL module, and continues up to the port line interface. Within 
5. Cards and Ports 
the tested module, the path includes most of the line interface circuits serving the selected port, and the 
operation of the routing circuits that handle the port signals within the module. 
As shown in the table above when a local loopback is activated, the port transmit signal is returned to 
the input of the same port receive path at a point just before the line interface. The local port must 
receive its own signal, and thus it must be frame-synchronized. In addition, each I/O module connected 
to the corresponding port must also receive its own signal. In general, the result is that these modules 
are synchronized and do not generate alarm indications.  
To provide a keep-alive signal to the transmission equipment serving the link under test while the 
loopback is activated, the port line interface transmits an unframed “all-ones” signal (AIS) to the line. AIS 
reception will cause the remote equipment to lose frame synchronization while the loopback is 
connected. This is normal and does not necessarily indicate a fault. 
Remote Loopback on E1 Port of I/O Module  
The remote port loopback is used to test the line interface circuits of a selected E1 external port. This 
test also checks the transmission plant connecting the equipment connected to the corresponding port. 
As shown in the table above, when a remote loopback is activated on an E1 port, that port returns the 
received signal to the remote unit, via the transmit path. The received signal remains connected as usual 
to the receive path of the corresponding port. To correct transmission distortions, the returned signal is 
regenerated by the corresponding line interface circuits. 
The remote loopback should be activated only after checking that the remote unit operates normally 
with the local port loopback. In this case, the remote unit must receive its own signal, and thus it must 
be frame-synchronized. The effect on the individual modules is mixed, as explained above for the local 
loopback. 
If the local Megaplex-4 unit also operated normally when the local port loopback was activated, then 
while the remote loopback is connected the local unit should receive a valid signal, and thus it must be 
frame-synchronized.  
The remote port loopback should be activated at only one of the units connected in a link, otherwise an 
unstable situation occurs.  
Local Loopback on Timeslots of E1 I/O Module Port 
The local loopback on selected timeslots of an E1 port is used to return the transmit payload carried by 
the selected timeslots through the same timeslots of the receive path. This test is recommended for 
testing the signal paths between an I/O port of another module that uses only a fraction of the available 
port bandwidth, and the E1 port. 
5. Cards and Ports 
As shown in the table above, the loopback is activated within the I/O module routing matrix, and only on 
the timeslots specified by the user during the activation of the loopback. As a result, there is no 
disturbance to services provided by means of the other timeslots of the same port: only the flow of 
payload carried by the specified timeslots is disrupted. 
You can activate the loopback on any individual timeslot, or on several arbitrarily selected timeslots. You 
cannot activate loopbacks on timeslots assigned to HDLC ports. 
This convenience feature is also available for loopback deactivation. The deactivation command can be 
issued to either one of the ports of the protection group (even if it has been activated by a command to 
the other port). 
Remote Loopback on Timeslots of E1 I/O Module Port  
The remote loopback on selected timeslots of an E1 port is used to return the receive payload carried by 
the selected timeslots through the same timeslots of the transmit path. This loopback is recommended 
for testing signal paths from a remote equipment unit, through the selected timeslots of the E1 port, to 
an I/O port of another module that uses only a fraction of the available port bandwidth. 
As shown in the table above, the loopback is activated within the I/O module routing matrix, and only on 
the timeslots specified by the user during the activation of the loopback. As a result, there is no 
disturbance to services provided by means of the other timeslots of the same port. Only the flow of 
payload carried by the specified timeslots is disrupted. 
You cannot activate loopbacks on timeslots assigned to HDLC ports. 
The other features related to loopback activation/deactivation described above for the local loopback 
on timeslots are also applicable to the remote loopback. 
BER Test  
The BER test, activated by the command bert, is used to evaluate data transmission through selected 
timeslots of the link connected to a selected E1 or E1-i port without using external test equipment.  
Data transmission is checked by applying a test sequence generated by an internal test sequence 
generator towards the remote equipment. The timeslots in which the sequence is transmitted, are 
defined by means of the bert command. The test sequence is 2E-15. 
To check that the line is alive or verify the BER detection calibration, the user can also inject single errors 
into the transmitted pattern. 
The BER Test on unframed ports is performed per port, while on framed ports it is performed per 
individual timeslot.  
5. Cards and Ports 
The timeslot on which BERT is performed must be cross-connected. 
The transmitted data is returned by means of a loop, somewhere along the data path, to the test 
sequence evaluator. The evaluator compares the received data, bit by bit, to the original data and 
detects any difference (bit error). The output of the evaluator is sampled during module polling, to 
check whether errors were detected in the interval between consecutive pollings. 
The number of errors is accumulated from the activation of the BER test.  
The test results are displayed on a supervision terminal as a number in the range of 0 (no errors 
detected during the current measurement interval) through 63535. The meaning of the displayed 
parameters is given in the table below. 
The BER test duration is infinite (to stop the test manually, use no bert command).  
  Bert Performance Parameters 
Parameter 
Description 
Status 
Displays the BERT status: Not Active, In Sync or Out of Sync 
Run Time (Sec)  
Displays the total time the test is running in seconds 
Sync Loss (Sec) 
Displays the number of times Sync Loss was detected since BERT 
started to run 
Bert Error Count 
Displays the total number of bit errors detected 
Pattern 
Displays the BERT pattern (always 2e-15)        
ES (Sec)        
Displays the total number of seconds in which errors have been 
detected  
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the Megaplex-4. 
Therefore, when you initiate a loopback, you have the option to limit its duration to an interval in the 
range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-4 before 
this timeout expires. When using inband management, always use the timeout option; otherwise, the 
management communication path may be permanently disconnected. 
The default is infinite duration (without timeout). 
5. Cards and Ports 
Activating Loopbacks and BER Tests  
 To perform a loopback or BER test on the E1 port: 
1. Navigate to configure port e1 <slot>/<port>/<tributary> to select the E1 port to be tested. 
The config>port>e1>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
 To perform a loopback or BER test on the internal E1 port:  
1. Navigate to configure port e1-i <slot>/<port> to select the internal E1 port to be tested. 
The config>port>e1-i>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below.  
Task 
Command 
Comments 
Activating and configuring the 
direction of the loopback (all 
modules) 
loopback {local | remote} [time-slot 
<1..31>] [duration <duration in 
minutes 1..30> ] 
 
• local – local loopback (per port and per 
timeslot) 
• remote – remote loopback (per port and 
per timeslot) 
Stopping the loopback  
no loopback 
 
Activating the BER test and 
configuring its parameters 
bert  [ts <ts number 1..31>] [inject-
error single]  
  
The [ts <ts number in the range from 1  to 
31>] command is used only for framed ports 
and is mandatory for these ports. 
The timeslot on which BERT is performed 
must be cross-connected. 
CL flip stops the BERT session. 
Stopping the BER test  
no bert 
 
Displaying the BER test results 
show bert 
 
A typical display: 
Status         : Not Active 
Bit Error Count: 1            
Pattern        : 2e-15        
Run Time (Sec) : 1            
ES (Sec)       : 1            
Sync Loss (Sec): 1  
Clearing the BER test counters 
clear-bert-counters 
 

## Displaying E1 Port Statistics  *(p.319)*

5. Cards and Ports 
Displaying E1 Port Statistics  
E1 and E1-i ports of Megaplex-4 feature the collection of statistical diagnostics per relevant parts of ITU-
T G.826, thereby allowing the carrier to monitor the transmission performance of the links.  
 To display the E1 port statistics: 
• 
At the prompt config>slot>port>e1(<slot><port>)#, enter show statistics followed by the 
parameters listed below. 
 To display the E1-i port statistics: 
• 
At the prompt config>slot>port>e1-i(<slot><port>)#, enter show statistics followed by the 
parameters listed below.  
Task 
Command 
Comments 
Displaying statistics 
show statistics {total | all | current}  
 
  
• total –total statistics of last 96 
intervals  
• current –current statistics 
• all –all statistics: first current 
statistics, then statistics for all valid 
intervals, and finally total statistics 
Displaying statistics 
for a specific interval 
show statistics interval <interval-num 
1..96> 
 
E1 port statistics are displayed.   
Note 
BES, LOFC and Rx Frames Slip are displayed for framed formats only. 
For example: 
Current statistics: 
 
config>port>e1(1/2)# show statistics current 
Current 
--------------------------------------------------------------- 
Time Elapsed (Sec) : 191 
Valid Intervals    : 2 
 
ES             : 0 
SES            : 0 
UAS            : 0 
 
BES            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
Statistics for interval 67: 
5. Cards and Ports 
 
config>port>e1(3/1)# show statistics interval 67 
Interval Number : 67 
 
Interval 
--------------------------------------------------------------- 
ES             : 16 
SES            : 1 
UAS            : 589 
 
BES            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
Total statistics: 
 
config>port>e1(1/2)# show statistics total 
Total 
--------------------------------------------------------------- 
ES             : 2 
SES            : 0 
UAS            : 0 
 
BES            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
All statistics:  
 
config>port>e1(1/2)# show statistics all 
Current 
--------------------------------------------------------------- 
Time Elapsed (Sec) : 171 
Valid Intervals    : 2 
config>port>e1(1/2)# 
 
ES             : 0 
SES            : 0 
UAS            : 0 
 
BES            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
 
Interval Number : 1 
 
Interval 
--------------------------------------------------------------- 
ES             : 0 
SES            : 0 
UAS            : 0 
 
BES            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
 
Interval Number : 2 
5. Cards and Ports 
 
Interval 
--------------------------------------------------------------- 
ES             : 2 
SES            : 0 
UAS            : 0 
 
BES            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
 
Total 
--------------------------------------------------------------- 
ES             : 2 
SES            : 0 
UAS            : 0 
 
BES            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
The counters are described in the following tables.  
E1 Port Statistics Parameters – Current 15-Minute Interval 
Parameter 
Description 
ES  
Displays the number of errored seconds in the current 15-minute interval. 
An errored second is any second not declared a UAS in which a OOF (Out of Frame) or 
CRC (Cyclic Redundancy Check error) occurred. 
UAS  
Displays the number of unavailable seconds (UAS) in the current interval. 
An unavailable second is one of the following: 
• Any second following 10 consecutive SES seconds 
• A second for which any of the previous 10 consecutive seconds was also a UAS and 
any of the previous 10 consecutive seconds was a SES. 
SES  
Displays the number of severely errored seconds (SES) in the current interval. 
A SES is any second not declared a UAS which contains an OOF or more than 320 CRC 
errors. 
BES  
Displays the number of bursty errored seconds (BES) in the current interval. 
A BES is any second which is not declared a UAS and contains 2 to 319 CRC errors 
LOFC  
Displays the number of LOFC in the current interval. 
The loss of frame (LOF) counter counts the loss of frame alignment events. The data is 
collected for the current 15-minute interval. 
Rx Frames Slip 
Displays the number of Rx Frames Slips in the current 15-minute interval. 
A CSS is a second with one or more controlled slip events. 
5. Cards and Ports 
Parameter 
Description 
Time elapsed 
The elapsed time (in seconds) since the beginning of the current interval. The range is 1 
to 900 seconds.  
Valid Intervals 
The number of elapsed finished 15-min intervals for which statistics data can be 
displayed, in addition to the current (not finished) interval (up to 96). 
E1 Port Statistics Parameters – Selected 15-Minute Interval  
Parameter 
Description 
ES  
Displays the total number of errored seconds (ES) in the selected interval 
UAS 
Displays the total number of unavailable seconds (UAS) in the selected interval 
SES  
Displays the total number of severely errored seconds (SES) in the selected interval 
BES  
Displays the total number of bursty errored seconds (BES) in the selected interval 
LOFC  
Displays the total number of loss of frame alignment events in the selected interval 
Rx Frames Slip 
Displays the total number of Rx Frames Slip events in the selected interval  
Interval number 
The number of interval for which statistics is displayed.  
E1 Port Statistics Parameters – Total Statistics 
Parameter 
Description 
ES  
Displays the total number of errored seconds (ES) since statistics are available 
UAS 
Displays the total number of unavailable seconds (UAS) since statistics are available 
SES  
Displays the total number of severely errored seconds since statistics are available 
BES  
Displays the total number of bursty errored seconds (BES) since statistics are available 
LOFC  
Displays the total number of loss of frame alignment events since statistics are available 
Rx Frames Slip 
Displays the total number of Rx Frames Slip events since statistics are available  
 To clear the statistics for an E1 port: 
• 
At the prompt config>port>e1<slot>/<port>)#, enter clear-statistics. 
The statistics for the specified port are cleared. 
 To clear the statistics for an E1-i port: 
• 
At the prompt config>port>e1-i<slot>/<port>)#, enter clear-statistics. 