# Feature Reference – 8 Monitoring and Diagnostics – 8.1 In-Service ICMP Echo Ping Test

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1276–1284.*


## Applicability and Scaling  *(p.1276)*


## Functional Description  *(p.1276)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Method 
How and What it Monitors 
TWAMP 
Measures one-way and two-way metrics between Layer-2 or 
Layer-3 network elements. 
Y.1564 Ethernet Service Activation Test 
Assesses the proper configuration and performance of an 
Ethernet service prior to customer notification and delivery 
8.1 In-Service ICMP Echo Ping Test 
In many cases, users want to be able to ping the Layer-2 EVC at the device for diagnostic purposes.  
ETX‑2i provides an in-service ICMP Echo ping test that enables you to activate a single, simple command 
to send a ping and check the connectivity across Layer-2 service paths for diagnostic purposes, without 
requiring configuration of a full TWAMP controller and responder. 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. 
Functional Description 
Layer-2 Ether-Access devices have the ability to initiate a connectivity test and also respond to in-service 
ping requests sent over Layer-2 services to a configured IP address. 
The in-service ICMP Echo ping test pings the Layer-2 EVC of the device from the flow level. The in-service 
ping includes a mechanism to enable performing a connectivity test across the flow inside the device, by 
configuring ICMP packets’ entry-point to the flow, either at the flow ingress or egress. The in-service 
ping runs independently of working routers.  
The in-service test requires that the devices be activated in two modes: 
Generator 
Device sends ping messages. 
Responder 
Device receives ping messages and sends a reply. 
A single ICMP Echo instance is supported – Generator or Responder.  
ETX‑2i supports generating a detailed report of the status of an active in-service test.  
ETX-2i Devices 
8. Monitoring and Diagnostics 
In-service ICMP Echo is supported in the following topologies: 
• 
Point-to-point E-line service 
• 
Multipoint-to-multipoint E-LAN (bridge) services 
• 
Multipoint-to-multipoint (or point-to-multipoint) E-Tree services 
Point-to-Point E-Line Service 
• 
IPv4 only 
• 
Two configurable probing scopes: 
 
Up – in-service ping request/response packets are injected at the ingress port of the service 
and mimic frame traverse of the UNI/NNI flow chain. 
 
Down – In-service ping request/response packets are injected directly at the egress port of 
the service using the highest priority queue 
 
ETX-2
ETH
Port
Policer
ETH
Port
Ping VRF
Ping
TWAMP
Router
Interface
 
ICMP Echo – Point-to-Point E-Line Services 
Multipoint-to-Multipoint E-LAN (bridge) Services 
• 
IPv4 only  
• 
Where bridge is used, in-service ping probing-scope is injected to the bridge only and generated 
toward any port connected to the specific VPN. 

## Configuring the In-Service ICMP Echo Ping Test  *(p.1278)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Bridge
ETX-2
ETH
Port
ETH
Port
Ping VRF
Ping
Bridge 
Port
Router
Interface
 
ICMP Echo – Bridge Services  
Multipoint-to-Multipoint (or Point-to-Multipoint) E-Tree Services 
• 
IPv4 only  
• 
Where bridge is used, in-service ping probing-scope is injected to the bridge only and generated 
toward any port connected to the specific VPN. 
• 
The internal bridge port from which the in-service ping-request is sent must be configured as 
root for the given Layer-2 VPN. The responder listens to in-service ping-requests received from 
the root bridge port on the specified VPN and replies with an in-service ping response on the 
same root bridge port. 
Configuring the In-Service ICMP Echo Ping Test 
 To configure the in-service ICMP Echo ping test: 
1. Configure the in-service ping response – at the device that responds to the ping-request packets 
with ping-response packets. You can configure the IP stack to start and listen to ping-requests 
being sent over a particular flow, targeted to a provisioned IP address. 
2. Configure the in-service ping request – at the device generating the ping test. 
It is not possible to save the in-service ping responder configuration. It is erased on reset and does not 
appear in the info command. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
When you invoke the commands, a temporary IP interface is created on the device, as well as a routing 
entry in the static-route table. When the test has completed, all IP context on the generator side that is 
related to the test is cleared; the IP context on the responder side must be cleared manually. 
Configuring In-Service ICMP Echo Ping Response 
Note 
In Point-to-Point mode, a service (flows) with corresponding classification 
must exist on the requested ingress port prior to in-service ping-response 
commands generation; it is optional to configure an opposite matching flow. 
In the case that an opposite matching flow does not exist, the service ping 
works in “down scope“ (the default) without any warning. 
 To configure an in-service ping response: 
