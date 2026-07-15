# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – B.4 Testing Basic Functionality

*Manual `MiNID_ver_2_6_mn.pdf`, pages 382–382.*


## Estimated Duration  *(p.382)*


## Setup and Configuration  *(p.382)*


## Test Procedure  *(p.382)*

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
 