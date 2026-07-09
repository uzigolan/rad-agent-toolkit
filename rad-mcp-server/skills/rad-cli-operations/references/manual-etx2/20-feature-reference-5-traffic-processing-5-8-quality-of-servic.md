# Feature Reference – 5 Traffic Processing – 5.8 Quality of Service (QoS)

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 992–1041.*


## Applicability and Scaling  *(p.992)*

ETX-2i Devices 
5. Traffic Processing 
POWER/MDI configuration 
Port-class 
 
 
: 
-- 
MDI Support Status 
 
 
: 
-- 
MDI Current  Status  
 
: 
Disabled 
PSE Pair Control Ability 
 
: 
-- 
Power Class 
 
 
: 
-- 
Max Frame Size 
 
 
: 
1500 
5.8 Quality of Service (QoS) 
The ETX-2i Quality of Service (QoS) parameters include the following profiles: 
• 
Queue mapping profiles 
• 
CoS mapping profiles 
• 
Color mapping profiles 
• 
Marking profiles 
• 
Bandwidth profiles 
• 
Queue block profiles 
• 
Queue group profiles 
These profiles can be applied to traffic flows and ports (Queue groups) to ensure the desired flow 
prioritization. 
QoS allows you to optimize bandwidth, avoiding the need to allocate excessive bandwidth to facilitate 
the necessary bandwidth for traffic at different requirements of speed and quality. 
Applicability and Scaling 
The QoS features in this section are applicable to all ETX-2i products. 
 
 
 

## Standards Compliance  *(p.993)*


## Functional Description  *(p.993)*

ETX-2i Devices 
5. Traffic Processing 
Standards Compliance 
The following standards are supported: 
• 
IEEE 802.1p 
• 
IEEE 802.1Q 
• 
MEF 10.3 
Functional Description 
Traffic Management 
ETX-2i traffic management entities are called queue groups. They are configured over physical ports. The 
queue groups consist of 2-level scheduling elements (queue blocks) per port; EVC at queue block level 0 
and port level at queue block level 1. The queue blocks consist of internal queues.  
Additionally, Shapers operate at per-scheduling-element level to shape traffic into a required traffic 
profile (CIR, CBS or CIR/EIR, CBS/EBS). 
Each flow is assigned to a queue block as its destination. Each queue block includes scheduling queues in 
accordance with CoS delivery priorities. Flow packets are mapped in the following ways to queues: 
• 
Mapped explicitly to a specific queue  
• 
Mapped to a queue according to a queue mapping profile (p-bit or DSCP to queue) 
• 
Mapped according to the packet’s CoS, in case of bridge or ETP (set by CoS mapping profile at 
the ingress), whereby CoS 7 is mapped to the lower priority queue, and CoS 0 to the highest 
Scheduling 
ETX-2i supports a combination of traffic scheduling techniques, whereby applications requiring low 
latency and jitter are mapped to strict priority (SP) queues, while other services are mapped to the 
remaining slots using weighted fair queuing (WFQ) and best effort (BE):  
• 
Strict Priority (SP) queues ensure minimal latency and jitter for the RT traffic, even when a large 
amount of bursty data traffic is sent over the same uplink. Strict priority traffic is always 
processed first, while flows mapped to the WFQ slots are buffered until the strict priority 
queues are empty. 
 
 

## Factory Defaults  *(p.994)*


## Queue Mapping Profiles  *(p.994)*

ETX-2i Devices 
5. Traffic Processing 
• 
The WFQ technique avoids scheduling starvation of lower priority queues and ensures relatively 
fair allocation of bandwidth by sharing it among all flows. In this manner, packets belonging to 
lower classes of service are not penalized when higher priority queues are not empty and may 
still receive transmission time. QoS-conformant scheduling is handled by assigning different 
weights to the various queues instead of equally dividing overall bandwidth among all active 
flows. 
• 
BE (best-effort) queues transmit packets only if there are no packets in higher level queues. 
Congestion avoidance is provided by WRED profiles (see WRED Profiles). 
Factory Defaults 
See the following sections for each QoS type’s specific defaults. 
Queue Mapping Profiles 
To differentiate traffic, the IEEE 802.1p standard specifies eight classes of service per user-defined 
queue mapping profile. These classes of service are associated with priority values between 0 and 7, 
using the 3-bit user priority field in an IEEE 802.1Q header added to VLAN-tagged frames within an 
Ethernet frame header. The way traffic is treated when assigned to a specific priority value is only 
generally defined and left to implementation. The general definitions are as follows: 
 
User Priority 
Traffic Type 
0 
Best effort 
1 
Background 
2 
Spare 
3 
Excellent effort 
4 
Controlled load 
5 
Video 
6 
Voice 
7 
Network control 
 
 
ETX-2i Devices 
5. Traffic Processing 
Queue mapping profiles are used to convert the following user priorities into internal priority queues.  
p-bit 
When ingress traffic is prioritized according to the 802.1p 
requirements 
ip-dscp 
When ingress traffic is prioritized according to DSCP; for both IPv4 
and IPv6 
ip-precedence 
When ingress traffic is prioritized according to IP precedence; for 
both IPv4 and IPv6  
Class of Service (CoS) 
When ingress traffic is mapped to an internal CoS (e.g., p-bit or 
DSCP to CoS) at the Bridge port ingress, ETP subscriber ingress, and 
flow that uses an Envelope Policer. 
For each profile, you must define the queue mapping to map the user priority values to the internal 
queue values. The internal queues are combined into a queue profile, which can be assigned to a queue 
block. 
Factory Defaults 
Default Queue Mapping Profile 
ETX-2i provides a default queue mapping profile named CosProfile1, which can be used when the 
ingress traffic is prioritized according to the 802.1p requirements. It is defined with classification p-bit, 
and the following mappings: 
• 
Map p-bit 0 to queue 7. 
• 
Map p-bit 1 to queue 6. 
• 
Map p-bit 2 to queue 5. 
• 
Map p-bit 3 to queue 4. 
• 
Map p-bit 4 to queue 3. 
• 
Map p-bit 5 to queue 2. 
• 
Map p-bit 6 to queue 1. 
• 
Map p-bit 7 to queue 0. 
There is also a predefined queue mapping profile named q-map-for-cos, which can be used for multi-Cos 
flows when you wish to map CoS 0 to queue 0, CoS 1 to queue 1, etc. 
ETX-2i Devices 
5. Traffic Processing 
Default Configuration for IP Precedence Classification 
When a new queue mapping profile is created with classification IP precedence, it contains the following 
mappings: 
• 
Map p-bit 0 to queue 7. 
• 
Map p-bit 1 to queue 6. 
• 
Map p-bit 2 to queue 5. 
• 
Map p-bit 3 to queue 4. 
• 
Map p-bit 4 to queue 3. 
• 
Map p-bit 5 to queue 2. 
• 
Map p-bit 6 to queue 1. 
• 
Map p-bit 7 to queue 0. 
Default Configuration for DSCP Classification 
When a new queue mapping profile is created with classification DSCP, it contains the following 
mappings: 
• 
Map p-bit 0 to queue 7. 
• 
Map p-bit 1 to queue 6. 
• 
Map p-bit 2 to queue 5. 
• 
Map p-bit 3 to queue 4. 
• 
Map p-bit 4 to queue 3. 
• 
Map p-bit 5 to queue 2. 
• 
Map p-bit 6 to queue 1. 
• 
Map p-bit 7 through 63 to queue 0. 
Adding Queue Mapping Profiles 
When you create a queue mapping profile, you specify the name and the classification method (p-bit, IP 
precedence, or DSCP). 
ETX-2i Devices 
5. Traffic Processing 
 To add a queue mapping profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Enter: 
queue-map-profile <queue-map-profile-name> classification {p-bit|ip-precedence|ip-dscp|cos} 
A queue mapping profile with the specified name and classification method is created and the 
following prompt is displayed: 
config>qos>queue-map-profile(<queue-map-profile-name>)$.  
The mappings for the new profile are configured by default as described in Factory Defaults. 
3. Configure the queue profile mappings as described in Configuring Queue Mappings. 
Configuring Queue Mappings 
 To configure queue mappings: 
1. Navigate to config qos queue-map-profile <queue-map-profile-name> to select the queue 
mapping profile to configure. 
The following prompt is displayed: 
config>qos>queue-map-profile(<queue-map-profile-name>)# 
2. Map the user priorities to queue IDs as necessary: 
 
Classification p-bit or IP precedence: 
map <0-7> to-queue <0-7> 
 
Classification DSCP: 
map <0-63> to-queue <0-7> 
 
Classification CoS: 
map <0-7> to-queue <0-7> 
Examples 
 To create and configure a queue mapping profile named QMapPbit with classification p-bit: 
• 
Map priority 0 to queue 3. 
• 
Map priority 4 and 6 to queue 2. 
exit all 
configure qos queue-map-profile QMapPbit classification p-bit 
  map 0 to 3 
  map 4 to 2 
ETX-2i Devices 
5. Traffic Processing 
  map 6 to 2 
  exit all 
 To display the configuration information for queue mapping profile QMapPbit: 
