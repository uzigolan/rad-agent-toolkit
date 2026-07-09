# Feature Reference – 8 Monitoring and Diagnostics – 8.2 OAM CFM (Connectivity Fault Management)

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1285–1367.*


## Viewing In-Service ICMP Echo Ping Test Status  *(p.1285)*


## Applicability and Scaling  *(p.1285)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing In-Service ICMP Echo Ping Test Status 
You can view the status of an in-service ICMP Echo Ping test. 
 To display the status of an in-service ICMP Echo Ping test: 
• 
In the config>flows# prompt, enter  
show service-ping. 
The status report appears. For information on the parameters, see the table in In-Service Ping 
Parameters. 
8.2 OAM CFM (Connectivity Fault Management) 
Ethernet OAM (Operation, Administration, and Maintenance) functions provide end-to-end connectivity 
checks and performance monitoring. 
Ethernet Connectivity Fault Management (CFM) is a service-level OAM protocol that provides tools for 
monitoring and troubleshooting end-to-end Ethernet services. This includes proactive connectivity 
monitoring, fault verification, and fault isolation. CFM uses standard Ethernet frames and can be run on 
any physical media that is capable of transporting Ethernet service frames. ETX‑2 also supports 
performance monitoring per Y.1731. 
Ethernet service providers can monitor their services proactively and guarantee that customers receive 
the contracted SLA. Fault monitoring and end to end performance measurement provide tools for 
monitoring frame delay, frame delay variation, and frame loss and availability. 
The device’s can act as a Maintenance Entity Group Intermediate Point (MIP) or Maintenance Entity 
Group End Point (MEP). When ETX‑2 acts as a MIP, it forwards OAM CFM messages transparently, 
responding only to OAM link trace (LTM) and unicast OAM loopback (LBM). 
Applicability and Scaling 
This feature is applicable to all ETX-2i products, with the following conditions: 
• 
Dimensioning differs between the products; this is indicated where relevant. 
• 
Automatic remote MEP learning is supported for 1 Sec CCM and 10 Sec CCM; not for 3.33 ms 
CCM period.  
• 
The ETX MEP service level configuration supports p-bit agnostic mode (used in flow tracking). 

## Standards  *(p.1286)*


## Functional Description  *(p.1286)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Standards 
IEEE 802.1ag-D8 
ITU-T Y.1731 
MEF 36 
Functional Description 
OAM CFM monitors networks by defining device ports within the network as part of a maintenance 
domain and monitoring specialized frames that are added to the data sent to, from or through those 
ports.  
ETX-2i devices can be configured to be part of a maintenance domain and to support the various 
functions required of a participant in such a domain. 
ETX‑2i devices provide the OAM CFM functions listed below in packet-switched networks: 
• 
End-to-end Connectivity Fault Management (CFM) per IEEE 802.1ag (also described in Y.1731): 
 
Continuity check (ETH-CC) 
 
Loopback (ETH-LB) 
 
Link trace for fault localization (ETH-LT)  
• 
End-to-end service and performance monitoring per ITU-T Y.1731 
 
Loss measurement (single-ended ETH-LM) 
 
Delay measurement (two-way ETH-DM). 
OAM CFM enables detection of network faults and distribution of fault-related information. OAM can 
also be used for measurement of network performance monitoring (OAM PM), to ensure that network 
operators comply with QoS guarantees, detect anomalies before they escalate, and isolate and bypass 
network defects. As a result, the operators can offer binding service-level agreements. 
OAM CFM Frame Types  
OAM network monitoring relies on dedicated OAM frame types as per 802.1ag and Y.1731.  
The following types of frames are used:  
Note 
Performance Management (defined in Y.1731) uses additional message types.  
ETX-2i Devices 
8. Monitoring and Diagnostics 
• 
CCM (continuity check message) – CCM frames are sent regularly at a configurable interval 
(from 3.33ms to 10 minutes) and are sent from MEPs (maintenance end points) to remote 
connected MEPs.  Transmission is multicast (one to many). 
o RDI (remote defect indicator) – NOT a frame, but an indicator set inside the CCM that 
notifies connected MEPs that a defect was detected.  
 
If an MEP stops receiving CCMs from a specific MEP (for a 3 CCM period), it 
changes its state to LOC (loss of continuity) and the RDI indicator in the CCMs it 
sends is set to a RDI defect until the Rx CCMs resume.  
Depending on configuration, an AIS frame may be sent downstream (see 
below), an event logged and trap issued.  
 
RDI is also transmitted for other MEP faults like unexpected MEP, unexpected 
MD level or unexpected CCM period. This indicates that the network may be 
receiving traffic it should not be receiving. 
o Interface Status TLV (Type-Length-Value) - CCMs may contain optional interface status 
TLV which indicates (by configuration) the status of the local Ethernet UNI port.  
o CCM priority is configurable as a P-bit value at the MEP level.  
o CCM interval is user-configurable at the MA level to 3.33 ms, 10 ms, 100 ms, 1 s, 1 m,  
10 m. 
• 
LBM / LBR (loopback message / loopback reply message) – Manually triggered messages that 
check if a MEP or MIP (maintenance end/interim point) is reachable (like a “ping”).  
o LBM is multicast or unicast, LBR is always unicast (back to sender).  
o When an LBM is generated, it is sent up to 500 times (configurable) at a rate of 50 fps. 
• 
LTM / LTR (linktrace message / linktrace reply message) – Manually triggered messages that 
trace the path between MEPs. Each MIP or MEP on the route sends an LTR (reply).  
o LTMs are multicast, the responses are unicast. 
o MIPs on the path to the destination MEP and the destination MEP reply with an LTR. 
o MIPs receiving a valid LTM, respond with an LTR and forward the LTM. 
o The LTM results in the originating MEP generating a list of the MIPs along the path, 
including the destination MEPs. 
Rules that apply to both LBM and LTM messages: 
o LTMs and LBMs are always sent from a MEP to a MAC address or a Remote MEP ID.  
• 
AIS (alarm indication signal) – Multicast frames sent downstream (upstream is the MEP NNI 
port, while downstream is UNI direction) by the MEP that detects a fault. The AIS provides a 
ETX-2i Devices 
8. Monitoring and Diagnostics 
single source for alarm signals (preventing repeat signals flooding the network). The AIS can 
generate an event log and a trap. 
The transmit interval is configured per MEP and can be set to one frame per second (default) or 
one frame per minute. The AIS message priority is set per MEP via P-bit (0–7) configuration. 
• 
Lock Signal (LCK) – Notification frame informing that a service is deliberately down. Sent 
multicast. ETX-2i devices send notifications that a LCK has been received. 
MD and MA - Network definitions 
• 
Maintenance Domain (MD) – The MD is the network or network segment which the OAM CFM 
messages are monitoring.  
o Each MD has a unique ID, (informational) text name and an MD level attribute (0 – 7, 
default 3). The MD level separates the MD and its associated MAs, MEPs and MIPs from 
other MDs that may be defined on the network. 
o Different MD levels are used to monitor different types of network: Customer networks, 
access provider networks and service provider networks. The role of the MD user affects 
the type of data collected. 
• 
Maintenance Association (MA) – Required. A Maintenance Association is a set of MEPs, each 
configured with the same (unique) MAID and MD level, established to verify the integrity of a 
single service instance. An MA can also be thought of as a full mesh of Maintenance Entities 
among a set of MEPs so configured.  
o MAs have MEPs (maintenance end points). 
o MAs can set defaults for their MEPS:  
 
The CCM interval. 
 
The VLAN (should be 0 if the MEP is associated with a classifier profile). 
MEP and MIP - Device/Port/Service definitions 
Each MEP and MIP (maintenance end/intermediate points) is configured on a single device and bound to 
a single monitored port, VLAN or interface point. MEPs and MIPs can only interact with MEPs/MIPs in 
the same MD.  
• 
Maintenance End Point (MEP) – Each MEP must be part of an MD and MA. A MEP monitors an 
interface point through which data enters or exits the MA (EVC/service).  
o Each MEP has a unique ID (1 – 8191) and uses its MD’s level attribute (0 – 7).  
o MEPs send CCM messages at regular intervals (configurable in the MA) to remote MEPs 
(RMEPs).  
ETX-2i Devices 
8. Monitoring and Diagnostics 
o Remote MEPs can be either manually configured or automatically learnt, using the 
command rmep-learning for automatic MEP learning or remote-mep for static MEP 
definition. 
o MEPs can transmit all types of OAM CFM messages with CLI command CCM-initiate, the 
lbm command sends a loopback message and linktrace command sends a link trace 
message. 
o MEPS can be up or down:  
Down MEP is supported over and bound to an Ethernet physical port, facing the port’s 
Egress direction. 
Configurable direction (Down) at the MEP level. 
Configurable Ethernet port binding at the MEP level. 
o Down MEP inherits its MAC address from the Ethernet physical port it is bound to.  
o MEPs forward OAM frames that have a higher MD level and drop OAM frames that have 
a lower MD level. 
o CCM priority is configurable as a P-bit value at the MEP level. CCM CoS is also set at the 
MEP level according to P-bit-to-CoS profile with up to four such profiles per chassis. 
• 
Maintenance Intermediate Points (MIPs) – Optional. MIPs are passive points (unlike MEPs) that 
do not initiate communications. They do respond when triggered by (LTM) link trace messages 
and (LBM) loopback messages. 
MIPs can be created either as MD-level MIPs (recommended) or Service-level MIPs: 
o MD-level MIPs are created with the md-level-mip command which causes ETX-2i 
devices to automatically create MIPs for each flow at each physical port, bridge port, 
ring port and on each EVC (VLAN). MIPs are created for the existing flows and for flows 
created after the command is sent. Each MIP inherits its source MAC address from the 
adjacent port.   
 
MD-level MIPS do not reply to loopback messages (LBMs). 
 
If an MD-level MIP is configured and a MEP with an equal or higher MD level is 
added on the same flow, the MIP is removed from the flow. An MD-level MIP 
cannot be provisioned for the flow while the MEP exists. 
 
MD-level MIPs are not provisioned for flows connected to a MEF-8 PW SVI, ETP 
subscriber/transport port, or router interface. 
 
MD-level MIPs can be defined over flows with one of the classifications: Single 
VLAN or Single outer + single inner VLAN. 
o Service-level MIPs are created manually (one MIP at a time) using the MIP<mipid> 
command. The service level MIPs must then be bound to a Rx or Tx flow direction and  
ETX-2i Devices 
8. Monitoring and Diagnostics 
Note 
The ability to create service-level MIPs in automatic mode is 
maintained for backward compatibility. For new deployments, it is 
recommended to use service-level MIPs in manual mode only. 
Rules that apply to all MIPS 
 
Each MIP has a unique ID and uses its MD’s level attribute (0 – 7). 
 
MIPs only send response messages. The only messages they respond to are LBM 
(loop back messages) and LTM (link trace messages, see OAM CFM Frame Types 
above) sent from a MEP with the same MD level. 
 
MIPs use the MAC address of the port they are bound to. 
 
MIPs can be bound to a particular flow direction (Rx or Tx). The MIP must be 
shutdown before it is bound to a specific port and/or Tx/Rx flow.   
MD Levels 
To enable different entities to separately monitor the network, OAM messages are partitioned by MD 
Level (0–7). Higher numbers are closer to network management and lower numbers to the individual 
device or port. Each MD level is isolated from the others and has no access to their monitoring data.  
• 
Customer network – MD level 7 or 6. Customer managed, UNI – user to network and up stream. 
Covers the whole network but is isolated from provider OAM messages. Oriented to customer 
needs, such as continuity and SLA (service level agreements). 
• 
Service provider network – MD level 5 or 4. Only for the provider infrastructure, UNI or NNI, 
downstream. Oriented to SLA thresholds and service quality. 
• 
Access provider network – MD level 3 or 2. NNI – Network to network, downstream. Oriented 
towards issuing alarms and looking for linkage problems.   
• 
Physical links – MD level 0 or 1. 
ETX-2i devices forward CCM messages belonging to higher MD levels and drop CCM messages 
belonging to lower levels. 
Each MD level maintains distinct CCM streams, MEPs and MIPs. 
Lower-level MDs remain within the confines of higher-level MDs (they cannot cross outside). 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Dynamic Remote MEP Learning 
ETX‑2 supports dynamic (automatic) Remote MEP (RMEP) learning per MEP, in addition to static RMEP 
configuration. RMEP learning uses the rmep-learning CLI command, allows each endpoint to learn 
RMEPs automatically, by recognizing CCMs (relevant for 1 Sec and 10 Sec CCMs) from new endpoints, 
and then automatically adding those endpoints to the MEP’s RMEP list.  
RMEP learning simplifies provisioning of large E-LAN installations. In the absence of dynamic RMEP 
learning, CCM in E-LAN applications would require the administrator to configure RMEPs of all E-LAN 
members. For example, for an E-LAN of n members, the administrator would have to configure n-1 
RMEPs for each endpoint. Moreover, if an additional endpoint is added to an existing E-LAN service with 
n endpoints, the administrator needs to add an RMEP to each endpoint. With dynamic RMEP learning, 
all remote MEPs are learned automatically, without requiring the administrator to configure them.   
Before moving to RMEP learning, you should: 
• 
shutdown the MEP. 
• 
Remove all the MEP’s RMEPs. 
Once RMEP learning is enabled, you cannot configure static RMEPs, and vice versa (sanity). Also, 
unexpected MEP alarms are disabled for this MEP.  
All learned RMEPs are removed/deleted by doing one of the following: 
• 
Rebooting the device 
• 
Shutting down the MEP 
An administrator can remove a specific learnt RMEP by:  
• 
Running the clear-dynamic-rmep CLI command 
Note 
• 
In some conditions, RMEP learning can cause SLM Loss. 
• 
If one of the RMEPs transmits with a different CCM period (mainly lower), 
learning is not performed properly. 
• 
Learned RMEPs are not saved to the device database. 
• 
When Y.1564 test is activated, automatic RMEP learning is automatically 
disabled. Once the test completes, RMEP learning is reenabled. 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
OAM Connectivity 
The figure below shows how the various levels of OAM sessions supported by RAD equipment allow 
each entity to monitor the layers under its responsibility and easily isolate problems. The Maintenance 
Entities (MEs) are created at different levels: 
• 
Lowest-level OAM session (subscriber ME) between two subscriber devices (devices 1 and 8 at 
the top of the diagram). ETX‑2i devices serve as MIPs. 
• 
End-to-end OAM session (EVC ME) between two ETX‑2 devices, which serve as MEPs. ETX-5 
devices act as MIPs. 
• 
Segment OAM session (operator service ME) between ETX‑2 and the network side of ETX-5. 
• 
Transport OAM session (tunnel ME) between network ports of two ETX-5 devices. 
Service Provider
Operator B NEs
Operator A NEs
Subscriber 
Equipment
Subscriber 
Equipment
Subscriber ME
Transport
Ethernet
EVC ME
Tunnel ME
Operator B Service ME
Operator A Service ME
UNI ME
UNI ME
1
2
3
4
5
6
7
8
Legend:
Triangle – MEP (Maintenance End Point)
Circle – MIP (Maintenance Intermediary Point)
ETX-5
Router
ETX-2
Router
ETX-2
ETX-5
 
Multi-Domain Ethernet Service OAM 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
OAM Performance Monitoring 
The OAM PM functionality complies with ITU-T Y.1731 and MEF 36. ETX‑2 provides loss and delay 
measurements, as well as event reporting. ETX‑2 supports the following measurement methods: 
• 
User data – This method measures user data and CCM messages. You can specify that this 
method should measure only green packets (color-aware loss measurement); additionally, you 
can specify that it should not measure CCM messages.  
In the case of color-aware loss measurement, the following statistic counters are based on green 
packets only: 
 
Forward/backward Tx/Rx frames 
 
Forward/backward Frame Loss Ratio (FLR) 
 
Forward/backward Availability/Unavailability 
• 
Synthetic – This method measures DM frames. It is recommended when working with devices 
that do not count user data frames. 
• 
LMM synthetic – This method measures synthetic frames as well. It is recommended for working 
with ETX-201A/202A. 
• 
SLM synthetic – This method measures synthetic SLM/SLR frames.  
ETX-2i devices calculate one-way IFDV (frame delay variation) measurement by dividing the two-way 
measurement result by two. 
Note 
• 
While working in a Bridge application, not learned user data packets, and 
multicast and broadcast transmitted frames are counted several times. 
• 
When the delay is 1 second or more the delay counters in the service and 
destination NE statistics do not show accurate results. 
One-Way Delay Measurement 
ETX-2i devices support one-way delay measurements using the 1DM standard as defined by Y.1731. 
One-way delay measurement allows a MEP to send frames with one-way ETH-DM information to its 
peer MEP, to facilitate one-way frame delay and/or one-way frame delay variation measurements at the 
peer MEP.  
Note 
One-way frame delay measurement can only be carried out if the clocks 
between the two MEPs are synchronized. 
The PDU used for one-way ETH-DM is 1DM. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
1DM transmission 
When configured for one-way delay measurements, a MEP periodically transmits 1DM frames with the 
TxTimeStampf value. 
1DM reception 
When configured for one-way delay measurements, a MEP, upon receiving a valid 1DM frame, uses the 
following values to make one-way frame delay measurement. These values serve as inputs to the one-
way frame delay variation measurement: 
• 
1DM frame TxTimeStampf value 
• 
RxTimef, which is the time at reception of the 1DM frame 
Operator
(Service Provider)
NID-A
UNI
MEP-B
MEP-A
1DM Tx
1DM Rx → Calc.   Delay A → B
NID-B
UNI
 
