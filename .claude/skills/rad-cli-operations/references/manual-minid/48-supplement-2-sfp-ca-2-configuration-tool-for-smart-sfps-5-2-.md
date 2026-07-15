# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 5.2 SFP and DDM

*Manual `MiNID_ver_2_6_mn.pdf`, pages 98–100.*


## (chapter introduction)  *(p.98)*

5. Ports 
Oversize Frames                 0       -- 
LBM Reflector Frames            0       -- 
LBM Reflector Octets            0       -- 
For each of Tx (Transmit) and Rx (Receive), the displayed statistics include the following parameters: 
Ethernet Statistics Counters 
Parameter 
Description 
Total Frames 
All traffic, in number of frames 
Correct Frames 
All traffic not included in FCS Errors and not included in Undersize/Oversize 
Errors, in number of frames 
Total Correct Octets 
Same as Correct Frames, in bytes 
Frames Discarded (FIFO Full) 
Buffer overflow 
FCS Errors 
Frames not matching their Frame Check Sequence checksums 
Undersize Frames 
Frames under 64 bytes 
Oversize Frames 
Frames over the MTU size (default = 12000 bytes) 
LBM Reflector Frames 
LBM frames received by reflector 
LBM Reflector Octets 
LBM frame octets received by reflector 
You can clear the stored traffic statistics for each port, resetting all values to 0. 
 To clear statistics for a port: 
Do one of the following: 
• 
In the web interface, go to Monitoring > Physical Port > Ethernet > SFP/Port 1 or MSA/Port 2 > 
Statistics, and click Clear Statistics. 
• 
In the CLI, go to the configure port context, and enter: 
ethernet { sfp/1 | msa/2 } 
clear statistics 
5.2 SFP and DDM 
MiNID can display SFP and DDM details. 

## Applicability and Scaling  *(p.99)*


## Benefits  *(p.99)*


## Displaying SFP and DDM Details Using the Web Interface  *(p.99)*

5. Ports 
Applicability and Scaling 
SFP and DDM details can be displayed in all MiNID devices. 
Benefits 
DDM details are displayed via the MiNID. 
Displaying SFP and DDM Details Using the Web Interface 
 
If the SFP inserted into the MINID SFP sleeve is SGMII, DDM details are not displayed. 
 
 To display SFP and DDM details: 
• 
Navigate to MiNID > Monitoring > Physical Port >Ethernet > SFP. 
SFP and DDM information is displayed. 
MiNID 
 
 
 
 
 
Monitoring>Physical Port>Ethernet>SFP 
 
 
 
 
 
Operational Status 
 
Down 
 
Rate Mbps 
 
Not Available 
 
Active Media 
 
None 
 
 
 
 
 
Ethernet Compliance Codes 
 
1000BASE SX 
 
Connector Type 
 
LC 
 
Manufacturer Name 
 
WTD 
Note 

## Displaying SFP and DDM Details Using the CLI  *(p.100)*

5. Ports 
 
Typical Maximum Range 
(Meter 
 
550 
 
Wave Length (nm) 
 
850 
 
Fiber Type 
 
MM 
 
 
 
 
 
RX Power (dBm) 
 
-31.5 dBm 
 
TX Power (dBm) 
 
-5.8 dBm 
 
Laser Bias (mA) 
 
0.9 mA 
 
Laser Temperature (Celsius) 
 
57.0 C 
 
Power Supply 
 
3.18 V 
 
 
 
 
 
Statistics 
 
 
 
Displaying SFP and DDM Details Using the CLI 
 To display SFP and DDM details: 
• 
Navigate to configure port ethernet sfp and enter show status. 
The SFP and DDM details are displayed. 
 