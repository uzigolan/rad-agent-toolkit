# 8 Resiliency and Optimization

*Manual `ETX-1p_6.4_Mn_05-26_GA.pdf`, pages 604–628.*


## 8.1 Ethernet Ring Protection (ERP)  *(p.604)*

8. Resiliency and Optimization 
8 Resiliency and Optimization 
This chapter describes features related to resiliency and optimization: 
• 
Fault Propagation 
• 
Link Redundancy 
 
8.1 Ethernet Ring Protection (ERP)  
A G.8032 Layer-2 Ethernet ring, a logical ring defined above a bridge, protects against link and node 
failures.  
Applicability and Scaling 
This feature is applicable to all devices. 
The device supports a single ring.  
The ring needs a VLAN-aware bridge. If the bridge is VLAN-unaware the configuration is accepted but 
the ring will not work – until a VLAN-aware bridge is configured. 
Standards Compliance 
ITU-T G.8032/Y.1344 (03/2020) 
Functional Description 
Ethernet Ring Protection (ERP) technology provides a solution for traffic protection and rapid service 
restoration. It is built on traditional Ethernet bridging functionality.  
8. Resiliency and Optimization 
ERP rings provide layer 2 protection by connecting devices in a ring. Each ring has east and west ports, 
bound to bridge ports, and traffic is forwarded from device to device (from the east to the west of each, 
and vice versa). Traffic is also terminated by each device according to the bridge VLAN configuration. 
A ring can be configured on any Ethernet port.  
The ring supports only ERPv2, without backward compatibility. 
Currently ERP always works in revertive mode (this mode is set in the RPL owner), which means that 
after recovering from a failure, the ring would revert to its original state. 
Ring Data VLANs 
The ring only protects data VLANs, and only on the east and west ports. VLANs on the east and west 
ports can only be configured by the ring commands. VLANs on other bridge ports (including data and R-
APS VLANs) may be configured with the bridge commands. They are handled by the bridge and the ring 
is unaware of them. 
If a user configures a data VLAN that does not exist in the device, the device will configure that VLAN 
and associate the east and west ports with it.  
If the user deletes a data VLAN, the device will disassociate the east and west ports from it, but will not 
delete that VLAN, even if it is not associated with other ports. The reason is that the VLAN might have 
been configured by the bridge commands. 
Protection Switching Functionality 
An Ethernet ring consists of multiple Ethernet nodes, each connected to adjacent Ethernet nodes using 
two independent ring links. In order to prevent loops, the ring uses a specific link to protect the ring, 
designated as the Ring Protection Link (RPL). When there are no failures in the ring, the RPL is blocked. 
When a failure is detected, the RPL is unblocked. 
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
8. Resiliency and Optimization 
After link recovery is detected, the adjacent nodes (to the initial failure) start to send R-APS with (NR, 
NB). When these packets get to the RPL owner, it starts a WTR (Wait To Restore) timer. If during the 
predefined value of this timer, no additional link failure is detected, the RPL Owner starts to send R-APS 
with (NR, RB) (RB = RPL Blocked) and blocks the RPL. Nodes receiving R APS (NR, RB) flush their MAC 
learning table, unblock their ports, and return to idle state. 
The following timers are not configurable, and adhere to the default values of the standard: 
• 
WTR: 5 minutes. 
• 
Guard timer: 500 milliseconds. 
• 
WTB: 5 seconds more than the guard timer. 
• 
Burst of three R-APS messages sent upon configuration change: Up to 3.33 milliseconds (and 
then one message every 5 seconds if no new event occurs). 
• 
Interval between CCM messages for fast failure detection: 100 milliseconds  
• 
Hold off: 0. 
R-APS Control Messages 
Nodes on the ring use Ring Automatic Protection Switching (R-APS) messages to coordinate ring 
protection switching. R-APS messages are transmitted over a VLAN designated as the R-APS VLAN.   
You can specify the VLAN priority (0-7) and the OAM CFM Maintenance Entity group Level (MEL). It can 
be 0-7, and the default is 7, if none is specified. 
Ring control messages are passed with the R-APS only protects data VLANs, and only on the east and 
west ports. VLANs on the east and west ports can only be configured by the ring commands. VLANs on 
other bridge ports (including data and R-APS VLANs) may be configured with the bridge commands. 
They are handled by the bridge and the ring is unaware of them. 
If you configure as R-APS VLAN a VLAN that does not exist in the device, the device configures that VLAN 
and associates the east and west ports with it.  
If you delete the R-APS VLAN, the device disassociates the east and west ports from it, but does not 
delete that VLAN, even if it is not associated with other ports. The reason is that the VLAN might have 
been configured by the bridge commands. 
OAM CFM Messages  
To prevent loops, one of the ring interfaces is always blocked, so traffic should never return to the 
originating node. 
8. Resiliency and Optimization 
One of the ring devices, designated as an RPL owner, decides which interface to block, depending on 
OAM CFM messages sent and received on a dedicated R-APS VLAN. 
OAM CFM CC messages (used to detect failures in case of devices that are not directly connected) are 
supported, but the MEP configuration uses many default values. You must provide MD ID, MA ID and 
MEP ID, while The rest of the MEP properties are hardcoded.  
CC messages must be terminated by the peer they are intended for and ignored by others. Since the 
messages are multicast, you must configure each segment with different MD/MA combination. This way 
each port will only terminate CCM messages carrying the same MD/MA as its own, and ignore others. 
Factory Defaults 
By default, there is no Ethernet protection ring created in the device. When the ring is created, it has the 
following default configuration. 
Parameter 
Default  
Remarks 
bridge 
1 
description 
ERP ring 1 
east-port  
no east-port 
port-description 
ERP ring 1 east  
ERP ring 1 west 
r-aps 
no vlan 
vlan-priority 0 
mel 255 
shutdown 
shutdown 
west-port 
no west-port 
Configuring Ethernet Ring Protection 
The ring configuration sequence is as follows: 
1. Configure the bridge (refer to Configuring the Bridge in the Traffic Processing chapter).  
8. Configure the ring. 
8. Resiliency and Optimization 
 To configure ERP: 
