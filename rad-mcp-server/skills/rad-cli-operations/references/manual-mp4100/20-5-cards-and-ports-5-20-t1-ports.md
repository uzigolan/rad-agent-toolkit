# 5 Cards and Ports – 5.20 T1 Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 402–424.*


## Applicability and Scaling  *(p.402)*

5. Cards and Ports 
5.20 T1 Ports  
Applicability and Scaling 
The following table shows the number of t1 and t1-i ports and the features supported by each 
Megaplex-4 module. The digits in brackets (1 to 3) denote restrictions or other special remarks regarding 
implementation of this feature in specific modules.  
Megaplex-4 T1 and Internal T1 Ports  
Feature/ 
Command 
T1 Ports (t1) 
Internal T1 Ports (t1-i) 
T3 
VS-16E1T1-
EoP 
VS-16E1T1-PW 
VS-6/E1T1 
CL.2    
VS-16E1T1-EoP 
Number of ports 
28 
16 
16 
8 
84 
16 
name 
√ 
√ 
√ 
√ 
√ 
√ 
shutdown 
√ 
√ 
√ 
√ 
√ 
√ 
hierarchy 
slot:1:trib 
slot:port 
slot:port 
slot:port 
slot:port 
slot:port 
inband-management  
√ (1) 
√(1)(4) 
√(1) 
√(1) 
√(1) 
– 
line-interface 
– 
√ 
√ 
√ 
– 
– 
line-type 
√ 
√ (5) 
√  
√  
√ 
√ 
line-length (DSU only) 
– 
√ 
√ 
√ 
– 
– 
line-code 
– 
√ 
√ 
√ 
– 
– 
line-buildout (CSU 
only) 
– 
√ 
√ 
√ 
– 
– 
out-of-service (voice, 
data, 
signaling) 
√ (1) 
√ (1) 
√ (1) 
√ (1) 
√ (1) 
– 
restoration-time  
√ 
– 
– 
– 
– 
– 
idle-code 
√ (1) 
√ (1) 
√ (1) 
√ (1) 
√ (1) 
– 
vc-profile  
√  
√ (3) 
√ (3) 
√ (3) 
√  
√  
tx-clock-source 
– 
– 
√(6) 
√(6) 
– 
– 
 
1 - N/A for Unframed 
2 – Unframed is not supported when working with CL.2 module without SDH/SONET ports 

## Standards Compliance  *(p.403)*


## Functional Description  *(p.403)*

