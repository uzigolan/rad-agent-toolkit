# Feature Reference – 8 Monitoring and Diagnostics – 8.8 Y.1564 Ethernet Service Activation Test

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1485–1535.*


## Applicability and Scaling  *(p.1485)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
exit all 
configure system  
  syslog device 
    facility local2 
    port 155 
    severity-level major 
no shutdown 
    exit 
  syslog server 1 
    address 178.16.173.152 
    port 155 
    no shutdown 
    save 
    exit all 
8.8 Y.1564 Ethernet Service Activation Test 
The Ethernet service activation test provides an out-of-service testing methodology to assess the proper 
configuration and performance of an Ethernet service prior to customer notification and delivery. This 
methodology allows service providers to have a standard way of measuring the performance of 
Ethernet-based services. The tests are performed per multiple traffic streams simultaneously, 
confirming policing per EVC or EVC.CoS. 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. 
Y.1564 is supported over Up MEPs and Down MEPS.  
Y.1564 over LAG is relevant for ETX-2i-10G and ETX-2i-100G only. 
ETX‑2i supports up to 64 generators, 64 responders, 64 simultaneous Y.1564 tests, and 64 test profiles. 
The following table shows the number of generators, responders, simultaneous tests, and test profiles 
per product: 
 
 

## Standards  *(p.1486)*


## Functional Description  *(p.1486)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
# Generators 
# Responders 
# Simultaneous Tests 
# Test Profiles 
ETX-2i 
8 
20 
8 
20 
ETX-2i-B 
8 
20 
8 
20 
ETX-2i-10G 
64 
64 
64 
64 
ETX-2i-100G/4Q 
8 
20 
8 
20 
The 8/64 generators and 20/64 responders can be activated over EVC, EVC.CoS, or a combination of EVC 
and EVC.CoS. The Y.1564 generator is limited to two VLANs; one MEP per generator. 
The rate of the Y.1564 traffic for a single generator/responder or several generators/responders running 
in parallel, cannot exceed 1 Gbps for ETX-2i, ETX-2i-B; 10 Gbps for ETX-2i-10G; 100Gbps for ETX-2i-100G. 
The test requires that the corresponding ingress and egress flows (or a bidirectional flow) be 
preconfigured at both ends. 
Standards 
ITU-T Y.1564 
Functional Description 
To assure quality of service (QoS), providers must properly configure their networks to define how the 
traffic is prioritized in the network. This is accomplished by assigning different levels of priority to each 
type of service and accurately configuring network prioritization algorithms. QoS enforcement refers to 
the method used to differentiate the traffic of various services via specific fields in the frames, thus 
providing better service to some frames over other ones.  
SLAs 
The service-level agreement (SLA) is a binding contract between a service provider and a customer, 
which guarantees the minimum performance that is assured for the services provided. 
Customer traffic is classified into three traffic classes, and each is assigned a specific color: green for 
committed traffic, yellow for excess traffic, and red for discarded traffic. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Policing 
ETX‑2i can set different traffic policing parameters. When a Policer is activated, it monitors the incoming 
frames and determines their color mode (CM). If CM is set to color aware, ETX‑2i monitors incoming 
frames and assigns them the relative color (green or yellow) based on the frame header matching the 
Policer setting and current information rate. 
Note 
• 
When the Y.1564 test is configured as bidirectional, it may fail if the 
Policer profiles for the directions generator->responder and responder-
>generator are different. For instance, the test could fail if a Policer profile 
is defined for the Rx and Tx flows in the generator, and the bandwidth of 
the ingress Policer is lower than that of the egress Policer. 
• 
You should configure a non-default Policer profile for the Tx flow and 
configure no profile for the Rx flow. 
• 
If multiple Tx flows are attached to the same MEP in the responder, any 
Policer profile attached to the Tx flows is not used in the responder egress 
direction (back towards the generator). 
• 
The Y.1564 generator discovers the test rate per service or service.CoS 
Policer, even when the Policer is not an aggregate Policer. 
Blocking User Traffic 
By default, user traffic on the flows associated with the test is automatically blocked by the device from 
the time a test is activated until it is completed. You can leave this default or configure the test to allow 
user traffic on the flows associated with the test. 
Y.1564 over LAG 
Note 
Y.1564 over LAG is relevant for ETX-2i-10G and ETX-2i-100G only. 
When LAG exists on the network path, Y.1564 is limited in its ability to test the full path SLA of the EVC. 
To overcome this limitation, ETX-2i-10G and ETX-2i-100G support changing the source MAC address (SA) 
in each transmitted frame (instead of the default, where the SA of the test frame is automatically 
inherited from the port that the associated MEP is bound to), so that the frames pass through all the 
links in the network LAG.  
In the Y.1564 test profile, you can select this operation mode, by setting a block of 32 consecutive MACs 
as SA. The SAs of generated test frames are then cyclically selected from the block of 32 consecutive 
MAC addresses. By default, 0x0020D2000100 is the first MAC address in the block of MACs used as SA in 
test frames. However, you have the option of setting another first address, provided it is a multiple of 
32.    
ETX-2i Devices 
8. Monitoring and Diagnostics 
When the hashing function of the network LAG is set to SA+DA MAC, the Y.1564 frames pass through all 
the links of the LAG, enabling testing the SLA of the different links. 
Router
ETX-2i-10G
L2
Network
Y.1564 Gen
LAG (SA+DA MAC HASH)
 
Y.1564 over LAG 
Y.1564 Standard 
The ITU-T Y.1564 testing methodology ensures that quality is maintained across networks with multiple 
streams and different policing parameters. Service providers use the SAC (Service Acceptance Criteria) 
information which is normally based on a subset of the users SLA to set pass/fail parameters. 
There are two main objectives: 
• 
To validate that each Ethernet-based service is correctly configured 
• 
To validate the quality of the services as delivered to the end user 
The test flowchart below illustrates the test phases. 
Enter test 
parameters
Start test
Service 
configuration 
test
Troubleshoot 
service 
configuration
Service 
performance 
test
Test completed
Fail
Pass
Pass
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuration Test 
The configuration test validates that services are configured as intended before proceeding to the 
service performance test. Each service is tested individually and the information rate (IR), Frame 
Transfer Delay (FTD), Frame Delay Variation (FDV), and Frame Loss Ratio (FLR) are measured 
simultaneously. The test is declared successful if the information rate and frame counters are within the 
Service Acceptance Criteria (SAC). 
The configuration test consists of the following procedures (mandatory to implement and optional to 
perform): 
• 
CIR (simple or stepped) 
• 
EIR (color-blind) 
• 
Traffic policing (color-blind); can be disabled 
In addition, the configuration test consists of the following burst test procedures (optional to 
implement): 
• 
CBS (color-aware or color-blind) 
• 
EBS (color-aware or color-blind) 
The CBS and EBS burst sub-tests can be disabled (the default) or enabled. These tests cannot coexist 
with another configuration test; if they do, a sanity error occurs. However, they can coexist with other 
running performance tests. 
A burst sub-test (CBS, EBS) consists of at least one transmission cycle. If needed, the actual duration of a 
burst sub-test is automatically extended i.e., by increasing the total duration of the configuration test. 
Performance Test 
The performance test validates the quality of the services over a user-configurable period of time 
(one minute to five days). Traffic is generated for all services at configured CIR levels; all Ethernet 
performance parameters are measured simultaneously. The bandwidth test is performed according to 
the bandwidth profile of a Policer assigned to the associated flow, or a Policer assigned to the test. 
 
Note 
• 
If there are two bandwidth profiles (flow and test), the test bandwidth 
profile is used. 
• 
OAM relevant packets are calculated as part of the test bandwidth. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Test Elements 
The Y.1564 test is an intrusive procedure that includes two main elements: 
• 
Generator – an entity that initiates the test, sends out the test and OAM frames, receives 
responses from the responder, processes the resulting measurements and displays test reports. 
In the case of a MEF46 LL responder, the generator executes the Latching Loopback (LL) 
controller functionality. 
• 
Responder – an entity that receives the test and OAM frames from the generator and transmits 
a response to the generator. The responder can be of the following types: 
 
Regular responder – adds time stamps to the OAM frames that it returns to the generator 
 
MAC swap responder – does not add time stamps to the OAM frames that it returns to the 
generator 
 
MEF46 Latching Loopback responder – Upon receiving LLM from the generator, replies with 
LLRs. OAM frames are not looped back. 
While performing/running the Y.1564 test, the responder does not transmit PM packets. 
The test operation can be configured as unidirectional or bidirectional (the default). When bidirectional, 
service performance is measured on the frames that make a round trip (generator > receiver > 
generator). 
PSN
Generator
Forward
Responder
Backward
 
Y.1564 Test Elements 
Test Cases 
The Y.1564 test supports two cases: 
Internal MEP case 
Supported for E-Line, E-LAN, and E-Tree services over PTP or Bridge, 
in which MEPs are not preconfigured 
Service MEP case 
Full support over point-to-point and E-LAN services, where Down or 
Up MEPs are preconfigured 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Operation – Internal MEP Case 
The test traffic flow for Y.1564 tests – Internal MEP case is illustrated and explained below.  
In Internal MEP case, if a service MEP does not already exist, an Up MEP is automatically created at the 
generator side under the first unused MA number at MD level 7. An ACL is also automatically created on 
the receive side of the generator. The ACL forwards to the internal MEP only frames having source MAC 
address equal to the configured destination MAC address.  
This automatically created MEP is automatically deleted at the end of the test. 
In Internal MEP case, the Y.1564 test is associated with only one of the following options: 
• 
A single multi-CoS flow with an optional list of CoS values (default is “all CoS”) 
• 
One or more single CoS flows 
• 
A service (identified by service name) with an egress port ID and an optional list of CoS values 
(default is “all CoS”). In this case, the flows on which the test is performed are automatically 
found. 
If the EVC is classified by VLAN, the test is performed using P-bit value 5. 
 
