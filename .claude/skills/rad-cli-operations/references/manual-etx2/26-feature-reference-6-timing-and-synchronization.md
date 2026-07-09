# Feature Reference – 6 Timing and Synchronization

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1150–1218.*


## 6.1 1588v2 Timing  *(p.1150)*

6 Timing and Synchronization 
6.1 1588v2 Timing 
ETX-2i devices with PTP fully support 
for distribution of synchronization signals over packet-switched networks. 
PTP is beneficial for applications that recover or distribute timing information. 
Best Master Clock Algorithm (BMCA) improves clock synchronization. 
Applicability and Scaling 
This feature is applicable to ETX-2i, ETX-2i-B, ETX-2i-10G/4SFPP, ETX-2i-10G-B/4SFPP, and  
ETX-2i-10G-B/8SFPP, with PTP options, under the following conditions: 
• 
ETX-2i, ETX-2i-10G, and ETX-2i-10G-B/8SFPP/PTP support the following 1588v2 entities:  
 
Grand Master clock (no GPS) 
 
Standalone slave clock 
 
Boundary clock 
• 
For G.8275.1, the PTP port limits are as follows: 
 
PTP ports with master role per device is <number of Ethernet ports> - 1, as follows: 
 
ETX-2i, ETX-2i-10G-B/8SFPP/PTP: Up to 7 
 
ETX-2i-10G full 19-inch: Up to 27 
 
