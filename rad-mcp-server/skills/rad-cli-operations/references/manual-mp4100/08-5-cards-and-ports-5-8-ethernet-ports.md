# 5 Cards and Ports – 5.8 Ethernet Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 288–299.*


## Applicability and Scaling  *(p.288)*


## Standards Compliance  *(p.288)*


## Functional Description  *(p.288)*

5. Cards and Ports 
5.8 Ethernet Ports  
Applicability and Scaling 
Megaplex-4 features the following user Ethernet ports: 
• 
Two fiber optic or copper Gigabit Ethernet network ports on each CL.2 module (except for 
CL.2/DS0)  
• 
Eight fiber optic or copper Gigabit Ethernet network ports on each M-ETH I/O module 
Standards Compliance 
IEEE 802.3, RFC 4836, RFC 3635. 
Functional Description 
GbE Port Interfaces  
The GbE ports on CL modules provide the physical connection to the packet switched network. The GbE 
ports on M-ETH modules provide Megaplex-4 with a multirate FE/GE interface, for optical or electrical 
media. This module can be used to provide LAN connectivity among Ethernet ports on the same module, 
as well as Ethernet services, thus eliminating the need for an external switch while providing a 
dependable Ethernet connectivity solution. 
These ports can be ordered with one of the following interfaces: 
• 
10/100/1000BASE-T copper ports. This type of ports support autonegotiation, with 
user-specified advertised data rate (10, 100 or 1000 Mbps) and operating mode (half- or 
full-duplex).  
The ports also support automatic polarity and crossover detection, and polarity correction, for 
connection through any type of cable to any type of Ethernet port (hub or station).  
Alternatively, auto-negotiation can be disabled and the rate and operating mode be directly 
specified. 
• 
SFP sockets, for installing 100/1000BASE-X SFP plug-in modules. Support for standard SFP 
optical transceivers for the GbE link interfaces enables selecting the optimal interface for each 
application. This type of ports does not support autonegotiation. 
5. Cards and Ports 
The interfaces support Synchronous Ethernet (Sync-E) master and slave modes according to ITU-T 
G.8261–G.8266 requirements. This allows each port to:  
• 
Extract the port clock. The derived clock will be used by the clock selection mechanism as a 
source clock  
• 
Set the port Tx clock according to the domain clock available from the CL module  
• 
Act as a source of ESMC messages for SSM-based clock modes. 
Fast Ethernet Port Interfaces  
The external Ethernet ports have 10/100 Mbps interfaces capable of auto-negotiation. The user can 
configure the advertised data rate (10 or 100 Mbps) and operating mode (half-duplex or full-duplex). 
Alternatively, auto-negotiation can be disabled, and the rate and operating mode be directly specified.  
The Ethernet ports can be ordered with one of the following types of interfaces: 
• 
Sockets for SFP Fast Ethernet transceivers. RAD offers several types of SFPs with optical 
interfaces, for meeting a wide range of operational requirements (SFPs with copper interfaces 
are also available). The SFPs are hot-swappable. 
• 
10/100BASE-TX interfaces terminated in RJ-45 connectors. In addition to auto-negotiation, 
MDI/MDIX polarity and cross-over detection and automatic cross-over correction are also 
supported. Therefore, these ports can always be connected through a “straight” (point-to-point) 
cable to any other type of 10/100BASE-T Ethernet port (hub or station). 
The ordering options depend on the specific I/O module. 
Hierarchy and Values  
The following table shows the number of Ethernet ports on each Megaplex-4 module, their CLI 
denomination, hierarchy and possible values. The hierarchical position of external Ethernet ports is 
slot:port for all the modules.  
  Ethernet Ports on I/O Modules  
