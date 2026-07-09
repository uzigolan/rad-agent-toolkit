# Feature Reference – 8 Monitoring and Diagnostics – 8.4 TWAMP

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1372–1423.*


## Applicability and Scaling  *(p.1372)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
8.4 TWAMP 
ETX‑2i provides a low-scale (150 sessions) OAM TWAMP Light mechanism for measurement of one-way 
and two-way metrics between Layer-2 or Layer-3 network elements at all locations, without the need 
for a special performance management system. Its ICMP Echo service is useful for probing and general 
debugging, such as path continuity and integrity verification.   
ETX-2i with the PMC option provides a powerful high-scale (3000 sessions) TWAMP mechanism for 
measurement of the IP performance of Layer-3 networks at all locations, without the need for a special 
performance management system. It ensures SLA parameters in Layer-3 networks, by testing thousands 
of Layer-3 services simultaneously. 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products, with the following conditions: 
• 
PCS port is relevant to ETX-2i with an SHDSL or VDSL2 module. 
• 
Full TWAMP, UDP test, and RADM are relevant for ETX-2i with the PMC option. 
ETX‑2i supports low-scale OAM TWAMP, in the following scale: 
• 
Up to 15 Layer-3 controllers (Router interfaces of HW Router) 
• 
Up to a total of seven Layer-2 controllers (RI over Bridge or RI over L2 probe) 
• 
Up to three Layer-2 controllers over L2 probe 
• 
Up to 15 peers per device for TWAMP controllers (all devices except ETX-2i-10G); up to 150 
peers in ETX-2i-10G. 
• 
Up to 150 sessions @10pps TWAMP sessions over a single Layer-2 service / TWAMP controller. 
PMC in ETX-2i supports high-scale OAM TWAMP, in the following scale: 
• 
Up to 64 TWAMP controllers and eight responders. 
• 
Total of 3000 sessions @10pps and up to 3000 peers.  
• 
Up to eight PMC responders (one or more) with a total of 100 test sessions. 
• 
Up to four VRFs 

## Standards  *(p.1373)*


## Functional Description  *(p.1373)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Standards 
RFC 5357 – A Two-Way Active Measurement Protocol (TWAMP) 
RFC 2330 – Framework for IP Performance Metrics   
RFC 2681 – A Round-trip Delay Metric for IPPM 
RFC 4656 – A One-way Active Measurement Protocol (OWAMP) 
RFC 5481 – Packet Delay Variation Applicability Statement 
RFC 4737 – Packet Reordering Metrics 
RFC 5560 – A One-Way Packet Duplication Metric 
ITU-T Y.1540 – Internet protocol data communication service – IP packet transfer and availability 
performance parameters 
ITU-T Y.1541 – Network performance objectives for IP-based services 
ITU-T Y.1543 – Measurements in IP networks for inter-domain performance assessment 
Functional Description 
OAM TWAMP 
ETX‑2i TWAMP controllers and responders can operate in the following modes: 
• 
Layer-2 E-Line (point-to-point) service – L2 probe configuration. The TWAMP 
controller/responder is associated with a router interface and bound to an Ethernet/logical 
MAC/PCS port and flow.  
 
IPv6 is supported over the L2 probe configuration.  
 
Up to a total of three controllers and responders are supported. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
• 
Layer-2 E-LAN service over bridge – The TWAMP controller/responder is associated with a 
router interface that is connected to a bridge port via an SVI. 
 
 
• 
Layer-3 – The TWAMP controller/responder is associated with a router interface that is 
connected to an Ethernet port via an SVI. 
 
This configuration is relevant to embedded router only. 
 
A Layer-3 router interface ACL can be configured on the router interface. 
 
 
TWAMP can be configured on an independent VRF. A total of seven controllers/responders can be 
configured (for example, three controllers and four responders).  
ETX-2i Devices 
8. Monitoring and Diagnostics 
PMC TWAMP 
ETX-2i with PMC provides TWAMP controllers and responders with higher limits than ETX‑2i TWAMP for 
measurement of the IP performance of your Layer-3 network at all locations.  
ETX-2i with PMC supports TWAMP with the following capabilities: 
• 
TWAMP Light 
• 
Full TWAMP, including TWAMP Control protocol  
• 
ICMP echo  
• 
UDP echo  
• 
Responder Agnostic Delay Measurement (RADM) – one-way measurement without 
local/remote node TOD (NTP) lock 
The PM protocol is defined per peer towards specific responder. It is possible to operate mixed 
protocols per peer in the same TWAMP controller. 
TWAMP Light is recommended for use in a high-scale environment, to avoid the TCP overhead. In a low-
scale environment, Full TWAMP is recommended, as the test can be configured on the controller side 
only, reducing operation overhead. 
PMC in ETX-2i supports up to 64 TWAMP controllers and eight responders. Responder Light functionality 
is supported on a different IP address than the controller. Each controller or responder is associated 
with a router interface (up to 64) within the configured router entity, with the same IP address as the 
controller/responder, which is bound to an x86 Ethernet port, and assigned a VLAN.  
You can configure PMC controllers (one or more) with a total of 3000 sessions @10pps and up to 3000 
peers. You can divide the 3000 sessions between the peers, as desired. For example, all 3000 sessions 
for a single peer, or 3000 sessions for 3000 peers (i.e., one session per peer). You can configure PMC 
responders (one or more) with a total of 100 test sessions, simultaneously with the 3000 sessions 
initiated by the controllers. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
TWAMP Light 
Note 
You can activate TWAMP Light on any ETX‑2i device, as well as on PMC in 
ETX-2i. 
 
TWAMP Light architecture comprises two hosts: 
Controller  
Functions as Session-Sender  
Responder 
Functions as Session-Reflector  
 
TWAMP Controller
Session-Sender
TWAMP Responder
Session-Reflector
TWAMP Test
 
Information is exchanged between TWAMP controllers and responders, using the TWAMP Light 
mechanism, thus enabling the monitoring of sessions.  
TWAMP Light works as follows: 
1. The controller establishes a test session with the responder. 
2. After the TWAMP test session is established, the controller transmits test packets to the 
responder.  
3. The responder adds information to the packet, including Rx stamp and Tx stamp. 
4. The responder reflects the test packets to the controller.  
The controller processes the resulting measurements and calculates metrics (one way or round-trip) that 
can be displayed in test reports (see Viewing TWAMP Reports). 
In addition to viewing the metrics in the test reports, you can also view them via a network management 
system portal, such as the RADview Performance Management portal, if collection of PM statistics for 
the OAM TWAMP component is enabled (via pm-collection command in the reporting level). See 
Performance Management below for details. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Full TWAMP 
Note 
You can configure Full TWAMP only on the PMC in ETX-2i. 
Full TWAMP on ETX-2i with PMC supports the following: 
• 
IPv4 and IPv6, tagged and untagged, TWAMP frame format 
• 
PCP, DSCP, and TC (IPv6) for TWAMP generated traffic 
• 
Up to 64 TWAMP controllers and eight responders. Each controller or responder is associated 
with a router interface within the configured router entity, with the same IP address as the 
controller/responder. Controllers and responders can reside on the same VRF or on different 
VRFs (up to four). 
• 
TWAMP controller supports up to 3000 peers and up to 3000 test sessions.  
• 
Maximum rate per session: 10pps for TWAMP peers. 
• 
PMC controllers and responders each support timestamp accuracy of at least 50 usec; 80 usec 
for one-way and 2 msec for RADM. 
• 
Status and statistics 
• 
Responder functionality, at a different IP address than the controller. 
• 
Up to eight responders that together handle a total of 100 test sessions, simultaneously with the 
3000 sessions initiated by the controllers residing on the same device. 
• 
Multiple VRFs – up to four 
Full TWAMP architecture comprises two hosts: 
Controller  
Functions as Control-Client and Session-Sender  
Responder 
Functions as Session-Reflector and Server  
 
