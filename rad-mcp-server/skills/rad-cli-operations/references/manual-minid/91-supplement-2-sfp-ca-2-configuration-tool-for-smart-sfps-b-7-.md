# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – B.7 Testing OAM (EFM)

*Manual `MiNID_ver_2_6_mn.pdf`, pages 387–388.*


## Setup and Configuration  *(p.387)*


## Test Procedure  *(p.387)*


## Estimated Duration  *(p.387)*

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

## Setup and Configuration  *(p.388)*


## Test Procedure  *(p.388)*

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
 