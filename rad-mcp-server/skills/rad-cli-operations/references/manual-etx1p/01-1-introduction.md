# 1 Introduction

*Manual `ETX-1p_6.4_Mn_05-26_GA.pdf`, pages 45–66.*


## 1.1 Overview  *(p.45)*

1. Introduction 
1 Introduction 
1.1 Overview  
ETX-1p is a branch office Physical CPE enabling business customer transformation to the cloud. It 
enables service providers to deliver IP-VPN services as well as value added virtual services from the 
data-center to the customer branch.  
ETX-1p combines powerful networking capabilities with flexible connectivity options and rich 
management interfaces. It is an ideal solution for delivering cloud based services in small and medium 
branch offices along with traditional IP-VPN services. 
ETX-1p is bundled with RAD’s pCPE-OS, compatible with ETX-1p used for universal CPEs, except support 
of Virtual Machines (VMs).  
For integration with operational and business support systems, orchestration systems and SDN 
controllers, ETX-1p features an open management platform, supporting integration by NETCONF/YANG 
or SNMP. 
 
Features  
Networking  
ETX-1p is the service provider’s demarcation point at branch offices, enabling underlay connectivity to 
IP-VPN and Broadband networks, as well as overlay connectivity to the service provider’s data center. 
Branch offices consume their networking services from the service provider’s data center, including IP-
VPN connectivity to other branch offices, Internet access and public cloud access. The service provider 
also delivers value-added-services from its data center, including networking (i.e., voice, secure Internet 
access) and IT (i.e., cloud on-ramp) services. Branch site underlay connectivity is resilient with a backup 
link, typically connected to a broadband network.    
1. Introduction 
Connectivity  
ETX-1p provides rich WAN connectivity over diverse access technologies, including Ethernet, IP/MPLS, 
WLAN and 4G/LTE.  
Hybrid WAN connectivity with ACTIVE/ACTIVE support enables high availability service using multiple 
links.  
ETX-1p provides Ethernet, LTE and WiFi LAN connectivity. 
Management and Security 
The digital transformation accelerates the pace of adoption of new services. ETX-1p is designed to 
simplify operations, while providing the service provider with visibility to its branch office demarcation. 
ETX-1p incorporates secure Zero-Touch-Provisioning mechanisms for agile and seamless OS deployment, 
reducing truck rolls and minimizing mass deployment operating costs. 
To automate setting up of overlay connectivity to the data center, ETX-1p can be integrated with the 
service provider’s SDN controllers or orchestration systems, using NETCONF/YANG modeling.  
ETX-1p can also be managed via WEB, CLI or by RADview.  
Management Capabilities 
• 
Secure remote management via any port using SSH, SNMP, NETCONF/YANG, or RADview, RAD’s 
SNMP-based management system 
• 
Zero Touch, allowing ETX-1p to receive software and configuration files automatically without 
having to manually log into ETX-1p. Supported over VPN and Public networks. 
• 
Performance Management – ETX-1p maintains performance management (PM) statistics. The 
PM statistics are collected into a file that can be read using RAD’s RV PM-portal for further 
analysis and presentation. 
• 
ETX-1p access control lists (ACLs) flexibly filter management traffic. Data ACLs with a single 
Permit rule are also supported for IPsec only, to set the traffic permitted through the IPsec 
tunnel and thus protected by IPsec. 
Console Port  
vCPE-OS can be installed on a white box with the following ports: 
• 
USB port for installation of vCPE-OS image from disk-on-key 
1. Introduction 
• 
Mini USB or serial (RS-232 or similar) port to which a console can be connected for management 
via CLI 
 