TWAMP Controller
Session Sender
TWAMP Responder
Session Reflector
TWAMP Test
TWAMP Control
Server
Control Client
Vendor 
Specific
Vendor 
Specific
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Full TWAMP consists of two inter-related protocols: 
TWAMP Control  
Layered over TCP; used to initiate, start, and stop measurement sessions.  
TWAMP Test 
Layered over UDP; used to exchange test packets between two measurement nodes.  
TWAMP Control supports the negotiation of two-way active measurement sessions in a straightforward 
manner. At session initiation, there is a negotiation of sender and receiver port numbers, and some 
attributes of the very general [RFC 2330] notion of packet type, including per-hop behavior (PHB) 
[RFC2474], which are used to support the measurement of two-way network characteristics across 
differentiated services networks.  
The initiator of the measurement session establishes a TCP connection to the default well-known port 
862, or other configurable port, on the target point and this connection remains open for the duration 
of the TWAMP Test sessions. A TWAMP server listens to this port. 
TWAMP-Control messages are transmitted only before TWAMP-Test sessions are actually started and 
after they are completed (with the possible exception of an early Stop-Sessions message).  
The TWAMP-Control protocol resolves different capability levels between the Control-Client and Server 
(e.g., mode selection – authentication/encryption). 
As the TWAMP Control protocol transmits information between controller and responder, there is no 
need to configure the responder. It is configured automatically, according to the information 
transmitted from the controller via the TWAMP Control protocol. 
Before test sessions can begin, a TCP Control connection between the TWAMP Controller and TWAMP 
Responder must be set up, as described below.  
The following table shows the steps required to configure the TWAMP generator in the PMC.  
# 
Step 
Performed In … 
1 
Configure router interfaces for management and TWAMP. 
TWAMP generator in PMC 
2 
Configure TWAMP controllers and responders. 
TWAMP generator in PMC 
3 
Configure SNMPv3. 
TWAMP generator in PMC 
4 
Configure NTP servers. 
TWAMP generator in PMC 
5 
Configure internal ports. 
ETX‑2i 
6 
Configure management and data flows, taking into account the VLANs 
used in the PMC TWAMP generator. 
ETX‑2i 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
The implementation of TWAMP Control protocol enables: 
• 
Interoperability of RAD TWAMP controller with 3rd party peers (routers, CPEs); standard RAD 
TWAMP controller can activate test sessions to 3rd party responders using a standard control 
protocol (specified in RFC5357, RFC4656) 
• 
Interoperability of 3rd party controller with RAD responders 
• 
Reduction of operation overhead at the beginning of the session, as the test can be configured 
on the controller side only. This is practical for low-scale testing; in a high-scale environment, 
especially when there are many configured peers, it is recommended to use TWAMP Light to 
avoid the TCP overhead. 
Setting Up a Connection on the Client Side 
A connection is established between a TWAMP Controller and Responder on the Client side, as follows: 
1. You request (via CLI or SNMP) to create a peer between a TWAMP Controller and a TWAMP 
Responder.  
2. You optionally configure the TCP port on which the control connection (peer) to the server is to 
be established. The default is 862. 
3. The agent validates that the TCP port value that you selected is < 49151. If not, it rejects your 
configuration attempt. 
4. The control-client connection to the TWAMP server takes place on the TCP port (default or 
configured), via the TWAMP connection setup procedure. 
5. The client automatically selects the source TCP port for the control connection in the range of 
49152–65535. This TCP port number shall be used for all control connection to different 
responders, and client shall distinguish received control traffic based on source IP address of the 
responders. Note that you cannot configure the source TCP port. 
6. The client supports only unauthenticated, unencrypted mode (‘open mode’). 
7. When the connection is established with the server, the client timestamps its local time, and 
uses it when you request peer-information (peer-level ‘show status’ command). 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Setting Up Connection on Server Side 
A connection between a TWAMP Controller and Responder is established on the Server side, as follows: 
1. You enable Control protocol at the server side by configuring the Responder without an IPPM 
type.  
2. You optionally configure the TCP port on which the server is to listen for connection attempts 
from the client. The default is 862. 
3. The agent validates that the TCP port value that you selected is < 49151. If not, it rejects the 
configuration attempt. 
4. The server supports multiple peers, initiated from different clients.  
5. The server accepts or rejects client attempt for connection.  
After a connection has been made between the client and server, the client must send to the server a 
request for each test session it wants to open on the peer, as described below.  
TWAMP Session Request on Client Side 
1. The client sends a single request for each test session it wishes to open on the peer. 
2. The source and destination UDP port of the outgoing TWAMP test packets for the requested 
sessions are conveyed to the server. 
3. The client monitors whether the test session has been accepted by the server. If it has been 
rejected, the client raises an event. 
TWAMP Session Request on Server Side 
1. The server listens to TWAMP control messages from the client. If the request is not valid, the 
server rejects it and raises an event. 
2. If the request is valid, the server sends the client the UDP port value, so that the client is aware 
that the UDP port is available at the reflector, and the sender can commence test session on this 
UDP port. This UDP port is used by the session sender as the destination UDP port for the 
transmitted test packets. 
3. If this UDP port is not available at the responder side, server sends an alternate UDP port value.  
4. Server configures the reflector to listen on this UDP port. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Starting Test Session – Client Side 
1. The client sends a request to initiate all test sessions provisioned with the server’s endpoint.  
2. If the start session request is accepted by the TWAMP server, it must commence as soon as 
possible. Otherwise, if it is rejected, the client terminates the TCP connection with the server, 
and raises an event. 
3. When you send a “no activate” command on the selected peer, or the peer’s configured test 
duration expires, all test sessions on the peer are terminated.  
Starting Test Session – Server Side 
If the server decides to acknowledge starting the test session request from the client, it configures the 
reflector to start processing the test packets to be received from all peers’ test sessions. It then sends to 
the client the acknowledgement to initiate test sessions. 
You can configure the PMC to run full TWAMP, as described in Running Test Sessions Via Controller 
Peers. 
ICMP Echo Test 
Note 
This test can be run on any ETX‑2i device, as well as on PMC in ETX-2i. 
ETX‑2i supports the two-way (round trip) ICMP Echo test, a member of the TWAMP tests. It is a useful 
tool for testing and debugging path continuity and integrity verification.  
The test, supported for both IPv4 and IPv6, is based on ICMP/ICMPv6 Echo request/reply packets. The 
ICMP Echo test is defined per peer towards a specific responder, which can be any device or workstation 
with standard IPv4/IPv6 stack that responds to standard ICMP/ICMPv6 Echo request packets. The ICMP 
peer can generate multiple ICMP Echo test sessions to the same responder; these tests differ in ICMP 
identifier, and possibly in packet length and DSCP. The ICMP peer can generate ICMP Echo tests in 
continuous and non-continuous modes. 
You do not configure peer parameters for the ICMP Echo test. The calculation mode is not configurable; 
it is automatically set to default (round-trip). The responder sequence number is also set to its default 
(off).  
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
ICMP Echo test is performed as follows: 
1. ICMP Echo IPv4/IPv6 test generates test packets based on IPv4/IPv6 ICMP Echo request 
standard packets.  
2. ICMP Echo builds test packets with: 
 
Test session identifier 
 
Controller’s transmit sequence number 
 
Controller’s transmit timestamp 
3. Controller identifies received packet according to ICMP identifier (represents test session). 
4. A packet’s round-trip delay is calculated according to received and transmitted timestamps. 
5. Loss, duplicate, and reorder are calculated according to sequence number. 
6. Metrics are calculated for roll-up window, current interval, and report interval (as defined for 
TWAMP). 
7. Metrics are collected according to the PM collection mechanism (as defined for TWAMP). 
8. ICMP Echo test events and alarms are generated as TWAMP events and alarms with the same 
definitions. 
 
Delay result (na/pass/fail) 
 
DV result (na/pass/fail)  
 
Loss result (na/pass/fail)  
UDP Echo Test 
Note 
This test can only be configured on PMC in ETX-2i. 
UDP Echo is a client-server service, defined at the UDP port level, which uses user packets for its 
measurements. As routers process pings at a lower priority than actual user packets and sometimes 
even block them, UDP Echo’s method of measuring packet transmission is more accurate than ICMP 
Echo, which uses pings for its measurements, and may delay or discard ICMP Echo requests in a manner 
that skews the measurement results.  
UDP Echo packets traverse the same intermediate nodes and logical queuing paths as the user data 
traffic of the same class of service. The class of service is dictated by DSCP code bit settings, etc., or 
other network operator specific criteria. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
UDP Echo is performed as follows: 
1. Once the peer of IPPM type udp-echo is activated, the UDP client (sender) commences sending 
periodic UDP packets (udp-echo-request) to the UDP server (reflector), according to its test-
profile attributes. It stores the transmission time for performance metric calculations. 
2. UDP server processes these packets and reflects them back to the UDP client (udp-echo-
response). UDP client validates the received UDP Echo response packet and stores the reception 
time for performance metric calculations. 
Configure UDP Echo on PMC, as follows: 
1. Configure the UDP client side: 
d. Configure the controller peer with IPPM type: udp-echo.  
e. At the peer level, configure multiple test sessions, differentiating between them by their 
UDP port. For each test session, configure the name, UDP port, test session, and DSCP. 
2. Configure the UDP server side: 
a. Configure the TWAMP responder with IPPM type: udp-echo. 
b. Under the UDP Echo responder, configure multiple test sessions for the peer, differentiating 
between them by their UDP port.  
 
Note 
The TWAMP controller and responder can be configured with UDP Echo as its 
IPPM type; however, UDP Echo can only be tested vs. third party equipment.  
RADM 
Note 
RADM can only be configured on the PMC in ETX-2i. 
Responder Agnostic Delay Measurement (RADM), a virtual ToD sync mechanism implemented at the 
controller, enables calculating one-way KPIs, even in the case that the controller and/or responder are 
not locked to an external ToD source, such as NTP, SNTP, or PTP (i.e., the controller and responder are 
not ToD-locked to each other).  
The RADM algorithm retrieves the responder’s standard TWAMP timestamps T2 and T3 every TWAMP 
test packet, calculating the time-error between the controller and responder. It then provides the 
TWAMP engine with new time error compensated T2 and T3 timestamps for further delay/PDV 
calculations.  
The RADM algorithm operates under the assumption that the network under test is symmetric in 
nature, meaning that the minimum delay experienced during the TWAMP test period is approximately 
the same on both forward (controller-to-responder) and backward (responder to controller) directions. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
As RADM operates at the TWAMP session level, the algorithm estimates and compensates for 
controller-responder time error for each TWAMP session independently, regardless of the session’s peer 
identity. This way, the calculated controller-responder time error estimation represents the true 
controller-responder time error experienced by the specific TWAMP session. 
The initial RADM algorithm convergence takes time. While converging, TWAMP provides approximate 
results. The convergence period depends mainly on the quality of the network on which the TWAMP 
test is running. For instance, it is expected that the RADM convergence period will last longer on Best-
Effort networks compared to real well-engineered carrier grade networks. In any case, initial 
convergence time should not last more than a few minutes.  
RADM, a relatively new technology, must meet both these conditions:  
• 
The clock at the responder should be free running rather than disciplined to an external 
reference (such as NTP or PTP).  
• 
The minimum physical one-way delay in the network should exceed 0.5 msec. Lower minimum 
physical one-way delays may render the estimated one-way delay inaccurate in cases that the 
network one-way delay actually falls below 0.5 msec. 
Operation with the RADM mechanism is configurable at the peer level (see Running Test Sessions Via 
Controller Peers). 
MOS On Demand 
Note 
This measurement is only displayed in the RADview Performance 
Management portal for the PMC in ETX-2i. 
Voice call quality depends on a variety of factors, including: 
• 
Type of handset and microphone 
• 
Ambient noise in the room 
• 
Network propagation delay 
• 
Loss of bandwidth in narrow-band (telephony grade) voice 
• 
Codec voice degradation 
• 
Effect of a lost packet on the decoder 
• 
Effect of a burst of packet losses 
• 
Effect of packet delay variation (as some packets may arrive too late to be used in the decoding) 

