# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 1.1 Overview

*Manual `MiNID_ver_2_6_mn.pdf`, pages 39–45.*


## (chapter introduction)  *(p.39)*

1 Introduction 
1.1 Overview 
MiNID is a miniature programmable network interface device offering MEF 2.0 certified Carrier Ethernet 
demarcation functionalities. With very low delay, based on cut-through forwarding technology, MiNID 
offers Hierarchical Quality of Service (HQOS) and SLA verification functionalities as well as fault 
detection and fault isolation tools. 
MiNID can be ordered as a pluggable smart SFP or as an SFP sleeve, hosting standard SFPs. 
It can be easily installed at customer sites, mobile base stations, and wholesale interconnection sites in 
order to establish and monitor business services, mobile backhauling, and wholesale applications. It can 
be owned and operated by service providers, wholesale providers, and even end customers. Supporting 
seamless integration with standard SFPs and its “Zero Touch” provisioning capabilities, MiNID offers a 
real plug-and-play solution, reducing capital expenditure (Capex), operational expenditure (Opex), and 
total cost of ownership (TCO). 
MiNID with Demarcation software load includes comprehensive Ethernet OAM (Operation, 
Administration, and Maintenance) functionality and SLA monitoring.  MiNID SFP sleeve transfers 
Synchronous Ethernet transparently to ensure highly accurate traffic delivery in packet-based mobile 
backhaul networks.  
MiNID with Platinum software load contains all demarcation capabilities with extra monitoring features. 
MiNID can be configured to process customer and network traffic consistently for all incoming traffic 
(all-in-one bundling), or to classify and map traffic by VLAN ID, VLAN priority, DSCP, MAC source or 
destination address.  
MiNID SFP sleeve form factor is a patent protected design that can be inserted into a standard 
MSA-compliant SFP port (FE/GbE) on a customer device. On the carrier side, MiNID provides a single SFP 
port into which standard MSA-compliant SFPs can be inserted. 
MiNID can either be managed independently with its own IP address or use a loaned IP mechanism that 
does not require IP address and uses a dedicated UDP port for management. 
MiNID can be managed through the following interfaces: 

## Product Options  *(p.40)*

1. Introduction 
• 
Web-based, menu-driven interface 
• 
Telnet/SSH with CLI, enabling configuration duplication in multiple units  
• 
SNMP 
• 
RADview-EMS network management system support, including PM collection of flow utilization 
counters 
Product Options 
Two versions of MiNID are available: 
• 
FE (100 Mbps) – fits into FE SFP ports and support 100BASE-FX SFPs 
• 
GbE (1 Gbps) - fits into FE or GE ports and supports 100BASE-FX as well as 1000BASE-FX SFPs 
MiNID is available as: 
1. SFP sleeve form with the following options: 
 
FE (100 Mbps) 
 
GbE (1 Gbps) 
2. SFP with the following options: 
 
850 nm multimode 
 
1310 nm single mode 
3. MiNID can be ordered with Sync-E capability enabled 
In all MiNID ordering options, port rates on both ports must be the same (FE or GE). When 
autonegotiation is enabled, MiNID automatically negotiates through its two ports to achieve the same 
rate on both ports.  
Nonetheless, when the Force Speed option is set to 1000 Mbps in SFP sleeve, the rates on two ports can 
be different. In such cases, shapers should be used to compensate for the rates difference. For more 
information on the Force Speed option, refer to Configuring Port Parameters. 

## Application  *(p.41)*


## Features  *(p.41)*

1. Introduction 
Application 
MiNID SFP sleeve eliminates the need for standalone demarcation devices, while allowing service 
providers, mobile operators, and wholesale carriers to receive real-time network/service performance 
reports with per-CoS SLA definition. 
Ethernet OAM and Service Turn-Up
Packet
Switched
Network
Aggregator/
PE
Router
Switch
eNodeB/
Small Cell
SFP-based
NID/NTU
MiNID
MiNID
MiNID
MiNID
 
