# 5 Cards and Ports – 5.7 DS1 Optical Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 284–287.*


## Applicability and Scaling  *(p.284)*


## Standards Compliance  *(p.284)*


## Functional Description  *(p.284)*


## Factory Defaults  *(p.284)*

5. Cards and Ports 
5.7 DS1 Optical Ports  
Applicability and Scaling 
DS1 optical ports denote fiber optic links of VS-6/C37 modules.  
Standards Compliance 
IEEE C37.94 
Functional Description 
The IEEE C37.94 standard defines a programmable nx64 kbps (n = 1…12) multimode optical fiber 
interface between teleprotection and digital multiplexer equipment, for distances of up to 2 km. 
The VS-6/C37 module features a dual-port fiber optic interface, operating at a nominal wavelength of 
830 nm and nominal line rate of 2.048 Mbps. Each port is terminated in a pair of ST connectors for 
connection to standard multimode fiber. 
The fiber optic interface has a wide dynamic range, which ensures that the receiver will not saturate 
even when using short fiber optic cables (saturation is caused when the optical power applied to the 
receiver exceeds its maximum allowed input power, and results in very high bit error rates). 
The interface can be used for both user and network ports – either for inter-substation communication 
or for transmitting distance Teleprotection information. 
Factory Defaults  
Megaplex-4 is supplied with all ds1-opt ports disabled. Other parameter defaults are listed in the table 
below. 
Parameter  
Default Value 
inband-management  
no inband-management (disabled) 
inband-management – routing-protocol  
none  

## Configuring DS1 Optical Port Parameters  *(p.285)*


## Viewing a DS1-Opt Port Status  *(p.285)*

5. Cards and Ports 
Configuring DS1 Optical Port Parameters  
 To configure the DS1 optical link parameters: 
1. Navigate to configure port ds1-opt <slot>/<port> to select the port to configure. 
The config>port>ds1-opt>(<slot>/<port>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
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
Enabling inband 
management and setting 
its parameters 
 
inband-management <timeslot> protocol 
{ppp | fr} [routing-protocol {none | prop-
rip | rip2} ] 
 
VS modules only. 
ppp – synchronous PPP over HDLC 
encapsulation  
fr –Frame Relay encapsulation (under 
DLCI 100) in accordance with RFC 
2427 
See also Configuring Inband 
Management in Chapter 8 for 
important considerations on selecting 
routing protocol. 
Using no inband management  
<timeslot> disables inband 
management through this timeslot 
Viewing a DS1-Opt Port Status 
Follow the instructions below for viewing the status of the DS1-opt port 5/1 as an example. 
 To view the DS1-opt port status: 
• 
At the config>port>ds1-opt (<slot>/<port>)# prompt, enter show status. 
The status information appears as illustrated below.  
config>port>ds1-opt(5/1)# show status 
Name                  : IO-5 Ds1 Opt01 
Administrative Status : Up 

## Testing DS1 Optical Links  *(p.286)*

5. Cards and Ports 
Operation Status      : Up 
Loopback Type         : None 
Testing DS1 Optical Links  
The test and diagnostics functions available on each optical link are: 
• 
Local loopback on local optical link 
• 
Remote loopback on local optical link 
Local Digital Loopback (Local Loop) 
The local loopback is a digital loopback performed at the digital output of a selected channel, by 
returning the transmit signal of the channel in the same timeslot of the receive path. The transmit signal 
is still sent to the remote Megaplex unit.  
While the loopback is connected, the local serial port should receive its own signal. 
The loopback signal path is shown below. 
 
Remote Digital Loopback (Remote Loop) 
The remote loopback is a digital loopback performed at the digital input of the channel, by returning the 
digital received signal of the channel to the input of the transmit path. The receive signal remains 
connected to the local user, and can be received by user.  
While the loopback is connected, the remote serial port should receive its own signal. 
The loopback signal path is shown below. 
5. Cards and Ports 
 
Loopback Duration 
The activation of a loopback disconnects the local and remote equipment served by the VS-6/C37 
module. Therefore, when you initiate a loopback, you have the option to limit its duration to an interval 
in the range of 1 through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local module before this 
timeout expires. When using inband management, always use the timeout option; otherwise, the 
management communication path may be permanently disconnected. 
The default is infinite duration (without timeout). 
Activating the Loopbacks 
 To perform a loopback on the DS1 optical link: 
1. Navigate to configure port ds1-opt <slot>/<port> to select the optical link to be tested. 
The config>port>ds1-opt>(<slot>/<port>)# prompt is displayed.  
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
 