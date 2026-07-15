# B Test Plan

*Manual `MiNID_ver_2_6_mn.pdf`, pages 378–396.*


## B.1 Introduction  *(p.378)*


## B.2 Required Equipment  *(p.378)*

Test Plan 
B.1 Introduction 
This document describes basic tests to verify MiNID functionality for the following features: 
• 
Basic functionality (connectivity, passing traffic without errors) 
• 
Flows 
• 
OAM (CFM) 
• 
OAM (EFM) 
• 
Service Loopbacks 
• 
RFC-2544 
• 
Sync-E 
• 
Device reset 
 
Note 
All tests should pass if the following procedures are performed precisely. 
B.2 Required Equipment 
The table below lists devices required for conducting the tests. 
Device 
Description 
Quantity 
Unit under test (UUT)  
MiNID 
4 
Local and remote ETX 
Hosting device for MiNID: 
ETX-203AX or ETX-205A (must be 
ETX-205A with Sync-E option if you 
wish to perform Sync-E tests) 
2 

## B.3 Preparing the Test Layout  *(p.379)*

B. Test Plan 
Device 
Description 
Quantity 
Local and remote IPmux 
Necessary for Sync-E tests 
2 
Network management station 
PC or Unix workstation equipped 
with RADview  
2 
Network Tester 
Network testing equipment with 
Ethernet interfaces such as 
IXIA 400T, Spirent Test Center, etc. 
2 
B.3 Preparing the Test Layout 
The following diagram illustrates the test plan setup. 
 
Local ETX
1
2
3
4
5
6
MiNID 1
Classifier VLAN+Pbit
MiNID 2
Classifier DSCP
MiNID 3
Classifier Source MAC
MiNID 4
Classifier Port
Network
Tester
Remote ETX
1
2
3
4
5
6
EFM 
Active
EFM 
Active
EFM 
Passive
EFM 
Passive
Network
Tester
EXT
CLK
EXT
CLK
Local 
IPmux
Remote 
IPmux
 
B. Test Plan 
Connecting the Test Layout 
The following tables list the connections between the devices, and the cable required for each 
connection. 
Test Layout Connections 
Device 
Cable 
Device 
Local ETX port 1 
Straight Ethernet cable 
Local Network Tester  
Local ETX port 2 
Not applicable; MiNID is inserted 
UUT-1 
Local ETX port 3 
Not applicable; MiNID is inserted 
UUT-2 
Local ETX port 4 
Not applicable; MiNID is inserted 
UUT-3 
Local ETX port 5 
Not applicable; MiNID is inserted 
UUT-4 
Local ETX EXT CLK port 
Straight Ethernet cable 
Local IPmux EXT CLK port 
Local IPmux EXT CLK port 
Straight Ethernet cable 
Local ETX EXT CLK port 
UUT-1 
Straight Ethernet cable 
Remote ETX port 2 
UUT-2 
Straight Ethernet cable 
Remote ETX port 3 
UUT-3 
Straight Ethernet cable 
Remote ETX port 4 
UUT-4 
Straight Ethernet cable 
Remote ETX port 5 
Remote ETX port 1 
Straight Ethernet cable 
Remote Network Tester  
Remote ETX port 2 
Straight Ethernet cable 
UUT-1 
Remote ETX port 3 
Straight Ethernet cable 
UUT-2 
Remote ETX port 4 
Straight Ethernet cable 
UUT-3 
Remote ETX port 5 
Straight Ethernet cable 
UUT-4 
Remote ETX EXT CLK port 
Straight Ethernet cable 
Remote IPmux EXT CLK port 
Remote IPmux EXT CLK port 
Straight Ethernet cable 
Remote ETX EXT CLK port 
Local Network Tester 
Straight Ethernet cable 
Local ETX port 1 
Remote Network Tester 
Straight Ethernet cable 
Remote ETX port 1 
 
B. Test Plan 
Configuring Devices 
This section presents the device configurations. The data, such as VLAN IDs and IP addresses, were 
randomly selected for test purposes, and can be changed to suit your particular configuration. 
The following table presents the configuration files for the MiNID and ETX devices. You can open or save 
the configuration files as follows: 
• 
To open the file – Double-click the icon
in the table below.  
• 
To save the file – Right-click the icon 
 in the table below and select Save Embedded File to 
Disk. 
Device 
File 
UUT-1 
 
UUT-2 
 
UUT-3 
 
UUT-4 
 
