# 2 Installation and Setup

*Manual `MiNID_ver_2_6_mn.pdf`, pages 50–58.*


## 2.1 Safety  *(p.50)*

This chapter describes installation and setup procedures for MiNID SFP sleeve  and SFP units. 
After installing the unit, refer to Operation for the operating instructions. 
Housed in a Small Form Factor Pluggable (SFP) package, MiNID SFP sleeve complies with the 
Multi-Source Agreement (MSA) and can be inserted into any MSA-compatible host unit. Furthermore, 
standard SFPs can be inserted into MiNID. 
MiNID is equipped with DIP switches on its underside that enable setting the MiNID unit to various 
operation modes. Operation modes depend on the desired task and are listed in the table below 
together with the associated DIP switch settings. 
2.1 Safety  
Note 
Before installing the product, review Handling Energized Products at the 
beginning of the manual. 
 
 
Warning 
The host product must be certified and approved according to 
EN/IEC/62368-1 or UL/CSA 62368-1 standards. 
 
 
 
Avertissement 
Le produit hôte doit être certifié et approuvé conformément aux normes 
EN/IEC/62368-1 ou UL/CSA 62368-1. 
 

## 2.2 Site Requirements and Prerequisites  *(p.51)*


## 2.3 Package Contents  *(p.51)*


## 2.4 Required Equipment  *(p.51)*

2. Installation and Setup 
Laser Safety 
 
Warning 
Third-party SFP optical transceivers must be CDRH-registered and comply 
with IEC 62368-1 and IEC 60825, as well as with the local laser safety 
regulations for Class I laser equipment. 
 
 
Avertissement 
Les émetteurs-récepteurs optiques SFP tiers doivent être enregistrés auprès 
du CDRH et être conformes aux normes IEC 62368-1 et IEC 60825, ainsi 
qu'aux réglementations locales en matière de sécurité laser pour les 
équipements laser de classe I. 
2.2 Site Requirements and Prerequisites 
MiNID SFP sleeve is intended for installation in an MSA-compatible SFP socket of the host equipment. 
The ambient temperature is 0 to 50°C (32 to 122°F).  
2.3 Package Contents 
The MiNID package includes the following items: 
• 
MiNID SFP sleeve or MiNID SFP 
• 
Manual download form 
 
Note 
The SFP-CA.2 configuration adapter module for the MiNID sleeve can be 
ordered separately. 
2.4 Required Equipment 
MiNID does not require special tools for installation. 

## 2.5 Setting the DIP Switches  *(p.52)*


## 2.6 Mounting  *(p.52)*

2. Installation and Setup 
2.5 Setting the DIP Switches 
MiNID SFP Sleeve and SFP 
MiNID SFPs (sleeve and short) include a two-part DIP switch on their underside, used to select the 
working mode of the device. 
SW1
SW2
OFF
ON
 
MiNID SFP DIP Switch 
The working modes are presented in the DIP Switch Settings table below. 
DIP Switch Settings  
Switch Position 
Working Mode 
SW1 
SW2 
OFF 
OFF 
Database initialization – Reset the device database to factory default values including the 
host parameters (IP address, gateway address, VLANs, etc.). The factory default values are 
taken from the file factory-default-config.  
ON 
OFF 
Normal operation  
OFF 
ON 
For MiNID SFP sleeve:  
Software download – Download a new software version via YMODEM protocol (can be 
used only with RAD SFP-CA.2 configuration module)  
ON 
ON 
Configuration –Set the device IP address to the default IP address 192.168.205.1  
Note: This DIP switch setting is normally used by field engineers who need to access the 
device without changing database values. 
2.6 Mounting 
This section presents instructions for installing MiNID SFP sleeve.  
2. Installation and Setup 
Installing SFPs into the SFP Sleeve 
MiNID SFP sleeve provides an MSA-compatible SFP port, for installing standard SFPs.  
Note 
You must remove MiNID SFP sleeve from the host unit before you insert or 
remove an SFP from MiNID SFP sleeve (see Inserting MiNID SFP Sleeve into a 
Host Unit for instructions on removing MiNID). 
 
Third-party SFP optical transceivers must be agency-approved, complying 
with the local laser safety regulations for Class I laser equipment. 
 
 To install the SFP: 
1. Lock the wire latch of the SFP module by lifting it up until it clicks into place, as illustrated below. 
 
Note 
Some SFP models have a plastic door instead of a wire latch. 
 
 
Locking the SFP Wire Latch 
2. Carefully remove the dust covers from the SFP slot. 
3. Insert the rear end of the SFP into the socket, and push slowly backwards to mate the 
connectors until the SFP clicks into place. If you feel resistance before the connectors are fully 
mated, retract the SFP using the wire latch as a pulling handle, and then repeat the procedure. 
 
2. Installation and Setup 
Caution 
Insert the SFP gently. Using force can damage the connecting pins. 
4. Remove the protective rubber caps from the SFP modules. 
 To remove the SFP module: 
