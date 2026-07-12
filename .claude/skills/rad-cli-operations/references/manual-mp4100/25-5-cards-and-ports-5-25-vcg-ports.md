# 5 Cards and Ports – 5.25 VCG Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 454–466.*


## Applicability and Scaling  *(p.454)*


## Standards Compliance  *(p.454)*

5. Cards and Ports 
Activating the Loopback 
 To perform a loopback on the cmd-out-i port: 
1. Navigate to configure port cmd-out-i <slot>/<port>/<trib>. 
The config>port> cmd-out-i>(<slot>/<port>/<trib>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Activating and configuring the 
direction of the loopback  
loopback remote [duration 
<minutes>] 
 
Returns the received data at the 
physical layer to the transmitting path. 
• Using no loopback stops the 
loopback. 
• Duration –1 to 30 minutes or infinite 
5.25 VCG Ports  
Applicability and Scaling 
Virtually concatenated groups (VCGs) can be configured on the following ports: 
• 
SDH/SONET (CL.2 modules) 
• 
E1/T1 (VS-16E1T1-EoP modules) 
• 
T3 (T3 modules).  
Standards Compliance 
Two types of supported encapsulation comply with the following standards: 
• 
LAPS (Link Access Protocol – SDH) encapsulation in accordance with ITU-T Rec. X.86  
• 
GFP (Generic Framing Procedure) encapsulation in accordance with ITU-T Rec. G.7041, using the 
framed mode. 

## Benefits  *(p.455)*


## Functional Description  *(p.455)*

5. Cards and Ports 
Benefits 
Virtual concatenation has the following main advantages: 
• 
Scalability: allows bandwidth to be selected in relatively small increments, as required to match 
the desired payload data rate. 
• 
Efficiency: the resulting signals are easily routed through a SDH/SONET network, without 
wasting bandwidth, and therefore allows for more efficient utilization of the bandwidth 
available on existing networks. 
• 
Compatibility: virtual concatenation requires only the end nodes to be aware of the containers 
being virtually concatenated, and therefore is transparent to the core network elements. 
• 
Resiliency: individual members of a virtually concatenated group can be freely routed across the 
network.  
Functional Description  
To prepare Ethernet traffic for efficient transport over the SDH/SONET network, the traffic is 
encapsulated using LAPS or GFP encapsulation, before being transmitted over a virtually concatenated 
group. Ethernet transport over T3 and Ethernet transport over E1/T1 is done using GFP encapsulation. 
Megaplex-4 also supports the Link Capacity Adjustment Scheme (LCAS), covered by ITU-T Rec. G.7042. 
In Megaplex-4, VCGs are protected by the Ethernet group redundancy. For description and instructions, 
refer to Ethernet Group Protection in Chapter 7. 
Ethernet over SDH/SONET  
To carry Ethernet payload without wasting bandwidth over SDH/SONET link, Megaplex-4 uses the Virtual 
Concatenation method. In this method, the contiguous bandwidth of the payload signal is divided into 
several streams, each having the rate necessary for insertion into individual VCs (SDH) or SPEs (SONET). 
With virtual concatenation, the individual VCs or SPEs are transported over the SDH or SONET network 
in the usual way, and then recombined to restore the original payload signal at the end point of the 
transmission path, using a technology similar to inverse multiplexing.  
The processing is as follows:  
1. At the source end, the inverse multiplexing subsystem splits the payload signal into several 
streams at a rate suitable for transmission over the desired type of VC (VC-12, VC-3 or VC-4) or 
SPE. The required information (type and number of VCs or SPEs) are defined when the virtually 
concatenated group (VCG) is defined.  
5. Cards and Ports 
2. The resulting streams are mapped to the desired VCs/SPEs, also configured by management. 
The Path Overhead (POH) byte carried by all the group members is used to transfer to the far 
endpoint the information needed to identify: 
 
The relative time difference between arriving members of the virtual group 
 
The sequence number of each arriving member. 
3. Each member of the virtual group is independently transmitted through the network. The 
network need not be aware of the type of payload carried by the virtual members of the group. 
4. At the receiving end, the phase of the incoming VCs/SPEs is aligned and then the original 
payload data stream is rebuilt. This requires using a memory of appropriate size for buffering all 
the arriving members of the group at the receiving end. The memory size depends on the 
maximum expected delay, therefore to minimize latency the maximum delay to be 
compensated can be defined by management. 
Encapsulation Modes 
Ethernet frames must be encapsulated before transport over the SDH/SONET network. You can select 
the desired encapsulation mode, independently, for each virtually concatenated group. This can be done 
by binding VCG ports to the corresponding entity:  
• 
For LAPS encapsulation, see Error! Reference source not found..  
• 
For GFP encapsulation, see Error! Reference source not found.. 
Support for LCAS 
Each virtually concatenated group with two or more VCs/VTs can be configured to support LCAS. 
With LCAS, the capacity of a virtually concatenated group can be hitlessly decreased when one of the 
VCs/VTs fails; when the failure is no longer present, the group will automatically and hitlessly recover to 
return to the normal capacity. Another LCAS advantage is that it allows setting up a link even when the 
number of VCs/VTs at the two endpoints, or anywhere along the trail followed by the VCG, is not equal. 
The user can specify a minimum number of VCs/VTs for the group capacity: if the number of VCs/VTs 
decreases below this minimum, an alarm will be generated. 
Ethernet over Full/Channelized T3  
T3 modules allow encapsulating Ethernet traffic with the GFP protocol and transferring it over full or 
channelized T3 media. In both cases Ethernet ports are connected to Logical MAC ports via flows, and 
these Logical MAC ports are bound to GFP ports. Starting from the GFP ports, two ways are available: 
5. Cards and Ports 
• 
To transfer Ethernet over full T3, only one GFP/Logical MAC port is created and T3 port is bound 
directly to it. 
• 
To transfer Ethernet over channelized T3, up to 16 Logical MAC, GFP and VCG ports are created, 
so that the VCG ports are bound to GFP ports and GFP ports are bound to Logical MAC ports. Up 
to 16 T1 ports can be bound to each VCG port, but the total T1 number is limited by 28 T1 ports 
per T3 module. On the remaining T1s, regular TDM traffic can be mapped.  
The figure below shows the relationship between the entities involved in the Ethernet over T3/T1 
functionality.  
 
Bind 1:1
Logical MAC
16
Flow
Egress/Ingress Port
GFP 1
GFP 16
VCG 1..16
Bind 1:1
T3
T1
Bind 1:n
Bind 1:1
ETH Group
OR
Logical MAC
1
Bind 1:1
 
Logical Entities Representing Ethernet Traffic over Full/Channelized T3 Media  
5. Cards and Ports 
Ethernet over E1/T1  
VS-16E1T1-EoP modules allow encapsulating Ethernet traffic with the GFP protocol and transferring it 
over E1/T1 media. Ethernet ports are connected to Logical MAC ports via flows, these Logical MAC ports 
are bound to GFP ports and GFP ports are bound to VCG ports. Up to 16 E1/T1 or E1-i/T1-i ports can be 
bound to each VCG port. 
The figure below shows the relationship between the entities involved in the Ethernet over E1/T1 
functionality.  
 

## Factory Defaults  *(p.459)*

5. Cards and Ports 
Bind 1:1
Logical MAC
16
Flow
Egress/Ingress Port
GFP 1
GFP 16
E1-i/T1-i
E1/T1
Bind 1:n
Bind 1:n
ETH Group
OR
Logical MAC
1
Bind 1:1
Bind 1:1
VCG 1
VCG 16
Bind 1:1
 
Logical Entities Representing Ethernet Traffic over E1/T1 Media 
Factory Defaults 
Megaplex-4 is supplied with all VCG ports disabled. 

## Configuring VCG Ports  *(p.460)*

5. Cards and Ports 
Configuring VCG Ports  
 To configure a VCG: 
• 
At the config>port>vcg (slot/port)# prompt, enter all necessary commands according to the 
tasks listed below:  
Task 
Command 
Comments 
Assigning short description to a 
VCG port 
name <string> 
Using no name removes the name 
Administratively enabling a VCG 
port 
no shutdown 
Using shutdown disables the VCG port 
Binding the corresponding 
VC/VT/STS-1 to the VCG port  
bind vc4-sts3c 
<slot>/<port>/<tributary>  
bind vc3-sts1 
<slot>/<port>/<au4>/ 
<tributary> 
bind vc-vt <slot>/<port>/ 
<au4>/<tug_3>/<tug_2> 
[/<tributary>]  
For the allowed ranges, see Entities Bound 
to Logical MAC. 
The connection to a VC or VT/STS depends 
on the frame selection (frame=sdh or 
frame=sonet) 
Using no before the corresponding 
command removes the binding 
The maximum number of VC-4/STS-3C 
containers per system is limited to the full 
STM-4/OC-3 capacity of a single CL.2 
module. 
The maximum number of vc-vt containers 
for EoS per CL module is limited to 128. 
Binding the T1 internal port of the 
T3 module to the VCG port  
bind t1  
<slot>/1/<tributary t1> 
The maximum number of T1 ports bound 
to one VCG port is 16. 
Binding the E1/T1 external and 
internal ports of the VS-16E1T1-
EoP module to the VCG port  
 
bind t1  <slot>/<port> 
bind t1-i  <slot>/<port> 
bind e1  <slot>/<port> 
bind e1-i  <slot>/<port> 
The maximum number of E1/T1 or E1-i/T1-
i ports bound to one VCG port is 16. 
Ports bound to VCG must be defined on 
same slot as this VCG port. 
The ports bound to a specific VCG must 
belong to the same type (no mix is allowed 
between e1 and e1-i ports or t1 and t1-I 
ports).  

## Configuration Errors  *(p.461)*


## Viewing LCAS Status Information  *(p.461)*

5. Cards and Ports 
Task 
Command 
Comments 
Enabling the use of the Link 
Capacity Adjustment Scheme 
(LCAS) on the corresponding 
group 
lcas 
 
LCAS is relevant only when the group 
includes 2 or more VCs/T1s. Therefore for 
VC-4 (STS-3c) binding it is relevant only 
when STM-4/OC-12 ports are configured 
Using no lcas disables the use of LCAS 
Selecting the minimum allowed 
number of operational 
VC/VT/STS/T1s that must remain 
in operation. If the number 
decreases below the selected 
value, an alarm is generated. 
minimum-number-of-links 
<value> 
This parameter is relevant only when LCAS 
is enabled.  
 
Selecting the maximum 
differential delay (delay 
compensation needed for 
alignment of low- and high-order 
virtually concatenated payloads in 
the SONET/SDH network) 
max-differential-
delay  <value> 
The range is 1 to 256 (in msec)  
Default: 64 msec 
For optimal latency performance of the 
ETHoSDH services, it is recommended to 
set low values of max-differential-delay 
(the minimum value needed for your 
application).  
Configuration Errors  
The tables below list messages generated by Megaplex-4 when a configuration error on the VCG ports is 
detected. 
VCG Configuration Error Messages  
Code 
Type 
Syntax 
Meaning 
767 
Error 
 
CAN'T BIND THE SAME E1/T1 
TO DIFFERENT VCGS 
The same E1/T1 port cannot be bound to 2 different VCGs. 
This error is relevant for VS-16E1T1EOP and T3 modules.  
Viewing LCAS Status Information  
For viewing the LCAS status information, follow the instructions below. 
5. Cards and Ports 
 To view the LCAS status information: 
1. Navigate to config>port>vcg> (<slot>/<port>)#  
2. Type show status. 
The status is displayed. 
Example for SDH/SONET:  
config>port>vcg(cl-a/2)# show status 
Name                  : CL-A vcg 02 
Administrative Status : Up 
Operation Status      : Up 
LCAS Status           : All Normal 
 
Members 
--------------------------------------------------------------- 
Link          : cl-a/2/1/1/1/2 
Source Status : Norm 
Sink Status   : Norm 
Status        : OK 
Link          : cl-a/2/1/1/1/3 
Source Status : Norm 
Sink Status   : Norm 
Status        : OK 
Link          : cl-a/2/1/2/2/3 
Source Status : Norm 
Sink Status   : Norm 
Status        : OK 
Link          : cl-a/2/1/3/5/1 
Source Status : Norm 
Sink Status   : Norm 
Status        : OK 
Link          : cl-a/1/2/1/2/1 
Source Status : Norm 
Sink Status   : Norm 
Status        : OK 
Link          : cl-a/1/2/2/3/1 
Source Status : Norm 
Sink Status   : Norm 
Status        : OK 
Link          : cl-a/1/2/2/5/1 
Source Status : EOS  
Sink Status   : EOS 
Status        : OK  
Example for T3:  
config>port>vcg(3/1)# show status 
Name                  : IO-3 vcg 01 
Administrative Status : Up 
Operation Status      : Up 
LCAS Status           : All Normal 
5. Cards and Ports 
 
Members 
----------------------------------------------------------------- 
Link          : 3/1/3 
Source Status : Norm 
Sink Status   : Norm 
Status        : OK 
Link          : 3/1/4 
Source Status : Norm 
Sink Status   : Norm 
Status        : OK 
Link          : 3/1/5 
Source Status : Norm 
Sink Status   : Norm 
 
Status        : OK 
Link          : 3/1/6 
Source Status : EOS 
Sink Status   : EOS 
Status        : OK 
The parameters displayed in the screen are as follows: 
Administrative Status 
Displays the administrative status of the corresponding VC/VT or T1 link: Up 
or Down 
Operation Status 
Displays the operation status of the corresponding VC/VT or T1 link: Up or 
Down 
LCAS Status 
Displays the LCAS status of the corresponding VC/VT or T1 link:  
• All Normal –all T1/VC/VT ports bound to the selected VCG are active 
• Within Range –number of  active T1/VC/VT ports bound to the selected 
VCG is not below the value set by the “minimum-number-of-links” 
parameter 
• Below Min No of VC –number of active T1/VC/VT ports bound to 
the selected VCG and active is below the value set by the “minimum-
number-of-links” parameter  
Link 
SDH/SONET: Identifies the position of the corresponding VC or VT within the 
STM-1/STM-4 or OC-3/OC-12 frame, using the vc4-sts3c/ tug-3/tug-2/tu 
format. The Link number also includes the identification of the link, cl-a/1, cl-
a/2, cl-b/1 or cl-b/2. 
T3: Identifies the position of the corresponding T1 within the T3 frame, using 
the <slot>/1/<t1 tributary> format.   

## Displaying LCAS Statistics  *(p.464)*

5. Cards and Ports 
Source Status 
 
Displays the state of the corresponding VC/VT (SDH/SONET) or T1 (T3 
module) on the local end of the path serving the selected VCG (that is, the 
end located on the Megaplex-4 to which the supervisory terminal is 
connected):  
• Fixed – the end uses the fixed bandwidth (not LCAS)  
• Add – the corresponding VC/VT or T1 is about to be added to the VCG  
• Norm – normal transmission state 
• EOS – end-of-sequence indication  
• Idle – the corresponding VC/VT or T1 is not part of the VCG, or is about to 
be removed from the group 
• DNU – do not use the corresponding VC/VT or T1, for example, because 
the sink side reported a failure.  
The state is correct at the time the command to display this screen has been 
received by the Megaplex-4. 
Sink Status 
Same as above for the sink side (remote end of the path).  
Status 
Displays the member status of the corresponding VC/VT or T1 link: OK or 
Failed 
Displaying LCAS Statistics  
VCG ports feature the collection of LCAS statistical diagnostics.  
 To display the LCAS statistics: 
• 
At the prompt config>slot>port>vcg (<slot><port>)#, enter show statistics followed by 
parameters listed below.  
Task 
Command 
Comments 
Displaying statistics 
show statistics {all | current}  
 
  
• current –Displays the current 
statistics 
• all –Displays all statistics: first 
current interval statistics, then 
statistics for all valid intervals 
Displaying statistics 
for a specific interval 
show statistics interval <interval-num 1..96> 
 
 
LCAS statistics are displayed.  The counters are described in the table below. For example: 
Current Statistics (SDH/SONET): 
5. Cards and Ports 
config>port>vcg(cl-a/2)# show statistics current 
Current 
----------------------------------------------------------------- 
Time Elapsed (Sec)               : 644 
Valid Intervals                  : 3 
Number of Active VCs/VTs         : 4 
Maximum Number of Active VCs/VTs : 4 
Minimum Number of Active VCs/VTs : 0 
Current Statistics (T3): 
config>port>vcg(3/1)# show statistics current 
Current 
----------------------------------------------------------------- 
Time Elapsed (Sec)             : 444 
Valid Intervals                : 96 
Number of Active Links         : 4 
Maximum Number of Active Links : 4 
Minimum Number of Active Links : 0 
Statistics for interval 2 (SDH/SONET): 
config>port>vcg(cl-a/2)# show statistics interval 2 
Interval 
----------------------------------------------------------------- 
Interval Number                  : 2 
Maximum Number of Active VCs/VTs : 4 
Minimum Number of Active VCs/VTs : 0 
Under Minimum Limit Time         : 0 
Statistics for interval 2 (T3): 
config>port>vcg(3/1)# show statistics interval 2 
Interval 
----------------------------------------------------------------- 
Interval Number                : 2 
Maximum Number of Active Links : 4 
Minimum Number of Active Links : 0 
Under Minimum Limit Time       : 0 
LCAS Statistics Parameters 
Parameter 
Description 
Time elapsed (Current 
statistics only) 
The elapsed time (in seconds) since the beginning of the current interval. The 
range is 1 to 900 seconds  
Valid Intervals (Current 
statistics only) 
The number of elapsed finished 15-min intervals for which statistics data can be 
displayed, in addition to the current (not finished) interval (up to 96) 
Interval number (Selected 
interval statistics only) 
Number of interval for which statistics is displayed 
5. Cards and Ports 
Parameter 
Description 
Number of Active 
VCs/VTs/Links (Current 
statistics only) 
Displays the current number of active VCs/VTs (for SDH/SONET) or T1 links (for 
T3 modules) reported for the corresponding VCG 
Maximum Number of Active 
VCs/VTs/Links  
Displays the maximum number of active VCs/VTs(for SDH/SONET) or T1 links 
(for T3 modules)  reported for the corresponding VCG during the selected 
interval 
Minimum Number of Active 
VCs/VTs/Links  
Displays the minimum number of active VCs/VTs(for SDH/SONET) or T1 links 
(for T3 modules)  reported for the corresponding VCG during the selected 
interval 
Under Minimum Limit Time       
(Selected interval statistics 
only) 
Displays the accumulated time, in seconds, during which the number of active 
VCs/VTs (for SDH/SONET) or T1 links (for T3 modules) for the corresponding 
VCG has been less than the configured minimum allowed number 
There are two options for clearing LCAS statistics data: 
• 
Clearing current interval statistics 
• 
Clearing all statistics, except for the current interval. 
 To clear the current interval statistics: 
1. Navigate to the corresponding entity as described above. 
2. Enter clear-statistics current-interval. 
The statistics for the specified entity are cleared. 
 To clear all statistics data except for from the current interval: 
1. Navigate to the corresponding entity as described above. 
2. Enter clear-statistics current-all. 
The statistics for the specified entity are cleared. 