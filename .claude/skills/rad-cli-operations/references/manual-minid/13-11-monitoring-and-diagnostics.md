# 11 Monitoring and Diagnostics

*Manual `MiNID_ver_2_6_mn.pdf`, pages 239–376.*


## 11.1 Layer-3 Service Activation Test  *(p.239)*

11.1 Layer-3 Service Activation Test 
The Layer-3 Service Activation Test (L3 SAT) provides an out-of-service (intrusive) IP/UDP test to assess 
the proper configuration and performance of an IP transport service prior to customer notification and 
delivery. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
ITU-T Y.1564 
Benefits 
The Y.1564 testing methodology allows service providers to have a standard way of measuring the 
performance of IP transport services. The tests are performed per multiple traffic streams 
simultaneously, confirming policing per EVC or EVC.CoS. 
Functional Description 
L3 SAT testing has the following objectives: 
• 
Validate that the IP transport service is correctly configured 
• 
Validate the quality of the services as delivered to the end user 
L3 SAT tests can be performed over Layer-3 networks. 
11. Monitoring and Diagnostics 
L3 SAT supports service performance test. 
Performance Test 
The performance test validates the quality of the services over a user-configurable period of time, as 
follows: 
• 
Traffic is generated for all services at the configured bandwidth level. 
• 
For all the test sessions, test packets are sent simultaneously at 100% of the bandwidth 
configured per test session 
• 
Per test session, the duration of the performance test is evenly divided between the different 
packet sizes, e.g. per test session, each packet size is transmitted for an equal amount of time 
The performance test is declared successful if the results are within SAC limits. 
Test Elements 
L3 SAT includes the following elements: 
• 
Generator – initiates multiple test sessions for multiple responders, sends out the test and OAM 
frames, receives responses from the responder, processes the resulting measurements, and 
displays test reports. Generator can support two responder types: TWAMP Light and IP Loop. 
• 
Peer – is used to run TWAMP test sessions. Only one peer can be configured per generator with 
IP address corresponding to responder 
• 
Test session – Only one test session can be configured per peer 
• 
Responders – receive test and OAM frames from generator and transmit responses to 
generator. Responders can be of the following types: 
 
TWAMP Light – receives a test packet, reflects the test packet after it, adds an Rx stamp and 
a Tx stamp 
 
IP loop – filters incoming traffic by destination IP address, and loops it back while 
performing MAC address swap and IP address swap 
L3 SAT generator supports a special packet format (short-packet mode) configured at the generator 
level. This mode can be enabled only with ip-loop responder. 
 
11. Monitoring and Diagnostics 
Factory Defaults 
By default, there are no L3 SAT entities configured in MiNID. 
When a peer profile is created, it has the following default configuration: 
 
Parameter 
Default  
Remarks 
performance-duration 
2h 
 
udp-port 
53248 
 
responder-type 
twamp-light 
 
When a session profile is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
delay-threshold 
200000 
 
delay-variation-threshold 
100000 
 
ip-size 
256 
 
loss-ratio-threshold 
100 
 
When a peer is created, there is no default configuration. 
When a test session is created, it has the following default configuration. 
 
Parameter 
Default  
Remarks 
<name> 
<Not applicable> 
<name> must be specified when the test session is created. 
session-profile  
<Not applicable> 
<profile-name> must be specified when the test session is created. 
bandwidth 
100 
<kbps> must be specified when the test session is created. 
dscp 
0 
 
When a generator is created, it has the following default configuration. 
 
Parameter 
Default  
Remarks 
<name> 
<Not applicable> 
<name> must be specified when the test session is created. 
11. Monitoring and Diagnostics 
Parameter 
Default  
Remarks 
session-profile  
<Not applicable> 
<profile-name> must be specified when the test session is created. 
 
Parameter 
Default  
Remarks 
peer 
<not applicable> 
This parameter has no default configuration. 
local-ip-address 
<not applicable> 
This parameter has no default configuration. 
Configuring L3 SAT Entities 
To configure L3 SAT, perform the following steps: 
1. In the responder device: 
a. Configure relevant router interface and flow. 
b. Configure and activate L3 SAT responder. 
2. In the generator device: 
a. Configure relevant router interface and flow. 
b. Configure L3 SAT peer and session profile. 
c. Configure and activate L3 SAT generator and relevant peer and test session. 
 
Note 
Only one peer profile and one session profile could be defined. 
Configuring a Generator 
 To configure an L3 SAT generator using the web interface: 
1. Navigate to Configuration > Test > L3SAT > Generator. 
2. Type in the name in the New Generator Name field. 
3. Click <Apply>. 
The new generator appears as a row in the generators table. 
 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Configuration>Test>L3SAT>Generator 
  
 
 
 New Generator 
Name 
 
 
  
 
 
 Apply 
 
 
  
 
 
 Generator 
Name 
Router 
Interface 
Router Interface 
oper status 
Generator 
Status 
 
 
 Gen1 
N/A 
N/A 
Not Ready 
Remove  
  
 
 
 
1. Click the generator name in the table. 
The generator profile page opens. 
2. Set the generator Local IP Address and Admin Status. 
3. Click <Apply>. 
MiNID 
  
 
 
 Configuration>Test>L3SAT>Generator> Generator Profiles (Gen1) 
  
 
 
 Local IP Address 
 
Router Interface 1 
 Add New Peer 
 
 
 Admin Status 
 
Disable 
 Short Packet Mode 
 
Disable 
 Apply 
 
 
  
 
 
 
Peer 
Short 
Packet 
Mode 
Last 
Connectivity 
Sub-test 
Responder 
Type 
Test 
Name 
UDP 
Port 
Status 
Summary 
Report 
Remove 
 
  
 
 
 
11. Monitoring and Diagnostics 
 To configure an L3 SAT generator using the CLI: 
1.  Navigate to configure test l3sat. 
The config>test>l3sat# prompt is displayed. 
2. Enter: 
generator <name> 
The config>test>l3sat>generator<name># prompt is displayed. 
3. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Assigning a router interface to 
the L3SAT generator 
local-ip-address <router-
interface-1|router-interface-2| 
router-interface-3|router-
interface-4|router-interface-5> 
If Loaned IP is enabled on router 
interface #1, generator IP 
address can be configured on 
any other router interface 
Defining peer entity 
(corresponding to generator) to 
run L3SAT session. 
peer <ip-address> 
 
Configuring the L3SAT test mode 
and the packet format 
[no] short-packet-mode 
 
short-packet-mode: 64–2028 
bytes frame 
no short-packet-mode: 95–
10240 bytes frame 
Administratively enabling or 
disabling the generator 
no shutdown 
Enter shutdown to 
administratively disable the 
generator 
Viewing generator status 
show status 
 
Configuring a Peer 
 To configure an L3 SAT peer using the web interface: 
1. On the Generator Profile page, click Add New Peer. 
2. On the Peer Profile page, set the parameters as detailed in the table below. 
3. Click <Apply>. 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Configuration>Test>L3SAT>Generator> Profiles Config>Add Peer 
  
 
 
 Activate 
 
Disable 
 Peer IP Address 
 
0.0.0.0 
 Peer Profile 
 
peer_profile 
 Apply 
 
 
  
 
 
 Test session 
Name 
Session 
Profile 
Bandwidth DSCP Report Remove  
  
 
 
 To configure an L3 SAT peer using the CLI: 
1. Navigate to configure test l3sat generator <name>. 
The config>test>l3sat>generator(<name>)# prompt is displayed. 
2. Enter: 
peer <ip-address> 
The prompt config>test>l3sat>generator(<name>)> peer(<ip-address>)# is displayed. 
3. Enter all necessary commands according to the tasks listed below. 
L3SAT Peer Parameters 
Task 
Command 
Comments 
Activating or deactivating the 
peer test sessions 
activate 
no activate 
You can activate a peer only if at 
least one test session has been 
configured 
Assigning a peer profile to use 
for the peer parameters 
peer-profile <profile-name> 
 
Assigning a test session  
test-session <name> session-
profile <session-profile> bw 
<bw-kbps> [dscp <dscp-
number>] 
bw –Rate of the test session 
traffic in Kbps. Range 4-1000000 
kbps 
dscp - Priority value for the test 
session traffic. Range: : 0-63  
(default: 0) 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Displaying results and 
measurements for a specific test 
show report  
Available only if peer was 
activated 
Displaying summary of test 
results and measurements 
show summary-report 
Available only if peer was 
activated 
Displaying the peer status 
show status 
 
Configuring a Peer Profile 
You can configure only one peer profile to associate with the peer. 
 To configure an L3 SAT peer profile using the web interface: 
1. Navigate to Configuration > Test > L3SAT > Peer Profile. 
2. In the New Peer Profile Name field, fill in the name. 
3. Click <Apply>. 
The peer profile appears in the table. 
MiNID 
  
 
 
 Configuration>Test>L3SAT>Peer Profile 
  
 
 
 New Peer Profile Name 
 
 
 Apply 
 
 
  
 
 
 Peer Profile Name 
 
 
 peer_prof 
Remove 
 
 
  
 
 
4. Click the peer profile name. 
The Peer Profile configuration page opens. 
5. Edit the peer profile parameters according to the tasks in the table below. 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Configuration>Test>L3SAT>Peer Profile>Peer Profiles Cfg (peer_prof) 
  
 
 
 Performance Duration 
 
2h 
 UDP Port 
 
53248 
 Responder Type 
 
TWAMP Light 
 Apply 
 
 
  
 
 
 To configure an L3 SAT peer profile using the CLI: 
1. Navigate to configure test l3sat. 
The config>test>l3sat># prompt is displayed. 
2. Enter: 
peer-profile <name> 
The config>test>l3sat>peer-profile<name># prompt is displayed. 
3. Enter all necessary commands according to the tasks listed below. 
L3SAT Peer Profile Parameters 
Task 
Command 
Comments 
Configuring the duration of the 
session 
performance-duration 
<15m|2h|24h|custom> 
Custom duration is measured in 
minutes. 
Specifying the type of the 
responder 
responder-type {twamp-
light|ip-loop} 
 
Specifying UDP port number 
udp-port <port-number> 
Range is <1-65535> 
Configuring a Session Profile 
You can configure only one L3 SAT session profile to associate with the peer. 
 To configure an L3 SAT session profile using the web interface: 
1. Navigate to Configuration > Test > L3SAT > Session Profile. 
2. In the New Session Profile Name field, fill in the name. 
11. Monitoring and Diagnostics 
3. Click <Apply>. 
The session profile appears in the table. 
 
MiNID 
  
 
 
 Configuration>Test>L3SAT>Session Profile 
  
 
 
 New Session Profile Name 
 
 Apply 
 
 
  
 
 
 Peer Profile Name 
 
 
 session_prof 
Remove 
 
 
  
 
 
4. Click the session profile name. 
The Session Profile configuration page opens. 
5. Edit the session profile parameters according to the tasks in the table below. 
6. Click <Apply>. 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Configuration>Test>L3SAT>Session Profile>Session Profiles Cfg 
(session_prof) 
  
 
 
 Loss Ratio Threshold 
 
100 
 Delay Threshold 
 
200000 
 Delay Variation 
Threshold 
 
100000 
 Packet Size 
128 
 
  
256 
 
  
512 
 
  
1024 
 
  
1280 
 
  
1500 
 
 Custom 
0 
 
 L1 Rate 
Disable 
 
 Apply 
 
 
  
 
 
 To configure an L3 SAT session profile using the CLI:  
1. Navigate to configure test l3sat. 
The config>test>l3sat># prompt is displayed. 
2. Enter: 
session-profile <name> 
The config>test>l3sat>session-profile<name># prompt is displayed. 
3. Enter all necessary commands according to the tasks listed below. 
L3 SAT Session Profile Parameters 
Task 
Command 
Comments 
Defining delay threshold in 
microseconds 
delay-threshold 
Range 0–1000000 
Defining delay variation 
threshold in microseconds 
delay-variation-threshold 
Range 0–1000000 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining if the test session 
bandwidth parameter is a Layer 
1 or Layer 2 rate  
l1-rate 
Default: no l1-rate (Layer 2 rate) 
Defining allowable test packet 
loss in ppm (parts per million) 
loss-ratio-threshold 
 
Defining test packet size in bytes 
packet-size 
{128|256|512|1024|1280|1500
} [custom <custom-size>] 
• You can specify up to four 
packet sizes 
• Range for custom size: 95–
2028 
Configuring Router Interface and Flow 
To configure a router interface, see Configuring Router Interface. 
To configure a flow, see Configuring Flows Using the Web Interface or Configuring Flows Using the CLI. 
Viewing L3 SAT Status 
You can view the status of the test as it is running: 
• 
Generator status 
 
in the web interface - the Generator row in the table as on Configuring a Generator. 
 
in the CLI - show status in the config test l3sat generator level 
 
MiNID>config>test>l3sat>generator(gen)# show status 
Router Interface             : 1 
Router Interface oper status : UP 
Generator Status             : Ready 
• 
Peer test session status  
 
in the Web interface – the Peer row in the table as on Configuring a Peer  
 
in the CLI – show status in level config test l3sat generator peer. 
MiNID-Generator>config>test>l3sat>generator(1)>peer(11.11.11.3)# show status 
Last Connectivity Sub-test   : Pass 
Short Packet Mode            : Enable  
Responder Type               : IP Loop 
 
Test Name                     UDP Port            status 
--------------------------------------------------------------- 
11. Monitoring and Diagnostics 
MiNID_SA                      862                 Pass 
 
MiNID-Generator>config>test>l3sat>generator(1)>peer(11.11.11.3)# 
Viewing L3 SAT Test Reports 
The generator calculates performance parameters according to the received test packets, for the peer 
and its active test session. Some performance parameters are recalculated on the fly (duration, delay, 
PDV, etc.); other parameters are recalculated at the end of the session (lost packets, loss ratio) The 
performance parameters are presented in test reports that can be viewed per peer and test session. 
 To display detailed test results in the CLI: 
MiNID-Generator>config>test>l3sat>generator(1)>peer(11.11.11.3)# show report 
End Points 
Generator Address    : 11.11.11.1 
Responder Address    : 11.11.11.3 
Short Packet Mode    : Enable  
Responder Type       : IP Loop 
UDP Port             : 862 
Test Rate Mode       : L1 
 
Test 
Scope                : Performance 
Peer Profile Name    : peer_profile 
BW [Kbps] - L1       : 4 
DSCP                 : 0 
Frame Size           : 128 
 
Session Profile Name : l3sat_session 
Start Date & Time    : 00:39:50 01-01-1970 
End Date & Time      : 00:40:53 01-01-1970 
Total Duration       : 00:01:03 
Overall Result       : Pass 
 
 Performance Phase 
--------------------------------------------------------------------- 
Duration [min]       : 1:03 
Performance Result   : Pass 
 
Parameter              Frame Size  Threshold 
                       #1 
                       128 bytes 
--------------------   ----------- 
Duration [min]         1:00 
Tx Rate [Kbps]         4 
IR - mean [Kbps]       4.990 
PL - count             0 
PLR                    0.000%       1.00E-01 
PTD - min [ms]         0.020 
11. Monitoring and Diagnostics 
PTD - mean [ms]        0.020        200000 
PTD - max [ms]         0.021 
PDV - mean [ms]        0.000 
PDV - max [ms]         0.000        100000 
--------------------   ----------- 
Result                 Pass 
MiNID-Generator>config>test>l3sat>generator(1)>peer(11.11.11.3)# 
L3 SAT Report Parameters 
Counter 
Description 
Information rate (IR) 
Number of received times test packet Ethernet frame length (in 
bits), divided by the elapsed time (in seconds) 
Frame rate (frms/sec) 
Shown on web only. Frame rate takes the total frame size into 
consideration (frame size plus preamble and inter-frame gap)  
Packet loss (PL) 
Number of lost test packets. A test packet is considered lost if it 
was not received back at the generator, or was received with a 
round-trip delay of over two seconds. 
Packet loss ratio (PLR) 
Number of lost packets divided by the number of transmitted 
packets 
One-way inter-packet delay 
variation (IPDV-Fwd)), forward – 
mean 
Average forward IPDV. IPDV is calculated according to RFC 
3393, from the variations of the delays between valid packets. 
One-way inter-packet delay 
variation (IPDV-Fvd), forward – 
max 
Maximum forward IPDV 
One-way inter-packet delay 
variation (IPDV-Bck), backward – 
mean 
Average backward IPDV. IPDV is calculated according to RFC 
3393, from the variations of the delays between valid packets. 
One-way inter-packet delay 
variation (IPDV-Bck), backward - 
max 
Maximum backward IPDV 
Round-trip packet transfer delay 
(PTD) –min 
Minimum round-trip PTD. The round-trip PTD is calculated from 
the test packet embedded timestamps. A round-trip PTD over 
two seconds is ignored, as the packet is considered lost. 
Round-trip PTD – mean 
Average round-trip PTD 
Round-trip PTD – max 
Maximum round-trip PTD 
Round-trip delay variation (PDV) – 
mean 
Average round-trip PDV. The round-trip PDV is calculated 
according to ITU-T Y.1540, by subtracting the minimum PTD 
from the 99.9% percentile of the PTD values 

## 11.2 Microburst Monitoring  *(p.253)*

11. Monitoring and Diagnostics 
Counter 
Description 
Round-trip delay variation (PDV) – 
max 
Maximum round-trip PDV 
 
 To view a summary report in the web interface: 
1. Navigate to generator profile (Configuration > Test > L3SAT > Generator) and click the generator 
name in the table. 
The generator profile configuration screen opens. 
2. In the peer row, click summary report.  
 
 To view a summary report in the CLI:  
MiNID-Generator>config>test>l3sat>generator(1)>peer(11.11.11.3)# show summary-report 
End Points 
Generator Address    : 11.11.11.1 
Responder Address    : 11.11.11.3 
Short Packet Mode    : Enable 
Responder Type       : IP Loop 
Test Rate Mode       : L1 
 
Test 
Scope                : Performance 
Peer Profile Name    : peer_profile 
Start Date & Time    : 00:39:50 01-01-1970 
End Date & Time      : 00:40:53 01-01-1970 
Total Duration       : 1:03 
Overall Result       : Pass 
 
Test Name                BW        DSCP      Performance Result 
                         [Kbps] 
----------------------------------------------------------------- 
MiNID_SA                 4         0         Pass 
 
MiNID-Generator>config>test>l3sat>generator(1)>peer(11.11.11.3)# 
11.2 Microburst Monitoring 
Granular bandwidth utilization and Microburst monitoring is a  Platinum feature available with the 
Platinum installation package. This feature enables you to monitor network traffic, on per-flow or 
11. Monitoring and Diagnostics 
multiple flows basis, and detect unexpected bursts of data in very short time intervals measured in 
microseconds. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Benefits 
Microburst monitoring provides clear indication of traffic and bursts passed, dropped or exceeding 
thresholds based on CIR/CBS and EIR/EBS. In addition, it helps facilitate bandwidth on demand. 
Functional Description 
Similar to OAM services statistics, microbursts statistics are collected for a certain PM interval, while this 
interval is defined from 1 to 900 seconds. 
When a Regular policer profile is used, excess bandwidth is shared or discarded, and the corresponding 
statistics are collected. When a Regular Accounting Only profile is used, only the statistics are collected, 
but the network traffic remains intact. 
Configuring Microburst Monitoring  
 To configure microburst monitoring, perform the following steps: 
1. Configure a policer profile (refer to Policer Profiles). 
2. Configure a flow. 
 To configure a flow with the web interface: 
1. Navigate to Configuration>Physical Ports>Flows> [SFP/ Port 1 | MSA/ Port 2] and click Add 
Flow. 
2. Set the PM collection parameters: 
a. Set PM Collection to Enable. 
11. Monitoring and Diagnostics 
b. Set PM Interval to the desired number of seconds to monitor traffic behavior during the 
interval. 
c. Set Policer type to Regular or Regular Accounting Only. 
3. Click Apply. 
4. Set the rest of the parameters as described in Per-Flow Tasks. 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>Add Flow 
  
 
 
 Flow Name 
 
Flow 1 
 Service Name 
 
Gold 
 Admin Status 
 
Enable 
 Ingress Port 
 
SFP/Port 1 
 L2CP Profile 
 
 
 L3L4 Loop 
 
Disabled 
 PM Collection 
 
Enable 
 PM Interval 
 
1 
 Policer Type 
 
Regular Accounting Only  
 Policer Profile 
 
mburst 
 Classification Tag Mode 
 
Single 
 Min VID Value 
 
0 
 Max VID Value 
 
4095 
 Min P-bit Value 
 
5 
 Max P-bit Value 
 
5 
 Flow Action 
 
Push VLAN 
  
 
 
 Apply 
 
 
  
 
 
Add Flow with PM Collection 
5. Navigate to Monitoring > Physical Port > Ethernet > Port [SFP/ Port 1 | MSA/ Port 2]. Click 
Statistics. 
Port statistics is displayed for the specified PM Interval. 

## 11.3 OAM (CFM)  *(p.256)*

11. Monitoring and Diagnostics 
 To configure a flow with the CLI: 
1. Go to the configure flows context, and enter: 
flow <name>: 
where <name> is the flow name 
The CLI enters the flow context. 
2. Type pm-collection interval <seconds> to enable the mode of collecting PM data and set the 
duration of the collection in seconds. 
3. Type policer regular-accounting-only <profile-name> or policer profile <profile-name> to 
associate the defined profile with the flow.  
4. Type show statistics to display the flow statistics. 
Viewing Flow Statistics 
 To display the flow statistics, do one of the following: 
