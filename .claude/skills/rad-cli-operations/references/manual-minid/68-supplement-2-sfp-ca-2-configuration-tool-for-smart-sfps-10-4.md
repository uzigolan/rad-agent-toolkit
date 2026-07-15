# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 10.4 Reset

*Manual `MiNID_ver_2_6_mn.pdf`, pages 237–238.*


## Resetting to Factory Defaults  *(p.237)*


## Resetting to User Defaults  *(p.237)*

10. Administration 
10.4 Reset 
You can reset MiNID in the following ways: 
• 
Reset to factory defaults. All settings return to factory defaults, except for host IP and VLAN 
parameters. To reset these, use the DIP switches (refer to Setting the DIP Switches). 
• 
Reset to user defaults (from user-default-config) 
• 
Overall reset (restart) of the device  
Resetting to Factory Defaults 
 To reset MiNID to factory defaults: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Set Factory Defaults. 
• 
In the CLI, in the admin context, enter: 
factory-default 
In both interfaces, you are prompted to confirm. 
Resetting to User Defaults 
 To reset MiNID to user defaults: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Set User Defaults. 
• 
In the CLI, in the admin context, enter: 
user-default 
In both interfaces, you are prompted to confirm. 

## Restarting the Unit  *(p.238)*

10. Administration 
Restarting the Unit 
 To restart MiNID: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Reset Device. 
• 
In the CLI, in the admin context, enter: 
reboot 
In both interfaces, you are prompted to confirm the reboot.  
 
 