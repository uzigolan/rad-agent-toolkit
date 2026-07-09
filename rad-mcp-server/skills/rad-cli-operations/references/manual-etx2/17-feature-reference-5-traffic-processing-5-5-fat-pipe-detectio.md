# Feature Reference – 5 Traffic Processing – 5.5 Fat Pipe Detection and Rate Limiting

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 961–969.*


## Port based Fat Pipe Detection  *(p.961)*

ETX-2i Devices 
5. Traffic Processing 
Parameter 
Description 
Tunnel Source Interface 
Router interface anchoring the tunnel 
Possible values:  
• -- (No interface is configured.) 
• Router Interface <router number>/<interface number> 
Physical interface bound to the router interface anchoring the tunnel 
Possible values: 
• Empty string 
• (<port-type> <port-number>) 
Tunnel Source Address 
Tunnel source IP address 
Possible values:  
• -- (Tunnel address is not configured.) 
<IPv4 or IPv6 unicast address>/<prefix length> 
Tunnel Destination 
Tunnel destination IP address 
Possible values: 
• -- (Tunnel destination IP address is not configured.) 
• IPv4 or IPv6 unicast address 
Up For (seconds) 
Tunnel uptime 
Possible values: Time in seconds; Display hint: ddd Days, hh:mm:ss 
Tunnel Encapsulated  
Number of Rx packets since tunnel uptime 
Tunnel Decapsulated  
Number of Tx packets since tunnel uptime   
5.5 Fat Pipe Detection and Rate Limiting  
Fat pipe (or ‘LFP’, which stands for ‘Large Flow Prevention’) detection is a mechanism that detects high 
bandwidth sessions transmitted over the link and limits its bandwidth. The Fat Pipe mechanism can be 
port based or flow based. 
Port based Fat Pipe Detection 
The current mechanism limits each detected high bandwidth flow to a pre-configured rate regardless of 
the total service bandwidth to minimize traffic congestion and dropped packets in the network. 

## Flow based Fat Pipe Detection  *(p.962)*

ETX-2i Devices 
5. Traffic Processing 
The example below illustrates the port-based Fat pipe mechanism. It shows a case in which a high 
bandwidth flow is detected. The total egress traffic exceeds the value as configured to the service 
policer. The rate-limiting is released, once the session rate drops below a configured value during a 
period defined in the release-hold-time. 
 
 
Flow based Fat Pipe Detection 
The flow (service level) based Fat Pipe model supports a policing scheme, which limits each one of the 
detected Fat pipe flows and still prevents the total bandwidth from exceeding the service bandwidth as 
configured by the service policer. 
In addition, the mechanism dynamically preserves ‘bandwidth fairness’ between LFP and non-LFP traffic. 
The configuration concept is also different whereas the new Fat pipe detection model is configured per 
flow and not per port as the current mechanism. 
 
4G non LFP
6G LFP
UNI
Other (non LFP stream)
LFP stream
5G Policer
2G Policer
4G non LFP
2G LFP
    6G
NNI
 
 
 

## Applicability and Scaling  *(p.963)*


## Standards Compliance  *(p.963)*


## Functional Description  *(p.963)*

