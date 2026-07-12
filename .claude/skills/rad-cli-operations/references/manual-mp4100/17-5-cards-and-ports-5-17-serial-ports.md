# 5 Cards and Ports – 5.17 Serial Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 345–356.*


## Applicability and Scaling  *(p.345)*

5. Cards and Ports 
Task 
Command 
Comments 
Set and activate the management 
timeout 
temp-enable-mng-ethernet-
traffic  <0..120> 
The command values are set in minutes.  
Entering a new value while 
previous timer is still active 
restarts the timer to the 
new value. 
0 stops the timer, management access via 
mng-ethernet is not allowed 
Changing of the mng-ethernet to “shutdown” 
while timer is active stops forwarding traffic. 
Default: 30  
 To display the timeout remaining time, use the following command: 
mp4100>config>mngmnt#show mng-ethernet-timeout  
Traffic Forwarding Configured Timeout [Min]     : 60  
Traffic Forwarding Remaining Time [Min]: 9  
5.17 Serial Ports  
The section describes the Megaplex-4 serial ports belonging to the VS I/O modules family. The VS-
OCU/E&M module has two OCU-DP ports also configured in CLI serial. For this reason, they are also 
described in this section. 
Applicability and Scaling 
The following table shows the type and number of serial ports available on each Megaplex-4 serial I/O 
module. 
Megaplex-4 Serial Ports 
Module  
Type of Module 
Number of Ports 
VS-6/BIN, VS-6/C37 
VS-6/FXS, VS-6/FXO,  
VS-6/E&M, VS-6/E1T1 
versatile  
6  
5. Cards and Ports 
Module  
Type of Module 
Number of Ports 
VS-12 
versatile 
12 
VS-OCU/E&M 
versatile 
2 
The following parameters can be configured for the serial ports: 
• 
Port name 
• 
Administrative status 
• 
Clock mode 
• 
Port data rate  
• 
Size of the FIFO buffer used by the channel 
• 
Port transmission mode  
• 
Setting CTS line to track the state of the local RTS line 
• 
Selecting the number of data bits/stop bits and controlling the  
end-to-end transfer of the parity bit in the asynchronous word format 
• 
Selecting other parameters for specific kind of modules. 
Although VS-OCU/E&M OCU ports are configured as serial, they are a special kind of serial ports not 
supporting most of the parameters. 
The following table list the features available for serial ports of VS modules. Refer to Error! Reference 
source not found. for configuration instructions. In addition, consult Chapter 13 for specific 
configuration considerations.  
Features Supported by VS Serial Ports  
Feature/Command 
VS modules 
VS-OCU/E&M 
Number of ports 
6/12 
2 
Additional ports 
cmd-in* 
cmd-out* 
cmd-ch* 
- 
Split TS cross-connect (for serial 
ports)  
√ 
- 
name 
√ 
√ 
shutdown 
√ 
√ 
5. Cards and Ports 
Feature/Command 
VS modules 
VS-OCU/E&M 
cts-rts 
√ 
- 
rate 
√ 
√ 
mode 
√ 
- 
encapsulation-mode 
√ 
- 
end-to-end-control 
√ 
- 
data-bits 
√ 
- 
parity 
√ 
- 
stop-bits 
√ 
- 
interface 
√ 
- 
s-bit-signaling 
√ 
- 
data-position  
√ 
- 
*for VS-6/BIN modules 
Support of some features related to serial ports differs for different VS modules. These features are 
listed in the following table. 
  Additional Features Related to Serial Ports of I/O Modules  
I/O Module 
R.111 
Encapsulation 
Conference 
Mode 
DS0-SNCP Bundles/ 
DS0 Groups 
VS-12, VS FXS/FXO Voice with 
serial ports (basic) 
Yes 
No 
28/14  
VS-6/C37 
Yes 
No 
16/8  
VS E&M Voice with serial ports 
(basic) 
Yes  
No 
24/12  
VS-6/BIN 
Yes 
Yes 
12/6 
VS-FXS/E&M 
No 
N/A 
20/10 
VS FXS/FXO Voice 
(PW-enhanced), VS-6/703  
No 
No 
28/14  
VS E&M Voice (PW-enhanced)  
No 
No 
20/10 
VS-6/8E1T1/PW 
No 
No 
N/A 
VS-OCU/E&M 
No 
No 
N/A 

## Standards Compliance  *(p.348)*


## Functional Description  *(p.348)*


## Factory Defaults  *(p.348)*


## Configuring Serial Port Parameters  *(p.348)*

