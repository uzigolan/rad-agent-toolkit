# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – B.8 Testing Service Loopbacks

*Manual `MiNID_ver_2_6_mn.pdf`, pages 389–391.*


## Estimated Duration  *(p.389)*

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

## Setup and Configuration  *(p.390)*


## Test Procedure  *(p.390)*

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
 
 