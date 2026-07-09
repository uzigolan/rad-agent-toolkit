# Feature Reference – 5 Traffic Processing – 5.2 Flows

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 892–943.*


## Applicability and Scaling  *(p.892)*

ETX-2i Devices 
5. Traffic Processing 
Spanning Tree Status – Bridge Port MSTI Level 
Port 1 (Eth1/1), MSTI 1000, Root, Forwarding, Edge (default) 
    Up 2 days 22:11:00 
VLANs mapped 1-20, 100 
Designated Root: Priority 32768, Address 00:11:22:33:44:55, Port 10 
Regional Root: Priority 32768, Address 00:11:22:33:44:55, Cost 200000000 
5.2 Flows 
User traffic can be classified into different Ethernet flows (EVC.CoS), which are unidirectional or 
bidirectional entities that connect two physical or logical ports, to provide services in a flexible manner. 
When creating a new flow, you can invoke MAC address learning (by default, it is disabled). ETX-2i 
supports the following port-level classification mechanisms:  
• 
Flow classification (see Flow Classification) 
• 
Port Classification (see Port Classification) 
With port classification, you can maintain network security by preventing malicious traffic from being 
forwarded by the port, as well as save network resources by dropping unwanted packets. 
Note 
If flow classification and port classification are configured for a port, port 
classification takes precedence over flow classification. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products, with the following conditions: 
• 
PCS port is relevant to ETX-2i with an SHDSL or VDSL2 module. 
• 
Pseudowire (PW) is relevant to devices that support smart SFP MiTOP functionality and ETX-2i-
64E1. 
• 
D-NFV is relevant only for ETX-2i with a D-NFV option. 
• 
ETX-2i-100G supports flow classification only; not port classification. 
• 
The status report of an active service ping command is relevant for version 6.8.2 (2.68). 
• 
VLAN edit actions “push VLAN tag with P-bit profile” and “swap internal VLAN with P-bit copy” 
(ETX-2i-10G/8SFPP) are relevant in versions 6.8.2 (0.52), 6.8.2 (0.55), and 6.8.2 (2.52). 

## Standards Compliance  *(p.893)*


## Functional Description  *(p.893)*

ETX-2i Devices 
5. Traffic Processing 
Standards Compliance 
IEEE 802.1ad, IEEE 802.1Q 
Functional Description 
Ethernet flows are unidirectional, or in the case of bridge flows, can also be bidirectional. For 
unidirectional flows, you have to define two flows between the two ports, one for each direction. For 
bidirectional flows, you only need to define one flow from a port to a bridge port and specify the 
reverse-direction command.  
Note 
• 
In the case of bridge flows, you can configure two flows between a 
physical port and a bridge port (one flow in each direction) or one 
bidirectional flow (reverse-flow)).  
• 
RAD recommends using bidirectional flows for bridge flows, as all testing 
is performed with bidirectional flows – a newer and more advanced 
method (than unidirectional flows). 
• 
When configuring two unidirectional flows, in the flow from the egress 
bridge port to the ingress physical port, the physical port automatically 
takes the queue from the CoS configured in the flow. Therefore, in the 
configuration of the flow in the other direction, from the ingress bridge 
port to the egress physical port, you cannot configure a queue in the 
egress physical port. Doing so results in the following error: A flow from 
bridge port must not use a Queue Mapping or a Queue Mapping profile.  
Flow Classification 
The ingress traffic is first classified into flows according to classification profiles. The classification is per 
port and is applied to the ingress port of the flow. Packets can be classified by means of their VLAN IDs 
and other criteria, fully specified in Configuring a Classifier Profile.  
In the following descriptions, VLAN refers to the service provider (outer) VLAN, sometimes referred to as 
SP-VLAN, while inner VLAN refers to the Customer Entity VLAN, sometimes referred to as CE-VLAN or 
C-VLAN. 
Flow classifications that apply to the same port are allowed in the combinations shown below. The 
priority shown is used to determine which classification is used if incoming packets for the port fit the 
criteria of more than one classification. Priority 4 is the lowest, priority 1 is the highest. NNI indicates 
ingress network port, UNI indicates ingress user port. 
ETX-2i Devices 
5. Traffic Processing 
Flow Classification Combinations 
Classification 
Other Classifications Allowed 
on Same Ingress Port 
Range 
Max Number 
Ranges 
Priority 
NNI/UNI 
Unclassified 
(all-to-one 
bundling) 
VLAN 
VLAN + IP precedence 
VLAN + DSCP 
VLAN + VLAN priority 
VLAN + non-IP  
VLAN priority 
IP precedence 
DSCP 
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
Non-IP 
Untagged 
– 
1 
4 
Both 
VLAN 
See Note 1 
VLAN + VLAN priority 
VLAN + IP precedence 
VLAN + DSCP 
VLAN + source MAC address 
VLAN + destination MAC address 
VLAN + source IP address 
VLAN + destination IP address 
VLAN + inner VLAN  
VLAN + VLAN priority + inner 
VLAN  
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
Unclassified 
Untagged 
0–4094 
30   
2 
Both 
ETX-2i Devices 
5. Traffic Processing 
Classification 
Other Classifications Allowed 
on Same Ingress Port 
Range 
Max Number 
Ranges 
Priority 
NNI/UNI 
VLAN + VLAN 
priority 
See Note 1  
VLAN 
VLAN + source MAC address  
VLAN + destination MAC address 
VLAN + source IP address 
VLAN + destination IP address 
VLAN + inner VLAN  
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
Unclassified  
Untagged 
0–4094 + 0–7 
30  
2 
Both 
VLAN + IP 
precedence  
VLAN 
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
Unclassified 
Non-IP 
Untagged 
0–4094 + 0–7 
30  
2 
Both 
VLAN + DSCP 
VLAN 
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
Unclassified 
Non-IP 
Untagged 
0–4094 + 0–
63 
30  
2 
Both 
VLAN + source 
MAC address 
VLAN 
VLAN + VLAN priority 
VLAN + inner VLAN 
VLAN + VLAN priority + inner 
VLAN  
0–4094 + 
MAC address 
One VLAN 
value + one 
MAC address 
range  
1 
Both   
ETX-2i Devices 
5. Traffic Processing 
Classification 
Other Classifications Allowed 
on Same Ingress Port 
Range 
Max Number 
Ranges 
Priority 
NNI/UNI 
VLAN + 
destination MAC 
address 
VLAN 
VLAN + VLAN priority 
VLAN + inner VLAN 
VLAN + VLAN priority + inner 
VLAN  
0–4094 + 
MAC address 
One VLAN 
value + one 
MAC address 
range  
1 
Both  
VLAN + source 
IP address 
VLAN 
VLAN + VLAN priority  
VLAN + inner VLAN 
VLAN + inner VLAN + VLAN 
priority 
0–4094 + 
IP address 
10 × VLAN 
value + IP 
address/range 
2 
Both  
VLAN + 
destination 
IP address 
VLAN 
VLAN + VLAN priority  
VLAN + inner VLAN 
VLAN + inner VLAN + VLAN 
priority 
0–4094 + 
IP address 
10 × VLAN 
value + IP 
address/range 
2 
Both  
VLAN + 
inner VLAN 
VLAN 
VLAN + VLAN priority 
VLAN + VLAN priority + inner 
VLAN 
VLAN + source MAC address 
VLAN + destination MAC address 
VLAN + source IP address 
VLAN + destination IP address 
Single value 
for VLAN and 
range for 
inner VLAN 
30 (for inner 
range) 
3 
Both  
VLAN + 
inner VLAN + 
VLAN priority  
VLAN 
VLAN + inner VLAN  
VLAN + source MAC address 
VLAN + destination MAC address 
VLAN + source IP address 
VLAN + destination IP address 
Single value 
for VLAN and 
range for 
inner VLAN 
30 (for inner 
range) 
3    
Both  
VLAN + 
inner VLAN + 
DSCP 
VLAN + inner VLAN 
VLAN +inner VLAN + non-IP 
VLAN + DSCP 
VLAN + non-IP 
Untagged 
Single value 
for VLAN and 
range for 
inner VLAN 
and DSCP  
10 for inner 
VLAN 
1 for DSCP 
2 
Both 
VLAN + 
inner VLAN + non-
IP 
VLAN + inner VLAN 
VLAN +inner VLAN + DSCP 
VLAN + DSCP 
VLAN + non-IP 
Untagged 
Single value 
for VLAN and 
range for 
inner VLAN 
10 (for inner 
range) 
1 
Both 
ETX-2i Devices 
5. Traffic Processing 
Classification 
Other Classifications Allowed 
on Same Ingress Port 
Range 
Max Number 
Ranges 
Priority 
NNI/UNI 
VLAN + non-IP 
Unclassified 
VLAN 
VLAN + IP precedence 
VLAN + DSCP 
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
Untagged 
0–4094 
30  
1 
Both 
VLAN priority 
Unclassified 
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
Untagged 
0–7 
30  
2 
Both 
IP precedence 
Unclassified 
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
Non-IP 
0–7 
30  
2 
Both 
DSCP 
Unclassified 
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
Non-IP 
0–63 
30  
2 
Both 
ETX-2i Devices 
5. Traffic Processing 
Classification 
Other Classifications Allowed 
on Same Ingress Port 
Range 
Max Number 
Ranges 
Priority 
NNI/UNI 
Source MAC 
address 
VLAN 
VLAN priority 
VLAN + VLAN priority 
VLAN + IP precedence 
VLAN + DSCP 
VLAN + Non-IP 
IP precedence 
DSCP 
Unclassified 
Non-IP 
Untagged 
MAC address 
1   
1 
Both 
Destination MAC 
address 
VLAN 
VLAN priority 
VLAN + VLAN priority 
VLAN + IP precedence 
VLAN + DSCP 
VLAN + Non-IP 
IP precedence 
DSCP 
My-MAC 
Unclassified 
Non-IP 
Untagged 
MAC address 
1  
1 
Both 
My-MAC 
VLAN 
VLAN priority 
VLAN + VLAN priority 
VLAN + IP precedence 
VLAN + DSCP 
VLAN + Non-IP 
IP precedence 
DSCP 
Destination MAC address 
Unclassified 
Non-IP 
Untagged 
1 
1 
1 
Both 
ETX-2i Devices 
5. Traffic Processing 
Classification 
Other Classifications Allowed 
on Same Ingress Port 
Range 
Max Number 
Ranges 
Priority 
NNI/UNI 
Source IP address 
See Note 2 
VLAN 
VLAN priority 
VLAN + VLAN priority 
VLAN + IP precedence 
VLAN + DSCP 
VLAN + Non-IP 
IP precedence 
DSCP 
Unclassified 
Non-IP 
Untagged 
IP address 
10   
1 
Both 
Destination 
IP address 
See Note 2 
VLAN 
VLAN priority 
VLAN + VLAN priority 
VLAN + IP precedence 
VLAN + DSCP 
VLAN + Non-IP 
IP precedence 
DSCP 
My-IP 
Unclassified 
Non-IP 
Untagged 
IP address 
10  
1 
Both 
My-IP 
VLAN 
VLAN priority 
VLAN + VLAN priority 
VLAN + IP precedence 
VLAN + DSCP 
VLAN + Non-IP 
IP precedence 
DSCP 
Destination IP address 
Unclassified 
Non-IP 
Untagged 
1 
1 
1 
Both 
ETX-2i Devices 
5. Traffic Processing 
Classification 
Other Classifications Allowed 
on Same Ingress Port 
Range 
Max Number 
Ranges 
Priority 
NNI/UNI 
Non-IP 
Unclassified 
VLAN + IP precedence 
VLAN + DSCP 
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
– 
1 
1 
Both 
Untagged 
Unclassified 
VLAN 
VLAN priority 
VLAN + VLAN priority 
VLAN + DSCP 
Source MAC address 
Destination MAC address 
My-MAC 
Source IP address 
Destination IP address 
My-IP 
 
