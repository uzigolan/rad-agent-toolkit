# 5 Cards and Ports – 5.18 SDH/SONET Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 357–399.*


## Applicability and Scaling  *(p.357)*

5. Cards and Ports 
Activating the Loopbacks 
 To perform a loopback on the serial port: 
1. Navigate to configure port serial <slot>/<port> to select the serial port to configure. 
The config>port>serial>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Activating and configuring the 
direction of the loopback  
loopback {local | remote | 
remote-on-remote}  
 
• local. Returns the transmitted data 
at the physical layer to the receiving 
path. The local physical loopback 
includes a configurable timeout 
mechanism that ends the loopback 
operation after a user-defined 
duration. 
• remote. Returns the received data 
at the physical layer to the 
transmitting path. 
• remote-on-remote. Returns the 
data transmitted from the OCU-DP 
port towards the CSU/DSU back to 
the OCU-DP receive line. Relevant 
for VS-OCU/E&M only. 
• Using no loopback stops the 
loopback. 
5.18 SDH/SONET Ports 
Applicability and Scaling 
Megaplex-4 features four SDH/SONET ports (two ports located on each of the two CL.2 modules). The 
ports can be ordered either with STM-1/OC-3 or STM-4/OC-12 interfaces. The panels and terminal 
identification for the STM-1/OC-3 and STM-4/OC-12 versions are identical. 

## Standards Compliance  *(p.358)*


## Functional Description  *(p.358)*

5. Cards and Ports 
Standards Compliance 
The SDH/SONET ports comply with the following standards:  
• 
SDH: ITU-T G.957, G.783, G.798 
• 
SONET: GR-253-core. 
In particular, framing complies with the following: 
• 
SDH: ITU-T G.707, G.708, G.709 
• 
SONET: GR-253-core. 
Functional Description  
SDH Implementation Principles  
This section describes the implementation principles for the Synchronous Digital Hierarchy (SDH), as a 
background for the detailed presentation of the SDH signal structures. In the following explanations, the 
following terms are used to describe SDH networks: 
• 
Network node. The SDH network node is a facility at which signals built in accordance with the 
SDH frame structure are generated and/or terminated. Therefore, a network node provides a 
convenient access point to add or drop payload signals, e.g., PDH tributary signals, for 
transmission over the SDH network.  
• 
SDH transport system. An SDH transport system provides the technical means to transfer SDH 
signals between two network nodes. 
• 
SDH network. An SDH network is formed by interconnecting the required number of network 
nodes by means of SDH transport systems.  
The Synchronous Digital Hierarchy (SDH) is implemented on the basis of two principles: 
1. Direct synchronous multiplexing of individual tributary signals within the structure of the 
higher-rate multiplexed signal.  
2. Transparent transporting of each individual tributary signal through the network, without any 
disassembly except at the two network nodes that exchange information through that particular 
signal.  
To enable synchronous multiplexing, SDH equipment is designed to permit efficient and reliable 
synchronization of the whole network to a single timing reference. 
5. Cards and Ports 
Direct Multiplexing Approach 
Direct multiplexing means that individual tributary signals can be inserted and removed into the SDH 
multiplexed signal without intermediate multiplexing and demultiplexing steps. This capability results in 
the following characteristics: 
• 
Efficient signal transport, as the same SDH transport system can carry various types of payloads 
(tributary signals).  
• 
Flexible routing, because any tributary can be inserted and removed into the SDH signal as a 
single unit, without affecting in any way the other tributary signals carried by the same SDH 
signal. This permits the user to build cost-effective add/drop multiplexers, the key component of 
flexible networks, instead of implementing digital cross-connect systems as entities separated 
from multiplexing equipment.  
In addition, the SDH signal structure includes sufficient overhead for management and maintenance 
purposes, and therefore provides the network operator full control over all the operational aspects of 
SDH networks and equipment units. This overhead permits the integration of the network management 
and maintenance functions within the transport network itself. 
General Structure of SDH Signals  
The SDH signal is a serial signal stream with a frame structure. The figure below shows the general 
structure of SDH signals. 
The SDH frame structure is formed by byte-interleaving the various signals carried within its structure. 
Each SDH frame starts with framing bytes, which enable equipment receiving the SDH data stream to 
identify the beginning of each frame. The location of the other bytes within this frame structure is 
determined by its position relative to the framing byte. 
The organization of the frame can be easily understood by representing the frame structure as a 
rectangle comprising boxes arranged in N rows and M columns, where each box carries one byte. In 
accordance with this representation, the framing byte appears in the top left-hand box (the byte located 
in row 1, column 1), which by convention is referred to as byte 1 of the SDH frame.  
5. Cards and Ports 
N x M Bytes
M Columns
F
F
F
F
N Rows
B   Signal Byte
F   Framing Byte
N x M Bytes
1
2
Order of
Transmission
F
B
B
B
B
B
B
B
B
Order of
Transmission
Legend
 
The frame bytes are transmitted bit by bit, sequentially, starting with those in the first row (see arrow in 
figure above). After the transmission of a row is completed, the bits in the next lower row are 
transmitted. The order of transmission within each row is from left to right. After transmission of the 
last byte in the frame (the byte located in row N, column M), the whole sequence repeats - starting with 
the framing byte of the following frame. 
SDH Frame Organization 
As shown below, an SDH frame comprises two distinct parts: 
• 
Section Overhead (SOH) 
• 
Virtual Container (VC). 
5. Cards and Ports 
Path Overhead (One Column)
 Virtual Container
(VC)
M Columns
N Rows
Section
Overhead
F
F
F
F
 
Section Overhead 
In SDH networks, the term section refers to the link between two consecutive SDH equipment units of 
the same type. 
Some signal carrying capacity is allocated in each SDH frame for the section overhead. This provides the 
facilities (alarm monitoring, bit error monitoring, data communications channels, etc.) required to 
support and maintain the transportation of a VC between nodes in an SDH network.  
The section overhead pertains only to an individual SDH transport system. This means that the section 
overhead is generated by the transmit side of a network node, and is terminated at the receive side of 
the next network node.  
Therefore, when several SDH transport systems are connected in tandem, the section overhead is not 
transferred together with the payload (VC) between the interconnected transport systems. 
Virtual Container (VC)  
The VC is an envelope (i.e., a special type of signal structure, or frame) that is used to transport a 
tributary signal across the SDH network.  
The path followed by a VC within the network may include any number of nodes, therefore the VC may 
be transferred from one SDH transport system to another, many times on its path through the network. 
Nevertheless, in most cases the VC is assembled at the point of entry to the SDH network and 
disassembled only at the point of exit.  
Since the VC is handled as an envelope that is opened only at the path end points, some of its signal 
carrying capacity is dedicated to path overhead. The path overhead provides the facilities (e.g., alarm 
5. Cards and Ports 
and performance monitoring), required to support and maintain the transportation of the VC between 
the end points. 
VC Assembly/Disassembly Process 
The concept of a tributary signal being inserted into a virtual container, to be transported end-to-end 
across a SDH network, is fundamental to the operation of SDH networks. This process of inserting the 
tributary signal into the proper locations of a VC is referred to as “mapping”. 
In all the SDH signal structures, the carrying capacity provided for each individual tributary signal is 
always slightly greater than that required by the tributary rate. Thus, the mapping process must 
compensate for this difference. This is achieved by adding stuffing bytes, e.g., path overhead bytes, to 
the signal stream as part of the mapping process. This increases the bit rate of the composite signal to 
the rate provided for tributary transport in the SDH structure. 
At the point of exit from the SDH network, the tributary signal must be recovered from the virtual 
container, by removing the path overhead and stuffing bits. This process is referred to as “demapping”. 
After demapping, it is necessary to restore the original data rate of the recovered tributary data stream.  
STM-1 Frame Structure 
The figure below shows the STM-1 frame structure.  
Path Overhead (9 Bytes)
1 Column
STM-1 Virtual Container (VC-4)
Container Capacity = 150.34 Mbps
Payload Capacity = 149.76 Mbps
260 Columns
9 Rows
2430 Bytes/Frame x 8 Bits/Byte x  8000 Frames/sec = 155.52 Mbps
Serial Signal
Stream
155.52 Mbps
2430 Bytes/Frame
9 Columns
Section
Overhead
F
F
F
F
 
