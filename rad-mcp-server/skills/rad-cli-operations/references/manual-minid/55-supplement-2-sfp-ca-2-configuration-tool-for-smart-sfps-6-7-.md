# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 6.7 SNMP Communities

*Manual `MiNID_ver_2_6_mn.pdf`, pages 134–134.*


## Factory Default  *(p.134)*


## Configuring the Session Timeout  *(p.134)*

6. Management and Security 
6.6 Session Timeout 
Both management interfaces (web and CLI) disconnect the user session after a configurable time period 
without user action. The timeout value is a whole number of minutes in the range 1–60. 
Factory Default 
The default timeout is 5 minutes. 
Configuring the Session Timeout 
 To configure the session timeout: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Management > Management Timeout, set 
the Timeout and click <Apply> to implement the changes, and then click <Save Configuration>: 
MiNID 
  
 
 
 Configuration>System>Management>Management Timeout 
  
 
 
 Timeout 
(Min.) 
 
5 
  
 
 
 
• 
In the CLI, go to the config>mngmnt level, and enter timeout <minutes>. 
6.7 SNMP Communities 
You can configure the names for the read-only, read/write, and trap communities used for SNMPv1/v2 
access. 