1. At the config>protection# prompt, enter:  
erp <ring-number 1..239>  
An ERP instance is created if it does not already exist, and the config>protection>erp(<ring-
number>)# prompt is displayed. 
9. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Assigning ring to bridge  
bridge 1 
no bridge deletes the bridge 
 
data-vlan <data-vlan> 
no data-vlan [<data-vlan>] 
 
no data-vlan <data-vlan> removes 
the selected data VLAN 
no data-vlan without a list of 
VLANs removes all the data VLANs 
If the command is repeated it is 
added to the existing 
configuration (rather than 
replacing it). 
Defining description text for the 
ring 
description <string 1..64 characters 
long> 
no description 
no description returns the 
description to the default value. 
 
Defining the east port of a ring 
node 
east-port <bridge-port-number>  
no east-port 
 
 
Defining the description for the 
ring ports (east and west) 
port-description {east | west} <string> 
no port-description {east|west} 
 
The description can be between 1 
and 64 characters long. 
no port-description returns the 
description to the default value. 
Defining ring port type (role) 
port-type {east|west} {node-
port|rpl|neighbor} 
 
 
node-port – Port with no 
designated role.  
rpl – Port is designated as RPL. 
neighbor – Port is directly 
connected to RPL owner. 
8. Resiliency and Optimization 
Task 
Command 
Comments 
Configuring dedicated VLAN for 
R-APS messages 
r-aps [vlan <vlan-id>] 
[vlan-priority <vlan-priority>] 
[mel <level>] 
no r-aps 
 
vlan-id: 1–4094 
vlan-priority: 0–7 
level: 0–7.  
The mel parameter specifies the 
maintenance entity group (MEG) 
level (MEL) of the R-APS 
messages. 
Enabling failure detection from 
the Ethernet OAM service layer  
sf-trigger {east | west} mep <md-id> 
<ma-id> <mep-id> 
no sf-trigger {east | west} 
 
Defining the west port of a ring 
node 
west-port <bridge-port-number>  
no west-port 
 
 
Administratively enabling the ERP  
no shutdown 
Type shutdown to disable the 
ERP. 
Displaying ERP status 
show status 
See Viewing ERP Status.  
Configuration Errors 
The table below lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Invalid bridge port number 
If bridge-port-number is out of the 
range of bridge ports the device 
supports (1/1..1/64) 
 
A bridge port cannot be both east 
and west-port 
You tried to configure the same bridge 
port as east-port and west-port of the 
ring 
 
Maximum number of ERP rings 
already configured 
The device supports a single ring.  
 
Bridge number out of range  
The device supports only bridge 1. 
 