• 
In the CLI, go to config flows flow <flow-id> and type show statistics. 
MiNID>config>flows>flow(1)# show statistics 
Total Matched Frames                    :       10000 
Total Matched Bytes                     :       64000 
Total Matched In-Service MAC Frames     :       0 
Total Matched In-Service MAC Bytes      :       0 
Total Matched In-Service L3\L4 Frames   :       0 
Total Matched In-Service L3\L4 Bytes    :       0 
Total Matched L2CP Frames               :       0 
Total Matched L2CP Bytes                :       0 
Total Matched Green Bytes               :       50000 
Total Matched Yellow Bytes              :       10000 
Total Matched Red Bytes                 :       4000 
• 
In the web interface, navigate to Monitoring > Physical Port > Classification > Port and click 
Statistics in the corresponding Flow row. 
11.3 OAM (CFM) 
Ethernet Connectivity Fault Management (CFM) is a service-level OAM protocol that provides tools for 
monitoring and troubleshooting end-to-end Ethernet services. This includes proactive connectivity 
monitoring, fault verification, fault isolation, and performance monitoring. CFM uses standard Ethernet 
frames and can be run on any physical media that can transport Ethernet service frames. 
11. Monitoring and Diagnostics 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
IEEE 802.1ag-D8 
ITU-T Y.1731 
Benefits 
OAM functionality ensures that network operators comply with QoS guarantees, detect anomalies 
before they escalate, and isolate and bypass network defects. As a result, operators can offer binding 
service-level agreements. 
Functional Description 
MiNID provides the OAM (CFM) functions listed below in packet-switched networks:  
• 
End-to-end Connectivity Fault Management (CFM) per IEEE 802.1ag: 
 
Continuity check (CC) 
 
Non-intrusive loopback, used to detect loss of bidirectional continuity  
 
Link Trace for fault localization 
• 
End-to-end performance monitoring per ITU-T Y.1731: 
 
Delay measurement 
 
Loss measurement 
 
Unavailability/Availability 
Frames must contain at least one VLAN to be considered as OAM (CFM) frames. You can configure 
maintenance associations to work in the following modes: 
• 
Untagged mode – OAM frames that run without a VLAN.  
• 
Single-tag mode – Only frames with one VLAN are classified as OAM frames.  
• 
Double-inner-tag mode – Only frames with two VLANs (inner and outer) are classified as OAM 
frames. The inner VLAN is used for handling incoming OAM frames 
11. Monitoring and Diagnostics 
• 
Double-outer-tag mode – Only frames with two VLANs (inner and outer) are classified as OAM 
frames. The outer VLAN is used for handling incoming OAM frames. 
OAM Elements 
The Ethernet OAM mechanism is implemented by the following elements: 
• 
Maintenance Domains (MDs) – MDs designate the part of the network for which connectivity 
faults can be managed. Each maintenance domain has a unique MD level that designates the 
scope of its monitoring, from 0–7. 
• 
Maintenance Associations (MAs) – Every MA belongs to a maintenance domain (MD), and 
inherits its level from the MD to which it belongs. An MD can contain up to eight MAs, which 
inherit the MD level and must have unique names. An MA can contain up to two maintenance 
end points (MEPs), one for each port, or one maintenance intermediate point (MIP).  
• 
Maintenance End Points (MEPs) – MEPs are active OAM CFM entities that provide MA 
endpoints. MEPs are identified based on the corresponding MD level, MA name, and MEP ID (is 
unique in the corresponding MA). Additionally, each MEP is associated with multiple remote 
MEPs, a VLAN, and a port (SFP/port 1 or MSA/port 2) through which to transmit frames 
corresponding to the MEP. All OAM frames generated by a particular MEP use the MEP VLAN 
properties (VLAN ID and p-bit information). 
MEPs generate and receive CFM PDUs and track responses, as follows: 
 
Validating received OAM frames. Incoming frames are processed by the MEP if the frame 
VLAN properties match the MEP VLAN properties. 
 
Forwarding OAM frames with MD level higher than the MEP MD level 
 
Discarding OAM frames with a lower MD level then the MEP MD level 
 
Transmitting periodic continuity check messages (CCMs), if CCM transmission is enabled, to 
the configured remote MEP(s)  
 
Performing OAM loopback (LBM): 
 
Transmitting LBM frames when LBM is initiated  
 
Receiving OAM loopback response (LBR) frames corresponding to previously 
transmitted LBMs  
 
Responding to LBM frames with LBR frames. 
 
Performing OAM link trace (LTM): 
 
Transmitting LTM frames when LTM is initiated 
 
Receiving OAM loopback response (LTR) frames corresponding to previously transmitted 
LTMs  
 
Responding to LTM frames with LTR frames. 
 
Performing delay measurement on PM services belonging to the MEP: 
11. Monitoring and Diagnostics 
 
Transmitting delay measurement message (DMM) frames periodically when accordingly 
configured 
 
Receiving delay measurement response (DMR) frames corresponding to previously 
transmitted DMMs 
 
Responding to DMM frames with DMR frames. 
 
Performing loss measurement on PM services belonging to the MEP: 
 
Transmitting loss measurement message (LMM/SLM) frames periodically when 
accordingly configured 
 
Receiving loss measurement response (LMR/SLR)frames corresponding to previously 
transmitted LMMs 
 
Responding to LMM/SLM frames with LMR/SLR frames. 
 
Reporting defects when detected. 
• 
PM Services – Provide loss and delay measurements for the relevant MEP. Up to 32 PM services 
can be created per device; 8 PM services per MEP. 
• 
Destination Network Elements (Dest NEs) –Provide performance monitoring for the relevant 
service 
• 
Maintenance Intermediate Points (MIPs) – Unlike MEPs, MIPs are passive OAM entities that 
respond to OAM frames but do not initiate actions. MIPs are identified based on the 
corresponding MD level and MA name. Additionally, each MIP is associated with a VLAN. All 
OAM frames generated by a particular MIP use the MIP VLAN properties (VLAN ID and p-bit 
information).  
MIPs perform the following: 
 
Validating received LTM and LBM frames. Incoming frames are processed by the MIP if the 
frame VLAN properties match the MIP VLAN properties 
 
Responding to LBMs with LBRs 
 
Responding to LTMs with LTRs, and forwarding the received LTM frames. 
 
Note 
MIPs ignore CCM frames. 
OAM Messages 
The Ethernet service OAM mechanism uses cyclic messages for availability verification, fault detection, 
and performance data collection. The main message types are described in the following sections. 
11. Monitoring and Diagnostics 
Continuity Check Messages (CCMs) 
CCMs are sent periodically (if enabled), in order to detect connectivity loss, referred to as loss of 
continuity (LOC), between each MEP and its remote MEPs in an MA. The CCM functionality also allows 
detection of unintended connectivity. The CCM interval is user-configurable at the MA level to 100 ms, 
1 sec, 1 min, or 10 min. 
If an error is detected by the MEP, CCM frames are transmitted to the appropriate remote MEP with the 
RDI bit set. When the MEP receives notification that the error was cleared, it clears the RDI bit. 
CCMs are transmitted as unicast or multicast: 
• 
Unicast – CCMs are transmitted to a configurable MAC address 
• 
Multicast – CCMs are transmitted to the MAC address corresponding to the MEP MD level, as 
shown below. 
Multicast MAC Address 
01-80-C2-00-00-3y 
MD Level 
Four Address Bits “y” 
7 
7 
6 
6 
5 
5 
4 
4 
3 
3 
2 
2 
1 
1 
0 
0 
Alarm Indication Signal (AIS) 
If a MEP detects a connectivity failure, it propagates AIS frames in the direction away from the detected 
failure, with the level set to the client MD level configured for the MEP (the default client MD level is the 
MEP MD level incremented by 1). The AIS is sent for the following trigger events: 
• 
LOS signal from network side (the MEP stops transmitting AIS frames when it receives indication 
that the defect is cleared) 
11. Monitoring and Diagnostics 
• 
LOC detected (the MEP stops transmitting AIS frames when it receives indication that the defect 
is cleared) 
• 
CCM received with Interface Status TLV with status set to down (the MEP stops transmitting AIS 
frames when it receives indication that the defect is cleared) 
• 
AIS received (the MEP stops transmitting AIS frames when no AIS frames are received within an 
interval of 3.5 seconds).  
AIS frames are transmitted periodically at 1-second intervals. The frames are multicast AIS frames with 
VLAN parameters (VLAN ID, priority) as configured in the MA. 
 
Note 
• 
AIS transmittal can be enabled or disabled per MEP. If disabled, the MEP 
does not transmit AIS frames and ignores any received AIS frames. 
• 
If the MEP MD level is 7 (the highest MD level) it does not transmit AIS 
frames. 
• 
MIPs do not transmit AIS frames. 
When the original defect is cleared, the MEP clears the AIS defect condition. 
Loopback Messages (LBMs) 
The OAM loopback functionality (ETH-LB) is used to verify the bidirectional connectivity of a MEP with a 
MIP or remote MEP, and is initiated upon user request. The OAM loopback is a ping-like request/reply 
function, where an LBM is sent by a MEP to a MIP or remote MEP, and a loopback response (LBR) is 
expected in response to the LBM.  
LBM transmission mode is one of the following: 
• 
Multicast – One LBMs is transmitted to the MAC address corresponding to the MEP MD level, as 
shown in the table in Continuity Check Messages (CCMs). 
• 
Unicast – LBMs are transmitted to a user-configurable MAC address 
• 
Remote MEP –MEP LBMs are transmitted in unicast mode to the remote MEP MAC address. 
LBM supports user-configurable data TLV length to provide the capability of testing the loopback with 
different frame sizes, with a data pattern of all zeros.   
Note 
An LBM session cannot be started if one is already in progress. 
LBMs are sent at the rate of approximately 40 frames per second. LBRs are expected to arrive within 
5 seconds after the last LBM frame transmitted. If an LBR frame arrives after this time interval, it is 
considered as invalid and is discarded. LBMs are sent with transaction identifiers that must match the 
received LBRs, therefore the MEP also detects and reports out-of-order LBRs. 
11. Monitoring and Diagnostics 
When a MEP/MIP receives an LBM, it replies with an LBR if the LBM is valid. The LBM is considered valid 
if the following are true: 
• 
The LBM MD level is equal to the MEP/MIP MD level 
• 
According to the frame transmission mode of multicast or unicast: 
 
Unicast –The LBM MAC address is equal to the MEP/MIP MAC address  
 
Multicast – The LBM MAC address is equal to the multicast MAC address corresponding to 
the MEP/MIP MD level (see the table in Continuity Check Messages (CCMs)). 
Note 
In addition to LBM/LBR sent and replied to by MEPs,  has an LBM reflector 
feature that enables replying with LBR to any LBM packet received with any 
VLAN and any MD level, per port SFP/port 1 or MSA/port 2. See Configuring 
LBM Reflector in Chapter 8. 
Link Trace Messages (LTMs) 
The Ethernet Link Trace function (ETH-LT) traces the path to a target MEP/MIP by retrieving adjacency 
relationships between a MEP and a MIP or remote MEP, therefore it can be used for fault localization, as 
the retrieved sequence of MIPs/MEPs is likely to be different if a fault exists. The ETH-LT function is 
initiated upon user request. 
The result of running an ETH-LT is a sequence of MIPs/MEPs from the source MEP to the target 
MIP/MEP. Each MIP /MEP is identified by its MAC address. 
When ETH-LT is initiated, the MEP sends a multicast LTM frame containing the TTL value, and the target 
device MAC address that terminates the link trace. The LTM frame is sent to the multicast MAC address 
corresponding to the MEP MD level (see the table in Continuity Check Messages (CCMs)). 
When a MEP/MIP receives an LTR, it verifies if the transaction identifier value is expected by the 
receiving MEP/MIP. If the LTR frame contains an unknown transaction identifier, it is considered as 
invalid and is discarded. LTRs are expected to arrive within 5 seconds after the last LTM frame 
transmitted. If an LTR frame arrives after this time interval, it is considered as invalid and is discarded. 
When a MEP/MIP receives an LTM, it generates a unicast LTR to the initiating MEP if the LTR is valid. It 
also forwards the LTM to the target destination MAC address, if it is not the target. When the frame is 
forwarded, the TTL is decremented by 1. The LTM is considered valid if the following are true: 
• 
The LTM MD level is equal to the MEP/MIP MD level 
• 
The LTM TTL is greater than 0 
11. Monitoring and Diagnostics 
Performance Monitoring 
PM services provide loss and two-way delay measurements for MEPs, based on ITU-T Y.1731. The 
measurements are between the corresponding local MEP and its configured remote MEP. Performance 
monitoring frames are unicast frames sent periodically to the remote MEP MAC address, at 
user-configurable intervals (100 ms, 1 sec, or 10 sec). 
The following performance parameters are measured: 
• 
Loss measurement (LM): 
 
Frame Loss Ratio (FLR) –Number of service frames not delivered, divided by the number of 
service frames received.  supports two synthetic loss measurement methods and a real 
traffic loss measurement method: 
 
SLM Synthetic – Synthetic SLM/SLR frames are used to calculate the loss ratio  
 
LMM Synthetic – Synthetic LMM/LMR frames are used to calculate the loss ratio 
 
User Data – Real traffic LMM/LMR frames with OAM type CCM, APS, or CSF are used to 
calculate the loss ratio. With this method, you can configure whether to count green, 
yellow, or both green and yellow frames, according to the frame DEI bit. 
• 
Delay measurement (DM): 
 
Frame Delay (FD) –Round trip delay for a frame, defined as the time elapsed since the start 
of transmission of the first bit of the frame by a source node, until the reception of the last 
bit of the loopbacked frame by the same source node, when the loopback is performed at 
the frame’s destination node 
 
Frame Delay Variation (FDV) –Difference between two subsequent frame delay 
measurements. 
When a MEP receives an LM or DM frame, it is considered valid if it has a valid MD level, and destination 
MAC address equal to the receiving MEP. If valid, the MEP responds with an LMR/SLR or DMR frame. 
When a MEP receives an LMR/SLR or DMR frame, it calculates the loss or delay measurements. 
 
Note 
Loss measurement and delay measurement can be enabled or disabled per 
PM service. 
Capacity 
OAM frame size is 64–2048 bytes.  
MiNID supports the following per device: 
• 
Up to eight MDs 
11. Monitoring and Diagnostics 
• 
Up to 32 MAs 
• 
Up to 32 MEPs or MIPs (one MIP per MA) 
• 
Up to 32 remote MEPs 
• 
Up to 32 PM services 
• 
Up to 32 destination NEs (up to 32 destination NEs per PM service) 
• 
Up to 32 simultaneous LM or DM sessions. 
Factory Defaults 
By default, there are no configured OAM CFM entities. 
Configuring OAM (CFM/PM)  
The Ethernet OAM (CFM) configuration procedure includes the following steps, detailed in this section: 
1. Configure a Maintenance Domain (MD). 
2. Configure Maintenance Associations (MA). 
3. For each Maintenance Association, configure a MIP or configure MEPs. 
4. For each MEP, configure remote MEPs. 
5. For each MEP, configure PM services. 
6. For each PM service, configure destination NEs. 
Configuring MDs 
The following parameters are configured in the MD. 
MD Parameters 
Parameter 
Description 
Web 
CLI 
MD Index 
<md index> 
 
11. Monitoring and Diagnostics 
Parameter 
Description 
Web 
CLI 
MD level 
<mdid> 
Maintenance domain level of MD 
to which MA belongs; used as 
maintenance domain index in the 
CLI 
MD name 
format 
<string|mac-
and-uint|dns>  
Maintenance domain name format: 
• String-Alphanumerical value 
• DNS 
• MAC and UINT 
• No MD Name Present 
MD name 
<name> 
Maintenance domain name 
 To add an MD in the web interface: 
1. Navigate to Configuration>OAM>CFM\PM. 
2. Select Legacy or SOAM Alarm type. 
3. Click Add New MD. 
4. Fill in the parameters specified in the table above. 
5. Click <Apply>. 
A message is displayed that the MD was successfully created. 
 To configure the MD in the web interface: 
1. Navigate to Configuration>OAM>CFM\PM. 
2. Click config in the MD index 
A new MA can be created in this screen. 
 To add an MD in the CLI: 
• 
Navigate to configure>oam cfm and configure the parameters listed in the table above. 
MiNID# configure oam cfm maintenance-domain 1 
MiNID>config>oam>cfm.md<1># md-level 1 
MiNID>config>oam>cfm.md<1># name string one 
11. Monitoring and Diagnostics 
Configuring MAs 
The following parameters are configured in MAs. 
MA Parameters 
Parameter 
Description 
Web 
CLI 
[Not visible] 
<maid> 
Maintenance association index (1–8); must be unique in the device. 
When an MA is created via the Web, the MA index is automatically 
generated by MiNID. 
MA Name 
name 
Maintenance association name, according to MA name format; 
must be unique in the corresponding MD 
MA Format 
format 
MA name format: 
• Character string – Alphanumeric value (up to 43 characters) 
• 2-octet integer – Unsigned integer decimal number (0–65535) 
• ICC based –Name is specified as the ITU carrier code that is 
assigned to the relevant network operator/service provider. The 
codes are maintained by ITU-T as defined in ITU-T Rec. M.1400 
Vlan Tag 
Mode 
tag-mode 
Indicates whether MA works in single-tag mode, double-tag mode 
with inner VLAN used to handle incoming OAM frames, double-tag 
mode with outer VLAN used to handle incoming OAM frames or 
untagged mode 
CCM Interval 
ccm-interval 
Specifies the interval for periodic transmission of CCMs (see 
Continuity Check Messages (CCMs)). Allowed values are: 
• 100ms 
• 1s 
• 10s 
• 1min 
• 10min 
Interface 
Status TLV 
interface-status-tlv 
Allowed values are: 
• Disable 
• Enable 
 To add an MA in the web interface: 
1. Navigate to Configuration > OAM > CFM\PM. 
  
11. Monitoring and Diagnostics 
MiNID 
 
 
 
 
 
 
  
 
Configuration>OAM>CFM\PM>Config MD (index) 
 
 
 
 
 
 
 
 
Add new MA 
 
 
 
 
 
MA Number 
MA Name 
MD Level 
Vlan Tag Mode 
Service Name 
 
 
 
 
1 
MA1 
3 
Single 
Gold 
remove 
config 
 
 
2 
MA2 
3 
Double-Inner 
Silver 
remove 
config 
 
 
3 
MA3 
2 
Double-Outer 
Gold 
remove 
config 
 
 
4 
MA4 
1 
Double-Inner 
Silver 
remove 
config 
 
 
5 
MA5 
4 
Single 
Gold 
remove 
config 
 
 
6 
MA6 
3 
Untagged 
Gold 
remove 
config 
 
 
 
 
 
Configuring OAM (CFM) 
2. Click Add new MA. 
MiNID 
  
 
 
 Configuration>OAM>CFM\PM>Add MA (MD index) 
  
 
 MA Number 
3 
 
 MA Name 
MA6 
 
 MA Format 
Character String 
 
 Vlan Tag Mode 
Single 
 
 CCM Interval 
1s 
 
 Interface Status 
TLV 
Disable 
 
  
 
 
 Apply 
 
 
  
 
 
New MA 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Configuration>OAM>CFM\PM>Add MA (MD index) 
  
 
 MA Number 
3 
 
 MA Name 
MA6 
 
 MA Format 
Character String 
 
 Vlan Tag Mode 
Double-Inner 
 
 CCM Interval 
1s 
 
 Interface Status 
TLV 
Disable 
 
  
 
 
 Apply 
 
 
  
 
 
New MA After Changing VLAN Tag Mode to Double-Inner 
1. Fill in the parameters as specified in the MA Parameters table. 
2. Click <Apply> to create the MA. 
A message is displayed that the MA was successfully created. 
3. Click <OK> to close the message. 
4. Click <Save Configuration>. 
 To configure a maintenance association in the web interface: 
1. Navigate to Configuration>OAM>CFM. 
2. Click config in the relevant MD row. 
3. Click the MA name. 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Configuration>OAM>CFM 
  
 
 MA Name 
 
MA4 
 MA Format 
 
Character String 
 Vlan Tag Mode 
 
Single 
 CCM Interval 
 
1s 
 Interface Status TLV 
 
Disable 
  
 
 
Updating MA Parameters – Single Tag Mode 
MiNID 
 
 
 
 
 
Configuration>OAM>CFM 
 
 
 
 
MA Name 
 
MA5 
 
MA Format 
 
Character String 
 
Vlan Tag Mode 
 
Double-Inner 
 
CCM Interval 
 
1s 
 
Interface Status TLV 
 
Disable 
 
 
 
 
Updating MA Parameters – Double Tag Mode 
4. Edit the parameters as specified in the MA Parameters table. 
Note 
You can change Vlan Tag Mode only if there are no MEPs in the MA. 
5. Click <Apply> to apply your changes, and then click <Save Configuration>. 
Maintenance associations can be configured with VLAN “untagged” mode. Only one MA under an MD 
can be configured as “untagged”, and only two MEPs can be configured per untagged MA (one per port). 
 To configure an MA with VLAN untagged mode (web interface): 
1. Navigate to Configuration > OAM > CFM. 
2. Click the MA name. 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Configuration>OAM>CFM 
  
 
 MD Level 
 
2 
 MA Name 
 
MA4 
 Vlan Tag Mode 
 
Untagged 
 Service Name 
 
Gold 
 
  
 
 
3. Edit the parameters as specified in the MA Parameters table. 
 To delete a maintenance association (web interface): 
1. Navigate to Configuration>OAM>CFM. 
2. In the row corresponding to the MA, click remove. 
You are prompted for confirmation. 
3. Click <Yes> to delete the MA. 
 
Note 
• 
Before creating a maintenance association, use info at the configure oam 
cfm level to display all configured OAM CFM entries, in order to find an 
unused MA index 
• 
If you want to configure an MA that you created via the web interface, 
you need to navigate to the corresponding maintenance domain CLI level 
and use info in order to find the MA ID, as the web interface shows the 
MA name but does not show its index. 
 
 To add or configure a maintenance association (with the CLI): 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid>, 