– 
1 
2    
Both 
 
Note 
Match policy depends on the presence or absence of a flow using a double 
VLAN tag classifier. 
If a port is assigned with single (outer) tag classifier flows only:  
• 
The frame outer VLAN tag is matched to the VLAN classifier, 
regardless of whether the frame has other (inner) VLAN tags. 
If a port is assigned with at least one flow which uses a double tag classifier: 
• 
Frames with at least two VLAN tags (outer and inner) are matched via 
double tag classifier flows only. 
• 
Frames with only one VLAN tag are matched by single tag classifier 
flows. 
• 
It should be noted that if a frame has more than one VLAN tag and 
doesn’t match the double tag classifier, it won’t be matched at all. 
This is true even if its outer VLAN tag matches the single tag classifier. 
This behavior changes on-the-fly with the addition or removal of a double tag 
classifier. 
 
ETX-2i Devices 
5. Traffic Processing 
Note 
If you apply two classification profiles with IP address ranges to a port, the 
profiles must have the same mask. 
For example: 
The following is valid (mask1 equal to mask2): 
Classification #1: 10.10.0.0 –10.10.0.255 -> mask1 = 255.255.255.0 
Classification #2: 20.20.0.0 –20.20.0.255 -> mask2 = 255.255.255.0 
The following is invalid (mask1 not equal to mask2): 
Classification #1: 10.10.0.0–0.10.0.255 -> mask1 = 255.255.255.0 
Classification #2: 20.20.0.0 –20.20.255.255 -> mask2 = 255.255.0.0 
Classification Keys 
The following classification keys are supported per port: 
• 
Legacy  
• 
VLAN 
• 
VLAN Inner VLAN 
The tables below show for the VLAN and VLAN Inner VLAN classification keys, respectively, the queue 
mapping method and the parameters that can be configured in a flow, the range per classification rule, 
maximum number of rules per flow, and the internal flow priority. See the table above for the 
combinations of flow classifications that are allowed per port. 
Queue Mapping Method and Configurable Flow Classification Parameters – VLAN Classification Key 
Queue/Priority 
Mapping Method  
Classification Profile Parameter  
Range (per defined 
classification rule)  
Max. # of 
Rules per Flow 
Internal 
Flow 
priority  
1. Flow 
2. DSCP 
3. P-bit 
Untagged  
NA 
1 
3 
Unclassified  
NA 
1 
2 
VLAN  
VLAN range [0..4094] 
30 
2 
VLAN+P-bit  
VLAN range [0..4094]; 
P-bit range [0..7] 
30 
2 
VLAN+DSCP  
VLAN range [0..4094]; 
DSCP range [0..63] 
30 
2A 
ETX-2i Devices 
5. Traffic Processing 
Queue/Priority 
Mapping Method  
Classification Profile Parameter  
Range (per defined 
classification rule)  
Max. # of 
Rules per Flow 
Internal 
Flow 
priority  
VLAN+IP-P  
VLAN range [0..4094]; 
IP-P range [0..7] 
30 
2A 
VLAN+MAC SA  
Single VLAN value 
SA MAC range 
1 
1 
VLAN+MAC DA  
Single VLAN value 
DA MAC range 
1 
1 
VLAN+IP SA  
VLAN range [0..4094], 
SRC IP  
10 
1 
VLAN+IP DA  
VLAN range [0..4094], 
Dest IP  
10 
1 
VLAN+EtherType  
Single VLAN value and 
single EtherType value 
1 
1 
VLAN+Non-IP  
VLAN Range [0..4094] 
30 
2 
MAC SA  
SA MAC Range 
1 
1 
MAC DA  
DA MAC Range 
1 
1 
IP SA  
SRC IP Range 
1 
1 
IP DA  
DST IP Range 
1 
1 
EtherType  
Single VLAN value  
1 
1 
Non-IP  
NA 
1 
2 
Queue Mapping Method and Configurable Flow Classification Parameters – VLAN Inner VLAN Classification Key 
Queue/Priority 
Mapping Method  
Classification Profile 
Parameter  
Range (per defined 
classification rule)  
Max. # of 
Rules per Flow 
Internal 
Flow 
priority  
4. Flow 
5. DSCP 
6. P-bit 
Untagged  
NA 
1 
3 
Unclassified  
NA 
1 
2 
VLAN, Inner VLAN  
Single Outer value 
Inner VLAN range [0..4094] 
30 
2 
ETX-2i Devices 
5. Traffic Processing 
Queue/Priority 
Mapping Method  
Classification Profile 
Parameter  
Range (per defined 
classification rule)  
Max. # of 
Rules per Flow 
Internal 
Flow 
priority  
VLAN, Inner VLAN, p-bit  
Single Outer value 
Inner VLAN range [0..4094] 
P-bit range [0..7] 
30 
2 
VLAN, Inner VLAN, DSCP 
Single Outer value 
Inner VLAN range [0..4094] 
DSCP range [0..63] 
30 
2 
VLAN, Inner VLAN, non-IP  
VLAN range [0..4094] 
30 
2 
VLAN (one tag level only)  
VLAN range [0..4094] 
30 
2 
MAC SA  
SA MAC range 
1 
1 
MAC DA  
DA MAC range 
1 
1 
IP SA  
SRC IP range 
1 
1 
IP DA  
DST IP range 
1 
1 
EtherType  
Single VLAN value  
1 
1 
Non-IP  
NA 
1 
2 
VLAN Actions 
You can perform marking and tagging actions on the outer and inner VLAN such as adding, replacing, or 
removing, as well as marking with p-bit. Only certain combinations of actions on the outer and inner 
VLAN are allowed. If no action is performed for the outer VLAN, then for the inner VLAN there must be 
no action performed. The table below shows valid VLAN action combinations on ingress frame tags and 
the resulting egress frame tags and p-bits, according to whether the ingress frame is untagged, contains 
one VLAN, or is double-tagged. Any combination not shown in the table is not supported. 
In the ETX-2i bridge, if one of the bridge ports is configured with VLAN classification, and another bridge 
port with VLAN + p-bit classification, in order to mark the p-bit of the inner VLAN, you must mark the 
required p-bit at the VLAN + p-bit bridge port.   
ETX-2i Devices 
5. Traffic Processing 
Valid VLAN Action Combinations 
Action on: 
Egress VLAN(s) and P-bit(s) for Ingress Frame Types: 
Outer VLAN 
Inner VLAN 
Untagged 
One VLAN (X) 
Double VLANs 
(X and Y) 
None 
None 
Untagged 
X 
X, Y 
Pop 
None 
Not applicable – 
unsupported 
Untagged 
Y 
Pop 
Mark with VLAN A 
Not applicable – 
unsupported  
Not applicable – 
unsupported 
A 
Pop 
Pop 
Not applicable – 
unsupported 
Not applicable – 
unsupported 
Untagged 
Push VLAN A 
None 
A 
A, X 
A, X, Y 
Push VLAN A 
Mark with VLAN B 
A 
A, B 
A, B, Y 
Push VLAN A 
Mark with p-bit D 
A 
A, X + p-bit D 
A, X + p-bit D, Y 
Push VLAN A 
Mark with profile F 
A 
A, X + p-bit 
according to F 
A, X + p-bit 
according to F, Y 
Push VLAN A.  
mark with profile E 
Relevant for  
ETX-2i-10G/8SFPP 
Mark VLAN B with 
p-bit copy 
A + p-bit 7 
A+ b-pit according 
to  E, B+pbit copy, X 
A + p-bit according 
to E,  
B + p-bit copy, X, Y 
Push VLAN A.  
mark with profile E 
Push VLAN B, 
mark with p-bit D 
A + p-bit 7 
according to E,  
B + p-bit D 
A + p-bit according 
to E, B + p-bit D, X 
A + p-bit according 
to E, B + p-bit D, X, 
Y 
Push VLAN A.  
mark with p-bit C 
Push VLAN B, 
mark with p-bit D 
A + p-bit C,  
B + p-bit D 
A + p-bit C,  
B + p-bit D, X 
A + p-bit C,  
B + p-bit D, X, Y 
Push VLAN A.  
mark with profile E 
Push VLAN B.  
mark with profile F 
A + p-bit 7 
according to E, 
B + p-bit 7 
according to F  
A + p-bit according 
to E,  
B + p-bit according 
to F, X 
A + p-bit according 
to E,  
B + p-bit according 
to F, X, Y 
Push VLAN A.  
mark with p-bit C 
Push VLAN B.  
mark with profile F 
 