Only r-aps and data-vlan commands 
can add ERP ports to VLAN 
The east or west port is member of a 
VLAN that was not configured with the 
r-aps and data-vlan commands 
 
8. Resiliency and Optimization 
Message 
Cause 
Corrective Action 
At least one ring port (east or west) 
must be node-port 
At least one of the ring ports (east or 
west) must be node-port. You tried to 
assign a different role to both 
 
R-APS VLAN may not be a data 
VLAN  
The configured data VLANs cannot 
include the R-APS VLAN.  
 
Bridge port 64 is already a member 
of this VLAN 
You configured a new R-APS VLAN, 
while bridge port 64 (connecting the 
bridge to the router) is already a 
member of the new VLAN 
 
Viewing ERP Status 
You can display the current status of an ERP entity. 
 To display ERP status: 
• 
At the config>protection>erp(<erp-number>)# prompt, enter: 
show status 
The ERP status is displayed. 
 
ERP Ring Number: 1 
R-APS VLAN     : 1000 
Ring Status    : Protected 
Wait To Restore: 5/120 seconds 
 
               East        West 
               ----------  ---------- 
Bridge Port :  1/1         1/2 
Connected To:  Ethernet 1  Ethernet 1    
Role        :  RPL         Node port 
Status      :  Forwarding  Blocked 
Signal Fail :  OAM CFM     OAM CFM 
 
ERP status provides information on: 
 
ERP Ring Number (always 1) 
 
R-APS VLAN  number 
 
Ring Status: 

## 8.2 Fault Propagation  *(p.611)*

8. Resiliency and Optimization 
 
Idle – The node is performing normally (there is no link failure on the ring). In this state, 
traffic is unblocked on both ring ports, except for the RPL owner node, which blocks the 
RPL port (the other RPL owner port is unblocked) and the RPL neighbor port. 
 
Disabled - The node is disabled (in ‘shutdown’). 
 
Pending – transition state between ‘Protected’ and ‘Idle’ (only in this direction). This 
state means that the device detected that a signal failure state was cleared and started 
the WTR timer. After the WTR timer consumes itself, the state changes to ‘Idle’. 
 
Protected – A failure occurred on the ring. A non-owner node has traffic blocked on the 
ring port that connects to the failed link. The RPL owner, if it is not at one end of the 
failed link, unblocks the RPL port so both ports are active. 
 
Wait To Restore: wtr-remaining time/wtr-configured time (in seconds) 
 
Bridge port number 
 
Bridge ports assigned to be East and West ring ports 
 
RPL link role: 
 
Node port – Port is not connected to RPL 
 
RPL – Port is designated as RPL 
 
Neighbor – Port is directly connected to RPL owner 
 
East/West Port Status: 
 
Forwarding – Port is forwarding data. 
 
Blocked – Port is blocked 
 
R-APS and data blocked - R-APS and data are blocked 
 
East/West Signal Failure:  
 
OAM CFM – the node stopped receiving CC messages 
 
Physical failure – Port down failure  
8.2 Fault Propagation  
Fault propagation enables you to specify what action to take when a certain entity fails. 
Applicability and Scaling 
This feature is applicable to all ETX-1p versions. 
8. Resiliency and Optimization 
Functional Description 
If a tunnel or router interface is operationally up, but a ping to a destination server works poorly or does 
not work at all due to a downstream problem, a fault propagation rule can be configured to change the 
routing, so that the traffic will be routed through an alternative path. This rule has the following 
characteristics: 
• 
The source and destination must both be the same router interface or tunnel. 
• 
The only allowed trigger is ip-monitor. The monitor is a ping, continually testing connectivity to a 
destination address.  
• 
The only allowed actions are pbr-adjust or routing-adjust. If fault propagation is activated, the 
device removes routes through the interface or tunnel, leaving only those required to keep the 
monitor working. Traffic is then routed through an alternative path, as long as the fault persists.  
Fault propagation is used when it is desired a trigger (typically alarm) on a source entity to initiate an 
action (typically another alarm) on a destination entity.  
A special case of fault propagation uses a group of IP monitors for activating a standby LTE connection. A 
group can contain multiple IP monitors, and if all of them fail, an alternate tunnel is raised. 
A group is configured (and used as from-element) within the group level in the configure>fault level, and 
members (which must be IP monitors) are associated with it with the member command inside that 
group level. The trigger must be ip-monitor-group, and the action interface-up. The to-element must be 
a tunnel interface. 
Up to ten groups can be configured. 
Factory Defaults 
By default, no fault propagation is configured. When you configure fault propagation for a particular 
entity pair, the default configuration is as follows: 
• 
No trigger is defined for fault detection. 
• 
No action is defined to be performed when a fault is detected.  
• 
No IP monitoring group is defined. 
Configuring Fault Propagation 
Follow this procedure to configure fault propagation: 
8. Resiliency and Optimization 
1. Add a fault propagation entry for a pair of entities. 
10. Configure up to 32 fault propagation rules for the entry: 
a. Specify the trigger(s). 
b. Specify the action. 
Adding Fault Propagation Entry 
 To add fault propagation for a pair of entities: 
