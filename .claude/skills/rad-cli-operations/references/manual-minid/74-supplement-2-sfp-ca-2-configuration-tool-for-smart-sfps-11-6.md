# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.6 Packet Capture

*Manual `MiNID_ver_2_6_mn.pdf`, pages 343–356.*


## Applicability and Scaling  *(p.343)*

11. Monitoring and Diagnostics 
 To view a test report: 
MiNID>config>oam>twamp>controller(1)>peer(2.2.2.2)# show-report 1 all 
Test Name                    : 1 
IPPM Type                    : TWAMP Light 
Controller IP Address        : 33.33.116.4 / 1229 
Responder IP Address         : 33.33.116.6 / 5001 
IP DSCP                      : 11 
Payload Length (bytes)       : 256 
Calculation Mode             : round-trip 
Test Session Start Time      : 00:00:54 01-01-1970 
 
Test Interval                       : Current 
Elapsed Time                   (sec): 420 
 
Tx Packets                          : 4200 
Loss Packets                        : 0 
Loss Ratio                          : 0 
Availability Count             (sec): 420 
Tx Packets         Fwd / Back       : 0           0 
Loss Packets       Fwd / Back       : 0           0 
Loss Ratio         Fwd / Back       : 0           0 
Availability Count Fwd / Back  (sec): 0           0 
Duplicate Packets  Fwd / Back       : 0           0 
Duplicate Ratio    Fwd / Back       : 0           0 
Reordered Packets  Fwd / Back       : 0           0 
Reordered Ratio    Fwd / Back       : 0           0 
Fragmented Packets Fwd / Back       : 0           0 
 
Delay Threshold Crossing Count      : 1 
Delay      Min / Max / Average (ms) : 0.099           1.891           0.101 
PDV              Max / Average (ms) : 0.182           0.002 
IPDV             Max / Average (ms) : 1.790           0.002 
IPDV-Fwd         Max / Average (ms) : 0.002           0.000 
IPDV-Back        Max / Average (ms) : 1.790           0.002 
11.6 Packet Capture 
MiNID sends packets to a PC running Wireshark or another packet analyzer supporting RPCAP. Then the 
traffic can be recorded and analyzed on the PC. 
Performance was tested with Wireshark version 1.12 and 2.0.3. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 

## Standards Compliance  *(p.344)*


## Benefits  *(p.344)*


## Functional Description  *(p.344)*

11. Monitoring and Diagnostics 
Standards Compliance 
RPCAP – Remote Packet Capture 
Benefits 
MiNID  can replace an equipped PC running Wireshark or dumpcap (Wireshark’s CLI) that is required at 
the viewing point.  MiNID captures bidirectional traffic and sends it to a packet analyzer running on a 
remote PC over IP/UDP/RPCAP. By configuring the analyzer filters, you can troubleshoot your network, 
analyze traffic, and use the data for software and communications protocol development. 
By applying relevant traffic filters,  tunnels only selected packets, thus reducing the network workload 
and preventing the PC from collapsing when there is a large number of packets. 
Functional Description 
MiNID enables you to capture real-time traffic and to transport it to a remote viewing /recording 
station. The station running Wireshark initiates the RPCAP tunneling session from the MiNID. 
MiNID can manipulate the captured traffic by editing or discarding frames. All flow actions are 
supported. 
The following scenario and example illustrate how packet capturing is performed. 
The user wishes to perform the flow action of push VLAN between the two ports of SFP and MSA):  
• 
If the user has defined the packet capture on one of the ports (for example, the SFP port), and 
the traffic arrives from the SFP (in the direction of the MSA), the user sees the captured packets 
before the push VLAN flow action has been performed.  
• 
If the traffic arrives from the MSA (in the direction of the SFP), the user sees the packets 
captured after the push VLAN flow action has been performed. 
Note 
Some of the traffic processed by  is not captured; only traffic passing through  
is captured. The feature of packet capture does not mirror traffic, such as 
OAM packets, which is addressed to  itself. 
 
Note 
Packet Capture applies to the IP address of the relevant router interface. 

## Factory Defaults  *(p.345)*


## Configuring Packet Capture  *(p.345)*

