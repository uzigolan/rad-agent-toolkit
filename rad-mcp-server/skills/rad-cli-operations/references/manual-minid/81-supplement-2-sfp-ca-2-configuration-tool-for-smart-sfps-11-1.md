# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.13 Troubleshooting

*Manual `MiNID_ver_2_6_mn.pdf`, pages 374–374.*


## Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.13 Troubleshooting  *(p.374)*

11. Monitoring and Diagnostics
c.
Set PM Interval Duration to 1 Min, 5 Min, 10 Min, or 15 Min.
d.
Set PM File Interval Duration to 10 Sec, 1 Min, 5 Min, 10 Min, or 15 Min.
Note 
PM File Interval Duration must be less than or equal to PM Interval Duration. 
e.
Click <Apply> to implement the changes, and then click <Save Configuration>.
MiNID 
Configuration – System - Performance Monitoring 
PM Mode 
Enable 
PM Interval Duration 
15 Min 
PM File Interval Duration 
5 Min 
•
In the CLI:
a.
Go to the configure reporting context.
b.
Enter pm to enable PM collection, or no pm to disable PM collection.
c.
Enter the following to set the PM interval:
interval-duration {1 | 5 | 10 | 15}
d.
Enter the following to set the interval for collecting the PM data:
file-interval-duration {10s |1 | 5 | 10 | 15}
Note 
The value set by file-interval-duration must be less than or equal to the value 
set by interval-duration. 
11.13 Troubleshooting 
This section contains a general troubleshooting chart that lists possible failures and provides 
workarounds. 
•
Use this chart to identify the cause of a problem that may arise during operation. For a detailed
description of the LED indicator functions, refer to Chapter 3.