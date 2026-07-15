# 5 Ports

*Manual `MiNID_ver_2_6_mn.pdf`, pages 92–100.*


## 5.1 Physical Ethernet Ports  *(p.92)*

The MiNID ports are as follows, according to the ordering option: 
• 
SFP sleeve – MiNID has two Ethernet ports, one at each end, designated as: 
 
SFP – SFP slot, for provider-side SFP plug 
 
MSA – SFP plug side, for plugging into a customer device 
• 
MiNID SFP – MiNID has two Ethernet ports, one at each end, designated as: 
 
SFP – SFP (5DH / 6DH according to the ordering option) 
 
MSA – SFP plug side, for plugging into a customer device 
5.1 Physical Ethernet Ports 
You can configure autonegotiation behavior, and set the port MTU to a value from 2000–12000. 
Note 
• 
In MiNID /FE, the physical link is set to 100 Mbps full duplex, and 
autonegotiation is disabled, therefore configuring autonegotiation is 
relevant only for MiNID /GbE. 
• 
In MiNID /GbE, autonegotiation can be set for automatic discovery of the 
autonegotiation status between MiNID and the port with which it needs 
to communicate. 
 
 
Applicability and Scaling 
Ethernet ports exist in all MiNID devices, according to the ordering options as stated above. 
5. Ports 
Standards Compliance 
Autonegotiation is defined in IEEE 802.3ab. 
Benefits 
Autonegotiation enables optimal communications between communicating ports of different devices, 
without error-prone manual configuration. 
Factory Defaults 
By default: 
• 
Autonegotiation is disabled on both ports for MiNID/FE  
• 
Autonegotiation is set for automatic discovery on both ports for MiNID/GbE 
• 
MTU is set to 12000 
Configuring Port Parameters 
 To configure Ethernet port parameters: 
Do one of the following: 
• 
In the web interface: 
a. Go to Configuration > Physical Port > Ethernet > SFP/Port 1 or Ethernet > MSA/Port 2. 
b. Set Auto Negotiation: 
 
Discovery – Configure automatic discovery of autonegotiation status  
 
Enable – Enable autonegotiation 
 
Disable – Disable autonegotiation 
c. Set Force Direct I2C to Disable (valid for MSA port of MiNID SFP and SFP sleeve devices 
only). 
To enable the Force Direct I2C mode, select Enable, save the configuration and reboot MiNID. 
a. Set Force Speed (for SFP sleeve only) to Disable. 
b. To enable the Force Speed mode, select Enable, save the configuration and reboot MiNID. 
5. Ports 
c. Set MTU to the maximum data packet size that the port transmits  
(2000–12000). 
d. Click <Apply> to implement the changes, and then click <Save Configuration>. 
MiNID 
  
 
 
 
Configuration>Physical Port>Ethernet>SFP/Port 1 
  
 
 
 
Port Capability 
 
1000 Mbps, Full Duplex  
 
Auto Negotiation 
 
Discovery 
 
Force Direct I2C 
 
Disable 
 
Force Speed 
 
1000 
 
MTU (Bytes) 
 
12000 
  
 
 
Port Parameters – SFP/Port 1 
• 
In the CLI: 
a. Go to the configure port ethernet sfp/1 or configure port ethernet msa/2 context. 
The prompt config>port>eth(sfp/1)# or config>port>eth(msa/2)# is displayed. 
b. Set Auto Negotiation: 
 
To configure automatic discovery of autonegotiation status, enter: 
auto-negotiation discovery 
 
To enable autonegotiation, enter: 
auto-negotiation 
 
To disable autonegotiation, enter: 
no auto-negotiation 
c. Force Direct I2C (for MiNID SFP and SFP sleeve devices only): By default, MiNID serves as a 
proxy between the host device and the SFP.  
d. If force direct I2C is enabled, the proxy is disabled and MiNID is transparent between the 
host device and the SFP. 
e. If force direct I2C is disabled, MiNID remains in proxy mode only when one of the following 
cases occurs: 
 
Plugged SFP is DDM.
 
5. Ports 
 
Force Speed mode is enabled.  
f. If none of the conditions above are met, MiNID automatically forces the direct I2C 
connection and moves to transparent mode. 
To enable the Force Direct I2C mode, go to the configure port ethernet  msa context, enter force-direct-
i2c, save the configuration, and reboot MiNID. 
Note 
Force Direct I2C is valid only for MSA port parameters. 
 
a. Force Speed (for SFP sleeve only): Force the speed of the MSA port to  
1 GbE. Save the configuration and remove the MiNID from the socket. Once you plug it back 
in, the new configuration is accepted. When working with 1GbE on the MSA side and FE on 
the SFP port, the traffic received from the MSA side must be shaped to 100 M.  
Force Speed can be enabled only when the Force Direct I2C mode is disabled, i.e. when the host device 
is not connected directly to the SFP via I2C. 
a. To set MTU to the maximum packet size that the port transmits  
(2000–12000), enter: 
mtu <mtu-size> 
Viewing Port Status 
You can view the operational status (Up/Down) and current traffic rate (100/1000 Mbps). 
 To view port status: 
Do one of the following: 
• 
In the web interface, go to Monitoring > Physical Port > Ethernet > SFP/Port 1 or MSA/Port 2: 
MiNID 
5. Ports 
  
 
 
 Monitoring>Physical Port>Ethernet>MSA/Port 2 
  
 
 
 Operational status 
 
UP 
 Rate (Mbps) 
 
1000 
 Active Media 
 
Fiber 
 Statistics 
 
 
 SFP Details 
 
 
Port Status – MSA/Port 2 
• 
In the CLI, go to the configure port context, and enter: 
ethernet { sfp/1 | msa/2 }  
show status 
For example: 
MiNID>config>port# ethernet msa 
MiNID>config>port>eth(msa/2) # show status 
Operational Status -     UP 
Rate (Mbps)        -     1000 
Active Media       -     Copper 
Viewing Port Statistics 
You can view per-port traffic statistics. 
 To view port statistics: 
Do one of the following: 
• 
In the web interface, go to Monitoring > Physical Port > Ethernet > SFP/Port 1  or MSA/Port 2, 
and click Statistics: 
MiNID 
5. Ports 
 
 
 
 
 
 
Monitoring>Physical Port>Ethernet> MSA/Port 2 >MSA/Port 2 Statistics 
 
 
 
 
 
 
 
 
---RX--- 
---TX--- 
 
Total Frames 
 
19519 
1514 
 
Total Correct Frames 
 
19519 
1514 
 
Total Correct Octets 
 
1346023 
201966 
 
Frames Discarded (FIFO Full) 
 
0 
0 
 
FCS Errors 
 
0 
 
 
Undersize Frames 
 
0 
 
 
Oversize Frames 
 
0 
 
 
LBM Reflector Frames 
 
0 
 
 
LBM Reflector Octets 
 
0 
 
 
 
 
 
 
 
Clear Statistics 
 
 
 
 
 
 
 
 
Port Statistics – MSA/Port 2 
• 
In the CLI, go to the configure port context, and enter: 
ethernet { sfp/1 | msa/2 } 
show statistics 
For example: 
MiNID>config>port# ethernet msa/2 
MiNID>config>port>eth(msa/2)# show statistics 
 
 
 
--Rx--  --Tx-- 
Total Frames                    329     293 
Correct Frames                  329     293 
Total Correct Octets            29074   24332 
Frames Discarded (FIFO Full)    0       0 
FCS Errors                      0       -- 
Undersize Frames                0       -- 

## 5.2 SFP and DDM  *(p.98)*

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
 