ETX-2i Devices 
5. Traffic Processing 
The mechanism detects up to two or six flows of high bandwidth, depending on ‘envelope-ranks’ 
configuration (config>qos# envelope-ranks {4|8} ): 
• 
If ‘envelope-ranks’ is configured to 4 (default), up to two flows of high bandwidth can be 
detected. 
• 
If ‘envelope-ranks’ is configured to 8, up to six flows of high bandwidth can be detected. 
 
Note 
The mechanism is supported over a single flow with a ‘match all’ classification. 
Applicability and Scaling 
This feature is applicable to ETX-2i-10G half 19-inch, ETX-2i-10G-B full and half 19-inch ordering options, 
ETX-2i-10G-B/8SFPP (full and half 19-inch models) ports 1-4, ETX-2i-100G/4Q, and ETX-2i-100G/40G user 
port groups only, i.e., ports 1/3-1/8, 3/3-3/4, and 2/1-2/8. 
Supports a single Fat pipe detection profile. 
You can bind up to two Ethernet ports or a single two-port LAG to a Fat pipe detection profile. 
Fat pipe detection profile can identify and rate limit (police) up to ten high BW sessions (micro flows) 
simultaneously. 
Fat pipe does not work under a bridge configuration. 
Standards Compliance 
N/A 
Functional Description 
Packet Frame Format 
The following packet types are supported and allow packet L3-L4 fields recognition: 
• 
Up to two VLAN tags 
• 
IPv4oETH 
• 
IPv6oETH 
ETX-2i Devices 
5. Traffic Processing 
• 
IPv4 in Ethernet over MPLS (VPLS) 
• 
IPv6 in Ethernet over MPLS (VPLS) 
• 
IPv4oMPLS, IPv6oMPLS (ETX-2i-10G-B/8SFPP and ETX-2i-10G half 19-inch in Charter ver. 6.4 
only) 
 
Up to three MPLS labels 
The following figures show the fields and layouts of an L3 VPN Service, a VPLS Service, and the Fat pipe 
detection profile search keys that can be defined to match the various fields in both scenarios.  
 
 
If a Fat pipe key includes both L2 and L3 keys, it will match the key for VPLS frames in the following way: 
• 
L2 fields match the Ethernet transport header of the VPLS 
• 
L3 and L4 fields match an IP frame (if present) in the encapsulated Ethernet frame. 
 
ETX-2i Devices 
5. Traffic Processing 
Fat Pipe Detection Workflow 
Fat pipe detection works as follows: 
1. Define the following in the Fat Detection profile (see Configuring Fat Pipe Detection below): 
 
Search key – used for Fat pipe differentiation; can include up to five of the following L2-L4 
fields (i.e., packet attributes): src-mac, dst-mac, ether-type, vlan, p-bit, dei, inner-ether-type, 
inner-vlan, inner-p-bit, dscp, ip-precedence, tos, protocol, src-ip-address, dst-ip-address, l4-
src-port, l4-dst-port.  
This means, for example, that if the search key selected is dst-ip-address, when the 
bandwidth of the packets going to a specific dst-ip-address adds up to more than the 
allowed bandwidth in the Policer, Fat pipe is detected, and the number of packets is limited. 
 
A preconfigured two-rate (CIR, EIR) three-color Policer BW profile – used to rate limit Fat 
pipe sessions.  
 
Release hold time – the amount of time that the Fat pipe Policer must stay below the 
defined CIR rate, in order to release the Policer. 
2. Bind the Fat detection profile to an Ethernet port (refer to Configuring Ethernet Port 
Parameters in the Cards and Ports chapter). Fat pipe detection begins. 
3. The Fat pipe search algorithm looks for exceptionally high BW sessions (up to ten simultaneous 
sessions) differentiated by the user-defined search key (i.e., with packets having fields that 
match the search key fields defined in the Fat pipe detection profile). When the session rate 
exceeds the CIR+EIR (PIR) rate defined in the Policer BW profile, a Fat pipe is declared found. It 
takes the algorithm ≤ one second to detect the first high-BW session, and ≤ 1+n seconds to 
detect the following n high-BW sessions. 
The following is relevant for ETX-2i-10G-B/8SFPP and ETX-2i-10G half 19-inch in Charter ver. 6.4 
only): 
 
Non-IP packets ignore IP keys defined in the Fat pipe detection profile, and match only L2 
keys (if they exist).  
 
If the only IP-level key defined in the Fat pipe detection profile is ip-precedence, a packet 
having this field with value 0 is interpreted as a non-IP packet and is not matched.  
 
IP-level search keys are applicable for L3-VPN services (IPv4oMPLS, IPv6oMPLS) for up to 
three nested MPLS labels. 
4. The Fat pipe detection procedure binds its defined two-rate three-color Policer BW profile to 
the exceptionally high-BW sessions, in order to rate limit the BW of these sessions. 
5. A Fat-pipe-found alarm (supported over the port bound to the Fat pipe profile) is issued for the 
first Fat pipe found (rate of detected rate exceeds configured CIR+EIR) or for the first Fat pipe 
found after the alarm has been cleared (see next step) and includes found values of the search 
key. 

## Factory Defaults  *(p.966)*


## Configuring Fat Pipe Detection  *(p.966)*

ETX-2i Devices 
5. Traffic Processing 
6. The sessions are monitored; once their BW drops below the CIR defined in the Policer for the 
defined release hold time, the Policer BW profile is released. Also, alarms are cleared, provided 
that there are no other Fat pipes in the system. Simultaneously, the search for additional high 
BW sessions is resumed (Step 3). 
 
Note 
Fat pipe traffic is detected according to the configured Fat pipe policer ONLY. 
Even if this traffic is part of a classified traffic stream that is configured to a 
different user-configured policer. 
7. At any time, you can display the information of active and history (closed) Fat pipes of an 
Ethernet port (refer to Viewing Fat Pipe Information in the Cards and Ports chapter).  
Factory Defaults  
By default, the device does not have a Fat pipe detection profile.  
The default release-hold-time of a newly created Fat pipe detection profile is 60 seconds.  
Configuring Fat Pipe Detection 
The following section describes how to create a profile with Fat pipe detection mechanism attributes.  
 To add a fat pipe detection profile to a port: 
