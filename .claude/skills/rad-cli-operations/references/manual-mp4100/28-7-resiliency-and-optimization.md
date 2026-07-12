# 7 Resiliency and Optimization

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 549–631.*


## (chapter introduction)  *(p.549)*

The modular, distributed architecture of Megaplex-4 enables redundancy at different levels of the 
network and provides a resilient system with no single point of failure. Hardware redundancy is 
provided through an optional redundant power supply and CL modules, with switchover to the backup 
CL links within 50 msec.  
Each combined common logic, cross-connect matrix and broadband link module (CL) provide automatic 
switchover between each two STM-1/STM-4/OC-3/OC-12 links within 50 msec, for 1+1 protection 
against hardware, network or cable failure. The SDH/SONET employs APS 1+1 protection as well as 
Subnetwork connection protection (SNCP for SDH and UPSR for SONET) for path protection.  
The Ethernet traffic is protected by a G.8032 Layer-2 Ethernet ring. This technology builds a logical ring, 
defined as a set of IEEE 802.1-compliant bridges, and protects against link and node failures. Megaplex-4 
supports 5 rings per chassis. 
The Ethernet GbE ports also feature LAG- and VCG-based link protection mechanism over SDH/SONET. 
In addition, any E1/T1 stream can be protected using various mechanisms over any interface.  
Selected I/O modules can also be configured for redundancy and can be hot-swapped, allowing for 
continuous service. In addition to supporting standard SDH/SONET rings, Megaplex-4 can be used to 
create E1, T1, TDM over fiber, or a mix of ring topologies.  
External and internal E1/T1 links feature the TDM group protection on the port level.  
The following tables show the protection features supported by each I/O module on the port level. The 
hierarchical position of e1/t1 and e1-i/t1-i ports is slot:port for all the modules).  
In addition, TP and T3 modules feature TDM group protection on their cmd-channel and t3 ports, 
respectively.  
All PW-equipped modules provide TDM group protection on their DS1 ports. In addition, all PW-
equipped modules feature PW protection.  
TDM Protection on E1/T1 Ports  
Protection  type 
VS E1/T1 Ports (e1/t1) 
 
 
dual-cable-tx 
√ 

## 7.1 Fault Propagation  *(p.550)*

7. Resiliency and Optimization 
Table 7-13. TDM Protection on E1-i/T1-i and DS1 Ports 
Protection  type 
Internal E1/T1 Ports (e1-i/t1-i) 
Internal DS1 Ports (ds1) 
CL.2    
 
 
VS, TP 
dual-cable-tx 
√ 
 
 
√ 
 
7.1 Fault Propagation   
The fault propagation function can be used to notify equipment at a far end port that a fault condition 
has been detected at a local port connected to it.  
Functional Description 
Fault propagation is supported for compatible types of ports, for example: 
• 
Between interconnected external E1/T1, internal E1-i/T1-i or PW ports  
• 
Between the Ethernet, GFP or MLPPP ports. 
For each port type, the following table lists the following: 
• 
Failure or alarm conditions at this (failed) port used to initiate a response at another (affected) 
port  
• 
Response (action) at this port when it is affected (“to” port in CLI). 
Fault Propagation Response  
Port Type  
Detected Failure or Alarm Condition 
Action at the Port when it is Affected  
GbE  
• “eth – los” alarm 
• “card – card_mismatch” alarm (module 
removed)  
Disconnecting GbE port 
External Fast 
Ethernet (I/O 
modules) 
• “eth – los” alarm 
• “card – card_mismatch” alarm (module 
removed) 
Disconnecting the Ethernet port 
7. Resiliency and Optimization 
Port Type  
Detected Failure or Alarm Condition 
Action at the Port when it is Affected  
GFP 
  
• With LCAS: “vcg –minimum members 
tca” alarm 
• Without LCAS: “gfp – rx_trail_failure” 
alarm  
• “gfp – csf” alarm 
• “card – card_mismatch” alarm (module 
removed) 
CSF(Client Signal Failure) frame will be 
sent instead of idle GFP frames on the 
associated VCGs 
MLPPP  
• “ppp – bcp_failure” alarm 
• “card – card_mismatch” alarm (module 
removed) 
MLPPP port is down (BCP down) 
PW 
• “pw –pw_configuration_mismatch” 
alarm 
• “pw – fe_rdi” alarm                           
• “pw –rx_failure” alarm  
• “pw –fe_rx_failure” alarm  
• “card – card_mismatch” alarm (module 
removed) 
Sending of PW packets with Local Fail 
indication (L-bit set) to remote PW 
 
E1-i/T1-i 
(CL.2 module) 
• “e1t1 – ais” alarm 
• “e1t1 – lof” alarm 
• “e1t1 – rai” alarm 
• “e1t1 – lomf” alarm 
• “e1t1 – lomf_fe” alarm 
• “e1t1 – los” alarm 
• “card – card_mismatch” alarm (module 
removed) 
Sending of AIS 
E1-i/T1-i 
(VS-16E1T1-EoP 
module)  
• “e1t1 – ais” alarm 
• “e1t1 – lof” alarm 
• “e1t1 – rai” alarm 
•  “e1t1 – los” alarm 
• “card – card_mismatch” alarm (module 
removed) 
Unframed AIS is generated 
7. Resiliency and Optimization 
Port Type  
Detected Failure or Alarm Condition 
Action at the Port when it is Affected  
E1/T1 ports  
(VS-16E1T1-EoP, 
VS-16E1T1-PW, 
VS-6/E1T1 
modules)  
• “e1t1 – ais” alarm 
• “e1t1 – lof” alarm 
• “e1t1 – rai” alarm 
• “e1t1 – lomf” alarm 
• “e1t1 – lomf_fe” alarm 
•  “e1t1 – los” alarm 
• “card – card_mismatch” alarm (module 
removed) 
Unframed AIS is generated 
Internal E1/T1 
ports (MP Optimux 
modules)   
• “e1t1 – ais” alarm 
• “e1t1 – lof” alarm 
• “e1t1 – rai” alarm 
• “e1t1 – lomf” alarm 
• “e1t1 – lomf_fe” alarm 
• “card – card_mismatch” alarm (module 
removed) 
Sending of AIS by the associated E1 port 
of the remote standalone device  
7. Resiliency and Optimization 
Port Type  
Detected Failure or Alarm Condition 
Action at the Port when it is Affected  
C37.94 
• “e1t1 – ais” alarm 
• “e1t1 – lof” alarm 
• “e1t1 – rai” alarm 
• “e1t1 – los” alarm 
• “card – card_mismatch” alarm (module 
removed) 
AIS shall be generated 
G.703 
• “ds0-g703 – ais” alarm 
• “ds0-g703 – los” alarm 
•  “ds0-g703 – oos” alarm 
AIS shall be generated  
Internal T1 ports 
(T3 module)  
• “e1t1 – ais” alarm 
• “e1t1 – lof” alarm 
• “e1t1 – rai” alarm 
• “e1t1 – lomf” alarm 
• “e1t1 – lomf_fe” alarm 
• “e1t1 – los” alarm 
• “card – card_mismatch” alarm (module 
removed) 
AIS shall be generated 
Factory Defaults  
By default, fault propagation is not configured.  
Configuring Fault Propagation 
Follow this procedure to configure fault propagation: 
 To add fault propagation for a pair of interfaces: 
3. Navigate to configure fault. 
4. Type the command: 
fault-propagation <from-interface> to <to-interface> 
The fault propagation in the “to” direction is established.  
7. Resiliency and Optimization 
Fault Propagation  
Task 
Command  
Comments 
Configuring fault 
propagation for 
external/internal e1/ 
t1 ports and 
pseudowires 
 
fault-propagation port {e1 | t1 | e1-i | 
t1-i | ds1-opt | pw} <slot>/<port> 
to port {e1 | t1 | e1-i | t1-i | ds1-opt | 
pw} <slot>/<port> 
Optional <tributary> index refers only to e1 
ports of t1 ports of T3 cards. 
In the case of a PW participating in the fault 
propagation, <slot>/<port>/ [<tributary>] 
on the corresponding side must be replaced 
by <pw number>. 
Using no before fault-propagation disables 
the command. 
Configuring fault 
propagation for 
ethernet type ports 
and pseudowires 
fault-propagation port {ethernet | gfp | 
mlppp | pw} <slot>/<port> 
to port {ethernet | gfp | mlppp | 
pw}  <slot>/<port> 
 
 In the case of a PW participating in the fault 
propagation, <slot>/<port> on the 
corresponding side must be replaced by 
<pw number>. 
Using no before the full command disables 
the command.  
When configuring fault propagation, the following must be taken into account: 
• 
The maximum number of affected ports defined per one failed port is 10  
• 
In bidirectional fault propagation, one failed port corresponds to one affected port and vice 
versa 
• 
The maximum number of fault propagation entries defined in the system is 200  
• 
Neither failed nor affected E1/T1/E1-i/T1-i port can be configured as unframed 
• 
An E1/T1/E1-i/T1-i port defined as protection in a TDM protection group cannot be selected by 
the user as failed or affected.  
• 
If a working port in a TDM protection group is selected as failed or affected, the protection port 
is internally added to the fault propagation configuration. In particular: 
 
If a working port of a TDM group is selected as failed, the port selected as affected responds 
only if both working and protection ports fail 
 
If a working port of a TDM group is selected as affected, both working and protection ports 
will be affected by the failed port. 
Configuration Errors 
The table below lists messages generated by Megaplex-4  when a configuration error is detected. 

## 7.2 APS Protection  *(p.555)*

7. Resiliency and Optimization 
Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
631 
Error 
FP PORT IS IN SHUTDOWN 
STATE 
The port configured for fault propagation is in shutdown 
state and the other one is set to no shutdown. Both ports 
must be set either to shutdown or to no shutdown.  
632 
Error 
FP PORT CAN'T AFFECT ITSELF 
The same port cannot be failed and affected at the same 
time. 
633 
Error 
UNFRAMED PORT CAN'T 
PARTICIPATE IN FP 
Neither failed nor affected E1/T1/E1-i/T1-i/DS-1 port can be 
configured as  unframed. 
634 
Error 
UP TO 200 FP ENTRIES CAN BE 
CONFIGURED 
The maximum number of fault propagation entries has been 
exceeded 
635 
Error 
FP AFFECTED PORT IS USED 
MORE THAN ONCE 
A port cannot be defined as affected by more than one 
failed port 
636 
Error 
FAILED PORT CAN AFFECT UP 
TO 10 PORTS 
The maximum number of affected ports per one failed port 
has been exceeded 
637 
Error 
ASYMMETRIC BI DIR FP 
CONFIGURATION 
In bidirectional fault propagation, one failed port must 
correspond to one affected port, and vice versa 
638 
Error 
PROTECTED PORT CAN'T BE 
CONFIGURED IN FP 
A port defined as protection in a protection group cannot  
be selected by user as failed or affected. If a working port is 
selected as failed or affected, the protection port is 
internally added to the fault propagation configuration. 
639 
Error 
FP FAILED PORT IS NOT 
SUPPORTED 
The failed port configured is not supported by Fault 
Propagation process 
640 
Error 
FP AFFECTED PORT IS NOT 
SUPPORTED 
 
The affected port configured is not supported by Fault 
Propagation process 
 
7.2 APS Protection 
Two SDH/SONET ports can work in APS (Automatic Protection Switching) mode. The APS configuration 
allows you to specify the two working ports and their operational mode, which can comply with one of 
the standards quoted below. 
7. Resiliency and Optimization 
Standards 
Automatic Protection Switching complies with the following standards: 
• 
1+1 unidirectional APS (G.842, Clause 7.1.4.4) 
• 
1+1 bidirectional compatible APS (G.841, Clause 7.1). 
• 
1+1 bidirectional optimized APS (G.841 Annex B. Linear Multiplex Section (MSP); compatible 
with 1:1 bidirectional switching) 
Benefits 
APS switches over traffic with minimal loss of data, thus avoiding time-consuming reroutes. With APS, 
there is no indication beyond the affected network element that a failure has occurred; other nodes stay 
intact. SDH/SONET APS performs switchovers at Layer 1 significantly faster than at Layer 2 or Layer 3. 
The effect of a failure is greatly minimized, and a fast switchover guarantees minimal effect on the 
network. 
Functional Description 
Automatic protection switching (APS) is a link-level protection mechanism for ensuring service 
continuity in the case of interface failure/error.  
In Megaplex-4, the APS can be configured with the following operating modes:  
• 
1+1 optimized bi-directional mode. You specify two working ports, 1 and 2, and bind one of the 
four ports available on CL.2 module (sdh-sonet cl-a/1, cl-a/2, cl-b/1, cl-b/2) to working port 1 
and another one to working port 2 respectively. The protocol used to handle the switching is 
carried out using K1 and K2 bytes from the line header of the SONET/SDH frame. 
• 
1+1 compatible bi-directional mode. You specify a working port and a protection port. Bind one 
of the four ports available on CL.2 module (sdh-sonet cl-a/1, cl-a/2, cl-b/1, cl-b/2) to the working 
port and another one to the protection port respectively. The protocol used to handle the 
switching is carried out using K1 and K2 bytes from the line header of the SONET/SDH frame. 
• 
1+1 unidirectional mode. You specify a working port and a protection port. Bind one of the four 
ports available on CL.2 module (sdh-sonet cl-a/1, cl-a/2, cl-b/1, cl-b/2) to the working port and 
another one to the protection port respectively. The protocol used to handle the switching is 
carried out using SDH/SONET alarms. 
7. Resiliency and Optimization 
The alarm criteria taken into consideration for protection switching are grouped into two categories: 
major alarm and minor alarm. 
The major alarms are caused by any of the following: 
• 
An SFP is removed from the socket  
• 
Loss of SDH/SONET line signal is detected 
• 
Loss of SDH/SONET frame is reported  
• 
AIS signal is received on the line  
• 
The configured module type does not match the actual module installed (in case of card 
removal, reset or failure) 
The minor alarms are caused by the following: 
• 
EED (excessive error degradation). The EED threshold can be selected by the user.  
• 
SD (signal degraded) condition, where the threshold can be selected by the user. However, the 
user can configure APS parameters to ignore the SD criterion.  
Note 
Minor alarms serve as flipping criteria only when flip upon signal degradation 
(flip-upon-sd) is enabled 
The working port always carries the traffic, as long as its total alarm weight does not exceed that of the 
protection. The user can force switching (flipping) to the other port by a manual flip command.  
The two ports in an APS group can be assigned priorities. Megaplex-4 will generate alarm messages to 
notify managers (supervision terminal, Telnet hosts, management stations, etc.) that protection switching 
from the high priority port to the low priority port, or vice versa, occurred.  
The recovery mode after a protection switching can be selected in accordance with the application 
requirements: 
• 
Non-revertive mode – the CL module will not automatically flip back after the failed port returns 
to normal operation, but only when the currently used port fails (that is, when its alarm weight 
exceeds that of the standby port). However, as explained above, the user can always initiate 
flipping back by a manual flip command. 
• 
Revertive mode – the CL module will flip back to the original port when it returns to normal 
operation (that is, its alarm weight is equal to, or lower than, that of the currently active port).  
To prevent switching under marginal conditions, the user can specify a restoration time (wait-to-
restore). This is the minimum interval before flipping back to the original port. During the restoration 
time, alarms with the same weight, or with lower weights, are ignored. As a result, the module starts 
7. Resiliency and Optimization 
evaluating the criteria for protection switching (flipping) only after the restoration time expires, thereby 
ensuring that another flip cannot occur before the specified time expires. 
However, if an alarm with a weight exceeding that of the alarm which caused flipping appears, 
immediate flipping will occur, even if the restoration time has not yet expired. 
Factory Defaults 
In Revertive mode, the wait-to-restore time is 300 sec.  
Configuring Automatic Protection Switching 
Adding and Removing an APS Group 
 To add and define an APS group: 