11. Monitoring and Diagnostics 
It is possible that timestamping of the captured traffic is altered due to synchronization with the NTP 
server clock. To prevent the time amendments during packet capturing, usage of NTP as a clock source 
can be disabled by choosing the Free Run option. 
Factory Defaults 
By default, packet capturing is disabled. 
When packet capturing is enabled, it is configured as shown below. 
Parameter 
Default  
Remarks 
capture-dscp 
0 
DSCP value for the mirrored traffic 
local-ip-address 
router-interface-1 
Dedicated IP interface for packet capture 
rpcap-tcp-port 
2002 
TCP port number 
inactive-timeout 
5 
Packet capture session inactivity timeout in 
minutes 
timestamp-source 
freerun 
Source of timestamping for captured traffic 
Configuring Packet Capture 
Enabling Packet Capture 
 To enable packet capture using the web interface: 
1. Navigate to Configuration > Packet Capture. 
11. Monitoring and Diagnostics 
 
 
 
  
 
 
 
 
Configuration>Packet Capture 
 
 
 
 
Capture 
 
Disable 
 
 
 
 
 
Capture-
DSCP 
 
0 
 
 
 
 
 
Local IP Address 
Router Interface 1 
 
 
 
 
RPCAP TCP Port 
 
2002 
 
 
 
 
 
 
Inactive Timeout 
 
Enable 
 
 
 
 
 
Inactive Timeout [Min.] 
5 
 
 
 
 
Timestamp Source 
Free Run 
 
 
 
 
 
 
 
 
 
 
 
 
 
Show Status 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Apply 
 
 
 
 
 
 
 
 
 
 
Enabling Packet Capture 
1. Fill in the relevant parameters as described in the table below. Set the Capture status to Enable. 
2. Click <Apply>. 
 To enable packet capture using the CLI: 
1. Navigate to configure>packet-capture. 
The config>packet-capture# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Packet Capture Parameters 
Task 
Command 
Comments 
Enabling or disabling packet 
capturing 
[no] capture 
Type capture to administratively enable 
packet capturing 
Setting the DSCP value for the 
mirrored traffic 
capture-dscp 
Range [0-63] 
Defining packet capture session 
inactivity timeout in minutes 
[no] inactive-timeout 
When timeout period is over, packet 
capturing is disabled. 
Possible values: 1-65536 minutes 
11. Monitoring and Diagnostics 
Task 
Command 
Comments 
Setting dedicated IP interface 
for packet capture 
local-ip-address <router-interface-1|router-
interface-2| router-interface-3|router-
interface-4|router-interface-5> 
If Loaned IP is enabled on router 
interface #1, packet capture can be set 
on any other router interface  
Setting the TCP port 
rpcap-tcp-port 
 
Displaying the status of the 
current Packet Capture session 
show status 
See Viewing  Statistics for Packet 
Capture 
Setting the source of 
timestamping for captured 
traffic 
timestamp source <freerun|ntp> 
freerun – internal clock is used as a 
timestamping source 
ntp – NTP server clock is used as a 
timestamping source 
Configuring a Wireshark Session 
You can have only one running Wireshark session. To open a new session, you have to close the previous 
one. 
 To define a new session: 
1. Open Wireshark. Click the Capture options 
 button on the Wireshark toolbar. 
The Capture Interfaces window opens. 
11. Monitoring and Diagnostics 
 
 
Capture Interfaces Window of Wireshark 
2. Click the Manage Interfaces button. 
The Manage Interfaces window opens. Switch to the Remote Interfaces tab. 
3. Click the + button in the bottom left to add a new remote interface.  
The Remote Interface window opens. 
11. Monitoring and Diagnostics 
 
Remote Interfaces Window of Wireshark 
4. Fill in the  local IP address (by default, 192.168.205.1) and TCP port (by default, 2002). Click OK. 
Two new interfaces are added. 
11. Monitoring and Diagnostics 
 
Adding  Ports as Remote Interfaces 
5. Select both  ports. For each of the ports, click the Remote Settings button. 
The Remote Capture Settings window opens. 
6. Under Capture Options, select Use UDP for data transfer. Click OK. 
 
Remote Capture Settings 
7. Close the Manage Interfaces window by clicking OK. 
11. Monitoring and Diagnostics 
Both  ports appear in the list as remote interfaces. 
8. In the Capture Interfaces window, select one of the  ports by clicking on its row.  
9. Click the Start button to initiate packet capturing. 
 