A + p-bit C, 
B + p-bit 7 
according to F  
A + p-bit C,  
B + p-bit according 
to F, X 
A + p-bit C,  
B + p-bit according 
to F, X, Y 
Mark with VLAN A 
None 
Untagged 
A 
A, Y 
Mark with VLAN A 
Mark with p-bit D 
Not applicable – 
unsupported 
Not applicable – 
unsupported 
A,  
Y + p-bit D 
ETX-2i Devices 
5. Traffic Processing 
Action on: 
Egress VLAN(s) and P-bit(s) for Ingress Frame Types: 
Outer VLAN 
Inner VLAN 
Untagged 
One VLAN (X) 
Double VLANs 
(X and Y) 
Mark with p-bit C 
Mark with p-bit D 
Not applicable – 
unsupported 
Not applicable – 
unsupported 
X+ p-bit C,  
Y + p-bit D 
Mark with VLAN A + 
p-bit 
Mark with p-bit D 
Not applicable – 
unsupported 
Not applicable – 
unsupported 
A + p-bit, 
Y + p-bit D 
Mark with VLAN A + 
profile E 
Mark with VLAN B 
+p-bit D 
Not applicable – 
unsupported 
Not applicable – 
unsupported 
A + p-bit according 
to E,B +p-bit D 
Permanent Flow Loopbacks 
You can set up a permanent flow loopback by specifying MAC and IP address swap for flow traffic in the 
marking context and saving it as part of the configuration. 
MAC Address Learning Per Flow 
ETX-2i supports MAC address learning on a specific ETX-2i flow, regardless of whether it is a bridged or 
non-bridged flow (i.e., not connected to the bridge).  
You can then display the MAC addresses associated with this flow. This facilitates troubleshooting 
customer L2 issues, such as loops and broadcast storms in the customer network.  
 
Note 
By default, ETX-2i supports a MAC table at the Bridge level, which includes all 
MAC addresses learned for the bridge. See MAC Address Learning (for Bridge) 
above. 
Unidirectional Hubs 
You can configure a unidirectional hub (UDH) by defining a group of flows with the same ingress port, 
classifier profile, and Policer aggregate, and different egress ports. The egress ports must be physical 
Ethernet ports, not virtual ports such as SVI, ETP, etc. Only one queue-mapping profile and one marking 
profile can be used for the flows in a UDH group; however, VLAN tag editing can be different in the 
different flows. 
In unidirectional hub mode, the rate of each flow that is part of the group cannot exceed the rate of the 
queue with the lowest rate; therefore, it is not possible to use different rates for different p-bits. 
ETX-2i Devices 
5. Traffic Processing 
Multi-CoS Flows 
A multi-CoS flow per MEF 10.3 contains multiple classes of service. It can be assigned an Envelope 
Policer (see Envelope Bandwidth Profiles) to enable sharing bandwidth between the CoSs, where each 
CoS is assigned a rank. Alternatively, if bandwidth policing is not required but per-CoS counters are 
required.you can specify that a multi-CoS flow has per-CoS counters. 
 
The CoS-to-rank mapping is done automatically by the device, according to the CoSs that are configured 
in the assigned Envelope Policer. CoS 0 is mapped to the highest rank needed for the number of 
configured CoSs, then CoS 1 is mapped to the next highest rank, ending with mapping the last 
configured CoS to 1. For example, if CoS 1, CoS 5, and CoS 6 are configured, then three ranks are used, 
and the mappings are: 
• 
CoS 1 to rank 3 
• 
CoS 5 to rank 2 
• 
CoS 6 to rank 1 
Traffic that is mapped to a CoS that does not correspond to a CoS configured in the Envelope profile is 
dropped (the port-level counter Unmapped CoS Frames indicates how many frames were dropped for 
this reason). 
Multi-CoS flows must be assigned a CoS mapping profile, which can be used to specify the mapping of 
untagged traffic to CoS in case of p-bit method, or non-IP to CoS in the case of DSCP. 
Multi-CoS flows support only the following ingress/egress ports: 
• 
Ingress and egress port are Ethernet or logical MAC. 
• 
Egress port is bridge port (unidirectional and reverse flows supported). 
• 
Egress port is ETP subscriber or transport port. 
The queue block mapping for the egress port in a multi-CoS flow is done as CoS to queue mapping as 
follows: Cos 0 to queue 0, Cos 1 to queue 1, CoS 2 to queue 2, etc. There is a predefined queue mapping 
profile with this mapping, with the reserved name q-map-for-cos. This profile cannot be modified. 
ETX-2i Devices 
5. Traffic Processing 
If a marking profile is assigned to a multi-CoS flow, it must be type CoS to p-bit. 
Port Classification 
Note 
ETX-2i-100G does not support port classification. 
You can define port classification to flexibly filter packet forwarding for ports. Port classification consists 
of a set of sequentially numbered rules (similar to ACLs), with the following rule types: 
• 
Comment – Text used for commenting and visually organizing the rules. 
• 
Match – Specifies the criteria for forwarding packets, as well as a flow attribute and optional CoS 
(required for Multi-CoS MEF 10.3 flows). 
• 
Drop – Specifies the criteria for dropping packets. 
The following table specifies the port classification criteria. 
Rule Criterion 
Rule Value/Range 
Comments 
Any 
- 
Allows match any or drop any rules 
Destination MAC address 
Value 
 
Source MAC address 
Value 
 
EtherType 
Value 
 
VLAN 
Range [0–4094] 
 
P-bit 
Value [0–7] 
 
DEI 
0 or 1 
 
Inner EtherType 
Value 
 
Inner VLAN 
Range [0–4094] 
 
Inner p-bit 
Value [0–7] 
 
IP DSCP 
Range [0–63] 
 
IP precedence 
Range [0–7] 
 
ToS 
Range [0–255] 
 
IP protocol 
Value 
 
Source IP address  
IP address/length 
IPv4 or IPv6  
Destination IP address 
IP address/length 
IPv4 or IPv6 
TCP Source Port  
Range  
IP Layer 4 

## Factory Defaults  *(p.908)*


## Configuring Flows  *(p.908)*

ETX-2i Devices 
5. Traffic Processing 
Rule Criterion 
Rule Value/Range 
Comments 
TCP Destination Port  
Range 
IP Layer 4 
UDP Source Port  
Range  
IP Layer 4 
UDP Destination Port  
Range 
IP Layer 4 
 
EtherType 
Ingress packets are identified as outer VLAN-tagged packets if the packet outer tag EtherType equals the 
port configured EtherType – 0x8100, 0x88a8, or one of the two user-configurable global EtherType 
values. 
Ingress packets are identified as inner VLAN-tagged packets if the packet inner tag EtherType equals 
0x8100, 0x88a8, or one of the two user-configurable global EtherType values. 
If the packet inner and outer tag EtherTypes do not meet these criteria, the packet is treated as 
untagged. 
Factory Defaults 
By default, no flows or port classifiers are configured. When a flow is created, the factory defaults are as 
in the following table. 
Parameter 
Description 
Default Value 
shutdown 
Enabling/disabling flow 
shutdown 
policer profile 
Associating Policer profile with flow 
“Policer1” 
mac-learning 
Invoking MAC address learning for flow 
no mac-learning 
Configuring Flows 
 To configure all flows: 
1. Navigate to config>flows. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Associating the flow with a 
classifier profile 
classifier-profile <profile-name> match-any 
no classifier-profile <classification-name> 
See Configuring a Classifier 
Profile. 
Note: If the flow is being used 
for port classification (see 
Port Classification), it inherits 
the ingress port from the port 
classification, and does not 
use a classifier profile. 
Clearing MAC address table 
clear-flow-mac-table 
Clears learned MACs for all 
user defined flows. 
Command requires 
confirmation: Learned entries 
within MAC table will be 
cleared. Are you sure? 
[yes/no] 
Associating multi-CoS flow 
with CoS mapping profile 
flow <flow-name> [port-classifier] 
no flow <flow-name> 
See Configuring a Flow. 
Configuring window size for 
sampling rate statistics 
rate-sampling-window 
Possible values: 1-30 minutes 
Default: 15 
Renaming flow or classifier 
rename { flow | classifier } <current name> 
<new name> 
The classifier/flow name is 
replaced in the entire running 
configuration, even while the 
classifier is in use or the flow 
is in no shutdown state, 
without affecting the 
classifier/flow functionality 
(hitless rename). 
The flow name can be a 
maximum of 64 bytes long 
(versions 6.8.2 (0.52),  
6.8.2 (0.55), 6.8.2 (2.52)). 
Configuring an in-service 
ping request  
[no] service-ping 
Refer to Configuring In-
Service ICMP Echo Ping 
Response in the Monitoring 
and Diagnostics chapter. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Configuring an in-service 
ping response 
[no] service-ping-response 
Refer to Configuring In-
Service ICMP Echo Ping 
Request in the Monitoring 
and Diagnostics chapter. 
Generating a detailed report 
of the status of an active 
service-ping command. 
show service-ping-status 
See Flow Service Ping Status. 
The status of a ping request is 
displayed in either one of the 
following two scenarios only: 
• Activated by CLI and 
shown from Telnet or SSH 
• Activated from Telnet/SSH 
and shown from a 
different Telnet/SSH 
session. 
Specifying whether 
transmitted and received 
OAM packets are included in 
the statistics counters for Rx 
and Tx statistics 
[no] statistics-count-oam 
Enter no statistics-count-oam 
if you do not want to include 
transmitted and received 
OAM packets in the statistics; 
this applies to the following 
OAM packets: 
AIS 
CCM’s 
DMM/DMR’s 
LMM/LMR’s 
LBM/LBR’s 
LTM/LTR’s 
Port status TLV 
 
show summary { details | brief } 
 
 
 
ETX-2i Devices 
5. Traffic Processing 
Configuring a Classifier Profile 
You can define classifier profiles to apply to flows for flow classification. 
Notes 
• 
Classifier profiles are not used for flows that are defined with the port 
classification attribute. 
• 
When a classification profile is assigned to a flow, each match in the 
profile is allocated one of the available internal classification match 
entries, according to the flow ingress port. 
• 
For example, if a classification profile is defined with matches to two 
different VLANS, then if the profile is assigned to two flows that use 
different ingress ports, the result is that four internal classification match 
entries are allocated. If the profile is assigned to two flows that use the 
same ingress port, the result is that two internal classification match 
entries are used. 
 To define a classifier profile: 
