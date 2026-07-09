# Feature Reference – 8 Monitoring and Diagnostics – 8.5 Layer-3 Service Activation Test

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1424–1461.*


## Applicability and Scaling  *(p.1424)*


## Standards  *(p.1424)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Message 
Cause 
Corrective Action 
Tried removing VLAN definition 
while responder was active 
(status ‘idle’ or ‘ready’). 
Shut down the responder and then 
remove the VLAN definition. 
Cannot modify; TWAMP 
responder is active 
Tried modifying the bound port 
definition while responder was 
active (status ‘idle’ or ‘ready’). 
Shut down the responder and then 
modify the bound port definition. 
Tried modifying VLAN definition 
while responder was active 
(status ‘idle’ or ‘ready’). 
Shut down the responder and then 
modify the VLAN definition. 
Tried modifying responder’s 
router entity number while 
responder was active (status 
‘idle’ or ‘ready’). 
Shut down the responder and then 
modify the router entity number. 
Tried modifying responder’s 
local IP address while responder 
was active (status ‘idle’ or 
‘ready’). 
Shut down the responder and then 
modify the local IP address. 
 
8.5 Layer-3 Service Activation Test 
The Layer-3 service activation test (L3 SAT) provides an out-of-service (intrusive) IP/UDP test to assess 
the proper configuration and performance of an IP transport service prior to customer notification and 
delivery. 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. Each product can have up to eight generators and eight 
responders. 
Standards 
ITU-T Y.1564 

## Functional Description  *(p.1425)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Functional Description 
L3 SAT testing has the following objectives: 
• 
Validates that the IP transport service is correctly configured. 
• 
Validates the quality of the services as delivered to the end user. 
L3 SAT tests can be performed over Layer-3 networks, or as a Layer-3 service over a Layer-2 network.  
Test Phases 
The methodology has a service configuration test phase followed by a service performance test phase; 
the service configuration test is short in order to prevent wasted time caused by failed service 
performance tests. The test flowchart below illustrates the two phases. 
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
service performance test. The following are performed: 
• 
Preliminary (common for all test sessions): 
 
Verify connectivity – If the connectivity subtest fails, the configuration test fails and the L3 
SAT to the relevant peer is stopped. Otherwise, the detected responder type is recorded and 
shown in the test report. 
 
Determine the path MTU – If the MTU subtest fails, the configuration test fails and the L3 
SAT to the relevant peer is stopped. Otherwise, the discovered MTU is recorded and shown 
in the test report. 
Note 
The preliminary tests are always performed, even if the configuration phase is 
not included in the scope of the test. 
• 
Bandwidth subtests (one test session at a time): 
 
Step load  
 
Policing 
The bandwidth subtests are performed for the packet sizes configured for the test session. They are 
performed in increasing order of packet size, one packet size at a time. The bandwidth subtest is 
successful if the subtest results are within the configured Service Acceptance Criteria (SAC) limits. 
If a bandwidth subtest fails for a particular packet size, the testing for that packet size continues and all 
remaining bandwidth subtests are performed. 
If packet sizes larger than the discovered MTU were configured for the test session, the bandwidth 
subtest is considered failed for these packet sizes; it is not performed for packet sizes larger than the 
MTU.  
A test session is declared successful only if the results for all tested packet sizes are within SAC limits. 
Note 
When the report-type parameter is clock-sync (report includes parameters 
requiring synchronization) and the responder type is loop and timestamp, an 
additional requirement for a test session to be declared successful is that 
there were no out-of-sync seconds during the test. 
The configuration test is declared successful if the results for all the test sessions are successful. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Performance Test 
The performance test validates the quality of the services over a user-configurable period of time, as 
follows: 
• 
Traffic is generated for all services at the configured bandwidth level.  
• 
For all the test sessions, test packets are sent simultaneously at 100% of the bandwidth 
configured per test session. 
• 
Per test session, the duration of the performance test is evenly divided between the different 
packet sizes, e.g., per test session, each packet size is transmitted for an equal amount of time. 
The performance test is declared successful if the results are within SAC limits. 
Note 
When the report-type parameter is clock-sync (report includes parameters 
requiring synchronization) and the responder type is loop and timestamp, an 
additional requirement for the performance test to be declared successful is 
that during the test, at least one minute was not excluded due to 
unavailability or out-of-sync. 
Test Elements 
L3 SAT includes the following elements: 
Generators 
Initiate multiple test sessions for multiple responders, send out the test and OAM frames, 
receive responses from the responder(s), process the resulting measurements, and display 
test reports. Generators can support mixed responder types. 
Peers 
Used to run TWAMP test sessions. One or more peers can be configured per generator with IP 
address(es) corresponding to responder(s). 
Test Sessions 
One or more test sessions can be configured per peer. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Responders 
Receive test and OAM frames from generator and transmit responses to generator. 
Responders can be of the following types: 
• IP loop – filters incoming traffic by destination IP address, and loops back the packets 
while performing MAC address swap and IP address swap. 
An IP loop responder is implemented by activating the L3 SAT responder in UDP agnostic 
mode. In this mode, no TWAMP Light responder is created, and the L3 SAT responder 
performs an IP loop (regardless of UDP port, if it at all exists) on both incoming test packet 
streams. 
This mode is implemented by setting the UDP port to 0 in the responder configuration. 
• UDP loop – filters incoming traffic by destination IP address and UDP port, and loops back 
the packets while performing MAC address swap, IP address, and UDP port swap 
• Loop and timestamp – filters incoming traffic by destination IP address and UDP port and 
performs IP loop for loss measurement packets, UDP loop with timestamp for delay 
measurement packets. 
The newly introduced ‘Loaned Address’ functionality blocks UNI traffic and sends a gratuitous 
Address Resolution Protocol (G.ARP) to the network router to update its ARP table with the 
responder’s MAC address.  
 
Note 
Responders can be ETX‑2i devices or third-party devices. Third-party 
responders can be only IP loop or UDP loop types. Only ETX‑2i can be a loop 
and timestamp responder, and only an ETX‑2i responder can provide one-way 
metrics. 
 
 
L3 SAT Generators and Responders 

## Factory Defaults  *(p.1429)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Factory Defaults 
By default, there are no L3 SAT entities configured in ETX‑2i. 
When a peer profile is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
bw-steps  
25 50 75 100  
configuration-duration 
100 
performance-duration 
120 
policing-test 
policing-test 
report-type 
no-clock-sync 
scope 
configuration performance 
udp-port 
53248 
When a session profile is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
availability-threshold 
9990 
delay-threshold 
200000 
delay-variation-threshold 
100000 
ip-size 
256 
loss-ratio-threshold 
1000 
When a peer is created, there is no default configuration. 
When a test session is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
<name> 
<Not applicable> 
<name> must be specified when the test 
session is created. 
session-profile  
<Not applicable> 
<profile-name> must be specified when the 
test session is created. 
bw 
<Not applicable> 
<kbps> must be specified when the test 
session is created. 
dscp 
0 

## Configuring L3 SAT Entities  *(p.1430)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
When a generator is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
bind 
<not applicable> 
This parameter has no default configuration. 
local-ip-address 
<not applicable> 
This parameter has no default configuration. 
router-entity 
1 
vlan-tag 
<not applicable> 
This parameter has no default configuration. 
When a responder is created, it has the following default configuration. 
Parameter 
Default  
Remarks 
bind 
<not applicable> 
This parameter has no default configuration. 
local-ip-address 
<not applicable> 
This parameter has no default configuration. 
router-entity 
1 
udp-port 
53248  
vlan-tag 
<not applicable> 
This parameter has no default configuration. 
Configuring L3 SAT Entities 
 To configure L3 SAT, perform the following steps: 