Modules 
CLI Name 
Hierarchy 
Possible Values 
M-ETH  
ethernet 
slot: port 
1..8 
VS 
ethernet 
slot:port 
1 per submodule 
For more information, see the respective module sections in Chapters 13 and 14.  
5. Cards and Ports 
Flow Control  
A flow control is a mechanism that allows an Ethernet receiving end that is unable to process all the 
traffic sent to it, to hold the transmitted traffic until it can process packets again.  
The mechanism uses a PAUSE frame, which is a packet that instructs the far-end device to stop 
transmission of packets until the receiver can handle traffic again. The PAUSE frame has a timer value 
included (set by the originating receiver), which tells the far-end device how long to suspend 
transmission. If that timer expires or is cleared by getting a PAUSE frame with timer value set to 0, the 
far-end device can then send packets again. Flow control is an optional port-level parameter. 
Flow control is supported on both directly- and indirectly-attached ports: 
• 
Directly-attached ports support symmetrical flow control (both Rx and Tx) 
• 
Indirectly-attached ports support Rx flow control only, without issuing Tx PAUSE 
frames (asymmetric flow control). 
When autonegotiation is enabled, flow control mode is negotiated and a port advertises its user-
selected flow control capabilities to the peer. The actual flow control mode, as well as duplex mode and 
transmission speed are set after the negotiation is completed. 
When autonegotiation is disabled, the flow control mode is manually selected by the user.  
All Megaplex-4 Ethernet interfaces, except the OOB management port, support flow control. 
L2CP Handling  
Megaplex-4 handles Layer-2 control protocol traffic on a per-port basis. The L2CP traffic is processed 
using a two-stage mechanism comprising per-port L2CP profiles (set of rules for traffic handling). The 
L2CP profile affects untagged L2CP frames. In total, Megaplex-4 supports up to 16 L2CP profiles: 
• 
Up to 4 (including default) port-level profiles can be defined on directly-attached ports  
• 
Up to 32 different addresses/protocols can be selected per L2CP profile. 
If no default action is configured for an unspecified address or protocol, this traffic is tunneled. 
Note 
If an L2CP profile has been attached to a port, the profile cannot be deleted or 
modified. 
L2CP Profile Settings 
Megaplex-4 can tunnel, discard or peer (trap to host for protocol processing) L2CP packets. These 
actions are defined by L2CP profiles, which also provide different L2CP addresses. The following MAC 

## Factory Defaults  *(p.291)*

5. Cards and Ports 
addresses are supported by L2CP profiles: 01-80-C2-00-00-00, 01-80-C2-00-00-02 – 10 and 01-80-C2-00-
00-20 – 2F. 
Note 
PAUSE frames (01-80-C2-00-00-01) are not part of L2CP profiles. They are 
either peered or discarded according to flow control setting of a port. 
 
