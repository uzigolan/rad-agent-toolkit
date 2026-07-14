# 5 Ports

*Manual `MP-1-mn_ver 2.2.pdf`, pages 142–215.*


## 5.1 Port-Related Profiles  *(p.142)*

5.1 Port-Related Profiles 
Analog Signaling Profiles 
This feature is available for the Megaplex-1 voice ports. 
The maximum number of analog signaling profiles is 4: two are predefined (read-only) and another two 
can be created/defined by the user. 
Functional Description 
Analog voice signals are digitized using PCM (Pulse-code modulation), in compliance with ITU-T G.711 
and AT&T Pub. 43801 standards. The signaling information of each voice channel is carried by means of 
up to four bits (signaling bits), designated by the applicable standards as bits A, B, C and D. Analog 
signaling profile is configured per channel and per direction. 
The following two tables show the analog signaling profile actions for the FXS and E&M interface.   
 
 
Megaplex-1 
5. Ports 
Analog Signaling Profile Actions for FXS Interface  
Signaling 
Mode  
Direction 
Signaling Bits 
A 
B 
C 
D 
Loop Start 
Tx 
signaling/inverse-sig 
1/0 
1/0 
1 
1/0 
signaling/inverse-sig 
1/0 
1 
1/0 
1 
1/0 
signaling/inverse-sig 
Rx 
signaling/inverse-sig 
not-used 
not-used 
not-used 
not-used 
signaling/inverse-sig 
not-used 
not-used 
signaling/inverse-sig 
forward-disconnect/ 
inverse-forward-disconnect 
not-used 
not-used 
forward-disconnect/ 
inverse-forward-
disconnect 
signaling/inverse-sig 
not-used 
not-used 
not-used 
not-used 
forward-
disconnect 
signaling/inverse-sig 
Wink 
Start 
Tx 
signaling/inverse-sig 
1/0 
1/0 
1 
Rx 
signaling/inverse-sig 
wink 
not-used 
not-used 
signaling/inverse-sig 
wink 
forward-
disconnect 
not-used 
signaling/inverse-sig 
forward-disconnect/ 
inverse-forward-disconnect 
wink 
not-used 
Analog Signaling Profile Actions for E&M Interface  
Direction 
Signaling Bits 
A 
B 
C 
D 
Tx 
signaling/inverse-sig 
1/0 
1/0 
1 
1/0 
signaling/inverse-sig 
1/0 
1 
1/0 
1 
1/0 
signaling/inverse-sig 
Rx 
signaling/inverse-sig 
not-used 
not-used 
not-used 
not-used 
signaling/inverse-sig 
not-used 
not-used 
Megaplex-1 
5. Ports 
Direction 
Signaling Bits 
A 
B 
C 
D 
not-used 
not-used 
not-used 
signaling/inverse-sig 
• 
not-used indicates that the corresponding bit is not relevant; 
• 
signaling states:  
 
For FXS interface, 0 indicates on-hook and 1 indicates off-hook. 
• 
inverse-sig has two states:  
 
For FXS interface, 0 indicates off-hook and 1 indicates on-hook. 
• 
forward-disconnect has two states:  
 
0 indicates the far-end party is not disconnected (FXS port is feeding the line)  ; 
 
1 indicates the far-end party has disconnected (FXS port has disconnected the line feeding); 
• 
inverse-forward-disconnect has two states:  
 
0 indicates the far-end party has disconnected (FXS port has disconnected the line feeding); 
 
1 indicates the far-end party is not disconnected (FXS port is feeding the line) ; 
• 
wink indicates reverse battery polarity: 
 
0 indicates reversion battery polarity,  
 
1 indicates normal battery polarity. 
Note 
Forward-disconnect/inverse-forward-disconnect and wink options are 
applicable only for the FXS interface.  
Factory Defaults 
The default analog signaling profiles are follows: 
• 
Applicable for FXS/E&M – "sig_over_a_bit":  
config>port# info detail  
    analog-signaling-profile  "sig_over_a_bit"  
        a-bit-tx  signaling  
        a-bit-rx  signaling  
        b-bit-tx  1  
        b-bit-rx  not-used  
        c-bit-tx  0  
        c-bit-rx  not-used  
        d-bit-tx  1  
Megaplex-1 
5. Ports 
        d-bit-rx  not-used  
    exit 
Signaling bit states for this profile are as follows: 
Signaling Bit States for ""sig_over_a_bit" Profile  
Direction 
Analog Interface State Signaling Bits 
A 
B 
C 
D 
Tx 
On-Hook 
0 
1 
0 
1 
 
Off-Hook 
1 
1 
0 
1 
Rx 
Ring 
1 
X 
X 
X 
 
No Ring 
0 
X 
X 
X 
 
• 
Applicable for FXS used in North American market, when working opposite to 3rd party channel 
banks: 
config>port# info detail  
    analog-signaling-profile  "sig_tx_a_bit_rx_b_bit"  
a-bit tx signaling rx not-used 
b-bit tx 1 rx inverse-sig 
c-bit tx signaling rx not-used 
d-bit tx 1 rx not-used  
    exit 
Signaling bit states for this profile are as follows: 
Signaling Bit States for "sig_tx_a_bit_rx_b_bit" Profile  
Direction 
Analog Interface State Signaling Bits 
A 
B 
C 
D 
Tx 
On-Hook 
0 
1 
0 
1 
 
Off-Hook 
1 
1 
1 
1 
Rx 
Ring 
X 
0 
X 
X 
 
No Ring 
X 
1 
X 
X 
The default analog signaling profiles cannot be modified or deleted.  
Megaplex-1 
5. Ports 
Configuring Analog Signaling Profiles  
 To configure an analog signaling profile: 
5. Navigate to configure port analog-signaling-profile <analog-signaling-profile-name> to 
configure. 
The config>port>analog-signaling-profile(<analog-signaling-profile-name>)# prompt is 
displayed. 
6. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying translation 
rules for signaling bit A 
(receive and transmit 
directions) 
a-bit-tx {1 | 0 | signaling | inverse-sig } 
a-bit-rx {not-used | signaling | inverse-sig | 
forward-disconnect |  
inverse-forward-disconnect} 
 
Specifying translation 
rules for signaling bit B 
(receive and transmit 
directions) 
b-bit-tx {1 | 0 | signaling | inverse-sig | wink} 
b-bit-rx {not-used | signaling | inverse-sig | 
forward-disconnect | 
 inverse-forward-disconnect | wink} 
 
 
Specifying translation 
rules for signaling bit C 
(receive and transmit 
directions) 
c-bit-tx {1 | 0 | signaling | wink} 
c-bit-rx {not-used | forward-disconnect | wink} 
 
Specifying translation 
rules for signaling bit D 
(receive and transmit 
directions) 
d-bit-tx {1 | 0 | signaling | inverse-sig} 
d-bit-rx {not-used | signaling | inverse-sig} 
 
Example 
 To create and configure analog signaling profile “profile1”: 
• 
a-bit-tx– fixed to ‘1’ 
• 
a-bit-rx–not-used 
• 
b-bit-tx– signaling 
• 
b-bit-rx– signaling  

## 5.2 DS1 Ports  *(p.147)*

Megaplex-1 
5. Ports 
• 
c-bit-tx and rx, d-bit-tx and rx use the default value 
config>port>analog-signaling-pro(profile1)# a-bit-tx 1 
config>port>analog-signaling-pro(profile1)# a-bit-rx not-used 
config>port>analog-signaling-pro(profile1)# b-bit-tx signaling 
config>port>analog-signaling-pro(profile1)# b-bit-rx signaling 
 To display the resulting signaling profile: 
config>port>signaling-profile(profile1)# info detail 
    a-bit-tx  1  
    a-bit-rx  not-used  
    b-bit-tx  signaling  
    b-bit-rx  signaling  
    c-bit-tx  0  
    c-bit-rx  not-used  
    d-bit-tx  1  
    d-bit-rx  not-used 
 To assign profile 1 to a voice port: 
config>port>voice(1/3)# analog-signaling-profile profile1 
 
5.2 DS1 Ports  
Applicable Interfaces 
Each user TDM interface supports 16 independently-configurable ds1 ports.  
Functional Description 
The internal DS1 ports are logical ports that provide the linkage between the packet processing 
subsystem and the TDM subsystem: 
• 
On the TDM side, a DS1 port serves as an endpoint for traffic from the TDM and signaling buses. 
Each port in the Megaplex-1 that will use pseudowires must be assigned bandwidth (timeslots) 
on the internal DS1 port, using the standard Megaplex-1 timeslot assignment procedures.  
Megaplex-1 
5. Ports 
• 
On the pseudowire side, a DS1 port serves as the collection point for timeslots to be carried by 
each pseudowire. Thus, to carry traffic from a specific TDM port by means of a pseudowire, it is 
necessary to assign the same timeslots on the TDM side and on the pseudowire side. The 
pseudowire timeslot assignment is performed via PW-TDM cross-connect (see Configuring a 
PW-TDM Cross Connection in Chapter 8). 
Factory Defaults  
Megaplex-1 is supplied with all DS1 ports disabled. Other parameter defaults are listed in the table 
below.  
 Parameter  
Default Value 
frame-type (for devices without e1/t1 ports) 
e1 
Signaling (for devices without e1/t1 ports) 
disabled 
line-type (for devices with e1/t1 ports) 
e1: g723s 
t1: sf 
Idle-code (for devices with e1/t1 ports) 
0x7f  
 
Configuring DS1 Port Parameters  
 To configure the DS1 port parameters:  
1. Navigate to configure port ds1 1/<port> to select the internal DS1 port to configure. 
The config>port>ds1>1/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
Assigning short description 
to port 
name <string> 
 
Using no before name removes the name 
Administratively enabling 
port 
no shutdown 
 
Using shutdown disables the port 
Megaplex-1 
5. Ports 
Task 
Command  
Comments 
Specifying the maximum 
number of timeslots used in 
the DS1 port (depends on 
the environment where 
Megaplex-1 is used) 
frame-type {e1 | t1}  
 
e1: 31 timeslots 
t1: 24 timeslots 
Make sure to select the same value at both 
endpoints. 
Relevant only for device with no e1/t1 ports 
Enabling transmission of 
signaling over the DS1 port 
signaling  
Relevant only for device with no e1/t1 ports 
no signaling disables transmission of signaling 
Specifying the framing 
mode of the internal DS1 
port  
line-type {unframed | g732n | 
g732s}  
line-type {unframed | esf | sf}  
Relevant only for device with e1/t1 ports 
Make sure to select the same value at both 
endpoints. 
Specifying  the code 
transmitted to fill unused 
timeslots   
idle-code <00 to FF (hexa)>     
Specifying  the code transmitted to fill unused 
timeslots  
Relevant only for device with e1/t1 ports 
Example 
The following section illustrates how to configure the DS1 port 1: 
• 
Set the line type to t1. 
• 
Administratively enable the port. 
• 
Leave all other parameters disabled or at their defaults. 
config>port>ds1(1/1)# frame-type t1  
config>port>ds1(1/1)# no shutdown 
Viewing DS1 Port Status 
Follow the instructions below for viewing the status of an internal DS1 port. 
 To view the DS1 port status: 
• 
At the config>port>ds1(1/<port>)# prompt, enter show status. 
The status information appears as illustrated below.  
config>port>ds1(1/1)# show status 
Name                  : DS1 1 
Megaplex-1 
5. Ports 
Administrative Status : Up 
Operation Status      : Up 
XC Level              : DS0 
Loopback Type         : None 
Testing DS1 Ports  
The DS1 ports feature local and remote loopbacks at the port and timeslot levels.  
The following sections briefly describe each type of loopback on DS1 ports.  
Serial 
Voice 
Ds1-opt 
Ds1 
DS0 CX
PW Engine
SYNC
Bridge
ETH
Remote Loop
Local Loop
 