Note 
This P-bit value often represents high priority data. 
 
ETX-2
ETX-2
Generator
ETH
Port
Responder
Key=crs_mac
MAC Swap 
Loopback
Automatic 
Block of User 
Traffic
ETH
Port
ETH
Port
ETH
Port
Internal
Up MEP
Test
Frames
Service
ACL
 
Y.1546 Test - Internal MEP Case (E-Line Services over PTP) 
ETX-2
ETX-2
Generator
ETH
Port
Responder
On all Flows to a 
Bridge-port
MAC Swap 
Loopback
Automatic 
Block of User 
Traffic
ETH
Port
Internal
Up MEP
Test
Frames
Service
ACL
B
ETH
Port
ETH
Port
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Y.1546 Test - Internal MEP Case (E-Line Services over Bridge) 
Note 
When running the Y.1564 test in a device, without configuring the OAM 
(Internal MEP case), configure the destination MAC address on the generator 
to the responder NNI MAC, as per the device used. 
The Y.1564 test for the Internal MEP case is performed as follows: 
1. At the generator side, a unique MAC is configured.  
2. At the generator side, an internal up MEP is automatically created. 
3. At the generator side, the source transmits test frames at data rate (different rates are used 
during different steps of the test) toward the configured MAC.  
4. DMM and LMM frames, transmitted periodically by the MEP at the generator side, are 
interleaved with the test data. 
5. At the responder side, the same unique MAC as used in the generator is configured. 
6. The responder loops back only frames with a destination MAC equal to the configured MAC. If 
egress-port is a bridge-port, loop and ACL on all ingress flows to a bridge-port. 
7. At the generator receive side, an ACL forwards only frames whose source MAC equals to the 
configured MAC. 
8. When the generator receives the looped DMM and LMM frames, it “responds” by sending DMR 
and LMR frames, respectively. 
9. The responder also loops back the DMRs and LMRs. 
10. Round-trip loss is measured by the sum of the LMR frame count and the local count at the 
generator ingress. 
11. Round-trip delay is measured by the DMR frame timestamps divided by two. 
Operation – Service MEP Case 
Generators and responders are supported over the following: 
• 
Down MEPs for E-Line and E-LAN services: 
 
Down MEP facing network ports 
 
Down MEP facing PCS port 
 
Down MEP facing EoPDH (logical MAC) 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
• 
Up MEPs for E-Line and E-LAN services over bridge/ring:  
 
Up MEP facing bridge port 
 
Up MEP facing ETP  
 
Up MEP facing port (E-Line up MEP) 
Note 
If a Y.1564 test is running over an ERP or ETP, any protection switchover 
causes the test to fail. 
Y.1564 test is supported over E-LAN in the presence of user traffic in the following cases: 
• 
E-LAN service is newly installed. 
• 
E-LAN service is already installed and running on E-LAN nodes, and you add a new node to the 
service. In this case, you can run the non-intrusive Y.1564 test on the new node without 
disrupting (blocking) the traffic on the other nodes. 
For the Service MEP case, the MA of the service MEPs used by the test, must be manually configured. 
The CoS on which the test is performed can optionally be configured with a single value or several values 
from 0 to 7; the default ‘all CoS’ indicates that all the preconfigured EVC.CoS will be tested. The MEPs 
and flows on which the test is performed are automatically learned from the configured MA and CoS. 
Regular Y.1564 Test 
The test traffic flow for regular Y.1564 tests is illustrated and explained below. The Y.1564 testing is 
disruptive; user traffic is blocked on the tested EVC during diagnostic procedure. 
PSN
Ethernet 
Port
Policer
Generator
Test 
Frames
Ethernet 
Port
Test Frames, 
DMMs, LMMs
Down 
MEP
Ethernet 
Port
Down 
MEP
Ethernet 
Port
Looped Test Frames, 
DMRs, LMRs
Responder
Policer
 
Full Y.1564 Traffic Path for EVC with Single CoS (Down MEP) 
ETX-2i Devices 
8. Monitoring and Diagnostics 
ETX-2
ETX-2
ETH
Port
ETH
Port
Down
MEP
Generator
ETH
Port
ETH
Port
Responder
Down
MEP
Test
Frames
Service
B
B
Test
Frames
Service
 
Full Y.1564 Traffic Path 
Note 
The responder can be configured to inject the test frames into the Policer or 
bypass it. 
The regular Y.1564 test is performed as follows: 
1. At the generator side, the source transmits test frames at specified data rate (different rates are 
used during the different steps of the test). 
2. The test frames are counted by the MEP LMM counters as they exit the generator. 
3. The test frames are counted again as they enter the responder by the MEP LMM counters. 
4. At the responder, the sink either drops the test frames or loops them back (unidirectional or 
bidirectional test configuration). 
5. LMR frames, returned by the MEP at the responder, plus local count at the generator ingress, 
provide the round-trip loss measurements (looped test frames are also counted by the LMR 
counters). 
6. DMM frames, transmitted periodically by the MEP at the generator side, are interleaved with 
the test data. The DMR frames, returned by the MEP at the responder side with two additional 
timestamps, provide the one-way and/or round-trip delay measurements. 
Y.1564 MAC Swap Loopback Test 
When the responder device has limited capabilities i.e., no service MEP is defined or the test frames 
cannot be identified and/or counted by the MEP, there is an alternative form of the responder – MAC 
swap loopback. Only bidirectional (round-trip) measurements are supported in this case. 
This test is supported over point-to-point services where MEPs are preconfigured at the generator side 
and a MAC swap loopback is activated at the responder side. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
PSN
Ethernet 
Port
Policer
Generator
Test 
Frames
Ethernet 
Port
Test Frames, 
DMMs, LMMs, DMRs, LMRs
Down 
MEP
Ethernet 
Port
Ethernet 
Port
Responder
Policer
MAC Swap 
Loopback
 
Y.1564 Test with MAC Swap 
The Y.1564 MAC swap loopback test is performed as follows: 
1. At the generator side, the source transmits test frames at specified data rate (different rates are 
used during different steps of the test). 
2. DMM and LMM frames, transmitted periodically by the MEP at the generator side, are 
interleaved with the test data. 
3. The responder loops back all the frames (the test frames as well as the OAM frames). 
4. When the generator receives the looped DMM and LMM frames it responds by sending DMR 
and LMR frames, respectively. 
5. The responder loops back the DMRs and LMRs received from the generator. 
6. Round-trip loss is measured by the sum of the LMR frame count and the local count at the 
generator ingress.  
7. Round-trip delay is measured by the DMR frame timestamps divided by two. 
 
Note 
In the case of a MAC swap loopback responder, the DMR timestamps include 
the time spent by the packet in the responder, therefore the round-trip delay 
measurements are less accurate. 
Y.1564 Launching Loopback Test 
When Launching Loopback functionality (LLF) is enabled on a MEP, the responder at the MEP level is 
used in the Y.1564 test. There is no need to define a Y.1564 responder, especially for the Y.1564 test. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
The Y.1564 Launching Loopback test is performed as follows: 
1. Enable the responder at MEP level. 
2. A generator having profile with responder type MEF4622, sends LLMs to responder. Some 
LMMs request status of LL; others request to activate or deactivate loopback. 
3. Upon receiving the LLM, the responder identifies the port, VLAN tags, and source MAC address 
of the generator.  
4. The Responder returns an LLR. 
5. If a reply is received, the Generator sends an LL Activate Request. 
Down MEP 
Depending on the specific implementation, a single MEP per EVC, or a separate MEP per single or 
multiple EVC.CoS is required to provision the test. In all cases, the service is supported with ‘regular’ and 
aggregate Policer. In case of a single MEP, the Rx flow classification can be VLAN or Outer VLAN.  In case 
of multiple MEPs, all the MEPs must belong to the same MA, and the Rx flow classification can only be 
VLAN + p-bit.  
Up MEP 
For multipoint-to-multipoint (E-LAN) services, the Y.1564 testing is performed over an Up MEP, for 
either a single Cos (EVC) or multi-CoS (EVC) service. The testing frames are transmitted into the bridge, 
and the VLAN tag value of the test traffic is defined by the Rx flow classification. In both cases, the 
service is supported with ‘regular’ and aggregate policer. 
 
Ethernet 
Port
Policer
Generator
Test 
Frames
Up MEP
SVI
Bridge
BP
BP
BP
Rx Flow
Tx Flow
 
