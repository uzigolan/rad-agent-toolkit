# Quick Start Guide

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 28–31.*


## Installing the Unit  *(p.28)*


## Connecting the Interfaces  *(p.28)*


## Connecting to a Terminal  *(p.28)*


## Connecting the Power  *(p.28)*

Quick Start Guide 
This section describes the minimum configuration needed to prepare Megaplex-4 for operation.  
Installing the Unit 
Perform the following steps to install the unit: 
1. Determine the required configuration of Megaplex-4, according to your application. 
2. Install the Megaplex-4 enclosure. 
3. Install the modules in accordance with the site installation plan. 
4. Connect the ASCII terminal to the RS-232 control port. 
5. Connect power to the unit. 
Connecting the Interfaces 
 To connect the interfaces: 
1. Insert the SFP modules (if applicable) into the relevant SFP-based Ethernet ports. 
2. Refer to the site installation plan, and connect the prescribed cables to the Megaplex-4 
modules. 
Connecting to a Terminal 
 To connect to an ASCII terminal:  
1. Connect one side of the cable supplied by RAD (CBL-DB9F-DB9M-STR for Megaplex-4100, CBL-
MUSB-DB9F for Megaplex-4104) to the Megaplex connector, designated CONTROL DCE. 
2. Connect the other side of the cable to the ASCII terminal equipment. 
Connecting the Power 
Connect the power cable(s) first to the connector on the PS module, and then to the power outlet. For 
DC cables, pay attention to polarity. 

## Configuring the Unit for Management  *(p.29)*


## Starting a Terminal Session for the First Time  *(p.29)*

Configuring the Unit for Management 
Configure Megaplex-4 for management, using a local ASCII-based terminal. 
Starting a Terminal Session for the First Time 
 To start the terminal session: 
1. Connect an ASCII terminal to the CONTROL DCE connector of the active CL module (use a 
straight cable). 
2. Configure the ASCII terminal to the settings listed below and then set the terminal emulator to 
VT100 emulation for optimal view of system menus. 
 
Data Rate:  
9,600 bps 
 
Data bits:  
8 
 
Parity:  
None 
 
Stop bits:  
1 
 
Flow control:  None. 
3. If you are using HyperTerminal, set the terminal mode to 132-column mode for optimal view of 
system menus (Properties> Settings> Terminal Setup> 132 column mode). 
4. Turn the power on.  
Note 
The Megaplex-4 PS modules do not include a power switch. Use an external 
power ON/OFF switch, for example, the circuit breaker used to protect the 
power lines.  
5. Wait for the completion of the power-up initialization process. During this interval, monitor the 
power-up indications: 
 
After a few seconds, Megaplex-4 starts decompressing its software.  
 
After software decompression is completed, all the indicators turn off for a few seconds 
(except for the POWER indicators) as Megaplex-4 performs its power-up initialization.  
You can monitor the decompression and initialization process on the terminal connected to the 
Megaplex-4.  
6. When the startup process is completed, you are prompted to press <Enter> to receive the login 
prompt. 
7. Press <Enter> until you receive the login prompt. 

## Configuring the Router  *(p.30)*


## Saving Management Configuration  *(p.30)*


## Saving Configuration  *(p.30)*

8. If the Megaplex-4 default user name and password have not yet been changed, log in as 
administrator using su as the user name (su for full configuration and monitoring access) and 
1234 for password. 
9. The device prompt appears: 
mp4100# 
You can now type the necessary CLI commands. 
Configuring the Router  
The router must be configured with a router interface that is bound to the SVI used for the management 
flows, and assigned an IP address. Also, a static route must be set up for the default gateway. 
This section illustrates the following configuration: 
• 
Router interface 1: 
 
Bound to SVI 1 
 
IP address 172.17.154.96 with mask 255.255.255.0 
• 
Router: Static route associated with IP address 172.17.154.1 (default gateway). 
 To define the router: 
• 
Enter the following commands: 
configure router 1 
interface 1 
bind svi 1 
# IP address 172.17.154.96 with mask 255.255.255.0 
address 172.17.154.96/24 
no shutdown 
exit 
# Default gateway 172.17.154.1 
static-route 0.0.0.0/0 address 172.17.154.1 
commit  
exit all 
Saving Management Configuration 
Saving Configuration 
Type save in any level to save your configuration in startup-config.  

## Copying User Configuration to Default Configuration  *(p.31)*


## Verifying Connectivity  *(p.31)*

Copying User Configuration to Default Configuration 
In addition to saving your configuration in startup-config, you may also wish to save your configuration 
as a user default configuration. 
 To save user default configuration: 
• 
Enter the following commands: 
exit all  
file copy startup-config user-default-config 
y 
Verifying Connectivity 
At the ASCII terminal, ping the IP address assigned to Megaplex-4 and verify that replies are received. If 
there is no reply to the ping, check your configuration and make the necessary corrections. 
 