5. Cards and Ports 
3 – Applicable if line type is unframed and the link is directly mapped to SDH-SONET vc12-
vt2  
4 –N/A for T1 bound to VCG 
5 –When T1 is bound to VCG, line-type=esf only 
6 - Applicable when T1 is cross connected directly to PW  
Standards Compliance 
The T1 interface complies with ANSI T1.403-1989, AT&T Pub. 54016, AT&T TR-62411 and ANSI T1.107.4 
standards. 
Functional Description  
External T1 Link Interfaces are available in VS-16E1T1-PW, VS-6/E1T1 and VS-16E1T1-EoP I/O modules. 
Internal T1 ports are available in CL.2 and VS-16E1T1-EoP modules (denoted in CLI as t1-i) and T3 
modules (denoted in CLI as t1). The parameters configurable for each module can be chosen from the 
Megaplex-4 T1 and Internal T1 Ports table. General description of T1 port parameters is given in the 
following sections.  
Framing  
The external and internal T1 ports can be independently configured in accordance with the desired ITU-T 
framing mode and signaling formats: 
• 
D4 (SF) framing (12 frames per multiframe)  
• 
ESF framing (24 frames per multiframe)  
• 
Unframed mode: enables transparent transfer of 1.544 Mbps streams, including streams with 
proprietary framing.  
The framer automatically adds the appropriate overhead. Unused timeslots are filled with a 
user-specified idle code. The user can also select specific timeslots to be transferred (DS0 cross-
connect). 
The framing mode can be independently selected for each external or internal T1 port of the I/O 
module. It is configured by means of line-type parameter. 
5. Cards and Ports 
Line Interface (VS-16E1T1-EoP, VS-16E1T1-PW, VS-6/E1T1 Only)  
Each T1 line interface has an integral CSU, which enables operation with line attenuations up to 34 dB. 
The nominal transmit level is ±3V.  
The CSU transmit level must be adjusted to ensure reliable operation of the network. It can be 
attenuated by 7.5, 15, or 22.5 dB, for compliance with FCC Rules Part 68A. This adjustment minimizes 
the interference your transmit signal causes to other users that transmit their signals on other pairs of 
the same cable. The required setting depends mainly on the length of the cable that connects the T1 
port and the first repeater down the line.  
Repeaters are usually spaced a mile apart. They are therefore designed to optimally handle signals 
attenuated by one mile length of cable. If the T1 port were closer, the repeater would receive your 
signal at a higher level. This will not significantly improve the handling of your signal, but will certainly 
increase the interference coupled from your pair to repeaters that serve other pairs in the cable. To 
prevent this, you can select an attenuation value that will bring your signal level closer to the expected 
repeater signal level. This is achieved by connecting, as required, one, two, or three artificial line 
sections in series with your T1 transmit signal. Each line section introduces a nominal attenuation of 
7.5 dB (equivalent to the attenuation of approximately 1000 feet of cable). Your system administrator or 
data carrier will give you the proper setting for each port. 
The line interface can also emulate a DSU or J1 interface. The selection CSU/DSU/J1 is defined by the 
line-interface parameter. The relative output transmit level of the port is selected by means of the line-
buildout parameter. 
Once J1 is selected, the interface will operate per J1 standard (using the relevant physical masks, 
framing and signaling as defined for J1 interface). 
Line Length 
When configured for DSU emulation, the line transmit signal is user-adjustable for line lengths of 0 to 
655 feet in accordance with AT&T CB-119. The transmit signal mask is selected in accordance with the 
transmit line length, to meet DSX-1 requirements, as specified by AT&T CB-119. The following selections 
are available: 
• 
0 – 133 Ft 
• 
133 – 266 Ft 
• 
266 – 399 Ft 
• 
399 – 533 Ft 
• 
533 – 655 Ft. 
5. Cards and Ports 
These values define the length of the cable (in feet) connected between the port connector and the 
network access point. 
Zero Suppression  
Zero suppression is user-selectable, separately for each port: transparent (AMI) coding, B7ZS, or B8ZS. It 
is configured by means of line-code parameter. 
Interface Type 
The external T1 links have 100 Ω balanced interfaces.  
Handling of T1 Alarm Conditions 
The external and internal T1 ports support two types of indications in the individual timeslots: idle 
timeslots and out-of-service (OOS) indications. 
• 
Idle Timeslot Indication. A special code can be transmitted in empty timeslots (timeslots which 
do not carry payload).  
• 
OOS Indications. The OOS code is inserted in individual timeslots to signal the equipment routed 
to one of the module ports that the link connected to the external port is out-of-service (e.g., 
because of a loss of frame synchronization).  
The idle code and OOS indications can be independently configured for each module port. Moreover, 
separate OOS codes can be transmitted in the timeslots, in accordance with the type of payload carried 
by each timeslot (voice or data). 
T1 Payload Processing  
The Megaplex-4 T1 modules support two main types of payload per timeslot: 
• 
Data timeslots: timeslots which are transparently transferred from port to port. In general, it is 
assumed that no CAS is associated with data timeslots.  
Timeslots assigned to HDLC ports are always processed as data timeslots. 
• 
Management timeslots: with framed signals, one timeslot can be assigned in any port to carry 
management traffic. Such timeslots are always directed to the CL management subsystem, for 
processing. 
5. Cards and Ports 
The flow of payload carried by voice timeslots is normally bidirectional (full duplex connection). It is also 
possible to define unidirectional flows, called unidirectional broadcasts, from one source (a timeslot of a 
source port) to multiple destinations (each destination being a selected timeslot of another port).  
In case of data timeslots, the flow of payload is normally unidirectional. If the application requires 
bidirectional flows, cross-connect must be configured symmetrically for both directions.  
OOS Signaling 
If communication between modules located in different Megaplex units fails, e.g., because loss of main 
link synchronization, it is necessary to control the state of the signaling information at each end of the 
link. This activity, called out-of-service (OOS) signaling, is performed by the M8T1 modules and can be 
selected in accordance with the specific application requirements, on a per-link basis.  
The OOS signaling options are as follows:  
• 
Signaling forced to the idle state for the duration of the out-of-service condition (force-idle). 
This option is suitable for use with all the VC module types. 
• 
Signaling forced to the busy state for the duration of the out-of-service condition (force-busy). 
This option is suitable for use with E&M and FXO modules, but not with FXS modules. 
• 
Signaling forced to the idle state for 2.5 seconds, and then changed to the busy state for the 
remaining duration of the out-of-service condition (idle-busy). This option is suitable for use 
with E&M and FXO modules, but not with FXS modules. 
• 
Signaling forced to the busy state for 2.5 seconds, and then changed to the idle state for the 
remaining duration of the out-of-service condition (busy-idle). This option is suitable for use 
with all the VC module types. 
Inband Management 
T1 and internal T1 ports of Megaplex-4 using a framed mode feature inband management access to the 
end user’s equipment provided by configuring a dedicated management timeslot. 
The transfer of inband management traffic is controlled by using synchronous PPP over HDLC 
encapsulation or Frame Relay encapsulation (under DLCI 100) in accordance with RFC 2427. 
Transmission of RIP2 routing tables is done via the following options:  
• 
Proprietary RIP – Management traffic is routed using RAD proprietary routing protocol 
• 
RIP2 – In addition to the RAD proprietary routing protocol, RIP2 routing is also supported. 