where <maid> is an unused MA ID if you are creating an MA. 
The config>oam>cfm>md(<mdid>)>ma(<maid>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Specifying the interval 
between continuity 
check messages 
ccm-interval { 100ms | 1s | 
10s | 1min | 10min} 
 
Configuring MEP for 
the MA 
mep <mepid> 
See Configuring MEPs 
Configuring MIP for the 
MA 
mip <mipid> 
See Configuring MIPs 
Specifying the name 
and name format of the 
maintenance 
association 
name <ma-name> format { 
icc | uint | string} 
<ma-name> – MA name, according to the 
specified format: 
• Format string – Specify <ma-name> as an 
alphanumeric string 
• Format uint – Specify <ma-name> as an 
unsigned integer decimal number (0–
65535) 
• Format icc – Specify <ma-name> as the 
ITU carrier code that is assigned to the 
relevant network operator/service 
provider. The codes are maintained by 
ITU-T as defined in ITU-T Rec. M.1400. 
Assigning service name 
to the MA 
service-name 
<service-name> 
 
Specifying whether MA 
works in single, double 
tag mode or untagged 
mode  
tag-mode {single-vlan | 
double-inner-vlan | 
double-outer-vlan 
|untagged } 
single-vlan – MA works in single-tag mode 
double-inner-vlan – MA works in double-tag 
mode and uses inner VLAN to handle 
incoming OAM frames 
double-outer-vlan – MA works in double-tag 
mode and uses outer VLAN to handle 
incoming OAM frames 
untagged- MA works in an untagged mode 
Enabling or disabling 
Interface Status Tlv 
[no] interface-status-tlv 
Allowed values: 
• Enable 
• Disable 
11. Monitoring and Diagnostics 
 To delete a maintenance association (CLI): 
• 
At the config>oam>cfm>md(<mdid>)# prompt enter: 
no maintenance-association <maid> 
The maintenance association is deleted. 
Configuring MEPs 
Maintenance endpoints (MEPs) reside at the edge of a maintenance domain. They initiate and respond 
to CCMs, linktrace requests, and loopbacks to detect, localize, and diagnose connectivity problems.  
Up to 32 MEPs can be created in an MA, as long as a MIP has not been created in the MA. The following 
parameters are configured in MEPs. 
MEP Parameters 
Parameter 
Description 
Web 
CLI 
MEP Enable 
[no] shutdown 
Administratively enables or disable the MEP 
MEP ID   
<mepid> 
MEP identification (1–8191); must be unique in the MA 
Remote MEP 
ID 
remote-mep 
Remote MEP identification (1–8191) ; must be unique in the MA. 
Multiple remote MEP IDs can be configured. OAM messages such as 
CCM, LBM, LTM, etc. are sent to all remote MEPs 
Ingress Port 
bind 
Port for transmitting and receiving frames: 
• SFP/Port 1 
• MSA/Port 2 
Inner Vlan Id 
vlan 
Inner VLAN ID (0–4095) assigned to MEP; must be unique in the 
MEP 
Note: Appears in Web menu only if VLAN tag mode is double-inner 
or double-outer 
Inner Priority 
priority 
Inner VLAN P-bit (0–7) assigned to MEP 
Note: Appears in Web menu only if VLAN tag mode is double-inner 
or double-outer  
Outer Vlan Id 
outer-vlan 
Outer VLAN ID (0–4095) assigned to MEP; must be unique in the 
MEP 
Note: Appears in Web menu only if VLAN tag mode is double-inner 
or double-outer 
11. Monitoring and Diagnostics 
Parameter 
Description 
Web 
CLI 
Outer Priority 
outer-priority 
Outer VLAN P-bit (0–7) assigned to MEP 
Note: Appears in Web menu only if VLAN tag mode is double-inner 
or double-outer 
Vlan Id  
vlan 
VLAN ID (0–4095) assigned to MEP; must be unique in the MEP 
Note: Appears in Web menu only if VLAN tag mode is single 
Priority 
priority 
P-bit (0–7) assigned to MEP  
Note: Appears in Web menu only if VLAN tag mode is single 
Service Name 
service-name 
Service name associated with MA, to enable network management 
systems to locate entities related to specific services 
CCM Enable 
ccm-initiate 
Enables or disables transmission of CCMs (see Continuity Check 
Messages (CCMs)) to any configured remote MEPs 
CCM 
Transmission 
Mode 
dest-addr-type 
CCMs are transmitted as unicast or multicast frames: 
• Unicast – CCMs are transmitted to the MAC address specified by 
Remote MEP MAC Address. In this mode, only one remote MEP 
can be configured for the MEP. 
• Multicast – CCMs are transmitted to the MAC address 
corresponding to the MEP MD level, as shown in the Multicast 
MAC Address table. In this mode, multiple remote MEPs can be 
configured for the MEP. 
Remote MEP 
MAC Address 
dest-mac-addr 
Specifies the MAC address to which to send unicast CCMs 
Note: Appears in Web interface/available in the CLI only if CCM 
transmission mode is set to unicast. 
AIS Enable 
ais 
Enable or disable transmission of AIS frames (see Alarm Indication 
Signal (AIS)) 
Client MD 
Level 
client-md-level 
Transmitted in AIS frames (default client MD level is the MD level 
corresponding to the MEP, incremented by 1) 
 To add a MEP with the web interface: 
1. Navigate to Configuration>OAM>CFM\PM. 
2. In the row corresponding to the MD for which to add the MEP, click config. 
3. In the row corresponding to the MA for which to add the MEP, click config. 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 
 Configuration>OAM>CFM\PM>Config MA (ID: MA1) 
  
 
 
 
 
Add new MEP 
 
 
 
 
Add new MIP 
 
 
 
 
 
 
 
 
 
MEP/MIP 
 
 
 
 
MEP (ID: 16) 
Remove  
Config MEP 
 
  
 
 
 
Configuring MA 
4. Click Add new MEP. 
MiNID 
  
 
 
 Configuration>OAM>CFM\PM>Config MA>Add MEP (MA MA1) 
  
 
 
Admin Status 
 
Disable 
 
MEP ID [1..8191] 
 
1 
 
Ingress Port 
 
SFP/Port 1 
 
Vlan Id [1..4094]  
 
1 
 
Classification Priority 
 
0 
 
Tag-Ether-Type 
 
0x8100 
 
 
 
 
 
CCM 
 
Disable 
 
CCM Priority 
 
0 
 
CCM Transmission Mode 
 
Multicast 
 
Client MD Level 
 
5 
 
AIS  
 
Disable 
 
 
 
 
New MEP for Single Tag OAM 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Configuration>OAM>CFM\PM>Config MA>Add MEP (MA MA1) 
  
 
 Admin Status 
 
Disable 
 MEP ID [1..8191] 
 
1 
 Ingress Port 
 
SFP/Port 1 
 Inner Vlan Id [1..4094]  
 
1 
 Classification Inner 
Priority 
 
Any 
 Tag-Ether-Type Inner 
 
0x8100 
 Outer Vlan Id [1..4094]  
 
1 
 Outer Priority 
 
0 
 Tag-Ether-Type Outer 
 
0x88A8 
  
 
 
 CCM 
 
Disable 
 CCM Priority 
 
0 
 CCM Transmission Mode 
 
Multicast 
 Client MD Level 
 
6 
 AIS  
 
Disable 
  
 
 
New MEP for Double Tag OAM 
5. Fill in the parameters as specified in the MEP Parameters table. 
6. Click <Apply> to create the MEP. 
A message is displayed that the MEP was successfully created. 
7. Click <OK> to close the message. 
8. Click <Save Configuration>. 
 To configure MEP parameters in the web interface: 
1. Navigate to Configuration>OAM>CFM. 
2. In the row corresponding to the MD to which the MEP belongs, click config to display the 
Configuration>OAM>CFM>Config MA screen. 
11. Monitoring and Diagnostics 
3. In the row corresponding to the MA to which the MEP belongs, click config to display the 
Configuration>OAM>CFM>Config MEP screen. 
4. In the row corresponding to the MEP, click the MEP name. 
MiNID 
  
 
 
 Configuration>OAM>CFM\PM>Config MA>Update MEP (MA MA6)  
  
 
 Admin Status 
 
Disable 
 MEP ID [1..8191] 
 
2 
 Vlan Id [1..4095] 
 
1 
 Priority 
 
0 
 Ingress Port 
 
MSA/Port 2 
 CCM Enable 
 
Enable 
 CCM Transmission 
Mode 
 
Multicast 
 Client MD Level 
 
5 
 AIS Enable 
 
Enable 
  
 
 
Updating MEP Parameters 
5. Edit the parameters as specified in the MEP Parameters table. 
6. Click <Apply> to apply your changes, and then click <Save Configuration>. 
 To add remote MEP IDs for the MEP (web): 
 
Note 
You can add remote MEPs only if the MEP is administratively enabled. 
 
1. Navigate to Configuration>OAM>CFM. 
2. In the row corresponding to the MA to which the MEP belongs for which you wish to add the 
service, click config to display the Configuration>OAM>CFM>Config MA screen. 
3. In the row corresponding to the MEP, click Config MEP to display the 
Configuration>OAM>CFM>Config MEP screen. 
4. Click Add Remote MEP. 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Configuration>OAM>CFM  
  
 
 Remote MEP ID 
[1..8191] 
 
1 
  
 
 
Adding Remote MEP 
5. Fill in the remote MEP ID. 
6. Click <Apply> to save the remote MEP ID. 
7. Repeat the above steps to add more remote MEP IDs if necessary. 
8. Click <Save Configuration>. 
 To delete remote MEPs (web): 
1. Navigate to Configuration>OAM>CFM. 
2. In the row corresponding to the MA to which the MEP belongs for which you wish to add the 
service, click config to display the Configuration>OAM>CFM>Config MA screen. 
3. In the row corresponding to the MEP, click Config MEP to display the 
Configuration>OAM>CFM>Config MEP screen. 
4. Click Remove in the row corresponding to the remote MEP that you wish to remove. 
The remote MEP ID is removed from the MEP configuration. 
5. Click <Save Configuration>. 
 To delete a MEP (web): 
1. Navigate to Configuration>OAM>CFM. 
2. In the row corresponding to the MA to which the MEP belongs, click config to display the 
Configuration>OAM>CFM>Config MA screen.  
3. In the row corresponding to the MEP, click Remove. 
You are prompted for confirmation. 
4. Click <Yes> to delete the MEP. 
5. Click <Save Configuration>. 
11. Monitoring and Diagnostics 
 To add or configure a maintenance endpoint (with the CLI): 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid>, where <mepid> is 1–8191. 
The prompt config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Enabling AIS 
transmission 
ais  
To disable AIS transmission, enter no ais 
Binding the MEP to an 
Ethernet port 
bind ingress-port {sfp/1 | 
msa/2} 
To unbind the MEP, enter no bind 
Enabling CCM 
transmission 
ccm-initiate  
To disable CCM transmission, enter 
no ccm-initiate 
Defining the MD level 
transmitted in AIS 
frames  
client-md-level 
Default client MD level is the MD level 
corresponding to the MEP, incremented by 1 
Defining the MAC 
address type sent in 
CCMs 
dest-addr-type ccm {unicast 
| multicast} 
• Unicast – CCMs are transmitted to the 
MAC address specified by Remote MEP 
MAC Address 
• Multicast – CCMs are transmitted to the 
MAC address corresponding to the MEP 
MD level, as shown in the Multicast MAC 
Address table. 
Defining a unicast MAC 
address if you defined 
unicast MAC address 
type for CCM messages 
via the dest-addr-type 
command 
dest-mac-addr <mac-addr> 
MAC address is in format xx-xx-xx-xx-xx-xx 
Initiating OAM 
loopback 
lbm 
See Performing OAM Loopback  
Initiating OAM linktrace 
linktrace 
See Performing OAM Link Trace 
Specifying inner VLAN 
or single VLAN p-bit 
assigned to MEP  
priority 
Allowed values: 0–7 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining remote MEP(s) 
with which the MEP 
communicates 
remote-mep 
<remote-mep-id> 
Allowed range for remote MEP ID(s) is:  
1–8191 
Type no remote-mep <remote-mep-id> to 
delete a remote MEP ID 
Configuring service for 
the MEP 
service <serviceid> 
See Configuring PM Services  
Displaying MEP status 
show status 
 
Administratively 
enabling MEP 
no shutdown 
To deactivate the MEP, enter shutdown 
Associating the MEP 
with a single/double 
tagged VLAN 
vlan <vlan-id>[p-bit <p-bit>] 
[tag-ether-type <ether-
tag>] 
vlan <vlan-id>[p-bit <p-bit>] 
[tag-ether-type <ether-
tag>] [inner-vlan <inner-
vlan> [p-bit <p-bit>][inner-
tag-ether-type <inner-
ether-tag>]] 
For single-tagged VLAN 
 
For double-tagged VLAN 
Allowed values for VLAN ID: 1–4094 
 To delete a maintenance endpoint (CLI): 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)# prompt, enter: 
no mep <mepid> 
The maintenance endpoint is deleted. 
Configuring MIPs 
Maintenance intermediate points reside in the middle of maintenance associations. They respond to 
linktrace requests and loopbacks; they do not initiate messages.  
One MIP can be created in an MA, as long as no MEPs have been created in the MA.  
 To add and configure a MIP in the web interface: 
1. Navigate to Configuration > OAM > CFM. 
2. In the row corresponding to the MA for which to add the MIP, click config to display the 
Configuration > OAM > CFM > Config MA screen. 
11. Monitoring and Diagnostics 
3. Click Add new MIP. 
MiNID 
  
 
 
 Configuration>OAM>CFM\PM> Config MA>Add MIP (MA MA1)  
  
 
 
 Admin Status 
 
Disable 
 Vlan ID 
(1…4094) 
 
1 
 Priority 
 
0 
 Tag-Ether-Type 
 
0x8100 
  
 
 
New MIP for Single-Tag VLAN 
MiNID 
  
 
 
 Configuration>OAM>CFM\PM> Config MA>Add MIP (MA MA3)  
  
 
 
 Admin Status 
 
Disable 
 Inner Vlan ID 
(1…4094) 
 
1 
 Inner Priority 
 
0 
 Tag-Ether-Type Inner 
 
0x8100 
 Outer Vlan ID 
(1…4094) 
 
1 
 Outer Priority 
 
0 
 Tag-Ether-Type Outer 
 
0x88A8 
  
 
 
 Apply 
 
 
  
 
 
New MIP for Double-Tag VLAN 
4. Set Admin Status to enable or disable the MIP. 
5. Type in the VLAN ID and priority in the corresponding fields.  
6. Click <Apply> to create the MIP. 
A message is displayed that the MIP was successfully created. 
11. Monitoring and Diagnostics 
7. Click <OK> to close the message. 
8. Click <Save Configuration>. 
 To delete a MIP in the web interface: 
1. Navigate to Configuration>OAM>CFM. 
2. In the row corresponding to the MA to which the MIP belongs, click config to display the 
Configuration>OAM>CFM>Config MA screen. 
3. Click Remove. 
You are prompted for confirmation. 
4. Click <Yes> to delete the MIP. 
 To add or configure a MIP in the CLI: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mip. 
The config>oam>cfm>md(<mdid>)>ma(<maid>)>mip# prompt is displayed. 
2. Enter no shutdown to administratively enable the MIP, or shutdown to administratively disable 
the MIP. 
 To delete a MIP in the CLI: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)# prompt enter:  
no mip <mipid> 
The MIP is deleted. 
Configuring PM Services 
Services define delay and delay variation thresholds. If the thresholds are exceeded, the service is 
declared as degraded. You can also define priority of OAM messages originating from this service. 
You can configure up to 32 services on a MEP, corresponding to each p-bit (32 services are supported for 
the entire  device). If a MEP is administratively disabled, its services are also disabled. If a MEP is 
deleted, its services are also deleted. 
The following parameters are configured in PM services.  
11. Monitoring and Diagnostics 
PM Service Parameters 
Parameter 
Description 
Web 
CLI 
Admin Status 
[no] shutdown 
Administratively enables or disables the service. Loss/delay 
measurement is performed only if the service is enabled. 
Service Priority   
priority 
P-bit assigned to service (0–7) 
Loss Threshold 
loss-threshold 
If loss measurement rises above this threshold, corresponding 
event and trap are sent; if it falls below the threshold, 
corresponding event and trap are sent 
Allowed range: 1–40 [%] 
DEI Bit Color 
loss-dei-bit-color 
If loss measurement is set to User Data, you can filter packets 
according to the DEI (Drop Eligible Indicator) bit: 
• Both – Use green and yellow packets for loss measurement 
• Green – Use only green packets for loss measurement 
• Yellow – Use only yellow packets for loss measurement 
Delay Threshold    delay-threshold 
If frame delay measurement rises above this threshold, 
corresponding event and trap are sent; if it falls below the 
threshold, corresponding event and trap are sent 
Allowed range: 1–5000000 [µs] 
Delay Var 
Threshold 
delay-var-threshold 
If frame delay variation measurement rises above this 
threshold, corresponding event and trap are sent; if it falls 
below the threshold, corresponding event and trap are sent 
Allowed range: 1–5000000 [µs] 
Service Lmm 
Interval 
lmm-interval 
Service interval for loss measurement messages 
Service Dmm 
Interval 
dmm-interval 
Service interval for delay measurement messages transmission 
of DM frames 
 To add PM services in the web interface: 
Note 
You can add PM services only if the corresponding MEP is administratively 
enabled. 
1. Navigate to Configuration > OAM > CFM\PM. 
2. In the row corresponding to the MA to which the MEP belongs for which you wish to add the 
service, click config to display the Configuration > OAM > CFM\PM>Config MA screen. 
3. In the row corresponding to the MEP, click Config MEP. 
11. Monitoring and Diagnostics 
MiNID 
 
 
 
 
 
 
Configuration>OAM>CFM\PM>Config MA>Config MEP (ID: 1 on MA MA 6) 
 
 
 
 
 
 
Add Remote MEP 
 
 
 
 
Start Loopback Session 
 
 
 
 
Start Linktrace Session 
 
 
 
 
Add PM Service 
 
 
 
 
 
 
 
 
 
Service (P-bit: 1) 
Configure 
Remove 
 
 
 
 
 
 
 
Remote MEP (ID:8) 
 
Remove 
 
 
 
 
 
 
Configuring MEP 
4. Click Add PM Service. 
MiNID 
 
 
 
 
 
Configuration>OAM>CFM>Config MA>PM Service 
 
 
 
 
Admin Status 
 
Disable 
 
Service Priority 
 
0 
 
Loss Threshold ([1..40]%) 
 
1 
 
DEI Bit Color 
 
Both 
 
Delay Threshold ([1..4000000]µs) 
 
1000 
 
Delay Var Threshold ([1..4000000]µs) 
 
1000 
 
Service Lmm Interval 
 
100 ms 
 
Service Dmm Interval 
 
100 ms 
 
 
 
 
PM Service 
5. Fill in the parameters as specified in the PM Service Parameters tablei. 
6. Click <Apply> to create the PM service, and then click <Save Configuration>. 
11. Monitoring and Diagnostics 
 To configure PM service parameters in the web interface: 
1. Navigate to Configuration>OAM>CFM. 
2. In the row corresponding to the MA to which the MEP belongs for which you wish to configure 
the service, click config to display the Configuration>OAM>CFM\PM>Config MA screen. 
3. In the row corresponding to the MEP, click Config MEP to display the 
Configuration>OAM>CFM>Config MEP screen. 
4. In the row corresponding to the service, click the service name to display the 
Configuration>OAM>CFM>PM Service screen. 
5. Edit the parameters as specified in. 
6. Click <Apply> to apply your changes, and then click <Save Configuration>. 
 To delete a PM service (web): 
1. Navigate to Configuration > OAM > CFM. 
2. In the row corresponding to the MA to which the MEP belongs for which you wish to delete the 
service, click config to display the Configuration>OAM>CFM>Config MA screen. 
3. In the row corresponding to the MEP, click Config MEP to display the 
Configuration>OAM>CFM>Config MEP screen. 
4. In the row corresponding to the service, click Remove. 
The service is deleted. 
 To add or configure a MEP service in the CLI: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintena?nce-association 
<maid> mep <mepid> service <serviceid>, where <serviceid> is 1–8. 
The prompt config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service(<serviceid>)# 
is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Clearing statistics 
clear-statistics 
 
Specifying delay threshold 
in microseconds   
delay-threshold 
<delay-thresh> 
Allowed range: 
1–5,000,000  
Specifying delay variation 
threshold in microseconds  
delay-var-threshold 
<delay-var-thresh> 
Allowed range: 
1–5,000,000 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Specifying the interval for 
delay measurement 
messages 
dmm-interval {100ms | 1s | 
10s} 
 
Specifying the interval for 
loss measurement 
messages 
lmm-interval {100ms | 1s | 
10s} 
 
Specifying packet filtering 
according to DEI if loss 
measurement is set to 
user-data 
loss-dei-bit-color {both | 
green | yellow} 
• both – Use green and yellow packets 
for loss measurement 
• green – Use only green packets for 
loss measurement 
• yellow – Use only yellow packets for 
loss measurement 
Specifying loss threshold  
loss-threshold 
<loss-threshold> 
Allowed range (1-40); Entered value is 
used as percentage for threshold 
Associating this service with 
a priority  
priority <p-bit> 
The allowed range is 0–7 
Note: Only one service can be defined on 
each p-bit. 
Activating the service 
no shutdown 
To disable the service, enter shutdown 
You can activate a service only if the 
corresponding MEP is active  
 To delete a PM service in the CLI: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, enter: 
no service <mepid> 
The PM service is deleted. 
Configuring Destination NEs 
You can define multiple destination NEs for a PM service, to enable separation between the different 
remote MEPs that are defined for the MEP. Independent loss measurement and delay measurement can 
be configured for each destination NE.  
 