STM-1 frames are transmitted at a fixed rate of 8000 frames per second.  
5. Cards and Ports 
Note 
At a transmission rate of 8000 frames per second, each byte supports a data 
rate of 64 kbps. 
The STM-1 signal frame comprises 9 rows by 270 columns, resulting in a total signal capacity of 2430 
bytes (19440 bits per frame). Considering the STM-1 frame repetition rate, 8000 frames per second, this 
yields a bit rate of 155.520 Mbps. 
The STM-1 frame comprises the following parts: 
• 
Section Overhead. The STM-1 section overhead occupies the first nine columns of the STM-1 
frame, for total of 81 bytes.  
• 
Virtual Container. The remaining 261 columns of the STM-1 frame, which contain a total of 
2349 bytes, are allocated to the virtual container. The virtual container itself comprises a 
container for the payload signal (260 columns), preceded by one column of path overhead. The 
virtual container carried in an STM-1 frame is referred to as a Virtual Container Level 4, or VC-4. 
VC-4, which is transported unchanged across the SDH network, provides a channel capacity of 
150.34 Mbps.  
The VC-4 structure includes one column (9 bytes) for the VC-4 path overhead, leaving 260 
columns of signal carrying capacity (149.76 Mbps). This carrying capacity is sufficient for 
transporting a 139.264 Mbps tributary signal (the fourth level in the PDH signal hierarchy). The 
VC-4 signal carrying capacity can also be subdivided, to permit the transport of multiple 
lower-level PDH signals. 
Pointers 
In the figure above, the VC-4 appears to start immediately after the section overhead part of the STM-1 
frame.  
Actually, to facilitate efficient multiplexing and cross-connection of signals in the SDH network, VC-4 
structures are allowed to float within the payload part of STM-1 frames. This means that the VC-4 may 
begin anywhere within the STM-1 payload part. The result is that in most cases, a given VC-4 begins in 
one STM-1 frame and ends in the next. 
Were the VC-4 not allowed to float, buffers would be required to store the VC-4 data up to the instant it 
can be inserted in the STM-1 frame. These buffers (called slip buffers), which are often used in PDH 
multiplex equipment, introduce long delays. Moreover, they also cause disruptions in case a slip occurs. 
Identifying VC-4 Beginning in the STM-1 Frame 
When a VC-4 is assembled into the STM-1 frame, a pointer (byte) located in the section overhead of the 
STM-1 frame indicates the location of the first byte (J1) of the VC-4 that starts in that STM-1 frame.  
5. Cards and Ports 
Using Pointers to Correct Timing Differences  
SDH network are intended to operate as synchronous networks. Ideally, this means that all SDH network 
nodes should derive their timing signals from a single master network clock. However, in practical 
applications, network implementation must accommodate timing differences (clock offsets). These may 
be the result of an SDH node losing network timing reference and operating on its standby clock, or it 
may be caused by timing differences at the boundary between two separate SDH networks.  
The VC-4 is allowed to float freely within the space made available for it in the STM-1 frame, therefore 
phase adjustments can be made as required between the VC-4 and the STM-1 frame. 
To accommodate timing differences, the VC-4 can be moved (justified), positively or negatively three 
bytes at time, with respect to the STM-1 frame. This is achieved by simply recalculating and updating the 
pointer value at each SDH network node. In addition to clock offsets, updating the pointer will also 
accommodate any other adjustment required between the input SDH signal rate and the timing 
reference of the SDH mode. 
Pointer adjustments introduce jitter. Excessive jitter on a tributary signal degrades signal quality and 
may cause errors. Therefore, SDH networks must be designed to permit reliable distribution of timing to 
minimize the number of pointer adjustments. 
SDH Overhead Data 
SDH Overhead Data Types 
In SDH networks, a transmission path can include three equipment functions:  
• 
SDH terminal multiplexer – which performs the insertion/removal of tributary signals into SDH 
frames 
• 
SDH cross-connect switch – permits to change the routing of tributary signals carried in SDH 
frames 
• 
Regenerator – used to increase the physical range of the transmission path. 
The resulting structure of an SDH transmission path is shown below. 
5. Cards and Ports 
SDH
Terminal
Multiplexer
VC
Assembly
SDH
Terminal
Multiplexer
Tributary
Signals
...
Tributary
Signals
...
Multiplexer
Section
Regenerator
Section
Regenerator
Section
Regenerator
Section
Multiplexer Section
VC
Disassembly
Path
SDH Cross-Connect
 
As shown above, a transmission path can comprise three types of segments: 
• 
Multiplexer section – a part of a transmission path located between a terminal multiplexer and 
an adjacent SDH cross-connect equipment, or between two adjacent SDH terminal multiplexers. 
• 
Regenerator section – a part of a transmission path located between a terminal multiplexer or 
SDH cross-connect equipment and the adjacent regenerator, or between two adjacent 
regenerators. A multiplexer section can include up to three regenerator sections. 
• 
Path – the logical connection between the point at which a tributary signal is assembled into its 
virtual container, and the point at which it is disassembled from the virtual container.  
To provide the support and maintenance signals associated with transmission across each segment, 
each of these segments is provided with its own overhead data, hence three types of overhead data: 
• 
Section overhead, carried in the first nine columns of the STM-1 frame: 
 
Multiplexer section (MS) overhead – carried in overhead rows 5 to 9  
 
Regenerator section (RS) overhead – carried in overhead rows 1 to 3 
 
AU pointers– carried in overhead row 4. 
• 
Path overhead, carried in the first column of a VC-4. The path overhead carried in the VC-4 is 
called high-order path overhead; see the Error! Reference source not found. section for a 
description of the low-order path overhead.  
The following figure shows the detailed structure of the overhead data in STM-1 frames. 
5. Cards and Ports 
Framing
A1
Framing
A1
Framing
A1
Framing
A2
Framing
A2
Framing
A2
ID
C1
BIP-8
B1
Orderwire
E1
User
F1
DCC
D1
DCC
D2
DCC
D3
Pointer
H1
Pointer
H2
Pointer
H3
Pointer
H3
Pointer
H3
B2
APS
K1
APS
K2
DCC
D4
DCC
D5
DCC
D6
DCC
D7
DCC
D8
DCC
D9
DCC
D10
DCC
D11
DCC
D12
Z1
Z1
Z1
Z2
Z2
Z2
Orderwire
E2
B2
B2
Path
Overhead
Path Trace
J1
BIP-8
B3
Signal Label
C2
Path Status
G1
User Channel
F2
Multiframe
H4
Z3
Z4
Z5
Bytes reserved for future use
Framing
A1
Multiplex
Section
Overhead
(Rows 5 - 9)
Regenerator
Section
Overhead
(Rows 1 - 3)
Section Overhead
BIP-24
AU Pointers
(Row 4)
 