According to L2CP profiles, Megaplex-4 performs the following: 
• 
Discards L2CP traffic.  
• 
Tunnels L2CP traffic. Megaplex-4 forwards the traffic according to its configuration (flows etc).  
• 
Peers L2CP traffic. Megaplex-4 forwards the traffic to the CPU.  
Note 
Megaplex-4 supports peer action only for the following MAC 
addresses/protocols: 
• 
01-80-C2-00-00-00 (RSTP) 
• 
01-80-C2-00-00-02 (LACP, OAM (EFM) 
• 
01-80-C2-00-00-03 (802.1x). 
Default L2CP Profile 
By default, a “tunnel all” profile is attached to every port.  
Autonegotiation  
The speed and duplex mode of an Ethernet interface is set either manually by the operator or 
negotiated with the peer interface. The autonegotiation procedure enables automatic selection of the 
operating mode on a LAN. It enables equipment connecting to an operating LAN to automatically adopt 
the LAN operating mode (if it is capable of supporting that mode).  
Queue Group Profile 
Queue group profiles are the largest entities used in pre- and post-forwarding traffic management. They 
are attached to physical ports and consist of queue block and shaper profiles. See Queue Group Profiles 
section in Chapter 8 for details. 
Factory Defaults  
By default, the Ethernet non-management ports have the following configuration. 
5. Cards and Ports 
Fast Ethernet ports: 
config>port>eth(4/1)# info detail 
    name  "IO-4 ethernet 01" 
    shutdown 
    auto-negotiation 
    max-capability  100-full-duplex 
    no flow-control 
    no policer  
    egress-mtu  1790  
    queue-group profile "FeDefaultQueueGroup" 
    no l2cp  
    tag-ethernet-type  0x8100  
GbE ports of CL modules: 
config>port>eth(cl-b/1)# info detail 
    name  "CL-B ethernet 01" 
    shutdown 
    auto-negotiation* 
    max-capability  1000-full-duplex** 
    min-tagged-frame-length  68 
    no efm 
    no shaper 
    egress-mtu  1790 
    queue-group profile  "GbeDefaultQueueGroup" 
    l2cp profile  "L2cpDefaultProfile" 
    tag-ethernet-type  0x8100 
GbE ports of M-ETH modules:  
config>port>eth(7/4)# info detail 
    name  "IO-7 ethernet 04" 
    shutdown 
    auto-negotiation* 
    max-capability  1000-full-duplex** 
    no flow-control 
    no efm 
    no policer 
    egress-mtu  1790 
    queue-group profile  "MeDefaultQueueGroup" 
    no l2cp 
    tag-ethernet-type  0x8100 
 
    
*copper ports only 
**for fiber ports: 1000-x-full-duplex 
For description of default queue group profiles, see Queue Group Profiles section in Chapter 8.  

## Configuring User Ethernet Ports  *(p.293)*

5. Cards and Ports 
Configuring User Ethernet Ports  
 To configure the user Ethernet port parameters (any module with Ethernet ports): 
1. Navigate to configure port ethernet <slot>/<port> to select the Ethernet port to configure.  
The config>port>eth>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed in the table below.  
Task 
Command 
Comments 
Assigning short description 
to the port 
name <string> 
Using no name removes the name 
Administratively enabling 
port 
no shutdown 
Using shutdown disables the port 
Enabling autonegotiation 
 
auto-negotiation  
For copper ports only 
Using no auto-negotiation disables autonegotiation 
Enabling OAM (EFM) on 
the Ethernet port  
efm  
 
See Ethernet OAM (EFM) in Chapter 8. 
GbE ports of CL.2 and M-ETH modules only 
no efm disables OAM (EFM) on the Ethernet port 
Setting maximum frame 
size (in bytes) to transmit 
(frames above the 
specified size are 
discarded) 
egress-mtu <64–9600> 
 
The maximum frame size for GBE Ethernet ports of CL and 
M-ETH modules is 9600. 
•  
Setting maximum 
advertised capability 
(highest traffic handling 
capability to be advertised 
during the 
autonegotiation process)  
 
 
 
max-capability {10-half-
duplex | 10-full-duplex | 
100-half-duplex | 100-full-
duplex | 1000-full-duplex | 
1000-x-full-duplex} 
 
  
10-full-duplex –10baseT full duplex (copper ports only) 
10-half-duplex – 10baseT half duplex (copper ports only) 
100-full-duplex – 100baseT full duplex 
100-half-duplex – 100baseT half duplex (in the case of M-ETH 
– copper ports only) 
1000-full-duplex – 1000base T full duplex (copper GbE ports 
only) 
1000-x-full-duplex – 1000base T full duplex (fiber GbE ports 
only) 
This parameter applies only if autonegotiation is enabled. 
5. Cards and Ports 
Task 
Command 
Comments 
Setting data rate and 
duplex mode of the 
Ethernet port, when 
autonegotiation is 
disabled 
  
speed-duplex 10-half-duplex 
| 10-full-duplex | 100-half-
duplex | 100-full-duplex | 
1000-full-duplex | 1000-x-
full-duplex} 
 
10-full-duplex –10baseT full duplex (copper ports only) 
10-half-duplex – 10baseT half duplex (copper ports only) 
100-full-duplex – 100baseT full duplex 
100-half-duplex – 100baseT half duplex (in the case of M-ETH 
– copper ports only) 
1000-full-duplex – 1000base T full duplex (copper GbE ports 
only) 
1000-x-full-duplex – 1000base T full duplex (fiber GbE ports 
only)  
Setting flow control for 
the selected port (when 
operating in the full 
duplex mode), or back 
pressure (when operating 
in the half-duplex mode) 
flow-control  
Using no flow-control disables flow control 
Assigning queue group 
profile to Ethernet port 
 
queue-group profile <queue-
group-profile-name> 
 