## Factory Defaults  *(p.1385)*


## Configuring TWAMP  *(p.1385)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Subjectively perceived voice quality is conventionally quantified on a scale of 1 to 5, where 5 is the 
highest score for excellent voice quality. People listen to a voice call and rate its quality. The average 
score is then recorded as the mean opinion score (MOS). 
For the PMC, RAD has a similar MOS estimation mechanism based on TWAMP PM KPIs (delay, delay-
variation, loss, and more). It estimates the MOS that a caller will experience based on measured packet 
loss ratio and one-way packet delay. Its results can be used for planning purposes, for statistical 
monitoring of customer satisfaction, and to proactively identify problematic network conditions. 
Factory Defaults 
By default, no controllers or responders are configured. 
Configuring TWAMP 
You can configure low-scale (150 sessions) TWAMP in an ETX‑2i device. 
To configure TWAMP in an ETX‑2i device, perform the following steps: 
1. In the responder device: 
a. Configure SVI port of type TWAMP (relevant for ETX‑2i TWAMP; not in PMC TWAMP in ETX-
2i), router interface, and flows. 
b. Configure relevant SNTP server(s). 
c. Configure and activate TWAMP responder and relevant test session(s). 
2. In the controller device: 
a. Configure SVI port of type TWAMP (relevant for ETX‑2i TWAMP; not in PMC TWAMP in ETX-
2i/), router interface, and flows. 
b. Configure relevant SNTP server(s) . 
c. Configure TWAMP profile(s). 
d. Configure and activate TWAMP controller, relevant peers, and test sessions. 
The TWAMP controller and responder can reside over the same router interface (configured with the 
same IP address). Over the x86 platform, the TWAMP controller and responder can be on the same 
subnet but cannot share the same IP address (cannot coexist on the same router interface). TWAMP 
controller resides on the x86 card, and TWAMP responder resides on the ETX‑2i card. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
The TWAMP controller/responder is defined to have IP connectivity when the following conditions are 
met: 
• 
Controller/responder local IP address is configured. 
• 
Associated router interface is configured and administratively enabled. 
• 
Controller/responder is bound to a port (if TWAMP mode is layer-2 E-Line). 
• 
Related SVI and flows are configured (TWAMP in ETX‑2i) 
• 
Related flows are configured (TWAMP in PMC of ETX-2i) 
Configuring Controllers 
 To configure a TWAMP Light controller of an ETX‑2i device: 
1. Navigate to configure oam twamp. 
2. Enter controller <name> [<number>] [light] [l2-probe]  
Note 
The parameter l2-probe specifies that the controller is working in mode 
Layer-2 E-Line service (see Functional Description). 
The config>oam>twamp>controller(<name>/light)# prompt is displayed. 
3. Perform the required tasks according to the following table.  
 To configure a TWAMP controller in PMC (relevant for ETX-2i with PMC): 
