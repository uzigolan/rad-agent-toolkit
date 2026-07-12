# 5 Cards and Ports – 5.23 Teleprotection Ports (Physical)

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 439–448.*


## Applicability and Scaling  *(p.439)*


## Functional Description  *(p.439)*


## Factory Defaults  *(p.439)*

5. Cards and Ports 
5.23 Teleprotection Ports (Physical)  
Applicability and Scaling 
The TP module supports up to 4 command inputs and 8 outputs, enabling teleprotection equipment to 
utilize the advanced transport capabilities offered by Megaplex. 
It also includes two independent groups of CMD channels: 
• 
East – CMD channels 1 (working) and 2 (protection) 
• 
West – CMD channels 3 (working) and 4 (protection). 
The teleprotection commands can be locally output or be carried to a peer card/Megaplex over a 
TDM/SDH network or over a packet-switched network. Up to 4 commands can be carried over a single 
DS0. 
Functional Description 
See Chapter 14.  
Factory Defaults 
The Megaplex-4 is supplied with all teleprotection ports disabled. Other parameter defaults are listed in 
the table below.  
Parameter  
Description 
Default Value 
cmd-in 
input-active  
Association between the cmd-in active state and the 
supplied voltage 
high 
preset-duration 
Extended cmd-in duration period (msec) 
0  
bounce-override 
Debounce filter window time (time during  which the cmd-in 
signal is sampled, µsec) 
1000  
switching-voltage  
Switching voltage 
110  
cmd-out 
 

## Configuring CMD-IN Ports  *(p.440)*

5. Cards and Ports 
Parameter  
Description 
Default Value 
prolongation  
Minimum duration of pulse period (msec) 
0  
alarm-state-energized 
cmd-out alarm state indication 
yes 
led-latched  
LED behavior when the related command turns inactive 
no led-latched  
pulse-duration  
Maximum duration of pulse period (msec) 
0 
cmd-channel 
 
rate 
Setting cmd-channel rate  
(in kbps) 
64  
tx-address 
Tx address for recognizing and preventing wrong cross-
connect of teleprotection data in the network 
1 
rx-address 
Rx address for recognizing and preventing wrong cross-
connect of teleprotection data in the network 
2 
trigger-mode 
Teleprotection triggering mode 
speed-optimized 
oos-recovery 
Mode of recovery from sending oos code and switching back 
from the protection state 
auto 
Configuring CMD-IN Ports  
 To configure a cmd-in port: 
1. Navigate to configure port cmd-in <slot>/<port> to select the cmd-in port to configure. 
The config>port>cmd-in>(<slot>/<port>)# prompt is displayed.  
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

## Configuring CMD-OUT Ports  *(p.441)*

5. Cards and Ports 
Task 
Command  
Comments 
Setting the debounce filter 
window time (time during  
which the cmd-in signal is 
sampled)  
bounce-override  <µsec >     
0 to 32000 µsec, in 250-µsec steps  
For more information on bounce-override 
command, see Teleprotection section in 
Chapter 14. 
Setting the extended cmd-in 
duration period 
preset-duration  <msec>    
 
 
 
0 to 2000 msec, in 1-msec steps 
For more information on preset-duration 
command, see Teleprotection section in 
Chapter 14.  
Defining the association 
between the cmd-in active 
state and the supplied 
voltage 
input-active  {high | low}     
• low – low voltage means that command 
input is in active state 
• high – high voltage means that  command 
input is in active state 
Defining LED behavior when 
the related command turns 
inactive 
 
led-latched 
 
• led-latched – the LED lights once the 
related command becomes active, and 
stays on even when the command is not 
active, until explicit clear-cmd-led 
command is issued by the user 
• no led-latched – the LED follows the 
related command activity 
Clearing the led-latched state 
clear-cmd-led 
 
See also Clear-Cmd-Led Command per 
System 
Forcing the cmd-in port into 
active state, disregarding the 
actual input state 
force-active  
• Using no force-active cancels the 
command 
Selection of the switching 
voltage 
switching-voltage  
{24 |48 |110 | 125 | 220 | 250} 
 