Note 
If the destination NE loss measurement method is user data, then only one 
destination NE can be configured for the PM service. 
11. Monitoring and Diagnostics 
The following parameters are configured in destination NEs.  
Destination NE Parameters 
Parameter 
Description 
Web 
CLI 
Dest NE ID 
dest-ne 
ID assigned to destination NE. This is automatically set by 
the Web interface to 1 for the first destination NE, and 
then incremented for each subsequent destination NE. 
Admin Status 
[no] shutdown 
Administratively enables or disables the destination NE. 
Loss/delay measurement is performed only if the 
destination NE is enabled. 
Remote MEP ID 
remote-mep 
Remote MEP ID to use for the loss and delay 
measurement; this can be set only to a remote MEP ID that 
is associated with the corresponding MEP 
Loss Measurement 
Service 
loss 
Enables or disables loss measurements for the destination 
NE: 
• Disable – Loss measurement is not performed 
• LMM Synthetic – Loss measurement is performed using 
synthetic LMM/LMR frames 
• SLM Synthetic – Loss measurement is performed using 
synthetic SLM/SLR frames 
• User Data – Loss measurement is performed on user 
data (real traffic) using LMM/LMR frames 
Delay Measurement 
Service 
delay 
Enables or disables delay measurements for the 
destination NE 
Delay Measurement 
Bin Profile 
delay-measurement-
bin-profile 
For Two way delay only 
Delay Var 
Measurement Bin 
Profile 
delay-var-
measurement-bin 
profile 
For one and two way delay variation 
 To add destination NEs in the web interface: 
Note 
You can add destination NEs only if the corresponding PM service is 
administratively enabled. 
1. Navigate to Configuration>OAM>CFM. 
11. Monitoring and Diagnostics 
2. In the row corresponding to the MA to which the MEP belongs for which you wish to add the 
destination NE, click config to display the Configuration > OAM > CFM > Config MA screen. 
3. In the row corresponding to the MEP, click Config MEP to display the Configuration > OAM > 
CFM > Config MA > Config MEP screen. 
4. In the row corresponding to the service, click Configure. 
MiNID 
 
 
 
 
 
 
Configuration>OAM>CFM\PM>Config MA>Config MEP>Config Service (P-
bit: 0 on MEP2, MA MA1) 
 
 
 
 
 
 
Add Destination Network 
Element 
 
 
 
 
 
 
 
 
 
Dest NE (ID: 1) 
Remove 
 
 
 
 
 
 
 
Configuring PM Service 
5. Click Add Destination Network Element. 
MiNID 
 
 
 
 
 
Configuration>OAM>CFM\PM>Config MA>Config MEP>Configure PM 
Service>Add Dest NE (MA: MA1, MEP-ID: 2, Service P-bit: 0) 
 
 
 
 
Dest NE Number 
 
1 
 
Admin Status 
 
Disable 
 
Remote MEP ID 
 
4 
 
Loss Measurement Service 
 
Disable 
 
Delay Measurement Service 
 
Disable 
 
Delay Measurement Bin Profile 
 
bin-profile-0 
 
Delay Var Measurement Bin Profile  
 
bin-profile-0 
 
 
 
 
Destination NE 
6. Fill in the parameters as specified in the Destination NE Parameters table. 
7. Click <Apply> to create the destination NE. 
11. Monitoring and Diagnostics 
 To configure a destination NE in the web interface: 
1. Navigate to Configuration>OAM>CFM. 
2. In the row corresponding to the MA to which the MEP belongs for which you wish to configure 
the destination NE, click config to display the Configuration>OAM>CFM>Config MA screen. 
3. In the row corresponding to the MEP, click Config MEP to display the 
Configuration>OAM>CFM>Config MEP screen. 
4. In the row corresponding to the service, click Configure to display the 
Configuration>OAM>CFM>Config PM Service screen. 
5. In the row corresponding to the destination NE, click the destination NE ID. 
6. Edit the parameters as specified in the Destination NE Parameters table. 
7. Click <Apply> to save your changes, and then click <Save Configuration>. 
 To delete a destination NE (web): 
1. Navigate to Configuration>OAM>CFM. 
2. In the row corresponding to the MA to which the MEP belongs for which you wish to delete the 
destination NE, click config to display the Configuration > OAM > CFM > Config MA screen. 
3. In the row corresponding to the MEP, click Config MEP to display the Configuration > OAM > 
CFM > Config MEP screen. 
4. In the row corresponding to the service, click Configure to display the Configuration > OAM > 
CFM > Config PM Service screen. 
5. In the row corresponding to the destination NE, click Remove. 
The destination NE is deleted. 
6. Click <Save Configuration>. 
 To add or configure a destination NE in the CLI: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid> service <serviceid> dest-ne <dest-neid>. 
The prompt config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service(<serviceid>)> 
dest-ne(<dest-neid>)# is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Clearing statistics 
clear-statistics 
 
Enabling delay 
measurement 
delay 
Enter no delay to disable delay 
measurement 
Delay Measurement Bin 
Profile 
delay-measurement-bin-
profile 
 
Delay Var Measurement Bin 
Profile 
delay-var-measurement-
bin profile 
 
Enabling loss measurement 
loss { slm | lmm-synthetic | 
user-data } 
• slm – Loss measurement is 
performed using synthetic SLM/SLR 
frames 
• lmm-synthetic – Loss measurement is 
performed using synthetic LMM/LMR 
frames 
• user-data – Loss measurement is 
performed on user data (real traffic) 
using LMM/LMR frames (only one 
destination NE per PM service is 
allowed with this method) 
Enter no loss to disable loss 
measurement 
Note: Only a single LM on real traffic is 
available per MiNID port for untagged 
OAM 
Defining remote MEP to 
associate with the 
destination NE 
remote-mep 
<remote-mep-id> 
This must be a remote MEP ID that has 
been configured for the corresponding 
MEP, and has not been associated with 
any other destination NE corresponding 
to the PM service 
Activating the destination 
NE 
no shutdown 
To disable the destination NE, enter 
shutdown 
You must define a valid remote MEP ID 
before you can activate the destination 
NE  
Displaying statistics 
show-statistics 
See Viewing Destination NE Statistics 
11. Monitoring and Diagnostics 
 To delete a destination NE: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)> 
service(<serviceid>)# prompt, enter: 
no dest-ne <dest neid> 
The destination NE is deleted. 
Configuring Measurement Bin Profiles 
 To add and configure a new measurement bin profile (web): 
1. Navigate to Configuration > OAM > CFM/PM > Measurement Bin Profiles. 
MiNID 
  
 
 
 
 
 Configuration>OAM>CFM/PM>Measurement Bin Profiles 
  
 
 
 
 
Add New Measurement Bin Profile 
  
 
 
 
 
 Profile Name 
 
 
 
 
  
 
 
 
 
  
 
 
 
 
  
 
 
 
 
2. Click Add New Measurement Bin Profile. 
MiNID 
  
 
 
 
 
 Configuration>OAM>CFM/PM>New Bin Profile 
  
 
 
 
 
 Profile Name 
Bin-porfile-2 
 
 
 
 Number of Thresholds 
1 
 
 
 
 Upper-Th-1 
10 
 
 
 
  
 
 
 
 
 Apply 
 
 
 
 
3. Type the name of the profile in the Profile Name field. 
4. Select the number of thresholds from the drop down list. 
11. Monitoring and Diagnostics 
5. In the Upper-Th-x field, type the upper threshold variable. 
6. Click <Apply>. 
MiNID 
  
 
 
 
 
 Configuration>OAM>CFM/PM>Measurement Bin Profiles 
  
 
 
 
 
Add New Measurement Bin Profile 
  
 
 
 
 
 Profile Name 
 
 
 
 
 Bin-profile-1 
remove 
 
 
 
 Bin-profile-2 
remove 
 
 
 
 Bin-profile-3 
remove 
 
 
 
  
 
 
 
 
7. To edit bin profile configuration, click the profile name and reconfigure the fields. 
8. To remove the bin profile, click remove. 
 To configure a measurement bin profile in the CLI: 
• 
Go to MiNID>config>oam>cfm# and configure the following: 
Task 
Command 
Comments 
Specifying the bin rpofile 
name 
measurement-bin-profile 
 
Specifying the thresholds 
for the bin profile 
thresholds 
The command is followed by the series of 
chosen thresholds 
Configuring Availability Parameters 
 To configure availability in the web interface: 
1. Navigate to Configuring > OAM > CFM/PM > Availability Params. 
The default parameters are displayed. 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 
 
 Configuration>OAM>CFM/PM>Availability Params 
  
 
 
 
 
 Delta-t 
1sec 
 
 
 
 n 
10 
 
 
 
 Forward Threshold 
50 
 
 
 
 Backward Threshold 
50 
 
 
 
  
 
 
 
 
 Apply 
 
 
 
 
2. Edit the parameters according to the following: 
 
Delta-t: Small interval time (in seconds) 
 
n: Number of consecutive small time intervals over which to measure availability 
 
Forward Threshold: Forward frame loss ratio threshold, for which unavailability occurs if 
exceeded 
 
Backward Threshold: Backward frame loss ratio threshold, for which unavailability occurs if 
exceeded 
3. Click Apply. 
 To configure availability in the CLI: 
• 
Navigate to MiNID>config>oam>cfm# and configure the following: 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining parameters for 
availability calculations 
availability [delta-t {1 | 2 | 
3 | 4 | 5 | 6 | 10 | 12 | 15 
| 20}] [n <n>] 
[forward-thr <forward-thr-
percents>] 
[backward-thr <backward-
thr-percents>] 
These parameters define availability performance 
measurement, based on frame loss during a sequence 
of consecutive small time intervals: 
• delta-t – Time interval (in seconds) 
• n –Number of consecutive small time intervals over 
which to measure availability 
• forward-thr – Forward frame loss ratio threshold, 
for which unavailability occurs if exceeded  
• backward-thr – Backward frame loss ratio 
threshold, for which unavailability occurs if 
exceeded  
Performing OAM Loopback 
This diagnostic utility verifies OAM connectivity on Ethernet connections.  
 To run an OAM loopback in the web interface: 
1. Navigate to Configuration > OAM > CFM. 
2. In the row corresponding to the MA to which the MEP belongs for which you wish to run OAM 
loopback, click config to display the Configuration > OAM > CFM\PM > Config MA screen. 
3. In the row corresponding to the MEP, click Config MEP to display the Configuration > OAM > 
CFM\PM > Config MA > Config MEP screen. 
4. Click Start Loopback Session. 
MiNID 
  
 
 
 Configuration>OAM>CFM>Config MA>Config MEP>LBM Session 
  
 
 
 LBM Session Mode 
 
Multicast 
 Data TLV Length [0..1450] 
 
0 
  
 
 
Starting LBM Session 
5. Set LBM Session Mode to one of the following: 
11. Monitoring and Diagnostics 
 
Multicast –To send LBMs to the MAC address corresponding to the MEP MD level, as shown 
in the MEP Parameters table. 
 
Unicast –To send LBMs to a specific MAC address 
 
Remote MEP – To send LBMs to the remote MEP MAC address 
6. If LBM Session Mode is set to Unicast, the parameters Destination MAC Address and Number Of 
LoopBack Messages appear in the screen. 
MiNID 
  
 
 
 Configuration>OAM>CFM 
  
 
 
 LBM Session Mode 
 
Unicast 
 Destination MAC Address 
 
00-00-00-00-00-00 
 Number of LoopBack Messages 
[1..1000] 
 
1 
 Data TLV Length [0..1450] 
 
0 
  
 
 
LBM Session – Unicast 
1. If LBM Session Mode is set to Remote MEP, the parameters Remote MEP ID and Number of 
LoopBack Messages parameter appear. 
MiNID 
  
 
 
 Configuration>OAM>CFM 
  
 
 
 LBM Session Mode 
 
Remote MEP 
 Remote MEP ID 
 
55 
 Number of LoopBack Messages 
[1..1000] 
 
20 
 Data TLV Length [0..1450] 
 
250 
  
 
 
LBM Session – Remote MEP 
1. Set the parameters as needed, and then click Run to start the loopback. 
11. Monitoring and Diagnostics 
 To view the OAM loopback results in the web interface: 
1. Navigate to Monitoring > OAM > CFM(see Error! Reference source not found.). 
2. In the row for the corresponding MA, click <Info> to display the Monitoring>OAM>CFM>MA Info 
screen (see Error! Reference source not found.). 
3. In the row for the corresponding MEP, click LB Status. 
MiNID 
  
 
 
 Monitoring>OAM>CFM 
  
 
 
 Dest Address 
 
00-20-D2-51-42-52 
 LBM Sent 
 
20 
 Replies In Order 
 
20 
 Replies Out Of Order 
 
0 
 MSG Lost\Timeout 
 
0 
 MSG Lost\Timeout (%) 
 
0.00 
  
 
 
OAM Loopback Status 
 To run an OAM loopback in the CLI: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, enter all necessary 
commands according to the tasks listed below. 
Task 
Command 
Comments 
Sending LBMs to specific MAC 
address 
lbm address <mac-address> [repeat 
<repeat-num>] [data-tlv-length <length>] 
• MAC address is in the format 
<xx-xx-xx-xx-xx-xx> 
• Allowed range of 
repeat-num is 1–1000 
• Allowed range of 
data-tlv-length is 0–1450 
 
Sending LBMs to multicast 
MAC address 
lbm multicast [data-tlv-length <length>] 
Multicast MAC address 
corresponds to the MEP MD 
level, as shown in Error! 
Reference source not found. 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Sending LBMs to remote MEP 
lbm remote-mep <remote-mep-id>  
[repeat <repeat-num>] [data-tlv-length 
<length>] 
 
Checking OAM loopback 
results 
show lbm-results 
 
Performing OAM Link Trace 
This diagnostic utility traces the OAM route to the destination.  
 To run an OAM link trace with the web interface: 
1. Navigate to Configuration>OAM>CFM (see Error! Reference source not found.). 
2. In the row corresponding to the MA to which the MEP belongs for which you wish to run OAM 
link trace, click config to display the Configuration>OAM>CFM\PM>Config MA screen . 
3. In the row corresponding to the MEP, click Config MEP to display the 
Configuration>OAM>CFM>Config MA>Config MEP screen. 
4. Click Start Linktrace Session. 
The LTM Session screen appears.  
MiNID 
  
 
 
 Configuration>OAM>CFM>Config MA>Config MEP>LTM Session 
  
 
 
 LTM Session Mode 
 
Unicast 
 Target MAC 
Address 
 
00-20-D2-51-42-52 
 TTL [1..24] 
 
24 
  
 
 
Starting LTM Session – Unicast  
1. Set LTM Session Mode to one of the following: 
 
Unicast –To send LTMs to a specific MAC address, specified by Target MAC Address 
 
Remote MEP – To send LTMs to a specific remote MEP, specified by Remote MEP ID 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Configuration>OAM>CFM>Config MA>Config MEP>LTM Session 
  
 
 
 LTM Session Mode 
 
Remote MEP 
 Remote MEP ID 
 
55 
 TTL [1..24] 
 
24 
  
 
 
Starting LTM Session – Remote MEP 
1. Set TTL (time-to-live) to the number of hops. Each unit in the link trace decrements the TTL until 
it reaches 0, which terminates the link trace. 
2. Click Run to start the link trace. 
 To view the OAM link trace results: 
1. Navigate to Monitoring>OAM>CFM. 
2. In the row for the corresponding MA, click <Info> to display the Monitoring>OAM>CFM>MA Info 
screen. 
3. In the row for the corresponding MEP, click LT Status. 
 
  
 
 
 
 
 Monitoring>OAM>CFM 
  
 
 
 
 
 
MAC Address 
TTL 
Last Egress ID 
Relay 
Action 
 
 
00-20-D2-51-42-52 
23 
(0010) 
00-20-D2-51-7E-2D 
RlyHit 
 
  
 
 
 
 
OAM Link Trace Status 
 To run an OAM link trace in the CLI: 
• 
At the config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# prompt, enter all necessary 
commands according to the tasks listed below. 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Sending LTMs to specific MAC 
address 
linktrace address <mac-address> 
[ttl <ttl>] 
• MAC address is in the format 
<xx-xx-xx-xx-xx-xx> 
• Allowed range for <ttl> is 1–
24. This parameter specifies 
number of hops. Each unit in 
the link trace decrements 
the TTL until it reaches 0, 
which terminates the link 
trace. 
Sending LTMs to remote MEP 
linktrace remote-mep 
<remote-mep-id>  [ttl <ttl>] 
 
 
Checking the OAM link trace 
results 
show linktrace-results 
 
Examples 
This section contains CLI configuration examples. 
Creating MA, MEP, and Service 
This example illustrates creating the following: 
• 
MD ID 4 
• 
MA ID 5: Name MA5, VLAN 17 
• 
MEP ID 16:  
 
Bound to port: SFP/1 
 
Enabled AIS and CCM transmission 
 
Remote MEP IDs 32, 64 
• 
Service 4: enabled loss (standard) and delay measurement 
 To create MEP and service: 
exit all 
configure oam cfm maintenance-domain 4 maintenance-association 5 
  name MA5 format string 
11. Monitoring and Diagnostics 
  vlan 17 
 
  mep 16 
    bind ingress-port sfp/1 
    ais 
    ccm-initiate 
    remote-mep 32 
    remote-mep 64 
    no shutdown 
 
    service 4 
      delay 
      loss slm 
      no shutdown 
      exit all 
 To display the configured entities: 
# configure oam cfm maintenance-domain 4 maintenance-association 5 
>config>oam>cfm>md(4)>ma(5)# info  
                ccm-interval 100ms 
                mep 16 
                        ais 
                        bind ingress-port sfp/1  
                        ccm-initiate 
                        client-md-level 5 
                        dest-addr-type ccm multicast 
                        remote-mep 32 
                        service 4 
                                delay 
                                delay-threshold 1 
                                delay-var-threshold 1 
                                lmm-interval 1s 
                                dmm-interval 1s 
                                loss slm 
                                priority 0 
                                no shutdown 
                        exit 
                        no shutdown 
                exit 
                name MA5 format string 
                priority 0 
                vlan 17 
        exit 
Creating MA and MIP 
This example illustrates creating the following: 
• 
MD ID 3 
• 
MA ID 2: Name MA2, VLAN 999 
11. Monitoring and Diagnostics 
• 
MIP 
 To create MIP: 
exit all 
configure oam cfm maintenance-domain 3 maintenance-association 2 
name MA2 format string 
vlan 999 
mip 
no shutdown 
exit all 
Displaying MEP Status  
The following illustrates displaying MEP status for the MEP configured in the above example, assuming 
that in another device in the network, MEP 32 has been configured with remote MEP 16 in MD ID 4, 
MA5. 
>config>oam>cfm>md(4)>ma(5)>mep(16)# show status 
MEP Defect:                                                   Status 
---------------------------------------------------------------------- 
Rx AIS                                                :       OFF 
Cross Connected CCM (Mismatch; Unexpected MD Level)   :       OFF 
Invalid CCM (Unexpected MEP; Unexpected CCM Period)   :       OFF 
 
Remote MEP      Remote MEP Address      Operational Status 
--------------------------------------------------------- 
32              00-20-D2-51-42-52       OK 
64              00-00-00-00-00-00       Fail 
 
>config>oam>cfm>md(4)>ma(5)>mep(16)# show remote-mep remote-mep-id 32 
Operational State       :       RMEP_OK 
SysUpTime               :       25199 sec. 
Remote MEP Address      :       00-20-D2-51-42-52 
Last RDI Bit            :       False 
Loss Of Continuity      :       OFF 
Performing OAM Loopback  
This example illustrates performing OAM loopback on the previously configured MEP: 
• 
Use remote MEP ID 
• 
Send 20 LBMs 
• 
LBM frame length 250 
>config>oam>cfm>md(4)>ma(5)>mep(16)# lbm remote-mep 32 repeat 20 data-tlv-length 250 
>config>oam>cfm>md(4)>ma(5)>mep(16)# show lbm-results 
Destination MAC :       00-20-D2-51-42-52 
11. Monitoring and Diagnostics 
LBM Sent                :       20 
Replies In Order        :       20 
Replies Out Of Order    :       0 
Messages Lost\Timeout   :       0 
Messages Lost\Timeout(%):       0.00 
Performing OAM Link Trace  
This example illustrates performing OAM link trace on the previously configured MEP: 
• 
Use remote MEP MAC address 
• 
TTL=20 
>config>oam>cfm>md(4)>ma(5)>mep(16)# linktrace address 00-20-D2-51-42-52 ttl 20 
>config>oam>cfm>md(4)>ma(5)>mep(16)# show linktrace-results 
MAC                     TTL     Last                            Relay 
Address                         Egress-Id                       Action 
----------------------------------------------------------------------- 
00-20-D2-51-42-52       19      (0010) 00-20-D2-51-7E-2D        RlyHit 
Displaying Running Statistics 
# configure oam cfm maintenance-domain 4 maintenance-association 5 mep 16 service 4 
dest-ne 1 show-statistics 
>config>oam>cfm>md(4)>ma(5)>mep(16)>service(4)>dest-ne(1)>show-stats# running 
Service State       :   Unavailable 
Statistics          :   Running 
Elapsed Time (Sec.) :   168517 
----------------------------------------------------- 
Two-Way Delay (ms)                      :       0.000 (ms) 
Two-Way Delay Variation (ms)            :       0.000 (ms) 
One-Way Delay Variation (ms)            :       0.000 (ms) 
Frames Exceed Delay Threshold           :       0 
Frames Exceed Delay Variation Threshold :       0 
 
                        Forward         Backward 
Tx Frames            :  0               0 
Rx Frames            :  0               0 
Frame Loss           :  0               0 
Frame Loss Ratio (%) :  0.000000        0.000000 
Unavailable Seconds  :  168517          168517 
Available Seconds    :  0               0 
 
       Tx       Rx 
LMMs : 0        LMRs : 0 
DMMs : 0        DMRs : 0 
 
 
11. Monitoring and Diagnostics 
Displaying Current Interval Statistics 
# configure oam cfm maintenance-domain 4 maintenance-association 5 mep 16 service 4 
dest-ne 1 show-statistics 
>config>oam>cfm>md(4)>ma(5)>mep(16)>service(4)>dest-ne(1)>show-stats# current 
Service State       :   Unavailable 
Statistics          :   Current (Last 15 Min.) 
Elapsed Time (Sec.) :   64 
----------------------------------------------------- 
 
                        Min     Average Max 
                        (ms)    (ms)    (ms) 