## Factory Defaults  *(p.407)*


## Configuring a T1 Port  *(p.407)*

5. Cards and Ports 
Factory Defaults 
Megaplex-4 is supplied with all t1/t1-i ports disabled. Other parameter defaults are listed in the table 
below. 
Parameter  
Default Value 
line-type 
esf  
restoration-time  
10sec 
line-interface  
csu  
idle-code  
0x7f 
inband-management  
no inband-management (disabled)  
inband-management – routing-protocol  
none  
out-of-service - voice  
00 
out-of-service - data  
00 
out-of-service - signaling   
force-idle 
signaling-profile  
1  
line-code  
b8zs 
line-length  
0-133 
line-buildout  
0db 
duration  
infinite 
Configuring a T1 Port  
 To configure the T1 port parameters of I/O modules: 
1. Navigate to configure port t1 <slot>/<port>/<tributary> to select the T1 port to configure.  
The config>port>t1>(<slot>/<port>/<tributary>)# prompt is displayed.  
Note 
<tributary> refers to T1 ports of T3 modules. 
2. Enter all necessary commands according to the tasks listed below (see Megaplex-4 T1 and 
Internal T1 Ports table for parameters supported in each module). 
5. Cards and Ports 
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
Specifying T1 framing 
mode  
line-type {unframed | esf | sf} 
 
When the T1 port is bound to a VCG port, VS-
16E1T1-EoP supports esf option only. 
Setting the line code used 
by the port, and the zero 
suppression method 
line-code {ami | b8zs}  
For guaranteed clear channel capability, use 
B8ZS; do not use B7ZS for ports carrying 
inband management 
Specifying T1 operation 
mode     
line-interface {dsu | csu | j1 }       
<dsu>  : DSU (short haul) 
<csu>   : CSU (long haul) 
<j1>      : J1 (long haul) 
Specifying the length of 
the T1 line in DSU mode 
line-length {0-133 | 134-266 | 267-399 | 
400-533 | 534-655}  
 
Specifying the code 
transmitted to fill unused 
timeslots in T1 frames 
idle-code <00 to FF (hexa)>     
The available selections are [0x40 to 0x7F] 
and [0xC0 to 0xFF] 
Enabling inband 
management and setting 
its parameters 
inband-management <timeslot> protocol 
{ppp | fr} [routing-protocol {none | 
prop-rip | rip2} ]  
  
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
Not available for VS-16E1T1-EoP when this  
T1 port is bound to a VCG port 
Transmitting an 
out-of-service signal (OOS)   
out-of-service [ voice <00 to FF (hexa)>] 
[data <00 to FF (hexa)>] [signaling 
{force-idle | force-busy | idle-busy | 
busy-idle} ]   
 