1. Disconnect the fiber optic cables from the SFP module. 
2. Unlock the wire latch by lowering it downwards (as opposed to locking). 
3. Hold the wire latch and pull the SFP module out of the Ethernet port.  
Caution 
Do not remove the SFP while the fiber optic cables are still connected. This 
may result in physical damage (such as a chipped SFP module clip or socket), 
or cause malfunction (e.g., the network port redundancy switching may be 
interrupted). 
Inserting MiNID SFP Sleeve into a Host Unit 
This section explains how to connect/eject MiNID  to/from a host device. 
You need to insert MiNID  into the host device in order to configure it via the host, or in order to operate 
it. Refer to Service Provisioning for procedures to configure MiNID via SFP-CA.2 or host device (switch). 
 
Note 
You do not have to switch off the host unit when inserting or extracting 
MiNID. 
 To insert MiNID: 
1. Set the DIP switches to the required operation mode as specified in Setting the DIP Switches. 
2. Insert the necessary SFP into MiNID (see Installing SFPs). 
3. Hold MiNID with the label facing up, and insert MiNID  into an MSA-compatible SFP socket of 
the host equipment. 
2. Installation and Setup 
 
Inserting MiNID  
4. Press MiNID  firmly into the SFP socket, until MiNID  clicks into place. 
MiNID  is ready to operate. 
 To eject : 
1. Disconnect any cables attached to MiNID. 
2. Push the release latch on MiNID’s underside in the direction of the host device. 
 
Note 
The pictures below show the MiNID underside in order to illustrate the release 
latch. 
 
 
Pushing Release Latch 
3. While continuing to keep pressure on the latch, push  MiNID gently towards the host device, and 
then pull MiNID gently out of the socket. 
2. Installation and Setup 
 
Removing MiNID  
4. Release the latch after you have completely removed  MiNID from the socket. 
 
 
Warning 
iNID can become very hot while in operation. Use caution when extracting 
it. 
Inserting MiNID SFP into a Host Unit 
This section explains how to connect/eject MiNID to/from a host device. 
You need to insert MiNID into the host device in order to configure it via the host, or in order to operate 
it. Refer to Service Provisioning for procedures to configure MiNID  via SFP-CA.2 or host device (switch). 
 
Note 
You do not have to switch off the host unit when inserting or extracting 
MiNID. 
 
 To insert MiNID: 
1. Set the DIP switches to the required operation mode as specified in Setting the DIP Switches. 
2. Insert MiNID into a free SFP (MSA-compatible) socket in the host device. 
3. Press MiNID firmly into the SFP socket until MiNID clicks into place and lift the latch to lock 
MiNID into place. 
MiNID SFP is ready to operate. 
2. Installation and Setup 
 To eject MiNID: 
1. Disconnect any cables attached to MiNID. 
2. To extract the MiNID SFP from the host device, open the latch and remove MiNID from the 
socket.  
Inserting MiNID into an SFP-CA.2 
 To connect MiNID and SFP-CA.2 to the PC: 
1. Insert MiNID into the SFP socket of the SFP-CA.2 module. 
2. Connect SFP-CA.2 to your PC via USB 2.0 port. 
The Ready LED on SFP-CA.2 turns on. 
 
SFP-CA.2 Configuration Module 
 To disconnect MiNID and SFP-CA.2 from the PC: 
1. Close all relevant management applications. 
2. Eject MiNID from SFP-CA.2 in the same manner as from a host unit (see Inserting MiNID SFP 
Sleeve into a Host Unit and Inserting MiNID SFP into a Host Unit). 
3.  Disconnect SFP-CA.2 from the PC and from the power. 
 To configure MiNID via SFP-CA.2: 
1. Configure the PC parameters if necessary. 
2. Insert any compatible SFP into MiNID, while it is not connected to SFP-CA.2 or a host device. 
3. Set MiNID to Configuration mode, using its DIP switches (refer to Setting the DIP Switches). 

## 2.7 Basic Connectivity Test  *(p.58)*

2. Installation and Setup 
Note 
While MiNID is in Configuration mode, it responds to the default IP address 
192.168.205.1, with no host VLAN, even if a different IP address was 
configured. 
4. Insert MiNID into the SFP socket of the SFP-CA.2 module. 
5. Connect SFP-CA.2 to your PC via USB 2.0 port. 
The Ready LED on SFP-CA.2 turns on. 
6. Using either your browser or Telnet, connect to 192.168.205.1 and log in with su credentials 
(see User Access). 
 
Note 
If no fiber is connected to the MSA port, ensure that all fault propagation 
actions are disabled (this is the default setting). 
2.7 Basic Connectivity Test 
Check connectivity between MiNID and the PC by sending a ping from the PC to the unit. 
 To ping MiNID: 
1. In the Windows Run prompt, type ping and enter the MiNID IP address (IPv4 or IPv6) as the 
destination IP address of the ping.  
2. Press <Enter> to start sending pings. 
3. A reply from MiNID indicates a proper communication link.  
4. If the ping request times out, check the link between MiNID and the PC (physical path, 
configuration parameters, such as static route, etc.). 
 