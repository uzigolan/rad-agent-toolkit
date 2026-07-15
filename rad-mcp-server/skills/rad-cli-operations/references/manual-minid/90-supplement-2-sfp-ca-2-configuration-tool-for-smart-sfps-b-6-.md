# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – B.6 Testing OAM (CFM)

*Manual `MiNID_ver_2_6_mn.pdf`, pages 386–386.*


## Estimated Duration  *(p.386)*

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