EVC: Single CoS and Single Up MEP  
ETX-2i Devices 
8. Monitoring and Diagnostics 
Running Test on MEP with No Configured Services 
The Y.1564 profile supports the auto-cos-completion option, which enables running the Y.1564 test on a 
MEP without pre-configuration of services on some or all of the CoS p-bits of the MEP. Use of this option 
requires you to explicitly configure the p-bit in the MEP on which the test is to be run.  
The auto-cos-completion and p-bit options should be configured in both the generator and responder. 
Test Procedures 
This section describes Y.1564 test procedures and success criteria. 
Stepped CIR Test 
Transmission rate is according to the configured steps in percentage of CIR. For example, 25% of CIR, 
50% of CIR, 75% of CIR and CIR. 
Success criteria – FLR, FTD, and FDV are within SAC limits. 
Color-Blind EIR Test 
Transmission rate is equal to CIR + EIR. 
Success criteria – 0.99 × CIR (1-FLR) ≤ IR ≤ 1.01 × (CIR + EIR) 
Color-Blind Traffic Policing Test 
Transmission rate is set as follows: 
• 
If EIR ≥ 20% of CIR, Tx rate is set to: CIR + 125% of EIR 
• 
If EIR < 20% of CIR, Tx rate is set to: 125% of CIR + EIR 
Success criteria – 0.99 × CIR (1-FLR) ≤ IR ≤ 1.01 × (CIR + EIR) 
Color-Aware and Color-Blind CBS Test 
Based on test case 36 in MEF 19. 
Objective: To form the transmission pattern shown in the following diagram for the duration of the test. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
time [ms]
100
200
300
400
500
600
700
rate
CIR
PHY
1.1CBS
 
Transmission Pattern (CBS Test) 
This can be realized by utilizing two generators: 
• 
The first generator (G1) should transmit at CIR for ~200 msec, turn off for 100 msec, and start 
over.  
Note 
If (8 × CBS/CIR) > 90 msec, the transmission off period should be floor (9 × 
CBS/CIR) instead of 100 msec. 
• 
The second generator (G2) should inject a burst of length 110% CBS at maximum rate every 
300 msec. 
Preparation: 
• 
Set EIR = 0 and EBS = 0 for the duration of the test. 
• 
Stop DMM transmission for the duration of the test. 
• 
Transmit LMM once at the beginning of the test (when the generators are off) and once at the 
end of the test (when the generators are off). 
Procedure: 
• 
G1 transmits green C frames at CIR.  
 
C = ceiling (200 msec × CIR/bitsInFrame)  
where 
bitsInFrame = the size of the test frame in bits 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
• 
G2 transmits green B frames at maximum rate (1G or 10G).  
 
B = ceiling (1.1 × CBS/frameLength) 
where 
frameLength = the size of the test frame in bytes 
• 
The number of CIR/burst cycles actually performed during the test are counted. 
Success criteria: 
• 
For color-aware test – 0.99 × number of cycles × (C + N) × (1-FLR) ≤ number of green frames 
• 
For color-blind test – 0.99 × number of cycles × (C + N) × (1-FLR) ≤ total number of frames 
C = number of frames at CIR per cycle, defined above 
N = number of frames in CBS w/o excess = floor (CBS/frameLength) 
Where: 
frameLength = the size of the test frame in bytes 
Color-Aware EBS Test 
Based on test case 37 in MEF 19. 
Objective: To form the transmission pattern shown in the following diagram for the duration of the test. 
 
time [ms]
100
200
300
400
500
600
700
rate
CIR
PHY
1.1EBS
 
Transmission Pattern (Color-Aware EBS Test) 
This can be realized by utilizing two generators: 
ETX-2i Devices 
8. Monitoring and Diagnostics 
• 
The first generator (G1) should transmit at CIR for ~200 msec, turn off for 100 msec, and start 
over.  
Note 
If (8 × EBS/EIR) > 270 msec, the transmission off period should be floor (9 × 
EBS/EIR) – 200 msec instead of 100 msec. 
• 
The second generator (G2) should inject a burst of length 110% (EBS) at maximum rate every 
300 msec. 
Note 
If (8 × EBS/EIR) > 270 msec, the burst should be transmitted every floor (9 × 
EBS/EIR) instead of every 300 msec. 
Preparation: 
• 
Stop DMM transmission for the duration of the test. 
• 
Transmit LMM once at the beginning of the test (when the generators are off) and once at the 
end of the test (when the generators are off). 
Procedure: 
• 
G1 transmits green C frames at CIR. 
 
C = ceiling (200 msec × CIR/bitsInFrame) 
where 
bitsInFrame = test frame size in bits 
• 
G2 transmits yellow B frames at maximum rate (1G or 10G).  
 
B = ceiling (1.1 × EBS/frameLength) 
where 
frameLength = test frame size in bytes 
• 
The number of CIR/burst cycles actually performed during the test are counted. 
Success criteria: 
0.99 × number of cycles × C × (1-FLR) ≤ total number of frames 
C = ceiling (200 msec × CIR/bitsInFrame) 
N = number of frames in CBS w/o excess = floor (CBS/frameLength) 
Color-Blind EBS Test 
Based on test case 37 in MEF 19. 
Objective: To form the transmission pattern shown in the following diagram for the duration of the test. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
time [ms]
100
200
300
400
500
600
700
rate
CIR+EIR
PHY
1.1(CBS+EBS)
 
Transmission Pattern (Color-Blind EBS Test) 
This can be realized by utilizing two generators: 
• 
The first generator (G1) should transmit at CIR+EIR for ~200 msec, turn off for 100 msec, and 
start over.  
 
Note 
T = max (CBS/CIR, EBS/EIR); If (8 × T) > 90 msec, the transmission off period 
should be floor (9 × T) instead of 100 msec. 
• 
The second generator (G2) should inject a burst of length 110% (CBS+EBS) at maximum rate 
every 300 msec. 
 
Note 
T = max (CBS/CIR, EBS/EIR); If (8 × T) > 90 msec, the burst is transmitted every 
floor (9 × T) + 200 msec instead of every 300 msec 
Preparation: 
• 
Stop DMM transmission for the duration of the test. 
• 
Transmit LMM once at the beginning of the test (when the generators are off) and once at the 
end of the test (when the generators are off). 
Procedure: 
• 
G1 transmits E frames at (CIR+EIR). 
 
E = ceiling (200 msec × (CIR+EIR)/bitsInFrame) 
where 
bitsInFrame = test frame size in bits 

## Factory Defaults  *(p.1502)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
• 
G2 transmits B frames at maximum rate (1G or 10G).  
 
B = ceiling (1.1 × (CBS+EBS)/frameLength) 
where 
frameLength = test frame size in bytes 
• 
The number of EIR/burst cycles actually performed during the test are counted. 
Success criteria: 
0.99 × number of cycles × (C + N) × (1-FLR) ≤ total number of frames 
C = ceiling (200 msec × CIR/bitsInFrame) 
N = number of frames in CBS w/o excess = floor (CBS/frameLength) 
Where: 
frameLength = the size of the test frame in bytes 
Performance Test 
Transmission rate is equal to CIR. 
Success criteria – FLR, FTD, FDV, and Availability are within SAC limits. 
Factory Defaults 
By default, Ethernet service activation testing functionality is disabled. 
When a Y.1564 test profile is added, it has the following default settings: 
Parameter  
Default Value 
Units 
auto-cos-completion 
no auto-cos-completion 
ethernet-type  
0x22e8 
frame-size 
512 
Bytes 
round-trip-thresholds 
flr – 200 
ftd – 26000 
fdv – 11000 
availability – 9990 
PPM (1E-6) 
Microseconds 
Microseconds 
Hundredths of percent 
scope 
configuration performance 

## Configuring Y.1564 Test  *(p.1503)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter  
Default Value 
Units 
direction 
bidirectional 
color-aware 
color-aware 
traffic-policing 
traffic-policing 
cir-steps 
s1-percent – 25 
s2-percent – 50 
s3-percent – 75 
s4-percent – 100 
configuration-duration 
60 
Seconds 
performance-duration 
120 
Minutes 
rate-convention 
data-rate 
responder-type 
y1564 
user-traffic-blocked 
user-traffic-blocked 
Configuring Y.1564 Test 
Y.1564 test configuration procedure includes the following steps, detailed in this section: 
1. Add and configure a Y.1564 test profile in the generator and responder devices. 
2. Add, configure, and activate a Y.1564 test responder. 
3. Add, configure, and activate a Y.1564 test generator. 
 
Note 
For the Y.1564 test – Service MEP case, in devices with OAM MEP configured 
with MEF46 Latching Loopback, there is no need to add a Y.1564 responder. 
Adding Y.1564 Test Profile 
You can define up to 20 Y.1564 test profiles for ETX-2i and ETX-2i-B, and up to 64 for ETX-2i-10G and 
ETX-2i-100G, to be applied to the generator and responder to ensure the desired test functionality. 
The test profiles are defined at the EVC level and can also contain profiles at the EVC.Cos (P-bit) level 
with frame size and threshold definitions. Any EVC.Cos configuration overrides the EVC configuration. 
This enables the definition of different frame sizes and thresholds according to P-bit. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Note 
The DMM frame size in the Y.1564 test is set according to the frame size 
configured for the test profile, rather than according to the dest NE 
data-tlv-length configuration. 
In addition, you can run a multi-frame test, which means a Y.1564 test on multiple frame sizes. 
 To add and configure a Y.1564 test profile: 
1. Navigate to config>test>y1564. 
2. Define a Y.1564 test profile and assign a name to it: profile <profile-name>  
The system switches to the context of the profile (config>test>y1564>profile<profile-name>). 
3. Perform the required tasks according to the table below. 
Note 
no profile <profile-name> deletes the Y.1564 test profile. 
 To set up a multi-frame Y.1564 test: 