1. In the responder device: 
e. Configure relevant SVI port, router interface, and flows. 
f. 
Configure and activate L3 SAT responder. 
2. In the generator device: 
g. Configure relevant SVI port, router interface, and flows. 
h. Configure L3 SAT peer and session profile(s). 
i. 
Configure and activate L3 SAT generator and relevant peers and test sessions. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuring Generators 
 To configure L3 SAT generators: 
1. Navigate to configure test l3sat. 
2. Enter: generator <name> [l2-probe]  
where name is a meaningful name for the L3 SAT generator; 1-32 character string  
Note 
The optional parameter l2-probe is used to specify Layer-3 over Layer-2 
operation. The default without the parameter is Layer-3 service. 
The config>test>l3sat>generator(<name>)# prompt is displayed. 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Binding generator to the port 
over which to test the service  
[no] bind ethernet <port-index> 
[no] bind logical-mac <port-number> 
[no] bind pcs <port-number> 
Visible if generator is working in 
layer-2 probe mode. Otherwise, 
masked. 
Configuring L3 SAT generator IP 
address 
local-ip-address <ip-address> 
ip-address – IP address of L3 SAT 
generator 
Defining peer entity 
(corresponding to responder) 
peer <ip-address> 
See Running Test Sessions Via 
Controller Peers. 
Associating generator with a 
router that contains a suitable 
router interface 
router-entity <number> 
number – number of the router under 
which L3SAT is performed.  
Router must contain a suitable router 
interface, which must be configured 
with the same IP address as 
local-ip-address. 
Setting tag structure of test 
packets 
vlan-tag <vlan> p-bit fixed <p-bit> 
[inner-vlan <inner-vlan>] 
[inner-p-bit <inner-p-bit>]  
vlan-tag <vlan> p-bit marking 
<dscp-to-pbit-profile> [inner-vlan 
<inner-vlan>] [inner-p-bit <inner-p-bit>] 
no vlan-tag <vlan> 
Visible if generator is working in 
layer-2 probe mode. Otherwise, 
masked. 
vlan – Outer VLAN tag of test packets 
Possible values: 0-4095 
p-bit– Outer VLAN priority (p-bit) of 
test packets 
Possible values: 0-7 
inner-vlan – Inner VLAN tag of test 
packets 
Possible values: 0-4095 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
inner-p-bit – Inner VLAN priority of 
test packets 
Possible values: 0-7 
dscp-to-pbit-profile – Marking profile 
used to mark outer VLAN priority (p-
bit) of test packets 
Possible values: up to 32-character 
string 
Administratively enabling L3 
SAT generator 
no shutdown 
Enter shutdown to administratively 
disable the generator. 
You should enable the generator only 
after at least one responder has been 
configured and enabled. 
Viewing L3 SAT generator status 
show status 
See Viewing L3 SAT Generator Status. 
 
Configuring Peers 
 To configure L3 SAT peers: 
1. Navigate to configure test l3sat generator <name>. 
2. Enter: peer <ip-address>  
The prompt config>test>l3sat>generator(<name>)> peer(<ip-address>)# is displayed. 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Activating or deactivating the 
peer test sessions 
activate 
no activate 
You can activate a peer only if at 
least one test session has been 
configured. 
Note: This command is not 
included in the configuration 
text file. 
Assigning a peer profile to use for 
the peer parameters 
peer-profile <profile-name> 
profile-name – name of profile 
used for peer parameters 
Possible values: Up to 32-
character string 
Note: A profile with this name 
must already exist. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Assigning a test session 
test-session <name> session-profile 
<profile-name> bw <kbps> 
[dscp <number>] 
no test-session <name> 
Multiple test sessions can be 
defined in the peer. 
name – meaningful test session 
name 
Possible values: Up to 32-
character string 
profile-name – name of profile 
used for test session parameters 
Possible values: Up to 32-
character string 
Note: A profile with this name 
must already exist. 
bw – rate of test session traffic 
in Kbps 
dscp – priority value for test 
session traffic 
Possible values: 0-63 
Displaying results and 
measurements for a specific test 
show report <test-name> 
Available only if peer was 
activated 
See Viewing Detailed Test 
Results. 
Displaying summary of test 
results and measurements 
show summary-report 
Available only if peer was 
activated 
See Viewing Summary Test 
Results. 
Displaying the peer status 
show status 
See Viewing L3 SAT Generator 
Peer Status. 
 
Configuring Peer Profiles 
 To configure L3 SAT peer profiles: 
1. Navigate to configure test l3sat. 
2. Enter: peer-profile <name> 
The prompt config>test>l3sat> peer-profile(<name>)# is displayed. 
3. Perform the required tasks according to the following table. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Setting the number of steps and 
their transmission rate in the 
bandwidth subtest 
bw-steps <s1-percent>  
bw-steps <s1-percent> <s2-percent> 
bw-steps <s1-percent> 
<s2-percent><s3-percent> 
bw-steps <s1-percent> <s2-percent> 
<s3-percent><s4-percent> 
s1-percent – transmission rate, as 
percentage of configured 
bandwidth, at the first step of the 
step load subtest (1–100) 
s2-percent – transmission rate, as 
percentage of configured 
bandwidth, at the second step of 
the step load subtest (1–100) 
s3-percent – transmission rate, as 
percentage of configured 
bandwidth, at the third step of 
the step load subtest (1–100) 
s4-percent – transmission rate, as 
percentage of configured 
bandwidth, at the fourth step of 
the step load subtest (1–100) 
Note: You can define fewer than 
four steps as long as the last step 
is 100%. 
 
Defining the duration of the 
configuration phase for each test 
session 
configuration-duration <seconds> 
Possible values: 60–300 seconds 
Defining the duration in minutes 
of the performance phase  
performance-duration [15m] [2h] 
[24h] [custom <custom>] 
Possible values: 15 minutes, 2 
hours, 24 hours, or a custom 
duration (1–7200 minutes) 
Specifying whether to include or 
exclude the traffic policing 
subtest from the configuration 
phase 
policing-test 
no policing-test 
 
Defining which parameters are 
included in the test report 
report-type {clock-sync | 
no-clock-sync} 
clock-sync – Include parameters 
requiring synchronization. 
no-clock-sync – Do not include 
parameters requiring 
synchronization. 
See Viewing L3 SAT Test Reports 
for details on which parameters 
are included in the test report. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Setting the scope of the test: 
configuration test, performance 
test, or both 
scope [configuration] [performance] 
You can enter the command with 
one or both parameters.  
Specifying start of the range of 
UDP ports that are used in the 
tests 
udp-port <port> 
Possible values: 0–65504 
  
Configuring Session Profiles 
 To configure L3 SAT session profiles: 
