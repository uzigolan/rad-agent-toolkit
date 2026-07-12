# 13 Versatile I/O Modules

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 929–1088.*


## 13.1 Overview  *(p.929)*

13.1 Overview  
This chapter describes the main features, applications and installation procedures for the versatile I/O 
modules operating in the Megaplex-4 chassis with CLI management: 
• 
VS-12 – 12-port serial module  
• 
VS-6/BIN – 6-port serial module with 8 binary in/out command ports  
• 
VS-6/C37 – 6-port serial module with 2 fiber optic C37.94 ports  
• 
VS-6/703 – 6-port serial module with 8 DS0-G703 ports  
• 
VS-6/E&M – 6-port serial modules with 4 E&M voice ports  
• 
VS-6/FXO – 6-port serial modules with 8 FXO voice ports  
• 
VS-6/FXS – 6-port serial modules with 8 FXS voice ports  
• 
FXS/E&M – Voice module with 4 E&M ports and 8 FXS ports 
• 
VS-OCU/E&M – Voice module with 2 OCU-DP – DDS ports and 4 E&M ports  
• 
VS-8/E&M – Voice module with 8 E&M ports  
• 
VS-16E1T1-EoP –16-port E1/T1 module with EoP support 
• 
VS-16E1T1-PW –16-port E1/T1 module with PW support 
• 
VS-6/E1T16 – 6-port serial module with 8 E1/T1 ports and PW support.   
Up to 10 modules can be installed in a single Megaplex-4100 chassis, and up to 4 modules in a single 
Megaplex-4104 chassis. 
Note 
In the Megaplex-4100 systems equipped with VS or T3 modules there might be 
a limitation for 9 such modules in the chassis. The remaining slot can be used 
for any other I/O module. For the conditions of this limitation, refer to Chapter 
1.  

## 13.2 VS (VS-12, VS-6/BIN, VS-6/703 and VS-6/C37)  *(p.930)*

13. Versatile I/O Modules 
13.2 VS (VS-12, VS-6/BIN, VS-6/703 and VS-6/C37)  
This section describes the technical characteristics, applications, installation and operation of the following 
modules: 
• 
VS-12 versatile data module and VS-6/BIN versatile data/binary command modules for use in the 
Megaplex-4 Next Generation Multiservice Access Node, ver 4.5 and higher  
• 
VS-6/C37 versatile fiber-optic modules for use in the Megaplex-4 ver 4.6 and higher 
• 
VS-6/703 serial module with DS0-G703 ports for use in the Megaplex-4 ver 4.9 and higher.  
For VS voice modules and VS-OCU/E&M module, see a separate section. 
Product Options 
Serial/Binary Command/C37/G703 Options 
Versatile modules are available in the following versions:  
• 
VS-12 consists of two identical submodules each featuring a serial interface with 6 sync/async 
channels. 
• 
VS-6/BIN module consists of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels  
 
Lower: binary command submodule with 8 inbound (cmd-in) and 8 outbound (cmd-out) ports. 
• 
VS-6/C37 consists of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels  
 
Lower: C37.94 submodule with 2 IEEE C37.94 fiber optic ports. 
• 
VS-6/703 consists of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels  
 
Lower: G.703 submodule with 8 64-kbps co-directional G.703 ports.  
Note 
In this chapter, the generic term VS is used when the information is applicable 
to the serial port section of all the VS models. The complete module 
designation (VS-12, VS-6/C37, VS-6/703 or VS-6/BIN) is used when 
information is applicable only to a specific model.  
13. Versatile I/O Modules 
Binary Command Relays 
Two relay types are available and can be selected in accordance with applications of VS-6/BIN as ordering 
options: Electro-mechanical relay (EMR) and Solid-state relay (SSR). 
G.703 
8 64-kbps G.703 codirectional data channels (ports) are available for connecting various devices with G.703 
interface to E1/T1, SDH/SONET and GbE networks. 
Applications  
Serial Data Applications  
The following figure shows an application where a single VS module enables users at several remote 
substations to connect to data equipment over a variety of serial interfaces such as RS-232, V.35, RS-449 or 
X.21, with configurable data rates from 2.4 to 1984 kbps. 
Sub-Stations
STM
-
GbE
ETH
RTU
MSAP Node
9.6 kbps 
FO
RS-232
V.35
RS-449
X.21
PBX
V.35/RS-449
Low Speed
Data
RTU
RS-232
Megaplex-4
PSN
SDH Access
Network
ADM
Megaplex-4
Megaplex-4
VS-12
VS-12
 
Substation Data Services Connectivity  
13. Versatile I/O Modules 
Binary Command Applications 
The following figure shows a typical alarm and control application for the VS-6/VIN module. In this 
application, the inbound ports of the VS-6/VIN module installed in Megaplex-4 are connected to the alarm 
relays of additional equipment units, and to sensors that monitor the state of critical resources; for 
example, the cooling fan of the communication rack, the mains power, etc. 
Warning
Buzzer
Cooling Fan
Activation
Backup
Power
Main Power
Loss Monitor
Control Fan
Alarm
External Equipment
Alarm Relay
Remote Site
Inbound
Inbound
Outbound
Outbound
Uplink 
Module
CL
CL
VS-6/
BIN
Warning
Buzzer
Cooling Fan
Activation
Backup
Power
Main Power
Loss Monitor
Control Fan
Alarm
External Equipment
Alarm Relay
Central Site
NMS
Megaplex-4
Megaplex-4
VS-6/
BIN
Uplink 
Module
 
Typical VS-6/VIN Application – Alarm and Control  
C.37 Applications 
The IEEE C37.94 standard defines a programmable multimode optical fiber interface between 
Teleprotection and digital multiplexer equipment, for distances of up to 2 km. The module can provide 
either tributary or uplink ports for teleprotection equipment. 
The VS-6/C37 module allows aggregating several C37.94 links from Megaplex-4 or 3rd party into a single 
C37.94 uplink and transmitting them to the communication Mux.   
In addition to the TDM capabilities, VS-6/C37 can perform direct encapsulation of Teleprotection 
commands into a PWE session over PSN. The direct encapsulation provides an effective way to keep the 
overall delay within the applications boundaries.  
 
13. Versatile I/O Modules 
SDH/SONET
PSN
Megaplex-4
Substation
Communication House
RTU
Distance TP
IEEE C37.94
IEEE C37.94
IEEE C37.94
RTU
RTU
Megaplex-4
 Typical 
VS-6/C37 Application  
G.703 Applications 
The figure below shows a typical VS-6/703 application. 
STM-1
G.703
E1
G.703
VS-6/703
SDH
ADM
Megaplex-4
Subrate 
Multiplexer
Subrate 
Multiplexer
ADM
Megaplex-4
VS-6/703
 
Typical VS-6/703 Application  
Features  
Serial Interfaces 
The VS modules feature 6/12 serial sync/async data ports (channels). Data rates are independently 
selectable for each channel and depend on the selected encapsulation mode. The interface terminates in 
68-pin SCSI-4 female connectors. Each submodule contains 2 connectors; each connector includes 3 
channels. The selection among V.35, RS-422 and RS-232 interfaces is done by CLI configuration. Adapter 
cables, available upon order, are offered by RAD to split each module connector into three separate 
channel interfaces with standard connectors: V.35, RS-422, RS-232, X.21 or V.36.  
13. Versatile I/O Modules 
Encapsulation Modes  
VS modules behave like different types of modules on selection of the specific encapsulation mode: 
• 
None: each channel operates at high speed rates of n×56 or n×64 kbps, where n = 1 to 31 (that is, 
maximum 1984 kbps). 
• 
v110: each channel operates at low speed rates of 2.4, 4.8, 9.6, 19.2 or 38.4 kbps. 
• 
3-bit transitional: the module provides transitional encoding to transmit asynchronous data at 
rates up to 19.2/38.4 kbps. It operates by encoding asynchronous data in a 3-bit transitional code, 
which is then transmitted over the Megaplex uplink using full DS0 timeslots.  
• 
r111: the module provides transitional encoding to transmit asynchronous data. It operates by 
encoding data in a 3-bit transitional code, which is then transmitted over the Megaplex uplink at a 
rate of 64 kbps. 
• 
hcm: the module transmits synchronous/asynchronous data over 64 kbps based on multiplexing 
with a DS0 timeslot.  Specifically, a DS0 is further multiplexed into a 10 byte structure with bytes in 
the 10 bytes frame labeled F0 through F9.   
Main characteristics of these modes are shown in the table below. 
VS Encapsulation Modes  
Encapsulation-
mode 
Rate 
Mode 
End-to-end-
control 
Data-bits/ 
stop-bits 
Available in VS 
modules 
3bit-
transitional 
{1 | 2 } x 64kbps 
N/A 
yes/no 
rts 
N/A 
Any VS module with 
serial ports 
v110 
{2.4 | 4.8 | 9.6 | 19.2 | 38.4 } 
sync/async 
yes/no 
rts 
data-bits 
stop-bits 
Any VS module with 
serial ports 
hcm 
{2.4 | 4.8 | 9.6 | 19.2 | 38.4 } 
sync/async 
yes/no 
rts 
data-bits 
stop-bits 
Any VS module with 
serial ports apart from 
E1/T1, G703 and 
PW-enhanced voice 
modules  
r111 
{2.4 | 4.8 | 9.6 | 19.2} 
N/A 
N/A 
N/A 
Any VS module with 
serial ports apart from 
E1/T1, G703 and 
PW-enhanced voice 
modules 
13. Versatile I/O Modules 
Encapsulation-
mode 
Rate 
Mode 
End-to-end-
control 
Data-bits/ 
stop-bits 
Available in VS 
modules 
none  
{1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
| 10 | 11 | 12 | 13 | 14 | 15 | 
16 | 17 | 18 | 19 | 20 | 21 | 22 
| 23 | 24 | 25 | 26 | 27 | 28 | 
29 | 30 | 31} x {56kbps | 
64kbps} 
N/A 
n x 64 kbps*: 
yes/no, 
rts/inverse-rts 
n x 56 kbps:  
yes/no 
rts 
N/A 
Any VS module with 
serial ports 
  * End-to-end control is not available for VS module with E1/T1 ports. 
Encapsulation mode (as well as sync/async mode) can be set independently per each channel.  
Interface Control Signals  
Each channel has local support for the CTS, RTS, DCD, DSR and DTR lines:  
• 
The CTS line can be independently configured to be always ON, or to track the RTS line. 
• 
The DCD line is constantly ON, except when communications are not possible because of the 
following cases: 
 
loss of frame synchronization 
 
loss of synchronization on E1/T1 uplink port 
• 
The DSR line (encapsulation-mode = v110 only) is always ON (unless end-to-end transmission is 
enabled).  
• 
The DCD line is also affected by remote RTS, when end-to-end control is selected. 
The interface control signals for end-to-end transfer depend on the selected encapsulation mode (see 
Configuring Serial Port parameters in Chapter 5).  
VS-12 Module   
The VS-12 module architecture and data flow is shown in the figure below. The following table lists the 
serial submodule entities (ports) and their hierarchy.  
Note 
Out of 24 PW ports of a VS module only 12 can be configured as working PW 
ports. Other 12 ports are reserved for protection PW ports.  
 
13. Versatile I/O Modules 
DS0
CL.2 DS0
Cross connect
GbE
CL.2 Ethernet 
Engine
tdm-bridge
1..4
Serial
1..12
16xE1/T1
4xE1/T1
12xE1/T1
12xE1/T1
12xE1/T1
PW 
1..24
DS1
1..12
Switch
 
VS-12 Module Architecture  
VS Module Architecture Entities and their Hierarchy  
Name 
Number of Ports  
Possible Values 
 
VS-12 
VS-6/BIN 
VS-12 
VS-6/BIN 
serial 
12 
6 
slot/1… slot/12 
slot/1… slot/6 
tdm-bridge 
4 
6 
slot/1… slot/4 
slot/1… slot/6  
ds1 
12 
12  
slot/1… slot/12 
slot/1… slot/12  
pw 
24 
24 
slot/1… slot/24 
slot/1… slot/24  
VS-6/BIN Module 
The VS-6/BIN module includes 8 outbound switches and 8 inbound sensors for Megaplex-4 alarm control.  
The binary commands can be locally output or be carried to a peer card/Megaplex over a TDM/SDH 
network or over a packet switched network. Up to 4 in/out commands can be carried over a single DS0.  
The module operates in conjunction with other Megaplex modules catering for a variety of interfaces, such 
as voice, high speed, low speed and others, to provide any possible service needed in a substation. 
The VS-6/BIN module architecture and data flow is shown in in the figure below. The following table lists 
the binary submodule entities (ports) and their hierarchy.  
13. Versatile I/O Modules 
CL.2 DS0
Cross connect
CL.2 Ethernet 
Engine
Switch
GbE
Bind
cmd-channel 
1
cmd-channel 
2
cmd-in/out 
2.1..2.4
cmd-in/out 
1.1..1.4
serial
1..6
tdm-bridge
1..6
13xE1/T1
6xE1/T1
DS0
ds1
1..12
PW 
1..24
12xE1/T1
12xE1/T1
 
VS-6/BIN Module Architecture  
The module provides the following functions:  
• 
8 binary input ports (cmd-in) – enable the management system to read inbound indications from 
external sources. 
• 
8 binary output ports (cmd-out) – provide outbound indications and control signals by means of 
dry relay contacts controlled by the management system. 
• 
Two cmd-channels (1,2) are used to transport binary information over the telecommunications 
network via end-to-end reporting: the input command is transferred to the remote location via a 
selected timeslot and affect the corresponding output. 
CMD-IN and CMD-OUT ports are automatically assigned to CMD CHANNELS (1,2) in accordance with the 
figure above. 
Binary Module Architecture Entities and their Hierarchy  
Name 
Number of 
Ports  
Possible Values 
Remarks 
cmd-in 
8 
slot /1/1 …… slot /1/4 
for cmd-channel 1  
 
 
slot /2/1 …… slot /2/4 
for cmd channel 2  
cmd-out 
8 
slot /1/1 …… slot /1/4 
for cmd-channel 1  
 
 
slot /2/1 …… slot /2/4 
for cmd channel 2  
13. Versatile I/O Modules 
Name 
Number of 
Ports  
Possible Values 
Remarks 
cmd-channel 
2 
slot /1, slot /2 
 
Binary Inbound (CMD-IN) Ports  
The VS-6/BIN module has 8 inbound ports, which enable it to report alarms external to the Megaplex-4 I/O 
Modules unit, and physical conditions in remote locations to a central management station. The inbound 
ports of the VS-6/BIN module can be connected to relay contacts, environmental sensors, etc.  
The VS-6/BIN module is configured by the user to “interpret” the state of each input and report events to 
the CL module of the local Megaplex-4 I/O Modules. For each event, the CL module will send the 
corresponding alarm message, respectively SNMP trap, to the supervision terminal and network 
management stations. Each event can be associated with a user-selected message that describes the 
situation, or prompts the remote user to take a prescribed action. For the list of available alarms, refer to 
Chapter 11. 
The user can monitor the state of each inbound port by means of indicators located on the VS-6/BIN front 
panel. 
Binary Outbound (CMD-OUT) Ports 
The VS-6/BIN module has 8 outbound ports equipped with change-over dry relay contacts. The default 
state (that is, the state of the relay contacts when the Megaplex-4 I/O Modules is operating) can be 
selected by the user, individually for each outbound port. 
The relay contacts can be used to report alarms to outside indicators (such as lights, buzzers and bells 
located on a bay alarm or remote monitoring panel), and to control external devices or applications (such 
as fans, dialers and backup power sources). Each relay can be controlled by a specific event in the network, 
in accordance with the configuration defined by means of the bind-alarm-to-relay and bind-alarm-source-
to-relay commands. 
The user can monitor the state of each outbound port by means of indicators located on the VS-6/BIN front 
panel. 
VS-6/703 Module  
High-Speed Data Transport  
The VS-6/703 module provides Megaplex-4 with 8 64-kbps G.703 codirectional data channels (ports). Each 
channel can be independently enabled or disabled by software configuration. 
13. Versatile I/O Modules 
64 kbps Codirectional Interface 
The 64 kbps codirectional interface is defined by ITU-T Rec. G.703, Section 1.1.4.1 and has the following 
functions: 
• 
Bidirectional transfer of data signals 
• 
Transfer of 64 kHz bit clock signals associated with the data signals 
• 
Transfer of 8 kHz byte clock signals associated with the data signals. 
ITU-T Rec. G.703, Section 1 describes three different versions for 64 kbps interfaces, which differ mainly in 
the type and direction of the clock signals, and the number of wires used.  
The term codirectional describes an interface that transmits the information and the associated timing 
signals in the same direction. The interface uses four wires (two twisted pairs), one pair for the transmit 
direction and the other pair for the receive direction). Each pair carries both the data and the associated 
clock signals. 
The following figure illustrates the flow of signals across the interface. 
RECEIVER
TRANSMITTER
TRANSMITTER
RECEIVER
Transmit Data and
Associated Timing
Receive Data and
Associated Timing
 
G.703 Codirectional Interface  
The 64 kbps co-directional interface transfers data at a nominal rate of 64 kbps, and a maximum rate 
tolerance of 100 ppm. The interface uses two balanced twisted pairs having a nominal impedance of 120Ω. 
The transmit pulse shape, measured across a 120Ω resistive load impedance, is nominally rectangular. A 
mark is represented by a peak voltage of 1.0V, and a space is represented by a voltage of 0 ±0.10V. The 
nominal pulse width is 3.9 μsec. The maximum line attenuation that should be compensated for by the 
receiver is 3 dB at up to 128_kHz. 
The interface supports the delineation of byte intervals. The signal waveform uses coding to carry both 
clock and timing information, and to obtain a signal with essentially zero DC component. The coding is 
performed in the following steps, illustrated in the figure below: 
• 
Step 1: The basic 64 kbps bit period is divided into four unit intervals. 
• 
Step 2: A binary “one” is encoded as a block of the following four symbols: 1100. A binary “zero” is 
encoded as a block of the following four symbols: 1010. 
13. Versatile I/O Modules 
• 
Step 3: The binary signal is converted into a three-level signal by alternating the polarity of 
consecutive blocks (to ensure DC balance). 
• 
Step 4: To mark the start and end of a byte, the alternation in polarity of the blocks is violated 
every eighth block. The violation block marks the last bit in a byte. 
 
 
G.703 Codirectional Signal Coding  
 
Architecture and Data Flow  
The VS-6/703 module architecture and data flow is shown below. G.703-specific entities include 8 ds0-g703 
ports per module. 
Bit Number  
64 kbps Data
8
0
1
0
2
1
3
0
4
0
5
1
6
1
7
1
8
0
1
1
Violation
Byte Timing
Step 1 + 2    Binary Data
Step 3   
Three-Level
Encoded Data
Step 4   
Three-Level
Signal 
with Polarity
Violations
7
1
Violation
One Byte
13. Versatile I/O Modules 
CL.2 DS0
Cross connect
CL.2 Ethernet 
Engine
Switch
GbE
Bind
DS0-G703
1..8
serial
1..6
tdm-bridge
1..4
23xE1/T1
4xE1/T1
DS0
ds1
1..12
PW 
1..24
12xE1/T1
12xE1/T1
 
VS-6/C37 Module  
The VS-6/C37 module features a dual-port fiber optic interface, operating at a nominal wavelength of 
830 nm and nominal line rate of 2.048 Mbps. Each port is terminated in a pair of ST connectors for 
connection to standard multimode fiber. 
Fiber Optic Interface  
The fiber optic interface has a wide dynamic range, which ensures that the receiver will not saturate even 
when using short fiber optic cables (saturation is caused when the optical power applied to the receiver 
exceeds its maximum allowed input power, and results in very high bit error rates). 
The interface can be used for both user and network ports – either for inter-substation communication or 
for transmitting distance Teleprotection information. 
C37.94 Frame Format  
The C37.94 frame structure is schematically shown below. 
 
TS0 
TS1 
TS 2-7 
TS 8 -31 
G704 Sync Header 
Overhead data 
Channel data 
13. Versatile I/O Modules 
C37.94 Frame Format 
Frame 
Element 
Description 
Bits 
Header 
The 16-bit header is a unique bit pattern to allow 
the receiver to synchronize to the 256-bit frame. 
a  b  c  d  e  f  g  h  0 0 0 0 1 1 1 1 
Overhead 
data 
This 48-bit section includes bits for providing 
information between the multiplexer and 
teleprotection equipment. Each data bit is followed 
by its complement (for 24 actual bits of 
information). 
p,q,r,s – One or zero data that 
depend upon the value of N used, 
where N = 1 to 12 (p = most-
signiﬁcant-bit) 
 
0,0,0,1  for N = 1 
0,0,1,0  for N = 2 
1,1,0,0, for N = 12 
Channel 
data 
This 192-bit section comprises 96 data bits, with 
each data bit followed by its complement.  
The ﬁrst N times 8 data bits carry the N times 64 
kilobit per second (kbit/s) data. 
The remaining 96 – (N times 8) data bits are set to 
1. 
 
Architecture and Data Flow  
The VS-6/C37 module architecture and data flow is shown below. C37-specific entities include two ds1-
optical ports per module. 
13. Versatile I/O Modules 
CL.2 DS0
Cross connect
CL.2 Ethernet 
Engine
Switch
GbE
Bind
C37.94
1..2
serial
1..6
tdm-bridge
1..6
26xE1/T1
6xE1/T1
DS0
ds1
1..12
PW 
1..24
12xE1/T1
12xE1/T1
 
VS-6/C37 Module Architecture 
Pseudowire Services  
VS I/O modules provide TDM pseudowire access gateway services over packet-switched networks 
(Ethernet and IP) for TDM traffic (E1, T1, high-speed and low-speed data, voice) received via the Megaplex-
4 TDM buses from other modules. This is done via independently-configurable internal DS1 ports available 
in the module. The number of DS1 ports is 12 for any VS module. 
In addition, the module provides direct PW access to its serial ports. The number of PW ports is 24 per any 
VS module. Out of these 24 ports 12 are used as working ports and other 12 as protection ports.  
VS modules provide pseudowire emulation services over packet-switched networks using the CESoPSN 
(structure-aware TDM circuit emulation over PSN) protocols in accordance with RFC5086. 
The pseudowire services enable converting TDM payload to packets and transferring these packets through 
router interfaces defined in the Megaplex-4.   
Packet structure is independently selectable for each pseudowire, for compatibility with the PSN type 
(UDP/IP or ETH). For maximum flexibility in system applications, the framing format of the pseudowire 
device at the destination (referred to as a pseudowire peer) can also be taken into account. Thus, in many 
cases traffic using the E1 standards can be directed at destinations using the T1 standards, and vice versa. 
The pseudowire exit port toward the PSN is also selectable, either via VS serial port, or via any other bridge 
port (GbE or VCG) of any module installed in the chassis. The selectable exit ports are bound (via SVI ports) 
to router interfaces, where each router interface has its own IP source address and, optionally, its own 
13. Versatile I/O Modules 
VLAN. Each VS submodule supports up to 12 interfaces, CL.2 modules support unlimited number of 
interfaces. However, the maximum number of router interfaces per Megaplex-4 is 100. The user can also 
specify static routes to control the IP routing.  
The PW engine in one of the VS modules can be used as a server for traffic from other modules cross-
connected via its DS1 ports.  
• 
VS-6/703 modules have independent adaptive clock recovery (ACR) mechanisms for each 
pseudowire, which recover the original timing (clock rate) of the far-end source of each 
pseudowire, according to ITU G.8261, G.823, G.824 and MEF 22 recommendations. The clock 
recovery mechanisms can provide recovered clock signals to serve as timing references for the 
Megaplex-4.  
Cross-Connections 
The VS modules feature DS0 and PW-TDM cross-connections, which can be used according to the module 
application as shown in the table below. For description of DSO and PW-TDM cross-connect functionalities, 
see respective sections in Chapter 8. 
Cross-Connect Type 
Diagram 
DS0 cross-connect between the 
serial/cmd-channel/ds1-opt port 
of the module and timeslots on 
the E1/T1/DS1/DS1-opt ports of 
the uplink module. 
1  
serial/
cmd-channel/
ds1-opt
cross connect 
dso
e1/t1/ds1
ds1-opt
serial/
cmd-channel/
ds1-opt
 
 
PW-TDM cross-connect: 
serial/ds1-opt port of the VS 
module is cross-connected 
directly to PW. This type allows 
low-latency transmission of TDM 
services over packet-switched 
networks and used when a single 
channel is carried over dedicated 
PW. 
2 
pw
1/1
flow
ETH
peer
cross connect 
pw-tdm
1:1
serial
RI
PW 
Static 
Router
13. Versatile I/O Modules 
Cross-Connect Type 
Diagram 
Serial/ds1-opt ports are cross-
connected to DS1 ports inside the 
module (DS0 cross-connect); DS1 
ports are cross-connected to PW 
(PW-TDM cross-connect). This 
type is used when multiple I/O 
channels are sharing the same 
PW.  
3 
PW 
Static 
Router
serial/
cmd-in/
ds1-opt
pw
1/1
cross connect 
dso
flow
RI
ETH
peer
ds1
1/1
1:1
cross connect 
pw-tdm
serial/
cmd-in/
ds1-opt
 
Any Megaplex-4 service port is 
cross-connected to the DS1 port 
inside the module (DS0 cross-
connect); DS1 ports are 
cross-connected to PW (PW-TDM 
cross-connect). In this application 
the VS module is used as a server 
for other modules not equipped 
with PW.  
4 
PW 
Static 
Router
Any port
pw
1/1
cross connect 
dso
flow
RI
ETH
peer
ds1
1/1
1:1
cross connect 
pw-tdm
Any port
Any Megaplex-4  
module
VS module
 
DS0 Cross-Connect  
The DS0 cross-connect matrix of the Megaplex-4 chassis enables flexible payload routing in the VS 
modules, independently configurable for each port, at the individual timeslots (DS0) level. This routing is 
configured via ds0 cross-connect command as follows: 
• 
Binary command submodule: between the cmd-channel and timeslots on the E1/T1/DS1/DS1-opt 
ports of the uplink module. This cross-connect is always performed in the bidirectional mode. 
• 
C37 submodule: between the ds1-opt port and timeslots on the E1/T1/DS1/DS1-opt ports of the 
uplink module. This cross-connect is always performed in the bidirectional mode. 
• 
Serial submodule: between the serial ports and timeslots on the E1/T1/DS1/DS1-opt ports of the 
uplink module.  
• 
G.703 submodule: between the DS0-G703 ports and timeslots on the E1/T1/DS1/DS1-opt ports of 
the uplink module.  
In addition to the normal full-duplex (bidirectional) mode, VS serial ports feature additional 
transmission modes, which enable point-to-multipoint communication: 
 
Unidirectional (simplex) transmission, where each channel can be configured either to receive 
(unidirectional RX) or transmit (unidirectional TX). 
 
Bidirectional broadcast (half-duplex) communication, suitable for polled applications. In this 
mode, a channel can not only receive, but can also  transmit (not both simultaneously).  
13. Versatile I/O Modules 
 
This feature is available for VS modules configured to 3-bit-transitional (and operating at 64 
kbps) or R.111 mode.  
 
