# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 1.3 Physical Description

*Manual `MiNID_ver_2_6_mn.pdf`, pages 46–46.*


## MiNID SFP Sleeve  *(p.46)*

1. Introduction 
Note 
ESSM frames correspond to the OAM protocol, which is peered by default in 
L2CP/L2PT handling; in this case, ESSM packets are discarded. If OAM protocol 
action is set to pass through, ESSM packets are delivered but link OAM is not 
operational. 
MiNID supports the following G.8262 requirements: 
• 
Jitter and wander generation 
• 
Jitter tolerance 
1.2 New in This Version 
Version 2.6 includes the following new features:  
• 
TACACS+ Authentication 
• 
Dedicated IP addresses for Packet Capture, TWAMP controller, and Layer-3 SAT, when MiNID  is 
managed with loaned IP 
• 
Serial Number display in the inventory 
• 
Free-run timestamping for Packet Capture 
• 
Read-only mode setting for SNMP 
1.3 Physical Description 
MiNID SFP Sleeve 
This figure shows a MiNID with the SFP socket (referred to as the SFP port in this manual) in the lower 
left corner, and the customer-side SFP connector (referred to as the MSA port in this manual) in the 
upper right corner. 