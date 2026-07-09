# Feature Reference – 5 Traffic Processing – 5.6 Layer-2 Control Protocol (L2CP) Processing

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 970–983.*


## Example  *(p.970)*


## Applicability and Scaling  *(p.970)*

ETX-2i Devices 
5. Traffic Processing 
Example 
The following example describes how to define a Fat pipe detection profile named e2000, with regular 
Policer 2000M, and search according to source MAC address. 
 To configure regular Policer 2000M: 
config qos policer-profile "2000M" bandwidth cir 500000  cbs 32000 eir 500000 ebs 
32000  
 To define Fat pipe detection profile named e2000: 
con port fat-pipe-detection-profile e2000  
policer profile 2000M release-hold-time 30  
search-key src-mac  
exit all 
5.6 Layer-2 Control Protocol (L2CP) Processing 
ETX-2i offers high flexibility in handling L2CP frames. According to application requirements, ETX-2i 
tunnels with MAC swap (Layer-2 Protocol Tunneling (L2PT)), discards, or peers (traps to the host CPU for 
protocol processing) the L2CP frames. These actions are defined by Layer-2 Control Protocol (L2CP) 
profiles, which also provide different L2CP addresses. The L2CP profiles are attached to ports and flows. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products. 
L2PT identifies Layer-2 slow protocols with up to four VLAN tags (ETX-2i). 
Up to four L2CP profiles are supported per device. 
The L2CP profile applies for the following MAC addresses: 
• 
Slow protocol MAC address range: 01-80-C2-00-00-00 to 01-80-C2-00-00-2F 
• 
01-00-0C-CC-CC-CC 
• 
01-00-0C-CC-CC-CD 

## Standards Compliance  *(p.971)*


## Functional Description  *(p.971)*

ETX-2i Devices 
5. Traffic Processing 
Standards Compliance 
IEEE 802.3 
Functional Description 
L2CP Profiles 
ETX-2i supports L2CP profiles to define the handling of Layer-2 Control Protocol traffic.  
You can create and configure L2CP profiles (see Configuring L2CP Processing) and then bind relevant 
L2CP profiles to ports and/or to flows (see Binding an L2CP Profile to a Flow or Port).  
ETX-2i handles Layer-2 control protocol traffic on a per-port and per-flow basis. L2CP traffic (both tagged 
and untagged L2CP frames) is processed using a two-stage mechanism comprising per-port or per-flow 
profiles (set of rules for traffic handling). If no per-flow L2CP profile is configured, a per-port-level profile 
is used. 
L2CP profiles pass through Layer-2 control frames (including other vendors’ L2CP frames) across the 
network, and perform the following actions: 
• 
Tunnel – perform protocol tunneling with MAC address swap, and discard Loopback frames 
(EtherType 0x9000) 
• 
Discard – discard L2CP frames 
• 
Peer – trap to host for protocol processing; per supported protocols  
If no default action is configured for an address or protocol, this traffic is tunneled. 
Note 
An L2CP profile that is attached to a port can be modified or replaced; it 
cannot be deleted.  
You can also display the L2CP port statistics for a port associated with an L2CP profile that is configured 
with tunneling and MAC swap (refer to Displaying Layer-2 Control Processing Statistics in the Cards and 
Ports chapter). 
 
 
ETX-2i Devices 
5. Traffic Processing 
Binding an L2CP Profile to a Flow or Port 
You can bind an L2CP profile to one of the following: 
• 
A flow – see Configuring Flows. 
• 
A port – Ethernet, PCS, or Logical MAC; refer to the relevant configuration section in the Cards 
and Ports chapter. 
When bound to a flow, L2CP profile functionality (discard, tunnel, or peer) applies on traffic classified to 
this flow. 
Flow level L2CP profile binding allows meeting the MEF requirement to support different policies for 
different EVC types (EPL, EVPL, EPLAN, EVPLAN, and more). 
When bound to a port, L2CP profile functionality (discard, tunnel, or peer) applies on all ingress traffic 
(i.e. both tagged and untagged) on this port. 
Port level L2CP enables easy configuration, when many port flows share the same L2CP policy. 
• 
If an L2CP profile is not bound to a flow, the behavior is according to the L2CP profile bound to 
the port. 
• 
If the port level L2CP profile is configured with the Discard or Peer actions, it has priority over 
the flow level L2CP profile configuration. This means that if a protocol is configured to be 
discarded or peered in the port profile, flow profile configuration for this protocol is not 
applicable. 
• 
If the port level L2CP profile is configured with the Tunnel action for a certain protocol (mac), 
then the flow profile (if configured) determines the final action (discard, peer, or tunnel). 
Handling Port Level Protocol Peering  
Port level protocol peering, such as LLDP or LACP, is sometimes required (untagged) for LAG or LLDP 
protocol termination. On the other hand, on the EVC level (tagged), it may be required to tunnel these 
protocols. However, a port level profile, configured with a Peer action for a protocol, results in trapping 
of protocol frames at the EVC level, as a port level profile peers both tagged and untagged frames to the 
CPU. This may not be the desired result. 
You can achieve peering of untagged only protocols frames to the CPU as follows: 
• 
Use an untagged flow for the sole purpose of peering port protocols to the CPU. 
• 
Configure the flow with a drop command to discard traffic transmitted by the flow. 
 
 
ETX-2i Devices 
5. Traffic Processing 
The peer action on a flow has precedence over the drop command, and therefore the port protocol is 
peered to the CPU and ALL other traffic on the flow is dropped. 
 