For configuration considerations, see Error! Reference source not found. below. 
VS modules operating in V.110 and R.111 modes also support split timeslot allocation.  
PW-TDM Cross-Connect  
PW-TDM cross-connections are used to transport TDM services over PSN networks. The table above shows 
diagrams of PW-TDM cross-connect configurations depending on the module application (see Diagram 2 
and Diagram 3). 
In Diagram 2, serial/ds1-opt port is cross-connected directly to PW. This type allows low-latency 
transmission of TDM services over packet-switched networks and used when a single channel is carried 
over dedicated PW.  
In Diagram 3, serial/ds1-opt ports are cross-connected to DS1 ports inside the module (DS0 cross-connect); 
DS1 ports are cross-connected to PW (PW-TDM cross-connect). This type is used when multiple I/O 
channels are sharing the same PW. 
Diagram 4 shows a VS module operating as a PW server for other modules not equipped with PW. 
E1/T1/DS1/serial ports of these modules are cross-connected to DS1 ports inside the VS module (DS0 
cross-connect); DS1 ports are cross-connected to PW (PW-TDM cross-connect).  
Pseudowire QoS/CoS 
To enable optimal handling of pseudowire traffic within the PSN, the following parameters can be 
configured: 
• 
For Ethernet transport networks: outgoing pseudowire packets are assigned to a dedicated VLAN 
ID according to 802.1Q and marked for priority using 802.1p bits. 
• 
For IP transport networks: outgoing pseudowire packets are marked for priority using DSCP or ToS 
bits. This allows TDMoIP packets to be given the highest priority in IP networks.  
The proper balance between the PSN throughput and delay is achieved via configurable packet size. A jitter 
buffer with selectable size compensates for packet delay variation (jitter) of up to 8 msec in the network.  
Fault Propagation  
VS modules perform fault propagation for pseudowires. If a problem is detected on a pseudowire, the 
attached physical port receives a fault indication and vice versa.  
13. Versatile I/O Modules 
Management 
• 
The VS module operating parameters are determined by commands received from the Megaplex-4 
CL module. The CL module can also download new software to the module, when the Megaplex-4 
software is updated.  
Setup, control, and diagnostics are performed in the following ways: 
• 
Via a supervisory port on the Megaplex-4 CL module using an ASCII terminal 
• 
Via management station connected to a dedicated 10/100BaseT Ethernet port on the Megaplex-4 
CL module  
• 
Using inband management with dedicated VLAN for managing remote units. 
Timing  
The VS module has an internal timing generator that receives the nodal timing and clock signals from the 
Megaplex-4 chassis and generates the internal timing and clock signals needed for module operation.  
The serial port synchronous channel timing mode is DCE: the serial port provides the clock signals to the 
DTE connected to it. This mode is suitable for connecting equipment with DTE interface to the VS ports.  
• 
VS-6/703 modules have independent adaptive clock recovery (ACR) mechanisms for each 
pseudowire, which recover the original timing (clock rate) of the far-end source of each 
pseudowire, according to ITU G.8261, G.823, G.824 and MEF 22 recommendations. The clock 
recovery mechanisms can provide recovered clock signals to serve as timing references for the 
Megaplex-4. 
Protection  
The VS module features the following types of protection: 
• 
TDM group protection between E1/T1/DS1/DS1-opt ports of the VS module and DS1/E1/T1/E1-
i/T1-i ports of other Megaplex-4 modules (see TDM Group Protection in Chapter 7) 
• 
TDM group protection between cmd-channel ports (see TDM Group Protection in Chapter) 
• 
Direct PW protection between two PW ports of the VS module (see PW Protection in Chapter ). 
• 
DS0 SNCP for end-to-end protection of n x ds0 services (ds0 bundles) over any TDM network 
infrastructure by selecting individual timeslots of E1/T1/E1-i/T1-i/DS1/DS0-G703 ports of the 
relevant uplink modules (see DS0 SNCP Protection in Chapter 7).  
13. Versatile I/O Modules 
TDM Group Protection on DS1 Ports 
When pseudowires are configured on redundant internal DS1 ports, the pseudowire traffic is automatically 
protected as well. The protection mode is 1+1, meaning that the traffic is also sent on the protection DS1 
port.  
The figure below illustrates the DS1 TDM group protection. For each protection group, you must first 
configure the internal DS1 port that will serve as the working port; this configuration is copied to the other 
port of the group. In addition, it is necessary to configure pseudowires from each internal DS1 port in the 
protection group to the desired destinations.  
 
GbE
CL-A/1
GbE
CL-B/1
I/O 
Serial Port
DS1 #1
Working
PW #1
PW #2
SVI #1
SVI #2
DS1 #2
Protection 
TDM Group
 
TDM Group Protection for DS1 Ports 
PW Protection  
For PW protection, two PW ports on the same module are connected to the same DS1 port. A typical 
configuration is shown in the figure below.  
GbE
CL-A/1
GbE
CL-B/1
I/O 
Serial Port
DS1
PW #1
Working 
PW #2
Protection
SVI #1
SVI #2
 
PW Protection 
13. Versatile I/O Modules 
During normal operation, both PW ports process as usual the transmit and receive signals, but the receive 
output of the protection port is disconnected. The operational state of the protection port is continuously 
monitored to ensure that it is operating properly. If the working link fails, the corresponding port is 
disconnected, and the protection port takes over.  
For two ports configured to PW protection, the following parameters must be the same for both ports: 
• 
psn type (udp-over-ip or ethernet)    
• 
tdm-oos  
• 
tdm-payload. 
DS0 SNCP Protection  
For DS0 SNCP protection, each tributary service is cross-connected to one or more timeslots on the 
selected E1/T1/E1-i/T1-i/DS1/DS0-G703 link. In parallel, the same timeslots are grouped as ds0-bundles. 
Per each ds0-bundle the user is asked to configure a timeslot and a signaling bit inside TS 16 for E2E path 
monitoring – for details, see Chapters 6 and 7). A typical configuration is shown in the figure below.  
Tributary
Port
E1/T1#1
E1/T1#2
ds0-
bundle#1
ds0-
bundle#2
DS0
CC
 
TDM SNCP Protection 
The data from the tributary port is transmitted to both uplink ports (parallel Tx mode. Based on the path 
status, it selects the active Rx path of the data. 
13. Versatile I/O Modules 
Physical Description  
The VS module occupies one I/O slot in the Megaplex-4 chassis. The module is based on a main board and 
two factory-replaceable submodules.  
 
For the VS-12 module, the submodules are identical and include a serial interface with 6 sync/async 
channels. 
VS-6/BIN consists of the following submodules: 
• 
Upper: serial interface submodule with 6 sync/async channels  
• 
Lower: binary command submodule with 8 CMD-IN/CMD-OUT binary command ports. 
VS-6/C37 consists of the following submodules:  
• 
Upper: serial interface submodule with 6 sync/async channels  
• 
Lower: C37.94 submodule with 2 IEEE C37.94 fiber optic ports. 
VS-6/703 consists of the following submodules:  
• 
Upper: serial interface submodule with 6 sync/async channels  
• 
Lower: G.703 submodule with 8 G.703 ports. 
The figures below show different VS module panels.  
Interface 
Module 1
Interface 
Module 2
Main Board
13. Versatile I/O Modules 
 
VS-12 
 
13. Versatile I/O Modules 
 
VS-6/BIN 
 
13. Versatile I/O Modules 
  
VS-6/C37 
 
13. Versatile I/O Modules 
 
VS-6/703 
The module panel includes two submodule panels.  
The upper submodule panel includes two 68-pin SCSI-4 female connectors, each containing three channels. 
The lower submodule panel depends on the module version: 
• 
For VS-12, it is identical with the upper panel. 
• 
For VS-6/BIN it includes the 44-pin female D-type connector for connection to the inbound (cmd-
in) and outbound (cmd-out) ports and 8 bi-color status indicators – one for each 
inbound/outbound port. 
13. Versatile I/O Modules 
• 
For VS-6/C37 it includes 6 C37.94 ports. 
• 
For VS-6/703 it includes 8 G.703 64-kbps codirectional ports. 
LED Indicators 
The serial section does not contain any LED indicators.  
Binary Command Indicators 
The table below explains the functions of the CMD-IN/OUT indicators located on the Binary module panel. 
VS-6/BIN Indicators  
Indicator 
Number 
Color 
Description 
CMD IN/OUT  
8  
Green/Red 
Green blinking: cmd-in port is active  
Red blinking: cmd-out port is active 
Green/Red blinking: cmd-in and cmd-out ports are 
both active 
Off: port is not active or not connected 
C37.94 Interface Indicators 
The table below explains the functions of indicators located on the C37 submodule panel. 
VS-6/C37 Indicators  
Indicator 
Color 
Description 
SYNC  
Green/ 
Red 
Lights steadily in green – the corresponding port is operating properly 
Flashes in green – the corresponding port is operating properly, but serves as 
the standby port when link protection is enabled 
Lights in red – the corresponding port detects loss of synchronization or loss 
of signal 
Flashes in red – the corresponding port serves as the standby port, and 
detects loss of synchronization 
REM SYNC 
Yellow 
On – the corresponding port detects loss of remote synchronization 
Off – the corresponding port is not connected. 
13. Versatile I/O Modules 
G.703 Interface Indicators 
The table below explains the functions of indicators located on the G.703 submodule panel. 
G.703 Indicators  
Indicator 
Color 
Description 
ALM 
Red 
Lights steadily – the corresponding port detects LOS  
Flashes –the corresponding port detects OOS pattern. 
Off – the corresponding port is not connected. 
Technical Specifications  
Serial Interface 
Number of Channels and Transmission 
Format 
6 data channels per submodule, sync/async, 
user-selectable  
 
Connectors 
68-pin SCSI female connector per each 3 data 
channels (2 connectors per submodule / 
4 connectors per VS-12 module) 
 
Electrical Interface  
 
• V.35 
• V.11/RS-422 
• V.24/RS-232 
Physical Interface (via adapter cables) 
• V.35  
• V.36/RS-449, RS-530, or X.21  
• RS-232  
 
Encapsulation Modes 
None 
V110 
R.111 
3-bit-transitional 
HCM   
 
Channel Data Rates 
 
 
 encapsulation-mode=none 
n×56 or n×64 kbps rates, independently 
selectable per channel: n = 1 to 31  
 
encapsulation-mode=v110 
2.4, 4.8, 9.6, 19.2, 38.4 kbps 
 
encapsulation-mode=r111 
2.4, 4.8, 9.6, 19.2 kbps 
 
encapsulation-mode=3-bit-transitional)  64 kbps, 128 kbps 
 
encapsulation-mode=hcm 
64 kbps 
13. Versatile I/O Modules 
 
Timing Mode  
DCE (VS channel provides both RX and TX clocks 
to the user DTE)  
 
Asynchronous Character Format 
 
 
Data bits  
5, 6, 7, or 8  
 
Parity  
Yes/No (Enable/disable transparent end-to-end 
transfer of parity bit) 
 
Stop bits 
1 or 2  
 
Interface Control Signals 
• Local support 
• End-to-end transfer  
 
Local support 
• Local DCD is ON when the uplink is 
synchronized and there is no LOF alarm on 
the channel 
• Local CTS tracks local RTS state, or is 
constantly ON (user-selectable) 
• DSR (encapsulation-mode = v110) always ON 
when module is powered (unless end-to-end 
transmission is enabled) 
 
End-to-end transfer (user-selectable)  
•  
 
encapsulation-mode = none  
• Local RTS line to remote DCD line (only for 
rates n x 56 kbps)  
 
encapsulation-mode = v110, hcm 
• Local RTS line to remote DCD line 
• Local DTR line to remote DSR line 
 
encapsulation-mode = 3bit-transitional • Local RTS line to remote DCD line  
Binary Command 
Interface 
Compliance 
IEEE 1613 (USA standard for equipment in 
electrical switching stations)  
IEC 61850-3 (equivalent European 
requirements) 
 
Connector 
DB-44 
 
Number of Ports 
Inbound: 8 
Outbound: 8 
 
Inbound Ports 
 
 
Maximum Input Control voltage  
 
±60 VDC  
 
Command trip point  
 
Above: 24 VDC ON 
Below: 18 VDC OFF 
 
Outbound Ports 
 
13. Versatile I/O Modules 
 
Relay type 
Electro-mechanical relay (EMR) 
Solid-state relay (SSR) 
 
Closed Contact Parameters 
Max current: 
• Electro-mechanical relay: 1A  
• Solid-state relay:          0.12A 
 
 
Impedance: < 0.1 Ohm 
 
 
 
 Minimum current (SSR only): 0.1 mA 
 
Maximum DC Voltage across Open 
Contacts 
60 VDC  
 
 
Isolation 
All input and outputs are galvanically isolated  
 
Indicators 
See VS-6/BIN Indicators table  
C37.94 Interface 
Compliance  
IEEE C37.94, optical part 
 
Number of ports 
2 
 
Connectors   
Pair of ST connectors, female 
 
Nominal Data Rate 
2.048 Mbps 
 
Wavelength 
830nm ± 40nm 
 
Fiber Type 
 
62.5/125 µm multimode 
50/125 µm multimode 
 
Transmitter Type 
LED 
 
Power Coupled into Fiber 
 
62.5/125 µm: -11 to -19 dBm 
50/125 µm: -11 to -23 dBm  
 
Mininum Receiver Sensitivity 
-32 dBm 
 
Maximum Receiver Input Power 
-11 dBm 
 
Receiver Dynamic Range 
21 dB 
 
Range (Typical) 
2 km/1.25 miles 
 
Indicators 
See G.703 Codirectional Interface table 
G.703 Interface 
Compliance  
 
ITU-T Rec. G.703, Section 1.1.4.1 
 
Number of ports 
8 
 
Connectors   
RJ-45 (one for 2 channels with a splitter cable)  
 
Nominal Data Rate 
64 kbps 
13. Versatile I/O Modules 
 
Indicators 
See G.703 Indicators table  
OCU-DP Interface 
Compliance  
 
AT&T PUB 62310 (Standard DDS), BELLCORE 
TA-TSY-000077 
 
Number of Data Channels 
2 
 
Connectors   
RJ-45 (per channel)  
 
Data Rates 
56 or 64 kbps, full-duplex 
 
Line Rates 
56 kbps: 56 kbps 
64 kbps: 72 kbps 
 
Mapping to Megaplex Timeslots  
56 kbps: single DS0 
64 kbps: two DS0 
 
 
Line Code 
AMI 
 
LED Indicators (per channel) 
LOS (red): Lights steadily when a loss of signal 
condition is detected by the channel 
TEST (yellow): Lights steadily when a local or 
remote loopback is activated 
 
Diagnostics (per channel) 
 
Local loopback  
Remote loopback (OCU loopback) 
Remote loopback on external unit (CSU 
loopback) 
 
Alarms (per channel) 
Loss of signal   
 
Out of service (OOS) 
Supported end-to-end   
 
“Idle state” 
56 kbps only 
 
Timing 
 
Locked to the Megaplex nodal timing 
Pseudowire 
Number of Pseudowires 
Up to 640 pseudowires per Megaplex-4 
Up to 2 active pseudowires per DS1 port 
Up to 24 pseudowires (12 working + 
12 protection) per VS module 
 
Pseudowire Protocol 
CESoPSN in accordance with RFC5086 
 
Packet Switched Network Types 
• UDP over IP 
• MEF-8 Ethernet 
13. Versatile I/O Modules 
 
Jitter Buffer Size 
Regular modules: 250 µsec to 8000 µsec, in 1-
µsec steps. 
/PW modules:  250 µsec to 256000 µsec, in 1-
µsec steps. 
Note: The value for VS modules entered by the 
user is rounded upward to the closest n*125 
µsec value.  
Power Consumption 
VS-12 
RS-422: 16.7W  
RS-232: 13.5W 
V.35: 15.9W 
 
VS-6/BIN 
RS-422: 14.7W  
RS-232: 13.0W 
V.35: 14.2W 
 
VS-6/C37 
RS-422: 12.9W  
RS-232: 11.3W 
V.35: 12.5W 
 
VS-6/703 
 
RS-422: 16.0W  
RS-232: 14.4W 
V.35: 15.6W 
 
VS-OCU/E&M 
11.5W  
 
Note: Power Consumption of VS modules was measured under the following conditions: 
• 
all serial ports configured to the same interface  
• 
at the maximum speed of 1984 kbps. 
Configuration 
 
Programmable via Megaplex-4 management 
system  
Environment 
Operating Temperature 
-10°C to 55°C (14°F to 131°F)   
 
Storage Temperature 
-20°C to 70°C  (-4°F to 160°F)   
 
Humidity 
Up to 95%, non-condensing  
13. Versatile I/O Modules 
Preparing the Modules for Installation 
 
Warning 
Before performing any internal settings, adjustment, maintenance, or 
repairs, first disconnect all the cables from the module, and then remove the 
module from the Megaplex-4 enclosure. 
No internal settings, adjustment, maintenance, and repairs may be 
performed by either the operator or the user; such activities may be 
performed only by a skilled technician who is aware of the hazards involved. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. 
 
Caution 
The modules contain components sensitive to electrostatic discharge (ESD). 
To prevent ESD damage, always hold the module by its sides, and do not 
touch the module components or connectors.  
 
Caution 
To prevent physical damage to the electronic components assembled on the 
two sides of the module printed circuit boards (PCB) while it is inserted into 
its chassis slot, support the module while sliding it into position and make 
sure that its components do not touch the chassis structure, nor other 
modules.  
Installing a Module in the Chassis 
VS modules may be installed in an operating chassis (hot insertion). 
 
Warning 
The module starts operating as soon as it is inserted in an operating chassis.  
 
 To install a VS module: 
3. Refer to the system installation plan and identify the prescribed module slot. 
4. Check that the fastening screws at the module sides are free to move. 
5. Insert the module in its chassis slot and slide it in as far as possible. 
13. Versatile I/O Modules 
6. Secure the module by tightening its two fastening screws. 
The module starts operating as soon as it is plugged into an operating enclosure. At this stage, 
ignore the alarm indications. 
Connecting to Remote Equipment 
Connecting Serial Equipment 
The user equipment is connected to serial data ports of VS modules via 68-pin SCSI female connectors 
designated CH 1-3, CH 4-6, CH 7-9, CH 10-12.  
SCSI Connector Pinout 
The table below lists the pin assignment of the CH connectors. Note that the pins in actual use depend on the 
module version. 
CH Connector, Pin Assignment 
Channel 
Pi
n 
Designation 
Function 
Pi
n 
Designation  
Function 
– 
1 
F.G. 
Frame Ground 
35 
S.G. 
Signal Ground 
1, 
4,  
7, 
10 
2 
RD(A) 
Receive Data A 
36 
RD(B) 
Receive Data B 
3 
TC(A) 
Transmit Clock A 
37 
TC(B) 
Transmit Clock B 
4 
RC(A) 
Receive Clock A 
38 
RC(B) 
Receive Clock B 
5 
ERC(A) 
External Receive Clock A 
39 
ERC(B) 
External Receive Clock B 
6 
ETC(A) 
External Transmit Clock A 
40 
ETC(B) 
External Transmit Clock B 
7 
TD(A) 
Transmit Data A 
41 
TD(B) 
Transmit Data B 
8 
CO(A) 
Control Out A 
42 
CO(B) 
Control Out B 
9 
DSR(A) 
Data Set Ready A 
43 
DSR(B) 
Data Set Ready B 
1
0 
DCD(A) 
Data Carrier Detect A 
44 
DCD(B) 
Data Carrier Detect B 
1
1 
CI(A) 
Control In A 
45 
CI(B) 
Control In B 
1
2 
F.G 
Frame Ground 
46 
S.G 
Signal Ground 
13. Versatile I/O Modules 
Channel 
Pi
n 
Designation 
Function 
Pi
n 
Designation  
Function 
2, 
5,  
8,  
11 
1
3 
RD(A) 
Receive Data A 
47 
RD(B) 
Receive Data B 
1
4 
TC(A) 
Transmit Clock A 
48 
TC(B) 
Transmit Clock B 
1
5 
RC(A) 
Receive Clock A 
49 
RC(B) 
Receive Clock B 
1
6 
ERC(A) 
External Receive Clock A 
50 
ERC(B) 
External Receive Clock B 
1
7 
ETC(A) 
External Transmit Clock A 
51 
ETC(B) 
External Transmit Clock B 
1
8 
TD(A) 
Transmit Data A 
52 
TD(B) 
Transmit Data B 
1
9 
CO(A) 
Control Out A 
53 
CO(B) 
Control Out B 
2
0 
DSR(A) 
Data Set Ready A 
54 
DSR(B) 
Data Set Ready B 
2
1 
DCD(A) 
Data Carrier Detect A 
55 
DCD(B) 
Data Carrier Detect B 
2
2 
CI(A) 
Control In A 
56 
CI(B) 
Control In B 
2
3 
F.G 
Frame Ground 
57 
S.G 
Signal Ground 
 3,  
6,  
9,  
12 
2
4 
RD(A) 
Receive Data A 
58 
RD(B) 
Receive Data B 
2
5 
TC(A) 
Transmit Clock A 
59 
TC(B) 
Transmit Clock B 
2
6 
RC(A) 
Receive Clock A 
60 
RC(B) 
Receive Clock B 
2
7 
ERC(A) 
External Receive Clock A 
61 
ERC(B) 
External Receive Clock B 
2
8 
ETC(A) 
External Transmit Clock A 
62 
ETC(B) 
External Transmit Clock B 
13. Versatile I/O Modules 
Channel 
Pi
n 
Designation 
Function 
Pi
n 
Designation  
Function 
2
9 
TD(A) 
Transmit Data A 
63 
TD(B) 
Transmit Data B 
3
0 
CO(A) 
Control Out A 
64 
CO(B) 
Control Out B 
3
1 
DSR(A) 
Data Set Ready A 
65 
DSR(B) 
Data Set Ready B 
3
2 
DCD(A) 
Data Carrier Detect A 
66 
DCD(B) 
Data Carrier Detect B 
3
3 
CI(A) 
Control In A 
67 
CI(B) 
Control In B 
3
4 
F.G 
Frame Ground 
68 
S.G 
Signal Ground 
 
RAD offers adapter cables for directly connecting user equipment with standard connectors to the 
appropriate 68-pin SCSI connector located on the  
VS module. The table below provides information on the adapter cables available from RAD.  
Adapter Cables Offered by RAD  
Selection 
Adapter Cable 
User’s Side Connectors  
V.35 
CBL-SCS68/3/V35/M 
34-pin VAPL male connector  
RS-422 
CBL-SCS68/3/530/M 
25-pin D-type male connector  
CBL-SCS68/3/X21/M 
15-pin D-type male connector 
CBL-SCS68/3/V36/M 
37-pin D-type male connector  
CBL-SCS68/3/V36/F 
37-pin D-type female connector  
RS-232 
CBL-SCS68/3/232/M 
25-pin D-type male connector  
 To connect the cables: 
Identify the cables intended for connection to each module connector, and connect them into the 
appropriate connectors.  
13. Versatile I/O Modules 
When using any of the adapter cables, plug each channel connector at the other end of the cable into the 
prescribed user equipment connector in accordance with the site installation plan. 
Note 
Using the above adapter cables is possible only when all the module channels 
are configured with the same interface. If your application includes channels 
with different interfaces, use an open free-end cable manufactured according 
to the SCSI connector pinout.  
Adapter Cables  
The user side of each cable is terminated in three connectors, designated CH-1, CH-2, CH-3. The tables in 
the following sections list the pinout of each connector on the VS-12 and user sides and indicate the 
number of VS-12 channel corresponding to each pin.   
CBL-SCS68/3/V35/M Cable 
The following figure shows a general view of the CBL-SCS68/3/V35/M cable, and the table below lists the 
cable wiring. 
CH-1
CH-2
CH-3
 
CBL-SCS68/3/V35/M Cable 
CBL-SCS68/3/V35/M, Cable Wiring 
Ch 
SCSI 
Connector  
Function 
34-Pin 
Connector 
SCSI 
Connector 
Function 
34-Pin 
Connector 
 
1 
F.G. 
Not Used 
 
35 
S.G. 
Not Used 
 
1, 
4,  
7, 
10 
2 
RD(A) 
Receive Data A 
R 
36 
RD(B) 
Receive Data B 
T 
3 
TC(A) 
Transmit Clock A 
Y 
37 
TC(B) 
Transmit Clock B 
AA 
4 
RC(A) 
Receive Clock A 
V 
38 
RC(B) 
Receive Clock B 
X 
5 
ERC(A) 
External Receive Clock 
A 
BB 
39 
ERC(B) 
External Receive Clock 
B 
Z 
13. Versatile I/O Modules 
Ch 
SCSI 
Connector  
Function 
34-Pin 
Connector 
SCSI 
Connector 
Function 
34-Pin 
Connector 
6 
ETC(A) 
External Transmit 
Clock A 
U 
40 
ETC(B) 
External Transmit Clock 
B 
W 
7 
TD(A) 
Transmit Data A 
P 
41 
TD(B) 
Transmit Data B 
S 
8 
CO 
Control Out 
D 
42 
– 
Not Used 
 
9 
DSR 
Data Set Ready 
E 
43 
– 
Not Used 
 
10 
DCD 
Data Carrier Detect  
F 
44 
– 
Not Used 
 
11 
CI 
Control In 
C 
45 
– 
Not Used 
 
12 
F.G 
Frame Ground 
A 
46 
S.G 
Signal Ground 
B 
2, 
5,  
8,  
11 
13 
RD(A) 
Receive Data A 
R 
47 
RD(B) 
Receive Data B 
T 
14 
TC(A) 
Transmit Clock A 
Y 
48 
TC(B) 
Transmit Clock B 
AA 
15 
RC(A) 
Receive Clock A 
V 
49 
RC(B) 
Receive Clock B 
X 
16 
ERC(A) 
External Receive Clock 
A 
BB 
50 
ERC(B) 
External Receive Clock 
B 
Z 
17 
ETC(A) 
External Transmit 
Clock A 
U 
51 
ETC(B) 
External Transmit Clock 
B 
W 
18 
TD(A) 
Transmit Data A 
P 
52 
TD(B) 
Transmit Data B 
S 
19 
CO 
Control Out 
D 
53 
– 
Not Used 
 
20 
DSR 
Data Set Ready 
E 
54 
– 
Not Used 
 
21 
DCD 
Data Carrier Detect 
F 
55 
– 
Not Used 
 
22 
CI 
Control In 
C 
56 
– 
Not Used 
 
23 
F.G 
Frame Ground 
A 
57 
S.G 
Signal Ground 
B 
3,  
6,  
9,  
12 
24 
RD(A) 
Receive Data A 
R 
58 
RD(B) 
Receive Data B 
T 
25 
TC(A) 
Transmit Clock A 
Y 
59 
TC(B) 
Transmit Clock B 
AA 
26 
RC(A) 
Receive Clock A 
V 
60 
RC(B) 
Receive Clock B 
X 
27 
ERC(A) 
External Receive Clock 
A 
BB 
61 
ERC(B) 
External Receive Clock 
B 
Z 
28 
ETC(A) 
External Transmit 
Clock A 
U 
62 
ETC(B) 
External Transmit Clock 
B 
W 
29 
TD(A) 
Transmit Data A 
P 
63 
TD(B) 
Transmit Data B 
S 
13. Versatile I/O Modules 
Ch 
SCSI 
Connector  
Function 
34-Pin 
Connector 
SCSI 
Connector 
Function 
34-Pin 
Connector 
30 
CO 
Control Out 
D 
64 
– 
Not Used 
 
31 
DSR 
Data Set Ready 
E 
65 
– 
Not Used 
 
32 
DCD 
Data Carrier Detect 
F 
66 
– 
Not Used 
 
33 
CI 
Control In 
C 
67 
– 
Not Used 
 
34 
F.G 
Frame Ground 
A 
68 
S.G 
Signal Ground 
B 
CBL-SCS68/3/530/M Cable 
The following figure shows a general view of the CBL-SCS68/3/530/M cable, and the table below lists the 
cable wiring. 
CH-1
CH-2
CH-3
 
CBL-SCS68/3/530/M Cable 
CBL-SCS68/3/530/M Cable Wiring 
Ch 
SCSI 
Connector  
Function 
25-Pin 
Connec-
tor 
SCSI 
Connector 
Function 
25-Pin 
Connec-
tor 
 
1 
F.G. 
Not Used 
 
35 
S.G. 
Not Used 
 
1, 
4,  
7, 
10 
2 
RD(A) 
Receive Data A 
3 
36 
RD(B) 
Receive Data B 
16 
3 
TC(A) 
Transmit Clock A 
15 
37 
TC(B) 
Transmit Clock B 
12 
4 
RC(A) 
Receive Clock A 
17 
38 
RC(B) 
Receive Clock B 
9 
5 
ERC(A) 
External Receive Clock 
A 
20 
39 
ERC(B) 
External Receive Clock 
B 
23 
6 
ETC(A) 
External Transmit Clock 
A 
24 
40 
ETC(B) 
External Transmit 
Clock B 
11 
7 
TD(A) 
Transmit Data A 
2 
41 
TD(B) 
Transmit Data B 
14 
13. Versatile I/O Modules 
Ch 
SCSI 
Connector  
Function 
25-Pin 
Connec-
tor 
SCSI 
Connector 
Function 
25-Pin 
Connec-
tor 
 