ETX-2i# configure qos queue-map-profile QMapPbit 
ETX-2i>config>qos>queue-map-profile(QMapPbit)# info detail 
    map  0 to-queue  3  
    map  1 to-queue  6  
    map  2 to-queue  5  
    map  3 to-queue  4  
    map  4..6 to-queue  2  
    map  7 to-queue  0 
 To create and configure a queue mapping profile named QMapIPprec with classification IP 
precedence: 
• 
Map priority 2 and 3 to queue 3. 
exit all 
configure qos queue-map-profile QMapIPprec classif ip-precedence 
  map 2 to 3 
  map 3 to 3 
  exit all 
 To display the configuration information for queue mapping profile QMapIPprec: 
ETX-2i# configure qos queue-map-profile QMapIPprec 
ETX-2i>config>qos>queue-map-profile(QMapIPprec)# info detail 
    map  0 to-queue  7  
    map  1 to-queue  6  
    map  2..4 to-queue  3  
    map  5 to-queue  2  
    map  6 to-queue  1  
    map  7 to-queue  0 
 To create and configure a queue mapping profile named QMapDSCP with classification DSCP: 
• 
Map priority 7 to queue 6. 
• 
Map priority 55 to queue 4. 
• 
Map priority 63 to queue 5. 
exit all  
configure qos queue-map-profile QMapDSCP classif ip-dscp 
  map 7 to 6 
  map 55 to 4 
  map 63 to 5 
  exit all 

## CoS Mapping Profiles  *(p.999)*

ETX-2i Devices 
5. Traffic Processing 
 To display the configuration information for queue mapping profile QMapDSCP: 
ETX-2i# configure qos queue-map-profile QMapDSCP 
ETX-2i>config>qos>queue-map-profile(QMapDSCP)# info detail 
    map  0 to-queue  7  
    map  1 to-queue  6  
    map  2 to-queue  5  
    map  3 to-queue  4  
    map  4 to-queue  3  
    map  5 to-queue  2  
    map  6 to-queue  1  
    map  7 to-queue  6  
    map  8..54 to-queue  0  
    map  55 to-queue   
4  
    map  56..62 to-queue  0  
    map  63 to-queue  5 
 To create and configure a queue mapping profile named QMapCoS with classification CoS: 
• 
Map CoS 6–7 to-queue 0. 
• 
Map CoS 3–5 to-queue 1. 
• 
Map CoS 0–2 to-queue 2. 
exit all  
configure qos queue-map-profile QMapCoS classification cos 
  map 6..7 to-queue 0 
  map 3..5 to-queue 1 
  map 0..2 to-queue 2 
  exit all 
CoS Mapping Profiles 
CoS mapping profiles can be used at the following levels: 
• 
Flow level — ingress Bridge port flows, ETP subscriber flows, and flows using Envelope Policer 
(MEF 10.3 BW profiles) 
• 
Ring level 
 
 
ETX-2i Devices 
5. Traffic Processing 
Class of Service (CoS) mapping profiles map the following user priorities to internal CoS values:  
p-bit 
Relevant at flow and ring levels; when ingress traffic is prioritized according to 802.1p 
requirements 
ip-dscp 
Only relevant at the flow level; when ingress traffic is prioritized according to DSCP 
ip-precedence 
Only relevant at the flow level; when ingress traffic is prioritized according to 
IP precedence 
 
Note 
If the flow from UNI to NNI is classified with one of the above classifications 
(p-bit only, ip-dscp, or ip-precedence), Up MEP and customer-tag-excluded 
MEP do not work, and it is therefore recommended not to use them.  
Internal CoS is used: 
• 
To map a packet to a specific egress queue (fixed mapping: CoS 0 maps to queue 0, CoS 1 maps 
to queue 1, etc.) 
• 
By marking profiles to set p-bits of remarked packets (‘CoS to p-bit’ marking profiles) 
• 
By flows with MEF 10.3 Envelope BW profiles to map traffic to the different Envelope ranks 
identified by CoS 
Factory Defaults 
By default, there are no CoS mapping profiles. When you create a CoS mapping profile, it is configured 
as follows: 
• 
Classification p-bit 
• 
Mappings: 
 
Map 0 to CoS 7. 
 
Map 1 to CoS 6. 
 
Map 2 to CoS 5. 
 
Map 3 to CoS 4. 
 
Map 4 to CoS 3. 
 
Map 5 to CoS 2. 
 
Map 6 to CoS 1. 
 
Map 7 to CoS 0. 
 
Untagged to CoS 7, for profile assigned to multi-Cos flow in case of p-bit mapping  
 
Non-IP to CoS 7, for profile assigned to multi-Cos flow in case of DSCP mapping 
ETX-2i Devices 
5. Traffic Processing 
Configuring CoS Mapping Profiles 
 To define a CoS mapping profile: 
1. Navigate to the qos context (config>qos). 
2. Define a CoS profile and assign a classification to it: 
cos-map-profile <cos-mapping-profile-name> [classification {p-bit | ip-precedence | ip-dscp }] 
Note that you can only configure classification p-bit for a CoS mapping profile to be associated 
with a ring. 
3. Map the user priority to a CoS value (user priority values 0–7 for p-bit and IP precedence, 0–63 
for the other priority types; CoS values 0–7): 
map <0-7> to <0-7> 
map <0-63> to <0-7> 
4. If the CoS mapping profile is intended for use with a multi-Cos flow: 
a. Define the mapping of untagged traffic in case of p-bit mapping: 
map untagged to <0-7> 
b. Define the mapping of non-IP traffic in case of DSCP mapping: 
map non-ip to <0-7> 
Examples 
 To create and configure a CoS mapping profile (for a flow or ring): 
• 
Profile name: my-p-bit 
• 
Classification: p-bit 
• 
Map priority 6–7 to CoS 0. 
• 
Map priority 3–5 to CoS 1. 
• 
Map priority 0–2 to CoS 2. 
exit all  
configure qos cos-map-profile my-p-bit classification p-bit 
  map 6..7 to-cos 0 
  map 3..5 to-cos 1 
  map 0..2 to-cos 2 
   exit all 
 
 

## Color Mapping Profiles  *(p.1002)*

ETX-2i Devices 
5. Traffic Processing 
 To create and configure a CoS mapping profile for a multi-CoS flow: 
• 
Profile name: p-bit-multi 
• 
Classification: p-bit 
• 
Map priority 0 to CoS 7. 
• 
Map priority 7 to CoS 0. 
• 
Map untagged traffic to CoS 0. 
exit all  
configure qos cos-map-profile p-bit-multi classification p-bit 
untagged-map to-cos 0 
   exit all 
Color Mapping Profiles 
Color mapping profiles map p-bits or the drop eligible indicator (DEI) bit to packet color: 
• 
Color mapping profiles with classification type p-bit are used to map p-bit values to green or 
yellow.  
• 
Color mapping profiles with classification type DEI are used to map the DEI bit to green or yellow 
as follows: 
 
DEI=0: Maps to green 
 
DEI=1: Maps to yellow 
Color mapping profiles with classification type p-bit are configurable, whereas color mapping profiles 
with classification type DEI are not configurable. 
Color mapping profiles can be assigned to flows and rings. 
Factory Defaults 
By default, there is no color mapping profile. When a color mapping profile with classification type p-bit 
is created, all the p-bit values are mapped to green. 
 
 

## Marking Profiles  *(p.1003)*

ETX-2i Devices 
5. Traffic Processing 
Configuring Color Mapping Profiles 
 To define a color mapping profile: 
1. Navigate to the qos context (config>qos). 
2. Define a color mapping profile according to classification type: 
 
P-bit classification: 
i. 
Enter: 
color-map-profile <color-mapping-profile-name> classification p-bit 
ii. Map the p-bits to a color as needed: 
map <class-value> to {green|yellow} 
 
DEI classification: color-map-profile <color-mapping-profile-name> classification dei 
Example 
 To create a color mapping profile kcolpb to map odd p-bit values to green, and even p-bit values 
to yellow: 
exit all 
configure qos 
    color-map-profile kcolpb classification p-bit 
      map 0 to yellow 
      map 2 to yellow 
      map 4 to yellow 
      map 6 to yellow 
      exit all 
save 
Marking Profiles 
Marking profiles map the p-bit, IP precedence, DSCP, or CoS classifications to the egress priority tags (p-
bit) or DSCP values (ip-dscp). The marking can also be done per color (green and/or yellow), to support 
color re-marking, optionally specifying the Drop Eligible Indicator (DEI) bit in the frame header.  
In the case that you configure the ETHoGRE tunnel DSCP value using a DSCP marking profile (see 
Ethernet over GRE (ETHoGRE) Tunnel), you must first configure the DSCP marking profile with 
classification p-bit and method ip-dscp (see below).  
ETX-2i Devices 
5. Traffic Processing 
Factory Defaults 
ETX-2i provides a default non color-aware marking profile named MarkingProfile1, which can be used 
when the ingress traffic is prioritized according to the 802.1p requirements. It is defined with 
classification p-bit and method p-bit, and the following markings: 
• 
P-bit 0 => priority 0 
• 
P-bit 1 =>priority 1 
• 
P-bit 2 =>priority 2 
• 
P-bit 3 =>priority 3 
• 
P-bit 4 =>priority 4 
• 
P-bit 5 =>priority 5 
• 
P-bit 6 =>priority 6 
• 
P-bit 7 =>priority 7 
When a non color-aware marking profile is created, it has the same configuration as MarkingProfile1. 
Configuring Marking Profiles 
 To define a marking profile: 
