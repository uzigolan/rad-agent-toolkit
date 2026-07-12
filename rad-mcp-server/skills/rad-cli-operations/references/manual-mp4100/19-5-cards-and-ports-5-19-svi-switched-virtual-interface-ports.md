# 5 Cards and Ports – 5.19 SVI (Switched Virtual Interface) Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 400–401.*


## 5 Cards and Ports – 5.19 SVI (Switched Virtual Interface) Ports  *(p.400)*

5. Cards and Ports 
SDH/SONET Port Statistics Parameters – Selected 15-Minute Interval  
Parameter 
Description 
Section ES  
Displays the total number of errored seconds (ES) in the selected interval 
Section SES  
Displays the total number of severely errored seconds (SES) in the selected interval 
Section SEFS 
Displays the total number of unavailable seconds (SEFS/UAS) in the selected interval 
Section CV 
Displays the total number of code violations (CV) in the selected interval 
Interval number 
Number of interval for which statistics is displayed  
There are two options for clearing SDH/SONET statistics data: 
• 
Clearing current interval statistics 
• 
Clearing all statistics, except for the current interval. 
 To clear the current interval statistics: 
1. Navigate to the corresponding entity as described above. 
2. Enter clear-statistics current-interval. 
The statistics for the specified entity are cleared. 
 To clear all statistics data except for from the current interval: 
1. Navigate to the corresponding entity as described above. 
2. Enter clear-statistics current-all. 
The statistics for the specified entity are cleared. 
5.19 SVI (Switched Virtual Interface) Ports  
A switched virtual interface (SVI) is a VLAN of switch ports represented by one interface to a routing or 
bridging system. There is no physical interface for the VLAN, and the SVI provides this interface for 
VLANs participating in management and PW traffic. 
In Megaplex-4 management, an SVI port is an intermediate Ethernet entity between the Bridge/Router 
and another Ethernet port (bound one-to-one) providing the Layer 3 processing for packets from all 
switch ports associated with the VLAN. It also serves as an ingress or egress port for terminating 
management flows. The flow is configured between the physical port, which is the management source, 
5. Cards and Ports 
and the corresponding SVI port bound to the bridge port. This flow will classify the management traffic 
to be forwarded to the bridge port. For illustration, see Example under Management Bridge in Chapter 
8. There is one-to-one mapping between a VLAN and SVI, thus only a single SVI can be mapped to a 
VLAN. 
PW traffic created in the Megaplex-4 is switched to the external network via flows with SVI as one of the 
flow endpoints. Same SVI can share multiple PW’s with a VLAN-based classifier, defined in the PW menu. 
You can enable and operate a switched virtual interface (SVI port) as explained below. 
 To define an SVI port: 
• 
At the config>port# prompt, enter svi <port number>. 
The config>port>svi <port number># prompt appears and the relevant SVI port is defined. 
 To administratively enable an SVI port: 
• 
At the config>port>svi<port number># prompt, enter no shutdown. 
The SVI port is administratively enabled. 
 To administratively disable an SVI port: 
• 
At the config>port>svi<port number># prompt, enter shutdown. 
The SVI port is administratively disabled. 
 To display all SVI ports configured in the system:  
• 
At the config>port prompt, enter show svi-summary. 
config>port# show svi-summary 
SVI Number  Admin     Bound to 
----------------------------------------------------------------------------- 
1           Enabled   Router 1 1 
2           Enabled   PW 1 
All SVI ports configured in the system are displayed together with the entities the SVI port is 
bound to. 