8 
CO(A) 
Control Out A 
5 
42 
CO(B) 
Control Out B 
13 
9 
DSR(A) 
Data Set Ready A 
6 
43 
DSR(B) 
Data Set Ready B 
22 
10 
DCD(A
) 
Data Carrier Detect A 
8 
44 
DCD(B) 
Data Carrier Detect B 
10 
11 
CI(A) 
Control In A 
4 
45 
CI(B) 
Control In B 
19 
12 
F.G 
Frame Ground 
1 
46 
S.G 
Signal Ground 
7 
2, 
5,  
8,  
11 
13 
RD(A) 
Receive Data A 
3 
47 
RD(B) 
Receive Data B 
16 
14 
TC(A) 
Transmit Clock A 
15 
48 
TC(B) 
Transmit Clock B 
12 
15 
RC(A) 
Receive Clock A 
17 
49 
RC(B) 
Receive Clock B 
9 
16 
ERC(A) 
External Receive Clock 
A 
20 
50 
ERC(B) 
External Receive Clock 
B 
23 
17 
ETC(A) 
External Transmit Clock 
A 
24 
51 
ETC(B) 
External Transmit 
Clock B 
11 
18 
TD(A) 
Transmit Data A 
2 
52 
TD(B) 
Transmit Data B 
14 
19 
CO(A) 
Control Out A 
5 
53 
CO(B) 
Control Out B 
13 
20 
DSR(A) 
Data Set Ready A 
6 
54 
DSR(B) 
Data Set Ready B 
22 
21 
DCD(A
) 
Data Carrier Detect A 
8 
55 
DCD(B) 
Data Carrier Detect B 
10 
22 
CI(A) 
Control In A 
4 
56 
CI(B) 
Control In B 
19 
23 
F.G 
Frame Ground 
1 
57 
S.G 
Signal Ground 
7 
3,  
6,  
9,  
12 
24 
RD(A) 
Receive Data A 
3 
58 
RD(B) 
Receive Data B 
16 
25 
TC(A) 
Transmit Clock A 
15 
59 
TC(B) 
Transmit Clock B 
12 
26 
RC(A) 
Receive Clock A 
17 
60 
RC(B) 
Receive Clock B 
9 
27 
ERC(A) 
External Receive Clock 
A 
20 
61 
ERC(B) 
External Receive Clock 
B 
23 
28 
ETC(A) 
External Transmit Clock 
A 
24 
62 
ETC(B) 
External Transmit 
Clock B 
11 
29 
TD(A) 
Transmit Data A 
2 
63 
TD(B) 
Transmit Data B 
14 
30 
CO(A) 
Control Out A 
5 
64 
CO(B) 
Control Out B 
13 
13. Versatile I/O Modules 
Ch 
SCSI 
Connector  
Function 
25-Pin 
Connec-
tor 
SCSI 
Connector 
Function 
25-Pin 
Connec-
tor 
31 
DSR(A) 
Data Set Ready A 
6 
65 
DSR(B) 
Data Set Ready B 
22 
32 
DCD(A
) 
Data Carrier Detect A 
8 
66 
DCD(B) 
Data Carrier Detect B 
10 
33 
CI(A) 
Control In A 
4 
67 
CI(B) 
Control In B 
19 
34 
F.G 
Frame Ground 
1 
68 
S.G 
Signal Ground 
7 
CBL-SCS68/3/X21/M Cable 
The figure below shows a general view of the CBL-SCS68/3/X21/M cable, and the following table lists the 
cable wiring. 
CH-1
CH-2
CH-3
 
CBL-SCS68/3/X21/M Cable 
CBL-SCS68/3/X21/M Cable Wiring 
Ch 
SCSI 
Connector  
Function 
15-Pin 
Connecto
r 
SCSI 
Connector 
Function 
15-Pin 
Connecto
r 
 
1 
F.G. 
Not Used 
 
35 
S.G. 
Not Used 
 
1, 
4,  
7, 
10 
2 
RD(A) 
Receive Data A 
4 
36 
RD(B) 
Receive Data B 
11 
3 
TC(A) 
Transmit Clock A 
6 
37 
TC(B) 
Transmit Clock B 
13 
4 
– 
Not Used 
 
38 
– 
Not Used 
 
5 
ETC(A) 
External Transmit Clock 
A 
7 
39 
ETC(B) 
External Transmit 
Clock B 
14 
6 
ETC(A) 
External Transmit Clock 
A 
7 
40 
ETC(B) 
External Transmit 
Clock B 
14 
13. Versatile I/O Modules 
Ch 
SCSI 
Connector  
Function 
15-Pin 
Connecto
r 
SCSI 
Connector 
Function 
15-Pin 
Connecto
r 
7 
TD(A) 
Transmit Data A 
2 
41 
TD(B) 
Transmit Data B 
9 
8 
– 
Not Used 
 
42 
– 
Not Used 
 
9 
– 
Not Used 
 
43 
– 
Not Used 
 
10 
DCD(A
) 
Data Carrier Detect A 
5 
44 
DCD(B) 
Data Carrier Detect B 
12 
11 
CI(A) 
Control In A 
3 
45 
CI(B) 
Control In B 
10 
12 
F.G 
Frame Ground 
1 
46 
S.G 
Signal Ground 
8 
 2, 
5,  
8,  
11 
13 
RD(A) 
Receive Data A 
4 
47 
RD(B) 
Receive Data B 
11 
14 
TC(A) 
Transmit Clock A 
6 
48 
TC(B) 
Transmit Clock B 
13 
15 
– 
Not Used 
 
49 
– 
Not Used 
 
16 
ETC(A) 
External Transmit Clock 
A 
7 
50 
ETC(B) 
External Transmit 
Clock B 
14 
17 
ETC(A) 
External Transmit Clock 
A 
7 
51 
ETC(B) 
External Transmit 
Clock B 
14 
18 
TD(A) 
Transmit Data A 
2 
52 
TD(B) 
Transmit Data B 
9 
19 
– 
Not Used 
 
53 
– 
Not Used 
 
20 
– 
Not Used 
 
54 
– 
Not Used 
 
21 
DCD(A
) 
Data Carrier Detect A 
5 
55 
DCD(B) 
Data Carrier Detect B 
12 
22 
CI(A) 
Control In A 
3 
56 
CI(B) 
Control In B 
10 
23 
F.G 
Frame Ground 
1 
57 
S.G 
Signal Ground 
8 
3,  
6,  
9,  
12 
24 
RD(A) 
Receive Data A 
4 
58 
RD(B) 
Receive Data B 
11 
25 
TC(A) 
Transmit Clock A 
6 
59 
TC(B) 
Transmit Clock B 
13 
26 
– 
Not Used 
 
60 
– 
Not Used 
 
27 
ETC(A) 
External Transmit Clock 
A 
7 
61 
ETC(B) 
External Transmit 
Clock B 
14 
28 
ETC(A) 
External Transmit Clock 
A 
7 
62 
ETC(B) 
External Transmit 
Clock B 
14 
29 
TD(A) 
Transmit Data A 
2 
63 
TD(B) 
Transmit Data B 
9 
13. Versatile I/O Modules 
Ch 
SCSI 
Connector  
Function 
15-Pin 
Connecto
r 
SCSI 
Connector 
Function 
15-Pin 
Connecto
r 
30 
– 
Not Used 
 
64 
– 
Not Used 
 
31 
– 
Not Used 
 
65 
– 
Not Used 
 
32 
DCD(A
) 
Data Carrier Detect A 
5 
66 
DCD(B) 
Data Carrier Detect B 
12 
33 
CI(A) 
Control In A 
3 
67 
CI(B) 
Control In B 
10 
34 
F.G 
Frame Ground 
1 
68 
S.G 
Signal Ground 
8 
CBL-SCS68/3/V36/M and CBL-SCS68/3/V36/F Cables  
The following figure shows general views of the CBL-SCS68/3/V36/M and CBL-SCS68/3/V36/F cables, and 
the table below lists the cable wiring. 
CH-1
CH-2
CH-3
 
CBL-SCS68/3/V36/M, CBL-SCS68/3/V36/F Cables 
CBL-SCS68/3/V36/M, CBL-SCS68/3/V36/F Cable Wiring 
Ch 
SCSI 
Connector  
Function 
37-Pin 
Connec-
tor 
SCSI 
Connector 
Function 
37-Pin 
Connec-
tor 
 
1 
F.G. 
Not Used 
 
35 
S.G. 
Not Used 
 
1, 
4,  
7, 
10 
2 
RD(A) 
Receive Data A 
6 
36 
RD(B) 
Receive Data B 
24 
3 
TC(A) 
Transmit Clock A 
5 
37 
TC(B) 
Transmit Clock B 
23 
4 
RC(A) 
Receive Clock A 
8 
38 
RC(B) 
Receive Clock B 
26 
5 
ERC(A) 
External Receive Clock 
A 
12 
39 
ERC(B) 
External Receive Clock 
B 
30 
6 
ETC(A) 
External Transmit Clock 
A 
17 
40 
ETC(B) 
External Transmit 
Clock B 
35 
13. Versatile I/O Modules 
Ch 
SCSI 
Connector  
Function 
37-Pin 
Connec-
tor 
SCSI 
Connector 
Function 
37-Pin 
Connec-
tor 
7 
TD(A) 
Transmit Data A 
4 
41 
TD(B) 
Transmit Data B 
22 
8 
CO(A) 
Control Out A 
9 
42 
CO(B) 
Control Out B 
27 
9 
DSR(A) 
Data Set Ready A 
11 
43 
DSR(B) 
Data Set Ready B 
29 
10 
DCD(A
) 
Data Carrier Detect A 
13 
44 
DCD(B) 
Data Carrier Detect B 
31 
11 
CI(A) 
Control In A 
7 
45 
CI(B) 
Control In B 
25 
12 
F.G 
Frame Ground 
1 
46 
S.G 
Signal Ground 
19, 20, 
37 
 2, 
5,  
8,  
11 
13 
RD(A) 
Receive Data A 
6 
47 
RD(B) 
Receive Data B 
24 
14 
TC(A) 
Transmit Clock A 
5 
48 
TC(B) 
Transmit Clock B 
23 
15 
RC(A) 
Receive Clock A 
8 
49 
RC(B) 
Receive Clock B 
26 
16 
ERC(A) 
External Receive Clock 
A 
12 
50 
ERC(B) 
External Receive Clock 
B 
30 
17 
ETC(A) 
External Transmit Clock 
A 
17 
51 
ETC(B) 
External Transmit 
Clock B 
35 
18 
TD(A) 
Transmit Data A 
4 
52 
TD(B) 
Transmit Data B 
22 
19 
CO(A) 
Control Out A 
9 
53 
CO(B) 
Control Out B 
27 
20 
DSR(A) 
Data Set Ready A 
11 
54 
DSR(B) 
Data Set Ready B 
29 
21 
DCD(A
) 
Data Carrier Detect A 
13 
55 
DCD(B) 
Data Carrier Detect B 
31 
22 
CI(A) 
Control In A 
7 
56 
CI(B) 
Control In B 
25 
23 
F.G 
Frame Ground 
1 
57 
S.G 
Signal Ground 
19, 20, 
37 
3,  
6,  
9,  
12 
24 
RD(A) 
Receive Data A 
6 
58 
RD(B) 
Receive Data B 
24 
25 
TC(A) 
Transmit Clock A 
5 
59 
TC(B) 
Transmit Clock B 
23 
26 
RC(A) 
Receive Clock A 
8 
60 
RC(B) 
Receive Clock B 
26 
27 
ERC(A) 
External Receive Clock 
A 
12 
61 
ERC(B) 
External Receive Clock 
B 
30 
28 
ETC(A) 
External Transmit Clock 
A 
17 
62 
ETC(B) 
External Transmit 
Clock B 
35 
13. Versatile I/O Modules 
Ch 
SCSI 
Connector  
Function 
37-Pin 
Connec-
tor 
SCSI 
Connector 
Function 
37-Pin 
Connec-
tor 
29 
TD(A) 
Transmit Data A 
4 
63 
TD(B) 
Transmit Data B 
22 
30 
CO(A) 
Control Out A 
9 
64 
CO(B) 
Control Out B 
27 
31 
DSR(A) 
Data Set Ready A 
11 
65 
DSR(B) 
Data Set Ready B 
29 
32 
DCD(A
) 
Data Carrier Detect A 
13 
66 
DCD(B) 
Data Carrier Detect B 
31 
33 
CI(A) 
Control In A 
7 
67 
CI(B) 
Control In B 
25 
34 
F.G 
Frame Ground 
1 
68 
S.G 
Signal Ground 
19, 20, 
37 
CBL-SCS68/3/232/M Cable  
The following figure shows a general view of the CBL-SCS68/3/232/M cable, and  
the table below lists the cable wiring. 
CH-1
CH-2
CH-3
 
CBL-SCS68/3/232/M Cable 
CBL-SCS68/3/232/M Cable Wiring 
Ch 
SCSI 
Connector  
Function 
25-Pin 
Connector 
SCSI 
Connector 
Function 
25-Pin 
Connector 
 
1 
F.G. 
Frame Ground 
1 
35 
S.G. 
Signal Ground 
7 
1, 
4,  
7, 
10 
2 
RD(A) 
Receive Data A 
3 
36 
– 
Not Used 
 
3 
TC(A) 
Transmit Clock A 
15 
37 
– 
Not Used 
 
4 
RC(A) 
Receive Clock A 
17 
38 
– 
Not Used 
 
5 
ERC(A) 
External Receive Clock  
20 
39 
– 
Not Used 
 
6 
ETC(A) 
External Transmit Clock  
24 
40 
– 
Not Used 
 
13. Versatile I/O Modules 
7 
TD(A) 
Transmit Data  
2 
41 
– 
Not Used 
 
8 
CO(A) 
Control Out  
5 
42 
– 
Not Used 
 
9 
DSR(A) 
Data Set Ready  
6 
43 
– 
Not Used 
 
10 
DCD(A
) 
Data Carrier Detect  
8 
44 
– 
Not Used 
 
11 
CI(A) 
Control In A 
4 
45 
– 
Not Used 
 
12 
F.G 
Frame Ground 
1 
46 
S.G 
Signal Ground 
7 
2, 
5,  
8,  
11 
13 
RD(A) 
Receive Data  
3 
47 
– 
Not Used 
 
14 
TC(A) 
Transmit Clock  
15 
48 
– 
Not Used 
 
15 
RC(A) 
Receive Clock  
17 
49 
– 
Not Used 
 
16 
ERC(A) 
External Receive Clock  
20 
50 
– 
Not Used 
 
17 
ETC(A) 
External Transmit Clock  
24 
51 
– 
Not Used 
 
18 
TD(A) 
Transmit Data  
2 
52 
– 
Not Used 
 
19 
CO(A) 
Control Out  
5 
53 
– 
Not Used 
 
20 
DSR(A) 
Data Set Ready  
6 
54 
– 
Not Used 
 
21 
DCD(A
) 
Data Carrier Detect  
8 
55 
– 
Not Used 
 
22 
CI(A) 
Control In  
4 
56 
– 
Not Used 
 
23 
F.G 
Frame Ground 
1 
57 
S.G 
Signal Ground 
7 
3,  
6,  
9,  
12 
24 
RD(A) 
Receive Data  
3 
58 
– 
Not Used 
 
25 
TC(A) 
Transmit Clock  
15 
59 
– 
Not Used 
 
26 
RC(A) 
Receive Clock  
17 
60 
– 
Not Used 
 
27 
ERC(A) 
External Receive Clock  
20 
61 
– 
Not Used 
 
28 
ETC(A) 
External Transmit Clock  
24 
62 
– 
Not Used 
 
29 
TD(A) 
Transmit Data  
2 
63 
– 
Not Used 
 
30 
CO(A) 
Control Out  
5 
64 
– 
Not Used 
 
31 
DSR(A) 
Data Set Ready  
6 
65 
– 
Not Used 
 
32 
DCD(A
) 
Data Carrier Detect  
8 
66 
– 
Not Used 
 
33 
CI(A) 
Control In  
4 
67 
– 
Not Used 
 
13. Versatile I/O Modules 
34 
F.G 
Frame Ground 
1 
68 
S.G 
Signal Ground 
7 
Connecting Binary Command Ports 
Before starting, identify the cables intended for connection to each port of this module, in accordance with 
the site installation plan.  
The module has a DB-44 female connector for connection to the CMD-IN/OUT ports and their status 
indicators. The tale below lists the functions of the pins in the connector. 
CMD 1-8 IN/OUT Connector, Pin Assignment  
DB-44 Pin 
Open End Color 
Function 
1 
} 
Twisted Pair 
White 
IN1 
2 
Blue 
IN1 
21 
} 
Twisted Pair 
White 
OUT1 
22 
Orange 
OUT1 
3 
} 
Twisted Pair 
White 
IN2 
4 
Green 
IN2 
23 
} 
Twisted Pair 
White 
OUT2 
24 
Brown 
OUT2 
14 
} 
Twisted Pair 
White 
IN3 
15 
Gray 
IN3 
25 
} 
Twisted Pair 
White 
OUT3 
26 
White/Blue 
OUT3 
16 
} 
Twisted Pair 
White 
IN4 
17 
Orange/Blue 
IN4 
27 
Twisted Pair 
White 
OUT4 
13. Versatile I/O Modules 
DB-44 Pin 
Open End Color 
Function 
28 
} 
Green/Blue 
OUT4 
18 
} 
Twisted Pair 
White 
IN5 
19 
Brown/Blue 
IN5 
7 
} 
Twisted Pair 
White 
OUT5 
8 
Gray/Blue 
OUT5 
31 
} 
Twisted Pair 
White 
IN6 
32 
White/Orange 
IN6 
9 
} 
Twisted Pair 
White 
OUT6 
10 
Orange/Green 
OUT6 
33 
} 
Twisted Pair 
White 
IN7 
34 
Orange/Brown 
IN7 
37 
} 
Twisted Pair 
White 
OUT7 
38 
Gray/Orange 
OUT7 
30 
} 
Twisted Pair 
White 
IN8 
44 
White/Green 
IN8 
39 
} 
Twisted Pair 
White 
OUT8 
40 
Green/Brown 
OUT8 
RAD offers the CBL-VS-BIN adapter cable for directly connecting user equipment to the 44-pin DB 
connector located on the VS-6/BIN module.  
The figure below shows a general view of the CBL-SCS68/3/V35/M cable, and  
the table below lists the cable wiring. 
13. Versatile I/O Modules 
44-pin Connector
 
CBL-VS-BIN Cable 
Connecting the C37 Ports 
Before starting, refer to the installation plan to determine the fiber-optic cables intended for connection to 
the VS-6/C37 module. 
Before connecting, clean the optical connectors using an approved solvent, and dry thoroughly using 
optical tissue. Avoid sharp bends and twisting of the fiber optic cables. 
 To connect the remote equipment: 
Connect the prescribed cables to the following connectors on the module panel: 
• 
Connect the transmit cable to the TX connector 
• 
Connect the receive cable to the RX connector.  
Connecting the G.703 Ports  
Before starting, identify the cables intended for connection to each port of this module, in accordance with 
the site installation plan.  
The user equipment is connected to G.703 ports via four RJ-45 connectors on the VS-6/703 module front 
panel. The connectors are designated CH 1,5; CH 2,6; CH 3, 7; CH 4,8.  
RAD offers the CBL-E1-SPLT adapter cable for directly connecting user equipment to these RJ-45 connectors 
located on the VS-6/703 module. The cable is 1 m long. 
The figure below shows a general view of the CBL-E1-SPLT cable. 
 
13. Versatile I/O Modules 
 
CBL-E1-SPLT Cable  
The table below lists the wiring for the cable splitting the upper main RJ-45 connector (CH 1,5) to two 
ports: CH 1 and CH 5. For CH 2,6 (CH 3,7; CH 4,8) module panel connectors use the same table with “1” in 
the Function column replaced by “2” (“3”, “4”) and “5” by “6” (“7”, “8”).   
CBL-E1-SPLT, Cable Wiring for Channels 1,5 
Main RJ-45 
Connector 
Function 
CH-1,2,3,4 Connector 
CH-5,6,7,8 Connector 
1 
RRING1 – IN 
4 
 
2 
RTIP1 – IN  
5 
 
3 
TRING5 – OUT 
 
1 
4 
TRING1 – OUT 
1 
 
5 
TTIP1 – OUT 
2 
 
6 
TTIP5 – OUT 
 
2 
7 
RRING5 – IN 
 
4 
8 
RTIP5 – IN 
 
5 
Normal Indications  
Once the equipment connected to the VS-6/BIN ports is operational, the CMD-IN and CMD-OUT indicators 
display the state of the corresponding port.  
Alarm outputs on a card are not bound to any alarm by default and users may decide which alarm or pair of 
alarm and source will activate them. 
Configuration Considerations  
Selecting the Data Rate  
Depending on selected encapsulation mode, different data rates are supported (see VS Encapsulation 
Modes table above).  
13. Versatile I/O Modules 
When using a user-manufactured open cable, the electrical interface selection can be done per port 
(channel) independently. However, when using RAD adaptor cables, the following rules must be followed: 
• 
All 3 channels sharing the same connector must be configured with the same interface type. 
• 
The adaptor cable connected to the interface must match the interface selected in CLI in 
accordance with the following table. 
RAD offers adapter cables for directly connecting user equipment with standard connectors to the 
appropriate 68-pin SCSI connector located on the  
VS module. The following table provides information on the adapter cables available from RAD.  
Matching Adapter Cables to Interface Selection  
Interface Selection in CLI 
Adapter Cable 
User’s Side Connectors  
v35 
CBL-SCS68/3/V35/M 
34-pin VAPL male connector  
rs-422 
CBL-SCS68/3/530/M 
25-pin D-type male connector  
CBL-SCS68/3/X21/M 
15-pin D-type male connector 
CBL-SCS68/3/V36/M 
37-pin D-type male connector  
CBL-SCS68/3/V36/F 
37-pin D-type female connector  
rs-232 
CBL-SCS68/3/232/M 
25-pin D-type male connector  
Working with Bidirectional Broadcast  
When configuring bidirectional broadcast applications (see Bidirectional Broadcast Applications in Chapter 
8), the following must be taken into account.  
If both the Control Center and the RTU equipment support end-to-end control, it must be enabled on both 
ends. In this case reception/transmission of bi-directional broadcast data channel is enabled/disabled by 
the state of the remote/local RTS line.  
If the RTU equipment does not support end-to-end control, the idle channels of the RTU must transmit 
0xFF data. 
Configuring E1/T1 Port as a Clock Source  
To configure an E1/T1 port of the VS module as a clock source, first configure cross-connect on its timeslots 
and only then define the port as a clock source. 
13. Versatile I/O Modules 
Configuring Cross-Connect in VS-6/C37 Module 
When configuring cross-connect in the VS-6/C37 module, pay attention to the following. Due to a specific 
structure of the C37.94 frame, the selected number of timeslots is controlling the rate bits inside the frame 
indicating the rate. If you cross-connect a single timeslot n of the C37.94 link and n > 1, all the timeslots 
preceding n are opened automatically. For this reason, when the module is used as a tributary and 
connected to an RTU, configure the cross-connected timeslots starting from 1. For example, instead of the 
following command  
ds0 ds1-opt 1/1 ts 3 e1-i cl-a/1 ts 2 data bi-direction 
ds0 e1-i cl-a/1 ts 2 ds1-opt 1/1 ts 3 data bi-direction 
use 
ds0 ds1-opt 1/1 ts 1 e1-i cl-a/1 ts 2 data bi-direction 
ds0 e1-i cl-a/1 ts 2 ds1-opt 1/1 ts 1 data bi-direction 
When the module is used as an uplink (two Megaplex-4 devices are connected via C37.94 link), in order to 
assure its future operation without affecting the running services, it is important to cross-connect the 
timeslots which are not used for tributaries. 
Configuring the Rates with R.111 Encapsulation  
When working with R.111 encapsulation, you can work with split-ts and full timeslot cross-connect. Split 
timeslot cross-connect allows carrying several data channels on a single timeslot. The figure below shows 
the number and the location of bits that must be configured for each supported rate. 
Split timeslot cross-connect is supported when the selected rate is 2 or 4 bits. As seen from the figures 
below, when the selected rate is 8 bits, only full timeslot cross-connect is possible. The following bit 
allocations can be selected for split timeslot cross-connect: 
• 
For 2.4 and 4.8 kbps – bits 1-2, 3-4, 5-6, 7-8 
• 
For 9.6 kbps – bits 1-4, 5-8. 
 
1 
2 
3 
4 
5 
6 
7 
8 
Rate 
 
 
 
 
 
 
 
 
2.4, 4.8 
 
 
 
 
 
 
 
 
9.6 
 
 
 
 
 
 
 
 
19.2 
Number and Location of Bits in R.111 Encapsulation, using Split Timeslot Cross-connect 
13. Versatile I/O Modules 
1 
2 
3 
4 
5 
6 
7 
8 
Rate 
 
 
 
 
 
 
 
 
2.4, 4.8 
 
 
 
 
 
 
 
 
9.6 
 
 
 
 
 
 
 
 
19.2 
Number and Location of Bits in R.111 Encapsulation, using Full Timeslot Cross-connect  
When working with split timeslot cross-connect, the data rates must be set according to the following 
table. 
 
 
Actual Number of Bits in Megaplex-4  
Rate, kbps 
Number of bits  
2.4 
2 
4.8 
2 
9.6 
4 
19.2 
8 
Configuring the Module with HCM Encapsulation 
HCM (High Capacity Multiplexing) is a Newbridge proprietary rate-adaption and sub-rate multiplexing 
scheme providing a bandwidth granularity of 800 bps throughout a network, by formatting low speed data 
into 10 bytes frame.  
Serial data transmission rates below the rate of a single DS0 (less than 64 kbps), are achieved using the 
High Capacity Multiplexing (HCM) proprietary protocol. These rates are known as sub-rates.  
The HCM format is based on multiplexing with a DS0 timeslot. Specifically, a DS0 is further multiplexed into 
a 10-byte structure with bytes in the 10 bytes frame labeled F0 through F9.   
In this mode, you must specify the location of the data channel within the HCM frame. This is done by 
means of two parameters: F (frame 0 to 9) and B (bits 0 to 7). In CLI this is done by setting the data-
position parameter. 
The columns are labeled B7-B0 and are the traditional 8 bits of a DS0 byte (or timeslot), with B0 serving as 
the LSB (Least Significant Bit).  F0-F9 represent the 10 byte structure of an HCM frame. The HCM frame has 
a multiframe structure containing a single framing bit, F, used to obtain multiframe synch.  
13. Versatile I/O Modules 
Bandwidth allocated to a circuit within an HCM frame is represented by HCM elements containing a D (for 
Data), where each D represents 800 kbps of bandwidth. 
End-to-end controls (Control Signal transport and remote sync indication) are implemented in CLI by 
enabling the s-bit-signaling parameter. S-bit (the HCM signaling superframe channel) is defined as a 
sequence of bits which are transmitted serially one per HCM frame with repetition period of 16 SF 
(Signaling SF). 
To configure the frames, use the following rules: 
• 
F-Bit is always located in a fixed location cell F0/B7 
• 
The channel rate is defined by the number of Data bits in the frame (for example 4.8 kbps = 800 
bps x 6 bits).  
• 
The value of F defines the number of row where the first data bit is allocated. 
• 
The value of B defines the number of columns (on the right) not available for data. For example:  
 
B=0 –full timeslot,  
 
B=1 – first column is not used 
 
B=2 – first 2 columns are not used  
• 
S-Bit (Signaling-Bit) value “Enabled/Disabled” changes the position of the first cell that carries data 
bits.  
Examples for various bit allocations are shown in the diagrams below together with the corresponding 
scripts. 
Example 1. 
 
