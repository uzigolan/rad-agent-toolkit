# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.5 OAM (TWAMP)

*Manual `MiNID_ver_2_6_mn.pdf`, pages 325–342.*


## Applicability and Scaling  *(p.325)*

11. Monitoring and Diagnostics 
Operational Status      : Send Local 
Loopback Status         : REMOTE 
 
OAM EFM Information 
-------------------------------------------------------- 
                Local                   Remote 
MAC Address     00-20-D2-51-42-52       -- 
OAM Mode        Active                  -- 
Unidirectional  Unsupported             -- 
Var Retrival    Unsupported             -- 
Link Events     Unsupported             -- 
Loopback        Supported               -- 
PDU Size        1518                    -- 
 To display the link OAM statistics: 
>config>oam>efm# show statistics 
OAM EFM Statistics 
-------------------------------------------------------- 
                        Rx              Tx 
Information             0               0 
Event Notification      0               0 
Loopback Ctrl           0               0 
Unsupported Codes       0 
11.5 OAM (TWAMP)  
MiNID provides up to 32 TWAMP Light Controller sessions that interoperate with TWAMP responders on 
other devices, by generating TWAMP test packets. You can display the session measurements and 
results. 
MiNID also provides up to 16 TWAMP Light responders that interoperate with TWAMP generators on 
other devices, by responding to TWAMP test packets with measurement packets.  
In addition, MiNID supports one-way loss TWAMP statistics. In order to calculate one-way packet loss, 
the following are required: 
• 
A responder that can generate an independent sequence number 
• 
A controller that is aware of the responder’s independent sequence number 
Applicability and Scaling 
This feature is applicable to all MiNID options. 

## Standards Compliance  *(p.326)*


## Benefits  *(p.326)*


## Functional Description  *(p.326)*

11. Monitoring and Diagnostics 
Standards Compliance 
RFC 5357 – A Two-Way Active Measurement Protocol (TWAMP) 
Benefits 
You can measure the IP performance of your Layer-3 network at all locations, without the need for a 
special performance management system. 
Functional Description 
TWAMP Responders 
The TWAMP Light mechanism provides for monitoring sessions where information is exchanged 
between TWAMP controllers and responders. The controller establishes the test session with the 
responder, and then the controller transmits test packets to the responder, which reflects the test 
packets to the controller. The controller processes the resulting measurements and calculates metrics 
that can be displayed in test reports.  
The  TWAMP responders work in Layer-2 probe mode, meaning they are bound to layer-2 interfaces 
(port/flow). A responder can be bound to more than one flow. The association between a TWAMP 
responder and flow/port is performed from the flow/port menus/CLI in the same way that flow/port 
layer-3/4 loopbacks are configured (see Flows for details). You can view statistics for TWAMP looped 
packets and bytes by viewing the associated flow statistics for layer-3/4 loopbacks. 
Note 
The TWAMP Light responders work in non-standard mode, i.e. the parameters 
for the TWAMP Light responder session are configured manually in  via the 
web/CLI, rather than by TWAMP control protocol. 
You can configure the following parameters for a TWAMP controller. 
TWAMP Controller Parameters 
Parameter 
Description 
Web 
CLI 
Controller Name 
controller <controller-name> 
Name of TWAMP controller in , up to 32 characters 
11. Monitoring and Diagnostics 
Parameter 
Description 
Web 
CLI 
IP Address 
local-ip-address <router-
interface-1|router-interface-2| 
router-interface-3|router-
interface-4|router-interface-5> 
Router interface associated with the controller, from 
which you can send TWAMP test packets and ARP 
requests. 
 