1. Navigate to the qos context (config>qos). 
2. Define the marking profile and assign a classification and method to it: 
marking-profile <marking-profile-name>  
[classification {p-bit | ip-precedence | ip-dscp |cos}] [method {p-bit | ip-dscp} ] [color-aware 
{none | green-yellow} [dei {always-green | always-yellow | by-policer}]  
 
Note 
• 
The color of a color-aware profile must be defined as green-yellow. 
• 
The classification must be cos if the marking profile is intended for use 
with a multi-CoS flow.  
• 
While working with ETP, marking profile on Transport flows must be 
mapped by cos (“marking-profile 1 classification cos”) and not p-bit 
(“marking-profile 1 classification p-bit”). 
 
 
ETX-2i Devices 
5. Traffic Processing 
The dei parameter affects the Drop Eligible Indicator (DEI) bit in transmitted frames as follows: 
 
always-green — Frames transmitted from the device are marked via the DEI bit as not 
eligible to be dropped. In this case, the color-aware parameter can be none or 
green-yellow. 
 
always-yellow — Frames transmitted from the device are marked via the DEI bit as eligible 
to be dropped. In this case, the color-aware parameter can be none or green-yellow. 
 
by-policer — Yellow frames transmitted from ETX-2i are marked via the DEI bit as eligible to 
be dropped, and green frames transmitted from ETX-2i are marked as not eligible to be 
dropped. In this case, the color-aware parameter must be green-yellow. 
3. Map the user priority (and packet color, if it is a color-aware marking profile) to a priority 
marking value according to the specific profile parameters (classification and method), as 
follows: 
At the config>qos>marking-profile(<profile-name>)$ prompt, enter:  
 
Non color-aware profile: 
mark <user-priority> to <priority-marking> 
 
Color-aware profile: 
mark <user-priority> {all|green|yellow} to <priority-marking> 
Where user-priority value can be set to:  
 
0-7 – for marking profile configured with classification p-bit, ip-precedence, or cos 
 
0-63 – for marking profile configured with classification ip-dscp 
And priority-marking value can be set to: 
 
0-7 – for marking profile configured with method p-bit 
 
0-63 – for marking profile configured with method ip-dscp 
4. For ip-dscp classification only, marking a DSCP code is supported. The command varies 
depending on the method (ip-dscp, p-bit), as follows. 
 
ip-dscp classification with ip-dscp method: 
You can map the following: 
 
dscp-code code (and packet color if it is a color-aware marking profile) to a code  
 
dscp-code code (and packet color if it is a color-aware marking profile) to a value  
 
dscp-code value (and packet color if it is a color-aware marking profile) to a code  
 
dscp-code value (and packet color if it is a color-aware marking profile) to a value  
At the config>qos>marking-profile(<profile-name>)$ prompt: 
 
mark-dscp-code code <code> [{all|green|yellow}] to-code <code> 
 
mark-dscp-code code <code> [{all|green|yellow}] to-value <priority-marking> 
 
mark-dscp-code value <user-priority> [{all|green|yellow}] to-code <code> 
 
mark-dscp-code value <user-priority> [{all|green|yellow}] to-value <priority-marking> 

## Bandwidth Profiles  *(p.1006)*

ETX-2i Devices 
5. Traffic Processing 
Where 
code: 
{cs0|cs1|cs2|cs3|cs4|cs5|cs6|cs7|af11|af12|af13|af21|af22|af23|af31|af32|af33|af41
|af42|af43|ef-phb|voice-admit} 
user-priority: 0..63 
priority-marking: 0..63 
 
ip-dscp classification with p-bit method: 
You can map the following: 
 
dscp-code code (and packet color if it is a color-aware marking profile) to a priority 
marking 
 
dscp-code value (and packet color if it is a color-aware marking profile) to a priority 
marking 
At the config>qos>marking-profile(<profile-name>)$ prompt: 
 
mark-dscp-code code <code> [{all|green|yellow}] to <priority-marking> 
 
mark-dscp-code value <user-priority> [{all|green|yellow}] to <priority-marking> 
Where 
code: 
{cs0|cs1|cs2|cs3|cs4|cs5|cs6|cs7|af11|af12|af13|af21|af22|af23|af31|af32|af33|af41
|af42|af43|ef-phb|voice-admit} 
user-priority: 0..63 
priority-marking: 0..7 
Bandwidth Profiles 
ETX-2i supports the following bandwidth profiles: 
Envelope Policer 
profile 
Specifies set of bandwidth profiles to apply to multi-CoS flows 
Policer aggregate 
Specifies non-Envelope Policer profile to apply to a group of flows 
You can control the egress bandwidth utilization by defining the committed information rate (CIR) and 
committed burst size (CBS) in Shaper and Policer profiles. You can also define the excessive information 
rate (EIR), excessive burst size (EBS), and compensation in Policer profiles. 
CIR 
Defines the Committed Information Rate (CIR) for the current 
profile. The CIR specifies a bandwidth with committed service 
guarantee (“green bucket” rate). 
CBS 
Defines the Committed Burst Size (CBS) for the current profile. The 
CBS specifies the maximum guaranteed burst size (“green bucket” 
size). 
ETX-2i Devices 
5. Traffic Processing 
EIR 
Defines the Excess Information Rate (EIR). The EIR specifies an extra 
bandwidth with no service guarantee (“yellow bucket” rate). 
EBS 
Defines the Excess Burst Size (EBS). The EBS specifies the extra burst 
with no service guarantee (“yellow bucket” size). 
Compensation 
Defines the number of bytes that the Envelope, Shaper, or Policer 
can compensate for Layer-1 overhead (preamble and IFG) and the 
overhead for the additional VLAN header in case of stacking. 
Color Aware 
You can specify the Policer profile as color aware. 
If the Policer profile is specified as color aware, you can set the packet color as follows: 
1. If the arriving packet is marked green and the CIR bucket complies, the packet color is set to 
green. 
2. If the result of the preceding test is not true, ETX-2i checks if the EIR bucket complies (if the 
coupling flag is set, the CIR+EIR bucket is used): 
 
If the test result is true, the packet color is set to yellow. 
 
If the test result is false, the packet color is set to red (packet is dropped). 
Factory Defaults 
The default for bandwidth-round-up is no bandwidth-round-up. The default value for envelope-ranks 
(maximum number of ranks in Envelope profiles) is 4. 
ETX-2i provides default bandwidth profiles, as specified in the following table.  
Profile Type 
Shaper 
 
 
Policer 
(non-Envelope) 
Profile Name 
Shaper1 
 
 
Policer1 
cir 
9999872 
 
 
 
0 
cbs 
16000000 
 
 
 
0 
eir 
[not applicable] 
 
 
10000000 
 
ebs 
[not applicable] 
 
 
32767 
color-aware 
[not applicable] 
 
 
no color-aware 
compensation 
0 
 
 
0 
coupling-flag 
[not applicable] 
 
 
no coupling-flag 
traffic-type 
[not applicable] 
 
 
all 
ETX-2i Devices 
5. Traffic Processing 
When an Envelope profile is created, it has the default values shown in the following table. 
Parameter 
Value 
compensation 
0 
cf-policy 
sharing-excess-bw 
color-aware 
no color-aware 
cos <n> bandwidth 
cir 0 cir-max 10000000 cbs 0 eir 0 eir-max 10000000 ebs 0 
Envelope Bandwidth Profiles 
An Envelope profile as defined in MEF 10.3 contains a set of bandwidth profiles, each of which has been 
assigned a unique rank from 1 (lowest) to 4 or 8 (highest). Excess bandwidth from a higher rank can 
overflow to a lower rank to be shared, either to the committed or to the excess bucket. In ETX-2i, each 
profile corresponds to a separate CoS. The figure below illustrates an Envelope profile with three CoSs. 
The coupling flags specify the path of overflow bandwidth. For the CoS coupling flags (CFi), 0 = 
committed token bucket of the next lower rank, and 1 = excess token bucket of the same rank. For 
coupling flag 0, 0 = discard, and 1 = excess token bucket of the highest rank.  
CIR3
CBS3
EIR3
1
0
CIR2
CF3
EIR2
1
0
CBS2
CIR2
EIR1
1
0
CBS1
CF2
CF1
1
0 CF0
EBS3
EBS2
EBS1
Rank #3
Rank #2
Rank #1
Envelope
 
When the Envelope profile is assigned to a multi-CoS flow (see Multi-CoS Flows), it enables the flow to 
share excess bandwidth. The bandwidth sharing can be overflowed to the excess bucket or independent 
from the excess bucket (see the following two figures).  
ETX-2i Devices 
5. Traffic Processing 
CIR3
CBS3
EIR3
1
CIR2
CF3
EIR2
1
CBS2
CIR2
EIR1
1
CBS1
CF2
CF1
EBS3
EBS2
EBS1
 
Sharing Excess Bandwidth 
CIRenv
CBS3
CF3
CBS2
CBS1
CF2
CF1
EBS3
EBS2
EBS1
EIRenv
0
0
0
 
Sharing Excess Bandwidth, Uncoupled from EIR/EBS 
ETX-2i can work with up to four or eight ranks (user configurable).  
ETX-2i Devices 
5. Traffic Processing 
 To change the maximum number of ranks: 
Note 
The following must be true in order to change the maximum number of ranks 
from 4 to 8: 
• 
No more than 125 active Envelope Policer instances exist in the device. 
• 
No more than 32 Envelope profiles are configured. 
The following must be true in order to change the maximum number of ranks 
from 8 to 4: 
• 
No Envelope Policer profile is configured with more than 4 ranks.  
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Enter: envelope-ranks {4|8} 
A message is displayed recommending that you reset the device in order to save the 
configuration and for changes to go into effect.  
Configuring Granularity Rounding 
In Policer, Envelope, and Shaper profiles, configured bandwidth CIR/EIR values are rounded either up or 
down for granularity, according to whether you enable or disable the bandwidth-round-up command. 
Bandwidth roundup is disabled by default for all devices. 
 To configure granularity rounding: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. To enable rounding up to the higher granular value, type: 
bandwidth-round-up 
The configured Policer, Envelope, and Shaper profile CIR/EIR bandwidth limits are rounded up to 
their higher granular values. 
3. To enable rounding down to the lower granular value, type: 
no bandwidth-round-up 
The configured Policer, Envelope, and Shaper profile CIR/EIR bandwidth limits are rounded 
down to their lower granular values. 
ETX-2i Devices 
5. Traffic Processing 
Note 
• 
A change to bandwidth granularity rounding (down to up or vice versa) 
only goes into effect after device reboot. 
• 
If no bandwidth-round-up is configured, CIR/EIR values are rounded down 
to the next lower granularity level, with the exception that granular values 
are not rounded down. The rounded down granular values are set in the 
hardware modules. They are also stored in the device database, and 
therefore the profile information (output of the info command) displays 
the rounded down granular values. 
• 
If bandwidth-round-up is configured, CIR/EIR values are rounded up to 
their next granularity levels, even if they are granular values. The rounded 
up granular values are set in the hardware modules. However, they are 
not stored in the device database, as if they were, at each reboot, the 
CIR/EIR values that are already at a granular level, would be further 
rounded up to the next granular level. Therefore, the profile information 
(output of the info command) displays the configured CIR/EIR values, and 
not their rounded up granular values. 
• 
You can run the show status command under the Shaper, Policer, or 
Envelope profile to see the rounding method, and the provisioned (i.e. 
rounded or configured) and actual (i.e. rounded up/down granular) values 
of each bandwidth limit.  
Configuring Shaper Profiles 
You can configure Shaper profiles and apply them to queue group blocks as needed. 
All ETX-2i devices support a single rate Shaper at level 0 and level 1 queue blocks. 
Note 
When the same Shaper profile is used for 1Gbps and 10Gbps ports (set to or 
support), the Actual Shaper BW displays values of the lower (indexed) port. 
(Relevant for ETX-2i-10G half and full models.) 
As the Bandwidth Shaper profile values apply differently over these ports, the 
actual BW display is not accurate for all ports.  
Adding Shaper Profiles 
 To add a Shaper profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Enter shaper-profile <shaper-profile-name>. 
ETX-2i Devices 
5. Traffic Processing 
A Shaper profile with the specified name is created and the config>qos>shaper-profile(<shaper-
profile-name>)$ prompt is displayed. The new Shaper profile parameters (except for name) are 
configured by default as described in Factory Defaults. 
3. Configure the Shaper profile as described in Configuring Shaper Profile Parameters. 
Configuring Shaper Profile Parameters 
 To configure Shaper profiles: 
1. Navigate to configure qos shaper-profile <shaper-profile-name> to select the Shaper profile to 
configure. 
The config>qos>shaper-profile(<shaper-profile-name>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying the CIR (Kbps) and 
CBS (bytes) bandwidth limits  
 
bandwidth [cir <cir-kbit-sec>] [cbs <cbs-bytes>] 
CIR allowed values: 
• ETX-2i, ETX-2i-B, ETX-
2i-10G (full and half 19-
inch): 0–20 Gbps 
• ETX-2i-100G/4Q:  
0-100 Gbps 
See the table below for the 
Shaper CIR granularity. 
CBS allowed values: 
• 0, or 64–16,777,215 
 
Compensating for Layer-1 
(preamble and IFG) and 
additional VLAN tags (in bytes) 
overhead 
compensation <0–63> 
For pre-forwarding 
(ingress) traffic 
management, the 
compensation is 
configurable in the 0-63 
range. 
For post-forwarding 
(egress), traffic 
management, the 
compensation is applied to 
level-0 Shapers only. It can 
be set to 0 (data rate) or 
20 (line rate). 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Generating Shaper profile 
bandwidth status 
show status 
Generates a report 
showing QoS bandwidth 
rounding method, and CIR 
and CBS values 
(provisioned and actual). 
See Viewing Shaper 
Profile Bandwidth Status 
for details. 
Shaper CIR Granularity 
Device 
CIR > 130 Mbps (fast) 
CIR <= 130 Mbps (slow) 
ETX-2i, ETX-2i-B, ETX-2i-10G 1G 
ports, ETX-2i-100G/4Q 10G 
ports   
256 Kbps 
64 Kbps 
ETX-2i-10G 10G ports,  
ETX-2i-100G/4Q 100G ports 
512 Kbps 
512 Kbps 
 
Note: Although the CLI enables you to configure the Shaper profile with 
either 64 Kbps or 256 Kbps granularity, when applied to ETX-2i-10G 10G 
ports or ETX-2i-100G ports, this value is rounded up or down to 512 Kbps 
(depending on whether or not you set the bandwidth-round-up 
configuration parameter). 
This behavior is due to HW limitations and due to the fact that the Shaper 
profile is not bound to any port when configured, but in actuality, can be 
bound to both 1G 10G, and 100G ports. 
Examples 
 To create and configure a Shaper profile named Shap2: 
• 
CIR = 99,840 Kbps 
• 
CBS = 32,000 bytes 
• 
Compensation = 48 
exit all  
configure qos shaper-profile Shap2 
  bandwidth cir 99840 cbs 32000 
  compensation 48 
  exit all 
ETX-2i Devices 
5. Traffic Processing 
Note 
• 
If bandwidth-round-up is disabled, the info command displays the 
rounded down CIR granular value. However, if bandwidth-round-up is 
enabled, the CIR value that you configured is displayed. 
• 
The output of the show status command displays the CIR configured and 
granular values, regardless of the rounding method used (see Viewing 
Shaper Profile Bandwidth Status).  
Viewing Shaper Profile Bandwidth Status  
When you configure the Shaper Profile CIR and CBS bandwidth limits, the device automatically rounds 
down or up the configured CIR value for granularity, depending on the setting of bandwidth-round-up 
(see Configuring Granularity Rounding), as follows: 
• 
no bandwidth-round-up – Configured CIR value is rounded down, which is the default. 
• 
bandwidth-round-up – Configured CIR value is rounded up. 
ETX-2i provides the show status command to view the Shaper profile bandwidth status. 
 To display the Shaper Profile bandwidth status: 
• 
When config > qos > no bandwidth-round-up 
ETX-2i# config>qos>shaper-profile(sh_1)$ show status 
Bandwidth 
-------------------------------------------------------------- 
 
Current Rounding : Down 
 
Parameter     Provisioned Value    Actual Value 
--------------------------------------------------------------- 
CIR [Kbps]       : 12288                12280 
CBS [Bytes       : 32000                32000  
The fields are described in the following table: 
Parameter 
Description 
Current Rounding 
Displays rounding method configured under config > qos level (see 
Configuring Granularity Rounding).  
Possible values: 
• Down – CIR provisioned value is rounded down for granularity (default). 
• Up – CIR provisioned value is rounded up for granularity. 
CIR Provisioned Value 
Configured CIR value 
CIR Actual Value 
Rounded up/down CIR granular value 
ETX-2i Devices 
5. Traffic Processing 
Parameter 
Description 
CBS Provisioned Value 
Configured CBS value 
CBS Actual Value 
Same as CBS Provisioned Value (no CBS rounding) 
Configuring Policer Profiles 
This section explains functionality and configuration of non-Envelope Policer profiles for traffic policing 
and rate limit. Policer profiles can be applied to flows or Ethernet ports.  
A port Policer profile (, also known as BUM filter (Broadcast, Unknown Unicast, Multicast filter),) is 
supported by binding a Policer BW profile to the Ethernet port. This BW profile can only be configured 
with CIR and CBS bandwidth parameters. 
Whereas a Policer BW profile bound to a flow relates to the entire traffic over this flow, a Policer BW 
profile bound to an Ethernet port can be configured to limit Broadcast, Multicast, Unknown Unicast, and 
their combinations (see below).  
You can configure the Policer BW profile bound to Ethernet port to rate limit the following traffic types: 
Broadcast 
Broadcast traffic from the port is limited per the configured CIR and CBS bandwidth 
limits. 
Multicast 
Multicast traffic from the port is limited per the configured CIR and CBS bandwidth 
limits. 
Unknown Unicast 
Unknown Unicast traffic from the port is limited per the configured CIR and CBS 
bandwidth limits. This is relevant only for traffic into a bridge. 
Broadcast + 
Multicast 
Traffic aggregation of Broadcast + Multicast from the port is limited per the configured 
CIR and CBS bandwidth limits. 
Broadcast + 
Multicast + 
Unknown Unicast 
Traffic aggregation of Broadcast + Multicast + Unknown Unicast from the port is limited 
per the configured CIR and CBS bandwidth limits. 
Supported by all ETX-2i devices.  
Adding Policer Profiles 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Enter: 
policer-profile <policer-profile-name>. 
A Policer profile with the specified name is created and the following prompt is displayed: 
config>qos>policer-profile(<policer-profile-name>)$  
ETX-2i Devices 
5. Traffic Processing 
The new Policer profile parameters (except for name) are configured by default as described in 
Factory Defaults. 
3. Configure the Policer profile as described in Configuring Policer Profile Parameters. 
Configuring Policer Profile Parameters 
1. Navigate to configure qos policer-profile <policer-profile-name> to select the Policer profile to 
configure. 
The config>qos>policer-profile(<policer-profile-name>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying the CIR (Kbps), CBS 
(bytes), EIR (Kbps), and EBS 
(bytes) bandwidth limits  
bandwidth [cir <cir-kbit-sec>] 
[cbs <cbs-bytes>] [eir <eir-kbit-sec>] 
[ebs <ebs-bytes>] 
CIR & EIR allowed values: 
• 0–10,000,000 (100 Gbps) 
CBS & EBS allowed values: 
• ETX-2i, ETX-2i-10G,  
ETX-2i-B: 0, or 64–
2,097,151 
• ETX-2i-10G-B/8SFPP: 
16MB 
• ETX-2i-100G/4Q:  
0–32Mbyte 
CIR can be set to zero only if 
CBS is set to zero. 
EIR can be set to zero only if 
EBS is set to zero. 
CIR + EIR must not exceed 
the maximum available 
bandwidth. 
CBS should be greater than 
the maximum frame size. 
For Policer profiles that are 
attached to Ethernet ports 
to limit broadcast/multicast 
traffic, only the CIR and CBS 
parameters are relevant (EIR 
and EBS should be set to 0). 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
A high-speed Policer (CIR or 
EIR >= 100,000 Kbps) cannot 
be associated with more 
than 64 flows. 
The CIR and EIR granularities 
depend on the configured 
values, as described below. 
The actual rate is rounded 
down or up according to the 
setting of 
bandwidth-round-up. 
The CBS must be greater 
than or equal to the CIR 
divided by Policer 
granularity. 
Specifying if the Policer profile 
is color aware 
[no] color-aware 
Default: no color-aware 
Compensating for Layer-1 
overhead and additional VLAN 
tag (in bytes) 
compensation <0–63> 
 
Specifying whether to check 
CIR+EIR when determining 
packet color 
coupling-flag 
Default: disabled 
Generating Policer profile 
bandwidth status 
show status 
Generates a report showing 
QoS bandwidth rounding 
method, and CIR, CBS, EIR, 
and EBS values (provisioned 
and actual). 
See Viewing Policer Profile 
Bandwidth Status for 
details. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Specifying the traffic type 
traffic-type {all | broadcast | multicast | 
unknown-unicast | broadcast-and-multicast | 
broadcast-and-multicast-
and-unknown-unicast}  
Note: 
• Traffic types other than 
all are relevant only for 
Policer profiles attached 
to ports. 
• All devices support traffic 
aggregation of 
broadcast-and-multicast
-and-unknown-unicast. 
Policer CIR/EIR Granularity 
Note 
IR values in the tables below (at rates above 1G) are rounded. 
 
 
IR (CIR, EIR) 
CBS < 2 MB 
IR < 10000 Kbps (10 Mbps) 
10 Kbps 
10000 ≤ IR < 100000 Kbps (100 Mbps) 
100 Kbps 
100000 ≤ IR < 1000000 Kbps (1 Gbps) 
1 Mbps 
1 Gbps ≤ IR < 1.6 Gbps 
100 Kbps  
1.6 Gbps ≤ IR < 16.3 Gbps 
1 Mbps 
16.3 Gbps ≤ IR < 100 Gbps 
10 Mbps 
 
IR (CIR, EIR) 
2 MB ≤ CBS < 4 MB 
IR < 10000 Kbps (10 Mbps) 
20 Kbps 
10000 ≤ IR < 100000 Kbps (100 Mbps) 
200 Kbps 
100000 ≤ IR < 1000000 Kbps (1 Gbps) 
2 Mbps 
1 Gbps ≤ IR < 3.3 Gbps 
200 Kbps  
3.3 Gbps ≤ IR < 32.7 Gbps 
2 Mbps 
32.7 Gbps ≤ IR < 100 Gbps 
20 Mbps 
 
 
ETX-2i Devices 
5. Traffic Processing 
IR (CIR, EIR) 
4 MB ≤ CBS < 8 MB 
IR < 10000 Kbps (10 Mbps) 
40 Kbps 
10000 ≤ IR < 100000 Kbps (100 Mbps) 
400 Kbps 
100000 ≤ IR < 1000000 Kbps (1 Gbps) 
4 Mbps 
1 Gbps ≤ IR < 6.5 Gbps 
400 Kbps  
6.5 Gbps ≤ IR < 65.3 Gbps 
4 Mbps 
65.3 Gbps ≤ IR < 100 Gbps 
40 Mbps 
 
IR (CIR, EIR) 
8 MB ≤ CBS < 16 MB 
IR < 10000 Kbps (10 Mbps) 
80 Kbps 
10000 ≤ IR < 100000 Kbps (100 Mbps) 
800 Kbps 
100000 ≤ IR < 1000000 Kbps (1 Gbps) 
8 Mbps 
1 Gbps ≤ IR < 1.3 Gbps 
80 Kbps  
1.3 Gbps ≤ IR < 13.1 Gbps 
800 Kbps 
13.1 Gbps ≤ IR < 100 Gbps 
8 Mbps 
 
IR (CIR, EIR) 
16 MB ≤ CBS < 32 MB 
IR < 10000 Kbps (10 Mbps) 
160 Kbps 
10000 ≤ IR < 100000 Kbps (100 Mbps) 
1600 Kbps 
100000 ≤ IR < 1000000 Kbps (1 Gbps) 
16 Mbps 
1 Gbps ≤ IR < 2.6 Gbps 
160 Kbps  
2.6 Gbps ≤ IR < 26.2 Gbps 
1600 Kbps 
26.2 Gbps ≤ IR < 100 Gbps 
16 Mbps 
 
ETX-2i Devices 
5. Traffic Processing 
Note 
• 
Rounded to 64 Kbps granularity for low speed Policers 
• 
Rounded to 500 Kbps granularity for high speed Policers 
• 
If bandwidth-round-up is disabled, the info command displays the 
rounded down CIR/EIR granular values. However, if bandwidth-round-up 
is enabled, the CIR/EIR values that you configured are displayed. 
• 
The output of the show status command displays the CIR and EIR 
configured and granular values, regardless of the rounding method used 
(see Viewing Policer Profile Bandwidth Status). 
Examples 
 To create and configure a Policer profile named Policer4: 
• 
CIR = 50,000 Kbps 
• 
CBS = 28,000 bytes  
• 
EIR = 30,000 Kbps 
• 
EBS = 20,000 bytes 
• 
Compensation = 56 
• 
no bandwidth-round-up (the default) 
ETX-2i-B>config>qos# policer-profile Policer4 
ETX-2i-B>config>qos>policer-profile(Policer4)$ compensation 56 
ETX-2i-B>config>qos>policer-profile(Policer4)$ bandwidth cir 50000 cbs 28000 eir 30000 ebs 
20000 
 To display the configuration information for Policer profile Policer4: 
ETX-2i-B# configure qos policer-profile Policer4$ info  
    bandwidth cir 50000 cbs 28000 eir 30000 ebs 20000 
    compensation 56 
 
Note 
As CBS is in the <2 MB range and IR is in the 10-100Mbps range, the 
granularity factor is 100 Kbps, and therefore the configured values are not 
changed, as seen in the output of the info command. 
 
 
ETX-2i Devices 
5. Traffic Processing 
 To create and configure a Policer profile named Policer5 (ETX-2i): 
• 
CIR = 50,000 Kbps 
• 
CBS = 19,000,000 bytes  
• 
EIR = 30,000 Kbps 
• 
EBS = 20,000 bytes 
• 
Compensation = 56 
• 
no bandwidth-round-up (the default) 
ETX-2i>config>qos# policer-profile policer5 
ETX-2i>config>qos>policer-profile(policer5)$ compensation 56 
ETX-2i>config>qos>policer-profile(policer5)$ bandwidth cir 50000 cbs 19000000 eir 30000 ebs 
20000 
 To display the configuration information for Policer profile Policer5: 
  
ETX-2i>config>qos>policer-profile(policer5)$ info 
    bandwidth cir 49600 cbs 19000000 eir 28800 ebs 20000 
    compensation 560 
 
Note 
CIR and EIR are rounded down to 1600 Kbps granularity, as this is a low-speed 
Policer with burst size between 16 and 32 MB.  
As CBS is in the 16-32MB range and IR is in the 10-100 Mbps range, the 
granularity factor is 1600 Kbps. Therefore, the CIR and EIR configured values 
changed accordingly while the CBS was not required to change, as seen in the 
output of the info command. 
 To create and configure a Policer profile named p1 (ETX-2i-10G half 19-inch): 
• 
bandwidth-round-up (and then rebooting the device) 
• 
CIR = 301,200 Kbps 
• 
CBS = 65,000 bytes  
ETX-2i-10G>config>qos>policer-profile(p1)# bandwidth cir 301200 cbs 65000 
ETX-2i-10G>config>qos>policer-profile(p1)# info 
    bandwidth cir 301200 cbs 65000 eir 0 ebs 0 
ETX-2i Devices 
5. Traffic Processing 
Viewing Policer Profile Bandwidth Status  
When you configure the Policer Profile bandwidth limits, the device automatically rounds down or up 
the configured CIR and EIR values for granularity, depending on the setting of bandwidth-round-up (see 
Configuring Granularity Rounding), as follows: 
• 
no bandwidth-round-up – Configured CIR and EIR values are rounded down; the default. 
• 
bandwidth-round-up – Configured CIR and EIR values are rounded up. 
ETX-2i provides the show status command to view the Policer profile bandwidth status. 
 To display the Policer Profile bandwidth status: 
• 
When config > qos > no bandwidth-round-up 
ETX-2i# config>qos> policer-profile(1)# show status 
Bandwidth 
--------------------------------------------------------------- 
 
Current Rounding : Down 
 
Parameter     Provisioned Value    Actual Value 
-------------------------------------------------------------- 
CIR [Kbps]           : 10500             10500 
CBS [Bytes]          : 32000             32000 
EIR [Kbps]           : 20300             20300 
EBS [Bytes]          : 32000             32000  
• 
When config > qos > bandwidth-round-up 
ETX-2i >config>qos>policer-profile(1)# show status 
Bandwidth 
-------------------------------------------------------------- 
 
Current Rounding : Up 
 
Parameter     Provisioned Value    Actual Value 
--------------------------------------------------------------- 
CIR [Kbps]  : 10560                10600 
CBS [Bytes] : 32000                32000 
EIR [Kbps]  : 20300                20400 
EBS [Bytes] : 32000                32000 
 
 
ETX-2i Devices 
5. Traffic Processing 
The fields are described in the following table: 
Parameter 
Description 
Current Rounding 
Displays rounding method configured under config > qos level (see Configuring 
Granularity Rounding).  
Possible values: 
• Down – CIR/EIR provisioned values are rounded down for granularity (default). 
• Up – CIR/EIR provisioned values are rounded up for granularity. 
CIR Provisioned Value 
Configured CIR value 
CIR Actual Value 
Rounded up/down CIR granular value 
CBS Provisioned Value 
Configured CBS value 
CBS Actual Value 
Same as CBS Provisioned Value (no CBS rounding) 
EIR Provisioned Value 
Configured EIR value 
EIR Actual Value 
Rounded up/down EIR granular value 
EBS Provisioned Value 
Configured EBS value 
EBS Actual Value 
Same as EBS Provisioned Value (no EBS rounding) 
Configuring Policer Aggregates 
You can define a Policer aggregate that specifies a non-Envelope (Aggregate) Policer profile (MEF 10.2) 
or an Envelope Policer profile (MEF 10.3) to apply to several flows. This is useful if you want to set 
bandwidth limits that are divided among more than one flow. 
 
Note 
In ETX-2i-100G/4Q, the ingress ports of all flows sharing the same Policer 
aggregate profile must be from the same port group: 
• 
Group 1: 3/1, 3/2 
• 
Group 2: All other ports 
Factory Defaults 
By default, no Policer aggregates exist. When a Policer aggregate is created, it has the following 
configuration: 
• 
No assigned Policer profile 
• 
No assigned flows  
• 
Rate sampling window (interval for sampling the associated flow statistics) set to 15 minutes 
ETX-2i Devices 
5. Traffic Processing 
Adding Policer Aggregates 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Enter: 
policer-aggregate <policer-aggregate-name> 
A Policer aggregate with the specified name is created and the config>qos>policer-
aggregate(<policer-aggregate-name>)$ prompt is displayed. The new Policer aggregate 
parameters are configured by default as described in Factory Default. 
3. Configure the policer aggregate as described in Configuring Policer Aggregate Parameters. 
Configuring Policer Aggregate Parameters 
1. Navigate to configure qos policer-aggregate <policer-aggregate-name> to select the Policer 
aggregate to configure. 
The following prompt is displayed: 
config>qos>policer-aggregate(<policer-aggregate-name>)# 
2. Perform the required tasks according to the following table. 
 
Note 
You assign flows to the Policer aggregate in the flow level (see Configuring 
Flows for details).  
 
Task 
Command 
Comments 
Binding Aggregate Policer to 
regular Policer profile or 
Envelope Policer profile  
policer { profile <policer-profile-name>  
|envelope <envelope-profile-name> } 
profile – regular Policer 
profile (MEF 10.2)  
envelope – Envelope 
Policer profile (MEF 10.3) 
Specifying rate sampling 
window (minutes) 
rate-sampling-window <1–30> 
 
Displaying the associated flows 
show flows 
 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Displaying statistics for the 
associated flows 
show statistics running 
When the Aggregate 
Policer is bound to a 
regular Policer profile, 
Aggregate Policer statistics 
show the regular flow 
statistics. 
When the Aggregate 
Policer is bound to an 
Envelope Policer profile, 
Aggregate Policer statistics 
show multi-CoS statistics. 
Clearing the statistics for the 
associated flows 
clear-statistics 
 
Examples 
 To create and configure a Policer aggregate named Aggr1: 
• 
Policer profile: Policer4 (created in Policer profile example). 
exit all 
configure qos  
  policer-aggregate Aggr1  
    policer profile Policer4 
    exit all 
Configuring Envelope Profiles 
This section explains how to configure Envelope profiles, to apply to multi-Cos flows per MEF 10.3.  
Adding Envelope Policer Profiles 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Enter envelope-profile <envelope-profile-name> 
An Envelope profile with the specified name is created and the following prompt is displayed: 
config>qos>envelope-profile(<envelope-profile-name>)$  
The new Envelope profile parameters are configured by default as described in Factory Defaults. 
3. Configure the Envelope profile as described in Configuring Envelope Profile Parameters. 
ETX-2i Devices 
5. Traffic Processing 
Configuring Envelope Profile Parameters 
1. Navigate to configure qos envelope-profile <envelope-profile-name> to select the Envelope 
profile to configure. 
The config>qos>policer-profile(<envelope-profile-name>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
 
Task 
Command 
Comments 
Defining policy for excess 
bandwidth sharing  
cf-policy {sharing-excess-bw | 
uncoupled-bw-sharing} 
sharing-excess-bw – Excess 
bandwidth is shared to excess 
token bucket. Selecting this 
parameter automatically sets 
coupling-flag-0 to 0 and sets 
each CoS coupling flag to 1.  
uncoupled-bw-sharing – Excess 
bandwidth is shared 
independently from EIR/EBS. 
Selecting this parameter 
automatically sets 
coupling-flag-0 to 0 and sets 
each CoS coupling flag to 0. 
If you enter no cf-policy, you can 
configure coupling-flag-0; each 
CoS coupling flag determines the 
bandwidth sharing. 
See Envelope Bandwidth 
Profiles. 
Specifying if the Envelope 
profile is color aware 
color-aware 
 
Specifying the 
compensation (bytes) 
compensation <value> 
Possible values: 0–63 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Specifying the CIR (Kbps), 
CBS (bytes), EIR (Kbps), 
and EBS (bytes) bandwidth 
limits, for a particular CoS 
cos <value> bandwidth [cir <cir-kbit-sec>] 
[cir-max <cir-max-kbit-sec>] [cbs <cbs-bytes>] 
[eir <eir-kbit-sec>] 
[eir-max <eir-max-kbit-sec>] 
[ebs <ebs-bytes>] 
[coupling-flag <coupling-flag>] 
• Range for cos value is 0–7; 
you can define up to four or 
eight cos values in an 
Envelope profile. 
• Range for <cir-kbit-sec>, 
<cir-max-kbit-sec>, 
<eir-kbit-sec>, and 
<eir-max-kbit-sec>: 
0–10000000 (0–10 Gbps) 
• Range for <cbs-bytes>, 
<ebs-bytes>:  
0–2000000 (0–2Mbytes) 
• <cir-max-kbit-sec> must be 
greater than or equal to 
<cir-kbit-sec>. 
• <eir-max-kbit-sec> must be 
greater than or equal to 
<eir-kbit-sec>. 
• coupling-flag controls the 
path of overflow tokens: 
0=overflow to committed 
token bucket, 1= overflow to 
excess token bucket. 
Specifying path of overflow 
bandwidth 
coupling-flag-0 <value> 
<value> is 0–1: 
0=discard, and 1=excess token 
bucket of the highest rank 
Generating Envelope 
profile bandwidth status 
show status 
Generates a report showing QoS 
bandwidth rounding method, 
the number of CoS, and CIR, CIR 
Max, CBS, EIR, EIR Max, and EBS 
values (provisioned and actual). 
See Viewing Envelope Profile 
Bandwidth Status for details. 
 
ETX-2i Devices 
5. Traffic Processing 
Note 
• 
If bandwidth-round-up is disabled, the info command displays the 
rounded down CIR, EIR, CIR Max, and EIR Max granular values. However, 
if bandwidth-round-up is enabled, the CIR, EIR, CIR Max, and EIR Max 
values that you configured are displayed. 
• 
The output of the show status command displays the CIR, EIR, CIR Max, 
and EIR Max configured and granular values, regardless of the rounding 
method used (see Viewing Shaper Profile Bandwidth Status).  
Viewing Envelope Profile Bandwidth Status  
When you configure the Envelope Profile bandwidth limits, the device automatically rounds down or up 
the configured CIR, EIR, CIR Max, and EIR Max values for granularity, depending on the setting of 
bandwidth-round-up (see Configuring Granularity Rounding), as follows: 
• 
no bandwidth-round-up – Configured CIR, EIR, CIR Max, and EIR Max values are rounded down; 
the default. 
• 
bandwidth-round-up – Configured CIR, EIR, CIR Max, and EIR Max values are rounded up. 
ETX-2i provides the show status command to view the Envelope profile bandwidth status. 
 To display the Envelope Profile bandwidth status: 
• 
When config > qos > no bandwidth-round-up 
ETX-2i# config>qos> envelope-profile(1)# show status 
 
Current Rounding : Down 
 
COS : 3 
 
Parameter     Provisioned Value    Actual Value 
--------------------------------------------------------------- 
CIR [Kbps]      : 10400                10400 
CIR MAX [Kbps]  : 65000                54600 
CBS [Bytes]     : 64000                64000 
EIR [Kbps]      : 12400                12400 
EIR MAX [Kbps]  : 75000                62600 
EBS [Bytes]     : 64000                64000 
• 
When config > qos > bandwidth-round-up 
ETX-2i # con qos envelope-profile 1 
ETX-2i >config>qos>envelope-profile(1)# show status 
 
 
 
ETX-2i Devices 
5. Traffic Processing 
Current Rounding : Up 
 
COS : 1 
 
Parameter     Provisioned Value    Actual Value 
--------------------------------------------------------------- 
CIR [Kbps]     : 15400                15500 
CIR MAX [Kbps] : 50000                34600 
CBS [Bytes]    : 32000                32000 
EIR [Kbps]     : 22300                22400 
EIR MAX [Kbps] : 60000                37700 
EBS [Bytes]    : 32000                32000 
 
 
COS : 3 
 
Parameter     Provisioned Value    Actual Value 
--------------------------------------------------------------- 
CIR [Kbps]     : 10400                10500 
CIR MAX [Kbps] : 65000                54600 
CBS [Bytes]    : 64000                64000 
EIR [Kbps]     : 12400                12500 
EIR MAX [Kbps] : 75000                62600 
EBS [Bytes]    : 64000                64000 
The fields are described in the following table: 
Parameter 
Description 
Current Rounding 
Displays rounding method configured under config > qos level (see Configuring 
Granularity Rounding).  
Possible values: 
• Down – CIR/EIR/CIR MAX/EIR MAX provisioned values are rounded down for 
granularity (default). 
• Up – CIR/EIR/CIR MAX/EIR MAX provisioned values are rounded up for 
granularity. 
COS 
Number of the CoS configured with the bandwidth values. 
CIR Provisioned Value 
Configured CIR value 
CIR Actual Value 
Rounded up/down CIR granular value 
CIR MAX Provisioned 
Value 
Configured CIR Max value 
CIR MAX Actual Value 
Rounded up/down CIR MAX granular value 
CBS Provisioned Value 
Configured CBS value 
CBS Actual Value 
Same as CBS Provisioned Value (no CBS rounding) 

## Queue Block Profiles  *(p.1030)*

ETX-2i Devices 
5. Traffic Processing 
Parameter 
Description 
EIR Provisioned Value 
Configured EIR value 
EIR Actual Value 
Rounded up/down EIR granular value 
EIR MAX Provisioned 
Value 
Configured EIR Max value 
EIR MAX Actual Value 
Rounded up/down EIR MAX granular value 
EBS Provisioned Value 
Configured EBS value 
EBS Actual Value 
Same as EBS Provisioned Value (no EBS rounding) 
Queue Block Profiles 
To facilitate congestion management, you can sort traffic by applying queue block profiles to queue 
block entities. A queue block profile contains entries for queues 0–7, with the following parameters: 
• 
Scheduling method: 
 
Strict – high-priority queues that are always serviced first. If a lower-priority queue is being 
serviced and a packet enters a higher queue, that queue is serviced immediately.  
 
WFQ (weighted fair queuing) – If one port does not transmit, its unused bandwidth is shared 
by the ‘transmitting’ queues according to the assigned weight. WFQ frames are transmitted 
only after transmission of any frames associated with Strict queues is completed.  
 
BE (best effort) – lowest priority queue(s). One or both of the lowest queues (Queue 6 
and/or Queue 7) in a level 0 queue block can be configured as BE. Packets in BE queues are 
transmitted only if there are no packets in the WFQ or Strict queues.  
 
Strict BE – When a BE queue is defined, it is strict in relation to the queues beneath it.  
• 
Number of frame buffers – Each frame buffer holds one queued packet; therefore, the number 
of frame buffers determines how many packets the queue can hold at one time. For example, if 
you configure 16384 frame buffers, then the queue can tolerate bursts of up to 16384 packets 
(if the queue size allows it). 
• 
Depth (queue size), in bytes. 
ETX-2i devices, with the exception of ETX-2i-100G/4Q, support the following queue block scheduling 
schemes (see figure below): 
• 
Level-0 – Seven SP/WFQ queues and one SP/WFQ/BE queue 
• 
Level 1 – Each queue either SP or WFQ 
ETX-2i Devices 
5. Traffic Processing 
ETX-2i-100G/4Q supports the following queue block scheduling scheme (see figure below): 
• 
Level 0 – Four SP queues and four WFQ queues 
• 
Level 1 – All queues WFQ 
 
The device rejects (sanity) any queue block with a different scheduling scheme. 
ETX-2i Devices 
5. Traffic Processing 
Factory Defaults 
ETX-2i provides a default queue block profile named DefaultQueue1, which defines queues 0–7. 
For all devices, with the exception of ETX-2i-100G/4Q, DefaultQueue1 is defined as follows: 
• 
Congestion avoidance – WRED profile corresponding to queue 
• 
Scheduling method – Eight queues WFQ, with default weight 100 
• 
Number of frame buffers – 511 
• 
Queue depth – 49152 
For ETX-2i-100G/4Q, DefaultQueue1 is defined as follows: 
• 
Scheduling method: 
 
Four strict priority (SP) queues 
 
Four WFQ queues, with default weight 100 
• 
Number of frame buffers – 4095 
• 
Queue depth – 8380416  
Adding Queue Block Profiles 
This section explains how to define queue block profiles. 
 To add a queue block profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Enter:  
queue-block-profile <queue-block-profile-name> [number-of-queues <number>] 
A queue block profile with the specified name, and number of queues, is created, and the 
following prompt is displayed: config>qos>queue-block-profile(<queue-block-profile-name>)$ 
The queues for the new profile are configured by default as described in Factory Defaults. 
3. Configure the queue block profile as described in Configuring Queue Block Profile Parameters. 
ETX-2i Devices 
5. Traffic Processing 
Configuring Queue Block Profile Parameters 
 To configure a queue block profile: 
1. Navigate to config qos queue-block-profile <queue-block-profile-name> to select the queue 
block profile to configure. 
The config>qos>queue-block-profile(<queue-block-profile-name>)# prompt is displayed. 
2. Perform the following for each queue that you wish to configure: 
a. To configure a queue, enter: 
queue <queue-ID> 
The following prompt is displayed: 
config>qos>queue-block-profile(<queue-block-profile-name>)>queue(<queue-ID>)#. 
b. Perform the required tasks according to the following table. 
c. Enter exit to return to the queue block profile context. 
Task 
Command 
Comments 
Specifying WRED profile 
that provides congestion 
avoidance policy  
congestion-avoidance wred 
profile <wred-profile-
name> 
wred-profile-name – name of predefined wired 
profile. 
Specifying queue depth (in 
bytes) 
depth <value>  
Possible values: 64–1048576 for ETX-2i 1GbE 
port33554431 
Note:  
• If the queue depth is configured to below 64, it 
is automatically rounded up to 64 bytes. 
• The queue depth that you configure might be 
changed by ETX-2i due to granularity (see the 
relevant Queue Depth Granularity table 
below). After you configure the queue depth, it 
is recommended to use info detail to see the 
actual value. 
• If a queue contains a relatively small amount of 
frame buffers, it is possible for the queue to be 
full when every buffer is in use, even if the 
queue size has not reached the maximum. This 
is more likely to happen in the case of relatively 
small frame sizes. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Specifying maximum 
frame buffers 
frame-buffers <number> 
Possible values:  
ETX-2i, ETX-2i-B: 0–16383  
ETX-2i-10G (full and half 19-inch), 
ETX-2i-100G/4Q): 0-4095 
Setting scheduling method  scheduling { strict | wfq 
<weight>| best-effort } 
The WFQ weight range is 3–1000 
Strict priority queues must have queue indices 
lower than WFQ or best-effort queues, and WFQ 
queues must have queue indices lower than 
best-effort queues. 
Note: Proper weight configuration should use the 
highest possible WFQ weight values.  
For example:  
Option 1: queue 1 weight = 3, queue 2 weight = 7 
Option 2: queue 1 weight = 300, queue 2 weight = 
700  
 
Queue Depth Granularity for ETX-2i, ETX-2i-B, ETX-2i-10G, and ETX-2i-100G 
Entered Via CLI 
Granularity 
0–65535 
64 
65536–131071 
128 
131072–262143 
256 
262144–524287 
512 
524288–1048575 
1024 
1048576–2097151 
2048 
2097152–4194303 
4096 
4194304–8388607 
8192 
8388607-16777215 
16384 
16777216-33554431 
32768 
 
 
ETX-2i Devices 
5. Traffic Processing 
Example 
 To create and configure a queue block profile named QBlockProf1: 
• 
Queue 0 set to strict scheduling and depth 524,288 
• 
Queue 1 set to strict scheduling and depth 212,992 
• 
Queues 2 and 3 set to WFQ scheduling with weight 75 
• 
Queues 6 and 7 set to Best Effort and depth 49,152 
exit all  
configure qos queue-block-profile QBlockProf1 
  queue 0 
    scheduling strict 
    depth 524288 
    exit 
  queue 1 
    scheduling strict 
    depth 212992 
    exit 
  queue 2 
    scheduling wfq 75 
    exit  
  queue 3 
    scheduling wfq 75 
    exit  
  queue 6 
    scheduling best-effort 
    depth 49152 
    exit 
  queue 7  
    scheduling best-effort 
    depth 49152 
    exit all 
 
 

## Queue Group Profiles  *(p.1036)*

ETX-2i Devices 
5. Traffic Processing 
Queue Group Profiles 
To facilitate congestion management, you can sort traffic by applying queue group profiles.  
Factory Defaults 
ETX-2i provides a default queue group profile named DefaultQueueGroup, with the following definition:  
• 
Two queue blocks 
• 
QB profile – DefaultQueue1 
• 
Level 1 QB profile – Scheduling1 (all WFQ in ETX-2i-100G/4Q) 
DefaultQueueGroup is configured as shown: 
ETX-2i# configure qos queue-group-profile DefaultQueueGroup 
ETX-2i> config>qos>queue-group-profile(DefaultQueueGroup)# info detail 
        queue-block 1/1 
            name "Level1QueueBlock" 
            profile "Scheduling1" 
            no shaper 
        exit 
        queue-block 0/1 
            name "Put your string here" 
            profile "DefaultQueue1" 
            bind queue 0 queue-block 1/1 
            shaper profile "Shaper1" 
        exit 
        queue-block 0/2 
            name "Put your string here" 
            profile "DefaultQueue1" 
            bind queue 1 queue-block 1/1 
            shaper profile "Shaper1" 
        exit 
ETX-2i-100G/4Q provides a default queue group profile named DefaultQueueGroup1, with the following 
definition: 
• 
Two queue blocks 
• 
QB profile – DefaultQueue2 
• 
Level1 QB profile – Scheduling2 (all WFQ) 
ETX-2i Devices 
5. Traffic Processing 
Adding Queue Group Profiles 
 To add a queue group profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Enter: 
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
2. Select a queue block in level 0 or 1 to configure: 
queue-block 0/<1–31> 
queue-block 1/1 
The following prompt is displayed: 
config>qos>queue-group-profile(<q-grp-profile-name>)>queue-block(<level/ID>)# 
3. Perform the required tasks according to the following table. 
4. If you wish to configure another queue block, type exit to return to the queue group profile 
context and start again at step 2. 
Task 
Command 
Comments 
Assigning a name to the queue 
block  
name <block-name> 
 
Assigning a queue block profile  
profile <queue-block-profile-name> 
 
Assigning a Shaper profile 
shaper profile <shaper-profile-name> 
 
 
ETX-2i Devices 
5. Traffic Processing 
Note 
Normally there is no need for you to enter the bind command. When you add 
a queue block in level 0 to the profile, bind is done automatically. 
You cannot use the bind command if the queue group contains a single 
queue block in level 0.  
Examples 
Note 
This example uses the Shaper profile and queue block profile created in the 
examples in the preceding sections.  
 To create and configure a queue group profile named QGroupProf1: 
• 
Queue block 0/1: 
 
Queue block profile: QBlockProf1 
 
Shaper profile: Shap2 
Note 
Queue blocks 1/1 and 0/2 are automatically created.  
 
exit all 
configure qos queue-group-profile QGroupProf1 
   queue-block 0/1 
    profile QBlockProf1 
    shaper profile Shap2 
     exit all 
 To display the configuration information for queue group profile QGroupProf1 
ETX-2i# configure qos queue-group-profile QGroupProf1 
ETX-2i>config>qos>queue-group-profile(QGroupProf1)# info detail 
    queue-block  1/1 
        name  "Level1QueueBlock" 
        profile  "Scheduling2" 
    exit 
    queue-block  0/1 
        name  "Put your string here" 
        profile  "QBlockProf1" 
        bind queue  0 queue-block  1/1 
        shaper profile  "Shap2" 
    exit 
    queue-block  0/2 
        name  "Put your string here" 
        profile  "DefaultQueue1" 
        bind queue  1 queue-block  1/1 
        shaper profile  "Shaper1" 
    exit  

## WRED Profiles  *(p.1039)*

ETX-2i Devices 
5. Traffic Processing 
WRED Profiles 
The ETX-2i traffic management engine employs a weighted random early discard (WRED) mechanism for 
intelligent queue management and congestion avoidance. The WRED algorithm monitors the fill level of 
each queue and determines whether an incoming packet should be queued or dropped, based on 
statistical probabilities. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products. 
Functional Description 
Congestion control policy is defined by: 
• 
Tail drop for green packets – Packets are queued if there is room in the queue and are dropped 
if the queue is full. 
• 
WRED profile for yellow packets 
WRED profiles include the following parameters: 
Maximum drop 
probability 
A percentage of the maximum threshold queue size that defines the 
drop probability 
Minimum threshold 
Set to a percentage of the maximum queue depth. If a packet is 
queued and the queue size is between 0 and the minimum 
threshold, the packet is admitted. 
Maximum threshold 
Set to a percentage of the maximum queue depth. If a packet is 
queued and the queue size is between the minimum threshold and 
the maximum threshold, the packet is dropped according to the 
drop probability of the particular queue size. 
Probability 
Set to a percentage of the maximum threshold queue size that 
defines the drop probability 
 
 
ETX-2i Devices 
5. Traffic Processing 
The following graph illustrates congestion control in ETX-2i. 
100%
Queue depth
(% of maximum)
Drop
 probability (%)
100%
Max
 threshold
Min
 threshold
WRED profile for
yellow packets
Tail drop for
green packets
 
There are eight WRED profiles available, named WREDProfile0 through WREDProfile7. They are bound 
to the internal queues automatically: WREDProfile0 is bound to queue 0, WREDProfile1 is bound to 
queue 1, etc. You cannot delete the WRED profiles, and you cannot add more WRED profiles. The 
binding of the profiles to the queues is set and cannot be changed, but you can change the profile 
parameters. You can view the assignment of WRED profiles to queues via the info command in the 
queue block profile level. 
Factory Defaults 
There are eight WRED profiles available, named WREDProfile0 through WREDProfile7, bound to the 
corresponding queues.  
Configuring WRED Profiles 
 To configure WRED profiles: 
1. Navigate to configure qos and type wred-profile WREDProfile<n> where n is 0 through 7. 
The config>qos>wred-profile(WREDProfile<n>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Setting the color  
color yellow 
no color yellow 
 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Setting the minimum 
threshold  
min <min-threshold> 
min-threshold – queue usage 
minimum threshold in 
percentage, 0–100 
Setting the maximum 
threshold  
max <max-threshold> 
max-threshold – queue usage 
maximum threshold in 
percentage, 0–100 
Setting the maximum drop 
percentage 
probability<max-probability> 
max-probability – percentage of 
packets to be dropped when the 
queue usage reaches the 
maximum limit 
 
Note 
You can configure the parameters for the color yellow only.  
Example 
 To configure WRED profile 4: 
• 
Minimum threshold 64 
• 
Maximum threshold 100 
• 
Probability 50 
exit all 
configure qos wred-profile WREDProfile4 
  color yellow min 64 max 100 probability 50  
  exit all 
save 
 To display the configuration information for WRED profile 4: 
ETX-2i# configure qos wred-profile WREDProfile4 
ETX-2i>config>qos>wred-profile(WREDProfile4)# info detail 
    color  yellow min  64 max  100 probability  50 
 
 