1. Navigate to configure test l3sat. 
The config>test>l3sat# prompt is displayed. 
2. Enter: session-profile <name> 
The prompt config>test>l3sat>session-profile(<name>)# is displayed. 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Defining Availability service 
acceptance criteria 
availability-threshold <availability> 
Availability is measured in 
hundredths of percent units (for 
example, use value 8930 in 
order to define 89.3%). 
Possible values: 0–10000 
Defining Packet Transfer Delay 
service acceptance criteria, in 
microseconds 
delay-threshold <μs> 
Possible values: 0–1000000 
Defining Packet Delay Variation 
service acceptance criteria, in 
microseconds 
delay-variation-threshold <μs> 
Possible values: 0–1000000 
Defining test packet size 
ip-size [64] [128] [256] [512] [1024] 
[1280] [1500] [mtu] [custom <size>] 
You can specify up to four 
packet sizes. 
Range for size: 
52–2000 
Setting the calculation of the test 
in L2 rate 
[no] l2-rate 
no l2-rate (default) expresses 
the service rate in L3 terms. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Defining Packet Loss Ratio service 
acceptance criteria, in ppm (1E-6 
units) 
loss-ratio-threshold <ppm>  
Possible values: 0–1000000 
 
Configuring Responders 
Note 
During activation of the L3 SAT responder, avoid shutting down or modifying 
relevant traffic flows. Shutting down a relevant flow stops responder 
operation, and it does not resume even after reactivating the flow. In this 
case, you must apply a shutdown/no shutdown cycle to the L3 SAT responder. 
 To configure L3 SAT responders: 
1. Navigate to configure test l3sat. 
2. Enter: responder <name> [l2-probe]  
where name is a meaningful name for the L3 SAT responder; 1–32-character string. 
Note 
The optional parameter l2-probe is used to specify Layer-3 over Layer-2 
operation. The default without the parameter is Layer-3 service. 
The config>test>l3sat>responder(<name>)# prompt is displayed. 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Binding responder to the port 
over which to test the service 
[no] bind ethernet <port-index> 
[no] bind logical-mac <port-number> 
[no] bind pcs <port-number> 
Visible if the responder is working in 
layer-2 probe mode. Otherwise, 
masked. 
Configuring L3 SAT responder 
IP address 
local-ip-address <ip-address> 
 
Associating responder with a 
router that contains a suitable 
router interface 
router-entity <number> 
number – number of router under 
which L3 SAT is performed.  
Router must contain a suitable router 
interface, which must be configured 
with the same IP address as 
local-ip-address. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Specifying start of the range 
of UDP ports that are used in 
the tests or setting L3 SAT 
responder to UDP agnostic 
mode 
[no] udp-port <port> 
port – start of range of UDP ports used 
in test 
Possible values:  
0 – 65504 
Where 
0 = no udp-port; UDP agnostic mode          
Note: The port number must be a 
multiple of 16. 
Setting tag structure of test 
packets 
vlan-tag <vlan> p-bit fixed <p-bit> 
[inner-vlan <inner-vlan>] 
[inner-p-bit <inner-p-bit>]  
vlan-tag <vlan> p-bit marking 
<dscp-to-pbit-profile> [inner-vlan 
<inner-vlan>] [inner-p-bit <inner-p-bit>] 
Visible if responder is working in layer-2 
probe mode. Otherwise, masked. 
vlan – Outer VLAN tag of test packets 
Possible values: 0-4095 
p-bit– Outer VLAN priority (p-bit) of test 
packets 
Possible values: 0-7 
inner-vlan – Inner VLAN tag of test 
packets 
Possible values: 0-4095 
inner-p-bit – Inner VLAN priority of test 
packets 
Possible values: 0-7 
dscp-to-pbit-profile – Marking profile 
used to mark outer VLAN priority (p-bit) 
of test packets 
Possible values: up to 32-character 
string 
Setting up Loaned Addresses 
to block UNI traffic 
[no] loaned-address 
Enabling/disabling the Loaned addresses 
parameter. 
Allowing responder traffic to 
run via UNI to NNI policer. 
[no] service-policer 
Including/excluding a policer to the L3 
SAT responder test path from the UNI to 
the NNI. 
Administratively enabling the 
responder 
no shutdown 
Enter shutdown to administratively 
disable the responder. 
Viewing responder status 
show status 
See Viewing L3 SAT Responder Status. 
 
 
 

## Viewing L3 SAT Test Status  *(p.1438)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing L3 SAT Test Status 
You can view the status of the test as it is running. 
Viewing L3 SAT Generator Status 
 To display the test status (generator side): 
• 
At the config>test>l3sat>generator(<generator-name>)# prompt, enter: 
show status 
For information on the status parameters, see the following table. 
ETX‑2i>config>test>l3sat>generator(gen1)# show status 
Application Type             : L3 Over L2 
Router Entity                : 1 
Router Interface             : 1 
Router Interface oper status : UP 
Generator Status             : Ready 
Tx Flow                      : 4_1_to_1_1 
Rx Flow                      : 1_1_to_4_1 
 
Parameter 
Description 
Application Type 
Role of the generator device in the service path 
Possible values:  
• Pure L3 – L3 forwarder 
• L3 over L2 – L2 probe 
Router Entity 
Number of the router under which L3 SAT is performed  
Router Interface 
Associated router interface ID  
Router Interface oper 
status 
Status of associated router interface 
Possible values: Up, Down 
Generator Status 
Current status of L3 SAT generator 
Possible values: Shutdown, Idle, Ready, In Progress  
Tx Flow 
Name of egress flow used by generator 
Note: Displayed only for L2 probe mode 
Rx Flow 
Name of ingress flow used by generator 
Note: Displayed only for L2 probe mode 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing L3 SAT Generator Peer Status 
 To display the test status (peer at generator side): 
• 
At the config>test>l3sat>generator(<generator-name>)>peer(<ip-address>)# prompt, enter: 
show status 
For information on the status parameters, see the following table. 
ETX‑2i>config>test>l3sat>generator(gen3)>peer(50.50.50.101)# show status 
Last Connectivity Sub-test : Passed 
Last MTU Sub-test          : Not Applicable 
  
Responder Type             : Loop & Timestamp 
Elapsed Time               : 00:00:02 
Time Remaining             : 00:13:26 
Current Phase              : 
TOD Status                 : Unknown 
  
Test Name                        LM UDP Ports   DM UDP Ports   Status 
----------------------------------------------------------------------------- 
test1                            53249, 53249   53248, 53248   In Progress 
test2                            53251, 53251   53250, 53250   In Progress 
test3                            53253, 53253   53252, 53252   In Progress 
test4                            53255, 53255   53254, 53254   In Progress 
test5                            53257, 53257   53256, 53256   In Progress 
test6                            53259, 53259   53258, 53258   In Progress 
test7                            53261, 53261   53260, 53260   In Progress 
test8                            53263, 53263   53262, 53262   In Progress 
 
ETX‑2i>config>test>l3sat>generator(gen1)>peer(10.10.10.20)# show status 
Last Connectivity Sub-test : Passed 
Last MTU Sub-test          : Not Applicable 
 
Responder Type             : Loop & Timestamp 
TOD Status                 : Unknown 
 
Test Name                        LM UDP Ports   DM UDP Ports   Status 
----------------------------------------------------------------------------- 
test1                            53249, 53249   53248, 53248   Passed 
 