Admin Status 
shutdown 
Administratively enable or disable the TWAMP 
controller 
You can configure the following parameters for a TWAMP responder. 
TWAMP Responder Parameters 
Parameter 
Description 
Web 
CLI 
Responder ID 
Not applicable 
Identification number assigned by MiNID, not 
user-configurable, displayed only in Web  
Responder Name 
responder <responder-name> 
Name of TWAMP responder in MiNID, up to 
32 characters 
TWAMP Local IP 
ip-address 
IP address (IPv4 or IPv6) associated with the responder, 
to which to send TWAMP test packets, ARP requests, or 
pings 
TWAMP UDP Port 
udp-port 
UDP port (range 1–65535) associated with responder  
Note: The combination of IP address and UDP port must 
be unique for each TWAMP responder. 
Use Loaned IP 
ip-loan 
If enabled,  responds only to TWAMP test packets sent 
to the TWAMP responder IP address, and does not 
respond to ARP/ping requests sent to the TWAMP 
responder IP address. This is useful if you have 
configured the responder with the same IP address as 
the  host device (i.e. the IP address was loaned from the 
host), and you want the host to answer ARP/ping 
requests. 
Admin Status 
shutdown 
Administratively enable or disable the TWAMP 
responder 

## Factory Defaults  *(p.328)*

11. Monitoring and Diagnostics 
MAC Allocation Logic  
The following MAC addresses are available in the device: 
• 
Device Management MAC – used for MiNID management and for TWAMP sessions 1 and 3 
• 
Router Int 2,4 MAC address – used for TWAMP sessions 2 and 4 
• 
Device Services MAC address – used for OAM/CFM only (not for TWAMP). 
 
They can be seen in the CLI and in Web GUI as follows: 
MiNID 
  
 
 
 Monitoring - System 
  
 
 
 Device Management MAC address 00-20-D2-51-7E-2D 
 
 Router Int2,4 MAC address 
00-20-D2-51-7E-2F 
 
 Device Services MAC address 
00-20-D2-51-7E-2E 
 
 System Up Time (hh:mm:ss) 
05:35:48 
 
 DIP Switches Mode 
Normal 
 
  
 
 
 Current date 
10 May 2025 14:15:51+00:00 
 
 Summer time 
not configured 
 
  
 
 
 NTP 
 
 
 Events Log 
 
 
  
 
 
 
MiNID>config>system# show status 
Device Management MAC address    :      00-20-D2-E2-37-93 
Router Int 2,4 MAC address       :      00-20-D2-E2-37-94 
Device Services MAC address      :      00-20-D2-E1-B3-C6 
System UP Time (hh:mm:ss)        :      948:05:02 
DIP Switches Mode                :      NORMAL 
Factory Defaults 
By default, no TWAMP controllers or responders are configured.  

## Configuring TWAMP  *(p.329)*

11. Monitoring and Diagnostics 
Configuring TWAMP 
 To configure TWAMP, perform the following steps: 
1. In the responder device: 
a. Configure relevant router interface and flows. 
b. Configure and activate TWAMP responder and relevant test session(s). 
2. In the controller device: 
a. Configure relevant router interface and flows. 
b. Configure TWAMP profile(s). 
c. Configure and activate TWAMP controller and relevant peers and test sessions. 
Profile is a set of properties that a TWAMP session has. You have to define at least one profile in order 
to define a TWAMP controller. 
Configuring TWAMP Controllers 
 To configure a TWAMP controller in the web interface: 
1. Navigate to Configuration > OAM > TWAMP > Controller. 
 
 
 
  
 
 
 
 
Configuration>OAM>TWAMP>Controller 
 
 
 
Add new Controller 
 
 
 
Controller 
Name 
 
 
 
 
 
Controller1 
Add Peer 
Show Peers 
Status 
Delete Controller 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Configuring TWAMP Controllers 
2. To add a new TWAMP controller: 
a. Click Add new Controller.  
11. Monitoring and Diagnostics 
 
 
 
 
 
Configuration>OAM>TWAMP>Controller>TWAMP Controller>New 
Controller 
 
 
 
 
Controller Name 
 
 
 
IP Address 
 
Router Interface 1 
 
Admin Status 
 
Disable 
 
 
 
Apply 
 
 
 
 
 
New TWAMP Controller 
b. Fill in the parameters as specified in the above figure.  
c. Click <Apply> to create the TWAMP controller. 
The Configuration>OAM>TWAMP Controller screen appears, with an entry containing the new 
TWAMP controller. 
3. Click Add Peer to define remote responder parameters in a TWAMP session.  
 
 
 
 
 