Megaplex-4 with CL.2/A modules only  
The queue group profile is defined under Quality of Service 
(QoS) in Chapter 8. 
no queue-group removes queue group association 
The default queue group profile for Fast Ethernet ports is 
defined with 10 Mbps shaper.  Define a new queue group 
profile if you need more bandwidth.  
The queue group profile cannot be edited. Thus to use bridge 
connectivity you need to remove the existing queue group 
profile from this Ethernet port, configure a new queue group 
profile and assign it to this port.  
Associating a Layer-2 
control processing profile 
with the port 
l2cp <l2cp-profile-name> 
no l2cp  
Megaplex-4 with CL.2/A modules only  
GbE ports of CL.2 and M-ETH modules only 
Defines discarding or tunneling policy for Layer-2 protocols.  
no l2cp removes association with L2CP profile 
The associated L2CP profile specifies peer action for the 
following MAC addresses depending on the protocol in use:  
• 01-80-C2-00-00-00 (RSTP) 
• 01-80-C2-00-00-02 (LACP, OAM (EFM)) 
• 01-80-C2-00-00-03 (802.1x). 

## Example  *(p.295)*

5. Cards and Ports 
Task 
Command 
Comments 
Configuring collection of 
performance management 
statistics for this port, 
which are presented via 
the RADview Performance 
Management portal 
pm-collection interval 
<seconds> 
You can enable PM statistics collection for all Ethernet ports 
rather than enabling it for individual ports. In addition to 
enabling PM statistics collection for the ports, it must be 
enabled for the device. Refer to the Performance 
Management section in the Monitoring and Diagnostics 
chapter for details. 
Activating/deactivating a p
olicer profile   
 
policer-profile <name> 
The policer profile is defined under Quality of Service (QoS) in 
Chapter 8. 
Using no policer <name> deactivates this policer profile 
The total sum of bandwidths defined in policer profiles for all 
8 ports of the M-ETH module must not exceed 1 GbE.  
Setting the minimum 
VLAN-tagged frame length 
(in bytes) that will be 
accepted 
min-tagged-frame-length 
{64 | 68 | 72} 
 
CL GbE only  
 
Specifying the Ethertype 
expected in Ethernet 
packet 
tag-ethernet-type 
<0x0000-0xFFFF> 
Megaplex-4 with CL.2/A modules only 
Enabling transmitting of 
Sync-E clock availability 
and quality via ESMC 
messages  
tx-ssm 
CL GbE ports only 
no tx-ssm disables ESMC messages transmission 
Example  
 To configure the Ethernet interface: 
• 
Port – port 1 on CL-A module 
• 
Autonegotiation – enabled 
• 
L2CP profile – l2cp_prof1 
• 
Maximum frame size to transmit – 9600 bytes 
• 
Queue group profile –_group1 
• 
Administratively enabled. 
# config port eth cl-a/1 no shutdown 

## Displaying Ethernet Port Status  *(p.296)*


## Testing Ethernet Ports  *(p.296)*


## Configuration Errors  *(p.296)*

5. Cards and Ports 
# configure port ethernet cl-a/1 queue-group profile group1 
# configure port ethernet cl-a/1 l2cp prof1 
# configure port ethernet cl-a/1 egress-mtu 9600  
Displaying Ethernet Port Status  
You can display the status and configuration of an individual external Ethernet port. To display status of 
an Ethernet port:  
• 
At the prompt config>port>eth(<slot>/<port>)#, enter show status. 
The Ethernet port status parameters are displayed. 
For example: Module – M-ETH, Slot – 10, Ethernet port – 1, copper RJ-45 connector.  
 
config>port>eth(1/1)# show status 
Name IO-1 ethernet 01 
 
Administrative Status : Up 
Operational Status    : Down 
Connector Type        : RJ45 
Auto Negotiation      : Configuring 
MAC Address           : 00-20-D2-92-1B-5E 
 
 
Note 
For GbE ports, assigned MAC addresses are also displayed. For MAC address 
allocation mechanism, see Chapter 10.  
Testing Ethernet Ports 
No testing is available. 
Configuration Errors 
The following tables list messages generated by Megaplex-4 when a configuration error on Ethernet 
ports is detected. 

## Displaying Ethernet Port Statistics  *(p.297)*

5. Cards and Ports 
Ethernet Configuration Error Messages  
Code 
Type 
Syntax 
Meaning 
407 
Error 
SUM POWER EXCEEDED  
The total allocated power per Megaplex-4 system must not 
exceed 250W. 
There is limitation of 250W, per Megaplex-4 chassis, due to 
PS limitation. These 250W are shared between the following 
modules: 
• Voice FXS (VC) modules – consuming 1.5W per port. 
This sanity appears if you open too many ports, with overall 
consumption of more than 250W. To correct, close some 
ports. 
587 
Warning SUM OF POLICERS RATE 
EXCEED SUPPORTED BW 
The total sum of bandwidths defined in policer profiles for 
all 8 ports of the M-ETH module must not exceed 1 GbE.  
Displaying Ethernet Port Statistics 
The Ethernet ports feature statistics collection in accordance with RMON-RFC2819.  
 To display the Ethernet port statistics:  
