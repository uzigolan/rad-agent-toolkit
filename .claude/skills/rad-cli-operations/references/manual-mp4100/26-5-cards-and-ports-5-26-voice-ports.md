# 5 Cards and Ports – 5.26 Voice Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 467–484.*


## Applicability and Scaling  *(p.467)*

5. Cards and Ports 
5.26 Voice Ports  
Applicability and Scaling 
Voice ports are available on the following modules: 
• 
VC-4, VC-8 and VC-16 
• 
VC-4A, VC-8A 
• 
VS voice modules (VS-6/FXS, VS-6/FXO, VS-6/E&M, VS-8/E&M and FXS/E&M) 
• 
PW-enhanced VS voice modules (VS-6/FXS/PW, VS-6/FXO/PW and VS-6/E&M/PW  
Note 
When the information is applicable to both basic and advanced version of the 
module, the basic name (such as VS-6/FXS) is used in this manual.  The 
complete designation is used only for information applicable to a specific PW-
enhanced version. 
The following table shows the number of voice ports on each Megaplex-4 I/O module. 
Megaplex-4 Voice Ports 
Module  
Number of Ports 
VC-4A/8A  
4/8  
VC-4/8/16 
4/8/16 
VS-6/FXS, VS-6/FXS/PW 
8 
VS-6/FXO, VS-6/FXO/PW 
8 
VS-6/E&M, VS-6/E&M/PW 
4  
VS-8/E&M 
8 
FXS/E&M 
8(FXS)+4(E&M) 
Analog voice interface modules, VC-4, VC-8 and VC-16, provide 4, 8 or 16 PCM-encoded toll-quality 
voice channels (ports). The modules are available in three models: 
• 
E&M: 4-wire or 2-wire interfaces with E&M signaling per RS-464 Types I, II, III and V, and BT 
SSDC5.  
• 
FXS: 2-wire interfaces for direct connection to telephone sets.  
• 
FXO: 2-wire interfaces for direct connection to PBX extension lines 

## Standards Compliance  *(p.468)*

5. Cards and Ports 
VC-4A and VC-8A modules are analog voice interface module similar to VC-4 and VC-8, except that they 
also support ADPCM. 
The VS voice modules (VS-6/FXS, VS-6/FXO, VS-6/E&M, VS-8/E&M and FXS/E&M) provide 8 FXS, 8 FXO, 8 
E&M or 4 E&M toll-quality analog voice channels. 
The following parameters can be configured for the voice ports:  
• 
Port name 
• 
Administrative status 
• 
End-to-end signaling transfer method  
• 
Pulse metering frequency for FXO/FXS channels (VC modules only) 
• 
Number of wires for E&M channels 
• 
Specifying the compression method used in the ADPCM encoding.  
• 
Analog signaling method for FXO/FXS channels 
• 
Analog signaling profile (VS voice modules only) 
• 
E&M signaling standard  
• 
Impedance for FXS and FXO modules (VS voice modules only) 
• 
Cadence for FXS and FXO modules (VS voice modules only) 
Standards Compliance 
The Megaplex-4 voice ports comply with following standards:  
Modulation Technique  
 
PCM: per ITU-T Rec. G.711 and AT&T Pub. 43801 
ADPCM: per ITU-T G.726 and G.727 
Echo Cancellation 
ITU-T G.168  
Analog Interface 
ITU-T Rec. G.712 
E&M Signaling Method  
EIA RS-464 Type I 
EIA RS-464 Type II, III and V (British Telecom SSDC5) using 
internal -12 VDC in place of -48 VDC 
FXS/FXO Signaling Modes  
EIA RS-464 loop-start and wink-start 

## Functional Description  *(p.469)*

5. Cards and Ports 
End-to-End Signaling for E1 
Uplinks 
User-selectable as per ITU-T Rec. G.704, para. 3.3.32 
Functional Description 
All the VC/VS voice modules provide high-quality voice channels. The functional difference between the 
various modules is in the signaling interface and mode.  
The analog interface depends on the module type: 
• 
VC-4/4A/8/8A/16 E&M modules: user-selectable for 2-wire or 4-wire 
• 
VC-4/4A/8/8A/16 FXS/FXO modules: always 2-wire 
• 
E&M submodules of VS voice modules: user-selectable for 2-wire or 4-wire 
• 
FXS/FXO submodules of VS voice modules: always 2-wire 
Voice encoding method for all VC-4A and VC-8A module versions is user-selectable for either toll-quality 
64 kbps PCM or 32/24 kbps ADPCM. The VC-4, VC-8, VC-16,  VS-6/E&M, FXS/E&M, VS-6/FXS, and VS-
6/FXO modules feature only PCM encoding. 
The user can select the companding law, µ-law or A-law, in accordance with system requirements. In 
accordance with ITU-T Rec. G.711, the A-law should be used on E1 trunks and the µ-law should be used 
on T1 trunks. However, the user can select the desired companding law, µ-law or A-law, in accordance 
with the specific system requirements. 
To increase application flexibility, the nominal audio transmit and receive levels of all the module 
versions can be adjusted over a wide range:  
Transmit and Receive Levels for Various Interfaces  
Module Interface 
Transmit 
[dbm] 
          min               max 
Receive 
[dbm] 
         min               max 
VC modules 
 
 
 
 
E&M regular 2-wire 
-8  
+5 
-17 
+2 
E&M regular 4-wire 
-8  
+5 
-17 
+3.5 
E&M 4W enhanced  
-17 
+5 
-17 
+9 
FXS 
-5 
+5 
-17 
+1 

## Factory Defaults  *(p.470)*

5. Cards and Ports 
Module Interface 
Transmit 
[dbm] 
          min               max 
Receive 
[dbm] 
         min               max 
LB 
-17 
+8 
-23 
+2 
FXO 
-3.5 
+5 
-17 
+1 
VS voice modules  
 
 
 
 
E&M 2W  
-8 
+5 
-17 
+2 
E&M 4W (when there is a mix 
of 2W/4W ports: within groups 
1..4 or 5..8) 
-8 
+5 
-17 
+3.5 
E&M 4W (all connected ports) 
-17 
+5 
-17 
+9 
FXS/FXO  
-5 
+5 
-17 
+1 
Due to the high quality audio reproduction, DTMF signaling is transparently transferred, inband. 
Therefore, the user can use DTMF signaling as usual, e.g., can operate the telephone set keypad to 
access voice mail systems, interactive systems, etc.  
The VC-4A and VC-8A modules use G.168 standard for echo cancellation (up to 4 ms per channel).  
For VS voice modules, pulse metering frequency is not supported. 
For more information, see also the following:  
• 
VC-4/VC-4A/VC-8/VC-8A/VC-16 section Chapter 14 
• 
VS Voice section Chapter 13.  
Factory Defaults 
Megaplex-4 is supplied with all voice ports disabled. Other parameter defaults are listed in the table 
below. 
Parameter  
Default Value 
coding 
a-law 
signaling  
no signaling (disabled)  
analog-signaling-profile 
sig_over_a_bit 
meter-rate  
12khz  

## Configuring External Voice Port Parameters  *(p.471)*

5. Cards and Ports 
Parameter  
Default Value 
wires  
2  
compression  
no compression (disabled) 
analog-signaling  
loop-start  
e-m-type  
ssdc5  
echo-canceler  
no echo-canceler (disabled) 
operation-mode  
ptp  
signaling-feedback 
no signaling-feedback (disabled)  
tx-gain  
0 dbm 
rx-sensitivity  
0 dbm 
impedance 
600 
cadence 
local 
loop-disconnect-time 
250msec 
forward-disconnect  
250msec 
duration 
infinite 
disconnect-tone 
no disconnect-tone (disabled)  
activity-detection  
disabled  
ring-voltage  
normal 
Configuring External Voice Port Parameters  
The sets of configurable parameters are different for voice ports of VC modules and VS voice modules. 
 To configure the external voice port parameters for VC modules: 
1. Navigate to configure port voice <slot>/<port> to select the voice port to configure. 
The config>port>voice>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
5. Cards and Ports 
Task 
Command  
Comments 
Assigning short 
description to port 
name <string> 
Using no before name removes the name 
Administratively enabling 
port 
no shutdown 
Using shutdown disables the port 
Specifying the 
companding law to be 
used by the voice channels  
coding {a-law | u-law} 
 
a-law  - A-law coding, intended for use on E1 
links 
u-law -µ-law coding, intended for use on T1 
links        
Specifying the end-to-end 
signaling transfer method 
for voice modules 
 
signaling {rbmf | cas | rbf} 
 
The signaling transfer options depend on the 
type of link module installed in the Megaplex 
chassis:  
• with T1 link modules, RBMF and RBF is 
used 
• with E1 link modules, CAS and RBF is used 
rbf – proprietary “robbed bit” signaling 
method that does not require multiframe 
synchronization, used as follows: 
• 7-bit PCM with channel signaling carried 
by the 8th bit of each channel  
• 3-bit ADPCM with channel signaling 
carried by the 4th bit of each channel 
when using G.727 
For VC family modules, the RBF option is used 
for VC-4A/VC-8A only.  
rbmf – robbed bit signaling in accordance 
with AT&T Pub 43801. 
cas – Channel-associated signaling in 
accordance with ITU-T Rec. G.704. 
Using no signaling  means that channel 
signaling is not transferred  
Specifying the pulse 
metering frequency  
meter-rate { 16khz | 12khz }  
This feature is supported only on FXS and FXO 
modules in PCM mode 
Specifying the interface to 
be used by the voice 
channels 
 
wires {2 | 4}  
Selection between 2-wire and 4-wire 
interface is available only for the 
VC-4/4A/8/8A/16 E&M modules. Can be 
independently selected for each pair of 
channels (1, 2; 3, 4; etc.).  
5. Cards and Ports 
Task 
Command  
Comments 
Specifying the 
compression method used 
in the ADPCM encoding 
 
compression {g726 | g727} 
Always use G.727 when working with RBF or 
RBMF signaling. 
If PCM encoding is used, a sanity error is sent.  
Using no compression  disables compression  
Specifying the analog 
signaling method used for 
all FXO/FXS channels  
analog-signaling {loop-start | wink-start}  
Can be selected only for FXO and FXS 
modules operated in PCM mode.  
For VC-4, VC-4A, VC-8 and VC-8A modules, 
the selection is made for the entire group of 
all the module channels. For VC-16 modules, 
the selection can be separately made for each 
group of eight channels: 1 to 8 and 9 to 16. 
Specifying the E&M 
signaling standard 
e-m-type {1 | 2 | 3 | ssdc5}  
This selection is available only for E&M 
modules. The E&M signaling type can be 
independently selected for each group of four 
channels 1, 2, 3, 4; 5, 6, 7, 8; etc.). 
Note: For the E&M/POS module, select 2 
only. 
Enabling the built-in 
adaptive echo canceller, 
supporting up to a 4 msec 
delay 
echo-canceler  
This option is relevant only for VC-4A and VC-
8A modules. 
Using no before echo-canceler disables echo 
canceling  
Controlling the use of 
signaling feedback for FXO 
modules 
signaling-feedback  
 
