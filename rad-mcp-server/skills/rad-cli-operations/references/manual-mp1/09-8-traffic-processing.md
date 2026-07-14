# 8 Traffic Processing

*Manual `MP-1-mn_ver 2.2.pdf`, pages 281–356.*


## 8.1 Bridge  *(p.281)*

This chapter explains how to configure network-related features: management bridge and router, flows, 
pseudowire environment and cross-connections. 
 
8.1 Bridge 
Bridge is a Layer-2 forwarding entity that can be VLAN-aware or VLAN-unaware. Megaplex-1 bridge is 
always VLAN-aware. 
Standards 
IEEE 802.1D 
IEEE 802.1Q 
Benefits  
The bridge delivers E-LAN services. 
Functional Description 
The bridge always operates in VLAN-aware mode. All the flows pass though the bridge and are 
bidirectional. 
Traffic through the bridge is configured via flows between non-bridge ports (e.g. Ethernet, SVI) and 
bridge ports, allowing editing action at the bridge ports.  
Megaplex-1 
8. Traffic Processing 
Admission to Bridge 
In order for a frame to be admitted to the bridge, its classification must match the flow classification 
configured for the bridge port. 
In VLAN-aware mode, VLAN membership can be automatically learned from the VLAN classification used 
in bridge port flows or can be added manually. Additionally, flows with untagged classification must 
have a push editing action. 
In VLAN-unaware mode, any packet may be admitted according to the configured flow classifications. 
Packet Editing on Reverse Flows  
All Megaplex-1 flows are bidirectional. Megaplex-1 performs editing on the reverse direction according 
to the flow classification and specified editing actions. The following table shows the editing action on 
the reverse flow, as well as the VLAN learned from the flow.  
Packet Editing on Reverse Flows  
Classification 
Editing of Flow with 
Bridge Port as Egress 
Port 
Editing of Reverse 
Directional Flow 
VLAN Value (VPN) 
VLAN X 
None  
None 
X 
VLAN X   
Inner VLAN Y 
None 
None 
X 
Any classification 
(classify all, including 
untagged) 
Push X p-bit fixed 
Pop 
X 
VLAN X   
Inner VLAN Y 
Pop 
Push X 
Y 
VLAN X 
Pop 
Not allowed 
Not allowed 
 
Management via Bridge  
In order to manage via the bridge, you need to configure the following: 
• 
Router interface for management, bound to SVI 
Megaplex-1 
8. Traffic Processing 
• 
Flow between SVI and bridge port (only one SVI<->bridge port flow can be created per bridge 
port) 
• 
Flow between Ethernet port and bridge port 
Factory Defaults  
The factory default configuration includes bridge 1 only. 
Configuring the Bridge 
To configure the bridge, perform the following steps: 
1. Configure the bridge. 
2. Configure the bridge ports. 
3. If working in VLAN-aware mode, configure VLANs.  
4. Configure flows between non-bridge ports and bridge ports.  
 To configure the bridge: 
1. At the config# prompt, enter:  
bridge 1 
The config> bridge(1)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining aging time for MAC 
table entries (seconds) 
aging-time <seconds>  
Possible values: 60–3000 
Clearing addresses in MAC 
table 
clear-mac-table 
 
Assigning a name to the bridge  
name 
To delete the bridge name, type no 
name. 
Configuring bridge ports (see 
Configuring Bridge Ports) 
port <port-number> 
Range is 1–18 
To delete a bridge port, enter 
no port <port-number>. 
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Defining VLANs (see below) 
vlan <vlan-id>  
Possible values: 1–4094 
To delete a VLAN, enter 
no vlan <vlan-id> 
Note: This command is available only if 
the bridge is VLAN-aware. 
Displaying VLAN information, 
including which bridge ports 
have been automatically 
added as tagged VLAN 
members 
show vlans 
 
Configuring Bridge Ports 
The following commands are available in the port level, at the config>bridge(1)>port(<port-number>)# 
prompt. 
Task 
Command 
Comments 
Assigning a name to the bridge 
port 
name <port-name> 
To delete the bridge port name, 
enter no name. 
Administratively enabling the 
bridge port 
no shutdown 
To administratively disable the 
bridge port, enter shutdown.  
Configuring VLAN 
The following commands are available in the vlan level, at the config>bridge(1)>vlan(<vlan-id>)# 
prompt. 
Task 
Command 
Comments 
Configure VLAN name 
name  
 
Add bridge ports to VLAN 
tagged list 
tagged-egress <bridge port 
list> 
 
You can set a list and/or range of 
ports, for example: 1,5..10 
no tagged-egress <bridge port list> 
command removes bridge ports 
from the list           
Megaplex-1 
8. Traffic Processing 
Examples  
This section illustrates the following configuration: 
• 
VLAN-aware bridge, with bridge ports 1–4 
• 
VLAN 100 used for management 
• 
VLAN 300 used for TDM traffic 
• 
VLAN 500 used for Ethernet traffic 
• 
Management flows (bidirectional) between SVI 1 and bridge port 1 3 
• 
Traffic flows (bidirectional) between: 
 
FE Ethernet port 0/3 and bridge port  1 4, with classification match all 
 
GbE Ethernet port 0/1 and bridge port 1 2, with classification of double VLAN: VLAN 400 as 
outer VLAN; VLAN 100, 300, 500 as inner VLANs 
 
 
#*******Configure SVI 
configure port  
  svi 1 
    name “Router” 
    no shutdown 
    exit 
  svi 2 
    name “PW” 
    no shutdown 
    exit 
  exit all 
 
#*******Configure bridge  
configure bridge 1 
  vlan-aware 
 
#*******Configure bridge ports 
  port 1 
     no shutdown 
    exit 
  port 2 
    no shutdown 
    exit 
  port 3 
    no shutdown 
    exit 
Megaplex-1 
8. Traffic Processing 
  port 4 
    no shutdown 
    exit 
 
#*******Configure VLANs 
  vlan 100 
    exit 
  vlan 300 
    exit 
  vlan 500 
    exit all 
 
#*******Configure classifier profiles 
 
configure flows 
  classifier-profile “match-all” match-any  
    match all 
    exit 
  classifier-profile “match-100” match-any  
    match vlan 100 
    exit 
  classifier-profile “match-400-100” match-any  
    match vlan 400 inner-vlan 100 
    exit 
  classifier-profile “match-300” match-any 
    match vlan 300 
    exit 
  classifier-profile “match-400-300” match-any  
    match vlan 400 inner-vlan 300 
    exit 
  classifier-profile “match-500” match-any 
    match vlan 500 
    exit 
  classifier-profile “match-400-500” match-any 
    match vlan 400 inner-vlan 500 
    exit 
#*******Configure management flows 
   
  flow 3 
  classifier “match-all” 
  ingress-port svi 1 
  egress-port bridge-port 1 3 
  vlan-tag push vlan 100 p-bit fixed 7 
  reverse-direction 
Megaplex-1 
8. Traffic Processing 
  no shutdown 
  exit 
 
#*******Configure management flow to physical port 
  flow 2 
  classifier “match-400-100”  
  ingress-port ethernet 0/1 
  egress-port bridge-port 1 2  
  vlan-tag pop vlan 
  reverse-direction  
  no shutdown 
  exit  
 
#*******Configure bidirectional traffic flows 
flow 1 
  classifier “match-all” 
  ingress-port svi 2 
  egress-port bridge-port 1 1  
  vlan-tag push vlan 300 p-bit fixed 7 
  reverse-direction  
  no shutdown 
  exit  
 
flow 4 
  classifier “match-400-300”  
  ingress-port ethernet 0/1  
  egress-port bridge-port 1 2 
  vlan-tag pop vlan 
  reverse-direction  
  no shutdown 
  exit 
 
flow 5 
  classifier “match-all” 
  ingress-port ethernet 0/3 
  egress-port bridge-port 1 4   
  vlan-tag push vlan 500 p-bit fixed 7 
  reverse-direction  
  no shutdown 
  exit  
 
 
flow 6 
  classifier “match-400-500” 
Megaplex-1 
8. Traffic Processing 
  ingress-port ethernet 0/1 
  egress-port bridge-port 1 2 
  vlan-tag pop vlan 
  reverse-direction  
  no shutdown 
  exit all 
Displaying VLAN Information  
This section illustrates displaying VLAN information after performing the configuration specified in 
VLAN-Aware Bridge. The VLAN information shows the following: 
VLAN 100 
Bridge ports 2-3 were automatically added as tagged ports. 
VLAN 100 
Bridge ports 1-2 were automatically added as tagged ports. 
VLAN 200 
Bridge ports 2,4 were automatically added as tagged ports. 
 
# configure bridge 1 
config>bridge(1)# show vlans 
 
VLAN ID : 100   Name  : BRIDGE 1, VLAN 100 
 
Tagged Ports   : 2,3 
 
VLAN ID : 300   Name  : BRIDGE 1, VLAN 300 
 
Tagged Ports   : 1,2 
 
 
VLAN ID : 500   Name  : BRIDGE 1, VLAN 500 
 
Tagged Ports   : 2,4 
Displaying MAC Table  
You can display a Megaplex-1 MAC table, which provides information on dynamic addresses, and the 
bridge ports and VLANs associated with them. 
 To display MAC address table: 
• 
At the config>bridge(bridge_number)# prompt, enter show mac-table.  
The MAC address table is displayed. 

## 8.2 Cross-Connections  *(p.289)*

Megaplex-1 
8. Traffic Processing 
Note 
Megaplex-1 displays only the first 1000 entries. To view the entire MAC table, 
download it to your PC, using SFTP. See File Operations in Chapter 10.  
# configure bridge 1 
>config>bridge(1)# show mac-table  
 
VLAN  MAC Address       Port Status      Vlan Name 
--------------------------------------------------------------- 
20    00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 20 
40    00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 40 
50    00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 50 
60    00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 60 
60    00-00-00-00-00-E1 7    Dynamic     BRIDGE 1, VLAN 60 
100   00-00-00-00-00-E1 7    Dynamic     BRIDGE 1, VLAN 100 
100   01-02-03-04-05-06 2    Static      BRIDGE 1, VLAN 100 
130   00-00-00-00-00-E1 7    Dynamic     BRIDGE 1, VLAN 130 
150   00-00-00-00-00-E1 7    Dynamic     BRIDGE 1, VLAN 150 
160   00-00-00-00-00-E1 7    Dynamic     BRIDGE 1, VLAN 160 
170   00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 170 
180   00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 180 
190   00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 190 
200   00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 200 
200   00-00-00-00-00-E1 7    Dynamic     BRIDGE 1, VLAN 200 
230   00-00-00-00-00-E1 7    Dynamic     BRIDGE 1, VLAN 230 
250   00-00-00-00-00-E1 7    Dynamic     BRIDGE 1, VLAN 250 
260   00-00-00-00-00-E1 7    Dynamic     BRIDGE 1, VLAN 260 
270   00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 270 
280   00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 280 
290   00-00-00-00-00-01 2    Static      BRIDGE 1, VLAN 290 
290   00-00-00-00-00-E1 7    Dynamic     BRIDGE 1, VLAN 290 
8.2 Cross-Connections   
Megaplex-1 features the following types of cross-connect: 
• 
DS0 – DS0 cross-connect between ds1/e1/t1 ports on one side and e1/t1/serial/voice/ds1-opt 
ports on the other side 
• 
TDM – cross-connect of full data streams (between unframed e1/t1 and ds1 ports)  
• 
PW-TDM –pseudowire cross-connect between e1/t1/ds1 ports and PWs. 
Megaplex-1 
8. Traffic Processing 
Factory Defaults 
No cross-connections exist in Megaplex-1 by default. 
Benefits  
Cross-connections allow flexible mapping of individual DS0 channels or pseudowire entities. 
DS0 Cross-Connect  
Megaplex-1 supports up to 16 DS1 and  8 E1/T1 ports with cross-connects.  
Megaplex-1 supports up to 16 PWs with DS1 cross connects, remaining 16 PWs can be used only for PW 
protection. 
Configuring a DS0 Cross-Connection  
 To configure a DS0 cross-connection:  
1. At the config# prompt, enter cross-connect or cro.  
The config>xc# prompt appears. 
2. Configure the cross-connection as illustrated and explained below for the various interfaces. 
Task 
Command 
Comments 
Cross-connecting timeslot x  
of the ds1 port to a voice 
port  
ds0 ds1 1/<port> ts <x> voice 
1/<port>  
no ds0 ds1 1/<port> ts <x> voice 
1/<port> removes 
cross-connection  
Cross-connecting timeslot x 
(or range of sequential 
timeslots x1..x2) of the 
ds1/e1/t1 port to a serial 
port  
ds0 {ds1|e1|t1} 1/<port> ts <x> 
serial 1/<port>  
 
no ds0 {ds1|e1|t1} 1/<port> ts 
<x> serial 1/<port> removes 
cross-connection  
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Cross-connecting timeslot x 
(or range of sequential 
timeslots 1..12) of the ds1 
port to a timeslot y (or range 
of sequential timeslots 1..12) 
of a ds1-opt port  
ds0 ds1 1/<port> ts <x> ds1-opt 
1/<port> {ts <y> | start-ts <y1>} 
no ds0 ds1 1/<port> ts <x> ds1-
opt 1/<port> ts <y> removes 
cross-connection  
Cross-connecting timeslot x 
(or range of sequential 
timeslots x1..x2) of the 
ds1/e1/t1 port to timeslot y 
(or range of sequential 
timeslots starting from y1) on 
the e1/t1 port and setting 
its/their type and direction 
ds0 {ds1|e1|t1} 1/<port> ts <x> 
{ds1 | e1 | t1}  1/<port> {ts <y> 
| start-ts <y1>} {data | voice} 
[bi-direction]  
 