Local and Remote Loopbacks on DS1 Port 
Local Loopback on the DS1 Port  
The local port loopback is used to test the path of the signals intended for transmission through a 
selected DS1 port: this path starts at the local interface ports (serial/voice/ds1-opt) connected to the 
selected DS1 port, passes through the cross-connect matrix, and continues up to the port line interface. 
The path includes most of the line interface circuits serving the selected port, and the operation of the 
routing circuits that handle the port signals within the device. 
When a local loopback is activated, the port transmit signal is returned to the input of the same port 
receive path at a point just before the PW engine. The local interface ports connected to the selected 
DS1 port must receive their own signal.  
Remote Loopback on the DS1 Port  
The remote port loopback is used to test the line interface circuits of a selected DS1 port. This test also 
checks the Tx and Rx path connecting the corresponding port to the remote unit. 
When a remote loopback is activated on a DS1 port, that port returns the received signal to the remote 
unit, via the transmit path. The received signal remains connected as usual to the receive path of the 
corresponding port. To correct transmission distortions, the returned signal is regenerated by the 
corresponding line interface circuits. 
Megaplex-1 
5. Ports 
The remote loopback should be activated only after checking that the remote unit operates normally 
with the local port loopback. In this case, the remote unit must receive its own signal, and thus it must 
be frame-synchronized.  
The remote port loopback should be activated only when both of the units are connected in a link, 
otherwise an unstable situation occurs.  
Local Loopback on Timeslots of DS1 Port  
The local loopback on selected timeslots of a DS1 port is used to return the transmit payload carried by 
the selected timeslots through the same timeslots of the receive path.  
The user can activate the loopback on any individual timeslot, or on several arbitrarily selected 
timeslots.  
Remote Loopback on Timeslots of DS1 Port  
The remote loopback on selected timeslots of a DS1 port is used to return the receive payload carried by 
the selected timeslots through the same timeslots of the transmit path. This test is recommended for 
testing signal paths from a remote equipment unit, that uses only a fraction of the available port 
bandwidth. 
Loopback Duration  
The activation of a loopback disconnects the local and remote equipment served by the PW. Therefore, 
when you initiate a loopback, you have the option to limit its duration to a selectable interval in the 
range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-1 before 
this timeout expires.  
The default is infinite duration (without timeout). 
Activating the Loopbacks  
 To perform a loopback on the internal DS1 port:  
1. Navigate to configure port ds1 1/<port> to select the internal DS1 port to be tested. 
The config>port>ds1>(1/<port>)# prompt is displayed.  
Megaplex-1 
5. Ports 
Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Activating and configuring 
the direction of the 
loopback and the duration 
of it (in minutes) 
loopback {local | remote} [time-
slot <1..31>] [duration <duration 
in minutes 1..30> ]  
 
• local – local loopback 
• remote – remote loopback 
Stopping the loopback  
no loopback  
 
Configuration Errors 
The following table lists messages generated by Megaplex-1 when a configuration error on DS1 ports is 
detected. 
Message 
Description 
Port: cross-connect is configured while 
admin status is down  
You cannot change the interface port status to “no 
shutdown” if the DS1 port is in shutdown state. First set the 
DS1 port to “no shutdown”. 
Port: fail to get data from DB slot 
Database problem. Try to reconfigure the DS1 port. 
Port: frame-type value error 
Frame-type value can be only e1 or t1. 
Port: port bound to tdm group, frame 
type mismatch  
This port is a member in tdm-group protection. Both ports of 
the tdm group must have the same frame-type values. 
Port: port bound to tdm group, 
signaling mismatch 
This port is a member in tdm-group protection. Both ports of 
the tdm group must have the same signaling-mode values. 
Port: cross connect configured, 
signaling mismatch. 
This port is cross-connected with DS1 port. Both ports of the 
cross-connect must have the same signaling-mode values. 
Port: time slot 16 reserved for cas 
signaling  
Time slot 16 cannot be used in cross-connect if the port is set 
to signaling mode. 
Port: Illegal ports state, cross-connect 
is configured while the interface is 
down 
Both ports in cross-connect must have the same status 
(shutdown/no shutdown). 
Port: can't change frame type if cross 
connect already exist 
You cannot change the DS1 port framing once cross-connect 
is configured on the port. 
Port: cross-connected to itself  
You cannot cross-connect a port to itself. Choose another 
port.  

## 5.3 DS1 Optical Ports  *(p.153)*

Megaplex-1 
5. Ports 
5.3 DS1 Optical Ports  
Applicable Models 
DS1 optical ports denote fiber optic links of MP-1/PSR/2GES/6S/C37/1FEU and MP-
1/PSR/2GEU/6S/C37/1FEU models.  
Standards  
IEEE C37.94 
Functional Description 
The IEEE C37.94 standard defines a programmable nx64 kbps (n = 1…12) multimode optical fiber 
interface between teleprotection and digital multiplexer equipment, for distances of up to 2 km. 
Fiber Optic Interface  
The C.37 Megaplex-1 models feature a dual-port fiber optic interface, operating at a nominal 
wavelength of 850 nm and nominal line rate of 2.048 Mbps. Each port is terminated in a pair of ST 
connectors for connection to standard multimode fiber. 
The fiber optic interface has a wide dynamic range, which ensures that the receiver will not saturate 
even when using short fiber optic cables (saturation is caused when the optical power applied to the 
receiver exceeds its maximum allowed input power, and results in very high bit error rates). 
The interface can be used for both user and network ports – either for inter-substation communication 
or for transmitting distance Teleprotection information. 
C37.94 Frame Format  
The C37.94 frame structure is schematically shown below. 
 
TS0 
TS1 
TS 2-7 
TS 8 -31 
G704 Sync Header 
Overhead data 
Channel data 
Megaplex-1 
5. Ports 
 
Frame Element 
Description 
Bits 
Header 
The 16-bit header is a unique bit pattern to allow 
the receiver to synchronize to the 256-bit frame. 
a  b  c  d  e  f  g  h  0 0 0 0 1 1 1 1 
Overhead data 
This 48-bit section includes bits for providing 
information between the multiplexer and 
teleprotection equipment. Each data bit is 
followed by its complement (for 24 actual bits of 
information). 
p,q,r,s – One or zero data that 
depend upon the value of N 
used, where N = 1 to 12 (p = 
most-signiﬁcant-bit) 
 
0,0,0,1  for N = 1 
0,0,1,0  for N = 2 
1,1,0,0, for N = 12 
Channel data 
This 192-bit section comprises 96 data bits, with 
each data bit followed by its complement.  
The first N times 8 data bits carry the N times 64 
kilobit per second (kbit/s) data. 
The remaining 96 – (N times 8) data bits are set to 
1. 
 
Factory Defaults  
Megaplex-1 is supplied with all ds1-opt ports disabled. 
Configuring DS1 Optical Port Parameters  
 To configure the DS1 optical link parameters: 
