# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 3.3 Startup

*Manual `MiNID_ver_2_6_mn.pdf`, pages 59–59.*


## Configuration and Software Files  *(p.59)*

3 Operation 
3.1 Turning On the Unit 
MiNID SFP sleeve and MiNID SFP receive power from its host device, therefore they start to function 
when inserted into SFP-CA.2 or a host unit, or when the host device is powered on. 
3.2 Indicators 
MiNID SFP sleeve and MiNID SFP do not have LED indicators. 
3.3 Startup 
Configuration and Software Files 
The following system files contain configuration settings or application software: 
• 
factory-default-config – Contains the manufacturer default settings. At startup, 
factory-default-config is loaded if startup-config and user-default-config are missing or invalid. 
• 
running-config – Contains the current configuration that the device is running 
• 
startup-config – Contains saved non-default user configuration. You can use the save or copy 
command to create startup-config, or click <Save Configuration> in the Web interface. At 
startup, startup-config is loaded if it exists and is valid. 
• 
user-default-config – Contains default user configuration. This file is not automatically created. 
You can use the copy command or Utilities > File > Copy screen to create it. At startup, 
user-default-config is loaded if startup-config is missing or invalid 