1. Navigate to configure port. 
The config>port# prompt is displayed. 
2. Enter fat-pipe-detection-profile <profile-name>. 
A Fat pipe detection profile with the specified name is created.  
3. At the config>port>fat-pipe-detection-profile(<profile-name>)$ prompt, perform the required 
tasks according to the following table. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Configuring a search key 
for Fat pipe differentiation 
[no] search-key [src-mac] [dst-mac] 
[ether-type] [vlan] [p-bit] [dei] [inner-
ether-type] [inner-vlan] [inner-p-bit] 
[dscp] [ip-precedence] [tos] [protocol] 
[src-ip-address] [dst-ip-address] [l4-src-
port] [l4-dst-port] 
The search key used for Fat pipe 
differentiation can include up to five 
L2-L4 packet attributes.  
Note:  
• The order of the attributes is 
significant. 
• If you configure search-key with 
the p-bit parameter, you must also 
configure the vlan parameter.  
• If you configure search-key with 
the inner-p-bit parameter, you 
must also configure the inner-vlan 
parameter.  
• If you configure search-key with 
the dei parameter, you must also 
configure the vlan parameter. 
• If you configure search-key with 
the ip-precedence, tos, or dscp 
parameter, you must also configure 
the src-ip-address or dst-ip-
address parameter. 
• The search recognizes L3-L4 fields 
of both IPv4 and IPv6 packets. 
• Entering no search-key followed by 
parameters, removes those 
specified parameters from the 
search key. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Configuring Policer BW 
profile  
policer profile <<policer-profile-
name>> 
no policer <policer-profile-name> 
policer-profile-name – Policer BW 
profile name to be used for Fat pipe 
rate limiting and for find and clear 
criteria. 
Note:  
• You cannot change the Policer 
profile in an existing Fat pipe 
profile. Instead, you can create 
another Fat pipe profile with the 
desired Policer profile.  
• Entering no policer <policer-
profile-name> discontinues use of 
that Policer profile for Fat pipe rate 
limiting. 
Configuring time that 
session BW must remain 
below defined CIR in order 
to release Policer. 
release-hold-time <time> 
 T  
time – Time that session BW is 
required to remain below CIR in order 
to release the Policer from the session, 
and release Fat pipe from active Fat 
pipe list. 
Possible values: 30-3600 seconds 
 To add a fat pipe detection profile to a flow: 
1. Navigate to configure flow. 
The config>flows# prompt is displayed. 
2. Enter flow. 
3. The config>flows>flow# prompt is displayed. 
4. Enter fat-pipe-detection-profile <profile-name>. 
A Fat pipe detection profile with the specified name is created.  
 
Note 
Fat pipe detection and envelope policer cannot coexist on the same flow. 
 To detect existing Fat pipe detection profiles on a flow: 
• 
At the config>flows>flow# prompt, enter show fat-pipe-list {active | history | all}. 
 
 

## Deleting a Fat Pipe Detection Profile  *(p.969)*

ETX-2i Devices 
5. Traffic Processing 
The Fat pipe detection profiles are displayed as follows: 
Entry < # > :Detection time : < ToD >     Duration : < seconds>   Detected Rate    <Mbps>   
Current rate <Mbps>   Guaranteed rate <Mbps>   
                   key field 1 : <value> 
                   key field 2 : <value> 
                   key field 3 : <value> 
                   key field 4 : <value> 
                   key field 5 : <value> 
Examples: 
• 
To show only active Fat pipe detection profiles, enter the following: 
config>flows>flow# show fat-pipe-list active 
Flow { flow name }: Active fat-pipes { profile name } 
      1 Detection time:  31/07/2016 10:22:20  Duration: 350 seconds  Detected Rate:  2231Mbps 
Current Rate:      2500Mbps Guaranteed rate 1660Mbps  
                   Src-mac: 15:22:34:67:77:90 
                   Dst-mac: 11:22:33:44:55:66 
The CLI displays up to 10 active Fat pipe detection profiles. 
• 
To show only the Fat pipe detection profile history, enter the following: 
config>flows>flow# show fat-pipe-list history 
Flow { flow name }: History fat-pipes { profile name } 
      1 Detection time:  30/07/2016 22:10:47  Duration: 650 seconds  Detected Rate:  2551Mbps  
                   Src-mac: 21:22:23:24:25:26 
                   Dst-mac: 31:22:33:34:35:36 
• 
To show both active detection profiles and the history, enter show fat-pipe-list all at the 
prompt. 
The CLI displays up to 32 old (inactive) Fat pipe detection profiles in the history list. 
Deleting a Fat Pipe Detection Profile 
You can delete a Fat pipe detection profile only if it is not bound to a port. 
 To delete a Fat pipe detection profile: 
1. Navigate to configure port. 
The config>port# prompt is displayed. 
2. Enter no fat-pipe-detection-profile <profile-name>. 
The Fat pipe detection profile of the specified name is deleted if it is not bound to any port.  