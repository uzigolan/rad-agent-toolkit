# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 3.11 Turning Off the Unit

*Manual `MiNID_ver_2_6_mn.pdf`, pages 88–88.*


## Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 3.11 Turning Off the Unit  *(p.88)*

3. Operation 
3.10 Configuration via Host (Telnet/SSH and CLI/Web 
Interface/RADview/SNMP) 
A similar procedure to configuring via SFP-CA.2 can be used to configure MiNID SFP sleeve and MiNID 
SFP when it is inserted into the SFP port of a host device, as long as connectivity is established to an 
available Ethernet port. 
 To configure MiNID via a host: 
1. Disconnect MiNID from any device. 
2. If you use MiNID SFP sleeve, insert any compatible SFP into it. 
3. Set MiNID to Configuration mode, using its DIP switches (refer to Setting the DIP Switches in 
Chapter 2). 
Note 
While MiNID is in Configuration mode, it responds to the default IP address 
192.168.205.1, with no host VLAN, even if a different IP address was 
configured. 
4. Insert MiNID SFP sleeve or MiNID SFP into an available SFP socket of the switch. 
5. Connect the available switch port to which connectivity has been established, to your PC, using 
an IP address in the subnet 192.168.205.XX. 
6. Using either your browser or Telnet, connect to 192.168.205.1 and log in with su credentials 
(see User Access). 
3.11 Turning Off the Unit 
 SFP sleeve and SFP receive power from their host device, therefore they stop functioning when 
removed from SFP-CA.2 or a host unit, or when the host device is powered off. 
 