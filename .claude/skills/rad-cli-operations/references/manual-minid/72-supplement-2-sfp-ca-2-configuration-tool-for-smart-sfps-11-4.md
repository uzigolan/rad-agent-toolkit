# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.4 OAM (EFM)

*Manual `MiNID_ver_2_6_mn.pdf`, pages 321–324.*


## Applicability and Scaling  *(p.321)*


## Standards Compliance  *(p.321)*


## Benefits  *(p.321)*


## Functional Description  *(p.321)*

11. Monitoring and Diagnostics 
The summary is displayed. 
 To view the summary using the CLI: 
1. Go to configure oam cfm. 
2. Type in show summary. 
The summary is displayed. 
11.4 OAM (EFM) 
This section covers the monitoring of Ethernet links using link OAM (EFM) (OAM Ethernet at the First 
Mile).  can act as the active or passive side in an IEEE 802.3-2005 application. The link OAM can be 
activated for one  port at a time. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
IEEE 802.3-2005 
Benefits 
Link OAM provides remote management and fault indication for the Ethernet links, as well as detection 
of remote link failure. 
Functional Description 
The OAM (EFM) discovery process allows a local data terminating entity (DTE) to detect Ethernet OAM 
capabilities on a remote DTE. Once Ethernet OAM support is detected, both ends of the link exchange 
state and configuration information, such as mode, PDU size, loopback support, etc. If both DTEs are 

## Factory Defaults  *(p.322)*


## Configuring Link OAM  *(p.322)*

11. Monitoring and Diagnostics 
satisfied with the settings, OAM is enabled on the link. However, the loss of a link or a failure to receive 
OAMPDUs for five seconds causes the discovery process to restart.  
DTEs may be in either active or passive mode. DTEs in active mode initiate the OAM (EFM) 
communications and can issue queries and commands to a remote device. DTEs in passive mode 
generally wait for the peer device to initiate OAM communications, and respond to commands and 
queries, but do not initiate them. 
A flag in the OAMPDU allows an OAM entity to convey the failure condition Link Fault to its peer. Link 
Fault refers to the loss of signal detected by the receiver; a Link Fault report is sent once per second with 
the Information OAMPDU. 
Factory Defaults 
By default, OAM EFM is not enabled for the  ports.  
Configuring Link OAM 
The following parameters are configured for link OAM. 
Link OAM Parameters 
Parameter 
Description 
Web 
CLI 
OAM Mode 
mode 
Specifies active or passive mode 
OAM Port 
bind 
Port for which link OAM is active: 
• SFP/1 
• MSA/2. 
 
Note 
In order for link OAM to function, an L2CP profile must be defined with the 
OAM protocol action set to peer, and flow classification mode must be port 
mode or VID+Pbits Range, to enable attaching the L2CP profile to the relevant 
port/flow. 
11. Monitoring and Diagnostics 
Configuring Link OAM Using the Web Interface 
 To configure link OAM: 
1. Navigate to Configuration > OAM > Link OAM. 
2. If OAM (EFM) is disabled, the screen appears as shown in the following figures. 
 
  
 
 
 Configuration>OAM>Link OAM 
  
 
 
 OAM Mode 
 
Passive 
 Ingress Port 
 
SFP/Port 1 
  
 
 
 Enable 
 
 
  
 
 
Link OAM Disabled 
 
  
 
 
 Configuration>OAM>Link OAM 
  
 
 
 OAM Mode 
 
Passive 
 Ingress Port 
 
SFP/Port 1 
  
 
 
 Disable 
 
 
  
 
 
Link OAM Enabled 
1. To enable, select the mode and port, and then click Enable. 
2. To disable, click Disable. 

## Examples  *(p.324)*

11. Monitoring and Diagnostics 
Configuring Link OAM Using the CLI 
 To configure link OAM: 
1. Navigate to configure oam efm. 
The config>oam>efm# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Specifying for which port to activate 
link OAM 
bind ingress-port {sfp/1 | 
msa/2} 
 
Enabling loopback  
loopback 
Type no loopback to disable 
loopback 
Note: Available only in passive 
mode 
Specifying active or passive mode 
mode {active | passive} 
 
Enabling link OAM 
no shutdown 
Type shutdown to disable link 
OAM 
Displaying link OAM (EFM) status 
show status 
 
Clearing link OAM (EFM) statistics 
clear-statistics 
 
Displaying link OAM (EFM) statistics 
show statistics 
 
Examples 
 To enable active link OAM for port SFP/1: 
exit all  
configure oam efm 
  shutdown 
  mode active 
  bind ingress-port sfp/1 
  loopback 
  no shutdown 
  exit all 
 To display the link OAM status: 
>config>oam>efm# show status 
Administrative Status   : Enabled 