Configuration>OAM>TWAMP>Controller>Peer>TWAMP Peer> New Peer 
 
 
 
 
Peer IP 
 
0.0.0.0 
 
Activation 
 
OFF 
 
Responder Sequence Num 
 
OFF 
 
Calculation Mode 
 
Round-Trip 
 
 
 
Apply 
 
 
 
 
 
New TWAMP Peer 
a. Fill in the parameters as specified in the table below. 
b. Click <Apply> to create the peer. 
 To add or configure a TWAMP controller in the CLI: 
1. Navigate to configure oam twamp controller <controller-name> [<number>], where 
<controller-name> is the name of the controller and <number> is the controller ID number. 
The config>oam>twamp>controller(<controller-name>)# prompt is displayed. 
11. Monitoring and Diagnostics 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Administratively enabling or 
disabling the controller 
no shutdown 
Enter shutdown to administratively 
disable the controller. 
You should enable the controller only 
after the responder has been configured 
and enabled. 
Configuring controller IP 
address 
local-ip-address <router-interface-1|router-
interface-2| router-interface-3|router-
interface-4|router-interface-5> 
If Loaned IP is enabled on router 
interface #1, controller IP address can be 
configured on any other router interface 
Assigning an IP address to the 
remote responder (peer). 
peer <ip-address> 
See  Running Test Sessions via 
Controller Peers 
Viewing controller status 
show-status 
 
Running Test Sessions via Controller Peers 
Do one of the following: 
• 
In the web interface: 
a. Navigate to Configuration > OAM > TWAMP > Controller. 
b. In the row of the configured controller, click Show Peers.  
c. In the row of the selected peer, click Add Test Session. 
 
 
 
 
 
Configuration – OAM – TWAMP – Controller- Peer - Test Session - 
TWAMP Test Session - New Test Session 
 
 
 
 
Test Session Name 
 
 
 
TWAMP Profile 
 
<profile-name> 
 
Display Num 
 
0 
 
UDP Port 
 
0 
 
DSCP 
 
0 
 
 
 
Apply 
 
 
 
 
 
Configuring New Test Session 
a. Fill in the parameters as specified in the table below. 
11. Monitoring and Diagnostics 
b. Click <Apply> to create the test session. 
• 
In the CLI: 
a. Navigate to configure oam twamp controller <name>peer <ip-address>. 
The config>oam>twamp>controller (<name>)>peer(<ip-address>)# prompt is displayed. 
b.  Enter all necessary commands according to the tasks listed below. 
c. Enter all necessary commands according to the tasks listed below. 
Peer Parameters 
Task 
Command 
Comments 
Activating all configured test 
sessions in one-time mode 
activate 
activate duration <minutes> 
The tests run for the specified amount of 
time. 
Type no activate to deactivate the one-
time (non-continuous) command. 
Activating all configured test 
sessions in continuous mode 
activate continuous 
The tests run until they are stopped. 
Type no activate to deactivate the 
continuous command. 
Defining the type of calculation 
for the TWAMP metrics 
calculation-mode <round-trip> 
TWAMP controller calculates standard 
TWAMP metrics. 
Specifying whether the 
responder transmits an 
independent sequence number 
responder-seq-num 
Notes: 
The controller calculates one-way loss 
and availability only if this is enabled. 
The corresponding responder must be 
configured to transmit the responder 
sequence number. 
Configuring test session 
test-session <number> name 
<name-string> udp-port <udp-
port-number> test-profile 
<profile-name> dscp <dscp-
number> 
The UDP and DSCP can be used to 
distinguish between test sessions. 
UDP port number: 1-65535 
Test profile name: Up to 32 characters 
DSCP number: 0-63 (default: 0) 
 Viewing test report 
show-report <test-name> 
{interval|current|all} 
[<interval-num>] 
See Viewing TWAMP Reports 
Viewing summary of test 
reports 
show summary-report 
See Viewing TWAMP Reports 
Viewing test status 
show status 
See Viewing TWAMP Status 
11. Monitoring and Diagnostics 
 To delete a TWAMP controller: 