Two-Way Delay           0.000  0.000  0.000 
Two-Way Delay Variation 0.000  0.000  0.000 
One-Way Delay Variation 0.000  0.000  0.000 
Frames Exceed Delay Threshold           :       0 
Frames Exceed Delay Variation Threshold :       0 
 
                        Forward         Backward 
Tx Frames            :  0               0 
Rx Frames            :  0               0 
Frame Loss           :  0               0 
Frame Loss Ratio (%) :  0.000000        0.000000 
Unavailable Seconds  :  64              64 
Available Seconds    :  0               0 
 
       Tx       Rx 
LMMs : 0        LMRs : 0 
DMMs : 0        DMRs : 0 
Displaying Selected Interval Statistics 
# configure oam cfm maintenance-domain 4 maintenance-association 5 mep 16 service 4 
dest-ne 1 show-statistics 
>config>oam>cfm>md(4)>ma(5)>mep(16)>service(4)>dest-ne(1)>show-stats# interval 4 
Statistics              :       Interval 
Interval Number         :       4 
Interval Duration       :       08:46:49 29-03-2016  - 09:01:39 29-03-2016 
-------------------------------------------------------------------------- 
 
                        Min     Average Max 
                        (ms)    (ms)    (ms) 
Two-Way Delay           0.000  0.000  0.000 
Two-Way Delay Variation 0.000  0.000  0.000 
Frames Exceed Delay Threshold           :       0 
Frames Exceed Delay Variation Threshold :       0 
 
                        Forward         Backward 
Tx Frames            :  0               0 
Rx Frames            :  0               0 
Frame Loss           :  0               0 
Frame Loss Ratio (%) :  0.000000        0.000000 
Unavailable Seconds  :  900             900 
11. Monitoring and Diagnostics 
Available Seconds    :  0               0 
 
       Tx       Rx 
LMMs : 0        LMRs : 0 
DMMs : 0        DMRs : 0 
Displaying Total Interval Statistics 
# configure oam cfm maintenance-domain 4 maintenance-association 5 mep 16 service 4 
dest-ne 1 show-statistics 
>config>oam>cfm>md(4)>ma(5)>mep(16)>service(4)>dest-ne(1)>show-stats# total-intervals 
Statistics              :       Total Interval 
----------------------------------------------------- 
 
                        Min     Average Max 
                        (ms)    (ms)    (ms) 
Two-Way Delay           0.000  0.000  0.000 
Two-Way Delay Variation 0.000  0.000  0.000 
Frames Exceed Delay Threshold           :       0 
Frames Exceed Delay Variation Threshold :       0 
 
                        Forward         Backward 
Tx Frames            :  0               0 
Rx Frames            :  0               0 
Frame Loss           :  0               0 
Frame Loss Ratio (%) :  0.000000        0.000000 
Unavailable Seconds  :  85500           85500 
Available Seconds    :  0               0 
 
       Tx       Rx 
LMMs : 0        LMRs : 0 
DMMs : 0        DMRs : 0 
Displaying All Interval Statistics 
This example illustrates displaying all intervals if there are two valid intervals. 
# configure oam cfm maintenance-domain 4 maintenance-association 5 mep 16 service 4 
dest-ne 1 show-statistics 
>config>oam>cfm>md(4)>ma(5)>mep(16)>service(4)>dest-ne(1)>show-stats# all-intervals 
Interval No.            :       1 
Interval Duration       :       09:31:20 29-03-2016  - 09:46:10 29-03-2016 
-------------------------------------------------------------------------- 
                        Min     Average Max 
                        (ms)    (ms)    (ms) 
Two-Way Delay           0.000  0.000  0.000 
Two-Way Delay Variation 0.000  0.000  0.000 
Frames Exceed Delay Threshold           :       0 
Frames Exceed Delay Variation Threshold :       0 
 
                        Forward         Backward 
Tx Frames            :  0               0 
11. Monitoring and Diagnostics 
Rx Frames            :  0               0 
Frame Loss           :  0               0 
Frame Loss Ratio (%) :  0.000000        0.000000 
Unavailable Seconds  :  900             900 
Available Seconds    :  0               0 
 
       Tx       Rx 
LMMs : 0        LMRs : 0 
DMMs : 0        DMRs : 0 
 
Interval No.            :       2 
Interval Duration       :       09:16:30 29-03-2016  - 09:31:20 29-03-2016 
-------------------------------------------------------------------------- 
 
 
                        Min     Average Max 
                        (ms)    (ms)    (ms) 
Two-Way Delay           0.000  0.000  0.000 
Two-Way Delay Variation 0.000  0.000  0.000 
Frames Exceed Delay Threshold           :       0 
Frames Exceed Delay Variation Threshold :       0 
 
                        Forward         Backward 
Tx Frames            :  0               0 
Rx Frames            :  0               0 
Frame Loss           :  0               0 
Frame Loss Ratio (%) :  0.000000        0.000000 
Unavailable Seconds  :  900             900 
Available Seconds    :  0               0 
 
       Tx       Rx 
LMMs : 0        LMRs : 0 
DMMs : 0        DMRs : 0 
Viewing OAM Status 
Viewing MEP Status 
 To view the MEP status in the web interface: 
1. Navigate to Monitoring>OAM>CFM\PM. 
 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 
 
 
 
 
 Monitoring>OAM>CFM\PM 
  
 
 
 
 
 
 
 
 MD Index 
MD Level 
MD Name 
MD Name Format  
 
 1 
5 
MD1 
String 
Info 
 
 2 
3 
MD2 
String 
Info 
 
 3 
4 
MD2 
String 
Info 
 
 4 
2 
MD4 
String 
Info 
 
 Summary  
 
 
 
 
 
 
  
 
 
 
 
 
 
 
Monitoring OAM (CFM) – MD Level 
2. In the row for the corresponding MD, click <Info>. 
MiNID 
  
 
 
 
 
 
 
 
 Monitoring>OAM>CFM\PM>MD Info 
  
 
 
 
 
 
 
 
 MD 
Index 
 
1 
 
 
 
 
 
 MD 
Level 
 
5 
 
 
 
 
 
 MD Name Format 
String 
 
 
 
 
 
 MD 
Name 
 
MD1 
 
 
 
 
 
  
 
 
 
 
 
 
 
 MA 
Index 
MA Name 
MD Level 
Vlan Tag 
Mode 
Service 
Name 
 
 
 1 
MA1 
5 
Single 
23 
Info 
 
 2 
MA3 
5 
Double-Inner 
Gold 
Info 
 
 3 
MA6 
5 
Double-Outer 
 
Info 
 
  
 
 
 
 
 
 
 
Monitoring OAM (CFM) – MA Level 
3. In the row for the corresponding MA, click <Info>. 
11. Monitoring and Diagnostics 
MiNID 
 
 
 
 
 
 
 
Monitoring>OAM>CFM\PM>MA Info 
 
 
 
 
 
 
 
MD Level 
 
5 
 
 
 
MA Name 
 
MA1 
 
 
 
MA Format 
 
Character String 
 
 
 
Service Name 
 
23 
 
 
 
Vlan Tag Mode 
 
Single 
 
 
 
CCM Interval 
 
100ms 
 
 
 
Interface Status TLV 
 
Disable 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
MEP (ID: 2) 
Info 
MEP Status 
LB 
Status 
LT 
Status 
Remote MEP – ID: 
100 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Monitoring OAM (CFM) – MA Info (Single-Tag Mode) 
11. Monitoring and Diagnostics 
MiNID 
 
 
 
 
 
 
 
Monitoring>OAM>CFM\PM>MA Info 
 
 
 
 
 
 
 
MD Level 
 
5 
 
 
 
MA Name 
 
MA6 
 
 
 
MA Format 
 
Character String 
 
 
 
Service Name 
 
Goldr 
 
 
 
Vlan Tag Mode 
 
Double-Inner 
 
 
 
CCM Interval 
 
100ms 
 
 
 
Interface Status 
TLV 
 
Disable 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
MEP (ID: 
11) 
Info 
MEP Status LB Status 
LT Status 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
MEP (ID: 2) 
Info 
MEP Status LB Status 
LT Status 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Monitoring OAM (CFM) – MA Info (Double-Tag Mode) 
4. In the row for the corresponding MEP, click <MEP Status>. 
Note 
If the MEP is administratively disabled, then the indication Disabled appears 
instead of the Status and Statistics links. 
The MEP status is displayed. 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Monitoring>OAM>CFM>MA MEP Status 
  
 
 
 Rx AIS 
 
OFF 
 Defects: 
 
 
 MisMerge* 
 
OFF 
 Unexpected MEP 
 
OFF 
 Unexpected MD Level 
 
OFF 
 Unexpected Period 
 
OFF 
  
 
 
  
 
 
Monitoring OAM (CFM) – MEP Status 
*MisMerge denotes a state when a CCM frame with the same MD Level but with a MAID (MEGID) 
different than the receiving MEP’s own MAID (MEGID) is received.  
 
5. To view status for a remote MEP, click <Back> to return to the MEP status screen, and then click 
the remote MEP ID for which you wish to view the status. 
MiNID 
  
 
 
 Monitoring>OAM>CFM 
  
 
 
 State 
 
RMEP_OK 
 Sys Up Time 
 
207 sec. 
 Last MAC Address 
Received 
 
00-20-D2-51-7E-2D 
 Loss of Continuity 
 
OFF 
 Last RDI Bit State 
 
False 
  
 
 
Monitoring OAM (CFM) – Remote MEP Status 
11. Monitoring and Diagnostics 
 To view MEP status in the CLI: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid>. 
The prompt config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)# is displayed. 
2. Enter: 
show status 
The MEP status is displayed. See Displaying MEP Status for an example. 
3. For each configured remote MEP, enter : 
show remote-mep remote-mep-id <remote-mep-id> 
The remote MEP status is displayed. See Displaying MEP Status for an example. 
Viewing OAM Statistics 
Viewing Destination NE Statistics 
You can view the following types of statistics for the OAM services destination NEs: 
• 
Running –OAM statistics collected since the destination NE was activated.  
• 
Interval – OAM statistics for the current interval or selected intervals 
• 
Total intervals – Sums of the statistics of all valid intervals (with the exception that the Two-Way 
Delay and Two-Way Delay Variation counters are averages). 
Note 
In order to be able to view the statistics, the destination NE, corresponding 
MEP, and corresponding service must be administratively enabled, for at least 
the duration of the configured PM interval. 
Viewing Statistics Using the Web Interface 
 To display the OAM CFM statistics: 
1. Navigate to Monitoring>OAM>CFM (see Error! Reference source not found.). 
2. In the row for the corresponding MA, click <Info> to display the Monitoring>OAM>CFM>MA Info 
screen (see Error! Reference source not found.). 
3. In the row for the corresponding MEP, click <Info>. 
 
11. Monitoring and Diagnostics 
MiNID 
 
 
 
c 
 
 
Monitoring >OAM>CFM 
 
 
 
 
 
 
Admin Status 
 
Enable 
 
 
MEP ID [1..8191] 
 
1 
 
 
Ingress Port 
 
SFP/Port 1 
 
 
CCM Enable 
 
Enable 
 
 
CCM Transmission Mode 
 
Multicast 
 
 
Client MD Level 
 
4 
 
 
AIS Enable 
 
Enable 
 
 
 
 
 
 
 
Service (P-bit: 0) 
Info 
Dest NE – ID: 1 
 
 
Dest NE – ID: 2 
 
Service (P-bit: 5) 
Info 
Dest NE – ID: 7 
 
 
Dest NE – ID: 8 
 
 
 
 
 
Monitoring OAM (CFM) – MEP Info 
4. Click the destination NE for which you wish to view statistics. 
11. Monitoring and Diagnostics 
MiNID 
  
 
 
 Monitoring>OAM>CFM 
  
 
 
 Admin Status 
 
Enable 
 Dest NE ID 
 
1 
 Remote MEP ID 
 
55 
 Loss Measurement Service 
 
LMM Synthetic 
 Delay Measurement Service 
 
Enable 
  
 
 
 Running statistics 
 
 
 Current statistics 
 
 
 Interval statistics 
 
 
 Total Interval statistics 
 
 
  
 
 
Monitoring OAM (CFM) – Dest NE Info 
5. According to which type of statistics to display: 
 
To display the running statistics, click Running Statistics. 
The statistics are displayed. To clear the statistics, click <Clear Statistics>. 
 
To display the current interval statistics, click Current. 
The statistics are displayed as illustrated in the figure below; for explanation, see OAM Statistic 
Counters and OAM Loss and Delay Measurement Counters tables. To clear the statistics, click 
<Clear Statistics>.  
 
To display the statistics for selected intervals, click Interval Statistics. 
The statistics are displayed for interval 1; see OAM Statistic Counters and OAM Loss and Delay 
Measurement Counters tables. 
The duration and validity of the interval are indicated in the interval statistics. An interval is 
considered as not valid if it has not yet ended, or if statistics were cleared during the 
interval. 
You can view selected intervals from the last 96 intervals (the amount of available intervals 
depends on how much time has passed since the destination NE was administratively 
enabled) by clicking <Previous> or <Next> to go to the previous or next interval, 
respectively, or by entering the interval number and then clicking <Change>. If you attempt 
to view an interval that is not available, a message to that effect is displayed. 
 
To display the total interval statistics, click Total Interval Statistics. 
11. Monitoring and Diagnostics 
The statistics are displayed as illustrated below; see OAM Statistic Counters and OAM Loss and 
Delay Measurement Counters tables. 
11. Monitoring and Diagnostics 
 
MiNID 
 Monitoring>OAM>CFM 
 
Dest NE State 
 
Unavailable 
 
Statistics 
 
Running 
 
 
 
 
 
Elapsed Time (Sec.) 
 
414 
 
 
 
 
 
Two-Way Delay (ms)  
 
0.000 (ms) 
 
Two-Way Delay Variation (ms) 
 
0.000 (ms) 
 
One-Way Delay Variation (ms) 
 
0.000 (ms) 
 
 
 
 
 
Frames Exceed Delay Threshold 
 
0 
 
Frames Exceed Delay Variation Threshold 
 
0 
 
 
Forward 
Backward 
 
Tx Frames 
0 
 
 
Rx Frames 
0 
 
 
Frame Loss 
0 
 
 
Frame Loss Ratio 
0.000000% 
0.000000% 
 
Available Seconds 
0 
0 
 
Unavailable Seconds 
414 
414 
 
 
 
 
 
Two-Way Delay Bins Measurement - No Bin Profile Bound: 
 
Bin Number 
Range [us] 
Counter 
 
1 
 
 
 
2 
 
 
 
3 
 
 
 
Two-Way Delay Variation Bins Measurement - No Bin Profile Bound: 
 
Bin Number 
Range [us] 
Counter 
 
1 
 
 
 
2 
 
 
 
3 
 
 
 
One-Way Delay Bins Measurement - No Bin Profile Bound: 
 
Bin Number 
Range [us] 
Counter 
 
1 
 
 
 
2 
 
 
 
3 
 
 
 
Transmitted 
 
Received 
 
LMMs: 0 
 
LMRs: 0 
 
DMMs: 0 
 
DMRs: 0 
 
Clear Statistics 
 
 
Monitoring OAM (CFM) – Running Statistics 
11. Monitoring and Diagnostics 
MiNID 
 Monitoring>OAM>CFM 
 
Dest NE State 
 
Unavailable 
 
Statistics 
 
Current (Last 15 minutes) 
 
 
 
 
 
Elapsed Time (Sec.) 
 
532 
 
 
Min 
Average 
Max 
 
Two-Way Delay (ms)  
0.000 
0.000 
0.000 
 
Two-Way Delay Variation (ms) 
0.000 
0.000 
0.000 
 
One-Way Delay Variation (ms) 
0.000 
0.000 
0.000 
 
 
 
 
 
Frames Exceed Delay Threshold 
 
0 
 
Frames Exceed Delay Variation 
Threshold 
 
0 
 
 
Forward 
Backward 
 
Tx Frames 
0 
 
 
Rx Frames 
0 
 
 
Frame Loss 
0 
 
 
Frame Loss Ratio 
0.000000% 
0.000000% 
 
Available Seconds 
0 
0 
 
Unavailable Seconds 
414 
414 
 
Two-Way Delay Bins Measurement - No Bin Profile Bound: 
 
Bin Number 
Range [us] 
Counter 
 
1 
 
 
 
2 
 
 
 
3 
 
 
 
Two-Way Delay Variation Bins Measurement - No Bin Profile Bound: 
 
Bin Number 
Range [us] 
Counter 
 
1 
 
 
 
2 
 
 
 
3 
 
 
 
One-Way Delay Bins Measurement - No Bin Profile Bound: 
 
Bin Number 
Range [us] 
Counter 
 
1 
 
 
 
2 
 
 
 
3 
 
 
 
Transmitted 
 
Received 
 
LMMs: 0 
 
LMRs: 0 
 
DMMs: 0 
 
DMRs: 0 
 
Clear Statistics 
 
 
Monitoring OAM (CFM) – Current Statistics 
11. Monitoring and Diagnostics 
MiNID 
 
Monitoring>OAM>CFM 
 
Interval Number 
 
1 
 
Interval Duration 
 
23:11:13 05-01-2016 – 23:26:02 05-01-2016 
 
Status 
 
Valid 
 
 
 
Min 
 
Two-Way Delay (ms)  
 
0.000 
 
Two-Way Delay Variation (ms) 
 
0.000 
 
One-Way Delay Variation (ms) 
 
0.000 
 
 
 
Frames Exceed Delay Threshold 
0 
 
Frames Exceed Delay Variation Threshold 
0 
 
Forward 
Backward 
 
Tx Frames 
0 
0 
 
Rx Frames 
0 
0 
 
Frame Loss 
0 
0 
 
Frame Loss Ratio 
0.000000% 
0.000000% 
 
Available Seconds 
0 
0 
 
Unavailable Seconds 
900 
900 
 
Delay Bins Measurement - No Bin Profile Bound: 
 
Bin Number 
Range [us] 
Counter 
 
1 
 
 
2 
 
 
3 
 
 
Delay Variation Bins Measurement - No Bin Profile Bound: 
 
Bin Number 
Range [us] 
Counter 
 
1 
 
 
2 
 
 
3 
 
 
One-Way Delay Variation Bins Measurement - No Bin Profile Bound: 
 
Bin Number 
Range [us] 
Counter 
 
1 
 
 
2 
 
 
3 
 
 
 
 
 
 
Transmitted 
 
Received 
 
LMMs: 0 
 
LMRs: 0 
 
DMMs: 0 
 
DMRs: 0 
11. Monitoring and Diagnostics 
 
Previous 
 
Next 
 
Interval(1-96) 
 
1 
 
 
 
Change 
 
 
 
 
Monitoring OAM (CFM) – Interval Statistics 
11. Monitoring and Diagnostics 
  
 
 
 Monitoring>OAM>CFM 
  
 
 
 Statistics 
 
15 Min. Interval 
  
 
 
 
Min 
Average 
Max 
 Two-Way Delay (ms)  
0.000 
0.000 
0.000 
 Two-Way Delay Variation (ms) 
0.000 
0.000 
0.000 
 One-Way Delay Variation (ms) 
0.000 
0.000 
0.000 
 
 
 Frames Exceed Delay Threshold 
 
0 
 Frames Exceed Delay Variation 
Threshold 
 
0 
 
Forward 
Backward 
 Tx Frames 
0 
0 
 Rx Frames 
0 
0 
 Frame Loss 
0 
0 
 Frame Loss Ratio 
0.000000% 0.000000% 
 Available Seconds 
0 
0 
 Unavailable Seconds 
5400 
5400 
 Two-Way Delay Bins Measurement - No Bin Profile Bound: 
 Bin Number 
Range [us] 
Counter 
 1 
 
 2 
 
 3 
 
 
 
 Two-Way Delay Variation Bins Measurement - No Bin Profile Bound: 
 Bin Number 
Range [us] 
Counter 
 1 
 
 
 2 
 
 
 3 
 
 
  
 
 
 One-Way Delay Bins Measurement - No Bin Profile Bound: 
 Bin Number 
Range [us] 
Counter 
 1 
 
 
 2 
 
 
 3 
 
 
 Transmitted 
 
Received 
11. Monitoring and Diagnostics 
 LMMs: 0 
 
LMRS: 0 
 DMMs: 0 
 
DMRs: 0 
  
 
 
Monitoring OAM (CFM) – Total Interval Statistics 
Viewing Statistics Using the CLI 
 To display the OAM CFM statistics: 
1. Navigate to configure oam cfm maintenance-domain <mdid> maintenance-association <maid> 
mep <mepid> service <serviceid> dest-ne <dest-neid> show-statistics. 
The following prompt is displayed: 
config>oam>cfm>md(<mdid>)>ma(<maid>)>mep(<mepid>)>service(<serviceid>)> 
dest-ne(<dest-neid>)>show-stats# 
2. Enter all necessary commands according to the tasks listed below. 
Note 
If the destination NE is administratively disabled, a message stating that is 
displayed if you attempt to display the statistics. 
 
Task 
Command 
Comments 
Viewing statistics for all 
intervals 
all-intervals 
If available, the statistics are 
displayed as shown in 
Displaying All Interval 
Statistics; see the tables 
below   
Viewing running statistics 
running  
If available, the statistics are 
displayed as shown in 
Displaying Running Statistics; 
see the tables below  
Viewing statistics for current 
interval 
current 
If available, the statistics are 
displayed as shown in 
Displaying Current Interval 
Statistics; see the tables 
below 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Viewing statistics for selected 
interval 
interval <interval-number> 
If available, the statistics are 
displayed as shown in 
Displaying Selected Interval 
Statistics; see the tables 
below 
Viewing statistics for total 
intervals 
total-intervals 
If available, the statistics are 
displayed as shown in 
Displaying Total Interval 
Statistics; see the tables 
below   
 
