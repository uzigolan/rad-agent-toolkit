# Feature Reference – 8 Monitoring and Diagnostics – 8.14 Troubleshooting

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1570–1571.*


## Configuration Errors  *(p.1570)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuration Errors 
The following table lists the messages displayed by ETX‑2i when a configuration error is detected.  
Message 
Possible Cause 
Corrective Action 
Cannot execute; multicast 
IP address not allowed 
You tried configuring the remote device with a 
multicast IP address. 
Configure the remote device 
with a valid IPv4 or IPv6 unicast 
address.   
8.14 Troubleshooting 
This section contains a general troubleshooting chart that lists possible failures and provides 
workarounds. Use this chart to identify the cause of a problem that may arise during operation. For 
detailed description of the LED indicators functions, refer to the Operation and Maintenance chapter. 
To correct the reported problem, perform the suggested corrective actions. If a problem cannot be 
resolved by performing the suggested action, please contact your RAD distributor. 
Fault/Problem 
Probable Cause 
Corrective Action 
The unit is “dead”  
(POWER LED is off) 
No power 
Verify that both ends of the power cable are 
properly connected. 
Blown fuse 
Disconnect the power cable from both ends 
and replace the fuse with another fuse of 
proper rating. 
The event log reports a 
fan or power supply 
error. 
 
View the inventory file by entering show 
inventory at the config>system prompt. 
Restart the unit. 
In case of failure, replace the entire unit. 
The unit is unreachable 
Incorrect management settings 
Using a local serial connection, enable the 
relevant management access type by 
entering telnet, snmp, and/or ssh at the 
config>mngmnt>access prompt.  
View the list of enabled management access 
types and settings by entering info detail at 
the config>mngmnt prompt 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Fault/Problem 
Probable Cause 
Corrective Action 
Verify that a router interface has been 
configured with management access set to 
allow all, assigned an IP address, and bound 
to an administratively enabled SVI. 
Verify that management flows have been 
set up to/from the SVI, and that the flows 
are enabled. 
Management path disconnected 
In the case of remote management, analyze 
this issue using a local serial connection. 
At the current prompt, check whether the 
desired unit responds by entering  
ping <IP address>. 
Check network connectivity issues and 
firewall settings. 
Verify that the management flows have 
been configured correctly. 
Physical link fails to 
respond 
Link may be administratively 
disabled. 
Administratively enable the link. 
In case of Ethernet links, make sure that the 
autonegotiation, speed, and duplex modes 
match the configured values on the access 
switch/router. 
Ethernet LINK LED 
is off 
Ethernet cable problem 
Check the Ethernet cable to see whether a 
cross or straight cable is needed. 
Check/replace Ethernet cable. 
Verify that the range is within the limits. 
Check the port by connecting the remote 
end of the cable to a different switch. 
Send the unit for repair. 
 
 