1. Navigate to configure oam twamp. 
2. Type no controller <controller-name>. 
Configuring TWAMP Profiles 
 To configure TWAMP profiles in the web interface: 
1. Navigate to Configuration>OAM>TWAMP>Profile. 
 
 
 
  
 
 
 
 
Configuration>OAM>TWAMP>Profile 
 
 
 
Add new Profile 
 
 
  
 
 
  
 
Profile 
Name 
 
 
Profile 1 
Delete Profile 
 
 
 
  
 
 
 
  
 
 
 
 
Configuring TWAMP Profiles 
2. To add a new TWAMP profile: 
c. Click Add new Profile. 
11. Monitoring and Diagnostics 
 
 
 
 
 
Configuration>OAM>TWAMP>Profile>TWAMP Profile>New Profile 
 
 
 
 
Profile Name 
 
 
Payload Length 
 
256 
 
Transmit Rate 
 
10 
 
Loss Timeout 
 
2000000 
 
Loss Ratio Threshold 
 
1000 
 
Delay Variation Threshold 
 
1000 
 
Delay Treshold 
 
1000 
 
Delay Variation Event Type 
 
pdv 
 
 
 
Apply 
 
 
 
 
 
New TWAMP Profile 
d. Fill in the parameters as specified in the table below. 
e. Click <Apply> to create the TWAMP profile.  
The Configuration>OAM>TWAMP>Profile screen appears, with an entry containing the new 
TWAMP profile. 
1. To delete a TWAMP profile, click Delete Profile in the corresponding row. 
The TWAMP profile is deleted. 
2. Click <Save Configuration>. 
 To add or configure a TWAMP profile in the CLI: 