1. At the config> prompt, enter protection. 
The config>protection# prompt appears. 
2. Enter aps <group name>. The group name may consist of up to 80 alphanumeric characters. 
The APS group is defined and enabled and the  
config>protection>aps(<group name>)# prompt appears. 
 To remove an APS group: 
• 
At the config>protection# prompt, enter no aps <group name>. 
The APS group is removed. 
Binding Ports to an APS Group 
Before you can bind ports to the APS group, you have to first specify the desired operation mode.  
 To specify the operation mode: 
• 
At the config>protection>aps(<group name>)# prompt, enter  
oper-mode {uni-directional | optimized-1-plus-1 | compatible-1-plus-1}. 
You are now able to bind a port to the APS group. 
7. Resiliency and Optimization 
 To define the working ports for the APS group if ‘optimized-1-plus-1’ is selected: 
1. At the config>protection>aps <group name># prompt, enter  
bind working 1 sdh-sonet <slot><port>. 
Working port 1 is bound to the APS group. 
2. At the config>protection>aps <group name># prompt, enter  
bind working 2 sdh-sonet <slot><port>. 
Working port 2 is bound to the APS group. 
 To bind the working and protecting ports to the APS group if ‘compatible-1-plus-1’ or ‘uni-
directional’ is selected: 
1. At the config>protection>aps <group name># prompt, enter  
bind working sdh-sonet <slot><port>. 
The working port is bound to the APS group. 
2. At the config>protection>aps <group name># prompt, enter  
bind protection sdh-sonet <slot><port>. 
The protection port is bound to the APS group. 
 To configure the SDH/SONET APS: 
• 
At the config>protection>aps(group name)# prompt, enter all necessary commands according 
to the tasks listed below: 
Task 
Command 
Comments 
Activating the APS group 
no shutdown 
Using shutdown switches the APS to standby 
mode 
Defining operation mode of the 
APS 
oper-mode {uni-
directional | optimized-
1-plus-1 | compatible-1-
plus-1} 
 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Adding a working port to the APS 
group (compatible 1+1 and 
unidirectional modes)  
 
bind { working | 
protection } sdh-sonet 
<slot/port> 
 
Available for the compatible 1+1 and 
unidirectional modes  
Using no bind { working | protection } 
removes a port from APS group  
Note: When APS group contains ports from 
CL-A and CL-B (HW redundancy), the 
following restrictions apply : 
• E1/T1-I: must be configured on both CL 
modules as partners in the TDM group 
• VCG must be configured on both CL 
modules as partners of ERPS  
Adding a working port to the APS 
group (1+1 optimized bidirectional 
mode) 
 
bind working {1 | 2} sdh-
sonet <slot/port>  
Available for the 1+1 optimized bi-directional 
mode. 
Using no bind { working | protection } 
removes a port from APS group 
Enabling the reverting of the 
working and protection ports (not 
available in 1+1 optimized mode) 
revertive 
Using no revertive disables the reverting 
Defining the wait-to-restore period 
for the revertive recovery mode 
(the time to elapse after the link 
recovery before traffic 
switches back) 
wait-to-restore <1–720> 
The unit of time is seconds 
 
Enabling the flip of the two 
SDH/SONET ports upon signal 
degradation 
flip-upon-sd 
 
Using no flip-upon-sd disables the flip 
Denying access of all traffic signals 
to the protection port by issuing a 
"Lockout of protection" request, 
unless an equal protection switch 
command is in effect 
lockout-of-protection 
 
 
Available only in compatible 1+1 and 
unidirectional modes  
 
Clears all externally initiated 
switch commands and the WTR 
time  
clear 
 
 
Forced switching of traffic from the 
protection port to the working port 
(unless an equal or higher priority 
request has been issued)  
force-switch-to-working 
 
 
Since a forced switch has a higher priority 
than SF or SD on a working port, this 
command is carried out regardless of the 
current condition of the working port 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Forced switching of traffic from the 
working port to the protection 
port, unless an equal or higher 
priority switch command is in 
effect, or if an SF condition exists 
on the protection port. 
force-switch-to-
protection 
 
 
Manual switching of traffic from 
the protection port back to the 
working port, unless an equal or 
higher priority request is in effect 
manual-switch-to-
working 
 
 
Since a manual switch has lower priority than 
SF or SD on a working port, this command is 
carried out only if the working port is not in 
SF or SD condition. 
Forced switching of traffic from the 
working port to the protection 
port, unless a failure condition 
exists on the protection port or an 
equal/higher priority switch 
command is in effect 
manual-switch-to-
protection 
 
 
 
Viewing the Status of an APS Group 
This section illustrates the status display of an APS group created in 1+1 Optimized Bi-directional mode. 
 To view the APS group’s status: 
• 
At the config>protection>aps(<group name>)# prompt, enter show status. 
The APS group’s status appears. 
 
In this example, the APS group name is test. 
config>protection>aps(test)# show status 
Group 
--------------------------------------------------------------- 
Mode                  : Uni Directional 
Administrative Status : Up 
Current Working       : cl-b/1 
Rx K1K2               : 0x0010 
Tx K1K2               : 0x0010 
 
 
Ports 
--------------------------------------------------------------- 
Port       Admin    Status     Active 
 

## 7.3 DS0 SNCP (DS0-Bundle) Protection  *(p.562)*

7. Resiliency and Optimization 
cl-a/1     Up         Up         No 
cl-b/1     Up         Up         Yes 
Example 
 To add and configure an APS group: 
• 
APS group name – test 
• 
Working port – Port 2 of the module installed in slot cl-a 
• 
Protection port – Port 1 of the module installed in slot cl-a 
• 
Recovery mode – revertive 
• 
Wait-to-restore period – 200 seconds. 
#configure protection aps test bind working sdh-sonet cl-a/2 
config>protection>aps(test)#bind protection sdh-sonet cl-a/1 
config>protection>aps(test)#revertive 
config>protection>aps(test)#wait-to-restore 200 
 To delete APS group named test: 
#configure protection no aps test 
7.3 DS0 SNCP (DS0-Bundle) Protection  
The DS0 SNCP protection is sub-network connection protection for PDH networks.   
Applicability and Scaling 
This feature is available for the all VS and VS voice modules, except for the E1/T1 VS modules. 
The maximum total number of DS0 SNCP protection groups that can be configured for Megaplex-4 is 
256. Each VS module supports up to 256 DS0 SNCP protection groups.  
7. Resiliency and Optimization 
Benefits  
DS0 SNCP assures protection on the individual timeslot level. It provides higher availability for critical 
applications at the DS0 level, with fast protection switching time. 
Standards 
DS0 SNCP is RAD proprietary technology. 
Factory Defaults 
Megaplex-4 is supplied with DS0 SNCP protection disabled. Other parameter defaults are listed in the 
table below.  
Parameter  
Default Value 
revertive/no revertive 
no revertive 
wait-to-restore  
300 sec 
Functional Description 
The protected services are voice or data depending on the module on which the DS0 SNCP is configured 
(voice/serial/ds1-opt/ds0-g703) and on the uplink type (E1 or T1). 
A usual application for this type of protection requires that the same E1/T1 link is used to carry different 
types of services, some of which have to be protected and some do not have to.  
In the DS0 SNCP mechanism, each service in the loop is assigned two independent transmission routes. 
In case of a fault in current route, traffic is switched by the system automatically to the intact route. The 
diagram below shows a typical protection scheme.  
Switchover Criteria  
Switching criteria are presented with the following alarms:  
• 
lof – Loss of frame detected at ds0 bundle 
• 
card_mismatch – The configured module type does not match the actual module installed (in 
case of card removal, reset or failure) 
7. Resiliency and Optimization 
• 
 
 
DS0 SNCP Protection 
In Tx direction the data is duplicated by DS0 cross-connect in the CL module and broadcast to both 
Uplinks. In Rx direction the CL cross-connect is getting timeslot selection control from DS0 bundles in the 
module and the selected timeslots are forwarded to the I/O interface.  
Data is not passing via the DS0 bundles. The uplink module is not aware about redundancy so that any 
module type can be used in the application. Since the protection control and the data path are 
independent, the DS0 bundle and the user interface can reside on same module or on different 
modules. 
Timeslots with path overhead information received from two E1/T1 ports configured as protection 
partners, must be cross connected to the VS module where the DS0 bundle was allocated. 
The DS0 bundle is monitoring bits assigned for this node for path status.  
DS0 Bundle Ports 
To protect individual timeslots of E1/T1/E1-i/T1-i/DS1 ports of the relevant uplink modules, special 
entities called DS0 bundles must be created in Megaplex-4. These DS0 bundle ports are protected by the 
DS0 SNCP group redundancy. For description and instructions, refer to DS0 Bundle Ports in Chapter 5.  
Signaling Method 
DS0 SNCP controls the end-to-end path by the method of signaling bit control. This is configured by 
means of the signaling-method signaling-bit parameter. 
Tributary
Port
E1/T1#1
E1/T1#2
ds0-
bundle#1
ds0-
bundle#2
DS0
CC
7. Resiliency and Optimization 
For configuration, see DS0 Bundle Ports in Chapter 5.  
Local and External Service Protection 
The VS module can protect either local service on the same module or external service on another 
module (server mode).  
When working as a server with signaling-bit control, the ds0-bundle port must include service timeslot 
of at least one port (serial, voice, ds0-g703 or ds1-opt) of the VS module bound to it, while other 
protected ports can be from other modules.  
Control Bit 
In DS0 SNCP protection, each number of timeslots that are carrying the service between the two end-
points are protected by an extra overhead bit (control-bit in CLI) located in the protection timeslot. A 
synchronization pattern (FAS) is running over this bit to validate the end-to-end connectivity. 
Each VS module supports up to 128 DS0 bundles in the DS0 SNCP over data protection and up to 16 DS0 
bundles in the DS0 SNCP over signaling protection. To create protected service, two DS0 bundles are 
required. 
Each bit in the DS0 bundle can be used to protect one or more timeslots/services. 
If the uplink line type is G.732S or G.732S-CRC, TS 16 has four signaling bits and one of them can be 
defined as control bit.  
For configuration, see DS0 Bundle Ports in Chapter 5.  
Configuration Procedure  
If Megaplex-4 is an end-point device, the protection configuration consists of the following stages: 
I. 
Configure the service (serial/voice/ds1-opt/ds0-g703 to e1/t1 uplink) by DS0 cross-connect of 
the required timeslots.  
II. 
Configure another e1/t1 uplink. 
III. 
Configure a ds0 bundle on the VS module and bind it to the timeslots of the service in step 1. 
IV. 
Configure an additional ds0 bundle on the VS module and bind it to the timeslots of the second 
e1/t1 uplink (from step 2). 
7. Resiliency and Optimization 
V. 
Define the DS0 SNCP group with the two bundles configured in steps 3 and 4 as 
working/protection bundles. 
If Megaplex-4 is a transit node device, the protection configuration consists of the following stages: 
I. 
Configure the service between two intermediate links by DS0 cross-connect of the required 
timeslots.  
II. 
Configure a ds0 bundle on the VS module and bind it to the timeslots of the service (on the first 
link). 
III. 
Configure an additional ds0 bundle on the VS module and bind it to the timeslots of the service 
(on the second link). 
IV. 
Configure the service between two intermediate links by DS0 cross-connect of the required 
timeslots. The control TS must be configured as a voice type timeslot in both links. 
Configuring DS0 SNCP Protection  
 To add a DS0 SNCP protection group:  
1. Navigate to configure>protection#. 
2. Type ds0-group and enter a group number [1..256]. 
The configure>protection>ds0-group<group-id># prompt is displayed.  
 
Task 
Command 
Comments 
Administratively enabling a DS0 
group 
no shutdown 
Using shutdown disables the group 
Assigning a name to the group 
name <Alphanumeric string> 
Maximum name length is 32 characters 
Defining operation mode of the 
DS0 group 
oper-mode 1-plus-1 
The operation mode in always 1-plus-1.  
Adding working and protection  
ds0-bundles to the DS0 group   
bind  {working | protection} 
ds0-bundle  <slot>/<port> 
Using no bind working/protection removes 
the port from the group.  
Slot: 1..10 
Port: 1..128 
Enabling the reverting of the 
working and protection ports  
revertive 
 
Using no revertive disables the reverting 
 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Defining the wait-to-restore 
period (after the switching 
criteria are cleared, the time to 
elapse before traffic 
switches back) 
wait-to-restore <1–720> 
 
 
The unit of time is seconds: 1..300..720 
This field is active only when the protection 
mode is revertive.  
Forced switching of traffic from 
the protection port to the 
working port  
force-switch-to-working 
 
 
 
Forced switching of traffic from 
the working port to the 
protection port  
force-switch-to-protection 
 
 
Manual switching of traffic from 
the protection port back to the 
working port, unless a failure 
condition exists on the working 
port or an equal/higher priority 
switch command is in effect 
manual-switch-to-working 
 
 
 
 
 
Manual switching of traffic from 
the working port to the 
protection port, unless a failure 
condition exists on the 
protection port or an 
equal/higher priority switch 
command is in effect 
manual-switch-to-protection 
 
 
Clears the current command - 
force switch or manual 
clear  
Once the command is cleared, the module 
returns back to normal operation. 
Viewing the DS0 SNCP Protection Status  
This section illustrates the status display of a DS0 SNCP protection group. 
 To view the DS0 SNCP protection group status:  