1. Navigate to configure oam twamp. 
2. Enter controller <name> [<number>  
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Binding controller to a port 
bind ethernet <port-index> 
bind logical-mac <port-number> 
bind pcs <port-number> 
Can bind controller to a port, only if 
controller is in layer-2 probe mode. 
Entering no bind deletes the 
definitions of the TWAMP ingress and 
egress ports. 
Note: It is only possible to bind a PMC 
responder to an Ethernet port 
(relevant for PMC in ETX-2i). 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Configuring controller local IP 
address 
local-ip-address <ip-address> 
Possible values:  
IPv4 or IPv6 network address 
Defining peer entity 
(corresponding to responder), 
to run TWAMP test sessions 
peer <ip-address> twamp-light | 
icmp-echo | twamp | udp-echo 
twamp (Full TWAMP, which includes 
TWAMP Light and TWAMP control) 
and udp-echo options are only 
relevant for configuration of PMC in 
ETX-2i. 
See Running Test Sessions Via 
Controller Peers. 
Associating controller with a 
router that contains a suitable 
router interface 
router-entity <number> 
The parameter <number> is the router 
number, in which a router interface 
must be configured with the same IP 
address as local-ip-address. 
Possible values:  
1-<maximum number of router 
entities> 
Associating controller with 
VLAN 
vlan-tag vlan <vlan> [p-bit <p-bit>] 
[inner-vlan <inner-vlan>] 
[inner-p-bit <inner-p-bit>] 
Can associate controller with VLAN 
only if controller is in layer-2 probe 
mode. 
Possible values for vlan, inner-vlan:  
0-4095 
Possible values for p-bit, inner p-bit:  
0-7 
Note: This parameter is not relevant 
for configuration of PMC in ETX-2i. 
Administratively enabling or 
disabling the controller 
no shutdown 
shutdown 
Enter shutdown to administratively 
disable the controller. 
You should enable the controller only 
after the responder has been 
configured and enabled. 
Viewing controller status 
show status 
 
Defining the TCP port number 
for the TWAMP control session 
tcp-port 
Possible values: 862 (default) 
                             1024–65535 
Note: This parameter is available only 
for ETX-2i with PMC when the peer 
test session is TWAMP. 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Running Test Sessions Via Controller Peers 
On an ETX‑2i device, you can configure up to 150 test sessions of TWAMP Light (default) and/or ICMP 
Echo protocols on each peer of a controller.  
On the PMC of an ETX-2i device, you can configure up to 3000 test sessions of TWAMP Light, Full 
TWAMP, ICMP Echo, and/or UDP Echo on each peer of a controller.   
This section describes how to define the peer entity for a group of TWAMP test sessions. 
Note 
On the PMC, before activating a TWAMP session (RTT or RADM), verify that 
the NTP client on board has moved into LOCKED state. 
 To configure TWAMP test sessions in ETX‑2i: 
1. Navigate to configure oam twamp controller <name> [<number>] light [l2-probe] peer 
<ip-address> [twamp-light | icmp-echo]. 
The config>oam>twamp>controller (<name>/light)> peer(<ip-address>) [twamp-light | icmp-
echo]# prompt is displayed. 
2. Perform the required tasks according to the following table. 
 To configure TWAMP test sessions in PMC (relevant for ETX-2i with PMC): 
1. Navigate to configure oam twamp controller <name> [<number>] peer <ip-address> [twamp-
light | icmp-echo | twamp | udp-echo]. 
The config>oam>twamp>controller (<name>)>peer(<ip-address> twamp-light [twamp-light | 
icmp-echo | twamp | udp-echo]# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Activating all configured test 
sessions in one-time mode 
activate duration <minutes> 
The tests run for the specified amount 
of time. 
Enter no activate to deactivate the one-
time (non-continuous) command. 
Possible values for minutes: 1-10080 
Activating all configured test 
sessions in continuous mode 
activate continuous 
The tests run until they are stopped. 
Enter no activate to deactivate the 
continuous command. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining the type of 
calculation for the TWAMP 
metrics 
calculation-mode { round-trip | one-way 
|one-way-radm } 
round-trip: TWAMP controller peer 
calculates standard TWAMP metrics and 
partial one-way metrics: 
• Two-way metrics – availability, loss, 
delay, PDV (packet delay variation), 
IPDV (inter-packet delay variation) 
• Partial one-way metrics – IPDV, 
duplicate packets, reordered 
packets, fragmented packets (no 
one-way delay or PDV metrics) 
• One-way loss and availability   
one-way: TWAMP controller peer 
calculates one-way metrics: 
• One-way metrics – delay, PDV, IPDV, 
duplicate packets, reordered 
packets, fragmented packets 
• One-way loss and availability 
one-way-radm: For configuration of 
PMC on ETX-2i. Same as enabled KPI 
one-way calculation when responder 
and/or controller are not ToD locked to 
an external reference, such as NTP.  
The TWAMP controller peer calculates 
responder agnostic one-way metrics. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
 
 
Note: 
• This parameter is masked when 
using ICMP Echo protocol, as its 
value is always round-trip (the 
default).  
• This parameter can be changed only 
if there is no active test session. 
• You can set one-way mode only if 
both the controller and responder 
are ToD locked.  
• One-way loss and availability is 
available only if responder is 
configured to transmit an 
independent sequence number 
(tx-seq-num enabled), and controller 
is configured accordingly 
(responder-seq-num enabled). 
• One-way delay and PDV metrics are 
available only if tx-extended-info 
has been enabled in responder, and 
it sent indication that its ToD (Time 
of Day) is synchronized; the metrics 
are accurate only if the controller 
ToD is also synchronized. 
• The fragmented packet count in the 
forward direction (controller to 
responder) is available only if 
tx-extended-info has been enabled 
in the responder, and it sent 
indication of fragmentation. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Specifying whether the 
responder transmits an 
independent sequence 
number 
responder-seq-num 
no responder-seq-num 
Note: 
• The controller calculates one-way 
loss and availability only if this is 
enabled.  
• The corresponding responder must 
be configured to transmit the 
responder sequence number (via 
command tx-seq-num). 
• This parameter is masked when 
using ICMP Echo protocol, as its 
value is always off (the default). 
Defining the TCP port number 
for the TWAMP control 
session 
tcp-port 
Possible values: 862 (default) 
                             1024–65535 
Note: This parameter is available only 
for configuration of PMC peer with 
TWAMP test session in ETX-2i with PMC. 
Configuring test session 
test-session <number> 
[name <name-string>] 
[udp-port <udp-port-number>] 
[test-profile <profile-name>] 
[dscp <dscp-number>] 
The UDP and DSCP can be used to 
distinguish between test sessions. 
UDP port number: 1–65535 
Test profile name: Up to 32 characters 
DSCP number: 0–63 (default: 63) 
Note:  
• The udp-port parameter is masked 
when using the ICMP Echo protocol. 
• The udp-port parameter is optional, 
when configuring PMC peer with 
TWAMP test session in ETX-2i with 
PMC. 
Viewing test report 
show report <name> all 
show report <name> current 
show report <name> interval 
<interval-num> 
See Viewing TWAMP Reports. 
Viewing summary of test 
reports 
show summary-report 
See Viewing TWAMP Reports. 
Viewing test status 
show status  
See Viewing TWAMP Status. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuring Test Profiles 
You can configure test profiles to associate with a test session. 
 To configure TWAMP test profiles: 
1. Navigate to configure oam twamp. 
2. To configure a test profile, enter: 
profile <name> [<number>]  
The config>oam>twamp>profile(<name>) prompt# is displayed. 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Defining delay threshold in 
microseconds 
delay-threshold <μs> 
 
Configuring delay variation 
event type to define whether 
the PDV or IPDV metric is 
used for the delay threshold  
delay-variation-event-type { pdv | ipdv } 
pdv – Packet delay variation metric 
ipdv – Inter-packet delay variation 
metric 
See RFC 5481 for details on these 
metrics. 
Defining delay variation 
threshold in microseconds 
delay-variation-threshold <μs> 
 
Defining test packet loss 
timeout in microseconds 
loss-timeout <msec> 
 
Defining test session loss-
ratio-threshold in ppm 
(packet per million) 
loss-ratio-threshold <ppm> 
Possible values: 1000–10000 ppm 
Default: 1000 ppm 
Defining test packet payload 
length in bytes 
payload-length <bytes> 
Possible values: 37–1472 
Defining test profile packet 
transmit rate in PPS 
transmit-rate <pps> 
Note: In layer-2 probe mode, 150 pps is 
possible only if the test packet payload 
length is not greater than 170 bytes. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuring Responders 
This section describes how to create a TWAMP responder entity. 
 To configure a TWAMP Light responder of an ETX‑2i device: 
1. Navigate to configure oam twamp. 
2. To configure the TWAMP Light responder, enter: 
responder <name> [<number>] [light] [l2-probe]  
Note 
The parameter l2-probe specifies that the responder is working in mode 
Layer-2 E-Line service (see Functional Description). 
The config>oam>twamp>responder(<name>/light)# prompt is displayed. 
3. Perform the required tasks according to the following table. 
 To configure a TWAMP responder in PMC (relevant for ETX-2i with PMC): 
1. Navigate to configure oam twamp. 
The config>oam>twamp# prompt is displayed. 
2. To configure the TWAMP responder, enter: 
responder <name> [<number>  
The config>oam>twamp>responder(<name># prompt is displayed. 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Binding responder to a port 
bind ethernet <port-index> 
bind logical-mac <port-number>bind pcs 
<port-number> 
Can bind responder to a port, only if 
responder is in layer-2 probe mode. 
Entering no bind deletes the definitions 
of the TWAMP ingress and egress ports. 
Note: It is only possible to bind a PMC 
responder to an Ethernet port (relevant 
for ETX-2i with PMC). 
Defining whether to provide 
indication of fragmentation in 
forward path, and status of 
ToD (Time Of Day) 
synchronization 
tx-extended-info 
no tx-extended-info 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Configuring responder local IP 
address 
local-ip-address <ip-address> 
Possible values:  
0 (default) – no IP address 
IPv4 or IPv6 network address 
Associating responder with a 
router that contains a suitable 
router interface 
router-entity <number> 
The parameter <number> is the router 
number, in which a router interface 
must be configured with the same IP 
address as local-ip-address. 
Possible values:  
0 (default) – no router entity 
1-Maximum number of router entities 
Associating responder with a 
test session 
test-session <number> 
[name <name-string>] 
[udp-port <udp-port-number>] 
Entering no test-session <number> 
[name <name-string>] deletes the test 
session entity. 
Note: 
• For TWAMP Light only 
• udp-port is masked if responder 
IPPM type is TWAMP (relevant for 
PMC configuration in ETX-2i with 
PMC). 
Defining whether responder 
transmits an independent 
sequence number, rather 
than copying the received 
sequence number into the 
transmitted packet  
tx-seq-num 
no tx-seq-num 
Note: 
• The responder independent 
sequence number can be used by 
the controller to calculate one-way 
loss and availability. 
• The corresponding controller must 
be configured to indicate that the 
responder sequence number is being 
transmitted (via command 
responder-seq-num). 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Associating responder with 
VLAN 
vlan-tag vlan <vlan> [p-bit <p-bit>] 
[inner-vlan <inner-vlan>] 
[inner-p-bit <inner-p-bit>] 
Can associate responder with VLAN only 
if responder is in layer-2 probe mode. 
Possible values for vlan, inner-vlan:  
0-4095 
Possible values for p-bit, inner p-bit: 0-7 
Entering no vlan deletes VLANs for L2 
service definition in L2 probe mode. 
The p-bit in the transmitted frame can 
be either configured (fixed, default 
option) or copied from received frame. 
Note: This parameter is not relevant for 
configuration of PMC in ETX-2i. 
Administratively enabling or 
disabling the responder 
no shutdown 
shutdown 
Enter shutdown to administratively 
disable the responder. 
Defining TCP port number for 
the TWAMP control session. 
tcp-port 
Relevant for PMC configuration in  
ETX-2i.  
Possible values: 862 (default) 
                             1024–65535 
Defining TWAMP test session 
inactivity timeout 
reflector-timeout 
no reflector-timeout 
Relevant for PMC configuration in  
ETX-2i. 
Possible values: 0, 60–3600 seconds 
Default: 900 
Defining TWAMP control 
session inactivity timer 
server-timeout 
no server-timeout 
Relevant for PMC configuration in  
ETX-2i.  
Possible values: 0, 60–3600 seconds 
Default: 900 
Viewing responder status 
show status 
See  
Viewing TWAMP Status. 
 
 

## Viewing TWAMP Status  *(p.1396)*


## Viewing TWAMP Reports  *(p.1396)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing TWAMP Status 
You can view the status of the controller, responder, or peer test sessions, in any device, as well as in 
the PMC of ETX-2i with PMC, using the show status command in the following levels.  
Controller status 
show status in level config oam twamp controller 
Responder status 
show status in level config oam twamp responder 
Peer test sessions status 
show status in level config oam twamp controller peer 
Viewing TWAMP Reports 
After you configure round-trip or one-way metrics calculation for each peer via command 
calculation-mode (see Running Test Sessions Via Controller Peers) you can generate the TWAMP 
report. 
The TWAMP controller calculates performance measurement metrics according to the received test 
packets for each peer and its active test sessions. The metrics are recalculated every minute. In the 
TWAMP report, you can view the metrics for the current interval, selected interval, or all intervals. You 
can also view the metrics via the RADview Performance Management portal if the TWAMP PM 
collection is enabled (see Performance Management below for details).  
 To view a summary report of all peer test sessions: 
1. Navigate to configure oam twamp controller peer. 
2. Enter show summary-report. 
 To view a report of all intervals in a specific peer test session: 
1. Navigate to configure oam twamp controller peer. 
2. Enter show report <name> all. 
 To view a report of the current interval in a specific peer test session: 
1. Navigate to configure oam twamp controller peer. 
2. Enter show report <name> current. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To view a report of a specific interval in a specific peer test session: 
1. Navigate to configure oam twamp controller peer. 
2. Enter show report <name> interval <interval-num>. 
The following table lists the metrics that are displayed in the TWAMP reports, subject to the restrictions 
specified above for the calculation modes. See  Viewing TWAMP Reports for examples of TWAMP 
reports. 
Counter 
Description 
Tx Packets Fwd 
Number of packets transmitted in forward direction (controller to responder)  
Tx Packets Back 
Number of packets transmitted in backward direction (responder to controller) 
Loss Packets Fwd 
Number of packets lost in forward direction, calculated by Tx Packets Fwd – 
Rx valid count 
Loss Packets Back 
Number of packets lost in backward direction, calculated by Tx Packets Back – 
Rx valid count 
Loss Ratio Fwd 
Loss Packets Fwd divided by Tx Packets Fwd, converted to a percentage 
Loss Ratio Back 
Loss Packets Back divided by Tx Packets Back, converted to a percentage 
Availability Count Fwd (sec) 
Number of available seconds in forward direction. A (forward) minute is declared 
as unavailable if it has more than 75% packet loss in forward direction, therefore it 
is available if packet loss in forward direction is 25% or less. When a minute is 
declared unavailable, the delay, delay variation, loss measurements, and their 
derived metrics are ignored for that minute.  
Availability Count Back (sec)  
Number of available seconds in backward direction. A (backward) minute is 
declared as unavailable if it has more than 75% packet loss in backward direction 
therefore it is available if packet loss in backward direction is 25% or less. When a 
minute is declared unavailable, the delay, delay variation, loss measurements, and 
their derived metrics are ignored for that minute.  
Duplicate Packets Fwd 
Number of duplicate packets in forward direction. A packet is considered duplicate 
(forward) if its controller sequence number or controller Tx timestamp matches 
that of a previously received packet in forward direction. 
Duplicate Packets Back 
Number of duplicate packets in backward direction. A packet is considered 
duplicate (backward) if its responder Tx timestamp matches that of a previously 
received packet in backward direction. 
Duplicate Ratio Fwd 
Duplicate Packets Fwd divided by Tx Packets Fwd, converted to a percentage 
Duplicate Ratio Back 
Duplicate Packets Back divided by Tx Packets Back, converted to a percentage 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Counter 
Description 
Reordered Packets Fwd 
Number of reordered packets in forward direction. A packet is considered 
reordered (forward) if its controller sequence number or controller Tx timestamp is 
smaller than that of a previously received packet in forward direction. 
Reordered Packets Back 
Number of reordered packets in backward direction. A packet is considered 
reordered (backward) if its responder sequence number is smaller than that of a 
previously received packet in backward direction. 
Reordered Ratio Fwd 
Reordered Packets Fwd divided by Tx Packets Fwd, converted to a percentage 
Reordered Ratio Back 
Reordered Packets Back divided by Tx Packets Back, converted to a percentage 
Fragmented Packets Fwd 
Number of fragmented packets in forward direction. When the TWAMP responder 
receives a fragmented packet, when it reflects it to the controller, the responder 
sends indication of fragmentation, if tx-extended-info was enabled. When this 
indication is received, the controller increments the Fragmented Packets Fwd 
counter.  
Fragmented Packets Back 
Number of fragmented packets in backward direction. When the TWAMP 
controller recognizes a fragmented packet, it increments the Fragmented Packets 
Back counter. 
Delay-Fwd Threshold Crossing 
Count 
Number of packets in forward direction with delay larger than the delay threshold 
configured for the corresponding test profile 
Delay-Back Threshold Crossing 
Count 
Number of packets in backward direction with delay larger than the delay 
threshold configured for the corresponding test profile 
Delay-Fwd Min (ms) 
Minimum of packet delay values in forward direction 
Delay-Fwd Max (ms) 
Maximum of packet delay values in forward direction 
Delay-Fwd Average (ms) 
Average of packet delay values in forward direction 
Delay-Back Min (ms) 
Minimum of packet delay values in backward direction 
Delay-Back Max (ms) 
Maximum of packet delay values in backward direction 
Delay-Back Average (ms) 
Average of packet delay values in backward direction 
PDV-Fwd Max (ms) 
Maximum of PDV (Packet Delay Variation) values in forward direction. Packet Delay 
Variation is calculated according to ITU-T Y.1540, by subtracting the minimum 
delay from the 99.9% percentile of the delay values 
PDV-Fwd Average (ms) 
Average of PDV (Packet Delay Variation) values in forward direction, calculated by 
subtracting Delay-Fwd Min from Delay-Fwd Average 
PDV-Back Max (ms) 
Maximum of PDV (Packet Delay Variation) values in backward direction 
PDV-Back Average (ms) 
Average of PDV (Packet Delay Variation) values in backward direction 

## Examples  *(p.1399)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Counter 
Description 
IPDV-Fwd Max (ms) 
Maximum of IPDV (Inter Packet Delay Variation) values in forward direction. Inter 
Packet Delay Variation is calculated according to RFC 5481, from the variations of 
the delays between valid packets. 
IPDV-Fwd Average (ms) 
Average of IPDV (Inter Packet Delay Variation) values in forward direction 
IPDV-Back Max (ms) 
Maximum of IPDV (Inter Packet Delay Variation) values in backward direction  
IPDV-Back Average (ms) 
Average of IPDV (Inter Packet Delay Variation) values in backward direction 
Examples 
Configuring TWAMP in Layer-2 E-Line Service Mode 
This example illustrates configuring TWAMP in mode Layer-2 E-Line service: 
• 
Controller with IP address = 11.11.11.1 
• 
Responder with IP address = 11.11.11.2 
 To configure the responder: 
• 
Router: Associate Interface 2 with SVI 2. 
• 
Flows between Ethernet ports 0/1 and 0/3: 
 
VLAN 100 
 
No Policer 
• 
Test session: 
 
UDP port 999 
exit all 
#*********Configure SVI for TWAMP  
configure  
  port svi 2 twamp 
    no shutdown 
    exit  
  exit 
 
#********* Configure classifier for VLAN 100 
  flows 
    classifier-profile v100 match-any  
    match vlan 100 
    exit 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#********* Configure flows between ETH 0/1 & 0/3 
    flow E1toE3 
      classifier v100 
      ingress-port ethernet 0/1 
      egress-port ethernet 0/3 queue 0 block 0/1 
      no policer 
      no shutdown 
      exit  
 
    flow E3toE1 
      classifier v100 
      ingress-port ethernet 0/3 
      egress-port ethernet 0/1 queue 0 block 0/1 
      no policer 
      no shutdown 
      exit 
    exit 
 
#*********Configure router 1 with interface 2 for TWAMP 
  router 1 
    interface 2 
      address 11.11.11.2/24 
      address 11:11:11::2/64 
      bind svi 2 
      no shutdown 
      exit  
    exit  
 
#*********Configure TWAMP responder  
  oam  
    twamp  
      responder 1 light l2-prob 
      bind ethernet 0/1 
      vlan-tag vlan 100 
      router-entity 1 
      local-ip-address 11.11.11.2 
      test-session 1 udp-port 999 
      tx-extended-info 
      tx-seq-num 
      no shutdown 
      exit all 
save 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure the controller: 
• 
Router: Associate Interface 2 with SVI 2. 
• 
Flows between Ethernet ports 0/1 and 0/3: 
 
VLAN 100 
 
No Policer 
• 
Test session: 
 
Profile with payload length 150, and loss timeout 1 second 
 
UDP port 999 
 
DSCP 0 
exit all 
#*********Configure SVI for TWAMP  
configure  
  port svi 2 twamp 
    no shutdown 
    exit 
  exit 
 
#********* Configure classifier for VLAN 100 
  flows 
    classifier-profile v100 match-any  
      match vlan 100 
      exit 
 
#********* Configure flows between ETH 0/1 & 0/3 
    flow E1toE3 
      classifier v100 
      ingress-port  ethernet 0/1 
      egress-port ethernet 0/3 queue 0 block 0/1 
      no policer 
      no shutdown 
      exit  
 
    flow E3toE1 
      classifier v100 
      ingress-port ethernet 0/3 
      egress-port ethernet 0/1 queue 0 block 0/1 
      no policer 
      no shutdown 
      exit 
    exit 
 
#*********Configure router 1 with interface 2 for TWAMP  
  router 1 
    interface 2 
      address 11.11.11.1/24 
      address 11:11:11::1/64 
ETX-2i Devices 
8. Monitoring and Diagnostics 
      bind svi 2 
      no shutdown 
      exit 
    exit 
 
#*********Configure TWAMP profile 
  oam  
    twamp  
      profile twp1 
        payload-length 150  
        loss-timeout 1000000 
        exit  
 
#*********Configure TWAMP controller 
      controller 1 light l2-probe 
        bind ethernet 0/1 
        vlan-tag vlan 100 
        router-entity 1 
        local-ip-address 11.11.11.1 
        peer 11.11.11.2 
          test-session 1 name twamp1 udp-port 999 test-profile twp1 dscp 0 
          calculation-mode round-trip 
          responder-seq-num 
          exit 
        no shutdown 
        exit all 
save 
Configuring TWAMP in Layer-2 E-LAN Service Mode 
This example illustrates configuring TWAMP in mode Layer-2 E-LAN service: 
• 
Controller with IP address = 11.11.101.6 
• 
Responder with IP address = 11.11.101.116 
 To configure the responder: 
• 
Bridge – Activate ports 1, 2, and 3; associate VLAN 1. 
• 
Router – Associate Interface 2 with SVI 2. 
• 
Flows between Ethernet port 1/1 and bridge port 1: 
 
Match VLAN 1 
 
No Policer 
 
Reverse direction 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
• 
Flows between Ethernet port 0/1 and bridge port 2: 
 
Match VLAN 1 
 
No Policer 
• 
Flows between bridge port 3 and SVI 2: 
 
Bridge port to SVI – Match VLAN 1, and pop VLAN. 
 
SVI to bridge port – Match all traffic, and push VLAN 1. 
 
No Policer 
• 
Test session: 
 
UDP port 900 
exit all 
#*********Configure SVI for TWAMP  
configure  
  port svi 2 twamp 
    no shutdown 
    exit  
  exit 
 
#*********Configure bridge ports 
configure bridge 1   
    port 1 no shutdown 
    port 2 no shutdown 
    port 3 no shutdown 
    vlan 1 
 exit all  
 
#*********Configure classifier for VLAN 1 
configure  
  flows 
    classifier-profile v1 match-any  
    match vlan 1 
    exit 
 
#*********Configure flow between Ethernet port 1/1 and bridge port 1 
     
    flow BP1to E1_1 
      classifier v1 
      ingress-port bridge-port 1 1 
      egress-port ethernet 1/1 block 0/1 
      reverse-direction 
      no policer 
      no shutdown 
      exit 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#*********Configure flows between Ethernet port 0/1 and bridge port 2 
    flow E0_1toBP2 
      classifier v1 
      ingress-port ethernet 0/1 
      egress-port bridge-port 1 2 
      no policer 
      no shutdown 
      exit  
 
    flow BP2toE0_1 
      classifier v1 
      ingress-port bridge-port 1 2 
      egress-port ethernet 0/1 block 0/1 
      no policer 
      no shutdown 
      exit 
 
#*********Configure flows between bridge port 3 and SVI 2  
    flow BP3toSVI2 
      classifier v1 
      ingress-port bridge-port 1 3 
      egress-port svi 2 
      vlan-tag pop vlan 
      reverse-direction 
      no policer 
      no shutdown 
      exit  
 
    flow SVI2toBP3 
      classifier all 
      ingress-port svi 2 
      egress-port bridge-port 1 3 
      vlan-tag push vlan 1 p-bit fixed 0 
      no policer 
      no shutdown 
      exit 
    exit 
 
#*********Configure router 1 with interface 2 for TWAMP 
  router 1 
    interface 2 
      address 11.11.101.116/24 
      address 11:11:101::116/64 
      bind svi 2 
      no shutdown 
      exit  
    exit  
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#*********Configure TWAMP responder  
  oam  
    twamp  
      responder 1 light 
      router-entity 1 
      local-ip-address 11.11.101.116 
      test-session 1 udp-port 900 
      tx-extended-info 
      tx-seq-num 
      no shutdown 
      exit all 
save 
 To configure the controller: 
• 
Bridge – Activate ports 1, 2, and 3; associate VLAN 1. 
• 
Router – Associate Interface 2 with SVI 2. 
• 
Flows between Ethernet port 1 and bridge port 1, and Ethernet port 3 and bridge port 2: 
 
Match VLAN 1 
 
No Policer 
 
Reverse-direction 
• 
Flows between bridge port 3 and SVI 2: 
 
Bridge port to SVI: Match VLAN 1, and pop VLAN. 
 
SVI to bridge port: Match all traffic, and push VLAN 1. 
 
No Policer 
• 
Test session: 
 
Profile with default values 
 
UDP port 900 
 
DSCP 22 
exit all 
#*********Configure SVI for TWAMP  
configure  
  port svi 2 twamp 
    no shutdown 
    exit  
  exit 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#*********Configure bridge ports 
configure bridge 1   
    port 1 no shutdown 
    port 2 no shutdown 
    port 3 no shutdown 
    vlan 1 
 exit all  
 
#*********Configure classifier for VLAN 1 
configure  
  flows 
    classifier-profile v1 match-any  
    match vlan 1 
    exit 
 
#*********Configure flow between Ethernet port 1 and bridge port 1 
 
    flow BP1to E1 
      classifier v1 
      ingress-port bridge-port 1 1 
      egress-port ethernet 1 block 0/1 
      no policer 
      reverse-direction  
      no shutdown 
      exit 
 
#*********Configure flow between Ethernet port 3 and bridge port 2 
     
    flow BP2to E3 
      classifier v1 
      ingress-port bridge-port 1 2 
      egress-port ethernet 3 block 0/1 
      no policer 
      reverse-direction 
      no shutdown 
      exit 
 
#*********Configure flows between bridge port 3 and SVI 2  
    flow BP3toSVI2 
      classifier v1 
      ingress-port bridge-port 1 3 
      egress-port svi 2 
      vlan-tag pop vlan 
      no policer 
      no shutdown 
      exit  
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
    flow SVI2toBP3 
      classifier all 
      ingress-port svi 2 
      egress-port bridge-port 1 3 
      vlan-tag push vlan 1 p-bit fixed 0 
      no policer 
      no shutdown 
      exit 
    exit 
 
#*********Configure router 1 with interface 2 for TWAMP 
  router 1 
    interface 2 
      address 11.11.101.6/24 
      address 11:11:101::6/64 
      bind svi 2 
      no shutdown 
      exit  
    exit  
 
#*********Configure TWAMP profile with default values 
  oam  
    twamp  
      profile twp1 
        exit  
 
#*********Configure TWAMP controller 
      controller 1 light  
        router-entity 1 
        local-ip-address 11.11.101.6 
        peer 11.11.101.116 
          test-session 1 name twamp1 udp-port 900 test-profile twp1 dscp 22 
          calculation-mode round-trip 
          responder-seq-num 
          exit 
        no shutdown 
        exit all 
save 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuring TWAMP in Layer-3 Mode 
This example illustrates configuring TWAMP in Layer-3 mode: 
• 
Controller with IP address=12.12.12.1 
• 
Responder with IP address=22.22.22.1 
Note 
This example assumes for the routers in the controller and responder: 
• 
In the controller, the next hop to reach the 22.22.22.0/24 subnet is 
12.12.12.2  
• 
In the responder, the next hop to reach the 12.12.12.0/24 subnet is 
22.22.22.2 
 To configure the responder: 
• 
Router: Associate Interface 2 with SVI 2. 
• 
Flows between Ethernet port 0/1 and SVI 2: 
 
Untagged traffic from Ethernet port 0/1 to SVI 2 
 
Untagged traffic from SVI 2 to Ethernet port 0/1 
 
No Policer 
• 
Test session: 
 
UDP port 999 
exit all 
#*********Configure SVI for TWAMP  
configure  
  port  
    svi 2 twamp 
      no shutdown 
    exit 
  exit 
 
#********* Configure classifier for untagged traffic 
  flows 
    classifier-profile untagged match-any  
      match untagged 
      exit 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#********* Configure flows between Eth port 0/1 & SVI 2 
    flow E1toSVI2 
      classifier untagged 
      ingress-port ethernet 0/1 
      egress-port svi 2 queue 0 
      no policer 
      no shutdown 
      exit 
 
    flow SVI2toE1 
      classifier untagged 
      ingress-port svi 2 
      egress-port ethernet 0/1 queue 0 block 0/1 
      no policer 
      no shutdown 
      exit 
    exit 
 
#*********Configure router with interface 2 for TWAMP 
  router 1 
    interface 2 
      address 22.22.22.1/24 
      address 22:22:22::1/64 
      bind svi 2 
      no shutdown 
      exit  
    static-route 12.12.12.0/24 address 22.22.22.2 
    exit 
 
#*********Configure TWAMP responder 
  oam  
    twamp  
      responder 1 light 
      router-entity 1 
      local-ip-address 22.22.22.1 
      test-session 1 name "twamp1" udp-port 999 
      tx-extended-info 
      tx-seq-num 
      no shutdown 
      exit all 
save 
 To configure the controller: 
• 
Router: Associate Interface 2 with SVI 2. 
• 
Flows between Ethernet port 0/1 and SVI 2: 
 
Untagged traffic from Ethernet port 0/1 to SVI 2 
 
Untagged traffic from SVI 2 to Ethernet port 0/1 
 
No Policer 
ETX-2i Devices 
8. Monitoring and Diagnostics 
• 
Test session: 
 
Profile with payload length 150, and loss timeout 1 second 
 
UDP port 999 
 
DSCP 0 
exit all 
#*********Configure SVI for TWAMP  
configure  
  port  
    svi 2 twamp 
      no shutdown 
    exit 
  exit 
 
#********* Configure classifier for untagged traffic 
  flows 
    classifier-profile untagged match-any  
      match untagged 
      exit 
 
#********* Configure flows between Eth port 0/1 & SVI 2 
    flow E1toSVI2 
      classifier untagged 
      ingress-port ethernet 0/1 
      egress-port svi 2 queue 0 
      no policer 
      no shutdown 
      exit 
 
    flow SVI2toE1 
      classifier untagged 
      ingress-port svi 2 
      egress-port ethernet 0/1 queue 0 block 0/1 
      no policer 
      no shutdown 
      exit 
    exit 
 
#*********Configure router with interface 2 for TWAMP 
  router 1 
    interface 2 
      address 12.12.12.1/24 
      address 12:12:12::1/64 
      bind svi 2 
      no shutdown 
      exit 
    static-route 22.22.22.0/24 address 12.12.12.2 
    exit 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#*********Configure TWAMP profile 
  oam  
    twamp  
      profile twp1 
        payload-length 150  
        loss-timeout 1000000 
        exit  
 
#*********Configure TWAMP controller 
      controller 1 light 
        router-entity 1 
        local-ip-address 12.12.12.1 
          peer 22.22.22.1 
          test-session 1 name twamp1 udp-port 999 test-profile twp1 dscp 0 
          calculation-mode one-way 
          responder-seq-num 
          exit 
        no shutdown 
        exit all 
save 
Configuring Management for TWAMP in PMC (relevant for ETX-2i with PMC) 
This example illustrates configuring the ETX‑2i NID and x86 card for management, according to the flows 
shown below.  
 
ETX-2i
MNG Traffic
VLAN 4094 
SVI 1 
ETX-2i
x86
NNI Port 1 
Internal 
Port 6
Bridge 1 
Push / PoP
VLAN 4094 
Eth 1
Eth 2
Push / PoP
VLAN 4094 
Internal 
Port 5
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure management in ETX‑2i: 
• 
SVI port 1, bridge 
• 
Management VLAN 4094 
• 
Flows: 
 
Flows between bridge port and Ethernet port 1, pushing/popping VLAN 4094 
 
Flows between bridge port and internal Ethernet port 6, with criterion VLAN 4094 
 
Flows between bridge port and SVI port 1, pushing/popping VLAN 4094 
 
Router interface with IP address 192.168.205.5, bound to SVI port 1 
#********* Configure SVI ********* 
exit all 
configure port 
    svi 1 
      no shutdown 
    exit all 
 
********* Configure bridge and VLAN********* 
configure bridge 1   
    port 1 no shutdown 
    port 6 no shutdown 
    port 9 no shutdown 
    vlan 4094 
exit all 
 
#********* Configure flows ********* 
configure flows  
    classifier-profile all match-any match all 
    classifier-profile untagged match-any match untagged 
    classifier-profile v4094 match-any match vlan 4094 
 
    flow eth1_bp1_untagged 
      classifier  untagged 
      ingress-port  ethernet  1 
      egress-port bridge-port 1 1 
      vlan-tag push vlan 4094 p-bit fixed 0 
      no policer 
      reverse-direction block 0/1 
      no shutdown 
    exit  
 
    flow int_eth6_bp6_v4094 
      classifier  v4094 
      ingress-port int-ethernet 6 
      egress-port bridge-port 1 6 
      no policer 
      reverse-direction block 0/1 
      no shutdown 
    exit  
ETX-2i Devices 
8. Monitoring and Diagnostics 
    flow svi1_bp9_all 
      classifier  all 
      ingress-port  svi 1 
      egress-port bridge-port 1 9 
      no policer 
      vlan-tag push vlan 4094 p-bit fixed 0 
      reverse-direction 
      no shutdown 
    exit  
 
#********* Configure router ********* 
configure router 1 
    interface 1 
      address 192.168.205.5/24 
      bind svi 1 
      no shutdown 
exit all 
 
#********* Save configuration ********* 
save 
 To configure in x86 card: 
 
Router interface with IP address 192.168.205.6, bound to Ethernet port 1 and VLAN 4094 
Note 
• 
The ETX‑2i internal Ethernet port 6 is connected to Ethernet port 1 on the 
x.86 card.  
• 
Configure the x86 card by accessing the x86 remote terminal via 
command configure chassis ve-module remote-terminal (refer to Remote 
Terminal in the Management and Security chapter). 
 
#********* Configure router ********* 
exit all 
configure router 1 
    interface 1 
      address 192.168.205.6/24 
      bind ethernet 0/1 
      vlan 4094 
      no shutdown 
exit all 
 
#********* Save configuration ********* 
save 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuring TWAMP in PMC (relevant for ETX-2i with PMC) 
This example illustrates configuring TWAMP in ETX‑2i and the x86 card. 
 To configure TWAMP in the x86 card: 
• 
Router interfaces: 
 
Router interface 1: Management, IP address 172.18.141.37, VLAN 4094 
 
Router interface 2: TWAMP, IP address 11.11.101.6, bound to Ethernet port 1, VLAN 101 
• 
TWAMP controller: 
 
IP address 11.11.101.6 
 
Peer IP address 33.33.116.6 
 
Router interface 2 
• 
SNMPv3 target and traps 
• 
NTP servers 
#********* Configure router interface for management ********* 
exit all 
    configure router 1 
    interface 1 
      bind ethernet 0/1 
      vlan 4094 
      address 172.18.141.37/24 
      no shutdown 
    exit 
    static-route 172.17.0.0/16 address 172.18.141.1 
 
#********* Configure router interface for TWAMP ********* 
    interface 2 
      address 11.11.101.6/24 
      mtu 2000 
      bind ethernet 0/1 
      vlan 101 
      no shutdown 
    exit 
    static-route 33.33.116.0/24 address 11.11.101.5 
    exit all 
 
#********* Configure TWAMP controller ********* 
configure oam twamp profile 1 
exit all 
configure oam twamp controller 1  
    router-entity 1 
    local-ip-address 11.11.101.6 
    no shutdown 
    peer 33.33.116.6 twamp-light 
ETX-2i Devices 
8. Monitoring and Diagnostics 
    calculation-mode one-way 
    responder-seq-num 
    test-session 1 name 1 udp-port 50000 test-profile 1 dscp 1 
    exit all 
 
#********* Configure control port ********* 
configure terminal  
    timeout forever 
    exit all 
 
#*********Configure SNMPv3 target and traps 
configure 
  management 
    access snmp 
      snmp 
        target MyPC 
          target-params  "tp1" 
          address  udp-domain  172.17.160.72 
          no shutdown 
          tag-list  "unmasked" 
        exit 
        target-params tp1 
          message-processing-model  snmpv3 
          version  usm 
          security name  "initial" level  no-auth-no-priv 
          no shutdown 
        exit all 
 
#********* Configure NTP servers ********* 
configure system date-and-time 
    zone utc +03:00 
    ntp server 1 
      address 172.17.171.141 
      prefer 
      no shutdown 
    exit 
    server 2 
      address 172.17.171.142 
      no shutdown 
    exit 
    server 3 
      address 172.17.172.65 
      no shutdown 
    exit all 
 
#********* Save configuration ********* 
save 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure flows in ETX‑2i: 
• 
Data VLAN 101 
• 
Flows for data 
#********* Configure flows ********* 
exit all 
configure flows  
    classifier-profile v101 match-any match vlan 101 
 
    flow Eth1_Int6_101 
      classifier  v101 
      ingress-port ethernet  1 
      egress-port int-ethernet 6 queue 0 block 0/1 
      no policer 
      no shutdown 
    exit  
 
    flow Int6_Eth1_101 
      classifier  v101 
      ingress-port int-ethernet 6 
      egress-port ethernet 1 queue 0 block 0/1 
      no policer 
      no shutdown 
    exit all 
 
#********* Save configuration ********* 
save 
Viewing the TWAMP Status 
 To view the controller status: 
ETX‑2i>config>oam>twamp>controller(1/light)# show status 
IPPM Type                    : TWAMP Light 
Router Entity                : 1 
Router Interface             : 2 
Router Interface oper status : UP 
Controller Status            : In Progress 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To view the responder status: 
ETX‑2i>config>oam>twamp>responder(1/light)# show status 
IPPM Type                    : TWAMP Light                    
Router Entity                : 1                              
Router Interface             : 2                              
Router Interface oper status : UP                             
Responder Status             : Ready                          
 
Responder Test Name      UDP Port  Tx Packets     Rx Packets      
--------------------------------------------------------------- 
TwampResponderSession    900       1107           1107        
 To view the peer test status for TWAMP Light continuous test: 
ETX‑2i>config>oam>twamp>controller(1/light)>peer(33.33.116.6)# show status 
IPPM Type          : TWAMP Light 
Activation Mode    : Continuous 
Start Time         : 2013-11-24 14:13:28 
 
Controller Test Name     Peer UDP  Status         Tx Packets     Rx Packets 
----------------------------------------------------------------------------- 
twamp1                   900       In Progress    600            599 
 To view peer test status for TWAMP Light non-continuous test: 
ETX‑2i>config>oam>twamp>controller(1/light)>peer(33.33.116.6)# show status 
IPPM type 
: TWAMP Light 
Activation mode 
: non-continuous 
Calculation Mode 
: round-trip  
Start time 
: 2013-05-30 15:29:45 
Duration [ min ] 
: 120 
Elapsed Time [ min ] : 20 
 
Controller test name      Peer UDP   Status       Tx packets   Rx packets 
----------------------------------------------------------------------------- 
XXXX                      30000      In progress  2000         1900 
YYYY                      35000      Ready        2000         1900  
ABCD                      40000      In progress  42000000     600000 
 To view peer test status for ICMP Echo continuous test: 
ETX‑2i>config>oam>twamp>controller(1)>peer(33.33.116.6)# show status 
IPPM type 
 
: ICMP Echo 
Activation mode 
 
: continuous 
Start time 
 
: 2013-05-30 15:29:45 
 
Controller test name              Status    Tx packets   Rx packets 
----------------------------------------------------------------------------- 
XXXX                              In progress  2000        1900 
YYYY                              Ready        2000        1900  
ETX-2i Devices 
8. Monitoring and Diagnostics 
ABCD                              In progress  42000000    600000 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing TWAMP Reports 
 To view a TWAMP Light test summary report (one-way calculation mode): 
ETX‑2i>config>oam>twamp>controller(1/light)>peer(33.33.116.6)# show summary-report 
IPPM Type                        : TWAMP Light 
Controller IP Address            : 11.11.101.6 
Responder IP Address             : 33.33.116.6 
Activation Mode                  : Off 
Calculation Mode                 : one-way 
TOD status controller/peer       : Sync / Out of sync 
Start / Elapsed / Duration (min) : 2014-06-01 10:36:41 / 1 / 1 
 
Controller Test Name   Dir IP   Size   Loss    Delay    PDV     IPDV   Result 
                           DSCP        Ratio   Max      Max     Max 
                                (bytes)        (ms)     (ms)    (ms) 
---------------------------------------------------------------------------- 
1                      fwd 22   1280   2.0E-2 0.658    0.065    0.048   Fail 
1                      bck 22   1280   0      0.263    0.014    0.011   Pass 
 To view a TWAMP Light test summary report (round-trip calculation mode): 
ETX‑2i>config>oam>twamp>controller(2/light)>peer(33.33.117.6)# show summary-report 
IPPM Type                        : TWAMP Light 
Controller IP Address            : 11.11.102.6 
Responder IP Address             : 33.33.117.6 
Activation Mode                  : Continuous 
Calculation Mode                 : round-trip 
Start Time / Elapsed Time (sec)  : 2014-06-02 00:27:30 / 240 
 
Controller Test Name     IP   Size    Loss    Delay    PDV     IPDV    Result 
                         DSCP         Ratio   Max      Max     Max 
                              (bytes)         (ms)    (ms)     (ms) 
----------------------------------------------------------------------------- 
6                        6     512    6.9E-1  179.292  3.415   2.312    NA 
7                        7     512    6.7E-1  181.170  5.494   3.888    NA 
8                        8     512    6.9E-1  183.131  5.817   4.545    NA 
9                        9     512    6.7E-1  185.145  7.609   6.323    NA 
10                       10    512    6.7E-1  187.108  10.949  9.789    NA 
 To view a TWAMP Light test report: 
ETX‑2i>config>oam>twamp>controller(1/light)>peer(33.33.116.6)# show report 1 all 
Test Name              : 1 
IPPM Type              : TWAMP Light 
Controller IP Address  : 11.11.101.6 / 56568 
Responder IP Address   : 33.33.116.6 / 50000 
IP DSCP                : 22 
Payload Length (bytes) : 256 
Calculation Mode       : one-way 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Start Time             : 2014-06-01 14:13:28 
 
Test Interval                          : Current 
Time Stamp                             : 2014-06-01 16:14:53 
Elapsed Time (sec)                     : 60 
TOD Sync Count (sec)                   : 0 
 
Tx Packets         Fwd / Back          : 5400         5360 
Loss Packets       Fwd / Back          : 40           17 
Loss Ratio         Fwd / Back          : 7.4E-3       3.2E-3 
Availability Count Fwd / Back (sec)    : 540          540 
       
Duplicate Packets  Fwd / Back          : 0           0 
Duplicate Ratio    Fwd / Back          : 0           0 
Reordered Packets  Fwd / Back          : 0           0 
Reordered Ratio    Fwd / Back          : 0           0 
Fragmented Packets Fwd / Back          : 0           0 
 
Delay-Fwd Threshold Crossing Count     : 0 
Delay-Back Threshold Crossing Count    : 8 
Delay-Fwd Min / Max / Average (ms)     : 0.530        0.892        0.615 
Delay-Back Min / Max / Average (ms)    : 0.226      775.498        0.899 
PDV-Fwd          Max / Average (ms)    : 0.351        0.085 
PDV-Back         Max / Average (ms)    : 377.482      0.673 
IPDV-Fwd Max / Average (ms)            : 0.306        0.010 
IPDV-Back Max / Average (ms)           : 775.263      0.293 
 
Loss Result                            : Pass                                               
Delay Result                           : Pass                                               
DV Result                              : Pass 
 To view an ICMP Echo test summary report (continuous, round-trip calculation mode): 
ETX‑2i>config>oam>twamp>controller(1)>peer(234.234.56.100)icmp-echo# show  summary-report 
IPPM                            : ICMP Echo 
Controller ip address 
 
: 1.1.1.1 
Responder ip address  
: 234.234.56.100 
Activation mode 
 
: continuous  
Start time / Elapsed time [sec] 
: 2013-05-30 15:29:45 / 500 
 
Controller test name              DSCP Size   Loss   Delay  PDV    IPDV  Result 
                                      [bytes] Ratio  Max    Max    Max  
                                                     [ms]   [ms]   [ms] 
--------------------------------------------------------------------------------  
AAAAA                             02   100   6.5E-5  5.000  1.000  2.000  NA 
 
 

## Configuration Errors  *(p.1421)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
 To view an ICMP Echo test report (non-continuous, round trip calculation mode): 
ETX‑2i>config>oam>twamp>controller(1)>peer(33.33.116.6)icmp-echo# show report  
AABBCC current 
 
Test Name                                : AABBCC 
IPPM type                                : ICMP Echo 
Controller ip address                    : 1.1.1.1 
Responder ip address                     : 234.234.56.100 
IP DSCP                                  : 34 
Payload length [bytes]                   : 1500 
Start Time                               : 2013-05-30 15:29:45 
------------------------------------------------------------------------------- 
Test interval                            : current 
Elapsed time [sec]                       : 180 
Tx packets                               : 1800  
 
Loss packets                             : 10 
Loss Ratio                               : 1.2E-3 
Availability count [sec]                 : 180 
Duplicate packets                        : 2 
Duplicate Ratio                          : 1.2E-3 
Reordered packets                        : 3 
Reordered Ratio                          : 1.2E-3 
Delay threshold crossing count           : 7 
Delay      min / max / average [ms]      : 1.000     2.000     1.500 
PDV              max / average [ms]      : 2.000     1.000 
IPDV             max / average [ms]      : 2.000     1.000 
Loss result                              : fail // for non-continuous only 
Delay result                             : pass // for non-continuous only 
DV result                                : pass // for non-continuous only 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Cannot modify; TWAMP 
controller is active 
Tried modifying the bound port 
definition while controller was 
active (status was not 
‘shutdown’). 
Shut down the controller and then 
modify the bound port definition. 
Tried modifying VLAN definition 
while controller was active 
(status was not ‘shutdown’). 
Shut down the controller and then 
modify the VLAN definition 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
Tried modifying controller’s 
router entity number while 
controller was active (status 
was not ‘shutdown’). 
Shut down the controller and then 
modify the router entity number. 
Tried modifying local IP address 
while controller was active 
(status was not ‘shutdown’). 
Shut down the controller and then 
modify the local IP address. 
Cannot modify; TWAMP 
controller has active test 
Tried modifying the bound port 
definition while controller had 
an active test. 
Wait for the active test to terminate and 
then modify the bound port definition. 
Tried modifying VLAN definition 
while controller had an active 
test. 
Wait for the active test to terminate and 
then modify the VLAN definition. 
Tried modifying controller’s 
router entity number while 
controller had an active test. 
Wait for the active test to terminate and 
then modify the controller’s router 
entity number. 
Tried modifying local IP address 
while controller had an active 
test. 
Wait for the active test to terminate and 
then modify the local IP address. 
Cannot delete; TWAMP controller 
is active 
Tried removing the bound port 
while controller was active 
(status was not ‘shutdown’). 
Shut down the controller and then 
remove the bound port. 
Tried removing the VLAN 
definition while controller was 
active (status was not 
‘shutdown’). 
Shut down the controller and then 
remove the VLAN definition. 
Cannot delete; TWAMP controller 
has active test 
Tried removing the bound port 
while controller had an active 
test. 
Wait for the active test to terminate and 
then remove the bound port. 
Tried removing the VLAN 
definition while controller had 
an active test. 
Wait for the active test to terminate and 
then remove the VLAN definition. 
Cannot activate; router entity and 
local ip address must be defined 
Tried activating controller when 
router entity and/or local IP 
address were not defined. 
Define router entity and local IP address, 
and then activate controller. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
Tried activating responder 
when router entity and/or local 
IP address were not defined. 
Define router entity and local IP address, 
and then activate responder. 
Cannot activate; router entity, 
local ip address and port must be 
defined 
In l2-probe mode, tried 
activating controller when 
router entity, local IP address, 
and/or port were not defined. 
Define router entity, local IP address, 
and port, and then activate controller. 
In l2-probe mode, tried 
activating responder when 
router entity, local IP address, 
and/or port were not defined. 
Define router entity, local IP address, 
and port, and then activate responder. 
Cannot delete; peer has active 
test 
Tried deleting peer entity, while 
there was an active test.  
Wait for active test to terminate, and 
then delete peer entity. 
Cannot create; name already in 
use 
Tried giving a test session a 
name that already exists under 
peer context. 
Give test session a unique name. 
Tried giving a test profile a 
name that already exists under 
TWAMP contest. 
Give test profile a unique name. 
Tried giving a responder a name 
that already exists under 
TWAMP context. 
Give responder a unique name. 
Tried giving a test session a 
name that already exists under 
responder contest. 
Give test session a unique name. 
Cannot activate; controller not 
ready 
Tried activating peer test 
sessions when controller status 
was ‘idle’ (not ready). 
Wait for controller to be ready, and then 
activate peer test sessions. 
Cannot activate; peer has active 
test 
Tried activating peer test 
sessions while there were 
active tests. 
Wait for active tests to terminate, and 
then activate peer test sessions. 
Cannot delete; TWAMP 
responder is active 
Tried removing active 
responder (status ‘idle’ or 
‘ready’). 
Shut down the responder and then 
delete it. 
Tried deleting the bound port 
definition while responder was 
active (status ‘idle’ or ‘ready’). 
Shut down the responder and then 
delete the bound port definition. 