no ds0 {ds1|e1|t1} 1/<port> ts 
<x> {ds1 | e1 | t1} 1/<port> ts <y> 
removes cross-connection  
In the current version [bi-
direction] is the only possible 
mode. 
 
TDM Cross-Connect 
 To configure a TDM cross-connection: 
1. At the config# prompt, enter cross-connect or cro. 
The config>xc# prompt appears. 
2. Configure the cross connection as illustrated and explained below for the various interfaces. 
Task 
Command 
Comments 
Cross-connecting the full 
payload from this ds1 port 
with an unframed e1 port 
tdm ds1 1/<port>  e1  1/<port>  
 
no tdm ds1 e1  1/<port> 
command disables the cross-
connection  
PW-TDM Cross-Connect  
Configuring a PW-TDM Cross-Connection 
When using the PW-TDM cross-connect for E1/T1 ports, line-type must be compatible with the PW type, 
as follows: 
Megaplex-1 
8. Traffic Processing 
• 
If the PW type is ces-psn-data, the E1/T1 port line-type must be g723n or g723n-crc for E1; esf 
for T1. 
• 
If the PW type is e1satop or t1satop, the E1/T1 port line-type must be unframed. 
 To configure a pw-tdm cross connection: 
1. In the case of E1/T1 ports, make sure that the line-type is configured correctly (see above).  
2. At the config# prompt, enter cross-connect or cro. 
The config>xc# prompt appears. 
3. Configure the cross connection as illustrated and explained below. 
 
 
Task 
Command 
Comments 
Establishing cross-
connection 
between this 
pseudowire and 
ds1 port 
 
pw-tdm pw <pw number> ds1 1/<port>  
time-slots <ts list> 
 
The ds1 port should be populated by using 
additional ds0 cross-connect command 
between ds1 and other ports in Megaplex-1 
(see example below) 
Timeslots in a list can be separated by a comma 
or given as a range, for example: 1..3, 5. 
The specified timeslots must be compatible with 
the payload size and rate specified for the PW 
via the tdm-payload command. 
Using no before the command removes the 
cross-connection 
Cross-connect cannot be configured to PWs 
defined as protection ports. 
A single PW can be connected to a single DS1 
port, although a DS1 port can be connected to 
several PWs.  
Establishing cross-
connection 
between this 
pseudowire and 
e1/t1 port 
pw-tdm pw <pw number> {e1 1/<port> 
| t1 1/<port>}   
 
 
Using no before the command removes the 
cross-connection 
Cross-connect cannot be configured to PWs 
defined as protection ports. 
Megaplex-1 
8. Traffic Processing 
Viewing the Cross-Connect Summary  
You can view a summary of the cross connections configured in the system. 
 To view the cross-connections summary: 
• 
At the config>cross-connect# prompt, enter show summary followed by the option listed in the 
table below.  
The summary of configured cross-connects appears. 
Task 
Command 
Comments 
Display all connections in the system 
all 
 
Display DS0 connections in the system 
ds0 {all | port-type  
{ds1|e1|t1} <port-type>| 
port-index {ds1|e1|t1} 
<port-index> } 
 
Display PW-TDM connections in the 
system 
pw {all | number  <pw-
num>} 
 
Display TDM connections in the system 
tdm {all | port-type  ds1 
| port-index ds1 <port-
index> } 
 
Example 1. Viewing all PW Connections in the System 
config>xc# show summary pw all 
PW XC 
------------------------------------------------------------------------
----- 
1                      1/1        TS  : 1 
2                      1/2        TS  : 1..2 
3                      1/3        TS  : 1..5, 8..10 
4                      1/4        TS  : 1 
5                      1/5        TS  : 1 
6                      1/6        TS  : 1 
Example 2. Viewing all DS0 Connections in the System for DS1 Ports 
config>xc# show summary ds0 port-type ds1 
DS0 XC 
------------------------------------------------------------------------ 
DS1       1/1     TS  1       BITS    Serial   1/1       TS           
Data   Bi-Direction 
Megaplex-1 
8. Traffic Processing 
DS1       1/1     TS  2       BITS    DS1 OPT  1/1       TS           
Data   Bi-Direction 
DS1       1/2     TS  1       BITS    Serial   1/2       TS           
Data   Bi-Direction 
DS1       1/2     TS  2       BITS    Serial   1/2       TS           
Data   Bi-Direction 
DS1       1/3     TS  1       BITS    Serial   1/3       TS           
Data   Bi-Direction 
DS1       1/3     TS  2       BITS    Serial   1/3       TS           
Data   Bi-Direction 
DS1       1/3     TS  3       BITS    Serial   1/3       TS           
Data   Bi-Direction 
Configuration Errors 
The table below lists messages generated by Megaplex-1 when a configuration error is detected.  
Message 
Description 
DS0 XC: Serial port rate does not 
match timeslot configuration 
The number of timeslots configured in the ds0 cross connect 
for this serial port must match the rate configured for the 
port. 
DS0 XC: Interface is already cross-
connected to another DS1 port  
This serial/voice port is already cross connected to another 
DS1 port.  
DS0 XC: Cross connect over voice port 
is already configured 
Only one cross-connect can be configured per voice port. 
DS0 XC: Only 12 timeslots assignment 
allowed for DS1-OPT interface  
You cannot configure more than 12 cross-connects per ds1-
opt port. 
DS0 XC: Fail to get data from DB 
Database problem. Try to reconfigure DS0 cross-connect. 
DS0 XC: Illegal ports state, DS1 port is 
down 
The port cannot be set to “no shutdown” if the 
corresponding DS1 port is in “shutdown”. 
DS0 XC: Illegal destination slot/port 
configuration 
Cross-connect can be configured between ds1 port and serial 
port or between ds1 or voice port only. 
DS0 XC: Illegal timeslots assignment 
Cross-connect timeslot configuration does not match DS1 
frame type and/or port rate. 
DS0 XC: Illegal signaling method, ts 16 
is used for signaling 
Time slot 16 is used for signalig and cannot participate in 
data cross-connect. 
DS0 XC: Incorrect timeslots type for 
this interface 
Timeslot type must be configured as “data” for serial/ ds1-
opt ports and “voice” for voice ports. 
Megaplex-1 
8. Traffic Processing 
Message 
Description 
DS0 XC: Illegal port, used as protection 
port in a tdm group 
Cross-connect cannot be configured over a port used as a 
protection port in tdm group. 
DS0 XC: Illegal signaling method. Ds1 
signaling is off but voice signaling is on 
When a voice port with signaling is cross-connected with a 
DS1 port, signaling must be configured on the DS1 port as 
well. 
DS0 XC: Illegal ports state, cross-
connect not configured 
Cross-connect must be configured in order to set this port to 
“no shutdown”. 
DS0 XC: PW cross-connect must be 
configured for this DS1 
Both DS0 cross connect and PW cross connect must be 
configured for this DS1 port. 
DS0 XC: Illegal PW type used for ds0 
cross-connect 
PW type must be ces-psn-data. 
DS0 XC: Illegal line type configuration 
Line-type of this e1/t1 port cannot be set to unframed. 
PDH_FrameType Change while Cross 
Connect exists for this port.  
You cannot change pdh-frame-type if a cross-connect is 
configured on it  
PDH_FrameType Change: Cross 
connect exists for this port Please 
perform Commit before changing the 
PDH frame type 
You are trying to change pdh-frame-type and remove cross-
connect simultaneously. First remove cross-connect and 
perform commit. 
PW XC: Fail to get data from DB 
Database problem. Try to reconfigure DS0 cross-connect. 
PW XC: Illegal number of timeslots is 
configured for this port 
The number of timeslots configured in pw cross-connect 
must be higher than the number of timeslots configured in 
ds0 cross connect. 
PW cross-connect must be configured 
for both working and protection TDM 
group ports 
Each port configured  in a tdm protection group must also be 
configured in pw cross-connect. 
PW XC: Different Number of timeslots 
on the working and protection ports 
for TDM group  
pw xc configuration The number of timeslots configured in 
pw cross-connect must be the same for both ports 
participating in tdm group protection. 
PW XC: This PW is already cross-
connected to another DS1 
A PW cannot be cross-connected to more than one DS1 
ports.  
PW XC: This DS1 port is already 
cross-connected to another PW  
A DS1 port cannot be cross-connected to more than one 
PWs. 
PW XC: Illegal jitter-buffer value for 
PW 
Illegal jitter-buffer value is configured for PW 
Megaplex-1 
8. Traffic Processing 
Message 
Description 
PW XC: PW should be in no-shutdown 
state. 
To configure pw cross connect, set this PW to “no-
shutdown”. 
PW XC: PW XC shouldn't be configured 
for protection member 
This pw is used as protection member in a pw group. 
PW: PW XC configured. Can't delete a 
PW. 
You cannot delete a PW if a pw-tdm cross-connect is 
configured for it. 
PW XC: Can't delete PW XC if PW is 
configured as working member in pw 
group  
You cannot delete a pw-tdm cross-connect configured as 
working member in a pw protection group 
 
PW XC: Can't delete PW XC if DS0 XC is 
configured for the DS1 cross-
connected to this pw 
You cannot delete a pw-tdm cross-connect if a DS1 port 
involved in it participates in a DS0 cross-connect. 
 
PW XC: Number of bytes in frame 
exceeds 1900  
The maximum payload value is 1900. 
PW XC: Maximum TDM Payload size 
value is 61 
The maximum tdm-payload value is 61. 
PW XC: wrong payload size for 
signaling voice cross-connect 
In case of a PW cross-connect to a DS1 port which is cross-
connected to a voice port), the tdm-payload size must have 
only the following values:  
• E1 with g732s/g732s-crc framing: 1, 2, 4, 8, 16.  
• T1 with sf/esf framing: 1, 2, 3, 4, 6, 8, 12, 24. 
PW XC: Illegal line type configuration 
Line type of this e1/t1 port must be unframed 
PW XC: DS0 XC exist with illegal line 
type configuration 
The ds1 port is cross-connected to an e1/t1 port with 
wrongly configured line-type parameter. The line-type must 
be unframed. 
PW XC: Direct mapping is illegal for 
CesOverPsn configuration 
PW configured as ces-psn-data cannot be cross-connected 
with e1/t1 port 
PW XC: wrong signaling configuration 
DS1 port signaling must match e1/t1 line-type 
PW XC: Maximum payload size in 
bytes is 1900 
The maximum tdm payload size for SAToP PW must be 1900  
 

## 8.3 Flows  *(p.297)*

Megaplex-1 
8. Traffic Processing 
8.3 Flows 
Traffic is classified into flows, which are unidirectional or bidirectional entities that connect two physical 
or logical ports.  
Standards 
IEEE 802.1ad, IEEE 802.1Q 
Benefits 
User traffic can be classified into different Ethernet flows (EVC.CoS) to provide services in a flexible 
manner. With port classification, you can maintain network security by preventing malicious traffic from 
being forwarded by the port, as well as save network resources by dropping unwanted packets. 
Factory Defaults 
By default, no flow classifiers are configured. 
Functional Description 
All Megaplex-1 flows are bidirectional, so that you only need to define one flow from a port to a bridge 
port, and specify the reverse-direction command. 
Aware and Unaware Traffic  
In general, a given port can serve as the termination point of several flows. Therefore, each flow must 
discriminate among the Ethernet frames (be aware of the frame VLANs) reaching an associated bridge 
port in order to determine how to handle customers’ edge traffic. In general, this action is based on the 
user’s VLAN identifier (VLAN ID) received in each frame. For untagged or priority-tagged traffic, a push 
VLAN ID command must be added for handling the Ethernet traffic via the bridge.  
The range of specific VLAN IDs that can be used for Ethernet traffic with IEEE 802.1Q tags is 1 to 4094.  
 
Megaplex-1 
8. Traffic Processing 
Flow Classification  
The ingress traffic is first classified into flows according to classification profiles. The classification is per 
port and is applied to the ingress port of the flow. Packets can be classified by means of their VLAN IDs 
or port-based.  
In the following descriptions, VLAN refers to the service provider (outer) VLAN, sometimes referred to as 
SP-VLAN, while inner VLAN refers to the Customer Entity VLAN, sometimes referred to as CE-VLAN or 
C-VLAN. 
ETH Traffic Handling  
Ingress traffic is classified based on the classifier profile and changed via editing command (on the flow 
level). You can perform marking and tagging actions on the outer and inner VLAN such as adding, 
replacing, or removing, as well as marking with p-bit. Only certain combinations of actions on the outer 
and inner VLAN are allowed. Flow editing rules depend on the following: 
• 
Ingress and Egress ports of the flow 
• 
Whether the editing is done before or after the bridge. 
Traffic ending in the bridge port should always contain a VLAN. This VLAN is VPN VLAN that should be 
configured in the bridge configuration. 
After the bridge, the packet is classified again and the final editing is done based on adding commands 
on the flow level.   
Configuring a Classifier Profile  
You can define classifier profiles to apply to flows for flow classification. 
 To define a classifier profile: 
1. Navigate to the flows context (config>flows). 
2. Define a classifier profile and assign a name to it: 
classifier-profile <profile-name> match-any  
The system switches to the context of the classifier profile (config>flows>classifier-
profile(<profile-name>)). 
3. Specify the criteria for the classifier profile:  
[no] match [ vlan <vlan ID> ] [ inner-vlan <vlan ID> ] [ all ]  
Megaplex-1 
8. Traffic Processing 
Note 
For Fast Ethernet ports only match all and match [vlan <vlan ID>] are 
allowed.  
4. When you have completed specifying the criteria, enter exit to exit the classifier profile context. 
Examples: 
 To create classifier profile with criteria VLAN 20 and inner VLAN 30: 
exit all  
configure flows classifier-profile v20_inner_30 match-any 
match vlan 20 inner-vlan 30 
exit all 
 To create classifier profile that matches all criteria: 
exit all  
configure flows classifier-profile all match-any 
match all 
exit all 
Configuring Flows  
 To create and configure a flow: 
