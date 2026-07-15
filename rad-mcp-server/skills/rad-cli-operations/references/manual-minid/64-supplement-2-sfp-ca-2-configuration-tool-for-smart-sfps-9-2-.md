# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 9.2 Sync-E Clock Source

*Manual `MiNID_ver_2_6_mn.pdf`, pages 224–225.*


## Applicability and Scaling  *(p.224)*


## Standards Compliance  *(p.224)*


## Benefits  *(p.224)*


## Functional Description  *(p.224)*


## Factory Defaults  *(p.224)*

9. Timing and Synchronization 
9.2 Sync-E Clock Source  
 SFP sleeve and SFP unit can transparently transfer the Sync-E clock and ESSM packets between its ports. 
You can define whether to transfer from the MSA port or the SFP port. 
Applicability and Scaling 
Copper SFPs do not support Sync-E transfer, except for SFP-ToC, which supports only the direction SFP 
to MSA. 
Standards Compliance 
ITU-T G.8262 
Benefits 
You have the flexibility to define which port transfers the Sync-E clock. 
Functional Description 
You can configure the Sync-E clock source as the MSA port (to transfer the Sync-E clock from the MSA 
port to the SFP port), or the SFP port (to transfer the Sync-E clock from the SFP port to the MSA port). 
If a physical fault (LOS) occurs on the clock source port,  automatically sets the clock source to the 
system internal oscillator. 
When the port fault is cleared, the clock source returns to the user-configured clock source.  
 
Note 
Port status polling rate is 400 ms, therefore it can take up to 400 ms for the 
clock source to change back to the configured source. 
Factory Defaults 
By default,  transfers the Sync-E clock from the MSA port to the SFP port. 

## Configuring the Sync-E Clock Source  *(p.225)*

9. Timing and Synchronization 
Configuring the Sync-E Clock Source 
 To define the Sync-E clock source: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Clock, select SFP/Port 2 to transfer timing 
packets from the SFP/Port 2 port to the MSA/Port 1 port; or MSA/Port 1 to transfer timing 
packets from the MSA/Port 1 port to the SFP/Port 2 port; then click <Apply> to implement the 
changes, and then click <Save Configuration>. 
 
MiNID 
  
 
 
 Configuration>System>Clock 
  
 
 
 Sync-E Clock 
Source 
 
MSA/Port 1 
  
 
 
 
• 
In the CLI, navigate to the configure system clock context, and do one of the following: 
 
To transfer timing packets from the SFP/Port 2 port to the MSA/Port 1 port, enter: 
sync-e-src sfp 
 
To transfer timing packets from the MSA/Port 1 port to the SFP/Port 2 port, enter: 
sync-e-src msa 
 
 