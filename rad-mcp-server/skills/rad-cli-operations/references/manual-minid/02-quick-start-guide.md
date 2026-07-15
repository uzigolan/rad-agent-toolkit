# Quick Start Guide

*Manual `MiNID_ver_2_6_mn.pdf`, pages 27–29.*


## Installing the Unit  *(p.27)*


## Configuring MiNID  *(p.27)*

This section describes the minimum configuration needed to prepare MiNID for operation. 
Installing the Unit 
Installing an SFP in MiNID SFP Sleeve 
Insert the required SFP into MiNID SFP sleeve (refer to Installing SFPs into the SFP Sleeve). 
Inserting MiNID SFP Sleeve into a Host Device 
Insert MiNID SFP sleeve into SFP-CA.2 or into a host device that is powered on and connected to a 
network. 
Configuring MiNID 
Initial Configuration for Management 
MiNID SFP sleeve can be configured via the SFP-CA.2 adaptor (provided that your PC has 
Windows XP SP2), or via a switch.  
Configuring via SFP-CA.2 
 To configure MiNID SFP sleeve via SFP-CA.2: 
1.
Configure the PC parameters (refer to Configuration via SFP-CA.2 in Chapter 4).
2.
Disconnect MiNID from any device (SFP-CA.2 or host).
3.
Insert any compatible SFP into MiNID.
4.
Set MiNID to Configuration mode, using its DIP switches (refer to Setting the DIP Switches).
Note 
While MiNID is in Configuration mode, it responds to the default IP address 
192.168.205.1, with no host VLAN, even if a different IP address was 
configured. 
5.
Insert MiNID into the SFP socket of the SFP-CA.2 module.
6.
Connect SFP-CA.2 to your PC via USB 2.0 port.
The Ready LED on SFP-CA.2 turns on.
SFP-CA.2 Configuration Module 
Note 
If no fiber is connected to the MSA port, ensure that all fault propagation 
actions are disabled (this is the default setting). 
Configuring via Switch 
A similar procedure to configuring via SFP-CA.2 can be used to configure MiNID when it is inserted into 
the SFP port of a switch, as long as connectivity is established to an available Ethernet port. 
 To configure MiNID via a switch: 
1.
Disconnect MiNID from any device (SFP-CA.2 or host).
2.
Insert any compatible SFP into MiNID.
3.
Set MiNID to Configuration mode, using its DIP switches (refer to Setting the DIP Switches).
Note 
While MiNID is in Configuration mode, it responds to the default IP address
192.168.205.1, with no host VLAN, even if a different IP address was
configured.
4.
Insert MiNID into an available SFP socket of the switch.
5. Connect the available switch port to which connectivity has been established, to your PC, using 
an IP address in the subnet 192.168.205.XX. 
Verifying Connectivity 
Ping the MiNID IP address (192.168.205.1). 
Preconfigure for Ethernet Service 
Using either your browser or Telnet, connect to 192.168.205.1 and log in with your user name (su for 
full configuration and monitoring access) and your password. 
Proceed with service configuration (refer to Traffic Processing for details of different scenarios for 
provisioning supported services). 
 
 