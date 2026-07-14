# Quick Start Guide

*Manual `MP-1-mn_ver 2.2.pdf`, pages 28–33.*


## Installing the Unit  *(p.28)*


## Connecting the Interfaces  *(p.28)*


## Connecting to a Terminal  *(p.28)*


## Connecting to Power  *(p.28)*

This section describes the minimum configuration needed to prepare Megaplex-1 for operation. 
Installing the Unit 
Perform the following steps to install the unit: 
1. Determine the required configuration of Megaplex-1, according to your application. 
2. Connect the interfaces as required for the application. 
3. Connect the ASCII terminal to the CONTROL port. 
4. Connect power to the unit. 
Connecting the Interfaces 
 To connect the interfaces: 
1. Connect the network port(s) to the service provider network equipment. 
2. Connect the user port(s) to the customer network equipment. 
Connecting to a Terminal 
 To connect the unit to a terminal: 
1. Connect the CBL-RJ45/D9/F/6FT cable to the CONTROL connector. 
2. Connect the other end of the CBL-RJ45/D9/F/6FT cable to a laptop equipped with an ASCII 
terminal emulation application.  
Connecting to Power 
The device can be connected to AC or DC power. 
 To connect to AC power: 
1. Connect the power cable to the power connector on Megaplex-1. 
2. Connect the power cable to the mains outlet. 

## Configuring the Unit for Management  *(p.29)*


## Starting a Terminal Session for the First Time  *(p.29)*

Megaplex-1 
The unit turns on automatically. 
 To connect to DC power: 
1. Wire the AC/DC plug to the power cable, and connect it to the unit.  
2. Connect the power cable to the mains outlet. 
The unit turns on automatically. 
Configuring the Unit for Management 
Configure Megaplex-1 for management, using a local ASCII-based terminal. 
Starting a Terminal Session for the First Time 
 To start the terminal session: 
1. Make sure all Megaplex-1 cables and connectors are properly connected. 
2. Turn on the control terminal or start the PC terminal emulation program to create a new 
terminal connection. 
3. Configure the PC communication port parameters to a baud rate of 9.6 kbps, 8 bits/character, 1 
stop bit, no parity and no flow control. 
4. Set the terminal input delay between characters to at least 10 msec. 
5. Power-up the unit.  
6. Megaplex-1 boots up. When the startup process is completed, you are prompted to press 
<ENTER> to receive the login prompt. 
7. Press <ENTER> until you receive the login prompt. 
8. To log in, enter your user name (su for full configuration and monitoring access) and your 
password. 
9. The device prompt appears: 
MP-1# 
You can now type the necessary CLI commands. 
Note 
RAD recommends using the 115.2 kbps data rate for CLI management 
sessions.  
10. Navigate to config>terminal# prompt and change the default terminal baud rate (9.6 kbps) to 
115.2 kbps. 

## Configuring Management Flows  *(p.30)*

Megaplex-1 
11. Configure the PC communication port parameters to a baud rate of 115.2 kbps to match the 
new Megaplex-1 setting. 
12. Continue with product configuration. 
Configuring Management Flows 
To manage the Megaplex-1 from a remote NMS, you must first preconfigure the basic parameters using 
a supervision terminal connected to the Megaplex-1 CONTROL port. RAD recommends Layer-3 
management access via the out-of-band Ethernet management port. 
 To preconfigure Megaplex-1 for Layer-3 management access: 
1. Add an SVI. 
2. Create classifier profiles for matching all traffic. 
3. Add a flow (with reverse direction) connecting out-of-band Ethernet management port and the 
SVI. 
4. Add a router interface, bind it to the SVI, and (if required) add a static route to the next hop. 
5. Configure SNMPv3 parameters:  
 
OID tree visibility, mask and type 
 
Access group 
 
Trap report policy. 
The following script provides all necessary configuration steps. Replace IP addresses and entity names 
with values relevant for your network environment.  
#***************Configuring Management Port and Adding_SVI******************** 
configure 
port 
     mng-ethernet 0/0 
       no shutdown 
       exit 
     svi 1 
       no shutdown 
       exit 
           exit         
#*********************************End**************************************** 
 
#***************************Configuring_Flows******************************** 
configure flows 
classifier-profile all match-any 
     match all 
     exit 
Megaplex-1 
flow 1 
     classifier all 
     ingress-port mng-ethernet 0/0 
     egress-port svi 1 
     reverse-direction 
     no shutdown 
     exit                                                                     
                    
exit 
#**********************************End*************************************** 
 
#*********************Configuring_Router_Interface*************************** 
configure router 1 interface 1 
address 172.18.219.116/24 
bind svi 1 
no shutdown 
exit 
static-route 0.0.0.0/0 address 172.18.219.1  
arp-timeout 1200 
 
#**********************************End*************************************** 
 
#*********************Configuring_SNMP_View/Mask/Type************************ 
configure management snmp 
view internet 1 
mask 1 
type included 
no shut 
exit all 
#**********************************End*************************************** 
 
#*********************Configuring_SNMP_Access_Group************************ 
configure management snmp 
access-group initial usm no-auth-no-priv 
context-match prefix 
exit all 
#**********************************End*************************************** 
 
#**************************Configring_SNMP_Traps***************************** 
configure management snmp 
target-params p 
message-processing-model snmpv3 
version usm 
security name initial level no-auth-no-priv 
no shutdown 
exit 
target a 
target-params p 
tag-list unmasked 

## Saving Management Configuration  *(p.32)*


## Saving Configuration  *(p.32)*


## Copying User Configuration to Default Configuration  *(p.32)*


## Verifying Connectivity  *(p.32)*


## Configuring Services  *(p.32)*

Megaplex-1 
address udp-domain 172.17.176.35 
no shutdown 
exit 
notify unmasked 
tag unmasked 
no shutdown 
exit all 
#**********************************End************************************ 
Saving Management Configuration 
Saving Configuration 
Type save in any level to save your configuration in startup-config.  
Copying User Configuration to Default Configuration 
In addition to saving your configuration in startup-config, you may also wish to save your configuration 
as a user default configuration. 
 To save user default configuration: 
• 
Enter the following commands: 
exit all  
file copy startup-config user-default-config 
Verifying Connectivity 
At the ASCII terminal, ping the IP address assigned to management router interface and verify that 
replies are received. If there is no reply to the ping, check your configuration and make the necessary 
corrections. 
Configuring Services 
Proceed with service configuration. Chapter 4 details different scenarios for provisioning supported 
Ethernet and TDM services. 
 
 
Megaplex-1 
 