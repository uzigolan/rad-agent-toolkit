# 1 Introduction

*Manual `SecFlow-1p_6.4_Mn_05-26_GA.pdf`, pages 47–71.*


## 1.1 Overview  *(p.47)*

1. Introduction 
1 Introduction 
1.1 Overview  
SecFlow-1p is an industrial IoT gateway, a member of RAD’s SecFlow suite of ruggedized Ethernet 
products. It is an open platform hosting third-party software, besides its communication capabilities.  
In its maximum configuration, SecFlow-1p can support: 
• 
Four GbE Copper ports 
• 
Two GbE SFP ports 
• 
Two serial ports (single RS-232 port or one RS-232 plus one RS-485/2W) 
• 
Built-in WiFi modem, GPS receiver for location indication and a cellular modem with two SIM 
cards or two modems for maximum link resiliency 
SecFlow-1p is equipped with serial interfaces for connectivity of legacy equipment. As a gateway it 
converts legacy serial protocols to modern IP-based protocols, enabling seamless communication from 
the IP SCADA to both the old and new RTUs. This provides a single box solution for multi-service 
applications and smooth migration to all-IP networks.  
SecFlow-1p features DIN-rail mounting, IP30 protection level, and wide operating temperature range 
(-40°C to 65°C), fanless. 
 
1. Introduction 
Example of a SecFlow-1p Unit 
 
Features  
Connectivity  
SecFlow-1p provides rich WAN connectivity over diverse access technologies, including Ethernet, 
IP/MPLS, WLAN and 4G/LTE.  
Hybrid WAN connectivity with ACTIVE/ACTIVE support enables high availability service using multiple 
links.  
SecFlow-1p provides Ethernet, LTE and WiFi LAN connectivity. 
Management and Security 
The digital transformation accelerates the pace of adoption of new services. SecFlow-1p is designed to 
simplify operations, while providing the service provider with visibility to its branch office demarcation. 
SecFlow-1p incorporates secure Zero-Touch-Provisioning mechanisms for agile and seamless OS 
deployment, reducing truck rolls and minimizing mass deployment operating costs. 
To automate setting up of overlay connectivity to the data center, SecFlow-1p can be integrated with 
the service provider’s SDN controllers or orchestration systems, using NETCONF/YANG modeling.  
SecFlow-1p can also be managed via WEB, CLI or by RADview.  
Management Capabilities 
• 
Secure remote management via any port using SSH, SNMP, NETCONF/YANG, or RADview, RAD’s 
SNMP-based management system 
• 
Zero Touch, allowing SecFlow-1p to receive software and configuration files automatically 
without having to manually log into SecFlow-1p. Supported over VPN and Public networks. 
• 
Performance Management – SecFlow-1p maintains performance management (PM) statistics. 
The PM statistics are collected into a file that can be read using RAD’s RV PM-portal for further 
analysis and presentation. 
1. Introduction 
• 
SecFlow-1p access control lists (ACLs) flexibly filter management traffic. Data ACLs with a single 
Permit rule are also supported for IPsec only, to set the traffic permitted through the IPsec 
tunnel and thus protected by IPsec. 
Console Port  
vCPE-OS can be installed on a white box with the following ports: 
• 
USB port for installation of vCPE-OS image from disk-on-key 
• 
Mini USB or serial (RS-232 or similar) port to which a console can be connected for management 
via CLI 
 