1. Navigate to configure fault. 
11. Type the command: 
fault-propagation <from-entity> to <to-entity> and enter the desired entities, as shown below. 
A prompt is displayed: 
config>fault>fault-propagation(<from-entity>/to/<to-entity>)$ 
12. Configure the fault propagation parameters as needed: 
 
From Entity 
To Entity 
Command 
Router Interface 
Router Interface 
fault-propagation router-interface <router-number> 
<interface-number> to router-interface <to-router-number> 
<to-interface-number> 
Router interface 
VRRP group 
fault-propagation router-interface <router-number> 
<interface-number> to vrrp < vrid> {ipv4|ipv6} 
router-interface <router-number-vrrp> <interface-number> 
Tunnel Interface 
Tunnel Interface 
fault-propagation tunnel <router-number> <tunnel-
interface-number> to tunnel <to-router-number> <to-
tunnel-interface-number>  
IP Monitor Group 
Tunnel Interface 
fault-propagation ip-monitor-group <name> to tunnel <to-
router-number> <to-interface-number> 
 
 
 
Configuring Fault Propagation Rules 
You can configure up to 32 fault propagation rules for a pair of entities. 
8. Resiliency and Optimization 
 To configure fault propagation rules: 
1. Navigate to configure fault fault-propagation <from-entity> to <to-entity> to select the fault 
propagation entry to configure. 
A prompt is displayed: 
config>fault>fault-propagation(<from-entity>/to/<to-entity>)# 
13. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying the action 
to take when fault 
propagation is 
triggered 
action-on-group {pbr-adjust | routing-adjust 
|interface-up | vrrp-priority-decrement <number>} 
 
The following actions are supported: 
• pbr-adjust – remove the PBR 
definition related to this group 
• routing-adjust – remove the routes 
related to this group 
• interface-up – activate the standby 
LTE connection in case all the group 
members fail. 
• vrrp-priority-decrement – Decrease 
VRRP priority.  
interface-up is available only if the 
source is a group of IP monitors; it is the 
only available action in this case  
Typing no action-on-group removes the 
action.  
The vrrp-priority-decrement action is 
allowed only if the to-entity is a VRRP 
group. 
<number> - VRRP priority to reduce 
when FP is activated (VRRP priority to 
reduce when FP activated (1..253).  
If the reduced priority is calculated to be 
less than 1, a value of 1 is used  
Default: 253 
8. Resiliency and Optimization 
Task 
Command 
Comments 
Specifying the trigger  
trigger {ip-monitor <ip-monitor-name> | ip-monitor-
group <ip-monitor-group-name>}  
 
 
 
 
 
 
Typing no before the command removes 
the specified trigger. 
ip-monitoring-group is available only if 
the source is a group of IP monitors; it is 
the only available trigger in this case 
<ip-monitor-name>} – IP monitoring 
profile name (up to 80 characters) 
<ip-monitor-group-name>} – IP monitor 
group name (up to 32 characters) 
 
Configuring IP Monitoring Groups 
You can configure up to 10 IP monitoring groups per device. 
 To define and configure an IP monitor group: 