Regenerator Section Overhead (RSOH)  
A regenerator section of an SDH network comprises the transmission medium and associated 
equipment between a network element and the adjacent regenerator, or between two adjacent 
regenerators. The associated equipment includes the aggregate interfaces and SDH processing 
equipment which either originates or terminates the regenerator section overhead. 
The functions of the various bytes carried in the STM-1 regenerator section overhead are described 
below. 
Framing (A1, A2 Bytes) 
The six framing bytes carry the framing pattern, and are used to indicate the start of an STM-1 frame.  
5. Cards and Ports 
Channel Identifier (C1 Byte) 
The C1 byte is used to identify STM-1 frames within a higher-level SDH frame (STM-N, where the 
standardized values of N are 4, 16, etc.). The byte carries the binary representation of the STM-1 frame 
number in the STM-N frame. 
Parity Check (B1 Byte) 
A 8-bit wide bit-interleaved parity (BIP-8) checksum is calculated over all the bits in the STM-1 frame, to 
permit error monitoring over the regenerator section. The computed even-parity checksum is placed in 
the RSOH of the following STM-1 frame. 
Data Communication Channel (D1, D2, D3 Bytes) 
The 192 kbps Data Communication Channel (DCC) provides the capability to transfer network 
management and maintenance information between regenerator section terminating equipment.  
Orderwire Channel (E1 Byte) 
The E1 byte is used to provide a local orderwire channel for voice communications between 
regenerators and remote terminal locations. 
User Communication Channel (F1 byte) 
The F1 byte is intended to provide the network operator with a channel that is terminated at each 
regenerator location, and can carry proprietary communications. 
The information transmitted on this channel can be passed unmodified through a regenerator, or can be 
overwritten by data generated by the regenerator. 
AU Pointers (H1, H2, H3 bytes)  
The AU (Administration Unit) pointer bytes are used to enable the transfer of STM-1 frames within 
STM-N frames, and therefore are processed by multiplexer section terminating equipment. Separate 
pointers are provided for each STM-1 frame in an STM-N frame.  
AU pointer function is to link between the section overhead and the associated virtual container(s).  
Multiplexer Section Overhead (MSOH)  
A multiplexer section of an SDH network comprises the transmission medium, together with the 
associated equipment (including regenerators) that provide the means of transporting information 
5. Cards and Ports 
between two consecutive network nodes (e.g., SDH multiplexers). One of the network nodes originates 
the multiplexer section overhead (MSOH) and the other terminates this overhead. 
The functions of the various bytes carried in the STM-1 multiplexer section overhead are described 
below. 
Parity Check (B2 Bytes) 
A 24-bit wide bit-interleaved parity (BIP) checksum is calculated over all the bits in the STM-1 frame 
(except those in the regenerator section overhead). The computed checksum is placed in the MSOH of 
the following STM-1 frame. 
Protection Switching (K1, K2 Bytes) 
The K1 and K2 bytes carry the information needed to activate/deactivate the switching between the 
main and protection paths on a multiplexer section. 
Data Communication Channel (D4 to D12 Bytes) 
Bytes D4 to D12 provide a 576 kbps data communication channel (DCC) between multiplexer section 
termination equipment. This channel is used to carry network administration and maintenance 
information.  
Orderwire Channel (E2 Byte) 
The E2 byte is used to provide a local orderwire channel for voice communications between multiplexer 
section terminating equipment. 
Alarm Signals 
Alarm information is included as part of the MSOH. These functions are explained in the Error! 
Reference source not found. section below. 
VC-4 Path Overhead Functions 
The path overhead (POH) is contained within the virtual container portion of the STM-1 frame. The POH 
data of the VC-4 occupies all the 9 bytes of the first column. The functions of the various bytes carried in 
the VC-4 path overhead are described below. 
Path Trace Message (J1 Byte)  
The J1 byte is used to repetitively transmit a 64-byte string (message). The message is transmitted one 
byte per VC-4 frame.  
5. Cards and Ports 
A unique message is assigned to each path in an SDH network. Therefore, the path trace message can be 
used to check continuity between any location on a transmission path and the path source.  
Parity Check (B3 Byte) 
An 8-bit wide bit-interleaved parity even checksum, used for error performance monitoring on the path, 
is calculated over all the bits of the previous VC-4. The computed value is placed in the B3 byte. 
Signal Label (C2 Byte) 
The signal label byte, C2, indicates the structure of the VC-4 container. The signal label can assume 256 
values, however two of these values are of particular importance: 
• 
The all “0”s code represents the VC-4 unequipped state (i.e., the VC-4 does not carry any 
tributary signals)  
• 
The code “00000001” represents the VC-4 equipped state. 
Path Status (G1 Byte) 
The G1 byte is used to send status and performance monitoring information from the receive side of the 
path terminating equipment to the path originating equipment. This allows the status and performance 
of a path to be monitored from either end, or at any point along the path. 
Multiframe Indication (H4 byte) 
The H4 byte is used as a payload multiframe indicator, to provide support for complex payload 
structures, for example payload structures carrying multiple tributary units (TUs – see the Error! 
Reference source not found. section). If, for example, the TU overhead is distributed over four TU 
frames, these four frames form a TU multiframe structure. The H4 byte then indicates which frame of 
the TU multiframe is present in the current VC-4. 
User Communication Channel (F2 Byte) 
The F2 byte supports a user channel that enables proprietary network operator communications 
between path terminating equipment. 
Alarm Signals 
Alarm and performance information is included as part of the path overhead. These functions are 
explained in Error! Reference source not found. section below. 
5. Cards and Ports 
SDH Tributary Units  
The VC-4 channel capacity, 149.76 Mbps, has been defined specifically for the transport of a fourth level 
(139.264 Mbps) PDH multiplex signal.  
To enable the transport and switching of lower-rate tributary signals within the VC-4, several special 
structures, called Tributary Units (TUs), have been defined. The characteristics of each TU type have 
been specifically selected to carry one of the standardized PDH signal rates. In addition, a fixed number 
of whole TUs may be mapped within the container area of a VC-4. 
Tributary Unit Frame Structure 
The structure of the tributary unit frame is rather similar to the SDH frame structure. With reference to 
the figure above, the tributary unit frame also includes a section overhead part and a virtual container 
part, which comprises a container and path overhead. 
In general, the tributary unit frame is generated in three steps: 
• 
A low rate tributary signal is mapped into the TU “container” 
• 
Low-path path overhead is added before the container, to form the corresponding virtual 
container (VC-11, VC-12, VC-2 or VC-3, depending on the TU type) 
• 
A TU pointer is added to indicate the beginning of the VC within the TU frame. This is the only 
element of TU section overhead. 
The TU frame is then multiplexed into a fixed location within the VC-4. 
Because of the byte interleaving method, a TU frame structure is distributed over four consecutive VC-4 
frames. It is therefore more accurate to refer to the structure as a TU multiframe. The phase of the 
multiframe structure is indicated by the H4 byte contained in the VC-4 path overhead. 
Tributary Unit Types 
As mentioned above, specific containers (C), virtual containers (VC) and associated TU structures have 
been defined for each standard PDH multiplex signal level. These structures are explained below: 
• 
TU-11: Each TU-11 frame consists of 27 bytes, structured as 3 columns of 9 bytes. At a frame 
rate of 8000 Hz, these bytes provide a transport capacity of 1.728 Mbps and will accommodate 
the mapping of a North American DS1 signal (1.544 Mbps). 84 TU-11s may be multiplexed into 
the STM-1 VC-4.  
• 
TU-12: Each TU-12 frame consists of 36 bytes, structured as 4 columns of 9 bytes. At a frame 
rate of 8000 Hz, these bytes provide a transport capacity of 2.304 Mbps and will accommodate 
the mapping of a CEPT 2.048 Mbps signal. 63 TU-12s may be multiplexed into the STM-1 VC-4. 
5. Cards and Ports 
• 
TU-2: Each TU-2 frame consists of 108 bytes, structured as 12 columns of 9 bytes. At a frame 
rate of 8000 Hz, these bytes provide a transport capacity of 6.912 Mbps and will accommodate 
the mapping of a North American DS2 signal. 21 TU-2s may be multiplexed into the STM-1 VC-4. 
• 
TU-3: Each TU-3 frame consists of 774 bytes, structured as 86 columns of 9 bytes. At a frame 
rate of 8000 Hz, these bytes provide a transport capacity of 49.54 Mbps and will accommodate 
the mapping of a CEPT 34.368 Mbps signal or a North American 44.768 DS3 signal. Three TU-3s 
may be multiplexed into the STM-1 VC-4. 
The following figure illustrates the assembly (multiplexing) of TUs in the VC-4 structure, for the specific 
case of the TU-12. For other multiplexing options, see below. 
VC-4 Path Overhead
260 Columns
9 Rows
Serial Signal
Stream
155.52 Mbps
2430 Bytes/Frame
Section
Overhead
TU-12 No.2
to
TU-12 No.62
9 Columns
1 Column
TU-12
No. 63
TU-12
No. 1
F
F
F
F
 
As shown above, 63 TU-12s can be packed into the 260 columns of payload capacity (i.e., the C-4 
container) provided by a VC-4. This leaves 8 columns in the C-4 container unused. These unused 
columns result from intermediate stages in the TU-12 to VC-4 multiplexing process, and are filled by 
fixed stuffing bytes. 
SDH Multiplexing Hierarchy 
The following figure shows a general view of the SDH multiplexing hierarchy. The hierarchy illustrates 
both the European and North American PDH multiplex levels. 
The figure also shows the utilization of additional SDH signal structures: 
• 
TUG: tributary unit group, is the structure generated by combining several lower level 
tributaries into the next higher level tributary. For example, TUG-2 is generated by combining 3 
TU-12, and TUG-3 is generated by combining 7 TUG-2.  
5. Cards and Ports 
• 
AU: administrative unit, is a structure that includes a VC and a pointer to the beginning of the 
VC. For example, AU-3 contains one VC-3 and includes a pointer to the beginning of the VC. 
• 
AUG: administrative unit group, is the structure generated by combining several lower level 
administrative units into the next higher level administrative unit. For example, AUG for the 
STM-1 level is generated by combining 3 AU-3 (several AUG can be combined for generating 
STM-N (N = 4, 16, etc.) structures). 
Note 
For simplicity, reference is made only to VCs (the actual structure needed to 
transport a VC can be found from the SDH or SONET multiplexing hierarchy). 
 
VC-12
Mapping
Pointer Processing
C-12
TU-12
VC-3
AU-3
VC-4
AU-4
AUG
STM-1
(155.520 Mbps)
x3
Legend
TUG-2
 x7
x3
x1
2.048 Mbps
(E1)
 