1. Set the Y.1564 test to use multiple frame sizes: 
config>test>y1564>profile>multi-frame-size 
Default: no multi-frame-size for performing the Y.1564 test on a single frame size. 
2. In a single CLI command, set up to four Y.1564 tests, each for a different frame size, (in bytes): 
config>test>y1564>profile>frame-size [64] [128] [256] [512] [1024] [1280] [1518] [custom 
<custom-size>] 
Default: 512. 
3. Refer to the relevant table entries for additional information and instructions. 
 
Task 
Command 
Comments 
Specifying whether OAM CFM 
services should be automatically 
created for tested p-bit values 
auto-cos-completion 
no auto-cos-completion 
Use of auto-cos-completion 
requires you to explicitly 
configure the p-bit command for 
the test (see parameter 
description below). 
Specifying whether to include or 
exclude the CBS and EBS sub-tests 
(burst tests) in the configuration 
phase  
[no] burst-test [cbs] [ebs] 
You can enter the command with 
one or both parameters. 
To specify not to include any 
burst tests in the configuration 
phase, enter: no burst-test. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Setting the number of steps and 
their transmission rate in the CIR 
subtest 
cir-steps s1 <s1-percent> 
[s2 <s2-percent>] [s3 <s3-percent>] 
[s4 <s4-percent>] 
s1-percent – transmission rate, 
as percentage of CIR, at the first 
step of the CIR subtest (1–100) 
s2-percent – transmission rate, 
as percentage of CIR, at the 
second step of the CIR subtest 
(1–100) 
s3-percent – transmission rate, 
as percentage of CIR, at the third 
step of the CIR subtest (1–100) 
s4-percent – transmission rate, 
as percentage of CIR, at the 
fourth step of the CIR subtest (1–
100) 
Note: You can define fewer than 
four steps as long as the last step 
is 100%. 
Setting the color mode used for 
the test 
color-aware 
no color-aware 
 
Defining the duration of the 
configuration test for each P-bit 
configuration-duration <seconds> 
Possible values: 18–360 seconds 
Setting the direction in which the 
test is performed 
direction {unidirectional | 
bidirectional} 
Default: bidirectional 
Defining EtherType of the test 
frames 
ethernet-type <hex-number> 
Note: The EtherType 
configuration is only applicable 
for the Y.1564 generator. It is not 
applicable for the responder, as 
it loops all test frames that it 
receives from the generator, 
regardless of their EtherType. 
Enabling multi-frame Y.1564 test 
multi-frame-size 
no multi-frame-size 
This command enables setting 
the Y.1564 test to run on 
multiple frame sizes (defined in 
the frame-size command above). 
Enter no multi-frame-size 
(default) to perform the test on a 
single frame size. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining test frame size 
frame-size { 64 | 128 | 256 | 512 | 
1024 | 1280 | 1518 | custom <bytes> } 
Range for custom bytes: 
64–9600 (jumbo frames) 
In case of traffic-policing no-
bandwidth-roundup in the 
responder side (see below), 
there is significance to the 
frame-size value. 
For a multi-frame Y.1564 test, 
enable multi-frame-size 
(command above), and then 
define in this command up to 
four frame sizes for the test.  
Example: frame-size 64 256 
custom 1234 
Setting the source MAC address 
in test frames  
(for Y.1564 over LAG) 
 
multiple-sa-mac 
multiple-sa-mac base 
<first-mac-address> 
no multiple-sa-mac 
Relevant for ETX-2i-10G and ETX-
2i-100G only. 
The source MAC addresses of 
generated test frames are 
cyclically selected from a block of 
32 consecutive MAC addresses 
beginning at default address 
0x0020D2000100 or at 
configured base address. 
base - the start of a block of 
MACs to be used as the source 
address in test frames. 
Must be a multiple of 32. 
Example: multiple-sa-mac base 
0x000012345600 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Setting the one-way service 
acceptance criteria 
one-way-thresholds flr <ppm> ftd 
<μs> fdv <μs> availability 
<percent/100> 
flr – unidirectional Frame Loss 
Ratio, measured in 1E-6 units 
ftd – unidirectional Frame 
Transfer Delay, measured in 
microseconds 
fdv – unidirectional Frame Delay 
Variation, measured in 
microseconds 
availability – unidirectional 
availability, measured in 
hundredths of percent units  
Possible values: 0-100000 
(For example, use value 8930 in 
order to define 89.3%) 
Creating, modifying, or deleting a 
Y.1564 test P-bit profile 
p-bit <0..7> 
The P-bit test profile allows 
configuring separate frame sizes 
and thresholds for specific P-bits. 
The rest of the P-bits are tested 
using the general profile. 
See P-bit configuration details 
below. 
Enter no p-bit <0..7> to delete a 
specific test P-bit profile. 
Defining the duration in minutes 
of the performance phase  
performance-duration [15m] [2h] 
[24h] [custom <custom>] 
Possible values: 15 minutes, 2 
hours, 24 hours, or a custom 
duration (1–7200 minutes) 
Defining the duration of the 
performance test, in minutes 
performance-duration minutes 
Possible values: 1–7200 minutes  
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining the convention of the 
rate measurements in the Y.1564 
test report  
rate-convention <data-rate | 
line-rate> 
The convention of the rate 
measurements section in the 
Y.1564 test report is determined 
by the option that you select: 
• data rate – section title is IR 
[Mbps]. 
• line rate – section title is ULR 
[Mbps]. 
Note: Configuring 
rate-convention only changes 
the title in the generated Y.1564 
test report according to your 
selection (IR for data-rate; ULR 
for line-rate). It does not change 
the values of the measurements 
in the report. Therefore, after 
changing rate-convention in the 
profile, you must run the Y.1564 
test again to display the 
measurements in the newly 
selected rate-convention.   
Defining the type of responder 
that receives the test and OAM 
frames from the generator in the 
Y.1564 test 
responder-type {y1564 | mac-swap | 
mef46-ll} 
y1564 – regular responder; adds 
time stamps to the OAM frames 
that it returns to the generator 
mac-swap - MAC swap 
responder; does not add time 
stamps to the OAM frames that it 
returns to the generator 
mef46-ll - MEF46 Latching 
Loopback responder; Upon 
receiving LLM from the 
generator, replies with LLRs. 
OAM frames are not looped 
back.  
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Setting the round-trip service 
acceptance criteria 
round-trip-thresholds flr <ppm> ftd 
<μs> fdv <μs> availability <availability> 
flr – bidirectional Frame Loss 
Ratio, measured in 1E-6 units 
ftd – bidirectional Frame 
Transfer Delay, measured in 
microseconds 
fdv – bidirectional Frame Delay 
Variation, measured in 
microseconds 
availability – bidirectional 
availability, measured in 
hundredths of percent units (for 
example, use value 8930 in order 
to define 89.3%) 
Setting the scope of the test: 
configuration test, performance 
test, or both 
scope [configuration] [performance] 
You can enter the command with 
one or both parameters 
To specify with no scope 
parameters, enter: no scope  
Specifying whether to apply 
traffic policing 
traffic-policing  
{ no-bandwidth-roundup | service } 
no traffic-policing 
This command sets the relevant 
EVC Policer on the loop, and 
affects the Generator and 
Responder sides as follows: 
• Generator side – includes or 
excludes the traffic policing 
subtest from the 
configuration phase 
• Responder side – passes or 
does not pass the data 
through the responder 
Policer 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
• no-bandwidth-roundup – 
relevant for the responder 
side only (in the generator it’s 
the same as traffic-policing 
without no-bandwidth-
roundup); indicates that 
relevant EVC Policer should 
not be rounded up to the 
CIR/EIR (if not specified, it is 
rounded up). If you set this 
option, there is significance 
to the frame-size value (see 
above). 
• service – relevant for the 
responder site only, indicates 
that tag handling is aligned 
with the service and its 
policer. 
no traffic-policing indicates no 
Policer on the loop.  
Specifying whether user traffic is 
to be blocked/allowed during the 
test 
user-traffic-blocked 
no user-traffic-blocked  
 
The following P-bit test profile parameters can be configured at the p-bit level in the 
config>test>y1564>profile(profile-name)>p-bit<value># prompt. 
Task 
Command 
Comments 
Defining test frame size 
frame-size { 64 | 128 | 256 | 512 | 
1024 | 1280 | 1518 | custom <bytes> } 
Range for custom bytes: 
64–9600 (jumbo frames) 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Setting the one-way service 
acceptance criteria 
one-way-thresholds flr <ppm> ftd <μs> 
fdv <μs> availability <availability> 
flr – service acceptance criteria 
for unidirectional Frame Loss 
Ratio, measured in 1E-6 units 
ftd – service acceptance criteria 
for unidirectional Frame 
Transfer Delay, measured in 
microseconds 
fdv – service acceptance criteria 
for unidirectional Frame Delay 
Variation, measured in 
microseconds 
availability – service acceptance 
criteria for unidirectional 
availability, measured in 
hundredths of percent units (for 
example, use value 8930 in 
order to define 89.3%) 
Setting the round-trip service 
acceptance criteria 
round-trip-thresholds flr <ppm> ftd 
<μs> fdv <μs> availability <availability> 
flr – service acceptance criteria 
for bidirectional Frame Loss 
Ratio, measured in 1E-6 units 
ftd – service acceptance criteria 
for bidirectional Frame Transfer 
Delay, measured in 
microseconds 
fdv – service acceptance criteria 
for bidirectional Frame Delay 
Variation, measured in 
microseconds 
availability – service acceptance 
criteria for bidirectional 
availability, measured in 
hundredths of percent units (for 
example, use value 8930 in 
order to define 89.3%) 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Adding Y.1564 Responder 
Note 
For the Y.1564 test - Service MEP case, in devices with OAM MEP configured 
with MEF46 Latching Loopback, there is no need to add a Y.1564 responder. 
You can define up to 20 Y.1564 test responders for ETX-2i and ETX-2i-B, when each OAM MA includes 
eight services (p-bits). These 20 responders can be all EVC, all EVC.CoS, or any combination of EVCs and 
EVC.CoSs. All the responders can be activated simultaneously. 
 To add and configure Y.1564 responder: 
