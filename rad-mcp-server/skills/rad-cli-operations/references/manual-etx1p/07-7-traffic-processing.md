# 7 Traffic Processing

*Manual `ETX-1p_6.4_Mn_05-26_GA.pdf`, pages 422–603.*


## 7.1 Bridge  *(p.422)*

7.1 Bridge  
The ETX-1p bridge is a Layer-2 networking device that creates a single, aggregate network from 
multiple communication networks or network segments. ETX-1p supports VLAN-unaware bridge and 
VLAN-aware bridge. 
Applicability and Scaling 
ETX-1p supports a single bridge, up to 63 bridge ports, and at least 512 MAC entries. Bridge ports can be 
bound uniquely to Ethernet ports. Only one bridge port can be assigned to a specific port.  
The ETX-1p bridge is a Layer-2 forwarding entity that can work in VLAN-aware or VLAN-unaware mode. 
Standards Compliance 
IEEE 802.1D 
IEEE 802.1Q 
Benefits 
The bridge enables performing local switching. 
7. Traffic Processing 
Functional Description 
Architecture  
The bridge is one of the networking components that can perform layer-2 connectivity between 
ethernet ports. The bridge can be connected to the router as host or layer-3 forwarder. 
Packet Walkthrough in VLAN-Unaware Mode 
The ETX-1p bridge in VLAN-unaware mode supports the following packet walkthrough: 
• 
The bridge receives all packets (no restrictions). 
• 
In Filter mode, the bridge learns the packet source MAC address and adds it to the MAC table 
with the corresponding source port. 
• 
The bridge forwards multicast and unicast packets, as follows: 
 
Flood broadcast – The bridge forwards multicast packets to all ports (except the packet 
source port). 
 
The bridge forwards unicast packets to the destination port: 
 
According to the packet’s destination in the MAC table (entries are dynamic provided by 
learning source MAC addresses or static by configuration) 
 
Flooded to all ports (except the packet source port) in case of a destination MAC that 
does not exist in the MAC table 
 
Flooded to all ports (except packet source port) in case of transparent mode 
• 
The bridge transmits packet as is (no modifications) 
 
Note 
In VLAN-unaware mode, legal packets are always forwarded (to a specific port 
or flooded to all ports). 
Packet Walkthrough in VLAN-Aware Mode 
The ETX-1p bridge in VLAN-aware mode forwards packets according to MAC address and VLAN, that is, 
by creating VLAN domains on the bridge.  
It supports VLAN membership table that defines VLAN membership per bridge port as follows: 
• 
By default, a port doesn’t have VLAN membership.  
• 
VLAN domain is defined by configuration and includes all ports with a specific VLAN 
membership. 
7. Traffic Processing 
• 
VLAN membership table defines whether Egress bridge port transmits packets with or without 
VLAN tag. 
The ETX-1p bridge in VLAN-aware mode supports the following packet walkthrough: 
• 
The bridge receives packets according to the port definition: 
 
In case of enabled Ingress filtering, ETX-1p discards incoming frames for VLANs that do not 
include the port in their members set. In case of disabled Ingress filtering, the port accepts 
all incoming frames. 
 
In case of Accept frame type set to tag-only, the bridge discards untagged frames received 
at the port. If it is set to all, untagged frames received at the port are accepted and assigned 
to a VID based on the VID set for this port (VLAN ID). 
• 
In Filter mode, the bridge learns the packet source MAC address and VLAN per VLAN domain 
and adds it to the MAC table with the corresponding source port. 
• 
The bridge forwards as follows: 
 
Flood broadcast – The bridge forwards multicast packets per VLAN domain to all ports 
(except packet source port) 
 
The bridge forwards unicast packets to the destination port per VLAN domain: 
 
According to the packet’s destination in the MAC table (entries are dynamic provided by 
learning source MAC addresses or static by configuration) 
 
Flooded per VLAN domain to all ports (except the packet source port) in case of a 
destination MAC that does not exist in the MAC table 
 
Flooded per VLAN domain to all ports (except packet source port) in case of transparent 
mode 
• 
The bridge transmits packets according to port definitions in VLAN membership table: 
 
Tagged – the bridge transmits with VLAN tag 
 
Untagged – the bridge transmits without VLAN tag 
In VLAN-aware mode, the ETX-1pbridge can stack or strip VLAN tags on an ingress bridge port to achieve 
double-VLAN support. 
VLAN Membership 
ETX-1p bridge supports VLAN domain definition per bridge entity, in VLAN-aware mode only. 
For each VLAN domain, ETX-1pbridge supports the following VLAN membership table configuration 
parameters: 
• 
VLAN-ID 
7. Traffic Processing 
• 
Egress tagged ports (the ports belong to VLAN domain and transmit tagged packets) 
• 
Egress untagged ports (the ports belong to VLAN domain and transmit untagged packets) 
MAC Table 
ETX-1p bridge erases MAC table every aging time period, implementing by this MAC table aging 
mechanism. 
It can clear MAC table learned entities with MAC table clear command.  
ETX-1pbridge supports the following static MAC configuration parameters: 
• 
Available for VLAN-aware mode only 
• 
Add / remove static entry 
• 
Static entries include: 
 
VLAN 
 
MAC address 
 
Bridge port 
ETX-1p bridge supports MAC table show with the following information 
• 
MAC address 
• 
Received bridge port 
Bridge Operation 
The device design supports up to 63 bridge ports, belonging to bridge 1. Port 64 is Internal ethernet 
switch port. 
VLAN unaware bridge operates as follows: once the user activates the bridge ports and binds them to 
the physical port, the activated bridge ports are forwarding traffic. 
VLAN aware bridge operates as follows: once the user activates the bridge ports, binds them to the 
physical port and defines VLAN membership for bridge ports, only the activated bridge ports with VLAN 
membership are forwarding traffic. 
Binding Ethernet ports to a bridge port and enabling it is allowed only when the bridge port is not bound 
to an upper layer (router interface or Multipath entity). 
7. Traffic Processing 
Factory Defaults 
By default, no bridge is configured in ETX-1p. When you create a bridge, by default it does not contain 
any bridge ports. 
The following table shows the default configuration of a bridge and bridge port once they are created. 
Parameter 
Description 
Default Value 
name 
Bridge name 
BRIDGE <bridge-number> 
filtering 
Bridge forwarding mode 
enable 
vlan-aware 
 
disable 
aging-time 
Aging time for MAC table entries 
300 
vlan 
Configure aware bridge VLAN membership 
no VLANS 
Bridge Port 
 
 
name 
Bridge port name 
BP <port-number> 
shutdown 
Administrative status of bridge port 
shutdown 
accept-frame-type 
Accepting all received packets 
all 
bind 
Bind bridge port to lower layer 
no bind 
ingress-filtering 
Enable ingress filtering 
disable 
ingress-tag-handling 
Defines ingress VLAN stacking/stripping mode and effects 
the egress direction with the opposite operation 
none 
pvid 
Configure PVID 
1 
Configuring the Bridge 
 To configure the bridge: 
1. At the config# prompt, enter bridge1. 
6. At the prompt, enter all necessary commands according to the tasks listed below. 
 
Note 
Creating a bridge is allowed only when its ports are not bound to any entity 
and have no configuration of ACL, QoS, PBR and force-next-hop. 
 
7. Traffic Processing 
Note 
Deleting a bridge (no bridge <number>) is allowed only when all bridge ports 
are not active. 
 
Task 
Command 
Comments 
Defining aging time for 
MAC table entries 
(seconds) 
aging-time <seconds>  
seconds – aging time 
Possible values: 60 – 15300 sec 
MAC table is erased every aging time period. 
Clearing MAC table 
learned MAC addresses 
clear-mac-table 
 
Enabling/disabling filtering 
forwarding mode 
filtering 
no filtering 
filtering: 
• For VLAN-unaware mode, enables filtering 
frames received according to the learned MAC 
address  
• For VLAN-aware mode, enables filtering frames 
received according to the learned MAC address 
and VLAN 
no filtering: 
• For VLAN-unaware mode, enables transparent 
bridge forwarding mode. In this mode, the 
bridge forwards all frames received to all ports 
(flooding) 
• For VLAN-aware mode, VLAN-aware 
transparent forwarding 
Assigning a name to the 
bridge  
[no] name <bridge-name> 
bridge-name – name assigned to bridge 
Possible values: 1-32 character string 
To delete the bridge name, type no name. 
Defining the behavior and 
attributes of bridge ports 
port <port-number> 
Possible values: 1-63 
To delete a bridge port, enter 
no port <port-number>. 
Note: You can delete a bridge port only if it is not 
active. 
For detailed configuration of bridge ports, see 
Configuring Bridge Ports. 
7. Traffic Processing 
Task 
Command 
Comments 
Configuring static MAC 
address entry in MAC table 
[no] static-mac <vlan-id> 
<mac-address> <bridge-
port> 
Appears in vlan-aware mode only. 
vlan-id – Possible values: 1–4094 
mac-address – xx-xx-xx-xx-xx-xx (hex format, 
x=0..F) 
bridge-port – bridge port number 
To delete a static MAC address entry from the MAC 
table, type no static-mac <vlan-id> <mac-address> 
<bridge-port> 
Displaying MAC address 
table  
show mac-address-table  
See Viewing MAC Table 
Displaying VLAN members 
show vlans 
See Viewing VLANs 
Displaying the bridge ports 
number, status, and 
Ethernet ports bound to 
them 
show summary 
Appears in vlan-aware mode only 
See Viewing Bridge Status  
 
Defining VLAN 
membership specifications 
vlan <vlan-id> 
no vlan <vlan-id> 
Appears in vlan-aware mode only 
Possible values: 1–4094 
Type no vlan <vlan-id> to delete the VLAN from the 
VLAN membership table. 
See Configuring VLAN 
Enabling or disabling Layer 
2 bridging according to the 
VLAN tag 
vlan-aware 
no vlan-aware 
You can change the mode only when there are no 
active bridge ports. 
Configuring Bridge Ports 
The following commands are available in the port level, at the config>bridge(<bridge-
number>)>port(<port-number>)# prompt.   
Note that static port 64 is reserved for switching and is automatically connected to switch1 port.  
Task 
Command 
Comments 
Defining whether to accept 
all packets or VLAN-tagged 
packets only 
accept-frame-type {all | vlan-only} 
Appears in vlan-aware mode only 
7. Traffic Processing 
Task 
Command 
Comments 
Binding a bridge port to 
physical or virtual port  
bind ethernet <port name> 
no bind 
 
Notes:  
• You can bind only one bridge port to a 
specific port. 
• You can bind the bridge port only to an 
existing port that is not bound to any entity, 
such as router interface or another bridge 
port.  
• You can enter no bind to remove a bound 
port. 
Bind options are any Ethernet port apart from 
Ethernet switch1. 
Enabling/disabling ingress 
filtering according to 
defined VLANs 
ingress-filtering 
no ingress-filtering 
Appears in vlan-aware mode only  
When ingress filtering is enabled, ETX-1p 
discards incoming frames for VLANs that do not 
include the port in their member set.   
When it is disabled, the port accepts all incoming 
frames. 
Assigning a name to the 
bridge port 
[no] name <port-name> 
port-name – bridge port name 
Possible values: 1-32 character string 
To delete the bridge port name, enter no name. 
Assigning default port 
VLAN ID to untagged 
traffic 
pvid <vlan-id> 
Appears in vlan-aware mode only  
Possible values: 1 – 4094 
Administratively 
enabling/disabling the 
bridge port 
[no] shutdown 
To administratively disable the bridge port, enter 
shutdown. 
Setting the port to ‘no shutdown’ is allowed only 
when port is not bound to another bridge port.  
Note:  Shutting down the bridge port does not 
stop the traffic. 
Configuring VLAN 
The following commands are available in the vlan level, at the config>bridge(<bridge-
number>)>vlan(<vlan-id>)# prompt.  
 
7. Traffic Processing 
Task 
Command 
Comments 
Defining a list of egress tagged ports 
tagged-port <port-list> 
no tagged-port <port-list> 
 
Defining a list of egress untagged ports 
untagged-port <port-list> 
no untagged-port <port-list> 
 
Examples 
Note 
To configure the bridge, you have first to delete the default router interface. 
 To configure a VLAN-unaware bridge: 
echo "Port Configuration" 
#   Port Configuration 
    port 
        ethernet wan2            //**Connecting the port to traffic generator**// 
            no shutdown 
        exit 
        ethernet lan3//**Connecting the port to traffic generator**// 
            no shutdown 
        exit 
        ethernet lan4 //**Connecting the port to traffic generator**// 
            no shutdown 
        exit 
    exit 
    echo "Bridge Configuration" 
#   Bridge Configuration 
    bridge 1  //**Configuring bridge 1, by default it’s vlan unaware**// 
        echo "Bridge Port Configuration" 
#       Bridge Port Configuration 
        port 1 
            bind ethernet 2 //**Binding the port connected to traffic generator**// 
            no shutdown 
        exit 
        port 2 
            bind ethernet lan4 //**Binding the port connected to traffic generator**// 
            no shutdown 
        exit 
        port 3 
            bind ethernet lan3  //**Binding the port connected to traffic generator**// 
            no shutdown 
        exit 
        port 64 
            bind ethernet switch1 /**Binding switch1 port**// 
            no shutdown 
7. Traffic Processing 
        exit 
    exit 
    router 1 
        name "Router#1" 
        interface 1 //**Creating router interface to connect to switch port that is 
connected to bridge**// 
            address 2.2.2.5/24 
            bind ethernet switch1 //**Binding to switch port**// 
            no shutdown 
        exit 
    exit 
 To configure a VLAN-aware bridge: 
    echo "Port Configuration" 
#   Port Configuration 
    port 
        ethernet wan2 //**Connecting the port to traffic generator**// 
            no shutdown 
        exit 
        ethernet lan4 //**Connecting the port to traffic generator**// 
            no shutdown 
        exit 
        ethernet switch1 //**Configuring switch port**// 
            vlan 200           //**Configuring VLAN at switch port**// 
                no shutdown   //**Activating VLAN **// 
            exit 
        exit 
    exit 
    
echo "Bridge Configuration" 
#   Bridge Configuration 
    bridge 1                     //**Configuring bridge 1**// 
        vlan-aware           //**Enabling vlan aware mode**// 
 
               filtering 
        static-mac 300 00-11-22-33-44-55 1 
        echo "VLAN Configuration" 
#       VLAN Configuration 
 
        vlan 200 //**Configuring vlan at bridge**// 
            tagged-port 1,64 //**Configure vlan tagged ports**// 
 
        exit 
        vlan 300 //**Configuring vlan at bridge**// 
            tagged-port 1..2 //**Configure vlan tagged ports**// 
        exit 
        echo "Bridge Port Configuration" 
#       Bridge Port Configuration 
        port 1 
            bind ethernet wan2        //**Connecting the port to traffic generator**// 
 
7. Traffic Processing 
            no shutdown 
        exit 
        port 2 
            bind ethernet lan4  //**Connecting the port to traffic generator**// 
            no shutdown 
        exit 
        port 64 
            bind ethernet switch1 
            no shutdown 
        exit 
    exit 
    router 1 
        name "Router#1"  //**Creating router interface to be connected to the switch port     
which is connected to the bridge**// 
 
        interface 1 
            address 2.2.2.5/24 
            bind ethernet switch1 vlan 200 //**Binding to switch port with the 
            same vlan**// 
 
            no shutdown 
        exit 
    exit 
 
Viewing Bridge Status 
Viewing Bridge Summary 
 To display the bridge summary: 
• 
At the config>bridge(bridge_number)# prompt, enter show summary. 
The summary is displayed.  
config>bridge(1)# show summary 
Num  Admin Status                  Bind 
----------------------------------------------------------------------------- 
1    Up                            Eth wan2 
2    Up                            Eth lan4 
3    Up                            Eth lan3 
64   Up                            Eth switch 
The above fields are: 
Num 
Bridge port number 
7. Traffic Processing 
Admin Status 
Entry status  
Possible values: Up, Down 
Bind 
Port the bridge port bound to 
Viewing MAC Table 
You can display the MAC table, which provides information on static and dynamic addresses, and the 
bridge ports associated with them. 
 To display the MAC address table: 
• 
At the config>bridge(bridge number)# prompt, enter show mac-address-table all. 
The MAC address table is displayed. 
 
Note 
ETX-1p displays only the first 1000 entries. To view the entire MAC table, 
download it to your PC using SFTP. For this, refer to File Operations. 
 
VLAN-unaware mode: 
config>bridge(1)# show mac-address-table all  
 
VLAN-aware mode: 
config>bridge(1)# show mac-address-table all 
Total MAC Addresses   : 3 
Static MAC Addresses  : 1 
Dynamic MAC Addresses : 2 
 
 
VLAN  Static MAC Address  Port Status 
----------------------------------------------------------------------------- 
100   12-12-12-11-15-14   1    Static 
 
VLAN  Learned MAC Address Port Status 
----------------------------------------------------------------------------- 
100   00-10-94-00-00-06   3    Dynamic 
100   00-55-66-77-01-42   1    Dynamic 
 
VLAN-unaware mode: 
config>bridge(1)# show mac-address-table all 
Total MAC Addresses   : 3 
7. Traffic Processing 
Static MAC Addresses  : 1 
Dynamic MAC Addresses : 2 
 
Static MAC Address  Port Status 
----------------------------------------------------------------------------- 
12-12-12-11-15-14   1    Static 
 
Learned MAC Address Port Status 
----------------------------------------------------------------------------- 
00-10-94-00-00-06   3    Dynamic 
00-55-66-77-01-42   1    Dynamic 
The above fields are: 
Total MAC Addresses 
Total number of entries in the MAC address table 
Static MAC Addresses 
Number of static entries in the MAC address table 
Dynamic MAC Addresses 
Number of dynamic entries in the MAC address table 
VLAN 
VLAN ID domain 
MAC Address 
Learned MAC address in MAC Address table 
Port 
Received bridge port 
Status 
Entry status  
Possible values: Static, Dynamic 
Viewing VLANS 
 To display VLAN domain members: 
• 
At the config>bridge(bridge_number)# prompt, enter show vlans. 
The VLAN members are displayed per VLAN. 
config>bridge(1)# show vlans 
 
VLAN ID        : 100 
-------------- : 
 
Tagged Ports   : 1..4 
Untagged Ports : 0 

## 7.2 DMVPN  *(p.435)*

7. Traffic Processing 
Configuration Errors 
ETX-1p generates the following messages when it detects a configuration error. 
Message 
Cause 
Corrective Action 
Port does not exist 
You tried binding the bridge port to a port 
that does not exist. 
Select another port that does exist, 
or create a port and then bind the 
bridge port to it. 
Port is already bound 
You tried binding the bridge port to a port 
that is already bound to another entity. 
Unbind the port from the other 
entity. 
Upper layer is bound to 
bridge port 
You tried to delete a bridge while there are 
ports bound by upper layer entity 
Unbind the port from the upper 
layer entity 
Cannot modify – there 
are active bridge ports” 
You tried to change the VLAN 
aware/unaware mode on a bridge with 
active bridge ports 
Set admin status of the active 
bridge ports to “down”, then you 
can change the bridge mode 
Cannot modify – bridge 
port is active  
You tried to unbind or modify an active 
bridge port 
Set admin status of the active 
bridge ports to “down”, then you 
can unbind or modify it. 
Cannot bind – port do not 
exist 
You tried to bind a non-existing port 
 
Cannot modify – bridge 
port is not bound 
You tried to enable a bridge port, which is 
not bound to a lower layer port. 
Bound the bridge port to a lower 
layer port. 
Bridge port is already 
assigned to membership 
list 
You tried to add a bridge port that is already 
assigned to another membership set 
Exclude the bridge port from 
another membership set, then you 
can add it to the new list 
7.2 DMVPN  
Dynamic Multipoint Virtual Private Network (DMVPN) is a technology that simplifies the configuration 
and management of large-scale VPN networks. It is widely used for enabling secure communication 
between multiple sites, such as branch offices and headquarters, over the Internet or private networks. 
DMVPN automates the process of establishing dynamic and scalable VPN tunnels between remote 
locations, reducing administrative overhead compared to traditional VPN solutions. 
7. Traffic Processing 
Applicability and Scaling 
This feature is applicable to all versions of ETX-1p.  
Standards Compliance  
RFC 2784 
Generic Routing Encapsulation (GRE) 
RFC 4087 
IP Tunnel MIB 
RFC 2332 
NBMA Next Hop Resolution Protocol (NHRP) 
Benefits 
DMVPN is ideal for organizations requiring a flexible, scalable VPN solution that can adapt to changing 
network requirements while maintaining security and efficiency. 
Benefits of DMVPN are as follows: 
• 
Cost Efficiency: Uses the Internet or shared infrastructure instead of dedicated leased lines. 
• 
Reduced Complexity: Minimal manual configuration of tunnels. 
• 
Improved Performance: Direct spoke-to-spoke tunnels reduce latency and optimize traffic paths. 
• 
Centralized Management: Centralized hub simplifies network management and policy 
enforcement. 
Functional Description 
The DMVPN solution uses a combination of the following protocols described in this chapter: 
Protocol 
Functionality 
Described in Section 
NHRP (Next Hop Resolution 
Protocol) 
Dynamically resolves public IPs for 
direct spoke-to-hub and spoke-to-
spoke tunnels 
GRE Tunneling 
GRE (Generic Routing 
Encapsulation),  
mGRE (Multipoint GRE) 
Encapsulates traffic for transport 
across the VPN 
GRE Tunneling 
7. Traffic Processing 
Protocol 
Functionality 
Described in Section 
IPsec (Internet Protocol Security) 
Provides encryption and security 
for VPN traffic 
IPsec 
Dynamic Routing Protocols  
Manages scalable routing, such as 
OSPF or BGP 
Routing Protocol BGP 
Routing Protocol OSPF 
 
DMVPN is usually divided into three phases: 
• 
Phase 1: Hub-and-spoke only; all traffic flows through the hub. 
• 
Phase 2: Enables direct spoke-to-spoke tunnels for optimized traffic flow. 
• 
Phase 3: Adds route summarization and dynamic redirection for improved scalability and 
efficiency. 
DMVPN works over public or private networks, including broadband Internet connections. It supports 
routing protocols like OSPF or BGP for scalable and flexible routing between sites. 
DMVPN is configured as a hub-and-spoke model with dynamic spoke-to-spoke tunnels. Initially, traffic 
flows through a central hub (hub-and-spoke topology). Spokes (remote sites) can dynamically establish 
direct tunnels with each other (spoke-to-spoke communication) without passing through the hub, 
reducing latency and bandwidth usage. 
This topology supports large-scale deployments with many remote sites. Dynamic configuration 
eliminates the need to manually set up tunnels between every pair of sites. 
NHRP (Next Hop Resolution Protocol) allows spokes to dynamically discover each other's public IP 
addresses and establish direct tunnels. 
Configuring DMVPN 
 To configure DMVPN: 
1. Navigate to configure router <number> to select the router interface on which to configure GRE 
tunneling.  
2. At the config>router(<number>)# prompt that is displayed, enter  
tunnel-interface <number> gre-ip 
The config>router(<number>)>tunnel-interface(<number>) is displayed. 
The tunnel is identified by this number. 
3. Configure GRE tunnel parameters (see GRE Tunneling) 

## 7.3 GRE Tunneling  *(p.438)*

7. Traffic Processing 
4. Configure NHRP parameters (see GRE Tunneling) 
5. In case of using SPOKE-to-SPOKE feature (DMVPN phase 2,3) – configure ‘multipoint’ (see GRE 
Tunneling) 
6. In case of secured VPN, create crypto-map profile and attach it to the tunnel-interface (see IPsec) 
7. In case of using routing protocols – configure routing protocol over the tunnel (see the 
corresponding section: Routing protocol BGP, Routing protocol OSPF, etc.) 
 
Viewing DMVPN Status 
See Viewing GRE Status  
7.3 GRE Tunneling  
ETX-1p supports Generic Routing Encapsulation (GRE) protocol, which sets up point-to-point tunnels 
between two sites and encapsulates other protocols. ETX-1p supports point-to-point GRE spoke 
functionality. 
Applicability and Scaling 
This feature is applicable to all versions of ETX-1p.  
Standards Compliance 
RFC 2784 
Generic Routing Encapsulation (GRE) 
RFC 4087 
IP Tunnel MIB 
RFC 2332 
NBMA Next Hop Resolution Protocol (NHRP) 
7. Traffic Processing 
Functional Description 
The terminology used in this section is described in the following table: 
Term 
Stands For 
Description 
GRE 
Generic Routing 
Encapsulation 
Protocol that sets up point-to-point tunnels between two sites and 
encapsulates other protocols 
Hub 
 
Central router 
Spoke 
 
All devices that contact the hub (central router) 
NBMA 
Non-Broadcast Multi 
Access 
Network to which multiple hosts are attached, but data is transmitted 
directly from one host to another over a virtual circuit 
NHC 
Next Hop Client 
Entity that initiates NHRP requests to obtain access to the NHRP service 
NHRP 
Next Hop Resolution 
Protocol 
ARP-like protocol that dynamically maps NBMA network 
NHS 
Next Hop Server 
Entity performing the NHRP service within the NBMA cloud 
GRE Tunneling 
GRE tunneling is accomplished through routable tunnel endpoints that operate on top of existing 
endpoints. 
Routers use GRE to send traffic through an intervening network that does not support the protocols or 
addresses of incoming packets. GRE encapsulates packets into another IP packet + IP header. For 
example, you can create an IPv4 tunnel to send IPv6 traffic through a network that handles IPv4 traffic. 
The device complies with the Generic Routing Encapsulation standard (RFC 2784). 
A GRE encapsulated packet has the form: 
 
    --------------------------------- 
    |       Delivery Header         | 
    --------------------------------- 
    |       GRE Header              | 
    --------------------------------- 
    |       Payload packet          | 
    --------------------------------- 
ETX-1p supports configuration of up to 30 tunnel interfaces under the router level.  
7. Traffic Processing 
You can configure the tunnel MTU, or calculate it based on the MTU of the media the tunnel passes 
through. 
ETX-1p supports IP fragmentation and defragmentation in tunnels, for packets that are larger than the 
tunnel IP MTU. 
Both delivery (encapsulating) and payload (encapsulated) protocols can be either IPv4 or IPv6, 
independently of each other. 
A GRE tunnel remains operationally up once you configure it with the following: 
• 
A valid tunnel source address or interface 
• 
A valid, routable tunnel destination IP address 
• 
A valid IP address for the tunnel 
A GRE tunnel becomes operationally down under any of the following conditions: 
• 
There is no route to the tunnel destination address. 
• 
The interface that anchors the tunnel source is down. 
• 
The route to the tunnel destination address is through the tunnel itself. 
Multipoint Tunnels  
You can configure a GRE IP tunnel as multipoint. When multipoint is enabled, the device (as a client) can 
open spoke-to-spoke tunnels based on mapping information it gets from the hub in NHRP resolution-
reply messages. 
The tunnel IP address prefix length (as configured by ip-address in the same level) has to be configured. 
Multipoint tunnels ignore the prefix and use 32 bits length. The prefix will become effective if no 
multipoint is configured. 
NHRP  
The device conforms to the NHRP standard [RFC 2332] but at the current stage implements only a 
portion of the standard.  
Note: NHRP (NBMA Next Hop Resolution Protocol) configuration and functionality apply to GRE tunnels, 
being irrelevant to other tunnels (e.g. native IPsec). 
The device supports periodic sending of registration requests from a client (NHC) to a single 
preconfigured server, as well as resolution requests and replies (if multipoint GRE is configured). Other 
packets are silently dropped if received. 
7. Traffic Processing 
The NHRP NHS (to which registration requests would be sent) can be configured per tunnel. For this 
purpose, you have to provide the NHS logical IP address. 
The logical address can be mapped to NBMA addresses. This is configured via NHRP mapping. 
When multipoint GRE is configured, the NHRP client maintains a cache of dynamic address mappings (of 
spokes it opens direct tunnels with) learned from resolution reply packets sent by the hub.  
NHRP packets consist of a fixed part, a mandatory part and an extensions part. The fixed part is common 
to all NHRP packet types. The mandatory part must be present but varies depending on packet type. The 
extensions part also varies depending on packet type and need not be present. This part is currently not 
supported by the device. 
Factory Defaults 
Parameter 
Description 
Default Value 
ip-mtu 
IP MTU of tunnel 
For IPv4 – 1476 
For IPv6 - 1456 
nhrp-registration-
timeout 
NHRP registration timeout 
 
no nhrp-registration-
timeout (hardcoded at 2400 
sec) 
multipoint 
Tunnel configured as multipoint  
no multipoint 
Configuring Tunneling 
Use the commands in the following procedure to create a point-to-point GRE tunnel. 
• 
Configure tunnel address – the IP address defined on the tunnel interface 
• 
Configure tunnel source.  
• 
Configure tunnel destination.  
 To configure tunneling: 
1. Navigate to configure router <number> to select the router interface on which to configure GRE 
tunneling.  
2. At the config>router(<number>)# prompt that is displayed, enter  
tunnel-interface <number> gre-ip 
7. Traffic Processing 
The config>router(<number>)>tunnel-interface(<number>) is displayed. 
The tunnel is identified by this number. 
3.  Enter all necessary commands according to the tasks listed below.  
 
Task 
Command 
Comments 
Defining tunnel IP address 
and prefix length 
ip-address <ip-address/prefix-
length> 
Entering no ip-address removes the 
tunnel IP address. 
ip-address – valid unicast IPv4 or non-
link-local IPv6 address with compatible 
prefix length 
Notes: 
• A tunnel can have only one 
address. If you repeat the 
command, the last instance applies. 
• The tunnel address cannot be the 
address of another tunnel or of a 
router interface. 
• Both ends of the tunnel should be 
on the same network. 
Defining tunnel IP MTU 
ip-mtu <number> 
 
Entering no ip-mtu removes IP MTU 
from the tunnel interface. 
Possible values: 0 (no IP MTU),  
128-65535 
Note: 0 means that the MTU is to be 
calculated according to the delivery 
protocol. For IPv4 it is 1476 and for 
IPv6 1456. 
Clearing the NHRP cache 
of learned mappings 
clear-nhrp 
Relevant only for GRE tunnel 
configured as multipoint  
Configuring the tunnel as 
multipoint  
multipoint  
[no] multipoint  
Tunnel type is gre-ip 
Configuring NHRP mapping 
nhrp-map <logical-ip-address> 
<nbma-ip-address> 
no nhrp-map <logical-ip-
address> <nbma-ip-address> 
 
logical-ip-address that will be mapped 
to NBMA address – valid unicast IP 
address 
nbma-ip-address – valid unicast IP 
address 
Only one mapping may be configured 
per tunnel.  
7. Traffic Processing 
Task 
Command 
Comments 
Configuring the NHRP 
server 
nhrp-nhs <ip-address> 
no nhrp-nhs <ip-address> 
 
ip-address must be a valid unicast IP 
address  
Only one NHS can be configured per 
tunnel 
Configuring NHRP 
registration timeout 
nhrp-registration-timeout 
<1..65535 seconds> 
no nhrp-registration-timeout 
 
Binding PBR rule to the 
port  
policy-based-route priority 
<priority> match-acl <name> 
{next-hop <ip-address>} 
interface <type, index> 
no policy-based-route priority 
<priority> 
See Configuring PBR 
 
Displaying tunnel status 
show status 
See Viewing GRE Status 
Defining tunnel 
destination IP address 
tunnel-destination <ip-
address> 
Entering no tunnel-destination 
removes the address.  
Possible values: Valid unicast IPv4 or 
non-link-local IPv6 address 
Notes: The source and destination 
addresses must be both IPv4 or IPv6. 
This command is not available for 
multipoint tunnels. 
Configuring GREoIPsec 
underlay destination 
 
tunnel-underlay-destination 
<IP address> 
 
Entering no tunnel-underlay-
destination removes the address. 
Possible values: Valid unicast IPv4 or 
non-link-local IPv6 address 
Notes: The source and destination 
addresses must be both IPv4 or IPv6. 
Configuring GREoIPsec 
underlay source 
tunnel-underlay-source [<ip-
address>] [router-interface 
<number>] 
Entering no tunnel-underlay-source 
removes the address. 
Possible values:  
ip-address – valid unicast IPv4 or non-
link local IPv6 address 
number - number of a non-loopback 
router interface 
Notes: 
7. Traffic Processing 
Task 
Command 
Comments 
• Either IP address or router 
interface number must be defined; 
not both. 
• The tunnel and the router interface 
anchoring it must be on the same 
router. 
The source and destination addresses 
must be both IPv4 or IPv6. 
Defining source IP address 
or router interface number 
used to bind the tunnel to 
a router interface 
tunnel-source [<ip-address>] 
[router-interface <number>] 
Entering no tunnel-source removes 
the address. 
Possible values:  
ip-address – valid unicast IPv4 or non-
link local IPv6 address 
number - number of a non-loopback 
router interface 
Notes: 
• Either IP address or router 
interface number must be defined; 
not both. 
• The tunnel and the router interface 
anchoring it must be on the same 
router. 
• The source and destination 
addresses must be both IPv4 or 
IPv6. 
Viewing the channel status 
show status [all] [nhrp] 
[dmvpn] 
See Viewing GRE Status below 
 To remove a GRE tunnel: 