Note 
The mini USB port has neither configuration nor monitoring parameters.  
File Transfer Protocols 
vCPE-OS supports SCP, SFTP, FTP and FTPs client functionality.  
Security Protocols 
ETX-1p supports the security protocols listed below, ensuring client-server communication privacy and 
correct user authentication: 
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
ETX-1p supports Dynamic Host Configuration Protocol (DHCP) server functionality for IPv4 clients. Based 
on the Bootstrap Protocol (BOOTP), DHCP server assigns to DHCP clients IPv4 addresses from configured 
pools, as well as various configuration parameters (DHCP options), in response to the broadcast 
requests of DHCP clients. This functionality eliminates the need to assign an IP address for each 
potential client. 
ETX-1p supports DHCP and DHCPv6 client functionality working opposite IPv4 and IPv6 servers to get 
network IP addressing as well as other configuration parameters (DHCP options) that facilitate the 
device’s ZT functionality.  
Traffic Processing 
Layer-3 Forwarding 
ETX-1p provides Layer-3 forwarding, with multiple Virtual Routing and Forwarding instances (VRFs). Up 
to 10 routers and 32 router interfaces are supported.  
1. Introduction 
ETX-1p supports static routing definitions, Border Gateway Protocol (BGP) and OSPF. 
Network Address Translation (NAT)  
ETX-1p supports Network Address Translation (NAT), a method that maps IP addresses (IPv4 only) from 
one IP domain to another in an attempt to provide transparent routing to hosts. 
IPsec Tunneling 
ETX-1p supports IPsec on router interfaces to secure private communication across public IP networks.  
GRE Tunneling  
ETX-1p supports Generic Routing Encapsulation (GRE) protocol, which sets up Layer-3 point-to-point 
connectivity between two remote sites (over an underlay Layer-3 network). 
Layer-2 Forwarding  
ETX-1p supports up to two bridges and up to 32 bridge ports. The bridge ports can be bound to Ethernet 
ports. The bridge entity enables users to perform local switching. 
Layer-3 Quality of Service (QoS)  
ETX-1p supports Quality of Service (QoS), i.e. traffic management, on Ethernet and Cellular ports to 
ensure that traffic with specific characteristics, such as management, is guaranteed specific bandwidth 
with minimum delay. 
QoS support also includes classification – classifying traffic into traffic-classes on the ingress directions of 
a port. Traffic class defines actions such as fixed Class of Service (CoS) mapping on the ingress direction 
of an Ethernet port and DSCP marking.  
Monitoring and Diagnostics 
ETX-1p offers several types of diagnostic procedures: 
• 
Fault Propagation 
• 
Syslog – Syslog protocol generates and transports event notification messages from ETX-1p to 
servers across IP networks. 
• 
Ping Test – ETX-1p can ping a remote IP host to check ETX-1p IP connectivity with that host. 
• 
Trace Route – ETX-1p can quickly trace a route through the network from ETX-1p. 

## 1.2 New in this Version  *(p.49)*


## 1.3 Technical Specifications  *(p.49)*

1. Introduction 
Timing 
You can configure the ETX-1p internal real-time clock as free running or with Network Time Protocol 
(NTPv4). 
1.2 New in this Version  
 
New Features 
Comments 
Enclosure, Cards and Ports 
New Global 5G modem (Ready for PoC) 
 
 
 
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
 
 
 
1.3 Technical Specifications  
 
Note 
Asterisk (*) marking the feature means that the feature will be released in a 
future version. Some of these features are described in the manual and 
marked with the asterisk.  
1. Introduction 
 