• 
At the config>protection>ds0-group (<group number>)# prompt, enter show status. 
The protection group status appears. In this example, the DS0 SNCP protection group number is 
1.  
7. Resiliency and Optimization 
config>protection>ds0-group(1)# show status 
Group 
------------------------------------------------------------------------ 
Mode                  : 1+1 
Administrative Status : Up 
Last Command          : 
 
Bundles 
------------------------------------------------------------------------ 
          Port              Admin Oper            Active 
------------------------------------------------------------------------ 
Protection ds0 bundle 5/1   Up    Down            -- 
Working    ds0 bundle 4/1   Up    Up              Yes 
Example. DS0 SNCP protects timeslots of serial and voice ports over CL E1-i 
link 
In this example we show how DS0 SNCP protects the following timeslots over CL module E1-i link: 
• 
Data TS from serial data module (VS-12) ; the serial channel data rate is 256 kbps (4 TS) 
• 
Voice TS from serial data module (VS-6/FXS). 
These tasks are done with the signaling-method parameter set to signaling-bit.  
## SLOT configuration## 
exit all 
config slot ps-a card-type power-supply ps 
config slot cl-a card-type cl cl2-622gbe 
config slot 4 card-type versatile vs-12 
config slot 8 card-type versatile vs-6-fxs 
 
## SDH_SONET configuration## 
exit all 
config port sdh-sonet cl-a/1 no shutdown 
config port sdh-sonet cl-a/2 no shutdown 
 
config port e1-i cl-a/1 no shutdown 
config port e1-i cl-a/1 line-type g732s 
config port e1-i cl-a/1 out-of-service signaling force-busy 
 
config port e1-i cl-a/2 no shutdown 
config port e1-i cl-a/2 line-type g732s 
config port e1-i cl-a/2 out-of-service signaling force-busy 
7. Resiliency and Optimization 
 
config cr sdh-sonet vc12-vt2 cl-a/1/1/1/1/1 e1-i cl-a/1 
config cr sdh-sonet vc12-vt2 cl-a/2/1/1/1/1 e1-i cl-a/2 
 
##VS-12 Serial port (Creating serial service)## 
exit all 
config port serial 4/1 no shutdown 
config port serial 4/1 encapsulation-mode none 
config port serial 4/1 rate 4 x 64 
config port serial 4/1 interface rs-232 
 
##XC (serial ports) 
config cr ds0 e1-i cl-a/1 ts [1..4] serial 4/1 bi-direction 
commit 
 
## VS6-FXS Voice port (Creating voice service) 
exit all 
config port voice 8/1 no shutdown 
config port voice 8/1 signaling cas 
config port voice 8/1 analog-signaling-profile "sig_over_a_bit" 
 
##XC (voice ports) 
config cr ds0 e1-i cl-a/1 ts 31 voice 8/1 bi-direction 
 
############################################################################# 
DS0 SNCP protects Data TS from VS-12 over CL-E1-I link - Serial channel data rate is 4 TS 
############################################################################# 
 
### Configuring DS0_Bundle ports 4/1 and 4/2 
exit all 
config port ds0-bundle 4/1 no shutdown 
config port ds0-bundle 4/1 signaling-method signaling-bit 
config port ds0-bundle 4/1 bind e1-i cl-a/1 time-slot 1..4 
config port ds0-bundle 4/1 control-bit ts 1 bit d 
 
config port ds0-bundle 4/2 no shutdown 
config port ds0-bundle 4/2 signaling-method signaling-bit 
config port ds0-bundle 4/2 bind e1-i cl-a/2 time-slot 1..4 
config port ds0-bundle 4/2 control-bit ts 1 bit d 
7. Resiliency and Optimization 
 
#### Configuring DS0-Group Protection between DS0_Bundle ports 4/1 and 4/2### 
 
exit all 
config protection ds0-group 1  
bind working ds0-bundle 4/1 
bind protection ds0-bundle 4/2 
oper-mode 1-plus-1 
revertive 
wait-to-restore 1 
no shutdown 
exit 
################################################################# 
DS0 SNCP protects Voice TS from VS-6/FXS module over CL-E1-I link  
################################################################# 
 
### Configuring DS0_Bundle Ports 8/1 and 8/2 
exit all 
config port ds0-bundle 8/1 no shutdown 
config port ds0-bundle 8/1 signaling-method signaling-bit 
config port ds0-bundle 8/1 bind e1-i cl-a/1 time-slot 31 
config port ds0-bundle 8/1 control-bit ts 31 bit d 
 
config port ds0-bundle 8/2 no shutdown 
config port ds0-bundle 8/2 signaling-method signaling-bit 
config port ds0-bundle 8/2 bind e1-i cl-a/2 time-slot 31 
config port ds0-bundle 8/2 control-bit ts 31 bit d 
 
##### DS0-Group Protection  ##### 
exit all 
config protection ds0-group 2 
bind working ds0-bundle 8/1 
bind protection ds0-bundle 8/2 
oper-mode 1-plus-1 
revertive 
wait-to-restore 1 
no shutdown 

## 7.4 Ethernet Group Protection  *(p.571)*

7. Resiliency and Optimization 
Configuration Errors 
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 
DS0 SNCP Protection Configuration Error Messages  
Code Type  
Syntax 
Meaning 
812 
 
Error 
PORT CAN BE BOUND TO 
LINK WITH E1 MF ONLY  
The DS0 bundle can be bound only to E1/E1-i/DS1 multiframe 
link (line-type g732s or g732s-crc) 
813 
 
Error 
PORT CAN'T BE BOUND TO 
LINK WITH TDM GROUP   
A ds0-bundle port cannot be bound to a link which is a 
member in tdm-group protection 
814 
 
Warning PORT IS NOT MEMBER OF 
ACTIVE DS0-GROUP 
If a ds0-bundle is defined it must be a member of an active (no 
shutdown) DS0 protection group. 
815 
 
Error 
CONTROL TS PAYLOAD 
BITS XC TO DIFF PORTS 
 
When using DS0-SNCP (using signaling bit control), if the 
control TS is configured as a split TS, only one port can be 
cross-connected with it. 
7.4 Ethernet Group Protection 
Megaplex-4 supports 1+1 protection (redundancy) for Ethernet, protecting Ethernet and packet traffic 
against transmission failures on the SDH/SONET, T3 and E1/T1 links.  
Applicability and Scaling 
This feature is available for the following modules and technologies:  
• 
SDH/SONET (CL.2 modules) – GFP encapsulation 
• 
E1/T1 (VS-16E1T1-EoP modules) – GFP encapsulation  
• 
T3 (T3 modules) – GFP encapsulation 
Note 
Ethernet Group Protection is not supported in CL.2/DS0 modules. 
7. Resiliency and Optimization 
Standards 
Ethernet group protection is RAD proprietary technology.  
Functional Description  
Any pair of logical MACs can be configured as an Ethernet protection group, even if the entities bound 
to them have different capacity, different encapsulation methods, and/or different parameters. Only the 
wait-to-restore delay must be the same. 
To use Ethernet group protection, both the primary (working) logical MAC and the secondary 
(protection) logical MAC must be assigned bandwidth (mapped) on the particular links. In other words, 
the lower-hierarchy entities on these desired links must be bound to this logical MAC. Provisioning 
appropriate trails through the network ensures that in case of a fault anywhere along the primary group 
path, its traffic will be automatically switched to the standby group and will follow a different path 
through the SDH/SONET/T3/E1/T1 network, thereby ensuring that the payload can still be transported 
end-to-end. 
Depending on the desired protection level, the protection partners can be mapped to different links on 
the same modules, or to links on the different modules.  
To prevent switching under marginal conditions, the user can specify a wait-to-restore time, which is the 
minimum interval before flipping back to the original port. However, if a more severe alarm appears, 
immediate flipping will take place, even if the wait-to-restore time has not yet expired.  
The following figures illustrate how Ethernet groups are bound to the physical layer for Ethernet over 
SDH/SONET, Ethernet over T3 and Ethernet over E1/T1, respectively. 
 
7. Resiliency and Optimization 
Bind 1:1
Logical MAC
32
Logical MAC
1
Flow
Egress/Ingress Port
GFP 1..32
VCG 
1..32
Bind 1:1
VC12/VT1.5
VC3/STS-1
VC4/STS-3C
VC4-4C/
STS-12C
Bind 1:n
Bind 1:1
VCAT No
ETH Group
OR
 
Ethernet Group Protection over SDH/SONET  
 
 
7. Resiliency and Optimization 
Bind 1:1
Logical MAC
16
Flow
Egress/Ingress Port
GFP 1
GFP 16
VCG 1..16
Bind 1:1
T3
T1
Bind 1:n
Bind 1:1
ETH Group
OR
Logical MAC
1
Bind 1:1
  
 
Ethernet Group Protection over T3  
7. Resiliency and Optimization 
 
Ethernet Group Protection over E1/T1 (VS-16E1T1-EoP Modules)  
Protection Modes 
The Ethernet group protection mode is always 1+1 and operates as follows: 
• 
During normal operation, the payload is directed to the primary logical MAC, and transmitted 
only over the bandwidth assigned to this group.  
Note 
Only the primary (working) logical MAC can be included in a flow. The 
protection logical MAC will not appear in the list of available bridge ports. 
 
 
 
Bind 1:1
Logical MAC
16
Flow
Egress/Ingress Port
GFP 1
GFP 16
E1-i/T1-i
E1/T1
Bind 1:n
Bind 1:n
ETH Group
OR
Logical MAC
1
Bind 1:1
Bind 1:1
VCG 1
VCG 16
Bind 1:1
7. Resiliency and Optimization 
• 
If an alarm condition is detected on the entities bound to the working logical MAC, the payload 
is directed to the protection logical MAC, and transmitted over its bandwidth. The alarm criteria 
taken into consideration for protection switching include physical port failures and VCG failures. 
When using LCAS, this also includes a decrease in available bandwidth below the specified 
minimum.  
The recovery mode after a redundancy switching is always revertive – which means that the traffic will 
be automatically redirected back to the original group when it returns to normal operation.  
Switchover Criteria  
With Ethernet group protection, switchover criteria depend on the ports participating in protection. This 
section lists the alarms affecting the protection switchover for different Megaplex-4 ports. 
Alarms on VCG ports are: 
• 
minimum_members_tca (with LCAS) – Number of minimum members below threshold 
• 
rx_trail_failure (without LCAS) –Rx trail failure 
• 
card_mismatch – The configured module type does not match the actual module installed (in 
case of card removal, reset or failure) 
Configuring Ethernet Protection Group 
Adding and Removing an Ethernet Protection Group 
 To add and define an Ethernet protection group: 
1. At the config> prompt, enter protection. 
The config>protection# prompt appears. 
2. Enter ethernet-group <group number>.  
The Ethernet protection group is defined and enabled and the  
config>protection>ethernet-group( <group number>)# prompt appears. 
 To remove an Ethernet protection group: 
• 
At the config>protection prompt, enter no ethernet-group <group number>. 
The Ethernet protection group is removed. 
7. Resiliency and Optimization 
Binding Ports to an Ethernet Protection Group  
 To configure the Ethernet group protection: 
• 
At the config>protection>ethernet-group(group number)# prompt, enter all necessary 
commands according to the tasks listed below: 
Task 
Command 
Comments 
Activating the Ethernet protection 
group  
no shutdown 
Using shutdown switches the Ethernet 
protection group to standby mode 
Adding a working/protection port 
to the Ethernet protection group   
bind  {working | protection} 
logical-mac <slot>/<port > 
Using no bind logical-mac 
<slot>/<port> removes a port from 
Ethernet protection group 
Port number is as follows: 
• 1..32 for SDH/SONET 
• 1..16 for T3 modules 
• 1..16 for VS-16E1T1-EoP modules. 
If TDM group protection is configured 
for a T3 port, the Ethernet group 
protection is also automatically 
created on all the open Logical MAC 
ports belonging to this T3 module. The 
Logical MAC members belonging to 
such a group have the same numbers. 
The numbers of these Ethernet 
protection groups start from 200.  
Specifying a wait-to-restore 
timeout in seconds       
wait-to-restore <time in 
seconds> 
1..300..720  
If this Ethernet protection group is 
automatically created upon 
configuring TDM group protection in a 
T3 module, its wait-to-restore value is 
the same as for the TDM group 
protection configured on the T3 
module. 
Viewing the Status of an Ethernet Protection Group  
This section illustrates the status display of an Ethernet protection group. 

## 7.5 Ethernet Ring Protection (ERP)  *(p.578)*

7. Resiliency and Optimization 
 To view the Ethernet protection group status: 
• 
At the config>protection>ethernet-group (<group number>)# prompt, enter show status. 
The Ethernet protection group status appears. In this example, the Ethernet protection group 
number is 1. 
config>protection# ethernet-group 1 
config>protection>eth-group(1)# show status 
Ports 
--------------------------------------------------------------- 
           Port                   Admin    Oper     Active 
Working    Logical MAC cl-a/1     Up       Up       -- 
Protection Logical MAC cl-a/2     Up       Down     Yes 
Configuration Errors  
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 
Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
608  
Error 
ILLEGAL PROTECTION GROUP 
DEFINITION 
Ethernet group protection over SDH/SONET is not supported 
in CL.2/A modules. 
See also Error 608 in PW Protection and Error! Reference 
source not found. for additional meanings. 
N615 
Error 
ETHERNET GROUP MEMBERS 
SHOULD BE THE SAME  
 
Working and protection logical MACs cannot be bound to 
entities of different types: they must be both bound either 
to gfp or hdlc ports.       
7.5 Ethernet Ring Protection (ERP)  
A G.8032 Layer-2 Ethernet ring is used by  for Ethernet traffic protection. This technology builds a logical 
ring, defined as a set of IEEE 802.1-compliant bridges, and protects against link and node failures. 
Megaplex-4 supports a total of 5 rings or sub-rings per chassis.  
7. Resiliency and Optimization 
Applicability and Scaling 
This feature is available for the following modules and ports: 
• 
CL.2 and M-ETH modules – between GbE ports 
• 
CL.2 – VCG ports 
The ERP functionality is supported with the following conditions: 
• 
When a CL.2/A module with advanced carrier capabilities is installed in the chassis 
• 
CL modules: Between ports on the same module as well as between CL-A and CL-B ports 
• 
M-ETH module: Between ports located on the same module 
• 
Sub-50 ms switching is guaranteed for up to 16 nodes per ring.  
Standards 
ITU-T G.8032/Y.1344, Y.1731 
Benefits 
G.8032 revertive rings provide sub-50 ms protection for Ethernet traffic and prevent loops at the 
Ethernet layer. 
Factory Defaults 
No Ethernet protection rings are configured in the system by default. Other parameter defaults are 
listed in the table below.  
Parameter  
Default Value 
bridge 
0 
east-port   
0 
west-port   
0 
force-sf  
no force-sf  
7. Resiliency and Optimization 
Parameter  
Default Value 
r-aps vlan  
0 
vlan-priority   
7 
mel   
255 
rpl/no rpl 
no rpl 
timers guard  500  
500 
holdoff   
0 
passthrough-vlan 
no passthrough vlan (added/dropped VLANs at the 
local ring node, as well as passthrough VLANs, must be 
configured with explicit flows into the bridge, and each 
one is assigned a bridge broadcast domain (device 
resource)) 
port-type  east 
node-port 
port-type  west 
node-port 
interconnection-node    
 no interconnection-node    