SDH Multiplexing Hierarchy  
The flexibility of the SDH multiplexing approach is illustrated by the many paths that can be used to 
build the various signal structures. For example, the figure above shows that the STM-1 signal can be 
generated by the following multiplexing paths: 
• 
Each E1 signal is mapped into a VC-12, which is then encapsulated in a TU-12.  
• 
Each group of 3 TU-12 is combined to obtain a TUG-2 (3 E1 signals per TUG-2.) 
• 
Seven TUG-2 are combined to obtain one TUG-3 (21 E1 signals per TUG-3). TUG-3 is carried in a 
VC-3. 
• 
Three VC-3 are combined to generate one VC-4 (63 E1 signals per VC-4). The STM-1 signal carries 
one VC-4.  
SDH Maintenance Signals and Response to Abnormal Conditions 
The maintenance signals transmitted within the SDH signal structure are explained: 
5. Cards and Ports 
SDH Maintenance Signal Definitions 
Signal 
Description 
Loss of Signal (LOS)  
LOS state entered when received signal level drops below the value at which an 
error ratio of 10-3 is predicted. 
LOS state exited when 2 consecutive valid framing patterns are received, provided 
that during this time no new LOS condition has been detected 
Out of Frame (OOF)  
OOF state entered when 4 or 5 consecutive SDH frames are received with invalid 
(errored) framing patterns. Maximum OOF detection time is therefore 625 µs. 
OOF state exited when 2 consecutive SDH frames are received with valid framing 
patterns 
Loss of Frame (LOF)  
LOF state entered when OOF state exists for up to 3 ms. If OOFs are intermittent, 
the timer is not reset to zero until an in-frame state persists continuously for 
0.25 ms. 
LOF state exited when an in-frame state exists continuously for 1 to 3 ms 
Loss of Pointer (LOP)  
LOP state entered when N consecutive invalid pointers are received where N = 8, 9 
or 10. 
LOP state exited when 3 equal valid pointers or 3 consecutive AIS indications are 
received. 
Note: The AIS indication is an “all 1’s” pattern in pointer bytes. 
 
Multiplexer Section AIS 
Sent by regenerator section terminating equipment (RSTE) to alert downstream 
MSTE of detected LOS or LOF state. Indicated by STM signal containing valid RSOH 
and a scrambled “all 1’s” pattern in the rest of the frame. 
Detected by MSTE when bits 6 to 8 of the received K2 byte are set to “111” for 3 
consecutive frames. Removal is detected by MSTE when 3 consecutive frames are 
received with a pattern other than “111” in bits 6 to 8 of K2. 
Far End Receive Failure 
(FERF or MS-FERF)  
Sent upstream by multiplexer section terminating equipment (MSTE) within 250 µs 
of detecting LOS, LOF or MS-AIS on incoming signal. Optionally transmitted upon 
detection of excessive BER defect (equivalent BER, based on B2 bytes, exceeds 10-3). 
Indicated by setting bits 6 to 8 of transmitted K2 byte to “110”. 
Detected by MSTE when bits 6 to 8 of received K2 byte are set to “110” for 3 
consecutive frames. Removal is detected by MSTE when 3 consecutive frames are 
received with a pattern other than “110” in bits 6 to 8 of K2. 
Transmission of MS-AIS overrides MS-FERF 
5. Cards and Ports 
Signal 
Description 
AU Path AIS 
Sent by MSTE to alert downstream high order path terminating equipment (HO PTE) 
of detected LOP state or received AU Path AIS. Indicated by transmitting “all 1’s” 
pattern in the H1, H2, H3 pointer bytes plus all bytes of associated VC-3 and VC-4). 
Detected by HO PTE when “all 1’s” pattern is received in bytes H1 and H2 for 3 
consecutive frames. Removal is detected when 3 consecutive valid AU pointers are 
received  
High Order Path Remote 
Alarm Indication  
(HO Path RAI, also known 
as HO Path FERF)  
Generated by high order path terminating equipment (HO PTE) in response to received 
AU path AIS. Sent upstream to peer HO PTE. Indicated by setting bit 5 of POH G1 byte to 
“1”. 
Detected by peer HO PTE when bit 5 of received G1 byte is set to “1” for 10 
consecutive frames. Removal detected when peer HO PTE receives 10 consecutive 
frames with bit 5 of G1 byte set to “0” 
TU Path AIS 
Sent downstream to alert low order path terminating equipment (LO PTE) of 
detected TU LOP state or received TU path AIS. Indicated by transmitting “all 1’s” 
pattern in entire TU-1, TU-2 and TU-3 (i.e., pointer bytes V1-V3, V4 byte, plus all 
bytes of associated VC-1, VC-2 and VC-3 loaded by “all 1’s” pattern). 
Detected by LO PTE when “all 1’s” pattern received in bytes V1 and V2 for 3 
consecutive multiframes. Removal is detected when 3 consecutive valid TU pointers 
are received. 
Note: TU Path AIS is only available when generating and/or receiving “floating 
mode” tributary unit payload structures. 
 
Low Order Path Remote 
Alarm Indication  
(LO Path RAI, also known as 
LO Path FERF)  
Generated by low order path terminating equipment (LO PTE) in response to 
received TU Path AIS. Sent upstream to peer LO PTE.  
Indicated by setting bit 8 of LO POH V5 byte to “1”. 
Detected by peer LO PTE when bit 8 of received V5 byte is set to “1” or 10 
consecutive multiframes. Removal detected when peer LO PTE receives 10 
consecutive multiframes with bit 8 of V5 byte set to “0”. 
Note: LO Path RAI is only available when generating and/or receiving “floating 
mode” tributary unit payload structures. 
 
This section describes the response to the wide range of conditions that can be detected by the 
maintenance means built into the SDH frames, and the flow of alarm and indication signals.  
The following figure provides a graphical representation of the flow of alarm and indication signals 
through an SDH transmission path. 
5. Cards and Ports 
LO PTE
HO PTE
MS TE
RS TE
MS TE
HO PTE
LO PTE
RAI
(VS)
BIP-2
(VS)
FEBE
(VS)
RAI
(G1)
FERF
(X2)
LOS
LOF
LOS
LOF
AIS (X2)
AIS
(H1H2)
Tributary
AIS
RAI  (G1)
RAI (VS)
B1(BIP-8)
B2(BIP-24)
B1(BIP-8)
B3(BIP-8)
FEBE
(G1)
FEBE
(G1)
FEBE
(VS)
Collection
Transmission
Generation
Legend
Low Order Path
High Order Path
Multiplexer Section
Regenerator
Section
Regenerator
Section
AIS
(V1V2)
LOP
LOP
LOP
LO
Low Order
HO
High Low Order
PTE
Path Terminating Equipment
RS TE
Regenerator Section Terminating Equipment
MS TE
Multiplexer Section Terminating Equipment
 
Flow of Alarm and Indication Signals through an SDH Transmission Path 
Flow of Alarm and Response Signals  
The major alarm conditions such as Loss of Signal (LOS), Loss of Frame (LOF), and Loss of Pointer (LOP) 
cause various types of Alarm Indication Signals (AIS) to be transmitted downstream.  
In response to the detection of an AIS signals, and detection of major receiver alarm conditions, other 
alarm signals are sent upstream to warn of trouble downstream: 
5. Cards and Ports 
• 
Far End Receive Failure (FERF) is sent upstream in the multiplexer overhead after multiplexer 
section AIS, or LOS, or LOF has been detected by equipment terminating in a multiplexer section 
span;  
• 
A Remote Alarm Indication (RAI) for a high order path is sent upstream after a path AIS or LOP 
condition has been detected by equipment terminating a path 
• 
A Remote Alarm Indication (RAI) for a low order path is sent upstream after low order path AIS 
or LOP condition has been detected by equipment terminating a low order path. 
Performance Monitoring  
Performance monitoring at each level in the maintenance hierarchy is based on the use of the byte 
interleaved parity (BIP) checksums calculated on a frame by frame basis. These BIP checksums are sent 
downstream in the overhead associated with the regenerator section, multiplexer section and path 
maintenance spans.  
In response to the detection of errors using the BIP checksums, the equipment terminating the 
corresponding path sends upstream Far End Block Error (FEBE) signals. 
SONET Environment 
SONET (Synchronous Optical Network) is an alternative standard to SDH, widely used in North America 
and other parts of the world. SONET uses similar implementation principles, and even the frame 
structures are quite similar to those used by SDH. Therefore, the following description is based on the 
information already presented for SDH. 
The following figure shows the SONET multiplexing hierarchy. 
Mapping
Pointer Processing
Legend
STS-3
(155.520 Mbps)
STS-3
STS-1
VT
Group 
 
STS-1
SPE
1.544 Mbps
(DS1)
VT1.5
VT1.5
SPE
x3
x7
x4
 