Note 
The mini USB port has neither configuration nor monitoring parameters.  
File Transfer Protocols 
vCPE-OS supports SCP, SFTP, FTP and FTPs client functionality.  
Security Protocols 
SecFlow-1p supports the security protocols listed below, ensuring client-server communication privacy 
and correct user authentication: 
• 
SNMPv3 (provides secure access to the device by authenticating and encrypting packets 
transmitted over the network) 
• 
RADIUS (client authentication) 
• 
TACACS+ (client authentication) 
• 
SSHv2 for Secure Shell communication session 
DHCP and DHCPv6 Client and Server 
SecFlow-1p supports Dynamic Host Configuration Protocol (DHCP) server functionality for IPv4 clients. 
Based on the Bootstrap Protocol (BOOTP), DHCP server assigns to DHCP clients IPv4 addresses from 
configured pools, as well as various configuration parameters (DHCP options), in response to the 
broadcast requests of DHCP clients. This functionality eliminates the need to assign an IP address for 
each potential client. 
SecFlow-1p supports DHCP and DHCPv6 client functionality working opposite IPv4 and IPv6 servers to 
get network IP addressing as well as other configuration parameters (DHCP options) that facilitate the 
device’s ZT functionality.  
1. Introduction 
Traffic Processing 
Layer-3 Forwarding 
SecFlow-1p provides Layer-3 forwarding, with multiple Virtual Routing and Forwarding instances (VRFs). 
Up to 10 routers and 32 router interfaces are supported.  
SecFlow-1p supports static routing definitions, Border Gateway Protocol (BGP) and OSPF. 
Network Address Translation (NAT)  
SecFlow-1p supports Network Address Translation (NAT), a method that maps IP addresses (IPv4 only) 
from one IP domain to another in an attempt to provide transparent routing to hosts. 
IPsec Tunneling 
SecFlow-1p supports IPsec on router interfaces to secure private communication across public IP 
networks.  
GRE Tunneling  
SecFlow-1p supports Generic Routing Encapsulation (GRE) protocol, which sets up Layer-3 point-to-point 
connectivity between two remote sites (over an underlay Layer-3 network). 
Layer-2 Forwarding  
SecFlow-1p supports up to two bridges and up to 32 bridge ports. The bridge ports can be bound to 
Ethernet ports. The bridge entity enables users to perform local switching. 
Layer-3 Quality of Service (QoS)  
SecFlow-1p supports Quality of Service (QoS), i.e. traffic management, on Ethernet and Cellular ports to 
ensure that traffic with specific characteristics, such as management, is guaranteed specific bandwidth 
with minimum delay. 
QoS support also includes classification – classifying traffic into traffic-classes on the ingress directions of 
a port. Traffic class defines actions such as fixed Class of Service (CoS) mapping on the ingress direction 
of an Ethernet port and DSCP marking.  
Monitoring and Diagnostics 
SecFlow-1p offers several types of diagnostic procedures: 

## 1.2 New in this Version  *(p.51)*

1. Introduction 
• 
Fault Propagation 
• 
Syslog – Syslog protocol generates and transports event notification messages from SecFlow-1p 
to servers across IP networks. 
• 
Ping Test – SecFlow-1p can ping a remote IP host to check SecFlow-1p IP connectivity with that 
host. 
• 
Trace Route – SecFlow-1p can quickly trace a route through the network from SecFlow-1p. 
Timing 
You can configure the SecFlow-1p internal real-time clock as free running or with Network Time Protocol 
(NTPv4). 
1.2 New in this Version  
 
New Features 
Comments 
Enclosure, Cards and Ports 
New Global 5G modem (Ready for PoC) 
 
New TAA compliant (L4T) modem for North 
American market (ready for PoC) 
 
LoRa Gateway ID is now editable 
 
Management and Security 
Trusted Platform Module (TPM 2.0) 
 
Linux kernel upgraded to latest version 
 
Password Enforcement 
 
Resiliency and 
Optimization 
ERPS G.8032 (Ethernet Ring Protection Switching) 
 
SD-IOT (L2oL3 client, including high availability) 
 
Monitoring and Diagnostics 
Device log report generation 
 
LoRaWAN packet forwarder and MQTT status 
display 
 
Web GUI 
Enhanced LoRaWAN GUI 
 
 
 

## 1.3 Product Description  *(p.52)*

1. Introduction 
1.3 Product Description  
Hardware Description 
Front Panel Interfaces 
 
 
SecFlow-1p Front Panel Interfaces 
*Model Dependent 
Power, Ground, Alarm, and Cards Panel  
Various power supply options are supported. Below is an example showing the panel of a unit 
supporting 12-48VDC with non-isolated power supply).  The available power supply options and 
connections are detailed under Power. 
1. Introduction 
 
Panel Example – 12-48VDC Non-isolated Power Supply 
 