backward-compatibility 
no backward-compatibility 
Functional Description 
Ethernet Ring Protection technology provides a scalable solution for low-cost traffic protection and rapid 
service restoration, with SDH/SONET-type resilience. It is built on traditional Ethernet MAC (IEEE 802.3) 
and bridging (IEEE 802.1) functions. It is independent of any physical-layer technologies and can be 
utilized in any carrier’s network. 
In ERP every ring node uses heartbeat messaging to determine availability of its neighbor. When a link 
failure occurs, it is detected via LOS or heartbeat messaging. Upon failure, node forwarding information 
is recalculated to ensure that data traffic reaches its destination, using alternative path.  
7. Resiliency and Optimization 
Ring ports can reside on the GbE Ethernet ports belonging to the same CL or I/O card, providing port 
redundancy. In addition, they can reside on the ports belonging to different CL cards, providing port 
redundancy. In total, Megaplex-4 supports up to 5 rings or sub-rings.  
Ring Topology 
Megaplex-4 supports different ring topologies, including single and interconnected (ladder) ring 
topologies.  
 
Single Ethernet Ring 
 
Interconnected Ethernet Rings 
R-APS Messaging 
Ethernet ring protection is achieved by means of a dedicated protocol, Automated Protection Switching 
(APS). Every ring link is bound by two adjacent nodes. At any time, traffic flows on all, but one of the ring 
links. This link is called the ring protection link (RPL). Under normal conditions this link is blocked. RPL is 
controlled by a single node called an RPL owner, which prevents traffic from using the RPL. When a 
failure is detected, the RPL owner unblocks the RPL port, allowing the RPL to be used for traffic. 
R-APS messages require a designated transmission channel (R-APS channel), which is separated from the 
service traffic channel. An R-APS channel is configured using a separate dedicated VLAN to enable the R-
Major Ring
Sub-Ring
7. Resiliency and Optimization 
APS messages to be handled differently from the service traffic. The R-APS channel and service traffic 
blocking is performed via VID filtering by the bridge. 
Mechanism of Operation  
Every failure along the ring triggers an R-APS (SF) (R-APS Signal Fail) message along both directions from 
the nodes adjacent to the failed link. Before sending the R-APS, these nodes block the ports facing the 
failed link. On receiving these messages, the RPL owner unblocks the RPL port. An SF message is 
triggered even if only one node adjacent to the failed link recognizes the failure. Moreover, to overcome 
scenarios in which link failures are not recognized via LOS (Loss of signal), ERPS can also use the standard 
Ethernet OAM 802.1ag Continuity Check Messages (CCMs) to expose the failure to the two adjacent 
nodes.  
During a recovery phase, when a failed link is restored and a node continually detects a Clear SF, it sends 
an R-APS No Request (NR) message and keeps the failed port blocked. When receiving the R-APS (NR), 
the RPL owner starts its Wait-To-Restore (WTR) timer. When that timer expires, it blocks the RPL port 
and sends RAPS (NR, RB) (R-APS no request, root blocked) messages in both directions of the ring. Nodes 
receiving the R-APS (NR, RB) message flush their learning table, unblock their blocked ports, and return 
to idle state. 
The following figure illustrates a stable-state Ethernet ring with blocked RPL to prevent a loop. Each 
node is monitored, using Ethernet CCM OAM messages, and the ring protection is triggered by loss of 
continuity or server layer failure, as defined in Y.1731.  
 
Fault-Free ERP 
Administrative Commands 
If there is a need to intervene into ERP operation for maintenance or any other reason, the operator can 
issue a forced or manual switch command. 
RPL Owner
CCM
CCM
CCM
CCM
CCM
CCM
Traffic is Blocked
7. Resiliency and Optimization 
• 
Forced Switch (FS) – This command forces a block on the ring port where the command is 
issued. It can be issued even if an SF condition exists on the ring. Multiple force switch 
commands can be supported per ring instance but only one per node. 
• 
Manual Switch (MS) – In the absence of a failure or FS, this command forces a block on the ring 
port where the command is issued. The manual switch command can be applied to a single ring 
node only. When the command is active, all ring nodes shift to the manual switch mode.  
• 
Clear switch command clears all existing force and manual switch command on the ERP. 
Note 
The manual and forced switch commands are temporary commands and do 
not permanently change the location of the RPL. 
Passthrough VLANs 
Passthrough VLANs over the ring are those VLANs that are not added/dropped to the ring at the local 
ring node (Megaplex-4), but only traverse via the ring node (East to West or vice versa).  
By default, added/dropped VLANs at the local ring node, as well as passthrough VLANs, must be 
configured explicitly with flows into the Bridge, and each one is assigned a bridge broadcast domain 
(device resource).  
Megaplex-4 ring configuration supports a passthrough attribute, which automatically assigns a 
ring/bridge bypass (East to West, West to East) for all passthrough traffic (i.e. all traffic other than the 
local added/dropped VLANs  which use bridge broadcast domains).  
As they do not go through the bridge and does not use Megaplex resources, Megaplex-4 allows an 
unlimited number of passthrough VLANS to enter the ring, and does not require explicit flows to the 
bridge of these passthrough VLANs. Added/dropped VLANs at the local ring node still need to be 
configured with explicit flows to the bridge. The number of added/dropped VLANs is limited, because 
they go through the bridge and use up its resources (bridge broadcast domains).  
Use of passthrough VLANs upscales the ring capacity – an unlimited number of passthrough services can 
travel through the ring; there is only a limit to the number of ring services added/dropped at the local 
ring node.  
This configuration applies only for the main ring over CL GbE Ethernet ports. It is not available for 
subrings at the intermediate node or rings over VCG ports. 
7. Resiliency and Optimization 
Multiple Rings 
Multiple rings with a common link are usually referred to as ladder network (see figure below). In such 
networks a common VLAN is shared on more than one physical ring. For example, a user connected to 
node E is communicating with a user connected to node A over the same VLAN. 
Ring topology includes a physical link between nodes G and C. It belongs to the major ring and is used by 
the sub-ring.  
 
Physical Ladder Topology 
 
Major Ring and Sub-Ring 
The following terms are commonly used for describing ladder ring topology: 
• 
Interconnection nodes – Ring nodes that are common to both interconnected rings (nodes C and 
G). 
Virtual Channel
Major Ring
Sub-Ring
A
B
C
D
E
H
G
F
Major Ring
A
B
C
H
G
Sub-Ring
C
D
E
G
F
7. Resiliency and Optimization 
• 
Major ring – An Ethernet ring that controls a full physical ring and is connected to the 
interconnection nodes on two ports (ring A-H-G-C-B) 
• 
Sub-ring –An Ethernet ring that is connected to a major ring at the interconnection nodes. By 
itself, the sub-ring does not constitute a closed physical ring. A sub-ring is connected to the 
interconnection nodes on only one port (ring C-D-E-F-G). Link C–G is not a part of the sub-ring 
and it is controlled by the major ring. Megaplex-4 supports up to four sub-rings per major ring. 
• 
R-APS virtual channel – The R-APS virtual channel is the R-APS channel connection between two 
interconnection nodes of a major ring over a network. 
In a stable state the rings have two RPL owners that prevent the traffic from looping in the network 
(nodes E, A). When a non-shared link fails in the network, the RPL owner that controls the ERPS instance 
containing that link unblocks the RPL port while the distant RPL port, which is not a part of this instance, 
remains blocked. For example, if link G-F fails, only node E unblocks its RPL port, while node A does not 
change the state of its RPL port. 
If a shared link fails (link G-C), the RPL owner of the main ring (node A) unblocks its port; however, the 
RPL port of the sub-ring (node E) remains blocked since that link is declared as virtual channel for this 
ring. 
Timers 
The following timers are used to facilitate ERP operation: 
• 
Wait-to-Restore (WTR) – Period of time used by RPL owner to verify that the ring has stabilized 
before blocking the RPL after signal recovery. 
• 
Guard – Period of time during which all received A-RPS messages are ignored by the ERP 
mechanism. This prevents the ring nodes from receiving outdated A-RPS messages circulating 
the network. 
• 
Hold-off – Period of time during which the underlying Ethernet layer attempts to filter out 
intermittent link faults before reporting them to the ERP mechanism. 
Switchover Criteria  
With ERP, switchover criteria depend on the ports participating in protection: either VCG ports or GbE 
ports of Megaplex-4.  
Alarms on VCG Ports: 
• 
minimum_members_tca (with LCAS) – Number of minimum members below threshold 
• 
rx_trail_failure (without LCAS) – Rx trail failure 
7. Resiliency and Optimization 
• 
card_mismatch – The configured module type does not match the actual module installed (in 
case of card removal, reset or failure) 
Alarms on GbE ports: 
• 
loc (with CCM OAM) –Loss of continuity  
• 
los –loss of signal on the Ethernet port 
• 
card_mismatch – The configured module type does not match the actual module installed (in 
case of card removal, reset or failure) 
ERP over LAG  
Ethernet Ring Protection (ERP) can be configured over a LAG for the GbE ports of the same CL module. 
ERP over LAG provides two points of failure redundancy rather than the single point of failure 
redundancy, as shown in the diagram below. 
 
ERP over LAG  
This type of the ERP configured is the same as of a standard ERP. A LAG is implicitly configured based on 
the flows. 
If the LAG is down, a service failure is triggered. A service failure can also be triggered based on OAM 
CCM-LOC.  
7. Resiliency and Optimization 
Note 
This OAM CCM-LOC must be defined on the related LAG (not on the GbE port 
bound to the LAG) 
 To configure an ERP over LAG: 
1. Create the LAG. See Error! Reference source not found.. 
2. Create the ring. See Error! Reference source not found.. 
ERP Configuration  
Configuring ERP  
 To configure ERP: 
1. In the configure>protection# prompt, enter erp followed by ring number  
(1–5). 
An ERP instance with is created and the config>protection>erp(1)# prompt is displayed.  
2. Configure the ERP as illustrated and explained below.  
Note 
Using no before erp (ERP_number) deletes an ERP instance. 
 
Task 
Command 
Comments 
Making the ring 
compatible with previous 
ERP implementations 
backward-compatibility 
no backward-compatibility 
This parameter cannot be changed when ERP is 
active. To change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Assigning the node to a 
bridge instance 
bridge <1–11> 
1 is always used for CL-A bridge,  
2..11 –for bridges on M-ETH modules 
This parameter cannot be changed when ERP is 
active. To change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
Forcing a signal failure 
to  initiate the Ethernet 
Ring protection 
mechanism  
force-sf {east | west} 
 
no force-sf cancels the command 
 
Defining ERP node as an 
interconnection node, 
sharing more than one 
ring 
interconnection-node 
no interconnection-node 
This parameter cannot be changed when ERP is 
active. To change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
Defining a bridge port as 
an East port of ERP node 
east-port 
<bridge_port_number> 
1..84  for bridge 1  
1..9  for bridges 2..11  
Sub-rings have East ports only 
This parameter cannot be changed when ERP is 
active. To change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Defining a bridge port as a 
West port of ERP node 
west-port 
<bridge_port_number> 
1..84  for bridge 1  
1..9  for bridges 2..11  
Sub-rings do not have West ports 
This parameter cannot be changed when ERP is 
active. To change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
Defining node port type in 
relation to RPL owner 
port-type owner {east | west} 
port-type neighbor {east | 
west} 
port-type next-neighbor {east 
| west} 
port-type node-port 
rpl – RPL owner 
neighbor – port directly connected to RPL owner 
next-neighbor – port connected to RPL owner via 
neighbor 
node-port – regular ring port, which is not 
connected to RPL owner 
These parameters cannot be changed when ERP 
is active. To change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
Configuring dedicated 
VLAN for R-APS messages 
r-aps [vlan <1–4094>] [mel 
<0–7>] 
 
R-APS settings must be the same for all ring 
members 
MEL – Dedicated Maintenance Entity Group Level 
for R-APS messages 
This parameter cannot be changed when ERP is 
active. To change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Configuring the revertive 
mode 
revertive 
 
This mode is relevant only to the RPL owner 
node. 
In the revertive mode, after condition causing the 
switch is cleared, traffic is blocked at the RPL 
owner and restored to the idle state (after WTR 
timer has expired). 
After the node has entered the state in revertive 
mode, use the Clear command to exit the state. 
no revertive enables non-revertive mode (system 
does not switch to idle state) 
This parameter cannot be changed when ERP is 
active. To change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
Enabling propagation of 
Signal Failure (SF) 
condition from the 
Ethernet OAM service 
layer  
sf-trigger {east | west} mep 
<md-id> <ma-id> <mep-id> 
no sf-trigger {east | west} 
Before enabling SF propagation, verify that 
relevant CFM parameters have been configured. 
MEPs used for SF propagation cannot reside on 
R-APS VLAN; they must be bound to data VLANs 
only. 
Adding a short description 
of the ring 
description <string> 
Up to 80 characters 
Using no description removes the description. 
Adding a short description 
of the East or Weat port 
port-description {east | west} 
<string> 
Up to 80 characters 
Using no description removes the description. 
Connecting previously 
defined sub-ring to a 
major ring  
sub-ring <ring_number> 
no sub-ring 
This option is available for major rings only. The 
sub-ring number must be lower than the number 
of the major ring it is assigned to. 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Defining wait-to restore 
period for RPL owner 
wait-to-restore <60–720> 
Wait-to-restore timer defines period of time used 
by RPL owner to verify that the ring has stabilized 
before blocking the RPL after signal recovery. The 
WTR timer is configured in 60-sec. steps.  
This parameter cannot be changed when ERP is 
active. To change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
Note: In case both ERP over SDH and ERP over 
Ethernet are configured with the same WTR, 
redundancy time increases. In this case it is 
recommended to configure different WTR values 
for each ring.  
Blocking the East or West 
port of a ring node  
manual-switch {east-port | 
west-port } 
The manual switch command can be applied to a 
single ring node only. When the command is 
active, all ring nodes shift to the manual switch 
mode.  
Enabling passthrough 
VLANs  
passthrough-vlan  
no passthrough-vlan 
Configures all VLANs, excluding localy 
added/dropped VLANs, as passthrough VLANs. 
Such VLANs bypass the bridge and do not require 
explicit flow configuration into the bridge, thus 
not using bridge broadcast domain resources.  
Enter no passthrough-vlan (default) to use the 
regular mode, where both added/dropped VLANs 
at the local ring node and passthrough VLANs 
must be configured explicitly with flows into the 
device bridge and are assigned each a bridge 
broadcast domain (device resource). 
This configuration applies only for main ring over 
CL GbE ports. 
Passthrough-vlan command is not applicable to 
logical mac ports.  
Blocking the East or West 
port of a ring node 
force-switch {east-port | 
west-port} 
Multiple force switch commands can be 
supported per ring instance, but only one is 
supported per node. 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Clearing the existing 
switch commands 
clear 
 
