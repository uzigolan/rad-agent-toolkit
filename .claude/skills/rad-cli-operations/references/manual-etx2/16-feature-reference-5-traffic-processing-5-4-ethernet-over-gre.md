# Feature Reference – 5 Traffic Processing – 5.4 Ethernet over GRE (ETHoGRE) Tunneling

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 948–960.*


## (chapter introduction)  *(p.948)*

ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Configuring DHCP relay source 
port  
source-port {default | udp <udp-port-
number>} 
udp-port-number – UDP port 
that DHCP relay uses when 
forwarding packets 
Possible values: 1-65535 
default – returns device to its 
default behavior, i.e., source-
port is set to a random UDP 
port higher than 1024. 
Note: Some servers expect 
relays to use UDP port 67 (the 
destination of client to server 
packets). This command 
enables the user to set the 
source port to UDP 67 to 
accommodate such servers. 
5.4 Ethernet over GRE (ETHoGRE) Tunneling  
ETX-2i devices with an embedded router support Ethernet over GRE (ETHoGRE), a Layer-2 tunneling 
technology that allows transport of Layer-2 frames and services over an IP/MPLS network using GRE 
Encapsulation.  
 

## Applicability and Scaling  *(p.949)*


## Standards Compliance  *(p.949)*


## Benefits  *(p.949)*

ETX-2i Devices 
5. Traffic Processing 
Applicability and Scaling 
This feature is applicable to ETX-2i and ETX-2i-B. 
ETX-2i supports up to 32 IPv4 or IPv6 GRE tunnels.  
Standards Compliance 
RFC 2784: Generic Routing Encapsulation (GRE) 
RFC 4087: IP Tunnel MIB 
RFC 2890: Key and Sequence Number Extensions to GRE 
Benefits 
• 
Allows transport of Layer-2 frames over an IP infrastructure. 
• 
Allows Service Providers to have a single infrastructure for both IP and Ethernet services. 
• 
Allows Layer-2 services in cases where only an IP network is available for transport. 
• 
Delivery of Layer-2 services to “out of reach” locations 
• 
Fast delivery of Layer-2 services while waiting for fiber connectivity 
 
 

## Functional Description  *(p.950)*

ETX-2i Devices 
5. Traffic Processing 
Functional Description 
ETHoGRE Encapsulation 
ETHoGRE encapsulation (tunneling) is illustrated in the following diagram.  
 
The original Ethernet frame header and payload are encapsulated with a GRE header, as described in 
RFC 2890 (optional fields are not supported), and a Tunnel IP header. 
 
 
 
 
ETX-2i Devices 
5. Traffic Processing 
Forwarding Model 
The diagram below describes the principal data path. 
Ethernet traffic entering the GRE tunnel is encapsulated with GRE and IP tunnel headers and then 
transmitted into the router. In the opposite direction, traffic identified as GRE tunnel, is stripped from its 
IP and GRE headers, and then transmitted to the Ethernet circuit. 
 
GRE packets that exceed the GRE interface (Tunnel) MTU are discarded. There is no support for 
fragmentation/reassembly.  
Tunnel source IP should match one of the Router Interface IP addresses. 
Configuration Concept and Management Entities 
The diagram below describes the configuration concepts and management entities for configuring GRE 
Tunnel and service. 
ETX-2i Devices 
5. Traffic Processing 
ETH
Port
Router
Bridge
ETP
SVI Type: GRE
SVI
GRE Tunnel IP
ETHoGRE
RI Facing 
Tunnel Network
Rx Flow
Tx Flow
ERP
Bridge
ETH
Port
ETH
Port
ETH
Port
 
A Layer-2 attachment circuit connected to a GRE SVI (that is bound to a GRE tunnel interface) by flows 
can connect to the following interfaces on the user side (Ethernet): 
• 
Ethernet port  
• 
Bridge port  
• 
ETP 
GRE
SVI
Tx Flow
Rx Flow
Flows must be identified by VLAN at this point
  
Flows to/from an SVI, support the following: 
• 
VLAN edit and p-bit marking (same capabilities supported for a PTP flow) 
• 
Policer / Envelope Policer over flows at Tunnel ingress 
• 
CoS/queue map per p-bit, DSCP, or fixed, for: 
 
Tx flows 
 
Rx flows: No Queue map, CoS mapping only for 10.3 envelope ONLY 
 
 
ETX-2i Devices 
5. Traffic Processing 
• 
OAM Up MEP (including 1564 support) 
• 
Flow L2CP profile 
• 
TWAMP – using Bridge (no support for L2 probe mode)  
• 
In-service (EVC) ping – using Bridge (no support for L2 probe mode) 
The SVI to GRE tunnel can support: 
• 
Eight Rx flows 
• 
A single Tx flow 
 
The Tunnel Tx flows can have the” Match all” classification profiles. 
Configuring GRE Tunnel  
The following procedure describes how to configure ETX-2i with a GRE tunnel: 
1. Create a Router SVI and activate it:  
configure port svi <svi-num>, and then no shutdown  
(refer to Switched Virtual Interfaces (SVIs) in the Cards and Ports chapter). 
2. Create a GRE SVI and activate it:  
configure port svi <svi-num> gre, and then no shutdown. 
 
 