Configuring CMD-OUT Ports  
Cmd out ports 1 to 4 always serve as primary ports. 
Cmd out ports 5 to 8 can either serve as secondary cmd-out ports or used to report internal system 
alarms to outside indicators. In the first case they are bound to the primary ports and automatically copy 
their configuration. In the second case you have to bind them to the corresponding alarms under 
reporting context by using bind-alarm-to-relay and bind-alarm-source-to-relay commands, as described 
in Chapter 11.  
5. Cards and Ports 
 To configure the cmd-out port parameters:  
1. Navigate to configure port cmd-out <slot>/<port> to select the port to configure. 
The config>port>cmd-out>(<slot>/<port>)# prompt is displayed.  
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
Setting minimum cmd-out 
signal duration (for very short 
pulses) 
prolongation <msec> 
If the received pulse period of cmd-out-i signal 
(received via cmd-channel) is shorter than this 
specific value, the cmd-out pulse duration will 
be extended to this value.  
Allowed values: 0 to 15000, with steps of 
1 msec 
If prolongation =0, the command is not 
activated and the received pulse period is not 
extended 
When cmd-out is functioning as a binary 
output port, this parameter does not appear. 
Setting maximum cmd-out 
signal duration (for very long 
pulses) 
pulse-duration <msec> 
 
If the received pulse period of cmd-out-i signal 
(received via cmd-channel) is longer than this 
specific value, the cmd-out pulse duration will 
be shortened to this value.  
Allowed values: 0 to 15000, with steps of 
1 msec 
If pulse-duration=0, the command is not 
activated and the received pulse period is not 
shortened 
When cmd-out is functioning as a binary 
output port, this parameter does not appear. 
Defining cmd-out alarm state 
indication 
alarm-state-energized {yes | 
no} 
yes – alarm state is indicated by closed cicruit 
no – alarm state is indicated by open cicruit 

## Configuring CMD-CHANNEL Ports  *(p.443)*

5. Cards and Ports 
Task 
Command  
Comments 
Defines LED behavior when 
the related command turns 
inactive 
 
led-latched 
• led-latched – the LED lights once the 
related command becomes active, and 
stays on even when the command is not 
active, until explicit clear-cmd-led 
command is issued by the user. 
• no led-latched – the LED follows the 
related command activity. 
Creating a set of ports that 
will be trigger sources for the 
current port 
trigger-bind < number> cmd-
out-i  <slot/port/tributary 
[none | or | and] 
trigger-bind < number> cmd-in  
<slot/port> [none | or | and] 
 
See Command Cross-Connect in Chapter 14. 
Using no trigger-bind < number> removes the 
set. 
“none” is default operator and can be omitted 
when only one trigger source is defined. 
When more than one trigger sources are 
defined, the operator must be either “or” or 
“and” for all trigger sources. 
Binding a secondary cmd-out 
port  to a primary cmd-out 
port 
secondary-bind <slot>/<port> 
 
Primary cmd-out ports: 1 to 4. 
Secondary cmd-out ports: 5 to 8. 
One or more secondary ports can be bound to 
one primary port. 
A cmd-out port cannot be simultaneously 
bound as Alarm Relay (see Chapter 11) and 
bound as secondary cmd-out port to a primary 
cmd-out port (the current command). 
To view the command result, use “info detail” 
command. 
Clearing the led-latched state 
clear-cmd-led 
See also Clear-Cmd-Led Command per System 
Configuring CMD-CHANNEL Ports 
 To configure the cmd-channel port parameters: 
1. Navigate to configure port cmd-channel <slot>/<port> to select the port to configure.  
The config>port>cmd-channel>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 

## Clear-Cmd-Led Command per System  *(p.444)*

5. Cards and Ports 
Task 
Command  
Comments 
Administratively enabling port 
no shutdown 
Using shutdown disables the port 
Assigning short description to port 
name <string> 
Using no name removes the name  
Setting cmd-channel rate  
(in kbps) 
rate {64 | 128} 
 
Configuring Tx address for 
recognizing and preventing wrong 
cross-connect of teleprotection data 
in the network 
tx-address   
 