1. Navigate to the flows context (config>flows). 
2. Define a classifier profile and assign a name to it: 
classifier-profile <profile-name> match-any 
The system switches to the context of the classifier profile (config>flows>classifier-
profile(<profile-name>)). 
Specify the criteria for the classifier profile: 
[no] match [sequence <sequence-number>] [vlan <vlan-range>] [inner-vlan <inner-vlan-range>] 
[p-bit <p-bit-range>] [ip-precedence <ip-precedence-range>] [ip-dscp <ip-dscp-range>] 
[src-mac <src-mac-low>] [to-src-mac <src-mac-high>] [dst-mac <dst-mac-low>] 
[to-dst-mac <dst-mac-high>] [src-ip <src-ip-low>] [to-src-ip <src-ip-high>] [dst-ip <dst-ip-low>] 
[to-dst-ip <dst-ip-high>] [ether-type <ether-type>] [untagged] [non-ip] [my-mac] [my-ip] [all] 
 
Note 
Using the matching type my-mac or my-ip is equivalent to using the matching 
type dest-mac <device-MAC-address> or dest-ip <host-IP-address>. 
3. When you have completed specifying the criteria, enter exit to exit the classifier profile context. 
 
ETX-2i Devices 
5. Traffic Processing 
Configuring a Flow 
 To configure a flow: 
1. Navigate to config>flows. 
2. Enter flow <flow-number>  
If the flow already exists, the config>flows>flow(<flow-number>)# prompt is displayed, 
otherwise the flow is created and the config>flows>flow(<flow-number>)$ prompt is displayed. 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Associating the flow with a classifier 
profile 
[no] classifier <classifier-profile-
name> 
If the flow is multi-CoS, the 
classification must be one of 
the following: 
• VLAN, VLAN + inner VLAN, 
VLAN range 
• Match all 
• Untagged 
This command cannot be used 
if port-classifier was specified 
for the flow. 
 
clear-statistics 
 
Associating multi-CoS flow with CoS 
mapping profile 
[no] cos-mapping profile 
<cos-mapping-profile-name> 
This command cannot be used 
if port-classifier is specified 
for the flow. 
Not relevant for ETX-2i-100G. 
 
Discarding traffic transmitted via the flow 
[no] drop 
 
Specifying the egress port, and defining 
queue 
egress-port ethernet 
[<slot>/]<port> [queue <queue-id> 
block <level-id/queue-id>] 
egress-port ethernet 
[<slot>/]<port> 
[queue-map-profile 
<queue-map-profile-name> 
block <level-id/queue-id>] 
egress-port ethernet <port> 
[block <level-id/queue-id>] 
If a queue mapping profile is 
used, it must be compatible 
with the classification criteria 
of the flow, e.g., if the 
classification is according to 
DSCP then the queue mapping 
should not be according to 
p-bit. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
egress-port bridge-port 
<bridge-number> 
<bridge-port-number> [cos 
<cos-id>] 
egress-port bridge-port 
<bridge-number> 
<bridge-port-number> 
[cos-map-profile 
<cos-map-profile-name>] 
egress-port etp <etp-name> 
{subscriber | transport} 
<port-number> [cos <cos-id>] 
egress-port etp <etp-name> 
{subscriber | transport} 
<port-number> [cos-map-profile 
<cos-map-profile-name>] 
egress-port logical-mac <port> 
[queue <queue-id> 
block <level-id/queue-id>] 
egress-port logical-mac <port> 
[queue-map-profile 
<queue-map-profile-name> 
block <level-id/queue-id>] 
egress-port logical-mac <port> 
[block <level-id/queue-id>] 
egress-port pcs <port> [queue 
<queue-id> 
block <level-id/queue-id>] 
egress-port pcs <port> 
[queue-map-profile 
<queue-map-profile-name> 
block <level-id/queue-id>] 
egress-port pcs <port> 
[block <level-id/queue-id>] 
egress-port svi <port> 
[queue <queue-id>] 
egress-port svi <port> 
[queue-map-profile 
<queue-map-profile-name>] 
For multi-CoS flows, the 
predefined q-map-for-cos 
queue mapping profile should 
be used.  
Note:  
• In the case that you 
choose to configure two 
flows between a bridge 
port and physical port (as 
opposed to one 
bidirectional flow), you 
cannot configure a queue 
number in the egress 
physical port of the flow 
where the bridge port is 
the ingress port, as the 
physical port’s queue is 
automatically taken from 
the CoS configured in the 
flow in the other direction 
(with egress bridge port 
and ingress physical port).  
Doing so results in the 
following error: A flow 
from bridge port must not 
use a Queue Mapping or a 
Queue Mapping profile.   
• If working with PW, 
packets forwarded from 
the SVI must be untagged 
or match all and push any 
necessary VLAN. 
Adding no before the 
command, removes the 
egress port. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Specifying the ingress packet color 
ingress-color green 
ingress-color yellow 
ingress-color profile 
<color-mapping-profile-name> 
You can set the packet color 
to green or yellow or use a 
color mapping profile (see 
Color Mapping Profiles). 
Specifying the ingress port   
ingress-port ethernet 
[<slot>/]<port> 
ingress-port bridge-port 
<bridge-number> 
<bridge-port-number> 
ingress-port etp <etp-name> 
{subscriber | transport} 
<port-number> 
ingress-port logical-mac <port> 
ingress-port pcs <port> 
ingress-port svi <port> 
This command cannot be used 
if port-classifier is specified 
for the flow. 
Note:  
• If working with PW, 
packets forwarded to the 
SVI must be untagged, and 
pop any VLAN. 
• Adding no before the 
command, removes the 
ingress port. 
Associating a Layer-2 control processing 
profile with the flow 
[no] l2cp profile 
<l2cp-profile-name> 
L2CP profile can be attached 
only to flows with the 
following classification types: 
• VLAN/VLAN+P-bit 
• Outer+Inner VLAN / Outer 
+P-bit + Inner VLAN 
• P-bits 
• VLAN+Non-IP 
• Untagged 
For an explanation on how to 
configure an L2CP profile, see 
Layer-2 Control Protocol 
(L2CP) Processing. 
Invoking MAC address learning for flow 
[no] mac-learning 
MAC learning can be enabled 
for bridge and non-bridge 
flows. 
Note: Toggling mac-learning 
in a flow that is bound to an 
active Y.1564 test, disrupts 
the test. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Defining marking actions for the flow 
such as overwriting the VLAN ID or inner 
VLAN ID or setting the priority, or 
specifying MAC and IP address swap 
mark all 
no mark 
See the following table for the 
marking actions. 
Associating the flow with a marking 
profile 
marking-profile <marking-profile-
name> 
no marking-profile 
marking-profile-name – 1-32 
characters  
Specifying that the flow is a multi-CoS 
flow with counters for the multiple CoS  
multi-cos-counters <cos-list> 
cos-list - the list of CoS values 
for the flow; can be a range 
such as 1..3 or a list of values 
such as 2,4,5 
Possible values: 0-7 
Note: You can assign either 
multiple CoS counters or an 
Envelope Policer to a 
multi-CoS flow; you cannot 
assign both. 
Not relevant for ETX-2i-100G. 
Enabling collection of performance 
management statistics for the flow  
pm-collection interval <seconds> 
no pm-collection 
Performance management 
statistics are presented via 
the RADview Performance 
Management portal. Refer to 
the Performance 
Management section in the 
Monitoring and Diagnostics 
chapter for details. 
Note: You must ensure that 
PM statistics collection is also 
enabled for the device.  
Associating regular flow with a 
non-Envelope Policer profile or Policer 
aggregate 
[no] policer profile 
<policer-profile-name> 
[no] policer 
aggregate <policer-aggregate-nam
e> 
Note: You cannot assign a 
Policer profile to a flow with a 
bridge port as ingress port. 
 
Associating multi-CoS flow with Envelope 
Policer 
policer envelope 
<policer-profile-name> 
You can assign either an 
Envelope Policer or multiple 
CoS counters to a multi-CoS 
flow; you cannot assign both. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Using the flow for port classification 
port-classifier 
If port-classifier is specified, 
this flow is used for port 
classification, and the 
commands ingress-port, 
classifier, reverse-direction, 
and cos-mapping are not 
used. 
Note: ETX-2i-100G does not 
support port classification.  
Measuring data rate and line rate of flow 
rate-measure interval <seconds> 
no rate-measure 
Possible values: 10–300  
See Viewing Flow Data Rate 
and Line Rate for details. 
Configuring window size for sampling 
rate statistics 
rate-sampling-window 
Possible values: 1-30 minutes 
Default: 15 
Note: Configuration of this 
parameter for a specific flow 
overrides the configuration 
for al flows (under the flows 
level). 
Defining flow to bridge port as 
bidirectional, if bridge is VLAN-aware 
reverse-direction 
block <queue-block-id> 
Note: This command is 
allowed only if port-classifier 
is not specified for the flow, 
the bridge is VLAN-aware, and 
the egress port is a bridge 
port. 
Assigning service name to flow for its 
subsequent discovery by RADview 
[no] service-name <name> 
The flows that belong to the 
same service must be tagged 
in both directions. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Displaying MAC addresses learned for 
this flow 
show mac-table [mac-address 
<mac-address>] 
This command is available 
only after enabling mac-
learning (see above).  
If no mac-address is specified, 
all learned MAC addresses are 
displayed in a table. If no MAC 
addresses have been learned 
on this flow, returns MAC Not 
Found. 
If a specific mac-address is 
specified, running the 
command searches whether 
the specified MAC address 
was learned on this flow. If 
found, returns MAC Found. 
Otherwise, returns MAC Not 
Found. 
See Viewing Learned MAC 
Addresses on Flow. 
Note: You can clear the entire 
MAC table for all user-defined 
flows using the clear-flow-
mac-table command under 
the config>flows level. 
Confirmation is requested 
before clearing the table. 
Displaying measured flow data rate and 
line rate 
show rate 
See Viewing Flow Data Rate 
and Line Rate for details. 
Displaying flow status 
show status 
Fault propagation actions are 
visible only for flows 
configured with fault 
propagation and activated 
fault propagation license. 
See Viewing Flow Status. 
Displaying flow test status 
show test 
 
