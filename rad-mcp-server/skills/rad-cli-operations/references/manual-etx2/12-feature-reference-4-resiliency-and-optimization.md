# Feature Reference – 4 Resiliency and Optimization

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 802–862.*


## 4.1 Ethernet Linear Protection  *(p.802)*

4 Resiliency and Optimization 
This chapter describes features related to resiliency and optimization: 
• 
Ethernet Linear Protection  
• 
Ethernet Ring Protection (ERP) 
• 
Fault Propagation 
• 
Link Aggregation 
• 
Link Protection 
4.1 Ethernet Linear Protection 
ETX-2i provides unidirectional (no protocol) and bidirectional protection switching for network ports per 
ITU-T G.8031, optionally using APS protocol. 
Ethernet linear protection provides a way to protect the flows belonging to an EVC. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products, with the following condition: 
• 
PCS port is relevant to ETX-2i with an SHDSL or VDSL2 module. 
G.8031 is supported over network ports. 
• 
ETP transport ports can be bound to network ports only (per user/network policy). 
ETX-2i supports up to 16 EVC Termination Points (ETPs) per device. 
There can be a maximum of eight flows from UNI port to the subscriber port. 
 
 
ETX-2i Devices 
4. Resiliency and Optimization 
The protection time is as follows: 
• 
One EVC pair – 50ms protection  
• 
Four EVC pairs – 200ms protection 
Pseudowire (PW) over ETP is not supported. 
Standards Compliance 
ITU-T G.8031 
Functional Description 
Protection is based on an EVC Termination Point (ETP). An ETP has one subscriber port and one or more 
transport ports. Multiple transport ports are used for protection only. There are two kinds of flows 
connected to the ETP ports: subscriber flows and transport flows.  
• 
Subscriber flows run between UNIs and ETP subscriber port. You can define classification and 
policing on subscriber flows, as well as marking.  
• 
Transport flows run between ETP transport ports and NNIs. You can define actions such as push, 
pop, and marking on transport flows. 
Note 
You can define transport flows between ETP transport ports and logical MAC 
ports corresponding to MiRICi-155 smart SFPs.  
Flows entering the ETP assign an internal CoS value to every frame using mapping profiles 
(priority-to-CoS) or by setting fixed CoS values. 
Flows exiting the ETP perform queuing based on the internal CoS value using mapping profiles 
(CoS-to-queue). 
Triggers are: 
• 
Port signal loss  
• 
CCM LOC, RDI, or interface status TLV indicating interface down 
• 
ETH-AIS  
ETX-2i Devices 
4. Resiliency and Optimization 
ETP Flow Attributes 
The following table shows which attributes you can configure for ETP flows. 
 
Attribute 
Subscriber 
(UNI to ETP) 
Subscriber  
(ETP to UNI) 
Transport 
(NNI to ETP) 
Transport  
(ETP to NNI) 
Ingress port 
Required 
Required 
Required 
Required 
Egress port 
Required 
Required 
Required 
Required 
Classifier profile 
Required, with any type of 
criteria 
Required, with 
criteria: 
Unclassified or 
VLAN 
Required, with 
criteria: 
SP VLAN 
Required, with 
criteria: 
Unclassified 
Policer profile 
Optional 
Optional 
Not allowed  
Not allowed 
Queue / block 
Not allowed 
Required, with 
queue mapping 
profile classified by 
CoS 
Not allowed 
Required, with 
queue mapping 
profile classified by 
CoS 
CoS 
Required, with CoS mapping 
profile 
Not allowed 
Required, with 
CoS mapping 
profile 
Not allowed 
VLAN tag (push) 
Optional 
Not allowed 
Not allowed 
For at least one of 
the actions, 
marking profile 
classified by CoS 
Mark 
Required, with marking 
profile classified by CoS 
Required, with CoS 
mapping profile 
For at least one 
of the actions, 
CoS mapping 
profile 
VLAN tag (pop) 
Not allowed 
Optional 
Not allowed 
Drop 
Optional 
Optional 
Optional 
Optional 
EVC Protection Switching 
EVC protection (1:1) is based on the ETP model. One of the transport ports is the working transport 
entity and the other port serves as the protection transport entity. 
Monitoring both working and protection transport entity is done via MEPs exchanging CCMs. In 
addition, the protection transport optionally runs APS protocol. 
When working without APS, switchover is affected by local events only (signal failure trigger, switch back 
to port after failure ends, manual switchover due to command). In one-to-one bidirectional mode, upon 
switchover both the EVC Rx and Tx flows move to the second path. 
ETX-2i Devices 
4. Resiliency and Optimization 
Master and Slave ETPs 
You can define one master ETP and several slave ETPs. The master ETP must have all the configuration 
of the protection, same as single ETP. The slave ETPs point to the master ETP via master command and 
bind each port ID to working/protection. 
The master ETP index MUST be lower than the index of the slave ETPs. You must create the master ETP 
before creating the slave ETPs. 
Management over ETP 
ETX-2i can be managed via a router interface connected to the ETP subscriber port. 
EVC and OAM 
On each transport entity, you must define a MEP to use as the signal failure trigger if working in APS 
mode, in order to monitor the connection using CCM. The MEPs must be activated so that the 
protection switching mechanism can monitor both working and protection transport entities. 
Monitoring can be accomplished by exchanging CCMs as defined in ITU-T Rec. Y.1731. In non-APS mode, 
the signal failure trigger can be a MEP or port status.   
In addition, the MEP can be defined to perform other Y.1731 services such as measuring delay and loss 
on the specific EVC. If an Up MEP associated with the transport is associated with an untagged classifier 
profile, services can still be defined for it; the Up MEP is transparent to the CVLAN, and the OAM 
transmitted from the ETP transport ports can be edited according to the SVLAN. 
EVC Fault Propagation 
You can define fault propagation based on EVC failure detection (ETP operation status) to shut down the 
UNIs that connect to it. The fault trigger can be one of the following: 
• 
In case of protection – the signal failure trigger MEP for ETP transport ports 
• 
In other cases – the NNI operation status 
EVC Loopback 
You can activate a loopback on any of the transport ports toward the network and on the subscriber 
port toward the user or network. 
In most cases you would activate a loop on the subscriber port toward the network, thus you can loop 
the EVC traffic without affecting protection. 
ETX-2i Devices 
4. Resiliency and Optimization 
If you wish to run a loop on a specific EVC path when you activate the loop on the transport ports, you 
have two options: 
• 
Loopback on a transport port affects OAM, as any traffic EVC path redundancy is triggered if 
present. 
• 
Loopback only data without affecting redundancy. 
Factory Defaults 
By default, no ETPs are configured. 
When you create an ETP port, by default it is configured as follows: 
• 
Name = “ETP <etp-name> Subscriber Port <port-index>” or 
““ETP <etp-name> Transport Port <port-index>”, according to whether port is subscriber or 
transport 
• 
Administratively enabled 
When you first enter the ETP protection level, by default the protection is configured as follows: 
ETX-2i#configure etps etp ETP1 protection 
ETX-2i>config>etps>etp(ETP1)>protection$ info detail 
    shutdown 
    no master-etp 
    mode  bi-directional-1-to-1 
    no aps-protocol 
    revertive 
    wait-to-restore  300 
 
ETX-2i>config>etps>etp(ETP1)>protection$ 
Configuring ETPs 
This section describes how to configure ETPs. You can configure up to 16 ETPs per device. 
 To configure ETPs: 
1. Navigate to configure etps etp <name> to select the ETP to configure. 
The ETP is created if it does not already exist, and the config>etps>etp(<name>)# prompt is 
displayed. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
Configuring ETP port 
[no] port {subscriber | transport} <port-id> 
Use the no form to remove the port. 
The port-id range is 1–2. 
See the procedure below for more 
information on configuring ETP ports. 
Configuring ETP protection 
[no] protection 
See Configuring ETP Protection for more 
information. 
Displaying ETP status 
show status 
 
Displaying ETP statistics 
show statistics running 
 
Displaying flows 
corresponding to ETP 
show flows-summary 
 
Clearing ETP statistics 
clear-statistics 
 
 To configure ETP ports: 
1. Navigate to configure etps etp <name> to select the ETP to configure. 
The config>etps>etp(<name>)# prompt is displayed. 
2. Type the following command to configure a port, where port-index can be 1 for subscriber 
ports, or 1–2 for transport ports: 
port {subscriber | transport} <port-index> 
The prompt is displayed according to whether you typed subscriber or transport: 
config>etps>etp(<name>)>port(subscriber/<port-index>)# 
config>etps>etp(<name>)>port(transport/<port-index>)# 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Activating loopback 
[no] loopback [local | remote] 
[duration <seconds>]  
 
Assigning name to ETP port 
[no] name <string> 
 
Displaying loopback status 
show loopback 
 
Displaying status 
show status 
 
Administratively enabling 
ETP port 
no shutdown 
Entering shutdown disables the port. 
Note: When the port is created, it is enabled by default. 
 
ETX-2i Devices 
4. Resiliency and Optimization 
Configuring ETP Protection 
To configure ETP protection, you define the working and protection ports, as well as other protection 
parameters. 
 To configure ETP protection: 
1. Navigate to configure etps etp <name> protection to configure protection for the selected ETP. 
The config>etps>etp(<name>)>protection# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Defining APS protocol for ETP 
[no] aps-protocol 
 
Defining transport port ID for 
protection or working port 
[no] bind {protection | working} transport 
<protection-port> 
Adds/removes working and protection 
ports to/from the APS 
Clearing the active near end 
lockout of Protection, Forced 
Switch, Manual Switch, WTR 
state, or Exercise command 
clear 
 
Forcing normal traffic signal to 
be selected from the protection 
transport entity, meaning jump 
to next port even if it is down 
force-switch 
 
Preventing a working signal 
from being selected from the 
protection transport entity, 
effectively disabling the 
protection group 
lockout 
Relevant for 1+1 bi-optimized 
bidirectional mode 
Forcing normal traffic signal to 
be selected from the protection 
transport entity in the absence 
of failure of working or 
protection transport entity, 
meaning jump to next port only 
if it is not down 
manual-switch 
 
Defining master ETP 
[no] master-etp <etp-name> 
 
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
Configuring protection mode 
mode { uni-directional-1-plus-1 | 
bi-directional-1-plus-1 | bi-directional-1-to-1 } 
uni-directional-1-plus-1 – provides 1:1 
unidirectional protection 
bi-directional-1-plus-1 – not supported 
bi-directional-1-to-1 – provides 1:1 
bidirectional protection 
Enables/disables reverting the 
working port and protection 
port 
[no] revertive 
 
Defining signal failure trigger  
sf-trigger { protection | working } port ethernet 
[<slot>/]<port-index> 
sf-trigger { protection | working } port 
logical-mac <port-number> 
sf-trigger { protection | working } mep <md-id> 
<ma-id> <mep-id> 
sf-trigger { protection | working } port pcs 
<port-number> 
no sf-trigger { protection | working } 
You can use MEPs from flows other than 
the ETP transport flows. 
md-id – Maintenance Domain (OAM 
CFM)  
Possible values: 0-0xFFFF 
ma-id – Maintenance Association (OAM 
CFM)  
Possible values: 0-0xFFFF 
mep-id – MEP ID (OAM CFM) 
Possible values: 1-8191 
Defining time between recovery 
and resumption of transmission 
wait-to-restore <seconds> 
 