5. Cards and Ports 
Standards Compliance 
The Megaplex-4 serial ports comply with following standards: V.35, V.11/RS-422, V.24/ EIA RS-232, ITU-T 
Rec. V.110.  
Functional Description 
See Chapter 13.  
Factory Defaults 
Megaplex-4 is supplied with all serial ports disabled. Other parameter defaults are listed in the table 
below. 
Parameter  
Default Value 
rate 
1 x 64kbps 
mode 
sync 
encapsulation-mode  
none  
cts-rts 
no cts-rts (disabled) 
end-to-end-control 
no end-to-end-control (disabled) 
data-bits  
8  
parity  
no parity (disabled) 
stop-bits  
1 
interface  
v35  
s-bit-signaling 
off 
data-position  
F:0 B:1 
Configuring Serial Port Parameters  
 To configure the serial port parameters: 
1. Navigate to configure port serial <slot>/<port> to select the serial port to configure. 
5. Cards and Ports 
The config>port>serial>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
Assigning short description to 
port 
name <string> 
Using no name removes the name 
Administratively enabling 
port 
no shutdown 
Using shutdown disables the port 
Selecting the data rate 
VS (encapsulation-
mode=none): rate {1 | 2 | 3 | 
4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 
12 | 13 | 14 | 15 | 16 | 17 | 18 
| 19 | 20 | 21 | 22 | 23 | 24 | 
25 | 26 | 27 | 28 | 29 | 30 | 
31} x {56kbps | 64kbps} 
The data rate of the serial port of VS-6/703 and 
PW-enhanced VS voice modules protected by 
DS0-SNCP is limited to 1792K (28*64 kbps).  
 
VS (encapsulation-
mode=v110): rate {2.4 | 4.8 | 
9.6 | 19.2 | 38.4 }  
 
VS (encapsulation-
mode=hcm): rate {2.4 | 4.8 | 
9.6 | 19.2 | 38.4 } 
With this encapsulation mode, each channel 
always occupies one timeslot (64 kbps) 
 
VS (encapsulation-
mode=r111): rate {2.4 | 4.8 | 
9.6 | 19.2 } 
For more information, see Configuring the 
Rates with R.111 Encapsulation in Chapter 13. 
VS (encapsulation-mode=3bit-
transitional) : rate {1 | 2 } x 
64kbps 
 
VS-OCU/E&M: rate {56 | 72 } 
 
Activating E2E S-Bit transport 
s-bit-signaling {on | off} 
Applicable only when encapsulation-mode is 
HCM 
Define location of the data 
channel inside HCM frame 
data-position F {0..9} B {0..7} 
Applicable only when encapsulation-mode is 
hcm.  
Selecting the port 
transmission mode  
mode {sync | async}  
This command is relevant only for v110 and 
hcm encapsulation modes. 
Selecting the encapsulation 
mode for the VS modules  
encapsulation-mode {v110 |  
3bit-transitional | none | hcm 
| r111} 
This parameter defines the serial port 
behaviour of VS modules (see diagram in 
Chapter 13, Encapsulation Modes).  
5. Cards and Ports 
Task 
Command  
Comments 
Enabling conference 
functionality (VS-6/BIN only)  
conference  
Using no conference disables the conference 
functionality. 
Setting CTS line to track the 
state of the local RTS line 
cts-rts 
Using no cts-rts sets the CTS line continously to 
on. 
Configuring end-to-end 
control   
 
end-to-end-control 
 
When configured, the state of the local RTS 
and DTR lines are reflected by the remote DCD 
and DSR line, respectively.  
Using no end-to-end-control disables end-to-
end control.  
When encapsulation-mode=3bit-transitional, 
only the state of the local RTS line can be 
transmitted end-to-end to the remote DCD 
line, but not local DTR to the remote DSR. The 
RTS line is functioning as follows: 
• RTS on: traffic flow is established to the  
remote equipment, remote DCD on  
• RTS off - 0xC0 code is sent to remote 
equipment, remote DCD off 
In VS modules, DTR and DSR lines are relevant 
only for the following encapsulation modes: 
• v110 
• hcm when s-bit-signaling is on. 
In VS modules, for encapsulation-mode=none 
this selection is available only for n x 56 kbps 
data rates. For n x 64 kbps data rates, see the 
next table row. 
Configuring end-to-end 
control (VS, encapsulation-
mode=none, n x 64 kbps data 
rates, serial port is cross-
connected to E1 uplink with 
G.732S or G.732S-CRC 
framing) 
end-to-end-control [rts | 
inverse-rts] 
 
  
This selection is unavailable for VS E1/T1 
modules. 
When configured, the state of the local RTS line 
is reflected by the remote DCD line.  
For end user devices using negative logic 
interpretation, use inverse-rts setting.  
For end user devices using positive logic 
interpretation (this is a normal usage case), use 
end-to-end-control rts setting or simply end-
to-end-control  (rts is set by default).  
Using no end-to-end-control disables end-to-
end control.  