MiNID SFP Sleeve as a Demarcation Device 
Features 
MiNID includes the following features: 
Ethernet 
Service Demarcation 
MiNID can work in port or flow-based mode. In port-based mode (all-in-one bundling),  MiNID processes 
customer and network traffic data frames consistently for all traffic coming into its single port in each 
direction. In flow-based mode,  MiNID can classify and map frames by any of the following: 
• 
Customer VLAN ID range and P-bit range 
• 
DSCP 
• 
MAC source or destination address 
• 
Ethertype 
1. Introduction 
In flow-based mode, up to 64 unidirectional flows can be configured (no more than 32 flows per 
direction). You can configure a service name for flows and MAs, to enable network management 
systems to locate entities related to specific services. For each configured flow, and for default, 
non-matched (unclassified) traffic, any of the following actions can be defined: 
• 
Drop – Drop the frame 
• 
VLAN – Push (add) for single and double VLANs, pop (remove) for single and double VLANs, or 
replace a C-tag (Customer VLAN tag) or S-tag (Service VLAN tag), as specified. 
• 
Loopback – The traffic is echoed back through the same port, with or without swapping the 
source and destination addresses (MAC, and where relevant also IP), as specified. 
• 
Pass through – Pass the traffic through the device without applying any changes. 
Priority Mapping 
When a flow is configured to push or replace a VLAN, the frame priority is set in the new VLAN priority 
bits (p-bits). The value of the p-bits can be configured to be set in any of the following ways, per flow: 
• 
Fixed value for the flow 
• 
Copied from the originating frame C-tag p-bit 
• 
According to a configured mapping of the originating frame C-tag p-bit value to p-bit values. All 
flows configured for C-tag p-bit to S-tag p-bit mapping (not copying) use the same mapping 
method 
• 
According to a configured mapping of DSCP values to p-bit values. All flows configured for 
DSCP-p-bit mapping use the same mapping method. 
L2CP Handling with L2PT 
MiNID  can handle Layer-2 control protocol traffic (L2CP) with Layer-2 protocol tunneling (L2PT), on a 
per-port and/or per-flow basis. L2CP classification is based on destination MAC Address, and L2PT 
classification is based on destination MAC address and Ethertype.  MiNID can pass through, tunnel, 
discard, or peer (trap to host for protocol processing) L2CP/L2PT packets.  
Monitoring and Diagnostics 
OAM 
MiNID uses its hardware-based processing capabilities to quickly perform OAM and PM measurements 
with maximum precision. This makes  MiNID an effective tool for network failure detection, 
1. Introduction 
troubleshooting, and measuring SLA parameters such as Frame Delay, Frame Delay Variance (jitter), 
Frame Loss and Availability. 
MiNID supports the following OAM standards with MEP/MIP support, for up to 32 MEPs: 
• 
CFM OAM (end-to-end OAM) as per IEEE 802.1ag (draft 8), per-EVC: Continuity check, 
non-intrusive loopback, and link trace. Maximal rate is 10 frames per second. Maintenance 
associations can process frames with one or two VLAN tags (user-configurable). MEP per 
EVC.COS that enables the user to configure MEPs (each one with a unique VLAN + P-Bit) under 
same MA. In addition, incoming packets are filtered according to the P-Bit configured. 
• 
ETH OAM as per ITU-T Y.1731 (PM), with AIS and RDI support, per EVC: Loss measurement 
(LMM/LMR, SLM/SLR), delay measurement (DMM/DMR; with hardware-based time stamping), 
delay variance measurement (hardware timestamping), and availability. 
• 
EFM OAM (link OAM) as per IEEE 802.3-2005 (formerly IEEE 802.3ah) in active or passive mode, 
for remote management and fault indication, including remote loopback, and dying gasp. 
 
Note 
Link OAM is operational only if the L2CP/L2PT action for OAM protocol is set 
to peer. 
Loopback Tests 
MiNID supports the following types of loopbacks: 
• 
Intrusive flow loopback (the whole flow is echoed), with or without MAC and IP address swap 
• 
In-service layer-2 loopbacks according to MAC address (source and/or destination), with or 
without MAC and IP address swap 
• 
In-service layer-3 loopbacks according to destination IP address with MAC and IP address swap 
• 
In-service layer-4 loopbacks according to destination IP address and destination UDP port with 
MAC and IP address swap 
• 
UDP echo responder 
• 
RFC-2544 responder 
• 
IP-agnostic loops 
1. Introduction 
Resiliency 
Fault Propagation 
MiNID SFP sleeve provides provider-to-customer fault propagation, in order to enable deactivating 
affected interfaces when required. You can also configure the direction (MSA to SFP, or SFP to MSA) in 
which to propagate OAM CFM faults (LOC, Rx AIS). 
Dying Gasp 
Upon power failure, MiNID finishes transmitting the currently-handled frame, and then sends the 
following: 
• 
10 Dying Gasp frames as defined in 802.3ah 
• 
10 Dying Gasp SNMPv2 traps to up to two configured SNMP servers. 
The dying gasp process stops when power is restored. 
DDM (Digital Diagnostic Monitoring) 
When equipped with an SFP transceiver that support DDM, the MiNID stores DDM statistics, enabling 
the following: 
• 
Forwarding the parameters to the host device 
• 
Reading the parameters from remote management systems without accessing the MiNID host 
device. 
Management 
MiNID can be managed using dedicated IP address or in a Loaned IP mode where an IP address is not 
required. In case of dedicated IP, the IP address can either be static or obtained from a DHCP server. 
In loaned IP mode, MiNID uses the IP address of the host device. In this mode, network management 
systems can communicate with MiNID by sending management packets to the host IP address with a 
pre-configured UDP port. MiNID responds to the packets or forwards them to the host device, 
depending on the packet TCP/UDP port number and the access configuration in MiNID. 
 
Note 
When MiNID  is working in loaned IP mode and is managed via RADview, then 
in order for automatic discovery to operate properly, there must be no more 
than one active IP address behind MiNID. Otherwise, MiNID responds to every 
active IP address behind it, causing incorrect device duplication. 
1. Introduction 
MiNID provides the following management functionality: 
• 
CLI-based management via Telnet / secure Telnet (SSH) 
• 
Menu-based management via Web interface (HTTP) 
• 
SNMP 
• 
Management interfaces for third-party NMS: 
 
Configuration via CLI 
 
Alarms via SNMPv1/SNMPv2 
 
PM collection by retrieving PM file via SFTP/TFTP 
• 
Integration into RADview-EMS for configuration and alarms, as well as support for RADview PM 
portal  
• 
Zero touch configuration – DHCP-based acquisition of IP address and configuration file 
 
Note 
Configuration via SNMP does not cover all MiNID functionalities. 
Four simultaneous Telnet or Web connections can be maintained at any given time. 
Access Control List (ACL) 
Access control lists are used to flexibly filter by IP address and mark incoming and outgoing network 
traffic. 
The service providers use the ACL to maintain the network security by preventing the malicious traffic 
from entering the device. The ACL can be used to save the network resources by dropping the unwanted 
packets. Ten rules can be configured for ACL. 
Timing and Synchronization 
Transparent Sync-E  
MiNID  supports Synchronous Ethernet (Sync-E) transparently, transferring the received clock and any 
ESSM messages from the MSA/Port 2 to the SFP/Port 1 port or from the SFP/Port 1 to the MSA/Port 2 
port (user-configurable). This feature is supported by SFP sleeve.  
 