Administratively enabling 
the ERP interface 
no shutdown 
To avoid traffic loops, always enable Ethernet 
ports only after enabling Ethernet rings. 
Using shutdown disables the ERP. 
Defining guard and hold-
off periods in msec  
timers [guard <10–2000>] 
[holdoff <0–10000]  
Guard timer is used by the ERP mechanism to 
prevent ring nodes from receive outdated R-APS 
messages. While the guard timer is active, all 
received R-APS messages are ignored by the 
node. The guard timer is configured in 10-ms 
steps. Its recommended value for all ring nodes is 
2 sec. 
Hold-off timer is used by Ethernet layer to filter 
out intermittent faults. Faults are reported to the 
ERP mechanism only after the hold-off timer 
expires. The guard timer is configured in 100-ms 
steps. 
This parameter cannot be changed when ERP is 
active. To change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
Displaying ERP status 
show status 
 
Displaying ERP statistics 
show statistics 
 
Clearing ERP statistics 
clear statistics 
 
Displaying ERP Status 
You can display current status of configured ERP entity. 
 To display ERP status: 
• 
In the config>protection>erp(erp_number)$ prompt, enter show status. 
The ERP status is displayed. 
7. Resiliency and Optimization 
config>protection>erp(5)# show status 
Bridge Number : 1            East Port  : 1    West Port  : 2 
RPL Link      : West 
Ring State    : Protection 
 
East Port Status : Block R-APS and Data  
Local SF Source  : Server Layer 
West Port Status : Forward               
Local SF Source  : OK 
The ERP status provides information on: 
 
Bridge number 
 
Bridge ports assigned to be East and West ring ports 
 
RPL link: East or West ring ports 
 
Ring state: 
 
Init – The node is not yet participating in the ring 
 
Idle – The node is performing normally (there is no link failure on the ring). In this state, 
traffic is unblocked on both ring ports, except for the RPL owner node, which blocks the 
RPL port (the other RPL owner port is unblocked). 
 
Protection – A failure occurred on the ring. A not-owner node have traffic blocked on 
the ring port that connects to the failed link. The RPL owner, if it is not at one end of the 
failed link, unblocks the RPL port so both ports are active. 
 
East/West Port Status: 
 
Forward – Port is forwarding data 
 
Blocked – Port is blocked 
 
East/West Port Local SF Source – Local Signal Failure source: 
 
Server Layer 
 
OAM CFM 
 
Admin 
Displaying ERP Statistics 
When the G.8032 Ethernet Ring Protection (ERP) is enabled, Megaplex-4 allows collecting statistics on R-
APS messages sent and received by the East and West ports. 
 To display ERP statistics: 
• 
In the config>protection>erp(erp_number)$ prompt, enter show statistics. 
7. Resiliency and Optimization 
The ERP statistic counters are displayed. 
config>protection>erp(1)$ show statistics 
East Port 
---------------------------------------------- 
R-APS Message Rx Frames  Tx Frames 
SF            1         51 
NR            0          0 
NR,RB         0          0 
Total Valid   0          0 
Total Errors  0          0 
 
West Port 
---------------------------------------------- 
R-APS Message Rx Frames  Tx Frames 
SF            1          51 
NR            0          0 
NR,RB         0          0 
Total Valid   0          0 
Total Errors  0          0 
ERP Statistic Counters 
Counter 
Description 
R-APS SF Message Tx/Rx 
Total number of R-APS Signal Fail (SF) messages received or transmitted by 
East/West port.  
Received R-APS Signal Fail message indicates a failed port in the ring. 
Transmitted R-APS Signal Fail message indicates a failed port in the node. 
R-APS NR Message Tx/Rx 
Total number of R-APS No Request (NR) messages received or transmitted 
by East/West port.  
Received R-APS No Request message indicates absence of failed ports in 
the ring.  
Transmitted R-APS No Request message indicates that the node fixed its 
failed port. 
R-APS NR, RB Tx/Rx 
Total number of R-APS No Request (NR), RPL Blocked (RB) messages 
received or transmitted by East/West port.  
Received R-APS No Request, RPL Blocked message indicates that RPL port is 
blocked and all other not-failed blocked ports are unblocked in the ring. 
Transmitted from the RPL No Request, RPL Blocked message indicates that 
RPL port is blocked. 
Total Valid Rx/Tx 
Total number of valid R-APS messages received or transmitted by 
East/West port 
Total Errors Rx/Tx 
Total number of errored R-APS messages received or transmitted by 
East/West port 
7. Resiliency and Optimization 
Example 
The figure and the script below illustrate configuration a G.8032v2 ring over the CL.2 and M-ETH module 
ports. 
 
 ERP Configuration 
 To configure the ERP: 
1. Assign previously configured queue groups to module ports. 
2. Add three bridge ports. 
3. Define bridge port VLAN membership for bridge ports that are not ring members: 
 
BP 3 – member of VLAN 500  
4. Configure the ring: 
 
BP 1 – East port 
 
BP 2 – West port, RPL owner 
 
R-APS VLAN – 200 
 
Data VLAN – 500 
5. Configure two management and data flows (red flows in the figure): 
 
Classifier profile for VLAN 500  
Bridge
M-ETH 
Module
Ethernet 
Ring
East
Port 1
BP 3
BP 1
West
(RPL Owner)
BP 2
GbE
Port 2
CL-A
GbE 
Port 1
Flow 2
Flow 1
Flow 3
VLAN
500
7. Resiliency and Optimization 
 
Configure flows 1, 2 between the CL.2 ports and BPs 
6. Configure one data flow (blue flow in the figure): 
 
Classifier profile for VLAN 500 
 
Configure the data flow 3. 
7. Enable the CL and M-ETH module ports. 
# exit all 
# config slot 3 card-type ethernet m8eth 
# 
#************Configuring_ Shaper_Profiles and Queue_Group_Profiles ********* 
# configure qos 
config>qos# shaper-profile b-s 
config>qos>shaper-profile(b-s)$ bandwidth cir 50000 
config>qos>shaper-profile(b-s)$ exit 
config>qos# queue-group-profile b-s 
config>qos>queue-group-profile(b-s)$ queue-block 0/1 
config>qos>queue-group-profile(b-s)>queue-block(0/1)$ profile DefaultQueue1 
config>qos>queue-group-profile(b-s)>queue-block(0/1)$ shaper profile b-s 
config>qos>queue-group-profile(b-s)>queue-block(0/1)$ exit all 
 
#***********Enabling_Ports and Assigning Queue Group Profiles*********** 
# 
# config port ethernet 3/1 
config>port>eth(3/1)# no shutdown 
config>port>eth(3/1)# queue-group profile b-s 
config>port>eth(3/1)# exit 
config>port# 
config>port# ethernet cl-a/1 
config>port>eth(cl-a/1)# no shutdown 
config>port>eth(cl-a/1)# queue-group profile b-s 
config>port>eth(cl-a/1)# exit 
config>port# 
config>port# ethernet cl-a/2 
config>port>eth(cl-a/2)# no shutdown 
config>port>eth(cl-a/2)# queue-group profile b-s 
config>port>eth(cl-a/2)# exit all 
#*********************************End**************************************** 
 
#***************************Configuring_Bridge Ports************************* 
# 
# config bridge 1 
config>bridge(1)$ port 1 
config>bridge(1)>port(1)$ no shutdown 
config>bridge(1)>port(1)$ exit 
config>bridge(1)# port 2 
config>bridge(1)>port(2)$ no shutdown 
config>bridge(1)>port(2)$ exit 
config>bridge(1)# port 3 
config>bridge(1)>port(3)$ no shutdown 
config>bridge(1)>port(3)$ exit 
7. Resiliency and Optimization 
config>bridge(1)# 
config>bridge(1)# vlan-aware 
config>bridge(1)# exit all 
# 
#*********************************End**************************************** 
 
#*********************Configuring_Classifier_Profiles***************** 
# config flows 
config>flows# classifier vlan500 match-any 
config>flows>classifier-profile(vlan500)$ match vlan 500 
config>flows>classifier-profile(vlan500)$ exit all 
#*********************************End**************************************** 
 
#******************Configuring_Management_and_Data_Flows 1,2***************** 
# config flows 
config>flows# flow 1 
config>flows>flow(1)$ class vlan500 
config>flows>flow(1)$ ingress ethernet cl-a/1 
config>flows>flow(1)$ egress bridge-port 1 1 
config>flows>flow(1)$ reverse-direction queue 0 block 0/1 
config>flows>flow(1)$ no shutdown 
config>flows>flow(1)$ exit 
config>flows# 
config>flows# flow 2 
config>flows>flow(2)$ class vlan500 
config>flows>flow(2)$ ingress ethernet cl-a/2 
config>flows>flow(2)$ egress bridge-port 1 2 
config>flows>flow(2)$ reverse-direction queue 0 block 0/1 
config>flows>flow(2)$ no shutdown 
config>flows>flow(2)$ exit 
config>flows# 
#*********************************End**************************************** 
 
#*********************Configuring_Data_Flow_3***************** 
config>flows# flow 3 
config>flows>flow(3)$ class vlan500 
config>flows>flow(3)$ ingress ethernet 3/1 
config>flows>flow(3)$ egress bridge-port 1 3 
config>flows>flow(3)$ reverse-direction queue 0 block 0/1 
config>flows>flow(3)$ no shutdown 
config>flows>flow(3)$ exit 
config>flows# 
#*********************************End**************************************** 
 
#************************ Configuring_the_Ring******************************* 
# configure protection erp 1 
config>protection>erp(1)# bridge 1 
config>protection>erp(1)# r-aps vlan 200 
config>protection>erp(1)# r-aps mel 5 
config>protection>erp(1)# east-port 1 
config>protection>erp(1)# west-port 2 
config>protection>erp(1)# port-type  west  rpl   
7. Resiliency and Optimization 
config>protection>erp(1)# no shutdown 
config>protection>erp(1)# exit all 
# commit 
Result : OK 
#*********************************End**************************************** 
Configuration Errors  
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 
Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
618 
Error 
ILLEGAL MAINTENANCE 
DOMAIN OF ERP GROUP         
Propagation of Signal Failure (SF) condition from the 
Ethernet OAM service layer cannot be enabled since the 
maintenance domain ID has illegal value 
619 
Error 
MAINTENANCE DOMAIN IS IN 
SHUTDOWN STATE 
Propagation of Signal Failure (SF) condition from the 
Ethernet OAM service layer cannot be enabled since the 
corresponding maintenance domain is in shutdown state 
620  
Error 
ILLEGAL BRIDGE EAST/WEST 
PORT DEFINITION 
The bridge port you are trying to set as an East/West port 
of ERP node does not exist. 
621 
Error 
ILLEGAL R-APS VLAN/MEL 
VALUE DEFINITION 
The value you are trying to set is out of the allowed range:  
[vlan <1–4094>] [mel <0–7>] 
623  
Error 
CANNOT MODIFY ACTIVE RING 
This parameter cannot be changed when ERP is active. To 
change, do the following: 
1. Set the ERP to shutdown. 
2. Perform commit. 
3. Change the parameter. 
4. Set the ERP to no shutdown. 
5. Perform commit. 
624 
Error 
FLOW BETWEEN ERP 
BP&PHYISICAL PORT IS MISSING  
To configure an ERP, you must first configure a flow 
between the physical port and the bridge port 
625 
Error 
BOTH ERP PORTS MUST BE 
CONFIGURED AS LAG 
If LAG is configured on the East port, it must be also 
configured on the West port and vice versa. 
626 
Error 
BOTH LAG MEMBERS MUST BE 
BOUND TO THE SAME CL 
LAG for East or West Ring interfaces must be configured on 
the GbE ports on the same CL module. 

## 7.6 LAG Protection  *(p.599)*

7. Resiliency and Optimization 
Code 
Type 
Syntax 
Meaning 
627 
Error 
SF TRIGGER SHOULD BE 
DEFINED WHEN PORT IS LAG 
When ERP is running over LAG, you have to activate the sf-
trigger command. 
629 
Error 
PASSTHROUGH-VLAN IS NOT 
APPLICABLE TO LOGICAL MAC  
Passthrough-vlan command is not applicable to logical mac 
ports.  
7.6 LAG Protection  
Two Gigabit Ethernet ports on the Megaplex-4 CL modules ports can be operated as a single logical 
interface, using link aggregation in accordance with IEEE 802.3-2005. LAG uses 1:1 distribution 
mechanism. Megaplex-4 supports up to 2 LAGs per chassis. 
Using link aggregation inherently provides redundancy; if one of the GbE ports fails, the other can 
continue transferring traffic. Link failure is detected by sensing the loss of valid signals, or receiving a 
failure report via Link Aggregation Control Protocol (LACP) if applicable, in which case all traffic is sent 
through the other link. 
The load sharing is automatically readjusted if a failure or recovery from failure occurs in any of the links 
that participate in a LAG. 
The CL modules support port aggregation on the same or different modules.  
Applicability and Scaling 
For a LAG aggregating two GbE of the same CL module, up to two LAGs can be configured each time in 
the system. When LAG members belong to different CL modules, only one LAG can be defined per 
system.  
CL.2 (non-A) modules do not support flows between GbE ports on two CL.2 modules with LAG 
protection to Logical Mac ports of CL.2 VCGs.  
Benefits 
Static LAGs provide the following benefits: 
• 
Increased availability 
7. Resiliency and Optimization 
If a link within a LAG fails or is replaced, the traffic is not disrupted and communication is 
maintained (even though the available capacity is reduced). 
• 
Load sharing 
Traffic is distributed across multiple links, minimizing the probability that a single link could be 
overwhelmed. 
• 
Use of existing hardware 
Software replaces the need to upgrade the hardware to higher bandwidth capacity. 
Link aggregation always provides revertive recovery, because that as soon as the down port returns to 
normal, the full bandwidth is again available.  
Configuring the LAG  
This section explains how to define a link aggregation group (LAG) and enable link aggregation control 
protocol (LACP). Megaplex-4 supports up to 2 LAGs.  
LAG is defined with two Ethernet ports bound to the group. LAG serves as a logical port with all relevant 
port attributes (queue block profile, L2CP profile, etc). Services flow to and from the LAG, use the LAG as 
their ingress/egress port. 
To ensure correct distribution of LACP traffic, you must configure a flow with an L2CP profile with peer 
action for the LACP address (01-80-c2-00-00-02). The flow must have the following attributes: 
• 
Ingress port – LAG 
• 
Egress port – according to application requirements. 
If you use the flow only to peer the LACP frames and do not need to forward the traffic, discard it, using 
the drop command on the flow. 
LAG configuration includes the following steps: 
1. Assigning a number to a LAG. 
2. Binding ports to the LAG 
3. Assigning a name to the LAG 
4. Storing the LAG. 
7. Resiliency and Optimization 
 To add a LAG: 