1. Navigate to config>fault>group(<name>)#. 
2. Define the IP monitor group: group ip-monitor <name> (1-32 characters). 
3. Add members to the group (up to two members) based on existing monitors and associate the 
tunnel to the monitor: 
config>fault>group(<name>)# member ip-monitor <name> {tunnel <router> <interface>} 
4. Define a fault propagation rule: 
config>fault# fault-propagation ip-monitor-group <name> to tunnel <to-router-number> <to-
interface-number> 
5. Define the action and the trigger: 
config>fault>fp(ip-monitor-grou/<from-entity>/to/<to-entity>)# action-on-group interface-up 
config>fault>fp(ip-monitor-grou/<from-entity>/to/<to-entity>)# trigger ip-monitor-group 
A prompt is displayed: 
config>fault>group(<from-entity>/to/<to-entity>)# 
Example 
This example demonstrates how an IP monitor group is configured. 
• 
Defining IP Monitors “eth1” and “eth2” (see Configuring IP Monitoring)  
8. Resiliency and Optimization 
config>oam# ip-monitoring eth1 
config>oam>ip-monitoring(eth1)# target 10.1.1.1  
config>oam# ip-monitoring eth2 
config>oam>ip-monitoring(eth1)# target 10.1.1.2 
• 
Defining a new group “ether”, adding members to the group based on existing monitors and 
associating the tunnel 
config>fault>group(ether)# member ip-monitor eth1 tunnel 1  1 
config>fault>group(ether)# member ip-monitor eth2 tunnel 1  3 
• 
Defining a fault propagation rule:  
config>fault# fault-propagation ip-monitor-group ether to tunnel 1 2 
config>fault>fp(ip-monitor-group/ether/to/tunnel/1/2)# action-on-group interface-up 
config>fault>fp(ip-monitor-group/ether/to/tunnel/1/2)# trigger ip-monitor-group 
Disabling Fault Propagation  
 To disable fault propagation for a pair of entities: 
1. Navigate to configure fault. 
14. Type the command: 
no fault-propagation <from-entity> to <to-entity> to select the entities for which to disable fault 
propagation. 
The specified fault propagation is disabled. 
 To enable fault propagation: 
• 
From router-interface 1 2  
• 
To router-interface 1 2 
• 
Trigger: IP monitoring entity “adir” 
• 
Action: adjust routing 
exit all 
config fault 
fault-propagation router-interface 1 2 to router-interface 1 2 
  action-on-group routing-adjust 
  trigger ip-monitor "adir" 
exit all 

## 8.3 Link Redundancy  *(p.617)*

8. Resiliency and Optimization 
Configuration Errors 
The table below lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Maximum number of members has 
been reached 
You tried to add more than two 
members to an IP monitor group 
 
This tunnel is a destination of a 
fault propagation rule 
 
You tried to configure as group member 
a tunnel that is already configured as a 
destination of a fault propagation rule 
 
This group is used in a fault 
propagation rule 
You tried to delete a group that is 
source of a fault propagation rule, this 
group cannot be deleted 
 
No such IP monitor group 
You tried to configure as source an IP 
monitor group that does not exist  
 
The tunnel is an IP monitor group 
member 
You tried to configure as destination a 
tunnel that is a member of an IP 
monitor group  
 
8.3 Link Redundancy  
ETX-1p features link redundancy functionality. The following link types are supported: 
• 
Ethernet, Ethernet + VLAN 
• 
PPPoE 
• 
WiFi access point 
• 
LTE 
• 
GRE tunnel 
• 
IPsec tunnel (route based) 
Note: IPsec tunnel (policy based) is not supported by the link redundancy mechanism. 
 
8. Resiliency and Optimization 
Applicability and Scaling 
This feature is applicable to all the device versions.  
Standards Compliance 
Link redundancy is RAD proprietary functionality.  
Benefits 
Link redundancy provides the capability of tracking connectivity to specific IP addresses.  
Functional Description  
ETX-1p features link redundancy mechanism, which is functioning as follows: 
• 
Links are set with priority between them, defined by means of routing or PBR. 
• 
High priority links are set to be tracked by ip-monitoring 
• 
A failure on a link detected by ip-monitoring mechanism (see IP Monitoring) causes a removal of 
its routes / PBR rules. In this case another link starts to forward the traffic. 
Link association to ip-monitoring entity is done by fault propagation mechanism. Fault propagation 
definition is as follows: 
• 
Source – router entity / router interface, router entity / tunnel interface. 
• 
Destination – router entity / router interface, router entity / tunnel interface. 
• 
Trigger – ip-monitoring <name> 
• 
Action-on-group – routing-adjust and/or pbr-adjust  
The links protected by link redundancy must be bound to the entities participating in the fault 
propagation mechanism (router interfaces and tunnel interfaces) as follows: 
• 
Router interface: 
 
Ethernet, Ethernet + VLAN 
 
PPPoE 
 
WiFi access point 
8. Resiliency and Optimization 
 
LTE 
• 
Tunnel interface: 
 
GRE tunnel 
 