Note 
• 
Elapsed Time includes the time it has so far taken to perform the steps, 
including the inter-step wait time.  
• 
Elapsed Time, Time Remaining, and Current Phase are displayed only 
while test Status is In Progress. 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Description 
Last Connectivity Sub-test 
Result of last connectivity sub-test  
Possible values: Not Applicable, Passed, Failed 
Last MTU Sub-test 
Result of last MTU sub-test  
Possible values: Not Applicable, Passed, Failed 
Responder Type 
Discovered type of the responder 
Possible values: Unknown, IP loop, UDP loop, Loop & Timestamp 
Elapsed Time 
Elapsed time of current test 
Note: Displayed only when status of at least one test is ‘In Progress’. 
Time Remaining 
Time remaining until end of test 
Note: Displayed only when status of at least one test is ‘In Progress’.  
Current Phase 
Current phase of test 
Possible values: Configuration, Performance 
Note: Displayed only when status of at least one test is ‘In Progress’. 
TOD Status 
Current TOD synchronization state with responder device 
Possible values: Sync, Out-of-sync, Unknown 
Test Name 
Test session name 
Possible values: Variable length string, up to 32 characters 
LM UDP Ports 
L4 source and destination ports of loss measurement stream 
Possible values: 0-65504 
                             N/A – if responder type is unknown 
DM UDP Ports 
L4 source and destination ports of delay measurement stream 
Possible values: 0-65504 
                             N/A – if responder type is unknown 
Status 
Current status of test session 
Possible values: Idle, Ready, In Progress, Passed, Failed, User Aborted, 
System Aborted 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing L3 SAT Responder Status 
 To display the test status (responder side): 
• 
At the config>test>l3sat>responder(<responder-name>)# prompt, enter: 
show status  
For information on the status parameters, see the following table. 
ETX‑2i>config>test>l3sat>responder(res1)# show status 
Application Type             : L3 Over L2 
Router Entity                : 1 
Router Interface             : 1 
Router Interface oper status : UP 
Responder Status             : Ready 
Total LM / DM Rx. Packets    : 128521202 / 12440 
Tx Flow                      : 3_to_1 
Rx Flow                      : 1_to_3 
 
Parameter 
Description 
Application Type 
Role of the responder device in the service path 
Possible values:  
• Pure L3 – L3 forwarder 
• L3 over L2 – L2 probe 
Router Entity 
Number of the router under which L3 SAT is performed  
Router Interface 
Associated router interface ID  
Router Interface oper 
status 
Status of associated router interface 
Possible values: Up, Down 
Responder Status 
Current status of L3 SAT responder 
Possible values: Shutdown, Idle, Ready  
Total LM / DM Rx. 
Packets 
Total number of packets received on all loss measurement / delay measurement 
streams 
Tx Flow 
Visible for layer-2 probe mode only 
Name of egress flow used by responder 
Note: Displayed only for L2 probe 
Rx Flow 
Visible for layer-2 probe mode only 
Name of ingress flow used by responder 
Note: Displayed only for L2 probe 

## Viewing L3 SAT Test Reports  *(p.1442)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing L3 SAT Test Reports 
The generator calculates performance parameters according to the received test packets, for each peer 
and its active test sessions. The performance parameters are recalculated every minute. The 
performance parameters are presented in test reports that can be viewed per peer and test session. 
Note 
Unavailable and out-of-sync time affect parameter evaluation as follows: 
• 
A minute is considered unavailable if it has more than 75% packet loss; 
therefore, it is considered available if it has packet loss less than or equal 
to 25%. Unavailable time is not used for performance parameter 
evaluation and comparison with test objectives. 
• 
A minute is considered out-of-sync if during the minute there was no 
accurate TOD synchronization between the generator device and the 
responder device. Out-of-sync time is not used for forward and backward 
packet transfer delay (PTD) evaluation and comparison with test 
objectives. 
Viewing Summary Test Results 
 To display summary test results: 
• 
At the config>test>l3sat>generator(<generator-name>)>peer(<IP-address>)# prompt, enter: 
show summary-report 
For information on the summary test parameters, see the following table. 
ETX‑2i>config>test>l3sat>generator(gen1)>peer(10.10.10.20)# show summary-report 
End Points 
Generator Address : 10.10.10.10 
Responder Address : 10.10.10.20 
Responder Type    : Loop & Timestamp 
MTU (bytes)       : 1500 
Tx Flow           : 4_1_to_1_1 
Rx Flow           : 1_1_to_4_1 
 
Test 
Scope             : Configuration + Performance 
Peer Profile Name : peer1 
Start Date & Time : 2019-04-15  18:59:36 
End Date & Time   : 2019-04-15  19:06:42 
Total Duration    : 426 
Overall Result    : Passed 
 
Test Name                        BW     DSCP Conf. Result   Perf. Result 
                                 (Mbps) 
----------------------------------------------------------------------------- 
test1                            100.00023   Passed         Passed 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Description 
Generator Address 
IP address of L3 SAT generator 
Responder Address 
IP address of L3 SAT peer 
Responder Type 
Discovered type of responder 
Possible values: Unknown, IP loop, UDP loop, Loop & Timestamp 
MTU 
Discovered IP MTU of path to responder 
Possible values: 68-2094; N/A if the connectivity or MTU sub-tests failed 
Tx Flow 
Name of egress flow used by generator 
Note: Displayed only for L2 probe mode 
Rx Flow 
Name of ingress flow used by generator 
Note: Displayed only for L2 probe mode 
Scope 
Scope of test 
Possible values: Configuration, Performance, Configuration + Performance 
Peer Profile Name 
Profile used for peer parameters 
Possible values: variable length string up to 32 characters 
Start Date & Time 
Date and time at last peer activation 
End Date & Time 
Date and time when last test ended 
Total Duration 
Duration of last test 
Out-of-sync Time 
Number of seconds there was no TOD synchronization with the responder device 
Note: Displayed only when Peer Profile report-type is no clock-sync. 
Overall Result 
Overall result of last test 
Possible values: Not Applicable, Passed, Failed, User Aborted, System Aborted 
Test Name 
Test session name 
Possible values: variable length string up to 32 characters 
BW 
Rate of test session traffic 
DSCP 
Priority value for test session traffic 
Possible values: 0-63 
Conf. Result 
Result of Configuration phase 
Possible values: Not Applicable, Passed, Failed, User Aborted, System Aborted 
Perf. Result 
Result of last Performance phase 
Possible values: Not Applicable, Passed, Failed, User Aborted, System Aborted 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing Detailed Test Results 
This section shows the detailed reports for L3 SAT performed both with and without clock 
synchronization. For information on the report header parameters and detailed test report counters, 
see table below. 
 To display detailed test results for L3 SAT with no clock synchronization: 
• 
At the config>test>l3sat>generator(<generator-name>)>peer(<IP-address>)# prompt, enter: 
show report <test-name> 
The detailed report is displayed. 
ETX‑2i>config>test>l3sat>generator(gen3)>peer(50.50.50.101)# show report test1 
End Points 
Generator Address    : 10.10.10.10 
Responder Address    : 10.10.10.20 
Responder Type       : Loop & Timestamp 
LM UDP Ports         : 53249, 53249 
DM UDP Ports         : 53248, 53248 
MTU (bytes)          : 1500 
Tx Flow              : 4_1_to_1_1 
Rx Flow              : 1_1_to_4_1 
 