One-Way Delay Measurement 
Clock source 
The clock source which sets the timestamps can be taken either from 1588 (slave/BC or master) or from 
NTP. 
• 
1588: If chassis has a PTP option and 1588 slave, BC, or GM is configured 
• 
NTP: If not (no PTP option or no 1588 configuration) 
Note 
One-way delay is applicable only if the end-to-end delay is higher than the 
level of NTP accuracy. This means for example that back-to-back testing 
would yield invalid results. 
One-Way delay measurement report 
See below an example of a one-way delay measurement report. The relevant statistics for 1DM are: 
• 
One Way Delay: Min/Average/Max 
• 
One Way IFDV: Min/Average/Max 
• 
1DM Rx, 1DM Tx 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
ETX-2i>config>oam>cfm# show ma 1 ma 1 m 1 se 1 des 1 statis cu 
Current 
----------------------------------------------------------------------------
-                       Forward              Backward             
Tx Frames            : 85                   85                   
Rx Frames            : 85                   85                   
Frames Loss          : 0                    0                    
Frame Loss Ratio (%) : 0.0000%              0.0000%              
Unavailable Seconds  : 254                  254                  
Available Seconds    : 0                    0                    
 
Two Way Unavailable Seconds : 254                  
Two Way Available Seconds   : 1                    
 
                Min        Average    Max        
                (mSec)     (mSec)     (mSec)     
One Way Delay : 1.470      1.746      1.991      
One Way IFDV  : 0.000      0.118      0.350      
 
Frames Above Delay Threshold : 85         
Frames Above IFDV Threshold  : 0          
                                          
Elapsed Time (sec)           : 257                                                 
 
Loss and Delay Measurements Messages 
----------------------------------------------------------------------------- 
       Tx                Rx         
LMMs : 87        LMRs  : 87         
1DM  : 87        1DM   : 87         
OAM Packet Handling 
This section describes how an OAM packet is handled in the following: 
• 
MEP – CCM 
• 
MEP – LB/LT 
• 
MEP – LM/DM 
• 
MIP 
For each of these modes, a description is provided as to how packets are discarded and counted in the 
port counters, per port, under the ‘OAM Discarded’ counter, at the following levels: 
• 
Low MD level – Packet’s OAM level is lower than the defined MEP’s level. 
• 
Equal MD level – Packet’s OAM level is equal to the defined MEP’s level. 
• 
High MD level – Packet’s OAM level is higher than the defined MEP’s level. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
MEP – CCM 
Lower MD-Level:  
• 
Multicast / unicast My-MAC / unicast different MAC 
 
Packet received from Active side –> MEP defect  
 
Cross Connected CCM (mismatch; unexpected MD level): On 
 
Packet received from Passive side –> OAM discarded on port. 
Equal MD-Level:  
• 
Multicast / unicast My-MAC 
 
Packet received from Active side –> OK 
 
Packet received from Passive side –> OAM discarded on port  
• 
Unicast different MAC (not My-MAC DA) 
 
Packet received from Active side –> DA MAC is not analyzed. No discard, no alarm – MEP in 
OK status.  
 
Packet received from Passive side –> OAM discarded on port 
Higher MD-Level: 
• 
Multicast /unicast different MAC 
 
Packet received from both sides –> considered as user data 
• 
Unicast My-MAC 
 
Packet received from both sides –> OAM discarded on port 
MEP – LB/LT 
Lower MD-Level: 
• 
LB/LT multicast / unicast My-MAC / unicast different MAC 
 
Packet received from both sides –> OAM discarded on port 
Equal MD-Level: 
• 
Multicast / Unicast My-MAC (LB/LT) 
 
Packet received from Active side –> OK 
 
Packet received from Passive side –> OAM discarded on port 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
• 
Unicast different MAC (not My-MAC DA) 
 
LB 
 
Packet received from both sides –> OAM discarded on port 
 
LT 
 
Packet received from Active side –> discarded by the CPU; no indication 
 
Packet received from Passive side –> OAM discarded on port 
Higher MD-Level: 
• 
Multicast /unicast different MAC 
 
Packet received from both sides –> considered as user data 
• 
Unicast My-MAC (relevant to LB only) 
 
Packet received from both sides –> OAM discarded on port 
MEP – LM/DM 
Lower MD-Level: 
• 
Multicast / unicast My-MAC / unicast different MAC 
 
Packet received from both sides –> OAM discarded on port 
Equal MD-Level: 
• 
Multicast / unicast My-MAC 
 
Packet received from Active side –> OK 
 
Packet received from Passive side –> OAM discarded on port 
• 
Unicast different MAC (not My-MAC DA) 
 
Packet received from both sides –> OAM discarded on port 
Higher MD-Level: 
• 
Multicast /unicast different MAC 
 
Packet received from both sides –> considered as user data 
• 
Unicast My-MAC 
 
Packet received from both sides –> OAM discarded on port 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
MIP  
Note 
Not relevant for global MIP. 
Lower MD-Level received packet:  
• 
Multicast / unicast different MAC –> considered as user data 
• 
Unicast My-MAC –> OAM discarded on port 
Equal MD-Level received packet:  
• 
Linktrace (LT) (always MC DA)  
 
Answer LTR. Forward LTM, if not HIT  
• 
Loopback (LB) 
 
MC -> considered as user data  
 
Unicast My-MAC–> answer LBR 
 
Unicast different MAC -> considered as user data 
• 
Other OAM packets 
 
MC -> considered as user data  
 
Unicast My-MAC –> OAM discarded on port 
 
Unicast different MAC -> considered as user data 
Higher MD-Level received packet: 
• 
Multicast /unicast different MAC 
 
Packet received from both sides –> considered as user data 
• 
Unicast My-MAC 
 
Packet received from both sides –> OAM discarded on port 
MEF46 Latching Loopback 
MEF46 enables associating a Latching Loopback State Machine (LLSM) with a MEP. You can enable or 
disable the Latching Loopback functionality (LLF) per MEP, which is configured with Rx and Tx flows (and 
not Classification). By default, LLF is disabled. LLF is supported in either a service down or up MEP that is 
connected to a physical or LAG port. When LLF is enabled, the operational status of the MEP is set to 
mef46Loop. Latching Loopback is supported in all network topologies that support Y.1564, i.e., E-Line, E-
LAN, and E-Tree. 

## Factory Defaults  *(p.1299)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Handling RMEP Alarm Storm 
ETX‑2i devices manage a high burst of RMEP alarms in the following manner: 
• 
If there are more than 100 RMEP alarms (LOC, RDI) per second, ETX‑2i stops sending specific 
RMEP alarms and instead sends the systemAlarmStorm alarm to indicate a high rate of RMEP 
alarms. 
• 
Once there are fewer than 100 RMEP alarms per second for a duration of 60 seconds, ETX‑2i 
turns off the systemAlarmStorm alarm and resumes sending specific RMEP alarms. 
Factory Defaults 
By default, OAM functionality is disabled. There are no MDs, MAs, or MEPs. 
The OAM CFM general parameters have the following default configuration. 
Parameter 
Default  
Remarks 
alarm-type  
legacy 
availability 
delta-t 1 n 10 forward-thr 50 
backward-thr 50 
Forward threshold and backward threshold 
default values are 50% (unit is %).   
md-level-mip 
no md-level-mip 
Service-level MIP is the default. 
mip-assign 
manual 
Manual MIP creation is the default. 
multicast-addr 
01-80-C2-00-00-30 
multi-mep-per-evc 
no multi-mep-per-evc 
 
When a maintenance domain is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
proprietary-cc 
no proprietary-cc 
Standard OAM protocol 
md-level 
3 
name   
string "MD<mdid>" 
For example, the default name for 
maintenance domain 1 is “MD1”. 
When a maintenance association is created, it has the following default configuration. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Default  
Remarks 
ccm-interval 
1s 
Continuity check interval is 1 second. 
interface-status-tlv 
interface-status-tlv 
classification  
vlan 0 
name   
string "MA<maid>" 
For example, the default name for 
maintenance association 1 is “MA1”. 
When a maintenance endpoint is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
ais 
no ais 
bind 
no bind 
ccm-initiate 
ccm-initiate 
Initiate continuity check messages. 
ccm-priority 
0 
classification  
vlan 0 
client-md-level  
4 
customer-tags-excluded 
no customer-tags-excluded 
dest-addr-type 
ccm multicast pm unicast 
Destination address type for CCM messages – 
multicast 
Destination address type for performance 
measurement messages – unicast 
direction 
down 
forwarding-method 
e-line 
queue   
fixed 0  
shutdown 
shutdown 
Administratively disabled 
When a service is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
delay-threshold  
1000 
delay-var-threshold 
1000 
dmm-interval 
1s 

## Configuring OAM CFM  *(p.1301)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Default  
Remarks 
lmm-interval 
1s 
shutdown 
shutdown 
Administratively disabled 
When a destination NE is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
bck-delay-var-bin 
no bck-delay-var-bin 
delay  
two-way data-tlv-length 0 
delay-measurement-bin 
no delay-measurement-bin 
delay-var-measurement-bin 
no delay-var-measurement-bin 
description 
"Put your string here" 
fwd-delay-var-bin 
no fwd-delay-var-bin 
loss 
single-ended user-data lm-mode tx-rx 
remote 
mac-address 00-00-00-00-00-00 
Configuring OAM CFM 
Ethernet OAM configuration includes the steps detailed in this section: 
Note 
Before deleting any OAM CFM component, verify that it is not used by other 
ETX‑2i elements, such as ERP. 
 To configure the service OAM: 
1. Configure general OAM parameters.  
2. Add and configure maintenance domain(s) (MD). 
3. Configure maintenance associations for the added MDs. 
4. If ETX‑2i is acting as a MIP, then configure the necessary MIPs. 
5. If ETX‑2i is acting as a MEP: 
a. Configure MA endpoints, referred to as MEPs. 
b. Configure MEP services. 
c. Configure Destination NEs. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Setting General Parameters 
You can define general OAM CFM parameters, as well as displaying OAM CFM information.   
 To define general OAM CFM parameters: 
1. Navigate to configure oam cfm. 
The config>oam>cfm prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Defining whether legacy 
alarms or newer alarms 
are used 
alarm-type { legacy | soam } 
legacy – OAM alarm names remain the same 
as in previous versions. 
soam – OAM alarm names change as follows: 
• defErrorCCM – MEP level alarm: invalid 
CCM received with CCM Interval that has 
not yet timed out; replaces mismatch 
• defMACstatus – RMEP level alarm: Defect 
reported by interface or port status TLV 
• defRDICCM – RMEP level alarm: RDI 
(remote defect); replaces rdi 
• defRemoteCCM – RMEP level alarm: Loss 
of continuity (LOC); replaces loc 
• defXconCCM – MEP level alarm: 
Unexpected CCM received from MAID or 
lower MD level; replaces mismatch 
Defining parameters for 
availability calculations 
availability [delta-t { 1 | 2 | 3 | 4 | 5 | 6 | 
10 |12|15|20 }][n<n>] 
[forward-thr <forward-thr-percents>] 
[backward-thr <backward-thr-percents>] 
These parameters define availability 
performance measurement, based on frame 
loss during a sequence of consecutive small 
time intervals. 
delta-t – time interval (in seconds) 
n – number of consecutive small time 
intervals over which to measure availability 
Possible values: 1-100 
forward-thr – Forward frame loss ratio 
threshold, for which unavailability occurs if 
exceeded (%) 
Possible values: 0–100  
forward-thr = 0 recommended for measuring 
low levels of loss 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
backward-thr – Backward frame loss ratio 
threshold, for which unavailability occurs if 
exceeded (%) 
Possible values: 0–100  
forward-thr = 0 recommended for measuring 
low levels of loss. 
Configuring LTR 
Parameters 
ltr [port-id-subtype { ifName | ifAlias }] 
[up-mep-port { uni | nni }] 
port-id-subtype – LTR frame port ID subtype 
Default: IfAlias 
up-mep-port - Advertised port in LTR for up 
MEP: 
• uni – egress TLV 
• nni – ingres TLV 
Default: nni 
Configuring 
Maintenance Domain 
(MD) 
[no] maintenance-domain <mdid> 
See Configuring Maintenance Domains for 
more details.  
Configuring MD-level 
MIP 
[no] md-level-mip <md-level-list> 
 
Configuring 
measurement bin 
profiles 
[no] measurement-bin-profile <name> 
See Configuring Measurement Bin Profiles 
for more details. 
Configuring service-level 
MIP creation mode 
mip-assign { automatic | manual } 
Recommended to create MIPs only in manual 
mode (default mip-assign manual; no need to 
run command). In this mode, you create MIPs 
under the MD level using the mip command 
(see Configuring Maintenance Intermediate 
Points). 
Automatic MIP creation mode (mip-assign 
automatic) is available for backward 
compatibility only. This mode is not 
recommended. 
Configuring the MAC 
address used in 
multicasts 
multicast-addr <mac-address> 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Enabling support and 
configuration of multiple 
MEPs for the same EVC 
(same MD, MD-level, 
and MA) 
[no] multi-mep-per-evc 
Default: no multi-mep-per-evc 
Displaying information 
on MIPs 
show mips 
Shows all service-level MIPs; not MD-level 
MIPs. 
Displaying OAM CFM 
information such as 
MDs, MAs, MEPs, etc. 
show summary 
See Viewing OAM CFM Information for more 
details. 
Configuring Measurement Bin Profiles 
You can define measurement bin profiles to define sets of threshold ranges (in microseconds (μs)) for 
displaying delay measurements in destination NEs. See Configuring and Viewing Delay Measurement 
Bins for a configuration example. 
 To define measurement bin profiles: 
1. Navigate to configure oam cfm. 
2. Enter the measurement bin profile level by entering the following: 
measurement-bin-profile <name>. 
3. Specify the thresholds (single value, or values separated by commas) in microseconds (μs). 
thresholds <thresholds-list> 
Each value is used as the upper range of a set of thresholds, up to 5,000,000. For instance, 
entering thresholds 500,1000,15000 results in this set of threshold ranges: 
 
0–500 
 
501–1,000 
 
1,001–15,000 
 
15,001–5,000,000 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing OAM CFM Information 
You can display OAM CFM information by entering show summary, as shown in the following. 
ETX‑2i# configure oam cfm 
ETX‑2i# config>oam>cfm# show summary 
 
 
 
md 
slot/ classifi 
admin mep ok/total 
md/ma/mepid 
md/ma name 
 
lvl 
port 
cation status def r.meps 
 
001/001/001 
MD1/MA1 
 
3 
eth0/1 100 
enable off 
1/1 
002/002/8191 1234567890123456789012 
3 
eth0/1 0 
disable 
 
34567890/1234567801234 
002/005/123 
1234567890123456789012 
3 
eth0/1 100/ 
enable off 
0/2 
 
34567890/155  
 
 
200 
002/006/101 
1234567890123456789012 
3 
eth0/3 untagged 
enable off 
0/3 
003/001/001 
/iccname 
 
4 
eth0/1 100.1 enable off 
0/1 
004/001/001 
20-64-32-AB-CD-64 120/ 
0 
eth0/1 4000 
enable off 
0/1 
 
MA1 
004/002/001 
20-64-32-AB-CD-64 120/ 
0 
eth0/1 3000/ enable off 
0/3 
 
12345678901234567890123 
Configuring Maintenance Domains  
MDs are domains for which the connectivity faults are managed. Each MD is assigned a name that must 
be unique among all those used or available to an operator. The MD name facilitates easy identification 
of administrative responsibility for the maintenance domain.  
 To add a maintenance domain: 
• 
At the config>oam>cfm# prompt enter: 
maintenance-domain <mdid> 
where mdid is 1–4095 
The maintenance domain is created and the config>oam>cfm>md(<mdid>)$ prompt is 
displayed. 
 To delete a maintenance domain: 