Displaying protection status 
show status 
 
Administratively 
enabling/disabling ETP 
protection 
[no] shutdown 
 
Examples 
 To configure an ETP: 
• 
Name = ETP1 
• 
Port members = subscriber 1, transport 1, transport 2 
exit all 
configure etps etp ETP1 
port subscriber 1 
exit 

## 4.2 Ethernet Ring Protection (ERP)  *(p.810)*

ETX-2i Devices 
4. Resiliency and Optimization 
port transport 1 
exit  
port transport 2 
exit all 
 To configure ETP protection: 
• 
ETP name = ETP1, port members = subscriber 1, transport 1, transport2 
• 
Protection mode = bidirectional 1:1 
• 
APS protocol used for protection 
• 
Working port = transport 1 
• 
Protection port = transport 2 
• 
Signal failure triggers = working MEP: MD 3 MA 2 MEP 1, protection MEP: MD 4 MA 2 MEP 1 
Note 
The MEPs must be active.  
• 
Revertive mode 
• 
Time to wait before restoring transmission = 300 seconds 
exit all 
configure etps etp ETP1 protection 
mode bi-directional-1-to-1  
aps-protocol 
bind working transport 1 
bind protection transport 2 
sf-trigger working mep 3 2 1 
sf-trigger protection mep 4 2 1 
revertive 
wait-to-restore 300 
no shutdown 
exit all 
4.2 Ethernet Ring Protection (ERP) 
A G.8032 Layer-2 Ethernet ring, a logical ring defined above a bridge, protects against link and node 
failures. G.8032 rings provide sub 50ms protection for Ethernet traffic. 
ETX-2i Devices 
4. Resiliency and Optimization 
Applicability and Scaling 
This feature is applicable to all ETX-2i products, with the following conditions: 
• 
ETX-2i, ETX-2i-B, and ETX-2i-10G-B/8SFPP support up to six ring instances. 
• 
ETX-2i-10G supports up to eight ring instances. 
• 
Device with ERP supports 50ms ring switchover time. 
• 
ETX-2i-100G/4QSFP support up to 10 G.8032 ring instances. Major rings and subrings (with or 
without R-APS Virtual Channel mode) are supported; multiple ring instances per physical port 
are not supported. 
• 
PCS port is relevant to ETX-2i with an SHDSL or VDSL2 module. 
Standards Compliance 
ITU-T G.8032v2, Y.1731 
Functional Description 
Ethernet Ring Protection (ERP) technology provides a scalable solution for low-cost traffic protection 
and rapid service restoration, with SDH/SONET-type resilience. It is built on traditional Ethernet MAC 
(IEEE 802.3) and bridging (IEEE 802.1) functionality. It is independent of any physical layer technologies 
and can be utilized in any carrier network.  
A ring can be configured on any Ethernet port - network or user.  
 
Note 
Rings are color-aware via the setting of the DEI bit: 
• 
Set to 0 – maps to green 
• 
Set to 1 – maps to yellow 
No additional configuration is needed for the color-aware functionality.  
You can also define the color-aware functionality of the ring by associating the 
ring with a predefined color mapping profile (see Color Mapping). This is an 
alternative method to using the DEI bit setting.  
 
 
ETX-2i Devices 
4. Resiliency and Optimization 
Ring Topology 
ETX-2i supports the following topologies: 
• 
Multi-ring  
 
• 
Major ring with multiple sub-rings 
 
Multiple rings with a common link are usually referred to as ladder network (see below). 
The following terms are commonly used for describing ladder ring topology: 
• 
Interconnection nodes – ring nodes that are common to both interconnected rings (nodes C and 
G below) 
• 
Major ring – an Ethernet ring that controls a full physical ring and is connected to the 
interconnection nodes on two ports (ring A-H-G-C-B below) 
• 
Sub-ring – an Ethernet ring that is connected to a major ring at the interconnection nodes. By 
itself, the sub-ring does not constitute a closed physical ring. A sub-ring is connected to the 
interconnection nodes on only one port (ring C-D-E-F-G below). Link C–G is not a part of the 
sub-ring; it is controlled by the major ring.  
G.8032 supports two operation modes of sub-rings: 
 
Sub-ring with an R-APS virtual channel – A virtual R-APS channel connection is established 
between two interconnection nodes of the sub-ring over a network or other ring, to tunnel 
R-APS messages. In this mode, R-APS of the sub-ring is configured as a data VLAN in the 
Major ring.  
ETX-2i Devices 
4. Resiliency and Optimization 
 
Sub-ring without an R-APS virtual channel – The R-APS channel is terminated at the 
interconnection nodes and its R-APS messages are not tunneled between the 
interconnection nodes. In this mode, R-APS of the sub-ring is not configured as a data VLAN 
in the Major ring. 
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
 
Physical Ladder Topology for Sub-Ring with R-APS Virtual Channel 
Note 
Sub-rings without R-APS virtual channel do not have a Virtual Channel 
between G and C.  
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
 
Major Ring and Sub-Ring 
In ladder networks, a common VLAN is shared on more than one physical ring. For example, a user 
connected to node E communicates with a user connected to node A over the same VLAN. Ring topology 
includes a physical link between nodes G and C. It belongs to the major ring and is used by the sub-ring 
as its R-APS channel. Note that a sub-ring without a virtual channel would not have an R-APS virtual 
channel between nodes G and C. 
ETX-2i Devices 
4. Resiliency and Optimization 
Ring Protection Links 
An Ethernet ring consists of multiple Ethernet nodes, each connected to adjacent Ethernet nodes using 
two independent ring links. In order to prevent loops, the ring uses a specific link to protect the ring, 
designated as the Ring Protection Link (RPL). When there are no failures in the ring, the RPL is blocked. 
When a failure is detected, the RPL is unblocked. 
R-APS Control Messages 
Nodes on the ring use Ring Automatic Protection Switching (R-APS) messages to coordinate ring 
protection switching. R-APS messages are transmitted over a VLAN designated as the R-APS VLAN.   
ETX-2i supports the configuration of a Ring ID parameter per ring instance (both major and sub). The 
configured Ring ID parameter is used as the suffix of the R-APS DA MAC address, so that R-APS messages 
are sent to 01-19-A7-00-00-<Ring ID>. For example, if you configure Ring ID of ring 3 as 03, R-APS 
messages will be sent to 01-19-A7-00-00-03. 
 
Note 
A single R-APS session is supported per VLAN.  
Multiple Ring Instances on a Single Port 
ETX-2i with Virtual Ring support enables multiple ring instances to reside over the same physical port, 
allowing better bandwidth utilization of the ring in Idle state.  
Each ring instance resides on a different set of bridge ports and supports R-APS on a different VLAN.  
It is not possible to allocate the same VLANs to ring instances residing on the same physical port; this 
results in a sanity error. In other words, if the same physical port is used for an ERPS sub-ring and major 
ring, you cannot configure the same data VLAN over both. 
The same MEP can be used as an sf-trigger to multiple rings residing on the same physical link. 
 
Multiple Rings on Single Physical Port  
ETX-2i Devices 
4. Resiliency and Optimization 
Passthrough VLANs 
Passthrough VLANs over the ring are those VLANs that are not added/dropped to the ring at the local 
ring node (ETX), but only traverse via the ring node (East to West or vice versa).  
By default, added/dropped VLANs at the local ring node, as well as passthrough VLANs, must be 
configured as data VLANs, and each one is assigned a bridge broadcast domain (device resource).  
ETX-2i ring configuration supports a passthrough attribute, which automatically assigns a ring/bridge 
bypass (East to West, West to East) for all passthrough traffic (i.e., all traffic other than the local 
added/dropped VLANs that are configured as data VLANs and use bridge broadcast domains). 
Passthrough traffic can be configured for either the full VLAN range other than the VLANs defined as 
data VLANs, or for a specific range of VLANs (again excluding the in-range added/dropped VLANs 
configured as data VLANs). 
As they do not go through the bridge and use its resources, ETX-2i allows an unlimited number of 
passthrough VLANS to enter the ring and does not require configuring them as data VLANs. 
Added/dropped VLANs at the local ring node still need to be configured as data VLANs. The number of 
added/dropped VLANs is limited, because they go through the bridge and use up its resources (bridge 
broadcast domains). 
Use of passthrough VLANs upscales the ring capacity – an unlimited number of passthrough services can 
travel through the ring; there is only a limit to the number of ring services added/dropped at the local 
ring node (maximum number of broadcast domains per local node). Without using the passthrough 
attribute, the maximum broadcast domain supported in a single local node limits the number of VLANs 
at the entire ring to this number. 
Protection Switching Functionality 
In idle state, traffic flows over all the ring links except the RPL. The RPL is controlled by a node called the 
RPL owner, which blocks the RPL when in idle state, in order to prevent loops. Each link is monitored by 
its two adjacent nodes (east and west ports) using standard ETH CC OAM messages per Y.1731 
(optional), or port physical status. 
When a node detects link failure, it transmits an R-APS Signal Fail (SF) message periodically, until link 
recovery is detected. Upon receiving the R-APS (SF), the RPL owner unblocks the RPL port. 
When a node detects link recovery, it sends R-APS No Request (NR) periodically until R-APS No Request, 
RPL Blocked (NR, RB) is received from the RPL owner. R-APS (NR, RB) is sent by the RPL owner to indicate 
that the ring has no failure and the RPL has been blocked. Nodes receiving R-APS (NR, RB) flush their 
MAC learning table, unblock their ports, and return to idle state. 
ETX-2i Devices 
4. Resiliency and Optimization 
After link recovery is detected, the adjacent nodes (to the initial failure) start to send R-APS with (NR, 
NB). When these packets get to the RPL owner, it starts a WTR (Wait To Restore) timer. If during the 
predefined value of this timer, no additional link failure is detected, the RPL Owner starts to send R-APS 
with (NR, RB) (RB = RPL Blocked) and blocks the RPL. Nodes receiving R APS (NR, RB) flush their MAC 
learning table, unblock their ports, and return to idle state. 
ERP Timers 
The following timers are used in ERP operation: 
Wait to Restore (WTR) 
Period used by RPL owner to verify that the ring has stabilized before blocking the RPL 
after signal recovery. Non-configurable; permanently set to 300 seconds. 
Guard 
Period during which all received R-APS messages are ignored by the ERP mechanism. 
This prevents the ring nodes from receiving outdated R-APS messages. 
Holdoff 
Period during which the Ethernet layer does not report link faults to the ERP 
mechanism. This filters out intermittent link faults. 
Ring Commands 
In addition to failure detection, protection switching can be initiated by the following commands: 
Force switch  
Forcefully blocks a particular ring port. It can be issued even if an SF condition exists on 
the ring, with multiple force switch commands allowed in the ring. 
Manual switch 
Manually blocks a particular ring port. It can be overridden by SF condition or a force 
switch command. Only one manual switch command is allowed in the ring. 
Clear 
Clears all existing force and manual switch commands in the ERP. 
Color Mapping 
ETX-2i supports color mapping configuration at ring nodes, in order to manage ring QoS.  
A ring can be configured with color mapping, according to either of the following methods: 
• 
DEI – the default; DEI value is not configurable; its default color aware functionality is as follows: 
 
DEI = 0 maps to green. 
 
