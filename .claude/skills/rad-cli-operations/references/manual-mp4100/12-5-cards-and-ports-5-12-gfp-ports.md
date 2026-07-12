# 5 Cards and Ports – 5.12 GFP Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 328–332.*


## Applicability and Scaling  *(p.328)*

5. Cards and Ports 
timeout expires. When using inband management, always use the timeout option; otherwise, the 
management communication path may be permanently disconnected. 
The default is infinite duration (without timeout). 
Activating Loopbacks and BER Tests  
 To perform a loopback or BER Test on the G703 link: 
1. Navigate to configure port ds0-g703 <slot>/<port> to select the optical link to be tested. 
The config>port> ds0-g703>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below.  
Task 
Command 
Comments 
Activating and configuring the 
direction of the loopback and 
the duration of it (in minutes) 
loopback {local | remote} 
[duration <duration in minutes 
1..30> ]  
local – local loopback 
remote – remote loopback 
  
Stopping the loopback  
no loopback 
 
Activating the BER test and 
configuring its parameters 
bert   
 
Stopping the BER test  
no bert 
 
Displaying the BER test results 
show bert 
 
A typical display: 
Status         : Not Active 
Bit Error Count: 1            
Pattern        : 2e-15        
Run Time (Sec) : 1            
ES (Sec)       : 1            
Sync Loss (Sec): 1  
5.12 GFP Ports  
Applicability and Scaling 
GFP ports represent VCGs (Virtual Concatenation Groups) with GFP encapsulation and can be configured 
for the following ports: 

## Standards Compliance  *(p.329)*


## Factory Defaults  *(p.329)*


## Configuring GFP Ports  *(p.329)*

5. Cards and Ports 
• 
SDH/SONET (CL.2 modules) 
• 
E1/T1 (VS-16E1T1-EoP modules) 
• 
T3 (T3 modules).  
They can be mapped either directly to the physical layer or to VCG. In the latter case, the binding is done 
in two stages and the VCG is further bound to the physical layer.  
Standards Compliance 
GFP Ports comply with ITU-T Rec. G.7041, using the framed mode. 
Factory Defaults 
Megaplex-4 is supplied with all GFP ports disabled. 
Configuring GFP Ports 
 To configure a GFP port: 
1. Navigate to configure port gfp <slot>/<port> to select the gfp port to configure. 
The config>port>gfp>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
`  
Assigning short description to 
port 
name <string> 
Using no name removes the name 
Administratively enabling port 
no shutdown 
Using shutdown disables the port 
5. Cards and Ports 
Task 
Command 
Comments 
`  
Binding the corresponding 
VC/VT/STS-1/VCG to the GFP port 
(CL modules)  
 
bind vc4-sts3c 
<slot>/<port>/<tributary>  
bind vc3-sts1 
<slot>/<port>/<au4>/ 
<tributary> 
bind vc-vt <slot>/<port>/ 
<au4>/<tug_3>/<tug_2> 
[/<tributary>]  
bind vcg <slot>/<port> 
For the allowed ranges, see Entities Bound 
to Logical MAC. 
The connection to a VC or VT/STS depends 
on the frame selection (frame=sdh or 
frame=sonet) 
You cannot bind both a VCG and a 
VC/VT/STS-1 to a GFP port  
Using no before the corresponding 
command removes the binding 
Binding the corresponding 
T3/VCG to the GFP port (T3 
modules)  
 
bind t3 <slot>/<1> 
bind vcg <slot>/<port> 
The allowed ranges of VCG ports is 1 to 16 
per slot. 
Using no before the corresponding 
command removes the binding 
Binding the corresponding VCG to 
the GFP port (VS-16E1T1-EoP 
modules)  
 
bind vcg <slot>/<port> 
The allowed ranges of VCG ports is 1 to 16 
per slot. 
Using no before the corresponding 
command removes the binding 
Enabling payload error detection: 
in this case, a frame checksum is 
calculated, using the 32-bit 
polynomial recommended by ITU-
T, and added to the GFP frame 
structure  
fcs-payload 
 
 
Using no fcs-payload disables payload 
error detection 
Enabling the use of payload data 
scrambling in the transmit and 
receive directions, before 
insertion in frames 
scrambler-payload { rx | tx | 
rx-tx } 
 
Using no scrambler-payload disables 
payload scrambling for both the transmit 
and receive directions 
Assigning user-defined VC profile 
to the port  
vc profile <profile name> 
For creating VC profiles, see VC Profiles.  
Using no vc removes the profile  
Before you assign the user-defined profile, 
you must use the no vc command to 
remove the automatical lvc-eos or hvc-gfp 
profile assignement 

## Displaying GFP Statistics  *(p.331)*

5. Cards and Ports 
Displaying GFP Statistics  
GFP ports feature the collection of statistical diagnostics.  
 To display the GFP port statistics: 
• 
At the prompt config>slot>port>gfp (<slot><port>)#, enter show statistics followed by 
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
 
 
 
GFP statistics are displayed.  The counters are described below. For example: 
Current Statistics: 
config>port>gfp(cl-b/6)# show statistics current 
 
Current 
---------------------------------------------------------------  
Time Elapsed (Sec) : 299 
Valid Intervals    : 96 
Total RX Frames    : 475682 
Total RX Frames    : 475681 
Idle Frames Error  : 237726 
cHEC Errors        : 0 
tHEC Errros        : 0 
eHEC Errors        : 0 
FCS Errors         : 0 
PTI Mismatch       : 0 
EXI Mismatch       : 0 
Statistics for interval 67: 
config>port>gfp(cl-a/1)# show statistics interval 67 
 
Interval  
--------------------------------------------------------------- 
Interval Number   : 67 
Total RX Frames   : 1192393 
Total RX Frames   : 1192403 
5. Cards and Ports 
Idle Frames Error : 0 
cHEC Errors       : 0 
tHEC Errros       : 0 
eHEC Errors       : 0 
FCS Errors        : 0 
PTI Mismatch      : 0 
EXI Mismatch      : 0 
GFP Statistics Parameters 
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
Total Rx Frames 
Total number of frames received 
Total Tx Frames 
Total number of frames transmitted 
Idle Frames Error  
 
Number of idle frames errors. 
Idle frame is a special four-octet GFP control frame consisting of only a GFP 
Core Header with the PLI and cHEC fields (see 6.1.1 in G.7041) set to 0, and no 
Payload Area. The Idle frame is intended for use as a filler frame for the GFP 
transmitter to facilitate the adaptation of the GFP octet stream to any given 
transport medium where the transport medium channel has a higher capacity 
than required by the client signal 
cHEC Errors  
 
Number of cHEC errors. 
GFP Core Header consists of a 16-bit PDU Length Indicator field and a 16-bit 
Core Header Error Check (cHEC). 
tHEC Errors  
 
Number of tHEC errors. 
GFP Core Header consists of a 16-bit PDU Length Indicator field and a 16-bit 
Type Header Error Check (tHEC). 
FCS Errors 
The number of frames received on this interface that are an integral number of 
octets in length but do not pass the FCS check  
PTI Mismatch  
Number of payload Headers with incorrect PTI values  
EXI Mismatch  
Number of payload Headers with incorrect EXI values  
There are two options for clearing GFP statistics data: 
• 
Clearing current interval statistics 