• 
At the config>oam>cfm# prompt enter: 
no maintenance-domain <mdid> 
The maintenance domain is deleted.  
Note 
A maintenance domain can be deleted only if all its MEPs/MIPs are deleted or 
disabled. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure a maintenance domain: 
1. Navigate to configure oam cfm maintenance-domain <mdid> to select the maintenance domain 
to configure. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Configuring maintenance 
association (MA) for the MD 
[no] maintenance-association <maid> 
See Configuring Maintenance 
Associations.  
no maintenance-association <maid> 
deletes the MA. 
Specifying the MD level 
md-level <md-level> 
The allowed range for md-level is 0–7. 
Note:  
• If pre-standard OAM protocol is being 
used, the only allowed value for the 
maintenance domain level is 3. 
• When md-level is set to 7, client md-
level, even if configured, becomes 
meaningless, as it must have a higher 
value than md-level but cannot exceed 
7. 
Configuring service-level 
MIP 
[no] mip <mipid> 
This parameter is visible only for manual 
MIP creation mode (the default and 
recommended mode).  
See Configuring Maintenance 
Intermediate Points for full configuration 
details. 
no mip <mip id> deletes the MIP. 
Defining service-level MIP 
policy 
mip-policy { explicit | default } 
This command is available for backward 
compatibility only, when you select 
automatic MIP creation mode (not 
recommended).  
Specifying the name format 
and name of the 
maintenance domain 
name string <md-name-string> 
name dns <md-name-string> 
name mac-and-uint <md-name-mac> 
<md-name-uint> 
no name 
Maximum length of md-name-string is 
43 characters. 
Maximum combined length of 
md-name-string and ma-name-string 
(maintenance association name) is 
48 characters. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Format mac-and-uint – Specify 
md-name-mac as xx-xx-xx-xx-xx-xx, and 
md-name-uint as an unsigned integer 
decimal number (0–65535). 
If pre-standard OAM protocol is being 
used, the maintenance domain must have 
no name (use command no name). 
Specifying the OAM 
protocol type 
no proprietary-cc 
proprietary-cc 
Use no proprietary-cc for standard OAM 
protocol. 
Use proprietary-cc for pre-standard OAM 
protocol. 
Note: MD must have no name (via no 
name) and the level must be 3 before you 
can set the protocol to pre-standard. 
Configuring Maintenance Associations 
A maintenance domain contains maintenance associations (MAs). 
 To add a maintenance association (MA): 
• 
At the config>oam>cfm>md(<mdid>)# prompt enter: 
maintenance- association <maid> 
where maid is 1–4095 
 To delete a maintenance association: 
• 
At the config>oam>cfm>md(<mdid>)# prompt enter: 
no maintenance-association <maid> 
Note 
A maintenance association can be deleted only if all its MEPs/MIPs are 
deleted or disabled. 
 To configure a maintenance association: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
to select the maintenance association to configure. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Specifying the interval 
between continuity check 
messages 
ccm-interval { 3.33ms | 10ms | 
100ms | 1s | 10s | 1min | 10min } 
Note: When ccm-interval is set to 3.33ms, then 
if you have defined the maximum number of 
MEPs (255), the interval is not enough time to 
activate them with all the corresponding remote 
MEPs.  
Associating the MA with a 
VLAN 
classification vlan <vlan-id> 
Verify that the VLAN is the same as the VLAN 
associated with the MEP. 
Note: If a classifier profile is associated with the 
MEP, the VLAN should be set to 0. 
Specifying if Interface Status 
TLV is in continuity check 
messages 
interface-status-tlv 
Note: A fault propagation rule must be 
configured to trigger interface-status-tlv upon 
port loss 
Example: fault-propagation port ethernet 0/5 to 
mep 1 1 5 
action-on-group oam-cfm-if-status-tlv 
trigger los 
Configuring MEP for the MA 
mep <mepid> 
See Configuring Maintenance Endpoints. 
Defining a general MIP policy 
for the MA 
mip-policy 
{ explicit | default | defer } 
This command is available for backward 
compatibility only, when you select automatic 
MIP creation mode (not recommended). 
Specifying the name format 
and name of the maintenance 
association 
name string <ma-name-string> 
name primary-vid 
<ma-name-vid> 
name uint <ma-name-uint> 
name icc <ma-name-icc> 
The maximum length of ma-name-string is 
45 characters. 
Maximum combined length of md-name-string 
and ma-name-string is 48 characters. 
Format primary-vid (primary VLAN ID) – Specify 
ma-name-vid as 1–4094. 
Format uint – Specify ma-name-uint as an 
unsigned integer decimal number  
(0–65535). 
Format icc – Specify ma-name-icc as the ITU 
carrier code that is assigned to the relevant 
network operator/service provider. The codes 
are maintained by ITU-T as defined in ITU-T Rec. 
M.1400. icc name length supported is 1-13 
charcters. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Note: If the icc option is selected or pre-standard 
OAM protocol is being used, the maintenance 
domain must have no name (use the command 
no name). 
Configuring Maintenance Endpoints 
Maintenance endpoints reside at the edge of a maintenance domain. They initiate and respond to 
CCMs, linktrace requests, and loopbacks, to detect, localize, and diagnose connectivity problems. 
Note 
For every MEP, a flow must be configured with the same classification as the 
MEP, in the direction UNI to NNI. This can be achieved using either of the 
following methods: 
• 
Classification method – Configure the MEP classification; the SW 
automatically finds and matches the corresponding flows to the MEP 
according to the MEP’s configured classification. 
• 
Rx, Tx flows method – Explicitly bind flows on a MEP. The MEP derives its 
classification from its bound flows. 
 To add a maintenance endpoint (MEP): 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)# prompt, enter: 
mep <mepid> 
where mepid is 1–8191 
 To delete a maintenance endpoint:  
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)# prompt, enter: 
no mep <mepid> 
Note 
You can remove a maintenance endpoint regardless of whether it contains 
services. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure a maintenance endpoint: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid>to select the maintenance endpoint to configure. 
2. Perform the required tasks according to the following table.  
Note 
When changing the MEP classification method, you must delete the MEP and 
then create a new MEP. 
 
Task 
Command 
Comments 
Defining sending of AIS  
ais [ interval { 1s | 1min }] 
[priority <priority>] 
When md-level is set to 7, client-md-level, 
even if configured, becomes meaningless. In 
this case, the MEP cannot be defined to AIS 
transmission and must be set to no-ais. 
Binding the MEP to an 
Ethernet port 
bind ethernet [<slot>/]<port> 
To remove the MEP from an Ethernet port, 
enter no bind. 
Binding the MEP to an ETP 
port if ETP is used 
bind etp <etp-name> 
{subscriber | transport} <port-id> 
To remove the MEP from an ETP port, enter 
no bind. 
Binding the MEP to a logical 
MAC port 
bind logical-mac <port-number> 
To remove the MEP from a logical MAC 
port, enter no bind. 
Binding the MEP to PCS port  
bind pcs <port-number> 
To remove the MEP from a PCS port, enter 
no bind. 
Note: Relevant only for the SHSDL module 
option. 
Binding the MEP to bridge 
port 
bind bridge-port <bridge-number> 
<port-number> 
The bridge port must not be used by a flow. 
Enabling initiation of 
continuity check messages 
(CCM) 
ccm-initiate  
To disable initiating continuity check 
messages, enter no ccm-initiate. 
Specifying the priority of 
CCMs and LTMs transmitted 
by the MEP 
ccm-priority <priority> 
Possible values: 0–7 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Associating the MEP with a 
classifier profile or VLAN 
classification vlan <vlan-id> 
classification profile <profile-name> 
You can associate more than one MEP to 
the same VLAN if the MEPs belong to MDs 
with different levels. 
Verify that the VLAN is the same as the 
VLAN associated with the MA. 
If using a classifier profile, it must be 
EVC.cos or VLAN+inner-VLAN. 
 
Deleting remote MEPs 
clear-dynamic-rmep <rmep#> 
Deletes the learned remote MEPs of the 
MEP. 
Clearing MEP statistics 
clear-statistics 
 
Defining client MD level 
client-md-level <md-level> 
Possible values: 0–7 
Client MD level must be higher than MD 
level.  
Note: When md-level is set to 7, 
client-md-level, even if configured, 
becomes meaningless, as it must have a 
higher value than md-level but cannot 
exceed 7. 
Specifying continuity 
verification method 
continuity-verification <cc-based | 
lb-based> 
This parameter is visible only in pre-
standard mode and can be configured only 
if ccm-initiate is enabled as explained 
above. Use lb-based only for RAD 
proprietary OAM functionality. 
Specifying that MEP 
transmits OAMPDUs with 
only S-tag, and no C-tag 
customer-tags-excluded 
This parameter is visible only for up MEPs 
and is relevant to E-line only; it is not 
applicable for up MEPs over bridge or ETP. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining the MAC address 
type sent in OAM continuity 
check messages (CCM) and 
performance measurement 
messages (PM) 
dest-addr-type [ccm { unicast|multicast }] 
[pm { unicast|multicast }] 
If more than one remote MEP ID has been 
defined for the MEP and you change the 
CCM destination address type from 
multicast to unicast, all remote MEP IDs are 
deleted except for the lowest remote MEP 
ID. 
If the MAC address type for PM messages is 
unicast, then the MAC address for the 
transmission of PM messages is determined 
by the configuration of the destination NE. 
If a remote MAC address is configured for 
the destination NE, that MAC is used. 
Otherwise, if a remote MEP ID is configured 
for the destination NE, the remote MAC 
address is learned from CCM messages. See 
Configuring Destination NEs for details. 
Defining a unicast MAC 
address if you defined 
unicast MAC address type 
for CCM messages with the 
dest-addr-type command 
dest-mac-addr <mac-addr> 
MAC address is in format xx-xx-xx-xx-xx-xx 
Defining direction 
direction { up | down } 
If the MEP is bound to a bridge or ETP port, 
the direction must be up. 
Assigning unidirectional or 
bidirectional Rx or Tx flow to 
the MEP 
flow uni-direction rx <rx-name> [ 
tx <tx-name>] 
flow bi-direction <name> 
Rx flow: Flow with ingress port that is the 
MEP facing port 
Tx flow: Flow with egress port that is MEP 
facing port 
Rx/Tx flows cannot be assigned if one of the 
following is true: 
• VLAN is configured at the MA level. 
• VLAN or profile is configured at the MEP 
level for the Rx classification. 
Up to eight Tx flows and eight Rx flows can 
be assigned to the MEP. 
Note: 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
• In case of a Down MEP, the classification 
is taken from the Rx flows; in this case, 
more than one Rx flow is supported only 
when all flows have the same VLAN 
classification with different P-bits. 
• When using an Up MEP on a physical 
port, more than one Rx flow is 
supported, even with different VLANs. 
This is not relevant in the case of an Up 
MEP with “customer-tag-exclude”; in 
this case, the classification is taken from 
the Rx flows and has the limitation of 
Down MEP (first note). 
• To delete flow assignment, enter no 
flow uni-direction or no flow 
bi-direction, respectively.  
Defining forwarding method 
forwarding-method { e-line | e-lan } 
 
Activating CFM loopback 
(LBM) 
lbm 
See Performing OAM Loopback for details. 
Activating linktrace (LTM) 
linktrace 
See Performing OAM Link Trace for details. 
Enabling/disabling Latching 
Loopback Function (LLF) on 
MEP 
mef46-ll  
no mef46-ll 
Note: MEF-46 can only be enabled on MEP 
configured with Rx and Tx flows. It cannot 
be enabled on MEP configured with 
classification. 
Defining the queue for the 
MEP 
queue fixed <queue-id> 
[block <level-id>/<queue-id>] 
queue queue-mapping 
<queue-map-profile-name> 
[block <level-id>/<queue-id>] 
Note: The block parameter is not allowed 
for up MEPs. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining remote MEP 
(static) with which the MEP 
communicates 
remote-mep[<rmep1>..<rmep2>,<rmep3>] 
Possible values for remote MEP IDs: 
1–8191 
You can define multiple remote MEP IDs in 
one remote-mep command by specifying a 
list of values separated by commas (with no 
spaces between the values), using .. to 
indicate ranges. You can end the command 
line with <CR> and then input another list. 
Up to 10 elements (where each element is 
either a single remote MEP or a range of 
multiple remote MEPs having consecutively 
numbered IDs) can be configured in a list. 
The MEP ID must be different than the 
remote MEP ID(s). You can use multiple 
remote-mep commands to define up to 100 
remote MEPs for the local MEP (up to 1024 
total remote MEPS in device) if standard 
OAM protocol is being used for the MD and 
the destination address type is multicast, 
otherwise you can define only one remote 
MEP. 
Note: While Remote MEP learning is 
enabled (see below task), it is not possible 
to configure a static remote MEP.  
Enabling dynamic Remote 
MEP learning 
rmep-learning 
no rmep-learning 
Enter no rmep-learning to disable Remote 
MEP learning.Note: If you configure static 
Remote MEPs (see above task), it is not 
possible to enable Remote MEP learning.  
Configuring service for the 
MEP 
service <serviceid> 
See Configuring Maintenance Endpoint 
Services. 
Note: You can configure a service for a MEP 
only if RMEP learning is disabled. 
Displaying MEF46 Latching 
Loopback status 
show mef46-ll-status 
This parameter is visible only for MEF-46 
enabled (see above). 
 
See Viewing the MEF46 Latching Loopback 
Status. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Displaying MEP status 
show status 
The MEP status includes the types of its 
remote MEPs (static/dynamic), addresses of 
its remote MEPs, and their operational 
status.  
See Viewing MEP Status (including status 
of its remote MEPs). 
Displaying loopback status 
show lbm-results 
See Performing OAM Loopback for details. 
Displaying linktrace status 
show linktrace-results 
See Performing OAM Link Trace for details. 
Displaying remote MEP 
status 
show remote-mep-status { remote-mep-id 
<remote-mep-id> | all }  
The remote MEP status shows the address 
of the specified remote MEP, type 
(static/dynamic), and operational status. 
See Viewing Remote MEP Status. 
If a remote MEP was never learned, its 
status is “NEW”. As a result, the following 
takes place: 
• Dest NE that is configured under this 
MEP’s services cannot learn the remote 
MAC address and therefore, does not 
transmit LMM and DMM.  
• “unavailability” is not indicated and 
therefore the unavailability counters are 
not increased. 
• Available counter increments, as it is 
ready for use as soon as the remote 
MEP is configured. 
Administratively enabling 
MEP 
no shutdown 
To deactivate the MEP, enter shutdown. 
When shutdown is performed on a MEP, its 
active services (i.e., no shutdown services) 
are moved automatically to shutdown as 
well. No error or warning message is 
displayed. 
When no shutdown is performed on a MEP 
is in, its services are not activated 
automatically. 
Note: Following no shutdown of MEP, the 
following warning message appears to 
notify you to activate relevant MEP services: 
“Warning: Relevant MEP services must be 
activated following MEP reactivation”.  
ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuring Maintenance Intermediate Points  
MD-Level MIP 
You can create MD-level MIPs at the OAM CFM level, as described in this section. When MD-level MIP 
mode is activated, ETX‑2i provisions a MIP for each flow at each physical port, bridge port, and ring port. 
The MIPs are added for each specified MD level, or MD level range. 
 To add an MD-level MIP: 
• 
At the config>oam>cfm# prompt, enter md-level-mip <md-level-list>. 
The MD levels in the list can be separated by a comma or given as a range, for example: 1..3,5. 
Note 
Do not type a space after any commas in the list. 
Entering no md-level-mip <md-level-list> removes the specified MD-level MIP. 
Service-Level MIP (manual mode) 
Note 
This section is relevant only for service-level MIPs in the recommended default 
manual MIP creation mode (mip-assign parameter under OAM CFM 
configuration is configured as manual).  
Service-level MIPs are bidirectional intermediate entities defined in the maintenance domain level.  
You can create a service-level MIP under the MD level, as described below, when in manual mode.  
 To add a service-level MIP in manual mode:  
1. Navigate to configure oam cfm maintenance-domain <mdid>. 
2. At the config>oam>cfm>md(<mdid>)# prompt, enter: 
mip <mipid> 
 To delete a MIP: 
• 
At the config>oam>cfm>md(<mdid>)# prompt enter: no mip <mipid> 
 To configure a service-level MIP in manual mode: 
1. Navigate to configure oam cfm maintenance-domain <mdid> mip <mipid> to select the MIP to 
configure. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Binding the MIP to an 
Ethernet port, logical MAC 
port, or PCS port 
bind ethernet [<slot>/]<port> 
bind logical-mac <port-number> 
bind pcs <port-number> 
 
To unbind the MIP, enter no bind. 
Assigning unidirectional Rx 
and Tx flows to the MIP 
flow uni-direction rx <rx-name> [tx 
<tx-name>] 
rx-name – Rx flow name 
rt-name – Tx flow name 
To delete flow assignment, enter no flow 
uni-direction. 
Administratively enabling 
MIP 
no shutdown 
To deactivate the MIP, enter shutdown. 
Displaying MIP status 
show status 
Displayed for active MIP only.  
See Viewing MIP Status below. 
Configuring Maintenance Endpoint Services 
You can configure up to eight services on a MEP, corresponding to each p-bit.  
Note 
Only one service is allowed if the classifier profile associated with the MEP is 
according to p-bit. 
Each service sets delay and delay variation thresholds. If the thresholds are exceeded, the service is 
declared as degraded. You can also define priority of OAM messages originating from this service. 
 To add a MEP service: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, enter:  
service <serviceid> 
where serviceid is 1–8. 
 To configure a MEP service: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid> service <serviceid> to select the service to configure (<serviceid> is 1–8). 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Associating this service with a 
priority  
classification priority-bit <p-bit> 
Possible values: 0–7 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Clearing service statistics 
clear-statistics 
 
Specifying delay threshold in 
microseconds   
delay-threshold <delay-thresh> 
Possible values: 1–5,000,000  
Note: The configured value is 
rounded down to 
100 microsecond granularity, 
e.g., values 0–99 are rounded to 
0, values 100–199 are rounded 
to 100, etc. 
 