1. Navigate to config>test>y1564. 
2. Define a Y.1564 test responder and assign a name to it: responder<responder-name>  
The system switches to the context of the responder (config>test>y1564>responder<responder-
name>). 
3. Perform the required tasks according to the following table. 
Note 
no responder <responder-name> deletes the Y.1564 responder. 
 
Task 
Command 
Comments 
Activating or deactivating the test 
at the responder side 
activate 
no activate 
 
Defining the service to be tested 
bind <md <id> ma <id> [p-bit <0..7>] 
no bind <md <id> ma <id> 
md – the maintenance domain 
to which the service belongs (1–
65535) 
ma – the maintenance 
association to which the service 
belongs (1–65535) 
p-bit – the specific P-bits to be 
tested, or all preconfigured 
P-bits if none are specified 
no bind md <id> ma <id> 
removes responder association 
with the service. 
When enabling 
auto-cos-completion, it is 
mandatory to explicitly 
configure the normally optional 
p-bit command. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining the service to be tested 
bind flow <flow-name> 
no bind flow <flow-name> 
Mutual exclusion with the other 
bind formats.  
flow – the multi-CoS flow that 
carries the service OR a single-
CoS flow that is part of the 
service. 
Possible values: Variable length 
string, up to 32 characters. 
A corresponding flow must 
already exist in the RAD flow 
table. 
no bind removes responder 
association with the service. 
Defining the service to be tested 
bind service <service-name> { 
ethernet} <port-index>  
bind service <service-name> { lag | pcs 
| logical-mac | svi} <port-number>  
bind service <service-name> 
bridge-port <bridge-number> 
<port-number>  
bind service <service-name> 
etp <etp-name> {subscriber|transport 
}  <port-number>  
no bind service <service-name>   
Mutual exclusion with the other 
bind formats  
service – the name of the tested 
service. A flow corresponding to 
service name, port must already 
exist in the RAD flow table. 
Possible values: Variable length 
string, up to 32 characters 
ethernet, lag, pcs, logical-mac, 
svi, bridge-port, etp subscriber, 
etp transport – the port over 
which the service is tested 
no bind removes responder 
association with the service. 
Setting the local MAC address 
used for the multipoint test 
local-mac mac <mac-address> 
no local-mac 
Note: Command available only 
when responder is bound to a 
flow. 
mac – the MAC address that the 
responder uses for E-LAN and E-
Tree tests 
Default value: 0x000000 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Setting the destination MAC 
address or remote MEP number 
destination mac <mac-address> 
destination remote-mep <rmep-id> 
mac – a configurable MAC 
address that identifies the 
generator side 
Note: When there is more than 
one generator on a certain 
E-LAN service, each generator 
has a unique remote MAC. 
remote-mep – identifier of a 
remote MEP at the generator 
side, towards which the test is 
conducted. 
Possible values: 0–8191 
Note: You can disassociate the 
destination remote MEP from 
the responder by entering 
destination remote-mep 0 (and 
not no destination). 
Assigning a test profile to the 
responder 
test-profile <profile-name> 
 
Displaying the Y.1564 test status 
show status 
See Viewing Test Status 
(Responder Side).  
Adding Y.1564 Generator 
You can define up to eight Y.1564 test generators for ETX-203AX/X and ETX-205A/X, each with up to 
eight p-bits. These eight generators can be all EVC, all EVC.CoS, or any combination of EVCs and 
EVC.CoSs. All the generators can be activated simultaneously. You can activate generators on up to eight 
p-bits simultaneously (a p-bit is equivalent to an OAM MEP service). 
 To add and configure Y.1564 generator: 
1. Navigate to config>test>y1564. 
2. Define a Y.1564 test generator and assign a name to it: generator<generator-name>  
The system switches to the context of the generator (config>test>y1564>generator<generator-
name>). 
3. Perform the required tasks according to the following table. 
Note 
no generator<generator-name> deletes the Y.1564 generator. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Activating or deactivating the test 
at the generator side 
activate 
no activate 
 
Defining the service to be tested 
bind md <id> ma <id> [p-bit <0..7>]  
no bind md <id> ma <id> 
md – maintenance domain to 
which the service belongs (1–
65535) 
ma – maintenance association 
to which the service belongs (1–
65535) 
p-bit – specific P-bits to be 
tested, or all preconfigured 
P-bits if none are specified 
no bind md <id> ma <id> 
removes generator association 
with the service. 
When enabling 
auto-cos-completion, it is 
mandatory to explicitly 
configure the normally optional 
p-bit command. 
Defining the service to be tested 
bind flow <flow-name> [multi-cos] 
[p-bit <0..7>] 
no bind flow <flow-name> 
Mutual exclusion with the other 
bind formats; if the optional 
multi-cos attribute does not 
exist, several bind commands 
with different flow names can 
be configured.  
flow – the multi-CoS flow that 
carries the service OR a single-
CoS flow that is part of the 
service. A corresponding flow 
must already exist in the RAD 
flow table. 
Possible values: Variable length 
string, up to 32 characters 
multi-cos – indicates that the 
specified flow name is a 
multi-CoS flow 
p-bit – specific P-bits to be 
tested, or all preconfigured 
P-bits if none are specified 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Valid only together with the 
optional multi-cos attribute. For 
each specified P-bit, a 
corresponding CoS (rank) must 
already exist in the envelope 
Policer of the multi-CoS flow. 
no bind removes generator 
association with the service. 
Note: When binding Y.1564 to a 
flow, Y.1564 always uses the 
user configured MAC address 
instead of the remote MEP MAC 
address, even in the case that a 
MEP is configured on the bound 
flow. 
Defining the service to be tested 
bind service <service-name> {ethernet} 
<port-index> [p-bit [<0..7>]] 
bind service <service-name> {lag | pcs 
| logical-mac | svi} <port-number> 
[p-bit [<0..7>]] 
bind service <service-name> 
bridge-port <bridge-number> 
<port-number> [p-bit [<0..7>]] 
bind service <service-name> 
etp <etp-name> {subscriber|transport} 
<port-number> [p-bit <p-bit>] 
no bind service <service-name>   
Mutual exclusion with the other 
bind formats  
service – the name of the tested 
service. A flow corresponding to 
service name, port must already 
exist in the RAD flow table. 
Possible values: Variable length 
string, up to 32 characters 
ethernet, lag, pcs, logical-mac, 
svi, bridge-port, etp subscriber, 
etp transport – the port over 
which the service is tested 
p-bit – the specific P-bits to be 
tested, or all preconfigured 
P-bits if none are specified. 
For each specified P-bit, a 
corresponding flow must 
already exist in the RAD flow 
table. 
no bind removes generator 
association with the service.  
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Setting the destination MAC 
address or remote MEP number 
destination mac <mac-address> 
destination remote-mep <rmep-id> 
mac – a configurable MAC 
address that identifies the 
responder side 
Note: When there is more than 
one responder on a certain E-
LAN service, each reponder has 
a unique remote MAC. 
remote-mep – identifier of a 
remote MEP at the responder 
side, towards which the test is 
conducted 
Possible values: 0-8191 
Note: Destination remote MEP 
can be disassociated from the 
generator by entering 
destination remote-mep 0 (and 
not no destination). 
Assigning Policer to test 
policer <p-bit> bandwidth 
[cir <cir-value>] [cbs <cbs-value>] 
[eir <eir-value>] [ebs <ebs-value>]  
[compensation <compensation-value>] 
policer <p-bit> profile 
<policer-profile-name> 
If a Policer is defined for the 
test, then the test is performed 
according to the test Policer, 
rather than according to the 
associated flow Policer. 
p-bit – CoS to which the 
configuration applies 
Possible values: 0..7 
cir – committed information 
rate 
cbs – committed burst size 
eir – excessive information rate 
ebs – excessive burst size 
compensation – extra bytes 
added to frame size to take into 
account Layer-1 overhead 
(preamble and IFG) in the 
network and the overhead for 
the added VLAN header. 
Possible values: 0..63 

## Examples  *(p.1518)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
profile – an optional predefined 
Policer profile to be used in the 
test 
Note: The option to define a 
test Policer is useful if there is 
no flow Policer, or the flow 
Policer has different limits than 
you wish to use for the test.  
Assigning a test profile to the 
generator 
test-profile <profile-name> 
 
