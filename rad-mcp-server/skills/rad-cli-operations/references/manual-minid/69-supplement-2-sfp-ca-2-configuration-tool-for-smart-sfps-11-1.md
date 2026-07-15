# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.1 Layer-3 Service Activation Test

*Manual `MiNID_ver_2_6_mn.pdf`, pages 239–252.*


## Applicability and Scaling  *(p.239)*


## Standards Compliance  *(p.239)*


## Benefits  *(p.239)*


## Functional Description  *(p.239)*

11 Monitoring and Diagnostics 
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
 

## Factory Defaults  *(p.241)*

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

## Configuring L3 SAT Entities  *(p.242)*

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

## Viewing L3 SAT Status  *(p.250)*

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

## Viewing L3 SAT Test Reports  *(p.251)*

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