Specifying delay variation 
threshold in microseconds  
delay-var-threshold <delay-var-thresh> 
Possible values: 1–5,000,000 
Note: The configured value is 
rounded down to 
100 microsecond granularity. 
 
Configuring destination NE for 
service 
dest-ne <dest-ne-index> 
Possible values: 1–255 
Specifying the interval for delay 
measurement messages, to be 
used by all remote NEs defined 
for service 
dmm-interval { 100ms | 1s | 10s } 
 
Specifying the interval for loss 
measurement messages, to be 
used by all remote NEs defined 
for service 
lmm-interval {100ms | 1s | 10s} 
When changing lmm-interval, 
you must perform no lmm-
interval and then lmm-interval.  
Configuring collection of 
performance management 
statistics for the service, that 
are presented via the RADview 
Performance Management 
portal 
pm-collection interval <seconds> 
Note: In addition to enabling PM 
statistics collection for the 
service, it must be enabled for 
the device. See Performance 
Management. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Activating the MEP service 
no shutdown 
You can activate a service only if 
the corresponding MEP is active 
and you have defined at least 
one destination NE.Note: 
Following no shutdown of MEP, 
the following warning message 
appears to remind you to 
activate relevant MEP services: 
“Warning: Relevant MEP 
services must be activated 
following MEP reactivation.” 
Configuring Destination NEs 
For performance measurement, it is necessary to know the exact address of the destination NE. You can 
configure the remote MAC address of the NE or ETX‑2i can learn it from the CCM messages, provided 
that the remote MEP of the destination NE has been learned (its status is not “NEW”).  
If the remote MAC address is not configured and needs to be learned, performance measurement 
messages (lmm and dmm) are sent only after the address is learned. 
 To add a destination NE: 
• 
At the prompt 
config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service(<serviceid>)#, enter:  
dest-ne <dest-ne-index> 
where <dest-ne-index> is 1–255 
 To configure a destination NE: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid> service <serviceid> dest-ne <dest-ne-index> to select the destination NE to 
configure. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Assigning the delay variation 
measurement bin profile for 
backward delay variation 
measurement 
bck-delay-var-bin-profile profile 
<name> 
 
Clearing statistics 
clear-statistics 
The destination network 
element running counters are 
cleared; the interval and current 
counters are not cleared. 
Specifying delay measurement 
method and length of DMM 
data TLV 
delay { one-way | two-way } 
[data-tlv-length <length-val>] 
If available and configured, one-
way delay measurements (1DM) 
use Time of Day (ToD) by 
GNSS/Y.1588 at first priority. If 
GPS is unavailable or Y.1588 
Grand Master is not configured, 
NTP ToD is used instead. 
Assigning the delay 
measurement bin profile  
delay-measurement-bin 
profile <name> 
The delay measurement bin 
profiles are defined in the 
conf>oam>cfm level. 
Assigning the delay variation 
measurement bin profile 
delay-var-measurement-bin 
profile <name> 
The delay measurement bin 
profiles are defined in the 
conf>oam>cfm level. 
Configuring description string 
description <string> 
 
Assigning the delay variation 
measurement bin profile for 
forward delay variation 
measurement 
fwd-delay-var-bin-profile 
profile <name> 
 