Local ETX 
 
Remote ETX 
 
The following table presents the IPmux device configurations. 
Parameter 
Local 
Remote 
Host IP 
192.168.205.32 
192.168.205.33 
E1 configuration 
Unframed 
Unframed 
Peer IP 
10.10.10.10 
10.10.10.11 
PW IP 
10.10.10.11 
10.10.10.10 
Payload size 
4 
4 
OAM 
Disable 
Disable 
 

## B.4 Testing Basic Functionality  *(p.382)*

B. Test Plan 
B.4 Testing Basic Functionality 
This test verifies that the test setup functions properly. 
Estimated Duration 
The estimated duration of this test is one hour. 
Setup and Configuration 
See Connecting the Test Layout and Configuring Devices. 
Test Procedure 
# 
Action 
Expected Result 
Result 
1 
Ping the UUTs to verify network 
connectivity 
The UUTs reply to ping 
 
2 
Open Telnet sessions to the UUTs 
Telnet and SSH sessions are established 
successfully 
 
3 
Initiate SNMP management 
session from RADview NMS and 
verify management connectivity to 
all devices 
Devices reply to ping and appear on 
RADview map 
 
4 
Display UUT inventory  
The inventory display is correct: 
Name:            MiNID-chassis 
Description:    RAD.MiNID.chassis 
HW Rev:          xxx[FE/GE] 
FW Rev:           yyy 
SW Rev:           zzz 
SW Date\Time: date of SW  
 

## B.5 Testing Flows  *(p.383)*

B. Test Plan 
# 
Action 
Expected Result 
Result 
5 
Run Ethernet traffic for at least 
15 minutes: From Network Tester 
port 1 and port 2, send packets 
with frame size 1518 bytes, VLAN 
4040, P-bit 5, DSCP 16, at 98% line 
rate 
The traffic passes without errors or 
packet loss 
 
6 
Verify status of all MEPs 
Verify that all MEPs are OK, e.g.: 
• Operational status is OK 
• No defects are displayed 
Remote MEP address matches the 
remote device MAC address. 
 
7 
Clear alarm logs in all devices 
Logs are empty with no active alarms 
 
 
B.5 Testing Flows 
This test verifies flow functionality. 
Estimated Duration 
The estimated duration of this test is one hour. 
Setup and Configuration 
See Connecting the Test Layout and Configuring Devices. 
Test Procedure 
# 
Action 
Expected Result 
Result 
1 
In the remote ETX, administratively 
disable flows d6 and d61 
Flows d6 and d1 are not active 
 
B. Test Plan 
# 
Action 
Expected Result 
Result 
2 
In UUT-1, verify classification Vlan range 
+ Pbit range: 
Send traffic between Network Tester 
ports 1 and 2 with VLAN range 40–45 
and p-bit 4, using a stream with line 
rate=100 pps, length=100 bytes, burst 
size=100 packets, number of bursts=1 
(stream #13 if using IXIA with the 
stream file from Configuring Devices) 
Capture frames received in 
Network Tester port 2, and 
verify: 
• The traffic passes without 
errors or packet loss 
• In UUT-1, flow statistics 
display the same amount of 
frames sent by the 
Network Tester 
 
3 
In UUT2-, verify classification DSCP: 
Send traffic between Network Tester 
ports 1 and 2 with VLAN range 100–
4094 and DSCP 16, using a stream with 
line rate=100 pps ,length=100 bytes 
,burst size=100 packets, number of 
bursts=1 (stream #5 if using IXIA with 
the stream file from Configuring 
Devices) 
Capture frames received in 
Network Tester port 2, and 
verify: 
• The traffic passes without 
errors or packet loss 
• In UUT-2, flow statistics 
display the same amount of 
frames sent by the 
Network Tester 
 
4 
In UUT-3, verify classification source 
MAC: 
Send traffic between Network Tester 
ports 1 and 2 with VLAN range 100–
4094 and source MAC 
00-00-00-00-00-BB, using a stream with 
line rate=100 pps, length=100 bytes, 
burst size=100 packets, number of 
bursts=1 (stream #19 if using IXIA with 
the stream file from Configuring 
Devices) 
Capture frames received in 
Network Tester port 2, and 
verify: 
• The traffic passes without 
errors or packet loss 
• In UUT-3, flow statistics 
display the same amount of 
frames sent by the 
Network Tester 
 
