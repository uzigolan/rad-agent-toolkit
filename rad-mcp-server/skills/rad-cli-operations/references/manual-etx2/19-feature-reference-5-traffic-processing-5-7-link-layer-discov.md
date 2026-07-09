# Feature Reference – 5 Traffic Processing – 5.7 Link Layer Discovery Protocol (LLDP)

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 984–991.*


## Applicability and Scaling  *(p.984)*


## Standards Compliance  *(p.984)*


## Functional Description  *(p.984)*

ETX-2i Devices 
5. Traffic Processing 
MIRP                  0              0 
DLDP                  0              0 
HGMP                  0              0 
PTP                   0              0 
ESMC                  0              0 
5.7 Link Layer Discovery Protocol (LLDP) 
LLDP is a standard layer-2 protocol that allows Ethernet network devices to advertise information about 
themselves and receive information from other Ethernet network devices. The devices store this 
information in local MIB databases accessible via SNMP; therefore, the network management system 
can access this information. 
Automated discovery of devices simplifies management and network maintenance and reduces general 
setup costs of new equipment.  
Applicability and Scaling 
This feature is applicable to all ETX-2i products. 
Standards Compliance 
IEEE 802.1AB-2009 
IEEE 802.3az-2010 
Functional Description 
LLDP is a neighbor discovery protocol that enables network devices to advertise information to peer 
devices on the same physical LAN and store information about the network. LLDP is supported for all 
Ethernet ports, including the management port and Ethernet ports that are bound to LAG. LLDP 
information is exchanged by means of LLDP packets. 
 
Note 
LLDP runs on physical links and is configured on each individual physical port; 
it neither runs nor is configured over the LAG logical layer. 
 
 
ETX-2i Devices 
5. Traffic Processing 
LLDP Bridge TypeLLDP works according to the following bridge type: 
Nearest bridge 
The propagation of LLDP packets is limited to a single physical link 
and is stopped by any type of bridge.   
LLDP Packets 
LLDP packets are sent periodically between ETX-2i and neighboring devices, in order to obtain neighbor 
information. The information from the LLDP packets is stored for a period of time, determined by the 
time-to-live (TTL) value in the received packet. When the TTL expires, the LLDP information is discarded.  
LLDP packets contain the following information: 
Destination MAC 
address 
Set to 01-80-C2-00-00-0E (nearest bridge) 
Source MAC address 
Set to port MAC address 
EtherType 
Set to 0x88CC 
LLDP Protocol Data 
Unit (LLDPDU) 
Contains a variable number of information units called TLVs: 
mandatory TLVs, optional TLVs, and an EndOfLLDPDU TLV. LLDPDUs 
are always sent untagged. TLVs consist of basic management TLVs 
and organizationally specific TLVs. The organizationally specific TLVs 
are differentiated by IEEE 802.1, IEEE 802.3, and more. 
Basic Management TLVs 
TLV Name 
Description 
TLV Appears in LLDPDU 
Chassis ID 
Management MAC address 
Mandatory 
Port ID 
Interface name per RFC 2863 
Mandatory 
Time To Live 
Time in seconds that specifies the validity period of 
the information   
Mandatory 
Port Description  
ifDescr per RFC 2863, which is port name 
Optional 
System Name 
Device name as configured by CLI 
(per RFC 3418) 
Optional 
System Description 
sysDescr per RFC 3418 includes: 
• Device name 
• HW version 
• SW version 
Optional 
ETX-2i Devices 
5. Traffic Processing 
TLV Name 
Description 
TLV Appears in LLDPDU 
System Capabilities 
Includes indications for the following: 
• MAC bridge 
• Router 
• C-VLAN component of VLAN bridge 
• S-VLAN component of VLAN bridge 
• Two-port MAC relay (TPMR) 
Optional 
Management Address 
Management IP address (IPv4 or IPv6) 
• If there is more than one active management 
address, the lowest IP address at the lowest 
router interface is advertised. 
• If there is no management address, the default 
management address (169.254.1.1) is 
advertised. Any additional active IP address 
takes precedence over the default management 
IP address. 
• Updated LLDP advertisement is triggered by one 
of the following: 
• 
New IP interface defined. 
• 
Shutting down or deleting an IP interface 
• 
Rebooting the device 
LLDP advertisement changes take effect with the 
next advertisement following the trigger. 
Optional 
End Of LLDPDU 
N/A; indicates end of LLDPDU 
Mandatory 
Organization-Specific IEEE 802.1 TLVs 
TLV Name 
Description 
Protocol Identity 
Protocols configured on the port. The following protocols are supported: 
• LLDP  
• EFM if configured  
• CFM  
• LAG-LACP if the port is in a LAG group 
• ESMC if tx-ssm is enabled for the port) 
• ERP-v2 if G.8032 ring is configured on the port (not supported by ETX-2i-
100G) 