Performing MAC swap loopback test 
[no] test [{ mac-swap | ip-swap }] 
[duration <seconds>] 
[ttl-force <ttl>] 
See Testing Flows. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Adding VLAN ID with p-bit set to specific 
value, and optionally adding inner VLAN 
ID with EtherType (optional) and with 
p-bit set to specific value 
vlan-tag push vlan <sp-vlan> p-bit 
fixed <fixed-p-bit> [inner-vlan 
<inner-sp-vlan>[inner-ether-type 
<inner-ether-type>] 
p-bit fixed <inner-fixed-p-bit>] 
Inner-ether-type can be 
configured to one of the four 
global device level EtherTypes 
(refer to the EtherType 
section in the Cards and Ports 
chapter). 
If not configured, the inner 
EtherType is set to 0x8100. 
Adding VLAN ID with p-bit set to specific 
value, and optionally adding inner VLAN 
ID with EtherType (optional) and with 
p-bit set via marking profile 
vlan-tag push vlan <sp-vlan> p-bit 
fixed <fixed-p-bit> [inner-vlan 
<inner-sp-vlan> [inner-ether-type 
<inner-ether-type>] 
p-bit profile <inner-marking-profil
e-name>] 
Inner-ether-type can be 
configured to one of the four 
global device level EtherTypes 
(refer to the EtherType 
section in the Cards and Ports 
chapter). 
If not configured, the inner 
EtherType is set to 0x8100. 
Adding VLAN ID with p-bit set to specific 
value, and optionally adding inner VLAN 
ID with EtherType (optional) and with 
p-bit set by copying from the incoming 
frame 
vlan-tag push vlan <sp-vlan> p-bit 
fixed <fixed-p-bit> [inner-vlan 
<inner-sp-vlan> [inner-ether-type 
<inner-ether-type>] p-bit copy] 
Inner-ether-type can be 
configured to one of the four 
global device level EtherTypes 
(refer to the EtherType 
section in the Cards and Ports 
chapter). 
If not configured, the inner 
EtherType is set to 0x8100. 
Adding VLAN ID with p-bit set via 
marking profile, and optionally adding 
inner VLAN ID with EtherType (optional) 
and with p-bit set to specific value 
vlan-tag push vlan <sp-vlan> 
p-bit profile <marking-profile-nam
e> [inner-vlan <inner-sp-vlan> 
[inner-ether-type <inner-ether-
type>] 
p-bit fixed <inner-fixed-p-bit>] 
Inner-ether-type can be 
configured to one of the four 
global device level EtherTypes 
(refer to the EtherType 
section in the Cards and Ports 
chapter). 
If not configured, the inner 
EtherType is set to 0x8100. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Adding VLAN ID with p-bit set via 
marking profile, and optionally adding 
inner VLAN ID with EtherType (optional) 
and with p-bit set via marking profile 
vlan-tag push vlan <sp-vlan> 
p-bit profile <marking-profile-nam
e> [inner-vlan <inner-sp-vlan> 
[inner-ether-type <inner-ether-
type>] 
p-bit profile <inner-marking-profil
e-name>] 
Inner-ether-type can be 
configured to one of the four 
global device level EtherTypes 
(refer to the EtherType 
section in the Cards and Ports 
chapter). 
If not configured, the inner 
EtherType is set to 0x8100. 
Adding VLAN ID with p-bit set via 
marking profile, and optionally adding 
inner VLAN ID with EtherType (optional) 
and with p-bit set by copying from the 
incoming frame 
vlan-tag push vlan <sp-vlan> 
p-bit profile <marking-profile-nam
e> [inner-vlan <inner-sp-vlan> 
[inner-ether-type <inner-ether-
type>] p-bit copy] 
Inner-ether-type can be 
configured to one of the four 
global device level EtherTypes 
(refer to the EtherType 
section in the Cards and Ports 
chapter). 
If not configured, the inner 
EtherType is set to 0x8100. 
Adding VLAN ID with p-bit set by copying 
from the incoming frame, and optionally 
adding inner VLAN ID with EtherType 
(optional) and with p-bit set to specific 
value: 
vlan-tag push vlan <sp-vlan> 
p-bit copy 
[inner-vlan <inner-sp-vlan> 
[inner-ether-type <inner-ether-
type>] 
p-bit fixed <inner-fixed-p-bit>] 
Inner-ether-type can be 
configured to one of the four 
global device level EtherTypes 
(refer to the EtherType 
section in the Cards and Ports 
chapter). 
If not configured, the inner 
EtherType is set to 0x8100. 
Adding VLAN ID with p-bit set by copying 
from the incoming frame, and optionally 
adding inner VLAN ID with EtherType 
(optional) and with p-bit set via marking 
profile 
vlan-tag push vlan <sp-vlan> 
p-bit copy 
[inner-vlan <inner-sp-vlan> 
[inner-ether-type <inner-ether-
type>] 
p-bit profile <inner-marking-profil
e-name>] 
Inner-ether-type can be 
configured to one of the four 
global device level EtherTypes 
(refer to the EtherType 
section in the Cards and Ports 
chapter). 
If not configured, the inner 
EtherType is set to 0x8100. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Adding VLAN ID with p-bit set by copying 
from the incoming frame, and optionally 
adding inner VLAN ID with EtherType 
(optional) and with p-bit set by copying 
from the incoming frame 
vlan-tag push vlan <sp-vlan> 
p-bit copy 
[inner-vlan <inner-sp-vlan> 
[inner-ether-type <inner-ether-
type>] p-bit copy] 
Inner-ether-type can be 
configured to one of the four 
global device level EtherTypes 
(refer to the EtherType 
section in the Cards and Ports 
chapter). 
If not configured, the inner 
EtherType is set to 0x8100. 
Removing VLAN ID, and optionally 
removing inner VLAN ID 
vlan-tag pop vlan [inner-vlan] 
 
Removing pushing of inner VLAN 
no vlan-tag [push inner-vlan] 
 
Displaying the flow statistics 
show statistics running 
See Viewing Flow Statistics. 
Administratively enabling the flow 
no shutdown 
• You can activate a flow 
only if it is associated with 
at least a classifier profile, 
ingress port, and egress 
port. 
• A flow from a bridge port 
to a physical port cannot 
be activated if another 
flow from the same bridge 
port, in the same VPN, 
exits to a different egress 
cluster (physical port and 
queue block). This applies 
to unidirectional flows and 
to the reverse direction of 
bidirectional flows. 
• Enter shutdown to disable 
the flow. 
The following marking actions can be performed in the mark level, at the 
config>flows>flow(<flow-name>)>mark# prompt. 
Task 
Command 
Comments 
Specifying permanent flow 
loopback with IP address 
swap 
ip swap 
 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Specifying permanent flow 
loopback with MAC address 
swap 
mac swap 
 
Overwriting p-bit according 
to marking profile 
marking-profile <marking-profile-name> 
If a marking profile is used, it 
must be compatible with the 
classification criteria of the 
flow, e.g., if the flow 
classification is according to 
DSCP, then the marking 
classification should not be 
according to p-bit. 
If the flow is multi-CoS, the 
marking profile must be of 
type CoS to p-bit. 
If a color-aware marking profile 
is applied for the outer VLAN of 
a flow, then if marking is 
applied to the inner VLAN, 
either the same color-aware 
marking profile must be used 
for the inner VLAN, or a 
non-color-aware marking 
profile must be used for the 
inner VLAN. 
Entering no marking-profile or 
no inner-marking-profile 
removes the overwriting of 
marking profile or inner 
marking profile respectively. 
Overwriting inner p-bit 
according to marking profile 
inner-marking-profile 
<inner-marking-profile-name> 
See comments for 
marking-profile. 
Overwriting p-bit with a new 
value 
p-bit <p-bit-value> 
Entering no p-bit removes the 
overwriting of p-bit. 
Overwriting inner p-bit with 
a new value 
inner-p-bit <inner-p-bit-value> 
Entering no inner-p-bit 
removes the overwriting of 
inner p-bit. 
Overwriting VLAN ID with a 
new value 
vlan <vlan-value> 
Entering no vlan removes the 
overwriting of VLAN ID. 

## Configuring Port Classification  *(p.922)*

ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Overwriting EtherType value  
 
ether-type <ether-type> 
ether-type can be configured 
to one of the four global device 
level EtherTypes (refer to the 
EtherType section in the Cards 
and Ports chapter). 
If not configured, ethertype is 
set to 0x8100. 
Entering no ether-type 
removes the overwriting of the 
EtherType. 
Overwriting inner EtherType 
value  
inner-ether-type <inner-ether-type> 
inner-ether-type can be 
configured to one of the four 
global device level EtherTypes 
(refer to the EtherType section 
in the Cards and Ports 
chapter). 
If not configured, inner-
ethertype is set to 0x8100. 
Entering no inner-ether-type 
removes the overwriting of the 
inner EtherType. 
Overwriting inner VLAN ID 
with a new value   
inner-vlan <inner-vlan-value>  
Entering no inner-vlan 
removes the overwriting of 
inner VLAN ID. 
Exiting the marking context 
and returning to the flow 
context 
exit 
 
Configuring Port Classification 
Note 
All ETX-2i devices, with the exception of ETX-2i-100G, support port 
classification. 
Port classification can be configured for the following ports: 
• 
Ethernet ports 
• 
Redundancy LAG ports. Port classifier rules are configured over the logical LAG port (LAG anchor 
port). 
ETX-2i Devices 
5. Traffic Processing 
• 
Logical MAC 
• 
PCS port 
 To configure port classification for Ethernet/LAG/logical MAC/PCS port: 
1. Navigate to configure port {ethernet [<slot>/]<port> | lag <port> | logical-mac <port>| 
pcs <port>}classifier. 
Note 
In the case of a LAG port, the port classifier rules must be configured for the 
anchor port. 
Exception: Ethernet ports in a LAG group, which are configured with G.8275.1 
PTP. In this case, port classifier rules are configured individually for each 
physical Ethernet port in the LAG group and not on the anchor port. 
2. At the prompt, perform the required tasks according to the following table. 
Task 
Command 
Comments 
Adding comment rule 
comment <description> 
[sequence <sequence-number>] 
description – text 
description 
sequence-number – 
sequence number for 
comment 
Removing rule 
delete <sequence-number> 
 