5. Cards and Ports 
Task 
Command  
Comments 
Setting the time required 
for a port to resume 
normal operation after 
loss of frame 
restoration-time {1sec | 10sec}  
Used to change the frame synchronization 
algorithm, to reduce the time required for the 
port to return to normal operation after local 
loss of synchronization. 
1sec – After 1 second. 
10sec – Similar to the requirements of AT&T 
TR-62411 (after 10 seconds). 
This parameter cannot be changed when 
using the Unframed mode. 
Specifying the line build-
out (relative output 
transmit level of the port) 
line-buildout {0db | -7dot5db | -15db |  
-22dot5db}  
VS-16E1T1-EoP, VS-16E1T1-PW and VS-
6/E1T1 modules only 
CSU mode only 
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
 
Relevant for VS-16E1T1-EoP and T3 modules, 
VS-16E1T1-PW, VS-6/E1T1.  
For creating VC profiles, see VC Profiles. 
Using no vc removes the profile. 
Configuring collection of 
performance management 
statistics for this port, 
which are presented via 
the RADview Performance 
Management portal 
 
pm-collection interval <seconds> 
You can enable PM statistics collection for all 
T1 ports rather than enabling it for individual 
ports. In addition to enabling PM statistics 
collection for the ports, it must be enabled 
for the device. Refer to the Performance 
Management section in the Monitoring and 
Diagnostics chapter for details. 

## Configuring an Internal T1 Port  *(p.410)*

5. Cards and Ports 
Configuring an Internal T1 Port  
 To configure the internal T1 port parameters: 
1. Navigate to configure port t1-i <slot>/<port> to select the internal T1 port to configure. 
The config>port>t1-i>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
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
Specifying T1 framing 
mode  
line-type {unframed | esf | sf} 
 
When the internal T1 port is bound to a VCG 
port, VS-16E1T1-EoP supports esf option only. 
Specifying  the code 
transmitted to fill unused 
timeslots in T1 frames 
idle-code <00 to FF (hexa)> 
The available selections are [0x40 to 0x7F] 
and [0xC0 to 0xFF] 
Enabling inband 
management and setting 
its parameters 
inband-management <timeslot> protocol 
{ppp | fr} [routing-protocol {none | 
prop-rip | rip2} ]  
  
ppp – synchronous PPP over HDLC 
encapsulation  
fr –Frame Relay encapsulation (under DLCI 
100) in accordance with RFC 2427 
See also Configuring Inband Management in 
Chapter 8 for important considerations on 
selecting the routing protocol. 
Not available for VS-16E1T1-EoP when this  
T1 port is bound to a VCG port 
Using no inband management  <timeslot> 
disables inband management through this 
timeslot 

## Examples  *(p.411)*

5. Cards and Ports 
Task 
Command  
Comments 
Setting the time required 
for a port to resume 
normal operation after 
loss of frame 
restoration-time {1sec | 10sec}  
 
Used to change the frame synchronization 
algorithm, to reduce the time required for the 
port to return to normal operation after local 
loss of synchronization. 
1sec – After 1 second. 
10sec – Similar to the requirements of AT&T 
TR-62411 (after 10 seconds). 
This parameter cannot be changed when 
using the Unframed mode. 
Configuring collection of 
performance management 
statistics for this port, 
which are presented via 
the RADview Performance 
Management portal 
 
pm-collection interval <seconds> 
You can enable PM statistics collection for all 
T1 ports rather than enabling it for individual 
ports. In addition to enabling PM statistics 
collection for the ports, it must be enabled 
for the device. Refer to the Performance 
Management section in the Monitoring and 
Diagnostics chapter for details. 
Assigning VC profile to the 
port 
vc profile <profile name> 
 
Using no vc removes the profile  
Examples 
Example 1 
The following example illustrates how to configure the T1 port labeled 1 on the module installed in slot 9 
as follows:  
• 
Set the T1 framing mode to SF. 
• 
Set the restoration time to 10 sec. 
• 
Set the line code to AMI. 
• 
Set the idle code to 8E. 
• 
Administratively enable the port. 
• 
Leave all other parameters disabled or at their defaults. 
config>port>t1(9/1)# line-type sf 
config>port>t1(9/1)# line-code ami  
config>port>t1(9/1)# restoration-time 10sec   