## Factory Defaults  *(p.954)*

ETX-2i Devices 
5. Traffic Processing 
3. Configure flows with:  
 
Ingress Ethernet port, bridge port, or ETP port, and egress GRE SVI port (defined in step 2). 
 
Ingress GRE SVI port (defined in step 2) and egress Ethernet port, bridge port, or ETP port. 
 
Ingress Ethernet port or bridge port, and egress Router SVI port (defined in step 1). 
 
Ingress Router SVI port (defined in step 1) and egress Ethernet port or  bridge port. 
(See Configuring a Flow above.) 
4. Enable flows: config>flows>flow (<flow name>)>no shutdown 
5. Configure a router interface in the router level and bind it to the Router SVI (created in step 1). 
6. Configure a GREoEth tunnel interface in the router level (same subnet as router interface), 
including tunnel source (router interface number or IP address) and tunnel destination:  
config>router n>tunnel-interface 1 (see Configuring GRE Tunneling below). 
Layer-2 flow packets traveling through GRE tunnel are encapsulated with IP address of router.  
7. Optionally, mark the tunnel IP with a fixed DSCP value or a previously defined p-bit to DSCP 
profile.  
config>router n>tunnel-interface 1>dscp {fixed <number> | profile <profile-name>} 
(see Configuring GRE Tunneling below). 
8. Bind the tunnel to the predefined GRE SVI (in Step 2):  
config>router n>tunnel-interface 1 bind svi <svi-num> 
The SVI is used to connect multiple layer-2 egress/ingress flows to/from the GREoEth tunnel. 
Factory Defaults 
Parameter 
Description 
Default Value 
number 
DSCP number 
0 
key-number 
GRE key 
no key 
name 
Tunnel name 
Tunnel-# (no name) 
shutdown 
Enable/disable GRE tunnel. 
no shutdown 
gre-ip/gre-eth 
Tunnel type 
gre-ip 

## Configuring GRE Tunneling  *(p.955)*

ETX-2i Devices 
5. Traffic Processing 
Configuring GRE Tunneling 
 To configure a GRE tunnel: 
1. Navigate to configure router <number> to select the router on which to configure GRE 
tunneling. 
The config>router(number)# prompt is displayed. 
2. Enter tunnel-interface <number> gre-eth  
 
Tunnel number can be 1-32. 
3. In the config>router(<number>)>tunnel-interface (<number>)# prompt that is displayed, 
perform the required tasks according to the following table. 
Task 
Command 
Comments 
Binding tunnel to a Layer-2 
attachment circuit (SVI) 
bind svi <svi-port-number> 
no bind 
Binds SVI of type GRE to interconnect to 
flows. 
svi-port-number – Layer-2 port number 
Possible values: 1-n (user-defined per SVI 
index range in the device) 
The SVI type must be set to GRE (refer to 
Service Virtual Interfaces in the Cards and 
Ports chapter).  
Clearing tunnel statistics counters 
clear-statistics 
 
Configuring tunnel DSCP value 
dscp {fixed <number> | 
profile <profile-name>} 
number – fixed DSCP value 
Possible values:  
0-63 
255 –means that the ETHoGRE will use the 
DSCP profile. 
profile-name – name of profile that maps 
p-bit to DSCP (see Configuring Marking 
Profiles). 
Possible values: 1–32-character string 
Configuring tunnel GRE key 
key <key-number> 
no key 
Possible values:  
0 (no key) 
1 to 4,294,967,295 
no key means the GRE header does not 
include the key field. 

## Deleting a GRE Tunnel  *(p.956)*

ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Assigning a meaningful name to the 
tunnel 
name <tunnel-name> 
no name 
tunnel-name – 0–64-character string 
Entering no name returns the tunnel 
name to Tunnel-# (# is the tunnel index). 
Displaying tunnel status 
show status 
See GRE-ETH Tunnels at Router example. 
Enabling/disabling the tunnel  
shutdown 
no shutdown 
Tunnel interface shutdown stops traffic. 
Note: 
• Tunnel parameters can be changed on 
the fly, even if Tunnel is no shutdown. 
• If no shutdown, Tunnel is operational 
if a valid source and destination IP are 
configured. 
Defining tunnel destination IP 
address 
tunnel-destination <ip-
address> 
no tunnel-destination 
ip-address must be a valid unicast IPv4 or 
non-link-local IPv6 address. 
Source and destination addresses must 
both be IPv4 or both IPv6. 
Defining source IP address or router 
interface number used to bind the 
tunnel to a router interface 
tunnel-source [<ip-
address>] [router-interface 
<number>] 
no tunnel-source 
Either router-interface number or IP 
address must be defined; not both. 
ip-address must be a valid unicast IPv4 or 
non-link-local IPv6 address 
Source and destination addresses must 
both be IPv4 or both IPv6. 
Deleting a GRE Tunnel 
The following section describes how to delete a GRE tunnel. 
 To delete a GRE tunnel: 