SONET Multiplexing Hierarchy  
The designations of the main signal structures in the SONET hierarchy are as follows: 
• 
Containers are replaced by Synchronous Payload Envelopes (SPE) for the various virtual 
tributaries (VTs) 
5. Cards and Ports 
• 
Virtual containers (VCs) are replaced by virtual tributaries (VTs), however the rates are similar to 
those used in the SDH hierarchy 
• 
Tributary unit groups (TUGs) are replaced by virtual tributary groups 
• 
The VC-3 level is replaced by the Synchronous Transport Signal level 1 (STS-1), and has the same 
rate (51.840 Mbps). 
• 
3 STS-1 can be combined to obtain one Synchronous Transport Signal level 3 (STS-3) at the same 
rate as STM-1 (155.520 Mbps). The corresponding optical line signal is designated OC-3. 
SDH/SONET Interfaces 
Each CL.2 module has two STM-1/OC-3/STM-4/OC-12 ports. The ports can be ordered with the following 
interfaces: 
• 
STM-1/OC-3:155.52 Mbps ±20 ppm 
• 
STM-4/OC-12: 622.08 Mbps ±20 ppm 
The panels and terminal identification for the STM-1/OC-3 and STM-4/OC-12 versions are identical. The 
bit rate for the STM-4/OC-12 version is set by means of the speed parameter. 
The framer operating mode, SDH or SONET, is selected by software configuration. The two modules 
must always use the same mode, and therefore selecting the mode for one module automatically 
switches the other to the same mode.  
Each port has an SFP socket that provides the physical interface. RAD offers a wide range of SFPs 
covering requirements from short-range low-cost optical interfaces to long-range, high-performance 
interfaces. Optical SFPs are terminated in LC connectors. RAD also offers SFPs with electrical interfaces 
for intra-office applications. 
The port interfaces support the enhanced digital diagnostic monitoring interface per SFF-8472, which 
enables collecting status and performance data from the SFPs, as well as alerting if abnormal conditions 
might cause damage or performance degradation. 
SFPs are hot-swappable, and can be replaced in the field. This enables upgrading the network port 
interface characteristics as network topology changes. 
Automatic Laser Shutdown  
For safety, Megaplex-4 uses automatic laser shutdown (ALS), which protects against accidental exposure 
to laser radiation in case of fiber breaks or disconnections. This is achieved by automatically switching 
off the transmitter of an SDH/SONET interface when the receiver of the same interface reports loss of 
the optical signal. To enable automatic recovery, the transmitter is periodically turned back on, for a 
5. Cards and Ports 
short time. If the receive signal does not reappear, the transmitter is turned back off; if the receive 
signal reappears, the transmitter remains on (normal operation). 
Inband Management Access through SDH/SONET Networks 
The following figure illustrates the inband management access through SDH/SONET networks. The 
inband management is done via the Data Communication Channel (DCC) carried in the SDH/SONET 
overhead. Each SDH/SONET link can have its DCC used for management. DCC ports use the host IP 
address of the Megaplex-4 management subsystem.  
Note 
Inband management can also support more complex topologies, such as rings. 
However, this is possible only if the carrier’s SDH/SONET network provides 
access to the DCC and enables transparent transfer of user data through the 
DCC. In this case, a Telnet host or an SNMP-based network management 
station connected to one of the Megaplex-4 units in the network can manage 
all the other units, inband. 
Typically, the Telnet host or management station is connected to a CL Ethernet port of the local 
Megaplex-4 unit. To enable remote management, the management traffic not addressed to the internal 
management subsystem of the Megaplex-4 is also connected by this subsystem to the DCCs carried by 
the other SDH/SONET links connected to the Megaplex-4. 
At the remote Megaplex-4 units, the management traffic is extracted from the DCC and connected to 
the local unit management subsystem. This arrangement enables the management station to manage 
each remote Megaplex-4 unit. 
5. Cards and Ports 
SDH/
SONET
 
Megaplex-4100
Megaplex-4100
Megaplex-4100
Network
Management
Station
CL
CL
CL
 
Inband Management Access through SDH/SONET Networks  
As mentioned above, the inband management traffic is carried in the DCC bytes, as part of the 
SDH/SONET overhead. The user can select the DCC bytes to carry the traffic, which are named 
differently for SDH and SONET environments. 
SDH: 
• 
Regenerator DCC bytes (D1, D2, D3), which provide a 192 kbps channel terminated at SDH 
regenerator section terminating equipment 
• 
Multiplex DCC bytes (D4 to D12), which provide a 576 kbps channel terminated at SDH multiplex 
section terminating equipment. 
SONET: 
• 
Section DCC bytes (D1, D2, D3), which provide a 192 kbps channel terminated at SONET 
regenerator section terminating equipment  
• 
Line DCC bytes (D4 to D12), which provide a 576 kbps channel terminated at SONET multiplex 
section terminating equipment. 

## Factory Defaults (SDH/SONET Parameters)  *(p.380)*

5. Cards and Ports 
You can also select the encapsulation and routing protocols used for inband management parameters: 
• 
Two encapsulation options are available: HDLC, or PPP over HDLC in accordance with RFC1661 
and RFC1662. 
For compatibility with particular implementations of the HDLC encapsulation protocol for 
management purposes, you can select the Type 1 flavor (for this flavor, the LCP (Link Control 
Protocol) packets do not include address and control fields in their overhead). 
• 
Two options are also available for the management traffic routing protocol: 
 
RAD proprietary protocol. This protocol is sufficient for managing any RAD equipment 
and should always be used with HDLC encapsulation.  
 
RIP2: the Megaplex-4 transmits RIP2 routing tables. This permits standard RIP routers to 
reach the Megaplex-4 SNMP agent through the inband (DCC) channel. The RIP2 network 
is limited to 14 nodes.  
SDH/SONET Hierarchy and Allowed Activities 
The Megaplex-4 CLI architecture follows the SDH/SONET hierarchy. The kinds of activities available on 
each SDH/SONET hierarchical level are listed below: 
Activities 
SDH/SONET 
AUG/OC-3 
TUG-3/STS-1 
VC-12/VT-1.5 
Configuring Port Parameters 
v 
- 
- 
- 
Assigning VC Profile 
- 
v 
- 
- 
Activating Loopbacks   
v 
v 
v 
v 
Displaying Status 
v 
v 
v 
v 
Displaying Statistics 
v 
v 
v 
v 
The following sections explain how these activities are performed. 
Factory Defaults (SDH/SONET Parameters) 
Megaplex-4 is supplied with all SDH/SONET ports enabled. Other parameter defaults are listed in the 
table below.  
Parameter  
Default Value 
frame-type  
sdh  
speed  
155mbps 

## Configuring an SDH/SONET Link  *(p.381)*

5. Cards and Ports 
Parameter  
Default Value 
dcc 
disabled 
dcc mode  
d1-to-d3  
dcc routing-protocol  
none  
dcc deviation  
standard  
threshold eed   
1e-3  
threshold sd  
1e-6  
j0-pathtrace direction 
tx  
j0-pathtrace padding  
nulls  
j0-pathtrace string  
www.rad.com  
rdi-on-failure 
enabled 
tim-response 
enabled 
automatic-laser-shutdown 
disabled 
loopback 
disabled 
Tx-ssm 
enabled 
Configuring an SDH/SONET Link  
 To configure external SDH/SONET parameters: 