5 
Verify pass-through action: 
Send traffic between Network Tester 
port 1 and Network Tester port 2 with 
VLAN range 101–4094 and DSCP 16, 
using a stream with line rate=100 pps, 
length=100 bytes, burst 
size=100 packets, number of bursts=1 
(stream #5 if using IXIA with the stream 
file from Configuring Devices) 
Capture frames received in 
Network Tester port 2, and 
verify: 
• The traffic passes without 
errors or packet loss 
• Port statistics display the 
same amount of frames sent 
by the Network Tester 
 
B. Test Plan 
# 
Action 
Expected Result 
Result 
6 
Verify push VLAN action (fixed p-bit):  
Send traffic between Network Tester 
port 1 and Network Tester port 2 with 
VLAN range 101–4094 and DSCP 8, 
using a stream with line rate=100 pps, 
length=100 bytes, burst 
size=100 packets, number of bursts=1, 
source MAC=00-00-00-00-00-02 
(stream #2 if using IXIA with the stream 
file from Configuring Devices) 
Capture frames received in 
Network Tester port 2, and 
verify: 
• The traffic passes without 
errors or packet loss 
• Flow statistics display the 
same amount of frames sent 
by the Network Tester 
• All frames with source MAC 
address 00-00-00-00-00-02 
are received with VLAN 555 
and p-bit 5, and Canonical 
Format Identifier (CFI) field 
changed to 1 
 
7 
Verify push VLAN action (p-bit according 
to DSCP mapping): 
Send traffic from Network Tester port 1 
to Network Tester port 2 with VLAN 
range 101–4094 and DSCP 32, using a 
stream with line rate=100 pps, 
length=100 bytes, burst 
size=100 packets, number of bursts=1, 
source MAC=00-00-00-00-00-08 
(stream #8 if using IXIA with the stream 
file from Configuring Devices) 
Capture frames received in 
Network Tester port 2, and 
verify: 
• The traffic passes without 
errors or packet loss 
• Flow statistics display the 
same amount of frames sent 
by the Network Tester 
• All frames with source MAC 
address 00-00-00-00-00-08 
are received with VLAN 888 
and p-bit equal to DSCP 
mapping (5) 
 
8 
Verify pop VLAN action: 
Send traffic from Network Tester port 1 
to Network Tester port 2 with VLAN 
range 101–4094 and DSCP 12, using a 
stream with line rate=100 pps, 
length=100 bytes, burst 
size=100 packets, number of bursts=1, 
source MAC=00-00-00-00-00-03 
(stream #3 if using IXIA with the stream 
file from Configuring Devices) 
Capture frames received in 
Network Tester port 2, and 
verify: 
• The traffic passes without 
errors or packet loss 
• Flow statistics display the 
same amount of frames sent 
by the Network Tester 
• All frames with source MAC 
address 00-00-00-00-00-03 
are received without a VLAN 
 

## B.6 Testing OAM (CFM)  *(p.386)*

B. Test Plan 
# 
Action 
Expected Result 
Result 
9 
Verify loop with MAC swap action: 
Send traffic between Network Tester 
port 1 and Network Tester port 2 with 
VLAN range 101–4094, DSCP 20, source 
MAC address 00-00-00-00-00-04, and 
destination MAC address 
00-00-00-00-00-10; using a stream with 
line rate=100 pps, length=100 bytes, 
burst size=100 packets, number of 
bursts=1 (stream #4 if using IXIA with 
the stream file from Configuring 
Devices) 
Capture frames received in 
Network Tester port 2, and 
verify: 
• The traffic passes without 
errors or packet loss 
• Flow statistics display the 
same amount of frames sent 
by the Network Tester 
• All frames with source MAC 
address 00-00-00-00-00-10 
and destination MAC 
address 00-00-00-00-00-04 
are received by the port 
from which they were sent  
 
10 
In the remote ETX, administratively 
enable flows d6 and d61 
Flows d6 and d1 are active 
 
11 
In UUT-4, verify classification Port 
Mode: 
Send traffic between Network Tester 
ports 1 and 2  with VLAN range 100–
4094, using a stream with line 
rate=100 pps, length=100 bytes ,burst 
size=100 packets, number of bursts=1, 
source=aa-aa-aa-aa-aa-aa, 
des=bb-bb-bb-bb-bb-bb (stream #27 if 
using IXIA with the stream file from 
Configuring Devices) 
Capture frames received in 
Network Tester port 2, and 
verify: 
• The traffic passes without 
errors or packet loss 
• In UUT-4, port statistics 
display the same amount of 
frames sent by the 
Network Tester 
 
 
B.6 Testing OAM (CFM) 
This test verifies the functionality of the MEPs. 
Estimated Duration 
The estimated duration of this test is one hour. 