Available only for FXO modules. 
For VC-4, VC-4A, VC-8 and VC-8A, the 
selection should be the same for all the 
module channels. For VC-16 modules, the 
selection can be separately made for each 
group of eight channels: 1 to 8 and 9 to 16. 
This is done by forcing the last choice 
(signaling-feedback/no signaling-feedback) 
to all the module/group ports. 
Using no before signaling-feedback disables 
the signaling feedback.  
Selecting the nominal 
input level of the transmit 
path 
tx-gain <value in dbm>  
The input level can be set in 0.5 dB steps in 
the range of +8 dBm to -17 dBm, depending 
on the module type (see above). 
Selects the nominal 
output level of the receive 
path 
rx-sensitivity <value in dbm> 
The output level can be set in 0.5 dB steps in 
the range of +9 dBm to -23 dBm, depending 
on the module type (see above.) 
5. Cards and Ports 
Task 
Command  
Comments 
Enabling the “end of 
speech” signal (short 
tones) on hanging up on 
the partner side  
disconnect-tone   
 
FXS modules only 
Using “no disconnect-tone” disables the tone  
 To configure the external voice port parameters for VS voice module: 
1. Navigate to configure port voice <slot>/<port> to select the voice port to configure. 
The config>port>voice>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
Assigning short 
description to port 
name <string> 
Using no before name removes the name 
Administratively enabling 
port 
no shutdown 
Using shutdown disables the port 
Specifying the 
companding law to be 
used by the voice channels  
coding {a-law | u-law} 
 