Test 
Scope                : Configuration + Performance 
Peer Profile Name    : peer1 
Report Type          : No Clock Sync 
BW (Mbps)            : 100.000 
DSCP                 : 23 
IP Sizes (bytes)     : 64 
Session Profile Name : session1 
Start Date & Time    : 2019-04-15  18:59:36 
End Date & Time      : 2019-04-15  19:06:42 
Total Duration       : 426 
Overall Result       : Passed 
 
 
Configuration Phase 
----------------------------------------------------------------------------- 
Duration (sec)       : 120 
Configuration Result : Passed 
 
 
IP Size (bytes) : 64 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Step Load 
----------------------------------------------------------------------------- 
Parameter             Step#1     Step#2     Step#3     Step#4     Thr 
----------------      --------   --------   --------   --------   -------- 
Tx Rate (L3) (Mbps)   19.040     38.083     57.128     76.167 
IR (L3) - mean (Mbps) 19.040     38.083     57.128     76.167 
Tx Rate (L2) (Mbps)   24.990     49.983     74.980     99.969 
IR (L2) - mean (Mbps) 24.990     49.983     74.980     99.969 
PL - count            0          0          0          0 
PLR                   0          0          0          0          1.000E-3 
PTD - min (ms)        0.074      0.074      0.074      0.074 
PTD - mean (ms)       0.075      0.075      0.075      0.086      200.000 
PTD - max (ms)        0.076      0.076      0.250      0.322 
PTD - std (ms)        0.000      0.000      0.011      0.044 
PDV - mean (ms)       0.001      0.001      0.001      0.012 
PDV - max (ms)        0.002      0.002      0.176      0.248      100.000 
IPDV-Fwd - mean (ms)  0.000      0.000      0.000      0.000 
IPDV-Fwd - max (ms)   0.001      0.002      0.002      0.002 
IPDV-Bck - mean (ms)  0.000      0.000      0.001      0.019 
IPDV-Bck - max (ms)   0.001      0.001      0.176      0.248 
----------------      --------   --------   --------   --------   -------- 
Result                Passed     Passed     Passed     Passed 
 
Policing 
 
 
 
----------------------------------------------------------------- 
Parameter             Policing       Thr 
----------------      --------       -------- 
Tx Rate (L3) (Mbps)   95.208 
IR (L3) - mean (Mbps) 76.200 
Tx Rate (L2) (Mbps)   124.960 
IR (L2) - mean (Mbps) 100.012 
PL - count            816757 
PLR                   1.0E-1         1.000E-3 
PTD - min (ms)        0.075 
PTD - mean (ms)       3.937          200.000 
PTD - max (ms)        4.182 
PTD - std (ms)        0.694 
PDV - mean (ms)       3.862 
PDV - max (ms)        4.107          100.000 
IPDV-Fwd - mean (ms)  0.092 
IPDV-Fwd - max (ms)   3.586 
IPDV-Bck - mean (ms)  0.002 
IPDV-Bck - max (ms)   0.172 
----------------      --------       -------- 
Result                Passed 
 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Performance Phase 
----------------------------------------------------------------------------- 
Duration (min)       : 5 
Configuration Result : Passed 
 
Parameter             IP Size #1 IP Size #2 IP Size #3 IP Size #4 Thr 
                      64 bytes   0 bytes    0 bytes    0 bytes 
----------------      --------   --------   --------   --------   -------- 
Duration (min)        5 
Tx Rate (L3) (Mbps)   76.166 
IR (L3) - mean (Mbps) 76.166 
Tx Rate (L2) (Mbps)   99.967 
IR (L2) - mean (Mbps) 99.967 
PL - count            0 
PLR                   0          0          0          0          1.000E-3 
UAS - count           0 
Availability (%)      100.00                                      99.90 
PTD - min (ms)        0.074 
PTD - mean (ms)       0.075                                       200.000 
PTD - max (ms)        0.077 
PTD - std (ms)        0.000 
PDV - mean (ms)       0.001 
PDV - max (ms)        0.003                                       100.000 
IPDV-Fwd - mean (ms)  0.000 
IPDV-Fwd - max (ms)   0.002 
IPDV-Bck - mean (ms)  0.000 
IPDV-Bck - max (ms)   0.002 
PD-Fwd - count        0 
PDR-Fwd               0          0          0          0 
PD-Bck - count        0 
PDR-Bck               0          0          0          0 
PR-Fwd - count        0 
PRR-Fwd               0          0          0          0 
PR-Bck - count        0 
PRR-Bck               0          0          0          0 
----------------      --------   --------   --------   --------   -------- 
Result                Passed 
 To display detailed test results for L3 SAT with clock synchronization: 
ETX‑2i>config>test>l3sat>generator(gen1)>peer(10.10.10.20)# show report test1 
End Points 
Generator Address    : 10.10.10.10 
Responder Address    : 10.10.10.20 
Responder Type       : Loop & Timestamp 
LM UDP Ports         : 53249, 53249 
DM UDP Ports         : 53248, 53248 
MTU (bytes)          : 1500 
Tx Flow              : 4_1_to_1_1 
Rx Flow              : 1_1_to_4_1 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Test 
Scope                : Configuration + Performance 
Peer Profile Name    : peer1 
Report Type          : Clock Sync 
BW (Mbps)            : 100.000 
DSCP                 : 23 
IP Sizes (bytes)     : 64 
Session Profile Name : session1 
Start Date & Time    : 2019-05-01  16:47:18 
End Date & Time      : 2019-05-01  16:54:23 
Total Duration       : 425 
Out-of-sync Time     : 0 
Overall Result       : Passed 
 
 
Configuration Phase 
----------------------------------------------------------------------------- 
Duration (sec)       : 120 
Configuration Result : Passed 
 
 
IP Size (bytes) : 64 
 
Step Load 
----------------------------------------------------------------------------- 
Parameter             Step#1     Step#2     Step#3     Step#4     Thr 
----------------      --------   --------   --------   --------   -------- 
Tx Rate (L3) (Mbps)   19.040     38.083     57.124     76.166 
IR (L3) - mean (Mbps) 19.040     38.083     57.124     76.166 
Tx Rate (L2) (Mbps)   24.990     49.983     74.975     99.967 
IR (L2) - mean (Mbps) 24.990     49.983     74.975     99.967 
PL - count            0          0          0          0 
PLR                   0          0          0          0          1.000E-3 
PTD-Fwd - min (ms)    0.000      0.000      0.000      0.000 
PTD-Fwd - mean (ms)   0.000      0.000      0.000      0.000      200.000 
PTD-Fwd - max (ms)    0.000      0.000      0.000      0.000 
PTD-Fwd - std (ms)    0.000      0.000      0.000      0.000 
PTD-Bck - min (ms)    0.000      0.000      0.000      0.000 
PTD-Bck - mean (ms)   0.000      0.000      0.000      0.000      200.000 
PTD-Bck - max (ms)    0.000      0.000      0.000      0.000 
PTD-Bck - std (ms)    0.000      0.000      0.000      0.000 
PDV-Fwd - mean (ms)   0.000      0.000      0.000      0.000 
PDV-Fwd - max (ms)    0.002      0.002      0.002      0.002      100.000 
PDV-Bck - mean (ms)   0.000      0.000      0.000      0.000 
PDV-Bck - max (ms)    0.001      0.002      0.001      0.002      100.000 
IPDV-Fwd - mean (ms)  0.000      0.000      0.000      0.000 
IPDV-Fwd - max (ms)   0.002      0.002      0.002      0.002 
IPDV-Bck - mean (ms)  0.000      0.000      0.000      0.000 
IPDV-Bck - max (ms)   0.001      0.002      0.001      0.002 
----------------      --------   --------   --------   --------   -------- 
Result                Passed     Passed     Passed     Passed 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Policing 
----------------------------------------------------------------------------- 
Parameter             Policing       Thr 
----------------      --------       -------- 
Tx Rate (L3) (Mbps)   95.209 
IR (L3) - mean (Mbps) 76.201 
Tx Rate (L2) (Mbps)   124.961 
IR (L2) - mean (Mbps) 100.013 
PL - count            816753 
PLR                   1.0E-1         1.000E-3 
PTD-Fwd - min (ms)    0.000 
PTD-Fwd - mean (ms)   0.000          200.000 
PTD-Fwd - max (ms)    0.000 
PTD-Fwd - std (ms)    0.000 
PTD-Bck - min (ms)    0.000 
PTD-Bck - mean (ms)   0.000          200.000 
PTD-Bck - max (ms)    0.000 
PTD-Bck - std (ms)    0.000 
PDV-Fwd - mean (ms)   0.000 
PDV-Fwd - max (ms)    4.013          100.000 
PDV-Bck - mean (ms)   0.000 
PDV-Bck - max (ms)    0.252          100.000 
IPDV-Fwd - mean (ms)  0.087 
IPDV-Fwd - max (ms)   4.013 
IPDV-Bck - mean (ms)  0.044 
IPDV-Bck - max (ms)   0.252 
----------------      --------       -------- 
Result                Passed 
 
 
 
 
Performance Phase 
----------------------------------------------------------------------------- 
Duration (min)       : 5 
Configuration Result : Passed 
 