1. Navigate to configure router <number> to select the router interface from which to delete a 
GRE tunnel. 
The config>router(number)# prompt is displayed. 
2. Enter no tunnel-interface <number>. 
The tunnel of the specified number is removed from the router interface.  

## Examples  *(p.957)*

ETX-2i Devices 
5. Traffic Processing 
Examples 
GRE-ETH Tunnels at Router 
The following example shows: 
• 
A router configured with a router interface facing the IP transport network. 
• 
Two GRE-ETH tunnels configured using two GRE interfaces at the router and bound to the 
Ethernet attachment circuit (flows) using SVI of type GRE. 
exit all 
config 
    port 
        svi 1 
            no shutdown 
        exit 
        svi 2 gre 
            no shutdown 
        exit 
        svi 3 gre 
            no shutdown 
        exit 
    exit 
    flows 
        classifier-profile "v100" match-any 
            match vlan 100 
        exit 
        classifier-profile "v200" match-any 
            match vlan 200 
        exit 
 
        flow "user_in" 
            classifier "untagged" 
            ingress-port ethernet 0/1 
            egress-port svi 1 
            no shutdown 
        exit 
        flow "user_out" 
            classifier "all" 
            ingress-port svi 1 
            egress-port ethernet 0/1 queue 0 block 0/1 
            no shutdown 
        exit 
        flow "tunnel1_in" 
            classifier "v100" 
            ingress-port ethernet 0/3 
            egress-port svi 2 
            no shutdown 
        exit 
        flow "tunnel1_out" 

## Configuration Errors  *(p.958)*

ETX-2i Devices 
5. Traffic Processing 
            classifier "v100" 
            ingress-port svi 2 
            egress-port ethernet 0/3 queue 0 block 0/1 
            no shutdown 
        exit 
        flow "tunnel2_in" 
            classifier "v200" 
            ingress-port ethernet 0/3 
            egress-port svi 3 
            no shutdown 
        exit 
        flow "tunnel2_out" 
            classifier "v200" 
            ingress-port svi 3 
            egress-port ethernet 0/3 queue 0 block 0/1 
            no shutdown 
        exit 
    exit 
    router 1 
        interface 1 
            address 20.20.20.20/24 
            bind svi 1 
            no shutdown 
        exit 
        tunnel-interface 1 gre-eth 
            no shutdown 
            tunnel-source router-interface 1 
            tunnel-destination 30.30.30.30 
            bind svi 2 
        exit 
        tunnel-interface 2 gre-eth 
            no shutdown 
            tunnel-source router-interface 1 
            tunnel-destination 40.40.40.40 
            bind svi 3 
        exit 
    exit 
exit 
Configuration Errors 
The following table lists the messages generated by ETX-2i when a configuration error is detected. 

## Viewing GRE Status  *(p.959)*

ETX-2i Devices 
5. Traffic Processing 
Message 
Cause 
Corrective Action 
Tunnel already exists with a 
different type 
You tried changing the type of 
an existing tunnel from gre-ip 
to gre-eth, or vice versa.  
Delete the tunnel and then create a new 
tunnel (same index as deleted tunnel) 
with the new type. 
Create a new tunnel (new index) of the 
new type. 
SVI type must be GRE 
SVI type is not GRE. 
Bind to SVI of type GRE. 
Profile type must be p-bit to 
DSCP 
Profile type is not p-bit to DSCP.   
The address is assigned to 
another interface 
You tried to configure the 
tunnel with an address of an 
already existing tunnel or 
router interface.  
Assign a unique address to the tunnel. 
Tunnel may not be anchored to 
loopback interface 
You assigned to the router 
interface anchoring the tunnel 
an address of a loopback 
interface.  
Assign another IP address. 
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
Define destination and source with 
same type of IP address – both IPv4 or 
both IPv6. 
Incorrect parameter value 
You tried configuring a tunnel 
interface number other than 1-
32. 
Configure tunnel-interface <1-32> only. 
Viewing GRE Status 
You can display the current GRE tunnel status. 
ETX-2i Devices 
5. Traffic Processing 
 To display GRE tunnel status: 
• 
At the config>router(<number>)>tunnel-interface(<number>)# prompt, enter: 
show status 
The GRE tunnel status is displayed. 
The following displays the status of a GRE-ETH tunnel. 
ETX-2I>config>router(2)>tunnel-interface(2)$ show status 
Tunnel             : 2 
Type               : GRE-ETH 
Status             : Up 
Tunnel Source 
   Interface       : Router Interface 2/1 (SVI 1) 
   Address         : 20.20.20.20 
Tunnel destination : 20.20.20.40 
 
Up For : 0 Day(s), 0:0:21 
 
                    Packets 
Tunnel Encapsulated 1532 
Tunnel Decapsulated 9800 
 
Parameter 
Description 
Tunnel 
Tunnel number 
Type 
Tunnel type 
Possible values: GRE-IP, GRE-ETH 
Status 
Tunnel status 
Possible values:  
Up 
Down: and one of the following: 
• Reason: Configuration Missing 
• Reason: Lower Layer Down 
• Reason: No Route To Destination 