The allowed values are 1 to 254. 
 
 
Configuring Rx address for 
recognizing and preventing wrong 
cross-connect of teleprotection data 
in the network 
 rx-address   
 
The allowed values are 1 to 254. 
 
Stopping transmitting the oos code 
reactivate 
For oos-recovery=manual only 
Controlling the mode of recovery 
from sending oos code and switching 
back from the protection state 
oos-recovery {auto | 
manual} 
 
• auto – when the OOS condition is over, the 
cmd-in-i port automatically stops sending 
the oos code and switches back from the 
protection state 
• manual – when the OOS condition is over, 
the oos code continues to be sent and the 
system remains in the protection state until 
the user sends “reactivate” command  
Defining teleprotection triggering 
mode 
 
trigger-mode {speed-
optimized | security-
optimized} 
• speed-optimized – one frame is enough to 
trigger command change 
• security-optimized – in order to trigger the 
command change, the value must be stable 
for at least two frames (this adds 1.5 msec 
delay)  
Clear-Cmd-Led Command per System  
The clear-cmd-led command can be performed not only for a specific port, but system-wide. 
 To clear the Latched Led state system-wide: 
1. Navigate to configure port. 
The config>port># prompt is displayed.  

## Configuration Errors  *(p.445)*

5. Cards and Ports 
2. Enter clear-cmd-led  {all | cmd-in | cmd-out} for the required ports: 
 
cmd-in – all cmd-in ports  
 
cmd-out – all cmd-out ports 
 
all – all cmd-in and cmd-out ports. 
 
The state is cleared for all the ports indicated in the command. 
Configuration Errors  
The tables below list messages generated by Megaplex-4 when a configuration error on the 
Teleprotection module is detected. 
TP Configuration Error Messages  
Code 
Type 
Syntax 
Meaning 
680 
Error 
IDENTICAL TX/RX ADDRESSES 
ARE ILLEGAL 
The Tx&Rx addresses on a cmd channel cannot be 
configured to the same value (with the exception of 254)  
681 
Error 
BOUND PORT IS IN SHUTDOWN 
STATE 
One of the following ports is in shutdown state: 
•  cmd-out-i or cmd-in port participating in trigger-bind 
command  
• cmd-out port participating in secondary-bind command 
682 
Error 
SECONDARY PORT IS BOUND 
MORE THAN ONCE 
A secondary cmd-out port can be bound to a primary cmd-
out port only once 
684 
Error 
ASSOCIATED CMD CHANNEL IS 
IN SHUTDOWN STATE 
When a cmd-in-i and/or cmd-out-i port is in “no shutdown” 
state, its associated cmd-channel ports must be also at “no 
shutdown”. 
685 
Error 
ILLEGAL LOGIC OPERATOR IN 
TRIGGER-BIND 
When more than one trigger sources are defined, the 
operator must be either “or” or “and” for all trigger sources. 
686 
Error 
ILLEGAL PORT TYPE USED IN 
TRIGGER BIND 
For cmd-out and cmd-in-i ports,  the associate trigger  port 
can be either cmd-out-i or cmd-in.              
687 
Error 
ILLEGAL SECONDARY 
SLOT/PORT BOUND 
Primary and secondary cmd-out ports bound to each other 
must reside in the same slot.   
688 
Error 
PULSE DURATION IS SHORTER 
THAN PROLONGATION 
Command prolongation must be shorter than pulse 
duration. 

## Viewing Status Information  *(p.446)*

5. Cards and Ports 
Viewing Status Information  
For viewing the status of the physical Teleprotection ports, follow the instructions below. 
 To view the status of a cmd-in port: 
1. Navigate to config>port> cmd-in> (<slot>/<port>)#  
2. Type show status. 
The status is displayed, for example as follows:  
 
config port cmd-in 4/1 show status 
Name                  : IO-4 Cmd in 01 
Administrative Status : Up 
Operation Status      : Up 
Value                 : 1 
Led                   : Latched 
Force                 : Yes 
Input Control Voltage : 220 VDC   
The status display provides information about: 
 
Administrative and operational status  
 
Value - Command value (0, 1, or N/A)  
 