Adding drop rule 
drop [dst-mac <dst-mac-address>] 
[src-mac <src-mac-address>] 
[ether-type <ether-type>] [vlan <vlan>] 
[p-bit <p-bit>] [dei {0 | 1}] 
[inner-ether-type <inner-ether-type>] 
[inner-vlan <inner-vlan>] 
[inner-p-bit <inner-p-bit>] 
[ip-dscp <ip-dscp>] 
[ip-precedence <ip-precedence>] 
[tos <tos>] [protocol <protocol>] 
[src-ip <src-ip-address>] 
[dst-ip <dst-ip-address>] 
[tcp-src-port <tcp-src-port>] 
[tcp-dst-port <tcp-dst-port>] 
[udp-src-port udp-src-port>] 
[udp-dst-port <udp-dst-port>] [any] 
[sequence <sequence-number>] 
Up to five criteria can be 
specified; they must be in 
the same order in which 
they appear in the 
command syntax 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Adding match rule 
match [dst-mac <dst-mac-address>] 
[src-mac <src-mac-address>] 
[ether-type <ether-type>] [vlan <vlan>] 
[p-bit <p-bit>] [dei {0 | 1}] 
[inner-ether-type <inner-ether-type>] 
[inner-vlan <inner-vlan>] 
[inner-p-bit <inner-p-bit>] 
[ip-dscp <ip-dscp>] 
[ip-precedence <ip-precedence>] 
[tos <tos>] [protocol <protocol>] 
[src-ip <src-ip-address>] 
[dst-ip <dst-ip-address>] 
[tcp-src-port <tcp-src-port>] 
[tcp-dst-port <tcp-dst-port>] 
[udp-src-port udp-src-port>] 
[udp-dst-port <udp-dst-port>] [any] 
[sequence <sequence-number>] 
to-flow <flow-name> 
{[to-cos-fixed <fixed-cos>] | 
[to-cos-profile <profile-cos>]} 
• Up to five criteria can be 
specified; they must be 
in the same order in 
which they appear in the 
command syntax 
• The flow specified by 
to-flow <flow-name> 
has to be defined as a 
flow with parameter 
port-classifier. 
• CoS is optional; it can be 
specified via 
to-cos-fixed as a fixed 
value or via 
to-cos-profile as a 
profile. 
• You can define G.8275.1 
PTP over a physical port 
in a LAG group, by 
configuring the 
command: match ether-
type 0x88f7 to-flow 
<flow-name>  
Resequencing the rules  
resequence [<step>] 
If you need to add a rule 
between existing rules with 
consecutive sequence 
numbers, use this command 
to add space between the 
rule sequence numbers. 
The <step> parameter 
specifies the interspacing 
value. For example, if you 
apply resequence 30 to a 
port classification that 
contains rules 1, 2, and 3, 
the rule sequence numbers 
change to 30, 60, and 90. 
Displaying port classifier 
status 
show status 
 
 

## Testing Flows  *(p.925)*

ETX-2i Devices 
5. Traffic Processing 
Testing Flows  
MAC swap loopback tests support two different use cases (methods): 
• 
Application layer loopback – performs MAC swap loopback of traffic with certain characteristics 
(e.g., MAC address, VLAN+MAC, etc.) by configuring a dedicated flow for this purpose 
• 
Flow diagnostics loopback – performs MAC swap loopback over an existing configured flow 
Note 
MAC swap is not performed if the flow is part of a unidirectional hub.  
Application Layer Loopback 
In this use case, an application layer loopback test is applied over a dedicated configured flow with a test 
mac-swap attribute. In this case, the egress port must be configured to be equal to the ingress port. 
You can run application layer loopbacks on a flow, with exchange of source and destination MAC 
addresses or IP addresses of incoming packets. This applies to all the data associated with the flow.  
Note 
Regardless of whether the mac-swap or ip-swap option is specified, if there is 
an IP header in the frames, then both MAC and IP addresses are swapped; 
otherwise only the MAC address is swapped.  
The following procedure shows how to run an application layer loopback test using a flow.  
 To run an application layer flow loopback test: 
1. Navigate to configure flows flow <flow-name> to select an existing flow. 
The config>flows>flow(<flow-name>)# prompt is displayed. 
2. Create a flow with the ingress port equal to the egress port with a test mac-swap attribute. 
test [{mac-swap | ip-swap}] [duration <seconds>] [ttl-force <ttl>] 
The flow is activated upon flow ‘no-shutdown’, and the TEST LED turns on. The test runs for the 
duration specified. If 0 is specified for the duration, the test runs until it is stopped manually, 
and the loop remains after reset (including MAC/IP swap).  
 To end the test: 
1. Delete the flow OR 
Navigate to configure flows flow <flow-name> to select the flow being tested. 
The config>flows>flow(<flow-name>)# prompt is displayed. 
2. Enter:  
no test 

## Viewing Learned MAC Addresses on Flow  *(p.926)*

ETX-2i Devices 
5. Traffic Processing 
Flow Diagnostics Loopback 
This method, supported over a point-to-point service, performs the loopback test using only one flow 
attribute – test mac-swap. No other changes are required to the flow; there is no need to configure 
egress port = ingress port, or to shut down the flow and associated MEPs. The loop command is cleared 
after reset.  
 To run flow diagnostics loopback test: 