## B.7 Testing OAM (EFM)  *(p.387)*

B. Test Plan 
Setup and Configuration 
See Connecting the Test Layout and Configuring Devices. 
Test Procedure 
# 
Action 
Expected Result 
Result 
1 
In the remote ETX, administratively 
disable flows d6 and d61 
Flows d6 and d1 are not active 
 
2 
To verify MEP Status when remote 
MEP is down: In the remote ETX, 
set MEP 2 to administratively 
disabled (via command shutdown) 
In UUT-1, display MEP 1 status and 
verify that operational status has 
changed to fail, and there is indication 
of loss of continuity 
 
3 
To verify MEP Status when remote 
MEP returns to up: In the remote 
ETX, set MEP 2 to administratively 
enabled (via command 
no shutdown) 
In UUT-1, display MEP 1 status and 
verify that operational status has 
returned to OK 
 
4 
Run OAM link trace between the 
various pairs of MEPs and their 
corresponding remote MEPs 
Link trace is successful 
 
5 
Run OAM loopback between the 
various pairs of MEPs and their 
corresponding remote MEPs 
Loopback is successful 
 
6 
In the remote ETX, administratively 
enable flows d6 and d61 
Flows d6 and d1 are active 
 
 
B.7 Testing OAM (EFM) 
This test verifies the functionality of link OAM. 
Estimated Duration 
The estimated duration of this test is one hour. 
B. Test Plan 
Setup and Configuration 
See Connecting the Test Layout and Configuring Devices. 
Test Procedure 
# 
Action 
Expected Result 
Result 
1 
In the remote ETX, verify that flows 
d6 and d61 are administratively 
enabled 
Flows d6 and d1 are active 
 
2 
Verify OAM (EFM) discovery between: 
• UUT-3 (active) to remote ETX 
port 4 (passive) 
• UUT-4 (passive) to remote ETX 
port 5 (active)  
Verify OAM (EFM) status: 
In UUT-3: 
• Operational status is up 
• Local MAC address matches 
UUT3 MAC address 
• Remote MAC address matches 
remote ETX port 4 MAC address 
• UUT-3 Local is Active and ETX 
port 4 Remote is Passive 
In UUT-4: 
• Operational status is up 
• Local MAC address matches 
UUT-4 MAC address 
• Remote MAC address matches 
remote ETX port 5 MAC address 
• UUT-4 Local is Active and ETX 
port 5 Remote is Passive 
 

## B.8 Testing Service Loopbacks  *(p.389)*

B. Test Plan 
# 
Action 
Expected Result 
Result 
3 
In remote ETX port 5, activate OAM 
EFM loopback: 
• Run the loopback for 5 minutes 
Send traffic from Network Tester 
port 1 that matches the flow 
classification in UUT-3 and UUT-4, 
using one stream with MAC address 
00-00-00-00-00-AA and one stream 
with MAC address 
AA-AA-AA-AA-AA-AA 
(stream #19 & 27 if using IXIA with 
the stream file from Configuring 
Devices) 
Capture frames received in 
Network Tester port 1, and verify: 
• The traffic passes without errors 
or packet loss 
• In UUT-3 and UUT-4, flow 
statistics display the same 
amount of frames sent by the 
Network Tester 
• All frames with both source 
MAC addresses are received in 
Network Tester 
 
4 
In remote ETX port 5, deactivate OAM 
EFM loopback: 
• Run data for 5 minutes 
Send traffic from Network Tester 
port 1 that matches the flow 
classification in UUT-3 and UUT-4, 
using one stream with MAC address 
00-00-00-00-00-AA and one stream 
with MAC address 
AA-AA-AA-AA-AA-AA 
(stream #19 & 27 if using IXIA with 
the stream file from Configuring 
Devices) 
Capture frames received in 
Network Tester port 1, and verify: 
• The traffic passes without errors 
or packet loss 
• In UUT-3 and UUT-4, flow 
statistics display the same 
amount of frames sent by the 
Network Tester 
• All frames with both source 
MAC addresses are received in 
Network Tester 
 
B.8 Testing Service Loopbacks 
This test verifies the functionality of service loopbacks. 
Estimated Duration 
The estimated duration of this test is one hour. 
B. Test Plan 
Setup and Configuration 
See Connecting the Test Layout and Configuring Devices. 
Test Procedure 
 