Led – LED behavior when the related command turns inactive (Latched/No Latched)  
 
Force – Whether the port is in force-active state (Yes/No) 
 
Input Control Voltage (24, 48, 110, 125, 220 or 250 VDC) 
 To view the status of a cmd-out port: 
1. Navigate to config>port> cmd-out> (<slot>/<port>)#  
2. Type show status. 
The status is displayed, for example as follows:  
config port cmd-out 4/1 show status 
Name                  : IO-4 Cmd out 01 
Administrative Status : Up 
Operation Status      : Down 
Value                 : 1 
Led                   : Not Latched 
Relay Type            : Electro Mechanical  
The status display provides information about: 
 
Administrative and operational status  
 
Value – Command value (0, 1, or N/A)  
5. Cards and Ports 
 
Led – LED behavior when the related command turns inactive (Latched/No Latched)  
 
Relay Type (Electro Mechanical or Solid State). The value is identical for all cmd-out ports 
and based on the card type. 
 To view the status of a cmd-channel port: 
1. Navigate to config>port> cmd-channel> (<slot>/<port>)#  
2. Type show status. 
The status is displayed, for example as follows:  
config port cmd-channel 4/1 show status 
Name                  : IO-4 CMD Channel 01 
Administrative Status : Up 
Operation Status      : Down 
Detail Status         : No Sync 
Rx Address            : 0 
Latency (millisec)    : 2 
Protection State      : Active 
 
CMD IN I       Name                 Admin     Oper   Tx Val 
 
4/1/1          IO-4 Cmd in-i 01     Up        Up     0 
4/1/2          IO-4 Cmd in-i 01     Up        Up     0 
4/1/3          IO-4 Cmd in-i 01     Up        Up     0 
4/1/4          IO-4 Cmd in-i 01     Up        Up     0 
 
CMD OUT I      Name                 Admin    Oper   Loopback  Rx Val 
 
4/1/1          IO-4 Cmd out-i 01    Up       Up     No Loop   0 
4/1/2          IO-4 Cmd out-i 01    Up       Up     No Loop   0 
4/1/3          IO-4 Cmd out-i 01    Up       Up     No Loop   0 
4/1/4          IO-4 Cmd out-i 01    Up       Up     No Loop   0 
The status display provides information about: 
 
Administrative and operational status  
 
Detail Status: 
 
Sync – port is synchronized 
 
No Sync –port is not synchronized 
 
Address mismatch – there is a mismatch between the Rx address and the expected Tx 
address 
 
N/A – not relevant 
 
Rx Address –recieved Rx address  
 
Latency –cmd-channel data end-to-end latency  
 
Protection state for cmd-channels 1/2 and 3/4 (Active/Standby or N/A if protection not 
defined) 

## Displaying Teleprotection Statistics  *(p.448)*

5. Cards and Ports 
 
Cmd-in and cmd-out-i status (see Error! Reference source not found. for details) 
Displaying Teleprotection Statistics  
Teleprotection ports cmd-in, cmd-out and cmd-channel feature RAD proprietary statistical diagnostics. 
 To display the statistics of a cmd-in port: 
1. Navigate to config>port> cmd-in> (<slot>/<port>)#  
2. Type show statistics. 
The statistics is displayed, for example as follows:  
config port cmd-in 4/1 show statistics 
       Raw            Debounced 
Trip : 1              1 
The statistics shows the number of trips occurred before (raw) and after (debounced) debounce 
filtering.  
 To display the statistics of a cmd-out port: 
1. Navigate to config>port> cmd-out> (<slot>/<port>)#  
2. Type show statistics. 
The statistics (number of trips) is displayed, for example as follows:  
config port cmd-out 4/1 show statistics 
Trip Counter : 4  
 To display the statistics of a cmd-channel port: 
1. Navigate to config>port> cmd-channel> (<slot>/<port>)#  
2. Type show statistics. 
The statistics is displayed, for example as follows:  
config port cmd-channel 4/1 show statistics 
Frame Error : 2 
CRC Error   : 3 
 
CMD IN I             Trip Counter 
 
4/1/1                0 
4/1/2                0 
4/1/3                0 
4/1/4                0 