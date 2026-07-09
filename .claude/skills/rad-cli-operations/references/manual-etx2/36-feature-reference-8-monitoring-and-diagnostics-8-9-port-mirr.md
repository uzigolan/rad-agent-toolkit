# Feature Reference – 8 Monitoring and Diagnostics – 8.9 Port Mirroring

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1536–1540.*


## Applicability and Scaling  *(p.1536)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Counter 
Description 
% 
The percentage of available time 
Availability Thr 
The Availability service acceptance criteria for the reported P-bit 
Burst Tests 
 
Number of Cycles 
The number of burst transmission cycles 
Frames per Cycle 
The number of frames in a single burst transmission cycle 
Minimum Expected 
Frames 
The minimum total number of frames expected to be received in the sub-test 
Actual Received 
Frames 
The actual total number of frames received during the sub-test 
8.9 Port Mirroring 
ETX‑2i supports local port mirroring (also called traffic mirroring), enabling you to constantly monitor 
and diagnose network traffic passing through ports, without disrupting traffic. A traffic analyzer at the 
destination port receives, records, and analyzes the traffic, sending an alert when a problem or error 
occurs.  
ETX‑2i supports both inbound Rx mirroring of port ingress traffic and outbound Tx mirroring of port 
egress traffic.  
Applicability and Scaling 
This feature is applicable to ETX-2i, ETX-2i-B, ETX-2i-10G (full and half 19-inch), and ETX-2i-100G, with 
support for the following: 
• 
Up to two mirroring sessions (two mirror (destination) ports). 
• 
Up to two sources (one Rx port and one Tx port) per session and in total in all sessions (i.e., two 
Rx or two Tx source ports are not supported; only one Rx and one Tx port per session and total 
in two sessions). 
 
 

## Standards  *(p.1537)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Port mirroring supports the following interfaces as sources for mirrored traffic: 
• 
ETH User or Network ports 
• 
PCS 
• 
Logical MAC 
 
Note 
LAG (load balancing, protection) is not supported.  
All devices support a single mirror (destination) port, which can be one of the following: 
• 
Ethernet 1GbE port (User or Network) 
• 
Ethernet 10GbE port (User or Network) 
• 
Ethernet 100GbE port 
The following port mirroring options are supported: 
• 
1GbE to 1GbE  
• 
10GbE to 10GbE 
• 
10GbE (up to 1GbE of forwarded traffic) to 1GbE; excess frames are discarded.  
• 
100GbE to 100GbE 
• 
10GbE to 100GbE 
• 
100GbE (up to 10GbE of forwarded traffic) to 10GbE; excess frames are discarded. 
Both Rx and Tx go to a single mirror port (i.e., one mirroring session), or Rx and Tx go to two different 
mirror ports (i.e., two mirroring sessions). 
Standards 
N/A  
 
 

## Functional Description  *(p.1538)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Functional Description 
You configure port mirroring by defining a mirroring session, its sources, the traffic direction of each 
source (Rx, Tx, or Rx-Tx), and a single destination. 
The mirror port (destination port) is dedicated solely for mirroring and does not support forwarding of 
inbound traffic. 
At any time, you can monitor in your device inbound (Rx) traffic to one port and/or outbound (Tx) traffic 
from another port, or both Rx and Tx traffic of a single port. You can configure mirroring of Rx and Tx 
traffic in one mirroring session to the same destination port or in two mirroring sessions to two separate 
destination ports.  
Inbound traffic includes all traffic admitted into the source port following physical layer tests, FCS, and 
more, but before filtering by L2CP, vlan-edit, policing, and more. Outbound traffic qualified for mirroring 
includes all packets of the source that were actually transmitted, such as after the dequeue process and 
filtering (e.g., egress MTU). 
You connect a PC or other capturing device that has a traffic analyzer to an unused port of your device 
(destination port). Then, you activate a mirroring session to capture the traffic going into or out of the 
source port and send it to the destination port for analysis. 
 
Note 
In port mirroring it is recommended to configure the source and destination 
on two different ports. Otherwise, this results in an endless loop of traffic. 
• 
 
A mirroring session source can be added while the session is running. Configuration of a new mirror 
destination overrides the existing one; there is no need to delete the existing destination. 
The device issues an event in the following two cases: 
• 
A port mirroring session is activated. 
• 
A port mirroring session is stopped. 
The device also issues an alarm when a port mirroring session is set. 
Mirroring of traffic from a port to itself is supported. In this case, the traffic designated by this vlan-tag is 
not duplicated. 
 
 

## Factory Defaults  *(p.1539)*


## Configuring Port Mirroring  *(p.1539)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
You can run the show status command under a port, which participates in a port mirroring session, to 
view the following: 
• 
Whether the port acts as source or destination for mirrored traffic.  
• 
In case the port is the source of traffic, specifies the part of traffic on this port that is mirrored 
(Rx, Tx, both Rx and Tx). 
Refer to Viewing Ethernet Port Status in the Cards and Ports chapter for a full explanation and 
examples. 
ETX‑2i supports a counter that presents the number of discarded frames on all flows. Refer to Viewing 
Overflow Discarded Frames Statistics in the Cards and Ports chapter for a full explanation and example. 
Factory Defaults  
By default, port mirroring is disabled. 
Configuring Port Mirroring 
 To configure port mirroring: 
1. Navigate to configure mirroring-session <num>. 
Note 
• 
<num> is the number of the mirroring session.  
• 
Enter no mirroring-session (num) to disable the mirroring session. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Adding/removing source port to/from the 
mirroring session 
[no] source {port <port-type> <port-
index>} {tx | rx | tx-rx} 
port type – source port type 
Possible values: ethernet, pcs, or 
logical-mac 
tx – enable outbound mirroring. 
rx – enable inbound mirroring. 
tx-rx – enable both outbound 
and inbound mirroring. 
Note: Recommended to 
configure source and destination 
on two different ports. 

## Configuration Errors  *(p.1540)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Adding/removing destination port to/from 
the mirroring session 
[no] destination <port-type> <port-
index> 
port type – destination port type 
Possible values: ethernet, pcs,  
or logical-mac 
Note:  
• A destination port can be 
used in one mirroring session 
only. 
• Recommended to configure 
source and destination on 
two different ports. 
Administratively enabling port mirroring 
no shutdown 
Enter shutdown to 
administratively disable the 
mirroring session. 
This command enables you to 
keep the mirror configuration 
and activate it only when 
needed. 
Configuration Errors 
The following table lists the messages generated by ETX‑2i when a configuration error is detected. 
Message 
Possible Cause 
Corrective Action 
Maximum number of Rx 
mirroring sessions has 
already been configured. 
You attempted to open a new Rx mirroring 
session even though the maximum number of 
supported Rx mirroring sessions was already 
configured. 
Remove an existing mirroring 
session in order to create a new 
mirroring session.   
Maximum number of Tx 
mirroring sessions has 
already been configured. 
You attempted to open a new Tx mirroring 
session even though the maximum number of 
supported Tx mirroring sessions was already 
configured. 
Remove an existing mirroring 
session in order to create a new 
Tx mirroring session.   
The same destination 
cannot be defined for 
different sessions. 
You used the same destination for more than 
one session. The same destination may not be 
defined for more than one session at a time.  
Define a different destination 
for each session.  