configure port 
13. Versatile I/O Modules 
serial 1/1 
encapsulation-mode hcm 
interface rs-232 
rate 4.8 
data-position f 2 b 4 
no shutdown 
exit 
Example 2. 
 
configure port 
serial 1/1 
encapsulation-mode hcm 
interface rs-232 
rate 2.4 
data-position f 3 b 1 
s-bit-signaling on  
no shutdown 
exit 
Example 3. 
F=3 
B=1 
Signaling Yes 
Rate 2.4K 
13. Versatile I/O Modules 
 
configure port 
serial 1/1 
encapsulation-mode hcm 
interface rs-232 
rate 4.8 
data-position f 2 b 4 
s-bit-signaling on  
no shutdown 
exit 
Configuring the PW IP Scheme  
When configuring the PW IP Scheme in VS modules, two options are available: 
• 
Option 1:  
 
Each PW card is assigned to a dedicated Router interface (dedicated subnet) 
 
Each PW card is configured over a different L2 broadcast domain (VLAN or Bridge/VLAN) 
• 
Option 2:  
 
Each PW card is configured with a dedicated IP address 
 
All PW cards IP addresses share the same IP subnet 
 
All PW cards share the same L2 Broadcast domain (configured over a Bridge/VLAN) 
Configuration concepts for these options are illustrated in the following figures. 
13. Versatile I/O Modules 
 
Option 1 without the Bridge – Traffic Flow 
 
 
Option 1 with the Bridge – Traffic Flow 
13. Versatile I/O Modules 
 
Option 2 – Logical Diagram 
  
Option 2 – Forwarding Diagram 
Choose Option 2 if you want a single VLAN (broadcast domain) and same subnet for all PW cards. A typical 
use case for this option is configuring PW over ERP (G.8032 Ring). 
 To configure Option 2: 
1. Configure each module with a loopback address in the same subnet: 
13. Versatile I/O Modules 
configure slot 1 
card-type versatile vs-12 
bind loopback-address 10.10.10.21 
exit 
configure slot 2 
card-type versatile vs-12 
bind loopback-address 10.10.10.22 
exit 
2. Configure a single router interface so that LB addresses of all configured modules are in the subnet 
of this router interface 
3. Connect (using SVI and flows, connect this router interface to a Bridge port residing over a 
Bridge/VLAN. 
Note: The PW peer IP must be in the subnet of the relevant Router Interface. 
Configuration Sequence 
The list of tasks that can be performed on the VS module and the recommended configuration sequence 
are described in the table below. For detailed descriptions, refer to Chapter 5. The second column indicates 
the configuration context for this task, under which it can be found in Chapter 5. The third column refers to 
the reference tables that should be consulted when planning the module operation. 
Task 
Configuration Context 
Comments and Reference  
Configure a module and put it 
into service 
configure>slot>card-type  
VS-12: card-type=versatile vs-12 
VS-6/BIN: card-
type=versatile  vs-6-bin 
VS-6/C37: card-
type=versatile  vs-6-c37 
VS-6/703: card-type=versatile  vs-
g703-pw 
Configure the serial port 
parameters  
configure>port>serial 
Serial Ports in Chapter 5 
Configure the tdm-bridge port 
parameters  
configure>port>tdm-bridge 
TDM Bridge Ports in Chapter 5 
Note: You must also configure the CL.2 or uplink module port parameters (depending on the VS 
module application). For the uplink module configuration procedure, refer to the appropriate section 
of this Appendix.  
13. Versatile I/O Modules 
Task 
Configuration Context 
Comments and Reference  
Configuring the cmd-in ports 
(VS-6/BIN only) 
configure>port>cmd-in 
Configuring Binary CMD-IN 
Command Ports in Chapter 5 
Configuring the cmd-out ports 
(VS-6/BIN only) 
configure>port>cmd-out 
Configuring Binary CMD-OUT 
Ports in Chapter 5 
Configuring the cmd-channels 
(VS-6/BIN only) 
configure>port>cmd-channel 
Configuring Binary CMD-
CHANNEL Ports in Chapter 5 
Configuring the DS1 optical ports 
(VS-6/C37 only) 
configure>port>ds1-opt 
Configuring DS1 Optical Ports in 
Chapter 5 
Configuring pseudowire services  
 
 
Routing parameters for the 
Megaplex-4 PW router 
(interfaces, associated static 
routes, default gateway) 
configure>router (2) 
Pseudowire Router in Chapter 8 
Adding pseudowire peers  
configure>pwe>pw>peer 
Peer in Chapter 8 
Configuring the PW peer 
parameters 
configure>peer 
Peer in Chapter 8 
Configuring the pseudowires  
configure>pwe>pw 
Pseudowires in Chapter 8 
Configuring the internal DS1 
ports  
configure>port>ds1  
DS1 Ports in Chapter 5 
Assigning a VS PW module with a 
dedicated IP address to support 
a single VLAN (broadcast 
domain) and same subnet for all 
PW modules  
configure>slot 
 
Configuring the PW IP Scheme in 
in the section above 
Configuring flows 
 
 
Configuring ingress and egress 
flows between the SVI port 
(bound to Router 2 interface) 
and Logical MAC port or Ethernet 
port  
configure>flows 
 
Flows in Chapter 8 
Configuring cross-connect  
 
 
13. Versatile I/O Modules 
Task 
Configuration Context 
Comments and Reference  
Configuring DS0 cross-connect 
between the serial/cmd-
channel/DS1 port or the module 
and timeslots on the E1/T1/DS1 
ports of the uplink module) 
configure>cr>ds0 
DS0 Cross-Connect in Chapter 8 
 
Configuring DS0 cross-connect 
between the timeslots of serial 
and DS1 ports of the same 
module) 
configure>cr>ds0 
DS0 Cross-Connect in Chapter 8 
 
Cross-connecting the DS1 port 
with a vc12-vt2/vc11-vt1.5 from 
an SDH/SONET port  
configure>cr>sdh-sonet   
 
SDH/SONET Cross-Connect in 
Chapter 8 
 
Establishing cross-connection 
between the pseudowire and 
timeslots on the ds1 or serial 
port (of the VS module) 
configure>cr>pw-tdm  
 
PW-TDM Cross-Connect in 
Chapter 8 
 
Configuring protection  
 
 
Configuring protection for 
internal DS1 ports 
configure>protection>tdm-
group 
TDM Group Protection in 
Chapter 7 
 
Configuring protection for PWs 
configure>protection>pw 
PW Protection in Chapter 7 
Configuring protection for 
individual timeslots on various 
uplink modules  
configure>protection>ds0-
group 
DS0 SNCP Protection in Chapter 7 
Creating an alarm input and 
setting the alarm description 
(VS-6/BIN only) 
configure>reporting 
Configuring Alarm Reporting in 
Chapter 11 
Binding an alarm of specific 
source type (optionally on a 
specific user port) to an alarm 
output port (VS-6/BIN only) 
configure>reporting 
Configuring Alarm Reporting in 
Chapter 11  
13. Versatile I/O Modules 
Configuration Examples (VS-6/BIN)  
Example 1. Transmitting Internal Alarms to Output Relays  
This typical configuration example includes the following actions: 
• 
Configure VS-6/BIN module in slot 4 
• 
Configure VS-6/BIN outbound ports 
• 
Bind all E1 alarms in the chassis to CMD-OUT port 4/1/2 (alarm state is indicated by open cicruit) 
• 
Bind E1 LOS alarm in port 9/3 to CMD-OUT ports 4/1/1 and 4/1/3 (alarm state is indicated by 
closed circuit – default setting) 
configure slot 4 card-type versatile vs-6-bin 
 
configure port cmd-out 4/1/1 no shutdown 
configure port cmd-out 4/1/2 no shutdown 
configure port cmd-out 4/1/3 no shutdown 
configure port cmd-out 4/1/4 no shutdown 
configure port cmd-out 4/2/1 no shutdown 
configure port cmd-out 4/2/2 no shutdown 
configure port cmd-out 4/2/3 no shutdown 
configure port cmd-out 4/2/4 no shutdown 
 
configure port cmd-out 4/1/2 alarm-state-energized no 
 
configure reporting bind-alarm-to-relay e1 all alarm-output 4/1/2 
configure reporting bind-alarm-source-to-relay e1 los 9/3 alarm-output 4/1/1 
configure reporting bind-alarm-source-to-relay e1 los 9/3 alarm-output 4/1/3 
Example 2. External Alarm Reporting  
This typical configuration example includes the following actions: 
• 
Configure VS-6/BIN module in slot 4 
• 
Configure the module inbound ports 
• 
Connect External Alarm “Inbound Alarm 1” to CMD-IN port 4/1/1 (high voltage means that 
command input is in active state – default) 
• 
Connect External Alarm “Inbound Alarm 2” to CMD-IN port 4/1/2 (low voltage means that 
command input is in active state) 
• 
Connect External Alarm “Inbound Alarm 3” to CMD-IN port 4/2/1(high voltage means that 
command input is in active state – default)  
13. Versatile I/O Modules 
• 
Display the current state of configured ports.  
configure slot 4 card-type versatile vs-6-bin 
configure port cmd-in 4/1/1 no shutdown 
configure port cmd-in 4/1/2 no shutdown 
configure port cmd-in 4/2/1 no shutdown 
 
configure port cmd-in 4/1/2 input-active low  
 
configure reporting alarm-input 4/1/1 description "Inbound Alarm 1" 
configure reporting alarm-input 4/1/2 description " Inbound Alarm 2" 
configure reporting alarm-input 4/2/1 description " Inbound Alarm 3”  
 
config>reporting# info detail  
alarm-input  cl-a/1 active  off description  "" 
alarm-input  4/1/1 active  off description "Inbound Alarm 1" 
alarm-input  4/1/2 active  off description "Inbound Alarm 2"    
alarm-input  4/1/3 active  off description  "" 
alarm-input  4/1/4 active  off description  "" 
alarm-input  4/2/1 active  off description "Inbound Alarm 3" 
alarm-input  4/2/2 active  off description  "" 
alarm-input  4/2/3 active  off description  "" 
alarm-input  4/2/4 active  off description  "" 
bind-alarm-to-relay e1 all alarm-output 4/1/2 
 
bind-alarm-source-to-relay  e1  los  9/3 alarm-output  4/1/1 
bind-alarm-source-to-relay  e1  los  9/3 alarm-output  4/1/3 
Diagnostics  
Serial Ports 
VS diagnostic capabilities include local and remote digital loopbacks on each serial port (see Serial Ports in 
Chapter 5).  
DS1-Optical Ports 
VS diagnostic capabilities include local and remote digital loopbacks on each DS1-opt port (see DS1 Optical 
Ports in Chapter 5).  
DS1 Ports 
DS1 diagnostic capabilities include local and remote loopbacks on each DS1 port (per timeslot) (see DS1 
Ports). VS-6/703 modules also feature local and remote loopbacks per entire DS1 port.  
13. Versatile I/O Modules 
Monitoring  
The monitoring tasks supported on each local VS port level are listed in the table below. 
Level 
Monitored Feature 
Path  
Reference 
Serial ports  
Status data  
configure>port> 
serial  
Serial Ports  in Chapter 5 
 
Statistics (3-bit transitional, 
HCM, R.111 encapsulation 
modes) 
configure>port> 
serial 
Serial Ports  in Chapter 5 
 
DS1 ports 
Status data for the DS1 port 
 
configure>port>ds1 
DS1 Ports in Chapter 5  
DS1 optical ports 
Status data for the ds1-opt 
port 
configure>port>ds1-opt 
DS1 Optical Ports in 
Chapter 5  
Binary 
Command ports 
 
 
 
Transmission performance 
statistics 
configure>port>cmd-in 
configure>port>cmd-
out 
configure>port>cmd-
channel 
Binary Command Ports  
in Chapter 5 
 
Status data  
configure>port>cmd-in 
configure>port>cmd-
out 
configure>port>cmd-
channel 
Binary Command Ports  
in Chapter 5 
 
Protection status  
configure> protection> 
tdm-group 
TDM Group Protection 
in Chapter 7  
PW ports  
 
Transmission performance 
statistics  
configure>port>pw 
Displaying PW Statistics 
in Chapter 8  
 
Status data  
configure>port>pw  
Viewing the Pseudowire 
Status in Chapter 8  
 
Protection status  
configure> 
protection>pw 
PW Protection in 
Chapter 7  
Troubleshooting  
If a problem occurs, check the displayed alarm messages and refer to Chapter 11 for their interpretation.  
13. Versatile I/O Modules 
Serial Ports 
If, after collecting all the relevant information, the problem appears to be related to the serial port 
submodule, perform the actions listed below, until the problem is corrected.  
If a complaint is received from one of the subscribers connected to the VS channels, first activate the local 
test loop at the side where the complaint comes from. The local subscriber must receive its own signal. 
If the signal is not received, the problem is at the local end: 
• 
Check the connections to the user equipment or the user equipment itself. 
• 
Replace the cable 
• 
Replace the local VS module. 
If the local subscriber receives its own signal when the local loopback is connected, activate the remote 
loopback at the remote side and repeat the check. 
If the remote loopback indicates that the link operates normally, the problem is at the remote end. To 
check, repeat the procedure on the remote Megaplex unit. 
Binary Command Ports 
If, after collecting all the relevant information, the problem appears to be related to the operation of the 
VS module, perform the actions listed below, until the problem is corrected.  
Inbound Alarm not Reported 
Check whether the corresponding CMD-IN indicator lights when the external alarm condition is present.  
• 
If not, check the cable connecting the external equipment to the CMD 1-8 IN/OUT connector, and 
make sure the alarm indication reaches the correct pins at the cable end attached to the VS-6/BIN 
module.  
• 
If not, replace the cable connecting the external equipment, or troubleshoot that equipment. 
• 
If the corresponding CMD-IN indicator lights, check whether the inbound alarm is masked. If it is 
not masked, replace the VS-6/BIN module. 
Outbound Alarm not Reported 
Check whether the corresponding CMD-OUT indicator lights when the alarm condition is present.  
• 
If not, check whether the alarm is masked. If not masked, replace the VS-6/BIN module. 

## 13.3 VS Voice Modules  *(p.994)*

13. Versatile I/O Modules 
• 
If the corresponding CMD-OUT indicator lights, check the cable connecting the external equipment 
to the CMD 1-8 IN/OUT connector, and make sure the alarm indication (open/short-circuit, in 
accordance with the port configuration) reaches the correct pins at the cable end attached to the 
equipment. If not, replace the cable connecting the external equipment, or troubleshoot that 
equipment. 
If the problem cannot be corrected by performing these actions, the VS-6/BIN module is probably defective 
and must be replaced.  
13.3 VS Voice Modules  
This section describes the technical characteristics, applications, installation and operation of the VS-6/FXS, 
VS-6/FXO, VS-6/E&M, VS-8/E&M, VS-OCU/E&M and FXS/E&M voice interface modules for use in the 
Megaplex-4 Next Generation Multiservice Access Node.  
Product Options 
Serial/E&M/FXS/FXO Options  
Voice modules are available in the following versions:  
• 
VS-6/FXS module consisting of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels   
 
Lower: voice submodule with 8 FXS ports. 
• 
VS-6/FXO module consisting of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels   
 
Lower: voice submodule with 8 FXO ports. 
• 
VS-6/E&M module consisting of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels   
 
Lower: voice submodule with 4 E&M ports. 
• 
FXS/E&M module consisting of the following submodules:  
 
Upper: voice submodule with 8 FXS ports. 
 
Lower: voice submodule with 4 E&M ports. 
• 
VS-8/E&M module consisting of the following submodules:  
13. Versatile I/O Modules 
 
Upper: voice submodule with 4 E&M ports. 
 
Lower: voice submodule with 4 E&M ports. 
• 
VS-OCU/E&M module consisting of the following submodules:  
 
Upper:  submodule with 2  OCU-DP – DDS ports. 
 
Lower: voice submodule with 4 E&M ports. 
Enhanced PW Capabilities  
VS-6/FXS, VS-6/FXO, VS-6/E&M and VS-8/E&M modules are available in additional, advanced versions 
featuring enhanced PW capabilities – in particular, adaptive clock recovery (ACR).  
Note 
When the information is applicable to both basic and advanced version of the 
module, the basic name (such as VS-6/FXS) is used in this manual.  The 
complete designation is used only for information applicable to a specific PW-
enhanced version.  
Applications  
Basic VS-6/E&M Applications 
The following figure shows a basic E&M tie line application using VS-6/E&M modules. 
In this application, one VS-6/E&M module is used to provide 4 E&M tie lines between two analog PBXs 
through the SDH/SONET link interconnecting the Megaplex systems. 
Megaplex-4
PBX
VS-6/E&M
Megaplex-4
PBX
VS-6/E&M
SDH/SONET
4 Tie 
Lines
4 Tie 
Lines
 
Basic Application for VS-6/E&M Modules  
Off-Premises Extension (OPX) Applications 
In a typical OPX application (see below), one VS-6/FXO module located at the PBX side is used in a link with 
an VS-6/FXS module to provide up to 8 off-premises extensions for an analog PBX connected to the VS-
6/FXO module channels.  
13. Versatile I/O Modules 
Megaplex-4
PBX
VS-6/FXO
Megaplex-4
VS-6/FXS
Extension
Lines
E1 or T1 Link
Ringer-2100R
FXS
1
8
 
OPX Application for VS-6/FXO and VS-6/FXS Modules  
The system configuration shown above permits using telephones connected to the channels of a VS-6/FXS 
module installed in the Megaplex unit located at the other end of the link as extensions of an analog PBX. 
Each remote telephone then becomes a regular local PBX subscriber, which can be dialed by other 
subscribers using standard procedures, and can also dial any other PBX subscriber and use all the services 
available to local PBX subscribers. 
PSTN Access Applications  
Due to the flexible signaling configuration capabilities, the VS-6/FXO modules can also be used on links 
ending in the public switched telephone network (PSTN). A typical PSTN access application is shown below.  
Megaplex-4
PBX
Extension 
Lines
VS-6/FXO
E1/T1
STM-1/OC-3
STM-4/0C-12
Public Switched
Telephone Network 
(PSTN)
Subscribers
 
PSTN Application for FXO Modules  
In the application shown above, the extension lines of an analog PBX are connected to the channels of a 
VS-6/FXO module, installed in a Megaplex unit connected to the PSTN through an E1/T1 or STM-1/OC-
13. Versatile I/O Modules 
3/STM-4/OC-12 trunk line. This enables the PBX subscribers to dial PSTN subscribers through the Megaplex 
link, and PSTN subscribers can dial to PBX subscribers. 
DDS Circuit Emulation Applications  
The figure below shows DDS circuit emulation over packet.   
Megaplex-4
56/72 Kbps
DTE
DDS CSU
56/64 Kbps
IP/MPLS
Ethernet
RS-232
Megaplex-4
56/72 Kbps
DDS CSU
RS-232
DTE
56/64 Kbps
 
 
Module Architecture 
The module architecture and data flow for VS voice modules with serial submodules are shown in two 
figures below. The VS Voice Module Architecture Entities and their Hierarchy table lists the module entities 
(ports) and their hierarchy.  
DS0
CL.2 DS0
Cross connect
GbE
CL.2 Ethernet 
Engine
tdm-bridge
1..6
Serial
1..6
29xE1
6xE1
12xE1
12xE1
PW 
1..24
DS1
1..12
Switch
Voice 1..8
(FXS/FXO)
Voice 1..4
(E&M)
 
VS-6/FXS, VS-6/FXO and VS-6/E&M Module Architecture  
13. Versatile I/O Modules 
DS0
CL.2 DS0
Cross connect
GbE
CL.2 Ethernet 
Engine
tdm-bridge
1..4
Serial
1..6
23xE1
6xE1
12xE1
12xE1
PW 
1..24
DS1
1..12
Switch
Voice 1..8
(FXS/FXO)
Voice 1..4
(E&M)
 
VS-6/FXS/PW, VS-6/FXO/PW and VS-6/E&M/PW Module Architecture  
VS Voice Module Architecture Entities and their Hierarchy  
Name 
Number of Ports  
Possible Values 
 
VS-6/FXS 
VS-6/FXO 
VS-6/E&M 
VS-6/FXS 
VS-6/FXO 
VS-6/E&M 
serial 
6 
6 
slot/1..6 
slot/1..6 
tdm-bridge: 
basic (pw-
enhanced) 
6 (4) 
6 (4) 
slot/1..6(1..4) 
slot/1..6(1..4) 
voice 
8 
4 
slot/1..8 
slot/1..4 
ds1 
12 
12  
slot/1..12 
slot/1..12 
pw 
24 
24 
slot/1..24 
slot/1..24 
The module architecture and data flow for FXS/E&M modules are shown below. The following table lists 
the module entities (ports) and their hierarchy.  
13. Versatile I/O Modules 
DS0
CL.2 DS0
Cross connect
GbE
CL.2 Ethernet 
Engine
13xE1
8xE1
8xE1
PW 
1..16
DS1
1..8
Switch
Voice 1..8
(FXS)
Voice 9..12
(E&M)
 
FXS/E&M Module Architecture Entities and their Hierarchy  
Name 
Number of Ports  
Possible Values 
voice (FXS) 
8 
slot/1..8 
voice (E&M) 
4 
slot/9..12 
ds1 
8 
slot/1..8 
pw 
16 
slot/1..16 
The module architecture and data flow for VS-8/E&M and VS-8/E&M/PW modules are shown in the figures 
below. The tables below list the module entities (ports) and their hierarchy.  
13. Versatile I/O Modules 
VS-8/E&M Module Architecture Entities and their Hierarchy 
DS0
CL.2 DS0
Cross connect
GbE
CL.2 Ethernet 
Engine
10xE1
8xE1
8xE1
PW 
1..8
DS1
1..8
Switch
Voice 1..4
(E&M)
Voice 5..8
(E&M)
 
Name 
Number of Ports  
Possible Values 
voice (E&M) 
8 
slot/1..8 
ds1 
8 
slot/1..8 
pw 
8 
slot/1..8  
VS-8/E&M/PW Module Architecture Entities and their Hierarchy  
DS0
CL.2 DS0
Cross connect
GbE
CL.2 Ethernet 
Engine
10xE1
8xE1
8xE1
PW 
1..16
DS1
1..12
Switch
Voice 1..4
(E&M)
Voice 5..8
(E&M)
 
13. Versatile I/O Modules 
Name 
Number of Ports  
Possible Values 
voice (E&M) 
8 
slot/1..8 
ds1 
12 
slot/1..12 
pw 
8 (16) 
slot/1..16  
Note 1: PWs 9..16 are used for redundancy only. 
Note 2: DS1 ports 9..12 do not support signaling. 
VS-OCU/E&M Module Architecture Entities and their Hierarchy   
DS0
CL.2 DS0
Cross connect
10 x E1
8 x E1
PW 
1..16
DS1
1..12
Serial 1..2
(OCU)
Voice 1..4
(E&M)
8 x E1
1 x E1
GbE
CL.2 Ethernet 
Engine
Switch
 
Name 
Number of Ports  
Possible Values 
serial (OCU) 
2 
slot/1..2 
voice (E&M) 
4 
slot/1..4 
ds1 
12 
slot/1..12 
pw 
8 (16) 
slot/1..16  
13. Versatile I/O Modules 
Features  
VS-OCU/E&M Module  
The VS-OCU/E&M module has two OCU-DP (Office Channel Unit – Dataport®) ports with standard DDS 
interfaces. 
The OCU-DP – DDS interface provides direct connection to products with a built-in CSU/DSU. It is also used 
with standalone CSU/DSU products. 
Each OCU-DP – DDS channel is compatible with AT&T PUB 62310 (Standard DDS) and BELLCORE TA-TSY-
0000777, and operates at data rates of 56 and 64 kbps, which corresponds to 56 kbps/72 kbps line rate. 
The channel interface supports full duplex transmission over two unconditioned two-wire telephone loops 
(twisted pairs) in accordance with the DDS standards, working with AMI line code. Each port has an RJ-45 
connector.  
OCU-DP interface supports sealing current (CSU-loop). Each channel interface has its own sealing current 
source. 
The polarity of the DC voltage provided by the sealing current source (normally tip positive with respect to 
ring) can be reversed, to cause the user’s equipment to activate its CSU (mandatory) loopback 
OCU-DP channel mapping to the Megaplex-4 timeslots is as follows: 
• 
56 kbps service is mapped to a single DS0 
• 
64 kbps service is mapped to two DS0. 
E&M Modules  
The E&M modules have user-selectable 2-wire or 4-wire analog interfaces using E&M signaling. The 
interface type (2-wire or 4-wire) can be independently selected for each channel.  
The E&M modules support four types of E&M signaling: EIA RS-464 types I, II, III and V (similar to British 
Telecom SSDC5). The figure below shows the equivalent signaling circuits for the different signaling modes. 
The signaling type should be the same for all the four channels (VS-6/E&M), or for each group of four 
channels (VS-8/E&M). 
• 
EIA RS-464 Type I signaling standard is supported without any external power supply. 
• 
EIA RS-464 Type II, III and V (BT SSDC5) signaling standards are supported by means of the 
internal -12 VDC power supply of the chassis. The -12 VDC voltage is suitable for most PBX systems. 
However, for full support of the EIA RS-464 Type II, III and V (BT SSDC5) signaling standards, 
a -48 VDC signaling voltage is required.  
13. Versatile I/O Modules 
The required -48 VDC voltage is always available when the Megaplex chassis is powered from a -
48 VDC source. An AC-powered Megaplex-4100/4104 chassis can be connected to an external 
ringer unit.  
The E&M modules provide signaling at +12V for applications that require positive signaling voltage 
(for example, radio transmitters) and perform fault propagation. In this mode, the VS voice module 
sends signaling to the radio transmitters by connecting GND to the E pin.  
13. Versatile I/O Modules 
 