## Configuration Errors  *(p.412)*

5. Cards and Ports 
config>port>t1(9/1)# idle-code 0x8E 
config>port>t1(9/1)# no shutdown 
Example 2 
This section illustrates how to configure inband management via a dedicated timeslot. 
1. Program a module in Slot 1 and configure inband management via T1 port 1 with the following 
parameters:  
 
Dedicated timeslot - #24   
 
Inband management protocol: synchronous PPP over HDLC encapsulation  
 
Routing protocol: RAD proprietary RIP.  
config>slot# 4 card-type e1-t1 m8t1 
config>port# t1 1/1 no shutdown 
config>port# t1 1/1 line-type sf 
config>port# t1 1/1 inband-management 24 protocol ppp routing-protocol prop-rip  
2. Configure router interface 5. 
config>router# 1 interface 5 address 17.17.17.17/24  
3. Bind T1 port 1/1 to router interface 5. 
config>router# 1 interface 5 bind t1 1/1 
Configuration Errors 
The following table lists messages generated by Megaplex-4 when a configuration error on T1 modules 
is detected.  
T1 Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
131 
Warning RESTORATION TIME DOES NOT 
MATCH THE STD 
For T1 links, the restoration time must be 10 seconds, 
according to the standard.  
132 
Error 
FRAME TYPE / PROFILE 
MISMATCH 
The selected framing mode does not support signaling 
profiles. 
141 
Error 
ROUTING PROTOCOL/ 
MNG TYPE MISMATCH 
The rip2 protocol on an I/O module port can be enabled 
only when the inband management method is configured to 
ppp or fr 

## Viewing a T1 Port Status  *(p.413)*


## Testing T1 Ports  *(p.413)*

5. Cards and Ports 
Code 
Type 
Syntax 
Meaning 
144 
Error 
ILLEGAL IDLE CODE SELECTION 
Code transmitted in idle timeslots is illegal. The available 
selections for T1/T1-i ports are [0x40 to 0x7F] and [0xC0 to 
0xFF]  
Viewing a T1 Port Status 
Follow the instructions below for viewing the status of a T1 port. 
 To view the T1 port status: 
• 
At the config>port>t1(<slot>/<port>/<tributary>)# prompt, enter show status. 
Note 
The index <tributary> is applicable to internal T1 ports of T3 modules. 
The status information appears as illustrated below.  
For T1-i ports of CL.2 modules: 
config>port>t1-i(cl-a/1)# show status 
Name                  : CL-A t1-i 01 
Administrative Status : Up 
Operation Status      : Up 
Loopback Type         : None 
For T1 ports of T3 modules: 
config>port>t1(3/1/1)# show status 
Name                  : IO-1 t1 01/01 
Administrative Status : Up 
Operation Status      : Up 
Loopback Type         : None 
Testing T1 Ports  
The Megaplex-4 T1 ports feature test and loopback functions at the port and timeslot levels. The 
following loops are supported on all t1/t1-i ports: 
• 
Local loopback on t1/t1-i module port 
• 
Remote loopback on t1/t1-i module port 
• 
Local loopback on timeslots of t1/t1-i module port 
• 
Remote loopback on timeslots of t1/t1-i module port 
5. Cards and Ports 
• 
BER test on T1 ports of VS modules.  
The hierarchical position of t1 ports is as follows: 
• 
For t1 ports of T3 modules: slot:1:tributary  
• 
For t1 and t1-i ports of other modules: slot:port.  
CL Modules 
The following sections briefly describe each type of loopback on T1-i ports of CL modules. The table 
below shows the paths of the signals when each or loopback is activated.  
Loopbacks on T1-i ports of CL.2 Modules 
 
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
Local loopback on T1-
i port  
 
 
1
......
E1-i/T1-i Framers
2
 
  
 
5. Cards and Ports 
Remote loopback on 
T1-i  port  
 
 
1
......
E1-i/T1-i Framers
2
 
  
 
