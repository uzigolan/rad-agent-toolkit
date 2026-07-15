# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 7.4 Configuring Fault Propagation

*Manual `MiNID_ver_2_6_mn.pdf`, pages 139–141.*


## Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 7.4 Configuring Fault Propagation  *(p.139)*

7. Resiliency (Fault Propagation) 
 
• 
 (SFP sleeve only) TX disable received by the MSA port –transmitted by host to request shutting 
down the transmitter optical output. You can configure whether MiNID propagates the TX 
disable signal from the MSA port to the SFP port. 
• 
(SFP sleeve only) TX fault received by the SFP port –indicates that a fault has occurred in the SFP. 
You can configure whether MiNID propagates the TX fault signal from the SFP port to the MSA 
port. 
 
Note 
For the SFP sleeve option, if you want the same fault indication behavior as if 
the SFP in MiNID were inserted directly into the host device, you should enable 
fault propagation for the TX-fault and TX-disable signals. 
 
Disable – When LOC or AIS failure is observed on any MEP, it is not propagated. 
• 
Interface Status TLV: 
 
Tx handling –The CCM to the peer MEP will carry “Interface Status TLV” with value of “isUp”. 
When the other side port is down, an “Interface Status TLV” will be sent in the CCM 
message to the peer MEP carrying value of “isDown”. The switching from “isUp” to 
“isDown” is triggered by interface deactivation, and vice versa. 
 
Rx handling –The receiving MEP will be able to deactivate the other side port (LOS signal, Tx 
Disable signal). 
7.3 Factory Defaults 
By default, all fault propagation actions are disabled, so LOS is blocked. 
7.4 Configuring Fault Propagation 
 To configure fault propagation actions: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Fault Propagation, enable or disable the 
relevant propagation actions (see Functional Description), and click <Apply> to implement the 
changes, and then click <Save Configuration>: 
7. Resiliency (Fault Propagation) 
Note 
The following appear only for the SFP sleeve option: 
• 
Disable Host PHY 
• 
Propagate TX Disable Signal 
Propagate TX Fault Signal. 
 
 
MiNID 
  
 
 
 Configuration>System>Fault Propagation 
  
 
 Propagate LOS Signal 
 
Disable 
 Disable Host PHY 
 
Disable 
 Transmit AIS 
 
Disable 
  
 
 
 Propagate TX Disable Signal 
 
Disable 
 Propagate TX Fault Signal 
 
Disable 
 CFM Fault : IF Deactivation 
 
Disable 
 IF Status TLV: IF Deactivation 
 
Disable 
  
 
 
Fault Propagation 
• 
In the CLI: 
a. Go to the configure system context, and enter fault-propagation, to go into the 
config>system>fault context. 
b. To enable LOS propagation from SFP/port 1 to MSA/port 2, enter: los-propagation 
c. To specify a direction for propagating OAM CFM faults (LOC, Rx AIS), enter: 
[no] cfm-fault {sfp/Port 1-msa/Port 2 | msa/Port 2-sfp/Port 1} 
d. For the MEP to deactivate the other side port, if-status-tlv {SFP|Port 1-MSA|Port 
2/MSA|Port 2-SFP|Port 1}.  
 
Note 
The following are relevant only for the SFP sleeve option: 
 
7. Resiliency (Fault Propagation) 
e. To disable the physical interface (PHY) towards the host in the event that LOS is received, 
enter: phy-disable 
f. If los-propagation and phy-disable are both disabled, you can enable sending an OAM CFM 
AIS when LOS is received, by entering: ais 
g. To enable propagating the TX disable signal from the MSA port to the SFP port, enter: tx-
disable 
h. To enable propagating the TX fault signal from the SFP port to the MSA port, enter: tx-fault 