Displaying the status of the 
MEF46 Latching Loopback 
generator 
show mef46-ll-status 
See Viewing the MEF46 
Latching Loopback Status. 
Displaying the Y.1564 test status 
show status 
See Viewing Test Status 
(Generator Side). 
Displaying the test results and 
measurements 
show report <summary | detailed> 
See Viewing Test Results. 
Examples 
This example shows how to create a Y.1564 test generator over a MEP located between two Ethernet 
ports and bound to one of them. The Y.1564 test (Service MEP case) is run over an OAM (CFM) service 
defined on P-bit 0. The test in this example is run on a network port, but Y.1564 tests can also be run on 
user ports.  
 To configure Y.1564 test generator over a MEP: 
1. Configure a Policer profile. 
2. Configure a VLAN-type classifier profile. 
3. Configure two flows from Ethernet port 0/1 to port 0/4 and vice versa.  
4. Define a MEP bound to port 1. 
5. Configure MEP service with LMMs and DMMs sent over P-bit 0. 
6. Configure a Y.1564 test profile. 
7. Add a Y.1564 generator, bind it to the relevant MD, MA, P-bit, and test profile. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Ethernet 
Port 1
Policer
Generator
Test 
Frames
MEP
Ethernet 
Port 4
P-bit 0
Flow 1
Flow 2
 
Y.1564 Test Generator over Down MEP 
************************Defining_Policer_Profile***************************** 
exit all 
config qos policer-profile v10 bandwidth cir 100000 cbs 10000 eir 10000 ebs 5000 
#*********************************End**************************************** 
 
************************Defining_Classifier_Profile************************** 
config flows classifier-profile vlan10 match-any 
  match vlan 10 
exit all 
#*********************************End**************************************** 
 
******************************Adding_Flows*********************************** 
configure flows flow v10_1to4 
  classifier vlan10 
  no policer  
  ingress-port ethernet 0/1 
  egress-port ethernet 0/4 queue 0 block 0/1 
  no shutdown 
  exit all 
 
configure flows flow v10_4to1 
  classifier vlan10 
  policer profile v10 
  ingress-port ethernet 0/4 
  egress-port ethernet 0/1 queue 0 block 0/1 
  no shutdown 
  exit all 
#*********************************End**************************************** 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#**************************Defining_MEP_and_MEP_Service********************** 
configure oam cfm 
  maintenance-domain 1 
    maintenance-association 1 
      ccm-interval 1s 
      classification vlan 0 
      mep 1 
        flow uni-direction rx v10_1to4 tx v10_4to1 
        bind ethernet 0/1 
        queue fixed 0 block 0/1 
        remote-mep 2 
        dest-addr-type ccm multicast 
        client-md-level 6 
        ais 
        no shutdown 
 
        service 1 
          classification priority-bit 0 
          delay-threshold 100000 
          delay-var-threshold 10000 
          lmm-interval 100ms 
          dmm-interval 100ms 
          dest-ne 1 
            remote mep 2 
            loss single-ended 
            delay two-way 
            exit 
          no shutdown 
          exit all 
#*********************************End**************************************** 
 
#*******************Configuring_Y.1564_Test_Profile_and_Generator************ 
config test y1564 
  profile 1 
    ethernet-type 0x22e8 
    frame-size 512 
    one-way-thresholds flr 100 ftd 13000 fdv 8000 availability 9990 
    round-trip-thresholds flr 200 ftd 26000 fdv 11000 availability 9990 
    scope configuration performance 
    direction bidirectional 
    color-blind 
    traffic-policing 
    cir-steps s1 25 s2 50 s3 75 s4 100 
    configuration-duration 60 
    performance-duration custom 1 
    rate-convention data-rate 
    exit 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
  generator 1 
    test-profile 1 
    bind md 1 ma 1 p-bit 0 
    activate 
    exit all 
save 
#*********************************End**************************************** 
  
The following example shows the configuration of the Y.1564 test (Service MEP case) over E-LAN service. 
Note that the node in the target device must be explicitly configured with the remote MEP number. 
 To run the Y.1564 test on an E-LAN service: 
generator "1" 
        test-profile "1" 
        bind md 1 ma 1 
        destination remote-mep 1 
responder "1" 
        test-profile "1" 
        bind md 1 ma 1 
        destination remote-mep 1 
The following example shows the configuration of both the generator and responder when the Y.1564 
test runs in a device without configuring the OAM (Internal MEP case). In this case, both generator and 
responder are bound to a flow (and not to an MA or MD). Also, the destination MAC address on the 
generator is configured to the responder NNI MAC. 
#generator : 
    configure 
        qos 
            policer-profile "CIR10M-EIR20M" 
                bandwidth cir 9984 cbs 64000 eir 19968 ebs 64000 
            exit 
        exit 
        flows 
            classifier-profile "v100" match-any 
                match vlan 100 
            exit 
            classifier-profile "v1502-p3" match-any 
                match vlan 1502 p-bit 3 
            exit 
            flow "gd-dn" 
                classifier "v1502-p3" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 4/1 
                egress-port ethernet 3/1 queue 1 block 0/1 
                no shutdown 
            exit 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
            flow "gd-up" 
                classifier "v100" 
                policer profile "CIR10M-EIR20M" 
                vlan-tag push vlan 1502 p-bit fixed 3 
                ingress-port ethernet 3/1 
                egress-port ethernet 4/1 queue 0 block 0/1 
                no shutdown 
            exit 
        exit 
    exit 
    configure 
        test 
            echo "Configure Y1564" 
#           Configure Y1564 
            y1564 
                echo "Y1564 - Profile Configuration" 
#               Y1564 - Profile Configuration 
                profile "2" 
                    performance-duration custom 1 
                exit 
                echo "Y1564 - Generator Configuration" 
#               Y1564 - Generator Configuration 
                generator "Generator1" 
                    test-profile "2" 
                    bind flow "gd-up" 
                    Destination 00-20-D2-EE-1B-B7 
                exit 
            exit 
        exit 
    exit 
 
#responder  
    configure 
        qos 
            policer-profile "CIR10M-EIR20M" 
                bandwidth cir 9984 cbs 64000 eir 19968 ebs 64000 
            exit 
        exit 
        flows 
            classifier-profile "v100" match-any 
                match vlan 100 
            exit 
            classifier-profile "v1502-p3" match-any 
                match vlan 1502 p-bit 3 
            exit 
 
 

## Configuration Errors  *(p.1523)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
            flow "gd-dn" 
                classifier "v1502-p3" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 4/1 
                egress-port ethernet 3/1 queue 1 block 0/1 
                no shutdown 
            exit 
            flow "gd-up" 
                classifier "v100" 
                policer profile "CIR10M-EIR20M" 
                vlan-tag push vlan 1502 p-bit fixed 3 
                ingress-port ethernet 3/1 
                egress-port ethernet 4/1 queue 0 block 0/1 
                no shutdown 
            exit 
        exit 
    exit 
    configure 
        test 
            echo "Configure Y1564" 
#           Configure Y1564 
            y1564 
                echo "Y1564 - Profile Configuration" 
#               Y1564 - Profile Configuration 
                profile "2" 
                exit 
                echo "Y1564 - Responder Configuration" 
#               Y1564 - Responder Configuration 
                responder "Responder1" 
                    test-profile "2" 
                    bind flow "gd-up" 
                exit 
            exit 
        exit 
The following example shows the configuration of the Policer under the Y.1564 generator. 
 To configure the Policer under the Y.1564 generator: 
ETX-2i>config>test>y1564>generator(1)$ policer 5 bandwidth cir 10000 cbs 32767 eir 5000 
ebs 32767 compensation 20 
Configuration Errors 
The following table lists the messages generated by ETX‑2i when a configuration error is detected. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Description 
Illegal frame size value 
Invalid test frame size for Y.1564 profile 
Unidirectional measurement is not 
supported 
Only bidirectional measurement is supported. 
Illegal threshold value 
Invalid round-trip service acceptance criteria for Y.1564 profile 
Illegal color value 
Invalid color mode for Y.1564 profile 
Illegal traffic policing value 
Invalid traffic Policer for Y.1564 profile 
Illegal CIR step value 
Invalid CIR step for Y.1564 profile 
Illegal configuration duration value 
Invalid duration of the configuration test for Y.1564 profile 
Illegal performance duration value 
Invalid duration of the performance test for Y.1564 profile 
Illegal rate convention value 
Invalid rate measurement convention for Y.1564 profile 
Illegal P-bit value 
Invalid P-bit value for Y.1564 profile or generator 
MD does not exist 
Maintenance domain selected for Y.1564 generator or responder 
has not been configured yet. 
MA does not exist 
Maintenance association selected for Y.1564 generator or 
responder has not been configured yet. 
Y.1564 profile does not exist 
(SNMP only) The configured Y.1564 test profile does not exist. 
Illegal command value 
Invalid value for the parameter 
Max number of active generators has 
been exceeded 
The maximum number of Y.1564 generators (8) has been reached 
and no additional generators can be added. 
Max number of active responders has 
been exceeded 
The maximum number of Y.1564 responders (20) has been 
reached and no additional responders can be added. 
Y.1564 profile is in use 
Y.1564 profile is in use and cannot be modified. 
Y.1564 profile has not been attached 
No Y.1564 profile has been attached to generator or responder. 
Active generator cannot be changed 
Active Y.1564 generators cannot be modified. 
Active responder cannot be changed 
Active Y.1564 responders cannot be modified. 
MEP or service have not been found 
MEP or OAM service within selected MD/MA does not exist. 
MEPs have different destination MAC 
address 
Y.1564 Generator works opposite one remote only. In EVC.cos, the 
MEPs under the MA are opposite several remotes, and therefore 
the test does not work. 