Defining single-ended/dual-
ended loss measurement 
method 
loss { single-ended |dual-ended}  
[user-data [green-only] [no-ccm] 
[lm-mode {rx | tx-rx }]] 
loss { single-ended |dual-ended} 
[user-data [lm-mode {rx | tx-rx 
}]] 
loss { single-ended |dual-ended} 
[user-data-green [lm-mode {rx | 
tx-rx }]] 
loss single-ended [synthetic 
[lm-mode { rx | tx-rx }]] 
user-data – measures user data 
and CCM messages. Do not use 
user-data on up MEPs in the 
Bridge application. 
green-only – measures green 
packets only, for user data 
single-ended/dual-ended loss 
measurement 
no-ccm – does not include CCMs 
in user data single-ended/dual-
ended loss measurement 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
loss single-ended 
[lmm-synthetic [lm-mode { rx | 
tx-rx }]] 
loss single-ended [slm 
[slm-data-tlv-length <slm-length
-val>] [lm-mode { rx | tx-rx }]  
user-data-green – measures 
green packets only, for user 
data single-ended/dual-ended 
loss measurement 
synthetic – measures DM 
frames; recommended when 
working with devices that do 
not count user data frames 
lmm-synthetic – measures 
synthetic frames as well; 
recommended for working with 
ETX-201A/202A 
slm – measures synthetic 
SLM/SLR frames 
lm-mode – specifies loss 
measurement message mode: 
rx indicates to respond with 
LMR/SLR when LMM/SLM is 
received. 
tx-rx indicates to transmit 
LMMs/SLMs and respond with 
LMR/SLR when LMM/SLM is 
received. 
slm-data-tlv-length – specifies 
length of SLM data TLV.  
Possible values: 0–1800 
(default: 0) 
Note: Green and yellow frames 
are identified by DEI (0=green, 
1=yellow). Therefore, in order 
for color-aware loss 
measurement to function 
properly, you need to do the 
following: 
• Mark green/yellow frames 
by DEI in the Tx flow. 
• Configure ingress-color by 
DEI.  
• Specify no policer for the 
flow. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Configuring collection of 
performance management 
statistics for the destination NE, 
that are presented via the 
RADview Performance 
Management portal 
pm-collection interval 
<seconds> 
Note: In addition to enabling PM 
statistics collection for the 
destination NE, it must be 
enabled for the device. See 
Performance Management. 
Defining the MAC address of the 
destination NE 
remote mac-address <mac> 
If the MAC address is 
00-00-00-00-00-00, the statistic 
counters for the destination NE 
do not increment. 
Defining the remote MEP ID of 
the destination NE 
remote mep-id 
<remote-mep-id> 
 
Displaying the delay 
measurement bins for delay 
measurements via DMRs  
show delay-measurement-bins 
{ rt-delay | rt-delay-var | fw-
delay-var | bw-delay-var } 
current 
show delay-measurement-bins 
{ rt-delay | rt-delay-var | fw-
delay-var | bw-delay-var } 
interval <interval-num> 
show delay-measurement-bins 
{ rt-delay | rt-delay-var | fw-
delay-var | bw-delay-var } all 
Relevant only if profiles were 
assigned via 
delay-measurement-bin, 
delay-var-measurement-bin. 
rt-delay – Round trip delay 
<rt-delay-var> – Round trip 
delay variation 
<fw-delay-var> – Forward delay 
variation 
<bw-delay-var> – Backward 
delay variation 
<current> – Current statistics 
<interval> – Interval statistics 
interval-num> – Interval 
number [number] 
all – all statistics 
Configuring OAM CFM Service Event Reporting 
You can define dedicated event reporting counters to track OAM SLA threshold crossing violations (for 
information on configuring the OAM service thresholds, see Configuring Maintenance Endpoint 
Services). 
In addition to the regular OAM statistics collection, ETX‑2i supports proactive SLA measurements per 
OAM service, as per RMON-based RFC 2819. The device sends reports when one of the counters rises 
above or drops below the set thresholds within the specified sampling period of time. These reports can 
ETX-2i Devices 
8. Monitoring and Diagnostics 
be sent as SNMP traps to the defined network management systems or written to the event log. If an 
event is generated, this action also sends a syslog notification packet, if syslog reporting is active (see 
Syslog for more details). 
The following counters can be monitored: 
Far End Frame Loss Ratio 
Total number of OAM frames lost from local MEP to remote MEP, 
divided by total number of transmitted OAM frames since the service 
was activated 
Near End Frame Loss Ratio 
Total number of OAM frames lost from remote MEP to local MEP, 
divided by total number of transmitted OAM frames since the service 
was activated 
Frames Above Delay 
Number of frames that exceeded delay threshold 
Frames Above Delay Variation (Jitter) 
Number of frames below or equal delay variation threshold 
Far End Unavailability Ratio 
Total number of far end unavailable seconds divided by elapsed time 
since service was activated 
Near End Unavailability Ratio 
Total number of near end unavailable seconds divided by elapsed time 
since service was activated 
For non ratio-based counters (Frames Above Delay and Frames Above Delay Variation), you have to 
define a sampling interval in addition to the rising and falling thresholds. The purpose of the interval is 
to define a timeline, in seconds, in which the service OAM data is sampled and compared with the 
pre-defined service thresholds. For the ratio-based counters, defining a sampling interval is not 
required. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure event reporting for a service: 
1. Navigate to configure fault cfm. 
2. Specify the service and counter for which you wish to configure event reporting: 
service md <mdid> ma <maid> mep <mepid> service <serviceid> {above-delay | 
above-delay-var | far-end-loss-ratio | near-end-loss-ratio | far-end-unavailability-ratio | 
near-end-unavailability-ratio} 
3. Specify the type of event reporting for the counter (see table below): 
 
For counters above-delay and above-delay-var: 
frames-report [event {none | log | trap | logandtrap}] [rising-threshold <rising-threshold>] 
[falling-threshold <falling-threshold>] [sampling-interval <value>] 
 
For counters near-end-loss-ratio or far-end-loss-ratio:  
frames-report [event {none | log | trap | logandtrap}] [rising-threshold {1e-3 | 1e-4 | 1e-5 
| 1e-6 | 1e-7 | 1e-8 | 1e-9 | 1e-10}] [falling-threshold {1e-3 | 1e-4 | 1e-5 | 1e-6 | 1e-7 | 
1e-8 | 1e-9 | 1e-10}] 
 
For counters near-end-unavailability-ratio or far-end-unavailability-ratio: 
frames-report [event {none | log | trap | logandtrap}] [rising-threshold 
<rising-threshold-thousandth>] [falling-threshold <falling-threshold-thousandth>]   
4. Enter no shutdown to activate the event reporting for the counter. 
Parameter 
Description 
Possible Values 
event 
Specifies the type of event reporting 
none – The event is not reported. 
log – The event is reported via the 
event log. 
trap – An SNMP trap is sent to report 
the event. 
logandtrap – The event is reported 
via the event log and an SNMP trap. 
rising-threshold 
falling-threshold 
A value above rising-threshold within the 
sampling interval for the particular event is 
considered as rising event occurred. 
A value below falling-threshold within the 
sampling interval for the particular event is 
considered as falling event occurred. 
For counters above-delay or 
above-delay-var (measured in 
seconds):  
1–60 

## Performing OAM Loopback  *(p.1325)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Description 
Possible Values 
For counters near-end-loss-ratio or 
far-end-loss-ratio:  
1e-3 
1e-4 
1e-5 
1e-6 
1e-7 
1e-8 
1e-9 
1e-10 
For counters 
near-end-unavailability-ratio or 
far-end-unavailability-ratio 
(measured in milliseconds): 
1–1000 
Note: Rising threshold must be 
greater than falling-threshold. 
sampling-interval 
Specifies the interval in seconds over which the 
data is sampled and compared with the rising 
and falling thresholds 
Note:  
• Relevant only for counters 
above-delay or above-delay-var 
• Sampling interval value must be 
at least double rising threshold. 
Performing OAM Loopback 
This diagnostic utility verifies OAM connectivity on Ethernet connections. You can execute the loopback 
according to the destination MAC address or the remote MEP number. 
Note 
The option for remote MEP ID is available only if ETX‑2i can resolve at least 
one remote MEP MAC address. 
 To run an OAM loopback: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, perform the 
required tasks according to the following table. 

## Interval PM File  *(p.1326)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Specifying remote MEP by 
MAC address  
lbm address <mac-address> [repeat 
<repeat-num>] [data-tlv-length 
<length-val>] 
mac-address is in the format 
<xx-xx-xx-xx-xx-xx>. 
The allowed range of 
repeat-num is 1–500. 
The allowed range of 
data-tlv-length is 0–1900. 
Specifying remote MEP by 
MEP ID 
lbm remote-mep <mep-id> [repeat 
<repeat-num>] [data-tlv-length 
<length-val>] 
Sending LBM messages to 
default multicast MAC 
address 
lbm multicast [repeat <repeat-num>] 
The only allowed value for 
repeat-num is 1. 
Checking OAM loopback 
results 
show lbm-results 
 
Interval PM File 
PM tests run continuously to provide current and interval PM statistics. The interval PM file functionality 
provides a file with PM session information (delay and loss) per interval, which is uploaded to an SFTP 
server. These files are plain text files and closed as *.gz archive. 
ETX-2i supports up to 96 intervals that can be between 1 minute and 15 minutes long. 
PM sessions are not automatically included with the file and must therefore be manually included with 
the relevant attributes as outlined. 
 To include a PM session in the interval PM file: 
1. Navigate to the config>oam>cfm>md>ma>mep>service>dest-ne prompt. 
2. Enter interval-pm-file. 
The relevant flow is included with the PM interval file. 
 To exclude the flow from the interval PM file: 
• 
At the config>oam>cfm>md>ma>mep>service>dest-ne prompt, enter no interval-pm-file. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
The PM files include the data listed below. 
Field 
Column# in the PM file 
Description 
Comment 
timestamp 
1 
Epoch Time  
In seconds, since  
01-01-1970, 00:00:00 UTC 
systemName 
2 
Device system name 
Can be configured in 
config>system>name# 
probeName 
3 
SOAM test name 
‘service-name’ taken from the 
MEP Tx flow 
probeIndex 
4 
SOAM probe index value 
Optional parameter 
Test identifier: 
MD#.MA#.MEP#.Pbit.RMEP#, 
such as 1.1.1.5.2 
firmwareVersion 
5 
Device firmware version 
 
manufacturerName 
6 
Device manufacturer name 
 
modelName 
7 
Device model name 
 
neFLRValid 
8 
Near-end FLR loss 
measurement validity  
‘1’: valid 
neFLRSamples 
9 
Received LMRs 
 
neFLR 
10 
Near-end (backward) loss 
ratio 
0-100 
feFLRValid 
11 
Far-end (forward) loss 
measurement validity 
‘1’: valid 
feFLRSamples 
12 
Received LMRs 
 
feFLR 
13 
Far-end (forward) loss ratio 
0-100 
rtDelayValid 
14 
Roundtrip delay 
measurement validity 
 ‘1’: valid 
rtDelaySamples 
15 
Received DMRs 
 
rtMinDelay 
16 
Roundtrip minimum delay 
(microseconds) 
 
rtMaxDelay 
17 
Roundtrip maximum delay 
(microseconds) 
 
rtAvgDelay 
18 
Roundtrip average delay 
(microseconds) 
 
rtDValid 
19 
RTD measurement validity 
 ‘1’: valid 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Field 
Column# in the PM file 
Description 
Comment 
rtDVSamples 
20 
Received DMRs 
 
rtMinDV 
21 
Roundtrip minimum delay 
variation (microseconds) 
 
rtMaxDV 
22 
Roundtrip maximum delay 
variation (microseconds) 
 
rtAvgDV 
23 
Roundtrip average delay 
variation (microseconds) 
 
neDelayValid 
24 
Near-end (backward) delay 
validity 
 
neDelaySamples 
25 
Received DMRs 
 
neMinDelay 
26 
Near-end (backward) 
minimum delay 
(microseconds) 
 
neMaxDelay 
27 
Near-end (backward) 
maximum delay 
(microseconds) 
 
neAvgDelay 
28 
Near-end (backward) average 
delay (microseconds) 
 
neDVValid 
29 
Near-end (backward) delay 
variation validity 
 
neDVSamples 
30 
Near-end (backward) delay 
variation measurement count 
 
neMinDV 
31 
Near-end (backward) 
minimum delay variation 
(microseconds) 
 
neMaxDV 
32 
Near-end (backward) 
maximum delay variation 
(microseconds) 
 
neAvgDV 
33 
Near-end (backward) average 
delay variation 
(microseconds) 
 
feDelayValid 
34 
Far-end (forward) delay 
validity 
 
feDelaySamples 
35 
Received DMRs 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Field 
Column# in the PM file 
Description 
Comment 
feMinDelay 
36 
Far-end (forward) minimum 
delay (microseconds) 
 
feMaxDelay 
37 
Far-end (forward) maximum 
delay (microseconds) 
 
feAvgDelay 
38 
Far-end (forward) average 
delay (microseconds) 
 
feDVValid 
39 
Far-end (forward) delay 
variation validity 
 
feDVSamples 
40 
Received DMRs 
 
feMinDV 
41 
Far-end (forward) minimum 
delay variation 
(microseconds) 
 
feMaxDV 
42 
Far-end (forward) maximum 
delay variation 
(microseconds) 
 
feAvgDV 
43 
Far-end (forward) average 
delay variation 
(microseconds) 
 
The example below illustrates a PM file: 
timestamp,systemName,probeName,probeIndex,firmwareVersion,manufacturerName,modelName,neFLRValid,neFLRSamples,neFLR,feFLRValid,feFLRSamples,feFLR,rtDelayValid,rtDelaySampl
es,rtMinDelay,rtMaxDelay,rtAvgDelay,rtDVValid,rtDVSamples,rtMinDV,rtMaxDV,rtAvgDV,neDelayValid,neDelaySamples,neMinDelay,neMaxDelay,neAvgDelay,neDVValid,neDVSamples,neMin
DV,neMaxDV,neAvgDV,feDelayValid,feDelaySamples,feMinDelay,feMaxDelay,feAvgDelay,feDVValid,feDVSamples,feMinDV,feMaxDV,feAvgDV  
1765197780,ETX-100G_QA_TLV,CNI_1,1.1.1.1.1001,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197780,ETX-100G_QA_TLV,CNI_2,2.2.2.3.1002,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197780,ETX-100G_QA_TLV,CNI_3,3.3.3.5.1003,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197780,ETX-100G_QA_TLV,CNI_4,4.4.4.7.1004,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197840,ETX-100G_QA_TLV,CNI_1,1.1.1.1.1001,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,1,0,0,60,0,1,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197840,ETX-100G_QA_TLV,CNI_2,2.2.2.3.1002,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197840,ETX-100G_QA_TLV,CNI_3,3.3.3.5.1003,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197840,ETX-100G_QA_TLV,CNI_4,4.4.4.7.1004,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,1,0,0,60,0,1,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197900,ETX-100G_QA_TLV,CNI_1,1.1.1.1.1001,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197900,ETX-100G_QA_TLV,CNI_2,2.2.2.3.1002,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197900,ETX-100G_QA_TLV,CNI_3,3.3.3.5.1003,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197900,ETX-100G_QA_TLV,CNI_4,4.4.4.7.1004,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197960,ETX-100G_QA_TLV,CNI_1,1.1.1.1.1001,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197960,ETX-100G_QA_TLV,CNI_2,2.2.2.3.1002,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197960,ETX-100G_QA_TLV,CNI_3,3.3.3.5.1003,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765197960,ETX-100G_QA_TLV,CNI_4,4.4.4.7.1004,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765198020,ETX-100G_QA_TLV,CNI_1,1.1.1.1.1001,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765198020,ETX-100G_QA_TLV,CNI_2,2.2.2.3.1002,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765198020,ETX-100G_QA_TLV,CNI_3,3.3.3.5.1003,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765198020,ETX-100G_QA_TLV,CNI_4,4.4.4.7.1004,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765198080,ETX-100G_QA_TLV,CNI_1,1.1.1.1.1001,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765198080,ETX-100G_QA_TLV,CNI_2,2.2.2.3.1002,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765198080,ETX-100G_QA_TLV,CNI_3,3.3.3.5.1003,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 
1765198080,ETX-100G_QA_TLV,CNI_4,4.4.4.7.1004,6.8.5(1.120),RAD,ETX-2I-100G-4QSFP,0,60,0,0,60,0,0,60,0,0,0,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0,0,60,--,--,--,0,60,0,0,0 

## PM On-Demand Test  *(p.1330)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
PM On-Demand Test 
In addition to proactive, ongoing PM tests which run continuously to provide current and interval PM 
statistics, ETX‑2i supports PM on-demand tests. During on-demand PM tests, ETX-2i transmits a 
preconfigured number of PM frames and issues a report with the results. ETX-2i supports up to 8 
simultaneously active on-demand PM tests for up to 1000 frames per test. ETX-2i keeps up to the 8 last 
completed on-demand test results. 
On-demand tests support the following PM procedures: 
• 
Single-ended user data Loss Measurement Management (LMM) 
• 
Single-ended synthetic Loss Measurement Management (LMM)  
You must set up a Delay Measurement Management (DMM) session when running an on-
demand LMM synthetic test. The DMM interval must be the same as the LMM interval used in 
the on-demand test. 
• 
Synthetic Loss Management (SLM) 
• 
Two-way ETH-DM (DMM) 
On-demand and Pro-active tests cannot be active together. If enabling an on-demand test, pro-active 
tests shut down automatically. 
Service and Destination Network Elements (Dest-NE) must not be changed while the on-demand test is 
running. 
Tests cannot start under the following conditions: 
• 
The Remote MAC is not resolved (sanity check). A Remote MAC not resolved message appears 
in this case. 
• 
Another test of the same type (LM or DM) is already running. 
Test procedure: 
• 
Once the test is enabled, start a training Tx pattern of three consecutive PM tests (LMMs, SLMs, 
DMMs) at rates of 100 ms. 
• 
Once the training phase is complete, the test starts. 
The remote ETX-2i device must be configured as follows: 
Test Type 
ETX-203 Remote MEP 
ETX-2i Remote MEP 
LMM user data 
Dest-NE must be configured with LMM 
Auto LMM (no service needed) 
SLM 
Auto SLM (no service needed), or service and Dest-
NE configured 
Auto SLM (no service needed), or 
service and Dest-NE configured 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Test Type 
ETX-203 Remote MEP 
ETX-2i Remote MEP 
Synthetic LMM 
Service and Dest-NE must be configured with LMM 
synthetic 
Service and Dest-NE must be 
configured with LMM synthetic 
 To set up the on-demand test: 
1. Go to config>oam>cfm>md>ma>mep>service>dest-ne# 
2. Enter on-demand-test and follow the instructions on the command syntax in the table below. 
Command 
Remark 
test-type 
On-demand test type, either loss or delay test 
slm-data-tlv-length 
Set the length of data for the TLV test for SLM 
slm-test-id 
Specify the SLM test ID 
dmm-data-tlv-length 
Specify the length of data for the TLV test for DMM 
duration 
Specify the test duration 
message-interval 
Specify the test PDUs transmit rate 
activate 
Activate the test 
show report 
Show on-demand test results 
 To define the test type: 
1. Go to config>oam>cfm>md>ma>mep>service>dest-ne>on-demand-test# 
2. Enter test-type { loss { user-data | lmm-synthetic | slm } | delay {two-way} } using the relevant 
parameters as explained below. 
loss: Testing for packets that fail to reach the destination using one of the following methods: 
 
user-data: Refers to the actual information being transmitted, which is encapsulated within 
an Ethernet frame's payload. 
 
lmm-synthetic: Using Loss Measurement Management (LMM) messages for Synthetic Loss 
Measurements (SLM). 
 
slm: Synthetic loss management, used to measure the loss of frames and forward the loss 
ratio between two points in a network 
delay: Testing the time it takes for packets to travel from the source to the destination 
according to the following method: 
 
two-way: Bidirectional communication, where data can be sent and received simultaneously 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To define the length of the data for an SLM test: 
1. Go to config>oam>cfm>md>ma>mep>service>dest-ne>on-demand-test# 
2. Enter slm-data-tlv-length <slm-length>.  
The slm-length can be a value between 0 and 1800 seconds and is relevant if the test-type is set 
to delay two-way. The default is 0. 
 To define the SLM test ID: 
1. Go to config>oam>cfm>md>ma>mep>service>dest-ne>on-demand-test# 
2. Enter slm-test-id <test-id#>. 
The slm-test-id can be a number between 1 and 255. The default is 1. 
 To define the length of the data for a DMM test: 
1. Go to config>oam>cfm>md>ma>mep>service>dest-ne>on-demand-test# 
2. Enter dmm-data-tlv-length <dmm-length>. 
The dmm-length can be a value between 0 and 1900 seconds and is relevant if the test-type is 
set to delay two-way. The default is 0. 
 To define the test duration: 
1. Go to config>oam>cfm>md>ma>mep>service>dest-ne>on-demand-test# 
2. Enter duration {count <number>}. 
The duration value is the number of transmitted OAMPDUs during the on-demand test and can 
be a value between 1 and 1000. The default is 100. 
 To define the OAMPDUs transmit rate (test message interval): 
1. Go to config>oam>cfm>md>ma>mep>service>dest-ne>on-demand-test# 
2. Enter message-interval <message interval>. 
The OAMPDU transmit rate defines the interval of the OAMPDU test messages and can be 
100ms, 1s, 10s or 15min. The default is 1s. 
 To activate the PM test: 
1. Go to config>oam>cfm>md>ma>mep>service>dest-ne>on-demand-test# 
2. Enter activate. 
The test is active. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To stop the PM test: 
• 
At the config>oam>cfm>md>ma>mep>service>dest-ne>on-demand-test# prompt, enter  
no activate. 
 To display the on-demand test report: 
1. Go to the config>oam>cfm>md>ma>mep>service>dest-ne>on-demand-test# level. 
2. To view a general test report, enter show report. 
3. To view a detailed test report, enter show report details. 
The examples below illustrate various types of test results. 
Output Format for LOSS 
If a test is in progress, ‘Remaining time’ is displayed and counters are not displayed. 
Test  :  
<  SLM/user data LMM /synthetic LMM / Two-way delay > 
MEP : 
< md/ma/mep > ,     Service <service # >   , dest-ne < dest-ne # >  
Name < name > 
Start time:     <start-time>  
Duration <duration>   / / Remaining Time <remaining time>    :  
 
Tx SLM’s/LMM’s : <tx frames>            / use SLM’s or LMM’s per test type 
Rx SLR’s/LMR’s : <rx frames>              / use SLR’s or LMR’s per test type 
                                         Forward               Backward 
Tx Frames :                    <tx-fwd>               <tx-bkwd> 
Rx Frames :                    <rx-fwd>               <rx-bkwd> 
Lost Frames :                 <lost-fwd>             <lost-bkwd> 
Frame Loss Ratio (%) :  <loss-ratio-fwd>      <loss-ratio-bkwd> 
 
LMR #                   Loss Two Way            Loss Forward                    Loss Backward 
 1                           0                        0                                     0 
 2                           2                        2                                     0 
 3                           2                        2                                     0 
 4                           2                        2                                     0 
 5                           5                        2                                     3 
 6                           5                        2                                     3 
 7                           2                        2                                     0 
 8                           2                        2                                     0 
 9                           5                        2                                     3 
 10                          5                        2                                     3 

## PM File Reporting  *(p.1334)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Output Format for Delay 
If test is in progress ‘Remaining time’ is displayed and counters are not displayed. 
Test  : <  SLM/user data LMM/synthetic LMM / Two-way delay > 
MEP : < md/ma/mep > ,     Service <service # >   , dest-ne < dest-ne # >  
Name < name > 
Start time: <start-time>  
Duration <duration> / Remaining Time <remaining time>    :  
 
Tx DMM’s : <tx frames> 
Rx DMR’s : <rx frames> 
                                                                          Min                                   Average                                        Max 
                                                                       (mSec)                                   (mSec)                                       (mSec) 
Two Way Delay :                                      <min-dly-tw>                      <avg-dly-tw>                            <max-dly-tw> 
Two Way IFDV :                                       <min-ifdv-tw>                      <avg-ifdv-tw>                          <max-ifdv-tw> 
Forward IFDV :                                         <min-ifdv-f>                         <avg-ifdv-f>                              <max-ifdv-f> 
Backward IFDV :                                      <min-ifdv-b>                        <avg-ifdv-b>                             <max-ifdv-b> 
 
Frames Above Delay Threshold :        <frames-above-dly-threshold> 
Frames Above IFDV Threshold :          <frames-above-dly-threshold> 
Test Start and End Alarms 
The example below illustrates the start and the end of an on-demand test 
oamCfmDestNeOnDemandTestStart                on_demand_test_start 
oamCfmDestNeOnDemandTestEnd                  on_demand_test_end 
PM File Reporting 
After generating PM data, this data is written into a file, which is closed as a *.gz archive and then 
uploaded to an SFTP server. By default, a file includes five 15-minute intervals per service (EVC). 
If the SFTP upload fails, two more attempts are made according to the specified interval duration. If 
these attempts fail as well, the file is saved on the ETX device and then uploaded together with the file 
of the next round (by default after one hour).  
Until files are uploaded, they can be viewed using the show file command. A file summary can be 
viewed using the show summary-file command respectively. 
The SFTP upload workflow is illustrated in the diagram below. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
1 hour interval start
n=1
n = n+1
n = last?
Try upload file n
Yes
No
Success?
No
Yes
Success?
Wait 1 minute 
and retry
No
Success?
Wait 1 minute 
and retry
Wait for the next
upload interval
No
Yes
Yes
 
Once the file has been uploaded to the SFTP server, it is deleted from the ETX device and can no longer 
be viewed. 
The file name, the file format and the file extension of a PM file is defined and configured as illustrated 
below: 
[configured-file-prefix]_[device id]_SOAM.Data_[File_closing_date_Format (in UTC):"YYYY-MM-
DD_hh.mm.ss"].[file_extension].gz 
Example: Ocular_TLV1_SOAM.Data_2014-08-15_16.15.00.pm.gz 
The configuration examples in the table use the example above for the file name as relevant. The 
configurable components of the file name in the table are colored according to the example above. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To set up PM file reporting: 
1. Go to config>oam>cfm>pm-file# 
2. Follow the instructions on the command syntax in the table below. 
Command 
Remark 
file-prefix 
Defining the prefix for the PM file, up to 33 characters. 
Syntax: file-prefix <prefix> 
Example: file-prefix TLV1 
file-extension 
Defining the file extension, up to three characters. 
Syntax: file-extension <extension> 
Example: file-extension pm 
pm-intervals 
Defining the number of PM intervals in a file, possible values are 5..96. 
Syntax: pm-intervals <intervals> 
Default: 5 
Example: pm-intervals 8 
server 
Defining the SFTP server to which the files are uploaded. 
Syntax: [no] server <address> username <username> {password <password> [hash] | 
public-key <key-name>} [port <port>] 
Example 1: server 20.20.20.20 username alpha password afgaggag hash port 26 
Example 2: server fil-server-tlv username alpha password afgaggag hash 
Example 3: server file-server-berlin username beta public-key strongarm 
server-directory 
Defining the path for the PM files inside the SFTP server. 
Syntax: server-directory <path on the SFTP server> 
Example: server-directory RAD-RD/CFM 
storage-period 
Defining how many hours PM files are kept before uploading to the SFTP server, possible 
values are 1..48. 
Default: 1 
Syntax: storage-period <hours> 
Example: storage-period 48 
show file 
Displaying the content of a PM file before uploading to the SFTP server. 
Syntax: show file <file-name> 
Example: show file Ocular_TLV1_SOAM.Data_2014-08-15_16.15.00.pm 
show summary-file 
Displaying a list of all PM files that are completed and still in progress (ongoing). 
Syntax: show summary-file 

## Performing OAM Link Trace  *(p.1337)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Command 
Remark 
pause-upload 
Pausing the upload of PM files. Uploads in progress are completed, but no new file is 
uploaded. 
no pause-upload 
Resuming the upload of PM files. 
delete-file 
Deleting a specific file or all of them before they were uploaded to the SFTP server. 
Syntax: delete-file {all | name <file-name>} 
Example 1: delete-file name Ocular_TLV1_SOAM.Data_2014-08-15_16.15.00.pm 
Example 2: delete-file all 
shutdown 
Enabling or disabling the PM file reporting 
Syntax: [no] shutdown 
Default: shutdown 
Enable: no shutdown 
Removing the SFTP 
Server 
no server <address> username <username> {password <password> [hash] | public-key 
<key-name>} [port <port>] 
Performing OAM Link Trace 
This diagnostic utility traces the OAM route to the destination, specified either by the MAC address or 
the maintenance end point (MEP).  
Note 
The option to specify the destination MEP ID is available only if ETX‑2i can 
resolve at least one remote MEP MAC address. 
 To run an OAM link trace: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, perform the 
required tasks according to the following table. 
Task 
Command 
Comments 
Specifying remote MEP by MAC 
address 
linktrace address <mac-address> 
[ttl <ttl-value>] 
mac-address is in the format 
<xx-xx-xx-xx-xx-xx>. 
The allowed range for ttl-value 
is 1–64. This parameter specifies 
the number of hops. Each unit in 
the link trace decrements the 
TTL until it reaches 0, which 
terminates the link trace. 
Specifying remote MEP by ID 
linktrace remote-mep <mep-id> 
[ttl <ttl-value>] 

## Examples  *(p.1338)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Checking the OAM link trace 
results 
show linktrace-results 
 
Examples 
Configuring MD, MA, and MEP 
This example illustrates configuring the following: 
• 
MD ID 1 
• 
MA ID 1 
• 
MEP ID 1:  
 
Remote MEP ID 2 
 
Classification VLAN 100 
 To configure MD, MA, and MEP: 
#**************************Configure MD  
exit all 
configure oam cfm 
maintenance-domain 1 
 
#**************************Configure MA 
maintenance-association 1 
classification vlan 100 
 
#**************************Configure MEP 
mep 1 
classification vlan 100 
bind ethernet 0/1 
queue fixed 1 block 0/1 
remote-mep 1..5,7,15..25,54,68,73..75,80,88..99,100,102,120 
remote-mep 150,160..164,180 
no shutdown 
exit all 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To display the configured MD, MA, and MEP: 
ETX‑2i# configure oam cfm maintenance-domain 1 
ETX‑2i>config>oam>cfm>md(1)# info detail 
    no proprietary-cc 
    md-level  3 
    name  string  "MD1" 
    maintenance-association  1 
        name  string  "MA1" 
        ccm-interval  1s 
        classification vlan  100 
        mep  1 
            bind  ethernet  0/1 
            classification  vlan  100 
            queue  fixed  0 block  0/1 
            remote-mep 1..5,7,15..25,54,68,73..75,80,88..99,100,102,120,150,160..164,180 
            dest-addr-type ccm  multicast pm  unicast 
            ccm-initiate 
            ccm-priority  0 
            forwarding-method  e-line 
            direction  down 
            client-md-level  4 
            no ais 
            no shutdown 
        exit 
    exit 
Configuring Service for Discovery 
This example illustrates configuring a service with MEP and Rx/Tx flows, with the flow and OAM 
parameters configured for service discovery by RADview, and with PM statistics collection enabled for 
the service components, for the RADview PM portal.  
• 
Rx flow parameters: 
 
Ingress port=Ethernet port 0/1, egress port=Ethernet port 0/3 
 
Classification=VLAN 21 
 
Service name=gold 
• 
Tx flow parameters: 
 
Ingress port=Ethernet port 0/3, egress port=Ethernet port 0/1 
 
Classification=VLAN 1 
 
Service name=gold 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
• 
MEP parameters: 
 
MD ID=10 
 
MA ID=10 
 
MEP ID=101 
Note 
VLAN classification must not be configured for the MEP, in order to facilitate 
the service discovery. 
 
Remote MEP ID=20 
 
Service ID=1 
 
Dest NE ID=1 
#**************************Enable PM in device 
exit all 
configure  
  reporting 
    pm 
  exit 
 
#**************************Configure classifiers 
  flows 
    classifier-profile v1 match-any 
      match vlan 1 
    exit 
    classifier-profile v21 match-any 
        match vlan 21 
    exit 
 
#**************************Configure Rx flow 
    flow v21_v1 
        ingress-port ethernet 0/1 
        egress-port ethernet 0/3 queue 0 block 0/1 
        classifier v21 
        pm-collection interval 300 
        service-name gold 
        no shutdown 
    exit 
 
#**************************Configure Tx flow 
    flow v1_v21 
        ingress-port ethernet 0/3 
        egress-port ethernet 0/1 queue 0 block 0/1 
        classifier v1 
        pm-collection interval 300 
        service-name gold 
        no shutdown 
    exit all 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#**************************Configure MEP, service, and dest NE  
configure oam cfm 
  maintenance-domain 10 
    maintenance-association 10 
      mep 101 
        bind ethernet 0/1 
        flow uni-direction rx v21_v1 
        flow uni-direction tx v1_v21 
        queue fixed 0 block 0/1 
        remote-mep 20 
        no shutdown 
          service 1 
            dest-ne 1 
              loss single-ended lmm-synthetic lm-mode tx-rx 
              pm-collection interval 300 
              remote mep-id 20 
            exit 
            no shutdown 
exit all 
Viewing MEP Status (including status of its remote MEPs) 
This example displays MEP status and the address and status of each remote MEP. 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)# show status 
Ingress Port           : Ethernet               0/1 
 
Direction              : Down 
Classification Profile : Class_A 
CCM Priority           : 7 
 
MD Name               : MD1 
MA Name               : MA1 
Administrative Status : Up 
Test Status           : Off 
 
MEP Defect                                          : Status 
Rx LCK                                              : Off 
Rx AIS                                              : Off 
Cross Connected CCM (Mismatch; Unexpected MD Level) : Off 
Invalid CCM (Unexpected MEP; Unexpected CCM Period) : Off 
 
RMEP Type             : Dynamic 
 
Remote MEP  Remote MEP Address  Operational Status 
----------------------------------------------------------------------------- 
4           00-20-D2-2C-97-A9   OK 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing Remote MEP Status 
This example shows the status of a specific Remote MEP. 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)# show remote-mep 4 status 
Remote MEP Address : 00-20-D2-2C-97-A9 
Remote MEP Type: Dynamic 
Operational Status : OK     
Configuring Service and Destination NE 
This section illustrates configuring the following service and destination NE: 
• 
MD ID 1, MA ID 1, MEP ID 1 (from example in Configuring MD, MA, and MEP) 
• 
Service 1 
• 
Destination NE 3 
 To configure service and destination NE: 