1. Navigate to configure port ds1-opt 1/<port> to select the port to configure. 
The config>port>ds1-opt>(1/<port>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
Assigning short 
description to port 
name <string> 
Using no name removes the name 
Megaplex-1 
5. Ports 
Task 
Command  
Comments 
Administratively 
enabling port 
no shutdown 
Using shutdown disables the port 
Viewing a DS1-Opt Port Status 
Follow the instructions below for viewing the status of the DS1-opt port 2 as an example. 
 To view the DS1-opt port status: 
• 
At the config>port>ds1-opt (<slot>/<port>)# prompt, enter show status. 
The status information appears as illustrated below.  
config>port>ds1-opt(1/1)# show status 
Name                  : DS1 OPT 1/1 
Administrative Status : Up 
Operation Status      : Up 
Loopback Type         : None 
Testing DS1 Optical Links  
The test and diagnostics functions available on each optical link are: 
• 
Local loopback on local optical link 
• 
Remote loopback on local optical link 
The loopbacks are schematically shown below. 
Megaplex-1 
5. Ports 
Ds1-opt
Local Loop
DS0 CX
PW Engine
SYNC
Bridge
Remote Loop
AIS
ETH
 
Local Digital Loopback (Local Loop) 
The local loopback is a digital loopback performed at the digital output of a selected port, by returning 
the local Rx input signal to the local Tx output. The transmit signal is still sent to the remote Megaplex 
unit.  
While the loopback is connected, the local ds1-opt port should receive its own signal. 
Remote Digital Loopback (Remote Loop) 
The remote loopback is a digital loopback performed at the digital input of the port, by returning the 
digital receive signal of the port to the remote unit via  the transmit path. The receive signal remains 
connected to the local user, and can be received by user.  
While the loopback is connected, the remote ds1-opt port should receive its own signal. 
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the DS1 optical link. 
Therefore, when you initiate a loopback, you have the option to limit its duration to an interval in the 
range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local device before this 
timeout expires.  
The default is infinite duration (without timeout). 

## 5.4 E1 Ports  *(p.157)*

Megaplex-1 
5. Ports 
Activating the Loopbacks 
 To perform a loopback on the DS1 optical link: 
1. Navigate to configure port ds1-opt 1/<port> to select the optical link to be tested. 
The config>port>ds1-opt>(1/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below.  
Task 
Command 
Comments 
Activating and configuring 
the direction of the loopback 
and the duration of it (in 
minutes) 
loopback {local | remote} 
[duration <duration in 
minutes 1..30> ]  
local – local 
loopback 
remote – remote 
loopback 
  
Stopping the loopback  
no loopback 
 
5.4 E1 Ports  
Applicable Models 
8 E1/T1 ports are available on the following options: 
• 
MP-1/PSR/2GES/4FEU/6S/8E1T1 
• 
MP-1/PSR/2GEU/4FEU/6S/8E1T1 
In the CLI, the E1 ports are designated and numbered e1  1/1 to e1  1/8. 
Standards  
The E1 link interfaces meet the applicable requirements of ITU-T Rec. G.703 (Physical layer), G.704, 
G.706 and G.732 (framing), and G.823 (jitter).  
Megaplex-1 
5. Ports 
Functional Description 
Megaplex-1 features 8 E1/T1 interfaces. The type of the interface is configured on the port> level by the 
“pdh-frame-type” command. This command applies to all the 8 interfaces simultaneously (you cannot 
configure part of the ports to E1 and another part to T1). The default configuration is E1.  
Framing  
The E1 ports can be independently configured in accordance with the desired ITU-T framing mode and 
signaling formats: 
• 
Basic G.704 framing (identified as G.732N) for applications that require CCS.  
• 
G.704 framing with timeslot 16 multiframe (identified as G.732S and referred to as G.704 
multiframe mode) for applications that require CAS. 
• 
Unframed mode for transparent transfer of 2.048 Mbps streams, including streams with 
proprietary framing. Also enables transferring framed E1 streams without terminating timeslot 
0, and timeslot 16. 
• 
G.732N and G.732S can be used with our without CRC. 
The framer automatically adds the appropriate overhead. Unused timeslots are filled with a 
user-specified idle code. The user can also select specific timeslots to be transferred (DS0 cross-
connect). 
The framing mode can be independently selected for each E1 port. It is configured by means of the line-
type parameter. 
Interface Type 
The E1 ports support two line interfaces: 
• 
120Ω balanced line interface. The nominal balanced interface transmit level is ±3V. 
• 
75Ω unbalanced interface. The nominal unbalanced interface transmit level is ±2.37V. For 
working in this mode, and adaptor cable (CBL-RJ45/2BNC/E1/X) is required. 
Only one of these interfaces can be active at any time. The active interface can be selected by the user, 
separately for each port.  
• 
The E1 interface line code is HDB3. 
Megaplex-1 
5. Ports 
Receive Signal Attenuation  
The E1 line interfaces have integral LTUs, which enable long-haul operation with line attenuation of up 
to 43 dB. The line interface can also emulate a DSU interface, for short-haul applications: in this case, 
the maximum line attenuation is 12 dB. The receive signal attenuation level is configured by means of 
the rx-sensitivity parameter.  
E1 Payload Processing  
E1 ports support two main types of payload per timeslot: 
• 
Data timeslots: timeslots which are transparently transferred from port to port. In general, it is 
assumed that no CAS is associated with data timeslots.  
• 
Voice timeslots: timeslots carrying PCM-encoded payload, with A-law companding for E1 ports 
and µ-law companding for T1 ports. When transferred between ports with different standards 
(for example, between E1 and T1 ports), these timeslots are converted by Megaplex-1. 
In general, CAS is always associated with voice timeslots, and therefore it must also be 
converted when transferred between ports with different standards.  
The flow of payload carried by voice timeslots is normally bidirectional (full duplex connection). 
However, it is also possible to define unidirectional flows, called unidirectional broadcasts, from one 
source (a timeslot of a source port) to multiple destinations (each destination being a selected timeslot 
of another port).  
In case of data timeslots, the flow of payload is normally unidirectional. If the application requires 
bidirectional flows, cross-connect must be configured symmetrically for both directions.  
Handling E1 Alarm Conditions  
E1 ports using framed mode support two types of indications in the individual timeslots:  
• 
Idle Timeslot Indication. A special code can be transmitted in empty timeslots (timeslots which 
do not carry payload).  
• 
OOS Indications. The OOS code is inserted in individual timeslots to signal the equipment routed 
to one of the E1 ports of the module that the link connected to the external port is 
out-of-service (e.g., because of loss of frame synchronization).  
For ports using a G.704 timeslot 16 multiframe mode, the CAS information can also be replaced 
by a selectable OOS indication.  
Megaplex-1 
5. Ports 
The idle code and OOS indications can be independently configured for each port. Moreover, separate 
OOS codes can be transmitted in the timeslots, in accordance with the type of payload carried by each 
timeslot (voice or data).  
OOS Signaling 
If the communication between modules located in different Megaplex units fails, e.g., because loss of 
main link synchronization, etc., it is necessary to control the state of the signaling information at the two 
ends of the link. This activity, called out-of-service (OOS) signaling, is performed by the E1 interfaces and 
can be selected in accordance with the specific application requirements, on a per-link basis.  
The OOS signaling options supported by the E1 module ports are as follows: 
• 
Signaling forced to idle state for the duration of the out-of-service condition (force-idle). This 
option is suitable for use with all voice interfaces. 
• 
Signaling forced to busy state for the duration of the out-of-service condition (force-busy). This 
option is suitable for use with E&M and FXO interfaces, but not with FXS interfaces. 
• 
Signaling forced to idle state for 2.5 seconds, and then changed to busy state for the remaining 
duration of the out-of-service condition (idle-busy). This option is suitable for use with E&M and 
FXO interfaces, but not with FXS interfaces. 
• 
Signaling forced to busy state for 2.5 seconds, and then changed to idle state for the remaining 
duration of the out-of-service condition (busy-idle). This option is suitable for use with all the 
voice interfaces. 
Factory Defaults 
Megaplex-1 is supplied with all E1 ports disabled. Other parameter defaults are listed in the table below. 
Parameter  
Default Value 
interface-type  
balanced  
idle-code  
0x7f 
line-type 
g732s  
out-of-service - voice  
0x00 
out-of-service - data  
0x00 
out-of-service - signaling   
force-idle 
rx-sensitivity  
short-haul  
Megaplex-1 
5. Ports 
Parameter  
Default Value 
tx-clock-
source                                        
domain 1 
                                    
Configuring an E1 Port  
If the Megaplex-1 interface type is set to T1, you need to change the configuration back to E1.  
 To change the configuration back to E1: 
1. Navigate to configure port pdh-frame-type and type e1.  
The interface type of all the device ports changes from t1 to e1. 
Note 
If any cross-connect exists over one of the ports or one of the e1/t1 ports is 
configured as a clock source, Megaplex-1 displays this configuration and 
rejects the command. If this is the case, delete the specified cross-
connect/clock source and repeat the command.  
 To configure the E1 port parameters: 
1. Navigate to configure port e1 <slot>/<port> to select the E1 port to configure.  
The config>port>e1>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below  
Task 
Command  
Comments 
Assigning short 
description to port 
name <string> 
Using no name removes the name 
Administratively 
enabling port 
no shutdown 
Using shutdown disables the port 
Specifying E1 framing 
mode  
line-type {unframed | g732n  
| g732n-crc | g732s | g732s-crc} 
unframed – Unframed 
g732n – G.732N without CRC 
g732n-crc – G.732N with CRC 
g732s– G.732S without CRC 
g732s-crc –  G.732S with CRC 
Megaplex-1 
5. Ports 
Task 
Command  
Comments 
Setting attenuation 
level of the receive 
signal 
rx-sensitivity {short-haul | long-haul }  
short-haul – low sensitivity (-12 dB) 
long-haul – high sensitivity (-43 dB) 
Specifying port 
impedance  
interface-type {balanced | unbalanced} 
 
 
Specifying  the code 
transmitted to fill 
unused timeslots in E1 
frames 
idle-code { 00 to FF (hexa) }  
 
 
The available selections are [0x01 to 
0xFF] with the following values that are 
illegal: 0x00, 0x08, 0x10, 0x12, 0x21, 
0x24, 0x42, 0x49, 0x84, 0x92  
Transmitting an 
out-of-service signal 
(OOS)   
out-of-service [voice <00 to FF (hexa)>] 
[ data <00 to FF (hexa)>] [signaling 
{force-idle | force-busy | idle-busy | 
busy-idle}]  
 
<force-idle>         : Force idle (0) 
<force-busy>         : Force busy (1) 
<busy-idle>          : Force busy (1) for 2.5 
seconds 
<idle-busy>          : Force idle (0) for 2.5 
seconds 
The hexadecimal number is in the range 
of 0 to FF (two digits)  
The selected out-of-service data code is 
also sent during out-of-service periods 
instead of the external data stream when 
the unframed mode is used  
out-of-service voice selection is relevant 
only when the g732s or g732s-crc modes 
are selected  
Configuring collection 
of performance 
management statistics 
for the port, that are 
presented via the 
RADview Performance 
Management portal 
pm-collection  
{interval <seconds 1..900> | on-
interval-close} 
PM collection can be enabled at a 
defined interval or before an interval 
expires.  
Type no pm-collection to disable PM 
statistics collection for the E1 port. 
Note: In addition to enabling PM 
statistics collection for the port, it must 
be enabled for the device. Refer to the 
Performance Management section in the 
Monitoring and Diagnostics chapter for 
details. 
Megaplex-1 
5. Ports 
Task 
Command  
Comments 
Selecting the timing 
reference source used 
by the port for the 
transmit-to-network 
direction 
tx-clock-source loopback  
tx-clock-source domain <number>  
tx-clock-source through-timing     
 
loopback – Clock received from the E1/T1 
port 
domain – Clock provided by system clock 
domain 
through-timing – Clock received from PW  
Example  
The following section illustrates how to configure E1 port 1: 
• 
Set the E1 framing mode to G.732N with CRC. 
• 
Set the line interface to unbalanced. 
• 
Set the attenuation level of the receive signal to long-haul. 
• 
Set the idle code to 8E. 
• 
Administratively enable the port. 
• 
Leave all other parameters disabled or at their defaults. 
config>port>e1(1/1)# interface-type unbalanced 
config>port>e1(1/1)# line-type g732n-crc  
config>port>e1(1/1)# rx-sensitivity long-haul  
config>port>e1(1/1)# idle-code 0x8E 
config>port>e1(1/1)# no shutdown 
Viewing an E1 Port Status 
Follow the instructions below for viewing the status of the E1 port 1/1 as an example. 
 To view the E1 port status: 
• 
At the config>port>e1(<slot>/<port>)# prompt, enter show status. 
The status information appears as illustrated below.  
config>port>e1(1/1)# show status 
Name                  : 
Administrative Status : Down 
Operation Status      : Up 
Megaplex-1 
5. Ports 
Interface Type        : Balanced 
Connector Type        : DB44 
Loopback : Off 
Testing E1 Ports  
The following test and diagnostics functions are available on each E1 port: 
• 
Local digital loopback  
• 
Remote digital loopback.  
The loopbacks are schematically shown in the figure below. 
 
 
Local Digital Loopback (Local Loop) 
The local loopback is a digital loopback performed at the digital output of a selected port, by returning 
the local Rx input signal to the local Tx output. The transmit signal is still sent to the remote Megaplex 
unit.  
While the loopback is connected, the local E1 port should receive its own signal.  
Remote Digital Loopback (Remote Loop) 
The remote loopback is a digital loopback performed at the digital input of the port, by returning the 
digital receive signal of the port to the remote unit via the transmit path. The receive signal remains 
connected to the local user, and can be received by user.  
While the loopback is connected, the remote E1 port should receive its own signal. 
Megaplex-1 
5. Ports 
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the Megaplex-1. 
Therefore, when you initiate a loopback, you have the option to limit its duration to an interval in the 
range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-1 before 
this timeout expires.  
The default is infinite duration (without timeout). 
Activating Loopbacks  
 To perform a loopback on the E1 port: 
1. Navigate to configure port e1 <slot>/<port> to select the E1 port to be tested. 
The config>port>e1>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below.  
Task 
Command 
Comments 
Activating and configuring 
the direction of the 
loopback (all modules) 
loopback {local | remote}  
[duration <duration in minutes 
1..30> ] 
• local – local loopback (per port 
and per timeslot) 
• remote – remote loopback (per 
port and per timeslot) 
Stopping the loopback  
no loopback 
 
Configuration Errors  
The following tables list messages generated by Megaplex-1 when a configuration error on E1 ports is 
detected. 
 
Message 
Description 
Illegal tx-clock-source configured  
You cannot change the tx-source clock on the E1 port 
(default=system) if it is not connected to DS1 port 
Megaplex-1 
5. Ports 
Displaying E1 Port Statistics  
E1 ports of Megaplex-1 feature the collection of statistical diagnostics per relevant parts of ITU-T G.826, 
thereby allowing the carrier to monitor the transmission performance of the links.  
 To display the E1 port statistics: 
• 
At the prompt config>slot>port>e1(<slot><port>[<tributary>])#, enter show statistics followed 
by the parameters listed below.  
Task 
Command 
Comments 
Displaying 
statistics 
show statistics {total | all | all-intervals |  
current}  
 
 
  
• total –total statistics of last 
96 intervals  
• current –current statistics 
• all-intervals – statistics for 
all valid intervals 
• all –all statistics: first current 
statistics, then statistics for 
all valid intervals, and finally 
total statistics 
Displaying 
statistics for a 
specific interval 
show statistics interval <interval-num 1..96> 
 
 
E1 port statistics are displayed.   
Note 
LOFC and Rx Frames Slip are displayed for framed formats only.  
For example: 
Current statistics: 
config>port>e1(1/2)# show statistics current 
Current 
--------------------------------------------------------------- 
Time Elapsed (Sec) : 191 
Valid Intervals    : 2 
ES             : 0 
SES            : 0 
UAS            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
Statistics for interval 67: 
config>port>e1(3/1)# show statistics interval 67 
Interval Number : 67 
Megaplex-1 
5. Ports 
 
Interval 
--------------------------------------------------------------- 
ES             : 16 
SES            : 1 
UAS            : 589 
Rx Frames Slip : 0 
LOFC           : 0 
Total statistics: 
 
config>port>e1(1/2)# show statistics total 
Total 
--------------------------------------------------------------- 
ES             : 2 
SES            : 0 
UAS            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
All statistics:  
 
config>port>e1(1/2)# show statistics all 
Current 
--------------------------------------------------------------- 
Time Elapsed (Sec) : 171 
Valid Intervals    : 2 
config>port>e1(1/2)# 
 
ES             : 0 
SES            : 0 
UAS            : 0 
 
Rx Frames Slip : 0 
LOFC           : 0 
 
Interval Number : 1 
 
Interval 
--------------------------------------------------------------- 
ES             : 0 
SES            : 0 
UAS            : 0 
 
Rx Frames Slip : 0 
LOFC           : 0 
 
Interval Number : 2 
 
Interval 
--------------------------------------------------------------- 
ES             : 2 
SES            : 0 
UAS            : 0 
 
Rx Frames Slip : 0 
LOFC           : 0 
Megaplex-1 
5. Ports 
 
Total 
--------------------------------------------------------------- 
ES             : 2 
SES            : 0 
UAS            : 0 
 
Rx Frames Slip : 0 
LOFC           : 0 
The counters are described in the following tables.  
E1 Port Statistics Parameters – Current 15-Minute Interval 
Parameter 
Description 
ES  
Displays the number of errored seconds in the current 15-minute interval. 
An errored second is any second not declared a UAS in which a OOF (Out of 
Frame) or CRC (Cyclic Redundancy Check error) occurred. 
UAS  
Displays the number of unavailable seconds (UAS) in the current interval. 
An unavailable second is one of the following: 
• Any second following 10 consecutive SES seconds 
• A second for which any of the previous 10 consecutive seconds was also a UAS 
and any of the previous 10 consecutive seconds was a SES. 
SES  
Displays the number of severely errored seconds (SES) in the current interval. 
A SES is any second not declared a UAS which contains an OOF or more than 320 
CRC errors. 
LOFC  
Displays the number of LOFC in the current interval. 
The loss of frame (LOF) counter counts the loss of frame alignment events. The 
data is collected for the current 15-minute interval. 
Rx Frames Slip 
Displays the number of Rx Frames Slips in the current 15-minute interval. 
A CSS is a second with one or more controlled slip events. 
Time elapsed 
The elapsed time (in seconds) since the beginning of the current interval, in 
seconds. The range is 1 to 900 seconds. 
Valid Intervals 
The number of elapsed finished 15-min intervals for which statistics data can be 
displayed, in addition to the current (not finished) interval (up to 96). 
E1 Port Statistics Parameters – Selected 15-Minute Interval  
Parameter 
Description 
ES  
Displays the total number of errored seconds (ES) in the selected interval 
UAS 
Displays the total number of unavailable seconds (UAS) in the selected interval 

## 5.5 Ethernet Ports  *(p.169)*

Megaplex-1 
5. Ports 
Parameter 
Description 
SES  
Displays the total number of severely errored seconds (SES) in the selected interval 
LOFC  
Displays the total number of loss of frame alignment events in the selected interval 
Rx Frames Slip 
Displays the total number of loss of of Rx Frames Slip events in the selected interval 
Interval number 
The number of interval for which statistics is displayed.  
E1 Port Statistics Parameters – Total Statistics 
Parameter 
Description 
ES  
Displays the total number of errored seconds (ES) since statistics are available 
UAS 
Displays the total number of unavailable seconds (UAS) since statistics are available 
SES  
Displays the total number of severely errored seconds since statistics are available 
LOFC  
Displays the total number of loss of frame alignment events since statistics are 
available 
Rx Frames Slip 
Displays the total number of loss of of Rx Frames Slip events since statistics are 
available 
Clearing Statistics 
 To clear the statistics for an E1 port: 
• 
At the prompt config>port>e1<slot>/<port>)#, enter clear-statistics. 
The statistics for the specified port are cleared. 
5.5 Ethernet Ports  
Applicable Models 
Megaplex-1 features the following Ethernet ports: 
• 
Two fiber optic or copper Gigabit Ethernet network (NNI) ports  
Megaplex-1 
5. Ports 
• 
Two or four copper Fast Ethernet user (UNI) ports 
• 
One copper Fast Ethernet port for management. 
Standards  
IEEE 802.3, RFC 4836, RFC 3635. 
Functional Description 
GbE (NNI) Port Interfaces  
The GbE Network (NNI) ports provide the physical connection to the packet switched network. These 
ports provide Megaplex-1 with a multirate FE/GE interface, for optical or electrical media.  
The ports can be ordered with one of the following interfaces: 
• 
10/100/1000BASE-T copper ports. This type of ports support autonegotiation, with 
user-specified advertised data rate (10, 100 or 1000 Mbps) and operating mode (half- or 
full-duplex).  
The ports also support automatic polarity and crossover detection, and polarity correction, for 
connection through any type of cable to any type of Ethernet port (hub or station).  
Alternatively, auto-negotiation can be disabled and the rate and operating mode be directly 
specified. 
• 
SFP sockets, for installing 100/1000BASE-X SFP plug-in modules. Support for standard SFP 
optical transceivers for the GbE link interfaces enables selecting the optimal interface for each 
application.  
Fast Ethernet (UNI) Port Interface  
The external Ethernet interface has two or four 10/100 Mbps (10/100BASE-Tx) ports capable of 
auto-negotiation. The user can configure the advertised data rate (10 or 100 Mbps) and operating mode 
(half-duplex or full-duplex). Alternatively, auto-negotiation can be disabled, and the rate and operating 
mode be directly specified. The interfaces are terminated in RJ-45 connectors. In addition to auto-
negotiation, MDI/MDIX polarity and cross-over detection and automatic cross-over correction are also 
supported.  
Megaplex-1 
5. Ports 
Management Ethernet Port  
The external Ethernet interface has a 10/100/1000 Mbps (10/100/1000BASE-Tx) port, supporting 
autonegotiation. The interface is terminated in RJ-45 connectors.  
Numbering 
The following table shows how to refer to the ports when configuring them with CLI commands. 
Ethernet Port Reference 
Port  
Description 
Port Number 
MNG-ETH 
Management Ethernet Port 
0/0 
GbE 1 
NNI port 1  
0/1 
GbE 2 
NNI port 2  
0/2 
ETH 1 
UNI (Fast Ethernet) port 
0/3 
ETH 2 
UNI (Fast Ethernet) port 
0/4 
ETH 3 
UNI (Fast Ethernet) port 
0/5* 
ETH 4 
UNI (Fast Ethernet) port 
0/6* 
 
 
*only for ordering options with 4 Fast Ethernet ports 
MAC Addresses 
Megaplex-1 has multiple MAC addresses. Each Ethernet port is assigned a different MAC address. 
You can view the MAC address assigned to an Ethernet port via show status (see Viewing Ethernet Port 
Status). For information on which MAC address is used by a particular feature, refer to the relevant 
section in this manual.   
Flow Control  
Megaplex-1 NNI and UNI Ethernet ports support Rx flow control. Flow control configuration is factory-
configured and cannot be changed by the user.  
Megaplex-1 
5. Ports 
Autonegotiation  
The speed and duplex mode of an Ethernet interface is set either manually by the operator or 
negotiated with the peer interface. The autonegotiation procedure enables automatic selection of the 
operating mode on a LAN. It enables equipment connecting to an operating LAN to automatically adopt 
the LAN operating mode (if it is capable of supporting that mode).  
Queue Group Profile 
Queue group profiles are the largest entities used in pre- and post-forwarding traffic management. They 
are attached to physical ports and consist of queue block and shaper profiles. See Queue Group Profiles 
section in Chapter 8  for details. 
Factory Defaults  
By default, the Ethernet non-management ports have the following configuration. 
FE port: 
    shutdown 
    name "ETH 1/1" 
    auto-negotiation 
    max-capability 100-full-duplex 
    speed-duplex 100-full-duplex 
    queue-group profile "FeDefaultQueueGroup" 
    queue-mapping profile "qmappbit" 
 
GbE ports: 
    shutdown 
    name "ETH 0/2" 
    auto-negotiation 
    max-capability 1000-full-duplex 
    speed-duplex 1000-full-duplex 
    queue-group profile "GbeDefaultQueueGroup" 
    queue-mapping profile "qmappbit" 
*for fiber ports: 1000-x-full-duplex 
For description of default queue group profiles, see Queue Group Profiles section in Chapter 8.  
Megaplex-1 
5. Ports 
Configuring Ethernet Ports  
 To configure the Ethernet port parameters: 
1. Navigate to configure port ethernet <slot>/<port> to select the Ethernet port to configure.  
The config>port>ethernet>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed in the table below.  
Task 
Command 
Comments 
Assigning short description 
to the port* 
name <string> 
Using no name removes the name 
Administratively enabling 
port* 
no shutdown 
Using shutdown disables the port 
Enabling autonegotiation 
 
auto-negotiation  
Using no auto-negotiation disables 
autonegotiation 
Setting maximum advertised 
capability (highest traffic 
handling capability to be 
advertised during the 
autonegotiation process)  
 
  
max-capability {10-half-
duplex | 10-full-duplex | 
100-half-duplex | 100-full-
duplex | 1000-full-duplex | 
1000-x-full-duplex} 
 
  
10-full-duplex –10baseT full duplex  
10-half-duplex – 10baseT half duplex  
100-full-duplex – 100baseT full duplex  
100-half-duplex – 100baseT half 
duplex  
1000-full-duplex – 1000base T full 
duplex (copper GbE ports only) 
1000-x-full-duplex – 1000base T full 
duplex (fiber GbE ports only)  
This parameter applies only if 
autonegotiation is enabled.  
Megaplex-1 
5. Ports 
Task 
Command 
Comments 
Setting data rate and duplex 
mode of the Ethernet port, 
when autonegotiation is 
disabled 
  
speed-duplex {10-half-
duplex | 10-full-duplex | 
100-half-duplex | 100-full-
duplex | 1000-full-duplex | 
1000-x-full-duplex} 
 
10-full-duplex –10baseT full duplex 
(copper ports only) 
10-half-duplex – 10baseT half duplex 
(copper ports only) 
100-full-duplex – 100baseT full duplex 
100-half-duplex – 100baseT half 
duplex  
1000-full-duplex – 1000base T full 
duplex (copper GbE ports only) 
1000-x-full-duplex – 1000base T full 
duplex (fiber GbE ports only)  
This parameter applies only if 
autonegotiation is enabled. 
Assigning queue group 
profile to Ethernet port 
  
queue-group profile 
<queue-group-profile-name> 
 
The queue group profile is defined 
under Quality of Service (QoS) in 
Chapter 8. 
no queue-group removes queue group 
association  
Note. In the current version, only 
default queue group profile is 
supported. 
 
Assigning queue mapping 
profile to Ethernet port 
 
queue-mapping profile 
<queue-group-profile-name> 
 
The queue mapping profile is defined 
under Quality of Service (QoS) in 
Chapter 8. 
no queue-mapping removes queue 
group association  
Note 1. In the current version, only 
default queue mapping profile is 
supported. 
Note 2. If the port is connected, the 
queue mapping profile cannot be 
edited.  
Assigning a policer profile to 
the port 
 
policer-profile <name> 
The policer profile is defined under 
Quality of Service (QoS) in Chapter 8. 
Using no policer <name> deactivates 
this policer profile. 
Megaplex-1 
5. Ports 
Task 
Command 
Comments 
Configuring collection of 
performance management 
statistics for the port, that 
are presented via the 
RADview Performance 
Management portal 
pm-collection  
{interval <seconds 1..900> | 
on-interval-close} 
PM collection can be enabled at a 
defined interval or before an interval 
expires.  
Type no pm-collection to disable PM 
statistics collection for the Ethernet 
port. 
Note: In addition to enabling PM 
statistics collection for the port, it must 
be enabled for the device. Refer to the 
Performance Management section in 
the Monitoring and Diagnostics 
chapter for details. 
*only “name”, “shutdown” and “pm-collection” parameters are supported for the MNG-ETH port.  
Example  
 To configure the GbE port 2: 
• 
Autonegotiation – enabled 
• 
Max capability – 100baseT full duplex 
• 
Administratively enabled. 
# config port eth 0/2 no shutdown 
   auto-negotiation 
   max-capability 100-full-duplex 
Viewing Ethernet Port Status  
You can display the status and configuration of an individual Ethernet port.  
 To display status of an Ethernet port:  
• 
At the prompt config>port>eth(<slot>/<port>)#, enter show status. 
The Ethernet port status parameters are displayed. 
config>port>eth(0/1)# show status 
Megaplex-1 
5. Ports 
Name                  : ETH 0/1                                              
Administrative Status : Up                                                   
Operational Status    : Up                                                   
Connector Type        : SFP In                                               
Auto Negotiation      : Complete                                             
Flow Control          : Enabled Receive                                      
MAC Address           : 00-20-D2-C7-1C-CF                                    
 
 To display the Ethernet fiber port information:  
• 
At the prompt config>port>eth(<slot>/<port>)#, enter show sfp-status. 
SFP 
----------------------------------------------------------------- 
Connector Type                : LC 
Transceiver Code              : 1000BASE-LX 
Vendor Name                   : EOPTOLINK INC 
Vendor Part Number            : EOLS131210RAD 
Vendor Revision               : 1.0 
Vendor Serial Number          : SC2E060077 
Enhanced Monitoring           : No 
Typical Maximum Range (Meter) : 10000 
Wave Length (nm)              : 1310.00 
Fiber Type                    : SM 
Testing Ethernet Ports 
No testing is available. 
Configuration Errors  
The following tables list messages generated by Megaplex-1 when a configuration error on Ethernet 
ports is detected. 
 
Message 
Description 
Can't perform changes on port that is 
bound to flow 
You cannot change parameters of this Ethernet port since it 
is  bound to a flow. 
Megaplex-1 
5. Ports 
Message 
Description 
You have to assign a queue-group 
profile to the Ethernet port 
Queue-group profile is missing for this port. 
Queue group profile does not exist 
You are trying to assign a queue-group profile that is not 
configured in the device. 
You have to assign a queue-mapping 
profile to the Ethernet port 
Queue-mapping profile is missing for this port. 
Viewing Ethernet Port Statistics 
The Ethernet ports feature statistics collection in accordance with RMON-RFC2819.  
 To display the User Ethernet port statistics:  
• 
At the prompt config>slot>port>eth(<slot>/<port>)#, enter show statistics running. 
Ethernet port statistics are displayed. The counters are described in the table below. 
---------------------------------------------------------------
config>port>eth(0/1)# show statistics running 
Running 
--------------------------------------------------------------- 
Counter                    Rx                   Tx 
Total Frames               0                    0 
Total Octets               0                    0 
Unicast Frames             0                    0 
Multicast Frames           0                    0 
Broadcast Frames           0                    0 
 
FCS Errors                 0                    -- 
Error Frames               0                    -- 
Undersize Frames           0                    -- 
Jabber Errors              0                    -- 
Oversize Frames            0                    0 
Unknown Protocol Discarded*0                    -- 
 
64 Octets                  0                    0 
65-127 Octets              0                    0 
128-255 Octets             0                    0 
256-511 Octets             0                    0 
512-1023 Octets            0                    0 
Megaplex-1 
5. Ports 
1024-1518 Octets           0                    0 
1519-2047 Octets           0                    0 
2048-Max Octets            0                    0 
 To display the Management Ethernet port statistics:  
• 
At the prompt config>slot>port>mng-eth(0/0)#, enter show statistics running. 
Ethernet port statistics are displayed. The counters are described in the table below. 
config>port>mng-eth(0/0)# show statistics running 
Running 
--------------------------------------------------------------- 
Counter                    Rx                   Tx 
Total Frames               0                    0 
Total Octets               0                    0 
Unicast Frames             0                    0 
Multicast Frames           0                    0 
Broadcast Frames           0                    0 
 
FCS Errors                 0                    -- 
Error Frames               0                    -- 
Undersize Frames           0                    -- 
Jabber Errors              0                    -- 
Oversize Frames            0                    0 
Parameter 
Description 
Note 
Total Frames 
Total number of frames received/transmitted 
 
Total Octets 
Total number of bytes received/transmitted 
 
Unicast Frames 
Total number of unicast frames received/transmitted 
 
Multicast Frames 
Total number of multicast frames received/transmitted 
 
Broadcast Frames 
Total number of broadcast frames received/transmitted 
 
FCS Errors 
The number of frames received on this interface that are 
an integral number of octets in length but do not pass the 
FCS check 
 
Error Frames 
Total number of error frames received 
 
Undersize Frames 
Total number of undersized frames received  
 
Jabber Errors 
Total number of frames received with jabber errors 
 
Oversize Frames 
Total number of oversized frames received/transmitted  
 

## 5.6 Service Virtual Interfaces  *(p.179)*

Megaplex-1 
5. Ports 
Parameter 
Description 
Note 
Unknown 
Protocol 
Discarded 
Total number of unknown classification discarded frames 
received 
 
64 Octets 
Total number of received/transmitted 64-byte packets  
 
65–127 Octets 
Total number of received/transmitted 65–127-byte 
packets 
 
128–255 Octets 
Total number of received/transmitted 128–255-byte 
packets 
 
256–511 Octets 
Total number of received/transmitted 256–511-byte 
packets 
 
512–1023 Octets 
Total number of received/transmitted 512–1023-byte 
packets 
 
1024–1518 
Octets 
 
Total number of received/transmitted 1024–1518-byte 
packets  
 
1519-2047 
Octets  
Total number of received/transmitted 1519–2047-byte 
packets 
 
2048 - Max 
Octets  
Total number of received/transmitted packets with 2048 
bytes and up to maximum  
 
 To clear the statistics for an Ethernet port: 
• 
User Ethernet port: At the prompt config>port>eth<slot>/<port>)#, enter clear-statistics. 
• 
Management Ethernet port: At the prompt config>port>mng-eth 0/0)#, enter clear-statistics. 
The statistics for the specified port are cleared. 
5.6 Service Virtual Interfaces 
SVIs are virtual ports used in routers. 
Megaplex-1 
5. Ports 
Benefits 
SVIs are used as ingress and egress ports for flows, serving as intermediaries for routers. 
Functional Description 
Service virtual interfaces (SVIs) are logical ports used to link router interfaces with Ethernet ports (via 
Layer-2 flows). 
Note 
Megaplex-1 supports up to 12 SVIs.  
For each SVI port you can optionally define its name and mode (mng+pw).  
The mng+pw mode allows you to have both data and management to reside on the same router 
interface (bound to this SVI). In this mode management and PW reside on the same subnet (router 
interface), same IP address and same logical layer. This mode also enables PW redundancy providing 
both PWs to share the same router interface. 
The router interface bound to this SVI must  be configured with ‘management-access all’. 
Factory Defaults 
By default, no SVIs exist in Megaplex-1. 
Configuring Service Virtual Interfaces 
You can enable and operate service virtual interfaces as explained below. 
 To configure the SVI parameters: 