E&M Equivalent Signaling Circuits  
13. Versatile I/O Modules 
The E&M Voice Activity Detection (VAD) feature allows Megaplex to identify whether an E&M voice 
channel is connected and active by analyzing PCM voice samples. Once enabled using the activity-detection 
configuration parameter, the detected connection status is shown in the E&M CLI status screen as Up 
(connected/active) or Down (disconnected/not active).  
FXS and FXO Modules  
The FXS and FXO submodules are used to connect regular telephone sets (and other equipment with 
similar interface properties) to central office (PSTN) and PBX extension lines.  
FXS and FXO submodules are intended for operation in a link, with the FXS module at the subscriber side 
and the FXO module at the central office or PBX side. However, FXS modules can also operate in a link with 
E&M modules. 
FXS Module Characteristics 
The FXS modules have 2-wire analog interfaces and support FXS loop-start signaling, for direct connection 
to subscriber telephone sets. The FXS modules also support wink-start signaling.  
To enable wink-start signaling, the FXS modules support feed voltage (battery) polarity reversal.  
The FXS modules require -48 VDC to supply the subscriber feed and ring voltages. The ring voltage is 
generated on the module itself, by an internal ringer.  
The required voltage can be supplied via the internal supply voltage connector of the module, from the 
chassis voltage distribution bus. 
FXO Module Characteristics  
The FXO modules have 2-wire analog interfaces and support FXO loop-start signaling for direct connection 
to central office and PBX extension lines.  
The FXO modules also support wink-start signaling.  
To enable wink-start signaling, the FXO module supports the detection of feed voltage (battery) polarity 
reversal.  
The FXO modules do not require any external supply voltage. 
Analog Signaling Profile 
Analog voice signals are digitized using PCM (Pulse-code modulation), in compliance with ITU-T G.711 and 
AT&T Pub. 43801 standards, the signaling information of each voice channel is carried by means of up to 
13. Versatile I/O Modules 
four bits (signaling bits), designated by the applicable standards as bits A, B, C and D. The analog signaling 
format can be modified by defining analog signaling profiles. The analog signaling profile is configured per 
channel and per direction. For more information on configuring analog signaling profiles, see Analog 
Signaling Profiles in Chapter 5.  
Pseudowire Services  
VS voice I/O modules provide TDM pseudowire access gateway services over packet-switched networks 
(Ethernet and IP) for TDM traffic (E1, T1, high-speed and low-speed data, voice) received via the Megaplex-
4 TDM buses from other modules. This is done via independently-configurable internal DS1 ports available 
in the module. The number of DS1 ports is 12 for any VS module.  
In addition, the module provides direct PW access to its serial ports. The number of PW ports is 24 per any 
VS module. Out of these 24 ports 12 are used as working ports and other 12 as protection ports.  
VS modules provide pseudowire emulation services over packet-switched networks using the CESoPSN 
(structure-aware TDM circuit emulation over PSN) protocols in accordance with RFC5086. 
The pseudowire services enable converting TDM payload to packets and transferring these packets through 
router interfaces defined in the Megaplex-4.   
Packet structure is independently selectable for each pseudowire, for compatibility with the PSN type 
(UDP/IP or ETH). For maximum flexibility in system applications, the framing format of the pseudowire 
device at the destination (referred to as a pseudowire peer) can also be taken into account. Thus, in many 
cases traffic using the E1 standards can be directed at destinations using the T1 standards, and vice versa. 
The pseudowire exit port toward the PSN is also selectable, either via any Ethernet port (GbE, Fast 
Ethernet, or VCG) of any module installed in the chassis. The selectable exit ports are bound (via SVI ports) 
to router interfaces, where each router interface has its own IP source address and, optionally, its own 
VLAN. Each VS submodule supports up to 12 interfaces, CL.2 modules support unlimited number of 
interfaces. However, the maximum number of router interfaces per Megaplex-4 is 100. The user can also 
specify static routes to control the IP routing.  
PW-enhanced voice modules have independent adaptive clock recovery (ACR) mechanisms for each 
pseudowire, which recover the original timing (clock rate) of the far-end source of each pseudowire, 
according to ITU G.8261, G.823, G.824 and MEF 22 recommendations. The clock recovery mechanisms can 
provide recovered clock signals to serve as timing references for the Megaplex-4.  
13. Versatile I/O Modules 
Cross-Connections 
The VS voice modules feature DS0 and PW-TDM cross-connections, which can be used according to the 
module application as shown in the table below. For description of DS0 and PW-TDM cross-connect 
functionalities, see respective sections in Chapter 8. 
DS0 Cross-Connect  
The DS0 cross-connect matrix of the Megaplex-4 chassis enables flexible payload routing in the VS voice 
modules, independently configurable for each port, at the individual timeslots (DS0) level. This routing is 
configured via ds0 cross-connect command as follows: 
• 
Serial submodule: between the serial ports and timeslots on the E1/T1/DS1/DS1-opt ports of the 
uplink module.  
In addition to the normal full-duplex (bidirectional) mode, VS serial ports feature additional 
transmission modes, which enable point-to-multipoint communication: 
 
Unidirectional (simplex) transmission, where each channel can be configured either to receive 
(unidirectional RX) or transmit (unidirectional TX). 
 
Bidirectional broadcast (half-duplex) communication, suitable for polled applications. In this 
mode, a channel can not only receive, but can also  transmit (not both simultaneously).  
 
This feature is available for VS modules configured to 3-bit-transitional mode (and operating at 
64 kbps) and R.111 mode.  
 
For configuration considerations, see Error! Reference source not found. below. 
 
VS modules operating in V.110 mode also support split timeslot allocation. 
• 
Voice submodule: between the voice ports and timeslots on the E1/T1/DS1/DS1-opt ports of the 
uplink module.  
In addition to the normal full-duplex (bidirectional) mode, VS E&M voice ports feature additional 
transmission modes, which enable point-to-multipoint communication: 
 
Unidirectional (simplex) transmission, where each channel can be configured to receive 
(unidirectional RX). 
 
Bidirectional broadcast (half-duplex) communication, suitable for polled applications. In this 
mode, a channel can not only receive, but can also transmit (not both simultaneously).  
PW-TDM Cross-Connect  
Voice ports are connected to PWs via DS1 ports, as shown in the diagram below. 
13. Versatile I/O Modules 
PW 
Static 
Router
serial/
voice
pw
1/1
cross connect 
dso
flow
RI
ETH
peer
ds1
1/1
1:1
cross connect 
pw-tdm
serial/
voice
 
Serial ports of VS voice modules feature direct PW cross-connect with PWs, as explained in Error! 
Reference source not found. section. 
VS voice modules can be also used as servers for other modules not equipped with PW. In the diagram 
below, any Megaplex-4 service port is cross-connected to the DS1 port of the VS module (DS0 cross-
connect); DS1 ports are cross-connected to PW (PW-TDM cross-connect). 
PW 
Static 
Router
Any port
pw
1/1
cross connect 
dso
flow
RI
ETH
peer
ds1
1/1
1:1
cross connect 
pw-tdm
Any port
Any Megaplex-4  
module
VS module
 
Cadence 
Cadence is used for setting the cadence of the ring about FXS and FXO modules, it may be generated locally 
or translated directly from the received signaling bit. 
Forward Disconnect and Loop Disconnect 
Forward disconnect functionality is signaling sent from a central office to a telephone subscriber to 
indicate that the calling party has hung up. This indicates that answering machines should stop recording, 
notifies conference call bridges that a participant has left or removes an abandoned call from a hold queue 
or interactive voice response menu. The FXS module disconnects the battery for the period selected in the 
CLI. 
Loop disconnect functionality is used to provide disconnect supervision from a central office. When the 
caller hangs up, the battery voltage to the called party's line is disconnected for a fraction of a second to 
signal the end of the call. 
The FXO module detects the central office momentary battery voltage removal and signals the remote FXS 
module to disconnect the battery for the period selected in the CLI. 
Protection  
The VS voice module features the following types of protection: 
13. Versatile I/O Modules 
• 
TDM group protection between DS1 ports of the VS module and DS1/DS1-opt/E1/T1/E1-i/T1-i 
ports of other Megaplex-4 modules (see TDM Group Protection in Chapter 7) 
• 
PW protection between two PW ports of the VS module (see PW Protection in Chapter 7). 
• 
DS0 SNCP end-to-end protection of n x ds0 services (ds0 bundles) over any TDM network 
infrastructure by selecting individual timeslots of E1/T1/E1-i/T1-i/DS1 ports of the relevant uplink 
modules (see DS0 SNCP Protection in Chapter 7).  
TDM Group Protection on DS1 Ports 
When pseudowires are configured on redundant internal DS1 ports, the pseudowire traffic is automatically 
protected as well. The protection mode is 1+1, meaning that the traffic is also sent on the protection DS1 
port.  
The figure below illustrates the DS1 TDM group protection. For each protection group, you must first 
configure the internal DS1 port that will serve as the working port; this configuration is copied to the other 
port of the group. In addition, it is necessary to configure pseudowires from each internal DS1 port in the 
protection group to the desired destinations.  
 
GbE
CL-A/1
GbE
CL-B/1
I/O 
Serial Port
DS1 #1
Working
PW #1
PW #2
SVI #1
SVI #2
DS1 #2
Protection 
TDM Group
 
TDM Group Protection for DS1 Ports   
PW Protection  
For PW protection, two PW ports on the same module are connected to the same DS1 port. A typical 
configuration is shown in the figure below.  
13. Versatile I/O Modules 
GbE
CL-A/1
GbE
CL-B/1
I/O 
Serial Port
DS1
PW #1
Working 
PW #2
Protection
SVI #1
SVI #2
 
PW Protection  
During normal operation, both PW ports process as usual the transmit and receive signals, but the receive 
output of the protection port is disconnected. The operational state of the protection port is continuously 
monitored to ensure that it is operating properly. If the working link fails, the corresponding port is 
disconnected, and the protection port takes over.  
For two ports configured to PW protection, the following parameters must be the same for both ports: 
• 
psn type (udp-over-ip or Ethernet)  
• 
tdm-oos  
• 
tdm-payload. 
DS0 SNCP Protection  
For DS0 SNCP protection, each tributary service is cross-connected to one or more timeslots on the 
selected E1/T1/E1-i/T1-i/DS1 link. In parallel, the same timeslots are grouped as ds0-bundles. Per each ds0-
bundle the user is asked to configure a timeslot and a signaling bit inside TS 16 for E2E path monitoring – 
for details, see Chapters 6 and 7). A typical configuration is shown in the figure below.  
Tributary
Port
E1/T1#1
E1/T1#2
ds0-
bundle#1
ds0-
bundle#2
DS0
CC
 