Note 
SIM slots have a protective cover. 
1. Introduction 
 
Antenna Panels 
The antenna panel provides the relevant antenna connections, according to your order. Below are 
several examples:  
    
 
 
MIMO WiFi and GPS  
 
 
 
 
LoRa and GPS 
 
 
 
LTE and GPS  
 
 
 
 
 
WiFi Halow and GPS 
1. Introduction 
Front Panel LEDs (Model Dependent) 
LED  
Color 
Description 
ALM   
Red 
Alarm status: 
OFF – no alarm 
ON – at least one alarm has been triggered 
RUN  
Green 
Unit system status: 
ON – Normal operation, system is up 
OFF – No power or at early boot stage 
Flashing – During Zero Touch procedure 
PWR 
Green 
Power input: 
ON – power input OK 
OFF – no power  
SIM status  
 
Green 
Two LEDs (one per SIM):  
• On – SIM card is enabled and inserted 
• Off – no SIM card in the slot or SIM card is disabled 
• Flashing – SIM card is connected to mobile network 
LTE signal  
Green 
RSSI indication, as follows: 
• Four LEDs ON – Excellent signal; RSSI [dBm}: S > -60 
• Three lower LEDs ON – Good signal; RSSI [dBm}: -60 > S > -75 
• Two lower LEDs ON – Fair signal; RSSI [dBm}: -75 > S > -85 
• One lower LED ON – Poor signal; RSSI [dBm}: -85 > S > -105 
• All LEDs OFF – No signal; RSSI [dBm}:  S < -105 
WiFi 
Green 
ON – port physically up 
Flashing – sending/receiving data 
AUX 
Green/Red 
Red blinking – Reboot in process 
Red Lit – ZTP in process 
Green Lit – Connected with MQTT server 
Green blinking – MQTT server configured but not connected 
Link/Act 
Green 
ON – Ethernet interface is synchronized 
Flashing – sending/receiving data 
Serial S1/S2 
Green 
TX blinking – Port is transmitting data 
RX blinking – Port is receiving data 

## 1.4 Technical Specifications  *(p.56)*

1. Introduction 
1.4 Technical Specifications  
 
Note 
Asterisk (*) marking the feature means that the feature will be released in a 
future version. Some of these features are described in the manual and 
marked with the asterisk.  
 
Hardware Specifications  
Memory and Storage 
DRAM  
1 Gb, 2 Gb  
Flash Storage  8 Gb, 32 Gb  
Interfaces 
Ethernet  
2 x 10/100/1000BASE-T ports (2U ordering option) 
2 x 1000FX, 4 x 10/100/1000BASE-T ports (4U2S ordering option) 
LTE 
LTE modem with dual SIM 
Wi-Fi 
802.11b/g/n/ac dual band 
Serial ports 
1 RS-232 interface 
2 RS-232 interfaces (non-isolated or isolated) 
1 RS-232, 1 RS-485 interfaces (non-isolated or isolated) 
Connector: RJ-45 
GNSS 
GPS – American (default)  
Galileo – European 
SD Card 
Max size: 32GB 
 
1. Introduction 
 
