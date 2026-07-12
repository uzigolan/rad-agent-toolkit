# 5 Cards and Ports – 5.13 HDLC Ports (CL.2 Modules)

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 333–336.*


## Applicability and Scaling  *(p.333)*


## Standards Compliance  *(p.333)*


## Factory Defaults  *(p.333)*

5. Cards and Ports 
• 
Clearing all statistics. 
 To clear the current interval statistics: 
1. Navigate to the corresponding entity as described above. 
2. Enter clear-statistics current-interval. 
The statistics for the specified entity are cleared. 
 To clear all statistics data: 
1. Navigate to the corresponding entity as described above. 
2. Enter clear-statistics current-all. 
The statistics are cleared. 
5.13 HDLC Ports (CL.2 Modules) 
Applicability and Scaling 
HDLC ports defined on CL.2 modules represent VCGs (Virtual Concatenation Groups) with LAPS 
encapsulation. They can be mapped either directly to the physical layer or to a VCG. In the latter case, 
the binding is done in two stages and the VCG is further bound to the physical layer. The maximum total 
number of GFP and HDLC ports that can be configured per slot is 32. 
Standards Compliance 
HDLC ports in CL.2 modules comply with ITU-T Rec. X.86.  
Factory Defaults 
Megaplex-4 is supplied with all HDLC ports disabled. 

## Configuring HDLC Ports  *(p.334)*


## Displaying HDLC Statistics  *(p.334)*

5. Cards and Ports 
Configuring HDLC Ports  
 To configure an HDLC port: 
1. Navigate to configure port hdlc <slot>/<port> to select the HDLC port to configure.  
The config>port>hdlc>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
Assigning short 
description to the port 
name <string> 
Using no before name removes the name 
Administratively enabling 
the port 
no shutdown 
Using shutdown disables the port 
Binding the corresponding 
VC/VT/STS-1/VCG to the 
HDLC port  
bind vc4-sts3c <slot>/<port>/<tributary>  
bind vc3-sts1 <slot>/<port>/<au4>/ 
<tributary> 
bind vc-vt <slot>/<port>/ 
<au4>/<tug_3>/<tug_2>/ 
[<tributary>]  
bind vcg <slot>/<port> 
For the allowed ranges, see Error! Reference 
source not found. 
The connection to a VC or VT/STS depends on 
the frame selection (frame=sdh or 
frame=sonet) 
You cannot bind both a VCG and a 
VC/VT/STS-1 to an HDLC port  
Using no before the corresponding command 
removes the binding 
Assigning user-defined VC 
profile to the port  
vc profile <profile name> 
For creating VC profiles, see VC Profiles.  
Using no vc removes the profile  
Before you assign the user-defined profile, 
you must use the no vc command to remove 
the automatical hvc-laps or lvc-eos profile 
assignement 
Displaying HDLC Statistics  
HDLC ports of CL.2 modules feature the collection of statistical diagnostics.  
 To display the HDLC port statistics: 
• 
At the prompt config>slot>port>hdlc (<slot><port>)#, enter show statistics followed by 
parameters listed below.  
5. Cards and Ports 
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
 
 
HDLC statistics are displayed.  The counters are described in the table below. For example: 
Current Statistics: 
config>port>hdlc(cl-b/6)# show statistics current 
Current 
---------------------------------------------------------------Time Elapsed (Sec)       
: 430 
Valid Intervals          : 96 
Total RX Frames          : 569704 
Total TX Frames          : 569703 
Address Mismatch         : 0 
Control Mismatch         : 0 
LAPS Sapi Mismatch       : 0 
FCS Errors               : 0 
Abort Frames             : 0 
Minimum Length Violation : 0  
Maximum Length Violation : 0  
Statistics for interval 67:  
config>port>sdh-sonet(cl-a/1)# show statistics interval 67 
 
Interval  
--------------------------------------------------------------- 
Interval Number   : 67 
Total RX Frames   : 1192393 
Total RX Frames   : 1192403 
Address Mismatch         : 0 
Control Mismatch         : 0 
LAPS Sapi Mismatch       : 0 
FCS Errors               : 0 
Abort Frames             : 0 
Minimum Length Violation : 0  
Maximum Length Violation : 0  
5. Cards and Ports 
HDLC Statistics Parameters 
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
Address Mismatch          
 
The number of frames with wrong address value (the correct value of Address 
byte in LAPS Overhead is 0x4) 
Control Mismatch 
 
The number of frames with wrong control value (the correct value of Control 
byte in LAPS Overhead is 0x3) 
LAPS Sapi Mismatch 
 
The number of frames with wrong SAPI value (the correct value of SAPI byte in 
LAPS Overhead is 0xF0E1) 
FCS Errors 
The number of frames received on this interface that are an integral number of 
octets in length but do not pass the FCS check 
Abort Frames 
The number of abort frames received (a packet can be aborted by inserting the 
abort sequence, 0x7d7e. Reception of this code at the far end will cause the 
receiver to discard this frame) 
Minimum Length Violation 
Total number of undersized frames received/transmitted 
Maximum Length Violation 
Total number of oversized frames received/transmitted 
There are two options for clearing HDLC statistics data: 
• 
Clearing current interval statistics 
• 
Clearing all statistics, except for the current interval. 
 To clear the current interval statistics: 
1. Navigate to the corresponding entity as described above. 
2. Enter clear-statistics current-interval. 
The statistics for the specified entity are cleared. 