1. Navigate to configure flows. 
The ETX‑2i>config>flows# prompt is displayed. 
2. Enter the following command, using the parameters described in the table below: 
service-ping-response {local-ip <local_ip_addr_and_subnetmask>}{next-
hop|<next_hop_ip_address>} {egress-port<egress_port>|bridge<bridge_id>} [vlan< vlan_id] 
[inner-vlan<inner_vlan_id>] [p-bit< p_bit_id] [inner-p-bit <inner_p_bit_id>] [probe-scope 
<up|down>] 
At any time, you can configure the device to cease listening to in-ping-requests, by entering the 
command: 
no service-ping-response 
The device clears any generated command context (the local IP address and routing entry).  
Note 
Invoking no service-ping-response terminates the command that was 
initiated in the same database session or in a different database session 
(same user or different user). 
Configuring In-Service ICMP Echo Ping Request 
Note 
In Point-to-Point mode, a service (flows) with corresponding classification 
must exist on the requested ingress port prior to in-service ping commands 
generation; it is optional to configure an opposite matching flow. In the case 
that an opposite matching flow does not exist, the service ping works in 
“down scope“ (the default) without any warning. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure an in-service ping request: 
1. Navigate to configure flows. 
The ETX‑2i>config>flows# prompt is displayed. 
2. Enter the following command, using the parameters described in the table below: 
service-ping {local-ip <local_ip_addr_and_subnetmask>} {dst-ip <destination_ip_addr>} {next-
hop|<next_hop_ip_address>} {egress-port<egress_port>|bridge<bridge_id>} [vlan< vlan_id] 
[inner-vlan<inner_vlan_id>] [p-bit< p_bit_id] [inner-p-bit <inner_p_bit_id>] [probe-scope 
<up|down>] [number-of-packets<number_of_packets>] [payload-size<number_of_bytes>] 
The next in-service ping request is transmitted after at least one second (hard-coded) has elapsed from 
the transmission of the previous in-service ping request, provided the previous in-service ping response 
packet has been received. If the in-service ping response packet has not been received within two 
seconds since it was sent (hard-coded timeout), the ping-packet is declared lost, a message is echoed 
back to your-screen, and the next in-service ping request is immediately transmitted. 
The in-service ping test is automatically terminated after the transmission of the ‘number-of-packets’ in 
the in-service ping request and the reception of the corresponding echoes.  
You can terminate the in-service ping test before the number-of-packets have been exhausted by 
clicking Ctrl-C or entering the command: 
no service-ping  
The initiator interrupts the current in-service ping test and returns the following termination message 
and test summary: 
Ping is terminated by user: 
<num_packet_tx> packets transmitted. < num_packet_rx> packets received, <loss_percentage>% 
packet loss 
round-trip (ms) min/avg/max = <rt_min>/<rt_avg>/<rt_max> 
 
Note 
Invoking no service-ping terminates the command that was initiated in the 
same database session or in a different database session (same user or 
different user). 
In-Service Ping Parameters 
Parameter 
Description 
Value 
local-ip 
The temporary IP address provisioned on the 
sender/responder for the duration of the test, combined 
with subnet-mask 
Valid IP address and subnet 
mask 
[0.0.0.0/32|0:0:0:0::0/128] 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Description 
Value 
dst-ip 
The IP address to which in-service ping request packets 
are destined 
Valid IP address 
[0.0.0.0|0:0:0:0::0] 
next-hop 
Next hop to use when destination IP is out of the source 
subnet 
Valid IP address 
[0.0.0.0|0:0:0:0::0] 
egress-port 
Egress port for Point-to-Point services (E-Line). The 
physical (e.g., Ethernet port) or logical (e.g., bridge ID) 
interface through which the ping request/response exits. 
Valid attribute only when bridge parameter is not 
introduced. 
ethernet, pcs, or logical-
mac 
bridge 
Bridge ID for bridged services (E-LAN/E-Tree service 
probing). Valid attribute only when egress-port 
parameter is not introduced. 
Valid bridge ID 
vlan 
Together with egress-port, defines the flow 
Possible values: 0–4095 
inner-vlan 
Together with egress-port, defines the flow 
Possible values: 0–4095 
p-bit 
The service VLAN priority bit used when encapsulating the 
ping packet 
Possible values: 0–7 
Default: 0 (untagged) 
inner-p-bit 
The inner-VLAN priority bit used when encapsulating the 
ping packet 
Possible values: 0–7 
Default: 0 (untagged) 
probe-scope 
The in-service ping request/response probing mode. 
Applicable only for E-Line services when egress-port is 
selected. Not applicable when user selects bridge. 
up/down 
Default: up 
number-of-packets 
Number of in-service ping request packets for the test 
Possible values: 1–10000 
Default: 5 
payload-size 
Payload size of the in-service ping request packets 
Possible values: 32–1450 
Default: 32 
In-Service ICMP Echo Ping Test Results 
Echo results (including RTT) are echoed back to the user terminal in a format similar to the existing ping 
format. 
 
 

