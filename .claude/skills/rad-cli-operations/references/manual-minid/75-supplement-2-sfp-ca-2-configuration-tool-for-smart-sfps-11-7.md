# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.7 Ping

*Manual `MiNID_ver_2_6_mn.pdf`, pages 357–359.*


## Applicability and Scaling  *(p.357)*


## Benefits  *(p.357)*


## Factory Defaults  *(p.357)*

11. Monitoring and Diagnostics 
Parameter 
Value 
Description 
Capture port 
<port name/number> 
 
Capture packet size 
First X bytes|Whole packet 
Shows the number of bytes 
in case of of truncated 
packets or writes about 
whole packet 
Start 
hh:mm:ss dd-mm-yyyy 
Start time of session 
End 
hh:mm:ss dd-mm-yyyy 
End time of session 
Elapsed time 
hh:mm:ss 
Time period from the session 
start 
Tx packets 
<packets number> 
Number of packets 
processed during the session 
Capture rule #1 
 
See filters in the table above 
Capture rule #2 
 
See filters in the table above 
11.7 Ping 
MiNID can initiate a ping to test whether the host is reachable across the IP network.  
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Benefits 
 Can verify communication with the host and other devices. 
Factory Defaults 
The default number of packets sent for the ping test is 5. 

## Configuring Ping Test  *(p.358)*

11. Monitoring and Diagnostics 
Configuring Ping Test 
 To initiate a ping using the web interface: 
1. Navigate to > Utilities> Ping. 
 
 
2. In the Destination IP address field, type in the IP address. 
3. In the Number of packets field, type in the number of packets you want the MiNID to send. 
4. Click <Apply>. 

## Example  *(p.359)*

11. Monitoring and Diagnostics 
 
 
5. Click <Stop ping> to stop the ping test. 
 To initiate a ping using the CLI: 
• 
In the command line, type ping <ip address> [number-of-packets <packets>].  
Example 
MiNID# ping 162.35.158.2 number-of-packets 6 
Reply from 162.35.158.2: bytes=32, packet number=1, time<1ms 
Reply from 162.35.158.2: bytes=32, packet number=2, time<1ms 
Reply from 162.35.158.2: bytes=32, packet number=3, time<1ms 
Reply from 162.35.158.2: bytes=32, packet number=4, time<1ms 
Reply from 162.35.158.2: bytes=32, packet number=5, time<1ms 
Reply from 162.35.158.2: bytes=32, packet number=6, time<1ms 
6 packets transmitted. 6 packets received. 0% packet loss 
Round Trip <ms> min/avg/max= 0/0/0  
 