1. Navigate to configure port. 
The config>port# prompt is displayed. 
2. Type lag and enter a LAG number (1 or 2). 
The config>port>lag(number)# prompt is displayed.  
Note 
LAGs must be added in consecutive order. This means LAG 2 must be added 
after LAG 1. 
 
 To configure the LAG:  
• 
At the config>port>lag(number)# prompt, enter all necessary commands according to the tasks 
listed below:  
Task 
Command 
Comments 
Adding a GBE port to the 
LAG 
bind ethernet <slot/port>  
 
To remove/add a link from/to existing LAG, use 
the procedure below. 
Assigning a name to the 
LAG 
name <Alphanumeric string> 
Maximum name length is 64 characters 
Selecting the type of ports 
protected by LAG 
admin-key giga-ethernet  
 
 
The only possible option for the current 
version is giga-ethernet: GbE ports 
Enabling LACP and setting 
LACP parameters: 
operation mode (active or 
passive), time to wait 
before sending LACP 
frames (long or short) and 
system priority 
lacp [tx-activity {active | 
passive}]  [tx-speed {slow | 
fast}] [sys-priority 
<0..65535>] 
tx-activity: 
active – LAG interface periodically transmits 
LACP frames (LACPDUs) to all links with LACP 
enabled  
passive – LAG interface does not initiate the 
LACP exchange, but replies to received 
LACPDUs. 
tx-speed: 
slow – 90 seconds  
fast_– 3 seconds 
no lacp disables LACP protocol. 
Assigning a queue group 
profile 
queue-group profile <profile 
name>  
no queue-group removes queue group 
association 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Assigning method of 
distributing traffic within 
LAG 
distribution-method dest-mac  
<slot/port> 
The only possible option is dest-mac: packets 
are distributed according to their destination 
MAC addresses 
Disabling the LAG 
shutdown 
Using no shutdown enables the LAG 
Displaying bind status 
show bind 
 
Displaying LAG status 
show status 
 
Displaying the LAG 
members statistics 
show lacp-statistics ethernet 
<slot/port> 
 
Displaying LAG members 
status 
show lacp-status ethernet 
<slot/port> 
 
For example: 
 To create a LAG  with packets distributed according to their destination MAC addresses: 
• 
LAG number – 1 
• 
LAG members – GbE Port 1 and GbE port 2of a CL.2 module installed in slot CL-A. 
configure slot cl-a card-type cl cl2-622gbe 
configure slot cl-b card-type cl cl2-622gbe 
config port lag 1 bind ethernet cl-a/1 
config port lag 1 bind ethernet cl-a/2 
config port lag 1 admin-key giga-ethernet 
config port lag 1 distribution-method dest-mac 
config port lag 1 no shutdown  
 To create a flow between this LAG and a fast Ethernet port of an M-ETH module installed in I/O 
slot 1:  
config flows classifier-profile 1000 match-all match vlan 1000 
 
config flows flow 5 classifier 1000 
config flows flow 5 ingress-port ethernet 1/1 
config flows flow 5 egress-port lag 1  
config flows flow 5 no shutdown  
 
config flows flow 6 classifier 1000 
config flows flow 6 ingress-port lag 1 
config flows flow 6 egress-port ethernet 1/1 
config flows flow 6 no shutdown 
commit 
7. Resiliency and Optimization 
To delete a LAG, you have to send the shutdown command followed by commit. Otherwise a CLI error is 
displayed. 
 To delete a LAG: 
config>port>lag(1)# exit 
config>port>no lag 1 
config>port>lag(1)# commit 
Result : OK 
mp4100>config# port lag 1 
config>port>lag(1)# shutdown            
config>port>lag(1)# commit 
Result : OK 
 To remove/add a link from/to an existing LAG, you have first to send the shutdown command followed 
by commit. Otherwise a CLI error is displayed. 
 To remove a link from LAG: 
config>port>lag(1)# shutdown            
config>port>lag(1)# commit 
Result : OK 
config>port>lag(1)# no bind ethernet cl-a/2 
config>port>lag(1)# bind ethernet cl-b/1 
config>port>lag(1)# lacp tx-activity active tx-speed fast 
config>port>lag(1)# no shutdown 
config>port>lag(1)# commit 
Result : OK 
In the example above, Ethernet port cl-a/2 is removed from LAG 1, and port cl-b/1 is added instead of it. 
Displaying LAG Status 
 To display the status of a specific LAG:  
config>port>lag(1)$ show status 
Name                  :  lag 01 
Administrative Status : Up 
Operation Status      : Up 
Displaying LACP Status  
You can display the current status of LACP for each LAG member. 
7. Resiliency and Optimization 
 To display LACP status: 
• 
At the config>port>lag(1–44) #prompt, enter show lacp-status ethernet <slot/port>. 
The LACP statistic counters are displayed. 
config>port>lag(1)# show lacp-status ethernet cl-a/1 
Ports 
----------------------------------------------------------------------------- 
                  Actor                Partner 
Port Number     : 3004                 0 
Port Priority   : 32768                0 
System ID       : 0020D2517B1D         0020D25171BE 
System Priority : 32768                32768 
Operational Key : 2                    31 
Activity        : Active               Active 
Timeout         : Short                Short 
Synchronized    : Yes                  Yes 
Collecting      : Yes                  Yes 
Distributing    : Yes                  Yes 
The LACP status screen provides information on the current state of the local (actor) and remote 
(partner) interfaces in an LACP exchange. 
LACP States 
Counter 
Description 
Actor 
Local device participating in LACP negotiation 
Partner 
Remote device participating in LACP negotiation 
Activity 
Actor or partner's port activity. Passive indicates the port's preference for 
not transmitting LAC PDUs unless its partner's control value is Active. Active 
indicates the port's preference to participate in the protocol regardless of 
the partner's control value. 
Timeout 
LACP timeout preference. Periodic transmissions of LACP PDUs occur at 
either a slow or fast transmission rate, depending upon the expressed LACP 
timeout preference (Long Timeout or Short Timeout) 
Synchronized 
If the value is Yes, the link is considered synchronized. It has been allocated 
to the correct link aggregation group, the group has been associated with a 
compatible aggregator, and the identity of the link aggregation group is 
consistent with the system ID and operational key information transmitted. 
If the value is No, the link is not synchronized. It is currently not in the right 
aggregation. 
Collecting 
Yes indicates collection of incoming frames on the link is currently enabled 
and is not expected to be disabled. Otherwise, the value is No. 
7. Resiliency and Optimization 
Counter 
Description 
Distributing 
No indicates distribution of outgoing frames on the link is currently 
disabled and is not expected to be enabled. Otherwise, the value is Yes. 
Displaying LAG Statistics 
 To display LAG statistics: 
config>port>lag(1)# show statistics 
Running 
--------------------------------------------------------------- 
Counter          Rx                   Tx 
Total Frames     21241092             7431095 
Total Octets     4948371714           0 
Unicast          12010124             0 
Multicast        0                    0 
Broadcast        9230656              7431095 
 
Paused Frames    0                    0 
FCS Errors       0                    --             
LAG Statistics Parameters 
Parameter 
Description 
Total Frames 
Total number of frames received/transmitted 
Total Octets 
Total number of bytes received/transmitted 
Unicast  
Total number of unicast frames received/transmitted 
Multicast  
Total number of multicast frames received/transmitted 
Broadcast  
Total number of broadcast frames received/transmitted 
Paused Frames 
Total number of pause frames (used for flow control) received/transmitted through the 
corresponding Ethernet port 
FCS Errors 
The number of frames received on this interface that are an integral number of octets in 
length but do not pass the FCS check 
Displaying LACP Statistics  
You can display current LACP statistics for each LAG member. 
7. Resiliency and Optimization 
 To display LACP statistics: 
• 
At the config>port>lag(1–44) #prompt, enter show lacp-statistics ethernet <slot/port>. 
The LACP statistic counters are displayed. 
config>port>lag(1)# show lacp-statistics ethernet cl-a/1 
LACP 
----------------------------------------------------------------------------- 
Rx LACP Frames            : 43 
Rx Marker Frames          : 0 
Rx Unknown Frames         : 0 
Rx Illegal Frames         : 0 
Tx LACP Frames            : 46 
Tx Marker response Frames : 0 
LACP Statistic Counters 
Counter 
Description 
Rx LACP Frames 
Number of valid LACP PDUs received 
Rx Marker Frames 
Number of valid Marker PDUs received 
Rx Unknown Frames 
Number of unrecognized packet errors 
Rx Illegal Frames 
Number of invalid packets received 
Tx LACP Frames 
Number of valid LACP PDUs transmitted 
Tx Marker Response Frames 
Number of valid Marker Response PDUs received 
Configuration Errors 
The table below lists messages generated by Megaplex-4 when a configuration error is detected. 
Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
553 
Error 
ILLEGAL NUMBER OF LAGs 
BETWEEN CL CARDS 
Only a single LAG can be configured between two CL cards 
554 
Error 
ILLEGAL NUMBER OF LAG 
MEMBERS 
At least two members must be defined in a LAG 
555 
Error 
LAG MEMBER IS SHUTDOWN 
A LAG member should be in no shutdown state 
- 
 
LAG on different CL cards and 
LOGICAL MAC on CL 
When working with CL2-622GBE module, a flow between 
LAG port and a VCG (Logical MAC port) is not supported. 

## 7.7 Path Protection for SDH/SONET Payload  *(p.607)*

7. Resiliency and Optimization 
7.7 Path Protection for SDH/SONET Payload  
Factory Defaults 
In Revertive mode, the wait-to-restore time is 300 sec.  
Functional Description  
Path (trail) protection is available for user-specified payload units (VC-12 for SDH links, or VT1.5 for 
SONET links) mapped to VCG. Up to 252 VC path protection groups can be defined by the user.  
When path protection is enabled, the protected payload unit is assigned bandwidth on both network 
links: 
• 
The same payload is transmitted on both links. 
• 
The receive interfaces of the two links continuously evaluate the received signals. As long as the 
working path operates satisfactorily, its signal is selected for processing. When the working path 
signal fails, or is degraded, the receive side rapidly selects the other signal for processing.  
Provisioning appropriate alternative paths through the network ensures that in case of a fault anywhere 
along the active path, the traffic is automatically switched to the standby path. 
Switchover Criteria 
The switchover criteria for VC/VT path protection are the following alarms: 
• 
ais-vcvt –Alarm indication signal  
• 
tim-vcvt –Path trace id mismatch  
• 
plm-vcvt –Payload label mismatch  
• 
lop-vcvt –Loss of pointer 
• 
card_mismatch – The configured module type does not match the actual module installed (in 
case of card removal, reset or failure). 
7. Resiliency and Optimization 
Recovery Modes 
The recovery mode after a protection switching can be selected in accordance with the application 
requirements:  
• 
Non-revertive mode – the CL module will not automatically flip back after the failed port returns 
to normal operation, but only when the currently used port fails (that is, when its alarm weight 
exceeds that of the standby port).  
• 
Revertive mode – the CL module will flip back to the original port when it returns to normal 
operation (that is, its alarm weight is equal to, or lower than, that of the currently active port).  
Configuring VC Path Protection  
Adding and Removing a VC Path Protection Group 
 To add and define a VC path protection group: 
1. At the config> prompt, enter protection. 
The config>protection# prompt appears. 
2. Enter vc-path <path name>. The path name may consist of up to 80 alphanumeric characters. 
The VC path protection group is defined and enabled and the  
config>protection>vc-path(<path name>)# prompt appears. 
 To remove a VC path protection group: 
• 
At the config>protection# prompt, enter no vc-path <path name>. 
The VC path protection group is removed. 
Binding Ports to a VC path Protection Group 
 To configure the SDH/SONET path protection: 
• 
At the config>protection>vc-path(group name)# prompt, enter all necessary commands 
according to the tasks listed below: 
Task 
Command 
Comments 
Assigning a name to the VC 
path protection group 
name <up to 80 characters> 
 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Activating the VC path 
protection group  
no shutdown 
Using shutdown switches the VC path 
protection group to standby mode 
Adding a working/protection 
port to the VC path protection 
group   
bind  {working | protection} 
vc-vt <slot>/<port>/<au4>/ 
<tug_3>/<tug_2>/<tributary> 
The number and type of working and 
protection ports must be identical.  
Using no before bind removes a port 
from VC path protection group.  
Enabling the reverting of the 
working and protection ports  
revertive 
In case reverting is selected, the wait-to-
restore time must be defined.  
Using no revertive disables the reverting. 
Defining the wait-to-restore 
period for the revertive 
recovery mode (the time to 
elapse after the link recovery 
before traffic switches back) 
wait-to-restore <1–720> 
 
The unit of time is seconds. 
Note. The last configured wait-to-restore 
value is copied to all VC path protection 
groups throughout the system, so that 
the wait-to-restore value is always the 
same for all vc-vt ports.  
Forced switching of traffic from 
the protection port to the 
working port  
force-switch-to-working 
 
 
  
Forced switching of traffic from 
the working port to the 
protection port 
force-switch-to-protection 
 
 
Clearing the force switch 
command 
clear  
Once the force-switch command is 
cleared, the module returns back to 
normal operation. 
Viewing the Status of a VC Path Protection Group  
This section illustrates the status display of a VC path protection group. 
 To view the VC path protection group status: 
• 
At the config>protection>vc-path(<group name>)# prompt, enter show status. 
The VC path protection group status appears. 
 
In this example, the VC path protection group name is test. 
7. Resiliency and Optimization 
>protection>vc-path(test)# show status 
-------------------------------------------------------------------- 
                : 1+1 
istrative Status : Up 
-------------------------------------------------------------------- 
ng        VC   
 
