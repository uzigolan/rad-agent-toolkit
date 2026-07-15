# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – B.5 Testing Flows

*Manual `MiNID_ver_2_6_mn.pdf`, pages 383–385.*


## Estimated Duration  *(p.383)*


## Setup and Configuration  *(p.383)*


## Test Procedure  *(p.383)*

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
 