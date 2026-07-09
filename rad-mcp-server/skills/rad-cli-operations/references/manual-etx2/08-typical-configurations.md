# Typical Configurations

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 341–496.*


## (chapter introduction)  *(p.341)*

ETX-2i Devices 
Carrier Ethernet Demarcation 
Version 6.8.5 
Typical Configurations 
Updated: 08/24 
Content 
Key Concepts ................................................................................................................................. 2 
1.1 Flows ................................................................................................................................................. 2 
1.2 Timing ............................................................................................................................................... 2 
2 
Quick Start ..................................................................................................................................... 3 
2.1 Installing the Unit ............................................................................................................................. 3 
2.2 Resource Allocation Considerations ................................................................................................. 4 
2.3 Configuring the Unit for Management ............................................................................................. 5 
2.4 Saving Management Configuration .................................................................................................. 7 
2.5 Configuring Services ......................................................................................................................... 8 
2.6 Verifying Connectivity ...................................................................................................................... 8 
3 
Applications ................................................................................................................................... 9 
3.1 E-Line Application ............................................................................................................................. 9 
3.2 Timing Synchronization for Mobile Networks ................................................................................ 16 
3.3 Carrier-Class Ethernet Application ................................................................................................. 44 
3.4 ETX-2i-100G 100G Single Fiber Adaptor ....................................................................................... 137 

## 1 Key Concepts  *(p.344)*

ETX-2i 
1. Key Concepts 
1 Key Concepts 
Key concepts describe the ‘brains of the device’ or the principles based on which the ETX devices 
operate. The two key concepts on which ETX-2i devices are running are the principle of flows over which 
the applications run and the timing (clocking) options. 
1.1 Flows 
According to RFC 2722 and RFC 3697, a flow is a traffic path on which traffic will flow that is defined 
between a physical or logical port on a source device and a physical or logical port on a destination 
device. This traffic path is uni-directional. To establish bi-directional communication between the two 
ports, two identical flows must be created with the source and destination ports switched around.  
The source port is referred to as Ingress Port while the destination port is referred to as Egress Port. 
Together with the ‘basic traffic path’, you define filtering, prioritizing, policing and smoothing (shaping) 
efforts as explained in the Feature Reference. 
 
Ingress Port
Classifier
Policer
Marking
CoS Mapping
Queue block 
Level 0
Editing
Shaper
Queue Block 
Level 1
Egress port
 
1.2 Timing 
The various clocking options are explained in the Feature Reference section of this user manual. 

## 2 Quick Start  *(p.345)*

ETX-2i 
2. Quick Start 
2 Quick Start 
This section describes the minimum configuration needed to prepare ETX-2i for operation. 
2.1 Installing the Unit 
Perform the following steps to install the unit: 
1. Determine the required configuration of ETX-2i according to your application. 
2. Connect the ASCII terminal to the CONTROL port. 
3. Connect power to the unit. 
Connecting to Terminal 
 To connect the unit to a terminal: 
1. Connect the male Mini USB / Micro USB connector of the CBL-MUSB-DB9F/CBL-UUSB-DB9F 
terminal cable to the unit’s 5-pin female connector, designated CONTROL.  
2. Connect the other end of the CBL-MUSB-DB9F/CBL-UUSB-DB9F terminal cable to the ASCII 
terminal equipment. 
Connecting to Power 
Regular units are available with single or dual AC or DC power supply, depending on the ordering option. 
There is also a dual DC inlet option for the 8.5-inch enclosure; the dual DC inlet is a single DC power 
supply, with two DC inlets for redundancy at the DC source level. The ETX-2i-B branch-office device is 
offered with a wide-range power supply; ETX-2i-10G-B with integrated dual AC and DC power supplies.  
For indoor installations, a standard AC external power cable is supplied to provide AC power to the unit.  
For connection to unprotected AC power networks, devices that do not have built-in AC surge 
protection are provided with an enhanced CBL-K21 AC external power cable per ITU-T K.21E. 
ETX-2i 
2. Quick Start 
AC/DC plugs or terminal block connectors are available for DC power supplies. 
 
Warning 
Before connecting or disconnecting any cable, the protective ground 
terminals of this unit must be connected to the protective ground conductor 
of the mains (AC or DC) power cord. If you are using an extension cord 
(power cable) make sure it is grounded as well. 
Any interruption of the protective (grounding) conductor (inside or outside 
the instrument) or disconnecting of the protective ground terminal can 
make this unit dangerous. Intentional interruption is prohibited. 
 
 To connect to AC power: 
1. Connect the relevant AC power cable to the power connector on ETX-2i. 
2. Connect the power cable to the mains outlet. 
The unit turns on automatically once connected to the mains. 
All DC options support NEBS level 3 on port type 8b (DC inlet). *** Check this 
 To connect to DC power: 
1. Wire the DC connection to the power cable (if required) and connect the assembled DC power 
supply to the unit. 
2. Connect the power cable to the mains outlet. 
The unit turns on automatically once connected to the mains. 
Refer to the relevant DC Power Supply Connection section in the Installation and Setup chapter for 
instructions on wiring the DC connection. 
2.2 Resource Allocation Considerations 
Applicability and Scaling 
This feature is applicable to ETX-2i-100G/4QSFP. 
ETX-2i 
2. Quick Start 
Functional Description 
In terms of resource allocation, ETX-2i-100G/4QSFP ports are divided into two main groups, as follows: 
• 
Group 1: 100G ports 3/1 and 3/2 
• 
Group 2: All other ports (100G ports 3/3 and 3/4 and 10G ports 1/1 to 1/8 and 2/1 to 2/8)  
Resource allocation and functional design are reflected as follows: 
• 
In terms of bandwidth, each group can ingress or Egress half of the declared total Ingress or 
Egress. For a classic aggregation/NID application, it is recommended to place all UNI ports in 
Group 2 and all NNI ports in Group 1. In case of MASH topology, the network design takes into 
consideration the total expected ingress and egress traffic of each group. 
• 
When defining LAG protection, the two protected ports/paths should be from the same group. 
100G LAG protection mode can be set between the ports in Group 1 and 10G LAG protection 
mode between ports in Group 2. 
• 
Ingress/egress traffic can pass between ports within the same group or between the two 
groups. Ingress/egress traffic on a specific port is logged under the group to which the port 
belongs. For ETX-2i-100G/4QSFP, traffic on ports 3/1 and 3/2 is logged under Group 1, and 
traffic on any other port is logged under Group 2. 
• 
Maximum 1860 flows per device; 930 per group 
2.3 Configuring the Unit for Management 
Configure ETX-2i for management, using a local ASCII-based terminal. 
Starting a Terminal Session for the First Time 
 To start the terminal session: 
1. Make sure all ETX-2i cables and connectors are properly connected. 
2. Connect ETX-2i to a PC equipped with an ASCII terminal emulation application. Refer to the 
Installation and Setup chapter for details on connecting to the control port. 
3. Start the PC terminal emulation program and create a new terminal connection. 
ETX-2i 
2. Quick Start 
4. Configure the PC communication port parameters to a baud rate of 9.6 kbps, 8 bits/character, 1 
stop bit, no parity, and no flow control. 
5. Power-up the unit.  
The boot manager of ETX-2i starts and displays a message that you can stop the auto-boot and 
enter the boot manager by pressing any key. A running countdown of the number of seconds 
remaining until auto-boot is displayed. If it reaches 0 before you press a key, then after a few 
seconds a message is displayed showing that the active software pack is being loaded. 
After a few more seconds, the login prompt is displayed. 
6. Log in with your username (default: su for full configuration and monitoring access) and 
password (default: 1234). 
The device prompt appears:  
ETX-2i# 
7. Type the necessary CLI commands. 
8. Continue with product configuration. 
Configuring Management Flows 
To manage ETX-2i from a remote NMS, you must first preconfigure the basic parameters using a 
supervision terminal connected to the ETX-2i CONTROL port. You can manage ETX-2i by setting up 
management flows between the out-of-band Ethernet management port and an SVI bound to a router 
interface. 
 To configure ETX-2i for management access: 
1. Add an SVI port. 
2. Create classifier profiles for matching all traffic and matching untagged traffic. 
3. Add two flows (incoming and outgoing) connecting the out-of-band Ethernet management port 
and the SVI. 
4. Add a router interface, bind it to the SVI, and add a static route to the next hop. 
The following script provides the necessary configuration steps. Replace IP addresses and entity names 
with values suitable for your network environment. 
#*******************************Adding_SVI*********************************** 
config port  
  svi 1  
    no shutdown 
exit all 
ETX-2i 
2. Quick Start 
#***************************Adding Classifier_Profiles***********************  
config flows 
  classifier-profile all match-any match all 
  classifier-profile untagged match-any match untagged 
 
#***************************Configuring_Flows******************************** 
  flow mng_in 
    classifier untagged 
    no policer 
    ingress-port ethernet 101 
    egress-port svi 1 
    no shutdown 
  exit  
 
  flow mng_out 
    classifier all 
    ingress-port svi 1 
    egress-port ethernet 101 queue 0 block 0/1 
    no shutdown 
exit all 
 
#*********************Configuring_Router_Interface*************************** 
configure router 1 
  interface 1 
    bind svi 1 
    address 172.18.141.39/24 
    no shutdown 
  exit 
  static-route 172.17.0.0/16 address 172.18.141.1 
exit all 
save 
2.4 Saving Management Configuration 
Saving Configuration 
Enter save in any level to save your configuration in startup-config.  
Copying User Configuration to Default Configuration 
In addition to saving your configuration in startup-config, you may also wish to save your configuration 
as a user default configuration. 
ETX-2i 
2. Quick Start 
 To save user default configuration: 
• 
Enter the following commands: 
exit all  
file copy startup-config user-default-config 
2.5 Configuring Services 
Proceed with service configuration (refer to the Services chapter for details of different scenarios for 
provisioning supported services). 
This chapter shows the data flow and configuration steps for services.  
The diagrams and tables in Sections 4.2 to 4.6 illustrate typical ETX-2i services. 
Services can be discovered using the RADview service discovery function (refer to Preconfiguration for 
Service Discovery). 
2.6 Verifying Connectivity 
At the ASCII terminal, ping the IP address assigned to the management router interface and verify that 
replies are received. If there is no reply to the ping, check your configuration and make the necessary 
corrections. 

## 3 Applications  *(p.351)*

ETX-2i 
3. Applications 
3 Applications 
The configuration activities presented in this chapter assume that ETX-2i is configured using a standard 
ASCII terminal, and that you are familiar with ETX-2i management as described in the Management and 
Security chapter.  
3.1 E-Line Application 
This section provides configuration guidelines for setting up a typical E-Line service. 
The figure below illustrates the E-Line application layout. The table below details a summary of port 
connections. 
 
Ethernet Private Line (EPL) is implemented using a point-to-point EVC. All service frames at the UNI are 
mapped to a single EVC. 
The data traffic flow in the application behaves as follows (from left to right): 
1. PC transmits untagged packets, traffic enters ETX­2i (1) User port #3. 
2. ETX­2i (1) adds VLAN ID 10 towards the network. 
3. ETX-5 accepts only traffic with VLAN 10 in port 1/10 and forwards the packets to port 1/20 in 
the same I/O card. 
4. ETX­2i (2) accepts only traffic tagged with VLAN 10, removes the VLAN, and forwards the 
untagged packets to PC. 
ETX-2i 
3. Applications 
Connection Summary 
From Device/Port 
To Device/Port 
ETX­2i (1), port 3 
PC network interface #2 
ETX­2i (1), port 1 
ETX-5, port 1/10 
ETX-5, port 1/20 
ETX­2i (2), port 1 
ETX­2i (2), port 3 
PC network interface #3 
Equipment List 
The following table lists the devices required for the application. 
Device 
Quantity 
ETX­2i (1) 
1 
ETX­2i (2) 
1 
ETX-5 
1 
PC with application such as Ostinato that can simulate traffic, and three network cards for 
following: 
• Management (one network card) 
• Connect to simulate traffic (two network cards)  
1 
Installing the Units 
Before starting configuration, install the units as follows: 
1. Configure PC network interface #1 with static IP address 172.17.192.10. 
2. Connect PC network interface #2 to ETX­2i (1) port 3. 
3. Connect ETX­2i (1) port 1 to ETX-5 port 1/10. 
4. Connect ETX-5 port 1/20 to ETX­2i (2) port 1. 
5. Connect ETX­2i (2) port 3 to PC network interface #3. 
ETX-2i 
3. Applications 
Configuring the E-Line Service 
This section describes how to configure the E-Line service.  
Configuring E-Line for ETX­2i (1) 
You need to create the following: 
• 
Outgoing data traffic from user to network:  
 