Admin     Oper       Active 
-------------------------------------------------------------------- 
tion     Sdh-Sonet cl-a/1/1/1/1/1         Up         Up 
    -- 
ng        Sdh-Sonet cl-a/2/1/1/1/1         Up         Up        Yes 
Example 
 To add and configure an VC path protection group: 
• 
VC-path protection group name – test 
• 
Working port: slot=cl-a, sdh port=2, aug=1, tug3=1, vc12=1, tributary=1 
• 
Protection port: slot=cl-a, sdh port=1, aug=1, tug3=1, vc12=1, tributary=1 
• 
Reverting is enabled 
config>protection> vc-path(test)#revertive 
• 
Wait-to-restore time is 25 sec. 
gure protection vc-path(test)#bind working sdh-sonet cl-a/2/1/1/1/1 
>protection> vc-path(test)#bind protection sdh-sonet cl-a/1/1/1/1/1 
>protection> vc-path(test)#revertive 
>protection> vc-path(test)#wait-to-restore 25 
 To delete VC path protection group named test: 
#configure protection no vc-path test 

## 7.8 PW Protection  *(p.611)*

7. Resiliency and Optimization 
Configuration Errors 
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 
VC Path Protection Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
607  
Error 
MISSING MEMBER IN 
PROTECTION GROUP 
VC-path group must contain two members. Bind another 
port to the group 
608  
Error 
ILLEGAL PROTECTION GROUP 
DEFINITION 
Path Protection cannot be configured on bypassed VC/VTs. 
See also Error 608 in Ethernet Group Protection and PW 
Protection for additional meanings. 
7.8 PW Protection  
PW protection mechanism protects pseudowire traffic in case of network path failure. The user defines 
different network paths for the working and protection pseudowires.  
Applicability and Scaling 
This type of protection is supported by all the PW-equipped modules, and is configured between two 
different PWs on the same module.  
Benefits 
The PW protection provides the following main advantages: 
• 
Automatically restores service within a short time without user intervention 
• 
Provides zero packet loss protection 
• 
In case of technical failure, allows service to continue while technical staff finds the source of 
the failure and corrects it. 
Moreover, when protection is used, tasks such as planned maintenance or installing modules with 
enhanced capabilities can also be performed without disrupting service, provided a few precautions are 
taken (see below). 
7. Resiliency and Optimization 
Standards 
PW Protection is RAD proprietary technology.  
Factory Defaults 
Megaplex-4 is supplied with PW protection disabled.  
Functional Description 
For PW protection, two PW ports on the same module are connected to the same DS1 port. A typical 
configuration is shown in the figure below. 
The working and protection PWs must be configured with the same psn parameter: either udp-over-ip 
or ethernet. 
During normal operation, the operational state of the working and protection PWs is continuously 
monitored to ensure that it is operating properly. In the case of faulty condition on one of the PWs, the 
traffic is routed to the DS1 port from the other PW, which is not suffering from faulty conditions.  
Switchover Criteria  
The switchover occurs on the rx_failure alarm (Ethernet frames are not received by the PW). 
The protection mode is non-revertive. 
 
 
PW Protection  
Working and Protection Port Parameters 
For two ports configured to PW protection, the following parameters must be the same for both ports: 
GbE
CL-A/1
GbE
CL-B/1
I/O 
Serial Port
DS1
PW #1
Working 
PW #2
Protection
SVI #1
SVI #2
7. Resiliency and Optimization 
• 
psn type (udp-over-ip or Ethernet)  
• 
tdm-oos  
• 
tdm-payload-size. 
Configuring PW Protection  
The PW protection is configured as follows. 
 To add a PW protection group: 
1. Navigate to configure protection. 
2. Type pw and enter a group number.  
The config>protection>pw(group-id)# prompt is displayed.  
 To configure the PW protection group: 
• 
At the config>protection>pw(group-id)# prompt, enter all necessary commands according to 
the tasks listed below: 
Task 
Command 
Comments 
Assigning a name to the PW 
protection group 
name <up to 80 characters> 
 
Administratively enabling a 
PW protection group  
no shutdown 
Using shutdown disables the group 
Adding working and 
protection PWs to the PW 
protection group   
bind  {working | protection} <pw 
number> 
 
 
Using no bind protection removes the 
protection port from the group. There is no 
need to remove the working port from the 
group. 
Defining operation mode of 
the PW protection 
oper-mode  1-plus-1  
Permanently set to 1-plus-1  
Example  
 To add and configure a PW protection group: 
• 
VS-12 module 
7. Resiliency and Optimization 
• 
Protection group-id – 4 
• 
Working PW number – 1 
• 
Protection PW number – 2 
config# protection 
config>protection# pw 4 
config>protection>pw(4)$ bind working 1 
config>protection>pw(4)$ bind protection 2 
config>protection>pw(4)$ no shutdown 
 To delete PW protection group 4: 
#configure protection no pw 4 
Viewing the PW Protection Status  
This section illustrates the status display of a PW protection group. 
 To view the PW protection group status:  
• 
At the config>protection>pw (<group-id>)# prompt, enter show status. 
The PW protection group status appears. In this example, the PW protection group number is 
pw1. 
mp4100>config>protection>pw(1)# show status 
Group 
------------------------------------------------------------------------ 
Mode                  : 1+1 
Administrative Status : Up 
 
PWs 
------------------------------------------------------------------------ 
Working    PW        Admin     Oper       Active 
------------------------------------------------------------------------ 
Protection pw2     Up            Down       -- 
Working    pw1     Up            Up         Yes 
    
------------------------------------------------------------------------  
Configuration Errors  
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 

## 7.9 TDM Group Protection  *(p.615)*

7. Resiliency and Optimization 
Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
603 
Error 
PORT PARAMETERS OF 
MEMBERS ARE ASYMMETRIC  
The following parameters must be identical for both 
members of the PW protection group: 
• PW Type 
• Jitter Buffer 
• TDM Payload size. 
608 
Error 
ILLEGAL PROTECTION GROUP 
DEFINITION 
 
Verify that working and protection PWs belong to the same 
module.  
See also Error 608 in Ethernet Group Protection and Error! 
Reference source not found. for additional meanings. 
7.9 TDM Group Protection  
One of the simplest methods to protect against link and hardware failure is to use the TDM group 
protection.  
Applicability and Scaling 
This type of protection is used for e1, e1-I, t1, t1-i, ds1, t3 and cmd-channel ports. 
For E1/T1/DS1/DS1-opt ports, the protection partner ports can be located on either the same module, 
or another module, and can be of any of the following depending on the interface type:  
• 
For external/internal E1 ports: any I/O external E1 ports, internal E1 ports of CL modules, DS1-
opt ports of VS-6/C37 modules or DS1 ports of all PW-equipped modules.  
• 
For external/internal T1 ports: any I/O external T1 ports, internal T1 ports of T3 modules, 
internal T1 ports of CL modules, DS1-opt ports of VS-6/C37 modules or DS1 ports of all PW-
equipped modules. 
For CMD channels (cmd-channel ports) of TP modules, the protection partner port is located on the 
same module and must be the following: 
• 
cmd-channel 2 is always a protection partner for cmd-channel 1  
• 
cmd-channel 4 is always a protection partner for cmd-channel 3.  
7. Resiliency and Optimization 
The maximum total number of TDM groups that can be configured for Megaplex-4 is 144.  
Benefits 
The TDM group protection provides two main advantages: 
• 
Automatically restores service within a short time without user intervention 
• 
In case of technical failure, allows service to continue while technical staff finds the source of 
the failure and corrects it. 
Moreover, when protection is used, tasks such as planned maintenance, updating software versions, or 
installing modules with enhanced capabilities, can also be performed without disrupting service, 
provided a few precautions are taken (see below). 
Standards 
TDM Group Protection is RAD proprietary technology. 
Factory Defaults 
Megaplex-4 is supplied with TDM protection disabled. Other parameter defaults are listed in the table 
below.  
Parameter  
Default Value 
oper-mode  
dual-cable-tx 
revertive/no revertive 
no revertive for cmd-channel ports 
revertive for other ports 
wait-to-restore  
300 sec 
Functional Description  
The TDM group (dual-cable) configuration provides protection against both transmission path failure 
and technical failure in the module hardware.  
7. Resiliency and Optimization 
For this type of protection, two ports of the same type are connected to the remote unit via two parallel 
links. Defining these two links as a TDM protection group ensures that traffic carrying capacity is 
available even if one of the links fails. These ports can be as follows: 
• 
e1/e1-i/ds1/ds1-opt ports 
• 
t1/t1-i/ds1/ds1-opt ports 
• 
cmd channels of TP modules  
• 
t3 ports of T3 modules. 
The figure below shows a typical system configuration using dual-cable protection. The user can select the 
module ports operating as a TDM group. Both ports process as usual the transmit and receive signals, but 
the receive output of the protection port is disconnected. 
During normal operation, the operational state of the working and protection ports is continuously 
monitored to ensure that they are operating properly. If the working port fails, the traffic is routed to 
the corresponding user/data port from the protection port.  
The maximum switching time between main and backup ports is 50 msec. Therefore protection 
switching will ensure essentially uninterrupted service for all the types of applications; in particular, it 
will not cause the disconnection of voice calls.  
 
E1/T1 Link Protection Using Dual Cables (TDM Group) 
Working and Protection Port Parameters 
For two ports configured to TDM group protection, the following parameters must be the same for both 
ports. 
For E1/T1/E1-i/T1-i ports:  
• 
Admin Status 
• 
line-type 
• 
line-code 
• 
inband-management > timeslot 
I/O Module with 
E1 or T1 Ports
Megaplex-4100
Working (Active) Link
Protection (Standby) Link
Megaplex-4100
I/O Module with 
E1 or T1 Ports
7. Resiliency and Optimization 
• 
inband-management > protocol 
• 
inband-management > routing-protocol 
For DS1 and DS1-opt ports:  
• 
Admin Status 
• 
line-type  
• 
signaling  
For cmd channels of TP modules:  
• 
rate & trigger-mode 
For T3 ports:  
• 
Admin Status 
• 
line-type. 
Protection Mode 
The recovery mode after a protection switching can be selected in accordance with the application 
requirements: 
• 
Non-revertive mode – the module will not automatically flip back from protection to working 
port after the working port returns to normal operation, but only when the currently used port 
fails. 
• 
Revertive mode – the module will flip back from protection to working port when it returns to 
normal operation.  
To prevent switching under marginal conditions, the user can specify a restoration time (wait-to-
restore). This is the minimum interval before flipping back to the working port. During the restoration 
time, alarms with the same weight, or with lower weights, are ignored. As a result, the module starts 
evaluating the criteria for protection switching (flipping) only after the restoration time expires, thereby 
ensuring that another flip cannot occur before the specified time expires.  
However, if an alarm with a weight exceeding that of the alarm which caused flipping appears, 
immediate flipping will occur, even if the restoration time has not yet expired. 
Switchover Criteria  
With TDM-group protection, switchover criteria depend on the ports participating in protection. This 
section lists the alarms affecting the protection switchover for different Megaplex-4 ports. 
7. Resiliency and Optimization 
E1/T1 Ports 
Alarms on E1/T1 Ports: 
• 
lof –  Loss of frame  
• 
lomf – Loss of multiframe  
• 
lomf_fe – Loss of multiframe at the far end  
• 
los – Loss of signal  
• 
rai – Remote alarm indication (Loss of sync (signal or frame) at far end)  
• 
ais – Alarm indication signal  
• 
card_mismatch – The configured module type does not match the actual module installed (in 
case of card removal, reset or failure) 
Upper Layer critical alarms (T3 port): 
• 
lof –  Loss of frame on T3 port 
• 
los – Loss of signal on T3 port  
• 
rai – Remote alarm indication on T3 port 
• 
ais – Alarm indication signal on T3 port 
E1-i/T1-i Ports 
Alarms on E1-i/T1-i Ports: 
• 
lof –  Loss of frame  
• 
lomf – Loss of multiframe  
• 
lomf_fe – Loss of multiframe at the far end  
• 
rai – Remote alarm indication (Loss of sync (signal or frame) at far end)  
• 
ais – Alarm indication signal  
• 
card_mismatch – The configured module type does not match the actual module installed (in 
case of card removal, reset or failure) 
Upper Layer critical alarms (SDH/SONET port):  
• 
SDH/SONET critical alarms (in any layer of SDH/SONET): LINE/SOH, HVC (vc4-sts1), LVC (vc-vt)  
7. Resiliency and Optimization 
DS1 Ports 
Alarms on DS1 Ports: 
• 
lof –  Loss of frame  
• 
lomf – Loss of multiframe  
• 
lomf_fe – Loss of multiframe at the far end  
• 
rai – Remote alarm indication (Loss of sync (signal or frame) at far end)  
• 
ais – Alarm indication signal  
• 
card_mismatch – The configured module type does not match the actual module installed (in 
case of card removal, reset or failure) 
Upper Layer critical alarms: 
• 
fe_rdi –  Remote defect indication (rdi) on the far-end device 
• 
rx_failure – Ethernet frames are not received by PW 
• 
fe_rx_failure – Ethernet frames not received by PW on the far-end device 
DS1-Opt Ports 
Alarms on DS1-Opt Ports: 
• 
ds1_lof – Loss of frame detected at DS1 framer 
• 
ds1_rai – Remote alarm indication detected at DS1 framer 
• 
c37.94_lof – Loss of frame detected at C37.94 framer 
• 
optical_receiver_los – Loss of signal detected at optical receiver 
• 
card_mismatch – The configured module type does not match the actual module installed (in 
case of card removal, reset or failure) 
Cmd channels 
Alarms on Cmd channels (1..2), (3..4): 
• 
lof – Loss of frame detected at cmd-channel 
• 
rai – Remote alarm indication (rai)  
• 
address_mismatch – Local and remote address mismatch 
• 
out_of_service 
 – Out of service 