DEI = 1 maps to yellow. 
ETX-2i Devices 
4. Resiliency and Optimization 
• 
Color mapping profile – associating ring with a predefined color mapping profile (p-bit to color). 
Refer to Color Mapping Profiles in Traffic Processing chapter on how to define a color mapping 
profile. 
By default, a ring is configured with DEI color mapping. 
CoS Mapping 
ETX-2i supports CoS mapping configuration at ring nodes, in order to manage ring QoS.  
By default, the ring is associated with a default one-to-one p-bit to CoS profile, where CoS 0 maps to the 
highest p-bit 7. 
 
You can associate a predefined CoS mapping profile to the ring. Refer to CoS Mapping Profiles in the 
Traffic Processing chapter on how to define a CoS mapping profile. 
Factory Defaults 
By default, there is no Ethernet protection ring created in the ETX-2i system. When the ring is created, it 
has the following default configuration. 
Parameter 
Default  
Remarks 
backward-compatibility 
no backward-compatibility 
Backward compatibility to G.8032v1 
bridge 
0 
color-mapping 
dei 
cos-mapping 
no-cos-mapping 
Associates the ring with the default one-to-
one p-bit to CoS profile, where CoS 0 maps to 
the highest p-bit 7 
east-port  
0 
ETX-2i Devices 
4. Resiliency and Optimization 
Parameter 
Default  
Remarks 
interconnection-node 
no interconnection-node 
passthrough-vlan 
no passthrough-vlan 
Default is no passthrough-vlan mode, i.e., 
added/dropped VLANs at the local ring node, 
as well as passthrough VLANs, must be 
configured as data VLANs, and each one is 
assigned a bridge broadcast domain (device 
resource). 
port-type 
east node-port 
west node-port 
r-aps 
vlan 0 vlan-priority 0 mel 255 
ring-id 
no ring-id 
shutdown 
shutdown 
timers  
guard 500 holdoff 0 wtr 300 
west-port 
0 
Configuring Ethernet Ring Protection 
The ring configuration sequence is as follows: 
1. Configure the bridge (refer to Configuring the Bridge in the Traffic Processing chapter).  
2. Configure the ring. 
3. Configure flows (refer to Configuring Flows in the Traffic Processing chapter). 
4. Configure the router (refer to Configuring the Router in the Traffic Processing chapter).  
Note 
ETX-2i-100G only supports flow classification; it does not support port 
classification. 
 To configure ERP: 
