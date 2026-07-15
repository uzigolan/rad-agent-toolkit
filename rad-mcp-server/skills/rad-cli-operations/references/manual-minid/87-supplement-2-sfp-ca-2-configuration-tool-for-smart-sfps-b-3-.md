# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – B.3 Preparing the Test Layout

*Manual `MiNID_ver_2_6_mn.pdf`, pages 379–381.*


## (chapter introduction)  *(p.379)*

B. Test Plan 
Device 
Description 
Quantity 
Local and remote IPmux 
Necessary for Sync-E tests 
2 
Network management station 
PC or Unix workstation equipped 
with RADview  
2 
Network Tester 
Network testing equipment with 
Ethernet interfaces such as 
IXIA 400T, Spirent Test Center, etc. 
2 
B.3 Preparing the Test Layout 
The following diagram illustrates the test plan setup. 
 
Local ETX
1
2
3
4
5
6
MiNID 1
Classifier VLAN+Pbit
MiNID 2
Classifier DSCP
MiNID 3
Classifier Source MAC
MiNID 4
Classifier Port
Network
Tester
Remote ETX
1
2
3
4
5
6
EFM 
Active
EFM 
Active
EFM 
Passive
EFM 
Passive
Network
Tester
EXT
CLK
EXT
CLK
Local 
IPmux
Remote 
IPmux
 

## Connecting the Test Layout  *(p.380)*

B. Test Plan 
Connecting the Test Layout 
The following tables list the connections between the devices, and the cable required for each 
connection. 
Test Layout Connections 
Device 
Cable 
Device 
Local ETX port 1 
Straight Ethernet cable 
Local Network Tester  
Local ETX port 2 
Not applicable; MiNID is inserted 
UUT-1 
Local ETX port 3 
Not applicable; MiNID is inserted 
UUT-2 
Local ETX port 4 
Not applicable; MiNID is inserted 
UUT-3 
Local ETX port 5 
Not applicable; MiNID is inserted 
UUT-4 
Local ETX EXT CLK port 
Straight Ethernet cable 
Local IPmux EXT CLK port 
Local IPmux EXT CLK port 
Straight Ethernet cable 
Local ETX EXT CLK port 
UUT-1 
Straight Ethernet cable 
Remote ETX port 2 
UUT-2 
Straight Ethernet cable 
Remote ETX port 3 
UUT-3 
Straight Ethernet cable 
Remote ETX port 4 
UUT-4 
Straight Ethernet cable 
Remote ETX port 5 
Remote ETX port 1 
Straight Ethernet cable 
Remote Network Tester  
Remote ETX port 2 
Straight Ethernet cable 
UUT-1 
Remote ETX port 3 
Straight Ethernet cable 
UUT-2 
Remote ETX port 4 
Straight Ethernet cable 
UUT-3 
Remote ETX port 5 
Straight Ethernet cable 
UUT-4 
Remote ETX EXT CLK port 
Straight Ethernet cable 
Remote IPmux EXT CLK port 
Remote IPmux EXT CLK port 
Straight Ethernet cable 
Remote ETX EXT CLK port 
Local Network Tester 
Straight Ethernet cable 
Local ETX port 1 
Remote Network Tester 
Straight Ethernet cable 
Remote ETX port 1 
 

## Configuring Devices  *(p.381)*

B. Test Plan 
Configuring Devices 
This section presents the device configurations. The data, such as VLAN IDs and IP addresses, were 
randomly selected for test purposes, and can be changed to suit your particular configuration. 
The following table presents the configuration files for the MiNID and ETX devices. You can open or save 
the configuration files as follows: 
• 
To open the file – Double-click the icon
in the table below.  
• 
To save the file – Right-click the icon 
 in the table below and select Save Embedded File to 
Disk. 
Device 
File 
UUT-1 
 
UUT-2 
 
UUT-3 
 
UUT-4 
 
Local ETX 
 
Remote ETX 
 
The following table presents the IPmux device configurations. 
Parameter 
Local 
Remote 
Host IP 
192.168.205.32 
192.168.205.33 
E1 configuration 
Unframed 
Unframed 
Peer IP 
10.10.10.10 
10.10.10.11 
PW IP 
10.10.10.11 
10.10.10.10 
Payload size 
4 
4 
OAM 
Disable 
Disable 
 