## Factory Defaults  *(p.987)*


## Configuring LLDP  *(p.987)*

ETX-2i Devices 
5. Traffic Processing 
Organization-Specific IEEE 802.3 TLVs 
TLV Name 
Description 
MAC/PHY Configuration/Status 
• Auto-negotiation support/status 
• Auto-negotiation advertised capability 
• MAU type (data rate and duplex mode) 
Maximum Frame Size 
Egress MTU 
Factory Defaults 
By default, no LLDP parameters are configured for ports. The system LLDP parameters have the default 
values shown in the following table. 
Parameter 
Default  
Remarks 
bridge-type 
nearest-bridge 
 
hold-multiplier 
4 
 
hold-time 
4 
 
shutdown 
shutdown 
LLDP is administratively enabled for all 
relevant interfaces. 
tx-interval 
30 
Value is in seconds. 
Configuring LLDP 
LLDP parameters are configured at the following levels: 
• 
Global – LLDP parameters that apply to the entire device are configured at the system level. 
• 
Port – LLDP parameters are configured at the Ethernet port level, to specify which TLVs to send 
for the port. 
Note 
In order for LLDP to function properly for the port, an L2CP profile must be 
associated with it that specifies peer action for MAC address 
01-80-C2-00-00-0E (nearest bridge). 
ETX-2i Devices 
5. Traffic Processing 
Setting System Parameters 
This section explains how to configure global parameters such as bridge type, as well as enable or 
disable LLDP for the device. 
 To configure LLDP system parameters: 
1. Navigate to configure system lldp. 
The config>system>lldp# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Setting device bridge type 
bridge-type nearest-bridge 
Currently the only available 
bridge type (default). 
Defining the port description 
port-description [ifAlias | ifDescr] 
Default: ifDescr 
You may set and use the port 
alias as port description. 
Specifying how long device 
should hold received LLDP 
packets before discarding them 
hold-multiplier 
(hold-time × hold-multiplier) + 
1 determines the time-to-live 
(TTL) value carried in LLDP 
frames transmitted by the 
LLDP agent. 
Possible values: 1-100 
hold-time 
Specifying the amount of time 
between LLDP transmissions 
tx-interval <seconds> 
 
Enabling or disabling LLDP for 
device 
shutdown 
Enter no shutdown to enable 
LLDP. 
Setting Port Parameters 
This section explains how to configure which TLVs to transmit for the port for LLDP bridge type: nearest 
bridge (see tables above for details on TLVs). 
 To configure LLDP parameters for Ethernet port: 
1. Navigate to configure port ethernet [<slot>/]<port> lldp. 
The prompt config>port>eth([<slot>/]<port>)>lldp# is displayed. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Enabling or disabling 
transmission of the specified 
protocol in the IEEE 802.1 
protocol identity TLV  
802.1-protocol-identity { lldp | efm 
| cfm | lag-lacp | rstp-mstp | esmc 
|erp-v2 } 
ETX-2i-100G does not support 
erp-v2. 
Enabling or disabling 
transmission of IEEE 802.3 
TLVs in customer bridge mode  
customer-bridge-802.3 
[mac-phy-configuration] 
[power-via-mdi] [max-frame-size] 
• mac-phy-configuration – 
MAC/PHY 
Configuration/Status TLV 
• power-via-mdi  – not 
supported 
• max-frame-size  – 
maximum Frame Size TLV 
Enabling or disabling 
transmission of basic 
management TLVs in customer 
bridge mode 
customer-bridge-basic-manageme
nt [port-description] [sys-name] 
[sys-description] [sys-capabilities] 
[management-address] 
• port-description  – port 
description TLV 
• sys-name  – system name 
TLV 
• sys-description – system 
description TLV 
• sys-capabilities – system 
capabilities TLV 
• management-address  –
management address TLV 
(IPv4 or IPv6) 
Enabling or disabling 
transmission of IEEE 802.3 
TLVs in nearest bridge mode  
nearest-bridge-802.3 
[mac-phy-configuration] 
[power-via-mdi] [max-frame-size] 
• mac-phy-configuration – 
MAC/PHY 
Configuration/Status TLV 
• power-via-mdi 
• max-frame-size – 
maximum Frame Size TLV 
Enabling or disabling 
transmission of basic 
management TLVs in nearest 
bridge mode 
nearest-bridge-basic-management 
[port-description] [sys-name] 
[sys-description] [sys-capabilities] 
[management-address] 
• port-description – port 
description TLV 
• sys-name – system name 
TLV 
• sys-description – system 
description TLV 
• sys-capabilities – system 
capabilities TLV 
• management-address – 
management address TLV 
(IPv4 or IPv6) 