exit all 
configure oam cfm ma 1 ma 1 mep 1 
service 1 
  pm-collection interval 900 
  dest-ne 3 
    pm-collection interval 900 
    exit 
  no shutdown 
  exit all 
 To display the configured service and destination NE: 
ETX‑2i# configure oam cfm ma 1 ma 1 mep 1 service 1 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)#info detail    delay-threshold  
1000 
    delay-var-threshold  1000 
    classification priority-bit  0 
    lmm-interval  1s 
    dmm-interval  1s 
    dest-ne  3 
        remote  mac-address  00-00-00-00-00-00 
        delay  two-way data-tlv-length  0 
        loss  single-ended  user-data 
        no delay-measurement-bin  
        no delay-var-measurement-bin  
        pm-collection interval 900 
    exit 
    pm-collection interval 900 
    no shutdown 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuring Service Event Reporting 
This section illustrates configuring OAM CFM event reporting as follows: 
• 
Configure counters for the following service, as shown in the table below: 
 
Maintenance domain 5 
 
Maintenance association 8 
 
MEP 3  
 
Service 4 
The delay and delay variation (jitter) threshold for this service are set to 10 and 5 milliseconds 
respectively. The reporting counters for this service are set as shown in the table below. 
 
Counter 
Event Type 
Rising Threshold 
Falling Threshold 
Sampling Interval 
Frames Above Delay 
Log and trap 
4 
2 
8 
Frames Above Delay Variation 
Log 
10 
5 
30 
Far End Frame Loss Ratio 
Trap 
1e-4   
1e-8 
 
Near End Frame Loss Ratio 
Log and trap 
1e-9   
1e-10 
 
Far End Unavailability Ratio  
Trap 
40 
20 
 
Near End Unavailability Ratio 
Log 
50 
25 
 
In this example, an SNMP trap and an event are generated as notification of the rising threshold if during 
an 8-second sample interval, four DMM packets or more exceed the 10-milliseconds delay threshold of 
this service. The alarm is cleared (falling threshold) if ETX‑2i detects an 8-second sample interval in 
which two or fewer packets cross the thresholds. 
A rising or falling threshold event is generated if a specific ratio is exceeded. For example, an SNMP trap 
is sent if the far end Frame Loss Ratio (from ETX‑2i to the network) exceed 10^-4, i.e., more than one 
frame out of 10,000 LMMs sent for this service are lost. 
 To configure OAM CFM event reporting: 
#************** Define the service delay thresholds 
exit all 
configure oam cfm ma 5 ma 8 mep 3 service 4 
delay-threshold 10 
delay-var-threshold 5 
exit all 
 
#************** Define the service event reporting counters 
#****************** Counter: Frames Above Delay 
ETX-2i Devices 
8. Monitoring and Diagnostics 
configure fault cfm 
service md 5 ma 8 mep 3 service 4 above-delay 
frames-report event logandtrap rising-threshold 4 falling-threshold 2 sampling-interval 8 
no shutdown 
exit 
 
#****************** Counter: Frames Above Delay Variation 
service md 5 ma 8 mep 3 service 4 above-delay-var 
frames-report event log rising-threshold 10 falling-threshold 5 sampling-interval 30 
no shutdown 
exit 
 
#****************** Counter: Far End Frame Loss Ratio 
service md 5 ma 8 mep 3 service 4 far-end-loss-ratio 
frames-report event trap rising-threshold 1e-4 falling-threshold 1e-8 
no shutdown 
exit 
 
#****************** Counter: Near End Frame Loss Ratio 
service md 5 ma 8 mep 3 service 4 near-end-loss-ratio 
frames-report event logandtrap rising-threshold 1e-9 falling-threshold 1e-10 
no shutdown 
exit 
 
#****************** Counter: Far End Unavailability Ratio 
service md 5 ma 8 mep 3 service 4 far-end-unavailability-ratio 
frames-report event trap rising-threshold 40 falling-threshold 20 
no shutdown 
exit 
 
#****************** Counter: Near End Unavailability Ratio 
service md 5 ma 8 mep 3 service 4 near-end-unavailability-ratio 
frames-report event log rising-threshold 50 falling-threshold 25 
no shutdown 
exit all 
 To display the defined service event reporting counters: 
ETX‑2i# configure fault cfm 
ETX‑2i>config>fault>cfm# info detail 
    service md  5 ma  8 mep  3 service  4  above-delay 
        frames-report event  logandtrap rising-threshold  4 falling-threshold  2 
sampling-interval  8 
        no shutdown 
    exit 
    service md  5 ma  8 mep  3 service  4  above-delay-var 
        frames-report event  log rising-threshold  10 falling-threshold  5 sampling-interval  
30 
        no shutdown 
    exit 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
    service md  5 ma  8 mep  3 service  4  far-end-loss-ratio 
        frames-report event  trap rising-threshold  1e-4 falling-threshold  1e-8 
        no shutdown 
    exit 
    service md  5 ma  8 mep  3 service  4  near-end-loss-ratio 
        frames-report event  logandtrap rising-threshold  1e-9 falling-threshold  1e-10 
        no shutdown 
    exit 
    service md  5 ma  8 mep  3 service  4  far-end-unavailability-ratio 
        frames-report event  trap rising-threshold  40 falling-threshold  20 
        no shutdown 
    exit 
    service md  5 ma  8 mep  3 service  4  near-end-unavailability-ratio 
        frames-report event  log rising-threshold  50 falling-threshold  25 
        no shutdown 
    exit 
Viewing MIP Status 
You can display the status of an active MIP. 
ETX-2i>config>oam>cfm>md(1)>mip(1)# show status 
Rx Flow     : Rx_v20 
Bind Port   : Ethernet                         1 
MAC Address : 00-20-D2-53-45-50 
Tx Flow     : Tx_v20 
 
MD Name               : MD1 
MD Level              : 3 
Administrative Status : Up 
Viewing Running Statistics 
ETX‑2i>config>oam>cfm>md(1)>ma(100)# mep 100 
ETX‑2i>config>oam>cfm>md(1)>ma(100)>mep(100)># show statistics running  
Running 
----------------------------------------------------------------------------- 
 
CCM P-bit     : 2                   MD Level  : 3 
CCM Tx frames : 1286 
 
R-MEP 
----------------------------------------------------------------------------- 
ID        CCM Rx frames 
----------------------------------------------------------------------------- 
101       1286 
102       0 
103       0 
ETX‑2i>config>oam>cfm# ma 1 ma 1 mep 1 serv 1  
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)# show statistics running 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Running Counters 
----------------------------------------------------------------------------- 
              Forward              Backward 
TX Frames   : 1548                    1548 
RX Frames   : 1548                    1548 
Lost Frames : 0                          0 
 
Two Way Delay (mSec)         : 0.062 
Two Way IFDV (mSec)          : 0.004 
Frames Above Delay Threshold : 0 
Frames Above IFDV Threshold  : 0 
 
Elapsed Time (sec)           : 31271 
 
Loss and Delay Measurements Messages 
----------------------------------------------------------------------------- 
       Tx                          Rx                                   
LMMs : 31271               LMRs  : 0 
DMMs : 31278               DMRs  : 0 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)# dest-ne 3 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)>dest-ne(3)# show statistics running 
Running Counters 
----------------------------------------------------------------------------- 
                      Forward              Backward 
Tx Frames           : 1759                 1759 
Rx Frames           : 1759                 1759 
Frames Loss         : 0                    0 
Unavailable Seconds : 0                    0 
Available S 
 
Two Way Delay (mSec)         : 0.062 
Two Way IFDV (mSec)          : 0.004 
Current Forward IFDV  (mSec) : 0.002 
Current Backward IFDV (mSec) : 0.002 
Frames Above Delay Threshold : 0 
Frames Above IFDV Threshold  : 0 
 
Elapsed Time (sec)           : 1759 
 
Loss and Delay Measurements Messages 
----------------------------------------------------------------------------- 
       Tx                          Rx 
LMMs : 1759                LMRs  : 1759 
DMMs : 1759                DMRs  : 1760 
Viewing Current Statistics  
ETX‑2i>config>oam>cfm>md(1)>ma(100)# mep 100 
ETX‑2i>config>oam>cfm>md(1)>ma(100)>mep(100)># show statistics current 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Current 
----------------------------------------------------------------------------- 
 
CCM P-bit    : 2                   MD Level  : 3 
Elapsed Time : 135 
CCM Tx frames: 137 
 
R-MEP 
----------------------------------------------------------------------------- 
ID        CCM Rx frames 
----------------------------------------------------------------------------- 
101       136 
102       0 
103       0  
ETX‑2i>config>oam>cfm# ma 1 ma 1 mep 1 serv 1  
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)# show statistics current 
Current 
----------------------------------------------------------------------------- 
                       Forward    Backward 
Tx Frames            : 1863          1863 
Rx Frames            : 1863          1863 
Lost Frames          : 0          0 
Frame Loss Ratio (%) : 0.0000     0.0000 
 
                Min        Average    Max 
                (mSec)     (mSec)     (mSec) 
Two Way Delay : 0.037      0.059      0.084 
Two Way IFDV  : 0.001      0.008      0.036 
Forward IFDV  : 0.000      0.004      0.018 
Backward IFDV : 0.000      0.004      0.018 
 
Frames Above Delay Threshold : 0 
Frames Above IFDV Threshold  : 0 
 
Elapsed Time (sec)           : 721                                               
 
 
Loss and Delay Measurements Messages 
----------------------------------------------------------------------------- 
       Tx                Rx 
LMMs : 722       LMRs  : 0 
DMMs : 722       DMRs  : 0 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)# dest-ne 3 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)>dest-ne(3)# show statistics current 
Current 
----------------------------------------------------------------------------- 
                       Forward              Backward 
Tx Frames            : 739                  739 
Rx Frames            : 739                  739 
Frames Loss          : 0                    0 
Frame Loss Ratio (%) : 0.0000%              0.0000% 
Unavailable Seconds  : 0                    0 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Available Seconds    : 739                  739 
 
Two Way Unavailable Seconds : 0 
Two Way Available Seconds   : 739 
 
                Min        Average    Max 
                (mSec)     (mSec)     (mSec) 
Two Way Delay : 0.037      0.059      0.084 
Two Way IFDV  : 0.001      0.008      0.036 
Forward IFDV  : 0.000      0.004      0.018 
Backward IFDV : 0.000      0.004      0.018 
 
Frames Above Delay Threshold : 0 
Frames Above IFDV Threshold  : 0 
 
Elapsed Time (sec)           : 740 
 
Loss and Delay Measurements Messages 
----------------------------------------------------------------------------- 
       Tx                Rx 
LMMs : 740       LMRs  : 740 
DMMs : 739       DMRs  : 739 
Viewing Interval Statistics 
ETX‑2i>config>oam>cfm>md(1)>ma(100)# mep 100 
ETX‑2i>config>oam>cfm>md(1)>ma(100)>mep(100)># show statistics interval 1 
Interval 
----------------------------------------------------------------------------- 
 
CCM P-bit      : 2                   MD Level  : 3 
Interval       : 1 
Time Stamp     : 28-10-2015                      11:09:59 
Valid Data     : Valid 
Duration (Sec) : 300 
CCM Tx frames  : 303 
 
R-MEP 
----------------------------------------------------------------------------- 
ID        CCM Rx frames 
----------------------------------------------------------------------------- 
101       303 
102       0 
103       0 
ETX‑2i>config>oam>cfm# ma 1 ma 1 mep 1 serv 1  
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)# show statist interval 1 
Interval 
----------------------------------------------------------------------------- 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Interval : 1 
 
                       Forward    Backward 
Tx Frames            : 1541          1541 
Rx Frames            : 1541          1541 
Lost Frames          : 0          0 
Frame Loss Ratio (%) : 0.0000     0.0000 
 
                Min        Average    Max 
                (mSec)     (mSec)     (mSec) 
Two Way Delay : 0.039      0.059      0.083 
Two Way IFDV  : 0.001      0.008      0.036 
Forward IFDV  : 0.000      0.004      0.018 
Backward IFDV : 0.000      0.004      0.018 
 
Loss and Delay Measurements Messages 
----------------------------------------------------------------------------- 
       Tx                Rx 
LMMs : 900       LMRs  : 0 
DMMs : 900       DMRs  : 0 
ETX‑2i>config>oam>cfm>md(1)>ma(2)>mep(1)>service(2)# 
ETX‑2i>config>oam>cfm>md(1)>ma(2)>mep(1)>service(2)# show statistics total-intervals 
 
Total Intervals 
----------------------------------------------------------------------------- 
              Forward    Backward 
Tx Frames   : 0          0 
Rx Frames   : 0          0 
Lost Frames : 0          0 
 
                Min        Average    Max 
                (mSec)     (mSec)     (mSec) 
Two Way Delay : 0.000      0.000      0.000 
Two Way IFDV  : 0.000      0.000      0.000 
 
 
Loss and Delay Measurements Messages 
----------------------------------------------------------------------------- 
       Tx                Rx 
LMMs : 0         LMRs  : 0 
DMMs : 0         DMRs  : 0 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)# dest-ne 3 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)>dest-ne(3)# show statist interval 1 
Interval 
----------------------------------------------------------------------------- 
Interval       : 1 
Valid Data     : Valid 
Time Stamp     : 19-05-2014 10:25:06 
Duration (Sec) : 1195 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
                       Forward              Backward 