Parameter             IP Size #1 IP Size #2 IP Size #3 IP Size #4 Thr 
                      64 bytes   0 bytes    0 bytes    0 bytes 
----------------      --------   --------   --------   --------   -------- 
Duration (min)        5 
Tx Rate (L3) (Mbps)   76.420 
IR (L3) - mean (Mbps) 76.420 
Tx Rate (L2) (Mbps)   100.301 
IR (L2) - mean (Mbps) 100.301 
PL - count            0 
PLR                   0          0          0          0          1.000E-3 
UAS - count           0 
Availability (%)      100.00                                      99.90 
PTD-Fwd - min (ms)    0.000 
PTD-Fwd - mean (ms)   0.000                                       200.000 
PTD-Fwd - max (ms)    0.000 
ETX-2i Devices 
8. Monitoring and Diagnostics 
PTD-Fwd - std (ms)    58973.712 
PTD-Bck - min (ms)    0.000 
PTD-Bck - mean (ms)   0.000                                       200.000 
PTD-Bck - max (ms)    0.000 
PTD-Bck - std (ms)    58995.021 
PDV-Fwd - mean (ms)   0.000 
PDV-Fwd - max (ms)    0.020                                       100.000 
PDV-Bck - mean (ms)   0.000 
PDV-Bck - max (ms)    0.002                                       100.000 
IPDV-Fwd - mean (ms)  0.000 
IPDV-Fwd - max (ms)   0.020 
IPDV-Bck - mean (ms)  0.000 
IPDV-Bck - max (ms)   0.002 
PD-Fwd - count        0 
PDR-Fwd               0          0          0          0 
PD-Bck - count        0 
PDR-Bck               0          0          0          0 
PR-Fwd - count        0 
PRR-Fwd               0          0          0          0 
PR-Bck - count        0 
PRR-Bck               0          0          0          0 
----------------      --------   --------   --------   --------   -------- 
Result                Passed 
The following table shows the general parameters at the head of the detailed report.  
Parameter 
Description 
BW (Mbps) 
Rate of test session traffic; three decimal point accuracy 
DM UDP Ports 
L4 source and destination ports of delay measurement stream 
Possible values: 0-65504 
                             N/A – if responder type is unknown 
Note: Displays L4 ports of first session in peer 
DSCP 
Priority value for test session traffic 
Possible values: 0-63 
End Date & Time 
Date and time that last test ended 
Generator Address 
IP address of L3 SAT generator 
IP Sizes 
List of tested IP sizes (IP part of test packets) 
Note: Only numbers are shown, e.g., the value of MTU is displayed and not the string 
‘MTU’. 
LM UDP Ports 
L4 source and destination ports of loss measurement stream 
Possible values: 0-65504 
                             N/A – if responder type is unknown 
Note: Displays L4 ports of first session in peer 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Description 
MTU (bytes)  
Discovered IP MTU of path to responder 
Possible values: 68-2094 
                             N/A – if connectivity or MTU sub-tests failed 
Out-of-fsync Time 
Number of seconds during which without TOD synchronization with responder device 
Note: Displayed only if report-type is clock-sync. 
Overall Result 
Overall result of last test 
Possible values: Not Applicable, Passed, Failed, User Aborted, System Aborted 
Peer Profile Name 
Profile used for peer parameters 
Possible values: Variable length string up to 32 characters 
Report Type 
Indicates metrics included in report 
Possible values: Clock Sync, No Clock Sync 
Responder Address 
IP address of L3 SAT peer 
Responder Type 
Discovered type of responder 
Possible values: Unknown, IP loop, UDP loop, Loop & Timestamp 
Rx Flow 
Name of ingress flow used by generator 
Note: Displayed only for L2 probe 
Scope 
Scope of test 
Possible values: Configuration, Performance, Configuration + Performance 
Session Profile Name 
Profile used for test session parameters 
Possible values: Variable length string up to 32 characters 
Start Date & Time 
Date and time at last peer activation 
Total Duration 
Duration of last test 
Tx Flow 
Name of egress flow used by generator 
Note: Displayed only for L2 probe 
The following table shows the test report parameters. The columns CS and NCS indicate if the parameter 
is presented for report type clock-sync and no-clock-sync, respectively. The forward direction refers to 
generator to responder, and backward direction refers to responder to generator. 
Counter 
Description 
CS 
NCS 
Availability (%) 
Percentage of available time 
 
 
Configuration Result 
Result of Configuration phase; repeated per tested IP size 
Possible values: Not Applicable, Passed, Failed, User Aborted, System 
Aborted 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Counter 
Description 
CS 
NCS 
Duration 
(in Performance Phase 
parameter table) 
Duration, in minutes, of performance test per IP size 
 
 
Duration (min) 
(Under Performance Phase 
heading) 
Duration in minutes of entire Performance phase 
 
 
Duration (sec) 
(Under Configuration Phase 
heading) 
Duration in seconds of Configuration phase 
 
 
IP Size#1 – IP Size #4 
IP size index of report 
Possible values: 64 bytes, 128 bytes, 256 bytes, 512 bytes, 1024 bytes, 
1280 bytes, 1500 bytes, MTU, Custom 
Note: Number of IP sizes varies from 1 to 4, according to number of L3 
SAT Session profile IP size.   
 
 
IP Size (bytes) 
IP size of Configuration phase 
 
 
IPDV–Bck – max (ms) 
Maximum one-way Inter-Packet Delay Variation (IPDV), backward 
(milliseconds) 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp. 
 
 
IPDV–Bck – mean (ms) 
Average one-way Inter-Packet Delay Variation (IPDV), backward 
(milliseconds) 
Calculated according to RFC 3393, from the variations of the delays 
between valid packets. 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp. 
 
 
IPDV–Fwd – max (ms) 
Maximum one-way Inter-Packet Delay Variation (IPDV), forward 
(milliseconds) 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp. 
 
 
IPDV–Fwd – mean (ms) 
Average one-way Inter-Packet Delay Variation (IPDV), forward 
(milliseconds) 
Calculated according to RFC 3393, from the variations of the delays 
between valid packets. 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Counter 
Description 
CS 
NCS 
IR (L2) - mean (Mbps) 
L2 average calculated Information Rate  
Number of received test packets multiplied by test packet Ethernet 
frame length (in bits), divided by the elapsed time (in seconds) 
Note: The test packet Ethernet frame length starts with the first MAC 
address bit and ends with the last FCS bit. 
 
 
IR (L3) - mean (Mbps) 
L3 average calculated Information Rate  
Number of received test packets multiplied by test packet Ethernet 
frame length (in bits), divided by the elapsed time (in seconds) 
Note: The test packet Ethernet frame length starts with the first MAC 
address bit and ends with the last FCS bit. 
 
 
PD-Bck - count 
One-way Packet Duplication (PD), backward.  
Number of duplicated packets in backward direction. A packet is 
considered duplicate (backward) if its generator Tx timestamp 
matches that of a previously received packet, and the responder Tx 
timestamps are different. 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp.  
 
 
PD-Fwd – count 
One-way Packet Duplication (PD), forward. 
Number of duplicated packets in forward direction. A packet is 
considered duplicate (forward) if its generator Tx timestamp matches 
that of a previously received packet, and the responder Tx timestamps 
are different. 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp.  
 
 
PDR-Bck 
Calculated one-way Packet Duplication Ratio (PDR), backward  
PDR (backward) is calculated as PD (backward) divided by the number 
of received valid packets, converted to a percentage. 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp. 
 