Note 
The untagged flow destination port can be any port, as no traffic leaks from 
this flow. It is even possible to have the untagged flow egress port the same as 
the ingress port (see the second use case example below). 
Use Case Examples 
All EVCs with the same L2CP policy; no port level protocols: 
 
Different L2CP policy for each EVC, with port level protocols: 
ETX-2i Devices 
5. Traffic Processing 
Layer-2 Protocol Tunneling (L2PT)  
ETX-2i supports L2PT – L2CP tunneling with MAC swap functionality, meaning that L2CP frames can be 
forwarded over networks that are not transparent to L2CP.  
L2PT is supported at the port level and applies for PTP flows, as well as for bridged traffic (refer to 
Configuring Ethernet Port Parameters in the Cards and Ports chapter). 
• 
ETX-2i supports multiple network ports with L2PT functionality for both PTP and Bridge 
applications.  
• 
Any port configured as NNI is L2PT Network, by default.  
• 
Any Ethernet, PCS, or Logical MAC user port can be configured to be L2PT Network (default 
‘no’). 
• 
L2PT mac-swap functionality is supported on L2CP frames having the following tag structure: 
 
Untagged frames 
 
Up to four VLAN tags  
 
VLAN EtherType 0x8100 or 0x88a8 at any tag level 
• 
Any port assigned with an L2CP profile with MAC swap, including port 1, can function as an L2PT 
user port. 
ETX-2i Devices 
5. Traffic Processing 
You can bind an L2CP profile configured with L2CP MAC swap to a user port; it cannot be bound to a 
flow. A port assigned with an L2PT profile expects “native” L2CP frames. MAC swap is performed toward 
the relevant network port or user port that is configured for use as L2PT network ports.  
L2PT functionality in ETX-2i is as follows:  
1. User to L2PT network port: IO port ingress traffic identified with the configured protocols is MAC 
swapped to a user preconfigured multicast address (e.g., 01-70-00-00-00-00) and proceeds with 
the original traffic path as set by the classification (tunnel). The actual functionality for these 
protocols is a tunnel with MAC swap. 
2. L2PT network port to user: IO port ingress traffic identified with the preconfigured L2PT 
multicast MAC address (e.g., 01-70-00-00-00-00) is MAC swapped to the original protocol MAC. 
Traffic then proceeds with the original traffic path as set by classification to the egress port.  
Note 
• 
An L2PT network port is an NNI port or any other user port configured as 
an L2PT network port (for tunnel with MAC swap). 
• 
Each L2PT protocol can be mapped to a unique destination multicast MAC 
address.  
 
MAC SWAP
User 
Port
SWAP Back
L2PT 
Network 
Port
 
Supported Topology 
Bridge
UNI
Port 1
UNI
Port 3
L2PT Network Port
Port 2
 
Bridge Flows and Ports 

## Factory Defaults  *(p.976)*


## Configuring L2CP Processing  *(p.976)*

ETX-2i Devices 
5. Traffic Processing 
Factory Defaults  
By default, a “tunnel all” profile is attached to every port. However, no default L2CP profile is attached 
to a newly created flow, meaning that the flow traffic behaves, by default, according to the port profile. 
When you create a new L2CP profile, it has the configuration of L2cpDefaultProfile, the ETX-2i-provided 
default L2CP profile. It is configured as follows: 
• 
For MAC hex byte 0x00 through 0x2f, action = tunnel  
• 
Default action = tunnel  
Configuring L2CP Processing 
Adding L2CP Profiles 
 To add an L2CP profile: 
