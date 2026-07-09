# Feature Reference – 8 Monitoring and Diagnostics – 8.11 Statistic Counters

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1557–1557.*


## Configuration Errors  *(p.1557)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Configuration Errors 
The following table lists the messages displayed by ETX‑2i when a configuration error is detected.  
Message 
Description 
Invalid interval; must divide evenly into 
3600 
The pm-collection command was entered with an interval value 
that does not divide evenly into 3600. 
Cannot execute; too many different 
intervals 
Attempt was made to configure more intervals than the supported 
maximum. 
Directory name cannot end with \; 
remove it or use / 
You configured a destination directory name ending with \. This is 
not valid, as configured strings are enclosed in quotation marks; 
and \” has a special meaning. 
PM file push is already configured 
You already sent a file format to the server. You can only send one 
file format to one server. 
8.11 Statistic Counters 
Statistic counters provide information on possible abnormal behavior and failures. You can collect 
statistics on the following: 
• 
Ethernet ports 
• 
E1/T1 ports, if applicable 
• 
SHDSL ports, if applicable 
• 
VDSL ports, if applicable 
• 
Flows 
• 
RADIUS server 
• 
OAM CFM 
For further information, refer to the relevant sections in the User Manual and the relevant sections in 
the troubleshooting chart. 
You can clear the statistics for Ethernet ports, flows, and OAM services. Statistics clearing is globally 
enabled by default. Once statistics are cleared from an interval, the interval becomes “not valid”. 