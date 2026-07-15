# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 3.5 Configuration and Management

*Manual `MiNID_ver_2_6_mn.pdf`, pages 62–62.*


## Saving Configuration Changes  *(p.62)*

3. Operation 
a. Send the trap systemDownloadEnd (with success indication) to any configured network 
managers 
b. Verify that the file contains valid CLI commands 
c. Execute the commands in the file. 
Saving Configuration Changes 
When you make changes to the MiNID configuration, you need to save the changes so that they are 
available after the next device reset. You can save your configuration as follows: 
• 
Web: Click <Save Configuration> 
CLI: Use the save command to save running-config as startup-config 
• 
Web: Use the Utilities > File > Copy screen to copy running-config to startup-config or 
user-default-config 
CLI: Use the copy command to copy running-config to startup-config or user-default-config. 
3.5 Configuration and Management 
MiNID provides the following management interfaces: 
• 
Web interface over HTTP 
• 
CLI interface over Telnet / secure Telnet (SSH) 
Once MiNID is accessible via IP address, it can be configured via Web or Telnet/ secure Telnet (SSH). 
By default, MiNID can transmit management data over both of its ports. The MiNID SFP sleeve and 
MiNID SFP ports are designated as follows: 
• 
SFP –Provides socket where an SFP can be inserted into MiNID 
• 
MSA – Enables inserting MiNID into a customer device 
Management can be disabled on either port (see Management Access Control); it cannot be disabled 
for both ports simultaneously. 
MiNID SFP sleeve and MiNID SFP can be configured via the SFP-CA.2 adaptor, or via a switch that acts as 
a host device. See Configuration of MiNID SFP via SFP-CA.2 (Telnet/SSH/Web) and Configuration via 
Host (Telnet/SSH and CLI/Web Interface/RADview/SNMP). 