1. Navigate to configure router <number> to select the router interface from which to remove a GRE 
tunnel.  
2. At the config>router(<number>)# prompt that is displayed, enter no tunnel-interface <number>. 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
7. Traffic Processing 
Message 
Cause 
Corrective Action 
Tunnel exists with a different 
type 
You tried changing the type of 
an existing tunnel.  
Create a new tunnel of the new type. 
Maximum number of tunnels 
exceeded 
You tried to create more 
tunnels than your device allows 
(30).  
 
Invalid address; enter a unicast 
address 
You tried to enter a broadcast 
or multicast address as the 
tunnel address.  
Enter a valid unicast IPv4 or IPv6 address 
with a compatible prefix-length. 
The address is assigned to 
another interface 
You tried to configure the 
tunnel with an address of an 
already existing tunnel or 
router interface.  
Assign a unique address to the tunnel. 
Configure either source address 
or interface, not both 
You tried to configure the 
router interface anchoring the 
tunnel with both an address 
and interface. 
Remove one of the configurations: 
either the address or interface. 
Source and destination must be 
both IPv4 or both IPv6 
You tried to configure tunnel 
destination with an IPv4 
address while the tunnel source 
is an IPv6 address. 
You tried to configure tunnel 
source with an IPv4 address 
while the tunnel destination is 
an IPv6 address. 
Define destination and source with same 
type of IP address – both IPv4 or both 
IPv6. 
Invalid address; enter a unicast 
address  
You tried to enter a broadcast 
or multicast logical or NBMA 
address.  
Enter a valid IP unicast address (at this 
phase it is usually the public address of 
the other side of the tunnel, which is the 
tunnel destination). 
Too many mappings 
Only one NHRP mapping can be 
configured per tunnel, you tried 
to configure more.  
 
No such mapping 
You tried to delete a 
nonexistent NHRP mapping  
 
Too many NHS 
Only one NHS can be 
configured per tunnel, you tried 
to configure more.  
 
7. Traffic Processing 
Message 
Cause 
Corrective Action 
No such NHS 
You tried to delete a 
nonexistent NHS 
 
Examples 
 To configure a tunnel from Router A to Router B: 
# Router A 
tunnel-interface 1 gre-ip 
                tunnel-source 2.2.2.2 
                tunnel-destination 2.2.2.1 
                ip-address 10.10.10.1/30 
            exit 
 To configure a tunnel from Router B to Router A: 
# Router B 
tunnel-interface 1 gre-ip 
                tunnel-source 2.2.2.1 
                tunnel-destination 2.2.2.2 
                ip-address 10.10.10.2/30 
            exit 
Viewing GRE Status 
You can display the current GRE tunnel status with the following commands: 
• 
show status – shows the status of the VPN connected to the HUB 
• 
show status nhrp – shows the NHRP information 
• 
show status dmvpn – shows SPOKE-to-SPOKE dynamic VPNs information 
 To display NHRP status: 
• 
At the config>router(<number>)>tunnel-interface(<number>)# prompt, enter: 
show status nhrp 
The GRE tunnel NHRP status displays the following: 
 
The NHS IP address 
 
For each NHRP entry: 
7. Traffic Processing 
 
NHRP type (nhs/local/static/dynamic/incomplete/negative) 
 
Logical address 
 
NBMA address 
config>router(1)>tunnel-interface(1)# show status nhrp 
Missing Configuration 
----------------------------------------------------------------------------- 
Anchoring Router Interface Not Configured 
NHRP Map Not Configured 
 
NHRP Information 
------------------ 
 
NHS : 70.0.0.4 
 
 
 
Type          Logical                                  NBMA 
----------------------------------------------------------------------------- 
dynamic      22.22.22.100                             172.17.232.72 
dynamic      33.33.33.100                             172.17.232.73 
dynamic      70.0.0.1                                 172.17.232.72 
dynamic      70.0.0.2                                 172.17.232.73 
local        70.0.0.3                                 172.17.232.74 
 
 
 To display DMVPN status: 
• 
At the config>router(<number>)>tunnel-interface(<number>)# prompt, enter: 
show status dmvpn. 
The GRE tunnel DMVPN status displays the following: 
 
For each NHRP entry: 
 
NHRP type (nhs/local/static/dynamic/incomplete/negative) 
 
Logical address 
 
NBMA address 
 
Crypto map name 
 
For each pair of tunnel peers: 
 
SA status (Connecting/Down/Up/Lower Layer Dormant) and SA age (X minutes ago) 
 
IKE in SPI 
 
IKE out SPI  
 
Time to IKE key reauthentication 
 
Transform set status (Down/Up) 
 
Transform set in SPI 
7. Traffic Processing 
 
Transform set out SPI 
 
Transform set remaining lifetime (in kilobytes) 
 
Transform set remaining lifetime (out kilobytes) 
 
Transform set remaining lifetime (in seconds) 
 
Total Tx/Rx SA Statistics (in packets and kilobytes) 
config>router(1)>tunnel-interface(1)# show status dmvpn 
Type          Logical                                  NBMA 
----------------------------------------------------------------------------- 
dynamic      70.0.0.2                                 172.17.233.130 
nhs          70.0.0.4                                 172.17.163.184 
local        70.0.0.8                                 172.17.233.138 
 
 
Crypto Map : dmvpn 
 
Tunnel Peers : 172.17.233.138---172.17.163.184 
 
IKE 
----------------------------------------------------------------------------- 
Status               : Up 39 minutes ago 
Version              : IKEv2 
SA Negotiation Mode  : NA 
Authentication       : Pre-Shared Secret 
Encryption           : AES-CBC-128 
Hashing              : SHA1-96-HMAC 
Diffie Hellman Group : 14 
In SPI               : e8beab447993af2a 
Out SPI              : e51b173cf6e887b1 
Reauthentication in  : 11 minutes 
 
Transform Set 
----------------------------------------------------------------------------- 
Encapsulation : Transport 
Algorithms    : ESP-AES-CBC-128 ESP-SHA1-96-HMAC 
PFS Group     : 14 
In SPI        : 00000000c779cfb6 
Out SPI       : 000000001d6d6299 
 
Remaining Lifetime 
----------------------------------------------------------------------------- 
In Kilobytes  : 0 
Out Kilobytes : 0 
Seconds       : 1012 
 
 
 
Tunnel Peers : 172.17.233.138---172.17.233.130 
 
Status               : Up 1 minutes ago 
In SPI               : 4c222865783a1c14 
7. Traffic Processing 
Out SPI              : 5be47803b6213799 
Reauthentication in  : 57 minutes 
Transform Set Status : Up 
In SPI               : 00000000ce86e95c 
Out SPI              : 00000000c9cb05aa 
Reauthentication in  : 57 minutes 
 
Remaining Lifetime 
----------------------------------------------------------------------------- 
In Kilobytes  : 0 
Out Kilobytes : 0 
Seconds       : 1015 
 
Total SA Statistics 
----------------------------------------------------------------------------- 
Tx : 50 packets, 4 kilobytes 
Rx : 41 packets, 3 kilobytes 
 
 
Tunnel Peers : 172.17.233.138---172.17.163.184 
 
Status               : Up 39 minutes ago 
In SPI               : e8beab447993af2a 
Out SPI              : e51b173cf6e887b1 
Reauthentication in  : 11 minutes 
Transform Set Status : Up 
In SPI               : 00000000c779cfb6 
Out SPI              : 000000001d6d6299 
Reauthentication in  : 11 minutes 
 
Remaining Lifetime 
----------------------------------------------------------------------------- 
In Kilobytes  : 0 
Out Kilobytes : 0 
Seconds       : 1012 
 
Total SA Statistics 
----------------------------------------------------------------------------- 
Tx : 400 packets, 30 kilobytes 
Rx : 400 packets, 35 kilobytes 
 To display GRE tunnel status:  
• 
At the config>router(<number>)>tunnel-interface(<number>)# prompt, enter: 
show status. 
The GRE tunnel status is displayed.  
Spoke_C>config>router(1)>tunnel-interface(1)# show status 
Tunnel        : 1 
Name          : Tunnel 
Type          : IP Over GRE 
7. Traffic Processing 
Tunnel Status 
    Admin     : Enabled 
    Oper      : Up 
 
Tunnel Address     : 70.0.0.3/24 
Tunnel Source 
   Interface       : Router Interface 1/1 (Ethernet 6) 
   Address         : -- 
Tunnel destination : -- 
IP MTU             : -- 
 
NHRP Information 
------------------ 
 
NHS : 70.0.0.4 
 
 
Type          Logical                                  NBMA 
----------------------------------------------------------------------------- 
dynamic      22.22.22.100                             172.17.232.72 
dynamic      33.33.33.100                             172.17.232.73 
dynamic      70.0.0.1                                 172.17.232.72 
dynamic      70.0.0.2                                 172.17.232.73 
local        70.0.0.3                                 172.17.232.74 
nhs          70.0.0.4                                 172.17.232.230 
 
Packets Types       Packets              Bytes 
Tunnel Encapsulated 853                  95808 
Tunnel Decapsulated 986                  111505 
Crypto Map : DMVPN 
 
Tunnel Peers : 172.17.232.74---172.17.232.230 
 
IKE 
----------------------------------------------------------------------------- 
Status               : Up 1 minutes ago 
Version              : IKEv2 
SA Negotiation Mode  : NA 
Authentication       : RSA Signature 
Encryption           : AES-CBC-128 
Hashing              : SHA1-96-HMAC 
Diffie Hellman Group : 14 
In SPI               : bbe72a1e6d5e4143 
Out SPI              : 4d580fa51254fffd 
Reauthentication in  : 36 minutes 
 
Transform Set 
----------------------------------------------------------------------------- 
Encapsulation : Transport 
Algorithms    : ESP-AES-CBC-128 ESP-SHA1-96-HMAC 
PFS Group     : 14 
In SPI        : 00000000c0c12721 

## 7.4 IPsec  *(p.451)*

7. Traffic Processing 
Out SPI       : 000000004fe1b877 
 
Remaining Lifetime 
----------------------------------------------------------------------------- 
In Kilobytes  : 0 
Out Kilobytes : 0 
Seconds       : 3277 
 
 
Spoke_C>config>router(1)>tunnel-interface(1)#  
7.4 IPsec  
IPsec is a protocol suite for securing private communication across IP networks. 
ETX-1p supports IPsec on router interfaces having an IPv4 address, with the following main features: 
• 
Tunnel or transport mode  
• 
ESP with the following algorithms: AES CBC 128 and 256, AES GCM 128 and 256, AES GMAC 128 
and 256, null encryption, SHA-1, SHA-2 256 and 512 
• 
DH groups: 
 
1 (768-bit modulus) 
 
2 (1024-bit modulus) 
 
5 (1536-bit modulus) 
 
14 (2048-bit modulus) 
 
19 (256-bit elliptic curve)  
 
20 (384-bit elliptic curve) 
• 
IKEv1 (main and aggressive mode) and IKEv2 
• 
IKE authentication with pre-shared keys 
• 
IKE algorithms AES CBC 128 and 256, SHA-1, SHA-2 256 and 512 
• 
Configurable IKE identities enable IPsec between peers, whose IP address is unknown at the 
time of configuration 
• 
IPsec over GRE 
• 
Policy-based and Route-based IPsec  
• 
Simple redundancy mechanism for route-based IPsec tunnels 
7. Traffic Processing 
• 
IPv4 and IPv6 
• 
NAT traversal 
• 
Transport (underlay) router can differ from the router on which the tunnel is configured. 
IPsec has two modes of operation, tunnel and transport, which is determined during IPsec phase 2. 
• 
In tunnel mode, ETX-1p adds an IPsec header before the original packet, then encapsulates it 
with a new IP header, whose source and destination addresses are those of the tunnel peers. 
This mode is usually used between two gateways protecting the machines behind them. 
• 
In transport mode an IPsec header is inserted after the original IP header, without adding a new 
IP header. This mode is usually used between end stations or when GRE is employed (GRE 
handles the tunneling and adds an encapsulating new IP header).  
IPsec tunnels always ensure the integrity of the traffic they protect. Encryption is optional. ETX-1p 
supports Encapsulating Security Protocol (ESP), which provides both integrity and confidentiality (i.e. 
encryption). ESP operates on top of IP, using IP protocol 50. 
Applicability and Scaling 
This feature is applicable to all the device versions.  
AH is not supported, since similar functionality can be achieved having ESP with null encryption. 
ETX-1p supports up to four proposals (policies). Up to 20 crypto maps can be configured. Up to 20 
transform sets can be configured. 
Standards Compliance 
RFC 5996 
Internet Key Exchange Protocol Version 2 (IKEv2) 
RFC 7383 
Internet Key Exchange Protocol Version 2 (IKEv2) Message Fragmentation 
Benefits 
IPsec automatically secures applications at the IP layer. 
7. Traffic Processing 
Functional Description 
The terminology used in this section is described in the following table: 
Term 
Stands For 
Description 
ESP 
Encapsulating Security Payload 
Protocol that provides origin authenticity, integrity, and 
confidentiality protection of IP packets 
IKE 
Internet Key Exchange 
 
ISAKMP 
Internet Security Association and 
Key Management Protocol  
Provides a framework for agreeing to the format of SA 
attributes, and for negotiating, modifying, and deleting SAs. 
IPsec 
IP Security 
A protocol suite for securing private communication across 
IP networks 
PSK 
Pre-shared key 
Authentication method for IPsec phase-one (IKE) policies 
PFS 
Perfect Forward Secrecy 
 
DH group 
Diffie-Hellman group 
 
SA 
Security Association 
Relationship between two or more entities (VPN Hubs and 
Spokes) that describes how the entities will utilize security 
services to communicate securely. 
Crypto Map 
ETX-1p supports the configuration of crypto maps - IPsec profiles that determine how IPsec tunnels are 
established and maintained. 
Crypto maps define tunnel policies. These policies determine how IPsec processes data packets.  
A valid crypto map should be configured with the following: 
• 
At least one IPsec phase one (IKE) policy  
• 
At least one source and one destination protected network  
• 
Peer address 
• 
At least one transform set  
After a crypto map is configured, and is associated with an operational router interface, ETX-1p 
establishes and maintains an IPsec tunnel. 
You can associate multiple crypto maps with one router interface. For each map, ETX-1p maintains a 
separate tunnel. When a packet enters or has to be forwarded, ETX-1p tries to match it against the 
7. Traffic Processing 
maps’ protected networks in the order of the map sequence numbers (lowest first). If multiple maps 
have the same number, they are checked in the order of their names (lowest first). A packet is handled 
by the first crypto map that matches it. Whatever the map does with it is final, even if the packet 
matches another map (with lower priority). 
Outgoing packets whose source and destination IP addresses match the crypto map protected network 
configuration, are processed by the crypto map before being forwarded. Incoming packets matching the 
configuration (after reversing its source and destination) are expected to be IPsec protected as well. If 
not, they are discarded. 
Packets whose source and destination IP addresses do not match the crypto map protected network 
configuration, are not processed by the crypto map (in both directions). They may be handled by a 
different crypto map, should they match its rules; otherwise, they are forwarded in the clear. 
ETX-1p supports crypto map binding to a router or tunnel interface. A map can be associated with 
multiple interfaces, and multiple maps may be associated with one interface. 
Security Associations (SAs) 
A Security Association (SA) is a relationship between two peers that describes how the entities will 
utilize security services to communicate securely.  
This relationship is represented by a set of information that can be considered a contract between the 
entities. The information must be agreed upon and shared between all the entities. 
ISAKMP (IKE) provides the protocol exchanges to establish a security association between negotiating 
entities followed by the establishment of a security association by these negotiating entities on behalf of 
ESP.  
Each SA (IKE) has its own lifetime. When it expires, the SA is deleted. 
Transform Sets 
ETX-1p supports the configuration of up to 20 transform sets, which define the algorithms to be used in 
IPsec phase 2. 
Internet Security Association and Key Management Protocol (ISAKMP) 
ISAKMP provides a framework for agreeing to the format of SA attributes, and for negotiating, 
modifying, and deleting SAs. 
7. Traffic Processing 
An initial protocol exchange allows a basic set of security attributes to be agreed upon. This basic set 
provides protection for subsequent ISAKMP exchanges. It also indicates the authentication method and 
key exchange that will be performed as part of the ISAKMP protocol. After the basic set of security 
attributes is agreed upon, initial identity authenticated, and required keys generated, the established SA 
can be used for the protection of the VPN tunnels. 
ISAKMP implementation guards against denial of service, replay/reflection, and man-in-the-middle 
(attacks against protocols). 
A security association (SA) is a set of policy and key(s) used to protect information. ISAKMP SA is the 
shared policy and key(s) used by the negotiating peers to protect their communication. 
ISAKMP uses the Internet Key Exchange (IKEv1) for the authentication and encryption establishment. 
Internet Key Exchange (IKE) 
IKE negotiates the IPsec security associations (SAs). This process requires that the IPsec systems first 
authenticate themselves to each other and establish ISAKMP (IKE) shared keys. 
If IKEv2 is configured, the device must support fragmentation by sending 
IKEV2_FRAGMENTATION_SUPPORTED notification in the IKE_SA_INIT exchange. If the peer does not 
support fragmentation, the tunnel is established without fragmentation support. If the peer supports 
fragmentation it is up to the initiator to decide on it. If the device is the initiator, fragmentation is 
available, with MTU of 576 for IPv4 and 1280 for IPv6. 
Phase 1 
In Phase 1, two IPsec peers establish a secure, authenticated channel to communicate. This process is 
called the ISAKMP Security Association (SA) or IKE Security Association. 
The authentication is supported with Pre-Shared Keys. 
Policies 
ETX-1p supports the configuration of up to twenty IPsec phase-one (IKE) policies. 
The following elements are configurable: 
• 
Authentication method (currently only the PSK (Pre-Shared Keys) method is supported.) 
• 
Encryption algorithm 
• 
Key exchange algorithm – Diffie-Hellman group 
7. Traffic Processing 
• 
Hashing algorithm 
• 
SA lifetime 
• 
Exchange mode 
Phase-one policies (i.e. proposals) are globally configured. Each has a sequence number that determines 
its priority (lowest number has the highest priority). They are proposed to the peers in the same order 
by all the IPsec tunnels.  
If IKEv2 is configured, ETX-1p acts as both initiator and responder, that is, it accepts tunnel initiation 
from a peer, and if the peer does not initiate the tunnel, it initiates the tunnel itself. 
ETX-1paccepts the first policy that a peer has proposed that it supports. If the mandatory elements are 
configured, ETX-1p starts negotiating the IPsec tunnel with the configured peer. 
If the process fails, ETX-1p retries, using a backoff algorithm, after 1 second, 2, 4, 8, 16, 32 and 64 
seconds; then restarts the sequence. 
If the peer does not answer, or the peer responds but the parties cannot agree, ETX-1p raises an alarm. 
ETX-1p drops packets, incoming or outgoing, which are supposed to pass through an IPsec tunnel, if that 
tunnel is not established. 
Diffie Hellman 
DH (Diffie-Hellman) describes a means for two parties to agree upon a shared secret. This secret may 
then be converted into cryptographic keying material for other (symmetric) algorithms. The Diffie-
Hellman key agreement requires that both the sender and recipient of a message have key pairs. The 
private key of each member is never sent over the insecure channel. The public key is generated from 
the private key by each member and is the one sent over the insecure channel. By combining one's 
private key and the other party's public key, both parties can compute the same shared secret number. 
This number can then be converted into cryptographic keying material. That keying material is typically 
used as a key-encryption key (KEK) to encrypt the IPsec tunnel traffic. This key is kept secret and never 
exchanged over the insecure channel. 
D-H groups are identified by a group number. The higher the group number, the higher the security 
level. 
Pre-shared Keys (PSKs) 
ETX-1p supports the configuration of up to twenty pre-shared keys (PSKs) for IKE phase-1 
authentication. 
7. Traffic Processing 
You configure PSKs at the Crypto level for pairs of addresses and prefix lengths. ETX-1p uses the one 
with the longest prefix match. 
You can configure PSKs for hosts or subnets. If a key is shared across a subnet, all the IPsec tunnels 
opposite peers on that subnet use the same key. This is less recommended as a breached key affects the 
security of multiple tunnels. When ETX-1p looks for a pre-shared key to use, if there is a key for the peer 
address, it uses it. If there is no key for the peer, it uses the key configured for the subnet with the 
longest prefix that contains the peer address. 
The encryption, hash, and authentication algorithm for use with a pre-shared key are part of the state 
information distributed with the key itself. Each peer must have a unique ID and common shared key 
known to the remote peer. 
Exchange Modes 
There are two Exchange modes: Main and Aggressive. 
Main mode is the more secure option for Phase1 as it involves identity protection. 
A session flow is as follows: 
• 
A session begins with the initiator sending a proposal to the responder describing what 
encryption and authentication protocols are supported, the lifetime of the keys, and if phase 2 
perfect forward secrecy should be implemented. The proposal may contain several offerings.  
The responder chooses from the offerings and replies to the initiator. 
• 
The next exchange passes Diffie-Hellman public keys and other data. All further negotiation is 
encrypted within the IKE SA.  
• 
The third exchange authenticates the ISAKMP session. Once the IKE SA is established, IPsec 
negotiation (Quick Mode) begins. 
In Aggressive mode, the negotiation is quicker since the session is completed in only three messages. 
The disadvantage is that the identity of the peers is not protected.  
The first two messages negotiate policy, exchange Diffie-Hellman public values and ancillary data 
necessary for the exchange, and identities. In addition, the second message authenticates the 
responder. The third message authenticates the initiator and provides a proof of participation in the 
exchange. 
• 
The initiator sends a request with all required SA information. 
• 
The responder replies with authentication and its ID. 
• 
The initiator authenticates the session in the follow-up message. 
7. Traffic Processing 
Phase 2 
In this phase, the negotiation of SA to secure the IPsec tunnel, is completed. 
Perfect Forward Secrecy (PFS) 
PFS forces a new D-H key exchange for each phase-2 tunnel, deriving phase-2 keys independent from 
and unrelated to the preceding keys.  
PFS is a part of the key agreement session and serves to ensure that a session key derived from a set of 
long-term public and private keys are not compromised if one of the (long-term) private keys is 
compromised in the future. The VPN (IPsec) sessions can negotiate new keys for every communication, 
and if a key is compromised only the specific session it protected is revealed. 
PFS uses the D-H groups as well, but independently of phase 1. 
NAT Traversal 
ETX-1p supports NAT traversal. NAT traversal changes the packets header so that they can pass NAT 
without the protected data being changed by the NAT. You cannot configure NAT traversal, as it is 
activated automatically when ETX-1p learns that an IPsec connection is passing through NAT. 
Route-Based IPsec Tunnels 
ETX-1p supports IPsec tunnels, with IPv4 as delivery and payload protocols, each one independently of 
the other. 
Configuring IPsec 
This section describes how to configure ETX-1p with IPsec at the Cryptography level.  
 To configure IPsec: 
1. Navigate to configure crypto.  
1. Enter all necessary commands according to the tasks listed below. 
 
