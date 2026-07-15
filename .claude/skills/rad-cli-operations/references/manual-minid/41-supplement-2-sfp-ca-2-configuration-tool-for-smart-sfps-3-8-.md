# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 3.8 SNMP-Based Network Management

*Manual `MiNID_ver_2_6_mn.pdf`, pages 85–85.*


## Working with RADview  *(p.85)*

3. Operation 
3.8 SNMP-Based Network Management 
Note 
Make sure that SNMP is enabled and not set in the “read-only” mode (see 
Management Access Control) before starting to work with RADview or other 
SNMP-based NMSs. 
Working with RADview 
RADview is a user-friendly and powerful SNMP-based element management system, used for planning, 
provisioning and managing heterogeneous networks. RADview provides a dedicated graphical user 
interface (GUI) for monitoring RAD products via their SNMP agents. RADview for MiNID is bundled in the 
RADview package for Windows or UNIX.  
RADview is a Windows-based modular, client-server, scalable management system that can be used in a 
distributed network topology or a single-station configuration. RADview consists of the system (EMS) 
and the following optional modules: 
• 
Service Manager (SM) – end-to-end Carrier Ethernet service provisioning for Ethernet Access 
products. This module includes the Service Center (SC) module, which is an end-to-end Carrier 
Ethernet and TDM service provisioning for CI (Critical infrastructure) products.  
• 
Performance Monitor (PM) – portal for service SLA monitoring for both carriers and their 
customers. 
 
Warning 
To prevent conflicts and ensure a stable and consistent network setup, 
provision services using either RADview Service Manager or CLI, but not 
both simultaneously. 
 
For more details about this network management software, and for detailed instructions on how to 
install, set up, and use RADview, contact your local RAD partner. See Working with Other SNMP-Based 
NMSs for details on the SNMP MIBs used by MiNID. 
RADview for MiNID supports autodiscovery and alarms, as well as configuration via SNMP. You can 
double-click the MiNID icon in RADview to activate a connection to the MiNID web interface, or 
right-click the MiNID icon in RADview and select the option to open a Telnet session. 