1. Navigate to configure port sdh-sonet <slot>/<port> to select the SDH/SONET port to configure. 
The config>port>sdh-sonet>(<slot>/<port># prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning short description to 
port 
name <string> 
Using no name removes the name 
Administratively enabling port 
no shutdown 
Using shutdown disables the port 
Setting the type of operation in 
accordance with the SDH or 
SONET standards   
frame-type {sdh | sonet}  
 
 
5. Cards and Ports 
Task 
Command 
Comments 
Selecting the SDH/SONET port 
speed and operating mode 
speed {155mbps | 622mbps}  
155mbps: STM-1 (SDH)/OC-3 (SONET) 
622mbps: STM-4 (SDH)/OC-12 (SONET)  
Enabling DCC inband 
management and configuring DCC 
parameters: encapsulation 
protocol and the DCC bytes used 
to carry inband management 
traffic 
dcc [encapsulation {hdlc | 
ppp-o-hdlc | type1}] [mode 
{d1-to-d3 | d4-to-d12}] 
[routing-protocol 
{ none | prop-rip | rip2}] 
[deviation {standard | type1} 
See Error! Reference source not found. 
above for parameter explanation. Using no 
dcc disables inband management  
See also Configuring Inband Management 
in Chapter 8 for important considerations 
on selecting the routing protocol. 
Selecting EED (error rate 
degradation) and SD (signal 
degrade) thresholds 
threshold [eed {1e-3 | 1e-4 | 
1e-5}] [sd {1e-6 | 1e-7 | 1e-8 
| 1e-9}]  
If the selected BER value is exceeded, 
Megaplex-4 generates the relevant (EED or 
SD) alarm 
Enabling the checking of the 
receive/transmit path trace label 
by the port and configuring the 
optional path trace direction and 
padding (when the path label is 
shorter than the required length 
of 15 characters)  
j0-pathtrace [direction { tx | 
rx-tx }] [string <path-trace-
string> ] [padding {spaces | 
nulls }] 
 
Using no j0-pathtrace disables the 
checking  
 
Enabling RDI (remote defect 
indication) sending in case of 
failure 
rdi-on-failure 
 
The SDH fault conditions are: 
• LOS (loss of SDH signal) 
• LOF (loss of SDH frame)  
• AIS (alarm indication signal) 
Using no rdi-on-failure disables RDI 
sending 
Enabling the sending of RDI 
indications by the port, in case 
the received path trace label 
(carried in SDH overhead byte J0) 
is different from the expected 
path trace label 
tim-response 
 
Using no tim-response disables sending of 
RDI indications  
Enabling automatic laser 
shutdown of optical laser link on 
sync loss   
automatic-laser-shutdown  
 
Using no automatic-laser-shutdown 
disables automatic shutdown  
5. Cards and Ports 
Task 
Command 
Comments 
Defines the administrative unit 
group (AUG)         
    
aug <aug number>  
This option is valid only when 
frame-type=sdh. 
Possible values: 
• for speed=155mbps: 1  
• for speed=622mbps: 1 to 4  
See also Assigning VC Profiles to 
AUG/OC-3 below 
Enabling SSM transmission 
tx-ssm  
 
Defines an OC-3 connection 
oc3 <oc3 number> 
This option is valid only when 
frame-type=sonet. 
Possible values: 
• for speed=155mbps: 1  
• for speed=622mbps: 1 to 4  
See also Assigning VC Profiles to 
AUG/OC-3 below 
Configuring collection of 
performance management 
statistics for this port, which are 
presented via the RADview 
Performance Management portal 
 
pm-collection interval 
<seconds> 
You can enable PM statistics collection for 
all sdh-sonet ports rather than enabling it 
for individual ports. In addition to enabling 
PM statistics collection for the ports, it 
must be enabled for the device. Refer to 
the Performance Management section in 
the Monitoring and Diagnostics chapter 
for details. 
 
Example 
This example illustrates how to configure an SDH Port with management via DCC (Dedicated 
Communication Channel). 
1. Program SDH Port 1 in Slot CL-A and configure DCC management with the following parameters: 
 
Speed: 155 Mbps 
 
DCC encapsulation protocol:  HDLC 
 
DCC bytes used to carry inband management traffic: D1 – D3 
config>slot# cl-a card-type cl cl2-622gbe  
config>port# sdh-sonet cl-a/1 no shutdown 
config>port# sdh-sonet cl-a/1 frame-type sdh 
config>port# sdh-sonet cl-a/1 speed 155mbps  
config>port# sdh-sonet cl-a/1 dcc encapsulation hdlc mode d1-to-d3 

## Assigning VC Profiles to AUG/OC-3  *(p.384)*

5. Cards and Ports 
2. Configure router interface 3, address 10.10.10.9, subnet mask 24  
config>router 1 interface 3 address 10.10.10.9/24 
3. Bind SDH port 1 on CL-A  to router interface 2  
config>router# 1 interface 3 bind sdh-sonet cl-a/1 
The inband management connectivity via DCC is established. 
Assigning VC Profiles to AUG/OC-3  
 To assign a VC profile to AUG: 
1. Navigate to configure port sdh-sonet <slot>/<port> to select the SDH port to configure. 
The config>port>sdh-sonet>(<slot>/<port># prompt is displayed.  
2. Set frame-type to sdh. 
3. Enter the aug command followed by the desired aug number (1 for 155 Mbps, 1 to 4 for 622 
Mbps). 
The config>port>sdh-sonet(<slot>/<port>)> aug(number)# prompt is displayed. 
4. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning user-defined VC profile 
to the port  
vc profile <profile name> 
For creating VC profiles, see VC Profiles. 
Using no vc removes the profile  
Before you assign the user-defined profile, 
you must use the no vc command to 
remove the automatical tug-structure/ 
hvc-laps/hvc-gfp profile assignement 
 To assign a VC Profile to OC-3: 
1. Navigate to configure port sdh-sonet <slot>/<port> to select the SONET port to configure. 
The config>port>sdh-sonet>(<slot>/<port>)# prompt is displayed.  
2. Set frame-type to sonet. 
3. Enter the oc3 command followed by the desired OC-3 number (1 for 155 Mbps, 1 to 4 for 622 
Mbps). 
The config>port>sdh-sonet(<slot>/<port>)> oc3(number)# prompt is displayed. 

## Configuration Errors  *(p.385)*

5. Cards and Ports 
4. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning user-defined VC profile 
to the port  
vc profile <profile name> 
For creating VC profiles, see VC Profiles.  
Using no vc removes the profile  
Before you assign the user-defined profile, 
you must use the no vc command to 
remove the automatical tug-structure/ 
hvc-laps/hvc-gfp profile assignement  
Configuration Errors 
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 
SDH/SONET Configuration Error Messages 
Code 
Type 
Syntax 
Meaning 
300 
Error 
TOO MUCH VCS/VTS 
The maximum number of virtual containers that can be used 
by one virtually concatenated group cannot exceed 63 for 
VC-12, or 64 for VT1.5  
301 
Error 
MINIMUM NUMBER OF 
VCs/VTs IS 2  
The minimum number of virtual containers (VC-12 or VT-1.5) 
in a group is 2 
302 
Error 
VC GROUP IS NOT CONNECTED 
 
The virtually concatenated group is not bound to any other 
entity. Check and correct 
303 
Error 
DIFFERENT CLS FRAME 
STRUCTURE 
The two CL modules installed in the Megaplex-4 must use 
the same link standards (either SDH or SONET) 
305 
Error 
MISSING E1-I/T1-I SDH-SONET 
CROSS CONNECT 
An E1-i/T1-i  port is opened on CL.2 but not cross-connected 
to VC/VT on SDH/SONET.   
307 
Error 
ILLEGAL VCG MAPPING 
The virtually concatenated group mapping is not correct 
309 
Error 
E1-I/T1-I PORT IS AT 
SHUTDOWN 
e1-i/t1-i port cannot be cross-connected when it is in 
shutdown state. Set the port to no shutdown 
5. Cards and Ports 
Code 
Type 
Syntax 
Meaning 
311 
 
Error 
ILLEGAL BINDING 
Pay attention to the following:  
• A VCG and a VC-VT container bound to it must belong to 
the same CL module (A or B). 
• A Logical MAC and a GFP/HDLC port bound to it must 
belong to the same CL module (A or B). 
• A GFP/HDLC port and a VCG bound to it must belong to 
the same CL module (A or B). 
• A GFP/HDLC port defined as “no shutdown” must be 
bound to a Logical MAC 
• A VCG port defined as “no shutdown” must be bound to 
a GFP/HDLC port. 
312 
Error 
ILLEGAL SDH/SONET CROSS 
CONNECT  
Pay attention to the following: 
• An E1-i/T1-i port and a VC-VT container cross-connected 
with it must belong to the same CL module (A or B). 
• A VCG over N*VC-3 and a VC-12 cannot be mixed on the 
same AU-4. If a mix on the same AU-4 is needed,  map 
the VC-12 on the 1st TUG-3 in this AU-4.  
313 
Error 
NUMBER OF LIMITED VC-VT X-
CONNECTS EXCEEDED 
Pay attention to the following: 
• Number of vc-vt containers per CL module is limited to 
252.  
• Number of vc-vt containers for EoS per CL module is 
limited to 128.  
5. Cards and Ports 
Code 
Type 
Syntax 
Meaning 
314 
Error 
ASSIGNMENT/NUMBER OF VC 
MISMATCH 
One of the following: 
•  Mismatch between the link speed (155mbps/622mbps) 
and the number of virtual containers defined. The 
numbers should not exceed the following ranges: 
SDH: 
<port 1..2> 
aug <aug number 1..4> (1 for STM-1) 
tug3 <tug3 number 1..3> 
vc12 <tug2 number 1..7> 
<tributary number 1..3> 
SONET: 
<port 1..2> 
oc3 (<oc3 number 1..4> (1 for OC-3) 
sts1 (<sts1 number 1..3> 
vt1-5 (<tug2 number 1..7> 
 <tributary number 1..4>). 
• A VC cannot be bound/cross-connected simultaneously 
to multiple sources (VCG port, E1-i/T1-i port, etc).          
315 
Error 
VCAT NUMBER OF VCs LIMITED 
TO 64 
The maximum number of virtual containers (VC-12 or VT-
1.5)  that can be bound to one VCG cannot exceed 64  
316 
Error 
GFP/HDLC PORT CAN BE 
BOUND TO SINGLE VC-VT ONLY 
A GFP or HDLC port of the CL module can be bound only to a 
single vc-vt container. 
317 
Error 
VC-PROFILE DOES NOT MATCH 
PORT TYPE 
The VC profile content does not match the port type. 
318 
Error 
WRONG LCAS PARAMETER 
One of the LCAS parameters does not match one of the VCG 
parameters. 
320 
Warning WTR VALUE WILL BE SET TO 
ALL VC-PATH GROUPS 
Changing Wait-To-Restore time in VC-PATH groups affects 
all other configured VC-PATH groups.  

## Viewing SDH/SONET Status Information  *(p.388)*

5. Cards and Ports 
Code 
Type 
Syntax 
Meaning 
776 
Error 
INSUFFICIENT BUS 
BANDWIDTH 
 
When SDH/SONET services are activated, the maximum 
number of activated TUG-2 ports is 60 for all the I/O 
modules. Due to this restriction on PDH bus occupancy, the 
maximum number of ports supported on all I/O modules in 
the chassis is as follows: 
When CL is assembled with SDH/SONET ports, the 
communication between CL and I/O modules is over 
proprietary PDH links, terminated by SDH/SONET framer 
with maximum 60 activated TUG-2 ports. Due to this 
restriction on PDH bus occupancy, the maximum number of 
ports supported on all I/O modules in the chassis is as 
follows: 
• 180 E1 ports 
• 240 T1 ports 
• 180 or 240 DS1 ports depending on the respective 
service (E1 or T1). 
Viewing SDH/SONET Status Information  
For viewing the status of the SDH/SONET hierarchical entities, follow the instructions below. 
 To view the status of an SDH/SONET port: 
1. Navigate to config>port>sdh-sonet> (<slot>/<port>)#  
2. Type show status. 
The status is displayed, for example as follows:  
config>port>sdh-sonet(cl-a/1)# show status 
Name                  : CL-A sdh-sonet 01 
Administrative Status : Up 
Operational Status    : Down 
 
Rx Quality                                     : DNU 
Tx Quality                                     : SEC 
Connector Type                                 : SFP Out 
 
Trace Message (J0) 
----------------------------------------------------------------- 
Received                                     : 
 
5. Cards and Ports 
 
 To view the SFP status: 
1. Navigate to config>port>sdh-sonet> (<slot>/<port>)#  
2. Type show sfp-status. 
The SFP status is displayed, for example as follows:  
 
 
SFP 
--------------------------------------------------------------- 
Connector Type                : LC 
Vendor Name                   :  
Vendor Part Number            : CT-0155TSP-MB5L 
Typical Maximum Range (Meter) : 15000 
Wave Length (nm)              : 1310 
Fiber Type                    : SM 
 
RX Power (dBm)              : -50.0 dBm 
TX Power (dBm)              : -12.0 dBm 
Laser Bias (mA)             : 14.0 mA 
Laser Temperature (Celsius) : 47.0 C 
Power Supply (V)            : 3.3 V 
Note 
The last 5 rows are displayed only for SFPs with built-in DDM functionality. 
The table below explains the parameters of the SFP installed for selected port. 
Link SFP Parameters  
Parameter 
Description 
Connector Type 
Displays the SFP connector type, for example, LC, SC, SC/APC, FC, etc.  
Manufacturer Name 
Displays the original manufacturer’s name 
Vendor PN 
Displays the original vendor’s part number 
Typical Max. Range 
(Meter) 
Displays the maximum range expected to be achieved over typical optical fibers, in 
meters 
Wave Length (nm) 
Displays the nominal operating wavelength of the SFP, in nm 
Fiber Type 
Displays the type of optical fiber for which the SFP is optimized: SM (single mode) or MM 
(multi mode) 
TX Power (dBm) 
Displays the current optical power, in dBm, transmitted by the SFP 
RX Power (dBm) 
Displays the current optical power, in dBm, received by the SFP 
5. Cards and Ports 
Parameter 
Description 
Laser Bias (mA) 
Displays the measured laser bias current, in mA 
Laser Temperature 
(Celcius) 
Displays the measured laser temperature, in °C 
Power Supply (V) 
Displays the SFP power supply voltage  
 To view the status of an AUG-3/OC-3: 
1. Navigate to: 
 
SDH: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
aug (<aug number 1..4> )# 
 
SONET: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
oc3 (<oc3 number 1..4># 
2. Type show status. 
The status is displayed, for example as follows:  
config>port>sdh-sonet(cl-a/1)>aug(1)# show status 
 
General 
------------------------------------------------------------Expected Trace Message (J1) 
: www.rad.com 
Received Trace Message (J1) : www.rad.com 
Expected Signal Label       : 0x1B 
Received Signal Label       : 0x1B        
Loopback Type               : None  
 
 To view the status of a TUG-3/STS-1: 
1. Navigate to: 
 
SDH: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
aug (<aug number 1..4> ) 
tug3 (<tug3 number 1..3>)# 
 
SONET: 
5. Cards and Ports 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
oc3 (<oc3 number 1..4>  
sts1 (<sts1 number 1..3>) # 
2. Type show status. 
The status is displayed, for example as follows:  
config>port>sdh-sonet(cl-a/1)>oc3(1)>sts1(2)# show status 
General 
--------------------------------------------------------------- 
Expected Trace Message (J1) : www.rad.com 
Received Trace Message (J1) : www.rad.com 
Expected Signal Label       : 0x02 
Received Signal Label       : 0x02 
Loopback Type               : None 
 To view the status of a VC-12/VT-1.5: 
1. Navigate to: 
 
SDH: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
aug (<aug number 1..4> ) 
tug3 (<tug3 number 1..3>) 
vc12 (<tug2 number 1..7>)/<tributary number 1..3>)#  
 
SONET: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
oc3 <oc3 number 1..4>)  
sts1 <sts1 number 1..3>)  
vt1-5 <tug2 number 1..7>)/ <tributary number 1..4>)#. 
2. Type show status. 
The status is displayed, for example as follows:  
config>port>sdh-sonet(cl-a/1)>oc3(1)>sts1(2)>vt1.5(1/1)# show status 
General 
--------------------------------------------------------------- 
Expected Trace Message (J2) : www.rad.com 
Received Trace Message (J2) : www.rad.com 
Expected Signal Label       : 0x05 
Received Signal Label       : 0x05 
Loopback Type               : None 

## Testing SDH/SONET Ports  *(p.392)*

5. Cards and Ports 
Testing SDH/SONET Ports  
Megaplex-4 features remote loopbacks on the SDH/SONET ports of the CL.2 modules, local loopbacks on 
AUG/OC-3 and TUG-3/STS-1 and remote loopbacks on AUG/OC-3, TUG-3/STS-1 and VC-12/VT-1.5. The 
following sections briefly describe each type of loopback. The figure below shows the paths of the 
signals when each loopback is activated.  
SDH/SONET Loopbacks  
Diagnostic 
Function 
Megaplex-4100
DS1
Cross-Connect
Matrix
CL
E1/T1
Mapper
SDH/
SONET
Framer
1
........
E1-i/T1-i 
Framers
2
SDH/SONET Interface 
VC/VT
Matrix
I/O Port
 
  
Remote 
loopback on 
SDH/SONET link  
 
 
 
 
 
 
Local loopbacks 
on AUG/OC-3, 
TUG-3/STS-1,  
VC-12/VT-1.5 
 
 
 
 
VC/VT 
Matrix
 
Remote 
loopbacks on 
AUG/OC-3, 
TUG-3/STS-1,  
VC-12/VT-1.5  
 
 
 
 
VC/VT 
Matrix
 
 
 
 
Framer
5. Cards and Ports 
Remote Loopback on SDH/SONET Link  
As shown in the figure above, the remote loopback is activated within the network side circuits of the 
SDH/SONET framer, and therefore the loopback signal paths includes all the circuits of the local 
Megaplex-4 SDH/SONET interface but very few of the framer circuits.  
When the remote loopback is activated, the received SDH/SONET signal is processed by the receive path 
of the local Megaplex-4 SDH/SONET interface and then returned to the input of the transmit path 
through the framer. Therefore, when the remote loopback is activated on the external port, the receive 
signal is returned to the remote unit. To correct transmission distortions, the returned signal is 
regenerated by the SDH/SONET interface circuits. 
The remote loopback should be activated at only one of the two units interconnected by the 
SDH/SONET link, otherwise an unstable situation occurs.  
Local Loopback on AUG/OC-3, TUG-3/STS-1, VC-12/VT-1.5  
As shown in the figure above, the local loopback is activated within the SDH/SONET VC cross-connect 
matrix. When the local loopback is activated, the transmit signal is returned to the receive path before 
the output to the SDH/SONET framer, at different points for each entity.  
While the loopback is activated, the equipment mapped to the corresponding E1-i/T1-i port of the local 
Megaplex-4 must receive its own signal, and thus it must be frame-synchronized.  
Note 
The local loopback on VC-12/VT-1.5 is supported for unframed E1/T1 or VC-
12/VT-1.5 ports mapped to VCG ports. It is not supported for VC-12/VT-1.5 
ports mapped to E1-i/T1-I ports of CL modules. 
Remote Loopback on AUG/OC-3, TUG-3/STS-1, VC-12/VT-1.5  
As shown in above, the remote loopback on AUG/OC-3, TUG-3/STS-1, or VC-12/VT-1.5 is activated 
within the network side circuits of the VC/VT cross-connect matrix. Therefore, the loopback signal path 
includes all the circuits of the local Megaplex-4 SDH/SONET interface and framer, but very few of the 
other circuits.  
When the remote loopback is activated, the received SDH/SONET signal is processed by the receive path 
of the local Megaplex-4 SDH/SONET interface and then returned to the input of the transmit path 
through the framer. Therefore, when the remote loopback is activated on the external port, the receive 
signal is returned to the remote unit.  
The remote loopback should be activated only after checking that the equipment connected at the 
remote side to the tested unit operates normally during a local loopback. In this case, the remote unit 
5. Cards and Ports 
must receive its own signal, and thus it must be frame-synchronized. The effect on the ports of the 
remote unit is mixed, as explained above for the local loopback. 
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the Megaplex-4. 
Therefore, when you initiate a loopback, you have the option to limit its duration to a selectable interval 
in the range of 1 through 60 minutes.  
After the selected interval expires, the loopback is automatically deactivated without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-4 before 
this timeout expires. When using inband management, always use the timeout option; otherwise, the 
management communication path may be permanently disconnected. 
The default is infinite duration (without timeout). 
Activating Loopbacks  
 To perform a loopback on the SDH/SONET port: 
1. Navigate to configure port sdh-sonet <slot>/<port> to select the SDH/SONET port to be tested. 
The config>port>sdh-sonet>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Activating the remote 
loopback and setting its 
duration (in minutes) 
loopback {remote} [duration 
<duration in minutes 1..60> ]  
Using no loopback remote disables the 
loopback   
Default (without duration parameter) is 
infinite loopback 
 To perform a loopback on the AUG/OC-3 port: 
• 
From the config>port>sdh-sonet> (<slot>/<port 1..2>) 
aug (<aug number 1..4>) or config>port>sdh-sonet> (<slot>/<port 1..2>) 
oc3 (<oc3 number 1..4>) # context, activate the loopback as follows:  
Task 
Command 
Comments 
Activating the local or 
remote loopback on this 
aug/oc3 port 
loopback { remote | local}  
 
Using no loopback followed by the 
corresponding command disables the 
loopback   
5. Cards and Ports 
 To perform a loopback on the TUG-3/STS-1 port: 
1. Navigate to: 
 
SDH: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
aug (<aug number 1..4>)  
tug3 (<tug3 number 1..3>)#  
 
SONET: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
oc3 (<oc3 number 1..4>)  
sts1 (<sts1 number 1..3>) # 
2. Activate the loopback as follows:  
Task 
Command 
Comments 
Activating the local or 
remote loopback on this 
tug3/sts1  
loopback {remote | local}  
 
Using no loopback followed by the 
corresponding command disables the 
loopback   
 To perform a loopback on the VC-12/VT-1.5:  
1. Navigate to: 
 
SDH: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
aug <aug number 1..4>  
tug3 <tug3 number 1..3>) 
vc12 <tug2 number 1..7>)/<tributary number 1..3>)#  
 