# 
Action 
Expected Result 
Result 
1 
In the remote ETX, administratively 
disable flows d6 and d61 
Flows d6 and d1 are not active 
 
2 
Test Layer-2 loopback: Send traffic 
from Network Tester port 1 to 
Network Tester port 2 with VLAN 
range 101–4094 and DSCP 16, using 
streams with line rate=100 pps, 
length=100 bytes, burst 
size=100 packets, number of 
bursts=1, source 
MAC=00-00-AA-AA-AA-AA to 
source MAC 00-00-DD-DD-DD-DD 
(stream #28–31 if using IXIA with 
the stream file from Configuring 
Devices)  
Capture frames returned to 
Network Tester port 1, and verify: 
• The traffic passes without errors or 
packet loss 
• MAC address and IP address are 
swapped 
• Port statistics display the same 
amount of frames sent by the 
Network Tester 
 
 
3 
Test Layer-2 loopback: Send traffic 
from Network Tester port 1 to 
Network Tester port 2 with VLAN 
range 101–4094 and DSCP 16, using 
streams with line rate=100 pps, 
length=100 bytes, burst 
size=100 packets, number of 
bursts=1, source 
MAC=00-00-AA-AA-AA-AA to 
source MAC 00-00-DD-DD-DD-DD 
(stream #32–35 if using IXIA with 
the stream file from Configuring 
Devices) 
Verify that frames are not returned to 
Network Tester port 1 
 
4 
In the remote ETX, administratively 
enable flows d6 and d61 
Flows d6 and d1 are active 
 
B. Test Plan 
# 
Action 
Expected Result 
Result 
5 
Test Layer-3/4 loopback by IP and 
UDP: Send traffic from 
Network Tester port 1 to 
Network Tester port 2 with VLAN 
range 101–4094 and DSCP 34, using 
streams with line rate=100 pps, 
length=100 bytes, burst 
size=100 packets, number of 
bursts=1, source 
MAC=00-00-AA-AA-AA-AA to 
source MAC 00-00-DD-DD-DD-DD, 
dest IP 192.0.0.1, dest UDP 5000 
Capture frames returned to 
Network Tester port 1, and verify: 
• The traffic passes without errors or 
packet loss 
• MAC address and IP address are 
swapped 
• Port statistics display the same 
amount of frames sent by the 
Network Tester 
 
 
6 
Test Layer-3/4 loopback by IP and 
UDP: Send traffic from 
Network Tester port 1 to 
Network Tester port 2 with VLAN 
range 0–4094 and DSCP 34, using 
streams with line rate=100 pps, 
length=100 bytes, burst 
size=100 packets, number of 
bursts=1, source MAC=00-00-00-
00-00-0A to source MAC 00-00-00-
00-00-0D, dest IP 192.0.0.1, 
dest UDP 1024 
Verify that frames are not returned to 
Network Tester port 1 
 
7 
Test Layer-3/4 loopback by IP: Send 
traffic from Network Tester port 1 
to Network Tester port 2 with VLAN 
range 101–4094 and DSCP 34, using 
streams with line rate=100 pps, 
length=100 bytes, burst 
size=100 packets, number of 
bursts=1, source MAC=00-00-AA-
AA-AA-AA to source mac 00-00-DD-
DD-DD-DD, dest IP 192.0.0.1, 
dest UDP 1024 
Capture frames returned to 
Network Tester port 1, and verify: 
• The traffic passes without errors or 
packet loss 
• MAC address and IP address are 
swapped 
• Port statistics display the same 
amount of frames sent by the 
Network Tester 
 
 

## B.9 Testing RFC-2544  *(p.392)*

B. Test Plan 
# 
Action 
Expected Result 
Result 
8 
Test Layer-3/4 loopback by IP: Send 
traffic from Network Tester port 1 
to Network Tester port 2 with VLAN 
range 0–4094 and DSCP 34, using 
streams with line rate=100 pps, 
length=100 bytes, burst 
size=100 packets, number of 
bursts=1, source MAC=00-00-00-
00-00-0A to source mac 00-00-00-
00-00-0D, dest IP 192.0.0.2, 
dest UDP 1024 
Verify that frames are not returned to 
Network Tester port 1 
 
 
B.9 Testing RFC-2544 
This test verifies the functionality of the RFC-2544 benchmark testing.  
Estimated Duration 
The estimated duration of this test is one hour. 
Setup and Configuration 
See Connecting the Test Layout and Configuring Devices. 
Test Procedure 
# 
Action 
Expected Result 
Result 
1 
In the remote ETX, administratively 
disable flows d6 and d61 
Flows d6 and d1 are not active 
 