13. Versatile I/O Modules 
TDM SNCP Protection  
The data from the tributary port is transmitted to both uplink ports (parallel Tx mode. Based on the path 
status, it selects the active Rx path of the data. 
Timing  
The VS voice module has an internal timing generator that receives the nodal timing and clock signals from 
the Megaplex-4 chassis and generates the internal timing and clock signals needed for module operation.  
The serial port synchronous channel timing mode is DCE: the serial port provides the clock signals to the 
DTE connected to it. This mode is suitable for connecting equipment with DTE interface to the VS ports.  
• 
The PW-enhanced VS-voice modules have independent adaptive clock recovery (ACR) mechanisms 
for each pseudowire, which recover the original timing (clock rate) of the far-end source of each 
pseudowire, according to ITU G.8261, G.823, G.824 and MEF 22 recommendations. The clock 
recovery mechanisms can provide recovered clock signals to serve as timing references for the 
Megaplex-4.  
For the VS-OCU/E&M module, the CSU/DSU customer equipment must work in LB timing. 
Management 
All the module operational parameters are controlled by means of the Megaplex system management. 
Physical Description  
The VS voice module occupies one I/O slot in the Megaplex-4 chassis. The module is based on a main board 
and two factory-replaceable submodules.  
 
• 
VS-6/FXS module consists of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels   
Interface 
Module 1
Interface 
Module 2
Main Board
13. Versatile I/O Modules 
 
Lower: voice submodule with 8 FXS ports. 
• 
VS-6/FXO module consists of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels   
 
Lower: voice submodule with 8 FXO ports. 
• 
VS-6/E&M module consists of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels   
 
Lower: voice submodule with 4 E&M ports. 
• 
FXS/E&M module consists of the following submodules:  
 
Upper: voice submodule with 8 FXS ports. 
 
Lower: voice submodule with 4 E&M ports.  
• 
VS-OCU/E&M module consists of the following submodules:  
 
Upper: OCU submodule with 2 OCU-DP – DDS ports. 
 
Lower: voice submodule with 4 E&M ports. 
• 
VS-8/E&M module consists of the following submodules:  
 
Upper: voice submodule with 4 E&M ports. 
 
Lower: voice submodule with 4 E&M ports. 
 
VS-6/FXS, VS-6/FXO, VS-6/E&M, FXS/E&M, VS-8/E&M and VS-OCU/E&M module panels are shown in the 
next 5 figures.  
13. Versatile I/O Modules 
 
VS-6/FXS Module Panels 
13. Versatile I/O Modules 
 
VS-6/FXO Module Panels 
13. Versatile I/O Modules 
 
VS-6/E&M Module Panels 
13. Versatile I/O Modules 
 
FXS/E&M and VS-8/E&M Module Panels 
 
13. Versatile I/O Modules 
 
 
VS-OCU-DP/E&M Module Panel 
The module panel includes two submodule panels.  
The upper submodule panel depends on the module version as follows: 
• 
For VS-6/FXS, VS-6/FXO and VS-6/E&M, it includes two 68-pin SCSI-4 female connectors, each 
containing three channels. 
• 
For FXS/E&M, the 8-channel module interface is terminated in four RJ-12 connectors – one per two 
channels. 
• 
For VS-8/E&M, each interface is terminated in four RJ-45 connectors – one per channel. 
• 
For VS-OCU/E&M, the interface is terminated in 2 OCU-DP – DDS ports with two RJ-45 connectors – 
one per channel.  
The lower submodule panel depends on the module version as follows: 
13. Versatile I/O Modules 
• 
For VS-6/FXS, VS-6/FXO, the 8-channel module interface is terminated in four RJ-12 connectors – 
one per two channels. 
• 
For VS-6/E&M, VS-8/E&M, FXS/E&M and VS-OCU/E&M, the 4-channel module interface is 
terminated in four RJ-45 connectors – one per channel. 
LED Indicators 
Serial (OCU) Port Indicators  
Each OCU port of the VS-OCU/E&M module has LOS and TEST indicators. Each port status indicator 
operates as follows: 
• 
LOS indicator (red): Lights steadily when a loss of signal condition is detected by the channel 
• 
TEST indicator (yellow): Lights steadily when a loopback or test is activated: 
 
Local LB 
 
Remote LB 
 
Remote on remote 
Voice Port Indicators  
All voice modules have separate LED indicators for each channel listed in the tables below.  
E&M Channel Indicators 
Name 
Description 
M  
On when the M line of the corresponding channel is off-hook (channel in use). 
E  
On when the E line of the corresponding channel is off-hook (channel in use). 
FXS Channel Indicators 
Indicator 
Number 
Color 
Description 
LOC/REM  
8  
Green/Yellow 
Lights steadily in green – Local “OFF-HOOK” 
Lights steadily in yellow – Remote “OFF-HOOK” 
Flashes in green/yellow – Local and Remote “OFF-
HOOK”. Conversation state 
Off: port is not connected or both directions of 
signaling is “ON-HOOK” 
13. Versatile I/O Modules 
FXO Channel Indicators 
Indicator 
Number 
Color 
Description 
RING/REM  
8  
Green/Yellow 
Lights steadily in green – Ringing is received on the 
corresponding channel 
Lights steadily in yellow – Remote “OFF-HOOK” 
Off: port is not connected or remote “ON-HOOK” 
and ringing is not received on the corresponding 
channel 
Technical Specifications 
For the corresponding technical specifications of serial interface submodule, refer to Technical 
Specifications table of VS (VS-12, VS-6/BIN and VS-6/C37) section in this chapter.   
Number of  
FXS and FXO submodule 
8 
Channels 
E&M submodule 
4  
Voice Processing 
Modulation Technique  
PCM, per ITU-T Rec. G.711 and AT&T Pub. 43801 
 
Companding 
µ-law or A-law (user-selectable)  
Bandwidth 
Requirements 
PCM  
64 kbps per enabled channel (one timeslot)  
Analog Interface 
Interface Type 
 
 
E&M  
4-wire or 2-wire (user-selectable) 
 
FXS, FXO 
2-wire 
Analog Parameters Nominal Level 
0 dBm  
 
Nominal Impedance 
600Ω 
 
Return Loss (ERL) at  
300 to 3400 Hz 
Better than 20 dB 
 
Frequency Response (Ref: 1020 
Hz) 
0 dB ±0.5 dB, at 300 to 3000 Hz 
0 dB ±1.1 dB, at 250 to 3400 Hz 
 
Transmit and Receive Levels 
User-selectable in 0.5 dB ±0.15 dB steps, see below. 
 
Signal to Total Distortion Using 
ITU-T Rec. G.712 (8-bit PCM 
encoding) 
-30 to 0 dBm0:  better than 33 dB 
-45 to +3 dBm0:  better than 22 dB 
 
Idle Channel Noise 
Better than -65 dBm0 (+20 dBrnc) 
13. Versatile I/O Modules 
 
Transformer Isolation 
1500 VRMS  
Transmit and Receive Levels for Various Interfaces  
Module Interface 
Transmit 
[dbm] 
          min               max 
Receive 
[dbm] 
         min               max 
E&M 2W  
-8 
+5 
-17 
+2 
E&M 4W (when there is a mix* 
of 2W/4W ports) 
-8 
+5 
-17 
+3.5 
E&M 4W**  
-17 
+5 
-17 
+9 
FXS 
-5 
+5 
-17 
+1 
FXO 
-3.5 
+5 
-17 
+1 
*within ports 1-4, 5-8 
**all connected ports  
E&M Interface 
Characteristics 
Signaling Method 
(User-Selectable) 
• EIA RS-464 Type I 
• EIA RS-464 Type II, III and V (British Telecom SSDC5) 
using internal -12 VDC in place of -48 VDC 
Note: For full support of Types II, III, and V (SSDC5) 
signaling standards, a -48 VDC supply is required.  
 
Dial Pulse Distortion 
±2 ms max 
FXS Interface 
Characteristics 
Signaling Modes  
EIA RS-464 loop-start and wink-start, user-selectable 
 
On-Hook/Off-Hook 
Threshold  
• Off-hook Threshold: Loop current >11mA 
• On-hook Threshold: Loop current <8mA  
 
Feed Current 
20 mA (±10%) 
 
Ringer Characteristics
 
Ring Voltage  
• 54 VRMS with up to 1 REN load 
• 45 VRMS with up to 5 REN load 
• Protected against overload 
 
 
Ring Frequency  
• 22 Hz (±10%) 
 
 
Ring Cadence 
• 1 second ON, 3 seconds OFF 
 
Reversal Polarity Pulse 
Distortion  
6 ms max 
13. Versatile I/O Modules 
FXO Interface 
Characteristics 
Signaling Modes  
EIA RS-464 loop-start and wink-start, user-selectable 
 
DC Resistance 
• Off-hook: 160 Ω at 50 mA feed, 270 Ω at 25 mA feed. 
• On-hook: 20 MΩ  
 
Ring Impedance 
20 MΩ  
 
Detection Thresholds 
• Detection:  > 16.5 VRMS, 13 to 68Hz 
• No detection:  < 13.5 VRMS 
 
Reversal Polarity Pulse 
Distortion  
6 ms max 
Diagnostics 
 
• Local digital loopback  
• Remote digital loopback  
• Forward tone injection (1 kHz, 0 dBm0) 
• Backward tone injection (1 kHz, 0 dBm0) 
Connectors 
E&M Submodule 
• RJ-45 connector for each channel 
 
FXO and FXS Submodules 
• RJ-12 connector for channels 
Indicators  
E&M Ports 
E-lead, M-lead indicators per channel 
 
FXS Ports 
See FXS Channel Indicators 
 
FXO Ports 
See FXO Channel Indicators  
Environment 
Operating Temperature 
-10°C to 55°C (14°F to 131°F)  
 
Storage Temperature 
-20°C to 70°C  (-4°F to 160°F)   
 
Humidity 
Up to 95%, non-condensing 
Power Consumption 
VS-6/8FXS 
RS-422: 14.7W  
RS-232: 13.1W 
V.35: 14.3W  
VS-6/8FXO 
RS-422: 13.9W  
RS-232: 12.3W 
V.35: 13.5W  
VS-6/4E&M 
RS-422: 17.0W  
RS-232: 15.4W 
V.35: 16.6W 
VS-8FXS/4E&M 
12.4W 
 
VS-8/E&M 
15.1W  
13. Versatile I/O Modules 
 
VS-6/703 
 
RS-422: 16.0W  
RS-232: 14.4W  
V.35: 15.6W 
Configuration 
Programmable via Megaplex system management 
Preparing the Module for Installation 
 
Warning 
Before performing any internal settings, adjustment, maintenance, or 
repairs, first disconnect all the cables from the module, and then remove the 
module from the Megaplex-4 enclosure. 
No internal settings, adjustment, maintenance, and repairs may be 
performed by either the operator or the user; such activities may be 
performed only by a skilled technician who is aware of the hazards involved. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product 
 
Caution 
The modules contain components sensitive to electrostatic 
discharge (ESD). To prevent ESD damage, always hold the 
module by its sides, and do not touch the module components 
or connectors 
 
Caution 
To prevent physical damage to the electronic components 
assembled on the two sides of the module printed circuit 
boards (PCB) while it is inserted into its chassis slot, support the 
module while sliding it into position and make sure that its 
components do not touch the chassis structure, nor other 
modules.  
Installing a Module in the Chassis 
VS voice modules may be installed in an operating chassis (hot insertion). 
 
Warning 
The module starts operating as soon as it is inserted in an operating chassis.  
13. Versatile I/O Modules 
 
 To install a VS voice module:  
1. Refer to the system installation plan and identify the prescribed module slot.  
2. Check that the fastening screws at the module sides are free to move. 
3. Insert the module in its chassis slot and slide it in as far as possible. 
4. Secure the module by tightening its two fastening screws. 
5. The module starts operating as soon as it is plugged into an operating enclosure. At this stage, 
ignore the alarm indications. 
Connecting to Remote Equipment 
Connecting Serial Equipment 
See Error! Reference source not found. in VS (VS-12, VS-6/BIN and VS-6/C37) section. 
Connecting E&M Equipment 
The VS-6/E&M, VS-8/E&M and FXS/E&M module interface is terminated in four/eight RJ-45 connectors – 
one per channel.  
The following table lists the wiring of the RJ-45 connectors used for the E&M modules. 
RJ-45 Connector Wiring 
Pin 
Designation 
Function 
1 
SB 
Signaling battery 
2 
M 
M lead input 
3 
R1-OUT 
Voice output (4W) 
Voice input/output (2W) 
4 
R-IN 
Voice input (4W) 
5 
T-IN 
Voice input (4W) 
6 
T1-OUT 
Voice output (4W) 
Voice input/output (2W) 
13. Versatile I/O Modules 
Pin 
Designation 
Function 
7 
SG 
Function depends on signaling mode: 
RS-464 Type I, III: Direct connection to signal ground 
RS-464 Type V, SSDC5: Connection to signal ground through 1.2 kΩ 
resistor 
RS-464 Type II: SG lead 
8 
E 
E lead output 
Connecting FXS and FXO Equipment  
The VS-6/FXS, VS-6/FXO and FXS/E&M module interface is terminated in four RJ-12 connectors – one per 
two channels.  
The following table lists the wiring of the RJ-12 connectors used for the VS-6/FXS, VS-6/FXO and FXS/E&M 
modules. 
RJ-12 Connector Wiring 
Pin 
Function 
1 
Not connected 
2 
Tip2 (for 5-8 channel) 
3 
Ring1 (for 1-4 channel) 
4 
Tip1 (for 1-4 channel) 
5 
Ring2 (for 5-8 channel) 
6 
Not connected 
To split each of the four RJ-12 connectors into two RJ-12 connectors intended for the end-user equipment, 
a CBL-VS-VOICE adaptor cable can be ordered from RAD. 
The following figure shows a general view of CBL-VS-VOICE and the following table lists the wiring of the 
CBL-VS-VOICE cable.  
13. Versatile I/O Modules 
 
CBL-VS-VOICE, General View 
CBL-VS-VOICE Cable Wiring 
Function 
C 
A 
B 
Tip2  
2 
 
4 
Ring1  
3 
3 
 
Tip1  
4 
4 
 
Ring2 
5 
 
3 
 
Using Ferrite Cores in Harsh Environment 
In harsh environments, such as heavy industry or electrical switching stations, it is recommended to use 
ferrite cores in order to reduce the effect of electromagnetic interference.  
The recommended ferrite core depends on the connector cable type. 
• 
For modules with RJ-12 connectors, use FAIR RITE catalog number 0443167251 or equivalent for 
small-diameter cables. The ferrite core must be installed on the cable close to the RJ-12 connector 
as shown below: 
13. Versatile I/O Modules 
 
 To install the ferrite core on VS-6/FXS, VS-6/FXO or FXS/E&M modules: 
1. Run the cable through the open core. 
2. If cable thickness allows, wrap it around the core and run it through again. 
Allow no more than 2 inches (5 cm) between the core and the cable connector to the unit. 
3. Snap the core shut. 
4. Connect the cables into the appropriate connectors. 
Connecting the Signaling and Feed Voltage Source 
The subscriber feed voltage used by FXS modules, or the -48 VDC signaling battery voltage used by 
E&M/EXT modules for full compliance with the EIA RS-464 Type II, III and V (BT SSDC5) signaling standards 
is supplied to the VS voice module from the chassis DC power distribution bus. 
The required -48 VDC voltage is always available when the Megaplex chassis is powered from a -48 VDC 
source. An AC-powered or Megaplex-4 chassis can be to an external ringer unit.  
 
Caution 
Since an external voltage source can supply voltage even when the 
Megaplex is not operating, observe the following precautions: 
• 
Always turn off the external source, before the Megaplex chassis is 
turned off. 
• 
Never connect external DC voltages to modules installed in a Megaplex 
chassis if it is not operating. 
• 
Do not connect/disconnect the ringer while it is operating.  
13. Versatile I/O Modules 
Normal Indications 
The module starts operating as soon as it is plugged into an operating Megaplex enclosure. During normal 
operation, the indicators of each channel indicate the channel activity:  
• 
For E&M channels, the E and M indicators indicate the activity on the signaling leads of the 
corresponding channel 
• 
For FXO channels, the RING/REM indicator lights steadily in green when ringing is received from 
the local switch or PBX on the corresponding channel, and the RING/REM indicator lights steadily in 
yellow indicator lights when the remote subscriber is in the off-hook state.  
• 
For FXS channels, the LOC/REM indicator lights steadily in yellow when a call initiated by the 
subscriber is being handled by the corresponding channel, and the LOC/REM indicator lights 
steadily in green when the local subscriber is in the off-hook state. When the LOC/REM indicator 
lights blink in green and yellow, the local and remote subscribers are in the conversation state. 
Configuration Considerations 
General Module Parameters 
Each VS voice port can be independently configured in accordance with the system requirements. 
However, e-m-type value must be the same for each group of E&M module ports (1,2,3,4 or 5,6,7,8).  
In addition, for each pair of FXS ports, once one of the ports is configured with a ring-voltage value of 
'high', the other port must be set to shutdown. 
Selection of Transmit and Receive Levels  
Transmit Level (tx-gain) selects the nominal input level of the transmit path. The input level can be set in 
0.5 dB steps in the range defined by the Transmit and Receive Levels for Various Interfaces table.  
Select the transmit level to match the transmission level point (TLP-transmit) of the equipment connected 
to the channel. The figure below explains how to determine the required level setting. 
Note that the application of an input signal at the nominal transmit level results in a 0 dBm digital level, 
and a far-end output signal equal to the far-end nominal receive level. 
Receive Level (rx-sensitivity) selects the nominal output level of the receive path. The output level can be 
set in 0.5 dB steps in the range defined by the Transmit and Receive Levels for Various Interfaces table. 
Select the receive level to match the TLP-receive of the equipment connected to the channel (see below). 
13. Versatile I/O Modules 
 
Selection of Transmit and Receive Levels 
Handling of Signaling Information  
The VS voice modules automatically adapt the generation and interpretation of the signaling information to 
their analog interface type (E&M, FXS or FXO) and to the signaling mode selected by the user (loop-start or 
wink-start).  
The following sections describe the handling of the signaling information in VS voice modules. 
Signaling Methods 
You can select the format of the signaling information generated by VS voice modules in accordance with 
the application requirements. 
The signaling information of each channel is carried by means of up to four bits (signaling bits), designated 
by the applicable standards as bits A, B, C, and D. The number of bits actually available for carrying 
signaling information, and the data rate at which signaling information can be transferred, depend on the 
main link, the framing mode and the PCM encoding type being used:  
• 
For E1 trunks with G.732N framing, no signaling information is transmitted. 
• 
For E1 trunks with G.732S framing, which use a 16-frame multiframe structure, the standard 
signaling method is Channel Associated Signaling (CAS). In the PCM mode, timeslot 16 carries four 
signaling bits for each payload timeslot.  
13. Versatile I/O Modules 
• 
For T1 trunks with ESF framing, which use a 24-frame multiframe structure, the standard signaling 
method is inband Robbed Bit Multiframe (RBMF) signaling. The ESF multiframe structure includes 
four signaling bits for each payload timeslot. When this method is used, the least significant bit of 
each channel is periodically overwritten with signaling information.  
• 
T1 trunks with SF (D4) framing, which use a 12-frame multiframe structure, also use the RBMF 
signaling method. Because of the shorter multiframe structure, in this case only two signaling bits 
(A and B) are available for each payload timeslot.  
• 
RAD Proprietary “Robbed Bit Frame” (RBF) signaling, applicable for both E1 and T1 trunks, avoids 
the need for multiframe synchronization. This method allocates the least significant bit of each 
channel to its own signaling information. Therefore, signaling is transparently transferred within 
the timeslot carrying the encoded audio signal, but because PCM encoding is effectively done with 
7-bit resolution, there is a slight decrease in transmission quality. This proprietary method allows 
the transmission of 31 voice channels by a Megaplex system with E1 links, when using G.732N 
framing. 
For applications which do not require end-to-end signaling, or can use only inband signaling (e.g., DTMF), 
the user can disable the transfer of signaling information. 
For your convenience, the following table lists the number of signaling bits as a function of voice encoding 
and framing method.  
Number of Available Signaling Bits  
Signaling Type 
G.732S 
G.732N 
ESF 
SF (D4) 
CAS 
4 
Not supported 
Not supported 
Not supported 
Robbed Bit 
Multiframe (RBMF) 
Not supported 
Not supported 
4 
2 
Robbed Bit Frame 
(RBF) 
1 
1 
1 
1 
Signaling Information  
The signaling information exchanged by the channels of VS voice modules is used for the following 
purposes: 
• 
Determine the state of the E and M leads 
• 
Report the detection of on-hook/off-hook conditions, and control DC closure across the line 
• 
Report the detection of ringing and control the sending of ringing 
• 
Control the generation and detection of feed voltage polarity reversal  
13. Versatile I/O Modules 
Each type of VS voice module generates and interprets signaling information in accordance with the analog 
interface type (E&M, FXS or FXO) and to the signaling mode selected by the user (loop-start or wink-start) 
and the defined analog signaling profile.  
The format of the signaling information generated by a VS voice module operating in the PCM mode, which 
depends on the analog interface type (E&M, FXS or FXO), the signaling mode (loop-start or wink-start) and 
the analog signaling profile. 
Note 
In most applications, the user need not be concerned with the issue of 
signaling information.  
Analog Signaling Profiles 
The additional flexibility needed to meet the requirements of special applications is provided by means of 
analog signaling profiles, which control the processing of signaling information received and transmitted by 
each uplink. The analog signaling profile enables the user to select the translation of each individual 
signaling bit. For more information on configuring analog signaling profiles, see Analog Signaling Profiles in 
Chapter 5.  
Signaling Feedback 
Certain types of PBX and central office switches require confirmation that the signaling information has 
been received, a function referred to as signaling-feedback in the Megaplex CLI. Signaling feedback can be 
enabled only for FXO modules.  
Configuring the PW IP Scheme  
When configuring the PW IP Scheme in VS modules, two options are available: 
• 
Option 1:  
 
Each PW card is assigned to a dedicated Router interface (dedicated subnet) 
 
Each PW card is configured over a different L2 broadcast domain (VLAN or Bridge/VLAN) 
• 
Option 2:  
 
Each PW card is configured with a dedicated IP address 
 
All PW cards IP addresses share the same IP subnet 
 
All PW cards share the same L2 Broadcast domain (configured over a Bridge/VLAN) 
Configuration concepts for these options are illustrated in the following figures. 
13. Versatile I/O Modules 
 
Option 1 without the Bridge – Traffic Flow 
 
 
Option 1 with the Bridge – Traffic Flow 
13. Versatile I/O Modules 
 
Option 2 – Logical Diagram 
  
Option 2 – Forwarding Diagram 
Choose Option 2 if you want a single VLAN (broadcast domain) and same subnet for all PW cards. A typical 
use case for this option is configuring PW over ERP (G.8032 Ring). 
 To configure Option 2: 
1. Configure each module with a loopback address in the same subnet: 
13. Versatile I/O Modules 
configure slot 1 
card-type versatile vs-6-fxs 
bind loopback-address 10.10.10.21 
exit 
configure slot 2 
card-type versatile vs-6-fxs 
bind loopback-address 10.10.10.22 
exit 
2. Configure a single router interface so that LB addresses of all configured modules are in the subnet 
of this router interface 
3. Connect (using SVI and flows, connect this router interface to a Bridge port residing over a 
Bridge/VLAN. 
Note: The PW peer IP must be in the subnet of the relevant Router Interface. 
Configuration Sequence  
The list of tasks that can be performed on the VS voice modules and the recommended configuration 
sequence are described in the table below. The second column indicates the configuration context for this 
task, under which it can be found in Chapter 5. The third column refers to the reference tables that should 
be consulted when planning the module operation.  
Task 
Configuration Context 
Comments and Reference  
Configure a VS voice module and 
put it into service 
configure>slot>card-type  
 
VS-6/FXS: card-type=versatile  vs-6-fxs 
VS-6/FXO: card-type=versatile  vs-6-fxo 
VS-6/E&M: card-type=versatile  vs-6-em 
VS-8/E&M: card-type=versatile  vs-8em 
VS-6/FXS/PW: card-type=versatile  vs-6-fxs-pw 
VS-6/FXO/PW: card-type=versatile  vs-6-fxo-pw 
VS-6/E&M/PW: card-type=versatile  vs-6-em-pw 
VS-8/E&M/PW: card-type=versatile  vs-8em-pw 
FXS/E&M: card-type=versatile  vs-fxs-em 
VS-OCU/E&M: card-type=versatile  vs-ocu-em 
Configure the voice port 
parameters  
configure>port>voice 
Voice Ports in Chapter 5 
Configure the serial port 
parameters  
configure>port>serial 
Serial Ports in Chapter 5 
13. Versatile I/O Modules 
Task 
Configuration Context 
Comments and Reference  
Note: You must also configure the CL.2 or uplink module port parameters (depending on the VS module 
application). For the uplink module configuration procedure, refer to the appropriate chapter of this manual.  
Configuring pseudowire 
services  
 
 
Adding pseudowire peers  
configure>pwe>pw>peer 
Peer in Chapter 8 
Configuring the PW peer 
parameters 
configure>peer 
Peer in Chapter 8 
Configuring the pseudowires  
configure>pwe>pw 
Pseudowires in Chapter 8 
Configuring the internal DS1 
ports  
configure>port>ds1  
DS1 Ports in Chapter 5 
Assigning a VS PW module 
with a dedicated IP address to 
support a single VLAN 
(broadcast domain) and same 
subnet for all PW modules  
configure>slot 
 
Configuring the PW IP Scheme in in the 
section above 
Configuring router 
 
 
Configuring SVI port 
configure>port>svi 
SVI (Switched Virtual Interface) Ports in 
Chapter 5 
Routing parameters for the 
Megaplex-4 PW router 
(interfaces, associated static 
routes, default gateway) 
configure>router (2) 
Pseudowire Router in Chapter 8 
Configuring flows 
 
 
Configuring ingress and egress 
flows between the SVI port 
(bound to Router 2 interface) 
and Logical MAC port or 
Ethernet port  
configure>flows 
 
Flows in Chapter 8 
Configuring cross-connect  
 
 
13. Versatile I/O Modules 
Task 
Configuration Context 
Comments and Reference  
Configuring DS0 cross-
connect between the 
voice/DS1 port or the module 
and timeslots on the 
E1/T1/DS1/DS1-opt ports of 
the uplink module) 
configure>cr>ds0 
DS0 Cross-Connect in Chapter 8 
 
Configuring DS0 cross-
connect between the 
timeslots of voice and DS1 
ports of the same module 
configure>cr>ds0 
DS0 Cross-Connect in Chapter 8 
 
Cross-connecting the DS1 port 
with a vc12-vt2/vc11-vt1.5 
from an SDH/SONET port  
configure>cr>sdh-sonet   
 
SDH/SONET Cross-Connect in Chapter 8 
Establishing cross-connection 
between the pseudowire and 
timeslots on the ds1 or serial 
port (of the VS voice module) 
configure>cr>pw-tdm  
 
PW-TDM Cross-Connect in Chapter 8 
 
Configuring protection 
 
 
Configuring protection for 
internal DS1 ports 
configure>protection>tdm-group 
TDM Group Protection in Chapter 7 
 
Configuring protection for 
PWs 
configure>protection>pw 
PW Protection in Chapter 7 
Configuring protection for 
individual timeslots on 
various uplink modules  
configure>protection>ds0-group 
DS0 SNCP Protection in Chapter 7 
Diagnostics  
Serial Ports 
VS diagnostic capabilities include local and remote digital loopbacks on each serial port (see Serial Ports in 
Chapter 5).  
13. Versatile I/O Modules 
In addition to local and remote loopbacks supported by regular serial ports, OCU-DP DDS ports of the VS-
OCU/E&M module also support remote (remote-on-remote) loopback on external unit (CSU loopback).  
Voice Ports 
The test and diagnostics functions available on each VS voice module channel are: 
• 
Local digital loopback  
• 
Remote digital loopback  
• 
Forward tone injection 
• 
Backward tone injection. 
For more detail, see Voice Ports in Chapter 5. 
DS1 Ports  
DS1 diagnostic capabilities include local and remote loopbacks on each DS1 port (per timeslot) (see DS1 
Ports in Chapter 5). In addition, VS voice modules with enhanced PW capabilities (VS-6/FXS/PW, VS-
6/FXO/PW and VS-6/E&M/PW) supports feature local and remote loopbacks per entire DS1 port.  
Monitoring  
The monitoring tasks supported on each local VS voice port level are listed in the table below. 
Level 
Monitored Feature 
Path  
Reference 
Serial ports  
Status data  
configure>port> 
serial  
Serial Ports in Chapter 5 
 
Statistics (3-bit transitional, 
HCM, R.111 encapsulation 
modes) 
configure>port> 
serial 
Serial Ports in Chapter 5 
 
DS1 ports 
Status data for the DS1 port 
 
configure>port>ds1 
DS1 Ports in Chapter 5  
Voice ports 
Status data for the voice 
port 
configure>port>voice 
Voice Ports in Chapter 5  
PW ports  
Transmission performance 
statistics  
configure>port>pw 
Displaying PW Statistics 
in Chapter 8  
13. Versatile I/O Modules 
Level 
Monitored Feature 
Path  
Reference 
 
Status data  
configure>port>pw  
Viewing the Pseudowire 
Status in Chapter 8  
Protection status  
configure> 
protection>pw 
PW Protection in 
Chapter 7  
Troubleshooting  
Serial Ports  
Refer to Error! Reference source not found. in VS (VS-12, VS-6/BIN and VS-6/C37) section.  
Voice Ports 
The test tone injection functions and the loopbacks available on the VS voice module provide a rapid and 
efficient way to identify the general location of a fault in either of the two VS voice modules connected in a 
link, in the external equipment, or in the connections to the channels.  
If a complaint is received from one of the subscribers connected to the VS voice channels, first activate the 
VS voice local test loop at the side where the complaint comes from. The local subscriber must receive its 
own signal. 
If the signal is not received, the problem is at the local end: 
• 
Check the connections to the subscriber equipment. 
• 
Replace the local VS voice module. 
If the local subscriber receives its own signal when the local loop is activated, activate test tone injection 
toward the complaining subscriber. If the subscriber receives the test tone, the problem is probably in the 
connections at the remote side (the side that sends the tone). You can check the computer path of the 
remote module channel by activating the remote loopback and the tone injection toward the remote 
subscriber, and checking that the local subscriber receives the test tone. 
If the problem is not corrected, the procedure must be repeated at the other side of the link. Deactivate 
the local loop and activate the remote loop on the remote Megaplex unit. 

## 13.4 VS–6/E1T1 and VS-16E1T1-PW Modules  *(p.1038)*

13. Versatile I/O Modules 
13.4 VS–6/E1T1 and VS-16E1T1-PW Modules  
This section describes the technical characteristics, applications, installation and operation of the VS-
6/E1T1 and VS-16E1T1-PW E1/T1 interface modules for use in the Megaplex-4 Next Generation 
Multiservice Access Node, ver 4.7 and higher.  
Product Options 
Serial/E1/T1 Combinations  
Versatile E1/T1 modules are available in the following versions:  
• 
VS-16E1T1-PW consists of two identical submodules each featuring a TDM interface with 8 E1/T1 
links for connecting to E1/T1 ports. 
• 
VS-6/E1T1 module consists of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels   
 
Lower: TDM interface submodule with 8 E1/T1 links for connecting to E1/T1 ports. 
Note 
VS-16E1T1-EoP, another versatile module with E1/T1 links, is described in a 
separate section.  
Applications  
The following figure shows a typical basic application for a Megaplex-4 equipped with VS-6/E1T1 modules.  
 
GbE
Megaplex-4100
GbE
Megaplex-4100
PSN
E1/T1
LS/HS
E1/T1
LS/HS
 
Basic application using GbE Ports  
13. Versatile I/O Modules 
Features  
VS-6/E1T1 Module 
The module architecture and data flow for VS-6/E1T1 modules with serial submodules are shown below. 
The following table lists the module entities (ports) and their hierarchy.  
E1/T1 
1..8
32 x E1
GbE
CL.2 
Ethernet 
CL.2 TDM
16 x E1
6 x E1
DS1
1..16
16 x E1
PW 1..64
Switch
Serial
1..6
DS0
 
VS-6/E1T1 Module Architecture Entities and their Hierarchy  
Name 
Number of Ports  
Possible Values 
Serial 
6 
slot/1… slot/6 
E1/T1 
8 
slot/1… slot/8 
DS1 
16 
slot/1… slot/16 
PW 
64 
slot/1… slot/64 
VS-16E1T1-PW Module 
The module architecture and data flow for VS-16E1T1-PW modules are shown in the figure below. The 
table below lists the module entities (ports) and their hierarchy.  
13. Versatile I/O Modules 
DS0
PW 1..128
E1/T1 
1..16
DS1
1..16
32 x E1
GbE
CL.2 
Ethernet 
CL.2 TDM
Switch
 
VS-16E1T1-PW Module Architecture Entities and their Hierarchy  
Name 
Number of Ports  
Possible Values 
e1/t1 
16 
slot/1… slot/16 
ds1 
16 
slot/1… slot/16 
pw 
128 
slot/1… slot/128 
E1/T1 Services  
The E1 interface is compatible with all carrier-provided E1 services, meeting the requirements of ITU-T Rec. 
G.703, G.704 and G.732. It supports both 2 (G.732N) and 16 (G.732S) frames per multiframe formats, as 
well as unframed mode. It also supports CRC-4 and E bit, in compliance with G.704 recommendations. Zero 
suppression over the line is HDB3.  
The T1 interface is compatible with ANSI requirements. Both D4 and ESF framing formats are supported. 
Zero suppression is selectable for Transparent, B7ZS, or B8ZS.  
Internal TDM flows are handled by an internal DS0 cross-connect matrix. The matrix supports flexible 
payload routing, independently configurable for each port, at the individual timeslots (DS0) level. This 
enables routing individually selected timeslots (including timeslots with split assignment) to other modules 
13. Versatile I/O Modules 
installed in the Megaplex-4 chassis, via the internal TDM buses. Timeslots can be routed to any port with 
compatible properties. The signaling information associated with voice timeslots can be translated by 
means of user-specified signaling profiles.  
The E1/T1 ports can also be connected to SDH/SONET links, which permits using the Megaplex-4 as an 
SDH/SONET terminal multiplexer (TM). Using the Megaplex-4 as an add/drop multiplexer (ADM), in either 
linear chain or ring topologies, enables dropping part of the SDH/SONET link payload at a certain location, 
and possibly inserting other payload. 
Timing  
Receive timing. VS-16E1T1-PW and VS-6/E1T1 modules recover the timing of each received E1/T1 stream 
or PW, and therefore can also provide timing reference signals derived from a selected E1/T1/PW for the 
Megaplex-4 system timing domain.  
Transmit timing. The timing reference source used by the port for the transmit-to-network direction can 
be selected as follows: 
• 
loopback – Clock received from the E1/T1 port 
• 
through-timing –Clock received from PW (ACR) or VC-12/VT1.5 (depending of the transport network)  
• 
domain – Clock provided by system clock domain. 
• 
Adaptive clock recovery (ACR).  VS-16E1T1-PW and VS-6/E1T1 modules have independent 
adaptive clock recovery mechanisms for each pseudowire, which recover the original timing (clock 
rate) of the far-end source of each pseudowire. The clock recovery mechanisms can provide 
recovered clock signals to serve as timing references for the Megaplex-4 system and the relevant 
(cross-connected) E1/T1 links.  
Cross-Connections  
The VS modules feature DS0, TDM and PW-TDM cross-connections, which can be used according to the 
module application as shown in the table below. For description of DS0, TDM and PW-TDM cross-connect 
functionalities, see respective sections Chapter 8. 
13. Versatile I/O Modules 
Cross-Connect Type 
Diagram 
DS0 cross-connect between the 
serial/E1/T1 port of the module and 
timeslots on the E1/T1/DS1 ports of 
the uplink module. 
1  
serial/e1/t1
cross connect 
dso
e1/t1/ds1
serial/e1/t1
 
 
TDM cross-connect: a full payload 
E1/T1 port is cross-connected 
via tdm cross-connect only 
with another full payload 
E1/T1 port on an I/O module 
supporting transparent 
mapping 
2  
e1/t1
cross connect d 
tdm
e1/t1
e1/t1
 
 
PW-TDM cross-connect: 
serial/e1/t1 port of the VS 
module is cross-connected 
directly to PW. This type allows 
low-latency transmission of TDM 
services over packet-switched 
networks and used when a single 
channel is carried over dedicated 
PW. 
3 
pw
1/1
flow
ETH
peer
cross connect 
pw-tdm
1:1
serial/e1/t1
RI
PW 
Static 
Router
Serial ports are cross-connected 
to DS1 ports inside the module 
(DS0 cross-connect); DS1 ports 
are cross-connected to PW 
(PW-TDM cross-connect). This 
type is used when multiple I/O 
channels are sharing the same 
PW.  
4 
PW 
Static 
Router
serial
pw
1/1
cross connect 
dso
flow
RI
ETH
peer
ds1
1/1
1:1
cross connect 
pw-tdm
serial
 
13. Versatile I/O Modules 
Cross-Connect Type 
Diagram 
Any Megaplex-4 service port is 
cross-connected to the DS1 port 
of the VS module (DS0 cross-
connect); DS1 ports are 
cross-connected to PW (PW-TDM 
cross-connect). In this application 
the VS module is used as a server 
for other modules not equipped 
with PW.  
5 
PW 
Static 
Router
Any port
pw
1/1
cross connect 
dso
flow
RI
ETH
peer
ds1
1/1
1:1
cross connect 
pw-tdm
Any port
Any Megaplex-4  
module
VS module
 
 
DS0 Cross-Connect  
The DS0 cross-connect matrix of the Megaplex-4 chassis enables flexible payload routing in the VS  
modules, independently configurable for each port, at the individual timeslots (DS0) level. This routing is 
configured via ds0 cross-connect command as follows: 
• 
Serial submodule: between the serial ports and timeslots on the E1/T1/DS1 ports of the uplink 
module.  
In addition to the normal full-duplex (bidirectional) mode, VS serial ports feature additional 
transmission modes, which enable point-to-multipoint communication: 
 
Unidirectional (simplex) transmission, where each channel can be configured either to receive 
(unidirectional RX) or transmit (unidirectional TX). 
 
Bidirectional broadcast (half-duplex) communication, suitable for polled applications. In this 
mode, a channel can not only receive, but can also transmit (not both simultaneously).  
 
This feature is available for VS modules configured to 3-bit-transitional (and operating at 64 
kbps) or R.111 mode.  
 
For configuration considerations, see Error! Reference source not found. below. 
VS modules operating in V.110 mode also support split timeslot allocation. 
• 
TDM submodule: between the E1/T1 ports and timeslots on the E1/T1/DS1 ports of the uplink 
module.  
TDM Cross-Connect 
In Diagram 2, a full payload E1/T1 port can be cross-connected via tdm cross-connect only with another full 
payload E1/T1 port on an I/O module supporting transparent mapping.  
13. Versatile I/O Modules 
PW-TDM Cross-Connect  
PW-TDM cross-connections are used to transport TDM services over PSN networks. The table above shows 
diagrams of PW-TDM cross-connect configurations depending on the module application (see Diagram 3 
and Diagram 4). 
In Diagram 3, serial/e1/t1 port is cross-connected directly to PW. This type allows low-latency transmission 
of TDM services over packet-switched networks and used when a single channel is carried over dedicated 
PW.  
In Diagram 4, serial ports are cross-connected to DS1 ports inside the module (DS0 cross-connect); DS1 
ports are cross-connected to PW (PW-TDM cross-connect). This type is used when multiple I/O channels 
are sharing the same PW. 
Diagram 5 shows a VS module operating as a PW server for other modules not equipped with PW. 
E1/T1/DS1/serial ports of these modules are cross-connected to DS1 ports inside the VS module (DS0 
cross-connect); DS1 ports are cross-connected to PW (PW-TDM cross-connect).  
Mapping of E1/T1 Links over SDH/SONET  
The E1/T1 ports can also be connected to SDH/SONET links, which permits using the Megaplex-4 as an 
SDH/SONET terminal multiplexer (TM). Using the Megaplex-4 as an add/drop multiplexer (ADM), in either 
linear chain or ring topologies, enables dropping part of the SDH/SONET link payload at a certain location, 
and possibly inserting other payload. 
When VS-6/E1T1 and VS-16E1T1-PW modules are working with CL modules that have SDH/SONET ports, it 
allows direct transparent mapping of unframed E1/T1 links over SDH/SONET; this feature is also called 
“transparent clocking”. Framed payload can be mapped to SDH/SONET links in two stages: first via DS0 
cross-connect to E1-i/T1-i ports of CL.2 modules and then to SDH/SONET containers.  
Pseudowire Services  
VS-16E1T1-PW and VS-6/E1T1 modules provide TDM pseudowire access gateway services over 
packet-switched networks (Ethernet and IP) for TDM traffic (E1, T1, high-speed and low-speed data, voice) 
received via the Megaplex-4 TDM buses from other modules. This is done via independently-configurable 
internal DS1 ports available in the module. The number of DS1 ports is 16 for either VS-6/E1T1 or VS-
16E1T1-PW module.  
In addition, the module provides direct PW access to its E1/T1 or serial ports. The number of PW ports is 64 
per VS-6/E1T1 and 128 per VS-16E1T1-PW module.  
13. Versatile I/O Modules 
Both modules provide pseudowire emulation services over packet-switched networks using the CESoPSN 
(structure-aware TDM circuit emulation over PSN) protocols in accordance with RFC5086 and SAToPSN 
(structure-agnostic TDM over PSN) in accordance with RFC4553. 
The pseudowire services enable converting TDM payload to packets and transferring these packets through 
router interfaces defined in the Megaplex-4.   
Packet structure is independently selectable for each pseudowire, for compatibility with the various 
pseudowire protocols (CESoPSN, SAToPSN) and the PSN type (UDP/IP or MPLS/ETH). For maximum 
flexibility in system applications, the framing format of the pseudowire device at the destination (referred 
to as a pseudowire peer) can also be taken into account. Thus, in many cases traffic using the E1 standards 
can be directed at destinations using the T1 standards, and vice versa. 
The pseudowire exit port toward the PSN is also selectable, via any Ethernet port (GbE or VCG) of any 
module installed in the chassis. The selectable exit ports are bound (via SVI ports) to router interfaces, 
where each router interface has its own IP source address and, optionally, its own VLAN. Each VS 
submodule supports up to 12 interfaces, CL.2 modules support unlimited number of interfaces. However, 
the maximum number of router interfaces per Megaplex-4 is 100. The user can also specify static routes to 
control the IP routing.  
The PW engine in one of the VS modules can be used as a server for traffic from other modules cross-
connected via its DS1 ports.  
• 
VS-16E1T1-PW and VS-6/E1T1 modules have independent adaptive clock recovery (ACR) 
mechanisms for each pseudowire, which recover the original timing (clock rate) of the far-end 
source of each pseudowire, according to ITU G.8261, G.823, G.824 and MEF 22 recommendations. 
The clock recovery mechanisms can provide recovered clock signals to serve as timing references 
for the Megaplex-4 system.  
Inband Management 
• 
VS-6/E1T1 and VS-16E1T1-PW modules supports the transfer of management traffic, inband. A 
dedicated management timeslot can be configured on each E1/T1 port operating in a framed 
mode. This enables extending the management connections to other RAD equipment using inband 
management over dedicate timeslots. 
Protection  
The VS module features the following types of protection: 
• 
TDM group protection between DS1 ports or E1/T1 ports of the VS module and DS1/E1/T1/E1-i/T1-
i ports of other Megaplex-4 modules (see TDM Group Protection in Chapter 7) 
13. Versatile I/O Modules 
• 
Direct PW protection between two PW ports of the VS module (see PW Protection in Chapter 7)  
TDM Group Protection  
When pseudowires are configured on redundant internal DS1 ports, the pseudowire traffic is automatically 
protected as well. The protection mode is 1+1, meaning that the traffic is also sent on the protection DS1 
port.  
The figure below illustrates the DS1 TDM group protection. For each protection group, you must first 
configure the internal DS1 port that will serve as the working port; this configuration is copied to the other 
port of the group. In addition, it is necessary to configure pseudowires from each internal DS1 port in the 
protection group to the desired destinations.  
 
GbE
CL-A/1
GbE
CL-B/1
I/O 
Tributary 
Port
DS1 #1
Working
PW #1
PW #2
SVI #1
SVI #2
DS1 #2
Protection 
TDM Group
 
TDM Group Protection for DS1 Ports  
PW Protection  
For PW protection, two PW ports on the same module are connected to the same DS1 port. A typical 
configuration is shown in the figure below.  
GbE
CL-A/1
GbE
CL-B/1
I/O 
Tributary 
Port
DS1
PW #1
Working 
PW #2
Protection
SVI #1
SVI #2
 
13. Versatile I/O Modules 
PW Protection  
During normal operation, both PW ports process as usual the transmit and receive signals, but the receive 
output of the protection port is disconnected. The operational state of the protection port is continuously 
monitored to ensure that it is operating properly. If the working link fails, the corresponding port is 
disconnected, and the protection port takes over.  
For two ports configured to PW protection, the following parameters must be the same for both ports: 
• 
tdm-oos  
• 
tdm-payload. 
Physical Description  
The VS module occupies one I/O slot in the Megaplex-4 chassis. The module is based on a main board and 
two factory-replaceable submodules.  
 
VS-16E1T1-PW consists of two identical submodules, each featuring a TDM interface with 8 E1/T1 links for 
connecting to all the E1/T1 ports. The panel is shown below. 
Interface 
Module 1
Interface 
Module 2
Main Board
13. Versatile I/O Modules 
 
VS-16E1T1-PW Module Panel 
• 
VS-6/E1T1 module consists of the following submodules:  
 
Upper: serial interface submodule with 6 sync/async channels  
 
Lower: TDM interface submodule with 8 E1/T1 links for connecting to E1/T1 ports.  
VS-6/E1T1 module panels are shown below. 
13. Versatile I/O Modules 
 
VS-6/E1T1-PW Module Panel 
 
VS-6/E1T1 Module Panels  
The upper submodule panel includes the following interface sections: 
• 
For VS-6/E1T1: the serial interfacing section consisting of two 68-pin SCSI-4 female connectors, 
each containing three channels. 
• 
For VS-16E1T1-PW: the TDM interfacing section including one 44-pin D-type female connector, for 
connecting to all the E1/T1 ports. 
13. Versatile I/O Modules 
The lower submodule panel includes the TDM interfacing section consisting of one 44-pin D-type female 
connector, each containing 8 E1/T1 links for connecting to all the E1/T1 ports. 
LED Indicators 
E1/T1 Indicators 
Each port status indicator operates as follows: 
• 
Lights steadily in green when the corresponding port is operating properly and is active (that is, it is 
connected, and serves as the working port when included in a protection group). 
• 
Flashes in green when the corresponding port is operating properly, and serves as the protection 
port when TDM group protection is enabled. 
• 
Lights in red when the corresponding port detects loss of synchronization, loss of signal or a red 
alarm 
• 
Flashes in red when the corresponding port is serving as the protection port and detects loss of 
synchronization  
• 
Off when the corresponding port is not connected. 
Technical Specifications 
For the corresponding technical specifications of serial interface submodule, refer to VS (VS-12, VS-6/BIN 
and VS-6/C37) section in this chapter.   
E1 Interface 
Type and Bit Rate 
E1, 2.048 Mbps (per link) 
Number of Links 
VS-6/E1T1: 8  
 
VS-16E1T1-PW: 16  
Line Interface 
• 4-wire, 120Ω balanced 
• Coax, 75Ω unbalanced 
Line Code 
HDB3 
Compliance 
ITU-T Rec. G.703, G704, G.732 (including CRC-4 and E bit) 
13. Versatile I/O Modules 
Framing 
• Basic G.704 framing (G732N) with or without CRC-4 
per ITU-T Rec. G.704 
• Timeslot 16 multiframe (G732S), with or without CRC-4 
per ITU-T Rec. G.704 
• No framing (unframed mode) 
Transmit Level 
• ±3V ±10%, balanced 
• ±2.37V ±10%, unbalanced 
 
Receive Level 
Software selectable: 
• 0 through -12 dB for short haul mode 
• 0 through -43 dB for long haul (LTU) mode 
 
Jitter Performance 
Per ITU-T Rec. G.823  
 
Surge Protection 
Per ITU-T Rec. K.21 
 
Connector 
44-pin D-type female for all ports. Adapter (splitter) cables 
available from RAD 
T1 Interface 
Type and Bit Rate 
T1, 1.544 Mbps 
 
Number of Links 
VS-6/E1T1: 8  
 
 
VS-16E1T1-PW: 16  
 
Compliance 
ANSI T1.107, ANSI T1.403  
 
Line Interface 
4-wire, 100Ω balanced 
 
Line Code 
Bipolar AMI 
 
Zero Suppression 
• Transparent (no zero suppression) 
• B7ZS  
• B8ZS 
 
Framing 
• SF (D4)  
• ESF 
 
Transmit Levels 
• 0.6, 1.2, 1.8, 2.4, 3.0 dBm user-adjustable, measured at 
0 to 655 ft 
 
Receive Level 
0 to -12 dBm  
 
Jitter Performance  
Per AT&T TR-62411 
 
Connector   
44-pin D-type female for all ports. Adapter cables available 
from RAD  
13. Versatile I/O Modules 
Indicators 
Status Indicator per Link 
Dual-color indicator: 
• Lights steadily in green when the port is connected and 
carries traffic 
• Flashes in green when the port is connected and is the 
protection port in a TDM protection pair 
• Lights in red during red alarm 
• Flashes in red for a protection port that reports loss of 
synchronization 
• Off when not connected  
Power Consumption VS-16E1T1-PW 
14.5W   
VS-6/E1T1 (UTP connectors) RS-422: 16.1W 
RS-232: 14.5W  
V.35: 15.7W 
Configuration 
 
Programmable via Megaplex-4 management system  
Environment 
Operating Temperature 
-10°C to 55°C  (14°F to 131°F)   
 
Storage Temperature 
-20°C to 70°C  (-4°F to 160°F)   
 
Humidity 
Up to 95%, non-condensing 
Preparing the Modules for Installation 
Note 
Before performing any internal settings, adjustment, maintenance, or repairs, 
first disconnect all the cables from the module, and then remove the module 
from the Megaplex-4 enclosure. 
No internal settings, adjustment, maintenance, and repairs may be performed 
by either the operator or the user; such activities may be performed only by a 
skilled technician who is aware of the hazards involved. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. 
 
Caution 
The modules contain components sensitive to electrostatic discharge (ESD). 
To prevent ESD damage, always hold the module by its sides, and do not 
touch the module components or connectors.  
 
13. Versatile I/O Modules 
Caution 
To prevent physical damage to the electronic components assembled on the 
two sides of the module printed circuit boards (PCB) while it is inserted into 
its chassis slot, support the module while sliding it into position and make 
sure that its components do not touch the chassis structure, nor other 
modules.  
Installing a Module in the Chassis 
 
 
Warning 
The module starts operating as soon as it is inserted in an operating chassis.  
 
 To install a module in the chassis: 
1. Refer to the system installation plan and identify the prescribed module slot. 
2. Check that the fastening screws at the module sides are free to move. 
3. Insert the module in its chassis slot and slide it in as far as possible. 
4. Secure the module by tightening its two fastening screws. 
The module starts operating as soon as it is plugged into an operating enclosure. At this stage, 
ignore the alarm indications. 
Connecting to Remote Equipment 
Connecting Serial Equipment 
See Error! Reference source not found. in VS (VS-12, VS-6/BIN and VS-6/C37) section. 
Connecting the E1/T1 Ports  
The module E1/T1 ports are terminated in a 44-pin D-type female connector. The module connector 
supports both the unbalanced and balanced interfaces. Each type requires a different adapter cable. 
13. Versatile I/O Modules 
RAD offers the following adapter cables:  
• 
CBL-G703-8/RJ45: adapter cable terminated in RJ-45 plugs at the user’s end, for use when VS-
6/E1T1 and VS-16E1T1-PW modules are connected to equipment with balanced E1/T1 interfaces 
using pins 1, 2 for the receive (RX) pair and pins 4,5 for the transmit (TX) pair  
• 
CBL-G703-8/RJ45/X: adapter cable terminated in RJ-45 plugs at the user’s end, for use when VS-
6/E1T1 and VS-16E1T1-PW modules are connected to equipment with balanced E1/T1 interfaces 
using pins 4,5 for the receive (RX) pair and pins 1, 2 for the transmit (TX) pair  
• 
CBL-G703-8/OPEN/2M: adapter cable terminated in free leads at the user’s end, for balanced 
E1/T1 applications 
• 
CBL-G703-8/COAX: adapter cable terminated in BNC connectors at the user’s end, for use when VS-
6/E1T1 and VS-16E1T1-PW modules are connected to equipment with unbalanced E1 interfaces  
The following sections describe these adapter cables, the functions of the 44-pin connector pins for each 
interface type, and connection instructions. 
CBL-G703-8/RJ45 Cable  
The CBL-G703-8/RJ45 is a 2-meter cable for VS-6/E1T1 and VS-16E1T1-PW modules using the balanced 
interface. The cable can be also ordered with 2.5m or 8m length. 
The figure below shows the cable construction. The table below presents the cable wiring and identifies the 
interface connector pin assignment. 
 
 
13. Versatile I/O Modules 
CBL-G703-8/RJ45 Cable Wiring 
Channel 
RJ-45 
Connector  
44-Pin Connector 
RJ-45 
Connector 
Pins 
Channel 
RJ-45 
Connector  
44-Pin Connector 
RJ-45 
Connector 
Pins 
Pin 
Function 
Pin 
Function 
1  
CH-1 
31 
RX Ring 
1 
5 
CH-5 
37 
RX Ring 
1 
17 
RX Tip 
2 
23 
RX Tip 
2 
16 
TX Ring 
4 
22 
TX Ring 
4 
1 
TX Tip 
5 
7 
TX Tip 
5 
2  
CH-2 
33 
RX Ring 
1 
6 
CH-6 
38 
RX Ring 
1 
32 
RX Tip 
2 
39 
RX Tip 
2 
2 
TX Ring 
4 
8 
TX Ring 
4 
3 
TX Tip 
5 
9 
TX Tip 
5 
3  
CH-3 
34 
RX Ring 
1 
7 
CH-7 
40 
RX Ring 
1 
20 
RX Tip 
2 
26 
RX Tip 
2 
19 
TX Ring 
4 
25 
TX Ring 
4 
4 
TX Tip 
5 
10 
TX Tip 
5 
4  
CH-4 
35 
RX Ring 
1 
8 
CH-8 
41 
RX Ring 
1 
36 
RX Tip 
2 
42 
RX Tip 
2 
5 
TX Ring 
4 
11 
TX Ring 
4 
6 
TX Tip 
5 
12 
TX Tip 
5 
CBL-G703-8/RJ45/X Cable  
CBL-G703-8/RJ45/X is a 2-meter cable. The figure below shows the cable construction. The table below 
presents the cable wiring and identifies the interface connector pin assignment. The cable can be also 
ordered with 2.5m length. 
13. Versatile I/O Modules 
CBL- G703-8/RJ45/X
Ch. 1
Ch. 2
Ch. 3
Ch. 4
Ch. 6
Ch. 7
Ch. 8
Ch. 5
 
CBL-G703-8/RJ45/X Cable  
CBL-G703-8/RJ45/X Cable Wiring 
Channel 
RJ-45 
Connector 
44-Pin 
Connector 
RJ-45 
Connector 
Pins 
Channel 
RJ-45 
Connector 
44-Pin 
Connector 
RJ-45 
Connector 
Pins 
Pin 
Function 
Pin 
Function 
1  
CH-1 
31 
RX Ring 
4 
5 
CH-5 
37 
RX Ring 
4 
17 
RX Tip 
5 
23 
RX Tip 
5 
16 
TX Ring 
1 
22 
TX Ring 
1 
1 
TX Tip 
2 
7 
TX Tip 
2 
2  
CH-2 
33 
RX Ring 
4 
6 
CH-6 
38 
RX Ring 
4 
32 
RX Tip 
5 
39 
RX Tip 
5 
2 
TX Ring 
1 
8 
TX Ring 
1 
3 
TX Tip 
2 
9 
TX Tip 
2 
3  
CH-3 
34 
RX Ring 
4 
7 
CH-7 
40 
RX Ring 
4 
20 
RX Tip 
5 
26 
RX Tip 
5 
19 
TX Ring 
1 
25 
TX Ring 
1 
4 
TX Tip 
2 
10 
TX Tip 
2 
4  
CH-4 
35 
RX Ring 
4 
8 
CH-8 
41 
RX Ring 
4 
36 
RX Tip 
5 
42 
RX Tip 
5 
5 
TX Ring 
1 
11 
TX Ring 
1 
6 
TX Tip 
2 
12 
TX Tip 
2 
13. Versatile I/O Modules 
CBL-G703-8/OPEN Cable 
CBL-G703-8/OPEN cable is a 2-meter cable for VS-6/E1T1 and VS-16E1T1-PW modules using the balanced 
E1/T1 interface, terminated in free leads that can be connected to any terminal block or connector 
appropriate for your application. The cable can be also ordered with 8m or 12m length. 
The figure below shows the cable construction. The table below resents the cable wiring and identifies the 
pair functions. 
 
CBL-G703-8/OPEN Cable 
CBL-G703-8/OPEN Cable Wiring  
Channel 
44-Pin Connector 
Pair Color 
Channel 
44-Pin Connector 
Pair Color 
Pin 
Function 
Pin 
Function 
1 
31 
Rx Ring 
White 
5 
37 
Rx Ring 
White 
17 
Rx Tip 
Blue 
23 
Rx Tip 
Brown/Blue 
1 
Tx Tip 
Orange 
7 
Tx Tip 
Grey/Blue 
16 
Tx Ring 
White 
22 
Tx Ring 
White 
2 
33 
Rx Ring 
White 
6 
38 
Rx Ring 
White 
32 
Rx Tip 
Green 
39 
Rx Tip 
White/Orange 
3 
Tx Tip 
Brown 
9 
Tx Tip 
Orange/Green 
2 
Tx Ring 
White 
8 
Tx Ring 
White 
3 
34 
Rx Ring 
White 
7 
40 
Rx Ring 
White 
20 
Rx Tip 
Grey 
26 
Rx Tip 
Orange/Brown 
4 
Tx Tip 
White/Blue 
10 
Tx Tip 
Grey/Orange 
19 
Tx Ring 
White 
25 
Tx Ring 
White 
4 
35 
Rx Ring 
White 
8 
41 
Rx Ring 
White 
36 
Rx Tip 
Orange/Blue 
42 
Rx Tip 
White/Green 
6 
Tx Tip 
Green/Blue 
12 
Tx Tip 
Green/Brown 
5 
Tx Ring 
White 
11 
Tx Ring 
White 
CBL-G703-8/OPEN
13. Versatile I/O Modules 
CBL-G703-8/COAX Cable  
CBL-G703-8/COAX is a 2-meter cable for VS-6/E1T1 and VS-16E1T1-PW modules using the unbalanced E1 
interface.  
 
CBL-G703-8/COAX Cable 
The table below presents the cable wiring and identifies the interface connector pin assignment.  
CBL-G703-8/COAX Cable Wiring 
Channel 
Function 
44-Pin Connector 
BNC Contact 
Channel 
Function  
44-Pin Connector 
BNC Contact 
Pin 
Function 
Pin 
Function 
1  
RX 
31 
Ring 
Shield 
5 
RX 
37 
Ring 
Shield 
29 
Frame Ground 
29 
Frame Ground 
 
17 
Tip 
Center 
23 
Tip 
Center 
TX 
1 
Tip 
Center 
TX 
7 
Tip 
Center 
16 
Ring 
Shield 
22 
Ring 
Shield 
14 
Frame Ground 
14 
Frame Ground 
2  
RX 
33 
Ring 
Shield 
6 
RX 
38 
Ring 
Shield 
44 
Frame Ground 
44 
Frame Ground 
 
32 
Tip 
Center 
39 
Tip 
Center 
TX 
3 
Tip 
Center 
TX 
9 
Tip 
Center 
2 
Ring 
Shield 
8 
Ring 
Shield 
29 
Frame Ground 
14 
Frame Ground 
3  
RX 
34 
Ring 
Shield 
7 
RX 
40 
Ring 
Shield 
29 
Frame Ground 
29 
Frame Ground 
 
13. Versatile I/O Modules 
20 
Tip 
Center 
26 
Tip 
Center 
TX 
4 
Tip 
Center 
TX 
10 
Tip 
Center 
19 
Ring 
Shield 
25 
Ring 
Shield 
14 
Frame Ground 
14 
Frame Ground 
4  
RX 
35 
Ring 
Shield 
8 
RX 
41 
Ring 
Shield 
44 
Frame Ground 
44 
Frame Ground 
 
36 
Tip 
Center 
42 
Tip 
Center 
TX 
6 
Tip 
Center 
TX 
12 
Tip 
Center 
5 
Ring 
Shield 
11 
Ring 
Shield 
29 
Frame Ground 
14 
Frame Ground 
Cable Type Sensing 
15 
Not used 
– 
 
 
 
 
Signal Ground 
30 
Ground 
– 
Frame Ground 
44 
Cable Shield 
– 
Connecting Cables to the E1/T1 Ports  
Using the site installation plan, identify the cable intended for connection to the corresponding VS-6/E1T1 
and VS-16E1T1-PW connector, and connect the cable to the module as explained below. 
 To connect the CBL-G703-8/RJ45 and CBL-G703-8/RJ45/X cables: 
1. Connect the 44-pin connector of the cable to the front panel connector. 
2. Connect the RJ-45 plug of each port interface (the plugs are marked CH-1 to CH-8) to the 
prescribed user equipment or patch panel connector. Insulate unused connectors, to prevent 
accidental short-circuiting of their exposed contacts to metallic surfaces.  
 To connect the CBL-G703-8/COAX cable: 
1. Connect the 44-pin male connector of the cable to the front panel connector. 
2. Connect the BNC plugs of each port interface (the plugs are marked with the number of the port) 
to the prescribed user equipment or patch panel connectors. Pay attention to correct connection: 
 
TX connector: serves as the transmit output of the port  
 
RX connector: serves as the receive input of the port. 
 To connect the CBL-G703-8/OPEN cable: 
1. Connect the free cable ends in accordance with the prescribed termination method. 
13. Versatile I/O Modules 
2. When done, connect the 44-pin male connector of the cable to the front panel connector. 
Normal Indications 
The status of each E1 link is indicated by a separate indicator.  
During normal operation, after communication with the remote equipment is established, the port 
indicators of the VS-6/E1T1 and VS-16E1T1-PW module light steadily in green; however, if a port is 
configured as the protection port in a protection group, its indicator flashes in green. 
If the other communication equipment on the link is not yet operative, the port indicator lights in red. The 
indicator turns green (or flashes in green) as soon as the link with the remote equipment is established.  
The indicators of ports configured at shutdown are off.  
Configuration Considerations 
Configuring an E1/T1 Port or Pseudowires as System Timing Reference  
After an E1/T1 port of VS-16E1T1-PW or VS-6/E1T1 module is configured and at no shutdown, its receive 
clock can be selected as a timing reference for the Megaplex-4 system. 
The allowed range of PW numbers that can serve as clock sources is 1 to 640.  
Configuring the PW IP Scheme  
When configuring the PW IP Scheme in VS modules, two options are available: 
• 
Option 1:  
 
Each PW card is assigned to a dedicated Router interface (dedicated subnet) 
 
Each PW card is configured over a different L2 broadcast domain (VLAN or Bridge/VLAN) 
• 
Option 2:  
 
Each PW card is configured with a dedicated IP address 
 
All PW cards IP addresses share the same IP subnet 
 
All PW cards share the same L2 Broadcast domain (configured over a Bridge/VLAN) 
Configuration concepts for these options are illustrated in the following figures. 
13. Versatile I/O Modules 
 
Option 1 without the Bridge – Traffic Flow 
 
 
Option 1 with the Bridge – Traffic Flow 
13. Versatile I/O Modules 
 
Option 2 – Logical Diagram 
  
Option 2 – Forwarding Diagram 
Choose Option 2 if you want a single VLAN (broadcast domain) and same subnet for all PW cards. A typical 
use case for this option is configuring PW over ERP (G.8032 Ring). 
 To configure Option 2: 
1. Configure each module with a loopback address in the same subnet: 
13. Versatile I/O Modules 
configure slot 1 
card-type versatile vs-e1-pw 
bind loopback-address 10.10.10.21  
exit 
configure slot 2 
card-type versatile vs-e1-pw  
bind loopback-address 10.10.10.22 
exit 
2. Configure a single router interface so that LB addresses of all configured modules are in the subnet 
of this router interface 
3. Connect (using SVI and flows, connect this router interface to a Bridge port residing over a 
Bridge/VLAN. 
Note: The PW peer IP must be in the subnet of the relevant Router Interface. 
Configuration Sequence 
The list of tasks that can be performed on the VS-6/E1T1 and VS-16E1T1-PW modules and the 
recommended configuration sequence are described in the table below. For detailed descriptions, refer to 
Chapter 5. The second column indicates the configuration context for this task, under which it can be found 
in Chapter 5. The third column refers to the reference tables and relevant sections that should be 
consulted when planning the module operation. 
Task 
Configuration Context 
Comments and Reference  
Configure a VS-16E1T1-PW or 
VS-6/E1T1 module and put it 
into service 
configure>slot>card-type  
VS-6/E1: card-type=versatile  vs-6-e1 
VS-6/T1: card-type=versatile  vs-6-t1 
VS-16E1: card-type=versatile  vs-e1-pw 
VS-16T1: card-type=versatile  vs-t1-pw 
Select an E1/T1 port as system 
timing reference  
config>system>clock>domain
(1) 
 
Configure the E1 port 
parameters  
configure>port>e1 
E1 Ports in Chapter 5 
Configure the T1 port 
parameters  
configure>port>t1 
T1 Ports in Chapter 5 
Configure the internal DS1 
ports  
configure>port>ds1  
DS1 Ports in Chapter 5 
13. Versatile I/O Modules 
Task 
Configuration Context 
Comments and Reference  
Configure the serial port 
parameters  
configure>port>serial 
Serial Ports in Chapter 5 
Note: You must also configure the CL.2 or uplink module port parameters (depending on the VS 
module application). For the uplink module configuration procedure, refer to the appropriate chapter 
of this manual.  
Configuring pseudowire 
services  
 
 
Configuring the PW peer 
parameters 
configure>peer 
Peer in Chapter 8 
Adding pseudowire peers  
configure>pwe>pw>peer 
Peer in Chapter 8 
Configuring the pseudowires  
configure>pwe>pw 
Pseudowires in Chapter 8 
Assigning a VS PW module with 
a dedicated IP address to 
support a single VLAN 
(broadcast domain) and same 
subnet for all PW modules  
configure>slot 
 
Configuring the PW IP Scheme in 
in the section above 
Configuring the router 
 
 
Configuring the SVI port 
configure>port>svi 
SVI (Switched Virtual 
Interface) Ports in Chapter 5 
Routing parameters for the 
Megaplex-4 PW router 
(interfaces, associated static 
routes, default gateway) 
configure>router (2) 
Pseudowire Router in Chapter 8 
Configuring flows 
 
 
Configuring ingress and egress 
flows between the SVI port 
(bound to Router 2 interface) 
and Logical MAC port or 
Ethernet port  
configure>flows 
 
Flows in Chapter 8 
Configuring cross-connect  
 
 
13. Versatile I/O Modules 
Task 
Configuration Context 
Comments and Reference  
Configuring DS0 cross-connect 
between the E1/T1/DS1 port or 
the module and timeslots on 
the E1/T1/DS1/DS1-opt ports of 
the uplink module) 
configure>cr>ds0 
DS0 Cross-Connect in Chapter 8 
 
Configuring DS0 cross-connect 
between the timeslots of E1/T1 
and DS1 ports of the same 
module 
configure>cr>ds0 
DS0 Cross-Connect in Chapter 8 
 
Cross-connect the full payload 
from this E1/T1 port with 
another port of the same type 
and configuration 
configure>cr>tdm   
 
Cross-connecting the 
DS1/E1/T1 port with a vc12-
vt2/vc11-vt1.5 from an 
SDH/SONET port  
configure>cr>sdh-sonet   
 
SDH/SONET Cross-Connect in 
Chapter 8 
Establishing cross-connection 
between the pseudowire and 
timeslots on the 
ds1/serial/E1/T1 port (of the 
VS-16E1T1-PW or VS-6/E1T1 
module) 
configure>cr>pw-tdm  
 
PW-TDM Cross-Connect in 
Chapter 8 
 
Configuring protection 
 
 
Configuring protection for 
internal DS1 or E1/T1 ports 
configure>protection>tdm-
group 
TDM Group Protection in 
Chapter 7 
 
Configuring protection for PWs 
configure>protection>pw 
PW Protection in Chapter 7 
13. Versatile I/O Modules 
Diagnostics  
Serial Ports 
VS diagnostic capabilities include local and remote digital loopbacks on each serial port (see Serial Ports in 
Chapter 5). 
E1/T1 Ports 
E1/T1 diagnostic capabilities include local and remote loopbacks on each E1/T1 port (per port and per 
timeslot) (see E1 Ports and T1 Ports in Chapter 5).  
In addition, VS modules feature the BER Test on E1/T1 ports.  
DS1 Ports 
DS1 diagnostic capabilities include local and remote loopbacks on each DS1 port (per port and per timeslot) 
(see DS1 Ports in Chapter 5).  
Monitoring  
The monitoring tasks supported on each local VS port level are listed in the table below. 
Level 
Monitored Feature 
Path  
Reference  
Serial ports  
Status data  
configure>port> 
serial  
Serial Ports  in Chapter 5 
 
Statistics (3-bit transitional, 
HCM, R.111 encapsulation 
modes) 
configure>port> 
serial 
Serial Ports  in Chapter 5 
 
DS1 ports 
Status data for the DS1 port 
 
configure>port>ds1 
DS1 Ports in Chapter 5  
E1 ports 
 
 
 
Transmission performance 
statistics 
configure>port>e1 
Displaying E1 Port 
Statistics in Chapter 5 
Status data  
configure>port>e1 
Viewing E1 Port Status 
in Chapter 5  
Protection status  
configure> 
protection>tdm-group 
TDM Group Protection 
in Chapter 7  
13. Versatile I/O Modules 
Level 
Monitored Feature 
Path  
Reference  
T1 ports 
 
 
 
Transmission performance 
statistics 
configure>port>t1 
Displaying T1 Port 
Statistics in Chapter 5 
 
Status data  
configure>port>t1 
Viewing T1 Port Status 
in Chapter 5  
 
Protection status  
configure> 
protection>tdm-group 
TDM Group Protection 
in Chapter 7  
PW ports  
 
Transmission performance 
statistics  
configure>port>pw 
Displaying PW Statistics 
in Chapter 8  
 
Status data  
configure>port>pw  
Viewing the Pseudowire 
Status in Chapter 8  
 
Protection status  
configure> 
protection>pw 
PW Protection in 
Chapter 7  
Troubleshooting  
Serial Ports 
Refer to Error! Reference source not found. in VS (VS-12, VS-6/BIN and VS-6/C37) section. 
E1/T1 Ports 
If a problem occurs, check the displayed alarm messages and refer to the Chapter 11 for their 
interpretation.  
Note 
If the problem is detected the first time the module is put into operation, 
perform the following preliminary checks before proceeding: 
• 
Check for proper module installation and correct cable connections, in 
accordance with the system installation plan. 
• 
Check that the module configuration parameters are in accordance with 
the specific application requirements, as provided by the system 
administrator. 

## 13.5 VS–16E1T1-EoP Modules  *(p.1068)*

13. Versatile I/O Modules 
If, after collecting all the relevant information, the problem appears to be related to the operation of one 
of the ports, perform the actions listed below, until the problem is corrected: 
• 
Make sure that no test has been activated on the corresponding port. Use the Megaplex-4 
management system to find and deactivate the active test or loopback. 
• 
Activate the local loopback on the corresponding port. If the indicator of the corresponding local 
port lights in green while the loop is connected, the problem is external. Check cable connections 
and the transmission equipment providing the link to the remote unit. 
• 
Quickly check the link to the remote Megaplex-4 unit by activating the remote port loopback at the 
remote unit. If the link operates properly, the indicator of the corresponding local port lights in 
green. 
If the test fails, there is a problem with the transmission through the network, or with the modules. 
Repeat the test after carefully checking all the configuration parameters of the module and its 
ports. If the problem persists, replace the module and check again. 
13.5 VS–16E1T1-EoP Modules  
This section describes the technical characteristics, applications, installation and operation of the VS-
16E1T1-EoP E1/T1 interface modules for use in the Megaplex-4 Next Generation Multiservice Access Node, 
ver 4.7 and higher.  
Applications  
The figure below shows multiservice aggregation over E1/T1.  
13. Versatile I/O Modules 
E1/T1
E1/T1
PBX
Megaplex-4
PBX
Megaplex-4
E1/T1
PBX
Megaplex-4
SDH/
SONET
Radio
Radio
 
 
Features  
VS-16E1T1-EoP Module 
The VS-16E1T1-EoP module uses next generation Ethernet over PDH encapsulation and bonding methods 
including: 
• 
Standard generic framing procedure (GFP) per G.8040 and G.7041/Y.1303 
• 
Virtual concatenation (VCAT) per G.7043 (PDH). 
• 
Link capacity adjustment scheme (LCAS) per G.7042. 
The module architecture and data flow for VS-16E1T1-EoP modules are shown in below. The table lists the 
module entities (ports) and their hierarchy.  
13. Versatile I/O Modules 
DS0
VCG 1..16
Switch
E1-i/T1-i 
1..16
E1/T1 
1..16
32 x E1
GbE
Data + 
Signaling
1:1
1:1
CL.2 
Ethernet 
Data 
only
L. MAC 1..16
GFP 1..16
CL.2 DS0 
Cross-Connect 
 
VS-16E1T1-EoP Module Architecture Entities and their Hierarchy  
Name 
Number of Ports  
Possible Values 
e1-i/t1-i 
16 
slot/1… slot/16 
e1/t1 
16 
slot/1… slot/16 
vcg 
16 
slot/1… slot/16 
gfp 
16 
slot/1… slot/16 
logical-mac 
16 
slot/1… slot/16 
Ethernet over E1/T1 
VS-16E1T1-EoP modules allow encapsulating Ethernet traffic with the GFP protocol and transferring it over 
E1/T1 media. Up to 16 Logical MAC, GFP and VCG ports can be created. In this case Ethernet ports are 
connected to Logical MAC ports via flows, and these Logical MAC ports are bound to GFP ports and GFP 
ports are bound to VCG ports. Up to 16 E1/T1 and/or E1-i/T1-i ports can be bound to each VCG port.  
This functionality is supported when VS-16E1T1-EoP modules are working with CL modules having GbE 
ports.  
13. Versatile I/O Modules 
E1/T1 Services  
The E1 interface is compatible with all carrier-provided E1 services, meeting the requirements of ITU-T Rec. 
G.703, G.704 and G.732. It supports both 2 (G.732N) and 16 (G.732S) frames per multiframe formats, as 
well as unframed mode. It also supports CRC-4 and E bit, in compliance with G.704 recommendations. Zero 
suppression over the line is HDB3.  
The T1 interface is compatible with ANSI requirements. Both D4 and ESF framing formats are supported. 
Zero suppression is selectable for Transparent, B7ZS, or B8ZS.  
Internal TDM flows are handled by an internal DS0 cross-connect matrix. The matrix supports flexible 
payload routing, independently configurable for each port, at the individual timeslots (DS0) level. This 
enables routing individually selected timeslots (including timeslots with split assignment) to other modules 
installed in the Megaplex-4 chassis, via the internal TDM buses. Timeslots can be routed to any port with 
compatible properties. The signaling information associated with voice timeslots can be translated by 
means of user-specified signaling profiles.  
The E1/T1 ports can also be connected to SDH/SONET links, which permits using the Megaplex-4 as an 
SDH/SONET terminal multiplexer (TM). Using the Megaplex-4 as an add/drop multiplexer (ADM), in either 
linear chain or ring topologies, enables dropping part of the SDH/SONET link payload at a certain location, 
and possibly inserting other payload. 
Timing 
VS-16E1T1-EoP modules recover the timing of each received E1/T1 stream, and therefore can also provide 
timing reference signals derived from a selected E1/T1 stream for the nodal Megaplex-4 timing subsystem. 
VS-16E1T1-EoP transmit timing can be locked to the Megaplex-4 nodal timing.  
Cross-Connections 
The VS-16E1T1-EoP modules feature DS0 and TDM cross-connections, which can be used according to the 
module application as shown in the table below. For description of DS0 and TDM cross-connect 
functionalities, see respective sections in Chapter 8. 
13. Versatile I/O Modules 
Cross-Connect Type 
Diagram 
DS0 cross-connect between the 
E1/T1 port of the module and 
timeslots on the E1/T1/DS1 ports of 
the uplink module 
1  
e1/t1
cross connect 
dso
e1/t1/ds1
e1/t1
 
 
TDM cross-connect: a full payload 
E1/T1 port is cross-connected 
via tdm cross-connect only 
with another full payload 
E1/T1 port on an I/O module 
supporting transparent 
mapping 
2  
e1/t1
cross connect d 
tdm
e1/t1
e1/t1
 
 
DS0 Cross-Connect  
The DS0 cross-connect matrix of the Megaplex-4 chassis enables flexible payload routing in the VS-16E1T1-
EoP modules, independently configurable for each port, at the individual timeslots (DS0) level. This routing 
is configured via ds0 cross-connect command between the E1/T1 ports and timeslots on the E1/T1/DS1 
ports of the uplink module.  
TDM Cross-Connect 
In Diagram 2, a full payload E1/T1 port can be cross-connected via tdm cross-connect only with another full 
payload E1/T1 port on an I/O module supporting transparent mapping.  
Note 
When VS-16E1T1-EoP modules are working with CL modules without 
SDH/SONET ports, only DS0 cross-connect is supported.  
Mapping of E1/T1/E1-i/T1-i Links over SDH/SONET  
The E1/T1 ports can also be connected to SDH/SONET links, which permits using the Megaplex-4 as an 
SDH/SONET terminal multiplexer (TM). Using Megaplex-4 as an add/drop multiplexer (ADM), in either 
linear chain or ring topologies, enables dropping a part of the SDH/SONET link payload at a certain location, 
and possibly inserting other payload. 
13. Versatile I/O Modules 
When VS-16E1T1-EoP modules are working with CL modules that have SDH/SONET ports, it allows direct 
transparent mapping of unframed E1/T1 links over SDH/SONET; this feature is also called “transparent 
clocking”. For external E1/T1 ports, framed payload can be mapped to SDH/SONET links in two stages: first 
via DS0 cross-connect to E1-i/T1-i ports of CL.2 modules and then to SDH/SONET containers. For internal 
E1/T1 ports, framed payload can be directly mapped to SDH/SONET.  
Inband Management 
• 
VS-16E1T1-EoP supports the transfer of management traffic, inband. A dedicated management 
timeslot can be configured on each E1/T1 port operating in a framed mode. This enables extending 
the management connections to other RAD equipment using inband management over dedicate 
timeslots. 
Protection  
The external E1/T1 ports of VS-16E1T1-EoP use the TDM group protection functionality.  
The Logical MAC ports of VS-16E1T1-EoP use the Ethernet group protection functionality, it is used for 
protecting Ethernet and packet traffic against transmission failures on the E1/T1, E1-i/T1-i links.  
For more information, see TDM Group Protection and Ethernet Group Protection in Chapter 7. 
Physical Description  
The VS-16E1T1-EoP module occupies one I/O slot in the Megaplex-4 chassis. The module is based on a 
main board and two factory-replaceable submodules.  
 
The submodules are identical, each including a TDM interfacing section with 8 E1/T1 ports.  
The VS-16E1T1-EoP module panel is shown below. The panel includes two 44-pin D-type female 
connectors, designated 1-8 and 9-16, for connecting to E1/T1 ports 1 to 8 and 9 to 16, respectively. 
 
Interface 
Module 1
Interface 
Module 2
Main Board
13. Versatile I/O Modules 
 
VS-16E1T1-EoP Module Panel 
LED Indicators 
Each E1/T1 port has its own dual-color LED indicator. Each port status indicator operates as follows: 
• 
Lights steadily in green when the corresponding port is operating properly and is active (that is, it is 
connected, and serves as the working port when included in a protection group). 
• 
Flashes in green when the corresponding port is operating properly, and serves as the protection 
port when TDM or Ethernet group protection is enabled. 
• 
Lights in red when the corresponding port detects loss of synchronization, loss of signal or a red 
alarm 
13. Versatile I/O Modules 
• 
Flashes in red when the corresponding port is serving as the protection port and detects loss of 
synchronization  
• 
Off when the corresponding port is not connected. 
Technical Specifications 
E1 Interface 
Type and Bit Rate 
E1, 2.048 Mbps (per link) 
Number of Links 
16 
Line Interface 
• 4-wire, 120Ω balanced 
• Coax, 75Ω unbalanced 
Line Code 
HDB3 
Compliance 
ITU-T Rec. G.703, G704, G.732 (including CRC-4 and E bit) 
Framing 
• Basic G.704 framing (G732N) with or without CRC-4 
per ITU-T Rec. G.704 
• Timeslot 16 multiframe (G732S), with or without CRC-4 
per ITU-T Rec. G.704 
• No framing (unframed mode) 
Transmit Level 
• ±3V ±10%, balanced 
• ±2.37V ±10%, unbalanced 
 
Receive Level 
Software selectable: 
• 0 through -12 dB for short haul mode 
• 0 through -43 dB for long haul mode 
 
Jitter Performance 
Per ITU-T Rec. G.823 
 
Surge Protection 
Per ITU-T Rec. K.21 
 
Connector 
44-pin D-type female for all ports. Adapter (splitter) cables 
are available from RAD 
T1 Interface 
Type and Bit Rate 
T1, 1.544 Mbps 
 
Compliance 
ANSI T1.107, ANSI T1.403  
 
Line Interface 
4-wire, 100Ω balanced 
 
Line Code 
Bipolar AMI 
 
Zero Suppression 
• Transparent (no zero suppression) 
• B7ZS  
• B8ZS 
13. Versatile I/O Modules 
 
Framing 
• ESF  
• SF (D4) (not in EoP mode) 
 
Transmit Levels 
• 0.6, 1.2, 1.8, 2.4, 3.0 dBm user-adjustable, measured at 
0 to 655 ft 
 
Receive Level 
0 to -12 dBm  
 
Jitter Performance  
Per AT&T TR-62411 
 
Surge Protection 
Per ITU-T Rec. K.21 
 
Connector   
44-pin D-type female for all ports. Adapter cables are 
available from RAD  
Indicators 
Status Indicator per Link 
Dual-color indicator: 
• Lights steadily in green when the port is connected and 
carries traffic 
• Flashes in green when the port is connected and is the 
protection port in a TDM or Ethernet group protection 
pair 
• Lights in red during red alarm 
• Flashes in red for a protection port that reports loss of 
synchronization 
• Off when not connected  
Power Consumption  
14.5W 
Configuration 
 
Programmable via Megaplex-4 management system  
Environment 
Operating Temperature 
-10°C to 55°C  (14°F to 131°F)   
 
Storage Temperature 
-20°C to 70°C  (-4°F to 160°F)   
 
Humidity 
Up to 95%, non-condensing 
Preparing the Module for Installation 
Note 
Before performing any internal settings, adjustment, maintenance, or repairs, 
first disconnect all the cables from the module, and then remove the module 
from the Megaplex-4 enclosure. 
No internal settings, adjustment, maintenance, and repairs may be performed 
by either the operator or the user; such activities may be performed only by a 
skilled technician who is aware of the hazards involved. 
Always observe standard safety precautions during installation, operation, 
and maintenance of this product. 
13. Versatile I/O Modules 
 
Caution 
The modules contain components sensitive to electrostatic discharge (ESD). 
To prevent ESD damage, always hold the module by its sides, and do not 
touch the module components or connectors.  
 
Caution 
To prevent physical damage to the electronic components assembled on the 
two sides of the module printed circuit boards (PCB) while it is inserted into 
its chassis slot, support the module while sliding it into position and make 
sure that its components do not touch the chassis structure, nor other 
modules.  
 
Installing a Module in the Chassis 
 
 
Warning 
The module starts operating as soon as it is inserted in an operating chassis.  
 To install a VS-16E1T1-EoP module in the chassis: 
1. Refer to the system installation plan and identify the prescribed module slot. 
2. Check that the fastening screws at the module sides are free to move. 
3. Insert the VS-16E1T1-EoP module in its chassis slot and slide it in as far as possible. 
4. Secure the VS-16E1T1-EoP module by tightening its two fastening screws. 
5. The module starts operating as soon as it is plugged into an operating enclosure. At this stage, 
ignore the alarm indications. 
 
13. Versatile I/O Modules 
Connecting to Remote Equipment 
The module E1/T1 ports are terminated in a 44-pin D-type female connector. The module connector 
supports both the unbalanced and balanced interfaces. Each type requires a different adapter cable. 
RAD offers the following adapter cables:  
• 
CBL-G703-8/RJ45: adapter cable terminated in RJ-45 plugs at the user’s end, for use when VS-
16E1T1-EoP modules are connected to equipment with balanced E1/T1 interfaces using pins 1, 2 
for the receive (RX) pair and pins 4,5 for the transmit (TX) pair  
• 
CBL-G703-8/RJ45/X: adapter cable terminated in RJ-45 plugs at the user’s end, for use when VS-
16E1T1-EoP modules are connected to equipment with balanced E1/T1 interfaces using pins 4,5 for 
the receive (RX) pair and pins 1, 2 for the transmit (TX) pair  
• 
CBL-G703-8/OPEN/2M: adapter cable terminated in free leads at the user’s end, for balanced 
E1/T1 applications 
• 
CBL-G703-8/COAX: adapter cable terminated in BNC connectors at the user’s end, for use when VS-
16E1T1-EoP modules are connected to equipment with unbalanced E1 interfaces.  
The following sections describe these adapter cables, the functions of the 44-pin connector pins for each 
interface type, and provide connection instructions. 
CBL-G703-8/RJ45 Cable  
The CBL-G703-8/RJ45 is a 2-meter cable for VS-16E1T1-EoP modules using the balanced interface.  
The figure below shows the cable construction. The table below presents the cable wiring and identifies the 
interface connector pin assignment. 
 
 
13. Versatile I/O Modules 
CBL-G703-8/RJ45 Cable  
CBL-G703-8/RJ45 Cable Wiring 
Channel 
RJ-45 
Connector  
44-Pin Connector 
RJ-45 
Connector 
Pins 
Channel 
RJ-45 
Connector  
44-Pin Connector 
RJ-45 
Connector 
Pins 
Pin 
Function 
Pin 
Function 
1  
CH-1 
31 
RX Ring 
1 
5 
CH-5 
37 
RX Ring 
1 
17 
RX Tip 
2 
23 
RX Tip 
2 
16 
TX Ring 
4 
22 
TX Ring 
4 
1 
TX Tip 
5 
7 
TX Tip 
5 
2  
CH-2 
33 
RX Ring 
1 
6 
CH-6 
38 
RX Ring 
1 
32 
RX Tip 
2 
39 
RX Tip 
2 
2 
TX Ring 
4 
8 
TX Ring 
4 
3 
TX Tip 
5 
9 
TX Tip 
5 
3  
CH-3 
34 
RX Ring 
1 
7 
CH-7 
40 
RX Ring 
1 
20 
RX Tip 
2 
26 
RX Tip 
2 
19 
TX Ring 
4 
25 
TX Ring 
4 
4 
TX Tip 
5 
10 
TX Tip 
5 
4  
CH-4 
35 
RX Ring 
1 
8 
CH-8 
41 
RX Ring 
1 
36 
RX Tip 
2 
42 
RX Tip 
2 
5 
TX Ring 
4 
11 
TX Ring 
4 
6 
TX Tip 
5 
12 
TX Tip 
5 
CBL-G703-8/RJ45/X Cable  
CBL-G703-8/RJ45/X is a 2-meter cable. The figure below shows the cable construction. The table below 
presents the cable wiring and identifies the interface connector pin assignment. 
13. Versatile I/O Modules 
CBL- G703-8/RJ45/X
Ch. 1
Ch. 2
Ch. 3
Ch. 4
Ch. 6
Ch. 7
Ch. 8
Ch. 5
 
CBL-G703-8/RJ45/X Cable  
CBL-G703-8/RJ45/X Cable Wiring 
Channel RJ-45 
Connector 
44-Pin 
Connector 
RJ-45 
Connector Pins Channel RJ-45 
Connector 
44-Pin 
Connector 
RJ-45 
Connector Pins 
Pin Function 
Pin Function 
1  
CH-1 
31 
RX Ring 
4 
5 
CH-5 
37 
RX Ring 
4 
17 
RX Tip 
5 
23 
RX Tip 
5 
16 
TX Ring 
1 
22 
TX Ring 
1 
1 
TX Tip 
2 
7 
TX Tip 
2 
2  
CH-2 
33 
RX Ring 
4 
6 
CH-6 
38 
RX Ring 
4 
32 
RX Tip 
5 
39 
RX Tip 
5 
2 
TX Ring 
1 
8 
TX Ring 
1 
3 
TX Tip 
2 
9 
TX Tip 
2 
3  
CH-3 
34 
RX Ring 
4 
7 
CH-7 
40 
RX Ring 
4 
20 
RX Tip 
5 
26 
RX Tip 
5 
19 
TX Ring 
1 
25 
TX Ring 
1 
4 
TX Tip 
2 
10 
TX Tip 
2 
4  
CH-4 
35 
RX Ring 
4 
8 
CH-8 
41 
RX Ring 
4 
36 
RX Tip 
5 
42 
RX Tip 
5 
5 
TX Ring 
1 
11 
TX Ring 
1 
13. Versatile I/O Modules 
6 
TX Tip 
2 
12 
TX Tip 
2 
CBL-G703-8/OPEN/2M Cable 
CBL-G703-8/OPEN/2M cable is a 2-meter cable for VS-16E1T1-EoP modules using the balanced E1/T1 
interface, terminated in free leads that can be connected to any terminal block or connector appropriate 
for your application. 
The figure below shows the cable construction. The table below resents the cable wiring and identifies the 
pair functions. 
 
CBL-G703-8/OPEN/2M Cable 
CBL-G703-8/OPEN/2M Cable Wiring  
Channel 
44-Pin Connector 
Pair Color 
Channel 
44-Pin Connector 
Pair Color 
Pin 
Function 
Pin 
Function 
1 
31 
Rx Ring 
White 
5 
37 
Rx Ring 
White 
17 
Rx Tip 
Blue 
23 
Rx Tip 
Brown/Blue 
1 
Tx Tip 
Orange 
7 
Tx Tip 
Grey/Blue 
16 
Tx Ring 
White 
22 
Tx Ring 
White 
2 
33 
Rx Ring 
White 
6 
38 
Rx Ring 
White 
32 
Rx Tip 
Green 
39 
Rx Tip 
White/Orange 
3 
Tx Tip 
Brown 
9 
Tx Tip 
Orange/Green 
2 
Tx Ring 
White 
8 
Tx Ring 
White 
3 
34 
Rx Ring 
White 
7 
40 
Rx Ring 
White 
20 
Rx Tip 
Grey 
26 
Rx Tip 
Orange/Brown 
4 
Tx Tip 
White/Blue 
10 
Tx Tip 
Grey/Orange 
19 
Tx Ring 
White 
25 
Tx Ring 
White 
4 
35 
Rx Ring 
White 
8 
41 
Rx Ring 
White 
36 
Rx Tip 
Orange/Blue 
42 
Rx Tip 
White/Green 
6 
Tx Tip 
Green/Blue 
12 
Tx Tip 
Green/Brown 
5 
Tx Ring 
White 
11 
Tx Ring 
White 
CBL-G703-8/OPEN/2M
13. Versatile I/O Modules 
CBL-G703-8/COAX Cable  
CBL-G703-8/COAX is a 2-meter cable for VS-16E1T1-EoP modules using the unbalanced E1 interface. The 
figure below shows the cable construction.  
 
CBL-G703-8/COAX Cable 
The table below presents the cable wiring and identifies the interface connector pin assignment.  
CBL-G703-8/COAX Cable Wiring 
Channel 
Function 
44-Pin Connector 
BNC Contact 
Channel 
Function  
44-Pin Connector 
BNC 
Contact 
Pin 
Function 
Pin 
Function 
1  
RX 
31 
Ring 
Shield 
5 
RX 
37 
Ring 
Shield 
29 
Frame Ground 
29 
Frame Ground 
 
17 
Tip 
Center 
23 
Tip 
Center 
TX 
1 
Tip 
Center 
TX 
7 
Tip 
Center 
16 
Ring 
Shield 
22 
Ring 
Shield 
14 
Frame Ground 
14 
Frame Ground 
2  
RX 
33 
Ring 
Shield 
6 
RX 
38 
Ring 
Shield 
44 
Frame Ground 
44 
Frame Ground 
 
32 
Tip 
Center 
39 
Tip 
Center 
TX 
3 
Tip 
Center 
TX 
9 
Tip 
Center 
2 
Ring 
Shield 
8 
Ring 
Shield 
29 
Frame Ground 
14 
Frame Ground 
3  
RX 
34 
Ring 
Shield 
7 
RX 
40 
Ring 
Shield 
29 
Frame Ground 
29 
Frame Ground 
 
20 
Tip 
Center 
26 
Tip 
Center 
13. Versatile I/O Modules 
TX 
4 
Tip 
Center 
TX 
10 
Tip 
Center 
19 
Ring 
Shield 
25 
Ring 
Shield 
14 
Frame Ground 
14 
Frame Ground 
4  
RX 
35 
Ring 
Shield 
8 
RX 
41 
Ring 
Shield 
44 
Frame Ground 
44 
Frame Ground 
 
36 
Tip 
Center 
42 
Tip 
Center 
TX 
6 
Tip 
Center 
TX 
12 
Tip 
Center 
5 
Ring 
Shield 
11 
Ring 
Shield 
29 
Frame Ground 
14 
Frame Ground 
Cable Type Sensing 
15 
Not used 
– 
 
 
 
 
Signal Ground 
30 
Ground 
– 
Frame Ground 
44 
Cable Shield 
– 
Connecting Cables to the E1/T1 Ports  
Using the site installation plan, identify the cable intended for connection to the corresponding VS-16E1T1-
EoP connector, and connect the cable to the module as explained below. 
 To connect the CBL-G703-8/RJ45 and CBL-G703-8/RJ45/X cables: 
1. Connect the 44-pin connector of the cable to the front panel connector. 
2. Connect the RJ-45 plug of each port interface (the plugs are marked CH-1 to CH-8) to the 
prescribed user equipment or patch panel connector. Insulate unused connectors, to prevent 
accidental short-circuiting of their exposed contacts to metallic surfaces.  
 To connect the CBL-G703-8/COAX cable: 
1. Connect the 44-pin male connector of the cable to the front panel connector. 
2. Connect the BNC plugs of each port interface (the plugs are marked with the number of the port) 
to the prescribed user equipment or patch panel connectors. Pay attention to correct connection: 
 
TX connector: serves as the transmit output of the port  
 
RX connector: serves as the receive input of the port. 
 To connect the CBL-G703-8/OPEN cable: 
1. Connect the free cable ends in accordance with the prescribed termination method. 
2. When done, connect the 44-pin male connector of the cable to the front panel connector. 
13. Versatile I/O Modules 
Normal Indications 
The status of each VS-16E1T1-EoP link is indicated by a separate indicator.  
During normal operation, after communication with the remote equipment is established, the port 
indicators of the VS-16E1T1-EoP module light steadily in green; however, if a port is configured as the 
protection port in a protection group, its indicator flashes in green. 
If the other communication equipment on the link is not yet operative, the port indicator lights in red. The 
indicator turns green (or flashes in green) as soon as the link with the remote equipment is established.  
The indicators of ports configured at shutdown are off.  
Configuration Considerations 
Configuring Transparent Mapping of E1/T1 Links over SDH/SONET  
 To configure a direct E1/T1 to  SDH/SONET connection: 
1. At the config# prompt, enter cross-connect or cr. 
The config>xc# prompt appears. 
2. Configure the cross connection as shown in the example below. 
VS-16E1T1-EoP module: 
• 
I/O slot 1 
• 
E1 port 2 
Mapping E1 port 2 to the following VC-12 container: 
• 
VC-12 = 1 
• 
TUG-3 = 7 
• 
TUG-2 = 1 
• 
AUG 1 = 1 
• 
SDH port 1 on the CL-A module. 
 cr sdh-sonet vc12-vt2 cl-a/1/1/1/7/1  e1 1/2 
13. Versatile I/O Modules 
Mapping Framed E1/T1 Link Payload to SDH/SONET  
Framed external E1/T1 links do not allow direct mapping to SDH/SONET. In this case the mapping is done in 
two stages: first the E1/T1 port is mapped to an internal E1/T1 port on the CL.2 module and then the 
internal E1/T1 port is mapped to the SDH/SONET. 
The following example serves as an illustration. 
• 
VS-16E1T1-EoP module installed in slot 1 
• 
Port 2, line type G.732S 
config>port>e1(1/2)# line-type g732s  
• 
 Cross-connecting E1 port 2 with internal E1 port 46 on CL-A module  
config>xc# ds0 e1 1/2 ts 1 e1-i cl-a/46 ts 1 data bi-direction 
config>xc# ds0 e1-i cl-a/46 ts 1 e1 1/2 ts 1 data bi-direction 
• 
Cross-connecting (mapping) internal E1 port 1 to the SDH: 
 
VC-12 = 2 
 
TUG-3 = 1 
 
TUG-2 = 1 
 
AUG 1 = 1 
 
SDH port 1 on the CL-A module. 
config# cr sdh-sonet vc12-vt2 cl-a/1/1/1/1/2 e1-i cl-a/46 
Internal E1/T1 links allow direct mapping to SDH/SONET when line-type of the internal E1/T1 ports is set as 
G.732N-CRC/ESF. 
The following example serves as an illustration. 
• 
VS-16E1T1-EoP module installed in slot 1 
• 
Port 2, line type G.732N-CRC 
config>port>e1-i(1/2)# line-type g732n-crc 
• 
Cross-connecting (mapping) internal E1 port 1 to the SDH: 
 
VC-12 = 1 
 
TUG-3 = 1 
 
TUG-2 = 1 
 
AUG 1 = 1 
 
Internal E1 port 1 on the VS-16E1T1-EoP module. 
config# cr sdh-sonet vc12-vt2 cl-a/1/1/1/1/1 e1-i 1/2 
13. Versatile I/O Modules 
Selecting an E1/T1 Port as System Timing Reference  
After an external E1/T1 port of VS-16E1T1-EoP module is configured and at no shutdown, its receive clock 
can be selected as a timing reference for the Megaplex-4 system. 
To modify the system timing reference with the supervision terminal, use the following commands at the 
config>system>clock>domain(1)# prompt: 
source <src-id> rx-port e1 <slot>/<port> 
source <src-id> rx-port t1 <slot>/<port> 
For detailed instructions, refer to Chapter 9. 
Configuration Sequence 
The list of tasks that can be performed on the VS-16E1T1-EoP module and the recommended configuration 
sequence are described in the table below. For detailed descriptions, refer to Chapter 5. The second 
column indicates the configuration context for this task, under which it can be found in Chapter 5. The third 
column refers to the reference tables that should be consulted when planning the module operation. 
Task 
Configuration Context 
Reference  
Configure a VS-16E1T1-EoP 
module and put it into service 
configure>slot>card-type  
VS-16E1-EOP: card-type=versatile  vs-e1-eop 
VS-16T1-EOP: card-type=versatile  vs-t1-eop  
Select an E1/T1 port as 
system timing reference  
config>system>clock>domain(1) 
 
Configure the E1 port 
parameters  
configure>port>e1 
E1 Ports in Chapter 5, pay attention to 
Features Supported by Megaplex-4 E1 and 
Internal E1 Ports table 
Configure the T1 port 
parameters  
configure>port>t1 
T1 Ports in Chapter 5, pay attention to 
Features Supported by Megaplex-4 T1 and 
Internal T1 Ports table 
Configure the VCG 
parameters and bind E1/T1 or 
E1-i/T1-i  ports to the VCG  
configure>port>vcg 
VCG Ports in Chapter 5 
Configure the GFP port 
parameters and bind VCG 
port to this GFP port 
configure>port>gfp 
GFP Ports in Chapter 5 
13. Versatile I/O Modules 
Task 
Configuration Context 
Reference  
Configure the Logical MAC 
and bind GFP port to it 
configure>port>logical-mac 
Logical MAC Ports in Chapter 5 
Configure flows between the 
Logical MAC and Ethernet 
ports 
configure>flow 
Flows in Chapter 8 
Configure timeslot 
assignment for E1/T1 ports 
(DS0 cross-connect for E1/T1 
ports) 
configure>cr>ds0 
To find which ports on which modules can be 
cross-connected with VS-16E1T1-EoP ports, 
see Cross-Connect Table in Chapter 8 
Cross-connect the full payload 
from this E1/T1 port with 
another port of the same type 
and configuration 
configure>cr>tdm   
 
Cross-connect the unframed 
E1/T1 port and internal 
E1/T1with a vc12-vt2/vc11-
vt1.5 from an SDH/SONET 
port  
configure>cr>sdh-sonet   
 
Line type is g.732n-crc/esf only 
Cross-connect the framed 
E1/T1 port with a vc12-
vt2/vc11-vt1.5 from an 
SDH/SONET port  
configure>cr>ds0   
 
 
Configure TDM group 
protection  
config>protection>tdm-group 
 
Monitoring and Diagnostics  
VS-16E1T1-EoP diagnostic capabilities include local and remote loopbacks on each E1/T1 and E1-i/T1-i port 
(per port and per timeslot) (see E1 Ports and, respectively, T1 Ports in Chapter 5). 
For performance monitoring and statistics on the E1/T1 ports, E1-i/T1-i ports, GFP ports, VCG Ports and 
Logical MAC ports, see E1/T1 Ports, GFP Ports, VCG Ports and Logical MAC Ports, respectively, in Chapter 
5). 
13. Versatile I/O Modules 
Troubleshooting  
If a problem occurs, check the displayed alarm messages and refer to the Chapter 11 for their 
interpretation.  
Note 
If the problem is detected the first time the module is put into operation, 
perform the following preliminary checks before proceeding: 
• 
Check for proper module installation and correct cable connections, in 
accordance with the system installation plan. 
• 
Check that the module configuration parameters are in accordance with 
the specific application requirements, as provided by the system 
administrator. 
If, after collecting all the relevant information, the problem appears to be related to the operation of one 
of the ports, perform the actions listed below, until the problem is corrected: 
• 
Make sure that no test has been activated on the corresponding port. Use the Megaplex-4 
management system to find and deactivate the active test or loopback. 
• 
Activate the local loopback on the corresponding port. If the indicator of the corresponding local 
port lights in green while the loop is connected, the problem is external. Check cable connections 
and the transmission equipment providing the link to the remote unit. 
• 
Quickly check the link to the remote Megaplex-4 unit by activating the remote port loopback at the 
remote unit. If the link operates properly, the indicator of the corresponding local port lights in 
green. 
If the test fails, there is a problem with the transmission through the network, or with the modules. 
Repeat the test after carefully checking all the configuration parameters of the module and its 
ports. If the problem persists, replace the module and check again. 
 