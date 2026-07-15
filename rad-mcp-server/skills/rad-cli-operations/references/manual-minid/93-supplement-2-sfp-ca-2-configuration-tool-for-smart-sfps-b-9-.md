# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – B.9 Testing RFC-2544

*Manual `MiNID_ver_2_6_mn.pdf`, pages 392–393.*


## Estimated Duration  *(p.392)*


## Setup and Configuration  *(p.392)*


## Test Procedure  *(p.392)*

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