OAM Statistic Counters 
Parameter 
Description 
Tx Frames Forward 
Total number of frames transmitted from local service to remote 
service since the service was activated  
Rx Frames Forward 
Total number of frames received by remote service since the service 
was activated 
Frame Loss Forward 
Total number of frames lost from local service to remote service 
since the service was activated (Far End Tx Frames - 
Far End Rx Frames) (the type of frames counted is either user data 
or synthetic, according to the method configured by the loss 
single-ended command) 
Unavailable Seconds Forward 
Number of seconds the remote service is considered unavailable in 
direction local service to remote service 
Tx Frames Backward 
Total number of frames transmitted from remote service to local 
service since the service was activated  
Rx Frames Backward 
Total number of frames received by local service since the service 
was activated  
Frame Loss Backward 
Total number of frames lost from service to local service since the 
service was activated (Near End Tx Frames - Near End Rx Frames)  
Unavailable Seconds Backward 
Number of seconds the remote service is considered unavailable in 
direction remote service to local service 
Available Seconds Forward 
Number of seconds the remote service is considered available in 
direction local service to remote service 
11. Monitoring and Diagnostics 
Parameter 
Description 
Available Seconds backward 
Number of seconds the remote service is considered available in 
direction remote service to local service 
Two-Way Delay (ms) 
Minimal, average and maximal of all frame delay values  
Two-Way Delay Variation (ms) 
Minimal, average and maximal difference between the frame delay 
values  
One-Way Delay Variation (ms) 
Minimal, average and maximal difference between the frame delay 
values  
Frames Exceed Delay Threshold 
Number of frames whose delay value exceeded the delay threshold 
configured for the service 
Frames Exceed Delay Variation 
Threshold 
Number of frames whose delay variation exceeded the delay 
variation threshold configured for the service 
OAM Loss and Delay Measurement Counters  
Parameter 
Description 
Transmitted LMMs 
Number of transmitted loss measurement messages 
Note: Relevant only for LMM synthetic and user data loss measurement. 
Transmitted SLMs 
Number of transmitted standard loss measurement messages 
Note: Relevant only for SLM synthetic loss measurement. 
Transmitted DMMs 
Number of transmitted delay measurement messages 
Received LMRs 
Number of received loss measurement replies 
Note: Relevant only for LMM synthetic and user data loss measurement. 
Received SLRs 
Number of received standard loss measurement replies 
Note: Relevant only for SLM synthetic loss measurement. 
Received DMRs 
Number of received delay measurement replies 
Viewing OAM/CFM Summary 
MiNID displays a summary of OAM/CFM statistics. 
 To view the summary using the web interface: 
1. Navigate to >Monitoring>OAM>CFP/PM. 
2. Click Summary. 

## 11.4 OAM (EFM)  *(p.321)*

11. Monitoring and Diagnostics 
The summary is displayed. 
 To view the summary using the CLI: 
1. Go to configure oam cfm. 
2. Type in show summary. 
The summary is displayed. 
11.4 OAM (EFM) 
This section covers the monitoring of Ethernet links using link OAM (EFM) (OAM Ethernet at the First 
Mile).  can act as the active or passive side in an IEEE 802.3-2005 application. The link OAM can be 
activated for one  port at a time. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
IEEE 802.3-2005 
Benefits 
Link OAM provides remote management and fault indication for the Ethernet links, as well as detection 
of remote link failure. 
Functional Description 
The OAM (EFM) discovery process allows a local data terminating entity (DTE) to detect Ethernet OAM 
capabilities on a remote DTE. Once Ethernet OAM support is detected, both ends of the link exchange 
state and configuration information, such as mode, PDU size, loopback support, etc. If both DTEs are 
11. Monitoring and Diagnostics 
satisfied with the settings, OAM is enabled on the link. However, the loss of a link or a failure to receive 
OAMPDUs for five seconds causes the discovery process to restart.  
DTEs may be in either active or passive mode. DTEs in active mode initiate the OAM (EFM) 
communications and can issue queries and commands to a remote device. DTEs in passive mode 
generally wait for the peer device to initiate OAM communications, and respond to commands and 
queries, but do not initiate them. 
A flag in the OAMPDU allows an OAM entity to convey the failure condition Link Fault to its peer. Link 
Fault refers to the loss of signal detected by the receiver; a Link Fault report is sent once per second with 
the Information OAMPDU. 
Factory Defaults 
By default, OAM EFM is not enabled for the  ports.  
Configuring Link OAM 
The following parameters are configured for link OAM. 
Link OAM Parameters 
Parameter 
Description 
Web 
CLI 
OAM Mode 
mode 
Specifies active or passive mode 
OAM Port 
bind 
Port for which link OAM is active: 
• SFP/1 
• MSA/2. 
 
Note 
In order for link OAM to function, an L2CP profile must be defined with the 
OAM protocol action set to peer, and flow classification mode must be port 
mode or VID+Pbits Range, to enable attaching the L2CP profile to the relevant 
port/flow. 
11. Monitoring and Diagnostics 
Configuring Link OAM Using the Web Interface 
 To configure link OAM: 
1. Navigate to Configuration > OAM > Link OAM. 
2. If OAM (EFM) is disabled, the screen appears as shown in the following figures. 
 
  
 
 
 Configuration>OAM>Link OAM 
  
 
 
 OAM Mode 
 
Passive 
 Ingress Port 
 
SFP/Port 1 
  
 
 
 Enable 
 
 
  
 
 
Link OAM Disabled 
 
  
 
 
 Configuration>OAM>Link OAM 
  
 
 
 OAM Mode 
 
Passive 
 Ingress Port 
 
SFP/Port 1 
  
 
 
 Disable 
 
 
  
 
 
Link OAM Enabled 
1. To enable, select the mode and port, and then click Enable. 
2. To disable, click Disable. 
11. Monitoring and Diagnostics 
Configuring Link OAM Using the CLI 
 To configure link OAM: 
1. Navigate to configure oam efm. 
The config>oam>efm# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying for which port to activate 
link OAM 
bind ingress-port {sfp/1 | 
msa/2} 
 
Enabling loopback  
loopback 
Type no loopback to disable 
loopback 
Note: Available only in passive 
mode 
Specifying active or passive mode 
mode {active | passive} 
 
Enabling link OAM 
no shutdown 
Type shutdown to disable link 
OAM 
Displaying link OAM (EFM) status 
show status 
 
Clearing link OAM (EFM) statistics 
clear-statistics 
 
Displaying link OAM (EFM) statistics 
show statistics 
 
Examples 
 To enable active link OAM for port SFP/1: 
exit all  
configure oam efm 
  shutdown 
  mode active 
  bind ingress-port sfp/1 
  loopback 
  no shutdown 
  exit all 
 To display the link OAM status: 
>config>oam>efm# show status 
Administrative Status   : Enabled 

## 11.5 OAM (TWAMP)  *(p.325)*

11. Monitoring and Diagnostics 
Operational Status      : Send Local 
Loopback Status         : REMOTE 
 
OAM EFM Information 
-------------------------------------------------------- 
                Local                   Remote 
MAC Address     00-20-D2-51-42-52       -- 
OAM Mode        Active                  -- 
Unidirectional  Unsupported             -- 
Var Retrival    Unsupported             -- 
Link Events     Unsupported             -- 
Loopback        Supported               -- 
PDU Size        1518                    -- 
 To display the link OAM statistics: 
>config>oam>efm# show statistics 
OAM EFM Statistics 
-------------------------------------------------------- 
                        Rx              Tx 
Information             0               0 
Event Notification      0               0 
Loopback Ctrl           0               0 
Unsupported Codes       0 
11.5 OAM (TWAMP)  
MiNID provides up to 32 TWAMP Light Controller sessions that interoperate with TWAMP responders on 
other devices, by generating TWAMP test packets. You can display the session measurements and 
results. 
MiNID also provides up to 16 TWAMP Light responders that interoperate with TWAMP generators on 
other devices, by responding to TWAMP test packets with measurement packets.  
In addition, MiNID supports one-way loss TWAMP statistics. In order to calculate one-way packet loss, 
the following are required: 
• 
A responder that can generate an independent sequence number 
• 
A controller that is aware of the responder’s independent sequence number 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
11. Monitoring and Diagnostics 
Standards Compliance 
RFC 5357 – A Two-Way Active Measurement Protocol (TWAMP) 
Benefits 
You can measure the IP performance of your Layer-3 network at all locations, without the need for a 
special performance management system. 
Functional Description 
TWAMP Responders 
The TWAMP Light mechanism provides for monitoring sessions where information is exchanged 
between TWAMP controllers and responders. The controller establishes the test session with the 
responder, and then the controller transmits test packets to the responder, which reflects the test 
packets to the controller. The controller processes the resulting measurements and calculates metrics 
that can be displayed in test reports.  
The  TWAMP responders work in Layer-2 probe mode, meaning they are bound to layer-2 interfaces 
(port/flow). A responder can be bound to more than one flow. The association between a TWAMP 
responder and flow/port is performed from the flow/port menus/CLI in the same way that flow/port 
layer-3/4 loopbacks are configured (see Flows for details). You can view statistics for TWAMP looped 
packets and bytes by viewing the associated flow statistics for layer-3/4 loopbacks. 
Note 
The TWAMP Light responders work in non-standard mode, i.e. the parameters 
for the TWAMP Light responder session are configured manually in  via the 
web/CLI, rather than by TWAMP control protocol. 
You can configure the following parameters for a TWAMP controller. 
TWAMP Controller Parameters 
Parameter 
Description 
Web 
CLI 
Controller Name 
controller <controller-name> 
Name of TWAMP controller in , up to 32 characters 
11. Monitoring and Diagnostics 
Parameter 
Description 
Web 
CLI 
IP Address 
local-ip-address <router-
interface-1|router-interface-2| 
router-interface-3|router-
interface-4|router-interface-5> 
Router interface associated with the controller, from 
which you can send TWAMP test packets and ARP 
requests. 
 
Admin Status 
shutdown 
Administratively enable or disable the TWAMP 
controller 
You can configure the following parameters for a TWAMP responder. 
TWAMP Responder Parameters 
Parameter 
Description 
Web 
CLI 
Responder ID 
Not applicable 
Identification number assigned by MiNID, not 
user-configurable, displayed only in Web  
Responder Name 
responder <responder-name> 
Name of TWAMP responder in MiNID, up to 
32 characters 
TWAMP Local IP 
ip-address 
IP address (IPv4 or IPv6) associated with the responder, 
to which to send TWAMP test packets, ARP requests, or 
pings 
TWAMP UDP Port 
udp-port 
UDP port (range 1–65535) associated with responder  
Note: The combination of IP address and UDP port must 
be unique for each TWAMP responder. 
Use Loaned IP 
ip-loan 
If enabled,  responds only to TWAMP test packets sent 
to the TWAMP responder IP address, and does not 
respond to ARP/ping requests sent to the TWAMP 
responder IP address. This is useful if you have 
configured the responder with the same IP address as 
the  host device (i.e. the IP address was loaned from the 
host), and you want the host to answer ARP/ping 
requests. 
Admin Status 
shutdown 
Administratively enable or disable the TWAMP 
responder 
11. Monitoring and Diagnostics 
MAC Allocation Logic  
The following MAC addresses are available in the device: 
• 
Device Management MAC – used for MiNID management and for TWAMP sessions 1 and 3 
• 
Router Int 2,4 MAC address – used for TWAMP sessions 2 and 4 
• 
Device Services MAC address – used for OAM/CFM only (not for TWAMP). 
 
They can be seen in the CLI and in Web GUI as follows: 
MiNID 
  
 
 
 Monitoring - System 
  
 
 
 Device Management MAC address 00-20-D2-51-7E-2D 
 
 Router Int2,4 MAC address 
00-20-D2-51-7E-2F 
 
 Device Services MAC address 
00-20-D2-51-7E-2E 
 
 System Up Time (hh:mm:ss) 
05:35:48 
 
 DIP Switches Mode 
Normal 
 
  
 
 
 Current date 
10 May 2025 14:15:51+00:00 
 
 Summer time 
not configured 
 
  
 
 
 NTP 
 
 
 Events Log 
 
 
  
 
 
 
MiNID>config>system# show status 
Device Management MAC address    :      00-20-D2-E2-37-93 
Router Int 2,4 MAC address       :      00-20-D2-E2-37-94 
Device Services MAC address      :      00-20-D2-E1-B3-C6 
System UP Time (hh:mm:ss)        :      948:05:02 
DIP Switches Mode                :      NORMAL 
Factory Defaults 
By default, no TWAMP controllers or responders are configured.  
11. Monitoring and Diagnostics 
Configuring TWAMP 
 To configure TWAMP, perform the following steps: 
1. In the responder device: 
a. Configure relevant router interface and flows. 
b. Configure and activate TWAMP responder and relevant test session(s). 
2. In the controller device: 
a. Configure relevant router interface and flows. 
b. Configure TWAMP profile(s). 
c. Configure and activate TWAMP controller and relevant peers and test sessions. 
Profile is a set of properties that a TWAMP session has. You have to define at least one profile in order 
to define a TWAMP controller. 
Configuring TWAMP Controllers 
 To configure a TWAMP controller in the web interface: 
1. Navigate to Configuration > OAM > TWAMP > Controller. 
 
 
 
  
 
 
 
 
Configuration>OAM>TWAMP>Controller 
 
 
 
Add new Controller 
 
 
 
Controller 
Name 
 
 
 
 
 
Controller1 
Add Peer 
Show Peers 
Status 
Delete Controller 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Configuring TWAMP Controllers 
2. To add a new TWAMP controller: 
a. Click Add new Controller.  
11. Monitoring and Diagnostics 
 
 
 
 
 
Configuration>OAM>TWAMP>Controller>TWAMP Controller>New 
Controller 
 
 
 
 
Controller Name 
 
 
 
IP Address 
 
Router Interface 1 
 
Admin Status 
 
Disable 
 
 
 
Apply 
 
 
 
 
 
New TWAMP Controller 
b. Fill in the parameters as specified in the above figure.  
c. Click <Apply> to create the TWAMP controller. 
The Configuration>OAM>TWAMP Controller screen appears, with an entry containing the new 
TWAMP controller. 
3. Click Add Peer to define remote responder parameters in a TWAMP session.  
 
 
 
 
 
Configuration>OAM>TWAMP>Controller>Peer>TWAMP Peer> New Peer 
 
 
 
 
Peer IP 
 
0.0.0.0 
 
Activation 
 
OFF 
 
Responder Sequence Num 
 
OFF 
 
Calculation Mode 
 
Round-Trip 
 
 
 
Apply 
 
 
 
 
 
New TWAMP Peer 
a. Fill in the parameters as specified in the table below. 
b. Click <Apply> to create the peer. 
 To add or configure a TWAMP controller in the CLI: 
1. Navigate to configure oam twamp controller <controller-name> [<number>], where 
<controller-name> is the name of the controller and <number> is the controller ID number. 
The config>oam>twamp>controller(<controller-name>)# prompt is displayed. 
11. Monitoring and Diagnostics 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Administratively enabling or 
disabling the controller 
no shutdown 
Enter shutdown to administratively 
disable the controller. 
You should enable the controller only 
after the responder has been configured 
and enabled. 
Configuring controller IP 
address 
local-ip-address <router-interface-1|router-
interface-2| router-interface-3|router-
interface-4|router-interface-5> 
If Loaned IP is enabled on router 
interface #1, controller IP address can be 
configured on any other router interface 
Assigning an IP address to the 
remote responder (peer). 
peer <ip-address> 
See  Running Test Sessions via 
Controller Peers 
Viewing controller status 
show-status 
 
Running Test Sessions via Controller Peers 
Do one of the following: 
• 
In the web interface: 
a. Navigate to Configuration > OAM > TWAMP > Controller. 
b. In the row of the configured controller, click Show Peers.  
c. In the row of the selected peer, click Add Test Session. 
 
 
 
 
 
Configuration – OAM – TWAMP – Controller- Peer - Test Session - 
TWAMP Test Session - New Test Session 
 
 
 
 
Test Session Name 
 
 
 
TWAMP Profile 
 
<profile-name> 
 
Display Num 
 
0 
 
UDP Port 
 
0 
 
DSCP 
 
0 
 
 
 
Apply 
 
 
 
 
 
Configuring New Test Session 
a. Fill in the parameters as specified in the table below. 
11. Monitoring and Diagnostics 
b. Click <Apply> to create the test session. 
• 
In the CLI: 
a. Navigate to configure oam twamp controller <name>peer <ip-address>. 
The config>oam>twamp>controller (<name>)>peer(<ip-address>)# prompt is displayed. 
b.  Enter all necessary commands according to the tasks listed below. 
c. Enter all necessary commands according to the tasks listed below. 
Peer Parameters 
Task 
Command 
Comments 
Activating all configured test 
sessions in one-time mode 
activate 
activate duration <minutes> 
The tests run for the specified amount of 
time. 
Type no activate to deactivate the one-
time (non-continuous) command. 
Activating all configured test 
sessions in continuous mode 
activate continuous 
The tests run until they are stopped. 
Type no activate to deactivate the 
continuous command. 
Defining the type of calculation 
for the TWAMP metrics 
calculation-mode <round-trip> 
TWAMP controller calculates standard 
TWAMP metrics. 
Specifying whether the 
responder transmits an 
independent sequence number 
responder-seq-num 
Notes: 
The controller calculates one-way loss 
and availability only if this is enabled. 
The corresponding responder must be 
configured to transmit the responder 
sequence number. 
Configuring test session 
test-session <number> name 
<name-string> udp-port <udp-
port-number> test-profile 
<profile-name> dscp <dscp-
number> 
The UDP and DSCP can be used to 
distinguish between test sessions. 
UDP port number: 1-65535 
Test profile name: Up to 32 characters 
DSCP number: 0-63 (default: 0) 
 Viewing test report 
show-report <test-name> 
{interval|current|all} 
[<interval-num>] 
See Viewing TWAMP Reports 
Viewing summary of test 
reports 
show summary-report 
See Viewing TWAMP Reports 
Viewing test status 
show status 
See Viewing TWAMP Status 
11. Monitoring and Diagnostics 
 To delete a TWAMP controller: 
1. Navigate to configure oam twamp. 
2. Type no controller <controller-name>. 
Configuring TWAMP Profiles 
 To configure TWAMP profiles in the web interface: 
1. Navigate to Configuration>OAM>TWAMP>Profile. 
 
 
 
  
 
 
 
 
Configuration>OAM>TWAMP>Profile 
 
 
 
Add new Profile 
 
 
  
 
 
  
 
Profile 
Name 
 
 
Profile 1 
Delete Profile 
 
 
 
  
 
 
 
  
 
 
 
 
Configuring TWAMP Profiles 
2. To add a new TWAMP profile: 
c. Click Add new Profile. 
11. Monitoring and Diagnostics 
 
 
 
 
 
Configuration>OAM>TWAMP>Profile>TWAMP Profile>New Profile 
 
 
 
 
Profile Name 
 
 
Payload Length 
 
256 
 
Transmit Rate 
 
10 
 
Loss Timeout 
 
2000000 
 
Loss Ratio Threshold 
 
1000 
 
Delay Variation Threshold 
 
1000 
 
Delay Treshold 
 
1000 
 
Delay Variation Event Type 
 
pdv 
 
 
 
Apply 
 
 
 
 
 
New TWAMP Profile 
d. Fill in the parameters as specified in the table below. 
e. Click <Apply> to create the TWAMP profile.  
The Configuration>OAM>TWAMP>Profile screen appears, with an entry containing the new 
TWAMP profile. 
1. To delete a TWAMP profile, click Delete Profile in the corresponding row. 
The TWAMP profile is deleted. 
2. Click <Save Configuration>. 
 To add or configure a TWAMP profile in the CLI: 
