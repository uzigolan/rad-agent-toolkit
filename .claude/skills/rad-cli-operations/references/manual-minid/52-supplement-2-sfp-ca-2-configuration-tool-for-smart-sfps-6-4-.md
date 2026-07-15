# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 6.4 Network Managers

*Manual `MiNID_ver_2_6_mn.pdf`, pages 123–123.*


## Factory Defaults  *(p.123)*


## Configuring Network Managers  *(p.123)*

6. Management and Security 
6.4 Network Managers 
You can define up to two network managers to receive alarms/events/traps from MiNID. 
Factory Defaults 
By default, no SNMP Managers are configured (both manager IP addresses are set to 0.0.0.0). 
Configuring Network Managers 
 To define network managers: 
Do one of the following: 
• 
In the web interface, go to Configuration> System > Management > Manager List, enter one or 
two IP addresses of network manager servers, and click <Apply> to implement the changes, and 
then click <Save Configuration>: 
MiNID 
  
 
 
 Configuration – System- Management - Manager List 
  
 
 
 Manager1  
192.168.42.248 
 Manager2  
10.10.36.61 
  
 
 
 
Network Managers 
• 
In the CLI, go to the config>mngmt level, and enter manager <IP address>. 
You can do this twice to have two network managers. To remove a specific manager, enter no 
manager <IP address>. 