a-law  - A-law coding, intended for use on E1 
links 
u-law -µ-law coding, intended for use on T1 
links        
Specifying the end-to-end 
signaling transfer method 
for voice modules 
 
signaling {rbmf | cas | rbf} 
 
The signaling transfer options depend on the 
type of link module installed in the Megaplex 
chassis:  
• with T1 link modules, RBMF and RBF is 
used 
• with E1 link modules, CAS and RBF is used
 
 
RBF is a proprietary “robbed bit” signaling 
method that does not require multiframe 
synchronization, it is supported by E&M 
module only. 
Using no signaling  means that channel 
signaling is not transferred 
5. Cards and Ports 
Task 
Command  
Comments 
Specifying the interface to 
be used by the voice 
channels 
wires {2 | 4}  
Selection between 2-wire and 4-wire 
interface is available only for the E&M 
modules.  
Can be independently selected for each 
channel. 
Specifying the analog 
signaling method used for 
all FXO/FXS channels 
analog-signaling {loop-start | wink-start}  
Can be selected only for FXO and FXS 
modules 
Configuring VAD to 
indicate whether E&M 
interface is active or not  
[no] activity-detection    
Available only for VS E&M modules  
Specifying the E&M 
signaling standard 
e-m-type {1 | 2 | 3 | ssdc5 | positive}  
This selection is available only for E&M 
modules.  
The E&M signaling type can be independently 
selected for each group of four channels 1, 2, 
3, 4; 5, 6, 7, 8; etc.) 
Controlling the use of 
signaling feedback for FXO 
modules 
signaling-feedback  
 