Classifier profile that accepts traffic untagged (data traffic entering ETX­2i (1) from user port 
#3) 
 
Flow named 3t1 from user port #3 to network port #1, using the above profile, and adding 
VLAN 10 (with P-bit 0) 
• 
Incoming data traffic from network to user: 
 
Classifier profile that accepts only traffic tagged with VLAN ID 10 (data traffic entering ETX­2i 
(1) from the network) 
 
Flow named 1t3 from network port #1 to user port #3, using the above profile, and 
removing the SP-VLAN 
exit all 
#*********** Create classifier profiles 
configure flows  
  classifier-profile untagged match-any 
    match untagged 
  exit 
 
  classifier-profile v10 match-any 
    match vlan 10 
  exit 
 
#*********** Create flows 
  flow 3t1 
    classifier untagged 
    ingress-port ethernet 0/3 
    egress-port ethernet 0/1 queue 0 block 0/1 
    vlan-tag push vlan 10 p-bit fixed 0 
    no shutdown 
  exit  
 
 
ETX-2i 
3. Applications 
  flow 1t3 
    classifier v10 
    ingress-port ethernet 0/1 
    egress-port ethernet 0/3 queue 0 block 0/1 
    vlan-tag pop vlan  
    no shutdown 
  exit all 
save 
Configuring E-Line for ETX­2i (2) 
As the ETX­2i units have the same configuration in this application, either repeat the same commands 
listed in Configuring E-Line for ETX­2i (1), or copy the commands to a script, transfer it to ETX­2i (2), and 
run it. 
Configuring E-Line for ETX-5  
 You need to create the following: 
• 
Queue group profile assigned to ports 1/10 and 1/20, and the ports enabled 
• 
SAG (service aggregation group) queue group profiles 
• 
Data traffic from port 1/10 to port 1/20:  
 
Flow from port 1/10 to SAP 
 
Flow from SAP to port 1/20 
• 
Data traffic from port 1/20 to port 1/10: 
 
Flow from port 1/20 to SAP 
 
Flow from SAP to port 1/10 
exit all 
#*********** Configure Ethernet port queue groups 
config port  
  ethernet 1/10  
    queue-group profile q_group_2_level_default 
    no shutdown 
  exit  
 
  ethernet 1/20  
    queue-group profile q_group_2_level_default 
    no shutdown 
  exit  
 
 
 
ETX-2i 
3. Applications 
#*********** Configure SAG queue group profiles 
  sag 1/1  
    queue-group profile q_group_SAG_2_level_default 
  exit  
 
  sag 1/2  
    queue-group profile q_group_SAG_2_level_default 
  exit all 
 
#*********** Configure classifier profiles 
configure flows  
  classifier-profile v10 match-any 
    match vlan 10 
  exit  
 
  classifier-profile all match-any 
    match all 
  exit  
 
#*********** Configure flows 
  flow 10_sap 
    classifier v10 
    ingress-port ethernet 1/10 
    egress-port sap 1/1/2 queue-map-profile QueueMapDefaultProfile block 0/1 
    no shutdown 
  exit  
 
  flow sap_20 
    classifier all 
    ingress-port sap 1/1/2 
    egress-port eth 1/20 queue-map-profile QueueMapDefaultProfile block 0/1 
    no shutdown 
  exit  
 
  flow 20_sap 
    classifier v10 
    ingress-port ethernet 1/20 
    egress-port sap 1/2/2 queue-map-profile QueueMapDefaultProfile block 0/1 
    no shutdown 
  exit  
 
  configure flows flow sap_10 
    classifier all 
    ingress-port sap 1/2/2 
    egress-port eth 1/10 queue-map-profile QueueMapDefaultProfile block 0/1 
    no shutdown 
  exit all 
save 
ETX-2i 
3. Applications 
Testing the Application 
Checking E-Line Connectivity 
To check the E-Line application, use the data traffic application on the PC to verify the following: 
• 
Only untagged packets pass between CPEs. 
• 
Traffic passes from end to end between CPEs. 
Checking Port/Flow Statistics 
 To check the statistics: 
1. Connect ETX-2i, and view user port #0/3 statistics. 
2. Verify that counters are as expected according to the generated traffic rate and type. The 
following shows an example of the statistics: 
ETX­2i# configure port ethernet 0/3 
ETX­2i>config>port>eth(0/3)# show statistics 
Rates Sampling Window 
-------------------------------------------------------------- 
Window Size [Min.]        : 15         
Window Remain Time [Min.] : 4          
Running 
-------------------------------------------------------------- 
                             Rx                   Tx 
Total Frames               : 120368               40674  
Total Octets               : 182716280            61743132      
Total Frames/Sec           : 192                  65          
Total Bits/Sec (L1)        : 0                    0             
Minimum Bits/Sec (L1)      : 0                    0             
Maximum Bits/Sec (L1)      : 0                    0             
 
Total Bits/Sec (L2)        : 2342512              791576        
Minimum Bits/Sec (L2)      : 14572800             4972968       
Maximum Bits/Sec (L2)      : 14773176             4985112       
Unicast Frames             : 120366               40674        
Multicast Frames           : 0                    0       
Broadcast Frames           : 2                    0          
CRC Errors                 : 0                    --          
Error Frames               : 0                    0           
L2CP Discarded             : 0                    --          
OAM Discarded              : 0                    --             
MTU Discarded              : 0                    56             
Unknown Protocol Discarded : 0                    --          
CRC Errors/Sec             : 0                    --     
Jabber Errors              : 0                    --         
ETX-2i 
3. Applications 
Oversize Frames            : 0                    0        
64 Octets                  : 0                    0           
65-127 Octets              : 0                    0            
128-255 Octets             : 0                    0           
256-511 Octets             : 0                    0           
512-1023 Octets            : 0                    0            
1024-1528 Octets           : 121575               41084           
1519-2047 Octets           : 0                    0             
2048-Max Octets            : 0                    0            
MTU Discarded Flow         : --/EVC1-TLV 
3. View statistics for flow 3t1, and verify that counters are as expected according to the generated 
traffic rate and type. The following shows an example of the statistics: 
ETX­2i# configure flows flow 3t1 
ETX­2i#>config>flows>flow(3t1)# show statistics running 
Rate Sampling Window 
----------------------------------------------------------------------------- 
Window Size [Min.]        : 15 
Window Remain Time [Min.] : 12 
 
Rx Statistics 
----------------------------------------------------------------------------- 
          Total 
Packets : 20000 
Bytes   : 20000000 
 
Drop Statistics 
----------------------------------------------------------------------------- 
 
                   Packets              Bytes 
Total            : 197941               197941000 
Green            : 197941               197941000 
Yellow           : 0                    0 
Red              : 0                    0 
Yellow/Red       : 0                    0 
Drop  Rate 
-----------------------------------------------------------------------------  
                               pps           L1 (bps)        L2(bps) 
Total(Rate)      :             243           1947758         1800000 
Green(Rate)      :             243           1947758         1800000 
Yellow(Rate)     :             0             0               0 
Red(Rate)        :             0             0               0 
Yellow/Red(Rate) :             0             0               0 
Tx Statistics  
-----------------------------------------------------------------------------  
                               Packets       Bytes  
Total            :             197941        197941000  
Green            :             197941        197941000  
Yellow           :             0             0  
Tx  Rate 
-----------------------------------------------------------------------------  
                               pps           L1 (bps)        L2(bps) 
ETX-2i 
3. Applications 
Total(Rate)      :             243           1947758         1800000 
Green(Rate)      :             243           1947758         1800000 
Yellow(Rate)     :             0             0               0 
Peak Measurement  
-----------------------------------------------------------------------------  
                               L1  Min.   L2 Min    L1  Max    L2 Max.  
Tx Bit Rate [bps]  :           0          0         1300       1252 
Drop Bit Rate [bps]:           0          0         13000      121203  
3.2 Timing Synchronization for Mobile Networks 
This section describes RAD timing synchronization for mobile networks. The architecture presented here 
is an example and not a requirement. 
Timing distribution is based on PTP (1588) for accurate synchronization of LTE/LTE-A base stations.  
The solution is based on distributed Grandmasters with the unique, patented form factor of the MiCLK 
product. 
 
Addresses stringent  timing requirement (frequency/phase) for LTE/LTE-A  macro and small cells. 
This is an optimized solution, distributing cost-effective PTP Grand-masters, closer towards cell sites: 
• 
Dedicated PTP-GM device (ETX-2)  
• 
Unique SFP-based device (MiCLK), plugged into aggregation switch 
ETX-2i 
3. Applications 
The following are key benefits, compared to alternatives: 
• 
Saves on GPS for every cell-site 
• 
No need for supporting long BC/TC chains across the whole network 
• 
Best Timing quality with possible backup scenarios (e.g., backup from Sync-E) 
Equipment List 
The following table lists the devices required for the application. 
Device 
Version 
Quantity 
Role 
ETX­205A 
6.6.0(0.22) 
1 
Dedicated for Slave device  
ETX­2i  
6.6.0(0.22) 
1 
Dedicated PTP-GM device 
MiCLK 
2.2.1(0.37) 
1 
Unique SFP-based device  
MiCLK 
Overview 
• 
MiCLK is 1588 Grandmaster on SFP, joined to RAD Smart SPFs family 
• 
Based on MiNID infrastructure and 1588 package from ETX 
• 
Approved as a patent in Japan and USA (miniature Grandmaster) 
• 
Three ordering options (same HW, different SW load): 
 
MiCLK supporting up to eight 1588 slaves (L3) 
 
MiCLK supporting up to 24 1588 slaves (L3) 
 
MiCLK supporting up to 64 1588 slaves (L3) 
Features 
• 
GNSS (Global Navigation Satellite System) Receiver supporting GPS system 
• 
GNSS backup using Sync-E 
• 
PTP ITU-T GM supporting the following Telecom Profiles: 
 
G.8265.1 (IP\Unicast) 
ETX-2i 
3. Applications 
 
G.8275.1 (L2\Multicast) 
 
G.8275.2 (IP\Unicast) 
• 
VLAN tagging for G.8265.1, G.8275.2, G.8275.1, and management 
• 
64 IP unicast slaves @ 128 PPS (symmetric) 
• 
DSCP/TOS marking for G.8265.1/G.8275.2 (IP/unicast) and management traffic 
• 
Sync-E frequency distribution 
• 
Power consumption less than 1.5W 
• 
Full support of IPv6 for Management and PTP data.  
• 
TACACS+ for enhanced security  
• 
DSCP for APTS to prioritize the 1588 packets 
MiCLK Physical Ports and LEDs 
• 
Ethernet port 1000-Base-X (GE) via MSA 
• 
GNSS ANT via mini-BNC (front right connector) 
• 
1-PPS out (clock in for future phase) via mini-BNC (front left connector) 
• 
Two LEDs: 
 
Green – GNSS status 
 
Red – Alarm 
 
 
 
ETX-2i 
3. Applications 
Typical Application and Deployment of MiCLK 
MiCLK can be configured and deployed in three main synchronization methods:  
• 
ITU-T G.8265.1 IP/unicast frequency without full timing support from the network 
• 
ITU-T G.8275.1 L2/multicast, phase, and time distribution with full timing support from the 
network 
• 
ITU-T G.8275.2 IP/unicast, time and phase with partial support from the network 
As displayed below –MiCLK can be connected to any Router/Switch between the Core and 
Aggregation/Access network connected. In addition, the Grandmaster can be a redundant clock source 
to MiCLK. 
 
MiCLK Web 
MiCLK can be managed from the Web in addition to CLI. 
 
ETX-2i 
3. Applications 
• 
1588 Recovered block was added 
• 
Another clock source is available in Clock Domain (APTS) 
 
MiCLK – Configuration Model 
The following elements should be configured in MiCLK  
ETX-2i 
3. Applications 
1588 Recovered should be configured if APTS is required. 
Configuring x86 with TWAMP Light 
You can reach the PMC from ETX-205A/X by entering: 
configure chassis ve-module remote desktop 
Once you conclude the x86 configuration (see below), you can log out from PMC by pressing CTRL + shift 
+ “-“. 
 To configure x86 with TWAMP Light: 
    configure  
        echo "Terminal Configuration" 
#       Terminal Configuration 
        terminal  
            timeout forever  
        exit 
        echo "System Configuration" 
#       System Configuration 
        system  
            name "PMC_TWAMP_Light"  
            date-and-time  
                zone utc +03:00  
                echo "NTP (Network Time Protocol)" 
#               NTP (Network Time Protocol) 
                ntp  
                    server 1  
                        address 172.17.171.141  
                        prefer  
                        no shutdown  
                    exit 
                exit 
            exit 
        exit 
        echo "Management configuration" 
ETX-2i 
3. Applications 
#       Management configuration 
        management  
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp  
                target-params "p1"  
                    message-processing-model snmpv3  
                    version usm  
                    security name "initial" level no-auth-no-priv  
                    no shutdown  
                exit 
                target "TS_RV"  
                    target-params "p1"  
                    address udp-domain 172.17.192.40  
                    no shutdown  
                    tag-list "unmasked"  
                    trap-sync-group 1  
                exit 
            exit 
        exit 
        router 1  
            name "Router#1"  
            interface 1  
                address 172.17.192.163/24  
                name "PMC_TWAMP_Light"  
                bind ethernet 1  
                vlan 4094  
                dhcp-client  
                    client-id mac  
                exit 
                no shutdown  
            exit 
            interface 2  
                address 30.30.30.1/24  
                bind ethernet 1  
                vlan 30  
                dhcp-client  
                    client-id mac  
                exit 
                no shutdown  
            exit 
            static-route 0.0.0.0/0 address 172.17.192.1 metric 1  
        exit 
        echo "Reporting" 
#       Reporting 
        reporting  
            pm-collection twamp interval 10  
        exit 
        oam  
        exit 
    exit 
 
ETX-2i 
3. Applications 
    configure  
        oam  
            twamp  
                echo "TWAMP - Profile Configuration" 
#               TWAMP - Profile Configuration 
                profile "1" 1  
                exit 
                echo "TWAMP - Controller Configuration" 
#               TWAMP - Controller Configuration 
                controller "1" 1  
                    router-entity 1  
                    local-ip-address 30.30.30.1  
                    no shutdown  
                    echo "TWAMP - Controller Peer Configuration" 
#                   TWAMP - Controller Peer Configuration 
                    peer 30.30.30.10  
                        test-session 1 name "pmc_1" test-profile "1" dscp 26  
                        responder-seq-num  
                        activate continuous  
                    exit 
                exit 
            exit 
        exit 
    exit 
Mobile Services: Application Diagram 
 
ETX-2i 
3. Applications 
IP Allocation 
 
Configuring MiCLK_GM – G.8275-2 
Application Diagram 
 
ETX-2i 
3. Applications 
Initial Configuration 
1. Change MiCLK DIP Switch to “Config” Mode. 
2. Insert MiCLK into the hub.  
3. Access the MiCLK with a telnet/Web to its default IP 
address – 192.168.205.1 
4. Configure the following: 
 
MNG 
 
GNSS 
 
Domain 
 
Master PTP profile g.8275-2 
 
Sync-E – Optional 
5. Save. 
6. Changed DIP switch to Normal. 
7. Insert MiCLK into ETX-2i-10G (Port 0/17) or where the 
MNG flow is defined. 
Configuring the Hosting Device 
####################################################################### 
#                         2.ETX-2i_10G.txt                            # 
#######################################################################  
configure port svi 1  
no shutdown 
exit all 
 
#*******************************  SNMP Management Configuration ******* 
configure management  
snmp  
target-params "225"  
message-processing-model snmpv3  
version usm  
security name "initial" level no-auth-no-priv  
no shutdown  
exit 
target "225"  
target-params "225"  
address udp-domain 172.17.191.225 
no shutdown  
tag-list "unmasked"  
trap-sync-group 1  
exit all 
 
ETX-2i 
3. Applications 
config system name "ETX2i_10G" 
 
 
#******************************* INBAND MNG Flows ********************* 
 
 
#******************************* Bridge Ports ************************* 
 
configure bridge 1 
port 1 
no shutdown 
exit 
port 2 
no shutdown 
exit 
vlan 100 
exit all 
 
#******************************* INBAND MNG Flows ********************* 
 
configure flows 
classifier-profile "mng_4094" match-any 
match vlan 4094 
exit 
 
classifier-profile "v100" match-any 
match vlan 100 
exit 
 
 
flow "mng_4094"  
classifier "mng_4094"  
no policer  
ingress-port ethernet 0/1 
egress-port bridge-port 1 1  
reverse-direction block 0/1 
mark all 
vlan 100 
exit  
no shutdown  
exit 
 
 
flow "mng_etx"  
classifier "mng_untagged"  
no policer  
vlan-tag push vlan 100 p-bit fixed 4 
ingress-port svi 1 
egress-port bridge-port 1 2  
reverse-direction  
no shutdown  
exit all 
ETX-2i 
3. Applications 
 
#*******************************  Router_Interface ******************** 
 
configure router 1 
interface 1 
address 172.17.197.105/24 
bind svi 1 
no shutdown 
exit  
static-route 0.0.0.0/0 address 172.17.197.1 
exit all 
 
#********************************************************************** 
#*******************************END************************************ 
#********************************************************************** 
 
 
save 
 
####################################################################### 
#                      3.ETX-2i_10G_MNG_MiCLK.txt                     # 
#######################################################################  
configure bridge 1 
port 3 
no shutdown 
exit all 
 
#******************************* INBAND MNG Flows ********************* 
 
configure flows 
 
flow "mng_MiCLK"  
classifier "v100"  
no policer  
ingress-port ethernet 0/17 
egress-port bridge-port 1 3  
reverse-direction block 0/1 
no shutdown  
exit all 
 
save 
MiCLK Operation Modes (DIP Switch) 
MiCLK is a member of the RAD Smart SFP family. As such, the DIP Switch configuration provides four 
operational modes, described in the following table. 
ETX-2i 
3. Applications 
Mode 
Function 
Config 
Device response to its default IP address (192.168.205.1), even if IP address has been changed 
(no host VLAN) 
INIT DB 
Resets device database to its factory default values including reset host parameters (IP, DGW, 
VLAN, etc’) during power up 
SW Download 
Access MiCLK boot (“miBoot”) menu using SFP-CA.2 
Normal 
Normal operation mode 
MiCLK Basic Configuration (MNG) 
 
ETX-2i 
3. Applications 
MiCLK G.8275-2 Profile Configuration (GNSS) 
 
ETX-2i 
3. Applications 
MiCLK GNSS Status 
 
ETX-2i 
3. Applications 
MiCLK G.8275-2 Profile Configuration (Domain) 
 
MiCLK G.8275-2 Profile Configuration (Router) 
 
ETX-2i 
3. Applications 
MiCLK G.8275-2 Profile Configuration (Grandmaster) 
 
Status of GNSS Grandmaster
 
ETX-2i 
3. Applications 
MiCLK G.8275-2 Profile Configuration (Optionally SyncE) 
 
MiCLK_APTS – G.8275-2 
1. Change MiCLK DIP Switch to “Config” Mode 
2. Insert MiCLK into the hub. 
3. Access MiCLK with Telnet to its default IP address – 192.168.205.1 
4. Configure the following: 
 
MNG 
 
GNSS 
 
Domain 
 
Recovered 1 ptp profile g.8275-2 apts 
 
Master PTP profile g.8275-2 
 
Sync-E – Optionally   
5. Save. 
6. Change DIP switch to Normal. 
7. Insert MiCLK into ETX-2i (Port 0/3). 
ETX-2i 
3. Applications 
Configuration on Web 
  
Application Diagram 
 
MiCLK_APTS – G.8275-2 
The following instructions are based on the previous figures: 
ETX-2i 
3. Applications 
For each group, repeat the following steps: 
• 
MiCLK G.8275-2 Profile Configuration (GNSS). 
• 
MiCLK G.8275-2 Profile Configuration (Domain). 
• 
MiCLK G.8275-2 Profile Configuration (Router- set the IP per group). 
 
Clock domain – APTS clock source 
APTS should be declared as a clock source in clock Domain 
 
APTS – Recovered Clock 
Recovered IP address should be identical to the 1588 Master IP address 
ETX-2i 
3. Applications 
CLI 
MiCLK>config>clock# [no] recovered <id> ptp profile g.8275-1 apts 
MiCLK>config>clock>recovered(1)# [no] revertive 
MiCLK>config>clock>recovered(1)# wait-to-restore <seconds>[0..720]default 300 
MiCLK>config>clock>recovered(1)# [no] ip-address <ip-address> 
MiCLK>config>clock>recovered(1)# ptp-domain <domain-id>[0..127, default 24]  
MiCLK>config>clock>recovered(1)# clear-network-metrics {master-to-slave|slave-to-master|all} 
MiCLK>config>clock>recovered(1)# [no] shutdown 
 
APTS – Bind 1588 Master to Recovered Clock (Web) 
The 1588 recovered entity can work opposite two 1588 Grandmasters 
 
ETX-2i 
3. Applications 
APTS – Master Status 
1588 Master attached to 1588 recovered (APTS) can be observed via WEB  
 
APTS – Recovered status 
 
 
 
ETX-2i 
3. Applications 
MiCLK_APTS – G.8275-2 
For each group, repeat the following steps: 
• 
MiCLK G.8275-2 Profile Configuration (Master). 
• 
MiCLK G.8275-2 Profile Configuration (Master Status). 
 
ETX-205_Slave 
Configure the following Flows through the bridge: 
• 
MNG Configuration for ETX-205_Slave: Using VLAN 4094 
• 
1588 Flows From/To MiCLK: Using VLAN 200 
 
 
ETX-2i 
3. Applications 
ETX-205_Slave - G.8265-1 
 
 
ETX-2i 
3. Applications 
 
 
ETX-2i 
3. Applications 
 
 
 
ETX-2i 
3. Applications 
Success Criteria – APTS 
Disconnect the GNSS antenna from the side where the APTS is defined. 
The status of the GNSS is down on the Domain 
 
The Clock Domain manages the frequency sources. 
Thus, when there is GNSS failure, the Clock Domain switches to an alternative fallback frequency.  
This fallback frequency can be from SyncE or from APTS. 
As a result, the Clock Domain shows Locked status to the selected frequency source. 
 
ETX-2i 
3. Applications 
The PTP Master however, when GNSS fails, switches to Holdover states. This can be seen by the 
clockClass in the Master screens. 
When GNSS is LOCKED the transmitted clockClass is 6. When there is a GNSS failure, the transmitted 
clockClass switches to 7. Depending on the frequency quality it either remains 7 or downgrades 
according to Table 2 in G.8275.2 (and the corresponding table in G.8275.1). 
 
ETX-2i 
3. Applications 
Success Criteria – APTS : CLI Log 
Configure -> Reporting -> show log 
3.3 Carrier-Class Ethernet Application 
This section describes the test plan that demonstrates the functionality of a generic Carrier Class 
Ethernet application based on the RAD ETX product line.  
RAD’s ETX-A line of Carrier Ethernet demarcation and aggregation devices, together with the Radview 
management system enables carriers and service providers to provide managed Carrier Ethernet 
connectivity solutions to their business and mobile client bases. 
Solutions are detailed and grouped for delivering EAD, EAD with timing capabilities, and 10GbE EAD 
services together with the management and performance monitoring capabilities that are pivotal to 
meeting exacting business customer service expectations. 
The test plan in this section uses RAD equipment: ETX-203AX, ETX-220A, ETX-2i, and Micro Network 
Interface Device (MiNID), which include the main features of the family of demarcations regarding traffic 
management (Ethernet traffic), monitoring (OAM, CFM, Y.1731), TWAMP, stress test (Y.1564, L3SAT), 
and recovery capability upon failure. The RAD Service Assured Access (SAA) solution offers a complete 
end-to-end solution for service activation and assurance with extensive fault/performance management 
and QoS capabilities. 
ETX-2i 
3. Applications 
Equipment List 
The following table lists the devices required for the application. 
Device 
Quantity 
ETX­203AX 
1 
ETX-220A 
1 
ETX­2i  
1 
MiNID 
1 
RADview performance portal 
1 
Layout Diagrams 
HLD 
With the ETX family and MiNID, RAD provides a very powerful solution for enhanced Ethernet services. 
The concept of SAA enables the Carrier to build services and monitor the SLA they sold. This document 
describes the interworking between the SAA portfolio members.  
 
ETX-2i 
3. Applications 
LLD 
The solution allows for continuous monitoring of L2/L3 VPN service quality based on standard OAM 
protocols (Y.1731 for L2, TWAMP for L3).  
The PM tests are carried out by ETX-2 or MiNID units at branches. PM controller is used for high scale 
testing, e.g., at HQ sites. Tests are carried opposite any standard responder where KPI records are 
reported by the controlling unit towards RADview PM.  
RADview PM acts as the presentation layer, translating the PM session results to graphical presentation 
of KPIs on a dashboard with drill-down capabilities and presentation/filter options by thresholds 
according to targeted SLA. 
The following POC begins with a very basic setup between two ETX-2 devices. Step by step, the number 
of devices and their functions are increased. The goal is to enable you to build up a complex Carrier 
Ethernet network in a ring topology with the complete SAA feature set.  
RADview is involved when PM or SM is used. 
The built-in toolbox that uses Carrier Ethernet, OAM, and TWAMP mechanisms, helps you show the 
customer the Quality of Service and provides tools to troubleshoot the network. 
 
Figure 4-1.  LLD Application – Detailed Diagram 
ETX-2i 
3. Applications 
LLD L3 Application – Detailed Diagram 
L2 Test Cases 
Management and Setup via RADview  
RADview is used for configuration of management and data services. 
This test case presents three modules:  
• 
Element Monitoring System (EMS) – Used to add a NID to the network topology, as well as 
present the alarms and status of each device added. 
• 
Service Manager (SM) – Used to create an E2E E-Line/E-LAN/E-Tree service between the two 
NIDs, while configuring various service setups. 
• 
Performance Monitor (PM) – Presents the PM Portal and SLA monitoring output. 
 
 
ETX-2i 
3. Applications 
Monitoring OAM CFM  
In this test case, OAM configuration performs online monitoring of each link through Layer 2 networks, 
using performance indicators such as Y.1731: 
• 
Frame Loss Ratio (FLR) 
• 
Frame Delay (FD) 
• 
Frame Delay Variation (FDV)  
The statistics can be monitored by RADview with PM. 
SAT Y.1564 Performance  
This test case shows how to configure and run Y.1564 (i.e., SAT), which tests SLA compliance in two 
steps: 
• 
Configuration test – a short test to confirm the configuration of the policy shapers and network 
connectivity  
• 
Performance test – a large test that measures Frame Loss Ratio (FLR), Frame Delay (FD), Frame 
Delay Variation (FDV). 
Test Steps 
Management via RADview 
Purpose 
Configure and verify management of ETX-2i-10G via RADview using VLAN 4090. 
Expected 
Results 
• Ability to add ETX-2i-10G to map RADview 
• ETX-2i-10G can be managed via RADview 
• Traps are sent to RADview 
Results 
□ PASS     □ FAIL    
ETX-2i 
3. Applications 
Comments 
 
 
 
 
 
ETX-2i 
3. Applications 
Ethernet Traffic – EPL Line 
Purpose  
Configure and verify EPL Line service. 
Expected 
Results 
• Set CE- VLAN ID. 
• Set priority on the CE-VLAN. 
• Set rate limit/bandwidth (CIR) on the service. 
• Set EIR on the service. 
• Perform VLAN mapping on the service. 
• Reclassify CoS value on the VLAN. 
• Set L2CP tunneling as per MEF standard for service. 
Results 
□ PASS     □ FAIL    
Comments 
ETX-2i 
3. Applications 
 
See scripts below. 
ETX-2i 
3. Applications 
NTY #1 LAG without LACP with OAM 
ETX # 1 
 
ETX-2I-10G-B# info 
    version "3.01A14" sw "6.4.0(0.27)" 
    configure 
        echo "Management configuration" 
#       Management configuration 
        management 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                target-params "tp1" 
                    message-processing-model snmpv3 
                    version usm 
                    security name "initial" level no-auth-no-priv 
                    no shutdown 
                exit 
                target "MyPC" 
                    target-params "tp1" 
                    address udp-domain 172.17.192.40 
                    no shutdown 
                    tag-list "unmasked" 
                    trap-sync-group 1 
                exit 
            exit 
        exit 
        echo "QoS - Configuration" 
#       QoS - Configuration 
        qos 
            policer-profile "S.Policer_10M.1130" 
                bandwidth cir 10000 cbs 64000 eir 50000 ebs 64000 
            exit 
            shaper-profile "S.Policer_10M.1127" 
                bandwidth cir 19968 cbs 64000 
            exit 
            queue-block-profile "S.Queue Block Profile.1128" 
                queue 0 
                    scheduling strict 
                exit 
                queue 1 
                    scheduling strict 
                exit 
                queue 2 
                    scheduling strict 
                exit 
                queue 3 
                    scheduling strict 
                exit 
                queue 4 
                    scheduling wfq 3 
                exit 
ETX-2i 
3. Applications 
                queue 5 
                    scheduling wfq 112 
                exit 
                queue 6 
                    scheduling wfq 3 
                exit 
                queue 7 
                    scheduling wfq 3 
                exit 
            exit 
            echo "Queue Group Configuration" 
#           Queue Group Configuration 
            queue-group-profile "DefaultQueueGroup" 
                queue-block 0/3 
                    name "S.Level 0 Queue Block.3" 
                    profile "S.Queue Block Profile.1128" 
                    shaper profile "S.Policer_10M.1127" 
                exit 
            exit 
            queue-map-profile "S.CoS_2_pBit.1131.CC" 
                map 0 to-queue 1 
                map 1 to-queue 7 
                map 2 to-queue 6 
                map 3 to-queue 5 
                map 4 to-queue 4 
                map 5 to-queue 3 
                map 6 to-queue 1 
                map 7 to-queue 0 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            echo "Service Virtual Interface- Port Configuration" 
#           Service Virtual Interface- Port Configuration 
            svi 96 
                no shutdown 
            exit 
            echo "LAG - Port Configuration" 
#           LAG - Port Configuration 
            lag 1 
                bind ethernet 0/1 
                bind ethernet 0/2 
                anchor-port ethernet 0/1 
                no shutdown 
            exit 
        exit 
        echo "Bridge Configuration" 
#       Bridge Configuration 
        bridge 1 
            name "BRIDGE 1" 
        exit 
ETX-2i 
3. Applications 
        echo "Flows Configuration" 
#       Flows Configuration 
        flows 
            echo "Classifier Profile Configuration" 
#           Classifier Profile Configuration 
            classifier-profile "mng_untagged" match-any 
                match untagged 
            exit 
            classifier-profile "mng_all" match-any 
                match all 
            exit 
            classifier-profile "v100" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT_1" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.170_vlan200" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.170_vlan200_1" match-any 
                match vlan 200 
            exit 
            echo "Flow Configuration" 
#           Flow Configuration 
            flow "mng_access_default_in" 
                classifier "mng_untagged" 
                no policer 
                ingress-port ethernet 0/101 
                egress-port svi 96 
                no shutdown 
            exit 
            flow "mng_access_default_out" 
                classifier "mng_all" 
                no policer 
                ingress-port svi 96 
                egress-port ethernet 0/101 
                no shutdown 
            exit 
            flow "S.169.1_1_1_LT" 
                classifier "S.169_LT" 
                no policer 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue-map-profile "S.CoS_2_pBit.1131.CC                              
" block 0/1 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
ETX-2i 
3. Applications 
            flow "S.169.1_1_LT" 
                classifier "S.169_LT_1" 
                policer profile "S.Policer_10M.1130" 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 5 block 0/3 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_1_vlan200" 
                classifier "S.170_vlan200" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1131.CC                              
" block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_vlan200" 
                classifier "S.170_vlan200_1" 
                no policer 
                vlan-tag push vlan 200 p-bit fixed 5 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
        exit 
        router 1 
            name "Router#1" 
            interface 1 
                dhcp-client 
                    client-id mac 
                exit 
                shutdown 
            exit 
            interface 32 
                address 172.17.192.105/24 
                bind svi 96 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 0.0.0.0/0 address 172.17.192.1 metric 1 
        exit 
    exit 
 
 
 
ETX-2i 
3. Applications 
    configure 
        oam 
            echo "OAM CFM Configuration" 
#           OAM CFM Configuration 
            cfm 
                maintenance-domain 1 
                    md-level 6 
                    no name 
                    maintenance-association 1 
                        name uint 100 
                        mep 101 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.169.1_1_1_LT" 
                            flow uni-direction tx "S.169.1_1_LT" 
                            queue queue-mapping "S.CoS_2_pBit.1131.CC" block 0/3                              
                            remote-mep 102 
                            ccm-priority 3 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 10000 
                                delay-var-threshold 3000 
                                classification priority-bit 3 
                                dest-ne 1 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                    maintenance-association 2 
                        name uint 200 
                        mep 101 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.170.1_1_1_vlan200" 
                            flow uni-direction tx "S.170.1_1_vlan200" 
                            queue queue-mapping "S.CoS_2_pBit.1131.CC" block 0/1                              
                            remote-mep 102 
                            ccm-priority 5 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 8000 
                                delay-var-threshold 2000 
                                classification priority-bit 5 
                                dest-ne 1 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
ETX-2i 
3. Applications 
                        exit 
                    exit 
                exit 
            exit 
        exit 
    exit 
 
 
ETX-2I-10G-B# 
ETX-2I-10G-B# 
ETX-2I-10G-B# 
NTY #2 LAG without LACP with OAM 
ETX-2I-10G-B# info 
    version "3.01A14" sw "6.4.0(0.27)" 
    configure 
        echo "Management configuration" 
#       Management configuration 
        management 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                target-params "tp1" 
                    message-processing-model snmpv3 
                    version usm 
                    security name "initial" level no-auth-no-priv 
                    no shutdown 
                exit 
                target "MyPC" 
                    target-params "tp1" 
                    address udp-domain 172.17.192.40 
                    no shutdown 
                    tag-list "unmasked" 
                    trap-sync-group 1 
                exit 
            exit 
        exit 
        echo "QoS - Configuration" 
#       QoS - Configuration 
        qos 
            policer-profile "S.Policer_10M.1124" 
                bandwidth cir 10000 cbs 64000 eir 50000 ebs 64000 
            exit 
            shaper-profile "S.Policer_10M.1121" 
                bandwidth cir 19968 cbs 64000 
            exit 
            queue-block-profile "S.Queue Block Profile.1122" 
                queue 0 
                    scheduling strict 
                exit 
                queue 1 
ETX-2i 
3. Applications 
                    scheduling strict 
                exit 
                queue 2 
                    scheduling strict 
                exit 
                queue 3 
                    scheduling strict 
                exit 
                queue 4 
                    scheduling wfq 3 
                exit 
                queue 5 
                    scheduling wfq 112 
                exit 
                queue 6 
                    scheduling wfq 3 
                exit 
                queue 7 
                    scheduling wfq 3 
                exit 
            exit 
            echo "Queue Group Configuration" 
#           Queue Group Configuration 
            queue-group-profile "DefaultQueueGroup" 
                queue-block 0/3 
                    name "S.Level 0 Queue Block.3" 
                    profile "S.Queue Block Profile.1122" 
                    shaper profile "S.Policer_10M.1121" 
                exit 
            exit 
            queue-map-profile "S.CoS_2_pBit.1125.CC" 
                map 0 to-queue 1 
                map 1 to-queue 7 
                map 2 to-queue 6 
                map 3 to-queue 5 
                map 4 to-queue 4 
                map 5 to-queue 3 
                map 6 to-queue 1 
                map 7 to-queue 0 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            echo "Service Virtual Interface- Port Configuration" 
#           Service Virtual Interface- Port Configuration 
            svi 96 
                no shutdown 
            exit 
            echo "LAG - Port Configuration" 
#           LAG - Port Configuration 
            lag 1 
ETX-2i 
3. Applications 
                admin-key ten-giga-ethernet 
                bind ethernet 0/1 
                bind ethernet 0/2 
                anchor-port ethernet 0/1 
                no shutdown 
            exit 
        exit 
        echo "Flows Configuration" 
#       Flows Configuration 
        flows 
            echo "Classifier Profile Configuration" 
#           Classifier Profile Configuration 
            classifier-profile "mng_untagged" match-any 
                match untagged 
            exit 
            classifier-profile "mng_all" match-any 
                match all 
            exit 
            classifier-profile "v100" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169.1_LT" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT_1" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.170.1_vlan200" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.170_vlan200_1" match-any 
                match vlan 200 
            exit 
            echo "Flow Configuration" 
#           Flow Configuration 
            flow "mng_access_default_in" 
                classifier "mng_untagged" 
                no policer 
                ingress-port ethernet 0/101 
                egress-port svi 96 
                no shutdown 
            exit 
            flow "mng_access_default_out" 
                classifier "mng_all" 
                no policer 
                ingress-port svi 96 
                egress-port ethernet 0/101 
                no shutdown 
            exit 
            flow "S.169.1_1_1_LT" 
                classifier "S.169.1_LT" 
                no policer 
ETX-2i 
3. Applications 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue-map-profile "S.CoS_2_pBit.1125.CC" block 0/1 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.169.1_1_LT" 
                classifier "S.169_LT_1" 
                policer profile "S.Policer_10M.1124" 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 5 block 0/3 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_1_vlan200" 
                classifier "S.170.1_vlan200" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1125.CC" block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_vlan200" 
                classifier "S.170_vlan200_1" 
                no policer 
                vlan-tag push vlan 200 p-bit fixed 5 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
        exit 
        router 1 
            name "Router#1" 
            interface 32 
                address 172.17.192.106/24 
                bind svi 96 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 0.0.0.0/0 address 172.17.192.1 metric 1 
        exit 
    exit 
 
    configure 
        oam 
ETX-2i 
3. Applications 
            echo "OAM CFM Configuration" 
#           OAM CFM Configuration 
            cfm 
                maintenance-domain 1 
                    md-level 6 
                    no name 
                    maintenance-association 1 
                        name uint 100 
                        mep 102 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.169.1_1_1_LT" 
                            flow uni-direction tx "S.169.1_1_LT" 
                            queue queue-mapping "S.CoS_2_pBit.1125.CC" block 0/3 
                            remote-mep 101 
                            ccm-priority 3 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 10000 
                                delay-var-threshold 3000 
                                classification priority-bit 3 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                    maintenance-association 2 
                        name uint 200 
                        mep 102 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.170.1_1_1_vlan200" 
                            flow uni-direction tx "S.170.1_1_vlan200" 
                            queue queue-mapping "S.CoS_2_pBit.1125.CC" block 0/1 
                            remote-mep 101 
                            ccm-priority 5 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 8000 
                                delay-var-threshold 2000 
                                classification priority-bit 5 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
ETX-2i 
3. Applications 
                exit 
            exit 
        exit 
    exit 
 
 
ETX-2I-10G-B# 
Ethernet Traffic – EPL LAN 
Purpose  
Configure and verify EPL Lan service. 
Expected 
Results 
1.  
Results 
□ PASS     □ FAIL    
Comments 
See scripts below. 
 
 
ETX-2i 
3. Applications 
Ethernet Traffic – ELAN NTU1 
ETX-2I-10G-B# info 
    version "3.01A14" sw "6.4.0(0.27)" 
    configure 
        echo "Management configuration" 
#       Management configuration 
        management 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                target-params "tp1" 
                    message-processing-model snmpv3 
                    version usm 
                    security name "initial" level no-auth-no-priv 
                    no shutdown 
                exit 
                target "MyPC" 
                    target-params "tp1" 
                    address udp-domain 172.17.192.40 
                    no shutdown 
                    tag-list "unmasked" 
                    trap-sync-group 1 
                exit 
            exit 
        exit 
        echo "QoS - Configuration" 
#       QoS - Configuration 
        qos 
            policer-profile "S.Policer_10M.1130" 
                bandwidth cir 10000 cbs 64000 eir 50000 ebs 64000 
            exit 
            shaper-profile "S.Policer_10M.1127" 
ETX-2i 
3. Applications 
                bandwidth cir 19968 cbs 64000 
            exit 
            queue-block-profile "S.Queue Block Profile.1128" 
                queue 0 
                    scheduling strict 
                exit 
                queue 1 
                    scheduling strict 
                exit 
                queue 2 
                    scheduling strict 
                exit 
                queue 3 
                    scheduling strict 
                exit 
                queue 4 
                    scheduling wfq 3 
                exit 
                queue 5 
                    scheduling wfq 112 
                exit 
                queue 6 
                    scheduling wfq 3 
                exit 
                queue 7 
                    scheduling wfq 3 
                exit 
            exit 
            echo "Queue Group Configuration" 
#           Queue Group Configuration 
            queue-group-profile "DefaultQueueGroup" 
                queue-block 0/3 
                    name "S.Level 0 Queue Block.3" 
                    profile "S.Queue Block Profile.1128" 
                    shaper profile "S.Policer_10M.1127" 
                exit 
            exit 
            queue-map-profile "S.CoS_2_pBit.1131.CC" 
                map 0 to-queue 1 
                map 1 to-queue 7 
                map 2 to-queue 6 
                map 3 to-queue 5 
                map 4 to-queue 4 
                map 5 to-queue 3 
                map 6 to-queue 1 
                map 7 to-queue 0 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            echo "Service Virtual Interface- Port Configuration" 
ETX-2i 
3. Applications 
#           Service Virtual Interface- Port Configuration 
            svi 96 
                no shutdown 
            exit 
            echo "LAG - Port Configuration" 
#           LAG - Port Configuration 
            lag 1 
                bind ethernet 0/1 
                bind ethernet 0/2 
                anchor-port ethernet 0/1 
                no shutdown 
            exit 
        exit 
        echo "Bridge Configuration" 
#       Bridge Configuration 
        bridge 1 
            name "BRIDGE 1" 
        exit 
        echo "Flows Configuration" 
#       Flows Configuration 
        flows 
            echo "Classifier Profile Configuration" 
#           Classifier Profile Configuration 
            classifier-profile "mng_untagged" match-any 
                match untagged 
            exit 
            classifier-profile "mng_all" match-any 
                match all 
            exit 
            classifier-profile "v100" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT_1" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.170_vlan200" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.170_vlan200_1" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.197.3_elan_1" match-any 
                match vlan 300 
            exit 
            classifier-profile "S.197.1.3_elan_1" match-any 
                match vlan 300 
            exit 
            echo "Flow Configuration" 
#           Flow Configuration 
ETX-2i 
3. Applications 
            flow "mng_access_default_in" 
                classifier "mng_untagged" 
                no policer 
                ingress-port ethernet 0/101 
                egress-port svi 96 
                no shutdown 
            exit 
            flow "mng_access_default_out" 
                classifier "mng_all" 
                no policer 
                ingress-port svi 96 
                egress-port ethernet 0/101 
                no shutdown 
            exit 
            flow "S.169.1_1_1_LT" 
                classifier "S.169_LT" 
                no policer 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue-map-profile "S.CoS_2_pBit.1131.CC                              
" block 0/1 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.169.1_1_LT" 
                classifier "S.169_LT_1" 
                policer profile "S.Policer_10M.1130" 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 5 block 0/3 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_1_vlan200" 
                classifier "S.170_vlan200" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1131.CC                              
" block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_vlan200" 
                classifier "S.170_vlan200_1" 
                no policer 
                vlan-tag push vlan 200 p-bit fixed 5 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
ETX-2i 
3. Applications 
                no shutdown 
            exit 
            flow "S.197.3.1_1_elan" 
                classifier "S.197.3_elan_1" 
                no policer 
                vlan-tag push vlan 300 p-bit fixed 3 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 5 block 0/1 
                service-name "elan.197" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.197.1.1_1_1_elan" 
                classifier "S.197.1.3_elan_1" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue 5 block 0/1 
                service-name "elan.197" 
                pm-collection interval 900 
                no shutdown 
            exit 
        exit 
        router 1 
            name "Router#1" 
            interface 1 
                dhcp-client 
                    client-id mac 
                exit 
                shutdown 
            exit 
            interface 32 
                address 172.17.192.105/24 
                bind svi 96 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 0.0.0.0/0 address 172.17.192.1 metric 1 
        exit 
    exit 
 
    configure 
        oam 
            echo "OAM CFM Configuration" 
#           OAM CFM Configuration 
            cfm 
                maintenance-domain 1 
                    md-level 6 
                    no name 
                    maintenance-association 1 
ETX-2i 
3. Applications 
                        name uint 100 
                        mep 101 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.169.1_1_1_LT" 
                            flow uni-direction tx "S.169.1_1_LT" 
                            queue queue-mapping "S.CoS_2_pBit.1131.CC" block 0/3                              
                            remote-mep 102 
                            ccm-priority 3 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 10000 
                                delay-var-threshold 3000 
                                classification priority-bit 3 
                                dest-ne 1 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                    maintenance-association 2 
                        name uint 200 
                        mep 101 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.170.1_1_1_vlan200" 
                            flow uni-direction tx "S.170.1_1_vlan200" 
                            queue queue-mapping "S.CoS_2_pBit.1131.CC" block 0/1                              
                            remote-mep 102 
                            ccm-priority 5 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 8000 
                                delay-var-threshold 2000 
                                classification priority-bit 5 
                                dest-ne 1 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                exit 
            exit 
        exit 
    exit 
 
ETX-2I-10G-B# 
ETX-2i 
3. Applications 
Ethernet Traffic – ELAN NTU2 
ETX-2I-10G-B# info 
    version "3.01A14" sw "6.4.0(0.27)" 
    configure 
        echo "Management configuration" 
#       Management configuration 
        management 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                target-params "tp1" 
                    message-processing-model snmpv3 
                    version usm 
                    security name "initial" level no-auth-no-priv 
                    no shutdown 
                exit 
                target "MyPC" 
                    target-params "tp1" 
                    address udp-domain 172.17.192.40 
                    no shutdown 
                    tag-list "unmasked" 
                    trap-sync-group 1 
                exit 
            exit 
        exit 
        echo "QoS - Configuration" 
#       QoS - Configuration 
        qos 
            policer-profile "S.Policer_10M.1124" 
                bandwidth cir 10000 cbs 64000 eir 50000 ebs 64000 
            exit 
            shaper-profile "S.Policer_10M.1121" 
                bandwidth cir 19968 cbs 64000 
            exit 
            echo "COS Mapping Profile Configuration" 
#           COS Mapping Profile Configuration 
            cos-map-profile "S.CoS_2_pBit.197.CC" 
                map 0..1 to-cos 7 
                map 2 to-cos 6 
                map 3 to-cos 5 
                map 4 to-cos 4 
                map 5 to-cos 3 
                map 6 to-cos 1 
                map 7 to-cos 0 
            exit 
            queue-block-profile "S.Queue Block Profile.1122" 
                queue 0 
                    scheduling strict 
                exit 
                queue 1 
                    scheduling strict 
                exit 
ETX-2i 
3. Applications 
                queue 2 
                    scheduling strict 
                exit 
                queue 3 
                    scheduling strict 
                exit 
                queue 4 
                    scheduling wfq 3 
                exit 
                queue 5 
                    scheduling wfq 112 
                exit 
                queue 6 
                    scheduling wfq 3 
                exit 
                queue 7 
                    scheduling wfq 3 
                exit 
            exit 
            queue-block-profile "S.Queue Block Profile.1213_RX" 
            exit 
            queue-block-profile "S.Queue Block Profile.1207_RX" 
            exit 
            queue-block-profile "S.Queue Block Profile.1210_RX" 
            exit 
            echo "Queue Group Configuration" 
#           Queue Group Configuration 
            queue-group-profile "DefaultQueueGroup" 
                queue-block 0/3 
                    name "S.Level 0 Queue Block.3" 
                    profile "S.Queue Block Profile.1122" 
                    shaper profile "S.Policer_10M.1121" 
                exit 
                queue-block 0/4 
                    name "S.Level 0 Queue Block.4" 
                    profile "S.Queue Block Profile.1213_RX" 
                exit 
            exit 
            queue-map-profile "S.CoS_2_pBit.1125.CC" 
                map 0 to-queue 1 
                map 1 to-queue 7 
                map 2 to-queue 6 
                map 3 to-queue 5 
                map 4 to-queue 4 
                map 5 to-queue 3 
                map 6 to-queue 1 
                map 7 to-queue 0 
            exit 
        exit 
        echo "Port Configuration" 
 
 
ETX-2i 
3. Applications 
#       Port Configuration 
        port 
            echo "Service Virtual Interface- Port Configuration" 
#           Service Virtual Interface- Port Configuration 
            svi 96 
                no shutdown 
            exit 
            echo "LAG - Port Configuration" 
#           LAG - Port Configuration 
            lag 1 
                admin-key ten-giga-ethernet 
                bind ethernet 0/1 
                bind ethernet 0/2 
                anchor-port ethernet 0/1 
                no shutdown 
            exit 
        exit 
        echo "Bridge Configuration" 
#       Bridge Configuration 
        bridge 1 
            name "S.Bridge 1" 
            echo "Bridge Port Configuration" 
#           Bridge Port Configuration 
            port 1 
                name "S.Bridge 1 Port 1" 
                no shutdown 
            exit 
            port 2 
                name "S.Bridge 1 Port 2" 
                no shutdown 
            exit 
            port 3 
                name "S.Bridge 1 Port 3" 
                no shutdown 
            exit 
            echo "VLAN Configuration" 
#           VLAN Configuration 
            vlan 300 
            exit 
        exit 
        echo "Flows Configuration" 
#       Flows Configuration 
        flows 
            echo "Classifier Profile Configuration" 
#           Classifier Profile Configuration 
            classifier-profile "mng_untagged" match-any 
                match untagged 
            exit 
            classifier-profile "mng_all" match-any 
                match all 
            exit 
 
 
ETX-2i 
3. Applications 
            classifier-profile "v100" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169.1_LT" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT_1" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.170.1_vlan200" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.170_vlan200_1" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.elan.1214" match-any 
                match vlan 300 
            exit 
            classifier-profile "S.197.3_elan_1" match-any 
                match vlan 300 
            exit 
            classifier-profile "S.197.4_elan_1" match-any 
                match vlan 300 
            exit 
            echo "Flow Configuration" 
#           Flow Configuration 
            flow "mng_access_default_in" 
                classifier "mng_untagged" 
                no policer 
                ingress-port ethernet 0/101 
                egress-port svi 96 
                no shutdown 
            exit 
            flow "mng_access_default_out" 
                classifier "mng_all" 
                no policer 
                ingress-port svi 96 
                egress-port ethernet 0/101 
                no shutdown 
            exit 
            flow "S.169.1_1_1_LT" 
                classifier "S.169.1_LT" 
                no policer 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue-map-profile "S.CoS_2_pBit.1125.CC" block 0/1 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.169.1_1_LT" 
                classifier "S.169_LT_1" 
                policer profile "S.Policer_10M.1124" 
ETX-2i 
3. Applications 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 5 block 0/3 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_1_vlan200" 
                classifier "S.170.1_vlan200" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1125.CC" block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_vlan200" 
                classifier "S.170_vlan200_1" 
                no policer 
                vlan-tag push vlan 200 p-bit fixed 5 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.197.1_1_elan" 
                classifier "S.elan.1214" 
                cos-mapping profile "S.CoS_2_pBit.197.CC" 
                no policer 
                ingress-port ethernet 0/1 
                egress-port bridge-port 1 1 
                reverse-direction block 0/4 
                service-name "elan.197" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.197.3.1_1_elan" 
                classifier "S.197.3_elan_1" 
                no policer 
                vlan-tag push vlan 300 p-bit fixed 3 
                ingress-port ethernet 0/3 
                egress-port bridge-port 1 2 cos 5 
                reverse-direction block 0/4 
                service-name "elan.197" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.197.4.1_1_elan" 
                classifier "S.197.4_elan_1" 
                no policer 
                vlan-tag push vlan 300 p-bit fixed 3 
ETX-2i 
3. Applications 
                ingress-port ethernet 0/4 
                egress-port bridge-port 1 3 cos 5 
                reverse-direction block 0/4 
                service-name "elan.197" 
                pm-collection interval 900 
                no shutdown 
            exit 
        exit 
        router 1 
            name "Router#1" 
            interface 32 
                address 172.17.192.106/24 
                bind svi 96 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 0.0.0.0/0 address 172.17.192.1 metric 1 
        exit 
    exit 
 
    configure 
        oam 
            echo "OAM CFM Configuration" 
#           OAM CFM Configuration 
            cfm 
                maintenance-domain 1 
                    md-level 6 
                    no name 
                    maintenance-association 1 
                        name uint 100 
                        mep 102 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.169.1_1_1_LT" 
                            flow uni-direction tx "S.169.1_1_LT" 
                            queue queue-mapping "S.CoS_2_pBit.1125.CC" block 0/3 
                            remote-mep 101 
                            ccm-priority 3 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 10000 
                                delay-var-threshold 3000 
                                classification priority-bit 3 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
ETX-2i 
3. Applications 
                    exit 
                    maintenance-association 2 
                        name uint 200 
                        mep 102 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.170.1_1_1_vlan200" 
                            flow uni-direction tx "S.170.1_1_vlan200" 
                            queue queue-mapping "S.CoS_2_pBit.1125.CC" block 0/1 
                            remote-mep 101 
                            ccm-priority 5 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 8000 
                                delay-var-threshold 2000 
                                classification priority-bit 5 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                exit 
            exit 
        exit 
    exit 
 
 
ETX-2I-10G-B# 
Ethernet Traffic – EPL E-TREE 
Purpose  
Configure and verify EPL E-tree service 
Expected 
Results 
• Set CE- VLAN ID. 
• Set priority on the CE-VLAN.  
• Set rate limit/bandwidth (CIR) on the service. 
• Set EIR on the service. 
• Perform VLAN mapping on the service. 
• Re-classify CoS value on the VLAN. 
• Set L2CP tunneling as per MEF standard for service. 
Results 
□ PASS     □ FAIL    
Comments 
See scripts below. 
ETX-2i 
3. Applications 
 
Ethernet Traffic – ETREE NTU1 
ETX-2I-10G-B# info 
    version "3.01A14" sw "6.4.0(0.27)" 
    configure 
        echo "Management configuration" 
#       Management configuration 
        management 
            echo "SNMP Configuration" 
#           SNMP Configuration 
ETX-2i 
3. Applications 
            snmp 
                target-params "tp1" 
                    message-processing-model snmpv3 
                    version usm 
                    security name "initial" level no-auth-no-priv 
                    no shutdown 
                exit 
                target "MyPC" 
                    target-params "tp1" 
                    address udp-domain 172.17.192.40 
                    no shutdown 
                    tag-list "unmasked" 
                    trap-sync-group 1 
                exit 
            exit 
        exit 
        echo "QoS - Configuration" 
#       QoS - Configuration 
        qos 
            policer-profile "S.Policer_10M.1124" 
                bandwidth cir 10000 cbs 64000 eir 50000 ebs 64000 
            exit 
            shaper-profile "S.Policer_10M.1121" 
                bandwidth cir 19968 cbs 64000 
            exit 
            queue-block-profile "S.Queue Block Profile.1122" 
                queue 0 
                    scheduling strict 
                exit 
                queue 1 
                    scheduling strict 
                exit 
                queue 2 
                    scheduling strict 
                exit 
                queue 3 
                    scheduling strict 
                exit 
                queue 4 
                    scheduling wfq 3 
                exit 
                queue 5 
                    scheduling wfq 112 
                exit 
                queue 6 
                    scheduling wfq 3 
                exit 
                queue 7 
                    scheduling wfq 3 
                exit 
            exit 
            echo "Queue Group Configuration" 
ETX-2i 
3. Applications 
#           Queue Group Configuration 
            queue-group-profile "DefaultQueueGroup" 
                queue-block 0/3 
                    name "S.Level 0 Queue Block.3" 
                    profile "S.Queue Block Profile.1122" 
                    shaper profile "S.Policer_10M.1121" 
                exit 
            exit 
            queue-map-profile "S.CoS_2_pBit.1125.CC" 
                map 0 to-queue 1 
                map 1 to-queue 7 
                map 2 to-queue 6 
                map 3 to-queue 5 
                map 4 to-queue 4 
                map 5 to-queue 3 
                map 6 to-queue 1 
                map 7 to-queue 0 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            echo "Service Virtual Interface- Port Configuration" 
#           Service Virtual Interface- Port Configuration 
            svi 96 
                no shutdown 
            exit 
            echo "LAG - Port Configuration" 
#           LAG - Port Configuration 
            lag 1 
                admin-key ten-giga-ethernet 
                bind ethernet 0/1 
                bind ethernet 0/2 
                anchor-port ethernet 0/1 
                no shutdown 
            exit 
        exit 
        echo "Bridge Configuration" 
#       Bridge Configuration 
        bridge 1 
            name "S.Bridge 1" 
        exit 
        echo "Flows Configuration" 
#       Flows Configuration 
        flows 
            echo "Classifier Profile Configuration" 
#           Classifier Profile Configuration 
            classifier-profile "mng_untagged" match-any 
                match untagged 
            exit 
            classifier-profile "mng_all" match-any 
                match all 
ETX-2i 
3. Applications 
            exit 
            classifier-profile "v100" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169.1_LT" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT_1" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.170.1_vlan200" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.170_vlan200_1" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.198.3_ETREE_1" match-any 
                match vlan 400 
            exit 
            classifier-profile "S.198.1.3_ETREE_1" match-any 
                match vlan 400 
            exit 
            echo "Flow Configuration" 
#           Flow Configuration 
            flow "mng_access_default_in" 
                classifier "mng_untagged" 
                no policer 
                ingress-port ethernet 0/101 
                egress-port svi 96 
                no shutdown 
            exit 
            flow "mng_access_default_out" 
                classifier "mng_all" 
                no policer 
                ingress-port svi 96 
                egress-port ethernet 0/101 
                no shutdown 
            exit 
            flow "S.169.1_1_1_LT" 
                classifier "S.169.1_LT" 
                no policer 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue-map-profile "S.CoS_2_pBit.1125.CC                              
" block 0/1 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.169.1_1_LT" 
                classifier "S.169_LT_1" 
                policer profile "S.Policer_10M.1124" 
                ingress-port ethernet 0/3 
ETX-2i 
3. Applications 
                egress-port ethernet 0/1 queue 5 block 0/3 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_1_vlan200" 
                classifier "S.170.1_vlan200" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1125.CC                              
" block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_vlan200" 
                classifier "S.170_vlan200_1" 
                no policer 
                vlan-tag push vlan 200 p-bit fixed 5 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.198.3.1_1_ETREE" 
                classifier "S.198.3_ETREE_1" 
                no policer 
                mark all 
                    vlan 400 
                exit 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "ETREE.198" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.198.1.1_1_1_ETREE" 
                classifier "S.198.1.3_ETREE_1" 
                no policer 
                mark all 
                    vlan 400 
                exit 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue 3 block 0/1 
                service-name "ETREE.198" 
                pm-collection interval 900 
                no shutdown 
            exit 
        exit 
 
 
ETX-2i 
3. Applications 
        router 1 
            name "Router#1" 
            interface 32 
                address 172.17.192.106/24 
                bind svi 96 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 0.0.0.0/0 address 172.17.192.1 metric 1 
        exit 
    exit 
 
    configure 
        oam 
            echo "OAM CFM Configuration" 
#           OAM CFM Configuration 
            cfm 
                maintenance-domain 1 
                    md-level 6 
                    no name 
                    maintenance-association 1 
                        name uint 100 
                        mep 102 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.169.1_1_1_LT" 
                            flow uni-direction tx "S.169.1_1_LT" 
                            queue queue-mapping "S.CoS_2_pBit.1125.CC" block 0/3                              
                            remote-mep 101 
                            ccm-priority 3 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 10000 
                                delay-var-threshold 3000 
                                classification priority-bit 3 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                    maintenance-association 2 
                        name uint 200 
                        mep 102 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.170.1_1_1_vlan200" 
                            flow uni-direction tx "S.170.1_1_vlan200" 
                            queue queue-mapping "S.CoS_2_pBit.1125.CC" block 0/1                              
ETX-2i 
3. Applications 
                            remote-mep 101 
                            ccm-priority 5 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 8000 
                                delay-var-threshold 2000 
                                classification priority-bit 5 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                exit 
            exit 
        exit 
    exit 
 
 
ETX-2I-10G-B# 
Ethernet Traffic – ETREE NTU2 
ETX-2I-10G-B# info 
    version "3.01A14" sw "6.4.0(0.27)" 
    configure 
        echo "Management configuration" 
#       Management configuration 
        management 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                target-params "tp1" 
                    message-processing-model snmpv3 
                    version usm 
                    security name "initial" level no-auth-no-priv 
                    no shutdown 
                exit 
                target "MyPC" 
                    target-params "tp1" 
                    address udp-domain 172.17.192.40 
                    no shutdown 
                    tag-list "unmasked" 
                    trap-sync-group 1 
                exit 
            exit 
        exit 
        echo "QoS - Configuration" 
#       QoS - Configuration 
ETX-2i 
3. Applications 
        qos 
            policer-profile "S.Policer_10M.1130" 
                bandwidth cir 10000 cbs 64000 eir 50000 ebs 64000 
            exit 
            shaper-profile "S.Policer_10M.1127" 
                bandwidth cir 19968 cbs 64000 
            exit 
            echo "COS Mapping Profile Configuration" 
#           COS Mapping Profile Configuration 
            cos-map-profile "S.CoS_2_pBit.198.CC" 
                map 0..1 to-cos 7 
                map 2 to-cos 6 
                map 3 to-cos 5 
                map 4 to-cos 4 
                map 5 to-cos 3 
                map 6 to-cos 1 
                map 7 to-cos 0 
            exit 
            queue-block-profile "S.Queue Block Profile.1128" 
                queue 0 
                    scheduling strict 
                exit 
                queue 1 
                    scheduling strict 
                exit 
                queue 2 
                    scheduling strict 
                exit 
                queue 3 
                    scheduling strict 
                exit 
                queue 4 
                    scheduling wfq 3 
                exit 
                queue 5 
                    scheduling wfq 112 
                exit 
                queue 6 
                    scheduling wfq 3 
                exit 
                queue 7 
                    scheduling wfq 3 
                exit 
            exit 
            queue-block-profile "S.Queue Block Profile.1223_RX" 
            exit 
            queue-block-profile "S.Queue Block Profile.1227_RX" 
            exit 
            queue-block-profile "S.Queue Block Profile.1230_RX" 
            exit 
            echo "Queue Group Configuration" 
#           Queue Group Configuration 
ETX-2i 
3. Applications 
            queue-group-profile "DefaultQueueGroup" 
                queue-block 0/3 
                    name "S.Level 0 Queue Block.3" 
                    profile "S.Queue Block Profile.1128" 
                    shaper profile "S.Policer_10M.1127" 
                exit 
                queue-block 0/4 
                    name "S.Level 0 Queue Block.4" 
                    profile "S.Queue Block Profile.1223_RX" 
                exit 
            exit 
            queue-map-profile "S.CoS_2_pBit.1131.CC" 
                map 0 to-queue 1 
                map 1 to-queue 7 
                map 2 to-queue 6 
                map 3 to-queue 5 
                map 4 to-queue 4 
                map 5 to-queue 3 
                map 6 to-queue 1 
                map 7 to-queue 0 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            echo "Service Virtual Interface- Port Configuration" 
#           Service Virtual Interface- Port Configuration 
            svi 96 
                no shutdown 
            exit 
            echo "LAG - Port Configuration" 
#           LAG - Port Configuration 
            lag 1 
                bind ethernet 0/1 
                bind ethernet 0/2 
                anchor-port ethernet 0/1 
                no shutdown 
            exit 
        exit 
        echo "Bridge Configuration" 
#       Bridge Configuration 
        bridge 1 
            name "BRIDGE 1" 
            echo "Bridge Port Configuration" 
#           Bridge Port Configuration 
            port 1 
                name "S.Bridge 1 Port 1" 
                no shutdown 
            exit 
            port 2 
                name "S.Bridge 1 Port 2" 
                no shutdown 
ETX-2i 
3. Applications 
            exit 
            port 3 
                name "S.Bridge 1 Port 3" 
                no shutdown 
            exit 
            echo "VLAN Configuration" 
#           VLAN Configuration 
            vlan 400 
                mode e-tree 
                root 1 
            exit 
        exit 
        echo "Flows Configuration" 
#       Flows Configuration 
        flows 
            echo "Classifier Profile Configuration" 
#           Classifier Profile Configuration 
            classifier-profile "mng_untagged" match-any 
                match untagged 
            exit 
            classifier-profile "mng_all" match-any 
                match all 
            exit 
            classifier-profile "v100" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT_1" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.170_vlan200" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.170_vlan200_1" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.ETREE.1224" match-any 
                match vlan 400 
            exit 
            classifier-profile "S.198.3_ETREE_1" match-any 
                match vlan 400 
            exit 
            classifier-profile "S.198.4_ETREE_1" match-any 
                match vlan 400 
            exit 
            echo "Flow Configuration" 
#           Flow Configuration 
            flow "mng_access_default_in" 
                classifier "mng_untagged" 
                no policer 
ETX-2i 
3. Applications 
                ingress-port ethernet 0/101 
                egress-port svi 96 
                no shutdown 
            exit 
            flow "mng_access_default_out" 
                classifier "mng_all" 
                no policer 
                ingress-port svi 96 
                egress-port ethernet 0/101 
                no shutdown 
            exit 
            flow "S.169.1_1_1_LT" 
                classifier "S.169_LT" 
                no policer 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue-map-profile "S.CoS_2_pBit.1131.CC                              
" block 0/1 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.169.1_1_LT" 
                classifier "S.169_LT_1" 
                policer profile "S.Policer_10M.1130" 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 5 block 0/3 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_1_vlan200" 
                classifier "S.170_vlan200" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1131.CC                              
" block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_vlan200" 
                classifier "S.170_vlan200_1" 
                no policer 
                vlan-tag push vlan 200 p-bit fixed 5 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.198.1_1_ETREE" 
ETX-2i 
3. Applications 
                classifier "S.ETREE.1224" 
                cos-mapping profile "S.CoS_2_pBit.198.CC" 
                no policer 
                ingress-port ethernet 0/1 
                egress-port bridge-port 1 1 
                reverse-direction block 0/4 
                service-name "ETREE.198" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.198.3.1_1_ETREE" 
                classifier "S.198.3_ETREE_1" 
                no policer 
                mark all 
                    vlan 400 
                exit 
                ingress-port ethernet 0/3 
                egress-port bridge-port 1 2 cos 3 
                reverse-direction block 0/4 
                service-name "ETREE.198" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.198.4.1_1_ETREE" 
                classifier "S.198.4_ETREE_1" 
                no policer 
                mark all 
                    vlan 400 
                exit 
                ingress-port ethernet 0/4 
                egress-port bridge-port 1 3 cos 3 
                reverse-direction block 0/4 
                service-name "ETREE.198" 
                pm-collection interval 900 
                no shutdown 
            exit 
        exit 
        router 1 
            name "Router#1" 
            interface 1 
                dhcp-client 
                    client-id mac 
                exit 
                shutdown 
            exit 
            interface 32 
                address 172.17.192.105/24 
                bind svi 96 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
ETX-2i 
3. Applications 
            exit 
            static-route 0.0.0.0/0 address 172.17.192.1 metric 1 
        exit 
    exit 
 
    configure 
        oam 
            echo "OAM CFM Configuration" 
#           OAM CFM Configuration 
            cfm 
                maintenance-domain 1 
                    md-level 6 
                    no name 
                    maintenance-association 1 
                        name uint 100 
                        mep 101 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.169.1_1_1_LT" 
                            flow uni-direction tx "S.169.1_1_LT" 
                            queue queue-mapping "S.CoS_2_pBit.1131.CC" block 0/3                              
                            remote-mep 102 
                            ccm-priority 3 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 10000 
                                delay-var-threshold 3000 
                                classification priority-bit 3 
                                dest-ne 1 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                    maintenance-association 2 
                        name uint 200 
                        mep 101 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.170.1_1_1_vlan200" 
                            flow uni-direction tx "S.170.1_1_vlan200" 
                            queue queue-mapping "S.CoS_2_pBit.1131.CC" block 0/1                              
                            remote-mep 102 
                            ccm-priority 5 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 8000 
                                delay-var-threshold 2000 
                                classification priority-bit 5 
                                dest-ne 1 
ETX-2i 
3. Applications 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                exit 
            exit 
        exit 
    exit 
 
 
ETX-2I-10G-B# 
ETX-2I-10G-B# 
Ethernet Traffic – EPL Access 
Test Purpose  
Configure and verify EPL Access service 
Expected 
Results 
• 
Set CE- VLAN ID 
• 
Set priority on the CE-VLAN  
• 
Set rate limit/bandwidth (CIR) on the service 
• 
Set EIR on the service 
• 
Do VLAN mapping on the service 
• 
Re-classify CoS value on the VLAN 
• 
Set L2CP tunneling as per MEF standard for service 
Results 
□ PASS     □ FAIL    
Comments 
Same as ELINE service 
 
ETX-2i 
3. Applications 
Ethernet Traffic – EVPL Line 
Test Purpose  
Configure and verify EVPL Line service 
Expected 
Results 
• 
Set CoS priority on the VLAN 
• 
Set rate limit/bandwidth (CIR) on the service 
• 
Set EIR on the service 
• 
Do VLAN mapping on the service 
• 
Re-classify CoS value on the VLAN 
• 
Set L2CP tunneling as per MEF standard for service 
Results 
□ PASS     □ FAIL    
Comments 
See scripts below 
Multicos NTU1 
ETX-2I-10G-B# info 
    version "3.01A14" sw "6.4.0(0.27)" 
    configure 
        echo "Management configuration" 
#       Management configuration 
        management 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                target-params "tp1" 
                    message-processing-model snmpv3 
                    version usm 
                    security name "initial" level no-auth-no-priv 
                    no shutdown 
                exit 
                target "MyPC" 
                    target-params "tp1" 
                    address udp-domain 172.17.192.40 
                    no shutdown 
                    tag-list "unmasked" 
                    trap-sync-group 1 
                exit 
            exit 
        exit 
        echo "QoS - Configuration" 
#       QoS - Configuration 
        qos 
            policer-profile "S.Policer_10M.1130" 
ETX-2i 
3. Applications 
                bandwidth cir 10000 cbs 64000 eir 50000 ebs 64000 
            exit 
            shaper-profile "S.Policer_10M.1127" 
                bandwidth cir 19968 cbs 64000 
            exit 
            marking-profile "S.CoS_2_pBit.1248_Rx" color-aware none 
                mark 0..2 to 0 
                mark 3 to 1 
                mark 4 to 0 
                mark 5 to 3 
                mark 6 to 0 
                mark 7 to 5 
            exit 
            queue-block-profile "S.Queue Block Profile.1128" 
                queue 0 
                    scheduling strict 
                exit 
                queue 1 
                    scheduling strict 
                exit 
                queue 2 
                    scheduling strict 
                exit 
                queue 3 
                    scheduling strict 
                exit 
                queue 4 
                    scheduling wfq 3 
                exit 
                queue 5 
                    scheduling wfq 112 
                exit 
                queue 6 
                    scheduling wfq 3 
                exit 
                queue 7 
                    scheduling wfq 3 
                exit 
            exit 
            echo "Queue Group Configuration" 
#           Queue Group Configuration 
            queue-group-profile "DefaultQueueGroup" 
                queue-block 0/3 
                    name "S.Level 0 Queue Block.3" 
                    profile "S.Queue Block Profile.1128" 
                    shaper profile "S.Policer_10M.1127" 
                exit 
            exit 
            queue-map-profile "S.CoS_2_pBit.1131.CC" 
                map 0 to-queue 1 
                map 1 to-queue 7 
                map 2 to-queue 6 
ETX-2i 
3. Applications 
                map 3 to-queue 5 
                map 4 to-queue 4 
                map 5 to-queue 3 
                map 6 to-queue 1 
                map 7 to-queue 0 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            echo "Service Virtual Interface- Port Configuration" 
#           Service Virtual Interface- Port Configuration 
            svi 96 
                no shutdown 
            exit 
            echo "LAG - Port Configuration" 
#           LAG - Port Configuration 
            lag 1 
                bind ethernet 0/1 
                bind ethernet 0/2 
                anchor-port ethernet 0/1 
                no shutdown 
            exit 
        exit 
        echo "Bridge Configuration" 
#       Bridge Configuration 
        bridge 1 
            name "BRIDGE 1" 
        exit 
        echo "Flows Configuration" 
#       Flows Configuration 
        flows 
            echo "Classifier Profile Configuration" 
#           Classifier Profile Configuration 
            classifier-profile "mng_untagged" match-any 
                match untagged 
            exit 
            classifier-profile "mng_all" match-any 
                match all 
            exit 
            classifier-profile "v100" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT_1" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.170_vlan200" match-any 
                match vlan 200 
            exit 
ETX-2i 
3. Applications 
            classifier-profile "S.170_vlan200_1" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.199_1_MUILTICOS" match-any 
                match vlan 600 
            exit 
            classifier-profile "S.199_1_MUILTICOS_1" match-any 
                match vlan 600 p-bit 5 
            exit 
            classifier-profile "S.199_2_MUILTICOS_1" match-any 
                match vlan 600 p-bit 3 
            exit 
            classifier-profile "S.199_3_MUILTICOS_1" match-any 
                match vlan 600 p-bit 1 
            exit 
            classifier-profile "S.199_4_MUILTICOS_1" match-any 
                match vlan 600 p-bit 0 
            exit 
            echo "Flow Configuration" 
#           Flow Configuration 
            flow "mng_access_default_in" 
                classifier "mng_untagged" 
                no policer 
                ingress-port ethernet 0/101 
                egress-port svi 96 
                no shutdown 
            exit 
            flow "mng_access_default_out" 
                classifier "mng_all" 
                no policer 
                ingress-port svi 96 
                egress-port ethernet 0/101 
                no shutdown 
            exit 
            flow "S.169.1_1_1_LT" 
                classifier "S.169_LT" 
                no policer 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue-map-profile "S.CoS_2_pBit.1131.CC" block 0/1 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.169.1_1_LT" 
                classifier "S.169_LT_1" 
                policer profile "S.Policer_10M.1130" 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 5 block 0/3 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
ETX-2i 
3. Applications 
            flow "S.170.1_1_1_vlan200" 
                classifier "S.170_vlan200" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1131.CC" block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_vlan200" 
                classifier "S.170_vlan200_1" 
                no policer 
                vlan-tag push vlan 200 p-bit fixed 5 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.199.1_1_1_MUILTICOS" 
                classifier "S.199_1_MUILTICOS" 
                no policer 
                mark all 
                    vlan 600 
                    marking-profile "S.CoS_2_pBit.1248_Rx" 
                exit 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue-map-profile "S.CoS_2_pBit.1131.CC" block 0/1 
                service-name "MUILTICOS.199" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.199.1_1_MUILTICOS" 
                classifier "S.199_1_MUILTICOS_1" 
                no policer 
                mark all 
                    vlan 600 
                    p-bit 7 
                exit 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 0 block 0/1 
                service-name "MUILTICOS.199" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.199.2_1_MUILTICOS" 
                classifier "S.199_2_MUILTICOS_1" 
                no policer 
                mark all 
                    vlan 600 
                    p-bit 5 
ETX-2i 
3. Applications 
                exit 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "MUILTICOS.199" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.199.3_1_MUILTICOS" 
                classifier "S.199_3_MUILTICOS_1" 
                no policer 
                mark all 
                    vlan 600 
                    p-bit 3 
                exit 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 5 block 0/1 
                service-name "MUILTICOS.199" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.199.4_1_MUILTICOS" 
                classifier "S.199_4_MUILTICOS_1" 
                no policer 
                mark all 
                    vlan 600 
                    p-bit 1 
                exit 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 7 block 0/1 
                service-name "MUILTICOS.199" 
                pm-collection interval 900 
                no shutdown 
            exit 
        exit 
        router 1 
            name "Router#1" 
            interface 1 
                dhcp-client 
                    client-id mac 
                exit 
                shutdown 
            exit 
            interface 32 
                address 172.17.192.105/24 
                bind svi 96 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 0.0.0.0/0 address 172.17.192.1 metric 1 
        exit 
ETX-2i 
3. Applications 
    exit 
 
    configure 
        oam 
            echo "OAM CFM Configuration" 
#           OAM CFM Configuration 
            cfm 
                maintenance-domain 1 
                    md-level 6 
                    no name 
                    maintenance-association 1 
                        name uint 100 
                        mep 101 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.169.1_1_1_LT" 
                            flow uni-direction tx "S.169.1_1_LT" 
                            queue queue-mapping "S.CoS_2_pBit.1131.CC" block 0/3 
                            remote-mep 102 
                            ccm-priority 3 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 10000 
                                delay-var-threshold 3000 
                                classification priority-bit 3 
                                dest-ne 1 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                    maintenance-association 2 
                        name uint 200 
                        mep 101 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.170.1_1_1_vlan200" 
                            flow uni-direction tx "S.170.1_1_vlan200" 
                            queue queue-mapping "S.CoS_2_pBit.1131.CC" block 0/1 
                            remote-mep 102 
                            ccm-priority 5 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 8000 
                                delay-var-threshold 2000 
                                classification priority-bit 5 
                                dest-ne 1 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
ETX-2i 
3. Applications 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                    maintenance-association 3 
                        name uint 600 
                        mep 101 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.199.1_1_1_MUILTICOS" 
                            flow uni-direction tx "S.199.1_1_MUILTICOS" 
                            flow uni-direction tx "S.199.2_1_MUILTICOS" 
                            flow uni-direction tx "S.199.3_1_MUILTICOS" 
                            flow uni-direction tx "S.199.4_1_MUILTICOS" 
                            queue queue-mapping "S.CoS_2_pBit.1131.CC" block 0/1 
                            remote-mep 102 
                            ccm-priority 7 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 6000 
                                classification priority-bit 7 
                                dest-ne 1 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                            service 2 
                                delay-threshold 8000 
                                delay-var-threshold 2000 
                                classification priority-bit 5 
                                dest-ne 1 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                            service 3 
                                delay-threshold 10000 
                                delay-var-threshold 3000 
                                classification priority-bit 3 
                                dest-ne 1 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                            service 4 
                                delay-threshold 15000 
                                delay-var-threshold 4000 
                                classification priority-bit 1 
                                dest-ne 1 
ETX-2i 
3. Applications 
                                    remote mep-id 102 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                exit 
            exit 
        exit 
    exit 
 
 
ETX-2I-10G-B# 
Multicos NTU2 
ETX-2I-10G-B>config>flows# info 
    echo "Classifier Profile Configuration" 
#   Classifier Profile Configuration 
    classifier-profile "mng_untagged" match-any 
        match untagged 
    exit 
    classifier-profile "mng_all" match-any 
        match all 
    exit 
    classifier-profile "v100" match-any 
        match vlan 100 
    exit 
    classifier-profile "S.169.1_LT" match-any 
        match vlan 100 
    exit 
    classifier-profile "S.169_LT_1" match-any 
        match vlan 100 
    exit 
    classifier-profile "S.170.1_vlan200" match-any 
        match vlan 200 
    exit 
    classifier-profile "S.170_vlan200_1" match-any 
        match vlan 200 
    exit 
    classifier-profile "S.199.1_1_MUILTICOS" match-any 
        match vlan 600 
    exit 
    classifier-profile "S.199_1_MUILTICOS_1" match-any 
        match vlan 600 p-bit 5 
    exit 
    classifier-profile "S.199_2_MUILTICOS_1" match-any 
        match vlan 600 p-bit 3 
    exit 
    classifier-profile "S.199_3_MUILTICOS_1" match-any 
        match vlan 600 p-bit 1 
ETX-2i 
3. Applications 
    exit 
    classifier-profile "S.199_4_MUILTICOS_1" match-any 
        match vlan 600 p-bit 0 
    exit 
    echo "Flow Configuration" 
#   Flow Configuration 
    flow "mng_access_default_in" 
        classifier "mng_untagged" 
        no policer 
        ingress-port ethernet 0/101 
        egress-port svi 96 
        no shutdown 
    exit 
    flow "mng_access_default_out" 
        classifier "mng_all" 
        no policer 
        ingress-port svi 96 
        egress-port ethernet 0/101 
        no shutdown 
    exit 
    flow "S.169.1_1_1_LT" 
        classifier "S.169.1_LT" 
        no policer 
        ingress-port ethernet 0/1 
        egress-port ethernet 0/3 queue-map-profile "S.CoS_2_pBit.1125.CC" block 0/1 
        service-name "LT.169" 
        pm-collection interval 900 
        no shutdown 
    exit 
    flow "S.169.1_1_LT" 
        classifier "S.169_LT_1" 
        policer profile "S.Policer_10M.1124" 
        ingress-port ethernet 0/3 
        egress-port ethernet 0/1 queue 5 block 0/3 
        service-name "LT.169" 
        pm-collection interval 900 
        no shutdown 
    exit 
    flow "S.170.1_1_1_vlan200" 
        classifier "S.170.1_vlan200" 
        no policer 
        vlan-tag pop vlan 
        ingress-port ethernet 0/1 
        egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1125.CC" block 0/1 
        service-name "vlan200.170" 
        pm-collection interval 900 
        no shutdown 
    exit 
    flow "S.170.1_1_vlan200" 
        classifier "S.170_vlan200_1" 
        no policer 
        vlan-tag push vlan 200 p-bit fixed 5 
ETX-2i 
3. Applications 
        ingress-port ethernet 0/4 
        egress-port ethernet 0/1 queue 3 block 0/1 
        service-name "vlan200.170" 
        pm-collection interval 900 
        no shutdown 
    exit 
    flow "S.199.1_1_1_MUILTICOS" 
        classifier "S.199.1_1_MUILTICOS" 
        no policer 
        mark all 
            vlan 600 
            marking-profile "S.CoS_2_pBit.1235_Rx" 
        exit 
        ingress-port ethernet 0/1 
        egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1125.CC" block 0/1 
        service-name "MUILTICOS.199" 
        pm-collection interval 900 
        no shutdown 
    exit 
    flow "S.199.1_1_MUILTICOS" 
        classifier "S.199_1_MUILTICOS_1" 
        no policer 
        mark all 
            vlan 600 
            p-bit 7 
        exit 
        ingress-port ethernet 0/4 
        egress-port ethernet 0/1 queue 0 block 0/1 
        service-name "MUILTICOS.199" 
        pm-collection interval 900 
        no shutdown 
    exit 
    flow "S.199.2_1_MUILTICOS" 
        classifier "S.199_2_MUILTICOS_1" 
        no policer 
        mark all 
            vlan 600 
            p-bit 5 
        exit 
        ingress-port ethernet 0/4 
        egress-port ethernet 0/1 queue 3 block 0/1 
        service-name "MUILTICOS.199" 
        pm-collection interval 900 
        no shutdown 
    exit 
    flow "S.199.3_1_MUILTICOS" 
        classifier "S.199_3_MUILTICOS_1" 
        no policer 
        mark all 
            vlan 600 
            p-bit 3 
        exit 
ETX-2i 
3. Applications 
        ingress-port ethernet 0/4 
        egress-port ethernet 0/1 queue 5 block 0/1 
        service-name "MUILTICOS.199" 
        pm-collection interval 900 
        no shutdown 
    exit 
    flow "S.199.4_1_MUILTICOS" 
        classifier "S.199_4_MUILTICOS_1" 
        no policer 
        mark all 
            vlan 600 
            p-bit 1 
        exit 
        ingress-port ethernet 0/4 
        egress-port ethernet 0/1 queue 7 block 0/1 
        service-name "MUILTICOS.199" 
        pm-collection interval 900 
        no shutdown 
    exit 
 
 
ETX-2I-10G-B>config>flows# 
ETX-2I-10G-B>config>flows# 
ETX-2I-10G-B>config>flows# 
ETX-2I-10G-B>config>flows# 
ETX-2I-10G-B>config>flows# 
ETX-2I-10G-B>config>flows# 
ETX-2I-10G-B>config>flows# 
ETX-2I-10G-B# 
ETX-2I-10G-B# 
ETX-2I-10G-B# 
ETX-2I-10G-B# 
ETX-2I-10G-B# info 
    version "3.01A14" sw "6.4.0(0.27)" 
    configure 
        echo "Management configuration" 
#       Management configuration 
        management 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                target-params "tp1" 
                    message-processing-model snmpv3 
                    version usm 
                    security name "initial" level no-auth-no-priv 
                    no shutdown 
                exit 
                target "MyPC" 
                    target-params "tp1" 
                    address udp-domain 172.17.192.40 
                    no shutdown 
                    tag-list "unmasked" 
ETX-2i 
3. Applications 
                    trap-sync-group 1 
                exit 
            exit 
        exit 
        echo "QoS - Configuration" 
#       QoS - Configuration 
        qos 
            policer-profile "S.Policer_10M.1124" 
                bandwidth cir 10000 cbs 64000 eir 50000 ebs 64000 
            exit 
            shaper-profile "S.Policer_10M.1121" 
                bandwidth cir 19968 cbs 64000 
            exit 
            marking-profile "S.CoS_2_pBit.1235_Rx" color-aware none 
                mark 0..2 to 0 
                mark 3 to 1 
                mark 4 to 0 
                mark 5 to 3 
                mark 6 to 0 
                mark 7 to 5 
            exit 
            queue-block-profile "S.Queue Block Profile.1122" 
                queue 0 
                    scheduling strict 
                exit 
                queue 1 
                    scheduling strict 
                exit 
                queue 2 
                    scheduling strict 
                exit 
                queue 3 
                    scheduling strict 
                exit 
                queue 4 
                    scheduling wfq 3 
                exit 
                queue 5 
                    scheduling wfq 112 
                exit 
                queue 6 
                    scheduling wfq 3 
                exit 
                queue 7 
                    scheduling wfq 3 
                exit 
            exit 
            echo "Queue Group Configuration" 
#           Queue Group Configuration 
            queue-group-profile "DefaultQueueGroup" 
                queue-block 0/3 
                    name "S.Level 0 Queue Block.3" 
ETX-2i 
3. Applications 
                    profile "S.Queue Block Profile.1122" 
                    shaper profile "S.Policer_10M.1121" 
                exit 
            exit 
            queue-map-profile "S.CoS_2_pBit.1125.CC" 
                map 0 to-queue 1 
                map 1 to-queue 7 
                map 2 to-queue 6 
                map 3 to-queue 5 
                map 4 to-queue 4 
                map 5 to-queue 3 
                map 6 to-queue 1 
                map 7 to-queue 0 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            echo "Service Virtual Interface- Port Configuration" 
#           Service Virtual Interface- Port Configuration 
            svi 96 
                no shutdown 
            exit 
            echo "LAG - Port Configuration" 
#           LAG - Port Configuration 
            lag 1 
                admin-key ten-giga-ethernet 
                bind ethernet 0/1 
                bind ethernet 0/2 
                anchor-port ethernet 0/1 
                no shutdown 
            exit 
        exit 
        echo "Bridge Configuration" 
#       Bridge Configuration 
        bridge 1 
            name "S.Bridge 1" 
        exit 
        echo "Flows Configuration" 
#       Flows Configuration 
        flows 
            echo "Classifier Profile Configuration" 
#           Classifier Profile Configuration 
            classifier-profile "mng_untagged" match-any 
                match untagged 
            exit 
            classifier-profile "mng_all" match-any 
                match all 
            exit 
            classifier-profile "v100" match-any 
                match vlan 100 
            exit 
ETX-2i 
3. Applications 
            classifier-profile "S.169.1_LT" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.169_LT_1" match-any 
                match vlan 100 
            exit 
            classifier-profile "S.170.1_vlan200" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.170_vlan200_1" match-any 
                match vlan 200 
            exit 
            classifier-profile "S.199.1_1_MUILTICOS" match-any 
                match vlan 600 
            exit 
            classifier-profile "S.199_1_MUILTICOS_1" match-any 
                match vlan 600 p-bit 5 
            exit 
            classifier-profile "S.199_2_MUILTICOS_1" match-any 
                match vlan 600 p-bit 3 
            exit 
            classifier-profile "S.199_3_MUILTICOS_1" match-any 
                match vlan 600 p-bit 1 
            exit 
            classifier-profile "S.199_4_MUILTICOS_1" match-any 
                match vlan 600 p-bit 0 
            exit 
            echo "Flow Configuration" 
#           Flow Configuration 
            flow "mng_access_default_in" 
                classifier "mng_untagged" 
                no policer 
                ingress-port ethernet 0/101 
                egress-port svi 96 
                no shutdown 
            exit 
            flow "mng_access_default_out" 
                classifier "mng_all" 
                no policer 
                ingress-port svi 96 
                egress-port ethernet 0/101 
                no shutdown 
            exit 
            flow "S.169.1_1_1_LT" 
                classifier "S.169.1_LT" 
                no policer 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/3 queue-map-profile "S.CoS_2_pBit.1125.CC" block 0/1 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
ETX-2i 
3. Applications 
            flow "S.169.1_1_LT" 
                classifier "S.169_LT_1" 
                policer profile "S.Policer_10M.1124" 
                ingress-port ethernet 0/3 
                egress-port ethernet 0/1 queue 5 block 0/3 
                service-name "LT.169" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_1_vlan200" 
                classifier "S.170.1_vlan200" 
                no policer 
                vlan-tag pop vlan 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1125.CC" block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.170.1_1_vlan200" 
                classifier "S.170_vlan200_1" 
                no policer 
                vlan-tag push vlan 200 p-bit fixed 5 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "vlan200.170" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.199.1_1_1_MUILTICOS" 
                classifier "S.199.1_1_MUILTICOS" 
                no policer 
                mark all 
                    vlan 600 
                    marking-profile "S.CoS_2_pBit.1235_Rx" 
                exit 
                ingress-port ethernet 0/1 
                egress-port ethernet 0/4 queue-map-profile "S.CoS_2_pBit.1125.CC" block 0/1 
                service-name "MUILTICOS.199" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.199.1_1_MUILTICOS" 
                classifier "S.199_1_MUILTICOS_1" 
                no policer 
                mark all 
                    vlan 600 
                    p-bit 7 
                exit 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 0 block 0/1 
                service-name "MUILTICOS.199" 
ETX-2i 
3. Applications 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.199.2_1_MUILTICOS" 
                classifier "S.199_2_MUILTICOS_1" 
                no policer 
                mark all 
                    vlan 600 
                    p-bit 5 
                exit 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 3 block 0/1 
                service-name "MUILTICOS.199" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.199.3_1_MUILTICOS" 
                classifier "S.199_3_MUILTICOS_1" 
                no policer 
                mark all 
                    vlan 600 
                    p-bit 3 
                exit 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 5 block 0/1 
                service-name "MUILTICOS.199" 
                pm-collection interval 900 
                no shutdown 
            exit 
            flow "S.199.4_1_MUILTICOS" 
                classifier "S.199_4_MUILTICOS_1" 
                no policer 
                mark all 
                    vlan 600 
                    p-bit 1 
                exit 
                ingress-port ethernet 0/4 
                egress-port ethernet 0/1 queue 7 block 0/1 
                service-name "MUILTICOS.199" 
                pm-collection interval 900 
                no shutdown 
            exit 
        exit 
        router 1 
            name "Router#1" 
            interface 32 
                address 172.17.192.106/24 
                bind svi 96 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
ETX-2i 
3. Applications 
            exit 
            static-route 0.0.0.0/0 address 172.17.192.1 metric 1 
        exit 
    exit 
 
    configure 
        oam 
            echo "OAM CFM Configuration" 
#           OAM CFM Configuration 
            cfm 
                maintenance-domain 1 
                    md-level 6 
                    no name 
                    maintenance-association 1 
                        name uint 100 
                        mep 102 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.169.1_1_1_LT" 
                            flow uni-direction tx "S.169.1_1_LT" 
                            queue queue-mapping "S.CoS_2_pBit.1125.CC" block 0/3 
                            remote-mep 101 
                            ccm-priority 3 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 10000 
                                delay-var-threshold 3000 
                                classification priority-bit 3 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                    maintenance-association 2 
                        name uint 200 
                        mep 102 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.170.1_1_1_vlan200" 
                            flow uni-direction tx "S.170.1_1_vlan200" 
                            queue queue-mapping "S.CoS_2_pBit.1125.CC" block 0/1 
                            remote-mep 101 
                            ccm-priority 5 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 8000 
                                delay-var-threshold 2000 
                                classification priority-bit 5 
                                dest-ne 1 
ETX-2i 
3. Applications 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                    maintenance-association 3 
                        name uint 600 
                        mep 102 
                            bind ethernet 0/1 
                            flow uni-direction rx "S.199.1_1_1_MUILTICOS" 
                            flow uni-direction tx "S.199.1_1_MUILTICOS" 
                            flow uni-direction tx "S.199.2_1_MUILTICOS" 
                            flow uni-direction tx "S.199.3_1_MUILTICOS" 
                            flow uni-direction tx "S.199.4_1_MUILTICOS" 
                            queue queue-mapping "S.CoS_2_pBit.1125.CC" block 0/1 
                            remote-mep 101 
                            ccm-priority 7 
                            client-md-level 7 
                            no shutdown 
                            service 1 
                                delay-threshold 6000 
                                classification priority-bit 7 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                            service 2 
                                delay-threshold 8000 
                                delay-var-threshold 2000 
                                classification priority-bit 5 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                            service 3 
                                delay-threshold 10000 
                                delay-var-threshold 3000 
                                classification priority-bit 3 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                            service 4 
                                delay-threshold 15000 
ETX-2i 
3. Applications 
                                delay-var-threshold 4000 
                                classification priority-bit 1 
                                dest-ne 1 
                                    remote mep-id 101 
                                    pm-collection interval 900 
                                exit 
                                no shutdown 
                            exit 
                        exit 
                    exit 
                exit 
            exit 
        exit 
    exit 
 
 
ETX-2I-10G-B# 
ETX-2I-10G-B# 
Monitoring OAM CFM Over Ethernet Services 
Test Purpose 
Configuring OAM service for the Ethernet service (VLAN #) and monitoring the link to  
ETX-2i-10G 
Expected 
Results 
• The MEP functions properly. 
• The Ethernet OAM packets on the service are sent and received correctly between devices. 
• Traffic/service is running properly. 
• Traffic/service is not affected by CFM OAM sessions. 
Results 
□ PASS     □ FAIL    
Comments 
 
RADview  
Test Purpose 
Configuring the catalogs, provisioning the E-LINE services for monitoring and collecting statistics 
to be displayed via Performance Portal.  
Expected 
Results 
• Services OAM CFM are properly monitored and statistics are displayed in the Performance 
Portal. 
• Availability charts, Frame Loss, Frame Delay, and Frame Delay variation are shown. 
Results 
□ PASS     □ FAIL    
ETX-2i 
3. Applications 
Comments 
ETX-2i 
3. Applications 
ETX-2i 
3. Applications 
ETX-2i 
3. Applications 
SAT Y.1564 Performance 
Test Purpose 
The ITU-T Y.1564 testing methodology ensures that quality is maintained across networks with 
multiple streams and different policing parameters. Service providers use the SAC (Service 
Acceptance Criteria) information, which is normally based on a subset of the users’ SLA to set 
pass/fail parameters. There are two main objectives:  
• Validate that each Ethernet-based service is correctly configured.  
• Validate the quality of the services as delivered to the end user. 
ETX-2i 
3. Applications 
Expected 
Results 
Tests service compliance with SLA in two steps: 
• Configuration test – short test, confirming proper configuration of policing, shaping, and 
network connectivity. 
• Performance test – longer test, measuring FLR, FD, FDV, and Availability. 
Results 
□ PASS     □ FAIL    
Comments 
E-LINE service with 10M CIR and EIR: 
Data Collection PM Portal 
Preparing EMS and PM Portals 
 To enable reporting to PM-Portal: 
• 
Add the following command, which configures the interval of the TWAMP sample. 
configure 
reporting 
pm-collection twamp interval 60 
ETX-2i 
3. Applications 
In order to report to PM-Portal, you need to ensure that the SFTP server is running (for example Solaris 
application). 
HsTwamp>config>mngmnt>access# sftp 
 To enable SFTP in RADview: 
1. Open the EMS. 
2. Navigate to Toolssystem consoleEMS Jobs Management (Back End). 
 
3. Create the devices in the Topology. 
ETX-2i 
3. Applications 
TWAMP Policy 
 
Creating Collect Statistics Jobs 
 To create Collect Statistics jobs: 
1. Select the job in the main screen (marked in yellow). 
2. Right click the HS device and select a new job. 
 
3. Select Collect Statistics option 
ETX-2i 
3. Applications 
4. Fill in the name and description. 
5. Select Advanced in order to set the log about the Job. 
6. Select the Recurring time of the Job. 
ETX-2i 
3. Applications 
Binding a TWAMP Session to a Service 
 
 
ETX-2i 
3. Applications 
PM Portal Monitoring 
1. Connect to the PM portal: Open Chrome browser, connect to the Server, and login with 
username root and password root. 
 
 
2. Click Dashboard and select TWAMP.  
There are three colors to identify the status of each parameter in the TWAMP: 
 
Green – Normal 
 
Yellow – Warning 
 
Red – Error 
ETX-2i 
3. Applications 
 
ETX-2i 
3. Applications 
3.  
 
4.  
 
ETX-2i 
3. Applications 
L3 SAT MiNID 
The Layer-3 service activation test (L3 SAT) provides an out-of-service (intrusive) IP/UDP test to assess 
the proper configuration and performance of an IP transport service prior to customer notification and 
delivery. 
The Y.1564 testing methodology gives service providers a standard way of measuring the performance 
of IP transport services. The tests are performed per multiple traffic streams simultaneously, confirming 
policing per EVC or EVC.CoS. 
L3 SAT testing has the following objectives:  
• 
Validates that the IP transport service is correctly configured. 
• 
Validates the quality of the services as delivered to the end user.  
L3 SAT tests can be performed over Layer-3 networks, or as a Layer-3 service over a Layer-2 network. 
Functional Description 
 L3 SAT testing has the following objectives:  
• 
Validate that the IP transport service is correctly configured.  
• 
Validate the quality of the services as delivered to the end user.  
L3 SAT tests can be performed over Layer-3 networks. MiNID L3 SAT supports service performance test.  
Performance Test  
The performance test validates the quality of the services over a user-configurable period of time, as 
follows:  
• 
Traffic is generated for all services at the configured bandwidth level. 
• 
For all the test sessions, test packets are sent simultaneously at 100% of the bandwidth 
configured per test session. 
• 
Per test session, the duration of the performance test is evenly divided between the different 
packet sizes, e.g., per test session, each packet size is transmitted for an equal amount of time. 
The performance test is declared successful if the results are within SAC limits. 
ETX-2i 
3. Applications 
Test Elements  
L3 SAT includes the following elements:  
• 
Generator – initiates multiple test sessions for multiple responders, sends out test and OAM 
frames, receives responses from the responder, processes the resulting measurements, and 
displays test reports. Generator can support two responder types: TWAMP Light and IP Loop.  
• 
Peer – used to run TWAMP test sessions. Only one peer can be configured per generator with IP 
address corresponding to responder. 
• 
Test session – Only one test session can be configured per peer. 
• 
Responders – receive test and OAM frames from generator and transmit responses to 
generator. Responders can be the following types:  
 
TWAMP Light – receives a test packet, reflects the test packet after it, adds an Rx stamp and 
a Tx stamp. 
 
IP loop – filters incoming traffic by destination IP address, and loops it back while 
performing MAC address swap and IP address swap. 
Configuring Static Route 
 
 
ETX-2i 
3. Applications 
Viewing the Configured Router Interface Parameters 
 
 
 
ETX-2i 
3. Applications 
ETX-2i 
3. Applications 
 
Configuring a Controller 
 
ETX-2i 
3. Applications 
Configuring a Peer 
 
Configuring a Peer Profile 
 
 
ETX-2i 
3. Applications 
Viewing L3 SAT Test Status 
 
Viewing L3 SAT Test Reports  
The generator calculates performance parameters according to the received test packets, for the peer 
and its active test session. Some performance parameters are recalculated on the fly (duration, delay, 
ETX-2i 
3. Applications 
PDV, etc.); other parameters are recalculated at the end of the session (lost packets, loss ratio). The 
performance parameters are presented in test reports that can be viewed per peer and test session. 
 
 
ETX-2i 
3. Applications 
 
 
ETX-2i 
3. Applications 
 
ETX-2i 
3. Applications 
Configuring Responder 
 
 
ETX-2i 
3. Applications 
 
 
 
ETX-2i 
3. Applications 
 
ETX-2i 
3. Applications 
 
ETX-2i 
3. Applications 
PM Portal 
 
 
 
ETX-2i 
3. Applications 
Show Chart 
 
3.4 ETX-2i-100G 100G Single Fiber Adaptor 
ETX-2i-100G is an L2 demarcation/aggregation device that can aggregate up to 10 ports of 10GE each 
to/from 100GE link. 
The following capabilities are presented in this POC: 
ETX-2i 
3. Applications 
• 
Two dedicated ports with a low latency path that can be used for connecting eCPRI links 
• 
 Ability to perform Service activation tests to check the links during installation before service is 
up  
• 
Performance monitoring for L3 (TWAMP- Regulation requirement in Japan)   
• 
Advanced traffic management, ability to give priority for different types of traffic, ability to 
shape and police different types of traffic according to the MEF. This HQOS mechanism is an 
enabler for network slicing required for 5G  
The single fiber adaptor, a device in development, uses RAD’s proprietary technology. The device is 
based on an optical component (circulator) and a solution for loop prevention (a loop might occur if all 
traffic generated is reflected to the origin when there is fiber cut). 
We will demonstrate that with the single fiber adaptor we can transfer 100GE bidirectional over single 
fiber. Suggested range for this test is 10 km. 
Note 
Loop prevention mechanism is under development and is not included in this 
demonstration.  
Architecture 
 
ETX-2i 
3. Applications 
Equipment List 
Unit 
Description 
ETX-2i-100G 
ETX CSG device with 2 ports of 100GE and 10 ports of 10GE 
Single Fiber unit A and unit B  
2 passive units for single fiber for 100GE, each unit requires 
QSFP28  
Traffic generator with two 100GE and 16 10GE 
ports 
Traffic generator with capability to tests delays in ns  
ETX-2i-10GE  
ETX device for 10GE (option for aid in additional tests) 
A pair of PCs with video streamer / viewer  
 
The test uses the following: 
 
ETX-2i-100G 
 
100GE Single Fiber Adaptor Prototype 
ETX-2i 
3. Applications 
Objectives 
The following functionalities are covered under the various test cases:  
• 
Two dedicated ports that have a low latency path, which can be used for connecting eCPRI links 
and perform in accordance with expectations 
• 
Present single fiber adaptor and demonstrate that it can fit requirements for single fiber 
transport. 
• 
Carrier Ethernet features for service assurance. We offer to demonstrate the following: 
 
SAT Y.1564 activation test - ability to perform Service activation tests to validate transport 
quality during installation prior service is up  
 
OAM for IP transport using TWAMP (also regulation requirement).  
 
Advanced traffic management, ability to give priority for different types of traffic, ability to 
shape and police different types of traffic (according to the MEF standards).   
Test Cases Description 
Low latency lanes for eCPRI  
In this test case, RAD presents the capability to transfer end to end eCPRI link using a designated port 
using an internal fast lane to achieve a desired minimal latency. We present the latency end to end 
between two ETX-2i-100GE based on frame size 64, 128, 512,1600, 9000 bytes while all the other ports 
aree max loaded.  
• 
Show that there is no impact on the latency due to the load on other ports  
• 
Show avg/max delay per packet size according to the following table: 
No  
Packet size bytes  
Delay on fast lane (via 2 units) * (u sec) 
1 
64  
 
2 
128  
 
3 
512 
 
4 
1600 
 
5 
9000 
 
ETX-2i 
3. Applications 
Single fiber for 100GE  
In this test case, we show that while we use the bookend solution of single fiber for 100G, we can 
transfer 100G full duplex successfully. The single fiber technology that we present is at mockup level 
without loop prevention mechanism.   
The test is performed in two steps: First step we connect the single fiber adaptor bookend solution to an 
IXIA tester for running bidirectional 100GE traffic over single fiber. Error-free run with minimal delay is 
demonstrated. 
Next, the single fiber transmission line solution is connected in between the two ETX-2i-100GE units, as 
illustrated below: 
 
The fast lane delay test is run again as described below. 
No  
Packet size bytes  
Delay on fast lane  
1 
64  
 
2 
128  
 
3 
512 
 
4 
1600 
 
5 
9000 
 
SAT Y.1564 Performance Test Case 
This test case demonstrates how to configure and run Y.1564 (i.e., SAT – Service Activation Test). We will 
demonstrate L3 SAT which seems more adequate to mobile backhaul architecture. The SAT tests the 
Transport SLA compliance in two steps:  
ETX-2i 
3. Applications 
• 
Configuration test: a short test to verify the configuration of the policer, shaper, and network 
connectivity.  
• 
Performance test: a longer duration test, measuring Frame Loss Ratio (FLR), Frame Delay (FD), 
Frame Delay Variation (FDV)  
L3 Performance Measurements (TWAMP) 
Test scenario: Verify TWAMP (RFC-5357) session connectivity between ETX devices. 
TWAMP light session is created from ETX-2i-100GE acting as Controller towards ETX-2-10GE acting as 
responder. 
The main parameters that will be measured are: 
 
• 
Availability 
• 
Packet Loss Ratio (PLR) 
• 
Maximum Delay 
• 
Average Delay  
• 
Delay Threshold Crossing Rate 
• 
Packet Delay Variation 
The statistics can be viewed via CLI. 
Advanced QOS as enabler to network slicing: 
ETX-2I-100GE has an advanced HQOS mechanism which is also enabler for network slicing 
implementation. This use case demonstrates that video traffic can be transmitted smoothly and get high 
priority over other traffic flows, by applying proper policing, scheduling, and shaping configuration.  
ETX-2i 
3. Applications 
Tests Steps 
Test outline proposed: 
Low latency for eCPRI  
Test Purpose 
To check the latency of the traffic that pass via low latency path in ETX-2i-100G (dual fiber 
transport)  
Expected 
Results 
To achieve 11us delay per product. In this setup end to end 22us.   
Results 
□ PASS     □ FAIL    
Comments 
The results were between ~4[us] at 64[Byte] to ~17[us] at 9600[Byte]. 
Detailed report will be sent. 
ETX-2i 
3. Applications 
Single fiber for 100GE  
Test Purpose 
To show that bidirectional traffic in a rate of 100GE can run over single fiber  
Expected 
Results 
  Traffic can pass via 10Km fiber without errors  
Results 
□ PASS     □ FAIL    
Comments 
• Pass without errors. 
• Tested with jumbo 9600B packets. 
• Tested with IMIX packets size. 
• Delay pof ~50us as expected on 10Km fibers. 
Low latency for eCPRI over single fiber transport 
Test Purpose 
Repeat test 3.1 also across the single fiber adaptor devices  
Expected 
Results 
  Traffic can pass via 10Km fiber without errors  
Results 
□ PASS     □ FAIL    
Comments 
Results on short run: 
No  
Packet size 
[bytes]  
Average latency 
on fast 
lane[uSec] 
Max latency on 
fast lane [uSec] 
Max latency – 
50[us] on fast lane 
[uSec] 
1 
64  
53.532 
53.7 
3.7 
2 
128 
53.75 
53.98 
3.98 
3 
512 
54.158 
54.36 
4.36 
4 
1600 
54.762 
55.26 
5.26 
5 
9000 
61.144 
62.26 
12.26 
6 
IMIX 
(64:11,512:10
,1500:7,9216:
18) 
62.603 
63.92 
13.92 
Note: 50us is the 10Km fiber latency. 
Note: The max latency that we saw was ~17[us] on jumbo packets. 
ETX-2i 
3. Applications 
Overnight running on IMIX packets size: 
Results summary -  
Lane 
Avg latency 
[uSec) 
Max latency 
[uSec) 
Fast   lane results 
62.411 
66.22 
Fast   lane results (reverse dir.) 
62.371 
64.6 
Slow lane results 
65.86 
72.12 
SAT Y.1564 Performance 
Test Purpose 
To demonstrate ETX capability to act as SAT generator and responder. There are two main 
objectives for SAT:  
• To validate that each Ethernet-based service is correctly configured  
• To validate the quality of the services as delivered to the end user. 
Expected 
Results 
Demonstrate successful test operation and results presentation: 
• Configuration test – short test, confirming proper configuration of policing, shaping and 
network connectivity 
• Performance test – longer test, measuring FLR, FD, FDV and Availability. 
Results 
□ PASS     □ FAIL    
Comments 
test  
            echo "Configure L3SAT" 
#           Configure L3SAT 
            l3sat  
                echo "L3Sat - Peer Profile Configuration" 
#               L3Sat - Peer Profile Configuration 
                peer-profile "1"  
                    no policing-test  
                    performance-duration custom 5  
                exit 
                echo "L3Sat - Session Profile Configuration" 
#               L3Sat - Session Profile Configuration 
                session-profile "1"  
                    ip-size 1024  
                exit 
                echo "L3SAT - Generator Configuration" 
#               L3SAT - Generator Configuration 
                generator "2"  
                    local-ip-address 192.168.30.30  
                    no shutdown  
                    echo "L3SAT - Controller Peer Configuration" 
#                   L3SAT - Controller Peer Configuration 
                    peer 192.168.30.31  
ETX-2i 
3. Applications 
                        peer-profile "1"  
                        test-session "1" session-profile "1" bw 5000000 dscp 
63  
                    exit 
ETX-2I-100G>config>test>l3sat>generator(2)>peer(192.168.30.31)# show status  
Last Connectivity Sub-test : Passed                         
Last MTU Sub-test          : Not Applicable                 
                                                            
Responder Type             : Loop & Timestamp               
TOD Status                 : Unknown                        
 
Test Name                        LM UDP Ports   DM UDP Ports   Status          
----------------------------------------------------------------------------- 
1                                53249, 53249   53248, 53248   Passed          
 
ETX-2I-100G>config>test>l3sat>generator(2)>peer(192.168.30.31)#  
 
 
ETX-2I-100G>config>test>l3sat>generator(2)>peer(192.168.30.31)# show report 1  
End Points                                               
Generator Address    : 192.168.30.30                     
Responder Address    : 192.168.30.31                     
Responder Type       : Loop & Timestamp                  
LM UDP Ports         : 53249, 53249                      
DM UDP Ports         : 53248, 53248                      
MTU (bytes)          : 1500                              
                                                         
Test                                                     
Scope                : Configuration + Performance       
Peer Profile Name    : 1                                 
Report Type          : No Clock Sync                     
BW (Mbps)            : 5000.000                          
DSCP                 : 63                                
IP Sizes (bytes)     : 1024                              
Session Profile Name : 1                                 
Start Date & Time    : 1970-01-01  02:44:17              
End Date & Time      : 1970-01-01  02:51:03              
Total Duration       : 406                               
Overall Result       : Passed                            
 
 
Configuration Phase 
----------------------------------------------------------------------------- 
Duration (sec)       : 100                            
Configuration Result : Passed                         
 
 
IP Size (bytes) : 1024                           
 
Step Load 
----------------------------------------------------------------------------- 
Parameter            Step#1     Step#2     Step#3     Step#4     Thr      
ETX-2i 
3. Applications 
----------------     --------   --------   --------   --------   -------- 
Tx Rate (Mbps)       1250.011   2500.023   3750.035   5000.047            
IR - mean (Mbps)     1250.011   2500.023   3750.035   5000.047            
PL - count           0          0          0          0                   
PLR                  0          0          0          0          1.000E-3 
PTD - min (ms)       0.059      0.059      0.058      0.056               
PTD - mean (ms)      0.060      0.060      0.060      0.060      200.000  
PTD - max (ms)       0.063      0.063      0.063      0.063               
PTD - std (ms)       0.000      0.000      0.000      0.000               
PDV - mean (ms)      0.001      0.001      0.002      0.004               
PDV - max (ms)       0.004      0.004      0.005      0.007      100.000  
IPDV-Fwd - mean (ms) 0.000      0.000      0.000      0.000               
IPDV-Fwd - max (ms)  0.003      0.003      0.003      0.004               
IPDV-Bck - mean (ms) 0.000      0.000      0.000      0.000               
IPDV-Bck - max (ms)  0.003      0.003      0.004      0.004               
----------------     --------   --------   --------   --------   -------- 
Result               Passed     Passed     Passed     Passed              
 
Policing 
----------------------------------------------------------------------------- 
Parameter            Policing       Thr      
----------------     --------       -------- 
Tx Rate (Mbps)                               
IR - mean (Mbps)                             
PL - count                                   
PLR                  0              1.000E-3 
PTD - min (ms)                               
PTD - mean (ms)                     200.000  
PTD - max (ms)                               
PTD - std (ms)                               
PDV - mean (ms)                              
PDV - max (ms)                      100.000  
IPDV-Fwd - mean (ms)                         
IPDV-Fwd - max (ms)                          
IPDV-Bck - mean (ms)                         
IPDV-Bck - max (ms)                          
----------------     --------       -------- 
Result                                       
 
 
 
 
Performance Phase 
----------------------------------------------------------------------------- 
Duration (min)       : 5                              
Configuration Result : Passed                         
 
Parameter            IP Size #1 IP Size #2 IP Size #3 IP Size #4 Thr        
                     1024 bytes 0 bytes    0 bytes    0 bytes               
----------------     --------   --------   --------   --------   --------   
Duration (min)       5                                                      
Tx Rate (Mbps)       5000.052                                               
ETX-2i 
3. Applications 
IR - mean (Mbps)     5000.052                                               
PL - count           0                                                      
PLR                  0          0          0          0          1.000E-3   
UAS - count          0                                                      
Availability (%)     100.00                                      99.90      
PTD - min (ms)       0.056                                                  
PTD - mean (ms)      0.060                                       200.000    
PTD - max (ms)       0.064                                                  
PTD - std (ms)       0.000                                                  
PDV - mean (ms)      0.004                                                  
PDV - max (ms)       0.008                                       100.000    
IPDV-Fwd - mean (ms) 0.000                                                  
IPDV-Fwd - max (ms)  0.004                                                  
IPDV-Bck - mean (ms) 0.000                                                  
IPDV-Bck - max (ms)  0.004                                                  
PD-Fwd - count       0                                                      
PDR-Fwd              0          0          0          0                     
PD-Bck - count       0                                                      
PDR-Bck              0          0          0          0                     
PR-Fwd - count       0                                                      
PRR-Fwd              0          0          0          0                     
PR-Bck - count       0                                                      
PRR-Bck              0          0          0          0                     
----------------     --------   --------   --------   --------   --------   
Result               Passed      
 
ETX-2I-100G>config>test>l3sat>generator(2)>peer(192.168.30.31)# show summary-
report  
End Points                                            
Generator Address : 192.168.30.30                     
Responder Address : 192.168.30.31                     
Responder Type    : Loop & Timestamp                  
MTU (bytes)       : 1500                              
                                                      
Test                                                  
Scope             : Configuration + Performance       
Peer Profile Name : 1                                 
Start Date & Time : 1970-01-01  02:44:17              
End Date & Time   : 1970-01-01  02:51:03              
Total Duration    : 406                               
Overall Result    : Passed                            
 
Test Name                        BW     DSCP Conf. Result   Perf. Result    
                                 (Mbps)                                     
----------------------------------------------------------------------------- 
1                                5000.0063   Passed         Passed    
ETX-2i 
3. Applications 
L3 Performance Measurements (TWAMP RFC 5357) 
Test Purpose 
To demonstrate ETX capability as generator and responder of TWAMP test. TWAMP is 
generated from ETX-100GE and responded by ETX-10GE through 10km fiber and another ETX-
100GE and vice versa while transmitting full BW data from Ixia. 
Expected 
Results 
Demonstrate successful test operation and results presentation, high deviation results, high 
latency, and losses. 
Results 
□ PASS     □ FAIL    
Comments 
Note: to see losses the fiber was disconnected and re-connected. 
ETX-2I-100G>config>oam>twamp# info 
    echo "TWAMP - Profile Configuration" 
#   TWAMP - Profile Configuration 
    profile "TwampProfile1" 1  
        payload-length 1400  
    exit 
    echo "TWAMP - Controller Configuration" 
#   TWAMP - Controller Configuration 
    controller "3" 3 l2-probe  
        bind ethernet 0/1  
        vlan-tag vlan 206  
        router-entity 1  
        local-ip-address 30.30.30.101  
        no shutdown  
        echo "TWAMP - Controller Peer Configuration" 
#       TWAMP - Controller Peer Configuration 
        peer 30.30.30.30  
            test-session 1 name "TwampTestSession3.1" udp-port 3501 test-
profile "TwampProfile1" dscp 30  
            activate continuous  
        exit 
    exit 
 
ETX-2I-100G>config>oam>twamp>controller(3)>peer(30.30.30.30)# show report 
TwampTestSession3.1 current  
Test Name              : TwampTestSession3.1              
IPPM Type              : TWAMP Light                      
Controller IP Address  : 30.30.30.101 / 52946             
Responder IP Address   : 30.30.30.30 / 3501               
IP DSCP                : 30                               
Payload Length (bytes) : 1400                             
Calculation Mode       : round-trip                       
Start Time             : 1970-01-02 04:11:56              
 
 
Test Interval                       : Current              
Time Stamp                          : 1970-01-02 04:15:01  
Elapsed Time                   (sec): 420                  
ETX-2i 
3. Applications 
Tx Packets                          : 4200         
Loss Packets                        : 329          
Loss Ratio                          : 7.8E-2       
Availability Count             (sec): 420          
 
Duplicate Packets  Fwd / Back       : 0           0            
Duplicate Ratio    Fwd / Back       : 0           0            
Reordered Packets  Fwd / Back       : 0           0            
Reordered Ratio    Fwd / Back       : 0           0            
Fragmented Packets Fwd / Back       : 0           0            
 
Delay Threshold Crossing Count      : 2708                                   
Delay      Min / Max / Average (ms) :   0.163       10.149        2.301      
PDV              Max / Average (ms) :   5.286        2.138                   
IPDV             Max / Average (ms) :   7.034        1.396                   
IPDV-Fwd         Max / Average (ms) :   0.006        0.001                   
IPDV-Back        Max / Average (ms) :   7.039        1.396                   
Advanced QOS as enabler to network slicing 
Test Purpose 
To show the capability of ETX in policing, scheduling, shaping and handling successfully high-
priority traffic (video stream in this demonstration) 
Expected 
Results 
Video will pass smoothly after applying proper policing, scheduling, and shaping to multiple test 
flows  
Results 
□ PASS     □ FAIL    
Comments 
 
ETX-2i 
3. Applications 
policer-profile "5M_5M"  
                bandwidth cir 5000 cbs 64000 eir 5000 ebs 64000  
            exit 
            policer-profile "4M_6M"  
                bandwidth cir 4000 cbs 64000 eir 6000 ebs 64000  
            exit 
            policer-profile "1M_9M"  
                bandwidth cir 1000 cbs 64000 eir 9000 ebs 64000  
            exit 
queue-block-profile "video"  
                queue 0  
                    scheduling strict  
                    depth 49152  
                exit 
                queue 1  
                    depth 49152  
                exit 
                queue 2  
                    scheduling wfq 80  
                    depth 49152  
                exit 
                queue 3  
                    scheduling wfq 20  
                    depth 49152  
                exit 
                queue 4  
                    scheduling wfq 5  
                    depth 49152  
                exit 
queue-group-profile "DefaultQueueGroup"  
                queue-block 0/2  
                    profile "video"  
                    shaper profile "10M"  
                exit 
classifier-profile "v204" match-any  
                match vlan 204  
            exit 
            classifier-profile "v10" match-any  
                match vlan 10  
            exit 
            classifier-profile "v205" match-any  
                match vlan 205  
            exit 
            classifier-profile "v206" match-any  
                match vlan 206  
            exit 
flow "video_in"  
                classifier "all"  
                no policer  
                vlan-tag push vlan 10 p-bit fixed 7  
                ingress-port ethernet 0/10  
                egress-port ethernet 0/1 queue 0 block 0/2  
ETX-2i 
3. Applications 
                no shutdown  
            exit 
            flow "video_out"  
                classifier "v10"  
                policer profile "Policer1"  
                vlan-tag pop vlan  
                ingress-port ethernet 0/1  
                egress-port ethernet 0/10 queue 0 block 0/1  
                no shutdown  
            exit 
            flow "data_in"  
                classifier "v204"  
                policer profile "5M_5M"  
                ingress-port ethernet 0/4  
                egress-port ethernet 0/1 queue 1 block 0/2  
                no shutdown  
            exit 
            flow "data_out"  
                classifier "v204"  
                policer profile "Policer1"  
                ingress-port ethernet 0/1  
                egress-port ethernet 0/4 queue 0 block 0/1  
                no shutdown  
            exit 
            flow "twamp_in"  
                classifier "unt"  
                policer profile "Policer1"  
                ingress-port ethernet 0/11  
                egress-port svi 10  
                no shutdown  
            exit 
            flow "twamp_out"  
                classifier "all"  
                policer profile "Policer1"  
                ingress-port svi 10  
                egress-port ethernet 0/11 queue 0 block 0/1  
                no shutdown  
            exit 
            flow "data_in_205"  
                classifier "v205"  
                policer profile "4M_6M"  
                ingress-port ethernet 0/5  
                egress-port ethernet 0/1 queue 2 block 0/2  
                no shutdown  
            exit 
            flow "data_out_205"  
                classifier "v205"  
                policer profile "Policer1"  
                ingress-port ethernet 0/1  
                egress-port ethernet 0/5 queue 0 block 0/1  
                no shutdown  
            exit 
ETX-2i 
3. Applications 
            flow "data_in_206"  
                classifier "v206"  
                policer profile "1M_9M"  
                ingress-port ethernet 0/6  
                egress-port ethernet 0/1 queue 3 block 0/2  
                no shutdown  
            exit 
            flow "data_out_206"  
                classifier "v206"  
                policer profile "Policer1"  
                ingress-port ethernet 0/1  
                egress-port ethernet 0/6 queue 0 block 0/1  
                no shutdown  
            exit 
Max queue size  
Test Purpose 
To check the actual queue size when transmitting jumbo 9600B packets. 
Expected 
Results 
To demonstrate 8Mb queue size. 
Results 
□ PASS     □ FAIL    
Comments 
Test description: 
• Configured the queue to be closed at the egress side. 
• Packets were injected to the queue by the Ixia.  
• Ixia was stopped and the counters were cleared.   
• Re-open the Queue. 
• The Ixia collected the packets that were stored in queue. 
• Checked with 9600B packets size. 
• Ixia collected 102 packets. (7,833,600[b]) 
Rebooting ETX2i-100G 
Test Purpose 
To check the recovery time of the device after unplugging the power and replugging it.   
Expected 
Results 
Below 5 minutes.   
Results 
□ PASS     □ FAIL    
Comments 
After 1:31 minutes, the traffic passed properly in the device. 
ETX-2i 
3. Applications 
 