1. Navigate to configure port. 
The config>port# prompt is displayed. 
2. Enter: 
l2cp-profile <l2cp-profile-name> 
An L2CP profile with the specified name is created and the 
config>port>l2cp-profile(<l2cp-profile-name>)$ prompt is displayed. The new profile is 
configured by default as described in Factory Defaults. 
3. Configure the L2CP profile as needed (see Configuring Layer 2 Control Processing Profile 
Parameters). 
Deleting L2CP Profiles 
You can delete an L2CP profile only if it is not assigned to any port. 
 To delete an L2CP profile: 
1. Navigate to configure port. 
The config>port# prompt is displayed. 
2. Enter no l2cp-profile <l2cp-profile-name> 
The L2CP profile with the specified name is deleted if it is not assigned to any port.  

## Setting L2CP Profile Parameters  *(p.977)*

ETX-2i Devices 
5. Traffic Processing 
Setting L2CP Profile Parameters 
 To configure an L2CP profile: 
1. Navigate to configure port l2cp-profile <l2cp-profile-name> to select the L2CP profile to 
configure. 
The config>port>l2cp-profile(<l2cp-profile-name>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying the 
default action 
for undefined 
control 
protocols 
default { discard | tunnel } 
 
Specifying the 
L2CP action for 
MAC addresses 
(discard, tunnel, 
or peer) 
mac <mac-addr-last-byte-value-list><mac-
addr> { discard | tunnel | peer } 
mac-addr –can be either of the following: 
• Long MAC address, i.e., full valid MAC 
adress [xx-xx-xx-xx-xx-xx]  
For example:  
01-80-c2-00-00-02 
Possible values:  
01-80-c2-00-00-xx, where xx= 0H-10H, 
20H-2FH; 
01-00-0c-cc-cc-cc 
01-00-0c-cc-cc-cd 
• Short MAC address, i.e., last byte of the 
control protocol MAC address 
[0x00..0x10,0x20..0x2F] 
For example: 0x02 is the short MAC 
address of 
 01-80-c2-00-00-02. 
Possible values: 0H-10H, 20H-2FH 
discard – L2CP frames are discarded. 
tunnel – L2CP frames are forwarded across 
the network as ordinary data. 
peer – ETX-2i peers with the user equipment 
to run the protocol. L2CP frames are 
forwarded to the ETX-2i CPU. Unidentified 
L2CP frames are forwarded across the 
network as ordinary data.  
Note:  
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
• Peer action cannot be used with the MAC 
addresses 01-00-0c-cc-cc-cc and 01-00-0c-
cc-cc-cd. 
• ETX-2i supports a single MAC address per 
chassis. This address is used by all L2PT 
profiles and protocols that user asks to 
tunnel. If you configure different MACs in 
different ports, the last MAC you 
configured is the one used. 
• Entering no mac 
<mac-addr-last-byte-value-list><mac-
addr> removes the action for the 
specified MAC address. 
Defining a 
Loopback 
protocol for 
discarding 
protocol  loopback  discard  
Entering no protocol loopback removes the 
action for the Loopback protocol. 
Defining a 
protocol for 
tunneling and 
specifying MAC 
swap address 
(for L2PT 
functionality) if 
other than 
default 
protocol { lacp | stp | vtp | cdp | lldp | 
pvstp| pagp | udld | dtp | lamp | link-oam 
|e-lmi |802.1x | gvrp | gmrp | mmrp | 
mvrp-customer-bridge | mvrp-provider-
bridge | msrp | mirp | dldp | hgmp | esmc 
| ptp } tunnel mac-change [<mac-address>] 
protocol – list of L2CP protocols in which 
tunneling and MAC swap can be performed. 
mac-address – the MAC address to be used as 
an alternative to the original MAC. This is an 
optional parameter; its default value is  
01-00-0C-CD-CD-D0.  
Entering no protocol followed by protocol 
names removes the action for the specified 
protocols. 
Note: 
• Supported over a user port only. 
• <mac-address> must be a valid multicast 
address. Must have a 1 value in the least-
significant bit of the first octet (for 
example, 01-03- 05) 
• You must use the same <mac-address> for 
all tunneled protocols. 
• L2PT MAC swap (mac-change) 
functionality is supported for L2CP frames 
with up to four vlan tags. 
• You can configure either gmrp or gvrp in a 
single profile; not both. 

## Examples  *(p.979)*

ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
• You can configure either mvrp-customer-
bridge or mvrp-provider-bridge in a single 
profile; not both. 
• You cannot map dldp and hgmp to a single 
MAC. However, they can share the same 
MAC with other protocols. 
• Protocols 802.1x-2001 and 802.1x-2004 
are supported. 
• ptp protocol is only configurable for 
devices with PTP. 
 
Examples 
 To add L2CP profile named layer2ctrl1 with discard action for hex byte 0x01 and 0x03 (short MAC 
format): 
exit all  
ETX-2i#configure port 
l2cp-profile layer2ctrl1 
ETX-2i>config>port>l2cp-profile (layer2ctrl1)#mac 0x01 discard 
mac 0x03 discard 
exit all 
 To add L2CP profile named layer2ctrl2 with tunnel action for long MAC addresses 01-80-c2-00-00-
00 and 01-80-c2-00-00-01 (long MAC format): 
exit all  
ETX-2i#configure port 
l2cp-profile layer2ctrl2 
ETX-2i>config>port>l2cp-profile(layer2ctrl2)# 
mac 01-80-c2-00-00-00 tunnel 
mac 01-80-c2-00-00-01 tunnel 
exit all 
 To add L2CP profile 1 that uses LACP protocol for tunneling with L2CP MAC swap: 
ETX-2i#configure port l2cp-profile 1  
ETX-2i>config>port>l2cp-profile(1)#  
protocol lacp tunnel mac-change 01-23-45-67-89-DD 
exit all 
ETX-2i Devices 
5. Traffic Processing 
 To display the layer2ctrl1 L2CP profile: 
ETX-2i#configure port l2cp-profile layer2ctrl1  
ETX-2i>config>port>l2cp-profile(layer2ctrl1)# info detail 
    mac  0x00  tunnel 
    mac  0x01  discard 
    mac  0x02  tunnel 
    mac  0x03  discard 
    mac  0x04  tunnel 
    mac  0x05  tunnel 
    mac  0x06  tunnel 
    mac  0x07  tunnel 
    mac  0x08  tunnel 
    mac  0x09  tunnel 
    mac  0x0a  tunnel 
    mac  0x0b  tunnel 
    mac  0x0c  tunnel 
    mac  0x0d  tunnel 
    mac  0x0e  tunnel 
    mac  0x0f  tunnel 
    mac  0x10  tunnel 
    mac  0x20  tunnel 
    mac  0x21  tunnel 
    mac  0x22  tunnel 
    mac  0x23  tunnel 
    mac  0x24  tunnel 
    mac  0x25  tunnel 
    mac  0x26  tunnel 
    mac  0x27  tunnel 
    mac  0x28  tunnel 
    mac  0x29  tunnel 
    mac  0x2a  tunnel 
    mac  0x2b  tunnel 
    mac  0x2c  tunnel 
    mac  0x2d  tunnel 
    mac  0x2e  tunnel 
    mac  0x2f  tunnel 
    default  tunnel 
    mac "01-80-c2-00-00-00" tunnel 
    mac "01-80-c2-00-00-01" tunnel 
    mac "01-80-c2-00-00-02" tunnel 
    mac "01-80-c2-00-00-03" tunnel 
    mac "01-80-c2-00-00-04" tunnel 
    mac "01-80-c2-00-00-05" discard 
    mac "01-80-c2-00-00-06" tunnel 
    mac "01-80-c2-00-00-07" tunnel 
    mac "01-80-c2-00-00-08" tunnel 
    mac "01-80-c2-00-00-09" tunnel 
    mac "01-80-c2-00-00-0a" tunnel 
    mac "01-80-c2-00-00-0b" tunnel 
    mac "01-80-c2-00-00-0c" tunnel 
    mac "01-80-c2-00-00-0d" tunnel 
    mac "01-80-c2-00-00-0e" tunnel 
ETX-2i Devices 
5. Traffic Processing 
    mac "01-80-c2-00-00-0f" tunnel 
    mac "01-80-c2-00-00-10" tunnel 
    mac "01-80-c2-00-00-20" tunnel 
    mac "01-80-c2-00-00-21" tunnel 
    mac "01-80-c2-00-00-22" discard 
    mac "01-80-c2-00-00-23" tunnel 
    mac "01-80-c2-00-00-24" tunnel 
    mac "01-80-c2-00-00-25" tunnel 
    mac "01-80-c2-00-00-26" tunnel 
    mac "01-80-c2-00-00-27" tunnel 
    mac "01-80-c2-00-00-28" tunnel 
    mac "01-80-c2-00-00-29" tunnel 
    mac "01-80-c2-00-00-2a" tunnel 
    mac "01-80-c2-00-00-2b" tunnel 
    mac "01-80-c2-00-00-2c" tunnel 
    mac "01-80-c2-00-00-2d" tunnel 
    mac "01-80-c2-00-00-2e" tunnel 
    mac "01-80-c2-00-00-2f" tunnel 
    mac "01-00-0c-cc-cc-cc" tunnel 
    mac "01-00-0c-cc-cc-cd" discard 
    default tunnel 
ETX-2i#configure port l2cp-profile layer2ctrl1  
ETX-2i>config>port>l2cp-profile(layer2ctrl1)# info 
    mac "01-80-c2-00-00-05" discard 
    mac "01-80-c2-00-00-22" discard 
    mac "01-00-0c-cc-cc-cd" discard 
 
Note 
The info detail command displays all actions (including the default action (in 
above example, tunnel). The info command only displays non-default actions. 
 To configure L2CP profile on a port: 
configure port 
l2cp-profile peer 
mac 0x### peer 
.. 
.. 
.. 
exit  
l2cp-profile tunnel 
mac 0x## tunnel 
.. 
.. 
.. 
exit  
ethernet 0/1 
l2cp-profile tunnel 
exit all 

## Configuration Errors  *(p.982)*

ETX-2i Devices 
5. Traffic Processing 
 To configure L2CP profile on a flow: 
configure flow 
classifier-profile untag_l2cp match any  match-untagged 
flow l2cp_eth0/1 
ingress-port ethernet 0/1 
egress-port ethernet 0/1 
classifier untag 
l2cp-profile peer 
drop 
no shutdown 
exit 
 To configure L2PT network on a user port: 
ETX-2i# config>port>eth(3)# l2pt-network 
 To delete L2CP profile layer2ctrl1: 
ETX-2i# configure port 
no l2cp-profile layer2ctrl1 
Configuration Errors 
The following table lists the messages generated by ETX-2i when a configuration error is detected. 
Message 
Description 
Cannot add MAC address: Max number of 
MAC addresses has been reached 
Cannot specify an L2CP processing action for a MAC address 
because the maximum number of addresses has been reached. 
Destination MAC addresses of DLDP 
protocol can’t be shared with HGMP 
protocol 
DLDP and HGMP were mapped to the same MAC address. 
Illegal L2CP processing action for this MAC 
address type 
The L2CP processing action selected for the current MAC address 
type is not valid. 
Illegal MAC address for peer action 
The MAC address selected for the peer processing action is not 
valid. The address must be 01-80-C2-00-00-02. 
Invalid L2PT protocol  
An invalid protocol was used to configure the L2CP MAC swap.  
L2CP MAC swap available only on IO ports 
The L2CP MAC swap is not supported for ports that are not IO 
ports.   
L2CP MAC swap not available on flows 
L2CP MAC swap can only be configured for ports. 

## Viewing L2CP Statistics  *(p.983)*

ETX-2i Devices 
5. Traffic Processing 
Message 
Description 
L2CP profile creation failure: Max number 
of L2CP profiles has been reached 
The L2CP profile cannot be added because the maximum number 
of L2CP profiles has been reached. 
L2CP profile deletion/modification failure: 
L2CP profile is in use 
The L2CP profile cannot be deleted or modified because it is 
currently attached to a port or a flow. 
L2CP profile does not exist 
Cannot bind an L2CP profile that has not yet been created.  
Only tunnel supported MAC change 
An invalid action was used to configure the L2CP MAC swap.   
Peer action is not allowed for port-bound 
L2CP profile 
An L2CP profile bound to a port cannot perform a peer action. 
Viewing L2CP Statistics 
You can view L2CP statistics for an Ethernet, a Logical MAC or a PCS port. 
 To display the L2CP statistics for an Ethernet port: 
• 
At the prompt config>port>eth(1/1)#, enter show l2cp-statistics 
L2CP statistics are relevant to the tunnel with the MAC swap function only and are displayed for 
the specified port, showing the number of encapsulated and decapsulated packets for each 
protocol being monitored. 
ETX-2i>config>port>eth(0/1)# show l2cp-statistics 
Protocol              Encapsulated   Decapsulated 
 
--------------------------------------------------------------- 
LACP                  0              0 
STP                   0              0 
CDP                   0              0 
VTP                   0              0 
LLDP                  0              0 
PVSTP                 0              0 
PAGP                  0              0 
UDLD                  0              0 
DTP                   0              0 
LAMP                  0              0 
Link OAM              0              0 
ELMI                  0              0 
802.1x                0              0 
GVRP                  0              0 
GMRP                  0              0 
MMRP                  0              0 
MVRP Customer Bridge  0              0 
MVRP Provider Bridge  0              0 
MSRP                  0              0 