## Example  *(p.990)*

ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Specifying transmission mode 
in nearest bridge mode 
nearest-bridge-mode { tx | rx | 
tx-rx } 
• tx – Transmit LLDP packets 
• rx – Receive LLDP packets 
• tx-rx: Transmit and 
Receive LLDP packets 
Viewing detailed information 
about neighboring devices 
show neighbors-details 
  
Viewing brief summary of 
neighboring devices 
show neighbors-summary 
 
Viewing LLDP statistics 
show statistics 
 
Clearing LLDP statistics 
clear-statistics 
 
Example  
The following example illustrates how to configure LLDP in the system. 
#*********************************Configuring_LLDP in system***************** 
conf system lldp 
 
tx-interval 10 
 
hold-time 2 
 
bridge-type nearest-bridge  
 
no shutdown 
 
exit all 
#***************************Configuring_L2CP_Profile*********** 
configure port 
 
l2cp-profile lldp  
 
mac 0x0e peer  
 
exit all 
 
configure port eth 1 
 
 l2cp profile lldp 
 
 no shutdown 
 
exit all 
#*****************************Configuring_LLDP in port********* 
configure port ethernet 1 lldp 
 
 
nearest-bridge-mode tx-rx  
 
 
nearest-bridge-basic-management sys-description  
 
 
nearest-bridge-basic-management sys-name 
 
 
nearest-bridge-basic-management sys-capabilities  
 
 
nearest-bridge-basic-management management-address 
 
 
nearest-bridge-basic-management port-description 
 
    nearest-bridge-802.3 mac-phy-configuration max-frame-size 
 

## Viewing LLDP Neighbor Information  *(p.991)*

ETX-2i Devices 
5. Traffic Processing 
Viewing LLDP Neighbor Information 
You can display detailed information about neighboring devices or display a brief summary of 
neighboring devices. 
 To display detailed information about neighboring devices: 
1. Navigate to configure port ethernet [<slot>/]<port> lldp. 
The prompt config>port>eth([<slot>/]<port>)>lldp# is displayed. 
2. Enter show neighbors-details. 
For example: 
ETX-2i# configure port ethernet 1 lldp 
ETX-2i>config>port>eth(1)>lldp# show neighbors-details 
Name : RAD-ETX-2i 
 
 ID  : 00 01 00 00 00 03  02 
 
 
Basic-Management Info 
Bridge-Type 
 
 
: 
NEAREST 
Chassis-type  
 
: 
MAC_ADDRESS 
Chassis-id 
 
 
: 
00:01:00:00:00:03 
Port-Type 
 
 
: 
Locally Assigned 
Port-id 
 
 
: 
eth-0/1 
Port-Descr 
 
 
: 
Ethernet Port 
System-name 
 
 
: 
RAD-ETX-2i 
System-Descr  
 
: 
RAD SWITCH 
System Capabilities   
 
: 
REPEATER, MAC_BRIDGE 
Enabled Capabilities  
 
: 
REPEATER, MAC_BRIDGE 
Remote Management Address  
 
Type 
 
 
: 
IPV4 
 
Address 
 
 
: 
192.168.200.10 
 
802.1 
Port-vlanId 
 
 
: 
10 
Port-protocol Vlan-id 
  
 
: 
-- 
Vlan Name 
 
 
: 
--  
Protocol Identity 
 
 
: 
Link-aggregation, OAM, ELMI 
VID Usage 
 
 
: 
-- 
Management VID 
 
 
: 
-- 
Link-Aggregation 
Link Aggregation Status 
 
: 
Enabled 
Lag-portId 
 
 
: 
100 
 
802.3 
MAC/PHY configuration 
Auto Negotiation Support Status 
: 
Supported 
Auto Negotiation Current Status 
: 
Enabled 
Auto-negotiation-advertised Capability 
: 
-- 
Operational MAU Type  
 
: 
-- 