1. Navigate to configure oam twamp profile <profile-name>, where <profile-name> is the name of 
the profile. 
The config>oam>twamp>profile(<profile-name>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
TWAMP Profile Parameters 
Task 
Command 
Comments 
Defining delay threshold in 
microseconds 
delay-threshold 
 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Configuring delay variation 
event type to define whether 
the PDV or IPDV metric is used 
for the delay threshold 
delay-variation-event-type 
pdv – Packet delay variation metric 
ipdv –Inter-packet delay variation metric 
Defining delay variation 
threshold in microseconds 
delay-variation-threshold 
 
Defining test packet loss 
timeout in microseconds 
loss-timeout  
 
Defining test session loss ratio 
threshold in ppm (packet per 
million) 
loss-ratio-threshold 
Range is 1000 – 10000 ppm 
Default: 1000 ppm 
Defining test packet payload 
length in bytes 
payload-length 
 
Defining test profile packet 
transmit rate in PPS 
transmit-rate <pps> 
 
 To delete a TWAMP profile: 
1. Navigate to configure oam twamp. 
2. Type no profile <profile-name>.  
The TWAMP profile is deleted. 
Configuring TWAMP Responders  
 To configure TWAMP responders in the web interface: 
1. Navigate to Configuration > OAM > TWAMP > Responder. 
11. Monitoring and Diagnostics 
 
 
 
 
  
 
 
 
Configuration – OAM – TWAMP - TWAMP Responder 
 
 
 
Add New TWAMP Responder Session 
 
 
 
 
 
 
 
 
 
ID 
Responder 
Name 
Admin 
Status 
TWAMP 
Local IP 
TWAMP 
UDP 
Port 
Tx 
Sequence 
Num 
Use 
Loaned IP 
 
 
 
 
 
1 
tw1 
Disable 
Session 
10.10.2.2 
3 
ENABLED 
ENABLED 
Status 
Unbind 
All 
Flows 
Delete 
Session 
 
 
2 
tw2 
Enable 
Session 
1.1.1.1 
5555 
DISABLED 
DISABLED 
Status 
Unbind 
All 
Flows 
Delete 
Session 
 
 
3 
tw3 
Enable 
Session 
10.10.2.2 
4 
DISABLED 
DISABLED 
Status 
Unbind 
All 
Flows 
Delete 
Session 
 
 
4 
tw4 
Disable 
Session 
2.2.2.2 
888 
ENABLED 
ENABLED 
Status 
Unbind 
All 
Flows 
Delete 
Session 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Configuring TWAMP Responders 
2. To add a new TWAMP responder:  
a. Click Add New TWAMP Responder Session.  
 
 
 
 
 
Configuration>OAM>TWAMP>Responder>TWAMP Responder>New 
Responder Session 
 
 
 
 
Responder ID 
 
5 
 
Responder Name 
 
 
 
IP Address 
 
 
UDP Port 
 
0 
 
Tx Sequence Num 
 
Enable 
 
Use Loaned IP 
 
Disable 
 
Admin Status 
 
Disable 
 
 
 
 
New TWAMP Responder 
 
11. Monitoring and Diagnostics 
b. Fill in the parameters as specified in See Peer Parameters table. 
c. Click <Apply> to create the TWAMP responder. 
The Configuration > OAM > TWAMP Responder screen (see above) appears, with an entry 
containing the new TWAMP responder. 
3. To enable or disable a TWAMP responder, click Enable Session/Disable Session in the 
corresponding row.  
4. To unbind all flows associated with a TWAMP responder, click Unbind All Flows in the 
corresponding row. 
5. To delete a TWAMP responder, click Delete Session in the corresponding row. 
6. The TWAMP responder is deleted, if it is administratively disabled and is not bound to any flows 
or ports. 
7. Click <Save Configuration>. 
 To add or configure a TWAMP responder with the CLI: 
1. Navigate to configure oam twamp responder <responder-name>, where <responder-name> is 
the name of the responder. 
The config>oam>twamp>responder(<responder-name>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning an IP address to the 
responder 
ip-address <ip-address> 
The address can be in either IPv4 or IPv6   
format. 
Specifying that the IP address 
assigned to the responder is 
loaned from the host device  
ip-loan 
Enter ip-loan for  to answer only 
TWAMP test packets sent to the IP 
address 
Enter no ip-loan for  to answer ARP/ping 
requests/TWAMP test packets sent to 
the IP address 
See Peer Parameters table for more 
details on IP loan  
Generating an independent 
sequence number for the 
TWAMP responder packets 
tx-sequence-num 
 
Administratively enabling or 
disabling the responder 
no shutdown 
Enter shutdown to 
administratively disable 
the responder 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Assigning a UDP port to the 
responder 
udp-port <udp-port> 
1–65535 
Unbinding any flows associated 
with the TWAMP responder 
unbind-all-flows 
 
 To delete a TWAMP responder: 
1. Navigate to configure OAM TWAMP. 
2. Type no responder <responder-name>. 
Viewing TWAMP Status 
You can view the following statuses using the CLI: 
• 
Controller status – show status in level config oam twamp controller 
• 
Responder status – show status in level config oam twamp responder 
• 
Status of peer test sessions – show-status in level config oam twamp controller peer. 
• 
The data is also available in the web interface: 
• 
Controller status – Navigate to the Controller page and click Status in the row of the 
corresponding controller 
• 
Responder status - Navigate to the Responder page and click Status in the row of the 
corresponding responder 
• 
Status of peer test sessions – Navigate to the TWAMP Peers page and click Status in the row of 
the corresponding peer. 
 To view controller status: 
MiNID>config>oam>twamp>controller(1)# show status 
IPPM Type                    : TWAMP Light 
Router Interface             : 1 
Controller Status            : Ready 
 To view responder status: 
MiNID>config>oam>twamp>responder(tw1)# show status 
IPPM Type                    : TWAMP Light 
Responder Status             : Ready 
11. Monitoring and Diagnostics 
 
Responder Name     UDP       Tx-Packets      Rx-Packets 
-------------------------------------------------- 
tw1                3         1107             1107 
 To view peer test status: 
MiNID>config>oam>twamp>controller(1)>peer(33.33.116.6)# show-status 
IPPM Type                    : TWAMP Light 
Activation Mode              : continuous 
Calculation Mode             : round-trip 
Start Time                   : 00:00:54 01-01-1970 
 
Controller Test-Name Peer          UDP   Status      Tx-Packets   Rx-Packets 
------------------------------------------------------------------------- 
1          1         33.33.116.6   5001   In Progress   1770       1770 
1          2         33.33.116.6   5002   In Progress   1770       1770 
1          3         33.33.116.6   5003   In Progress   1770       1770 
1          4         33.33.116.6   5004   In Progress   1770       1770 
1          5         33.33.116.6   5005   In Progress   1770       1770 
1          6         33.33.116.6   5006   In Progress   1770       1770 
1          7         33.33.116.6   5007   In Progress   1770       1770 
1          8         33.33.116.6   5008   In Progress   1771       1771 
Viewing TWAMP Reports 
TWAMP Metrics 
The  TWAMP controller calculates performance measurement metrics according to the received test 
packets for each peer and its active test sessions. The metrics are recalculated every minute. You can 
view the metrics for the current interval, selected interval, or all intervals by viewing the TWAMP report.  
When the TWAMP responder receives a test packet, it reflects the test packet after it adds an Rx stamp 
and a Tx stamp.  
When the TWAMP controller receives a test packet from the responder, it calculates the following:  
• 
Delay = Responder Rx stamp - Controller Tx stamp + Controller Rx stamp –Responder Tx stamp 
• 
Forward delay = Responder Rx stamp - Controller Tx stamp 
• 
Backward delay = Controller Rx stamp - Responder Tx stamp 
• 
Packet validity – determined by checking if the delay is less than the value configured by 
command loss-timeout. If so, the Rx valid count is incremented, otherwise the packet is 
dropped. 
11. Monitoring and Diagnostics 
The following table lists the metrics that are displayed in the TWAMP reports, subject to the restrictions 
specified above for the calculation modes. See Viewing the Metrics for instructions on viewing the 
reports and for examples of TWAMP reports. 
TWAMP Report Metrics 
Counter 
Description 
Availability Count (sec) 
Number of available seconds. A minute is declared as unavailable if it has 
more than 75% packet loss, therefore it is available if packet loss is 25% or 
less. When a minute is declared unavailable, the delay, delay variation, loss 
measurements, and their derived metrics are ignored for that minute. 
Availability Count Fwd/Back 
Number of available seconds. A minute is declared as unavailable if it has 
more than 75% packet loss, therefore it is available if packet loss is 25% or 
less. When a minute is declared unavailable, the delay, delay variation, loss 
measurements, and their derived metrics are ignored for that minute. These 
statistics are for the forward and backward directions.  
Note: These statistics appear only when responder seq-num is enabled.  
Delay Average (ms) 
Average of packet delay values 
Delay Max (ms) 
Maximum of packet delay values 
Delay Min (ms) 
Minimum of packet delay values 
Delay Threshold Crossing 
Count 
Number of packets with delay larger than the delay threshold configured for 
the corresponding test profile 
Duplicate Packets Back 
Number of duplicate packets in backward direction. A packet is considered 
duplicate (backward) if its responder Tx timestamp matches that of a 
previously received packet in backward direction. 
Duplicate Packets Fwd  
Number of duplicate packets in forward direction. A packet is considered 
duplicate (forward) if its controller sequence number or controller Tx 
timestamp matches that of a previously received packet in forward direction. 
Duplicate Ratio Back  
Duplicate Packets Back divided by Tx Packets Back, converted to a percentage 
Duplicate Ratio Fwd  
Duplicate Packets Fwd divided by Tx Packets Fwd, converted to a percentage 
Fragmented Packets Back  
Number of fragmented packets in backward direction. When the TWAMP 
controller recognizes a fragmented packet, it increments the Fragmented 
Packets Back counter. 
11. Monitoring and Diagnostics 
Counter 
Description 
Fragmented Packets Fwd  
Number of fragmented packets in forward direction. When the TWAMP 
responder receives a fragmented packet, when it reflects it to the controller, 
the responder sends indication of fragmentation, if tx-extended-info was 
enabled. When this indication is received, the controller increments the 
Fragmented 
Packets Fwd counter. 
IPDV Average (ms)  
Average of IPDV (Inter Packet Delay Variation) values in both directions 
IPDV Max (ms)  
Maximum of IPDV (Inter Packet Delay Variation) values in both directions. 
Inter Packet Delay Variation is calculated according to RFC 5481, from the 
variations of the delays between valid packets. 
IPDV-Back Average (ms) 
Average of IPDV (Inter Packet Delay Variation) values in backward direction 
IPDV-Back Max (ms) 
Maximum of IPDV (Inter Packet Delay Variation) values in backward direction 
IPDV-Fwd Average (ms)  
Average of IPDV (Inter Packet Delay Variation) values in forward direction 
IPDV-Fwd Max (ms)  
Maximum of IPDV (Inter Packet Delay Variation) values in forward direction 
Loss Packets 
Number of packets lost 
Loss Packets Fwd/Back 
Number of packets lost in each of the directions, calculated by Tx Packets –Rx 
valid count  
Note: These statistics appear only when responder seq-num is enabled. 
Loss Ratio 
Loss Packets divided by Tx Packets, converted to a percentage 
Loss Ratio Fwd/Back 
Loss Packets divided by Tx Packets, converted to a percentage in each of the 
directions 
Note: These statistics appear only when responder seq-num is enabled. 
PDV Average (ms) 
Average of PDV (Packet Delay Variation) values, calculated by subtracting 
Delay Min from Delay Average 
PDV Max (ms)  
Maximum of PDV (Packet Delay Variation) values. Packet Delay Variation is 
calculated according to ITU-T Y.1540, by subtracting the minimum delay from 
the 99.9% percentile of the delay values 
Reordered Packets Back  
Number of reordered packets in backward direction. A packet is considered 
reordered (backward) if its responder sequence number is smaller than that 
of a previously received packet in backward direction. 
Reordered Packets Fwd  
Number of reordered packets in forward direction. A packet is considered 
reordered (forward) if its controller sequence number or controller Tx 
timestamp is smaller than that of a previously received packet in forward 
direction. 
11. Monitoring and Diagnostics 
Counter 
Description 
Reordered Ratio Back 
Reordered Packets Back divided by Tx Packets converted to a percentage 
Reordered Ratio Fwd 
Reordered Packets Fwd divided by Tx Packets converted to a percentage 
Tx Packets 
Number of packets transmitted in forward direction (controller to responder) 
Tx Packets Fwd/Back 
Number of packets transmitted forwared (from controller to responder) and 
back (from responder to controller) 
Note: These statistics appear only when responder seq-num is enabled. 
Viewing the Metrics 
You can view the following reports in level config oam twamp controller peer: 
• 
Summary report of all peer test sessions –show-summary-report 
• 
Test report of a particular session: 
 
Test report of all intervals – show-report <name> all 
 
Test report of current interval – show-report <name> current 
 
Test report of selected interval – show-report <name> interval <interval-num> 
 To view a summary report: 
MiNID>config>oam>twamp>controller(1)>peer(33.33.116.6)# show-summary-report 
IPPM Type                    : TWAMP Light 
Controller IP Address        : 33.33.116.4 
Responder IP Address         : 33.33.116.6 
Activation Mode              : continuous 
Calculation Mode             : round-trip 
 
Controller Test-Name  IP   Size    Loss     Delay    PDV      IPDV     Result 
                      DSCP         Ratio    Max      Max      Max 
                           (bytes)          (ms)     (ms)     (ms) 
----------------------------------------------------------------------------- 
1           1         1     256     0        1.891   0.246    1.790    NA 
1           2         1     256     0        0.321   0.147    0.221    NA 
1           3         1     256     0        0.390   0.173    0.290    NA 
1           4         1     256     0        0.374   0.176    0.274    NA 
1           5         1     256     0        0.301   0.144    0.201    NA 
1           6         1     256     0        0.351   0.164    0.250    NA 
1           7         1     256     0        1.889   0.092    1.789    NA 
1           8         1     256     0        0.316   0.181    0.216    NA 
 

## 11.6 Packet Capture  *(p.343)*

11. Monitoring and Diagnostics 
 To view a test report: 
MiNID>config>oam>twamp>controller(1)>peer(2.2.2.2)# show-report 1 all 
Test Name                    : 1 
IPPM Type                    : TWAMP Light 
Controller IP Address        : 33.33.116.4 / 1229 
Responder IP Address         : 33.33.116.6 / 5001 
IP DSCP                      : 11 
Payload Length (bytes)       : 256 
Calculation Mode             : round-trip 
Test Session Start Time      : 00:00:54 01-01-1970 
 
Test Interval                       : Current 
Elapsed Time                   (sec): 420 
 
Tx Packets                          : 4200 
Loss Packets                        : 0 
Loss Ratio                          : 0 
Availability Count             (sec): 420 
Tx Packets         Fwd / Back       : 0           0 
Loss Packets       Fwd / Back       : 0           0 
Loss Ratio         Fwd / Back       : 0           0 
Availability Count Fwd / Back  (sec): 0           0 
Duplicate Packets  Fwd / Back       : 0           0 
Duplicate Ratio    Fwd / Back       : 0           0 
Reordered Packets  Fwd / Back       : 0           0 
Reordered Ratio    Fwd / Back       : 0           0 
Fragmented Packets Fwd / Back       : 0           0 
 
Delay Threshold Crossing Count      : 1 
Delay      Min / Max / Average (ms) : 0.099           1.891           0.101 
PDV              Max / Average (ms) : 0.182           0.002 
IPDV             Max / Average (ms) : 1.790           0.002 
IPDV-Fwd         Max / Average (ms) : 0.002           0.000 
IPDV-Back        Max / Average (ms) : 1.790           0.002 
11.6 Packet Capture 
MiNID sends packets to a PC running Wireshark or another packet analyzer supporting RPCAP. Then the 
traffic can be recorded and analyzed on the PC. 
Performance was tested with Wireshark version 1.12 and 2.0.3. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
11. Monitoring and Diagnostics 
Standards Compliance 
RPCAP – Remote Packet Capture 
Benefits 
MiNID  can replace an equipped PC running Wireshark or dumpcap (Wireshark’s CLI) that is required at 
the viewing point.  MiNID captures bidirectional traffic and sends it to a packet analyzer running on a 
remote PC over IP/UDP/RPCAP. By configuring the analyzer filters, you can troubleshoot your network, 
analyze traffic, and use the data for software and communications protocol development. 
By applying relevant traffic filters,  tunnels only selected packets, thus reducing the network workload 
and preventing the PC from collapsing when there is a large number of packets. 
Functional Description 
MiNID enables you to capture real-time traffic and to transport it to a remote viewing /recording 
station. The station running Wireshark initiates the RPCAP tunneling session from the MiNID. 
MiNID can manipulate the captured traffic by editing or discarding frames. All flow actions are 
supported. 
The following scenario and example illustrate how packet capturing is performed. 
The user wishes to perform the flow action of push VLAN between the two ports of SFP and MSA):  
• 
If the user has defined the packet capture on one of the ports (for example, the SFP port), and 
the traffic arrives from the SFP (in the direction of the MSA), the user sees the captured packets 
before the push VLAN flow action has been performed.  
• 
If the traffic arrives from the MSA (in the direction of the SFP), the user sees the packets 
captured after the push VLAN flow action has been performed. 
Note 
Some of the traffic processed by  is not captured; only traffic passing through  
is captured. The feature of packet capture does not mirror traffic, such as 
OAM packets, which is addressed to  itself. 
 
Note 
Packet Capture applies to the IP address of the relevant router interface. 
11. Monitoring and Diagnostics 
It is possible that timestamping of the captured traffic is altered due to synchronization with the NTP 
server clock. To prevent the time amendments during packet capturing, usage of NTP as a clock source 
can be disabled by choosing the Free Run option. 
Factory Defaults 
By default, packet capturing is disabled. 
When packet capturing is enabled, it is configured as shown below. 
Parameter 
Default  
Remarks 
capture-dscp 
0 
DSCP value for the mirrored traffic 
local-ip-address 
router-interface-1 
Dedicated IP interface for packet capture 
rpcap-tcp-port 
2002 
TCP port number 
inactive-timeout 
5 
Packet capture session inactivity timeout in 
minutes 
timestamp-source 
freerun 
Source of timestamping for captured traffic 
Configuring Packet Capture 
Enabling Packet Capture 
 To enable packet capture using the web interface: 
1. Navigate to Configuration > Packet Capture. 
11. Monitoring and Diagnostics 
 
 
 
  
 
 
 
 
Configuration>Packet Capture 
 
 
 
 
Capture 
 
Disable 
 
 
 
 
 
Capture-
DSCP 
 
0 
 
 
 
 
 
Local IP Address 
Router Interface 1 
 
 
 
 
RPCAP TCP Port 
 
2002 
 
 
 
 
 
 
Inactive Timeout 
 
Enable 
 
 
 
 
 
Inactive Timeout [Min.] 
5 
 
 
 
 
Timestamp Source 
Free Run 
 
 
 
 
 
 
 
 
 
 
 
 
 
Show Status 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Apply 
 
 
 
 
 
 
 
 
 
 
Enabling Packet Capture 
1. Fill in the relevant parameters as described in the table below. Set the Capture status to Enable. 
2. Click <Apply>. 
 To enable packet capture using the CLI: 
1. Navigate to configure>packet-capture. 
The config>packet-capture# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Packet Capture Parameters 
Task 
Command 
Comments 
Enabling or disabling packet 
capturing 
[no] capture 
Type capture to administratively enable 
packet capturing 
Setting the DSCP value for the 
mirrored traffic 
capture-dscp 
Range [0-63] 
Defining packet capture session 
inactivity timeout in minutes 
[no] inactive-timeout 
When timeout period is over, packet 
capturing is disabled. 
Possible values: 1-65536 minutes 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Setting dedicated IP interface 
for packet capture 
local-ip-address <router-interface-1|router-
interface-2| router-interface-3|router-
interface-4|router-interface-5> 
If Loaned IP is enabled on router 
interface #1, packet capture can be set 
on any other router interface  
Setting the TCP port 
rpcap-tcp-port 
 
Displaying the status of the 
current Packet Capture session 
show status 
See Viewing  Statistics for Packet 
Capture 
Setting the source of 
timestamping for captured 
traffic 
timestamp source <freerun|ntp> 
freerun – internal clock is used as a 
timestamping source 
ntp – NTP server clock is used as a 
timestamping source 
Configuring a Wireshark Session 
You can have only one running Wireshark session. To open a new session, you have to close the previous 
one. 
 To define a new session: 
1. Open Wireshark. Click the Capture options 
 button on the Wireshark toolbar. 
The Capture Interfaces window opens. 
11. Monitoring and Diagnostics 
 
 
Capture Interfaces Window of Wireshark 
2. Click the Manage Interfaces button. 
The Manage Interfaces window opens. Switch to the Remote Interfaces tab. 
3. Click the + button in the bottom left to add a new remote interface.  
The Remote Interface window opens. 
11. Monitoring and Diagnostics 
 
Remote Interfaces Window of Wireshark 
4. Fill in the  local IP address (by default, 192.168.205.1) and TCP port (by default, 2002). Click OK. 
Two new interfaces are added. 
11. Monitoring and Diagnostics 
 
Adding  Ports as Remote Interfaces 
5. Select both  ports. For each of the ports, click the Remote Settings button. 
The Remote Capture Settings window opens. 
6. Under Capture Options, select Use UDP for data transfer. Click OK. 
 
Remote Capture Settings 
7. Close the Manage Interfaces window by clicking OK. 
11. Monitoring and Diagnostics 
Both  ports appear in the list as remote interfaces. 
8. In the Capture Interfaces window, select one of the  ports by clicking on its row.  
9. Click the Start button to initiate packet capturing. 
 
Starting a Session 
Wireshark starts to display all traffic in the main window. 
11. Monitoring and Diagnostics 
 
 
Captured Traffic in Wireshark Window 
10. To end the session, click the Stop capturing packets 
 button on the Wireshark toolbar. 
Configuring Display Filters in Wireshark 
In addition to capturing the whole traffic, you can apply various filters to choose only specific type of 
traffic. 
Note 
MiNID supports filtering of IPv4 packets. IPv6 packets are ignored. 
 
11. Monitoring and Diagnostics 
 To define a display filter: 
1. Click the Capture options 
 button on the Wireshark toolbar. 
The Capture Interfaces window opens. 
2. In the Capture filter for selected interfaces field, type the filtering criteria. For displaying only 
one host, type host <host-IP>. Click Start. 
 
Now Wireshark displays only traffic coming from and arriving to the host with the specified IP. 
11. Monitoring and Diagnostics 
 
Captured Traffic with a Filter Applied 
The following filtering criteria can be added: 
Filters Applied to Captured Traffic 
Criteria 
Command 
Comment 
Traffic coming from 
and to a selected host 
host <host-ip> 
ARP and reverse ARP packets for the 
host are captured as well, when only 
IP address is specified. 
This parameter is required to get a 
correct filter expression 
Traffic coming from a 
selected host 
src host <host-ip> 
 
11. Monitoring and Diagnostics 
Criteria 
Command 
Comment 
Traffic arriving to a 
selected host 
dst host  <host-ip> 
 
Applied protocol 
<protocol name> 
IP traffic includes only IPv4 packets, 
not IPv6 packets. Protocol name 
should be paired with ipv4 
Example: 
tcp and ipv4 
Port used in a source 
host 
src port <port number> 
 
Port used in a 
destination host 
dst port <port number> 
 
 
Note 
You can define up to two filter expressions concatenated by or. The 
parameters within a filter expression are joined by and.  
Example:  
(src host 1.1.1.1 and dst host 4.4.4.4  
and tcp src port 1025 and tcp dst port 2050) 
or 
(src host 4.4.4.4 and dst host 1.1.1.1 
and tcp src port 2050 and tcp dst port 1025) 
Configuring Packet Truncation 
MiNID enables you to take only the most important data (start of a packet) and pass it to the viewing 
station. The truncated packet size should be specified in Wireshark. The software displays the full packet 
size if you specify the size of the truncated file more than 12,000 bytes. If the value is less than 32 bytes 
or more than 255 bytes, Wireshark displays an error message. 
 To display truncated packets: 
1. In Wireshark, open the Capture Interfaces window. 
2. In the row of the selected  port, double-click the Snaplen (B) field to open it editing.  
3. Type the desired file size to be captured in the range of 32-255 bytes. Click Start. 
Wireshark displays truncated packets. 
11. Monitoring and Diagnostics 
Viewing  Statistics for Packet Capture 
 To view statistics in: 
1. In the web interface, click Show Status in the Packet Capture page. 
2. In the CLI, navigate to config> packet-capture and type show status. 
Relevant statistic parameters are displayed. 
Capture state             : In Progress 
Destination address       : 192.168.205.55 
Encapsulation protocol    : RPCAP 
TCP port                  : 2002 
UDP port                  : 59093 
 
--------------------------------------------------------- 
Capture port              : 1 
Capture packet size       : First 255 Bytes 
Start                     : 02:37:01 01-01-1970 
End                       : N/A 
Elapsed time              : 00:09:49 
Tx packets                : 54 
 
Capture rule #1 
--------------------------------------------------------- 
Pass All 
 
Capture rule #2 
--------------------------------------------------------- 
Pass All 
Packet Capture Status 
Parameter 
Value 
Description 
Capture State 
in progress|ready|disabled 
• In progress – Wireshark 
session is running 
• Ready – Wireshark 
session is completed 
• Disabled – capturing is 
administratively disabled 
in  
Destination Address 
<ip-addresss> 
 
Encapsulation protocol 
RPCAP 
 
TCP port 
<tcp-port-number> 
 
UDP port 
<udp-port-number> 
 

## 11.7 Ping  *(p.357)*

11. Monitoring and Diagnostics 
Parameter 
Value 
Description 
Capture port 
<port name/number> 
 
Capture packet size 
First X bytes|Whole packet 
Shows the number of bytes 
in case of of truncated 
packets or writes about 
whole packet 
Start 
hh:mm:ss dd-mm-yyyy 
Start time of session 
End 
hh:mm:ss dd-mm-yyyy 
End time of session 
Elapsed time 
hh:mm:ss 
Time period from the session 
start 
Tx packets 
<packets number> 
Number of packets 
processed during the session 
Capture rule #1 
 
See filters in the table above 
Capture rule #2 
 
See filters in the table above 
11.7 Ping 
MiNID can initiate a ping to test whether the host is reachable across the IP network.  
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Benefits 
 Can verify communication with the host and other devices. 
Factory Defaults 
The default number of packets sent for the ping test is 5. 
11. Monitoring and Diagnostics 
Configuring Ping Test 
 To initiate a ping using the web interface: 
1. Navigate to > Utilities> Ping. 
 
 
2. In the Destination IP address field, type in the IP address. 
3. In the Number of packets field, type in the number of packets you want the MiNID to send. 
4. Click <Apply>. 
11. Monitoring and Diagnostics 
 
 
5. Click <Stop ping> to stop the ping test. 
 To initiate a ping using the CLI: 
• 
In the command line, type ping <ip address> [number-of-packets <packets>].  
Example 
MiNID# ping 162.35.158.2 number-of-packets 6 
Reply from 162.35.158.2: bytes=32, packet number=1, time<1ms 
Reply from 162.35.158.2: bytes=32, packet number=2, time<1ms 
Reply from 162.35.158.2: bytes=32, packet number=3, time<1ms 
Reply from 162.35.158.2: bytes=32, packet number=4, time<1ms 
Reply from 162.35.158.2: bytes=32, packet number=5, time<1ms 
Reply from 162.35.158.2: bytes=32, packet number=6, time<1ms 
6 packets transmitted. 6 packets received. 0% packet loss 
Round Trip <ms> min/avg/max= 0/0/0  
 

## 11.8 RFC-2544 Responder  *(p.360)*

11. Monitoring and Diagnostics 
11.8 RFC-2544 Responder 
 MiNID provides an RFC-2544 responder that allows you to test the link at full capacity, and handles up 
to 1Gbps of traffic. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
RFC-2544, Benchmarking Methodology for Carrier Ethernet Networks 
Benefits 
You can evaluate the performance of network devices to provide performance metrics of the Ethernet 
network and validate the SLA. 
Functional Description 
The RFC-2544 responder uses OAM CFM loopback messages (LBM) and loopback replies (LBR). 
Configuring RFC-2544 Responder 
 To use the RFC-2544 responder: 
1. In MiNID, create a MEP with the appropriate MD level, MA ID, and VLAN (refer to OAM (CFM)  
for details on configuring MEPs). 
2. To start the RFC-2544 test, send LBM frames towards the MEP in the desired rate, with the MD 
level, MA ID, and VLAN that correspond to the MEP. 
3. To start RFC-2544 latency tests, send DMM frames towards the MEP, with the MD level, MA ID, 
and VLAN that correspond to the MEP. 

## 11.9 Syslog  *(p.361)*

11. Monitoring and Diagnostics 
11.9 Syslog 
MiNID uses the Syslog protocol to generate and transport event notification messages over IP networks 
to Syslog servers. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
RFC 3164, RFC 5674 
Benefits 
Syslog protocol collects heterogeneous data into a single data repository. It provides system 
administrators with a single point of management for collecting, distributing and processing audit data. 
Syslog standardizes log file formats, making it easier to examine log data with various standard tools. 
Data logging can be used for: 
• 
Long-term auditing 
• 
Intrusion detection 
• 
Tracking user and administrator activity 
• 
Product operation management 
Functional Description 
The Syslog protocol provides an instrument for generating and transporting event notification messages 
from MiNID to servers across IP networks. 
11. Monitoring and Diagnostics 
Elements 
Typical Syslog topology includes message senders (devices) and message receivers (servers). MiNID 
supports up to five Syslog servers. The receiver displays, stores, or forwards logged information. The 
standard designates two types of receivers: 
Relay 
Forwards messages 
Collector 
Displays and stores messages 
Transport Protocol 
Syslog uses User Datagram Protocol (UDP) for its transport. The UDP port assigned to Syslog is 514, but 
devices and servers can be defined to use any port for communication. 
Message Format 
The length of a Syslog message is 1024 bytes or less. It contains the following information: 
• 
Facility and severity (see below) 
• 
Host name or IP address of the device 
• 
Timestamp 
• 
Message content 
A typical Syslog message looks like this: 
<145>Jan 15 13:24:07 172.17.160.69 Eth 1: Loss of signal (LOS) 
Facilities and Severities 
Facility designates a device or application that sends a message. The standard includes some predefined 
facilities in the 0–15 range. For originator identification, MiNID uses facilities local1– local7. 
Severity is assigned to a message to specify its importance. MiNID uses the following severity 
designations: 
Syslog Severities 
Code 
Syslog Type 
Description 
0 
Emergency 
Emergency message 
1 
Alert 
Critical alarm 
11. Monitoring and Diagnostics 
Code 
Syslog Type 
Description 
2 
Critical 
Major alarm 
3 
Error 
Minor alarm 
4 
Warning 
Event 
5 
Notice 
Cleared alarm 
6 
Informational 
Informational message, not in use 
7 
Debug 
Debug-level messages, not in use 
 
Note 
The Syslog operation is not supported if  uses a loaned IP address. 
Factory Defaults 
By default, Syslog operation is disabled. When enabled, the default parameters are as follows: 
Parameter 
Default Value 
facility 
local1 
port 
514 
severity-level 
informational 
Configuring Syslog Parameters 
When configuring Syslog parameters, it is necessary to define Syslog device and servers. 
 To configure Syslog device in the CLI: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. Enter the necessary commands according to the tasks listed below. 
11. Monitoring and Diagnostics 
Syslog Configuration Parameters 
Task 
Command 
Comments 
Defining a facility from which Syslog 
messages are sent 
facility {local1 | local2 | local3 | 
local4 | local5 | local6 | local7} 
Defining Syslog device UDP port for 
communication 
port <udp-port-number> 
Possible values: 1–65535 
Port configuration is allowed 
only if a Syslog device is 
administratively disabled. 
Defining severity level 
severity-level { emergency | alert | 
critical | error | warning | notice | 
informational | debug} 
The log messages that contain 
severity level above or equal to 
the specified level are 
transmitted. 
Administratively enabling Syslog device 
no shutdown 
shutdown administratively 
disables the Syslog device. 
Displaying statistics 
show statistics 
Clearing statistics 
clear-statistics 
 To configure a Syslog server in the CLI: 
1. Navigate to configure system). 
The config>system# prompt is displayed. 
2. At the config>system# prompt, enter syslog server <server-ID> to specify the server to receive 
Syslog messages, where <server-ID> is 1 to 5. 
The config>system>syslog(<server-ID>)# prompt is displayed. 
3. Enter the necessary commands according to the tasks listed below. 
Syslog Server Parameters 
Task 
Command 
Comments 
Enabling logging of command entries  
accounting commands 
To disable command logging, 
enter no accounting commands 
Defining Syslog server IP address 
address <ip-address> 
Possible values: 
0.0.0.0–255.255.255.255 
Defining Syslog server UDP port for 
communication 
port <udp-port-number> 
Possible values: 1–65535 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Administratively enabling Syslog server 
no shutdown 
shutdown administratively 
disables Syslog server. 
 To configure Syslog device in the web interface: 