1. At the config>protection # prompt, enter:  
erp <ring-number> [{major | sub}] 
An ERP instance of the specified type is created if it does not already exist, and the 
config>protection>erp(<ring-number>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
Making the ring compatible with 
previous ERP implementations 
backward-compatibility 
no backward-compatibility 
 
Assigning ring to bridge  
bridge 1 
 
Clearing any existing force-switch 
or manual-switch command 
clear 
 
Clearing ERP statistics 
clear-statistics [{ east | west }] 
 
Defining color mapping type for 
ring 
color-mapping { dei | profile <profile-
name> } 
Packet at ring ingress and at any 
node mapped to color according 
to one of the following: 
dei – DEI (default) 
profile – predefined p-bit color 
mapping profile (p-bit to color); 
string 1-32 characters 
Associating CoS profile with ring 
cos-mapping profile <cos-mapping-
profile-name> 
no cos-mapping 
profile – predefined p-bit color 
mapping profile (p-bit to color); 
string 1-32 characters 
no cos-mapping associates the 
ring with a default one-to-one 
p-bit to CoS profile, where CoS 0 
maps to the highest p-bit. 
Defining description text for ring 
description <string> 
 
Defining the east port of a ring 
node 
east-port <bridge-port-number> 
ethernet [<slot>/]<port-index> 
east-port <bridge-port-number> 
logical-mac <port-number> 
east-port <bridge-port-number> 
pcs <port-number> 
 
 
Blocking the east or west port of a 
ring node, regardless of any 
failure conditions 
force-switch { east | west } 
The force switch can be applied to 
any number of nodes in the ring. 
Defining ERP node as an 
interconnection node, sharing 
more than one ring 
interconnection-node 
 
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
Blocking the east or west port of a 
ring node manually 
manual-switch { east | west} 
The manual switch command can 
be applied to a single ring node 
only.  
Defining description text for port 
port-description { east | west } <string> 
 
Defining ring port type  
port-type { east | west } { node-port | 
rpl | neighbor | next-neighbor } 
node-port – Port is not connected 
to RPL.  
rpl – Port is designated as RPL. 
neighbor – Port is directly 
connected to RPL owner. 
next-neighbor – Port is connected 
to RPL owner via neighbor. 
Configuring dedicated VLAN for 
R-APS messages 
r-aps [vlan <vlan-id>] 
[vlan-priority <vlan-priority>] 
[mel <level>] 
vlan-id: 1–4094 
vlan-priority: 0–7 
level: 0–7.  
The mel parameter specifies the 
maintenance entity group (MEG) 
level (MEL) of the R-APS 
messages. 
Defining whether ring reverts 
back to original RPL when failure 
is cleared 
revertive 
Enter no revertive to specify 
non-revertive operation. 
Configuring the ring ID 
ring-id <number> 
no ring-id 
Used to configure destination of 
R-APS messages. ring-id is 
appended to the R-APS DA MAC 
address as follows: 
01-19-A7-00-00-<Ring ID> 
Possible values: 1-255 (00-FF) 
Enabling propagation of Signal 
Failure (SF) condition from the 
Ethernet OAM service layer  
sf-trigger { east | west } mep <md-id> 
<ma-id> <mep-id> 
no sf-trigger { east | west } 
Before enabling SF propagation, 
verify that the relevant CFM 
parameters have been configured.  
Connecting previously defined 
sub-ring to a major ring 
sub-ring <sub-ring-number> 
Note: This is available for major 
rings only. The sub-ring number 
must be lower than the number 
of the major ring it is assigned to. 
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
Defining ring timers 
timers [guard <guard-msec>] 
[holdoff <holdoff-msec>] 
guard – While the guard timer is 
active, all received R-APS 
messages are ignored by the 
node, thus preventing the receipt 
of outdated R-APS messages. The 
range is 10 ms to 2 seconds in 
10 ms steps.  
holdoff – specifies the amount of 
time an ERP-enabled node waits 
from the point it recognizes a 
local failure until it reacts to the 
failure, i.e., it blocks the port 
adjacent to the failed link and 
send R-APS (SF) to the RPL owner. 
The range is 0 to 10 seconds in 
100 ms steps.  
Defining data VLANs for user 
traffic 
vlan <vlan-id> 
If using no passthrough-vlan 
mode (the default), configure 
both added/dropped and 
passthrough VLANs as data 
VLANs. If configuring passthrough 
VLANs, configure dropped VLANs 
only. 
Note: In Passthrough VLAN mode, 
if you configure a passthrough 
VLAN as a data VLAN, it behaves 
as an added/dropped VLAN, and 
goes through the bridge, instead 
of bypassing it.  
To remove the VLAN assignment, 
enter: no vlan <vlan-id>. 
Before removing the VLAN 
assignment, verify that all flows 
using this VLAN have been 
disabled.  
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
Enabling passthrough VLANs  
passthrough-vlan [<vlan-range>] 
[queue-block east <qb-east> west <qb-
west>] 
no passthrough-vlan 
Configure all VLANs or an explicit 
range of VLANs, excluding those 
defined as data VLANs, as 
passthrough VLANs.  
East and west queue blocks can 
optionally be configured.  
Enter no passthrough-vlan (the 
default) to use the regular mode, 
where both added/dropped 
VLANs at the local ring node and 
passthrough VLANs must be 
configured as data VLANs and are 
each assigned a bridge broadcast 
domain (device resource). 
Commands in vlan level 
 
 
Defining the queue blocks for the 
VLAN 
queue-block east <east-block> 
west <west-block> 
 
Assigning service name to VLAN 
service-name <name> 
 
Administratively enabling the 
VLAN  
no shutdown 
Enter shutdown to disable the 
VLAN. 
Defining amount of time for RPL 
owner to wait before blocking 
RPL after failure recovery 
wait-to-restore <seconds> 
This timer specifies how long the 
RPL owner waits to verify that ring 
failures have been cleared, before 
blocking the RPL. The range is 1 
min (60 sec) to 12 min (720 sec). 
Defining the west port of a ring 
node 
west-port <bridge-port-number> 
ethernet [<slot>/]<port-index> 
west-port <bridge-port-number> 
logical-mac <port-number> 
west-port <bridge-port-number> 
pcs <port-number> 
 
 
Administratively enabling the ERP  
no shutdown 
Type shutdown to disable the 
ERP. 
Displaying ERP status 
show status 
See Viewing ERP Status.  
Displaying ERP statistics 
show statistics 
See Viewing ERP Statistics. 
ETX-2i Devices 
4. Resiliency and Optimization 
Examples 
This section illustrates the following configuration: 
• 
VLAN-aware bridge, with bridge ports 1–4 
• 
Ring: 
 
East port – Bridge port 1, Ethernet port 0/1  
 
West port – Bridge port 2, Ethernet port 0/2  
 
R-APS VLAN – 57 
 
User traffic VLANs – 100, 4000 
• 
Management flows (unidirectional) between SVI 1 and bridge port 4, over VLAN 4000 
• 
Traffic flow (bidirectional) between Ethernet port 0/3 and bridge port 3, with classification 
VLAN 100 
#*******Configure SVI 
exit all  
configure port svi 1  
  no shutdown  
  exit all 
 
 
# *******Configure bridge and bridge ports 
configure bridge 1  
  port 1  
    no shutdown  
    exit 
  port 2  
    no shutdown  
    exit 
  port 3  
    no shutdown  
    exit 
  port 4  
    no shutdown  
    exit all 
 
# *******Configure Ethernet Ring Protection 
configure protection  
  erp 1 major  
    bridge 1  
    east-port 1 ethernet 0/1  
    west-port 2 ethernet 0/2  
    r-aps vlan 57 vlan-priority 0 mel 3  
    port-type east node-port  
    port-type west node-port 
    color-mapping dei 
    cos-mapping my-p-bit   
ETX-2i Devices 
4. Resiliency and Optimization 
    vlan 100  
      queue-block east 0/1 west 0/1  
      no shutdown  
      exit 
 
    vlan 4000  
      queue-block east 0/2 west 0/2  
      no shutdown  
      exit 
 
    timers holdoff 0  
    no shutdown  
    exit all 
 
#*******Configure classifier profiles 
configure flows  
  classifier-profile v100 match-any  
    match vlan 100  
    exit 
  classifier-profile v4000 match-any  
    match vlan 4000  
    exit 
  classifier-profile all match-any  
    match all  
    exit 
 
#*******Configure flows 
  flow data  
    classifier v100  
    ingress-port ethernet 0/3  
    egress-port bridge-port 1 3  
    reverse-direction block 0/1  
    no shutdown  
    exit 
 
  flow mng_in  
    classifier v4000  
    no policer  
    vlan-tag pop vlan  
    ingress-port bridge-port 1 4  
    egress-port svi 1  
    no shutdown  
    exit 
 
  flow mng_out  
    classifier all  
    no policer  
    vlan-tag push vlan 4000 p-bit fixed 0  
    ingress-port svi 1  
    egress-port bridge-port 1 4  
    no shutdown  
    exit all 
ETX-2i Devices 
4. Resiliency and Optimization 
#*******Configure router 
 interface 
configure router 1  
  interface 1  
    address 172.18.141.11/24  
    bind svi 1   
    no shutdown  
    exit 
    static-route 0.0.0.0/0 address 172.18.141.1  
  exit all 
save 
Viewing ERP Status 
You can display the current status of an ERP entity. 
 To display ERP status: 
• 
At the config>protection>erp(<erp-number>)# prompt, enter: 
show status 
The ERP status is displayed. 
ETX-2i>config>protection>erp(1)$ show status 
 
Bridge Number : 0            East Port  : 0    West Port  : 0 
RPL Link      : Not Owner 
Ring State    : Init 
 
 
 
East Port Status : Block R-APS and Data Local SF Source 
West Port Status : Block R-APS and Data Local SF Source 
ERP status provides information on: 
 
Bridge number 
 
Bridge ports assigned to be East and West ring ports 
 
RPL link role: 
 
Not owner – All other nodes on the ring (that is, those that are not the RPL owner node) 
operate as normal nodes and have no special role on the ring. 
 
RPL owner – This node owns the RPL and blocks or unblocks the RPL as conditions 
require. This node initiates the R-APS message. 
 
 
ETX-2i Devices 
4. Resiliency and Optimization 
 
Ring state: 
 
Init – The node is disabled (in ‘shutdown’). 
 
Idle – The node is performing normally (there is no link failure on the ring). In this state, 
traffic is unblocked on both ring ports, except for the RPL owner node, which blocks the 
RPL port (the other RPL owner port is unblocked) and the RPL neighbor port. 
 
Pending – transition state between ‘Protected’ and ‘Idle’ (only in this direction). This 
state means that the device detected that a signal failure state was cleared and started 
the WTR timer. After the WTR timer consumes itself, the state changes to ‘Idle’. 
 
Protected – A failure occurred on the ring. A non-owner node has traffic blocked on the 
ring port that connects to the failed link. The RPL owner, if it is not at one end of the 
failed link, unblocks the RPL port so both ports are active. 
 
East/West Port Status: 
 
Forward – Port is forwarding data. 
 
Block R-APS and Data – Port is blocked. 
 
East/West Port Local SF Source – Local Signal Failure source: 
 
OK – Port forwarding 
 
CFM CC – OAM failure  
 
Server Layer – Port down failure 
Viewing ERP Statistics 
You can view statistics on R-APS messages sent and received by the East and West ports. 
 To display ERP statistics: 
• 
At the config>protection>erp(<erp-number>)# prompt, enter 
show statistics 
The ERP statistic counters are displayed. 
ETX-2i>config>protection>erp(1)$ show statistics 
East Port 
---------------------------------------------- 
R-APS Message Rx Frames  Tx Frames 
SF            0          0 
NR            0          0 
NR,RB         0          0 
Total Valid   0          0 
Total Errors  0          0 
 
 
 

## 4.3 Fault Propagation  *(p.827)*

ETX-2i Devices 
4. Resiliency and Optimization 
West Port 
---------------------------------------------- 
R-APS Message Rx Frames  Tx Frames 
SF            0          0 
NR            0          0 
NR,RB         0          0 
Total Valid   0          0 
Total Errors  0          0 
 
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
4.3 Fault Propagation 
Fault propagation enables you to specify what action to take when a certain entity fails. 
Fault propagation ensures that you send packets via links that have not failed. Failures are propagated 
end-to-end via actions such as OAM CFM messages and entity deactivation, as well as VRRP priority 
decrement. 
ETX-2i Devices 
4. Resiliency and Optimization 
Applicability and Scaling 
This feature is applicable to all ETX-2i products, with the following conditions: 
• 
VRRP group is relevant to ETX-2i.  
• 
PCS port is relevant to ETX-2i with an SHDSL or VDSL2 module. 
Standards Compliance 
IEEE 802.1ag-D8 
ITU-T Y.1731 
Functional Description 
In the network-to-user or user-to-network direction, if a link fails for which fault propagation is enabled, 
the corresponding port shuts down or OAM CFM message indicating failure is sent, thus signaling the 
connected CPE to stop forwarding frames through the link.  
You can enable fault propagation to be triggered by failure detection on a network/user interface or 
entity, which causes a user-configurable action (such as deactivation or OAM CFM message indicating 
failure sent or lowering VRRP priority) to be performed on a user/network interface or entity. You can 
enable fault propagation in the network-to-user or user-to-network direction, for a pair of entities such 
as PCS port, Ethernet ports, MEPs, VRRP group, queue block Shaper, flow Policer, card (VDSL), TWAMP 
sessions, and ETPs. 
You can define the following when you enable fault propagation for a pair of entities: 
• 
Trigger: 
 
Failure detected on a router interface. 
 
Failure detected on port: 
 
LOS – link down detected  
 
Failure detected on MEP: 
 
OAM CFM AIS – alarm indication signal detected 
 
OAM CFM LOC – loss of continuity detected 
 
OAM CFM RDI – remote defect indication detected 
 
OAM CFM Interface status TLV – remote port failure detected 
 
OAM CFM E-LAN failure – LOC has occurred for all the remote MEPs of the MEP. 
ETX-2i Devices 
4. Resiliency and Optimization 
 
Failure detected on ETP 
 
Failure detected in Bidirectional Forwarding Detection (BFD) 
 
Failure detected in TWAMP session (relevant for ETX-2i with VDSL card). This is detected via 
ping to a remote station using ICMP Echo. 75% lost pings in one minute (i.e., unavailable 
minute) indicates an ICMP Echo fail event.  
• 
Action to take when fault propagation is triggered: 
 
Action performed on port: 
 
Deactivate interface. 
 
Action performed on VRRP group: 
 
Decrease VRRP priority. 
 
Action performed on MEP: 
 
Send OAM CFM alarm indication signal to indicate failure OR 
 
Send OAM CFM interface status TLV to indicate failure. 
 
Action performed on queue block Shaper: 
 
Change Shaper rate according to specified shaper-profile. 
 
Action performed on flow Policer: 
 
Change Policer rate according to specified policer-profile. 
 
Action performed on VDSL card (relevant for ETX-2i with VDSL card): 
 
Reset VDSL card. 
• 
Wait-to-restore time – the time period before enabling the shut-down entity or ceasing to send 
OAM CFM interface status once the failed entity has been restored 
• 
Holdoff timer – Action is triggered only if detected fault persists for the amount of time 
configured in the holdoff timer. Holdoff timer enables timing the fault propagation action and 
synchronizing with other network redundancy mechanisms.  
Factory Defaults 
By default, no fault propagation is configured. When you configure fault propagation for a particular 
entity pair, the default configuration is as follows: 
• 
No trigger is defined for fault detection. 
• 
No action is defined to be performed when a fault is detected.  
• 
Holdoff time = 0. Trigger activates fault propagation as soon as it is detected. 
• 
Wait-to-restore time = 0 
ETX-2i Devices 
4. Resiliency and Optimization 
Configuring Fault Propagation 
Follow this procedure to configure fault propagation: 
1. Add a fault propagation entry for a pair of entities. 
2. Configure up to 32 fault propagation rules for the entry: 
a. Specify the trigger(s). 
b. Specify the action. 
c. Define the holdoff timer. 
d. For applicable actions, specify the wait-to-restore time if you do not want the default value 
0. 
Adding Fault Propagation Entry 
 To add fault propagation for a pair of entities: 
1. Navigate to configure fault. 
2. Type the command: 
fault-propagation <from-entity> to <to-entity> and enter the desired entities, as shown below. 
A prompt is displayed: 
config>fault>fault-propagation(<from-entity>/to/<to-entity>)$ 
3. Configure the fault propagation parameters as needed (see Configuring Fault Propagation ). 
From Entity 
To Entity 
Command 
BFD 
VRRP group 
fault-propagation bfd <router>/<interface>ip<ip-address> 
to vrrp <vrid> {ipv4|ipv6} router-interface 
<router>/<interface> 
ETP 
Ethernet port 
fault-propagation etp <etp-name> to 
port ethernet [<slot>/]<port> 
ETP 
 
PCS 
fault-propagation etp <etp-name> to port pcs <port> 
ETP 
Logical MAC 
fault-propagation etp <etp-name> to port logical-
mac <port> 
ETP 
MEP 
fault-propagation etp <etp-name> to 
mep <to-mdid> <to-maid> <to-mepid> 
Ethernet port 
Ethernet port 
fault-propagation port ethernet [<slot>/]port> to 
port ethernet [<slot>/]<port> 
ETX-2i Devices 
4. Resiliency and Optimization 
From Entity 
To Entity 
Command 
Ethernet port 
Logical MAC 
fault-propagation port ethernet [<slot>/]port> to 
port logical-mac <port> 
Ethernet port 
MEP 
fault-propagation port ethernet [<slot>/]port> to 
mep <to-mdid> <to-maid> <to-mepid> 
Ethernet port 
PCS 
fault-propagation port ethernet [<slot>/]port> to 
port pcs <port> 
Ethernet port 
Queue Block 
Shaper 
fault-propagation port ethernet [<slot>/]port> to shaper 
port <eth-port> queue-block <level>/<queue-block> 
Ethernet port  
Policer instance 
fault-propagation port ethernet [<slot>/]port> to policer 
flow <flow-name> 
Ethernet port  
TWAMP 
responder 
fault-propagation port ethernet [<slot>/]port > to twamp-
responder <id> 
LAG port  
Ethernet port 
fault-propagation port lag <port> to port 
ethernet [<slot>/]<port> 
LAG port  
Logical MAC 
fault-propagation port lag <port> to port logical-
mac <port>   
LAG port  
MEP 
fault-propagation port lag <port> to 
mep <to-mdid> <to-maid> <to-mepid> 
LAG port  
PCS port 
fault-propagation port lag <port> to port pcs <port> 
Logical MAC  
Ethernet port 
fault-propagation port logical-mac <port> to port 
ethernet [<slot>/]<port> 
Logical MAC  
Logical MAC 
fault-propagation port logical-mac <port> to port logical-
mac <port>   
Logical MAC  
MEP 
fault-propagation port logical-mac <port> to 
mep <to-mdid> <to-maid> <to-mepid> 
Logical MAC  
PCS port 
fault-propagation port logical-mac <port> to port pcs 
<port> 
MEP 
Ethernet port 
fault-propagation mep <md-id> <ma-id> <mep-id> to 
port ethernet [<slot>/]<port> 
MEP 
Logical MAC 
fault-propagation mep <md-id> <ma-id> <mep-id> to 
port logical-mac <port> 
MEP 
MEP 
fault-propagation mep <md-id> <ma-id> <mep-id> to 
mep <to-mdid> <to-maid> <to-mepid> 
ETX-2i Devices 
4. Resiliency and Optimization 
From Entity 
To Entity 
Command 
MEP 
PCS 
fault-propagation mep <md-id> <ma-id> <mep-id> to 
port pcs <port> 
MEP 
Queue Block 
Shaper 
fault-propagation mep <md-id> <ma-id> <mep-id> to 
shaper port <eth-port> queue-block <level>/<queue-block> 
MEP  
Policer instance 
fault-propagation port mep <md-id> <ma-id> <mep-id> to 
policer flow <flow-name> 
PCS port (only 
with SHDSL 
module) 
Ethernet port 
fault-propagation port pcs <port> to port 
ethernet [<slot>/]<port> 
PCS port (only 
with SHDSL 
module) 
Logical MAC 
fault-propagation port pcs <port> to port logical-
mac <port> 
PCS port (only 
with SHDSL 
module) 
MEP 
fault-propagation port pcs <port> to 
mep <to-mdid> <to-maid> <to-mepid> 
PCS port (only 
with SHDSL 
module) 
PCS port (only 
with SHDSL 
module) 
fault-propagation port pcs <port> to port pcs <port> 
Router interface 
VRRP group 
fault-propagation router-interface <router-
number>/<interface-number> to vrrp <to-vrid> {ipv4|ipv6} 
router-interface <router-number-vrrp>/<interface-number> 
TWAMP session 
Controller 
Card (VDSL) 
fault-propagation twamp-session controller <twamp-
controller> peer <twamp-peer> session-id <twamp-session-
id> to slot <number> 
Ethernet port 
fault-propagation twamp-session controller <twamp-
controller> peer <twamp-peer> session-id <twamp-session-
id> to port ethernet <to-port-index> 
PCS port 
fault-propagation twamp-session controller <twamp-
controller> peer <twamp-peer> session-id <twamp-session-
id> to port pcs <to-port-number> 
Logical MAC  
fault-propagation twamp-session controller <twamp-
controller> peer <twamp-peer> session-id <twamp-session-
id> to port logical-mac <to-port-number> 
MEP 
fault-propagation twamp-session controller <twamp-
controller> peer <twamp-peer> session-id <twamp-session-
id> to mep <to-mdid> <to-maid> <to-mepid> 
ETX-2i Devices 
4. Resiliency and Optimization 
Configuring Fault Propagation Rules 
You can configure up to 32 fault propagation rules for a pair of entities. 
 To configure fault propagation rules: 
1. Navigate to configure fault fault-propagation <from-entity> to <to-entity> to select the fault 
propagation entry to configure. 
A prompt is displayed: 
config>fault>fault-propagation(<from-entity>/to/<to-entity>)# 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying the action 
to take when fault 
propagation is 
triggered 
action-on-group { interface-deactivation | 
oam-cfm-if-status-tlv | oam-cfm-ais| oam-cfm-rdi 
| shaper-swap <shaper-profile> | policer-swap 
<policer-profile> | reset | 
vrrp-priority-decrement <number> | twamp-
deactivation } 
The following actions are supported: 
• interface-deactivation – Deactivate 
interface. 
• oam-cfm-if-status-tlv – Send OAM 
CFM interface status TLV to indicate 
failure.   
• oam-cfm-ais – Send OAM CFM alarm 
indication signal to indicate failure.  
• oam-cfm-rdi – RDI detected 
• shaper-swap – Change Shaper rate 
according to shaper-profile. 
• policer-swap – Change Policer rate 
according to policer-profile. 
• reset – Reset the card. Relevant for 
ETX-2i with VDSL card. 
• vrrp-priority-decrement – Decrease 
VRRP priority.  
• twamp-deactivation – Disable TWAMP 
responder action (Multi-NNI feature) 
Typing no action-on-group removes the 
action.  
Note:  
• The interface-deactivation action is 
allowed only if the to-entity is an 
Ethernet port.  
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
• The oam-cfm-if-status-tlv or oam-cfm-
ais action is allowed only if the to-entity 
is a MEP.  
• The vrrp-priority-decrement action is 
allowed only if the to-entity is a VRRP 
group. 
• The reset action is allowed only for a slot 
destination. 
• The shaper-swap action is relevant only 
for the Queue Block Shaper destination. 
• The policer-swap action is relevant only 
for the flow Policer destination. 
• shaper-swap and policer-swap actions 
are enabled only if you have activated 
the TMFP license for enhanced fault 
propagation features. 
Defining the number 
of milliseconds to 
wait before a trigger 
activates fault 
propagation 
holdoff <milliseconds> 
no holdoff 
Possible values: 0-10,000 milliseconds (10 
seconds) 
0 – default; no holdoff; trigger activates 
fault propagation as soon as it is detected. 
Note:  
• The holdoff time that you configure is 
rounded up or down to a granularity of 
10 ms. This means that if you configure a 
holdoff time with the last digit 1-5, the 
holdoff time is rounded down; and with 
the last digit 6-9, it is rounded up.    
• After you configure the holdoff, you can 
run the info detail command to see the 
actual value.   
Specifying the 
trigger(s)  
trigger { los | interface-up | oam-cfm-loc | 
oam-cfm-rdi | oam-cfm-if-status-tlv | oam-cfm-ais | 
oam-cfm-all-remote-meps-failed | router-interface-
down | bfd-session-down | unavailable }  
The following triggers are supported: 
• los – link down 
• interface-up – link up 
• oam-cfm-loc – LOC detected 
• oam-cfm-rdi – RDI detected 
• oam-cfm-if-status-tlv 
• oam-cfm-ais – AIS detected 
• oam-cfm-all-remote-meps-failed – All 
remote MEPs failed. 
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
• router-interface-down  
• bfd-session-down – Underlying BFD 
session failed. 
• unavailable – TWAMP session is 
unavailable. 
Typing no before the command removes 
the specified trigger. 
Note:  
• The LOS trigger is allowed only if the 
from-entity is an Ethernet port or ETP. 
• The OAM CFM triggers are allowed only 
if the from-entity is a MEP. 
• The Router Interface Down trigger is 
allowed only if the trigger-entity-type is 
a router interface. 
• The BFD Session Down trigger is allowed 
only if the trigger-entity-type is BFD. 
• The Unavailable trigger is allowed only if 
the trigger-entity-type is a TWAMP 
session. 
Specifying the 
wait-to-restore time 
wait-to-restore <seconds> 
Possible values: 0–3600 
Disabling Fault Propagation  
 To disable fault propagation for a pair of entities: 
1. Navigate to configure fault. 
2. Type the command: 
no fault-propagation <from-entity> to <to-entity> to select the entities for which to disable 
fault propagation. 
The specified fault propagation is disabled. 
ETX-2i Devices 
4. Resiliency and Optimization 
Examples 
 To enable fault propagation: 
• 
From Ethernet port 0/3  
• 
To MEP 3 in maintenance association 3 in maintenance domain 2 (this example assumes the 
MEP has been created) 
• 
Trigger: LOS 
• 
Action: Send OAM CFM interface status TLV. 
• 
Wait-to-restore time = 120 seconds 
• 
Holdoff timer = 150 milliseconds 
exit all 
config fault 
fault-propagation port ethernet 0/3 to mep 2 3 3 
  trigger los 
  action-on-group oam-cfm-if-stat 
  wait-to-restore 120 
  holdoff 150 
exit all 
 To display information on the fault propagation configured above: 
ETX-2i# config fault fault-propagation port eth 0/3 to mep 2 3 3 
ETX-2i>config>fault>fault-propagation(port/ethernet/0/3/to/mep/2/3/3)$ info detail 
    action-on-group  oam-cfm-if-status-tlv  
    trigger  los  
    no trigger  oam-cfm-loc  
    no trigger  oam-cfm-if-status-tlv  
    no trigger  oam-cfm-rdi 
    wait-to-restore  120 
    holdoff          150 
 To enable fault propagation: 
• 
From Ethernet port 0/1 
• 
To Ethernet port 0/3 
• 
Trigger: LOS 
• 
Action: Shut down Ethernet port. 
• 
Wait-to-restore time = 90 seconds 
• 
Holdoff time = 320 milliseconds 
ETX-2i Devices 
4. Resiliency and Optimization 
exit all 
config fault fault-prop port ethernet 0/1 to port ethernet 0/3 
  trigger los 
  action interface-deact 
  wait-to-restore 90 
  holdoff 320 
  exit all 
 To display information on the fault propagation configured above: 
ETX-2i# config fault fault-prop port eth 0/1 to port eth 0/3 
ETX-2i>config>fault>fault-propagation(port/ethernet/0/1/to/port/ethernet/0/3)# info detail 
    action-on-group  interface-deactivation  
    trigger  los  
    no trigger  oam-cfm-loc  
    no trigger  oam-cfm-if-status-tlv  
    no trigger  oam-cfm-rdi 
    wait-to-restore  90 
    holdoff 320 
 To enable fault propagation: 
• 
From MEP 1 in maintenance association 1 in maintenance domain 1 (this example assumes the 
MEP has been created)  
• 
To MEP 2 in maintenance association 2 in maintenance domain 1 (this example assumes the 
MEP has been created) 
• 
Trigger: Any OAM CFM error  
• 
Action: Send OAM CFM interface status TLV 
• 
Wait-to-restore time = 300 seconds 
exit all 
config fault 
fault-propagation mep 1 1 1 to mep 1 2 2 
  trigger oam-cfm-loc 
  trigger oam-cfm-rdi 
  trigger oam-cfm-if-status-tl 
  action-on-g oam-cfm-if-stat 
  wait-to-restore 300 
  exit all 
 
 
ETX-2i Devices 
4. Resiliency and Optimization 
 To display information on the fault propagation configured above: 
ETX-2i# config fault fault-propagation mep 1 1 1 to mep 1 2 2 
ETX-2i>config>fault>fault-propagation(mep/1/1/1/to/mep/1/2/2)# info detail 
    action-on-group  oam-cfm-if-status-tlv  
    no trigger  los  
    trigger  oam-cfm-loc  
    trigger  oam-cfm-if-status-tlv  
    trigger  oam-cfm-rdi 
    wait-to-restore  300 
 To enable fault propagation: 
• 
From Ethernet port 0/1 
• 
To Shaper port 0/3 
• 
Trigger: LOS 
• 
Action: Change Shaper rate to 100M. 
• 
Wait-to-restore time = 100 seconds 
exit all 
config fault fault-prop port ethernet 0/1 to shaper port ethernet 0/3 queue-block 0/2  
  wait-to-restore 100 
  trigger los  
  action-on-group shaper-swap rate_100M  
exit all  
 To enable fault propagation: 
• 
From Ethernet port 0/1 
• 
To Policer flow tlv1 
• 
Trigger: LOS 
• 
Action: Change Policer rate to 70M. 
• 
Wait-to-restore time = 100 seconds 
config fault fault-propagation port ethernet 0/1 to policer flow tlv1 
  wait-to-restore 100 
  trigger los  
  action-on-group policer-swap rate_70M 
exit all  

## 4.4 Interface Redundancy  *(p.839)*

ETX-2i Devices 
4. Resiliency and Optimization 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Cannot delete entity while it 
participates in fault propagation 
You tried to delete an entity 
used in fault propagation 
existent configuration. 
 
Fault propagation source does 
not exist 
You tried to configure fault 
propagation with a non-existent 
source. 
 
Fault propagation destination 
does not exist 
You tried to configure fault 
propagation with an existent 
source 20Gbut non-existent 
destination. 
 
Priority decrement fault 
propagation banned on VRRP 
address owner 
You tried to configure a VRRP 
group address owner as a 
to-element.  
Either configure the to-element with a 
different IP address that is not a virtual 
IP address or use a virtual address that is 
not a real address of the to-element. 
VRRP priority preemption must 
be enabled for fault propagation 
You tried to configure a VRRP 
group whose preemption is 
disabled as a to-element. 
Enable preemption for the VRRP group. 
4.4 Interface Redundancy 
Two Ethernet network interfaces can operate in 1:1 bidirectional protection (redundancy) mode. In this 
mode, only one port is active at a time to carry traffic. If it fails, the second port takes over. This 
Ethernet protection is also known as Link protection or Dual Homing. The recovery mode (revertive or 
non-revertive) and the restoration time in revertive mode can be selected according to the application 
requirements. 
ETX-2i can continue to route traffic even if one of the links fails. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products. 
ETX-2i Devices 
4. Resiliency and Optimization 
ETX-2i supports a single instance of dual homing (Ethernet protection). 
Interface redundancy is supported only with interfaces Ethernet 0/1 as primary and Ethernet 0/2 as 
secondary. 
Standards Compliance 
IEEE 802.3ad 
Functional Description 
Link protection offers an alternative to link aggregation if protection without LACP is acceptable. You can 
configure parameters such as revertive/non-revertive mode, the restoration time in revertive mode, 
forcing active link, etc.; however, the switchover time to the standby link is longer than for LAG.  
In 1:1 bidirectional mode, the following topologies can be used: 
• 
Connection of both ports to the same switch/router. 
• 
Connection of the ports to different switch/routers. The main advantage of this topology is its 
higher availability because each port can be routed along a different path through the network. 
This topology is also referred to as dual homing. 
With 1:1 bidirectional redundancy mode, at any time only one of the ports is actively carrying traffic, 
and the other port serves as the backup port. A RAD proprietary redundancy algorithm, based on loss of 
Ethernet signal, is used to detect line failure. The protection switching (flipping) time is less than 
1 second. It also depends on the network “relearning” time or aging. 
The recovery mode after protection switching can be selected in accordance with the application 
requirements: 
• 
Non-revertive mode – ETX-2i does not automatically flip back after the failed port returns to 
normal operation, but only when the currently used port fails, or after a manual flip command. 
• 
Revertive mode – ETX-2i flips back to the original port when it returns to normal operation. 
Flipping back can be delayed by specifying a restoration time, during which alarms are ignored. 
As a result, ETX-2i starts evaluating the criteria for protection switching (flipping) only after the 
restoration time expires, thereby ensuring that another flip cannot occur before the specified 
time expires. 
ETX-2i Devices 
4. Resiliency and Optimization 
Factory Defaults 
By default, bidirectional redundancy is not enabled. 
Configuring Link Protection 
Configuring 1:1 protection requires defining an Ethernet group. 
 To configure link protection: 
1. Define an Ethernet group: At the Protection context (config>protection), enter: 
ethernet-group <group-id> 
The system switches to the context of the specified Ethernet group 
(config>protection>eth-group(<group-id>)). 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Defining operation mode 
oper-mode { 1-to-1 | manual } 
 
Defining port recovery mode as 
revertive 
[no] revertive 
Traffic is switched back to the 
primary port after it recovers. 
no revertive sets the port 
recovery mode to non-revertive. 
Traffic continues being 
transmitted over the secondary 
port after the primary port 
recovers. 
Displaying protection group 
status 
show status 
 
Setting the time between 
recovery and resumption of 
transmission 
wait-to-restore <seconds> 
The primary port resumes 
transmitting traffic once the link 
has been restored and the 
specified time has elapsed. 
Possible values: 0-720 seconds 
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
Forcing port to transmit 
force-active-port ethernet 
[<slot>/]<port> 
Relevant for manual mode only. 
The specified port is set to be 
active. You can choose the 
primary port (1) or the 
secondary port (2).  
Port 1. Port 1 is configured as a 
permanently active link. Even if 
port 1 fails, the traffic is not 
switched to the standby port. 
Port 2. Port 2 is configured as a 
permanently active link. Even if 
port 2 fails, the traffic is not 
switched to the standby port. 
no force-active-port specifies 
that neither of the ports is 
forced to remain active. 
Adding/removing protection 
and working ports to the 
protection group 
bind ethernet [primary [<slot>/]<port>] 
[secondary [<slot>/]<port>] 
no bind ethernet primary 
no bind ethernet secondary 
In manual mode, bind/remove 
primary ports only. 
In 1-to-1 mode, bind/remove 
primary and/or secondary ports. 
Setting the time that the failed 
link pauses transmission to 
report failure 
tx-down-duration-upon-flip <seconds> 
Relevant for manual mode only. 
The secondary port resumes 
transmitting after the specified 
‘reporting’ time. This function is 
useful if there is no auto-
negotiation between the link 
endpoints. 
Possible values: 0-30  
 
 

## 4.5 Link Aggregation (LAG)  *(p.843)*

ETX-2i Devices 
4. Resiliency and Optimization 
Example 
 To define link protection: 
• 
Ethernet group 1 
• 
Protection port – Ethernet port 1/1  
• 
Working port – Ethernet port 1/2 
• 
Operation mode – One-to-one 
exit all 
configure protection ethernet-group 1 
bind eth primary 1/1 secondary 1/2 
oper-mode 1-to-1 
exit all 
 To display configuration information for the link protection: 
ETX-2i#configure protection ethernet-group 1 
ETX-2i>config>protection>eth-group(1)# info detail 
    bind  ethernet primary  1/1 secondary  1/2 
    oper-mode  1-to-1 
    revertive 
    wait-to-restore  0 
    tx-down-duration-upon-flip  0 
    no shutdown 
4.5 Link Aggregation (LAG) 
In link aggregation (LAG) mode according to IEEE 802.3ad, Ethernet interfaces can be aggregated into a 
single logical link for protection or load balancing. This means that ETX-2i can continue to route traffic 
even if one of the links fails. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products, with the following conditions: 
• 
Ethernet 10GbE ports are relevant only to ETX-2i-10G (half and full 19-inch), ETX-2i-10G-B/8SFPP 
(half and full 19-inch), and ETX-2i-100G. 
• 
Ethernet 100GbE ports are relevant only to ETX-2i-100G. 
ETX-2i Devices 
4. Resiliency and Optimization 
• 
LAG is supported with or without LACP (user-configurable), with 50ms LAG switchover time.  
• 
A LAG can function in protection or load-balancing mode.  
• 
All load balancing LAGs should use the same distribution method. 
• 
Protection LAGs can have up to two members (ports), and load-balancing LAG groups can have 
up to four members (ports). 
• 
A protection LAG can be made up of one or two adjacent network ports or user ports and not 
both types. 
• 
A LAG can include ports of the same speed only (1G, 10G, or 100G). 
• 
A LAG cannot be used as PTP Master port. 
• 
A load-balancing LAG group can comprise up to four members from specified ports. The ports do 
not have to be adjacent. 
Exception: In ETX-2i-100G/4QSFP, the LAG group of 100G ports can include only two ports (3/1 
and 3/2). 
• 
ETX-2i supports up to four LAG groups (protection and load-balancing).  
• 
ETX-2i-B supports up to three LAG groups (protection and load-balancing).  
• 
ETX-2i-10G half 19-inch supports up to six LAG groups (protection and load-balancing). 
 
Members in a protection LAG group can be: 1 and 2, 3 and 4, 5 and 6, 7 and 8, 9 and 10, or 
11 and 12. 
 
Members in a load-balancing LAG group can include ports from one of the following groups: 
(A single LAG group cannot contain some ports from one group and other ports from 
another group.) 
 
1, 2 
 
3-8 (if 3, 4 are 10GbE, LAG can be supported only between the two.) 
 
9-12 
• 
ETX-2i-10G full 19-inch supports up to 14 LAG groups (protection and load-balancing): 
 
Members in a protection LAG group can be: 1 and 2, 3 and 4, 5 and 6, 7 and 8, 9 and 10, 11 
and 12, …, or 27 and 28. 
 
Members in a load-balancing LAG group can include ports from one of the following groups: 
(A single LAG group cannot contain some ports from one group and other ports from 
another group.) 
 
1, 2 
 
3-16  
 
17-28  
ETX-2i Devices 
4. Resiliency and Optimization 
• 
ETX-2i-10G-B/8SFPP (half and full models) supports up to six LAG groups. LAG group members 
must be from the same port group: 
 
ETH1 – ETH4 
 
ETH5 – ETH8 
• 
ETX-2i-100G/4QSFP supports up to ten LAG groups (protection and load-balancing). 
 
LAG (protection and load-balancing) is supported between ports from the same port group: 
 
Port Group 1 - 100G ports 3/1 and 3/2. (100G ports 3/3 and 3/4 cannot be included in 
this LAG group.) 
 
Port Group 2 – all other ports 
 
Protection LAG group is supported with up to two adjacent 10G/100G ports: 
 
1/1-1/2, 1/3-1/4, 1/5-1/6, 1/7-1/8 
 
2/1-2/2, 2/3-2/4, 2/5-2/6, 2/7-2/8 
 
3/1-3/2, 3/3-3/4 
Standards Compliance 
IEEE 802.3ad 
Functional Description 
All LAG ports receive traffic at the same time and one port transmits. The LAG members can be network 
or user interfaces and must be connected to the same switch/router. If LACP is activated, then LACP 
control frames are periodically transmitted in order to locate failures as they occur. 
You can configure an anchor port for a LAG group, which you can use to configure flows to/from the LAG 
group. The default anchor port is the first port bound to the LAG group. The MAC address of the anchor 
port is used for logical port level entities (router interface over the LAG, OAM MEP over the LAG, etc.). 
Fat Pipe Detection 
You can perform Fat pipe detection on a LAG port of a device (ETX-2i-10G half 19-inch,  
ETX-2i-10G-B (half and full 19-inch), ETX-2i-10G-B/8SFPP, and ETX-2i-100G/4QSFP), by binding a Fat pipe 
detection profile to the LAG anchor port. For detailed information, refer to Fat Pipe Detection in the 
Traffic Processing Chapter and Ethernet Ports in the Cards and Ports chapter.  
ETX-2i Devices 
4. Resiliency and Optimization 
Protection 
If the transmitting port fails, ETX-2i switches to a standby link. The equipment connected to the Ethernet 
ports must use compatible switching criteria for redundancy to be available: 
• 
For networks using Layer 2 switching – The criterion is signal loss. 
• 
For networks using Layer-3 routing – The router must support IEEE 802.3ad or other link 
aggregation protocol that views the aggregated link as a single logical interface.    
Using link aggregation inherently provides redundancy, because if a port fails, another port can continue 
transferring traffic. Failure of a link is detected by sensing the loss of valid signals or receiving a failure 
report via Link Aggregation Control Protocol (LACP) if applicable, in which case all traffic is sent through 
the other link. 
Load Balancing 
In a load balancing LAG group, traffic is distributed to the different ports according to the configured 
distribution method. You can configure the following distribution methods: 
• 
MAC source address  
• 
MAC destination address 
• 
MAC source address and MAC destination address 
• 
IP source address 
• 
IP destination address 
• 
IP source address and IP destination address 
• 
MAC source/destination address and IP source/destination address 
For distribution method based on IP address, all non-IP packets are forwarded on the same port. For 
distribution method based on MAC source/destination address + IP source/destination address, fallback 
for non-IP packets is based on MAC address info. 
Note 
All load balancing LAG groups in the device must use the same distribution 
method.  
The load balancing and distribution is performed after the queuing mechanism. The port Policer is 
supported at the port level, not on LAG aggregate ingress traffic. For ETX-2i-10G, aggregate LAG egress 
traffic can be shaped at the LAG level up to a maximum of 20 Gbps, which means that the level 1 Shaper 
is supported for rates up to 20 Gbps. For ETX-2i-100G, aggregate LAG egress traffic can be shaped (LAG 
level) up to a maximum of 100Gbps, which means that the level 1 Shaper is supported for rates up to 
100 Gbps. 
ETX-2i Devices 
4. Resiliency and Optimization 
You can configure the minimum number of active ports in the LAG for it to be considered operationally 
active. A port is considered as active if it has no physical layer failure and LACP is synched (if LACP is 
enabled). 
If there are flows over the anchor port when the LAG group is created and enabled, the flows are 
inherited by the LAG group. The LAG group can be administratively enabled if flows exist over the 
anchor port, but not if flows exist over a non-anchor port. If the LAG group is deleted or administratively 
disabled, the flows and traffic remain on the anchor port; they are not distributed to other ports. 
PTP and SyncE 
SyncE and 8275.1 PTP relate to a physical port and have no relation to the logical LAG level. Thus, SyncE 
and 8275.1 PTP are configured over each one of the physical ports and not over the logical LAG interface 
(anchor port. 
For SyncE configuration, the CSM source can be any of the physical ports of the LAG group (one or 
more).  
G.2875.1 PTP configuration over a physical port that is a member in a LAG group is done differently than 
a physical port that is not a LAG member. 
You can configure a physical port, which is a LAG member, with G.2875.1 PTP, as follows:  
1. Configure an SVI for the LAG port and then enable the SVI (refer to Service Virtual Interfaces 
(SVIs) in the Cards and Ports chapter). 
2. For the LAG port, classify flows for PTP traffic, using Port Classification with PTP EtherType 
0x88f7 as a classifier (refer to Classification by Port/Flow in the Traffic Processing chapter). 
3. Bind the PTP flows to the SVI that you configured in step 1 (refer to Classification by Port/Flow 
in the Traffic Processing chapter). 
SVI 1
Port Classifier 
EtherType 0x88F7 
to Flow A
LAG
G.8275.1 
PTP Port
Port Classifier 
EtherType 0x88F7 
to Flow B
Flow A
Flow B
 
ETX-2i Devices 
4. Resiliency and Optimization 
Factory Defaults 
By default, no LAG groups are configured. When a LAG group is created, it has the following default 
configuration. 
 
Parameter 
Default  
Remarks 
giga-ethernet  
LAG admin key is GbE port 
anchor-port 
no anchor-port 
distribution-method  
one-to-one 
mo 
lacp 
no lacp 
LACP not enabled 
mode 
redundancy 
LAG is protection LAG 
shutdown 
shutdown 
Administratively disabled 
If the mode is changed to load-balance, the default configuration is as shown below. 
Parameter 
Default  
Remarks 
admin-key 
giga-ethernet  
LAG admin key is GbE port 
anchor-port 
no anchor-port 
distribution-method  
src-ip 
Packets distributed according to source IP address 
lacp 
no lacp 
LACP not enabled 
minimum-link-number 
1 
One LAG port must be active  
mode 
load-balance 
LAG is load balancing LAG 
shutdown 
shutdown 
Administratively disabled 
Configuring LAG 
This section explains how to define a link aggregation group (LAG) and enable link aggregation control 
protocol (LACP). 
ETX-2i Devices 
4. Resiliency and Optimization 
Note 
• 
In order to enable LACP for the LAG, at least one port must be already 
bound to the LAG. 
• 
In order for LACP to function, the ports bound to the LAG must be 
associated with an L2CP profile that specifies peer action for MAC 0x02. 
• 
In a load-balancing LAG, all non-anchor ports bound to the LAG must not 
be associated with a queue group profile (use command no queue-group).  
 To configure LAG: 
1. Navigate to configure port lag <num>. 
The config>port>lag(<num>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Assigning an admin key to the 
LAG to indicate the port speed 
admin-key {fast-ethernet | giga-ethernet 
| ten-giga-ethernet | 
hundred-giga-ethernet } 
You must define admin-key 
before binding ports to the LAG. 
Defining the LAG anchor port 
anchor-port ethernet  
[<slot>/] port-num> 
anchor-port logical-mac <port-number> 
 
Adding a port to the LAG 
bind ethernet [<slot>/]<port-num> 
bind logical-mac <port-num> 
Bind to the LAG port an 
Ethernet port with a higher port 
number than that of the anchor 
port. This ensures that a ping to 
a neighboring IP address 
succeeds.  
Entering no bind removes a link 
from the LAG. 
Clearing LACP statistics 
clear-lacp-statistics 
 
Clearing LAG statistics 
clear-statistics 
 
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
Configuring port to trust DHCP 
packets sent from server 
dhcp-trust 
Client ports must always be 
untrusted (no dhcp-trust); 
otherwise, the DHCP relay 
discards the discovery messages 
sent from the client port to the 
server. 
Relevant only if DHCP snooping 
is enabled (refer to DHCP Relay 
in the Management and Security 
chapter). 
Assigning method of 
distributing traffic within LAG 
distribution-method { src-mac | dest-mac 
| src-and-dest-mac | src-ip | dest-ip | 
src-dest-mac-ip | one-to-one |  
src-dest-ip } 
src-mac – Packets are 
distributed according to their 
source MAC addresses. 
dest-mac – Packets are 
distributed according to their 
destination MAC addresses. 
src-and-dest-mac – Packets are 
distributed according to their 
source and destination MAC 
addresses. 
src-ip – Packets are distributed 
according to their source IP 
addresses. 
dest-ip – Packets are distributed 
according to their destination IP 
addresses 
src-dest-mac-ip – Packets are 
distributed according to their 
source and destination MAC and 
IP addresses. 
one-to-one – Packets are sent 
only through the active link. 
src-dest-ip – Packets are 
distributed according to their 
source and destination IP 
addresses. 
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
Note: The one-to-one 
parameter is relevant only for 
redundancy LAG; the other 
parameters are relevant only for 
load balancing LAG. 
 
Enabling LACP and setting LACP 
parameters  
lacp [tx-activity { active | passive }] 
[tx-speed { slow | fast }] [sys-priority 
<sys-priority>] 
tx-activity – Defines operation 
mode: 
• active – LAG interface 
periodically transmits LACP 
frames (LACPDUs) to all links 
with LACP enabled.  
• passive – LAG interface does 
not initiate the LACP 
exchange but replies to 
received LACPDUs. 
tx-speed – Defines time to wait 
before sending LACP frames: 
• fast – three seconds 
• slow – 30 seconds 
sys-priority – determines 
aggregation precedence. If there 
are two partner devices 
competing for the same LAG, 
LACP compares the priorities for 
each grouping of ports. The LAG 
with the lower priority is given 
precedence. 
Possible values: 0–65535 
Defaults: 
• If you type lacp without 
specifying tx-activity, it is set 
to passive. 
• If you type lacp without 
specifying tx-speed, it is set 
to slow. 
• If you type lacp without 
specifying sys-priority, it is 
set to 32768. 
 
ETX-2i Devices 
4. Resiliency and Optimization 
Task 
Command 
Comments 
Note: 
• To enable LACP for LAG, at 
least one port must be 
already bound to LAG. 
• Typing no lacp disables LACP 
protocol. 
Configuring LLDP parameters 
lldp 
Refer to Link Layer Discovery 
Protocol (LLDP) in the Traffic 
Processing chapter for details. 
Defining the minimum number 
of links required for load 
balancing LAG 
minimum-link-number <number> 
Range is 1 to maximum number 
of LAG members. 
If less links than the configured 
minimum number of links 
function properly, LAG failure is 
reported. 
Specifying if LAG is for 
redundancy or load balancing 
mode { redundancy | load-balance } 
 
Assigning a name to a LAG 
name <lag-name> 
lag-name – Name assigned to 
the LAG 
Possible values: 1-64 characters 
Default: LAG 1, LAG 2, etc. 
Administratively enabling LAG 
no shutdown 
Using shutdown disables the 
LAG. 
Displaying bind status 
show bind 
 
Displaying LACP statistics 
show lacp-statistics ethernet 
[<slot>/]<port-id> 
 
Displaying LACP status 
show lacp-status ethernet 
[<slot>/]<port-id> 
 
Displaying LAG level statistics 
show statistics running 
See Viewing LAG Statistics. 
Displaying LAG status 
show status 
See Viewing LAG Status. 
 
 
ETX-2i Devices 
4. Resiliency and Optimization 
Viewing LAG Status 
You can display the LAG status, including the information specified below.  
 To display the LAG status: 
• 
At the prompt config>port>lag(<num>)#, enter: 
show status 
ETX-2i# configure port lag 1 
ETX-2i>config>port>lag(1)# show status 
 
Group 
--------------------------------------------------------------- 
Name : LAG 1 
 
Group 
--------------------------------------------------------------- 
Administrative Status : Up 
Operation Status      : Up 
Mode                  : Redundancy 
Speed                 : 1Gbps 
MAC Address           : 00-20-D2-50-C0-D3 
 
Links 
--------------------------------------------------------------- 
Port      Admin   Oper            LACP      Redundancy 
--------------------------------------------------------------- 
0/1         Up      Up              Sync      Active 
0/2         Up      Up              Sync      Active 
 
Parameter 
Description 
Group 
Name 
Displays name assigned to LAG 
Administrative Status 
Indicates if LAG is administratively enabled or disabled: Up or Down 
Operational Status 
Indicates if LAG is operational:  
Up – LAG is operational. 
Down – LAG is not operational, for reason such as being administratively 
disabled, or link shut down for Fault propagation. 
LLD (all links down) – Both protection LAG ports are down, in case of 
protection LAG). 
LLD (minimum links down) – Minimum links are down, in case of load 
balancing LAG. 
 
ETX-2i Devices 
4. Resiliency and Optimization 
Parameter 
Description 
Mode 
Displays LAG mode: Redundancy or Load Balance 
Speed 
Indicates LAG speed as one of the following, according to X (port speed in 
case of protection LAG, or number of active links × link rate in case of load 
balancing LAG): 
• X >=1 Gbps – Speed indicated as X Gbps 
• 0 < X < 1 Gbps – Speed indicated as X Mbps 
• X = 0 – Speed indicated as Not Applicable 
MAC Address 
Displays MAC address of LAG 
Links 
Information displayed only if LAG is Up. 
Port  
Displays port number of link 
Admin 
Indicates if link is administratively enabled or disabled: Up or Down 
Oper 
Indicates if link is operational: Up or Down 
LACP 
Indicates if LACP is synchronized 
Redundancy 
Indicates if redundancy is active 
Viewing LAG Statistics 
You can display statistics for a LAG port.  
 
Note 
Aggregated statistics do not reflect the counters of all ports at the same 
moment. Some deviation may occur. 
 To display LAG statistics: 
• 
At the prompt config>port>lag(<num>)#, enter: 
show statistics running 
ETX-2i# configure port lag 1 
ETX-2i>config>port>lag(1)# show statistics running 
Running 
----------------------------------------------------------------------------- 
Counter                    Rx                   Tx 
Total Frames               1148154870201        57243227028 
Total Octets               146963822937728      7327133044352 
Total Frames/Sec           17283900             864195 
Total Bits/Sec (L1)        20248980056          1023207655 
ETX-2i Devices 
4. Resiliency and Optimization 
Minimum Bits/Sec (L1)      20004876824          1002055448 
Maximum Bits/Sec (L1)      21254299840          1008226232 
Total Bits/Sec (L2)        17483555814          884936354 
Minimum Bits/Sec (L2)      17213013624          860798488 
Maximum Bits/Sec (L2)      17392648320          868944312 
Unicast Frames             1148154866859        57243226949 
Multicast Frames           0                    0 
Broadcast Frames           0                    0 
 
CRC Errors                 0                    -- 
Error Frames               0                    -- 
L2CP Discarded             0                    -- 
OAM Discarded              0                    -- 
Unknown Protocol Discarded 0                    -- 
CRC Errors/Sec             0                    -- 
Jabber Errors              0                    -- 
Oversize Frames            0                    0 
Unmapped Cos Frames        0                    -- 
MTU Discarded              --                   0 
MTU Discarded Flow         --                   -- 
 
64 Octets                  0                    0 
65-127 Octets              0                    0 
128-255 Octets             1148189977055        57244982407 
256-511 Octets             0                    0 
512-1023 Octets            0                    0 
1024-1518 Octets           0                    0 
1519-2047 Octets           0                    0 
2048-Max Octets            0                    0 
 
 
Rate of Total 
----------------------------------------------------------------------------- 
Port                Rx Total Frames     Tx Total Frames 
                    (%)                 (%) 
----------------------------------------------------------------------------- 
0/1                 50.00               100.00 
0/2                 50.00               0.00 
For parameter descriptions, refer to Viewing Ethernet Port Statistics in the Cards and Ports chapter.  
ETX-2i Devices 
4. Resiliency and Optimization 
Examples 
Protection LAG 
 To define LAG: 
• 
L2CP profile mac2peer, with MAC 0x02 set to peer action 
• 
LAG members – Ethernet ports 0/1 and 0/2 
• 
LACP operation mode – active  
• 
Distribution method – one to one 
• 
System priority –32768 
#****************Create L2CP profile mac2peer 
exit all 
configure port l2cp-profile mac2peer 
mac 0x02 peer 
exit 
 
#****************Assign L2CP profile mac2peer to network ports 
eth 0/1 l2cp profile mac2peer 
eth 0/2 l2cp profile mac2peer 
 
#****************Configure LAG 1 
lag 1 
bind ethernet 0/1 
bind ethernet 0/2 
lacp tx-activity active tx-speed slow sys-priority 32768   
distribution-method one-to-one 
no shutdown 
exit all 
 To display LACP status: 
ETX-2i#configure port lag 1 
ETX-2i>config>port>lag(1)# show lacp-status eth 0/1 
Ports  
----------------------------------------------------------- 
                  Actor                Partner 
Port Number     : 1                    1 
Port Priority   : 32768                0 
System ID       : 0020D250E70A         0020D2F5AD58 
System Priority : 32768                32768 
Operational Key : 2                    32 
Activity        : Active               Active 
Timeout         : Long                 Long 
Synchronized    : Yes                  No 
ETX-2i Devices 
4. Resiliency and Optimization 
Collecting      : No                   No 
Distributing    : No                   No 
 To display LACP statistics: 
ETX-2i#configure port lag 1 
ETX-2i>config>port>lag(1)# show lacp-statistics ethernet 0/1 
LACP 
--------------------------------------------------------------- 
Rx LACP Frames            : 3221 
Rx Marker Frames          : 0 
Rx Unknown Frames         : 0 
Rx Illegal Frames         : 0 
Tx LACP Frames            : 5783 
Tx Marker response Frames : 0 
 To display the status of a protection LAG with all links down: 
ETX-2i# configure port lag 1 
ETX-2i>config>port>lag(1)# show status 
 
Group 
--------------------------------------------------------------- 
Name : LAG 1 
 
Group 
--------------------------------------------------------------- 
Administrative Status : Up 
Operational Status    : LLD (all links down) 
Mode                  : Redundancy 
Speed                 : Not Applicable 
MAC Address           : 00-20-D2-50-C0-D3 
 
Links 
--------------------------------------------------------------- 
Port      Admin   Oper            LACP      Redundancy 
--------------------------------------------------------------- 
0/1         Up      Down            Not Sync  Active 
0/2         Up      Down            Not Sync  Active 
 
 
ETX-2i Devices 
4. Resiliency and Optimization 
Load Balancing LAG 
 To define load balancing LAGs: 
• 
L2CP profile mac2peer, with MAC 0x02 set to peer action 
• 
LAG members: 
 
LAG 1: – GbE ports 0/3 to 0/6 
 
LAG 2: – GbE ports 0/7 to 0/8. 
• 
LACP operation mode – active  
• 
Distribution method – Destination MAC address 
• 
Flows: 
 
Flows for LAG 1 – between GbE 0/1 and 0/3, VLAN 100 
 
Flows for LAG 2 – between GbE 0/1 and 0/7, VLAN 200 
exit all 
#***********Configure L2CP profile 
configure port l2cp-profile mac2peer 
    mac 0x02 peer 
    exit  
 
#***********Associate ports with the L2CP profile 
#***********Specify no queue group profile for non-anchor ports 
    ethernet 0/3 
      l2cp profile mac2peer 
      no shutdown 
      exit 
 
    ethernet 0/4 
      l2cp profile mac2peer 
      no queue-group 
      no shutdown 
      exit 
 
    ethernet 0/5 
      l2cp profile mac2peer 
      no queue-group 
      no shutdown 
      exit 
 
    ethernet 0/6 
      l2cp profile mac2peer 
      no queue-group 
      no shutdown 
      exit 
 
 
ETX-2i Devices 
4. Resiliency and Optimization 
    ethernet 0/7 
      l2cp profile mac2peer 
      no shutdown 
      exit 
 
    ethernet 0/8 
      l2cp profile mac2peer 
      no queue-group 
      no shutdown 
      exit 
 
 
 
#***********Configure LAGs 
    lag 1 
      mode load-balance 
      distribution-method dest-mac 
      admin-key giga-ethernet 
      bind ethernet 0/3 
      bind ethernet 0/4 
      bind ethernet 5 
      bind ethernet 6 
      lacp tx-activity active tx-speed fast 
      anchor-port ethernet 0/3 
      no shutdown 
      exit 
 
    lag 2 
      mode load-balance 
      distribution-method dest-mac 
      admin-key giga-ethernet 
      bind ethernet 0/7 
      bind ethernet 0/8 
 
      lacp tx-activity active tx-speed fast 
      anchor-port ethernet 0/7 
      no shutdown 
      exit 
 
 
 
#***********Configure classification profiles for flows 
    exit 
  flows 
    classifier-profile vlan100 match-any match vlan 100 
    classifier-profile vlan200 match-any match vlan 200 
 
    exit 
 
#***********Configure flow for LAG 1  
    flow lag1_1_to_3  
      classifier vlan100 
ETX-2i Devices 
4. Resiliency and Optimization 
      no policer 
      ingress-port ethernet 0/1 
      egress-port ethernet 0/3 queue 0 block 0/1 
      no shutdown 
      exit 
 
    flow lag1_3_to_1 
      classifier vlan100 
      no policer 
      ingress-port ethernet 0/3 
      egress-port ethernet 0/1 queue 0 block 0/1 
      no shutdown 
      exit  
 
#***********Configure flow for LAG 2  
    flow lag2_1_to_7  
      classifier vlan200 
      no policer 
      ingress-port ethernet 0/1 
      egress-port ethernet 0/7 queue 0 block 0/1 
      no shutdown 
      exit 
 
    flow lag2_7_to_1 
      classifier vlan200 
      no policer 
      ingress-port ethernet 0/7 
      egress-port ethernet 0/1 queue 0 block 0/1 
      no shutdown 
 
 
 
      exit all 
save 
 To display LACP status: 
ETX-2i#configure port lag 1 
ETX-2i>config>port>lag(1)# show lacp-status ethernet 0/3 
Ports  
----------------------------------------------------------- 
                  Actor                Partner              
Port Number     : 3                    3 
Port Priority   : 32768                0 
System ID       : 0020D2EE5ED8         0020D2EE62E1 
System Priority : 32768                0 
Operational Key : 2                    31 
Activity        : Active               Active 
Timeout         : Short                Short 
Synchronized    : Yes                  Yes 
Collecting      : Yes                  Yes 
Distributing    : Yes                  Yes 
ETX-2i Devices 
4. Resiliency and Optimization 
 To display LACP statistics: 
ETX-2i#configure port lag 1 
ETX-2i>config>port>lag(1)# show lacp-statistics ethernet 0/3 
LACP 
--------------------------------------------------------------- 
Rx LACP Frames            : 386                    
Rx Marker Frames          : 0                    
Rx Unknown Frames         : 0                    
Rx Illegal Frames         : 0                    
Tx LACP Frames            : 386                    
Tx Marker response Frames : 0                    
 To display LAG status: 
ETX-2i#configure port lag 1 
ETX-2i>config>port>lag(1)# show status 
Group 
--------------------------------------------------------------- 
Administrative Status: Up 
Operation Status     : Up 
MAC Address          : 00-20-D2-EE-5E-D8 
 
Links 
--------------------------------------------------------------- 
Port Admin  
Oper 
LACP 
 
Redundancy 
--------------------------------------------------------------- 
0/3 
Up 
 
Up 
Sync 
 
Active 
0/4 
Up 
 
Up 
Sync 
 
Active 
0/5 
Up 
 
Up 
Sync 
 
Active 
0/6 
Up 
 
Up 
Sync 
 
Active 
 To display LAG statistics: 
ETX-2i#configure port lag 1 
ETX-2i>config>port>lag(1)# show statistics running 
Rate of Total 
--------------------------------------------------------------- 
Port Rx Total Frames 
Tx Total Frames 
 
(%) 
 
 
(%) 
--------------------------------------------------------------- 
03 
25.00  
 
25.00 
04 
25.00  
 
25.00 
05 
25.00  
 
25.00 
06 
25.00  
 
25.00 
 
 
ETX-2i Devices 
4. Resiliency and Optimization 
 To display the status of a load balancing LAG with minimum links down: 
ETX-2i# configure port lag 1 
ETX-2i>config>port>lag(1)# show status 
 
Group 
--------------------------------------------------------------- 
Administrative Status : Up 
Operational Status    : LLD (minimum links down) 
Mode                  : Load Balance 
Speed                 : Not Applicable 
MAC Address           : 00-20-D2-EE-41-C1 
 
Links 
--------------------------------------------------------------- 
Port      Admin   Oper            LACP      Redundancy 
--------------------------------------------------------------- 
01       Up      Down            Not Sync  Active 
02       Up      Down            Not Sync  Active 
G.8275.1 PTP over LAG 
#####  G.8275.1 PTP over LAG ######## 
#####  SVI config ######## 
configure port 
 
svi 1 name "SVI_PTP_Slave_1" 
 
svi 1 no shutdown 
 
#####  To classify flows for the PTP traffic: define by Port Classifier ######## 
#####  This configuration is per port not LAG, each port in the LAG is an independant entity 
(slave/master/none)regarding PTP ######## 
 
con port eth 0/3 classifier 
match ether-type 0x88f7 to-flow "ptptosvi1"  ///  
exit all 
 
#####  configure PTP flows to PTP SVIs ######## 
con flow 
flow "ptptosv1" port-classifier 
egress-port svi 1 
no shut 
 
flow "svi1toptp" 
classifier all 
ingress-port svi 1 
egress-port ethernet 0/3 queue 1 block 0/1 
no shut 
exit 
 