1. Navigate to the flows context (config>flows). 
2. Define a flow and assign a name to it: 
flow <flow-name> 
The system switches to the respective flow context (config>flows>flow(<flow-name>)) 
3. Specify the flow as explained in the table below.  
Task 
Command 
Comments 
Administratively enabling 
the flow (the flow is created 
as inactive by default) 
no shutdown  
You can activate a flow only if it is 
associated with at least a classifier 
profile, ingress port, and egress 
port. 
Using shutdown disables the flow  
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Mapping the previously 
configured classifier profile 
to the flow 
classifier-profile <classifier-
profile name>  
no classifier removes the mapping 
For FE ports, this command is 
possible only with classifier match 
all or match [vlan <vlan ID>] 
Specifying the egress port 
(bridge port, svi)  
 
egress-port  bridge-port <bridge 
port number>  
egress-port  svi <port number> 
(only for ingress-port mng-
ethernet 0/0) 
•  
Specifying the opposite flow 
reverse-direction  
 
Flows with same ingress port must 
have same queue-map-profile  
Specifying the ingress port 
(ethernet, svi, mng-
ethernet)  
ingress-port ethernet <port 
number> 
ingress-port  svi <port number> 
ingress-port mng-ethernet 0/0 
•  
Adding VLAN ID with p-bit 
set to specific value, and 
optionally adding inner VLAN 
ID with p-bit set to specific 
value  
vlan-tag push vlan <sp-vlan> p-
bit fixed <fixed-p-bit>   
 
For FE ports, this command is 
possible only with classifier match 
all 
Adding VLAN ID with p-bit 
copied from the receieved 
VLAN tag 
vlan-tag push vlan <sp-vlan> p-
bit copy  
For GbE ports only 
 
Removing VLAN ID, and 
optionally removing inner 
VLAN ID  
vlan-tag pop vlan 
For GbE ports only 
 
Removing editing 
no vlan-tag  
 
 
Examples  
See example in Bridge section. 
Megaplex-1 
8. Traffic Processing 
Testing Flows  
No testing is available for flows in the current product version. 
Viewing Flow Status  
You can display the operational status and reverse operational status of a flow, as well as the service 
name for flows configured with a service. Fault propagation actions are visible only for flows configured 
with fault propagation and fault propogation license activated. 
Example 
 
 To display flow status: 
# configure flows flow a1 
config>flows>flow(a1)# show status 
Operational Status                   : Down 
Reverse Operational Status           : Up 
 
Status Details 
----------------------------------------------------------------------
------- 
                                     : Ingress Port Oper Status: Down 
Configuration Errors 
The table below lists messages generated by Megaplex-1 when a configuration error is detected. 
Message 
Description 
Management flow criteria must be 
Unclassified, VLAN ID, or VLAN ID + 
Inner VLAN ID  
Management flow criteria may be “Unclassified”, “VLAN ID”, 
or “VLAN ID + Inner VLAN ID” only 
Unsupported combination of vlan-
tagging and marking 
Marking is not supported in Megaplex-1 
Overlapping mapping entries on 
current port 
Two or more flows with the same ingress port use the same 
VLAN 
Megaplex-1 
8. Traffic Processing 
Message 
Description 
Classification Profile: Exceeds number 
of matches per profile 
Only one match is allowed for classification profile 
Classification Profile: unsupported 
criteria!  
Criteria may be Unclassified, VLAN ID or VLAN ID + Inner 
VLAN ID only 
A classifier without a match to an 
active flow cannot be assigned 
Classification profile must include a match for binding it to 
flow 
Flow to/from svi can be added only if 
svi is activated 
To configure a flow with SVI as an ingress port, you must set 
this SVI to “no shutdown”. 
You cannot change a parameter in 'no 
shutdown' state 
To change any parameter in a flow, the flow has to be in 
shutdown state 
Egress port or Ingress port is missing 
To configure a flow, you have to define both egress and 
ingress ports. 
You cannot activate a flow without a 
classifier 
In order to set flow to “no shutdown” state, you have to 
connect a classification profile to it 
Reverse flow does not exist 
In order to set a flow to “no shutdown” state, you have to 
define a reverse flow 
Bridge port does not exist or is not 
active 
To set flow with egress port = bridge port  to “no shutdown” 
state, the bridge port must be in “no shutdown”  state 
Ingress and egress ports can't be SVI 
Both ingress and egress ports cannot be configured to SVI.  
Flow must have classification or 
editing 
In order to set a flow to “no shutdown” state, you must have 
a classification profile configured with one of the following 
criteria: 
• “Unclassified” 
• “VLAN ID” 
• “VLAN ID + Inner VLAN ID” 
Egress port in shutdown state 
To activate a flow, configure the egress port to “no 
shutdown”. 
Ingress port in shutdown state 
To activate a flow, configure the ingress port to “no 
shutdown”. 
Flow cannot be configured with an SVI 
without a pre-configured router 
interface 
To configure a management flow with SVI as an ingress port, 
you must first confure a router interface connected to this 
SVI. 
Router Interface: Router Interface 
cannot be deleted or disabled while 
connected to an active flow 
A router Interface cannot be deleted or disabled while 
connected to an active flow. 

## 8.4 Quality of Service (QoS)  *(p.303)*

Megaplex-1 
8. Traffic Processing 
Message 
Description 
Flow must be configured for SVI that is 
bound to PW UDP over IP 
To set a “udp-over-ip” pw to “no shutdown” state, you must 
configure a flow with the corresponding svi connected to a 
router interface 
You cannot remove a reverse flow 
from a flow in active state 
For each flow in “no shutdown” state, a reverse flow has to 
be configured 
Invalid VLAN ID 
VLAN ID must be in the range 1.. 4094. 
Unable to configure both flow vlans 
and PW Vlan 
For a PW with UDP over IP encapsulation, VLAN can be 
configure on the flow only 
For PW UDP over IP vlan can be 
configured on flow only, for PW MEF 
vlan must be configured on pw or on 
flow. 
For PW UDP over IP encapsulation, VLAN can be configured 
on a flow only; for PW MEF encapsulation, VLAN must be 
configured on a pw or on a flow. 
8.4 Quality of Service (QoS) 
The Megaplex-1 Quality of Service (QoS) parameters include the following profiles: 
• 
Queue map profiles 
• 
Queue block profiles 
• 
Queue group profiles 
• 
Queue internal profiles 
• 
Shaper profiles    
• 
Policer profiles.   
These profiles can be applied to the traffic flows to ensure the desired flow prioritization. 
Standards 
The following standards are supported:  
• 
IEEE 802.1p 
• 
IEEE 802.1Q 
Megaplex-1 
8. Traffic Processing 
• 
MEF 10.3 
Benefits 
QoS allows you to optimize bandwidth for traffic at different requirements of speed and quality. 
Functional Description 
Traffic Management 
Megaplex-1 traffic management entities are called queue groups. They are configured over physical 
ports. The queue groups consist of 1-level scheduling element (single queue block) per port. The queue 
blocks consist of internal queues.  
Additionally, shapers operate at per-scheduling-element level to shape traffic into a required traffic 
profile (CIR, CBS).   
Each queue block includes scheduling queues in accordance with CoS delivery priorities. Flow packets 
are mapped to a queue according a queue mapping profile (p-bit to queue). 
Scheduling  
Megaplex-1 supports a combination of traffic scheduling techniques, whereby applications requiring low 
latency and jitter are mapped to Strict priority queues, while other services are mapped to the 
remaining slots using weighted fair queuing (WFQ):  
• 
The Strict priority queues ensure minimal latency and jitter for the RT traffic, even when a large 
amount of bursty data traffic is sent over the same uplink. Strict priority traffic is always 
processed first, while flows mapped to the WFQ slots are buffered until the strict priority 
queues are empty. 
• 
The WFQ technique avoids scheduling starvation of lower priority queues and ensures relatively 
fair allocation of bandwidth by sharing it among all flows. In this manner, packets belonging to 
lower classes of service are not penalized when higher priority queues are not empty and may 
still receive transmission time. QoS-conformant scheduling is handled by assigning different 
weights to the various queues instead of equally dividing overall bandwidth among all active 
flows. 
Megaplex-1 
8. Traffic Processing 
Factory Defaults 
See the following sections for each QoS type specific defaults. 
Bandwidth Profiles 
Megaplex-1 supports the following bandwidth profiles: 
Shaper profile 
Applied to queue group blocks, shaping egress traffic 
Policer profile  
Applied to Ethernet ports, limiting ingress traffic  
You can control the egress bandwidth utilization by defining the committed information rate and 
committed burst size in shaper and policer profiles.  
CIR 
Defines the Committed Information Rate (CIR) for the current 
profile. The CIR specifies a bandwidth with committed service 
guarantee (“green bucket” rate). 
CBS 
Defines the Committed Burst Size (CBS) for the current profile. The 
CBS specifies the maximum guaranteed burst size (“green bucket” 
size). 
Factory Defaults  
Megaplex-1 provides default bandwidth profiles, as specified in the following table.  
Default Bandwidth Profiles 
Profile Type and Name 
CIR 
CBS  
FeDefaultShaper 
100000  
- 
GbeDefaultShaper  
1000000 
- 
FeDefaultPolicer  
100000  
65535 
GbeDefaultPolicer 
1000000 
65535 
Configuring Shaper Profiles 
You can configure shaper profiles and apply them to queue group blocks as needed. 
Megaplex-1 
8. Traffic Processing 
Adding Shaper Profiles 
 To add a shaper profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type: 
shaper-profile <shaper-profile-name>. 
A shaper profile with the specified name is created and the config>qos>shaper-profile(<shaper-
profile-name>)$ prompt is displayed. The new shaper profile parameters (except for name) are 
configured by default as described in Factory Defaults. 
3. Configure the shaper profile as described in Configuring Shaper Profile Parameters. 
Configuring Shaper Profile Parameters 
 To configure shaper profiles: 