Hardware Specifications  
Memory and Storage 
DRAM  
1 Gb, 2 Gb  
Flash Storage  8 Gb, 32 Gb  
Interfaces 
WAN 
1 GbE SFP and 1 GbE UTP (RJ-45) ports 
LAN 
4 GbE UTP (RJ-45)  
LTE 
LTE modem with dual SIM 
Wi-Fi 
802.11b/g/n/ac dual band 
GNSS 
GPS – American (default)  
Galileo – European 
Modems 
Dual SIM Cellular Modem LTE bands – see Integrated LTE Modems table below 
EVDO networks (technology backward compatible) 
Firmware Upgrade 
FOTA (Firmware upgrade Over the Air) 
LoRaWAN Module 
EU868, RU864, US915, AS923 (1-4), AU915, KR920, IN865 
bands 
SX1303 baseband processor  
8 x 8 channels LoRa packet detectors 
8 x SF5-SF12 LoRa demodulators, 
8 x SF5-SF10 LoRa demodulators 
LoRaWAN Class A, B, C 
1. Introduction 
Packet forwarder 
Tx power: up to 27 dBm  
Rx sensitivity: down to -139 dBm @ SF12, BW 125 kHz 
Configurable Cellular 
Authentication 
PAP, CHAP 
SIM Card 
Mini SIM, 25 mm x 15 mm (0.98 in x 0.59 in 
Form factor: 2FF 
WiFi Module  
IEEE 802.11ac/a/b/g/n 
Dual band 2.4 GHz or 5 GHz (software selectable) 
Up to 8 users 
 
Integrated LTE Modems 
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
L450A 
CAT 4 450MHz for private LTE networks 
LTE-FDD: B3/7/20/31/72  
1. Introduction 
L450B 
CAT 4 450MHz for private LTE networks 
LTE-FDD: B3/20/87 
L5 
CAT 4 Japan  
LTE FDD: B1, B3, B8, B18, B19, B26 
LTE TDD: B41 
WCDMA: B1, B6, B8, B19  
LTA 
CAT 4 North America, TAA-compliant 
LTE: B2, B4, B5, B12, B13, B14, B25, B26, B66, B71 
WCDMA: B2, B4, B5  
Antennas  
Depending on the ordering option, your package may include a number of antennas supplied along with 
the modems. For instructions on the antenna installation, refer to Installing Antennas. 
Cellular Antennas – Embedded  
 
 
Embedded LTE 
(L1, L3)  
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
1. Introduction 
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
1. Introduction 
Frequencies 
[Mhz] 
410-496 
617-960 
1427-2690 
3300-5000 
5150-5925 
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
Embedded LTE (L5) Antenna – Gain and VSWR 
Frequencies [Mhz] 
698-960 
1710-2170 
2500-2700 
Peak Gain [dBi] 
-1.6 
1.5 
2.9 
Avg. Gain [dB] 
-3.8 
-2.4 
-2.6 
VSWR 
1.6:1 
2.1:1 
2.3:1 
 
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
 
1. Introduction 
 
SF-ANT3G-2M(5M) 
SF-ANT4G-2M(5M) 
SF-ANT-LTE700-7DBI-MGNT 
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
Cable length 
2m/5m 
2m/5m 
3m  
*Antenna gain depend on size of the ground plane 
**VSWR stated when measured with 2.5m RG174 on 50x50cm ground-plane 
***Values stated when measured on 50x30cm ground plane 
1. Introduction 
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
Outdoor antenna for LoRaWAN options, 3 dBi 
Photo 
 
Electrical Specifications 
Frequency 
EU433, EU868, AU915, US915, AS923 
Impedance 
50 Ohms 
1. Introduction 
 
SF-ANT-LORA-3DBI-SMA 
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
IP/IK ratings 
IP-65 
Connection Specifications 
Connector type 
RP-SMA male straight connector 
Cable 
RG-178 coaxial cable 
Management and Diagnostics 
Control Port 
RS-232 interface, RJ-45 connector 
1. Introduction 
Note: Control port cable is not included and must be ordered separately  
LEDs 
Including alarm indication and cellular RSSI level 
Compliance 
Standards 
CE 
EMC Class A 
Environment 
Temperature  
Operating: -10 to 50°C (32 to 122°F) 
Storage: -40 to 65°C (-40 to 149°F) 
Humidity 
5% to 90%, non-condensing 
Physical 
Enclosure 
Plastic Box 
Height  
44 mm (1.73”)  
Width 
230 mm (9.05”)  
Depth 
175 mm (6.9”)  
Weight 
Net: 0.5 kg (1.1 lb)  
Max (including device + package + power supply + cable 
adaptor + 2 LTE antennas + 2 Wi-Fi antennas): 1.04 kg (2.3 lb)  
Power   
Power Supply 
External 90–240 VAC 
Power 
Consumption 
< 5W  
Idle: 3.0W** 
Typical: 3.6W** 
Maximum: 4.5W** 
**On a platform with one LTE modem 
1. Introduction 
 
Interfaces 
 
1. Introduction 
 
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
Cellular and GPS 
LTE 
Single SIM 
Dual SIM 
Dual LTE modems 
Operation Modes 
PPP, Eth/DHCP 
1. Introduction 
GPS 
Location reporting 
OAM 
SLA Monitoring  
ICMP echo, UDP echo  
ZTP 
On-net 
Off-net (over unsecured network) performs secure “call 
home” using Public Key Infrastructure (X.509) 
 