× 
PDR-Fwd 
Calculated one-way Packet Duplication Ratio (PDR), forward  
PDR (forward) is calculated as PD (forward) divided by the number of 
received valid packets, converted to a percentage. 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp. 
 
× 
PDV – max (ms) 
Maximum calculated round-trip Packet Delay Variation (milliseconds) 
× 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Counter 
Description 
CS 
NCS 
PDV – mean (ms) 
Average calculated round-trip Packet Delay Variation (milliseconds). 
The round-trip PDV is calculated according to ITU-T Y.1540, by 
subtracting the minimum PTD from the 99.9% percentile of the PTD 
values. 
× 
 
PDV-Bck – max (ms) 
Maximum calculated one-way Packet transfer Delay Variation (PDV) 
(milliseconds), backward 
 
× 
PDV-Bck – mean (ms) 
Average calculated one-way Packet transfer Delay Variation (PDV) 
(milliseconds), backward 
 
× 
PDV-Fwd – max (ms) 
Maximum calculated one-way Packet transfer Delay Variation (PDV) 
(milliseconds), forward 
 
× 
PDV-Fwd – mean (ms) 
Average calculated one-way Packet transfer Delay Variation (PDV) 
(milliseconds), forward 
 
× 
Performance Result 
Result of last performance phase 
Possible values: Not Applicable, Passed, Failed, User Aborted, System 
Aborted 
 
 
PL - count 
Packet loss (PL); Number of lost test packets.  
A test packet is considered lost in the following cases: 
• Test packet was not received back at the generator or was 
received with a round-trip delay of over two seconds. 
• Report type parameter is clock-sync and the responder type is 
loop and timestamp, and test packet was received with a forward 
and/or backward delay over one second. 
 
 
PLR 
Calculated Packet Loss Ratio (PLR) 
Number of lost packets divided by the number of transmitted packets 
 
 
Policing 
Sub-test type index of report 
Possible value: Policing 
Note: Policing table (column) is not displayed if corresponding Peer 
Profile Policing test is disabled. 
 
 
PR-Bck - count 
Number of reordered packets in backward direction. A packet is 
considered reordered (backward) if its responder Tx timestamp is 
smaller than that of a previously received packet in backward 
direction. Duplicated and lost packets are not included in the 
calculation. 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp. 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Counter 
Description 
CS 
NCS 
PR-Fwd - count 
Number of reordered packets in forward direction. A packet is 
considered reordered (forward) if its generator Tx timestamp is 
smaller than that of a previously received packet in forward direction. 
Duplicated and lost packets are not included in the calculation. 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp.  
 
 
PRR-Bck 
Calculated one-way Packets Reordered Ratio (PRR), backward  
PRR (backward) is calculated as PR (backward) divided by the number 
of received valid packets, converted to a percentage. 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp. 
 
× 
PRR-Fwd 
Calculated one-way Packets Reordered Ratio (PRR), forward  
PRR (forward) is calculated as PR (forward) divided by the number of 
received valid packets, converted to a percentage. 
Note: Displayed in report only if Responder Type is Loop & 
Timestamp. 
 
× 
PTD – max (ms) 
Maximum measured round-trip Packet Transfer Delay (milliseconds) 
× 
 
PTD – mean (ms) 
Average calculated round-trip Packet Transfer Delay (milliseconds) 
× 
 
PTD – min (ms) 
Minimum measured round-trip Packet Transfer Delay (PTD) 
(milliseconds)  
The round-trip PTD is calculated from the test packet embedded 
timestamps. A round-trip PTD over two seconds is ignored, as the 
packet is considered lost. 
× 
 
PTD – std (ms) 
Calculated standard deviation of round-trip Packet Transfer Delay 
(milliseconds) 
× 
 
PTD-Bck – max (ms) 
Maximum measured one-way Packet Transfer Delay, backward 
(milliseconds) 
 
× 
PTD-Bck – mean (ms) 
Average calculated one-way Packet Transfer Delay, backward 
(milliseconds) 
 
× 
PTD-Bck – min (ms) 
Minimum measured one-way Packet Transfer Delay (TPTD), backward 
(milliseconds). The backward PTD is calculated from the test packet 
embedded timestamps. A backward PTD over one second is ignored, 
as the packet is considered lost. 
 
× 
PTD-Bck – std (ms) 
Calculated standard deviation of one-way Packet Transfer Delay, 
backward (milliseconds) 
 
× 

## Examples  *(p.1455)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Counter 
Description 
CS 
NCS 
PTD-Fwd – max (ms) 
Maximum measured one-way packet transfer delay (PTD), forward 
(milliseconds) 
 
× 
PTD-Fwd – mean (ms) 
Average calculated one-way packet transfer delay (PTD), forward 
(milliseconds) 
 
× 
PTD-Fwd – min (ms) 
Minimum measured one-way packet transfer delay (PTD), forward 
(milliseconds). The forward PTD is calculated from the test packet 
embedded timestamps. A forward PTD over one second is ignored, as 
the packet is considered lost. 
Note: The one-way PTD measurements are valid only when there is 
TOD synchronization between the generator device and the responder 
device; accurate TOD synchronization is feasible only with a responder 
of type loop and timestamp. 
 
× 
PTD-Fwd – std (ms) 
Calculated standard deviation of one-way Packet Transfer Delay (PTD) 
(milliseconds) 
 
× 
Result 
Result of sub-test 
Possible values: Not Applicable, Passed, Failed, User Aborted, System 
Aborted 
 
 
Step#1 – Step#4 
Sub-test type index of report 
Possible values: Step #1, Step #2, Step #3, Step #4  
Note: Number of bandwidth steps varies from 1 to 4, according to 
number of bw-steps configured in peer profile. 
 
 
Thr 
Service acceptance criteria for reported test session and IP size 
Note:  
• Threshold value is taken from profile corresponding to reported 
test session. 
• If test session configuration changes, “—“ is displayed. 
 
 
Tx Rate (L2) (Mbps) 
L2 transmission rate (Mbps), configured in sub-test generator 
 
 
Tx Rate (L3) (Mbps) 
L3 transmission rate (Mbps), configured in sub-test generator 
 
 
UAS count 
Number of unavailable seconds 
 
 
 