SONET: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
oc3 (<oc3 number 1..4>) 
sts1 (<sts1 number 1..3>)  
vt1-5 (<tug2 number 1..7>)/ <tributary number 1..4>)#. 
2. Activate the loopback as follows:  
Task 
Command 
Comments 
Activating the remote 
loopback on this vc12/vc1-5  
loopback remote  
Using no loopback remote disables the 
loopback   

## Displaying SDH/SONET Statistics  *(p.396)*

5. Cards and Ports 
Displaying SDH/SONET Statistics  
SDH/SONET ports of Megaplex-4 feature the collection of statistical diagnostics at different hierarchical 
levels, per ANSI T1.403.  
Note 
Only locally-terminated entities (AUG/OC-3, TUG-3/STS-1, VC-12/VT-1.5) are 
monitored by Megaplex-4. 
 To display the SDH/SONET port statistics: 
• 
At the prompt config>slot>port>sdh-sonet (<slot><port>)#, enter show statistics followed by 
parameters listed below.  
 To display the AUG/OC-3 statistics: 
1. Navigate to: 
 
SDH: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
aug (<aug number 1..4> )# 
 
SONET: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
oc3 (<oc3 number 1..4> )# 
2. Enter show statistics followed by parameters listed in the table below. 
 To display the TUG-3/STS-1 statistics: 