1. Navigate to configure flows flow <flow-name> to select an existing flow. 
The config>flows>flow(<flow-name>)# prompt is displayed. 
2. Enter:  
test [{mac-swap|] [duration <seconds>]  
The TEST LED turns on. The test runs for the duration specified. If 0 is specified for the duration, 
the test runs until it is stopped manually.  
 To end the test: 
1. Navigate to configure flows flow <flow-name> to select the flow being tested. 
The config>flows>flow(<flow-name>)# prompt is displayed. 
2. Enter:  
no test 
Viewing Learned MAC Addresses on Flow 
You can display all learned MACs on a user-defined flow, or search for a specific MAC address on a flow. 
 To show all learned MACs (two learned MACs): 
ETX-2i>config>flows>flow(1)# show mac-table 
Total MAC Addresses   :  2 
 
MAC Addresses 
--------------------------------------------------------------- 
40-A8-F0-3E-C2-2B 
6
05
-
8
-CA-28-22-7B 
 
 

## Viewing Flow Status  *(p.927)*


## Viewing Flow Statistics  *(p.927)*

ETX-2i Devices 
5. Traffic Processing 
 To show all learned MACs (no learned MACs): 
ETX-2i>config>flows>flow(1)# show mac-table 
MAC Not Found 
--------------------------------------------------------------- 
 To search for a MAC address (learned on flow 1): 
ETX-2i>config>flows>flow(1)# show mac-table 40-A8-F0-3E-C2-2B 
MAC Found 
--------------------------------------------------------------- 
 To search for a MAC address (not learned on flow 1): 
ETX-2i>config>flows>flow(1)# show mac-table 40-A8-F0-3E-AA-AA 
MAC Not Found 
--------------------------------------------------------------- 
Viewing Flow Status  
You can display the operational status and reverse operational status of a flow, as well as the service 
name for flows configured with a service. Fault propagation actions are visible only for flows configured 
with fault propagation and fault propagation license activated. 
Viewing Flow Statistics  
You can display the number of forwarded and discarded packets and bytes for a flow (Rx and Tx), 
specifying whether transmitted and received OAM packets are included.  
You can enter no statistics-count-oam to exclude transmitted and received OAM packets in the 
statistics. This applies to the following OAM packets: 
• 
AIS 
• 
CCM’s 
• 
DMM/DMR’s 
• 
LMM/LMR’s 
• 
LBM/LBR’s 
• 
LTM/LTR’s 
• 
Port status TLV 
ETX-2i Devices 
5. Traffic Processing 
ETP subscriber flow statistics include: 
• 
Red dropped counters at Policer, as the logical flow extends to the ETP and not to the Egress 
port. 
• 
Green and yellow dropped counters, reflecting the statistic of the flow up to the Egress port. 
Note 
See Configuring Policer Aggregate Parameters for information on displaying 
statistics for flows associated with Policer aggregates.  
 To display the statistics for a flow: 
• 
At the relevant flow context (config>flows>flow(<flow-id>)), enter: 
show statistics running 
Flow statistics are displayed.  
ETX-2i>config>flows>flow(mng_v51_in)# show statistics running 
Rate Sampling Window 
----------------------------------------------------------------------------- 
Window Size [Min.]        : 15 
Window Remain Time [Min.] : 8 
 
 
Rx Statistics 
----------------------------------------------------------------------------- 
          Total 
Packets : 5478132 
Bytes   : 552356312 
 
Drop Statistics 
----------------------------------------------------------------------------- 
             Packets              Bytes 
Total      : 904209               90687706 
Green      : 798642               81984940 
Yellow     : 105567               8702766 
Red        : 0                    0 
Yellow/Red : 105567               8702766 
 
 
Drop Rate 
----------------------------------------------------------------------------- 
                   pps          L1 (bps)             L2 (bps) 
Total(Rate)      : 1            1293                 1054 
Green(Rate)      : 1            1293                 1054 
Yellow(Rate)     : 0            0                    0 
Red(Rate)        : 0            0                    0 
Yellow/Red(Rate) : 0            0                    0 
 
 
 
 

## Viewing Flow Data Rate and Line Rate  *(p.929)*

ETX-2i Devices 
5. Traffic Processing 
Tx Statistics 
----------------------------------------------------------------------------- 
         Packets              Bytes 
Total  : 4573923              461668606 
Green  : 4573866              461641624 
Yellow : 57                   26982 
 
 
Tx Rate 
----------------------------------------------------------------------------- 
         pps          L1 (bps)             L2 (bps) 
Total  : 12           10833                8891 
Green  : 12           10833                8891 
Yellow : 0            0                    0 
 
 
Peak Measurement 
----------------------------------------------------------------------------- 
                      L1 Min               L2 Min               L1 Max               L2 Max 
Tx Bit Rate [bps]   : 264                  264                  57728                50528 
Drop Bit Rate [bps] : 0                    0                    29504                24384 
 
Note 
Bytes counter value is relevant for the four highest capacity VPNs or 16 
highest capacity flows (as defined by the relevant Shaper setting). 
 To clear the statistics for a flow: 
• 
At the relevant flow context (config>flows>flow(<flow-id>)), enter: 
clear-statistics 
The statistics for the flow are cleared. 
Viewing Flow Data Rate and Line Rate 
You can measure the data rate and line rate at which flows transmit and receive, for a configurable time 
interval of 10–300 seconds.  
After you enter the command to measure the rates, ETX-2i automatically displays the results when the 
specified time interval ends.  
The data rate is calculated by dividing the number of total bytes (not including line overhead) by the 
time interval. The line rate is calculated by dividing (number of total bytes + (number of packets x 20 
bytes of line overhead)) by the time interval. 

## Examples  *(p.930)*

ETX-2i Devices 
5. Traffic Processing 
 To start data rate and line rate measurements for flow: 
• 
At the prompt config>flows>flow(<name>)#, enter: 
rate-measure interval <seconds> 
The rate measurement starts. You can use show rate to monitor how much of the time interval 
has elapsed. The result is automatically displayed, without the need to enter show rate, after 
the specified time interval ends. 
Examples 
Classifier Profiles 
 To create a classifier profile with criteria VLAN 100 to VLAN 150: 
exit all 
configure flows classifier-profile v100_150 match-any 
match vlan 100..150 
exit all 
 To create a classifier profile with criteria VLAN 20 and inner VLAN 30: 
exit all  
configure flows classifier-profile v20_inner_30 match-any 
match vlan 20 inner-vlan 30 
exit all 
 To create a classifier profile that matches all criteria: 
exit all  
configure flows classifier-profile all match-any 
match all 
exit all 
Traffic Flows 
This section provides an example of configuring the following flows: 
• 
Outgoing traffic from port ETH 0/3 to port ETH 0/1: 
 
Accept only traffic tagged with VLAN 10. 
 
Add VLAN 100 with p-bit 5 (this causes VLAN 100 to be the outer VLAN and VLAN 10 to be 
the inner VLAN). 
 
 
ETX-2i Devices 
5. Traffic Processing 
• 
Incoming traffic from port ETH 0/1 to port ETH 0/3: 
 
Accept only traffic tagged with VLAN 100 and inner VLAN 10. 
 
Remove the outer VLAN (VLAN 100). 
 To configure the flows: 
#*******Configure v10 classifier profile for outgoing flow  
exit all 
configure flows  
classifier-profile v10 match-any 
match vlan 10 
exit  
 
#*******Configure outgoing flow with v10 classifier profile,  
#********* with ingress at ETH 1/3, egress at ETH 0/1,  
#********* and pushing VLAN 100 with p-bit 5 
flow f10_out 
classifier v10 
ingress-port ethernet 0/3 
egress-port ethernet 0/1 queue 0 block 0/1 
vlan-tag push vlan 100 p-bit fixed 5 
service-name v10 
pm-collection interval 900 
no shutdown 
exit  
 
#*******Configure v100_inner_v10 classifier profile for incoming flow 
classifier-profile v100_inner_v10 match-any 
match vlan 100 inner-vlan 10 
exit  
 
#*******Configure flow with v100_inner_v10 classifier profile, 
#********* ingress at ETH 0/1, egress at ETH 0/3, and popping the outer VLAN 
flow f100_in 
classifier v100_inner_v10 
ingress-port ethernet 0/1 
egress-port ethernet 0/3 queue 0 block 0/1 
vlan-tag pop vlan  
service-name v10 
pm-collection interval 900 
no shutdown 
exit all 
 
 
ETX-2i Devices 
5. Traffic Processing 
ETP Flows 
This section provides an example of configuring the following flows:   
• 
Flow sub1: 
 
Ingress = ethernet 0/3 
 
Egress = etp ETP1 subscriber 1, CoS mapping profile my-p-bit (see Configuring CoS Mapping 
Profiles for details on CoS mapping profiles) 
• 
Flow trans1: 
 
Ingress = etp ETP1 transport 1 
 
Egress = ethernet 0/1, queue 0, block 0/1 
 To configure ETP flows: 
#**************Configure flow sub1 
exit all 
configure flows 
flow sub1 
ingress-port ethernet 0/3 
egress-port etp ETP1 subscriber 1 cos-mapping my-p-bit 
exit 
 
#**************Configure flow trans1 
flow trans1 
ingress-port etp ETP1 transport 1 
egress-port ethernet 0/1 queue 0 block 0/1 
exit all 
ETP Subscriber Flow Statistics 
This example displays statistics of ETP subscriber flow sub1 (see configuration in the ETP Flows example 
above. 
 To display flow statistics (ETP): 
ETX-2i# configure flows flow sub1 
ETX-2i>config>flows>flow(sub1)# show statistics running 
Rate Sampling Window 
----------------------------------------------------------------------------- 
Window Size [Min.]        : 15 
Window Remain Time [Min.] : 12 
 
 
 
ETX-2i Devices 
5. Traffic Processing 
Rx Statistics 
----------------------------------------------------------------------------- 
          Total 
Packets : 20000 
Bytes   : 20000000 
 
Drop Statistics 
----------------------------------------------------------------------------- 
 
                   Packets              Bytes 
Total            : 197941               197941000 
Green            : 197941               197941000 
Yellow           : 0                    0 
Red              : 0                    0 
Yellow/Red       : 0                    0 
Drop  Rate 
-----------------------------------------------------------------------------  
                               pps           L1 (bps)        L2(bps) 
Total(Rate)      :             243           1947758         1800000 
Green(Rate)      :             243           1947758         1800000 
Yellow(Rate)     :             0             0               0 
Red(Rate)        :             0             0               0 
Yellow/Red(Rate) :             0             0               0 
Tx Statistics  
-----------------------------------------------------------------------------  
                               Packets       Bytes  
Total            :             197941        197941000  
Green            :             197941        197941000  
Yellow           :             0             0  
Tx  Rate 
-----------------------------------------------------------------------------  
                               pps           L1 (bps)        L2(bps) 
Total(Rate)      :             243           1947758         1800000 
Green(Rate)      :             243           1947758         1800000 
Yellow(Rate)     :             0             0               0 
Peak Measurement  
-----------------------------------------------------------------------------  
                               L1  Min.   L2 Min    L1  Max    L2 Max.  
Tx Bit Rate [bps]  :           0          0         1300       1252 
Drop Bit Rate [bps]:           0          0         13000      121203  
Unidirectional Hub 
This section provides an example of configuring a unidirectional hub with five flows: 
• 
Ingress port = ETH 0/1 
• 
Egress ports: 
 
ETH 0/3, queue 0, block 0/1 
 
ETH 0/3, queue 0, block 0/2 
ETX-2i Devices 
5. Traffic Processing 
 
ETH 0/5, queue 1, block 0/1 
 
ETH 0/5, queue 1, block 0/2 
 
ETH 0/6, queue 0, block 0/1 
• 
Criteria = VLAN 100 
• 
Policer profile bandwidth limits = CIR 10000, CBS 5000, EIR 0, EBS 0 
 To configure the hub: 
#**************** Configure policer profile and aggregate for UDH 
exit all 
configure qos 
policer-profile udh_pol bandwidth cir 10000 cbs 5000 eir 0 ebs 0 
policer-aggregate udh_agg policer profile udh_pol 
exit all 
 
#*************** Configure classifier profile for UDH 
configure flows 
classifier-profile udh_class match-any match vlan 100 
exit 
 
#*************** Configure flow udh1 
flow udh1 
ingress-port ethernet 0/1 
egress-port ethernet 0/3 queue 0 block 0/1 
classifier udh_class 
policer aggregate udh_agg 
no shutdown 
exit  
 
#*************** Configure flow udh2 
flow udh2 
classifier udh_class 
ingress-port ethernet 0/1 
egress-port ethernet 0/3 queue 0 block 0/2 
policer aggregate udh_agg 
no shutdown 
exit  
 
#*************** Configure flow udh3 
flow udh3 
classifier udh_class 
ingress-port ethernet 0/1 
egress-port ethernet 0/5 queue 1 block 0/1 
policer aggregate udh_agg 
no shutdown 
exit  
 
 
ETX-2i Devices 
5. Traffic Processing 
#*************** Configure flow udh4 
flow udh4 
classifier udh_class 
ingress-port ethernet ethernet 0/1 
egress-port e ethernet 0/5 queue 1 block 0/2 
policer aggregate udh_agg 
no shutdown 
exit 
 
#*************** Configure flow udh5 
flow udh5 
classifier udh_class 
ingress-port ethernet 0/1 
egress-port ethernet 0/6 queue 0 block 0/1 
policer aggregate udh_agg 
no shutdown 
exit all 
Multi-CoS Flow 
This section provides an example of configuring multi-CoS flows per MEF 10.3: 
• 
Flow with multi-CoS counters: 
 
Ingress port = ETH 0/1 
 
Egress port: ETH 1/1 
 
Criteria = VLAN 10 
• 
Flow with Envelope Policer: 
 
Ingress port = ETH 1/1 
 
Egress port: ETH 0/1 
 
Criteria = VLAN 10 
• 
Envelope profile bandwidth limits: 
 
CIR 1000; maximum CIR 10,000; CBS 2000; EIR 0; EBS 0; maximum EIR 0 
 
CIR 2000; maximum CIR 10,000; CBS 2000; EIR 0; EBS 0; maximum EIR 0 
 
CIR 4000; maximum CIR 10,000; CBS 5000; EIR 0; EBS 0; maximum EIR 0 
 
CIR 8000; maximum CIR 10,000; CBS 5000; EIR 0; EBS 0; maximum EIR 0 
 To configure the multi-CoS flows: 
#**************** Configure CoS mapping profile 
exit all 
configure  
  qos 
    cos-map-profile cos-pbit classification p-bit 
ETX-2i Devices 
5. Traffic Processing 
      untagged-map to-cos 0 
    exit  
 
#**************** Configure envelope profile  
    envelope-profile env1 
      cf-policy uncoupled-BW-sharing 
      cos 0 bandwidth cir 1000 cir-max 10000  cbs 2000 eir 0 eir-max 0 ebs 0 
      cos 1 bandwidth cir 2000 cir-max 10000  cbs 2000 eir 0 ebs 0 
      cos 2 bandwidth cir 4000 cir-max 10000  cbs 5000 eir 0 ebs 0 
      cos 3 bandwidth cir 8000 cir-max 10000  cbs 5000 eir 0 ebs 0 
    exit 
  exit 
 
#*************** Configure classifier profile 
  flows 
    classifier-profile v10 match-any match vlan 10 
    exit 
 
#*************** Configure multi-cos-counters flow  
    flow multi2 
      classifier v10 
      cos-mapping profile cos-pbit 
      no policer 
      multi-cos-counters 0..3 
      ingress-port ethernet 0/1 
      egress-port ethernet 1/1 queue-map-profile q-map-for-cos block 0/1 
      no shutdown   
    exit 
 
#*************** Configure flow with envelope policer 
    flow env2 
      classifier v10 
      policer envelope env1 
      cos-mapping profile cos-pbit 
      ingress-port ethernet 1/1 
      egress-port ethernet 0/1 queue-map-profile q-map-for-cos block 0/1 
      no shutdown 
exit all 
save 
Port Classification 
The following illustrates configuring port classification for Ethernet port 0/1. 
exit all 
#************Outer VLAN************ 
configure port ethernet 0/1 classifier 
  match vlan 100 sequence 1 to-flow 1 
exit all 
 
configure flows flow 1 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
 
ETX-2i Devices 
5. Traffic Processing 
#************Outer p-bit************ 
configure port ethernet 0/1 classifier 
  match p-bit 2 sequence 2 to-flow 2 
exit all 
 
configure flows flow 2 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
 
#************Dest MAC************ 
configure port ethernet 0/1 classifier 
  match dst-mac 00-11-22-33-44-55 sequence 3 to-flow 3 
exit all 
 
configure flows flow 3 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
 
#************Dest IP address IPv4************ 
configure port ethernet 0/1 classifier 
  match dst-ip 172.17.160.173/32 sequence 4 to-flow 4 
exit all 
 
configure flows flow 4 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
 
#************Dst IP address IPv6************ 
configure port ethernet 0/1 classifier 
  match dst-ip 1234:1235:1236:1237:1238::1239/128 sequence 5 to-flow 5 
exit all 
 
configure flows flow 5 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
 
#************Dest TCP port************ 
configure port ethernet 0/1 classifier 
  match tcp-dst-port 0070 sequence 6 to-flow 6 
exit all 
 
configure flows flow 6 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
 
 
 
ETX-2i Devices 
5. Traffic Processing 
#************Dest UDP port************ 
configure port ethernet 0/1 classifier 
  match udp-dst-port 0070 sequence 7 to-flow 7 
exit all 
 
configure flows flow 7 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
 
#************ToS************ 
configure port ethernet 0/1 classifier 
  match tos 8 sequence 8 to-flow 8 
exit all 
 
configure flows flow 8 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
 
#************Protocol************ 
configure port ethernet 0/1 classifier 
  match protocol 5 sequence 9 to-flow 9 
exit all 
 
configure flows flow 9 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
 
#************ IP DSCP************ 
configure port ethernet 0/1 classifier 
  match ip-dscp 4..6 sequence 10 to-flow 10 
exit all 
 
configure flows flow 10 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
 
#************IP Precedence************ 
configure port ethernet 0/1 classifier 
  match ip-dscp 4..6 sequence 11 to-flow 11 
exit all 
 
configure flows flow 11 port-classifier 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
exit all 
ETX-2i Devices 
5. Traffic Processing 
Multi-CoS Flow Statistics 
This example displays statistics of multi-cos flow multi2 (see configuration in Multi-CoS Flow example). 
 To display multi-CoS flow statistics: 
ETX-2i# configure flows flow multi2 
ETX-2i>config>flows>flow(multi2)# show statistics running 
Rate Sampling Window 
----------------------------------------------------------------------------- 
Window Size [Min.]        : 15 
Window Remain Time [Min.] : 12 
 
Cos Number : 2 
 
Rx Statistics 
----------------------------------------------------------------------------- 
          Total 
Packets : 0 
Bytes   : 0 
 
Drop Statistics 
----------------------------------------------------------------------------- 
                   Packets              Bytes 
Total            : 0                    0 
Green            : 0                    0 
Yellow           : 0                    0 
Red              : 0                    0 
Yellow/Red       : 0                    0 
Drop  Rate 
-----------------------------------------------------------------------------  
                               pps           L1 (bps)        L2(bps) 
Total(Rate)      :             0             0               0 
Green(Rate)      :             0             0               0 
Yellow(Rate)     :             0             0               0 
Red(Rate)        :             0             0               0 
Yellow/Red(Rate) :             0             0               0 
Tx Statistics  
-----------------------------------------------------------------------------  
                               Packets       Bytes  
Total            :             0             0  
Green            :             0             0  
Yellow           :             0             0  
Tx  Rate 
-----------------------------------------------------------------------------  
 
 
ETX-2i Devices 
5. Traffic Processing 
                               pps           L1 (bps)        L2(bps) 
Total(Rate)      :             0             0               0 
Green(Rate)      :             0             0               0 
Yellow(Rate)     :             0             0               0 
Peak Measurement  
-----------------------------------------------------------------------------  
                               L1  Min.   L2 Min    L1  Max    L2 Max.  
Tx Bit Rate [bps]  :           0          0         0          0 
Drop Bit Rate [bps]:           0          0         0          0 
 
Cos Number : 3 
 
Rx Statistics 
----------------------------------------------------------------------------- 
          Total 
Packets : 0 
Bytes   : 0 
 
Drop Statistics 
----------------------------------------------------------------------------- 
                   Packets              Bytes 
Total            : 197941               197941000 
Green            : 197941               197941000 
Yellow           : 0                    0 
Red              : 0                    0 
Yellow/Red       : 0                    0 
Drop  Rate 
-----------------------------------------------------------------------------  
                               pps           L1 (bps)        L2(bps) 
Total(Rate)      :             243           1947758         1800000 
Green(Rate)      :             243           1947758         1800000 
Yellow(Rate)     :             0             0               0 
Red(Rate)        :             0             0               0 
Yellow/Red(Rate) :             0             0               0 
Tx Statistics  
-----------------------------------------------------------------------------  
                               Packets       Bytes  
Total            :             197941        197941000  
Green            :             197941        197941000  
Yellow           :             0             0  
Tx  Rate 
-----------------------------------------------------------------------------  
                               pps           L1 (bps)        L2(bps) 
Total(Rate)      :             243           1947758         1800000 
Green(Rate)      :             243           1947758         1800000 
Yellow(Rate)     :             0             0               0 
Peak Measurement  
-----------------------------------------------------------------------------  
                               L1  Min.   L2 Min    L1  Max    L2 Max.  
Tx Bit Rate [bps]  :           0          0         1300       1252 
Drop Bit Rate [bps]:           0          0         13000      121203  
Cos Number : 5 
ETX-2i Devices 
5. Traffic Processing 
Rx Statistics 
----------------------------------------------------------------------------- 
          Total 
Packets : 0 
Bytes   : 0 
 
Drop Statistics 
----------------------------------------------------------------------------- 
                   Packets              Bytes 
Total            : 0                    0 
Green            : 0                    0 
Yellow           : 0                    0 
Red              : 0                    0 
Yellow/Red       : 0                    0 
Drop  Rate 
-----------------------------------------------------------------------------  
                               pps           L1 (bps)        L2(bps) 
Total(Rate)      :             0             0               0 
Green(Rate)      :             0             0               0 
Yellow(Rate)     :             0             0               0 
Red(Rate)        :             0             0               0 
Yellow/Red(Rate) :             0             0               0 
Tx Statistics  
-----------------------------------------------------------------------------  
                               Packets       Bytes  
Total            :             0             0  
Green            :             0             0  
Yellow           :             0             0  
Tx  Rate 
-----------------------------------------------------------------------------  
                               pps           L1 (bps)        L2(bps) 
Total(Rate)      :             0             0               0 
Green(Rate)      :             0             0               0 
Yellow(Rate)     :             0             0               0 
Peak Measurement  
-----------------------------------------------------------------------------  
                               L1  Min.   L2 Min    L1  Max    L2 Max.  
Tx Bit Rate [bps]  :           0          0         0          0 
Drop Bit Rate [bps]:           0          0         0          0 
Flow Status 
 To display flow status: 
ETX-2i# configure flows flow a1 
ETX-2i>config>flows>flow(a1)# show status 
Operational Status                   : Down 
Reverse Operational Status           : Up 
Service Name                         : 
 
 
ETX-2i Devices 
5. Traffic Processing 
Fault propagation actions: 
Policer changed : ‘policer profile’ 
Shaper changed                       
 
Status Details 
----------------------------------------------------------------------------- 
                                     : Ingress Port Oper Status: Down 
Flow Data Rate and Line Rate 
 To display data rate line and rate for flow: 
ETX-2i# configure flows flow f10_out 
ETX-2i>config>flows>flow(f10_out)# rate-measure interval 30 
 
ETX-2i>config>flows>flow(f10_out)# show rate 
Name                       : f10_out                           
Status                     : In Progress                       
Time Left to Elapse (Sec) : 18 
 
ETX-2i>config>flows>flow(f10_out)# 
Name           : f10_out 
Status         : Passed 
Start Time     : 2014-11-13 12:24:36 UTC +00:00 
Duration (Sec) : 30 
Cos               : 255 
 
                    L1            L2 
Rx Rate (bps)     : 1000          950 
Tx Rate (bps)     : 1500          1400 
Green Drop (bps)  : 100           95 
Yellow Drop (bps) : 100           95 
Red Drop (bps)    : 100           90 
Flow Service Ping Status 
 To display the status of the service ping: 
ETX-2x>config>flows# show service-ping-status 
State             : Request 
Local IP          : 172.17.92.64/24 
Destination IP    : 172.17.92.46 
Next Hop          : 172.17.92.1 
Egress Port       : Ethernet 0/1 
VLAN ID           : 51 
Pbit              : ---- 
Inner VLAN ID     : ---- 
Inner Pbit        : ---- 
Probe Scope       : Down 
ETX-2i Devices 
5. Traffic Processing 
Number Of Packets : 5 
Paylod Size       : 32 
Tx Flows          : mng_v51_in_1 
Rx Flows          : flow unsupported 
Application Layer Loopback 
Note 
This example uses the classifier profile ‘da mac aa’, created in the classifier 
profile examples.  
 To configure the mac-swap loopback: 
exit all 
configure flows flow Tflow 
ingress-port ethernet 1 
egress-port ethernet 1 queue 0 block 0/1 
classifier da_mac_aa 
test mac-swap duration 50 
no shutdown 
exit all 
ETH1
 
Application Layer Loopback Test on Flow with Three Attributes 
 To display flow test status: 
ETX-2i>config>flows>flow(Tflow)# show test 
Test : MAC Swap  Duration (Sec)  : 50    Remain (sec)  : 40     No TTL 
Flow Diagnostics Loopback 
In the following example, two flows of an EVC are configured. The diagnostics loop is performed over 
evc1_in the flow (back to the network). 
Note 
This example uses the classifier profile ‘all’, created in the classifier profile 
examples.  
 To configure the mac-swap loopback: 
exit all 
ETX-2i configure flows flow (evc1_in)# test mac-swap duration 50 