## Examples  *(p.1282)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
For example, pinging IP address 172.17.155.83 with number-of-packets = 6 and payload-size = 32: 
Reply from 172.17.155.83: bytes = 32, packet number = 0, time < 10 ms 
Reply from 172.17.155.83: bytes = 32, packet number = 1, time < 10 ms 
Reply from 172.17.155.83: bytes = 32, packet number = 2, time < 10 ms 
Reply from 172.17.155.83: bytes = 32, packet number = 3, time < 10 ms 
Reply from 172.17.155.83: bytes = 32, packet number = 4, time < 10 ms 
5 packets transmitted. 5 packets received, 0% packet loss 
round-trip (ms) min/avg/max = 0/0/0 
Examples 
The following example illustrates configuring in-service ping test over Eth services. Layer-2 E-Line 
service is provisioned between device UNI and NNI. 
 To configure the responder with an in-service ping response: 
exit all 
#********* Configure classifier for VLAN 100 
configure 
flows 
classifier-profile v100 match-any 
match vlan 100 
exit 
#********* Configure Service between ETH 3 & 4 
flow ping_E3toE4 
classifier v100 
ingress-port ethernet 3 
egress-port ethernet 4 queue 3 block 0/1 
no policer 
no shutdown 
exit 
 
flow ping_E4toE3 
classifier v100 
ingress-port ethernet 4 
egress-port ethernet 3 queue 3 block 0/1 
no policer 
no shutdown 
exit 
 
#*********In-Service Ping ******************************** 
 
service-ping-response local-ip 10.10.10.30/24 next-hop 10.10.10.20 egress-port ethernet 4 vlan 
100 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure the generator with an in-service ping request: 
exit all 
#********* Configure classifier for VLAN 100 
configure 
flows 
classifier-profile v100 match-any 
match vlan 100 
exit 
#********* Configure Service between ETH 3 & 4 
flow ping_E3toE4 
classifier v100 
ingress-port ethernet 3 
egress-port ethernet 4 queue 3 block 0/1 
no policer 
no shutdown 
exit 
 
flow ping_E4toE3 
classifier v100 
ingress-port ethernet 4 
egress-port ethernet 3 queue 3 block 0/1 
no policer 
no shutdown 
exit 
 
#*********In-Service Ping ******************************** 
 
service-ping local-ip 10.10.10.20/24 dst-ip 10.10.10.30 next-hop 10.10.10.30 egress-port 
ethernet 4 vlan 100 probe-scope down number-of-packets 5 payload-size 64 
The following example illustrates configuring an in-service ping test over bridge services. Layer-2 E-LAN 
service is provisioned between device UNI and an internal bridge port. 
exit all 
#*******Configure bridge 
configure bridge 1 
vlan-aware 
#*******Configure bridge ports 
port 1 
no shutdown 
exit all 
#********* Configure classifier for VLAN 100 
configure 
flows 
classifier-profile v100 match-any 
match vlan 100 
exit 
 
 
#********* Configure flows between ETH 3 & BP11 
flow ping_E03_BP11 
classifier v100 

## Configuration Errors  *(p.1284)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
ingress-port ethernet 3 
egress-port bridge-port 1 1 
reverse-direction block 0/1 
no policer 
no shutdown 
exit 
 
 
service-ping-response local-ip 10.10.10.30/24 next-hop 10.10.10.20 bridge 1 vlan 100 
#*********In-Service Ping ******************************** 
 
 
#*********In-Service Ping ********************************# 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Parameter or keyword missing or 
wrong 
The entered service (outer) 
VLAN, does not also populate 
the customer (inner) VLAN in 
the command. 
Configure a service (outer) VLAN that 
also populates the customer (inner) 
VLAN in the command. 
Invalid parameter value. Local-ip 
and next-hop must belong to the 
same network  
The next-hop address does not 
belong to the same network as 
the sender address (local IP 
address). 
Choose local IP and next-hop IP 
addresses in the same network. 
Invalid parameter value. Local-ip 
and next-hop must be equal as 
dst-ip belongs to the same 
network 
The destination IP address 
belongs to the same network as 
the sender, but the next-hop 
address is not equal to the local 
IP address. 
Make next hop address equal to the 
local IP address. 
 
 