This parameter is available only for FXO 
modules and is needed when FXO is working 
opposite E&M interface. 
Using no before signaling-feedback disables 
the signaling feedback.  
Selecting the nominal 
input level of the transmit 
path 
tx-gain <value in dbm>  
The input level can be set in 0.5 dB steps in 
the range of +5 dBm to -17 dBm, depending 
on the module type (see table Transmit and 
Receive Levels for Various Interfaces). 
Selects the nominal 
output level of the receive 
path 
rx-sensitivity <value in dbm> 
The input level can be set in 0.5 dB steps in 
the range of +9 dBm to -17 dBm, depending 
on the module type (see table Transmit and 
Receive Levels for Various Interfaces). 
Specifying the analog 
signaling profile 
analog-signaling-profile <profile-name> 
By default the analog signaling profile shall be 
sig_over_a_bit 
Specifying the line 
impedance 
impedance {600 | 900} 
Available only for FXS/FXO modules 

## Example  *(p.476)*

5. Cards and Ports 
Task 
Command  
Comments 
Specifying if the cadence 
of the ring is generated 
locally or translated 
directly from the received 
signaling bit 
cadence {local | transparent} 
Available only for FXS/FXO modules 
Specifying the amount of 
time during which the 
battery voltage is 
disconnected by the FXS 
port after a far-end 
notification has been 
received 
forward-disconnect {250msec | 500msec | 
750msec | 1sec | 2sec} 
Available only for FXS modules 
Specifying the amount of 
time of momentary 
battery voltage removal 
that will be detected by 
the FXO port  
loop-disconnect-time {250msec | 500msec 
| 750msec | 1sec | 2sec} 
Avaliable only for FXO modules 
Specifying the ring voltage 
value 
ring-voltage {normal | high} 
Available only for FXS ports: 
• normal – 54 Vrms 
• high – 85 Vrms 
For each pair of FXS ports (1..2, 3..4, 5..6, 7..8) 
- once one of the ports is configured with a 
Ring Voltage value of 'high', the second port 
shall be set to shutdown. 
Example  
The following section illustrates how to configure the voice FXS port 1 on the VC-8 module installed in 
slot 9: 
• 
Set -µ-law coding 
• 
Set CAS signaling 
• 
Administratively enable the port 
• 
Leave all other parameters disabled or at their defaults. 
config# #----------vc8fxs----------------- 
config# port voice 9/1 no shutdown 
config# port voice 9/1 coding u-law  

## Configuration Errors  *(p.477)*

5. Cards and Ports 
config# port voice 9/1 signaling cas 
Configuration Errors 
The following tables list messages generated by Megaplex-4 when a configuration error on voice 
modules is detected. 
VC and VS Voice Modules Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
170 
Error 
ILLEGAL SIGNALING METHOD 
You can select the channel associated signaling method only 
when an E1 module port with G.732S framing is used. 
You can select the robbed bit multiframe signaling transfer 
method only for E1 links with G.732S framing, or on T1 links. 
171 
Warning VOICE CODING LAW (E1/T1) 
MISMATCH 
The selected voice companding law differs from the 
companding law specified by the standards: the A-law is 
generally used for E1 links, and the µ-law is generally used 
on T1 links 
172 
Error 
TX GAIN VALUE OUT OF RANGE  The transmit gain selected for the specified channel is not 
within the supported range 
173 
Error 
RX SENSITIVITY VALUE OUT OF 
RANGE  
The receive sensitivity (gain) selected for the specified 
channel is not within the supported range  
174 
Error 
OOS/INTERFACE MISMATCH 
The selected OOS mode cannot be used on this type of 
interface   
175 
Error 
SIGNALING 
PROFILE/INTERFACE 
MISMATCH 
The selected profile cannot be used on this type of interface  
176 
Error 
ILLEGAL NUMBER OF WIRES 
Voice modules with /FXO and /FXS interfaces support only 
the two-wire interface. 
For voice modules with /E&M interface only, it is possible to 
select two-wire or four-wire interfaces. In addition, for VC-
4/4A/8A/16 modules with /E&M interface, the same 
interface type must be selected for consecutive pairs of 
channels (for example, 1, 2 or 15, 16)  
177 
Error 
NO SIGNALING IS ILLEGAL FOR 
THIS INTERFACE 
The selected interface cannot be used with no signaling –the 
signaling option must be specified 

