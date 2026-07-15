# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.2 Microburst Monitoring

*Manual `MiNID_ver_2_6_mn.pdf`, pages 253–255.*


## (chapter introduction)  *(p.253)*

11. Monitoring and Diagnostics 
Counter 
Description 
Round-trip delay variation (PDV) – 
max 
Maximum round-trip PDV 
 
 To view a summary report in the web interface: 
1. Navigate to generator profile (Configuration > Test > L3SAT > Generator) and click the generator 
name in the table. 
The generator profile configuration screen opens. 
2. In the peer row, click summary report.  
 
 To view a summary report in the CLI:  
MiNID-Generator>config>test>l3sat>generator(1)>peer(11.11.11.3)# show summary-report 
End Points 
Generator Address    : 11.11.11.1 
Responder Address    : 11.11.11.3 
Short Packet Mode    : Enable 
Responder Type       : IP Loop 
Test Rate Mode       : L1 
 
Test 
Scope                : Performance 
Peer Profile Name    : peer_profile 
Start Date & Time    : 00:39:50 01-01-1970 
End Date & Time      : 00:40:53 01-01-1970 
Total Duration       : 1:03 
Overall Result       : Pass 
 
Test Name                BW        DSCP      Performance Result 
                         [Kbps] 
----------------------------------------------------------------- 
MiNID_SA                 4         0         Pass 
 
MiNID-Generator>config>test>l3sat>generator(1)>peer(11.11.11.3)# 
11.2 Microburst Monitoring 
Granular bandwidth utilization and Microburst monitoring is a  Platinum feature available with the 
Platinum installation package. This feature enables you to monitor network traffic, on per-flow or 

## Applicability and Scaling  *(p.254)*


## Benefits  *(p.254)*


## Functional Description  *(p.254)*


## Configuring Microburst Monitoring  *(p.254)*

11. Monitoring and Diagnostics 
multiple flows basis, and detect unexpected bursts of data in very short time intervals measured in 
microseconds. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Benefits 
Microburst monitoring provides clear indication of traffic and bursts passed, dropped or exceeding 
thresholds based on CIR/CBS and EIR/EBS. In addition, it helps facilitate bandwidth on demand. 
Functional Description 
Similar to OAM services statistics, microbursts statistics are collected for a certain PM interval, while this 
interval is defined from 1 to 900 seconds. 
When a Regular policer profile is used, excess bandwidth is shared or discarded, and the corresponding 
statistics are collected. When a Regular Accounting Only profile is used, only the statistics are collected, 
but the network traffic remains intact. 
Configuring Microburst Monitoring  
 To configure microburst monitoring, perform the following steps: 
1. Configure a policer profile (refer to Policer Profiles). 
2. Configure a flow. 
 To configure a flow with the web interface: 
1. Navigate to Configuration>Physical Ports>Flows> [SFP/ Port 1 | MSA/ Port 2] and click Add 
Flow. 
2. Set the PM collection parameters: 
a. Set PM Collection to Enable. 
11. Monitoring and Diagnostics 
b. Set PM Interval to the desired number of seconds to monitor traffic behavior during the 
interval. 
c. Set Policer type to Regular or Regular Accounting Only. 
3. Click Apply. 
4. Set the rest of the parameters as described in Per-Flow Tasks. 
MiNID 
  
 
 
 Configuration>Physical Ports>Flows>Add Flow 
  
 
 
 Flow Name 
 
Flow 1 
 Service Name 
 
Gold 
 Admin Status 
 
Enable 
 Ingress Port 
 
SFP/Port 1 
 L2CP Profile 
 
 
 L3L4 Loop 
 
Disabled 
 PM Collection 
 
Enable 
 PM Interval 
 
1 
 Policer Type 
 
Regular Accounting Only  
 Policer Profile 
 
mburst 
 Classification Tag Mode 
 
Single 
 Min VID Value 
 
0 
 Max VID Value 
 
4095 
 Min P-bit Value 
 
5 
 Max P-bit Value 
 
5 
 Flow Action 
 
Push VLAN 
  
 
 
 Apply 
 
 
  
 
 
Add Flow with PM Collection 
5. Navigate to Monitoring > Physical Port > Ethernet > Port [SFP/ Port 1 | MSA/ Port 2]. Click 
Statistics. 
Port statistics is displayed for the specified PM Interval. 