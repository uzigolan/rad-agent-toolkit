# 5 Cards and Ports – 5.22 TDM Bridge Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 437–438.*


## Applicability and Scaling  *(p.437)*

5. Cards and Ports 
Parameter 
Description 
PCV 
Displays the number of P-bit Coding Violations (PCV). 
A P-bit Coding Violation or a P-bit Parity Error event is the occurrence of a received P-bit 
code on the DS3 M-frame that is not identical to the corresponding locally-calculated 
code. 
CES 
Displays the number of C-bit Errored Seconds (CES). 
 A CES is a second with one or more CCVs OR one or more Out of Frame defects OR 
detected incoming AIS.  This count is only for the SYNTRAN and C-bit Parity DS3 
applications.  This gauge is not incremented when UASs are counted.  
PSES 
Displays the number of P-bit Severely Errored Seconds (PSES)  
A PSES is a second with 44 or more PCVs OR one or more Out of Frame defects OR 
detected incoming AIS.  This gauge is not incremented when UASs are counted. 
CSES  
Displays the number of C-bit severely errored seconds (CSES) in the current interval. 
A CSES is a second with 44 or more CCVs OR one or more Out of Frame defects OR 
detected incoming AIS.  This count is only for the SYNTRAN and C-bit Parity DS3 
applications.  This gauge is not incremented when UASs are counted. 
SEFS 
Displays the number of Severely Errored Framing Seconds (SEFS) 
A SEFS is a second with one or more Out of Frame defects OR detected incoming AIS.  
This item is not incremented during unavailable seconds.   
 To clear the statistics for a T3 port: 
• 
At the prompt config>port>t3<slot>/<port>)#, enter clear-statistics. 
The statistics for the specified port are cleared. 
5.22 TDM Bridge Ports  
Applicability and Scaling 
To implement specific bidirectional broadcast applications over serial ports of VS modules, Megaplex-4 
architecture uses an entity named TDM bridge port. TDM bridge ports exist only on VS modules and are 
mapped to serial ports. The maximum number of TDM bridge ports is 4 per VS-12 module and 6 per VS-
6/C37, VS-6/BIN, VS-6/FXS, VS-6/FXO, VS-6/E&M modules.  

## Standards Compliance  *(p.438)*


## Factory Defaults  *(p.438)*


## Configuring TDM Bridge Ports  *(p.438)*


## Example  *(p.438)*

5. Cards and Ports 
Standards Compliance 
TDM bridge ports are RAD proprietary technology. 
Factory Defaults 
Megaplex-4 is supplied with all TDM bridge ports disabled. 
Configuring TDM Bridge Ports 
 To configure a TDM Bridge port: 
1. Navigate to configure port tdm-bridge <slot>/<port> to select the TDM bridge port to 
configure. 
The config>port>tdm-bridge>(<slot>/<port>)# prompt is displayed.  
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Assigning short description to 
port 
name <string> 
Using no name removes the name 
Administratively enabling port 
no shutdown 
Using shutdown disables the port 
Binding the serial port to the tdm-
bridge port  
 
bind serial <slot>/<port> 
 
 
Serial slot number must be the same as 
tdm-bridge slot number.  
Using no before the corresponding 
command removes the binding 
Example 
See DS0 Cross-Connect section in Chapter 8, Example 9. 