Tx Frames            : 899                  899 
Rx Frames            : 899                  899 
Frames Loss          : 0                    0 
Frame Loss Ratio (%) : 0.0000%              0.0000% 
Unavailable Seconds  : 0                    0 
Available Seconds    : 1195                 1195 
 
Two Way Unavailable Seconds : 0 
Two Way Available Seconds   : 1195 
 
                Min        Average    Max 
                (mSec)     (mSec)     (mSec) 
Two Way Delay : 0.039      0.059      0.083 
Two Way IFDV  : 0.001      0.008      0.036 
Forward IFDV  : 0.000      0.004      0.018 
Backward IFDV : 0.000      0.004      0.018 
 
Loss and Delay Measurements Messages 
----------------------------------------------------------------------------- 
       Tx                Rx 
LMMs : 899       LMRs  : 899 
DMMs : 900       DMRs  : 900 
ETX‑2i>config>oam>cfm>md(1)>ma(2)>mep(1)>service(2)>dest-ne(1)# 
ETX‑2i>config>oam>cfm>md(1)>ma(2)>mep(1)>service(2)>dest-ne(1)# show statistics total-
intervals 
 
Total Intervals 
----------------------------------------------------------------------------- 
 
 
                        Forward              Backward 
Tx Frames             : 0                    0 
Rx Frames             : 0                    0 
Frames Loss           : 0                    0 
Frame Loss Ration (%) : 0.0000%              0.0000% 
Unavailable Seconds   : 0                    0 
Available Seconds     : 0                    0 
 
                Min        Average    Max 
                (mSec)     (mSec)     (mSec) 
Two Way Delay : 0.000      0.000      0.000 
Two Way IFDV  : 0.000      0.000      0.000 
Forward IFDV  : 0.000      0.000      0.000 
Backward IFDV : 0.000      0.000      0.000 
 
 
Loss and Delay Measurements Messages 
----------------------------------------------------------------------------- 
       Tx                Rx 
LMMs : 0         LMRs  : 0 
DMMs : 0         DMRs  : 0 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuring and Viewing Delay Measurement Bins 
This section illustrates configuring delay measurement bins as follows: 
• 
Bin1 used for round trip delay measurements, with threshold ranges (in microseconds (μs)):  
 
0–15,000 
 
15,001–49,000 
 
49,001–55,000 
 
55,001–250,000 
 
250,001–5,000,000 
• 
Bin2 used for round trip delay variation measurements, with threshold ranges (in microseconds 
(μs)): 
 
0–15,000 
 
15,001–55,000 
 
55,001–105,000 
 
105,001–205,000 
 
205,001–5,000,000 
 To configure delay measurement bins: 
#*****************Configure delay measurement bin: bin1 
exit all 
config oam cfm  
measurement-bin-profile bin1 
  thresholds 15000,49000,55000,250000 
  exit 
 
#*****************Configure delay measurement bin: bin2 
measurement-bin-profile bin2 
  thresholds 15000,55000,105000,205000 
  exit 
 
#*****************Configure dest NE 3 with the delay measurement bins 
ma 1 ma 1 mep 1 serv 1 dest-ne 3 
delay-measurement-bin profile bin1 
delay-var-measurement-bin profile bin2 
exit all 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To display delay measurement bins: 
ETX‑2i# config oam cfm ma 1 ma 1 mep 1 service 1 dest-ne 3# 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)>dest-ne(3)#show 
delay-measurement-bins rt-delay all 
Type : rt Delay 
 
Current 
 
Bin  range                    Rx DMR 
     (us) 
--------------------------------------------------------------- 
1    0..15000                 0 
2    15001..49000             0 
3    49001..55000             0 
4    55001..250000            0 
5    250001..5000000          0 
 
Type : rt Delay 
 
Interval  Bin  range                    Rx DMR 
               (us) 
--------------------------------------------------------------- 
1         1    0..15000                 36 
1         2    15001..49000             0 
1         3    49001..55000             0 
1         4    55001..250000            0 
1         5    250001..5000000          0 
2         1    0..15000                 753 
2         2    15001..49000             0 
2         3    49001..55000             0 
2         4    55001..250000            0 
2         5    250001..5000000          0 
3         1    0..15000                 713 
3         2    15001..49000             0 
3         3    49001..55000             0 
3         4    55001..250000            0 
3         5    250001..5000000          0 
 
ETX‑2i>config>oam>cfm>md(1)>ma(1)>mep(1)>service(1)>dest-ne(3)# show 
delay-measurement-bins rt-delay-var all 
Type : rt Delay Var 
 
Current 
--------------------------------------------------------------- 
Bin  range                    Rx DMR 
     (us) 
--------------------------------------------------------------- 
1    0..15000                 0 
2    15001..55000             0 
3    55001..105000            0 
4    105001..205000           0 
5    205001..5000000          0 

## Configuration Errors  *(p.1353)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Type : rt Delay Var 
 
Interval  Bin  range                    Rx DMR 
               (us) 
--------------------------------------------------------------- 
1         1    0..15000                 36 
1         2    15001..55000             0 
1         3    55001..105000            0 
1         4    105001..205000           0 
1         5    205001..5000000          0 
2         1    0..15000                 753 
2         2    15001..55000             0 
2         3    55001..105000            0 
2         4    105001..205000           0 
2         5    205001..5000000          0 
3         1    0..15000                 713 
3         2    15001..55000             0 
3         3    55001..105000            0 
3         4    105001..205000           0 
3         5    205001..5000000          0 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
OAM CFM: A service with the 
same priority already exists 
You tried to configure more 
than one service on the same 
priority bit. 
Check the priority bit classification and 
verify that there is no other configured 
service on it. 
OAM CFM: A Maintenance 
Association with this format and 
name already exists 
You previously configured 
another MA with the same 
configuration. 
Configure the MA with another name or 
format. 
OAM CFM: A Maintenance 
Domain with this format name 
and level already exists 
You previously configured 
another MD with the same 
configuration. 
Configure the MD with another format, 
name, or level. 
OAM CFM: Active MEP cannot 
work without a flow 
You tried to delete or shut 
down a flow that is being used 
by a MEP. 
Disassociate the flow from the MEP, and 
then delete or shut down the flow. 
OAM CFM: Active MEP requires 
at least 1 remote MEP 
You did not configure a single 
remote ID on the MEP. 
Configure at least one remote MEP. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
OAM CFM: Active MIP cannot 
work without a flow 
You did not configure a TX or Rx 
flow on the manual MIP that 
you configured. 
Configure a TX or Rx flow on the manual 
MIP that you configured. 
OAM CFM: Active MIP cannot 
work without an active flow 
The Tx or RX flow that you 
configured on the MIP is not 
active. 
Configure the MIP with an active Tx or 
Rx flow. 
OAM CFM: AIS cannot be enabled 
when MD level equals seven (7) 
You configured MEP on a 
maintenance Domain with Level 
7, and therefore AIS could not 
be enabled on it. 
Configure MEP on a maintenance 
Domain other than Level 7. 
OAM CFM: Cannot activate a 
service without a dest-NE 
You tried to activate a Service 
that has no Dest NE configured 
under it. 
Configure a Dest NE under Service. 
OAM CFM: Cannot activate MIP 
without a bound port 
You did not configure a bound 
port on a manual MIP. 
Configure a bound port on the manual 
MIP. 
OAM CFM: Cannot change 
parameters when active    
You tried to change parameters 
on an active Fault CFM entity. 
Disable Fault CFM entity, and then 
change parameters. 
OAM CFM: Cannot change pm to 
multicast because there is a 
destne that counts loss     
You tried to configure a 
multicast destination address 
on a Dest NE that has user data 
loss measurements. 
Configure a multicast destination 
address on a Dest NE that does not have 
user data loss measurements. 
OAM CFM: Cannot configure 
destination address type unicast 
and more than one remote MEP  
You configured a MEP to work 
with unicast destination 
address, but also assigned to it 
more than one remote MEP. 
Configure only one remote MEP per 
MEP.  
OAM CFM: Cannot configure ICC 
with MD name    
It is not legal to configure MD 
name when MA name format is 
ICC. 
Change MA name to format other ICC. 
OAM CFM: Cannot delete a 
remote MEP that is being used by 
a dest-ne    
You tried to delete a remote 
MEP from MEP configuration, 
while this remote MEP is being 
used in one of the MEP’s Dest 
NEs as remote peer address. 
Disassociate the remote MEP from the 
Dest NE and then delete it. 
OAM CFM: Cannot delete destne; 
it is bound to rfc2544 test. 
You tried to delete or shut 
down a Dest NE that is used on 
an active RFC2544 test. 
Wait until RFC2544 test has completed, 
and then delete or shut down the Dest 
NE. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
OAM CFM: Cannot delete MEP; 
MEP is under Y.1564 test. 
You tried to delete a MEP which 
is being used in a Y.1564 test. 
Finish using the MEP under the Y.1564 
test, and then delete it. 
OAM CFM: Cannot delete or 
change measurement profile   
first remove from dest-NE 
You tried to modify or delete a 
used Bin profile.  
Remove the Bin profile from the Dest 
NE, and then modify or delete it. 
OAM CFM: Cannot enable loss 
measurement because pm is in 
multicast 
You tried to configure user data 
loss measurements on a Dest 
NE with multicast destination 
address. 
Configure Dest NE without a multicast 
address or use another loss 
measurement method. 
OAM CFM: Cannot enable service 
while the MEP is not active 
You are trying to enable (no 
shutdown) a service of one of 
the MEP’s priority bits, while 
the MEP is not enabled 
(shutdown). 
Enable the MEP (no shutdown). 
OAM CFM: Cannot have a dest-
NE remote MEP-ID when CCM is 
disabled    
You tried to configure remote 
MEP Id on the Dest NE while 
MEP’s CCM is not active. 
Activate MEP’s CCM or use remote-mac. 
OAM CFM: Cannot modify a 
remote MEP while it is being used   
You tried to change remote 
MEP parameters in MEP 
configuration while the Remote 
MEP is being. used  
Shut down the service, delete the Dest 
NE that uses this remote MEP or change 
its configuration to remote MAC. 
OAM CFM: Cannot resolve this 
remote MEP MAC address 
You are using remote MEP ID 
for loopback or linktrace 
transmission, but the remote 
MEP MAC address was not 
learned by the CCM yet. 
Use a remote MEP ID only of remote 
MEP MAC address that was learned by 
the CCM. 
OAM CFM: Cannot send more 
than one LB to multicast address 
You sent more than one 
loopback message to the same 
multicast destination address of 
the MEP. All relevant remote 
MEPs should answer – one LBR 
from every remote MEP. 
Send only one LB message to multicast 
address. 
OAM CFM: Cannot shutdown 
MEP; MEP is under Y.1564 test. 
You tried to disable a MEP 
which is being used in a Y.1564 
test. 
Finish using the MEP under the Y.1564 
test and then disable it.  
OAM CFM: Classification: Conflict 
with another MEP classification 
You previously configured 
another MEP with the same 
parameters. 
Configure the MEP with a different 
classification. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
OAM CFM: Classification: Inner 
VLAN range is not supported    
You tried to configure a MEP 
with a non-supported flow 
classification. 
Configure the MEP with a supported 
flow classification. 
OAM CFM: Classification: 
Unsupported criteria    
You tried to configure a MEP 
with a non-supported flow 
classification. 
Configure the MEP with a supported 
flow classification. 
OAM CFM: Classification: VID=0 is 
invalid    
You configured an Illegal VLAN 
on a MEP. 
Configure a VLAN with ID other than 0 
on the MEP. 
OAM CFM: Client MD level must 
be higher than MD level    
You tried to configure a client 
Maintenance Domain Level 
(MDL) lower than or equal to 
the MDL. 
Configure client MD level higher than 
MD level.    
OAM CFM: Conflict between 
OAM destination MAC address 
and device MAC address 
You configured a destination 
MAC address, which conflicts 
with the device’s MAC address. 
Select a valid destination MAC address. 
OAM CFM: Deactivate service 
before erasing last dest-NE   
You did not deactivate service 
before erasing last active Dest 
NE under it. 
Deactivate service, and then erase last 
active Dest NE under it. 
OAM CFM: dest-NE out of range    
You configured Dest NE ID out 
the range 1..255. 
Confiugre a Dest NE ID between 1 and 
255.  
OAM CFM: EVC.COS: Illegal 
remote MEP configuration  
You did not configure Local 
MEP Id (can only occur via 
SNMP). 
Configure Local MEP Id. 
OAM CFM: EVC.COS: More than 1 
MEP on the same MA is only 
allowed when all classifications 
are VLAN + pBit    
You tried to configure two 
MEPs on the same MA. 
Configure only one MEP on the same 
MA or use vlan+ pBit classification for all 
MEPs on MA. 
OAM CFM: EVC.COS: Priority bit 
doesn't match classifier    
You did not configure EVC.cos 
MEP’s flow classification to 
match the MEP’s configured 
priority. 
Configure the EVC.cos MEP’s flow 
classification to match the MEP’s 
configured priority. 
OAM CFM: EVC.COS: Two MEPs 
on the same MA must use 
classifiers with same VLAN and 
different priorities    
You tried to configure two 
MEPs on the same MA with the 
same priority.  
Configure two MEPs on the same MA 
with different priorities. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
OAM CFM: Event type must be 
different than none    
You tried to configure for 
unavailability, a Fault CFM 
frame report entity that has no 
event. 
Configure an event for the Fault CFM 
frame report entity. 
OAM CFM: Exceeded number of 
entries in alarmTable    
You tried to define more than 
100 fault CFM entities. 
Define only up to 100 fault CFM entities. 
OAM CFM: Falling 
alarm_threshold must be less 
than rising alarm_threshold    
On Fault CFM entity, you 
configured a lower limit for 
alarm falling, which is higher 
than the higher limit of alarm 
rising. 
Configure a lower limit for alarm falling, 
which is lower than the higher limit of 
alarm rising. 
OAM CFM: FPGA supports up to 
1000000 uSec (1 second) 
threshold    
You tried to configure the Bin 
profile limit which is higher 
than 1 second.  
Configure a Bin profile limit which is up 
to 1 second. 
OAM CFM: Illegal change of 
bounded port    
You tried to change the 
bounded port from a Bridge 
Port to a regular port or vice 
versa. 
 
OAM CFM: Illegal MAC address 
You configured the MAC 
address with all zeroes or all 
ones.  
Configure a valid MAC address. 
OAM CFM: Illegal queue block    
You did not configure a queue 
block on the MEP. 
Configure a queue block on the MEP. 
OAM CFM: Illegal value    
CFM entity was configured with 
illegal or out of range indices 
(for example, loopback on an 
active CFM loopback). 
Configure CFM entity with legal indices. 
OAM CFM: Invalid falling 
threshold     
You configured the falling 
threshold to less than one-of-
thousand or higher than 1000 
one-of-thousand. Or you 
configured the falling threshold 
to a higher value than the rising 
threshold.    
Configure the falling threshold between 
one-of-thousand and 1000 one-of-
thousand. Make sure that the falling 
threshold value is lower than the rising 
threshold.    
OAM CFM: Invalid forwarding 
method for MEP with direction 
set to down     
 
You configured E-LAN 
forwarding method on a Down 
MEP. 
Configure another forwarding method. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
OAM CFM: Invalid rising 
threshold     
You configured the rising 
threshold to less than one-of-
thousand or higher than 1000 
one-of-thousand. Or you 
configured the rising threshold 
to a lower value than the falling 
threshold.    
Configure the rising threshold between 
one-of-thousand and 1000 one-of-
thousand. Make sure that the rising 
threshold value is higher than the falling 
threshold.    
OAM CFM: Invalid time interval     
You tried to configure a fault 
CFM interval which is shorter 
than 1 second or longer than 60 
seconds. 
Configure an interval between 1 and 60 
seconds. 
OAM CFM: Lmm and dmm 
intervals must be equal if lmm-
synthetic was selected     
You configured lmm-synthetic 
while in the service level, but 
you also set lmm or dmm 
intervals to be different than 1 
second. 
Configure one second on both lmm and 
dmm. 
OAM CFM: Local MEP-ID and 
remote MEP-ID are equal 
You assigned the same ID to a 
remote MEP and local MEP. 
Configure the remote MEP and local 
MEP with different IDs. 
OAM CFM: MA and MEP VLAN 
don't match    
You configured a classification 
VLAN on MA level that does not 
match the configured 
classification VLAN on the MEP 
level. 
Configure a classification VLAN on the 
MA level to match the configured 
classification VLAN on the MEP level. 
OAM CFM: MA name max length 
is 13 characters when format is 
ICC    
You configured an MA name in 
ICC format more than 13 
characters long. 
Configure an MA name in ICC format up 
to 13 characters long. 
OAM CFM: MA-ID size exceeds 
limit 
You defined an MD or MA name 
length that is longer than the 
maximum allowed length. 
Define an MD or MA name that is not 
longer than the maximum allowed 
length. 
OAM CFM: Max allowed dest-NEs 
in active services already reached 
You tried to add more than 
allowed maximum Dest NEs.  
Configure up to the allowed number of 
Dest NEs. 
OAM CFM: Max allowed number 
of remote MEPs reached 
You already configured the 
maximum allowed number of 
remote MEPs on the device. 
Configure up to the allowed number 
remote MEPs per device. 
OAM CFM: MD level out of range 
You configured an MD level that 
is smaller than 0 or bigger than 
7 (can happen only via SNMP). 
Configure an MD level between 0 and 7. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
OAM CFM: MEP direction is not 
correct for port type 
You bound the MEP to the 
wrong port. For example: You 
bound a Down MEP to a Bridge 
port or an UP MEP to an SVI.  
Bind a MEP of the correct direction to a 
port.  
OAM CFM: MEP must be active 
for this action 
You tried to send LBM or LTM 
on a non-active MEP. 
Activate MEP, and then send LBm or 
LTM. 
OAM CFM: MEP out of range    
You configured a MEP ID 
outside the range 1..8191 
Configure a MEP ID between 1 and 
8191. 
OAM CFM: Name cannot be 
empty 
 You did not configure an MD or 
