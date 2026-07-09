# Feature Reference – 5 Traffic Processing – 5.3 DHCP Layer-3 Relay

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 944–947.*


## Applicability and Scaling  *(p.944)*

ETX-2i Devices 
5. Traffic Processing 
 To display flow test status: 
ETX-2i>config>flows>flow(evc1_in)# show test 
Test : MAC Swap  Duration (Sec)  : 50    Remain (sec)  : 40     No TTL 
ETH 3
ETH 1
Loop performed on this flow (evc1_in)
 
Application Layer Loopback Test on Flow with a Single Attribute 
5.3 DHCP Layer-3 Relay 
ETX-2i supports DHCP Layer-3 Relay agent to pass DHCP requests and replies between clients and 
servers that are not on the same subnet. Unlike Layer-2 Relay (refer to DHCP Layer-2 Relay in 
Management and Security chapter), DHCP Layer-3 Relay agent intercepts DHCP client requests, converts 
them to unicast messages, and sends them to the configured server. It also intercepts and sends back 
replies to the client.  
Applicability and Scaling 
This feature is applicable to a device with an embedded router or bridge. 
One DHCP Relay agent is supported per router. 
Up to four DHCP servers are supported by DHCP Relay agent. 
Note 
If multiple servers are configured, Layer-3 forwards client packets to all 
servers simultaneously. 
 

## Standards and Compliance  *(p.945)*


## Functional Description  *(p.945)*

ETX-2i Devices 
5. Traffic Processing 
Standards and Compliance 
[RFC 1542] — Clarifications and Extensions for the Bootstrap Protocol 
[RFC 2131] — Dynamic Host Configuration Protocol 
[RFC 2132] — DHCP Options and BOOTP Vendor Extensions 
[RFC 3046] — DHCP Relay Agent Information Option 
Functional Description 
ETX-2i supports two DHCP Layer-3 Relay models: 
• 
DHCP Layer-3 Relay model for HW router 
• 
DHCP Layer-3 Relay model for bridge 
ETX-2i also supports a command to set the source port that DHCP relay uses when forwarding packets. 
Implementation of DHCP Layer-3 Relay requires configuration of DHCP Layer-3 Relay for HW router or 
bridge (see Configuring DHCP Layer-3 Relay for HW Router or Configuring DHCP Layer-3 Relay for 
Bridge.  
DHCP Packet Flow through DHCP Layer-3 Relay 
Once configured, the flow of DHCP packets through DHCP Layer-3 Relay is as follows (see figures below):  
1. DHCP client broadcasts a DHCP request. 
2. DHCP relay agent intercepts the request, and performs a sanity check on the packet. 
3. If the request is not valid, DHCP relay agent discards the message. 
4. Otherwise, if it is valid, DHCP relay agent sends the message toward DHCP server. If several 
servers are configured, the message is relayed to all servers. 
5. DHCP server sends a DHCP reply. In the case of multiple servers, user can configure a particular 
server to answer per requester MAC address; in this case, only one server, which is configured 
with the requester MAC, replies. Otherwise, all servers reply, and the first reply is the valid one. 
6. DHCP relay agent intercepts the request, performs a sanity check on the packet, and forwards 
the packet to DHCP client. 

## Factory Defaults  *(p.946)*

ETX-2i Devices 
5. Traffic Processing 
ETX -2i HW Router
L3 Network
Router IF
Router IF
DHCP Client
DHCP Server
Relay Agent
 
DHCP Layer-3 Relay Model for HW Router 
L3 Network
Bridge Port
Bridge Port
DHCP Client
DHCP Server
3rd Router
Bridge Port
Router Interface
DHCP-Relay
ETX-2 Bridge
 
DHCP Layer-3 Relay Model for Bridge 
Source Port 
ETX-2i supports setting the source port that DHCP relay uses when forwarding packets. The default 
source port varies, depending on the implementation. Most RAD devices use a random port higher than 
1024. However, some servers expect relays to use port 67 (the destination of client to server packets). 
The source-port command enables you to set the source port to 67 (or another port) to accommodate 
such servers. 
Factory Defaults 
The system DHCP Layer-3 Relay parameters have the default values shown in the following table. 
Parameter 
Default  
Remarks 
source-port 
default 
The default UDP port is a random number 
higher than 1024 

## Configuring DHCP Layer-3 Relay  *(p.947)*

ETX-2i Devices 
5. Traffic Processing 
Configuring DHCP Layer-3 Relay 
Configuring DHCP Layer-3 Relay for HW Router  
 To configure DHCP Layer-3 Relay application for ETX-2i HW Router: 
1. Define at least one DHCP server (IPv4 unicast address only; maximum four servers) for the 
router’s DHCP layer-3 relay (dhcp-relay-server command in router level). 
2. Under that router, on a router interface, enable DHCP Layer-3 relay agent (dhcp-relay command 
in router>interface level). 
Configuring DHCP Layer-3 Relay for Bridge  
 To configure DHCP Layer-3 Relay application for Bridge: 
1. Define at least one DHCP server (IPv4 unicast address only; maximum four servers) for the 
router’s DHCP layer-3 Relay (dhcp-relay-server command in router level). 
2. Under that router, on another router interface, enable DHCP Layer-3 Relay agent (dhcp-relay 
command in router>interface level). 
3. Bind ETX-2i bridge port to router interface with DHCP Layer-3 Relay agent, as follows: 
 
On the ETX-2i device, configure bidirectional flows between SVI port and bridge port 
(ingress-port svi, egress-port bridge-port, and reverse-direction commands under 
config>flows>flow <flow-number>). 
 
Bind the router interface with Relay agent to SVI port (bind command in router>interface 
level).  
Configuring the DHCP Layer-3 Relay Source Port 
 To configure the source port: 
1. Navigate to configure system dhcp-relay. 
The config>system>dhcp-relay# prompt is displayed. 
2. Configure the source port according to the following table. 