7. Traffic Processing 
Task 
Command 
Comments 
Creating crypto map 
crypto-map <name> 
no crypto-map <name> 
name – crypto map name 
Possible values: 1-80 character string 
See Configuring Crypto Map for available 
crypto map configuration tasks. 
Configuring IPsec phase 2 
policy 
ipsec-transform-set <name> 
no ipsec-transform-set <name> 
name –IPsec transform set name  
Possible values: 1-80 character string 
See Configuring IPsec Transform Set for 
available transform set configuration tasks. 
Configuring IKE pre-shared 
key (PSK) 
isakmp-key <pre-shared-key> 
{address <peer-ip-address> 
[/<peer-ip-prefix-length>] | 
hostname <hostname>}  
no isakmp-key address <peer-
ip-address> [/<peer-ip-prefix-
length>] 
The pre-shared authentication method (only 
available method) requires configuration of 
PSKs for pairs of address and prefix length. 
pre-shared-key – IKE pre-shared key 
Possible values: 1-255 character string 
peer-ip-address – IKE peer IP address 
Possible values: IPv4 address 
peer-ip-prefix-length – IKE peer IP prefix 
length 
Possible values: 0-32 
hostname – hostname of IKE peer 
Possible value: 1-255 character string 
Notes: 
• PSKs can be configured for hosts or 
subnets. peer-ip-address must be a host 
address if IKE key peer address type is 32, 
and a subnet (in accordance with IKE peer 
address prefix length.  
• The prefix length must agree with the 
address (e.g. a host address can only be 
configured with a prefix length of 32). 
• If you configure a PSK for an existing pair 
of address and prefix length, the new 
command replaces the previous. 
Configuring IPsec Phase 1 
policy 
isakmp-policy <sequence-
number> 
no isakmp-policy <sequence-
number> 
sequence-number – IKE policy priority 
Possible values: number 
Note: You can configure up to twenty policies. 
For full configuration of IKE policies, see 
Configuring IKE Policy. 
7. Traffic Processing 
Configuring Crypto Map 
This section describes how to configure a Crypto Map. Once the Crypto Map is configured, you associate 
it to a router (see Configuring Router Interfaces) or tunnel interface (See Configuring Tunnel 
Interfaces). 
 To configure a crypto map:  
1. Navigate to configure crypto crypto-map (<name>). 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Configuring local IKE 
identity 
ike-identity-local {default-
address | address <ip-
address> | default-
hostname |   
IKE peer can be identified either by IP 
address or by hostname, if IP address is 
unknown. 
For local identity, the default hostname 
(which is the device hostname defined as 
the MAC address) can be used. 
Configuring remote IKE 
identity 
ike-identity-remote 
{default-address | address 
<ip-address> |   
IKE Peer can be identified either by IP 
address or by hostname, if IP address is 
unknown. 
For remote identity, you have to provide the 
hostname. 
Configuring IKE SA 
lifetime 
ike-sa-lifetime <seconds> 
Possible values: 60-86400 
Configuring IKE SA 
negotiation mode 
ike-sa-negotiation {main | 
aggressive} 
Relevant only for ike-version 1 
Configuring IKE version 
ike-version {1 | 2} 
 
Configuring destination 
address to protect 
match-destination 
address <ip-
address>/<prefix-length> 
no match-destination 
address <ip-
address>/<prefix-length> 
 
7. Traffic Processing 
Task 
Command 
Comments 
Configuring source 
address to protect 
match-source {address 
<ip-address>/<prefix-
length> | interface 
<interface-name>} 
no match-source {address 
<ip-address>/<prefix-
length> | interface 
<interface-name>} 
 
Configuring IPsec peer IP 
address  
peer-address <ip-address> 
no peer-address 
ip-address – IP address of the peer with 
which the IPsec tunnel is to be established 
Possible values: IPv4 address 
Notes: 
• You can configure only one instance of 
this command in a crypto map. If you 
repeat the command, the last instance 
applies. 
• no peer-address (the default) sets the 
peer address to 0. 
Configuring PFS Diffie 
Hellman group 
 
pfs-group {1 | 2 | 5 | 14 | 
19 | 20} 
no pfs-group 
 
One instance of the command can be 
configured in a crypto map. If the command 
is repeated the last instance applies. 
Configuring 1, 2, 5 or 14 does not provide 
adequate protection from modern threats. 
Recommended values are 19 or 20 (default) 
Setting the device not to 
initiate connection 
(typically used for a 
central device with many 
simultaneous tunnels 
open) 
responder-only 
[no] responder-only 
Default: no responder-only 
 
7. Traffic Processing 
Task 
Command 
Comments 
Configuring SA lifetime 
sa-lifetime [seconds 
<seconds>] [kilobytes 
<kilobytes>]  
no sa-lifetime 
seconds – SA lifetime in seconds  
Possible values: 60-86400 
kilobytes – SA lifetime in kilobytes  
Possible values: 76800 – 110592000 
Notes: 
• You can configure only one instance of 
this command in a crypto map. If you 
repeat the command, the last instance 
applies. 
• The command must have at least one 
argument. 
• The SA is invalidated if the seconds or 
kilobytes reach the maximum time 
before the SA is renewed. 
• no sa-lifetime sets seconds to 3600 and 
kilobytes to 4608000 (the defaults). 
Configuring Crypto Map 
priority 
sequence-number 
<number>  
no sequence-number 
number – crypto map priority 
Possible values: 1-1000 
Notes: 
• You can configure only one instance of 
this command in a crypto map. If you 
repeat the command, the last instance 
applies. 
• no sequence-number sets number to 10 
(the default). 
Associating IPsec phase 2 
transform set with crypto 
map 
transform-set <name-1> 
[name-2 [name-3 [name-
4]]] 
no transform-set 
name-x – IPsec phase 2 transform set 
created at Crypto level (see Configuring 
IPsec) 
Possible values: 1-80 character string 
Notes: 
• You can configure only one instance of 
this command in a crypto map. If you 
repeat the command, the last instance 
applies. 
• no transform-set (the default) sets 
name-x  to empty string.  
 
 
 
7. Traffic Processing 
Configuring IPsec Transform Set 
This section describes how to create an IPsec transform set at the Crypto level. After the Transform Set 
has been created and configured, you can bind it to a Crypto Map (see Configuring Crypto Map above).  
 To configure IPsec transform set: 
1. Navigate to configure crypto ipsec-transform-set <name>.  
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Configuring IPsec phase 
2 algorithms  
algorithms <first transform set 
algorithm> [second transform 
set algorithm] 
First transform set algorithm –used for 
encryption 
Possible values: esp-aes-cbc-128, esp-aes-
cbc-256, esp-aes-gcm-128, esp-aes-gcm-
256, esp-null, esp-aes-gmac-128, esp-aes-
gmac-256 
Second transform set algorithm –used for 
authentication 
Possible values: esp-sha1, esp-sha2-256, 
esp-sha2-512 
Notes:  
• You can configure one instance of the 
command in a transform set. If you 
repeat the command, the last instance 
applies.  
• If you configure the first transform set 
algorithm (encryption) with an 
algorithm used for both encryption 
and authentication (esp-aes-gcm-128, 
esp-aes-gcm-256, esp-aes-gmac-128, 
or esp-aes-gmac-256), you cannot 
configure a second algorithm (for 
authentication). In this case, the 
second algorithm default (esp-sha1) 
does not appear in the info command 
output. 
7. Traffic Processing 
Task 
Command 
Comments 
• If you select for the first transform set 
algorithm (encryption) one of the 
encryption only algorithms (esp-aes-
cbc-128, esp-aes-cbc-256, or esp-null), 
you must select one of the following 
second authentication algorithms: esp-
sha1, esp-sha2-256, or esp-sha2-512. 
Otherwise, the second algorithm 
default (esp-sha1) is selected. Also, the 
info command output specifies 
whether esp-sha1 was selected as 
default or explicitly specified. 
Selecting IPsec operating 
mode 
mode {transport | tunnel} 
 
Configuring IKE Policy  
 To configure an IKE policy: 
1. Navigate to configure crypto isakmp-policy <sequence-number>, where sequence number 
signifies the IKE policy priority. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Configuring 
authentication method 
(pre-share) 
authentication {pre-share } 
 
Configuring encryption 
algorithm 
encryption {aes-cbc-128|aes-cbc-
256|aes-128-gcm-64|aes-128-
gcm-96| aes-128-gcm-128|aes-
256-gcm-64|aes-256-gcm-96|aes-
256-gcm-128}  
Default: aes-cbc-256  
Note: You can configure only one 
instance of the command in a policy. 
If you repeat the command, the last 
instance applies. 
7. Traffic Processing 
Task 
Command 
Comments 
Configuring key exchange 
algorithm (Diffie-Hellman 
group) 
group {1 | 2 | 5 | 14 | 19 | 20} 
 
group – Diffie-Hellman group 
Possible values: 
1 – 768-bit modulus 
2 – 1024-bit modulus 
5 – 1536-bit modulus 
14 – 2048-bit modulus 
19 – 256-bit elliptic curve 
20 – 384-bit elliptic curve (default)  
Notes: 
• You can configure only one 
instance of the command in a 
policy. If you repeat the 
command, the last instance 
applies. 
• Groups 1, 2, and 5 are not 
considered secured and 14 is 
acceptable, but not recommended  
• If you configure 1, 2, 5, or 14, ETX-
1p accepts the command, but 
generates the following message: 
WARNING: This algorithm does 
not provide an adequate security 
level against modern threats and 
should not be used to protect 
sensitive information. 
Configuring hashing 
algorithm 
hash {sha1 | sha2-256 | sha2-512} 
hash – hashing algorithm 
Possible values: 
sha1 – 96-bit (default) 
sha2-256 – 128-bit 
sha2-512 – 256-bit  
Note: You can configure only one 
instance of the command in a policy. 
If you repeat the command, the last 
instance applies. 
7. Traffic Processing 
Configuration Errors  
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Too many crypto maps 
You tried configuring more 
than 30 crypto maps. 
Remove crypto maps that you no longer 
need. 
IP address already configured 
You tried configuring a crypto 
map with an IP address (source 
or destination) that was 
already used in another crypto 
map command. 
Configure the crypto map command 
with a unique IP address. 
Too many IP addresses 
You tried configuring more 
than 20 addresses (source or 
destination) on the crypto 
map. 
Remove IP addresses that you do not 
need.  
The interface must be a tunnel 
interface 
You tried configuring a non-
tunnel interface. 
Configure a tunnel interface. 
A source interface is already 
configured 
You tried configuring an 
address or another interface, 
while one interface has been 
already configured. 
 
A source IP address is already 
configured 
You tried configuring an 
interface, while an address has 
already been configured. 
 
Too many transform sets 
You tried configuring more 
than one transform set on the 
crypto map. 
Remove transform set that you do not 
need. 
Too many keys 
You tried configuring more 
than 30 IKE pre-shared keys. 
Remove keys that you do not need. 
Too many policies 
You tried configuring more 
than 30 IKE policies. 
Remove policies that you do not need. 
Configure either source address or 
interface, not both 
You tried to configure the 
router interface anchoring the 
tunnel with both an address 
and interface. 
Remove one of the configurations: 
either the address or interface. 

## 7.5 LoRaWAN  *(p.467)*

7. Traffic Processing 
Message 
Cause 
Corrective Action 
Source and destination must be 
both IPv4 or both IPv6 
You tried to configure tunnel 
destination with an IPv4 
address while the tunnel 
source is an IPv6 address. 
You tried to configure tunnel 
source with an IPv4 address 
while the tunnel destination is 
an IPv6 address. 
Define destination and source with 
same type of IP address – both IPv4 or 
both IPv6. 
Too many mappings 
You tried configuring more 
than one mapping per tunnel.  
 
No such mapping 
You tried to delete a 
nonexistent mapping. 
 
7.5 LoRaWAN  
Low-Power Wide-Area Network (LPWAN) is implemented in  by means of LoRa (Long Range) technology 
to allow long-range communications at a low bit rate among IoT devices, such as sensors operated on a 
battery. The device is equipped with LoRaWAN (Low Range Wide Area Network) modem that allows to 
aggregate multiple low-power low-bandwidth sensors/meters deployed over a wide area. 
It provides long-range communication up to 5–10 km in rural/open areas and 2–4 km in urban zones, 
with the following capacity: 
• 
Up to 500 nodes per km2 (Typical 1000 nodes) 
• 
Tx power up to 25 dBm, Rx sensitivity down to -139 dBm @ SF12, BW 125 kHz 
LPWAN is used in industrial IoT because of its low power, long range, and low-cost communication 
characteristics. 
The LoRa gateway forwards data from endpoint devices to a LoRa server, and back. If a device has 
multiple modems, a gateway can be configured for each. 
LoRa frequencies differ between countries. In most cases users buy a modem fitting their country, and 
the modem dictates the frequency plan. AS923 is an exception, supporting four plans. Users buying this 
modem may need to configure a different plan if they reside in a country not covered by the default 
plan. 
7. Traffic Processing 
Applicability and Scaling 
LoRaWAN is available in  devices with the /LRx ordering option equipped with the corresponding 
LoRaWAN modem and antenna (ordered separately).  
Functional Description 
Multiple LoRa sensors distributed in remote locations send data via  gateway to a central server that can 
gather the data.  
Frequencies  
The frequencies LoRa uses vary between countries. The customers can order an LRA (9XX frequencies), 
or LRB (8XX frequencies) modem. The device reads the modem type from its EEPROM, and the 
frequency plan can be set in the configure>port>lora>gateway level: 
• 
The configurable plans for 9XX modems are AS923_1, AS923_2, AS923_3, AS923_4, AU915,  
KR920 and US915. 
• 
The configurable plans for 8XX modems are EU868, IN865 and RU864. 
You can also order a TAA-compliant 9XX modem with US915, AS923, AU915 and KR920 configurable 
plans. 
Sometimes it is required to restrict the frequency plan to a sub-band. To use the frequency plan on a 
sub-band, use the sub-band command on the configure>port>lora level. The command is available for 
the AU915 and US915 frequency plans. Only sub-bands 1-8 (one of them) can be configured. By default, 
no sub-band is configured and the frequency plan is used as is. If the command is repeated, the last 
instance applies.  
Operation Mode 
The available packet forwarding methods for LoRA are UDP forwarding or ChirpStack (the default).  
The gateway requires a server to be operational and you are responsible to configure one. For UDP 
forwarding it is done with the server command and for ChirpStack with the mqtt-server command (if 
the server is configured to work with a certificate, MQTTS is utilized). 
For the description of MQTT server, refer to the MQTT Server section in Chapter 6. 
7. Traffic Processing 
Factory Defaults 
Parameter 
Default Value 
server port – uplink 
1680 
server port – downlink 
1680 
gateway-id  
auto 
mqtt-server 
 
no mqtt-server (MQTT 
server is not configured) 
operation-mode 
chirpstack 
Configuring LoRaWAN 
 To configure LoRaWAN: 
1. At the config>port># prompt, type lora [number]. 
2. Enter the necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Configuring the AS923 modem 
frequency  
frequency plan <plan-name> 
Possible values depend on the LoRa 
modem ordered with the device:  
• LRA and L9 (9XX) modems: as923_1, 
as923_2, as923_3, as923_4, au915, 
kr920, us915  
• LRB (8XX) modem: eu868, in865, 
ru864 
Entering LoRa gateway level (see 
below) 
gateway 
[no] gateway 
Default: LoRa gateway is not 
configured 
Restricting the frequency plan to a 
sub-band  
sub-band  <sub-band-number 
1..8> 
The command is available for the 
AU915 and US915 frequency plans.  
 
The following commands are available in the lora-gateway level, at the config> port> lora [number] > 
lora-gateway # prompt. 
7. Traffic Processing 
Task 
Command 
Comments 
Configuring the LoRa gateway ID 
(EUI) 
 
gateway-id {auto | string <hex-
string>} 
 
The ID is a 64bit hex string, 
which should be globally 
unique. The device identifies 
itself with it while 
communicating with the server.  
The default gateway ID is based 
on the LoRa modem port MAC 
address, but since a MAC 
address is 48bits, fffe is added 
in the middle. 
Configuring MQTT server (for 
working with Chirpstack) 
 
 
mqtt-server name <server-
name> 
[no] mqtt-server 
Appears only when operation-
mode is chirpstack 
<server-name>: 1-32 characters 
Configuring LoRa operation 
mode (choosing the packet 
forwarding method) 
operation-mode {udp-forward 
| chirpstack}  
 
 
udp-forward - UDP forwarding 
is done with the server 
command and for ChirpStack 
chirpstack –forwarding is done 
with the mqtt-server command. 
Configuring LoRa server 
properties (for working with 
UDP forwarding)  
 
 
server {ip-address <ip-address> | 
url <url-string>} [downstream-
port <down-port>] [upstream-
port <up-port>] 
no server {ip-address <ip-
address> | url <url-string>} 
  
 
<ip-address> –  valid IPv4 or 
IPv6 unicast address  
<url-string> – URL string 
<down-port> – LoRa server 
downstream port 
<up-port> – LoRa server 
upstream port 
Possible Values for both ports: 
1-65535 
Unspecified UDP ports are set 
to the default value (1680). To 
be on the safe side, always 
specify both ports 
Displaying the gateway status 
show status 
See below 
Enabling/disabling LoRa gateway 
no [shutdown] 
Default: shutdown 
7. Traffic Processing 
Viewing LoRaWAN Status  
You can display the current LoRa status. 
 To display LoRa status: 
• 
At the config>port>lora(<number>)>gateway# prompt, enter: 
show status 
The LoRa status is displayed. 
 
Operational Mode = Chirpstack 
Administrative Status  : Up 
LoRa Operational Status: Up 
Gateway ID (EUI)       : de:ad:00:ff:fe:00:be:ef  
Frequency Plan         : AS923_1 
Operation Mode 
   : Chirpstack 
MQTT Server  
   : mqtt-lns 
MQTT Status  
   : Connected 
 
 
Operational Mode = UDP Forward 
Administrative Status  : Up 
LoRa Operational Status: Up 
Gateway ID (EUI)       : de:ad:00:ff:fe:00:be:ef  
Frequency Plan         : AS923_1 
Operation Mode 
   : Udp Forward 
Udp Forward Status    : Up 
 
Server  
Port 
 
-------------------- 
127.0.0.1 
1680 
 
 
Status Parameters 
Parameter 
Description 
Administrative Status 
Administrative status 
Possible Values: Enabled, Disabled 
Operational Status 
LoRa Operational Status  
Possible Values: Up, Down 
 
Gateway ID (EUI)   
 
LoRa gateway ID (EUI) 
Possible Values: 64 bit octet string, formatted 00:00:00:00:00:00:00:00 
(followed by “auto” if auto ID was configured) 
7. Traffic Processing 
Parameter 
Description 
Frequency Plan    
 
 
Modem frequency plan 
Possible Values: AS923_1, AS923_2, AS923_3, AS923_4, EU433, EU868, 
AU915, US915, KR920 
Not Configured, AS923_1, AS923_2, AS923_3, AS923_4, AU915, KR920, 
US915, EU868, IN865, RU864 
Operation Mode 
 
LoRa operation mode 
Possible Values: udp-forward, chirpstack 
Server Name 
(chirpstack only) 
MQTT server name (string) 
 
MQTT Status 
(chirpstack only) 
 
 
 
MQTT module status: 
• Not configured – configuration is missing  
• Disconnected – connection fails after ‘Connected’ state 
• Connected – connection process succeeded 
• Connecting – trying to connect before first “Connected” state  
MQTT Configuration 
Problem 
(chirpstack only) 
 
 
MQTT configuration problem (MQTT cannot start due to missing 
configuration) 
• Undefined MQTT server in LoRa gateway 
• Undefined MQTT address 
• Undefined certificate or user 
• There is no certificate 
UDP Forward Status 
(udp-forward only) 
Possible Values: Up, Down 
Server Address 
(udp-forward only) 
UDP Server address 
Possible Values: IP address or URL 
Port 
(udp-forward only) 
UDP port the LoRa server uses  
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 

## 7.6 Network Address Translator (NAT)  *(p.473)*

7. Traffic Processing 
Message 
Cause 
Corrective Action 
Maximum number of servers is 
configured  
You tried to configure more than 
four servers 
 
Invalid unicast IP address  
 
You tried to specify an  
ip-address that is not a valid 
unicast IP address 
 
Frequency plan must be configured 
when LoRa is enabled 
You tried to configure no frequency 
while LoRa gateway was enabled  
Disable LoRa gateway 
Example 
 To configure LoRa working with Chirpstack: 
1. Define the Lora connectivity. The MQTT value should be the same as in the MQTT server you 
created under configure>system>mqtt (in this example, the name is “1”).  
configure port Lora 1 
            frequency plan us915 
            gateway 
                mqtt-server "1" 
                no shutdown 
            exit 
            sub-band 2 
2.  Save the GW ID for configuring it after that on the LNS Server: 
configure port Lora 1 
gateway 
show status 
Gateway ID (EUI)      : 0016c001f1108617 (auto)  
3.  Save the GW ID for configuring it after that on the LNS Server. 
4. Create the GW on Chirpstack server and verify that it is online. 
7.6 Network Address Translator (NAT)  
Network Address Translation (NAT) is a method that maps IP addresses (IPv4 only) from one IP domain 
to another in an attempt to provide transparent routing to hosts. 
7. Traffic Processing 
Applicability and Scaling 
• 
20,000 entries in the mapping table 
• 
Up to 32 NAT rules of static NAT, NAPT and Outside to Inside (Static IP:Port) 
Functional Description 
Traditionally, NAT devices connect networks and hosts having private unregistered addresses to a global 
public network with globally unique registered addresses. 
IP Address translation is required for the following reasons: 
• 
The network's internal IP addresses cannot be used outside the network, either because they 
are invalid for use outside, or because the internal addressing must be kept private from the 
external network. 
• 
Lack of public IP addresses and the need to represent as many hosts as possible (using private IP 
addresses) via a single public address. NAT uses the IP address resource in an efficient way. 
The terminology used in this section is described in the following table: 
Inside network 
Private network side of the NAT function 
Outside network 
Public network side of the NAT function 
Inside local address 
IP address assigned to a host on the inside network. This is the address 
configured as a parameter of the computer OS or received via dynamic 
address allocation protocols, such as DHCP. The address is not likely a 
legitimate IP address assigned by the Network Information Center (NIC) or 
service provider. 
Inside global address 
Legitimate IP address assigned by the NIC or service provider; represents one 
or more inside local IP addresses to the outside world. 
Outside local address 
IP address of an outside host as it appears to the inside network. Not 
necessarily a legitimate address, it is allocated from an address space routable 
on the inside. 
Outside global address 
IP address assigned to a host on the outside network by the host owner. The 
address is allocated from a globally routable address or network space. 
Inside network 
Private network side of the NAT function 
7. Traffic Processing 
NAT Functionality: Address Translation 
NAT translates in the following ways: 
• 
NAT translations:  
 
Inside to Outside: Inside (private) IP SA (Inside local)  Outside (public) IP SA (Inside global) 
 
Outside to Inside: Outside (public) IP DA (Inside global)  Inside (private) IP DA (Inside local) 
• 
NAPT translations – TCP and UDP sessions are translated with port number, in addition to the IP 
address: 
 
Inside to Outside: Inside (private) IP SA:Port (inside local)  Outside (public) IP SA:Port 
(Inside global) 
 
Outside to Inside: Outside (public) IP DA:Port (Inside global)  Inside (private) IP DA:Port 
(Inside local) 
Traffic that does not match NAT entries, is forwarded per router regular path. 
Outside Network
NAT
Inside 
Host
Outside 
Host
Inside Network
DA
Outside Local
DA
Inside Local
DA
Outside Global
DA
Inside Global
SA
Inside Local
SA
Outside Local
SA
Inside Global
SA
Outside Global
Translate
 
Supported NAT Types 
ETX-1p supports the following NAT types: 
• 
Static (One to One) NAT with the following properties: 
 
One to One – Translates a single private IPSA to a single public IPSA; does not translate port 
 
Bidirectional – Sessions can be initiated both from the Inside and Outside 
• 
NAPT/PAT: In this mode, many hosts on the private (Inside) network are represented by a single 
public (Outside) IP, using the TCP or UDP port number to differentiate between the different 
sessions.  
7. Traffic Processing 
In this mode, many different IPs (IP:Port) are translated into a single IP:Port, while the translated 
port is used to differentiate between the sessions (as translated IP uses the same IP). 
 
Many to One – Translate IP and Port for TCP/UDP sessions.  
 
Unidirectional – Sessions can be initiated only from the Inside  
 
TCP/UDP – Port mapping functionality valid for TCP/UDP sessions only. 
• 
Outside destination to Inside hole punching (Static Port configuration):  
 
One to One – Translates IP DA:Port from the Outside to the Inside 
 
Unidirectional – Sessions can be initiated only from the Outside. 
NAT supports symmetric operation, meaning that NAT sessions are identified by both IPSA (:Port) and IP 
DA (:Port).  
NAT Instances 
ETX-1p supports a single instance of NAT, which may be configured over each one of the ETX-1p VRFs. 
Configuring Network Address Translator (NAT)  
You can configure a single instance of NAT over one of the device VRFs. 
 To configure NAT: 
1. At the config>router(<number>)# prompt, enter: 
nat 
The config>router(<number>)>nat# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Configuring or deleting a 
NAT exclude expression 
nat-exclude-source-ip <source-ip> 
no nat-exclude-source-ip <source-
ip> 
It is possible to add multiple 
NAT exclude expressions (up to 
10) 
7. Traffic Processing 
Task 
Command 
Comments 
Configuring, modifying, or 
deleting a NAT rule from the 
inside to outside 
nat-inside-source-static <inside-ip> { 
ip <outside-ip> | interface <rif-id> }  
no nat-inside-source-static <inside-
ip> 
no nat-inside-source-static <inside-
ip>  
     
  
 
inside-ip – IPv4 address of 
Inside IP station 
ip – Ipv4 address for translation 
interface – number of outside 
facing router interace whose IP 
address is used for IP 
translation.  
A NAT rule that is missing info 
(yet to be configured) is saved 
and applied once you configure 
the missing info. There is no 
sanity reject. 
Configuring, modifying, or 
deleting a NAPT rule from 
the inside to outside 
 
nat-inside-source-static-port {tcp | 
udp} <inside-ip> <port> { ip 
<outside-ip> <port>|interface <RI-
id> <port>}  
no nat-inside-source-static-port tcp 
<inside-ip> <inside-port> ip 
<outside-ip> 
no nat-inside-source-static-port udp 
<inside-ip> <inside-port> ip 
<outside-ip> 
no nat-inside-source-static-port tcp 
<inside-ip> <inside-port> interface 
<rif-id> 
no nat-inside-source-static-port udp 
<inside-ip> <inside-port> interface 
<rif-id> 
source – source address 
translation 
<inside ip/prefix> - IP subnet of 
inside Inside network   
ip – IPv4 address for translation 
interface – number of outside 
facing router interface whose IP 
address is used for IP translation 
tcp - range of IP ports to be 
used for TCP port translations 
udp - range of IP ports to be 
used for UDP port translations 
Possible values: 
start-port: 1024 (default)– 
65535 
size: 1 – 64511 (default) 
Configuring, modifying, or 
deleting a NAPT rule from 
the inside to outside 
nat-inside-overload source  <inside 
ip/prefix> { ip <outside-ip> | 
interface <RI number> } [ tcp < start-
port> <size> ] [udp < start-port> 
<size> ]  
no nat-inside-overload source 
<inside ip/prefix> <outside-ip> 
no nat-inside-overload source 
<inside ip/prefix> interface <RI 
number> 
 
 
7. Traffic Processing 
Task 
Command 
Comments 
Configuring or modifying 
NAT translation table entry 
timeout 
nat-timeout [ tcp < tcp-timeout>] [ 
udp <udp-timeout> ] [ other <other-
timeout> ] 
tcp -  expiration timeout of TCP 
entries in NAT translation table 
udp - expiration timeout of UDP 
entries in NAT translation table 
other - expiration timeout of 
other protocol entries in NAT 
translation table 
Possible values: 60-432000 
Default: 60 
Displaying NAT translation 
table  
show nat-translations  
See Viewing NAT Translation 
Table 
Clearing NAT translation 
table 
clear nat-translations 
 
Displaying NAT statistics 
counters 
show nat-statistics 
 
Clearing NAT statistics 
counters 
clear nat-statistics 
 
Viewing NAT Translation Table 
You can display the NAT translation table. 
 To display the NAT translation table: 
• 
At the config>router(<number>)>nat # prompt, enter: 
show nat-translations 
The NAT translation table is displayed. 
config router 1 nat 
config>router(1)>nat# show nat-translations 
Number of entries : 1 
 
Entry Protocol  Inside Local          Inside Global       
----------------------------------------------------------------------------- 
1     ICMP      30.30.30.30:1         20.20.20.30:1       
The above fields are: 
7. Traffic Processing 
Number of Entries 
Total number of entries in the translation table 
Possible values: 0-1000 
Entry 
Entry number  
Possible values: 1-1000 
Protocol 
The associated router interface ID 
Possible values: TCP, UDP, ICMP, Other 
Inside Local 
Inside local address or address/port 
Possible Values: IP address: port, where port=1-65535 
Note: For Other protocol, only IP address is displayed. 
Inside Global 
Translated inside global address or address/port 
Possible Values: IP address: port, where port=1-65535 
Note: For Other protocol, only IP address is displayed. 
Viewing NAT Statistics 
You can display NAT statistics counters. 
 To display NAT statistics: 
• 
At the config>router(<number>)>nat # prompt, enter: 
show nat-statistics 
The NAT statistics are displayed. 
config>router(1)>nat# show nat-statistics 
Translated packets Inside to Outside : 62 
Translated packets Outside to Inside : 69 
The above fields are: 
Translated packets Inside to 
Outside 
Number of packets translated by NAT at the Inside to Outside direction 
Translated packets Outside to 
Inside 
Number of packets translated by NAT at the Outside to Inside direction  
7. Traffic Processing 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Cannot delete; interface associated 
with the router 
You tried to delete a router entity 
that has router interfaces 
associated with it. 
Disassociate router interfaces from 
router. 
Cannot set address; DHCP enabled 
You tried adding an IPv4 address 
when DHCP is enabled. 
Disable DHCP. 
Cannot set address; too many 
addresses already configured 
You tried adding an IP address, but 
the amount of IP addresses already 
reached its limit. 
Delete one of the associated 
addresses before associating a new 
IP address. 
Cannot set address; invalid 
You tried adding a multicast IP 
address or an interface IPv4 
address with prefix length 32 (, 
which is only allowed for loopback 
interface). 
When configuring static-route, you 
tried to do one of the following: 
• Add a multicast IP network 
address. 
• Add an IP network address 
when it was not allowed. 
 
Use /31 prefix-length on non point-
to-point interface cautiously  
You tried adding anIPv4 interface 
address with prefix length 31. 
 
Cannot modify; activated router 
interface 
You tried modifying or removing a 
bound port while the router 
interface was activated (no 
shutdown). 
You tried adding, modifying, or 
removing a VLAN while the router 
interface was activated (no 
shutdown). 
Shut down the router interface and 
try again. 
Cannot enable; IPv4 address exists 
You tried enabling DHCP even 
though manual IPv4 address exists. 
 
Cannot enable; DHCPv6 is enabled 
You tried enabling DHCP even 
though DHCPv6 is enabled. 
Disable DHCPv6. 
7. Traffic Processing 
Message 
Cause 
Corrective Action 
Cannot set; DHCPv6 client is 
already defined 
You tried enabling DHCPv6 client 
when there is already one defined 
in the device. 
Remove existing DHCPv6 client. 
Cannot enable; DHCP (v4) is 
enabled 
You tried enabling DHCPv6 while 
DHCPv4 is enabled. 
Disable DHCPv4. 
Cannot set; Router Interface is 
loopback interface 
You tried enabling DHCPv6 client 
while router interface is defined as 
loopback interface. 
Associate DHCPv6 client with a 
router interface that is not defined 
as a loopback interface. 
Cannot activate; must be bound to 
port 
You tried activating a router 
interface, which is neither a 
loopback interface nor bound to a 
port. 
Bind the router interface to a 
loopback interface or a port. 
Cannot activate; bound port in use 
by another router interface 
You tried activating the router 
interface, while the bound port is 
already in use by another router 
interface. 
 
Cannot activate; bound port+vlan 
in use by another router interface 
You tried activating the router 
interface that is bound to port + 
vlan, while bound pair port+vlan is 
already in use by another router 
interface. 
 
Cannot activate; ip address is set 
You tried activating the router 
interface bound to PPP port, when 
IP address was set. 
 
Cannot activate; dhcp is enable  
You tried activating the router 
interface bound to PPP port, when 
DHCP is enabled. 
 
Address is not IPv4 address. 
You configured the IP address of 
Inside IP station with a non-IPv4 
address. 
Configure the IP address of Inside 
IP station with an IPv4 address. 
Timeout is out of range 
Expiration timeout of 
TCP/UDP/other protocol entries in 
NAT translation table is out of the 
allowed range (60-43200). 
 

## 7.7 Policy-Based Routing (PBR)  *(p.482)*

7. Traffic Processing 
7.7 Policy-Based Routing (PBR)  
Policy-based routing allows you to use a policy to bypass the normal routing rules. 
Applicability and Scaling 
No forwarding is allowed between VRFs. 
Only Ethernet, virtual and VLAN ports can be ingress ports. 
Benefits 
PBR rules can bypass any Layer 3 routing/forwarding thus enabling routing resiliency. 
Functional Description 
You can set the following PBR entities: 
• 
ACL – to classify specific traffic  
• 
Policy – to define where to define the traffic captured by ACL 
• 
Attach the policy to ingress interface 
When PBR is defined on specific ingress interface, the incoming traffic on this ingress interface captured 
by the ACL is directed according to the policy definition. PBR rule direction is set by the next hop IP 
address or by an egress interface. 
PBR provides classification based on ACL capabilities and supports:  
• 
IPv4, IPv6 
• 
Match options: 
 
Source IP/prefix-len 
 
Destination IP/prefix-len 
 
Source port range 
 
Destination port range 
 
Protocol (protocol number, i.e., icmp-1, tcp-6, udp-17) 
7. Traffic Processing 
ETX-1p PBR policy supports the following destination definitions: 
• 
Next hop address 
• 
Egress interface: 
 
Broadcast interface with static/dynamic IP address 
 
Point-to-point interface 
ETX-1p PBR is supported for the following ingress interfaces: 
• 
Ethernet ports 
• 
VLAN ports 
• 
Virtual ports 
Factory Defaults 
By default, no PBR exists. 
Configuring PBR 
 To configure PBR: 
1. Create an ACL profile (see Configuring ACL). 
2. Define policy on an ingress interface: 
a. Match ACL 
b. Set direction (next-hop or interface) 
c. Set priority 
 To define policy on the ingress port:  
1. For Ethernet port: Navigate to configure port ethernet <port-name> to select the Ethernet port 
on which PBR is configured. 
For Ethernet VLAN: Navigate to configure port ethernet <port-name>vlan<vlan-id> to select the 
VLAN port on which PBR is configured. 
For Virtual port: Navigate to configure port virtual <port-name> to select the Virtual port on 
which PBR is configured. 
7. Traffic Processing 
For Cellular port: Navigate to configure port cellular <port-name> to select the Cellular port on 
which PBR is configured. 
For Wireless port: Navigate to configure port wlan <port-name> access-point <ap-number> to 
select the Wireless port on which PBR is configured. 
For IP tunnel: Navigate to configure router*(<number>)> tunnel-interface(<number>) to select 
the IP tunnel on which PBR is configured. 
2. At the prompt, enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Binding PBR rule to this 
entity 
policy-based-route priority 
<priority> match-acl <name> {next-
hop <ip-address> | interface <type, 
index>} 
no policy-based-route priority 
<priority> 
 
priority <number> - set PBR rule priority 
per interface; the lower is the number, the 
higher is the priority 
Possible values: 1 – 4294967295 
match-acl <name> - attach ACL to PBR rule 
Possible values: 1–80 characters string 
next-hop <ip-address> – Set next hop IP 
address to define the direction of PBR rule 
interface <type, index> – Set interface to 
define the direction of PBR rule. 
Possible values:  
• ethernet < port-name> 
• ethernet < port-name> vlan <vlan-
number> 
• virtual <port-number> 
• cellular < port-name> 
• wlan < port-name> + ap 
• router(<number>)>tunnel-interface 
(<number>)  
Configuration Errors 
Message 
Cause 
Corrective Action 
PBR rule address type mismatch 
In the PBR rule you defined the 
address families of the ACL profile 
and IP-next-hop are not identical. 
Set matching address type for ACL 
profile and IP-next-hop. 
 

## 7.8 Quality of Service (QoS)  *(p.485)*

7. Traffic Processing 
7.8 Quality of Service (QoS)  
ETX-1p supports Quality of Service (QoS), i.e. traffic management, on Ethernet ports to ensure that 
traffic with specific characteristics, such as management, is guaranteed specific bandwidth with 
minimum delay. 
QoS support also includes classification – classifying traffic into traffic-classes on the ingress directions of 
a port. Traffic class defines actions such as fixed Class of Service (CoS) mapping on the ingress direction 
of an Ethernet port and DSCP marking. 
Applicability and Scaling 
This feature is applicable to all the device versions. 
The following quantity of QoS elements can be configured in the device: 
• 
Classifier rules per ingress port: 10   
• 
Traffic-classes per port: 20 
• 
Shaper profiles: 20 
• 
Queue-block profiles: 10 
• 
Queue-group profiles: 10 
Benefits  
QoS allows you to optimize bandwidth for traffic at different requirements of speed and quality, 
avoiding the allocation of excessive bandwidth. 
ETX-1p Quality of Service (QoS) traffic prioritization improves the performance level of data flow. 
Functional Description 
QoS Components 
QoS components include: 
• 
Classifyer Layer-3,4 ingress only (see Classifyer) 
7. Traffic Processing 
• 
Traffic Class (see Traffic-class) 
• 
Queueing (see Queuing) 
Factory Defaults 
See the following sections for each QoS type’s specific defaults. 
Classifier  
ETX-1p  supports classifying traffic into traffic classes on the ingress direction of a port. 
It is possible to define up to ten classifier rules per ingress direction on the Ethernet ports. 
Applicability and Scaling 
This feature is applicable to all ETX-1p devices. 
Functional Description 
Classifying consists of a set of sequentially numbered rules (similar to ACLs), with the following rule 
types: 
• 
Match – defines a classifier action rule for forwarding packets 
• 
Delete – deletes a classifier rule or comments 
• 
Comment – text used for commenting and visually organizing the rules 
• 
Resequence – updates the sequence numbers of existing classifier actions and comments  
Each classifier rule can have an unlimited number of match options. 
The following table specifies the criteria. 
Classification Criteria 
Rule Criterion 
Rule Value/Range 
Comments 
Any 
- 
Allows match any rules 
Layer-3 
 
 
7. Traffic Processing 
Rule Criterion 
Rule Value/Range 
Comments 
IP DSCP 
Range [0–63] 
 
IP protocol 
Value 
 
Source IP address  
IP address/length 
IPv4 or Ipv6  
Destination IP address 
IP address/length 
Ipv4 or Ipv6 
Layer-4 
 
 
TCP Source Port  
Range  
IP Layer 4 
TCP Destination Port  
Range 
IP Layer 4 
UDP Source Port  
Range  
IP Layer 4 
UDP Destination Port  
Range 
IP Layer 4 
The action rule that you define in the classifier is used to perform classification on the forwarding frames 
entering the ingress direction of the port. Those packets that match the defined rules go through the 
port. 
Traffic packets filtered by the classification rule, enter the traffic-class (defined in the classifier), where 
the defined action (e.g. fixed CoS mapping) is performed on the packets. 
Benefits 
With classifying, you can maintain QoS by classifying traffic classes that set traffic CoS and define other 
actions.  
Factory Defaults 
By default, no classifiers are configured. 
Configuring Port Classification 
This section describes how to create a classifier for an Ethernet port. 
 To configure classifying for a port:  
1. For Ethernet port: Navigate to configure port ethernet <port-num> classifier ingress } to select 
the Ethernet port classifier to configure. 
7. Traffic Processing 
Where 
Ingress indicates that the classifier classification direction is from port to application. 
2. At the prompt, perform all required tasks according to the following table. 
Task 
Command 
Comments 
Entering free text among the 
classifier rules 
comment <description> 
[sequence <number>] 
description - free text describing the following 
rules 
Possible values: variable length string, up to 252 
characters 
sequence - sequence number (priority) of the 
comment 
Possible values: 1-4294967295 
Deleting a classifier rule or 
comment 
delete <sequence-number> 
sequence - sequence number of the 
match/drop/comment to be deleted 
Possible values: 1-4294967295 
7. Traffic Processing 
Task 
Command 
Comments 
Defining a classifier action 
rule for forwarding frames  
match  [{dscp <x..y> | 
[protocol <number>]  [src-ip 
<ip-addr>[/<prefix-length>]]  
[dst-ip <ip-addr>[/<prefix-
length>]]  [tcp-src-port 
<x..y>]  [tcp-dst-port <x..y>]  
[udp-src-port <x..y>]  [udp-
dst-port <x..y>] to-tc <tc-
name> [sequence 
<number>]   
match any to-tc <tc-name> 
[sequence <number>]   
 
 
dscp – range of IP DSCP values to compare with 
Possible values: 0-63 
protocol – value of the IPv4 header Protocol 
field or the IPv6 header Next Header field to 
compare with 
Possible values: 0-255 
src-ip – IP address or IP subnet to match against 
the packet's source IP address 
dst-ip – IP address or IP subnet to match against 
the packet's destination IP address 
tcp-src-prt – range of TCP source port numbers 
to compare with 
Possible values: 0-65535 
tcp-dst-prt – range of TCP destination port 
numbers to compare with 
Possible values: 0-65535 
udp-src-prt - the range of UDP source port 
numbers to compare with 
Possible values: 0-65535 
udp-dst-prt – range of UDP destination port 
numbers to compare with 
Possible values: 0-65535 
any – Any incoming frame is matched. 
Possible value: 0 
sequence – sequence number (priority) of the 
rule 
Possible values: 1-4294967295 
to-tc – name of associated tc (traffic-class).  
Define this traffic-class using the traffic-class 
command (see Configuring Traffic-Class). 
Possible values: variable length string, up to 252 
characters 
Notes:  
• Up to five criteria can be specified; they 
must be in the same order in which they 
appear in the command syntax. 
• The same string may be used in separate 
match commands of the same classifier. 
7. Traffic Processing 
Task 
Command 
Comments 
Resequencing the rules (of 
existing classifier actions and 
comments) 
resequence [<step>] 
If you need to add a rule between existing rules 
with consecutive sequence numbers, use this 
command to add space between the rule 
sequence numbers. 
The <step> parameter specifies the interspacing 
value. For example, if you apply resequence 30 
to a port classification that contains rules 1, 2, 
and 3, the rule sequence numbers change to 30, 
60, and 90. 
step – step between sequence numbers 
Possible values: 1-10000 
Default: 10 
Displaying a sorted list of 
port classifier actions 
show status 
See Viewing Port Classifier Status. 
 
Note 
You can remove a classifier from a port, by entering at the prompt,  
no classifier ingress. 
 
Viewing Port Classifier Status 
You can display the status and configuration of an Ethernet port ingress Classifier. 
The following example shows the Ethernet port classifier ingress status. 
 To display Ethernet Classifier (ingress) status:   
config>port>Ethernet wan1> classifier(ingress)# show status 
Ingress Classification Rules: 
Number of Classification Rules (by this port) 
: 10 
 
Sequence     Action TC Name    Admin            Hits 
 
 
     
_ 
  
   10        Match 
Kuku1      Up 
1200  
   20        Match 
Tutu1      Up 
300 
   26        Match 
Tutu1      Up 
300  
   30        Match 
Susu1      Down 
0 
   40        Match 
Fufu1      N/A 
0 
7. Traffic Processing 
Port Status Parameters 
Parameter 
Description 
Direction (Ingress) 
Shows classifier direction (always ingress) 
Number of Classification 
Rules (by this port) 
The number of classifier actions defined for this port  
Possible values: 0-9999 
Sequence 
The sequence number (priority) of the classifier rule  
Possible values: 1-4294967295 
Action 
The type of action 
Possible value: Match 
TC Name 
The name of the associated TC 
Possible values: variable length string, up to 252 characters 
TC Admin 
The administrative status of the associated TC 
Possible values: Up, Down, N/A 
Hits 
The number of incoming frames that matched the rule 
Traffic-Class  
Traffic packets, filtered by the classifier rules, enter the traffic-class for performing the defined actions 
(e.g mapping to transmit queues). ETX-1p supports fixed Class of Service (CoS) mapping on the ingress 
direction of an Ethernet port and marking of DSCP on traffic class in ingress port (LAN).  
Applicability and Scaling 
This feature is applicable to all ETX-1p devices. 
Functional Description 
Traffic-Class 
Traffic packets that match the rules defined in the classifier are forwarded to the traffic-class defined in 
the rules, provided that you defined for the port a traffic-class by that name, and it is in no shutdown 
state. 
Several rules can point to the same traffic-class. 
It is possible to configure up to 20 traffic-classes per port.  
7. Traffic Processing 
CoS Mapping 
Packets that enter the TC (traffic-class) can be mapped to a fixed CoS value defined in the TC definition 
on the port, or if not defined, to CoS 7 (the default; lowest priority). The packet’s meta-data is marked 
with the fixed CoS value across the forwarding path toward the transmit queues.  
A packet is transmitted to the queue corresponding to its CoS value. CoS 0 is mapped to Queue 0, …, CoS 
7 is mapped to Queue 7. 
Marking 
Packets that enter the TC (traffic-class) can have their DSCP marked to a value defined in the TC 
definition on the port, as follows:  
• 
DSCP with a pushed IP header (fixed value); possible values: 0-63 
If not defined, DSCP is marked with pushed IP header 0. 
Configuring Traffic-Class  
 To configure a Traffic-Class: 
1. Navigate to configure port ethernet <port-index> traffic-class (<tc-name>) to select the Ethernet 
port traffic-class to configure. tc-name can be an up to 32-character string. 
2. At the prompt, perform all required tasks according to the following table. 
Task 
Command 
Comments 
Defining traffic class CoS 
(CoS Mapping) by a fixed 
value 
cos fixed <cos-value> 
no cos 
 
cos-value – the CoS assigned to the traffic-
class (fixed value) 
Possible values: 0-7 
Default: 7 (lowest priority) 
0 is the highest priority.  
CoS 0 is mapped to Queue 0, CoS 1 to Queue 
1,…, CoS 7 to Queue 7. 
Enter no cos to delete the CoS definition. 
Defining the traffic class 
with fixed marking 
mark {dscp-fixed <dscp-
value>} 
no mark 
dscp-value possible values: 0-63 
Enter no mark to delete the marking 
definition. 
Enabling/disabling 
traffic-class activity 
shutdown 
no shutdown (default) 
 
7. Traffic Processing 
 
Note 
You can remove a traffic-class, by entering at the prompt,  
no traffic-class <tc-name>. 
Example  
The following example shows how to configure Ethernet port with traffic-class and fixed CoS mapping, 
and define port classification rules. 
• 
Create traffic-class src_ip-Dst_ip on Ethernet port wan1. 
• 
Define CoS mapping of packets that enter traffic-class src_ip-Dst_ip to CoS 0 (highest priority), 
so that packets are transmitted to corresponding Queue 0. 
• 
Define classifier on ingress direction of port traffic with match rule that determines which 
incoming packets are forwarded to traffic-class src_ip-Dst_ip. 
• 
Create traffic-class src_ip-Dst_ip2 on Ethernet port wan1. 
• 
Define CoS mapping of packets that leave traffic-class src_ip-Dst_ip to CoS 1, so that packets are 
transmitted to corresponding Queue 1. 
exit all 
con port ethernet wan1 
traffic-class src_ip-Dst_ip 
cos fixed 0 
exit 
classifier ingress 
match src-ip 10.10.10.10/32  dst-ip 20.20.20.20/32 to-tc src_ip-Dst_ip  
exit  
traffic-class src_ip-Dst_ip2 
cos fixed 1 
exit 
Queuing 
In order to facilitate congestion management, you can sort traffic by applying queue group profiles and 
queue block profiles to queue block entities.  
You can also apply shaper profiles to queue group blocks.  
7. Traffic Processing 
Queueing  
ETX-1p traffic management entities are called queue groups. They are configured over physical ports 
and represents hierarchical structure of queue-blocks. The queue blocks consist of internal queues. The 
queue groups have the following basic structure: 
• 
1 level (level-0) with 1 queue-block 
• 
Shaper towards physical port 
Shapers operate at per-scheduling-element level to shape traffic into a required traffic profile (CIR). 
 
 
 
 
 
Scheduling  
ETX-1p supports a combination of traffic scheduling techniques, whereby applications requiring low 
latency and jitter are mapped to Strict priority queues, while other services are mapped to the 
remaining slots using weighted fair queuing (WFQ)  
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
You can map packets to queues according to the packet’s CoS, with CoS 7 mapped to the lower priority 
queue (Queue 7), and CoS 0 to the highest (Queue 0). 
Level-0 
Q
Q
Q
Q
Scheduler
Q
Q
Q
Q
Shaper
Physical port 
7. Traffic Processing 
QoS Data Flow  
The following is a description of a full featured packet QoS walkthrough from when the packet is 
received in the ingress port.  
• 
A packet is received in the ingress port. 
• 
The classifier checks if the incoming traffic matches the rules – first rule is checked first. If the 
packet matches the rules, it is classified into the defined TC (traffic-class). 
• 
The traffic-class ingress actions (fixed CoS mapping, marking) are operated on the packet.  
• 
The packet is forwarded to a forwarder (router, virtualization, etc). 
• 
The packet is transmitted from the forwarder to the egress port.  
• 
Packet is mapped to level-0 queue-block while queue is mapped according to CoS 
• 
Shaping action is operated on transmit packets towards egress port 
• 
The packet is transmitted. 
 
 
ETX-1p QoS Data Flow  
7. Traffic Processing 
Use Case: Prioritization of Management and User Traffic 
 
 
 
 
 
 
 
 
In this case, QoS does the following: 
• 
Classifies each type of traffic to traffic-class and sets CoS 
• 
Sets queues as follows: 
 
Queue 0 to strict with rate limit 
 
Queue 1 to strict with rate limit 
 
All other queues to WFQ 
• 
Traffic is mapped to queues according to CoS. 
Configuration Method 
You configure QoS in two parts. 
• 
On the physical port, you configure: 
 
Classifier: classifier match rules into TC  
 
TC actions: fixed CoS, marking 
 
Queue-group 
• 
On the QoS level, you configure: 
 
shaper-profile  
 
queue-block-profile 
 
queue-group-profile 
 
Q
5
Q
4
Q
3
Q
2
Scheduler 
Ethernet Port 
Q
7
Q
6
Q
1
Q
0
Management 
User traffic - VoIP 
User traffic - data 
7. Traffic Processing 
Shaper Profiles 
ETX-1p  supports shaper profiles applied to queue group blocks. 
Factory Defaults 
By default, there is no shaper profile configured. 
Configuring Shaper Profiles  
You can configure Shaper profiles and apply them to queue group blocks as needed. 
 To add a Shaper profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type shaper-profile <shaper-profile-name> 
A Shaper profile with the specified name is created and the config>qos>shaper-profile(<shaper-
profile-name>)$ prompt is displayed. The new Shaper profile parameters (except for name) are 
configured by default as described in Factory Defaults. 
3. Configure the Shaper profile as described in Configuring Shaper Profile Parameters. 
 To configure Shaper profiles: 
1. Navigate to configure qos shaper-profile <shaper-profile-name> to select the Shaper profile to 
configure. 
The config>qos>shaper-profile(<shaper-profile-name>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Note 
To delete a profile, make sure it is used in any queue-group (including the case 
when the queue-group is not in use). 
 
Task 
Command 
Comments 
Specifying the CIR (Kbps) and 
CBS (bytes) bandwidth limits  
 
bandwidth [cir <cir-kbit-sec>] 
CIR allowed values: 
• Range: 0 – 4294967295 (in 
kbps) 
• Default: 1000000 
7. Traffic Processing 
Example 
 To create and configure a Shaper profile named Shap2: 
• 
CIR = 99,840 Kbps 
exit all  
configure qos shaper-profile Shap2 
  bandwidth cir 99840  
  exit all 
Queue Block Profiles 
In order to facilitate congestion management, you can sort traffic by applying queue block profiles to 
queue block entities. A queue block profile contains entries for queues 0–7 (queue 0 has the highest 
priority), with the following parameters: 
• 
Scheduling method: 
 
Strict – high-priority queues that are always serviced first. If a lower-priority queue is being 
serviced and a packet enters a higher queue, that queue is serviced immediately.  
 
WFQ (weighted fair queuing) – If one port does not transmit, its unused bandwidth is shared 
by the ‘transmitting’ queues. WFQ frames are transmitted only after transmission of any 
frames associated with Strict queues is completed.  
• 
Bandwidth: 
 
CIR – Defines the Committed Information Rate (CIR) for the current profile. The CIR specifies 
a bandwidth with committed service guarantee (“green bucket” rate). 
 
EIR – Defines the Excess Information Rate (EIR). The EIR specifies an extra bandwidth with 
no service guarantee (“yellow bucket” rate). 
Factory Defaults 
ETX-1p provides a default queue block profile named DefaultQueueBlock1, which defines queues 0–7 as 
follows: 
• 
Scheduling method – WFQ 
• 
CIR = 0 kbps 
• 
EIR = 1000000 kbps 
The default profile is shown below. 
config>qos# info d 
    echo "Queue Block Profile Configuration" 
7. Traffic Processing 
#   Queue Block Profile Configuration 
    queue-block-profile "DefaultQueueBlock1" 
        queue 0 
            bandwidth cir 0 eir 1000000 
            scheduling wfq 
        exit 
        queue 1 
            bandwidth cir 0 eir 1000000 
            scheduling wfq 
        exit 
        queue 2 
            bandwidth cir 0 eir 1000000 
            scheduling wfq 
        exit 
        queue 3 
            bandwidth cir 0 eir 1000000 
            scheduling wfq 
        exit 
        queue 4 
            bandwidth cir 0 eir 1000000 
            scheduling wfq 
        exit 
        queue 5 
            bandwidth cir 0 eir 1000000 
            scheduling wfq 
        exit 
        queue 6 
            bandwidth cir 0 eir 1000000 
            scheduling wfq 
        exit 
        queue 7 
            bandwidth cir 0 eir 1000000 
            scheduling wfq 
        exit 
    exit 
        exit 
    exit 
 
 
config>qos# 
The default profile cannot be deleted. 
Adding Queue Block Profiles 
This section explains how to define queue block profiles. 
 To add a queue block profile: 
1. Navigate to configure qos. 
7. Traffic Processing 
The config>qos# prompt is displayed. 
2. Type:  
queue-block-profile <queue-block-profile-name> [number-of-queues <number>] 
A queue block profile with the specified name, and number of queues, is created, and the 
following prompt is displayed: config>qos>queue-block-profile(<queue-block-profile-name>)$ 
The queues for the new profile are configured by default as described in Factory Defaults. 
3. Configure the queue block profile as described in Configuring Queue Block Profile Parameters. 
Configuring Queue Block Profile Parameters 
 To configure a queue block profile: 
1. Navigate to config qos queue-block-profile <queue-block-profile-name> to select the queue block 
profile to configure. 
The config>qos>queue-block-profile(<queue-block-profile-name>)# prompt is displayed. 
2. Perform the following for each queue that you wish to configure: 
a. To configure a queue, enter: 
queue <queue-ID> 
The following prompt is displayed: 
config>qos>queue-block-profile(<queue-block-profile-name>)>queue(<queue-ID>)#. 
b. Perform the required tasks according to the following table. 
c. Type exit to return to the queue block profile context. 
Note 
To delete a profile, make sure it is used in any queue-group (including the case 
when the queue-group is not in use). 
 
Task 
Command 
Comments 
Defining queue bandwidth 
attributes 
bandwidth [cir <cir-kbit-
sec>] [eir <eir-kbit-sec>] 
CIR allowed values: 
• Range: 0 – 4294967295 (in kbps) 
• Default: 0 
EIR allowed values: 
• Range: 0 – 4294967295 (in kbps) 
• Default: 1000000 kbps (1Gbps) 
CIR + EIR must not exceed the maximum available 
bandwidth. 
7. Traffic Processing 
Task 
Command 
Comments 
Setting scheduling method  scheduling {strict | wfq } 
Default: wfq 
Queues defined as strict must be the highest 
priority queues in a mixed structure. 
 
Example 
 To create and configure a queue block profile named QBlockProf1:  
• 
Queue 0 set to strict scheduling and cir 524,288  
• 
Queue 1 set to strict scheduling and eir 212,992 
• 
Queues 2 and 3 set to WFQ scheduling  
exit all  
configure qos queue-block-profile QBlockProf1 
  queue 0 
    scheduling strict 
    cir 524288 
    exit 
  queue 1 
    scheduling strict 
    eir 212992 
    exit 
  queue 2 
    scheduling wfq  
    exit  
  queue 3 
    scheduling wfq  
    exit  
    exit all 
Queue Group Profiles 
In order to facilitate congestion management, you can sort traffic by applying queue group profiles.  
Factory Defaults 
ETX-1p provides a default queue group profile named DefaultQueueGroup1, configured as shown: 
#   Queue Group Configuration 
    queue-group-profile "DefaultQueueGroup1" 
        queue-block 0/1 
            profile "DefaultQueueBlock1" 
            no shaper 
7. Traffic Processing 
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
Configuring Queue Group Parameters 
 To configure a queue group profile: 
1. Navigate to config qos queue-group-profile <queue-group-profile-name> to select the queue 
group profile to configure. 
The config>qos>queue-group-profile(<queue-group-profile-name>)# prompt is displayed. 
2. Select a queue block in level 0 to configure: 
queue-block 0/1 
The following prompt is displayed: 
config>qos>queue-group-profile(<q-grp-profile-name>)>queue-block(<level/ID>)# 
3. Perform the required tasks according to the following table. 
4. If you wish to configure another queue block, type exit to return to the queue group profile 
context, and start again at step 2. 
Task 
Command 
Comments 
Assigning a queue block profile  
profile <queue-block-profile-name> 
 
Assigning a shaper profile 
shaper profile <shaper-profile-name> 
 
Examples 
Note 
This example uses the Shaper profile and queue block profile created in the 
examples in the preceding sections.  

## 7.9 Router  *(p.503)*

7. Traffic Processing 
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
    shaper profile Shap2 
     exit all 
7.9 Router 
ETX-1p provides Layer-3 forwarding, with multiple (up to 10) Virtual Routing and Forwarding instances 
(VRFs).  
Applicability and Scaling  
This feature is applicable to all ETX-1p versions. 
ARP table is limited to 255 entries. 
Fragmentation does not work on the router interface. Configure the MTU value manually under the 
corresponding port. 
Standards Compliance 
RFC 1812 – Requirements for IP Version 4 Routers  
RFC 2460 – Internet Protocol, Version 6 (IPv6) Specification 
RFC 2464 – Transmission of IPv6 Packets over Ethernet Networks 
RFC 4291 – IP Version 6 Addressing Architecture 
RFC 4294 – IPv6 Node Requirements 
RFC 4862 – IPv6 Stateless Address Autoconfiguration 
7. Traffic Processing 
RFC 2766 – Traditional IP Address Translator 
RFC 3489 – Simple Traversal of User Datagram Protocol through Network Address Translator (STUN) 
RFC 7857 –Traditional IP Address Translator 
RFC 2131 – Dynamic Host Configuration Protocol 
RFC 2132 – DHCP Options and BOOTP Vendor Extensions 
RFC 1701 – Generic Routing Encapsulation (GRE) 
RFC 2890 – Key and Sequence Number Extensions to GRE 
ARP Parameters – Address Resolution Protocol (ARP) Parameters 
RFC 5859 – TFTP Server Address Option for DHCPv4 
Benefits 
The router provides IP Routing and Forwarding for IPv4 and IPv6 packets.  
Functional Description 
ETX-1p Layer-3 forwarding has the following main features: 
• 
Up to 10 routers are supported. Only router 1 can be used for management. 
• 
The maximum number of router interfaces (including loopback interfaces) is 32. 
 
Note 
You may create router interfaces numbered 1-32 in any router (they need not 
be contiguous or start at 1), as long as the total number of router interfaces in 
the device does not exceed 32 
 
• 
IPv4 and IPv6 are both supported. 
• 
Static routing definitions, BGP, OSPFv2 are supported. 
• 
You can configure a management IP address, which is used as a source address in sessions that 
are initiated by the device, such as ping.  
7. Traffic Processing 
The router maintains a table of IPv6 neighbors, via discovery of neighboring IPv6 nodes. It is 
recommended to manage ETX-1p via a router interface defined as a loopback interface, as this router 
interface remains active. To ensure that packets generated by the router are transmitted with the 
loopback IP address, you need to define the management source IP address for IPv4 and IPv6 (refer to 
Management Source IP Address in the Management and Security chapter).  
Router interface that resides directly on a port uses that port’s MAC address.  
The control packets transmitted by the router have a configurable IP DSCP value, so that each router 
entity can control its traffic priority by setting its DSCP value for its protocols (see Configuring the 
Router on how to configure the DSCP). 
The embedded router supports the Border Gateway Protocol (BGP) – See Routing Protocol BGP. 
DHCP Client 
ETX-1p supports DHCP and DHCPv6 client functionality.  
Each ETX-1p router interface can either have a static IP address assigned to it or can be configured to 
acquire a dynamic address via DHCP.  
DHCP client configuration is performed inside a router interface.  
A router interface supports only one instance of DHCP client, and a DHCP client instance can be bound 
to only one router interface. 
The DHCPv6 client supports prefix delegation. It can receive from the provider a prefix, out of which 
shorter prefixes can be allocated to the user-side router interfaces and the machines behind them. The 
prefixes are passed to those machines by IPv6 router advertisements. They cannot be passed with 
DHCPv6 server.  
RA also passes DNS server addresses and hostname information. Dynamically received data is passed if 
none is configured. Otherwise, the configured data is passed. This enables the device to be a DNS proxy, 
publishing its own address as DNS server to the user hosts behind it, while using dynamically received 
DNS server addresses as the next resolver for its own use. 
Note 
If a DHCPv6 client is configured to receive prefix delegation information, it 
cannot receive an address for its router interface, and vice versa. To work with 
PD, you can configure ETX-1p to receive an address from a DHCPv6 client 
(without PD), and initiate a ZTP process; the ZTP configuration file can 
statically configure the address, and activate PD. Another option is to use RA 
for receiving address and DHCPv6 client for PD. 
7. Traffic Processing 
Crypto Map 
ETX-1p supports binding of a defined crypto map (see Configuring Crypto Map) to a router interface. 
One map can be associated with multiple interfaces, and multiple maps (up to five) can be associated 
with one interface. 
If the router interface has multiple IP addresses, by default the lowest one is used as the IPsec tunnel 
source.  
You can bind a predefined crypto map to an address (even if the router interface has a single address). 
In this case: 
• 
The tunnel source is the one configured. 
• 
If the interface does not own the configured address, ETX-1p ignores the configuration and 
behaves as if the map is not bound to the interface. 
Factory Defaults  
By default, no router interfaces exist. The other router parameters are configured as shown in the 
following table.  
By default, the source management IP address for IPv4/IPv6 is not configured. 
 
Parameter 
Default  
Remarks 
name   
"Router#1” 
 
dhcp-client duid-type 
ll 
 
dhcp-client host-name 
sys-name 
In the DHCP client, the device 
name is used as the host name.  
dhcp-client vendor-class-id 
ent-physical-name 
In the DHCP client, the entity 
physical name is used as the 
vendor class ID. 
tunnel-interface 
gre-ip  
Tunnel type, when tunneling is 
configured 
7. Traffic Processing 
Configuring the Router 
The router functionality allows ETX-1p to establish links to Ethernet ports via SVIs, or to peers that 
provide the 1588v2 master clock, or to establish PPPoE sessions via PPP ports. 
 To configure the router:  
1. At the config# prompt, enter: 
router <number> 
The config>router(<number>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Configuring BGP 
[no] bgp <as-number> 
as-number – local AS 
Possible values: 1-4294967295, 
Default: 0 
See Routing Protocol BGP 
Deleting dynamic ARP entities 
clear-arp-table [<address>] 
Specify the IP address to clear 
only the entries corresponding 
to it. 
Clearing IPv6 neighbor table 
clear-neighbor-table 
 
Configuring DHCP client for the 
router interface 
dhcp-client 
 
Commands in level dhcp-client 
 
 
Providing host name to DHCP 
server 
host-name <string> 
host-name sys-name 
no host-name 
You can specify a name, or 
specify sys-name to indicate 
that the system name should be 
used as the host name. 
Providing vendor ID to DHCP 
server 
vendor-class-id <string> 
vendor-class-id 
ent-physical-name 
You can specify an ID, or specify 
ent-physical-name to indicate 
that the device name should be 
used as the vendor ID. 
7. Traffic Processing 
Task 
Command 
Comments 
Configuring DHCP client to 
request DHCPv6 server for 
option 17  
dhcpv6-option-request 
[vendor-specific-information-
17] 
no dhcpv6-option-request 
Relevant for IPv6. 
Vendor specific information 
option 17 is used to pass data 
needed for the Zero Touch 
process.  
Notes:  
• The command behaves the 
same regardless of whether 
you specify vendor-specific-
information-17 optional 
keyword. 
• If you repeat the command, 
the last instance replaces 
the previous. 
Entering no dhcpv6-option-
request results in DHCP client 
not explicitly requesting option 
17.  
Configuring DHCPv6 Unique 
Identifier (DUID) type  
duid-type {en | ll} 
Relevant for IPv6. 
• en –enterprise number (type 
2); comprises an enterprise 
number (RAD’s is 164) and 
an identifier (MAC address 
of the port out of which the 
request is sent) 
ll – link layer address (type 3); 
comprises a hardware type (1 
for Ethernet) and a link-layer 
address (MAC address of the 
port out of which the request is 
sent) 
Configuring DNS server 
 
 
dns-name-server <ip-address> 
[priority <priority>] 
 
Type [no] dns-name-server <ip-
address> to delete the DNS 
server. 
ip-address can be IPv4 or IPv6 
priority 
Possible values: 1–255 
Configuring DSCP value for 
router entity traffic 
dscp <number> 
Possible values: 0–63 
Default: 0 
7. Traffic Processing 
Task 
Command 
Comments 
Creating a router interface 
interface <interface-num> 
[{loopback } ] 
interface-num – a unique 
number assigned to the router 
interface 
Possible values: 1–32 
loopback – sets router interface 
as loopback  
Type no interface number to 
delete a router interface. 
See the Configuring Router 
Interfaces section for a list of 
tasks that can be configured on 
a router interface. 
Assigning name to router 
name <string> 
Alphanumeric string 
Enter no name to remove 
router name. 
Enabling, or disabling and 
deleting Network Address 
Translator (NAT) 
nat 
Typing no nat disables and 
deletes the existing NAT 
configuration, including. all 
mapping table entries. 
Note: You can configure a single 
instance of NAT over each one 
of the supported VRFs. 
For details on configuring NAT 
parameters, see Configuring 
Network Address Translator 
(NAT) 
Configuring OSPF 
ospf 
See Configuring OSPF at the 
Router Level 
Creating a prefix-list policy              
profile for the router 
prefix-list <name> {ipv4|ipv6} 
 
Name – unique prefix-list policy 
profile name.  
1-252 characters 
Entering no prefix-list <name> 
deletes the router’s prefix-list 
policy profile. 
7. Traffic Processing 
Task 
Command 
Comments 
Resequencing policy profile 
resequence <name>  
 
name –policy profile to 
resequence; 1..252 characters 
number – steps between policy 
rules entries numbers 
Possible values: 1-100000 
Default: 10 
Creating the router’s route-map    
policy profile 
route-map <name> 
name – route-map policy profile 
unique name. 1-252 characters 
Entering no route-map <name> 
deletes the router’s route-map 
policy profile. 
Enabling the static route and the 
next gateway (next hop) using 
the next hop’s IP address 
static-route 
<IP-address/IP-mask-of-static-ro
ute> address 
<IP-address-of-next-hop> 
[metric <metric>][ install | no-
install ] 
no static-route <IP 
Address/prefix-length> address 
<address> 
 
The next hop must be a subnet 
of one of the router interfaces. 
To set the default-gateway, 
configure static route of address 
0.0.0.0/0 to next hop default 
gateway address. Entering no 
static-route deletes static route 
entry. 
Metric specifies the priority of 
the static route 
Possible values: 1–255 
Note: the value of 255 is 
considered as unreachable and 
the appropriate route is not be 
added to the routing table. 
Default: 1 
install option forwards a specific 
route entry into the FIB. 
no-install option does not 
forward a specific route entry 
into the FIB. 
7. Traffic Processing 
Task 
Command 
Comments 
Enabling the static route and the 
router interface number toward 
which the destination subnet is 
to be routed 
static-route 
<IP-address/IP-mask-of-static-ro
ute> interface 
<router-interface-num> [metric 
<metric>][ install | no-install ] 
no static-route <IP 
Address/prefix-length> interface 
<router-interface>  
no static-route deletes static 
route entry. 
Metric specifies the priority of 
the static route: 1–255 (default: 
1). 
<priority> should be an integer 
in range 1–255.  
Note: the value of 255 is 
considered as unreachable and 
the appropriate route is not be 
added to the routing table. 
Install option forwards a specific 
route entry into the FIB. 
No-install option does not 
forward a specific route entry 
into the FIB. 
Configuring tunnel interface 
tunnel-interface <number> 
[gre-ip | ipsec]  
 
number – tunnel number 1-256 
Entering no tunnel-interface 
<number> deletes the tunnel 
interface. 
See Port Classification for more 
details 
Displaying the address 
resolution protocol (ARP) table, 
which lists the original MAC 
addresses and the associated 
(resolved) IP addresses 
show arp-table 
[ address <ip-address> ] 
 
 
See Viewing ARP Table 
Note: The ARP table is limited to 
255 entries. 
Displaying DNS resolver 
show dns-resolver 
 
Displaying IPv6 neighbors table 
show neighbor-table [address 
<ip-address>] 
See Viewing IPv6 Neighbors 
Displaying the IPv4 or IPv6 RIB 
(Routing Information Base) table 
show rib { ipv4 | ipv6 }  
See Viewing RIB 
Displaying VRRP summary 
show vrrp-summary 
 
7. Traffic Processing 
Task 
Command 
Comments 
Displaying the routing table 
show routing-table [address 
<IP-address/IP-mask>] [protocol 
{dynamic|static}]  
 
IP-address/IP-mask – View 
routing information for a 
specific IP address of a specified 
prefix length. 
See Viewing Routing 
Information 
Displaying the interface table 
show summary-interface 
See Viewing Router Interface 
Status 
Displaying the IP monitoring 
summary 
show ip-monitoring-summary  
See Viewing IP Monitoring 
Status 
Configuring Router Interfaces 
You can configure up to 32 router interfaces. 
 To configure a router interface: 
1. At the config>router(<number>)# prompt, enter: 
interface <interface-num> [loopback] 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning an IP address and 
prefix length to the router 
interface 
address 
<IP-address/prefix-length> 
no address 
<IP-address/prefix-length> 
 
 
The IP address can be IPv4 (e.g. 10.10.10.1) 
or IPv6 format (e.g. 
10:10:10:10:10:10:10:10) 
Prefix length:  
• For vitual ports: IPv4 1–32; IPv6 1–128 
• For other ports: IPv4 1–31; IPv6 1–127 
You cannot define an IP address if the 
router interface is bound to a PPP port. 
7. Traffic Processing 
Task 
Command 
Comments 
Binding router interface to a 
port (Cellular, Ethernet, 
Virtual, or PPP), or access 
point  
bind cellular < port-name>[sim 
<sim#>] [apn <apn# 1..4>] 
bind ethernet <port-name> [vlan 
<vlan-id>] 
bind virtual <port-index> [vlan 
<vlan-id>] 
bind ppp <port-number> 
bind wlan {2.4g  } access-point 
<ap-number> 
no bind 
[no] bind wifi-client [1] 
 
• port-number (port-name) – number 
(name) of device interface port 
connected to the router interface. 
• vlan-id - port number of the VLAN port 
connected to the router interface 
sim must be configured only for the device 
operating in single modem (configure port 
cellular lte) and dual sim configuration. 
<sim#> options: 
• sim1 
• sim2  
• auto 
Default: auto 
Associating router interface 
with a crypto map 
crypto-map <name> [address 
<ip-address>] 
no crypto-map <name> 
name – crypto map name 
Possible values: 1-80 character string 
ip-address – local peer IP address 
Notes:  
• You can associate up to five crypto 
maps with one interface. 
• If no address is specified, ip-address is 
an empty string. 
If the specified crypto map is not 
defined, ETX-1p ignores this 
configuration and behaves as if it is not 
bound to it. 
Enabling/disabling DHCP 
client 
dhcp 
no dhcp 
You cannot enable DHCP (for IPv4) in the 
following cases: 
• Router interface is bound to a PPP port. 
• IPv4 address is configured. 
• Router interface is not unnumbered. 
• DHCPv6 is enabled. 
Configuring DHCP client for 
the router interface 
dhcp-client 
 
Command in level dhcp-client  
 
 
Providing client ID (DHCP 
option 61) to DHCP server 
client-id id <string> 
client-id mac 
You can specify an ID, or specify mac to 
indicate that the device MAC address 
should be used as the client ID. 
7. Traffic Processing 
Task 
Command 
Comments 
Enabling or disabling DHCPv6 
client for the router interface 
dhcpv6-client [pd name <prefix-
name>] [rapid-commit] 
no dhcpv6-client 
 
You can enable DHCPv6 client provided 
that the following conditions exist: 
• Router entity is Router # 1. 
• There is no other DHCPv6 client defined 
in the device. 
• DHCPv4 is not enabled. 
• The router interface is not defined as 
loopback. 
It is optional to enable rapid commit or 
prefix delegation (pd). 
prefix-name – 1-255 character string 
Note:  
• If the command is repeated, the last 
instance applies. 
DHCPv6 client, server, and relay are 
mutually exclusive on the same interface. 
Therefore, it is possible to enable a client, 
only if neither a relay nor a server are 
configured on the router interface. 
Enabling DHPv6 server 
dhcpv6-server pool <pool-name> 
[rapid-commit] [preference 
<value>]  
no dhcpv6-server 
pool – defines the pool name 
rapid-commit – enables DHCPv6 rapid 
commit 
preference (optional) – configures 
preference in DHCPv6 advertisement 
messages; possible values: 0 to 255 
The DHCPv6 client and server  functions are 
mutually exclusive on an interface.  
Enabling/disabling IP 
forwarding 
ip-forwarding 
 
Configuring IPv6 address from 
prefix 
ipv6-address-prefix <prefix-
name> <prefix-length> [no-
autoconfig] 
no ipv6-address-prefix <prefix-
name> 
 
If you repeat the command with the same 
prefix name, the new command replaces 
the previous one. 
If you try to repeat the command with a 
different prefix name, ETX-1p rejects the 
command  
7. Traffic Processing 
Task 
Command 
Comments 
Enabling or disabling IPv6 
autoconfiguration on router 
interface 
ipv6-autoconfig 
no ipv6-autoconfig 
Enter no ipv6-autoconfig to disable IPv6 
autoconfiguration. 
Configuring interface 
management access  
management-access {allow-all | 
allow-ping} 
 
You can set management access to 
allow-all for up to two router interfaces. 
Enter no management-access to remove 
management access from router interface. 
Assigning a name to the 
router interface 
name <interface-name> 
no name 
 
Configuring OSPF 
ospf 
 
See Configuring OSPF at the Interface 
Level 
Enabling or disabling IPv6 
router-advertisement 
router-advertisement 
no router-advertisement 
 
Displaying ACL summary 
show access-list summary 
See Viewing Access List Status. 
Displaying crypto map 
information 
show crypto-map-status 
[<name>] 
 
name – crypto map name 
Possible values: 1-80 character string 
Note: If name is specified, the command 
displays the data of only that crypto map. 
Otherwise, the command displays data of 
all the crypto maps associated with the 
interface. 
For a detailed description of the crypto 
map parameters, see Viewing Crypto Map 
Information below. 
Displaying router interface 
status 
show status 
See Viewing Router Interface Status. 
Administratively enabling or 
disabling the router interface 
no shutdown 
shutdown 
Entering shutdown disables the interface. 
Enable sending of ICMP 
Unreachable messages for the 
router interface 
unreachables 
no unreachables 
 
Deleting a Router 
You can delete a router if there are no router interfaces associated with it. 
7. Traffic Processing 
 To delete a router: 
• 
At the config# prompt, enter: 
no router <number> 
Deleting a Router Interface 
 To delete a router interface: 
• 
At the config>router(<number>)# prompt, enter: 
no interface <interface-num> 
Viewing Router Information 
You can view information on each router by using the show summary-interface command. 
 To display the router information: 
1. Navigate to configure router <number>.  
2. At the config>router(<number>)# prompt that is displayed, enter show summary-interface. 
The router interface information is displayed. 
 
 
 
config>router(1)# show summary-interface 
 
Router Interface: 1 
  Name:           RI 1 
 
  Admin:Up      Oper: LLD         Bound to:  ethernet lan1  
 
  172.17.161.101/24                           (manual)        (preferred) 
 
 
Router Interface: 2 
  Name:           RI 2 
 
  Admin:Up      Oper: Up          Bound to:  ethernet lan2  
 
  10.10.10.1/24                               (manual)        (preferred) 
The above fields are: 
7. Traffic Processing 
Router Interface (number) 
Unique number assigned to the router interface 
Name 
Name of the router interface (alphanumeric string) 
Admin 
Administrative status: 
Up – ready to pass packets 
Down  
Oper 
Operational status: 
Up – ready to pass packets 
Down 
LLD – Lower Layer Down; down due to state of lower-layer 
interface(s) 
Bound to 
The port that the router interface is bound to 
IP Addresses 
IP Address/prefix length 
IPv4 or IPv6 address and prefix length  
Note: Supported for DHCPv6 
origin 
Origin of the IP address. 
Possible origins are:  
other – for example, link local address 
manual – indicates that the address was manually configured 
to a specified address 
dhcp – indicates an address that was assigned to this system 
by a DHCP server 
link layer – indicates an address created by IPv6 stateless 
auto-configuration 
random – indicates an address chosen by the system at 
random 
7. Traffic Processing 
Router Interface (number) 
Unique number assigned to the router interface 
Name 
Name of the router interface (alphanumeric string) 
status 
Status of the IP address.   
Available statuses (from the IPv6 Stateless Address 
Autoconfiguration protocol) are: 
preferred (default) 
deprecated 
invalid 
inaccessible 
unknown 
tentative 
duplicate 
optimistic 
 
  
Viewing Access List Status 
You can view the access list summary using the show access-list summary command. 
 To view access-list summary: 
1. Navigate to configure router <number> interface <number>.  
2. At the config>router(<number>) interface (<number>)#  prompt that is displayed, enter show 
access-list summary. 
3. The access list summary is displayed. 
ACL Name  Type  Bound To  Direction 
----------------------------------- 
my-acl    IPv4  RI 1/1    Inbound  
Viewing ARP Table 
 To display the ARP table: 
1. Navigate to configure router <number>.  
2. At the config>router(<number>)# prompt that is displayed, enter show arp-table. 
7. Traffic Processing 
The ARP table is displayed. 
config>router(1)# show arp-table 
IP Address          MAC Address         Status 
--------------------------------------------------------------- 
172.17.161.1        E0-2F-6D-12-95-42   Dynamic 
Viewing Crypto Map Information 
You can view information on a specific crypto map or all configured crypto maps using the show crypto-
map-status command. 
 To display the crypto map information: 
1. Navigate to configure router <number>interface<number>.  
2. At the config>router(<number> interface (<number>))# prompt that is displayed, enter show 
crypto-map-status.  
config>router(1)interface(1)# show crypto-map-status 
Crypto Map               : my-map-1 
Tunnel Peers             : 10.10.10.1 --- 20.20.20.1  
Security Association     : Up 111 minutes ago 
IKE 
  Version                : 2     : 
  SA Negotiation Mode    : Main 
  Authentication         : Pre-shared secret 
  Encryption             : AES-CBC-256 
  Hashing                : SHA1-96-HMAC 
  Diffie Hellman Group   : 20 
  In SPI                 : 7423470e4a9ab53b 
  Out SPI                : 987279bf53131617 
  Reauthentication in    : 10 minutes 
Transform Set            : 
  Algorithms             : ESP-AES-GCM-256 
  In SPI                 : c8a473f3 
  Out SPI                : ca7455fb 
  Remaining Lifetime     : 
    In Kilobytes         : 10000 
    Out Kilobytes        : 2000 
    Seconds              : 100 
 
 
The above fields are: 
Tunnel Peers 
Local peer --- remote peer 
Possible values: ip-address 
7. Traffic Processing 
Local Protected Networks 
Local protected network. 
Possible values: <ip-address>/<prefix-length> 
 
Remote Protected Networks 
Remote protected network. 
Possible values: <ip-address>/<prefix-length> 
 
Security Association 
SA status and SA age 
Possible values:  
SA status – Connecting, Down, Up 
SA age – <number> minutes ago 
IKE  
Version 
IKE version 
Possible values: 1, 2 
SA Negotiation Mode 
IKE SA negotiation mode 
Possible values: Aggressive, Main 
Authentication          
IKE authentication method  
Possible value: Pre-shared secret 
Encryption            
IKE encryption algorithm  
Possible values: AES-CBC-128, AES-CBC-256, AES-128-GCM-
64, AES-128-GCM-96, AES-128-GCM-128, AES-256-GCM-
64, AES-256-GCM-96, AES-256-GCM-128 
Hashing                 
IKE hashing algorithm   
Possible values: SHA1-96-HMAC, SHA2-256-128-HMAC,  
SHA2-512-256-HMAC 
Diffie Hellman Group 
IKE Diffie Hellman group 
Possible values: 1, 2, 5, 14, 19, 20 
7. Traffic Processing 
In SPI 
IKE in SPI 
Possible values: string 
Out SPI 
IKE out SPI 
Possible values: string 
Re-authentication in 
Time to IKE key re-authentication 
Possible values: <number> minutes/hours/days 
Transform Set 
Algorithms  
Transform set first algorithm 
Possible values: ESP-AES-CBC-128, ESP-AES-CBC-256, ESP-
AES-GCM-128, ESP-AES-GCM-256, ESP-NULL, ESP-AES-
GMAC-128, ESP-AES-GMAC-256 
Transform set second algorithm 
Possible values: ESP-SHA1-96-HMAC, ESP-SHA2-256-128-
HMAC, ESP-SHA2-512-256-HMAC 
In SPI 
Transform set in SPI 
Out SPI 
Transform set in SPI 
Remaining Lifetime 
In Kilobytes 
Transform set remaining lifetime (in kilobytes) 
Out Kilobytes 
Transform set remaining lifetime (out kilobytes) 
Seconds 
Transform set remaining lifetime (seconds) 
Viewing IPv6 Neighbors  
You can view information on each IPv6 neighbor by using the show neighbor-table command. 
 To display the neighbor table: 
1. Navigate to configure router <number>.  
7. Traffic Processing 
2. At the config>router(<number>)# prompt that is displayed, enter show neighbor-table. 
The IPv6 neighbors are displayed. 
config>router(1)# show neighbor-table  
IPv6 Address                             MAC address        State  Interface 
============================================================================= 
1234:1234:1234:1234:1234:1234:1234:1234  01-01-01-01-01-01  reachable   1 
1234:1234:1234:1234:1234:1234:1234:1234  01-01-01-01-01-01  incomplete  28 
FE80::200:E8FF:FE00:2A2B                 00-00-e8-00-2a-2b  stale       2 
The above fields are: 
IPv6 address 
Neighbor IPv6 address 
MAC address 
Neighbor MAC address 
State 
The Neighbor Unreachability Detection state for the interface when the 
address mapping in this entry is used:  
• reachable – confirmed reachability 
• stale – unconfirmed reachability 
• delay – waiting for reachability confirmation before entering probe state 
• probe – actively probing 
• invalid – invalidated mapping 
• unknown – state cannot be determined for some reason 
• incomplete – address resolution is being performed 
interface 
Router interface number 
Viewing IP Monitoring Status  
For the feature description, see IP Monitoring in the Monitoring and Diagnostics chapter. 
 To display IP monitoring status: 
1. Navigate to configure router <number>.  
2. At the config>router(<number>)# prompt that is displayed, enter show ip-monitoring-summary. 
The ip-monitoring status is displayed. 
configure> router (1) #show ip-monitoring-summary 
ip-monitoring (AAA) 
      Tracked interface: Router-interface 1/1 
            Target IP: 1.1.1.1 
            Status: UP 
            Last change time 2022-01-30  05:42:24.00 
7. Traffic Processing 
      Tracked interface: Tunnel-interface 2/1 
            Target IP: 1.1.1.1 
            Status: DOWN 
 
            Last change time 2022-01-30  05:42:24.00 
ip-monitoring (BBB) 
      Tracked interface: Tunnel-interface 3/2 
            Target IP: 2.2.2.2 
            Status: UP 
            Last change time 2022-01-30  05:42:24.00 
Status Parameters 
Parameter 
Description 
Tracked interface 
The device interface tracked by IP monitoring entity 
Target IP 
Target IP address 
Status 
 
IP monitoring entity status 
Possible Values: 
• Inactive  
• UP  
• DOWN  
Last change time 
Last change date and time  
Viewing RIB 
You can view the RIB (Routing Information Base) by using the command show rib. This command is 
available in the CLI contexts for IPv4 or IPv6, at the router level: config>router(<number>)#.  
 To display the IPv4 RIB: 
1. Navigate to configure router <number>.  
2. At the config>router(<number>)# prompt that is displayed, enter show rib ipv4. 
The IPv4 RIB is displayed. 
config>router(1)# show rib ipv4 
* = Active Route 
   Network              > Next Hop             RI  Proto  Metric 
============================================================================= 
*  0.0.0.0/0            > 172.17.171.1          2  Static      1 
*  2.2.2.0/24           > 172.17.171.205        2  BGP           
*  3.3.3.0/24           > 0.0.0.0               1  Local       0     
   3.3.3.0/24           > 172.17.171.205        2  BGP 
*  111.222.111.0/24     > 0.0.0.0               2  Local       0     
   111.222.111.0/24     > 172.17.171.205        2  BGP 
7. Traffic Processing 
 To display the IPv6 RIB: 
1. Navigate to configure router <number>.  
2. At the config>router(<number>)# prompt that is displayed, enter show rib ipv6. 
The IPv6 RIB is displayed. 
config>router(1)# show rib ipv6 
* = Active Route 
   Network              > Next Hop             RI  Proto  Metric 
============================================================================= 
*  ::/0                 > 11:11:11:11::1        1  Static      1   
*  11:11:11:11::/64     > ::                    1  Local       0     
*  abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126      
   > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd    1  Static      1 
*  fe80::/64            > ::                    1  Local       0     
The above fields are: 
Status (Active Route) 
Marks with a “*” an ‘Active Route’, i.e. route entry is forwarded to the FIB 
(Forwarding Information Base) 
Network 
IPv4 or IPv6 network address (prefix and prefix length) 
IPv4 prefix length can be 0–32; IPv6 prefix length can be 0–128. 
Next hop 
Route entry next hop IP address 
RI 
Local interface through which the next hop of this route should be reached 
Protocol 
Source protocol 
Metric 
Route entry metric 
Viewing Routing Information  
You can view all routing information or only information on dynamic or static routes, for all IP addresses 
or for a specific IP address and prefix length of a dynamic or static by using the show routing-table 
command:  
config>router(<number>)>show routing-table [ address <IP-address/IP-mask> ] 
[ protocol { dynamic | static } ]. 
 To display the routing table: 
config>router(1)# show routing-table  
IP address/prefix    Next Hop       interface    Protocol    Metric  
==================================================================== 
172.17.175.0/24      172.177.170.100    1        Static 
  250 
7. Traffic Processing 
172.17.176.0/24      0.0.0.0            3        Local        0 
1.1.1.1/32           0.0.0.0            4        Local        0 
The above fields are: 
IP address/prefix 
IPv4 or IPv6 address and prefix length 
Next Hop 
Route entry next hop IP address 
Interface 
Router interface number 
Protocol 
Source protocol: 
• static 
• local 
• bgp 
Metric 
Route entry metric 
When protocol is BGP, this is blank. 
Viewing Router Interface Status 
You can view the router interface status by using the show status command:  
config>router(<number>) >interface(<interface-num>) >show status. 
 To display the router interface status: 
1. Navigate to configure router <number> interface <number>.  
2. At the config>router(<number>) interface(<number>)#  prompt that is displayed, enter show 
status. 
The router interface status is displayed. 
config>router(1)>interface(1)# show status  
Admin: Up     Oper: Up  
Ip Addresses:  
  
30.30.30.11/24 (dhcp) (preferred)  
  
IPv4 Default Router : 30.30.30.1  
  
DHCP Client Information  
DHCP Status : Holding Lease  
  
Server : 30.30.30.1  
Router : 30.30.30.1  
Lease Obtained : 2017-02-10 18:21:20  
7. Traffic Processing 
Expires : 2017-02-10 18:26:20  
Lease Renewal: : 2017-02-10 18:23:50  
Rebinding: : 2017-02-10 18:25:42  
TFTP Server : --  
Bootfile Name : --  
Host Name : --  
Static Routes : --  
The above fields are: 
Admin 
Administrative status: 
• up – ready to pass packets 
• down  
Oper 
Operational status: 
• up – ready to pass packets 
• down  
IP Addresses 
IP Address/prefix length IPv4 or IPv6 address and prefix length  
Note: Supported for DHCPv6 
origin 
Origin of the IP address. 
Possible origins are:  
• other 
• manual 
• DHCP 
• link layer 
• random 
status 
Status of the IP address.   
Available statuses (from the IPv6 Stateless Address Autoconfiguration 
protocol) are: 
• preferred (default) 
• deprecated 
• invalid 
• inaccessible 
• unknown 
• tentative 
• duplicate 
• optimistic 
7. Traffic Processing 
IPv4 Default Router 
IP address of the IPv4 default router 
DHCP Client Information (Section appears only when DHCP is enabled.)  
Status 
DHCP client operational status. Available options are: 
• Holding Lease 
• Not Holding Lease 
• Failed to Obtain Lease 
• Waiting for Lease 
• Initializing 
• No Lease Address In Use 
Server 
Displays client server’s address 
Router 
List of default routers, in order of preference 
If the first router is in use, (active) is displayed following its address. 
The first router is not in use if: 
• There is a different static default router. 
• The DHCP default router is invalid, i.e., not on the device’s networks. 
Lease Obtained 
Date and time when the DHCP lease was obtained 
Expires 
Date and time when the DHCP lease will expire, if not renewed 
Lease Renewal 
Date and time when the device will try to renew the DHCP lease. 
renewal time = (expired - obtained) * 0.5 
If the lease last chance for renewal time passes,  --  is displayed. Otherwise, 
the next renewal time is displayed, as follows: 
• Date and time, formatted like other date and time values in the device (by 
default as dd mm-yyyy hh:mm:ss) 
• If real time clock is not available, time in seconds since startup. 
Rebinding 
Date and time when the device will try to rebind the DHCP lease 
TFTP Server 
IP address of TFTP server, received by DHCP 
Boot file Name 
File to obtain from TFTP server, received by DHCP 
Host Name 
Host name, received by DHCP 
Static Routes 
File to obtain from TFTP server, received by DHCP 
 
7. Traffic Processing 
Viewing Router Statistics 
You can view the router statistics using the show statistics command.  
 To view router IPv4 traffic statistics: 
1. Navigate to configure router <number>.  
2. At the config>router(<number>)  #  prompt that is displayed, enter show statistics ipv4 traffic. 
The router interface IPv4 traffic statistics are displayed. 
IPv4 statistics:  
In: 
Receives:          18446744073709551616 Octets:        18446744073709551616 
Multicast Packets: 18446744073709551616 Multicast Octets:18446744073709551616 
Broadcast Packets: 18446744073709551616 Header Errors:   4294967296 
No Routes:                 4294967296   Address Errors:           4294967296 
Unknown Protocols:         4294967296   Truncated Packets:        4294967296 
Forward Packets:  18446744073709551616  Reassembled Required:     4294967296  
Reassembled Ok:              4294967296 Reassembled Fails:        4294967296 
Discards:                    4294967296 Delivers:       18446744073709551616 
Out: 
Requests:          18446744073709551616 No Routes:               4294967296 
Forward Packets:   18446744073709551616 Discards:                4294967296 
Fragmentation Required:      4294967296 Fragmentation Ok:        4294967296 
Fragmentation Fails:         4294967296 Fragmentation Creates:   4294967296 
Transmits:         18446744073709551616 Octets:        18446744073709551616 
Multicast Packets: 18446744073709551616 Multicast Octets: 8446744073709551616 
Broadcast Packets: 18446744073709551616   
 
 
 To view router IPv6 traffic statistics: 
1. Navigate to configure router <number>.  
2. At the config>router(<number>)#  prompt that is displayed, enter show statistics ipv6 traffic. 
The router interface IPv6 traffic statistics are displayed. 
IPv6 statistics:  
In: 
Receives:          18446744073709551616 Octets:          18446744073709551616 
Multicast Packets: 18446744073709551616 Multicast Octets:18446744073709551616 
Broadcast Packets: 18446744073709551616 Header Errors:             4294967296 
No Routes:                   4294967296 Address Errors:            4294967296 
Unknown Protocols:           4294967296 Truncated Packets:         4294967296 
Forward Packets:   18446744073709551616 Reassembled Required:      4294967296 
Reassembled Ok:              4294967296 Reassembled Fails:         4294967296 
Discards:                    4294967296 Delivers:        18446744073709551616 
Out: 
7. Traffic Processing 
Requests:          18446744073709551616 No Routes:                 4294967296 
Forward Packets:   18446744073709551616 Discards:                  4294967296 
Fragmentation Required:      4294967296 Fragmentation Ok:          4294967296 
Fragmentation Fails:         4294967296 Fragmentation Creates:     4294967296 
Transmits:         18446744073709551616 Octets:          18446744073709551616 
Multicast Packets: 18446744073709551616 Multicast Octets:18446744073709551616 
Broadcast Packets: 18446744073709551616  
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Cannot delete; interface associated 
with the router 
You tried to delete a router entity 
that has router interfaces 
associated with it. 
Disassociate router interfaces from 
router. 
Cannot set address; DHCP enabled 
You tried adding an IPv4 address 
when DHCP is enabled. 
Disable DHCP. 
Cannot set address; too many 
addresses already configured 
You tried adding an IP address, but 
the amount of IP addresses already 
reached its limit. 
Delete one of the associated 
addresses before associating a new 
IP address. 
Cannot set address; invalid 
You tried adding a multicast IP 
address or an interface IPv4 
address with prefix length 32 (, 
which is only allowed for loopback 
interface). 
When configuring static-route, you 
tried to do one of the following: 
• Add a multicast IP network 
address. 
• Add an IP network address 
when it was not allowed. 
 
Use /31 prefix-length on non point-
to-point interface cautiously  
You tried adding anIPv4 interface 
address with prefix length 31. 
 
7. Traffic Processing 
Message 
Cause 
Corrective Action 
Cannot modify; activated router 
interface 
You tried modifying or removing a 
bound port while the router 
interface was activated (no 
shutdown). 
You tried adding, modifying, or 
removing a VLAN while the router 
interface was activated (no 
shutdown). 
Shut down the router interface and 
try again. 
Cannot enable; IPv4 address exists 
You tried enabling DHCP even 
though manual IPv4 address exists. 
 
Cannot enable; DHCPv6 is enabled 
You tried enabling DHCP even 
though DHCPv6 is enabled. 
Disable DHCPv6. 
Cannot set; DHCPv6 client is 
already defined 
You tried enabling DHCPv6 client 
when there is already one defined 
in the device. 
Remove existing DHCPv6 client. 
Cannot enable; DHCP (v4) is 
enabled 
You tried enabling DHCPv6 while 
DHCPv4 is enabled. 
Disable DHCPv4. 
Cannot set; Router Interface is 
loopback interface 
You tried enabling DHCPv6 client 
while router interface is defined as 
loopback interface. 
Associate DHCPv6 client with a 
router interface that is not defined 
as a loopback interface. 
Cannot activate; must be bound to 
port 
You tried activating a router 
interface, which is neither a 
loopback interface nor bound to a 
port. 
Bind the router interface to a 
loopback interface or a port. 
Cannot activate; bound port in use 
by another router interface 
You tried activating the router 
interface, while the bound port is 
already in use by another router 
interface. 
 
Cannot activate; bound port+vlan 
in use by another router interface 
You tried activating the router 
interface that is bound to port + 
vlan, while bound pair port+vlan is 
already in use by another router 
interface. 
 
Cannot activate; ip address is set 
You tried activating the router 
interface bound to PPP port, when 
IP address was set. 
 

## 7.10 Routing Protocol BGP  *(p.531)*

7. Traffic Processing 
Message 
Cause 
Corrective Action 
Cannot activate; dhcp is enable  
You tried activating the router 
interface bound to PPP port, when 
DHCP is enabled. 
 
Address is not IPv4 address. 
You configured the IP address of 
Inside IP station with a non-IPv4 
address. 
Configure the IP address of Inside 
IP station with an IPv4 address. 
Too many crypto maps associated 
with the interface 
You tried associating more than 
five crypto maps with the router 
interface. 
Disassociate at least one crypto 
map from the router interface. 
There are no IP monitoring entities 
in use 
No IP monitoring entities have 
been configured in the device 
 
Cannot set – port is in use as 
ingress port in sd-iot module 
Bind is allowed only when port is 
not in use as ingress-port in sd-iot 
module (see Configuring SD IoT).  
 
Only one of DHCPv6 server, client 
or relay can be configured 
DHCPv6 client, server and relay are 
mutually exclusive on the same 
router interface.  
 
DHCP client cannot be configured if 
relay is configured 
DHCP client and relay are mutually 
exclusive on the same router 
interface.  
 
 
7.10 Routing Protocol BGP 
BGP (Border Gateway Protocol) is a path-vector protocol for dynamic routing, used for route distribution 
between Autonomous Systems (AS) across the internet and other large networks.   
Applicability and Scaling 
This feature is applicable to all the device versions. 
Standards Compliance 
RFC 4271 - A Border Gateway Protocol 4 (BGP-4)  
7. Traffic Processing 
RFC 4893 - BGP Support for Four-octet AS Number Space 
RFC 5396 - Textual Representation of Autonomous System (AS) Numbers  
RFC 2385 - Protection of BGP Sessions via the TCP MD5 Signature Option   
RFC 2545 - Use of BGP-4 Multiprotocol Extensions for IPv6 Inter-Domain Routing  
The following BGP features are not supported:  
• 
Graceful restart (RFC 4724) 
• 
Interaction with ECMP 
Benefits 
Dynamic routing protocols enable routing tables to automatically adapt to changing networks. BGP is 
the de-facto standard in the internet for communicating routing information between Autonomous 
Systems (AS), making it the only option for AS boundary routers (ASBR) to enable route communication 
with other ASes.  
Functional Description 
BGP is intended for use on customer-premises equipment (CPE) at the boundary of a large customer 
network that is an independent ‘stub’ AS connected to only one other AS (the service provider network).  
BGP functionality is explained in the following sections. 
Dynamic Routing Protocols 
Routers direct packets through their various interfaces according to their routing tables, which specify 
an exit interface for each destination IP network. While routing tables can include static, manually 
configured routes, an optimized routing table requires knowledge of remote network topology and 
complex path calculations. Dynamic routing protocols define how routers communicate network 
topology with each other and how they accordingly calculate optimized network paths and create their 
routing tables. 
The internet is divided into Autonomous Systems (AS). An AS is usually the network of an Internet 
Service Provider (ISP) or another large organization that administers the AS-internal routing policy. 
Routing information inside each AS is communicated and determined by an Interior Gateway Protocol 
7. Traffic Processing 
(IGP) such as OSPF; routing information between ASes is communicated by the Border Gateway Protocol 
(BGP). 
BGP: Path-Vector Routing 
BGP is a path-vector routing protocol. As opposed to link-state protocols, in which network topology is 
communicated throughout a network, and as opposed to distance-vector protocols, in which routers 
communicate destination distances, routers using a path-vector protocol communicate actual paths, or 
routes, to destinations. 
In BGP, communicated paths for each destination contain the IP address of the first hop, and the list of 
ASes, by AS numbers (ASN), which need to be traversed to reach the destination. BGP aggregates routes, 
and, to prevent loops and to choose among the path alternatives, each BGP router decides which actual 
routes to adopt among BGP updates received from its neighbors and which of its known routes to 
advertise to its neighbors. BGP makes these decisions using optimization algorithms and (in other BGP 
implementations) additional criteria from a locally configurable policy. 
BGP Neighbors  
BGP is configured only on AS Boundary Routers (ASBR). Each BGP router recognizes a limited list of BGP 
neighbors from which it receives route updates and to which it advertises route updates. A BGP 
neighbor relationship needs to be manually defined on both BGP routers. BGP routers identify neighbors 
by their IP addresses and AS numbers. 
BGP neighbors always belong to the IPv4 unicast address family, and can optionally belong to the IPv6 
unicast address family. 
AS-Internal Destination Injection 
To be able to advertise its local AS-internal destinations to the rest of the internet, BGP needs to know 
what destination networks are included in its local AS. BGP can become aware of these networks in 
several configurable ways: 
• 
BGP can be configured to redistribute static routes from the router’s routing table. 
• 
BGP can be configured to redistribute connected networks. 
• 
BGP can be configured to redistribute routes from the AS’ IGP (OSPF). Supported only for IPv4 
address family. 
• 
Specified network addresses can be manually configured in BGP. These destinations are 
advertised only if they are found in the local routing table. 
7. Traffic Processing 
AS Numbers (ASN) 
BGP communicates paths as a list of numbers of the ASes that need to be traversed to reach 
destinations. Generally, ASNs uniquely define the AS, and are allocated for the individual AS by the 
Internet Assigned Numbers Authority (IANA); however, ISPs can define private ASes for their customer 
networks with ASNs in the range 64512–65534. 
Limiting Received Routes 
The number of routes received can be limited for each neighbor. When the number of received routes 
reaches 90% of the configured value, the device generates an alarm and sends an SNMP trap. When the 
configured value is exceeded, the session goes down for five minutes. 
BGP Session Timers 
BGP neighbors send each other keep-alive messages to confirm the connection’s health. Two 
parameters are defined: 
keepalive is the interval, in seconds, between messages confirming connection health to the neighbor. If 
the value is 0, these messages are disabled. 
holdtime is the interval, in seconds, after which the connection with the neighbor is considered down if 
no keep-alive messages have been received from the neighbor. If the value is 0, the neighbor is never 
considered down. 
Upon session initiation, the neighbors negotiate for each of these two parameters and then both use the 
lower of their values. Negotiated values can be viewed (see Viewing Neighbor Connection Status). 
Either both parameters must be non-zero or both must be zero. 
Routing Preferences 
When there are conflicts between routes received from different sources, such as static routes, 
connected networks, and BGP routes, the router’s Routing Table Manager (RTM) chooses among the 
sources according to configurable source preference indices (lowest number indicates highest priority). 
Separate preference indices are defined for BGP routes received from BGP neighbors in the same AS 
(Internal BGP) and for BGP routes received from BGP neighbors in other ASes (External BGP). 
7. Traffic Processing 
BGP Path Attributes 
Path attributes are contained in BGP update packets. The path attributes of advertised routes are used 
to select the route from multiple routes, and to propagate policy. 
BGP path attributes have the following types: 
Well-known mandatory 
Must be supported and propagated 
Well-known discretionary 
Must be supported; propagation optional 
Optional transitive 
Marked as partial if unsupported by neighbor 
Optional nontransitive 
Deleted if unsupported by neighbor 
The following table lists the path attributes. 
Name  
Description  
Path Type 
1 Origin  
Origin type (IGP, EGP, or unknown)  
Well-known mandatory 
2 AS Path  
List of autonomous systems which 
the advertisement has traversed  
Well-known mandatory 
3 Next Hop  
External peer in neighboring AS  
Well-known mandatory 
5 Local Preference  
Metric for internal neighbors to 
reach external destinations (default 
100)  
Well-known discretionary 
8 Community  
Route tag 
Well-known discretionary 
4 Multiple Exit Discriminator (MED)  Metric for external neighbors to 
reach the local AS (default 0) 
Optional nontransitive 
BGP Policies 
The BGP functionality provides a flexible filtering mechanism to ensure that the router processes only 
relevant BGP update packets. The filtering is done by means of defining BGP policy profiles of the 
following types: 
Prefix lists 
Filter by prefix and prefix length, where prefix is specified by IP 
address and mask, with prefix length between 24 and 26 
Route maps 
Permit/deny if packet matches community in the form x:y. The 
community is a BGP path attribute (see BGP Path Attributes) that is 
usually set by each network. 
7. Traffic Processing 
BGP policy profiles are assigned per IPv4/IPv6 unicast address family per neighbor. One of each policy 
profile type can be assigned in the inbound direction (to be applied to received packets) and outbound 
direction (to be applied to advertised packets), per IPv4/IPv6 unicast address family per neighbor. 
BGP policy profiles comprise sequentially numbered rules, each of which can be one of the following: 
Permit action 
Specifies criteria for permitting packet, and optionally sets action in 
case of route map profile 
Deny action 
Specifies criteria for dropping a packet 
Remark 
Used for commenting and visually organizing rules 
If there is a need to add a rule between already existing rules with consecutive sequence numbers, the 
rules can be interspaced to accommodate additional rules between them. 
• 
The packet filtering is done as follows: Each BGP update packet is checked according to the 
associated prefix list policy (if exists), and then the associated route map policy (if exists), 
starting with the first rule.  
• 
If the packet doesn’t match a rule, the next rule according to the sequence number is checked.  
• 
If the packet matches a deny rule, it is dropped, and the filtering ends. 
• 
If the packet matches a permit rule, the packet is permitted. Any set operation in the rule is 
performed, in the case of route map profile. 
• 
If the packet doesn’t match any rule, it is dropped. 
Maintained Information 
BGP maintains the following network information, all of which can be viewed (see Viewing BGP Status): 
• 
Neighbor connectivity details 
• 
Per-neighbor received routes 
• 
Per-neighbor advertised routes 
• 
Per-neighbor policy profiles 
• 
Per-neighbor communities 
• 
Per-neighbor RIB 
• 
Per neighbor summary 
7. Traffic Processing 
Factory Defaults 
By default, BGP is not configured on RAD routers. The following tables show the default values when it is 
configured. 
Router  
The following parameters determine BGP behavior for the whole router, for all interfaces: 
Parameter 
Description 
Default Value 
bgp 
Whether BGP is defined (but not 
necessarily enabled) on this router, 
and the local ASN 
no bgp 
router-id 
ID for router in BGP 
communications, in IP address 
format  
-- 
(mandatory configuration) 
shutdown 
Enable (no shutdown) / disable 
(shutdown) BGP on the router 
shutdown 
IPv4 and IPv6 Unicast Address Family 
The following parameters characterize behavior for the IPv4/IPv6 unicast address families, for all BGP 
neighbors. The parameters for IPv4 and IPv6 have the same names but are defined in separate levels. 
Parameter 
Description 
Default Value 
external-preference 
Preference index for external BGP 
routes. See Routing Preferences. 
20 
internal-preference 
Preference index for internal BGP 
routes. See Routing Preferences. 
200 
network 
AS-internal networks that should 
be advertised to BGP neighbors. 
See AS-Internal Destination 
Injection. 
no network 
redistribute 
Sources other than BGP of routes 
that should be advertised to BGP 
neighbors. See AS-Internal 
Destination Injection.  
no redistribute 
7. Traffic Processing 
Neighbor  
The following parameters determine BGP behavior per neighbor: 
Parameter 
Description 
Default Value 
active 
Whether IPv6 is enabled (active) or disabled (no 
active) for the neighbor 
no active 
local-address 
The local IP address from which to advertise BGP 
updates to the neighbor 
-- 
(Uses closest interface to neighbor) 
max-prefixes 
The maximum number of destination networks 
to receive from the neighbor 
0 
(=no limit) 
password 
Secret key for authentication of and to the 
neighbor 
no password 
remote-as 
The neighbor’s ASN 
-- 
(mandatory configuration) 
shutdown 
Whether the neighbor is administratively enabled 
(no shutdown) or disabled (shutdown) for  
shutdown 
keepalive 
Interval, in seconds, between messages 
confirming connection health to the neighbor 
30 
holdtime 
Interval, in seconds, after which the connection 
with the neighbor is considered down if no 
keepalive messages have been received from the 
neighbor 
90 
Configuring BGP 
You can configure BGP on a RAD router that is at the boundary of an AS, after the router itself has been 
properly configured. To configure BGP properly, you need to know your network BGP design, including 
the router’s IP address and ASN, designated BGP neighbors’ IP addresses and ASNs, whether IPv6 is 
required, and the desired method of passing AS-internal destinations to BGP. 
When multiple VPN routers are configured on a device, each router should be configured with its own 
instance of BGP. All of these BGP instances must share the same ASN. 
BGP parameters are configured at the following levels: 
• 
Configuring BGP at Router Level: Parameters that determine BGP behavior for the whole 
router, for all IP families and neighbors 
7. Traffic Processing 
• 
Configuring BGP Neighbors: Per-neighbor parameters 
• 
Configuring IPv4/IPv6 Unicast Address Families: Parameters that characterize BGP behavior for 
IPv4/IPv6 unicast address families. 
Follow these steps to configure BGP: 
1. Define the BGP router IP address and ASN (see Configuring BGP at Router Level). 
2. Administratively enable BGP. 
3. Define any necessary BGP neighbors, along with the remote AS to which the neighbor belongs (see 
Configuring BGP Neighbors). 
4. Administratively enable the BGP neighbors. 
5. If it is necessary for BGP to be aware of AS-internal destinations that need to be advertised, 
configure redistribution (of OSPF routes, static routes, and/or connected networks) or explicit 
networks, for IPv4 and IPV6 unicast address families (see Configuring IPv4/IPv6 Unicast Address 
Families). 
6. For each BGP neighbor, if network design requires any non-default values for IPv4 and IPV6 
unicast address families, configure the parameters (see Configuring Neighbor Parameters). 
Configuring BGP at Router Level 
 To configure BGP: 
1. At the config>router(<number>)# prompt, type: 
bgp <ASN> 
The config>router(<number>)>bgp(<ASN>)# prompt is displayed. 
 
Note 
• 
<ASN> is the number of the local AS where the router is located 
• 
Type no bgp <ASN> to remove BGP from the router (if no neighbors are 
defined). 
 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Enabling BGP on the router 
[no] bgp <ASN> 
<ASN> is the number of the local 
AS where the router is located. 
7. Traffic Processing 
Task 
Command 
Comments 
Restarting a BGP session with 
neighbor and reloading BGP 
policy profiles 
clear-neighbor <IP-address> 
[soft] 
 
<IP-address> is the neighbor’s IP 
address (IPv4 or IPv6). 
If you specify soft, the link with 
the neighbor is not reset, but 
the BGP policy profiles are 
reloaded. 
Configuring BGP parameters for 
IPv4 or IPv6 unicast address 
family 
ipv4-unicast-af 
ipv6-unicast-af 
See Configuring IPv4/IPv6 
Unicast Address Families. 
Configuring BGP neighbor 
neighbor <IP-address> 
<IP-address> is the neighbor’s IP 
address (IPv4 or IPv6). See 
Configuring BGP Neighbors. 
no neighbor <IP-address> 
removes the neighbor from BGP 
configuration. 
Defining IP address for the 
router in BGP communications 
router-id <IP-address> 
 
To simplify management, the IP 
address can be the actual IP 
address of one of the router’s 
interfaces, or there may be 
some other organizational 
convention. 
Defining or changing the router 
IP address requires BGP to be 
administratively disabled 
(shutdown). 
Displaying the IPv4 or IPv6 
community table 
show community { ipv4 | ipv6 } 
See Viewing BGP Communities. 
Displaying the IPv4 or IPv6 RIB 
(Routing Information Base) table 
show rib { ipv4 | ipv6 } 
See Viewing BGP RIB. 
Displaying summary of neighbor 
connections information 
show summary 
See Viewing BGP Summary. 
Administratively enabling or 
disabling BGP on the router 
[no] shutdown 
To disable: shutdown; to 
enable: no shutdown 
When BGP is disabled, 
operational status of BGP 
neighbors moves down. 
 
7. Traffic Processing 
Configuring BGP Neighbors 
You can define BGP neighbors to represent neighboring routers from which the BGP router entity 
receives route updates and to which it advertises route updates. 
 To configure BGP neighbors: 
1. At the config>router(<number>)>bgp(<ASN>)# prompt, type: 
neighbor <IP-address> 
The config>router(<number>)>bgp(<ASN>)> neighbor(<IP-address>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Defining the local IP address from 
which to advertise BGP updates to 
the neighbor 
[no] local-address [<IP-address>] 
local-address <IP-address> sets a 
parameter value; no local-address 
clears the parameter. When no 
local address is set (default), BGP 
uses the closest interface to the 
neighbor. 
The change takes effect only after 
clear-neighbor or shutdown. 
Setting the maximum number of 
routes to accept from the neighbor 
max-prefixes <prefixes> 
<prefixes> is a number in range: 
0–2147483647. 0 means no limit. 
See Limiting Received Routes. 
Change takes effect only after 
clear-neighbor or shutdown. 
Setting password for neighbor 
session 
[no] password <password> [hash] 
The <password> can be up to 80 
characters. 
hash specifies that the password 
should be encrypted. 
no password deletes the password. 
Change takes effect only after 
clear-neighbor or shutdown. 
Defining neighbor’s ASN 
remote-as <ASN> 
Available only when 
communication with the neighbor 
is disabled (shutdown). 
7. Traffic Processing 
Task 
Command 
Comments 
Setting keepalive and holdtime 
timers 
timers <keepalive> <holdtime> 
See BGP Session Timers 
Change takes effect only after 
clear-neighbor or shutdown. 
Viewing connectivity details 
show neighbor-connection 
See Viewing Neighbor Connection 
Status 
Enabling or disabling BGP 
communication with the neighbor 
[no] shutdown 
To enable: no shutdown (requires 
remote-as to have been 
configured) 
To disable: shutdown . 
 
Configuring IPv4/IPv6 Unicast Address Families 
The parameters for IPv4/IPv6 unicast address families are configured in the levels configure router 
<number> bgp <ASN> ipv4-unicast-af and configure router <number> bgp <ASN> ipv6-unicast-af, 
respectively. You can configure general parameters for the unicast address families, or neighbor 
parameters. 
Configuring Unicast Address Family Parameters 
 To configure IPv4/IPv6 unicast address families: 
1. At the config>router(<number>)>bgp(<ASN>)# prompt, type one of the following, according to 
whether you wish to configure BGP parameters for IPv4 or IPv6 unicast address families: 
 
ipv4-unicast-af 
 
ipv6-unicast-af 
The prompt config>router(<number>)>bgp(<ASN>)>ipv4-unicast-af# or 
config>router(<number>)>bgp (<ASN>)>ipv6-unicast-af# is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Defining the preference index 
for external BGP routes 
external-preference 
<priority> 
<priority> should be an integer in range 1–255.  
7. Traffic Processing 
Task 
Command 
Comments 
Defining the preference index 
for internal BGP routes 
internal-preference 
<priority> 
Note: the value of 255 is considered as 
unreachable and the appropriate route is not be 
added to the routing table. 
See Routing Preferences. 
Note: Priority can be changed at any time; the 
change takes effect only after 
clear-neighborclear-neighborclear-neighborclea
r-neighbor or shutdown. 
Specifying a neighbor router 
neighbor <IP-address> 
See Configuring Neighbor Parameters. 
Defining an explicit network 
that should be advertised to 
BGP neighbors as a 
destination in this AS 
network 
<IP-address>/<netmask> 
<IP-address> is the network’s IP address, and 
<netmask> is the length of the network part 
(CIDR notation). 
Each added network requires a separate 
command. 
To delete the network entity: no network 
<IP-address>/<netmask See AS-Internal 
Destination Injection. 
Defining non-BGP sources of 
routes that should be 
advertised to BGP neighbors 
[no] redistribute 
{connected  |  static | ospf} 
 
To disable distribution: no redistribute { 
connected | static | ospf}. 
Each source protocol (connected, static, ospf) 
requires a separate command. 
For IPv6, only the connected and static options 
are supported. 
See AS-Internal Destination Injection. 
Configuring Neighbor Parameters  
 To configure BGP neighbor parameters under IPv4/IPv6 unicast address families: 
1. At the prompt config>router(<number>)>bgp(<ASN>)> ipv4-unicast-af# or 
config>router(<number>)>bgp(<ASN>)> ipv6-unicast-af#, type: 
neighbor <IP-address> 
The prompt config>router(<number>)>bgp(<ASN>)>ipv4-unicast-af> 
neighbor(<IP-address>)# or config>router(<number>)>bgp(<ASN>)> 
ipv6-unicast-af neighbor>(<IP-address>)# is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
7. Traffic Processing 
Task 
Command 
Comments 
Enabling or disabling IPv4 or IPv6 
BGP for the neighbor 
[no] active 
Enable – active 
Disable – no active  
You cannot type no active for IPv4, 
as the address family IPv4 unicast is 
always enabled for all neighbors. 
Associating prefix list BGP policy 
with the neighbor unicast address 
family for incoming or outgoing 
direction 
prefix-list-bind <name> {in | out} 
Type no before the command to 
remove the association with the 
prefix list. 
Associating route map BGP policy 
to the neighbor unicast address 
family for incoming or outgoing 
direction 
route-map-bind <name>{in | out} 
Type no before the command to 
remove the association with the 
route map. 
Viewing routes advertised to the 
neighbor 
show advertised-route 
See Viewing Advertised Routes. 
Displaying any associated prefix list 
policy profiles and rules related to 
a BGP neighbor per AF 
show prefix-list 
See Viewing BGP Policy Profiles. 
Viewing routes received from the 
neighbor 
show received-route 
See Viewing Received Routes. 
Displaying any associated route 
map policy profiles and rules 
related to a BGP neighbor per AF 
show route-map 
See Viewing BGP Policy Profiles. 
 
Configuring BGP Policy Profiles 
BGP policy profiles are configured at the router level. They can be prefix list or route map policy profiles 
(see BGP Policies for more information). After changing a policy profile, you should use the command 
clear-neighbor with the soft parameter, to ensure that the change is applied to the neighbor BGP 
policies. 
 To configure BGP policy profiles: 
1. Navigate to configure router <number>. 
2. Enter the necessary commands according to the table below. 
7. Traffic Processing 
3. See Configuring Prefix List Rules or Configuring Route Map Rules respectively, for commands to 
configure the rules in a prefix list policy profile or route map policy profile. 
 
Task 
Command 
Comments 
Configuring prefix list 
policy profile, for 
IPv4/IPv6 
prefix-list <name> {ipv4 | ipv6} 
 
Type no prefix-list <name> to 
delete the prefix list. 
Configuring route map 
policy profile 
route-map <name> 
Type no before the command to 
delete the route map. 
Resequencing the rules in 
a policy profile 
resequence <name> [<number>] 
This command can be used when 
you need to insert rules in the 
middle of a policy profile. 
<name> – name of the policy 
profile  
<number> – steps to insert 
between the rule sequence 
numbers. For instance, if you 
specify 10, the rule sequence 
numbers are changed to 10, 20, 30, 
etc. 
Range for <number>: 1–100000. 
Configuring Prefix List Rules 
 To configure the rules in a prefix list policy profile: 
1. Navigate to configure router prefix-list <name> {ipv4 | ipv6}. 
2. Enter the necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Removing a rule 
delete <sequence> 
<sequence> – sequence number of 
the rule to delete 
7. Traffic Processing 
Task 
Command 
Comments 
Adding a deny rule 
deny <prefix>/<length> 
[ge <ge-value>] [le <le-value>] 
[sequence <sequence>] 
• <prefix>/<length> – prefix and 
length identifying the network 
that this rule matches, in the 
following form according to 
IPv4 or IPv6: 
(IPv4) <IPv4 address>/<1–32> 
(IPv6) <IPv6 address>/<1–128> 
• ge – Rule matches packets with 
prefix length greater than or 
equal to <ge-value>. 
• le – Rule matches packets with 
prefix length less than or equal 
to <le-value>. 
• sequence – assigns <sequence> 
as the sequence number of the 
rule. Sequence number range: 
1–2147483648 
The ge and le parameters are 
validated as follows: 
• (IPv4) Prefix length <ge < le <= 
32  
• (IPv6) Prefix length <ge < le <= 
128 
Adding a permit rule 
permit <prefix>/<length> 
[ge <ge-value>] [le <le-value>] 
[sequence <sequence>] 
For an explanation of the 
parameters, see the comments 
above for the deny rule. 
Adding a remark 
remark [<description>] [sequence 
<sequence>] 
The description can contain up to 
252 characters. 
 
Configuring Route Map Rules 
 To configure the rules in a route map policy profile: 
1. Navigate to configure router route-map <name>. 
2. Enter the necessary commands according to the tasks listed below. 
7. Traffic Processing 
Task 
Command 
Comments 
Removing a 
rule 
delete <sequence> 
<sequence> – sequence number of the rule to delete 
Adding a deny 
rule 
deny [match [as-path 
string] [community string] 
[ prefix-list string] 
][sequence sequence>] 
 
as-path – BGP AS Path that this rule uses to match to a 
route in ASCII format; in regular expression format 
(permitted length 0–127 characters). 
Note: AS numbers are matched as decimal numbers. For 
example, the AS number '0x0123' should be represented 
in the regular expression string as '291'. A NULL string 
indicates that the field is not in use. 
community – BGP community that this rule matches, in 
the form aa:nn  (permitted length 0–127 characters). If 
community is not specified, this rule matches all packets. 
Note: Community has the new-format decimal notation. 
For example, the community '0x00120101' should be 
represented in the string as '18:257'. 
prefix-list - BGP policy prefix-list profile name that this 
rule matches; permitted length 0–80 characters 
sequence – Assigns <sequence> as the sequence number 
of the rule.  
Sequence number range: 1–2147483648  
Adding a 
permit rule, 
and optionally 
specifying set 
actions 
permit[match [as-path 
string] [community string] 
[ prefix-list string] ][set 
[as2-path-prepend string] 
[as4-path-prepend string] 
[community string] [local-
preference number] [med 
number] ][sequence 
sequence>] 
as-path – BGP AS Path that this rule uses to match to a 
route in ASCII format; in regular expression format 
(permitted length 0–127 characters). 
Note: AS numbers are matched as decimal numbers. For 
example, the AS number '0x0123' should be represented 
in the regular expression string as '291'. A NULL string 
indicates that the field is not in use. 
community – BGP community that this rule matches, in 
the form aa:nn (permitted length 0–127 characters). If 
community is not specified, this rule matches all packets.  
Note: Community has the new-format decimal notation. 
For example, the community '0x00120101' should be 
represented in the string as '18:257'. 
prefix-list - BGP policy prefix-list profile name that this 
rule matches; permitted length 0–80 characters 
set – Specify set actions for BGP path attributes (see BGP 
Path Attributes). 
7. Traffic Processing 
Task 
Command 
Comments 
as2-path-prepend/as4-path-prepend – Set AS prepend 
(for 2/4 octets AS size) to <string>; permitted length 0–
127 characters 
Note: You can define only one as-path-prepend 
statement - as2-path-prepend or as4-path-prepend. 
community – Set community to a string in the form 
aa:nn (permitted length 0–127 characters.  
local-preference – Set local preference to <number>.  
Possible values: 0–4294967295 
med – Set Multiple Exit Discriminator (MED) to 
<number>.  
Possible values: 0–4294967295 
sequence – Assigns <sequence> as the sequence number 
of the rule.  
Sequence number range: 
1–2147483648 
Adding a 
remark 
remark [<description>] 
[sequence <sequence>] 
The description can contain up to 255 characters. 
 
Examples 
This section illustrates configuring BGP policy profiles. 
 To configure prefix list (IPv4): 
• 
BGP AS =  65530 
• 
Neighbor IP address = 120.120.120.120 
• 
Permit routes with prefix 100.102.0.0/11, and prefix length 24–26 
exit all 
#****** Configure the prefix list 
configure router 1 
  prefix-list subnetsIN ipv4 
    permit 100.102.0.0/11 ge 24 le 26 sequence 10 
    remark "permit 100.102.0.0/11 with prefix length 24 to 26" sequence 10000 
  exit  
 
#****** Bind the prefix list  
  bgp 65530 ipv4-unicast-af neighbor 120.120.120.120 
    prefix-list-bind subnetsIN in 
  exit all 
 
7. Traffic Processing 
#****** Reload BGP policy profiles for the neighbor 
configure router 1 bgp 65530 
  clear-neighbor 120.120.120.120 soft 
  save 
 To configure prefix list (IPv6): 
• 
BGP AS =  65530 
• 
Neighbor IP address = 78:78:78::78 
• 
Permit routes with prefix 123a:bbb1::/28 and prefix length 50–66 
exit all 
#****** Configure the prefix list 
configure router 1 
  prefix-list subnetsIN ipv6 
    permit 123a:bbb1::/28 ge 50 le 66 sequence 10 
    remark "permit 123a:bbb1::/28 with prefix length 50 to 66" sequence 10000   
  exit  
 
#****** Bind the prefix list 
  bgp 65530 ipv6-unicast-af neighbor 78:78:78::78 
    prefix-list-bind subnetsIN in 
  exit all 
 
#****** Reload BGP policy profiles for the neighbor 
configure router 1 bgp 65530 
  clear-neighbor 78:78:78::78 soft 
save 
 To configure route map (IPv4): 
• 
BGP AS =  65530 
• 
Neighbor IP address = 120.120.120.120 
• 
Deny subnets with community 1:10 
exit all 
#****** Configure the route map 
configure router 1 
  route-map commIN 
    deny match community 1:10 sequence 10 
    remark "deny subnets with community 1:10" sequence 10000 
  exit  
 
#****** Bind the route map 
  bgp 65530 ipv4-unicast-af neighbor 120.120.120.120 
    route-map-bind commIN in 
  exit all 
 
7. Traffic Processing 
#****** Reload BGP policy profiles for the neighbor 
configure router 1 bgp 65530 
  clear-neighbor 120.120.120.120 soft 
  save 
 To configure route map (IPv6): 
• 
BGP AS =  65530 
• 
Neighbor IP address = 78:78:78::78 
• 
Permit subnets with community 1:10 
exit all 
#****** Configure the route map 
configure router 1 
  route-map commIN 
    permit match community 1:10 sequence 10 
    remark "permit subnets with community 1:10" sequence 10000 
  exit  
 
#****** Bind the route map 
  bgp 65530 ipv6-unicast-af neighbor 78:78:78::78 
    route-map-bind commIN in 
  exit all 
 
#****** Reload BGP policy profiles for the neighbor 
configure router 1 bgp 65530 
  clear-neighbor 78:78:78::78 soft 
  save 
Example 
In this example, a customer-premises RAD device has been placed at the boundary of an organization’s 
network, which is an independent AS. The RAD device needs to be configured for BGP. 
The only BGP neighbor is the Provider Edge (PE) router. Since this is a stub AS, it has been decided that 
AS-internal destinations should be aggregated and manually defined (with the network command) 
rather than enabling automatic redistribution. IPv6 is required for this network. 
 
Device 
IP 
ASN 
CPE ASBR (the device being 
configured for BGP) 
10.10.1.1 
64515 
PE (BGP neighbor) 
10.10.10.1 
613 
7. Traffic Processing 
The configuration process for this example is: 
#***** Configure BGP on router 
configure router 1 
    bgp 64515 
      router-id 10.10.1.1 
      no shutdown 
#***** define AS-internal networks for advertisement 
      ipv4-unicast-af 
        network 10.10.1.0/24 
      exit 
      ipv6-unicast-af 
        network fc00:1234:a1b1:0000:0000:0000:0000:0000/48 
      exit 
#***** configure neighbor 
      neighbor 10.10.10.1 
        remote-as 613 
        no shutdown 
      exit all 
save 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Cannot delete; BGP neighbor exist 
You tried to run no bgp, but there 
are configured BGP neighbors. 
Delete all neighbors and try again. 
Cannot create; AS number must be 
equal for all BGP entities 
You tried to define BGP with an 
ASN different from the BGP ASN 
configured for another router on 
this device. 
Use the same ASN for BGP on all 
the device’s routers. 
Cannot clear; unknown neighbor 
You tried to run clear-neighbor on 
an IP address that is not configured 
for any defined BGP neighbor. 
Use the correct IP address 
configured for the neighbor. 
Cannot set; AS number change 
requires deletion of all BGP entities 
You tried changing the BGP ASN 
before deleting all BGP entities. 
Delete all BGP entities, and then 
change the ASN. 
Cannot set; change requires bgp 
shutdown 
You tried to set the router-id with 
BGP running. 
Run shutdown and then try again. 
Cannot activate; router-id number 
must be set 
You tried to enable BGP (no 
shutdown) without having set the 
router-id. 
Set the router-id and try again. 
7. Traffic Processing 
Message 
Cause 
Corrective Action 
Cannot set; No such neighbor 
You tried to enter an IP / neighbor 
context, but you specified an IP 
address that is not configured for 
any neighbor. 
Use the correct IP address 
configured for the neighbor. 
Cannot set; ipv4 unicast address 
family always enable 
You tried using the active 
command in the IPv4 neighbor CLI 
context. 
IPv4 cannot be disabled for any 
neighbors. If you meant to enable 
or disable IPv6, navigate to 
config>router(<number>)>bgp(<AS
N>)>ipv6-unicast-af>neighbor(<IP-
address>)# and try again. 
Cannot activate; remote IP address 
and AS number must be set 
You tried to run no shutdown for a 
BGP neighbor, but this neighbor 
does not yet have an ASN. 
Set the neighbor’s ASN (with the 
remote-as command) and then try 
again. 
Cannot set; Hold time should be 
greater than the keepalive time 
You tried to run the timers 
command with hold time less than 
or equal to keepalive time. 
Run the command again with hold 
time greater than keepalive time.  
Cannot bind; policy profile type 
does not match 
You tried to bind a policy profile 
that does not match the required 
policy type (prefix-list-ipv4 or 
prefix-list-ipv6).  
Change policy type to prefix-list-
ipv4 or prefix-list-ipv6). 
Cannot bind; prefix-list profile 
already in use in match statement 
You tried to bind prefix-list profile 
when route-map profile with 
‘match prefix-list’ statement is 
already bound to the same BGP 
connection.  
Unbind route-map profile with 
‘match prefix-list’ statement from 
the BGP connection. 
Cannot bind; no such policy profile 
You tried to bind a policy profile 
that does not exist. 
Create the policy profile that you 
want to bind. 
Cannot bind; policy profile type 
does not match 
You tried to bind a policy profile 
that does not match the required 
type (route-map) 
Bind the policy profile to route-
map. 
Cannot bind; address-family 
mismatch with match statement 
You tried to bind a route-map 
profile with ‘match prefix-list’ 
statement with a prefix-list 
address-family that is not identical 
to bound connection address-
family. 
Create a prefix-list address-family 
that is identical to bound 
connection address-family. 
7. Traffic Processing 
Message 
Cause 
Corrective Action 
Cannot bind; prefix-list profile 
already bound 
You tried to bind a route-map 
profile with ‘match prefix-list’ 
statement when prefix-list profile is 
bound to the same BGP 
connection. 
Unbind prefix-list profile from the 
BGP connection. 
Cannot delete; prefix list is 
matched in a route-map 
You tried to delete a prefix –list 
that is matched in a route-map. 
Unbind the policy profile from all 
entities bound to it.  
Cannot create; name already in use 
You tried creating a prefix-list 
policy profile with a name that 
already exists in the system. 
Choose a unique name for the 
newly created prefix-list policy 
profile. 
Cannot add statement; wrong 
prefix address type 
You tried adding a rule with an 
address type (ipv4 or ipv6) that is 
not related to the profile type. 
Use the appropriate address type. 
Cannot add statement; wrong 
length parameters 
You tried adding a rule with 
incorrect length parameters.  
Correct the length parameters so 
that length < ge-value <= le-value 
<= address length of family (32 or 
128). 
Cannot add statement; regular 
expression is incorrect 
The regular expression that you 
entered does not translate into a 
valid AS path.  
Enter a new regular expression for 
the AS path. 
Cannot add statement; no such 
policy profile 
You tried adding a statement with 
a prefix-list profile that does not 
exist. 
Create the prefix-list profile or use 
an existing prefix-list profile. 
Cannot add statement; prefix-list 
address-family mismatch 
You tried adding a statement with 
a prefix-list profile address-family 
that is different than similar 
previous statements. 
Use a prefix-list profile address-
family that is similar to previous 
statements. 
Cannot add statement; the route-
map is bound to bgp connection 
with bound prefix-list 
You tried adding a statement, but 
the route-map profile (with the 
new ‘match prefix-list’ statement) 
is bound to a connection with a 
bound prefix-list profile. 
Unbind the route map from the 
bgp connection. 
Warning: prefix list profile contains 
permit statement 
You used a prefix-list profile that 
contains at least one “permit” 
statement. 
Use another prefix-list profile or 
remove all “permit” statements 
from the current prefix-list profile. 
7. Traffic Processing 
Message 
Cause 
Corrective Action 
Set timer to ‘0’ requires holdtime = 
keepalive = 0 
You tried to run the timers 
command with one 0 value. Either 
both or neither must be 0. 
Run the command again with 
either both or neither parameter 
being 0. 
Viewing BGP Status 
You can view the current configuration (see Viewing the Current Configuration), status of the 
connection with each configured neighbor (see Viewing Neighbor Connection Status), and routes 
received from and advertised to each neighbor (see Viewing Received Routes and Viewing Advertised 
Routes). This information can be used for testing (see Testing BGP) and debugging. 
Viewing the Current Configuration 
To view the configuration, use the commands info (to include only non-default configuration) and info 
detail (to include default configuration). 
You can view this info at any of the following configuration levels: 
Level 
Context Prompt 
Router 
config>router(<number>)>bgp(<ASN>)# 
IPv4/IPv6 unicast 
address family 
config>router(<number>)>bgp(<ASN>)>ipv4-unicast-af#  
config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af#  
Neighbor 
config>router(<number>)>bgp(<ASN>)>neighbor(<IP-address>)# 
IPv6 neighbor 
config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af>neighbor(<IP-address>)#  
For example: 
config>router(1)>bgp(64515)# info detail 
    router-id 10.10.1.1 
    no shutdown 
    echo "BGP Neighbor Configuration"# 
#   BGP Neighbor Configuration 
    neighbor 10.10.10.1 
        local-address 0.0.0.0 
        max-prefixes 0 
        password "" hash 
        remote-as 613 
        no shutdown 
        timers keepalive 30 holdtime 90 
        exit 
7. Traffic Processing 
        echo "IPv4 Unicast Address Family Configuration" 
#   IPv4 Unicast Address Family Configuration 
    ipv4-unicast-af 
        external-preference 20 
        internal-preference 200 
        redistribute ospf 
        echo "IPv4 Unicast Address Family - Neighbor Configuration" 
#       IPv4 Unicast Address Family - Neighbor Configuration  
        neighbor 10.10.10.1 
            active 
        exit 
    exit 
    echo "IPv6 Unicast Address Family Configuration" 
#   IPv6 Unicast Address Family Configuration 
    ipv6-unicast-af 
        external-preference 20 
        internal-preference 200 
        echo "IPv6 Unicast Address Family - Neighbor Configuration" 
#       IPv6 Unicast Address Family - Neighbor Configuration 
        neighbor 10.10.10.1 
        no active 
        exit 
    exit 
Viewing Neighbor Connection Status 
You can view connectivity details with any configured BGP neighbor by using the show 
neighbor-connection command. This command is available in the BGP neighbor CLI context: 
config>router(<number>)>bgp(<ASN>)>neighbor(<IP-address>)#. You can use this information for 
troubleshooting and testing.  
For example: 
config>router(1)>bgp(64515)>neighbor(10.10.10.1)# show neighbor-connection 
Remote Host: 10.10.10.1 
Remote Port: 179 
Local Host : 0.0.0.0 
Local Port : 36586 
Remote AS  : 613 
 
BGP State: Active             Up for 12d 06:23:53 
Hold Time (seconds) : 180     Keepalive Interval (seconds): 60 
 
Last Error : None 
 
Neighbor Advertised Capabilities 
--------------------------------------------------------------------------- 
Address Family IPv4 Unicast : Advertised and received 
Address Family IPv6 Unicast : Advertised and received 
Route refresh               : Advertised and received 
7. Traffic Processing 
Graceful Restart            : None 
Four Octet AS               : Received 
Viewing Received Routes 
You can view the database of routes received from a particular neighbor by using the show received-
route command. This command is available in the CLI contexts for IPv4 or IPv6 unicast address families, 
at the neighbor level: config>router(<number>)>bgp(<ASN>)>ipv4-unicast-af>neighbor(<IP-address>)# 
or config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af> 
neighbor(<IP-address>)#. 
To display the received routes for IPv4 unicast address families: 
config>router(1)>bgp(1)>ipv4-unicast-af>neighbor(2.2.2.2)# show received-route 
Network            > Next Hop        MED    LocPrf Path  
================================================================================ 
0.0.0.0/0          > 172.17.171.1    1000   2000   3000 1000 100 2333 
111.222.111.220/30 > 111.222.111.223 65200  65200  4000 800 65500 
 To display the received routes for IPv6 unicast address families: 
config>router(1)>bgp(1)>ipv6-unicast-af>neighbor(1:1:1:1::2)# show received-route 
Network              > Next Hop             MED    LocPrf Path  
================================================================================ 
::/0                 > 11:11:11:11::1       1000   2000   3000 1000 100 2333 
11:11:11:11::/64     > ::                   1000   2000   3000 1000 100 
abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126      
> abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200  65200  4000 80 65500 
The above fields are: 
 
Network 
IPv4 or IPv6 network address (prefix and prefix length) 
IPv4 prefix length can be 0–32; IPv6 prefix length can be 0–128. 
Next Hop 
Neighbor IPv4 or IPv6 address 
MED 
Number of Multi-exit Discriminators (in decimal value) 
Possible values: 0–4294967295 
LocPrf 
Local preference 
Possible values: 0–4294967295 
Path 
AS path details 
7. Traffic Processing 
Viewing Advertised Routes 
You can view the database of routes that are advertised to a particular neighbor by using the show 
advertised-route command. This command is available in the CLI contexts for IPv4 or IPv6 unicast 
address families, at the neighbor level: config>router(<number>)>bgp(<ASN>)>ipv4-unicast-
af>neighbor(<IP-address>)# or config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af> 
neighbor(<IP-address>)#.  
 To display the advertised routes for IPv4 unicast address families: 
config>router(1)>bgp(1)>ipv4-unicast-af>neighbor(1.1.1.1)# show advertised-route 
A = advertised, S = suppressed, E = endingWithdrawal W = withdrawn 
   Network            > Next Hop        MED    LocPrf Path  
================================================================================ 
A  0.0.0.0/0          > 172.17.171.1    1000   2000   3000 1000 100 2333 
A  111.222.111.220/30 > 111.222.111.223 65200  65200  4000 800 65500 
 To display the advertised routes for IPv6 unicast address families: 
config>router(1)>bgp(1)>ipv6-unicast-af>neighbor(1:1:1:1::2)# show advertised-route 
A = advertised, S = suppressed, E = endingWithdrawal W = withdrawn 
   Network              > Next Hop             MED    LocPrf Path  
================================================================================ 
A  ::/0                 > 11:11:11:11::1       1000   2000   3000 1000 100 2333 
S  11:11:11:11::/64     > ::                   1000   2000   3000 1000 100     
A  abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126      
   > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200  65200  4000 80 65500 
The above fields are: 
 
Status 
Status of route 
Possible values are: 
• A – advertised 
• S – suppressed 
• E – endingWithdrawal 
• W – withdrawn 
Neighbor  
IPv4 or IPv6 network address (prefix and prefix length) 
IPv4 prefix length can be 0–32; IPv6 prefix length can be 0–128. 
Next hop 
Neighbor IPv4 or IPv6 address 
MED 
Number of Multi-exit Discriminators (in decimal value) 
Possible values: 0–4294967295 
7. Traffic Processing 
LocPrf 
Local preference 
Possible values: 0–4294967295 
Path 
Network prefix and prefix length 
Value: string with interpretation of two octets or four octets 
Viewing BGP Policy Profiles 
You can view the BGP policy profiles assigned to a particular neighbor by using the command show 
prefix-list or show route-map. These commands are available in the CLI contexts for IPv4 or IPv6 unicast 
address families, at the neighbor level: config>router(<number>)>bgp(<ASN>)>ipv4-unicast-
af>neighbor(<IP-address>)# or config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af> 
neighbor(<IP-address>)#.  
 To display the prefix list policy profiles assigned to the neighbor 1.1.1.1 IPv4 unicast family: 
config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(1.1.1.1)# show prefix-list 
 
Name: aaaaaAAAAAbbbbbBBBBBcccccCCCCCdddddDDDDD (In) 
 10 deny 10.10.10.0/24 (hit count: 2) 
 20 permit 3.3.3.0/24 ge 25 le 27 (hit count: 35) 
Name: XXXX (Out) 
 100000 permit 2.2.2.0/24 10 (hit count: 35) 
 To display the prefix list policy profiles assigned to the neighbor 10:10:10::10 IPv6 unicast family: 
config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10:10:10::10)# show prefix-list 
 
Name: aaaaaAAAAAbbbbbBBBBBcccccCCCCCdddddDDDDD (In) 
 100000 permit 1234:1234:1234:1234:1234:1234:1234:1234/100 ge 110 le 120 
        (hit count: 4294967295) 
Name: XXXX (Out) 
 20 permit 2:2:2::0/64 (hit count: 15) 
 To display the route map policy profiles assigned to the neighbor 1.1.1.1 IPv4 unicast family: 
config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(1.1.1.1)# show route-map 
Name: aaaaaAAAAAbbbbbBBBBBcccccCCCCCdddddDDDDD (In) 
  10 permit (hit count: 0) 
    match  community 1:2 
    set  community 2:3  med 456799  local-pref 123456 
  20 deny (hit count: 2) 
    match community 1000:2000 
Name: XXXX (Out) 
  10 permit (hit count: 10) 
    match community 3000:4000 
7. Traffic Processing 
    set community 1000:2000 local-pref 110  
  20 permit (hit count: 1) 
    match community 100:200 
  40 permit (hit count: 2) 
    match as-path _150$ prefix-list AAAA community 10:20 
    set as2-path-prepend “100 100” community 30:40 
 To display the route map policy profiles assigned to the neighbor 10:10:10::10 IPv6 unicast family: 
config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10:10:10::10)# show route-map 
 
Name: aaaaaAAAAAbbbbbBBBBBcccccCCCCCdddddDDDDD (In) 
  10 permit (hit count: 0) 
    match  community 1:2 
    set  community 2:3  med 456799  local-pref 123456 
  20 deny (hit count: 2) 
    match community 1000:2000 
Name: XXXX (Out) 
  10 permit (hit count: 10) 
    match community 3000:4000 
    set community 1000:2000 local-pref 110  
  20 permit (hit count: 1) 
    match community 100:200 
  40 permit (hit count: 2) 
    match as-path _150$ prefix-list AAAA community 10:20 
    set as2-path-prepend “100 100” community 30:40  
The above fields are: 
 
Name 
Profile name 
(In)/(Out)  
Policy direction: inbound or outbound 
Sequence number 
Policy rule sequence number 
Type 
Policy rule type 
Possible options are: 
• Deny 
• Permit 
Route map rule 
information 
Route-map rule information 
7. Traffic Processing 
Viewing BGP Communities 
You can view the received communities of all neighbors by using the command show community. This 
command is available in the CLI contexts for IPv4 or IPv6, at the BGP level: 
config>router(<number>)>bgp(<ASN>)#.  
 To display the IPv4 BGP communities received by all neighbors: 
config>router(1)>bgp(1)# show community ipv4 
 
Network                Community  
=============================================================== 
Neighbor 2.2.2.2 
 0.0.0.0/0              65000:65000 
 111.222.111.220/30     20:20 
Neighbor 33.33.33.33 
 0.0.0.0/0              1000:2000 
 111.222.111.220/30     100:100 200:200 300:300 400:400 
 To display the IPv6 BGP communities received by all neighbors: 
config>router(1)> bgp(1)# show community ipv6 
 
Network                                      Community 
============================================================================= 
Neighbor 2:2:2:2::2 
 ::/0                 > 11:11:11:11::1       65000:65000 1000:2000 3000:1000 
 11:11:11:11::/64     > ::                   1000:2000 
 abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126 
 > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200:65200 
Neighbor 33:33:33:33::33 
 ::/0                 > 11:11:11:11::1       20:30 
 11:11:11:11::/64     > ::                   400:400 
 abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126 
 > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200:65200 4000:65500 
The above fields are: 
Neighbor  
Neighbor IPv4 or IPv6 address 
Network 
IPv4 or IPv6 network address (prefix and prefix length) 
IPv4 prefix length can be 0–32; IPv6 prefix length can be 0–128. 
Community 
Decimal value, in format xxxx:yyyy 
Possible values: 00000:00000–65535:65535 
7. Traffic Processing 
Viewing BGP RIB 
You can view the BGP RIB (Routing Information Base) for each neighbor by using the command show rib. 
This command is available in the CLI contexts for IPv4 or IPv6, at the BGP level: 
config>router(<number>)>bgp(<ASN>) #.  
 To display the IPv4 BGP RIB: 
config>router(1)>bgp(1)# show rib ipv4 
 
* = Best Route 
   Network            > Next Hop        MED    LocPrf Path  
============================================================================= 
Neighbor 2.2.2.2 
*  0.0.0.0/0          > 172.17.171.1    1000   2000   3000 1000 100 2333 
*  111.222.111.220/30 > 111.222.111.223 65200  65200  4000 800 65500 
Neighbor 33.33.33.33 
   0.0.0.0/0          > 172.17.171.1    1000   2000   3000 1000 100 2333 
   111.222.111.220/30 > 111.222.111.223 65200  65200  4000 800 65500 
 To display the IPv6 BGP RIB: 
config>router(1)> bgp(1)# show rib ipv6 
* = Best Route 
   Network              > Next Hop             MED    LocPrf Path  
============================================================================= 
Neighbor 2:2:2:2::2 
*  ::/0                 > 11:11:11:11::1       1000   2000   3000 1000 100 2333 
   11:11:11:11::/64     > ::                   1000   2000   3000 1000 100 
*  abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126 
   > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200  65200  4000 80 65500 
Neighbor 33:33:33:33::33 
   ::/0                 > 11:11:11:11::1       1000   2000   3000 1000 100 2333 
*  11:11:11:11::/64     > ::                   1000   2000   3000 1000 100 
   abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd/126 
   > abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd   65200  65200  4000 80 65500 
The above fields are: 
Neighbor  
Neighbor IPv4 or IPv6 address 
Status (Best Route) 
Marks with a “*” the ‘Best Route’, i.e. the route entry 
forwarded to the Router’s RIB (Routing Information Base) 
Network 
IPv4 or IPv6 network address (prefix and prefix length) 
IPv4 prefix length can be 0–32; IPv6 prefix length can be 0–128. 
Next hop 
Network prefix and prefix length 
7. Traffic Processing 
MED 
Number of Multi-exit Discriminators (in decimal value) 
Possible values: 0–4294967295 
LocPrf 
Local preference 
Possible values: 0–4294967295 
Path 
Network prefix and prefix length 
Value: string with interpretation of two octets or four octets 
Viewing BGP Summary 
You can view the summary of neighbor connections information by using the command show summary. 
This command is available in the CLI contexts for IPv4 and IPv6, at the BGP level: 
config>router(<number>)>bgp(<ASN>)#.  
IPv4 AF connections appear on top, followed by IPv6 AF connections. 
 To display the BGP summary: 
config>router(1)>bgp(1)# show summary 
Neighbor                                 AS     Up/Down       State 
============================================================================= 
11:11:11:11::205                         209    never         Active 
3.3.3.2                                  3000   never         Idle 
172.17.171.205                           209    12d 06:23:53  Established 
172.17.171.218                           209    12d 06:23:53  Active 
abcd:abcd:abcd:abcd:abcd:abcd:abcd:abcd  65200  never         Active 
The above fields are: 
Neighbor  
Neighbor IPv4 or IPv6 address 
AS  
Remote AS number 
Possible values: 0..35655 or 0..4294967295 
Up/Down  
Amount of time that the underlying TCP connection has been in existence, i.e. 
how long this peer has been in the Established state. 
Note: Up/Down time is set to zero when a new peer is configured or the 
router is booted. 
Possible values: 0 - 4294967295 seconds 
When up/down time = 0, displays “never”. 
Otherwise displays in format number of days, hours, minutes, and seconds, 
for example: “12d 06:23:53” 
7. Traffic Processing 
State 
BGP session state 
Possible values are: 
• Idle 
• Connect 
• Active 
• Opensent 
• Openconfirm 
• Established 
After configuring BGP on a router in an existing BGP environment, you should test that BGP is working 
properly. 
 To test BGP: 
1. Wait a few seconds after configuration for BGP communications to take place. 
2. For each configured BGP neighbor: 
a. Navigate to the BGP neighbor CLI context 
(config>router(<number>)>bgp(<ASN>)>neighbor(<IP-address>)#). 
b. Enter show neighbor-connection and check that communication has been successfully 
established. 
c. Navigate to the IPv4 unicast address family neighbor context 
(config>router(<number>)>bgp(<ASN>)>ipv4-unicast-af> 
neighbor(<IP-address>)#). 
d. Enter show advertised-route and check that the correct destination routes are being 
advertised. 
e. Enter show received-route and check that BGP routes are being received. 
3. If IPv6 has been configured for this neighbor: 
a. Navigate to the IPv6 unicast address family neighbor context 
(config>router(<number>)>bgp(<ASN>)>ipv6-unicast-af> 
neighbor(<IP-address>)#). 
b. Enter show advertised-route and check that the correct destination routes are being 
advertised. 
c. Enter show received-route and check that BGP routes are being received. 
4. Navigate out of the BGP context, to the router CLI context. 
5. Enter show routing-table and check that there are new routes marked as originating in BGP. 

## 7.11 Routing Protocol OSPF  *(p.564)*

7. Traffic Processing 
7.11 Routing Protocol OSPF 
Open Shortest Path First (OSPF) is a link-state interior-gateway protocol for dynamic routing. The 
current implementation is OSPFv2 (handles IPv4 only).  
Applicability and Scaling 
The following functionality is not supported in OSPF version 2: 
 
Note 
OSPF does not support the BFD protocol. 
Standards Compliance 
Standard 
Name 
Unsupported functionality 
RFC 2328 
OSPF Version 2 
• IPv6 (supported only in OSPF v.3) 
• Multiple OSPF instances on a router 
• Area-to-backbone virtual links 
RFC 3101 
The OSPF Not-So-Stubby Area (NSSA) Option 
 
RFC 3509 
Alternative Implementations of OSPF Area 
Border Routers 
 
RFC 4750 
OSPF Version 2 Management Information Base 
 
RFC 4940 
IANA Considerations for OSPF 
 
Benefits 
Dynamic routing protocols enable routing tables to automatically adapt to changing networks. Link-state 
dynamic routing protocols such as OSPF quickly adapt to network changes, enable intelligent decisions 
for best routing paths, and are highly scalable. 
All the routers in an Autonomous System (AS) must use the same Interior Gateway Protocol (IGP). 
7. Traffic Processing 
Functional Description 
OSPF functionality is explained in the following sections. 
Dynamic Routing Protocols 
Routers direct packets through their various interfaces according to their routing tables, which specify 
an exit interface for each destination IP network. While routing tables can include static, manually 
configured routes, an optimized routing table requires knowledge of remote network topology and 
complex path calculations. Dynamic routing protocols define how routers communicate network 
topology with each other and how they accordingly calculate optimized network paths and create their 
routing tables. 
The internet is divided into Autonomous Systems (AS). An AS is usually the network of an Internet 
Service Provider (ISP) or another large organization that administers the AS-internal routing policy. 
Routing information inside each AS is communicated and determined by an Interior Gateway Protocol 
(IGP) such as OSPF; Routing information between ASes is communicated by the Border Gateway 
Protocol (BGP). 
Link-State Routing 
Link-state routing is one of the two main types of IGPs, along with distance-vector routing. OSPF is a link-
state routing protocol. 
In link-state protocols, each router creates and maintains a relatively full map of network connectivity. 
The connectivity map, called the Link-State Database (LSDB), includes information on which routers are 
connected to which other routers, and each connection’s cost metric, which takes into account things 
like round-trip time, throughput, and link availability. The map’s completeness enables the router to 
intelligently calculate the optimal path from itself to any network destination, without having to rely on 
partial path calculations made in other parts of the network. These optimal paths are used to 
dynamically create a routing table. 
To supply information for LSDBs, each router in the network notifies the network about its own 
immediate neighboring routers and the costs of its connections with them. Routers collect this link-state 
information and issue Link-State Advertisements (LSAs) to their neighbors. Upon receiving an LSA, each 
router updates its LSDB. 
To inform their neighbors of their existence, routers send periodical HELLO messages. When HELLO 
messages stop coming from a router, the connection with that router is considered to have failed, and 
an LSA is generated to inform the network of the lost connection. 
7. Traffic Processing 
OSPF Network Architecture 
To reduce routing traffic and LSDB size, an AS that uses OSPF is divided into OSPF areas. Each area is a 
group of contiguous networks which appears to OSPF externally as a single unit with an invisible internal 
topology. 
The AS must have a single designated backbone area so that each other area is directly connected to the 
backbone. A router that connects an area to the backbone (that is, it has an interface in the backbone 
and an interface in another area) is called an Area Border Router (ABR). An ABR summarizes its area’s 
topology for external distribution, and maintains an LSDB for all areas to which it is connected. 
 
 
AS-External Information 
To enable routing to destinations outside the AS, designated Autonomous System Boundary Routers 
(ASBRs) receive topology information about other ASs, and distribute it to internal routers. ASBRs can be 
configured whether to distribute topology from specified external sources (static routes or from BGP). 
However, to reduce traffic, LSDB size, and routing table size, areas can be configured so that only the 
area ABR is aware of the AS-external topology, and the internal routers route traffic with destinations 
outside the AS through the ABR. Two types of such areas can be configured: 
 
7. Traffic Processing 
Stub Area 
Cannot originate nor import AS-external topology. Internal routers in this area 
route through the ABR. 
Not So Stubby Area (NSSA) 
Cannot originate but can import AS-external topology 
 
An area which is neither stub nor NSSA is called a transit area. The backbone area must always be a 
transit area. 
Link-State Summarization 
For AS-internal topology information, there is by default no difference between the different types of 
non-backbone areas: ABRs of stub, NSSA and transit (except for backbone) areas summarize AS-internal, 
area-external link-state information for distribution to area-internal routers. However, a stub or NSSA 
ABR can be optionally configured to suppress summary-LSAs, instead becoming the area’s single default 
gateway. 
Designated Routers 
To reduce network traffic, each network selects a Designated Router (DR) to send LSAs outside of the 
network. A Backup Designated Router (BDR) is also selected in case of DR failure. Routers are selected 
according to configurable router priority indexes (lowest number indicates highest priority). 
Authentication 
OSPF can be configured to perform authentication, in which case OSPF information is accepted only 
from password-authenticated routers. 
Routing Preferences 
When there are conflicts between routes received from different sources, such as static routes, OSPF 
AS-internal routes, and OSPF AS-external routes, the Routing Table Manager (RTM) chooses among the 
sources according to configurable source preference indices (lowest number indicates highest priority).  
Explicit Range Aggregation 
To reduce route lists, explicit ranges can be configured to replace included subnets. Specifically, internal 
IP address ranges can be configured to be summarized by a transit area ABR, or external IP address 
7. Traffic Processing 
ranges can be aggregated by an NSSA ABR. For a transit area ABR, an internal range can also be 
configured to be hidden from other areas. 
Maintained Information 
OSPF maintains the following network information, all of which can be viewed (see Viewing OSPF 
Status): 
• 
Neighbor list 
• 
Interface information 
• 
LSDB  
• 
LSA counters (see Viewing OSPF Statistics) 
Factory Defaults 
OSPF parameters are configured at these levels: 
• 
Configuring OSPF at the Router Level: Parameters that determine OSPF behavior for the whole 
router, for all interfaces 
• 
Configuring OSPF at the Area Level: Parameters that characterize an area, for all interfaces that 
are configured as belonging in this area 
• 
Configuring OSPF at the Interface Level: Per-interface parameters 
Router OSPF Parameters 
The following parameters determine OSPF behavior for the whole router, for all interfaces: 
Parameter 
Description 
Default Value 
external-preference 
Preference index for OSPF AS-external routes. See 
Routing Preferences. 
110 
internal-preference 
Preference index for OSPF AS-internal routes. See Routing 
Preferences. 
10 
ospf 
Whether OSPF configuration is defined (but not 
necessarily enabled) on this router 
no ospf 
redistribute 
Whether to distribute routes from specified external 
sources (connected, static or BGP) to the rest of the AS. 
See AS-External Information. 
no redistribute 
7. Traffic Processing 
Parameter 
Description 
Default Value 
router-id 
ID for router in OSPF communications, in format like IP 
address. Must be unique in AS 
-- 
(mandatory configuration) 
shutdown 
Enable (no shutdown) / disable (shutdown) OSPF on the 
router. 
shutdown 
Area OSPF Parameters 
The following parameters characterize an area (see OSPF Network Architecture), for all interfaces that 
are configured as belonging in this area: 
Parameter 
Description 
Default Value 
area-id 
ID for area in OSPF communications. Must be unique in AS. 
Format is like IP address. Can be same as IP address of a 
network in the area. Backbone area must have ID 0.0.0.0 
-- 
default-cost 
Cost metric of default route, for stub area ABR to advertise 
into the area. See Link-State Routing. 
1 
nssa 
Whether area is NSSA, and whether the area ABR will provide 
area routers with summary LSAs (or just rely on its default 
route). See AS-External Information and Link-State 
Summarization. 
no nssa, no-summary 
range 
Internal IP address range(s) to be summarized or hidden by a 
transit area ABR, or external IP address range(s) to be 
aggregated by an NSSA ABR. See Explicit Range Aggregation. 
-- 
shutdown 
Enable (no shutdown) / disable (shutdown) the area 
shutdown 
stub 
Whether area is a stub area, and whether the area ABR will 
provide area routers with summary LSAs (rather than just rely 
on its default route). See AS-External Information and Link-
State Summarization. 
no stub, no-summary 
Interface OSPF Parameters 
The following parameters determine OSPF behavior per-interface: 
Parameter 
Description 
Default Value 
area 
ID of area to which interface belongs. See OSPF Network 
Architecture. 
no area 
7. Traffic Processing 
Parameter 
Description 
Default Value 
authentication-key 
Password for OSPF authentication. See Authentication. 
-- 
authentication-type 
Whether OSPF information should be password-
authenticated. See Authentication. 
no authentication 
dead-interval 
Time after which the connection with a silent neighbor is 
considered failed. See Link-State Routing. 
40 
hello-interval 
Time, in seconds, between sending HELLO packets. See Link-
State Routing. 
10 
metric  
Explicit network cost of the interface for OSPF path 
calculation. See Link-State Routing. 
1 
ospf 
Whether OSPF configuration is defined (but not necessarily 
enabled) on this interface 
no ospf 
passive 
Whether OSPF packets can (no passive) or cannot (passive) 
be sent through this interface 
no passive 
priority 
Priority index for becoming DR or BDR. See Designated 
Routers. 
1 
retransmit-interval 
Time, in seconds, between retransmissions of 
unacknowledged adjacency LSAs and of other network 
advertisements. See Link-State Routing.  
5 
shutdown 
Enable (no shutdown) / disable (shutdown) OSPF on the 
interface 
shutdown 
transit-delay 
Time, in seconds, to be added to the LSA’s age before 
transmission. Should be the estimated time of LSA 
transmission over the interface including propagation delays 
1 
Configuring OSPF 
OSPF is not configured by default on RAD routers. On a router that does not have OSPF defined, once 
the router itself and its interfaces have been properly configured, you can configure OSPF. To configure 
OSPF properly, you will need to know your network OSPF design. 
 To configure OSPF on a fresh router: 
1. Define OSPF on the router by entering the following commands in the device CLI: 
configure 
router <number> 
7. Traffic Processing 
ospf 
OSPF is defined on the router, and the CLI ospf context is provided. 
2. In the router ospf context, define the router ID: 
router-id <id> 
where <id> is an ID for the router in OSPF communications, in IP address format (<0-255>.<0-
255>.<0-255>.<0-255>). The ID must be unique in the AS. To simplify management, the ID can 
be the actual IP address of one of the router’s interfaces, or there may be some other 
organizational convention. 
3. Where network design requires that this router have non-default values (see Parameters and 
Factory Defaults) for any router-level OSPF parameters, configure them (see Configuring OSPF at 
the Router Level). 
4. Still in the router ospf context, enable OSPF on the router by entering: 
no shutdown 
5. Configure each OSPF area (see OSPF Network Architecture) that the router should be in according 
to network design: 
d. In the router OSPF context (config>router(<router_number>)>ospf#), define the are ID: 
area <area-id> 
where <area-id> is an ID for the area in OSPF communications, in IP address format (<0-
255>.<0-255>.<0-255>.<0-255>). The ID must be unique in the AS. To simplify management, 
the ID can be the actual IP address of a network in the area, or there may be some other 
organizational convention. The backbone area ID must be 0.0.0.0 . 
The area is defined, and the CLI area context is provided. 
e. In the area context (config>router(<router_number>)>ospf>area(<area-id>)#): 
 
If according to network design the area should be a stub area, enter: 
stub 
 
If according to network design the area should be an NSSA area, enter: 
nssa 
f. Where network design requires that this router have non-default values (see Parameters 
and Factory Defaults) for any area-level OSPF parameters, configure them (see Configuring 
OSPF at the Area Level). 
g. Still in the area context, enable the area by entering: 
no shutdown 
An enabled area means that OSPF interfaces connected to it can be enabled, and that the 
area’s type (stub / NSSA / transit) cannot be changed. 
h. Exit the area context. 
7. Traffic Processing 
6. Exit the router OSPF context to return to the router CLI context. 
7. Configure OSPF on each interface: 
a. Go into the interface CLI context (config>router(<router_number>)> 
interface(<interface_number>)#), and define OSPF on the interface: 
ospf 
OSPF is defined on the interface, and the CLI interface ospf context is provided. 
b. In the interface OSPF context, set the area with which to associate the interface: 
area <area-id> 
where <area-id> is the area’s ID, according to network design. 
c. Where network design requires that this interface have non-default values (see Parameters 
and Factory Defaults) for any interface-level OSPF parameters, configure them (see 
Configuring OSPF at the Interface Level). 
d. Still in the interface OSPF context, activate OSPF on the interface by entering: 
no shutdown 
e. Exit the interface OSPF context, and exit the interface context. 
Configuring OSPF at the Router Level 
The following commands are available in the CLI router OSPF context: 
config>router(<router_number>)>ospf# . The exception to this is the ospf command itself, which is 
performed in the router context: config>router(<router_number>)# . 
 
Task 
Command 
Comments 
Define OSPF on the router (if not yet 
defined), and provide the router CLI 
ospf context 
[no] ospf 
After defining OSPF on the router, OSPF still 
needs to be enabled (after setting router-id) 
with no shutdown. 
no ospf removes OSPF from the router (if no 
areas are defined). 
Define ID for the router in OSPF 
communications 
router-id <id> 
<id> is in IP address format: <0-255>.<0-
255>.<0-255>.<0-255> . The ID must be unique 
in the AS. To simplify management, the ID can 
be the actual IP address of one of the router’s 
interfaces, or there may be some other 
organizational convention. 
7. Traffic Processing 
Task 
Command 
Comments 
Enable / disable OSPF on the router 
[no] shutdown 
To disable: shutdown . To enable: no 
shutdown 
Define / remove OSPF area, with an 
ID for the area in OSPF 
communications 
[no] area <area-id> 
<area-id> is in IP address format: <0-255>.<0-
255>.<0-255>.<0-255>. The ID must be unique 
in the AS. To simplify management, the ID can 
be the actual IP address of a network in the 
area, or there may be some other 
organizational convention. The backbone area 
ID must be 0.0.0.0 . 
no area <area-id> removes the area from 
router OSPF configuration (if the area is not 
associated with any interfaces). 
To further configure the area, see Configuring 
OSPF at the Area Level 
Set ASBR to distribute routes from 
specified external sources (static or 
BGP) to the rest of the AS, or disable 
distribution 
[no] redistribute 
{connected | static | 
bgp}  
To disable distribution: no redistribute . 
See AS-External Information 
Note: The redistribute bgp command does not 
work for local BGPs. To redistribute routes into 
local (directly connected) OSPF and advertise 
the BGP, use redistribute connected. 
Set preference index for OSPF AS-
external routes 
external-preference 
<priority> 
<priority> should be an integer in range 1–255.  
Note: the value of 255 is considered as 
unreachable and the appropriate route is not 
be added to the routing table. 
See Routing Preferences 
Set preference index for OSPF AS-
internal routes 
internal-preference 
<priority> 
<priority> should be an integer in range 1–255.  
Note: the value of 255 is considered as 
unreachable and the appropriate route is not 
be added to the routing table. 
 
See Routing Preferences 
View Link-State Database (LSDB) 
show database 
See Viewing OSPF Status 
View OSPF interface information 
show interface-table 
View OSPF neighbors 
show neighbor-table 
7. Traffic Processing 
Configuring OSPF at the Area Level 
The following commands are available in the CLI OSPF area context: 
config>router(<router_number>)>ospf>area(<area-id>)# . Note that the area command, which is 
performed in the router OSPF context: config>router(<router_number>)>ospf#, appears under 
Configuring OSPF at the Router Level. 
 
Task 
Command 
Comments 
Setting cost metric of 
default route, for stub 
area ABR to advertise 
into the area 
default-cost <metric> 
Use only on stub area ABR.  
Possible values: 1–16777215 (24-bit) 
See Link-State Routing. 
Making area an NSSA 
area, or changing an 
NSSA area back to a 
transit area 
[no] nssa [summary | 
no-summary] 
All routers in an NSSA area must be configured as 
such. See AS-External Information. 
This command is effective regardless of the area’s 
current type (transit or stub). 
For the area ABR to just rely on its default route 
rather than provide area routers with summary 
LSAs, use nssa no-summary. For it to go back to 
providing summary LSAs, use nssa summary. See 
Link-State Summarization. 
To change an NSSA area back to a transit area, use 
no nssa 
Setting internal IP 
address range(s) to be 
summarized or hidden 
by a transit area ABR 
[no] range <ip-address>/ 
<mask-length> [advertise | 
not-advertise]  
To set internal transit area summarization, on the 
transit ABR use: range <ip-address>/<mask-length> 
advertise. 
To set internal transit area hiding, on the transit ABR 
use: range <ip-address>/<mask-length> not-
advertise. 
<ip-address> should represent an IP range, in IP 
address format. <mask-length> should be an integer 
in range 1–32, representing the number of first bits 
in <ip-address> that are the network mask. 
To delete a configured range, use: no range <ip-
address>/<mask-length>. 
See Explicit Range Aggregation. 
7. Traffic Processing 
Task 
Command 
Comments 
Making area a stub area, 
or change a stub area 
back to a transit area 
[no] stub [summary | 
no-summary] 
All routers in a stub area must be configured as 
such. See AS-External Information. 
This command is effective regardless of the area’s 
current type (transit or NSSA). 
For the area ABR to just rely on its default route 
rather than provide area routers with summary 
LSAs, use stub no-summary . For it to go back to 
providing summary LSAs, use stub summary. See 
Link-State Summarization. 
To change a stub area back to a transit area, use no 
stub 
Enable / disable the area 
[no] shutdown 
To disable: shutdown. To enable: no shutdown 
Configuring OSPF at the Interface Level 
The following commands are available in the CLI interface OSPF context: 
config>router(<router_number>)>interface(<interface_number>)>ospf# . The exception to this is the 
interface ospf command, which is performed in the interface OSPF context: 
config>router(<router_number>)>interface(< 
interface_number>)# . 
Task 
Command 
Comments 
Define OSPF on the 
interface (if not yet 
defined), and provide the 
interface CLI ospf context 
ospf 
After defining OSPF on the interface, OSPF still 
needs to be enabled (after associating the 
interface with an area) with no shutdown. 
no ospf removes OSPF from the interface (if no 
areas are defined) 
Associate interface with an 
area 
[no] area <area-id> 
Specify the area with its <area-id>. 
To disassociate the interface from any area, use 
no area <area-id>. 
Set password 
authentication for OSPF 
communications 
[no] authentication-type 
[simple-password] 
To set authentication, use: authentication-type 
password . To disable authentication, use: no 
authentication. 
See Authentication. 
7. Traffic Processing 
Task 
Command 
Comments 
Set password for OSPF 
authentication, if enabled 
authentication-key 
<authentication-key> [hash] 
<authentication-key> can be any combination 
of up to 8 ASCII characters. Use the hash option 
to specify that the provided key should be 
encrypted, in which case the key can be up to 
22 characters. 
See Authentication. 
Enable / disable OSPF on 
the interface 
[no] shutdown 
To disable: shutdown . To enable: no shutdown 
Set the time after which the 
connection with a silent 
neighbor is considered 
failed 
dead-interval <seconds> 
 
Possible values: 1–2147483647. 
See Link-State Routing. 
Set the time between 
sending HELLO packets 
hello-interval <seconds> 
<seconds> should be in range 1–65535. 
See Link-State Routing. 
Explicitly set the network 
cost of the interface for 
OSPF path calculation 
metric <number> 
Possible values: 1–65535 
See Link-State Routing. 
Set the priority index for 
becoming DR or BDR 
priority <priority> 
Possible values: 0–255. 
See Designated Routers 
Prevent OSPF packets from 
being sent through the 
interface 
[no] passive 
A passive interface is still advertised as an OSPF 
interface, but doesn’t itself run the OSPF 
protocol. 
To re-enable sending OSPF packets, use no 
passive 
Set the time between 
retransmissions of 
unacknowledged adjacency 
LSAs and of other network 
advertisements 
retransmit-interval <seconds> 
 
 
Possible values: 0–3600. 
See Link-State Routing. 
Set the time to be added to 
the LSA’s age before 
transmission 
transit-delay <seconds> 
The estimated time of LSA transmission over 
the interface including propagation delays 
Possible values: 0–3600 
7. Traffic Processing 
Example 
In this example, a router needs to be configured for OSPF. According to network design, this router is a 
stub area ABR with two interfaces, one in the backbone and one in a stub area. Authentication is used in 
both areas, but each area uses a different password. 
The relevant part of the network design is: 
Router ID 
Interface 
Area 
Password 
10.10.1.1 
Interface 1 
0.0.0.0 
12345672 
Interface 2 
10.10.0.0 
abcdefgh 
The actual configuration process for this example is: 
configure 
router 1 
remark Configure OSPF on router 
ospf 
router-id 10.10.1.1 
no shutdown 
remark Configure OSPF Areas 
area 0.0.0.0 
no shutdown 
exit 
area 10.10.0.0 
stub no-summary 
no shutdown 
exit 
exit 
remark Configure OSPF with authentication on interfaces 
interface 1 
ospf 
area 0.0.0.0 
authentication-type simple-password 
authentication-key 12345678 
no shutdown 
exit 
exit 
interface 2 
ospf 
area 10.10.0.0 
authentication-type simple-password 
authentication-key abcdefgh 
no shutdown 
exit 
exit 
7. Traffic Processing 
Configuration Errors 
The table below lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Cannot be modified; OSPF interface 
is administratively enabled 
You tried to associate an interface with 
an area, but the interface is OSPF-
enabled 
Enter shutdown and try again. 
Cannot create OSPF interface; IP 
address wasn’t configured 
You tried to run ospf in the interface 
context, but the interface itself has no 
fixed IP address (it is possibly DHCP) 
Set a fixed IP address for the 
interface. 
Cannot create OSPF interface; more 
than one IP address is configured 
You tried to run ospf in the interface 
context, but the interface itself has 
multiple IPv4 addresses 
Remove interface IP addresses 
to leave only one, and try 
again. 
Cannot delete area; There is an 
OSPF interface associated with the 
Area 
You tried to run no area (router OSPF 
context) on an area associated with an 
interface 
Go to the relevant interface 
OSPF context and enter no 
area <area-id>. 
Cannot delete ospf; ospf area or 
OSPF interface exist 
You tried to run no ospf (router context) 
with existing areas or OSPF interfaces 
Remove OSPF from all 
interfaces, delete all areas, and 
try again. 
cannot enable OSPF interface; area-
id is not defined 
You tried to enable OSPF on an interface 
without an associated area 
Set an area for the interface 
and try again. 
Cannot enable OSPF; router-id is 
not configured 
You tried to run no shutdown (router 
OSPF context) with no OSPF router ID 
Set router-id and try again. 
Cannot execute, license required 
You tried to run ospf (router context) 
without an OSPF license 
Contact your RAD sales 
representative to obtain a 
license. 
Cannot modify area parameter; 
area is administratively enable 
You tried to make an enabled area into 
a stub or NSSA 
Enter shutdown and try again. 
Cannot modify; OSPF is enabled 
You tried to change router-id with OSPF 
enabled 
Enter shutdown and try again. 
Cannot set area as nssa; area-id 
0.0.0.0 cannot be nssa 
You tried to make the backbone a stub 
or NSSA 
If this is not the backbone, 
change the area ID and try 
again. 
Cannot set metric; Area is a Transit 
You tried to run the default-cost 
command on a transit area 
If this area should be a stub 
area, enter stub and try again. 
7. Traffic Processing 
Message 
Cause 
Corrective Action 
OSPF entity shall be initiated before 
interface’s configuration 
You tried to run ospf in the interface 
context, but OSPF hasn’t been defined 
on the router 
Exit to the router context and 
enter ospf. Then try again. 
Viewing OSPF Status 
You can view the current configuration (see Viewing the Current Configuration), and you can also view 
several types of dynamic and traffic-based OSPF information (see sections below). This information can 
be used for testing (see Testing OSPF) and debugging. 
Viewing the Current Configuration 
To view the current configuration, use the standard RAD commands: info (to view only non-default 
configuration) and info detail (to include default configuration). 
You can view this info at any of the following configuration levels: 
Level 
Context Prompt 
Router 
config>router(<router_number>)>ospf# 
Area 
config>router(<router_number>)>ospf>area(<area-id>)#  
Interface 
config>router(<router_number>)>interface(<interface_number>)>ospf# 
For example: 
configure 
config# router 1 
config>router(1)# ospf 
config>router(1)>ospf# info detail 
 
router-id 1.2.3.4 
 
 
external-preference 110 
 
internal-preference 30 
 
 
shutdown 
 
echo "OSPF AREA Configuration" 
# 
OSPF AREA Configuration 
 
area 0.0.0.0 
 
 
no nssa 
 
 
no stub 
 
 
no shutdown 
 
exit 
 
config>router(1)>ospf# 
7. Traffic Processing 
Viewing the Link-State Database 
You can view the current Link-State Database by using the show database command. This command is 
available in the CLI router OSPF context: (config>router(<router_number>)>ospf#), and can be used for 
testing (see Testing OSPF) and debugging. 
For example: 
Area ID 
Type 
LS ID Router ID 
Sequence 
Age 
Checksum 
-------------------------------------------------------------------------------- 
100.100.100.100 
1 
000.000.010.010 
000.000.010.010 
0x80000096 
938
 
0x609b 
100.100.100.100 
1 
050.050.050.020 
050.050.050.020 
0x80000006 
839
 
0x49d4 
000.000.000.000 
2 
020.020.020.020 
020.020.020.030 
0x80000008 
946
 
0x3c3a 
000.000.000.000 
3 
050.050.050.000 
000.000.010.010 
0x8000000d 
764
 
0xcbd9 
000.000.000.000 
4 
000.000.010.010 
050.050.050.020 
0x80000002 
840
 
0x83f7 
The above fields are: 
Area ID 
<area-id> of an OSPF area  
Type 
One of the following LSA types: 
1 – Router-LSA: Describes collected states of router's interfaces 
2 – Network-LSA: Describes routers attached to network 
3 – Network summary-LSA: Describes inter-area routes to networks, summarized by 
ABR 
4 – ASBR summary-LSA: Describes inter-area routes to ASBRs, summarized by ABR 
5 – AS-external-LSA: Originated by ASBR, describes routes to AS-external 
destinations or a default route for the AS  
7 – NSSA-external-LSA:  Describes external route information within an NSSA 
LS ID 
Router ID or IP address (depending on Type) of domain described by the LSA 
Router ID 
ID of originating router 
Sequence 
Signed 32-bit integer, incremented each time the router originates a new instance of 
the LSA. Used to detect old and duplicate LSAs 
Age 
LSA age in seconds 
Checksum 
Checksum of complete LSA contents except for Age field 
7. Traffic Processing 
Viewing OSPF Interface States 
You can view current interface states by using the show interface-table command. This command is 
available in the CLI router OSPF context: (config>router(<router_number>)>ospf#), and can be used for 
testing (see Testing OSPF) and debugging. 
For example: 
IP Address 
Area ID 
Type 
Priority 
DR 
BDR 
State 
------------------------------------------------------------------------------------- 
000.000.000.000 
000.000.000.001 
P-T-P 0001 
000.000.000.000 
000.000.000.000
 
Down 
192.168.001.001 
000.000.000.003 
BRDCST 0001 
192.168.001.007 
192.168.001.002
 
Up 
The above fields are: 
IP Address 
Interface IP address 
Area ID 
ID of area with which the interface is associated 
Type 
Broadcast or point-to-point 
Priority 
Priority index for becoming DR or BDR 
DR 
Designated Router in this network 
BDR 
Backup Designated Router in this network 
State 
UP if all of the following are true: OSPF is enabled (no shutdown), the IP 
interface’s operational status is UP, and the OSPF interface is enabled (no 
shutdown) 
Viewing OSPF Neighbors 
You can view the current OSPF neighbors by using the show neighbor-table command. This command is 
available in the CLI router OSPF context: (config>router(<router_number>)>ospf#), and can be used for 
testing (see Testing OSPF) and debugging. 
For example: 
Neighbor 
Neighbor ID 
Priority 
      State 
Interface 
Port 
---------------------------------------------------------------------------- 
192.168.001.003 
192.168.001.009 
0001 
Full 
192.168.001.002 
Ethernet wan1 
192.168.001.007 
000.000.000.004 
0004 
Full 
192.168.001.002 
Ethernet wan1 
10.10.001.001        000.000.000.005 
0005 
Full 
10.10.001.002        Ethernet wan2 
7. Traffic Processing 
The above fields are: 
Neighbor 
IP address used by this neighbor as its source address  
Neighbor ID 
The neighbor’s OSPF router-id 
Priority 
The neighbor’s priority index for becoming DR or BDR 
State 
The state of the connection with this neighbor. One of: 
• Down 
• Attempt 
• Init 
• Twoway 
• Exchangestart 
• Exchange 
• Loading 
• Full*  
*OSPF adjacency is not full if there is MTU mismatch between RAD and other vendors 
equipment. If this is the case, change the default egress-mtu value from 1790 to the value 
of the other vendor (e.g. 1500). (so that egress-mtu values should be equal in both OSPF 
adjacencies. 
Interface 
IP address of the neighbor’s interface with which a connection is established 
Port 
Name of the neighbor’s interface with which a connection is established 
Viewing OSPF Statistics 
You can view LSA counters by using the show statistics command. This command is available in the CLI 
router OSPF context: (config>router(<router_number>)>ospf#). 
For example: 
 
Count Checksum 
-------------------------------------- 
External LSA 50 
0x3245 
AS LSA  
1059 
0x7843 
New LSAs Originated 45 
- 
New LSAs Received 
1024 
- 
The above fields are: 

## 7.12 Tunneling  *(p.583)*

7. Traffic Processing 
Count 
The number of LSAs of this type 
Checksum 
32-bit sum of the checksums of the LSAs of this type. Can be used to check if an 
LSDB has changed or to compare LSDBs. 
Testing OSPF 
After configuring OSPF on a router in an existing OSPF environment, you should test that OSPF is 
working properly.  
 To test OSPF: 
1. Wait a few seconds after configuration for OSPF communications to take place. 
2. Navigate to the CLI router OSPF context (config>router(<router_number>)> 
ospf#). 
3. Enter show interface-table and check that a DR and a BDR have been successfully elected. 
4. Enter show neighbor-table and check that connections have been established with all neighbors. 
5. Enter show routing-table and check that expected routes have been learned from OSPF neighbors. 
6. Exit the OSPF context, to the router CLI context. 
7. Enter show routing-table and check that there are new routes marked as originating in OSPF. 
 
7.12 Tunneling  
ETX-1p supports route-based IPsec tunnels.  
Applicability and Scaling 
This feature is applicable to all the device versions. 
7. Traffic Processing 
Standards Compliance 
RFC 4087: IP Tunnel MIB 
Functional Description 
ETX-1p supports configuration of tunnel interfaces under the router level.  
Both delivery (encapsulating) and payload (encapsulated) protocols can be either IPv4 or IPv6, 
independently of each other. 
IPsec tunnels are employed in route-based IPsec mode. Crypto maps connected to router interfaces 
work in policy-based IPsec mode. You cannot have both types in the same device, so if there is an IPsec 
tunnel, and you cannot to bind a crypto map to a router interface. 
IPsec tunnels cannot be configured within VRFs. 
If the interface has multiple IP addresses, by default, the lowest one is used as tunnel source. You can 
bind a map to an address (even if the interface has a single address). In this case: 
• 
The tunnel source will be the one configured. 
• 
If the interface does not own the configured address, ETX-1p ignores the configuration and 
behaves as if the map is not bound to the interface. 
Once an IPsec tunnel is enabled, it becomes and remains operationally up when you configure all of the 
following: 
• 
Tunnel source address or interface 
• 
Tunnel destination 
• 
IP address 
• 
Crypto map 
An IPsec tunnel becomes operationally down under any of the following conditions: 
• 
There is no route to the tunnel destination address. 
• 
The route to the tunnel destination address is through the tunnel itself. 
• 
You configure the tunnel address indirectly by anchoring the tunnel to a router interface, and 
that router interface does not have an address of the same type (IPv4 or non-link-local IPv6) as 
the tunnel, or has multiple such addresses. 
• 
The interface that anchors the tunnel source is down. 
7. Traffic Processing 
 
Notes 
The tunnel remains operationally down as long as the anchoring router 
interface is not active and does not have a valid IP address. 
 
Both ends of the tunnel should be on the same network. 
You can configure a tunnel source IP address. This address binds the tunnel to a router interface.  
• 
The tunnel and the router interface anchoring it are on the same router. 
• 
You can configure the address directly, by providing an IPv4 or a non-link-local IPv6. 
Alternatively, the address can be configured indirectly, by providing a router interface. For such 
configuration, the tunnel is operationally up only if the anchoring router interface has a single address of 
the same type (IPv4 or non-link-local IPv6) as the tunnel. 
 
Notes 
The tunnel remains operationally down as long as there is no active router 
interface configured with this address. 
 
You can configure a tunnel destination IP address that can be either IPv4 or non-link-local IPv6. 
 
Note 
The tunnel destination address should be configured at the other end of the 
tunnel as the tunnel source address. 
 
Configure proper routing to use a tunnel. The next hop should be either the address of the other end of 
the tunnel or the tunnel interface. The tunnel address can be propagated by routing protocols such as 
OSPF or BGP. 
ETX-1p supports IP fragmentation and defragmentation in tunnels, for packets that are larger than the 
tunnel IP MTU. 
Route-Based IPsec Redundancy 
You can configure backup tunnels for route-based IPsec redundancy. 
1. Assign each backup a unique priority. The configurable range is 1-254 (higher values indicate 
higher priorities). Multiple backups of a tunnel must have unique priorities. 
2. If an IPsec tunnel has backup tunnels, only one backup may be active at any time. First, ETX-1p 
tries to establish the primary tunnel.  
7. Traffic Processing 
3. If it fails, ETX-1p tries the backup with the highest priority. If that backup fails, it proceeds to the 
one with the next highest priority, and so on, until a tunnel comes up.  
4. If all the backups are exhausted, ETX-1p returns to the primary tunnel. 
If the active tunnel fails, ETX-1p follows the same procedure, starting with the primary (or the highest 
prioritized backup, if the primary was the one that failed). 
While searching for an operating backup, ETX-1p skips non-existent and disabled tunnels. 
Dead peer detection timers are as follows: 
• 
Packet retransmission: 1 seconds. 
• 
Time after which a tunnel is considered failed if not responding: 9 seconds. 
• 
Time after which tunnel establishment is considered to fail: 30 seconds. 
Factory Defaults 
Parameter 
Description 
Default Value 
ip-mtu 
IP MTU of tunnel 
0 
shutdown 
Enable (no shutdown) / disable (shutdown) IPsec tunnel. 
no shutdown 
transport-router 
No transport-router is configured 
no transport-router 
Configuring Tunnels 
Configuring Tunnel Interfaces 
 To configure a tunnel interface: 
1. Navigate to configure router <number> to select the router on which to configure IPsec tunnels.  
2. At the config>router(<number>)# prompt that is displayed, enter  
tunnel-interface <number> ipsec.  
The config>router(<number>)>tunnel-interface(<number>) is displayed. 
The tunnel is identified by this number. 
3. Enter all necessary commands according to the tasks listed below. 
7. Traffic Processing 
4. In order to activate the tunnel following configuration change, perform “shutdown” command 
and then “no shutdown“.  
 
 
Task 
Command 
Comments 
Configuring backup 
tunnel 
backup tunnel-interface 
<interface-number> priority 
<number> 
no backup tunnel-interface 
<interface-number> 
number – backup priority 
Possible values: 1–254 
Clearing tunnel statistics 
clear-statistics 
 
Associating interface 
with crypto map 
crypto-map 
See Configuring Crypto Map 
Defining tunnel IP 
address and prefix 
length 
ip-address {static <ip-
address/prefix-length | 
negotiated }> 
 
Entering no ip-address removes the tunnel 
IP address. 
ip-address – valid static unicast IPv4 or 
non-link-local IPv6 address with compatible 
prefix length 
negotiated – IPsec tunnel IP address is to 
be learned from a responder  
Notes:  
• A tunnel can have only one address. If 
you repeat the command, the last 
instance applies. 
• The address cannot be an address of a 
tunnel or a router interface. 
• Both ends of the tunnel should be on 
the same network. 
Defining tunnel IP MTU 
ip-mtu <number> 
Entering no ip-mtu removes IP MTU from 
the tunnel interface. 
Possible values: 0 (no IP MTU), 128-–65535 
Note: 0 means that the MTU is to be 
calculated according to the delivery 
protocol. For IPv4 it is 1476 and for IPv6 
1456.  
Defining tunnel name 
name <tunnel-name> 
tunnel-name – 0–64 character string 
Entering no name returns the tunnel name 
to its default value. 
7. Traffic Processing 
Task 
Command 
Comments 
Displaying crypto map 
status 
show crypto-map-status 
[<name>] 
See  Viewing Crypto Map Information 
Showing tunnel status 
show status 
See Viewing Tunnel Status 
Disabling tunnel 
interface 
shutdown 
Entering no shutdown enables the tunnel 
interface. 
Configuring an underlay 
router 
transport-router <router-
number> 
no transport-router 
router-number – is always 1 
This means that the tunnel should be 
configured on a router other than 1. 
Defining tunnel 
destination IP address 
tunnel-destination <ip-address> 
Entering no tunnel-destination removes 
the address. 
Possible values: Valid unicast IPv4 or non-
link-local IPv6 address 
Notes: 
• The source and destination addresses 
must be both IPv4 or IPv6. 
• The tunnel destination address should 
be configured at the other end of the 
tunnel as the tunnel source address. 
Defining source IP 
address or router 
interface number used 
to bind the tunnel to a 
router interface 
tunnel-source [<ip-address>] 
[router-interface <number>] 
Entering no tunnel-source removes the 
address. 
Possible values:  
ip-address – valid unicast IPv4 or non-link 
local IPv6 address 
number - number of a router interface 
Notes: 
• Either IP address or router interface 
number must be defined; not both. 
• The tunnel and the router interface 
anchoring it must be on the same 
router. 
• If you configure the tunnel source IP 
address, the tunnel goes up only if 
there is an active router interface 
configured with this IP address. 
7. Traffic Processing 
Task 
Command 
Comments 
• If you configure the router interface 
number, the tunnel goes up only if the 
router interface has a single address of 
the same type (IPv4 or non-link-local 
IPv6) as the tunnel. 
• The source and destination addresses 
must be both IPv4 or IPv6. 
• The tunnel source address should be 
configured at the other end of the 
tunnel as the tunnel destination 
address. 
Removing a Tunnel 
 To remove a tunnel: 
1. Navigate to configure router <number> to select the router from which to remove a tunnel.  
2. At the config>router(<number>)# prompt that is displayed, enter no tunnel-interface <number>. 
Examples 
This example demonstrates how a tunnel interface is created and bound to a previously defined crypto 
map. 
• 
Creating an access-control list 
configure 
        access-control 
            access-list "tunnel1" 
                permit ip any any sequence 10 
            exit 
        exit 
 
• 
Defining IPsec parameters 
        crypto 
            ipsec-transform-set "tunnel1" 
                algorithms esp-aes-cbc-128 esp-sha1 
            exit 
            isakmp-key "abcd1234" address 20.20.20.2 
            isakmp-key "abcd1234" address 30.30.30.2 
            isakmp-policy 1 
7. Traffic Processing 
                encryption aes-cbc-128 
                group 14 
            exit 
• 
Creating a crypto map tunnel1 (IPsec profile) 
 
            crypto-map "tunnel1" 
                match-address "tunnel1" 
                peer-address 20.20.20.2 
                pfs-group 14 
                sa-lifetime seconds 8000 
                transform-set "tunnel1" 
                sequence-number 11 
            exit 
• 
Creating a crypto map tunnel2 (IPsec profile) 
            crypto-map "tunnel2" 
                match-address "tunnel1" 
                peer-address 30.30.30.2 
                pfs-group 14 
                sa-lifetime seconds 8000 
                transform-set "tunnel1" 
                sequence-number 11 
            exit 
        exit 
 
• 
        Creating Ethernet interfaces 
        router 1 
            name "Router#1" 
            interface 1 
                address 40.40.40.1/24 
                bind ethernet wan1  
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 2 
                address 20.20.20.1/24 
                bind ethernet wan2 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 3 
                address 30.30.30.1/24 
                bind ethernet lan1 
                dhcp-client 
                    client-id mac 
7. Traffic Processing 
                exit 
                no shutdown 
            exit 
            interface 4 
                address 172.17.233.38/24 
                bind ethernet lan2 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 5 
                address 41.41.41.1/24 
                bind ethernet lan3 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 32 
                address 169.254.1.1/16 
                bind ethernet lan4 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
• 
Creating static route 
            static-route 0.0.0.0/0 address 172.17.233.1 metric 1 
• 
Creating a tunnel interface 1 and binding it to the crypto map 
            tunnel-interface 1 ipsec 
                no shutdown 
                tunnel-source 20.20.20.1 
                tunnel-destination 20.20.20.2 
                ip-address 60.60.60.1/24 
                crypto-map "tunnel1" 
            exit 
• 
Creating a tunnel interface 2 and binding it to the crypto map 
            tunnel-interface 2 ipsec 
                no shutdown 
                tunnel-source 30.30.30.1 
                tunnel-destination 30.30.30.2 
                ip-address 70.70.70.1/24 
                crypto-map "tunnel2" 
            exit 
        exit 
    exit 
7. Traffic Processing 
Configuration Errors 
Message 
Cause 
Corrective Action 
Tunnel exists with a different type 
You tried changing the type of an 
existing tunnel.  
Create a new tunnel of the new 
type. 
There is a crypto map connected 
to a router interface 
You tried to configure an IPsec 
tunnel, while the crypto map was 
connected to a router interface. 
Cancel policy-based IPsec mode; 
then you can connect a crypto 
map to a tunnel interface and 
configure an IPsec tunnel.  
Maximum number of tunnels 
exceeded 
You tried to create more tunnels 
than ETX-1p allows. 
Delete unnecessary tunnels and 
create a new one. 
Invalid address; enter a unicast 
address 
You assigned a broadcast or 
multicast address to the tunnel. 
Assign a unicast address to the 
tunnel. 
The address is assigned to another 
interface 
You tried to configure the tunnel 
with an address of an already 
existing tunnel or router interface.  
Assign a unique address to the 
tunnel. 
Configure either source address or 
interface, not both 
You tried to configure the router 
interface anchoring the tunnel 
with both an address and 
interface. 
Remove one of the configurations: 
either the address or interface. 
Source and destination must be 
both IPv4 or both IPv6 
You tried to configure tunnel 
destination with an IPv4 address, 
while the tunnel source is an IPv6 
address. 
You tried to configure tunnel 
source with an IPv4 address while 
the tunnel destination is an IPv6 
address. 
Define destination and source with 
same type of IP address – both 
IPv4 or both IPv6. 
This priority is in use by another 
backup 
You tried to configure multiple 
backups with the same priority 
Use unique value of priority with 
each tunnel 
This tunnel is a backup of another 
tunnel 
You tried to configure a tunnel as 
primary, while it is already a 
backup of another tunnel 
Create a new tunnel to serve as a 
primary tunnel 
The backup tunnel is a backup of 
another tunnel 
You tried to configure a tunnel as 
backup, while it is already a 
backup of another tunnel 
Create a new tunnel to serve as a 
backup tunnel 
7. Traffic Processing 
Message 
Cause 
Corrective Action 
The backup tunnel has a backup 
tunnel 
You tried to configure a tunnel as 
backup, while it is already a 
primary tunnel (i.e. it is configured 
with a backup) 
Create a new tunnel to serve as a 
backup tunnel 
A tunnel cannot be a backup of 
itself 
You tried to configure a tunnel as 
a backup of itself 
Create a new tunnel to serve as a 
backup tunnel 
This priority is in use by another 
backup 
You tried to configure multiple 
backups with the same priority 
Use a unique priority for each 
backup 
Viewing Tunnel Status 
You can display the current tunnel status. 
 To display tunnel status: 
• 
At the config>router(<number>)>tunnel-interface(<number>)# prompt, enter: 
show status 
The tunnel status is displayed. 
 
config>router(1)>tunnel-interface(1)# show status 
Tunnel             : 1 
Type               : IPSEC 
Status             : Up 
Tunnel Address     : 60.60.60.2/24 (IKEv2 acquired) 
Tunnel Source 
   Interface       : Router Interface 1/2 (Ethernet  3) 
   Address         : 192.168.1.11 
Tunnel destination : 192.168.1.10 
Transport Router   : 1  
IP MTU             : 1476 (Calculated) 
 
Up For : 1 Day(s), 10:25:01 
                           Packets          Bytes 
Tunnel Encapsulated        150              10000 
Tunnel Decapsulated        150              5000 
  
7. Traffic Processing 
Status Parameters 
Parameter 
Description 
Tunnel 
Tunnel number 
Type 
Tunnel type 
Possible value: IPsec 
Status 
Tunnel administrative and operational status 
Possible values: Up, Down 
Tunnel Address 
Tunnel IP address 
Possible values: 
• -- (Tunnel source IP address is not configured.) 
• IPv4 or IPv6 unicast addres 
• Acquired By IKEv2 (If IPsec tunnel address was acquired by IKEv2) 
Tunnel Source 
Interface 
Router interface anchoring the tunnel 
Possible values:  
• -- (No interface is configured.) 
• Router Interface <router number>/<interface number> 
or 
Physical interface bound to the router interface anchoring the tunnel 
Possible values: 
• -- (empty string) 
• (<port-type> <port-number>) 
Tunnel Source 
Address 
Tunnel source IP address 
Possible values: 
• -- (Tunnel source IP address is not configured.) 
• IPv4 or IPv6 unicast address 
Tunnel Destination 
Tunnel destination IP address 
Possible values: 
• -- (Tunnel destination IP address is not configured.) 
• IPv4 or IPv6 unicast address 
Transport Router 
Number of tunnel transport router 
Possible values: 
• number 
7. Traffic Processing 
Parameter 
Description 
IP MTU 
Tunnel IP MTU 
Possible values: -- or number.  
If Tunnel IP MTU configuration method is non-zero, it is printed 
If Tunnel IP MTU configuration method is zero:  
• If tunnel source address type is IPv4, 1476 is printed. 
• If tunnel source address type is IPv6, 1456 is printed. 
• If tunnel source address type is unknown, -- is printed. 
Up For 
Tunnel uptime in seconds 
Display hint: ddd Days, hh:mm:ss 
Input Bytes 
Number of Rx bytes since tunnel uptime 
Input Packets 
Number of Rx packets since tunnel uptime 
Output Bytes 
Number of Tx bytes since tunnel uptime 
Output Packets 
Number of Tx packets since tunnel uptime 
 
Viewing Crypto Map Information 
You can view information on a specific crypto map or all configured crypto maps using the show crypto-
map-status command. 
 To display the crypto map information: 
1. Navigate to configure router <number>tunnel-interface<number>.  
2. At the config>router(<number>tunnel-interface (<number>))# prompt that is displayed, enter 
show crypto-map-status [<tunnel-name>]. 
config>router(1)tunnel-interface(1)# show crypto-map-status tunnel1 
Crypto Map               : tunnel1 
Tunnel Peers             : 20.20.20.1 --- 20.20.20.2  
Security Association     : Up 0 minutes ago 
 
IKE 
----------------------------------------------------------------------------- 
Version              : 2 
SA Negotiation Mode  : NA 
Authentication       : Pre-shared secret 
Encryption           : AES-CBC-128 
Hashing              : SHA1 
Diffie Hellman Group : 14 
In SPI               : e047c3660524fdd4 
7. Traffic Processing 
Out SPI              : 93d0e80fd8d1b0a6 
Reauthentication in  : 999 days 
 
Transform Set 
----------------------------------------------------------------------------- 
Algorithms  : ESP-AES-CBC-128 ESP-SHA-1 
In SPI      : 00000000ca0944c9 
Out SPI     : 00000000c71e1971 
 
Remaining Lifetime 
----------------------------------------------------------------------------- 
In Kilobytes  : 4608000 
Out Kilobytes : 4608000 
Seconds       : 6960 
 
The above fields are: 
Tunnel Peers 
Local peer --- remote peer 
Possible values: ip-address 
Security Association 
SA status and SA age 
Possible values:  
SA status – Connecting, Down, Up 
SA age – <number> minutes ago 
IKE version  
SA Negotiation Mode 
IKE SA negotiation mode 
Possible values: Aggressive, Main 
Authentication          
IKE authentication method  
Possible value: Pre-shared secret 
Encryption            
IKE encryption algorithm  
Possible value: AES-CBC-128, AES-CBC-256 
Hashing                 
IKE hashing algorithm   
Possible values: SHA1-96-HMAC, SHA2-256-128-HMAC,  
SHA2-512-256-HMAC 
Diffie Hellman Group 
IKE Diffie Hellman group 
Possible values: 1, 2, 5, 14, 19, 20 
In SPI 
IKE in SPI 
Possible values: string 

## 7.13 Virtual Router Redundancy Protocol (VRRP)  *(p.597)*

7. Traffic Processing 
Out SPI 
IKE out SPI 
Possible values: string 
Re-authentication in 
Time to IKE key re-authentication 
Possible values: <number> minutes/hours/days 
Transform Set 
Algorithms  
Transform set first algorithm 
Possible values: ESP-AES-CBC-128, ESP-AES-CBC-256, ESP-
AES-GCM-128, ESP-AES-GCM-256, ESP-NULL, ESP-AES-
GMAC-128,  
ESP-AES-GMAC-256 
Transform set second algorithm 
Possible values: ESP-SHA1-96-HMAC, ESP-SHA2-256-128-
HMAC, ESP-SHA2-512-256-HMAC 
In SPI 
Transform set in SPI 
Out SPI 
Transform set in SPI 
Remaining Lifetime 
In Kilobytes 
Transform set remaining lifetime (in kilobytes) 
Out Kilobytes 
Transform set remaining lifetime (out kilobytes) 
Seconds 
Transform set remaining lifetime (seconds) 
 
7.13 Virtual Router Redundancy Protocol (VRRP)  
Virtual Router Redundancy Protocol (VRRP) enables a group of routers to act as a virtual router with a 
virtual IP address that can be configured as the default gateway for access devices in a LAN.  
A static default gateway router is a potential single point of failure, which is eliminated by VRRP. 
7. Traffic Processing 
Standards Compliance and MIBs 
The VRRP feature complies with the following standards. 
Standard 
Title 
RFC 5798 
Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6 
RFC 6527 
Definitions of Managed Objects for the Virtual Router Redundancy Protocol Version 3 
(VRRPv3) 
Functional Description 
VRRP Group 
A VRRP group is defined as a group of routers that share one or more virtual IP addresses. If a router’s 
physical IP address matches a virtual IP address, it is referred to as the address owner. The routers in the 
group are assigned priorities ranging from 1–255, with 255 being the highest priority, however only 
priorities 1–254 are configurable. Priority 255 is automatically assigned to the address owner regardless 
of the configured priority. Up to 4 VRRP groups are supported per device. 
Master Router 
At any time, one of the routers is the master (active) and the others are backups. The router with the 
highest priority is selected as the master, therefore the address owner is the master unless it has failed. 
If more than one router has the highest priority, the one with the highest primary IP address is selected 
as master. The primary IP address is one of the router interface’s real (IPv4) or link-local (IPv6) IP 
addresses. It is used as the source address in VRRP advertisements 
The master router forwards upstream traffic packets destined for the virtual IP address(es), and sends 
periodic advertisements to the backup routers at a user-configurable interval. If the backup routers do 
not receive an advertisement for a set period, the backup router with the next highest priority takes 
over as master.  
Preemption 
If preemption is enabled, then when a new router is added to a VRRP group and its priority is higher 
than any of the routers in the group, it preempts the master role. When a router with priority 255 
(address owner) is added to a VRRP group or becomes active, it preempts all lower-priority routers, even 
7. Traffic Processing 
if preemption is disabled. If no router has priority 255 and preemption is disabled, then no preemption 
occurs. 
Factory Defaults 
By default, no VRRP groups exist. When a VRRP group is created, its default configuration is the 
following: 
Parameter 
Default  
Remarks 
description 
 
virtual router <ip-ver> group <id> 
• <ip-ver> is either IPv4 or IPv6. 
• <id> is the group VRID. 
The description does not affect the device 
behavior; it is solely provided for better 
readability 
preempt 
preempt 
Preemption is enabled by default. 
priority 
100 
 
shutdown 
shutdown  
VRRP is disabled by default; at least one 
virtual IP address must be associated with 
the group before the group can be 
enabled. 
timer-advertise 
100 centiseconds 
 
Configuring VRRP 
You configure VRRP group parameters at the router interface level. 
Note 
A VRRP group cannot be associated with a router interface for which any of 
the following is true: 
• 
The router interface is bound to a port other than Ethernet or wifi access 
point (e.g. PPP port). 
• 
The router interface is a loopback interface. 
 To configure VRRP group parameters: 
1. At the config>router(<number>)>interface(<interface-num>)# prompt, enter the following, 
specifying the VRRP group ID (1–255) and IP version: 
vrrp <vrid> [{ipv4 | ipv6}] 
7. Traffic Processing 
One of the following prompts is displayed, depending on the IP version entered: 
config>router(<number>)>interface(<interface-num>)>vrrp(<vrid>,ipv4)# 
config>router(<number>)>interface(<interface-num>)>vrrp(<vrid>,ipv6)# 
7. Perform the required tasks according to the following table. 
 
Task 
Command 
Comments 
Configuring VRRP group 
description 
description <string> 
Type no description to use an 
empty (NULL) string. 
Associating a virtual IP address 
with the VRRP group 
ip <ip-address> 
• Type no ip <ip-address> to 
delete the association with 
the IP address. 
• The IP address must be in the 
correct form for the 
configured IP version. 
Enabling preemption 
preempt 
Type no preempt to disable 
preemption. 
Configuring VRRP priority 
priority <number> 
Possible values for number:  
1–254 
If the device is an address owner 
it overrides the configured 
priority with 255 (which is not a 
configurable value) 
Configuring interval between 
sending advertisement 
messages 
timer-advertise 
<centiseconds>  
Possible values:  
1–4095 
Viewing VRRP status 
show status 
 
Administratively enabling or 
disabling VRRP for router 
interface 
no shutdown 
• Type shutdown to 
administratively disable VRRP. 
• VRRP can be enabled only if at 
least one virtual IP address 
has been associated. 
 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
7. Traffic Processing 
Message 
Cause 
Corrective Action 
Too many VRRP groups on this 
interface 
You tried to create more than 
four groups. 
Delete one of the VRRP groups from the 
interface. 
The address must be a valid 
unicast IP 
You tried to configure an invalid 
IP address. 
Configure a valid unicast IP address. 
The port bound to the router 
interface does not support VRRP 
 
You tried to to configure VRRP 
on an active router interface 
bound to a port other than 
Ethernet or wifi access point 
(e.g. PPP), or activate a router 
interface with VRRP 
Configure VRRP on a router interface 
bound to a port on which VRRP can run. 
VRRP is not allowed on a 
loopback router interface 
You tried to configure VRRP on 
a router interface that is a 
loopback router interface. 
Configure VRRP on a router interface 
bound to a port on which VRRP can run. 
Too many addresses are 
configured for the VRRP group 
  
You tried to configure more 
than four addresses. 
Delete one of the associated addresses 
before associating a new IP address with 
the group. 
IP version of the address and the 
VRRP group are incompatible 
 
You tried to associate an IPv4 
address with an IPv6 group or 
an IPv6 address with an IPv4 
group.  
Associate an IPv4 address with an IPv4 
group, or an IPv6 address with an IPv6 
group. 
 
Viewing VRRP Status  
You can view VRRP status by using the show status command. This command is available in one of the 
following CLI contexts, depending on the IP version of the VRRP group:  
config>router(<number>)>interface(<interface-num>)>vrrp(<vrid>,ipv4)# 
config>router(<number>)>interface(<interface-num>)>vrrp(<vrid>,ipv6)# 
 
For example: 
# configure router(1)>interface(7)>vrrp(1,ipv4)# show status 
Router/Interface                 : 1/7 
  Physical Port                  : Ethernet 2/2 
VRRP Group                       : 1 (IPv4)                   
  Administrative Status          : Enabled 
  Operational Status             : Master 
  Uptime (seconds)               : 1111 
7. Traffic Processing 
Primary IP Address               : 10.20.0.01/24 
Protected IP Address             : 10.20.0.01/24 
                                 : 10.20.0.10/24 
Virtual MAC Address              : 00:00:5e:00:01:01 
Advertisement Interval (seconds) : 1 
Preemption                       : Enabled     
Priority                         : 255 
Field 
Description 
Router/Interface 
Router and interface where the VRRP group is configured 
Physical Port 
Physical interface that is bound to the router interface 
VRRP Group 
VRRP group ID 
Administrative Status 
VRRP group administrative status – Disabled or Enabled 
Operational Status 
VRRP role: 
• Backup – Router interface is acting as backup. 
• Master – Router interface is acting as master. 
• Init – Router interface VRRP group parameters are being initialized. 
• Lower Layer Down – The interface with which the group is associated is 
non-operational. 
Uptime (seconds) 
Time since VRRP role changed from Init to Backup or Master 
Primary IP Address 
Primary IP address and mask of the VRRP group 
Protected IP Address 
One or more virtual IP address(es) protected by the VRRP group; one output line is 
displayed for each protected IP address. 
Virtual MAC Address 
Virtual MAC address of the VRRP group 
Advertisement Interval 
(seconds) 
Interval between VRRP advertisements (if the router is acting as master) 
Preemption 
Preemption state – Disabled or Enabled 
Priority 
Router VRRP priority (0–255) 
 
Viewing VRRP Summary 
You can view a VRRP group summary by using the show vrrp-summary command for router, or show 
summary-vrrp command for router interface. This command is available in the following CLI contexts: 
• 
config>system>router – displays information for all VRRP groups in the device 
7. Traffic Processing 
• 
config>router(<number>) – displays information for all VRRP groups configured for any router 
interfaces belonging to the router 
• 
config>router(<number>)>interface – displays information for all VRRP groups configured for 
the router interface 
For example: 
#configure router(1)>interface(1)# show summary-vrrp 
Rtr If Phys If       Group     Pri Own Pre State  Primary Address  
1/1    Ethernet 1/2  111(IPv4) 100 Yes Ena Master 10.10.10.10 
1/1    Ethernet 1/2  222(IPv6) 200 --  Dis Backup FE80::1234 
 
Field 
Description 
Rtr 
Router and interface where the VRRP group is configured 
Phys If 
Physical interface that is bound to the router interface 
Group 
VRRP group ID 
Pri 
Router VRRP priority (0–255) 
Own 
Indicates if VRRP group is address owner: Yes or -- 
Pre 
Preemption state – Dis or Ena 
State 
VRRP role: 
• Backup – Router interface is acting as backup. 
• Master – Router interface is acting as master. 
• Init – Router interface VRRP group parameters are being initialized. 
• LLD – The router interface where the VRRP group is configured, is not 
operational. 
Primary Address 
Primary IP address of the VRRP group 