1. Navigate to configure oam twamp profile <profile-name>, where <profile-name> is the name of 
the profile. 
The config>oam>twamp>profile(<profile-name>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
TWAMP Profile Parameters 
Task 
Command 
Comments 
Defining delay threshold in 
microseconds 
delay-threshold 
 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Configuring delay variation 
event type to define whether 
the PDV or IPDV metric is used 
for the delay threshold 
delay-variation-event-type 
pdv – Packet delay variation metric 
ipdv –Inter-packet delay variation metric 
Defining delay variation 
threshold in microseconds 
delay-variation-threshold 
 
Defining test packet loss 
timeout in microseconds 
loss-timeout  
 
Defining test session loss ratio 
threshold in ppm (packet per 
million) 
loss-ratio-threshold 
Range is 1000 – 10000 ppm 
Default: 1000 ppm 
Defining test packet payload 
length in bytes 
payload-length 
 
Defining test profile packet 
transmit rate in PPS 
transmit-rate <pps> 
 
 To delete a TWAMP profile: 
1. Navigate to configure oam twamp. 
2. Type no profile <profile-name>.  
The TWAMP profile is deleted. 
Configuring TWAMP Responders  
 To configure TWAMP responders in the web interface: 
1. Navigate to Configuration > OAM > TWAMP > Responder. 
11. Monitoring and Diagnostics 
 
 
 
 
  
 
 
 
Configuration – OAM – TWAMP - TWAMP Responder 
 
 
 
Add New TWAMP Responder Session 
 
 
 
 
 
 
 
 
 
ID 
Responder 
Name 
Admin 
Status 
TWAMP 
Local IP 
TWAMP 
UDP 
Port 
Tx 
Sequence 
Num 
Use 
Loaned IP 
 
 
 
 
 
1 
tw1 
Disable 
Session 
10.10.2.2 
3 
ENABLED 
ENABLED 
Status 
Unbind 
All 
Flows 
Delete 
Session 
 
 
2 
tw2 
Enable 
Session 
1.1.1.1 
5555 
DISABLED 
DISABLED 
Status 
Unbind 
All 
Flows 
Delete 
Session 
 
 
3 
tw3 
Enable 
Session 
10.10.2.2 
4 
DISABLED 
DISABLED 
Status 
Unbind 
All 
Flows 
Delete 
Session 
 
 
4 
tw4 
Disable 
Session 
2.2.2.2 
888 
ENABLED 
ENABLED 
Status 
Unbind 
All 
Flows 
Delete 
Session 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Configuring TWAMP Responders 
2. To add a new TWAMP responder:  
a. Click Add New TWAMP Responder Session.  
 
 
 
 
 
Configuration>OAM>TWAMP>Responder>TWAMP Responder>New 
Responder Session 
 
 
 
 
Responder ID 
 
5 
 
Responder Name 
 
 
 
IP Address 
 
 
UDP Port 
 
0 
 
Tx Sequence Num 
 
Enable 
 
Use Loaned IP 
 
Disable 
 
Admin Status 
 
Disable 
 
 
 
 
New TWAMP Responder 
 
11. Monitoring and Diagnostics 
b. Fill in the parameters as specified in See Peer Parameters table. 
c. Click <Apply> to create the TWAMP responder. 
The Configuration > OAM > TWAMP Responder screen (see above) appears, with an entry 
containing the new TWAMP responder. 
3. To enable or disable a TWAMP responder, click Enable Session/Disable Session in the 
corresponding row.  
4. To unbind all flows associated with a TWAMP responder, click Unbind All Flows in the 
corresponding row. 
5. To delete a TWAMP responder, click Delete Session in the corresponding row. 
6. The TWAMP responder is deleted, if it is administratively disabled and is not bound to any flows 
or ports. 
7. Click <Save Configuration>. 
 To add or configure a TWAMP responder with the CLI: 
1. Navigate to configure oam twamp responder <responder-name>, where <responder-name> is 
the name of the responder. 
The config>oam>twamp>responder(<responder-name>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning an IP address to the 
responder 
ip-address <ip-address> 
The address can be in either IPv4 or IPv6   
format. 
Specifying that the IP address 
assigned to the responder is 
loaned from the host device  
ip-loan 
Enter ip-loan for  to answer only 
TWAMP test packets sent to the IP 
address 
Enter no ip-loan for  to answer ARP/ping 
requests/TWAMP test packets sent to 
the IP address 
See Peer Parameters table for more 
details on IP loan  
Generating an independent 
sequence number for the 
TWAMP responder packets 
tx-sequence-num 
 
Administratively enabling or 
disabling the responder 
no shutdown 
Enter shutdown to 
administratively disable 
the responder 

## Viewing TWAMP Status  *(p.338)*

11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Assigning a UDP port to the 
responder 
udp-port <udp-port> 
1–65535 
Unbinding any flows associated 
with the TWAMP responder 
unbind-all-flows 
 
 To delete a TWAMP responder: 
1. Navigate to configure OAM TWAMP. 
2. Type no responder <responder-name>. 
Viewing TWAMP Status 
You can view the following statuses using the CLI: 
• 
Controller status – show status in level config oam twamp controller 
• 
Responder status – show status in level config oam twamp responder 
• 
Status of peer test sessions – show-status in level config oam twamp controller peer. 
• 
The data is also available in the web interface: 
• 
Controller status – Navigate to the Controller page and click Status in the row of the 
corresponding controller 
• 
Responder status - Navigate to the Responder page and click Status in the row of the 
corresponding responder 
• 
Status of peer test sessions – Navigate to the TWAMP Peers page and click Status in the row of 
the corresponding peer. 
 To view controller status: 
MiNID>config>oam>twamp>controller(1)# show status 
IPPM Type                    : TWAMP Light 
Router Interface             : 1 
Controller Status            : Ready 
 To view responder status: 
MiNID>config>oam>twamp>responder(tw1)# show status 
IPPM Type                    : TWAMP Light 
Responder Status             : Ready 

## Viewing TWAMP Reports  *(p.339)*

11. Monitoring and Diagnostics 
 
Responder Name     UDP       Tx-Packets      Rx-Packets 
-------------------------------------------------- 
tw1                3         1107             1107 
 To view peer test status: 
MiNID>config>oam>twamp>controller(1)>peer(33.33.116.6)# show-status 
IPPM Type                    : TWAMP Light 
Activation Mode              : continuous 
Calculation Mode             : round-trip 
Start Time                   : 00:00:54 01-01-1970 
 
Controller Test-Name Peer          UDP   Status      Tx-Packets   Rx-Packets 
------------------------------------------------------------------------- 
1          1         33.33.116.6   5001   In Progress   1770       1770 
1          2         33.33.116.6   5002   In Progress   1770       1770 
1          3         33.33.116.6   5003   In Progress   1770       1770 
1          4         33.33.116.6   5004   In Progress   1770       1770 
1          5         33.33.116.6   5005   In Progress   1770       1770 
1          6         33.33.116.6   5006   In Progress   1770       1770 
1          7         33.33.116.6   5007   In Progress   1770       1770 
1          8         33.33.116.6   5008   In Progress   1771       1771 
Viewing TWAMP Reports 
TWAMP Metrics 
The  TWAMP controller calculates performance measurement metrics according to the received test 
packets for each peer and its active test sessions. The metrics are recalculated every minute. You can 
view the metrics for the current interval, selected interval, or all intervals by viewing the TWAMP report.  
When the TWAMP responder receives a test packet, it reflects the test packet after it adds an Rx stamp 
and a Tx stamp.  
When the TWAMP controller receives a test packet from the responder, it calculates the following:  
• 
Delay = Responder Rx stamp - Controller Tx stamp + Controller Rx stamp –Responder Tx stamp 
• 
Forward delay = Responder Rx stamp - Controller Tx stamp 
• 
Backward delay = Controller Rx stamp - Responder Tx stamp 
• 
Packet validity – determined by checking if the delay is less than the value configured by 
command loss-timeout. If so, the Rx valid count is incremented, otherwise the packet is 
dropped. 
11. Monitoring and Diagnostics 
The following table lists the metrics that are displayed in the TWAMP reports, subject to the restrictions 
specified above for the calculation modes. See Viewing the Metrics for instructions on viewing the 
reports and for examples of TWAMP reports. 
TWAMP Report Metrics 
Counter 
Description 
Availability Count (sec) 
Number of available seconds. A minute is declared as unavailable if it has 
more than 75% packet loss, therefore it is available if packet loss is 25% or 
less. When a minute is declared unavailable, the delay, delay variation, loss 
measurements, and their derived metrics are ignored for that minute. 
Availability Count Fwd/Back 
Number of available seconds. A minute is declared as unavailable if it has 
more than 75% packet loss, therefore it is available if packet loss is 25% or 
less. When a minute is declared unavailable, the delay, delay variation, loss 
measurements, and their derived metrics are ignored for that minute. These 
statistics are for the forward and backward directions.  
Note: These statistics appear only when responder seq-num is enabled.  
Delay Average (ms) 
Average of packet delay values 
Delay Max (ms) 
Maximum of packet delay values 
Delay Min (ms) 
Minimum of packet delay values 
Delay Threshold Crossing 
Count 
Number of packets with delay larger than the delay threshold configured for 
the corresponding test profile 
Duplicate Packets Back 
Number of duplicate packets in backward direction. A packet is considered 
duplicate (backward) if its responder Tx timestamp matches that of a 
previously received packet in backward direction. 
Duplicate Packets Fwd  
Number of duplicate packets in forward direction. A packet is considered 
duplicate (forward) if its controller sequence number or controller Tx 
timestamp matches that of a previously received packet in forward direction. 
Duplicate Ratio Back  
Duplicate Packets Back divided by Tx Packets Back, converted to a percentage 
Duplicate Ratio Fwd  
Duplicate Packets Fwd divided by Tx Packets Fwd, converted to a percentage 
Fragmented Packets Back  
Number of fragmented packets in backward direction. When the TWAMP 
controller recognizes a fragmented packet, it increments the Fragmented 
Packets Back counter. 
11. Monitoring and Diagnostics 
Counter 
Description 
Fragmented Packets Fwd  
Number of fragmented packets in forward direction. When the TWAMP 
responder receives a fragmented packet, when it reflects it to the controller, 
the responder sends indication of fragmentation, if tx-extended-info was 
enabled. When this indication is received, the controller increments the 
Fragmented 
Packets Fwd counter. 
IPDV Average (ms)  
Average of IPDV (Inter Packet Delay Variation) values in both directions 
IPDV Max (ms)  
Maximum of IPDV (Inter Packet Delay Variation) values in both directions. 
Inter Packet Delay Variation is calculated according to RFC 5481, from the 
variations of the delays between valid packets. 
IPDV-Back Average (ms) 
Average of IPDV (Inter Packet Delay Variation) values in backward direction 
IPDV-Back Max (ms) 
Maximum of IPDV (Inter Packet Delay Variation) values in backward direction 
IPDV-Fwd Average (ms)  
Average of IPDV (Inter Packet Delay Variation) values in forward direction 
IPDV-Fwd Max (ms)  
Maximum of IPDV (Inter Packet Delay Variation) values in forward direction 
Loss Packets 
Number of packets lost 
Loss Packets Fwd/Back 
Number of packets lost in each of the directions, calculated by Tx Packets –Rx 
valid count  
Note: These statistics appear only when responder seq-num is enabled. 
Loss Ratio 
Loss Packets divided by Tx Packets, converted to a percentage 
Loss Ratio Fwd/Back 
Loss Packets divided by Tx Packets, converted to a percentage in each of the 
directions 
Note: These statistics appear only when responder seq-num is enabled. 
PDV Average (ms) 
Average of PDV (Packet Delay Variation) values, calculated by subtracting 
Delay Min from Delay Average 
PDV Max (ms)  
Maximum of PDV (Packet Delay Variation) values. Packet Delay Variation is 
calculated according to ITU-T Y.1540, by subtracting the minimum delay from 
the 99.9% percentile of the delay values 
Reordered Packets Back  
Number of reordered packets in backward direction. A packet is considered 
reordered (backward) if its responder sequence number is smaller than that 
of a previously received packet in backward direction. 
Reordered Packets Fwd  
Number of reordered packets in forward direction. A packet is considered 
reordered (forward) if its controller sequence number or controller Tx 
timestamp is smaller than that of a previously received packet in forward 
direction. 
11. Monitoring and Diagnostics 
Counter 
Description 
Reordered Ratio Back 
Reordered Packets Back divided by Tx Packets converted to a percentage 
Reordered Ratio Fwd 
Reordered Packets Fwd divided by Tx Packets converted to a percentage 
Tx Packets 
Number of packets transmitted in forward direction (controller to responder) 
Tx Packets Fwd/Back 
Number of packets transmitted forwared (from controller to responder) and 
back (from responder to controller) 
Note: These statistics appear only when responder seq-num is enabled. 
Viewing the Metrics 
You can view the following reports in level config oam twamp controller peer: 
• 
Summary report of all peer test sessions –show-summary-report 
• 
Test report of a particular session: 
 
Test report of all intervals – show-report <name> all 
 
Test report of current interval – show-report <name> current 
 
Test report of selected interval – show-report <name> interval <interval-num> 
 To view a summary report: 
MiNID>config>oam>twamp>controller(1)>peer(33.33.116.6)# show-summary-report 
IPPM Type                    : TWAMP Light 
Controller IP Address        : 33.33.116.4 
Responder IP Address         : 33.33.116.6 
Activation Mode              : continuous 
Calculation Mode             : round-trip 
 
Controller Test-Name  IP   Size    Loss     Delay    PDV      IPDV     Result 
                      DSCP         Ratio    Max      Max      Max 
                           (bytes)          (ms)     (ms)     (ms) 
----------------------------------------------------------------------------- 
1           1         1     256     0        1.891   0.246    1.790    NA 
1           2         1     256     0        0.321   0.147    0.221    NA 
1           3         1     256     0        0.390   0.173    0.290    NA 
1           4         1     256     0        0.374   0.176    0.274    NA 
1           5         1     256     0        0.301   0.144    0.201    NA 
1           6         1     256     0        0.351   0.164    0.250    NA 
1           7         1     256     0        1.889   0.092    1.789    NA 
1           8         1     256     0        0.316   0.181    0.216    NA 
 