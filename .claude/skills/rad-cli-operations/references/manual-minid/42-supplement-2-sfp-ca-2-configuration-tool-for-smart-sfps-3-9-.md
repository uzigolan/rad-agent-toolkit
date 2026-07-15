# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 3.9 Configuration of MiNID SFP via SFP-CA.2 (Telnet/SSH/Web)

*Manual `MiNID_ver_2_6_mn.pdf`, pages 86–87.*


## Working with Other SNMP-Based NMSs  *(p.86)*

3. Operation 
Working with Other SNMP-Based NMSs 
MiNID can be integrated into third-party network management systems (NMS) with basic autodiscovery 
and alarm functionality, by having MiNID send basic status SNMP traps to the NMS. MiNID must be 
configured to define the NMS as an SNMP Manager. 
SNMP (Simple Network Management Protocol) is an application-layer protocol that provides a message 
format for communication between managers and agents. MiNID acts as an SNMP agent, sending SNMP 
traps to up to two configured SNMP Managers. MiNID supports SNMPv1 and SNMPv2. 
The supported SNMP features are based on the following standards: 
Reference 
Title 
RFC 3418 
Management Information Base (MIB) for the Simple Network 
Management Protocol (SNMP) 
RFC 2863 
The Interfaces Group MIB 
The MiNID OIDs are: 
• 
For SPF sleeve – 1.3.6.1.4.1.164.6.1.6.36 
• 
For  SFP – 1.3.6.1.4.1.164.6.1.6.54 
3.9 Configuration of MiNID SFP via SFP-CA.2 
(Telnet/SSH/Web) 
You can use RAD’s SFP-CA.2 module for the following: 
• 
Configure MiNID SFP and MiNID SFP Sleeve by using SFP-CA.2 as a hosting device (possible only 
with a PC that has Windows XP SP2 installed) 
• 
Access the boot menu in order to upgrade MiNID software (possible only with a PC that has 
Windows XP SP2, Windows 7, or Windows 10 installed). Refer to Chapter 12 for more 
information on upgrading 
Note 
All SFP-CA.2 modules have the MAC address 00-00-E8-00-00-01. 

## Preconfiguration for SFP-CA.2  *(p.87)*


## Connecting SFP-CA.2  *(p.87)*

3. Operation 
Preconfiguration for SFP-CA.2 
When you connect SFP-CA.2 to a specific PC for the first time, if you wish to configure MiNID via 
SFP-CA.2 then you have to install the SFP-CA.2 driver on that PC, and configure the PC network 
parameters for communication with SFP-CA.2. Refer to the SFP-CA.2 supplement for instructions on how 
to download and install the driver. 
 To configure the PC network parameters for the SFP-CA.2 connection to MiNID: 
1. Connect the SFP-CA.2 configuration unit to a USB port on your PC.  
The New Hardware is Detected notice appears. 
2. Right-click My Network Places. 
A new local area network connection appears in the list of network connections.  
3. Right-click the new local area connection and rename it SFP-CA. 
4. Right-click Properties, click Configure, and select the Advanced tab 
The Network Connection Properties dialog box appears. 
5. Choose Select Media and under Value, choose Home LAN, and then click OK. 
The dialog box closes and your settings are applied. 
6. Right-click the SFP-CA connection and click Properties. 
The Local Area Connection Properties dialog box appears. 
7. Select Internet Protocol (TCP/IP) and click Properties. 
The Internet Protocol (TCP/IP) dialog box appears. 
8. To enable entering TCP/IP settings, select Use the following IP Address. 
The IP Address and Subnet Mask fields become available. 
9. Enter the following TCP/IP settings and then click OK: 
 
IP Address: 192.168.205.20 
 
Subnet Mask: 255.255.255.0 
10. Close My Network Places. 
The PC is ready to communicate with MiNID. 
Connecting SFP-CA.2 
For instructions on how to connect SFP-CA.2, see the Inserting  into an SFP-CA.2 section in Chapter 2. 