1. Navigate to configure qos shaper-profile <shaper-profile-name> to select the shaper profile to 
configure. 
The config>qos>shaper-profile(<shaper-profile-name>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying the CIR (Kbps) 
and CBS (bytes) 
bandwidth limits  
 
bandwidth [cir 
<cir-kbit-sec>] [cbs 
<cbs-bytes>]  
• CIR allowed values: 64–1000000 
• CBS allowed values: 0, or 4000–
16773000  
• CIR granularity for 1GbE ports: 64 kbps 
• CIR granularity for FE ports:  
 
between 64 kbps – 1 Mbps: 64 kbps 
 
between 1 Mbps – 100 Mbps: 1Mbps  
 
between 100Mbps – 1000Mbps: 
10Mbps 
 
The value entered by the user is 
rounded up to the closest 
n*<granularity> value. For example, if 
you enter 100 kbps, the closest 
n*<granularity> value and the actual 
rate will be 128 kbps.  
 
Megaplex-1 
8. Traffic Processing 
Examples 
 To create and configure a shaper profile named Shap2: 
• 
CIR = 99,840 Kbps 
• 
CBS = 32,000 bytes  
exit all  
configure qos shaper-profile Shap2 
  bandwidth cir 99840 cbs 32000 
  exit all 
Configuring Policer Profiles 
This section explains functionality and configuration of policer profiles for traffic policing and rate limit. 
Policer profiles are applied to Ethernet ports.  
A port policer profile is supported by binding a policer BW profile to the Ethernet port. This BW profile 
can only be configured with CIR and CBS bandwidth parameters. 
Adding Policer Profiles 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type: 
policer-profile <policer-profile-name> 
A policer profile with the specified name is created and the following prompt is displayed:  
config>qos>policer-profile(<policer-profile-name>)$  
The new policer profile parameters (except for name) are configured by default as described in 
Factory Defaults. 
3. Configure the policer profile as described in Configuring Policer Profile Parameters. 
Configuring Policer Profile Parameters 
4. Navigate to configure qos policer-profile <policer-profile-name> to select the policer profile to 
configure. 
The config>qos>policer-profile(<policer-profile-name>)# prompt is displayed. 
5. Enter all necessary commands according to the tasks listed below. 
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Specifying the CIR (Kbps) 
and CBS (bytes) 
bandwidth limits  
bandwidth 
[cir <cir-kbit-sec>] 
[cbs <cbs-bytes>]  
 
• CIR allowed values: 64–1000000   
• CBS allowed values: 4500–16773000     
• CBS should be greater than the maximum 
frame size. 
• CIR granularity for 1GbE ports: 64 kbps 
• CIR granularity for FE ports:  
 
between 64 kbps – 1 Mbps: 64 kbps 
 
between 1 Mbps – 100 Mbps: 1Mbps  
 
between 100Mbps – 1000Mbps: 
10Mbps  
• The value entered by the user is rounded up 
to the closest n*<granularity> value. For 
example, if you enter 100 kbps, the closest 
n*<granularity> value and the actual rate will 
be 128 kbps. 
 
Examples 
 To create and configure a policer profile named Policer4: 
• 
CIR = 50,000 Kbps 
• 
CBS = 28,000 bytes  
exit all 
configure qos policer-profile Policer4 
  bandwidth cir 50000 cbs 28000  
  exit all 
 To display the configuration information for policer profile Policer4: 
# configure qos policer-profile Policer4 
config>qos>policer-profile(Policer4)# info detail 
    bandwidth cir  50000 cbs  28000   
Note 
The actual CIR value is 50048 and CBS value is 28672 (the CBS granularity is 
4096 rounded up).  
Megaplex-1 
8. Traffic Processing 
Queue Mapping Profiles 
To differentiate traffic, ingress traffic is prioritized according to the 802.1p requirements. The IEEE 
802.1p standard specifies eight classes of service per user-defined queue map profile. These classes of 
service are associated with priority values between 0 and 7, using the 3-bit user priority field in an 
IEEE 802.1Q header added to VLAN-tagged frames within an Ethernet frame header. Queue mapping 
profiles are used to define the method and values for mapping packet attributes (P-bit only) to internal 
priority queues. 
For each profile, you have to define the queue mapping to map the user priority values to the internal 
queue values. The internal queues are combined into a queue profile, which can be assigned to a queue 
block. 
Queue mapping profile is the same for all Ethernet ports in the chassis.  
Factory Defaults 
Megaplex-1 provides a default queue mapping profile named qmappbit, which can be used when the 
ingress traffic is prioritized according to the 802.1p requirements. It is defined with classification p-bit, 
and the following mappings:  
• 
Map p-bit 0 to queue 7. 
• 
Map p-bit 1 to queue 6. 
• 
Map p-bit 2 to queue 5. 
• 
Map p-bit 3 to queue 4. 
• 
Map p-bit 4 to queue 3. 
• 
Map p-bit 5 to queue 2. 
• 
Map p-bit 6 to queue 1. 
• 
Map p-bit 7 to queue 0. 
Adding Queue Mapping Profiles 
When you create a queue mapping profile, you specify the name and the classification method (always 
p-bit). 
 To add a queue mapping profile: 
1. Navigate to configure qos. 
Megaplex-1 
8. Traffic Processing 
The config>qos# prompt is displayed. 
2. Type: 
queue-map-profile <queue-map-profile-name> classification p-bit 
A queue mapping profile with the specified name and classification method is created and the 
following prompt is displayed: 
config>qos>queue-map-profile(<queue-map-profile-name>)$. The mappings for the new 
profile are configured by default as described in Factory Defaults.  
3. Configure the queue profile mappings as described in Configuring Queue Mappings. 
Configuring Queue Mappings 
 To configure queue mappings: 
1. Navigate to config qos queue-map-profile <queue-map-profile-name> to select the queue 
mapping profile to configure. 
The following prompt is displayed: 
config>qos>queue-map-profile(<queue-map-profile-name>)# 
2. Map the user priorities to queue IDs as follows: 
 
map <0-7> to-queue <0-7> 
Example 
 To create and configure a queue mapping profile named QMapPbit1 with classification p-bit:  
• 
Map priority 0 to queue 3. 
• 
Map priority 4 and 6 to queue 2. 
exit all 
configure qos queue-map-profile QMapPbit1 classification p-bit 
  map 0 to 3 
  map  1..3 to-queue 0 
  map 4 to-queue 2 
  map 6 to-queue 2  
  exit all 
 To display the configuration information for queue mapping profile QMapPbit1: 
# configure qos queue-map-profile QMapPbit1  
config>qos>queue-map-profile(QMapPbit1)# info detail 
Megaplex-1 
8. Traffic Processing 
    map 0 to-queue 3 
    map 1..3 to-queue 0 
    map 4 to-queue 2 
    map 5 to-queue 0 
    map 6 to-queue 2 
    map 7 to-queue 0 
Queue Block Profiles 
In order to facilitate congestion management, you can sort traffic by applying queue block profiles to 
queue block entities. A queue block profile contains entries for queues, with the internal profiles 
assigned to each queue. The number of queues is 8 for GbE ports and 4 for FE ports. 
Factory Defaults 
Megaplex-1 provides the following default queue block profiles: 
L0StrictDefaultPriority for GbE ports, which defines queues 0–7 as follows: 
config qos queue-block-profile “L0StrictDefaultPriority " 
queue 0 internal-profile profile QueueDefaultStrict 
queue 1 internal-profile profile QueueDefaultStrict 
queue 2 internal-profile profile QueueDefaultStrict 
queue 3 internal-profile profile QueueDefaultStrict 
queue 4 internal-profile profile QueueDefaultStrict 
queue 5 internal-profile profile QueueDefaultStrict 
queue 6 internal-profile profile QueueDefaultStrict 
queue 7 internal-profile profile QueueDefaultStrict 
FEL0StrictDefaultPriority for FE ports, which defines queues 0–3 as follows: 
config qos queue-block-profile “FEL0StrictDefaultPriority " 
queue 0 internal-profile profile QueueDefaultStrict 
queue 1 internal-profile profile QueueDefaultStrict 
queue 2 internal-profile profile QueueDefaultStrict 
queue 3 internal-profile profile QueueDefaultStrict 
For default internal queue profiles, see the corresponding section. 
Adding Queue Block Profiles 
This section explains how to define queue block profiles. 
Megaplex-1 
8. Traffic Processing 
 To add a queue block profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type:  
queue-block-profile <queue-block-profile-name>  
A queue block profile with the specified name, and number of queues, is created, and the 
following prompt is displayed: config>qos>queue-block-profile(<queue-block-profile-name>)$ 
The queues for the new profile are configured by default as described in Factory Defaults. 
3. Configure the queue block profile as described in Configuring Queue Block Profile Parameters. 
Configuring Queue Block Profile Parameters 
 To configure a queue block profile: 
1. Navigate to config qos queue-block-profile <queue-block-profile-name> to select the queue 
block profile to configure. 
The config>qos>queue-block-profile(<queue-block-profile-name>)# prompt is displayed. 
2. Perform the following for each queue that you wish to configure: 
a. To configure a queue, enter: 
queue <queue-ID 0..7> 
The following prompt is displayed: 
config>qos>queue-block-profile(<queue-block-profile-name>)>queue(<queue-ID>)#. 
b. Assign internal profile for the queue: 
MP-1>config>qos>queue-block-profile(<queue-block-profile-name>)> 
queue(<queue-ID>)$ internal-profile (<internal-profile-name> 
c. Type exit to return to the queue block profile context. 
Examples  
 To create and configure a queue block profile for GbE port named QBlockProf1: 
• 
Queue 1 configured with internal profile InternalQ1 
• 
Other queues left at their defaults 
configure qos queue-block-profile QBlockProf1 
   
Megaplex-1 
8. Traffic Processing 
    queue-block-profile "QBlockProf1" 
        queue 0 
            internal-profile profile "InternalQ1" 
        exit 
        queue 1 
            internal-profile profile "QueueDefaultStrict" 
        exit 
        queue 2 
            internal-profile profile "QueueDefaultStrict" 
        exit 
        queue 3 
            internal-profile profile "QueueDefaultStrict" 
        exit 
        queue 4 
            internal-profile profile "QueueDefaultStrict " 
        exit 
        queue 5 
            internal-profile profile "QueueDefaultStrict" 
        exit 
        queue 6 
            internal-profile profile "QueueDefaultStrict" 
        exit 
        queue 7 
            internal-profile profile "QueueDefaultStrict" 
        exit  
    exit 
Internal Queue Profiles 
To configure queue block profiles, you have first to configure internal queue profiles to assign to each of 
the queues (0-7). An internal queue profile can be configured with the following entries for queues 0–7, 
with the following scheduling methods: 
• 
Strict – high-priority queues that are always serviced first. If a lower-priority queue is being 
serviced and a packet enters a higher queue, that queue is serviced immediately.  
• 
WFQ (weighted fair queuing) – If one port does not transmit, its unused bandwidth is shared by 
the ‘transmitting’ queues according to the assigned weight. WFQ frames are transmitted only 
after transmission of any frames associated with Strict queues is completed.  
Megaplex-1 
8. Traffic Processing 
Factory Defaults 
Megaplex-1 provides a default internal queue profile named QueueDefaultStrict, which defines strict 
scheduling method. 
Adding Internal Queue Profiles 
This section explains how to define internal queue profiles. 
 To add an internal queue profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type:  
queue-internal-profile <queue-internal-profile-name> 
An internal queue profile with the specified name is created, and the following prompt is 
displayed: config>qos> queue-internal-profile (<queue-internal-profile-name>)$ 
The queues for the new profile are configured by default as described in Factory Defaults. 
3. Configure the queue internal profile as described below. 
Configuring Internal Queue Profile Parameters 
 To configure an internal queue profile: 
1. Navigate to config qos queue-internal-profile <queue-internal-profile-name> to select the 
internal queue profile to configure. 
The config>qos>queue-internal-profile(<queue-internal-profile-name>)# prompt is displayed. 
2. Set the scheduling method as follows: 
Task 
Command 
Comments 
Setting scheduling method  
scheduling {strict | wfq 
<weight>} 
The WFQ weight range is 3–1000 
Strict queues must have queue indices lower 
than WFQ queues. 
 
Megaplex-1 
8. Traffic Processing 
Queue Group Profiles 
In order to facilitate congestion management, you can sort traffic by applying queue group profiles.  
Factory Defaults 
Megaplex-1 provides default two queue group profiles. The profiles depend on the 
type of port and are as follows:  
queue-group-profile    
“GbeDefaultQueueGroup" 
queue-block 0/1  
name  "Level0QueueBlock" 
profile 
L0StrictDefaultPriority 
shaper profile 
"GbeDefaultShaper" 
exit  
queue-group-profile   
"FeDefaultQueueGroup" 
queue-block 0/1  
name  "Level0QueueBlock" 
profile 
FEL0StrictDefaultPriority 
shaper profile 
"FeDefaultShaper" 
exit  
For the default profiles mentioned in the above screens see the relevant profile  
sections. 
Adding Queue Group Profiles 
 To add a queue group profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type: 
queue-group-profile <queue-group-profile-name>. 
A queue group profile with the specified name is created and the following prompt is displayed:   
config>qos>queue-group-profile(<queue-group-profile-name>)$ 
The queue group profile parameters are configured by default as described in Factory Defaults. 
3. Configure the queue group profile as described in Configuring Queue Group . 
Megaplex-1 
8. Traffic Processing 
Configuring Queue Group Parameters 
 To configure a queue group profile: 
1. Navigate to config qos queue-group-profile <queue-group-profile-name> to select the queue 
group profile to configure. 
The config>qos>queue-group-profile(<queue-group-profile-name>)# prompt is displayed. 
2. Define a queue block in level 0: 
queue-block 0/1  
3. The following prompt is displayed: 
config>qos>queue-group-profile(<q-grp-profile-name>)>queue-block(<0/1>)# 
4. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning a name to the 
queue block  
name <block-name> 
 
Assigning a queue block 
profile  
profile <queue-block-profile-name> 
The queue-block profile must 
be the same for all Fast 
Ethernet port (for GbE ports 
it can differ by port in the 
chassis) 
Assigning a shaper 
profile 
shaper-profile <shaper-profile-name> 
 
Examples 
Note 
This example uses the shaper profile and queue block profile created in the 
examples in the preceding sections.  
 To create and configure a queue group profile named QGroupProf1: 
• 
Queue block 0/1: 
 
Queue block profile: QBlockProf1 
 
Shaper profile: Shap2 
exit all 
configure qos queue-group-profile QGroupProf1 
   queue-block 0/1 
    profile QBlockProf1 
Megaplex-1 
8. Traffic Processing 
    shaper profile Shap2 
     exit all 
 To display the configuration information for queue group profile QGroupProf1 
 
# configure qos queue-group-profile QGroupProf1 
>config>qos>queue-group-profile(QGroupProf1)# info detail 
     
    queue-block  0/1 
        name  "Put your string here" 
        profile  "QBlockProf1" 
            exit 
    
Configuration Errors  
The table below lists the messages displayed by Megaplex-1 when a configuration error is detected.  
Message 
Description 
Profile was not found 
One of the following: 
• Classification profile connected to a flow is not defined 
• Queue group profile connected to a port is not defined 
Illegal action on default profile 
You cannot delete or change default queue group, queue 
block or internal profile  
Wrong number of internal queue level 
0 
Internal queue on level 0 are numbered 0 to 7 
Queue block profile on level 0 not 
defined 
Queue block profile is not defined on level 0 
Internal profile on level 0 not defined 
Internal queue profile is not defined  
Queue block 0/1 not defined 
Queue block 0/1 is not defined 
You have to assign a queue-group 
profile to the Ethernet port 
You have to assign a queue-group profile to the Ethernet 
port 
Queue group profile does not exist 
The queue group profile you assigned to the Ethernet port is 
not defined 
You have to assign a queue-mapping 
profile to the Ethernet port 
You have to assign a queue-mapping profile to the Ethernet 
port 

## 8.5 Peer  *(p.318)*

Megaplex-1 
8. Traffic Processing 
Message 
Description 
The profile cannot be deleted since it 
is being used 
You cannot delete a profile that is connected to a port or a 
flow 
The profile cannot be changed since it 
is being used 
You cannot change a profile that is connected to a port or a 
flow 
Illegal string length 
Max length of a queue block profile is 32. 
All FE ports must have the same queue 
block profile 
All FE ports must have the same queue block profile 
All FE ports must have the same queue 
mapping profile 
All FE ports must have the same queue mapping profile 
Wrong number of internal queue level 
0 
For a profile connected to FE port, the maximum number of 
internal queues is 4 
Strict queues should be followed by 
wfq queues 
When configuring a queue block profile, strict internal 
queues must be always given numbers lower than wfq 
internal queues 
Queue block should include all queues 
When configuring a queue block profile, all possible internal 
queues must be listed (4 for FE port, 8 for GbE port). 
8.5 Peer  
Remote devices that serve as destinations for pseudowire traffic are referred to as peers. 
Factory Defaults 
No peers exist by default. 
Benefits 
Peers serve as destinations for pseudowire connections for transporting a TDM payload over packet-
switched networks. 
Megaplex-1 
8. Traffic Processing 
Functional Description 
Peers are remote devices operating opposite router interfaces. These devices serve as destinations for 
pseudowire connections for transporting a TDM payload over packet-switched networks. You can define 
up to 12 peers, each assigned a unique index number. The index number is then used to specify the 
pseudowire destination, instead of directly providing the necessary destination information. 
Peers are remote devices operating opposite router interfaces or MAC addresses.  
To configure a UDP/IP peer, it is necessary to provide its IP address, and as an option – the next hop IP 
address (if the peer IP address is not within a router interface subnet).  
For MEF-8 peers, you must specify the either an IP address or a MAC address of the destination device.  
When the MEF-8 peer is a MAC address, the central Megaplex device is configured with a static MAC. In 
this case when the remote device fails needs to be replaced with a different device (with different MAC), 
the peer must be reconfigured with the new MAC to start working. 
When the MEF-8 peer is an IP address, Megaplex-1 learns the remote MAC by ARPs, and the remote 
device failure does not require reconfiguring the peer. 
Adding and Configuring Remote Peers  
Peers are remote devices operating opposite router interfaces or MAC addresses.  
These devices serve as destinations for pseudowire connections for transporting a TDM payload over 
packet-switched networks. You can define up to 12 peers.  
 To add a remote peer:  
• 
At the config>peer # prompt, type the peer number in the range of 1 to 12.  
 To configure a remote peer: 
• 
At the config>peer (peer number) # prompt, enter all necessary commands according to the 
tasks listed below:  
Task 
Command 
Comments 
Defining IP address of a 
remote peer in IP/UDP, or 
MEF-8 Ethernet networks  
ip <valid IP address> 
 
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Assigning a name to a remote 
peer 
name <alphanumeric string > 
 
Specifying the IP address of 
the next port to which packets 
directed to the selected peer 
will be sent 
 
next-hop-ip <valid IP address> 
 
You need to specify a next 
hop IP address only when the 
peer IP address is not within 
the IP subnet of the router 
interface that will be used to 
send packets to this peer.  
The default value, 0.0.0.0, 
means that no next hop IP 
address is defined 
Defining MAC address of a 
remote peer in MEF-8 
Ethernet networks 
mac<valid MAC address> 
 
 To remove a remote peer:  
• 
At the config>peer (peer number) # prompt, type no peer (peer number).  
Note 
Setting remote peers as destinations is done under configure pwe context.  
Viewing the Remote Peer Summary  
You can view a summary of the remote peers configured in the system, both IP- and MAC-based. 
 To view the remote peer summary: 
• 
At the config# prompt, enter show peer-summary. 
The summary of all configured remote peers appears. 
config# show peer-summary 
 
Number : 1 
Name   : Put your string here 
MAC    : 00-01-02-03-04-05 
 
Number : 2 
Name   : Put your string here 
IP     : 172.17.173.23 

## 8.6 Pseudowires  *(p.321)*

Megaplex-1 
8. Traffic Processing 
Examples  
 To configure remote peer 1 for UDP/IP PSN:  
• 
IP address: 9.9.9.9 
• 
Next hop IP address: 0.0.0.0 
• 
Name: peer1. 
configure peer 1 ip 9.9.9.9 name peer1 next-hop-ip 0.0.0.0 
 To configure remote MAC peer 1 for MEF-8 PSN: 
• 
MAC address: 00-20-d6-54-bf-05 
• 
Name: peer2. 
configure peer 1 mac 00-20-d6-54-bf-05 name peer2  
 To configure remote IP peer 1 for MEF-8 PSN: 
• 
IP address: 9.9.9.9 
• 
Name: peer2. 
configure peer 1 ip 9.9.9.9 name peer2  
 To delete remote peer 1:  
config# no peer 1 
Configuration Errors 
See Pseudowires section. 
8.6 Pseudowires  
Pseudowires are an emulation of Layer-2 point-to-point connection-oriented services over packet-
switching networks (PSN).  
The following user-configurable protocols are supported, independently for each pseudowire:  
Megaplex-1 
8. Traffic Processing 
• 
CESoPSN (structure-aware TDM circuit emulation over PSN) in accordance with RFC5086.  
• 
SAToPSN (structure-agnostic TDM over PSN) in accordance with RFC4553.  
Packet formats can be selected on a per-pseudowire basis for optimal transmission over UDP/IP or 
Ethernet-based networks. Each pseudowire can be independently routed to any destination.  
The powerful pseudowire engine in the devices with 8 E1/T1 ports provides up to 16 protected (or up to 
32 unprotected) PWs with up to 31 timeslots per each PW port. All other Megaplex-1 devices provide up 
to 6 protected (or up to 12 unprotected) PWs with up to 31 timeslots per each PW port.  
Standards 
• 
IETF RFC 5086  
• 
ITU-T Y.1453  
In addition, Megaplex-1 meet the requirements for edge-to-edge simulation of TDM circuits over PSN in 
accordance with RFC4197, including high-performance adaptive timing recovery capabilities.  
Benefits  
Pseudowire circuit emulation technology enables packet-based infrastructure to provide TDM services 
with the service quality of an SDH/SONET network.  
Functional Description 
The device supports the CESoPSN and SAToP network encapsulation methods, transmitting   traffic over 
Ethernet (MEF 8) or UDP/IP packet-switched networks.  
Pseudowire Packet Structure 
A PW packet comprises the following data components (see Figure 8-16): 
Ethernet Header 
Contains the DA (destination MAC address), SA (local MAC address), 
and Ethernet network type 
PSN Header 
Defines the PSN transport type: Ethernet or UDP/IP 
Control Word 
Data control as defined in the relevant IETF RFCs and drafts 
Payload 
TDM service payload containing the actual traffic data 
Megaplex-1 
8. Traffic Processing 
Ethernet Header 
PSN Header 
Control Word 
Payload 
 
Note 
The source MAC address is the egress port MAC address for MEF 8 (Ethernet) 
PWs, or the MAC address of the egress router interface for UDP/IP PWs.  
TDM Service Encapsulation 
TDM traffic can be encapsulated over PSN in two modes: 
CESoPSN 
CES (Circuit Emulation Services) over PSN, for framed TDM traffic 
with or without CAS 
SAToP 
Structure-Agnostic TDM over Packet, for unframed E1/T1 traffic 
CESoPSN 
The CESoPSN method is a structure-aware format for framed services. It converts structured data flows 
into IP packets and vice versa with static assignment of timeslots according to IETF RFC 5086 and 
ITU-T Y.1413. The CESoPSN packet size is a multiple of TDM frame size. Figure 8-17  illustrates CESoPSN 
encapsulation without signaling.  
4
25
25
4
25
4
Frame
1
Frame
2
Frame
N
Frame 1
4
25
4
25
4
25
Frame 2
Frame N
L2/L3
Header
Control
Word
CRC
Ethernet Packet
TDM Payload
FRG bits = 00
(no fragmentation)
 
CESoPSN Encapsulation without Signaling, PW with Timeslots 4 and 25  
Megaplex-1 
8. Traffic Processing 
CESoPSN with signaling is applicable only when the cross-connected DS1 is carrying voice traffic with 
signaling. 
SAToP  
The SAToP encapsulation method is used to convert unframed E1/T1 data flows into Ethernet or IP 
packets and vice versa according to IETF RFC 4553. It provides flexible packet size configuration and low 
end-to-end delay. 
 
SAToP Encapsulation 
Encapsulation over Different PSN Types 
The pseudowire connections can be encapsulated by Megaplex-1 for the following types of PSN 
transport networks: 
• 
UDP/IP (UDP over IP) 
• 
MEF 8 (Ethernet). 
PSN Configuration Parameters  
Each pseudowire is handled in accordance with the user-configured PSN parameters, considering the 
user-selected pseudowire parameters, and the framing and signaling mode of the associated DS1/E1/T1 
port.  
Megaplex-1 enables the user to select the PSN type (UDP/IP or Ethernet), and configure the PSN 
transport parameters. 
The PSN parameters, which are reflected in the pseudowire header structure, enable specifying the 
requested priority or quality of service for pseudowire traffic generated by the Megaplex-1. The 
applicable parameters depend on PSN type: 
L2/L3
Header
Control
Word
TDM Payload
CRC
Ethernet
Packet
N TDM Bytes
TDM
Bitstream
FRG bits = 00
(no fragmentation)
Megaplex-1 
8. Traffic Processing 
• 
When the PSN is based on Layer 2 forwarding, the user can specify the VLAN priority (per IEEE 
802.1p) for the Ethernet frames carrying pseudowire packets. The priority is selectable for traffic 
forwarded through the Megaplex-1 Ethernet ports; when using bridge ports as pseudowire exit 
ports, it is necessary to configure VLAN tagging in order to request a specific priority. 
• 
When the PSN uses IP routing, the user can specify the Type of Service (ToS) per RFC791; if the 
PSN supports RFC2474, ToS is interpreted as a DiffServ codepoint per RFC2474. 
Pseudowire QoS/CoS  
To enable optimal handling of pseudowire traffic within the PSN, the following parameters can be 
configured: 
• 
For Ethernet transport networks: outgoing pseudowire packets are assigned to a dedicated 
VLAN ID according to 802.1Q and marked for priority using 802.1p bits. 
• 
For IP transport networks: outgoing pseudowire packets are marked for priority using ToS bits. 
This allows PW packets to be given the highest priority in IP networks. 
The proper balance between the PSN throughput and delay is achieved via configurable packet size. A 
jitter buffer with selectable size compensates for packet delay variation (jitter) of up to 256 msec in the 
network. 
ToS  
The ToS specifies the Layer 3 priority assigned to the traffic generated by this pseudowire. 
For IP networks, this priority is indicated by the IP type-of-service parameter for this pseudowire. The 
specified value is inserted in the IP TOS field of the pseudowire IP packets. 
When supported by an IP network, the type-of-service parameter is interpreted, in accordance with 
RFC791 or RFC2474, as a set of qualitative parameters for the precedence, delay, throughput and 
delivery reliability to be provided to the IP traffic generated by this pseudowire. 
These qualitative parameters may be used by each network that transfers the pseudowire IP traffic to 
select specific values for the actual service parameters of the network, to achieve the desired quality of 
service. 
You can also specify a Layer 2 priority by means of the vlan priority command. 
Megaplex-1 
8. Traffic Processing 
Jitter Buffer  
The packets of each pseudowire are transmitted by Megaplex-1 at essentially fixed intervals toward the 
PSN. The packets are transported by the PSN and arrive to the far end after some delay. Ideally, the PSN 
transport delay should be constant, meaning the packets arrive at regular intervals (equivalent to the 
intervals at which they were transmitted). However, in reality, packets arrive at irregular intervals, 
because of variations in the network transmission delay. The term Packet Delay Variation (PDV) is used 
to designate the maximum expected deviation from the nominal arrival time of the packets at the far 
end device.  
Note 
The deviations from the nominal transmission delay experienced by packets 
are referred to as jitter, and the PDV is equal to the expected peak value of 
the jitter. However, nothing prevents the actual delay from exceeding the 
selected PDV value.  
To compensate for deviations from the expected packet arrival time, Megaplex-1 uses jitter buffers that 
temporarily store the packets arriving from the PSN (that is, from the far end equipment) before being 
transmitted to the local TDM equipment, to ensure that the TDM traffic is sent to the TDM side at a 
constant rate. 
For each pseudowire, the jitter buffer must be configured to compensate for the jitter level expected to 
be introduced by the PSN; that is, the jitter buffer size determines the Packet Delay Variation Tolerance 
(PDVT).  
Two conflicting requirements apply: 
• 
As packets arriving from the PSN are first stored in the jitter buffer before being transmitted to 
the TDM side, TDM traffic suffers an additional delay. The added delay time is equal to the jitter 
buffer size configured by the user. 
• 
The jitter buffer is filled by the incoming packets and emptied to fill the TDM stream. If the PSN 
jitter exceeds the configured jitter buffer size, underflow/overflow conditions occur, resulting in 
errors at the TDM side: 
 
A jitter buffer overrun occurs when it receives a burst of packets that exceeds the 
configured jitter buffer size + packetization delay.  
 
A jitter buffer underrun occurs when no packets are received for more than the configured 
jitter buffer size. 
When the first packet is received, or immediately after an underrun, the buffer is automatically filled 
with a conditioning pattern up to the PDVT level in order to compensate for the underrun. Then, 
Megaplex-1 starts processing the packets and emptying the jitter buffer toward the TDM side.  
To minimize the possibility of buffer overflow/underflow events, two conditions must be fulfilled: 
Megaplex-1 
8. Traffic Processing 
• 
The buffer must have sufficient capacity. For this purpose, the buffer size can be selected by the 
user in accordance with the expected jitter characteristics, separately for each pseudowire, in 
the range of 250-256,000 usec. 
• 
TDM clocks at both ends should be synchronized so that the read-out rate shall be equal to the 
average rate at which frames are received from the network. One way to achieve this is by 
adaptive clock recovery, which continuously adapts the recovered clock to the packet rate. 
Other ways may be by distributing the same clock to Megaplex-1 by External clock input.  
Jitter Buffer Centering  
Megaplex-1 includes a Jitter Buffer (JB) Centering mechanism designed to maintain a stable end-to-end 
delay for a pseudowire (PW), especially in networks with high jitter. Normally, when a PW is established 
or after underrun/overrun events, the jitter buffer is centered to protect traffic from network delay 
variations and bursts. However, in highly jittered networks, the initial buffer state after centering may 
still be inaccurate, causing inconsistent end-to-end delay following PW recovery events. 
To address this, Megaplex-1 can verify the jitter buffer position after PW setup or underrun/overrun 
recovery. Once TDM playout starts, the system samples the jitter buffer fill level and calculates the 
average fill level. If the average deviates from the expected center by more than a configurable 
threshold, the jitter buffer is flushed and re-centered automatically. This functionality is configured per 
PW and can be enabled or disabled using the jitter-buffer-centering deviation <%> command. By 
default, the feature is disabled. 
Adaptive Timing  
Megaplex-1 provides independent adaptive clock recovery mechanism for each pseudowire. Each of the 
PWs can be configured as a clock source. Based on the PW status and priority, clock selection module 
(CSM) automatically selects one of the configured clock sources to lock the system timing.  
Each pseudowire has its own adaptive timing recovery mechanism, in accordance with the options listed 
in RFC4197.  
The adaptive clock recovery mechanism estimates the average rate of the payload data received in the 
frames arriving from the packet-switched network. Assuming that the packet-switched network does 
not lose data, the average rate at which payload arrives will be equal to the rate at which payload is 
transmitted by the source.  
Note 
Generally, packets that did not arrive in the correct order can be reordered.  
The method used to recover the payload clock of a pseudowire is based on monitoring the fill level of 
the selected pseudowire jitter buffer: the clock recovery mechanism monitors the buffer fill level, and 
generates a read-out clock signal with adjustable frequency. The frequency of this clock signal is 
Megaplex-1 
8. Traffic Processing 
adjusted so as to read frames out of the buffer at a rate that keeps the jitter buffer as near as possible to 
the half-full mark. This condition can be maintained only when the rate at which frames are loaded into 
the buffer is equal to the rate at which frames are removed. Therefore, the adaptive clock recovery 
mechanism actually recovers the original payload transmit clock.  
You can select a total of 16 pseudowire clocks per Megaplex-1. 
Factory Defaults 
No PWs are included in the Megaplex-1 factory defaults. You must define the necessary PWs in 
accordance with your application requirements. Other parameter defaults are listed in the table below. 
Parameter  
Default Value 
psn  
udp-over-ip 
type  
ces-psn-data 
tos 
0 
jitter-buffer, sec 
2500  
jitter-buffer centering 
Disabled  
tdm-payload  
1  
vlan priority 
0 
label 
Same as the PW index number  
udp-mux-method  
src-port 
name 
PW + PW number 
peer 
peer-1 
oos parameters: 
signaling   
force-idle  
data 
00 
voice 
00 
Configuring Pseudowires  
The configuration of a PW comprises the following steps: 
Megaplex-1 
8. Traffic Processing 
1. Verify that all the necessary entities (DS1 ports and SVI/RI) have been configured as needed and 
are administratively enabled. 
2. Verify that the peer to be used for the PW has been defined. 
3. Verify that Layer-2 and Layer-3 entities have been defined (e.g. flows, router, etc.).  
4. If you are configuring PW encapsulation for PSN – UDP over IP (see step 6), configure the router 
interface for PWE, making sure to set the router interface to allow-ping (mandatory). You are 
not required to configure the router interface for PSN MEF 8 (Ethernet).   
5. Select the PW connection type: CESoPSN for framed TDM ports (DS1/E1/T1/serial/ds1-
opt/voice), SAToP for unframed E1/T1/DS1 ports. 
6. Select the PSN type: UDP over IP or Ethernet. 
7. Configure the PW parameters in accordance with the selected connection type and PSN type. 
8. Set the PW to “no shutdown”. 
New pseudowires are added by defining their number (1–32), type (connection mode, always ces-psn-
data, e1satop, t1satop) and a PSN type.  
The following figures schematically illustrate configuring PWs with UDP over IP and MEF-8 encapsulation 
modes. 
 
 
Configuring PWs with UDP over IP Encapsulation Mode 
Megaplex-1 
8. Traffic Processing 
 
Configuring PWs with MEF-8 Encapsulation Mode 
 To define and configure a pseudowire: 
1. If you intend to use UDP/IP PSN type, verify that the router interface with valid IP address has 
been configured (see Configuring the Router).  
2. At the config>pwe# prompt, enter the syntax illustrated in the table below. 
The config>pwe>pw(<pw-number>)# prompt appears. 
Note 
A DS1 port becomes active only if at least one enabled pseudowire with a valid 
cross-connection is assigned to the port 
 
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Assigning the pseudowire 
number and specifying the PSN 
type (selecting the type of PSN 
header)  
 
pw <pw-number> type {ces-
psn-data | e1satop | 
t1satop} [psn { ethernet | 
udp-over-ip}]  
        
  
• PW number: 1..12  
PW type: 
• ces-psn-data – PW bundle using 
the CESoPSN protocol, for 
carrying framed data streams 
• e1satop – PW bundle using the 
SAToP protocol, for carrying an 
unframed E1 data stream 
• t1satop – PW bundle using the 
SAToP protocol, for carrying an 
unframed T1 data stream 
psn (must be configured for the first 
time): 
• udp-over-ip – UDP over IP 
network encapsulation 
• ethernet – MEF-8 Ethernet 
network encapsulation 
Using no before pw <number> 
deletes the pseudowire 
3. At the config>pwe>pw(<pw-number>)# prompt, enter the parameters specified in the table 
below. 
Task 
Command 
Comments 
Assigning a name to the 
pseudowire 
name <up to 32 
characters> 
 
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Specifying the PW label 
used in the inbound and 
outbound directions 
label  [in <number>] 
[out < number>] 
    
Out PW label: 
• For udp-over-ip: Specifies the UDP source 
port number used by the pseudowire  
• For ethernet: Specifies the Emulated Circuit 
ID (ECID) for Tx PW packets 
In PW label: 
• For udp-over-ip: Specifies the UDP source 
port number used by the pseudowire for the 
Tx PW packets (destination port for Rx PW 
packets) 
• For ethernet: Specifies the expected 
Emulated Circuit ID (ECID) Rx PW packets 
Each PW must have a unique in (source) label. 
For udp-over-ip the allowed range is 1 to 65535, 
for ethernet - 2^20-1 (1048575) 
Controlling whether the 
next-hop MAC is 
periodically monitored 
according to the ARP 
table  
arp-table-refresh  
no arp-table-
refresh  
For udp-over-ip only  
When using arp-table-refresh, PW transmission 
will be stopped once the next hop ARP entry is 
flushed from the ARP table, otherwise the PW 
will keep transmitting.   
Transmitting an 
out-of-service signal 
(OOS) on PW failure and 
selecting the code 
transmitted by the port 
during out-of-service 
periods on the timeslots 
defined as data and voice 
timeslots.  
  
tdm-oos [voice <00 
to FF (hexa)>] [data 
<00 to FF (hexa)>]  
[signaling 
{force-idle|force-
busy} ]  
  
tdm-oos voice and data are hexadecimal 
numbers in the range of 00 to FF (two digits). 
The selected code for data is also sent during 
out-of-service periods instead of the external 
data stream when the unframed mode is used 
signaling – Determines the state of the signaling 
bits sent to the DS1 port connected to the 
selected pseudowire during out-of-service 
periods (relevant only when the attached DS1 
port is configured with signaling enabled): 
• force-idle – The signaling bits are forced to 
the idle state (05 hexa) during out-of-service 
periods.  
• force-busy – The signaling bits are forced to 
the busy state (0F hexa) during out-of-service 
periods. 
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Defining the jitter buffer 
size in msec 
jitter-buffer <value 
in µsec>  
 
  
Use the shortest feasible buffer, to minimize 
connection latency. Possible values are 250 µsec 
to 256000 µsec, in 1-µsec steps (the value 
entered by the user is rounded upward to the 
closest n*125 µsec value). 
Enabling Jitter Buffer (JB) 
Centering mechanism 
and configuring the  
deviation threshold 
jitter-buffer-
centering deviation 
<value in %>  
 
Default: no jitter-buffer-centering 
Defining a remote peer 
terminating this PW 
peer <1–12> 
The peer type must be according to the PSN type: 
• IP address for UDP/IP 
• MAC or IP address for Ethernet  
Using no peer removes the remote peer  
 
CESoPSN: specifying the 
number of frames to be 
inserted in each packet. 
SATOP: indicating the 
number of bytes in each 
packet. 
CESoPSN: tdm-
payload <1–61>  
SAToP: tdm-
payload <32-1900>  
 
 
A larger value decreases the bandwidth 
utilization efficiency, but also increases the 
connection intrinsic latency. 
The packet size in CESopSN is defined as (TDM 
number of frames * number of timeslots). The 
packet size is limited to 1-1900 for data and 4-
1900 for voice. 
Specifying the value for 
the TOS byte used on 
outbound traffic 
tos <tos  number> 
   
This parameter is relevant only when psn is 
udp-over-ip. 
Range: from 0 to 255.  
In accordance with RFC 2474, it is recommended 
to use only values which are multiples of 4.  
Enabling and configuring 
VLAN tagging and priority 
on every transmitted 
packet (relevant only for 
MEF PW) 
vlan [priority 
<0..7>] 
 
 
       
 
VLAN priority: The allowed range in accordance 
with IEEE 802.1p is 7 (highest priority) to 0 
(lowest priority). 
Note: If the traffic on the specific PW must be 
assigned priority, the priority parameter must be 
configured in this context (not as part of flow 
configuration) and then mapped via queue-map-
profile configuration. 
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Controlling whether the 
PW carries a failure 
indication if the local 
domain clock fails 
domain-failure-
indication 
no domain-failure-
indication 
 
Defining the conditions 
when the PW is 
considered failed for the 
CSM 
source-clock-fail 
[pw-down] 
[remote-domain-
down] 
pw-down – PW failure (always enabled) 
remote-domain-down – Once the PW receives an 
indication of failure from the far-end side, the PW 
clock moves to the fail state 
Assigning egress port for 
L2 forwarding 
egress-port svi 
<svi_number> 
This parameter is relevant only when psn is 
Ethernet and peer is mac 
Specifying the UDP port 
multiplexing method 
 
  
udp-mux-method  
{dst-port | src-port}  
 
 
This parameter is relevant only when psn is 
udp-over-ip. 
dst-port: 
UDP destination port = 0xC000 + <out-PW-label>  
UDP source port is 0xC000 + <in-PW-label> 
src-port: 
UDP destination port = 0xC000 + <out-PW-label>  
UDP source port is 0x85E 
Administratively enabling 
the PW  
no shutdown 
Type shutdown to administratively disable the 
PW. 
 
Displaying PW status 
show status 
 
 To delete a PW: 
1. At the config>pwe>pw(<pw-number>)# prompt, enter: 
shutdown 
The PW is administratively disabled. 
2. At the config>pwe# prompt, enter:  
no pw <pw-number>. 
The PW is removed. 
Viewing the Pseudowire Status and Summary  
You can display information about the PW configuration. 
Megaplex-1 
8. Traffic Processing 
 To display PW configuration summary:  
• 
At the config>pwe# prompt, enter the show summary command. 
For example:  
 
MP-1>config>pwe# show summary 
 
PW                  : 1                             Name     : PW 
1 
 
PSN Type            : Ethernet                      PW Type  : 
CES PSN Data 
 
Connectivity Status : Local Fail 
 
SVI                : 2                  In Label           : 1 
Peer               : 1 
IP Addr            : 0.0.0.0 
Next Hop Mac       : 00-20-D2-54-08-ED 
Out Label          : 1 
 
Time Slots : 1..2 
 
Jitter Buffer         : 2500            Payload Size          : 3 
 
 
PW                  : 2                             Name     : PW 
2 
 
PSN Type            : Ethernet                      PW Type  : 
CES PSN Data 
 
Connectivity Status : Local Fail 
 
SVI                : 2                  In Label           : 2 
Peer               : 1 
IP Addr            : 0.0.0.0 
Next Hop Mac       : 00-20-D2-54-08-ED 
Out Label          : 2 
 
Time Slots : 1..2 
 
Jitter Buffer         : 2500            Payload Size          : 3 
Megaplex-1 
8. Traffic Processing 
 
 
PW                  : 3                             Name     : PW 
3 
 
PSN Type            : Ethernet                      PW Type  : 
CES PSN Data 
 
Connectivity Status : Local Fail 
 
SVI                : 2                  In Label           : 3 
Peer               : 1 
IP Addr            : 0.0.0.0 
Next Hop Mac       : 00-20-D2-54-08-ED 
Out Label          : 3 
 
Time Slots : 1..3 
 
Jitter Buffer         : 2500            Payload Size          : 3 
 
 
PW                  : 4                             Name     : PW 
4 
 
PSN Type            : Ethernet                      PW Type  : 
CES PSN Data 
 
Connectivity Status : Local Fail 
 
SVI                : 2                  In Label           : 4 
Peer               : 1 
IP Addr            : 0.0.0.0 
Next Hop Mac       : 00-20-D2-54-08-ED 
Out Label          : 4 
 
Time Slots : 1..4 
 
Jitter Buffer         : 2500            Payload Size          : 3 
 
 
PW                  : 5                             Name     : PW 
5 
 
Megaplex-1 
8. Traffic Processing 
PSN Type            : Ethernet                      PW Type  : 
CES PSN Data 
 
Connectivity Status : Local Fail 
 
SVI                : 2                  In Label           : 5 
Peer               : 1 
IP Addr            : 0.0.0.0 
Next Hop Mac       : 00-20-D2-54-08-ED 
Out Label          : 5 
 
Time Slots : 1..5 
 
Jitter Buffer         : 2500            Payload Size          : 3 
 
 
PW                  : 6                             Name     : PW 
6 
 
PSN Type            : Ethernet                      PW Type  : 
CES PSN Data 
 
Connectivity Status : Local Fail 
 
SVI                : 2                  In Label           : 6 
Peer               : 1 
IP Addr            : 0.0.0.0 
Next Hop Mac       : 00-20-D2-54-08-ED 
Out Label          : 6 
 
Time Slots : 1..6 
 
Jitter Buffer         : 2500            Payload Size          : 3 
 
 
PW                  : 7                             Name     : PW 
7 
 
PSN Type            : Ethernet                      PW Type  : 
CES PSN Data 
 
Connectivity Status : Down 
 
SVI                : 3                  In Label           : 7 
Megaplex-1 
8. Traffic Processing 
Peer               : 1 
IP Addr            : 0.0.0.0 
Next Hop Mac       : 00-00-00-00-00-00 
Out Label          : 7 
 
Jitter Buffer         : 2500            Payload Size          : 4 
 
MP-1>config>pwe# 
 To display a single PW status: 
1. At the config#pwe prompt, enter the desired pseudowire (pw <number>). 
The config>pwe>pw(<number>)$ prompt appears. 
2. Enter show status. 
The status screen appears. For information on the connectivity status values, refer to the table 
below. 
config>pwe>pw(1)# show status 
PW   : 1 
 
Name : PW 1 
 
 
PW Type                                        : CES PSN Data 
PSN Type                                       : Ethernet 
Connectivity Status                            : Local Fail 
Out Label                                      : 1 
In Label                                       : 1 
Next Hop MAC Address                           : 00-20-D2-54-08-
ED 
Peer                                           : 1 
SVI                                            : 2 
The table below explains the connectivity status values of the selected pseudowire. 
Parameter Displayed 
Description 
Disable 
The pseudowire is disabled 
Up 
  
The pseudowire carries traffic, and both the remote and the local pseudowire 
endpoints receive Ethernet frames. However, there may be problems such as 
sequence errors, underflows, overflows, etc., which may be displayed using 
the Statistics function. 
Megaplex-1 
8. Traffic Processing 
Parameter Displayed 
Description 
Unavailable 
 
The pseudowire reports loss of connectivity. This is often caused by network 
problems, or configuration errors.  
Down 
The pseudowire is waiting for timeslot assignment 
Local Fail 
 
A failure has been detected at the local pseudowire endpoint. 
Remote Fail 
A failure is reported by the remote pseudowire endpoint. 
Displaying PW Statistics  
PW ports feature the collection of statistical diagnostics, thereby allowing the carrier to monitor the 
transmission performance of the links. 
The pseudowire transmission statistics enable analyzing pseudowire traffic volume, evaluate the end-to-
end transmission quality (as indicated by sequence errors), and jitter buffer performance. By resetting 
the status data at the desired instant, it is possible to ensure that only current, valid data is taken into 
consideration. 
 To display the PW statistics:  
• 
At the prompt config>slot>pwe>pw(<PW number>)#, enter show statistics followed by the 
parameters listed below.  
Task 
Command 
Comments 
Displaying statistics 
show statistics {total | all | 
all-intervals | current}  
  
• current - Displays the current 
statistics 
• all-intervals – Displays statistics 
for all valid intervals (without 
current statistics) 
• all –all statistics: first current 
statistics, then statistics for all 
valid intervals, and finally total 
statistics 
• total – Displays total statistics of 
last 96 intervals 
Displaying statistics for a 
specific interval 
show statistics interval 
<interval-num 1..96> 
 
PW statistics are displayed.  The counters are described in the tables below. 
Megaplex-1 
8. Traffic Processing 
For example:  
Current Statistics:  
MP-1>config>pwe>pw(1)# show statistics current 
PW : 1 
 
Current 
--------------------------------------------------------------- 
Time Elapsed (Sec) : 263 
Valid Intervals    : 96 
 
Rx Packets                : 0 
Tx Packets                : 701331 
Missing Packets           : 0 
Mis-order Dropped Packets : 0 
Reordered Packets         : 0 
Malformed Packets         : 0 
Jitter Buffer Underrun    : 263 
Jitter Buffer Overrun     : 0 
Sequence Error Seconds    : 0 
Jitter Buffer Centering Events     : 0 
Statistics for interval 96: 
MP-1>config>pwe>pw(1)# show statistics interval 96 
PW : 1 
 
Interval Number : 96 
Valid           : True 
Time Elapsed    : 900 
 
Rx Packets                : 0 
Tx Packets                : 2400010 
Missing Packets           : 0 
Mis-order Dropped Packets : 0 
Reordered Packets         : 0 
Malformed Packets         : 0 
Jitter Buffer Underrun    : 900 
Jitter Buffer Overrun     : 0 
Sequence Error Seconds    : 0  
Jitter Buffer Centering Events     : 0 
 
Total Statistics:  
Megaplex-1 
8. Traffic Processing 
MP-1>config>pwe>pw(1)# show statistics total 
Total 
--------------------------------------------------------------- 
Rx Frames                        : 0 
Tx Frames                        : 206368463 
Jitter Buffer Underflows Seconds : 77390 
Jitter Buffer Overflows Seconds  : 0 
Sequence Error Seconds           : 0 
PWE Statistics Parameters – Current 15-Minute Interval  
Parameter 
Description 
Time Elapsed 
(Sec) 
The elapsed time (in seconds) since the beginning of the current interval, in 
seconds. The range is 1 to 900 seconds 
Valid Intervals 
The number of elapsed finished 15-min intervals for which statistics data can be 
displayed, in addition to the current (not finished) interval (up to 96). 
Missing Packets  
Number of missing packets as detected via Control Word sequence number gaps. 
This count does not include misordered dropped packets.  
Mis-order 
Dropped Packets  
Number of packets detected via Control Word sequence number to be out of 
sequence, and could not be re-ordered, or could not fit in the jitter buffer. This 
count includes duplicated packets. 
Reordered 
Packets  
Number of packets detected via Control Word sequence number to be out of 
sequence, but successfully reordered. 
Sequence Errors 
Seconds 
 
Displays the number of seconds during which sequence errors have been 
detected. 
In accordance with the applicable standards, the transmitted packets carry a 
sequence number that is automatically assigned, such that consecutive packets 
are automatically consecutive sequence numbers. At the receive side, these 
numbers are checked by the receive mechanism, which expects each new 
incoming packet to carry the next number in the sequence, relative to the 
previous one (i.e., packet 5 must be received after packet 4). Any deviation from 
the this rule indicates a problem with packet flow integrity (and hence with the 
pseudowire payload (data or voice) integrity), and in this case the sequence errors 
count is incremented by 1. 
There are two main reasons for a sequence error event: 
• One or more packets have been lost somewhere in the network. 
• Packets have been reordered within the network. Packet reordering may occur 
due to queuing mechanisms, rerouting by the network, or when the router 
updates include very large routing tables 
Megaplex-1 
8. Traffic Processing 
Parameter 
Description 
Malformed 
Packets 
Number of malformed packets as detected via Control Word sequence number 
gaps. 
Rx Packets 
Number of packets received from the PSN during the current interval 
Tx Packets 
Number of packets transmitted toward the PSN during the current interval 
Jitter Buffer 
Underrun  
Displays the number of seconds during which at least one jitter buffer underrun 
event has been detected.  
Megaplex-1 is equipped with a Packet Delay Variation Tolerance buffer, also 
called a “jitter buffer”, which is used to automatically compensate for packet 
network delay variation (jitter). Each pseudowire has its own jitter buffer. 
Although packets leave the transmitting PW-module at a constant rate, they will 
usually reach the far end at a rate which is not constant, because in practice the 
network transmission delay varies (due to factors such as congestion, rerouting, 
queuing mechanisms, transport  over wireless or half-duplex media, etc.).  
TDM equipment at both ends of a pseudowire require a constant flow of data, 
and cannot tolerate delay variation. Therefore, the receive side jitter buffer is 
required to provide the TDM equipment with a synchronous and constant flow. 
For this purpose, when a pseudowire is set up (and at any time after 
communication is restored), the jitter buffer is loaded with packets up to its 
middle point: only after this point it starts outputting TDM data towards the 
connected TDM equipment. The stored packets assure that the TDM equipment 
will continue receiving data even if the network delay momentarily increases. 
Obviously, if packets are delayed too long, the buffer is gradually emptied out 
until it underflows (this situation is called buffer starvation, and it affects the end-
to-end voice/data integrity).  
Each underflow event increases the jitter buffer underflow counter by 1.   
Jitter Buffer 
Overrun 
Displays the number of seconds during which at least one jitter buffer overrun 
event has been detected.   
As explained above, during steady state, the jitter buffer is filled up to its middle 
point, which means that it has space to hold additional packets. An overflow will 
occur when the network delay suddently decreases, for example, when a large 
burst of packets reaches the PW. If the burst includes more packets than the jitter 
buffer can store at that instant, the buffer will be filled up to its top. In this case, 
an unknown number of excess packets are dropped. To correct the situation, 
Megaplex-1 initiates a forced underflow by flushing (emptying) the buffer. 
Therefore, an overflow always results in an immediate underflow. After the buffer 
is flushed, the process of filling up the buffer is started again 
Megaplex-1 
8. Traffic Processing 
Parameter 
Description 
Jitter Buffer 
Centering Events 
Displays the number of times the jitter buffer centering mechanism has been 
triggered. A centering event may occur during the initial PW setup or following a 
jitter buffer underrun or overrun condition. The purpose of the centering 
mechanism is to ensure that the jitter buffer operates around its optimal middle 
position, protecting the PW from excessive delay variations and packet bursts in 
highly jittered networks. 
After a centering event is triggered and TDM playout begins, Megaplex-1 
periodically samples the jitter buffer fill level and calculates an average buffer 
position. If the measured average deviates from the expected center by more 
than the configured threshold, the jitter buffer is flushed and re-centered 
automatically. This mechanism helps maintain a stable end-to-end delay and 
prevents incorrect jitter buffer positioning after recovery from underrun or 
overrun events. 
PWE Statistics Parameters – All Intervals Statistics  
Parameter 
Description 
Valid  
True indicates that the counting was done for all the interval period (900 
seconds). False indicates that the interval runs less or more than 900 seconds. 
This can be caused by changes in the device clock, cleared statistics or shutdown 
of the pw. 
Sequence Errors 
Seconds 
Displays the number of seconds during which sequence errors have been 
detected. 
In accordance with the applicable standards, the transmitted packets carry a 
sequence number that is automatically assigned, such that consecutive packets 
are automatically consecutive sequence numbers. At the receive side, these 
numbers are checked by the receive mechanism, which expects each new 
incoming packet to carry the next number in the sequence, relative to the 
previous one (i.e., packet 5 must be received after packet 4). Any deviation from 
the this rule indicates a problem with packet flow integrity (and hence with the 
pseudowire payload (data or voice) integrity), and in this case the sequence errors 
count is incremented by 1. 
There are two main reasons for a sequence error event: 
• One or more packets have been lost somewhere in the network. 
• Packets have been reordered within the network. Packet reordering may occur 
due to queuing mechanisms, rerouting by the network, or when the router 
updates include very large routing tables 
Rx Packets 
Number of packets received from the PSN during the current interval 
Tx Packets 
Number of packets transmitted toward the PSN during the current interval 
Megaplex-1 
8. Traffic Processing 
Parameter 
Description 
Mis-order 
Dropped Packets  
Number of packets detected via Control Word sequence number to be out of 
sequence, and could not be re-ordered, or could not fit in the jitter buffer. This 
count includes duplicated packets. 
Reordered 
Packets  
Number of packets detected via Control Word sequence number to be out of 
sequence, but successfully reordered. 
Malformed 
Packets 
Number of malformed packets as detected via Control Word sequence number 
gaps. 
Jitter Buffer 
Underrun  
Displays the number of seconds during which at least one jitter buffer underrun 
event has been detected.  
Megaplex-1 is equipped with a Packet Delay Variation Tolerance buffer, also 
called a “jitter buffer”, which is used to automatically compensate for packet 
network delay variation (jitter). Each pseudowire has its own jitter buffer. 
Although packets leave the transmitting PW-module at a constant rate, they will 
usually reach the far end at a rate which is not constant, because in practice the 
network transmission delay varies (due to factors such as congestion, rerouting, 
queuing mechanisms, transport  over wireless or half-duplex media, etc.).  
TDM equipment at both ends of a pseudowire require a constant flow of data, 
and cannot tolerate delay variation. Therefore, the receive side jitter buffer is 
required to provide the TDM equipment with a synchronous and constant flow. 
For this purpose, when a pseudowire is set up (and at any time after 
communication is restored), the jitter buffer is loaded with packets up to its 
middle point: only after this point it starts outputting TDM data towards the 
connected TDM equipment. The stored packets assure that the TDM equipment 
will continue receiving data even if the network delay momentarily increases. 
Obviously, if packets are delayed too long, the buffer is gradually emptied out 
until it underflows (this situation is called buffer starvation, and it affects the end-
to-end voice/data integrity).  
Each underflow event increases the jitter buffer underflow counter by 1.   
Jitter Buffer 
Overrun 
Displays the number of seconds during which at least one jitter buffer overrun 
event has been detected.   
As explained above, during steady state, the jitter buffer is filled up to its middle 
point, which means that it has space to hold additional packets. An overflow will 
occur when the network delay suddently decreases, for example, when a large 
burst of packets reaches the PW. If the burst includes more packets than the jitter 
buffer can store at that instant, the buffer will be filled up to its top. In this case, 
an unknown number of excess packets are dropped. To correct the situation, 
Megaplex-1 initiates a forced underflow by flushing (emptying) the buffer. 
Therefore, an overflow always results in an immediate underflow. After the buffer 
is flushed, the process of filling up the buffer is started again 
Megaplex-1 
8. Traffic Processing 
Parameter 
Description 
Jitter Buffer 
Centering Events 
Displays the number of times the jitter buffer centering mechanism has been 
triggered. A centering event may occur during the initial PW setup or following a 
jitter buffer underrun or overrun condition. The purpose of the centering 
mechanism is to ensure that the jitter buffer operates around its optimal middle 
position, protecting the PW from excessive delay variations and packet bursts in 
highly jittered networks. 
After a centering event is triggered and TDM playout begins, Megaplex-1 
periodically samples the jitter buffer fill level and calculates an average buffer 
position. If the measured average deviates from the expected center by more 
than the configured threshold, the jitter buffer is flushed and re-centered 
automatically. This mechanism helps maintain a stable end-to-end delay and 
prevents incorrect jitter buffer positioning after recovery from underrun or 
overrun events. 
PWE Statistics Parameters – Total Statistics 
Parameter 
Description 
Tx Frames 
Total number of frames transmitted toward the PSN 
Rx Frames 
Total number of frames received from the PSN 
Sequence Errors Seconds 
 
Displays the number of seconds during which sequence errors have 
been detected. 
In accordance with the applicable standards, the transmitted packets 
carry a sequence number that is automatically assigned, such that 
consecutive packets are automatically consecutive sequence numbers. 
At the receive side, these numbers are checked by the receive 
mechanism, which expects each new incoming packet to carry the next 
number in the sequence, relative to the previous one (i.e., packet 5 
must be received after packet 4). Any deviation from the this rule 
indicates a problem with packet flow integrity (and hence with the 
pseudowire payload (data or voice) integrity), and in this case the 
sequence errors count is incremented by 1. 
There are two main reasons for a sequence error event: 
• One or more packets have been lost somewhere in the network. 
• Packets have been reordered within the network. Packet reordering 
may occur due to queuing mechanisms, rerouting by the network, or 
when the router updates include very large routing tables 
Jitter Buffer Underflows 
Seconds 
Total number of jitter buffer underflow events (not relevant for HDLC 
pseudowires).  
Megaplex-1 
8. Traffic Processing 
Parameter 
Description 
Jitter Buffer Overflows 
Seconds 
Total number of jitter buffer overflow events (not relevant for HDLC 
pseudowires).  
Clearing Statistics  
 To clear the PW statistics: 
• 
At the prompt config>pwe>pw<PW number>)#, enter clear-statistics. 
The statistics for the specified PW are cleared. 
Examples 
 To create and activate a CES PW with UDP encapsulation:  
    configure pw  
      pw 1 type ces-psn-data psn udp-over-ip 
        peer 1 
        label in 100 out 100 
        tdm-payload size 40  
        no shutdown 
    exit all 
 
Configuration Errors 
The following table lists messages generated by Megaplex-1 when a configuration error is detected. 
 
Message 
Description 
PW XC: Number of bytes in frame 
exceeds 1900  
The maximum payload value is 1900. 
PW XC: Maximum TDM Payload size 
value is 61 
The maximum tdm-payload value is 61. 

## 8.7 Router  *(p.347)*

Megaplex-1 
8. Traffic Processing 
Message 
Description 
PW XC: wrong payload size for signaling 
voice cross-connect 
In case of a PW cross-connect to a DS1 port which is cross-
connected to a voice port), the tdm-payload size must have 
only the following values:  
• E1 with g732s/g732s-crc framing: 1, 2, 4, 8, 16.  
• T1 with esf framing: 1, 2, 3, 4, 6, 8, 12, 24. 
• T1 with esf framing: 1, 2, 3, 4, 6, 8, 12. 
Router interface must be defined for 
PW UDP 
When using UDP method, you must define a router 
interface. 
Appropriate peer must be defined for 
PW. 
You must define a PW peer. 
Incorrect PW number, legal values: 
1..32 
Incorrect PW number, legal values are 1..32 
Peer's IP address must be different than 
Router Interface IP address 
The Peer and the Router interface IP addresses must lie in 
the same subnet but be different. 
Cannot delete PW that is a clock source 
This PW is used as a clock source and cannot be deleted 
Illegal action on PW that is a clock 
source 
This PW is used as a clock source and cannot be put to 
shutdown 
Cannot delete PW if it is a protection 
member 
This PW is used in a PW protection group and cannot be 
deleted 
Need to define egress port for PW 
For a PW of MEF type an egress port must be defined. 
8.7 Router  
Megaplex-1 features IPv4 static router, for management and PW purposes only.  
You can configure two types of router interfaces: 
• 
Management router interface – used to get full management access to the device 
• 
PW router interface – used for UDP/IP PW data forwarding. You cannot manage the device via 
this router interface, only ping is available for management. 
Inband management is available via any Ethernet port of the device. For this purpose, the router 
interface must be configured over bridge. 
Megaplex-1 
8. Traffic Processing 
Out-of-band management is available through the mng-ethernet port. For this purpose, the router 
interface can be configured over the mng-ethernet port or over bridge. 
The router uses service virtual interfaces (SVIs) for connecting to bridge ports. The connection is always 
made by directing flows from a SVI to bridge port.  
Standards 
RFC 1812 – Requirements for IP Version 4 Routers  
Benefits 
The router provides IPv4 managment capabilities. 
Configuring the Router 
Note 
• 
In order to enable management, you must configure a router interface 
with management access allow-all, assign it an IP address, and bind it to 
an SVI for which management flows have been defined.  
Any flow into/out of the device, which is related to management, must be via an SVI that is bound to a 
router interface. A router interface can be associated via binding to only one SVI. If a flow is used for 
management purposes, the router interface corresponding to the SVI should be configured with 
management access allow-all. 
 To configure the router: 