## Viewing Test Status (Responder Side)  *(p.1525)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Description 
The device didn't learn the remote's mac-
address. 
No CCM was received from the remote MEP and its MAC address 
was not learned. This is relevant only if remote-mep is configured 
on the DestNE. 
MEPs have different source MAC 
addresses 
 All MEPs under the same MA must be bound to the same port. 
MEPs have different classification types 
MEPs within selected MD/MA have different classification types. 
MEPs have different VLANs 
MEPs within selected MD/MA have different VLANs. 
MEPs have different inner VLANs 
MEPs within selected MD/MA have different inner VLANs. 
MEP or service are not active 
MEP or OAM service within selected MD/MA has not been 
activated yet. 
OAM CFM: Max number of remote MEP 
elements in a line has been exceeded. 
The maximum number of remote MEP elements in a line has been 
reached and no additional MEP elements can be added. 
OAM CFM: Max allowed number of 
<512/1024> remote MEPs has been 
reached. 
Adding MEPs to previously configured MEPs exceeds the allowed 
maximum number of remote MEP elements that can be 
configured (512/1024). 
Policer profile is missing 
No Policer is configured on the relevant Tx flow. 
I/O flow with matching CoS has not been 
found 
The Y.1564 test mechanism failed to identify a MEP Tx flow with a 
P-bit, matching testing criteria. 
Generator can test only one P-bit 
If there is only one Tx flow with the non-envelope Policer, only one 
P-bit can be tested. 
MEP is already under test 
A test is already running on this MEP. 
Viewing Test Status (Responder Side) 
 To display the test status (responder side): 
• 
In the config>test>y1564>responder<responder-name># prompt, enter show status. 
The status screen appears. For information on the test status values, see the following table. 
ETX‑2i>config>test>y1564>responder(1)# show status 
Status : In Progress 
 
MEP 
Service      P-BIT      
21  
1 
       1          
22  
1 
       3          
23   1 
       5          

## Viewing MEF46 Latching Loopback Generator Status  *(p.1526)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Description 
Status 
Current status of the test (responder): 
Idle – Test has been configured and has not yet been run. 
Ready – Test is ready to run. 
In progress – Test is currently running. 
MEP 
Identifier of the MEP that is associated with the responder and specific P-bit 
Possible values: 1–8191 
Service 
Identifier of the service that is associated with the responder and specific P-bit 
Possible values: 1–8 or — 
P-BIT 
P-bit that is included in the tested service 
Possible values: 0–7 
 
Viewing MEF46 Latching Loopback Generator Status 
 To display the MEF46 LL generator status: 
• 
In the config>test>y1564>generator<generator-name># prompt, enter show mef46-ll-status. 
The status screen appears. For information on the test status values, see the following table. 
ETX-2i>config>test>y1564>generator(1)# show mef46-ll-status 
Tx LLMs            : 3 
Rx LLRs            : 3 
Rx Autonomous LLRs : 0 
 
Last Received LLR 
----------------------------------------------------------------------------- 
Flags         :    Status  : Inactive              Direction  : NA        Unrecognized TLV  : 
No 
Response Code :              No Error 
 
ETX-2i >config>test>y1564>generator(1)# 
 
Parameter Displayed 
Description 
Tx LLMs 
Number of LLM PDUs sent by the LL controller 
Rx LLRs 
Number of LLR PDUs received by the LL controller 

## Viewing Test Status (Generator Side)  *(p.1527)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter Displayed 
Description 
Rx Autonomous LLRs 
Number of autonomous LLR PDUs received by the LL controller 
Status 
Latching Loopback status: 
Possible values: Inactive, Active 
Direction 
Latching Loopback direction: 
Possible values: NA, Internal, External 
Unrecognized TLV 
Indicates whether one or more of the included TLVs were not recognized  
Possible values: No, Yes 
Response Code 
Response code in the last received LLR PDU 
Possible values: No Error, Malformed Request, Max Session Exceeded, Resource 
Unavailable, Already Active, Already Inactive, Unsupported, Wrong MP, Timeout, 
Prohibited, Unknown Message Type, Unknown Error 
Viewing Test Status (Generator Side) 
 To display the test status (generator side): 
• 
In the config>test>y1564>generator<generator-name># prompt, enter show status. 
The status screen appears. For information on the test status values, see the following table. 
ETX‑2i>config>test>y1564>generator(1)# show status 
Status : In Progress 
 
Time Remaining : 00:00:24 
Test Phase     : Performance 
 
Associated EVC 
----------------------------------------------------------------------------- 
Inner VLAN : ---            Outer VLAN  : 20 
 
 
MEP   Service P-BIT  Tx Flow                           Rx Flow 
----------------------------------------------------------------------------- 
1     2       1      flow2_3to1                        flow2_1to3 
 
 
 
MEP   Service P-BIT  CIR       EIR       BWP In Use 
                     (Mbps)    (Mbps) 
----------------------------------------------------------------------------- 
1     2       1      37.5      75.0      Flow 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter Displayed 
Description 
Status 
Current Test status (generator): 
Idle – Test has been configured and has not yet been run. 
In Progress – Test is currently running. 
Passed – Test has been completed successfully. 
Failed – Test has failed. 
User Aborted – Test has been stopped by the operator. 
Time Remaining 
Time remaining until the end of the test 
Displayed when Status is In Progress 
Test Phase 
Current phase of the test 
Possible values: Configuration, Performance 
Displayed when Status is In Progress 
Inner VLAN 
Value of the inner VLAN (usually C-Tag) 
Possible values: 0–4095 
If there is no inner tag, the string “—“ is displayed. 
Displayed when Status is other than Idle 
Outer VLAN 
Value of the outer VLAN (usually S-Tag) 
Possible values: 0–4095 
If there is no outer tag, the string “—“ is displayed. 
Displayed when Status is other than Idle. 
MEP 
Identifier of the MEP that is associated with the P-bit 
Possible values: 1–8191 
Displayed when Status is other than Idle 
Service 
Identifier of the service that is associated with the P-bit 
Possible values: 1–8 or — 
Displayed when Status is other than Idle. 
P-BIT 
P-bit that corresponds to the tested service 
Possible values: 0-7 
Displayed when Status is other than Idle and when EVC is untagged 
Tx Flow 
Egress flow corresponding to the MEP and P-bit 
Displayed when Status is other than Idle 

## Viewing Test Results  *(p.1529)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter Displayed 
Description 
Rx Flow 
Ingress flow corresponding to the MEP and P-bit 
Displayed when Status is other than Idle 
CIR (Mbps) 
Provisioned CIR of the egress flow 
Displayed when Status is other than Idle 
EIR (Mbps) 
Provisioned EIR of the egress flow 
Displayed when Status is other than Idle 
BWP in use 
Origin of the associated bandwidth profile for the EVc.CoS 
Possible values: Test, Flow 
Displayed when Status is other than Idle 
 
Viewing Test Results 
When displaying the Y.1564 test results, you can choose to generate a test summary or a detailed test 
report. 
Note 
In detailed test report, in case a step is Not Applicable, all step parameters 
display value --- and not 0. 
 To display the summary test results: 
• 
In the config>test>y1564>generator<generator-name># prompt, enter show report summary. 
The summary report screen is displayed. For information on the test report summary counters, 
see the following table. 
 
ETX-2i>config>test>y1564>generator(1)# show report summary 
Services 
----------------------------------------------------------------------------- 
Destination MAC Address : 00-20-D2-54-11-92 
Source MAC Address      : 00-20-d2-f1-d1-66 
Inner Tag               : ---                                     Outer Tag  : 1 
P-bit/s                 : 0 
 
 
Summary 
----------------------------------------------------------------------------- 
Scope             : Configuration+Performance 
Profile Name      : 1 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Start Date & Time : 2016-07-24  13:04:44 
End Date & Time   : 2016-07-24  13:05:05 
Total Duration    : 00:00:21 
Overall Result    : Failed 
 
 
Configuration Test Report 
----------------------------------------------------------------------------- 
P-bit          : 0 
Duration (Sec) : 20 
Result         : Failed               CIR,EIR,Policing 
 
   Test   Result                              Tx Rate  IR       FLR      FTD      FDV 
                                              (Mbps)   (Mbps)            (ms)     (ms) 
 
CIR Test 
----------------------------------------------------------------------------- 
   Step#1 Failed           FLR                25.0     0.0      1.0E+00  0.004    0.0 
   Step#2 Failed           FLR                50.0     0.0      1.0E+00  0.004    0.0 
   Step#3 Failed           FLR                75.0     0.0      1.0E+00  0.004    0.0 
   Step#4 Failed           FLR                100.0    0.0      1.0E+00  0.004    0.0 
 
EIR Test 
----------------------------------------------------------------------------- 
          Failed           IR                 101.0    0.0      1.0E+00  0.004    0.0 
 
Traffic Policing Test 
----------------------------------------------------------------------------- 
          Failed           IR                 126.0    0.0      0.0E+00  0.0      0.0 
 
CBS Test 
----------------------------------------------------------------------------- 
          Passed 
 
EBS Test 
----------------------------------------------------------------------------- 
          Passed 
 
 
 
Performance Test Report 
----------------------------------------------------------------------------- 
Duration (Min) : 1 
Result         : Failed               P-bit/s 0 
 