Modems 
Dual SIM 
Cellular 
Modem 
LTE bands – see Table below 
EVDO networks (technology backward compatible) 
Firmware 
Upgrade 
FOTA (Firmware upgrade Over the Air) 
LoRaWAN 
Module 
EU868, RU864, US915, AS923 (1-4), AU915, KR920, IN865 bands 
SX1303 baseband processor  
8 x 8 channels LoRa packet detectors 
8 x SF5-SF12 LoRa demodulators, 
8 x SF5-SF10 LoRa demodulators 
LoRaWAN Class A, B, C 
Packet forwarder 
Tx power: up to 27 dBm  
Rx sensitivity: down to -139 dBm @ SF12, BW 125 kHz 
Configurable 
Cellular 
Authentication 
PAP, CHAP 
SIM Card 
Mini SIM, 25 mm x 15 mm (0.98 in x 0.59 in 
Form factor: 2 FF 
WiFi Module  
IEEE 802.11ac/a/b/g/n 
Dual band 2.4 GHz or 5 GHz (software selectable) 
Up to 8 users 
Integrated LTE Modems 
1. Introduction 
LTE Ordering Code 
Modem Category and Frequency Bands 
L1 
CAT 4 EMEA/Korea/Thailand  
LTE FDD: B1/B3/B5/B7/B8/B20 
LTE TDD: B38/B40/B41 
WCDMA: B1/B5/B8 
GSM: B3/B8 
L3 
CAT 4 Australia/New Zealand/Taiwan/Brazil 
LTE FDD: B1/B2/B3/B4/B5/B7/B8/B28 
LTE TDD: B40 
WCDMA: B1/B2/B5/B8 
GSM: B2/B3/B5/B8 
L4  
CAT 4 North America, Verizon wireless + AT&T LTE  
LTE FDD: B2/B4/B5/B12/B13/B14/B66/B71  
WCDMA: B2/B4/B5 
L4P  
CAT 4 North American private networks (Anterix & CBRS) + Public networks 
LTE TDD: B48   
LTE FDD: Anterix B8                          
LTE FDD: B2, B4, B5, B12, B13, B14, B26, B66 
L5 
CAT 4 Japan  
LTE FDD: B1, B3, B8, B18, B19, B26 
LTE TDD: B41 
WCDMA: B1, B6, B8, B19  
LTA 
CAT 4 North America, TAA-compliant 
LTE: B2, B4, B5, B12, B13, B14, B25, B26, B66, B71 
WCDMA: B2, B4, B5  
L450A 
CAT 4 450 MHz for private LTE networks 
LTE-FDD: B3/7/20/31/72  
L450B 
CAT 4 450 MHz for private LTE networks 
LTE-FDD: B3/20/87 
1. Introduction 
Antennas  
Depending on the ordering option, your package may include a number of antennas supplied along with 
the modems. For instructions on the antenna installation, refer to Installing Antennas. 
Cellular Antennas – Embedded  
 
Embedded LTE (L1, 
L3)  
Embedded LTE (L4) 
Embedded LTE  
(L450A, L450B) and 5G 
Embedded LTE (L5) 
Description 
Embedded 
antenna for 
devices with L1 
and L3 cellular 
modem 
Embedded antenna 
for devices with L4 
cellular modem 
Embedded antenna for 
devices with L450 and 
5G cellular modems 
Embedded antenna for 
devices with L5 cellular 
modem 
Photo 
 
 
Frequencies 
[Mhz] 
690-960 
1400-2170 
2300-2700 
699-960  
1710-2690  
  
 
410-496  
617-960  
1427-2690  
3300-5000  
5150-5925 
698-960 
1710-2170 
2500-2700 
 
 
  
 
Impedance 
50 Ohms 
50 Ohms 
50 Ohms 
50 Ohms 
Polarization 
Linear 
Linear 
Linear 
Linear 
1. Introduction 
 
Embedded LTE (L1, 
L3)  
Embedded LTE (L4) 
Embedded LTE  
(L450A, L450B) and 5G 
Embedded LTE (L5) 
Gain 
maximum Peak 
Gain: 4 dBi 
See Embedded LTE 
(L4) Antenna – Gain 
and VSWR table below 
See Embedded LTE 
(L450A, L450B) and 5G 
Antenna – Gain and 
VSWR table below 
See Embedded LTE (L5) 
Antenna – Gain and 
VSWR table below 
VSWR 
<2 
See Embedded LTE 
(L4) Antenna – Gain 
and VSWR table below  
See Embedded LTE 
(L450A, L450B) and 5G 
Antenna – Gain and 
VSWR table below 
See Embedded LTE (L5) 
Antenna – Gain and 
VSWR table below 
IP/IK ratings 
IP67 
IP67, IK09 
IP67 
IP67 
Connector 
type 
SMA male 
SMA male 
SMA male 
SMA male 
Cable 
none 
none 
none 
none 
Embedded LTE (L450A, L450B) and 5G Antenna – Gain and VSWR 
Frequencies 
[Mhz] 
410-496 
617-960 
1427-2690 
3300-5000 
5150-5925 
Peak Gain 
[dBi] 
-4.5 
0.5 
2.1 
1.5 
2.5 
Avg. Gain [dB] 
-7 
-4.2 
-2.4 
-4.4 
-5.5 
VSWR 
3.8:1 
1.7:1 
2.5:1 
4.1:1 
2.1:1 
Embedded LTE (L4) Antenna – Gain and VSWR 
Frequencies [Mhz] 
698-960 
1710-2170 
2500-2700 
Peak Gain [dBi] 
0.4 
2.6 
1.3 
Avg. Gain [dB] 
-2.1 
-1.3 
-3 
VSWR 
2.4:1 
1.6:1 
2.2:1 
 
1. Introduction 
Cellular Antennas – External  
 
SF-ANT3G-2M(5M) 
SF-ANT4G-2M(5M) 
SF-ANT-LTE700-7DBI-MGNT 
Description 
Outdoor antenna 3G cellular 
modem,2 m (5 m) connecting 
cable, 824-894 MHz/900 
MHz/1800 MHz/1900 MHz 
Outdoor antenna for 4G 
cellular modem, 2 m (5 m) 
connecting cable, 699-960 
MHz/1710-2170 MHz/2500-
2690 MHz 
Outdoor magnetic base 
antenna for LTE options and 
for LoRaWAN 868 and 915 
MHz, 7 dBi  
Photo 
 
 
 
Electrical Specifications 
Frequencies 
AMPS (824-894 MHz) 
ISM (868 MHz) 
GSM (900 MHz) 
DCS (1800 MHz) 
PCS (1900 MHz) 
3G (UMTS 2.1 GHz) 
WIFI / BLUETOOTH (2.4 GHz) 
4G/LTE  
699-960 MHz /  
1710-2170 MHz /  
2500-2690 MHz 
700-960 MHz 
1710-2170 MHz 
2500-2700 MHz 
Impedance 
50 Ohms 
50 Ohms 
50 Ohms 
Polarization 
Linear 
Vertical 
- 
Gain 
2.2 dBi avg.* 
3 dBi typ. 
7.0 dBi 
VSWR 
<2.6:1**  
699-960 MHz <5:1 /  
1710-2690 MHz <3:1*** 
< 2.5 
IP/IK ratings 
IP67 
IP67, IK09 
- 
Connection Specifications 
Connector 
type 
FME female 
SMA male 
SMA male 
Cable 
RG174U 
RG174 
RG195 
1. Introduction 
 
SF-ANT3G-2M(5M) 
SF-ANT4G-2M(5M) 
SF-ANT-LTE700-7DBI-MGNT 
Cable length 
2m/5m 
2m/5m 
3m  
*Antenna gain depend on size of the ground plane 
**VSWR stated when measured with 2.5m RG174 on 50x50cm ground-plane 
***Values stated when measured on 50x30cm ground plane 
GPS Antenna 
 
SF-ANT-GPS-PAS-3DBI-MAG/3M 
Description 
GPS passive antenna, 3m 
Photo 
 
Electrical Specifications 
Center Frequency 
1575.42 ± 3 MHz 
Band Width 
CF  ± 5 MHz 
Impedance 
50 Ohms 
Polarization 
RHCP 
Gain (Zenith) 
3 dBic 
VSWR 
1.5 
Connection Specifications 
Connector type 
SMA male 
Cable 
RG174 
Cable length 
3 m 
LoRaWAN Antenna  
 
SF-ANT-LORA-3DBI-SMA 
Description 
Outdoor antenna for LoRaWAN modem options, 3 dBi 
1. Introduction 
 
SF-ANT-LORA-3DBI-SMA 
Photo 
 
Electrical Specifications 
Frequency 
EU433, EU868, AU915, US915, AS923 
Impedance 
50 Ohms 
Polarization 
Vertical 
Gain 
3 dBi 
VSWR 
< 1.5 
Connection Specifications 
Connector type 
SMA 
Cable length 
48 mm 
WiFi Antenna 
 
SF-ANT-WIFI-DUALBAND-3DBI-SMA 
Description 
WiFi dual band antenna, 3 dBi, for options with WiFi modem 
Photo 
 
Electrical Specifications  
Frequencies 
2.4–2.5 GHz 
5.15–5.85 GHz 
Impedance 
50 Ohms 
Polarization 
Linear Vertical 
Gain 
2.37 dBi 
2.93 dBi 
1. Introduction 
 
SF-ANT-WIFI-DUALBAND-3DBI-SMA 
IP/IK ratings 
IP-65 
Connection Specifications 
Connector type 
RP-SMA male straight connector 
Cable 
RG-178 coaxial cable 
Management and Diagnostics 
Console Port 
Ethernet port with the highest number (4 or 6, according to the device ordered), RJ-45 
connector 
Note: Console cable is not included and must be ordered separately (see Optional 
Accessories). 
LEDs 
Including alarm indication and cellular RSSI level 
Dry Contacts 
2 In, 2 Out  
3 In, 1 Out (special ordering option)  
Maximum rating: 60 VDC, 1A 
Maximum switching power: 30W, 37.5VA  
General 
Compliance 
EMC: EN 55032, EN 55035, EN 50121-4*, ETSI EN 301 489-1, ETSI EN 301 908-1, CFR 47 
FCC, VCCI-CISPR 32, AS/NZS CISPR 32 
EU: CE 
FCC and TUV for North America 
Safety:  UL 62368-1, IEC/EN 62368-1 
Industry standards: IEC 61850-3, IEEE 1613** 
Hazardous locations standards: UL 121201, CSA C22.2 (Class 1 & 2, Division 2 & Class3, 
Div 1 & 2 Hazardous)* 
US Carrier: PTCRB, AT&T, Verizon*, T-Mobile* 
** Please contact the PLM for a certified platform 
1. Introduction 
Environment 
Storage 
Temperature 
-40 to 85°C (-40 to 185°F) 
Operating 
Temperature 
DIN rail: -40 to 65°C (-40 to 149°F) 
Humidity 
Up to 90% 
Physical 
Height mm (in) 
138 (5.43) 
Width 
53.3 (2.1) 
Depth 
123.3 (4.85) 
Weight 
0.88 kg (1.94 lb) 
Power  
DC  
12-24-48 VDC (10-60 VDC) 
Non-isolated 
WDC 
24-48 VDC (20-60 VDC) 
12-24-48 VDC (10-60 VDC in future versions)* 
Isolated 
12V 
12- 24 VDC (11-30 VDC) 
Isolated 
EXT AC Power 
Supply 
90–240VAC 
Power Consumption < 5W  
Idle: 3.0W**  
Typical: 3.6W** 
Maximum: 4.5W** 
**On a platform with one LTE modem 
 
1. Introduction 
Software Specifications 
Management 
Configuration 
Web-based interface using HTTPS or HTTP 
CLI with password-protected access 
Protocols 
NETCONF server (v1.0/v1.1)/ YANG 
SNMP v2/v3 
Telnet, SSH v2, HTTPS server, TFTP/SFTP 
Users 
User roles and privileges 
Monitoring and 
Diagnostics 
Syslog 
Traceroute, ping 
Alarm and event logs 
DHCP Server 
IPv4, IP subnet pools support 256 addresses 
IP Addressing and Routing 
Addressing 
IPv4 and IPv6 
Routing 
Protocols 
OSPF v2, BGP v4 
VRRP 
IP-BFD for fast route propagation* 
Routing 
Technologies 
Static  
Policy-based 
VRF (10), Router Interfaces (32) 
NAT 
Static/dynamic 
NAPT/NAT 
DHCP 
Client, server, relay 
1. Introduction 
IP helper addresses 
DNS 
Server 
Resiliency and Optimization 
Link 
Redundancy 
Tracking connectivity to specific IP addresses 
using fault propagation and IP monitoring 
functionalities 
Monitoring and Diagnostics 
Features 
Syslog 
Traceroute, ping 
Alarm and event logs 
Timing 
Date and 
Time 
Local time setting 
Protocol 
SNTPv4 
IP Quality of Service  
Classification Port-based, IP-based, DSCP 
Egress 
Queues 
8 queues per port 
Queuing 
Class-based, SPQ, WFQ 
Scheduling 
Strict Priority / WRR 
Traffic Class 
Actions 
CoS mapping (queues)  
Marking, remarking (DSCP) 
Traffic 
Processing 
Shaping 
1. Introduction 
Security  
Trusted Platform 
Module 
Secure boot 
TPM2.0 
Access Lists 
Standard and extended  
Firewall 
Zone-based, stateful ACL rules  
Session 
Monitoring and limiting 
Authentication 
Locally, RADIUS, TACACS+ (also for 
authorization and accounting) 
Port-based: 802.1X on Ethernet and Wi-Fi  
Multi-factor authentication (MFA) 
One-time password (OTP) 
Public Keys 
Public Key Infrastructure with X.509 
certification for Zero Touch 
Certificates with SCEP CA server 
Features 
Login lockout 
IP VPNs 
Protocols 
Policy- and route-based IPsec, GRE  
GREoIPsec 
IKEv1, IKEv2  
DMVPN client, DMVPN phase 3 
L3 IPsec VPN 
PPPoE supporting Broadband or LTE access 
ESP Algorithms 
AES CTR 128, 256 and 192, AES GCM 128 and 256, 
ChaCha20-Poly1305  
1. Introduction 
IKE Algorithms 
ECDH-SHA2 NISTP 521, 384 and 256, Curve25519-
SHA256, DH-Group18-SHA512, DH-Group17-SHA512, 
DH-Group16-SHA512, DH-Group15-SHA512, DH-
Group14-SHA256, DH-GEX-SHA256 
IKE Hashing 
Algorithms 
SHA2-256-128-HMAC, SHA2-512-256-HMAC 
DH Groups  
1 (768-bit modulus)  
2 (1024-bit modulus)  
5 (1536-bit modulus)  
14 (2048-bit modulus)  
19 (256-bit elliptic curve)  
20 (384-bit elliptic curve) 
Technologies 
NAT traversal 
Interoperability with SCEP server 2012 and higher 
Edge Computing (Containers) 
Containers 
Docker 
Zone-based Firewall  
Type 
Stateless  
Stateful  
IPv4 and IPv6 NAT 
SNAT, DNAT 
REDIRECT  
NAPT/NAT 
Configuration 
via Web GUI, SSH and SNMP 
Rules 
Interfaces are assigned to zones, for which a 
set of rules is configured  
IPv4 and IPv6  
Limit maximum number of simultaneous 
connections 
1. Introduction 
Limit rules by traffic (kilobyte per 
second/packet per second) 
Rule hits reported to local LINUX Syslog* 
DoS Prevention 
Blacklist 
Defend from IP sweep  
Integrated Routing and Bridging (IRB) 
Operation Mode 
VLAN aware VLAN un-aware 
Static or Dynamic MAC addresses 
Max number of bridges 
2  
Max number of bridge 
ports 
32 
Max MAC addresses per 
bridge 
512 
Wi-Fi 
2.4/5 GHz 
Mode 
Access Point, Client 
Radio mode 802.11a/b/g/n/ac 
Security 
WPA2-AES 
Users 
8 concurrent 
HaLow 
Radio Mode 802.11ah Wi-Fi HaLow  
Bands 
902.0 ~ 928.0 MHz 
Bandwidth 
1/2/4 MHz  
Security 
OPEN, WPA2-PSK (AES), WPA3-OWE, WPA3-SAE  
1. Introduction 
OFDM modulation with AES-CCMP encryption 
Users 
22 concurrent  
Mode 
Access point  
Station mode 
Simultaneous GATT server & client 
Data Rate 
Up to 4 Mbps  
Range  
Up to 1 km  
Tx Power 
Gain 
+23 dBm  
Max Input 
Level 
-10 dBm  
Cellular and GPS 
LTE 
Single SIM 
Dual SIM 
Dual LTE modems 
Operation Modes 
PPP, Eth/DHCP 
GPS 
Location reporting 
OAM 
SLA Monitoring  
ICMP echo, UDP echo  
ZTP 
On-net 
Off-net (over unsecured network) performs secure “call 
home” using Public Key Infrastructure (X.509) 
 