1. At the config# prompt, enter: 
router <number> 
The config>router(<number>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Deleting dynamic ARP 
entities 
clear-arp-table [<address>] 
Specify the IP address to clear only the 
entries corresponding to it. 
Clearing router statistics  
clear-statistics ipv4  
 
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Creating a router 
interface 
interface <interface-num> 
Interface-num – a unique number 
assigned to the router interface 
Possible values: 1–8 
Type no interface number to delete a 
router interface. 
See Configuring Router Interfaces for a 
list of tasks that can be configured on a 
router interface. 
Assigning a name to the 
router 
name <string> 
Alphanumeric string 
Displaying the address 
resolution protocol 
(ARP) table, which lists 
the original MAC 
addresses and the 
associated (resolved) IP 
addresses 
show arp-table [address <ip-address>] 
 
Displaying the interface 
table 
show summary-interface 
See Viewing Router Interface 
Information. 
 
Displaying the routing 
table 
show routing-table [ address 
<IP-address/IP-mask> ] 
[protocol { dynamic | static }] 
IP-address/IP-mask – View routing 
information for a specific IP address of a 
specified prefix length. 
protocol { dynamic | static } – View 
information on only dynamic or static 
routes. 
See Viewing Routing Information. 
Displaying router 
statistics 
show statistics  
 
Configuring Router Interfaces 
You can configure up to 8 router interfaces.  
 To configure router interfaces: 
1. At the config>router(1)# prompt, enter: 
interface <interface-num>  
Megaplex-1 
8. Traffic Processing 
The config>router(1)>interface(<interface-num>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning an IP address 
and prefix length to the 
router interface 
address 
<IP-address/prefix-length>  
no address 
<IP-address/prefix-length> 
• The IP address is IPv4 format (e.g. 
10.10.10.1)  
• Prefix length: 1–32.  
Enabling address aging 
function 
arp-timeout   
 
• Using no arp-timeout disables 
address aging function 
Binding router interface 
to an SVI logical port 
bind svi <port-number> 
• You can bind only one SVI to a 
router interface 
• The SVI must be created before 
entering bind command   
• Enter no bind to unbind the router 
interface. 
Clearing router interface 
statistics  
clear-statistics ipv4  
 
Enabling/disabling IP 
forwarding  
  
Configuring 
IPv6  
ip-forwaring  
 
Configuring interface 
management access 
management-access {allow-all | 
allow-ping}  
• You can set management access to 
allow-all for only one router 
interface 
• A PW-related router interface 
must be configured with 
management access allow-ping 
Assigning a name to the 
router interface 
name <interface-name> 
no name 
 
Displaying router 
interface statistic 
show statistics  
 
 
Displaying router 
interface status 
show status 
See Viewing Router Interface Status. 
Megaplex-1 
8. Traffic Processing 
Task 
Command 
Comments 
Administratively enabling 
or disabling the router 
interface 
no shutdown 
shutdown 
You can administratively enable the 
router interface only if one of the 
following is true: 
• The router interface is bound to an 
administratively enabled SVI, and 
the following are true: 
• An IP address was assigned via the 
address command. 
• Flows have been defined to and 
from the SVI, and are 
administratively enabled.  
Using shutdown disables the 
interface. 
Configuring the Management Source IP Address  
The management source IP address provides a single point of contact for management applications that 
interface with Megaplex-1.  
When a router interface responds to management packets, the responding packet source IP address is 
set to the router interface IP address. If the router interface sends a management packet that is not a 
response, the packet source IP address is set to the Megaplex-1 management source IP address. If the 
management source IP address is not configured or the corresponding router interface is down, the 
packet source IP address set to the router interface IP address. You can configure a single management 
source address for IPv4 to be used in all client management applications, including: SNMPv3 (for trap), 
Radius, Tacacs+. Syslog, SNTP, TFTP, and SFTP. 
 To configure the management source IP address: 
1. Navigate to configure management. 
The config> mngmnt# prompt is displayed.  
2. Type: 
management-address <ip-address> 
The management source IP address is set to the specified IP address. 
3. To delete the management address, type: 
no management-address  
Megaplex-1 
8. Traffic Processing 
Deleting a Router Interface 
The router cannot be deleted. 
 To delete a router interface:  
• 
At the config>router(<number>)# prompt, enter:ip-for no interface <interface-num> 
Displaying the ARP Table 
You can display the Address Resolution Protocol table with original MAC addresses and resolved IP 
addresses. 
 To display ARP table: 
• 
At the config>router(1)# prompt, enter show arp-table. 
The ARP table is displayed. 
config>router(1)# show arp-table 
IP Address          MAC Address         Status 
--------------------------------------------------------------- 
3.3.3.1             00-20-D2-2C-1A-E5   Dynamic 
Viewing Router Interface Information  
You can view information on each router interface by using the show summary-interface command:  
config>router(<number>)>show summary-interface 
 To display the interface summary: 
config>router(1)# show summary-interface 
 
Router Interface: 1 
  Name: RI001 
 
  Admin: Up      Oper: Up          Bound to:  svi 1 
 
  3.3.3.15/24                                 (manual)        (preferred
) 
The above fields are: 
Megaplex-1 
8. Traffic Processing 
Field 
Description 
Name 
Name of the router interface (alphanumeric string) 
Admin 
Administrative status: 
• up – ready to pass packets 
• down  
Oper 
Operational status: 
• up – ready to pass packets 
• down 
Bound to 
The port that the router interface is bound to 
origin 
Origin of the IP address: 
• manual – indicates that the address was manually configured to a 
specified address. 
status 
Status of the IP address: preferred. 
Viewing Routing Information  
You can view all routing information or only information on dynamic or static routes, for all IP addresses 
or for a specific IP address and prefix length by using the show routing-table command:  
config>router(<number>)>show routing-table [ address <IP-address/IP-mask> ]  
 To display the routing table: 
config>router(1)# show routing-table 
IP Address/Prefix Length Next 
Hop         Interface      Protocol   Metric 
----------------------------------------------------------------------
------- 
3.3.3.0/24               0.0.0.0          1              Local      0 
The above fields are: 
Field 
Description 
IP address/prefix 
IPv4 address and prefix length 
Next Hop 
Route entry next hop IP address 
Interface 
Router interface number 
Protocol 
Source protocol: Local & Static 
Megaplex-1 
8. Traffic Processing 
Field 
Description 
Metric 
Route entry metric  
   
Viewing Router Interface Status 
You can view the router interface status by using the show status command:  
config>router(<number>)>interface(<interface-num>)>show status 
 To display the router interface status: 
config>router(1)>interface(1)# show status 
 
Admin: Up          Oper: Up 
Ip Addresses: 
3.3.3.15/24                                 (manual)        (preferred
) 
The above fields are: 
Field 
Description 
Admin 
Administrative status: 
• up – ready to pass packets 
• down  
Oper 
Operational status: 
• up – ready to pass packets 
• down  
IP Addresses 
origin 
Origin of the IP address: manual 
status 
Status of the IP address: preferred  
IPv4 Default Router 
IP address of the IPv4 default router 
Viewing Router Interface Statistics 
The management router interface features statistics collection in accordance with RMON-RFC2819.  
Megaplex-1 
8. Traffic Processing 
 To display the router statistics:  
• 
At the prompt config>router(1)>interface (<number>)#, enter show statistics. 
Router interface statistics are displayed. The counters are described in the table below. 
config>router(1)>interface(1)# show statistics ipv4  
 
IPv4 Statistics:  
In 
-----------------------------------------------------------------
----------- 
Receives          : 120                 In Octets            : 
9360 
Multicast Packets : 0                   Multicast Octets      : 0 
Broadcast Packets : 0                   Header Errors         : 0 
No Routes         : 0                   Address Errors        : 0 
Unknown Protocols : 0                   Truncated Packets     : 0 
Forward Packets   : 0                   Reassembled Required  : 0 
Reassembled Ok    : 0                   Reassembled Fails     : 0 
Discards          : 0                   Delivers              : 0 
 
Out -------------------------------------------------------------
----------- 
Requests              : 0                   Forward 
Packets         : 0 
Discards              : 0                   Fragmentation 
Required  : 0 
Fragmentation Ok      : 0                   Fragmentation 
Fails     : 0 
Fragmentation Creates : 
0                   Transmits               : 120 
Octets                : 9360                Multicast 
Packets       : 0 
Multicast Octects     : 0                   Broadcast 
Packets       : 0 
 
IPv4 Default Router :  
Configuration Errors  
The following table lists the messages generated by the device when a configuration error is detected. 
Megaplex-1 
8. Traffic Processing 
Message 
Description 
Failed to approach DB           
Database problem. Try reconfiguring the router. 
Unable to get Mac Address from Mac 
2801 driver 
Failed to read MAC address. Try reconfiguring the router 
interface. 
SVI port is not defined yet      
To configure a router you have to define a corresponding SVI 
port. 
Only single router instance is 
supported 
SVI port can be bound only to a single router interface. 
Can't delete interface, flow with SVI 
router port is in active state 
To delete a router interface, first set the SVI connected to the 
router to “shutdown”. 
The maximum number of router 
interfaces for management has been 
reached 
Only a single router interface with management-access 
allow-all is supported in Megaplex-1 
Vlan cannot be configured on both 
flow and PW 
VLAN can be configured either for a flow or for a PW which is 
part of this flow, not for both.  
 
 
 
 
 
 
 
 