IPsec tunnel  
An example for Internet access is shown below: 
• 
Link 1 has default GW with metric 1 and IP monitoring. 
• 
Link 2 has default GW with metric 10. 
• 
Once IP monitoring detects a failure – Link 1 routes are removed, and traffic goes to Link 2. 
 
 
 
 
 
 
 
Configuring Link Redundancy 
 To prepare the device for configuring link redundancy: 
• 
Set priorities between the links either by using routing metrics or configuring the PBR.  
Note 
PBR has higher priority over routing entries. 
 To configure link redundacy:  
1. Bind the link to be protected to a router or tunnel, according to the link type (as explained in 
Functional Description) 
2. Under configure oam ip-monitoring, create the ip-monitor entity and set the target IP address 
and other parameters (see IP Monitoring in Monitoring and Diagnostics Chapter. 
The IP monitoring entity is activated. 
8. Resiliency and Optimization 
3. Using fault propagation, associate the ip-monitoring entity to the router/tunnel configured in step 
1 (see Fault Propagation).  
Once IP monitoring detects a failure in the protected link, the traffic will be routed through an 
alternative path (the link you defined earlier with lower priority), as long as the fault persists. 
Examples  
Preliminary configuration: 
• 
Links are set with priority between them by routing configuration:  
 
interface 3 metric 10 
 
address 10.10.10.2 metric 1 
• 
Router 1 interface 2 is bound to ethernet lan2 port, IP address 10.10.10.1/24 
Link redundancy configuration: 
• 
IP monitoring entity “adir” is created and IP address for monitoring is set to 20.20.20.2  
• 
Fault propagation is defined on router 1 interface 2:  
 
Trigger: tracking ethernet lan2 with ip-monitoring entity “adir” 
 
Action – remove static route 10.10.10.2 on failure defined by IP monitioring 
In the case of failure forwarding will be done by the cellular LTE port. 
 
#   
    router 1 
        name "Router#1"   
         
        interface 2 
            address 10.10.10.1/24 
            bind ethernet lan2 
            dhcp-client 
                client-id mac 
            exit 
            no shutdown 
        exit 
        interface 3 
            bind cellular lte 
            dhcp 
             
            exit 
            no shutdown 
        exit 
         
             

## 8.4 SD-IoT  *(p.621)*

8. Resiliency and Optimization 
        static-route 0.0.0.0/0 interface 3 metric 10 
        static-route 0.0.0.0/0 address 10.10.10.2 metric 1 
    exit 
    exit 
    oam 
        ip-monitoring "adir" 
            target 20.20.20.2 (“ip address for monitoring”) 
        exit 
    exit 
     
#       Fault Propagation Configuration 
        fault-propagation router-interface 1 2 to router-interface 1 2 
            action-on-group routing-adjust 
            trigger ip-monitor "adir" 
        exit 
    exit 
 
    exit  
 
8.4 SD-IoT  
SD-IoT is a software-defined technology that provides connectivity between distributed sites and a 
central hub over any IP network. 
Applicability and Scaling 
This feature is applicable to all devices. 
Standards Compliance 
SD-IoT is RAD proprietary functionality. 
Functional Description 
SD-IoT is a software-defined, multipath connectivity overlay that delivers resilient, encrypted, and QoS-
aware WAN connectivity between distributed sites and a central hub over any IP underlay 
(fiber/MPLS/GPON, Cellular 4G/5G, satellite). 
8. Resiliency and Optimization 
Layer 2 services are delivered as SSL/TLS-encrypted tunnels (L2-over-L3) while the SD-IoT client on RAD 
gateways processes and steers traffic across multiple links, supporting redundancy with fast 
failover/restore mechanisms. L2 duplication function supports services that require very low latency (IEC 
61850 GOOSE) by duplicating the traffic into separate WAN link in parallel to SD-IoT links. 
The SD-IoT server at the hub provides connectivity between the distributed sites. The SD-IoT server is 
deployed on Ubuntu (bare metal or VM), supports high-availability clustering, offers centralized zero-
touch provisioning/monitoring/analytics via RADview, and scales to thousands of secure tunnels. 
The SD-IoT system with its clients and servers can be described as a huge VLAN-aware bridge 
implemented over multiple layer 3 links while the client and server LAN ports are the L2 service entry 
points. L2 services are defined based on VLAN ID. 
The SD-IoT system supports HA (High Availability) by enabling connection to Primary and Secondary SD-
IoT servers. The HA is driven by the Gateway functionality while the [Product-Name] device defines the 
connections and shows the status. 
High Availability (HA) 
SD-IoT module is considered to operate in High Availability (HA) mode when at least one of the tunnel’s 
secondary peer addresses is configured. HA functionality is fully controlled by MPGW. 
 
Minimal Required Configurations 
• 
Operation of the SD-IoT client in ETX-1p device must include the following minimal configuration 
parameters: 
• 
Client number 
• 
Authentication method and username/password or valid certificate accordingly 
• 
Activation (No shutdown) 
• 
Ingress port. 
• 
At least one tunnel with tunnel parameters – peer address, no shutdown 
Note 
The module starts operation once all the required parameters are configured. 
• 
The following parameters are optional and can be left at their defaults: 
 
Keep-alive and retries 
 
Tunnel priority 
 
Duplication parameters (required active VLAN port with VLAN equal to PVID) 
8. Resiliency and Optimization 
 
Duplication traffic type  
 
Ingress port PVID and Pbit  
For each tunnel you must configure the following: 
• 
Tunnel number  
• 
Peer address, TCP port 
• 
Secondary peer address, tcp-port 
• 
Priority 
• 
Shutdown 
For the ingress port you must configure the LAN Ethernet port, the PVID and the Pbit. 
For the duplication port you must configure the WAN Ethernet port and the traffic type passing through 
this port. 
Factory Defaults 
By default, there is no SD-IoT client created in the device. When the client is created, it has the following 
default configuration. 
Parameter 
Default  
Remarks 
authentication-method 
psk 
username 
“” (empty string) 
password 
“” (empty string) 
certificate 
“” (empty string) 
keep-alive interval 
1 sec 
keep-alive retries 
3 
shutdown 
shutdown 
tunnel level 
 
    port 
443 
    secondary-port 
443 
     priority 
100 
     shutdown 
shutdown 
8. Resiliency and Optimization 
Parameter 
Default  
Remarks 
pvid 
1 
pbit 
0 
traffic-type 
all 
Configuring SD-IoT 
The configuration sequence is as follows: 
1. Configure the router (refer to Configuring the Router  in the Traffic Processing chapter).  
15. Configure the IoT module. 
 To define a sd-iot entity: 
1. At the config # prompt, enter:  
sd-iot 1  
An sd-iot instance is created if it does not already exist, and the config>sd-iot(1)# prompt is 
displayed. 
16. Perform the required tasks according to the following table. 
 
Task 
Command 
Comments 
Configuring sd-iot authentication 
method 
authentication-method {psk | 
certificate} 
 
Configuring sd-iot certification 
certificate <certificate-name 1..64 
characters long > 
no certificate deletes the 
certificate 
Clearing sd-iot statistics 
clear-statistics 
 
Configuring sd-iot client number 
 
client-number <number 1..1000> 
no client-number deletes the 
client 
Configuring sd-iot duplication 
function 
 
duplication ethernet <port-index> 
[traffic-type {all | multicast | goose}] 
 
no duplication ethernet <port-
index> deletes the duplication 
entity 
Only WAN ports can serve as a 
duplication egress port. 
8. Resiliency and Optimization 
Task 
Command 
Comments 
Configuring sd-iot ingress port 
ingress-port ethernet <port-index> 
[pvid <vlan-id 1..4095> [pbit <0..7 >] 
 
Only LAN ports are allowed  
no ingress-port ethernet <port-
index> deletes the ingress port 
Configuring sd-iot tunnels keep-
alive interval and retries 
keep-alive [interval <1..1200 seconds>] 
[retries <3..10>] 
 
Tunnel level 
tunnel <1..2> 
See Configuring the Tunnel below 
Configuring sd-iot username and 
password 
 
username <name 1..20 char> password 
<password> [hash] 
 
no username deletes the 
username 
The max length of clear text 
string is 20 chars, of the hashed 
string –  40 chars 
Administratively enabling the sd-
iot entity 
no shutdown  
 
Type shutdown to disable the 
entity. 
Configuring the Tunnel  
 To configure the tunnel parameters: 
1. Navigate to configure sd-iot# tunnel <1..2> to select the tunnel to configure.  
The config> sd-iot # tunnel <tunnel number> prompt is displayed.  
1. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
Configuring the tunnel 
peer address and sd-iot 
tunnel peer TCP port 
 
peer-address <ip-address> 
[port <443, 1024..65535> 
  
no peer-address deletes the peer address 
By default no addresses are configured 
Default port number: 443 
Configuring the sd-iot 
tunnel secondary peer 
address and sd-iot tunnel 
secondary peer TCP port 
secondary-peer-address 
<ip-address> [port <443, 
1024..65535>] 
 
no secondary-peer-address deletes the secondary peer 
address 
By default no addresses are configured 
Default port number: 443 
Configuring the tunnel 
priority 
priority <number 1..255> 
 
Default: 100 
8. Resiliency and Optimization 
Task 
Command  
Comments 
Enabling sd-iot tunnel 
entity  
no shutdown 
  
 
Configuration Errors 
The table below lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Cannot set – illegal peer address 
Only valid unicast IP address is allowed 
for peer address and/or secondary peer 
address 
 
Cannot set – only WAN ports can be 
used as duplication port 
Only WAN ports are allowed as 
duplication ports. 
 
Cannot set – only one duplication 
port can be defined 
Only one duplication port is allowed.  
 
Cannot set – only LAN ports can be 
used as ingress port  
Only LAN ports are allowed as ingress 
ports.  
 
Cannot set – only one ingress port 
can be defined 
Only one ingress port is allowed.  
 
Cannot set – port is bound to 
another entity or has configuration 
of ACL, QoS, PBR, force-next-hop, 
dot1x or mac-access-control 
Defining port as ingress port is allowed 
only when it is not bound to any entity 
and has no configuration of ACL, QoS, 
PBR, force-next-hop, dot1x, mac-access-
control 
 
Cannot set – vlan is not defined 
Allowed to set only with valid VLAN (> 
0).  
 
Viewing IoT Status 
You can display the current status of an IoT entity. 
 To display IoT status: 
• 
At the config>iot(<number>)# prompt, enter: 
show status 
8. Resiliency and Optimization 
The IoT status is displayed. 
Example – Stand Alone GW: 
 
configure>sd-iot(number)# show status 
SD-IoT Module Mode    : L2-Standalone 
 
 
SD-IoT Module Version : 1.8 
 
 
 
SD-IoT Module Status  : Up 
 
Tunnel: 1 
Administrative Status : Up 
Operational Status    : Down 
Tunnel: 2 
Administrative Status : Up 
Operational Status    : Up 
 
Example – HA: 
 
configure>sd-iot(number)# show status 
SD-IoT Module Mode    : L2-HA 
 
 
 
SD-IoT Module Version : 1.8 
 
 
 
SD-IoT Module Status  : Up 
 
GW HA Status:  
 
 
 
 
Primary GW   : Active 
 
 
 
 
Secondary GW : Standby 
 
 
 
 
 
Tunnel: 1 
Administrative Status             : Up 
Operational Status (primary GW)   : Up 
Operational Status (secondary GW) : Up 
 
Tunnel: 2 
Administrative Status             : Up 
Operational Status (primary GW)   : Up 
Operational Status (secondary GW) : Down  
 
IoT status provides information on the following: 
• 
SD-IoT network-mode (always L2 in the current version) 
• 
SD-IoT ha-mode (high availability mode) 
• 
SD-IoT Module version 
• 
SD-IoT module status: 
 
Up – module is operated (all required operational parameters are OK) 
 
Down – module admin status is ‘down’ 
 
Configuration Missing  
8. Resiliency and Optimization 
• 
SD-IoT primary and secondary GW status 
 
active 
 
standby  
• 
Administrative status (per tunnel) 
 
Up 
 
Down 
• 
Operational status for the primary and secondary GW (per tunnel) 
 
Up 
 
Down 
Viewing IoT Statistics 
You can view the IoT statistics by using the show statistics command. This command is available in the 
sd-iot context: (config>sd-iot#). 
The output displays  the following: 
• 
LAN total receive/transmit packets/octets 
• 
Duplication receive/transmit packets/octets 
• 
Receive/transmit packets/octets per tunnel 
For example: 
Example 
Counter                      Rx                      Tx                    
------------------------------------------------------------------------------ 
LAN Total Octets             99999                   99999 
LAN Total Frames             99999                   99999 
Duplication Octets           99999                   99999 
Tunnel 1: 
  Tunnel Total Octets        99999                   99999 
z  Tunnel Total Frames        99999                   99999 
Tunnel 2: 
  Tunnel Total Octets        99999                   99999 
  Tunnel Total Frames        99999                   99999 
                                   
 
 