MA name. 
Configure a name for MD or MA. 
OAM CFM: Name length too long 
You configured an illegal MD or 
MA name length (more than 43 
characters). 
Configure an MD/MA name up to 43 
characters. 
OAM CFM: NE remote MEP-ID or 
MAC address conflicts with 
another NE on the current service 
You tried to define Dest NE that 
has same indices as an existing 
Dest NE. 
Define a Dest NE that has different 
indices than an existing Dest NE. 
OAM CFM: No port is bound to 
MEP 
You tried to activate a MEP with 
no bounded port. 
Bind a port to the MEP. 
OAM CFM: Only 10 TX flows per 
MEP are allowed 
You tried to configure more 
than 10 Tx flows on a MEP.  
Configure up to 10 Tx flows. 
OAM CFM: Only one destne can 
be configured if loss user data 
was selected 
You tried to configure more 
than one Dest NE on a service 
with User Data Loss 
measurement method.  
Configure only one Dest NE on a service 
with User Data Loss measurement 
method. 
OAM CFM: Only one RX flow per 
MEP is allowed 
You tried to configure more 
than one Rx flow on a MEP. 
Configure only one Rx flow on the MEP. 
OAM CFM: Please make sure you 
configure a unicast type and MAC 
address when MEP is shutdown  
You configured a MEP to work 
with unicast destination 
address but did not configure a 
valid unicast address as 
destination address. 
When MEP is shutdown, configure a 
valid unicast address as destination 
address. 
OAM CFM: Port is occupied with 
another action 
You tried to send loopback or 
linktrace while there is another 
active loopback or linktrace 
respectively. 
Send loopback or linktrace only when no 
other loopback or linktrace respectively, 
is active. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
OAM CFM: Port level MEP: Only 
one allowed per port    
You tried to configure more 
than one MEP on an untagged 
port. 
Configure only one MEP on an untagged 
port. 
OAM CFM: Priority out of range 
You configured a Priority that is 
smaller than 0 or bigger than 7 
(can happen only via SNMP). 
Configure a Priority between 0 and 7. 
OAM CFM: Profile must have only 
one entry 
You tried to use a flow with 
multiple VLANs matching 
classification. 
Use a flow with only one VLAN matching 
classification. 
OAM CFM: Profile was not found 
You used a wrong or non-
existing profile. 
Use a correct or existing profile. 
OAM CFM: Remote MEP doesn't 
exist 
You tried to configure a remote 
MEP Id at the Dest NE, as 
remote peer address, but this 
Remote MEP Id is not 
configured at the MEP as 
Remote. 
Configure the remote MEP ID at the 
MEP as Remote.  
OAM CFM: Remote MEP ID 
cannot be equal to local MEP ID    
You tried to configure a remote 
MEP with the same ID as the 
MEP itself. 
Configure the remote MEP with an ID 
that is different than the MEP ID. 
OAM CFM: rfc2544 test is in 
progress; cannot enable service 
You tried to change the status 
of a service that one of its Dest 
NEs is used on an active 
RFC2544 test.  
Wait until RFC2544 test terminates and 
then change the service’s status.  
OAM CFM: Service out of range 
You configured a service ID 
outside the range 1..8 
Configure a service ID between 1 and 8. 
OAM CFM: The Rx and Tx flows 
must be in opposite directions. 
You configured Rx and Tx flows 
so that they do not start and 
end on opposite Ingress and 
Egress ports. 
Configure Rx and Tx flows to start and 
end on opposite Ingress and Egress 
ports. 
OAM CFM: The Rx flow must 
originate from the bound port.     
You configured manual MIP, so 
that Rx flow’s Ingress port is not 
equal to the MIP’s bound port.   
Configure the Rx flow’s Ingress port to 
be equal to the MIP’s bound port. 

## Viewing the MEF46 Latching Loopback Status  *(p.1361)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
OAM CFM: There is no MEP with 
those indices 
You tried to create an entry in 
the MepFlow table and to 
connect between a flow and a 
MEP that does not exist (can 
only occur via SNMP). 
Connect the flow to a MEP that already 
exists. 
OAM CFM: VID out of range    
You configured a VLAN ID 
outside the range 1..4094 
Configure a VLAN ID between 1 and 
4094. 
OAM CFM: When using untagged 
or EVC.COS MEP classification 
only service index 1 is permitted 
You tried to configure a MEP 
with EVC.cos classification and 
Service Id other than 1. 
Configure a MEP with EVC.cos 
classification and Service Id equal to 1. 
OAM CFM: MEF-46 should have 
Tx/Rx flow classification 
You tried to configure MEF-46 
on a MEP that is configured 
with a classifier profile or VLAN.  
Configure MEF-46 on a MEP that is 
configured with Rx and Tx flows. 
Viewing the MEF46 Latching Loopback Status 
You can view the MEF46 Latching Loopback (LL) status of an MEF-46 enabled MEP that is configured 
with Rx and Tx flows. 
 To display the MEF46 LL status: 
• 
In the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, enter  
show mef46-ll-status. 
The status screen appears. For information on the MEF46 LL status values, see the following 
table. 
ETX-2i>config>oam>cfm>md(1)>ma(1)>mep(2)# show mef46-ll-status 
Administrative Status : Up 
 
Rx Unicast LLMs    : 2 
Rx Multicast LLMs  : 0 
Rx Discarded LLMs  : 0 
Tx LLRs            : 2 
Tx Autonomous LLRs : 0 
 
Num  First Source MAC Address  Last Source MAC Address   Time Remaining 
----------------------------------------------------------------------------- 
1    00-20-D2-54-11-92                                   00:06:43 
 
ETX-2i config>oam>cfm>md(1)>ma(1)>mep(2)# 

## Viewing OAM CFM Statistics  *(p.1362)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter Displayed 
Description 
Administrative Status 
Current status of the LLF 
Possible values: Up, Down 
Note: The parameters of this report are only displayed when Administrative Status 
is Up. 
Rx Unicast LLMs 
Number of unicast LLM PDUs received by the LLF 
Rx Multicast LLMs 
Number of multicast LLM PDUs received by the LLF 
Rx Discarded LLMs 
Number of invalid LLM PDUs discarded by the LLF 
Tx LLRs 
Number of LLR PDUs sent by the LLF 
Tx Autonomous LLRs 
Number of autonomous LLR PDUs sent by the LLF. An autonomous LLR has a 
response code of Timeout or Prohibited. 
First Source MAC Address 
Start of a block of source MACs in incoming frames that are looped 
Last Source MAC Address 
End of a block of source MACs in incoming frames that are looped 
Time Remaining 
Time remaining until deactivation of the loop 
Viewing OAM CFM Statistics 
You can display end-to-end performance monitoring data for the MEPs, OAM services, and destination 
NEs. The statistics for a service are calculated from the statistics for its destination NEs. 
ETX‑2i measures performance in fixed intervals (the interval length can be configured by the 
interval-duration command). 
You can view the following types of statistics for MEPs, services, and destination NEs: 
Running 
OAM statistics collected since the corresponding service was activated 
Current 
OAM statistics for the current interval 
Interval 
OAM statistics for a selected interval. You can select an interval only if it has already ended 
since the corresponding service was activated. 
When a service is first activated, you can view statistics for only the current interval. The statistical data 
is shown for the time elapsed since the beginning of the interval. When the current interval ends, it 
becomes interval 1 and you can select it for viewing interval statistics. After each interval ends, you can 
select it for viewing interval statistics. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
OAM CFM supports checking Availability status within an interval as well as across intervals. In the case 
that there are less than n consecutive delta-t small time intervals at the end of an interval that have 
changed Availability status (become Available or Unavailable), the delta-t small time intervals at the 
beginning of the next interval are checked to see if there is a total of n consecutive delta-t small time 
intervals across the intervals (the end of the current interval and the beginning of the next interval). If 
so, the delta-t small time intervals at the end of the current interval are all considered to have a changed 
Availability status (Available or Unavailable).  
For example, when Availability is defined for ten one-second intervals, and there are three SES seconds 
at the end of the current interval, those seconds are considered Unavailable only if the first seven 
seconds of the next interval are also SES, i.e., ten consecutive SES.  
An interval is closed only after the following Availability and Unavailability counters are updated 
accordingly, taking into consideration the Availability status change of Delta-t’s in the current interval 
that are affected by the Availability status of Delta-t’s in the new interval (see OAM Statistic Counters 
table below for a description of the counters):   
• 
Tx Frames [Forward] 
• 
Tx Frames [Backward] 
• 
Rx Frames [Forward] 
• 
Rx Frames [Backward] 
• 
Unavailable Seconds [Forward] 
• 
Unavailable Seconds [Backward] 
• 
Frame Loss Ratio (%) [Forward] 
• 
Frame Loss Ratio (%) [Backward] 
Also, the statistics of the last History interval (i.e., the interval before the current) can only be viewed n * 
Delta_t seconds after the current interval has commenced. 
 To configure the OAM CFM statistics interval in minutes: 
• 
At the config>system prompt, use the interval-duration command as specified: 
interval-duration { 1 | 5 | 10 | 15 } 
Note 
• 
If RADview is being used to manage ETX‑2i, then when the interval 
duration is changed, it is recommended to clear the statistics of all 
relevant Dest NEs, in order to avoid any inconsistencies. 
• 
interval-duration must be configured to a larger value than availability 
(delta_t * n) calculation; otherwise, a sanity error occurs. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To display the OAM CFM statistics for a MEP, service, or destination NE: 
1. Navigate to the level corresponding to the OAM MEP, service, or destination NE for which you 
wish to view the statistics  
configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid>   
or  
configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid> service <serviceid>  
or  
configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid> service <serviceid> dest-ne <dest-ne-index>). 
2. Perform the required tasks according to the following table. 
Note 
The service for which you wish to view the statistics must be active. If the 
service is not active, the commands to view statistics are not recognized. 
 
Task 
Command 
Comments 
Viewing running 
statistics 
show statistics 
running 
The statistics are displayed as shown in Viewing Running Statistics; 
see the following two tables. 
Viewing statistics 
for the current 
interval 
show statistics 
current 
The statistics for the current interval are displayed as shown in 
Viewing Current Statistics; see the following two tables.   
Viewing the 
statistics for a 
selected interval 
show statistics 
interval 
<interval-num> 
Allowed values for interval-num: 1–48 
The statistics for the selected interval are displayed as shown in 
Viewing Interval Statistics; see the following two tables. 
If you specified an interval that has not yet ended since the service 
was activated, a message is displayed that the interval doesn’t exist. 
Viewing running 
statistics, 
statistics for the 
current interval, 
and statistics for 
all intervals 
show statistics all 
The statistics are displayed as shown in Viewing Running Statistics, 
Viewing Current Statistics, Viewing Interval Statistics; see the 
following two tables. 
Viewing statistics 
for all intervals 
show statistics 
all-intervals 
The statistics for all intervals are displayed as shown in Viewing 
Interval Statistics; see the following two tables. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Clearing the 
statistics for the 
service or 
destination NE 
clear-statistics 
The running statistics for the MEP, service, or destination NE are 
cleared (the interval and current counters are not cleared). 
 
OAM Statistic Counters 
Parameter 
Description 
Tx Frames [Forward] 
Total number of frames transmitted from local destination NE to remote 
destination NE since the service was activated  
Note: Counts Tx frames during Available time only. 
Tx Frames [Backward] 
Total number of frames transmitted from remote destination NE to local 
destination NE since the service was activated  
Note: Counts Tx frames during Available time only. 
Rx Frames [Forward] 
Total number of frames received by remote destination NE since the 
service was activated  
Note: Counts Rx frames during Available time only. 
Rx Frames [Backward] 
Total number of frames received by local destination NE since the 
service was activated 
Note: Counts Rx frames during Available time only. 
Lost Frames [Forward] (in service 
statistics) 
Frames Loss [Forward] (in dest-ne 
statistics) 
Total number of frames lost from local destination NE to remote 
destination NE since the service was activated   
Note: This counter is called Lost Frames for Services, and Frames Loss 
for dest NEs. 
Lost Frames [Backward] (in service 
statistics) 
Frames Loss [Backward] (in dest-ne 
statistics) 
Total number of frames lost from remote destination NE to local 
destination NE since the service was activated  
Note: This counter is called Lost Frames for Services, and Frames Loss 
for dest NEs. 
Frame Loss Ratio (%) [Forward] 
Lost Frames [Forward] divided by Tx Frames [Forward] 
Note: Counts FLR during Available time only. 
Frame Loss Ratio (%) [Backward] 
Lost Frames [Backward] divided by Tx Frames [Backward] 
Note: Counts FLR during Available time only. 
Unavailable Seconds [Forward] 
Number of seconds the remote destination NE is considered unavailable  
Note: This counter is displayed only for dest NEs. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Description 
Unavailable Seconds [Backward] 
Number of seconds the local destination NE is considered unavailable  
Note: This counter is displayed only for dest NEs. 
Available Seconds [Forward] 
Number of seconds the remote destination NE is considered available 
Note: This counter is displayed only for dest NEs. 
Two Way Unavailable Seconds 
Number of seconds that either the remote destination NE (forward) 
and/or local destination NE (backward) are unavailable. 
Note: This counter is displayed only for dest NEs current and interval 
statistics. 
Available Seconds [Backward] 
Number of seconds the local destination NE is considered available 
Note: This counter is displayed only for dest NEs. 
Two Way Available Seconds 
Number of seconds that both the remote destination NE (forward) and 
local destination NE (backward) are available. 
Note: This counter is displayed only for dest NEs current and interval 
statistics. 
Two Way Delay (mSec)  
Round trip frame delay  
Two Way IFDV (mSec) 
Round trip frame delay variation 
Current Forward IFDV (mSec) 
Difference between the current delay value and the previous current 
delay value, for forward direction Note: This counter is displayed only 
for dest NEs. 
Current Backward IFDV (mSec) 
Difference between the current delay value and the previous current 
delay value, for backward direction Note: This counter is displayed only 
for dest NEs. 
Frames Above Delay Threshold 
Number of DM frames whose delay value exceeded the configured 
delay threshold 
Frames Above IFDV Threshold 
Number of DM frames whose delay variation exceeded the configured 
delay variation threshold  
Two Way Delay (msec) [Min] 
Minimum frame delay value received in DM frame 
Two Way Delay (mSec) [Average] 
Average of all frame delay values received in DM frames 
Two Way Delay (msec) [Max] 
Maximum frame delay value received in DM frame 
Two Way IFDV (msec) [Min] 
Minimum difference between the frame delay values received in DM 
frames 
Two Way IFDV (mSec) [Average] 
Average difference between the frame delay values received in DM 
frames 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Description 
Two Way IFDV (msec) [Max] 
Maximum difference between the frame delay values received in DM 
frames 
Forward IFDV [Min] 
Minimum difference between the frame delay values received in DM 
frames for forward direction 
Forward IFDV [Average] 
Average difference between the frame delay values received in DM 
frames for forward direction 
Forward IFDV [Max] 
Maximum difference between the frame delay values received in DM 
frames for forward direction 
Backward IFDV [Min] 
Minimum difference between the frame delay values received in DM 
frames for backward direction 
Backward IFDV [Average] 
Average difference between the frame delay values received in DM 
frames for backward direction 
Backward IFDV [Max] 
Maximum difference between the frame delay values received in DM 
frames for backward direction 
Elapsed Time (sec)   
Time (in seconds) elapsed since the service was activated. 
Exception: Following shutdown and then no shutdown of a service, 
current statistics of the first interval display in Elapsed Time the time 
that is aligned to the wall clock, and not the elapsed time since the 
service was activated. Hence, all current statistics calculated using 
Elapsed Time are not valid for the first interval following shutdown and 
no shutdown.  
CCM P-bit 
P-bit where CCM resides 
MD Level 
MD level number where CCM resides 
CCM Tx frames 
Number of CCM Tx frames per MEP 
RMEP ID 
The ID of the remote MEP associated with the MEP 
CCM Rx frames 
Number of CCM Rx frames per remote MEP 
OAM Delay and Loss Measurement Counters  
Parameter 
Description 
Tx LMMs 
Number of transmitted loss measurement messages 
Tx DMMs 
Number of transmitted delay measurement messages 
Rx LMRs 
Number of received loss measurement replies 
Rx DMRs 
Number of received delay measurement replies 