B. Test Plan 
# 
Action 
Expected Result 
Result 
2 
Test throughput for 64-byte frame size: 
In the remote ETX, run the RFC-2544 
throughput test that uses profile 1 (via 
command config test rfc2544 test 1 
activate) 
The test starts 
 
3 
Check the test status (via command 
show status) 
The command output shows 
that the test is in progress; after 
about four minutes, the 
command output shows that 
the test has completed 
 
4 
Display the test results (via command 
show summary) 
Verify that measured results 
match the expected results: 
Test result is successful 
Throughput (FPS) column 
displays a value such that the 
result of [FPS × Frame Size × 8] is 
the following according to frame 
size: 
• 64 – 76% 
• 512 – 96% 
• 1518 – 98% 
 
 
 
# 
Action 
Expected Result 
1 
In the remote ETX, administratively disable flows 
d6 and d61 
Flows d6 and d1 are not active 
2 
Test throughput for 64-byte frame size: In the 
remote ETX, run the RFC-2544 throughput test 
that uses profile 1 (via command config test 
rfc2544 test 1 activate) 
The test starts 
3 
Check the test status (via command show 
status) 
The command output shows that the test is in progress; after about 
four minutes, the command output shows that the test has completed 

## B.10 Testing Sync-E  *(p.394)*

B. Test Plan 
# 
Action 
Expected Result 
4 
Display the test results (via command show 
summary) 
Verify that measured results match the expected results: 
• Test result is successful 
• Throughput (FPS) column displays a value such that the result of 
[FPS × Frame Size × 8] is the following according to frame size: 
 
64 – 76% 
 
512 – 96% 
 
1518 – 98% 
5 
In the remote ETX, administratively enable flows 
d6 and d61 
Flows d6 and d1 are active 
 
B.10 Testing Sync-E 
This test verifies the functionality of the Sync-E benchmark testing.  
Estimated Duration 
The estimated duration of this test is one hour. 
Setup and Configuration 
See Connecting the Test Layout and Configuring Devices. 
Test Procedure 
# 
Action 
Expected Result 
Result 
 
 
 
 
 
 
 
 
 

## B.11 Testing Device Reset  *(p.395)*

B. Test Plan 
 
# 
Action 
Expected Result 
Result 
1 
Set local ETX as master clock  
 
 
2 
Set remote ETX as slave clock with 
clock source Ethernet port 2 
Verify the local and remote ETX are locked 
 
3 
Set local IPmux to internal clock 
 
 
4 
Set remote IPmux to loopback clock 
 
 
5 
In UUT1, set the Sync-E clock source 
to the MSA port  
After five minutes, verify that the connection statistics 
in the remote IPmux do not indicate errors  
 
6 
Set local ETX as slave clock with 
clock source Ethernet port 2  
 
 
7 
Set remote ETX as master clock 
Verify the local and remote ETX are locked 
 
8 
Set local IPmux to loopback clock 
 
 
9 
Set remote IPmux to internal clock 
 
 
10 
In UUT1, set the Sync-E clock source 
to the SFP port  
After five minutes, verify that the connection statistics 
in the local IPmux do not indicate errors 
 
 
B.11 Testing Device Reset 
This test verifies the correct execution of device reboot, and verifies that all configured entities operate 
properly after the reboot. 
Estimated Duration 
The estimated duration of this test is one hour. 
Setup and Configuration 
See Connecting the Test Layout and Configuring Devices. 
B. Test Plan
Test Procedure 
# 
Action 
Expected Result 
Result 
1 
Save the UUT configuration 
File is saved successfully 
2 
Upload configuration file 
File is uploaded 
successfully 
3 
Verify that traffic is running 
through all relevant ports 
Traffic is running without 
errors or packet loss  
4 
Reboot UUT 
•
UUT retains its
configuration after
the reboot
•
The device responds
to pings
•
Management access
(Telnet/SSH)has been
restored
Traffic is running 
error-free. 
5 
Upload the device configuration 
file, and compare it to the 
configuration file uploaded 
before the reboot 
The uploaded 
configuration files before 
and after the reboot are 
the same 