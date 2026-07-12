# 5 Cards and Ports – 5.15 Management Ethernet Port

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 341–341.*


## 5 Cards and Ports – 5.15 Management Ethernet Port  *(p.341)*

5. Cards and Ports 
Parameter 
Description 
Maximum Bits/Sec Rx/Tx 
Maximum number of bits received/transmitted per second 
64 Octets 
Total number of received/transmitted 64-byte packets  
65–127 Octets 
Total number of received/transmitted 65–127-byte packets 
128–255 Octets 
Total number of received/transmitted 128–255-byte packets 
256–511 Octets 
Total number of received/transmitted 256–511-byte packets 
512–1023 Octets 
Total number of received/transmitted 512–1023-byte packets 
1024–1518 Octets 
Total number of received/transmitted 1024–1518-byte packets  
1519–2047 Octets 
Total number of received/transmitted 1519–2047-byte packets  
2048-Max Octets 
Total number of received/transmitted packets with 2048 bytes and up to  
maximum 
 To clear the statistics for a Logical MAC port: 
• 
At the prompt config>port>log-mac<slot>/<port>)#, enter clear-statistics. 
The statistics for the specified port are cleared. 
5.15 Management Ethernet Port  
Megaplex-4 has one out-of-band management Ethernet port (CONTROL ETH) located on each CL.2 
module panel dedicated to management traffic. The port has a 10BASE-T/100BASE-TX Ethernet 
interface. This interface supports MDI/MDIX crossover, and therefore the port can always be connected 
through a “straight” (point-to-point) cable to any other type of 10/100BASE-T Ethernet port (hub or 
station).  
The CONTROL ETH ports of both CL modules can be simultaneously connected to the same LAN, through 
standard Ethernet hubs or switches. 
To support out-of-band management, management stations, Telnet hosts, etc can be attached to the 
same LAN, or to any LAN from which IP communication with the CL.2 module Ethernet ports is possible. 