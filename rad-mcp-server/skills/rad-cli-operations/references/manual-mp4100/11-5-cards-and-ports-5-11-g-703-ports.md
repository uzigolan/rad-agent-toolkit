# 5 Cards and Ports – 5.11 G.703 Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 323–327.*


## Applicability and Scaling  *(p.323)*


## Standards Compliance  *(p.323)*


## Functional Description  *(p.323)*

5. Cards and Ports 
The statistics for the specified port are cleared. 
5.10 E1-i, T1-i Ports 
See Error! Reference source not found. and T1 Ports sections, respectively.  
5.11 G.703 Ports 
Applicability and Scaling 
G.703 ports denote G.703 codirectional links of VS-6/703 modules.  
Standards Compliance 
ITU-T Rec. G.703, Section 1.1.4.1  
Functional Description 
The 64 kbps codirectional interface is defined by ITU-T Rec. G.703, Section 1.1.4.1 and has the following 
functions: 
• 
Bidirectional transfer of data signals 
• 
Transfer of 64 kHz bit clock signals associated with the data signals 
• 
Transfer of 8 kHz byte clock signals associated with the data signals. 
ITU-T Rec. G.703, Section 1 describes three different versions for 64 kbps interfaces, which differ mainly 
in the type and direction of the clock signals, and the number of wires used.  
The term codirectional describes an interface that transmits the information and the associated timing 
signals in the same direction. The interface uses four wires (two twisted pairs), one pair for the transmit 
direction and the other pair for the receive direction). Each pair carries both the data and the associated 
clock signals. 
5. Cards and Ports 
The following figure illustrates the flow of signals across the interface. 
RECEIVER
TRANSMITTER
TRANSMITTER
RECEIVER
Transmit Data and
Associated Timing
Receive Data and
Associated Timing
 
The 64 kbps co-directional interface transfers data at a nominal rate of 64 kbps, and a maximum rate 
tolerance of 100 ppm. The interface uses two balanced twisted pairs having a nominal impedance of 
120Ω. The transmit pulse shape, measured across a 120Ω resistive load impedance, is nominally 
rectangular. A mark is represented by a peak voltage of 1.0V, and a space is represented by a voltage of 
0 ±0.10V. The nominal pulse width is 3.9 μsec. The maximum line attenuation that should be 
compensated for by the receiver is 3 dB at up to 128_kHz. 
The interface supports the delineation of byte intervals. The signal waveform uses coding to carry both 
clock and timing information, and to obtain a signal with essentially zero DC component. The coding is 
performed in the following steps, illustrated in the figure below: 
• 
Step 1: The basic 64 kbps bit period is divided into four unit intervals. 
• 
Step 2: A binary “one” is encoded as a block of the following four symbols: 1100. A binary “zero” 
is encoded as a block of the following four symbols: 1010. 
• 
Step 3: The binary signal is converted into a three-level signal by alternating the polarity of 
consecutive blocks (to ensure DC balance). 
• 
Step 4: To mark the start and end of a byte, the alternation in polarity of the blocks is violated 
every eighth block. The violation block marks the last bit in a byte. 
 

## Factory Defaults  *(p.325)*


## Configuring DS0-G703 Port Parameters  *(p.325)*

5. Cards and Ports 
 
Factory Defaults  
Megaplex-4 is supplied with all ds0-g703 ports disabled.  
Configuring DS0-G703 Port Parameters  
 To configure the DS0-G703 link parameters: 
1. Navigate to configure port ds0-g703 <slot>/<port> to select the port to configure. 
The config>port> ds0-g703>(<slot>/<port>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
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

## Viewing a DS0-G703 Port Status  *(p.326)*


## Testing DS0-G703 Links  *(p.326)*

5. Cards and Ports 
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
Viewing a DS0-G703 Port Status 
Follow the instructions below for viewing the status of the DS0-G703 port 10/1 as an example. 
 To view the DS0-G703 port status: 
• 
At the config>port> ds0-g703 (<slot>/<port>)# prompt, enter show status. 
The status information appears as illustrated below.  
config>port>ds0-g703(10/1)# show status 
Name                  : VS-6/703 Link 1 
Administrative Status : Down 
Operation Status      : Down 
Loopback Type         : None 
Testing DS0-G703 Links  
The test and diagnostics functions available on each optical link are: 
• 
Local loopback on local link 
• 
Remote loopback on local link 
• 
BER test on the link 
Local Digital Loopback (Local Loop) 
The local loopback is a digital loopback performed at the digital output of a selected channel, by 
returning the transmit signal of the channel in the same timeslot of the receive path. The transmit signal 
is still sent to the remote Megaplex unit.  
While the loopback is connected, the local serial port should receive its own signal. 
The loopback signal path is shown below. 
5. Cards and Ports 
 
Remote Digital Loopback (Remote Loop) 
The remote loopback is a digital loopback performed at the digital input of the channel, by returning the 
digital received signal of the channel to the input of the transmit path. The receive signal remains 
connected to the local user, and can be received by user.  
While the loopback is connected, the remote serial port should receive its own signal. 
The loopback signal path is shown below. 
 
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the VS-6/G703 
module. Therefore, when you initiate a loopback, you have the option to limit its duration to an interval 
in the range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local module before this 