1. Navigate to configure port svi <port-num> to select the SVI to configure. 
The config>port>svi(<port-num>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Setting the port name 
name <string> 
 
Administratively enabling SVI 
no shutdown 
Using shutdown disables the SVI. 
Megaplex-1 
5. Ports 
Task 
Command 
Comments 
Defining the SVI mode  
pw-mng 
 
Viewing SVI Status 
Follow the instructions below for viewing the SVI status. 
 To view the SVI status: 
• 
At the config>port>svi (<port>)# prompt, enter show status. 
The status information appears as illustrated below.  
config>port>svi(1)# show status 
Name                   : SVI 1 
Type                   : Router 
Administrative Status  : Up 
Operational Status     : Up 
Bind to                : Router 1/1 
MAC Address            : 00-20-D2-C7-1D-4E 
 To view the SVI type: 
• 
At the config>port>svi (<port>)# prompt, enter level-info. 
The information appears as illustrated below.  
MP-1>config>port# level-info 
svi  1 
svi  4  pw-mng 
Configuration Errors  
The tables below list messages generated by Megaplex-1 when a configuration error on serial ports is 
detected. 
Message 
Description 
Unable to delete an SVI which is 
connected to an active flow 
You cannot delete an SVI port that is bound to an active flow. 

## 5.7 Serial Ports  *(p.182)*

Megaplex-1 
5. Ports 
Message 
Description 
Can't perform changes on port that is 
bound to a flow 
You cannot perform changes on an SVI port that is bound to 
a flow 
SVI= # PW must be configured for SVI 
type pw_mng 
You must configure a PW bound to this SVI 
 
SVI= # Maximum number of SVI type 
pw_mng has been reached 
You can configure only one SVI of pw_mng type 
 
SVI= #  SVI type pw_mng cannot be 
mixed with other SVI types 
If you configured one of the SVI’s as pw_mng type, you 
cannot SVIs for other PWs (only management SVIs are 
allowed) 
5.7 Serial Ports  
Applicable Models  
6 or 3 serial ports are available on the following options: 
• 
MP-1/PSR/2GES/6S/C37/1FEU 
• 
MP-1/PSR/2GEU/6S/C37/1FEU 
• 
MP-1/PSR/2GES/6S/4E&M/1FEU 
• 
MP-1/PSR/2GEU/6S/4E&M/1FEU 
• 
MP-1/PSR/2GEU/3S/2FEU 
• 
MP-1/PSR/2GES/3S/2FEU 
In the CLI the ports are designated and numbered serial  1/1 to serial  1/6 (1/3). 
Standards  
The Megaplex-1 serial ports comply with V.35, V.11/RS-422, V.24/ EIA RS-232 and ITU-T Rec. V.110. 
standards. 
Megaplex-1 
5. Ports 
Functional Description 
Serial Interfaces 
The device features 3 or 6 serial sync/async data ports (channels). Data rates are independently 
selectable for each channel and depend on the selected encapsulation mode. The interface terminates 
in 1 or 2 68-pin SCSI-4 female connectors; each connector includes 3 channels. The selection among 
V.35, RS-422 and RS-232 interfaces is done by CLI configuration. Adapter cables, available upon order, 
are offered by RAD to split each interface connector into three separate channel interfaces with 
standard connectors: V.35, RS-422, RS-232, X.21 or V.36.  
Encapsulation Modes  
Serial interfaces behave differently on selection of the specific encapsulation mode: 
• 
None: each channel operates at high speed rates of n×56 or n×64 kbps, where n = 1 to 31 (that 
is, maximum 1984 kbps). 
• 
v110: each channel operates at low speed rates of 2.4, 4.8, 9.6, 19.2 or 38.4 kbps. 
• 
3-bit transitional: the interface provides transitional encoding to transmit asynchronous data at 
rates up to 19.2/38.4 kbps. It operates by encoding asynchronous data in a 3-bit transitional 
code, which is then transmitted over the Megaplex uplink using full DS0 timeslots.  
Main characteristics of these modes are shown in the table below. 
encapsulation-
mode 
rate 
mode 
end-to-end-control 
3bit-
transitional 
{1 | 2 } x 64kbps 
async 
Async rates up to 38.4 are 
supported by oversampling  
no 
rts 
v110 
{2.4 | 4.8 | 9.6 | 19.2 | 38.4} 
sync  
no 
rts 
none  
{1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 
10 | 11 | 12 | 13 | 14 | 15 | 16 | 
17 | 18 | 19 | 20 | 21 | 22 | 23 | 
24 | 25 | 26 | 27 | 28 | 29 | 30 | 
31} x {56kbps | 64kbps} 
N/A 
n x 64 kbps: no 
n x 56 kbps:  
no 
rts 
Encapsulation mode can be set independently per each port. 
Megaplex-1 
5. Ports 
Interface Control Signals  
Each channel has local support for the CTS, RTS, DCD, DSR and DTR lines:  
• 
The CTS line can be independently configured to be always ON, or to track the RTS line. 
• 
The DCD line is constantly ON, except when communications are not possible because of the 
loss of frame synchronization or uplink/PW fail 
• 
The DSR line is always ON (unless end-to-end transmission is enabled and encapsulation is 
v110). In V.110 mode when end-to-end transmission is enabled, it follows the remote DTR. 
• 
The DCD line is also affected by remote RTS, when end-to-end control is selected. 
The interface control signals for end-to-end transfer depend on the selected encapsulation mode (see 
Configuring Serial Port Parameters).  
Factory Defaults 
Megaplex-1 is supplied with all serial ports disabled. Other parameter defaults are listed in the table 
below. 
Parameter  
Default Value 
rate 
1 x 64kbps 
encapsulation-mode  
none  
cts-rts 
no cts-rts (disabled) 
end-to-end-control 
no end-to-end-control (disabled) 
interface  
v35  
Configuring Serial Port Parameters  
 To configure the serial port parameters: 
1. Navigate to configure port serial 1/<port> to select the serial port to configure. 
The config>port>serial>(1/<port>)# prompt is displayed.  
Enter all necessary commands according to the tasks listed below. 
Megaplex-1 
5. Ports 
Task 
Command  
Comments 
Assigning short 
description to port 
name <string> 
Using no name removes the name 
Administratively enabling 
port 
no shutdown 
Using shutdown disables the port 
Setting the data rate of 
this port in kbps. The 
selection depends on the 
encapsulation type 
 
encapsulation-
mode=none: rate {1 | 
2 | 3 | 4 | 5 | 6 | 7 | 8 
| 9 | 10 | 11 | 12 | 13 
| 14 | 15 | 16 | 17 | 
18 | 19 | 20 | 21 | 22 
| 23 | 24 | 25 | 26 | 
27 | 28 | 29 | 30 | 31} 
x {56kbps | 64kbps} 
 
 
    
encapsulation-
mode=v110: rate {2.4 
| 4.8 | 9.6 | 19.2 | 
38.4 }  
 
encapsulation-
mode=3bit-
transitional: rate {1 | 
2 } x 64kbps 
 
Selecting the 
encapsulation mode  
encapsulation-mode 
{v110 |  3bit-
transitional | none } 
Sync traffic:  v110 and none modes are supported 
Async traffic:  3bit-transitional is supported 
Setting CTS line to track 
the state of the local RTS 
line 
cts-rts 
 
Using no cts-rts sets the CTS line continously to on. 
Megaplex-1 
5. Ports 
Task 
Command  
Comments 
Configuring end-to-end 
control  
 
end-to-end-control 
[rts]  
When configured, the state of the local RTS and DTR lines 
are reflected by the remote DCD and DSR line, 
respectively (DTR and DSR lines are relevant only for v110 
encapsulation mode). 
Using no end-to-end-control disables end-to-end control.  
When encapsulation-mode=3bit-transitional, only the 
state of the local RTS line can be transmitted end-to-end 
to the remote DCD line.  
The RTS line is functioning as follows: 
• RTS on: traffic flow is established to the  remote 
equipment, remote DCD on  
• RTS off: 0xC0 code is sent to remote equipment, 
remote DCD off 
When encapsulation-mode=v110, the state of the local 
RTS and DTR lines are reflected by the remote DCD and 
DSR line, respectively.  
The RTS line is functioning as follows: 
• RTS on: traffic flow is established to the  remote 
equipment, remote DCD on  
• RTS off: traffic flow is established to remote 
equipment, remote DCD off 
The DTR line is functioning as follows: 
• DTR on: traffic flow is established to the  remote 
equipment, remote DSR on  
• DTR off: traffic flow is established to remote 
equipment, remote DSR off  
When encapsulation-mode=none only the state of the 
local RTS line can be transmitted end-to-end to the 
remote DCD line. This selection is available only for n x 56 
kbps data rates. For n x 64 kbps data rates, this selection 
is not valid.   
The RTS line is functioning as follows: 
• RTS on: traffic flow is established to the  remote 
equipment, remote DCD on  
• RTS off: traffic flow is established to remote 
equipment, remote DCD off 
Setting the physical 
interface  
interface {rs-232 | v35 
| rs-422}  
 
Megaplex-1 
5. Ports 
Example 
The following section illustrates how to configure serial port 5: 
• 
Data rate 128 kbps.  
• 
Set CTS line to track the state of the local RTS line 
• 
Administratively enable the port. 
• 
Leave all other parameters disabled or at their defaults. 
config>port>serial(1/5)# rate 2 x 64kbps 
config>port>serial(1/5)# cts-rts  
config>port>serial(1/5)# no shutdown  
Viewing Status Information  
 To view the status of a serial port: 
1. Navigate to config>port> serial (1/<port>)#  
2. Type show status. 
The status is displayed, for example as follows:  
config>port>serial(1/3)# show status 
Name                  : SERIAL 1/3 
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
Megaplex-1 
5. Ports 
Viewing Serial Port Statistics  
Serial ports feature RAD proprietary statistical diagnostics.  
 To display the statistics of a serial port: 
1. Navigate to config>port> serial> (1/<port>)#  
2. Type show statistics. 
The statistics is displayed, for example as follows:  
# config port serial 1/3 
config>port>serial(1/3)# show statistics 
DTE Rx Counter   : 609087 
DTE Tx Counter   : 609087 
WAN Rx Violation : 0 
Parameter 
Description 
DTE Rx Counter  
  
Number of data transitions on the input data wires since last reset or power-up 
(Rx from DTE)  
DTE Tx Counter    
Number of data transitions on the output data wires since last reset or power-up 
(Tx to DTE)  
WAN Rx Violation  
Number of 3-bit transitional protocol code violation since last reset or power-up  
 To clear the statistics on a serial port: 
1. Navigate to the corresponding port. 
2. Enter clear-statistics. 
The statistics for the specified port are cleared. 
Configuration Errors  
The tables below list messages generated by Megaplex-1 when a configuration error on serial ports is 
detected. 
Message 
Description 
Serial port: end-to-end control and 
rate mismatch  
Encapsulation mode none and rate nx64 doesn’t support 
end-to-end control.  
Serial port: Fail to get data from DB 
Database problem. Try to reconfigure the serial port. 
Megaplex-1 
5. Ports 
Testing Serial Ports  
The following test and diagnostics functions available on each serial port: 
• 
Local digital loopback  
• 
Remote digital loopback  
The loopbacks are schematically shown in the figure below. 
 
 
Local Digital Loopback (Local Loop) 
The local loopback is a digital loopback performed at the digital output of a selected channel, by 
returning the local Rx input signal to the local Tx output. The transmit signal is still sent to the remote 
Megaplex unit.  
While the loopback is connected, the local serial port should receive its own signal. 
Remote Digital Loopback (Remote Loop) 
The remote loopback is a digital loopback performed at the digital input of the port, by returning the 
digital receive signal of the port to the remote unit via the transmit path. The receive signal remains 
connected to the local user, and can be received by user.  
While the loopback is connected, the remote serial port should receive its own signal. 
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the Megaplex-1. 
Therefore, when you initiate a loopback, you have the option to limit its duration to an interval in the 
range of 1 through 30 minutes.  

## 5.8 T1 Ports  *(p.190)*

Megaplex-1 
5. Ports 
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-1 before 
this timeout expires.  
The default is infinite duration (without timeout). 
Activating the Loopbacks  
 To perform a loopback on the serial port: 
1. Navigate to configure port serial 1/<port> to select the serial port to configure. 
The config>port>serial>(1/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Activating and configuring 
the direction and the 
duration of the loopback  
loopback {local | remote} 
[duration <duration in minutes 
1..30> ]  
• Local – local loopback.  
• Remote – remote loopback 
Stopping the loopback 
 
no loopback 
 
5.8 T1 Ports  
Applicable Models 
8 E1/T1 ports are available on the following options: 
• 
MP-1/PSR/2GES/4FEU/6S/8E1T1 
• 
MP-1/PSR/2GEU/4FEU/6S/8E1T1 
In the CLI, the T1 ports are designated and numbered t1  1/1 to t1  1/8. 
Megaplex-1 
5. Ports 
Standards  
The T1 link interfaces meet the applicable requirements of ANSI T1.403 (Physical layer), ANSI T1.107, 
AT&T PUB-54016 (framing), and AT&T TR-62411 (jitter).  
Functional Description 
Megaplex-1 features 8 E1/T1 interfaces. The type of the interface is configured on the port> level by the 
“pdh-frame-type” command. This command applies to all the 8 interfaces simultaneously (you cannot 
configure part of the ports to E1 and another part to T1). The default configuration is E1. 
Framing  
The T1 ports can be independently configured in accordance with the desired ITU-T framing mode and 
signaling formats: 
• 
D4 (SF) framing (12 frames per multiframe)  
• 
ESF framing (24 frames per multiframe)  
• 
Unframed mode: enables transparent transfer of 1.544 Mbps streams, including streams with 
proprietary framing.  
The framer automatically adds the appropriate overhead. Unused timeslots are filled with a 
user-specified idle code. The user can also select specific timeslots to be transferred (DS0 cross-
connect). 
The framing mode can be independently selected for each T1 port. It is configured by means of line-type 
parameter. 
Line Interface  
Each T1 line interface has an integral CSU, which enables operation with line attenuations up to 34 dB. 
The nominal transmit level is ±3V.  
The CSU transmit level must be adjusted to ensure reliable operation of the network. It can be 
attenuated by 7.5, 15, or 22.5 dB, for compliance with FCC Rules Part 68A. This adjustment minimizes 
the interference your transmit signal causes to other users that transmit their signals on other pairs of 
the same cable. The required setting depends mainly on the length of the cable that connects the T1 
port and the first repeater down the line.  
Megaplex-1 
5. Ports 
Repeaters are usually spaced a mile apart. They are therefore designed to optimally handle signals 
attenuated by one mile length of cable. If the T1 port were closer, the repeater would receive your 
signal at a higher level. This will not significantly improve the handling of your signal, but will certainly 
increase the interference coupled from your pair to repeaters that serve other pairs in the cable. To 
prevent this, you can select an attenuation value that will bring your signal level closer to the expected 
repeater signal level. This is achieved by connecting, as required, one, two, or three artificial line 
sections in series with your T1 transmit signal. Each line section introduces a nominal attenuation of 
7.5 dB (equivalent to the attenuation of approximately 1000 feet of cable). Your system administrator or 
data carrier will give you the proper setting for each port. 
The line interface can also emulate a DSU interface. The selection CSU/DSU is defined by the line-
interface parameter. The relative output transmit level of the port is selected by means of the line-
buildout parameter. 
Line Length 
When configured for DSU emulation, the line transmit signal is user-adjustable for line lengths of 0 to 
655 feet in accordance with AT&T CB-119. The transmit signal mask is selected in accordance with the 
transmit line length, to meet DSX-1 requirements, as specified by AT&T CB-119. The following selections 
are available: 
• 
0 – 133 Ft 
• 
133 – 266 Ft 
• 
266 – 399 Ft 
• 
399 – 533 Ft 
• 
533 – 655 Ft. 
These values define the length of the cable (in feet) connected between the port connector and the 
network access point. 
Zero Suppression  
Zero suppression is user-selectable, separately for each port: transparent (AMI) coding or B8ZS. It is 
configured by means of line-code parameter. 
Interface Type 
The external T1 links have 100 Ω balanced interfaces.  
Megaplex-1 
5. Ports 
Handling of T1 Alarm Conditions 
The external and internal T1 ports support two types of indications in the individual timeslots: idle 
timeslots and out-of-service (OOS) indications. 
• 
Idle Timeslot Indication. A special code can be transmitted in empty timeslots (timeslots which 
do not carry payload).  
• 
OOS Indications. The OOS code is inserted in individual timeslots to signal the equipment routed 
to one of the module ports that the link connected to the external port is out-of-service (e.g., 
because of a loss of frame synchronization).  
The idle code and OOS indications can be independently configured for each module port. Moreover, 
separate OOS codes can be transmitted in the timeslots, in accordance with the type of payload carried 
by each timeslot (voice or data). 
T1 Payload Processing  
T1 ports support two main types of payload per timeslot: 
• 
Data timeslots: timeslots which are transparently transferred from port to port. In general, it is 
assumed that no CAS is associated with data timeslots.  
• 
Voice timeslots: timeslots carrying PCM-encoded payload, with A-law companding for T1 ports 
and µ-law companding for T1 ports. When transferred between ports with different standards 
(for example, between E1 and T1 ports), these timeslots are converted by Megaplex-1. 
In general, CAS is always associated with voice timeslots, and therefore it must also be 
converted when transferred between ports with different standards.  
The flow of payload carried by voice timeslots is normally bidirectional (full duplex connection). 
However, it is also possible to define unidirectional flows, called unidirectional broadcasts, from one 
source (a timeslot of a source port) to multiple destinations (each destination being a selected timeslot 
of another port).  
In case of data timeslots, the flow of payload is normally unidirectional. If the application requires 
bidirectional flows, cross-connect must be configured symmetrically for both directions.  
OOS Signaling 
If the communication between modules located in different Megaplex units fails, e.g., because loss of 
main link synchronization, etc., it is necessary to control the state of the signaling information at the two 
ends of the link. This activity, called out-of-service (OOS) signaling, is performed by the T1 interfaces and 
can be selected in accordance with the specific application requirements, on a per-link basis.  
Megaplex-1 
5. Ports 
The OOS signaling options supported by the T1 module ports are as follows: 
• 
Signaling forced to idle state for the duration of the out-of-service condition (force-idle). This 
option is suitable for use with all voice interfaces. 
• 
Signaling forced to busy state for the duration of the out-of-service condition (force-busy). This 
option is suitable for use with E&M and FXO interfaces, but not with FXS interfaces. 
• 
Signaling forced to idle state for 2.5 seconds, and then changed to busy state for the remaining 
duration of the out-of-service condition (idle-busy). This option is suitable for use with E&M and 
FXO interfaces, but not with FXS interfaces. 
• 
Signaling forced to busy state for 2.5 seconds, and then changed to idle state for the remaining 
duration of the out-of-service condition (busy-idle). This option is suitable for use with all the 
voice interfaces. 
Factory Defaults 
Megaplex-1 is supplied with all t1 ports disabled. Other parameter defaults are listed in the table below. 
Parameter  
Default Value 
line-type 
esf  
line-interface  
dsu  
idle-code  
0x7f 
out-of-service - voice  
00 
out-of-service - data  
00 
out-of-service - signaling   
force-idle 
line-code  
b8zs 
line-length  
0-133 
line-buildout  
0db  
tx-clock-
source                                        
domain 1 
Megaplex-1 
5. Ports 
Configuring a T1 Port  
 To set all the device ports to T1: 
1. Navigate to configure port pdh-frame-type and type t1.  
The interface type of all the device ports changes from e1 to t1. 
Note 
If any cross-connect exists over one of the ports or one of the e1/t1 ports is 
configured as a clock source, Megaplex-1 displays this configuration and 
rejects the command. If this is the case, delete the specified cross-
connect/clock source and repeat the command.  
 To configure the T1 port parameters: 
1. Navigate to configure port t1 1/<port> to select the T1 port to configure.  
The config>port>t1>(1/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
Assigning short 
description to port 
name <string> 
Using no name removes the name 
Administratively 
enabling port 
no shutdown 
Using shutdown disables the port 
Specifying T1 framing 
mode  
line-type {unframed | esf | sf} 
 
<unframed>  – Unframed 
 <esf>  – Extended Super Frame (ESF) 
 <sf>  –   Super Frame (SF) 
Setting the line code 
used by the port, and 
the zero suppression 
method 
line-code {ami | b8zs}  
 
Specifying T1 operation 
mode     
line-interface {dsu | csu }      
<dsu>    : DSU (short haul) 
<csu>      : CSU (long haul) 
Specifying the length of 
the T1 line in DSU mode 
line-length {0-133 | 134-266 | 267-
399 | 400-533 | 534-655}  
 
<0-133>              : 0-133 feet 
 <134-266>            : 134-266 feet 
 <267-399>            : 267-399 feet 
 <400-533>            : 400-533 feet 
 <534-655>            : 534-655 feet 
Megaplex-1 
5. Ports 
Task 
Command  
Comments 
Specifying  the code 
transmitted to fill 
unused timeslots in T1 
frames 
idle-code <00 to FF (hexa)>     
The available selections are [0x40 to 0x7F] 
and [0xC0 to 0xFF]  
Transmitting an 
out-of-service signal 
(OOS)   
out-of-service [voice <00 to FF 
(hexa)>] [data <00 to FF (hexa)>] 
[signaling {force-idle | force-busy | 
idle-busy | busy-idle}]  
  
<force-idle>    : Force idle (0) 
<force-busy>  : Force busy (1) 
<busy-idle>    : Force busy (1) for 2.5 
seconds 
<idle-busy>    : Force idle (0) for 2.5 seconds 
The hexadecimal number is in the range of 0 
to FF (two digits)  
The selected out-of-service data code is also 
sent during out-of-service periods instead of 
the external data stream when the 
unframed mode is used  
out-of-service voice selection is relevant 
only when the esf mode is selected  
Specifying the line 
build-out (relative 
output transmit level of 
the port) 
line-buildout {0db | -7dot5db | -
15db |  
-22dot5db}  
<0db>: 0dB 
<-7dot5db>: -7.5dB 
<-15db>: -15dB 
<-22dot5db>: -22.5dB 
 CSU mode only 
Selecting the timing 
reference source used 
by the port for the 
transmit-to-network 
direction 
tx-clock-source loopback  
tx-clock-source domain <number>  
tx-clock-source through-timing     
 
loopback – Clock received from the E1/T1 
port 
domain – Clock provided by system clock 
domain 
through-timing – Clock received from PW  
Configuring collection 
of performance 
management statistics 
for the port, that are 
presented via the 
RADview Performance 
Management portal 
pm-collection  
{interval <seconds 1..900> | on-
interval-close} 
PM collection can be enabled at a defined 
interval or before an interval expires.  
Type no pm-collection to disable PM 
statistics collection for the E1 port. 
Note: In addition to enabling PM statistics 
collection for the port, it must be enabled for 
the device. Refer to the Performance 
Management section in the Monitoring and 
Diagnostics chapter for details. 
Megaplex-1 
5. Ports 
Example  
The following example illustrates how to configure the T1 port labeled 1: 
• 
Set the T1 framing mode to SF. 
• 
Set the restoration time to 10 sec. 
• 
Set the line code to AMI. 
• 
Set the idle code to 8E. 
• 
Administratively enable the port. 
• 
Leave all other parameters disabled or at their defaults. 
config>port>t1(1/1)# line-type sf 
config>port>t1(1/1)# line-code ami  
config>port>t1(1/1)# idle-code 0x7F 
config>port>t1(1/1)# no shutdown 
Viewing a T1 Port Status 
Follow the instructions below for viewing the status of the T1 port 1/1 as an example. 
 To view the T1 port status: 
• 
At the config>port>t1(<slot>/<port>)# prompt, enter show status. 
The status information appears as illustrated below.  
config>port>t1(1/1)# show status 
Name                  : 
Administrative Status : Down 
Operation Status      : Up 
Interface Type        : Balanced 
Connector Type        : DB44 
Loopback : Off 
Testing T1 Ports  
The following test and diagnostics functions available on each T1 port: 
• 
Local digital loopback  
Megaplex-1 
5. Ports 
• 
Remote digital loopback.  
The loopbacks are schematically shown in the figure below. 
 
 
 
Local Digital Loopback (Local Loop) 
The local loopback is a digital loopback performed at the digital output of a selected port, by returning 
the local Rx input signal to the local Tx output. The transmit signal is still sent to the remote Megaplex 
unit.  
While the loopback is connected, the local T1 port should receive its own signal. 
Remote Digital Loopback (Remote Loop) 
The remote loopback is a digital loopback performed at the digital input of the port, by returning the 
digital receive signal of the port to the remote unit via the transmit path. The receive signal remains 
connected to the local user, and can be received by user.  
While the loopback is connected, the remote T1 port should receive its own signal. 
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the Megaplex-1. 
Therefore, when you initiate a loopback, you have the option to limit its duration to an interval in the 
range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-1 before 
this timeout expires.  
The default is infinite duration (without timeout). 
Megaplex-1 
5. Ports 
Activating the Loopbacks  
 To perform a loopback on the t1 port: 
1. Navigate to configure port t1 1/<port> to select the serial port to configure. 
The config>port>t1>(1/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Activating and configuring 
the direction and the 
duration of the loopback  
loopback {local | remote} 
[duration <duration in minutes 
1..30> ]  
• Local – local loopback.  
• Remote – remote loopback 
• Stopping the loopback 
 
no loopback 
•  
Configuration Errors  
The following tables list messages generated by Megaplex-1 when a configuration error on T1 ports is 
detected. 
 
Message 
Description 
Illegal tx-clock-source configured  
You cannot change the tx-source clock on the T1 port 
(default=system) if it is not connected to DS1 port 
Displaying T1 Port Statistics  
T1 ports of Megaplex-1 feature the collection of statistical diagnostics per relevant parts of ITU-T G.826, 
thereby allowing the carrier to monitor the transmission performance of the links.  
 To display the T1 port statistics: 
• 
At the prompt config>slot>port>t1(<slot><port>])#, enter show statistics followed by the 
parameters listed below.  
Megaplex-1 
5. Ports 
Task 
Command 
Comments 
Displaying 
statistics 
show statistics {total | all | all-intervals |  
current}  
 
 
  
• total –total statistics of last 
96 intervals  
• current –current statistics 
• all-intervals – statistics for 
all valid intervals 
• all –all statistics: first current 
statistics, then statistics for 
all valid intervals, and finally 
total statistics 
Displaying 
statistics for a 
specific interval 
show statistics interval <interval-num 1..96> 
 
 
T1 port statistics are displayed.   
Note 
LOFC and Rx Frames Slip are displayed for framed formats only.  
For example: 
Current statistics: 
config>port> t1(1/2)# show statistics current 
Current 
--------------------------------------------------------------- 
Time Elapsed (Sec) : 191 
Valid Intervals    : 2 
ES             : 0 
SES            : 0 
UAS            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
Statistics for interval 67: 
config>port> t1(3/1)# show statistics interval 67 
Interval Number : 67 
 
Interval 
--------------------------------------------------------------- 
ES             : 16 
SES            : 1 
UAS            : 589 
Rx Frames Slip : 0 
LOFC           : 0 
Megaplex-1 
5. Ports 
Total statistics: 
 
config>port> t1(1/2)# show statistics total 
Total 
--------------------------------------------------------------- 
ES             : 2 
SES            : 0 
UAS            : 0 
Rx Frames Slip : 0 
LOFC           : 0 
All statistics:  
 
config>port>t1(1/2)# show statistics all 
Current 
--------------------------------------------------------------- 
Time Elapsed (Sec) : 171 
Valid Intervals    : 2 
config>port>e1(1/2)# 
 
ES             : 0 
SES            : 0 
UAS            : 0 
 
Rx Frames Slip : 0 
LOFC           : 0 
 
Interval Number : 1 
 
Interval 
--------------------------------------------------------------- 
ES             : 0 
SES            : 0 
UAS            : 0 
 
Rx Frames Slip : 0 
LOFC           : 0 
 
Interval Number : 2 
 
Interval 
--------------------------------------------------------------- 
ES             : 2 
SES            : 0 
UAS            : 0 
 
Rx Frames Slip : 0 
LOFC           : 0 
Megaplex-1 
5. Ports 
 
Total 
--------------------------------------------------------------- 
ES             : 2 
SES            : 0 
UAS            : 0 
 
Rx Frames Slip : 0 
LOFC           : 0 
The counters are described in the following tables.  
E1 Port Statistics Parameters – Current 15-Minute Interval 
Parameter 
Description 
ES  
Displays the number of errored seconds in the current 15-minute interval. 
An errored second is any second not declared a UAS in which a OOF (Out of 
Frame) or CRC (Cyclic Redundancy Check error) occurred. 
UAS  
Displays the number of unavailable seconds (UAS) in the current interval. 
An unavailable second is one of the following: 
• Any second following 10 consecutive SES seconds 
• A second for which any of the previous 10 consecutive seconds was also a UAS 
and any of the previous 10 consecutive seconds was a SES. 
SES  
Displays the number of severely errored seconds (SES) in the current interval. 
A SES is any second not declared a UAS which contains an OOF or more than 320 
CRC errors. 
LOFC  
Displays the number of LOFC in the current interval. 
The loss of frame (LOF) counter counts the loss of frame alignment events. The 
data is collected for the current 15-minute interval. 
Rx Frames Slip 
Displays the number of Rx Frames Slips in the current 15-minute interval. 
A CSS is a second with one or more controlled slip events. 
Time elapsed 
The elapsed time (in seconds) since the beginning of the current interval, in 
seconds. The range is 1 to 900 seconds. 
Valid Intervals 
The number of elapsed finished 15-min intervals for which statistics data can be 
displayed, in addition to the current (not finished) interval (up to 96). 
E1 Port Statistics Parameters – Selected 15-Minute Interval  
Parameter 
Description 
ES  
Displays the total number of errored seconds (ES) in the selected interval 

## 5.9 Voice Ports  *(p.203)*

Megaplex-1 
5. Ports 
Parameter 
Description 
UAS 
Displays the total number of unavailable seconds (UAS) in the selected interval 
SES  
Displays the total number of severely errored seconds (SES) in the selected interval 
LOFC  
Displays the total number of loss of frame alignment events in the selected interval 
Rx Frames Slip 
Displays the total number of loss of of Rx Frames Slip events in the selected interval 
Interval number 
The number of interval for which statistics is displayed.  
E1 Port Statistics Parameters – Total Statistics 
Parameter 
Description 
ES  
Displays the total number of errored seconds (ES) since statistics are available 
UAS 
Displays the total number of unavailable seconds (UAS) since statistics are available 
SES  
Displays the total number of severely errored seconds since statistics are available 
LOFC  
Displays the total number of loss of frame alignment events since statistics are 
available 
Rx Frames Slip 
Displays the total number of loss of of Rx Frames Slip events since statistics are 
available 
Clearing Statistics 
 To clear the statistics for a T1 port: 
• 
At the prompt config>port>t1<slot>/<port>)#, enter clear-statistics. 
The statistics for the specified port are cleared. 
5.9 Voice Ports  
Applicable Models 
Voice ports are available on the following models:  
Megaplex-1 
5. Ports 
• 
MP-1/PSR/2GES/6S/4E&M/1FEU, MP-1/PSR/2GEU/6S/4E&M/1FEU – 4E&M voice ports 
• 
MP-1/PSR/2GES/8FXS/4E&M, MP-1/PSR/2GEU/8FXS/4E&M – 4E&M + 8 FXS voice ports 
The following parameters can be configured for the voice ports:  
• 
Port name 
• 
Administrative status 
• 
End-to-end signaling transfer method  
• 
Number of wires for E&M channels 
• 
Analog signaling method for FXS channels 
• 
Analog signaling profile  
• 
E&M signaling standard 
• 
Impedance for the FXS interface  
• 
Cadence for the FXS interface  
Standards  
The Megaplex-1 voice ports comply with following standards:  
Modulation Technique  
PCM: per ITU-T Rec. G.711 and AT&T Pub. 43801 
Analog Interface 
ITU-T Rec. G.712 
E&M Signaling Method  
• EIA RS-464 Type I 
• EIA RS-464 Type II, III and V (British Telecom SSDC5) using 
internal -12 VDC in place of -48 VDC 
FXS Signaling Modes  
• EIA RS-464 loop-start and wink-start 
Functional Description 
All the voice interfaces provide high-quality voice channels. The functional difference between the 
various interfaces is in the signaling interface and mode.  
The analog interface:  
• 
E&M: user-selectable for 2-wire or 4-wire 
Megaplex-1 
5. Ports 
• 
FXS: always 2-wire 
The voice interfaces work with PCM encoding. 
The user can select the companding law, µ-law or A-law, in accordance with system requirements. In 
accordance with ITU-T Rec. G.711, the A-law should be used when working in the E1 environment and 
the µ-law should be with the T1 environment. However, the user can select the desired companding 
law, µ-law or A-law, in accordance with the specific system requirements. 
To increase application flexibility, the nominal audio transmit and receive levels can be adjusted over a 
wide range (see the following table).  
Transmit and Receive Levels for Various Interfaces  
Interface 
Transmit (Analog to Digital) 
                 [dbm] 
  min                        max 
Receive (Digital to Analog) 
            [dbm] 
 min                  max 
E&M 2W  
-8 
+5 
-17 
+2 
E&M 4W (when there is a 
mix of 2W/4W ports) 
-8 
-17 
+3.5 
E&M 4W (all connected 
ports) 
-17 
+5 
-17 
+9 
FXS 
-5 
+5 
-17 
+1 
Due to the high quality audio reproduction, DTMF signaling is transparently transferred, inband. 
Therefore, the user can use DTMF signaling as usual, e.g., can operate the telephone set keypad to 
access voice mail systems, interactive systems, etc.  
Numbering 
The following table shows how to refer to the ports when configuring them with CLI commands. 
Port  
Description 
Port Number 
E&M 1..4 
E&M voice ports 
1/1..1/4 
FXS 1..8 
FXS voice ports 
1/5..1/12 
Megaplex-1 
5. Ports 
E&M Interface  
The E&M interface is user-selectable 2-wire or 4-wire analog interface using E&M signaling. The 
interface type (2-wire or 4-wire) can be independently selected for each channel.  
The E&M interface supports four types of E&M signaling: EIA RS-464 types I, II, III and V (similar to 
British Telecom SSDC5). The figure below shows the equivalent signaling circuits for the different 
signaling modes. The signaling type should be the same for all the four channels. 
• 
EIA RS-464 Type I signaling standard is supported without any external power supply. 
• 
EIA RS-464 Type II, III and V (BT SSDC5) signaling standards are supported by means of the 
internal -12 VDC power supply of the chassis. The -12 VDC voltage is suitable for most PBX 
systems. However, for full support of the EIA RS-464 Type II, III and V (BT SSDC5) signaling 
standards, a -48 VDC signaling voltage is required.  
The E&M interface provides signaling at +12V for applications that require positive signaling 
voltage (for example, radio transmitters). In this mode, the voice port sends signaling to the 
radio transmitters by connecting GND to the E pin.  
Megaplex-1 
5. Ports 
 
E&M Equivalent Signaling Circuits 
Megaplex-1 
5. Ports 
The E&M Voice Activity Detection (VAD) feature allows Megaplex to identify whether an E&M voice 
channel is connected and active by analyzing PCM voice samples. Once enabled using the activity-
detection configuration parameter, the detected connection status is shown in the E&M CLI status 
screen as Up (connected/active) or Down (disconnected/not active).  
FXS Characteristics 
The FXS interface is a 2-wire analog interface supporting the FXS loop-start signaling, for direct 
connection to subscriber telephone sets. The interface also supports wink-start signaling.  
To enable wink-start signaling, the FXS interface uses feed voltage (battery) polarity reversal.  
The subscriber feed and ring voltages for the FXS interfaces is generated on the interface itself, by a 
ringer.  
Analog Signaling Profile 
Analog voice signals are digitized using PCM (Pulse-code modulation), in compliance with ITU-T G.711 
and AT&T Pub. 43801 standards, the signaling information of each voice channel is carried by means of 
up to four bits (signaling bits), designated by the applicable standards as bits A, B, C and D. The analog 
signaling format can be modified by defining analog signaling profiles. The analog signaling profile is 
configured per channel and per direction. For more information on configuring analog signaling profiles, 
see Analog Signaling Profiles.  
Factory Defaults 
Megaplex-1 is supplied with all voice ports disabled. Other parameter defaults are listed in the table 
below. 
Parameter  
Default Value 
General 
 
analog-signaling-profile 
sig_over_a_bit 
coding 
a-law 
rx-sensitivity  
0.0 dbm 
signaling  
E&M ports: no signaling (disabled)  
FXS ports: signaling (enabled)  
tx-gain  
0.0 dbm 
Megaplex-1 
5. Ports 
Parameter  
Default Value 
FXS 
 
analog-signaling  
loop-start  
cadence 
local  
forward-disconnect 
250msec 
impedance 
600 
ring-voltage  
normal 
E&M 
 
e-m-type  
ssdc5  
activity-detection  
disabled  
wires  
2 
Configuring Voice Port Parameters 
  To configure the voice port parameters: 
1. Navigate to configure port voice 1/<port> to select the voice port to configure. 
The config>port>voice>(1/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
General 
 
 
Assigning short description 
to port 
name <string> 
Using no before name removes the name 
Administratively enabling 
port 
no shutdown 
Using shutdown disables the port 
Specifying the analog 
signaling profile 
analog-signaling-profile <profile-
name> 
By default the analog signaling profile is 
sig_over_a_bit 
Megaplex-1 
5. Ports 
Task 
Command  
Comments 
Specifying the companding 
law to be used by the voice 
port 
coding {a-law | u-law} 
 
a-law  - A-law coding, intended for use 
on E1 networks 
u-law -µ-law coding, intended for use on 
T1 networks     
The selection is done per port.    
Note: When working with T1 links, it is 
also recommended to set t1 on the port> 
level using “pdh-frame-type” command.  
Selects the nominal output 
level of the receive path 
rx-sensitivity <value in dbm> 
 
The input level can be set in 0.5 dB steps 
in the range of +9 dBm to -17 dBm, 
depending on the interface type (see 
Transmit and Receive Levels for Various 
Interfaces table) 
Enabling the end-to-end 
signaling transfer for the 
port 
signaling  
 
Using no signaling  means that port 
signaling is not transferred 
Selecting the nominal input 
level of the transmit path 
tx-gain <value in dbm>  
 
The input level can be set in 0.5 dB steps 
in the range of +5 dBm to -17 dBm, 
depending on the interface type (see 
Transmit and Receive Levels for Various 
Interfaces table) 
FXS only 
 
 
Specifying the analog 
signaling method used for all 
FXS ports 
analog-signaling {loop-start | 
wink-start}  
 
Specifying if the cadence of 
the ring is generated locally 
or translated directly from 
the received signaling bit 
cadence {local | transparent} 
 
 
Specifying the amount of 
time during which the 
battery voltage is 
disconnected by the FXS port 
after a far-end notification 
has been received 
forward-disconnect {250msec | 
500msec | 750msec | 1sec | 2sec} 
 
 
Specifying the line 
impedance 
impedance {600 | 900} 
 
Megaplex-1 
5. Ports 
Task 
Command  
Comments 
Specifying the ring voltage 
value 
ring-voltage {normal | high} 
• normal – 54 Vrms 
• high – 85 Vrms 
For each pair of ports (1-2, 3-4, 5-6 or 7-
8) only one channel can be set to 'high', 
the other one must be set to ‘shutdown’. 
E&M only 
 
 
Configuring VAD to indicate 
whether E&M interface is 
active or not  
[no] activity-detection    
 
Specifying the E&M signaling 
standard 
e-m-type {1 | 2 | 3 | ssdc5 | pos}  
 
The E&M signaling type must be the 
same for all voice ports. 
Specifying the interface to 
be used by the voice 
channels 
wires {2 | 4}  
Selection between 2-wire and 4-wire 
interface is available only for the E&M 
interface. 
Can be independently selected for each 
port. 
Example  
The following section illustrates how to configure the voice FXS port 1:  
• 
Set -µ-law coding 
• 
Enable signaling 
• 
Administratively enable the port 
• 
Leave all other parameters disabled or at their defaults.  
config# port voice 1/5 no shutdown 
config# port voice 1/5 coding a-law 
config# port voice 1/5 signaling   
Viewing a Voice Port Status 
Follow the instructions below for viewing the status of a voice port. 
Megaplex-1 
5. Ports 
 To view the voice port status: 
• 
At the config>port>voice(1/<port>)# prompt, enter show status. 
The status information appears as illustrated below.  
config>port>voice(1/12)# show status 
Name                  : VOICE 1/12 
Administrative Status : Up 
Operation Status      : Down 
Connector Type        : RJ45 
Loopback Type         : None 
 
Interface Type : E&M 
Rx ABCD        : 0101 
Tx ABCD        : 0101 
The status display provides information about: 
 
Administrative status  
 
Operational status (for E&M modules Up corresponds to the voice activity on the channel (in 
the case VAD (voice activity detection) is enabled) 
 
Connector type 
 
Status of loopback activated on the port (None, Local, Remote, Local Tone Injection, Remote 
Tone Injection) 
 
Interface type and signaling bits (VS modules only) 
Testing Voice Ports 
The test and diagnostics functions available on each voice channel are: 
• 
Local digital loopback  
• 
Remote digital loopback  
• 
Forward (remote) tone injection 
• 
Backward (local) tone injection. 
The tests are schematically shown in the figure below. 
Megaplex-1 
5. Ports 
 
Local Digital Loopback (Local Loop) 
The local loopback is a digital loopback performed at the digital output of a selected port, by returning 
the local Rx input signal to the local Tx output. The transmit signal is still sent to the remote Megaplex 
unit.  
While the loopback is connected, the local voice channel should receive its own signal, e.g., a strong 
sidetone should be heard in the earpiece if the channel is connected to a telephone set. 
Remote Digital Loopback (Remote Loop) 
The remote loopback is a digital loopback performed at the digital input of the port, by returning the 
digital received signal of the channel to the remote unit via the transmit path. The receive signal remains 
connected to the local user, and can be received by user.  
While the loopback is connected, the remote voice port should receive its own signal, e.g., a strong 
sidetone should be heard in the earpiece if the channel is connected to a telephone set. 
Remote (Forward) Tone Injection 
The test tone is a data sequence repeating at a rate of 1 kHz. This data sequence is identical to the data 
sequence that would have been generated if a 1-kHz signal having a nominal level of 1 mW (0 dBm0) 
were applied to the input of the channel codec. 
The tone is injected to the local transmit path, instead of the transmit signal of the channel. The signal 
received from the other end remains connected to the local subscriber. 
While the remote tone injection is activated, the remote user should hear the tone in the earpiece if the 
channel is connected to a telephone set. 
Megaplex-1 
5. Ports 
Local (Backward) Tone Injection 
When the local test tone injection is enabled, the test tone (a data sequence repeating at a rate of 1 
kHz) is injected to the local receive input of the channel decoder, instead of the received signal of the 
channel, and the resulting analog signal is supplied to the local subscriber. The signal received from the 
other end is disconnected from the local subscriber. 
While the local tone injection is activated, the local user should hear the tone in the earpiece if the 
channel is connected to a telephone set. 
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the Megaplex-1. 
Therefore, when you initiate a loopback, you have the option to limit its duration to an interval in the 
range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-1 before 
this timeout expires.  
The default is infinite duration (without timeout). 
Activating Loopbacks and Tone-Inject Tests  
 To perform a loopback on the voice port: 
1. Navigate to configure port voice 1/<port> to select the voice port to configure. 
The config>port>voice>(1/<port>)# prompt is displayed.  
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
loopback {local | remote} [tone-
inject] [duration <duration in minutes 
1..30> ] 
  
local – local loopback 
remote – remote loopback 
local tone-inject – backward tone 
injection  
remote tone-inject – forward tone 
injection  
Stopping the 
loopback  
no loopback 
 
Megaplex-1 
5. Ports 
Configuration Errors  
The table below lists messages generated by Megaplex-1 when a configuration error on voice ports is 
detected. 
Message 
Description 
FXS pair: if one of the ports is 
configured to high ring voltage, the 
second one has to be at shutdown. 
For each pair of FXS ports (1-2, 3-4, 5-6 or 7-8) the following 
must be configured: if one of the ports is set to 'high', the 
other one must be set to shutdown. 
Warning: Voice port: coding law and 
DS1 frame type mismatch 
Configured coding law does not match the frame type. 
Voice port: tx gain value is out of range 
The input level can be set in the range of +5 dBm to -17 dBm, 
depending on the interface type (see Transmit and Receive 
Levels for Various Interfaces table) 
Voice port: rx sensitivity value is out of 
range 
The input level can be set in the range of +9 dBm to -17 dBm, 
depending on the interface type (see Transmit and Receive 
Levels for Various Interfaces table) 
Voice port: tx/rx gain level must be set 
in 0.5 db steps 
Tx/Rx gain level must be set in 0.5 db steps. 
Voice port: Fail to get data from DB 
Database problem. Try to reconfigure the voice port. 
Voice port: Illegal E&M type 
combination 
E&M type must be the same for all voice ports. 
 
 
 
 