7. Resiliency and Optimization 
Traffic Duplication  
Traffic Duplication is a new technology developed by RAD for enhanced reliability and performance, 
used to minimize delay on critical utility applications (such as teleprotection). This technology is 
implemented in all PW-equipped I/O modules. Mission-critical traffic can be transported over a new 
Carrier Ethernet network running in parallel with the existing SDH/SONET network, while preparing for 
future full service migration. 
This type of protection employs three members and is implemented by defining two TDM groups with a 
common member (see Example 5).  One tdm group is configured between two e1-i/t1-i ports on the 
CL.2 module and the second tdm-group is configured between one of the e1-i/t1-i partners in the 
previous group and a ds1 port of the PW-equipped module.  
Megaplex-4 duplicates the TDM service to two parallel flows: 
• 
Towards the TDM uplink (PDH or SDH/SONET) based on its internal TDM cross-connect.  When 
transported over SDH/SONET it is also protected using path protection.  
• 
Towards the Ethernet uplink (single or Ring) using PWE encapsulation. The figure below shows a 
G.8032 ring used to protect the Ethernet service.  
 
 
Adding Traffic Duplication to an Existing SONET/SDH Network through an Existing PSN  
Configuring TDM Group Protection 
The TDM Group Protection is configured as follows. 
TDM 
Traffic
PSN
G.8032 Ring
SONET/SDH
VC-VT CL.2/B
VC-VT CL.2/A
VC-VT CL.2/B
VC-VT CL.2/A
PW
PW
DS1
DS1
E1/T1 CL.2/A
E1/T1 CL.2/B
E1/T1 CL.2/A
E1/T1 CL.2/B
TDM Group
Parallel Tx
TDM Group
Parallel Tx
7. Resiliency and Optimization 
 To add a TDM protection group: 
1. Navigate to configure protection. 
2. Type tdm-group and enter a group number.  
The config>protection>tdm-group(group number)# prompt is displayed. 
 To configure the TDM protection group: 
• 
At the config>protection>tdm-group(group number)# prompt, enter all necessary commands 
according to the tasks listed below: 
Task 
Command 
Comments 
Administratively enabling 
TDM group 
no shutdown 
Using shutdown disables the group 
Defining operation mode of 
the TDM group 
oper-mode dual-cable-tx 
 
 
Adding working and 
protection  
e1/e1-i/ds1 
ports to the TDM group 
   
bind  {working | protection} 
e1  <slot>/<port> 
bind  {working | protection} e1-
i  <slot>/<port> 
bind  {working | protection} 
ds1  <slot>/<port> 
 
Using no bind protection  (e1/e1-i/ds1) 
removes the protection port from the 
group. There is no need to remove the 
working port from the group. 
An e1 port of VS-16E1T1-EoP module bound 
to a VCG cannot be configured as a partner 
in tdm-group.  
An e1 port of VS-16E1T1-PW or VS-6/E1T1 
module cross connected directly to PW 
cannot be configured as a partner in tdm-
group.  
An e1 port bound/cross-connected with 
HDLC cannot be configured as a partner in 
tdm-group.  
7. Resiliency and Optimization 
Task 
Command 
Comments 
Adding working and 
protection t1/t1-i/ds1 
ports to the TDM group 
   
bind  {working | protection} 
t1  <slot>/<port>/[<tributary>]  
bind  {working | protection} t1-
i  <slot>/<port> 
bind  {working | protection} 
ds1  <slot>/<port> 
 
Using no bind protection (t1/t1-i/ds1)  
removes the protection port from the 
group. There is no need to remove the 
working port from the group. 
[<tributary>] relates to internal T1 ports of 
T3 modules.  
If TDM group protection is configured for a 
T3 port, the same type of protection is also 
automatically configured on all the open 
internal T1 ports belonging to this T3 
module. The T1 members belonging to such 
a group have the same numbers. The group 
numbers start from 200. 
You can also configure TDM group 
protection on individual selected T1 ports if 
their T3 ports are not configured to 
protection. 
A t1 port of  VS-16E1T1-EoP module bound 
to a VCG cannot be  configured as a partner 
in tdm-group. 
A t1 port of VS-16E1T1-PW or VS-6/E1T1 
module cross connected directly to PW 
cannot be configured as a partner in tdm-
group.  
Adding working and 
protection t3 ports to 
the TDM group   
 
bind  {working | protection} 
t3  <slot>/<port>  
 
 
Using no bind protection t3 removes the 
protection port from the group. There is no 
need to remove the working port from the 
group. 
Once TDM group protection is configured 
for the T3 port, the same type of protection 
is also automatically configured on all the 
open internal T1 ports belonging to this T3 
module.  
Adding working and 
protection cmd-channel 
ports to the TDM group   
bind  {working | protection} 
cmd-channel <slot>/<port> 
1,3 – working channels 
2, 4 – protection channels  
Using no bind protection cmd-channel 
removes the protection port from the 
group. There is no need to remove the 
working port from the group. 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Enabling the reverting from 
the protection port to the 
working port  
revertive 
Using no revertive disables the reverting 
The reverting value (revertive/no revertive) 
configured for a T3 port TDM protection 
group is automatically copied to the TDM 
protection groups of all T1 ports belonging 
to this T3.   
Defining the wait-to-restore 
period (after the switching 
criteria are cleared, 
the time to elapse 
before traffic switches back) 
wait-to-restore <0–720> 
 
 
The unit of time is seconds.  
The wait-to-restore value configured for a 
T3 port TDM protection group is 
automatically copied to the TDM protection 
groups of all T1 ports belonging to this T3.  
Forced switching of traffic 
from the protection port to 
the working port  
force-switch-to-working 
 
 
 
Forced switching of traffic 
from the working port to 
the protection port 
force-switch-to-protection 
 
 
Manual switching of traffic 
from the protection port 
back to the working port, 
unless a failure condition 
exists on the working port 
or an equal/higher priority 
switch command is in effect 
manual-switch-to-working 
 
 
 
 
 
Forced switching of traffic 
from the working port to 
the protection port, unless 
a failure condition exists on 
the protection port or an 
equal/higher priority switch 
command is in effect 
manual-switch-to-protection 
 
 
Clearing the force switch 
command 
clear  
Once the force-switch command is cleared, 
the module returns back to normal 
operation. 
7. Resiliency and Optimization 
Example 1 
 To add and configure an E1/T1 protection group: 
• 
Protection group number – 2 
• 
Working link – Port 1 of the module installed in slot 6 
• 
Protection link – Port 2 of the module installed in slot 5 
• 
Operation mode – dual cable protection 
• 
Wait-to-restore period – 200 seconds. 
#configure protection tdm-group 2 bind working e1 6/1 
#configure protection tdm-group 2 
config>protection>tdm-group (2)#bind protection e1 5/2 
config>protection>tdm-group (2)#wait-to-restore 200 
 To delete protection group 2: 
#configure protection no tdm-group 2 
 To display the protection status: 
mp4100>config>protection>tdm-group(1)# show status 
Group 
--------------------------------------------------------------- 
Mode                                      : Dual Cable Tx 
Administrative Status       : Up 
Last Switchover Reason  : None 
Last Command                    : 
 
Cards 
--------------------------------------------------------------- 
            Port         Admin     Oper       Active 
Working     DS1    4/1   Up        Up         Yes 
Protection  DS1    4/2   Up        Down       -- 
 To delete protection group 1: 
#configure protection no tdm-group 1 
7. Resiliency and Optimization 
Example 2 
 To add and configure an CMD Channel protection group on TP module: 
• 
Protection group number – 1 
• 
Working link – CMD channel 1 of the module installed in slot 4 
• 
Protection link – CMD channel 2 of the module installed in slot 4 
• 
Operation mode – dual cable protection (this is the only option so the 3rd string is optional)   
• 
Not revertive 
config protection tdm-group 1 bind  working  cmd-channel  4/1 
config protection tdm-group 1 bind  protection  cmd-channel  4/2 
config protection tdm-group 1 oper-mode  dual-cable-tx 
config protection tdm-group 1 no-revertive 
 To display the protection status: 
config>protection>tdm-group(1)# show status 
Group 
--------------------------------------------------------------- 
Mode                  : Dual Cable Tx 
Administrative Status : Up 
 
Cards 
--------------------------------------------------------------- 
           Port                   Admin    Oper     Active 
Working    Cmd Channel 4/1        Up       Up       Yes 
Protection Cmd Channel 4/2        Up       Up       -- 
Example 3 
 To add and configure a T3 protection group: 
• 
Protection group number – 1 
• 
Working link – T3 Port (1) of the module installed in slot 9 
• 
Protection link – T3 Port (1) of the module installed in slot 8 
• 
All other parameters are at their defaults. 
#configure protection tdm-group 1 bind working t3 9/1 
#configure protection tdm-group 1 bind protection t3 8/1 
7. Resiliency and Optimization 
 To display the results: 
config>protection# info detail 
    echo "TDM Group Protection" 
#   TDM Group Protection 
    tdm-group  1 
        bind  working  t3  9/1 
        bind  protection  t3  8/1 
    exit 
#   TDM Group Protection 
    tdm-group  200 
        bind  working  t1  9/1/3 
        bind  protection  t1  8/1/3 
    exit 
#   TDM Group Protection 
    tdm-group  201 
        bind  working  t1  9/1/2 
        bind  protection  t1  8/1/2 
    exit 
#   TDM Group Protection 
    tdm-group  202 
        bind  working  t1  9/1/1 
        bind  protection  t1  8/1/1 
    exit 
The display includes the created T3 TDM protection group 1 and T1 TDM protections groups 200, 201 
and 202 automatically created for all open T1 ports. 
 To display the status of each T1 protection group: 
config>protection# tdm-group 200 
config>protection>tdm-group(200)# show status 
Group 
---------------------------------------------------------------------- 
Mode                  : Dual Cable Tx 
Administrative Status : Up 
Last Command          : 
 
Cards 
---------------------------------------------------------------------- 
           Port                   Admin    Oper     Active 
Working    T1          9/1/3      Up       Up       Yes 
Protection T1          8/1/3      Up       Down     -- 
 To delete protection group 1: 
#configure protection no tdm-group 1 
7. Resiliency and Optimization 
Configuration Errors 
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 
TDM Group Protection Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
140 
Error 
ILLEGAL TDM PROTECTION 
ASSIGNMENT 
The protection assignment of one port does not point to 
another port 
142 
Error 
PORT CAN PARTICIPATE ONLY 
IN ONE TDM GROUP 
An E1/T1 port cannot be member of several TDM protection 
groups.  
420 
Error 
MLPPP PORT CAN'T BE BOUND 
TO TDM GROUP 
E1 port bound to MLPPP port cannot be a member of 
protection group 
476 
Error 
PROTECTED PORTS HAVE 
ASSYMETRIC PARAMETERS 
When TDM protection is configured between two DS1 ports, 
all their physical layer parameters must be identical  
601 
Error 
WORKING & PROTECTION ARE 
ON THE SAME PORT 
The same port cannot be defined as both working and 
protection port 
602 
Error 
UNFRAMED TYPE CAN'T BE A 
MEMBER OF TDM GROUP 
Unframed E1/T1 ports cannot be selected as members of 
TDM group   
603 
Error 
PORT PARAMETERS OF 
MEMBERS ARE ASSYMETRIC 
 
For two ports configured to TDM group protection, the 
following parameters must be the same for both ports. 
For E1/T1/E1-i/T1-i ports: 
• Admin Status 
• line-type 
• line-code 
• inband-management > timeslot 
• inband-management > protocol 
• inband-management > routing-protocol 
For cmd channels of TP modules:  
• rate & trigger-mode 
For T3 ports: 
• Admin Status 
• line-type. 
604  
Error 
PROTECTION PORT IS IN 
SHUTDOWN STATE   
One of the ports in tdm protection group is in shutdown 
state 

## 7.10 Accelerated Ethernet Hardware Switchover Protection  *(p.629)*

7. Resiliency and Optimization 
Code 
Type 
Syntax 
Meaning 
611 
Error 
TRAFFIC DUP ENTRY MUST BE 
NON REVERTIVE 
In traffic duplication configuration, the tdm group 
employing two CL e1(t1)-i ports, must be configured to non-
revertive mode. 
612 
Error 
IN T3 PROTECTION, MEMBERS 
MUST BE SYMMETRIC 
 
The following asymmetrical ports were manually defined by 
the user on the T3 module: 
• either T1 ports as TDM group protection members  
• or Logical MAC ports as Ethernet group protection 
members.  
These members must be symmetric for working and 
protection T3 module slots.  
622 
Error 
WORKING OR PROTECTION 
PORTS ALREADY USED 
The working or protection ports you are trying to set are 
already used for another protection pair.   
683  
Error 
ILLEGAL CMD CHANNEL 
PROTECTION ASSIGNMENT  
 
Cmd-channel protection members must satisfy the following 
conditions: 
• Working and protection ports must belong to the same 
slot  
• Working ports must be Cmd-Channels 1 or 3 
• Protected ports must be either Cmd-Channel 2 (for 
working port 1) or 4 (for working port 3); no other option 
is allowed. 
777 
Error 
PORT DISABLED ON PRIMARY 
TDM-GROUP MEMBER 
 
A T1 or Logical MAC port was defined as a member of T3 
TDM protection group in the protection module slot, while 
is not opened in the working module slot. 
7.10 Accelerated Ethernet Hardware Switchover Protection  
To meet 50ms hardware redundancy between CL.2 modules, the rate of the communication between VS 
modules and CL should be limited to 100M. In M-ETH, the bandwidth between the module ports is not 
influenced by this parameter. 
For other I/O modules the equipment is operating properly.  
The problem mainly arises for CL card level redundancy in the following cases:  
7. Resiliency and Optimization 
• 
Between GbE ports of CL modules when a flow is set from the Ethernet ports of VS modules to 
an ERP ring port  
• 
Between GbE ports of CL modules in a system with PW traffic. 
Accelerated Ethernet Hardware Switchover Protection offers a workaround for this problem for the 
majority of the modules involved. 
Note 
In this mode the aggregate traffic from M-ETH module does not exceed 
100 Mbps. 
Applicability and Scaling  
This feature applies for the following I/O modules: 
• 
VS-6/12  
• 
VS-6/BIN 
• 
VS-6/C37 
• 
VS-6/703 
• 
VS-6/E1T1 
• 
VS voice modules with serial ports (both basic and PW-enhanced versions) 
• 
M-ETH 
Benefits  
Accelerated Ethernet Hardware Switchover provides higher availability for critical applications at HW 
card level redundancy, with fast protection switching time. 
Factory Defaults 
Megaplex-4 is supplied with Accelerated Ethernet Hardware Switchover protection disabled.  
7. Resiliency and Optimization 
Configuring 50ms HW protection between CL.2 modules 
Caution 
Since changing the operation mode may result in loss of traffic, this 
procedure is to be done before launching any service. 
 To run Accelerated Ethernet Hardware Switchover between CL.2 modules: 
1. Navigate to configure>protection#. 
2. Type accelerated-eth-hw-switchover. 
The command is activated and the following caution is displayed. 
*****This action will change operating mode and may affect user traffic***** 
 To stop Accelerated Ethernet Hardware Switchover: 
1. Type no accelerated-eth-hw-switchover. 
The device returns to the basic operating mode. 
Note 
To assure error-free functioning, the CIR value of the Ethernet ports in the VS 
modules must be set to the default value (10M). 
 
 
 