P-bit    Result                          Tx Rate 
----------------------------------------------------------------------------- 
0        Failed          IR,Avail.       100.0 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
IR (Mbps) 
----------------------------------------------------------------------------- 
P-bit    IR        FLR     FTD     FDV         Avail 
                           (ms)    (ms)        (%) 
----------------------------------------------------------------------------- 
0        0.0       0.0E+00 0.0     0.0         1.66 
 
Counter 
Description 
Name 
Name of the tested service 
Destination MAC Address 
MAC address of the remote MEP 
Source MAC Address 
MAC address of the local MEP 
Inner Tag 
Value of the inner VLAN 
Outer Tag 
Value of the outer VLAN  
P-bit/s 
List of the P-bit values that were actually tested 
Scope 
Scope of the test: configuration test, performance test, or both phases 
Possible values: Configuration, Performance, Configuration + Performance 
Profile Name 
Profile used in the test 
Start Date & Time 
Date and time at the last test activation 
End Date & Time 
Date and time when the last test ended (regardless of the end result 
passed/failed/aborted) 
Total Duration 
Duration of the last test 
Overall Result 
Possible values: Not Applicable, Passed, Failed, User Aborted, System Aborted 
Configuration Test report (summary) 
P-bit 
Duration 
Duration of the configuration test (in seconds) 
Result 
Result of the last configuration test for the specific P-bit and if it failed, the 
reason for failure 
Possible Result values: Not Applicable, Passed, Failed, User Aborted, System 
Aborted 
Possible reasons for failure: CIR, EIR, Policing, and/or CBS test 
Test 
Name of the sub-test: CIR Test, EIR Test, Traffic Policing Test, CBS Test, EBS 
Test 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Counter 
Description 
Result 
Result of the sub-test 
Possible Result values: Not Applicable, Passed, Failed, User Aborted, System 
Aborted 
Reason for failure 
If sub-test failed, shows the reason(s) for failure. 
Possible reasons for failure: 
• CIR Test – FLR, FTD, or FDV 
• EIR Test – IR 
• Traffic Policing Test – IR 
• CBS Test – Burst size 
• EBS Test – Burst size 
Tx Rate (Mbps) 
Transmission rate to which the generator is configured in the subtest 
IR (Mbps) 
Average calculated Information Rate 
FLR 
Calculated Frame Loss Ratio 
FTD (ms) 
Average calculated Frame Transfer Delay 
FDV (ms) 
Average calculated Frame Delay Variation 
Performance test report (summary) 
Duration 
Duration of the performance test (in minutes) 
Result 
Performance test result summary for all CoS (p-bits) 
Possible values: Not Applicable, Passed, Failed, User Aborted, System Aborted 
If test failed, displays the failed CoS (p-bit(s)) 
P-bit 
P-bit (sub-test) that is included in the tested service 
Result 
Result of the sub-test for the CoS (p-bit)  
Possible values: Not Applicable, Passed, Failed, User Aborted, System Aborted 
Reason for failure 
If sub-test failed, displays the reason for failure: FLR, FTD, or FDV 
Tx Rate (Mbps) 
Transmission rate to which the generator is configured in the subtest 
IR (Mbps) 
Average calculated Information Rate 
FLR 
Calculated Frame Loss Ratio 
FTD (ms) 
Average calculated Frame Transfer Delay 
FDV (ms) 
Average calculated Frame Delay Variation 
Avail (%) 
Percentage of available time 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To display the detailed test results: 
• 
In the config>test>y1564>generator<generator-name># prompt, enter show report detailed. 
The detailed report screen is displayed. For information on the detailed test report counters, see 
the table below. 
ETX‑2i>config>test>y1564>generator(1)# show report detailed 
Services 
----------------------------------------------------------------------------- 
Destination MAC Address : 00-20-D2-50-95-A3 
Source MAC Address      : 00-20-D2-54-EF-EB 
Inner Tag               : ---                 Outer Tag  : 20 
P-bit/s                 : 1 
 
 
Summary 
----------------------------------------------------------------------------- 
Scope             : Configuration+Performance 
Profile Name      : 1 
Start Date & Time : 2017-05-21  13:04:44 
End Date & Time   : 2017-05-21  13:05:05 
Total Duration    : 00:00:21 
Overall Result    : Failed 
 
Configuration Test Report 
----------------------------------------------------------------------------- 
P-bit          : 0 
Duration (Sec) : 20 
Result         : Failed               CIR,EIR,Policing 
 
CIR Test 
----------------------------------------------------------------------------- 
Parameter        Step#1             Step#2           Step#3           Step#4       Thr 
---------------- --------           --------         --------         --------     ---- 
Tx Rate (Mbps)   25.0               ---              75.0             100.0 
IR - Min (Mbps)  0.0                ---              0.0              0.0 
IR - Mean (Mbps) 0.0                ---              0.0              0.0 
IR - Max (Mbps)  0.0                ---              0.0              0.0 
Tx Count         6101               ---              18301            24391 
Rx Count         0                  ---              0                0 
FL Count         6101               ---              18301            24391 
FLR              1.0E+00            ---              1.0E+00          1.0E+00      3.0E-04 
FTD - Min (ms)   0.004              ---              0.004            0.004 
FTD - Mean (ms)  0.004              ---              0.004            0.004        26.000 
FTD - Max (ms)   0.004              ---              0.004            0.004 
FTD - Std (ms)   0.0                ---              0.0              0.0 
FDV - Mean (ms)  0.0                ---              0.0              0.0          11.000 
FDV - Max (ms)   0.0                ---              0.0              0.0 
---------------- --------           --------         --------         --------     ---- 
Result           Failed             Not Applicable   Failed           Failed 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
EIR Test & Traffic Policing Test 
----------------------------------------------------------------------------- 
                 EIR              Policing           Thr 
---------------- --------         --------           -------- 
Tx Rate (Mbps)   101.0            126.0 
IR - Min (Mbps)  0.0              0.0 
IR - Mean (Mbps) 0.0              0.0                0.0 - 10.128 
IR - Max (Mbps)  0.0              0.0 
Tx Count         24633            0 
Rx Count         0                0 
FL Count         24633            0 
FLR              1.0E+00          0.0E+00 
FTD - Min (ms)   0.004            0.0 
FTD - Mean (ms)  0.004            0.0 
FTD - Max (ms)   0.004            0.0 
FTD - Std (ms)   0.0              0.0 
FDV - Mean (ms)  0.0              0.0 
FDV - Max (ms)   0.0              0.0 
---------------- --------         --------            -------- 
Result           Failed           Failed 
 
Burst Tests 
----------------------------------------------------------------------------- 
Parameter                         CBS                       EBS 
--------------------------------- --------                  -------- 
Number of Cycles                  24                        24 
Frames per Cycle                  70                        140 
Minimum Expected Frames           105881                    105730 
Actual Received Frames            106733                    159260 
--------------------------------- --------                  -------- 
Result                            Passed                    Passed 
 
 
Performance Test Report 
----------------------------------------------------------------------------- 
Duration (Min) : 1 
Result         : Failed               P-bit/s 0 
 
P-bit    Result                          Tx Rate 
----------------------------------------------------------------------------- 
0        Failed          IR,Avail.       100.0 
 
IR (Mbps) 
----------------------------------------------------------------------------- 
P-bit    Min       Mean      Max 
----------------------------------------------------------------------------- 
0        0.0       0.0       0.0 
 
FL 
----------------------------------------------------------------------------- 
P-bit    Count   FLR     Thr 
----------------------------------------------------------------------------- 
0        0       0.0E+00 3.0E-04 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
FTD (ms) 
----------------------------------------------------------------------------- 
P-bit    Min     Max     Std     Mean    Thr 
         (ms)    (ms)    (ms)    (ms) 
----------------------------------------------------------------------------- 
0        0.0     0.0     0.0     0.0     26.000 
 
FDV (ms) 
----------------------------------------------------------------------------- 
P-bit    Max         Mean        Thr 
         (ms)        (ms) 
----------------------------------------------------------------------------- 
0        0.0         0.0         11.000 
 
Availability 
----------------------------------------------------------------------------- 
P-bit    UAS         %           Thr (%) 
----------------------------------------------------------------------------- 
0        59          1.66        99.90 
 
Counter 
Description 
Tx Rate (Mbps) 
The transmission rate to which the generator is configured in the subtest 
IR – Min (Mbps) 
The minimum measured Information Rate 
IR – Mean (Mbps) 
The average calculated Information Rate 
Note: For EIR and Traffic Policing tests, displays under Thr column, the service 
acceptance criteria (SAC). 
IR – Max (Mbps) 
The maximum measured Information Rate 
Tx Count 
Number of transmitted frames 
Rx Count 
Number of received frames 
FL Count 
The number of lost frames  
FLR 
The calculated Frame Loss Ratio 
FTD – Min (ms) 
The minimum measured Frame Transfer Delay 
FTD – Mean (ms) 
The average calculated Frame Transfer Delay 
FTD – Max (ms) 
The maximum measured Frame Transfer Delay 
FTD – Std (ms) 
The calculated standard deviation of the Frame Transfer Delay 
FDV – Mean (ms) 
The average calculated Frame Delay Variation 
FDV – Max (ms) 
The maximum calculated Frame Delay Variation 
UAS 
The number of unavailable seconds 