1. Navigate to: 
 
SDH: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
aug (<aug number 1..4>)  
tug3 (<tug3 number 1..3>)# 
 
SONET: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
oc3 (<oc3 number 1..4>)  
sts1 (<sts1 number 1..3>) # 
2. Enter show statistics followed by parameters listed in the table below. 
5. Cards and Ports 
 To display the VC-12/VT-1.5 statistics: 
1. Navigate to: 
 
SDH: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
aug <aug number 1..4>  
tug3 <tug3 number 1..3>) 
vc12 <tug2 number 1..7>)/<tributary number 1..3>)#  
 
SONET: 
config>port>sdh-sonet> (<slot>/<port 1..2>) 
oc3 (<oc3 number 1..4>)  
sts1 (<sts1 number 1..3>)  
vt1-5 (<tug2 number 1..7>)/ (<tributary number 1..4>)#. 
2. Enter show statistics followed by parameters listed in the table below. 
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
 
 
SDH/SONET statistics are displayed.  The counters are described in the tables below. For 
example: 
Current statistics: 
config>port>sdh-sonet(cl-a/1)# show statistics current 
Current 
--------------------------------------------------------------- 
Time Elapsed (Sec) : 222 
Valid Intervals    : 2 
ES                 : 0 
SES                : 0 
SEFS               : 0 
CV                 : 0 
Statistics for interval 67: 
config>port>sdh-sonet(cl-a/1)# show statistics interval 67 
 
Interval  
5. Cards and Ports 
--------------------------------------------------------------- 
Interval Number : 67 
Section ES      : 0 
Section SES     : 0 
Section SEFS    : 31 
Section CV      : 0 
All statistics: 
config>port>sdh-sonet(cl-a/1)>oc3(1)>sts1(2)>vt1.5(1/1)# show statistics all 
Current 
--------------------------------------------------------------- 
Time Elapsed (Sec) : 712 
Valid Intervals    : 1 
ES                 : 0 
SES                : 0 
UAS                : 0 
CV                 : 0 
 
Interval 
-------------------------------------------------------------- 
Interval Number : 1 
ES              : 3 
SES             : 2 
UAS             : 57 
CV              : 0 
 
5. Cards and Ports 
SDH/SONET Port Statistics Parameters – Current 15-Minute Interval 
Parameter 
Description 
ES  
Displays the number of errored seconds in the current 15-minute interval. 
An errored second is any second containing one or more of the following types of errors: 
• Severely Errored Frame (SEF) defect (also called Out-of-Frame (OOF) event): 
A SEF defect is declared after detection of four contiguous errored frame 
alignment words.  
The SEF defect is terminated when two contiguous error-free frame words are 
detected.  
• Loss of Signal (LOS) defect: 
A LOS defect is declared after no transitions are detected in the incoming line 
signal (before descrambling) in an interval of 2.3 to 100 microseconds. 
The LOS defect is terminated after a 125-microsecond interval (one frame) in 
which no LOS defect is detected.  
• Loss of Pointer (LOP) defect: 
A LOP defect is declared after no valid pointer is detected in eight consecutive 
frames. The LOP defect will not be reported while an AIS signal is present. 
The LOP defect is terminated after a valid pointer is detected.  
• Alarm Indication Signal (AIS) received in the SDH overhead. 
• Coding Violation (CV): a coding violation is declared when a Bit Interleaved Parity (BIP) 
error is detected in the incoming signal. The BIP information is collected using the B1 
byte in the Section Overhead. 
SEFS (UAS)  
Displays the number of unavailable seconds (UAS (SEFS)) in the current interval. 
An unavailable second is any second in which one or more SEF defects have been 
detected. 
SES  
Displays the number of severely errored seconds (SES) in the current interval. 
A SES is any second in which multiple error events of the types taken into consideration 
for an ES have occurred. 
CV 
Displays the number of coding violations (CV) in the current interval. 
Time elapsed 
The elapsed time (in seconds) since the beginning of the current interval. The range is 1 
to 900 seconds  
Valid Intervals 
The number of elapsed finished 15-min intervals for which statistics data can be 
displayed, in addition to the current (not finished) interval (up to 96) 