1. Go to Configuration > System > Syslog. 
 
  
 
 
 Configuration – System - Syslog 
  
 
 
 Device Configuration: 
 
 
 Facility 
Local1 
 
 Severity Level 
informational 
 
 Port 
514 
 
 Admin Status 
Disable 
 
  
 
 
 Apply 
 
 
  
 
 
 Server Configuration 
 
 
 
Server ID 
Address 
Accounting Commands 
Port 
Admin Status 
 
 
1 
FE80:B5BA:59E4:1A3D:F3CD 
ENABLED 
514 
ENABLED 
 
 
2 
192.168.205.55 
ENABLED 
514 
ENABLED 
 
 
3 
192.168.205.2 
ENABLED 
514 
ENABLED 
 
 
4 
0.0.0.0 
DISABLED 
514 
DISABLED 
 
 
5 
0.0.0.0 
DISABLED 
514 
DISABLED 
 
  
 
 
 Statistics: 
 
 
 Total Tx Messages 
356 
 
 Non-queued Dropped Messages 
10 
 
 Clear Statistics 
 
 
  
 
 
Syslog Configuration 
2. Set the device configuration according to Syslog Server Parameters table. 
3. Click <Apply>. 
11. Monitoring and Diagnostics 
 To configure a Syslog server in the web interface: 
1. Under Server Configuration, click the ID number of the server to receive Syslog messages. 
 
  
 
 
 Configuration – System - Syslog - Server Update 
  
 
 
 Server ID 
2 
 
 Address 
192.168.205.55 
 
 Accounting Commands 
Enable 
 
 Port 
514 
 
 Admin Status 
Enable 
 
  
 
 
 Apply 
 
 
  
 
 
1. Enter the necessary commands according to Syslog Statistic Parameters table. 
2. Click <Apply>. 
Viewing Syslog Statistics 
 To display Syslog statistics in the CLI: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. At the config>system>syslog(device)#, enter show statistics. 
Syslog statistics appear as shown below. The counters are described in the table below. 
MiNID>config>system>syslog(device)# show statistics 
Total Tx Messages  
 
: 356 
Non-queued Dropped Messages 
 
 
: 265 
Syslog Statistic Parameters 
Parameter 
Description 
Total Tx Messages 
The total number of Syslog messages transmitted 
11. Monitoring and Diagnostics 
Parameter 
Description 
Non-queued Dropped Messages 
The total number of Syslog messages that were dropped 
before being queued 
 To clear Syslog statistics in the CLI: 
1. Navigate to configure system syslog device. 
The config>system>syslog(device)# prompt is displayed. 
2. At the config>system>syslog(device)# prompt, enter clear-statistics. 
The Syslog statistic counters are set to 0. 
 
 To display Syslog statistics in the web interface:  
1. Go to Configuration > System > Syslog.  
2. Syslog statistics are displayed at the bottom. The counters are described in the table above.  
 To clear Syslog statistics in the web interface:  
1. Go to Configuration > System > Syslog. 
2. Click Clear Statistics.  
The Syslog statistic counters are set to 0. 
Example 
• 
Server IP address: 178.16.173.152 
• 
UDP port: 155 
exit all 
configure system  
  syslog device 
    no shutdown 
    exit 
  syslog server 1 
    address 178.16.173.152 
    port 155 
    no shutdown 
    save 
    exit all 

## 11.10 Detecting Problems  *(p.368)*

11. Monitoring and Diagnostics 
Configuration Errors 
The table below lists messages generated by MiNID when a configuration error is detected. 
Configuration Error Messages 
Message 
Description 
Syslog Port is out of range 
Selected UDP port value is out of allowed range (1–65535). 
Port is illegal or Device Port is already in 
use 
Selected UDP port is already in use. 
Parameter cannot be changed if Logging 
Status/Server Access is enabled 
Device/server UDP port or server IP address cannot be changed 
while Syslog server is enabled. 
Illegal Severity 
Invalid severity value 
Illegal Facility 
Invalid facility value 
Illegal Server IP Address 
Invalid server IP address 
11.10 Detecting Problems 
Alarms and Traps 
Alarms serve as notification of a fault in the device, and are indicated by an entry in the alarm and event 
history log, and/or an SNMP trap to a management station. See Handling Alarms and Events for further 
details on alarms, events, and traps. 
Statistic Counters 
Statistic counters provide information on possible abnormal behavior and failures. You can collect 
statistics on the following: 
• 
Flows 
• 
OAM CFM/EFM 
• 
SFP/MSA (sleeve) ports  

## 11.11 Handling Alarms and Events  *(p.369)*

11. Monitoring and Diagnostics 
For further information, refer to the relevant sections in Chapter 6 –10 and the relevant sections in the 
troubleshooting chart. 
11.11 Handling Alarms and Events 
This section describes how to display and clear the event log, and lists the  events and traps. 
Defining Alarm Types 
The alarm type can be defined as the “legacy” alarms or the new SOAM alarms supported by MEF 36. 
 To define the alarm type using the web interface: 
1. Navigate to Configuration > OAM > CFM. 
 
  
 
 
 Configuration>OAM>CFM 
  
 
 
 Alarm Type 
Legacy/SOAM 
 
  
 
 
 Add New MD 
 
 
  
 
 
  
 
 
 Apply 
 
 
  
 
 
1. Select the relevant alarm type: 
 
Legacy: Previous alarm set 
 
SOAM: New MEF 36 alarm set. This mode supports alarm suppression. 
 To define the alarm type using the CLI: 
1. Navigate to MiNID>config>oam>cfm#. 
2. Use the following command to select alarm type: 
11. Monitoring and Diagnostics 
 
alarm-type {legacy | soam} 
Working with the Event Log 
The event log contains the events that have occurred since the last startup of . The event log can hold up 
to 300 events. If it reaches that limit, further events are stored in a wraparound fashion, i.e. the later 
events overwrite the earlier events. The file entries are time-stamped with the time since the last 
startup. 
 To display the event log: 
Do one of the following: 
• 
In the web interface, go to Monitoring > System, and click Events Log:  
MiNID 
  
 
 
 Monitoring - System 
  
 
 
 Device Management MAC address 00-20-D2-51-7E-2D 
 
 Router Int2,4 MAC address 
00-20-D2-51-7E-2F 
 
 Device Services MAC address 
00-20-D2-51-7E-2E 
 
 System Up Time (hh:mm:ss) 
05:35:48 
 
 DIP Switches Mode 
Normal 
 
  
 
 
 Current date 
10 May 2025 14:15:51+00:00 
 
 Summer time 
not configured 
 
  
 
 
 NTP 
 
 
 Events Log 
 
 
  
 
 
Monitoring System 
11. Monitoring and Diagnostics 
MiNID 
 
 
 
 
 
 
Monitoring>System>Events Log 
 
 
 
 
 
 
Log Page 
 
1 
 
 
Time 
Event 
Severity 
Description 
 
00:04:38 
LOC 
MAJOR 
OFF, MEP [2.MA1.1.55] 
 
00:04:20 
LOC 
MAJOR 
ON, MEP [2.MA1.1.55] 
 
00:04:12 
UPLOAD FILE 
MINOR 
Upload log-file success via 
SFTP 
 
00:01:01 
TELNET MESSAGE 
MINOR 
CLI Parsing startup-config 
Success 
 
00:00:53 
LINK UP 
MAJOR 
SFP Port (sleeve) 
 
00:00:46 
LINK DOWN 
MAJOR 
SFP Port (sleeve) 
 
00:00:31 
LOGIN SUCCESS 
MAJOR 
User: su (telnet) 
 
 
 
 
 
 
Clear table 
 
 
 
 
 
 
 
 
Displaying Event Log 
• 
In the CLI, go to the configure reporting level, and enter show log. 
>config>report# show log 
Time         Event            Severity     Description 
--------------------------------------------------------- 
00:04:38     LOC              MAJOR        OFF, MEP [2.MA1.1.55] 
00:04:20     LOC              MAJOR        ON, MEP [2.MA1.1.55] 
00:04:12     UPLOAD FILE      MINOR        Upload log file success via SFTP 
00:01:01     TELNET MESSAGE   MINOR        CLI Parsing startup-config Success 
00:00:53     LINK UP          MAJOR        SFP Port (sleeve) 
00:00:46     LINK DOWN        MAJOR        SFP Port(sleeve) 
00:00:31     LOGIN SUCCESS    MAJOR        User: su (telnet) 
 To clear the event log: 
Do one of the following: 
• 
In the web interface, go to Monitoring > System> Log File as described in the above procedure 
to display the event log, and click Clear table. 
• 
In the CLI, go to the configure reporting level, and enter clear-log. 
>config>report# clear-log 

## 11.12 Performance Monitoring  *(p.372)*

11. Monitoring and Diagnostics
>config>report#
Alarm and Event Lists 
You can view the full lists of alarms and events supported by , along with the traps corresponding to 
each alarm or event.  
 To view the alarms table: 
•
Double-click the paperclip image on the following line.
 To view the events table: 
•
Double-click the paperclip image on the following line.
11.12 Performance Monitoring 
 maintains performance management (PM) statistics that are collected into a file periodically, for 
retrieval by RADview, for display in the RADview PM portal (refer to the RADview System User’s Manual 
for further details on the PM portal). The PM file can also be retrieved by a third-party network 
management system.  
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Benefits 
The PM data is useful for analyzing  service quality. The flexible statistics collection allows only the 
necessary data to be collected. 
11. Monitoring and Diagnostics
Functional Description 
PM statistics collection is configured globally for MiNID. When it is enabled,  collects PM data. When it is 
disabled,  deletes any PM data previously collected and stops collecting PM data. 
MiNID  stores PM data at user-configurable intervals (1, 5, 10, or 15 minutes). Additionally the interval 
for collecting the PM data from  can be configured to 1, 5, 10, or 15 minutes. 
Note 
•
If the PM file reaches 90% capacity,  sends the PM SPACE OVERFLOW
event; if PM data cannot be saved due to insufficient space,  stops
collecting PM data and sends the PM PROCESS DISABLED event
•
If performance monitoring is enabled, ensure that the data is collected by
RADview or a third-party NMS, otherwise one or both of the alarms is
triggered. If it is not possible to collect the data, then disable performance
monitoring.
Factory Defaults 
Parameter 
Default 
Remarks 
pm 
pm 
PM statistics collection in device is 
globally enabled by default 
interval-duration 
15 
PM interval is 15 minutes by 
default 
file-interval-duration 
5 
PM file is collected every 5 minutes 
by default 
Configuring Performance Monitoring 
 To configure PM collection: 
Do one of the following: 
•
In the web interface:
a.
Go to Configuration > System > Performance Monitoring.
b.
Set PM Mode to Enable or Disable.

## 11.13 Troubleshooting  *(p.374)*

11. Monitoring and Diagnostics
c.
Set PM Interval Duration to 1 Min, 5 Min, 10 Min, or 15 Min.
d.
Set PM File Interval Duration to 10 Sec, 1 Min, 5 Min, 10 Min, or 15 Min.
Note 
PM File Interval Duration must be less than or equal to PM Interval Duration. 
e.
Click <Apply> to implement the changes, and then click <Save Configuration>.
MiNID 
Configuration – System - Performance Monitoring 
PM Mode 
Enable 
PM Interval Duration 
15 Min 
PM File Interval Duration 
5 Min 
•
In the CLI:
a.
Go to the configure reporting context.
b.
Enter pm to enable PM collection, or no pm to disable PM collection.
c.
Enter the following to set the PM interval:
interval-duration {1 | 5 | 10 | 15}
d.
Enter the following to set the interval for collecting the PM data:
file-interval-duration {10s |1 | 5 | 10 | 15}
Note 
The value set by file-interval-duration must be less than or equal to the value 
set by interval-duration. 
11.13 Troubleshooting 
This section contains a general troubleshooting chart that lists possible failures and provides 
workarounds. 
•
Use this chart to identify the cause of a problem that may arise during operation. For a detailed
description of the LED indicator functions, refer to Chapter 3.

## 11.14 Frequently Asked Questions  *(p.375)*


## 11.15 Technical Support  *(p.375)*

11. Monitoring and Diagnostics 
To correct the reported problem, perform the suggested corrective actions. If a problem cannot be 
resolved by performing the suggested action, contact your RAD distributor. 
Fault/Problem 
Probable Cause 
Corrective Action 
The unit is unreachable 
Incorrect management settings 
Using a local serial connection, 
verify the management settings  
Management path disconnected 
In case of remote management, 
analyze this issue using a local 
serial connection 
Check network connectivity issues 
and firewall settings 
MiNID does not answer pings 
Ping packets are larger than 
128 bytes 
Send ping packets that are no 
larger than 128 bytes 
Physical link fails to respond 
Link may be administratively 
disabled. 
Administratively enable the link 
11.14 Frequently Asked Questions 
Q What do I need to configure in order to automatically distribute a configuration file to  via 
zero touch? 
A You need to configure the management VLAN and set DHCP to enable. You also need to set up 
the DHCP and TFTP servers as specified in the explanation of zero touch (for further details refer 
to Chapter 3). 
11.15 Technical Support 
For technical support of registered products, contact your local authorized RAD partner or go to 
RADcare Online (if you have a valid RADcare service package). 
RAD would like your help in improving its product documentation. Please send us an e-mail with your 
comments. 
Thank you for your assistance! 
 
11. Monitoring and Diagnostics 
 