## Viewing a Voice Port Status  *(p.478)*

5. Cards and Ports 
Code 
Type 
Syntax 
Meaning 
179 
Error 
ILLEGAL ANALOG SIG 
COMBINATION  
 
For VC-4, VC-4A, VC-8 and VC-8A modules, the selection of 
analog-signaling parameter must be made for the entire 
group of all the module channels. For VC-16 modules, the 
selection can be separately made for each group of eight 
channels: 1 to 8 and 9 to 16. 
180 
Error 
ILLEGAL FXO SIG FEEDBACK 
COMBINATION        
For VC-4, VC-4A, VC-8 and VC-8A modules, the selection of 
signaling-feedback parameter must be made for the entire 
group of all the module channels. For VC-16 modules, the 
selection can be separately made for each group of eight 
channels: 1 to 8 and 9 to 16. 
181 
Error 
ILLEGAL TS SPLIT CONFIG FOR 
ADPCM MODE 
Split timeslot cross-connect must be peformed on a pair of 
ports (1,2 or 3,4..)  
182 
Error 
TX/RX GAIN LEVEL MUST BE 
SET IN 0.5 dB STEPS 
Step value is not legal for VS voice modules. 
750 
Error 
NUM OF BI-DIRECTION-RX TS 
EXCEEDS 30 
The number of bidirection-rx timeslots cross-connected to 
the voice port in VS voice modules cannot exceed 30.  
763 
Error 
SERIAL PORT/PW BANDWIDTH 
MISMATCH 
In VS modules, the serial port rate must match the number 
of timeslots on this serial port listed in the cross-connect 
pw-tdm command. 
764  
 
Error 
ILLEGAL RING VOLTAGE/PORTS 
ADMIN COMBINATION 
For each pair of channels (1-2, 3-4, 5-6 or 7-8) only one 
channel can be set to 'high' ring voltage. 
Viewing a Voice Port Status 
Follow the instructions below for viewing the status of a voice port. 
 To view the voice port status: 
• 
At the config>port>voice(<slot>/<port>)# prompt, enter show status.  
The status information appears as illustrated below.  
config>port>voice(7/1)# show status 
Name                  : IO-7 voice 01 
Administrative Status : Up 
Operation Status      : Down 
HW Type               : IO-7 voice 01 
Loopback Type         : None 
 
Interface Type : E&M 

## Testing Voice Ports  *(p.479)*

5. Cards and Ports 
Rx ABCD        : 0101 
Tx ABCD        : 0101 
The status display provides information about: 
 
Administrative status  
 