## Viewing Status Information  *(p.351)*

5. Cards and Ports 
Task 
Command  
Comments 
Selecting the number of data 
bits in the asynchronous 
word format  
data-bits {5 | 6 | 7 | 8} 
 
This command is relevant only for v110 and 
hcm encapsulation modes  
Controlling the  
end-to-end transfer of the 
parity bit in the asynchronous 
word format 
parity  
 
Using no parity means that the parity bit is not 
transferred 
This command is relevant only for 
encapsulation mode=v110 
Selecting the number of stop 
bits in the asynchronous 
word format  
stop-bits {1 | 2}  
 
 
Setting the physical interface 
type  
interface {rs-232 | v35 | 
rs-422}  
 
Viewing Status Information  
 To view the status of a VS serial port: 
1. Navigate to config>port> serial (<slot>/<port>)#  
2. Type show status. 
The status is displayed, for example as follows:  
config>port>serial(3/7)# show status 
Name                  : IO-3 serial 07 
Administrative Status : Up 
Operation Status      : Up 
Loopback Type         : None 
 
RTS : High 
CTS : High 
DCD : High 
DTR : Low 
DSR : High 
The status display provides information about: 
 
Administrative and operational status  
 
Loopback Type – Status of loopback activated on the port (None, Local, Remote) 
 
State of control signals (High/Low) 
When using the HCM encapsulation, the following additional parameters are displayed in the 
status screen:  

## Displaying VS Serial Port Statistics  *(p.352)*

5. Cards and Ports 
 
Frame synchronization, local and remote (LOS/In Sync)  
 
SSF – State of local S-bit synchronization (Disabled/LOS/In Sync)  
 
State of remote RTS and DTR control signals (High/Low) 
config>port>serial(3/7)# show status 
Name                  : IO-3 serial 07 
Administrative Status : Up 
Operation Status      : Up 
Loopback Type         : None 
 
RTS: High 
 
F Sync     : In Sync  
CTS: High 
 
SSF        : In Sync 
DCD: High 
 
Rem F Sync : In Sync 
DTR: Low 
 
Rem RTS    : High 
DSR: High 
 
Rem DTR    : High 
 
 
 
Displaying VS Serial Port Statistics  
Serial ports feature RAD proprietary statistical diagnostics. This feature is available for the following 
encapsulation modes: 
• 
3bit-transitional 
• 
HCM 
• 
R.111. 
 To display the statistics of a serial port: 
1. Navigate to config>port> serial> (<slot>/<port>)#  
2. Type show statistics. 
The statistics is displayed, for example as follows:  
# config port serial 3/3 
config>port>serial(3/3)# show statistics 
DTE Rx Counter   : 609087 
DTE Tx Counter   : 0 
WAN Rx Violation : 0 
  VS Module Serial Port Statistics Parameters  
Parameter 
Description 
DTE Rx Counter  
  
Number of data transitions on the input data wires since last reset or power-up (Rx from 
DTE)  

## Configuration Errors  *(p.353)*

5. Cards and Ports 
Parameter 
Description 
DTE Tx Counter    
Number of data transitions on the output data wires since last reset or power-up (Tx to 
DTE)  
WAN Rx Violation 
(3-bit transitional 
only) 
Number of 3-bit transitional protocol code violation since last reset or power-up  
HCM F bit errors 
(hcm only) 
Number of errors in the Framing bit since last reset or power-up 
 
 To clear the statistics on a serial port: 
1. Navigate to the corresponding port. 
2. Enter clear-statistics. 
The statistics for the specified port are cleared. 
Configuration Errors  
The tables below list messages generated by Megaplex-4 when a configuration error on modules with 
serial ports is detected. 
  
Code 
Type 
Syntax 
Meaning 
768 
Error 
PORT ENCAPSULATION MODE 
NOT SUPPORTED ON CARD 
 