Local loopback on 
timeslots of  
T1-i port  
 
 
1
......
E1-i/T1-i Framers
2
  
 
Remote loopback on 
timeslots of  
T1-i  port  
 
 
1
......
E1-i/T1-i Framers
2
 
  
 
Local Loopback on T1-i Port  
The local T1-i port loopback is used to test the intra-Megaplex-4 paths of the signals intended for 
transmission through a selected T1-i port. These paths start at the other Megaplex-4 port(s) connected 
to the tested T1-i port, pass through the DS1 cross-connect matrix in the CL module, and continues up to 
the framer of the T1-i port within the SDH/SONET link interface. These paths include all of the Megaplex-
4 local ports connected to the tested T1-i port, and in the particular the operation of the DS1 
cross-connect matrix circuits that handle the signals directed to the tested T1-i port within the CL 
module. 
The local T1-i port loopback is activated within the T1-i framer of a selected CL T1-i port, as shown 
above. 
5. Cards and Ports 
Remote Loopback on T1-i Port  
The T1-i port remote loopback is activated on the framer serving the port within the SDH/SONET link 
interface, as shown above. 
Local Loopback on T1-i Port Timeslots  
The local loopback on selected timeslots of a T1-i port is used to return the transmit payload carried by 
the selected timeslots through the same timeslots of the receive path. The timeslots looped back remain 
connected to the transmit path of the port, but the corresponding timeslots received from the remote 
end are disconnected. 
This test is recommended for testing the signal paths between the T1-i port and an I/O port of another 
module that uses only a fraction of the available T1-i port bandwidth. 
The loopback is activated only on the timeslots specified by the user, as shown above.  As a result, there 
is no disturbance to services provided by means of the other timeslots of the same T1-i port: only the 
flow of payload carried by the specified timeslots is disrupted. 
You can activate the loopback on any individual timeslot, or on several arbitrarily selected timeslots. You 
cannot activate loopbacks on timeslots cross-connected with HDLC ports. 
Remote Loopback on T1-i Port Timeslots  
The remote loopback on selected timeslots of a T1-i port is used to return the receive payload carried by 
the selected timeslots through the same timeslots of the transmit path. The corresponding timeslots 
received from the local equipment are disconnected.  
This test is recommended for testing signal paths from a remote equipment unit, through the selected 
timeslots of the T1-i port, to an I/O port of another module that uses only a fraction of the available port 
bandwidth. 
The loopback is activated only on the timeslots specified by the user, as shown above. As a result, there 
is no disturbance to services provided by means of the other timeslots of the same T1-i port: only the 
flow of payload carried by the specified timeslots is disrupted. You cannot to activate loopbacks on 
timeslots assigned to HDLC ports. 
I/O Modules  
The following sections briefly describe each type of loopback on T1 ports of I/O modules. The figure 
below shows the paths of the signals when each or loopback is activated.  
5. Cards and Ports 
 Loopbacks on T1 Ports of I/O Modules 
 
 I/O CL 
Local loopback on T1 port (VS-16E1T1-
EoP, VS-16E1T1-PW, VS-6/E1T1, T3 
modules) 
Port 
Interface
 1 
"   "
DS1
Cross-Connect
Matrix
 
Remote loopback on T1 port (VS-16E1T1-
EoP, VS-16E1T1-PW, VS-6/E1T1 modules) 
    Port 
    Interface
DS1
Cross-Connect
Matrix
 
Local loopback on T1 timeslots (VS-
16E1T1-PW, VS-6/E1T1, VS-16E1T1-EoP 
modules) 
DS1
Cross-Connect
Matrix
1
.....
2
I/O Interface
 
Remote loopback on T1 timeslots (VS-
16E1T1-EoP, VS-16E1T1-PW, VS-6/E1T1 
modules) 
1
.....
2
DS1
Cross-Connect
Matrix
I/O Interface
 