PTP ports with slave role per device (ETX-2i, ETX-2i-10G 19-inch, ETX-2i-10G-B/8SFPP/PTP: 
Up to 2 
 
PTP Master ports cannot be defined on LAGs. 
• 
<slot> is relevant for ETX-2i, ETX-2i-B, and ETX-2i-10G. 
All devices (with and without timing), except for ETX-2i-100G/4Q, support transparent clock (TC).  
ETX-2i Devices 
6. Timing and Synchronization 
Standards Compliance 
IEEE 1588 Precision Time Protocol 
ITU-T G.8265.1 Precision Time Protocol Telecom Profile 
ITU-T G.8275.1 Precision Time Protocol Telecom Profile  
ITU-T G.8275.2 Precision time protocol telecom profile for time/phase synchronization with partial 
timing support from the network 
ITU-T G.8273.2 Telecom Boundary Clock (T-BC) Specification 
Functional Description 
PTP Protocols 
G.8265.1 is an end-to-end protocol based on IP packets. The synchronization message rate and 
announce rate are negotiated between the slave and master. The G.8265.1 protocol is used to obtain 
frequency and time. 
G.8275.1 is a point-to-point protocol based on Layer-2 multicast messages. There is no signaling phase; 
the message rate is always 16 PPS and the announce rate is 8 PPS. The G.8275.1 protocol is used to 
obtain time rather than frequency. It obtains frequency from SyncE to get a more accurate time. The 
reference frequency is taken from the Clock Selection Mechanism (CSM) source if it is PRC; otherwise 
from the 1588v2 frequency. 
G.8275.2 supports telecom applications that require accurate phase and time synchronization for phase 
alignment and time of day synchronization over a wide area network, as in mobile cellular systems. 
Based on partial timing support (PTS) or assisted partial timing support (APTS) from the network 
architecture, G.8275.2 does not require nodes to be directly connected. This profile is used in well-
planned cases where network behavior and performance can be constrained within well-defined limits, 
including limits on static asymmetry. 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
1588v2 Entities 
ETX-2i supports the following 1588v2 entities: 
Grand Master 
Distributes the clock signal over PTP (no GPS) 
Standalone slave 
Recovers the clock signal from master clocks 
Boundary clock 
Transfers time of day (ToD) and frequency from a remote master clock to one or more 
slave clocks. The boundary clock is implemented as a back-to-back master and slave 
clock. 
 
Note 
Only IPv4 addresses are supported in the timing/synchronization messaging.  
PTP Port 
Note 
PTP port configuration is required for G.8275.1 only. 
When a 1588v2 entity acts according to G.8275.1, you need to configure a PTP port entity for each clock 
entity. The PTP port has a provisioned state that you configure, as well as an actual state. The 
provisioned state can be one of the following: 
Slave 
Acts as the time source of ETX-2i 
Master 
Provides the distribution path for the device time 
The actual state can be one of the following: 
• 
Slave (one per device) 
• 
Master 
• 
Passive – neither master nor slave 
Best Master Clock Algorithm (BMCA) 
ETX-2i uses Best Master Clock Algorithm (BMCA) to select the best clock from the ports provisioned as 
slave. The selection is done according to port priority and quality level received in announce messages.  
The actual state of the provisioned slave port that is selected as the best clock is set to slave. The actual 
state of the provisioned slave ports not selected is set to passive. 
Under G.8275.1, BMCA is supported over two PTP Slave Ports only. Automatic PTP port state settings 
are not supported, and therefore G.8275.1 is not applicable over G.8032 Ring or RSTP topologies. 
ETX-2i Devices 
6. Timing and Synchronization 
Slave Clock 
The standalone slave clock complies with G.8265.1, G.8275.2, or G.8275.1. 
G.8265.1, G.8275.2 
The G.8265.1 or G.8275.2 slave clock can work in one-way mode, where it receives only frequency from 
up to two IEEE 1588 master clocks, or in two-way mode (full synchronization), where it receives 
frequency and time. When the master clock grants signal transmission it notifies the slave clock of the 
master clock quality level and source port identification, then periodically transmits synchronization 
signals. 
The slave clock works in the following recovery modes:  
Time (also referred 
to as Hybrid) 
The slave uses its regenerated frequency to reconstruct the remote clock or uses a 
high-quality clock (PRC/PRS) from the clock domain. Therefore, the time accuracy 
depends on the quality of the reconstructed frequency; noise in the frequency 
generation impacts the time accuracy. 
Frequency 
The slave reconstructs the remote clock using Sync messages and delay 
request/response sent from master to slave. Time-related status and alarms, as well as 
time indication over the ToD interface, are not supported. 
Frequency and Time 
The slave provides frequency information and time information as described above. As 
the slave uses the frequency for time recovery, a high-quality reference clock usually 
improves the time recovery, except in the case of network asymmetry. 
1588v2 traffic is transmitted only via Ethernet port 0/1. 
G.8275.1  
The G.8275.1 slave clock receives frequency from one or more IEEE 1588 master clocks that periodically 
transmit synchronization signals. 
The slave clock works in time (also referred to as hybrid) recovery mode. The slave uses both Sync and 
Delay messages to reconstruct the remote clock and takes the reference frequency from the clock 
domain (same as the G.8265.1 slave in hybrid mode). 
G.8275.1 meets the requirements of G.8273.2. 
Boundary Clock 
The boundary clock is defined in ETX-2i as a back-to-back master and slave clock sharing the same IP 
address and PTP domain. The slave and master can both be a G.8265.1, G.8275.2, or G.8275.1 entity. Or, 
ETX-2i Devices 
6. Timing and Synchronization 
the slave can be a G.8265.1 entity and the master a G.8275.1 entity, or vice versa, as dual mode master 
is supported in both G.8265.1 and G.8275.1. Dual mode master is not supported in G.8275.2. 
The boundary clock performs the following tasks: 
• 
The local slave recovers reference ToD and frequency from a remote master. 
• 
The local master uses the local slave recovered ToD as its reference ToD. 
• 
The local master uses the local slave recovered frequency as its reference frequency. 
Master Clock (Standalone) 
The standalone master is the only mode available for ETX-2i-10G-B/8SFPP Outdoor with GNSS. The 
master distributes timing information to up to 64 slaves. 
The master clock receives both frequency and time information from the GNSS only, or frequency from 
the system clock.  
The standalone master clock can comply with G.8265.1 or G.8275.1, or it can function as a dual mode 
master, also called a Distributed PTP Grandmaster (DISTRIBUTED GM®), which supports PTP and Sync-E 
Time and Frequency distribution. PTP distribution is based on both G.8265.1 and G.8275.1.  
Master Clock (Frequency Only with non-GNSS option) 
The diagram below illustrates the implementation of the 1588v2 clock as Grand Master. 
E1
E1
E1 Station 
Clock
E1 Timing 
Source
1588 Master
ETX-205-PTP
TDM
Network
1588 Slave
ETX-205-E1-PTP
1588 Slave
ETX-205-E1-PTP
 
Forwarding 
Note 
On power up, UDP ports 319 (ptp-event) and 320 (ptp-general) are closed, for 
security reasons. When activating G.8265.1 (over Layer-3), these UDP ports 
open, as required, for forwarding of PTP frames. When activating G.8275.1 
(on Layer-2), the UDP ports are not required, and therefore remain closed.  
ETX-2i Devices 
6. Timing and Synchronization 
G.8265.1, G.8275.2 
You need to configure the following for the G.8265.1/G.8275.2 clock entities to function correctly: 
• 
Corresponding SVI 
• 
Corresponding flows 
• 
Corresponding router interface. For the G.8265.1/G.8275.2 boundary clock, the SVI 
corresponding to the router interface must be connected via flow to a bridge port.  
In order to communicate with the remote master of the G.8265.1/G.8275.2 boundary clock, a peer must 
be defined with the remote master IP address; additionally, if the remote master is not in the same 
subnet as ETX-2i, a static route must be configured to define how to reach the remote master. 
G.8275.1  
1588v2 traffic for G.8275.1 PTP ports is transmitted and received by the 1588 entity to/from an Ethernet 
port. 
You need to configure the following for the G.8275.1 clock entities to function correctly: 
• 
Corresponding SVI 
• 
Corresponding PTP port 
• 
Corresponding flows. The traffic from the Ethernet port to the SVI port should be classified as 
untagged. The traffic from the SVI port to the Ethernet port should be classified to match all 
packets. 
• 
For an Ethernet port that is a member in a LAG, flows should be configured differently, using 
port classifier to match EtherType 0x88f7. 
 
Note 
The ingress/egress Ethernet port that is connected via a flow to the 
egress/ingress SVI bound to a PTP clock port, can only be a non-management 
port (and not MNG-ETH 101 or 0/101), as PTP 1588v2 traffic cannot run over 
an out of bound port. 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
Dual Mode Master  
You configure a dual mode master, also called a Distributed PTP Grandmaster (DISTRIBUTED GM®), by 
configuring a G.8265.1 master entity and a G.8275.1 master entity: 
• 
Any configuration change to the dual mode master (Grandmaster) requires that you first 
remove and then add the G.8265.1 master entity. 
• 
The two masters must be configured with different PTP clock domains. 
• 
Each master can support different 1588 message rates. A G.8265.1 master supports message 
rates per slave negotiation, and a G.8275.1 master supports the standard sync rate of 16 PPS.  
Note 
G.8275.2 does not support dual mode master. 
Factory Defaults 
By default, there is no configured master or slave clock.  
Configuring 1588v2 Timing 
Configuring PTP Ports 
You need to configure a PTP port entity for each G.8275.1 clock entity. 
 To configure a PTP port: 
1. Navigate to configure system clock ptp-port 0/1 g.8275-1 port <port>. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Configuring asymmetry 
correction to compensate 
for possible network 
asymmetry  
asymmetry-correction 
<nano-sec> 
Possible values: 0-134217727 
Default: 0 
Binding SVI to port 
[no] bind svi <port-number> 
Specifying which 
destination MAC address 
to use 
mac {01-1b-19-00-00-00 | 
01-80-c2-00-00-0e} 
Layer-2 IEEE 1588 packets have 
destination MAC address 
01-1B-19-00-00-00 or 01-80-C2-00-00-0E 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Setting port priority 
priority <value> 
Priority is used when selecting the best 
source from the PTP ports that are 
provisioned as slaves. 
Possible values: 1-255 
Default: 128 
Provisioning PTP port 
state 
state {master | slave | auto | 
auto-no-slave} 
master – distributes time  
slave – provides time source 
Clearing statistics  
clear-statistics 
Viewing PTP port status 
show status 
 
Viewing PTP port 
statistics 
show statistics running 
 
Administratively enabling 
PTP port 
no shutdown 
Entering shutdown disables the port. 
Configuring the Slave Clock 
This section describes how to configure a G.8265.1 (the default; no need to specify in CLI command), 
G.8275.2, or G.8275.1 slave clock. The slave clock is configured in the clock recovered 0/1 ptp level, 
specifying g.8275-1 or g.8275-2 if you are configuring a G.8275.1 or G.8275.2 slave clock. Additionally, 
for G.8275.1 you need to configure PTP ports. The PTP protocols (g.8265 and g.8275) embed a bit that 
indicates the traceability of the clock source in terms of frequency and time. You can see the value of 
this flag (0/1) in the show status report. 
 
Note 
It is possible to move a PTP slave from one port to another. However, there is 
a timeout (between 6 and 10 seconds) before the new port acquires slave 
clock functionality. 
For examples of configuring G.8265.1, G.8275.2, and G.8275.1 slave clocks, see Examples section below. 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
 To configure the slave clock: 
1. Navigate to configure system clock recovered 0/1 ptp [g.8275-1 | g.8275-2] dscp <0-63>. 
Note 
ETX-2i-10G supports sending the following PTP event messages with 
configurable DSCP value (1-63): 
• 
sync 
• 
delay-request 
• 
delay-response 
All other messages, such as “announce”, are sent under DSCP = 0, which is the 
default. 
2. Perform the required tasks according to the following table. 
 
Task 
Command 
Comments 
Configuring IP address  
ip-address <ip-address> 
Relevant for G.8265.1 and G.8275.2 
Defining master 
recovered clock 
[no] master <id> 
Possible values: 1–2 
See below the procedure for the master 
level. 
Relevant for G.8265.1 and G.8275.2  
Setting minimal clock 
1588 clock quality level 
min-clock-class 
Possible values: 0-255 
0 is the highest clock class value; 255 is 
the lowest (default) 
If the incoming PTP clock class falls below 
the configured minimum quality level 
(i.e., its clock class is a higher value than 
the configured minimum clock class), the 
device issues a clock_class_low alarm. 
Relevant for G.8265.1 only 
Configuring multicast 
IP address 
multicast <ip-address> 
Relevant for G.8265.1 
Defining Telecom Profile 
profile-type 
{telecom-end-to-end | 
telecom-peer-to-peer} 
Relevant for G.8265.1 only  
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Setting precision time 
protocol (PTP) domain  
ptp-domain <number> 
no ptp-domain 
Relevant for G.8265.1, G.8275.1, and 
G.8275.2 
Recommended values:  
4–23 – for 8265.1 
24–43 – for 8275.1 
44-63 – for 8275.2 
Possible values: 0, 4-127 
Default: 4 for 8265.1; 24 for 8275.1; 44 
for 8275.2  
Setting clock recovery 
mode 
recovery-mode { frequency | 
time-frequency | time } 
frequency – frequency only 
time-frequency – time and frequency 
(allowed only in two-way mode; see 
description of delay-respond in master 
level.) 
time – Hybrid mode (allowed only in 
two-way mode; see description of 
delay-respond in master level.) 
Relevant for G.8265.1 only 
Defining whether 
recovered clock is 
revertive  
[no] revertive 
Relevant for G.8265.1 and G.8275.2 
Squelching 1 PPS output 
when clock quality is 
below minimum quality 
level 
[no] squelch-1pps-min-clock-
class 
Relevant for G.8265.1 and G.8275.2 
Defining amount of time 
that previously failed 
clock must be fault free 
in order to be considered 
available 
wait-to-restore <seconds> 
Possible values: 0–720 
Default: 300 
Relevant for G.8265.1 and G.8275.2  
Clearing network metrics 
clear-network-metrics 
{master-to-slave | 
slave-to-master | all} 
See Viewing Clock Recovery Metrics. 
Relevant for G.8265.1, G.8275.1, and 
G.8275.2 
Clearing statistics  
clear-statistics 
Relevant for G.8265.1 and G.8275.2 
Viewing network metrics 
show network-metrics  
See Viewing Clock Recovery Metrics. 
Relevant for G.8265.1, G.8275.1, and 
G.8275.2 
 
show statistics 
Relevant for G.8275.1 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Displaying status 
show status 
Displays the recovered clock status, 
including master/slave 
Relevant for G.8265.1, G.8275.1, and 
G.8275.2 
Administratively enabling 
recovered clock 
no shutdown 
Using shutdown disables the recovered 
clock. 
Relevant for G.8265.1, G.8275.1, and 
G.8275.2 
 
 To configure a peer master for the slave clock (relevant only for G.8265.1 | G.8275-2 slave): 
1. Navigate to configure system clock recovered 0/1 ptp [g.8275-2] master <id>. 
2. Perform the required tasks according to the following table. 
 
Task 
Command 
Comments 
Specifying the requested 
rate for announce 
messages  
announce [rate <rate>] 
[minimum-expected 
<minimum-expected>] 
[grant-period <grant-period>] 
announce-rate, minimum-expected-rate 
possible values: 
For G.8265.1: 16sec | 8sec | 4sec | 2sec 
| 1sec | 500msec | 250msec | 125msec 
Default: 2sec 
For G.8275.2: 1sec | 500msec | 250msec 
| 125msec 
grant-period possible values: 60–1000 
Default 300 
Relevant for G.8265.1 and G.8275.2 
Configuring asymmetry 
correction to compensate 
for possible asymmetry 
between the slave and 
grandmaster 
asymmetry-correction 
<nano-seconds> 
correction-value – asymmetry correction 
value to compensate for possible 
asymmetry between the slave and 
grandmaster 
Possible values: –134217727 to 
+134217727 nanoseconds 
Default: 0 
Relevant for G.8265.1 and G.8275.2 
Configuring clock identity 
clock-identity clock-id <id> 
port [<slot>/]<number>  
If this is not configured, by default a 
standard clock ID is generated. 
Relevant for G.8265.1 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Specifying the requested 
rate for delay-response 
messages 
delay-respond [rate <rate>] 
[minimum-expected 
<minimum-expected>] 
[grant-period <grant-period>] 
Possible values for rate: 16pps, 32pps, 
64pps, 128pps  
Default: 128pps 
Possible values for minimum-expected: 
16pps, 32pps, 64pps, 128pps  
Default: 128pps  
The allowed range for grant-period is 
60–1000 
Default 300 seconds 
The recovered clock works in one-way 
mode if no delay-respond is entered. It 
works in two-way mode if delay-respond 
is entered with parameters.  
Relevant for G.8265.1 and G.8275.2 
Forcing local clock class 
over the value received in 
announce messages 
[no] force-clock-class <class-
number> 
Possible values: 0-255 
Default: no force-clock-class 
Relevant for G.8275.2 
Configuring network type 
network-type { automatic | 
dsl } 
Relevant for G.8265.1 
Specifying the peer 
device that transmits the 
clock signal 
peer <peer-number> 
Relevant for recovered PTP master clock  
Relevant for G.8265.1 and G.8275.2 
Setting priority 
priority <value> 
Relevant for G.8265.1 and G.8275.2 
Setting quality level 
quality-level { prc | ssu-a | 
ssu-b | type1-sec | type1-dnu | 
type1-ssm-based } 
quality-level { prs | stu | st2 | 
tnc | st3e | st3 | smc | dus | 
type2-ssm-based | prov | unk | 
type3-sec | type3-dnu | 
type3-ssm-based } 
The quality level values are according to 
the network type. 
Relevant for G.8265.1 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Specifying the requested 
rate for synchronization 
messages  
sync [rate <rate>] 
[minimum-expected 
<minimum-expected>] 
[grant-period <grant-period>] 
Possible values for rate: 16pps, 32pps, 
64pps, 128pps  
Default: 128pps 
Possible values for minimum-expected: 
16pps, 32pps, 64pps, 128pps  
Default: 128pps  
The allowed range for grant-period is 
60–1000 
Default 300 seconds 
Relevant for G.8265.1 and G.8275.2 
Clearing statistics  
clear-statistics 
Relevant for G.8265.1 and G.8275.2 
Clearing measured 
statistics  
clear-measured-statistics 
Relevant for G.8265.1 and G.8275.2 
Displaying status 
show status 
Relevant for G.8265.1 
Displaying statistics 
show statistics running 
Displaying the 1588v2 statistic counters 
Relevant for G.8265.1 and G.8275.2 
Displaying measured 
statistics  
show measured-statistics 
Displaying the measured rates of the 
received 1588v2 messages 
Relevant for G.8275.2 
Administratively enabling 
master 
no shutdown 
Using shutdown disables the master 
clock. 
Relevant for G.8265.1 and G.8275.2 
Configuring the Master Clock 
The master clock is configured in the clock master 0/1 ptp level, specifying g.8275-1 if you are 
configuring a G.8275.1 master clock; g.8275-2 if you are configuring a G.8275.2 master clock. The default 
is G.8265.1 master clock (no need to specify). Additionally, for G.8275.1, you need to configure PTP 
ports. For examples of configuring G.8265.1, G.8275.2, and G.8275.1 master clocks, see Examples 
section below. 
 
Note 
When configuring a boundary clock, you must configure the slave clock before 
the master clock. 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
 To configure the master clock: 
1. Navigate to configure system clock master 0/1 ptp [g.8275-1 | g.8275-2] dscp <0-63>. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Defining the 1588v2 
message exchange 
mode 
distributed-mode {frequency | 
time-frequency} 
In frequency mode, the master transmits sync 
and announce messages to slaves. 
In time-frequency mode, the master transmits 
sync, announce, and delay response messages 
to slaves. 
Relevant for G.8265.1 only 
Defining the PTP domain 
domain-number <number> 
Recommended values:  
4–23 – for 8265.1 
24–43 – for 8275.1 
44–63 – for 8275.2 
Possible values: 0, 4–127 
Default: 4 for 8265.1; 24 for 8275.1; 44 for 
8275.2 
Note: A domain consists of one or more PTP 
devices (masters or slaves) communicating 
with each other according to PTP 
requirements. For correct distribution of 
timing signals, a 1588v2 master and slaves 
operating with it must belong to the same PTP 
domain. 
Relevant for G.8265.1, G.8275.1 and G.8275.2 
Defining the master IP 
address  
ip-address <address> 
The IP address must be the same as the IP 
address of the dedicated router interface. 
Relevant for G.8265.1 and G.8275.2 
Defining remote slave 
slave <ip> 
See the commands in the slave level below. 
Relevant for G.8265.1 only 
Defining maximum 
number of slaves 
maximum-slaves <number> 
Possible values: 1–128 
Relevant for G.8265.1 and G.8275.2 
Defining priority value 
to be used in Announce 
message 
priority2 <number>  
Relevant for G.8275.1 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Enabling statistic 
collection 
pm-collection 
no pm-collection resets statistic counters and 
stops further collection of performance 
monitoring data. 
Relevant for G.8265.1 only 
Defining Telecom Profile 
profile-type {telecom-end-to-end 
| telecom-peer-to-peer} 
Relevant for G.8265.1 only 
Defining the 
synchronization 
message rate 
sync-rate { 16pps | 32pps | 64pps 
| 128pps } 
All slaves within the domain must use the 
same message rate. 
Default: 128pps 
Relevant for G.8265.1 and G.8275.2  
Selecting Tx clock 
domain 
tx-clock {domain <1>} 
Relevant for G.8265.1 
Displaying status of 
master clock 
show status 
Relevant for G.8265.1, G.8275.1, and G.8275.2 
Enabling the master 
clock 
no shutdown 
Entering shutdown disables the master clock. 
Displaying statistics for 
master clock 
show statistics running 
Relevant for G.8265.1, G.8275.1, and G.8275.2 
Clearing statistics for 
master clock 
clear-statistics 
Relevant for G.8265.1, G.8275.1, and G.8275.2 
Commands in level slave 
 
Relevant for G.8265.1 
Displaying slave status 
show status 
 
Displaying statistics for 
slave clock 
show statistics running 
 
Clearing statistics 
clear-statistics 
 
Viewing Clock Recovery Metrics 
You can display the network performance metrics of the recovered timing. The metrics apply to the 
network packet delay variation (PDV) sequence and are useful for projecting the required system 
bandwidth. The metrics are displayed for the slave clock for the following directions: 
• 
Master to slave (based on Sync messages) 
• 
Slave to master (based on Delay Request messages) 
ETX-2i Devices 
6. Timing and Synchronization 
You can display current metrics, metrics for a selected interval of one hour, or for all intervals. 
 To display the clock recovery metrics: 
1. Navigate to configure system clock recovered 0/1 ptp [g.8275-1 | g.8275-2]. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Viewing current 
metrics 
show network-metrics current 
The metrics for the current interval are 
displayed as shown in Viewing Current 
Metrics. 
Viewing the metrics 
for a selected interval 
show network-metrics interval 
<interval-number> 
Allowed values for interval-num: 1–24 
The metrics for the selected interval are 
displayed as shown in Viewing Metrics for 
Selected Interval. 
Viewing all metrics 
show network-metrics all 
The metrics are displayed as shown in 
Viewing Current Metrics and Viewing 
Metrics for Selected Interval. 
Viewing metrics for all 
intervals 
show network-metrics all-
intervals 
The metrics for all intervals are displayed 
as shown in Viewing Metrics for Selected 
Interval. 
Clearing the metrics 
clear-network-metrics 
{master-to-slave | 
slave-to-master | all} 
master-to-slave – Clear the metrics for 
the direction master->slave.  
slave-to-master – Clear the metrics for 
the direction slave -> master. 
all – Clear all metrics. 
Network Metrics 
Parameter 
Description 
Master ID 
Master clock identification 
Id 
Index of metric observation window (1–22) 
Tau (Sec) 
Metric observation window  
Tdev (ns) 
Time Deviation PDV metric that characterizes PDV spectral noise, as defined in ITU-T 
G.8260 
Note: Tdev values displayed in the network metrics are squares of the actual Tdev 
values; therefore, you must compute the square roots to obtain the correct values. 
ETX-2i Devices 
6. Timing and Synchronization 
Parameter 
Description 
minTdev (ns) 
Minimum Time Deviation PDV metric that characterizes floor delay PDV spectral 
noise, as defined in ITU-T G.8260 
Note: minTdev values displayed in the network metrics are squares of the actual 
minTdev values; therefore, you must compute the square roots to obtain the correct 
values. 
Elapsed Time  
This time counter, in seconds, shows the statistics total information gathering time 
and indicates the statistics reliability (tightness). 
Sampling Time 
Time of sample 
Sampling Date 
Date of sample 
 
Viewing Master Clock Statistics 
 To display the master clock statistics for G.8275-1: 
1. Navigate to configure system clock master 0/1 ptp g.8275-1. 
2. At the config>system>clock>master(0/1)# prompt, enter show statistics running. 
Tx Announce       : 0 
Tx Sync           : 0 
Rx Delay Request  : 0 
Tx Delay Response : 0 
 To display the master clock statistics for G.8275-2: 
1. Navigate to configure system clock master 0/1 ptp [g.8275-2]. 
2. At the config>system>clock>master(0/1)# prompt, enter show statistics running. 
Running 
---------------------------------------------------------------- 
Tx Packets                  : 437352 
Tx Sync Packets             : 217864 
TX Follow Up Packets        : 0 
TX Delay Response Packets   : 217549 
TX Announce Packets         : 1736 
TX Signaling Packets        : 203 
Rx Packets                  : 217752 
RX Signaling Packets        : 203 
RX Delay Request Packets    : 217549 
Discarded Signaling Packets : 0 
ETX-2i Devices 
6. Timing and Synchronization 
 To display the recovered clock’s master clock statistics for G.8265-1 or G.8275-2: 
1. Navigate to configure system clock recovered 0/1 ptp [g.8275-2] master 1. 
2. At the prompt, enter show statistics running. 
Unicast Announce Request            : 0 
Unicast Announce Accept             : 0 
Unicast Announce Reject             : 0 
Unicast Announce Timeout            : 0 
Unicast Sync Request                : 0 
Unicast Sync Accept                 : 0 
Unicast Sync Reject                 : 0 
Unicast Sync Timeout                : 0 
Unicast Delay Respond Request       : 0 
Unicast Delay Respond Accept        : 0 
Unicast Delay Respond Reject        : 0 
Unicast Delay Respond Timeout       : 0 
Rx Unicast Sync Miss Ordered        : 0 
No Sync Total Elapsed Time          : 0 
No Sync Elapsed Time                : 0 
No Announce Total Elapsed Time      : 0 
No Announce Elapsed Time            : 0 
No Delay Respond Total Elapsed Time : 0 
No Delay Respond Elapsed Time       : 0 
Rx Sync Packets                     : 0 
Rx Sync Lost                        : 0 
Rx Delay Respond Packets            : 0 
Examples 
Configuring a Slave Clock (G.8265.1) 
 To configure a G.8265.1 slave clock: 
exit all 
config port  
            svi 1  
                no shutdown  
            exit all 
 
configure qos policer-profile policer1  
 bandwidth cir 1000 cbs 32000 eir 0 ebs 0  
 exit all 
  
 
 
ETX-2i Devices 
6. Timing and Synchronization 
config flows  
            classifier-profile "Router_All" match-any  
                match all  
            exit 
            classifier-profile "Router_Untagged" match-any  
                match untagged  
            exit 
 
            flow "Router_In"  
                classifier "Router_Untagged" 
                policer profile policer1 
                ingress-port ethernet 0/1  
                egress-port svi 1 queue 1  
                no shutdown  
            exit 
            flow "Router_Out"  
                classifier "Router_All" 
                policer profile policer1 
                ingress-port svi 1  
                egress-port ethernet 0/1 queue 0 block 0/1  
                no shutdown  
            exit all 
 
config router 1  
            interface 1  
                address 172.18.141.15/24  
                bind svi 1  
                no management-access  
                no shutdown  
            exit 
                static-route 172.17.171.0/24 address 172.18.141.1 metric 1 
        exit 
 
        peer 1 ip 172.17.171.158 
 
        exit all  
 
configure  
        system  
        clock 
        domain  1 
        source  1  recovered  0/1 
            priority  1 
            quality-level  ssm-based 
            wait-to-restore  0 
            clear-wait-to-restore 
        exit 
    exit 
 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
    recovered  0/1  ptp 
        wait-to-restore  0 
        master  1 
            peer  1 
            priority 1 
            sync grant-period 60 
            announce grant-period 60 
            delay-respond grant-period 60 
            quality-level type1-ssm-based 
            no shutdown 
            exit 
        
        no shutdown 
    exit 
Viewing Slave Clock Information 
 To display recovered clock information: 
ETX-2i# configure system clock recovered 0/1 ptp 
ETX-2i>config>system>clock>recovered(0/1/ptp)# info d 
    multicast 0.0.0.0 
    no revertive 
    wait-to-restore 0 
    no ip-address 
    ptp-domain 4 
    recovery-mode time-frequency 
    master 1 
        clock-identity clock-id ffffffffffffffff port ffff 
        priority 1 
        network-type automatic 
        peer 1 
        sync rate 64pps minimum-expected 64pps grant-period 300 
        announce rate 2sec minimum-expected 2sec grant-period 300 
        delay-respond rate 64pps minimum-expected 64pps grant-period 300 
        quality-level type1-ssm-based 
        no shutdown 
    exit 
    no shutdown 
Viewing Slave Clock Status 
 To display recovered clock status: 
ETX-2i# configure system clock recovered 0/1 ptp 
ETX-2i>config>system>clock>recovered(0/1/ptp)# show status 
Clock State:  Frequency         : Not Applicable       Time        : Not Applicable 
Indicated QL                    :                                                  
Clock Identity                  : 1      
ETX-2i Devices 
6. Timing and Synchronization 
Active Master                   : 1                    Ip Address                                             
Traceable Frequency Flag        : 0 
Traceable Time Flag             : 0 
 
Master Num                         : 1 
IP 
PTSF                               : NACT 
Clock Identity                     : FFFFFFFFFFFFFFFF 
Received QL                        : 
Granted Sync Rate (pps)            : 
Granted  Sync Period (sec)         : 0 
Granted Announce Rate              : 
Granted  Announce Period (sec)     : 0 
Granted Delay Respond Rate (pps)   : 
Granted Delay Respond Period (sec) : 0 
Configuring the Slave Clock (G.8275.1)  
 To configure a G.8275.1 slave clock: 
• 
Clock sources: Ethernet port 0/1 and Ethernet port 0/4 
• 
Flows between: 
 
Ethernet port 0/1 and SVI 1 
 
Ethernet port 0/4 and SVI 4 
• 
PTP ports: 
 
Port 1 bound to SVI 1 
 
Port 4 bound to SVI 4 
#****************Configure SVIs 
exit all 
configure port svi 1 
      no shutdown 
      exit 
    svi 4 
      no shutdown 
      exit 
 
#**************Configure L2CP profile for SSM and Ethernet ports 
    l2cp-profile SSM 
      mac 0x02 peer 
      exit 
 
    ethernet 0/1 
      l2cp profile SSM 
      tx-ssm 
      exit 
 
ETX-2i Devices 
6. Timing and Synchronization 
    ethernet 0/4 
      l2cp profile SSM 
      tx-ssm 
      exit 
    exit 
 
#****************Configure classifier profiles 
  flows 
    classifier-profile all match-any match all 
    classifier-profile untagged match-any match untagged 
 
#****************Configure flows 
    flow eth1_svi1 
      classifier untagged 
      ingress-port ethernet 0/1 
      egress-port svi 1 
      no shutdown 
      exit 
    flow svi1_eth1 
      classifier all 
      ingress-port svi 1 
      egress-port ethernet 0/1 queue 1 block 0/1 
      no shutdown 
      exit 
 
    flow eth4_svi4 
      classifier untagged 
      ingress-port ethernet 0/4 
      egress-port svi 4 
      no shutdown 
      exit 
    flow svi4_eth4 
      classifier all 
      ingress-port svi 4 
      egress-port ethernet 0/4 queue 4 block 0/1 
      no shutdown 
      exit 
    exit 
#****************Configure PTP ports 
  system clock ptp-port 0/1 g.8275-1 
    port 1 
      bind svi 1 
      no shutdown 
      exit 
    port 4 
      bind svi 4   
      no shutdown 
      exit 
    exit 
 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
#****************Configure slave clock 
  recovered 0/1 ptp g.8275-1 
    no shutdown 
    exit 
 
#**************** Configure clock sources 
  domain 1 
    source 1 rx-port ethernet 0/1 
      quality-level ssm-based 
      priority 1 
      wait-to-restore 0 
      clear 
      exit 
 
    source 2 rx-port ethernet 0/4 
      quality-level ssm-based 
      priority 2 
      wait-to-restore 0 
      clear 
exit all 
save 
Configuring the Slave Clock (G.8275.2)  
config 
    peer 1 ip 15.88.111.12 
   system 
        name "slave" 
        clock 
            recovered 0/1 ptp g.8275-2 
                wait-to-restore 0 
                ip-address 15.88.111.88 
                ptp-domain 44 
                master 1 
                    priority 1 
                    peer 1 
#        sync rate 64pps minimum-expected 64pps grant-period 300 
#        delay-respond rate 64pps minimum-expected 64pps grant-period 300 
                    announce rate 1sec minimum-expected 1sec 
                    asymmetry-correction 0 
                    no shutdown 
                exit 
                no shutdown 
            exit 
        exit 
    exit 
    port 
        svi 1 no shutdown 
    exit 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
    flows 
        classifier-profile "untagged" match-any 
            match untagged 
        exit 
        classifier-profile "all" match-any 
            match all 
        exit 
  
        flow "1_svi1" 
            classifier "untagged" 
            policer profile "Policer1" 
            ingress-port ethernet 1 
            egress-port svi 1 
            no shutdown 
        exit 
        flow "svi1_1" 
            classifier "all" 
            policer profile "Policer1" 
            ingress-port svi 1 
            egress-port ethernet 1 queue 0 block 0/1 
            no shutdown 
        exit 
    exit 
    router 1 
        name "Router#1" 
        interface 1 
            address 15.88.111.88/24 
            bind svi 1 
            no management-access 
            dhcp-client 
                client-id mac 
            exit 
            no shutdown 
        exit 
    exit  
Configuring a Boundary Clock (G.8265.1) 
 To configure a boundary clock with G.8265.1 slave and master: 
#**************************** Configure slave clock ************ 
exit all 
configure 
          system   
              clock 
                  recovered 0/1 ptp 
                      no ptp-domain 
                      master 1 
                          priority 0 
                          peer 1   
                          sync-rate 128pps 
ETX-2i Devices 
6. Timing and Synchronization 
                          delay-respond 128pps 
                          no shutdown 
                      exit 
                      no shutdown 
                  exit  
 
#************************* Configure master clock ************** 
                  master 0/1 ptp 
                      ip-address 172.17.163.140 
                      domain-number 0 
                      sync-rate 128pps 
                      no shutdown 
                  exit all 
 
#************************* Save configuration ****************** 
save 
Configuring a Boundary Clock (G.8275.1) 
 To configure a boundary clock with G.8275.1 slave and master: 
• 
Clock source: Ethernet port 0/1  
• 
Flows between: 
 
Ethernet port 0/1 and SVI 2 
 
Ethernet port 0/3 and SVI 4 
 
Ethernet port 0/5 and SVI 6 
• 
PTP ports: 
 
Port 3 bound to SVI 2 
 
Port 5 bound to SVI 4 
 
Port 7 bound to SVI 6 
#****************Configure SVIs 
exit all 
configure port svi 2 
      no shutdown 
      exit 
    svi 4 
      no shutdown 
      exit 
    svi 6 
      no shutdown 
      exit 
 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
#**************Configure L2CP profile for SSM and Ethernet ports 
    l2cp-profile SSM 
      mac 0x02 peer 
      exit 
    ethernet 0/1 
      l2cp profile SSM 
      tx-ssm 
      exit 
    ethernet 0/3 
      tx-ssm 
      exit 
    ethernet 0/5 
      tx-ssm 
      exit  
    exit 
 
#****************Configure classifier profiles 
  flows 
    classifier-profile all match-any match all 
    classifier-profile untagged match-any match untagged 
 
#****************Configure flows 
    flow eth1_svi2 
      classifier untagged 
      ingress-port ethernet 0/1 
      egress-port svi 2 
      no shutdown 
      exit 
    flow svi2_eth1 
      classifier all 
      ingress-port svi 2 
      egress-port ethernet 0/1 queue 1 block 0/1 
      no shutdown 
      exit 
 
    flow eth3_svi4 
      classifier untagged 
      ingress-port ethernet 0/3 
      egress-port svi 4 
      no shutdown 
      exit 
    flow svi4_eth3 
      classifier all 
      ingress-port svi 4 
      egress-port ethernet 0/3 queue 3 block 0/1 
      no shutdown 
      exit 
 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
    flow eth5_svi6 
      classifier untagged 
      ingress-port ethernet 0/5 
      egress-port svi 6 
      no shutdown 
      exit 
    flow svi6_eth5 
      classifier all 
      ingress-port svi 6 
      egress-port ethernet 0/5 queue 5 block 0/1 
      no shutdown 
      exit 
    exit 
 
#****************Configure PTP ports 
  system clock ptp-port 0/1 g.8275-1 
    port 3 
      bind svi 2 
      no shutdown 
      exit 
    port 5 
      bind svi 4 
      state master 
      no shutdown 
      exit 
    port 7 
      bind svi 6 
      state master 
      no shutdown 
      exit 
    exit 
 
#****************Configure slave clock 
  recovered 0/1 ptp g.8275-1 
    no shutdown 
    exit 
 
#****************Configure master clock 
  master 0/1 ptp g.8275-1 
    no shutdown 
    exit 
 
#**************** Configure clock source 
  domain 1 
    source 1 rx-port ethernet 0/1 
      quality-level ssm-based 
      priority 1 
      wait-to-restore 0 
      clear 
      exit all 
save 
ETX-2i Devices 
6. Timing and Synchronization 
Configuring a Boundary Clock (G.8275.2) 
 To configure a boundary clock with G.8275.2 slave and master: 
config 
    peer 1 ip 15.88.111.11 
    peer 2 ip 15.88.111.12 
    system 
        name "BC" 
        clock 
            recovered 0/1 ptp g.8275-2 
                wait-to-restore 0 
                ip-address 15.88.111.99 
                ptp-domain 44 
 
                master 1 
                    priority 1 
                    peer 1 
                    announce rate 1sec minimum-expected 1sec 
                    asymmetry-correction 0 
                    no shutdown 
                exit 
 
                master 2 
                    priority 2 
                    peer 2 
                    announce rate 1sec minimum-expected 1sec 
                    asymmetry-correction 0 
                    no shutdown 
                exit 
 
                no shutdown 
            exit 
 
            master 0/1 ptp g.8275-2 
                ip-address 15.88.111.99 
                domain-number 55 
                maximum-slaves 4 
                no shutdown 
            exit 
        exit 
    exit 
 
    port 
        svi 1 no shutdown 
    exit 
    bridge 1 
        name "BRIDGE 1" 
        port 1 
            no shutdown 
        exit 
        port 2 
ETX-2i Devices 
6. Timing and Synchronization 
            no shutdown 
        exit 
        port 3 
            no shutdown 
        exit 
        vlan 100 
        exit 
    exit 
    flows 
        classifier-profile "untagged" match-any 
            match untagged 
        exit 
        classifier-profile "all" match-any 
            match all 
        exit 
        classifier-profile "v100" match-any 
            match vlan 100 
        exit 
 
#1588 packets from/to master  
        flow "to_master" 
            classifier "untagged" 
            policer profile "Policer1" 
            vlan-tag push vlan 100 p-bit fixed 0 
            ingress-port ethernet 0/1 
            egress-port bridge-port 1 1 
            reverse-direction block 0/1 
            no shutdown 
        exit 
        flow "svi_out" 
            classifier "all" 
            policer profile "Policer1" 
            vlan-tag push vlan 100 p-bit fixed 0 
            ingress-port svi 1 
            egress-port bridge-port 1 2 
            reverse-direction 
            no shutdown 
        exit 
#1588 packets from/to slave 
        flow "to_slave" 
            classifier "untagged" 
            policer profile "Policer1" 
            vlan-tag push vlan 100 p-bit fixed 0 
            ingress-port ethernet 0/3 
            egress-port bridge-port 1 3 
            reverse-direction block 0/1 
            no shutdown 
        exit 
    exit 
 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
    router 1 
        name "Router#1" 
        interface 1 
            address 15.88.111.99/24 
            bind svi 1 
            no management-access 
            dhcp-client 
                client-id mac 
            exit 
            no shutdown 
        exit 
    exit 
Configuring a Boundary Clock (Dual Mode) 
 To configure a boundary clock with G.8265.1 slave, and dual mode master: 
• 
G8265.1 slave: 
 
PTP domain 4 
 
SVI port 1 
 
VLAN 2385 
 
Flows between Ethernet port 0/1 and bridge port 1 
 
Flows between SVI port 1 and bridge port 2 
 
Remote master IP address 172.19.171.100 
• 
G8265.1 master: 
 
PTP domain 4 
 
IP address 172.19.171.101 
 
Flows between Ethernet ports 0/2, 0/4, 0/6 and bridge ports 3, 5, 7 
• 
Router interface 1 (used for both G8265.1 slave and G8265.1 master):  
 
IP address 172.19.171.101 
 
SVI port 1 
• 
G8275.1 master: 
 
PTP domain 5 
 
Flows between Ethernet ports 0/3–0/5 and SVI ports 3–5 
 
PTP ports 3–5 bound to SVI ports 3–5 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
#**************** Configure SVI ports 
exit all 
config port  
    svi 1  
      no shutdown  
    exit  
    svi 3  
      no shutdown  
    exit  
    svi 4  
      no shutdown  
    exit  
    svi 5  
      no shutdown  
    exit  
  exit  
 
#**************** Configure classifier profiles 
    flows  
      classifier-profile all match-any match all  
      classifier-profile untagged match-any match untagged  
      classifier-profile v2385 match-any match vlan 2385 
 
#**************** Configure flows for G.8265.1 slave 
      flow 8265_in  
        classifier v2385 
        ingress-port bridge-port 1 1  
        reverse-direction block 1/1  
        no shutdown  
       exit 
       flow 8265_out  
         classifier all 
         ingress-port svi 1  
         egress-port bridge-port 1 2 
         reverse-direction  
         no shutdown  
        exit  
 
#**************** Configure flows for G.8265.1 master 
        flow "in1"  
          classifier "v2385"  
          ingress-port ethernet 0/2  
          egress-port bridge-port 1 3  
          reverse-direction block 1/1  
          no shutdown  
        exit 
        flow "in4"  
          classifier "v2385"  
          ingress-port ethernet 0/4  
          egress-port bridge-port 1 5  
          reverse-direction block 1/1  
          no shutdown  
ETX-2i Devices 
6. Timing and Synchronization 
        exit 
        flow "in6"  
          classifier "v2385"  
          ingress-port ethernet 0/6  
          egress-port bridge-port 1 7  
          reverse-direction block 1/1  
          no shutdown  
        exit 
 
#**************** Configure flows for G.8275.1 master 
            flow "eth3_svi3"  
                classifier "untagged"  
                ingress-port ethernet 0/3  
                egress-port svi 3  
                no shutdown  
            exit 
            flow "svi3_eth3"  
                classifier "all"  
                ingress-port svi 3  
                egress-port ethernet 0/3 queue 3 block 0/1  
                no shutdown  
            exit 
            flow "eth4_svi4"  
                classifier "untagged"  
                ingress-color green  
                ingress-port ethernet 0/4  
                egress-port svi 4  
                no shutdown  
            exit 
            flow "svi4_eth4"  
                classifier "all"  
                ingress-port svi 4  
                egress-port ethernet 0/4 queue 4 block 0/1  
                no shutdown  
            exit 
            flow "eth5_svi5"  
                classifier "untagged"  
                ingress-port ethernet 0/5  
                egress-port svi 5  
                no shutdown  
            exit 
            flow "svi5_eth5"  
                classifier "all"  
                ingress-port svi 5  
                egress-port ethernet 0/5 queue 5 block 0/1  
                no shutdown  
            exit 
 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
#******* Configure router interface for G8265.1 slave and master 
config router 1  
            interface 1  
                address 172.19.171.101/24  
                bind svi 1  
                no management-access  
                no shutdown  
            exit 
        exit 
 
#*********** Configure peer for remote master, for G8265.1 slave 
        peer 1 172.19.171.100 
        exit  
 
#**************** Configure clock source 
    system clock domain 1  
      source 1 recovered 0/1  
         priority 1  
         quality-level ssm-based  
         wait-to-restore 0  
         exit 
       exit 
 
#**************** Configure PTP ports 
       ptp-port 0/1 g.8275-1  
          port 3  
             bind svi 3  
             state master  
             no shutdown  
          exit 
          port 4  
             bind svi 4  
             state master  
             no shutdown  
          exit 
          port 5  
             bind svi 5  
             state master  
             no shutdown  
          exit 
       exit 
 
#**************** Configure G8265.1 slave 
    recovered  0/1  ptp 
        ptp-domain 4 
        wait-to-restore  0 
        no shutdown 
        master  1 
            peer  1 
            priority 1 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
            network-type automatic 
            no shutdown 
        exit 
     exit 
#**************** Configure G8265.1 master 
        master 0/1 ptp  
          ip-address 172.19.171.101  
          domain-number 4  
          tx-clock domain 1  
          no shutdown  
        exit 
 
#**************** Configure G8275.1 master 
       master 0/1 ptp g.8275-1  
         domain-number 5  
         no shutdown  
    exit all 
save 
Configuring G.8275.1 over LAG  
Boundary Clock LAG  
config 
    system 
        name "8275.1-BC-LAG1" 
        clock 
            recovered 0/1 ptp g.8275-1 
                no shutdown 
            exit 
            master 0/1 ptp g.8275-1 
                domain-number 5 
                no shutdown 
            exit 
            domain 1 
                force-t4-as-t0 
                source 1 recovered 0/1 
                    priority 1 
                    wait-to-restore 0 
                exit 
            exit 
        exit 
    exit 
 
    port 
        l2cp-profile "L2cpDefaultProfile" 
            mac "01-80-c2-00-00-02" peer 
        exit 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
        ethernet 0/5 
            classifier 
                match ether-type 0x88f7 sequence 10 to-flow "ptp_to_svi1" 
            exit 
        exit 
        svi 1 no shutdown 
        svi 28 no shutdown 
        lag 1 
            bind ethernet 0/5 
            bind ethernet 0/6 
            lacp tx-activity active tx-speed fast 
            anchor-port ethernet 0/5 
            no shutdown 
        exit 
    exit 
    flows 
        classifier-profile "all" match-any 
            match all 
        exit 
        classifier-profile "untagged" match-any 
            match untagged 
        exit 
 
        flow "eth28_svi28" 
            classifier "untagged" 
            policer profile "Policer1" 
            ingress-port ethernet 0/28 
            egress-port svi 28 
            no shutdown 
        exit 
        flow "svi28_eth28" 
            classifier "all" 
            policer profile "Policer1" 
            ingress-port svi 28 
            egress-port ethernet 0/28 queue 1 block 0/1 
            no shutdown 
        exit 
 
        flow "ptp_to_svi1" port-classifier 
            policer profile "Policer1" 
            egress-port svi 1 
            no shutdown 
        exit 
        flow "svi1_to_ptp" 
            classifier "all" 
            policer profile "Policer1" 
            ingress-port svi 1 
            egress-port ethernet 0/5 queue 1 block 0/1 
            no shutdown 
        exit 
    exit 
 
ETX-2i Devices 
6. Timing and Synchronization 
   system 
        clock 
            ptp-port 0/1 g.8275-1 
                port 1 
                    bind svi 1 
                    state master 
                    no shutdown 
                exit 
                port 28 
                    bind svi 28 
                    no shutdown 
                exit 
            exit 
        exit 
    exit 
Slave Clock LAG 
config 
    system 
        name "8275.1-SL-LAG1" 
        clock 
            recovered 0/1 ptp g.8275-1 
                ptp-domain 5 
                no shutdown 
            exit 
            domain 1 
                force-t4-as-t0 
                source 1 recovered 0/1 
                    priority 1 
                    wait-to-restore 0 
                exit 
            exit 
        exit 
    exit 
 
 
 
 
    port 
        l2cp-profile "L2cpDefaultProfile" 
            mac "01-80-c2-00-00-02" peer 
        exit 
        ethernet 0/5 
            classifier 
                match ether-type 0x88f7 sequence 10 to-flow "ptp_to_svi1" 
            exit 
        exit 
        svi 1 no shutdown 
 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
        lag 1 
            bind ethernet 0/5 
            bind ethernet 0/6 
            lacp tx-activity passive tx-speed fast 
            anchor-port ethernet 0/5 
            no shutdown 
        exit 
    exit 
    flows 
        classifier-profile "all" match-any 
            match all 
        exit 
        classifier-profile "untagged" match-any 
            match untagged 
        exit 
 
        flow "ptp_to_svi1" port-classifier 
            policer profile "Policer1" 
            egress-port svi 1 
            no shutdown 
        exit 
        flow "svi1_to_ptp" 
            classifier "all" 
            policer profile "Policer1" 
            ingress-port svi 1 
            egress-port ethernet 0/5 queue 1 block 0/1 
            no shutdown 
        exit 
    exit 
 
   system 
        clock 
            ptp-port 0/1 g.8275-1 
                port 1 
                    bind svi 1 
                    no shutdown 
                exit 
            exit 
        exit 
    exit 
Viewing Current Metrics 
ETX-2i>config>system>clock>recovered(0/1/ptp)# show network-metrics current 
Current 
----------------------------------------------------------------------------- 
Master ID : 1 
 
Master To Slave 
----------------------------------------------------------------------------- 
Id  Tau       Tdev      minTdev   Elasped Time 
    (Sec)     (ns)      (ns) 
ETX-2i Devices 
6. Timing and Synchronization 
----------------------------------------------------------------------------- 
1   1         100       501       00:33:29 
2   2         55        452       00:33:28 
3   4         41        400       00:33:28 
4   8         39        400       00:33:29 
5   12        71        400       00:33:25 
6   16        121       438       00:33:21 
7   24        171       411       00:33:14 
8   32        231       520       00:33:06 
9   48        180       484       00:32:51 
10  64        162       593       00:33:07 
11  96        63        674       00:32:06 
12  128       115       402       00:32:07 
13  196       146       547       00:32:41 
14  256       138       673       00:29:57 
15  384       132       879       00:32:07 
16  512       96        400       00:25:46 
17  768       172       400       01:04:00 
18  1024      116       400       00:51:14 
19  2048      1         1         00:34:14 
20  4096      1         1         00:00:18 
21  8192      1         1         00:00:19 
22  32768     1         1         00:00:19 
Slave To Master 
----------------------------------------------------------------------------- 
Id  Tau       Tdev      minTdev   Elasped Time 
    (Sec)     (ns)      (ns) 
----------------------------------------------------------------------------- 
1   1         128       449       00:33:30 
2   2         63        400       00:33:30 
3   4         45        400       00:33:28 
4   8         54        406       00:33:29 
5   12        75        400       00:33:25 
6   16        122       420       00:33:21 
7   24        187       406       00:33:14 
8   32        233       428       00:33:06 
9   48        189       477       00:32:51 
10  64        158       400       00:33:07 
11  96        64        400       00:32:06 
12  128       122       400       00:32:07 
13  196       135       400       00:32:41 
14  256       130       569       00:29:57 
15  384       129       400       00:32:07 
16  512       107       400       00:25:46 
17  768       103       400       00:51:13 
18  1024      25        400       00:51:13 
19  2048      1         1         00:34:09 
20  4096      1         1         00:00:18 
21  8192      1         1         00:00:19 
22  32768     1         1         00:00:19 
ETX-2i Devices 
6. Timing and Synchronization 
Viewing Metrics for Selected Interval 
ETX-2i>config>system>clock>recovered(0/1/ptp)# show network-metrics interval 1 
Interval Number : 1 
Master ID       : 1 
Sampling Time   : 08:00:00 
Sampling Date   : 26-07-2012 
 
Master To Slave 
----------------------------------------------------------------------------- 
Id  Tau       Tdev      minTdev   Elapsed Time 
    (Sec)     (ns)      (ns) 
----------------------------------------------------------------------------- 
1   1         41448968  58527396  00:05:49 
2   2         18079422  28993502  00:05:48 
3   4         5276496   15718937  00:05:48 
4   8         1201367   12813626  00:05:45 
5   12        691645    12206705  00:05:49 
6   16        506413    8053903   00:05:38 
7   24        622610    3623477   00:05:39 
8   32        347378    4017002   00:05:22 
9   48        78378     9761690   00:05:39 
10  64        139133    6660025   00:05:23 
11  96        606       139842    00:04:53 
12  128       1         1         00:04:19 
13  196       1         1         00:03:19 
14  256       1         1         00:04:21 
15  384       1         1         00:00:11 
16  512       1         1         00:00:13 
17  768       1         1         00:00:14 
18  1024      1         1         00:00:15 
19  2048      1         1         00:00:15 
20  4096      1         1         00:00:18 
21  8192      1         1         00:00:19 
22  32768     1         1         00:00:19 
 
Slave To Master 
----------------------------------------------------------------------------- 
Id  Tau       Tdev      minTdev   Elapsed Time 
    (Sec)     (ns)      (ns) 
----------------------------------------------------------------------------- 
1   1         617756    400       00:30:44 
2   2         770042    400       00:30:44 
3   4         344708    400       00:30:44 
4   8         246177    2935      00:30:41 
5   12        226724    65673     00:30:37 
6   16        159360    316373    00:30:41 
7   24        218542    1682603   00:30:27 
8   32        231636    3483920   00:30:27 
9   48        203230    6556856   00:30:29 
10  64        166905    9179698   00:29:55 
11  96        103179    14061712  00:30:29 
12  128       88556     19896568  00:29:55 

## 6.2 Clock Selection  *(p.1189)*

ETX-2i Devices 
6. Timing and Synchronization 
13  196       79678     34140880  00:29:25 
14  256       50201     47704072  00:29:57 
15  384       60187     119676112 00:25:45 
16  512       60686     237447312 00:25:46 
17  768       1         1         00:25:47 
18  1024      1         1         00:17:10 
19  2048      1         1         00:00:15 
20  4096      1         1         00:00:18 
21  8192      1         1         00:00:19 
22  32768     1         1         00:00:19 
6.2 Clock Selection 
This section discusses the clock selection mechanism provided by ETX-2i. Clock selection provides 
synchronization over packet transport networks. 
For a detailed explanation on clock selection and management (CSM), refer to Appendix C. 
Applicability and Scaling 
This feature is applicable to ETX-2i, ETX-2i-B, ETX-2i-10G/4SFPP (full and half 19-inch), ETX-2i-10G-
B/4SFPP (full and half 19-inch), and ETX-2i-10G-B/8SFPP (full and half 19-inch), and ETX-2i-10G-
B/8SFPP/ODU with timing options. It is not applicable to ETX-2i-100G. 
Standards Compliance 
ITU-T G.8261/G.8262-G.8264 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
Factory Defaults 
By default, if a timing card is installed in the unit, a clock domain entry is created with the following 
configuration: 
• 
Synchronization network type 1 
• 
Minimum quality PRC 
• 
Mode auto (clock selection mechanism functions normally) 
• 
No force T4 as T0 
Station Clock 
The EXT CLK (External clock) port located at the left side of the panel is known as the Station Clock (as it 
is commonly used at base stations). Using SyncE or PTP, ETX-2i acquires and follows a clock signal. One 
way to make use of this signal is by connecting to the EXT CLK port and extracting the clock signal as a 
2048kHz clock signal or E1/T1 signal (configurable).  
When a station clock is created, its default configuration is the following (see the task list below for 
explanations of the parameters): 
• 
Tx clock source = system 
• 
Interface type = e1 balanced 
• 
Line code = ami 
• 
Rx sensitivity = short-haul 
• 
no shutdown 
Clock Sources 
When a clock source is created, its default configuration is the following (see the task list below for 
explanations of the parameters): 
• 
priority = 2 
• 
wait-to-restore = five minutes (300 seconds) 
• 
hold-off = 300 milliseconds 
• 
quality-level = ssm-based 
ETX-2i Devices 
6. Timing and Synchronization 
Functional Description 
You can configure a slave (recovered) clock that complies with the IEEE-1588 Precision Time Protocol 
(PTP). You need to configure the clock domain before configuring the recovered clock. 
ETX-2i supports one clock domain with up to two clock sources. The sources can be network/user 
Ethernet ports, PTP recovered clock, station clock.  For ETX-2i with EoPDH AIO module, an Rx clock of a 
single E1 (bound to VCG 5) can also be provided as a source clock to ETX-2i CSM. 
In Synchronous Optical Networking (SONET) and Synchronous Digital Hierarchy (SDH) equipment, the 
communication channel for conveying clock information is SSM. Information provided by SSM quality 
levels helps a node derive timing from the most reliable source and prevent timing loops.  
With Ethernet equipment (that is gradually replacing SONET and SDH equipment in service-provider 
networks), all links and locations are not synchronous, and therefore frequency synchronization is 
required to provide high-quality clock synchronization over Ethernet ports. Synchronous Ethernet 
(SyncE), supported over all device network and user ports, provides the required synchronization at the 
physical level. SyncE provides, through the ESMC channel, the frequency distribution, as it exists in 
SONET and SDH. Operation messages maintain SyncE links and ensure that a node always derives timing 
from the most reliable source. SSM messages are supported and transmitted over ESMC frames at 1 pps 
rate.  
The timing subsystem automatically selects the best timing source to use for synchronization. Each one 
of the Ethernet ports’ recovered clocks can be input to the CSM. 
 
Note 
For ETX-2i with EoPDH AIO module, the ETX­2i CSM system clock can be 
provided to module E1s (provided the E1s are bound to VCG 5). For further 
information, refer to the VCGs section in the Cards and Ports chapter. 
 
 
Clock Domain 
The domain parameters include the synchronization network type and the timing quality level. 
The synchronization network type identifies the type of synchronization network connections and the 
synchronization level. Each synchronization network connection is provided by one or more 
synchronization link connections, each supported by a synchronized PDH trail, SDH multiplex section 
trail, or 802.3 physical media trail.  
The synchronization network types are: 
• 
Option I (Europe)  
• 
Option II (USA) 
ETX-2i Devices 
6. Timing and Synchronization 
You can define the timing quality level of the domain and source, or work without quality level. The 
supported quality levels are according to the synchronization network type, as shown in the following 
tables. The quality levels are shown in order of highest quality level to lowest quality level. 
 
Note 
In order to support the three new Quality Levels ePRTC, PRTC, and PRC, the 
extended QL TLV format as defined in G.8264 should be supported.  
You can set different minimum clock quality levels for SyncE system clock T0 (quality min-level-system) 
and station clock T4 (quality min-level-station). Changing the level of one clock does not change the level 
of the other clock.  
When quality min-level-system is set and the quality of the T0 DPLL source falls below the configured 
minimum level, T0 clock (SEC/EEC) invokes a holdover mechanism, meaning that the system clock 
output goes into holdover state, and issues a system_clock_ql_low alarm. 
Similarly, when quality min-level-station is set and the quality of the station clock falls below the 
configured minimum level, T4 clock invokes a holdover mechanism, meaning that the station clock 
output goes into holdover state, and issues a station_clock_ql_low alarm. 
Option I Quality Levels (Europe) 
Quality 
Level 
Description 
Rank 
ePRTC 
Timing source is Enhanced Primary Reference Time Clock as defined in G.8272.1. 
Highest 
PRTC 
Timing source is Primary Reference Time Clock as defined in G.8272.  
| 
PRC 
Timing source is Primary Reference Clock as defined in Recommendation G.811. 
| 
SSU-A 
Timing source is Type I or V Synchronization Supply Unit (SSU) clock as defined in 
Recommendation G.812. 
| 
SSU-B 
Timing source is Type VI Synchronization Supply Unit (SSU) clock as defined in 
Recommendation G.812. 
| 
eEEC 
Timing source is Enhanced EEC. 
| 
SEC 
Timing source is Synchronous Equipment Clock as defined in Recommendation 
G.813 or G.8262, Option I. 
| 
DNU 
Do Not Use – Do not use this signal for synchronization. 
Lowest 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
Option II Quality Levels (USA) 
Quality 
Level 
Description 
Rank 
ePRTC 
Timing source is Enhanced Primary Reference Time Clock as defined in G.8272.1. 
Highest 
PRTC 
Timing source is Primary Reference Time Clock as defined in G.8272.  
| 
PRS 
Timing source is Primary Reference Source clock as defined in Recommendation 
G.811 
| 
STU 
Synchronization Traceability Unknown – Timing signal does not carry a quality level 
indication of the source. 
| 
ST2 
Timing source is Stratum 2 clock as defined in Recommendation G.812, Type II. 
| 
TNC 
Timing source is Transit Node Clock as defined in Recommendation G.812, Type V. 
| 
ST3E 
Timing source is Stratum 3E clock as defined in Recommendation G.812, Type III. 
| 
ST3 
Timing source is Stratum 3 clock as defined in Recommendation G.812, Type IV. 
| 
SMC 
Timing source is SONET/Ethernet self-timed clock as defined in Recommendation 
G.813 or G.8262, Option II. 
| 
ST4 
Timing source is Stratum 4 free-running clock (applicable only to 1.5 Mbit/s signals). 
| 
PROV 
Provisional by the network operator; default position 
| 
DUS 
Do Not Use – Do not use this signal for synchronization. 
Lowest 
 
Station Clock 
The station clock is an E1/2MHz port that can be used for synchronization.  
Clock Sources 
You can define up to two clock sources for the domain. The sources can be:  
• 
Ethernet ports 
• 
Recovered clock 
• 
Station clock 
• 
E1 Rx clock (for ETX-2i with EoPDH AIO module) 
ETX-2i Devices 
6. Timing and Synchronization 
Note 
• 
If an Ethernet port is defined as a clock source, it must be associated with 
an L2CP profile (flow level or port level) that specifies peer action for MAC 
0x02. It is also recommended to enable the transmitting of SSM messages 
by the port (via tx-ssm), as it may need to transfer clock signals. 
• 
In ETX-2i with EoPDH AIO module, only an E1 port bound to VCG 5 can be 
defined as a clock source. This feature provides redundancy; if the selected 
E1 is inactive, another E1 (active with a valid clock) within VCG 5 is 
automatically selected as the source. 
Configuring Clock Selection 
Configuring the Clock Domain 
 To configure the clock domain: 
1. Navigate to configure system clock domain 1. 
2. At the config>system>clock>domain(1)# prompt, perform the required tasks according to the 
following table. 
Task 
Command 
Comments 
Canceling previously 
issued force or manual 
command 
clear 
 
Clearing statistics for all 
clock sources 
clear-statistics 
 
Forcing selection of a 
particular clock source 
when the sources have 
different quality levels 
force <source-id> 
 
Forcing T4 (station 
clock) timing generator 
to use the same clock 
source as the T0 (system 
clock) generator 
force-t4-as-t0 
Use no-force-t4-as-t0 to 
prevent T4 timing generator 
from using the same clock 
source as the T0 generator. 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Manually selecting a 
particular clock source  
manual <source-id> 
This command may be used 
in the following conditions: 
• No quality is defined for 
the clock domain. 
• The sources have the 
same qualities. 
• The sources have 
different priorities. 
Setting maximum 
frequency deviation  
max-frequency-deviation <value> 
Range is 381–6096, in units 
of PPM*100 (e.g., specifying 
381 sets maximum 
frequency deviation to 
3.81). 
Default: 1524 
When frequency deviation 
of an input clock source 
exceeds the defined 
maximum frequency 
deviation, the clock source 
is declared invalid. 
Setting clock mode 
mode { auto | free-run | force-t0-holdover } 
auto – Clock selection 
mechanism functions 
normally, e.g., the best 
available clock source is 
selected for 
synchronization. 
free-run – Internal oscillator 
is used for synchronization. 
force-t0-holdover – Clock is 
no longer synchronized to 
reference clock source. 
Setting minimum clock 
quality levels for the 
station (T4) and/or 
system (T0) clocks 
Network type 1 (Europe): quality [min-level-station 
<ql1>] [min-level-system <ql1>] 
Network type 2 (USA): quality [min-level-station 
<ql2>] [min-level-system <ql2>] 
no quality 
ql1 – quality level (according 
to network type 1 Europe) 
Possible values: eprtc, prtc, 
prc, ssu-a, ssu-b, eeec, sec, 
dnu  
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
ql2 – quality level (according 
to network type 2 USA) 
Possible values: prs, stu, st2, 
tnc, st3e, st3, smc, st4, dus, 
prov, eprtc, prtc 
no quality removes the 
minimum quality 
parameter. If no minimum 
quality is defined for the 
domain, you cannot 
configure the quality level 
for the sources. A clock 
source with a quality level 
lower than the defined 
minimum quality is ignored 
by the clock selection 
mechanism. 
Note:  
• The quality values are 
according to the 
synchronization network 
type defined for the 
domain. 
• The system minimum 
clock quality level and 
station minimum clock 
quality level are 
independent of each 
other. 
Displaying domain 
status 
show status 
See  
Viewing Clock Domain 
Status. 
Adding clock source  
source <src-id> recovered [<slot>/]<port> 
source <src-id> rx-port {ethernet [<slot>/]<port>|e1 
<slot>/<port>} 
source <src-id> station [<slot>/]<port> 
Entering no source <src-id> 
deletes the source. 
For detailed information on 
adding clock sources, see 
Configuring the Clock 
Sources. 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Note: 
• Only an E1 port bound 
to VCG 5 can be used as 
an Rx port in CSM. 
• Only one E1 from the 
EoPDH AIO module can 
be used as a source. 
However, if the selected 
E1 is inactive, the system 
automatically finds the 
next active E1 in VCG 5, 
and uses it as a source 
(redundancy). 
Setting synchronization 
network type 
sync -network -type { 1 | 2} 
Type 1 – Europe  
Type 2 – USA 
Note: When you change the 
synchronization network 
type, you have to redefine 
the clock sources. 
Configuring the Station Clock 
 To connect ETX-2i to an unbalanced clock source: 
1. Connect the RJ-45 connector of the adapter cable to the station clock port. 
2. Connect the external clock source to the receiving BNC connector of the adapter cable. 
3. Connect the transmitting BNC connector of the adapter cable to the equipment that should 
receive the clock signal. 
 To configure the station clock: 
1. Navigate to configure system clock station 0/1. 
The config>system>clock>station(0/1)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Setting interface type 
interface-type e1 [{ balanced | unbalanced }] 
interface-type 2mhz [{ balanced | unbalanced }] 
If you specify e1 or 2mhz 
and do not specify balanced 
or unbalanced, by default 
the interface is set as 
balanced. 
Note: You can configure the 
interface type only if the 
station clock is 
administratively disabled 
(shutdown). 
Setting line code 
line-code { ami | hdb3 } 
ami – Referred to as 
Alternate Mark Inversion 
because a 1 is referred to as 
a mark and a 0 as a space. 
hdb3 – Referred to as High 
Density Bipolar of order 3, 
this code is a 
telecommunication line 
code based on AMI and 
used in E1 lines. 
Note: You can configure the 
line code only if the 
interface type is E1 and the 
station clock is 
administratively disabled 
(shutdown). 
Setting receiver 
sensitivity to adjust the 
signal’s capability to 
reach destinations close 
by or farther away 
rx-sensitivity { short-haul | long-haul } 
 
Setting clock timing to 
be based on internal 
system or external 
source 
tx-clock-source { system | loopback-timing } 
system – timing based on 
internal system  
loopback-timing – timing 
based on E1/2MHz external 
source 
Administratively 
enabling station clock 
no shutdown 
Using shutdown disables 
the station clock. 
ETX-2i Devices 
6. Timing and Synchronization 
Configuring the Clock Sources 
 To add a clock source: 
1. Navigate to configure system clock domain 1. 
2. Type one of the following, according to the type of clock source: 
source <1–2> rx-port ethernet [<slot>/]<port> 
source <1–2> rx-port e1 <slot>/<port> 
source 1 recovered [<slot>/]<port> 
source <1–2> station [<slot>/]<port> 
The clock source is created and the config>system>clock>domain(1)>source(<1–2>)$ prompt is 
displayed. 
3. Perform the required tasks according to the following table. 
 To configure a clock source that has already been created: 
1. Navigate to configure system clock domain 1. 
The config>system>clock>domain(1)# prompt is displayed. 
2. Type source <1–2> to select the source to configure. 
The config>system>clock>domain(1)>source(<1–2>)# prompt is displayed. 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Resetting the running 
wait-to-restore timer of a 
clock source.   
clear-wait-to-restore 
This one-time reset of the 
running WTR is useful if a 
timing source fault is 
cleared, and you want the 
source to be immediately 
available. 
Defining amount of time 
(in milliseconds) that signal 
failure must be active 
before it is transmitted  
hold-off <milliseconds> 
Possible values: 300–1800 
Default: 300 milliseconds 
Setting priority 
priority <num> 
Possible values: 1–2 
Note: Priority 1 is the 
highest. 
no priority excludes the 
clock source. 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Setting quality level of the 
clock source 
CSM Network type 1 (Europe): quality-level 
{ eprtc | prtc | prc | ssu-a | ssu-b | eeec | sec | 
dnu | ssm-based } 
CSM Network type 2 (USA):quality-level { prs | stu 
| st2 | tnc | st3e | st3 | smc | st4 | dus | 
ssm-based | prov | eprtc | prtc } 
 
Note:  
• If no minimum quality 
is defined for the 
domain, this command 
is not available. 
• The quality level values 
are according to the 
synchronization 
network type defined 
for the domain 
• The quality level 
ssm-based indicates 
the quality level is 
based on SSM 
messages. This option 
requires that if an 
Ethernet port is being 
used as the clock 
source, the port is 
associated with an L2CP 
profile that specifies 
peer action for MAC 
0x02. 
Defining amount of time 
(in seconds) that a 
previously failed 
synchronization source 
must be fault free in order 
to be considered available  
wait-to-restore <seconds> 
Possible values: 0–720 
Default: 300 seconds 
Displaying status 
show status 
See Viewing Clock Source 
Status. 
Displaying statistics 
show statistics 
See Viewing Clock Source 
Statistics. 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
Viewing Clock Domain Status 
 To display the clock domain status: 
1. Navigate to configure system clock domain 1. 
2. At the prompt, enter: 
show status 
A report is generated with the fields described in the following table.  
Field 
Description 
System Clock Source 
Tx quality transmitted over the ESMC packets  
State 
State of the system clock source 
Possible values: Freerun, Locked, Unlocked, Holdover 
Quality 
CSM quality mode  
Station Out Clock 
Source 
 
State 
State of the station out clock source 
Possible values: Locked, Unlocked 
Force Switch 
Current Force Switch state of the clock domain 
Possible values: Active, Inactive 
Manual Switch 
Current Manual Switch state of the clock domain 
Possible values: Active, Inactive 
T0 Offset in PPB 
The selected clock (T0) frequency offset in PPB 
Possible values: -262,000 to 262,000 
Viewing Clock Source Status 
You can display the Ethernet clock source status. 
 To display the Ethernet clock source status: 
1. Navigate to configure system clock domain 1 source <src-id>. 
The following prompt is displayed: config>system>clock>domain(1)>source(<src-id>)#. 
2. Enter: 
show status. 
ETX-2i Devices 
6. Timing and Synchronization 
A report is generated with the fields described in the following table. 
Field 
Description 
Status 
Status can be one of the following: 
• OK – either ESMC received and OK or QL is configured to a predefined 
value but not ssm-based. 
• Physical Fail – such as LOS or port shutdown 
• ESMC Fail – if QL is configured to ‘ssm-based’ and five consecutive 
seconds passed without Rx of ESMC packets, if the SSM is learned by 
ESMC messages and it's not forced QL 
• Monitoring Fail – SEC HW found a problem with the clock deviation. 
Tx Quality 
Tx quality transmitted over the ESMC packets  
Rx Quality 
Rx quality received from the ESMC packets  
ESMC State 
• Locked – ESMC messages received. 
• Unlocked – ESMC messages not received. 
WTR State 
• Active 
• Inactive 
Viewing Clock Source Statistics 
Ethernet Synchronization Messaging Channel (ESMC) relays the SSM code representing the clock quality 
level.  
You can display the Ethernet Synchronization Messaging Channel (ESMC) statistics for the clock sources. 
 To display the ESMC statistics for a clock source: 
1. Navigate to configure system clock domain 1 source <src-id>. 
The following prompt is displayed: config>system>clock>domain(1)>source(<src-id>)#. 
2. Enter: 
show statistics 
The ESMC statistics are displayed with the fields described in the following table. 
Field 
Description 
ESMC Failure Counter 
ESMC protocol disconnections 
Rx ESMC Events 
Indicates the number of SSM status changes indicated by Rx ESMC 
messages 
ETX-2i Devices 
6. Timing and Synchronization 
Field 
Description 
Tx ESMC Events  
Indicates the number of SSM status changes indicated by Tx ESMC 
messages 
ESMC Information Rx 
Number of Rx ESMC packets 
ESMC Information Tx 
Number of Tx ESMC packets 
Examples 
Configuring Clock Selection 
 To configure clock selection: 
• 
Domain 1: 
 
Synchronization network type 2 
 
Quality level: Timing source is Stratum 3E clock 
 
Source 1: Ethernet port 0/3 (which is configured with L2CP profile with peer for MAC 0x02, 
and transmitting of clock SSM messages) 
exit all 
configure port l2cp-profile ssm 
  mac 0x02 peer 
  exit  
 
ethernet 0/3 
  l2cp profile ssm 
  tx-ssm 
  exit all 
 
configure system clock domain 1 
  sync-network-type 2 
  quality min-level-station st3e 
  source 1 rx-port ethernet 0/3 
  exit all 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
Viewing Clock Domain Status 
 To display the clock domain status: 
ETX-2i>config>system>clock>domain(1)# show status 
System Clock Source      : 0         State  : Freerun     Quality  : SEC         
Station Out Clock Source : 0         State  : Unlocked                           
Force Switch             : InActive                                              
Manual Switch            : InActive                                              
T0 offset in PPB         : 0   
Viewing Clock Source Status 
 To display the clock source status: 
ETX-2i# configure system clock domain 1 source 1 
ETX-2i>config>system>clock>domain(1)>source(1)# show status 
Status     : OK 
Tx Quality : DNU 
Rx Quality : PRC 
ESMC State : Unlocked 
WTR State  : Inactive 
Viewing Clock Source Statistics 
 To display the clock source statistics: 
ETX-2i# configure system clock domain 1 source 1 
ETX-2i>config>system>clock>domain(1)>source(1)# show statistics 
ESMC Failure Counter : 0 
                       Rx         Tx 
ESMC Events          : 1           2  
ESMC Information     : 1           255 
 
ETX-2i>config>system>clock>domain(1)>source(1)$ exit 
ETX-2i>config>system>clock>domain(1)# info detail 
    sync-network-type  2 
    quality min-level-station dnu min-level-system sec 
    max-frequency-deviation  1200 
    mode  auto 
    no force-t4-as-t0 
    echo "Clock Source Configuration" 
#   Clock Source Configuration 
    source  1  rx-port  ethernet  0/3 
        priority  2 
        quality-level  ssm-based        wait-to-restore  300 
        hold-off  300 
    exit 

## 6.3 Date and Time  *(p.1205)*

ETX-2i Devices 
6. Timing and Synchronization 
Configuring E1 Port as Rx Clock Source 
 To configure AIO E1 1/1 port as rx-clock-source 1 under domain 1: 
ETX-2i# configure system clock domain 1 source 1 
ETX-2i>config>system>clock>domain(1)# source 1 rx-port e1 1/1 
6.3 Date and Time 
You can configure the ETX-2i to use internal real-time clock (RTC) as free running or to use Network Time 
Protocol version 4 (NTPv4). In ETX-2i with D-NFV/PMC, ETX-2i relays the date and time to the x86 card. 
NTP synchronizes the internal clocks of network devices to a single time reference source. NTP provides 
comprehensive mechanisms to access national time dissemination services, organizes the NTP subnet of 
servers and clients, and adjusts the system clock in each participant. It improves the timekeeping quality 
of the network by using redundant reference sources and diverse paths for time distribution. 
 
Note 
It is recommended to set the date and time using NTP in order to continuously 
maintain the true real time clock. Otherwise. If NTP is not used, the product 
might not restore accurate real time clock after reset. 
Applicability and Scaling 
All ETX-2i products, except for ETX-2i-10G-B, ETX-2i-10G-B/8SFPP and ETX-2i-10G-E/8SFPP, support RTC. 
NTP Multicast Client was introduced in version 6.8.2 (0.31).  
Standards Compliance and MIBs 
• 
DISMAN-SCHEDULE-MIB, RFC 3231 
• 
IF-MIB, RFC 2863 
• 
RFC 5905 
ETX-2i Devices 
6. Timing and Synchronization 
Functional Description 
NTP is a networking protocol for clock synchronization between computer systems over packet-
switched, variable-latency data networks. It is a large and very complex application for the 
synchronization of computers and computer networks, incorporating complex statistical algorithms that 
filter out small discrepancies in time and makes time adjustments. It synchronizes all participating 
computers to within a few milliseconds of Coordinated Universal Time (UTC). 
You can configure the time on the internal clock of an ETX-2i device with the time on an NTP server.  
The device can receive the clock signal from up to three NTP servers in the network. One of the active 
NTP servers can be designated as the preferred server for receiving NTP requests.  
NTP Authentication 
ETX-2i supports NTP authentication. You can configure NTP authentication as follows: 
• 
On the NTP client (device): 
 
Enable NTP authentication – indicates that the client (device) requires NTP authentication 
from its defined NTP servers. 
 
Define authentication keys – For each authentication key, define the key number and key 
value (shared secret). 
 
Define trusted keys, i.e., defined authentication key numbers that can be used for NTP 
authentication with NTP server. 
• 
On the NTP server: 
 
Specify whether this is the preferred server for receiving NTP requests from the client. 
 
Define a single authentication key. NTP protocol requests and responses take place between 
the client and server only if the server’s authentication key matches one of the client’s 
trusted keys. 
If authentication is enabled, the ETX-2i device only accepts authenticated NTP packets from the NTP 
server; otherwise, If NTP authentication is not enabled (the default), the device accepts all NTP packets 
sent from the NTP server.  
Note 
Use of the D-NFV virtualization features requires the Controller and Compute 
Node to use the same clock. It is recommended that the clock come from the 
NTP server. However, if you do not configure an NTP server, you can use the 
Controller clock, which by default, is configured as an NTP server. In this case, 
you must manually configure the Compute Node with the same time zone as 
the Controller. 
ETX-2i Devices 
6. Timing and Synchronization 
NTP Multicast Client 
ETX-2i supports NTP multicast over IPv6. Multicast mode is a special server mode where the NTP server 
broadcasts its synchronization information to all clients.  
You can enable NTP multicast mode by: 
• 
Enabling multicast-client under the NTP level and setting its IPv6 multicast address (or leaving 
the default) on which the device listens for NTP messages (see below).    
• 
Enabling multicast client on a single router interface (refer to Configuring Router Interfaces in 
the Traffic Processing chapter). 
The device can work in either multicast or unicast mode; not both. 
Factory Defaults 
By default, no NTP servers are defined. When an NTP server is defined, its default configuration is: 
• 
IP address is set to 0.0.0.0 
• 
No NTP server authentication key 
• 
Not preferred 
• 
Administratively disabled (shutdown) 
When multicast-client is enabled under NTP, the default multicast-ip-address is ff05::101.  
Configuring the Date and Time 
Setting the Date and Time Parameters 
 To set the system date and time: 
1. Navigate to configure system date-and-time.  
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying the desired date 
format 
date-format { yyyy-mm-dd | dd-mm-yyyy 
| mm-dd-yyyy | yyyy-dd-mm } 
 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Defining the date 
date <date> 
Date is according to the configured 
date format. 
Configuring NTP 
ntp 
For configuration of the internal 
clock in the ETX-2i device. 
See Setting NTP Parameters. 
Scheduling adjustment of 
device time for daylight 
saving time start and stop 
summer-time 
See Configuring Daylight Saving 
Time Scheduling. 
Displaying daylight saving 
time scheduling 
information 
show summer-time 
For details and an example on how 
to view scheduled daylight saving 
time in your device, refer to Viewing 
Scheduling Information in the 
Operation and Maintenance 
chapter. 
Defining the time 
time <hh:mm[:ss]> 
 
Defining the time zone 
relative to Universal Time 
Coordinated (UTC) 
zone utc [<[{+|-}]hh[:mm]>] 
Possible values: 
 -12:00 to +12:00, in 30-minute 
increments 
Setting NTP Parameters 
 To configure NTP parameters: 
1. Navigate to configure system date-and-time ntp. 
The config>system>date-and-time>ntp# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Enabling NTP authentication 
[no] authenticate 
Indicates that the client 
(device) requires NTP 
authentication from its 
defined NTP server  
NTP authentication is not 
supported in multicast 
mode. 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Configuring NTP 
authentication key 
authentication-key <number> md5 
<value> [hashed] 
no authentication-key [<number>] 
number – NTP 
authentication key number 
Possible values: 1-
4294967295 
value – NTP authentication 
key MD5 value 
Possible values: 1-32- 
character string 
hashed – indicates that the 
key value is hashed 
Note: 
• You can repeat this 
command to configure 
multiple keys. 
• Entering no 
authentication-key, 
without the NTP 
authentication key 
number, deletes all keys 
from the configuration. 
• The device saves in the 
database a hashed string 
of the entered MD5 
value, and adds the 
[hashed] keyword, so 
that clear MD5 values 
do not appear in the 
configuration. Users 
should not use the 
[hashed] keyword when 
providing a cleartext 
MD5 string. 
• NTP authentication keys 
are not supported in 
multicast mode. 
Defining minimum and 
maximum polling intervals in 
terms of {log 2} seconds 
polling-interval min <min-poll-
period> max <max-poll-period> 
Possible values for min-poll-
period and max-poll-period 
are 2-17 where 2 means  
22 seconds and 17 means  
217 seconds respectively. 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
The default is 2 (22 seconds) 
for both min-poll-period 
and max-poll-period. 
Note: Polling intervals can 
be configured for unicast 
NTP servers only. 
Configuring the multicast 
client 
multicast-client [<multicast-ip-
address>] 
multicast-ip-address - the 
IPv6 multicast address on 
which the device listens for 
NTP messages. 
If an address is not 
configured, the device 
listens on the default 
address (ff05::101) 
Note:  
• NTP multicast works 
only if it is also enabled 
on a router interface, 
with the ntp-multicast-
client command in the 
config>router>interface 
level (see below) 
• If you configure 
multicast client, do not 
configure unicast client-
server mode (server 
command below). If you 
do so, the unicast client-
server mode overrides 
multicast mode. 
ETX-2i Devices 
6. Timing and Synchronization 
Task 
Command 
Comments 
Defining the NTP server  
server <server-id> 
server-id – IDs of NTP 
servers that can send clock 
signals to the client (device) 
Possible values: 1-3 
See Defining NTP Servers 
for all tasks that you can 
perform on NTP servers. 
Note: Once multicast client 
is enabled, unicast mode 
(client-server mode) is 
disabled, and you should 
not configure NTP servers. 
Doing so results in the 
unicast server configuration 
overriding the NTP MC. 
Displaying NTP status 
show status 
 
Configuring NTP 
authentication trusted key 
trusted-key <number> 
no trusted-key [<number>] 
number – NTP 
authentication key number 
Possible values: 1-
4294967295 
Note: 
• You can repeat this 
command to configure 
multiple keys.  
• Entering no trusted-key, 
without the NTP 
authentication key 
number, configures all 
keys as untrusted. 
 
Defining NTP Servers  
You can define up to three NTP servers. 
 To define an NTP server: 
1. Navigate to config system date-and-time ntp. 
2. At the prompt, type server <server-id> to define an NTP server with ID <server-id>. 
ETX-2i Devices 
6. Timing and Synchronization 
3. At the config>system>date-time>ntp>server(<server-id>)$prompt, perform the required tasks 
according to the following table. 
 
Task 
Command 
Comments 
Setting the server IP address 
address <IP-address> 
 
Configuring the NTP server 
authentication key 
key <number> 
no key [<number>] 
number – number of 
authentication key 
Possible values:  
1-4294967295 
Note: Repeating the 
command replaces the 
previous one. 
Setting the NTP server as the 
preferred server. 
prefer 
Enter no prefer to remove 
preference. 
Note: Only one server can 
be preferred. 
Administratively enabling 
server 
no shutdown 
Entering shutdown disables 
the server. 
Sending an NTP polling request 
to check server status 
query-server 
 
Viewing the Date and Time 
 To display the date and time: 
• 
From the system context (config>system), enter: 
show system-date 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
Examples 
Setting Date and Time 
 To set the date and time: 
• 
Format = mm-dd-yyyy 
• 
Date = May 17, 2012 
• 
Time = 5:40pm 
• 
Zone = UTC –4 hours and 30 minutes 
exit all 
configure system date-and-time 
  date-format mm-dd-yyyy 
  date 05-17-2012 
  time 17:40 
  zone utc -04:30 
Defining NTP Client 
 To define the NTP client: 
• 
Enable authentication  
• 
Authentication keys 10, 13, 19, 22 
• 
Servers 1,2, and 3 
• 
Trusted keys 13, 22 
exit all 
configure system  
  date-and-time 
  ntp 
    authenticate 
    authentication-key 10 17262626 
    authentication-key 13 57648 hashed 
    authentication-key 19 3444486 hashed 
    authentication-key 22 98761122  
    server 1 
    server 2 
    server 3 
    trusted key 13 
    trusted key 22 
exit 
ETX-2i Devices 
6. Timing and Synchronization 
Defining NTP Server 
 To define the NTP server: 
• 
Server ID = 1 
• 
IP address = 172.17.171.141 
• 
Key = 13 
• 
Preferred 
• 
Administratively enabled 
exit all 
configure system  
  date-and-time 
  zone utc +03:00 
  ntp 
  server 1 
    address 172.17.171.141 
    key 13 
    prefer      
    no shutdown 
exit 
Viewing NTP Status 
 To display the NTP status: 
ETX-2i# show con system date-and-time ntp status 
System Uptime       : 000 Days 20:54:36 
System Time (Local) : 04-07-2024 12:19:22 
 
Current Source : NTP 
Drift (ppm)    : 11.650 
Locking Status : Out Of Limits 
 
Servers 
---------------------------------------------------------------------------- 
Name : ntp1.rd.sce-dcn.net 
Prefer : --      Type        : Unicast   Admin        : Enabled   Stratum       : 0 
Key    : --      Delay (ms)  : --        Offset (ms)  : --        Jitter (ms)  : -- 
 
Name : ntp2.rd.sce-dcn.net 
Prefer : Prefer  Type        : Unicast   Admin        : Enabled   Stratum       : 2 
Key    : --      Delay (ms)  : 1.162     Offset (ms)  : 0.596     Jitter (ms)  : 0.398 
 
exit all 
 
 
ETX-2i Devices 
6. Timing and Synchronization 
configure system  
  date-and-time 
  zone utc +03:00 
  ntp 
  server 1 
    address 172.17.171.141 
    key 13 
    prefer      
    no shutdown 
exit 
The fields above are described in the following table. 
Field 
Description 
Drift (ppm) 
Frequency offset between the system clock running at nominal frequency 
and the frequency required to remain in synchronization with UTC 
Locking status 
NTP out of limits indication is based on a noise value derived from peer 
Jitter and wander. 
If the average noise over a 120-second sliding window exceeds 250 
microseconds, out-of-limit is declared. 
Return to “in-limit” status requires the average noise to be under 166 
microseconds for a 300-second sliding window. 
Delay (ms) 
Round-trip delay between the client and server (RFC-5905) 
Offset (ms) 
Maximum-likelihood time offset of the server clock relative to the system 
clock (RFC-5905) 
Jitter (ms) 
Root-mean-square (RMS) average of the most recent offset differences, 
representing the nominal error in estimating the offset (RFC-5905) 
Configuration Errors 
The following table lists the messages that the device generates when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Invalid IP multicast 
address 
The address is not a valid IP multicast. 
Enter a valid IP multicast address. 
Multicast address is 
already configured 
You repeated the command, but only one 
address is allowed. 
Delete the previous multicast address, 
and then configure a new one. 

## 6.4 Daylight Saving Time  *(p.1216)*

ETX-2i Devices 
6. Timing and Synchronization 
6.4 Daylight Saving Time 
You can schedule your device to change its system time to daylight saving time (also known as summer 
time), at a specific date and time.  
Applicability and Scaling 
This feature is applicable to all ETX-2i products. 
Factory Defaults 
By default, no scheduling is configured. 
The default value for daylight saving time offset is 60 minutes. 
Functional Description 
You can specify when the device local system time should reflect the start of daylight saving time by 
adding an offset, and when it should reflect the end of daylight saving time by subtracting the offset. 
Daylight saving time can be scheduled in one of the following ways: 
One shot 
Daylight saving time starts and ends once, at a specified date and 
time (e.g., November 6 2016). 
Recurring 
Daylight saving time starts and ends every year at a specified time, 
and a date specified according to the weekday and month (e.g., first 
Sunday in October). 
The daylight-saving time schedule is saved in nonvolatile (permanent) memory, in order to be available 
after device reboot. 
Note 
ETX-2i logs the start and end of daylight saving time with the events 
summer_time_started and summer_time_ended, respectively. Each event is 
also sent as an SNMP notification to management systems.  
ETX-2i Devices 
6. Timing and Synchronization 
Configuring Daylight Saving Time Scheduling 
When you configure daylight saving time scheduling, the first set of parameters in the commands 
specifies when daylight saving time starts, and the second set of parameters specifies when daylight 
saving time ends. 
 To configure daylight saving time: 
• 
Navigate to the config>system>date-time level and enter the summer-time command 
according to the type of schedule: 
 
One shot – Enter: 
summer-time date {january | february | march | april | may | june | july | august | 
september | october | november | december} <dd> <yyyy> <hh>:<mm> {january | 
february | march | april | may | june | july | august | september | october | november | 
december} <dd> <yyyy> <hh>:<mm> [<offset>] 
 
Recurring – Enter: 
summer-time recurring { 1 | 2 | 3 | 4 | last} {sunday | monday | tuesday | wednesday | 
thursday | friday | saturday} {january | february | march | april | may | june | july | 
august | september | october | november | december} <hh>:<mm> { 1 | 2 | 3 | 4 | last} 
{sunday | monday | tuesday | wednesday | thursday | friday | saturday} {january | 
february | march | april | may | june | july | august | september | october | november | 
december} <hh>:<mm>[<offset>] 
The parameter {1 | 2 | 3 | 4 | last} specifies the week of the month. 
For both schedule types, <offset> specifies (in minutes) the time to add at daylight saving time start, or 
subtract at daylight saving time end. Its range is 1–1440. 
 To delete daylight saving time scheduling: 
• 
Navigate to the config>system>date-time level and enter: 
no summer-time 
Viewing Scheduling Information 
For details and an example on how to view scheduled daylight saving time in your device, refer to 
Viewing Scheduling Information in the Operation and Maintenance chapter. 
ETX-2i Devices 
6. Timing and Synchronization 
Examples 
 To schedule daylight saving time starting March 27 2016 at 1:00 and ending October 27 2016 at 
2:00: 
exit all 
configure system date-and-time 
summer-time date march 27 2016 01:00 october 27 02:00 
save 
 To schedule daylight saving time starting on the first Friday in March at 2:00 and ending on the 
last Sunday in October at 3:00: 
exit all 
configure system date-and-time 
summer-time recurring 1 friday march 02:00 last sunday october 03:00 
save 
Configuration Errors 
The following table lists the messages that the device generates when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Schedule with this name 
already configured 
You tried to create a new schedule with a 
name that is used by an existing schedule. 
Specify a name that is not being used 
by an existing schedule. 
Summer-time already 
configured 
You entered the summer-time command 
to configure daylight saving time, but the 
scheduling of summer-time has already 
been configured. 
Delete the existing summer-time 
configuration; and then re-enter the 
summer-time command. 
Recurring summer-time 
start and end must be on 
different months 
You tried to configure summer-time start 
and end in the same month. 
Enter the summer-time command 
with summer-time start and end in 
different months. 
Summer-time cannot 
end before it starts 
You entered the summer-time command 
(with one-shot schedule type) with 
summer-time end time earlier than 
summer-time start.  
Enter the summer-time command 
with summer-time start time earlier 
than the end time. 