# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 2.7 Basic Connectivity Test

*Manual `MiNID_ver_2_6_mn.pdf`, pages 58–58.*


## Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 2.7 Basic Connectivity Test  *(p.58)*

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
 