Local Loopback on T1 Port of I/O Module  
The local port loopback is used to test the path of the signals intended for transmission through a 
selected T1 port: this path starts at the other  
Megaplex-4 port(s) connected to the selected port, passes through the cross-connect matrix in the CL 
module, and continues up to the port line interface. Within the tested module, the path includes most 
5. Cards and Ports 
of the line interface circuits serving the selected port, and the operation of the routing circuits that 
handle the port signals within the module. 
As shown above, when a local loopback is activated, the port transmit signal is returned to the input of 
the same port receive path at a point just before the line interface. The local port must receive its own 
signal, and thus it must be frame-synchronized. In addition, each I/O module connected to the 
corresponding port must also receive its own signal. In general, the result is that these modules are 
synchronized and do not generate alarm indications.  
To provide a keep-alive signal to the transmission equipment serving the link under test while the 
loopback is activated, the port line interface transmits an unframed “all-ones” signal (AIS) to the line. AIS 
reception will cause the remote equipment to lose frame synchronization while the loopback is 
connected. This is normal and does not necessarily indicate a fault. 
Remote Loopback on T1 Port of I/O Module  
The remote port loopback is used to test the line interface circuits of a selected T1 external port. This 
test also checks the transmission plant connecting the equipment connected to the corresponding port. 
As shown above, when a remote loopback is activated on a T1 port, that port returns the received signal 
to the remote unit, via the transmit path. The received signal remains connected as usual to the receive 
path of the corresponding port. To correct transmission distortions, the returned signal is regenerated 
by the corresponding line interface circuits. 
The remote loopback should be activated only after checking that the remote unit operates normally 
with the local port loopback. In this case, the remote unit must receive its own signal, and thus it must 
be frame-synchronized. The effect on the individual modules is mixed, as explained above for the local 
loopback. 
If the local Megaplex-4 unit also operated normally when the local port loopback was activated, then 
while the remote loopback is connected the local unit should receive a valid signal, and thus it must be 
frame-synchronized.  
The remote port loopback should be activated at only one of the units connected in a link, otherwise an 
unstable situation occurs.  
Local Loopback on Timeslots of T1 I/O Module Port 
The local loopback on selected timeslots of a T1 port is used to return the transmit payload carried by 
the selected timeslots through the same timeslots of the receive path. This test is recommended for 
testing the signal paths between an I/O port of another module that uses only a fraction of the available 
port bandwidth, and the T1 port. 
5. Cards and Ports 
As shown above, the loopback is activated within the I/O module routing matrix, and only on the 
timeslots specified by the user during the activation of the loopback. As a result, there is no disturbance 
to services provided by means of the other timeslots of the same port: only the flow of payload carried 
by the specified timeslots is disrupted. 
The user can activate the loopback on any individual timeslot, or on several arbitrarily selected 
timeslots. It is not allowed to activate loopbacks on timeslots assigned to HDLC ports. 
This convenience feature is also available for loopback deactivation: the deactivation command can be 
issued to either one of the ports of the protection group (even if it has been activated by a command to 
the other port). 
Remote Loopback on Timeslots of T1 I/O Module Port  
The remote loopback on selected timeslots of a T1 port is used to return the receive payload carried by 
the selected timeslots through the same timeslots of the transmit path. This test is recommended for 
testing signal paths from a remote equipment unit, through the selected timeslots of the T1 port, to an 
I/O port of another module that uses only a fraction of the available port bandwidth. 
As shown above, the loopback is activated within the I/O module routing matrix, and only on the 
timeslots specified by the user. As a result, there is no disturbance to services provided by means of the 
other timeslots of the same port: only the flow of payload carried by the specified timeslots is disrupted. 
It is not allowed to activate loopbacks on timeslots assigned to HDLC ports. 
The other features related to loopback activation/deactivation described above for the local loopback 
on timeslots are also applicable to the remote loopback. 
BER Test  
The BER test, activated by the command bert, is used to evaluate data transmission through selected 
timeslots of the link connected to a selected T1 without using external test equipment. It is available on 
the T1 ports of VS modules.  
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the Megaplex-4. 
Therefore, when you initiate a loopback, you have the option to limit its duration to an interval in the 
range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-4 before 
5. Cards and Ports 
this timeout expires. When using inband management, always use the timeout option; otherwise, the 
management communication path may be permanently disconnected. 
The default is infinite duration (without timeout). 
Activating Loopbacks and BER Tests  
 To perform a loopback or BER test on the T1 port: 
