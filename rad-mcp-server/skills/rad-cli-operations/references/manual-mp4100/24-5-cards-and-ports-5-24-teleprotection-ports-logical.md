# 5 Cards and Ports – 5.24 Teleprotection Ports (Logical)

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 449–453.*


## Applicability and Scaling  *(p.449)*

5. Cards and Ports 
 
CMD OUT I            Trip Counter 
 
4/1/1                0 
4/1/2                0 
4/1/3                0 
4/1/4                0 
TP Statistics Parameters  
Parameter 
Description 
Frame Error  
Number of frame errors received on the cmd channel since last reset or power-up 
CRC Error  
Number of CRC errors received on the cmd channel since last reset or power-up 
A CRC error is declared when the CRC bits generated locally on the data in the received 
frame (protecting critical teleprotection bits) do not match the CRC bits (crc1 – crc4) 
received from the transmitter.  
 To clear the statistics on a TP port: 
1. Navigate to the corresponding port. 
2. Enter clear-statistics. 
The statistics for the specified port are cleared. 
5.24 Teleprotection Ports (Logical)  
Applicability and Scaling 
Teleprotection ports are available on TP modules. Four cmd-in-i and four cmd-out-i ports for each of 
cmd channels 1 and 3 house the logic to manipulate the logical Rx/Tx information over the 
corresponding cmd channel. This logic is capable to perform either basic transparent command cross-
connect or logical (and/or) operation between the external/logical inputs/outputs and teleprotection 
information transported over cmd channels.  
Automation cmd channels 5 and 6 can be connected to four cmd-out-i ports each. 

## Functional Description  *(p.450)*


## Factory Defaults  *(p.450)*


## Configuring CMD-IN-I Ports  *(p.450)*

5. Cards and Ports 
Functional Description 
See the Teleprotection Modules section in Chapter 14.  
Factory Defaults 
The Megaplex-4 is supplied with all teleprotection ports disabled. Cmd in-i ports have no factory 
defaults. Cmd-out-i parameter defaults are listed in the table below. 
Parameter  
Description 
Default Value 
oos-code  
The value that will be inserted to the related cmd-out output 
when the cmd-channel is in the out-of-service state 
last-valid-state 
Configuring CMD-IN-I Ports 
 To configure the cmd-in internal port parameters: 
1. Navigate to configure port cmd-in-i <slot>/<port>/<tributary> to select the port to configure. 
The config>port>cmd-in-i>(<slot>/<port>/<tributary>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
Administratively enabling 
port 
no shutdown 
Using shutdown disables the port 
Assigning short description 
to port 
name <string> 
Using no name removes the name 
Creating a set of ports that 
will be trigger sources for 
the current port 
trigger-bind < number> cmd-out-i  
<slot/port/tributary> [none | or | 
and] 
trigger-bind < number> cmd-in  
<slot/port> [none | or | and] 
 
See Command Cross-Connect in Chapter 
14. 
Using no trigger-bind < number> removes 
the set. 
“none” is default operator and can be 
omitted when only one trigger source is 
defined. 
When more than one trigger sources are 
defined, the operator must be either “or” 
or “and” for all trigger sources. 

## Configuring CMD-OUT-I Ports  *(p.451)*


## Viewing Status Information of Logical Teleprotection Ports  *(p.451)*

5. Cards and Ports 
Configuring CMD-OUT-I Ports 
 To configure the cmd-out internal port parameters: 
1. Navigate to configure port cmd-out-i <slot>/<port>/<tributary> to select the port to configure. 
The config>port>cmd-out-i>(<slot>/<port>/<tributary>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command  
Comments 
Administratively enabling 
port 
no shutdown 
Using shutdown disables the port 
Assigning short description to 
port 
name <string> 
Using no name removes the name  
Selecting the value that will 
be inserted to the related 
cmd-out output  when the 
cmd-channel is in the out-of-
service state 
oos-code {on | off | 
last-valid-state} 
off – Cmd-out is forced to off 
on  – Cmd-out is forced to on 
last-valid-state – Cmd-out takes the last valid 
state value (on or off) 
Activating remote loopback  
loopback remote [duration 
<minutes>] 
See Testing Teleprotection Ports below 
Viewing Status Information of Logical Teleprotection Ports 
For viewing the status of the logical Teleprotection ports, follow the instructions below. 
 To view the status of a cmd-out-i port: 
1. Navigate to config>port> cmd-out-i> (<slot>/<port>/<trib>)#  
2. Type show status. 
The status is displayed, for example as follows:  
config port cmd-out-i(4/1/1)# show status 
Name                  : IO-4 Cmd out-i 01 
Administrative Status : Up 
Operation Status      : Up 
Value                 : 1 
Loopback              : No Loop 
The status display provides information about:  

## Testing Teleprotection Ports  *(p.452)*

5. Cards and Ports 
 
Administrative and operational status  
 
Value - Command value (0, 1, N/A)  
 
Whether a remote loopback is active on the port. 
 To view the status of a cmd-in-i port: 
1. Navigate to config>port> cmd-in-i> (<slot>/<port>/<trib>)#  
2. Type show status. 
The status is displayed, for example as follows:  
config port cmd-in-i(4/1/1)# show status 
Name                  : IO-4 Cmd-in-i 01 
Administrative Status : Up 
Operation Status      : Up 
Value                 : 1 
The status display provides information about: 
 
Administrative and operational status  
 
Value - Command value (0, 1, N/A).  
Testing Teleprotection Ports  
The remote digital loopback in the TP module are activated from cmd-out-i ports. The loopback can be 
performed independently per each entity. 
The remote loopback is a digital loopback performed at the cmd-out-i port, by returning the received 
teleprotection signal from the communication network (cmd-channel) back to the remote RTU. This 
loopback checks network connectivity of the remote RTU. 
The diagram below shows where the loopback is implemented.  
5. Cards and Ports 
Logical AND/OR
Selected cross connect
Primary CMD selection
CMD OUT 1..4 – Primary
CMD OUT 5..8 - Secondary
CMD slot:port
CMD slot:port:tributary
CMD In #1
CMD Out #1
CMD-CH 1/2
or
or
or
or
CMD-CH 3/4
CMD-CH 1/2
CMD-CH 3/4
CMD In #2
CMD In #3
CMD In #4
CMD Out #2
CMD Out #3
CMD Out #4
CMD Out #5
CMD Out #6
CMD Out #7
CMD Out #8
CMD-OUT-I #1
CMD-OUT-I #2
CMD-OUT-I #3
CMD-OUT-I #4
CMD-OUT-I#1
CMD-OUT-I #2
CMD-OUT-I #3
CMD-OUT-I #4
CMD-IN-I #1
CMD-IN-I #2
CMD-IN-I #3
CMD-IN-I #4
CMD-IN-I #1
CMD-IN-I #2
CMD-IN-I #3
CMD-IN-I #4
Remote loopback
 
Remote Loopback Functionality inside TP Cross-Connect  
Loopback Duration 
The activation of a loopback disconnects the remote equipment served by the Megaplex-4. Therefore, 
when you initiate a loopback, you have the option to limit its duration to an interval in the range of 1 
through 30 minutes.  
After the selected interval expires, the loopback is automatically deactivated, without operator 
intervention. However, you can always deactivate a loopback activated on the local Megaplex-4 before 
this timeout expires.  
The default is infinite duration (without timeout). 