Starting a Session 
Wireshark starts to display all traffic in the main window. 
11. Monitoring and Diagnostics 
 
 
Captured Traffic in Wireshark Window 
10. To end the session, click the Stop capturing packets 
 button on the Wireshark toolbar. 
Configuring Display Filters in Wireshark 
In addition to capturing the whole traffic, you can apply various filters to choose only specific type of 
traffic. 
Note 
MiNID supports filtering of IPv4 packets. IPv6 packets are ignored. 
 
11. Monitoring and Diagnostics 
 To define a display filter: 
1. Click the Capture options 
 button on the Wireshark toolbar. 
The Capture Interfaces window opens. 
2. In the Capture filter for selected interfaces field, type the filtering criteria. For displaying only 
one host, type host <host-IP>. Click Start. 
 
Now Wireshark displays only traffic coming from and arriving to the host with the specified IP. 
11. Monitoring and Diagnostics 
 
Captured Traffic with a Filter Applied 
The following filtering criteria can be added: 
Filters Applied to Captured Traffic 
Criteria 
Command 
Comment 
Traffic coming from 
and to a selected host 
host <host-ip> 
ARP and reverse ARP packets for the 
host are captured as well, when only 
IP address is specified. 
This parameter is required to get a 
correct filter expression 
Traffic coming from a 
selected host 
src host <host-ip> 
 
11. Monitoring and Diagnostics 
Criteria 
Command 
Comment 
Traffic arriving to a 
selected host 
dst host  <host-ip> 
 
Applied protocol 
<protocol name> 
IP traffic includes only IPv4 packets, 
not IPv6 packets. Protocol name 
should be paired with ipv4 
Example: 
tcp and ipv4 
Port used in a source 
host 
src port <port number> 
 
Port used in a 
destination host 
dst port <port number> 
 
 
Note 
You can define up to two filter expressions concatenated by or. The 
parameters within a filter expression are joined by and.  
Example:  
(src host 1.1.1.1 and dst host 4.4.4.4  
and tcp src port 1025 and tcp dst port 2050) 
or 
(src host 4.4.4.4 and dst host 1.1.1.1 
and tcp src port 2050 and tcp dst port 1025) 
Configuring Packet Truncation 
MiNID enables you to take only the most important data (start of a packet) and pass it to the viewing 
station. The truncated packet size should be specified in Wireshark. The software displays the full packet 
size if you specify the size of the truncated file more than 12,000 bytes. If the value is less than 32 bytes 
or more than 255 bytes, Wireshark displays an error message. 
 To display truncated packets: 
1. In Wireshark, open the Capture Interfaces window. 
2. In the row of the selected  port, double-click the Snaplen (B) field to open it editing.  
3. Type the desired file size to be captured in the range of 32-255 bytes. Click Start. 
Wireshark displays truncated packets. 

## Viewing  Statistics for Packet Capture  *(p.356)*

11. Monitoring and Diagnostics 
Viewing  Statistics for Packet Capture 
 To view statistics in: 
1. In the web interface, click Show Status in the Packet Capture page. 
2. In the CLI, navigate to config> packet-capture and type show status. 
Relevant statistic parameters are displayed. 
Capture state             : In Progress 
Destination address       : 192.168.205.55 
Encapsulation protocol    : RPCAP 
TCP port                  : 2002 
UDP port                  : 59093 
 
--------------------------------------------------------- 
Capture port              : 1 
Capture packet size       : First 255 Bytes 
Start                     : 02:37:01 01-01-1970 
End                       : N/A 
Elapsed time              : 00:09:49 
Tx packets                : 54 
 
Capture rule #1 
--------------------------------------------------------- 
Pass All 
 
Capture rule #2 
--------------------------------------------------------- 
Pass All 
Packet Capture Status 
Parameter 
Value 
Description 
Capture State 
in progress|ready|disabled 
• In progress – Wireshark 
session is running 
• Ready – Wireshark 
session is completed 
• Disabled – capturing is 
administratively disabled 
in  
Destination Address 
<ip-addresss> 
 
Encapsulation protocol 
RPCAP 
 
TCP port 
<tcp-port-number> 
 
UDP port 
<udp-port-number> 
 