1. Navigate to configure port t1 <slot>/<port>/[<tributary>] to select the T1 port to be tested. 
Note 
The index <tributary> is applicable to internal T1 ports of T3 modules. 
The config>port>t1>(<slot>/<port>[<tributary>])# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
 To perform a loopback on the internal T1 port:  
1. Navigate to configure port t1-i <slot>/<port> to select the internal T1 port to be tested. 
The config>port>t1-i>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Activating and configuring 
the direction of the 
loopback and the duration 
of it (in minutes) 
loopback {local | remote} [time-
slot <1..24>] [duration <duration 
in minutes 1..30> ]  
 
• local – local loopback 
• remote – remote loopback 
Stopping the loopback  
no loopback 
 
Activating the BER test and 
configuring its parameters 
bert  [ts <ts number 1..24>] 
[inject-error single]  
  
The [ts <ts number in the range from 1  to 
24>] command is used only for framed 
ports and is mandatory for these ports. 
The timeslot on which BERT is performed 
must be cross-connected. 
CL flip stops the BERT session. 
Stopping the BER test  
no bert 
 

## Displaying T1 Port Statistics  *(p.421)*

5. Cards and Ports 
Task 
Command 
Comments 
Displaying the BER test 
results 
show bert 
 
A typical display: 
Status         : Not Active 
Bit Error Count: 1            
Pattern        : 2e-15        
Run Time (Sec) : 1            
ES (Sec)       : 1            
Sync Loss (Sec): 1  
Clearing the BER test 
counters 
clear-bert-counters 
 
 
Displaying T1 Port Statistics  
T1 and T1-i ports of Megaplex-4 feature the collection of statistical diagnostics per ANSI T1.403, thereby 
allowing the carrier to monitor the transmission performance of the links. 
 To display the T1 port statistics: 
• 
At the prompt config>slot>port>t1(<slot>/<port>/[tributary])#, enter show statistics followed 
by the parameters listed below.  
Note 
The index <tributary> is applicable to internal T1 ports of T3 modules. 
 To display the T1-i port statistics: 
• 
At the prompt config>slot>port>t1-i(<slot>/<port>)#, enter show statistics followed by the 
parameters listed below.  
Task 
Command 
Comments 
Displaying statistics 
show statistics {total | all | all-intervals | 
current}  
 
 
 
  
• total - Total statistics of last 96 
intervals  
• all-intervals – Statistics for all 
valid intervals  
• current - Current statistics 
• all – All statistics: first current 
statistics, then statistics for all 
valid intervals, and finally total 
statistics 
5. Cards and Ports 
Task 
Command 
Comments 
Displaying statistics 
for a specific interval 
show statistics interval <interval-num 1..96> 
 
 
T1 port statistics are displayed.  The counters are described above. 
Note 
BES, LOFC and Rx Frames Slip are displayed for framed formats only and are 
not displayed for T1 ports of T3 modules. 
For example: 
Current statistics: 
 
config>port>t1(1/2)# show statistics current 
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
 
config>port>t1(3/1)# show statistics interval 67 
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
 
config>port>t1(1/2)# show statistics total 
Total 
--------------------------------------------------------------- 
ES             : 2 
SES            : 0 
UAS            : 0 
 
BES            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
All statistics: 
5. Cards and Ports 
 
config>port>t1(1/2)# show statistics all 
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
T1 Port Statistics Parameters – Current 15-Minute Interval  
Parameter 
Description 
ES  
Displays the number of errored seconds in the current 15-minute interval. 
An errored second is any second not declared a UAS in which a OOF (Out of Frame) or 
CRC (Cyclic Redundancy Check error) occurred. 
5. Cards and Ports 
Parameter 
Description 
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
Time elapsed 
The elapsed time (in seconds) since the beginning of the current interval. The range is 1 
to 900 seconds.  
Valid Intervals 
The number of elapsed finished 15-min intervals for which statistics data can be 
displayed, in addition to the current (not finished) interval (up to 96). 
T1 Port Statistics Parameters – Selected 15-Minute Interval  
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
 
Displays the number of interval for which statistics is displayed. Interval #1 is the earliest in 
time. 