• 
At the prompt config>slot>port>eth(<slot>/<port>)#, enter show statistics. 
Ethernet port statistics are displayed. The counters are described in the table below. 
Screens and counters are different for Fast Ethernet ports of I/O modules and GbE ports of CL.2 
modules. 
M-ETH Module: 
config>port>eth(7/3)# show statistics 
Running 
----------------------------------------------------------------- 
Counter          Rx                   Tx 
Total Frames     0                    9 
Total Octets     0                    2002 
Unicast Frames   0                    0 
Multicast Frames 0                    0 
Broadcast Frames 0                    9 
 
Paused Frames    0                    0 
FCS Errors       0                    -- 
Filtered Frames  0                    -- 
Jabber Errors    0                    -- 
Undersize Frames 0                    -- 
5. Cards and Ports 
Oversize Frames  0                    -- 
Discard Frames   --                   0 
 
64 Octets        0                    0 
 
65-127 Octets    0                    4 
128-255 Octets   0                    0 
256-511 Octets   0                    5 
512-1023 Octets  0                    0 
1024-1518 Octets 0                    0  
1519-Max Octets  0                    0 
CL.2 Module:  
config>port>eth(cl-a/1)# show statistics 
Running 
--------------------------------------------------------------- 
Counter               Rx                   Tx 
Total Frames          0                    0 
Total Octets          0                    0 
Unicast Frames        0                    0 
Multicast Frames      0                    0 
Broadcast Frames      0                    0 
 
Single Collision     --                    0 
Paused Frames         0                    0 
FCS Errors            0                   -- 
Ethernet Statistics Parameters 
Parameter 
Description 
Note 
Total Frames 
Total number of frames received/transmitted 
 
Total Octets 
Total number of bytes received/transmitted 
 
Unicast Frames 
Total number of unicast frames received/transmitted 
 
Multicast Frames 
Total number of multicast frames received/transmitted 
 
Broadcast Frames 
Total number of broadcast frames received/transmitted 
 
Single Collision 
The number of successfully transmitted frames on this interface 
for which transmission is inhibited by exactly one collision.  
CL.2 GbE ports only 
Paused Frames 
Total number of pause frames (used for flow control) 
received/transmitted through the corresponding Ethernet port 
 
FCS Errors 
The number of frames received on this interface that are an 
integral number of octets in length but do not pass the FCS 
check 
 
5. Cards and Ports 
Parameter 
Description 
Note 
Filtered Frames   
 
Total number of filtered frames received/transmitted 
I/O Ethernet ports only 
Jabber Errors 
Total number of frames received with jabber errors 
I/O Ethernet ports only 
Oversize Frames 
Total number of oversized frames received/transmitted 
I/O Ethernet ports only 
Undersize Frames 
Total number of undersized frames received/transmitted 
I/O Ethernet ports only 
Discard Frames   
Total number of discarded frames received/transmitted 
M-ETH ports only 
64 Octets 
Total number of received/transmitted 64-byte packets  
I/O Ethernet ports only 
65–127 Octets 
Total number of received/transmitted 65–127-byte packets 
I/O Ethernet ports only 
128–255 Octets 
Total number of received/transmitted 128–255-byte packets 
I/O Ethernet ports only 
256–511 Octets 
Total number of received/transmitted 256–511-byte packets 
 
 
 
I/O Ethernet ports only 
512–1023 Octets 
Total number of received/transmitted 512–1023-byte packets 
I/O Ethernet ports only 
1024–1518 Octets 
 
Total number of received/transmitted 1024–1518-byte packets  
I/O Ethernet ports only 
1519 - Max Octets  
Total number of received/transmitted packets with 1519 bytes 
and up to maximum  
M-ETH ports only 
 To clear the statistics for an Ethernet port: 
• 
At the prompt config>port>eth<slot>/<port>)#, enter clear-statistics. 
The statistics for the specified port are cleared. 