Examples 
Note 
Before configuring the Generator and Responder in the following examples, 
connect the respective devices with an ETH cable via their NET 1 ports. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Layer-2 Probe Mode 
This example illustrates configuring L3 SAT in layer-2 probe mode: 
• 
Generator with IP address = 20.20.20.101 
• 
Responder with IP address = 20.20.20.20 
 To configure the responder: 
• 
Router: Associate Interface 2 with SVI 2 (type TWAMP). 
• 
Flows between Ethernet ports 0/1 and 0/3, classified to VLAN 100 
exit all 
#*********Configure SVI type TWAMP  
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
      ingress-port ethernet 0/1 
      egress-port ethernet 0/3 queue 0 block 0/1 
      no shutdown 
      exit  
 
    flow E3toE1 
      classifier v100 
      ingress-port ethernet 0/3 
      egress-port ethernet 0/1 queue 0 block 0/1 
      no shutdown 
      exit 
    exit 
 
#*********Configure router 1 with interface 2 for L3 SAT 
  router 1 
    interface 2 
      address 20.20.20.20/24 
      bind svi 2 
      no shutdown 
      exit  
    exit  
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#*********Configure L3 SAT responder  
  test  
    l3sat  
      responder res1 l2-probe 
        bind ethernet 0/1 
        local-ip-address 20.20.20.20 
        router-entity 1 
        vlan-tag vlan 100 pbit fixed 3 
        no shutdown 
      exit all 
save 
 To configure the generator: 
• 
Router: Associate Interface 2 with SVI 2 (type TWAMP). 
• 
Flows between Ethernet ports 0/1 and 0/3, classified to VLAN 100 
• 
Test sessions: 
 
Session1: 
 
Packet sizes 128, 512, and 750 
 
Bandwidth 10000 
 
DSCP 11 
 
Session2: 
 
Default packet size (256) 
 
Bandwidth 5000 
 
DSCP 12 
 
exit all 
#*********Configure SVI type TWAMP  
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
ETX-2i Devices 
8. Monitoring and Diagnostics 
      no shutdown 
      exit  
 
    flow E3toE1 
      classifier v100 
      ingress-port ethernet 0/3 
      egress-port ethernet 0/1 queue 0 block 0/1 
      no shutdown 
      exit 
    exit 
 
#*********Configure router 1 with interface 2 for L3 SAT  
  router 1 
    interface 2 
      address 20.20.20.101/24 
      bind svi 2 
      no shutdown 
      exit 
    exit 
 
#*********Configure L3 SAT peer profile 
  test  
    l3sat  
      peer-profile peer1 
        performance-duration custom 5 
        exit  
 
#*********Configure L3 SAT session profiles 
      session-profile session1 
        ip-size 128 512 custom 750 
        exit  
      session-profile session2 
        exit  
#*********Configure L3 SAT generator 
      generator gen1 l2-probe 
        bind ethernet 0/1 
        local-ip-address 20.20.20.101 
        router-entity 1 
        vlan-tag vlan 100 pbit fixed 3 
        no shutdown 
        peer 20.20.20.20 
          peer-profile peer1 
          test-session test1 session-profile session1 bw 10000 dscp 11 
          test-session test2 session-profile session2 bw 5000 dscp 12 
          activate 
          exit 
        exit all 
save 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Layer-3 
This example illustrates configuring L3 SAT in Layer-3 mode: 
• 
Generator with IP address = 20.20.20.101 
• 
Responder with IP address = 20.20.20.20 
 To configure the responder: 
• 
Router: Associate Interface 2 with SVI 2. 
• 
Flows between Ethernet port 0/3 and SVI 2: 
 
Ethernet port 0/3 to SVI 2: Traffic tagged with VLAN 12, VLAN popped 
 
SVI 2 to Ethernet port 0/3: All traffic, VLAN 12 pushed 
exit all 
#*********Configure SVI for L3 SAT  
configure  
  port  
    svi 2  
      no shutdown 
    exit 
  exit 
 
#********* Configure classifiers for VLAN 12 & all traffic  
  flows 
    classifier-profile v12 match-any  
      match vlan 12 
    exit 
    classifier-profile all match-any  
      match all 
    exit 
#********* Configure flows between Eth port 0/3 & SVI 2 
    flow E3toSVI2 
      ingress-port ethernet 0/3 
      egress-port svi 2 queue 0 
      classifier v12 
      vlan-tag pop vlan 
      no shutdown 
      exit 
 
    flow SVI2toE3 
      ingress-port svi 2 
      egress-port ethernet 0/3 queue 0 block 0/1 
      classifier all 
      vlan-tag push vlan 12 p-bit fixed 0 
      no shutdown 
      exit 
    exit 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#*********Configure router with interface 2 for L3 SAT 
  router 1 
    interface 2 
      address 20.20.20.20/24 
      bind svi 2 
      no shutdown 
      exit  
    exit 
 
#*********Configure L3 SAT responder 
  test 
    l3sat 
      responder res1 
        local-ip-address 20.20.20.20 
        router-entity 1 
         no shutdown 
      exit all 
save 
 To configure the generator: 
• 
Router: Associate Interface 2 with SVI 2. 
• 
Flows between Ethernet port 0/3 and SVI 2: 
 
Ethernet port 0/3 to SVI 2: Traffic tagged with VLAN 12, VLAN popped 
 
SVI 2 to Ethernet port 0/3: All traffic, VLAN 12 pushed 
• 
Test sessions: 
 
Session1: 
 
Packet sizes 512, 700 
 
Bandwidth 10000 
 
DSCP 11 
 
Session2: 
 
Default packet size (256) 
 
Bandwidth 5000 
 
DSCP 12 
 
exit all 
#*********Configure SVI for L3 SAT  
configure  
  port  
    svi 2 twamp 
      no shutdown 
    exit 
  exit 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
#********* Configure classifiers for VLAN 12 & all traffic  
  flows 
    classifier-profile v12 match-any  
      match vlan 12 
    exit 
    classifier-profile all match-any  
      match all 
    exit 
 
#********* Configure flows between Eth port 0/3 & SVI 2 
    flow E3toSVI2 
      ingress-port ethernet 0/3 
      egress-port svi 2 queue 0 
      classifier v12 
      vlan-tag pop vlan 
      no shutdown 
      exit 
 
    flow SVI2toE3 
      ingress-port svi 2 
      egress-port ethernet 0/3 queue 0 block 0/1 
      classifier all 
      vlan-tag push vlan 12 p-bit fixed 0 
      no shutdown 
      exit 
    exit 
 
#*********Configure router with interface 2 for L3 SAT 
  router 1 
    interface 2 
      address 20.20.20.101/24 
      bind svi 2 
      no shutdown 
      exit 
    exit 
 
#*********Configure L3 SAT peer profile 
  test  
    l3sat 
      peer-profile peer1 
        performance-duration custom 5 
        exit  
#*********Configure L3 SAT session profiles 
      session-profile session1 
        ip-size 512 custom 700 
        exit  
      session-profile session2 
        exit  
 
 
 