Operational status (for E&M modules Up corresponds to the voice activity on the channel (in 
the case VAD (voice activity detection) is enabled) 
 
Status of loopback activated on the port (None, Local, Remote, Local Tone Injection, Remote 
Tone Injection) 
 
Interface type and signaling bits (VS modules only) 
 
Module hardware type according to the following table: 
VC Module Hardware Types  
Displayed String 
Module Description 
Ordering Option 
 
"FXS RP MP" 
Reverse polarity & Metering 
FXS/MET, 
FXS/RJ/MET 
 
"FXS RP NO MP" 
Reverse polarity & No Metering 
FXS, FXS/RJ 
 
“FXO RP MP" 
Reverse polarity & Metering 
FXO/MET, 
FXO/RJ/MET 
 
"FXO RP NO MP"  
Reverse polarity & No Metering 
FXO, FXO/RJ 
 
"EM 4W EXT GAIN” 
4W only, with enhanced gain 
levels  
E&M/4WIRE 
 
"EM 2W/4W"         
Regular 2w & 4w 
E&M, E&M/EXT 
 
"EM 2W/4W DS"            
Double Signaling 
E&M/DS 
 
"EM 2W/4W POS 5/12 V" 
Positive signaling voltage, 5/12V 
E&M/POS  
 
"EM 2W/4W POS 24V" 
Positive signaling voltage, 24V 
E&M/RJ/POS/24 
 
Testing Voice Ports 
The test and diagnostics functions available on each voice channel are: 
• 
Local digital loopback  
• 
Remote digital loopback  
• 
Forward tone injection 
• 
Backward tone injection. 
5. Cards and Ports 
Local Digital Loopback (Local Loop) 
The local loopback is a digital loopback performed at the digital output of a selected channel, by 
returning the transmit signal of the channel in the same timeslot of the receive path. The transmit signal 
is still sent to the remote Megaplex unit.  
While the loopback is connected, the local voice channel should receive its own signal, e.g., a strong 
sidetone should be heard in the earpiece if the channel is connected to a telephone set. 
The loopback signal path is shown below. 
Local
Unit
Remote
Unit
User or
Test
Equipment
User or
Test
Equipment
VC-16
I/O Modules
Channel 1
.....
.....
.....
...
VC-16
I/O Modules
System
Management
...
 
 
Note 
When working in the ADPCM mode, the local digital loopback towards the 
local user equipment is performed for each pair of consecutive channels (1-2, 
3-4, etc.) 
Remote Digital Loopback (Remote Loop) 
The remote loopback is a digital loopback performed at the digital input of the channel, by returning the 
digital received signal of the channel to the input of the transmit path. The receive signal remains 
connected to the local user, and can be received by user.  
5. Cards and Ports 
While the loopback is connected, the remote voice channel should receive its own signal, e.g., a strong 
sidetone should be heard in the earpiece if the channel is connected to a telephone set. 
The loopback signal path is shown below. 
Local
Unit
Remote
Unit
User or
Test
Equipment
VC-16
I/O Modules
VC-16
I/O Modules
User or
Test
Equipment
Channel 1
.....
.....
.....
System
Management
.......
 
Forward Tone Injection 
The test tone is a data sequence repeating at a rate of 1 kHz. This data sequence is identical to the data 
sequence that would have been generated if a 1-kHz signal having a nominal level of 1 mW (0 dBm0) 
were applied to the input of the channel codec. 
The tone is injected to the local transmit path multiplexer, instead of the transmit signal of the channel. 
The signal received from the other end remains connected to the local subscriber. 
While the forward tone injection is activated, the remote user should hear the tone in the earpiece if the 
channel is connected to a telephone set. 
The following figure shows the signal path. 
5. Cards and Ports 
Local
Unit
Remote
Unit
User or
Test
Equipment
VC-16
I/O Modules
I/O Modules
User or
Test
Equipment
Channel 1
.....
.....
.....
~ Test
Tone
VC-16
.......
System
Management
 
Backward Tone Injection 
When the backward test tone injection is enabled, the test tone (a data sequence repeating at a rate of 
1 kHz) is injected to the local receive input of the channel decoder, instead of the received signal of the 
channel, and the resulting analog signal is supplied to the local subscriber. The signal received from the 
other end is disconnected from the local subscriber. 
While the backward tone injection is activated, the local user should hear the tone in the earpiece if the 
channel is connected to a telephone set. 
The following figure shows the signal path. 
5. Cards and Ports 
Local
Unit
Remote
Unit
User or
Test
Equipment
VC-16
I/O Modules
I/O Modules
User or
Test
Equipment
Channel 1
.....
.....
.....
Test
Tone
VC-16
.......
System
Management
 
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the Megaplex-4. 
Therefore, when you initiate a loopback, you have the option to limit its duration to an interval in the 
range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-4 before 
this timeout expires. When using inband management, always use the timeout option; otherwise, the 
management communication path may be permanently disconnected. 
The default is infinite duration (without timeout). 
Activating Loopbacks and Tone-Inject Tests  
 To perform a loopback on the voice port: 
1. Navigate to configure port voice <slot>/<port> to select the voice port to configure. 
The config>port>voice>(<slot>/<port>)# prompt is displayed.  
5. Cards and Ports 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Activating and 
configuring the 
direction of the 
loopback and the 
duration of it (in 
seconds) 
loopback {local | remote} [tone-inject] 
[duration <duration in minutes 1..30> ] 
  
local – local loopback 
remote – remote loopback 
local tone-inject – backward tone 
injection  
remote tone-inject – forward tone 
injection  
 
 
 
 
 