HCM and R.111 encapsulation modes for serial interface are 
not supported in the following modules: 
• VS-6/E1T1 modules  
• VS-G703 
• VS-6-FXS-PW-ACR  
• VS-6-FXO-PW-ACR 
• VS-6-EM-PW-ACR  
810 
Error 
E2E CONTROL / 
ENCAPSULATION-MODE 
MISMATCH 
When serial port encapsulation mode is v110, 3-bit-
transitional or hcm, end-to-end-control  inverse-rts is illegal 
(use end-to-end-control  rts). 
811 
Error 
E2E CONTROL / XC LINK LINE-
TYPE MISMATCH 
When serial port encapsulation mode is none, port rate is 
Nx64Kbps and end-to-end-control is enabled, the only 
possibility of serial port cross-connect is E1 link with either 
g732s or g732s-crc line-type)  

## Testing Serial Ports  *(p.354)*

5. Cards and Ports 
Code 
Type 
Syntax 
Meaning 
817 
Error 
PORT RATE / CONFERENCE 
MODE MISMATCH 
 
For VS-6/BIN module with encapsulation-mode = 3-bit-
transitional and conference mode activated, port rate can 
be 1x64Kbps only.  
818 
Error 
 
ILLEGAL PORT RATE FOR 
DS0-GROUP SUPPORT 
 
The data rate of the serial port of VS-6/703 and 
PW-enhanced VS voice modules protected by DS0-SNCP is 
limited to 1792K (28*64 kbps).  
819 
Error 
ILLEGAL CONFERENCE MODE 
FOR BOUND PORT 
A serial port cannot be bound to a tdm-bridge when it is set 
to conference mode.  
 
Testing Serial Ports  
The following test and diagnostics functions are available on each serial port: 
• 
Local digital loopback  
• 
Remote digital loopback  
• 
CSU Loopback (for OCU ports only) 
Local Digital Loopback (Local Loop) 
The local loopback is a digital loopback performed at the digital output of a selected channel, by 
returning the transmit signal of the channel in the same timeslot of the receive path. The transmit signal 
is still sent to the remote Megaplex unit.  
While the loopback is connected, the local serial port should receive its own signal. 
The loopback signal path is shown below.  
 
 
 
 
 
5. Cards and Ports 
NMS
Megaplex-4
User or Test
Equipment
Local Site
Remote Site
Megaplex-4
VS-12
User or Test 
Equipment
VS-12
 
Remote Digital Loopback (Remote Loop)  
The remote loopback is a digital loopback performed at the digital input of the channel, by returning the 
digital received signal of the channel to the input of the transmit path. The receive signal remains 
connected to the local user and can be received by user.  
While the loopback is connected, the remote serial port should receive its own signal. 
The loopback signal path is shown below. 
NMS
Megaplex-4
User or Test
Equipment
Local Site
Remote Site
Megaplex-4
VS-12
User or Test 
Equipment
VS-12
 
CSU (Mandatory) Loopback   
The CSU loopback, also called “mandatory loopback” (“remote-on-remote” in the CLI) is a remote 
loopback on the CSU section of a CSU/DSU unit connected to the channel.  
The loopback is initiated by the user (from the terminal or management system). This loopback can be 
initiated by means of the local channel, or by the corresponding channel of the remote system 
Megaplex. 
When a CSU loopback activation command is applied to an OCU module channel, the channel reverses 
the polarity of the sealing loop current: 
5. Cards and Ports 
• 
The loop current normally flows from the positive pole of the loop current source (located in the 
OCU module), through the receive pair and the line side of the customer CSU/DSU into the 
transmit pair, and then back through the transmit line into the minus pole of the source.  
• 
When the OCU module channel reverses the current polarity, the CSU section of the customer 
CSU/DSU will enter the loopback state for as long as the polarity reversal is maintained. 
While the loopback connection is active, the remote user (located at the remote end of the Megaplex 
uplink) can transmit test patterns and check the returned signal.  
Since inside the customer CSU/DSU equipment the loopback connection is made as close as possible to 
the DDS line connection, this loop is generally used to sectionalize a fault between the user’s premises 
and the DDS transmission plant. 
The implementation of this loopback is mandatory, hence its name. 
The loopback signal paths are shown below. 
NMS
Megaplex-4
User’s
Equipment
Central Site
Remote Site
Megaplex-4
OCU-DP
User or Test 
Equipment
CSU 
Loopback
OCU-DP
 
CSU (Mandatory) Loopback, Signal Path 
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the Megaplex-4. 
Therefore, when you initiate a loopback, you have the option to limit its duration to an interval in the 
range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-4 before 
this timeout expires. When using inband management, always use the timeout option; otherwise, the 
management communication path may be permanently disconnected. 
The default is infinite duration (without timeout). 