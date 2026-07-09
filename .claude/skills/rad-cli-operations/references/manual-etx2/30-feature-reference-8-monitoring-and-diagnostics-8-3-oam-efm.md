# Feature Reference – 8 Monitoring and Diagnostics – 8.3 OAM EFM

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1368–1371.*


## Applicability and Scaling  *(p.1368)*


## Standards  *(p.1368)*


## Functional Description  *(p.1368)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
8.3 OAM EFM 
Ethernet OAM (Operation, Administration, and Maintenance) functions provide end-to-end connectivity 
checks and performance monitoring. 
Ethernet in the First Mile (EFM), a link-layer OAM protocol that operates at the level of the single link for 
remote management and fault indication, can detect link failure. ETX‑2i can act as the active or passive 
side in an IEEE 802.3ah application.  
The term last mile is often used by core network engineers to refer to access links from an operator’s 
central office to the customer’s locations. The opposite term first mile refers to the same access links 
but from the customer’s perspective. 
This section covers the monitoring of Ethernet links using OAM EFM (OAM Ethernet at the First Mile).   
Applicability and Scaling 
This feature is applicable to all ETX‑2i products, with the following conditions: 
• 
PCS port is relevant to ETX-2i with an SHDSL or VDSL2 module. 
• 
ETX-2i, ETX-2i-B, ETX-2i-10G, ETX-2i-10G-B, and ETX-2i-100G/4Q support dying gasp over OAM 
EFM on hard-coded ports 0/1, 0/2, 0/3, and 0/4. 
Standards 
IEEE 802.3-2005 
Functional Description 
The OAM (EFM) discovery process allows a local data terminating entity (DTE) to detect Ethernet OAM 
capabilities on a remote DTE. Once Ethernet OAM support is detected, both ends of the link exchange 
state and configuration information, such as mode, PDU size, loopback support, etc. If both DTEs are 
satisfied with the settings, OAM is enabled on the link. However, the loss of a link or a failure to receive 
OAMPDUs for five seconds may cause the discovery process to restart.  
DTEs may either be in active or passive mode. DTEs in active mode initiate the ETH-OAM (EFM) 
communications and can issue queries and commands to a remote device. DTEs in passive mode 

## Factory Defaults  *(p.1369)*


## Configuring OAM EFM  *(p.1369)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
generally wait for the peer device to initiate OAM communications and respond to commands and 
queries, but do not initiate them. 
A flag in the OAMPDU allows an OAM entity to convey the failure condition Link Fault to its peer. Link 
Fault refers to the loss of signal detected by the receiver; A Link Fault report is sent once per second 
with the Information OAMPDU. 
Factory Defaults 
By default, OAM EFM is not enabled for Ethernet/logical MAC/PCS ports.  
Configuring OAM EFM 
There are two available OAM EFM descriptors. Each can be configured to indicate active or passive OAM 
EFM. When you enable OAM EFM for a port, you assign a descriptor to the port. 
You can configure OAM EFM for Ethernet/logical MAC/PCS ports. When link OAM (EFM) is enabled for a 
port, you can view its status by displaying the port status (show status). You can also display the OAM 
(EFM) parameters and OAM (EFM) statistics.  
 To configure OAM EFM descriptor: 
1. Navigate to configure oam efm. 
2. Enter descriptor <number> {active | passive} 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure link OAM (EFM) for Ethernet/logical MAC/PCS port: 
1. Navigate to configure port ethernet [<slot>/]<port> or configure port logical-mac <port> or 
configure port pcs <port>, respectively. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Enabling link OAM (EFM)  
efm descriptor <1–2> 
The EFM descriptor must exist 
before you can assign it to a port. 
Note: In order for link OAM (EFM) 
to function properly, the relevant 
Ethernet port must be associated 
with an L2CP profile that specifies 
peer action for MAC 0x02. 
Disabling link OAM (EFM) 
no efm 
 
Displaying link OAM (EFM) 
parameters 
show oam-efm 
Note: Relevant only for 
Ethernet/PCS ports if link OAM 
(EFM) is enabled. 
Displaying link OAM (EFM) statistics 
show oam-efm-statistics 
Note: Relevant only for 
Ethernet/PCS ports if link OAM 
(EFM) is enabled. 
Commands in level efm 
Enabling loopback  
loopback 
Enter no loopback to disable 
loopback. 
Enabling SNMP tunneling for OAM 
EFM 
snmp-tunneling  
Enter no snmp-tunneling to disable 
snmp tunneling. 
 
 

## Examples  *(p.1371)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Examples 
 To enable active link OAM (EFM) for Ethernet port 1/1: 
#************** Configure L2CP profile for OAM EFM 
exit all 
configure port l2cp-profile mac2peer 
  mac 0x02 peer 
  exit all 
 
#************** Configure OAM EFM descriptor 
configure oam efm 
  descriptor 2 active 
  exit all 
 
#************** Configure Ethernet port 1/1: 
#**************   Associate L2CP profile and OAM EFM descriptor 
configure port ethernet 1/1 
  l2cp profile mac2peer 
  efm descriptor 2 
  exit all 
 To display the link OAM (EFM) status for Ethernet port 1/1: 
ETX‑2i>config>port>eth(1/1)# show oam-efm 
Administrative Status : Enabled                                  
Operational Status    : Link Fault                               
Loopback Status       : Off                                      
 
Information 
--------------------------------------------------------------- 
                 Local                     Remote     
Mode           : Active                    --         
MAC Address    : 00-20-D2-30-CC-9D         --         
Unidirectional : Not Supported             --         
Vars Retrieval : Supported                 --         
Link Events    : Supported                 --         
Loopback       : Supported                 --         
PDU Size       : 1518                      --         
Vendor OUI     : 0x0020D2                  --         
 
 